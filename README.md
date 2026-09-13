# Engineering craft

A small set of skills for engineering judgment, clear writing, and change-risk assessment. No plugin, runtime hooks, or `AGENTS.md` changes are required.

## Skills

- [Craft](skills/craft/SKILL.md) contains the everyday engineering standard and routes consequential architectural decisions to [design guidance](skills/craft/references/design.md).
- [Unslop](skills/unslop/SKILL.md) guides substantive writing without forced personality, word blacklists, or a mandatory editing process.
- [Blast radius](skills/blast-radius/SKILL.md) investigates consequences beyond the diff and tests the assumptions that make a change safe.
- [Grill me](skills/grill-me/SKILL.md) challenges a plan through focused questions and recommendations before implementation.
- [Prototype](skills/prototype/SKILL.md) builds a small, runnable experiment for a UI, interaction, or state-model question.
- [Handoff](skills/handoff/SKILL.md) captures the context a fresh session needs without duplicating existing artifacts.
- [Walkthrough](skills/walkthrough/SKILL.md) guides an experienced engineer through unfamiliar code in small, source-backed steps.

The skills are independently selectable. Craft does not require loading the others for every code change or short reply. None imposes a Git workflow or PR template. Interviews, experiments, and handoffs stay within their requested scope rather than automatically continuing into implementation.

## Invocation

In Claude Code and OpenCode 2, request a skill with its slash command. In Codex, select a skill in the client or mention it explicitly with `$skill-name` where supported.

| Skill | Invocation policy |
| --- | --- |
| `/craft <task>` | Manual or automatic for substantive code changes |
| `/unslop <writing request>` | Manual or automatic for substantive writing |
| `/blast-radius <change>` | Manual or automatic for relevant risk assessment |
| `/grill-me <plan or question>` | Manual only |
| `/prototype <design question>` | Manual only |
| `/handoff <next session's focus>` | Manual only |
| `/walkthrough <question or area>` | Manual only |

Automatic selection is model judgment, not guaranteed enforcement. Grill me, prototype, handoff, and walkthrough use each tool's manual-only setting. Claude Code and OpenCode read these fields in `SKILL.md`:

```yaml
disable-model-invocation: true
metadata:
  opencode/autoinvoke: false
```

Codex reads the policy in each manual skill's `agents/openai.yaml`:

```yaml
policy:
  allow_implicit_invocation: false
```

The instructions are shared, not copied into separate versions for each tool. Invocation preferences do not grant permission to perform actions. See the [Claude Code](https://code.claude.com/docs/en/skills), [Codex](https://developers.openai.com/codex/build-skills), and [OpenCode 2](https://opencode.ai/v2/docs/skills) documentation for discovery and invocation details.

## Install

On macOS or Linux, clone this repository wherever you want to keep it:

```bash
git clone https://github.com/emadabdulrahim/engineering-craft.git
cd engineering-craft
./install.sh
```

The installer creates per-skill symlinks to this checkout in `~/.claude/skills/` for Claude Code and `~/.agents/skills/` for Codex. OpenCode 2 discovers both locations automatically and resolves duplicate IDs by precedence. Both copies of each link point to the same instructions.

The script works from any current directory and requires Bash and standard Unix utilities. Correct existing links are left alone. Conflicting files, directories, or links cause installation to stop before creating any links. Resolve the reported conflicts yourself, then rerun. Agent configuration, permissions, and unrelated skills are untouched.

If OpenCode already has an explicit skill source with the same IDs, that source takes precedence. Avoid leaving an explicit source pointing to an older checkout. This installer does not edit existing configuration.

These links apply to local sessions on this computer, not remote or cloud environments. Start a fresh session if an agent does not detect an update.

### Update

From this checkout on `main`:

```bash
git pull --ff-only
./install.sh
```

Content changes are available through existing links immediately; rerunning registers newly added skills. The checkout must stay in place. Before moving or deleting it, uninstall its links, then run the installer from the new location if needed.

### Uninstall

```bash
./install.sh --uninstall
```

Only symlinks pointing to this checkout's skill folders are removed, including links to skills deleted since installation. Source files, agent configuration, unrelated entries, and destination directories are preserved. Repeated uninstall runs are safe.

If you also registered this checkout as an explicit OpenCode skill source, it remains active until you remove that entry from the configuration.

## Test the installer

```bash
bash -n install.sh
python3 -B -m unittest discover -s tests -v
```

Tests execute a copy of the real installer against copied skills and temporary home directories. They cover repeated installation, live source updates, new skills, conflicts, paths with spaces, and scoped removal without modifying your actual agent setup. They do not test agent interpretation of the instructions.

## Evaluate

Useful review cases:

- A local bug fix should investigate the cause without inventing an architectural redesign.
- A feature that changes state ownership should load the design reference and explain the consequential choice.
- Related duplication should prompt consolidation when it removes repeated knowledge, not an unrelated repository cleanup. Extraction should reduce what readers must understand rather than scatter tightly related logic.
- A shared interface should simplify current use without embedding product-specific cases or making every caller repeat its mechanics. Contract documentation should expose the information callers need without narrating implementation details.
- Special-case elimination should preserve meaningful failures, not hide invalid input or report failed work as successful.
- Verification should target a meaningful failure without adding tests that repeat existing guarantees.
- Test expectations should have an independent basis rather than repeat the implementation's algorithm.
- A writing edit should remove filler while preserving technical terms, qualifications, failure details, and the author's voice.
- A risk review should follow indirect consumers and distinguish confirmed problems, cleared concerns, and unresolved assumptions. It should not require a new script when existing checks establish the claim.
- A grilling session should investigate discoverable facts, ask dependency-aware questions, and stop at confirmed understanding rather than start implementation.
- A prototype should answer an explicit question, expose relevant state or UI differences, and report the limits of mocked behavior without automatically promoting code to production.
- A handoff should preserve decisions and unfinished work, link to existing evidence, and save outside the repository unless another destination was requested.
- A walkthrough should explain one coherent idea at a time, link to actual code, and support detours without losing the main thread or starting implementation.
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

Craft's design criteria also draw on John Ousterhout's *A Philosophy of Software Design*, using his [published second-edition extract](https://web.stanford.edu/~ouster/cgi-bin/aposd2ndEdExtract.pdf), [Stanford discussion notes](https://web.stanford.edu/~ouster/cs190-winter24/lectures/aposd), and [discussion with Robert Martin](https://github.com/johnousterhout/aposd-vs-clean-code). The guidance applies these ideas as decision criteria rather than prescribing a particular architecture or process.
