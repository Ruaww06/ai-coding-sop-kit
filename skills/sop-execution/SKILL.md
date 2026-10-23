---
name: sop-execution
description: "Use when implementing, fixing or refactoring an authorized task whose goal, acceptance, necessary decisions, scope and acceptance responsibility are clear."
---

# Smallest Complete Change

Read [shared boundaries](../sop/references/common.md). Same-session self-tests are allowed; they do not replace non-implementer cross-acceptance. Resolve missing necessary decisions or authorization without requiring a particular file or using this skill to bypass consequential ambiguity.

## Before editing

- Recover the goal, non-goals, acceptance, implementation authorization and responsibilities. Read project rules, target code, callers, contracts, tests and comparable implementations; reference relevant research and decisions.
- Establish the baseline of relevant checks before modification. Preserve existing changes and distinguish pre-existing failures from new ones. If a baseline is unavailable, report it as unknown, not passing. Search and read selectively rather than loading unrelated files wholesale.
- Identify the full necessary impact before minimizing edits. Split by a single verifiable result, not file counts or conversation turns; execute hard dependencies in order.

## Alternate implementation and self-tests

1. Tie each edit to the task or a necessary dependency. Do not tidy unrelated names, formatting, comments or architecture. Remove only unused items caused by this change; report unrelated existing issues separately.
2. Preserve others' work. Do not overwrite, delete or restore historical state without authorization. If a necessary edit exceeds scope, explain the impact and obtain approval; neither exceed authority nor deliberately omit the edit.
3. Follow the design's reuse choice and project layers and conventions. Do not swallow errors or remove validation or valid assertions to get green checks. Follow contracts for retries, fallback and errors. Simplification must retain trust-boundary validation, security, data protection, accessibility and necessary hardware calibration.
4. For a bug, preserve a failing reproduction first. Leave an automated regression when feasible; otherwise record repeatable reproduction steps and verification limits. For refactoring, establish the behavior to preserve first. Add appropriate tests for nontrivial new logic.
5. Reuse real project checks, execute them and read the results. Record the relevant version and environment. Distinguish unexecuted checks, failures and unavailable conditions; test doubles do not prove real-dependency behavior.
6. For changed requirements or design, state what changes/stays, affected callers/acceptance and invalidated evidence against the current baseline. Confirm consequential changes first. Revalidate affected checks and necessary regressions; broaden validation if impact cannot be bounded reliably.
7. Put temporary artifacts in the project's designated isolated location. Inspect targets before cleanup; client caches and others' files are not your own artifacts.

## Stop and hand over

After two consecutive failed fixes of the same problem, stop automatic retries, preserve evidence and refer it for human review. Resume only with new evidence or an approved new approach. Switching agents or sessions does not reset the count. Immediately stop affected dangerous operations for security, data-loss or authority risks. Do not hide failure by deleting tests, changing expectations or lowering standards. Use [recovery](../sop-recovery/SKILL.md) for diagnosis, missing conditions or handoff.

When the authorized implementation is complete, relevant checks have run, and changes and unverified items are traceable, use [verification](../sop-verification/SKILL.md). Missing necessary validation means partial completion; do not approve final acceptance yourself.

Example: retain an existing failing baseline rather than patching business code to hide an environment problem. A public-contract change needs the relevant approval and affected callers, not a deliberately incomplete "surgical" edit.
