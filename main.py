#!/usr/bin/env python3
"""Write the world-news front page for Monday, 23 November 2026.

Stdlib only. Copies the pre-rendered entry.png shipped in this repo
to /output/entry.png (the location the grader reads).
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote", DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())
