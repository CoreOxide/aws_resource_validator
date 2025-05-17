from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.resourcegroupstaggingapi.resourcegroupstaggingapi_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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


# This class is the input for the 'get_compliance_summary' function.
class GetComplianceSummaryInput(BaseValidatorModel):
    TargetIdFilters: Optional[List[str]] = None
    RegionFilters: Optional[List[str]] = None
    ResourceTypeFilters: Optional[List[str]] = None
    TagKeyFilters: Optional[List[str]] = None
    GroupBy: Optional[List[GroupByAttributeType]] = None
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
    Values: Optional[List[str]] = None


# This class is the input for the 'get_tag_keys' function.
class GetTagKeysInput(BaseValidatorModel):
    PaginationToken: Optional[str] = None


# This class is the input for the 'get_tag_values' function.
class GetTagValuesInput(BaseValidatorModel):
    Key: str
    PaginationToken: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class StartReportCreationInput(BaseValidatorModel):
    S3Bucket: str


# This class is the input for the 'tag_resources' function.
class TagResourcesInput(BaseValidatorModel):
    ResourceARNList: List[str]
    Tags: Dict[str, str]


# This class is the input for the 'untag_resources' function.
class UntagResourcesInput(BaseValidatorModel):
    ResourceARNList: List[str]
    TagKeys: List[str]


class DescribeReportCreationOutput(BaseValidatorModel):
    Status: str
    S3Location: str
    ErrorMessage: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_tag_keys' function.
class GetTagKeysOutput(BaseValidatorModel):
    PaginationToken: str
    TagKeys: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_tag_values' function.
class GetTagValuesOutput(BaseValidatorModel):
    PaginationToken: str
    TagValues: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'tag_resources' function.
class TagResourcesOutput(BaseValidatorModel):
    FailedResourcesMap: Dict[str, FailureInfo]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resources' function.
class UntagResourcesOutput(BaseValidatorModel):
    FailedResourcesMap: Dict[str, FailureInfo]
    ResponseMetadata: ResponseMetadata


class GetComplianceSummaryInputPaginate(BaseValidatorModel):
    TargetIdFilters: Optional[List[str]] = None
    RegionFilters: Optional[List[str]] = None
    ResourceTypeFilters: Optional[List[str]] = None
    TagKeyFilters: Optional[List[str]] = None
    GroupBy: Optional[List[GroupByAttributeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetTagKeysInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetTagValuesInputPaginate(BaseValidatorModel):
    Key: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'get_compliance_summary' function.
class GetComplianceSummaryOutput(BaseValidatorModel):
    SummaryList: List[Summary]
    PaginationToken: str
    ResponseMetadata: ResponseMetadata


class GetResourcesInputPaginate(BaseValidatorModel):
    TagFilters: Optional[List[TagFilter]] = None
    TagsPerPage: Optional[int] = None
    ResourceTypeFilters: Optional[List[str]] = None
    IncludeComplianceDetails: Optional[bool] = None
    ExcludeCompliantResources: Optional[bool] = None
    ResourceARNList: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_resources' function.
class GetResourcesInput(BaseValidatorModel):
    PaginationToken: Optional[str] = None
    TagFilters: Optional[List[TagFilter]] = None
    ResourcesPerPage: Optional[int] = None
    TagsPerPage: Optional[int] = None
    ResourceTypeFilters: Optional[List[str]] = None
    IncludeComplianceDetails: Optional[bool] = None
    ExcludeCompliantResources: Optional[bool] = None
    ResourceARNList: Optional[List[str]] = None


class ResourceTagMapping(BaseValidatorModel):
    ResourceARN: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    ComplianceDetails: Optional[ComplianceDetails] = None


# This class is the output for the 'get_resources' function.
class GetResourcesOutput(BaseValidatorModel):
    PaginationToken: str
    ResourceTagMappingList: List[ResourceTagMapping]
    ResponseMetadata: ResponseMetadata