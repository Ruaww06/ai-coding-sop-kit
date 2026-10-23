# Agent Installation Guide

SOP content: v3.1. Package: `3.1.0-beta.1`, a beta test release. Real-host installation and model behavior remain unverified. Report the actual version and commit obtained; fetching a guide alone does not establish installation success.

Installation provides capabilities, not project adoption or permission to develop, commit or publish. Do not change global configuration, permissions or credentials; install clients or dependencies; or start another model process. Stop when the host denies permission.

## 1. Confirm host, project and source

Use the user's selected project and applicable instructions. Check the actual host/version, project root, file access and skill discovery/invocation mechanism. Do not install into a subdirectory merely because it is the current working directory, scan the whole filesystem, or invent paths and commands. Ask when scope or capabilities are unclear.

Documented project-skill mechanisms:

| Host | Mechanism to verify |
| --- | --- |
| Claude Code | `<projectRoot>/.claude/skills/`; invoke the discovered `sop` and confirm its base directory and shared resources. No plugin namespace or startup hook in this form. |
| DeepSeek Harness | `<projectRoot>/.dsh/skills/`; projectRoot is the nearest ancestor containing `.git`, otherwise session cwd. Confirm a mismatch with the selected scope. Invoke the current profile's actual `skill` tool, not an assumed UI command. |
| Other hosts | Verify their real mechanism first. If only explicit file reading is available, propose an authorized stable location and report that limitation; do not call it native discovery or use it to conceal discovery failure. |

These are documented mechanisms, not verified installations of this candidate. Claude Code local-plugin loading is a separate option in [installation notes](docs/installation.md); do not silently enable both forms.

Use one complete checkout for all files and record its version and commit. For a local candidate, also report uncommitted changes: HEAD alone does not identify modified content. The public repository is `https://github.com/Ruaww06/ai-coding-sop-kit.git`. For this release, use tag `v3.1.0-beta.1` and read this guide from that same tag. Use moving `main` only when the user requests the development version, then read its guide and report its actual version. When fetching, use a new authorized source directory, never overwrite an existing one. Do not execute downloaded scripts or tests, use `curl | sh`, or retain staging as a runtime dependency. If network or Git is unavailable, report it; a verified local source is acceptable, not evidence of the latest release.

## 2. Check conflicts, then copy

The skills are `sop`, `sop-design`, `sop-execution`, `sop-verification` and `sop-recovery`, with only `sop/references/common.md` as shared support. If a source contains legacy active skills or retired resources, stop before copying and report the leftovers. Do not silently omit extra active `sop-*` skills or disable existing entries without authorization.

For a clean source, install the intended skills together as sibling directories, preserving resources and relative links. Reject unexpected active SOP skill directories and retired support content; check file contents and resolvable references rather than a fixed file count.

- Inspect source and destination paths, symlinks and existing same-name content. Prevent path escape, partial installs and unapproved overwrites. List differences and ask about modified, extra, incomplete or unknown files and conflicting active entries.
- An identical complete installation need not be rewritten. Leave unrelated skills alone. Report known copies for other hosts without changing, synchronizing or treating them as this host's loading evidence. State any unknown user-level/plugin precedence.
- Copy only the complete skills and license; the repository license may be placed at `sop/LICENSE`. Do not copy maintainer `AGENTS.md`, `.git`, tests, CI, plugin metadata or hooks into a project-skill installation. Do not replace the project's license.
- Do not automatically rewrite project rules or disable/delete old entries. If switching requires changes, preview the affected differences and obtain authorization. Preserve customization, task history, failure counts and unresolved verification. Renaming or updating a skill cannot turn missing evidence into completion. This is conflict handling, not a mandatory migration workflow for every task.

## 3. Verify and report

Compare installed content with the same source, including resources, extra files and license. Actually load `sop` and verify its base directory and shared rules. File existence, discovery, invocation and correct behavior are separate claims. If loading is not observed, report it as unverified; suggest a new session in the same project when needed, without starting another model or changing permissions.

Report host, scope, form, actual version/commit, paths, content checks, loading evidence, conflicts and limits. After interruption, reread current files and valid authorization; handle only remaining authorized changes, preserve new edits and do not roll back on your own. Report temporary source leftovers; cleanup requires applicable authorization.

Updates are user-initiated and repeat source, conflict and loading checks. Before removal, list this installation's directories and local changes and obtain deletion approval. Do not delete the host's whole skills directory, project records or other copies.

## Mechanism references

- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Harness Skills, pinned source](https://github.com/deepseek-ai/deepseek-harness/blob/86a402200d95fecef4529d969836f1fe13c6cb0d/docs/subsystems/skills.zh.md)

These are existing documentation references; host implementations were not rechecked in this pass. See [design evidence](docs/design.md) and [verification limits](docs/testing.md).
