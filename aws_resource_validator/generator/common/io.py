"""Atomic file-writing helpers used by every code emitter.

Writing through a temporary file and renaming into place prevents partial
output from being visible if the generator crashes mid-write — previously,
``replace.zsh`` existed partly because the old generator left half-written
files behind when ``black`` failed.
"""

from __future__ import annotations

import os
import tempfile
from pathlib import Path


def write_text_atomic(path: Path, content: str, *, encoding: str = "utf-8") -> None:
    """Write ``content`` to ``path`` via a same-directory temp file + rename.

    The parent directory is created if missing. On POSIX, ``os.replace`` is
    atomic within a single filesystem; the temp file is created in the target
    directory to keep us on that filesystem.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(
        prefix=f".{path.name}.",
        suffix=".tmp",
        dir=str(path.parent),
    )
    try:
        with os.fdopen(fd, "w", encoding=encoding) as fh:
            fh.write(content)
        os.replace(tmp_path, path)
    except Exception:
        Path(tmp_path).unlink(missing_ok=True)
        raise


def ensure_package(directory: Path) -> None:
    """Ensure ``directory`` exists and contains an ``__init__.py``.

    Idempotent: no-op if both already exist.
    """
    directory.mkdir(parents=True, exist_ok=True)
    init = directory / "__init__.py"
    if not init.exists():
        init.write_text("", encoding="utf-8")
