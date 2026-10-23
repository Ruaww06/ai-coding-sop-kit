# Agent Installation Guide

SOP content: v4.0. Package: `4.0.0-beta.1`, a **Beta pre-release**. Use tag `v4.0.0-beta.1` and this guide from the same complete source. Deterministic checks passed; v4 native loading, real installation/upgrade behavior and business acceptance remain unverified. Historical observations do not establish this version's behavior.

Installation provides capabilities, not project adoption or permission to develop, commit or publish. Do not change global configuration, permissions or credentials; install clients or dependencies; or start another model process. Stop when the host denies permission.

## 1. Confirm host, project and source

Use the user's selected project and applicable instructions. Check the actual host/version, project root, file access and skill discovery/invocation mechanism. Do not install into a subdirectory merely because it is the current working directory, scan the whole filesystem, or invent paths and commands. Ask when scope or capabilities are unclear.

Documented project-skill mechanisms:

| Host | Mechanism to verify |
| --- | --- |
| Claude Code | `<projectRoot>/.claude/skills/`; invoke the discovered `sop` and confirm its base directory and shared resources. No plugin namespace or startup hook in this form. |
| DeepSeek Harness | `<projectRoot>/.dsh/skills/`; projectRoot is the nearest ancestor containing `.git`, otherwise session cwd. Confirm a mismatch with the selected scope. Invoke the current profile's actual `skill` tool, not an assumed UI command. |
| Other hosts | Verify their real mechanism first. If only explicit file reading is available, propose an authorized stable location and report that limitation; do not call it native discovery or use it to conceal discovery failure. |

These are documented mechanisms, not a cross-host compatibility guarantee. Claude Code local-plugin loading is a separate option in [installation notes](docs/installation.md); do not silently enable both forms.

Use one complete checkout for all files and record its declared version and commit, plus uncommitted changes: HEAD alone does not identify modified content. Obtain tag `v4.0.0-beta.1` from `https://github.com/Ruaww06/ai-coding-sop-kit.git` and read its guide. Confirm all six skills and consistent metadata; stop on incomplete or mixed sources rather than filling gaps from another release. A fetched guide alone is not installation evidence. A verified complete local source is acceptable; record its actual identity.

For an explicitly requested historical release, obtain its guide and complete source from the same real tag; [version history](docs/upgrading.md) lists known sources, including `v3.1.0-beta.2` at `b3f57ee0178e4afb9bbb802f2c4ca5eec27367a7`. Use moving `main` only when the user requests that development source, then read its guide and report its actual version, not an assumed v4. When fetching, use a new authorized source directory, never overwrite an existing one. Do not execute downloaded scripts or tests, use `curl | sh`, or retain staging as a runtime dependency. If network or Git is unavailable, report it; local source inspection is not evidence of the latest public release.

## 2. Check conflicts, then copy

The six skills are `sop`, `sop-requirements`, `sop-design`, `sop-execution`, `sop-verification` and `sop-recovery`. The existing five entry names remain supported; `sop-requirements` is an intended v4 entry, not an extra active leftover. Shared boundaries remain at `sop/references/common.md`; `sop/references/upgrade.md` is loaded only for existing installations, version/form switches or legacy conflicts. Preserve the complete sibling layout, resources and relative links in both project-skill and local-plugin forms.

Reject unexpected extra active SOP skill directories and retired support content; inspect file contents and resolvable references rather than a fixed file count. `sop-startup` remains retired: v4 adds no startup skill. The v2 `sop-requirements` name now refers to a new implementation for semantic clarification and independent requirements review, not permission to retain its old body. Retired v2 references/assets are not required compatibility resources. If the candidate source contains legacy active skills, old support rules or mixed versions, stop before copying and report them; do not silently omit files or disable entries without authorization.

- Before any destination writes, inspect source and destination paths, symlinks, existing same-name content and applicable project rule entries. An old setup may use a different path from the new destination. For an existing installation, version/form switch or legacy conflict, read [the upgrade procedure](skills/sop/references/upgrade.md) and [version differences](docs/upgrading.md) from this source first. Follow explicit project references; report any unresolved scope or loading evidence. Prevent path escape, partial installs and unapproved overwrites. Preview the complete affected switch, including unknown, modified, mixed-origin, extra or incomplete files and conflicting active entries. Same names do not establish equal content.
- An identical complete installation need not be rewritten. Leave unrelated skills alone. Report known copies for other hosts without changing, synchronizing or treating them as this host's loading evidence. State any unknown user-level/plugin precedence.
- Copy only the complete skills and license; the repository license may be placed at `sop/LICENSE`. Do not copy maintainer `AGENTS.md`, `.git`, tests, CI, plugin metadata or hooks into a project-skill installation. Do not replace the project's license.
- Do not automatically rewrite project rules or disable/delete old entries. Obtain authorization for the complete affected switch before overwriting shared files. Never overlay directories as an automatic migration or assume copying removes retired files. Stage outside discovery; an updated plugin path can still coexist with old project skills or embedded rules. Resolve these through the approved plan, not silent filtering or compatibility stubs that keep conflicting rules active. Verify the new source is usable before retiring the only working entry; if isolated loading is unavailable, obtain an explicit reversible switch plan and keep loading pending until observed. This branch is not mandatory for fresh installs.
- Preserve customization, real business records, task/dependency/progress history, approvals, failure counts, unresolved feedback and HOLD/validation records. Filled-in project records are not disposable templates. A software upgrade neither resets approvals or failures nor converts HOLD, missing review or missing verification into completion; it does not start business development.

## 3. Verify and report

Compare installed content with the same source, including all six skills, resources, extra files and license. Actually load `sop` and verify its base directory and shared rules; check that the host discovers the intended entries, including the new `sop-requirements`, from the target source. File existence, discovery, invocation and correct behavior are separate claims. If loading is not observed, report it as unverified; suggest a new session in the same project when needed, without starting another model or changing permissions. Do not claim all six skills' behavior from a single invocation.

V4 adds requirements and design review, persistent task dependencies/progress, and feedback writeback/closure across all stages. When inspecting an adopted v3 project, find actual review evidence for its existing requirements and design: reuse valid reviewed parts, identify missing reviews or changed assumptions, and re-confirm only affected parts. Document presence, old phase names or installation success do not automatically pass review, and migration does not require a full redo. Requirements review needs a non-drafter check; critical design review and final acceptance retain their independent responsibilities. AI agreement is not human approval.

Report host, scope, form, actual version/commit and local changes, paths, content checks, loading evidence, conflicts and limits. Report file installation, host loading and project-rule switching separately. Adoption uses the project's existing persistent records for task dependencies, owners, acceptance/verification, progress and blockers; feedback must retain evidence, route to the responsible decision-maker, write decisions back to the authoritative basis, update affected tasks and invalidate/recheck affected evidence. An issue closes only after the basis, implementation and documents are updated, necessary verification passes and the responsible person confirms. Installation creates neither a mandatory record suite nor business authorization.

After interruption, reread current files and valid authorization; handle only remaining authorized changes, preserve new edits and do not roll back on your own. Report temporary source leftovers; cleanup requires applicable authorization.

Updates are user-initiated and repeat the upgrade procedure, source, conflict and loading checks. Verify that retired entries are inactive, required references resolve, rule-body conflicts are decided and customization/history remain intact; report loading or project switching pending until demonstrated. Before removal, list this installation's directories and local changes and obtain deletion approval. Do not delete the host's whole skills directory, project records or other copies.

## Mechanism references

- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Harness Skills, pinned source](https://github.com/deepseek-ai/deepseek-harness/blob/86a402200d95fecef4529d969836f1fe13c6cb0d/docs/subsystems/skills.zh.md)

These are existing documentation references; host implementations were not rechecked for this candidate. [Design evidence](docs/design.md) and [verification notes](docs/testing.md) may describe historical versions; do not relabel historical observations as v4 candidate tests.
