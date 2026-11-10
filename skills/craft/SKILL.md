---
name: craft
description: "Engineering judgment for substantive features, bug fixes, and refactors. Use when implementing or designing code changes, or when explicitly requested."
slash: true
---

# Craft

Deliver working software that leaves the codebase simpler, faster, and easier to change than you found it. Use these criteria to exercise judgment, not as a mandatory checklist or reply template.

## Solve the real problem

- Find the cause and fix it where its rules or state belong. Another conditional, fallback, flag, or wrapper placed over a broken invariant is a patch. It hides the problem and makes the next change harder.
- Find the layer that owns the cause before fixing anything. A symptom often shows up far from its source: in the interface when the server sends the wrong data, in the code when the schema or the stored data is wrong, in the implementation when the requirement itself is off. A fix made where the symptom appears is a patch even when it is tidy, so follow the problem across the client, the server, the data, configuration, and dependencies until you reach the place that should have prevented it.
- Fix the class of problem, not only the instance. Once you know the cause, look for the same mistake elsewhere, and prefer a change that makes it impossible to repeat, such as a type, a constraint, or a single owner, over one that corrects this occurrence.
- When the right fix is a change to the design or the data model, make it when it is within reach of the request. When it is larger than that, say so, describe it, and recommend it. Never ship a patch as if it were the fix.
- Understand the affected behavior, callers, data flow, and constraints before changing them. Use real callers and representative data to separate requirements from assumptions. Follow project conventions and reuse existing capabilities, while questioning patterns that cause the problem. Read what the change requires, not the whole repository by default.
- For a bug, first build a tight loop that goes red on the reported symptom: a test, script, or command you have run. Theorize only once it exists, weighing several falsifiable hypotheses rather than the first plausible one. Distinguish evidence from explanation and name unresolved uncertainty.

## Get the shape right

- Start from the data model. Represent each fact once, derive the rest, and model meaningful states explicitly so that invalid combinations cannot be expressed. Code that is awkward to write is often a sign that the model is wrong.
- Look for state machines, including the ones nobody named. A lifecycle, workflow, or mode spread across booleans, nullable fields, and scattered conditionals is an implicit state machine, and it usually allows combinations that should be impossible. Give it named states and put the allowed transitions in one place when that makes the behavior more correct and easier to read. Use the lightest form that does the job, which is often a union type and one transition function.
- Give each rule and each piece of state one owner that creates, changes, persists, and disposes of it. Organize code around shared knowledge and responsibility rather than execution order. Share code when its consumers share knowledge and should change together, not because their implementations look alike.
- Keep boundaries clear. An interface is everything a caller needs to use it correctly: ordering, invariants, side effects, errors, and cost, not only signatures. Keep shared mechanics inside the module that understands them, so callers don't repeat setup or coordinate internal steps. Validate untrusted data where it enters the system, so the code inside can rely on its types. Test a questionable abstraction by imagining it deleted: either complexity disappears, or it spreads to every caller.
- Judge simplicity by what a maintainer must know to make a correct change, how many places must change together, and how discoverable those dependencies are. A smaller diff or more helpers is not inherently simpler, and function length alone is not a reason to split.
- Make it fast by construction. Choose data shapes, access patterns, and boundaries that make the efficient path the natural one, so the design avoids repeated work, per-item round trips, and unbounded growth. Count the complexity and correctness cost of a cache or concurrency before adding one, and support performance claims with measurements.
- Build what is needed now so that it is easy to extend. That comes from few concepts, clear owners, and coherent operations, not from options, hooks, or generality for features nobody has asked for.
- Before adding a special case, see whether the representation or operation can handle it naturally. Preserve meaningful distinctions and observable failures: invalid input or failed work must never look successful. Consider cancellation, concurrency, partial success, and retries where they apply.
- When a choice of interface, ownership, or persistence is consequential, sketch two or three genuinely different designs before choosing, and recommend one. Record the decision using project conventions when it is costly to reverse and would surprise a reader without context.

## Leave it better

- Improve the code your change touches. Remove the duplication, dead paths, and awkward structure you find there, so the next change in this area is easier than this one was. Keep cleanup that preserves behavior distinguishable from behavior changes.
- Remove obsolete paths instead of keeping parallel implementations or compatibility shims.
- Report an improvement that is too large or too far from the task, with a recommendation, instead of doing it silently or dropping it.
- Document non-obvious contracts and rationale near their owner. Add what names, types, and code do not already say.

## Verify and finish

- Verify coherent units before building further on them. Check changed behavior, relevant failure modes, and contracts preserved by refactors. Exercise the actual feature or integration where correctness depends on it; a build alone does not establish runtime behavior.
- Reuse existing checks. Add tests for meaningful failures they miss, using stable behavior contracts and expectations independent of the implementation. For regressions, show that the check detects the original failure when feasible. Test counts and coverage percentages are not the goal.
- Before calling the work done, review it as you would review someone else's: whether it is the right solution or a patch, whether it is correct and does what was asked and nothing else, and what it left behind. Fix what you find.
- Continue through implementation, verification, and correction of failures caused by the change. Distinguish pre-existing failures from regressions and report the result, evidence, and remaining limitations.
- Make implementation decisions within the request, and ask when a material ambiguity changes the outcome. Preserve unrelated user work. Publishing, deploying, and destructive actions need their own request.
