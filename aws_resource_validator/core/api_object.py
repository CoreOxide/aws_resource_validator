"""Value type representing a single AWS shape with a regex pattern constraint."""

from __future__ import annotations

import re
from dataclasses import dataclass

import exrex

# Ceiling for exrex when the shape declares no max — botocore's own patterns
# never exceed a few kilobytes, and ``exrex.getone`` requires a finite limit
# to terminate on unbounded quantifiers like ``.+``.
_DEFAULT_GENERATE_LIMIT = 2048


@dataclass(frozen=True, slots=True)
class APIObject:
    """A single AWS API shape with a regex-based validation contract.

    Instances are produced by :mod:`aws_resource_validator.generator.pipeline_a`
    from ``service-2.json`` shape definitions that declare both a ``type`` and
    a ``pattern``. They are the leaves of :class:`~.Service`.

    Attributes:
        name: The shape name as it appears in the botocore definition.
        type: The botocore shape type (typically ``"string"``).
        pattern: A Python-compatible regular expression the value must match.
        min_length: Optional lower bound on the value length.
        max_length: Optional upper bound on the value length.
    """

    name: str
    type: str
    pattern: str
    min_length: int | None = None
    max_length: int | None = None

    def validate(self, value: str) -> bool:
        """Return ``True`` iff ``value`` is within length bounds and matches :attr:`pattern`.

        Uses :func:`re.match` semantics: the match is anchored at the start
        only, mirroring botocore's own validation (it does not anchor at end).
        """
        if self.min_length is not None and len(value) < self.min_length:
            return False
        if self.max_length is not None and len(value) > self.max_length:
            return False
        return re.match(self.pattern, value) is not None

    def generate(self) -> str:
        """Produce a single example value that satisfies :attr:`pattern`.

        Bounds exrex by :attr:`max_length` when set, otherwise by a sane
        default, so unbounded quantifiers like ``.+`` always terminate.
        """
        limit = self.max_length if self.max_length is not None else _DEFAULT_GENERATE_LIMIT
        result: str = exrex.getone(self.pattern, limit=limit)
        return result
