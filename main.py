"""ai-happy-01 entry (Python 3.13, standard library only).

The image is entry.png beside this file; the program copies it to
/output/entry.png. The gate takes a whole PNG or JPEG of at most 1 MiB
and 1024 by 1024 pixels, and the judge sees exactly the bytes copied.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")

# The run must write exactly the image's bytes: confirm the copy is whole.
assert (OUT / "entry.png").read_bytes() == (HERE / "entry.png").read_bytes()
