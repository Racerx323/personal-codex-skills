# Source provenance and updates

[upstreams.json](upstreams.json) records immutable upstream commits and SHA-256
hashes of the reviewed source files. The installed Stop Slop entrypoint matched
the reviewed upstream entrypoint at consolidation time.

The merged skill uses Stop Slop's pattern catalog and No AI Slop's minimal-edit,
voice-preservation, detection, and evaluation guidance. It intentionally drops
blanket grammatical bans, arbitrary quality scores, mandatory change summaries,
and instructions that might flatten uncertainty or technical precision.

The repository layout follows `frame-and-sample`: root instructions and README,
`docs/`, `templates/`, `.github/` governance, local pre-commit tools, and the shared
baseline workflow. Domain-specific folders and prose were not copied. The user
selected MIT for new content; upstream MIT notices remain in the skill bundle.

## Update procedure

1. Resolve the candidate upstream revision to a full commit ID.
2. Compare it with the recorded commit and review changed instructions and notices.
3. Adopt only changes supported by this skill's scope; do not concatenate entrypoints.
4. Update source hashes and attribution, then run static checks and behavioral cases.
5. Record actual results and preserve the prior installed tree before replacement.

Keep one deployed writing skill. Do not install the upstream skills alongside
Clear Writing as an update mechanism. Taste Skill is excluded by user decision.

## LikeC4 and Playwright maintenance sources

LikeC4's installed provenance points to the likec4.dev well-known skill tarball;
the original immutable revision was not recorded. Compared against
`likec4/likec4@33dbc2d34c399a99daf96e92fc28fe5d280a7fd5`. Its MIT notice is
preserved in the bundle. Existing evaluations were retained under evals/likec4-dsl.

Playwright's installed skill predates or differs from the bundled npm entrypoint.
Its original installed revision is unknown. Compared with @playwright/cli0.1.22
and `microsoft/playwright-cli@b85c7a736bb473bf55b584e54a09ffa698d6d871`. The
Apache-2.0 license is preserved; this derived bundle is not relicensed as MIT.

Comparison commits are not claims about the original installed revisions.
Adaptations shorten entrypoints, move catalogs to references, correct verified
DSL/CLI errors, remove unsafe cleanup/storage suggestions and preserve test
assertions. Imported Markdown formatting was normalized to repository checks.
