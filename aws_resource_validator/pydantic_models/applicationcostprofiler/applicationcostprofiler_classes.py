from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.applicationcostprofiler.applicationcostprofiler_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class DeleteReportDefinitionRequest(BaseValidatorModel):
    reportId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetReportDefinitionRequest(BaseValidatorModel):
    reportId: str


class S3Location(BaseValidatorModel):
    bucket: str
    prefix: str


class SourceS3Location(BaseValidatorModel):
    bucket: str
    key: str
    region: Optional[S3BucketRegionType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListReportDefinitionsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DeleteReportDefinitionResult(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadata


class ImportApplicationUsageResult(BaseValidatorModel):
    importId: str
    ResponseMetadata: ResponseMetadata


class PutReportDefinitionResult(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadata


class UpdateReportDefinitionResult(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadata


class GetReportDefinitionResult(BaseValidatorModel):
    reportId: str
    reportDescription: str
    reportFrequency: ReportFrequencyType
    format: FormatType
    destinationS3Location: S3Location
    createdAt: datetime
    lastUpdated: datetime
    ResponseMetadata: ResponseMetadata


class PutReportDefinitionRequest(BaseValidatorModel):
    reportId: str
    reportDescription: str
    reportFrequency: ReportFrequencyType
    format: FormatType
    destinationS3Location: S3Location


class ReportDefinition(BaseValidatorModel):
    reportId: Optional[str] = None
    reportDescription: Optional[str] = None
    reportFrequency: Optional[ReportFrequencyType] = None
    format: Optional[FormatType] = None
    destinationS3Location: Optional[S3Location] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None


class UpdateReportDefinitionRequest(BaseValidatorModel):
    reportId: str
    reportDescription: str
    reportFrequency: ReportFrequencyType
    format: FormatType
    destinationS3Location: S3Location


class ImportApplicationUsageRequest(BaseValidatorModel):
    sourceS3Location: SourceS3Location


class ListReportDefinitionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListReportDefinitionsResult(BaseValidatorModel):
    reportDefinitions: List[ReportDefinition]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None