---
name: sop-verification
description: "Checks independent expectations, executed evidence and responsible acceptance. Use when validating a change, preparing cross-acceptance or delivery, or about to claim completion or passing checks."
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
6. Trace each applicable acceptance condition to the current reviewed requirements and actual evidence. For full-stack behavior, check the end-to-end scenario across affected layers; separate frontend/backend unit passes are insufficient. Review critical assertion sources and repeatability, not just coverage. Check authorization, changed scope and necessary documentation. A path or dependency restriction is a programmatic gate only with real checks and blocking actions; do not claim enforcement without a checker.
7. A discovered requirement or design defect uses [feedback](../sop-recovery/SKILL.md): obtain the responsible decision, update the basis and review affected changes before revalidation. Do not revise expectations merely to match implementation.

## Cross-acceptance and delivery

Distinguish implementer self-tests, AI-assisted review, non-implementer cross-acceptance and acceptance by the acceptance owner. A fresh session or another model does not automatically establish independent evidence or replace a responsible person. The implementer must not handle final acceptance alone.

Report **what changed, why, applicable acceptance, actual validation results, unresolved items and next responsibility**. Update affected requirements, contracts, design and usage documentation; reference valid unchanged records. For runnable deliverables provide reproducible startup and usage steps rather than handing necessary testing to the user. Missing necessary validation means partial completion; use [recovery](../sop-recovery/SKILL.md) to record recovery actions, owner and review point. Propose task-aligned commit splits and messages when needed; execute only with authorization.

Completion requires evidence for all applicable acceptance conditions, passing affected regressions, necessary documentation updates, completed non-implementer cross-acceptance and acceptance by the acceptance owner. Submitting material is not acceptance. Passing tests is not product acceptance; acceptance does not authorize merging or release.

Example: structural and script checks establish only their checked properties. If host behavior was not exercised, report it as unverified rather than claiming installation success or method effectiveness.
