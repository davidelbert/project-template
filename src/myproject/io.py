"""Data I/O — loading, parsing, light validation.

Functions here are imported by notebooks. Keep them small and pure where you can.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """Load a CSV from disk into a DataFrame.

    Replace this stub with project-specific loaders as the project grows.
    """
    return pd.read_csv(Path(path))
