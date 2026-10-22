# Attribution

This personal Codex adaptation derives its audit and remediation workflow from
Fernando Paladini's [harness-score](https://github.com/paladini/harness-score),
MIT licensed, at commit `b8c3941ba49edcf69f973e26c1940dae487f7c7a` (v1.8.3).

Reviewed sources:

- `plugins/claude-code/skills/harness-engineering/SKILL.md`
- `plugins/claude-code/commands/harness-audit.md`
- `PLUGINS-ROADMAP.md`
- `LICENSE`

The upstream notice is preserved in [LICENSE.txt](LICENSE.txt). This is a
locally maintained adaptation, not an upstream Codex plugin. It combines audit
and requested remediation in one skill, uses Codex instruction and skill paths,
removes Claude Code hook recipes, respects repository version pins and existing
gates, and checks scan completeness before interpreting scores. Upstream updates
are reviewed manually; the installed copy does not follow upstream automatically.
