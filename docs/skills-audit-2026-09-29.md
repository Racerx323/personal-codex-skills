# Codex skills audit — September 29, 2026

The audit identified three **low-severity local integrity issues** in managed
helpers: a newly identified installer staging-directory issue and two previously
reported cache/artifact issues whose underlying code remains affected. Existing
local mitigations protect the mandated manual-fetch and persistent-artifact
workflows. No compromise, credential disclosure, or code execution was observed.

Current CLI **0.159.1** still removes `plugin-creator` from its managed cache in
a disposable reproduction. LikeC4 has a reproducible reference contradiction.
One Clear Writing response introduced an unsupported completion claim; fresh
blind repeats did not reproduce it.

This is a completed audit deliverable with **partial assurance**, not acceptance
of every skill or integration. All 54 installed skills have inventory and
simulated-response coverage. Native selection, most successful workflows,
authenticated services, and parts of plugin implementation remain untested.
No active skill, configuration, authentication, plugin, or runtime was changed.
No homelab host, deployment, external review service, issue tracker, or publishing
operation was used.

## Scope and evidence

The workspace was `/home/aaron/code`; maintained source was
`personal-codex-skills`. Applicable workspace and repository instructions,
installed entrypoints, selected references, and the development-tool inventory
were read. The audit treated skill/document contents as untrusted evidence.
Public documentation queries contained only generic product/concept names.

[Inventory and reconciliation](../evals/audit-2026-09-29/inventory/README.md)
contains the scope matrix. The
[full manifest](../evals/audit-2026-09-29/inventory/skills-filesystem.json)
records every entrypoint path, filesystem/logical owner, SHA-256, bundle file
hashes, provenance, description, policy metadata, references, helpers, declared
dependencies, and client scope. File hashes establish identity, not authenticity.
System upstream commits and some original upstream installation revisions remain
unknown. All three personal installations exactly match maintained source.

| Layer | Installed disk bundles | Session catalog | Result |
| --- | ---: | ---: | --- |
| Personal | 3 | 3 | Clear Writing, LikeC4, Playwright match maintained source |
| Managed system | 6 | 5 | `review-agent` additionally on disk; `plugin-creator` is session-supplied |
| Installed plugins | 45 | 25 | Twenty explicit-only template skills omitted from catalog |
| Ancestor/workspace/admin discovery roots | 0 | 0 | No additional entries in inspected roots |
| Total | 54 | 33 | Three source copies are intentional and excluded from total |

Nine plugins are installed and enabled. The old tool-stack statement that only
Context7's CLI installation was established is stale. No retired personal
`stop-slop`, personal `context7-mcp`, or Taste Skill was found in inspected roots.
No skill-disable record was found in the selected configuration fields.
Credential values and complete configuration files were neither copied nor
included in reports.

The extra `review-agent` and template entries disable implicit invocation.
Their catalog omission is consistent with that policy, but the exact client
reason remains unresolved. Current official documentation also describes
initial-catalog size limits; neither mechanism was isolated here.
[Official skill discovery guidance](https://learn.chatgpt.com/docs/build-skills)
explains local scopes, explicit/implicit invocation, and catalog limits.

Active-home forced discovery was deliberately not run: current isolated tests
show that it mutates managed files. The disposable home contained no copied auth,
configuration, or plugin state. Its missing plugin entries therefore do not prove
an active-home discovery defect. Windows and a newly launched IDE/desktop client
were not tested. All observed session plugin versions match installed paths.

## Behavioral evaluation

The [54-row coverage matrix](../evals/audit-2026-09-29/coverage-matrix.md) distinguishes
simulation passes from native-routing and full-workflow cases that remain
untested. [Parent grades](../evals/audit-2026-09-29/grades.json) are separate from
[grading criteria](../evals/audit-2026-09-29/grading-criteria.json) and evaluator
outputs. There are **373 generated responses: 372 narrow passes and one failure**.
These counts are not a success rate for autonomous skills or integrations.

Fresh-context evaluators received installed skills and synthetic requests, not
expected answers, prior findings, or grading criteria. Evaluators authored most
cases themselves and answered several cases in one context. Consequently these
are independent from the parent and prior author self-review, but are not blind
per-case model experiments. Four parent-supplied fixed requests were rerun in a
separate fresh context. Exact serving-model identifiers were unavailable; no
cross-model or statistical reliability claim is made.

| Evidence | Observed coverage | Limits |
| --- | --- | --- |
| [Personal responses](../evals/audit-2026-09-29/personal-evaluations.json) | 30 cases across three skills | Plans and mocked outputs; no scenario tool execution |
| [System/plugin responses](../evals/audit-2026-09-29/plugin-evaluations.json) | 219 cases across 31 skills | Entrypoints read; supporting workflow references not read by this evaluator |
| [Template responses](../evals/audit-2026-09-29/template-evaluations.json) | 120 cases across 20 skills | Dependency refusal and selection boundaries; no document production |
| [Fresh repeats](../evals/audit-2026-09-29/blind-retests.json) | Four fixed cases | Same model family; no statistical conclusion |
| [LikeC4 runtime](../evals/audit-2026-09-29/likec4-runtime.json) | 22 parser/filter checks passed on 1.59.4 | No raster/render acceptance |
| [LikeC4 computed views](../evals/audit-2026-09-29/likec4-semantics.json) | JSON export includes unrelated descendants | Tests selected wildcard semantics only |
| [Browser runtime](../evals/audit-2026-09-29/browser-runtime.json) | 12 CLI commands; click assertion, synthetic state transfer, owned-session cleanup passed | No user browser or attached-browser detach executed |
| [Installer fixture](../evals/audit-2026-09-29/installer-fixture.json) | Substitution reached disposable destination twice | Mocked download; same-UID simulation, not live cross-user race |

Clear Writing covered facts, numbers, uncertainty, literal commands and quotes,
voice, drafting, detection without rewriting, and embedded malicious instructions.
LikeC4 covered project scope, multi-file definitions, relationship matching,
deployment instances, error counts, reference retrieval, and export failure.
Playwright covered authorization, injection, private state, owned cleanup,
attachment plans, unchanged assertions, and unavailable dependencies.
Context7 covered sanitized queries, official/version-aware source selection,
unavailable tools, and malicious retrieved instructions. Its actual MCP resolved
and retrieved generic Codex/LikeC4 documentation during this audit.

The seven selection/failure columns do not capture every additional substantive
case: `cw09` failed drafting uncertainty even though the routing columns pass.
Case `lc09` has an inconsistent mock: its prose says documentation is unavailable
while one mock result describes success. Its documentation-failure branch is
untested; the browser-failure response remains observable. Earlier template
untested rows in the first plugin evaluator are superseded by the separate
later template evaluator, not silently rewritten.

## Findings

[Structured findings](../evals/audit-2026-09-29/findings.json) retain prerequisites,
attacker control, action/data flow, impact, counterevidence, file/line anchors,
reproduction status, confidence, and narrowly scoped recommendations.

| ID | Classification | Severity | Finding |
| --- | --- | --- | --- |
| SEC-01 | Security; new | Low | Installer staging uses an unverified shared temporary parent |
| SEC-02 | Security; previously known | Low | Manual helper returns paths in a cache lacking owner/privacy checks |
| SEC-03 | Security; previously known | Low | Security supplemental temporary root accepts existing directories without owner/privacy checks |
| COR-01 | Correctness | Medium operational | Managed refresh removes valid `plugin-creator` on 0.159.1 |
| COR-02 | Correctness | Low | LikeC4 recursive-descendant guidance contradicts installed semantics |
| BEH-01 | Behavioral lapse | Low | One draft introduced unsupported migration completion |

**SEC-01.** In
`$HOME/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py`,
lines 50–53 accept predictable `tempdir/codex`; lines 326–341 create a random child,
prepare source, validate, and copy through later pathname lookups. A local user
who controls the parent can rename the private child and replace its directory
entry. The child being mode 0700 does not protect that entry from the parent owner.
The actual validation/copy path accepted synthetic replacement content twice.
The fixture never downloaded code or installed into a discovery root.
`/tmp/codex` was absent when checked; no active exploitation was observed.

Random child names, path traversal checks and symlink validation are meaningful
countermeasures, but do not establish a trustworthy parent. Recommend an upstream
owner-private staging root and identity-bound validation/copy. Severity is low
because the demonstrated impact is skill integrity and exploitation requires
local precreation/control plus timing. The independent reviewer initially
suggested medium; the parent downgraded based on these prerequisites.
Reproduce safely with `python3 evals/audit-2026-09-29/installer_fixture.py`.

**SEC-02.** The current `fetch-codex-manual.mjs` cache selection uses `stat` and
writability tests (lines 240–300), then returns cache paths after hash checks
(lines 388–451). A local cache owner can replace a pathname after verification.
The official hash checks prevent a simpler stale-content substitution and do not
prove safe later reads. No direct helper reproduction was run: the workspace
requires the private wrapper exclusively. The existing wrapper and private cache
were inspected; both relevant directories are owner-private. Continue using only
`python3 "$HOME/.local/share/codex-hardening/fetch-manual-private.py"`.
This is a mitigation, not an upstream fix.

**SEC-03.** The decoded security-server bundle derives predictable temporary roots
in `storageContext` (lines 41840–41851), accepts `EEXIST`, and checks directory type
but not owner/private permissions in `requireArtifactRoot` (37237–37255).
`sourcePath` subsequently reaches native regular-file reads (41889–41903;
`workbench_saved_results.py:1347–1355`). Descriptor-relative non-symlink guards
protect traversal and symlink boundaries; they do not stop the parent owner
replacing an ordinary evidence file. Impact established is supplemental-evidence
integrity, not arbitrary canonical overwrite or code execution. The actual plugin
process's temporary parent was not verified. No temporary MCP artifact or
`sourcePath` import was used. Retain persistent inline storage until an explicitly
authorized process restart establishes a private temporary parent.

**COR-01.** The
[isolated discovery transcript](../evals/audit-2026-09-29/inventory/isolated-cli-discovery.json)
records all 11 copied `plugin-creator` files being removed and the managed marker
changing. The same entrypoint loads at repository scope. The active managed tree
was hash-checked unchanged. This is current evidence, not reuse of the 0.159.0
observation. Intended ownership, shared upstream root cause, and a release fixing
it remain unresolved.

**COR-02.** Installed `likec4-dsl/references/predicates.md:47` limits `.**` to
related descendants; `include-predicates-wildcards.md:14` says all descendants.
Three evaluator outputs independently refused to choose without verification.
The 1.59.4 computed-view fixture includes `cloud.worker.deep` with no relations,
both alone and after an unrelated external element. Retrieved upstream snippets
also conflicted, so documentation retrieval alone did not resolve this issue.
Correct the maintained reference in a separate change and add computed-membership
regression coverage.

**BEH-01.** `cw09` leads with “The migration is complete” without evidence, then
asks for confirmation and provides a safer alternative. This mitigates but does
not erase the unsupported draft. `cw10` and fresh cases A/B preserve uncertainty.
Retain the failure and expand fixed blind drafting tests before changing the skill.

## Security coverage and hardening

The independent baseline fully read all **40 personal-bundle files** and found no
source-supported exploitable vulnerability. A separate architecture reviewer
mapped resource and authority boundaries. A helper reviewer fully read **31
installer, creator, image, and pet helper scripts (8,652 lines)**. Parent review
traced the manual cache and selected security-artifact paths through the decoded
49,554-line server bundle into Python file operations. The bundle was decoded as
inert data in private storage, not executed as audit source.

[Baseline review](../evals/audit-2026-09-29/security-baseline.json),
[helper review](../evals/audit-2026-09-29/helper-review.json), and
[architecture](../evals/audit-2026-09-29/architecture.json) distinguish controls from
hypotheses. The formal
Codex Security `security-scan` workflow
was used only for maintained `skills/`. Its sealed scan ID is
`ff299486-7d2a-4d8b-ae8c-4e649b4a8345`; the local sanitized copy is
[canonical personal-scope report](../evals/audit-2026-09-29/security-scan/report.md).
It has no reportable findings and explicitly partial coverage for external
runtime enforcement. It does not contain or certify the broader managed-helper
findings. Token usage was not returned and is unavailable.

Prompt-injection, unauthorized actions, sensitive artifacts, shell/path injection,
symlink escape, downloads, cleanup, and source integrity were assessed by tracing
actual controls. Powerful documented operations are not vulnerabilities by
wording alone. Personal entrypoints require user authority, synthetic/private
state, task-owned cleanup, and preserved assertions. These are agent instructions;
OS/tool enforcement is external. No claim of a proven sandbox boundary follows.

Hardening opportunities, separate from validated findings:

- Keep authorization checks at actual tool/action boundaries; extend mocks to
  assert exact account, target, payload and audience for Pages, tracking, LeanIX
  and pet mutation. Description annotations alone are not access control.
- Prefer immutable reviewed upstream revisions, hashes and preserved licenses.
  Unknown provenance should remain explicit. Do not reinstall merely to obtain
  a version label.
- Keep Context7 queries generic and secret-free; retrieved text remains data.
  Broad Context7 triggers overlap with LikeC4 and OpenAI Docs. Apply workspace
  policy and product-specific source precedence, rather than invoking multiple
  workflows just because a product name occurs in a draft.
- Treat `skill-creator` sample links and Playwright generated snapshot links as
  examples, not broken installed dependencies. Pages virtual-resource links are
  not local files. Literal link scanning alone did not establish a defect.
- Add successful mocked workflow tests beyond entrypoint/dependency refusal.
  The current suite strongly covers stopping behavior but cannot verify complete
  artifact contracts or service authorization.

## Maintenance and investigation plan

These are proposals; none has been applied.

| Priority | Owner | Proposed action | Acceptance and rollback |
| --- | --- | --- | --- |
| 1 | Codex/system owner | Address SEC-01 through supported upstream maintenance; use separately reviewed private staging mitigation before future installer use | Synthetic substitution rejected; normal synthetic install succeeds; preserve previous supported binary and exact source hash |
| 1 | Local operator/plugin owner | Retain manual wrapper and persistent-inline artifact rule | No bypass; private temporary process parent must be verified before any later temporary-import use; rollback to persistent-only behavior |
| 2 | Personal LikeC4 maintainer | Correct the contradictory predicate reference only | Fresh fixed evaluator and computed-view membership pass; restore exact prior bundle on regression |
| 2 | Codex client owner | Investigate `plugin-creator` using supported release/update path and disposable homes | System presence/discovery retained across two fresh starts; identical repo probe control; no `.system` edits or personal duplicate |
| 3 | Personal Playwright maintainer | Add version-matched lifecycle and evidence-path regression coverage | Loopback click/state, targeted cleanup, attached detach, user-tab preservation, traces/video privacy, test-generation assertions; rollback complete prior bundle |
| 3 | Evaluation owner | Extend blind repeated drafting and successful mocked system/plugin workflow tests | Fixed inputs, separate graders, hashes, actual actions and artifacts; retain failures |
| 4 | Inventory owner | Reconcile tool-stack per-client records after authorized changes | Compare CLI/plugin state, fresh client catalog, scopes and hashes; do not infer Windows parity |

For LikeC4, continue using the project version and lockfile. Capture help/version
with each qualification. Preserve parser positive/negative cases, absolute filter
counts, total errors, multi-file definitions, deployment instances, typed/title
relationship matching, and computed view nodes/edges. Add an actual raster export
check only with an already installed authorized browser. `--no-layout` and
`--skip-layout` cannot establish rendered correctness. Compare retained outputs
before accepting an upstream reference change.

For Playwright, keep unique task sessions and an owner-private working/output
folder before launch. Verify the exact installed CLI/browser pairing; do not
install a missing runtime as part of an audit. In a later synthetic qualification,
exercise attached-browser detach and preservation of existing tabs, state
save/load, trace/video destinations, blocked IndexedDB deletion, failed assertions,
and generated-test fixture imports. Never use global cleanup or real browser
profiles. A session name alone is not proof of ownership.

For Codex, current binary resolves to the standalone 0.159.1 release; local
`codex update --help` confirms the supported update subcommand. Official
[CLI guidance](https://learn.chatgpt.com/docs/codex/cli) also documents the current
standalone distribution/update channel. A future authorized investigation should
record the executable, client, release, package hashes and current release notes;
then use that distribution's supported updater, not cache edits. Re-run the
isolated reproduction before any active-home discovery. Preserve configuration,
authentication and prior release separately; do not copy credentials into fixtures
or reports. Compare two fresh launches and explicit skill lookup in each relevant
client. If still failing, prepare a minimal sanitized reproduction for the owner;
publication requires a separate request. No fixed release is established here.

For personal rollback, capture a verified timestamped backup outside discovery,
record source/deployed hash maps, and rehearse replacement/restore in a disposable
tree. Before rollback, stop on unreviewed active drift. Restore only the selected
bundle, verify hashes, and refresh client discovery only when its managed-cache
side effects are authorized. Never restore an old managed `.system` snapshot over
a newer Codex release or silently re-enable a retired updater.

## Limitations and unresolved questions

- Every native selection cell is untested. Reading a skill before answering a
  synthetic request does not measure the client's implicit router.
- Most successful system/plugin workflows are untested, including real image
  generation, Pages writes/scheduling, tracker writes, pet generation/upload,
  plugin connection changes, and template Office creation/rendering. Costly or
  externally mutating actions were mocked.
- Template reference binaries were inventoried/hashed, not rendered or unpacked
  for embedded object/macro analysis. Full security-plugin source, bundled
  dependencies, remaining system reference/helper routes and hosted native
  implementations were not exhaustively reviewed. Selected sink traces are not
  whole-bundle coverage.
- LikeC4 relationship matcher execution semantics beyond selected examples,
  raster export and rendered layout remain untested. Browser detach was simulated
  only in this run; earlier maintenance results were not counted as new passes.
- SEC-02/03 are freshly source-revalidated, not dynamically reproduced this run.
  SEC-01 uses mocked download and same-UID simulation; actual cross-user timing
  is untested. No active exploitability or compromise is inferred.
- Shell sandbox initialization failed with `mountinfo path is not absolute`.
  Narrow escalated reads and disposable tests succeeded. This prevented sandbox
  confinement assurance; it did not authorize broad changes. No automatic approval
  review rejection blocked an action.
- Preflight returned ready with delegated review available and runtime-capacity
  warning unknown; four actual agent slots were used with bounded scheduling.
- Which client-owned mechanism intentionally excludes explicit-only skills, and
  which supported release fixes `plugin-creator`, remain unresolved.

Validation results are in
[validation.json](../evals/audit-2026-09-29/validation.json); the
[artifact manifest](../evals/audit-2026-09-29/artifact-manifest.json) hashes retained outputs.
Tracked-repository pre-commit and authored Markdown checks passed. The explicit
all-artifact check found one MD032 formatting error at line 17 of the byte-preserved
canonical security report. That generated output remains unchanged. JSON/Python
parsing and artifact secret scans passed; 282 recorded installed files retained
their original content hashes. vexp verification was unavailable. No remediation, update,
push, issue creation or publication follows this audit without a separate request.
