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

class NotificationPropertyTypeDef(BaseValidatorModel):
    NotifyDelayAfter: Optional[int] = None


class AggregateOperationOutputTypeDef(BaseValidatorModel):
    Column: List[str]
    AggFunc: AggFunctionType


class AggregateOperationTypeDef(BaseValidatorModel):
    Column: Sequence[str]
    AggFunc: AggFunctionType


class AllowedValueTypeDef(BaseValidatorModel):
    Value: str
    Description: Optional[str] = None


class AmazonRedshiftAdvancedOptionTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class OptionTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    Label: Optional[str] = None
    Description: Optional[str] = None


class AnnotationErrorTypeDef(BaseValidatorModel):
    ProfileId: Optional[str] = None
    StatisticId: Optional[str] = None
    FailureReason: Optional[str] = None


class MappingOutputTypeDef(BaseValidatorModel):
    ToKey: Optional[str] = None
    FromPath: Optional[List[str]] = None
    FromType: Optional[str] = None
    ToType: Optional[str] = None
    Dropped: Optional[bool] = None
    Children: Optional[List[Dict[str, Any]]] = None


class MappingPaginatorTypeDef(BaseValidatorModel):
    ToKey: Optional[str] = None
    FromPath: Optional[List[str]] = None
    FromType: Optional[str] = None
    ToType: Optional[str] = None
    Dropped: Optional[bool] = None
    Children: Optional[List[Dict[str, Any]]] = None


class AuditContextTypeDef(BaseValidatorModel):
    AdditionalAuditContext: Optional[str] = None
    RequestedColumns: Optional[Sequence[str]] = None
    AllColumnsRequested: Optional[bool] = None


class BasicAuthenticationCredentialsTypeDef(BaseValidatorModel):
    Username: Optional[str] = None
    Password: Optional[str] = None


class AuthorizationCodePropertiesTypeDef(BaseValidatorModel):
    AuthorizationCode: Optional[str] = None
    RedirectUri: Optional[str] = None


class PartitionValueListOutputTypeDef(BaseValidatorModel):
    Values: List[str]


class BasicCatalogTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str
    PartitionKeys: Optional[List[List[str]]] = None


class BasicCatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDeleteConnectionRequestTypeDef(BaseValidatorModel):
    ConnectionNameList: Sequence[str]
    CatalogId: Optional[str] = None


class ErrorDetailTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class BatchDeleteTableRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TablesToDelete: Sequence[str]
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None


class BatchDeleteTableVersionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    VersionIds: Sequence[str]
    CatalogId: Optional[str] = None


class BatchGetBlueprintsRequestTypeDef(BaseValidatorModel):
    Names: Sequence[str]
    IncludeBlueprint: Optional[bool] = None
    IncludeParameterSpec: Optional[bool] = None


class BatchGetCrawlersRequestTypeDef(BaseValidatorModel):
    CrawlerNames: Sequence[str]


class BatchGetCustomEntityTypesRequestTypeDef(BaseValidatorModel):
    Names: Sequence[str]


class CustomEntityTypeTypeDef(BaseValidatorModel):
    Name: str
    RegexString: str
    ContextWords: Optional[List[str]] = None


class BatchGetDataQualityResultRequestTypeDef(BaseValidatorModel):
    ResultIds: Sequence[str]


class BatchGetDevEndpointsRequestTypeDef(BaseValidatorModel):
    DevEndpointNames: Sequence[str]


class DevEndpointTypeDef(BaseValidatorModel):
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


class BatchGetJobsRequestTypeDef(BaseValidatorModel):
    JobNames: Sequence[str]


class BatchGetTriggersRequestTypeDef(BaseValidatorModel):
    TriggerNames: Sequence[str]


class BatchGetWorkflowsRequestTypeDef(BaseValidatorModel):
    Names: Sequence[str]
    IncludeGraph: Optional[bool] = None


class DatapointInclusionAnnotationTypeDef(BaseValidatorModel):
    ProfileId: Optional[str] = None
    StatisticId: Optional[str] = None
    InclusionAnnotation: Optional[InclusionAnnotationValueType] = None


class BatchStopJobRunRequestTypeDef(BaseValidatorModel):
    JobName: str
    JobRunIds: Sequence[str]


class BatchStopJobRunSuccessfulSubmissionTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None


class BinaryColumnStatisticsDataTypeDef(BaseValidatorModel):
    MaximumLength: int
    AverageLength: float
    NumberOfNulls: int


class BlueprintDetailsTypeDef(BaseValidatorModel):
    BlueprintName: Optional[str] = None
    RunId: Optional[str] = None


class BlueprintRunTypeDef(BaseValidatorModel):
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


class LastActiveDefinitionTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    LastModifiedOn: Optional[datetime] = None
    ParameterSpec: Optional[str] = None
    BlueprintLocation: Optional[str] = None
    BlueprintServiceLocation: Optional[str] = None


class BooleanColumnStatisticsDataTypeDef(BaseValidatorModel):
    NumberOfTrues: int
    NumberOfFalses: int
    NumberOfNulls: int


class CancelDataQualityRuleRecommendationRunRequestTypeDef(BaseValidatorModel):
    RunId: str


class CancelDataQualityRulesetEvaluationRunRequestTypeDef(BaseValidatorModel):
    RunId: str


class CancelMLTaskRunRequestTypeDef(BaseValidatorModel):
    TransformId: str
    TaskRunId: str


class CancelStatementRequestTypeDef(BaseValidatorModel):
    SessionId: str
    Id: int
    RequestOrigin: Optional[str] = None


class CapabilitiesTypeDef(BaseValidatorModel):
    SupportedAuthenticationTypes: List[AuthenticationTypeType]
    SupportedDataOperations: List[DataOperationType]
    SupportedComputeEnvironments: List[ComputeEnvironmentType]


class CatalogEntryTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str


class CatalogImportStatusTypeDef(BaseValidatorModel):
    ImportCompleted: Optional[bool] = None
    ImportTime: Optional[datetime] = None
    ImportedBy: Optional[str] = None


class FederatedCatalogTypeDef(BaseValidatorModel):
    Identifier: Optional[str] = None
    ConnectionName: Optional[str] = None


class TargetRedshiftCatalogTypeDef(BaseValidatorModel):
    CatalogArn: str


class KafkaStreamingSourceOptionsOutputTypeDef(BaseValidatorModel):
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


class StreamingDataPreviewOptionsTypeDef(BaseValidatorModel):
    PollingTime: Optional[int] = None
    RecordPollingLimit: Optional[int] = None


class KinesisStreamingSourceOptionsOutputTypeDef(BaseValidatorModel):
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


class DataLakeAccessPropertiesOutputTypeDef(BaseValidatorModel):
    DataLakeAccess: Optional[bool] = None
    DataTransferRole: Optional[str] = None
    KmsKey: Optional[str] = None
    ManagedWorkgroupName: Optional[str] = None
    ManagedWorkgroupStatus: Optional[str] = None
    RedshiftDatabaseName: Optional[str] = None
    StatusMessage: Optional[str] = None
    CatalogType: Optional[str] = None


class DataLakeAccessPropertiesTypeDef(BaseValidatorModel):
    DataLakeAccess: Optional[bool] = None
    DataTransferRole: Optional[str] = None
    KmsKey: Optional[str] = None
    CatalogType: Optional[str] = None


class CatalogSchemaChangePolicyTypeDef(BaseValidatorModel):
    EnableUpdateCatalog: Optional[bool] = None
    UpdateBehavior: Optional[UpdateCatalogBehaviorType] = None


class CatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class CatalogTargetOutputTypeDef(BaseValidatorModel):
    DatabaseName: str
    Tables: List[str]
    ConnectionName: Optional[str] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None


class CatalogTargetTypeDef(BaseValidatorModel):
    DatabaseName: str
    Tables: Sequence[str]
    ConnectionName: Optional[str] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None


class CheckSchemaVersionValidityInputTypeDef(BaseValidatorModel):
    DataFormat: DataFormatType
    SchemaDefinition: str


class CsvClassifierTypeDef(BaseValidatorModel):
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


class GrokClassifierTypeDef(BaseValidatorModel):
    Name: str
    Classification: str
    GrokPattern: str
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    Version: Optional[int] = None
    CustomPatterns: Optional[str] = None


class JsonClassifierTypeDef(BaseValidatorModel):
    Name: str
    JsonPath: str
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    Version: Optional[int] = None


class XMLClassifierTypeDef(BaseValidatorModel):
    Name: str
    Classification: str
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    Version: Optional[int] = None
    RowTag: Optional[str] = None


class CloudWatchEncryptionTypeDef(BaseValidatorModel):
    CloudWatchEncryptionMode: Optional[CloudWatchEncryptionModeType] = None
    KmsKeyArn: Optional[str] = None


class ConnectorDataTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    ConnectionType: str
    Data: Dict[str, str]
    Inputs: Optional[List[str]] = None


class DirectJDBCSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    ConnectionName: str
    ConnectionType: JDBCConnectionTypeType
    RedshiftTmpDir: Optional[str] = None


class DropDuplicatesOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Columns: Optional[List[List[str]]] = None


class DropFieldsOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]


class DynamoDBCatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class FillMissingValuesOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    ImputedPath: str
    FilledPath: Optional[str] = None


class MergeOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Source: str
    PrimaryKeys: List[List[str]]


class MicrosoftSQLServerCatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class MicrosoftSQLServerCatalogTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str


class MySQLCatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class MySQLCatalogTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str


class OracleSQLCatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class OracleSQLCatalogTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str


class PIIDetectionOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    PiiType: PiiTypeType
    EntityTypesToDetect: List[str]
    OutputColumnName: Optional[str] = None
    SampleFraction: Optional[float] = None
    ThresholdFraction: Optional[float] = None
    MaskValue: Optional[str] = None


class PostgreSQLCatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class PostgreSQLCatalogTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str


class RedshiftSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    RedshiftTmpDir: Optional[str] = None
    TmpDirIAMRole: Optional[str] = None


class RelationalCatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str


class RenameFieldOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    SourcePath: List[str]
    TargetPath: List[str]


class SelectFieldsOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]


class SelectFromCollectionOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Index: int


class SpigotOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    Topk: Optional[int] = None
    Prob: Optional[float] = None


class SplitFieldsOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]


class UnionOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    UnionType: UnionTypeType


class CodeGenEdgeTypeDef(BaseValidatorModel):
    Source: str
    Target: str
    TargetParameter: Optional[str] = None


class CodeGenNodeArgTypeDef(BaseValidatorModel):
    Name: str
    Value: str
    Param: Optional[bool] = None


class ColumnImportanceTypeDef(BaseValidatorModel):
    ColumnName: Optional[str] = None
    Importance: Optional[float] = None


class ColumnRowFilterTypeDef(BaseValidatorModel):
    ColumnName: Optional[str] = None
    RowFilterExpression: Optional[str] = None


class DateColumnStatisticsDataOutputTypeDef(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[datetime] = None
    MaximumValue: Optional[datetime] = None


class DoubleColumnStatisticsDataTypeDef(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[float] = None
    MaximumValue: Optional[float] = None


class LongColumnStatisticsDataTypeDef(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[int] = None
    MaximumValue: Optional[int] = None


class StringColumnStatisticsDataTypeDef(BaseValidatorModel):
    MaximumLength: int
    AverageLength: float
    NumberOfNulls: int
    NumberOfDistinctValues: int


class ColumnStatisticsTaskRunTypeDef(BaseValidatorModel):
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


class ExecutionAttemptTypeDef(BaseValidatorModel):
    Status: Optional[ExecutionStatusType] = None
    ColumnStatisticsTaskRunId: Optional[str] = None
    ExecutionTimestamp: Optional[datetime] = None
    ErrorMessage: Optional[str] = None


class ScheduleTypeDef(BaseValidatorModel):
    ScheduleExpression: Optional[str] = None
    State: Optional[ScheduleStateType] = None


class IcebergCompactionMetricsTypeDef(BaseValidatorModel):
    NumberOfBytesCompacted: Optional[int] = None
    NumberOfFilesCompacted: Optional[int] = None
    NumberOfDpus: Optional[int] = None
    JobDurationInHour: Optional[float] = None


class ConditionExpressionTypeDef(BaseValidatorModel):
    Condition: str
    TargetColumn: str
    Value: Optional[str] = None


class ConditionTypeDef(BaseValidatorModel):
    LogicalOperator: Optional[Literal["EQUALS"]] = None
    JobName: Optional[str] = None
    State: Optional[JobRunStateType] = None
    CrawlerName: Optional[str] = None
    CrawlState: Optional[CrawlStateType] = None


class ConfigurationObjectOutputTypeDef(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    AllowedValues: Optional[List[str]] = None
    MinValue: Optional[str] = None
    MaxValue: Optional[str] = None


class ConfigurationObjectTypeDef(BaseValidatorModel):
    DefaultValue: Optional[str] = None
    AllowedValues: Optional[Sequence[str]] = None
    MinValue: Optional[str] = None
    MaxValue: Optional[str] = None


class ConfusionMatrixTypeDef(BaseValidatorModel):
    NumTruePositives: Optional[int] = None
    NumFalsePositives: Optional[int] = None
    NumTrueNegatives: Optional[int] = None
    NumFalseNegatives: Optional[int] = None


class ConnectionPasswordEncryptionTypeDef(BaseValidatorModel):
    ReturnConnectionPasswordEncrypted: bool
    AwsKmsKeyId: Optional[str] = None


class PhysicalConnectionRequirementsOutputTypeDef(BaseValidatorModel):
    SubnetId: Optional[str] = None
    SecurityGroupIdList: Optional[List[str]] = None
    AvailabilityZone: Optional[str] = None


class ConnectionsListOutputTypeDef(BaseValidatorModel):
    Connections: Optional[List[str]] = None


class ConnectionsListTypeDef(BaseValidatorModel):
    Connections: Optional[Sequence[str]] = None


class ConnectorDataTargetTypeDef(BaseValidatorModel):
    Name: str
    ConnectionType: str
    Data: Mapping[str, str]
    Inputs: Optional[Sequence[str]] = None


class CrawlTypeDef(BaseValidatorModel):
    State: Optional[CrawlStateType] = None
    StartedOn: Optional[datetime] = None
    CompletedOn: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    LogGroup: Optional[str] = None
    LogStream: Optional[str] = None


class CrawlerHistoryTypeDef(BaseValidatorModel):
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


class CrawlerMetricsTypeDef(BaseValidatorModel):
    CrawlerName: Optional[str] = None
    TimeLeftSeconds: Optional[float] = None
    StillEstimating: Optional[bool] = None
    LastRuntimeSeconds: Optional[float] = None
    MedianRuntimeSeconds: Optional[float] = None
    TablesCreated: Optional[int] = None
    TablesUpdated: Optional[int] = None
    TablesDeleted: Optional[int] = None


class DeltaTargetOutputTypeDef(BaseValidatorModel):
    DeltaTables: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    WriteManifest: Optional[bool] = None
    CreateNativeDeltaTable: Optional[bool] = None


class DynamoDBTargetTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    scanAll: Optional[bool] = None
    scanRate: Optional[float] = None


class HudiTargetOutputTypeDef(BaseValidatorModel):
    Paths: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    MaximumTraversalDepth: Optional[int] = None


class IcebergTargetOutputTypeDef(BaseValidatorModel):
    Paths: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    MaximumTraversalDepth: Optional[int] = None


class JdbcTargetOutputTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    Path: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    EnableAdditionalMetadata: Optional[List[JdbcMetadataEntryType]] = None


class MongoDBTargetTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    Path: Optional[str] = None
    ScanAll: Optional[bool] = None


class S3TargetOutputTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    SampleSize: Optional[int] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None


class DeltaTargetTypeDef(BaseValidatorModel):
    DeltaTables: Optional[Sequence[str]] = None
    ConnectionName: Optional[str] = None
    WriteManifest: Optional[bool] = None
    CreateNativeDeltaTable: Optional[bool] = None


class HudiTargetTypeDef(BaseValidatorModel):
    Paths: Optional[Sequence[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[Sequence[str]] = None
    MaximumTraversalDepth: Optional[int] = None


class IcebergTargetTypeDef(BaseValidatorModel):
    Paths: Optional[Sequence[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[Sequence[str]] = None
    MaximumTraversalDepth: Optional[int] = None


class JdbcTargetTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    Path: Optional[str] = None
    Exclusions: Optional[Sequence[str]] = None
    EnableAdditionalMetadata: Optional[Sequence[JdbcMetadataEntryType]] = None


class S3TargetTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    Exclusions: Optional[Sequence[str]] = None
    ConnectionName: Optional[str] = None
    SampleSize: Optional[int] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None


class LakeFormationConfigurationTypeDef(BaseValidatorModel):
    UseLakeFormationCredentials: Optional[bool] = None
    AccountId: Optional[str] = None


class LastCrawlInfoTypeDef(BaseValidatorModel):
    Status: Optional[LastCrawlStatusType] = None
    ErrorMessage: Optional[str] = None
    LogGroup: Optional[str] = None
    LogStream: Optional[str] = None
    MessagePrefix: Optional[str] = None
    StartTime: Optional[datetime] = None


class LineageConfigurationTypeDef(BaseValidatorModel):
    CrawlerLineageSettings: Optional[CrawlerLineageSettingsType] = None


class RecrawlPolicyTypeDef(BaseValidatorModel):
    RecrawlBehavior: Optional[RecrawlBehaviorType] = None


class SchemaChangePolicyTypeDef(BaseValidatorModel):
    UpdateBehavior: Optional[UpdateBehaviorType] = None
    DeleteBehavior: Optional[DeleteBehaviorType] = None


class CrawlsFilterTypeDef(BaseValidatorModel):
    FieldName: Optional[FieldNameType] = None
    FilterOperator: Optional[FilterOperatorType] = None
    FieldValue: Optional[str] = None


class CreateBlueprintRequestTypeDef(BaseValidatorModel):
    Name: str
    BlueprintLocation: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateCsvClassifierRequestTypeDef(BaseValidatorModel):
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


class CreateGrokClassifierRequestTypeDef(BaseValidatorModel):
    Classification: str
    Name: str
    GrokPattern: str
    CustomPatterns: Optional[str] = None


class CreateJsonClassifierRequestTypeDef(BaseValidatorModel):
    Name: str
    JsonPath: str


class CreateXMLClassifierRequestTypeDef(BaseValidatorModel):
    Classification: str
    Name: str
    RowTag: Optional[str] = None


class CreateColumnStatisticsTaskSettingsRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    Role: str
    Schedule: Optional[str] = None
    ColumnNameList: Optional[Sequence[str]] = None
    SampleSize: Optional[float] = None
    CatalogID: Optional[str] = None
    SecurityConfiguration: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateCustomEntityTypeRequestTypeDef(BaseValidatorModel):
    Name: str
    RegexString: str
    ContextWords: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None


class DataQualityTargetTableTypeDef(BaseValidatorModel):
    TableName: str
    DatabaseName: str
    CatalogId: Optional[str] = None


class CreateDevEndpointRequestTypeDef(BaseValidatorModel):
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


class TagTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class SourceProcessingPropertiesTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None


class TargetProcessingPropertiesTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None
    KmsArn: Optional[str] = None
    ConnectionName: Optional[str] = None
    EventBusArn: Optional[str] = None


class IntegrationErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class ExecutionPropertyTypeDef(BaseValidatorModel):
    MaxConcurrentRuns: Optional[int] = None


class JobCommandTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ScriptLocation: Optional[str] = None
    PythonVersion: Optional[str] = None
    Runtime: Optional[str] = None


class SourceControlDetailsTypeDef(BaseValidatorModel):
    Provider: Optional[SourceControlProviderType] = None
    Repository: Optional[str] = None
    Owner: Optional[str] = None
    Branch: Optional[str] = None
    Folder: Optional[str] = None
    LastCommitId: Optional[str] = None
    AuthStrategy: Optional[SourceControlAuthStrategyType] = None
    AuthToken: Optional[str] = None


class PartitionIndexTypeDef(BaseValidatorModel):
    Keys: Sequence[str]
    IndexName: str


class CreateRegistryInputTypeDef(BaseValidatorModel):
    RegistryName: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class RegistryIdTypeDef(BaseValidatorModel):
    RegistryName: Optional[str] = None
    RegistryArn: Optional[str] = None


class SessionCommandTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    PythonVersion: Optional[str] = None


class EventBatchingConditionTypeDef(BaseValidatorModel):
    BatchSize: int
    BatchWindow: Optional[int] = None


class CreateWorkflowRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    DefaultRunProperties: Optional[Mapping[str, str]] = None
    Tags: Optional[Mapping[str, str]] = None
    MaxConcurrentRuns: Optional[int] = None


class DQResultsPublishingOptionsTypeDef(BaseValidatorModel):
    EvaluationContext: Optional[str] = None
    ResultsS3Prefix: Optional[str] = None
    CloudWatchMetricsEnabled: Optional[bool] = None
    ResultsPublishingEnabled: Optional[bool] = None


class DQStopJobOnFailureOptionsTypeDef(BaseValidatorModel):
    StopJobOnFailureTiming: Optional[DQStopJobOnFailureTimingType] = None


class EncryptionAtRestTypeDef(BaseValidatorModel):
    CatalogEncryptionMode: CatalogEncryptionModeType
    SseAwsKmsKeyId: Optional[str] = None
    CatalogEncryptionServiceRole: Optional[str] = None


class DataLakePrincipalTypeDef(BaseValidatorModel):
    DataLakePrincipalIdentifier: Optional[str] = None


class DataQualityAnalyzerResultTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    EvaluationMessage: Optional[str] = None
    EvaluatedMetrics: Optional[Dict[str, float]] = None


class DataQualityEncryptionTypeDef(BaseValidatorModel):
    DataQualityEncryptionMode: Optional[DataQualityEncryptionModeType] = None
    KmsKeyArn: Optional[str] = None


class DataQualityEvaluationRunAdditionalRunOptionsTypeDef(BaseValidatorModel):
    CloudWatchMetricsEnabled: Optional[bool] = None
    ResultsS3Prefix: Optional[str] = None
    CompositeRuleEvaluationMethod: Optional[DQCompositeRuleEvaluationMethodType] = None


class DataQualityMetricValuesTypeDef(BaseValidatorModel):
    ActualValue: Optional[float] = None
    ExpectedValue: Optional[float] = None
    LowerLimit: Optional[float] = None
    UpperLimit: Optional[float] = None


class DataQualityRuleResultTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    EvaluationMessage: Optional[str] = None
    Result: Optional[DataQualityRuleResultStatusType] = None
    EvaluatedMetrics: Optional[Dict[str, float]] = None
    EvaluatedRule: Optional[str] = None


class GlueTableOutputTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    ConnectionName: Optional[str] = None
    AdditionalOptions: Optional[Dict[str, str]] = None


class DatabaseIdentifierTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    Region: Optional[str] = None


class FederatedDatabaseTypeDef(BaseValidatorModel):
    Identifier: Optional[str] = None
    ConnectionName: Optional[str] = None


class DatatypeTypeDef(BaseValidatorModel):
    Id: str
    Label: str


class DecimalNumberOutputTypeDef(BaseValidatorModel):
    UnscaledValue: bytes
    Scale: int


class DeleteBlueprintRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteCatalogRequestTypeDef(BaseValidatorModel):
    CatalogId: str


class DeleteClassifierRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteColumnStatisticsForPartitionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnName: str
    CatalogId: Optional[str] = None


class DeleteColumnStatisticsForTableRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    ColumnName: str
    CatalogId: Optional[str] = None


class DeleteColumnStatisticsTaskSettingsRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str


class DeleteConnectionRequestTypeDef(BaseValidatorModel):
    ConnectionName: str
    CatalogId: Optional[str] = None


class DeleteCrawlerRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteCustomEntityTypeRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteDataQualityRulesetRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteDatabaseRequestTypeDef(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None


class DeleteDevEndpointRequestTypeDef(BaseValidatorModel):
    EndpointName: str


class DeleteIntegrationRequestTypeDef(BaseValidatorModel):
    IntegrationIdentifier: str


class DeleteIntegrationTablePropertiesRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TableName: str


class DeleteJobRequestTypeDef(BaseValidatorModel):
    JobName: str


class DeleteMLTransformRequestTypeDef(BaseValidatorModel):
    TransformId: str


class DeletePartitionIndexRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    IndexName: str
    CatalogId: Optional[str] = None


class DeletePartitionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    CatalogId: Optional[str] = None


class DeleteResourcePolicyRequestTypeDef(BaseValidatorModel):
    PolicyHashCondition: Optional[str] = None
    ResourceArn: Optional[str] = None


class SchemaIdTypeDef(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    RegistryName: Optional[str] = None


class DeleteSecurityConfigurationRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteSessionRequestTypeDef(BaseValidatorModel):
    Id: str
    RequestOrigin: Optional[str] = None


class DeleteTableRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None


class DeleteTableVersionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    VersionId: str
    CatalogId: Optional[str] = None


class DeleteTriggerRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteUsageProfileRequestTypeDef(BaseValidatorModel):
    Name: str


class DeleteUserDefinedFunctionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    FunctionName: str
    CatalogId: Optional[str] = None


class DeleteWorkflowRequestTypeDef(BaseValidatorModel):
    Name: str


class DescribeConnectionTypeRequestTypeDef(BaseValidatorModel):
    ConnectionType: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeEntityRequestTypeDef(BaseValidatorModel):
    ConnectionName: str
    EntityName: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    DataStoreApiVersion: Optional[str] = None


class FieldTypeDef(BaseValidatorModel):
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


class DescribeInboundIntegrationsRequestTypeDef(BaseValidatorModel):
    IntegrationArn: Optional[str] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    TargetArn: Optional[str] = None


class IntegrationFilterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[Sequence[str]] = None


class DevEndpointCustomLibrariesTypeDef(BaseValidatorModel):
    ExtraPythonLibsS3Path: Optional[str] = None
    ExtraJarsS3Path: Optional[str] = None


class DirectSchemaChangePolicyTypeDef(BaseValidatorModel):
    EnableUpdateCatalog: Optional[bool] = None
    UpdateBehavior: Optional[UpdateCatalogBehaviorType] = None
    Table: Optional[str] = None
    Database: Optional[str] = None


class DropDuplicatesTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Columns: Optional[Sequence[Sequence[str]]] = None


class DropFieldsTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]


class NullCheckBoxListTypeDef(BaseValidatorModel):
    IsEmpty: Optional[bool] = None
    IsNullString: Optional[bool] = None
    IsNegOne: Optional[bool] = None


class EdgeTypeDef(BaseValidatorModel):
    SourceId: Optional[str] = None
    DestinationId: Optional[str] = None


class JobBookmarksEncryptionTypeDef(BaseValidatorModel):
    JobBookmarksEncryptionMode: Optional[JobBookmarksEncryptionModeType] = None
    KmsKeyArn: Optional[str] = None


class S3EncryptionTypeDef(BaseValidatorModel):
    S3EncryptionMode: Optional[S3EncryptionModeType] = None
    KmsKeyArn: Optional[str] = None


class EntityTypeDef(BaseValidatorModel):
    EntityName: Optional[str] = None
    Label: Optional[str] = None
    IsParentEntity: Optional[bool] = None
    Description: Optional[str] = None
    Category: Optional[str] = None
    CustomProperties: Optional[Dict[str, str]] = None


class ErrorDetailsTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class ExportLabelsTaskRunPropertiesTypeDef(BaseValidatorModel):
    OutputS3Path: Optional[str] = None


class FederatedTableTypeDef(BaseValidatorModel):
    Identifier: Optional[str] = None
    DatabaseIdentifier: Optional[str] = None
    ConnectionName: Optional[str] = None


class FillMissingValuesTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    ImputedPath: str
    FilledPath: Optional[str] = None


class FindMatchesParametersTypeDef(BaseValidatorModel):
    PrimaryKeyColumnName: Optional[str] = None
    PrecisionRecallTradeoff: Optional[float] = None
    AccuracyCostTradeoff: Optional[float] = None
    EnforceProvidedLabels: Optional[bool] = None


class FindMatchesTaskRunPropertiesTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None


class GetBlueprintRequestTypeDef(BaseValidatorModel):
    Name: str
    IncludeBlueprint: Optional[bool] = None
    IncludeParameterSpec: Optional[bool] = None


class GetBlueprintRunRequestTypeDef(BaseValidatorModel):
    BlueprintName: str
    RunId: str


class GetBlueprintRunsRequestTypeDef(BaseValidatorModel):
    BlueprintName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetCatalogImportStatusRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None


class GetCatalogRequestTypeDef(BaseValidatorModel):
    CatalogId: str


class GetCatalogsRequestTypeDef(BaseValidatorModel):
    ParentCatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Recursive: Optional[bool] = None
    IncludeRoot: Optional[bool] = None


class GetClassifierRequestTypeDef(BaseValidatorModel):
    Name: str


class GetClassifiersRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetColumnStatisticsForPartitionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnNames: Sequence[str]
    CatalogId: Optional[str] = None


class GetColumnStatisticsForTableRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    ColumnNames: Sequence[str]
    CatalogId: Optional[str] = None


class GetColumnStatisticsTaskRunRequestTypeDef(BaseValidatorModel):
    ColumnStatisticsTaskRunId: str


class GetColumnStatisticsTaskRunsRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetColumnStatisticsTaskSettingsRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str


class GetConnectionRequestTypeDef(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None
    HidePassword: Optional[bool] = None
    ApplyOverrideForComputeEnvironment: Optional[ComputeEnvironmentType] = None


class GetConnectionsFilterTypeDef(BaseValidatorModel):
    MatchCriteria: Optional[Sequence[str]] = None
    ConnectionType: Optional[ConnectionTypeType] = None
    ConnectionSchemaVersion: Optional[int] = None


class GetCrawlerMetricsRequestTypeDef(BaseValidatorModel):
    CrawlerNameList: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetCrawlerRequestTypeDef(BaseValidatorModel):
    Name: str


class GetCrawlersRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetCustomEntityTypeRequestTypeDef(BaseValidatorModel):
    Name: str


class GetDataCatalogEncryptionSettingsRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None


class GetDataQualityModelRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    StatisticId: Optional[str] = None


class GetDataQualityModelResultRequestTypeDef(BaseValidatorModel):
    StatisticId: str
    ProfileId: str


class StatisticModelResultTypeDef(BaseValidatorModel):
    LowerBound: Optional[float] = None
    UpperBound: Optional[float] = None
    PredictedValue: Optional[float] = None
    ActualValue: Optional[float] = None
    Date: Optional[datetime] = None
    InclusionAnnotation: Optional[InclusionAnnotationValueType] = None


class GetDataQualityResultRequestTypeDef(BaseValidatorModel):
    ResultId: str


class GetDataQualityRuleRecommendationRunRequestTypeDef(BaseValidatorModel):
    RunId: str


class GetDataQualityRulesetEvaluationRunRequestTypeDef(BaseValidatorModel):
    RunId: str


class GetDataQualityRulesetRequestTypeDef(BaseValidatorModel):
    Name: str


class GetDatabaseRequestTypeDef(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None


class GetDatabasesRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    AttributesToGet: Optional[Sequence[Literal["NAME"]]] = None


class GetDataflowGraphRequestTypeDef(BaseValidatorModel):
    PythonScript: Optional[str] = None


class GetDevEndpointRequestTypeDef(BaseValidatorModel):
    EndpointName: str


class GetDevEndpointsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetEntityRecordsRequestTypeDef(BaseValidatorModel):
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


class GetIntegrationResourcePropertyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class GetIntegrationTablePropertiesRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TableName: str


class SourceTableConfigOutputTypeDef(BaseValidatorModel):
    Fields: Optional[List[str]] = None
    FilterPredicate: Optional[str] = None
    PrimaryKey: Optional[List[str]] = None
    RecordUpdateField: Optional[str] = None


class GetJobBookmarkRequestTypeDef(BaseValidatorModel):
    JobName: str
    RunId: Optional[str] = None


class JobBookmarkEntryTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    Version: Optional[int] = None
    Run: Optional[int] = None
    Attempt: Optional[int] = None
    PreviousRunId: Optional[str] = None
    RunId: Optional[str] = None
    JobBookmark: Optional[str] = None


class GetJobRequestTypeDef(BaseValidatorModel):
    JobName: str


class GetJobRunRequestTypeDef(BaseValidatorModel):
    JobName: str
    RunId: str
    PredecessorsIncluded: Optional[bool] = None


class GetJobRunsRequestTypeDef(BaseValidatorModel):
    JobName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetJobsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetMLTaskRunRequestTypeDef(BaseValidatorModel):
    TransformId: str
    TaskRunId: str


class TaskRunSortCriteriaTypeDef(BaseValidatorModel):
    Column: TaskRunSortColumnTypeType
    SortDirection: SortDirectionTypeType


class GetMLTransformRequestTypeDef(BaseValidatorModel):
    TransformId: str


class SchemaColumnTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    DataType: Optional[str] = None


class TransformSortCriteriaTypeDef(BaseValidatorModel):
    Column: TransformSortColumnTypeType
    SortDirection: SortDirectionTypeType


class MappingEntryTypeDef(BaseValidatorModel):
    SourceTable: Optional[str] = None
    SourcePath: Optional[str] = None
    SourceType: Optional[str] = None
    TargetTable: Optional[str] = None
    TargetPath: Optional[str] = None
    TargetType: Optional[str] = None


class GetPartitionIndexesRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None


class GetPartitionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    CatalogId: Optional[str] = None


class SegmentTypeDef(BaseValidatorModel):
    SegmentNumber: int
    TotalSegments: int


class GetResourcePoliciesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GluePolicyTypeDef(BaseValidatorModel):
    PolicyInJson: Optional[str] = None
    PolicyHash: Optional[str] = None
    CreateTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None


class GetResourcePolicyRequestTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None


class SchemaVersionNumberTypeDef(BaseValidatorModel):
    LatestVersion: Optional[bool] = None
    VersionNumber: Optional[int] = None


class GetSecurityConfigurationRequestTypeDef(BaseValidatorModel):
    Name: str


class GetSecurityConfigurationsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetSessionRequestTypeDef(BaseValidatorModel):
    Id: str
    RequestOrigin: Optional[str] = None


class GetStatementRequestTypeDef(BaseValidatorModel):
    SessionId: str
    Id: int
    RequestOrigin: Optional[str] = None


class GetTableVersionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    VersionId: Optional[str] = None


class GetTableVersionsRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetTagsRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class GetTriggerRequestTypeDef(BaseValidatorModel):
    Name: str


class GetTriggersRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    DependentJobName: Optional[str] = None
    MaxResults: Optional[int] = None


class SupportedDialectTypeDef(BaseValidatorModel):
    Dialect: Optional[ViewDialectType] = None
    DialectVersion: Optional[str] = None


class GetUsageProfileRequestTypeDef(BaseValidatorModel):
    Name: str


class GetUserDefinedFunctionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    FunctionName: str
    CatalogId: Optional[str] = None


class GetWorkflowRequestTypeDef(BaseValidatorModel):
    Name: str
    IncludeGraph: Optional[bool] = None


class GetWorkflowRunPropertiesRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str


class GetWorkflowRunRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str
    IncludeGraph: Optional[bool] = None


class GetWorkflowRunsRequestTypeDef(BaseValidatorModel):
    Name: str
    IncludeGraph: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GlueTableTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    ConnectionName: Optional[str] = None
    AdditionalOptions: Optional[Mapping[str, str]] = None


class S3SourceAdditionalOptionsTypeDef(BaseValidatorModel):
    BoundedSize: Optional[int] = None
    BoundedFiles: Optional[int] = None


class IcebergInputTypeDef(BaseValidatorModel):
    MetadataOperation: Literal["CREATE"]
    Version: Optional[str] = None


class IcebergOrphanFileDeletionConfigurationTypeDef(BaseValidatorModel):
    orphanFileRetentionPeriodInDays: Optional[int] = None
    location: Optional[str] = None


class IcebergOrphanFileDeletionMetricsTypeDef(BaseValidatorModel):
    NumberOfOrphanFilesDeleted: Optional[int] = None
    NumberOfDpus: Optional[int] = None
    JobDurationInHour: Optional[float] = None


class IcebergRetentionConfigurationTypeDef(BaseValidatorModel):
    snapshotRetentionPeriodInDays: Optional[int] = None
    numberOfSnapshotsToRetain: Optional[int] = None
    cleanExpiredFiles: Optional[bool] = None


class IcebergRetentionMetricsTypeDef(BaseValidatorModel):
    NumberOfDataFilesDeleted: Optional[int] = None
    NumberOfManifestFilesDeleted: Optional[int] = None
    NumberOfManifestListsDeleted: Optional[int] = None
    NumberOfDpus: Optional[int] = None
    JobDurationInHour: Optional[float] = None


class ImportCatalogToGlueRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None


class ImportLabelsTaskRunPropertiesTypeDef(BaseValidatorModel):
    InputS3Path: Optional[str] = None
    Replace: Optional[bool] = None


class IntegrationPartitionTypeDef(BaseValidatorModel):
    FieldName: Optional[str] = None
    FunctionSpec: Optional[str] = None


class JDBCConnectorOptionsOutputTypeDef(BaseValidatorModel):
    FilterPredicate: Optional[str] = None
    PartitionColumn: Optional[str] = None
    LowerBound: Optional[int] = None
    UpperBound: Optional[int] = None
    NumPartitions: Optional[int] = None
    JobBookmarkKeys: Optional[List[str]] = None
    JobBookmarkKeysSortOrder: Optional[str] = None
    DataTypeMapping: Optional[Dict[JDBCDataTypeType, GlueRecordTypeType]] = None


class JDBCConnectorOptionsTypeDef(BaseValidatorModel):
    FilterPredicate: Optional[str] = None
    PartitionColumn: Optional[str] = None
    LowerBound: Optional[int] = None
    UpperBound: Optional[int] = None
    NumPartitions: Optional[int] = None
    JobBookmarkKeys: Optional[Sequence[str]] = None
    JobBookmarkKeysSortOrder: Optional[str] = None
    DataTypeMapping: Optional[Mapping[JDBCDataTypeType, GlueRecordTypeType]] = None


class PredecessorTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    RunId: Optional[str] = None


class JoinColumnOutputTypeDef(BaseValidatorModel):
    From: str
    Keys: List[List[str]]


class JoinColumnTypeDef(BaseValidatorModel):
    From: str
    Keys: Sequence[Sequence[str]]


class LabelingSetGenerationTaskRunPropertiesTypeDef(BaseValidatorModel):
    OutputS3Path: Optional[str] = None


class ListBlueprintsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class ListColumnStatisticsTaskRunsRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListConnectionTypesRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListCrawlersRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class ListCustomEntityTypesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class ListDevEndpointsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class ListEntitiesRequestTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    CatalogId: Optional[str] = None
    ParentEntityName: Optional[str] = None
    NextToken: Optional[str] = None
    DataStoreApiVersion: Optional[str] = None


class ListJobsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class ListRegistriesInputTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RegistryListItemTypeDef(BaseValidatorModel):
    RegistryName: Optional[str] = None
    RegistryArn: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[RegistryStatusType] = None
    CreatedTime: Optional[str] = None
    UpdatedTime: Optional[str] = None


class SchemaVersionListItemTypeDef(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    SchemaVersionId: Optional[str] = None
    VersionNumber: Optional[int] = None
    Status: Optional[SchemaVersionStatusType] = None
    CreatedTime: Optional[str] = None


class SchemaListItemTypeDef(BaseValidatorModel):
    RegistryName: Optional[str] = None
    SchemaName: Optional[str] = None
    SchemaArn: Optional[str] = None
    Description: Optional[str] = None
    SchemaStatus: Optional[SchemaStatusType] = None
    CreatedTime: Optional[str] = None
    UpdatedTime: Optional[str] = None


class ListSessionsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None
    RequestOrigin: Optional[str] = None


class ListStatementsRequestTypeDef(BaseValidatorModel):
    SessionId: str
    RequestOrigin: Optional[str] = None
    NextToken: Optional[str] = None


class ListTriggersRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    DependentJobName: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class ListUsageProfilesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class UsageProfileDefinitionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None


class ListWorkflowsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MLUserDataEncryptionTypeDef(BaseValidatorModel):
    MlUserDataEncryptionMode: MLUserDataEncryptionModeStringType
    KmsKeyId: Optional[str] = None


class MappingTypeDef(BaseValidatorModel):
    ToKey: Optional[str] = None
    FromPath: Optional[Sequence[str]] = None
    FromType: Optional[str] = None
    ToType: Optional[str] = None
    Dropped: Optional[bool] = None
    Children: Optional[Sequence[Mapping[str, Any]]] = None


class MergeTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Source: str
    PrimaryKeys: Sequence[Sequence[str]]


class OtherMetadataValueListItemTypeDef(BaseValidatorModel):
    MetadataValue: Optional[str] = None
    CreatedTime: Optional[str] = None


class MetadataKeyValuePairTypeDef(BaseValidatorModel):
    MetadataKey: Optional[str] = None
    MetadataValue: Optional[str] = None


class MicrosoftSQLServerCatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str


class ModifyIntegrationRequestTypeDef(BaseValidatorModel):
    IntegrationIdentifier: str
    Description: Optional[str] = None
    DataFilter: Optional[str] = None
    IntegrationName: Optional[str] = None


class MySQLCatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str


class OAuth2ClientApplicationTypeDef(BaseValidatorModel):
    UserManagedClientApplicationClientId: Optional[str] = None
    AWSManagedClientApplicationReference: Optional[str] = None


class OAuth2CredentialsTypeDef(BaseValidatorModel):
    UserManagedClientApplicationClientSecret: Optional[str] = None
    AccessToken: Optional[str] = None
    RefreshToken: Optional[str] = None
    JwtToken: Optional[str] = None


class OracleSQLCatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str


class OrderTypeDef(BaseValidatorModel):
    Column: str
    SortOrder: int


class PIIDetectionTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    PiiType: PiiTypeType
    EntityTypesToDetect: Sequence[str]
    OutputColumnName: Optional[str] = None
    SampleFraction: Optional[float] = None
    ThresholdFraction: Optional[float] = None
    MaskValue: Optional[str] = None


class PartitionValueListTypeDef(BaseValidatorModel):
    Values: Sequence[str]


class PhysicalConnectionRequirementsTypeDef(BaseValidatorModel):
    SubnetId: Optional[str] = None
    SecurityGroupIdList: Optional[Sequence[str]] = None
    AvailabilityZone: Optional[str] = None


class PostgreSQLCatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str


class PropertyPredicateTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Comparator: Optional[ComparatorType] = None


class PutDataQualityProfileAnnotationRequestTypeDef(BaseValidatorModel):
    ProfileId: str
    InclusionAnnotation: InclusionAnnotationValueType


class PutResourcePolicyRequestTypeDef(BaseValidatorModel):
    PolicyInJson: str
    ResourceArn: Optional[str] = None
    PolicyHashCondition: Optional[str] = None
    PolicyExistsCondition: Optional[ExistConditionType] = None
    EnableHybrid: Optional[EnableHybridValuesType] = None


class PutWorkflowRunPropertiesRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str
    RunProperties: Mapping[str, str]


class RecipeActionOutputTypeDef(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Dict[str, str]] = None


class RecipeActionTypeDef(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Mapping[str, str]] = None


class RecipeReferenceTypeDef(BaseValidatorModel):
    RecipeArn: str
    RecipeVersion: str


class UpsertRedshiftTargetOptionsOutputTypeDef(BaseValidatorModel):
    TableLocation: Optional[str] = None
    ConnectionName: Optional[str] = None
    UpsertKeys: Optional[List[str]] = None


class RenameFieldTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    SourcePath: Sequence[str]
    TargetPath: Sequence[str]


class ResetJobBookmarkRequestTypeDef(BaseValidatorModel):
    JobName: str
    RunId: Optional[str] = None


class ResourceUriTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Uri: Optional[str] = None


class ResumeWorkflowRunRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str
    NodeIds: Sequence[str]


class RunIdentifierTypeDef(BaseValidatorModel):
    RunId: Optional[str] = None
    JobRunId: Optional[str] = None


class RunMetricsTypeDef(BaseValidatorModel):
    NumberOfBytesCompacted: Optional[str] = None
    NumberOfFilesCompacted: Optional[str] = None
    NumberOfDpus: Optional[str] = None
    JobDurationInHour: Optional[str] = None


class RunStatementRequestTypeDef(BaseValidatorModel):
    SessionId: str
    Code: str
    RequestOrigin: Optional[str] = None


class S3DirectSourceAdditionalOptionsTypeDef(BaseValidatorModel):
    BoundedSize: Optional[int] = None
    BoundedFiles: Optional[int] = None
    EnableSamplePath: Optional[bool] = None
    SamplePath: Optional[str] = None


class SortCriterionTypeDef(BaseValidatorModel):
    FieldName: Optional[str] = None
    Sort: Optional[SortType] = None


class SelectFieldsTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]


class SelectFromCollectionTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Index: int


class SerDeInfoOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    SerializationLibrary: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None


class SerDeInfoTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    SerializationLibrary: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None


class SkewedInfoOutputTypeDef(BaseValidatorModel):
    SkewedColumnNames: Optional[List[str]] = None
    SkewedColumnValues: Optional[List[str]] = None
    SkewedColumnValueLocationMaps: Optional[Dict[str, str]] = None


class SkewedInfoTypeDef(BaseValidatorModel):
    SkewedColumnNames: Optional[Sequence[str]] = None
    SkewedColumnValues: Optional[Sequence[str]] = None
    SkewedColumnValueLocationMaps: Optional[Mapping[str, str]] = None


class SourceTableConfigTypeDef(BaseValidatorModel):
    Fields: Optional[Sequence[str]] = None
    FilterPredicate: Optional[str] = None
    PrimaryKey: Optional[Sequence[str]] = None
    RecordUpdateField: Optional[str] = None


class SqlAliasTypeDef(BaseValidatorModel):
    From: str
    Alias: str


class SpigotTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Topk: Optional[int] = None
    Prob: Optional[float] = None


class SplitFieldsTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]


class StartBlueprintRunRequestTypeDef(BaseValidatorModel):
    BlueprintName: str
    RoleArn: str
    Parameters: Optional[str] = None


class StartColumnStatisticsTaskRunRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    Role: str
    ColumnNameList: Optional[Sequence[str]] = None
    SampleSize: Optional[float] = None
    CatalogID: Optional[str] = None
    SecurityConfiguration: Optional[str] = None


class StartColumnStatisticsTaskRunScheduleRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str


class StartCrawlerRequestTypeDef(BaseValidatorModel):
    Name: str


class StartCrawlerScheduleRequestTypeDef(BaseValidatorModel):
    CrawlerName: str


class StartExportLabelsTaskRunRequestTypeDef(BaseValidatorModel):
    TransformId: str
    OutputS3Path: str


class StartImportLabelsTaskRunRequestTypeDef(BaseValidatorModel):
    TransformId: str
    InputS3Path: str
    ReplaceAllLabels: Optional[bool] = None


class StartMLEvaluationTaskRunRequestTypeDef(BaseValidatorModel):
    TransformId: str


class StartMLLabelingSetGenerationTaskRunRequestTypeDef(BaseValidatorModel):
    TransformId: str
    OutputS3Path: str


class StartTriggerRequestTypeDef(BaseValidatorModel):
    Name: str


class StartWorkflowRunRequestTypeDef(BaseValidatorModel):
    Name: str
    RunProperties: Optional[Mapping[str, str]] = None


class StartingEventBatchConditionTypeDef(BaseValidatorModel):
    BatchSize: Optional[int] = None
    BatchWindow: Optional[int] = None


class StatementOutputDataTypeDef(BaseValidatorModel):
    TextPlain: Optional[str] = None


class TimestampedInclusionAnnotationTypeDef(BaseValidatorModel):
    Value: Optional[InclusionAnnotationValueType] = None
    LastModifiedOn: Optional[datetime] = None


class StopColumnStatisticsTaskRunRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str


class StopColumnStatisticsTaskRunScheduleRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str


class StopCrawlerRequestTypeDef(BaseValidatorModel):
    Name: str


class StopCrawlerScheduleRequestTypeDef(BaseValidatorModel):
    CrawlerName: str


class StopSessionRequestTypeDef(BaseValidatorModel):
    Id: str
    RequestOrigin: Optional[str] = None


class StopTriggerRequestTypeDef(BaseValidatorModel):
    Name: str


class StopWorkflowRunRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str


class TableIdentifierTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    Name: Optional[str] = None
    Region: Optional[str] = None


class TableOptimizerVpcConfigurationTypeDef(BaseValidatorModel):
    glueConnectionName: Optional[str] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagsToAdd: Mapping[str, str]


class UnionTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    UnionType: UnionTypeType


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagsToRemove: Sequence[str]


class UpdateBlueprintRequestTypeDef(BaseValidatorModel):
    Name: str
    BlueprintLocation: str
    Description: Optional[str] = None


class UpdateCsvClassifierRequestTypeDef(BaseValidatorModel):
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


class UpdateGrokClassifierRequestTypeDef(BaseValidatorModel):
    Name: str
    Classification: Optional[str] = None
    GrokPattern: Optional[str] = None
    CustomPatterns: Optional[str] = None


class UpdateJsonClassifierRequestTypeDef(BaseValidatorModel):
    Name: str
    JsonPath: Optional[str] = None


class UpdateXMLClassifierRequestTypeDef(BaseValidatorModel):
    Name: str
    Classification: Optional[str] = None
    RowTag: Optional[str] = None


class UpdateColumnStatisticsTaskSettingsRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    Role: Optional[str] = None
    Schedule: Optional[str] = None
    ColumnNameList: Optional[Sequence[str]] = None
    SampleSize: Optional[float] = None
    CatalogID: Optional[str] = None
    SecurityConfiguration: Optional[str] = None


class UpdateCrawlerScheduleRequestTypeDef(BaseValidatorModel):
    CrawlerName: str
    Schedule: Optional[str] = None


class UpdateDataQualityRulesetRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Ruleset: Optional[str] = None


class UpdateJobFromSourceControlRequestTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    Provider: Optional[SourceControlProviderType] = None
    RepositoryName: Optional[str] = None
    RepositoryOwner: Optional[str] = None
    BranchName: Optional[str] = None
    Folder: Optional[str] = None
    CommitId: Optional[str] = None
    AuthStrategy: Optional[SourceControlAuthStrategyType] = None
    AuthToken: Optional[str] = None


class UpdateSourceControlFromJobRequestTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    Provider: Optional[SourceControlProviderType] = None
    RepositoryName: Optional[str] = None
    RepositoryOwner: Optional[str] = None
    BranchName: Optional[str] = None
    Folder: Optional[str] = None
    CommitId: Optional[str] = None
    AuthStrategy: Optional[SourceControlAuthStrategyType] = None
    AuthToken: Optional[str] = None


class UpdateWorkflowRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    DefaultRunProperties: Optional[Mapping[str, str]] = None
    MaxConcurrentRuns: Optional[int] = None


class UpsertRedshiftTargetOptionsTypeDef(BaseValidatorModel):
    TableLocation: Optional[str] = None
    ConnectionName: Optional[str] = None
    UpsertKeys: Optional[Sequence[str]] = None


class ViewRepresentationInputTypeDef(BaseValidatorModel):
    Dialect: Optional[ViewDialectType] = None
    DialectVersion: Optional[str] = None
    ViewOriginalText: Optional[str] = None
    ValidationConnection: Optional[str] = None
    ViewExpandedText: Optional[str] = None


class ViewRepresentationTypeDef(BaseValidatorModel):
    Dialect: Optional[ViewDialectType] = None
    DialectVersion: Optional[str] = None
    ViewOriginalText: Optional[str] = None
    ViewExpandedText: Optional[str] = None
    ValidationConnection: Optional[str] = None
    IsStale: Optional[bool] = None


class WorkflowRunStatisticsTypeDef(BaseValidatorModel):
    TotalActions: Optional[int] = None
    TimeoutActions: Optional[int] = None
    FailedActions: Optional[int] = None
    StoppedActions: Optional[int] = None
    SucceededActions: Optional[int] = None
    RunningActions: Optional[int] = None
    ErroredActions: Optional[int] = None
    WaitingActions: Optional[int] = None


class ActionOutputTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    Arguments: Optional[Dict[str, str]] = None
    Timeout: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationPropertyTypeDef] = None
    CrawlerName: Optional[str] = None


class ActionTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    Arguments: Optional[Mapping[str, str]] = None
    Timeout: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationPropertyTypeDef] = None
    CrawlerName: Optional[str] = None


class StartJobRunRequestTypeDef(BaseValidatorModel):
    JobName: str
    JobRunQueuingEnabled: Optional[bool] = None
    JobRunId: Optional[str] = None
    Arguments: Optional[Mapping[str, str]] = None
    AllocatedCapacity: Optional[int] = None
    Timeout: Optional[int] = None
    MaxCapacity: Optional[float] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationPropertyTypeDef] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    ExecutionClass: Optional[ExecutionClassType] = None


class AggregateOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Groups: List[List[str]]
    Aggs: List[AggregateOperationOutputTypeDef]


class AmazonRedshiftNodeDataOutputTypeDef(BaseValidatorModel):
    AccessType: Optional[str] = None
    SourceType: Optional[str] = None
    Connection: Optional[OptionTypeDef] = None
    Schema: Optional[OptionTypeDef] = None
    Table: Optional[OptionTypeDef] = None
    CatalogDatabase: Optional[OptionTypeDef] = None
    CatalogTable: Optional[OptionTypeDef] = None
    CatalogRedshiftSchema: Optional[str] = None
    CatalogRedshiftTable: Optional[str] = None
    TempDir: Optional[str] = None
    IamRole: Optional[OptionTypeDef] = None
    AdvancedOptions: Optional[List[AmazonRedshiftAdvancedOptionTypeDef]] = None
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
    TableSchema: Optional[List[OptionTypeDef]] = None
    StagingTable: Optional[str] = None
    SelectedColumns: Optional[List[OptionTypeDef]] = None


class AmazonRedshiftNodeDataTypeDef(BaseValidatorModel):
    AccessType: Optional[str] = None
    SourceType: Optional[str] = None
    Connection: Optional[OptionTypeDef] = None
    Schema: Optional[OptionTypeDef] = None
    Table: Optional[OptionTypeDef] = None
    CatalogDatabase: Optional[OptionTypeDef] = None
    CatalogTable: Optional[OptionTypeDef] = None
    CatalogRedshiftSchema: Optional[str] = None
    CatalogRedshiftTable: Optional[str] = None
    TempDir: Optional[str] = None
    IamRole: Optional[OptionTypeDef] = None
    AdvancedOptions: Optional[Sequence[AmazonRedshiftAdvancedOptionTypeDef]] = None
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
    TableSchema: Optional[Sequence[OptionTypeDef]] = None
    StagingTable: Optional[str] = None
    SelectedColumns: Optional[Sequence[OptionTypeDef]] = None


class SnowflakeNodeDataOutputTypeDef(BaseValidatorModel):
    SourceType: Optional[str] = None
    Connection: Optional[OptionTypeDef] = None
    Schema: Optional[str] = None
    Table: Optional[str] = None
    Database: Optional[str] = None
    TempDir: Optional[str] = None
    IamRole: Optional[OptionTypeDef] = None
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
    SelectedColumns: Optional[List[OptionTypeDef]] = None
    AutoPushdown: Optional[bool] = None
    TableSchema: Optional[List[OptionTypeDef]] = None


class SnowflakeNodeDataTypeDef(BaseValidatorModel):
    SourceType: Optional[str] = None
    Connection: Optional[OptionTypeDef] = None
    Schema: Optional[str] = None
    Table: Optional[str] = None
    Database: Optional[str] = None
    TempDir: Optional[str] = None
    IamRole: Optional[OptionTypeDef] = None
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
    SelectedColumns: Optional[Sequence[OptionTypeDef]] = None
    AutoPushdown: Optional[bool] = None
    TableSchema: Optional[Sequence[OptionTypeDef]] = None


class BackfillErrorTypeDef(BaseValidatorModel):
    Code: Optional[BackfillErrorCodeType] = None
    Partitions: Optional[List[PartitionValueListOutputTypeDef]] = None


class BatchPutDataQualityStatisticAnnotationResponseTypeDef(BaseValidatorModel):
    FailedInclusionAnnotations: List[AnnotationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CancelMLTaskRunResponseTypeDef(BaseValidatorModel):
    TransformId: str
    TaskRunId: str
    Status: TaskStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef


class CheckSchemaVersionValidityResponseTypeDef(BaseValidatorModel):
    Valid: bool
    Error: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateBlueprintResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateConnectionResponseTypeDef(BaseValidatorModel):
    CreateConnectionStatus: ConnectionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCustomEntityTypeResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataQualityRulesetResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDevEndpointResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class CreateJobResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMLTransformResponseTypeDef(BaseValidatorModel):
    TransformId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRegistryResponseTypeDef(BaseValidatorModel):
    RegistryArn: str
    RegistryName: str
    Description: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSchemaResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class CreateScriptResponseTypeDef(BaseValidatorModel):
    PythonScript: str
    ScalaCode: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSecurityConfigurationResponseTypeDef(BaseValidatorModel):
    Name: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class CreateTriggerResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateUsageProfileResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWorkflowResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteBlueprintResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCustomEntityTypeResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteJobResponseTypeDef(BaseValidatorModel):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteMLTransformResponseTypeDef(BaseValidatorModel):
    TransformId: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRegistryResponseTypeDef(BaseValidatorModel):
    RegistryName: str
    RegistryArn: str
    Status: RegistryStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSchemaResponseTypeDef(BaseValidatorModel):
    SchemaArn: str
    SchemaName: str
    Status: SchemaStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSessionResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteTriggerResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteWorkflowResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetCustomEntityTypeResponseTypeDef(BaseValidatorModel):
    Name: str
    RegexString: str
    ContextWords: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDataQualityModelResponseTypeDef(BaseValidatorModel):
    Status: DataQualityModelStatusType
    StartedOn: datetime
    CompletedOn: datetime
    FailureReason: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetEntityRecordsResponseTypeDef(BaseValidatorModel):
    Records: List[Dict[str, Any]]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetPlanResponseTypeDef(BaseValidatorModel):
    PythonScript: str
    ScalaCode: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRegistryResponseTypeDef(BaseValidatorModel):
    RegistryName: str
    RegistryArn: str
    Description: str
    Status: RegistryStatusType
    CreatedTime: str
    UpdatedTime: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetResourcePolicyResponseTypeDef(BaseValidatorModel):
    PolicyInJson: str
    PolicyHash: str
    CreateTime: datetime
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetSchemaByDefinitionResponseTypeDef(BaseValidatorModel):
    SchemaVersionId: str
    SchemaArn: str
    DataFormat: DataFormatType
    Status: SchemaVersionStatusType
    CreatedTime: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetSchemaResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class GetSchemaVersionResponseTypeDef(BaseValidatorModel):
    SchemaVersionId: str
    SchemaDefinition: str
    DataFormat: DataFormatType
    SchemaArn: str
    VersionNumber: int
    Status: SchemaVersionStatusType
    CreatedTime: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetSchemaVersionsDiffResponseTypeDef(BaseValidatorModel):
    Diff: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetTagsResponseTypeDef(BaseValidatorModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetWorkflowRunPropertiesResponseTypeDef(BaseValidatorModel):
    RunProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListBlueprintsResponseTypeDef(BaseValidatorModel):
    Blueprints: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListColumnStatisticsTaskRunsResponseTypeDef(BaseValidatorModel):
    ColumnStatisticsTaskRunIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListCrawlersResponseTypeDef(BaseValidatorModel):
    CrawlerNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDevEndpointsResponseTypeDef(BaseValidatorModel):
    DevEndpointNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListJobsResponseTypeDef(BaseValidatorModel):
    JobNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListMLTransformsResponseTypeDef(BaseValidatorModel):
    TransformIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListTriggersResponseTypeDef(BaseValidatorModel):
    TriggerNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListWorkflowsResponseTypeDef(BaseValidatorModel):
    Workflows: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PutResourcePolicyResponseTypeDef(BaseValidatorModel):
    PolicyHash: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutSchemaVersionMetadataResponseTypeDef(BaseValidatorModel):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    LatestVersion: bool
    VersionNumber: int
    SchemaVersionId: str
    MetadataKey: str
    MetadataValue: str
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterSchemaVersionResponseTypeDef(BaseValidatorModel):
    SchemaVersionId: str
    VersionNumber: int
    Status: SchemaVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class RemoveSchemaVersionMetadataResponseTypeDef(BaseValidatorModel):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    LatestVersion: bool
    VersionNumber: int
    SchemaVersionId: str
    MetadataKey: str
    MetadataValue: str
    ResponseMetadata: ResponseMetadataTypeDef


class ResumeWorkflowRunResponseTypeDef(BaseValidatorModel):
    RunId: str
    NodeIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class RunStatementResponseTypeDef(BaseValidatorModel):
    Id: int
    ResponseMetadata: ResponseMetadataTypeDef


class StartBlueprintRunResponseTypeDef(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartColumnStatisticsTaskRunResponseTypeDef(BaseValidatorModel):
    ColumnStatisticsTaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartDataQualityRuleRecommendationRunResponseTypeDef(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartDataQualityRulesetEvaluationRunResponseTypeDef(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartExportLabelsTaskRunResponseTypeDef(BaseValidatorModel):
    TaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartImportLabelsTaskRunResponseTypeDef(BaseValidatorModel):
    TaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartJobRunResponseTypeDef(BaseValidatorModel):
    JobRunId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartMLEvaluationTaskRunResponseTypeDef(BaseValidatorModel):
    TaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartMLLabelingSetGenerationTaskRunResponseTypeDef(BaseValidatorModel):
    TaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartTriggerResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartWorkflowRunResponseTypeDef(BaseValidatorModel):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StopSessionResponseTypeDef(BaseValidatorModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef


class StopTriggerResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBlueprintResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDataQualityRulesetResponseTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    Ruleset: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateJobFromSourceControlResponseTypeDef(BaseValidatorModel):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateJobResponseTypeDef(BaseValidatorModel):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMLTransformResponseTypeDef(BaseValidatorModel):
    TransformId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateRegistryResponseTypeDef(BaseValidatorModel):
    RegistryName: str
    RegistryArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSchemaResponseTypeDef(BaseValidatorModel):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSourceControlFromJobResponseTypeDef(BaseValidatorModel):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateUsageProfileResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateWorkflowResponseTypeDef(BaseValidatorModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDeleteConnectionResponseTypeDef(BaseValidatorModel):
    Succeeded: List[str]
    Errors: Dict[str, ErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchStopJobRunErrorTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None
    ErrorDetail: Optional[ErrorDetailTypeDef] = None


class BatchUpdatePartitionFailureEntryTypeDef(BaseValidatorModel):
    PartitionValueList: Optional[List[str]] = None
    ErrorDetail: Optional[ErrorDetailTypeDef] = None


class ColumnErrorTypeDef(BaseValidatorModel):
    ColumnName: Optional[str] = None
    Error: Optional[ErrorDetailTypeDef] = None


class PartitionErrorTypeDef(BaseValidatorModel):
    PartitionValues: Optional[List[str]] = None
    ErrorDetail: Optional[ErrorDetailTypeDef] = None


class TableErrorTypeDef(BaseValidatorModel):
    TableName: Optional[str] = None
    ErrorDetail: Optional[ErrorDetailTypeDef] = None


class TableVersionErrorTypeDef(BaseValidatorModel):
    TableName: Optional[str] = None
    VersionId: Optional[str] = None
    ErrorDetail: Optional[ErrorDetailTypeDef] = None


class ViewValidationTypeDef(BaseValidatorModel):
    Dialect: Optional[ViewDialectType] = None
    DialectVersion: Optional[str] = None
    ViewValidationText: Optional[str] = None
    UpdateTime: Optional[datetime] = None
    State: Optional[ResourceStateType] = None
    Error: Optional[ErrorDetailTypeDef] = None


class BatchGetCustomEntityTypesResponseTypeDef(BaseValidatorModel):
    CustomEntityTypes: List[CustomEntityTypeTypeDef]
    CustomEntityTypesNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListCustomEntityTypesResponseTypeDef(BaseValidatorModel):
    CustomEntityTypes: List[CustomEntityTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BatchGetDevEndpointsResponseTypeDef(BaseValidatorModel):
    DevEndpoints: List[DevEndpointTypeDef]
    DevEndpointsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDevEndpointResponseTypeDef(BaseValidatorModel):
    DevEndpoint: DevEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDevEndpointsResponseTypeDef(BaseValidatorModel):
    DevEndpoints: List[DevEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BatchGetTableOptimizerEntryTypeDef(BaseValidatorModel):
    pass


class BatchGetTableOptimizerRequestTypeDef(BaseValidatorModel):
    Entries: Sequence[BatchGetTableOptimizerEntryTypeDef]


class BatchPutDataQualityStatisticAnnotationRequestTypeDef(BaseValidatorModel):
    InclusionAnnotations: Sequence[DatapointInclusionAnnotationTypeDef]
    ClientToken: Optional[str] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class DecimalNumberTypeDef(BaseValidatorModel):
    UnscaledValue: BlobTypeDef
    Scale: int


class GetBlueprintRunResponseTypeDef(BaseValidatorModel):
    BlueprintRun: BlueprintRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetBlueprintRunsResponseTypeDef(BaseValidatorModel):
    BlueprintRuns: List[BlueprintRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BlueprintTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    ParameterSpec: Optional[str] = None
    BlueprintLocation: Optional[str] = None
    BlueprintServiceLocation: Optional[str] = None
    Status: Optional[BlueprintStatusType] = None
    ErrorMessage: Optional[str] = None
    LastActiveDefinition: Optional[LastActiveDefinitionTypeDef] = None


class ConnectionTypeBriefTypeDef(BaseValidatorModel):
    ConnectionType: Optional[ConnectionTypeType] = None
    Description: Optional[str] = None
    Capabilities: Optional[CapabilitiesTypeDef] = None


class GetCatalogImportStatusResponseTypeDef(BaseValidatorModel):
    ImportStatus: CatalogImportStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CatalogKafkaSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KafkaStreamingSourceOptionsOutputTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None


class DirectKafkaSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    StreamingOptions: Optional[KafkaStreamingSourceOptionsOutputTypeDef] = None
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None


class CatalogKinesisSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsOutputTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None


class DirectKinesisSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsOutputTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None


class CatalogPropertiesOutputTypeDef(BaseValidatorModel):
    DataLakeAccessProperties: Optional[DataLakeAccessPropertiesOutputTypeDef] = None
    CustomProperties: Optional[Dict[str, str]] = None


class CatalogPropertiesTypeDef(BaseValidatorModel):
    DataLakeAccessProperties: Optional[DataLakeAccessPropertiesTypeDef] = None
    CustomProperties: Optional[Mapping[str, str]] = None


class GovernedCatalogTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None


class GovernedCatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None


class S3CatalogTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None


class S3CatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None


class S3DeltaCatalogTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    AdditionalOptions: Optional[Dict[str, str]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None


class S3DeltaCatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    AdditionalOptions: Optional[Mapping[str, str]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None


class S3HudiCatalogTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    AdditionalOptions: Dict[str, str]
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None


class S3HudiCatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    AdditionalOptions: Mapping[str, str]
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None


class ClassifierTypeDef(BaseValidatorModel):
    GrokClassifier: Optional[GrokClassifierTypeDef] = None
    XMLClassifier: Optional[XMLClassifierTypeDef] = None
    JsonClassifier: Optional[JsonClassifierTypeDef] = None
    CsvClassifier: Optional[CsvClassifierTypeDef] = None


class CodeGenNodeOutputTypeDef(BaseValidatorModel):
    Id: str
    NodeType: str
    Args: List[CodeGenNodeArgTypeDef]
    LineNumber: Optional[int] = None


class CodeGenNodeTypeDef(BaseValidatorModel):
    Id: str
    NodeType: str
    Args: Sequence[CodeGenNodeArgTypeDef]
    LineNumber: Optional[int] = None


class LocationTypeDef(BaseValidatorModel):
    Jdbc: Optional[Sequence[CodeGenNodeArgTypeDef]] = None
    S3: Optional[Sequence[CodeGenNodeArgTypeDef]] = None
    DynamoDB: Optional[Sequence[CodeGenNodeArgTypeDef]] = None


class GetColumnStatisticsTaskRunResponseTypeDef(BaseValidatorModel):
    ColumnStatisticsTaskRun: ColumnStatisticsTaskRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetColumnStatisticsTaskRunsResponseTypeDef(BaseValidatorModel):
    ColumnStatisticsTaskRuns: List[ColumnStatisticsTaskRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ColumnStatisticsTaskSettingsTypeDef(BaseValidatorModel):
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    Schedule: Optional[ScheduleTypeDef] = None
    ColumnNameList: Optional[List[str]] = None
    CatalogID: Optional[str] = None
    Role: Optional[str] = None
    SampleSize: Optional[float] = None
    SecurityConfiguration: Optional[str] = None
    ScheduleType: Optional[ScheduleTypeType] = None
    SettingSource: Optional[SettingSourceType] = None
    LastExecutionAttempt: Optional[ExecutionAttemptTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class DateColumnStatisticsDataTypeDef(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[TimestampTypeDef] = None
    MaximumValue: Optional[TimestampTypeDef] = None


class GetTableRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None
    IncludeStatusDetails: Optional[bool] = None


class GetTablesRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None
    IncludeStatusDetails: Optional[bool] = None
    AttributesToGet: Optional[Sequence[TableAttributesType]] = None


class KafkaStreamingSourceOptionsTypeDef(BaseValidatorModel):
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
    StartingTimestamp: Optional[TimestampTypeDef] = None


class KinesisStreamingSourceOptionsTypeDef(BaseValidatorModel):
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
    StartingTimestamp: Optional[TimestampTypeDef] = None


class QuerySessionContextTypeDef(BaseValidatorModel):
    QueryId: Optional[str] = None
    QueryStartTime: Optional[TimestampTypeDef] = None
    ClusterId: Optional[str] = None
    QueryAuthorizationId: Optional[str] = None
    AdditionalContext: Optional[Mapping[str, str]] = None


class TaskRunFilterCriteriaTypeDef(BaseValidatorModel):
    TaskRunType: Optional[TaskTypeType] = None
    Status: Optional[TaskStatusTypeType] = None
    StartedBefore: Optional[TimestampTypeDef] = None
    StartedAfter: Optional[TimestampTypeDef] = None


class TimestampFilterTypeDef(BaseValidatorModel):
    RecordedBefore: Optional[TimestampTypeDef] = None
    RecordedAfter: Optional[TimestampTypeDef] = None


class CompactionMetricsTypeDef(BaseValidatorModel):
    IcebergMetrics: Optional[IcebergCompactionMetricsTypeDef] = None


class PredicateOutputTypeDef(BaseValidatorModel):
    Logical: Optional[LogicalType] = None
    Conditions: Optional[List[ConditionTypeDef]] = None


class PredicateTypeDef(BaseValidatorModel):
    Logical: Optional[LogicalType] = None
    Conditions: Optional[Sequence[ConditionTypeDef]] = None


class ProfileConfigurationOutputTypeDef(BaseValidatorModel):
    SessionConfiguration: Optional[Dict[str, ConfigurationObjectOutputTypeDef]] = None
    JobConfiguration: Optional[Dict[str, ConfigurationObjectOutputTypeDef]] = None


class ProfileConfigurationTypeDef(BaseValidatorModel):
    SessionConfiguration: Optional[Mapping[str, ConfigurationObjectTypeDef]] = None
    JobConfiguration: Optional[Mapping[str, ConfigurationObjectTypeDef]] = None


class FindMatchesMetricsTypeDef(BaseValidatorModel):
    AreaUnderPRCurve: Optional[float] = None
    Precision: Optional[float] = None
    Recall: Optional[float] = None
    F1: Optional[float] = None
    ConfusionMatrix: Optional[ConfusionMatrixTypeDef] = None
    ColumnImportances: Optional[List[ColumnImportanceTypeDef]] = None


class CrawlerNodeDetailsTypeDef(BaseValidatorModel):
    Crawls: Optional[List[CrawlTypeDef]] = None


class ListCrawlsResponseTypeDef(BaseValidatorModel):
    Crawls: List[CrawlerHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetCrawlerMetricsResponseTypeDef(BaseValidatorModel):
    CrawlerMetricsList: List[CrawlerMetricsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CrawlerTargetsOutputTypeDef(BaseValidatorModel):
    S3Targets: Optional[List[S3TargetOutputTypeDef]] = None
    JdbcTargets: Optional[List[JdbcTargetOutputTypeDef]] = None
    MongoDBTargets: Optional[List[MongoDBTargetTypeDef]] = None
    DynamoDBTargets: Optional[List[DynamoDBTargetTypeDef]] = None
    CatalogTargets: Optional[List[CatalogTargetOutputTypeDef]] = None
    DeltaTargets: Optional[List[DeltaTargetOutputTypeDef]] = None
    IcebergTargets: Optional[List[IcebergTargetOutputTypeDef]] = None
    HudiTargets: Optional[List[HudiTargetOutputTypeDef]] = None


class CrawlerTargetsTypeDef(BaseValidatorModel):
    S3Targets: Optional[Sequence[S3TargetTypeDef]] = None
    JdbcTargets: Optional[Sequence[JdbcTargetTypeDef]] = None
    MongoDBTargets: Optional[Sequence[MongoDBTargetTypeDef]] = None
    DynamoDBTargets: Optional[Sequence[DynamoDBTargetTypeDef]] = None
    CatalogTargets: Optional[Sequence[CatalogTargetTypeDef]] = None
    DeltaTargets: Optional[Sequence[DeltaTargetTypeDef]] = None
    IcebergTargets: Optional[Sequence[IcebergTargetTypeDef]] = None
    HudiTargets: Optional[Sequence[HudiTargetTypeDef]] = None


class ListCrawlsRequestTypeDef(BaseValidatorModel):
    CrawlerName: str
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[CrawlsFilterTypeDef]] = None
    NextToken: Optional[str] = None


class CreateClassifierRequestTypeDef(BaseValidatorModel):
    GrokClassifier: Optional[CreateGrokClassifierRequestTypeDef] = None
    XMLClassifier: Optional[CreateXMLClassifierRequestTypeDef] = None
    JsonClassifier: Optional[CreateJsonClassifierRequestTypeDef] = None
    CsvClassifier: Optional[CreateCsvClassifierRequestTypeDef] = None


class CreateDataQualityRulesetRequestTypeDef(BaseValidatorModel):
    Name: str
    Ruleset: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    TargetTable: Optional[DataQualityTargetTableTypeDef] = None
    DataQualitySecurityConfiguration: Optional[str] = None
    ClientToken: Optional[str] = None


class DataQualityRulesetFilterCriteriaTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    LastModifiedBefore: Optional[TimestampTypeDef] = None
    LastModifiedAfter: Optional[TimestampTypeDef] = None
    TargetTable: Optional[DataQualityTargetTableTypeDef] = None


class DataQualityRulesetListDetailsTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    TargetTable: Optional[DataQualityTargetTableTypeDef] = None
    RecommendationRunId: Optional[str] = None
    RuleCount: Optional[int] = None


class GetDataQualityRulesetResponseTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    Ruleset: str
    TargetTable: DataQualityTargetTableTypeDef
    CreatedOn: datetime
    LastModifiedOn: datetime
    RecommendationRunId: str
    DataQualitySecurityConfiguration: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIntegrationRequestTypeDef(BaseValidatorModel):
    IntegrationName: str
    SourceArn: str
    TargetArn: str
    Description: Optional[str] = None
    DataFilter: Optional[str] = None
    KmsKeyId: Optional[str] = None
    AdditionalEncryptionContext: Optional[Mapping[str, str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateIntegrationResourcePropertyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    SourceProcessingProperties: Optional[SourceProcessingPropertiesTypeDef] = None
    TargetProcessingProperties: Optional[TargetProcessingPropertiesTypeDef] = None


class CreateIntegrationResourcePropertyResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    SourceProcessingProperties: SourceProcessingPropertiesTypeDef
    TargetProcessingProperties: TargetProcessingPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetIntegrationResourcePropertyResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    SourceProcessingProperties: SourceProcessingPropertiesTypeDef
    TargetProcessingProperties: TargetProcessingPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateIntegrationResourcePropertyRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    SourceProcessingProperties: Optional[SourceProcessingPropertiesTypeDef] = None
    TargetProcessingProperties: Optional[TargetProcessingPropertiesTypeDef] = None


class UpdateIntegrationResourcePropertyResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    SourceProcessingProperties: SourceProcessingPropertiesTypeDef
    TargetProcessingProperties: TargetProcessingPropertiesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIntegrationResponseTypeDef(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    Description: str
    IntegrationArn: str
    KmsKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Tags: List[TagTypeDef]
    Status: IntegrationStatusType
    CreateTime: datetime
    Errors: List[IntegrationErrorTypeDef]
    DataFilter: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteIntegrationResponseTypeDef(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    Description: str
    IntegrationArn: str
    KmsKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Tags: List[TagTypeDef]
    Status: IntegrationStatusType
    CreateTime: datetime
    Errors: List[IntegrationErrorTypeDef]
    DataFilter: str
    ResponseMetadata: ResponseMetadataTypeDef


class InboundIntegrationTypeDef(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationArn: str
    Status: IntegrationStatusType
    CreateTime: datetime
    Errors: Optional[List[IntegrationErrorTypeDef]] = None


class IntegrationTypeDef(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    IntegrationArn: str
    Status: IntegrationStatusType
    CreateTime: datetime
    Description: Optional[str] = None
    KmsKeyId: Optional[str] = None
    AdditionalEncryptionContext: Optional[Dict[str, str]] = None
    Tags: Optional[List[TagTypeDef]] = None
    Errors: Optional[List[IntegrationErrorTypeDef]] = None
    DataFilter: Optional[str] = None


class ModifyIntegrationResponseTypeDef(BaseValidatorModel):
    SourceArn: str
    TargetArn: str
    IntegrationName: str
    Description: str
    IntegrationArn: str
    KmsKeyId: str
    AdditionalEncryptionContext: Dict[str, str]
    Tags: List[TagTypeDef]
    Status: IntegrationStatusType
    CreateTime: datetime
    Errors: List[IntegrationErrorTypeDef]
    DataFilter: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePartitionIndexRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionIndex: PartitionIndexTypeDef
    CatalogId: Optional[str] = None


class CreateSchemaInputTypeDef(BaseValidatorModel):
    SchemaName: str
    DataFormat: DataFormatType
    RegistryId: Optional[RegistryIdTypeDef] = None
    Compatibility: Optional[CompatibilityType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    SchemaDefinition: Optional[str] = None


class DeleteRegistryInputTypeDef(BaseValidatorModel):
    RegistryId: RegistryIdTypeDef


class GetRegistryInputTypeDef(BaseValidatorModel):
    RegistryId: RegistryIdTypeDef


class ListSchemasInputTypeDef(BaseValidatorModel):
    RegistryId: Optional[RegistryIdTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class UpdateRegistryInputTypeDef(BaseValidatorModel):
    RegistryId: RegistryIdTypeDef
    Description: str


class SessionTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    Status: Optional[SessionStatusType] = None
    ErrorMessage: Optional[str] = None
    Description: Optional[str] = None
    Role: Optional[str] = None
    Command: Optional[SessionCommandTypeDef] = None
    DefaultArguments: Optional[Dict[str, str]] = None
    Connections: Optional[ConnectionsListOutputTypeDef] = None
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


class EvaluateDataQualityMultiFrameOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Ruleset: str
    AdditionalDataSources: Optional[Dict[str, str]] = None
    PublishingOptions: Optional[DQResultsPublishingOptionsTypeDef] = None
    AdditionalOptions: Optional[Dict[AdditionalOptionKeysType, str]] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptionsTypeDef] = None


class EvaluateDataQualityMultiFrameTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Ruleset: str
    AdditionalDataSources: Optional[Mapping[str, str]] = None
    PublishingOptions: Optional[DQResultsPublishingOptionsTypeDef] = None
    AdditionalOptions: Optional[Mapping[AdditionalOptionKeysType, str]] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptionsTypeDef] = None


class EvaluateDataQualityOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Ruleset: str
    Output: Optional[DQTransformOutputType] = None
    PublishingOptions: Optional[DQResultsPublishingOptionsTypeDef] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptionsTypeDef] = None


class EvaluateDataQualityTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Ruleset: str
    Output: Optional[DQTransformOutputType] = None
    PublishingOptions: Optional[DQResultsPublishingOptionsTypeDef] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptionsTypeDef] = None


class DataCatalogEncryptionSettingsTypeDef(BaseValidatorModel):
    EncryptionAtRest: Optional[EncryptionAtRestTypeDef] = None
    ConnectionPasswordEncryption: Optional[ConnectionPasswordEncryptionTypeDef] = None


class PrincipalPermissionsOutputTypeDef(BaseValidatorModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Permissions: Optional[List[PermissionType]] = None


class PrincipalPermissionsTypeDef(BaseValidatorModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Permissions: Optional[Sequence[PermissionType]] = None


class MetricBasedObservationTypeDef(BaseValidatorModel):
    MetricName: Optional[str] = None
    StatisticId: Optional[str] = None
    MetricValues: Optional[DataQualityMetricValuesTypeDef] = None
    NewRules: Optional[List[str]] = None


class DataSourceOutputTypeDef(BaseValidatorModel):
    GlueTable: GlueTableOutputTypeDef


class NullValueFieldTypeDef(BaseValidatorModel):
    Value: str
    Datatype: DatatypeTypeDef


class DecimalColumnStatisticsDataOutputTypeDef(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[DecimalNumberOutputTypeDef] = None
    MaximumValue: Optional[DecimalNumberOutputTypeDef] = None


class DeleteSchemaInputTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef


class DeleteSchemaVersionsInputTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    Versions: str


class GetSchemaByDefinitionInputTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    SchemaDefinition: str


class GetSchemaInputTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef


class ListSchemaVersionsInputTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RegisterSchemaVersionInputTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    SchemaDefinition: str


class SchemaReferenceTypeDef(BaseValidatorModel):
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionId: Optional[str] = None
    SchemaVersionNumber: Optional[int] = None


class DescribeEntityRequestPaginateTypeDef(BaseValidatorModel):
    ConnectionName: str
    EntityName: str
    CatalogId: Optional[str] = None
    DataStoreApiVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetClassifiersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetCrawlerMetricsRequestPaginateTypeDef(BaseValidatorModel):
    CrawlerNameList: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetCrawlersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetDatabasesRequestPaginateTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    AttributesToGet: Optional[Sequence[Literal["NAME"]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetDevEndpointsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetJobRunsRequestPaginateTypeDef(BaseValidatorModel):
    JobName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetJobsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetPartitionIndexesRequestPaginateTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetResourcePoliciesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetSecurityConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetTableVersionsRequestPaginateTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetTablesRequestPaginateTypeDef(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None
    IncludeStatusDetails: Optional[bool] = None
    AttributesToGet: Optional[Sequence[TableAttributesType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetTriggersRequestPaginateTypeDef(BaseValidatorModel):
    DependentJobName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetWorkflowRunsRequestPaginateTypeDef(BaseValidatorModel):
    Name: str
    IncludeGraph: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBlueprintsRequestPaginateTypeDef(BaseValidatorModel):
    Tags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConnectionTypesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEntitiesRequestPaginateTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    CatalogId: Optional[str] = None
    ParentEntityName: Optional[str] = None
    DataStoreApiVersion: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobsRequestPaginateTypeDef(BaseValidatorModel):
    Tags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRegistriesInputPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSchemaVersionsInputPaginateTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSchemasInputPaginateTypeDef(BaseValidatorModel):
    RegistryId: Optional[RegistryIdTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTriggersRequestPaginateTypeDef(BaseValidatorModel):
    DependentJobName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsageProfilesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWorkflowsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEntityResponseTypeDef(BaseValidatorModel):
    Fields: List[FieldTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeIntegrationsRequestTypeDef(BaseValidatorModel):
    IntegrationIdentifier: Optional[str] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    Filters: Optional[Sequence[IntegrationFilterTypeDef]] = None


class UpdateDevEndpointRequestTypeDef(BaseValidatorModel):
    EndpointName: str
    PublicKey: Optional[str] = None
    AddPublicKeys: Optional[Sequence[str]] = None
    DeletePublicKeys: Optional[Sequence[str]] = None
    CustomLibraries: Optional[DevEndpointCustomLibrariesTypeDef] = None
    UpdateEtlLibraries: Optional[bool] = None
    DeleteArguments: Optional[Sequence[str]] = None
    AddArguments: Optional[Mapping[str, str]] = None


class S3DeltaDirectTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    Compression: DeltaTargetCompressionTypeType
    Format: TargetFormatType
    PartitionKeys: Optional[List[List[str]]] = None
    AdditionalOptions: Optional[Dict[str, str]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None


class S3DeltaDirectTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Compression: DeltaTargetCompressionTypeType
    Format: TargetFormatType
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    AdditionalOptions: Optional[Mapping[str, str]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None


class S3DirectTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    Format: TargetFormatType
    PartitionKeys: Optional[List[List[str]]] = None
    Compression: Optional[str] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None


class S3DirectTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Format: TargetFormatType
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    Compression: Optional[str] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None


class S3GlueParquetTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    PartitionKeys: Optional[List[List[str]]] = None
    Compression: Optional[ParquetCompressionTypeType] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None


class S3GlueParquetTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    Compression: Optional[ParquetCompressionTypeType] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None


class S3HudiDirectTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    Compression: HudiTargetCompressionTypeType
    Format: TargetFormatType
    AdditionalOptions: Dict[str, str]
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None


class S3HudiDirectTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Compression: HudiTargetCompressionTypeType
    Format: TargetFormatType
    AdditionalOptions: Mapping[str, str]
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None


class EncryptionConfigurationOutputTypeDef(BaseValidatorModel):
    S3Encryption: Optional[List[S3EncryptionTypeDef]] = None
    CloudWatchEncryption: Optional[CloudWatchEncryptionTypeDef] = None
    JobBookmarksEncryption: Optional[JobBookmarksEncryptionTypeDef] = None
    DataQualityEncryption: Optional[DataQualityEncryptionTypeDef] = None


class EncryptionConfigurationTypeDef(BaseValidatorModel):
    S3Encryption: Optional[Sequence[S3EncryptionTypeDef]] = None
    CloudWatchEncryption: Optional[CloudWatchEncryptionTypeDef] = None
    JobBookmarksEncryption: Optional[JobBookmarksEncryptionTypeDef] = None
    DataQualityEncryption: Optional[DataQualityEncryptionTypeDef] = None


class ListEntitiesResponseTypeDef(BaseValidatorModel):
    Entities: List[EntityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SchemaVersionErrorItemTypeDef(BaseValidatorModel):
    VersionNumber: Optional[int] = None
    ErrorDetails: Optional[ErrorDetailsTypeDef] = None


class FilterValueOutputTypeDef(BaseValidatorModel):
    pass


class FilterExpressionOutputTypeDef(BaseValidatorModel):
    Operation: FilterOperationType
    Values: List[FilterValueOutputTypeDef]
    Negated: Optional[bool] = None


class TransformParametersTypeDef(BaseValidatorModel):
    TransformType: Literal["FIND_MATCHES"]
    FindMatchesParameters: Optional[FindMatchesParametersTypeDef] = None


class GetConnectionsRequestPaginateTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    Filter: Optional[GetConnectionsFilterTypeDef] = None
    HidePassword: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetConnectionsRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    Filter: Optional[GetConnectionsFilterTypeDef] = None
    HidePassword: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetDataQualityModelResultResponseTypeDef(BaseValidatorModel):
    CompletedOn: datetime
    Model: List[StatisticModelResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetJobBookmarkResponseTypeDef(BaseValidatorModel):
    JobBookmarkEntry: JobBookmarkEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ResetJobBookmarkResponseTypeDef(BaseValidatorModel):
    JobBookmarkEntry: JobBookmarkEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TransformFilterCriteriaTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    TransformType: Optional[Literal["FIND_MATCHES"]] = None
    Status: Optional[TransformStatusTypeType] = None
    GlueVersion: Optional[str] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    LastModifiedBefore: Optional[TimestampTypeDef] = None
    LastModifiedAfter: Optional[TimestampTypeDef] = None
    Schema: Optional[Sequence[SchemaColumnTypeDef]] = None


class GetPartitionsRequestPaginateTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    Segment: Optional[SegmentTypeDef] = None
    ExcludeColumnSchema: Optional[bool] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetPartitionsRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    NextToken: Optional[str] = None
    Segment: Optional[SegmentTypeDef] = None
    MaxResults: Optional[int] = None
    ExcludeColumnSchema: Optional[bool] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None


class GetResourcePoliciesResponseTypeDef(BaseValidatorModel):
    GetResourcePoliciesResponseList: List[GluePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetSchemaVersionInputTypeDef(BaseValidatorModel):
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionId: Optional[str] = None
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None


class GetSchemaVersionsDiffInputTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    FirstSchemaVersionNumber: SchemaVersionNumberTypeDef
    SecondSchemaVersionNumber: SchemaVersionNumberTypeDef
    SchemaDiffType: Literal["SYNTAX_DIFF"]


class UpdateSchemaInputTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None
    Compatibility: Optional[CompatibilityType] = None
    Description: Optional[str] = None


class GlueStudioSchemaColumnTypeDef(BaseValidatorModel):
    pass


class GlueSchemaOutputTypeDef(BaseValidatorModel):
    Columns: Optional[List[GlueStudioSchemaColumnTypeDef]] = None


class GlueSchemaTypeDef(BaseValidatorModel):
    Columns: Optional[Sequence[GlueStudioSchemaColumnTypeDef]] = None


class GovernedCatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    PartitionPredicate: Optional[str] = None
    AdditionalOptions: Optional[S3SourceAdditionalOptionsTypeDef] = None


class S3CatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    PartitionPredicate: Optional[str] = None
    AdditionalOptions: Optional[S3SourceAdditionalOptionsTypeDef] = None


class OpenTableFormatInputTypeDef(BaseValidatorModel):
    IcebergInput: Optional[IcebergInputTypeDef] = None


class OrphanFileDeletionConfigurationTypeDef(BaseValidatorModel):
    icebergConfiguration: Optional[IcebergOrphanFileDeletionConfigurationTypeDef] = None


class OrphanFileDeletionMetricsTypeDef(BaseValidatorModel):
    IcebergMetrics: Optional[IcebergOrphanFileDeletionMetricsTypeDef] = None


class RetentionConfigurationTypeDef(BaseValidatorModel):
    icebergConfiguration: Optional[IcebergRetentionConfigurationTypeDef] = None


class RetentionMetricsTypeDef(BaseValidatorModel):
    IcebergMetrics: Optional[IcebergRetentionMetricsTypeDef] = None


class TargetTableConfigOutputTypeDef(BaseValidatorModel):
    UnnestSpec: Optional[UnnestSpecType] = None
    PartitionSpec: Optional[List[IntegrationPartitionTypeDef]] = None
    TargetTableName: Optional[str] = None


class TargetTableConfigTypeDef(BaseValidatorModel):
    UnnestSpec: Optional[UnnestSpecType] = None
    PartitionSpec: Optional[Sequence[IntegrationPartitionTypeDef]] = None
    TargetTableName: Optional[str] = None


class JobRunTypeDef(BaseValidatorModel):
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
    PredecessorRuns: Optional[List[PredecessorTypeDef]] = None
    AllocatedCapacity: Optional[int] = None
    ExecutionTime: Optional[int] = None
    Timeout: Optional[int] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    LogGroupName: Optional[str] = None
    NotificationProperty: Optional[NotificationPropertyTypeDef] = None
    GlueVersion: Optional[str] = None
    DPUSeconds: Optional[float] = None
    ExecutionClass: Optional[ExecutionClassType] = None
    MaintenanceWindow: Optional[str] = None
    ProfileName: Optional[str] = None
    StateDetail: Optional[str] = None


class JoinOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    JoinType: JoinTypeType
    Columns: List[JoinColumnOutputTypeDef]


class TaskRunPropertiesTypeDef(BaseValidatorModel):
    TaskType: Optional[TaskTypeType] = None
    ImportLabelsTaskRunProperties: Optional[ImportLabelsTaskRunPropertiesTypeDef] = None
    ExportLabelsTaskRunProperties: Optional[ExportLabelsTaskRunPropertiesTypeDef] = None
    LabelingSetGenerationTaskRunProperties: Optional[ LabelingSetGenerationTaskRunPropertiesTypeDef ] = None
    FindMatchesTaskRunProperties: Optional[FindMatchesTaskRunPropertiesTypeDef] = None


class ListRegistriesResponseTypeDef(BaseValidatorModel):
    Registries: List[RegistryListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSchemaVersionsResponseTypeDef(BaseValidatorModel):
    Schemas: List[SchemaVersionListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSchemasResponseTypeDef(BaseValidatorModel):
    Schemas: List[SchemaListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListUsageProfilesResponseTypeDef(BaseValidatorModel):
    Profiles: List[UsageProfileDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TransformEncryptionTypeDef(BaseValidatorModel):
    MlUserDataEncryption: Optional[MLUserDataEncryptionTypeDef] = None
    TaskRunSecurityConfigurationName: Optional[str] = None


class MetadataInfoTypeDef(BaseValidatorModel):
    MetadataValue: Optional[str] = None
    CreatedTime: Optional[str] = None
    OtherMetadataValueList: Optional[List[OtherMetadataValueListItemTypeDef]] = None


class PutSchemaVersionMetadataInputTypeDef(BaseValidatorModel):
    MetadataKeyValue: MetadataKeyValuePairTypeDef
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None
    SchemaVersionId: Optional[str] = None


class QuerySchemaVersionMetadataInputTypeDef(BaseValidatorModel):
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None
    SchemaVersionId: Optional[str] = None
    MetadataList: Optional[Sequence[MetadataKeyValuePairTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class RemoveSchemaVersionMetadataInputTypeDef(BaseValidatorModel):
    MetadataKeyValue: MetadataKeyValuePairTypeDef
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None
    SchemaVersionId: Optional[str] = None


class OAuth2PropertiesTypeDef(BaseValidatorModel):
    OAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    OAuth2ClientApplication: Optional[OAuth2ClientApplicationTypeDef] = None
    TokenUrl: Optional[str] = None
    TokenUrlParametersMap: Optional[Dict[str, str]] = None


class OAuth2PropertiesInputTypeDef(BaseValidatorModel):
    OAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    OAuth2ClientApplication: Optional[OAuth2ClientApplicationTypeDef] = None
    TokenUrl: Optional[str] = None
    TokenUrlParametersMap: Optional[Mapping[str, str]] = None
    AuthorizationCodeProperties: Optional[AuthorizationCodePropertiesTypeDef] = None
    OAuth2Credentials: Optional[OAuth2CredentialsTypeDef] = None


class RecipeStepOutputTypeDef(BaseValidatorModel):
    Action: RecipeActionOutputTypeDef
    ConditionExpressions: Optional[List[ConditionExpressionTypeDef]] = None


class RedshiftTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str
    RedshiftTmpDir: Optional[str] = None
    TmpDirIAMRole: Optional[str] = None
    UpsertRedshiftOptions: Optional[UpsertRedshiftTargetOptionsOutputTypeDef] = None


class UserDefinedFunctionInputTypeDef(BaseValidatorModel):
    FunctionName: Optional[str] = None
    ClassName: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerType: Optional[PrincipalTypeType] = None
    ResourceUris: Optional[Sequence[ResourceUriTypeDef]] = None


class UserDefinedFunctionTypeDef(BaseValidatorModel):
    FunctionName: Optional[str] = None
    DatabaseName: Optional[str] = None
    ClassName: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerType: Optional[PrincipalTypeType] = None
    CreateTime: Optional[datetime] = None
    ResourceUris: Optional[List[ResourceUriTypeDef]] = None
    CatalogId: Optional[str] = None


class SearchTablesRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[PropertyPredicateTypeDef]] = None
    SearchText: Optional[str] = None
    SortCriteria: Optional[Sequence[SortCriterionTypeDef]] = None
    MaxResults: Optional[int] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    IncludeStatusDetails: Optional[bool] = None


class StatementOutputTypeDef(BaseValidatorModel):
    Data: Optional[StatementOutputDataTypeDef] = None
    ExecutionCount: Optional[int] = None
    Status: Optional[StatementStateType] = None
    ErrorName: Optional[str] = None
    ErrorValue: Optional[str] = None
    Traceback: Optional[List[str]] = None


class StatisticAnnotationTypeDef(BaseValidatorModel):
    ProfileId: Optional[str] = None
    StatisticId: Optional[str] = None
    StatisticRecordedOn: Optional[datetime] = None
    InclusionAnnotation: Optional[TimestampedInclusionAnnotationTypeDef] = None


class StatisticSummaryTypeDef(BaseValidatorModel):
    StatisticId: Optional[str] = None
    ProfileId: Optional[str] = None
    RunIdentifier: Optional[RunIdentifierTypeDef] = None
    StatisticName: Optional[str] = None
    DoubleValue: Optional[float] = None
    EvaluationLevel: Optional[StatisticEvaluationLevelType] = None
    ColumnsReferenced: Optional[List[str]] = None
    ReferencedDatasets: Optional[List[str]] = None
    StatisticProperties: Optional[Dict[str, str]] = None
    RecordedOn: Optional[datetime] = None
    InclusionAnnotation: Optional[TimestampedInclusionAnnotationTypeDef] = None


class UpdateClassifierRequestTypeDef(BaseValidatorModel):
    GrokClassifier: Optional[UpdateGrokClassifierRequestTypeDef] = None
    XMLClassifier: Optional[UpdateXMLClassifierRequestTypeDef] = None
    JsonClassifier: Optional[UpdateJsonClassifierRequestTypeDef] = None
    CsvClassifier: Optional[UpdateCsvClassifierRequestTypeDef] = None


class ViewDefinitionInputTypeDef(BaseValidatorModel):
    IsProtected: Optional[bool] = None
    Definer: Optional[str] = None
    Representations: Optional[Sequence[ViewRepresentationInputTypeDef]] = None
    SubObjects: Optional[Sequence[str]] = None


class ViewDefinitionTypeDef(BaseValidatorModel):
    IsProtected: Optional[bool] = None
    Definer: Optional[str] = None
    SubObjects: Optional[List[str]] = None
    Representations: Optional[List[ViewRepresentationTypeDef]] = None


class AggregateOperationUnionTypeDef(BaseValidatorModel):
    pass


class AggregateTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Groups: Sequence[Sequence[str]]
    Aggs: Sequence[AggregateOperationUnionTypeDef]


class PropertyTypeDef(BaseValidatorModel):
    pass


class AuthConfigurationTypeDef(BaseValidatorModel):
    AuthenticationType: PropertyTypeDef
    SecretArn: Optional[PropertyTypeDef] = None
    OAuth2Properties: Optional[Dict[str, PropertyTypeDef]] = None
    BasicAuthenticationProperties: Optional[Dict[str, PropertyTypeDef]] = None
    CustomAuthenticationProperties: Optional[Dict[str, PropertyTypeDef]] = None


class ComputeEnvironmentConfigurationTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    ComputeEnvironment: ComputeEnvironmentType
    SupportedAuthenticationTypes: List[AuthenticationTypeType]
    ConnectionOptions: Dict[str, PropertyTypeDef]
    ConnectionPropertyNameOverrides: Dict[str, str]
    ConnectionOptionNameOverrides: Dict[str, str]
    ConnectionPropertiesRequiredOverrides: List[str]
    PhysicalConnectionPropertiesRequired: Optional[bool] = None


class AmazonRedshiftSourceOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataOutputTypeDef] = None


class AmazonRedshiftTargetOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataOutputTypeDef] = None
    Inputs: Optional[List[str]] = None


class SnowflakeTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Data: SnowflakeNodeDataOutputTypeDef
    Inputs: Optional[List[str]] = None


class KeySchemaElementTypeDef(BaseValidatorModel):
    pass


class PartitionIndexDescriptorTypeDef(BaseValidatorModel):
    IndexName: str
    Keys: List[KeySchemaElementTypeDef]
    IndexStatus: PartitionIndexStatusType
    BackfillErrors: Optional[List[BackfillErrorTypeDef]] = None


class BatchStopJobRunResponseTypeDef(BaseValidatorModel):
    SuccessfulSubmissions: List[BatchStopJobRunSuccessfulSubmissionTypeDef]
    Errors: List[BatchStopJobRunErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchUpdatePartitionResponseTypeDef(BaseValidatorModel):
    Errors: List[BatchUpdatePartitionFailureEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchCreatePartitionResponseTypeDef(BaseValidatorModel):
    Errors: List[PartitionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDeletePartitionResponseTypeDef(BaseValidatorModel):
    Errors: List[PartitionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDeleteTableResponseTypeDef(BaseValidatorModel):
    Errors: List[TableErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDeleteTableVersionResponseTypeDef(BaseValidatorModel):
    Errors: List[TableVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StatusDetailsPaginatorTypeDef(BaseValidatorModel):
    RequestedChange: Optional[Dict[str, Any]] = None
    ViewValidations: Optional[List[ViewValidationTypeDef]] = None


class StatusDetailsTypeDef(BaseValidatorModel):
    RequestedChange: Optional[Dict[str, Any]] = None
    ViewValidations: Optional[List[ViewValidationTypeDef]] = None


class BatchGetBlueprintsResponseTypeDef(BaseValidatorModel):
    Blueprints: List[BlueprintTypeDef]
    MissingBlueprints: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetBlueprintResponseTypeDef(BaseValidatorModel):
    Blueprint: BlueprintTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListConnectionTypesResponseTypeDef(BaseValidatorModel):
    ConnectionTypes: List[ConnectionTypeBriefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetClassifierResponseTypeDef(BaseValidatorModel):
    Classifier: ClassifierTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetClassifiersResponseTypeDef(BaseValidatorModel):
    Classifiers: List[ClassifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetDataflowGraphResponseTypeDef(BaseValidatorModel):
    DagNodes: List[CodeGenNodeOutputTypeDef]
    DagEdges: List[CodeGenEdgeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetMappingRequestTypeDef(BaseValidatorModel):
    Source: CatalogEntryTypeDef
    Sinks: Optional[Sequence[CatalogEntryTypeDef]] = None
    Location: Optional[LocationTypeDef] = None


class GetColumnStatisticsTaskSettingsResponseTypeDef(BaseValidatorModel):
    ColumnStatisticsTaskSettings: ColumnStatisticsTaskSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetUnfilteredPartitionMetadataRequestTypeDef(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    SupportedPermissionTypes: Sequence[PermissionTypeType]
    Region: Optional[str] = None
    AuditContext: Optional[AuditContextTypeDef] = None
    QuerySessionContext: Optional[QuerySessionContextTypeDef] = None


class GetUnfilteredPartitionsMetadataRequestTypeDef(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    SupportedPermissionTypes: Sequence[PermissionTypeType]
    Region: Optional[str] = None
    Expression: Optional[str] = None
    AuditContext: Optional[AuditContextTypeDef] = None
    NextToken: Optional[str] = None
    Segment: Optional[SegmentTypeDef] = None
    MaxResults: Optional[int] = None
    QuerySessionContext: Optional[QuerySessionContextTypeDef] = None


class GetUnfilteredTableMetadataRequestTypeDef(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    Name: str
    SupportedPermissionTypes: Sequence[PermissionTypeType]
    Region: Optional[str] = None
    AuditContext: Optional[AuditContextTypeDef] = None
    ParentResourceArn: Optional[str] = None
    RootResourceArn: Optional[str] = None
    SupportedDialect: Optional[SupportedDialectTypeDef] = None
    Permissions: Optional[Sequence[PermissionType]] = None
    QuerySessionContext: Optional[QuerySessionContextTypeDef] = None


class GetMLTaskRunsRequestTypeDef(BaseValidatorModel):
    TransformId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[TaskRunFilterCriteriaTypeDef] = None
    Sort: Optional[TaskRunSortCriteriaTypeDef] = None


class ListDataQualityStatisticAnnotationsRequestTypeDef(BaseValidatorModel):
    StatisticId: Optional[str] = None
    ProfileId: Optional[str] = None
    TimestampFilter: Optional[TimestampFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListDataQualityStatisticsRequestTypeDef(BaseValidatorModel):
    StatisticId: Optional[str] = None
    ProfileId: Optional[str] = None
    TimestampFilter: Optional[TimestampFilterTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class GetUsageProfileResponseTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    Configuration: ProfileConfigurationOutputTypeDef
    CreatedOn: datetime
    LastModifiedOn: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class EvaluationMetricsTypeDef(BaseValidatorModel):
    TransformType: Literal["FIND_MATCHES"]
    FindMatchesMetrics: Optional[FindMatchesMetricsTypeDef] = None


class ConnectionsListUnionTypeDef(BaseValidatorModel):
    pass


class CreateSessionRequestTypeDef(BaseValidatorModel):
    Id: str
    Role: str
    Command: SessionCommandTypeDef
    Description: Optional[str] = None
    Timeout: Optional[int] = None
    IdleTimeout: Optional[int] = None
    DefaultArguments: Optional[Mapping[str, str]] = None
    Connections: Optional[ConnectionsListUnionTypeDef] = None
    MaxCapacity: Optional[float] = None
    NumberOfWorkers: Optional[int] = None
    WorkerType: Optional[WorkerTypeType] = None
    SecurityConfiguration: Optional[str] = None
    GlueVersion: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    RequestOrigin: Optional[str] = None


class CrawlerTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Role: Optional[str] = None
    Targets: Optional[CrawlerTargetsOutputTypeDef] = None
    DatabaseName: Optional[str] = None
    Description: Optional[str] = None
    Classifiers: Optional[List[str]] = None
    RecrawlPolicy: Optional[RecrawlPolicyTypeDef] = None
    SchemaChangePolicy: Optional[SchemaChangePolicyTypeDef] = None
    LineageConfiguration: Optional[LineageConfigurationTypeDef] = None
    State: Optional[CrawlerStateType] = None
    TablePrefix: Optional[str] = None
    Schedule: Optional[ScheduleTypeDef] = None
    CrawlElapsedTime: Optional[int] = None
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    LastCrawl: Optional[LastCrawlInfoTypeDef] = None
    Version: Optional[int] = None
    Configuration: Optional[str] = None
    CrawlerSecurityConfiguration: Optional[str] = None
    LakeFormationConfiguration: Optional[LakeFormationConfigurationTypeDef] = None


class ListDataQualityRulesetsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[DataQualityRulesetFilterCriteriaTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class ListDataQualityRulesetsResponseTypeDef(BaseValidatorModel):
    Rulesets: List[DataQualityRulesetListDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeInboundIntegrationsResponseTypeDef(BaseValidatorModel):
    InboundIntegrations: List[InboundIntegrationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeIntegrationsResponseTypeDef(BaseValidatorModel):
    Integrations: List[IntegrationTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSessionResponseTypeDef(BaseValidatorModel):
    Session: SessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSessionResponseTypeDef(BaseValidatorModel):
    Session: SessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListSessionsResponseTypeDef(BaseValidatorModel):
    Ids: List[str]
    Sessions: List[SessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetDataCatalogEncryptionSettingsResponseTypeDef(BaseValidatorModel):
    DataCatalogEncryptionSettings: DataCatalogEncryptionSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutDataCatalogEncryptionSettingsRequestTypeDef(BaseValidatorModel):
    DataCatalogEncryptionSettings: DataCatalogEncryptionSettingsTypeDef
    CatalogId: Optional[str] = None


class CatalogTypeDef(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None
    ResourceArn: Optional[str] = None
    Description: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None
    CreateTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None
    TargetRedshiftCatalog: Optional[TargetRedshiftCatalogTypeDef] = None
    FederatedCatalog: Optional[FederatedCatalogTypeDef] = None
    CatalogProperties: Optional[CatalogPropertiesOutputTypeDef] = None
    CreateTableDefaultPermissions: Optional[List[PrincipalPermissionsOutputTypeDef]] = None
    CreateDatabaseDefaultPermissions: Optional[List[PrincipalPermissionsOutputTypeDef]] = None


class DatabaseTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    LocationUri: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None
    CreateTime: Optional[datetime] = None
    CreateTableDefaultPermissions: Optional[List[PrincipalPermissionsOutputTypeDef]] = None
    TargetDatabase: Optional[DatabaseIdentifierTypeDef] = None
    CatalogId: Optional[str] = None
    FederatedDatabase: Optional[FederatedDatabaseTypeDef] = None


class DataQualityObservationTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    MetricBasedObservation: Optional[MetricBasedObservationTypeDef] = None


class DataQualityResultDescriptionTypeDef(BaseValidatorModel):
    ResultId: Optional[str] = None
    DataSource: Optional[DataSourceOutputTypeDef] = None
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None
    StartedOn: Optional[datetime] = None


class DataQualityRuleRecommendationRunDescriptionTypeDef(BaseValidatorModel):
    RunId: Optional[str] = None
    Status: Optional[TaskStatusTypeType] = None
    StartedOn: Optional[datetime] = None
    DataSource: Optional[DataSourceOutputTypeDef] = None


class DataQualityRulesetEvaluationRunDescriptionTypeDef(BaseValidatorModel):
    RunId: Optional[str] = None
    Status: Optional[TaskStatusTypeType] = None
    StartedOn: Optional[datetime] = None
    DataSource: Optional[DataSourceOutputTypeDef] = None


class GetDataQualityRuleRecommendationRunResponseTypeDef(BaseValidatorModel):
    RunId: str
    DataSource: DataSourceOutputTypeDef
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
    ResponseMetadata: ResponseMetadataTypeDef


class GetDataQualityRulesetEvaluationRunResponseTypeDef(BaseValidatorModel):
    RunId: str
    DataSource: DataSourceOutputTypeDef
    Role: str
    NumberOfWorkers: int
    Timeout: int
    AdditionalRunOptions: DataQualityEvaluationRunAdditionalRunOptionsTypeDef
    Status: TaskStatusTypeType
    ErrorString: str
    StartedOn: datetime
    LastModifiedOn: datetime
    CompletedOn: datetime
    ExecutionTime: int
    RulesetNames: List[str]
    ResultIds: List[str]
    AdditionalDataSources: Dict[str, DataSourceOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DropNullFieldsOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    NullCheckBoxList: Optional[NullCheckBoxListTypeDef] = None
    NullTextList: Optional[List[NullValueFieldTypeDef]] = None


class DropNullFieldsTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    NullCheckBoxList: Optional[NullCheckBoxListTypeDef] = None
    NullTextList: Optional[Sequence[NullValueFieldTypeDef]] = None


class ColumnOutputTypeDef(BaseValidatorModel):
    pass


class StorageDescriptorOutputTypeDef(BaseValidatorModel):
    Columns: Optional[List[ColumnOutputTypeDef]] = None
    Location: Optional[str] = None
    AdditionalLocations: Optional[List[str]] = None
    InputFormat: Optional[str] = None
    OutputFormat: Optional[str] = None
    Compressed: Optional[bool] = None
    NumberOfBuckets: Optional[int] = None
    SerdeInfo: Optional[SerDeInfoOutputTypeDef] = None
    BucketColumns: Optional[List[str]] = None
    SortColumns: Optional[List[OrderTypeDef]] = None
    Parameters: Optional[Dict[str, str]] = None
    SkewedInfo: Optional[SkewedInfoOutputTypeDef] = None
    StoredAsSubDirectories: Optional[bool] = None
    SchemaReference: Optional[SchemaReferenceTypeDef] = None


class SecurityConfigurationTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    CreatedTimeStamp: Optional[datetime] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationOutputTypeDef] = None


class DeleteSchemaVersionsResponseTypeDef(BaseValidatorModel):
    SchemaVersionErrors: List[SchemaVersionErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class FilterOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    LogicalOperator: FilterLogicalOperatorType
    Filters: List[FilterExpressionOutputTypeDef]


class FilterValueUnionTypeDef(BaseValidatorModel):
    pass


class FilterExpressionTypeDef(BaseValidatorModel):
    Operation: FilterOperationType
    Values: Sequence[FilterValueUnionTypeDef]
    Negated: Optional[bool] = None


class UpdateMLTransformRequestTypeDef(BaseValidatorModel):
    TransformId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Parameters: Optional[TransformParametersTypeDef] = None
    Role: Optional[str] = None
    GlueVersion: Optional[str] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    MaxRetries: Optional[int] = None


class GetMLTransformsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[TransformFilterCriteriaTypeDef] = None
    Sort: Optional[TransformSortCriteriaTypeDef] = None


class ListMLTransformsRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[TransformFilterCriteriaTypeDef] = None
    Sort: Optional[TransformSortCriteriaTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class AthenaConnectorSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    SchemaName: str
    ConnectionTable: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class CatalogDeltaSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class CatalogHudiSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class ConnectorDataSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    ConnectionType: str
    Data: Dict[str, str]
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class CustomCodeOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Code: str
    ClassName: str
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class TransformConfigParameterOutputTypeDef(BaseValidatorModel):
    pass


class DynamicTransformOutputTypeDef(BaseValidatorModel):
    Name: str
    TransformName: str
    Inputs: List[str]
    FunctionName: str
    Path: str
    Parameters: Optional[List[TransformConfigParameterOutputTypeDef]] = None
    Version: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class JDBCConnectorSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[JDBCConnectorOptionsOutputTypeDef] = None
    ConnectionTable: Optional[str] = None
    Query: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class JDBCConnectorTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    ConnectionName: str
    ConnectionTable: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class S3CatalogDeltaSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class S3CatalogHudiSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class S3CsvSourceOutputTypeDef(BaseValidatorModel):
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
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    Escaper: Optional[str] = None
    Multiline: Optional[bool] = None
    WithHeader: Optional[bool] = None
    WriteHeader: Optional[bool] = None
    SkipFirst: Optional[bool] = None
    OptimizePerformance: Optional[bool] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class S3DeltaSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    Paths: List[str]
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class S3HudiSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    Paths: List[str]
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class S3JsonSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    Paths: List[str]
    CompressionType: Optional[CompressionTypeType] = None
    Exclusions: Optional[List[str]] = None
    GroupSize: Optional[str] = None
    GroupFiles: Optional[str] = None
    Recurse: Optional[bool] = None
    MaxBand: Optional[int] = None
    MaxFilesInBand: Optional[int] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    JsonPath: Optional[str] = None
    Multiline: Optional[bool] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class S3ParquetSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    Paths: List[str]
    CompressionType: Optional[ParquetCompressionTypeType] = None
    Exclusions: Optional[List[str]] = None
    GroupSize: Optional[str] = None
    GroupFiles: Optional[str] = None
    Recurse: Optional[bool] = None
    MaxBand: Optional[int] = None
    MaxFilesInBand: Optional[int] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class SnowflakeSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    Data: SnowflakeNodeDataOutputTypeDef
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class SparkConnectorSourceOutputTypeDef(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class SparkConnectorTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class SparkSQLOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    SqlQuery: str
    SqlAliases: List[SqlAliasTypeDef]
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None


class AthenaConnectorSourceTypeDef(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    SchemaName: str
    ConnectionTable: Optional[str] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class CatalogDeltaSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class CatalogHudiSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class CustomCodeTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Code: str
    ClassName: str
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class JDBCConnectorTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    ConnectionName: str
    ConnectionTable: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class S3CatalogDeltaSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class S3CatalogHudiSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class S3CsvSourceTypeDef(BaseValidatorModel):
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
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    Escaper: Optional[str] = None
    Multiline: Optional[bool] = None
    WithHeader: Optional[bool] = None
    WriteHeader: Optional[bool] = None
    SkipFirst: Optional[bool] = None
    OptimizePerformance: Optional[bool] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class S3DeltaSourceTypeDef(BaseValidatorModel):
    Name: str
    Paths: Sequence[str]
    AdditionalDeltaOptions: Optional[Mapping[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class S3HudiSourceTypeDef(BaseValidatorModel):
    Name: str
    Paths: Sequence[str]
    AdditionalHudiOptions: Optional[Mapping[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class S3JsonSourceTypeDef(BaseValidatorModel):
    Name: str
    Paths: Sequence[str]
    CompressionType: Optional[CompressionTypeType] = None
    Exclusions: Optional[Sequence[str]] = None
    GroupSize: Optional[str] = None
    GroupFiles: Optional[str] = None
    Recurse: Optional[bool] = None
    MaxBand: Optional[int] = None
    MaxFilesInBand: Optional[int] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    JsonPath: Optional[str] = None
    Multiline: Optional[bool] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class S3ParquetSourceTypeDef(BaseValidatorModel):
    Name: str
    Paths: Sequence[str]
    CompressionType: Optional[ParquetCompressionTypeType] = None
    Exclusions: Optional[Sequence[str]] = None
    GroupSize: Optional[str] = None
    GroupFiles: Optional[str] = None
    Recurse: Optional[bool] = None
    MaxBand: Optional[int] = None
    MaxFilesInBand: Optional[int] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class SparkConnectorSourceTypeDef(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class SparkConnectorTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class SparkSQLTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    SqlQuery: str
    SqlAliases: Sequence[SqlAliasTypeDef]
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class GlueTableUnionTypeDef(BaseValidatorModel):
    pass


class DataSourceTypeDef(BaseValidatorModel):
    GlueTable: GlueTableUnionTypeDef


class TableOptimizerConfigurationTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None
    enabled: Optional[bool] = None
    vpcConfiguration: Optional[TableOptimizerVpcConfigurationTypeDef] = None
    retentionConfiguration: Optional[RetentionConfigurationTypeDef] = None
    orphanFileDeletionConfiguration: Optional[OrphanFileDeletionConfigurationTypeDef] = None


class TableOptimizerRunTypeDef(BaseValidatorModel):
    eventType: Optional[TableOptimizerEventTypeType] = None
    startTimestamp: Optional[datetime] = None
    endTimestamp: Optional[datetime] = None
    metrics: Optional[RunMetricsTypeDef] = None
    error: Optional[str] = None
    compactionMetrics: Optional[CompactionMetricsTypeDef] = None
    retentionMetrics: Optional[RetentionMetricsTypeDef] = None
    orphanFileDeletionMetrics: Optional[OrphanFileDeletionMetricsTypeDef] = None


class GetIntegrationTablePropertiesResponseTypeDef(BaseValidatorModel):
    ResourceArn: str
    TableName: str
    SourceTableConfig: SourceTableConfigOutputTypeDef
    TargetTableConfig: TargetTableConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class JDBCConnectorOptionsUnionTypeDef(BaseValidatorModel):
    pass


class JDBCConnectorSourceTypeDef(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[JDBCConnectorOptionsUnionTypeDef] = None
    ConnectionTable: Optional[str] = None
    Query: Optional[str] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class GetJobRunResponseTypeDef(BaseValidatorModel):
    JobRun: JobRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetJobRunsResponseTypeDef(BaseValidatorModel):
    JobRuns: List[JobRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class JobNodeDetailsTypeDef(BaseValidatorModel):
    JobRuns: Optional[List[JobRunTypeDef]] = None


class JoinColumnUnionTypeDef(BaseValidatorModel):
    pass


class JoinTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    JoinType: JoinTypeType
    Columns: Sequence[JoinColumnUnionTypeDef]


class GetMLTaskRunResponseTypeDef(BaseValidatorModel):
    TransformId: str
    TaskRunId: str
    Status: TaskStatusTypeType
    LogGroupName: str
    Properties: TaskRunPropertiesTypeDef
    ErrorString: str
    StartedOn: datetime
    LastModifiedOn: datetime
    CompletedOn: datetime
    ExecutionTime: int
    ResponseMetadata: ResponseMetadataTypeDef


class TaskRunTypeDef(BaseValidatorModel):
    TransformId: Optional[str] = None
    TaskRunId: Optional[str] = None
    Status: Optional[TaskStatusTypeType] = None
    LogGroupName: Optional[str] = None
    Properties: Optional[TaskRunPropertiesTypeDef] = None
    ErrorString: Optional[str] = None
    StartedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    CompletedOn: Optional[datetime] = None
    ExecutionTime: Optional[int] = None


class CreateMLTransformRequestTypeDef(BaseValidatorModel):
    Name: str
    InputRecordTables: Sequence[GlueTableUnionTypeDef]
    Parameters: TransformParametersTypeDef
    Role: str
    Description: Optional[str] = None
    GlueVersion: Optional[str] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    MaxRetries: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None
    TransformEncryption: Optional[TransformEncryptionTypeDef] = None


class QuerySchemaVersionMetadataResponseTypeDef(BaseValidatorModel):
    MetadataInfoMap: Dict[str, MetadataInfoTypeDef]
    SchemaVersionId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AuthenticationConfigurationTypeDef(BaseValidatorModel):
    AuthenticationType: Optional[AuthenticationTypeType] = None
    SecretArn: Optional[str] = None
    OAuth2Properties: Optional[OAuth2PropertiesTypeDef] = None


class AuthenticationConfigurationInputTypeDef(BaseValidatorModel):
    AuthenticationType: Optional[AuthenticationTypeType] = None
    OAuth2Properties: Optional[OAuth2PropertiesInputTypeDef] = None
    SecretArn: Optional[str] = None
    KmsKeyArn: Optional[str] = None
    BasicAuthenticationCredentials: Optional[BasicAuthenticationCredentialsTypeDef] = None
    CustomAuthenticationCredentials: Optional[Mapping[str, str]] = None


class PartitionValueListUnionTypeDef(BaseValidatorModel):
    pass


class BatchDeletePartitionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionsToDelete: Sequence[PartitionValueListUnionTypeDef]
    CatalogId: Optional[str] = None


class BatchGetPartitionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionsToGet: Sequence[PartitionValueListUnionTypeDef]
    CatalogId: Optional[str] = None


class RecipeOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    RecipeSteps: Optional[List[RecipeStepOutputTypeDef]] = None


class RecipeActionUnionTypeDef(BaseValidatorModel):
    pass


class RecipeStepTypeDef(BaseValidatorModel):
    Action: RecipeActionUnionTypeDef
    ConditionExpressions: Optional[Sequence[ConditionExpressionTypeDef]] = None


class CreateUserDefinedFunctionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    FunctionInput: UserDefinedFunctionInputTypeDef
    CatalogId: Optional[str] = None


class UpdateUserDefinedFunctionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    FunctionName: str
    FunctionInput: UserDefinedFunctionInputTypeDef
    CatalogId: Optional[str] = None


class GetUserDefinedFunctionResponseTypeDef(BaseValidatorModel):
    UserDefinedFunction: UserDefinedFunctionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetUserDefinedFunctionsResponseTypeDef(BaseValidatorModel):
    UserDefinedFunctions: List[UserDefinedFunctionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ColumnUnionTypeDef(BaseValidatorModel):
    pass


class SerDeInfoUnionTypeDef(BaseValidatorModel):
    pass


class SkewedInfoUnionTypeDef(BaseValidatorModel):
    pass


class StorageDescriptorTypeDef(BaseValidatorModel):
    Columns: Optional[Sequence[ColumnUnionTypeDef]] = None
    Location: Optional[str] = None
    AdditionalLocations: Optional[Sequence[str]] = None
    InputFormat: Optional[str] = None
    OutputFormat: Optional[str] = None
    Compressed: Optional[bool] = None
    NumberOfBuckets: Optional[int] = None
    SerdeInfo: Optional[SerDeInfoUnionTypeDef] = None
    BucketColumns: Optional[Sequence[str]] = None
    SortColumns: Optional[Sequence[OrderTypeDef]] = None
    Parameters: Optional[Mapping[str, str]] = None
    SkewedInfo: Optional[SkewedInfoUnionTypeDef] = None
    StoredAsSubDirectories: Optional[bool] = None
    SchemaReference: Optional[SchemaReferenceTypeDef] = None


class StatementTypeDef(BaseValidatorModel):
    Id: Optional[int] = None
    Code: Optional[str] = None
    State: Optional[StatementStateType] = None
    Output: Optional[StatementOutputTypeDef] = None
    Progress: Optional[float] = None
    StartedOn: Optional[int] = None
    CompletedOn: Optional[int] = None


class ListDataQualityStatisticAnnotationsResponseTypeDef(BaseValidatorModel):
    Annotations: List[StatisticAnnotationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDataQualityStatisticsResponseTypeDef(BaseValidatorModel):
    Statistics: List[StatisticSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TransformConfigParameterUnionTypeDef(BaseValidatorModel):
    pass


class DynamicTransformTypeDef(BaseValidatorModel):
    Name: str
    TransformName: str
    Inputs: Sequence[str]
    FunctionName: str
    Path: str
    Parameters: Optional[Sequence[TransformConfigParameterUnionTypeDef]] = None
    Version: Optional[str] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None


class UpsertRedshiftTargetOptionsUnionTypeDef(BaseValidatorModel):
    pass


class RedshiftTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str
    RedshiftTmpDir: Optional[str] = None
    TmpDirIAMRole: Optional[str] = None
    UpsertRedshiftOptions: Optional[UpsertRedshiftTargetOptionsUnionTypeDef] = None


class DescribeConnectionTypeResponseTypeDef(BaseValidatorModel):
    ConnectionType: str
    Description: str
    Capabilities: CapabilitiesTypeDef
    ConnectionProperties: Dict[str, PropertyTypeDef]
    ConnectionOptions: Dict[str, PropertyTypeDef]
    AuthenticationConfiguration: AuthConfigurationTypeDef
    ComputeEnvironmentConfigurations: Dict[str, ComputeEnvironmentConfigurationTypeDef]
    PhysicalConnectionRequirements: Dict[str, PropertyTypeDef]
    AthenaConnectionProperties: Dict[str, PropertyTypeDef]
    PythonConnectionProperties: Dict[str, PropertyTypeDef]
    SparkConnectionProperties: Dict[str, PropertyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AmazonRedshiftNodeDataUnionTypeDef(BaseValidatorModel):
    pass


class AmazonRedshiftSourceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataUnionTypeDef] = None


class AmazonRedshiftTargetTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataUnionTypeDef] = None
    Inputs: Optional[Sequence[str]] = None


class SnowflakeNodeDataUnionTypeDef(BaseValidatorModel):
    pass


class SnowflakeTargetTypeDef(BaseValidatorModel):
    Name: str
    Data: SnowflakeNodeDataUnionTypeDef
    Inputs: Optional[Sequence[str]] = None


class GetPartitionIndexesResponseTypeDef(BaseValidatorModel):
    PartitionIndexDescriptorList: List[PartitionIndexDescriptorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TableStatusPaginatorTypeDef(BaseValidatorModel):
    RequestedBy: Optional[str] = None
    UpdatedBy: Optional[str] = None
    RequestTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None
    Action: Optional[ResourceActionType] = None
    State: Optional[ResourceStateType] = None
    Error: Optional[ErrorDetailTypeDef] = None
    Details: Optional[StatusDetailsPaginatorTypeDef] = None


class TableStatusTypeDef(BaseValidatorModel):
    RequestedBy: Optional[str] = None
    UpdatedBy: Optional[str] = None
    RequestTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None
    Action: Optional[ResourceActionType] = None
    State: Optional[ResourceStateType] = None
    Error: Optional[ErrorDetailTypeDef] = None
    Details: Optional[StatusDetailsTypeDef] = None


class DecimalNumberUnionTypeDef(BaseValidatorModel):
    pass


class DecimalColumnStatisticsDataTypeDef(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[DecimalNumberUnionTypeDef] = None
    MaximumValue: Optional[DecimalNumberUnionTypeDef] = None


class CodeGenNodeUnionTypeDef(BaseValidatorModel):
    pass


class CreateScriptRequestTypeDef(BaseValidatorModel):
    DagNodes: Optional[Sequence[CodeGenNodeUnionTypeDef]] = None
    DagEdges: Optional[Sequence[CodeGenEdgeTypeDef]] = None
    Language: Optional[LanguageType] = None


class KafkaStreamingSourceOptionsUnionTypeDef(BaseValidatorModel):
    pass


class CatalogKafkaSourceTypeDef(BaseValidatorModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KafkaStreamingSourceOptionsUnionTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None


class DirectKafkaSourceTypeDef(BaseValidatorModel):
    Name: str
    StreamingOptions: Optional[KafkaStreamingSourceOptionsUnionTypeDef] = None
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None


class KinesisStreamingSourceOptionsUnionTypeDef(BaseValidatorModel):
    pass


class CatalogKinesisSourceTypeDef(BaseValidatorModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsUnionTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None


class DirectKinesisSourceTypeDef(BaseValidatorModel):
    Name: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsUnionTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None


class TriggerTypeDef(BaseValidatorModel):
    pass


class BatchGetTriggersResponseTypeDef(BaseValidatorModel):
    Triggers: List[TriggerTypeDef]
    TriggersNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetTriggerResponseTypeDef(BaseValidatorModel):
    Trigger: TriggerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetTriggersResponseTypeDef(BaseValidatorModel):
    Triggers: List[TriggerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TriggerNodeDetailsTypeDef(BaseValidatorModel):
    Trigger: Optional[TriggerTypeDef] = None


class UpdateTriggerResponseTypeDef(BaseValidatorModel):
    Trigger: TriggerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PredicateUnionTypeDef(BaseValidatorModel):
    pass


class ActionUnionTypeDef(BaseValidatorModel):
    pass


class TriggerUpdateTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Schedule: Optional[str] = None
    Actions: Optional[Sequence[ActionUnionTypeDef]] = None
    Predicate: Optional[PredicateUnionTypeDef] = None
    EventBatchingCondition: Optional[EventBatchingConditionTypeDef] = None


class ProfileConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateUsageProfileRequestTypeDef(BaseValidatorModel):
    Name: str
    Configuration: ProfileConfigurationUnionTypeDef
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateUsageProfileRequestTypeDef(BaseValidatorModel):
    Name: str
    Configuration: ProfileConfigurationUnionTypeDef
    Description: Optional[str] = None


class GetMLTransformResponseTypeDef(BaseValidatorModel):
    TransformId: str
    Name: str
    Description: str
    Status: TransformStatusTypeType
    CreatedOn: datetime
    LastModifiedOn: datetime
    InputRecordTables: List[GlueTableOutputTypeDef]
    Parameters: TransformParametersTypeDef
    EvaluationMetrics: EvaluationMetricsTypeDef
    LabelCount: int
    Schema: List[SchemaColumnTypeDef]
    Role: str
    GlueVersion: str
    MaxCapacity: float
    WorkerType: WorkerTypeType
    NumberOfWorkers: int
    Timeout: int
    MaxRetries: int
    TransformEncryption: TransformEncryptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class MLTransformTypeDef(BaseValidatorModel):
    TransformId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[TransformStatusTypeType] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    InputRecordTables: Optional[List[GlueTableOutputTypeDef]] = None
    Parameters: Optional[TransformParametersTypeDef] = None
    EvaluationMetrics: Optional[EvaluationMetricsTypeDef] = None
    LabelCount: Optional[int] = None
    Schema: Optional[List[SchemaColumnTypeDef]] = None
    Role: Optional[str] = None
    GlueVersion: Optional[str] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    MaxRetries: Optional[int] = None
    TransformEncryption: Optional[TransformEncryptionTypeDef] = None


class BatchGetCrawlersResponseTypeDef(BaseValidatorModel):
    Crawlers: List[CrawlerTypeDef]
    CrawlersNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetCrawlerResponseTypeDef(BaseValidatorModel):
    Crawler: CrawlerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCrawlersResponseTypeDef(BaseValidatorModel):
    Crawlers: List[CrawlerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CrawlerTargetsUnionTypeDef(BaseValidatorModel):
    pass


class CreateCrawlerRequestTypeDef(BaseValidatorModel):
    Name: str
    Role: str
    Targets: CrawlerTargetsUnionTypeDef
    DatabaseName: Optional[str] = None
    Description: Optional[str] = None
    Schedule: Optional[str] = None
    Classifiers: Optional[Sequence[str]] = None
    TablePrefix: Optional[str] = None
    SchemaChangePolicy: Optional[SchemaChangePolicyTypeDef] = None
    RecrawlPolicy: Optional[RecrawlPolicyTypeDef] = None
    LineageConfiguration: Optional[LineageConfigurationTypeDef] = None
    LakeFormationConfiguration: Optional[LakeFormationConfigurationTypeDef] = None
    Configuration: Optional[str] = None
    CrawlerSecurityConfiguration: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateCrawlerRequestTypeDef(BaseValidatorModel):
    Name: str
    Role: Optional[str] = None
    DatabaseName: Optional[str] = None
    Description: Optional[str] = None
    Targets: Optional[CrawlerTargetsUnionTypeDef] = None
    Schedule: Optional[str] = None
    Classifiers: Optional[Sequence[str]] = None
    TablePrefix: Optional[str] = None
    SchemaChangePolicy: Optional[SchemaChangePolicyTypeDef] = None
    RecrawlPolicy: Optional[RecrawlPolicyTypeDef] = None
    LineageConfiguration: Optional[LineageConfigurationTypeDef] = None
    LakeFormationConfiguration: Optional[LakeFormationConfigurationTypeDef] = None
    Configuration: Optional[str] = None
    CrawlerSecurityConfiguration: Optional[str] = None


class GetCatalogResponseTypeDef(BaseValidatorModel):
    Catalog: CatalogTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetCatalogsResponseTypeDef(BaseValidatorModel):
    CatalogList: List[CatalogTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetDatabaseResponseTypeDef(BaseValidatorModel):
    Database: DatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetDatabasesResponseTypeDef(BaseValidatorModel):
    DatabaseList: List[DatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PrincipalPermissionsUnionTypeDef(BaseValidatorModel):
    pass


class CatalogInputTypeDef(BaseValidatorModel):
    Description: Optional[str] = None
    FederatedCatalog: Optional[FederatedCatalogTypeDef] = None
    Parameters: Optional[Mapping[str, str]] = None
    TargetRedshiftCatalog: Optional[TargetRedshiftCatalogTypeDef] = None
    CatalogProperties: Optional[CatalogPropertiesTypeDef] = None
    CreateTableDefaultPermissions: Optional[Sequence[PrincipalPermissionsUnionTypeDef]] = None
    CreateDatabaseDefaultPermissions: Optional[Sequence[PrincipalPermissionsUnionTypeDef]] = None


class DatabaseInputTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    LocationUri: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    CreateTableDefaultPermissions: Optional[Sequence[PrincipalPermissionsUnionTypeDef]] = None
    TargetDatabase: Optional[DatabaseIdentifierTypeDef] = None
    FederatedDatabase: Optional[FederatedDatabaseTypeDef] = None


class DataQualityResultTypeDef(BaseValidatorModel):
    ResultId: Optional[str] = None
    ProfileId: Optional[str] = None
    Score: Optional[float] = None
    DataSource: Optional[DataSourceOutputTypeDef] = None
    RulesetName: Optional[str] = None
    EvaluationContext: Optional[str] = None
    StartedOn: Optional[datetime] = None
    CompletedOn: Optional[datetime] = None
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None
    RulesetEvaluationRunId: Optional[str] = None
    RuleResults: Optional[List[DataQualityRuleResultTypeDef]] = None
    AnalyzerResults: Optional[List[DataQualityAnalyzerResultTypeDef]] = None
    Observations: Optional[List[DataQualityObservationTypeDef]] = None


class GetDataQualityResultResponseTypeDef(BaseValidatorModel):
    ResultId: str
    ProfileId: str
    Score: float
    DataSource: DataSourceOutputTypeDef
    RulesetName: str
    EvaluationContext: str
    StartedOn: datetime
    CompletedOn: datetime
    JobName: str
    JobRunId: str
    RulesetEvaluationRunId: str
    RuleResults: List[DataQualityRuleResultTypeDef]
    AnalyzerResults: List[DataQualityAnalyzerResultTypeDef]
    Observations: List[DataQualityObservationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListDataQualityResultsResponseTypeDef(BaseValidatorModel):
    Results: List[DataQualityResultDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDataQualityRuleRecommendationRunsResponseTypeDef(BaseValidatorModel):
    Runs: List[DataQualityRuleRecommendationRunDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDataQualityRulesetEvaluationRunsResponseTypeDef(BaseValidatorModel):
    Runs: List[DataQualityRulesetEvaluationRunDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ColumnStatisticsDataOutputTypeDef(BaseValidatorModel):
    pass


class ColumnStatisticsOutputTypeDef(BaseValidatorModel):
    ColumnName: str
    ColumnType: str
    AnalyzedTime: datetime
    StatisticsData: ColumnStatisticsDataOutputTypeDef


class PartitionTypeDef(BaseValidatorModel):
    Values: Optional[List[str]] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastAccessTime: Optional[datetime] = None
    StorageDescriptor: Optional[StorageDescriptorOutputTypeDef] = None
    Parameters: Optional[Dict[str, str]] = None
    LastAnalyzedTime: Optional[datetime] = None
    CatalogId: Optional[str] = None


class GetSecurityConfigurationResponseTypeDef(BaseValidatorModel):
    SecurityConfiguration: SecurityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSecurityConfigurationsResponseTypeDef(BaseValidatorModel):
    SecurityConfigurations: List[SecurityConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class EncryptionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateSecurityConfigurationRequestTypeDef(BaseValidatorModel):
    Name: str
    EncryptionConfiguration: EncryptionConfigurationUnionTypeDef


class GlueSchemaUnionTypeDef(BaseValidatorModel):
    pass


class ConnectorDataSourceTypeDef(BaseValidatorModel):
    Name: str
    ConnectionType: str
    Data: Mapping[str, str]
    OutputSchemas: Optional[Sequence[GlueSchemaUnionTypeDef]] = None


class SnowflakeSourceTypeDef(BaseValidatorModel):
    Name: str
    Data: SnowflakeNodeDataUnionTypeDef
    OutputSchemas: Optional[Sequence[GlueSchemaUnionTypeDef]] = None


class ListTableOptimizerRunsResponseTypeDef(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    TableOptimizerRuns: List[TableOptimizerRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SourceTableConfigUnionTypeDef(BaseValidatorModel):
    pass


class TargetTableConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateIntegrationTablePropertiesRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TableName: str
    SourceTableConfig: Optional[SourceTableConfigUnionTypeDef] = None
    TargetTableConfig: Optional[TargetTableConfigUnionTypeDef] = None


class UpdateIntegrationTablePropertiesRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TableName: str
    SourceTableConfig: Optional[SourceTableConfigUnionTypeDef] = None
    TargetTableConfig: Optional[TargetTableConfigUnionTypeDef] = None


class GetMLTaskRunsResponseTypeDef(BaseValidatorModel):
    TaskRuns: List[TaskRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ConnectionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    ConnectionType: Optional[ConnectionTypeType] = None
    MatchCriteria: Optional[List[str]] = None
    ConnectionProperties: Optional[Dict[ConnectionPropertyKeyType, str]] = None
    SparkProperties: Optional[Dict[str, str]] = None
    AthenaProperties: Optional[Dict[str, str]] = None
    PythonProperties: Optional[Dict[str, str]] = None
    PhysicalConnectionRequirements: Optional[PhysicalConnectionRequirementsOutputTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    LastUpdatedBy: Optional[str] = None
    Status: Optional[ConnectionStatusType] = None
    StatusReason: Optional[str] = None
    LastConnectionValidationTime: Optional[datetime] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationTypeDef] = None
    ConnectionSchemaVersion: Optional[int] = None
    CompatibleComputeEnvironments: Optional[List[ComputeEnvironmentType]] = None


class PhysicalConnectionRequirementsUnionTypeDef(BaseValidatorModel):
    pass


class ConnectionInputTypeDef(BaseValidatorModel):
    Name: str
    ConnectionType: ConnectionTypeType
    ConnectionProperties: Mapping[ConnectionPropertyKeyType, str]
    Description: Optional[str] = None
    MatchCriteria: Optional[Sequence[str]] = None
    SparkProperties: Optional[Mapping[str, str]] = None
    AthenaProperties: Optional[Mapping[str, str]] = None
    PythonProperties: Optional[Mapping[str, str]] = None
    PhysicalConnectionRequirements: Optional[PhysicalConnectionRequirementsUnionTypeDef] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationInputTypeDef] = None
    ValidateCredentials: Optional[bool] = None
    ValidateForComputeEnvironments: Optional[Sequence[ComputeEnvironmentType]] = None


class TestConnectionInputTypeDef(BaseValidatorModel):
    ConnectionType: ConnectionTypeType
    ConnectionProperties: Mapping[ConnectionPropertyKeyType, str]
    AuthenticationConfiguration: Optional[AuthenticationConfigurationInputTypeDef] = None


class GetStatementResponseTypeDef(BaseValidatorModel):
    Statement: StatementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListStatementsResponseTypeDef(BaseValidatorModel):
    Statements: List[StatementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TablePaginatorTypeDef(BaseValidatorModel):
    Name: str
    DatabaseName: Optional[str] = None
    Description: Optional[str] = None
    Owner: Optional[str] = None
    CreateTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None
    LastAccessTime: Optional[datetime] = None
    LastAnalyzedTime: Optional[datetime] = None
    Retention: Optional[int] = None
    StorageDescriptor: Optional[StorageDescriptorOutputTypeDef] = None
    PartitionKeys: Optional[List[ColumnOutputTypeDef]] = None
    ViewOriginalText: Optional[str] = None
    ViewExpandedText: Optional[str] = None
    TableType: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None
    CreatedBy: Optional[str] = None
    IsRegisteredWithLakeFormation: Optional[bool] = None
    TargetTable: Optional[TableIdentifierTypeDef] = None
    CatalogId: Optional[str] = None
    VersionId: Optional[str] = None
    FederatedTable: Optional[FederatedTableTypeDef] = None
    ViewDefinition: Optional[ViewDefinitionTypeDef] = None
    IsMultiDialectView: Optional[bool] = None
    Status: Optional[TableStatusPaginatorTypeDef] = None


class TableTypeDef(BaseValidatorModel):
    Name: str
    DatabaseName: Optional[str] = None
    Description: Optional[str] = None
    Owner: Optional[str] = None
    CreateTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None
    LastAccessTime: Optional[datetime] = None
    LastAnalyzedTime: Optional[datetime] = None
    Retention: Optional[int] = None
    StorageDescriptor: Optional[StorageDescriptorOutputTypeDef] = None
    PartitionKeys: Optional[List[ColumnOutputTypeDef]] = None
    ViewOriginalText: Optional[str] = None
    ViewExpandedText: Optional[str] = None
    TableType: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None
    CreatedBy: Optional[str] = None
    IsRegisteredWithLakeFormation: Optional[bool] = None
    TargetTable: Optional[TableIdentifierTypeDef] = None
    CatalogId: Optional[str] = None
    VersionId: Optional[str] = None
    FederatedTable: Optional[FederatedTableTypeDef] = None
    ViewDefinition: Optional[ViewDefinitionTypeDef] = None
    IsMultiDialectView: Optional[bool] = None
    Status: Optional[TableStatusTypeDef] = None


class UpdateTriggerRequestTypeDef(BaseValidatorModel):
    Name: str
    TriggerUpdate: TriggerUpdateTypeDef


class GetMLTransformsResponseTypeDef(BaseValidatorModel):
    Transforms: List[MLTransformTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateCatalogRequestTypeDef(BaseValidatorModel):
    Name: str
    CatalogInput: CatalogInputTypeDef
    Tags: Optional[Mapping[str, str]] = None


class UpdateCatalogRequestTypeDef(BaseValidatorModel):
    CatalogId: str
    CatalogInput: CatalogInputTypeDef


class CreateDatabaseRequestTypeDef(BaseValidatorModel):
    DatabaseInput: DatabaseInputTypeDef
    CatalogId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateDatabaseRequestTypeDef(BaseValidatorModel):
    Name: str
    DatabaseInput: DatabaseInputTypeDef
    CatalogId: Optional[str] = None


class BatchGetDataQualityResultResponseTypeDef(BaseValidatorModel):
    Results: List[DataQualityResultTypeDef]
    ResultsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class ColumnStatisticsErrorTypeDef(BaseValidatorModel):
    ColumnStatistics: Optional[ColumnStatisticsOutputTypeDef] = None
    Error: Optional[ErrorDetailTypeDef] = None


class GetColumnStatisticsForPartitionResponseTypeDef(BaseValidatorModel):
    ColumnStatisticsList: List[ColumnStatisticsOutputTypeDef]
    Errors: List[ColumnErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetColumnStatisticsForTableResponseTypeDef(BaseValidatorModel):
    ColumnStatisticsList: List[ColumnStatisticsOutputTypeDef]
    Errors: List[ColumnErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetPartitionResponseTypeDef(BaseValidatorModel):
    Partitions: List[PartitionTypeDef]
    UnprocessedKeys: List[PartitionValueListOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetPartitionResponseTypeDef(BaseValidatorModel):
    Partition: PartitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPartitionsResponseTypeDef(BaseValidatorModel):
    Partitions: List[PartitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetUnfilteredPartitionMetadataResponseTypeDef(BaseValidatorModel):
    Partition: PartitionTypeDef
    AuthorizedColumns: List[str]
    IsRegisteredWithLakeFormation: bool
    ResponseMetadata: ResponseMetadataTypeDef


class UnfilteredPartitionTypeDef(BaseValidatorModel):
    Partition: Optional[PartitionTypeDef] = None
    AuthorizedColumns: Optional[List[str]] = None
    IsRegisteredWithLakeFormation: Optional[bool] = None


class FilterExpressionUnionTypeDef(BaseValidatorModel):
    pass


class FilterTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    LogicalOperator: FilterLogicalOperatorType
    Filters: Sequence[FilterExpressionUnionTypeDef]


class DataSourceUnionTypeDef(BaseValidatorModel):
    pass


class DataQualityResultFilterCriteriaTypeDef(BaseValidatorModel):
    DataSource: Optional[DataSourceUnionTypeDef] = None
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None
    StartedAfter: Optional[TimestampTypeDef] = None
    StartedBefore: Optional[TimestampTypeDef] = None


class DataQualityRuleRecommendationRunFilterTypeDef(BaseValidatorModel):
    DataSource: DataSourceUnionTypeDef
    StartedBefore: Optional[TimestampTypeDef] = None
    StartedAfter: Optional[TimestampTypeDef] = None


class DataQualityRulesetEvaluationRunFilterTypeDef(BaseValidatorModel):
    DataSource: DataSourceUnionTypeDef
    StartedBefore: Optional[TimestampTypeDef] = None
    StartedAfter: Optional[TimestampTypeDef] = None


class StartDataQualityRuleRecommendationRunRequestTypeDef(BaseValidatorModel):
    DataSource: DataSourceUnionTypeDef
    Role: str
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    CreatedRulesetName: Optional[str] = None
    DataQualitySecurityConfiguration: Optional[str] = None
    ClientToken: Optional[str] = None


class StartDataQualityRulesetEvaluationRunRequestTypeDef(BaseValidatorModel):
    DataSource: DataSourceUnionTypeDef
    Role: str
    RulesetNames: Sequence[str]
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    ClientToken: Optional[str] = None
    AdditionalRunOptions: Optional[DataQualityEvaluationRunAdditionalRunOptionsTypeDef] = None
    AdditionalDataSources: Optional[Mapping[str, DataSourceUnionTypeDef]] = None


class TableOptimizerTypeDef(BaseValidatorModel):
    pass


class BatchTableOptimizerTypeDef(BaseValidatorModel):
    catalogId: Optional[str] = None
    databaseName: Optional[str] = None
    tableName: Optional[str] = None
    tableOptimizer: Optional[TableOptimizerTypeDef] = None


class GetTableOptimizerResponseTypeDef(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    TableOptimizer: TableOptimizerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetConnectionResponseTypeDef(BaseValidatorModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetConnectionsResponseTypeDef(BaseValidatorModel):
    ConnectionList: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateConnectionRequestTypeDef(BaseValidatorModel):
    ConnectionInput: ConnectionInputTypeDef
    CatalogId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateConnectionRequestTypeDef(BaseValidatorModel):
    Name: str
    ConnectionInput: ConnectionInputTypeDef
    CatalogId: Optional[str] = None


class TestConnectionRequestTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    CatalogId: Optional[str] = None
    TestConnectionInput: Optional[TestConnectionInputTypeDef] = None


class CodeGenConfigurationNodeOutputTypeDef(BaseValidatorModel):
    pass


class JobTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    JobMode: Optional[JobModeType] = None
    JobRunQueuingEnabled: Optional[bool] = None
    Description: Optional[str] = None
    LogUri: Optional[str] = None
    Role: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    ExecutionProperty: Optional[ExecutionPropertyTypeDef] = None
    Command: Optional[JobCommandTypeDef] = None
    DefaultArguments: Optional[Dict[str, str]] = None
    NonOverridableArguments: Optional[Dict[str, str]] = None
    Connections: Optional[ConnectionsListOutputTypeDef] = None
    MaxRetries: Optional[int] = None
    AllocatedCapacity: Optional[int] = None
    Timeout: Optional[int] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationPropertyTypeDef] = None
    GlueVersion: Optional[str] = None
    CodeGenConfigurationNodes: Optional[Dict[str, CodeGenConfigurationNodeOutputTypeDef]] = None
    ExecutionClass: Optional[ExecutionClassType] = None
    SourceControlDetails: Optional[SourceControlDetailsTypeDef] = None
    MaintenanceWindow: Optional[str] = None
    ProfileName: Optional[str] = None


class CodeGenConfigurationNodePaginatorTypeDef(BaseValidatorModel):
    pass


class JobPaginatorTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    JobMode: Optional[JobModeType] = None
    JobRunQueuingEnabled: Optional[bool] = None
    Description: Optional[str] = None
    LogUri: Optional[str] = None
    Role: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    ExecutionProperty: Optional[ExecutionPropertyTypeDef] = None
    Command: Optional[JobCommandTypeDef] = None
    DefaultArguments: Optional[Dict[str, str]] = None
    NonOverridableArguments: Optional[Dict[str, str]] = None
    Connections: Optional[ConnectionsListOutputTypeDef] = None
    MaxRetries: Optional[int] = None
    AllocatedCapacity: Optional[int] = None
    Timeout: Optional[int] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationPropertyTypeDef] = None
    GlueVersion: Optional[str] = None
    CodeGenConfigurationNodes: Optional[Dict[str, CodeGenConfigurationNodePaginatorTypeDef]] = None
    ExecutionClass: Optional[ExecutionClassType] = None
    SourceControlDetails: Optional[SourceControlDetailsTypeDef] = None
    MaintenanceWindow: Optional[str] = None
    ProfileName: Optional[str] = None


class RecipeStepUnionTypeDef(BaseValidatorModel):
    pass


class RecipeTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    RecipeSteps: Optional[Sequence[RecipeStepUnionTypeDef]] = None


class StorageDescriptorUnionTypeDef(BaseValidatorModel):
    pass


class PartitionInputTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None
    LastAccessTime: Optional[TimestampTypeDef] = None
    StorageDescriptor: Optional[StorageDescriptorUnionTypeDef] = None
    Parameters: Optional[Mapping[str, str]] = None
    LastAnalyzedTime: Optional[TimestampTypeDef] = None


class TableInputTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Owner: Optional[str] = None
    LastAccessTime: Optional[TimestampTypeDef] = None
    LastAnalyzedTime: Optional[TimestampTypeDef] = None
    Retention: Optional[int] = None
    StorageDescriptor: Optional[StorageDescriptorUnionTypeDef] = None
    PartitionKeys: Optional[Sequence[ColumnUnionTypeDef]] = None
    ViewOriginalText: Optional[str] = None
    ViewExpandedText: Optional[str] = None
    TableType: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    TargetTable: Optional[TableIdentifierTypeDef] = None
    ViewDefinition: Optional[ViewDefinitionInputTypeDef] = None


class GetTablesResponsePaginatorTypeDef(BaseValidatorModel):
    TableList: List[TablePaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TableVersionPaginatorTypeDef(BaseValidatorModel):
    Table: Optional[TablePaginatorTypeDef] = None
    VersionId: Optional[str] = None


class GetTableResponseTypeDef(BaseValidatorModel):
    Table: TableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetTablesResponseTypeDef(BaseValidatorModel):
    TableList: List[TableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetUnfilteredTableMetadataResponseTypeDef(BaseValidatorModel):
    Table: TableTypeDef
    AuthorizedColumns: List[str]
    IsRegisteredWithLakeFormation: bool
    CellFilters: List[ColumnRowFilterTypeDef]
    QueryAuthorizationId: str
    IsMultiDialectView: bool
    ResourceArn: str
    IsProtected: bool
    Permissions: List[PermissionType]
    RowFilter: str
    ResponseMetadata: ResponseMetadataTypeDef


class SearchTablesResponseTypeDef(BaseValidatorModel):
    TableList: List[TableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TableVersionTypeDef(BaseValidatorModel):
    Table: Optional[TableTypeDef] = None
    VersionId: Optional[str] = None


class NodeTypeDef(BaseValidatorModel):
    pass


class WorkflowGraphTypeDef(BaseValidatorModel):
    Nodes: Optional[List[NodeTypeDef]] = None
    Edges: Optional[List[EdgeTypeDef]] = None


class UpdateColumnStatisticsForPartitionResponseTypeDef(BaseValidatorModel):
    Errors: List[ColumnStatisticsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateColumnStatisticsForTableResponseTypeDef(BaseValidatorModel):
    Errors: List[ColumnStatisticsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetUnfilteredPartitionsMetadataResponseTypeDef(BaseValidatorModel):
    UnfilteredPartitions: List[UnfilteredPartitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListDataQualityResultsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[DataQualityResultFilterCriteriaTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataQualityRuleRecommendationRunsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[DataQualityRuleRecommendationRunFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListDataQualityRulesetEvaluationRunsRequestTypeDef(BaseValidatorModel):
    Filter: Optional[DataQualityRulesetEvaluationRunFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class BatchGetTableOptimizerErrorTypeDef(BaseValidatorModel):
    pass


class BatchGetTableOptimizerResponseTypeDef(BaseValidatorModel):
    TableOptimizers: List[BatchTableOptimizerTypeDef]
    Failures: List[BatchGetTableOptimizerErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetJobsResponseTypeDef(BaseValidatorModel):
    Jobs: List[JobTypeDef]
    JobsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetJobResponseTypeDef(BaseValidatorModel):
    Job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetJobsResponseTypeDef(BaseValidatorModel):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetJobsResponsePaginatorTypeDef(BaseValidatorModel):
    Jobs: List[JobPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BatchCreatePartitionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionInputList: Sequence[PartitionInputTypeDef]
    CatalogId: Optional[str] = None


class BatchUpdatePartitionRequestEntryTypeDef(BaseValidatorModel):
    PartitionValueList: Sequence[str]
    PartitionInput: PartitionInputTypeDef


class CreatePartitionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionInput: PartitionInputTypeDef
    CatalogId: Optional[str] = None


class UpdatePartitionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValueList: Sequence[str]
    PartitionInput: PartitionInputTypeDef
    CatalogId: Optional[str] = None


class CreateTableRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableInput: TableInputTypeDef
    CatalogId: Optional[str] = None
    PartitionIndexes: Optional[Sequence[PartitionIndexTypeDef]] = None
    TransactionId: Optional[str] = None
    OpenTableFormatInput: Optional[OpenTableFormatInputTypeDef] = None


class UpdateTableRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableInput: TableInputTypeDef
    CatalogId: Optional[str] = None
    SkipArchive: Optional[bool] = None
    TransactionId: Optional[str] = None
    VersionId: Optional[str] = None
    ViewUpdateAction: Optional[ViewUpdateActionType] = None
    Force: Optional[bool] = None


class GetTableVersionsResponsePaginatorTypeDef(BaseValidatorModel):
    TableVersions: List[TableVersionPaginatorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetTableVersionResponseTypeDef(BaseValidatorModel):
    TableVersion: TableVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetTableVersionsResponseTypeDef(BaseValidatorModel):
    TableVersions: List[TableVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class WorkflowRunTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    WorkflowRunId: Optional[str] = None
    PreviousRunId: Optional[str] = None
    WorkflowRunProperties: Optional[Dict[str, str]] = None
    StartedOn: Optional[datetime] = None
    CompletedOn: Optional[datetime] = None
    Status: Optional[WorkflowRunStatusType] = None
    ErrorMessage: Optional[str] = None
    Statistics: Optional[WorkflowRunStatisticsTypeDef] = None
    Graph: Optional[WorkflowGraphTypeDef] = None
    StartingEventBatchCondition: Optional[StartingEventBatchConditionTypeDef] = None


class BatchUpdatePartitionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    Entries: Sequence[BatchUpdatePartitionRequestEntryTypeDef]
    CatalogId: Optional[str] = None


class ColumnStatisticsDataUnionTypeDef(BaseValidatorModel):
    pass


class ColumnStatisticsTypeDef(BaseValidatorModel):
    ColumnName: str
    ColumnType: str
    AnalyzedTime: TimestampTypeDef
    StatisticsData: ColumnStatisticsDataUnionTypeDef


class GetWorkflowRunResponseTypeDef(BaseValidatorModel):
    Run: WorkflowRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetWorkflowRunsResponseTypeDef(BaseValidatorModel):
    Runs: List[WorkflowRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class WorkflowTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    DefaultRunProperties: Optional[Dict[str, str]] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    LastRun: Optional[WorkflowRunTypeDef] = None
    Graph: Optional[WorkflowGraphTypeDef] = None
    MaxConcurrentRuns: Optional[int] = None
    BlueprintDetails: Optional[BlueprintDetailsTypeDef] = None


class BatchGetWorkflowsResponseTypeDef(BaseValidatorModel):
    Workflows: List[WorkflowTypeDef]
    MissingWorkflows: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetWorkflowResponseTypeDef(BaseValidatorModel):
    Workflow: WorkflowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CodeGenConfigurationNodeUnionTypeDef(BaseValidatorModel):
    pass


class CreateJobRequestTypeDef(BaseValidatorModel):
    Name: str
    Role: str
    Command: JobCommandTypeDef
    JobMode: Optional[JobModeType] = None
    JobRunQueuingEnabled: Optional[bool] = None
    Description: Optional[str] = None
    LogUri: Optional[str] = None
    ExecutionProperty: Optional[ExecutionPropertyTypeDef] = None
    DefaultArguments: Optional[Mapping[str, str]] = None
    NonOverridableArguments: Optional[Mapping[str, str]] = None
    Connections: Optional[ConnectionsListUnionTypeDef] = None
    MaxRetries: Optional[int] = None
    AllocatedCapacity: Optional[int] = None
    Timeout: Optional[int] = None
    MaxCapacity: Optional[float] = None
    SecurityConfiguration: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    NotificationProperty: Optional[NotificationPropertyTypeDef] = None
    GlueVersion: Optional[str] = None
    NumberOfWorkers: Optional[int] = None
    WorkerType: Optional[WorkerTypeType] = None
    CodeGenConfigurationNodes: Optional[Mapping[str, CodeGenConfigurationNodeUnionTypeDef]] = None
    ExecutionClass: Optional[ExecutionClassType] = None
    SourceControlDetails: Optional[SourceControlDetailsTypeDef] = None
    MaintenanceWindow: Optional[str] = None


class JobUpdateTypeDef(BaseValidatorModel):
    JobMode: Optional[JobModeType] = None
    JobRunQueuingEnabled: Optional[bool] = None
    Description: Optional[str] = None
    LogUri: Optional[str] = None
    Role: Optional[str] = None
    ExecutionProperty: Optional[ExecutionPropertyTypeDef] = None
    Command: Optional[JobCommandTypeDef] = None
    DefaultArguments: Optional[Mapping[str, str]] = None
    NonOverridableArguments: Optional[Mapping[str, str]] = None
    Connections: Optional[ConnectionsListUnionTypeDef] = None
    MaxRetries: Optional[int] = None
    AllocatedCapacity: Optional[int] = None
    Timeout: Optional[int] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationPropertyTypeDef] = None
    GlueVersion: Optional[str] = None
    CodeGenConfigurationNodes: Optional[Mapping[str, CodeGenConfigurationNodeUnionTypeDef]] = None
    ExecutionClass: Optional[ExecutionClassType] = None
    SourceControlDetails: Optional[SourceControlDetailsTypeDef] = None
    MaintenanceWindow: Optional[str] = None


class ColumnStatisticsUnionTypeDef(BaseValidatorModel):
    pass


class UpdateColumnStatisticsForPartitionRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnStatisticsList: Sequence[ColumnStatisticsUnionTypeDef]
    CatalogId: Optional[str] = None


class UpdateColumnStatisticsForTableRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    ColumnStatisticsList: Sequence[ColumnStatisticsUnionTypeDef]
    CatalogId: Optional[str] = None


class UpdateJobRequestTypeDef(BaseValidatorModel):
    JobName: str
    JobUpdate: JobUpdateTypeDef


