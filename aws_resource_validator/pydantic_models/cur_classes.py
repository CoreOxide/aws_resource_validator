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
from aws_resource_validator.pydantic_models.cur_constants import *

class DeleteReportDefinitionRequestTypeDef(BaseValidatorModel):
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


class DescribeReportDefinitionsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ReportName: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ReportStatusTypeDef(BaseValidatorModel):
    lastDelivery: Optional[str] = None
    lastStatus: Optional[LastStatusType] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ReportName: str
    TagKeys: Sequence[str]


class DeleteReportDefinitionResponseTypeDef(BaseValidatorModel):
    ResponseMessage: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeReportDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    ReportName: str
    Tags: Sequence[TagTypeDef]


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
    ReportDefinitions: List[ReportDefinitionOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ReportDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class ModifyReportDefinitionRequestTypeDef(BaseValidatorModel):
    ReportName: str
    ReportDefinition: ReportDefinitionUnionTypeDef


class PutReportDefinitionRequestTypeDef(BaseValidatorModel):
    ReportDefinition: ReportDefinitionUnionTypeDef
    Tags: Optional[Sequence[TagTypeDef]] = None


