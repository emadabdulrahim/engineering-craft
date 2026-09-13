---
name: prototype
description: "Build a small experiment to answer a design question. Use for requested UI alternatives or interactive exploration of logic and state, not routine feature implementation."
slash: true
disable-model-invocation: true
metadata:
  opencode/autoinvoke: false
---

# Prototype

A prototype answers a question before production implementation. Completion means a runnable experiment and a clear account of what it establishes, not a shipped feature.

## Choose the experiment

State the question and what observation would help answer it. Identify the uncertain decision from the prompt, conversation, and affected code. Ask only when ambiguity would produce the wrong experiment.

Choose the artifact for the question:

- **Logic and state:** make transitions and awkward scenarios inspectable. Help someone discover whether the model allows the behavior they expect.
- **UI and interaction:** compare meaningful differences in layout, information hierarchy, or interaction. Evaluate them in the surrounding product where practical.

If the question spans both, build the smallest experiment that exposes their relationship. Do not force a single HTML file, a framework, or multiple variants when another format answers the question better.

## Make it useful to evaluate

For logic and state, separate the model from the controls used to explore it. Show the relevant state after each action in domain language. Provide repeatable scenarios and a way to reset, including a normal case and a consequential edge case. Allow free exploration when unexpected sequences are part of the question.

For UI, use the project's components and styling conventions. Prefer evaluating changes inside a plausible host page with representative content and density, rather than an empty showcase. Make alternatives materially different where the question warrants alternatives, not cosmetic variations of the same idea. Provide an easy way to compare them without prescribing a specific switcher or route scheme.

Label synthetic data, mocked behavior, and shortcuts. Preserve existing user work and keep experiments clearly identifiable and isolated from normal product behavior. Use safe local fixtures or in-memory state for mutations; do not wire exploratory controls to production writes.

## Spend effort on the uncertainty

Make the experiment easy to run using existing project tools. A self-contained file is useful when it improves portability, but not when it hides the actual integration being evaluated.

Add only the polish, error handling, and checks needed for a safe, interpretable experiment. Tests are useful when they establish the property under investigation. Avoid speculative abstractions and production infrastructure unrelated to the question.

Run the experiment and exercise the relevant scenarios. Check that the artifact can demonstrate the distinction being investigated. Do not claim that mocked behavior or a visual demonstration proves production correctness.

## Hand over the result

Provide the file or local URL, how to run it, and what to try. Explain what was observed, what remains unresolved, and which shortcuts limit the evidence. Keep your recommendation distinct from the user's choice.

Stop at the experiment unless implementation was also requested. Carry validated decisions into production only with appropriate implementation and verification. Do not automatically commit, create branches, publish, delete the experiment, or promote prototype code into production.
