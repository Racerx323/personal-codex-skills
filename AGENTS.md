# Personal Codex Skills

## Placement and scope

- Put installable skills under `skills/<name>/` with a short `SKILL.md` entrypoint.
- Put conditional guidance in each skill's `references/` directory.
- Keep evaluation inputs and observed results under `evals/`.
- Put installation, maintenance, provenance, and rollback guidance under `docs/`.
- Use `templates/` for reusable authoring patterns.
- Install personal skills under `$HOME/.agents/skills`; keep backups outside all discovery roots.
- Keep upstream copyright and permission notices with derived skill content.
- Do not install upstream updates automatically. Review an immutable commit first.
- Preserve user intent, factual uncertainty, technical literals, and authorization boundaries.

## Validation

Run `pre-commit run --all-files` for repository checks. Validate each changed
skill with the installed skill-creator `quick_validate.py`, check its relative
links, and exercise the relevant cases in `evals/clear-writing/cases.json`.
Record actual outputs and distinguish author self-review from independent testing.
A syntax check does not establish writing quality or model routing behavior.

## Reviews

Use draft pull requests during development. The CodeRabbit configuration follows
the shared draft-first policy. An external review requires the requested change
scope to be clear; repository scaffolding alone does not send review data.
