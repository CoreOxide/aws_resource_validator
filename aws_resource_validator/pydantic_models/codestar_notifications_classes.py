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
from aws_resource_validator.pydantic_models.codestar_notifications_constants import *

class Target(BaseValidatorModel):
    TargetType: Optional[str] = None
    TargetAddress: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteNotificationRuleRequest(BaseValidatorModel):
    Arn: str


class DeleteTargetRequest(BaseValidatorModel):
    TargetAddress: str
    ForceUnsubscribeAll: Optional[bool] = None


class DescribeNotificationRuleRequest(BaseValidatorModel):
    Arn: str


class TargetSummary(BaseValidatorModel):
    TargetAddress: Optional[str] = None
    TargetType: Optional[str] = None
    TargetStatus: Optional[TargetStatusType] = None


class ListEventTypesFilter(BaseValidatorModel):
    Name: ListEventTypesFilterNameType
    Value: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListNotificationRulesFilter(BaseValidatorModel):
    Name: ListNotificationRulesFilterNameType
    Value: str


class NotificationRuleSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    Arn: str


class ListTargetsFilter(BaseValidatorModel):
    Name: ListTargetsFilterNameType
    Value: str


class TagResourceRequest(BaseValidatorModel):
    Arn: str
    Tags: Mapping[str, str]


class UnsubscribeRequest(BaseValidatorModel):
    Arn: str
    TargetAddress: str


class UntagResourceRequest(BaseValidatorModel):
    Arn: str
    TagKeys: Sequence[str]


class CreateNotificationRuleRequest(BaseValidatorModel):
    Name: str
    EventTypeIds: Sequence[str]
    Resource: str
    Targets: Sequence[Target]
    DetailType: DetailTypeType
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Status: Optional[NotificationRuleStatusType] = None


class SubscribeRequest(BaseValidatorModel):
    Arn: str
    Target: Target
    ClientRequestToken: Optional[str] = None


class UpdateNotificationRuleRequest(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Status: Optional[NotificationRuleStatusType] = None
    EventTypeIds: Optional[Sequence[str]] = None
    Targets: Optional[Sequence[Target]] = None
    DetailType: Optional[DetailTypeType] = None


class CreateNotificationRuleResult(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class DeleteNotificationRuleResult(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResult(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class SubscribeResult(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class TagResourceResult(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UnsubscribeResult(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class EventTypeSummary(BaseValidatorModel):
    pass


class ListEventTypesResult(BaseValidatorModel):
    EventTypes: List[EventTypeSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeNotificationRuleResult(BaseValidatorModel):
    Arn: str
    Name: str
    EventTypes: List[EventTypeSummary]
    Resource: str
    Targets: List[TargetSummary]
    DetailType: DetailTypeType
    CreatedBy: str
    Status: NotificationRuleStatusType
    CreatedTimestamp: datetime
    LastModifiedTimestamp: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListTargetsResult(BaseValidatorModel):
    Targets: List[TargetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEventTypesRequest(BaseValidatorModel):
    Filters: Optional[Sequence[ListEventTypesFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventTypesRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[ListEventTypesFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNotificationRulesRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[ListNotificationRulesFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNotificationRulesRequest(BaseValidatorModel):
    Filters: Optional[Sequence[ListNotificationRulesFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListNotificationRulesResult(BaseValidatorModel):
    NotificationRules: List[NotificationRuleSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTargetsRequestPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[ListTargetsFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTargetsRequest(BaseValidatorModel):
    Filters: Optional[Sequence[ListTargetsFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


