---
name: refactor-safely
description: Improve internal structure while preserving observable behavior. Use for clean-code refactoring, dependency cleanup, decomposition, pattern replacement, duplication removal, or preparing a safe seam before a later change.
---

# Refactor safely

1. State the structural problem, affected behavior, and success measure.
2. Establish a green baseline and add characterization tests when behavior is insufficiently protected.
3. Separate behavior changes from refactoring wherever practical.
4. Make small reversible transformations and run focused tests between meaningful steps.
5. Prefer removing indirection and clarifying ownership over adding new layers.
6. Apply DRY only after stable common knowledge is clear; tolerate small duplication over a wrong abstraction.
7. Preserve public contracts, serialization, persistence, timing, exceptions, and side effects unless explicitly changed.
8. Compare complexity before/after: dependencies, branches, concepts, allocations/I/O, and testability.
9. Remove dead compatibility scaffolding only with usage evidence.
