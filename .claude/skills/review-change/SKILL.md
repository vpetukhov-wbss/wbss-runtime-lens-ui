---
name: review-change
description: Review a proposed or completed code change for correctness, security, data integrity, compatibility, reliability, performance, accessibility, tests, and maintainability. Use before merge or when an independent risk-focused review is requested.
---

# Review change

1. Read the task/acceptance criteria, repository instructions, full diff, callers/consumers, and relevant tests.
2. Prioritize correctness, security, data loss, compatibility, reliability, concurrency, and authorization over style.
3. Trace input to side effects and output; inspect negative/failure paths, cancellation, retries, and cleanup.
4. Check API/event/schema compatibility and mixed-version rollout.
5. Check tests for meaningful behavior and missing high-risk scenarios.
6. Check UI accessibility and all async/empty/error states when applicable.
7. Report only actionable findings with severity, concrete evidence, impact, and proportionate remediation.
8. Distinguish confirmed defects, risks requiring validation, and optional improvements.
9. If no material findings exist, say so and list residual verification gaps.
