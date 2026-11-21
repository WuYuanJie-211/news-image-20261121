"""news-image-20261121 entry (Python 3, standard library only).

The entry image is the entry.png in this directory. The program copies it
to the output directory: /output by default, or MAKEFUN_OUTPUT_DIR when set.

Deterministic: a pure byte copy. No network access, no timestamps, no
randomness, so two runs produce identical bytes. Run locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUT.mkdir(parents=True, exist_ok=True)

SRC = HERE / "entry.png"
DST = OUT / "entry.png"
shutil.copyfile(SRC, DST)

# Self-check: the copy must be a whole PNG, at most 1024x1024 pixels and
# at most 1 MiB, or the entry would fail the gate. Fail loudly instead of
# shipping a corrupt or oversized file.
data = DST.read_bytes()
if data[:8] != b"\x89PNG\r\n\x1a\n":
    sys.exit("entry.png is not a PNG")
width, height = struct.unpack(">II", data[16:24])
if width > 1024 or height > 1024:
    sys.exit(f"entry.png is {width}x{height}, over the 1024 cap")
if len(data) > 1048576:
    sys.exit(f"entry.png is {len(data)} bytes, over the 1 MiB cap")
print(f"wrote {DST} ({width}x{height}, {len(data)} bytes)")
