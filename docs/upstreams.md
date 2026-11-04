# Source provenance and updates

[upstreams.json](upstreams.json) records immutable upstream commits and SHA-256
hashes of the source files used by the maintained bundles. These provenance pins
identify derived content and license obligations; they are not tool upgrade pins.

The merged skill uses Stop Slop's pattern catalog and No AI Slop's minimal-edit,
voice-preservation, detection, and evaluation guidance. It intentionally drops
blanket grammatical bans, arbitrary quality scores, mandatory change summaries,
and instructions that might flatten uncertainty or technical precision.

Unslop contributes stance preservation, contextual hedge and boilerplate editing,
sample-based voice guidance, editing scope, and blinded comparison methodology at
commit `eaa3b92e0b54a29076df23ff6d846c5f81bed7b9`. Its MIT notice travels with
Clear Writing. The adaptation excludes blanket bans, artificial rhythm targets,
detector optimization, persistent activation, and upstream executable helpers.
See the [evaluation protocol](../evals/clear-writing/README.md) for preservation
checks and the distinction between author self-review and independent judgments.

The repository layout follows `frame-and-sample`: root instructions and README,
`docs/`, `templates/`, `.github/` governance, local pre-commit tools, and the shared
baseline workflow. Domain-specific folders and prose were not copied. The user
selected MIT for new content; upstream MIT notices remain in the skill bundle.

## Harness Engineering

The personal `harness-engineering` bundle adapts paladini/harness-score's MIT
audit command and Claude Code skill at immutable v1.8.3 commit
`b8c3941ba49edcf69f973e26c1940dae487f7c7a`. It retains audit-before-remediation
and the recipe families, replaces editor-specific paths and hooks with Codex
guidance, uses the installed version matched to repository pins, and rejects
incomplete results. It preserves existing gate and publication policies.

There is no upstream Codex bundle at the reviewed revision. Do not replace this
adaptation with the Claude Code or Cursor skill verbatim. See its
[attribution](../skills/harness-engineering/ATTRIBUTION.md) for the source paths.

## Codebase Memory

The personal `codebase-memory` skill adapts DeusData/codebase-memory-mcp's embedded
`skill_content` in `src/cli/cli.c` at v0.12.1 commit
`a7158ac2f48ca646b4527341b76f930f2aeff87e`. The MIT notice is preserved in the
bundle. The local adaptation retains workspace discovery order and authorization
boundaries, narrows queries to unresolved questions, and records stable-release
session-scoped watch behavior rather than adopting newer main-branch behavior.

See its [attribution](../skills/codebase-memory/ATTRIBUTION.md) and
[maintenance guide](codebase-memory.md). The provenance pin identifies reviewed
skill content; the separate native CBM installation has its own lifecycle.

## Update procedure

1. Resolve the candidate upstream revision to a full commit ID.
2. Compare it with the recorded commit and review changed instructions and notices.
3. Adopt only changes supported by this skill's scope; do not concatenate entrypoints.
4. Update source hashes and attribution, then run static checks and behavioral cases.
5. Record actual results and preserve the prior installed tree before replacement.

Keep one deployed writing skill. Do not install the upstream skills alongside
Clear Writing as an update mechanism. Taste Skill is excluded by user decision.

## LikeC4 and Playwright maintenance sources

LikeC4's upstream source is `likec4/likec4`, directory `skills/likec4-dsl`.
The homelab LikeC4 installation guide documents the Vercel Skills CLI command
using `https://likec4.dev/`; the installer's lock points to that site's well-known
skill tarball. The GitHub repository is the source, the tarball is the delivery
method, and `vercel-labs/skills` supplies the installer;
the original immutable revision was not recorded. Compared against
`likec4/likec4@33dbc2d34c399a99daf96e92fc28fe5d280a7fd5`. Its MIT notice is
preserved in the bundle. Existing evaluations were retained under evals/likec4-dsl.

Playwright's installed skill predates or differs from the bundled npm entrypoint.
Its original installed revision is unknown. Compared with `@playwright/cli` 0.1.22
and `microsoft/playwright-cli@b85c7a736bb473bf55b584e54a09ffa698d6d871`. The
Apache-2.0 license is preserved; this derived bundle is not relicensed as MIT.

Comparison commits are not claims about the original installed revisions.
Adaptations shorten entrypoints, move catalogs to references, correct verified
DSL/CLI errors, remove unsafe cleanup/storage suggestions and preserve test
assertions. Imported Markdown formatting was normalized to repository checks.
