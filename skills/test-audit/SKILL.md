---
name: test-audit
description: "The value bar for tests. Use when writing, changing, or reviewing tests, or when sweeping a suite for low-value, duplicated, or implementation-coupled tests."
slash: true
---

# Test audit

A test earns its maintenance cost by protecting observable behavior, a credible regression, or a contract someone depends on. Optimize for confidence, not for test counts, coverage, or lines deleted. The same bar applies when writing a test and when deciding whether an existing one should stay.

## Before adding a test

Be able to answer four questions. If you can't, don't add the test yet.

1. What observable behavior, invariant, or contract does it protect?
2. What credible regression would make it fail?
3. Why doesn't existing coverage already catch that? Each contract has one primary test at the strongest boundary that can prove it, and another layer needs its own distinct risk. Extend an existing case or fixture rather than adding a near-duplicate.
4. Does it need a production seam, such as an export, flag, wrapper, or injection hook, that no production caller needs? If so, test at the real boundary instead.

A regression test has to fail on the code before the fix, for the intended reason, and pass after it. One that never failed says nothing about the fix.

## What a low-value test looks like

It would still pass if the behavior broke, or it breaks when the behavior did not change. The usual forms:

- It asserts nothing, or compares a value with itself or with output from the code under test.
- It restates the source: copied fixtures, lists, strings, flags, or call shapes.
- It repeats a contract already proven at a stronger boundary, or replays one scenario at every layer it crosses.
- Its mock or fixture supplies the behavior being asserted.
- It passes for an unrelated reason, or its name promises more than its input exercises.
- It exists to keep a test-only export, wrapper, or dead production path alive.

## Removing tests

Be slower to delete a test than to decline to add one. A test that looks like implementation detail may be the only independent guard on a public API, protocol, stored format, migration, security rule, or default. Before removing one, read the whole test and the production code it covers, and know what failure it can detect and what stronger proof remains. A test you meant to keep that fails on the baseline may have found a product bug, so reproduce it and fix the owner.

Work in coherent batches by owner rather than one sweeping change. Delete the test-only seams and dead production code that a removed test was keeping alive. Afterward, run the affected tests and the repository's own checks, and report what was removed and why, what was kept that looked removable, and what you ran.
