# Clear Writing workspace routing

After installing Clear Writing, add this section to the workspace `AGENTS.md`
when prose requests should select the skill even for short tasks. Preserve the
workspace's other instructions. The rule applies within that workspace's scope.

```markdown
## Clear Writing routing

When the user asks to draft, edit, rewrite, proofread, or identify formulaic prose,
load and apply `clear-writing` before composing the result, including short
requests. Exclude code-only tasks and ordinary conversation.
```

The [routing retest](../evals/clear-writing/routing-with-rule.json) records the
tested rule, workspace instruction hashes, and results. It does not guarantee
future selection or establish behavior in other clients.
