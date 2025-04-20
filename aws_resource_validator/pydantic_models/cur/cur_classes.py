from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.cur.cur_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class DeleteReportDefinitionRequest(BaseValidatorModel):
    ReportName: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeReportDefinitionsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ReportName: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ReportStatus(BaseValidatorModel):
    lastDelivery: Optional[str] = None
    lastStatus: Optional[LastStatusType] = None


class UntagResourceRequest(BaseValidatorModel):
    ReportName: str
    TagKeys: List[str]


class DeleteReportDefinitionResponse(BaseValidatorModel):
    ResponseMessage: str
    ResponseMetadata: ResponseMetadata


class DescribeReportDefinitionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    ReportName: str
    Tags: List[Tag]


class ReportDefinitionOutput(BaseValidatorModel):
    ReportName: str
    TimeUnit: TimeUnitType
    Format: ReportFormatType
    Compression: CompressionFormatType
    AdditionalSchemaElements: List[SchemaElementType]
    S3Bucket: str
    S3Prefix: str
    S3Region: AWSRegionType
    AdditionalArtifacts: Optional[List[AdditionalArtifactType]] = None
    RefreshClosedReports: Optional[bool] = None
    ReportVersioning: Optional[ReportVersioningType] = None
    BillingViewArn: Optional[str] = None
    ReportStatus: Optional[ReportStatus] = None


class ReportDefinition(BaseValidatorModel):
    ReportName: str
    TimeUnit: TimeUnitType
    Format: ReportFormatType
    Compression: CompressionFormatType
    AdditionalSchemaElements: List[SchemaElementType]
    S3Bucket: str
    S3Prefix: str
    S3Region: AWSRegionType
    AdditionalArtifacts: Optional[List[AdditionalArtifactType]] = None
    RefreshClosedReports: Optional[bool] = None
    ReportVersioning: Optional[ReportVersioningType] = None
    BillingViewArn: Optional[str] = None
    ReportStatus: Optional[ReportStatus] = None


class DescribeReportDefinitionsResponse(BaseValidatorModel):
    ReportDefinitions: List[ReportDefinitionOutput]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

ReportDefinitionUnion = Union[ReportDefinition, ReportDefinitionOutput]


class ModifyReportDefinitionRequest(BaseValidatorModel):
    ReportName: str
    ReportDefinition: ReportDefinitionUnion


class PutReportDefinitionRequest(BaseValidatorModel):
    ReportDefinition: ReportDefinitionUnion
    Tags: Optional[List[Tag]] = None