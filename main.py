#!/usr/bin/env python3
"""Funniest Lost Sock Status Update.

Writes a single status update, in the voice of a lost sock, to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).

Pure Python standard library only; no third-party packages.
"""

import os

STATUS = (
    "Update: I've been promoted to puppet. The kid loves me, "
    "the dog fears me, and HR says I can't go back to being a sock."
)


def validate(text):
    """Enforce the competition gate: one line, 1-120 chars, not blank."""
    if "\n" in text or "\r" in text:
        raise ValueError("status update must be a single line")
    if not (1 <= len(text) <= 120):
        raise ValueError(
            "status update must be 1-120 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("status update must not be only whitespace")
    text.encode("utf-8")  # must be encodable as UTF-8


def main():
    validate(STATUS)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    data = STATUS.encode("utf-8")
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, data)
    finally:
        os.close(fd)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
