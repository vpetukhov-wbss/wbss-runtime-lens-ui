---
name: architecture-decision
description: Evaluate and record a consequential architecture choice with evidence, alternatives, tradeoffs, fitness criteria, and a reversal trigger. Use for module boundaries, architecture style, service extraction, CQRS, event-driven design, persistence, framework, or build-vs-buy decisions.
---

# Architecture decision

1. Read repository instructions, current architecture, deployment, telemetry, ownership, and representative code.
2. State the decision question and distinguish facts, assumptions, and constraints.
3. Identify business invariants, change drivers, scale, security/compliance, operations, and team topology.
4. Present at least two viable options plus retaining the current design when viable.
5. Compare simplicity, coupling, consistency, latency, failure modes, operability, cost, migration, and reversibility.
6. Reject fashionable patterns that do not solve a demonstrated problem.
7. Recommend one option with consequences, rollout steps, compatibility, and rollback.
8. Define measurable fitness criteria and a date/event that triggers review.
9. Produce a concise ADR in the repository's established location and format only when requested.
