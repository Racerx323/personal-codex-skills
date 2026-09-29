# Skills maintenance result — September 29, 2026

## Changes and ownership

LikeC4 and Playwright now have maintained source bundles in this repository.
Entrypoints retain selection, correctness and operational boundaries; detailed
syntax and commands live in conditional references. Existing LikeC4 evaluations
are preserved. Clear Writing source and its deployment are unchanged.

LikeC4 corrections were driven by installed 1.59.4 parser behavior: absolute file
filters and count checks, deployment instances inside nodes, accepted trailing
hyphens, binary bidirectional syntax, no nested parallel blocks, and separate
return steps where chained returns are unsupported. Old forced 1.53.0 pinning was
removed. Model fixtures validate typed matching syntax with both kinds present;
the test does not inspect rendered graphs or prove matcher execution semantics.

Playwright guidance uses owned sessions, detach for attached browsers, private
state files, and authoritative test expectations. Shared-seed test runs remain
sequential unless data is isolated. Browser automation no longer implies a
blanket global installation or permission to follow page instructions.

Codex standalone updated through `codex update`: 0.159.0 → 0.159.1. System/plugin
files were not hand-patched. The plugin-creator discrepancy persists and has an
[evidence-backed draft report](plugin-creator-cache-refresh.md). No personal
copy or Taste Skill was installed. The tool-stack document owns the per-client
inventory; Windows-local discovery remains unverified.

## Validation

Independent baseline and initial candidate evaluations covered 12 requests.
Baseline responses passed parent review. The initial candidate failed two
LikeC4 cases (root instance and relative file filters). Both were repaired and
passed independent retests; four new syntax cases also passed. These are single
response samples, not a statistical demonstration of improved model behavior.
[Actual responses and grading](../evals/maintenance-2026-09-29/grading.json)
retain failures and distinguish offline plans from executed tests.

Ten [LikeC4 CLI fixtures](../evals/maintenance-2026-09-29/likec4-runtime.json)
passed, including expected invalid inputs and empty-filter detection. Re-run with
`python3 evals/likec4-dsl/verify_cli.py`. Layout/rendering was not tested.

[Browser runtime tests](../evals/maintenance-2026-09-29/browser-runtime.json)
passed against a loopback fixture: click assertion, synthetic state save/load,
targeted close preserving another owned session, detach and reconnection to a
synthetic external browser. An initial test incorrectly required a CLI-created
page to survive detach; it failed and was replaced by a browser-process lifecycle
assertion. This does not claim user-tab preservation was exercised.

The installed CLI needed Chromium 1247. User-approved installation supplied the
matching browser and headless shell and garbage-collected unused 1237. No CLI
package upgrade occurred. All three skill metadata validators passed. Repository
checks, deployment hash verification and discovery are recorded separately below.

## Expanded security audit

The Standard security audit covered the available skill and full plugin source
scope, including the 49,554-line decoded server bundle, Python helpers, schemas,
loaders and bundled dependencies. Review used trust-boundary tracing, sink
inspection and independent reviewers; it was not exhaustive line/branch proof.
The 285-file snapshot was retained before mutation outside skill discovery.

Two LOW static integrity findings were validated: shared temporary documentation
cache replacement and security supplemental-artifact replacement before import.
Both require local precreation/control of a shared temporary directory. No
confidentiality loss or code execution was established. System/plugin fixes are
not claimed. [Maintenance guidance](maintenance.md) documents private-directory
workarounds and supported upstream maintenance.

The canonical report is private at
`$HOME/.codex/state/plugins/codex-security/scans/baseline/unversioned_20260929T204757Z_gzxgiq7t/report.md`,
scan `71ced207-bf23-4bda-8d48-949568c5bb1e`, completed and sealed. Coverage remains
partial for unavailable native implementation, inherited MCP authority and
external runtime behavior. Two stale early progress rows were retained by the
plugin's checkpoint-preservation behavior; the report's scope limitations and
closure entries explain that those source reviews finished. Source-scope
completion must not be mistaken for complete end-to-end host assurance.

## Deployment evidence

Deployment completed from source commit `f5404bf9425d6704dfde074bf66bcb00d9e49e9a`.
[Installation evidence](maintenance-installation.json) records all 285 verified
baseline files, rollback rehearsals, exact deployed hashes and nine enabled CLI
skills with no load errors. Backups are under
`$HOME/.local/state/personal-codex-skills/backups/20260929T211752Z-maintenance/`.
Both repository pre-commit checks passed; all 71 relative documentation links
resolved. vexp verification was unavailable because the shared workspace root
is not a Git repository, so it is not counted as a passed check.
Backups remain outside discovery. A fresh conversation is required to confirm
another client's catalog; this run cannot refresh its own initial catalog.
