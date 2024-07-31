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
from aws_resource_validator.pydantic_models.resource_groups_constants import *

class AccountSettingsTypeDef(BaseModel):
    GroupLifecycleEventsDesiredStatus: Optional[GroupLifecycleEventsDesiredStatusType] = None
    GroupLifecycleEventsStatus: Optional[GroupLifecycleEventsStatusType] = None
    GroupLifecycleEventsStatusMessage: Optional[str] = None

class ResourceQueryTypeDef(BaseModel):
    Type: QueryTypeType
    Query: str

class GroupTypeDef(BaseModel):
    GroupArn: str
    Name: str
    Description: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteGroupInputRequestTypeDef(BaseModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None

class FailedResourceTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None

class GetGroupConfigurationInputRequestTypeDef(BaseModel):
    Group: Optional[str] = None

class GetGroupInputRequestTypeDef(BaseModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None

class GetGroupQueryInputRequestTypeDef(BaseModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None

class GetTagsInputRequestTypeDef(BaseModel):
    Arn: str

class GroupConfigurationParameterTypeDef(BaseModel):
    Name: str
    Values: Optional[Sequence[str]] = None

class GroupFilterTypeDef(BaseModel):
    Name: GroupFilterNameType
    Values: Sequence[str]

class GroupIdentifierTypeDef(BaseModel):
    GroupName: Optional[str] = None
    GroupArn: Optional[str] = None

class GroupResourcesInputRequestTypeDef(BaseModel):
    Group: str
    ResourceArns: Sequence[str]

class PendingResourceTypeDef(BaseModel):
    ResourceArn: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ResourceFilterTypeDef(BaseModel):
    Name: Literal["resource-type"]
    Values: Sequence[str]

class ResourceIdentifierTypeDef(BaseModel):
    ResourceArn: Optional[str] = None
    ResourceType: Optional[str] = None

class ResourceStatusTypeDef(BaseModel):
    Name: Optional[Literal["PENDING"]] = None

class QueryErrorTypeDef(BaseModel):
    ErrorCode: Optional[QueryErrorCodeType] = None
    Message: Optional[str] = None

class TagInputRequestTypeDef(BaseModel):
    Arn: str
    Tags: Mapping[str, str]

class UngroupResourcesInputRequestTypeDef(BaseModel):
    Group: str
    ResourceArns: Sequence[str]

class UntagInputRequestTypeDef(BaseModel):
    Arn: str
    Keys: Sequence[str]

class UpdateAccountSettingsInputRequestTypeDef(BaseModel):
    GroupLifecycleEventsDesiredStatus: Optional[GroupLifecycleEventsDesiredStatusType] = None

class UpdateGroupInputRequestTypeDef(BaseModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Description: Optional[str] = None

class GroupQueryTypeDef(BaseModel):
    GroupName: str
    ResourceQuery: ResourceQueryTypeDef

class SearchResourcesInputRequestTypeDef(BaseModel):
    ResourceQuery: ResourceQueryTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UpdateGroupQueryInputRequestTypeDef(BaseModel):
    ResourceQuery: ResourceQueryTypeDef
    GroupName: Optional[str] = None
    Group: Optional[str] = None

class DeleteGroupOutputTypeDef(BaseModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSettingsOutputTypeDef(BaseModel):
    AccountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupOutputTypeDef(BaseModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTagsOutputTypeDef(BaseModel):
    Arn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class TagOutputTypeDef(BaseModel):
    Arn: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UntagOutputTypeDef(BaseModel):
    Arn: str
    Keys: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountSettingsOutputTypeDef(BaseModel):
    AccountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGroupOutputTypeDef(BaseModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GroupConfigurationItemTypeDef(BaseModel):
    Type: str
    Parameters: Optional[Sequence[GroupConfigurationParameterTypeDef]] = None

class ListGroupsInputRequestTypeDef(BaseModel):
    Filters: Optional[Sequence[GroupFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListGroupsOutputTypeDef(BaseModel):
    GroupIdentifiers: List[GroupIdentifierTypeDef]
    Groups: List[GroupTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GroupResourcesOutputTypeDef(BaseModel):
    Succeeded: List[str]
    Failed: List[FailedResourceTypeDef]
    Pending: List[PendingResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UngroupResourcesOutputTypeDef(BaseModel):
    Succeeded: List[str]
    Failed: List[FailedResourceTypeDef]
    Pending: List[PendingResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGroupsInputListGroupsPaginateTypeDef(BaseModel):
    Filters: Optional[Sequence[GroupFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchResourcesInputSearchResourcesPaginateTypeDef(BaseModel):
    ResourceQuery: ResourceQueryTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupResourcesInputListGroupResourcesPaginateTypeDef(BaseModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Filters: Optional[Sequence[ResourceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupResourcesInputRequestTypeDef(BaseModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Filters: Optional[Sequence[ResourceFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListGroupResourcesItemTypeDef(BaseModel):
    Identifier: Optional[ResourceIdentifierTypeDef] = None
    Status: Optional[ResourceStatusTypeDef] = None

class SearchResourcesOutputTypeDef(BaseModel):
    ResourceIdentifiers: List[ResourceIdentifierTypeDef]
    NextToken: str
    QueryErrors: List[QueryErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupQueryOutputTypeDef(BaseModel):
    GroupQuery: GroupQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGroupQueryOutputTypeDef(BaseModel):
    GroupQuery: GroupQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupInputRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    ResourceQuery: Optional[ResourceQueryTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    Configuration: Optional[Sequence[GroupConfigurationItemTypeDef]] = None

class GroupConfigurationTypeDef(BaseModel):
    Configuration: Optional[List[GroupConfigurationItemTypeDef]] = None
    ProposedConfiguration: Optional[List[GroupConfigurationItemTypeDef]] = None
    Status: Optional[GroupConfigurationStatusType] = None
    FailureReason: Optional[str] = None

class PutGroupConfigurationInputRequestTypeDef(BaseModel):
    Group: Optional[str] = None
    Configuration: Optional[Sequence[GroupConfigurationItemTypeDef]] = None

class ListGroupResourcesOutputTypeDef(BaseModel):
    Resources: List[ListGroupResourcesItemTypeDef]
    ResourceIdentifiers: List[ResourceIdentifierTypeDef]
    NextToken: str
    QueryErrors: List[QueryErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupOutputTypeDef(BaseModel):
    Group: GroupTypeDef
    ResourceQuery: ResourceQueryTypeDef
    Tags: Dict[str, str]
    GroupConfiguration: GroupConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupConfigurationOutputTypeDef(BaseModel):
    GroupConfiguration: GroupConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

