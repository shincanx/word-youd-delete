#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary entry.

The word is "irregardless": a double-negative mistake that bullied its way
into the dictionary, where it now sits legitimised despite meaning exactly
what "regardless" already means. Deleting it is the dictionary correcting
its own mistake -- and nothing is lost, because "regardless" was doing the
job all along.

Writes the word to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: no randomness, no network, no input files.
"""

import os

WORD = "irregardless"


def main():
    # The gate allows 1-77 characters; a single word, no spaces, no newline.
    # Normalise defensively so the file holds exactly the word, nothing else.
    word = WORD.strip().lower()
    assert word and word.isalpha() and " " not in word and len(word) <= 77
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
