"""drive-grep — offline query over the vault's Drive sources.

Usage:
    python drive_grep.py catalog <pattern>
    python drive_grep.py folders <pattern>
    python drive_grep.py summary <idx>
    python drive_grep.py summary-grep <pattern>

See SKILL.md for full description.
"""
import json
import re
import sys
from pathlib import Path

VAULT = Path(r"C:\dev\ahmad-brain")
CATALOG = VAULT / "wiki" / "sources" / "drive-catalog.md"
MASTER = VAULT / "wiki" / "sources" / "drive-folders-master-index.md"
JSONL = Path(r"C:\Users\aass1\ahmad-brain-import\drive-folders-gemini.jsonl")
INVENTORY = VAULT / "raw" / "drive" / "full-inventory.tsv"


def cmd_catalog(pattern: str) -> int:
    if not CATALOG.exists():
        print(f"[error] catalog not found at {CATALOG}", file=sys.stderr)
        return 2
    needle = pattern.lower()
    hits = []
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        if needle in line.lower():
            hits.append(line.strip())
    for h in hits:
        print(h)
    print(f"\n[{len(hits)} match(es) for '{pattern}' in drive-catalog.md]", file=sys.stderr)
    return 0 if hits else 1


def cmd_folders(pattern: str) -> int:
    if not MASTER.exists():
        print(f"[error] master index not found at {MASTER}", file=sys.stderr)
        return 2
    needle = pattern.lower()
    rows = []
    in_table = False
    for line in MASTER.read_text(encoding="utf-8").splitlines():
        if line.startswith("| #") or line.startswith("|---"):
            in_table = True
            continue
        if in_table and line.startswith("|") and "|" in line[1:]:
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= 2 and needle in line.lower():
                rows.append((cells[0], cells[1] if len(cells) > 1 else ""))
        elif in_table and not line.startswith("|"):
            in_table = False
    for idx, name in rows:
        print(f"#{idx}\t{name}")
    print(f"\n[{len(rows)} match(es) for '{pattern}' in 68-folder master index]", file=sys.stderr)
    return 0 if rows else 1


def cmd_summary(idx_str: str) -> int:
    if not JSONL.exists():
        print(f"[error] JSONL not found at {JSONL}", file=sys.stderr)
        return 2
    try:
        idx = int(idx_str)
    except ValueError:
        print(f"[error] idx must be an integer, got '{idx_str}'", file=sys.stderr)
        return 2
    with JSONL.open(encoding="utf-8") as f:
        for line in f:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if row.get("idx") == idx:
                print(f"=== Folder #{idx}: {row.get('title', '?')} ===\n")
                print(row.get("summary", row.get("content", "(no summary field)")))
                return 0
    print(f"[no entry found for idx={idx}]", file=sys.stderr)
    return 1


def cmd_summary_grep(pattern: str) -> int:
    if not JSONL.exists():
        print(f"[error] JSONL not found at {JSONL}", file=sys.stderr)
        return 2
    needle = pattern.lower()
    total_hits = 0
    with JSONL.open(encoding="utf-8") as f:
        for line in f:
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            text = row.get("summary", row.get("content", ""))
            idx = row.get("idx", "?")
            title = row.get("title", "?")
            for ln_no, ln in enumerate(text.split("\n"), 1):
                if needle in ln.lower():
                    print(f"#{idx} {title} :{ln_no}: {ln.strip()[:200]}")
                    total_hits += 1
    print(f"\n[{total_hits} match(es) across 68 folder summaries]", file=sys.stderr)
    return 0 if total_hits else 1


def cmd_inventory(pattern: str) -> int:
    if not INVENTORY.exists():
        print(f"[error] inventory not found at {INVENTORY}", file=sys.stderr)
        return 2
    needle = pattern.lower()
    hits = 0
    for line in INVENTORY.read_text(encoding="utf-8").splitlines():
        if needle in line.lower():
            print(line)
            hits += 1
    print(f"\n[{hits} match(es) for '{pattern}' in full-inventory.tsv ({INVENTORY.stat().st_size:,} bytes, ~{sum(1 for _ in INVENTORY.open(encoding='utf-8'))} lines)]", file=sys.stderr)
    return 0 if hits else 1


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2
    cmd = argv[1]
    arg = " ".join(argv[2:])
    handlers = {
        "catalog": cmd_catalog,
        "folders": cmd_folders,
        "summary": cmd_summary,
        "summary-grep": cmd_summary_grep,
        "inventory": cmd_inventory,
    }
    handler = handlers.get(cmd)
    if not handler:
        print(f"[error] unknown subcommand '{cmd}'. Valid: {', '.join(handlers)}", file=sys.stderr)
        return 2
    return handler(arg)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
