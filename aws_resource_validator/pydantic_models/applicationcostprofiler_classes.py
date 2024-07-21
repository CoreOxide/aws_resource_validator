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
from aws_resource_validator.pydantic_models.applicationcostprofiler_constants import *

class DeleteReportDefinitionRequestRequestTypeDef(BaseModel):
    reportId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class GetReportDefinitionRequestRequestTypeDef(BaseModel):
    reportId: str

class S3LocationTypeDef(BaseModel):
    bucket: str
    prefix: str

class SourceS3LocationTypeDef(BaseModel):
    bucket: str
    key: str
    region: Optional[S3BucketRegionType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListReportDefinitionsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DeleteReportDefinitionResultTypeDef(BaseModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportApplicationUsageResultTypeDef(BaseModel):
    importId: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutReportDefinitionResultTypeDef(BaseModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateReportDefinitionResultTypeDef(BaseModel):
    reportId: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetReportDefinitionResultTypeDef(BaseModel):
    reportId: str
    reportDescription: str
    reportFrequency: ReportFrequencyType
    format: FormatType
    destinationS3Location: S3LocationTypeDef
    createdAt: datetime
    lastUpdated: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutReportDefinitionRequestRequestTypeDef(BaseModel):
    reportId: str
    reportDescription: str
    reportFrequency: ReportFrequencyType
    format: FormatType
    destinationS3Location: S3LocationTypeDef

class ReportDefinitionTypeDef(BaseModel):
    reportId: Optional[str] = None
    reportDescription: Optional[str] = None
    reportFrequency: Optional[ReportFrequencyType] = None
    format: Optional[FormatType] = None
    destinationS3Location: Optional[S3LocationTypeDef] = None
    createdAt: Optional[datetime] = None
    lastUpdatedAt: Optional[datetime] = None

class UpdateReportDefinitionRequestRequestTypeDef(BaseModel):
    reportId: str
    reportDescription: str
    reportFrequency: ReportFrequencyType
    format: FormatType
    destinationS3Location: S3LocationTypeDef

class ImportApplicationUsageRequestRequestTypeDef(BaseModel):
    sourceS3Location: SourceS3LocationTypeDef

class ListReportDefinitionsRequestListReportDefinitionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListReportDefinitionsResultTypeDef(BaseModel):
    reportDefinitions: List[ReportDefinitionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

