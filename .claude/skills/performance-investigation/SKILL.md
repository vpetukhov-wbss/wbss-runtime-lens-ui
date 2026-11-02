---
name: performance-investigation
description: Investigate and improve a measured latency, throughput, allocation, startup, database, network, rendering, or mobile performance problem. Use when a performance target or symptom exists; do not use for speculative micro-optimization.
---

# Performance investigation

1. Define the user-facing target, workload, environment, and acceptable tradeoffs.
2. Reproduce and record a baseline with suitable profiler, trace, benchmark, query plan, or browser/mobile tooling.
3. Attribute cost to algorithm, database, network, serialization, rendering, allocation/GC, startup, or contention.
4. Fix the highest-impact root cause with the smallest maintainable change.
5. Check correctness, staleness, memory, power, bandwidth, cache invalidation, and failure amplification.
6. Re-run the same measurement and report absolute and relative change with variance.
7. Add a regression benchmark, budget, metric, or query-plan assertion when the path is critical.
8. Remove complexity if it no longer earns measurable value.
