"""
Vault linter. Read-only.

Checks:
  1. Required frontmatter keys present on every note.
  2. `type:` is from the allowed set.
  3. Every [[slug]] in frontmatter link-fields and body resolves to a known id.
  4. Link-field shape: `related` / `amends` / `supersedes` / `superseded-by`
     are either absent, a single string, or a multiline list of quoted strings.
  5. No duplicate `id` across the vault.

Exit 0 clean, 1 if any issues.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

VAULT = Path(r"C:\dev\ahmad-brain")
ROOTS = [VAULT / "wiki", VAULT / "decisions", VAULT / "log"]
# Top-level vault notes that must also be indexed (e.g. _CLAUDE.md).
ROOT_FILES = [VAULT / "_CLAUDE.md"]

CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")

REQUIRED_KEYS = {"id", "title", "type", "status", "tags", "created", "updated", "summary"}
ALLOWED_TYPES = {
    "source", "wiki", "decision", "log",
    "person", "project", "concept", "entity",
    "synthesis", "moc",
}
LINK_FIELDS = ("related", "amends", "supersedes", "superseded-by")

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\[\]|#]+?)(?:#[^\[\]|]*)?(?:\|[^\[\]]*)?\]\]")


def split_frontmatter(text: str) -> tuple[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return "", text
    return m.group(1), text[m.end():]


def parse_top_level_keys(raw: str) -> dict[str, str]:
    """Return dict of top-level key → raw block value (everything until the next top-level key)."""
    lines = raw.split("\n")
    keys: dict[str, list[str]] = {}
    current = None
    for line in lines:
        if not line.strip():
            if current is not None:
                keys[current].append(line)
            continue
        m = re.match(r"^([a-zA-Z_][\w-]*)\s*:\s*(.*)$", line)
        if m and not line.startswith(" ") and not line.startswith("\t"):
            current = m.group(1)
            keys.setdefault(current, []).append(m.group(2))
        elif current is not None:
            keys[current].append(line)
    return {k: "\n".join(v).strip() for k, v in keys.items()}


def parse_id(raw_fm: str) -> str | None:
    for line in raw_fm.split("\n"):
        m = re.match(r"^id\s*:\s*(.+?)\s*$", line)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    return None


def parse_type(raw_fm: str) -> str | None:
    for line in raw_fm.split("\n"):
        m = re.match(r"^type\s*:\s*(.+?)\s*$", line)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    return None


def link_field_block(raw_fm: str, field: str) -> list[str] | None:
    """Return the lines of a link field block (key + its indented children),
    or None if the field is absent."""
    lines = raw_fm.split("\n")
    out: list[str] = []
    in_block = False
    for line in lines:
        if line.strip().startswith("#"):
            continue
        if re.match(rf"^{re.escape(field)}\s*:", line):
            out = [line]
            in_block = True
            continue
        if in_block:
            # Another top-level key terminates the block
            if re.match(r"^[a-zA-Z_][\w-]*\s*:", line):
                break
            out.append(line)
    return out if out else None


def detect_link_field_issues(raw_fm: str, field: str) -> list[str]:
    block = link_field_block(raw_fm, field)
    if block is None:
        return []
    head = block[0]
    issues: list[str] = []

    # Head-line inline value
    head_val = head.split(":", 1)[1].strip() if ":" in head else ""

    if head_val:
        # Disallow inline comma-list of wikilinks without proper quoting:
        # `related: [[a]], [[b]]` or `related: [[a]]`
        if "[[" in head_val:
            issues.append(
                f"{field}: inline wikilink(s) on head line — use multiline list of quoted strings"
            )
        # Allow `related: []` or `related: "[[a]]"` or `related:` (empty head) only

    # Nested-list corruption: lines of shape `  - - something`
    for line in block[1:]:
        if re.match(r"^\s+- - ", line):
            issues.append(f"{field}: nested-list corruption (`- -`) detected")
            break

    # Multiline list items should be quoted strings
    for line in block[1:]:
        m = re.match(r"^\s+-\s+(.+?)\s*$", line)
        if not m:
            continue
        val = m.group(1)
        if val.startswith("- "):
            continue  # already flagged as nested-list
        if "[[" in val and not (val.startswith('"') or val.startswith("'")):
            issues.append(f"{field}: list item `{val}` is a wikilink but not a quoted string")

    return issues


def extract_wikilinks_from_field_block(block: list[str]) -> list[str]:
    if not block:
        return []
    joined = "\n".join(block)
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(joined)]


def extract_all_ids(all_notes: list[tuple[Path, str, str]]) -> dict[str, Path]:
    """id → path. Warns on duplicates (resolved elsewhere)."""
    ids: dict[str, Path] = {}
    for path, raw_fm, _body in all_notes:
        nid = parse_id(raw_fm)
        if nid:
            ids.setdefault(nid, path)
    return ids


def main() -> int:
    all_notes: list[tuple[Path, str, str]] = []  # (path, raw_frontmatter, body)
    for root in ROOTS:
        if not root.exists():
            continue
        for p in sorted(root.rglob("*.md")):
            text = p.read_text(encoding="utf-8", errors="replace")
            raw_fm, body = split_frontmatter(text)
            all_notes.append((p, raw_fm, body))
    for p in ROOT_FILES:
        if p.exists():
            text = p.read_text(encoding="utf-8", errors="replace")
            raw_fm, body = split_frontmatter(text)
            if raw_fm.strip():
                all_notes.append((p, raw_fm, body))

    known_ids = extract_all_ids(all_notes)

    # Duplicates
    id_paths: dict[str, list[Path]] = defaultdict(list)
    for path, raw_fm, _ in all_notes:
        nid = parse_id(raw_fm)
        if nid:
            id_paths[nid].append(path)
    duplicates = {i: ps for i, ps in id_paths.items() if len(ps) > 1}

    # Per-file checks
    missing_keys: list[tuple[Path, set[str]]] = []
    bad_types: list[tuple[Path, str]] = []
    no_frontmatter: list[Path] = []
    link_field_issues: list[tuple[Path, str, str]] = []
    broken_wikilinks: list[tuple[Path, str, str]] = []  # (path, location, slug)

    for path, raw_fm, body in all_notes:
        if not raw_fm.strip():
            no_frontmatter.append(path)
            continue

        top_keys = set(parse_top_level_keys(raw_fm).keys())
        missing = REQUIRED_KEYS - top_keys
        if missing:
            missing_keys.append((path, missing))

        t = parse_type(raw_fm)
        if t and t not in ALLOWED_TYPES:
            bad_types.append((path, t))

        # Link-field shape + resolution
        for field in LINK_FIELDS:
            issues = detect_link_field_issues(raw_fm, field)
            for issue in issues:
                link_field_issues.append((path, field, issue))

            block = link_field_block(raw_fm, field)
            for slug in extract_wikilinks_from_field_block(block or []):
                if slug not in known_ids:
                    broken_wikilinks.append((path, f"frontmatter:{field}", slug))

        # Body wikilinks — strip fenced + inline code first (schema examples, etc.)
        body_stripped = CODE_FENCE_RE.sub("", body)
        body_stripped = INLINE_CODE_RE.sub("", body_stripped)
        for m in WIKILINK_RE.finditer(body_stripped):
            slug = m.group(1).strip()
            if slug not in known_ids:
                broken_wikilinks.append((path, "body", slug))

    # Report
    print("=" * 72)
    print(f"Vault lint — {len(all_notes)} notes scanned under {VAULT}")
    print("=" * 72)

    total_issues = 0

    def section(title: str, count: int) -> None:
        nonlocal total_issues
        total_issues += count
        print(f"\n[{title}] {count}")

    section("notes without frontmatter", len(no_frontmatter))
    for p in no_frontmatter:
        print(f"  - {p.relative_to(VAULT)}")

    section("missing required keys", len(missing_keys))
    for p, missing in missing_keys:
        print(f"  - {p.relative_to(VAULT)} :: missing {sorted(missing)}")

    section("bad type values", len(bad_types))
    for p, t in bad_types:
        print(f"  - {p.relative_to(VAULT)} :: type={t!r}")

    section("duplicate ids", len(duplicates))
    for i, ps in duplicates.items():
        print(f"  - id={i!r} used by {len(ps)} files:")
        for p in ps:
            print(f"      {p.relative_to(VAULT)}")

    section("link-field shape issues", len(link_field_issues))
    for p, field, issue in link_field_issues:
        print(f"  - {p.relative_to(VAULT)} :: {issue}")

    section("broken wikilinks", len(broken_wikilinks))
    for p, loc, slug in broken_wikilinks:
        print(f"  - {p.relative_to(VAULT)} :: [[{slug}]] ({loc})")

    print("\n" + "=" * 72)
    print(f"TOTAL ISSUES: {total_issues}")
    print("=" * 72)

    return 0 if total_issues == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
