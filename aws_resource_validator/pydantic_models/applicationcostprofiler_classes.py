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

class DeleteReportDefinitionRequestTypeDef(BaseValidatorModel):
    reportId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class GetReportDefinitionRequestTypeDef(BaseValidatorModel):
    reportId: str


class S3LocationTypeDef(BaseValidatorModel):
    bucket: str
    prefix: str


class SourceS3LocationTypeDef(BaseValidatorModel):
    bucket: str
    key: str
    region: Optional[S3BucketRegionType] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListReportDefinitionsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DeleteReportDefinitionResultTypeDef(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ImportApplicationUsageResultTypeDef(BaseValidatorModel):
    importId: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutReportDefinitionResultTypeDef(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateReportDefinitionResultTypeDef(BaseValidatorModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef


class ImportApplicationUsageRequestTypeDef(BaseValidatorModel):
    sourceS3Location: SourceS3LocationTypeDef


class ListReportDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ReportDefinitionTypeDef(BaseValidatorModel):
    pass


class ListReportDefinitionsResultTypeDef(BaseValidatorModel):
    reportDefinitions: List[ReportDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


