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
from aws_resource_validator.pydantic_models.cur_constants import *

class DeleteReportDefinitionRequestRequestTypeDef(BaseValidatorModel):
    ReportName: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeReportDefinitionsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ReportName: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class ReportStatusTypeDef(BaseValidatorModel):
    lastDelivery: Optional[str] = None
    lastStatus: Optional[LastStatusType] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ReportName: str
    TagKeys: Sequence[str]

class DeleteReportDefinitionResponseTypeDef(BaseValidatorModel):
    ResponseMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReportDefinitionsRequestDescribeReportDefinitionsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ReportName: str
    Tags: Sequence[TagTypeDef]

class ReportDefinitionExtraOutputTypeDef(BaseValidatorModel):
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

class ReportDefinitionOutputTypeDef(BaseValidatorModel):
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

class ReportDefinitionTypeDef(BaseValidatorModel):
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

class DescribeReportDefinitionsResponseTypeDef(BaseValidatorModel):
    ReportDefinitions: List[ReportDefinitionExtraOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyReportDefinitionRequestRequestTypeDef(BaseValidatorModel):
    ReportName: str
    ReportDefinition: ReportDefinitionTypeDef

class PutReportDefinitionRequestRequestTypeDef(BaseValidatorModel):
    ReportDefinition: ReportDefinitionTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None

