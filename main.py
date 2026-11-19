"""One picture for the news of Wednesday 18 November 2026.

The bundled picture tells the day in three scenes:

- leaders meet in Shenzhen as the APEC gathering opens, with a
  three-way session due the next day;
- jets and drones trade blows across the Gulf after a strike on
  an island missile site;
- a bridge to Crimea is struck again and a stretch of its roadway
  drops into the sea.

The script draws nothing and needs no network: it hands the
bundled picture to the output folder, so repeated runs agree.
"""

import os
import sys
from pathlib import Path

ORIGIN = Path(__file__).resolve().parent / "entry.png"
OUTDIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
OUTFILE = OUTDIR / "entry.png"
CEILING = 1024 * 1024


def place() -> None:
    data = ORIGIN.read_bytes()
    if len(data) > CEILING:
        sys.exit(f"entry.png is {len(data)} bytes, over the {CEILING} byte limit")
    OUTDIR.mkdir(parents=True, exist_ok=True)
    OUTFILE.write_bytes(data)
    again = OUTFILE.read_bytes()
    if again != data:
        sys.exit("written file does not match the bundled picture")
    print(f"wrote {OUTFILE} ({len(data)} bytes)")


if __name__ == "__main__":
    place()
