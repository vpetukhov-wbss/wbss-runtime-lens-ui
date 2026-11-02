# Performance and scalability

- Do not optimize from intuition alone. Establish a target, representative workload, baseline, and measurement.
- Fix algorithmic, database, network, serialization, rendering, and allocation bottlenecks in that order of likely impact.
- Bound data, concurrency, queues, retries, request bodies, uploads, and caches.
- Avoid N+1 I/O, chatty service calls, repeated serialization, redundant renders, and loading unused columns/graphs.
- Paginate or stream large data with deterministic ordering and cancellation.
- Cache only with ownership, key, variation, staleness, invalidation, size, and privacy rules. Prevent cache stampedes.
- Pool or reuse expensive resources through supported framework facilities; do not pool objects with unsafe retained state.
- Use spans, `ValueTask`, source generation, memoization, compiled queries, and manual virtualization only when profiling justifies complexity.
- Include cold start, steady state, peak load, mobile device limits, poor networks, and failure/retry amplification where relevant.
- Add a regression benchmark or observable metric for critical optimizations.
