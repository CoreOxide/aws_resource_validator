from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.bcm_data_exports.bcm_data_exports_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Column(BaseValidatorModel):
    Description: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[str] = None


class ResourceTag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DataQueryOutput(BaseValidatorModel):
    QueryStatement: str
    TableConfigurations: Optional[Dict[str, Dict[str, str]]] = None


class DataQuery(BaseValidatorModel):
    QueryStatement: str
    TableConfigurations: Optional[Dict[str, Dict[str, str]]] = None


class DeleteExportRequest(BaseValidatorModel):
    ExportArn: str


class ExecutionStatus(BaseValidatorModel):
    CompletedAt: Optional[datetime] = None
    CreatedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    StatusCode: Optional[ExecutionStatusCodeType] = None
    StatusReason: Optional[ExecutionStatusReasonType] = None


class RefreshCadence(BaseValidatorModel):
    Frequency: Literal['SYNCHRONOUS']


class ExportStatus(BaseValidatorModel):
    CreatedAt: Optional[datetime] = None
    LastRefreshedAt: Optional[datetime] = None
    LastUpdatedAt: Optional[datetime] = None
    StatusCode: Optional[ExportStatusCodeType] = None
    StatusReason: Optional[ExecutionStatusReasonType] = None


class GetExecutionRequest(BaseValidatorModel):
    ExecutionId: str
    ExportArn: str


class GetExportRequest(BaseValidatorModel):
    ExportArn: str


class GetTableRequest(BaseValidatorModel):
    TableName: str
    TableProperties: Optional[Dict[str, str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListExecutionsRequest(BaseValidatorModel):
    ExportArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListExportsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTablesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class S3OutputConfigurations(BaseValidatorModel):
    Compression: CompressionOptionType
    Format: FormatOptionType
    OutputType: Literal['CUSTOM']
    Overwrite: OverwriteOptionType


class TablePropertyDescription(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    ValidValues: Optional[List[str]] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    ResourceTagKeys: List[str]


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    ResourceTags: List[ResourceTag]


class CreateExportResponse(BaseValidatorModel):
    ExportArn: str
    ResponseMetadata: ResponseMetadata


class DeleteExportResponse(BaseValidatorModel):
    ExportArn: str
    ResponseMetadata: ResponseMetadata


class GetTableResponse(BaseValidatorModel):
    Description: str
    Schema: List[Column]
    TableName: str
    TableProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    ResourceTags: List[ResourceTag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateExportResponse(BaseValidatorModel):
    ExportArn: str
    ResponseMetadata: ResponseMetadata


class ExecutionReference(BaseValidatorModel):
    ExecutionId: str
    ExecutionStatus: ExecutionStatus


class ExportReference(BaseValidatorModel):
    ExportArn: str
    ExportName: str
    ExportStatus: ExportStatus


class ListExecutionsRequestPaginate(BaseValidatorModel):
    ExportArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListExportsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTablesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class S3Destination(BaseValidatorModel):
    S3Bucket: str
    S3OutputConfigurations: S3OutputConfigurations
    S3Prefix: str
    S3Region: str


class Table(BaseValidatorModel):
    Description: Optional[str] = None
    TableName: Optional[str] = None
    TableProperties: Optional[List[TablePropertyDescription]] = None


class ListExecutionsResponse(BaseValidatorModel):
    Executions: List[ExecutionReference]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListExportsResponse(BaseValidatorModel):
    Exports: List[ExportReference]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DestinationConfigurations(BaseValidatorModel):
    S3Destination: S3Destination


class ListTablesResponse(BaseValidatorModel):
    Tables: List[Table]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ExportOutput(BaseValidatorModel):
    DataQuery: DataQueryOutput
    DestinationConfigurations: DestinationConfigurations
    Name: str
    RefreshCadence: RefreshCadence
    Description: Optional[str] = None
    ExportArn: Optional[str] = None


class Export(BaseValidatorModel):
    DataQuery: DataQuery
    DestinationConfigurations: DestinationConfigurations
    Name: str
    RefreshCadence: RefreshCadence
    Description: Optional[str] = None
    ExportArn: Optional[str] = None


class GetExecutionResponse(BaseValidatorModel):
    ExecutionId: str
    ExecutionStatus: ExecutionStatus
    Export: ExportOutput
    ResponseMetadata: ResponseMetadata


class GetExportResponse(BaseValidatorModel):
    Export: ExportOutput
    ExportStatus: ExportStatus
    ResponseMetadata: ResponseMetadata

ExportUnion = Union[Export, ExportOutput]


class CreateExportRequest(BaseValidatorModel):
    Export: ExportUnion
    ResourceTags: Optional[List[ResourceTag]] = None


class UpdateExportRequest(BaseValidatorModel):
    Export: ExportUnion
    ExportArn: str