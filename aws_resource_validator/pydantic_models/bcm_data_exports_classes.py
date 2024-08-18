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
from aws_resource_validator.pydantic_models.bcm_data_exports_constants import *

class ColumnTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[str] = None

class ResourceTagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DataQueryTypeDef(BaseValidatorModel):
    QueryStatement: str
    TableConfigurations: Optional[Mapping[str, Mapping[str, str]]] = None

class DeleteExportRequestRequestTypeDef(BaseValidatorModel):
    ExportArn: str

class ExecutionStatusTypeDef(BaseValidatorModel):
    CompletedAt: Optional[datetime] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    StatusCode: Optional[ExecutionStatusCodeType] = None
    StatusReason: Optional[ExecutionStatusReasonType] = None

class ExportStatusTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    LastRefreshedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    StatusCode: Optional[ExportStatusCodeType] = None
    StatusReason: Optional[ExecutionStatusReasonType] = None

class RefreshCadenceTypeDef(BaseValidatorModel):
    Frequency: Literal["SYNCHRONOUS"]

class GetExecutionRequestRequestTypeDef(BaseValidatorModel):
    ExecutionId: str
    ExportArn: str

class GetExportRequestRequestTypeDef(BaseValidatorModel):
    ExportArn: str

class GetTableRequestRequestTypeDef(BaseValidatorModel):
    TableName: str
    TableProperties: Optional[Mapping[str, str]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListExecutionsRequestRequestTypeDef(BaseValidatorModel):
    ExportArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListExportsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTablesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class S3OutputConfigurationsTypeDef(BaseValidatorModel):
    Compression: CompressionOptionType
    Format: FormatOptionType
    OutputType: Literal["CUSTOM"]
    Overwrite: OverwriteOptionType

class TablePropertyDescriptionTypeDef(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    ValidValues: Optional[List[str]] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourceTagKeys: Sequence[str]

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourceTags: Sequence[ResourceTagTypeDef]

class CreateExportResponseTypeDef(BaseValidatorModel):
    ExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteExportResponseTypeDef(BaseValidatorModel):
    ExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableResponseTypeDef(BaseValidatorModel):
    Description: str
    Schema: List[ColumnTypeDef]
    TableName: str
    TableProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    NextToken: str
    ResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateExportResponseTypeDef(BaseValidatorModel):
    ExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExecutionReferenceTypeDef(BaseValidatorModel):
    ExecutionId: str
    ExecutionStatus: ExecutionStatusTypeDef

class ExportReferenceTypeDef(BaseValidatorModel):
    ExportArn: str
    ExportName: str
    ExportStatus: ExportStatusTypeDef

class ListExecutionsRequestListExecutionsPaginateTypeDef(BaseValidatorModel):
    ExportArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExportsRequestListExportsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTablesRequestListTablesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class S3DestinationTypeDef(BaseValidatorModel):
    S3Bucket: str
    S3OutputConfigurations: S3OutputConfigurationsTypeDef
    S3Prefix: str
    S3Region: str

class TableTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    TableName: Optional[str] = None
    TableProperties: Optional[List[TablePropertyDescriptionTypeDef]] = None

class ListExecutionsResponseTypeDef(BaseValidatorModel):
    Executions: List[ExecutionReferenceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListExportsResponseTypeDef(BaseValidatorModel):
    Exports: List[ExportReferenceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationConfigurationsTypeDef(BaseValidatorModel):
    S3Destination: S3DestinationTypeDef

class ListTablesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Tables: List[TableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTypeDef(BaseValidatorModel):
    DataQuery: DataQueryTypeDef
    DestinationConfigurations: DestinationConfigurationsTypeDef
    Name: str
    RefreshCadence: RefreshCadenceTypeDef
    Description: Optional[str] = None
    ExportArn: Optional[str] = None

class CreateExportRequestRequestTypeDef(BaseValidatorModel):
    Export: ExportTypeDef
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None

class GetExecutionResponseTypeDef(BaseValidatorModel):
    ExecutionId: str
    ExecutionStatus: ExecutionStatusTypeDef
    Export: ExportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetExportResponseTypeDef(BaseValidatorModel):
    Export: ExportTypeDef
    ExportStatus: ExportStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateExportRequestRequestTypeDef(BaseValidatorModel):
    Export: ExportTypeDef
    ExportArn: str

