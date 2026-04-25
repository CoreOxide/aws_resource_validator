"""Central logger factory for all generator code.

All generator modules call :func:`get_logger` instead of using :func:`print`
or instantiating their own loggers. This gives us a single place to tune the
format and level (including from tests, which set the level explicitly).
"""

from __future__ import annotations

import logging
from functools import cache

_DEFAULT_FORMAT = "%(asctime)s %(levelname)-7s %(name)s: %(message)s"


@cache
def _configure_root_once() -> None:
    logging.basicConfig(format=_DEFAULT_FORMAT)


def get_logger(name: str, *, level: int = logging.INFO) -> logging.Logger:
    """Return a logger for the given dotted ``name``.

    The first call wires up the root handler; every call sets the requested
    level on the root logger so tests and the CLI can reliably change verbosity.
    """
    _configure_root_once()
    logging.getLogger().setLevel(level)
    return logging.getLogger(name)
