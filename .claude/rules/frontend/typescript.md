---
paths:
  - "src/**/*.ts"
  - "tests/**/*.ts"
  - "e2e/**/*.ts"
  - "*.ts"
  - "tsconfig*.json"
  - "package.json"
---

# TypeScript

- Read `tsconfig`, package manager/lockfile, runtime, module resolution, linter, formatter, and framework versions before editing.
- Use strict type checking. Do not weaken global compiler settings to silence a local error.
- Prefer inference for obvious local types and explicit types at public, serialized, callback, and architectural boundaries.
- Avoid `any`; use `unknown` and narrow it. Avoid unchecked assertions and non-null assertions unless a verified invariant is documented.
- Use discriminated unions and exhaustive `never` checks for closed state machines/results.
- Model optional, nullable, absent, and empty states deliberately; do not conflate them.
- Treat API, storage, environment, message, and URL data as untrusted at runtime. Validate at boundaries; TypeScript types disappear at runtime.
- Prefer immutable data and pure transformations. Avoid mutation shared across components/modules.
- Prefer named exports and coherent feature modules unless repository conventions differ.
- Keep public types small and intentional. Do not expose vendor/framework types across stable domain boundaries without a reason.
- Use `async`/`await`, propagate abort/cancellation signals, and handle promise rejections. Avoid floating promises.
- Do not add dependencies for trivial utilities. Check bundle, maintenance, security, licensing, and tree-shaking implications.
- Preserve source maps and actionable errors without leaking secrets or sensitive payloads.
