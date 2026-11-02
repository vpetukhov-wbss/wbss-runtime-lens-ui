# Git and review hygiene

- Inspect status and diff before and after changes; preserve unrelated edits.
- Keep commits conceptually coherent and avoid generated/reformatted noise unrelated to the task.
- Never commit secrets, local configuration, credentials, build outputs, or environment-specific state.
- Explain non-obvious tradeoffs and compatibility/rollout concerns in the change description.
- Review API, schema, event, configuration, feature-flag, migration, and deployment changes for backward/forward compatibility.
- Prioritize review findings by correctness, security, data loss, compatibility, reliability, performance, maintainability, then style.
- Every finding must cite concrete evidence, impact, and a proportionate remedy; avoid speculative nitpicks.
- Do not declare a change safe based only on a green build. Verify behavior and risk-relevant tests.
