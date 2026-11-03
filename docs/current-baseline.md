# Current installation and qualification

Observation date: October 4, 2026. The
[development toolstack](../../homelab-docs/docs/development-tool-stack.md)
defines intended installed versions. This baseline replaces superseded audit,
installation and qualification snapshots.

## Deployed personal bundles

[The installation manifest](current-installation.json) verifies every file in
Clear Writing, LikeC4 DSL and Playwright CLI against `$HOME/.agents/skills`.
All 40 source files match their deployed copies. No bundle was installed or
changed during this documentation cleanup. Upstream commits and license hashes
remain in [the provenance record](upstreams.md).

[Fresh skill discovery](../evals/current/discovery.json) returned 13 Ubuntu
entries and 12 native Windows entries without load errors on Codex 0.160.0.
The inventories differ by client. These results establish discovery, not
behavioral quality, plugin installation or model-request routing.

## October 22 Harness Engineering addition

Installed the reviewed personal Codex adaptation under
`$HOME/.agents/skills/harness-engineering`. All three files match the maintained
source bundle, including attribution and the upstream MIT notice. The manifest
records the source base revision and working-tree status; this addition does not
requalify the October 4 observations above.

Metadata validation, Markdown checks, relative links, and a scoped secret scan
passed. An actual repository-only audit of frame-and-sample completed without
changing its working tree. An out-of-root symlink fixture exited 2 with an
incomplete verdict. See [qualification](../evals/harness-engineering/qualification.json)
for inputs, results, and bundle hashes. These are local execution and author
self-review results, not independent model or routing evaluations.

Fresh Codex CLI/IDE discovery remains to be checked on a subsequent turn or fresh
client. Native Windows installation and cross-client parity were not tested.
The original Cursor/Claude Code packages and Windsurf support status are recorded
in the [development toolstack](../../homelab-docs/docs/development-tool-stack.md#editor-and-agent-integration).

## November 3 Clear Writing update

Installed Clear Writing from commit `75b81f09e32c2e139a0f0c5a2f58e5ad9ff47524`.
All ten deployed files match the reviewed source. The prior eight-file bundle
matched its manifest; its private backup and file rollback rehearsal were verified.

Fresh discovery on Codex CLI 0.166.0 found the skill enabled with no load errors.
Four fresh read-only sessions used the configured `gpt-6.1-sol` model without
naming the skill in their requests. Detection loaded the installed entrypoint;
short editing and drafting requests answered without a visible skill read. The
code-only request did not load it. Automatic selection was inconsistent in these
samples. See [routing evidence](../evals/clear-writing/routing.json).

A subsequent scoped rule in the workspace `AGENTS.md` requires Clear Writing for
requested prose work, including short requests, and excludes code-only work and
ordinary conversation. Three fresh trials for each of the same four scenarios
loaded the installed skill for all nine prose requests and left it unloaded for
all three code-only requests. See the
[retest evidence](../evals/clear-writing/routing-with-rule.json), including the
exact rule and workspace instruction hashes. These finite results support the
rule for the tested CLI scenarios; they do not guarantee future selection.

These observations qualify Ubuntu/WSL CLI discovery and the tested requests.
IDE and native Windows routing remain untested. No managed system-skill file
changed during discovery or these sessions; installed Clear Writing hashes
remained unchanged. Other personal bundles were not replaced or requalified.

## Version-qualified runtime checks

| Component | Current version | Evidence |
| --- | --- | --- |
| LikeC4 CLI | 1.59.4; CI pin remains 1.59.1 | Repository validation passed for 16 model files; current parser and computed-membership fixtures are retained separately |
| Playwright CLI | 0.1.22; Playwright/Core 1.64.0-alpha-1790635538000 | All ten synthetic lifecycle checks passed with Chromium 1247 / 155.0.8059.12 |
| Mermaid CLI | 12.0.0; Puppeteer 25.12.0 | Default validation and SVG, PNG and PDF exports passed using chrome-headless-shell 154.0.8037.57 |

See [runtime qualification](../evals/current/tool-qualification.json),
[LikeC4 parser cases](../evals/current/likec4-parser.json),
[computed semantics](../evals/current/likec4-semantics.json), and
[Playwright results](../evals/current/playwright.json). The Playwright report
binds results to the current harness hash. Its synthetic external browser uses
`--password-store=basic` with a disposable profile, avoiding a desktop-keyring
setup prompt; it does not qualify real credential storage.

## Reusable evaluations and retained issues

Keep [Clear Writing cases](../evals/clear-writing/cases.json), LikeC4 parser and
semantic scripts, and the Playwright lifecycle harness. Author self-review
outputs and superseded scenario grades are removed. The Clear Writing cases
include missing completion status, supported by
[one inconsistent behavioral finding](../evals/issues/clear-writing/unsupported-completion.json).
It does not establish a deterministic skill defect.

Historical evidence remains only for that behavioral issue,
[unresolved storage findings](storage-issues.md), and
[the plugin-creator cache conflict](plugin-creator-cache-refresh.md).
The former LikeC4 recursive-selector contradiction is corrected in the current
references and covered by computed-membership tests; its old finding is removed.
Current source hashes and private rollback metadata are maintained separately
from obsolete installation reports.
