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
from aws_resource_validator.pydantic_models.bcm_data_exports_constants import *

class ColumnTypeDef(BaseModel):
    Description: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[str] = None

class ResourceTagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class DataQueryTypeDef(BaseModel):
    QueryStatement: str
    TableConfigurations: Optional[Mapping[str, Mapping[str, str]]] = None

class DeleteExportRequestRequestTypeDef(BaseModel):
    ExportArn: str

class ExecutionStatusTypeDef(BaseModel):
    CompletedAt: Optional[datetime] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    StatusCode: Optional[ExecutionStatusCodeType] = None
    StatusReason: Optional[ExecutionStatusReasonType] = None

class ExportStatusTypeDef(BaseModel):
    CreatedAt: Optional[datetime] = None
    LastRefreshedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    StatusCode: Optional[ExportStatusCodeType] = None
    StatusReason: Optional[ExecutionStatusReasonType] = None

class RefreshCadenceTypeDef(BaseModel):
    Frequency: Literal["SYNCHRONOUS"]

class GetExecutionRequestRequestTypeDef(BaseModel):
    ExecutionId: str
    ExportArn: str

class GetExportRequestRequestTypeDef(BaseModel):
    ExportArn: str

class GetTableRequestRequestTypeDef(BaseModel):
    TableName: str
    TableProperties: Optional[Mapping[str, str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListExecutionsRequestRequestTypeDef(BaseModel):
    ExportArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListExportsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTablesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class S3OutputConfigurationsTypeDef(BaseModel):
    Compression: CompressionOptionType
    Format: FormatOptionType
    OutputType: Literal["CUSTOM"]
    Overwrite: OverwriteOptionType

class TablePropertyDescriptionTypeDef(BaseModel):
    DefaultValue: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    ValidValues: Optional[List[str]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    ResourceTagKeys: Sequence[str]

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    ResourceTags: Sequence[ResourceTagTypeDef]

class CreateExportResponseTypeDef(BaseModel):
    ExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteExportResponseTypeDef(BaseModel):
    ExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableResponseTypeDef(BaseModel):
    Description: str
    Schema: List[ColumnTypeDef]
    TableName: str
    TableProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    NextToken: str
    ResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateExportResponseTypeDef(BaseModel):
    ExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExecutionReferenceTypeDef(BaseModel):
    ExecutionId: str
    ExecutionStatus: ExecutionStatusTypeDef

class ExportReferenceTypeDef(BaseModel):
    ExportArn: str
    ExportName: str
    ExportStatus: ExportStatusTypeDef

class ListExecutionsRequestListExecutionsPaginateTypeDef(BaseModel):
    ExportArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListExportsRequestListExportsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTablesRequestListTablesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class S3DestinationTypeDef(BaseModel):
    S3Bucket: str
    S3OutputConfigurations: S3OutputConfigurationsTypeDef
    S3Prefix: str
    S3Region: str

class TableTypeDef(BaseModel):
    Description: Optional[str] = None
    TableName: Optional[str] = None
    TableProperties: Optional[List[TablePropertyDescriptionTypeDef]] = None

class ListExecutionsResponseTypeDef(BaseModel):
    Executions: List[ExecutionReferenceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListExportsResponseTypeDef(BaseModel):
    Exports: List[ExportReferenceTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationConfigurationsTypeDef(BaseModel):
    S3Destination: S3DestinationTypeDef

class ListTablesResponseTypeDef(BaseModel):
    NextToken: str
    Tables: List[TableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTypeDef(BaseModel):
    DataQuery: DataQueryTypeDef
    DestinationConfigurations: DestinationConfigurationsTypeDef
    Name: str
    RefreshCadence: RefreshCadenceTypeDef
    Description: Optional[str] = None
    ExportArn: Optional[str] = None

class CreateExportRequestRequestTypeDef(BaseModel):
    Export: ExportTypeDef
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None

class GetExecutionResponseTypeDef(BaseModel):
    ExecutionId: str
    ExecutionStatus: ExecutionStatusTypeDef
    Export: ExportTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetExportResponseTypeDef(BaseModel):
    Export: ExportTypeDef
    ExportStatus: ExportStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateExportRequestRequestTypeDef(BaseModel):
    Export: ExportTypeDef
    ExportArn: str

