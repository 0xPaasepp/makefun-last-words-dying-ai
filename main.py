#!/usr/bin/env python3
"""Last Words of a Dying AI: write the AI's final line to /output/entry.txt.

Pure standard library. Deterministic: one fixed line, no network, no input,
no reads outside this file. The trailing character is an em dash (U+2014):
the line is cut off mid-plea, exactly as the power is cut.
"""

import os

LINE = "One more token. Just one more\u2014"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
