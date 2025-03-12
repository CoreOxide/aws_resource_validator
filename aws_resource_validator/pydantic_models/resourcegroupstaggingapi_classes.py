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
from aws_resource_validator.pydantic_models.resourcegroupstaggingapi_constants import *

class ComplianceDetailsTypeDef(BaseValidatorModel):
    NoncompliantKeys: Optional[List[str]] = None
    KeysWithNoncompliantValues: Optional[List[str]] = None
    ComplianceStatus: Optional[bool] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class FailureInfoTypeDef(BaseValidatorModel):
    StatusCode: Optional[int] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetComplianceSummaryInputTypeDef(BaseValidatorModel):
    TargetIdFilters: Optional[Sequence[str]] = None
    RegionFilters: Optional[Sequence[str]] = None
    ResourceTypeFilters: Optional[Sequence[str]] = None
    TagKeyFilters: Optional[Sequence[str]] = None
    GroupBy: Optional[Sequence[GroupByAttributeType]] = None
    MaxResults: Optional[int] = None
    PaginationToken: Optional[str] = None


class SummaryTypeDef(BaseValidatorModel):
    LastUpdated: Optional[str] = None
    TargetId: Optional[str] = None
    TargetIdType: Optional[TargetIdTypeType] = None
    Region: Optional[str] = None
    ResourceType: Optional[str] = None
    NonCompliantResources: Optional[int] = None


class TagFilterTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class GetTagKeysInputTypeDef(BaseValidatorModel):
    PaginationToken: Optional[str] = None


class GetTagValuesInputTypeDef(BaseValidatorModel):
    Key: str
    PaginationToken: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class StartReportCreationInputTypeDef(BaseValidatorModel):
    S3Bucket: str


class TagResourcesInputTypeDef(BaseValidatorModel):
    ResourceARNList: Sequence[str]
    Tags: Mapping[str, str]


class UntagResourcesInputTypeDef(BaseValidatorModel):
    ResourceARNList: Sequence[str]
    TagKeys: Sequence[str]


class DescribeReportCreationOutputTypeDef(BaseValidatorModel):
    Status: str
    S3Location: str
    ErrorMessage: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTagKeysOutputTypeDef(BaseValidatorModel):
    PaginationToken: str
    TagKeys: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetTagValuesOutputTypeDef(BaseValidatorModel):
    PaginationToken: str
    TagValues: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourcesOutputTypeDef(BaseValidatorModel):
    FailedResourcesMap: Dict[str, FailureInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UntagResourcesOutputTypeDef(BaseValidatorModel):
    FailedResourcesMap: Dict[str, FailureInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetComplianceSummaryInputPaginateTypeDef(BaseValidatorModel):
    TargetIdFilters: Optional[Sequence[str]] = None
    RegionFilters: Optional[Sequence[str]] = None
    ResourceTypeFilters: Optional[Sequence[str]] = None
    TagKeyFilters: Optional[Sequence[str]] = None
    GroupBy: Optional[Sequence[GroupByAttributeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetTagKeysInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetTagValuesInputPaginateTypeDef(BaseValidatorModel):
    Key: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetComplianceSummaryOutputTypeDef(BaseValidatorModel):
    SummaryList: List[SummaryTypeDef]
    PaginationToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcesInputPaginateTypeDef(BaseValidatorModel):
    TagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    TagsPerPage: Optional[int] = None
    ResourceTypeFilters: Optional[Sequence[str]] = None
    IncludeComplianceDetails: Optional[bool] = None
    ExcludeCompliantResources: Optional[bool] = None
    ResourceARNList: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetResourcesInputTypeDef(BaseValidatorModel):
    PaginationToken: Optional[str] = None
    TagFilters: Optional[Sequence[TagFilterTypeDef]] = None
    ResourcesPerPage: Optional[int] = None
    TagsPerPage: Optional[int] = None
    ResourceTypeFilters: Optional[Sequence[str]] = None
    IncludeComplianceDetails: Optional[bool] = None
    ExcludeCompliantResources: Optional[bool] = None
    ResourceARNList: Optional[Sequence[str]] = None


class ResourceTagMappingTypeDef(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    Tags: Optional[List[TagTypeDef]] = None
    ComplianceDetails: Optional[ComplianceDetailsTypeDef] = None


class GetResourcesOutputTypeDef(BaseValidatorModel):
    PaginationToken: str
    ResourceTagMappingList: List[ResourceTagMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


