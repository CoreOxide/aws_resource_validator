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
from aws_resource_validator.pydantic_models.timestream_query_constants import *

class CancelQueryRequestRequestTypeDef(BaseModel):
    QueryId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ColumnInfoTypeDef(BaseModel):
    Type: "TypeTypeDef"
    Name: Optional[str] = None

class ScheduleConfigurationTypeDef(BaseModel):
    ScheduleExpression: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class RowTypeDef(BaseModel):
    Data: List["DatumTypeDef"]

class TimeSeriesDataPointTypeDef(BaseModel):
    Time: str
    Value: "DatumTypeDef"

class DeleteScheduledQueryRequestRequestTypeDef(BaseModel):
    ScheduledQueryArn: str

class EndpointTypeDef(BaseModel):
    Address: str
    CachePeriodInMinutes: int

class DescribeScheduledQueryRequestRequestTypeDef(BaseModel):
    ScheduledQueryArn: str

class DimensionMappingTypeDef(BaseModel):
    Name: str
    DimensionValueType: Literal["VARCHAR"]

class S3ConfigurationTypeDef(BaseModel):
    BucketName: str
    ObjectKeyPrefix: Optional[str] = None
    EncryptionOption: Optional[S3EncryptionOptionType] = None

class S3ReportLocationTypeDef(BaseModel):
    BucketName: Optional[str] = None
    ObjectKey: Optional[str] = None

class ExecutionStatsTypeDef(BaseModel):
    ExecutionTimeInMillis: Optional[int] = None
    DataWrites: Optional[int] = None
    BytesMetered: Optional[int] = None
    CumulativeBytesScanned: Optional[int] = None
    RecordsIngested: Optional[int] = None
    QueryResultRows: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListScheduledQueriesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MultiMeasureAttributeMappingTypeDef(BaseModel):
    SourceColumn: str
    MeasureValueType: ScalarMeasureValueTypeType
    TargetMultiMeasureAttributeName: Optional[str] = None

class SnsConfigurationTypeDef(BaseModel):
    TopicArn: str

class ParameterMappingTypeDef(BaseModel):
    Name: str
    Type: "TypeTypeDef"

class PrepareQueryRequestRequestTypeDef(BaseModel):
    QueryString: str
    ValidateOnly: Optional[bool] = None

class SelectColumnTypeDef(BaseModel):
    Name: Optional[str] = None
    Type: Optional["TypeTypeDef"] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Aliased: Optional[bool] = None

class QueryRequestRequestTypeDef(BaseModel):
    QueryString: str
    ClientToken: Optional[str] = None
    NextToken: Optional[str] = None
    MaxRows: Optional[int] = None

class QueryStatusTypeDef(BaseModel):
    ProgressPercentage: Optional[float] = None
    CumulativeBytesScanned: Optional[int] = None
    CumulativeBytesMetered: Optional[int] = None

class TimestreamDestinationTypeDef(BaseModel):
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None

class TypeTypeDef(BaseModel):
    ScalarType: Optional[ScalarTypeType] = None
    ArrayColumnInfo: Optional[Dict[str, Any]] = None
    TimeSeriesMeasureValueColumnInfo: Optional[Dict[str, Any]] = None
    RowColumnInfo: Optional[List[Dict[str, Any]]] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateAccountSettingsRequestRequestTypeDef(BaseModel):
    MaxQueryTCU: Optional[int] = None
    QueryPricingModel: Optional[QueryPricingModelType] = None

class UpdateScheduledQueryRequestRequestTypeDef(BaseModel):
    ScheduledQueryArn: str
    State: ScheduledQueryStateType

class CancelQueryResponseTypeDef(BaseModel):
    CancellationMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScheduledQueryResponseTypeDef(BaseModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountSettingsResponseTypeDef(BaseModel):
    MaxQueryTCU: int
    QueryPricingModel: QueryPricingModelType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountSettingsResponseTypeDef(BaseModel):
    MaxQueryTCU: int
    QueryPricingModel: QueryPricingModelType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class DatumTypeDef(BaseModel):
    ScalarValue: Optional[str] = None
    TimeSeriesValue: Optional[List[Dict[str, Any]]] = None
    ArrayValue: Optional[List[Dict[str, Any]]] = None
    RowValue: Optional[Dict[str, Any]] = None
    NullValue: Optional[bool] = None

class DescribeEndpointsResponseTypeDef(BaseModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ErrorReportConfigurationTypeDef(BaseModel):
    S3Configuration: S3ConfigurationTypeDef

class ErrorReportLocationTypeDef(BaseModel):
    S3ReportLocation: Optional[S3ReportLocationTypeDef] = None

class ExecuteScheduledQueryRequestRequestTypeDef(BaseModel):
    ScheduledQueryArn: str
    InvocationTime: TimestampTypeDef
    ClientToken: Optional[str] = None

class ListScheduledQueriesRequestListScheduledQueriesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class QueryRequestQueryPaginateTypeDef(BaseModel):
    QueryString: str
    ClientToken: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class MixedMeasureMappingOutputTypeDef(BaseModel):
    MeasureValueType: MeasureValueTypeType
    MeasureName: Optional[str] = None
    SourceColumn: Optional[str] = None
    TargetMeasureName: Optional[str] = None
    MultiMeasureAttributeMappings: Optional[List[MultiMeasureAttributeMappingTypeDef]] = None

class MixedMeasureMappingTypeDef(BaseModel):
    MeasureValueType: MeasureValueTypeType
    MeasureName: Optional[str] = None
    SourceColumn: Optional[str] = None
    TargetMeasureName: Optional[str] = None
    MultiMeasureAttributeMappings: Optional[Sequence[MultiMeasureAttributeMappingTypeDef]] = None

class MultiMeasureMappingsOutputTypeDef(BaseModel):
    MultiMeasureAttributeMappings: List[MultiMeasureAttributeMappingTypeDef]
    TargetMultiMeasureName: Optional[str] = None

class MultiMeasureMappingsTypeDef(BaseModel):
    MultiMeasureAttributeMappings: Sequence[MultiMeasureAttributeMappingTypeDef]
    TargetMultiMeasureName: Optional[str] = None

class NotificationConfigurationTypeDef(BaseModel):
    SnsConfiguration: SnsConfigurationTypeDef

class PrepareQueryResponseTypeDef(BaseModel):
    QueryString: str
    Columns: List[SelectColumnTypeDef]
    Parameters: List[ParameterMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class QueryResponseTypeDef(BaseModel):
    QueryId: str
    Rows: List[RowTypeDef]
    ColumnInfo: List["ColumnInfoTypeDef"]
    QueryStatus: QueryStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TargetDestinationTypeDef(BaseModel):
    TimestreamDestination: Optional[TimestreamDestinationTypeDef] = None

class ScheduledQueryRunSummaryTypeDef(BaseModel):
    InvocationTime: Optional[datetime] = None
    TriggerTime: Optional[datetime] = None
    RunStatus: Optional[ScheduledQueryRunStatusType] = None
    ExecutionStats: Optional[ExecutionStatsTypeDef] = None
    ErrorReportLocation: Optional[ErrorReportLocationTypeDef] = None
    FailureReason: Optional[str] = None

class TimestreamConfigurationOutputTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    TimeColumn: str
    DimensionMappings: List[DimensionMappingTypeDef]
    MultiMeasureMappings: Optional[MultiMeasureMappingsOutputTypeDef] = None
    MixedMeasureMappings: Optional[List[MixedMeasureMappingOutputTypeDef]] = None
    MeasureNameColumn: Optional[str] = None

class TimestreamConfigurationTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    TimeColumn: str
    DimensionMappings: Sequence[DimensionMappingTypeDef]
    MultiMeasureMappings: Optional[MultiMeasureMappingsTypeDef] = None
    MixedMeasureMappings: Optional[Sequence[MixedMeasureMappingTypeDef]] = None
    MeasureNameColumn: Optional[str] = None

class ScheduledQueryTypeDef(BaseModel):
    Arn: str
    Name: str
    State: ScheduledQueryStateType
    CreationTime: Optional[datetime] = None
    PreviousInvocationTime: Optional[datetime] = None
    NextInvocationTime: Optional[datetime] = None
    ErrorReportConfiguration: Optional[ErrorReportConfigurationTypeDef] = None
    TargetDestination: Optional[TargetDestinationTypeDef] = None
    LastRunStatus: Optional[ScheduledQueryRunStatusType] = None

class TargetConfigurationOutputTypeDef(BaseModel):
    TimestreamConfiguration: TimestreamConfigurationOutputTypeDef

class TargetConfigurationTypeDef(BaseModel):
    TimestreamConfiguration: TimestreamConfigurationTypeDef

class ListScheduledQueriesResponseTypeDef(BaseModel):
    ScheduledQueries: List[ScheduledQueryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ScheduledQueryDescriptionTypeDef(BaseModel):
    Arn: str
    Name: str
    QueryString: str
    State: ScheduledQueryStateType
    ScheduleConfiguration: ScheduleConfigurationTypeDef
    NotificationConfiguration: NotificationConfigurationTypeDef
    CreationTime: Optional[datetime] = None
    PreviousInvocationTime: Optional[datetime] = None
    NextInvocationTime: Optional[datetime] = None
    TargetConfiguration: Optional[TargetConfigurationOutputTypeDef] = None
    ScheduledQueryExecutionRoleArn: Optional[str] = None
    KmsKeyId: Optional[str] = None
    ErrorReportConfiguration: Optional[ErrorReportConfigurationTypeDef] = None
    LastRunSummary: Optional[ScheduledQueryRunSummaryTypeDef] = None
    RecentlyFailedRuns: Optional[List[ScheduledQueryRunSummaryTypeDef]] = None

class CreateScheduledQueryRequestRequestTypeDef(BaseModel):
    Name: str
    QueryString: str
    ScheduleConfiguration: ScheduleConfigurationTypeDef
    NotificationConfiguration: NotificationConfigurationTypeDef
    ScheduledQueryExecutionRoleArn: str
    ErrorReportConfiguration: ErrorReportConfigurationTypeDef
    TargetConfiguration: Optional[TargetConfigurationTypeDef] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None

class DescribeScheduledQueryResponseTypeDef(BaseModel):
    ScheduledQuery: ScheduledQueryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

