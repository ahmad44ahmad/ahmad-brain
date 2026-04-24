---
type: decision
status: active
track: <% tp.system.prompt("track") %>
lang: <% tp.system.prompt("lang (ar/en)", "en") %>
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
tags: [decision]
---

# <% tp.file.title %>

## Question

What was being decided?

## Context

The situation that forced the decision. Constraints at the time.

## Options considered

1. **Option A** — pros / cons / cost
2. **Option B** — pros / cons / cost
3. **Option C** — pros / cons / cost

## Decision

What was chosen.

## Rationale

Why this one. What we were optimising for.

## Consequences (to be filled later)

- Expected:
- Actual (fill in retrospectively):

## Related

- Project: [[]]
- Approver: [[]]
