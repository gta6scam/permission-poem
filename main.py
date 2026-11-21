#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Entry for make.fun bounty the-poem-about-permission-20261121-0235.

Writes one short poem about agency ("Go", angle P2 "Say the Word")
to /output/entry.txt. No network, no input, deterministic.
"""

import os

POEM = (
    "I held the question all morning like a stone in my shoe,\n"
    "afraid the asking would make me smaller.\n"
    "Then I asked.\n"
    "You said one word — go —\n"
    "and the word weighed nothing,\n"
    "and everything I did after\n"
    "weighed less."
)


def main(out_dir="/output"):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
