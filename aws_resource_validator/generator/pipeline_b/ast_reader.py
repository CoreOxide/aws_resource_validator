"""Thin wrapper around :func:`ast.parse` with per-file memoization."""

from __future__ import annotations

import ast
from functools import cache
from pathlib import Path


@cache
def read_module(path: Path) -> ast.Module:
    """Parse the Python source at ``path`` and return its AST module node.

    Memoized: reading the same stub file twice in one generator run is cheap.
    The cache is keyed by :class:`~pathlib.Path`, so different paths
    pointing at the same file produce distinct cache entries.
    """
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
