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
from aws_resource_validator.pydantic_models.resourcegroupstaggingapi_constants import *

class ComplianceDetailsTypeDef(BaseModel):
    NoncompliantKeys: Optional[List[str]] = None
    KeysWithNoncompliantValues: Optional[List[str]] = None
    ComplianceStatus: Optional[bool] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class FailureInfoTypeDef(BaseModel):
    StatusCode: Optional[int] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetComplianceSummaryInputRequestTypeDef(BaseModel):
    TargetIdFilters: Optional[Sequence[str]] = None
    RegionFilters: Optional[Sequence[str]] = None
    ResourceTypeFilters: Optional[Sequence[str]] = None
    TagKeyFilters: Optional[Sequence[str]] = None
    GroupBy: Optional[Sequence[GroupByAttributeType]] = None
    MaxResults: Optional[int] = None
    PaginationToken: Optional[str] = None

class SummaryTypeDef(BaseModel):
    LastUpdated: Optional[str] = None
    TargetId: Optional[str] = None
    TargetIdType: Optional[TargetIdTypeType] = None
    Region: Optional[str] = None
    ResourceType: Optional[str] = None
    NonCompliantResources: Optional[int] = None

class TagFilterTypeDef(BaseModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None

class GetTagKeysInputRequestTypeDef(BaseModel):
    PaginationToken: Optional[str] = None

class GetTagValuesInputRequestTypeDef(BaseModel):
    Key: str
    PaginationToken: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class StartReportCreationInputRequestTypeDef(BaseModel):
    S3Bucket: str

class TagResourcesInputRequestTypeDef(BaseModel):
    ResourceARNList: Sequence[str]
    Tags: Mapping[str, str]

class UntagResourcesInputRequestTypeDef(BaseModel):
    ResourceARNList: Sequence[str]
    TagKeys: Sequence[str]

class DescribeReportCreationOutputTypeDef(BaseModel):
    Status: str
    S3Location: str
    ErrorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTagKeysOutputTypeDef(BaseModel):
    PaginationToken: str
    TagKeys: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTagValuesOutputTypeDef(BaseModel):
    PaginationToken: str
    TagValues: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourcesOutputTypeDef(BaseModel):
    FailedResourcesMap: Dict[str, FailureInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UntagResourcesOutputTypeDef(BaseModel):
    FailedResourcesMap: Dict[str, FailureInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetComplianceSummaryInputGetComplianceSummaryPaginateTypeDef(BaseModel):
    TargetIdFilters: Optional[Sequence[str]] = None
    RegionFilters: Optional[Sequence[str]] = None
    ResourceTypeFilters: Optional[Sequence[str]] = None
    TagKeyFilters: Optional[Sequence[str]] = None
    GroupBy: Optional[Sequence[GroupByAttributeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTagKeysInputGetTagKeysPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTagValuesInputGetTagValuesPaginateTypeDef(BaseModel):
    Key: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetComplianceSummaryOutputTypeDef(BaseModel):
    SummaryList: List[SummaryTypeDef]
    PaginationToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcesInputGetResourcesPaginateTypeDef(BaseModel):
    TagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    TagsPerPage: Optional[int] = None
    ResourceTypeFilters: Optional[Sequence[str]] = None
    IncludeComplianceDetails: Optional[bool] = None
    ExcludeCompliantResources: Optional[bool] = None
    ResourceARNList: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourcesInputRequestTypeDef(BaseModel):
    PaginationToken: Optional[str] = None
    TagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    ResourcesPerPage: Optional[int] = None
    TagsPerPage: Optional[int] = None
    ResourceTypeFilters: Optional[Sequence[str]] = None
    IncludeComplianceDetails: Optional[bool] = None
    ExcludeCompliantResources: Optional[bool] = None
    ResourceARNList: Optional[Sequence[str]] = None

class ResourceTagMappingTypeDef(BaseModel):
    ResourceARN: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    ComplianceDetails: Optional[ComplianceDetailsTypeDef] = None

class GetResourcesOutputTypeDef(BaseModel):
    PaginationToken: str
    ResourceTagMappingList: List[ResourceTagMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

