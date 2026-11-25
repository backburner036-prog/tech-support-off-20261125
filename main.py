"""Have You Tried Turning It Off? -- make.fun entry.

Writes one line, a hopeless tech support agent's reply to a desperate
customer, to /output/entry.txt.
"""

from pathlib import Path

LINE = "Let's try turning it off and on again. If that doesn't work, I'll escalate you to someone who will suggest exactly the same thing."
OUT_PATH = Path("/output/entry.txt")
MIN_LEN = 1
MAX_LEN = 199


def trim_to_gate(text: str) -> str:
    """Collapse stray whitespace at the edges; the gate counts characters."""
    return " ".join(text.split())


def check_gate(text: str) -> str:
    """The sealed scorer wants 1-199 chars of non-blank UTF-8 text."""
    cleaned = trim_to_gate(text)
    assert MIN_LEN <= len(cleaned) <= MAX_LEN, (
        f"entry is {len(cleaned)} chars, gate wants 1-199"
    )
    assert cleaned.strip(), "entry must not be blank"
    return cleaned


def drop_line(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    # Round-trip: what the grader reads must be exactly what we wrote.
    assert path.read_text(encoding="utf-8") == text, "entry.txt round-trip mismatch"


def main() -> None:
    drop_line(OUT_PATH, check_gate(LINE))


if __name__ == "__main__":
    main()
