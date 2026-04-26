"""Shared Pydantic base model and EventStream wrapper used by every generated service module."""

from __future__ import annotations

from typing import Generic, TypeVar

from botocore.eventstream import EventStream as BaseEventStream
from pydantic import BaseModel, ConfigDict

T = TypeVar("T")


class BaseValidatorModel(BaseModel):
    """Base Pydantic model with botocore-friendly defaults.

    * ``arbitrary_types_allowed``: botocore returns opaque types like
      :class:`~botocore.response.StreamingBody`; Pydantic must accept them
      without schema introspection.
    * ``extra="allow"``: AWS APIs add fields over time; accepting unknown
      keys keeps models forward-compatible with new boto3 releases.
      Consequence: unknown keys are silently preserved rather than rejected —
      strict callers should validate against the explicit field list.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="allow")


class EventStream(BaseEventStream, Generic[T]):
    """Generic wrapper making :class:`botocore.eventstream.EventStream` subscriptable.

    Pydantic's schema generator requires annotated generics; the bare botocore
    class is not parameterized, so we expose a :class:`~typing.Generic` shim
    whose type parameter is the event union produced by each AWS operation.
    """
