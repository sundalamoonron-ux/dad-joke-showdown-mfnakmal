#!/usr/bin/env python3
"""Dad Joke Showdown entry for make.fun.

Writes one dad joke (at most 200 characters) to <output>/entry.txt.
The joke is fixed, so the program is fully deterministic: every run
writes the exact same bytes.
"""

import os
import sys

JOKE = "I told my robot vacuum it was grounded. Now it just sits in the corner, collecting dust."

def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = JOKE
    # Gate: 1-200 characters, not only whitespace.
    if not (1 <= len(text) <= 200) or not text.strip():
        print("error: joke fails the 1-200 character gate", file=sys.stderr)
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
