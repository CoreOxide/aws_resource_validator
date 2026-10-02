"""Pre-flight parameter validation against botocore shape models."""

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any

from aws_resource_validator.client_wrapper.rules import get_extra_validator, get_shape_rule
from aws_resource_validator.core.api_object import APIObject
from aws_resource_validator.core.diagnostics import ValidationResult, diagnose_validation
from aws_resource_validator.core.resolver import resolve_service, resolve_shape

if TYPE_CHECKING:
    from botocore.model import OperationModel, Shape


class ShapeValidator:
    """Validates operation parameters against AWS shape constraints and regex patterns."""

    def __init__(self, custom_rules: Mapping[Any, Any] | None = None) -> None:
        self.custom_rules = custom_rules
        self._shape_cache: dict[tuple[str, str, str | None], APIObject | None] = {}

    def _resolve_from_registry(
        self,
        service_name: str,
        shape_name: str,
        param_name: str | None,
    ) -> APIObject | None:
        service_obj, _ = resolve_service(service_name)
        if service_obj is None:
            return None
        obj, _ = resolve_shape(service_obj, shape_name)
        if obj is not None:
            return obj
        if param_name:
            obj, _ = resolve_shape(service_obj, param_name)
            return obj
        return None

    def _resolve_from_metadata(self, shape: Shape) -> APIObject | None:
        metadata = getattr(shape, "metadata", {})
        pattern = metadata.get("pattern")
        min_length = metadata.get("min")
        max_length = metadata.get("max")
        if pattern is not None:
            return APIObject(
                name=shape.name,
                type=getattr(shape, "type_name", "string"),
                pattern=pattern,
                min_length=min_length,
                max_length=max_length,
            )
        if min_length is not None or max_length is not None:
            return APIObject(
                name=shape.name,
                type=getattr(shape, "type_name", "string"),
                pattern=".*",
                min_length=min_length,
                max_length=max_length,
            )
        return None

    def resolve_api_object(
        self,
        service_name: str,
        shape: Shape,
        param_name: str | None = None,
    ) -> APIObject | None:
        """Resolve the APIObject constraint for a shape and parameter."""
        cache_key = (service_name.lower(), shape.name, param_name)
        if cache_key in self._shape_cache:
            return self._shape_cache[cache_key]

        api_obj = (
            get_shape_rule(service_name, shape.name, param_name, self.custom_rules)
            or self._resolve_from_registry(service_name, shape.name, param_name)
            or self._resolve_from_metadata(shape)
        )
        self._shape_cache[cache_key] = api_obj
        return api_obj

    def _traverse_structure(
        self,
        service_name: str,
        value: dict[str, Any],
        shape: Shape,
        path: str,
        *,
        strict: bool,
        violations: list[tuple[str, str, ValidationResult]],
    ) -> None:
        members = getattr(shape, "members", {})
        for field_name, field_value in value.items():
            if field_name in members:
                next_path = f"{path}.{field_name}" if path else field_name
                self._validate_node(
                    service_name,
                    field_value,
                    members[field_name],
                    next_path,
                    field_name,
                    strict=strict,
                    violations=violations,
                )

    def _traverse_list(
        self,
        service_name: str,
        value: list[Any] | tuple[Any, ...],
        shape: Shape,
        path: str,
        param_name: str | None,
        *,
        strict: bool,
        violations: list[tuple[str, str, ValidationResult]],
    ) -> None:
        member_shape = getattr(shape, "member", None)
        if member_shape is not None:
            for idx, item in enumerate(value):
                self._validate_node(
                    service_name,
                    item,
                    member_shape,
                    f"{path}[{idx}]",
                    param_name,
                    strict=strict,
                    violations=violations,
                )

    def _traverse_map(
        self,
        service_name: str,
        value: dict[str, Any],
        shape: Shape,
        path: str,
        param_name: str | None,
        *,
        strict: bool,
        violations: list[tuple[str, str, ValidationResult]],
    ) -> None:
        key_shape = getattr(shape, "key", None)
        val_shape = getattr(shape, "value", None)
        for k, v in value.items():
            if key_shape is not None and isinstance(k, str):
                self._validate_node(
                    service_name,
                    k,
                    key_shape,
                    f"{path}.key({k})",
                    str(k),
                    strict=strict,
                    violations=violations,
                )
            if val_shape is not None:
                self._validate_node(
                    service_name,
                    v,
                    val_shape,
                    f"{path}[{k}]",
                    param_name,
                    strict=strict,
                    violations=violations,
                )

    def _validate_string(
        self,
        service_name: str,
        value: str,
        shape: Shape,
        path: str,
        param_name: str | None,
        *,
        strict: bool,
        violations: list[tuple[str, str, ValidationResult]],
    ) -> None:
        api_obj = self.resolve_api_object(service_name, shape, param_name)
        if api_obj is None:
            return

        res = diagnose_validation(api_obj, service_name, value, strict=strict)

        extra_validator = get_extra_validator(service_name, shape.name, param_name)
        if extra_validator is not None:
            extra_errs = extra_validator(value)
            if extra_errs:
                all_errs = list(res.errors) + extra_errs
                res = ValidationResult(
                    is_valid=False,
                    value=res.value,
                    service_name=res.service_name,
                    shape_name=res.shape_name,
                    pattern=res.pattern,
                    min_length=res.min_length,
                    max_length=res.max_length,
                    length=res.length,
                    errors=all_errs,
                    warnings=res.warnings,
                    strict=res.strict,
                    prefix_matched=res.prefix_matched,
                    full_matched=res.full_matched,
                )

        if not res.is_valid:
            violations.append((path, shape.name, res))

    def _validate_node(
        self,
        service_name: str,
        value: Any,
        shape: Shape,
        path: str,
        param_name: str | None,
        *,
        strict: bool,
        violations: list[tuple[str, str, ValidationResult]],
    ) -> None:
        if value is None:
            return

        type_name = getattr(shape, "type_name", "")
        if type_name == "structure" and isinstance(value, dict):
            self._traverse_structure(service_name, value, shape, path, strict=strict, violations=violations)
        elif type_name == "list" and isinstance(value, (list, tuple)):
            self._traverse_list(service_name, value, shape, path, param_name, strict=strict, violations=violations)
        elif type_name == "map" and isinstance(value, dict):
            self._traverse_map(service_name, value, shape, path, param_name, strict=strict, violations=violations)
        elif type_name == "string" and isinstance(value, str):
            self._validate_string(service_name, value, shape, path, param_name, strict=strict, violations=violations)

    def validate_operation_parameters(
        self,
        service_name: str,
        operation_model: OperationModel,
        params: dict[str, Any],
        *,
        strict: bool = False,
    ) -> list[tuple[str, str, ValidationResult]]:
        """Traverse parameters and validate against operation input shapes.

        Returns a list of ``(param_path, shape_name, validation_result)``
        for all failed constraints.
        """
        input_shape = getattr(operation_model, "input_shape", None)
        if input_shape is None or not params:
            return []

        violations: list[tuple[str, str, ValidationResult]] = []
        members = getattr(input_shape, "members", {})
        for param_k, param_v in params.items():
            if param_k in members:
                self._validate_node(
                    service_name,
                    param_v,
                    members[param_k],
                    param_k,
                    param_k,
                    strict=strict,
                    violations=violations,
                )

        return violations
