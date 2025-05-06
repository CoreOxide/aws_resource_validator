from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.resource_explorer_2.resource_explorer_2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


class BatchGetViewInput(BaseValidatorModel):
    ViewArns: Optional[List[str]] = None


class CreateIndexInput(BaseValidatorModel):
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class IncludedProperty(BaseValidatorModel):
    Name: str


class SearchFilter(BaseValidatorModel):
    FilterString: str


class DeleteIndexInput(BaseValidatorModel):
    Arn: str


class DeleteViewInput(BaseValidatorModel):
    ViewArn: str


class OrgConfiguration(BaseValidatorModel):
    AWSServiceAccessStatus: AWSServiceAccessStatusType
    ServiceLinkedRole: Optional[str] = None


class GetManagedViewInput(BaseValidatorModel):
    ManagedViewArn: str


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


class ListIndexesForMembersInput(BaseValidatorModel):
    AccountIdList: List[str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MemberIndex(BaseValidatorModel):
    AccountId: Optional[str] = None
    Arn: Optional[str] = None
    Region: Optional[str] = None
    Type: Optional[IndexTypeType] = None


class ListIndexesInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Regions: Optional[List[str]] = None
    Type: Optional[IndexTypeType] = None


class ListManagedViewsInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ServicePrincipal: Optional[str] = None


class ListSupportedResourceTypesInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SupportedResourceType(BaseValidatorModel):
    ResourceType: Optional[str] = None
    Service: Optional[str] = None


class ListTagsForResourceInput(BaseValidatorModel):
    resourceArn: str


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


class UpdateIndexTypeInput(BaseValidatorModel):
    Arn: str
    Type: IndexTypeType


class AssociateDefaultViewOutput(BaseValidatorModel):
    ViewArn: str
    ResponseMetadata: ResponseMetadata


class CreateIndexOutput(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    State: IndexStateType
    ResponseMetadata: ResponseMetadata


class DeleteIndexOutput(BaseValidatorModel):
    Arn: str
    LastUpdatedAt: datetime
    State: IndexStateType
    ResponseMetadata: ResponseMetadata


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


class ListManagedViewsOutput(BaseValidatorModel):
    ManagedViews: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListViewsOutput(BaseValidatorModel):
    Views: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateIndexTypeOutput(BaseValidatorModel):
    Arn: str
    LastUpdatedAt: datetime
    State: IndexStateType
    Type: IndexTypeType
    ResponseMetadata: ResponseMetadata


class CreateViewInput(BaseValidatorModel):
    ViewName: str
    ClientToken: Optional[str] = None
    Filters: Optional[SearchFilter] = None
    IncludedProperties: Optional[List[IncludedProperty]] = None
    Scope: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


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


class ListIndexesForMembersOutput(BaseValidatorModel):
    Indexes: List[MemberIndex]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class GetManagedViewOutput(BaseValidatorModel):
    ManagedView: ManagedView
    ResponseMetadata: ResponseMetadata


class BatchGetViewOutput(BaseValidatorModel):
    Errors: List[BatchGetViewError]
    Views: List[View]
    ResponseMetadata: ResponseMetadata


class CreateViewOutput(BaseValidatorModel):
    View: View
    ResponseMetadata: ResponseMetadata


class GetViewOutput(BaseValidatorModel):
    Tags: Dict[str, str]
    View: View
    ResponseMetadata: ResponseMetadata


class UpdateViewOutput(BaseValidatorModel):
    View: View
    ResponseMetadata: ResponseMetadata


class ListResourcesOutput(BaseValidatorModel):
    Resources: List[Resource]
    ViewArn: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchOutput(BaseValidatorModel):
    Count: ResourceCount
    Resources: List[Resource]
    ViewArn: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None