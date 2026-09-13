# Design guidance

Resolve the decisions that would be expensive to undo. Scale the explanation to the uncertainty and consequence, not the number of files. Use the questions relevant to this task, not every topic below.

## Establish the contract

Identify the expected behavior, constraints, and invariants. Separate requirements from assumptions. Look at real callers and representative data before designing an interface.

Resolve ambiguous domain terms with concrete scenarios. Check whether the code matches the stated behavior, and distinguish an implementation defect from a change in requirements. Use the project's established vocabulary rather than imposing a new glossary.

Sketch a caller, data model, or interaction when it exposes a consequential choice. Do not require empty function bodies or multiple proposals when the existing design already answers the question.

## Put knowledge and state with their owners

Group code by the rules and responsibilities it owns rather than incidental execution order. Keep an invariant with the code that enforces it. Callers should not need to coordinate several modules to maintain one rule.

For stateful behavior, establish who creates, reads, changes, persists, and disposes of the state. Make transitions and resource lifetime explicit. Avoid storing values that must be synchronized when they can be derived from one source.

Use a state machine, discriminated union, registry, or another structure when it removes invalid combinations or repeated decisions. Do not impose one merely because the pattern is familiar.

## Keep boundaries useful

Prefer cohesive modules with explicit dependencies and small, meaningful contracts. Keep side effects visible. Separate policy from infrastructure when doing so isolates real variation or makes important behavior testable.

An interface includes everything a caller must know: ordering, invariants, errors, configuration, and performance characteristics, not just types or method signatures. Judge an abstraction by how much knowledge it removes from callers, not by the size of its implementation.

Prefer composition over inheritance hierarchies that couple unrelated behavior. Introduce a shared abstraction when consumers share a rule and should change together. Keep superficially similar code separate when its responsibilities differ.

An interface, adapter, event bus, generic framework, or new dependency needs a concrete job. Name the coupling or complexity it removes and the complexity it introduces. Do not build hypothetical consumers or extension points.

Apply the deletion test when a module seems unnecessary. If removing it removes complexity, it may not earn its place. If its responsibilities would spread across callers, it is doing useful work. Trace where the responsibility goes rather than counting deleted lines.

## Design relevant failure and cost behavior

Consider cancellation, concurrency, partial success, retries, and unavailable dependencies where the feature can encounter them. Define how callers observe and recover from failure. Add only the mechanisms the contract needs. A retry is not safe merely because an operation failed.

Protect trust boundaries and avoid exposing sensitive data in errors or logs. Make failures diagnosable with useful context rather than logging every operation.

Identify likely costs in data growth, repeated work, I/O, and resource retention. Use representative measurements when a performance decision is material. Account for the complexity and correctness costs of caching or concurrency before adding them.

## Choose and explain

Prefer the least complex approach that satisfies the contract and credible growth constraints. Compare alternatives only when the tradeoff is meaningful. Use a named pattern to solve a concrete problem, not to demonstrate architectural sophistication.

Briefly explain the consequential choice, its tradeoff, and how it will be verified. Use a diagram, example, or short design note only when it makes the decision easier to understand. Follow the project's convention for recording durable architectural decisions.

A durable decision record is useful when the choice is costly to reverse, surprising without context, and the result of a genuine tradeoff. Do not create a document merely because a design conversation occurred.

Resolve product ambiguity or commitments outside the request before proceeding. Otherwise, make the design decision and continue through implementation and verification without an automatic review gate.
