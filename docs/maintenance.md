# Skills maintenance

## Ownership and review boundary

Maintain personal adaptations in this repository and deploy only individual
`skills/<name>` bundles into `$HOME/.agents/skills`. Keep native system skills
and plugin packages managed by their supported Codex update mechanisms.
Update the per-client inventory in the homelab development-tool-stack document
at the same time; a directory in a cache is not proof of installation.

Before each update, record the source revision or unknown provenance, license,
all bundle hashes, tool versions, selection policy, and observed discovery by
client. Review instructions and the complete available implementation scope
before installing candidates. Record unavailable native/service implementations
as limitations; do not describe a source audit as proof of system safety.

## Candidate validation

For LikeC4, keep the entrypoint focused on scope, reference selection, exact
syntax and validation. Run positive and negative DSL fixtures using the project
version, check filteredFiles and totalErrors, and retain existing evaluations.
For Playwright, test task-owned sessions, attached-browser detach, synthetic
state round-trip, unchanged assertions, prompt-injection resistance, and cleanup
against a loopback fixture. Never use real credentials for these checks.

Use independent baseline and candidate evaluators with the same requests;
record actual answers and parent grading separately. A simulated plan does not
prove browser/runtime behavior. Repair failed cases and retain the initial
failure and retest, rather than replacing historical results with a pass.

Run repository pre-commit checks, metadata validation for changed skills,
relative-link checks, and the relevant behavioral/runtime cases. Keep upstream
notices with the derived bundle. Recheck reference contradictions after moving
instructions; shorter entrypoints alone are not acceptance evidence.

## Installation and rollback

1. Compare the active bundle with the captured baseline. Stop on unreviewed drift.
2. Back up outside discovery under the timestamped personal-codex-skills state
   directory. Verify every file hash before replacing anything.
3. Rehearse baseline → candidate → baseline in a non-discoverable staging tree,
   verifying exact hashes after each copy. This checks file rollback, not every
   possible client cache behavior.
4. Replace one reviewed skill at a time and verify its complete deployed hash map.
5. Refresh CLI discovery and check enabled state and load errors. Refresh the
   other client in a new conversation before asserting cross-client parity.
6. Keep the backup, manifests, review results and source revision. For rollback,
   first verify the active tree still matches the deployment manifest; archive
   it, restore that skill's backup, verify hashes and refresh discovery again.

Do not recursively delete an unknown destination, overwrite a changed skill,
or restore a system-skill snapshot over a newer Codex-managed bundle.

## System skills and plugins

Use `codex update` for the standalone CLI, then start a fresh client and compare
versions, discovery and managed-file hashes. Keep the prior supported binary
for diagnostic comparison if the updater retains it. Do not maintain personal
patches in `.system` or a plugin cache. The
[plugin-creator report](plugin-creator-cache-refresh.md) records the observed
cache conflict and the unsuccessful update remedy.

For the documentation cache finding, use the helper's supported `--cache-dir`
option with an absolute owner-private directory created beneath a trusted parent.
Verify ownership, reject symlinks and require mode0700. This is a workaround,
not a patched system helper. For security-plugin temporary artifacts, prefer
persistent private artifact storage; temporary storage requires a process-wide
owner-private temporary parent configured before the plugin starts. Do not
assume the current running host uses such a parent or silently change its config.

Keep external review/upload and connector writes within the user's authorized
scope. A local read-only worker profile is not sufficient evidence that every
inherited MCP tool is read-only. Review that host boundary separately.
