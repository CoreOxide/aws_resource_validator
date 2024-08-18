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
from aws_resource_validator.pydantic_models.timestream_query_constants import *

class CancelQueryRequestRequestTypeDef(BaseValidatorModel):
    QueryId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ColumnInfoTypeDef(BaseValidatorModel):
    Type: "TypeTypeDef"
    Name: Optional[str] = None

class ScheduleConfigurationTypeDef(BaseValidatorModel):
    ScheduleExpression: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class RowTypeDef(BaseValidatorModel):
    Data: List["DatumTypeDef"]

class TimeSeriesDataPointTypeDef(BaseValidatorModel):
    Time: str
    Value: "DatumTypeDef"

class DeleteScheduledQueryRequestRequestTypeDef(BaseValidatorModel):
    ScheduledQueryArn: str

class EndpointTypeDef(BaseValidatorModel):
    Address: str
    CachePeriodInMinutes: int

class DescribeScheduledQueryRequestRequestTypeDef(BaseValidatorModel):
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

class ExecutionStatsTypeDef(BaseValidatorModel):
    ExecutionTimeInMillis: Optional[int] = None
    DataWrites: Optional[int] = None
    BytesMetered: Optional[int] = None
    CumulativeBytesScanned: Optional[int] = None
    RecordsIngested: Optional[int] = None
    QueryResultRows: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListScheduledQueriesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class MultiMeasureAttributeMappingTypeDef(BaseValidatorModel):
    SourceColumn: str
    MeasureValueType: ScalarMeasureValueTypeType
    TargetMultiMeasureAttributeName: Optional[str] = None

class SnsConfigurationTypeDef(BaseValidatorModel):
    TopicArn: str

class ParameterMappingTypeDef(BaseValidatorModel):
    Name: str
    Type: "TypeTypeDef"

class PrepareQueryRequestRequestTypeDef(BaseValidatorModel):
    QueryString: str
    ValidateOnly: Optional[bool] = None

class SelectColumnTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Type: Optional["TypeTypeDef"] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Aliased: Optional[bool] = None

class QueryRequestRequestTypeDef(BaseValidatorModel):
    QueryString: str
    ClientToken: Optional[str] = None
    NextToken: Optional[str] = None
    MaxRows: Optional[int] = None

class QueryStatusTypeDef(BaseValidatorModel):
    ProgressPercentage: Optional[float] = None
    CumulativeBytesScanned: Optional[int] = None
    CumulativeBytesMetered: Optional[int] = None

class TimestreamDestinationTypeDef(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None

class TypeTypeDef(BaseValidatorModel):
    ScalarType: Optional[ScalarTypeType] = None
    ArrayColumnInfo: Optional[Dict[str, Any]] = None
    TimeSeriesMeasureValueColumnInfo: Optional[Dict[str, Any]] = None
    RowColumnInfo: Optional[List[Dict[str, Any]]] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateAccountSettingsRequestRequestTypeDef(BaseValidatorModel):
    MaxQueryTCU: Optional[int] = None
    QueryPricingModel: Optional[QueryPricingModelType] = None

class UpdateScheduledQueryRequestRequestTypeDef(BaseValidatorModel):
    ScheduledQueryArn: str
    State: ScheduledQueryStateType

class CancelQueryResponseTypeDef(BaseValidatorModel):
    CancellationMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateScheduledQueryResponseTypeDef(BaseValidatorModel):
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAccountSettingsResponseTypeDef(BaseValidatorModel):
    MaxQueryTCU: int
    QueryPricingModel: QueryPricingModelType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountSettingsResponseTypeDef(BaseValidatorModel):
    MaxQueryTCU: int
    QueryPricingModel: QueryPricingModelType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class DatumTypeDef(BaseValidatorModel):
    ScalarValue: Optional[str] = None
    TimeSeriesValue: Optional[List[Dict[str, Any]]] = None
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

class ExecuteScheduledQueryRequestRequestTypeDef(BaseValidatorModel):
    ScheduledQueryArn: str
    InvocationTime: TimestampTypeDef
    ClientToken: Optional[str] = None

class ListScheduledQueriesRequestListScheduledQueriesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsForResourceRequestListTagsForResourcePaginateTypeDef(BaseValidatorModel):
    ResourceARN: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class QueryRequestQueryPaginateTypeDef(BaseValidatorModel):
    QueryString: str
    ClientToken: Optional[str] = None
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

class NotificationConfigurationTypeDef(BaseValidatorModel):
    SnsConfiguration: SnsConfigurationTypeDef

class PrepareQueryResponseTypeDef(BaseValidatorModel):
    QueryString: str
    Columns: List[SelectColumnTypeDef]
    Parameters: List[ParameterMappingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class QueryResponseTypeDef(BaseValidatorModel):
    QueryId: str
    Rows: List[RowTypeDef]
    ColumnInfo: List["ColumnInfoTypeDef"]
    QueryStatus: QueryStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TargetDestinationTypeDef(BaseValidatorModel):
    TimestreamDestination: Optional[TimestreamDestinationTypeDef] = None

class ScheduledQueryRunSummaryTypeDef(BaseValidatorModel):
    InvocationTime: Optional[datetime] = None
    TriggerTime: Optional[datetime] = None
    RunStatus: Optional[ScheduledQueryRunStatusType] = None
    ExecutionStats: Optional[ExecutionStatsTypeDef] = None
    ErrorReportLocation: Optional[ErrorReportLocationTypeDef] = None
    FailureReason: Optional[str] = None

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

class TargetConfigurationOutputTypeDef(BaseValidatorModel):
    TimestreamConfiguration: TimestreamConfigurationOutputTypeDef

class TargetConfigurationTypeDef(BaseValidatorModel):
    TimestreamConfiguration: TimestreamConfigurationTypeDef

class ListScheduledQueriesResponseTypeDef(BaseValidatorModel):
    ScheduledQueries: List[ScheduledQueryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

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

class CreateScheduledQueryRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeScheduledQueryResponseTypeDef(BaseValidatorModel):
    ScheduledQuery: ScheduledQueryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

