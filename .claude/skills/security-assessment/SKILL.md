---
name: security-assessment
description: Perform a focused application security and privacy assessment of a change, feature, API, mobile/web flow, or repository. Use for threat modeling, authorization, input/output handling, secrets, SSRF, XSS/CSRF, uploads, dependencies, and sensitive telemetry.
---

# Security assessment

1. Identify assets, actors, entry points, trust boundaries, privileges, sensitive data, and external dependencies.
2. Trace authentication and authorization separately; verify resource and tenant ownership on every path.
3. Review validation, canonicalization, output encoding, injection, SSRF, XSS, CSRF, path traversal, redirects, uploads, and deserialization according to the surface.
4. Review secrets, token/cookie lifetime, storage, transport, key rotation, and client exposure.
5. Review privacy minimization, retention, logs, traces, analytics, backups, and deletion.
6. Test abuse cases, size/rate limits, replay/idempotency, concurrency, and error information leakage.
7. Rank findings by exploitability, impact, evidence, and affected assets; distinguish confirmed issues from hypotheses.
8. Recommend the smallest effective remediation and a verification test.
9. Do not change code unless the task explicitly includes remediation.
