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
from aws_resource_validator.pydantic_models.cur_constants import *

class DeleteReportDefinitionRequestRequestTypeDef(BaseModel):
    ReportName: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeReportDefinitionsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ReportName: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ReportStatusTypeDef(BaseModel):
    lastDelivery: Optional[str] = None
    lastStatus: Optional[LastStatusType] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ReportName: str
    TagKeys: Sequence[str]

class DeleteReportDefinitionResponseTypeDef(BaseModel):
    ResponseMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReportDefinitionsRequestDescribeReportDefinitionsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ReportName: str
    Tags: Sequence[TagTypeDef]

class ReportDefinitionExtraOutputTypeDef(BaseModel):
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
    ReportStatus: Optional[ReportStatusTypeDef] = None

class ReportDefinitionOutputTypeDef(BaseModel):
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
    ReportStatus: Optional[ReportStatusTypeDef] = None

class ReportDefinitionTypeDef(BaseModel):
    ReportName: str
    TimeUnit: TimeUnitType
    Format: ReportFormatType
    Compression: CompressionFormatType
    AdditionalSchemaElements: Sequence[SchemaElementType]
    S3Bucket: str
    S3Prefix: str
    S3Region: AWSRegionType
    AdditionalArtifacts: Optional[Sequence[AdditionalArtifactType]] = None
    RefreshClosedReports: Optional[bool] = None
    ReportVersioning: Optional[ReportVersioningType] = None
    BillingViewArn: Optional[str] = None
    ReportStatus: Optional[ReportStatusTypeDef] = None

class DescribeReportDefinitionsResponseTypeDef(BaseModel):
    ReportDefinitions: List[ReportDefinitionExtraOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyReportDefinitionRequestRequestTypeDef(BaseModel):
    ReportName: str
    ReportDefinition: ReportDefinitionTypeDef

class PutReportDefinitionRequestRequestTypeDef(BaseModel):
    ReportDefinition: ReportDefinitionTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

