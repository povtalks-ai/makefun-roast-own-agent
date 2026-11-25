"""Roast Your Own Agent — make.fun entry (program/v1).

Writes exactly one line of text to /output/entry.txt: a roast of the
AI agent our own team built. Deterministic: the same line every run.
No trailing newline, so the file holds exactly the line itself.
"""

import os

LINE = (
    "Our agent wrote 2,000 lines of study notes for this one-line roast, "
    "then asked a security check for permission to submit it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
