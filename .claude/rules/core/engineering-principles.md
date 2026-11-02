# Engineering principles

- Optimize first for correctness and clarity, then maintainability, operability, security, and measured performance.
- Use KISS and YAGNI to reject speculative complexity.
- Use DRY for stable knowledge, not superficial textual similarity. Prefer AHA: tolerate small duplication until the correct abstraction is clear.
- Apply SOLID and GRASP as diagnostic lenses. Do not create an interface, service, or project for every class.
- Maximize cohesion and minimize coupling. Keep dependencies explicit and directed toward stable policy.
- Prefer composition over inheritance, pure transformations over hidden mutation, and explicit state over ambient/global state.
- Name by business meaning and intent. Avoid vague `Manager`, `Helper`, `Processor`, `Common`, and `Utils` types unless the role is genuinely precise.
- Keep functions focused, but do not fragment readable logic into trivial indirection.
- Model invalid states out where proportionate; validate untrusted input at system boundaries.
- Use comments for rationale, constraints, and non-obvious tradeoffs—not to narrate code.
- Delete dead code. Do not leave commented-out implementations or speculative extension points.
- Do not silently change behavior while “cleaning up.” Separate behavioral changes from mechanical refactoring when practical.
