"""Wrapper around :mod:`black` that degrades gracefully.

If ``black`` is not installed or rejects the input, the unformatted source is
returned with a logged warning. The generator must still produce *something*
parseable in that case; CI catches formatting regressions separately.
"""

from __future__ import annotations

from aws_resource_validator.generator.common.logging import get_logger

_logger = get_logger(__name__)

try:
    import black as _black
except ImportError:  # pragma: no cover — formatter degrades gracefully below.
    _black = None  # type: ignore[assignment]


def format_python(source: str, *, line_length: int = 120) -> str:
    """Format Python source with black. Return the original source on failure."""
    if _black is None:
        _logger.warning("black is not installed; emitting unformatted source.")
        return source
    try:
        mode = _black.FileMode(line_length=line_length)
        return _black.format_str(source, mode=mode)
    except Exception as err:  # black raises InvalidInput for unparseable code
        _logger.warning("black failed to format source (%s); emitting unformatted.", err)
        return source
