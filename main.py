#!/usr/bin/env python3
"""news-image-20261120 entrypoint.

Copies the pre-rendered front page (entry-v1.png) to the output directory
as entry.png. The program is deterministic: every run writes the same bytes.
"""
import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = here / "entry-v1.png"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    print("news-image-20261120: wrote %d bytes to %s" % (dst.stat().st_size, dst))


if __name__ == "__main__":
    main()
