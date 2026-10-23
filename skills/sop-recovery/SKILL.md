---
name: sop-recovery
description: "Use when fixes fail repeatedly, assumptions break, required validation is blocked, a review date arrives, or work must resume or hand off across sessions."
---

# Stop Blind Fixes, Keep Responsibility

Read [shared boundaries](../sop/references/common.md). Preserve failure evidence before choosing the next action. Recording a problem is not permission to deliver it as passing.

## Diagnose and stop losses

Recover the current baseline, confirmed constraints, authorization, minimal reproduction, failure evidence, attempts and failure counts, outstanding validation and decisions needed. Unknown counts are not zero. Switching agents or sessions does not reset them.

| Evidence points to | Action |
| --- | --- |
| Implementation violates clear requirements | Fix within authorization and run regressions |
| Environment or dependency failure | Reproduce and isolate environmental factors; do not mask them with business patches |
| Invalid contract, model or approach | Revise the affected design and state the increment before implementing again |
| Missing or conflicting requirements | Stop affected implementation and refer to the requirements owner |

Isolate the issue with a minimal reproduction, compare a working project path and test one hypothesis at a time. Do not repeat the same patch without new evidence.

After two consecutive failed fixes of the same problem, stop automatic retries, preserve evidence and refer it for human review. Resume only with new evidence or an approved new approach; switching agents or sessions does not reset the count. Immediately stop affected dangerous operations for security, data-loss or authority risks. Do not hide failure by deleting tests, changing expectations or lowering standards.

## Required validation cannot run yet

Use the existing task or issue record to state **what is missing, its impact, a recovery action, an owner and a review point**. Explicitly leave unknown assignments or dates unresolved rather than inventing them. Record validation failure separately from unavailable conditions; a local failure is not an external blocker.

- The requirements owner may approve continuing unaffected authorized work. This is not a passing result and does not permit merging or release. Until necessary validation is supplied, the feature cannot enter final acceptance as a completed item.
- Scope or acceptance changes need explicit approval and reassessment of remaining risk. Renaming or postponing work cannot waive mandatory safety or compliance requirements.
- At the review point, decide to resume, replan, change scope or terminate; do not automatically extend it. Resolve each outstanding validation item at project closure instead of silently marking it complete.

## Resume, hand off and retain knowledge

Carry only useful information: current baseline, confirmed constraints and authorization, minimal reproduction, failure evidence and counts, rejected approaches with reasons, outstanding validation and decisions needed. Exclude credentials, unsanitized data and unrelated full transcripts.

For incremental redispatch, state what changes/stays, affected callers/acceptance and invalidated evidence. Confirm consequential changes before proceeding without re-explaining unchanged constraints. Check current files and valid authorization; do not overwrite new work with an old baseline.

Retain reusable decisions, recurring failures and important limits with their basis, applicability, verification time and reassessment conditions. Use the project's existing record locations and references elsewhere. Age or infrequent retrieval prompts review, not automatic invalidation; a rejection does not remain valid after its premises change.

Example: a missing device permits an honest partial-delivery report and a follow-up plan, not "passed next week." A task with two failed fixes needs investigation or an approved new approach after handoff, not a fresh retry count.
