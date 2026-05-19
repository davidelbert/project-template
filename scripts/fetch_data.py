"""Fetch raw data for this project from OSF (osf.io) into data/raw/.

UVM Open Science projects are deposited on OSF. This pulls every file in
a public OSF project's storage down to data/raw/, preserving the folder
layout. Raw data is gitignored — this script is how anyone gets it back.

Usage:
    uv run python scripts/fetch_data.py --project abcde
    OSF_PROJECT=abcde uv run python scripts/fetch_data.py

Requires the optional "data" dependencies:
    uv pip install -e ".[dev,data]"

For private/embargoed projects or non-OSF sources, see DATA.md and adapt.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

DEST_DEFAULT = Path(__file__).resolve().parent.parent / "data" / "raw"


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Download an OSF project's files into data/raw/.")
    p.add_argument(
        "--project",
        default=os.environ.get("OSF_PROJECT"),
        help="OSF project ID (the 5-char code in the URL, e.g. 'abcde'). "
        "Defaults to the OSF_PROJECT environment variable.",
    )
    p.add_argument(
        "--dest",
        type=Path,
        default=DEST_DEFAULT,
        help=f"Destination directory (default: {DEST_DEFAULT}).",
    )
    p.add_argument(
        "--overwrite",
        action="store_true",
        help="Re-download files that already exist locally.",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()

    if not args.project:
        sys.exit(
            "No OSF project ID given. Pass --project <id> or set OSF_PROJECT.\n"
            "Find the ID in the OSF URL: https://osf.io/<id>/  — see DATA.md."
        )

    try:
        from osfclient import OSF
    except ModuleNotFoundError:
        sys.exit(
            "osfclient is not installed. Install the data extra:\n"
            '    uv pip install -e ".[dev,data]"'
        )

    dest: Path = args.dest
    dest.mkdir(parents=True, exist_ok=True)

    osf = OSF()  # anonymous — works for public projects
    try:
        project = osf.project(args.project)
    except Exception as exc:  # noqa: BLE001 — surface any OSF error plainly
        sys.exit(f"Could not open OSF project {args.project!r}: {exc}")

    n_got = n_skipped = 0
    for store in project.storages:
        for file in store.files:
            target = dest / file.path.lstrip("/")
            if target.exists() and not args.overwrite:
                print(f"skip  {file.path} (exists)")
                n_skipped += 1
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            print(f"fetch {file.path}")
            with open(target, "wb") as fp:
                file.write_to(fp)
            n_got += 1

    print(f"\nDone. {n_got} downloaded, {n_skipped} skipped, into {dest}")
    if n_got == 0 and n_skipped == 0:
        print("No files found. Check the project ID and that it's public.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
