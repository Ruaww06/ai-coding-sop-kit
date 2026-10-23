"""Regression checks for review findings; no models, installs or remote Git calls."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RegressionTests(unittest.TestCase):
    def workspace(self):
        parent = ROOT / "tmp"
        parent.mkdir(exist_ok=True)
        directory = tempfile.TemporaryDirectory(prefix="review-", dir=parent)
        self.addCleanup(directory.cleanup)
        return Path(directory.name)

    def test_execution_contains_stop_rules_without_loading_another_stage(self):
        text = (ROOT / "skills/sop-execution/SKILL.md").read_text()
        self.assertIn("two consecutive failed fixes", text)
        self.assertIn("stop automatic retries", text)
        self.assertIn("new evidence or an approved new approach", text)
        self.assertIn("does not reset the count", text)
        self.assertIn("Immediately stop", text)

    def test_missing_validation_does_not_grant_acceptance_or_release(self):
        text = (ROOT / "skills/sop-recovery/SKILL.md").read_text()
        for term in ["what is missing", "its impact", "a recovery action", "an owner",
                     "a review point", "not a passing result", "does not permit merging or release",
                     "cannot enter final acceptance", "do not automatically extend",
                     "project closure", "explicit approval"]:
            with self.subTest(term=term):
                self.assertIn(term, text)
        self.assertIn("local failure is not an external blocker", text)

    def test_knowledge_is_conditional_not_automatically_expired(self):
        text = (ROOT / "skills/sop-recovery/SKILL.md").read_text()
        self.assertIn("existing record locations", text)
        self.assertIn("basis, applicability, verification time and reassessment conditions", text)
        self.assertIn("not automatic invalidation", text)

    def test_research_enters_choice_and_preserves_applicability(self):
        text = (ROOT / "skills/sop-design/SKILL.md").read_text()
        for term in ["project implementations", "failure experience", "mature implementations",
                     "actual sources, access time, applicable versions", "still-valid research",
                     "Use research conclusions in the choice", "rejection reasons and applicability",
                     "counterexample", "which evidence becomes invalid"]:
            self.assertIn(term, text)

    def test_independent_expectations_and_human_acceptance_are_distinct(self):
        common = (ROOT / "skills/sop/references/common.md").read_text()
        verify = (ROOT / "skills/sop-verification/SKILL.md").read_text()
        self.assertIn("same session", common)
        self.assertIn("not by reverse-engineering the implementation", verify)
        self.assertIn("must not handle final acceptance alone", verify)
        self.assertIn("Passing tests is not product acceptance", verify)
        self.assertIn("does not authorize merging or release", verify)
        self.assertIn("only with real checks and blocking actions", verify)

    def test_small_tasks_have_no_template_or_approval_ritual(self):
        text = (ROOT / "skills/sop/SKILL.md").read_text()
        self.assertIn("Missing templates do not prevent read-only investigation", text)
        self.assertIn("may go straight to execution", text)
        self.assertIn("Do not impose directories, templates, plans, meetings", text)
        self.assertIn("Do not request the same valid authorization again", text)
        common = (ROOT / "skills/sop/references/common.md").read_text()
        self.assertIn("task data", common)
        self.assertIn("do not grant authority", common)
        self.assertIn("private code or unsanitized data", common)

    def test_markdown_validation_under_tmp_ancestor(self):
        base = self.workspace() / "tmp" / "checkout"
        tests = base / "tests"
        tests.mkdir(parents=True)
        shutil.copy2(ROOT / "tests/test_package.py", tests / "test_package.py")
        # These are excluded relative to the checkout, not because of its parent.
        for folder in ["tmp", ".git", "__pycache__"]:
            (base / folder).mkdir()
            (base / folder / "ignored.md").write_text("```\n[bad](missing.md)\n")
        command = [os.sys.executable, "-B", str(tests / "test_package.py"),
                   "PackageTests.test_markdown_links_and_fences"]
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
        readme = base / "README.md"
        readme.write_text("# Valid\n")
        result = subprocess.run(command, cwd=base, env=env, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        for content in ["[broken](missing.md)\n", "```python\n"]:
            readme.write_text(content)
            result = subprocess.run(command, cwd=base, env=env, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0, "Broken Markdown was silently skipped")
            self.assertIn("FAIL", result.stderr)

    @unittest.skipUnless(shutil.which("git"), "Git required for committed-patch regression")
    def test_CI_checks_committed_push_PR_and_initial_patches(self):
        script = ROOT / ".github/scripts/check-whitespace.sh"
        self.assertTrue(script.is_file(), "Missing commit-range checker")
        workflow = (ROOT / ".github/workflows/test.yml").read_text()
        self.assertIn("fetch-depth: 0", workflow)
        self.assertIn("github.event.pull_request.base.sha", workflow)
        self.assertIn("github.event.pull_request.head.sha", workflow)
        self.assertIn("github.event.before", workflow)
        self.assertIn(".github/scripts/check-whitespace.sh", workflow)
        base = self.workspace()
        env = dict(os.environ, GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                   GIT_AUTHOR_NAME="Fixture", GIT_AUTHOR_EMAIL="fixture@example.invalid",
                   GIT_COMMITTER_NAME="Fixture", GIT_COMMITTER_EMAIL="fixture@example.invalid")

        def git(*args):
            return subprocess.check_output(["git", *args], cwd=base, env=env, text=True).strip()

        def check(before, after, event, forced="false"):
            return subprocess.run(["sh", str(script), before, after, event, forced], cwd=base,
                                  env=env, capture_output=True, text=True)

        git("init", "-q")
        (base / "file.md").write_text("clean\n")
        git("add", "file.md")
        git("commit", "-qm", "baseline")
        start = git("rev-parse", "HEAD")
        zero = "0" * 40
        self.assertEqual(check(zero, start, "push").returncode, 0)
        # Bad whitespace is already committed: checking only the worktree misses it.
        (base / "file.md").write_text("bad  \n")
        git("add", "file.md")
        git("commit", "-qm", "bad whitespace")
        bad = git("rev-parse", "HEAD")
        self.assertEqual(git("status", "--porcelain"), "")
        self.assertEqual(git("diff", "--check"), "")
        self.assertNotEqual(check(start, bad, "push").returncode, 0)
        self.assertNotEqual(check(zero, bad, "push").returncode, 0)
        self.assertNotEqual(check(start, bad, "pull_request").returncode, 0)
        # New target-branch whitespace is not part of a clean PR's patch.
        git("checkout", "-q", "--detach", start)
        (base / "feature.md").write_text("clean feature\n")
        git("add", "feature.md")
        git("commit", "-qm", "clean feature")
        feature = git("rev-parse", "HEAD")
        self.assertEqual(check(bad, feature, "pull_request").returncode, 0)
        self.assertNotEqual(check("f" * 40, feature, "push").returncode, 0)
        self.assertEqual(check("f" * 40, feature, "push", "true").returncode, 0)
        self.assertNotEqual(check("f" * 40, bad, "push", "true").returncode, 0)
        self.assertNotEqual(check("f" * 40, feature, "pull_request", "true").returncode, 0)
        self.assertIn("github.event.forced", workflow)


if __name__ == "__main__":
    unittest.main()
