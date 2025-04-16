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
from aws_resource_validator.pydantic_models.resource_groups_constants import *

class AccountSettings(BaseValidatorModel):
    GroupLifecycleEventsDesiredStatus: Optional[GroupLifecycleEventsDesiredStatusType] = None
    GroupLifecycleEventsStatus: Optional[GroupLifecycleEventsStatusType] = None
    GroupLifecycleEventsStatusMessage: Optional[str] = None


class CancelTagSyncTaskInput(BaseValidatorModel):
    TaskArn: str


class Group(BaseValidatorModel):
    GroupArn: str
    Name: str
    Description: Optional[str] = None
    Criticality: Optional[int] = None
    Owner: Optional[str] = None
    DisplayName: Optional[str] = None
    ApplicationTag: Optional[Dict[str, str]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteGroupInput(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None


class FailedResource(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None


class GetGroupConfigurationInput(BaseValidatorModel):
    Group: Optional[str] = None


class GetGroupInput(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None


class GetGroupQueryInput(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None


class GetTagSyncTaskInput(BaseValidatorModel):
    TaskArn: str


class GetTagsInput(BaseValidatorModel):
    Arn: str


class GroupConfigurationParameterOutput(BaseValidatorModel):
    Name: str
    Values: Optional[List[str]] = None


class GroupConfigurationParameter(BaseValidatorModel):
    Name: str
    Values: Optional[Sequence[str]] = None


class GroupFilter(BaseValidatorModel):
    Name: GroupFilterNameType
    Values: Sequence[str]


class GroupIdentifier(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupArn: Optional[str] = None
    Description: Optional[str] = None
    Criticality: Optional[int] = None
    Owner: Optional[str] = None
    DisplayName: Optional[str] = None


class GroupResourcesInput(BaseValidatorModel):
    Group: str
    ResourceArns: Sequence[str]


class PendingResource(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class GroupingStatusesItem(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Action: Optional[GroupingTypeType] = None
    Status: Optional[GroupingStatusType] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None
    UpdatedAt: Optional[datetime] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ResourceFilter(BaseValidatorModel):
    Name: Literal["resource-type"]
    Values: Sequence[str]


class ResourceIdentifier(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None


class ResourceStatus(BaseValidatorModel):
    Name: Optional[Literal["PENDING"]] = None


class QueryError(BaseValidatorModel):
    ErrorCode: Optional[QueryErrorCodeType] = None
    Message: Optional[str] = None


class ListGroupingStatusesFilter(BaseValidatorModel):
    Name: ListGroupingStatusesFilterNameType
    Values: Sequence[str]


class ListTagSyncTasksFilter(BaseValidatorModel):
    GroupArn: Optional[str] = None
    GroupName: Optional[str] = None


class TagSyncTaskItem(BaseValidatorModel):
    GroupArn: Optional[str] = None
    GroupName: Optional[str] = None
    TaskArn: Optional[str] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    RoleArn: Optional[str] = None
    Status: Optional[TagSyncTaskStatusType] = None
    ErrorMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None


class StartTagSyncTaskInput(BaseValidatorModel):
    Group: str
    TagKey: str
    TagValue: str
    RoleArn: str


class TagInput(BaseValidatorModel):
    Arn: str
    Tags: Mapping[str, str]


class UngroupResourcesInput(BaseValidatorModel):
    Group: str
    ResourceArns: Sequence[str]


class UntagInput(BaseValidatorModel):
    Arn: str
    Keys: Sequence[str]


class UpdateAccountSettingsInput(BaseValidatorModel):
    GroupLifecycleEventsDesiredStatus: Optional[GroupLifecycleEventsDesiredStatusType] = None


class UpdateGroupInput(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Description: Optional[str] = None
    Criticality: Optional[int] = None
    Owner: Optional[str] = None
    DisplayName: Optional[str] = None


class ResourceQuery(BaseValidatorModel):
    pass


class GroupQuery(BaseValidatorModel):
    GroupName: str
    ResourceQuery: ResourceQuery


class SearchResourcesInput(BaseValidatorModel):
    ResourceQuery: ResourceQuery
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class UpdateGroupQueryInput(BaseValidatorModel):
    ResourceQuery: ResourceQuery
    GroupName: Optional[str] = None
    Group: Optional[str] = None


class DeleteGroupOutput(BaseValidatorModel):
    Group: Group
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAccountSettingsOutput(BaseValidatorModel):
    AccountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


class GetGroupOutput(BaseValidatorModel):
    Group: Group
    ResponseMetadata: ResponseMetadata


class GetTagSyncTaskOutput(BaseValidatorModel):
    GroupArn: str
    GroupName: str
    TaskArn: str
    TagKey: str
    TagValue: str
    RoleArn: str
    Status: TagSyncTaskStatusType
    ErrorMessage: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadata


class GetTagsOutput(BaseValidatorModel):
    Arn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class StartTagSyncTaskOutput(BaseValidatorModel):
    GroupArn: str
    GroupName: str
    TaskArn: str
    TagKey: str
    TagValue: str
    RoleArn: str
    ResponseMetadata: ResponseMetadata


class TagOutput(BaseValidatorModel):
    Arn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UntagOutput(BaseValidatorModel):
    Arn: str
    Keys: List[str]
    ResponseMetadata: ResponseMetadata


class UpdateAccountSettingsOutput(BaseValidatorModel):
    AccountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


class UpdateGroupOutput(BaseValidatorModel):
    Group: Group
    ResponseMetadata: ResponseMetadata


class ListGroupsInput(BaseValidatorModel):
    Filters: Optional[Sequence[GroupFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListGroupsOutput(BaseValidatorModel):
    GroupIdentifiers: List[GroupIdentifier]
    Groups: List[Group]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GroupResourcesOutput(BaseValidatorModel):
    Succeeded: List[str]
    Failed: List[FailedResource]
    Pending: List[PendingResource]
    ResponseMetadata: ResponseMetadata


class UngroupResourcesOutput(BaseValidatorModel):
    Succeeded: List[str]
    Failed: List[FailedResource]
    Pending: List[PendingResource]
    ResponseMetadata: ResponseMetadata


class ListGroupingStatusesOutput(BaseValidatorModel):
    Group: str
    GroupingStatuses: List[GroupingStatusesItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGroupsInputPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[GroupFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchResourcesInputPaginate(BaseValidatorModel):
    ResourceQuery: ResourceQuery
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupResourcesInputPaginate(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Filters: Optional[Sequence[ResourceFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupResourcesInput(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Filters: Optional[Sequence[ResourceFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListGroupResourcesItem(BaseValidatorModel):
    Identifier: Optional[ResourceIdentifier] = None
    Status: Optional[ResourceStatus] = None


class SearchResourcesOutput(BaseValidatorModel):
    ResourceIdentifiers: List[ResourceIdentifier]
    QueryErrors: List[QueryError]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGroupingStatusesInputPaginate(BaseValidatorModel):
    Group: str
    Filters: Optional[Sequence[ListGroupingStatusesFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupingStatusesInput(BaseValidatorModel):
    Group: str
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[ListGroupingStatusesFilter]] = None
    NextToken: Optional[str] = None


class ListTagSyncTasksInputPaginate(BaseValidatorModel):
    Filters: Optional[Sequence[ListTagSyncTasksFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagSyncTasksInput(BaseValidatorModel):
    Filters: Optional[Sequence[ListTagSyncTasksFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagSyncTasksOutput(BaseValidatorModel):
    TagSyncTasks: List[TagSyncTaskItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetGroupQueryOutput(BaseValidatorModel):
    GroupQuery: GroupQuery
    ResponseMetadata: ResponseMetadata


class UpdateGroupQueryOutput(BaseValidatorModel):
    GroupQuery: GroupQuery
    ResponseMetadata: ResponseMetadata


class GroupConfigurationItemOutput(BaseValidatorModel):
    pass


class GroupConfiguration(BaseValidatorModel):
    Configuration: Optional[List[GroupConfigurationItemOutput]] = None
    ProposedConfiguration: Optional[List[GroupConfigurationItemOutput]] = None
    Status: Optional[GroupConfigurationStatusType] = None
    FailureReason: Optional[str] = None


class ListGroupResourcesOutput(BaseValidatorModel):
    Resources: List[ListGroupResourcesItem]
    ResourceIdentifiers: List[ResourceIdentifier]
    QueryErrors: List[QueryError]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateGroupOutput(BaseValidatorModel):
    Group: Group
    ResourceQuery: ResourceQuery
    Tags: Dict[str, str]
    GroupConfiguration: GroupConfiguration
    ResponseMetadata: ResponseMetadata


class GetGroupConfigurationOutput(BaseValidatorModel):
    GroupConfiguration: GroupConfiguration
    ResponseMetadata: ResponseMetadata


class GroupConfigurationItemUnion(BaseValidatorModel):
    pass


class CreateGroupInput(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    ResourceQuery: Optional[ResourceQuery] = None
    Tags: Optional[Mapping[str, str]] = None
    Configuration: Optional[Sequence[GroupConfigurationItemUnion]] = None
    Criticality: Optional[int] = None
    Owner: Optional[str] = None
    DisplayName: Optional[str] = None


class PutGroupConfigurationInput(BaseValidatorModel):
    Group: Optional[str] = None
    Configuration: Optional[Sequence[GroupConfigurationItemUnion]] = None


