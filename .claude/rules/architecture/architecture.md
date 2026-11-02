# Architecture rules

- Choose the smallest architecture that protects current invariants and expected change.
- Organize complex domains around business capabilities; use straightforward layers for simple CRUD.
- Keep transport, persistence, and vendor concerns outside core business policy where change isolation justifies the boundary.
- A module owns its behavior, schema/data, and internal types. Cross-module access uses explicit public contracts.
- Do not share mutable database tables across independently deployed services.
- Keep a transaction within one consistency boundary where possible; coordinate long-running work explicitly.
- Separate domain events from versioned integration events.
- Use an outbox/inbox when durable messaging must agree with database state.
- Do not introduce microservices without independent deployment/ownership/scaling or isolation needs and operational readiness.
- Do not introduce CQRS, a mediator, event sourcing, a generic repository, or mapping layers by default.
- Record consequential decisions with context, options, consequences, validation metric, and revisit trigger.
