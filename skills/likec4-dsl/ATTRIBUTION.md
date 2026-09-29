# Attribution

Derived from the official [LikeC4 GitHub skill](https://github.com/likec4/likec4/tree/main/skills/likec4-dsl).
The workstation installation guide documents `npx skills add https://likec4.dev/`
with `--skill likec4-dsl --agent codex --global --yes`. The installer lock records
delivery from `https://likec4.dev/.well-known/agent-skills/likec4-dsl.tar.gz` on
2026-07-20. GitHub is the upstream source; the website archive is the recorded
installation transport. `vercel-labs/skills` is the installer, not the DSL author.
The original download did not record a commit or archive hash; it is not presented
as a verified immutable release.

The baseline was compared with
[LikeC4 commit 33dbc2d](https://github.com/likec4/likec4/tree/33dbc2d34c399a99daf96e92fc28fe5d280a7fd5/skills/likec4-dsl).
The entrypoint differs by one upstream title-escaping clarification.
LikeC4 is copyright 2023-2026 Denis Davydkov and is distributed under the
[MIT license](LICENSE.txt).

Local maintenance shortens the entrypoint, moves exact task guidance into a
conditional reference, preserves existing references and evaluation cases,
and clarifies topology ownership, version selection, and validation limits.
