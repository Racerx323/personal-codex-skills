# Skill inventory, 2026-09-29

Observed CLI: `codex-cli 0.159.1`. Read-only `codex plugin list --json`
reported nine installed, enabled plugins. This supersedes the older development
tool inventory's claim that only Context7 has an established CLI installation.
No installation, update, authentication, or active configuration changes ran.

## Scope and discovery matrix

| Layer | Disk entrypoints | Session catalog | Observation |
| --- | ---: | ---: | --- |
| Personal | 3 | 3 | clear-writing, likec4-dsl, playwright-cli; all bundle file hashes equal maintained source |
| Maintained repository source | 3 | 0 additional | Intentional source copies under skills/, not discovery duplicates |
| Workspace/ancestor/admin discovery roots | 0 | 0 | No additional .agents/skills roots at /, home/code, maintained repo, or /etc/codex/skills |
| Managed system | 6 | 5 | Session includes plugin-creator; disk also includes explicit-only review-agent |
| Installed plugin cache | 45 | 25 | Includes 20 explicit-only openai-templates skills omitted from session catalog |
| Total distinct installed skill bundles | 54 | 33 | Excludes three maintained source copies |

No personal stop-slop, context7-mcp, or Taste Skill entrypoint exists in the
inspected discovery roots. No skill-disable records appear in the selected
config fields. Configuration inspection retained only skills.config,
features.plugins, and plugin enabled fields. No credentials or full config
were copied. All inventoried files have filesystem owner aaron; logical owners,
entrypoint hashes, per-file hashes/modes, descriptions, invocation policies,
references, helpers, and declared MCP dependencies are in skills-filesystem.json.
Package versions are encoded in plugin paths and plugins.json. System bundle
upstream commit is unknown. Original immutable installation commits for LikeC4
and Playwright remain unknown, as their current attribution files state.

## Reconciliation and system reproduction

Fresh isolated CLI discovery returned three personal skills and five system
skills: imagegen, openai-docs, review-agent, skill-creator, skill-installer.
No discovery errors occurred. A disposable repo copy of plugin-creator loaded
successfully with repo scope. Starting discovery replaced the disposable managed
marker and removed all eleven copied plugin-creator files. Before/after hashes
of the active system directory were identical.

This independently reproduces the managed bundle conflict on current 0.159.1.
It establishes system refresh versus repo-entrypoint behavior; it does not
establish intended ownership, upstream root cause, or a supported fix. The
isolated fixture had no copied authentication, configuration or plugin state.
Consequently missing plugin skills in that fixture are expected and say nothing
about active-home plugin discovery. Active-home app-server discovery was not run
because it can mutate the active system bundle, which this audit forbids.

The review-agent and template skills declare allow_implicit_invocation: false.
Their absence from the automatic session catalog is consistent with that policy,
but this audit did not execute an explicit-invocation client UI lookup to prove
why the session omitted them. Classify the explanation as plausible/unresolved,
not proven defect. The system plugin-creator discrepancy is reproduced.
The session's supplied plugin versions match current installed package paths.
No obsolete cache versions were found in this inventory.

Commands and evidence: `codex --version`, `codex plugin list --json`,
collect_inventory.py (read-only inventory), and reproduce_discovery.py
(disposable CODEX_HOME, no model execution). The latter sends initialize,
initialized, and skills/list with forceReload. Its sanitized response and
before/after comparison are in isolated-cli-discovery.json. The fixture is
owner-private under /tmp, outside discovery roots. Exact user paths in helper
scripts are local fixture locations, not private source contents.

## Limits

The file manifests are inventory evidence, not a claim of full security or
behavioral validation. static-inventory-checks.json contains literal Markdown
link candidates, not validated defects; example placeholders and references to
plugin virtual resources require interpretation. The scan enumerated standard
ancestor roots for this workspace and maintained repository, not every nested
repository on the machine. Windows-client discovery was not tested. Live remote
plugin registration, authenticated integrations and server behavior were not
invoked. Historical repository docs informed reproduction design only; all
reported version, package, hash and discovery observations were collected anew.
