from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class ActionTypeDef(BaseValidatorModel):
    actionId: str
    properties: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class MetricAttributionTypeDef(BaseValidatorModel):
    eventAttributionSource: str

class ItemTypeDef(BaseValidatorModel):
    itemId: str
    properties: Optional[str] = None

class UserTypeDef(BaseValidatorModel):
    userId: str
    properties: Optional[str] = None

class ActionInteractionTypeDef(BaseValidatorModel):
    actionId: str
    sessionId: str
    timestamp: TimestampTypeDef
    eventType: str
    userId: Optional[str] = None
    eventId: Optional[str] = None
    recommendationId: Optional[str] = None
    impression: Optional[Sequence[str]] = None
    properties: Optional[str] = None

class PutActionsRequestRequestTypeDef(BaseValidatorModel):
    datasetArn: str
    actions: Sequence[ActionTypeDef]

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EventTypeDef(BaseValidatorModel):
    eventType: str
    sentAt: TimestampTypeDef
    eventId: Optional[str] = None
    eventValue: Optional[float] = None
    itemId: Optional[str] = None
    properties: Optional[str] = None
    recommendationId: Optional[str] = None
    impression: Optional[Sequence[str]] = None
    metricAttribution: Optional[MetricAttributionTypeDef] = None

class PutItemsRequestRequestTypeDef(BaseValidatorModel):
    datasetArn: str
    items: Sequence[ItemTypeDef]

class PutUsersRequestRequestTypeDef(BaseValidatorModel):
    datasetArn: str
    users: Sequence[UserTypeDef]

class PutActionInteractionsRequestRequestTypeDef(BaseValidatorModel):
    trackingId: str
    actionInteractions: Sequence[ActionInteractionTypeDef]

class PutEventsRequestRequestTypeDef(BaseValidatorModel):
    trackingId: str
    sessionId: str
    eventList: Sequence[EventTypeDef]
    userId: Optional[str] = None

