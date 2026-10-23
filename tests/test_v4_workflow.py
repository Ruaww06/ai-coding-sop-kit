"""Text contracts for v4 mechanisms; these do not establish model compliance."""
import json
import unittest

from test_package import ROOT


def skill(name):
    return (ROOT / f"skills/{name}/SKILL.md").read_text()


class WorkflowTests(unittest.TestCase):
    def test_requirements_review_is_not_document_completeness(self):
        entry = skill("sop")
        requirements = skill("sop-requirements")
        self.assertIn("../sop-requirements/SKILL.md", entry)
        self.assertIn("not yet reviewed", entry)
        for term in ["someone other than its drafter", "reviewer, conclusion", "return for clarification",
                     "requirements owner", "observable acceptance", "failure experience"]:
            self.assertIn(term, requirements)

    def test_design_requires_review_of_end_to_end_behavior(self):
        text = skill("sop-design")
        for term in ["reviewer, conclusion", "someone other than its drafter", "end-to-end",
                     "requirements review", "return", "counterexample"]:
            self.assertIn(term, text)
        self.assertIn("valid review", skill("sop-execution"))

    def test_execution_keeps_plan_dependencies_and_progress(self):
        text = skill("sop-execution")
        for term in ["predecessors", "owner", "acceptance basis", "validation approach", "status",
                     "persistent plan", "blocked", "next action", "one authoritative"]:
            self.assertIn(term, text)

    def test_feedback_closes_after_basis_and_validation_update(self):
        text = skill("sop-recovery")
        for term in ["any stage", "design owner", "requirements owner", "write the decision back",
                     "review affected", "invalidated evidence", "Close only", "recurring invalidation",
                     "local failure is not an external blocker", "request time"]:
            self.assertIn(term, text)
        self.assertIn("end-to-end", skill("sop-verification"))

    def test_upgrade_keeps_names_history_and_reviews_without_auto_approval(self):
        text = (ROOT / "skills/sop/references/upgrade.md").read_text()
        for term in ["v3", "five", "sop-requirements", "same name", "valid review",
                     "not retroactive approval", "failure counts", "outstanding validation"]:
            self.assertIn(term, text)

    def test_new_behavior_specifications_stay_unexecuted(self):
        cases = json.loads((ROOT / "tests/behavior-cases.json").read_text())
        topics = {case["id"] for case in cases}
        self.assertTrue({"complete-but-unreviewed-requirements", "unreviewed-design",
                         "plan-and-progress", "feedback-writes-back", "recurring-design-failure",
                         "v3-reuse-valid-review"} <= topics)
        self.assertTrue(all(case["status"] == "not-run" for case in cases))


if __name__ == "__main__":
    unittest.main()
