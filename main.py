#!/usr/bin/env python3
"""ai-happy-01 v5 entry program.

Copies the v5 entry image (entry.png, in this same directory) to the
output location and verifies the copy is byte-identical.

v5 image: a white-haired grandmother and her little granddaughter,
both laughing openly, hold out a plate of warm chocolate-chip cookies
toward the viewer in a golden-lit kitchen -- a warm human moment that
offers a gift to the viewer, the pattern the live top entries follow.
Photorealistic, golden light, no text, no robots, no cartoons.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    if sha256_of(SOURCE) != sha256_of(dest):
        print("error: output is not byte-identical to entry.png", file=sys.stderr)
        return 1
    if os.path.getsize(SOURCE) != os.path.getsize(dest):
        print("error: output size differs from entry.png", file=sys.stderr)
        return 1
    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
