"""Upgrade text contracts and read-only fixtures, not model behavior tests."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from test_package import EXPECTED, local_links, snapshot

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "tests/migration-cases.json"
PROCEDURE = ROOT / "skills/sop/references/upgrade.md"


class MigrationTests(unittest.TestCase):
    def test_install_contract_protects_scope_and_existing_work(self):
        text = (ROOT / "INSTALL.md").read_text()
        for term in ["authorization", "conflict", "one complete checkout", "global", "LICENSE",
                     "extra active", "retired support content", "history", "loading"]:
            with self.subTest(term=term):
                self.assertIn(term.lower(), text.lower())
        for name in EXPECTED:
            self.assertIn(name, text)
        self.assertNotIn("skills/sop/references/migration.md", text)
        self.assertIn("](skills/sop/references/upgrade.md)", text)
        self.assertIn("](docs/upgrading.md)", text)

    def test_upgrade_is_reachable_before_install_writes(self):
        install = (ROOT / "INSTALL.md").read_text()
        self.assertLess(install.index("skills/sop/references/upgrade.md"),
                        install.index("Copy only the complete skills"))
        entry = (ROOT / "skills/sop/SKILL.md").read_text()
        self.assertIn("](references/upgrade.md)", entry)
        self.assertIn("not required for fresh projects", entry)
        self.assertIn(PROCEDURE, {p.resolve() for p in local_links(ROOT / "skills/sop/SKILL.md")})

    def test_upgrade_contract_requires_a_complete_authorized_switch(self):
        text = PROCEDURE.read_text()
        for term in ["before changing anything", "explicit rule references", "not directory names",
                     "before overwriting shared files", "rule body", "Copying over existing",
                     "outside all host discovery paths", "only working entry", "reversible switch plan",
                     "loading is actually observed", "do not become current approval",
                     "New edits", "retired skills are no longer discoverable",
                     "customization/history remain intact", "pending, partial or verified",
                     "do not automatically roll back", "no-op", "Unknown failure counts"]:
            with self.subTest(term=term):
                self.assertIn(term.lower(), text.lower())
        self.assertNotRegex(text, r"[一-鿿]")

    def test_install_scenarios_have_safe_paths_and_unexecuted_status(self):
        cases = json.loads(CASES.read_text())
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        self.assertTrue(cases)
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertTrue(case["prompt"])
                self.assertTrue(case["assertions"])
                self.assertEqual(case["status"], "not-run")
                self.assertTrue(case["files"])
                for name in case["files"]:
                    path = Path(name)
                    self.assertFalse(path.is_absolute())
                    self.assertNotIn("..", path.parts)
                    self.assertNotIn(".git", path.parts)
        topics = {case["id"] for case in cases}
        self.assertTrue({"install-only", "customized-update", "unknown-host",
                         "mixed-active-skills", "interrupted-update", "same-content-rerun",
                         "loading-unverified", "embedded-rule-conflict",
                         "v1-different-destination", "plugin-plus-project-skills"} <= topics)

    def test_hook_preserves_existing_and_partial_projects(self):
        parent = ROOT / "tmp"
        parent.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="install 空格-", dir=parent) as temp:
            base = Path(temp)
            plugin = base / "插件"
            shutil.copytree(ROOT / "hooks", plugin / "hooks")
            shutil.copytree(ROOT / "skills", plugin / "skills")
            env = dict(os.environ, CLAUDE_PLUGIN_ROOT=str(plugin))
            for case in json.loads(CASES.read_text()):
                with self.subTest(case=case["id"]):
                    project = base / case["id"]
                    project.mkdir()
                    for name, content in case["files"].items():
                        path = project / name
                        path.parent.mkdir(parents=True, exist_ok=True)
                        path.write_text(content)
                    before = snapshot(base)
                    for _ in range(2):
                        result = subprocess.run(["sh", str(plugin / "hooks/session-start.sh")],
                                                cwd=project, env=env, text=True, capture_output=True)
                        self.assertEqual(result.returncode, 0, result.stderr)
                        self.assertIn("Entry skill", result.stdout)
                        self.assertEqual(snapshot(base), before)


if __name__ == "__main__":
    unittest.main()
