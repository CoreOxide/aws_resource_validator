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
from aws_resource_validator.pydantic_models.resource_explorer_2_constants import *

class AssociateDefaultViewInputRequestTypeDef(BaseModel):
    ViewArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchGetViewErrorTypeDef(BaseModel):
    ErrorMessage: str
    ViewArn: str

class BatchGetViewInputRequestTypeDef(BaseModel):
    ViewArns: Optional[Sequence[str]] = None

class CreateIndexInputRequestTypeDef(BaseModel):
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class IncludedPropertyTypeDef(BaseModel):
    Name: str

class SearchFilterTypeDef(BaseModel):
    FilterString: str

class DeleteIndexInputRequestTypeDef(BaseModel):
    Arn: str

class DeleteViewInputRequestTypeDef(BaseModel):
    ViewArn: str

class OrgConfigurationTypeDef(BaseModel):
    AWSServiceAccessStatus: AWSServiceAccessStatusType
    ServiceLinkedRole: Optional[str] = None

class GetViewInputRequestTypeDef(BaseModel):
    ViewArn: str

class IndexTypeDef(BaseModel):
    Arn: Optional[str] = None
    Region: Optional[str] = None
    Type: Optional[IndexTypeType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListIndexesForMembersInputRequestTypeDef(BaseModel):
    AccountIdList: Sequence[str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MemberIndexTypeDef(BaseModel):
    AccountId: Optional[str] = None
    Arn: Optional[str] = None
    Region: Optional[str] = None
    Type: Optional[IndexTypeType] = None

class ListIndexesInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Regions: Optional[Sequence[str]] = None
    Type: Optional[IndexTypeType] = None

class ListSupportedResourceTypesInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SupportedResourceTypeTypeDef(BaseModel):
    ResourceType: Optional[str] = None
    Service: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseModel):
    resourceArn: str

class ListViewsInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ResourceCountTypeDef(BaseModel):
    Complete: Optional[bool] = None
    TotalResources: Optional[int] = None

class ResourcePropertyTypeDef(BaseModel):
    Data: Optional[Dict[str, Any]] = None
    LastReportedAt: Optional[datetime] = None
    Name: Optional[str] = None

class SearchInputRequestTypeDef(BaseModel):
    QueryString: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ViewArn: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    Tags: Optional[Mapping[str, str]] = None

class UntagResourceInputRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateIndexTypeInputRequestTypeDef(BaseModel):
    Arn: str
    Type: IndexTypeType

class AssociateDefaultViewOutputTypeDef(BaseModel):
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIndexOutputTypeDef(BaseModel):
    Arn: str
    CreatedAt: datetime
    State: IndexStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteIndexOutputTypeDef(BaseModel):
    Arn: str
    LastUpdatedAt: datetime
    State: IndexStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteViewOutputTypeDef(BaseModel):
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetDefaultViewOutputTypeDef(BaseModel):
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetIndexOutputTypeDef(BaseModel):
    Arn: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    ReplicatingFrom: List[str]
    ReplicatingTo: List[str]
    State: IndexStateType
    Tags: Dict[str, str]
    Type: IndexTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListViewsOutputTypeDef(BaseModel):
    NextToken: str
    Views: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIndexTypeOutputTypeDef(BaseModel):
    Arn: str
    LastUpdatedAt: datetime
    State: IndexStateType
    Type: IndexTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateViewInputRequestTypeDef(BaseModel):
    ViewName: str
    ClientToken: Optional[str] = None
    Filters: Optional[SearchFilterTypeDef] = None
    IncludedProperties: Optional[Sequence[IncludedPropertyTypeDef]] = None
    Scope: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateViewInputRequestTypeDef(BaseModel):
    ViewArn: str
    Filters: Optional[SearchFilterTypeDef] = None
    IncludedProperties: Optional[Sequence[IncludedPropertyTypeDef]] = None

class ViewTypeDef(BaseModel):
    Filters: Optional[SearchFilterTypeDef] = None
    IncludedProperties: Optional[List[IncludedPropertyTypeDef]] = None
    LastUpdatedAt: Optional[datetime] = None
    Owner: Optional[str] = None
    Scope: Optional[str] = None
    ViewArn: Optional[str] = None

class GetAccountLevelServiceConfigurationOutputTypeDef(BaseModel):
    OrgConfiguration: OrgConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListIndexesOutputTypeDef(BaseModel):
    Indexes: List[IndexTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIndexesForMembersInputListIndexesForMembersPaginateTypeDef(BaseModel):
    AccountIdList: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIndexesInputListIndexesPaginateTypeDef(BaseModel):
    Regions: Optional[Sequence[str]] = None
    Type: Optional[IndexTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSupportedResourceTypesInputListSupportedResourceTypesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListViewsInputListViewsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchInputSearchPaginateTypeDef(BaseModel):
    QueryString: str
    ViewArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIndexesForMembersOutputTypeDef(BaseModel):
    Indexes: List[MemberIndexTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSupportedResourceTypesOutputTypeDef(BaseModel):
    NextToken: str
    ResourceTypes: List[SupportedResourceTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceTypeDef(BaseModel):
    Arn: Optional[str] = None
    LastReportedAt: Optional[datetime] = None
    OwningAccountId: Optional[str] = None
    Properties: Optional[List[ResourcePropertyTypeDef]] = None
    Region: Optional[str] = None
    ResourceType: Optional[str] = None
    Service: Optional[str] = None

class BatchGetViewOutputTypeDef(BaseModel):
    Errors: List[BatchGetViewErrorTypeDef]
    Views: List[ViewTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateViewOutputTypeDef(BaseModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetViewOutputTypeDef(BaseModel):
    Tags: Dict[str, str]
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateViewOutputTypeDef(BaseModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchOutputTypeDef(BaseModel):
    Count: ResourceCountTypeDef
    NextToken: str
    Resources: List[ResourceTypeDef]
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef

