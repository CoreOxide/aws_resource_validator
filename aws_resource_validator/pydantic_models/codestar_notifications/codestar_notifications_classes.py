from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.codestar_notifications.codestar_notifications_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Target(BaseValidatorModel):
    TargetType: Optional[str] = None
    TargetAddress: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'delete_notification_rule' function.
class DeleteNotificationRuleRequest(BaseValidatorModel):
    Arn: str


class DeleteTargetRequest(BaseValidatorModel):
    TargetAddress: str
    ForceUnsubscribeAll: Optional[bool] = None


# This class is the input for the 'describe_notification_rule' function.
class DescribeNotificationRuleRequest(BaseValidatorModel):
    Arn: str


class EventTypeSummary(BaseValidatorModel):
    EventTypeId: Optional[str] = None
    ServiceName: Optional[str] = None
    EventTypeName: Optional[str] = None
    ResourceType: Optional[str] = None


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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    Arn: str


class ListTargetsFilter(BaseValidatorModel):
    Name: ListTargetsFilterNameType
    Value: str


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    Arn: str
    Tags: Dict[str, str]


# This class is the input for the 'unsubscribe' function.
class UnsubscribeRequest(BaseValidatorModel):
    Arn: str
    TargetAddress: str


class UntagResourceRequest(BaseValidatorModel):
    Arn: str
    TagKeys: List[str]


# This class is the input for the 'create_notification_rule' function.
class CreateNotificationRuleRequest(BaseValidatorModel):
    Name: str
    EventTypeIds: List[str]
    Resource: str
    Targets: List[Target]
    DetailType: DetailTypeType
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    Status: Optional[NotificationRuleStatusType] = None


# This class is the input for the 'subscribe' function.
class SubscribeRequest(BaseValidatorModel):
    Arn: str
    Target: Target
    ClientRequestToken: Optional[str] = None


class UpdateNotificationRuleRequest(BaseValidatorModel):
    Arn: str
    Name: Optional[str] = None
    Status: Optional[NotificationRuleStatusType] = None
    EventTypeIds: Optional[List[str]] = None
    Targets: Optional[List[Target]] = None
    DetailType: Optional[DetailTypeType] = None


# This class is the output for the 'create_notification_rule' function.
class CreateNotificationRuleResult(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_notification_rule' function.
class DeleteNotificationRuleResult(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResult(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'subscribe' function.
class SubscribeResult(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'tag_resource' function.
class TagResourceResult(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'unsubscribe' function.
class UnsubscribeResult(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_event_types' function.
class ListEventTypesResult(BaseValidatorModel):
    EventTypes: List[EventTypeSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_notification_rule' function.
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


# This class is the output for the 'list_targets' function.
class ListTargetsResult(BaseValidatorModel):
    Targets: List[TargetSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'list_event_types' function.
class ListEventTypesRequest(BaseValidatorModel):
    Filters: Optional[List[ListEventTypesFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListEventTypesRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[ListEventTypesFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListNotificationRulesRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[ListNotificationRulesFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_notification_rules' function.
class ListNotificationRulesRequest(BaseValidatorModel):
    Filters: Optional[List[ListNotificationRulesFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'list_notification_rules' function.
class ListNotificationRulesResult(BaseValidatorModel):
    NotificationRules: List[NotificationRuleSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTargetsRequestPaginate(BaseValidatorModel):
    Filters: Optional[List[ListTargetsFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_targets' function.
class ListTargetsRequest(BaseValidatorModel):
    Filters: Optional[List[ListTargetsFilter]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None