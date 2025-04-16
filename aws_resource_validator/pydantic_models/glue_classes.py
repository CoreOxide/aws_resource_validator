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
from aws_resource_validator.pydantic_models.glue_constants import *

class NotificationProperty(BaseValidatorModel):
    NotifyDelayAfter: Optional[int] = None


class AggregateOperationOutput(BaseValidatorModel):
    Column: List[str]
    AggFunc: AggFunctionType


class AggregateOperation(BaseValidatorModel):
    Column: Sequence[str]
    AggFunc: AggFunctionType


class AllowedValue(BaseValidatorModel):
    Value: str
    Description: Optional[str] = None


class AmazonRedshiftAdvancedOption(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class Option(BaseValidatorModel):
    Value: Optional[str] = None
    Label: Optional[str] = None
    Description: Optional[str] = None


class AnnotationError(BaseValidatorModel):
    ProfileId: Optional[str] = None
    StatisticId: Optional[str] = None
    FailureReason: Optional[str] = None


class MappingOutput(BaseValidatorModel):
    ToKey: Optional[str] = None
    FromPath: Optional[List[str]] = None
    FromType: Optional[str] = None
    ToType: Optional[str] = None
    Dropped: Optional[bool] = None
    Children: Optional[List[Dict[str, Any]]] = None


class MappingPaginator(BaseValidatorModel):
    ToKey: Optional[str] = None
    FromPath: Optional[List[str]] = None
    FromType: Optional[str] = None
    ToType: Optional[str] = None
    Dropped: Optional[bool] = None
    Children: Optional[List[Dict[str, Any]]] = None


class AuditContext(BaseValidatorModel):
    AdditionalAuditContext: Optional[str] = None
    RequestedColumns: Optional[Sequence[str]] = None
    AllColumnsRequested: Optional[bool] = None


class BasicAuthenticationCredentials(BaseValidatorModel):
    Username: Optional[str] = None
    Password: Optional[str] = None


class AuthorizationCodeProperties(BaseValidatorModel):
    AuthorizationCode: Optional[str] = None
    RedirectUri: Optional[str] = None


class PartitionValueListOutput(BaseValidatorModel):
    Values: List[str]


class BasicCatalogTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str
    PartitionKeys: Optional[List[List[str]]] = None


class BasicCatalogTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDeleteConnectionRequest(BaseValidatorModel):
    ConnectionNameList: Sequence[str]
    CatalogId: Optional[str] = None


class ErrorDetail(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class BatchDeleteTableRequest(BaseValidatorModel):
    DatabaseName: str
    TablesToDelete: Sequence[str]
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None


class BatchDeleteTableVersionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    VersionIds: Sequence[str]
    CatalogId: Optional[str] = None


class BatchGetBlueprintsRequest(BaseValidatorModel):
    Names: Sequence[str]
    IncludeBlueprint: Optional[bool] = None
    IncludeParameterSpec: Optional[bool] = None


class BatchGetCrawlersRequest(BaseValidatorModel):
    CrawlerNames: Sequence[str]


class BatchGetCustomEntityTypesRequest(BaseValidatorModel):
    Names: Sequence[str]


class CustomEntityType(BaseValidatorModel):
    Name: str
    RegexString: str
    ContextWords: Optional[List[str]] = None


class BatchGetDataQualityResultRequest(BaseValidatorModel):
    ResultIds: Sequence[str]


class BatchGetDevEndpointsRequest(BaseValidatorModel):
    DevEndpointNames: Sequence[str]


class DevEndpoint(BaseValidatorModel):
    EndpointName: Optional[str] = None
    RoleArn: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    SubnetId: Optional[str] = None
    YarnEndpointAddress: Optional[str] = None
    PrivateAddress: Optional[str] = None
    ZeppelinRemoteSparkInterpreterPort: Optional[int] = None
    PublicAddress: Optional[str] = None
    Status: Optional[str] = None
    WorkerType: Optional[WorkerTypeType] = None
    GlueVersion: Optional[str] = None
    NumberOfWorkers: Optional[int] = None
    NumberOfNodes: Optional[int] = None
    AvailabilityZone: Optional[str] = None
    VpcId: Optional[str] = None
    ExtraPythonLibsS3Path: Optional[str] = None
    ExtraJarsS3Path: Optional[str] = None
    FailureReason: Optional[str] = None
    LastUpdateStatus: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastModifiedTimestamp: Optional[datetime] = None
    PublicKey: Optional[str] = None
    PublicKeys: Optional[List[str]] = None
    SecurityConfiguration: Optional[str] = None
    Arguments: Optional[Dict[str, str]] = None


class BatchGetJobsRequest(BaseValidatorModel):
    JobNames: Sequence[str]


class BatchGetTriggersRequest(BaseValidatorModel):
    TriggerNames: Sequence[str]


class BatchGetWorkflowsRequest(BaseValidatorModel):
    Names: Sequence[str]
    IncludeGraph: Optional[bool] = None


class DatapointInclusionAnnotation(BaseValidatorModel):
    ProfileId: Optional[str] = None
    StatisticId: Optional[str] = None
    InclusionAnnotation: Optional[InclusionAnnotationValueType] = None


class BatchStopJobRunRequest(BaseValidatorModel):
    JobName: str
    JobRunIds: Sequence[str]


class BatchStopJobRunSuccessfulSubmission(BaseValidatorModel):
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None


class BinaryColumnStatisticsData(BaseValidatorModel):
    MaximumLength: int
    AverageLength: float
    NumberOfNulls: int


class BlueprintDetails(BaseValidatorModel):
    BlueprintName: Optional[str] = None
    RunId: Optional[str] = None


class BlueprintRun(BaseValidatorModel):
    BlueprintName: Optional[str] = None
    RunId: Optional[str] = None
    WorkflowName: Optional[str] = None
    State: Optional[BlueprintRunStateType] = None
    StartedOn: Optional[datetime] = None
    CompletedOn: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    RollbackErrorMessage: Optional[str] = None
    Parameters: Optional[str] = None
    RoleArn: Optional[str] = None


class LastActiveDefinition(BaseValidatorModel):
    Description: Optional[str] = None
    LastModifiedOn: Optional[datetime] = None
    ParameterSpec: Optional[str] = None
    BlueprintLocation: Optional[str] = None
    BlueprintServiceLocation: Optional[str] = None


class BooleanColumnStatisticsData(BaseValidatorModel):
    NumberOfTrues: int
    NumberOfFalses: int
    NumberOfNulls: int


class CancelDataQualityRuleRecommendationRunRequest(BaseValidatorModel):
    RunId: str


class CancelDataQualityRulesetEvaluationRunRequest(BaseValidatorModel):
    RunId: str


class CancelMLTaskRunRequest(BaseValidatorModel):
    TransformId: str
    TaskRunId: str


class CancelStatementRequest(BaseValidatorModel):
    SessionId: str
    Id: int
    RequestOrigin: Optional[str] = None


class Capabilities(BaseValidatorModel):
    SupportedAuthenticationTypes: List[AuthenticationTypeType]
    SupportedDataOperations: List[DataOperationType]
    SupportedComputeEnvironments: List[ComputeEnvironmentType]


class CatalogEntry(BaseValidatorModel):
    DatabaseName: str
    TableName: str


class CatalogImportStatus(BaseValidatorModel):
    ImportCompleted: Optional[bool] = None
    ImportTime: Optional[datetime] = None
    ImportedBy: Optional[str] = None


class FederatedCatalog(BaseValidatorModel):
    Identifier: Optional[str] = None
    ConnectionName: Optional[str] = None


class TargetRedshiftCatalog(BaseValidatorModel):
    CatalogArn: str


class KafkaStreamingSourceOptionsOutput(BaseValidatorModel):
    BootstrapServers: Optional[str] = None
    SecurityProtocol: Optional[str] = None
    ConnectionName: Optional[str] = None
    TopicName: Optional[str] = None
    Assign: Optional[str] = None
    SubscribePattern: Optional[str] = None
    Classification: Optional[str] = None
    Delimiter: Optional[str] = None
    StartingOffsets: Optional[str] = None
    EndingOffsets: Optional[str] = None
    PollTimeoutMs: Optional[int] = None
    NumRetries: Optional[int] = None
    RetryIntervalMs: Optional[int] = None
    MaxOffsetsPerTrigger: Optional[int] = None
    MinPartitions: Optional[int] = None
    IncludeHeaders: Optional[bool] = None
    AddRecordTimestamp: Optional[str] = None
    EmitConsumerLagMetrics: Optional[str] = None
    StartingTimestamp: Optional[datetime] = None


class StreamingDataPreviewOptions(BaseValidatorModel):
    PollingTime: Optional[int] = None
    RecordPollingLimit: Optional[int] = None


class KinesisStreamingSourceOptionsOutput(BaseValidatorModel):
    EndpointUrl: Optional[str] = None
    StreamName: Optional[str] = None
    Classification: Optional[str] = None
    Delimiter: Optional[str] = None
    StartingPosition: Optional[StartingPositionType] = None
    MaxFetchTimeInMs: Optional[int] = None
    MaxFetchRecordsPerShard: Optional[int] = None
    MaxRecordPerRead: Optional[int] = None
    AddIdleTimeBetweenReads: Optional[bool] = None
    IdleTimeBetweenReadsInMs: Optional[int] = None
    DescribeShardInterval: Optional[int] = None
    NumRetries: Optional[int] = None
    RetryIntervalMs: Optional[int] = None
    MaxRetryIntervalMs: Optional[int] = None
    AvoidEmptyBatches: Optional[bool] = None
    StreamArn: Optional[str] = None
    RoleArn: Optional[str] = None
    RoleSessionName: Optional[str] = None
    AddRecordTimestamp: Optional[str] = None
    EmitConsumerLagMetrics: Optional[str] = None
    StartingTimestamp: Optional[datetime] = None


class DataLakeAccessPropertiesOutput(BaseValidatorModel):
    DataLakeAccess: Optional[bool] = None
    DataTransferRole: Optional[str] = None
    KmsKey: Optional[str] = None
    ManagedWorkgroupName: Optional[str] = None
    ManagedWorkgroupStatus: Optional[str] = None
    RedshiftDatabaseName: Optional[str] = None
    StatusMessage: Optional[str] = None
    CatalogType: Optional[str] = None


class DataLakeAccessProperties(BaseValidatorModel):
    DataLakeAccess: Optional[bool] = None
    DataTransferRole: Optional[str] = None
    KmsKey: Optional[str] = None
    CatalogType: Optional[str] = None


class CatalogSchemaChangePolicy(BaseValidatorModel):
    EnableUpdateCatalog: Optional[bool] = None
    UpdateBehavior: Optional[UpdateCatalogBehaviorType] = None


class CatalogSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class CatalogTargetOutput(BaseValidatorModel):
    DatabaseName: str
    Tables: List[str]
    ConnectionName: Optional[str] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None


class CatalogTarget(BaseValidatorModel):
    DatabaseName: str
    Tables: Sequence[str]
    ConnectionName: Optional[str] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None


class CheckSchemaVersionValidityInput(BaseValidatorModel):
    DataFormat: DataFormatType
    SchemaDefinition: str


class CsvClassifier(BaseValidatorModel):
    Name: str
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    Version: Optional[int] = None
    Delimiter: Optional[str] = None
    QuoteSymbol: Optional[str] = None
    ContainsHeader: Optional[CsvHeaderOptionType] = None
    Header: Optional[List[str]] = None
    DisableValueTrimming: Optional[bool] = None
    AllowSingleColumn: Optional[bool] = None
    CustomDatatypeConfigured: Optional[bool] = None
    CustomDatatypes: Optional[List[str]] = None
    Serde: Optional[CsvSerdeOptionType] = None


class GrokClassifier(BaseValidatorModel):
    Name: str
    Classification: str
    GrokPattern: str
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    Version: Optional[int] = None
    CustomPatterns: Optional[str] = None


class JsonClassifier(BaseValidatorModel):
    Name: str
    JsonPath: str
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    Version: Optional[int] = None


class XMLClassifier(BaseValidatorModel):
    Name: str
    Classification: str
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    Version: Optional[int] = None
    RowTag: Optional[str] = None


class CloudWatchEncryption(BaseValidatorModel):
    CloudWatchEncryptionMode: Optional[CloudWatchEncryptionModeType] = None
    KmsKeyArn: Optional[str] = None


class ConnectorDataTargetOutput(BaseValidatorModel):
    Name: str
    ConnectionType: str
    Data: Dict[str, str]
    Inputs: Optional[List[str]] = None


class DirectJDBCSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    ConnectionName: str
    ConnectionType: JDBCConnectionTypeType
    RedshiftTmpDir: Optional[str] = None


class DropDuplicatesOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Columns: Optional[List[List[str]]] = None


class DropFieldsOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]


class DynamoDBCatalogSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class FillMissingValuesOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    ImputedPath: str
    FilledPath: Optional[str] = None


class MergeOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Source: str
    PrimaryKeys: List[List[str]]


class MicrosoftSQLServerCatalogSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class MicrosoftSQLServerCatalogTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str


class MySQLCatalogSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class MySQLCatalogTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str


class OracleSQLCatalogSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class OracleSQLCatalogTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str


class PIIDetectionOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    PiiType: PiiTypeType
    EntityTypesToDetect: List[str]
    OutputColumnName: Optional[str] = None
    SampleFraction: Optional[float] = None
    ThresholdFraction: Optional[float] = None
    MaskValue: Optional[str] = None


class PostgreSQLCatalogSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class PostgreSQLCatalogTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str


class RedshiftSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    RedshiftTmpDir: Optional[str] = None
    TmpDirIAMRole: Optional[str] = None


class RelationalCatalogSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class RenameFieldOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    SourcePath: List[str]
    TargetPath: List[str]


class SelectFieldsOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]


class SelectFromCollectionOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Index: int


class SpigotOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    Topk: Optional[int] = None
    Prob: Optional[float] = None


class SplitFieldsOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]


class UnionOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    UnionType: UnionTypeType


class CodeGenEdge(BaseValidatorModel):
    Source: str
    Target: str
    TargetParameter: Optional[str] = None


class CodeGenNodeArg(BaseValidatorModel):
    Name: str
    Value: str
    Param: Optional[bool] = None


class ColumnImportance(BaseValidatorModel):
    ColumnName: Optional[str] = None
    Importance: Optional[float] = None


class ColumnRowFilter(BaseValidatorModel):
    ColumnName: Optional[str] = None
    RowFilterExpression: Optional[str] = None


class DateColumnStatisticsDataOutput(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[datetime] = None
    MaximumValue: Optional[datetime] = None


class DoubleColumnStatisticsData(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[float] = None
    MaximumValue: Optional[float] = None


class LongColumnStatisticsData(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[int] = None
    MaximumValue: Optional[int] = None


class StringColumnStatisticsData(BaseValidatorModel):
    MaximumLength: int
    AverageLength: float
    NumberOfNulls: int
    NumberOfDistinctValues: int


class ColumnStatisticsTaskRun(BaseValidatorModel):
    CustomerId: Optional[str] = None
    ColumnStatisticsTaskRunId: Optional[str] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    ColumnNameList: Optional[List[str]] = None
    CatalogID: Optional[str] = None
    Role: Optional[str] = None
    SampleSize: Optional[float] = None
    SecurityConfiguration: Optional[str] = None
    NumberOfWorkers: Optional[int] = None
    WorkerType: Optional[str] = None
    ComputationType: Optional[ComputationTypeType] = None
    Status: Optional[ColumnStatisticsStateType] = None
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    DPUSeconds: Optional[float] = None


class ExecutionAttempt(BaseValidatorModel):
    Status: Optional[ExecutionStatusType] = None
    ColumnStatisticsTaskRunId: Optional[str] = None
    ExecutionTimestamp: Optional[datetime] = None
    ErrorMessage: Optional[str] = None


class Schedule(BaseValidatorModel):
    ScheduleExpression: Optional[str] = None
    State: Optional[ScheduleStateType] = None


class IcebergCompactionMetrics(BaseValidatorModel):
    NumberOfBytesCompacted: Optional[int] = None
    NumberOfFilesCompacted: Optional[int] = None
    NumberOfDpus: Optional[int] = None
    JobDurationInHour: Optional[float] = None


class ConditionExpression(BaseValidatorModel):
    Condition: str
    TargetColumn: str
    Value: Optional[str] = None


class Condition(BaseValidatorModel):
    LogicalOperator: Optional[Literal["EQUALS"]] = None
    JobName: Optional[str] = None
    State: Optional[JobRunStateType] = None
    CrawlerName: Optional[str] = None
    CrawlState: Optional[CrawlStateType] = None


class ConfigurationObjectOutput(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    AllowedValues: Optional[List[str]] = None
    MinValue: Optional[str] = None
    MaxValue: Optional[str] = None


class ConfigurationObject(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    AllowedValues: Optional[Sequence[str]] = None
    MinValue: Optional[str] = None
    MaxValue: Optional[str] = None


class ConfusionMatrix(BaseValidatorModel):
    NumTruePositives: Optional[int] = None
    NumFalsePositives: Optional[int] = None
    NumTrueNegatives: Optional[int] = None
    NumFalseNegatives: Optional[int] = None


class ConnectionPasswordEncryption(BaseValidatorModel):
    ReturnConnectionPasswordEncrypted: bool
    AwsKmsKeyId: Optional[str] = None


class PhysicalConnectionRequirementsOutput(BaseValidatorModel):
    SubnetId: Optional[str] = None
    SecurityGroupIdList: Optional[List[str]] = None
    AvailabilityZone: Optional[str] = None


class ConnectionsListOutput(BaseValidatorModel):
    Connections: Optional[List[str]] = None


class ConnectionsList(BaseValidatorModel):
    Connections: Optional[Sequence[str]] = None


class ConnectorDataTarget(BaseValidatorModel):
    Name: str
    ConnectionType: str
    Data: Mapping[str, str]
    Inputs: Optional[Sequence[str]] = None


class Crawl(BaseValidatorModel):
    State: Optional[CrawlStateType] = None
    StartedOn: Optional[datetime] = None
    CompletedOn: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    LogGroup: Optional[str] = None
    LogStream: Optional[str] = None


class CrawlerHistory(BaseValidatorModel):
    CrawlId: Optional[str] = None
    State: Optional[CrawlerHistoryStateType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    Summary: Optional[str] = None
    ErrorMessage: Optional[str] = None
    LogGroup: Optional[str] = None
    LogStream: Optional[str] = None
    MessagePrefix: Optional[str] = None
    DPUHour: Optional[float] = None


class CrawlerMetrics(BaseValidatorModel):
    CrawlerName: Optional[str] = None
    TimeLeftSeconds: Optional[float] = None
    StillEstimating: Optional[bool] = None
    LastRuntimeSeconds: Optional[float] = None
    MedianRuntimeSeconds: Optional[float] = None
    TablesCreated: Optional[int] = None
    TablesUpdated: Optional[int] = None
    TablesDeleted: Optional[int] = None


class DeltaTargetOutput(BaseValidatorModel):
    DeltaTables: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    WriteManifest: Optional[bool] = None
    CreateNativeDeltaTable: Optional[bool] = None


class DynamoDBTarget(BaseValidatorModel):
    Path: Optional[str] = None
    scanAll: Optional[bool] = None
    scanRate: Optional[float] = None


class HudiTargetOutput(BaseValidatorModel):
    Paths: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    MaximumTraversalDepth: Optional[int] = None


class IcebergTargetOutput(BaseValidatorModel):
    Paths: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    MaximumTraversalDepth: Optional[int] = None


class JdbcTargetOutput(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    Path: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    EnableAdditionalMetadata: Optional[List[JdbcMetadataEntryType]] = None


class MongoDBTarget(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    Path: Optional[str] = None
    ScanAll: Optional[bool] = None


class S3TargetOutput(BaseValidatorModel):
    Path: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    SampleSize: Optional[int] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None


class DeltaTarget(BaseValidatorModel):
    DeltaTables: Optional[Sequence[str]] = None
    ConnectionName: Optional[str] = None
    WriteManifest: Optional[bool] = None
    CreateNativeDeltaTable: Optional[bool] = None


class HudiTarget(BaseValidatorModel):
    Paths: Optional[Sequence[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[Sequence[str]] = None
    MaximumTraversalDepth: Optional[int] = None


class IcebergTarget(BaseValidatorModel):
    Paths: Optional[Sequence[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[Sequence[str]] = None
    MaximumTraversalDepth: Optional[int] = None


class JdbcTarget(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    Path: Optional[str] = None
    Exclusions: Optional[Sequence[str]] = None
    EnableAdditionalMetadata: Optional[Sequence[JdbcMetadataEntryType]] = None


class S3Target(BaseValidatorModel):
    Path: Optional[str] = None
    Exclusions: Optional[Sequence[str]] = None
    ConnectionName: Optional[str] = None
    SampleSize: Optional[int] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None


class LakeFormationConfiguration(BaseValidatorModel):
    UseLakeFormationCredentials: Optional[bool] = None
    AccountId: Optional[str] = None


class LastCrawlInfo(BaseValidatorModel):
    Status: Optional[LastCrawlStatusType] = None
    ErrorMessage: Optional[str] = None
    LogGroup: Optional[str] = None
    LogStream: Optional[str] = None
    MessagePrefix: Optional[str] = None
    StartTime: Optional[datetime] = None


class LineageConfiguration(BaseValidatorModel):
    CrawlerLineageSettings: Optional[CrawlerLineageSettingsType] = None


class RecrawlPolicy(BaseValidatorModel):
    RecrawlBehavior: Optional[RecrawlBehaviorType] = None


class SchemaChangePolicy(BaseValidatorModel):
    UpdateBehavior: Optional[UpdateBehaviorType] = None
    DeleteBehavior: Optional[DeleteBehaviorType] = None


class CrawlsFilter(BaseValidatorModel):
    FieldName: Optional[FieldNameType] = None
    FilterOperator: Optional[FilterOperatorType] = None
    FieldValue: Optional[str] = None


class CreateBlueprintRequest(BaseValidatorModel):
    Name: str
    BlueprintLocation: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateCsvClassifierRequest(BaseValidatorModel):
    Name: str
    Delimiter: Optional[str] = None
    QuoteSymbol: Optional[str] = None
    ContainsHeader: Optional[CsvHeaderOptionType] = None
    Header: Optional[Sequence[str]] = None
    DisableValueTrimming: Optional[bool] = None
    AllowSingleColumn: Optional[bool] = None
    CustomDatatypeConfigured: Optional[bool] = None
    CustomDatatypes: Optional[Sequence[str]] = None
    Serde: Optional[CsvSerdeOptionType] = None


class CreateGrokClassifierRequest(BaseValidatorModel):
    Classification: str
    Name: str
    GrokPattern: str
    CustomPatterns: Optional[str] = None


class CreateJsonClassifierRequest(BaseValidatorModel):
    Name: str
    JsonPath: str


class CreateXMLClassifierRequest(BaseValidatorModel):
    Classification: str
    Name: str
    RowTag: Optional[str] = None


class CreateColumnStatisticsTaskSettingsRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    Role: str
    Schedule: Optional[str] = None
    ColumnNameList: Optional[Sequence[str]] = None
    SampleSize: Optional[float] = None
    CatalogID: Optional[str] = None
    SecurityConfiguration: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateCustomEntityTypeRequest(BaseValidatorModel):
    Name: str
    RegexString: str
    ContextWords: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None


class DataQualityTargetTable(BaseValidatorModel):
    TableName: str
    DatabaseName: str
    CatalogId: Optional[str] = None


class CreateDevEndpointRequest(BaseValidatorModel):
    EndpointName: str
    RoleArn: str
    SecurityGroupIds: Optional[Sequence[str]] = None
    SubnetId: Optional[str] = None
    PublicKey: Optional[str] = None
    PublicKeys: Optional[Sequence[str]] = None
    NumberOfNodes: Optional[int] = None
    WorkerType: Optional[WorkerTypeType] = None
    GlueVersion: Optional[str] = None
    NumberOfWorkers: Optional[int] = None
    ExtraPythonLibsS3Path: Optional[str] = None
    ExtraJarsS3Path: Optional[str] = None
    SecurityConfiguration: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    Arguments: Optional[Mapping[str, str]] = None


class Tag(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class SourceProcessingProperties(BaseValidatorModel):
    RoleArn: Optional[str] = None


class TargetProcessingProperties(BaseValidatorModel):
    RoleArn: Optional[str] = None
    KmsArn: Optional[str] = None
    ConnectionName: Optional[str] = None
    EventBusArn: Optional[str] = None


class IntegrationError(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class ExecutionProperty(BaseValidatorModel):
    MaxConcurrentRuns: Optional[int] = None


class JobCommand(BaseValidatorModel):
    Name: Optional[str] = None
    ScriptLocation: Optional[str] = None
    PythonVersion: Optional[str] = None
    Runtime: Optional[str] = None


class SourceControlDetails(BaseValidatorModel):
    Provider: Optional[SourceControlProviderType] = None
    Repository: Optional[str] = None
    Owner: Optional[str] = None
    Branch: Optional[str] = None
    Folder: Optional[str] = None
    LastCommitId: Optional[str] = None
    AuthStrategy: Optional[SourceControlAuthStrategyType] = None
    AuthToken: Optional[str] = None


class PartitionIndex(BaseValidatorModel):
    Keys: Sequence[str]
    IndexName: str


class CreateRegistryInput(BaseValidatorModel):
    RegistryName: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class RegistryId(BaseValidatorModel):
    RegistryName: Optional[str] = None
    RegistryArn: Optional[str] = None


class SessionCommand(BaseValidatorModel):
    Name: Optional[str] = None
    PythonVersion: Optional[str] = None


class EventBatchingCondition(BaseValidatorModel):
    BatchSize: int
    BatchWindow: Optional[int] = None


class CreateWorkflowRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    DefaultRunProperties: Optional[Mapping[str, str]] = None
    Tags: Optional[Mapping[str, str]] = None
    MaxConcurrentRuns: Optional[int] = None


class DQResultsPublishingOptions(BaseValidatorModel):
    EvaluationContext: Optional[str] = None
    ResultsS3Prefix: Optional[str] = None
    CloudWatchMetricsEnabled: Optional[bool] = None
    ResultsPublishingEnabled: Optional[bool] = None


class DQStopJobOnFailureOptions(BaseValidatorModel):
    StopJobOnFailureTiming: Optional[DQStopJobOnFailureTimingType] = None


class EncryptionAtRest(BaseValidatorModel):
    CatalogEncryptionMode: CatalogEncryptionModeType
    SseAwsKmsKeyId: Optional[str] = None
    CatalogEncryptionServiceRole: Optional[str] = None


class DataLakePrincipal(BaseValidatorModel):
    DataLakePrincipalIdentifier: Optional[str] = None


class DataQualityAnalyzerResult(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    EvaluationMessage: Optional[str] = None
    EvaluatedMetrics: Optional[Dict[str, float]] = None


class DataQualityEncryption(BaseValidatorModel):
    DataQualityEncryptionMode: Optional[DataQualityEncryptionModeType] = None
    KmsKeyArn: Optional[str] = None


class DataQualityEvaluationRunAdditionalRunOptions(BaseValidatorModel):
    CloudWatchMetricsEnabled: Optional[bool] = None
    ResultsS3Prefix: Optional[str] = None
    CompositeRuleEvaluationMethod: Optional[DQCompositeRuleEvaluationMethodType] = None


class DataQualityMetricValues(BaseValidatorModel):
    ActualValue: Optional[float] = None
    ExpectedValue: Optional[float] = None
    LowerLimit: Optional[float] = None
    UpperLimit: Optional[float] = None


class DataQualityRuleResult(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    EvaluationMessage: Optional[str] = None
    Result: Optional[DataQualityRuleResultStatusType] = None
    EvaluatedMetrics: Optional[Dict[str, float]] = None
    EvaluatedRule: Optional[str] = None


class GlueTableOutput(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    ConnectionName: Optional[str] = None
    AdditionalOptions: Optional[Dict[str, str]] = None


class DatabaseIdentifier(BaseValidatorModel):
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    Region: Optional[str] = None


class FederatedDatabase(BaseValidatorModel):
    Identifier: Optional[str] = None
    ConnectionName: Optional[str] = None


class Datatype(BaseValidatorModel):
    Id: str
    Label: str


class DecimalNumberOutput(BaseValidatorModel):
    UnscaledValue: bytes
    Scale: int


class DeleteBlueprintRequest(BaseValidatorModel):
    Name: str


class DeleteCatalogRequest(BaseValidatorModel):
    CatalogId: str


class DeleteClassifierRequest(BaseValidatorModel):
    Name: str


class DeleteColumnStatisticsForPartitionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnName: str
    CatalogId: Optional[str] = None


class DeleteColumnStatisticsForTableRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    ColumnName: str
    CatalogId: Optional[str] = None


class DeleteColumnStatisticsTaskSettingsRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str


class DeleteConnectionRequest(BaseValidatorModel):
    ConnectionName: str
    CatalogId: Optional[str] = None


class DeleteCrawlerRequest(BaseValidatorModel):
    Name: str


class DeleteCustomEntityTypeRequest(BaseValidatorModel):
    Name: str


class DeleteDataQualityRulesetRequest(BaseValidatorModel):
    Name: str


class DeleteDatabaseRequest(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None


class DeleteDevEndpointRequest(BaseValidatorModel):
    EndpointName: str


class DeleteIntegrationRequest(BaseValidatorModel):
    IntegrationIdentifier: str


class DeleteIntegrationTablePropertiesRequest(BaseValidatorModel):
    ResourceArn: str
    TableName: str


class DeleteJobRequest(BaseValidatorModel):
    JobName: str


class DeleteMLTransformRequest(BaseValidatorModel):
    TransformId: str


class DeletePartitionIndexRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    IndexName: str
    CatalogId: Optional[str] = None


class DeletePartitionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    CatalogId: Optional[str] = None


class DeleteResourcePolicyRequest(BaseValidatorModel):
    PolicyHashCondition: Optional[str] = None
    ResourceArn: Optional[str] = None


class SchemaId(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    RegistryName: Optional[str] = None


class DeleteSecurityConfigurationRequest(BaseValidatorModel):
    Name: str


class DeleteSessionRequest(BaseValidatorModel):
    Id: str
    RequestOrigin: Optional[str] = None


class DeleteTableRequest(BaseValidatorModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None


class DeleteTableVersionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    VersionId: str
    CatalogId: Optional[str] = None


class DeleteTriggerRequest(BaseValidatorModel):
    Name: str


class DeleteUsageProfileRequest(BaseValidatorModel):
    Name: str


class DeleteUserDefinedFunctionRequest(BaseValidatorModel):
    DatabaseName: str
    FunctionName: str
    CatalogId: Optional[str] = None


class DeleteWorkflowRequest(BaseValidatorModel):
    Name: str


class DescribeConnectionTypeRequest(BaseValidatorModel):
    ConnectionType: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeEntityRequest(BaseValidatorModel):
    ConnectionName: str
    EntityName: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    DataStoreApiVersion: Optional[str] = None


class Field(BaseValidatorModel):
    FieldName: Optional[str] = None
    Label: Optional[str] = None
    Description: Optional[str] = None
    FieldType: Optional[FieldDataTypeType] = None
    IsPrimaryKey: Optional[bool] = None
    IsNullable: Optional[bool] = None
    IsRetrievable: Optional[bool] = None
    IsFilterable: Optional[bool] = None
    IsPartitionable: Optional[bool] = None
    IsCreateable: Optional[bool] = None
    IsUpdateable: Optional[bool] = None
    IsUpsertable: Optional[bool] = None
    IsDefaultOnCreate: Optional[bool] = None
    SupportedValues: Optional[List[str]] = None
    SupportedFilterOperators: Optional[List[FieldFilterOperatorType]] = None
    ParentField: Optional[str] = None
    NativeDataType: Optional[str] = None
    CustomProperties: Optional[Dict[str, str]] = None


class DescribeInboundIntegrationsRequest(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    TargetArn: Optional[str] = None


class IntegrationFilter(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class DevEndpointCustomLibraries(BaseValidatorModel):
    ExtraPythonLibsS3Path: Optional[str] = None
    ExtraJarsS3Path: Optional[str] = None


class DirectSchemaChangePolicy(BaseValidatorModel):
    EnableUpdateCatalog: Optional[bool] = None
    UpdateBehavior: Optional[UpdateCatalogBehaviorType] = None
    Table: Optional[str] = None
    Database: Optional[str] = None


class DropDuplicates(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Columns: Optional[Sequence[Sequence[str]]] = None


class DropFields(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]


class NullCheckBoxList(BaseValidatorModel):
    IsEmpty: Optional[bool] = None
    IsNullString: Optional[bool] = None
    IsNegOne: Optional[bool] = None


class Edge(BaseValidatorModel):
    SourceId: Optional[str] = None
    DestinationId: Optional[str] = None


class JobBookmarksEncryption(BaseValidatorModel):
    JobBookmarksEncryptionMode: Optional[JobBookmarksEncryptionModeType] = None
    KmsKeyArn: Optional[str] = None


class S3Encryption(BaseValidatorModel):
    S3EncryptionMode: Optional[S3EncryptionModeType] = None
    KmsKeyArn: Optional[str] = None


class Entity(BaseValidatorModel):
    EntityName: Optional[str] = None
    Label: Optional[str] = None
    IsParentEntity: Optional[bool] = None
    Description: Optional[str] = None
    Category: Optional[str] = None
    CustomProperties: Optional[Dict[str, str]] = None


class ErrorDetails(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class ExportLabelsTaskRunProperties(BaseValidatorModel):
    OutputS3Path: Optional[str] = None


class FederatedTable(BaseValidatorModel):
    Identifier: Optional[str] = None
    DatabaseIdentifier: Optional[str] = None
    ConnectionName: Optional[str] = None


class FillMissingValues(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    ImputedPath: str
    FilledPath: Optional[str] = None


class FindMatchesParameters(BaseValidatorModel):
    PrimaryKeyColumnName: Optional[str] = None
    PrecisionRecallTradeoff: Optional[float] = None
    AccuracyCostTradeoff: Optional[float] = None
    EnforceProvidedLabels: Optional[bool] = None


class FindMatchesTaskRunProperties(BaseValidatorModel):
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None


class GetBlueprintRequest(BaseValidatorModel):
    Name: str
    IncludeBlueprint: Optional[bool] = None
    IncludeParameterSpec: Optional[bool] = None


class GetBlueprintRunRequest(BaseValidatorModel):
    BlueprintName: str
    RunId: str


class GetBlueprintRunsRequest(BaseValidatorModel):
    BlueprintName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetCatalogImportStatusRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None


class GetCatalogRequest(BaseValidatorModel):
    CatalogId: str


class GetCatalogsRequest(BaseValidatorModel):
    ParentCatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Recursive: Optional[bool] = None
    IncludeRoot: Optional[bool] = None


class GetClassifierRequest(BaseValidatorModel):
    Name: str


class GetClassifiersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetColumnStatisticsForPartitionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnNames: Sequence[str]
    CatalogId: Optional[str] = None


class GetColumnStatisticsForTableRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    ColumnNames: Sequence[str]
    CatalogId: Optional[str] = None


class GetColumnStatisticsTaskRunRequest(BaseValidatorModel):
    ColumnStatisticsTaskRunId: str


class GetColumnStatisticsTaskRunsRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetColumnStatisticsTaskSettingsRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str


class GetConnectionRequest(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None
    HidePassword: Optional[bool] = None
    ApplyOverrideForComputeEnvironment: Optional[ComputeEnvironmentType] = None


class GetConnectionsFilter(BaseValidatorModel):
    MatchCriteria: Optional[Sequence[str]] = None
    ConnectionType: Optional[ConnectionTypeType] = None
    ConnectionSchemaVersion: Optional[int] = None


class GetCrawlerMetricsRequest(BaseValidatorModel):
    CrawlerNameList: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetCrawlerRequest(BaseValidatorModel):
    Name: str


class GetCrawlersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetCustomEntityTypeRequest(BaseValidatorModel):
    Name: str


class GetDataCatalogEncryptionSettingsRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None


class GetDataQualityModelRequest(BaseValidatorModel):
    ProfileId: str
    StatisticId: Optional[str] = None


class GetDataQualityModelResultRequest(BaseValidatorModel):
    StatisticId: str
    ProfileId: str


class StatisticModelResult(BaseValidatorModel):
    LowerBound: Optional[float] = None
    UpperBound: Optional[float] = None
    PredictedValue: Optional[float] = None
    ActualValue: Optional[float] = None
    Date: Optional[datetime] = None
    InclusionAnnotation: Optional[InclusionAnnotationValueType] = None


class GetDataQualityResultRequest(BaseValidatorModel):
    ResultId: str


class GetDataQualityRuleRecommendationRunRequest(BaseValidatorModel):
    RunId: str


class GetDataQualityRulesetEvaluationRunRequest(BaseValidatorModel):
    RunId: str


class GetDataQualityRulesetRequest(BaseValidatorModel):
    Name: str


class GetDatabaseRequest(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None


class GetDatabasesRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    AttributesToGet: Optional[Sequence[Literal["NAME"]]] = None


class GetDataflowGraphRequest(BaseValidatorModel):
    PythonScript: Optional[str] = None


class GetDevEndpointRequest(BaseValidatorModel):
    EndpointName: str


class GetDevEndpointsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetEntityRecordsRequest(BaseValidatorModel):
    EntityName: str
    Limit: int
    ConnectionName: Optional[str] = None
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    DataStoreApiVersion: Optional[str] = None
    ConnectionOptions: Optional[Mapping[str, str]] = None
    FilterPredicate: Optional[str] = None
    OrderBy: Optional[str] = None
    SelectedFields: Optional[Sequence[str]] = None


class GetIntegrationResourcePropertyRequest(BaseValidatorModel):
    ResourceArn: str


class GetIntegrationTablePropertiesRequest(BaseValidatorModel):
    ResourceArn: str
    TableName: str


class SourceTableConfigOutput(BaseValidatorModel):
    Fields: Optional[List[str]] = None
    FilterPredicate: Optional[str] = None
    PrimaryKey: Optional[List[str]] = None
    RecordUpdateField: Optional[str] = None


class GetJobBookmarkRequest(BaseValidatorModel):
    JobName: str
    RunId: Optional[str] = None


class JobBookmarkEntry(BaseValidatorModel):
    JobName: Optional[str] = None
    Version: Optional[int] = None
    Run: Optional[int] = None
    Attempt: Optional[int] = None
    PreviousRunId: Optional[str] = None
    RunId: Optional[str] = None
    JobBookmark: Optional[str] = None


class GetJobRequest(BaseValidatorModel):
    JobName: str


class GetJobRunRequest(BaseValidatorModel):
    JobName: str
    RunId: str
    PredecessorsIncluded: Optional[bool] = None


class GetJobRunsRequest(BaseValidatorModel):
    JobName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetJobsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetMLTaskRunRequest(BaseValidatorModel):
    TransformId: str
    TaskRunId: str


class TaskRunSortCriteria(BaseValidatorModel):
    Column: TaskRunSortColumnTypeType
    SortDirection: SortDirectionTypeType


class GetMLTransformRequest(BaseValidatorModel):
    TransformId: str


class SchemaColumn(BaseValidatorModel):
    Name: Optional[str] = None
    DataType: Optional[str] = None


class TransformSortCriteria(BaseValidatorModel):
    Column: TransformSortColumnTypeType
    SortDirection: SortDirectionTypeType


class MappingEntry(BaseValidatorModel):
    SourceTable: Optional[str] = None
    SourcePath: Optional[str] = None
    SourceType: Optional[str] = None
    TargetTable: Optional[str] = None
    TargetPath: Optional[str] = None
    TargetType: Optional[str] = None


class GetPartitionIndexesRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None


class GetPartitionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    CatalogId: Optional[str] = None


class Segment(BaseValidatorModel):
    SegmentNumber: int
    TotalSegments: int


class GetResourcePoliciesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GluePolicy(BaseValidatorModel):
    PolicyInJson: Optional[str] = None
    PolicyHash: Optional[str] = None
    CreateTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None


class GetResourcePolicyRequest(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class SchemaVersionNumber(BaseValidatorModel):
    LatestVersion: Optional[bool] = None
    VersionNumber: Optional[int] = None


class GetSecurityConfigurationRequest(BaseValidatorModel):
    Name: str


class GetSecurityConfigurationsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetSessionRequest(BaseValidatorModel):
    Id: str
    RequestOrigin: Optional[str] = None


class GetStatementRequest(BaseValidatorModel):
    SessionId: str
    Id: int
    RequestOrigin: Optional[str] = None


class GetTableVersionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    VersionId: Optional[str] = None


class GetTableVersionsRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetTagsRequest(BaseValidatorModel):
    ResourceArn: str


class GetTriggerRequest(BaseValidatorModel):
    Name: str


class GetTriggersRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    DependentJobName: Optional[str] = None
    MaxResults: Optional[int] = None


class SupportedDialect(BaseValidatorModel):
    Dialect: Optional[ViewDialectType] = None
    DialectVersion: Optional[str] = None


class GetUsageProfileRequest(BaseValidatorModel):
    Name: str


class GetUserDefinedFunctionRequest(BaseValidatorModel):
    DatabaseName: str
    FunctionName: str
    CatalogId: Optional[str] = None


class GetWorkflowRequest(BaseValidatorModel):
    Name: str
    IncludeGraph: Optional[bool] = None


class GetWorkflowRunPropertiesRequest(BaseValidatorModel):
    Name: str
    RunId: str


class GetWorkflowRunRequest(BaseValidatorModel):
    Name: str
    RunId: str
    IncludeGraph: Optional[bool] = None


class GetWorkflowRunsRequest(BaseValidatorModel):
    Name: str
    IncludeGraph: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GlueTable(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    ConnectionName: Optional[str] = None
    AdditionalOptions: Optional[Mapping[str, str]] = None


class S3SourceAdditionalOptions(BaseValidatorModel):
    BoundedSize: Optional[int] = None
    BoundedFiles: Optional[int] = None


class IcebergInput(BaseValidatorModel):
    MetadataOperation: Literal["CREATE"]
    Version: Optional[str] = None


class IcebergOrphanFileDeletionConfiguration(BaseValidatorModel):
    orphanFileRetentionPeriodInDays: Optional[int] = None
    location: Optional[str] = None


class IcebergOrphanFileDeletionMetrics(BaseValidatorModel):
    NumberOfOrphanFilesDeleted: Optional[int] = None
    NumberOfDpus: Optional[int] = None
    JobDurationInHour: Optional[float] = None


class IcebergRetentionConfiguration(BaseValidatorModel):
    snapshotRetentionPeriodInDays: Optional[int] = None
    numberOfSnapshotsToRetain: Optional[int] = None
    cleanExpiredFiles: Optional[bool] = None


class IcebergRetentionMetrics(BaseValidatorModel):
    NumberOfDataFilesDeleted: Optional[int] = None
    NumberOfManifestFilesDeleted: Optional[int] = None
    NumberOfManifestListsDeleted: Optional[int] = None
    NumberOfDpus: Optional[int] = None
    JobDurationInHour: Optional[float] = None


class ImportCatalogToGlueRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None


class ImportLabelsTaskRunProperties(BaseValidatorModel):
    InputS3Path: Optional[str] = None
    Replace: Optional[bool] = None


class IntegrationPartition(BaseValidatorModel):
    FieldName: Optional[str] = None
    FunctionSpec: Optional[str] = None


class JDBCConnectorOptionsOutput(BaseValidatorModel):
    FilterPredicate: Optional[str] = None
    PartitionColumn: Optional[str] = None
    LowerBound: Optional[int] = None
    UpperBound: Optional[int] = None
    NumPartitions: Optional[int] = None
    JobBookmarkKeys: Optional[List[str]] = None
    JobBookmarkKeysSortOrder: Optional[str] = None
    DataTypeMapping: Optional[Dict[JDBCDataTypeType, GlueRecordTypeType]] = None


class JDBCConnectorOptions(BaseValidatorModel):
    FilterPredicate: Optional[str] = None
    PartitionColumn: Optional[str] = None
    LowerBound: Optional[int] = None
    UpperBound: Optional[int] = None
    NumPartitions: Optional[int] = None
    JobBookmarkKeys: Optional[Sequence[str]] = None
    JobBookmarkKeysSortOrder: Optional[str] = None
    DataTypeMapping: Optional[Mapping[JDBCDataTypeType, GlueRecordTypeType]] = None


class Predecessor(BaseValidatorModel):
    JobName: Optional[str] = None
    RunId: Optional[str] = None


class JoinColumnOutput(BaseValidatorModel):
    From: str
    Keys: List[List[str]]


class JoinColumn(BaseValidatorModel):
    From: str
    Keys: Sequence[Sequence[str]]


class LabelingSetGenerationTaskRunProperties(BaseValidatorModel):
    OutputS3Path: Optional[str] = None


class ListBlueprintsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class ListColumnStatisticsTaskRunsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListConnectionTypesRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCrawlersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ListCustomEntityTypesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class ListDevEndpointsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class ListEntitiesRequest(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    CatalogId: Optional[str] = None
    ParentEntityName: Optional[str] = None
    NextToken: Optional[str] = None
    DataStoreApiVersion: Optional[str] = None


class ListJobsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class ListRegistriesInput(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RegistryListItem(BaseValidatorModel):
    RegistryName: Optional[str] = None
    RegistryArn: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[RegistryStatusType] = None
    CreatedTime: Optional[str] = None
    UpdatedTime: Optional[str] = None


class SchemaVersionListItem(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    SchemaVersionId: Optional[str] = None
    VersionNumber: Optional[int] = None
    Status: Optional[SchemaVersionStatusType] = None
    CreatedTime: Optional[str] = None


class SchemaListItem(BaseValidatorModel):
    RegistryName: Optional[str] = None
    SchemaName: Optional[str] = None
    SchemaArn: Optional[str] = None
    Description: Optional[str] = None
    SchemaStatus: Optional[SchemaStatusType] = None
    CreatedTime: Optional[str] = None
    UpdatedTime: Optional[str] = None


class ListSessionsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None
    RequestOrigin: Optional[str] = None


class ListStatementsRequest(BaseValidatorModel):
    SessionId: str
    RequestOrigin: Optional[str] = None
    NextToken: Optional[str] = None


class ListTriggersRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    DependentJobName: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class ListUsageProfilesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class UsageProfileDefinition(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None


class ListWorkflowsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MLUserDataEncryption(BaseValidatorModel):
    MlUserDataEncryptionMode: MLUserDataEncryptionModeStringType
    KmsKeyId: Optional[str] = None


class MappingType(BaseValidatorModel):
    ToKey: Optional[str] = None
    FromPath: Optional[Sequence[str]] = None
    FromType: Optional[str] = None
    ToType: Optional[str] = None
    Dropped: Optional[bool] = None
    Children: Optional[Sequence[Mapping[str, Any]]] = None


class Merge(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Source: str
    PrimaryKeys: Sequence[Sequence[str]]


class OtherMetadataValueListItem(BaseValidatorModel):
    MetadataValue: Optional[str] = None
    CreatedTime: Optional[str] = None


class MetadataKeyValuePair(BaseValidatorModel):
    MetadataKey: Optional[str] = None
    MetadataValue: Optional[str] = None


class MicrosoftSQLServerCatalogTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str


class ModifyIntegrationRequest(BaseValidatorModel):
    IntegrationIdentifier: str
    Description: Optional[str] = None
    DataFilter: Optional[str] = None
    IntegrationName: Optional[str] = None


class MySQLCatalogTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str


class OAuth2ClientApplication(BaseValidatorModel):
    UserManagedClientApplicationClientId: Optional[str] = None
    AWSManagedClientApplicationReference: Optional[str] = None


class OAuth2Credentials(BaseValidatorModel):
    UserManagedClientApplicationClientSecret: Optional[str] = None
    AccessToken: Optional[str] = None
    RefreshToken: Optional[str] = None
    JwtToken: Optional[str] = None


class OracleSQLCatalogTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str


class Order(BaseValidatorModel):
    Column: str
    SortOrder: int


class PIIDetection(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    PiiType: PiiTypeType
    EntityTypesToDetect: Sequence[str]
    OutputColumnName: Optional[str] = None
    SampleFraction: Optional[float] = None
    ThresholdFraction: Optional[float] = None
    MaskValue: Optional[str] = None


class PartitionValueList(BaseValidatorModel):
    Values: Sequence[str]


class PhysicalConnectionRequirements(BaseValidatorModel):
    SubnetId: Optional[str] = None
    SecurityGroupIdList: Optional[Sequence[str]] = None
    AvailabilityZone: Optional[str] = None


class PostgreSQLCatalogTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str


class PropertyPredicate(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Comparator: Optional[ComparatorType] = None


class PutDataQualityProfileAnnotationRequest(BaseValidatorModel):
    ProfileId: str
    InclusionAnnotation: InclusionAnnotationValueType


class PutResourcePolicyRequest(BaseValidatorModel):
    PolicyInJson: str
    ResourceArn: Optional[str] = None
    PolicyHashCondition: Optional[str] = None
    PolicyExistsCondition: Optional[ExistConditionType] = None
    EnableHybrid: Optional[EnableHybridValuesType] = None


class PutWorkflowRunPropertiesRequest(BaseValidatorModel):
    Name: str
    RunId: str
    RunProperties: Mapping[str, str]


class RecipeActionOutput(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Dict[str, str]] = None


class RecipeAction(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Mapping[str, str]] = None


class RecipeReference(BaseValidatorModel):
    RecipeArn: str
    RecipeVersion: str


class UpsertRedshiftTargetOptionsOutput(BaseValidatorModel):
    TableLocation: Optional[str] = None
    ConnectionName: Optional[str] = None
    UpsertKeys: Optional[List[str]] = None


class RenameField(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    SourcePath: Sequence[str]
    TargetPath: Sequence[str]


class ResetJobBookmarkRequest(BaseValidatorModel):
    JobName: str
    RunId: Optional[str] = None


class ResourceUri(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Uri: Optional[str] = None


class ResumeWorkflowRunRequest(BaseValidatorModel):
    Name: str
    RunId: str
    NodeIds: Sequence[str]


class RunIdentifier(BaseValidatorModel):
    RunId: Optional[str] = None
    JobRunId: Optional[str] = None


class RunMetrics(BaseValidatorModel):
    NumberOfBytesCompacted: Optional[str] = None
    NumberOfFilesCompacted: Optional[str] = None
    NumberOfDpus: Optional[str] = None
    JobDurationInHour: Optional[str] = None


class RunStatementRequest(BaseValidatorModel):
    SessionId: str
    Code: str
    RequestOrigin: Optional[str] = None


class S3DirectSourceAdditionalOptions(BaseValidatorModel):
    BoundedSize: Optional[int] = None
    BoundedFiles: Optional[int] = None
    EnableSamplePath: Optional[bool] = None
    SamplePath: Optional[str] = None


class SortCriterion(BaseValidatorModel):
    FieldName: Optional[str] = None
    Sort: Optional[SortType] = None


class SelectFields(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]


class SelectFromCollection(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Index: int


class SerDeInfoOutput(BaseValidatorModel):
    Name: Optional[str] = None
    SerializationLibrary: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None


class SerDeInfo(BaseValidatorModel):
    Name: Optional[str] = None
    SerializationLibrary: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None


class SkewedInfoOutput(BaseValidatorModel):
    SkewedColumnNames: Optional[List[str]] = None
    SkewedColumnValues: Optional[List[str]] = None
    SkewedColumnValueLocationMaps: Optional[Dict[str, str]] = None


class SkewedInfo(BaseValidatorModel):
    SkewedColumnNames: Optional[Sequence[str]] = None
    SkewedColumnValues: Optional[Sequence[str]] = None
    SkewedColumnValueLocationMaps: Optional[Mapping[str, str]] = None


class SourceTableConfig(BaseValidatorModel):
    Fields: Optional[Sequence[str]] = None
    FilterPredicate: Optional[str] = None
    PrimaryKey: Optional[Sequence[str]] = None
    RecordUpdateField: Optional[str] = None


class SqlAlias(BaseValidatorModel):
    From: str
    Alias: str


class Spigot(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Topk: Optional[int] = None
    Prob: Optional[float] = None


class SplitFields(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]


class StartBlueprintRunRequest(BaseValidatorModel):
    BlueprintName: str
    RoleArn: str
    Parameters: Optional[str] = None


class StartColumnStatisticsTaskRunRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    Role: str
    ColumnNameList: Optional[Sequence[str]] = None
    SampleSize: Optional[float] = None
    CatalogID: Optional[str] = None
    SecurityConfiguration: Optional[str] = None


class StartColumnStatisticsTaskRunScheduleRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str


class StartCrawlerRequest(BaseValidatorModel):
    Name: str


class StartCrawlerScheduleRequest(BaseValidatorModel):
    CrawlerName: str


class StartExportLabelsTaskRunRequest(BaseValidatorModel):
    TransformId: str
    OutputS3Path: str


class StartImportLabelsTaskRunRequest(BaseValidatorModel):
    TransformId: str
    InputS3Path: str
    ReplaceAllLabels: Optional[bool] = None


class StartMLEvaluationTaskRunRequest(BaseValidatorModel):
    TransformId: str


class StartMLLabelingSetGenerationTaskRunRequest(BaseValidatorModel):
    TransformId: str
    OutputS3Path: str


class StartTriggerRequest(BaseValidatorModel):
    Name: str


class StartWorkflowRunRequest(BaseValidatorModel):
    Name: str
    RunProperties: Optional[Mapping[str, str]] = None


class StartingEventBatchCondition(BaseValidatorModel):
    BatchSize: Optional[int] = None
    BatchWindow: Optional[int] = None


class StatementOutputData(BaseValidatorModel):
    TextPlain: Optional[str] = None


class TimestampedInclusionAnnotation(BaseValidatorModel):
    Value: Optional[InclusionAnnotationValueType] = None
    LastModifiedOn: Optional[datetime] = None


class StopColumnStatisticsTaskRunRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str


class StopColumnStatisticsTaskRunScheduleRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str


class StopCrawlerRequest(BaseValidatorModel):
    Name: str


class StopCrawlerScheduleRequest(BaseValidatorModel):
    CrawlerName: str


class StopSessionRequest(BaseValidatorModel):
    Id: str
    RequestOrigin: Optional[str] = None


class StopTriggerRequest(BaseValidatorModel):
    Name: str


class StopWorkflowRunRequest(BaseValidatorModel):
    Name: str
    RunId: str


class TableIdentifier(BaseValidatorModel):
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    Name: Optional[str] = None
    Region: Optional[str] = None


class TableOptimizerVpcConfiguration(BaseValidatorModel):
    glueConnectionName: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagsToAdd: Mapping[str, str]


class Union(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    UnionType: UnionTypeType


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagsToRemove: Sequence[str]


class UpdateBlueprintRequest(BaseValidatorModel):
    Name: str
    BlueprintLocation: str
    Description: Optional[str] = None


class UpdateCsvClassifierRequest(BaseValidatorModel):
    Name: str
    Delimiter: Optional[str] = None
    QuoteSymbol: Optional[str] = None
    ContainsHeader: Optional[CsvHeaderOptionType] = None
    Header: Optional[Sequence[str]] = None
    DisableValueTrimming: Optional[bool] = None
    AllowSingleColumn: Optional[bool] = None
    CustomDatatypeConfigured: Optional[bool] = None
    CustomDatatypes: Optional[Sequence[str]] = None
    Serde: Optional[CsvSerdeOptionType] = None


class UpdateGrokClassifierRequest(BaseValidatorModel):
    Name: str
    Classification: Optional[str] = None
    GrokPattern: Optional[str] = None
    CustomPatterns: Optional[str] = None


class UpdateJsonClassifierRequest(BaseValidatorModel):
    Name: str
    JsonPath: Optional[str] = None


class UpdateXMLClassifierRequest(BaseValidatorModel):
    Name: str
    Classification: Optional[str] = None
    RowTag: Optional[str] = None


class UpdateColumnStatisticsTaskSettingsRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    Role: Optional[str] = None
    Schedule: Optional[str] = None
    ColumnNameList: Optional[Sequence[str]] = None
    SampleSize: Optional[float] = None
    CatalogID: Optional[str] = None
    SecurityConfiguration: Optional[str] = None


class UpdateCrawlerScheduleRequest(BaseValidatorModel):
    CrawlerName: str
    Schedule: Optional[str] = None


class UpdateDataQualityRulesetRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Ruleset: Optional[str] = None


class UpdateJobFromSourceControlRequest(BaseValidatorModel):
    JobName: Optional[str] = None
    Provider: Optional[SourceControlProviderType] = None
    RepositoryName: Optional[str] = None
    RepositoryOwner: Optional[str] = None
    BranchName: Optional[str] = None
    Folder: Optional[str] = None
    CommitId: Optional[str] = None
    AuthStrategy: Optional[SourceControlAuthStrategyType] = None
    AuthToken: Optional[str] = None


class UpdateSourceControlFromJobRequest(BaseValidatorModel):
    JobName: Optional[str] = None
    Provider: Optional[SourceControlProviderType] = None
    RepositoryName: Optional[str] = None
    RepositoryOwner: Optional[str] = None
    BranchName: Optional[str] = None
    Folder: Optional[str] = None
    CommitId: Optional[str] = None
    AuthStrategy: Optional[SourceControlAuthStrategyType] = None
    AuthToken: Optional[str] = None


class UpdateWorkflowRequest(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    DefaultRunProperties: Optional[Mapping[str, str]] = None
    MaxConcurrentRuns: Optional[int] = None


class UpsertRedshiftTargetOptions(BaseValidatorModel):
    TableLocation: Optional[str] = None
    ConnectionName: Optional[str] = None
    UpsertKeys: Optional[Sequence[str]] = None


class ViewRepresentationInput(BaseValidatorModel):
    Dialect: Optional[ViewDialectType] = None
    DialectVersion: Optional[str] = None
    ViewOriginalText: Optional[str] = None
    ValidationConnection: Optional[str] = None
    ViewExpandedText: Optional[str] = None


class ViewRepresentation(BaseValidatorModel):
    Dialect: Optional[ViewDialectType] = None
    DialectVersion: Optional[str] = None
    ViewOriginalText: Optional[str] = None
    ViewExpandedText: Optional[str] = None
    ValidationConnection: Optional[str] = None
    IsStale: Optional[bool] = None


class WorkflowRunStatistics(BaseValidatorModel):
    TotalActions: Optional[int] = None
    TimeoutActions: Optional[int] = None
    FailedActions: Optional[int] = None
    StoppedActions: Optional[int] = None
    SucceededActions: Optional[int] = None
    RunningActions: Optional[int] = None
    ErroredActions: Optional[int] = None
    WaitingActions: Optional[int] = None


class ActionOutput(BaseValidatorModel):
    JobName: Optional[str] = None
    Arguments: Optional[Dict[str, str]] = None
    Timeout: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationProperty] = None
    CrawlerName: Optional[str] = None


class Action(BaseValidatorModel):
    JobName: Optional[str] = None
    Arguments: Optional[Mapping[str, str]] = None
    Timeout: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationProperty] = None
    CrawlerName: Optional[str] = None


class StartJobRunRequest(BaseValidatorModel):
    JobName: str
    JobRunQueuingEnabled: Optional[bool] = None
    JobRunId: Optional[str] = None
    Arguments: Optional[Mapping[str, str]] = None
    AllocatedCapacity: Optional[int] = None
    Timeout: Optional[int] = None
    MaxCapacity: Optional[float] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationProperty] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    ExecutionClass: Optional[ExecutionClassType] = None


class AggregateOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Groups: List[List[str]]
    Aggs: List[AggregateOperationOutput]


class AmazonRedshiftNodeDataOutput(BaseValidatorModel):
    AccessType: Optional[str] = None
    SourceType: Optional[str] = None
    Connection: Optional[Option] = None
    Schema: Optional[Option] = None
    Table: Optional[Option] = None
    CatalogDatabase: Optional[Option] = None
    CatalogTable: Optional[Option] = None
    CatalogRedshiftSchema: Optional[str] = None
    CatalogRedshiftTable: Optional[str] = None
    TempDir: Optional[str] = None
    IamRole: Optional[Option] = None
    AdvancedOptions: Optional[List[AmazonRedshiftAdvancedOption]] = None
    SampleQuery: Optional[str] = None
    PreAction: Optional[str] = None
    PostAction: Optional[str] = None
    Action: Optional[str] = None
    TablePrefix: Optional[str] = None
    Upsert: Optional[bool] = None
    MergeAction: Optional[str] = None
    MergeWhenMatched: Optional[str] = None
    MergeWhenNotMatched: Optional[str] = None
    MergeClause: Optional[str] = None
    CrawlerConnection: Optional[str] = None
    TableSchema: Optional[List[Option]] = None
    StagingTable: Optional[str] = None
    SelectedColumns: Optional[List[Option]] = None


class AmazonRedshiftNodeData(BaseValidatorModel):
    AccessType: Optional[str] = None
    SourceType: Optional[str] = None
    Connection: Optional[Option] = None
    Schema: Optional[Option] = None
    Table: Optional[Option] = None
    CatalogDatabase: Optional[Option] = None
    CatalogTable: Optional[Option] = None
    CatalogRedshiftSchema: Optional[str] = None
    CatalogRedshiftTable: Optional[str] = None
    TempDir: Optional[str] = None
    IamRole: Optional[Option] = None
    AdvancedOptions: Optional[Sequence[AmazonRedshiftAdvancedOption]] = None
    SampleQuery: Optional[str] = None
    PreAction: Optional[str] = None
    PostAction: Optional[str] = None
    Action: Optional[str] = None
    TablePrefix: Optional[str] = None
    Upsert: Optional[bool] = None
    MergeAction: Optional[str] = None
    MergeWhenMatched: Optional[str] = None
    MergeWhenNotMatched: Optional[str] = None
    MergeClause: Optional[str] = None
    CrawlerConnection: Optional[str] = None
    TableSchema: Optional[Sequence[Option]] = None
    StagingTable: Optional[str] = None
    SelectedColumns: Optional[Sequence[Option]] = None


class SnowflakeNodeDataOutput(BaseValidatorModel):
    SourceType: Optional[str] = None
    Connection: Optional[Option] = None
    Schema: Optional[str] = None
    Table: Optional[str] = None
    Database: Optional[str] = None
    TempDir: Optional[str] = None
    IamRole: Optional[Option] = None
    AdditionalOptions: Optional[Dict[str, str]] = None
    SampleQuery: Optional[str] = None
    PreAction: Optional[str] = None
    PostAction: Optional[str] = None
    Action: Optional[str] = None
    Upsert: Optional[bool] = None
    MergeAction: Optional[str] = None
    MergeWhenMatched: Optional[str] = None
    MergeWhenNotMatched: Optional[str] = None
    MergeClause: Optional[str] = None
    StagingTable: Optional[str] = None
    SelectedColumns: Optional[List[Option]] = None
    AutoPushdown: Optional[bool] = None
    TableSchema: Optional[List[Option]] = None


class SnowflakeNodeData(BaseValidatorModel):
    SourceType: Optional[str] = None
    Connection: Optional[Option] = None
    Schema: Optional[str] = None
    Table: Optional[str] = None
    Database: Optional[str] = None
    TempDir: Optional[str] = None
    IamRole: Optional[Option] = None
    AdditionalOptions: Optional[Mapping[str, str]] = None
    SampleQuery: Optional[str] = None
    PreAction: Optional[str] = None
    PostAction: Optional[str] = None
    Action: Optional[str] = None
    Upsert: Optional[bool] = None
    MergeAction: Optional[str] = None
    MergeWhenMatched: Optional[str] = None
    MergeWhenNotMatched: Optional[str] = None
    MergeClause: Optional[str] = None
    StagingTable: Optional[str] = None
    SelectedColumns: Optional[Sequence[Option]] = None
    AutoPushdown: Optional[bool] = None
    TableSchema: Optional[Sequence[Option]] = None


class BackfillError(BaseValidatorModel):
    Code: Optional[BackfillErrorCodeType] = None
    Partitions: Optional[List[PartitionValueListOutput]] = None


class BatchPutDataQualityStatisticAnnotationResponse(BaseValidatorModel):
    FailedInclusionAnnotations: List[AnnotationError]
    ResponseMetadata: ResponseMetadata


class CancelMLTaskRunResponse(BaseValidatorModel):
    TransformId: str
    TaskRunId: str
    Status: TaskStatusTypeType
    ResponseMetadata: ResponseMetadata


class CheckSchemaVersionValidityResponse(BaseValidatorModel):
    Valid: bool
    Error: str
    ResponseMetadata: ResponseMetadata


class CreateBlueprintResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateConnectionResponse(BaseValidatorModel):
    CreateConnectionStatus: ConnectionStatusType
    ResponseMetadata: ResponseMetadata


class CreateCustomEntityTypeResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateDataQualityRulesetResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateDevEndpointResponse(BaseValidatorModel):
    EndpointName: str
    Status: str
    SecurityGroupIds: List[str]
    SubnetId: str
    RoleArn: str
    YarnEndpointAddress: str
    ZeppelinRemoteSparkInterpreterPort: int
    NumberOfNodes: int
    WorkerType: WorkerTypeType
    GlueVersion: str
    NumberOfWorkers: int
    AvailabilityZone: str
    VpcId: str
    ExtraPythonLibsS3Path: str
    ExtraJarsS3Path: str
    FailureReason: str
    SecurityConfiguration: str
    CreatedTimestamp: datetime
    Arguments: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateJobResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateMLTransformResponse(BaseValidatorModel):
    TransformId: str
    ResponseMetadata: ResponseMetadata


class CreateRegistryResponse(BaseValidatorModel):
    RegistryArn: str
    RegistryName: str
    Description: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateSchemaResponse(BaseValidatorModel):
    RegistryName: str
    RegistryArn: str
    SchemaName: str
    SchemaArn: str
    Description: str
    DataFormat: DataFormatType
    Compatibility: CompatibilityType
    SchemaCheckpoint: int
    LatestSchemaVersion: int
    NextSchemaVersion: int
    SchemaStatus: SchemaStatusType
    Tags: Dict[str, str]
    SchemaVersionId: str
    SchemaVersionStatus: SchemaVersionStatusType
    ResponseMetadata: ResponseMetadata


class CreateScriptResponse(BaseValidatorModel):
    PythonScript: str
    ScalaCode: str
    ResponseMetadata: ResponseMetadata


class CreateSecurityConfigurationResponse(BaseValidatorModel):
    Name: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class CreateTriggerResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateUsageProfileResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class CreateWorkflowResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class DeleteBlueprintResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class DeleteCustomEntityTypeResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class DeleteJobResponse(BaseValidatorModel):
    JobName: str
    ResponseMetadata: ResponseMetadata


class DeleteMLTransformResponse(BaseValidatorModel):
    TransformId: str
    ResponseMetadata: ResponseMetadata


class DeleteRegistryResponse(BaseValidatorModel):
    RegistryName: str
    RegistryArn: str
    Status: RegistryStatusType
    ResponseMetadata: ResponseMetadata


class DeleteSchemaResponse(BaseValidatorModel):
    SchemaArn: str
    SchemaName: str
    Status: SchemaStatusType
    ResponseMetadata: ResponseMetadata


class DeleteSessionResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


class DeleteTriggerResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class DeleteWorkflowResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class GetCustomEntityTypeResponse(BaseValidatorModel):
    Name: str
    RegexString: str
    ContextWords: List[str]
    ResponseMetadata: ResponseMetadata


class GetDataQualityModelResponse(BaseValidatorModel):
    Status: DataQualityModelStatusType
    StartedOn: datetime
    CompletedOn: datetime
    FailureReason: str
    ResponseMetadata: ResponseMetadata


class GetEntityRecordsResponse(BaseValidatorModel):
    Records: List[Dict[str, Any]]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetPlanResponse(BaseValidatorModel):
    PythonScript: str
    ScalaCode: str
    ResponseMetadata: ResponseMetadata


class GetRegistryResponse(BaseValidatorModel):
    RegistryName: str
    RegistryArn: str
    Description: str
    Status: RegistryStatusType
    CreatedTime: str
    UpdatedTime: str
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyResponse(BaseValidatorModel):
    PolicyInJson: str
    PolicyHash: str
    CreateTime: datetime
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadata


class GetSchemaByDefinitionResponse(BaseValidatorModel):
    SchemaVersionId: str
    SchemaArn: str
    DataFormat: DataFormatType
    Status: SchemaVersionStatusType
    CreatedTime: str
    ResponseMetadata: ResponseMetadata


class GetSchemaResponse(BaseValidatorModel):
    RegistryName: str
    RegistryArn: str
    SchemaName: str
    SchemaArn: str
    Description: str
    DataFormat: DataFormatType
    Compatibility: CompatibilityType
    SchemaCheckpoint: int
    LatestSchemaVersion: int
    NextSchemaVersion: int
    SchemaStatus: SchemaStatusType
    CreatedTime: str
    UpdatedTime: str
    ResponseMetadata: ResponseMetadata


class GetSchemaVersionResponse(BaseValidatorModel):
    SchemaVersionId: str
    SchemaDefinition: str
    DataFormat: DataFormatType
    SchemaArn: str
    VersionNumber: int
    Status: SchemaVersionStatusType
    CreatedTime: str
    ResponseMetadata: ResponseMetadata


class GetSchemaVersionsDiffResponse(BaseValidatorModel):
    Diff: str
    ResponseMetadata: ResponseMetadata


class GetTagsResponse(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetWorkflowRunPropertiesResponse(BaseValidatorModel):
    RunProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListBlueprintsResponse(BaseValidatorModel):
    Blueprints: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListColumnStatisticsTaskRunsResponse(BaseValidatorModel):
    ColumnStatisticsTaskRunIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListCrawlersResponse(BaseValidatorModel):
    CrawlerNames: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDevEndpointsResponse(BaseValidatorModel):
    DevEndpointNames: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListJobsResponse(BaseValidatorModel):
    JobNames: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMLTransformsResponse(BaseValidatorModel):
    TransformIds: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTriggersResponse(BaseValidatorModel):
    TriggerNames: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListWorkflowsResponse(BaseValidatorModel):
    Workflows: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PutResourcePolicyResponse(BaseValidatorModel):
    PolicyHash: str
    ResponseMetadata: ResponseMetadata


class PutSchemaVersionMetadataResponse(BaseValidatorModel):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    LatestVersion: bool
    VersionNumber: int
    SchemaVersionId: str
    MetadataKey: str
    MetadataValue: str
    ResponseMetadata: ResponseMetadata


class RegisterSchemaVersionResponse(BaseValidatorModel):
    SchemaVersionId: str
    VersionNumber: int
    Status: SchemaVersionStatusType
    ResponseMetadata: ResponseMetadata


class RemoveSchemaVersionMetadataResponse(BaseValidatorModel):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    LatestVersion: bool
    VersionNumber: int
    SchemaVersionId: str
    MetadataKey: str
    MetadataValue: str
    ResponseMetadata: ResponseMetadata


class ResumeWorkflowRunResponse(BaseValidatorModel):
    RunId: str
    NodeIds: List[str]
    ResponseMetadata: ResponseMetadata


class RunStatementResponse(BaseValidatorModel):
    Id: int
    ResponseMetadata: ResponseMetadata


class StartBlueprintRunResponse(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadata


class StartColumnStatisticsTaskRunResponse(BaseValidatorModel):
    ColumnStatisticsTaskRunId: str
    ResponseMetadata: ResponseMetadata


class StartDataQualityRuleRecommendationRunResponse(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadata


class StartDataQualityRulesetEvaluationRunResponse(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadata


class StartExportLabelsTaskRunResponse(BaseValidatorModel):
    TaskRunId: str
    ResponseMetadata: ResponseMetadata


class StartImportLabelsTaskRunResponse(BaseValidatorModel):
    TaskRunId: str
    ResponseMetadata: ResponseMetadata


class StartJobRunResponse(BaseValidatorModel):
    JobRunId: str
    ResponseMetadata: ResponseMetadata


class StartMLEvaluationTaskRunResponse(BaseValidatorModel):
    TaskRunId: str
    ResponseMetadata: ResponseMetadata


class StartMLLabelingSetGenerationTaskRunResponse(BaseValidatorModel):
    TaskRunId: str
    ResponseMetadata: ResponseMetadata


class StartTriggerResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class StartWorkflowRunResponse(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadata


class StopSessionResponse(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadata


class StopTriggerResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class UpdateBlueprintResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class UpdateDataQualityRulesetResponse(BaseValidatorModel):
    Name: str
    Description: str
    Ruleset: str
    ResponseMetadata: ResponseMetadata


class UpdateJobFromSourceControlResponse(BaseValidatorModel):
    JobName: str
    ResponseMetadata: ResponseMetadata


class UpdateJobResponse(BaseValidatorModel):
    JobName: str
    ResponseMetadata: ResponseMetadata


class UpdateMLTransformResponse(BaseValidatorModel):
    TransformId: str
    ResponseMetadata: ResponseMetadata


class UpdateRegistryResponse(BaseValidatorModel):
    RegistryName: str
    RegistryArn: str
    ResponseMetadata: ResponseMetadata


class UpdateSchemaResponse(BaseValidatorModel):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    ResponseMetadata: ResponseMetadata


class UpdateSourceControlFromJobResponse(BaseValidatorModel):
    JobName: str
    ResponseMetadata: ResponseMetadata


class UpdateUsageProfileResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class UpdateWorkflowResponse(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadata


class BatchDeleteConnectionResponse(BaseValidatorModel):
    Succeeded: List[str]
    Errors: Dict[str, ErrorDetail]
    ResponseMetadata: ResponseMetadata


class BatchStopJobRunError(BaseValidatorModel):
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None
    ErrorDetail: Optional[ErrorDetail] = None


class BatchUpdatePartitionFailureEntry(BaseValidatorModel):
    PartitionValueList: Optional[List[str]] = None
    ErrorDetail: Optional[ErrorDetail] = None


class ColumnError(BaseValidatorModel):
    ColumnName: Optional[str] = None
    Error: Optional[ErrorDetail] = None


class PartitionError(BaseValidatorModel):
    PartitionValues: Optional[List[str]] = None
    ErrorDetail: Optional[ErrorDetail] = None


class TableError(BaseValidatorModel):
    TableName: Optional[str] = None
    ErrorDetail: Optional[ErrorDetail] = None


class TableVersionError(BaseValidatorModel):
    TableName: Optional[str] = None
    VersionId: Optional[str] = None
    ErrorDetail: Optional[ErrorDetail] = None


class ViewValidation(BaseValidatorModel):
    Dialect: Optional[ViewDialectType] = None
    DialectVersion: Optional[str] = None
    ViewValidationText: Optional[str] = None
    UpdateTime: Optional[datetime] = None
    State: Optional[ResourceStateType] = None
    Error: Optional[ErrorDetail] = None


class BatchGetCustomEntityTypesResponse(BaseValidatorModel):
    CustomEntityTypes: List[CustomEntityType]
    CustomEntityTypesNotFound: List[str]
    ResponseMetadata: ResponseMetadata


class ListCustomEntityTypesResponse(BaseValidatorModel):
    CustomEntityTypes: List[CustomEntityType]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchGetDevEndpointsResponse(BaseValidatorModel):
    DevEndpoints: List[DevEndpoint]
    DevEndpointsNotFound: List[str]
    ResponseMetadata: ResponseMetadata


class GetDevEndpointResponse(BaseValidatorModel):
    DevEndpoint: DevEndpoint
    ResponseMetadata: ResponseMetadata


class GetDevEndpointsResponse(BaseValidatorModel):
    DevEndpoints: List[DevEndpoint]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchGetTableOptimizerEntry(BaseValidatorModel):
    pass


class BatchGetTableOptimizerRequest(BaseValidatorModel):
    Entries: Sequence[BatchGetTableOptimizerEntry]


class BatchPutDataQualityStatisticAnnotationRequest(BaseValidatorModel):
    InclusionAnnotations: Sequence[DatapointInclusionAnnotation]
    ClientToken: Optional[str] = None


class Blob(BaseValidatorModel):
    pass


class DecimalNumber(BaseValidatorModel):
    UnscaledValue: Blob
    Scale: int


class GetBlueprintRunResponse(BaseValidatorModel):
    BlueprintRun: BlueprintRun
    ResponseMetadata: ResponseMetadata


class GetBlueprintRunsResponse(BaseValidatorModel):
    BlueprintRuns: List[BlueprintRun]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Blueprint(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    ParameterSpec: Optional[str] = None
    BlueprintLocation: Optional[str] = None
    BlueprintServiceLocation: Optional[str] = None
    Status: Optional[BlueprintStatusType] = None
    ErrorMessage: Optional[str] = None
    LastActiveDefinition: Optional[LastActiveDefinition] = None


class ConnectionTypeBrief(BaseValidatorModel):
    ConnectionType: Optional[ConnectionTypeType] = None
    Description: Optional[str] = None
    Capabilities: Optional[Capabilities] = None


class GetCatalogImportStatusResponse(BaseValidatorModel):
    ImportStatus: CatalogImportStatus
    ResponseMetadata: ResponseMetadata


class CatalogKafkaSourceOutput(BaseValidatorModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KafkaStreamingSourceOptionsOutput] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptions] = None


class DirectKafkaSourceOutput(BaseValidatorModel):
    Name: str
    StreamingOptions: Optional[KafkaStreamingSourceOptionsOutput] = None
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptions] = None


class CatalogKinesisSourceOutput(BaseValidatorModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsOutput] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptions] = None


class DirectKinesisSourceOutput(BaseValidatorModel):
    Name: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsOutput] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptions] = None


class CatalogPropertiesOutput(BaseValidatorModel):
    DataLakeAccessProperties: Optional[DataLakeAccessPropertiesOutput] = None
    CustomProperties: Optional[Dict[str, str]] = None


class CatalogProperties(BaseValidatorModel):
    DataLakeAccessProperties: Optional[DataLakeAccessProperties] = None
    CustomProperties: Optional[Mapping[str, str]] = None


class GovernedCatalogTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicy] = None


class GovernedCatalogTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicy] = None


class S3CatalogTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicy] = None


class S3CatalogTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicy] = None


class S3DeltaCatalogTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    AdditionalOptions: Optional[Dict[str, str]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicy] = None


class S3DeltaCatalogTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    AdditionalOptions: Optional[Mapping[str, str]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicy] = None


class S3HudiCatalogTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    AdditionalOptions: Dict[str, str]
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicy] = None


class S3HudiCatalogTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    AdditionalOptions: Mapping[str, str]
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicy] = None


class Classifier(BaseValidatorModel):
    GrokClassifier: Optional[GrokClassifier] = None
    XMLClassifier: Optional[XMLClassifier] = None
    JsonClassifier: Optional[JsonClassifier] = None
    CsvClassifier: Optional[CsvClassifier] = None


class CodeGenNodeOutput(BaseValidatorModel):
    Id: str
    NodeType: str
    Args: List[CodeGenNodeArg]
    LineNumber: Optional[int] = None


class CodeGenNode(BaseValidatorModel):
    Id: str
    NodeType: str
    Args: Sequence[CodeGenNodeArg]
    LineNumber: Optional[int] = None


class Location(BaseValidatorModel):
    Jdbc: Optional[Sequence[CodeGenNodeArg]] = None
    S3: Optional[Sequence[CodeGenNodeArg]] = None
    DynamoDB: Optional[Sequence[CodeGenNodeArg]] = None


class GetColumnStatisticsTaskRunResponse(BaseValidatorModel):
    ColumnStatisticsTaskRun: ColumnStatisticsTaskRun
    ResponseMetadata: ResponseMetadata


class GetColumnStatisticsTaskRunsResponse(BaseValidatorModel):
    ColumnStatisticsTaskRuns: List[ColumnStatisticsTaskRun]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ColumnStatisticsTaskSettings(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Schedule: Optional[Schedule] = None
    ColumnNameList: Optional[List[str]] = None
    CatalogID: Optional[str] = None
    Role: Optional[str] = None
    SampleSize: Optional[float] = None
    SecurityConfiguration: Optional[str] = None
    ScheduleType: Optional[ScheduleTypeType] = None
    SettingSource: Optional[SettingSourceType] = None
    LastExecutionAttempt: Optional[ExecutionAttempt] = None


class Timestamp(BaseValidatorModel):
    pass


class DateColumnStatisticsData(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[Timestamp] = None
    MaximumValue: Optional[Timestamp] = None


class GetTableRequest(BaseValidatorModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[Timestamp] = None
    IncludeStatusDetails: Optional[bool] = None


class GetTablesRequest(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[Timestamp] = None
    IncludeStatusDetails: Optional[bool] = None
    AttributesToGet: Optional[Sequence[TableAttributesType]] = None


class KafkaStreamingSourceOptions(BaseValidatorModel):
    BootstrapServers: Optional[str] = None
    SecurityProtocol: Optional[str] = None
    ConnectionName: Optional[str] = None
    TopicName: Optional[str] = None
    Assign: Optional[str] = None
    SubscribePattern: Optional[str] = None
    Classification: Optional[str] = None
    Delimiter: Optional[str] = None
    StartingOffsets: Optional[str] = None
    EndingOffsets: Optional[str] = None
    PollTimeoutMs: Optional[int] = None
    NumRetries: Optional[int] = None
    RetryIntervalMs: Optional[int] = None
    MaxOffsetsPerTrigger: Optional[int] = None
    MinPartitions: Optional[int] = None
    IncludeHeaders: Optional[bool] = None
    AddRecordTimestamp: Optional[str] = None
    EmitConsumerLagMetrics: Optional[str] = None
    StartingTimestamp: Optional[Timestamp] = None


class KinesisStreamingSourceOptions(BaseValidatorModel):
    EndpointUrl: Optional[str] = None
    StreamName: Optional[str] = None
    Classification: Optional[str] = None
    Delimiter: Optional[str] = None
    StartingPosition: Optional[StartingPositionType] = None
    MaxFetchTimeInMs: Optional[int] = None
    MaxFetchRecordsPerShard: Optional[int] = None
    MaxRecordPerRead: Optional[int] = None
    AddIdleTimeBetweenReads: Optional[bool] = None
    IdleTimeBetweenReadsInMs: Optional[int] = None
    DescribeShardInterval: Optional[int] = None
    NumRetries: Optional[int] = None
    RetryIntervalMs: Optional[int] = None
    MaxRetryIntervalMs: Optional[int] = None
    AvoidEmptyBatches: Optional[bool] = None
    StreamArn: Optional[str] = None
    RoleArn: Optional[str] = None
    RoleSessionName: Optional[str] = None
    AddRecordTimestamp: Optional[str] = None
    EmitConsumerLagMetrics: Optional[str] = None
    StartingTimestamp: Optional[Timestamp] = None


class QuerySessionContext(BaseValidatorModel):
    QueryId: Optional[str] = None
    QueryStartTime: Optional[Timestamp] = None
    ClusterId: Optional[str] = None
    QueryAuthorizationId: Optional[str] = None
    AdditionalContext: Optional[Mapping[str, str]] = None


class TaskRunFilterCriteria(BaseValidatorModel):
    TaskRunType: Optional[TaskTypeType] = None
    Status: Optional[TaskStatusTypeType] = None
    StartedBefore: Optional[Timestamp] = None
    StartedAfter: Optional[Timestamp] = None


class TimestampFilter(BaseValidatorModel):
    RecordedBefore: Optional[Timestamp] = None
    RecordedAfter: Optional[Timestamp] = None


class CompactionMetrics(BaseValidatorModel):
    IcebergMetrics: Optional[IcebergCompactionMetrics] = None


class PredicateOutput(BaseValidatorModel):
    Logical: Optional[LogicalType] = None
    Conditions: Optional[List[Condition]] = None


class Predicate(BaseValidatorModel):
    Logical: Optional[LogicalType] = None
    Conditions: Optional[Sequence[Condition]] = None


class ProfileConfigurationOutput(BaseValidatorModel):
    SessionConfiguration: Optional[Dict[str, ConfigurationObjectOutput]] = None
    JobConfiguration: Optional[Dict[str, ConfigurationObjectOutput]] = None


class ProfileConfiguration(BaseValidatorModel):
    SessionConfiguration: Optional[Mapping[str, ConfigurationObject]] = None
    JobConfiguration: Optional[Mapping[str, ConfigurationObject]] = None


class FindMatchesMetrics(BaseValidatorModel):
    AreaUnderPRCurve: Optional[float] = None
    Precision: Optional[float] = None
    Recall: Optional[float] = None
    F1: Optional[float] = None
    ConfusionMatrix: Optional[ConfusionMatrix] = None
    ColumnImportances: Optional[List[ColumnImportance]] = None


class CrawlerNodeDetails(BaseValidatorModel):
    Crawls: Optional[List[Crawl]] = None


class ListCrawlsResponse(BaseValidatorModel):
    Crawls: List[CrawlerHistory]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetCrawlerMetricsResponse(BaseValidatorModel):
    CrawlerMetricsList: List[CrawlerMetrics]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CrawlerTargetsOutput(BaseValidatorModel):
    S3Targets: Optional[List[S3TargetOutput]] = None
    JdbcTargets: Optional[List[JdbcTargetOutput]] = None
    MongoDBTargets: Optional[List[MongoDBTarget]] = None
    DynamoDBTargets: Optional[List[DynamoDBTarget]] = None
    CatalogTargets: Optional[List[CatalogTargetOutput]] = None
    DeltaTargets: Optional[List[DeltaTargetOutput]] = None
    IcebergTargets: Optional[List[IcebergTargetOutput]] = None
    HudiTargets: Optional[List[HudiTargetOutput]] = None


class CrawlerTargets(BaseValidatorModel):
    S3Targets: Optional[Sequence[S3Target]] = None
    JdbcTargets: Optional[Sequence[JdbcTarget]] = None
    MongoDBTargets: Optional[Sequence[MongoDBTarget]] = None
    DynamoDBTargets: Optional[Sequence[DynamoDBTarget]] = None
    CatalogTargets: Optional[Sequence[CatalogTarget]] = None
    DeltaTargets: Optional[Sequence[DeltaTarget]] = None
    IcebergTargets: Optional[Sequence[IcebergTarget]] = None
    HudiTargets: Optional[Sequence[HudiTarget]] = None


class ListCrawlsRequest(BaseValidatorModel):
    CrawlerName: str
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[CrawlsFilter]] = None
    NextToken: Optional[str] = None


class CreateClassifierRequest(BaseValidatorModel):
    GrokClassifier: Optional[CreateGrokClassifierRequest] = None
    XMLClassifier: Optional[CreateXMLClassifierRequest] = None
    JsonClassifier: Optional[CreateJsonClassifierRequest] = None
    CsvClassifier: Optional[CreateCsvClassifierRequest] = None


class CreateDataQualityRulesetRequest(BaseValidatorModel):
    Name: str
    Ruleset: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    TargetTable: Optional[DataQualityTargetTable] = None
    DataQualitySecurityConfiguration: Optional[str] = None
    ClientToken: Optional[str] = None


class DataQualityRulesetFilterCriteria(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedBefore: Optional[Timestamp] = None
    CreatedAfter: Optional[Timestamp] = None
    LastModifiedBefore: Optional[Timestamp] = None
    LastModifiedAfter: Optional[Timestamp] = None
    TargetTable: Optional[DataQualityTargetTable] = None


class DataQualityRulesetListDetails(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    TargetTable: Optional[DataQualityTargetTable] = None
    RecommendationRunId: Optional[str] = None
    RuleCount: Optional[int] = None


class GetDataQualityRulesetResponse(BaseValidatorModel):
    Name: str
    Description: str
    Ruleset: str
    TargetTable: DataQualityTargetTable
    CreatedOn: datetime
    LastModifiedOn: datetime
    RecommendationRunId: str
    DataQualitySecurityConfiguration: str
    ResponseMetadata: ResponseMetadata


class CreateIntegrationRequest(BaseValidatorModel):
    IntegrationName: str
    SourceArn: str
    TargetArn: str
    Description: Optional[str] = None
    DataFilter: Optional[str] = None
    KmsKeyId: Optional[str] = None
    AdditionalEncryptionContext: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateIntegrationResourcePropertyRequest(BaseValidatorModel):
    ResourceArn: str
    SourceProcessingProperties: Optional[SourceProcessingProperties] = None
    TargetProcessingProperties: Optional[TargetProcessingProperties] = None


class CreateIntegrationResourcePropertyResponse(BaseValidatorModel):
    ResourceArn: str
    SourceProcessingProperties: SourceProcessingProperties
    TargetProcessingProperties: TargetProcessingProperties
    ResponseMetadata: ResponseMetadata


class GetIntegrationResourcePropertyResponse(BaseValidatorModel):
    ResourceArn: str
    SourceProcessingProperties: SourceProcessingProperties
    TargetProcessingProperties: TargetProcessingProperties
    ResponseMetadata: ResponseMetadata


class UpdateIntegrationResourcePropertyRequest(BaseValidatorModel):
    ResourceArn: str
    SourceProcessingProperties: Optional[SourceProcessingProperties] = None
    TargetProcessingProperties: Optional[TargetProcessingProperties] = None


class UpdateIntegrationResourcePropertyResponse(BaseValidatorModel):
    ResourceArn: str
    SourceProcessingProperties: SourceProcessingProperties
    TargetProcessingProperties: TargetProcessingProperties
    ResponseMetadata: ResponseMetadata


class CreateIntegrationResponse(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    Description: str
    IntegrationArn: str
    KmsKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Tags: List[Tag]
    Status: IntegrationStatusType
    CreateTime: datetime
    Errors: List[IntegrationError]
    DataFilter: str
    ResponseMetadata: ResponseMetadata


class DeleteIntegrationResponse(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    Description: str
    IntegrationArn: str
    KmsKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Tags: List[Tag]
    Status: IntegrationStatusType
    CreateTime: datetime
    Errors: List[IntegrationError]
    DataFilter: str
    ResponseMetadata: ResponseMetadata


class InboundIntegration(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationArn: str
    Status: IntegrationStatusType
    CreateTime: datetime
    Errors: Optional[List[IntegrationError]] = None


class Integration(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    IntegrationArn: str
    Status: IntegrationStatusType
    CreateTime: datetime
    Description: Optional[str] = None
    KmsKeyId: Optional[str] = None
    AdditionalEncryptionContext: Optional[Dict[str, str]] = None
    Tags: Optional[List[Tag]] = None
    Errors: Optional[List[IntegrationError]] = None
    DataFilter: Optional[str] = None


class ModifyIntegrationResponse(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    Description: str
    IntegrationArn: str
    KmsKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Tags: List[Tag]
    Status: IntegrationStatusType
    CreateTime: datetime
    Errors: List[IntegrationError]
    DataFilter: str
    ResponseMetadata: ResponseMetadata


class CreatePartitionIndexRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionIndex: PartitionIndex
    CatalogId: Optional[str] = None


class CreateSchemaInput(BaseValidatorModel):
    SchemaName: str
    DataFormat: DataFormatType
    RegistryId: Optional[RegistryId] = None
    Compatibility: Optional[CompatibilityType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    SchemaDefinition: Optional[str] = None


class DeleteRegistryInput(BaseValidatorModel):
    RegistryId: RegistryId


class GetRegistryInput(BaseValidatorModel):
    RegistryId: RegistryId


class ListSchemasInput(BaseValidatorModel):
    RegistryId: Optional[RegistryId] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class UpdateRegistryInput(BaseValidatorModel):
    RegistryId: RegistryId
    Description: str


class Session(BaseValidatorModel):
    Id: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    Status: Optional[SessionStatusType] = None
    ErrorMessage: Optional[str] = None
    Description: Optional[str] = None
    Role: Optional[str] = None
    Command: Optional[SessionCommand] = None
    DefaultArguments: Optional[Dict[str, str]] = None
    Connections: Optional[ConnectionsListOutput] = None
    Progress: Optional[float] = None
    MaxCapacity: Optional[float] = None
    SecurityConfiguration: Optional[str] = None
    GlueVersion: Optional[str] = None
    NumberOfWorkers: Optional[int] = None
    WorkerType: Optional[WorkerTypeType] = None
    CompletedOn: Optional[datetime] = None
    ExecutionTime: Optional[float] = None
    DPUSeconds: Optional[float] = None
    IdleTimeout: Optional[int] = None
    ProfileName: Optional[str] = None


class EvaluateDataQualityMultiFrameOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Ruleset: str
    AdditionalDataSources: Optional[Dict[str, str]] = None
    PublishingOptions: Optional[DQResultsPublishingOptions] = None
    AdditionalOptions: Optional[Dict[AdditionalOptionKeysType, str]] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptions] = None


class EvaluateDataQualityMultiFrame(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Ruleset: str
    AdditionalDataSources: Optional[Mapping[str, str]] = None
    PublishingOptions: Optional[DQResultsPublishingOptions] = None
    AdditionalOptions: Optional[Mapping[AdditionalOptionKeysType, str]] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptions] = None


class EvaluateDataQualityOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Ruleset: str
    Output: Optional[DQTransformOutputType] = None
    PublishingOptions: Optional[DQResultsPublishingOptions] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptions] = None


class EvaluateDataQuality(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Ruleset: str
    Output: Optional[DQTransformOutputType] = None
    PublishingOptions: Optional[DQResultsPublishingOptions] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptions] = None


class DataCatalogEncryptionSettings(BaseValidatorModel):
    EncryptionAtRest: Optional[EncryptionAtRest] = None
    ConnectionPasswordEncryption: Optional[ConnectionPasswordEncryption] = None


class PrincipalPermissionsOutput(BaseValidatorModel):
    Principal: Optional[DataLakePrincipal] = None
    Permissions: Optional[List[PermissionType]] = None


class PrincipalPermissions(BaseValidatorModel):
    Principal: Optional[DataLakePrincipal] = None
    Permissions: Optional[Sequence[PermissionType]] = None


class MetricBasedObservation(BaseValidatorModel):
    MetricName: Optional[str] = None
    StatisticId: Optional[str] = None
    MetricValues: Optional[DataQualityMetricValues] = None
    NewRules: Optional[List[str]] = None


class DataSourceOutput(BaseValidatorModel):
    GlueTable: GlueTableOutput


class NullValueField(BaseValidatorModel):
    Value: str
    Datatype: Datatype


class DecimalColumnStatisticsDataOutput(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[DecimalNumberOutput] = None
    MaximumValue: Optional[DecimalNumberOutput] = None


class DeleteSchemaInput(BaseValidatorModel):
    SchemaId: SchemaId


class DeleteSchemaVersionsInput(BaseValidatorModel):
    SchemaId: SchemaId
    Versions: str


class GetSchemaByDefinitionInput(BaseValidatorModel):
    SchemaId: SchemaId
    SchemaDefinition: str


class GetSchemaInput(BaseValidatorModel):
    SchemaId: SchemaId


class ListSchemaVersionsInput(BaseValidatorModel):
    SchemaId: SchemaId
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RegisterSchemaVersionInput(BaseValidatorModel):
    SchemaId: SchemaId
    SchemaDefinition: str


class SchemaReference(BaseValidatorModel):
    SchemaId: Optional[SchemaId] = None
    SchemaVersionId: Optional[str] = None
    SchemaVersionNumber: Optional[int] = None


class DescribeEntityRequestPaginate(BaseValidatorModel):
    ConnectionName: str
    EntityName: str
    CatalogId: Optional[str] = None
    DataStoreApiVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetClassifiersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetCrawlerMetricsRequestPaginate(BaseValidatorModel):
    CrawlerNameList: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetCrawlersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDatabasesRequestPaginate(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    AttributesToGet: Optional[Sequence[Literal["NAME"]]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetDevEndpointsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetJobRunsRequestPaginate(BaseValidatorModel):
    JobName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class GetJobsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetPartitionIndexesRequestPaginate(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetResourcePoliciesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetSecurityConfigurationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class GetTableVersionsRequestPaginate(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetTablesRequestPaginate(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[Timestamp] = None
    IncludeStatusDetails: Optional[bool] = None
    AttributesToGet: Optional[Sequence[TableAttributesType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetTriggersRequestPaginate(BaseValidatorModel):
    DependentJobName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetWorkflowRunsRequestPaginate(BaseValidatorModel):
    Name: str
    IncludeGraph: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBlueprintsRequestPaginate(BaseValidatorModel):
    Tags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConnectionTypesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEntitiesRequestPaginate(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    CatalogId: Optional[str] = None
    ParentEntityName: Optional[str] = None
    DataStoreApiVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobsRequestPaginate(BaseValidatorModel):
    Tags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRegistriesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchemaVersionsInputPaginate(BaseValidatorModel):
    SchemaId: SchemaId
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchemasInputPaginate(BaseValidatorModel):
    RegistryId: Optional[RegistryId] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTriggersRequestPaginate(BaseValidatorModel):
    DependentJobName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsageProfilesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWorkflowsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEntityResponse(BaseValidatorModel):
    Fields: List[Field]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeIntegrationsRequest(BaseValidatorModel):
    IntegrationIdentifier: Optional[str] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    Filters: Optional[Sequence[IntegrationFilter]] = None


class UpdateDevEndpointRequest(BaseValidatorModel):
    EndpointName: str
    PublicKey: Optional[str] = None
    AddPublicKeys: Optional[Sequence[str]] = None
    DeletePublicKeys: Optional[Sequence[str]] = None
    CustomLibraries: Optional[DevEndpointCustomLibraries] = None
    UpdateEtlLibraries: Optional[bool] = None
    DeleteArguments: Optional[Sequence[str]] = None
    AddArguments: Optional[Mapping[str, str]] = None


class S3DeltaDirectTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    Compression: DeltaTargetCompressionTypeType
    Format: TargetFormatType
    PartitionKeys: Optional[List[List[str]]] = None
    AdditionalOptions: Optional[Dict[str, str]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy] = None


class S3DeltaDirectTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Compression: DeltaTargetCompressionTypeType
    Format: TargetFormatType
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    AdditionalOptions: Optional[Mapping[str, str]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy] = None


class S3DirectTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    Format: TargetFormatType
    PartitionKeys: Optional[List[List[str]]] = None
    Compression: Optional[str] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy] = None


class S3DirectTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Format: TargetFormatType
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    Compression: Optional[str] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy] = None


class S3GlueParquetTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    PartitionKeys: Optional[List[List[str]]] = None
    Compression: Optional[ParquetCompressionTypeType] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy] = None


class S3GlueParquetTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    Compression: Optional[ParquetCompressionTypeType] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy] = None


class S3HudiDirectTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    Compression: HudiTargetCompressionTypeType
    Format: TargetFormatType
    AdditionalOptions: Dict[str, str]
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy] = None


class S3HudiDirectTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Compression: HudiTargetCompressionTypeType
    Format: TargetFormatType
    AdditionalOptions: Mapping[str, str]
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicy] = None


class EncryptionConfigurationOutput(BaseValidatorModel):
    S3Encryption: Optional[List[S3Encryption]] = None
    CloudWatchEncryption: Optional[CloudWatchEncryption] = None
    JobBookmarksEncryption: Optional[JobBookmarksEncryption] = None
    DataQualityEncryption: Optional[DataQualityEncryption] = None


class EncryptionConfiguration(BaseValidatorModel):
    S3Encryption: Optional[Sequence[S3Encryption]] = None
    CloudWatchEncryption: Optional[CloudWatchEncryption] = None
    JobBookmarksEncryption: Optional[JobBookmarksEncryption] = None
    DataQualityEncryption: Optional[DataQualityEncryption] = None


class ListEntitiesResponse(BaseValidatorModel):
    Entities: List[Entity]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SchemaVersionErrorItem(BaseValidatorModel):
    VersionNumber: Optional[int] = None
    ErrorDetails: Optional[ErrorDetails] = None


class FilterValueOutput(BaseValidatorModel):
    pass


class FilterExpressionOutput(BaseValidatorModel):
    Operation: FilterOperationType
    Values: List[FilterValueOutput]
    Negated: Optional[bool] = None


class TransformParameters(BaseValidatorModel):
    TransformType: Literal["FIND_MATCHES"]
    FindMatchesParameters: Optional[FindMatchesParameters] = None


class GetConnectionsRequestPaginate(BaseValidatorModel):
    CatalogId: Optional[str] = None
    Filter: Optional[GetConnectionsFilter] = None
    HidePassword: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetConnectionsRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    Filter: Optional[GetConnectionsFilter] = None
    HidePassword: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetDataQualityModelResultResponse(BaseValidatorModel):
    CompletedOn: datetime
    Model: List[StatisticModelResult]
    ResponseMetadata: ResponseMetadata


class GetJobBookmarkResponse(BaseValidatorModel):
    JobBookmarkEntry: JobBookmarkEntry
    ResponseMetadata: ResponseMetadata


class ResetJobBookmarkResponse(BaseValidatorModel):
    JobBookmarkEntry: JobBookmarkEntry
    ResponseMetadata: ResponseMetadata


class TransformFilterCriteria(BaseValidatorModel):
    Name: Optional[str] = None
    TransformType: Optional[Literal["FIND_MATCHES"]] = None
    Status: Optional[TransformStatusTypeType] = None
    GlueVersion: Optional[str] = None
    CreatedBefore: Optional[Timestamp] = None
    CreatedAfter: Optional[Timestamp] = None
    LastModifiedBefore: Optional[Timestamp] = None
    LastModifiedAfter: Optional[Timestamp] = None
    Schema: Optional[Sequence[SchemaColumn]] = None


class GetPartitionsRequestPaginate(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    Segment: Optional[Segment] = None
    ExcludeColumnSchema: Optional[bool] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[Timestamp] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetPartitionsRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    NextToken: Optional[str] = None
    Segment: Optional[Segment] = None
    MaxResults: Optional[int] = None
    ExcludeColumnSchema: Optional[bool] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[Timestamp] = None


class GetResourcePoliciesResponse(BaseValidatorModel):
    GetResourcePoliciesResponseList: List[GluePolicy]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetSchemaVersionInput(BaseValidatorModel):
    SchemaId: Optional[SchemaId] = None
    SchemaVersionId: Optional[str] = None
    SchemaVersionNumber: Optional[SchemaVersionNumber] = None


class GetSchemaVersionsDiffInput(BaseValidatorModel):
    SchemaId: SchemaId
    FirstSchemaVersionNumber: SchemaVersionNumber
    SecondSchemaVersionNumber: SchemaVersionNumber
    SchemaDiffType: Literal["SYNTAX_DIFF"]


class UpdateSchemaInput(BaseValidatorModel):
    SchemaId: SchemaId
    SchemaVersionNumber: Optional[SchemaVersionNumber] = None
    Compatibility: Optional[CompatibilityType] = None
    Description: Optional[str] = None


class GlueStudioSchemaColumn(BaseValidatorModel):
    pass


class GlueSchemaOutput(BaseValidatorModel):
    Columns: Optional[List[GlueStudioSchemaColumn]] = None


class GlueSchema(BaseValidatorModel):
    Columns: Optional[Sequence[GlueStudioSchemaColumn]] = None


class GovernedCatalogSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    PartitionPredicate: Optional[str] = None
    AdditionalOptions: Optional[S3SourceAdditionalOptions] = None


class S3CatalogSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    PartitionPredicate: Optional[str] = None
    AdditionalOptions: Optional[S3SourceAdditionalOptions] = None


class OpenTableFormatInput(BaseValidatorModel):
    IcebergInput: Optional[IcebergInput] = None


class OrphanFileDeletionConfiguration(BaseValidatorModel):
    icebergConfiguration: Optional[IcebergOrphanFileDeletionConfiguration] = None


class OrphanFileDeletionMetrics(BaseValidatorModel):
    IcebergMetrics: Optional[IcebergOrphanFileDeletionMetrics] = None


class RetentionConfiguration(BaseValidatorModel):
    icebergConfiguration: Optional[IcebergRetentionConfiguration] = None


class RetentionMetrics(BaseValidatorModel):
    IcebergMetrics: Optional[IcebergRetentionMetrics] = None


class TargetTableConfigOutput(BaseValidatorModel):
    UnnestSpec: Optional[UnnestSpecType] = None
    PartitionSpec: Optional[List[IntegrationPartition]] = None
    TargetTableName: Optional[str] = None


class TargetTableConfig(BaseValidatorModel):
    UnnestSpec: Optional[UnnestSpecType] = None
    PartitionSpec: Optional[Sequence[IntegrationPartition]] = None
    TargetTableName: Optional[str] = None


class JobRun(BaseValidatorModel):
    Id: Optional[str] = None
    Attempt: Optional[int] = None
    PreviousRunId: Optional[str] = None
    TriggerName: Optional[str] = None
    JobName: Optional[str] = None
    JobMode: Optional[JobModeType] = None
    JobRunQueuingEnabled: Optional[bool] = None
    StartedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    CompletedOn: Optional[datetime] = None
    JobRunState: Optional[JobRunStateType] = None
    Arguments: Optional[Dict[str, str]] = None
    ErrorMessage: Optional[str] = None
    PredecessorRuns: Optional[List[Predecessor]] = None
    AllocatedCapacity: Optional[int] = None
    ExecutionTime: Optional[int] = None
    Timeout: Optional[int] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    LogGroupName: Optional[str] = None
    NotificationProperty: Optional[NotificationProperty] = None
    GlueVersion: Optional[str] = None
    DPUSeconds: Optional[float] = None
    ExecutionClass: Optional[ExecutionClassType] = None
    MaintenanceWindow: Optional[str] = None
    ProfileName: Optional[str] = None
    StateDetail: Optional[str] = None


class JoinOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    JoinType: JoinTypeType
    Columns: List[JoinColumnOutput]


class TaskRunProperties(BaseValidatorModel):
    TaskType: Optional[TaskTypeType] = None
    ImportLabelsTaskRunProperties: Optional[ImportLabelsTaskRunProperties] = None
    ExportLabelsTaskRunProperties: Optional[ExportLabelsTaskRunProperties] = None
    LabelingSetGenerationTaskRunProperties: Optional[ LabelingSetGenerationTaskRunProperties ] = None
    FindMatchesTaskRunProperties: Optional[FindMatchesTaskRunProperties] = None


class ListRegistriesResponse(BaseValidatorModel):
    Registries: List[RegistryListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSchemaVersionsResponse(BaseValidatorModel):
    Schemas: List[SchemaVersionListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSchemasResponse(BaseValidatorModel):
    Schemas: List[SchemaListItem]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListUsageProfilesResponse(BaseValidatorModel):
    Profiles: List[UsageProfileDefinition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TransformEncryption(BaseValidatorModel):
    MlUserDataEncryption: Optional[MLUserDataEncryption] = None
    TaskRunSecurityConfigurationName: Optional[str] = None


class MetadataInfo(BaseValidatorModel):
    MetadataValue: Optional[str] = None
    CreatedTime: Optional[str] = None
    OtherMetadataValueList: Optional[List[OtherMetadataValueListItem]] = None


class PutSchemaVersionMetadataInput(BaseValidatorModel):
    MetadataKeyValue: MetadataKeyValuePair
    SchemaId: Optional[SchemaId] = None
    SchemaVersionNumber: Optional[SchemaVersionNumber] = None
    SchemaVersionId: Optional[str] = None


class QuerySchemaVersionMetadataInput(BaseValidatorModel):
    SchemaId: Optional[SchemaId] = None
    SchemaVersionNumber: Optional[SchemaVersionNumber] = None
    SchemaVersionId: Optional[str] = None
    MetadataList: Optional[Sequence[MetadataKeyValuePair]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RemoveSchemaVersionMetadataInput(BaseValidatorModel):
    MetadataKeyValue: MetadataKeyValuePair
    SchemaId: Optional[SchemaId] = None
    SchemaVersionNumber: Optional[SchemaVersionNumber] = None
    SchemaVersionId: Optional[str] = None


class OAuth2Properties(BaseValidatorModel):
    OAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    OAuth2ClientApplication: Optional[OAuth2ClientApplication] = None
    TokenUrl: Optional[str] = None
    TokenUrlParametersMap: Optional[Dict[str, str]] = None


class OAuth2PropertiesInput(BaseValidatorModel):
    OAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    OAuth2ClientApplication: Optional[OAuth2ClientApplication] = None
    TokenUrl: Optional[str] = None
    TokenUrlParametersMap: Optional[Mapping[str, str]] = None
    AuthorizationCodeProperties: Optional[AuthorizationCodeProperties] = None
    OAuth2Credentials: Optional[OAuth2Credentials] = None


class RecipeStepOutput(BaseValidatorModel):
    Action: RecipeActionOutput
    ConditionExpressions: Optional[List[ConditionExpression]] = None


class RedshiftTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str
    RedshiftTmpDir: Optional[str] = None
    TmpDirIAMRole: Optional[str] = None
    UpsertRedshiftOptions: Optional[UpsertRedshiftTargetOptionsOutput] = None


class UserDefinedFunctionInput(BaseValidatorModel):
    FunctionName: Optional[str] = None
    ClassName: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerType: Optional[PrincipalTypeType] = None
    ResourceUris: Optional[Sequence[ResourceUri]] = None


class UserDefinedFunction(BaseValidatorModel):
    FunctionName: Optional[str] = None
    DatabaseName: Optional[str] = None
    ClassName: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerType: Optional[PrincipalTypeType] = None
    CreateTime: Optional[datetime] = None
    ResourceUris: Optional[List[ResourceUri]] = None
    CatalogId: Optional[str] = None


class SearchTablesRequest(BaseValidatorModel):
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[PropertyPredicate]] = None
    SearchText: Optional[str] = None
    SortCriteria: Optional[Sequence[SortCriterion]] = None
    MaxResults: Optional[int] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    IncludeStatusDetails: Optional[bool] = None


class StatementOutput(BaseValidatorModel):
    Data: Optional[StatementOutputData] = None
    ExecutionCount: Optional[int] = None
    Status: Optional[StatementStateType] = None
    ErrorName: Optional[str] = None
    ErrorValue: Optional[str] = None
    Traceback: Optional[List[str]] = None


class StatisticAnnotation(BaseValidatorModel):
    ProfileId: Optional[str] = None
    StatisticId: Optional[str] = None
    StatisticRecordedOn: Optional[datetime] = None
    InclusionAnnotation: Optional[TimestampedInclusionAnnotation] = None


class StatisticSummary(BaseValidatorModel):
    StatisticId: Optional[str] = None
    ProfileId: Optional[str] = None
    RunIdentifier: Optional[RunIdentifier] = None
    StatisticName: Optional[str] = None
    DoubleValue: Optional[float] = None
    EvaluationLevel: Optional[StatisticEvaluationLevelType] = None
    ColumnsReferenced: Optional[List[str]] = None
    ReferencedDatasets: Optional[List[str]] = None
    StatisticProperties: Optional[Dict[str, str]] = None
    RecordedOn: Optional[datetime] = None
    InclusionAnnotation: Optional[TimestampedInclusionAnnotation] = None


class UpdateClassifierRequest(BaseValidatorModel):
    GrokClassifier: Optional[UpdateGrokClassifierRequest] = None
    XMLClassifier: Optional[UpdateXMLClassifierRequest] = None
    JsonClassifier: Optional[UpdateJsonClassifierRequest] = None
    CsvClassifier: Optional[UpdateCsvClassifierRequest] = None


class ViewDefinitionInput(BaseValidatorModel):
    IsProtected: Optional[bool] = None
    Definer: Optional[str] = None
    Representations: Optional[Sequence[ViewRepresentationInput]] = None
    SubObjects: Optional[Sequence[str]] = None


class ViewDefinition(BaseValidatorModel):
    IsProtected: Optional[bool] = None
    Definer: Optional[str] = None
    SubObjects: Optional[List[str]] = None
    Representations: Optional[List[ViewRepresentation]] = None


class AggregateOperationUnion(BaseValidatorModel):
    pass


class Aggregate(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Groups: Sequence[Sequence[str]]
    Aggs: Sequence[AggregateOperationUnion]


class Property(BaseValidatorModel):
    pass


class AuthConfiguration(BaseValidatorModel):
    AuthenticationType: Property
    SecretArn: Optional[Property] = None
    OAuth2Properties: Optional[Dict[str, Property]] = None
    BasicAuthenticationProperties: Optional[Dict[str, Property]] = None
    CustomAuthenticationProperties: Optional[Dict[str, Property]] = None


class ComputeEnvironmentConfiguration(BaseValidatorModel):
    Name: str
    Description: str
    ComputeEnvironment: ComputeEnvironmentType
    SupportedAuthenticationTypes: List[AuthenticationTypeType]
    ConnectionOptions: Dict[str, Property]
    ConnectionPropertyNameOverrides: Dict[str, str]
    ConnectionOptionNameOverrides: Dict[str, str]
    ConnectionPropertiesRequiredOverrides: List[str]
    PhysicalConnectionPropertiesRequired: Optional[bool] = None


class AmazonRedshiftSourceOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataOutput] = None


class AmazonRedshiftTargetOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataOutput] = None
    Inputs: Optional[List[str]] = None


class SnowflakeTargetOutput(BaseValidatorModel):
    Name: str
    Data: SnowflakeNodeDataOutput
    Inputs: Optional[List[str]] = None


class KeySchemaElement(BaseValidatorModel):
    pass


class PartitionIndexDescriptor(BaseValidatorModel):
    IndexName: str
    Keys: List[KeySchemaElement]
    IndexStatus: PartitionIndexStatusType
    BackfillErrors: Optional[List[BackfillError]] = None


class BatchStopJobRunResponse(BaseValidatorModel):
    SuccessfulSubmissions: List[BatchStopJobRunSuccessfulSubmission]
    Errors: List[BatchStopJobRunError]
    ResponseMetadata: ResponseMetadata


class BatchUpdatePartitionResponse(BaseValidatorModel):
    Errors: List[BatchUpdatePartitionFailureEntry]
    ResponseMetadata: ResponseMetadata


class BatchCreatePartitionResponse(BaseValidatorModel):
    Errors: List[PartitionError]
    ResponseMetadata: ResponseMetadata


class BatchDeletePartitionResponse(BaseValidatorModel):
    Errors: List[PartitionError]
    ResponseMetadata: ResponseMetadata


class BatchDeleteTableResponse(BaseValidatorModel):
    Errors: List[TableError]
    ResponseMetadata: ResponseMetadata


class BatchDeleteTableVersionResponse(BaseValidatorModel):
    Errors: List[TableVersionError]
    ResponseMetadata: ResponseMetadata


class StatusDetailsPaginator(BaseValidatorModel):
    RequestedChange: Optional[Dict[str, Any]] = None
    ViewValidations: Optional[List[ViewValidation]] = None


class StatusDetails(BaseValidatorModel):
    RequestedChange: Optional[Dict[str, Any]] = None
    ViewValidations: Optional[List[ViewValidation]] = None


class BatchGetBlueprintsResponse(BaseValidatorModel):
    Blueprints: List[Blueprint]
    MissingBlueprints: List[str]
    ResponseMetadata: ResponseMetadata


class GetBlueprintResponse(BaseValidatorModel):
    Blueprint: Blueprint
    ResponseMetadata: ResponseMetadata


class ListConnectionTypesResponse(BaseValidatorModel):
    ConnectionTypes: List[ConnectionTypeBrief]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetClassifierResponse(BaseValidatorModel):
    Classifier: Classifier
    ResponseMetadata: ResponseMetadata


class GetClassifiersResponse(BaseValidatorModel):
    Classifiers: List[Classifier]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetDataflowGraphResponse(BaseValidatorModel):
    DagNodes: List[CodeGenNodeOutput]
    DagEdges: List[CodeGenEdge]
    ResponseMetadata: ResponseMetadata


class GetMappingRequest(BaseValidatorModel):
    Source: CatalogEntry
    Sinks: Optional[Sequence[CatalogEntry]] = None
    Location: Optional[Location] = None


class GetColumnStatisticsTaskSettingsResponse(BaseValidatorModel):
    ColumnStatisticsTaskSettings: ColumnStatisticsTaskSettings
    ResponseMetadata: ResponseMetadata


class GetUnfilteredPartitionMetadataRequest(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    SupportedPermissionTypes: Sequence[PermissionTypeType]
    Region: Optional[str] = None
    AuditContext: Optional[AuditContext] = None
    QuerySessionContext: Optional[QuerySessionContext] = None


class GetUnfilteredPartitionsMetadataRequest(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    SupportedPermissionTypes: Sequence[PermissionTypeType]
    Region: Optional[str] = None
    Expression: Optional[str] = None
    AuditContext: Optional[AuditContext] = None
    NextToken: Optional[str] = None
    Segment: Optional[Segment] = None
    MaxResults: Optional[int] = None
    QuerySessionContext: Optional[QuerySessionContext] = None


class GetUnfilteredTableMetadataRequest(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    Name: str
    SupportedPermissionTypes: Sequence[PermissionTypeType]
    Region: Optional[str] = None
    AuditContext: Optional[AuditContext] = None
    ParentResourceArn: Optional[str] = None
    RootResourceArn: Optional[str] = None
    SupportedDialect: Optional[SupportedDialect] = None
    Permissions: Optional[Sequence[PermissionType]] = None
    QuerySessionContext: Optional[QuerySessionContext] = None


class GetMLTaskRunsRequest(BaseValidatorModel):
    TransformId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[TaskRunFilterCriteria] = None
    Sort: Optional[TaskRunSortCriteria] = None


class ListDataQualityStatisticAnnotationsRequest(BaseValidatorModel):
    StatisticId: Optional[str] = None
    ProfileId: Optional[str] = None
    TimestampFilter: Optional[TimestampFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDataQualityStatisticsRequest(BaseValidatorModel):
    StatisticId: Optional[str] = None
    ProfileId: Optional[str] = None
    TimestampFilter: Optional[TimestampFilter] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetUsageProfileResponse(BaseValidatorModel):
    Name: str
    Description: str
    Configuration: ProfileConfigurationOutput
    CreatedOn: datetime
    LastModifiedOn: datetime
    ResponseMetadata: ResponseMetadata


class EvaluationMetrics(BaseValidatorModel):
    TransformType: Literal["FIND_MATCHES"]
    FindMatchesMetrics: Optional[FindMatchesMetrics] = None


class ConnectionsListUnion(BaseValidatorModel):
    pass


class CreateSessionRequest(BaseValidatorModel):
    Id: str
    Role: str
    Command: SessionCommand
    Description: Optional[str] = None
    Timeout: Optional[int] = None
    IdleTimeout: Optional[int] = None
    DefaultArguments: Optional[Mapping[str, str]] = None
    Connections: Optional[ConnectionsListUnion] = None
    MaxCapacity: Optional[float] = None
    NumberOfWorkers: Optional[int] = None
    WorkerType: Optional[WorkerTypeType] = None
    SecurityConfiguration: Optional[str] = None
    GlueVersion: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    RequestOrigin: Optional[str] = None


class Crawler(BaseValidatorModel):
    Name: Optional[str] = None
    Role: Optional[str] = None
    Targets: Optional[CrawlerTargetsOutput] = None
    DatabaseName: Optional[str] = None
    Description: Optional[str] = None
    Classifiers: Optional[List[str]] = None
    RecrawlPolicy: Optional[RecrawlPolicy] = None
    SchemaChangePolicy: Optional[SchemaChangePolicy] = None
    LineageConfiguration: Optional[LineageConfiguration] = None
    State: Optional[CrawlerStateType] = None
    TablePrefix: Optional[str] = None
    Schedule: Optional[Schedule] = None
    CrawlElapsedTime: Optional[int] = None
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    LastCrawl: Optional[LastCrawlInfo] = None
    Version: Optional[int] = None
    Configuration: Optional[str] = None
    CrawlerSecurityConfiguration: Optional[str] = None
    LakeFormationConfiguration: Optional[LakeFormationConfiguration] = None


class ListDataQualityRulesetsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[DataQualityRulesetFilterCriteria] = None
    Tags: Optional[Mapping[str, str]] = None


class ListDataQualityRulesetsResponse(BaseValidatorModel):
    Rulesets: List[DataQualityRulesetListDetails]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeInboundIntegrationsResponse(BaseValidatorModel):
    InboundIntegrations: List[InboundIntegration]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeIntegrationsResponse(BaseValidatorModel):
    Integrations: List[Integration]
    Marker: str
    ResponseMetadata: ResponseMetadata


class CreateSessionResponse(BaseValidatorModel):
    Session: Session
    ResponseMetadata: ResponseMetadata


class GetSessionResponse(BaseValidatorModel):
    Session: Session
    ResponseMetadata: ResponseMetadata


class ListSessionsResponse(BaseValidatorModel):
    Ids: List[str]
    Sessions: List[Session]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetDataCatalogEncryptionSettingsResponse(BaseValidatorModel):
    DataCatalogEncryptionSettings: DataCatalogEncryptionSettings
    ResponseMetadata: ResponseMetadata


class PutDataCatalogEncryptionSettingsRequest(BaseValidatorModel):
    DataCatalogEncryptionSettings: DataCatalogEncryptionSettings
    CatalogId: Optional[str] = None


class Catalog(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None
    ResourceArn: Optional[str] = None
    Description: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None
    CreateTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None
    TargetRedshiftCatalog: Optional[TargetRedshiftCatalog] = None
    FederatedCatalog: Optional[FederatedCatalog] = None
    CatalogProperties: Optional[CatalogPropertiesOutput] = None
    CreateTableDefaultPermissions: Optional[List[PrincipalPermissionsOutput]] = None
    CreateDatabaseDefaultPermissions: Optional[List[PrincipalPermissionsOutput]] = None


class Database(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    LocationUri: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None
    CreateTime: Optional[datetime] = None
    CreateTableDefaultPermissions: Optional[List[PrincipalPermissionsOutput]] = None
    TargetDatabase: Optional[DatabaseIdentifier] = None
    CatalogId: Optional[str] = None
    FederatedDatabase: Optional[FederatedDatabase] = None


class DataQualityObservation(BaseValidatorModel):
    Description: Optional[str] = None
    MetricBasedObservation: Optional[MetricBasedObservation] = None


class DataQualityResultDescription(BaseValidatorModel):
    ResultId: Optional[str] = None
    DataSource: Optional[DataSourceOutput] = None
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None
    StartedOn: Optional[datetime] = None


class DataQualityRuleRecommendationRunDescription(BaseValidatorModel):
    RunId: Optional[str] = None
    Status: Optional[TaskStatusTypeType] = None
    StartedOn: Optional[datetime] = None
    DataSource: Optional[DataSourceOutput] = None


class DataQualityRulesetEvaluationRunDescription(BaseValidatorModel):
    RunId: Optional[str] = None
    Status: Optional[TaskStatusTypeType] = None
    StartedOn: Optional[datetime] = None
    DataSource: Optional[DataSourceOutput] = None


class GetDataQualityRuleRecommendationRunResponse(BaseValidatorModel):
    RunId: str
    DataSource: DataSourceOutput
    Role: str
    NumberOfWorkers: int
    Timeout: int
    Status: TaskStatusTypeType
    ErrorString: str
    StartedOn: datetime
    LastModifiedOn: datetime
    CompletedOn: datetime
    ExecutionTime: int
    RecommendedRuleset: str
    CreatedRulesetName: str
    DataQualitySecurityConfiguration: str
    ResponseMetadata: ResponseMetadata


class GetDataQualityRulesetEvaluationRunResponse(BaseValidatorModel):
    RunId: str
    DataSource: DataSourceOutput
    Role: str
    NumberOfWorkers: int
    Timeout: int
    AdditionalRunOptions: DataQualityEvaluationRunAdditionalRunOptions
    Status: TaskStatusTypeType
    ErrorString: str
    StartedOn: datetime
    LastModifiedOn: datetime
    CompletedOn: datetime
    ExecutionTime: int
    RulesetNames: List[str]
    ResultIds: List[str]
    AdditionalDataSources: Dict[str, DataSourceOutput]
    ResponseMetadata: ResponseMetadata


class DropNullFieldsOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    NullCheckBoxList: Optional[NullCheckBoxList] = None
    NullTextList: Optional[List[NullValueField]] = None


class DropNullFields(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    NullCheckBoxList: Optional[NullCheckBoxList] = None
    NullTextList: Optional[Sequence[NullValueField]] = None


class ColumnOutput(BaseValidatorModel):
    pass


class StorageDescriptorOutput(BaseValidatorModel):
    Columns: Optional[List[ColumnOutput]] = None
    Location: Optional[str] = None
    AdditionalLocations: Optional[List[str]] = None
    InputFormat: Optional[str] = None
    OutputFormat: Optional[str] = None
    Compressed: Optional[bool] = None
    NumberOfBuckets: Optional[int] = None
    SerdeInfo: Optional[SerDeInfoOutput] = None
    BucketColumns: Optional[List[str]] = None
    SortColumns: Optional[List[Order]] = None
    Parameters: Optional[Dict[str, str]] = None
    SkewedInfo: Optional[SkewedInfoOutput] = None
    StoredAsSubDirectories: Optional[bool] = None
    SchemaReference: Optional[SchemaReference] = None


class SecurityConfiguration(BaseValidatorModel):
    Name: Optional[str] = None
    CreatedTimeStamp: Optional[datetime] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationOutput] = None


class DeleteSchemaVersionsResponse(BaseValidatorModel):
    SchemaVersionErrors: List[SchemaVersionErrorItem]
    ResponseMetadata: ResponseMetadata


class FilterOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    LogicalOperator: FilterLogicalOperatorType
    Filters: List[FilterExpressionOutput]


class FilterValueUnion(BaseValidatorModel):
    pass


class FilterExpression(BaseValidatorModel):
    Operation: FilterOperationType
    Values: Sequence[FilterValueUnion]
    Negated: Optional[bool] = None


class UpdateMLTransformRequest(BaseValidatorModel):
    TransformId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Parameters: Optional[TransformParameters] = None
    Role: Optional[str] = None
    GlueVersion: Optional[str] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    MaxRetries: Optional[int] = None


class GetMLTransformsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[TransformFilterCriteria] = None
    Sort: Optional[TransformSortCriteria] = None


class ListMLTransformsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[TransformFilterCriteria] = None
    Sort: Optional[TransformSortCriteria] = None
    Tags: Optional[Mapping[str, str]] = None


class AthenaConnectorSourceOutput(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    SchemaName: str
    ConnectionTable: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class CatalogDeltaSourceOutput(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class CatalogHudiSourceOutput(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class ConnectorDataSourceOutput(BaseValidatorModel):
    Name: str
    ConnectionType: str
    Data: Dict[str, str]
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class CustomCodeOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Code: str
    ClassName: str
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class TransformConfigParameterOutput(BaseValidatorModel):
    pass


class DynamicTransformOutput(BaseValidatorModel):
    Name: str
    TransformName: str
    Inputs: List[str]
    FunctionName: str
    Path: str
    Parameters: Optional[List[TransformConfigParameterOutput]] = None
    Version: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class JDBCConnectorSourceOutput(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[JDBCConnectorOptionsOutput] = None
    ConnectionTable: Optional[str] = None
    Query: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class JDBCConnectorTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    ConnectionName: str
    ConnectionTable: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class S3CatalogDeltaSourceOutput(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class S3CatalogHudiSourceOutput(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class S3CsvSourceOutput(BaseValidatorModel):
    Name: str
    Paths: List[str]
    Separator: SeparatorType
    QuoteChar: QuoteCharType
    CompressionType: Optional[CompressionTypeType] = None
    Exclusions: Optional[List[str]] = None
    GroupSize: Optional[str] = None
    GroupFiles: Optional[str] = None
    Recurse: Optional[bool] = None
    MaxBand: Optional[int] = None
    MaxFilesInBand: Optional[int] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions] = None
    Escaper: Optional[str] = None
    Multiline: Optional[bool] = None
    WithHeader: Optional[bool] = None
    WriteHeader: Optional[bool] = None
    SkipFirst: Optional[bool] = None
    OptimizePerformance: Optional[bool] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class S3DeltaSourceOutput(BaseValidatorModel):
    Name: str
    Paths: List[str]
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class S3HudiSourceOutput(BaseValidatorModel):
    Name: str
    Paths: List[str]
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class S3JsonSourceOutput(BaseValidatorModel):
    Name: str
    Paths: List[str]
    CompressionType: Optional[CompressionTypeType] = None
    Exclusions: Optional[List[str]] = None
    GroupSize: Optional[str] = None
    GroupFiles: Optional[str] = None
    Recurse: Optional[bool] = None
    MaxBand: Optional[int] = None
    MaxFilesInBand: Optional[int] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions] = None
    JsonPath: Optional[str] = None
    Multiline: Optional[bool] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class S3ParquetSourceOutput(BaseValidatorModel):
    Name: str
    Paths: List[str]
    CompressionType: Optional[ParquetCompressionTypeType] = None
    Exclusions: Optional[List[str]] = None
    GroupSize: Optional[str] = None
    GroupFiles: Optional[str] = None
    Recurse: Optional[bool] = None
    MaxBand: Optional[int] = None
    MaxFilesInBand: Optional[int] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class SnowflakeSourceOutput(BaseValidatorModel):
    Name: str
    Data: SnowflakeNodeDataOutput
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class SparkConnectorSourceOutput(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class SparkConnectorTargetOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class SparkSQLOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    SqlQuery: str
    SqlAliases: List[SqlAlias]
    OutputSchemas: Optional[List[GlueSchemaOutput]] = None


class AthenaConnectorSource(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    SchemaName: str
    ConnectionTable: Optional[str] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class CatalogDeltaSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class CatalogHudiSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class CustomCode(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Code: str
    ClassName: str
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class JDBCConnectorTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    ConnectionName: str
    ConnectionTable: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class S3CatalogDeltaSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class S3CatalogHudiSource(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class S3CsvSource(BaseValidatorModel):
    Name: str
    Paths: Sequence[str]
    Separator: SeparatorType
    QuoteChar: QuoteCharType
    CompressionType: Optional[CompressionTypeType] = None
    Exclusions: Optional[Sequence[str]] = None
    GroupSize: Optional[str] = None
    GroupFiles: Optional[str] = None
    Recurse: Optional[bool] = None
    MaxBand: Optional[int] = None
    MaxFilesInBand: Optional[int] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions] = None
    Escaper: Optional[str] = None
    Multiline: Optional[bool] = None
    WithHeader: Optional[bool] = None
    WriteHeader: Optional[bool] = None
    SkipFirst: Optional[bool] = None
    OptimizePerformance: Optional[bool] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class S3DeltaSource(BaseValidatorModel):
    Name: str
    Paths: Sequence[str]
    AdditionalDeltaOptions: Optional[Mapping[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class S3HudiSource(BaseValidatorModel):
    Name: str
    Paths: Sequence[str]
    AdditionalHudiOptions: Optional[Mapping[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class S3JsonSource(BaseValidatorModel):
    Name: str
    Paths: Sequence[str]
    CompressionType: Optional[CompressionTypeType] = None
    Exclusions: Optional[Sequence[str]] = None
    GroupSize: Optional[str] = None
    GroupFiles: Optional[str] = None
    Recurse: Optional[bool] = None
    MaxBand: Optional[int] = None
    MaxFilesInBand: Optional[int] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions] = None
    JsonPath: Optional[str] = None
    Multiline: Optional[bool] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class S3ParquetSource(BaseValidatorModel):
    Name: str
    Paths: Sequence[str]
    CompressionType: Optional[ParquetCompressionTypeType] = None
    Exclusions: Optional[Sequence[str]] = None
    GroupSize: Optional[str] = None
    GroupFiles: Optional[str] = None
    Recurse: Optional[bool] = None
    MaxBand: Optional[int] = None
    MaxFilesInBand: Optional[int] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptions] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class SparkConnectorSource(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class SparkConnectorTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class SparkSQL(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    SqlQuery: str
    SqlAliases: Sequence[SqlAlias]
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class GlueTableUnion(BaseValidatorModel):
    pass


class DataSource(BaseValidatorModel):
    GlueTable: GlueTableUnion


class TableOptimizerConfiguration(BaseValidatorModel):
    roleArn: Optional[str] = None
    enabled: Optional[bool] = None
    vpcConfiguration: Optional[TableOptimizerVpcConfiguration] = None
    retentionConfiguration: Optional[RetentionConfiguration] = None
    orphanFileDeletionConfiguration: Optional[OrphanFileDeletionConfiguration] = None


class TableOptimizerRun(BaseValidatorModel):
    eventType: Optional[TableOptimizerEventTypeType] = None
    startTimestamp: Optional[datetime] = None
    endTimestamp: Optional[datetime] = None
    metrics: Optional[RunMetrics] = None
    error: Optional[str] = None
    compactionMetrics: Optional[CompactionMetrics] = None
    retentionMetrics: Optional[RetentionMetrics] = None
    orphanFileDeletionMetrics: Optional[OrphanFileDeletionMetrics] = None


class GetIntegrationTablePropertiesResponse(BaseValidatorModel):
    ResourceArn: str
    TableName: str
    SourceTableConfig: SourceTableConfigOutput
    TargetTableConfig: TargetTableConfigOutput
    ResponseMetadata: ResponseMetadata


class JDBCConnectorOptionsUnion(BaseValidatorModel):
    pass


class JDBCConnectorSource(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[JDBCConnectorOptionsUnion] = None
    ConnectionTable: Optional[str] = None
    Query: Optional[str] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class GetJobRunResponse(BaseValidatorModel):
    JobRun: JobRun
    ResponseMetadata: ResponseMetadata


class GetJobRunsResponse(BaseValidatorModel):
    JobRuns: List[JobRun]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class JobNodeDetails(BaseValidatorModel):
    JobRuns: Optional[List[JobRun]] = None


class JoinColumnUnion(BaseValidatorModel):
    pass


class Join(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    JoinType: JoinTypeType
    Columns: Sequence[JoinColumnUnion]


class GetMLTaskRunResponse(BaseValidatorModel):
    TransformId: str
    TaskRunId: str
    Status: TaskStatusTypeType
    LogGroupName: str
    Properties: TaskRunProperties
    ErrorString: str
    StartedOn: datetime
    LastModifiedOn: datetime
    CompletedOn: datetime
    ExecutionTime: int
    ResponseMetadata: ResponseMetadata


class TaskRun(BaseValidatorModel):
    TransformId: Optional[str] = None
    TaskRunId: Optional[str] = None
    Status: Optional[TaskStatusTypeType] = None
    LogGroupName: Optional[str] = None
    Properties: Optional[TaskRunProperties] = None
    ErrorString: Optional[str] = None
    StartedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    CompletedOn: Optional[datetime] = None
    ExecutionTime: Optional[int] = None


class CreateMLTransformRequest(BaseValidatorModel):
    Name: str
    InputRecordTables: Sequence[GlueTableUnion]
    Parameters: TransformParameters
    Role: str
    Description: Optional[str] = None
    GlueVersion: Optional[str] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    MaxRetries: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None
    TransformEncryption: Optional[TransformEncryption] = None


class QuerySchemaVersionMetadataResponse(BaseValidatorModel):
    MetadataInfoMap: Dict[str, MetadataInfo]
    SchemaVersionId: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AuthenticationConfiguration(BaseValidatorModel):
    AuthenticationType: Optional[AuthenticationTypeType] = None
    SecretArn: Optional[str] = None
    OAuth2Properties: Optional[OAuth2Properties] = None


class AuthenticationConfigurationInput(BaseValidatorModel):
    AuthenticationType: Optional[AuthenticationTypeType] = None
    OAuth2Properties: Optional[OAuth2PropertiesInput] = None
    SecretArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    BasicAuthenticationCredentials: Optional[BasicAuthenticationCredentials] = None
    CustomAuthenticationCredentials: Optional[Mapping[str, str]] = None


class PartitionValueListUnion(BaseValidatorModel):
    pass


class BatchDeletePartitionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionsToDelete: Sequence[PartitionValueListUnion]
    CatalogId: Optional[str] = None


class BatchGetPartitionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionsToGet: Sequence[PartitionValueListUnion]
    CatalogId: Optional[str] = None


class RecipeOutput(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    RecipeReference: Optional[RecipeReference] = None
    RecipeSteps: Optional[List[RecipeStepOutput]] = None


class RecipeActionUnion(BaseValidatorModel):
    pass


class RecipeStep(BaseValidatorModel):
    Action: RecipeActionUnion
    ConditionExpressions: Optional[Sequence[ConditionExpression]] = None


class CreateUserDefinedFunctionRequest(BaseValidatorModel):
    DatabaseName: str
    FunctionInput: UserDefinedFunctionInput
    CatalogId: Optional[str] = None


class UpdateUserDefinedFunctionRequest(BaseValidatorModel):
    DatabaseName: str
    FunctionName: str
    FunctionInput: UserDefinedFunctionInput
    CatalogId: Optional[str] = None


class GetUserDefinedFunctionResponse(BaseValidatorModel):
    UserDefinedFunction: UserDefinedFunction
    ResponseMetadata: ResponseMetadata


class GetUserDefinedFunctionsResponse(BaseValidatorModel):
    UserDefinedFunctions: List[UserDefinedFunction]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ColumnUnion(BaseValidatorModel):
    pass


class SerDeInfoUnion(BaseValidatorModel):
    pass


class SkewedInfoUnion(BaseValidatorModel):
    pass


class StorageDescriptor(BaseValidatorModel):
    Columns: Optional[Sequence[ColumnUnion]] = None
    Location: Optional[str] = None
    AdditionalLocations: Optional[Sequence[str]] = None
    InputFormat: Optional[str] = None
    OutputFormat: Optional[str] = None
    Compressed: Optional[bool] = None
    NumberOfBuckets: Optional[int] = None
    SerdeInfo: Optional[SerDeInfoUnion] = None
    BucketColumns: Optional[Sequence[str]] = None
    SortColumns: Optional[Sequence[Order]] = None
    Parameters: Optional[Mapping[str, str]] = None
    SkewedInfo: Optional[SkewedInfoUnion] = None
    StoredAsSubDirectories: Optional[bool] = None
    SchemaReference: Optional[SchemaReference] = None


class Statement(BaseValidatorModel):
    Id: Optional[int] = None
    Code: Optional[str] = None
    State: Optional[StatementStateType] = None
    Output: Optional[StatementOutput] = None
    Progress: Optional[float] = None
    StartedOn: Optional[int] = None
    CompletedOn: Optional[int] = None


class ListDataQualityStatisticAnnotationsResponse(BaseValidatorModel):
    Annotations: List[StatisticAnnotation]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDataQualityStatisticsResponse(BaseValidatorModel):
    Statistics: List[StatisticSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TransformConfigParameterUnion(BaseValidatorModel):
    pass


class DynamicTransform(BaseValidatorModel):
    Name: str
    TransformName: str
    Inputs: Sequence[str]
    FunctionName: str
    Path: str
    Parameters: Optional[Sequence[TransformConfigParameterUnion]] = None
    Version: Optional[str] = None
    OutputSchemas: Optional[Sequence[GlueSchema]] = None


class UpsertRedshiftTargetOptionsUnion(BaseValidatorModel):
    pass


class RedshiftTarget(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str
    RedshiftTmpDir: Optional[str] = None
    TmpDirIAMRole: Optional[str] = None
    UpsertRedshiftOptions: Optional[UpsertRedshiftTargetOptionsUnion] = None


class DescribeConnectionTypeResponse(BaseValidatorModel):
    ConnectionType: str
    Description: str
    Capabilities: Capabilities
    ConnectionProperties: Dict[str, Property]
    ConnectionOptions: Dict[str, Property]
    AuthenticationConfiguration: AuthConfiguration
    ComputeEnvironmentConfigurations: Dict[str, ComputeEnvironmentConfiguration]
    PhysicalConnectionRequirements: Dict[str, Property]
    AthenaConnectionProperties: Dict[str, Property]
    PythonConnectionProperties: Dict[str, Property]
    SparkConnectionProperties: Dict[str, Property]
    ResponseMetadata: ResponseMetadata


class AmazonRedshiftNodeDataUnion(BaseValidatorModel):
    pass


class AmazonRedshiftSource(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataUnion] = None


class AmazonRedshiftTarget(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataUnion] = None
    Inputs: Optional[Sequence[str]] = None


class SnowflakeNodeDataUnion(BaseValidatorModel):
    pass


class SnowflakeTarget(BaseValidatorModel):
    Name: str
    Data: SnowflakeNodeDataUnion
    Inputs: Optional[Sequence[str]] = None


class GetPartitionIndexesResponse(BaseValidatorModel):
    PartitionIndexDescriptorList: List[PartitionIndexDescriptor]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TableStatusPaginator(BaseValidatorModel):
    RequestedBy: Optional[str] = None
    UpdatedBy: Optional[str] = None
    RequestTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None
    Action: Optional[ResourceActionType] = None
    State: Optional[ResourceStateType] = None
    Error: Optional[ErrorDetail] = None
    Details: Optional[StatusDetailsPaginator] = None


class TableStatus(BaseValidatorModel):
    RequestedBy: Optional[str] = None
    UpdatedBy: Optional[str] = None
    RequestTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None
    Action: Optional[ResourceActionType] = None
    State: Optional[ResourceStateType] = None
    Error: Optional[ErrorDetail] = None
    Details: Optional[StatusDetails] = None


class DecimalNumberUnion(BaseValidatorModel):
    pass


class DecimalColumnStatisticsData(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[DecimalNumberUnion] = None
    MaximumValue: Optional[DecimalNumberUnion] = None


class CodeGenNodeUnion(BaseValidatorModel):
    pass


class CreateScriptRequest(BaseValidatorModel):
    DagNodes: Optional[Sequence[CodeGenNodeUnion]] = None
    DagEdges: Optional[Sequence[CodeGenEdge]] = None
    Language: Optional[LanguageType] = None


class KafkaStreamingSourceOptionsUnion(BaseValidatorModel):
    pass


class CatalogKafkaSource(BaseValidatorModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KafkaStreamingSourceOptionsUnion] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptions] = None


class DirectKafkaSource(BaseValidatorModel):
    Name: str
    StreamingOptions: Optional[KafkaStreamingSourceOptionsUnion] = None
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptions] = None


class KinesisStreamingSourceOptionsUnion(BaseValidatorModel):
    pass


class CatalogKinesisSource(BaseValidatorModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsUnion] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptions] = None


class DirectKinesisSource(BaseValidatorModel):
    Name: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsUnion] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptions] = None


class Trigger(BaseValidatorModel):
    pass


class BatchGetTriggersResponse(BaseValidatorModel):
    Triggers: List[Trigger]
    TriggersNotFound: List[str]
    ResponseMetadata: ResponseMetadata


class GetTriggerResponse(BaseValidatorModel):
    Trigger: Trigger
    ResponseMetadata: ResponseMetadata


class GetTriggersResponse(BaseValidatorModel):
    Triggers: List[Trigger]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TriggerNodeDetails(BaseValidatorModel):
    Trigger: Optional[Trigger] = None


class UpdateTriggerResponse(BaseValidatorModel):
    Trigger: Trigger
    ResponseMetadata: ResponseMetadata


class PredicateUnion(BaseValidatorModel):
    pass


class ActionUnion(BaseValidatorModel):
    pass


class TriggerUpdate(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Schedule: Optional[str] = None
    Actions: Optional[Sequence[ActionUnion]] = None
    Predicate: Optional[PredicateUnion] = None
    EventBatchingCondition: Optional[EventBatchingCondition] = None


class ProfileConfigurationUnion(BaseValidatorModel):
    pass


class CreateUsageProfileRequest(BaseValidatorModel):
    Name: str
    Configuration: ProfileConfigurationUnion
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateUsageProfileRequest(BaseValidatorModel):
    Name: str
    Configuration: ProfileConfigurationUnion
    Description: Optional[str] = None


class GetMLTransformResponse(BaseValidatorModel):
    TransformId: str
    Name: str
    Description: str
    Status: TransformStatusTypeType
    CreatedOn: datetime
    LastModifiedOn: datetime
    InputRecordTables: List[GlueTableOutput]
    Parameters: TransformParameters
    EvaluationMetrics: EvaluationMetrics
    LabelCount: int
    Schema: List[SchemaColumn]
    Role: str
    GlueVersion: str
    MaxCapacity: float
    WorkerType: WorkerTypeType
    NumberOfWorkers: int
    Timeout: int
    MaxRetries: int
    TransformEncryption: TransformEncryption
    ResponseMetadata: ResponseMetadata


class MLTransform(BaseValidatorModel):
    TransformId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[TransformStatusTypeType] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    InputRecordTables: Optional[List[GlueTableOutput]] = None
    Parameters: Optional[TransformParameters] = None
    EvaluationMetrics: Optional[EvaluationMetrics] = None
    LabelCount: Optional[int] = None
    Schema: Optional[List[SchemaColumn]] = None
    Role: Optional[str] = None
    GlueVersion: Optional[str] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    MaxRetries: Optional[int] = None
    TransformEncryption: Optional[TransformEncryption] = None


class BatchGetCrawlersResponse(BaseValidatorModel):
    Crawlers: List[Crawler]
    CrawlersNotFound: List[str]
    ResponseMetadata: ResponseMetadata


class GetCrawlerResponse(BaseValidatorModel):
    Crawler: Crawler
    ResponseMetadata: ResponseMetadata


class GetCrawlersResponse(BaseValidatorModel):
    Crawlers: List[Crawler]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CrawlerTargetsUnion(BaseValidatorModel):
    pass


class CreateCrawlerRequest(BaseValidatorModel):
    Name: str
    Role: str
    Targets: CrawlerTargetsUnion
    DatabaseName: Optional[str] = None
    Description: Optional[str] = None
    Schedule: Optional[str] = None
    Classifiers: Optional[Sequence[str]] = None
    TablePrefix: Optional[str] = None
    SchemaChangePolicy: Optional[SchemaChangePolicy] = None
    RecrawlPolicy: Optional[RecrawlPolicy] = None
    LineageConfiguration: Optional[LineageConfiguration] = None
    LakeFormationConfiguration: Optional[LakeFormationConfiguration] = None
    Configuration: Optional[str] = None
    CrawlerSecurityConfiguration: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateCrawlerRequest(BaseValidatorModel):
    Name: str
    Role: Optional[str] = None
    DatabaseName: Optional[str] = None
    Description: Optional[str] = None
    Targets: Optional[CrawlerTargetsUnion] = None
    Schedule: Optional[str] = None
    Classifiers: Optional[Sequence[str]] = None
    TablePrefix: Optional[str] = None
    SchemaChangePolicy: Optional[SchemaChangePolicy] = None
    RecrawlPolicy: Optional[RecrawlPolicy] = None
    LineageConfiguration: Optional[LineageConfiguration] = None
    LakeFormationConfiguration: Optional[LakeFormationConfiguration] = None
    Configuration: Optional[str] = None
    CrawlerSecurityConfiguration: Optional[str] = None


class GetCatalogResponse(BaseValidatorModel):
    Catalog: Catalog
    ResponseMetadata: ResponseMetadata


class GetCatalogsResponse(BaseValidatorModel):
    CatalogList: List[Catalog]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetDatabaseResponse(BaseValidatorModel):
    Database: Database
    ResponseMetadata: ResponseMetadata


class GetDatabasesResponse(BaseValidatorModel):
    DatabaseList: List[Database]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PrincipalPermissionsUnion(BaseValidatorModel):
    pass


class CatalogInput(BaseValidatorModel):
    Description: Optional[str] = None
    FederatedCatalog: Optional[FederatedCatalog] = None
    Parameters: Optional[Mapping[str, str]] = None
    TargetRedshiftCatalog: Optional[TargetRedshiftCatalog] = None
    CatalogProperties: Optional[CatalogProperties] = None
    CreateTableDefaultPermissions: Optional[Sequence[PrincipalPermissionsUnion]] = None
    CreateDatabaseDefaultPermissions: Optional[Sequence[PrincipalPermissionsUnion]] = None


class DatabaseInput(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    LocationUri: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    CreateTableDefaultPermissions: Optional[Sequence[PrincipalPermissionsUnion]] = None
    TargetDatabase: Optional[DatabaseIdentifier] = None
    FederatedDatabase: Optional[FederatedDatabase] = None


class DataQualityResult(BaseValidatorModel):
    ResultId: Optional[str] = None
    ProfileId: Optional[str] = None
    Score: Optional[float] = None
    DataSource: Optional[DataSourceOutput] = None
    RulesetName: Optional[str] = None
    EvaluationContext: Optional[str] = None
    StartedOn: Optional[datetime] = None
    CompletedOn: Optional[datetime] = None
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None
    RulesetEvaluationRunId: Optional[str] = None
    RuleResults: Optional[List[DataQualityRuleResult]] = None
    AnalyzerResults: Optional[List[DataQualityAnalyzerResult]] = None
    Observations: Optional[List[DataQualityObservation]] = None


class GetDataQualityResultResponse(BaseValidatorModel):
    ResultId: str
    ProfileId: str
    Score: float
    DataSource: DataSourceOutput
    RulesetName: str
    EvaluationContext: str
    StartedOn: datetime
    CompletedOn: datetime
    JobName: str
    JobRunId: str
    RulesetEvaluationRunId: str
    RuleResults: List[DataQualityRuleResult]
    AnalyzerResults: List[DataQualityAnalyzerResult]
    Observations: List[DataQualityObservation]
    ResponseMetadata: ResponseMetadata


class ListDataQualityResultsResponse(BaseValidatorModel):
    Results: List[DataQualityResultDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDataQualityRuleRecommendationRunsResponse(BaseValidatorModel):
    Runs: List[DataQualityRuleRecommendationRunDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDataQualityRulesetEvaluationRunsResponse(BaseValidatorModel):
    Runs: List[DataQualityRulesetEvaluationRunDescription]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ColumnStatisticsDataOutput(BaseValidatorModel):
    pass


class ColumnStatisticsOutput(BaseValidatorModel):
    ColumnName: str
    ColumnType: str
    AnalyzedTime: datetime
    StatisticsData: ColumnStatisticsDataOutput


class Partition(BaseValidatorModel):
    Values: Optional[List[str]] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastAccessTime: Optional[datetime] = None
    StorageDescriptor: Optional[StorageDescriptorOutput] = None
    Parameters: Optional[Dict[str, str]] = None
    LastAnalyzedTime: Optional[datetime] = None
    CatalogId: Optional[str] = None


class GetSecurityConfigurationResponse(BaseValidatorModel):
    SecurityConfiguration: SecurityConfiguration
    ResponseMetadata: ResponseMetadata


class GetSecurityConfigurationsResponse(BaseValidatorModel):
    SecurityConfigurations: List[SecurityConfiguration]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EncryptionConfigurationUnion(BaseValidatorModel):
    pass


class CreateSecurityConfigurationRequest(BaseValidatorModel):
    Name: str
    EncryptionConfiguration: EncryptionConfigurationUnion


class GlueSchemaUnion(BaseValidatorModel):
    pass


class ConnectorDataSource(BaseValidatorModel):
    Name: str
    ConnectionType: str
    Data: Mapping[str, str]
    OutputSchemas: Optional[Sequence[GlueSchemaUnion]] = None


class SnowflakeSource(BaseValidatorModel):
    Name: str
    Data: SnowflakeNodeDataUnion
    OutputSchemas: Optional[Sequence[GlueSchemaUnion]] = None


class ListTableOptimizerRunsResponse(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    TableOptimizerRuns: List[TableOptimizerRun]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SourceTableConfigUnion(BaseValidatorModel):
    pass


class TargetTableConfigUnion(BaseValidatorModel):
    pass


class CreateIntegrationTablePropertiesRequest(BaseValidatorModel):
    ResourceArn: str
    TableName: str
    SourceTableConfig: Optional[SourceTableConfigUnion] = None
    TargetTableConfig: Optional[TargetTableConfigUnion] = None


class UpdateIntegrationTablePropertiesRequest(BaseValidatorModel):
    ResourceArn: str
    TableName: str
    SourceTableConfig: Optional[SourceTableConfigUnion] = None
    TargetTableConfig: Optional[TargetTableConfigUnion] = None


class GetMLTaskRunsResponse(BaseValidatorModel):
    TaskRuns: List[TaskRun]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Connection(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    ConnectionType: Optional[ConnectionTypeType] = None
    MatchCriteria: Optional[List[str]] = None
    ConnectionProperties: Optional[Dict[ConnectionPropertyKeyType, str]] = None
    SparkProperties: Optional[Dict[str, str]] = None
    AthenaProperties: Optional[Dict[str, str]] = None
    PythonProperties: Optional[Dict[str, str]] = None
    PhysicalConnectionRequirements: Optional[PhysicalConnectionRequirementsOutput] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    LastUpdatedBy: Optional[str] = None
    Status: Optional[ConnectionStatusType] = None
    StatusReason: Optional[str] = None
    LastConnectionValidationTime: Optional[datetime] = None
    AuthenticationConfiguration: Optional[AuthenticationConfiguration] = None
    ConnectionSchemaVersion: Optional[int] = None
    CompatibleComputeEnvironments: Optional[List[ComputeEnvironmentType]] = None


class PhysicalConnectionRequirementsUnion(BaseValidatorModel):
    pass


class ConnectionInput(BaseValidatorModel):
    Name: str
    ConnectionType: ConnectionTypeType
    ConnectionProperties: Mapping[ConnectionPropertyKeyType, str]
    Description: Optional[str] = None
    MatchCriteria: Optional[Sequence[str]] = None
    SparkProperties: Optional[Mapping[str, str]] = None
    AthenaProperties: Optional[Mapping[str, str]] = None
    PythonProperties: Optional[Mapping[str, str]] = None
    PhysicalConnectionRequirements: Optional[PhysicalConnectionRequirementsUnion] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationInput] = None
    ValidateCredentials: Optional[bool] = None
    ValidateForComputeEnvironments: Optional[Sequence[ComputeEnvironmentType]] = None


class TestConnectionInput(BaseValidatorModel):
    ConnectionType: ConnectionTypeType
    ConnectionProperties: Mapping[ConnectionPropertyKeyType, str]
    AuthenticationConfiguration: Optional[AuthenticationConfigurationInput] = None


class GetStatementResponse(BaseValidatorModel):
    Statement: Statement
    ResponseMetadata: ResponseMetadata


class ListStatementsResponse(BaseValidatorModel):
    Statements: List[Statement]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TablePaginator(BaseValidatorModel):
    Name: str
    DatabaseName: Optional[str] = None
    Description: Optional[str] = None
    Owner: Optional[str] = None
    CreateTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None
    LastAccessTime: Optional[datetime] = None
    LastAnalyzedTime: Optional[datetime] = None
    Retention: Optional[int] = None
    StorageDescriptor: Optional[StorageDescriptorOutput] = None
    PartitionKeys: Optional[List[ColumnOutput]] = None
    ViewOriginalText: Optional[str] = None
    ViewExpandedText: Optional[str] = None
    TableType: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None
    CreatedBy: Optional[str] = None
    IsRegisteredWithLakeFormation: Optional[bool] = None
    TargetTable: Optional[TableIdentifier] = None
    CatalogId: Optional[str] = None
    VersionId: Optional[str] = None
    FederatedTable: Optional[FederatedTable] = None
    ViewDefinition: Optional[ViewDefinition] = None
    IsMultiDialectView: Optional[bool] = None
    Status: Optional[TableStatusPaginator] = None


class Table(BaseValidatorModel):
    Name: str
    DatabaseName: Optional[str] = None
    Description: Optional[str] = None
    Owner: Optional[str] = None
    CreateTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None
    LastAccessTime: Optional[datetime] = None
    LastAnalyzedTime: Optional[datetime] = None
    Retention: Optional[int] = None
    StorageDescriptor: Optional[StorageDescriptorOutput] = None
    PartitionKeys: Optional[List[ColumnOutput]] = None
    ViewOriginalText: Optional[str] = None
    ViewExpandedText: Optional[str] = None
    TableType: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None
    CreatedBy: Optional[str] = None
    IsRegisteredWithLakeFormation: Optional[bool] = None
    TargetTable: Optional[TableIdentifier] = None
    CatalogId: Optional[str] = None
    VersionId: Optional[str] = None
    FederatedTable: Optional[FederatedTable] = None
    ViewDefinition: Optional[ViewDefinition] = None
    IsMultiDialectView: Optional[bool] = None
    Status: Optional[TableStatus] = None


class UpdateTriggerRequest(BaseValidatorModel):
    Name: str
    TriggerUpdate: TriggerUpdate


class GetMLTransformsResponse(BaseValidatorModel):
    Transforms: List[MLTransform]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateCatalogRequest(BaseValidatorModel):
    Name: str
    CatalogInput: CatalogInput
    Tags: Optional[Mapping[str, str]] = None


class UpdateCatalogRequest(BaseValidatorModel):
    CatalogId: str
    CatalogInput: CatalogInput


class CreateDatabaseRequest(BaseValidatorModel):
    DatabaseInput: DatabaseInput
    CatalogId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateDatabaseRequest(BaseValidatorModel):
    Name: str
    DatabaseInput: DatabaseInput
    CatalogId: Optional[str] = None


class BatchGetDataQualityResultResponse(BaseValidatorModel):
    Results: List[DataQualityResult]
    ResultsNotFound: List[str]
    ResponseMetadata: ResponseMetadata


class ColumnStatisticsError(BaseValidatorModel):
    ColumnStatistics: Optional[ColumnStatisticsOutput] = None
    Error: Optional[ErrorDetail] = None


class GetColumnStatisticsForPartitionResponse(BaseValidatorModel):
    ColumnStatisticsList: List[ColumnStatisticsOutput]
    Errors: List[ColumnError]
    ResponseMetadata: ResponseMetadata


class GetColumnStatisticsForTableResponse(BaseValidatorModel):
    ColumnStatisticsList: List[ColumnStatisticsOutput]
    Errors: List[ColumnError]
    ResponseMetadata: ResponseMetadata


class BatchGetPartitionResponse(BaseValidatorModel):
    Partitions: List[Partition]
    UnprocessedKeys: List[PartitionValueListOutput]
    ResponseMetadata: ResponseMetadata


class GetPartitionResponse(BaseValidatorModel):
    Partition: Partition
    ResponseMetadata: ResponseMetadata


class GetPartitionsResponse(BaseValidatorModel):
    Partitions: List[Partition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetUnfilteredPartitionMetadataResponse(BaseValidatorModel):
    Partition: Partition
    AuthorizedColumns: List[str]
    IsRegisteredWithLakeFormation: bool
    ResponseMetadata: ResponseMetadata


class UnfilteredPartition(BaseValidatorModel):
    Partition: Optional[Partition] = None
    AuthorizedColumns: Optional[List[str]] = None
    IsRegisteredWithLakeFormation: Optional[bool] = None


class FilterExpressionUnion(BaseValidatorModel):
    pass


class Filter(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    LogicalOperator: FilterLogicalOperatorType
    Filters: Sequence[FilterExpressionUnion]


class DataSourceUnion(BaseValidatorModel):
    pass


class DataQualityResultFilterCriteria(BaseValidatorModel):
    DataSource: Optional[DataSourceUnion] = None
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None
    StartedAfter: Optional[Timestamp] = None
    StartedBefore: Optional[Timestamp] = None


class DataQualityRuleRecommendationRunFilter(BaseValidatorModel):
    DataSource: DataSourceUnion
    StartedBefore: Optional[Timestamp] = None
    StartedAfter: Optional[Timestamp] = None


class DataQualityRulesetEvaluationRunFilter(BaseValidatorModel):
    DataSource: DataSourceUnion
    StartedBefore: Optional[Timestamp] = None
    StartedAfter: Optional[Timestamp] = None


class StartDataQualityRuleRecommendationRunRequest(BaseValidatorModel):
    DataSource: DataSourceUnion
    Role: str
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    CreatedRulesetName: Optional[str] = None
    DataQualitySecurityConfiguration: Optional[str] = None
    ClientToken: Optional[str] = None


class StartDataQualityRulesetEvaluationRunRequest(BaseValidatorModel):
    DataSource: DataSourceUnion
    Role: str
    RulesetNames: Sequence[str]
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    ClientToken: Optional[str] = None
    AdditionalRunOptions: Optional[DataQualityEvaluationRunAdditionalRunOptions] = None
    AdditionalDataSources: Optional[Mapping[str, DataSourceUnion]] = None


class TableOptimizer(BaseValidatorModel):
    pass


class BatchTableOptimizer(BaseValidatorModel):
    catalogId: Optional[str] = None
    databaseName: Optional[str] = None
    tableName: Optional[str] = None
    tableOptimizer: Optional[TableOptimizer] = None


class GetTableOptimizerResponse(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    TableOptimizer: TableOptimizer
    ResponseMetadata: ResponseMetadata


class GetConnectionResponse(BaseValidatorModel):
    Connection: Connection
    ResponseMetadata: ResponseMetadata


class GetConnectionsResponse(BaseValidatorModel):
    ConnectionList: List[Connection]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateConnectionRequest(BaseValidatorModel):
    ConnectionInput: ConnectionInput
    CatalogId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateConnectionRequest(BaseValidatorModel):
    Name: str
    ConnectionInput: ConnectionInput
    CatalogId: Optional[str] = None


class TestConnectionRequest(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    CatalogId: Optional[str] = None
    TestConnectionInput: Optional[TestConnectionInput] = None


class CodeGenConfigurationNodeOutput(BaseValidatorModel):
    pass


class Job(BaseValidatorModel):
    Name: Optional[str] = None
    JobMode: Optional[JobModeType] = None
    JobRunQueuingEnabled: Optional[bool] = None
    Description: Optional[str] = None
    LogUri: Optional[str] = None
    Role: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    ExecutionProperty: Optional[ExecutionProperty] = None
    Command: Optional[JobCommand] = None
    DefaultArguments: Optional[Dict[str, str]] = None
    NonOverridableArguments: Optional[Dict[str, str]] = None
    Connections: Optional[ConnectionsListOutput] = None
    MaxRetries: Optional[int] = None
    AllocatedCapacity: Optional[int] = None
    Timeout: Optional[int] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationProperty] = None
    GlueVersion: Optional[str] = None
    CodeGenConfigurationNodes: Optional[Dict[str, CodeGenConfigurationNodeOutput]] = None
    ExecutionClass: Optional[ExecutionClassType] = None
    SourceControlDetails: Optional[SourceControlDetails] = None
    MaintenanceWindow: Optional[str] = None
    ProfileName: Optional[str] = None


class CodeGenConfigurationNodePaginator(BaseValidatorModel):
    pass


class JobPaginator(BaseValidatorModel):
    Name: Optional[str] = None
    JobMode: Optional[JobModeType] = None
    JobRunQueuingEnabled: Optional[bool] = None
    Description: Optional[str] = None
    LogUri: Optional[str] = None
    Role: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    ExecutionProperty: Optional[ExecutionProperty] = None
    Command: Optional[JobCommand] = None
    DefaultArguments: Optional[Dict[str, str]] = None
    NonOverridableArguments: Optional[Dict[str, str]] = None
    Connections: Optional[ConnectionsListOutput] = None
    MaxRetries: Optional[int] = None
    AllocatedCapacity: Optional[int] = None
    Timeout: Optional[int] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationProperty] = None
    GlueVersion: Optional[str] = None
    CodeGenConfigurationNodes: Optional[Dict[str, CodeGenConfigurationNodePaginator]] = None
    ExecutionClass: Optional[ExecutionClassType] = None
    SourceControlDetails: Optional[SourceControlDetails] = None
    MaintenanceWindow: Optional[str] = None
    ProfileName: Optional[str] = None


class RecipeStepUnion(BaseValidatorModel):
    pass


class Recipe(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    RecipeReference: Optional[RecipeReference] = None
    RecipeSteps: Optional[Sequence[RecipeStepUnion]] = None


class StorageDescriptorUnion(BaseValidatorModel):
    pass


class PartitionInput(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None
    LastAccessTime: Optional[Timestamp] = None
    StorageDescriptor: Optional[StorageDescriptorUnion] = None
    Parameters: Optional[Mapping[str, str]] = None
    LastAnalyzedTime: Optional[Timestamp] = None


class TableInput(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Owner: Optional[str] = None
    LastAccessTime: Optional[Timestamp] = None
    LastAnalyzedTime: Optional[Timestamp] = None
    Retention: Optional[int] = None
    StorageDescriptor: Optional[StorageDescriptorUnion] = None
    PartitionKeys: Optional[Sequence[ColumnUnion]] = None
    ViewOriginalText: Optional[str] = None
    ViewExpandedText: Optional[str] = None
    TableType: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    TargetTable: Optional[TableIdentifier] = None
    ViewDefinition: Optional[ViewDefinitionInput] = None


class GetTablesResponsePaginator(BaseValidatorModel):
    TableList: List[TablePaginator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TableVersionPaginator(BaseValidatorModel):
    Table: Optional[TablePaginator] = None
    VersionId: Optional[str] = None


class GetTableResponse(BaseValidatorModel):
    Table: Table
    ResponseMetadata: ResponseMetadata


class GetTablesResponse(BaseValidatorModel):
    TableList: List[Table]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetUnfilteredTableMetadataResponse(BaseValidatorModel):
    Table: Table
    AuthorizedColumns: List[str]
    IsRegisteredWithLakeFormation: bool
    CellFilters: List[ColumnRowFilter]
    QueryAuthorizationId: str
    IsMultiDialectView: bool
    ResourceArn: str
    IsProtected: bool
    Permissions: List[PermissionType]
    RowFilter: str
    ResponseMetadata: ResponseMetadata


class SearchTablesResponse(BaseValidatorModel):
    TableList: List[Table]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TableVersion(BaseValidatorModel):
    Table: Optional[Table] = None
    VersionId: Optional[str] = None


class Node(BaseValidatorModel):
    pass


class WorkflowGraph(BaseValidatorModel):
    Nodes: Optional[List[Node]] = None
    Edges: Optional[List[Edge]] = None


class UpdateColumnStatisticsForPartitionResponse(BaseValidatorModel):
    Errors: List[ColumnStatisticsError]
    ResponseMetadata: ResponseMetadata


class UpdateColumnStatisticsForTableResponse(BaseValidatorModel):
    Errors: List[ColumnStatisticsError]
    ResponseMetadata: ResponseMetadata


class GetUnfilteredPartitionsMetadataResponse(BaseValidatorModel):
    UnfilteredPartitions: List[UnfilteredPartition]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListDataQualityResultsRequest(BaseValidatorModel):
    Filter: Optional[DataQualityResultFilterCriteria] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataQualityRuleRecommendationRunsRequest(BaseValidatorModel):
    Filter: Optional[DataQualityRuleRecommendationRunFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataQualityRulesetEvaluationRunsRequest(BaseValidatorModel):
    Filter: Optional[DataQualityRulesetEvaluationRunFilter] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchGetTableOptimizerError(BaseValidatorModel):
    pass


class BatchGetTableOptimizerResponse(BaseValidatorModel):
    TableOptimizers: List[BatchTableOptimizer]
    Failures: List[BatchGetTableOptimizerError]
    ResponseMetadata: ResponseMetadata


class BatchGetJobsResponse(BaseValidatorModel):
    Jobs: List[Job]
    JobsNotFound: List[str]
    ResponseMetadata: ResponseMetadata


class GetJobResponse(BaseValidatorModel):
    Job: Job
    ResponseMetadata: ResponseMetadata


class GetJobsResponse(BaseValidatorModel):
    Jobs: List[Job]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetJobsResponsePaginator(BaseValidatorModel):
    Jobs: List[JobPaginator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchCreatePartitionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionInputList: Sequence[PartitionInput]
    CatalogId: Optional[str] = None


class BatchUpdatePartitionRequestEntry(BaseValidatorModel):
    PartitionValueList: Sequence[str]
    PartitionInput: PartitionInput


class CreatePartitionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionInput: PartitionInput
    CatalogId: Optional[str] = None


class UpdatePartitionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValueList: Sequence[str]
    PartitionInput: PartitionInput
    CatalogId: Optional[str] = None


class CreateTableRequest(BaseValidatorModel):
    DatabaseName: str
    TableInput: TableInput
    CatalogId: Optional[str] = None
    PartitionIndexes: Optional[Sequence[PartitionIndex]] = None
    TransactionId: Optional[str] = None
    OpenTableFormatInput: Optional[OpenTableFormatInput] = None


class UpdateTableRequest(BaseValidatorModel):
    DatabaseName: str
    TableInput: TableInput
    CatalogId: Optional[str] = None
    SkipArchive: Optional[bool] = None
    TransactionId: Optional[str] = None
    VersionId: Optional[str] = None
    ViewUpdateAction: Optional[ViewUpdateActionType] = None
    Force: Optional[bool] = None


class GetTableVersionsResponsePaginator(BaseValidatorModel):
    TableVersions: List[TableVersionPaginator]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetTableVersionResponse(BaseValidatorModel):
    TableVersion: TableVersion
    ResponseMetadata: ResponseMetadata


class GetTableVersionsResponse(BaseValidatorModel):
    TableVersions: List[TableVersion]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class WorkflowRun(BaseValidatorModel):
    Name: Optional[str] = None
    WorkflowRunId: Optional[str] = None
    PreviousRunId: Optional[str] = None
    WorkflowRunProperties: Optional[Dict[str, str]] = None
    StartedOn: Optional[datetime] = None
    CompletedOn: Optional[datetime] = None
    Status: Optional[WorkflowRunStatusType] = None
    ErrorMessage: Optional[str] = None
    Statistics: Optional[WorkflowRunStatistics] = None
    Graph: Optional[WorkflowGraph] = None
    StartingEventBatchCondition: Optional[StartingEventBatchCondition] = None


class BatchUpdatePartitionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    Entries: Sequence[BatchUpdatePartitionRequestEntry]
    CatalogId: Optional[str] = None


class ColumnStatisticsDataUnion(BaseValidatorModel):
    pass


class ColumnStatistics(BaseValidatorModel):
    ColumnName: str
    ColumnType: str
    AnalyzedTime: Timestamp
    StatisticsData: ColumnStatisticsDataUnion


class GetWorkflowRunResponse(BaseValidatorModel):
    Run: WorkflowRun
    ResponseMetadata: ResponseMetadata


class GetWorkflowRunsResponse(BaseValidatorModel):
    Runs: List[WorkflowRun]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Workflow(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    DefaultRunProperties: Optional[Dict[str, str]] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    LastRun: Optional[WorkflowRun] = None
    Graph: Optional[WorkflowGraph] = None
    MaxConcurrentRuns: Optional[int] = None
    BlueprintDetails: Optional[BlueprintDetails] = None


class BatchGetWorkflowsResponse(BaseValidatorModel):
    Workflows: List[Workflow]
    MissingWorkflows: List[str]
    ResponseMetadata: ResponseMetadata


class GetWorkflowResponse(BaseValidatorModel):
    Workflow: Workflow
    ResponseMetadata: ResponseMetadata


class CodeGenConfigurationNodeUnion(BaseValidatorModel):
    pass


class CreateJobRequest(BaseValidatorModel):
    Name: str
    Role: str
    Command: JobCommand
    JobMode: Optional[JobModeType] = None
    JobRunQueuingEnabled: Optional[bool] = None
    Description: Optional[str] = None
    LogUri: Optional[str] = None
    ExecutionProperty: Optional[ExecutionProperty] = None
    DefaultArguments: Optional[Mapping[str, str]] = None
    NonOverridableArguments: Optional[Mapping[str, str]] = None
    Connections: Optional[ConnectionsListUnion] = None
    MaxRetries: Optional[int] = None
    AllocatedCapacity: Optional[int] = None
    Timeout: Optional[int] = None
    MaxCapacity: Optional[float] = None
    SecurityConfiguration: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    NotificationProperty: Optional[NotificationProperty] = None
    GlueVersion: Optional[str] = None
    NumberOfWorkers: Optional[int] = None
    WorkerType: Optional[WorkerTypeType] = None
    CodeGenConfigurationNodes: Optional[Mapping[str, CodeGenConfigurationNodeUnion]] = None
    ExecutionClass: Optional[ExecutionClassType] = None
    SourceControlDetails: Optional[SourceControlDetails] = None
    MaintenanceWindow: Optional[str] = None


class JobUpdate(BaseValidatorModel):
    JobMode: Optional[JobModeType] = None
    JobRunQueuingEnabled: Optional[bool] = None
    Description: Optional[str] = None
    LogUri: Optional[str] = None
    Role: Optional[str] = None
    ExecutionProperty: Optional[ExecutionProperty] = None
    Command: Optional[JobCommand] = None
    DefaultArguments: Optional[Mapping[str, str]] = None
    NonOverridableArguments: Optional[Mapping[str, str]] = None
    Connections: Optional[ConnectionsListUnion] = None
    MaxRetries: Optional[int] = None
    AllocatedCapacity: Optional[int] = None
    Timeout: Optional[int] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationProperty] = None
    GlueVersion: Optional[str] = None
    CodeGenConfigurationNodes: Optional[Mapping[str, CodeGenConfigurationNodeUnion]] = None
    ExecutionClass: Optional[ExecutionClassType] = None
    SourceControlDetails: Optional[SourceControlDetails] = None
    MaintenanceWindow: Optional[str] = None


class ColumnStatisticsUnion(BaseValidatorModel):
    pass


class UpdateColumnStatisticsForPartitionRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnStatisticsList: Sequence[ColumnStatisticsUnion]
    CatalogId: Optional[str] = None


class UpdateColumnStatisticsForTableRequest(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    ColumnStatisticsList: Sequence[ColumnStatisticsUnion]
    CatalogId: Optional[str] = None


class UpdateJobRequest(BaseValidatorModel):
    JobName: str
    JobUpdate: JobUpdate


