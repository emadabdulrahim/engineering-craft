---
name: handoff
description: "Capture the context a fresh session needs to continue the work. Invoke explicitly, optionally naming the next session's focus."
slash: true
disable-model-invocation: true
metadata:
  opencode/autoinvoke: false
---

# Handoff

Write a concise handoff document that lets another session continue without reconstructing the conversation. Tailor it to the user's stated next task. If no focus is given, capture the unfinished work and agreed next step.

## Preserve what is not already recorded

Include the information the next session needs:

- The goal, scope, and definition of done.
- Decisions, constraints, and reasons that are not recoverable from existing artifacts.
- Current state, including relevant repository paths, branch, uncommitted work, and running processes when applicable.
- What has been verified, the evidence location, and remaining failures or uncertainty.
- Open questions, blockers, and the next useful action.

Link to existing specs, issues, commits, diffs, and documentation instead of copying them. Include enough context to explain why each pointer matters. Distinguish established facts, user decisions, and untested hypotheses.

Verify cheap current facts such as paths and Git status before recording them. Label older observations when they may be stale. Do not present a previous successful check as evidence about subsequent changes.

Suggest specific skills only when they are available and relevant to the next task. Do not turn the handoff into a generic workflow or a transcript dump.

## Save and report

Use the destination requested by the user. Otherwise, create a uniquely named Markdown file in the runtime's approved temporary directory, outside the repository. Include absolute local paths when the handoff is for another session on the same machine.

Exclude credentials, secrets, and unnecessary personal data. Point to protected artifacts rather than copying sensitive payloads into the handoff. Read the saved file to check that it is accurate and usable, then return its path and a brief statement of what it covers.

Do not commit or publish the handoff, start another agent, or continue implementing the task as part of this request.
