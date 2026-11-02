---
name: debug-root-cause
description: Diagnose a defect, exception, test failure, race, rendering issue, or production incident by reproducing it and proving the root cause. Use when symptoms are known but the actual failing mechanism is not.
---

# Debug root cause

1. Capture expected behavior, actual behavior, exact environment/version, and smallest reproduction.
2. Read logs, traces, metrics, stack traces, recent diffs, and relevant code without assuming correlation is causation.
3. Form a short ranked hypothesis list; define evidence that would confirm or falsify each.
4. Instrument or isolate at boundaries; change one variable at a time.
5. Check concurrency, cancellation, lifetime/disposal, stale state, caches, time zones/culture, network retries, and data shape.
6. Identify the earliest incorrect state or decision, not merely the final exception.
7. Add a regression test that fails for the proven cause.
8. Propose the smallest fix and explain why it prevents recurrence and what it does not address.
9. Verify the reproduction, focused tests, and relevant broader tests.
