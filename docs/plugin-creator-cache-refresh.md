# Upstream report: shared system-skill refresh removes plugin-creator

Submitted as a related reproduction on [Codex issue #19265](https://github.com/openai/codex/issues/19265#issuecomment-5899517948).
The original reproduction differs; a shared root cause is not yet established.

## Environment and observed behavior

Ubuntu/WSL, a shared Codex home, CLI 0.159.0 and supported update 0.159.1.
The active conversation exposes plugin-creator as a system skill. The CLI's
forced `skills/list` returns five system skills and omits plugin-creator.

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
2. Start `codex app-server --stdio` using the same Codex home as the other client.
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

The raw reproducer remains in the private maintenance archive. Sanitized
[discovery](../evals/maintenance-2026-09-29/discovery-updated.json),
[repo-copy discovery](../evals/maintenance-2026-09-29/repro-updated.json), and
[before/after hashes](../evals/maintenance-2026-09-29/system-refresh-hashes.json)
are retained here. No authentication/configuration files are included.
