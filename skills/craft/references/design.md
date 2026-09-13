# Design guidance

Focus on consequential decisions. Apply the relevant criteria below and scale the explanation to the uncertainty and cost of changing direction.

## Establish the contract

Use real callers, representative data, and concrete scenarios to clarify behavior, constraints, and domain terms. Separate requirements from assumptions and implementation defects from changed requirements. Use the project's vocabulary.

An interface includes everything callers need to use it correctly: ordering, invariants, side effects, errors, configuration, and performance characteristics, not just signatures. Make those obligations discoverable without requiring callers to read the implementation. Hide incidental details, not information needed for correct use.

## Put knowledge and state with their owners

Organize code around shared rules and responsibilities rather than execution order. Share code when consumers share knowledge and should change together, not merely because their implementations look similar.

For stateful behavior, establish who creates, changes, persists, and disposes of state. Keep transitions and resource lifetime understandable. Choose a representation that removes invalid combinations and duplicated decisions rather than requiring callers to keep them synchronized.

Keep shared mechanics inside the module that understands them. Avoid making each caller repeat setup, coordinate internal steps, or choose settings the implementation can determine safely. Keep genuine product policy with its owner. A larger implementation can reduce complexity for the system as a whole.

## Keep boundaries useful

Implement the capabilities needed now, with operations independent of incidental callers or UI flows. Prefer coherent operations over accumulating case-specific methods. Generality earns its place by simplifying current use, even with one caller, not by supporting hypothetical features.

Extract code when its contract lets readers understand the caller independently. Keep tightly related logic together when splitting it forces readers to reconstruct shared state or ordering across helpers. Function length alone is not a reason to split.

Use the deletion test for a questionable abstraction: while preserving its behavior, would removal eliminate complexity or merely spread its responsibilities across callers? Keep boundaries that reduce what readers must know. Name the concrete benefit before adding a layer or dependency.

## Design relevant failure and cost behavior

Before adding a special case, consider whether the representation or operation can handle it naturally. Give empty or boundary cases ordinary semantics where the contract permits. Preserve meaningful distinctions and observable failures; invalid input or failed work must not appear successful.

Consider cancellation, concurrency, partial success, retries, and unavailable dependencies when relevant. Define how callers observe and recover from failure. Verify retry safety rather than assuming it. Make failures diagnosable without exposing sensitive data.

Identify likely costs in data growth, repeated work, I/O, and resource retention. Account for the complexity and correctness costs of caching or concurrency before adding them.

## Choose and explain

Compare plausible alternatives when the tradeoff matters. Use a caller sketch, data model, or diagram when it helps evaluate the choice; the existing design may already be sufficient.

Explain consequential choices and how they will be verified. Keep non-obvious contract documentation near its owner and separate from implementation detail. Record a durable architectural decision using project conventions when it is costly to reverse, surprising without context, and the result of a genuine tradeoff.
