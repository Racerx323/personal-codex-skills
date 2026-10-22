---
name: harness-engineering
description: Audit a repository with harness-score and implement requested agent-harness improvements to instructions, skills, guardrails, or CI. Use for harness-maturity audits and remediation of scanner findings.
---

# Harness engineering

Audit the requested repository and improve its agent harness within the user's
scope. Use the [Harness Score guide](https://paladini.github.io/harness-score/)
and the failed checks' recipe links when implementation detail is needed.
Upstream provenance and adaptation notes are in [ATTRIBUTION.md](ATTRIBUTION.md).

## Audit

- Resolve the individual repository root and read its applicable instructions.
  A multi-repository workspace is not one repository-wide scan target.
- Check the installed `harness-score --version` against the repository's CLI pin,
  when present. Report a missing or mismatched CLI; installation or upgrades are
  separate work unless the user requested them.
- Run from that repository root, leaving user/system scopes disabled:

  ```bash
  harness-score . --gate maturity --min-level 0 --json
  ```

  Capture output privately outside the scan root. Relevant ignored and untracked
  files affect results; identify whether this is a working-tree scan or a clean
  snapshot comparison. Keep before/after inputs and scanner versions comparable.
- Check the exit status and `verdicts.maturity.status` before interpreting scores.
  Exit 2 or an incomplete verdict means the maturity result is unavailable;
  report reasons and do not publish a level or badge as authoritative. Preserve
  the scanner's diagnostics instead of substituting a model-generated score.
- For a complete report, give the level, total, dimension percentages, and next
  level gaps. Prioritize failed applicable checks by relevance to this repository,
  then by points. Report evidence, remediation, and `docsUrl` for the top gaps.
  Distinguish an unrecognized existing tool from an absent safeguard. The scanner
  detects infrastructure; it does not establish functional correctness.
- An audit-only request ends with findings. Remediation requires a request to
  make changes; do not infer it from a low score.

## Requested improvements

Use the existing tooling and actual commands. Follow recipes suited to the
repository; avoid adding software, empty skills, or tests merely to earn points.

- Context: keep concise repository instructions in `AGENTS.md`; use nested
  `AGENTS.md` for directory-specific guidance when needed.
- Skills: use `.agents/skills/` for shared repository procedures and
  `$HOME/.agents/skills/` for personal skills. Invoke Codex skills with `$name`;
  do not install another editor's command files as Codex slash commands.
- Guardrails: use the client's supported sandbox and approval settings plus
  appropriate repository checks. Claude Code and Cursor hook JSON are not Codex
  hook formats. Changes to client permissions need their own requested scope.
- Sensors and CI: extend real lint, test, format, or schema checks and existing
  workflows. Documentation repositories do not need an invented application
  runtime or type checker. Keep any existing Harness Score gate and publication
  restrictions; a higher minimum or wider adoption needs explicit approval.
- Hygiene: follow existing ignore, license, and secret-handling conventions.
  Credential removal, rotation, or history rewriting are separate operations.

Run the checks relevant to the changed artifacts, then repeat the comparable
scan. Report observed improvements and remaining gaps, without treating a score
increase as behavioral proof. Keep publication and live deployment within the
user's authorization.
