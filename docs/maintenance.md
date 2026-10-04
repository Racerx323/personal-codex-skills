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
version and check filteredFiles and totalErrors. Replace superseded results.
For Playwright, test task-owned sessions, attached-browser detach, synthetic
state round-trip, unchanged assertions, prompt-injection resistance, and cleanup
against a loopback fixture. Never use real credentials for these checks.

Use independent baseline and candidate evaluators with the same requests;
record actual answers and parent grading separately. A simulated plan does not
prove browser/runtime behavior. Repair failed cases. Keep failure and retest
evidence only while it explains an unresolved issue or retained version.

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
6. Keep the current manifest, source provenance and required private backups.
   Remove superseded public audit records. For rollback,
   first verify the active tree still matches the deployment manifest; archive
   it, restore that skill's backup, verify hashes and refresh discovery again.

When reverting LikeC4 to upstream-managed ownership, use the private updater-lock
backup identified in [the current manifest](current-installation.json). Restore
only its original entry after checking for a
conflicting current entry; retain all other live installer settings. A rollback
to an earlier personal adaptation keeps the upstream updater entry retired.

Do not recursively delete an unknown destination, overwrite a changed skill,
or restore a system-skill snapshot over a newer Codex-managed bundle.

## System skills and plugins

Use `codex update` for the standalone CLI, then start a fresh client and compare
versions, discovery and managed-file hashes. Keep the prior supported binary
for diagnostic comparison if the updater retains it. Do not maintain personal
patches in `.system` or a plugin cache. The
[plugin-creator report](plugin-creator-cache-refresh.md) records the observed
cache conflict and the unsuccessful update remedy.

For the documentation cache finding, invoke the managed helper only through
`python3 "$HOME/.local/share/codex-hardening/fetch-manual-private.py"`.
The wrapper validates its fixed private cache. Do not invoke or import the helper
directly or substitute a shared cache. Codex Security supplemental artifacts
require `storage: "persistent"` with inline `content`, or prepared/read persistent
storage. Temporary storage and `sourcePath` imports remain prohibited until the
actual plugin process has a verified owner-private temporary parent. See
[the retained findings](storage-issues.md) for scope and evidence limitations.

Keep external review/upload and connector writes within the user's authorized
scope. A local read-only worker profile is not sufficient evidence that every
inherited MCP tool is read-only. Review that host boundary separately.
