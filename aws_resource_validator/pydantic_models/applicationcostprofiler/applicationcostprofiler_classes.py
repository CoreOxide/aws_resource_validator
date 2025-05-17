from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.applicationcostprofiler.applicationcostprofiler_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'delete_report_definition' function.
class DeleteReportDefinitionRequest(BaseValidatorModel):
    reportId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'get_report_definition' function.
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


# This class is the input for the 'list_report_definitions' function.
class ListReportDefinitionsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the output for the 'delete_report_definition' function.
class DeleteReportDefinitionResult(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_application_usage' function.
class ImportApplicationUsageResult(BaseValidatorModel):
    importId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_report_definition' function.
class PutReportDefinitionResult(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_report_definition' function.
class UpdateReportDefinitionResult(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_report_definition' function.
class GetReportDefinitionResult(BaseValidatorModel):
    reportId: str
    reportDescription: str
    reportFrequency: ReportFrequencyType
    format: FormatType
    destinationS3Location: S3Location
    createdAt: datetime
    lastUpdated: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_report_definition' function.
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


# This class is the input for the 'update_report_definition' function.
class UpdateReportDefinitionRequest(BaseValidatorModel):
    reportId: str
    reportDescription: str
    reportFrequency: ReportFrequencyType
    format: FormatType
    destinationS3Location: S3Location


# This class is the input for the 'import_application_usage' function.
class ImportApplicationUsageRequest(BaseValidatorModel):
    sourceS3Location: SourceS3Location


class ListReportDefinitionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_report_definitions' function.
class ListReportDefinitionsResult(BaseValidatorModel):
    reportDefinitions: List[ReportDefinition]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None