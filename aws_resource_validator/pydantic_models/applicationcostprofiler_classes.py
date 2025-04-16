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
from aws_resource_validator.pydantic_models.applicationcostprofiler_constants import *

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


class ImportApplicationUsageRequest(BaseValidatorModel):
    sourceS3Location: SourceS3Location


class ListReportDefinitionsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ReportDefinition(BaseValidatorModel):
    pass


class ListReportDefinitionsResult(BaseValidatorModel):
    reportDefinitions: List[ReportDefinition]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


