"""
Vault reconciler. Read-only.

Deterministic checks for semantic drift:
  1. Date integrity — parseable + ordered (created ≤ updated; valid_from ≤ updated).
  2. ADR supersede-chain reciprocity — X supersedes Y ⇔ Y superseded-by X.
  3. ID / alias collisions — no alias shadows a different note's id or alias.
  4. Stale drafts — status: draft + older than STALE_DRAFT_DAYS.
  5. Duplicate tags within a single note.
  6. Stale open threads — a non-empty `open:` field on a note untouched > STALE_OPEN_DAYS
     (the live action is likely resolved or needs a refresh — keeps the open-items surface honest).

Exit 0 clean, 1 if any findings.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

VAULT = Path(r"C:\dev\ahmad-brain")
ROOTS = [VAULT / "wiki", VAULT / "decisions", VAULT / "log"]
ROOT_FILES = [VAULT / "_CLAUDE.md"]

STALE_DRAFT_DAYS = 14
STALE_OPEN_DAYS = 30
TODAY = date.today()

LINK_FIELDS = ("related", "amends", "supersedes", "superseded-by")
DATE_FIELDS = ("created", "updated", "valid_from", "learned_at")

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
SLUG_RE = re.compile(r"\[\[([^\[\]|#]+?)(?:#[^\[\]|]*)?(?:\|[^\[\]]*)?\]\]")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def split_frontmatter(text: str) -> str:
    m = FRONTMATTER_RE.match(text)
    return m.group(1) if m else ""


def parse_scalar(raw_fm: str, key: str) -> str | None:
    for line in raw_fm.split("\n"):
        m = re.match(rf"^{re.escape(key)}\s*:\s*(.*?)\s*$", line)
        if m:
            v = m.group(1).strip().strip('"').strip("'")
            return v or None
    return None


def parse_list_field(raw_fm: str, key: str) -> list[str]:
    """Return raw list items (strings, wikilink-stripped)."""
    lines = raw_fm.split("\n")
    out: list[str] = []
    in_block = False
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(key)}\s*:", line):
            in_block = True
            # inline list on head line: `tags: [a, b]`
            tail = line.split(":", 1)[1].strip()
            if tail.startswith("[") and tail.endswith("]"):
                inner = tail[1:-1].strip()
                if inner:
                    for item in inner.split(","):
                        v = item.strip().strip('"').strip("'")
                        if v:
                            out.append(v)
                return out
            continue
        if in_block:
            if re.match(r"^[a-zA-Z_][\w-]*\s*:", line):
                break
            m = re.match(r"^\s+-\s+(.+?)\s*$", line)
            if m:
                v = m.group(1).strip().strip('"').strip("'")
                if v:
                    out.append(v)
    return out


def extract_slugs_from_items(items: list[str]) -> list[str]:
    out = []
    for item in items:
        m = SLUG_RE.search(item)
        if m:
            out.append(m.group(1).strip())
    return out


def parse_date(s: str | None) -> date | None:
    if not s:
        return None
    if not DATE_RE.match(s):
        return None
    try:
        y, m, d = s.split("-")
        return date(int(y), int(m), int(d))
    except ValueError:
        return None


def has_open_field(raw_fm: str) -> bool:
    """True if the note carries a non-empty `open:` action field (inline or folded `>-` block)."""
    lines = raw_fm.split("\n")
    for i, line in enumerate(lines):
        m = re.match(r"^open\s*:\s*(.*?)\s*$", line)
        if not m:
            continue
        inline = m.group(1).strip()
        if inline and inline not in (">-", ">", "|", "|-"):
            return True  # inline content, e.g. `open: NOW submit X`
        for nxt in lines[i + 1:]:  # folded/literal block — look for an indented content line
            if re.match(r"^[a-zA-Z_][\w-]*\s*:", nxt):
                break
            if nxt.strip():
                return True
        return False
    return False


def main() -> int:
    notes: list[tuple[Path, str]] = []
    for root in ROOTS:
        if not root.exists():
            continue
        for p in sorted(root.rglob("*.md")):
            text = p.read_text(encoding="utf-8", errors="replace")
            fm = split_frontmatter(text)
            if fm.strip():
                notes.append((p, fm))
    for p in ROOT_FILES:
        if p.exists():
            text = p.read_text(encoding="utf-8", errors="replace")
            fm = split_frontmatter(text)
            if fm.strip():
                notes.append((p, fm))

    # Build id index
    id_to_path: dict[str, Path] = {}
    for p, fm in notes:
        nid = parse_scalar(fm, "id")
        if nid:
            id_to_path.setdefault(nid, p)

    # Findings buckets
    date_issues: list[tuple[Path, str]] = []
    supersede_issues: list[tuple[Path, str]] = []
    alias_collisions: list[tuple[Path, str]] = []
    stale_drafts: list[tuple[Path, int]] = []
    stale_open: list[tuple[Path, int]] = []
    duplicate_tags: list[tuple[Path, list[str]]] = []

    # Alias/id map — who owns each "name token"?
    # (id, aliases) all map back to path
    name_owners: dict[str, list[tuple[Path, str]]] = defaultdict(list)  # name → [(path, kind)]
    for p, fm in notes:
        nid = parse_scalar(fm, "id")
        if nid:
            name_owners[nid].append((p, "id"))
        aliases = parse_list_field(fm, "aliases")
        for a in aliases:
            name_owners[a].append((p, "alias"))

    for name, owners in name_owners.items():
        if len(owners) > 1:
            # Genuine collision: multiple different paths share this name
            paths = {p for p, _ in owners}
            if len(paths) > 1:
                summary = ", ".join(f"{p.relative_to(VAULT)} ({kind})" for p, kind in owners)
                alias_collisions.append((owners[0][0], f"{name!r} shared by: {summary}"))

    for p, fm in notes:
        rel = p.relative_to(VAULT)
        nid = parse_scalar(fm, "id") or "<no-id>"

        # 1. Date integrity
        parsed_dates: dict[str, date | None] = {}
        for field in DATE_FIELDS:
            raw = parse_scalar(fm, field)
            if raw is None:
                parsed_dates[field] = None
                continue
            d = parse_date(raw)
            if d is None:
                date_issues.append((p, f"{field}: unparseable value {raw!r}"))
            parsed_dates[field] = d

        created = parsed_dates.get("created")
        updated = parsed_dates.get("updated")
        valid_from = parsed_dates.get("valid_from")

        if created and updated and created > updated:
            date_issues.append((p, f"created ({created}) > updated ({updated})"))
        if valid_from and updated and valid_from > updated:
            date_issues.append((p, f"valid_from ({valid_from}) > updated ({updated})"))

        # 2. ADR supersede-chain reciprocity
        supersedes_items = parse_list_field(fm, "supersedes")
        superseded_by_items = parse_list_field(fm, "superseded-by")
        # Single-value fallback
        if not supersedes_items:
            single = parse_scalar(fm, "supersedes")
            if single and "[[" in single:
                supersedes_items = [single]
        if not superseded_by_items:
            single = parse_scalar(fm, "superseded-by")
            if single and "[[" in single:
                superseded_by_items = [single]

        for sup_slug in extract_slugs_from_items(supersedes_items):
            target_path = id_to_path.get(sup_slug)
            if target_path is None:
                supersede_issues.append((p, f"supersedes unknown id [[{sup_slug}]]"))
                continue
            target_fm = split_frontmatter(target_path.read_text(encoding="utf-8", errors="replace"))
            reverse_items = parse_list_field(target_fm, "superseded-by")
            if not reverse_items:
                single = parse_scalar(target_fm, "superseded-by")
                if single and "[[" in single:
                    reverse_items = [single]
            reverse_slugs = extract_slugs_from_items(reverse_items)
            if nid not in reverse_slugs:
                supersede_issues.append(
                    (p, f"[[{sup_slug}]] does not list this note ({nid}) in superseded-by")
                )

        # 4. Stale drafts
        status = parse_scalar(fm, "status")
        if status == "draft" and updated:
            age = (TODAY - updated).days
            if age > STALE_DRAFT_DAYS:
                stale_drafts.append((p, age))

        # 4b. Stale open threads — a live `open:` action on a note untouched > STALE_OPEN_DAYS
        if has_open_field(fm) and updated:
            age = (TODAY - updated).days
            if age > STALE_OPEN_DAYS:
                stale_open.append((p, age))

        # 5. Duplicate tags within a note
        tags = parse_list_field(fm, "tags")
        seen_tags: dict[str, int] = defaultdict(int)
        for t in tags:
            seen_tags[t] += 1
        dupes = [t for t, n in seen_tags.items() if n > 1]
        if dupes:
            duplicate_tags.append((p, dupes))

    # Report
    print("=" * 72)
    print(f"Vault reconcile — {len(notes)} notes scanned under {VAULT}")
    print("=" * 72)

    total = 0

    def section(title: str, count: int) -> None:
        nonlocal total
        total += count
        print(f"\n[{title}] {count}")

    section("date integrity", len(date_issues))
    for p, msg in date_issues:
        print(f"  - {p.relative_to(VAULT)} :: {msg}")

    section("supersede-chain reciprocity", len(supersede_issues))
    for p, msg in supersede_issues:
        print(f"  - {p.relative_to(VAULT)} :: {msg}")

    section("id/alias collisions", len(alias_collisions))
    seen_messages = set()
    for p, msg in alias_collisions:
        if msg in seen_messages:
            continue
        seen_messages.add(msg)
        print(f"  - {msg}")

    section("stale drafts", len(stale_drafts))
    for p, age in stale_drafts:
        print(f"  - {p.relative_to(VAULT)} :: {age} days since updated")

    section("stale open threads", len(stale_open))
    for p, age in stale_open:
        print(f"  - {p.relative_to(VAULT)} :: open: field, {age} days since updated — resolve or refresh")

    section("duplicate tags", len(duplicate_tags))
    for p, dupes in duplicate_tags:
        print(f"  - {p.relative_to(VAULT)} :: duplicates: {dupes}")

    print("\n" + "=" * 72)
    collision_unique = len(seen_messages)
    real_total = (
        len(date_issues)
        + len(supersede_issues)
        + collision_unique
        + len(stale_drafts)
        + len(stale_open)
        + len(duplicate_tags)
    )
    print(f"TOTAL FINDINGS: {real_total}")
    print("=" * 72)

    return 0 if real_total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
