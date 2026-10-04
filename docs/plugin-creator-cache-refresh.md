# Upstream report: shared system-skill refresh removes plugin-creator

Submitted as a related reproduction on [Codex issue #19265](https://github.com/openai/codex/issues/19265#issuecomment-5899517948).
The original reproduction differs; a shared root cause is not yet established.

## Environment and observed behavior

Retained for the unresolved upstream issue. The October 4 inventory uses Codex
0.160.0 and finds no plugin-creator in Ubuntu or Windows discovery. The cache
removal below was observed on 0.159.0/0.159.1; it has not been reproduced on
0.160.0 and is not evidence that the current release should supply the skill.

Ubuntu/WSL, a shared Codex home, CLI 0.159.0 and supported update 0.159.1.
The conversation exposed plugin-creator as a system skill. The CLI's
forced `skills/list` returned five system skills and omitted plugin-creator.

Within one process invocation, hashing `.system` before and after app-server
initialization/discovery demonstrated removal of all eleven plugin-creator
files and replacement of `.codex-system-skills.marker`; other system file
hashes stayed equal. A later host invocation materialized the session copy
again. The observation establishes a shared cache refresh conflict; it does
not establish which release should own that skill or a supported parity fix.

The same plugin-creator entrypoint is discovered with repo scope from a
throwaway `.agents/skills/plugin-creator/SKILL.md`. Its frontmatter is therefore
accepted by this CLI. The temporary copy is a reproducer, not an installation.

## Reproduce

1. Record CLI version and hash every regular file beneath the system-skill root.
2. Start the installed release's supported stdio app-server using the same Codex
   home as the other client. Check `codex app-server --help` for that release.
3. Send `initialize` with clientInfo and experimentalApi capability, followed
   by the `initialized` notification.
4. Send `skills/list` with `cwds` containing the development workspace and
   `forceReload: true`. Retain only names, scopes, enabled flags and errors.
5. Before leaving the same invocation, hash the system root again and compare.
6. Repeat discovery from an isolated repo containing only a copy of the omitted
   SKILL.md. Confirm repo-scope discovery, then retain the copy outside ordinary
   workspaces for evidence.

Discovery itself may refresh the managed cache. Back up first. Do not edit the
marker or introduce a permanent personal duplicate to work around this.

## Expected outcome and follow-up

Clients sharing a Codex home should either agree on the managed bundle or
isolate their managed caches so one refresh cannot remove another client's
capability. Maintainers should confirm the intended ownership and supported
migration. Recheck after a supported Codex release; do not call updating a fix
until both the before/after filesystem evidence and discovery agree.

Sanitized
[discovery](../evals/issues/plugin-creator/discovery-updated.json),
[repo-copy discovery](../evals/issues/plugin-creator/repro-updated.json), and
[before/after hashes](../evals/issues/plugin-creator/system-refresh-hashes.json)
are retained here. No authentication/configuration files are included.
