"""Pre-flight parameter validation wrappers for boto3 and botocore clients and sessions."""

from __future__ import annotations

import logging
import warnings
from collections.abc import Mapping
from contextlib import suppress
from typing import Any, TypeVar

from aws_resource_validator.client_wrapper.exceptions import AWSValidationError, AWSValidationWarning
from aws_resource_validator.client_wrapper.validator import ShapeValidator

_UNIQUE_ID = "aws_resource_validator_preflight"
_CONTEXT_FLAG = "_arv_validated"
_DEFAULT_LOGGER = logging.getLogger("aws_resource_validator.client_wrapper")

T = TypeVar("T")


def _resolve_client_events(target: Any) -> tuple[Any, str]:
    """Extract event emitter and service name from a botocore/boto3 client or resource."""
    # 1. botocore.client.BaseClient
    if hasattr(target, "meta") and hasattr(target.meta, "events"):
        service_name = getattr(getattr(target.meta, "service_model", None), "service_name", "")
        return target.meta.events, service_name

    # 2. boto3 ServiceResource (e.g. boto3.resource('s3'))
    if hasattr(target, "meta") and hasattr(target.meta, "client"):
        client = target.meta.client
        if hasattr(client, "meta") and hasattr(client.meta, "events"):
            service_name = getattr(getattr(client.meta, "service_model", None), "service_name", "")
            return client.meta.events, service_name

    raise TypeError(f"Expected a boto3/botocore client or ServiceResource, got {type(target).__name__}")


def _resolve_session_emitter(session: Any) -> Any:
    """Extract the event emitter from a botocore or boto3 Session."""
    # 1. botocore.session.Session
    if hasattr(session, "get_component"):
        with suppress(Exception):
            return session.get_component("event_emitter")

    # 2. boto3.session.Session (wraps botocore session in ._session)
    if hasattr(session, "_session") and hasattr(session._session, "get_component"):
        with suppress(Exception):
            return session._session.get_component("event_emitter")

    raise TypeError(f"Expected a boto3.Session or botocore.session.Session, got {type(session).__name__}")


def _build_handler(
    default_service_name: str,
    validator: ShapeValidator,
    strict: bool,
    mode: str,
    logger: logging.Logger | None,
) -> Any:
    """Build the pre-flight event handler for before-parameter-build."""

    def _handler(params: dict[str, Any], model: Any, context: dict[str, Any], **kwargs: Any) -> None:
        if context.get(_CONTEXT_FLAG):
            return

        service_name = default_service_name
        if not service_name and hasattr(model, "service_model"):
            service_name = getattr(model.service_model, "service_name", "")

        violations = validator.validate_operation_parameters(
            service_name,
            model,
            params,
            strict=strict,
        )

        if not violations:
            context[_CONTEXT_FLAG] = True
            return

        first_path, first_shape, first_res = violations[0]
        reasons = "; ".join(first_res.errors)
        op_name = getattr(model, "name", "")
        msg = (
            f"Parameter '{first_path}' failed pre-flight validation for {service_name.upper()} "
            f"shape '{first_shape}': Value '{first_res.value}' is invalid. {reasons}"
        )

        if mode == "raise":
            raise AWSValidationError(
                msg,
                service_name=service_name,
                operation_name=op_name,
                param_name=first_path,
                shape_name=first_shape,
                value=first_res.value,
                diagnostics=first_res.errors,
                validation_result=first_res,
            )
        elif mode == "warn":
            warnings.warn(msg, category=AWSValidationWarning, stacklevel=3)
        elif mode == "log":
            log = logger or _DEFAULT_LOGGER
            log.warning(msg)
        else:
            raise ValueError(f"Invalid validation mode: {mode!r}. Must be 'raise', 'warn', or 'log'.")

        context[_CONTEXT_FLAG] = True

    return _handler


def wrap_client(
    client: T,
    *,
    strict: bool = True,
    mode: str = "raise",
    custom_rules: Mapping[Any, Any] | None = None,
    logger: logging.Logger | None = None,
) -> T:
    """Wrap a boto3 or botocore client with pre-flight parameter validation.

    Intercepts API calls locally in memory (< 0.2ms) before making HTTP network
    requests to AWS. Validates parameter shape constraints, length limits,
    regex patterns, and nested structures.

    Parameters:
        client: A boto3 or botocore client instance (or boto3 ServiceResource).
        strict: When True, requires full-string regex match (default). When False,
            mirrors botocore prefix-only matching semantics.
        mode: How to handle validation violations:
            - ``"raise"`` (default): raises :class:`AWSValidationError`.
            - ``"warn"``: emits :class:`AWSValidationWarning`.
            - ``"log"``: logs a warning to the configured logger.
        custom_rules: Optional dictionary mapping ``(service, shape)`` or shape name
            to custom :class:`~aws_resource_validator.core.api_object.APIObject` rules.
        logger: Optional logger for ``mode="log"``. Defaults to package logger.

    Returns:
        The same client instance with the validation hook registered.
    """
    events, service_name = _resolve_client_events(client)
    validator = ShapeValidator(custom_rules=custom_rules)
    handler = _build_handler(service_name, validator, strict, mode, logger)

    events.register(
        "before-parameter-build.*.*",
        handler,
        unique_id=_UNIQUE_ID,
    )
    return client


def unwrap_client(client: T) -> T:
    """Remove pre-flight validation hook from a wrapped client."""
    events, _ = _resolve_client_events(client)
    events.unregister(
        "before-parameter-build.*.*",
        unique_id=_UNIQUE_ID,
    )
    return client


def wrap_session(
    session: T,
    *,
    strict: bool = True,
    mode: str = "raise",
    custom_rules: Mapping[Any, Any] | None = None,
    logger: logging.Logger | None = None,
) -> T:
    """Wrap a boto3 or botocore Session so all clients created inherit pre-flight validation.

    Parameters:
        session: A :class:`boto3.Session` or :class:`botocore.session.Session`.
        strict: When True (default), enforces end-to-end regex match.
        mode: ``"raise"``, ``"warn"``, or ``"log"``.
        custom_rules: Optional custom shape rules mapping.
        logger: Optional logger for ``mode="log"``.

    Returns:
        The session instance with validation enabled across all child clients.
    """
    emitter = _resolve_session_emitter(session)
    validator = ShapeValidator(custom_rules=custom_rules)
    handler = _build_handler("", validator, strict, mode, logger)

    emitter.register(
        "before-parameter-build.*.*",
        handler,
        unique_id=_UNIQUE_ID,
    )
    return session


def unwrap_session(session: T) -> T:
    """Remove pre-flight validation hook from a wrapped session."""
    emitter = _resolve_session_emitter(session)
    emitter.unregister(
        "before-parameter-build.*.*",
        unique_id=_UNIQUE_ID,
    )
    return session
