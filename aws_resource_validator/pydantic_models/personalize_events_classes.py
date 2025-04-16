from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.personalize_events_constants import *

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


class Timestamp(BaseValidatorModel):
    pass


class ActionInteraction(BaseValidatorModel):
    actionId: str
    sessionId: str
    timestamp: Timestamp
    eventType: str
    userId: Optional[str] = None
    eventId: Optional[str] = None
    recommendationId: Optional[str] = None
    impression: Optional[Sequence[str]] = None
    properties: Optional[str] = None


class PutActionsRequest(BaseValidatorModel):
    datasetArn: str
    actions: Sequence[Action]


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
    impression: Optional[Sequence[str]] = None
    metricAttribution: Optional[MetricAttribution] = None


class PutItemsRequest(BaseValidatorModel):
    datasetArn: str
    items: Sequence[Item]


class PutUsersRequest(BaseValidatorModel):
    datasetArn: str
    users: Sequence[User]


class PutActionInteractionsRequest(BaseValidatorModel):
    trackingId: str
    actionInteractions: Sequence[ActionInteraction]


class PutEventsRequest(BaseValidatorModel):
    trackingId: str
    sessionId: str
    eventList: Sequence[Event]
    userId: Optional[str] = None


