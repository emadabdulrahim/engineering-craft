---
name: blast-radius
description: "Assess what a change could break beyond its diff. Use for risk reviews, shared-contract or lifecycle changes, or explicit /blast-radius, not every local edit."
slash: true
---

# Blast radius

Find the consequences outside the immediate change and establish the assumptions that make it safe. A list of callers or a convincing explanation is not enough. Investigate plausible failure mechanisms, not an exhaustive list of hypothetical risks.

## Follow the behavior beyond the diff

- Understand what changes for callers, including behavior the diff does not state explicitly. Identify the contracts and invariants consumers rely on.
- Follow dependencies that symbol searches miss: serialized data, API responses, storage, generated code, configuration, and consumers in other languages or processes. A search with no matches does not establish that there are no consumers.
- When safety depends on library behavior, inspect the version the project actually uses and relevant local patches. Do not substitute current upstream documentation for the installed implementation.
- Check relevant timing and ownership: initialization, asynchronous work, cancellation, concurrent access, teardown, and shared state. Look for behavior that is correct in isolation but fails when operations overlap or run in a different order.

## Test the safety assumptions

- Identify the assumptions that would cause meaningful breakage if false. There may be several independent assumptions. Prioritize them by plausible impact and available evidence, not invented probabilities.
- Choose evidence that tests the mechanism. Prefer existing tests and real execution paths. Add a focused test or script when it closes an important gap; a new harness is not mandatory.
- Verify that the check exercises the relevant code, version, and conditions. Mocks or a simplified reproduction may omit the dependency or timing behavior under investigation. Run the app when the claim depends on its integration or lifecycle.
- Distinguish source inspection, inference, and executed checks. State what each establishes and what it cannot establish. If access or reproduction is unavailable, keep the assumption unresolved rather than presenting it as safe.

## Report what matters

Lead with actionable findings. For each material concern, explain the failure mechanism, affected consumer, and consequence. Cite real code locations and the evidence you observed. Separate confirmed problems, concerns cleared by checks, and unresolved risks without forcing a fixed report template.

Include relevant commands and outcomes so the evidence can be inspected or repeated. Recommend a focused follow-up for consequential uncertainty. Do not claim the entire change is safe merely because one check passed. If no problems were found, state the scope checked and remaining limits.

An assessment request does not authorize fixing every issue, changing Git history, or publishing findings. Use safe local checks, preserve unrelated work, and exclude secrets and private data from shared evidence.
