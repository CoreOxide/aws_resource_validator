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
from aws_resource_validator.pydantic_models.timestream_query_constants import *

class SnsConfiguration(BaseValidatorModel):
    TopicArn: str


class CancelQueryRequest(BaseValidatorModel):
    QueryId: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TypePaginator(BaseValidatorModel):
    ScalarType: Optional[ScalarTypeType] = None
    ArrayColumnInfo: Optional[Dict[str, Any]] = None
    TimeSeriesMeasureValueColumnInfo: Optional[Dict[str, Any]] = None
    RowColumnInfo: Optional[List[Dict[str, Any]]] = None


class ScheduleConfiguration(BaseValidatorModel):
    ScheduleExpression: str


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class TimeSeriesDataPointPaginator(BaseValidatorModel):
    Time: str
    Value: Dict[str, Any]


class TimeSeriesDataPoint(BaseValidatorModel):
    Time: str
    Value: Dict[str, Any]


class DeleteScheduledQueryRequest(BaseValidatorModel):
    ScheduledQueryArn: str


class Endpoint(BaseValidatorModel):
    Address: str
    CachePeriodInMinutes: int


class DescribeScheduledQueryRequest(BaseValidatorModel):
    ScheduledQueryArn: str


class DimensionMapping(BaseValidatorModel):
    Name: str
    DimensionValueType: Literal["VARCHAR"]


class S3Configuration(BaseValidatorModel):
    BucketName: str
    ObjectKeyPrefix: Optional[str] = None
    EncryptionOption: Optional[S3EncryptionOptionType] = None


class S3ReportLocation(BaseValidatorModel):
    BucketName: Optional[str] = None
    ObjectKey: Optional[str] = None


class ScheduledQueryInsights(BaseValidatorModel):
    Mode: ScheduledQueryInsightsModeType


class ExecutionStats(BaseValidatorModel):
    ExecutionTimeInMillis: Optional[int] = None
    DataWrites: Optional[int] = None
    BytesMetered: Optional[int] = None
    CumulativeBytesScanned: Optional[int] = None
    RecordsIngested: Optional[int] = None
    QueryResultRows: Optional[int] = None


class LastUpdate(BaseValidatorModel):
    TargetQueryTCU: Optional[int] = None
    Status: Optional[LastUpdateStatusType] = None
    StatusMessage: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListScheduledQueriesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MultiMeasureAttributeMapping(BaseValidatorModel):
    SourceColumn: str
    MeasureValueType: ScalarMeasureValueTypeType
    TargetMultiMeasureAttributeName: Optional[str] = None


class PrepareQueryRequest(BaseValidatorModel):
    QueryString: str
    ValidateOnly: Optional[bool] = None


class QueryInsights(BaseValidatorModel):
    Mode: QueryInsightsModeType


class QueryStatus(BaseValidatorModel):
    ProgressPercentage: Optional[float] = None
    CumulativeBytesScanned: Optional[int] = None
    CumulativeBytesMetered: Optional[int] = None


class QuerySpatialCoverageMax(BaseValidatorModel):
    Value: Optional[float] = None
    TableArn: Optional[str] = None
    PartitionKey: Optional[List[str]] = None


class QueryTemporalRangeMax(BaseValidatorModel):
    Value: Optional[int] = None
    TableArn: Optional[str] = None


class TimestreamDestination(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateScheduledQueryRequest(BaseValidatorModel):
    ScheduledQueryArn: str
    State: ScheduledQueryStateType


class AccountSettingsNotificationConfiguration(BaseValidatorModel):
    RoleArn: str
    SnsConfiguration: Optional[SnsConfiguration] = None


class NotificationConfiguration(BaseValidatorModel):
    SnsConfiguration: SnsConfiguration


class CancelQueryResponse(BaseValidatorModel):
    CancellationMessage: str
    ResponseMetadata: ResponseMetadata


class CreateScheduledQueryResponse(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ColumnInfo(BaseValidatorModel):
    pass


class Type(BaseValidatorModel):
    ScalarType: Optional[ScalarTypeType] = None
    ArrayColumnInfo: Optional[Dict[str, Any]] = None
    TimeSeriesMeasureValueColumnInfo: Optional[Dict[str, Any]] = None
    RowColumnInfo: Optional[List[ColumnInfo]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class DatumPaginator(BaseValidatorModel):
    ScalarValue: Optional[str] = None
    TimeSeriesValue: Optional[List[TimeSeriesDataPointPaginator]] = None
    ArrayValue: Optional[List[Dict[str, Any]]] = None
    RowValue: Optional[Dict[str, Any]] = None
    NullValue: Optional[bool] = None


class Datum(BaseValidatorModel):
    ScalarValue: Optional[str] = None
    TimeSeriesValue: Optional[List[TimeSeriesDataPoint]] = None
    ArrayValue: Optional[List[Dict[str, Any]]] = None
    RowValue: Optional[Dict[str, Any]] = None
    NullValue: Optional[bool] = None


class DescribeEndpointsResponse(BaseValidatorModel):
    Endpoints: List[Endpoint]
    ResponseMetadata: ResponseMetadata


class ErrorReportConfiguration(BaseValidatorModel):
    S3Configuration: S3Configuration


class ErrorReportLocation(BaseValidatorModel):
    S3ReportLocation: Optional[S3ReportLocation] = None


class Timestamp(BaseValidatorModel):
    pass


class ExecuteScheduledQueryRequest(BaseValidatorModel):
    ScheduledQueryArn: str
    InvocationTime: Timestamp
    ClientToken: Optional[str] = None
    QueryInsights: Optional[ScheduledQueryInsights] = None


class ListScheduledQueriesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsForResourceRequestPaginate(BaseValidatorModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfig] = None


class MixedMeasureMappingOutput(BaseValidatorModel):
    MeasureValueType: MeasureValueTypeType
    MeasureName: Optional[str] = None
    SourceColumn: Optional[str] = None
    TargetMeasureName: Optional[str] = None
    MultiMeasureAttributeMappings: Optional[List[MultiMeasureAttributeMapping]] = None


class MixedMeasureMapping(BaseValidatorModel):
    MeasureValueType: MeasureValueTypeType
    MeasureName: Optional[str] = None
    SourceColumn: Optional[str] = None
    TargetMeasureName: Optional[str] = None
    MultiMeasureAttributeMappings: Optional[Sequence[MultiMeasureAttributeMapping]] = None


class MultiMeasureMappingsOutput(BaseValidatorModel):
    MultiMeasureAttributeMappings: List[MultiMeasureAttributeMapping]
    TargetMultiMeasureName: Optional[str] = None


class MultiMeasureMappings(BaseValidatorModel):
    MultiMeasureAttributeMappings: Sequence[MultiMeasureAttributeMapping]
    TargetMultiMeasureName: Optional[str] = None


class QueryRequestPaginate(BaseValidatorModel):
    QueryString: str
    ClientToken: Optional[str] = None
    QueryInsights: Optional[QueryInsights] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class QueryRequest(BaseValidatorModel):
    QueryString: str
    ClientToken: Optional[str] = None
    NextToken: Optional[str] = None
    MaxRows: Optional[int] = None
    QueryInsights: Optional[QueryInsights] = None


class QuerySpatialCoverage(BaseValidatorModel):
    Max: Optional[QuerySpatialCoverageMax] = None


class QueryTemporalRange(BaseValidatorModel):
    Max: Optional[QueryTemporalRangeMax] = None


class TargetDestination(BaseValidatorModel):
    TimestreamDestination: Optional[TimestreamDestination] = None


class ProvisionedCapacityRequest(BaseValidatorModel):
    TargetQueryTCU: int
    NotificationConfiguration: Optional[AccountSettingsNotificationConfiguration] = None


class ProvisionedCapacityResponse(BaseValidatorModel):
    ActiveQueryTCU: Optional[int] = None
    NotificationConfiguration: Optional[AccountSettingsNotificationConfiguration] = None
    LastUpdate: Optional[LastUpdate] = None


class RowPaginator(BaseValidatorModel):
    Data: List[DatumPaginator]


class Row(BaseValidatorModel):
    Data: List[Datum]


class TimestreamConfigurationOutput(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    TimeColumn: str
    DimensionMappings: List[DimensionMapping]
    MultiMeasureMappings: Optional[MultiMeasureMappingsOutput] = None
    MixedMeasureMappings: Optional[List[MixedMeasureMappingOutput]] = None
    MeasureNameColumn: Optional[str] = None


class TimestreamConfiguration(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    TimeColumn: str
    DimensionMappings: Sequence[DimensionMapping]
    MultiMeasureMappings: Optional[MultiMeasureMappings] = None
    MixedMeasureMappings: Optional[Sequence[MixedMeasureMapping]] = None
    MeasureNameColumn: Optional[str] = None


class QueryInsightsResponse(BaseValidatorModel):
    QuerySpatialCoverage: Optional[QuerySpatialCoverage] = None
    QueryTemporalRange: Optional[QueryTemporalRange] = None
    QueryTableCount: Optional[int] = None
    OutputRows: Optional[int] = None
    OutputBytes: Optional[int] = None
    UnloadPartitionCount: Optional[int] = None
    UnloadWrittenRows: Optional[int] = None
    UnloadWrittenBytes: Optional[int] = None


class ScheduledQueryInsightsResponse(BaseValidatorModel):
    QuerySpatialCoverage: Optional[QuerySpatialCoverage] = None
    QueryTemporalRange: Optional[QueryTemporalRange] = None
    QueryTableCount: Optional[int] = None
    OutputRows: Optional[int] = None
    OutputBytes: Optional[int] = None


class ScheduledQuery(BaseValidatorModel):
    Arn: str
    Name: str
    State: ScheduledQueryStateType
    CreationTime: Optional[datetime] = None
    PreviousInvocationTime: Optional[datetime] = None
    NextInvocationTime: Optional[datetime] = None
    ErrorReportConfiguration: Optional[ErrorReportConfiguration] = None
    TargetDestination: Optional[TargetDestination] = None
    LastRunStatus: Optional[ScheduledQueryRunStatusType] = None


class QueryComputeRequest(BaseValidatorModel):
    ComputeMode: Optional[ComputeModeType] = None
    ProvisionedCapacity: Optional[ProvisionedCapacityRequest] = None


class QueryComputeResponse(BaseValidatorModel):
    ComputeMode: Optional[ComputeModeType] = None
    ProvisionedCapacity: Optional[ProvisionedCapacityResponse] = None


class SelectColumn(BaseValidatorModel):
    pass


class ParameterMapping(BaseValidatorModel):
    pass


class PrepareQueryResponse(BaseValidatorModel):
    QueryString: str
    Columns: List[SelectColumn]
    Parameters: List[ParameterMapping]
    ResponseMetadata: ResponseMetadata


class TargetConfigurationOutput(BaseValidatorModel):
    TimestreamConfiguration: TimestreamConfigurationOutput


class TargetConfiguration(BaseValidatorModel):
    TimestreamConfiguration: TimestreamConfiguration


class ColumnInfoPaginator(BaseValidatorModel):
    pass


class QueryResponsePaginator(BaseValidatorModel):
    QueryId: str
    Rows: List[RowPaginator]
    ColumnInfo: List[ColumnInfoPaginator]
    QueryStatus: QueryStatus
    QueryInsightsResponse: QueryInsightsResponse
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class QueryResponse(BaseValidatorModel):
    QueryId: str
    Rows: List[Row]
    ColumnInfo: List[ColumnInfo]
    QueryStatus: QueryStatus
    QueryInsightsResponse: QueryInsightsResponse
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ScheduledQueryRunSummary(BaseValidatorModel):
    InvocationTime: Optional[datetime] = None
    TriggerTime: Optional[datetime] = None
    RunStatus: Optional[ScheduledQueryRunStatusType] = None
    ExecutionStats: Optional[ExecutionStats] = None
    QueryInsightsResponse: Optional[ScheduledQueryInsightsResponse] = None
    ErrorReportLocation: Optional[ErrorReportLocation] = None
    FailureReason: Optional[str] = None


class ListScheduledQueriesResponse(BaseValidatorModel):
    ScheduledQueries: List[ScheduledQuery]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateAccountSettingsRequest(BaseValidatorModel):
    MaxQueryTCU: Optional[int] = None
    QueryPricingModel: Optional[QueryPricingModelType] = None
    QueryCompute: Optional[QueryComputeRequest] = None


class DescribeAccountSettingsResponse(BaseValidatorModel):
    MaxQueryTCU: int
    QueryPricingModel: QueryPricingModelType
    QueryCompute: QueryComputeResponse
    ResponseMetadata: ResponseMetadata


class UpdateAccountSettingsResponse(BaseValidatorModel):
    MaxQueryTCU: int
    QueryPricingModel: QueryPricingModelType
    QueryCompute: QueryComputeResponse
    ResponseMetadata: ResponseMetadata


class ScheduledQueryDescription(BaseValidatorModel):
    Arn: str
    Name: str
    QueryString: str
    State: ScheduledQueryStateType
    ScheduleConfiguration: ScheduleConfiguration
    NotificationConfiguration: NotificationConfiguration
    CreationTime: Optional[datetime] = None
    PreviousInvocationTime: Optional[datetime] = None
    NextInvocationTime: Optional[datetime] = None
    TargetConfiguration: Optional[TargetConfigurationOutput] = None
    ScheduledQueryExecutionRoleArn: Optional[str] = None
    KmsKeyId: Optional[str] = None
    ErrorReportConfiguration: Optional[ErrorReportConfiguration] = None
    LastRunSummary: Optional[ScheduledQueryRunSummary] = None
    RecentlyFailedRuns: Optional[List[ScheduledQueryRunSummary]] = None


class TargetConfigurationUnion(BaseValidatorModel):
    pass


class CreateScheduledQueryRequest(BaseValidatorModel):
    Name: str
    QueryString: str
    ScheduleConfiguration: ScheduleConfiguration
    NotificationConfiguration: NotificationConfiguration
    ScheduledQueryExecutionRoleArn: str
    ErrorReportConfiguration: ErrorReportConfiguration
    TargetConfiguration: Optional[TargetConfigurationUnion] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    KmsKeyId: Optional[str] = None


class DescribeScheduledQueryResponse(BaseValidatorModel):
    ScheduledQuery: ScheduledQueryDescription
    ResponseMetadata: ResponseMetadata


