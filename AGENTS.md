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


## vexp - Context-Aware AI Coding <!-- vexp v3.3.0 -->

### Context strategy: call run_pipeline ONCE at task start
If the task already names the files/symbols to touch, SKIP vexp. Otherwise one
`run_pipeline({ "task": "..." })` returns ranked pivot files with line ranges and
blast radius. Do NOT open files one by one to find your way around - every extra
tool call costs a turn. Call it again ONLY when the task moves to a new area.
`get_skeleton` for files to understand, not edit. `verify_done` before calling a
multi-file task complete, then RUN the tests it names.

### Query shape (do this)
Anchor the task on real identifiers (ClassName, functionName) or file paths:
`run_pipeline({ "task": "fix JWT expiry in AuthService.validateToken" })`

vexp runs entirely on this machine, index in `.vexp/`;
`run_pipeline` transmits nothing to any external service.
On `status: "degraded"` or 0 pivots the index is still building - use your own tools.
For literal string sweeps use your native search - do NOT route text sweeps through vexp.
Repo SOURCE only: logs, dist/, node_modules/ and files outside the repo are NOT indexed.
<!-- /vexp -->