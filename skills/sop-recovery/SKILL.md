---
name: sop-recovery
description: "Routes problems at any stage through diagnosis, decisions, basis updates and verified closure. Use when requirements or design fail, fixes recur, validation is blocked, a review point arrives, or work resumes or hands off."
---

# Diagnose, Decide and Close the Loop

Read [shared boundaries](../sop/references/common.md). This feedback route applies at any stage, including requirements and design review. Recording a problem is not permission to deliver it as passing.

## Preserve evidence and route the decision

Recover the current baseline, confirmed constraints, authorization, minimal reproduction or counterexample, expected/actual results, failure evidence, attempts and failure counts, outstanding validation and decisions needed. Unknown counts are not zero. Switching agents or sessions does not reset them. If evidence is insufficient, investigate before assigning a cause.

| Evidence points to | Action and responsibility |
| --- | --- |
| Implementation violates clear requirements | Implementation owner fixes within authorization and runs regressions; local problems do not require global redesign |
| Environment or dependency failure | Reproduce and isolate environmental factors and assign recovery; do not mask them with business patches or assume design failure |
| Clear requirements cannot be met by the contract, model or approach | Refer to the design owner; identify the invalidated assumption, impact and checks, revise and review affected design |
| Missing/conflicting business semantics or changed goals/acceptance | Stop dependent work; the requirements owner decides, then review affected requirements |

Use [requirements](../sop-requirements/SKILL.md) or [design](../sop-design/SKILL.md) for the affected review. If both layers are involved, decide business tradeoffs before revising design. Pause affected or dangerous work; unrelated authorized work may continue. Isolate with a minimal reproduction, compare a working path and test one hypothesis at a time.

## Update the basis and redispatch the increment

After the responsible decision, write the decision back to the authoritative requirements, contract, design or rule, retaining reasons and responsibility. Update affected tasks and references; retain reusable invalidated assumptions in the project's knowledge records. A chat-only decision does not close the issue.

Against an identifiable current baseline state **what changes and why, what stays, affected callers/data/tasks/acceptance, invalidated evidence, and revalidation/recovery**. Before editing, the implementer states their understanding of consequential changes; resolve disagreement first. Confirm changes with the responsible owner and review affected parts, without reopening unchanged valid constraints or repeating valid authorization. Do not overwrite current work with an old baseline.

Revalidate affected behavior and necessary regressions; broaden checks if impact is uncertain. **Close only when the basis, affected implementation and documentation are updated, necessary checks pass and the corresponding responsible person confirms closure.** Changing expected results is not a substitute for a requirements decision.

## Stop blind retries

After two consecutive failed fixes of the same problem, stop automatic retries, preserve evidence and refer it for human review. Resume only with new evidence or an approved new approach; switching agents or sessions does not reset the count. Also pause affected implementation for design review on recurring invalidation of the same premise or feedback that repeatedly introduces regressions, even with different symptoms.

Immediately stop affected dangerous operations for security, data-loss or authority risks. Do not hide failure by deleting tests, changing expectations or lowering standards. Stopping still requires investigation, handoff and a next owner/action; it is not completion. Unrelated nonessential existing issues may become separate tasks; current necessary acceptance failures cannot be deferred into a passing result. Retain and investigate flaky failures rather than silently suppressing them.

## Required validation cannot run yet

Use the existing task or issue record to state **what is missing, its impact, a recovery action, an owner, request time and a review point**. Leave unknown assignments or dates unresolved rather than inventing them. Record validation failure separately from unavailable conditions; a local failure is not an external blocker. A nonapplicable check or lower validation strength needs the responsible person's reason; mandatory real-world checks cannot be renamed away.

- The requirements owner may approve continuing unaffected authorized work. This is not a passing result and does not permit merging or release. Until necessary validation is supplied, the feature cannot enter final acceptance as a completed item.
- Scope or acceptance changes need explicit approval and reassessment of remaining risk. Renaming or postponing work cannot waive mandatory safety or compliance requirements.
- Keep pending items visible in project progress. At the review point, decide to resume, replan, change scope or terminate; do not automatically extend it. Repeated deferrals or shared blockers need a resource/plan decision rather than independent endless extensions. Resolve each outstanding validation item at project closure instead of silently marking it complete.

## Resume, hand off and retain knowledge

Carry only useful information: current baseline, confirmed constraints and authorization, progress, minimal reproduction, failure evidence and counts, rejected approaches with reasons, outstanding validation, decisions needed and next responsibility. Exclude credentials, unsanitized data and unrelated full transcripts. Recheck actual files and authorization before resuming.

Retain reusable decisions, recurring failures and important limits with their basis, applicability, verification time and reassessment conditions. Use existing record locations and references elsewhere. Consult before design, check before implementation and update after feedback. Age or infrequent retrieval prompts review, not automatic invalidation; a rejection does not remain valid after its premises change.

Example: validation discovers undefined refund behavior. Preserve the failing scenario, get the business decision, review the changed requirement/design, update the contract and tasks, then implement and revalidate. A missing device permits partial delivery and a recovery plan, not a passing result.
