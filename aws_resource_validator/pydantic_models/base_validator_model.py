from pydantic import BaseModel
from botocore.eventstream import EventStream as BaseEventStream
from typing import Generic, TypeVar


class BaseValidatorModel(BaseModel):
    class Config:
        arbitrary_types_allowed = True
        exclude_none = True


T = TypeVar("T")
class EventStream(BaseEventStream, Generic[T]):
    """
    Generic wrapper around the original EventStream
    so that Pydantic sees it as subscriptable (EventStream[T]).
    """
    pass
