"""Smoke test — proves the package imports and CI is wired up.

This test reads the package name from pyproject.toml rather than
hard-coding `import myproject`, so it keeps passing after you rename the
placeholder package in Step 3 — you don't have to touch this file.

Replace or augment this with real tests as you build out src/.
"""

import importlib
import tomllib
from pathlib import Path


def _package_name() -> str:
    pyproject = Path(__file__).resolve().parent.parent / "pyproject.toml"
    return tomllib.loads(pyproject.read_text(encoding="utf-8"))["project"]["name"]


def test_package_imports():
    pkg = importlib.import_module(_package_name())
    assert pkg.__version__
