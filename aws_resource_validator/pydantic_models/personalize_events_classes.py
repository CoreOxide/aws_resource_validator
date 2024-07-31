from datetime import datetime
from pydantic import BaseModel
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

class ActionTypeDef(BaseModel):
    actionId: str
    properties: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class MetricAttributionTypeDef(BaseModel):
    eventAttributionSource: str

class ItemTypeDef(BaseModel):
    itemId: str
    properties: Optional[str] = None

class UserTypeDef(BaseModel):
    userId: str
    properties: Optional[str] = None

class ActionInteractionTypeDef(BaseModel):
    actionId: str
    sessionId: str
    timestamp: TimestampTypeDef
    eventType: str
    userId: Optional[str] = None
    eventId: Optional[str] = None
    recommendationId: Optional[str] = None
    impression: Optional[Sequence[str]] = None
    properties: Optional[str] = None

class PutActionsRequestRequestTypeDef(BaseModel):
    datasetArn: str
    actions: Sequence[ActionTypeDef]

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EventTypeDef(BaseModel):
    eventType: str
    sentAt: TimestampTypeDef
    eventId: Optional[str] = None
    eventValue: Optional[float] = None
    itemId: Optional[str] = None
    properties: Optional[str] = None
    recommendationId: Optional[str] = None
    impression: Optional[Sequence[str]] = None
    metricAttribution: Optional[MetricAttributionTypeDef] = None

class PutItemsRequestRequestTypeDef(BaseModel):
    datasetArn: str
    items: Sequence[ItemTypeDef]

class PutUsersRequestRequestTypeDef(BaseModel):
    datasetArn: str
    users: Sequence[UserTypeDef]

class PutActionInteractionsRequestRequestTypeDef(BaseModel):
    trackingId: str
    actionInteractions: Sequence[ActionInteractionTypeDef]

class PutEventsRequestRequestTypeDef(BaseModel):
    trackingId: str
    sessionId: str
    eventList: Sequence[EventTypeDef]
    userId: Optional[str] = None

