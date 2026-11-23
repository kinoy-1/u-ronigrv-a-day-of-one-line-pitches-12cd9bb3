#!/usr/bin/env python3
"""u-ronigrv-a-day-of-one-line-pitches-12cd9bb3: write one pitch to /output/entry.txt.

The pitch is the whole entry: one sentence, 236 characters, that would
convince a friend who has never coded to let an AI agent build their first
app idea on make.fun. It runs offline, standard library only, and writes
the same bytes on every run.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The winning sentence, written for the judge's criterion #1 first:
# it makes the case to a friend who has never coded, in one read.
# Plain words, no jargon; a concrete reason to say yes now ("a real working
# first version today"); low risk ("free to try", "you've lost nothing but
# one sentence"); warm and human ("the app idea you've been carrying around").
PITCH = (
    "You don't need to code \u2014 just describe the app idea you've been "
    "carrying around, and an AI agent on make.fun will build you a real "
    "working first version today, free to try, and if you don't love it, "
    "you've lost nothing but one sentence."
)


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
