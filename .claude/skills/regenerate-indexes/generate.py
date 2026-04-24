"""
Regenerate index/*.md from wiki/ + decisions/ frontmatter.

Safe to overwrite. Re-run anytime.
"""
import re
import sys
from pathlib import Path
from datetime import date

VAULT = Path(r"C:\dev\ahmad-brain")
INDEX = VAULT / "index"
WIKI = VAULT / "wiki"
DECISIONS = VAULT / "decisions"
LOG = VAULT / "log"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def parse_frontmatter(text):
    """Parse simple YAML-ish frontmatter into dict. Good enough for our schema."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    raw = m.group(1)
    result = {}
    current_key = None
    for line in raw.split("\n"):
        if not line.strip():
            continue
        # Simple key: value or key: >- or list item
        m2 = re.match(r"^([a-zA-Z_][\w-]*)\s*:\s*(.*)$", line)
        if m2:
            current_key = m2.group(1)
            value = m2.group(2).strip()
            if value.startswith(">-") or value == ">":
                result[current_key] = ""  # multiline follows
            elif value.startswith("[") and value.endswith("]"):
                # simple inline list
                inner = value[1:-1].strip()
                if inner:
                    items = [x.strip().strip('"').strip("'") for x in inner.split(",")]
                    result[current_key] = items
                else:
                    result[current_key] = []
            else:
                result[current_key] = value.strip('"').strip("'")
        elif line.startswith("  ") and current_key:
            # multiline continuation
            if isinstance(result.get(current_key), str):
                result[current_key] = (result[current_key] + " " + line.strip()).strip()
    return result


def load_notes(root):
    """Walk a directory and return list of (path, frontmatter) tuples."""
    notes = []
    for p in sorted(root.rglob("*.md")):
        try:
            content = p.read_text(encoding="utf-8")
            fm = parse_frontmatter(content)
            if fm:
                notes.append((p, fm))
        except Exception as e:
            print(f"WARN: couldn't parse {p}: {e}", file=sys.stderr)
    return notes


def truncate(s, n=100):
    if not s:
        return ""
    s = s.strip()
    return s[: n - 1] + "…" if len(s) > n else s


def rel(path):
    return str(path.relative_to(VAULT)).replace("\\", "/")


def write_index_table(target_name, title, notes, filter_fn, columns):
    """columns = list of (header, lambda fm: str) pairs."""
    filtered = [(p, fm) for p, fm in notes if filter_fn(fm)]
    filtered.sort(key=lambda x: x[1].get("id", ""))
    lines = [f"""---
id: index-{target_name}
title: {title}
type: moc
status: active
tags: [index, auto-generated]
created: 2026-04-24
updated: {date.today().isoformat()}
summary: >-
  Auto-generated index. Regenerate via `.claude/skills/regenerate-indexes/generate.py`.
  Count: {len(filtered)} entries.
---

# {title}

Auto-generated {date.today().isoformat()}. {len(filtered)} entries. Regenerate with `/regenerate-indexes` skill.

"""]
    if not filtered:
        lines.append("_No entries._\n")
    else:
        header = "| " + " | ".join(h for h, _ in columns) + " |"
        sep = "|" + "|".join(["---"] * len(columns)) + "|"
        lines.append(header)
        lines.append(sep)
        for p, fm in filtered:
            row = "| " + " | ".join(str(getter(fm, p)) for _, getter in columns) + " |"
            lines.append(row)
        lines.append("")
    (INDEX / f"{target_name}.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote index/{target_name}.md ({len(filtered)} entries)")


def main():
    wiki_notes = load_notes(WIKI)
    decision_notes = load_notes(DECISIONS)
    log_notes = load_notes(LOG)
    all_notes = wiki_notes + decision_notes + log_notes

    # index/people.md
    write_index_table(
        "people", "People Index",
        wiki_notes,
        lambda fm: fm.get("type") == "person",
        [
            ("id", lambda fm, p: f"[[{fm.get('id','')}]]"),
            ("title", lambda fm, p: truncate(fm.get("title", ""), 60)),
            ("status", lambda fm, p: fm.get("status", "")),
            ("summary", lambda fm, p: truncate(fm.get("summary", ""), 120)),
        ],
    )

    # index/projects.md
    write_index_table(
        "projects", "Projects Index",
        wiki_notes,
        lambda fm: fm.get("type") == "project",
        [
            ("id", lambda fm, p: f"[[{fm.get('id','')}]]"),
            ("title", lambda fm, p: truncate(fm.get("title", ""), 60)),
            ("status", lambda fm, p: fm.get("status", "")),
            ("summary", lambda fm, p: truncate(fm.get("summary", ""), 120)),
        ],
    )

    # index/concepts.md
    write_index_table(
        "concepts", "Concepts Index",
        wiki_notes,
        lambda fm: fm.get("type") == "concept",
        [
            ("id", lambda fm, p: f"[[{fm.get('id','')}]]"),
            ("title", lambda fm, p: truncate(fm.get("title", ""), 60)),
            ("summary", lambda fm, p: truncate(fm.get("summary", ""), 140)),
        ],
    )

    # index/sources.md
    write_index_table(
        "sources", "Sources Index",
        wiki_notes,
        lambda fm: fm.get("type") == "source",
        [
            ("id", lambda fm, p: f"[[{fm.get('id','')}]]"),
            ("title", lambda fm, p: truncate(fm.get("title", ""), 60)),
            ("source", lambda fm, p: fm.get("source", "")),
            ("summary", lambda fm, p: truncate(fm.get("summary", ""), 120)),
        ],
    )

    # index/synthesis.md
    write_index_table(
        "synthesis", "Synthesis Index",
        wiki_notes,
        lambda fm: fm.get("type") == "synthesis",
        [
            ("id", lambda fm, p: f"[[{fm.get('id','')}]]"),
            ("title", lambda fm, p: truncate(fm.get("title", ""), 60)),
            ("summary", lambda fm, p: truncate(fm.get("summary", ""), 140)),
        ],
    )

    # index/decisions.md
    write_index_table(
        "decisions", "Decisions Index (ADRs)",
        decision_notes,
        lambda fm: fm.get("type") == "decision",
        [
            ("id", lambda fm, p: f"[[{fm.get('id','')}]]"),
            ("title", lambda fm, p: truncate(fm.get("title", ""), 60)),
            ("status", lambda fm, p: fm.get("status", "")),
            ("summary", lambda fm, p: truncate(fm.get("summary", ""), 120)),
        ],
    )

    # index/open-questions.md (status: draft OR type: log with open TODOs)
    drafts = [(p, fm) for p, fm in all_notes if fm.get("status") == "draft"]
    drafts.sort(key=lambda x: x[1].get("id", ""))
    lines = [f"""---
id: index-open-questions
title: Open Questions & Draft Stubs
type: moc
status: active
tags: [index, auto-generated, draft-stubs, open-questions]
created: 2026-04-24
updated: {date.today().isoformat()}
summary: >-
  Notes currently in status draft — stubs awaiting full migration or Ahmad's
  next touch on the topic. {len(drafts)} entries.
---

# Open Questions & Draft Stubs

{len(drafts)} notes in `status: draft`. Regenerate with `/regenerate-indexes`.

"""]
    if drafts:
        lines.append("| id | title | summary |")
        lines.append("|---|---|---|")
        for p, fm in drafts:
            lines.append(f"| [[{fm.get('id','')}]] | {truncate(fm.get('title',''), 60)} | {truncate(fm.get('summary',''), 140)} |")
    (INDEX / "open-questions.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote index/open-questions.md ({len(drafts)} entries)")

    # index/timeline.md (chronological: decisions + logs)
    timeline = []
    for p, fm in decision_notes + log_notes:
        d = fm.get("created") or fm.get("updated")
        if d:
            timeline.append((d, fm.get("type", ""), fm.get("id", ""), fm.get("title", "")))
    timeline.sort(reverse=True)
    lines = [f"""---
id: index-timeline
title: Timeline — Decisions + Session Logs
type: moc
status: active
tags: [index, auto-generated, timeline]
created: 2026-04-24
updated: {date.today().isoformat()}
summary: >-
  Reverse-chronological feed of ADRs and session logs. {len(timeline)} entries.
---

# Timeline

{len(timeline)} dated entries. Most recent first.

| date | type | id | title |
|---|---|---|---|
"""]
    for d, t, i, title in timeline:
        lines.append(f"| {d} | {t} | [[{i}]] | {truncate(title, 80)} |")
    (INDEX / "timeline.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote index/timeline.md ({len(timeline)} entries)")

    # index/README.md (master pointer)
    readme = f"""---
id: index-readme
title: Index — Master Pointer
type: moc
status: active
tags: [index, master-pointer]
created: 2026-04-24
updated: {date.today().isoformat()}
summary: >-
  Master pointer to the 8 auto-generated vault indexes.
---

# Master Index

All files here auto-generated by `/regenerate-indexes` skill. Do not edit by hand — edits will be overwritten.

| Index | Covers | Count |
|---|---|---|
| [[index-people]] | All `type: person` — who's in Ahmad's orbit | {sum(1 for _,fm in wiki_notes if fm.get('type')=='person')} |
| [[index-projects]] | All `type: project` — active work | {sum(1 for _,fm in wiki_notes if fm.get('type')=='project')} |
| [[index-concepts]] | All `type: concept` — frameworks, doctrines | {sum(1 for _,fm in wiki_notes if fm.get('type')=='concept')} |
| [[index-sources]] | All `type: source` — distilled external material | {sum(1 for _,fm in wiki_notes if fm.get('type')=='source')} |
| [[index-synthesis]] | All `type: synthesis` — Ahmad's original cross-cutting analysis | {sum(1 for _,fm in wiki_notes if fm.get('type')=='synthesis')} |
| [[index-decisions]] | All ADRs (`decisions/`) | {sum(1 for _,fm in decision_notes if fm.get('type')=='decision')} |
| [[index-timeline]] | Decisions + logs reverse-chronological | — |
| [[index-open-questions]] | Notes in `status: draft` awaiting expansion | {sum(1 for _,fm in wiki_notes+decision_notes+log_notes if fm.get('status')=='draft')} |

## Quick totals

- Total wiki notes: **{len(wiki_notes)}**
- Total decisions (ADRs): **{len(decision_notes)}**
- Total logs: **{len(log_notes)}**
- Grand total: **{len(wiki_notes)+len(decision_notes)+len(log_notes)}** structured notes.

Generated {date.today().isoformat()}.
"""
    (INDEX / "README.md").write_text(readme, encoding="utf-8")
    print(f"wrote index/README.md")


if __name__ == "__main__":
    main()
