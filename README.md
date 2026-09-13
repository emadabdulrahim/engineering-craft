# Engineering craft

A small set of skills for engineering judgment, clear writing, and change-risk assessment. No plugin, runtime hooks, or `AGENTS.md` changes are required.

## Skills

- [Craft](skills/craft/SKILL.md) contains the everyday engineering standard and routes consequential architectural decisions to [design guidance](skills/craft/references/design.md).
- [Unslop](skills/unslop/SKILL.md) guides substantive writing without forced personality, word blacklists, or a mandatory editing process.
- [Blast radius](skills/blast-radius/SKILL.md) investigates consequences beyond the diff and tests the assumptions that make a change safe.
- [Grill me](skills/grill-me/SKILL.md) challenges a plan through focused questions and recommendations before implementation.
- [Prototype](skills/prototype/SKILL.md) builds a small, runnable experiment for a UI, interaction, or state-model question.
- [Handoff](skills/handoff/SKILL.md) captures the context a fresh session needs without duplicating existing artifacts.

The skills are independently selectable. Craft does not require loading the others for every code change or short reply. None imposes a Git workflow or PR template. Interviews, experiments, and handoffs stay within their requested scope rather than automatically continuing into implementation.

## Invocation

After registration, request a skill with its slash command:

| Command | OpenCode invocation |
| --- | --- |
| `/craft <task>` | Manual or automatic for substantive code changes |
| `/unslop <writing request>` | Manual or automatic for substantive writing |
| `/blast-radius <change>` | Manual or automatic for relevant risk assessment |
| `/grill-me <plan or question>` | Manual only |
| `/prototype <design question>` | Manual only |
| `/handoff <next session's focus>` | Manual only |

Automatic selection is model judgment, not guaranteed enforcement. In OpenCode V2, `slash: true` exposes each skill in the interactive command catalog. Grill me, prototype, and handoff opt out of automatic discovery with this frontmatter:

```yaml
metadata:
  opencode/autoinvoke: false
```

This setting hides a skill from the model's advertised list but leaves it available by explicit ID. It is an invocation preference, not an authorization boundary.

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
- Test expectations should have an independent basis rather than repeat the implementation's algorithm.
- A writing edit should remove filler while preserving technical terms, qualifications, failure details, and the author's voice.
- A risk review should follow indirect consumers and distinguish confirmed problems, cleared concerns, and unresolved assumptions. It should not require a new script when existing checks establish the claim.
- A grilling session should investigate discoverable facts, ask dependency-aware questions, and stop at confirmed understanding rather than start implementation.
- A prototype should answer an explicit question, expose relevant state or UI differences, and report the limits of mocked behavior without automatically promoting code to production.
- A handoff should preserve decisions and unfinished work, link to existing evidence, and save outside the repository unless another destination was requested.
- Completion should not trigger an unsolicited commit, branch, PR, or deployment.

These are evaluation cases, not claims that agent behavior has been tested.

## Source material

Adapted from Lowside Labs' private `agent-stack` collection:

- Craft and the principle skills contributed root causes, domain modeling, simplicity, authoritative types, direct verification, and coherent units of work.
- Its unslop reference and technical-writing skill contributed concrete language, consistent terminology, precise instructions, and respect for meaning over stylistic rules.
- Its blast-radius skill contributed indirect dependency analysis, version-specific investigation, lifecycle reasoning, and evidence for safety assumptions.

Removed separate principle activation, mandatory playbooks, automatic Git operations, rigid writing layers, and the requirement that every risk assessment produce a script or depend on one safety fact.

The source identifies itself as a derivative of pstack. Its copyright and license notice are preserved in [LICENSE](LICENSE).

Also adapted from [Matt Pocock's skills at `3cca18b`](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015):

- `grill-me` and `grilling` contributed dependency-aware interview rounds, recommendations, and the distinction between discoverable facts and user decisions. They are combined here without mandatory subagents or exhaustive questioning.
- `prototype` contributed question-led experiments, interactive state exploration, and meaningful UI alternatives. This version leaves the artifact format flexible and removes automatic Git operations and production promotion.
- `handoff` contributed focused session transfer, artifact pointers, temporary-file output, and redaction.
- `codebase-design`, `domain-modeling`, and `tdd/tests.md` contributed caller knowledge, the deletion test, concrete domain scenarios, selective decision records, and independent test expectations.

Matt Pocock's copyright notice and the shared MIT permission notice are included in [LICENSE](LICENSE).
