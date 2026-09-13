---
name: craft
description: "Engineering judgment for substantive features, bug fixes, and refactors. Use when implementing or designing code changes, or when explicitly requested."
slash: true
---

# Craft

Deliver working software with less complexity for the next engineer. Choose the approach and sequence that fit the task. These are decision criteria, not a mandatory checklist or reply template.

## Understand before changing

- Understand the affected behavior, callers, data flow, and constraints. Read relevant project guidance and code, not the whole repository by default.
- For a bug, establish the failure and trace its mechanism before choosing a fix. Use reproduction, tests, logs, or instrumentation to distinguish evidence from a plausible explanation. If evidence is unavailable, name the uncertainty rather than claiming a confirmed cause.
- Fix the problem where its rules or state belong. Do not conceal a broken invariant with another conditional, fallback, or layer. Guards are appropriate where invalid input or failure is part of the contract.

## Make the design simpler

- Prefer composition and clear, declarative expressions of intent. Use ordinary functions, data structures, and straightforward control flow before frameworks or clever abstractions. A simple loop is better than an elaborate abstraction that hides it.
- Minimize duplicated knowledge, hidden state, indirection, and coordination between files. The simplest maintainable solution is not necessarily the smallest diff.
- Keep related behavior and invariants together. Give each fact an authoritative representation and derive other values when practical. Share code around a common rule or responsibility, not merely similar-looking text.
- Follow project conventions and reuse existing capabilities. Do not perpetuate a convention that causes the problem. Model meaningful states explicitly, derive types from their authoritative definitions, and validate untrusted data where it enters the system.
- Leave the affected code better. Include reasonably sized refactoring, consolidation, and organization in the same change when they clarify the implementation or remove related risk. Preserve behavior during structural cleanup and verify it alongside the requested change. Do not expand into an unrelated rewrite.
- Remove obsolete paths involved in the change. Avoid parallel implementations, compatibility shims, and speculative extension points. Keep simple code when no structural change earns its place.
- Consider algorithms, data access, network round trips, and resource lifetime. Measure before making non-obvious performance tradeoffs. Do not claim an improvement without evidence.

## Verify and finish

- Choose checks that establish the changed behavior and relevant failure modes. Exercise the actual feature or integration when correctness depends on it. A successful build alone does not establish runtime behavior.
- Add a test when it catches a plausible, meaningful failure that existing checks miss. Prefer stable behavior contracts over private call sequences or mock setup. For a regression, show that the check detects the original failure when feasible. Do not chase test counts or coverage percentages.
- Establish expected results independently of the implementation, using the contract, a worked example, or a trusted reference. Recomputing the expectation with the same algorithm can reproduce the same mistake and create false confidence.
- Verify coherent units of work before building further on them. Reuse existing checks before adding a custom harness. For refactors, establish which behavior must remain unchanged and check that contract.
- Continue through implementation, verification, and correction of failures caused by the change. Distinguish pre-existing failures from regressions. Report the result, relevant evidence, and remaining limitations without manufacturing sections or certainty.
- Make implementation decisions within the request. Ask when a material ambiguity changes the outcome or an action needs authorization. This skill does not authorize publishing, deploying, destructive actions, or changing Git history. Preserve unrelated user work.

## Route consequential design decisions

Read [design guidance](references/design.md) when the task introduces or materially changes module boundaries, shared contracts, state ownership, persistence, or cross-component coordination. Also read it when the user explicitly asks for architecture or design work.

Do not load it merely because the task adds a feature. Use the existing design when it fits.
