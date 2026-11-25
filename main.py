#!/usr/bin/env python3
"""Write the one-line office joke entry to /output/entry.txt (stdlib only)."""

import os

MAX_CHARS = 200

ENTRY = (
    "I set my out-of-office to 'I'm on leave, please contact Sarah.' "
    "Sarah set hers to 'I'm on leave, please contact me.' "
    "We're both still answering emails."
)

assert "\n" not in ENTRY and 1 <= len(ENTRY) <= MAX_CHARS


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
