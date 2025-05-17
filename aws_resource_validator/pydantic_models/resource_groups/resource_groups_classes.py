from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.resource_groups.resource_groups_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountSettings(BaseValidatorModel):
    GroupLifecycleEventsDesiredStatus: Optional[GroupLifecycleEventsDesiredStatusType] = None
    GroupLifecycleEventsStatus: Optional[GroupLifecycleEventsStatusType] = None
    GroupLifecycleEventsStatusMessage: Optional[str] = None


# This class is the input for the 'cancel_tag_sync_task' function.
class CancelTagSyncTaskInput(BaseValidatorModel):
    TaskArn: str


class ResourceQuery(BaseValidatorModel):
    Type: QueryTypeType
    Query: str


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


# This class is the input for the 'delete_group' function.
class DeleteGroupInput(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None


class FailedResource(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None


# This class is the input for the 'get_group_configuration' function.
class GetGroupConfigurationInput(BaseValidatorModel):
    Group: Optional[str] = None


# This class is the input for the 'get_group' function.
class GetGroupInput(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None


# This class is the input for the 'get_group_query' function.
class GetGroupQueryInput(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None


# This class is the input for the 'get_tag_sync_task' function.
class GetTagSyncTaskInput(BaseValidatorModel):
    TaskArn: str


# This class is the input for the 'get_tags' function.
class GetTagsInput(BaseValidatorModel):
    Arn: str


class GroupConfigurationParameterOutput(BaseValidatorModel):
    Name: str
    Values: Optional[List[str]] = None


class GroupConfigurationParameter(BaseValidatorModel):
    Name: str
    Values: Optional[List[str]] = None


class GroupFilter(BaseValidatorModel):
    Name: GroupFilterNameType
    Values: List[str]


class GroupIdentifier(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupArn: Optional[str] = None
    Description: Optional[str] = None
    Criticality: Optional[int] = None
    Owner: Optional[str] = None
    DisplayName: Optional[str] = None


# This class is the input for the 'group_resources' function.
class GroupResourcesInput(BaseValidatorModel):
    Group: str
    ResourceArns: List[str]


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
    Name: Literal['resource-type']
    Values: List[str]


class ResourceIdentifier(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None


class ResourceStatus(BaseValidatorModel):
    Name: Optional[Literal['PENDING']] = None


class QueryError(BaseValidatorModel):
    ErrorCode: Optional[QueryErrorCodeType] = None
    Message: Optional[str] = None


class ListGroupingStatusesFilter(BaseValidatorModel):
    Name: ListGroupingStatusesFilterNameType
    Values: List[str]


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


# This class is the input for the 'start_tag_sync_task' function.
class StartTagSyncTaskInput(BaseValidatorModel):
    Group: str
    TagKey: str
    TagValue: str
    RoleArn: str


# This class is the input for the 'tag' function.
class TagInput(BaseValidatorModel):
    Arn: str
    Tags: Dict[str, str]


# This class is the input for the 'ungroup_resources' function.
class UngroupResourcesInput(BaseValidatorModel):
    Group: str
    ResourceArns: List[str]


# This class is the input for the 'untag' function.
class UntagInput(BaseValidatorModel):
    Arn: str
    Keys: List[str]


# This class is the input for the 'update_account_settings' function.
class UpdateAccountSettingsInput(BaseValidatorModel):
    GroupLifecycleEventsDesiredStatus: Optional[GroupLifecycleEventsDesiredStatusType] = None


# This class is the input for the 'update_group' function.
class UpdateGroupInput(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Description: Optional[str] = None
    Criticality: Optional[int] = None
    Owner: Optional[str] = None
    DisplayName: Optional[str] = None


class GroupQuery(BaseValidatorModel):
    GroupName: str
    ResourceQuery: ResourceQuery


# This class is the input for the 'search_resources' function.
class SearchResourcesInput(BaseValidatorModel):
    ResourceQuery: ResourceQuery
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'update_group_query' function.
class UpdateGroupQueryInput(BaseValidatorModel):
    ResourceQuery: ResourceQuery
    GroupName: Optional[str] = None
    Group: Optional[str] = None


# This class is the output for the 'delete_group' function.
class DeleteGroupOutput(BaseValidatorModel):
    Group: Group
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_tag_sync_task' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAccountSettingsOutput(BaseValidatorModel):
    AccountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_group' function.
class GetGroupOutput(BaseValidatorModel):
    Group: Group
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_tag_sync_task' function.
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


# This class is the output for the 'get_tags' function.
class GetTagsOutput(BaseValidatorModel):
    Arn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_tag_sync_task' function.
class StartTagSyncTaskOutput(BaseValidatorModel):
    GroupArn: str
    GroupName: str
    TaskArn: str
    TagKey: str
    TagValue: str
    RoleArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'tag' function.
class TagOutput(BaseValidatorModel):
    Arn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag' function.
class UntagOutput(BaseValidatorModel):
    Arn: str
    Keys: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_account_settings' function.
class UpdateAccountSettingsOutput(BaseValidatorModel):
    AccountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_group' function.
class UpdateGroupOutput(BaseValidatorModel):
    Group: Group
    ResponseMetadata: ResponseMetadata


class GroupConfigurationItemOutput(BaseValidatorModel):
    Type: str
    Parameters: Optional[List[GroupConfigurationParameterOutput]] = None

GroupConfigurationParameterUnion = Union[GroupConfigurationParameter, GroupConfigurationParameterOutput]


# This class is the input for the 'list_groups' function.
class ListGroupsInput(BaseValidatorModel):
    Filters: Optional[List[GroupFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'list_groups' function.
class ListGroupsOutput(BaseValidatorModel):
    GroupIdentifiers: List[GroupIdentifier]
    Groups: List[Group]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'group_resources' function.
class GroupResourcesOutput(BaseValidatorModel):
    Succeeded: List[str]
    Failed: List[FailedResource]
    Pending: List[PendingResource]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'ungroup_resources' function.
class UngroupResourcesOutput(BaseValidatorModel):
    Succeeded: List[str]
    Failed: List[FailedResource]
    Pending: List[PendingResource]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_grouping_statuses' function.
class ListGroupingStatusesOutput(BaseValidatorModel):
    Group: str
    GroupingStatuses: List[GroupingStatusesItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGroupsInputPaginate(BaseValidatorModel):
    Filters: Optional[List[GroupFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchResourcesInputPaginate(BaseValidatorModel):
    ResourceQuery: ResourceQuery
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupResourcesInputPaginate(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Filters: Optional[List[ResourceFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_group_resources' function.
class ListGroupResourcesInput(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Filters: Optional[List[ResourceFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListGroupResourcesItem(BaseValidatorModel):
    Identifier: Optional[ResourceIdentifier] = None
    Status: Optional[ResourceStatus] = None


# This class is the output for the 'search_resources' function.
class SearchResourcesOutput(BaseValidatorModel):
    ResourceIdentifiers: List[ResourceIdentifier]
    QueryErrors: List[QueryError]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListGroupingStatusesInputPaginate(BaseValidatorModel):
    Group: str
    Filters: Optional[List[ListGroupingStatusesFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_grouping_statuses' function.
class ListGroupingStatusesInput(BaseValidatorModel):
    Group: str
    MaxResults: Optional[int] = None
    Filters: Optional[List[ListGroupingStatusesFilter]] = None
    NextToken: Optional[str] = None


class ListTagSyncTasksInputPaginate(BaseValidatorModel):
    Filters: Optional[List[ListTagSyncTasksFilter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_tag_sync_tasks' function.
class ListTagSyncTasksInput(BaseValidatorModel):
    Filters: Optional[List[ListTagSyncTasksFilter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'list_tag_sync_tasks' function.
class ListTagSyncTasksOutput(BaseValidatorModel):
    TagSyncTasks: List[TagSyncTaskItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_group_query' function.
class GetGroupQueryOutput(BaseValidatorModel):
    GroupQuery: GroupQuery
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_group_query' function.
class UpdateGroupQueryOutput(BaseValidatorModel):
    GroupQuery: GroupQuery
    ResponseMetadata: ResponseMetadata


class GroupConfiguration(BaseValidatorModel):
    Configuration: Optional[List[GroupConfigurationItemOutput]] = None
    ProposedConfiguration: Optional[List[GroupConfigurationItemOutput]] = None
    Status: Optional[GroupConfigurationStatusType] = None
    FailureReason: Optional[str] = None


class GroupConfigurationItem(BaseValidatorModel):
    Type: str
    Parameters: Optional[List[GroupConfigurationParameterUnion]] = None


# This class is the output for the 'list_group_resources' function.
class ListGroupResourcesOutput(BaseValidatorModel):
    Resources: List[ListGroupResourcesItem]
    ResourceIdentifiers: List[ResourceIdentifier]
    QueryErrors: List[QueryError]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_group' function.
class CreateGroupOutput(BaseValidatorModel):
    Group: Group
    ResourceQuery: ResourceQuery
    Tags: Dict[str, str]
    GroupConfiguration: GroupConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_group_configuration' function.
class GetGroupConfigurationOutput(BaseValidatorModel):
    GroupConfiguration: GroupConfiguration
    ResponseMetadata: ResponseMetadata

GroupConfigurationItemUnion = Union[GroupConfigurationItem, GroupConfigurationItemOutput]


# This class is the input for the 'create_group' function.
class CreateGroupInput(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    ResourceQuery: Optional[ResourceQuery] = None
    Tags: Optional[Dict[str, str]] = None
    Configuration: Optional[List[GroupConfigurationItemUnion]] = None
    Criticality: Optional[int] = None
    Owner: Optional[str] = None
    DisplayName: Optional[str] = None


class PutGroupConfigurationInput(BaseValidatorModel):
    Group: Optional[str] = None
    Configuration: Optional[List[GroupConfigurationItemUnion]] = None