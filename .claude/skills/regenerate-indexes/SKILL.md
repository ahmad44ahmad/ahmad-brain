---
name: regenerate-indexes
description: Walk wiki/ and decisions/ and regenerate index/*.md files from YAML frontmatter. Run after batch migrations or when Ahmad adds many new notes. Safe to run anytime — overwrites index/ contents.
---

# Regenerate Indexes Skill

Rebuilds `index/` MOCs from current vault frontmatter. Use when:

- Notes have been added/removed/retyped.
- Frontmatter has changed (status, type, tags).
- After a batch migration like Phase B.

## Usage

```bash
python C:\dev\ahmad-brain\.claude\skills\regenerate-indexes\generate.py
```

Overwrites files in `index/`:
- `index/people.md` — all `type: person`
- `index/projects.md` — all `type: project`
- `index/concepts.md` — all `type: concept`
- `index/sources.md` — all `type: source`
- `index/synthesis.md` — all `type: synthesis`
- `index/decisions.md` — all ADRs
- `index/timeline.md` — chronological events + decisions
- `index/open-questions.md` — notes with `status: draft` or stub
- `index/README.md` — master pointer

## When NOT to run

Do not run during active migration — wait for a git commit so generated indexes match committed state.
