# Installation and recovery

## Scope

Install an individually reviewed `skills/<name>/` bundle under
`$HOME/.agents/skills/<name>/`. The original Clear Writing consolidation procedure
below is historical; subsequent LikeC4/Playwright updates follow
[the maintenance procedure](maintenance.md).
Keep source checkouts under the development workspace and backups under
`$HOME/.local/state/personal-codex-skills/backups/`, outside discovery roots.
Do not copy the whole repository into a skill directory.

The install is a reviewed local copy. It does not follow upstream updates or
working-tree changes automatically. Codex-managed system skills remain under
`$HOME/.codex/skills`.

## Preflight

1. Validate the skill with skill-creator's `quick_validate.py`.
2. Run repository checks and the cases under `evals/clear-writing/`.
3. Confirm the plugin-provided Context7 skill is enabled and discovered.
4. Record hashes of the existing `stop-slop`, personal `context7-mcp`, and new skill.
5. Ensure the new destination does not already contain an unrelated installation.

## Apply

Create a timestamped backup directory and copy the existing skills into it.
Verify every backed-up file against its source before removing an active copy.
Copy the reviewed Clear Writing bundle into its new destination and verify its
file hashes against the source tree. Retire the old `stop-slop` and personal
`context7-mcp` directories only after those checks succeed.

Force a Codex skill-discovery refresh and confirm Clear Writing and the Context7
plugin skill are enabled, with neither retired personal skill discovered. An
already-running conversation may retain its earlier skill catalog; use the next
turn or a fresh session to confirm client visibility.

## Rollback

Read the installation record for the exact backup directory and hashes. Compare
the installed Clear Writing tree with that record before touching it; stop if
someone has changed it. Move it out of discovery into a separate rollback archive.
Restore both retired personal directories from their verified backups only when
the original destinations are absent. Refresh discovery and check the restored
catalog. This restores the previous duplicate Context7 state intentionally.

No rollback modifies the Context7 plugin, LikeC4, Playwright, or system skills.

## Updates

Review changes in this repository, rerun evaluation, and repeat backup, copy,
readback, and discovery verification. Never replace a modified destination without
reviewing its differences. Record the source revision and file hashes each time.
