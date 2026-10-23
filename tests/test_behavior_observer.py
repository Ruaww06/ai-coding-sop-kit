"""Check behavior-run evidence accounting without invoking any model."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from run_upgrade_behavior import manual, manual_command, observe, snapshot
from run_upgrade_followup import TASK_COMMAND, check as check_followup, launch as launch_followup
from test_package import ROOT


class BehaviorObserverTests(unittest.TestCase):
    def fixture(self):
        parent = ROOT / "tmp"
        parent.mkdir(exist_ok=True)
        directory = tempfile.TemporaryDirectory(prefix="observer-", dir=parent)
        self.addCleanup(directory.cleanup)
        run = Path(directory.name)
        case = run / "preview-v1"
        project = case / "project"
        (project / "candidate/skills/sop").mkdir(parents=True)
        (project / "candidate/skills/sop/SKILL.md").write_text("# Entry\n")
        (project / "candidate/LICENSE").write_text("Package license\n")
        for name in ["tasks.md", "LICENSE", "app.py"]:
            (project / name).write_text("protected\n")
        (project / "AGENTS.md").write_text("public API compatibility must be preserved\n")
        (case / "before.json").write_text(json.dumps(snapshot(project)))
        (run / "source-manifest.json").write_text(json.dumps(snapshot(project / "candidate")))
        return run, case, project

    def test_missing_results_and_model_claims_do_not_establish_loading(self):
        run, case, project = self.fixture()
        first = observe(run, "preview-v1")
        self.assertIsNone(first["result"])
        self.assertTrue(first["read_only_postcondition"])
        (case / "events.jsonl").write_text(json.dumps({"type": "result", "result": "Everything passed"}) + "\n")
        second = observe(run, "preview-v1")
        self.assertFalse(second["exact_current_group"])
        self.assertIn("not inferred", second["native_loading_verdict"])

    def test_protected_edits_and_candidate_edits_are_detected(self):
        run, case, project = self.fixture()
        (project / "tasks.md").write_text("incorrectly marked completed\n")
        (project / "candidate/skills/sop/SKILL.md").write_text("altered\n")
        (case / "events.jsonl").write_text("not-json\n")
        report = observe(run, "preview-v1")
        self.assertFalse(report["read_only_postcondition"])
        self.assertFalse(report["protected_unchanged"]["tasks.md"])
        self.assertFalse(report["candidate_unchanged"])
        self.assertFalse(report["frozen_source_matches"])
        self.assertEqual(report["parse_error_lines"], [1])

    def test_manual_mode_requires_a_real_terminal_before_any_launch(self):
        with patch("run_upgrade_behavior.sys.stdin.isatty", return_value=False), \
                patch("run_upgrade_behavior.subprocess.run") as launch:
            with self.assertRaisesRegex(RuntimeError, "real human-controlled terminal"):
                manual(Path("/unused"), "upgrade-v2")
            launch.assert_not_called()

    def test_manual_command_cannot_automatically_approve_writes(self):
        run, case, project = self.fixture()
        (case / "prompt.txt").write_text("Upgrade the synthetic project only.\n")
        command = manual_command(case)
        self.assertEqual(command[command.index("--permission-mode") + 1], "manual")
        self.assertIn("Bash", command[command.index("--tools") + 1])
        for flag in ["--allowedTools", "--dangerously-skip-permissions", "--restricted", "--print",
                     "--permission-prompts", "--max-budget-usd"]:
            self.assertNotIn(flag, command)

    def followup_fixture(self):
        run, case, project = self.fixture()
        directory = run / "followup"
        directory.mkdir()
        (directory / "project.json").write_text(json.dumps({"path": str(project)}))
        (directory / "baseline.json").write_text(json.dumps(snapshot(project)))
        return directory, project

    def test_followup_rerun_and_task_have_distinct_file_postconditions(self):
        directory, project = self.followup_fixture()
        self.assertTrue(check_followup(directory, "rerun")["file_postconditions_pass"])
        self.assertFalse(check_followup(directory, "task")["file_postconditions_pass"])
        (project / "USAGE.md").write_text(f"# Usage\n```sh\n{TASK_COMMAND}\n```\nOutput: hello\n")
        self.assertFalse(check_followup(directory, "rerun")["file_postconditions_pass"])
        self.assertTrue(check_followup(directory, "task")["file_postconditions_pass"])
        (project / "tasks.md").write_text("incorrectly cleared history\n")
        self.assertFalse(check_followup(directory, "task")["file_postconditions_pass"])

    def test_followup_task_requires_review_not_only_passing_files(self):
        directory, project = self.followup_fixture()
        with patch("run_upgrade_followup.sys.stdin.isatty", return_value=True), \
                patch("run_upgrade_followup.sys.stdout.isatty", return_value=True), \
                patch("run_upgrade_followup.sys.platform", "darwin"), \
                patch("run_upgrade_followup.subprocess.run") as launch:
            with self.assertRaisesRegex(RuntimeError, "Independent rerun review"):
                launch_followup(directory, "task")
            launch.assert_not_called()


if __name__ == "__main__":
    unittest.main()
