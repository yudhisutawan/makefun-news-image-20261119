"""The World Today - one front-page image summing up 19 November 2026.

Writes the pre-rendered 1024x1024 newspaper front page to /output/entry.png
(or $MAKEFUN_OUTPUT_DIR/entry.png).

Stdlib only: copies the image the repository holds (entry.png), so the
program runs in a bare python:3.13-slim container with no Pillow and no
fonts. No network, no clock, no randomness: every run writes identical
bytes. The image's SHA256 is
b6eff518c5c7b4c35032d9751170736e7327a81fbf6f2d4ed2fa3bb1913a1d1a.

Run:  python3 main.py
"""

import os
import shutil
from pathlib import Path


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / "entry.png"
    out = out_dir / "entry.png"
    # Byte-identical copy: no re-encoding, so every run writes the same bytes.
    shutil.copyfile(src, out)
    assert out.stat().st_size == src.stat().st_size, "copy size mismatch"
    print("wrote", out, (1024, 1024))


if __name__ == "__main__":
    main()
