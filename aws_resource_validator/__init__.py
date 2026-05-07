"""Public API for the aws_resource_validator runtime.

Generated artifacts live under :mod:`aws_resource_validator.class_definitions`
(single-file Pipeline A output) and :mod:`aws_resource_validator.pydantic_models`
(Pipeline B output, one sub-package per AWS service). The generator itself
lives under :mod:`aws_resource_validator.generator` and is not part of the
runtime surface.
"""

from aws_resource_validator.core import (
    APIObject,
    APIRegistry,
    BaseValidatorModel,
    EventStream,
    Service,
)

__all__ = [
    "APIObject",
    "APIRegistry",
    "BaseValidatorModel",
    "EventStream",
    "Service",
]

__version__ = "2.0.3"
