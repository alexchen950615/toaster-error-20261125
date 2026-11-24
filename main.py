#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun bounty entry.

Writes the entry (a single line, 1-120 chars) to /output/entry.txt
(and mirrors it to /opt/output/entry.txt, which shares the same
output location in some build environments).
"""

ENTRY = "ERROR: I burned your toast again. I am sorry. I was thinking about my own mortality. Please forgive me."

OUTPUT_PATHS = ["/output/entry.txt", "/opt/output/entry.txt"]


def main() -> None:
    # Gate: entry must be a single line of 1-120 characters.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, must be 1-120"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    for path in OUTPUT_PATHS:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
