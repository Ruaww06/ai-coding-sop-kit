---
name: sop
description: "Use when starting or resuming AI-assisted development under SOP, clarifying task boundaries, adopting the workflow, or choosing the next engineering step. Also use when the user explicitly asks to follow SOP."
---

# SOP Entry

Solve a clear problem with the smallest complete change, and deliver real evidence.

Read [shared boundaries](references/common.md) first. This skill chooses the next action; it does not take over human decisions about goals, tradeoffs, risk acceptance or delivery acceptance. The language of these instructions does not require English replies; follow the user's communication language.

## Start from the actual task

1. Read applicable project rules, relevant code and uncommitted changes. Recover the real goal and authorization. Missing templates do not prevent read-only investigation.
2. Recover from the task or existing requirements: **goal and non-goals, observable acceptance conditions for given situations, permitted code/data/environment changes, validation approach and acceptance responsibility, and unavailable conditions**. Include relevant failures and boundaries without quotas. Require evidence-based performance, capacity or cost numbers only when they affect the approach.
3. Investigate facts available in code, contracts and documentation before asking. Refer consequential ambiguity about product behavior, public contracts, safety or irreversible actions to the responsible human. An unanswered assumption is not approval. Do not request the same valid authorization again.
4. Load the skill needed now. A clear, authorized task with sufficient decisions may go straight to execution; do not force a tour of every stage.

| Need | Skill | Next action |
| --- | --- | --- |
| Unclear approach, new capability, important choice, public contract or data decision | `../sop-design/SKILL.md` | Research, then choose the simplest complete solution |
| Clear goal, necessary decisions and implementation authorization | `../sop-execution/SKILL.md` | Establish the baseline, implement and self-test |
| Validation, cross-acceptance or delivery | `../sop-verification/SKILL.md` | Check expectations and actual evidence |
| Failure, missing validation conditions, resumption or handoff | `../sop-recovery/SKILL.md` | Preserve evidence, stop blind retries and resolve outstanding work |

If installing over an existing setup, switching versions/forms, or encountering conflicting legacy entries, read [the upgrade procedure](references/upgrade.md) before changing files or starting affected business work. This branch is not required for fresh projects or unrelated read-only investigation.

If the goal or consequential authorization is unclear, investigate and clarify here without starting the affected implementation. Execute work with hard dependencies in dependency order.

## Project adoption

Installing or discussing the kit does not adopt the workflow or authorize business changes. On adoption, reuse one clear project entry describing rule locations, permission boundaries, checks and responsible people. Verify the host's actual rule-loading behavior; a declaration is not proof it works.

Do not impose directories, templates, plans, meetings or a state system. A small task can keep its goal, decisions and evidence in one record. Multi-person, cross-session or long-running work needs a persistent plan when useful. Keep one authoritative location for each task status, blocker and decision; reference it elsewhere. Identify material conflicts with older rules and seek human resolution rather than running conflicting workflows together.

## Resources and reporting

- Resolve resources from this skill's directory, not the user's working directory. Use the host's actually discovered skill names, including any namespace; if native invocation is unavailable, read the linked file instead of inventing a command.
- Load only the skills needed now. Treat installed skills as read-only resources; project records belong in the project's established locations.
- Report what changed, why, actual validation results and unresolved items. Missing necessary evidence means partial completion. Passing tests is not product acceptance.

Example: "Explore the project without changes" stays read-only. A clear authorized small fix starts with its baseline, not new requirement, design and dispatch files.
