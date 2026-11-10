---
name: pr
description: "Write or revise a pull request description that is short, plain, and gives its reader confidence in the change. Use whenever writing a PR body."
slash: true
---

# PR

The reader wants to stay in the loop without reading the diff. After a minute with the description they should understand why the change exists, what it does, and why they can trust it. Length is a cost to that reader, so every sentence has to earn its place. The diff carries the rest.

## What it says

- **Problem.** Why this change exists, in plain words: what was wrong or missing, and for whom. Link the issue.
- **What changed.** What behaves differently now, in product terms. Add a sentence or two on the approach when it isn't obvious. Leave out file lists and step-by-step mechanics.
- **Verification.** What you ran or saw that shows it works: a before and after screenshot for a visual change, otherwise the check that failed and now passes. Say what you did not check.
- **Worth knowing.** Only when something would surprise the reader or needs their say: a risk, a choice with a real tradeoff, behavior they might not expect, or work left undone. Leave it out when there is nothing.

A small fix can be three sentences. A large change still gets a short description, because depth belongs in the code, its comments, and linked docs. When the repository has a PR template, fill it with this content.

## How it reads

Write full, plain sentences without em dashes. Use the codebase's own names, and explain a project-specific name the first time it appears. State only what you observed. When the reason behind a consequential choice isn't in the diff, the issue, or the session, ask for it.

Writing the description does not authorize pushing or opening a PR.
