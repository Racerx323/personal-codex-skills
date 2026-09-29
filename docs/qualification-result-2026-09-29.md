# LikeC4, Playwright, and tool inventory qualification

The follow-up corrects one LikeC4 reference sentence, adds reusable regression
coverage, and refreshes the WSL tool inventory. Installed runtime versions were
retained. The earlier audit report and its sealed evidence remain historical.

## LikeC4

`references/predicates.md` now says `element.**` includes every recursive
descendant regardless of relationships. No other skill instruction changed.
The maintained source and installed personal copy match.

- Existing parser/filter suite: **22/22 pass**, including positive and negative
  parser cases, absolute file counts, total errors, multi-file definitions,
  deployment syntax, and typed/title relationship syntax.
- New semantic suite: **8/8 pass**, including exact computed nodes and edge
  relation membership, unrelated descendants, accumulated external elements,
  deployment instances, and extension of only the matching kind/title relation.
- Fresh reference-only evaluator: **3/3 fixed questions pass**. It received no
  prior audit answers. Parent grading and runtime verification are separate.
- Actual PNG export passed with LikeC4 **1.59.4**, its existing Playwright
  **1.60.0**, and installed Chromium revision **1223**. The PNG is retained;
  successful raster generation is not a comprehensive visual-quality review.

This checkout has no local LikeC4 package manifest or lockfile. Qualification
used the existing resolved global CLI; it did not replace a project version or
lockfile. For projects with a local dependency, use that project dependency and
lockfile. Version and relevant command help are captured with computed outputs.
`--no-layout` and `--skip-layout` establish no rendered correctness by themselves.
Context7's upstream predicate reference still contained the contradictory
wording; the local installed-version computation supports this narrow correction.
Do not accept later upstream changes without comparing these retained outputs.

The evaluator also noted an adjacent ambiguity about unary incoming relationship
selection. That observation was not runtime-qualified or changed in this scoped
correction; it is not reported as a confirmed implementation defect.

Run from the skills checkout:

```bash
python3 evals/likec4-dsl/verify_cli.py --output /private/path/parser.json
python3 evals/likec4-dsl/verify_semantics.py --raster --output /private/path/semantics.json
```

The raster option uses only LikeC4's existing browser dependency. An absent
browser is reported unavailable; it is never downloaded by the harness.

## Playwright

The reusable lifecycle harness passed **10/10 checks** across 42 commands with
CLI **0.1.22**, bundled Playwright/Core **1.64.0-alpha-1790635538000**, and
Chromium **155.0.8059.12**, revision **1247**. No runtime or skill-bundle change
was needed.

Coverage includes snapshot-referenced click, cookie/localStorage save/load into
a second session, blocked IndexedDB deletion, authoritative failed assertions,
actual trace/video paths, targeted session cleanup, synthetic attached-browser
detach preserving both existing tab IDs/URLs and the external browser process,
and generated-action tests using both fixture and standalone imports.

Every raw artifact was checked for owner-only permissions and ownership.
Unique session names were combined with a task-owned working folder, browser
profile, subprocess handles, and tab identity checks. No global cleanup or real
user profile was used. Raw artifacts remain under owner-private
`/tmp/playwright-qualification-8b6sbvbe`; they may disappear during normal temporary
storage cleanup. Sanitized results and hashes are retained in the repository.

The initial run had one fixture failure: headless Chromium rejects multiple
startup URLs. The corrected fixture creates its second preexisting tab over
loopback CDP. Both runs are retained. Generated tests reuse the CLI-emitted
click action and expose the already installed `playwright/test` through a private
temporary `@playwright/test` alias; no package was installed. Two positive tests
passed and the deliberately wrong expectation failed with exit 1. Interactive
paused-test generation and extension attachment were not exercised.

```bash
python3 evals/playwright-cli/verify_lifecycle.py --report /private/path/lifecycle.json
```

## Tool inventory

`homelab-docs/docs/development-tool-stack.md` now records live WSL tool and
extension versions, all nine installed/enabled plugins, and the distinction
between installed plugins, cached packages, and supplied skills. Windows-local
observations remain explicitly dated September 14. Running MCP process versions
are unverified rather than inferred from CLI package versions.

Updated versions include markdownlint-cli2, Terraform, Copilot, Ollama, vexp,
Erode, Doppler, npm, the WSL kernel/remote editor launcher, and several extensions.
Erode's version comes from package metadata because direct startup required an
unavailable provider credential; Gitleaks uses APT metadata because its version
banner is unset. No credentials were retrieved. Routine Playwright installation
and downgrade advice was replaced with installed-pair qualification guidance.

## Acceptance, backup, and limits

The only installed bundle change is `likec4-dsl/references/predicates.md`.
Complete previous LikeC4 and Playwright bundles and their file-hash manifest are
backed up outside discovery at:

`$HOME/.local/state/personal-codex-skills/backups/20260929T234507Z-qualification/`

On a confirmed bundle regression, restore the entire affected skill directory
from that backup and verify every file against its manifest, including the file
set. Do not roll back the CLI or browser version. No regression required restore
in this run. Playwright's installed bundle remained byte-for-byte unchanged.

Personal-skills tracked pre-commit checks and changed-skill metadata validation
passed. The initial documentation check found a Mermaid pin mismatch. The user then
requested the latest available Mermaid release. The npm registry returned
**12.0.0**, already installed; the repository pin was advanced from **11.16.0**
to **12.0.0**, without installing or downgrading a runtime. All documentation
checks then passed with a private `MERMAID_PUPPETEER_CONFIG` selecting existing
Chromium 155.0.8059.12. Default launch remains unavailable because Puppeteer
headless-shell 154.0.8037.57 is absent; the documented override is required. `vexp verify_done`
reported unavailable because the workspace root is not a Git repository; it is
not counted as verification. No changes were committed or published.

Evidence lives in [the qualification directory](../evals/qualification-2026-09-29/).
The original audit artifacts are preserved and hash-checked separately.

## Subsequent default-browser repair and publication checks

The later authorized Mermaid repair installed the bundled Puppeteer's expected
chrome-headless-shell 154.0.8037.57. Default rendering and the complete
`homelab-docs` pre-commit suite passed without browser overrides. Mermaid CLI
remained 12.0.0 and the Playwright browser hash was unchanged. The earlier
qualification files above retain their original observations.

For publication, Markdown lint excludes only the immutable canonical security
report whose original MD032 issue was already recorded. Gitleaks permits only
the exact verified `style-tokens-colors.md` checksum match in the manifests.
These exceptions preserve evidence bytes and leave other documents and secret
values subject to their normal checks.
