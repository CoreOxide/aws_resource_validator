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

class SnsConfigurationTypeDef(BaseValidatorModel):
    TopicArn: str


class CancelQueryRequestTypeDef(BaseValidatorModel):
    QueryId: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TypePaginatorTypeDef(BaseValidatorModel):
    ScalarType: Optional[ScalarTypeType] = None
    ArrayColumnInfo: Optional[Dict[str, Any]] = None
    TimeSeriesMeasureValueColumnInfo: Optional[Dict[str, Any]] = None
    RowColumnInfo: Optional[List[Dict[str, Any]]] = None


class ScheduleConfigurationTypeDef(BaseValidatorModel):
    ScheduleExpression: str


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class TimeSeriesDataPointPaginatorTypeDef(BaseValidatorModel):
    Time: str
    Value: Dict[str, Any]


class TimeSeriesDataPointTypeDef(BaseValidatorModel):
    Time: str
    Value: Dict[str, Any]


class DeleteScheduledQueryRequestTypeDef(BaseValidatorModel):
    ScheduledQueryArn: str


class EndpointTypeDef(BaseValidatorModel):
    Address: str
    CachePeriodInMinutes: int


class DescribeScheduledQueryRequestTypeDef(BaseValidatorModel):
    ScheduledQueryArn: str


class DimensionMappingTypeDef(BaseValidatorModel):
    Name: str
    DimensionValueType: Literal["VARCHAR"]


class S3ConfigurationTypeDef(BaseValidatorModel):
    BucketName: str
    ObjectKeyPrefix: Optional[str] = None
    EncryptionOption: Optional[S3EncryptionOptionType] = None


class S3ReportLocationTypeDef(BaseValidatorModel):
    BucketName: Optional[str] = None
    ObjectKey: Optional[str] = None


class ScheduledQueryInsightsTypeDef(BaseValidatorModel):
    Mode: ScheduledQueryInsightsModeType


class ExecutionStatsTypeDef(BaseValidatorModel):
    ExecutionTimeInMillis: Optional[int] = None
    DataWrites: Optional[int] = None
    BytesMetered: Optional[int] = None
    CumulativeBytesScanned: Optional[int] = None
    RecordsIngested: Optional[int] = None
    QueryResultRows: Optional[int] = None


class LastUpdateTypeDef(BaseValidatorModel):
    TargetQueryTCU: Optional[int] = None
    Status: Optional[LastUpdateStatusType] = None
    StatusMessage: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListScheduledQueriesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MultiMeasureAttributeMappingTypeDef(BaseValidatorModel):
    SourceColumn: str
    MeasureValueType: ScalarMeasureValueTypeType
    TargetMultiMeasureAttributeName: Optional[str] = None


class PrepareQueryRequestTypeDef(BaseValidatorModel):
    QueryString: str
    ValidateOnly: Optional[bool] = None


class QueryInsightsTypeDef(BaseValidatorModel):
    Mode: QueryInsightsModeType


class QueryStatusTypeDef(BaseValidatorModel):
    ProgressPercentage: Optional[float] = None
    CumulativeBytesScanned: Optional[int] = None
    CumulativeBytesMetered: Optional[int] = None


class QuerySpatialCoverageMaxTypeDef(BaseValidatorModel):
    Value: Optional[float] = None
    TableArn: Optional[str] = None
    PartitionKey: Optional[List[str]] = None


class QueryTemporalRangeMaxTypeDef(BaseValidatorModel):
    Value: Optional[int] = None
    TableArn: Optional[str] = None


class TimestreamDestinationTypeDef(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateScheduledQueryRequestTypeDef(BaseValidatorModel):
    ScheduledQueryArn: str
    State: ScheduledQueryStateType


class AccountSettingsNotificationConfigurationTypeDef(BaseValidatorModel):
    RoleArn: str
    SnsConfiguration: Optional[SnsConfigurationTypeDef] = None


class NotificationConfigurationTypeDef(BaseValidatorModel):
    SnsConfiguration: SnsConfigurationTypeDef


class CancelQueryResponseTypeDef(BaseValidatorModel):
    CancellationMessage: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateScheduledQueryResponseTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ColumnInfoTypeDef(BaseValidatorModel):
    pass


class TypeTypeDef(BaseValidatorModel):
    ScalarType: Optional[ScalarTypeType] = None
    ArrayColumnInfo: Optional[Dict[str, Any]] = None
    TimeSeriesMeasureValueColumnInfo: Optional[Dict[str, Any]] = None
    RowColumnInfo: Optional[List[ColumnInfoTypeDef]] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]


class DatumPaginatorTypeDef(BaseValidatorModel):
    ScalarValue: Optional[str] = None
    TimeSeriesValue: Optional[List[TimeSeriesDataPointPaginatorTypeDef]] = None
    ArrayValue: Optional[List[Dict[str, Any]]] = None
    RowValue: Optional[Dict[str, Any]] = None
    NullValue: Optional[bool] = None


class DatumTypeDef(BaseValidatorModel):
    ScalarValue: Optional[str] = None
    TimeSeriesValue: Optional[List[TimeSeriesDataPointTypeDef]] = None
    ArrayValue: Optional[List[Dict[str, Any]]] = None
    RowValue: Optional[Dict[str, Any]] = None
    NullValue: Optional[bool] = None


class DescribeEndpointsResponseTypeDef(BaseValidatorModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ErrorReportConfigurationTypeDef(BaseValidatorModel):
    S3Configuration: S3ConfigurationTypeDef


class ErrorReportLocationTypeDef(BaseValidatorModel):
    S3ReportLocation: Optional[S3ReportLocationTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class ExecuteScheduledQueryRequestTypeDef(BaseValidatorModel):
    ScheduledQueryArn: str
    InvocationTime: TimestampTypeDef
    ClientToken: Optional[str] = None
    QueryInsights: Optional[ScheduledQueryInsightsTypeDef] = None


class ListScheduledQueriesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsForResourceRequestPaginateTypeDef(BaseValidatorModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class MixedMeasureMappingOutputTypeDef(BaseValidatorModel):
    MeasureValueType: MeasureValueTypeType
    MeasureName: Optional[str] = None
    SourceColumn: Optional[str] = None
    TargetMeasureName: Optional[str] = None
    MultiMeasureAttributeMappings: Optional[List[MultiMeasureAttributeMappingTypeDef]] = None


class MixedMeasureMappingTypeDef(BaseValidatorModel):
    MeasureValueType: MeasureValueTypeType
    MeasureName: Optional[str] = None
    SourceColumn: Optional[str] = None
    TargetMeasureName: Optional[str] = None
    MultiMeasureAttributeMappings: Optional[Sequence[MultiMeasureAttributeMappingTypeDef]] = None


class MultiMeasureMappingsOutputTypeDef(BaseValidatorModel):
    MultiMeasureAttributeMappings: List[MultiMeasureAttributeMappingTypeDef]
    TargetMultiMeasureName: Optional[str] = None


class MultiMeasureMappingsTypeDef(BaseValidatorModel):
    MultiMeasureAttributeMappings: Sequence[MultiMeasureAttributeMappingTypeDef]
    TargetMultiMeasureName: Optional[str] = None


class QueryRequestPaginateTypeDef(BaseValidatorModel):
    QueryString: str
    ClientToken: Optional[str] = None
    QueryInsights: Optional[QueryInsightsTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class QueryRequestTypeDef(BaseValidatorModel):
    QueryString: str
    ClientToken: Optional[str] = None
    NextToken: Optional[str] = None
    MaxRows: Optional[int] = None
    QueryInsights: Optional[QueryInsightsTypeDef] = None


class QuerySpatialCoverageTypeDef(BaseValidatorModel):
    Max: Optional[QuerySpatialCoverageMaxTypeDef] = None


class QueryTemporalRangeTypeDef(BaseValidatorModel):
    Max: Optional[QueryTemporalRangeMaxTypeDef] = None


class TargetDestinationTypeDef(BaseValidatorModel):
    TimestreamDestination: Optional[TimestreamDestinationTypeDef] = None


class ProvisionedCapacityRequestTypeDef(BaseValidatorModel):
    TargetQueryTCU: int
    NotificationConfiguration: Optional[AccountSettingsNotificationConfigurationTypeDef] = None


class ProvisionedCapacityResponseTypeDef(BaseValidatorModel):
    ActiveQueryTCU: Optional[int] = None
    NotificationConfiguration: Optional[AccountSettingsNotificationConfigurationTypeDef] = None
    LastUpdate: Optional[LastUpdateTypeDef] = None


class RowPaginatorTypeDef(BaseValidatorModel):
    Data: List[DatumPaginatorTypeDef]


class RowTypeDef(BaseValidatorModel):
    Data: List[DatumTypeDef]


class TimestreamConfigurationOutputTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    TimeColumn: str
    DimensionMappings: List[DimensionMappingTypeDef]
    MultiMeasureMappings: Optional[MultiMeasureMappingsOutputTypeDef] = None
    MixedMeasureMappings: Optional[List[MixedMeasureMappingOutputTypeDef]] = None
    MeasureNameColumn: Optional[str] = None


class TimestreamConfigurationTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    TimeColumn: str
    DimensionMappings: Sequence[DimensionMappingTypeDef]
    MultiMeasureMappings: Optional[MultiMeasureMappingsTypeDef] = None
    MixedMeasureMappings: Optional[Sequence[MixedMeasureMappingTypeDef]] = None
    MeasureNameColumn: Optional[str] = None


class QueryInsightsResponseTypeDef(BaseValidatorModel):
    QuerySpatialCoverage: Optional[QuerySpatialCoverageTypeDef] = None
    QueryTemporalRange: Optional[QueryTemporalRangeTypeDef] = None
    QueryTableCount: Optional[int] = None
    OutputRows: Optional[int] = None
    OutputBytes: Optional[int] = None
    UnloadPartitionCount: Optional[int] = None
    UnloadWrittenRows: Optional[int] = None
    UnloadWrittenBytes: Optional[int] = None


class ScheduledQueryInsightsResponseTypeDef(BaseValidatorModel):
    QuerySpatialCoverage: Optional[QuerySpatialCoverageTypeDef] = None
    QueryTemporalRange: Optional[QueryTemporalRangeTypeDef] = None
    QueryTableCount: Optional[int] = None
    OutputRows: Optional[int] = None
    OutputBytes: Optional[int] = None


class ScheduledQueryTypeDef(BaseValidatorModel):
    Arn: str
    Name: str
    State: ScheduledQueryStateType
    CreationTime: Optional[datetime] = None
    PreviousInvocationTime: Optional[datetime] = None
    NextInvocationTime: Optional[datetime] = None
    ErrorReportConfiguration: Optional[ErrorReportConfigurationTypeDef] = None
    TargetDestination: Optional[TargetDestinationTypeDef] = None
    LastRunStatus: Optional[ScheduledQueryRunStatusType] = None


class QueryComputeRequestTypeDef(BaseValidatorModel):
    ComputeMode: Optional[ComputeModeType] = None
    ProvisionedCapacity: Optional[ProvisionedCapacityRequestTypeDef] = None


class QueryComputeResponseTypeDef(BaseValidatorModel):
    ComputeMode: Optional[ComputeModeType] = None
    ProvisionedCapacity: Optional[ProvisionedCapacityResponseTypeDef] = None


class SelectColumnTypeDef(BaseValidatorModel):
    pass


class ParameterMappingTypeDef(BaseValidatorModel):
    pass


class PrepareQueryResponseTypeDef(BaseValidatorModel):
    QueryString: str
    Columns: List[SelectColumnTypeDef]
    Parameters: List[ParameterMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TargetConfigurationOutputTypeDef(BaseValidatorModel):
    TimestreamConfiguration: TimestreamConfigurationOutputTypeDef


class TargetConfigurationTypeDef(BaseValidatorModel):
    TimestreamConfiguration: TimestreamConfigurationTypeDef


class ColumnInfoPaginatorTypeDef(BaseValidatorModel):
    pass


class QueryResponsePaginatorTypeDef(BaseValidatorModel):
    QueryId: str
    Rows: List[RowPaginatorTypeDef]
    ColumnInfo: List[ColumnInfoPaginatorTypeDef]
    QueryStatus: QueryStatusTypeDef
    QueryInsightsResponse: QueryInsightsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class QueryResponseTypeDef(BaseValidatorModel):
    QueryId: str
    Rows: List[RowTypeDef]
    ColumnInfo: List[ColumnInfoTypeDef]
    QueryStatus: QueryStatusTypeDef
    QueryInsightsResponse: QueryInsightsResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ScheduledQueryRunSummaryTypeDef(BaseValidatorModel):
    InvocationTime: Optional[datetime] = None
    TriggerTime: Optional[datetime] = None
    RunStatus: Optional[ScheduledQueryRunStatusType] = None
    ExecutionStats: Optional[ExecutionStatsTypeDef] = None
    QueryInsightsResponse: Optional[ScheduledQueryInsightsResponseTypeDef] = None
    ErrorReportLocation: Optional[ErrorReportLocationTypeDef] = None
    FailureReason: Optional[str] = None


class ListScheduledQueriesResponseTypeDef(BaseValidatorModel):
    ScheduledQueries: List[ScheduledQueryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateAccountSettingsRequestTypeDef(BaseValidatorModel):
    MaxQueryTCU: Optional[int] = None
    QueryPricingModel: Optional[QueryPricingModelType] = None
    QueryCompute: Optional[QueryComputeRequestTypeDef] = None


class DescribeAccountSettingsResponseTypeDef(BaseValidatorModel):
    MaxQueryTCU: int
    QueryPricingModel: QueryPricingModelType
    QueryCompute: QueryComputeResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAccountSettingsResponseTypeDef(BaseValidatorModel):
    MaxQueryTCU: int
    QueryPricingModel: QueryPricingModelType
    QueryCompute: QueryComputeResponseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ScheduledQueryDescriptionTypeDef(BaseValidatorModel):
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


class TargetConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateScheduledQueryRequestTypeDef(BaseValidatorModel):
    Name: str
    QueryString: str
    ScheduleConfiguration: ScheduleConfigurationTypeDef
    NotificationConfiguration: NotificationConfigurationTypeDef
    ScheduledQueryExecutionRoleArn: str
    ErrorReportConfiguration: ErrorReportConfigurationTypeDef
    TargetConfiguration: Optional[TargetConfigurationUnionTypeDef] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None


class DescribeScheduledQueryResponseTypeDef(BaseValidatorModel):
    ScheduledQuery: ScheduledQueryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


