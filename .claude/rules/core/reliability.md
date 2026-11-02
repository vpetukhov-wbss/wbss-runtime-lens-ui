# Reliability and failure semantics

- Distinguish validation/business failures, absence, conflicts, authorization failures, transient dependency failures, and programming defects.
- Never swallow exceptions. Catch only when adding context, translating at a boundary, compensating, or recovering.
- Preserve the original exception as the cause when translating.
- Propagate cancellation through every cancellable I/O and long-running operation. Cancellation is not an error to retry.
- Make time explicit and testable; avoid scattered calls to the system clock.
- Design commands that may be retried to be idempotent or protected by an idempotency key.
- Apply timeouts to remote operations. Retry only transient and safe work with bounded attempts and jitter.
- Use bounded queues/channels and backpressure. Avoid unbounded concurrency and fire-and-forget work.
- Define concurrency behavior: atomic update, optimistic conflict, pessimistic lock, or accepted last-write-wins.
- Never report success before durable work and required side effects meet the operation's consistency contract.
