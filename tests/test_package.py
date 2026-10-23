"""Deterministic packaging checks; never start a model or install a plugin."""
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
EXPECTED = {"sop", "sop-design", "sop-execution", "sop-verification", "sop-recovery"}


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
        self.assertEqual(plugin["name"], "ai-coding-sop-kit")
        self.assertEqual(plugin["version"], "3.1.0-beta.1")
        self.assertEqual({p.name for p in (ROOT / ".claude-plugin").iterdir()}, {"plugin.json"})
        for name in ["README.md", "CHANGELOG.md", "INSTALL.md"]:
            self.assertIn(plugin["version"], (ROOT / name).read_text())

    def test_distribution_has_no_legacy_rule_paths(self):
        actual = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        obsolete = sorted(actual - EXPECTED)
        missing = sorted(EXPECTED - actual)
        resources = set((ROOT / "skills/sop").rglob("*.md"))
        allowed = {ROOT / "skills/sop/SKILL.md", ROOT / "skills/sop/references/common.md"}
        stale_resources = sorted(str(p.relative_to(ROOT)) for p in resources - allowed)
        stale_docs = sorted(str(p.relative_to(ROOT)) for p in (ROOT / "docs/sop").rglob("*.md"))
        self.assertFalse(
            obsolete or missing or stale_resources or stale_docs,
            f"Obsolete skills: {obsolete}; missing: {missing}; "
            f"obsolete resources: {stale_resources}; obsolete docs: {stale_docs}",
        )

    def test_skill_metadata_and_english_execution_core(self):
        for name in sorted(EXPECTED):
            path = ROOT / f"skills/{name}/SKILL.md"
            with self.subTest(skill=name):
                text = path.read_text()
                self.assertTrue(text.startswith("---\n"))
                header = text.split("---", 2)[1]
                self.assertEqual(re.search(r"^name: (.+)$", header, re.M).group(1), name)
                value = json.loads(re.search(r"^description: (.+)$", header, re.M).group(1))
                self.assertTrue(value.startswith("Use when"))
                self.assertLessEqual(len(value), 1024)
                self.assertLess(len(text.splitlines()), 100)
                self.assertNotRegex(text, r"[一-鿿]")
        self.assertNotRegex((ROOT / "skills/sop/references/common.md").read_text(), r"[一-鿿]")

    def test_markdown_links_and_fences(self):
        for path in ROOT.rglob("*.md"):
            if any(part in {".git", "tmp", "__pycache__"} for part in path.relative_to(ROOT).parts):
                continue
            with self.subTest(file=str(path.relative_to(ROOT))):
                self.assertEqual(len(re.findall(r"^```", path.read_text(), re.M)) % 2, 0)
                for target in local_links(path):
                    self.assertTrue(target.exists(), f"{path}: missing {target}")

    def test_skills_are_portable_as_a_group(self):
        base = (ROOT / "skills").resolve()
        for path in base.rglob("*.md"):
            for target in local_links(path):
                self.assertTrue(target.resolve().is_relative_to(base), str(target))
        parent = ROOT / "tmp"
        parent.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="skills 空格-", dir=parent) as temp:
            relocated = Path(temp) / "技能"
            shutil.copytree(base, relocated)
            for name in EXPECTED:
                path = relocated / name / "SKILL.md"
                for target in local_links(path):
                    self.assertTrue(target.exists(), str(target))

    def test_hook_configuration(self):
        config = json.loads((ROOT / "hooks/hooks.json").read_text())
        self.assertEqual(set(config["hooks"]), {"SessionStart"})
        item = config["hooks"]["SessionStart"][0]
        self.assertEqual(set(item["matcher"].split("|")), {"startup", "resume", "clear", "compact"})
        self.assertEqual(item["hooks"][0]["command"], 'sh "${CLAUDE_PLUGIN_ROOT}/hooks/session-start.sh"')
        self.assertEqual(item["hooks"][0]["type"], "command")

    def test_bootstrap_is_read_only_relocatable_and_repeatable(self):
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
            env = dict(os.environ, CLAUDE_PLUGIN_ROOT=str(plugin))
            command = ["sh", str(plugin / "hooks/session-start.sh")]
            first = subprocess.run(command, cwd=project, env=env, text=True, capture_output=True)
            second = subprocess.run(command, cwd=project, env=env, text=True, capture_output=True)
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertEqual(first.stdout, second.stdout)
            self.assertIn(str(plugin / "skills/sop/SKILL.md"), first.stdout)
            self.assertIn("Installation is not adoption", first.stdout)
            self.assertEqual(first.stderr, "")
            self.assertEqual(snapshot(base), before)

    def test_bootstrap_reports_missing_root_and_each_resource(self):
        parent = ROOT / "tmp"
        parent.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="missing-", dir=parent) as temp:
            base = Path(temp)
            script = ROOT / "hooks/session-start.sh"
            env = os.environ.copy()
            env.pop("CLAUDE_PLUGIN_ROOT", None)
            result = subprocess.run(["sh", str(script)], env=env, text=True, capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(result.stdout, "")
            # Create partial fixtures instead of deleting any source resources.
            for resource in ["none", "entry-only", "bootstrap-only"]:
                plugin = base / resource
                plugin.mkdir()
                if resource == "entry-only":
                    entry = plugin / "skills/sop/SKILL.md"
                    entry.parent.mkdir(parents=True)
                    entry.write_text("# Entry\n")
                if resource == "bootstrap-only":
                    guidance = plugin / "hooks/bootstrap.md"
                    guidance.parent.mkdir()
                    guidance.write_text("Read-only navigation.\n")
                env["CLAUDE_PLUGIN_ROOT"] = str(plugin)
                result = subprocess.run(["sh", str(script)], env=env, text=True, capture_output=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertIn("missing", result.stderr)

    def test_behavior_cases_are_unexecuted_observable_specifications(self):
        cases = json.loads((ROOT / "tests/behavior-cases.json").read_text())
        self.assertTrue(cases)
        self.assertEqual(len({case["id"] for case in cases}), len(cases))
        for case in cases:
            self.assertTrue(case["prompt"])
            self.assertIn(case["expected_skill"], EXPECTED)
            self.assertTrue(case["assertions"])
            self.assertEqual(case["status"], "not-run")
        expected_topics = {
            "explore-only", "clear-small-task", "research-before-choice", "same-session-self-test",
            "independent-expectations", "incremental-invalidation", "resume-keeps-counts",
            "blocked-validation", "no-automatic-extension", "untrusted-authorization",
        }
        self.assertTrue(expected_topics <= {case["id"] for case in cases})


if __name__ == "__main__":
    unittest.main()
