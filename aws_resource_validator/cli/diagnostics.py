"""Detailed diagnostic analysis for AWS resource name validation.

Re-exports core diagnostics functionality for backward compatibility with CLI callers.
"""

from __future__ import annotations

from aws_resource_validator.core.diagnostics import ValidationResult, diagnose_validation

__all__ = [
    "ValidationResult",
    "diagnose_validation",
]
