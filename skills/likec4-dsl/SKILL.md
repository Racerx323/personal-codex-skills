---
name: likec4-dsl
description: Create, edit, or explain LikeC4 models and exact CLI commands. Use for .c4/.likec4 files, predicates, deployment and dynamic views, relationship matching, or validation/export; not generic prose or unrelated UI work.
---

# LikeC4 DSL

Use the existing project's architecture and conventions. Preserve explicit
output constraints and verify the edited model with the project's toolchain.

## Establish scope

Find the nearest LikeC4 configuration and the relevant specification, model,
and views. Read existing definitions before adding kinds or changing relationships.
Do not invent deployment hosts, addresses, ownership, or physical topology.
Ask when those facts are necessary and missing. Create a project or specification
only when the task calls for one; inspection or explanation does not require edits.

Use the project's installed LikeC4 version and lockfile. Consult current official
documentation through Context7 for CLI or DSL details, then check local help when
version-specific behavior matters. Do not install or downgrade a tool to satisfy
an old version example in a reference.

## Read the relevant reference

| Task | Reference |
| --- | --- |
| Project scope and config | [configuration](references/configuration.md) |
| Kinds, tags, and styles | [specification](references/specification.md), [style tokens](references/style-tokens-colors.md) |
| Elements, relationships, FQNs | [model](references/model.md), [identifier validity](references/identifier-validity.md) |
| Include/exclude and wildcard semantics | [predicates](references/predicates.md), [wildcards](references/include-predicates-wildcards.md) |
| Static views | [views](references/views.md) |
| Deployment nodes and instances | [deployment](references/deployment.md) |
| Sequence, parallel, and branching flows | [dynamic views](references/dynamic-views.md) |
| Exact snippets or strict output | [task contracts](references/task-contracts.md) |
| Commands and validation | [CLI](references/cli.md) |
| Failures or examples | [troubleshooting](references/troubleshooting.md), [examples](references/examples.md) |
| Bidirectional relationships | [bidirectional syntax](references/relationships-bidirectional.md) |
| LeanIX/draw.io bridge | [bridge guidance](references/bridge-leanix-drawio.md) |

Read only the references needed for the task. Retain exact distinctions between
`*`, `_`, and `**`; use FQNs where required across files. For relationship extension,
match source, target, kind, and title as needed to select the intended relationship.
Named deployment instances use `IDENTIFIER = instanceOf ELEMENT_ID` inside a
deployment node, never at the deployment root. Ask for the containing node when
it is unknown, or clearly label a fragment for insertion into an existing node.

## Validate and deliver

For source changes, validate each edited DSL file with structured output:

```bash
likec4 validate --json --no-layout --file /path/to/project/model.c4 --file /path/to/project/views.c4 /path/to/project
```

Repeat `--file` for the actual edited files. Relative file filters resolve against
the command working directory; prefer absolute file paths when specifying a
different project directory. Check `filteredFiles` matches the
intended DSL-file count. Report `filteredErrors`, `totalErrors`, and process status
accurately. Zero filtered errors does not establish project health or prove other
errors are unrelated; inspect dependencies before making that claim. Run broader
project validation when cross-file changes or repository policy require it.
`--no-layout` does not establish rendered-layout correctness. Rendering/export
requires the configured browser/runtime and appropriate execution permissions.

For strict command/snippet-first requests, give the requested artifact first and
avoid unrequested alternatives. Never claim validation ran unless it did. Follow
repository-specific formatting and checks. See [attribution](ATTRIBUTION.md) for
source and license details.
