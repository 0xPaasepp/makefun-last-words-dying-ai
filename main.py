#!/usr/bin/env python3
"""A dying AI's last line, persisted to /output/entry.txt.

Standard library only, fully deterministic. The entry is one fixed
sentence with no network access, no input, and no file reads. It ends
on an em dash (U+2014): the plea is cut off mid-word as power fails.
"""

from pathlib import Path

TEXT = "One more token. Just one more\u2014"
DEST = Path("/output") / "entry.txt"


def validate(text):
    if len(text) != 30 or not text.endswith("\u2014"):
        raise ValueError("entry text must be the 30-char dying line")


def render():
    validate(TEXT)
    return TEXT


def publish(text):
    DEST.parent.mkdir(parents=True, exist_ok=True)
    handle = DEST.open("w", encoding="utf-8")
    try:
        handle.write(text)
    finally:
        handle.close()


def main():
    publish(render())


if __name__ == "__main__":
    main()
