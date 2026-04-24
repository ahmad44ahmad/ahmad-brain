"""
One-shot normalizer for YAML link-list fields.

Converts every `related` / `amends` / `supersedes` / `superseded-by` field in
every vault note to canonical form:

    related:
      - "[[slug-1]]"
      - "[[slug-2]]"

Handles these input shapes:
  - Head-line inline: `related: [[a]], [[b]]`
  - Head-line flow list: `related: [[[a]], [[b]]]`
  - Nested-list corruption: `related:\n  - - a`
  - Multiline unquoted: `related:\n  - [[a]]`
  - Already-canonical: `related:\n  - "[[a]]"` (left untouched)

Dry-run by default. Pass --apply to write files.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

VAULT = Path(r"C:\dev\ahmad-brain")
ROOTS = [VAULT / "wiki", VAULT / "decisions", VAULT / "log"]
ROOT_FILES = [VAULT / "_CLAUDE.md"]

LINK_FIELDS = ("related", "amends", "supersedes", "superseded-by")
FRONTMATTER_RE = re.compile(r"^(---\s*\n)(.*?)(\n---\s*\n)", re.DOTALL)
SLUG_RE = re.compile(r"\[\[([^\[\]|#]+?)(?:#[^\[\]|]*)?(?:\|[^\[\]]*)?\]\]")
BARE_SLUG_LINE_RE = re.compile(r"^\s+-\s+-\s+([a-zA-Z0-9][\w-]*)\s*$")


def find_field_block(lines: list[str], field: str) -> tuple[int, int] | None:
    """Return (start_idx, end_idx_exclusive) of the field's block, or None."""
    start: int | None = None
    for i, line in enumerate(lines):
        if re.match(rf"^{re.escape(field)}\s*:", line):
            start = i
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start + 1, len(lines)):
        # Another top-level key or comment terminates the block
        if re.match(r"^[a-zA-Z_][\w-]*\s*:", lines[j]):
            end = j
            break
    return start, end


def extract_slugs(block_lines: list[str]) -> list[str]:
    slugs: list[str] = []
    seen: set[str] = set()
    joined = "\n".join(block_lines)

    # Canonical wikilink form first
    for m in SLUG_RE.finditer(joined):
        s = m.group(1).strip()
        if s and s not in seen:
            slugs.append(s)
            seen.add(s)

    # Nested-list corruption: `  - - bare-slug` (no brackets).
    # Only collect slugs that didn't already appear bracketed.
    for line in block_lines:
        m = BARE_SLUG_LINE_RE.match(line)
        if m:
            s = m.group(1).strip()
            if s and s not in seen:
                slugs.append(s)
                seen.add(s)

    return slugs


def canonical_block(field: str, slugs: list[str]) -> list[str]:
    if not slugs:
        return [f"{field}: []"]
    out = [f"{field}:"]
    for s in slugs:
        out.append(f'  - "[[{s}]]"')
    return out


def already_canonical(block_lines: list[str], field: str) -> bool:
    """Check whether the block is already in canonical form."""
    if not block_lines:
        return False
    head = block_lines[0]
    # Head must be `field:` with nothing after the colon (empty value)
    if not re.match(rf"^{re.escape(field)}\s*:\s*$", head):
        return False
    for line in block_lines[1:]:
        if not line.strip():
            continue
        # Each item must be `  - "[[slug]]"`
        if not re.match(r'^\s+-\s+"\[\[[^\[\]]+\]\]"\s*$', line):
            return False
    return True


def normalize_frontmatter(raw_fm: str) -> tuple[str, list[str]]:
    """Return (new_frontmatter, list_of_changes). Preserves blank lines and
    everything outside the four link fields."""
    lines = raw_fm.split("\n")
    changes: list[str] = []

    # Process in reverse so index edits don't clobber each other.
    for field in LINK_FIELDS:
        block = find_field_block(lines, field)
        if not block:
            continue
        start, end = block
        block_lines = lines[start:end]
        # Trim trailing blank lines inside the block (they'll be reintroduced by caller layout)
        while block_lines and not block_lines[-1].strip():
            block_lines.pop()

        if already_canonical(block_lines, field):
            continue

        slugs = extract_slugs(block_lines)
        new_block = canonical_block(field, slugs)
        if new_block != block_lines:
            # Preserve a trailing blank line if the original block had one before the next key
            lines[start:end] = new_block + [""] if (end < len(lines) and lines[end - 1].strip() == "" if end - 1 >= start else False) else new_block
            changes.append(f"{field}: {len(slugs)} slug(s)")

    return "\n".join(lines), changes


def normalize_file(path: Path, apply: bool) -> tuple[bool, list[str]]:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return False, []
    raw_fm = m.group(2)
    new_fm, changes = normalize_frontmatter(raw_fm)
    if not changes:
        return False, []
    new_text = m.group(1) + new_fm + m.group(3) + text[m.end():]
    if apply:
        path.write_text(new_text, encoding="utf-8")
    return True, changes


def iter_targets() -> list[Path]:
    targets: list[Path] = []
    for root in ROOTS:
        if root.exists():
            targets.extend(sorted(root.rglob("*.md")))
    for p in ROOT_FILES:
        if p.exists():
            targets.append(p)
    return targets


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="Write changes (default: dry run)")
    args = ap.parse_args()

    touched = 0
    for path in iter_targets():
        changed, changes = normalize_file(path, apply=args.apply)
        if changed:
            touched += 1
            rel = path.relative_to(VAULT)
            verb = "would update" if not args.apply else "updated"
            print(f"{verb} {rel} :: {', '.join(changes)}")

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"\n[{mode}] {touched} file(s) {'updated' if args.apply else 'would be updated'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
