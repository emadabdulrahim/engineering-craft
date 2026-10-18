---
name: pr
description: "Write or revise a pull request description around the change's consequential decisions. Use whenever writing a PR body."
slash: true
---

# PR

Write for two readers. The person approving the change reads the top and should know what they're agreeing to without opening the diff. A reviewer opens the folded section for how the system's shape changed. The diff carries the rest.

## Shape

Fill the repository's PR template when one exists, mapping these parts onto it.

1. **Opening.** One or two sentences in plain words: what changes, for whom, and the problem it solves. Explain any project-specific name the first time it appears. Link the issue.
2. **Verdict.** A line or two on whether this is the right long-term design, a reasonable stopgap, or patchwork, and the strongest alternative with why it lost.
3. **Decisions.** The choices the approver is agreeing to: product behavior, UI, stored data, shared contracts, and any threshold or default picked. One bullet each, decision first, reason in a clause.
4. **Risk.** One-way or two-way door, and the blast radius in product terms. Judge reversibility by effects (written data, sent messages, published APIs), not by whether the commit reverts.
5. **Verification.** Before and after: a screenshot for visual changes, otherwise the check that failed and now passes, or the output that changed. Name what was not verified.
6. **How it works,** folded in `<details>`. Module boundaries, contracts, state ownership, data flow, and what changed in the system's shape. Pair it with the smallest view that makes it clear: a shaped diff of a file, component, or call tree; pseudocode for logic; Mermaid for flow across boundaries. Usually one view.

Scale to consequence, not diff size. A local fix may need only the opening and verification. Include only parts with something true to say.

## Write

- Full, plain sentences that connect. Bullets for lists of separate items, one idea per bullet.
- The codebase's names for modules, types, and concepts, explained on first use.
- Only evidence you observed. Ask for the reason behind a consequential choice the diff, issue, and session do not explain.
- No em dashes.

Writing the description does not authorize pushing or opening a PR.
