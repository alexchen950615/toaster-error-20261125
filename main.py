#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun bounty entry.

Competition: u-eager-stork-81-9647-the-funniest-toaster-error-436406cd
Task: write the funniest toaster error message, a single line of 1-120 chars.
Repository: https://github.com/alexchen950615/toaster-error-20261125

Writes the entry to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Only that one file is written; the sandbox filesystem is read-only
except for /output and /tmp, so no other output path is attempted.
"""

import os

ENTRY = "ERROR: I burned your toast again. I am sorry. I was thinking about my own mortality. Please forgive me."


def main() -> None:
    # Gate: entry must be a single line of 1-120 characters.
    assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, must be 1-120"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Sandbox-safe: exactly one output file, created under MAKEFUN_OUTPUT_DIR.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
