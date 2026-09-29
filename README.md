# Personal Codex Skills

Maintained personal skills for Codex, with source provenance and behavioral
checks. This repository uses the documentation, governance, templates, and
validation layout of `frame-and-sample`, adapted for skills.

## Skills

| Skill | Purpose | Installation |
| --- | --- | --- |
| [clear-writing](skills/clear-writing/SKILL.md) | Draft, edit, or detect formulaic prose while preserving meaning and voice | Personal standalone skill |

`clear-writing` combines selected guidance from Stop Slop and No AI Slop.
It replaces the personal `stop-slop` installation. Taste Skill is excluded.

## Repository layout

- `skills/`: deployable skill bundles, including attribution and notices.
- `evals/`: behavioral cases and observed results.
- `docs/`: provenance, installation, maintenance, and audit records.
- `templates/`: a reusable evaluation report format.
- `.github/`: contribution, review, and validation configuration.

## Use and maintenance

Invoke `$clear-writing` explicitly or let Codex select it for prose work.
Use a detection-only request when you want findings without a rewrite.

Read [installation and recovery](docs/installation.md),
[upstream provenance](docs/upstreams.md), and
[evaluation cases](evals/clear-writing/cases.json) before changing an installation.
Only the reviewed skill directory is deployed; repository governance and evals
are not copied into the active skill folder.

## License

New content is [MIT licensed](LICENSE.md). The deployed skill retains both
[upstream notices](skills/clear-writing/ATTRIBUTION.md).
