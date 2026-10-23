---
name: sop-execution
description: "Plans and implements the smallest complete authorized change with self-tests and visible progress. Use when requirements and necessary design have valid review conclusions and implementation, a fix or refactoring is authorized."
---

# Smallest Complete Change

Read [shared boundaries](../sop/references/common.md). Same-session self-tests are allowed; they do not replace non-implementer cross-acceptance. Resolve missing necessary decisions or authorization without requiring a particular file or using this skill to bypass consequential ambiguity.

## Plan before editing

Confirm a valid review of requirements and necessary design, plus implementation authorization; reuse unchanged reviewed baselines. A clear task or design draft alone is not review evidence. Use [requirements](../sop-requirements/SKILL.md) or [design](../sop-design/SKILL.md) for missing decisions without forcing new files.

Before first dispatch, associate each single-result task with its predecessors, owner, acceptance basis, validation approach and status. Respect hard dependencies. One task record suffices for a small change; dependent, collaborative or cross-session work needs a persistent plan. Have the responsible person confirm validation strength by risk, not an AI-selected downgrade.

Keep progress observable: what is complete, active, blocked or in feedback, and the next action and responsible person. Update changes promptly; summarize at handoff or agreed review points without mandatory meetings. Use one authoritative location for task status and one for each issue; summarize by reference, not duplicated details. Estimation and full scheduling methods are outside this requirement.

- Recover the goal, non-goals, acceptance, implementation authorization and responsibilities. Read project rules, target code, callers, contracts, tests and comparable implementations; reference relevant research and decisions. Check relevant failure knowledge before implementation and report what was consulted and applicable, not merely 'searched'.
- Establish the baseline of relevant checks before modification. Preserve existing changes and distinguish pre-existing failures from new ones. If a baseline is unavailable, report it as unknown, not passing. Search and read selectively rather than loading unrelated files wholesale.
- Identify the full necessary impact before minimizing edits. Split by a single verifiable result, not file counts or conversation turns; execute hard dependencies in order.

## Alternate implementation and self-tests

1. Tie each edit to the task or a necessary dependency. Do not tidy unrelated names, formatting, comments or architecture. Remove only unused items caused by this change; report unrelated existing issues separately.
2. Preserve others' work. Do not overwrite, delete or restore historical state without authorization. If a necessary edit exceeds scope, explain the impact and obtain approval; neither exceed authority nor deliberately omit the edit.
3. Follow the design's reuse choice and project layers and conventions. Do not swallow errors or remove validation or valid assertions to get green checks. Follow contracts for retries, fallback and errors. Simplification must retain trust-boundary validation, security, data protection, accessibility and necessary hardware calibration.
4. For a bug, preserve a failing reproduction first. Leave an automated regression when feasible; otherwise record repeatable reproduction steps and verification limits. For refactoring, establish the behavior to preserve first. Add appropriate tests for nontrivial new logic.
5. Reuse real project checks, execute them and read the results. Record the relevant version and environment. Distinguish unexecuted checks, failures and unavailable conditions; test doubles do not prove real-dependency behavior.
6. Problems at any stage use [feedback](../sop-recovery/SKILL.md), not a patch that silently changes business behavior. For changed requirements or design, update the authoritative basis, state what changes/stays, affected callers/acceptance and invalidated evidence against the current baseline, and obtain affected review and approval first. Revalidate affected checks and necessary regressions; broaden validation if impact cannot be bounded reliably.
7. Put temporary artifacts in the project's designated isolated location. Inspect targets before cleanup; client caches and others' files are not your own artifacts.

## Stop and hand over

After two consecutive failed fixes of the same problem, stop automatic retries, preserve evidence and refer it for human review. Resume only with new evidence or an approved new approach. Switching agents or sessions does not reset the count. Immediately stop affected dangerous operations for security, data-loss or authority risks. Do not hide failure by deleting tests, changing expectations or lowering standards. Use [recovery](../sop-recovery/SKILL.md) for diagnosis, missing conditions or handoff.

Recurring invalidation of one design premise or new regressions from repeated feedback also require pausing affected implementation for design review, even if each failure looks different. When the authorized implementation is complete, relevant checks have run, progress is current, and changes and unverified items are traceable, use [verification](../sop-verification/SKILL.md). Missing necessary validation means partial completion; do not approve final acceptance yourself.

Example: retain an existing failing baseline rather than patching business code to hide an environment problem. A public-contract change needs the relevant approval and affected callers, not a deliberately incomplete "surgical" edit.
