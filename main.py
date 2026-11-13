#!/usr/bin/env python3
"""news-image-01-entry: deliver the bundled artwork to /output/entry.png.

This entry is a static infographic image. The program does not generate
or modify the image; it simply copies the bundled ``entry.png`` that
ships next to this script, byte-for-byte, into ``/output/entry.png``.

Standard library only. No network access. Deterministic: every run
writes the exact same bytes.
"""

import hashlib
import os
import shutil
import sys


def sha256_of(path):
    """Return the hex SHA-256 digest of the file at *path*."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def deliver_artwork(source, destination):
    """Copy *source* to *destination* byte-for-byte and return its digest."""
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    shutil.copyfile(source, destination)
    return sha256_of(destination)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, "entry.png")
    destination_dir = "/output"
    destination = os.path.join(destination_dir, "entry.png")

    if not os.path.isfile(source):
        print("error: bundled artwork not found: " + source, file=sys.stderr)
        return 1

    digest = deliver_artwork(source, destination)
    print("wrote " + destination + " (sha256 " + digest + ")")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
