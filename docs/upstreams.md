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
