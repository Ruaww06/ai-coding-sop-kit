"""Real published-file regressions, not a simulated migrator or Agent test.

Tests materialize Git blobs inside isolated repository tmp directories. They
exercise additive copy and reference resolution only; no extracted code runs.
"""
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

from test_package import EXPECTED, ROOT, local_links

PUBLISHED = {
    "v1.0": "d2b5049f9fb84353b3f848926acc0c690e71caf5",
    "v2.0.0-beta.1": "e2246a60c1e10d8214587c66c28b129dee387092",
    "v3.1.0-beta.1": "62f612e4466cf2f3c7420fb5d7acade00492deec",
}


@unittest.skipUnless(shutil.which("git"), "Git required for published-file regressions")
class PublishedUpgradeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.trees = {}
        for ref, commit in PUBLISHED.items():
            check = subprocess.run(["git", "cat-file", "-e", f"{ref}^{{commit}}"],
                                   cwd=ROOT, capture_output=True)
            if check.returncode:
                raise unittest.SkipTest(f"Published tag {ref} unavailable; no network fetch attempted")
            actual = subprocess.check_output(["git", "rev-parse", f"{ref}^{{commit}}"],
                                             cwd=ROOT, text=True).strip()
            if actual != commit:
                raise AssertionError(f"Published tag {ref} changed: {actual}")
            cls.trees[ref] = subprocess.check_output(
                ["git", "ls-tree", "-rz", "--full-tree", ref], cwd=ROOT).split(b"\0")

    def workspace(self):
        parent = ROOT / "tmp"
        parent.mkdir(exist_ok=True)
        temp = tempfile.TemporaryDirectory(prefix="published upgrade 空格-", dir=parent)
        self.addCleanup(temp.cleanup)
        return Path(temp.name)

    def materialize(self, ref, destination, prefixes):
        for entry in self.trees[ref]:
            if not entry:
                continue
            metadata, encoded_path = entry.split(b"\t", 1)
            mode, kind, oid = metadata.split()
            name = encoded_path.decode()
            if not any(name == p or name.startswith(p.rstrip("/") + "/") for p in prefixes):
                continue
            path = Path(name)
            self.assertFalse(path.is_absolute())
            self.assertNotIn("..", path.parts)
            self.assertEqual(kind, b"blob")
            self.assertIn(mode, {b"100644", b"100755"})
            target = destination / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(subprocess.check_output(["git", "cat-file", "blob", oid.decode()], cwd=ROOT))

    def copy_current_skills(self, destination):
        shutil.copytree(ROOT / "skills", destination, dirs_exist_ok=True)

    def test_v2_additive_copy_leaves_retired_skills_and_resources(self):
        project = self.workspace()
        self.materialize("v2.0.0-beta.1", project, ["skills"])
        old_files = {p.relative_to(project / "skills") for p in (project / "skills").rglob("*") if p.is_file()}
        new_files = {p.relative_to(ROOT / "skills") for p in (ROOT / "skills").rglob("*") if p.is_file()}
        retired = old_files - new_files
        self.assertTrue(retired)
        self.copy_current_skills(project / "skills")
        self.assertTrue((project / "skills/sop-startup/SKILL.md").is_file())
        self.assertTrue((project / "skills/sop-requirements/SKILL.md").is_file())
        self.assertTrue((project / "skills/sop/assets/task.md").is_file())
        self.assertTrue((project / "skills/sop/references/gates.md").is_file())
        self.assertTrue(all((project / "skills" / p).is_file() for p in retired))
        for name in EXPECTED:
            self.assertEqual((project / f"skills/{name}/SKILL.md").read_bytes(),
                             (ROOT / f"skills/{name}/SKILL.md").read_bytes())

    def test_clean_support_with_retained_old_skills_has_broken_links(self):
        project = self.workspace()
        self.copy_current_skills(project / "skills")
        self.materialize("v2.0.0-beta.1", project,
                         ["skills/sop-startup", "skills/sop-requirements"])
        missing = []
        for name in ["sop-startup", "sop-requirements"]:
            path = project / f"skills/{name}/SKILL.md"
            missing.extend(target for target in local_links(path) if not target.exists())
        self.assertTrue(missing, "Old skills must not be mistaken for compatible aliases")
        self.assertTrue(any(p.name == "stages.md" for p in missing))
        self.assertTrue(any("assets" in p.parts for p in missing))

    def test_v1_new_destination_leaves_active_old_references_and_customization(self):
        project = self.workspace()
        self.materialize("v1.0", project, ["AGENTS.md", ".agents/skills/sop", "docs/sop", "LICENSE"])
        agents = project / "AGENTS.md"
        original = agents.read_text()
        self.assertIn("docs/sop/workflow.md", original)
        self.assertIn(".agents/skills/sop/SKILL.md", original)
        custom = "\nProject-specific requirement: preserve API compatibility.\n"
        agents.write_text(original + custom)
        (project / "tasks.md").write_text("Two failed fixes; required device validation not executed.\n")
        history = (project / "tasks.md").read_bytes()
        shutil.copy2(project / "LICENSE", project / "docs/sop/LICENSE")
        license_before = (project / "docs/sop/LICENSE").read_bytes()
        self.copy_current_skills(project / ".claude/skills")
        self.assertEqual(agents.read_text(), original + custom)
        self.assertEqual((project / "tasks.md").read_bytes(), history)
        self.assertEqual((project / "docs/sop/LICENSE").read_bytes(), license_before)
        self.assertTrue((project / ".agents/skills/sop/SKILL.md").is_file())
        self.assertTrue((project / "docs/sop/workflow.md").is_file())

    def test_v2_v1_style_document_copy_does_not_supply_root_skills(self):
        project = self.workspace()
        self.materialize("v2.0.0-beta.1", project, [".agents/skills/sop", "docs/sop"])
        redirect = project / ".agents/skills/sop/SKILL.md"
        broken = [p for p in local_links(redirect) if not p.exists()]
        self.assertIn(project / "skills/sop/SKILL.md", [p.resolve() for p in broken])
        for name in ["workflow", "templates"]:
            links = list(local_links(project / f"docs/sop/{name}.md"))
            self.assertTrue(any(not p.exists() for p in links))

    def test_previous_v3_group_is_complete_but_lacks_upgrade_resource(self):
        project = self.workspace()
        self.materialize("v3.1.0-beta.1", project, ["skills"])
        actual = {p.parent.name for p in (project / "skills").glob("*/SKILL.md")}
        self.assertEqual(actual, EXPECTED)
        for path in (project / "skills").rglob("*.md"):
            for target in local_links(path):
                self.assertTrue(target.exists())
        self.assertFalse((project / "skills/sop/references/upgrade.md").exists())
        self.copy_current_skills(project / "skills")
        self.assertTrue((project / "skills/sop/references/upgrade.md").exists())
        first = {p.relative_to(project): p.read_bytes() for p in project.rglob("*") if p.is_file()}
        self.copy_current_skills(project / "skills")
        self.assertEqual(first, {p.relative_to(project): p.read_bytes() for p in project.rglob("*") if p.is_file()})


if __name__ == "__main__":
    unittest.main()
