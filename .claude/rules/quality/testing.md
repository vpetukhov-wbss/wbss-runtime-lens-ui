---
paths:
  - "**/*{Test,Tests,Spec,Specs}*.{cs,ts,tsx,js,jsx}"
  - "**/{test,tests,spec,specs}/**"
---

# Testing

- Choose the cheapest test that provides adequate confidence: pure unit, component, integration, contract, or end-to-end.
- Test externally meaningful behavior, invariants, state transitions, contracts, and failure paths.
- Use Arrange-Act-Assert or Given-When-Then where it improves readability; one test may contain several assertions about one behavior.
- Name tests by scenario and expected outcome, not method implementation.
- Keep tests deterministic: control time, randomness, IDs, culture, network, and concurrency.
- Prefer real domain objects and fakes for simple boundaries. Mock volatile external collaboration, not every internal class.
- Use a real representative database/container for persistence semantics, migrations, constraints, and provider-specific queries.
- Use contract tests for independently evolving APIs/events and end-to-end tests for a small set of critical journeys.
- Assert authorization isolation, concurrency conflicts, cancellation, retry/idempotency, and malformed input where relevant.
- Do not make production APIs worse only to satisfy tests. Improve seams at actual boundaries.
- Avoid sleeps and timing guesses; synchronize on observable conditions with bounded deadlines.
- A regression fix requires a failing test or a documented reason why an automated test is impractical.
