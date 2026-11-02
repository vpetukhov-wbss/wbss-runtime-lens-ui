---
name: test-strategy
description: Design or improve a risk-based automated test strategy for a feature, module, migration, or repository. Use when choosing unit, component, integration, contract, end-to-end, performance, or security tests and defining coverage priorities.
---

# Test strategy

1. Map critical user journeys, business invariants, integrations, failure modes, and change hotspots.
2. Rank risks by impact and likelihood.
3. Select the cheapest test level that catches each risk with realistic semantics.
4. Keep domain logic under fast deterministic tests; verify data/provider behavior with integration tests.
5. Add contract tests at independently evolving boundaries and few end-to-end tests for critical journeys.
6. Cover authorization isolation, invalid data, conflicts, idempotency, cancellation, time, retries, offline/reconnect, and accessibility where relevant.
7. Define fixtures/builders, test data isolation, clock/randomness control, and parallel execution policy.
8. Identify slow/flaky tests and replace sleeps, shared state, and over-mocking.
9. Produce a prioritized matrix of risk, test, level, owner, and CI stage.
