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
from aws_resource_validator.pydantic_models.codestar_notifications_constants import *

class TargetTypeDef(BaseModel):
    TargetType: Optional[str] = None
    TargetAddress: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteNotificationRuleRequestRequestTypeDef(BaseModel):
    Arn: str

class DeleteTargetRequestRequestTypeDef(BaseModel):
    TargetAddress: str
    ForceUnsubscribeAll: Optional[bool] = None

class DescribeNotificationRuleRequestRequestTypeDef(BaseModel):
    Arn: str

class EventTypeSummaryTypeDef(BaseModel):
    EventTypeId: Optional[str] = None
    ServiceName: Optional[str] = None
    EventTypeName: Optional[str] = None
    ResourceType: Optional[str] = None

class TargetSummaryTypeDef(BaseModel):
    TargetAddress: Optional[str] = None
    TargetType: Optional[str] = None
    TargetStatus: Optional[TargetStatusType] = None

class ListEventTypesFilterTypeDef(BaseModel):
    Name: ListEventTypesFilterNameType
    Value: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListNotificationRulesFilterTypeDef(BaseModel):
    Name: ListNotificationRulesFilterNameType
    Value: str

class NotificationRuleSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    Arn: str

class ListTargetsFilterTypeDef(BaseModel):
    Name: ListTargetsFilterNameType
    Value: str

class TagResourceRequestRequestTypeDef(BaseModel):
    Arn: str
    Tags: Mapping[str, str]

class UnsubscribeRequestRequestTypeDef(BaseModel):
    Arn: str
    TargetAddress: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    Arn: str
    TagKeys: Sequence[str]

class CreateNotificationRuleRequestRequestTypeDef(BaseModel):
    Name: str
    EventTypeIds: Sequence[str]
    Resource: str
    Targets: Sequence[TargetTypeDef]
    DetailType: DetailTypeType
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Status: Optional[NotificationRuleStatusType] = None

class SubscribeRequestRequestTypeDef(BaseModel):
    Arn: str
    Target: TargetTypeDef
    ClientRequestToken: Optional[str] = None

class UpdateNotificationRuleRequestRequestTypeDef(BaseModel):
    Arn: str
    Name: Optional[str] = None
    Status: Optional[NotificationRuleStatusType] = None
    EventTypeIds: Optional[Sequence[str]] = None
    Targets: Optional[Sequence[TargetTypeDef]] = None
    DetailType: Optional[DetailTypeType] = None

class CreateNotificationRuleResultTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNotificationRuleResultTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SubscribeResultTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceResultTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UnsubscribeResultTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventTypesResultTypeDef(BaseModel):
    EventTypes: List[EventTypeSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNotificationRuleResultTypeDef(BaseModel):
    Arn: str
    Name: str
    EventTypes: List[EventTypeSummaryTypeDef]
    Resource: str
    Targets: List[TargetSummaryTypeDef]
    DetailType: DetailTypeType
    CreatedBy: str
    Status: NotificationRuleStatusType
    CreatedTimestamp: datetime
    LastModifiedTimestamp: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetsResultTypeDef(BaseModel):
    Targets: List[TargetSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventTypesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[ListEventTypesFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEventTypesRequestListEventTypesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[ListEventTypesFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNotificationRulesRequestListNotificationRulesPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[ListNotificationRulesFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNotificationRulesRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[ListNotificationRulesFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListNotificationRulesResultTypeDef(BaseModel):
    NextToken: str
    NotificationRules: List[NotificationRuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetsRequestListTargetsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[ListTargetsFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetsRequestRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[ListTargetsFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

