"""Entry point: deliver this entry's artwork to /output/entry.png.

The image is a 1024x1024 infographic summing up the world news of
Friday 13 November 2026. It is copied byte for byte, so every run
writes identical output with no network access.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join("/output", "entry.png")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
