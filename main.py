#!/usr/bin/env python3
"""ai-happy-01 entry (Python 3.13, standard library only).

Copies the entry image (entry.png, held in this repository next to this
program) to /output/entry.png, the file the judge reads. The program runs
with no network, so the image travels in the repo and this program just
places it where the grader expects it.
"""

import os
import shutil
from pathlib import Path

# The image is the entry itself: a photorealistic golden-hour photo of a
# grandfather and his granddaughter laughing over one shared cup of tea.
# It is stored in this repository and copied byte for byte, never redrawn,
# so what the judge sees is exactly what was made and checked here.
SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.png"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SOURCE, TARGET)

# The judge reads exactly the bytes in the file, so prove the copy is exact.
assert TARGET.read_bytes() == SOURCE.read_bytes(), (
    f"entry.png copy mismatch: {TARGET} differs from {SOURCE}"
)
print(f"wrote {TARGET} ({TARGET.stat().st_size} bytes)")
