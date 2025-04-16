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

class ComplianceDetails(BaseValidatorModel):
    NoncompliantKeys: Optional[List[str]] = None
    KeysWithNoncompliantValues: Optional[List[str]] = None
    ComplianceStatus: Optional[bool] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class FailureInfo(BaseValidatorModel):
    StatusCode: Optional[int] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetComplianceSummaryInput(BaseValidatorModel):
    TargetIdFilters: Optional[Sequence[str]] = None
    RegionFilters: Optional[Sequence[str]] = None
    ResourceTypeFilters: Optional[Sequence[str]] = None
    TagKeyFilters: Optional[Sequence[str]] = None
    GroupBy: Optional[Sequence[GroupByAttributeType]] = None
    MaxResults: Optional[int] = None
    PaginationToken: Optional[str] = None


class Summary(BaseValidatorModel):
    LastUpdated: Optional[str] = None
    TargetId: Optional[str] = None
    TargetIdType: Optional[TargetIdTypeType] = None
    Region: Optional[str] = None
    ResourceType: Optional[str] = None
    NonCompliantResources: Optional[int] = None


class TagFilter(BaseValidatorModel):
    Key: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class GetTagKeysInput(BaseValidatorModel):
    PaginationToken: Optional[str] = None


class GetTagValuesInput(BaseValidatorModel):
    Key: str
    PaginationToken: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class StartReportCreationInput(BaseValidatorModel):
    S3Bucket: str


class TagResourcesInput(BaseValidatorModel):
    ResourceARNList: Sequence[str]
    Tags: Mapping[str, str]


class UntagResourcesInput(BaseValidatorModel):
    ResourceARNList: Sequence[str]
    TagKeys: Sequence[str]


class DescribeReportCreationOutput(BaseValidatorModel):
    Status: str
    S3Location: str
    ErrorMessage: str
    ResponseMetadata: ResponseMetadata


class GetTagKeysOutput(BaseValidatorModel):
    PaginationToken: str
    TagKeys: List[str]
    ResponseMetadata: ResponseMetadata


class GetTagValuesOutput(BaseValidatorModel):
    PaginationToken: str
    TagValues: List[str]
    ResponseMetadata: ResponseMetadata


class TagResourcesOutput(BaseValidatorModel):
    FailedResourcesMap: Dict[str, FailureInfo]
    ResponseMetadata: ResponseMetadata


class UntagResourcesOutput(BaseValidatorModel):
    FailedResourcesMap: Dict[str, FailureInfo]
    ResponseMetadata: ResponseMetadata


class GetComplianceSummaryInputPaginate(BaseValidatorModel):
    TargetIdFilters: Optional[Sequence[str]] = None
    RegionFilters: Optional[Sequence[str]] = None
    ResourceTypeFilters: Optional[Sequence[str]] = None
    TagKeyFilters: Optional[Sequence[str]] = None
    GroupBy: Optional[Sequence[GroupByAttributeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetTagKeysInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetTagValuesInputPaginate(BaseValidatorModel):
    Key: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetComplianceSummaryOutput(BaseValidatorModel):
    SummaryList: List[Summary]
    PaginationToken: str
    ResponseMetadata: ResponseMetadata


class GetResourcesInputPaginate(BaseValidatorModel):
    TagFilters: Optional[Sequence[TagFilter]] = None
    TagsPerPage: Optional[int] = None
    ResourceTypeFilters: Optional[Sequence[str]] = None
    IncludeComplianceDetails: Optional[bool] = None
    ExcludeCompliantResources: Optional[bool] = None
    ResourceARNList: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetResourcesInput(BaseValidatorModel):
    PaginationToken: Optional[str] = None
    TagFilters: Optional[Sequence[TagFilter]] = None
    ResourcesPerPage: Optional[int] = None
    TagsPerPage: Optional[int] = None
    ResourceTypeFilters: Optional[Sequence[str]] = None
    IncludeComplianceDetails: Optional[bool] = None
    ExcludeCompliantResources: Optional[bool] = None
    ResourceARNList: Optional[Sequence[str]] = None


class ResourceTagMapping(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ComplianceDetails: Optional[ComplianceDetails] = None


class GetResourcesOutput(BaseValidatorModel):
    PaginationToken: str
    ResourceTagMappingList: List[ResourceTagMapping]
    ResponseMetadata: ResponseMetadata


