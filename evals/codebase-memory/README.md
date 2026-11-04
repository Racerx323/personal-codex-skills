# Codebase Memory evaluations

[cases.json](cases.json) covers discovery order, direct-read routing, canonical
project selection, incomplete coverage, stable session-scoped watching, and
authorization boundaries. Supply each request and context to the evaluator;
keep the criteria separate when testing generated behavior.

Record actual tool actions and answers, then grade each criterion. Manual review
of the skill can establish that instructions address a case; it cannot establish
automatic model selection or compliance. Compare baseline and candidate under
the same model, settings, and requests when making a behavioral comparison.

[qualification.json](qualification.json) separates author self-review from native
CBM checks and fresh Codex discovery. The native checks use a disposable Git
repository with `compute` calling `increment`. A controlled symbol rename and
restoration test watch freshness. Start the MCP process in the fixture repository,
verify its watch and initial scan, and keep unrelated graphs unchanged. A process
started elsewhere provides the negative `not_session_project` case for stable
0.12.1. Delete only the disposable graph after testing.

Keep raw logs, local paths, credentials, and private repository snippets outside
this repository. Retain sanitized observations and exact source/deployment hashes.
Neither successful discovery nor native tool behavior proves that a model loaded
and followed the skill. Independent model-routing and behavioral comparisons
have not been run for this adaptation.
