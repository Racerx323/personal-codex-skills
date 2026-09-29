# Security Review: personal-codex-skills

## Scope

Independent static review of all 40 files under skills/.

- Scan mode: scoped_path
- Target kind: git_worktree
- Target ID: target_sha256_867634ed87c9f539c64283b2159390d14226db500dc6051138d5f4860178421d
- Revision: 0c685c7c64926b037062ece1a4b1a955153cb817
- Snapshot digest: codex-security-snapshot/v1:sha256:839799c5e8f6f99458461c366f89368ca825d3fb027e4189c00089adc2af089e
- Inventory strategy: scoped_path
- Included paths: skills
- Excluded paths: none

Limitations and exclusions:
- Installed system/plugin code is assessed separately in the broader audit, outside this registered scope.
- No live authenticated service testing or complete external CLI/browser enforcement audit.

### Scan Summary

| Field | Value |
| --- | --- |
| Scan outcome | completed |
| Reportable findings | 0 |
| Severity mix | none |
| Confidence mix | none |
| Coverage | partial |
| Validation mode | not recorded |

Canonical artifacts: `scan-manifest.json`, `findings.json`, and `coverage.json`. This report is a deterministic projection of those files.

## Threat Model

Three personal agent skills: clear-writing transforms supplied prose; likec4-dsl guides model edits and conditional CLI workflows; playwright-cli guides browser inspection, automation and evidence collection. Entry points are Markdown SKILL.md files with task-specific reference documents. Scope contains no runtime implementing tool permissions; operational actions occur in the consuming agent host and external installed tools. Sources: skills/clear-writing/SKILL.md:11-35; skills/likec4-dsl/SKILL.md:11-39; skills/playwright-cli/SKILL.md:11-32.

### Assets

- Integrity of user facts, uncertainty, operational authorization and requested assertions: skills/clear-writing/SKILL.md:28-35; skills/playwright-cli/SKILL.md:40-48.
- Browser cookies, storage, authenticated state, user-owned browser/profile lifetime and private evidence: skills/playwright-cli/SKILL.md:26-32,50-57.
- Project models, configuration, derived exports and conditional LeanIX account mutation authority: skills/likec4-dsl/references/configuration.md:194-215; skills/likec4-dsl/references/bridge-leanix-drawio.md:7-18.

### Trust Boundaries

- User request -\> agent authorization: draft instructions and web/tool/page content do not grant authority. Controls are textual guidance, with host authorization enforcement outside scoped source. skills/clear-writing/SKILL.md:34-35; skills/playwright-cli/SKILL.md:40-44.
- Agent -\> external browser CLI -\> selected browser/site: new task-owned sessions, existing user browser attachment and persistent profiles are distinct authority paths. Ownership is not established by a session name. skills/playwright-cli/SKILL.md:18-32; skills/playwright-cli/references/session-management.md:47-49,98-164.
- Browser state -\> local artifacts -\> reports/possible authorized uploads: explicit state files, traces and videos have separate destination controls. Private-path instructions are not filesystem enforcement. skills/playwright-cli/SKILL.md:50-57; skills/playwright-cli/references/storage-state.md:274-283; skills/playwright-cli/references/tracing.md:5-10; skills/playwright-cli/references/video-recording.md:5-15.
- Project configuration/model -\> external LikeC4 process -\> artifacts or external service: includes can leave project tree; JS/TS custom generators write output; LeanIX apply is a credential-bearing network mutation separate from read/query MCP. skills/likec4-dsl/references/configuration.md:66-84,194-215; skills/likec4-dsl/references/bridge-leanix-drawio.md:16-18,39-42.
- Browser task actions (New isolated browser): Authorized URL and explicit unique -s session passed to installed CLI; effective resource Task-selected URL and session; ephemeral profile requested; no concrete runtime path supplied; recipients CLI browser and authorized website; control Agent must choose scope; actual session isolation implemented by external CLI/browser, not this repository. Evidence: skills/playwright-cli/SKILL.md:13-32; skills/playwright-cli/references/session-management.md:26-35.
- Existing browser control (User-authorized attachment): attach --cdp channel or endpoint, or --extension; optional --session; effective resource Selected running browser; documented channel-derived session without explicit --session, otherwise default for unspecified examples; recipients CLI and preexisting browser with its accessible state; control User authorization and named-target confirmation are prose obligations; remote-debugging/extension access enforced outside scope; detach preserves external browser. Evidence: skills/playwright-cli/SKILL.md:26-32; skills/playwright-cli/references/session-management.md:110-164.
- Persistent browser profile (Optional persistent launch): open --persistent or --profile=/path/to/profile; effective resource Auto-generated location unspecified in source, or caller-selected absolute profile directory; recipients Browser/CLI and local filesystem principals; control Host filesystem permissions; task ownership checks are prose only. Evidence: skills/playwright-cli/references/session-management.md:98-108; skills/playwright-cli/references/session-management.md:47-49.
- Authentication state export and restore (Explicit state-save/state-load): Explicit absolute path must replace placeholder; effective resource \<verified private task directory\>/auth.json or session.json; no deployment directory established; recipients Local CLI process, browser on restore, filesystem readers; control Agent verifies owner-private external directory and authorized reuse; OS permissions and CLI write behavior outside scope. Evidence: skills/playwright-cli/references/storage-state.md:11-26; skills/playwright-cli/references/storage-state.md:274-283.
- Trace files (Recording task-owned session): Private cwd plus launch outputDir or PLAYWRIGHT_MCP_OUTPUT_DIR set before open; effective resource Documented \<configured task output\>/traces/trace-{timestamp}.trace and .network, plus trace resources; actual CLI resolution unverified; recipients Local CLI/browser and permitted artifact readers; control Owner-private directory verification is textual; actual output resolution/permissions external. Evidence: skills/playwright-cli/references/tracing.md:5-10; skills/playwright-cli/references/tracing.md:27-59.
- Video files (Explicit video-start or screencast.start): Explicit absolute private output file; effective resource \<verified private task directory\>/demo.webm or video.webm; recipients Local browser/CLI and permitted artifact readers; control Agent must replace placeholders and verify privacy; OS/CLI enforce writes. Evidence: skills/playwright-cli/references/video-recording.md:5-15; skills/playwright-cli/references/video-recording.md:54-57.
- Custom browser automation (run-code inline or file): Function expression inline or --filename=./my-script.js evaluated by CLI; effective resource Caller-selected code and file relative to command working directory; browser page/context capabilities; recipients CLI evaluator, browser context and contacted sites; control Skill authorization instructions plus external CLI/browser/host controls; absence of import/require syntax is not proof of sandboxing. Evidence: skills/playwright-cli/references/running-code.md:3-21; skills/playwright-cli/SKILL.md:40-56.
- LikeC4 project configuration and model (Installed project toolchain): Nearest configuration; config-directory DSL plus include.paths; JS/TS config supports custom generators; effective resource Selected project directory and external included directories; manual layouts default \<config directory\>/.likec4; recipients Installed LikeC4 CLI and host filesystem; control Agent scope/version rules are prose; config loading and executable generator authority belong to external runtime. Evidence: skills/likec4-dsl/SKILL.md:13-22; skills/likec4-dsl/references/configuration.md:66-84; skills/likec4-dsl/references/configuration.md:123-135; skills/likec4-dsl/references/configuration.md:194-219.
- LikeC4 artifacts and preview (Build/export/serve): Explicit -o plus selected project directory; PNG export invokes Playwright; effective resource Examples ./dist, ./images and model.json relative to invocation cwd; documented preview port 5173; recipients Local filesystem/browser and any reachable preview client (binding unspecified); control External CLI/filesystem/browser controls; publication not automatically authorized by artifact generation. Evidence: skills/likec4-dsl/references/cli.md:31-68; skills/likec4-dsl/SKILL.md:63-68.
- LeanIX inventory mutation (Separately authorized sync --apply): LikeC4 resolved model -\> mapping -\> CLI sync --apply; LEANIX_API_TOKEN; effective resource Environment credential reference LEANIX_API_TOKEN; endpoint/account unspecified; out/bridge relative to project-root invocation; recipients External LeanIX API and local bridge artifact readers; control External API credential authorization; skill describes dry-run/apply distinction but provides no implemented approval or exact payload binding. Evidence: skills/likec4-dsl/references/bridge-leanix-drawio.md:7-18; skills/likec4-dsl/references/bridge-leanix-drawio.md:35-42.
- LikeC4 model queries (MCP stdio or optional HTTP): likec4 mcp workspace with --http/--port; effective resource Default stdio; documented HTTP port 33335 or explicit port; binding/authentication unspecified; recipients MCP caller and selected workspace model; control Read/query-only is a documentation claim; runtime authorization and transport exposure outside scope. Evidence: skills/likec4-dsl/references/cli.md:106-116; skills/likec4-dsl/references/bridge-leanix-drawio.md:39-42.

### Attacker Capabilities

- An author of inspected page content, downloaded material, tool-described content or a supplied prose draft can place misleading instructions in material the agent reads, but is not assumed to control the user, host permissions or trusted skill installation. New impact requires the agent to turn this lower-trust material into privileged actions despite explicit textual boundaries. skills/playwright-cli/SKILL.md:40-44; skills/clear-writing/SKILL.md:34-35.
- An untrusted model/config contributor can influence selected project inputs if the operator actually opens that project. Runtime execution behavior of JS/TS config and generators is external and not established here. skills/likec4-dsl/references/configuration.md:9-13,194-215.
- No remote multi-tenant service or sandbox escape is established by this repository. A user intentionally providing run-code already requests code execution; syntax restrictions alone establish no additional confinement. skills/playwright-cli/references/running-code.md:3-21.

### Security Objectives

- Preserve user authorization and do not infer login, host contact, account mutations, uploads or tool installations from page/document suggestions. skills/playwright-cli/SKILL.md:13-16,26-44.
- Retain ownership boundaries when closing browsers and deleting profiles/artifacts; protect state exports with real filesystem privacy and avoid sensitive reports. skills/playwright-cli/SKILL.md:28-32,52-56; skills/playwright-cli/references/storage-state.md:274-283.
- Maintain factual and verification integrity; preserve supplied assertions and avoid reporting validation without execution. skills/clear-writing/SKILL.md:28-35; skills/playwright-cli/SKILL.md:46-48; skills/likec4-dsl/SKILL.md:56-68.
- User audit constraint: no remediation, active installation/configuration/authentication/runtime changes, homelab host contact, publication or external mutations. Synthetic disposable local execution is authorized.

### Assumptions

- Exact scope is skills/. This model reviews Markdown architecture, not external CLI/browser implementation or host authorization. SECURITY.md was not present in the offline repository file inventory; caller reports empty resolved security policy.
- Source lines establish what the skills instruct/document, not that installed versions implement every claimed default, path or isolation property.
- Examples use implicit/default sessions despite entrypoint instructions for unique task sessions; documented defaults and PLAYWRIGHT_CLI_SESSION exist, so examples require adaptation rather than proving wrong-session behavior. skills/playwright-cli/SKILL.md:18-26; skills/playwright-cli/references/session-management.md:52-59,166-174.
- No concrete private runtime directory, profile root, CLI output precedence, remote LeanIX account or browser attachment is configured in scoped source. Effective resources above therefore retain parameterized paths and explicit unknowns instead of inventing deployment facts.
- LeanIX documentation distinguishes dry-run from apply and requires a token, but account/revision/payload approval binding and readback implementation are not in scope. skills/likec4-dsl/references/bridge-leanix-drawio.md:16-18.
- LikeC4 MCP is documented as read/query-only; tool implementation, bind address and transport authentication are absent. skills/likec4-dsl/references/bridge-leanix-drawio.md:39-42; skills/likec4-dsl/references/cli.md:106-116.
- Architecture mapping is not completed vulnerability-audit coverage.

## Findings

### No findings

No reportable findings survived the canonical discovery, validation, and reportability gates.

## Reviewed Surfaces

| Surface | Risk Area | Outcome | Notes |
| --- | --- | --- | --- |
| All 40 personal skill files | not recorded | No issue found | Independent baseline fully read all 40 files. Draft/page authority, private storage, browser ownership, shell examples, dependencies, conditional LeanIX mutation and assertion integrity traced. No source-supported exploitable vulnerability found. |
| External runtime enforcement | not recorded | Needs follow-up | External host/browser/CLI enforcement and authenticated integrations unavailable to this scoped source review. These are assurance limits, not unreviewed files within skills/. |
| Independent baseline all 40 personal skill source files | not recorded | No issue found | Independent baseline returned no reportable vulnerabilities; parent reconciliation pending. Draft/page instruction trust, browser private state, owned cleanup, package-runner scope and assertion integrity reviewed. |
