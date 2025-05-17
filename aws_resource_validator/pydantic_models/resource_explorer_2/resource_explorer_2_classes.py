from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'associate_default_view' function.
class AssociateDefaultViewInput(BaseValidatorModel):
    ViewArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetViewError(BaseValidatorModel):
    ErrorMessage: str
    ViewArn: str


# This class is the input for the 'batch_get_view' function.
class BatchGetViewInput(BaseValidatorModel):
    ViewArns: Optional[List[str]] = None


# This class is the input for the 'create_index' function.
class CreateIndexInput(BaseValidatorModel):
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class IncludedProperty(BaseValidatorModel):
    Name: str


class SearchFilter(BaseValidatorModel):
    FilterString: str


# This class is the input for the 'delete_index' function.
class DeleteIndexInput(BaseValidatorModel):
    Arn: str


# This class is the input for the 'delete_view' function.
class DeleteViewInput(BaseValidatorModel):
    ViewArn: str


class OrgConfiguration(BaseValidatorModel):
    AWSServiceAccessStatus: AWSServiceAccessStatusType
    ServiceLinkedRole: Optional[str] = None


# This class is the input for the 'get_managed_view' function.
class GetManagedViewInput(BaseValidatorModel):
    ManagedViewArn: str


# This class is the input for the 'get_view' function.
class GetViewInput(BaseValidatorModel):
    ViewArn: str


class Index(BaseValidatorModel):
    Arn: Optional[str] = None
    Region: Optional[str] = None
    Type: Optional[IndexTypeType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_indexes_for_members' function.
class ListIndexesForMembersInput(BaseValidatorModel):
    AccountIdList: List[str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MemberIndex(BaseValidatorModel):
    AccountId: Optional[str] = None
    Arn: Optional[str] = None
    Region: Optional[str] = None
    Type: Optional[IndexTypeType] = None


# This class is the input for the 'list_indexes' function.
class ListIndexesInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Regions: Optional[List[str]] = None
    Type: Optional[IndexTypeType] = None


# This class is the input for the 'list_managed_views' function.
class ListManagedViewsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ServicePrincipal: Optional[str] = None


# This class is the input for the 'list_supported_resource_types' function.
class ListSupportedResourceTypesInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SupportedResourceType(BaseValidatorModel):
    ResourceType: Optional[str] = None
    Service: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_views' function.
class ListViewsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ResourceCount(BaseValidatorModel):
    Complete: Optional[bool] = None
    TotalResources: Optional[int] = None


class ResourceProperty(BaseValidatorModel):
    Data: Optional[Dict[str, Any]] = None
    LastReportedAt: Optional[datetime] = None
    Name: Optional[str] = None


# This class is the input for the 'search' function.
class SearchInput(BaseValidatorModel):
    QueryString: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ViewArn: Optional[str] = None


class TagResourceInput(BaseValidatorModel):
    resourceArn: str
    Tags: Optional[Dict[str, str]] = None


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_index_type' function.
class UpdateIndexTypeInput(BaseValidatorModel):
    Arn: str
    Type: IndexTypeType


# This class is the output for the 'associate_default_view' function.
class AssociateDefaultViewOutput(BaseValidatorModel):
    ViewArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_index' function.
class CreateIndexOutput(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    State: IndexStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_index' function.
class DeleteIndexOutput(BaseValidatorModel):
    Arn: str
    LastUpdatedAt: datetime
    State: IndexStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_view' function.
class DeleteViewOutput(BaseValidatorModel):
    ViewArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetDefaultViewOutput(BaseValidatorModel):
    ViewArn: str
    ResponseMetadata: ResponseMetadata


class GetIndexOutput(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    ReplicatingFrom: List[str]
    ReplicatingTo: List[str]
    State: IndexStateType
    Tags: Dict[str, str]
    Type: IndexTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_managed_views' function.
class ListManagedViewsOutput(BaseValidatorModel):
    ManagedViews: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_views' function.
class ListViewsOutput(BaseValidatorModel):
    Views: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_index_type' function.
class UpdateIndexTypeOutput(BaseValidatorModel):
    Arn: str
    LastUpdatedAt: datetime
    State: IndexStateType
    Type: IndexTypeType
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_view' function.
class CreateViewInput(BaseValidatorModel):
    ViewName: str
    ClientToken: Optional[str] = None
    Filters: Optional[SearchFilter] = None
    IncludedProperties: Optional[List[IncludedProperty]] = None
    Scope: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'list_resources' function.
class ListResourcesInput(BaseValidatorModel):
    Filters: Optional[SearchFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ViewArn: Optional[str] = None


class ManagedView(BaseValidatorModel):
    Filters: Optional[SearchFilter] = None
    IncludedProperties: Optional[List[IncludedProperty]] = None
    LastUpdatedAt: Optional[datetime] = None
    ManagedViewArn: Optional[str] = None
    ManagedViewName: Optional[str] = None
    Owner: Optional[str] = None
    ResourcePolicy: Optional[str] = None
    Scope: Optional[str] = None
    TrustedService: Optional[str] = None
    Version: Optional[str] = None


# This class is the input for the 'update_view' function.
class UpdateViewInput(BaseValidatorModel):
    ViewArn: str
    Filters: Optional[SearchFilter] = None
    IncludedProperties: Optional[List[IncludedProperty]] = None


class View(BaseValidatorModel):
    Filters: Optional[SearchFilter] = None
    IncludedProperties: Optional[List[IncludedProperty]] = None
    LastUpdatedAt: Optional[datetime] = None
    Owner: Optional[str] = None
    Scope: Optional[str] = None
    ViewArn: Optional[str] = None


class GetAccountLevelServiceConfigurationOutput(BaseValidatorModel):
    OrgConfiguration: OrgConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_indexes' function.
class ListIndexesOutput(BaseValidatorModel):
    Indexes: List[Index]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListIndexesForMembersInputPaginate(BaseValidatorModel):
    AccountIdList: List[str]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIndexesInputPaginate(BaseValidatorModel):
    Regions: Optional[List[str]] = None
    Type: Optional[IndexTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListManagedViewsInputPaginate(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListResourcesInputPaginate(BaseValidatorModel):
    Filters: Optional[SearchFilter] = None
    ViewArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSupportedResourceTypesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListViewsInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchInputPaginate(BaseValidatorModel):
    QueryString: str
    ViewArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_indexes_for_members' function.
class ListIndexesForMembersOutput(BaseValidatorModel):
    Indexes: List[MemberIndex]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_supported_resource_types' function.
class ListSupportedResourceTypesOutput(BaseValidatorModel):
    ResourceTypes: List[SupportedResourceType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Resource(BaseValidatorModel):
    Arn: Optional[str] = None
    LastReportedAt: Optional[datetime] = None
    OwningAccountId: Optional[str] = None
    Properties: Optional[List[ResourceProperty]] = None
    Region: Optional[str] = None
    ResourceType: Optional[str] = None
    Service: Optional[str] = None


# This class is the output for the 'get_managed_view' function.
class GetManagedViewOutput(BaseValidatorModel):
    ManagedView: ManagedView
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_get_view' function.
class BatchGetViewOutput(BaseValidatorModel):
    Errors: List[BatchGetViewError]
    Views: List[View]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_view' function.
class CreateViewOutput(BaseValidatorModel):
    View: View
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_view' function.
class GetViewOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    View: View
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_view' function.
class UpdateViewOutput(BaseValidatorModel):
    View: View
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_resources' function.
class ListResourcesOutput(BaseValidatorModel):
    Resources: List[Resource]
    ViewArn: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'search' function.
class SearchOutput(BaseValidatorModel):
    Count: ResourceCount
    Resources: List[Resource]
    ViewArn: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None