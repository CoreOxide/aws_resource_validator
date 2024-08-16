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
from aws_resource_validator.pydantic_models.resource_explorer_2_constants import *

class AssociateDefaultViewInputRequestTypeDef(BaseValidatorModel):
    ViewArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class BatchGetViewErrorTypeDef(BaseValidatorModel):
    ErrorMessage: str
    ViewArn: str

class BatchGetViewInputRequestTypeDef(BaseValidatorModel):
    ViewArns: Optional[Sequence[str]] = None

class CreateIndexInputRequestTypeDef(BaseValidatorModel):
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class IncludedPropertyTypeDef(BaseValidatorModel):
    Name: str

class SearchFilterTypeDef(BaseValidatorModel):
    FilterString: str

class DeleteIndexInputRequestTypeDef(BaseValidatorModel):
    Arn: str

class DeleteViewInputRequestTypeDef(BaseValidatorModel):
    ViewArn: str

class OrgConfigurationTypeDef(BaseValidatorModel):
    AWSServiceAccessStatus: AWSServiceAccessStatusType
    ServiceLinkedRole: Optional[str] = None

class GetViewInputRequestTypeDef(BaseValidatorModel):
    ViewArn: str

class IndexTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Region: Optional[str] = None
    Type: Optional[IndexTypeType] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListIndexesForMembersInputRequestTypeDef(BaseValidatorModel):
    AccountIdList: Sequence[str]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MemberIndexTypeDef(BaseValidatorModel):
    AccountId: Optional[str] = None
    Arn: Optional[str] = None
    Region: Optional[str] = None
    Type: Optional[IndexTypeType] = None

class ListIndexesInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Regions: Optional[Sequence[str]] = None
    Type: Optional[IndexTypeType] = None

class ListSupportedResourceTypesInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SupportedResourceTypeTypeDef(BaseValidatorModel):
    ResourceType: Optional[str] = None
    Service: Optional[str] = None

class ListTagsForResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListViewsInputRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ResourceCountTypeDef(BaseValidatorModel):
    Complete: Optional[bool] = None
    TotalResources: Optional[int] = None

class ResourcePropertyTypeDef(BaseValidatorModel):
    Data: Optional[Dict[str, Any]] = None
    LastReportedAt: Optional[datetime] = None
    Name: Optional[str] = None

class SearchInputRequestTypeDef(BaseValidatorModel):
    QueryString: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ViewArn: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    Tags: Optional[Mapping[str, str]] = None

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateIndexTypeInputRequestTypeDef(BaseValidatorModel):
    Arn: str
    Type: IndexTypeType

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

class GetIndexOutputTypeDef(BaseValidatorModel):
    Arn: str
    CreatedAt: datetime
    LastUpdatedAt: datetime
    ReplicatingFrom: List[str]
    ReplicatingTo: List[str]
    State: IndexStateType
    Tags: Dict[str, str]
    Type: IndexTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListViewsOutputTypeDef(BaseValidatorModel):
    NextToken: str
    Views: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateIndexTypeOutputTypeDef(BaseValidatorModel):
    Arn: str
    LastUpdatedAt: datetime
    State: IndexStateType
    Type: IndexTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateViewInputRequestTypeDef(BaseValidatorModel):
    ViewName: str
    ClientToken: Optional[str] = None
    Filters: Optional[SearchFilterTypeDef] = None
    IncludedProperties: Optional[Sequence[IncludedPropertyTypeDef]] = None
    Scope: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateViewInputRequestTypeDef(BaseValidatorModel):
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

class ListIndexesOutputTypeDef(BaseValidatorModel):
    Indexes: List[IndexTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListIndexesForMembersInputListIndexesForMembersPaginateTypeDef(BaseValidatorModel):
    AccountIdList: Sequence[str]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIndexesInputListIndexesPaginateTypeDef(BaseValidatorModel):
    Regions: Optional[Sequence[str]] = None
    Type: Optional[IndexTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSupportedResourceTypesInputListSupportedResourceTypesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListViewsInputListViewsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchInputSearchPaginateTypeDef(BaseValidatorModel):
    QueryString: str
    ViewArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIndexesForMembersOutputTypeDef(BaseValidatorModel):
    Indexes: List[MemberIndexTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSupportedResourceTypesOutputTypeDef(BaseValidatorModel):
    NextToken: str
    ResourceTypes: List[SupportedResourceTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResourceTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    LastReportedAt: Optional[datetime] = None
    OwningAccountId: Optional[str] = None
    Properties: Optional[List[ResourcePropertyTypeDef]] = None
    Region: Optional[str] = None
    ResourceType: Optional[str] = None
    Service: Optional[str] = None

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

class SearchOutputTypeDef(BaseValidatorModel):
    Count: ResourceCountTypeDef
    NextToken: str
    Resources: List[ResourceTypeDef]
    ViewArn: str
    ResponseMetadata: ResponseMetadataTypeDef

