# Observability

- Use structured logs with stable event names and useful dimensions; do not build messages by concatenating data.
- Correlate work across HTTP, messaging, background jobs, database calls, and client-visible operation IDs.
- Trace meaningful boundaries and dependencies. Avoid a span per trivial method.
- Define metrics from operational questions: traffic, errors, latency, saturation, queue age/depth, retries, and business outcomes.
- Control label cardinality. Never use user IDs, raw URLs, exception text, or unbounded values as metric labels.
- Record exceptions once at the responsible boundary with context; avoid duplicate logging at every layer.
- Redact secrets and personal/sensitive data in logs, traces, baggage, and telemetry attributes.
- Separate liveness, readiness, startup, and dependency health semantics.
- Make alerts actionable and tied to user impact or exhausted error budgets, not raw noise.
- Ensure graceful shutdown drains or safely hands off in-flight requests/messages within a bounded deadline.
