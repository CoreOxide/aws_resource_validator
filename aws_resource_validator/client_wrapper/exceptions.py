"""Exception classes for pre-flight boto3 client parameter validation."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

try:
    from botocore.exceptions import ParamValidationError
except ImportError:  # pragma: no cover
    ParamValidationError = Exception  # type: ignore[misc,assignment]

if TYPE_CHECKING:
    from aws_resource_validator.core.diagnostics import ValidationResult


class AWSValidationError(ValueError, ParamValidationError):
    """Raised when an AWS client parameter violates shape constraints during pre-flight check.

    Inherits from both :class:`ValueError` and botocore's :class:`ParamValidationError`
    so callers catching either standard error type will catch this exception.
    """

    def __init__(
        self,
        message: str,
        *,
        service_name: str = "",
        operation_name: str = "",
        param_name: str = "",
        shape_name: str = "",
        value: Any = None,
        diagnostics: list[str] | None = None,
        validation_result: ValidationResult | None = None,
        suggested_fix: str | None = None,
        visual_pointer: str | None = None,
    ) -> None:
        self.message = message
        self.service_name = service_name
        self.operation_name = operation_name
        self.param_name = param_name
        self.shape_name = shape_name
        self.value = value
        self.validation_result = validation_result
        self.suggested_fix = suggested_fix or (validation_result.suggested_fix if validation_result else None)
        self.visual_pointer = visual_pointer or (validation_result.visual_pointer if validation_result else None)
        self.diagnostics = (
            diagnostics if diagnostics is not None else (validation_result.diagnostics if validation_result else [])
        )
        ValueError.__init__(self, message)
        ParamValidationError.__init__(self, report=message)

    def __str__(self) -> str:
        return self.message

    def __repr__(self) -> str:
        return (
            f"AWSValidationError({self.message!r}, service={self.service_name!r}, "
            f"operation={self.operation_name!r}, param={self.param_name!r})"
        )


class AWSValidationWarning(UserWarning):
    """Emitted when an AWS client parameter violates shape constraints in warn mode."""
