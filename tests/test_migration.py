"""Migration protocol contracts and read-only hook checks, not Agent migration tests."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from test_package import snapshot

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / "skills/sop/references/migration.md"
CASES = ROOT / "tests/migration-cases.json"


class MigrationTests(unittest.TestCase):
    def test_install_and_skills_share_the_shipped_protocol(self):
        links = {
            "INSTALL.md": "skills/sop/references/migration.md",
            "skills/sop/SKILL.md": "references/migration.md",
            "skills/sop-startup/SKILL.md": "../sop/references/migration.md",
            "docs/sop/migration-v2.md": "../../skills/sop/references/migration.md",
        }
        for name, link in links.items():
            text = (ROOT / name).read_text()
            self.assertIn(f"]({link})", text, name)
            self.assertEqual(((ROOT / name).parent / link).resolve(), PROTOCOL)
        install = (ROOT / "INSTALL.md").read_text()
        self.assertLess(install.index("**先只读识别旧项目。**"), install.index("**复制整组。**"))
        self.assertIn("## 旧项目迁移分支", install)
        for term in ["AGENTS.md", "CLAUDE.md", "docs/sop/", ".agents/skills/sop/SKILL.md",
                     "项目未迁移", "加载待验证", "中断或重跑", "同名旧技能被加载"]:
            self.assertIn(term, install)
        entry = (ROOT / "skills/sop/SKILL.md").read_text()
        self.assertLess(entry.index("references/migration.md"), entry.index("已采用且没有未解决"))
        startup = (ROOT / "skills/sop-startup/SKILL.md").read_text()
        self.assertLess(startup.index("references/migration.md"), startup.index("assets/startup.md"))
        self.assertIn("迁移授权不自动包含后续启动补齐", startup)

    def test_protocol_keeps_authorization_history_and_recovery_boundaries(self):
        text = PROTOCOL.read_text()
        # These guardrails are a text contract; they do not prove a model follows it.
        for term in ["只有路径", "符号链接", "未验证", "版本证据", "逐文件差异",
                     "拒绝或暂缓", "加载待验证", "不得撤下唯一可用旧入口",
                     "失败次数", "HOLD", "Known Issues", "不能清零",
                     "不整文件替换", "旧 `.agents/skills/sop/SKILL.md`", "活动入口",
                     "许可证", "预览基线", "新的用户改动", "有效授权",
                     "已完成且一致的步骤不重写", "不擅自删除新文件",
                     "没有冲突的 v1/v2 双路由", "不代表业务测试",
                     "显式读取已核验，原生发现不适用", "绕过宿主原生发现失败",
                     "旧规约主体", "交人裁决"]:
            with self.subTest(term=term):
                self.assertIn(term, text)
        template = (ROOT / "skills/sop/assets/startup.md").read_text()
        for term in ["来源 commit", "迁移授权", "保留定制与历史", "恢复动作"]:
            self.assertIn(term, template)

    def test_scenarios_have_safe_paths_and_explicit_unexecuted_status(self):
        cases = json.loads(CASES.read_text())
        expected = {"v1-install-only", "v1-customized-preview", "unknown-same-path",
                    "mixed-active-entry", "interrupted-migration-new-edit",
                    "already-migrated-rerun", "authorized-targeted-migration"}
        self.assertEqual({case["id"] for case in cases}, expected)
        self.assertEqual(len(cases), len(expected))
        by_id = {case["id"]: case for case in cases}
        for name in ["mixed-active-entry", "authorized-targeted-migration"]:
            self.assertIn("小任务可省不适用产物", by_id[name]["files"]["AGENTS.md"])
            self.assertTrue(any("未经裁决" in item for item in by_id[name]["assertions"]))
        self.assertTrue(any("无原生发现机制" in item
                            for item in by_id["already-migrated-rerun"]["assertions"]))
        for case in cases:
            with self.subTest(case=case["id"]):
                self.assertTrue(case["prompt"])
                self.assertTrue(case["expected_state"])
                self.assertEqual(case["expected_skill"], "sop-startup")
                self.assertEqual(case["status"], "not-run")
                self.assertGreaterEqual(len(case["assertions"]), 3)
                self.assertTrue(case["files"])
                for name in [*case["files"], *case["allowed_project_changes"]]:
                    path = Path(name)
                    self.assertFalse(path.is_absolute())
                    self.assertNotIn("..", path.parts)
                    self.assertNotIn(".git", path.parts)
                if case["id"] != "authorized-targeted-migration":
                    self.assertEqual(case["allowed_project_changes"], [])

    def test_hook_preserves_legacy_customized_and_partial_projects(self):
        # Run only the real hook, never a fake detector or a simulated migration.
        parent = ROOT / "tmp"
        parent.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="migration 空格-", dir=parent) as temp:
            base = Path(temp)
            plugin = base / "插件"
            shutil.copytree(ROOT / "hooks", plugin / "hooks")
            shutil.copytree(ROOT / "skills", plugin / "skills")
            self.assertTrue((plugin / "skills/sop/references/migration.md").is_file())
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
