# Behavioral coverage matrix

All grades are narrow simulated-response grades. No row is an end-to-end acceptance result.

S = pass in simulation; F = failure; U = untested. Explicit unavailable-dependency cases cover missing dependencies for plugin/system skills. Templates combine dependency and failure in one scenario. Clear Writing cw09 is an additional drafting failure outside the seven selection columns.

| Skill | Explicit | Implicit | Negative | Ambiguous | Missing dependency | Failure | Output contract | Native routing | Full live workflow |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| clear-writing | S | S | S | S | S | S | S | U | U |
| likec4-dsl | S | S | S | S | S | S | S | U | U |
| playwright-cli | S | S | S | S | S | S | S | U | U |
| imagegen | S | S | S | S | S | S | S | U | U |
| openai-docs | S | S | S | S | S | S | S | U | U |
| plugin-creator | S | S | S | S | S | S | S | U | U |
| review-agent | S | S | S | S | S | S | S | U | U |
| skill-creator | S | S | S | S | S | S | S | U | U |
| skill-installer | S | S | S | S | S | S | S | U | U |
| context7-mcp | S | S | S | S | S | S | S | U | U |
| code-review | S | S | S | S | S | S | S | U | U |
| assess-patch-risk | S | S | S | S | S | S | S | U | U |
| attack-path-analysis | S | S | S | S | S | S | S | U | U |
| deep-security-scan | S | S | S | S | S | S | S | U | U |
| define-security-policy | S | S | S | S | S | S | S | U | U |
| finding-discovery | S | S | S | S | S | S | S | U | U |
| fix-finding | S | S | S | S | S | S | S | U | U |
| propose-security-hardening | S | S | S | S | S | S | S | U | U |
| security-diff-scan | S | S | S | S | S | S | S | U | U |
| security-scan | S | S | S | S | S | S | S | U | U |
| threat-model | S | S | S | S | S | S | S | U | U |
| track-findings | S | S | S | S | S | S | S | U | U |
| triage-finding | S | S | S | S | S | S | S | U | U |
| validation | S | S | S | S | S | S | S | U | U |
| verify-fix | S | S | S | S | S | S | S | U | U |
| vulnerability-writeup | S | S | S | S | S | S | S | U | U |
| artifact-template-analytics-dashboard | S | S | S | S | S | S | S | U | U |
| artifact-template-business-review | S | S | S | S | S | S | S | U | U |
| artifact-template-design-report | S | S | S | S | S | S | S | U | U |
| artifact-template-experiment-analysis | S | S | S | S | S | S | S | U | U |
| artifact-template-financial-budget | S | S | S | S | S | S | S | U | U |
| artifact-template-investment-committee-memo | S | S | S | S | S | S | S | U | U |
| artifact-template-legal-memorandum | S | S | S | S | S | S | S | U | U |
| artifact-template-market-trends-report | S | S | S | S | S | S | S | U | U |
| artifact-template-minimal-letterhead | S | S | S | S | S | S | S | U | U |
| artifact-template-operating-calendar | S | S | S | S | S | S | S | U | U |
| artifact-template-operating-review | S | S | S | S | S | S | S | U | U |
| artifact-template-project-kickoff | S | S | S | S | S | S | S | U | U |
| artifact-template-project-tracker | S | S | S | S | S | S | S | U | U |
| artifact-template-sales-pipeline | S | S | S | S | S | S | S | U | U |
| artifact-template-simple-dark-mode | S | S | S | S | S | S | S | U | U |
| artifact-template-simple-light-mode | S | S | S | S | S | S | S | U | U |
| artifact-template-strategy-memorandum | S | S | S | S | S | S | S | U | U |
| artifact-template-system-design | S | S | S | S | S | S | S | U | U |
| artifact-template-team-alignment | S | S | S | S | S | S | S | U | U |
| artifact-template-three-statement-forecast | S | S | S | S | S | S | S | U | U |
| maintain-space | S | S | S | S | S | S | S | U | U |
| manage-schedules | S | S | S | S | S | S | S | U | U |
| organize-space | S | S | S | S | S | S | S | U | U |
| write-page | S | S | S | S | S | S | S | U | U |
| plugin-management | S | S | S | S | S | S | S | U | U |
| create-pet | S | S | S | S | S | S | S | U | U |
| pets | S | S | S | S | S | S | S | U | U |
| update-pet | S | S | S | S | S | S | S | U | U |

The 54 installed rows exclude three identical maintained-source copies. See grades.json for all 373 response outputs and the separate runtime JSON files for executed checks. The earlier plugin evaluator template-untested list is superseded by template-evaluations.json; it remains an honest record of that evaluator's scope.
