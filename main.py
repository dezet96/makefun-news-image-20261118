"""news-image-20261118 entry: sum up Wednesday 18 November 2026 in one image.

The image (entry.png, a JPEG kept under a .png name, as the rules allow)
is a three-panel editorial illustration of the day's world news:

  1. Xi Jinping greets Donald Trump on the tarmac in Shenzhen as APEC
     opens, with Vladimir Putin beside them, ahead of Thursday's
     three-way talks.
  2. US fighter jets strike an Iranian missile launch site on Qeshm
     Island at night, as Iranian drones fly over the Gulf toward
     American bases in Kuwait and Bahrain.
  3. Ukraine strikes the Kerch Bridge to Crimea for a second day, and
     part of the road span collapses into the sea.

The program has no network access and draws nothing at run time: it
copies the bundled image to the output directory, so two runs write
identical bytes — the output is fully deterministic by construction.

Usage (outside the grader's container):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

# The image bundled beside this file, and where the grader expects it.
SOURCE_IMAGE = Path(__file__).resolve().parent / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTPUT_IMAGE = OUTPUT_DIR / "entry.png"

# The gate accepts a whole PNG or JPEG of at most 1 MiB.
MAX_BYTES = 1_048_576


def main() -> None:
    image = SOURCE_IMAGE.read_bytes()
    if len(image) > MAX_BYTES:
        raise SystemExit(
            f"entry.png is {len(image)} bytes, over the {MAX_BYTES} byte limit"
        )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE_IMAGE, OUTPUT_IMAGE)
    copied = OUTPUT_IMAGE.read_bytes()
    if copied != image:
        raise SystemExit("copy mismatch: output bytes differ from entry.png")
    print(f"wrote {OUTPUT_IMAGE} ({len(image)} bytes)")


if __name__ == "__main__":
    main()
