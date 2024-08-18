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
from aws_resource_validator.pydantic_models.applicationcostprofiler_constants import *

class DeleteReportDefinitionRequestRequestTypeDef(BaseValidatorModel):
    reportId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetReportDefinitionRequestRequestTypeDef(BaseValidatorModel):
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

class ListReportDefinitionsRequestRequestTypeDef(BaseValidatorModel):
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

class GetReportDefinitionResultTypeDef(BaseValidatorModel):
    reportId: str
    reportDescription: str
    reportFrequency: ReportFrequencyType
    format: FormatType
    destinationS3Location: S3LocationTypeDef
    createdAt: datetime
    lastUpdated: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutReportDefinitionRequestRequestTypeDef(BaseValidatorModel):
    reportId: str
    reportDescription: str
    reportFrequency: ReportFrequencyType
    format: FormatType
    destinationS3Location: S3LocationTypeDef

class ReportDefinitionTypeDef(BaseValidatorModel):
    reportId: Optional[str] = None
    reportDescription: Optional[str] = None
    reportFrequency: Optional[ReportFrequencyType] = None
    format: Optional[FormatType] = None
    destinationS3Location: Optional[S3LocationTypeDef] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None

class UpdateReportDefinitionRequestRequestTypeDef(BaseValidatorModel):
    reportId: str
    reportDescription: str
    reportFrequency: ReportFrequencyType
    format: FormatType
    destinationS3Location: S3LocationTypeDef

class ImportApplicationUsageRequestRequestTypeDef(BaseValidatorModel):
    sourceS3Location: SourceS3LocationTypeDef

class ListReportDefinitionsRequestListReportDefinitionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReportDefinitionsResultTypeDef(BaseValidatorModel):
    reportDefinitions: List[ReportDefinitionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

