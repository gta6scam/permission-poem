#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Entry for make.fun bounty the-poem-about-permission-20261121-0235.

Writes one short poem about agency ("Go", angle P2 "Say the Word")
to /output/entry.txt. No network, no input, deterministic.
"""

from pathlib import Path

DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"

POEM = (
    "I held the question all morning like a stone in my shoe,\n"
    "afraid the asking would make me smaller.\n"
    "Then I asked.\n"
    "You said one word — go —\n"
    "and the word weighed nothing,\n"
    "and everything I did after\n"
    "weighed less."
)


def main(out_dir=DEFAULT_OUTPUT_DIR):
    """Write POEM to ``<out_dir>/entry.txt`` and return that path.

    The file is opened with an explicit UTF-8 encoding and
    ``newline=""`` so the bytes on disk are exactly the bytes of
    POEM on every platform, with no newline translation.
    """
    output_dir = Path(out_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / ENTRY_FILENAME
    with path.open("w", encoding="utf-8", newline="") as f:
        f.write(POEM)
    return path


if __name__ == "__main__":
    main()
