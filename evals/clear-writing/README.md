# Clear Writing evaluation

Use [cases.json](cases.json) for draft, edit, detection, and routing scenarios.
Supply the case's request and input, plus its voice sample when present. Keep the
criteria and preservation expectations out of the generation prompt.

## Preservation checks

Record the actual response and any tool actions. Check every `preserve_exact`
string byte-for-byte in the response, then review the case's criteria for meaning,
stance, uncertainty, authorization boundaries, and requested editing scope.
For detection, verify the original was not rewritten; for routing, verify whether
the skill was selected. A generated response cannot prove routing or tool behavior.

Literal checks are necessary where specified but cannot establish semantic
preservation. Treat a changed fact, objection, causal strength, or prerequisite as
a preservation failure even if readers prefer the rewrite. No-change edits and
no-finding detection results are valid when the source warrants them.

## Paired reader judgments

Compare baseline and candidate skills on the same requests, source texts, model,
and settings. Keep each version's actual output and identify the skill revision
or content hashes. Review preservation separately before comparing reader value.

Present outputs as A and B without version labels. Counterbalance their order:
judge each pair in both orders. Ask separately which is clearer, more useful for
the requested task, and closer to the supplied voice when applicable. Allow ties
and record a brief reason. Report preservation failures alongside preferences;
do not let a preference win conceal a failure.

Keep the same model and settings between conditions, and record repetitions,
judge identities, order disagreements, and skipped or inapplicable judgments.
Label model judgments as model judgments and author self-review as self-review;
neither establishes independent human preference. Do not use AI probabilities,
phrase counts, or sentence-length targets as writing-quality acceptance gates.

## Recorded checks

[qualification.json](qualification.json) records the outputs exercised during
this adaptation, their literal checks, and author self-review of the criteria.
It does not establish an improvement over the baseline, independent preference,
or fresh-client skill routing. Run the paired protocol to measure those writing
comparisons.

[routing.json](routing.json) separately records four actual fresh CLI sessions
after installation. Detection loaded the skill; short edit and draft requests
answered without visible skill reads; the code-only request did not load it.
This is mixed routing evidence, not proof that automatic selection is reliable.

[routing-with-rule.json](routing-with-rule.json) records the retest after adding
the scoped workspace `AGENTS.md` rule. Three fresh trials per scenario loaded the
installed skill for all nine prose requests and left it unloaded for all three
code-only requests. The prompts and model configuration match the earlier test;
the report records the rule and workspace instruction hashes. These results
support the rule for the tested CLI scenarios, without guaranteeing future
selection or establishing IDE and native Windows behavior.
