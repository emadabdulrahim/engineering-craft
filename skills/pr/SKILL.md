---
name: pr
description: "Write or revise a pull request description around the change's consequential decisions. Use whenever writing a PR body."
slash: true
---

# PR

Write what a reviewer reads before opening the diff: how the system's shape changed and why. The diff carries the details.

## Shape

Fill the repository's PR template when one exists, mapping these parts onto it.

1. **Opening.** One or two sentences: what changes and the problem it solves. Link the issue.
2. **Decisions.** The choices a maintainer must know: module boundaries, contracts, state ownership, data flow, persistence, and alternatives worth rejecting. One bullet each, decision first, reason in a clause. Pair a decision with the smallest view that makes it clear: a shaped diff of a file, component, or call tree; pseudocode for logic; Mermaid for flow across boundaries. Usually one view.
3. **Verification.** Before and after: a screenshot for visual changes, otherwise the check that failed and now passes, or the output that changed. Name what was not verified.
4. **Risk.** One-way or two-way door, and the blast radius. Judge reversibility by effects (written data, sent messages, published APIs), not by whether the commit reverts.

Scale to consequence, not diff size. A local fix may need only the opening and verification. Include only parts with something true to say.

## Write

- Bullets and views over paragraphs, one idea per bullet.
- The codebase's names for modules, types, and concepts.
- Only evidence you observed. Ask for the reason behind a consequential choice the diff, issue, and session do not explain.
- No em dashes.

Writing the description does not authorize pushing or opening a PR.
