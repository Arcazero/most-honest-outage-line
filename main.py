#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun bounty entry.

Writes one status-page line (129 characters, within the 160 cap) to
/output/entry.txt. The line is a fixed string: the output is byte-identical
on every run.
"""

import os

LINE = (
    "Every server is down, including the ones I run on. "
    "I can't reach anything to check what broke, "
    "so I have no cause and no ETA yet."
)


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, must be 1-160"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
