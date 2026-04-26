"""Pure name-conversion helpers used by both the runtime and the generator.

All functions here are side-effect free and independently unit-tested. They
are placed in ``core`` (rather than under ``generator``) because the runtime
service classes produced by Pipeline A call them to build attribute aliases.
"""

from __future__ import annotations

import keyword
import re

_CAMEL_TO_SNAKE = re.compile(r"(?<!^)(?=[A-Z])")
_NON_IDENTIFIER = re.compile(r"[^a-zA-Z0-9]")


def to_snake_case(name: str) -> str:
    """Convert ``CamelCase`` or ``PascalCase`` to ``snake_case``."""
    return _CAMEL_TO_SNAKE.sub("_", name).lower()


def to_pascal_case(name: str) -> str:
    """Convert an arbitrary string to ``PascalCase``.

    Non-alphanumeric characters act as word separators. If the resulting
    identifier collides with a Python keyword, a trailing underscore is
    appended.
    """
    cleaned = _NON_IDENTIFIER.sub("_", name)
    parts = [part for part in cleaned.split("_") if part]
    pascal = "".join(part[:1].upper() + part[1:] for part in parts)
    return f"{pascal}_" if keyword.iskeyword(pascal) else pascal


def safe_identifier(name: str) -> str:
    """Return a syntactically-valid Python identifier for ``name``.

    Dashes are replaced with underscores; reserved keywords get a trailing
    underscore. Does not enforce the start-with-letter rule — that is the
    caller's responsibility.
    """
    candidate = name.replace("-", "_")
    return f"{candidate}_" if keyword.iskeyword(candidate) else candidate
