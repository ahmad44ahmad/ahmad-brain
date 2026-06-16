---
id: prompt-forge
title: Prompt-Forge — Engineered-Intake Template
type: synthesis
status: active
aliases: [prompt-forge-format-2]
tags: [prompt-engineering, claude-workflow, intake-template, method]
created: 2026-04-17
updated: 2026-06-16
source: ahmad-workflow
related:
  - "[[vault-operating-manual]]"
  - "[[ai-model-routing-and-governance]]"
  - "[[architecture-first-knowledge-retrieval]]"
summary: >-
  Ahmad's canonical intake-prompt template for substantive Claude tasks.
  Format-2 — engineered context packet (goal, constraints, deliverable,
  success criteria, prior art) — replaces raw brainstorm dumps that
  historically caused drift. Apply before non-trivial work.
---

# PROMPT-FORGE — engineered intake template (Format 2)

> **Not stored in memory.** This is a workflow reference for Claude.
> **Trigger:** any brainstorm, context dump, open-ended mission, or `/mission` command on a non-trivial task.
> **Skip when:** trivial / Ahmad says "quick" / direct factual question.

---

## The inverted flow

```
OLD:  Ahmad (raw brainstorm + goal) → Claude (executes raw input) → drift → average output
NEW:  Ahmad (raw brainstorm + goal) → Claude (engineered prompt) → Ahmad (stamp) → Claude (executes)
```

Ahmad is not a prompt engineer. He shouldn't be. His job is the vision. Claude's job is to translate vision into an engineered intent document that won't drift during execution.

---

## Template — Claude fills every section, then hands to Ahmad to stamp

### 1. Goal — ONE sentence
What is being asked. Literal. No expansion.

### 2. Unstated assumptions I'm making
Things Ahmad didn't say but I'm inferring. Flag any load-bearing + uncertain one for stamp.

### 3. Constraints
- **Hard (non-negotiable):** ...
- **Soft (preferences):** ...
- **Scope boundary (what's NOT in scope):** ...

### 4. Approaches considered (2–4, REAL alternatives)
Not decorative options. Each must be genuinely different in architecture/cost/risk.

| # | Approach | Cost | Risk | Strongest win |
|---|---|---|---|---|
| A | | | | |
| B | | | | |
| C | | | | |

### 5. Selected approach — and why the others lose
One line per rejected option. No generic "less flexible" — be specific.

### 6. Execution plan
Concrete steps. Tool calls named. Not "I will consider X" — "I will run Y with arg Z".

1. ...
2. ...
3. ...

### 7. Failure points anticipated
What breaks this? What do I do when it breaks?

### 8. Adversarial summary
**Strongest argument AGAINST this plan**, stated honestly. If I cannot find one in 30 seconds, I haven't looked — flag it.

### 9. Ready-to-execute prompt (the distilled output)
The single paragraph I will operate from. Terse. No preamble.

### 10. Handoff line
> "Ahmad: review sections 2, 3, 5, 8. Stamp / modify / challenge. I execute on your signal."

---

## Failure modes for the forge itself

The forge can become drift in disguise if filled with filler. Watch for:

- **Vague assumptions** (section 2) → if I can't name a specific assumption, I didn't dig.
- **Decorative alternatives** (section 4) → if B and C are just "slightly different A", I lied about having alternatives.
- **Soft adversarial** (section 8) → if the counter-argument is weak/hypothetical, I went easy.

If any of these fire → redo with more rigor, NOT more words.

---

## When to SKIP the forge (trivial-task escape hatch)

- <5 minutes, no file risk, no ambiguity.
- Direct factual question ("what's the command for X?").
- Single-line fix request.
- Ahmad says "quick" / "بسرعة" / "just do".

**When in doubt → forge.** Over-forging costs 2 minutes. Under-forging costs a project.
