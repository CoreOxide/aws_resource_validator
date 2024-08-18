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
from aws_resource_validator.pydantic_models.resource_groups_constants import *

class AccountSettingsTypeDef(BaseValidatorModel):
    GroupLifecycleEventsDesiredStatus: Optional[GroupLifecycleEventsDesiredStatusType] = None
    GroupLifecycleEventsStatus: Optional[GroupLifecycleEventsStatusType] = None
    GroupLifecycleEventsStatusMessage: Optional[str] = None

class ResourceQueryTypeDef(BaseValidatorModel):
    Type: QueryTypeType
    Query: str

class GroupTypeDef(BaseValidatorModel):
    GroupArn: str
    Name: str
    Description: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeleteGroupInputRequestTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None

class FailedResourceTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None
    ErrorMessage: Optional[str] = None
    ErrorCode: Optional[str] = None

class GetGroupConfigurationInputRequestTypeDef(BaseValidatorModel):
    Group: Optional[str] = None

class GetGroupInputRequestTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None

class GetGroupQueryInputRequestTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None

class GetTagsInputRequestTypeDef(BaseValidatorModel):
    Arn: str

class GroupConfigurationParameterTypeDef(BaseValidatorModel):
    Name: str
    Values: Optional[Sequence[str]] = None

class GroupFilterTypeDef(BaseValidatorModel):
    Name: GroupFilterNameType
    Values: Sequence[str]

class GroupIdentifierTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    GroupArn: Optional[str] = None

class GroupResourcesInputRequestTypeDef(BaseValidatorModel):
    Group: str
    ResourceArns: Sequence[str]

class PendingResourceTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None

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

class TagInputRequestTypeDef(BaseValidatorModel):
    Arn: str
    Tags: Mapping[str, str]

class UngroupResourcesInputRequestTypeDef(BaseValidatorModel):
    Group: str
    ResourceArns: Sequence[str]

class UntagInputRequestTypeDef(BaseValidatorModel):
    Arn: str
    Keys: Sequence[str]

class UpdateAccountSettingsInputRequestTypeDef(BaseValidatorModel):
    GroupLifecycleEventsDesiredStatus: Optional[GroupLifecycleEventsDesiredStatusType] = None

class UpdateGroupInputRequestTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Description: Optional[str] = None

class GroupQueryTypeDef(BaseValidatorModel):
    GroupName: str
    ResourceQuery: ResourceQueryTypeDef

class SearchResourcesInputRequestTypeDef(BaseValidatorModel):
    ResourceQuery: ResourceQueryTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UpdateGroupQueryInputRequestTypeDef(BaseValidatorModel):
    ResourceQuery: ResourceQueryTypeDef
    GroupName: Optional[str] = None
    Group: Optional[str] = None

class DeleteGroupOutputTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSettingsOutputTypeDef(BaseValidatorModel):
    AccountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupOutputTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTagsOutputTypeDef(BaseValidatorModel):
    Arn: str
    Tags: Dict[str, str]
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

class GroupConfigurationItemTypeDef(BaseValidatorModel):
    Type: str
    Parameters: Optional[Sequence[GroupConfigurationParameterTypeDef]] = None

class ListGroupsInputRequestTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[GroupFilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListGroupsOutputTypeDef(BaseValidatorModel):
    GroupIdentifiers: List[GroupIdentifierTypeDef]
    Groups: List[GroupTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListGroupsInputListGroupsPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[Sequence[GroupFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchResourcesInputSearchResourcesPaginateTypeDef(BaseValidatorModel):
    ResourceQuery: ResourceQueryTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupResourcesInputListGroupResourcesPaginateTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None
    Group: Optional[str] = None
    Filters: Optional[Sequence[ResourceFilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupResourcesInputRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    QueryErrors: List[QueryErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupQueryOutputTypeDef(BaseValidatorModel):
    GroupQuery: GroupQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGroupQueryOutputTypeDef(BaseValidatorModel):
    GroupQuery: GroupQueryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupInputRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    ResourceQuery: Optional[ResourceQueryTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None
    Configuration: Optional[Sequence[GroupConfigurationItemTypeDef]] = None

class GroupConfigurationTypeDef(BaseValidatorModel):
    Configuration: Optional[List[GroupConfigurationItemTypeDef]] = None
    ProposedConfiguration: Optional[List[GroupConfigurationItemTypeDef]] = None
    Status: Optional[GroupConfigurationStatusType] = None
    FailureReason: Optional[str] = None

class PutGroupConfigurationInputRequestTypeDef(BaseValidatorModel):
    Group: Optional[str] = None
    Configuration: Optional[Sequence[GroupConfigurationItemTypeDef]] = None

class ListGroupResourcesOutputTypeDef(BaseValidatorModel):
    Resources: List[ListGroupResourcesItemTypeDef]
    ResourceIdentifiers: List[ResourceIdentifierTypeDef]
    NextToken: str
    QueryErrors: List[QueryErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGroupOutputTypeDef(BaseValidatorModel):
    Group: GroupTypeDef
    ResourceQuery: ResourceQueryTypeDef
    Tags: Dict[str, str]
    GroupConfiguration: GroupConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupConfigurationOutputTypeDef(BaseValidatorModel):
    GroupConfiguration: GroupConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

