# Codebase Memory skill maintenance

This repository owns the adapted [skill bundle](../skills/codebase-memory/SKILL.md),
its [upstream attribution](../skills/codebase-memory/ATTRIBUTION.md),
[evaluation cases](../evals/codebase-memory/cases.json), and
[qualification record](../evals/codebase-memory/qualification.json).

The separate [CBM installation and lifecycle guide](../../homelab-docs/docs/codebase-memory-installation-and-lifecycle.md)
owns workstation configuration: executable and cache paths, Codex registration,
Headroom disablement, daemon and watcher behavior, binary updates, and rollback.
The [development tool inventory](../../homelab-docs/docs/development-tool-stack.md#codebase-memory-indexing-and-agent-workflow)
links to that guide. Keep those operational details out of this skill's source
provenance pins.

## Source and adaptation

The reviewed upstream source is `DeusData/codebase-memory-mcp` v0.12.1 at commit
`a7158ac2f48ca646b4527341b76f930f2aeff87e`. Its skill is embedded in
`src/cli/cli.c`; [upstreams.json](upstreams.json) records the reviewed source and
license hashes. Preserve the upstream MIT notice with every deployed bundle.

The local adaptation preserves the workspace's vexp → CBM → Serena order,
canonical-root selection, targeted queries, paged coverage checks, and direct
source fallback. It adds the observed stable-release watch boundary and keeps
delegation within the user's authorization. It does not install upstream's
global activation pointer, hooks, graph agent profiles, or other client configs.

## Install or reconcile the bundle

Follow [installation and recovery](installation.md) for the shared procedure.
The source directory is `skills/codebase-memory`; the deployment directory is
`$HOME/.agents/skills/codebase-memory`. Deploy all three bundle files, including
attribution and license. Keep backups under the private personal-skills state
directory outside discovery roots, and compare complete file/hash maps before
and after replacement. Do not copy the entire repository into the skill root.

The November 4 installation initially created only a local entrypoint. This
repository addition captures that adaptation, adds the notices and relative
attribution link, and reconciles the installed bundle to the maintained source.
It does not change CBM's binary, cache, runtime settings, or Codex registration.
The preparation base revision and exact deployed content hashes are recorded in
[the deployment manifest](current-installation.json). The repository's commit
history records the subsequent source capture and maintenance changes.

Validate metadata, Markdown, JSON, and relative links. Rehearse file replacement
and restoration in a non-discoverable directory, then compare the installed tree
with the source. Use fresh Codex discovery to confirm enabled state and no load
errors. An existing conversation's catalog is not proof of a refreshed client.

## Update and rollback

Review an immutable candidate upstream commit and its embedded skill, runtime
documentation, and license. Check that every adopted tool and runtime assumption
exists in the installed CBM release; a skill update does not upgrade the native
server. Reconcile the local discovery order and authorization boundaries rather
than replacing the adaptation with upstream instructions wholesale.

Update the source and license hashes, attribution, cases, and qualification
record. Keep actual native execution, manual review, model behavior, and fresh
client discovery as separate evidence. Use [maintenance](maintenance.md) for the
shared deployment checks and preservation rules. Update the manifest and current
baseline after deployment; do not rewrite other skills' historical observations.

For skill-only rollback, verify the active bundle against its manifest, archive
it outside discovery, restore the verified prior bundle, compare every hash,
and refresh discovery. Native binary/cache rollback follows the homelab guide
and is a separate operation. Headroom remains disabled; an uninstall of its
retained copy is not part of skill maintenance.
