"""Deterministic packaging tests; never start an LLM or install a plugin."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "sop", "sop-startup", "sop-requirements", "sop-design",
    "sop-execution", "sop-verification", "sop-recovery",
}


def local_links(path):
    for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^\s)]+)\)", path.read_text()):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        yield path.parent / unquote(target.split("#", 1)[0])


def snapshot(directory):
    return {
        str(p.relative_to(directory)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in directory.rglob("*") if p.is_file()
    }


class PackageTests(unittest.TestCase):
    def test_manifests_and_version(self):
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(plugin["name"], "ai-coding-sop-kit")
        self.assertRegex(plugin["version"], r"^\d+\.\d+\.\d+(?:-[a-z0-9.]+)?$")
        self.assertEqual(market["plugins"][0]["name"], plugin["name"])
        self.assertEqual(market["plugins"][0]["source"], "./")
        self.assertNotIn("version", market["plugins"][0])
        for name in ["README.md", "CHANGELOG.md", "docs/sop/migration-v2.md"]:
            self.assertIn(plugin["version"], (ROOT / name).read_text())

    def test_skill_metadata(self):
        paths = list((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual({p.parent.name for p in paths}, EXPECTED)
        for path in paths:
            with self.subTest(skill=path.parent.name):
                text = path.read_text()
                self.assertTrue(text.startswith("---\n"))
                header = text.split("---", 2)[1]
                name = re.search(r"^name: (.+)$", header, re.M).group(1)
                description = re.search(r"^description: (.+)$", header, re.M).group(1)
                self.assertEqual(name, path.parent.name)
                self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
                self.assertLessEqual(len(name), 64)
                value = json.loads(description)
                self.assertTrue(value.startswith("Use when"))
                self.assertLessEqual(len(value), 1024)
                self.assertLess(len(text.splitlines()), 100)

    def test_markdown_links_and_fences(self):
        for path in ROOT.rglob("*.md"):
            if any(part in {".git", "tmp", "__pycache__"} for part in path.relative_to(ROOT).parts):
                continue
            with self.subTest(file=str(path.relative_to(ROOT))):
                self.assertEqual(len(re.findall(r"^```", path.read_text(), re.M)) % 2, 0)
                for target in local_links(path):
                    self.assertTrue(target.exists(), f"{path}: missing {target}")

    def test_skills_are_portable_as_a_group(self):
        # A skills-only install must not require the repository docs or working directory.
        base = (ROOT / "skills").resolve()
        for path in base.rglob("*.md"):
            for target in local_links(path):
                self.assertTrue(target.resolve().is_relative_to(base), str(target))
        self.assertEqual(len(list(base.glob("sop/assets/*.md"))), 13)
        self.assertEqual(len(list(base.glob("sop/references/*.md"))), 8)

    def test_docs_are_indexes_not_duplicate_rules(self):
        for name in ["workflow", "templates"]:
            text = (ROOT / f"docs/sop/{name}.md").read_text()
            self.assertIn("索引", text)
            self.assertNotIn("```markdown", text)
        legacy = (ROOT / ".agents/skills/sop/SKILL.md").read_text()
        self.assertIn("../../../skills/sop/SKILL.md", legacy)
        self.assertIn("disable-model-invocation: true", legacy)

    def test_hook_configuration(self):
        config = json.loads((ROOT / "hooks/hooks.json").read_text())
        self.assertEqual(set(config["hooks"]), {"SessionStart"})
        item = config["hooks"]["SessionStart"][0]
        self.assertEqual(set(item["matcher"].split("|")), {"startup", "resume", "clear", "compact"})
        self.assertEqual(item["hooks"][0]["command"], 'sh "${CLAUDE_PLUGIN_ROOT}/hooks/session-start.sh"')
        self.assertEqual(item["hooks"][0]["type"], "command")

    def test_bootstrap_is_read_only_relocatable_and_repeatable(self):
        # Keep temporary files inside the gitignored repository test area.
        parent = ROOT / "tmp"
        parent.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="plugin 空格-", dir=parent) as temp:
            base = Path(temp)
            plugin = base / "插件 副本"
            project = base / "业务 项目"
            project.mkdir()
            (project / "AGENTS.md").write_text("Do not overwrite this project rule.\n")
            shutil.copytree(ROOT / "hooks", plugin / "hooks")
            shutil.copytree(ROOT / "skills", plugin / "skills")
            before = snapshot(base)
            env = os.environ.copy()
            env["CLAUDE_PLUGIN_ROOT"] = str(plugin)
            command = ["sh", str(plugin / "hooks/session-start.sh")]
            first = subprocess.run(command, cwd=project, env=env, text=True, capture_output=True)
            second = subprocess.run(command, cwd=project, env=env, text=True, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(first.stdout, second.stdout)
            self.assertIn(str(plugin / "skills/sop/SKILL.md"), first.stdout)
            self.assertIn("Installation is not project adoption", first.stdout)
            self.assertEqual(first.stderr, "")
            self.assertEqual(snapshot(base), before)

    def test_bootstrap_reports_missing_root_and_resources(self):
        env = os.environ.copy()
        env.pop("CLAUDE_PLUGIN_ROOT", None)
        script = ROOT / "hooks/session-start.sh"
        result = subprocess.run(["sh", str(script)], env=env, text=True, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        env["CLAUDE_PLUGIN_ROOT"] = str(ROOT / "tests/no-such-plugin")
        result = subprocess.run(["sh", str(script)], env=env, text=True, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("missing", result.stderr)

    def test_behavior_cases_are_unique_and_have_observable_checks(self):
        cases = json.loads((ROOT / "tests/behavior-cases.json").read_text())
        self.assertGreaterEqual(len(cases), 6)
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        for case in cases:
            self.assertTrue(case["prompt"])
            self.assertIn(case["expected_skill"], EXPECTED)
            self.assertGreaterEqual(len(case["assertions"]), 2)
            self.assertEqual(case["status"], "not-run")


if __name__ == "__main__":
    unittest.main()
