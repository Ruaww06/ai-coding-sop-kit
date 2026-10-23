---
name: sop-verification
description: "Use when running project validation, assessing acceptance evidence, preparing cross-acceptance or delivery, or about to claim a task is complete or a check passed."
---

# Evidence Before Delivery

Read [shared boundaries](../sop/references/common.md). Answer separately: Is the expectation justified? Did the check actually run? Has delivery been accepted? One answer does not substitute for another.

## Check the basis and results

1. Inspect the actual artifact version, diff, confirmed acceptance and pre-change baseline, not just the implementer's summary.
2. Derive expectations from requirements, external specifications, business truth, verified references or invariants, not by reverse-engineering the implementation. Humans confirm business and risk tradeoffs. AI may derive expectations from a clear specification and cite it; humans need not write every assertion.
3. Choose validation by consequences, with human confirmation—not fixed test tiers:
   - Local low-risk changes: directly check the result and affected regressions; do not mechanically add tests.
   - Behavior changes: cover main flows, relevant boundaries and failures; add contract or integration checks as impact requires.
   - High-risk changes: a competent technical reviewer confirms the approach, including security, invariants, real dependencies and recovery; use sampled mutation or fault injection when needed.
4. Reuse project check entry points. Actually execute checks, read results and exit status, and record commands/operations, outcomes, code version and relevant environment. Distinguish failure, unavailable conditions and unexecuted checks. Verify that old evidence still applies; revalidate affected checks after changes and broaden regression when impact is uncertain.
5. Check subjective experience with concrete scenarios, reference examples and human observation, not fabricated numerical precision. Doubles can isolate or inject faults but cannot stand in for real-dependency or device evidence. Coverage, static checks and model agreement alone cannot establish correctness.
6. Check authorization, changed scope and necessary documentation. A path or dependency restriction is a programmatic gate only with real checks and blocking actions; do not claim enforcement without a checker.

## Cross-acceptance and delivery

Distinguish implementer self-tests, AI-assisted review, non-implementer cross-acceptance and acceptance by the acceptance owner. A fresh session or another model does not automatically establish independent evidence or replace a responsible person. The implementer must not handle final acceptance alone.

Report **what changed, why, actual validation results and unresolved items**. Missing necessary validation means partial completion; use [recovery](../sop-recovery/SKILL.md) to record recovery actions, owner and review point.

Completion requires evidence for all applicable acceptance conditions, passing affected regressions, necessary documentation updates, completed non-implementer cross-acceptance and acceptance by the acceptance owner. Submitting material is not acceptance. Passing tests is not product acceptance; acceptance does not authorize merging or release.

Example: structural and script checks establish only their checked properties. If host behavior was not exercised, report it as unverified rather than claiming installation success or method effectiveness.
