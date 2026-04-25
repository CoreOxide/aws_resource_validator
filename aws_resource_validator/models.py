"""Deprecated shim.

This module re-exports names from :mod:`aws_resource_validator.core` so that
the committed ``class_definitions.py`` keeps working until the next Pipeline
A regeneration. New code should import from :mod:`aws_resource_validator.core`
directly.
"""

from aws_resource_validator.core import APIObject, APIRegistry, Service

__all__ = ["APIObject", "APIRegistry", "Service"]
