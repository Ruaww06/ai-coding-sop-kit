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

    def test_execution_loads_stop_rules_before_implementation(self):
        text = (ROOT / "skills/sop-execution/SKILL.md").read_text()
        reading = text.split("## 操作", 1)[0]
        self.assertIn("../sop/references/feedback.md", reading)
        self.assertIn("两轮", (ROOT / "skills/sop/references/feedback.md").read_text())

    def test_pending_H_record_is_distinct_from_approval(self):
        skill = (ROOT / "skills/sop-recovery/SKILL.md").read_text()
        rules = (ROOT / "skills/sop/references/recovery.md").read_text()
        for text in [skill, rules]:
            self.assertIn("待裁决", text)
            self.assertIn("无写入授权", text)
            self.assertIn("不标 HOLD", text)
            self.assertIn("人批准 H 后", text)
            self.assertIn("拒绝", text)
        self.assertNotIn("人判定后即写", skill)

    def test_knowledge_location_uses_confirmed_project_entry(self):
        text = (ROOT / "skills/sop/references/feedback.md").read_text()
        self.assertIn("启动记录中确认的唯一知识库位置", text)
        self.assertIn("尚无约定", text)
        self.assertNotIn("唯一登记在 `docs/knowledge/`", text)

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
