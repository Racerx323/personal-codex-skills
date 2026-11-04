---
name: codebase-memory
description: Query Codebase Memory MCP for unresolved structural questions about symbols, callers, dependencies, architecture, and change impact. Follow repository discovery order; use direct reads for literal searches and coverage gaps.
---

# Codebase Memory

Use the standalone CBM server already configured in Codex. Follow repository
instructions: vexp provides initial orientation when needed; CBM resolves
remaining structural questions; Serena provides targeted symbol reads and edits.
Do not repeat discovery that another tool has answered.

Select the entry from `list_projects` whose canonical `root_path` matches the
repository. Pass its returned project name to subsequent calls. For cross-repo
work, query each relevant project; the parent workspace is not a substitute.

Check `index_status` before relying on a graph. Reuse its generation and freshness
evidence until the project or source changes. Check watcher state when freshness
matters: the installed stable server watches only its active MCP session's
repository. An explicit index of a different root refreshes that graph but does
not register its watch. Open Codex in the target repository for auto-watch; from
a parent-workspace session, refresh the target explicitly when needed. Keep index
persistence off unless repository artifacts were requested. Index only authorized
repository roots.

Choose the smallest query that answers the question:

- `search_graph`: locate symbols and exact qualified names.
- `trace_path`: inspect callers, callees, and relevant relationships; select the
  direction and depth needed for the task.
- `get_code_snippet` or `get_file_outline`: inspect a bounded source unit.
- `get_architecture`: inspect broader relationships when needed.
- `detect_changes`: map a local diff to indexed symbols and possible impact.
- `get_graph_schema` and `query_graph`: resolve questions requiring graph schema
  or relationships that the dedicated tools do not express.

After identifying evidence paths, batch them in `check_index_coverage`; include
relevant scopes for negative or exhaustive claims. Follow result pagination.
No recorded gap does not prove completeness. Read current source for partial,
excluded, missing, or stale coverage. An empty graph does not prove absence or
dead code. Current source takes precedence over either index.

Keep graph work in the current agent unless delegation is authorized. If work is
delegated, pass the exact project, generation, scope, qualified symbols, paths,
coverage gaps, and unresolved questions. Do not assume a child has MCP access.

CBM processing and graph storage are local, but MCP processes have their own
permissions. Indexing, ADR writes, trace ingestion, and project deletion are
mutations; apply the user's task scope. Preserve required repository tests and
vexp completion checks.

Installation, updating, rollback, and Headroom ownership are documented in
`/home/aaron/code/homelab-docs/docs/codebase-memory-installation-and-lifecycle.md`.
See [attribution](ATTRIBUTION.md) for pinned upstream provenance and the local
adaptation boundary.
