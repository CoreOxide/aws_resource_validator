from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.personalize_events.personalize_events_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream



Timestamp = Union[datetime, str]


class Action(BaseValidatorModel):
    actionId: str
    properties: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class MetricAttribution(BaseValidatorModel):
    eventAttributionSource: str


class Item(BaseValidatorModel):
    itemId: str
    properties: Optional[str] = None


class User(BaseValidatorModel):
    userId: str
    properties: Optional[str] = None


class ActionInteraction(BaseValidatorModel):
    actionId: str
    sessionId: str
    timestamp: Timestamp
    eventType: str
    userId: Optional[str] = None
    eventId: Optional[str] = None
    recommendationId: Optional[str] = None
    impression: Optional[List[str]] = None
    properties: Optional[str] = None


# This class is the input for the 'put_actions' function.
class PutActionsRequest(BaseValidatorModel):
    datasetArn: str
    actions: List[Action]


# This class is the output for the 'put_users' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class Event(BaseValidatorModel):
    eventType: str
    sentAt: Timestamp
    eventId: Optional[str] = None
    eventValue: Optional[float] = None
    itemId: Optional[str] = None
    properties: Optional[str] = None
    recommendationId: Optional[str] = None
    impression: Optional[List[str]] = None
    metricAttribution: Optional[MetricAttribution] = None


# This class is the input for the 'put_items' function.
class PutItemsRequest(BaseValidatorModel):
    datasetArn: str
    items: List[Item]


# This class is the input for the 'put_users' function.
class PutUsersRequest(BaseValidatorModel):
    datasetArn: str
    users: List[User]


# This class is the input for the 'put_action_interactions' function.
class PutActionInteractionsRequest(BaseValidatorModel):
    trackingId: str
    actionInteractions: List[ActionInteraction]


# This class is the input for the 'put_events' function.
class PutEventsRequest(BaseValidatorModel):
    trackingId: str
    sessionId: str
    eventList: List[Event]
    userId: Optional[str] = None