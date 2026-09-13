# Engineering craft

A small set of skills for engineering judgment, clear writing, and change-risk assessment. No plugin, runtime hooks, or `AGENTS.md` changes are required.

## Skills

- [Craft](skills/craft/SKILL.md) contains the everyday engineering standard and routes consequential architectural decisions to [design guidance](skills/craft/references/design.md).
- [Unslop](skills/unslop/SKILL.md) guides substantive writing without forced personality, word blacklists, or a mandatory editing process.
- [Blast radius](skills/blast-radius/SKILL.md) investigates consequences beyond the diff and tests the assumptions that make a change safe.

The skills are independently selectable. Craft does not require loading the other two for every code change or short reply. None imposes a task itinerary, mandatory design document, Git workflow, or PR template.

## Invocation

After registration, request a skill explicitly with `/craft <task>`, `/unslop <writing request>`, or `/blast-radius <change to assess>`. Each description also allows an agent to select that skill automatically for relevant work. Automatic selection is model judgment, not guaranteed enforcement.

In OpenCode V2, `slash: true` exposes each skill in the interactive command catalog. Automatic invocation is enabled by default. For manual-only use, add this frontmatter to the relevant skill:

```yaml
metadata:
  opencode/autoinvoke: false
```

See the [OpenCode V2 skill documentation](https://opencode.ai/v2/docs/skills) for discovery, metadata, and precedence. Other harnesses have their own discovery and invocation rules.

## Install

Register your local checkout's `skills` directory in the `skills` array of your OpenCode configuration. Alternatively, copy the desired skill directories into a project's `.opencode/skills/` directory.

An explicit source can override installed skills with the same IDs. Choose one version deliberately before registration. This collection does not register itself or modify existing skills.

## Evaluate

Useful review cases:

- A local bug fix should investigate the cause without inventing an architectural redesign.
- A feature that changes state ownership should load the design reference and explain the consequential choice.
- Related duplication should prompt consolidation when it removes shared knowledge, not an unrelated repository cleanup.
- Verification should target a meaningful failure without adding tests that repeat existing guarantees.
- A writing edit should remove filler while preserving technical terms, qualifications, failure details, and the author's voice.
- A risk review should follow indirect consumers and distinguish confirmed problems, cleared concerns, and unresolved assumptions. It should not require a new script when existing checks establish the claim.
- Completion should not trigger an unsolicited commit, branch, PR, or deployment.

These are evaluation cases, not claims that agent behavior has been tested.

## Source material

Adapted from Lowside Labs' private `agent-stack` collection:

- Craft and the principle skills contributed root causes, domain modeling, simplicity, authoritative types, direct verification, and coherent units of work.
- Its unslop reference and technical-writing skill contributed concrete language, consistent terminology, precise instructions, and respect for meaning over stylistic rules.
- Its blast-radius skill contributed indirect dependency analysis, version-specific investigation, lifecycle reasoning, and evidence for safety assumptions.

Removed separate principle activation, mandatory playbooks, automatic Git operations, rigid writing layers, and the requirement that every risk assessment produce a script or depend on one safety fact.

The source identifies itself as a derivative of pstack. Its copyright and license notice are preserved in [LICENSE](LICENSE).
