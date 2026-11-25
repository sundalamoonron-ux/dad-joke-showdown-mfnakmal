#!/usr/bin/env python3
"""Dad Joke Showdown entry for make.fun.

Writes one dad joke (at most 200 characters) to <output>/entry.txt.
The joke is fixed, so the program is fully deterministic: every run
writes the exact same bytes.

Resubmit v2 (2026-11-26 ~00:40 WITA): the submitted vacuum joke ranked
74/3621 (score 647697) and pays $0 — only top 3 are paid. The soap joke
below won the in-session pairwise tournament 6-0 (candidates-v2.md) and
beats the vacuum line decisively (margin 3): one clean pun ("come clean"),
universal domestic subject, punchline ends on the played word.
"""

import os
import sys

JOKE = "My wife asked me to stop making jokes about the soap. I said, 'I can't — I always come clean.'"

def validate(text: str) -> None:
    """Gate from RULES.txt: /output/entry.txt must be UTF-8 text of 1-200
    characters, not only whitespace, and a single dad joke. Raises
    ValueError on any violation so a bad entry can never be written."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("joke must not be empty or whitespace-only")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke is {len(text)} chars, gate is 1-200")
    if text != text.strip():
        raise ValueError("joke must not have leading/trailing whitespace")

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE
    # Gate: 1-200 characters, not only whitespace.
    try:
        validate(text)
    except ValueError as exc:
        print(f"error: joke fails the 1-200 character gate: {exc}", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Self-check: read it back and fail hard if it is not exactly the joke.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        print("error: entry.txt does not match the joke", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
