---
name: retro
description: "Review a coding session for environment changes that would improve future runs. Invoke explicitly, optionally naming the session."
slash: true
disable-model-invocation: true
metadata:
  opencode/autoinvoke: false
---

# Retro

Look back at a coding session and recommend changes to the agent's environment, not the code: what would have made the work faster, cheaper, or correct the first time. Use the current session unless the user names another.

## Find the friction

Read the primary sources: the transcript or session logs, the resulting diff, and the steering files and checks the agent had. Find where the agent searched long, guessed, repeated work, made a mistake, or was corrected, and trace each moment to the missing piece of environment:

- **Navigation.** Information that took long to find, or hidden dependencies between files. A pointer in the right steering file or doc may fix it.
- **Automated checks.** A mistake a linter, type check, test, or CI job could have caught. Read the repository's existing check commands and CI first; an existing check that is unwired or broken is the finding. A repository with no check running on commit or in CI is a finding by itself.
- **Standards.** A mistake review should have caught. A mechanical rule (a banned API, an import shape, a file location) belongs in a deterministic check. Written standards are for judgment calls, kept where review reads them: review sees only the diff, so it can carry standards that implementation cannot hold in mind.
- **Steering files.** Always-loaded instructions (`AGENTS.md`, `CLAUDE.md`, skill descriptions) cost context every turn. Flag instructions the agent already follows by default, stale ones, and ones that belong in a check, a doc, or a skill.
- **Tool economy.** Expensive or repeated tool calls, and verbose tooling a better command, script, or flag would streamline.
- **Information access.** Information the agent needed but could not reach, such as dev server logs, runtime state, or read-only access to a service.

## Report

Present candidates in order of impact. For each, give what happened with a pointer to it in the session, the proposed change and where it lives, and why it prevents a repeat. Prefer the cheapest durable fix: a check over a rule, a pointer over a copied doc. Say so when the session shows no meaningful friction.

Steering files, checks, and skills stay unchanged until the user picks which changes to apply.
