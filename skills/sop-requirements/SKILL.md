---
name: sop-requirements
description: "Clarifies and reviews requirements for requirements-driven development. Use when a request is vague, a requirements document is not yet reviewed, acceptance is unclear, or product behavior or scope changes."
---

# Define and Review the Right Outcome

Read [shared boundaries](../sop/references/common.md). A complete-looking document is not a reviewed requirement. Reuse valid existing decisions and review evidence; work only on gaps and changes, without fixed templates or question quotas.

## Clarify from facts

1. Read existing requirements, project rules, contracts and relevant implementation before asking. Investigate facts available in the project; ask the requirements owner to resolve consequential business ambiguity. Do not answer on their behalf or treat an option's default as approval.
2. Establish the users, situation, goal and reason; scope and non-goals; main behavior, relevant boundaries, failures and recovery; constraints, dependencies and assumptions; observable acceptance and the conditions needed to check it. Keep terminology consistent. Require evidence-based performance, capacity or cost numbers only when they affect decisions.
3. Acceptance describes given situations and observable results, invariants or concrete experience examples. Include relevant exceptional paths, not a fixed number of assertions. For subjective experience use scenarios and human observation, not fabricated precision. Mark necessary real dependencies, devices or site checks and unavailable conditions.
4. Inspect existing solutions, decisions and failure experience. If feasibility affects a promise, investigate it before commitment. For unfamiliar capabilities or important choices, use [design research](../sop-design/SKILL.md) as needed without treating research as design approval. Record what was actually consulted, applicability and unknowns; do not fabricate sources or rechecks.
5. Keep requirements, acceptance and unresolved decisions in the project's existing authoritative record. Read-only exploration can continue without adopting SOP or creating documents. A prototype must have its question, permitted actions and exit condition defined; its output is not production acceptance.

## Review, not just drafting

The requirements owner confirms business intent. Have someone other than its drafter examine and restate the goal and consequential behavior from user and delivery perspectives. AI may assist; another model does not replace accountable human review.

Check whether:

- Conflicting implementations could both fit the wording, or key terms have different meanings.
- Acceptance distinguishes correct from incorrect behavior, including relevant boundaries and failures.
- Scope, constraints, dependencies and acceptance agree, and necessary research supports the promise.
- Missing conditions, their impact and the person responsible for resolving them are clear.

Retain the **reviewer, conclusion and unresolved items** in the existing record; no meeting or separate report is required. For unresolved consequential ambiguity, conflicting requirements or unjudgeable acceptance, return for clarification rather than coding a guess. Do not invent a reviewer or approval when unavailable.

## Exit and changes

The requirements owner confirms the goal and acceptance; the reviewer finds the requirements judgeable with no unresolved consequential ambiguity; dependencies and validation gaps are explicit. This establishes the requirements baseline, not implementation permission.

Use [design](../sop-design/SKILL.md) for necessary approach decisions, or reuse valid reviewed design for a local task. Changed behavior, scope or acceptance goes through [feedback](../sop-recovery/SKILL.md): update the basis, review affected requirements, identify invalidated evidence and then redispatch the increment. Never silently change acceptance to fit implementation.

Example: an account-deletion specification that omits financial-history retention needs a business decision and review, even if its sections are filled in and implementation looks straightforward.
