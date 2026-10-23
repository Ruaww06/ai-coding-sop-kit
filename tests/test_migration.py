"""Install/update text contracts and read-only fixtures, not model behavior tests."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from test_package import EXPECTED, snapshot

ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "tests/migration-cases.json"


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
        self.assertNotIn("docs/sop/", text)

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
                         "mixed-active-skills", "interrupted-update", "same-content-rerun"} <= topics)

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
