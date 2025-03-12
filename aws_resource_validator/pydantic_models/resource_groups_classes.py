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

class AccountSettingsTypeDef(BaseValidatorModel):
    GroupLifecycleEventsDesiredStatus: Optional[GroupLifecycleEventsDesiredStatusType] = None
    GroupLifecycleEventsStatus: Optional[GroupLifecycleEventsStatusType] = None
    GroupLifecycleEventsStatusMessage: Optional[str] = None


class CancelTagSyncTaskInputTypeDef(BaseValidatorModel):
    TaskArn: str


class GroupTypeDef(BaseValidatorModel):
    GroupArn: str
    Name: str
    Description: Optional[str] = None
    Criticality: Optional[int] = None
    Owner: Optional[str] = None
    DisplayName: Optional[str] = None
    ApplicationTag: Optional[Dict[str, str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeleteGroupInputTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None


class FailedResourceTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None


class GetGroupConfigurationInputTypeDef(BaseValidatorModel):
    Group: Optional[str] = None


class GetGroupInputTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None


class GetGroupQueryInputTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None


class GetTagSyncTaskInputTypeDef(BaseValidatorModel):
    TaskArn: str


class GetTagsInputTypeDef(BaseValidatorModel):
    Arn: str


class GroupConfigurationParameterOutputTypeDef(BaseValidatorModel):
    Name: str
    Values: Optional[List[str]] = None


class GroupConfigurationParameterTypeDef(BaseValidatorModel):
    Name: str
    Values: Optional[Sequence[str]] = None


class GroupFilterTypeDef(BaseValidatorModel):
    Name: GroupFilterNameType
    Values: Sequence[str]


class GroupIdentifierTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupArn: Optional[str] = None
    Description: Optional[str] = None
    Criticality: Optional[int] = None
    Owner: Optional[str] = None
    DisplayName: Optional[str] = None


class GroupResourcesInputTypeDef(BaseValidatorModel):
    Group: str
    ResourceArns: Sequence[str]


class PendingResourceTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class GroupingStatusesItemTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    Action: Optional[GroupingTypeType] = None
    Status: Optional[GroupingStatusType] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None
    UpdatedAt: Optional[datetime] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ResourceFilterTypeDef(BaseValidatorModel):
    Name: Literal["resource-type"]
    Values: Sequence[str]


class ResourceIdentifierTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None


class ResourceStatusTypeDef(BaseValidatorModel):
    Name: Optional[Literal["PENDING"]] = None


class QueryErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[QueryErrorCodeType] = None
    Message: Optional[str] = None


class ListGroupingStatusesFilterTypeDef(BaseValidatorModel):
    Name: ListGroupingStatusesFilterNameType
    Values: Sequence[str]


class ListTagSyncTasksFilterTypeDef(BaseValidatorModel):
    GroupArn: Optional[str] = None
    GroupName: Optional[str] = None


class TagSyncTaskItemTypeDef(BaseValidatorModel):
    GroupArn: Optional[str] = None
    GroupName: Optional[str] = None
    TaskArn: Optional[str] = None
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None
    RoleArn: Optional[str] = None
    Status: Optional[TagSyncTaskStatusType] = None
    ErrorMessage: Optional[str] = None
    CreatedAt: Optional[datetime] = None


class StartTagSyncTaskInputTypeDef(BaseValidatorModel):
    Group: str
    TagKey: str
    TagValue: str
    RoleArn: str


class TagInputTypeDef(BaseValidatorModel):
    Arn: str
    Tags: Mapping[str, str]


class UngroupResourcesInputTypeDef(BaseValidatorModel):
    Group: str
    ResourceArns: Sequence[str]


class UntagInputTypeDef(BaseValidatorModel):
    Arn: str
    Keys: Sequence[str]


class UpdateAccountSettingsInputTypeDef(BaseValidatorModel):
    GroupLifecycleEventsDesiredStatus: Optional[GroupLifecycleEventsDesiredStatusType] = None


class UpdateGroupInputTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Description: Optional[str] = None
    Criticality: Optional[int] = None
    Owner: Optional[str] = None
    DisplayName: Optional[str] = None


class ResourceQueryTypeDef(BaseValidatorModel):
    pass


class GroupQueryTypeDef(BaseValidatorModel):
    GroupName: str
    ResourceQuery: ResourceQueryTypeDef


class SearchResourcesInputTypeDef(BaseValidatorModel):
    ResourceQuery: ResourceQueryTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class UpdateGroupQueryInputTypeDef(BaseValidatorModel):
    ResourceQuery: ResourceQueryTypeDef
    GroupName: Optional[str] = None
    Group: Optional[str] = None


class DeleteGroupOutputTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccountSettingsOutputTypeDef(BaseValidatorModel):
    AccountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetGroupOutputTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetTagSyncTaskOutputTypeDef(BaseValidatorModel):
    GroupArn: str
    GroupName: str
    TaskArn: str
    TagKey: str
    TagValue: str
    RoleArn: str
    Status: TagSyncTaskStatusType
    ErrorMessage: str
    CreatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetTagsOutputTypeDef(BaseValidatorModel):
    Arn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class StartTagSyncTaskOutputTypeDef(BaseValidatorModel):
    GroupArn: str
    GroupName: str
    TaskArn: str
    TagKey: str
    TagValue: str
    RoleArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class TagOutputTypeDef(BaseValidatorModel):
    Arn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class UntagOutputTypeDef(BaseValidatorModel):
    Arn: str
    Keys: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAccountSettingsOutputTypeDef(BaseValidatorModel):
    AccountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateGroupOutputTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListGroupsInputTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[GroupFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListGroupsOutputTypeDef(BaseValidatorModel):
    GroupIdentifiers: List[GroupIdentifierTypeDef]
    Groups: List[GroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GroupResourcesOutputTypeDef(BaseValidatorModel):
    Succeeded: List[str]
    Failed: List[FailedResourceTypeDef]
    Pending: List[PendingResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UngroupResourcesOutputTypeDef(BaseValidatorModel):
    Succeeded: List[str]
    Failed: List[FailedResourceTypeDef]
    Pending: List[PendingResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListGroupingStatusesOutputTypeDef(BaseValidatorModel):
    Group: str
    GroupingStatuses: List[GroupingStatusesItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListGroupsInputPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[GroupFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchResourcesInputPaginateTypeDef(BaseValidatorModel):
    ResourceQuery: ResourceQueryTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupResourcesInputPaginateTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Filters: Optional[Sequence[ResourceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupResourcesInputTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Filters: Optional[Sequence[ResourceFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListGroupResourcesItemTypeDef(BaseValidatorModel):
    Identifier: Optional[ResourceIdentifierTypeDef] = None
    Status: Optional[ResourceStatusTypeDef] = None


class SearchResourcesOutputTypeDef(BaseValidatorModel):
    ResourceIdentifiers: List[ResourceIdentifierTypeDef]
    QueryErrors: List[QueryErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListGroupingStatusesInputPaginateTypeDef(BaseValidatorModel):
    Group: str
    Filters: Optional[Sequence[ListGroupingStatusesFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupingStatusesInputTypeDef(BaseValidatorModel):
    Group: str
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[ListGroupingStatusesFilterTypeDef]] = None
    NextToken: Optional[str] = None


class ListTagSyncTasksInputPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ListTagSyncTasksFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagSyncTasksInputTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[ListTagSyncTasksFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagSyncTasksOutputTypeDef(BaseValidatorModel):
    TagSyncTasks: List[TagSyncTaskItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetGroupQueryOutputTypeDef(BaseValidatorModel):
    GroupQuery: GroupQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateGroupQueryOutputTypeDef(BaseValidatorModel):
    GroupQuery: GroupQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GroupConfigurationItemOutputTypeDef(BaseValidatorModel):
    pass


class GroupConfigurationTypeDef(BaseValidatorModel):
    Configuration: Optional[List[GroupConfigurationItemOutputTypeDef]] = None
    ProposedConfiguration: Optional[List[GroupConfigurationItemOutputTypeDef]] = None
    Status: Optional[GroupConfigurationStatusType] = None
    FailureReason: Optional[str] = None


class ListGroupResourcesOutputTypeDef(BaseValidatorModel):
    Resources: List[ListGroupResourcesItemTypeDef]
    ResourceIdentifiers: List[ResourceIdentifierTypeDef]
    QueryErrors: List[QueryErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateGroupOutputTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResourceQuery: ResourceQueryTypeDef
    Tags: Dict[str, str]
    GroupConfiguration: GroupConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetGroupConfigurationOutputTypeDef(BaseValidatorModel):
    GroupConfiguration: GroupConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GroupConfigurationItemUnionTypeDef(BaseValidatorModel):
    pass


class CreateGroupInputTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    ResourceQuery: Optional[ResourceQueryTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    Configuration: Optional[Sequence[GroupConfigurationItemUnionTypeDef]] = None
    Criticality: Optional[int] = None
    Owner: Optional[str] = None
    DisplayName: Optional[str] = None


class PutGroupConfigurationInputTypeDef(BaseValidatorModel):
    Group: Optional[str] = None
    Configuration: Optional[Sequence[GroupConfigurationItemUnionTypeDef]] = None


