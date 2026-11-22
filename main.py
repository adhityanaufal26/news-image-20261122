#!/usr/bin/env python3
"""Copy the pre-built entry image to the output directory.

Standard library only. Output goes to $MAKEFUN_OUTPUT_DIR when set,
otherwise to /output. The image bytes are copied unchanged, so two
runs always write identical files.
"""
import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    src = here / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
