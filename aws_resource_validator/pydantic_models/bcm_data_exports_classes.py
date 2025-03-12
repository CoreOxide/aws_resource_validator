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
from aws_resource_validator.pydantic_models.bcm_data_exports_constants import *

class ResourceTagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DataQueryOutputTypeDef(BaseValidatorModel):
    QueryStatement: str
    TableConfigurations: Optional[Dict[str, Dict[str, str]]] = None


class DataQueryTypeDef(BaseValidatorModel):
    QueryStatement: str
    TableConfigurations: Optional[Mapping[str, Mapping[str, str]]] = None


class DeleteExportRequestTypeDef(BaseValidatorModel):
    ExportArn: str


class ExecutionStatusTypeDef(BaseValidatorModel):
    CompletedAt: Optional[datetime] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    StatusCode: Optional[ExecutionStatusCodeType] = None
    StatusReason: Optional[ExecutionStatusReasonType] = None


class RefreshCadenceTypeDef(BaseValidatorModel):
    Frequency: Literal["SYNCHRONOUS"]


class ExportStatusTypeDef(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    LastRefreshedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    StatusCode: Optional[ExportStatusCodeType] = None
    StatusReason: Optional[ExecutionStatusReasonType] = None


class GetExecutionRequestTypeDef(BaseValidatorModel):
    ExecutionId: str
    ExportArn: str


class GetExportRequestTypeDef(BaseValidatorModel):
    ExportArn: str


class GetTableRequestTypeDef(BaseValidatorModel):
    TableName: str
    TableProperties: Optional[Mapping[str, str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListExecutionsRequestTypeDef(BaseValidatorModel):
    ExportArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListExportsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTablesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
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


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourceTagKeys: Sequence[str]


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ResourceTags: Sequence[ResourceTagTypeDef]


class CreateExportResponseTypeDef(BaseValidatorModel):
    ExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteExportResponseTypeDef(BaseValidatorModel):
    ExportArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ColumnTypeDef(BaseValidatorModel):
    pass


class GetTableResponseTypeDef(BaseValidatorModel):
    Description: str
    Schema: List[ColumnTypeDef]
    TableName: str
    TableProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    ResourceTags: List[ResourceTagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class ListExecutionsRequestPaginateTypeDef(BaseValidatorModel):
    ExportArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListExportsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTablesRequestPaginateTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListExportsResponseTypeDef(BaseValidatorModel):
    Exports: List[ExportReferenceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DestinationConfigurationsTypeDef(BaseValidatorModel):
    S3Destination: S3DestinationTypeDef


class ListTablesResponseTypeDef(BaseValidatorModel):
    Tables: List[TableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ExportOutputTypeDef(BaseValidatorModel):
    DataQuery: DataQueryOutputTypeDef
    DestinationConfigurations: DestinationConfigurationsTypeDef
    Name: str
    RefreshCadence: RefreshCadenceTypeDef
    Description: Optional[str] = None
    ExportArn: Optional[str] = None


class ExportTypeDef(BaseValidatorModel):
    DataQuery: DataQueryTypeDef
    DestinationConfigurations: DestinationConfigurationsTypeDef
    Name: str
    RefreshCadence: RefreshCadenceTypeDef
    Description: Optional[str] = None
    ExportArn: Optional[str] = None


class GetExecutionResponseTypeDef(BaseValidatorModel):
    ExecutionId: str
    ExecutionStatus: ExecutionStatusTypeDef
    Export: ExportOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetExportResponseTypeDef(BaseValidatorModel):
    Export: ExportOutputTypeDef
    ExportStatus: ExportStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ExportUnionTypeDef(BaseValidatorModel):
    pass


class CreateExportRequestTypeDef(BaseValidatorModel):
    Export: ExportUnionTypeDef
    ResourceTags: Optional[Sequence[ResourceTagTypeDef]] = None


class UpdateExportRequestTypeDef(BaseValidatorModel):
    Export: ExportUnionTypeDef
    ExportArn: str


