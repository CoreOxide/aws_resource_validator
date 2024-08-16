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
from aws_resource_validator.pydantic_models.codestar_notifications_constants import *

class TargetTypeDef(BaseValidatorModel):
    TargetType: Optional[str] = None
    TargetAddress: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DeleteNotificationRuleRequestRequestTypeDef(BaseValidatorModel):
    Arn: str

class DeleteTargetRequestRequestTypeDef(BaseValidatorModel):
    TargetAddress: str
    ForceUnsubscribeAll: Optional[bool] = None

class DescribeNotificationRuleRequestRequestTypeDef(BaseValidatorModel):
    Arn: str

class EventTypeSummaryTypeDef(BaseValidatorModel):
    EventTypeId: Optional[str] = None
    ServiceName: Optional[str] = None
    EventTypeName: Optional[str] = None
    ResourceType: Optional[str] = None

class TargetSummaryTypeDef(BaseValidatorModel):
    TargetAddress: Optional[str] = None
    TargetType: Optional[str] = None
    TargetStatus: Optional[TargetStatusType] = None

class ListEventTypesFilterTypeDef(BaseValidatorModel):
    Name: ListEventTypesFilterNameType
    Value: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListNotificationRulesFilterTypeDef(BaseValidatorModel):
    Name: ListNotificationRulesFilterNameType
    Value: str

class NotificationRuleSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    Arn: str

class ListTargetsFilterTypeDef(BaseValidatorModel):
    Name: ListTargetsFilterNameType
    Value: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    Tags: Mapping[str, str]

class UnsubscribeRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    TargetAddress: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    TagKeys: Sequence[str]

class CreateNotificationRuleRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    EventTypeIds: Sequence[str]
    Resource: str
    Targets: Sequence[TargetTypeDef]
    DetailType: DetailTypeType
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Status: Optional[NotificationRuleStatusType] = None

class SubscribeRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    Target: TargetTypeDef
    ClientRequestToken: Optional[str] = None

class UpdateNotificationRuleRequestRequestTypeDef(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Status: Optional[NotificationRuleStatusType] = None
    EventTypeIds: Optional[Sequence[str]] = None
    Targets: Optional[Sequence[TargetTypeDef]] = None
    DetailType: Optional[DetailTypeType] = None

class CreateNotificationRuleResultTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteNotificationRuleResultTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SubscribeResultTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceResultTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UnsubscribeResultTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventTypesResultTypeDef(BaseValidatorModel):
    EventTypes: List[EventTypeSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNotificationRuleResultTypeDef(BaseValidatorModel):
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

class ListTargetsResultTypeDef(BaseValidatorModel):
    Targets: List[TargetSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListEventTypesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ListEventTypesFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListEventTypesRequestListEventTypesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ListEventTypesFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNotificationRulesRequestListNotificationRulesPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ListNotificationRulesFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListNotificationRulesRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ListNotificationRulesFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListNotificationRulesResultTypeDef(BaseValidatorModel):
    NextToken: str
    NotificationRules: List[NotificationRuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTargetsRequestListTargetsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ListTargetsFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTargetsRequestRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ListTargetsFilterTypeDef]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

