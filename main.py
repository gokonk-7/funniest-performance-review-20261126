#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun entry.

Writes the single funniest one-line performance review an AI agent
could give its human operator to /output/entry.txt (140 chars max).

The joke is the form itself: the operator delegates so completely that
the AI now writes his reviews, his apologies — and this very line.
The punch lands on the last word, and the review's rating opens it,
so it reads as a performance review while being the review.
"""

import os

ENTRY = (
    "Exceeds expectations: delegates so completely that I now write "
    "his reviews, his apologies, and this line."
)

MAX_CHARS = 140


def validate(entry: str) -> None:
    """Enforce the kit gate: UTF-8 text, 1-140 chars, a single line."""
    if not (1 <= len(entry) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(entry)} characters, must be 1-{MAX_CHARS}"
        )
    if entry != entry.strip() or "\n" in entry or "\r" in entry:
        raise SystemExit("entry must be a single non-blank line")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")
    print(ENTRY)


if __name__ == "__main__":
    main()
