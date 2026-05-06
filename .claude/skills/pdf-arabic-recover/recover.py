"""pdf-arabic-recover — recover Arabic text from per-word-reversed PDF exports.

Usage:
    python recover.py < input.txt > output.txt
    echo "نص معكوس" | python recover.py
    python recover.py file.txt   # path argument also accepted

The script applies per-word character reversal to each line of input.
See SKILL.md for full description, when to apply, and limitations.
"""
import sys
from pathlib import Path


def recover_line(line: str) -> str:
    """Reverse characters within each whitespace-separated word; preserve word order."""
    return " ".join(w[::-1] for w in line.split(" "))


def main(argv: list[str]) -> int:
    if len(argv) >= 2 and argv[1] not in ("-", "--stdin"):
        path = Path(argv[1])
        if not path.exists():
            print(f"[error] file not found: {path}", file=sys.stderr)
            return 2
        text = path.read_text(encoding="utf-8")
    else:
        text = sys.stdin.read()

    for line in text.splitlines():
        # Preserve all whitespace runs by splitting only on single spaces;
        # leading/trailing whitespace is preserved in the line as a unit.
        recovered = recover_line(line)
        print(recovered)

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
