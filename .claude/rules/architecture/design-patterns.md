# Design pattern policy

- Name the problem and axis of change before selecting a pattern.
- Prefer a language or framework feature when it expresses the design more directly.
- Use Strategy for genuinely interchangeable policies; keep a simple exhaustive switch when it is clearer.
- Use factories/builders when construction varies or must enforce invariants, not to hide ordinary constructors.
- Use Adapter at external or legacy boundaries and Facade to expose a stable small surface.
- Use Decorator or an explicit pipeline for orthogonal behavior; do not build deep inheritance hierarchies.
- Use State or a state machine when lifecycle transitions and invalid transitions matter.
- Use Specification only for reusable business predicates; do not create a leaky universal query DSL.
- Use Value Objects and Aggregates where business meaning and transactional invariants justify them.
- Use Repository only when an aggregate-oriented collection abstraction adds value beyond the native data API.
- Use Saga/process manager for long-running cross-boundary workflows with explicit compensation and idempotency.
- Reject patterns that add indirection without reducing change cost, defect risk, or operational risk.
