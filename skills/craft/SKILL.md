---
name: craft
description: "Engineering judgment for substantive features, bug fixes, and refactors. Use when implementing or designing code changes, or when explicitly requested."
slash: true
---

# Craft

Deliver working software that is easier to understand and change. Use these criteria to exercise judgment, not as a mandatory checklist or reply template.

## Understand before changing

- Understand the affected behavior, callers, data flow, and constraints. Follow project conventions and reuse existing capabilities, while questioning patterns that cause the problem. Read what the change requires, not the whole repository by default.
- For a bug, establish the failure and trace its mechanism using reproduction, tests, logs, or instrumentation. Distinguish evidence from a plausible explanation and name unresolved uncertainty.
- Fix the problem where its rules or state belong. Guards should enforce a meaningful contract, not conceal a broken invariant with another conditional, fallback, or layer.

## Make the design simpler

- Judge simplicity by what a maintainer must know to make a correct change, how many places must change together, and how discoverable those dependencies are. A smaller diff or more helpers is not inherently simpler.
- Prefer composition and readable expressions of intent. Use declarative code when it clarifies behavior and straightforward control flow when that is clearer. Choose abstractions for the understanding they save, not their size or pattern name.
- Keep related behavior and invariants together. Represent each fact authoritatively and derive other values when practical. Model meaningful states explicitly, derive types from their authoritative definitions, and validate untrusted data at entry points.
- Include reasonably sized, related refactoring and consolidation when they clarify the requested change or reduce its risk. Preserve behavior during structural cleanup. Remove obsolete paths instead of retaining parallel implementations or compatibility shims; keep unrelated cleanup out of scope.
- Document non-obvious contracts and rationale near their owner. Add information that names, types, and code do not communicate clearly rather than narrating statements.
- Consider algorithms, data access, network round trips, and resource lifetime. Measure material performance tradeoffs and support improvement claims with evidence.

## Verify and finish

- Verify coherent units before building further on them. Check changed behavior, relevant failure modes, and contracts preserved by refactors. Exercise the actual feature or integration where correctness depends on it; a build alone does not establish runtime behavior.
- Reuse existing checks. Add tests for meaningful failures they miss, using stable behavior contracts and expectations independent of the implementation. For regressions, show that the check detects the original failure when feasible. Test counts and coverage percentages are not the goal.
- Continue through implementation, verification, and correction of failures caused by the change. Distinguish pre-existing failures from regressions and report the result, evidence, and remaining limitations.
- Make implementation decisions within the request. Ask when a material ambiguity changes the outcome or an action needs authorization. Preserve unrelated user work. This skill does not authorize publishing, deploying, destructive actions, or changing Git history.

## Route consequential design decisions

Read [design guidance](references/design.md) for material changes to module boundaries, shared contracts, state ownership, persistence, or cross-component coordination, or for explicit architecture work. Otherwise, use the existing design when it fits.
