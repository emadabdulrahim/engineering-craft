---
name: review
description: "Review a change for whether it is the right solution, whether it is correct, and what it should clean up, so the codebase ends up better than before. Use when asked to review code, a diff, a branch, or a PR, and before calling substantial work done."
slash: true
---

# Review

A review exists so that each change leaves the codebase simpler, more correct, and easier for the next person or agent to work in. Read the change and the code around it the way a senior engineer who has to own it would. Ask the questions below in order, because the answer to an earlier one can make the later ones moot.

## Is this the right solution?

- Does it fix the cause where the rule or state belongs, or does it cover a symptom with another condition, fallback, or layer? Is the fix at the layer that owns the problem, which may be the server, the data, or the requirement rather than where the symptom showed up? Does it fix the whole class of problem or only this instance?
- Did the design get simpler? Consider what a maintainer now has to know and how many places must change together. A change that works but makes the next change harder is a finding.
- Are the data model and the module boundaries right for what the system now does? Look for a fact stored twice, states that can contradict each other, a lifecycle spread across flags that would be safer as an explicit state machine, callers that must know a module's internals, and work that is slow because of how data is shaped or fetched.
- Would you build it this way starting fresh? When a clearly better design exists, say what it is and what it would cost to get there.

## Is it correct?

Trace real inputs through the change and look for what a careful reader finds: empty and boundary cases, failure and partial-failure paths, ordering and concurrency, and behavior that differs from what was asked. Check that the verification exercises the thing that changed.

## What did it leave behind or walk past?

Look at the area the change touched: logic that now has one more copy, code the change made dead, names and comments that no longer match, and nearby structure that could be consolidated or simplified while it is open.

## What to do with what you find

Confirm a finding by reading the code path or running it before you report it, and say which findings are confirmed and which are suspicions. Rank them by consequence, and prefer a few that matter over a long list of small ones. When the change is sound, say so and say what you checked.

When you review your own work, or are asked to fix, make the improvements that are small and safe as part of the same change, keep cleanup that preserves behavior distinguishable from behavior changes, and verify again afterward. Report what is too large or too risky to fold in, each with a recommendation. When you review someone else's change, report and recommend only.
