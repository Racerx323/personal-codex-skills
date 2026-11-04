# Installation and recovery

Install only an individually reviewed `skills/<name>/` bundle under
`$HOME/.agents/skills/<name>/`. Keep the source checkout in the development
workspace and backups under `$HOME/.local/state/personal-codex-skills/backups/`,
outside discovery roots. Codex manages system skills under `$HOME/.codex/skills`.

The deployed bundle is a local copy and does not follow source edits. The
[current manifest](current-installation.json) records all deployed file hashes;
[the baseline](current-baseline.md) records qualification and discovery limits.

## Before installation

1. Review source provenance, licenses and the complete proposed bundle.
2. Validate changed skill metadata with skill-creator's `quick_validate.py`.
3. Run repository checks and relevant evaluation cases described in
   [maintenance](maintenance.md).
4. Compare the existing destination with its deployment manifest. Stop on drift
   or an unrelated installation.
5. Record the reviewed source revision and intended destination.

## Install and verify

Back up the existing bundle outside discovery and verify every backed-up file.
Copy the reviewed bundle to its intended destination and compare the complete
source and deployed hash maps, including licenses and references. Preserve only
one personal copy of each capability; plugin duplicates require an explicit
ownership decision.

Verify discovery in each intended client using a fresh conversation or its
supported discovery API. Check enabled state and load errors. A running
conversation may retain an earlier catalog. Discovery can refresh Codex-managed
files; do not describe it as a filesystem read without side effects.

For explicit workspace routing of prose requests, use the
[Clear Writing routing section](../templates/clear-writing-routing.md). The
workspace `AGENTS.md` is maintained separately from the installed skill bundle;
the template preserves the tested section without copying unrelated instructions.

Refresh the current manifest and baseline after deployment. Keep required private
rollback copies; remove superseded public inventories and successful audit logs.

For CBM, deploy the complete `skills/codebase-memory` bundle. Its
[skill-specific guide](codebase-memory.md) distinguishes skill deployment from
the native server installation maintained in `homelab-docs`. Do not run the
upstream multi-client installer to update this personal skill.

## Recovery

Confirm the active tree still matches its deployment manifest before replacing
it. Archive that tree outside discovery, restore the selected verified backup,
compare every restored hash and verify fresh discovery. Stop if the manifest or
backup cannot establish the intended contents.

Restore only the affected personal skill. Use supported Codex maintenance for
system skills and plugins. LikeC4 updater ownership has a separate private lock
backup recorded in the current manifest; restore only its relevant entry after
checking for a conflicting live entry.
