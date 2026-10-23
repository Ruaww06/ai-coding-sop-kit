---
name: sop-design
description: "Use when an authorized task needs an approach, unfamiliar capability, important technology choice, public contract or data decision, or reassessment of an existing design."
---

# Research Before Choosing

Read [shared boundaries](../sop/references/common.md). Scale design work to its impact, not a mandatory architecture/model/ADR package. Investigate and clarify an unclear goal or consequential ambiguity; do not treat assumptions as approval.

## Find existing solutions

1. Inspect existing project implementations, relevant decisions and failure experience. For a new capability, important choice, unfamiliar domain or an approach worth reconsidering, also consult mature implementations, official documentation and existing evaluations. Research can challenge the current approach, not merely fill gaps.
2. Answer: **What solutions already exist? Under what conditions do they apply? How does this project differ?** Do not manufacture candidates to meet a quota, substitute popularity for evidence or adopt another project's conclusions as this project's results.
3. Record actual sources, access time, applicable versions, key conclusions and unknowns. Reuse still-valid research without pretending to have rechecked it. Verify consequential facts; never assume an unverified fact that affects safety or the design's viability. Humans decide business and risk tradeoffs.
4. Use research conclusions in the choice. Preserve rejection reasons and applicability conditions, avoiding both repeated exploration and permanent rejection detached from its premises. Use existing task or design records, not a new ledger.

## Choose the simplest complete solution

Choose the first option in this order that completely solves the problem:

1. **Is anything new necessary?** Do not add unrequested features, options or extensibility. Clarify the core use when the request is vague.
2. **Does the project already have it?** Reuse functions, components, services or patterns as surrounding code does.
3. **Can the standard library or platform do it?** Use it directly; prefer the project's established implementation when one exists.
4. **Can an installed dependency do it?** Use existing dependencies; do not add one for a few lines.
5. **Can it be a one-liner understood at a glance?** If so, do not expand it. A line that takes effort to decode is not simple.
6. **Otherwise, write the minimum necessary code.** If a new dependency is genuinely needed, explain why and obtain the relevant approval.

Identify everything that must change before minimizing the change: code, callers, data and tests. Do not build frameworks for one-off logic or add unrequested wrappers and configuration. Preserve established layers, interfaces and conventions; moving or merging code must retain validation and error handling. Explain a simpler alternative's tradeoffs; obtain human approval if it changes confirmed requirements.

## Challenge consequential decisions

Front-load only decisions that affect others or are hard to reverse: public interfaces and error semantics, data ownership and lifecycle, permissions, transactions and consistency, important dependencies, migration and recovery. Leave local reversible organization to implementation.

For each consequential decision, state **the conditions it relies on, a counterexample that would invalidate it, and how to check**. Consider dependency failure, data invariants, concurrency and scale as relevant. "Scalable" and "reliable" are not concrete constraints.

Record what the change needs: inputs/outputs/errors/compatibility/callers for public behavior; invariants/migration/failure/recovery for data; reasons/important alternatives/exit cost for substantial choices. Reference valid records; do not create empty documents when no corresponding change exists.

For an incremental change, state against the current baseline: what changes, what stays, affected callers and acceptance, and which evidence becomes invalid. Confirm consequential changes before implementation without re-explaining unchanged constraints. Split work by a single verifiable result; respect hard dependencies.

## Exit

The impact is identified, necessary research has a basis, consequential choices and viability conditions are confirmed, and necessary contracts, validation and recovery approaches are available. With sufficient existing decisions, proceed to execution. Design approval alone does not authorize implementation.

Example: inspect project code and failure experience for an existing-interface fix. For new storage, also research mature options, applicable versions, data constraints and migration recovery—not just popular products.
