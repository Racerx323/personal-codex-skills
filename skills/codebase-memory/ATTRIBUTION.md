# Attribution

This personal Codex adaptation derives its graph-query, coverage, evidence, and
handoff guidance from DeusData's
[codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp), MIT licensed,
at immutable commit `a7158ac2f48ca646b4527341b76f930f2aeff87e` (v0.12.1).

The [upstream skill source](https://github.com/DeusData/codebase-memory-mcp/blob/a7158ac2f48ca646b4527341b76f930f2aeff87e/src/cli/cli.c)
is embedded as `skill_content`; it is not
a standalone `SKILL.md` bundle at this revision. The original copyright and
permission notice is preserved byte-for-byte in [LICENSE.txt](LICENSE.txt).

The adaptation keeps the workspace's vexp → Codebase Memory → Serena discovery
order, selects graphs by canonical repository root, and retains coverage,
pagination, source-fallback, and authorization boundaries. It omits fixed tool
counts, token-saving claims, unconditional session-start graph queries, automatic
delegation, and installation of upstream hooks or agent profiles.

Stable v0.12.1's session-repository watch limitation is explicit. Indexing another
root refreshes its graph without registering its watch; newer main-branch
documentation is not the installed release's contract. Local native qualification
confirmed the distinction. Review upstream changes manually before adopting them.

The skill is maintained locally and deployed as one personal bundle under
`~/.agents/skills/codebase-memory`. This bundle does not contain or install the
native CBM executable. Source hashes and review boundaries are recorded in the
repository's provenance and qualification records.
