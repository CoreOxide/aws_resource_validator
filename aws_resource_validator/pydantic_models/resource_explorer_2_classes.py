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

class AssociateDefaultViewInputTypeDef(BaseValidatorModel):
    ViewArn: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetViewErrorTypeDef(BaseValidatorModel):
    ErrorMessage: str
    ViewArn: str


class BatchGetViewInputTypeDef(BaseValidatorModel):
    ViewArns: Optional[Sequence[str]] = None


class CreateIndexInputTypeDef(BaseValidatorModel):
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class IncludedPropertyTypeDef(BaseValidatorModel):
    Name: str


class SearchFilterTypeDef(BaseValidatorModel):
    FilterString: str


class DeleteIndexInputTypeDef(BaseValidatorModel):
    Arn: str


class DeleteViewInputTypeDef(BaseValidatorModel):
    ViewArn: str


class OrgConfigurationTypeDef(BaseValidatorModel):
    AWSServiceAccessStatus: AWSServiceAccessStatusType
    ServiceLinkedRole: Optional[str] = None


class GetManagedViewInputTypeDef(BaseValidatorModel):
    ManagedViewArn: str


class GetViewInputTypeDef(BaseValidatorModel):
    ViewArn: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListIndexesForMembersInputTypeDef(BaseValidatorModel):
    AccountIdList: Sequence[str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListManagedViewsInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ServicePrincipal: Optional[str] = None


class ListSupportedResourceTypesInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class SupportedResourceTypeTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    Service: Optional[str] = None


class ListTagsForResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str


class ListViewsInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ResourceCountTypeDef(BaseValidatorModel):
    Complete: Optional[bool] = None
    TotalResources: Optional[int] = None


class ResourcePropertyTypeDef(BaseValidatorModel):
    Data: Optional[Dict[str, Any]] = None
    LastReportedAt: Optional[datetime] = None
    Name: Optional[str] = None


class SearchInputTypeDef(BaseValidatorModel):
    QueryString: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ViewArn: Optional[str] = None


class TagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    Tags: Optional[Mapping[str, str]] = None


class UntagResourceInputTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class AssociateDefaultViewOutputTypeDef(BaseValidatorModel):
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIndexOutputTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    State: IndexStateType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteIndexOutputTypeDef(BaseValidatorModel):
    Arn: str
    LastUpdatedAt: datetime
    State: IndexStateType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteViewOutputTypeDef(BaseValidatorModel):
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetDefaultViewOutputTypeDef(BaseValidatorModel):
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListManagedViewsOutputTypeDef(BaseValidatorModel):
    ManagedViews: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListViewsOutputTypeDef(BaseValidatorModel):
    Views: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateViewInputTypeDef(BaseValidatorModel):
    ViewName: str
    ClientToken: Optional[str] = None
    Filters: Optional[SearchFilterTypeDef] = None
    IncludedProperties: Optional[Sequence[IncludedPropertyTypeDef]] = None
    Scope: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ListResourcesInputTypeDef(BaseValidatorModel):
    Filters: Optional[SearchFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ViewArn: Optional[str] = None


class ManagedViewTypeDef(BaseValidatorModel):
    Filters: Optional[SearchFilterTypeDef] = None
    IncludedProperties: Optional[List[IncludedPropertyTypeDef]] = None
    LastUpdatedAt: Optional[datetime] = None
    ManagedViewArn: Optional[str] = None
    ManagedViewName: Optional[str] = None
    Owner: Optional[str] = None
    ResourcePolicy: Optional[str] = None
    Scope: Optional[str] = None
    TrustedService: Optional[str] = None
    Version: Optional[str] = None


class UpdateViewInputTypeDef(BaseValidatorModel):
    ViewArn: str
    Filters: Optional[SearchFilterTypeDef] = None
    IncludedProperties: Optional[Sequence[IncludedPropertyTypeDef]] = None


class ViewTypeDef(BaseValidatorModel):
    Filters: Optional[SearchFilterTypeDef] = None
    IncludedProperties: Optional[List[IncludedPropertyTypeDef]] = None
    LastUpdatedAt: Optional[datetime] = None
    Owner: Optional[str] = None
    Scope: Optional[str] = None
    ViewArn: Optional[str] = None


class GetAccountLevelServiceConfigurationOutputTypeDef(BaseValidatorModel):
    OrgConfiguration: OrgConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class IndexTypeDef(BaseValidatorModel):
    pass


class ListIndexesOutputTypeDef(BaseValidatorModel):
    Indexes: List[IndexTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListIndexesForMembersInputPaginateTypeDef(BaseValidatorModel):
    AccountIdList: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListManagedViewsInputPaginateTypeDef(BaseValidatorModel):
    ServicePrincipal: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListResourcesInputPaginateTypeDef(BaseValidatorModel):
    Filters: Optional[SearchFilterTypeDef] = None
    ViewArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSupportedResourceTypesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListViewsInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchInputPaginateTypeDef(BaseValidatorModel):
    QueryString: str
    ViewArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class MemberIndexTypeDef(BaseValidatorModel):
    pass


class ListIndexesForMembersOutputTypeDef(BaseValidatorModel):
    Indexes: List[MemberIndexTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSupportedResourceTypesOutputTypeDef(BaseValidatorModel):
    ResourceTypes: List[SupportedResourceTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ResourceTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    LastReportedAt: Optional[datetime] = None
    OwningAccountId: Optional[str] = None
    Properties: Optional[List[ResourcePropertyTypeDef]] = None
    Region: Optional[str] = None
    ResourceType: Optional[str] = None
    Service: Optional[str] = None


class GetManagedViewOutputTypeDef(BaseValidatorModel):
    ManagedView: ManagedViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetViewOutputTypeDef(BaseValidatorModel):
    Errors: List[BatchGetViewErrorTypeDef]
    Views: List[ViewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateViewOutputTypeDef(BaseValidatorModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetViewOutputTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateViewOutputTypeDef(BaseValidatorModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListResourcesOutputTypeDef(BaseValidatorModel):
    Resources: List[ResourceTypeDef]
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchOutputTypeDef(BaseValidatorModel):
    Count: ResourceCountTypeDef
    Resources: List[ResourceTypeDef]
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


