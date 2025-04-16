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
from aws_resource_validator.pydantic_models.resource_explorer_2_constants import *

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
    ViewArns: Optional[Sequence[str]] = None


class CreateIndexInput(BaseValidatorModel):
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


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


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListIndexesForMembersInput(BaseValidatorModel):
    AccountIdList: Sequence[str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


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
    Tags: Optional[Mapping[str, str]] = None


class UntagResourceInput(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


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


class CreateViewInput(BaseValidatorModel):
    ViewName: str
    ClientToken: Optional[str] = None
    Filters: Optional[SearchFilter] = None
    IncludedProperties: Optional[Sequence[IncludedProperty]] = None
    Scope: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


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
    IncludedProperties: Optional[Sequence[IncludedProperty]] = None


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


class Index(BaseValidatorModel):
    pass


class ListIndexesOutput(BaseValidatorModel):
    Indexes: List[Index]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListIndexesForMembersInputPaginate(BaseValidatorModel):
    AccountIdList: Sequence[str]
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


class MemberIndex(BaseValidatorModel):
    pass


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


