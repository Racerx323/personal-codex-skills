# Unresolved storage findings

These three low-severity findings remain relevant to installed helpers and
Codex Security 0.1.31. Their
[source hashes](../evals/issues/storage/selected-security-source-hashes.json)
and the installer fixture's helper hash matched the installed files on
October 4, 2026. Evidence was originally collected on September 29; matching
hashes do not establish current exposure, exploitation or a complete security
audit. Keep this evidence while the source mechanisms or local mitigations apply.

[The calibrated findings](../evals/issues/storage/findings.json) describe
attacker prerequisites, counterevidence and limitations.

| Issue | Evidence and current boundary |
| --- | --- |
| SEC-01: installer staging parent | Two mocked-download, same-UID parent-replacement simulations installed the replacement marker. No real cross-user race or active skill installation was tested. The shared staging parent needs ownership and privacy validation upstream. |
| SEC-02: manual helper cache | Source review identified replacement of returned cache paths after verification. Use only the private wrapper; no direct helper or shared-cache reproduction was executed. |
| SEC-03: security supplemental artifacts | Selected decoded-bundle and Python traces identified missing owner/mode checks for a predictable temporary root. Live exposure remains unverified; no temporary artifact import was performed. |

The offline [installer fixture](../evals/issues/storage/installer_fixture.py)
and [observed result](../evals/issues/storage/installer-fixture.json) are retained
for SEC-01. It uses disposable storage and writes an adjacent sanitized report;
it does not install into active skill directories.

Invoke the managed manual helper only through
`python3 "$HOME/.local/share/codex-hardening/fetch-manual-private.py"`.
The wrapper validates its fixed private cache. Codex Security supplemental
artifacts require `storage: "persistent"` with inline `content`, or prepared/read
persistent storage. Temporary storage and `sourcePath` imports require prior
verification of the actual plugin process's owner-private temporary parent.
Do not patch managed bundles or restart a plugin to work around these findings
without separate authorization.
