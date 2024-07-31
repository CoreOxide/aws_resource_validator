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
from aws_resource_validator.pydantic_models.glue_constants import *

class NotificationPropertyTypeDef(BaseModel):
    NotifyDelayAfter: Optional[int] = None

class AggregateOperationExtraOutputTypeDef(BaseModel):
    Column: List[str]
    AggFunc: AggFunctionType

class AggregateOperationOutputTypeDef(BaseModel):
    Column: List[str]
    AggFunc: AggFunctionType

class AggregateOperationTypeDef(BaseModel):
    Column: Sequence[str]
    AggFunc: AggFunctionType

class AmazonRedshiftAdvancedOptionTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class OptionTypeDef(BaseModel):
    Value: Optional[str] = None
    Label: Optional[str] = None
    Description: Optional[str] = None

class ApplyMappingExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Mapping: List["MappingExtraOutputTypeDef"]

class ApplyMappingOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Mapping: List["MappingOutputTypeDef"]

class ApplyMappingTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Mapping: Sequence["MappingTypeDef"]

class AuditContextTypeDef(BaseModel):
    AdditionalAuditContext: Optional[str] = None
    RequestedColumns: Optional[Sequence[str]] = None
    AllColumnsRequested: Optional[bool] = None

class AuthorizationCodePropertiesTypeDef(BaseModel):
    AuthorizationCode: Optional[str] = None
    RedirectUri: Optional[str] = None

class PartitionValueListOutputTypeDef(BaseModel):
    Values: List[str]

class BasicCatalogTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class BasicCatalogTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class BasicCatalogTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchDeleteConnectionRequestRequestTypeDef(BaseModel):
    ConnectionNameList: Sequence[str]
    CatalogId: Optional[str] = None

class ErrorDetailTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class BatchDeleteTableRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TablesToDelete: Sequence[str]
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None

class BatchDeleteTableVersionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    VersionIds: Sequence[str]
    CatalogId: Optional[str] = None

class BatchGetBlueprintsRequestRequestTypeDef(BaseModel):
    Names: Sequence[str]
    IncludeBlueprint: Optional[bool] = None
    IncludeParameterSpec: Optional[bool] = None

class BatchGetCrawlersRequestRequestTypeDef(BaseModel):
    CrawlerNames: Sequence[str]

class BatchGetCustomEntityTypesRequestRequestTypeDef(BaseModel):
    Names: Sequence[str]

class CustomEntityTypeTypeDef(BaseModel):
    Name: str
    RegexString: str
    ContextWords: Optional[List[str]] = None

class BatchGetDataQualityResultRequestRequestTypeDef(BaseModel):
    ResultIds: Sequence[str]

class BatchGetDevEndpointsRequestRequestTypeDef(BaseModel):
    DevEndpointNames: Sequence[str]

class DevEndpointTypeDef(BaseModel):
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

class BatchGetJobsRequestRequestTypeDef(BaseModel):
    JobNames: Sequence[str]

class BatchGetTableOptimizerEntryTypeDef(BaseModel):
    catalogId: Optional[str] = None
    databaseName: Optional[str] = None
    tableName: Optional[str] = None
    type: Optional[Literal["compaction"]] = None

class BatchGetTriggersRequestRequestTypeDef(BaseModel):
    TriggerNames: Sequence[str]

class BatchGetWorkflowsRequestRequestTypeDef(BaseModel):
    Names: Sequence[str]
    IncludeGraph: Optional[bool] = None

class BatchStopJobRunRequestRequestTypeDef(BaseModel):
    JobName: str
    JobRunIds: Sequence[str]

class BatchStopJobRunSuccessfulSubmissionTypeDef(BaseModel):
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None

class BinaryColumnStatisticsDataTypeDef(BaseModel):
    MaximumLength: int
    AverageLength: float
    NumberOfNulls: int

class BlueprintDetailsTypeDef(BaseModel):
    BlueprintName: Optional[str] = None
    RunId: Optional[str] = None

class BlueprintRunTypeDef(BaseModel):
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

class LastActiveDefinitionTypeDef(BaseModel):
    Description: Optional[str] = None
    LastModifiedOn: Optional[datetime] = None
    ParameterSpec: Optional[str] = None
    BlueprintLocation: Optional[str] = None
    BlueprintServiceLocation: Optional[str] = None

class BooleanColumnStatisticsDataTypeDef(BaseModel):
    NumberOfTrues: int
    NumberOfFalses: int
    NumberOfNulls: int

class CancelDataQualityRuleRecommendationRunRequestRequestTypeDef(BaseModel):
    RunId: str

class CancelDataQualityRulesetEvaluationRunRequestRequestTypeDef(BaseModel):
    RunId: str

class CancelMLTaskRunRequestRequestTypeDef(BaseModel):
    TransformId: str
    TaskRunId: str

class CancelStatementRequestRequestTypeDef(BaseModel):
    SessionId: str
    Id: int
    RequestOrigin: Optional[str] = None

class CatalogEntryTypeDef(BaseModel):
    DatabaseName: str
    TableName: str

class CatalogImportStatusTypeDef(BaseModel):
    ImportCompleted: Optional[bool] = None
    ImportTime: Optional[datetime] = None
    ImportedBy: Optional[str] = None

class KafkaStreamingSourceOptionsExtraOutputTypeDef(BaseModel):
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

class StreamingDataPreviewOptionsTypeDef(BaseModel):
    PollingTime: Optional[int] = None
    RecordPollingLimit: Optional[int] = None

class KafkaStreamingSourceOptionsOutputTypeDef(BaseModel):
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

class KinesisStreamingSourceOptionsExtraOutputTypeDef(BaseModel):
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

class KinesisStreamingSourceOptionsOutputTypeDef(BaseModel):
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

class CatalogSchemaChangePolicyTypeDef(BaseModel):
    EnableUpdateCatalog: Optional[bool] = None
    UpdateBehavior: Optional[UpdateCatalogBehaviorType] = None

class CatalogSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str

class CatalogTargetExtraOutputTypeDef(BaseModel):
    DatabaseName: str
    Tables: List[str]
    ConnectionName: Optional[str] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None

class CatalogTargetOutputTypeDef(BaseModel):
    DatabaseName: str
    Tables: List[str]
    ConnectionName: Optional[str] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None

class CatalogTargetTypeDef(BaseModel):
    DatabaseName: str
    Tables: Sequence[str]
    ConnectionName: Optional[str] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None

class CheckSchemaVersionValidityInputRequestTypeDef(BaseModel):
    DataFormat: DataFormatType
    SchemaDefinition: str

class CsvClassifierTypeDef(BaseModel):
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

class GrokClassifierTypeDef(BaseModel):
    Name: str
    Classification: str
    GrokPattern: str
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    Version: Optional[int] = None
    CustomPatterns: Optional[str] = None

class JsonClassifierTypeDef(BaseModel):
    Name: str
    JsonPath: str
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    Version: Optional[int] = None

class XMLClassifierTypeDef(BaseModel):
    Name: str
    Classification: str
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    Version: Optional[int] = None
    RowTag: Optional[str] = None

class CloudWatchEncryptionTypeDef(BaseModel):
    CloudWatchEncryptionMode: Optional[CloudWatchEncryptionModeType] = None
    KmsKeyArn: Optional[str] = None

class ConnectorDataTargetExtraOutputTypeDef(BaseModel):
    Name: str
    ConnectionType: str
    Data: Dict[str, str]
    Inputs: Optional[List[str]] = None

class DirectJDBCSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    ConnectionName: str
    ConnectionType: JDBCConnectionTypeType
    RedshiftTmpDir: Optional[str] = None

class DropDuplicatesExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Columns: Optional[List[List[str]]] = None

class DropFieldsExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]

class DynamoDBCatalogSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str

class FillMissingValuesExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    ImputedPath: str
    FilledPath: Optional[str] = None

class MergeExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Source: str
    PrimaryKeys: List[List[str]]

class MicrosoftSQLServerCatalogSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str

class MicrosoftSQLServerCatalogTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class MySQLCatalogSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str

class MySQLCatalogTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class OracleSQLCatalogSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str

class OracleSQLCatalogTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class PIIDetectionExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    PiiType: PiiTypeType
    EntityTypesToDetect: List[str]
    OutputColumnName: Optional[str] = None
    SampleFraction: Optional[float] = None
    ThresholdFraction: Optional[float] = None
    MaskValue: Optional[str] = None

class PostgreSQLCatalogSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str

class PostgreSQLCatalogTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class RedshiftSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    RedshiftTmpDir: Optional[str] = None
    TmpDirIAMRole: Optional[str] = None

class RelationalCatalogSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str

class RenameFieldExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    SourcePath: List[str]
    TargetPath: List[str]

class SelectFieldsExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]

class SelectFromCollectionExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Index: int

class SpigotExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Path: str
    Topk: Optional[int] = None
    Prob: Optional[float] = None

class SplitFieldsExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]

class UnionExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    UnionType: UnionTypeType

class ConnectorDataTargetOutputTypeDef(BaseModel):
    Name: str
    ConnectionType: str
    Data: Dict[str, str]
    Inputs: Optional[List[str]] = None

class DropDuplicatesOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Columns: Optional[List[List[str]]] = None

class DropFieldsOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]

class FillMissingValuesOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    ImputedPath: str
    FilledPath: Optional[str] = None

class MergeOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Source: str
    PrimaryKeys: List[List[str]]

class MicrosoftSQLServerCatalogTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class MySQLCatalogTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class OracleSQLCatalogTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class PIIDetectionOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    PiiType: PiiTypeType
    EntityTypesToDetect: List[str]
    OutputColumnName: Optional[str] = None
    SampleFraction: Optional[float] = None
    ThresholdFraction: Optional[float] = None
    MaskValue: Optional[str] = None

class PostgreSQLCatalogTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class RenameFieldOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    SourcePath: List[str]
    TargetPath: List[str]

class SelectFieldsOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]

class SelectFromCollectionOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Index: int

class SpigotOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Path: str
    Topk: Optional[int] = None
    Prob: Optional[float] = None

class SplitFieldsOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]

class UnionOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    UnionType: UnionTypeType

class ConnectorDataTargetTypeDef(BaseModel):
    Name: str
    ConnectionType: str
    Data: Mapping[str, str]
    Inputs: Optional[Sequence[str]] = None

class DropDuplicatesTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Columns: Optional[Sequence[Sequence[str]]] = None

class DropFieldsTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]

class FillMissingValuesTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    ImputedPath: str
    FilledPath: Optional[str] = None

class MergeTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Source: str
    PrimaryKeys: Sequence[Sequence[str]]

class MicrosoftSQLServerCatalogTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class MySQLCatalogTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class OracleSQLCatalogTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class PIIDetectionTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    PiiType: PiiTypeType
    EntityTypesToDetect: Sequence[str]
    OutputColumnName: Optional[str] = None
    SampleFraction: Optional[float] = None
    ThresholdFraction: Optional[float] = None
    MaskValue: Optional[str] = None

class PostgreSQLCatalogTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class RenameFieldTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    SourcePath: Sequence[str]
    TargetPath: Sequence[str]

class SelectFieldsTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]

class SelectFromCollectionTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Index: int

class SpigotTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Topk: Optional[int] = None
    Prob: Optional[float] = None

class SplitFieldsTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]

class UnionTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    UnionType: UnionTypeType

class CodeGenEdgeTypeDef(BaseModel):
    Source: str
    Target: str
    TargetParameter: Optional[str] = None

class CodeGenNodeArgTypeDef(BaseModel):
    Name: str
    Value: str
    Param: Optional[bool] = None

class ColumnImportanceTypeDef(BaseModel):
    ColumnName: Optional[str] = None
    Importance: Optional[float] = None

class ColumnOutputTypeDef(BaseModel):
    Name: str
    Type: Optional[str] = None
    Comment: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None

class ColumnRowFilterTypeDef(BaseModel):
    ColumnName: Optional[str] = None
    RowFilterExpression: Optional[str] = None

class DateColumnStatisticsDataOutputTypeDef(BaseModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[datetime] = None
    MaximumValue: Optional[datetime] = None

class DoubleColumnStatisticsDataTypeDef(BaseModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[float] = None
    MaximumValue: Optional[float] = None

class LongColumnStatisticsDataTypeDef(BaseModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[int] = None
    MaximumValue: Optional[int] = None

class StringColumnStatisticsDataTypeDef(BaseModel):
    MaximumLength: int
    AverageLength: float
    NumberOfNulls: int
    NumberOfDistinctValues: int

class ColumnStatisticsTaskRunTypeDef(BaseModel):
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
    Status: Optional[ColumnStatisticsStateType] = None
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    DPUSeconds: Optional[float] = None

class ColumnTypeDef(BaseModel):
    Name: str
    Type: Optional[str] = None
    Comment: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None

class ConditionExpressionTypeDef(BaseModel):
    Condition: str
    TargetColumn: str
    Value: Optional[str] = None

class ConditionTypeDef(BaseModel):
    LogicalOperator: Optional[Literal["EQUALS"]] = None
    JobName: Optional[str] = None
    State: Optional[JobRunStateType] = None
    CrawlerName: Optional[str] = None
    CrawlState: Optional[CrawlStateType] = None

class ConfigurationObjectOutputTypeDef(BaseModel):
    DefaultValue: Optional[str] = None
    AllowedValues: Optional[List[str]] = None
    MinValue: Optional[str] = None
    MaxValue: Optional[str] = None

class ConfigurationObjectTypeDef(BaseModel):
    DefaultValue: Optional[str] = None
    AllowedValues: Optional[Sequence[str]] = None
    MinValue: Optional[str] = None
    MaxValue: Optional[str] = None

class ConfusionMatrixTypeDef(BaseModel):
    NumTruePositives: Optional[int] = None
    NumFalsePositives: Optional[int] = None
    NumTrueNegatives: Optional[int] = None
    NumFalseNegatives: Optional[int] = None

class PhysicalConnectionRequirementsTypeDef(BaseModel):
    SubnetId: Optional[str] = None
    SecurityGroupIdList: Optional[Sequence[str]] = None
    AvailabilityZone: Optional[str] = None

class ConnectionPasswordEncryptionTypeDef(BaseModel):
    ReturnConnectionPasswordEncrypted: bool
    AwsKmsKeyId: Optional[str] = None

class PhysicalConnectionRequirementsOutputTypeDef(BaseModel):
    SubnetId: Optional[str] = None
    SecurityGroupIdList: Optional[List[str]] = None
    AvailabilityZone: Optional[str] = None

class ConnectionsListExtraOutputTypeDef(BaseModel):
    Connections: Optional[List[str]] = None

class ConnectionsListOutputTypeDef(BaseModel):
    Connections: Optional[List[str]] = None

class ConnectionsListTypeDef(BaseModel):
    Connections: Optional[Sequence[str]] = None

class CrawlTypeDef(BaseModel):
    State: Optional[CrawlStateType] = None
    StartedOn: Optional[datetime] = None
    CompletedOn: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    LogGroup: Optional[str] = None
    LogStream: Optional[str] = None

class CrawlerHistoryTypeDef(BaseModel):
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

class CrawlerMetricsTypeDef(BaseModel):
    CrawlerName: Optional[str] = None
    TimeLeftSeconds: Optional[float] = None
    StillEstimating: Optional[bool] = None
    LastRuntimeSeconds: Optional[float] = None
    MedianRuntimeSeconds: Optional[float] = None
    TablesCreated: Optional[int] = None
    TablesUpdated: Optional[int] = None
    TablesDeleted: Optional[int] = None

class DeltaTargetExtraOutputTypeDef(BaseModel):
    DeltaTables: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    WriteManifest: Optional[bool] = None
    CreateNativeDeltaTable: Optional[bool] = None

class DynamoDBTargetTypeDef(BaseModel):
    Path: Optional[str] = None
    scanAll: Optional[bool] = None
    scanRate: Optional[float] = None

class HudiTargetExtraOutputTypeDef(BaseModel):
    Paths: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    MaximumTraversalDepth: Optional[int] = None

class IcebergTargetExtraOutputTypeDef(BaseModel):
    Paths: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    MaximumTraversalDepth: Optional[int] = None

class JdbcTargetExtraOutputTypeDef(BaseModel):
    ConnectionName: Optional[str] = None
    Path: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    EnableAdditionalMetadata: Optional[List[JdbcMetadataEntryType]] = None

class MongoDBTargetTypeDef(BaseModel):
    ConnectionName: Optional[str] = None
    Path: Optional[str] = None
    ScanAll: Optional[bool] = None

class S3TargetExtraOutputTypeDef(BaseModel):
    Path: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    SampleSize: Optional[int] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None

class DeltaTargetOutputTypeDef(BaseModel):
    DeltaTables: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    WriteManifest: Optional[bool] = None
    CreateNativeDeltaTable: Optional[bool] = None

class HudiTargetOutputTypeDef(BaseModel):
    Paths: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    MaximumTraversalDepth: Optional[int] = None

class IcebergTargetOutputTypeDef(BaseModel):
    Paths: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    MaximumTraversalDepth: Optional[int] = None

class JdbcTargetOutputTypeDef(BaseModel):
    ConnectionName: Optional[str] = None
    Path: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    EnableAdditionalMetadata: Optional[List[JdbcMetadataEntryType]] = None

class S3TargetOutputTypeDef(BaseModel):
    Path: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    SampleSize: Optional[int] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None

class DeltaTargetTypeDef(BaseModel):
    DeltaTables: Optional[Sequence[str]] = None
    ConnectionName: Optional[str] = None
    WriteManifest: Optional[bool] = None
    CreateNativeDeltaTable: Optional[bool] = None

class HudiTargetTypeDef(BaseModel):
    Paths: Optional[Sequence[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[Sequence[str]] = None
    MaximumTraversalDepth: Optional[int] = None

class IcebergTargetTypeDef(BaseModel):
    Paths: Optional[Sequence[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[Sequence[str]] = None
    MaximumTraversalDepth: Optional[int] = None

class JdbcTargetTypeDef(BaseModel):
    ConnectionName: Optional[str] = None
    Path: Optional[str] = None
    Exclusions: Optional[Sequence[str]] = None
    EnableAdditionalMetadata: Optional[Sequence[JdbcMetadataEntryType]] = None

class S3TargetTypeDef(BaseModel):
    Path: Optional[str] = None
    Exclusions: Optional[Sequence[str]] = None
    ConnectionName: Optional[str] = None
    SampleSize: Optional[int] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None

class LakeFormationConfigurationTypeDef(BaseModel):
    UseLakeFormationCredentials: Optional[bool] = None
    AccountId: Optional[str] = None

class LastCrawlInfoTypeDef(BaseModel):
    Status: Optional[LastCrawlStatusType] = None
    ErrorMessage: Optional[str] = None
    LogGroup: Optional[str] = None
    LogStream: Optional[str] = None
    MessagePrefix: Optional[str] = None
    StartTime: Optional[datetime] = None

class LineageConfigurationTypeDef(BaseModel):
    CrawlerLineageSettings: Optional[CrawlerLineageSettingsType] = None

class RecrawlPolicyTypeDef(BaseModel):
    RecrawlBehavior: Optional[RecrawlBehaviorType] = None

class ScheduleTypeDef(BaseModel):
    ScheduleExpression: Optional[str] = None
    State: Optional[ScheduleStateType] = None

class SchemaChangePolicyTypeDef(BaseModel):
    UpdateBehavior: Optional[UpdateBehaviorType] = None
    DeleteBehavior: Optional[DeleteBehaviorType] = None

class CrawlsFilterTypeDef(BaseModel):
    FieldName: Optional[FieldNameType] = None
    FilterOperator: Optional[FilterOperatorType] = None
    FieldValue: Optional[str] = None

class CreateBlueprintRequestRequestTypeDef(BaseModel):
    Name: str
    BlueprintLocation: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateCsvClassifierRequestTypeDef(BaseModel):
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

class CreateGrokClassifierRequestTypeDef(BaseModel):
    Classification: str
    Name: str
    GrokPattern: str
    CustomPatterns: Optional[str] = None

class CreateJsonClassifierRequestTypeDef(BaseModel):
    Name: str
    JsonPath: str

class CreateXMLClassifierRequestTypeDef(BaseModel):
    Classification: str
    Name: str
    RowTag: Optional[str] = None

class CreateCustomEntityTypeRequestRequestTypeDef(BaseModel):
    Name: str
    RegexString: str
    ContextWords: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class DataQualityTargetTableTypeDef(BaseModel):
    TableName: str
    DatabaseName: str
    CatalogId: Optional[str] = None

class CreateDevEndpointRequestRequestTypeDef(BaseModel):
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

class ExecutionPropertyTypeDef(BaseModel):
    MaxConcurrentRuns: Optional[int] = None

class JobCommandTypeDef(BaseModel):
    Name: Optional[str] = None
    ScriptLocation: Optional[str] = None
    PythonVersion: Optional[str] = None
    Runtime: Optional[str] = None

class SourceControlDetailsTypeDef(BaseModel):
    Provider: Optional[SourceControlProviderType] = None
    Repository: Optional[str] = None
    Owner: Optional[str] = None
    Branch: Optional[str] = None
    Folder: Optional[str] = None
    LastCommitId: Optional[str] = None
    AuthStrategy: Optional[SourceControlAuthStrategyType] = None
    AuthToken: Optional[str] = None

class PartitionIndexTypeDef(BaseModel):
    Keys: Sequence[str]
    IndexName: str

class CreateRegistryInputRequestTypeDef(BaseModel):
    RegistryName: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class RegistryIdTypeDef(BaseModel):
    RegistryName: Optional[str] = None
    RegistryArn: Optional[str] = None

class SessionCommandTypeDef(BaseModel):
    Name: Optional[str] = None
    PythonVersion: Optional[str] = None

class TableOptimizerConfigurationTypeDef(BaseModel):
    roleArn: Optional[str] = None
    enabled: Optional[bool] = None

class EventBatchingConditionTypeDef(BaseModel):
    BatchSize: int
    BatchWindow: Optional[int] = None

class CreateWorkflowRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    DefaultRunProperties: Optional[Mapping[str, str]] = None
    Tags: Optional[Mapping[str, str]] = None
    MaxConcurrentRuns: Optional[int] = None

class DQResultsPublishingOptionsTypeDef(BaseModel):
    EvaluationContext: Optional[str] = None
    ResultsS3Prefix: Optional[str] = None
    CloudWatchMetricsEnabled: Optional[bool] = None
    ResultsPublishingEnabled: Optional[bool] = None

class DQStopJobOnFailureOptionsTypeDef(BaseModel):
    StopJobOnFailureTiming: Optional[DQStopJobOnFailureTimingType] = None

class EncryptionAtRestTypeDef(BaseModel):
    CatalogEncryptionMode: CatalogEncryptionModeType
    SseAwsKmsKeyId: Optional[str] = None
    CatalogEncryptionServiceRole: Optional[str] = None

class DataLakePrincipalTypeDef(BaseModel):
    DataLakePrincipalIdentifier: Optional[str] = None

class DataQualityAnalyzerResultTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    EvaluationMessage: Optional[str] = None
    EvaluatedMetrics: Optional[Dict[str, float]] = None

class DataQualityEvaluationRunAdditionalRunOptionsTypeDef(BaseModel):
    CloudWatchMetricsEnabled: Optional[bool] = None
    ResultsS3Prefix: Optional[str] = None
    CompositeRuleEvaluationMethod: Optional[DQCompositeRuleEvaluationMethodType] = None

class DataQualityMetricValuesTypeDef(BaseModel):
    ActualValue: Optional[float] = None
    ExpectedValue: Optional[float] = None
    LowerLimit: Optional[float] = None
    UpperLimit: Optional[float] = None

class DataQualityRuleResultTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    EvaluationMessage: Optional[str] = None
    Result: Optional[DataQualityRuleResultStatusType] = None
    EvaluatedMetrics: Optional[Dict[str, float]] = None

class GlueTableOutputTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    ConnectionName: Optional[str] = None
    AdditionalOptions: Optional[Dict[str, str]] = None

class GlueTableTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    ConnectionName: Optional[str] = None
    AdditionalOptions: Optional[Mapping[str, str]] = None

class DatabaseIdentifierTypeDef(BaseModel):
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    Region: Optional[str] = None

class FederatedDatabaseTypeDef(BaseModel):
    Identifier: Optional[str] = None
    ConnectionName: Optional[str] = None

class DatatypeTypeDef(BaseModel):
    Id: str
    Label: str

class DecimalNumberOutputTypeDef(BaseModel):
    UnscaledValue: bytes
    Scale: int

class DeleteBlueprintRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteClassifierRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteColumnStatisticsForPartitionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnName: str
    CatalogId: Optional[str] = None

class DeleteColumnStatisticsForTableRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    ColumnName: str
    CatalogId: Optional[str] = None

class DeleteConnectionRequestRequestTypeDef(BaseModel):
    ConnectionName: str
    CatalogId: Optional[str] = None

class DeleteCrawlerRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteCustomEntityTypeRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteDataQualityRulesetRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteDatabaseRequestRequestTypeDef(BaseModel):
    Name: str
    CatalogId: Optional[str] = None

class DeleteDevEndpointRequestRequestTypeDef(BaseModel):
    EndpointName: str

class DeleteJobRequestRequestTypeDef(BaseModel):
    JobName: str

class DeleteMLTransformRequestRequestTypeDef(BaseModel):
    TransformId: str

class DeletePartitionIndexRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    IndexName: str
    CatalogId: Optional[str] = None

class DeletePartitionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    CatalogId: Optional[str] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseModel):
    PolicyHashCondition: Optional[str] = None
    ResourceArn: Optional[str] = None

class SchemaIdTypeDef(BaseModel):
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    RegistryName: Optional[str] = None

class DeleteSecurityConfigurationRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteSessionRequestRequestTypeDef(BaseModel):
    Id: str
    RequestOrigin: Optional[str] = None

class DeleteTableOptimizerRequestRequestTypeDef(BaseModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    Type: Literal["compaction"]

class DeleteTableRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None

class DeleteTableVersionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    VersionId: str
    CatalogId: Optional[str] = None

class DeleteTriggerRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteUsageProfileRequestRequestTypeDef(BaseModel):
    Name: str

class DeleteUserDefinedFunctionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    FunctionName: str
    CatalogId: Optional[str] = None

class DeleteWorkflowRequestRequestTypeDef(BaseModel):
    Name: str

class DevEndpointCustomLibrariesTypeDef(BaseModel):
    ExtraPythonLibsS3Path: Optional[str] = None
    ExtraJarsS3Path: Optional[str] = None

class DirectSchemaChangePolicyTypeDef(BaseModel):
    EnableUpdateCatalog: Optional[bool] = None
    UpdateBehavior: Optional[UpdateCatalogBehaviorType] = None
    Table: Optional[str] = None
    Database: Optional[str] = None

class NullCheckBoxListTypeDef(BaseModel):
    IsEmpty: Optional[bool] = None
    IsNullString: Optional[bool] = None
    IsNegOne: Optional[bool] = None

class TransformConfigParameterExtraOutputTypeDef(BaseModel):
    Name: str
    Type: ParamTypeType
    ValidationRule: Optional[str] = None
    ValidationMessage: Optional[str] = None
    Value: Optional[List[str]] = None
    ListType: Optional[ParamTypeType] = None
    IsOptional: Optional[bool] = None

class TransformConfigParameterOutputTypeDef(BaseModel):
    Name: str
    Type: ParamTypeType
    ValidationRule: Optional[str] = None
    ValidationMessage: Optional[str] = None
    Value: Optional[List[str]] = None
    ListType: Optional[ParamTypeType] = None
    IsOptional: Optional[bool] = None

class TransformConfigParameterTypeDef(BaseModel):
    Name: str
    Type: ParamTypeType
    ValidationRule: Optional[str] = None
    ValidationMessage: Optional[str] = None
    Value: Optional[Sequence[str]] = None
    ListType: Optional[ParamTypeType] = None
    IsOptional: Optional[bool] = None

class EdgeTypeDef(BaseModel):
    SourceId: Optional[str] = None
    DestinationId: Optional[str] = None

class JobBookmarksEncryptionTypeDef(BaseModel):
    JobBookmarksEncryptionMode: Optional[JobBookmarksEncryptionModeType] = None
    KmsKeyArn: Optional[str] = None

class S3EncryptionTypeDef(BaseModel):
    S3EncryptionMode: Optional[S3EncryptionModeType] = None
    KmsKeyArn: Optional[str] = None

class ErrorDetailsTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class ExportLabelsTaskRunPropertiesTypeDef(BaseModel):
    OutputS3Path: Optional[str] = None

class FederatedTableTypeDef(BaseModel):
    Identifier: Optional[str] = None
    DatabaseIdentifier: Optional[str] = None
    ConnectionName: Optional[str] = None

class FilterValueExtraOutputTypeDef(BaseModel):
    Type: FilterValueTypeType
    Value: List[str]

class FilterValueOutputTypeDef(BaseModel):
    Type: FilterValueTypeType
    Value: List[str]

class FilterValueTypeDef(BaseModel):
    Type: FilterValueTypeType
    Value: Sequence[str]

class FindMatchesParametersTypeDef(BaseModel):
    PrimaryKeyColumnName: Optional[str] = None
    PrecisionRecallTradeoff: Optional[float] = None
    AccuracyCostTradeoff: Optional[float] = None
    EnforceProvidedLabels: Optional[bool] = None

class FindMatchesTaskRunPropertiesTypeDef(BaseModel):
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None

class GetBlueprintRequestRequestTypeDef(BaseModel):
    Name: str
    IncludeBlueprint: Optional[bool] = None
    IncludeParameterSpec: Optional[bool] = None

class GetBlueprintRunRequestRequestTypeDef(BaseModel):
    BlueprintName: str
    RunId: str

class GetBlueprintRunsRequestRequestTypeDef(BaseModel):
    BlueprintName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetCatalogImportStatusRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None

class GetClassifierRequestRequestTypeDef(BaseModel):
    Name: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetClassifiersRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetColumnStatisticsForPartitionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnNames: Sequence[str]
    CatalogId: Optional[str] = None

class GetColumnStatisticsForTableRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    ColumnNames: Sequence[str]
    CatalogId: Optional[str] = None

class GetColumnStatisticsTaskRunRequestRequestTypeDef(BaseModel):
    ColumnStatisticsTaskRunId: str

class GetColumnStatisticsTaskRunsRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetConnectionRequestRequestTypeDef(BaseModel):
    Name: str
    CatalogId: Optional[str] = None
    HidePassword: Optional[bool] = None

class GetConnectionsFilterTypeDef(BaseModel):
    MatchCriteria: Optional[Sequence[str]] = None
    ConnectionType: Optional[ConnectionTypeType] = None

class GetCrawlerMetricsRequestRequestTypeDef(BaseModel):
    CrawlerNameList: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetCrawlerRequestRequestTypeDef(BaseModel):
    Name: str

class GetCrawlersRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetCustomEntityTypeRequestRequestTypeDef(BaseModel):
    Name: str

class GetDataCatalogEncryptionSettingsRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None

class GetDataQualityResultRequestRequestTypeDef(BaseModel):
    ResultId: str

class GetDataQualityRuleRecommendationRunRequestRequestTypeDef(BaseModel):
    RunId: str

class GetDataQualityRulesetEvaluationRunRequestRequestTypeDef(BaseModel):
    RunId: str

class GetDataQualityRulesetRequestRequestTypeDef(BaseModel):
    Name: str

class GetDatabaseRequestRequestTypeDef(BaseModel):
    Name: str
    CatalogId: Optional[str] = None

class GetDatabasesRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    AttributesToGet: Optional[Sequence[Literal["NAME"]]] = None

class GetDataflowGraphRequestRequestTypeDef(BaseModel):
    PythonScript: Optional[str] = None

class GetDevEndpointRequestRequestTypeDef(BaseModel):
    EndpointName: str

class GetDevEndpointsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetJobBookmarkRequestRequestTypeDef(BaseModel):
    JobName: str
    RunId: Optional[str] = None

class JobBookmarkEntryTypeDef(BaseModel):
    JobName: Optional[str] = None
    Version: Optional[int] = None
    Run: Optional[int] = None
    Attempt: Optional[int] = None
    PreviousRunId: Optional[str] = None
    RunId: Optional[str] = None
    JobBookmark: Optional[str] = None

class GetJobRequestRequestTypeDef(BaseModel):
    JobName: str

class GetJobRunRequestRequestTypeDef(BaseModel):
    JobName: str
    RunId: str
    PredecessorsIncluded: Optional[bool] = None

class GetJobRunsRequestRequestTypeDef(BaseModel):
    JobName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetJobsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetMLTaskRunRequestRequestTypeDef(BaseModel):
    TransformId: str
    TaskRunId: str

class TaskRunSortCriteriaTypeDef(BaseModel):
    Column: TaskRunSortColumnTypeType
    SortDirection: SortDirectionTypeType

class GetMLTransformRequestRequestTypeDef(BaseModel):
    TransformId: str

class SchemaColumnTypeDef(BaseModel):
    Name: Optional[str] = None
    DataType: Optional[str] = None

class TransformSortCriteriaTypeDef(BaseModel):
    Column: TransformSortColumnTypeType
    SortDirection: SortDirectionTypeType

class MappingEntryTypeDef(BaseModel):
    SourceTable: Optional[str] = None
    SourcePath: Optional[str] = None
    SourceType: Optional[str] = None
    TargetTable: Optional[str] = None
    TargetPath: Optional[str] = None
    TargetType: Optional[str] = None

class GetPartitionIndexesRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None

class GetPartitionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    CatalogId: Optional[str] = None

class SegmentTypeDef(BaseModel):
    SegmentNumber: int
    TotalSegments: int

class GetResourcePoliciesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GluePolicyTypeDef(BaseModel):
    PolicyInJson: Optional[str] = None
    PolicyHash: Optional[str] = None
    CreateTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None

class GetResourcePolicyRequestRequestTypeDef(BaseModel):
    ResourceArn: Optional[str] = None

class SchemaVersionNumberTypeDef(BaseModel):
    LatestVersion: Optional[bool] = None
    VersionNumber: Optional[int] = None

class GetSecurityConfigurationRequestRequestTypeDef(BaseModel):
    Name: str

class GetSecurityConfigurationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetSessionRequestRequestTypeDef(BaseModel):
    Id: str
    RequestOrigin: Optional[str] = None

class GetStatementRequestRequestTypeDef(BaseModel):
    SessionId: str
    Id: int
    RequestOrigin: Optional[str] = None

class GetTableOptimizerRequestRequestTypeDef(BaseModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    Type: Literal["compaction"]

class GetTableVersionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    VersionId: Optional[str] = None

class GetTableVersionsRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetTagsRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class GetTriggerRequestRequestTypeDef(BaseModel):
    Name: str

class GetTriggersRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    DependentJobName: Optional[str] = None
    MaxResults: Optional[int] = None

class SupportedDialectTypeDef(BaseModel):
    Dialect: Optional[ViewDialectType] = None
    DialectVersion: Optional[str] = None

class GetUsageProfileRequestRequestTypeDef(BaseModel):
    Name: str

class GetUserDefinedFunctionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    FunctionName: str
    CatalogId: Optional[str] = None

class GetUserDefinedFunctionsRequestRequestTypeDef(BaseModel):
    Pattern: str
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetWorkflowRequestRequestTypeDef(BaseModel):
    Name: str
    IncludeGraph: Optional[bool] = None

class GetWorkflowRunPropertiesRequestRequestTypeDef(BaseModel):
    Name: str
    RunId: str

class GetWorkflowRunRequestRequestTypeDef(BaseModel):
    Name: str
    RunId: str
    IncludeGraph: Optional[bool] = None

class GetWorkflowRunsRequestRequestTypeDef(BaseModel):
    Name: str
    IncludeGraph: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GlueStudioSchemaColumnTypeDef(BaseModel):
    Name: str
    Type: Optional[str] = None

class S3SourceAdditionalOptionsTypeDef(BaseModel):
    BoundedSize: Optional[int] = None
    BoundedFiles: Optional[int] = None

class IcebergInputTypeDef(BaseModel):
    MetadataOperation: Literal["CREATE"]
    Version: Optional[str] = None

class ImportCatalogToGlueRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None

class ImportLabelsTaskRunPropertiesTypeDef(BaseModel):
    InputS3Path: Optional[str] = None
    Replace: Optional[bool] = None

class JDBCConnectorOptionsExtraOutputTypeDef(BaseModel):
    FilterPredicate: Optional[str] = None
    PartitionColumn: Optional[str] = None
    LowerBound: Optional[int] = None
    UpperBound: Optional[int] = None
    NumPartitions: Optional[int] = None
    JobBookmarkKeys: Optional[List[str]] = None
    JobBookmarkKeysSortOrder: Optional[str] = None
    DataTypeMapping: Optional[Dict[JDBCDataTypeType, GlueRecordTypeType]] = None

class JDBCConnectorOptionsOutputTypeDef(BaseModel):
    FilterPredicate: Optional[str] = None
    PartitionColumn: Optional[str] = None
    LowerBound: Optional[int] = None
    UpperBound: Optional[int] = None
    NumPartitions: Optional[int] = None
    JobBookmarkKeys: Optional[List[str]] = None
    JobBookmarkKeysSortOrder: Optional[str] = None
    DataTypeMapping: Optional[Dict[JDBCDataTypeType, GlueRecordTypeType]] = None

class JDBCConnectorOptionsTypeDef(BaseModel):
    FilterPredicate: Optional[str] = None
    PartitionColumn: Optional[str] = None
    LowerBound: Optional[int] = None
    UpperBound: Optional[int] = None
    NumPartitions: Optional[int] = None
    JobBookmarkKeys: Optional[Sequence[str]] = None
    JobBookmarkKeysSortOrder: Optional[str] = None
    DataTypeMapping: Optional[Mapping[JDBCDataTypeType, GlueRecordTypeType]] = None

class PredecessorTypeDef(BaseModel):
    JobName: Optional[str] = None
    RunId: Optional[str] = None

class JoinColumnExtraOutputTypeDef(BaseModel):
    From: str
    Keys: List[List[str]]

class JoinColumnOutputTypeDef(BaseModel):
    From: str
    Keys: List[List[str]]

class JoinColumnTypeDef(BaseModel):
    From: str
    Keys: Sequence[Sequence[str]]

class KeySchemaElementTypeDef(BaseModel):
    Name: str
    Type: str

class LabelingSetGenerationTaskRunPropertiesTypeDef(BaseModel):
    OutputS3Path: Optional[str] = None

class ListBlueprintsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class ListColumnStatisticsTaskRunsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCrawlersRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class ListCustomEntityTypesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class ListDevEndpointsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class ListJobsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class ListRegistriesInputRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RegistryListItemTypeDef(BaseModel):
    RegistryName: Optional[str] = None
    RegistryArn: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[RegistryStatusType] = None
    CreatedTime: Optional[str] = None
    UpdatedTime: Optional[str] = None

class SchemaVersionListItemTypeDef(BaseModel):
    SchemaArn: Optional[str] = None
    SchemaVersionId: Optional[str] = None
    VersionNumber: Optional[int] = None
    Status: Optional[SchemaVersionStatusType] = None
    CreatedTime: Optional[str] = None

class SchemaListItemTypeDef(BaseModel):
    RegistryName: Optional[str] = None
    SchemaName: Optional[str] = None
    SchemaArn: Optional[str] = None
    Description: Optional[str] = None
    SchemaStatus: Optional[SchemaStatusType] = None
    CreatedTime: Optional[str] = None
    UpdatedTime: Optional[str] = None

class ListSessionsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None
    RequestOrigin: Optional[str] = None

class ListStatementsRequestRequestTypeDef(BaseModel):
    SessionId: str
    RequestOrigin: Optional[str] = None
    NextToken: Optional[str] = None

class ListTableOptimizerRunsRequestRequestTypeDef(BaseModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    Type: Literal["compaction"]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTriggersRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    DependentJobName: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class ListUsageProfilesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class UsageProfileDefinitionTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None

class ListWorkflowsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MLUserDataEncryptionTypeDef(BaseModel):
    MlUserDataEncryptionMode: MLUserDataEncryptionModeStringType
    KmsKeyId: Optional[str] = None

class MappingExtraOutputTypeDef(BaseModel):
    ToKey: Optional[str] = None
    FromPath: Optional[List[str]] = None
    FromType: Optional[str] = None
    ToType: Optional[str] = None
    Dropped: Optional[bool] = None
    Children: Optional[List[Dict[str, Any]]] = None

class MappingOutputTypeDef(BaseModel):
    ToKey: Optional[str] = None
    FromPath: Optional[List[str]] = None
    FromType: Optional[str] = None
    ToType: Optional[str] = None
    Dropped: Optional[bool] = None
    Children: Optional[List[Dict[str, Any]]] = None

class MappingTypeDef(BaseModel):
    ToKey: Optional[str] = None
    FromPath: Optional[Sequence[str]] = None
    FromType: Optional[str] = None
    ToType: Optional[str] = None
    Dropped: Optional[bool] = None
    Children: Optional[Sequence[Dict[str, Any]]] = None

class OtherMetadataValueListItemTypeDef(BaseModel):
    MetadataValue: Optional[str] = None
    CreatedTime: Optional[str] = None

class MetadataKeyValuePairTypeDef(BaseModel):
    MetadataKey: Optional[str] = None
    MetadataValue: Optional[str] = None

class OAuth2ClientApplicationTypeDef(BaseModel):
    UserManagedClientApplicationClientId: Optional[str] = None
    AWSManagedClientApplicationReference: Optional[str] = None

class OrderTypeDef(BaseModel):
    Column: str
    SortOrder: int

class PartitionValueListExtraOutputTypeDef(BaseModel):
    Values: List[str]

class PartitionValueListTypeDef(BaseModel):
    Values: Sequence[str]

class PropertyPredicateTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Comparator: Optional[ComparatorType] = None

class PutResourcePolicyRequestRequestTypeDef(BaseModel):
    PolicyInJson: str
    ResourceArn: Optional[str] = None
    PolicyHashCondition: Optional[str] = None
    PolicyExistsCondition: Optional[ExistConditionType] = None
    EnableHybrid: Optional[EnableHybridValuesType] = None

class PutWorkflowRunPropertiesRequestRequestTypeDef(BaseModel):
    Name: str
    RunId: str
    RunProperties: Mapping[str, str]

class RecipeActionExtraOutputTypeDef(BaseModel):
    Operation: str
    Parameters: Optional[Dict[str, str]] = None

class RecipeActionOutputTypeDef(BaseModel):
    Operation: str
    Parameters: Optional[Dict[str, str]] = None

class RecipeActionTypeDef(BaseModel):
    Operation: str
    Parameters: Optional[Mapping[str, str]] = None

class RecipeReferenceTypeDef(BaseModel):
    RecipeArn: str
    RecipeVersion: str

class UpsertRedshiftTargetOptionsExtraOutputTypeDef(BaseModel):
    TableLocation: Optional[str] = None
    ConnectionName: Optional[str] = None
    UpsertKeys: Optional[List[str]] = None

class UpsertRedshiftTargetOptionsOutputTypeDef(BaseModel):
    TableLocation: Optional[str] = None
    ConnectionName: Optional[str] = None
    UpsertKeys: Optional[List[str]] = None

class UpsertRedshiftTargetOptionsTypeDef(BaseModel):
    TableLocation: Optional[str] = None
    ConnectionName: Optional[str] = None
    UpsertKeys: Optional[Sequence[str]] = None

class ResetJobBookmarkRequestRequestTypeDef(BaseModel):
    JobName: str
    RunId: Optional[str] = None

class ResourceUriTypeDef(BaseModel):
    ResourceType: Optional[ResourceTypeType] = None
    Uri: Optional[str] = None

class ResumeWorkflowRunRequestRequestTypeDef(BaseModel):
    Name: str
    RunId: str
    NodeIds: Sequence[str]

class RunMetricsTypeDef(BaseModel):
    NumberOfBytesCompacted: Optional[str] = None
    NumberOfFilesCompacted: Optional[str] = None
    NumberOfDpus: Optional[str] = None
    JobDurationInHour: Optional[str] = None

class RunStatementRequestRequestTypeDef(BaseModel):
    SessionId: str
    Code: str
    RequestOrigin: Optional[str] = None

class S3DirectSourceAdditionalOptionsTypeDef(BaseModel):
    BoundedSize: Optional[int] = None
    BoundedFiles: Optional[int] = None
    EnableSamplePath: Optional[bool] = None
    SamplePath: Optional[str] = None

class SortCriterionTypeDef(BaseModel):
    FieldName: Optional[str] = None
    Sort: Optional[SortType] = None

class SerDeInfoOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    SerializationLibrary: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None

class SerDeInfoTypeDef(BaseModel):
    Name: Optional[str] = None
    SerializationLibrary: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None

class SkewedInfoOutputTypeDef(BaseModel):
    SkewedColumnNames: Optional[List[str]] = None
    SkewedColumnValues: Optional[List[str]] = None
    SkewedColumnValueLocationMaps: Optional[Dict[str, str]] = None

class SkewedInfoTypeDef(BaseModel):
    SkewedColumnNames: Optional[Sequence[str]] = None
    SkewedColumnValues: Optional[Sequence[str]] = None
    SkewedColumnValueLocationMaps: Optional[Mapping[str, str]] = None

class SqlAliasTypeDef(BaseModel):
    From: str
    Alias: str

class StartBlueprintRunRequestRequestTypeDef(BaseModel):
    BlueprintName: str
    RoleArn: str
    Parameters: Optional[str] = None

class StartColumnStatisticsTaskRunRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    Role: str
    ColumnNameList: Optional[Sequence[str]] = None
    SampleSize: Optional[float] = None
    CatalogID: Optional[str] = None
    SecurityConfiguration: Optional[str] = None

class StartCrawlerRequestRequestTypeDef(BaseModel):
    Name: str

class StartCrawlerScheduleRequestRequestTypeDef(BaseModel):
    CrawlerName: str

class StartExportLabelsTaskRunRequestRequestTypeDef(BaseModel):
    TransformId: str
    OutputS3Path: str

class StartImportLabelsTaskRunRequestRequestTypeDef(BaseModel):
    TransformId: str
    InputS3Path: str
    ReplaceAllLabels: Optional[bool] = None

class StartMLEvaluationTaskRunRequestRequestTypeDef(BaseModel):
    TransformId: str

class StartMLLabelingSetGenerationTaskRunRequestRequestTypeDef(BaseModel):
    TransformId: str
    OutputS3Path: str

class StartTriggerRequestRequestTypeDef(BaseModel):
    Name: str

class StartWorkflowRunRequestRequestTypeDef(BaseModel):
    Name: str
    RunProperties: Optional[Mapping[str, str]] = None

class StartingEventBatchConditionTypeDef(BaseModel):
    BatchSize: Optional[int] = None
    BatchWindow: Optional[int] = None

class StatementOutputDataTypeDef(BaseModel):
    TextPlain: Optional[str] = None

class StopColumnStatisticsTaskRunRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str

class StopCrawlerRequestRequestTypeDef(BaseModel):
    Name: str

class StopCrawlerScheduleRequestRequestTypeDef(BaseModel):
    CrawlerName: str

class StopSessionRequestRequestTypeDef(BaseModel):
    Id: str
    RequestOrigin: Optional[str] = None

class StopTriggerRequestRequestTypeDef(BaseModel):
    Name: str

class StopWorkflowRunRequestRequestTypeDef(BaseModel):
    Name: str
    RunId: str

class TableIdentifierTypeDef(BaseModel):
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    Name: Optional[str] = None
    Region: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagsToAdd: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagsToRemove: Sequence[str]

class UpdateBlueprintRequestRequestTypeDef(BaseModel):
    Name: str
    BlueprintLocation: str
    Description: Optional[str] = None

class UpdateCsvClassifierRequestTypeDef(BaseModel):
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

class UpdateGrokClassifierRequestTypeDef(BaseModel):
    Name: str
    Classification: Optional[str] = None
    GrokPattern: Optional[str] = None
    CustomPatterns: Optional[str] = None

class UpdateJsonClassifierRequestTypeDef(BaseModel):
    Name: str
    JsonPath: Optional[str] = None

class UpdateXMLClassifierRequestTypeDef(BaseModel):
    Name: str
    Classification: Optional[str] = None
    RowTag: Optional[str] = None

class UpdateCrawlerScheduleRequestRequestTypeDef(BaseModel):
    CrawlerName: str
    Schedule: Optional[str] = None

class UpdateDataQualityRulesetRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    Ruleset: Optional[str] = None

class UpdateJobFromSourceControlRequestRequestTypeDef(BaseModel):
    JobName: Optional[str] = None
    Provider: Optional[SourceControlProviderType] = None
    RepositoryName: Optional[str] = None
    RepositoryOwner: Optional[str] = None
    BranchName: Optional[str] = None
    Folder: Optional[str] = None
    CommitId: Optional[str] = None
    AuthStrategy: Optional[SourceControlAuthStrategyType] = None
    AuthToken: Optional[str] = None

class UpdateSourceControlFromJobRequestRequestTypeDef(BaseModel):
    JobName: Optional[str] = None
    Provider: Optional[SourceControlProviderType] = None
    RepositoryName: Optional[str] = None
    RepositoryOwner: Optional[str] = None
    BranchName: Optional[str] = None
    Folder: Optional[str] = None
    CommitId: Optional[str] = None
    AuthStrategy: Optional[SourceControlAuthStrategyType] = None
    AuthToken: Optional[str] = None

class UpdateWorkflowRequestRequestTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    DefaultRunProperties: Optional[Mapping[str, str]] = None
    MaxConcurrentRuns: Optional[int] = None

class ViewRepresentationInputTypeDef(BaseModel):
    Dialect: Optional[ViewDialectType] = None
    DialectVersion: Optional[str] = None
    ViewOriginalText: Optional[str] = None
    ValidationConnection: Optional[str] = None
    ViewExpandedText: Optional[str] = None

class ViewRepresentationTypeDef(BaseModel):
    Dialect: Optional[ViewDialectType] = None
    DialectVersion: Optional[str] = None
    ViewOriginalText: Optional[str] = None
    ViewExpandedText: Optional[str] = None
    ValidationConnection: Optional[str] = None
    IsStale: Optional[bool] = None

class WorkflowRunStatisticsTypeDef(BaseModel):
    TotalActions: Optional[int] = None
    TimeoutActions: Optional[int] = None
    FailedActions: Optional[int] = None
    StoppedActions: Optional[int] = None
    SucceededActions: Optional[int] = None
    RunningActions: Optional[int] = None
    ErroredActions: Optional[int] = None
    WaitingActions: Optional[int] = None

class ActionExtraOutputTypeDef(BaseModel):
    JobName: Optional[str] = None
    Arguments: Optional[Dict[str, str]] = None
    Timeout: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationPropertyTypeDef] = None
    CrawlerName: Optional[str] = None

class ActionOutputTypeDef(BaseModel):
    JobName: Optional[str] = None
    Arguments: Optional[Dict[str, str]] = None
    Timeout: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationPropertyTypeDef] = None
    CrawlerName: Optional[str] = None

class ActionTypeDef(BaseModel):
    JobName: Optional[str] = None
    Arguments: Optional[Mapping[str, str]] = None
    Timeout: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationPropertyTypeDef] = None
    CrawlerName: Optional[str] = None

class StartJobRunRequestRequestTypeDef(BaseModel):
    JobName: str
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

class AggregateExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Groups: List[List[str]]
    Aggs: List[AggregateOperationExtraOutputTypeDef]

class AggregateOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Groups: List[List[str]]
    Aggs: List[AggregateOperationOutputTypeDef]

class AggregateTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Groups: Sequence[Sequence[str]]
    Aggs: Sequence[AggregateOperationTypeDef]

class AmazonRedshiftNodeDataExtraOutputTypeDef(BaseModel):
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

class AmazonRedshiftNodeDataOutputTypeDef(BaseModel):
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

class AmazonRedshiftNodeDataTypeDef(BaseModel):
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

class SnowflakeNodeDataExtraOutputTypeDef(BaseModel):
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

class SnowflakeNodeDataOutputTypeDef(BaseModel):
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

class SnowflakeNodeDataTypeDef(BaseModel):
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

class BackfillErrorTypeDef(BaseModel):
    Code: Optional[BackfillErrorCodeType] = None
    Partitions: Optional[List[PartitionValueListOutputTypeDef]] = None

class CancelMLTaskRunResponseTypeDef(BaseModel):
    TransformId: str
    TaskRunId: str
    Status: TaskStatusTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class CheckSchemaVersionValidityResponseTypeDef(BaseModel):
    Valid: bool
    Error: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateBlueprintResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateConnectionResponseTypeDef(BaseModel):
    CreateConnectionStatus: ConnectionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCustomEntityTypeResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataQualityRulesetResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDevEndpointResponseTypeDef(BaseModel):
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

class CreateJobResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMLTransformResponseTypeDef(BaseModel):
    TransformId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRegistryResponseTypeDef(BaseModel):
    RegistryArn: str
    RegistryName: str
    Description: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSchemaResponseTypeDef(BaseModel):
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

class CreateScriptResponseTypeDef(BaseModel):
    PythonScript: str
    ScalaCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityConfigurationResponseTypeDef(BaseModel):
    Name: str
    CreatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTriggerResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUsageProfileResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBlueprintResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCustomEntityTypeResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteJobResponseTypeDef(BaseModel):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteMLTransformResponseTypeDef(BaseModel):
    TransformId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegistryResponseTypeDef(BaseModel):
    RegistryName: str
    RegistryArn: str
    Status: RegistryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSchemaResponseTypeDef(BaseModel):
    SchemaArn: str
    SchemaName: str
    Status: SchemaStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSessionResponseTypeDef(BaseModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTriggerResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkflowResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCustomEntityTypeResponseTypeDef(BaseModel):
    Name: str
    RegexString: str
    ContextWords: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPlanResponseTypeDef(BaseModel):
    PythonScript: str
    ScalaCode: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegistryResponseTypeDef(BaseModel):
    RegistryName: str
    RegistryArn: str
    Description: str
    Status: RegistryStatusType
    CreatedTime: str
    UpdatedTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyResponseTypeDef(BaseModel):
    PolicyInJson: str
    PolicyHash: str
    CreateTime: datetime
    UpdateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaByDefinitionResponseTypeDef(BaseModel):
    SchemaVersionId: str
    SchemaArn: str
    DataFormat: DataFormatType
    Status: SchemaVersionStatusType
    CreatedTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaResponseTypeDef(BaseModel):
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

class GetSchemaVersionResponseTypeDef(BaseModel):
    SchemaVersionId: str
    SchemaDefinition: str
    DataFormat: DataFormatType
    SchemaArn: str
    VersionNumber: int
    Status: SchemaVersionStatusType
    CreatedTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetSchemaVersionsDiffResponseTypeDef(BaseModel):
    Diff: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetTagsResponseTypeDef(BaseModel):
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowRunPropertiesResponseTypeDef(BaseModel):
    RunProperties: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListBlueprintsResponseTypeDef(BaseModel):
    Blueprints: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListColumnStatisticsTaskRunsResponseTypeDef(BaseModel):
    ColumnStatisticsTaskRunIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListCrawlersResponseTypeDef(BaseModel):
    CrawlerNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDevEndpointsResponseTypeDef(BaseModel):
    DevEndpointNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListJobsResponseTypeDef(BaseModel):
    JobNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMLTransformsResponseTypeDef(BaseModel):
    TransformIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTriggersResponseTypeDef(BaseModel):
    TriggerNames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListWorkflowsResponseTypeDef(BaseModel):
    Workflows: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class PutResourcePolicyResponseTypeDef(BaseModel):
    PolicyHash: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutSchemaVersionMetadataResponseTypeDef(BaseModel):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    LatestVersion: bool
    VersionNumber: int
    SchemaVersionId: str
    MetadataKey: str
    MetadataValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterSchemaVersionResponseTypeDef(BaseModel):
    SchemaVersionId: str
    VersionNumber: int
    Status: SchemaVersionStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveSchemaVersionMetadataResponseTypeDef(BaseModel):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    LatestVersion: bool
    VersionNumber: int
    SchemaVersionId: str
    MetadataKey: str
    MetadataValue: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResumeWorkflowRunResponseTypeDef(BaseModel):
    RunId: str
    NodeIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class RunStatementResponseTypeDef(BaseModel):
    Id: int
    ResponseMetadata: ResponseMetadataTypeDef

class StartBlueprintRunResponseTypeDef(BaseModel):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartColumnStatisticsTaskRunResponseTypeDef(BaseModel):
    ColumnStatisticsTaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataQualityRuleRecommendationRunResponseTypeDef(BaseModel):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataQualityRulesetEvaluationRunResponseTypeDef(BaseModel):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartExportLabelsTaskRunResponseTypeDef(BaseModel):
    TaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportLabelsTaskRunResponseTypeDef(BaseModel):
    TaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartJobRunResponseTypeDef(BaseModel):
    JobRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMLEvaluationTaskRunResponseTypeDef(BaseModel):
    TaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartMLLabelingSetGenerationTaskRunResponseTypeDef(BaseModel):
    TaskRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartTriggerResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartWorkflowRunResponseTypeDef(BaseModel):
    RunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopSessionResponseTypeDef(BaseModel):
    Id: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopTriggerResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBlueprintResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDataQualityRulesetResponseTypeDef(BaseModel):
    Name: str
    Description: str
    Ruleset: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateJobFromSourceControlResponseTypeDef(BaseModel):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateJobResponseTypeDef(BaseModel):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMLTransformResponseTypeDef(BaseModel):
    TransformId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRegistryResponseTypeDef(BaseModel):
    RegistryName: str
    RegistryArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSchemaResponseTypeDef(BaseModel):
    SchemaArn: str
    SchemaName: str
    RegistryName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSourceControlFromJobResponseTypeDef(BaseModel):
    JobName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUsageProfileResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWorkflowResponseTypeDef(BaseModel):
    Name: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteConnectionResponseTypeDef(BaseModel):
    Succeeded: List[str]
    Errors: Dict[str, ErrorDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetTableOptimizerErrorTypeDef(BaseModel):
    error: Optional[ErrorDetailTypeDef] = None
    catalogId: Optional[str] = None
    databaseName: Optional[str] = None
    tableName: Optional[str] = None
    type: Optional[Literal["compaction"]] = None

class BatchStopJobRunErrorTypeDef(BaseModel):
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None
    ErrorDetail: Optional[ErrorDetailTypeDef] = None

class BatchUpdatePartitionFailureEntryTypeDef(BaseModel):
    PartitionValueList: Optional[List[str]] = None
    ErrorDetail: Optional[ErrorDetailTypeDef] = None

class ColumnErrorTypeDef(BaseModel):
    ColumnName: Optional[str] = None
    Error: Optional[ErrorDetailTypeDef] = None

class PartitionErrorTypeDef(BaseModel):
    PartitionValues: Optional[List[str]] = None
    ErrorDetail: Optional[ErrorDetailTypeDef] = None

class TableErrorTypeDef(BaseModel):
    TableName: Optional[str] = None
    ErrorDetail: Optional[ErrorDetailTypeDef] = None

class TableVersionErrorTypeDef(BaseModel):
    TableName: Optional[str] = None
    VersionId: Optional[str] = None
    ErrorDetail: Optional[ErrorDetailTypeDef] = None

class BatchGetCustomEntityTypesResponseTypeDef(BaseModel):
    CustomEntityTypes: List[CustomEntityTypeTypeDef]
    CustomEntityTypesNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ListCustomEntityTypesResponseTypeDef(BaseModel):
    CustomEntityTypes: List[CustomEntityTypeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchGetDevEndpointsResponseTypeDef(BaseModel):
    DevEndpoints: List[DevEndpointTypeDef]
    DevEndpointsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevEndpointResponseTypeDef(BaseModel):
    DevEndpoint: DevEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDevEndpointsResponseTypeDef(BaseModel):
    DevEndpoints: List[DevEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchGetTableOptimizerRequestRequestTypeDef(BaseModel):
    Entries: Sequence[BatchGetTableOptimizerEntryTypeDef]

class DecimalNumberTypeDef(BaseModel):
    UnscaledValue: BlobTypeDef
    Scale: int

class GetBlueprintRunResponseTypeDef(BaseModel):
    BlueprintRun: BlueprintRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlueprintRunsResponseTypeDef(BaseModel):
    BlueprintRuns: List[BlueprintRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BlueprintTypeDef(BaseModel):
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

class GetCatalogImportStatusResponseTypeDef(BaseModel):
    ImportStatus: CatalogImportStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CatalogKafkaSourceExtraOutputTypeDef(BaseModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KafkaStreamingSourceOptionsExtraOutputTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class DirectKafkaSourceExtraOutputTypeDef(BaseModel):
    Name: str
    StreamingOptions: Optional[KafkaStreamingSourceOptionsExtraOutputTypeDef] = None
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class CatalogKafkaSourceOutputTypeDef(BaseModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KafkaStreamingSourceOptionsOutputTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class DirectKafkaSourceOutputTypeDef(BaseModel):
    Name: str
    StreamingOptions: Optional[KafkaStreamingSourceOptionsOutputTypeDef] = None
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class CatalogKinesisSourceExtraOutputTypeDef(BaseModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsExtraOutputTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class DirectKinesisSourceExtraOutputTypeDef(BaseModel):
    Name: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsExtraOutputTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class CatalogKinesisSourceOutputTypeDef(BaseModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsOutputTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class DirectKinesisSourceOutputTypeDef(BaseModel):
    Name: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsOutputTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class GovernedCatalogTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None

class GovernedCatalogTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None

class GovernedCatalogTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None

class S3CatalogTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None

class S3CatalogTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None

class S3CatalogTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None

class S3DeltaCatalogTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    AdditionalOptions: Optional[Dict[str, str]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None

class S3DeltaCatalogTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    AdditionalOptions: Optional[Dict[str, str]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None

class S3DeltaCatalogTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    AdditionalOptions: Optional[Mapping[str, str]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None

class S3HudiCatalogTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    AdditionalOptions: Dict[str, str]
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None

class S3HudiCatalogTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    AdditionalOptions: Dict[str, str]
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None

class S3HudiCatalogTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Table: str
    Database: str
    AdditionalOptions: Mapping[str, str]
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None

class ClassifierTypeDef(BaseModel):
    GrokClassifier: Optional[GrokClassifierTypeDef] = None
    XMLClassifier: Optional[XMLClassifierTypeDef] = None
    JsonClassifier: Optional[JsonClassifierTypeDef] = None
    CsvClassifier: Optional[CsvClassifierTypeDef] = None

class CodeGenNodeOutputTypeDef(BaseModel):
    Id: str
    NodeType: str
    Args: List[CodeGenNodeArgTypeDef]
    LineNumber: Optional[int] = None

class CodeGenNodeTypeDef(BaseModel):
    Id: str
    NodeType: str
    Args: Sequence[CodeGenNodeArgTypeDef]
    LineNumber: Optional[int] = None

class LocationTypeDef(BaseModel):
    Jdbc: Optional[Sequence[CodeGenNodeArgTypeDef]] = None
    S3: Optional[Sequence[CodeGenNodeArgTypeDef]] = None
    DynamoDB: Optional[Sequence[CodeGenNodeArgTypeDef]] = None

class GetColumnStatisticsTaskRunResponseTypeDef(BaseModel):
    ColumnStatisticsTaskRun: ColumnStatisticsTaskRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetColumnStatisticsTaskRunsResponseTypeDef(BaseModel):
    ColumnStatisticsTaskRuns: List[ColumnStatisticsTaskRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DateColumnStatisticsDataTypeDef(BaseModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[TimestampTypeDef] = None
    MaximumValue: Optional[TimestampTypeDef] = None

class GetTableRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None

class GetTablesRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None

class KafkaStreamingSourceOptionsTypeDef(BaseModel):
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

class KinesisStreamingSourceOptionsTypeDef(BaseModel):
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

class QuerySessionContextTypeDef(BaseModel):
    QueryId: Optional[str] = None
    QueryStartTime: Optional[TimestampTypeDef] = None
    ClusterId: Optional[str] = None
    QueryAuthorizationId: Optional[str] = None
    AdditionalContext: Optional[Mapping[str, str]] = None

class TaskRunFilterCriteriaTypeDef(BaseModel):
    TaskRunType: Optional[TaskTypeType] = None
    Status: Optional[TaskStatusTypeType] = None
    StartedBefore: Optional[TimestampTypeDef] = None
    StartedAfter: Optional[TimestampTypeDef] = None

class PredicateExtraOutputTypeDef(BaseModel):
    Logical: Optional[LogicalType] = None
    Conditions: Optional[List[ConditionTypeDef]] = None

class PredicateOutputTypeDef(BaseModel):
    Logical: Optional[LogicalType] = None
    Conditions: Optional[List[ConditionTypeDef]] = None

class PredicateTypeDef(BaseModel):
    Logical: Optional[LogicalType] = None
    Conditions: Optional[Sequence[ConditionTypeDef]] = None

class ProfileConfigurationOutputTypeDef(BaseModel):
    SessionConfiguration: Optional[Dict[str, ConfigurationObjectOutputTypeDef]] = None
    JobConfiguration: Optional[Dict[str, ConfigurationObjectOutputTypeDef]] = None

class ProfileConfigurationTypeDef(BaseModel):
    SessionConfiguration: Optional[Mapping[str, ConfigurationObjectTypeDef]] = None
    JobConfiguration: Optional[Mapping[str, ConfigurationObjectTypeDef]] = None

class FindMatchesMetricsTypeDef(BaseModel):
    AreaUnderPRCurve: Optional[float] = None
    Precision: Optional[float] = None
    Recall: Optional[float] = None
    F1: Optional[float] = None
    ConfusionMatrix: Optional[ConfusionMatrixTypeDef] = None
    ColumnImportances: Optional[List[ColumnImportanceTypeDef]] = None

class CrawlerNodeDetailsTypeDef(BaseModel):
    Crawls: Optional[List[CrawlTypeDef]] = None

class ListCrawlsResponseTypeDef(BaseModel):
    Crawls: List[CrawlerHistoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCrawlerMetricsResponseTypeDef(BaseModel):
    CrawlerMetricsList: List[CrawlerMetricsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CrawlerTargetsExtraOutputTypeDef(BaseModel):
    S3Targets: Optional[List[S3TargetExtraOutputTypeDef]] = None
    JdbcTargets: Optional[List[JdbcTargetExtraOutputTypeDef]] = None
    MongoDBTargets: Optional[List[MongoDBTargetTypeDef]] = None
    DynamoDBTargets: Optional[List[DynamoDBTargetTypeDef]] = None
    CatalogTargets: Optional[List[CatalogTargetExtraOutputTypeDef]] = None
    DeltaTargets: Optional[List[DeltaTargetExtraOutputTypeDef]] = None
    IcebergTargets: Optional[List[IcebergTargetExtraOutputTypeDef]] = None
    HudiTargets: Optional[List[HudiTargetExtraOutputTypeDef]] = None

class CrawlerTargetsOutputTypeDef(BaseModel):
    S3Targets: Optional[List[S3TargetOutputTypeDef]] = None
    JdbcTargets: Optional[List[JdbcTargetOutputTypeDef]] = None
    MongoDBTargets: Optional[List[MongoDBTargetTypeDef]] = None
    DynamoDBTargets: Optional[List[DynamoDBTargetTypeDef]] = None
    CatalogTargets: Optional[List[CatalogTargetOutputTypeDef]] = None
    DeltaTargets: Optional[List[DeltaTargetOutputTypeDef]] = None
    IcebergTargets: Optional[List[IcebergTargetOutputTypeDef]] = None
    HudiTargets: Optional[List[HudiTargetOutputTypeDef]] = None

class CrawlerTargetsTypeDef(BaseModel):
    S3Targets: Optional[Sequence[S3TargetTypeDef]] = None
    JdbcTargets: Optional[Sequence[JdbcTargetTypeDef]] = None
    MongoDBTargets: Optional[Sequence[MongoDBTargetTypeDef]] = None
    DynamoDBTargets: Optional[Sequence[DynamoDBTargetTypeDef]] = None
    CatalogTargets: Optional[Sequence[CatalogTargetTypeDef]] = None
    DeltaTargets: Optional[Sequence[DeltaTargetTypeDef]] = None
    IcebergTargets: Optional[Sequence[IcebergTargetTypeDef]] = None
    HudiTargets: Optional[Sequence[HudiTargetTypeDef]] = None

class ListCrawlsRequestRequestTypeDef(BaseModel):
    CrawlerName: str
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[CrawlsFilterTypeDef]] = None
    NextToken: Optional[str] = None

class CreateClassifierRequestRequestTypeDef(BaseModel):
    GrokClassifier: Optional[CreateGrokClassifierRequestTypeDef] = None
    XMLClassifier: Optional[CreateXMLClassifierRequestTypeDef] = None
    JsonClassifier: Optional[CreateJsonClassifierRequestTypeDef] = None
    CsvClassifier: Optional[CreateCsvClassifierRequestTypeDef] = None

class CreateDataQualityRulesetRequestRequestTypeDef(BaseModel):
    Name: str
    Ruleset: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    TargetTable: Optional[DataQualityTargetTableTypeDef] = None
    ClientToken: Optional[str] = None

class DataQualityRulesetFilterCriteriaTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    LastModifiedBefore: Optional[TimestampTypeDef] = None
    LastModifiedAfter: Optional[TimestampTypeDef] = None
    TargetTable: Optional[DataQualityTargetTableTypeDef] = None

class DataQualityRulesetListDetailsTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    TargetTable: Optional[DataQualityTargetTableTypeDef] = None
    RecommendationRunId: Optional[str] = None
    RuleCount: Optional[int] = None

class GetDataQualityRulesetResponseTypeDef(BaseModel):
    Name: str
    Description: str
    Ruleset: str
    TargetTable: DataQualityTargetTableTypeDef
    CreatedOn: datetime
    LastModifiedOn: datetime
    RecommendationRunId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePartitionIndexRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    PartitionIndex: PartitionIndexTypeDef
    CatalogId: Optional[str] = None

class CreateSchemaInputRequestTypeDef(BaseModel):
    SchemaName: str
    DataFormat: DataFormatType
    RegistryId: Optional[RegistryIdTypeDef] = None
    Compatibility: Optional[CompatibilityType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    SchemaDefinition: Optional[str] = None

class DeleteRegistryInputRequestTypeDef(BaseModel):
    RegistryId: RegistryIdTypeDef

class GetRegistryInputRequestTypeDef(BaseModel):
    RegistryId: RegistryIdTypeDef

class ListSchemasInputRequestTypeDef(BaseModel):
    RegistryId: Optional[RegistryIdTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UpdateRegistryInputRequestTypeDef(BaseModel):
    RegistryId: RegistryIdTypeDef
    Description: str

class CreateSessionRequestRequestTypeDef(BaseModel):
    Id: str
    Role: str
    Command: SessionCommandTypeDef
    Description: Optional[str] = None
    Timeout: Optional[int] = None
    IdleTimeout: Optional[int] = None
    DefaultArguments: Optional[Mapping[str, str]] = None
    Connections: Optional[ConnectionsListTypeDef] = None
    MaxCapacity: Optional[float] = None
    NumberOfWorkers: Optional[int] = None
    WorkerType: Optional[WorkerTypeType] = None
    SecurityConfiguration: Optional[str] = None
    GlueVersion: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    RequestOrigin: Optional[str] = None

class SessionTypeDef(BaseModel):
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

class CreateTableOptimizerRequestRequestTypeDef(BaseModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    Type: Literal["compaction"]
    TableOptimizerConfiguration: TableOptimizerConfigurationTypeDef

class UpdateTableOptimizerRequestRequestTypeDef(BaseModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    Type: Literal["compaction"]
    TableOptimizerConfiguration: TableOptimizerConfigurationTypeDef

class EvaluateDataQualityExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Ruleset: str
    Output: Optional[DQTransformOutputType] = None
    PublishingOptions: Optional[DQResultsPublishingOptionsTypeDef] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptionsTypeDef] = None

class EvaluateDataQualityMultiFrameExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Ruleset: str
    AdditionalDataSources: Optional[Dict[str, str]] = None
    PublishingOptions: Optional[DQResultsPublishingOptionsTypeDef] = None
    AdditionalOptions: Optional[Dict[AdditionalOptionKeysType, str]] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptionsTypeDef] = None

class EvaluateDataQualityMultiFrameOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Ruleset: str
    AdditionalDataSources: Optional[Dict[str, str]] = None
    PublishingOptions: Optional[DQResultsPublishingOptionsTypeDef] = None
    AdditionalOptions: Optional[Dict[AdditionalOptionKeysType, str]] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptionsTypeDef] = None

class EvaluateDataQualityMultiFrameTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Ruleset: str
    AdditionalDataSources: Optional[Mapping[str, str]] = None
    PublishingOptions: Optional[DQResultsPublishingOptionsTypeDef] = None
    AdditionalOptions: Optional[Mapping[AdditionalOptionKeysType, str]] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptionsTypeDef] = None

class EvaluateDataQualityOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Ruleset: str
    Output: Optional[DQTransformOutputType] = None
    PublishingOptions: Optional[DQResultsPublishingOptionsTypeDef] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptionsTypeDef] = None

class EvaluateDataQualityTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Ruleset: str
    Output: Optional[DQTransformOutputType] = None
    PublishingOptions: Optional[DQResultsPublishingOptionsTypeDef] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptionsTypeDef] = None

class DataCatalogEncryptionSettingsTypeDef(BaseModel):
    EncryptionAtRest: Optional[EncryptionAtRestTypeDef] = None
    ConnectionPasswordEncryption: Optional[ConnectionPasswordEncryptionTypeDef] = None

class PrincipalPermissionsOutputTypeDef(BaseModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Permissions: Optional[List[PermissionType]] = None

class PrincipalPermissionsTypeDef(BaseModel):
    Principal: Optional[DataLakePrincipalTypeDef] = None
    Permissions: Optional[Sequence[PermissionType]] = None

class MetricBasedObservationTypeDef(BaseModel):
    MetricName: Optional[str] = None
    MetricValues: Optional[DataQualityMetricValuesTypeDef] = None
    NewRules: Optional[List[str]] = None

class DataSourceOutputTypeDef(BaseModel):
    GlueTable: GlueTableOutputTypeDef

class DataSourceTypeDef(BaseModel):
    GlueTable: GlueTableTypeDef

class NullValueFieldTypeDef(BaseModel):
    Value: str
    Datatype: DatatypeTypeDef

class DecimalColumnStatisticsDataOutputTypeDef(BaseModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[DecimalNumberOutputTypeDef] = None
    MaximumValue: Optional[DecimalNumberOutputTypeDef] = None

class DeleteSchemaInputRequestTypeDef(BaseModel):
    SchemaId: SchemaIdTypeDef

class DeleteSchemaVersionsInputRequestTypeDef(BaseModel):
    SchemaId: SchemaIdTypeDef
    Versions: str

class GetSchemaByDefinitionInputRequestTypeDef(BaseModel):
    SchemaId: SchemaIdTypeDef
    SchemaDefinition: str

class GetSchemaInputRequestTypeDef(BaseModel):
    SchemaId: SchemaIdTypeDef

class ListSchemaVersionsInputRequestTypeDef(BaseModel):
    SchemaId: SchemaIdTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RegisterSchemaVersionInputRequestTypeDef(BaseModel):
    SchemaId: SchemaIdTypeDef
    SchemaDefinition: str

class SchemaReferenceTypeDef(BaseModel):
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionId: Optional[str] = None
    SchemaVersionNumber: Optional[int] = None

class UpdateDevEndpointRequestRequestTypeDef(BaseModel):
    EndpointName: str
    PublicKey: Optional[str] = None
    AddPublicKeys: Optional[Sequence[str]] = None
    DeletePublicKeys: Optional[Sequence[str]] = None
    CustomLibraries: Optional[DevEndpointCustomLibrariesTypeDef] = None
    UpdateEtlLibraries: Optional[bool] = None
    DeleteArguments: Optional[Sequence[str]] = None
    AddArguments: Optional[Mapping[str, str]] = None

class S3DeltaDirectTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Path: str
    Compression: DeltaTargetCompressionTypeType
    Format: TargetFormatType
    PartitionKeys: Optional[List[List[str]]] = None
    AdditionalOptions: Optional[Dict[str, str]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None

class S3DeltaDirectTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Path: str
    Compression: DeltaTargetCompressionTypeType
    Format: TargetFormatType
    PartitionKeys: Optional[List[List[str]]] = None
    AdditionalOptions: Optional[Dict[str, str]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None

class S3DeltaDirectTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Compression: DeltaTargetCompressionTypeType
    Format: TargetFormatType
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    AdditionalOptions: Optional[Mapping[str, str]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None

class S3DirectTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Path: str
    Format: TargetFormatType
    PartitionKeys: Optional[List[List[str]]] = None
    Compression: Optional[str] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None

class S3DirectTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Path: str
    Format: TargetFormatType
    PartitionKeys: Optional[List[List[str]]] = None
    Compression: Optional[str] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None

class S3DirectTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Format: TargetFormatType
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    Compression: Optional[str] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None

class S3GlueParquetTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Path: str
    PartitionKeys: Optional[List[List[str]]] = None
    Compression: Optional[ParquetCompressionTypeType] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None

class S3GlueParquetTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Path: str
    PartitionKeys: Optional[List[List[str]]] = None
    Compression: Optional[ParquetCompressionTypeType] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None

class S3GlueParquetTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    Compression: Optional[ParquetCompressionTypeType] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None

class S3HudiDirectTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Path: str
    Compression: HudiTargetCompressionTypeType
    Format: TargetFormatType
    AdditionalOptions: Dict[str, str]
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None

class S3HudiDirectTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Path: str
    Compression: HudiTargetCompressionTypeType
    Format: TargetFormatType
    AdditionalOptions: Dict[str, str]
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None

class S3HudiDirectTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Path: str
    Compression: HudiTargetCompressionTypeType
    Format: TargetFormatType
    AdditionalOptions: Mapping[str, str]
    PartitionKeys: Optional[Sequence[Sequence[str]]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None

class EncryptionConfigurationExtraOutputTypeDef(BaseModel):
    S3Encryption: Optional[List[S3EncryptionTypeDef]] = None
    CloudWatchEncryption: Optional[CloudWatchEncryptionTypeDef] = None
    JobBookmarksEncryption: Optional[JobBookmarksEncryptionTypeDef] = None

class EncryptionConfigurationOutputTypeDef(BaseModel):
    S3Encryption: Optional[List[S3EncryptionTypeDef]] = None
    CloudWatchEncryption: Optional[CloudWatchEncryptionTypeDef] = None
    JobBookmarksEncryption: Optional[JobBookmarksEncryptionTypeDef] = None

class EncryptionConfigurationTypeDef(BaseModel):
    S3Encryption: Optional[Sequence[S3EncryptionTypeDef]] = None
    CloudWatchEncryption: Optional[CloudWatchEncryptionTypeDef] = None
    JobBookmarksEncryption: Optional[JobBookmarksEncryptionTypeDef] = None

class SchemaVersionErrorItemTypeDef(BaseModel):
    VersionNumber: Optional[int] = None
    ErrorDetails: Optional[ErrorDetailsTypeDef] = None

class FilterExpressionExtraOutputTypeDef(BaseModel):
    Operation: FilterOperationType
    Values: List[FilterValueExtraOutputTypeDef]
    Negated: Optional[bool] = None

class FilterExpressionOutputTypeDef(BaseModel):
    Operation: FilterOperationType
    Values: List[FilterValueOutputTypeDef]
    Negated: Optional[bool] = None

class FilterExpressionTypeDef(BaseModel):
    Operation: FilterOperationType
    Values: Sequence[FilterValueTypeDef]
    Negated: Optional[bool] = None

class TransformParametersTypeDef(BaseModel):
    TransformType: Literal["FIND_MATCHES"]
    FindMatchesParameters: Optional[FindMatchesParametersTypeDef] = None

class GetClassifiersRequestGetClassifiersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCrawlerMetricsRequestGetCrawlerMetricsPaginateTypeDef(BaseModel):
    CrawlerNameList: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCrawlersRequestGetCrawlersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDatabasesRequestGetDatabasesPaginateTypeDef(BaseModel):
    CatalogId: Optional[str] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    AttributesToGet: Optional[Sequence[Literal["NAME"]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDevEndpointsRequestGetDevEndpointsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetJobRunsRequestGetJobRunsPaginateTypeDef(BaseModel):
    JobName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetJobsRequestGetJobsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetPartitionIndexesRequestGetPartitionIndexesPaginateTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSecurityConfigurationsRequestGetSecurityConfigurationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTableVersionsRequestGetTableVersionsPaginateTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTablesRequestGetTablesPaginateTypeDef(BaseModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTriggersRequestGetTriggersPaginateTypeDef(BaseModel):
    DependentJobName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetUserDefinedFunctionsRequestGetUserDefinedFunctionsPaginateTypeDef(BaseModel):
    Pattern: str
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetWorkflowRunsRequestGetWorkflowRunsPaginateTypeDef(BaseModel):
    Name: str
    IncludeGraph: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBlueprintsRequestListBlueprintsPaginateTypeDef(BaseModel):
    Tags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseModel):
    Tags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRegistriesInputListRegistriesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemaVersionsInputListSchemaVersionsPaginateTypeDef(BaseModel):
    SchemaId: SchemaIdTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemasInputListSchemasPaginateTypeDef(BaseModel):
    RegistryId: Optional[RegistryIdTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTriggersRequestListTriggersPaginateTypeDef(BaseModel):
    DependentJobName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsageProfilesRequestListUsageProfilesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowsRequestListWorkflowsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetConnectionsRequestGetConnectionsPaginateTypeDef(BaseModel):
    CatalogId: Optional[str] = None
    Filter: Optional[GetConnectionsFilterTypeDef] = None
    HidePassword: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetConnectionsRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None
    Filter: Optional[GetConnectionsFilterTypeDef] = None
    HidePassword: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetJobBookmarkResponseTypeDef(BaseModel):
    JobBookmarkEntry: JobBookmarkEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ResetJobBookmarkResponseTypeDef(BaseModel):
    JobBookmarkEntry: JobBookmarkEntryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TransformFilterCriteriaTypeDef(BaseModel):
    Name: Optional[str] = None
    TransformType: Optional[Literal["FIND_MATCHES"]] = None
    Status: Optional[TransformStatusTypeType] = None
    GlueVersion: Optional[str] = None
    CreatedBefore: Optional[TimestampTypeDef] = None
    CreatedAfter: Optional[TimestampTypeDef] = None
    LastModifiedBefore: Optional[TimestampTypeDef] = None
    LastModifiedAfter: Optional[TimestampTypeDef] = None
    Schema: Optional[Sequence[SchemaColumnTypeDef]] = None

class GetMappingResponseTypeDef(BaseModel):
    Mapping: List[MappingEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPartitionsRequestGetPartitionsPaginateTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    Segment: Optional[SegmentTypeDef] = None
    ExcludeColumnSchema: Optional[bool] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetPartitionsRequestRequestTypeDef(BaseModel):
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

class GetResourcePoliciesResponseTypeDef(BaseModel):
    GetResourcePoliciesResponseList: List[GluePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetSchemaVersionInputRequestTypeDef(BaseModel):
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionId: Optional[str] = None
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None

class GetSchemaVersionsDiffInputRequestTypeDef(BaseModel):
    SchemaId: SchemaIdTypeDef
    FirstSchemaVersionNumber: SchemaVersionNumberTypeDef
    SecondSchemaVersionNumber: SchemaVersionNumberTypeDef
    SchemaDiffType: Literal["SYNTAX_DIFF"]

class UpdateSchemaInputRequestTypeDef(BaseModel):
    SchemaId: SchemaIdTypeDef
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None
    Compatibility: Optional[CompatibilityType] = None
    Description: Optional[str] = None

class GlueSchemaExtraOutputTypeDef(BaseModel):
    Columns: Optional[List[GlueStudioSchemaColumnTypeDef]] = None

class GlueSchemaOutputTypeDef(BaseModel):
    Columns: Optional[List[GlueStudioSchemaColumnTypeDef]] = None

class GlueSchemaTypeDef(BaseModel):
    Columns: Optional[Sequence[GlueStudioSchemaColumnTypeDef]] = None

class GovernedCatalogSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    PartitionPredicate: Optional[str] = None
    AdditionalOptions: Optional[S3SourceAdditionalOptionsTypeDef] = None

class S3CatalogSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    PartitionPredicate: Optional[str] = None
    AdditionalOptions: Optional[S3SourceAdditionalOptionsTypeDef] = None

class OpenTableFormatInputTypeDef(BaseModel):
    IcebergInput: Optional[IcebergInputTypeDef] = None

class JobRunTypeDef(BaseModel):
    Id: Optional[str] = None
    Attempt: Optional[int] = None
    PreviousRunId: Optional[str] = None
    TriggerName: Optional[str] = None
    JobName: Optional[str] = None
    JobMode: Optional[JobModeType] = None
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

class JoinExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    JoinType: JoinTypeType
    Columns: List[JoinColumnExtraOutputTypeDef]

class JoinOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    JoinType: JoinTypeType
    Columns: List[JoinColumnOutputTypeDef]

class JoinTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    JoinType: JoinTypeType
    Columns: Sequence[JoinColumnTypeDef]

class TaskRunPropertiesTypeDef(BaseModel):
    TaskType: Optional[TaskTypeType] = None
    ImportLabelsTaskRunProperties: Optional[ImportLabelsTaskRunPropertiesTypeDef] = None
    ExportLabelsTaskRunProperties: Optional[ExportLabelsTaskRunPropertiesTypeDef] = None
    LabelingSetGenerationTaskRunProperties: Optional[       LabelingSetGenerationTaskRunPropertiesTypeDef     ] = None
    FindMatchesTaskRunProperties: Optional[FindMatchesTaskRunPropertiesTypeDef] = None

class ListRegistriesResponseTypeDef(BaseModel):
    Registries: List[RegistryListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSchemaVersionsResponseTypeDef(BaseModel):
    Schemas: List[SchemaVersionListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSchemasResponseTypeDef(BaseModel):
    Schemas: List[SchemaListItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUsageProfilesResponseTypeDef(BaseModel):
    Profiles: List[UsageProfileDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TransformEncryptionTypeDef(BaseModel):
    MlUserDataEncryption: Optional[MLUserDataEncryptionTypeDef] = None
    TaskRunSecurityConfigurationName: Optional[str] = None

class MetadataInfoTypeDef(BaseModel):
    MetadataValue: Optional[str] = None
    CreatedTime: Optional[str] = None
    OtherMetadataValueList: Optional[List[OtherMetadataValueListItemTypeDef]] = None

class PutSchemaVersionMetadataInputRequestTypeDef(BaseModel):
    MetadataKeyValue: MetadataKeyValuePairTypeDef
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None
    SchemaVersionId: Optional[str] = None

class QuerySchemaVersionMetadataInputRequestTypeDef(BaseModel):
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None
    SchemaVersionId: Optional[str] = None
    MetadataList: Optional[Sequence[MetadataKeyValuePairTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RemoveSchemaVersionMetadataInputRequestTypeDef(BaseModel):
    MetadataKeyValue: MetadataKeyValuePairTypeDef
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None
    SchemaVersionId: Optional[str] = None

class OAuth2PropertiesInputTypeDef(BaseModel):
    OAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    OAuth2ClientApplication: Optional[OAuth2ClientApplicationTypeDef] = None
    TokenUrl: Optional[str] = None
    TokenUrlParametersMap: Optional[Mapping[str, str]] = None
    AuthorizationCodeProperties: Optional[AuthorizationCodePropertiesTypeDef] = None

class OAuth2PropertiesTypeDef(BaseModel):
    OAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    OAuth2ClientApplication: Optional[OAuth2ClientApplicationTypeDef] = None
    TokenUrl: Optional[str] = None
    TokenUrlParametersMap: Optional[Dict[str, str]] = None

class RecipeStepExtraOutputTypeDef(BaseModel):
    Action: RecipeActionExtraOutputTypeDef
    ConditionExpressions: Optional[List[ConditionExpressionTypeDef]] = None

class RecipeStepOutputTypeDef(BaseModel):
    Action: RecipeActionOutputTypeDef
    ConditionExpressions: Optional[List[ConditionExpressionTypeDef]] = None

class RecipeStepTypeDef(BaseModel):
    Action: RecipeActionTypeDef
    ConditionExpressions: Optional[Sequence[ConditionExpressionTypeDef]] = None

class RedshiftTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str
    RedshiftTmpDir: Optional[str] = None
    TmpDirIAMRole: Optional[str] = None
    UpsertRedshiftOptions: Optional[UpsertRedshiftTargetOptionsExtraOutputTypeDef] = None

class RedshiftTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str
    RedshiftTmpDir: Optional[str] = None
    TmpDirIAMRole: Optional[str] = None
    UpsertRedshiftOptions: Optional[UpsertRedshiftTargetOptionsOutputTypeDef] = None

class RedshiftTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str
    RedshiftTmpDir: Optional[str] = None
    TmpDirIAMRole: Optional[str] = None
    UpsertRedshiftOptions: Optional[UpsertRedshiftTargetOptionsTypeDef] = None

class UserDefinedFunctionInputTypeDef(BaseModel):
    FunctionName: Optional[str] = None
    ClassName: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerType: Optional[PrincipalTypeType] = None
    ResourceUris: Optional[Sequence[ResourceUriTypeDef]] = None

class UserDefinedFunctionTypeDef(BaseModel):
    FunctionName: Optional[str] = None
    DatabaseName: Optional[str] = None
    ClassName: Optional[str] = None
    OwnerName: Optional[str] = None
    OwnerType: Optional[PrincipalTypeType] = None
    CreateTime: Optional[datetime] = None
    ResourceUris: Optional[List[ResourceUriTypeDef]] = None
    CatalogId: Optional[str] = None

class TableOptimizerRunTypeDef(BaseModel):
    eventType: Optional[TableOptimizerEventTypeType] = None
    startTimestamp: Optional[datetime] = None
    endTimestamp: Optional[datetime] = None
    metrics: Optional[RunMetricsTypeDef] = None
    error: Optional[str] = None

class SearchTablesRequestRequestTypeDef(BaseModel):
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[PropertyPredicateTypeDef]] = None
    SearchText: Optional[str] = None
    SortCriteria: Optional[Sequence[SortCriterionTypeDef]] = None
    MaxResults: Optional[int] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None

class StatementOutputTypeDef(BaseModel):
    Data: Optional[StatementOutputDataTypeDef] = None
    ExecutionCount: Optional[int] = None
    Status: Optional[StatementStateType] = None
    ErrorName: Optional[str] = None
    ErrorValue: Optional[str] = None
    Traceback: Optional[List[str]] = None

class UpdateClassifierRequestRequestTypeDef(BaseModel):
    GrokClassifier: Optional[UpdateGrokClassifierRequestTypeDef] = None
    XMLClassifier: Optional[UpdateXMLClassifierRequestTypeDef] = None
    JsonClassifier: Optional[UpdateJsonClassifierRequestTypeDef] = None
    CsvClassifier: Optional[UpdateCsvClassifierRequestTypeDef] = None

class ViewDefinitionInputTypeDef(BaseModel):
    IsProtected: Optional[bool] = None
    Definer: Optional[str] = None
    Representations: Optional[Sequence[ViewRepresentationInputTypeDef]] = None
    SubObjects: Optional[Sequence[str]] = None

class ViewDefinitionTypeDef(BaseModel):
    IsProtected: Optional[bool] = None
    Definer: Optional[str] = None
    SubObjects: Optional[List[str]] = None
    Representations: Optional[List[ViewRepresentationTypeDef]] = None

class AmazonRedshiftSourceExtraOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataExtraOutputTypeDef] = None

class AmazonRedshiftTargetExtraOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataExtraOutputTypeDef] = None
    Inputs: Optional[List[str]] = None

class AmazonRedshiftSourceOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataOutputTypeDef] = None

class AmazonRedshiftTargetOutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataOutputTypeDef] = None
    Inputs: Optional[List[str]] = None

class AmazonRedshiftSourceTypeDef(BaseModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataTypeDef] = None

class AmazonRedshiftTargetTypeDef(BaseModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataTypeDef] = None
    Inputs: Optional[Sequence[str]] = None

class SnowflakeTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Data: SnowflakeNodeDataExtraOutputTypeDef
    Inputs: Optional[List[str]] = None

class SnowflakeTargetOutputTypeDef(BaseModel):
    Name: str
    Data: SnowflakeNodeDataOutputTypeDef
    Inputs: Optional[List[str]] = None

class SnowflakeTargetTypeDef(BaseModel):
    Name: str
    Data: SnowflakeNodeDataTypeDef
    Inputs: Optional[Sequence[str]] = None

class PartitionIndexDescriptorTypeDef(BaseModel):
    IndexName: str
    Keys: List[KeySchemaElementTypeDef]
    IndexStatus: PartitionIndexStatusType
    BackfillErrors: Optional[List[BackfillErrorTypeDef]] = None

class BatchStopJobRunResponseTypeDef(BaseModel):
    SuccessfulSubmissions: List[BatchStopJobRunSuccessfulSubmissionTypeDef]
    Errors: List[BatchStopJobRunErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdatePartitionResponseTypeDef(BaseModel):
    Errors: List[BatchUpdatePartitionFailureEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreatePartitionResponseTypeDef(BaseModel):
    Errors: List[PartitionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeletePartitionResponseTypeDef(BaseModel):
    Errors: List[PartitionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteTableResponseTypeDef(BaseModel):
    Errors: List[TableErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteTableVersionResponseTypeDef(BaseModel):
    Errors: List[TableVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DecimalColumnStatisticsDataTypeDef(BaseModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[DecimalNumberTypeDef] = None
    MaximumValue: Optional[DecimalNumberTypeDef] = None

class BatchGetBlueprintsResponseTypeDef(BaseModel):
    Blueprints: List[BlueprintTypeDef]
    MissingBlueprints: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlueprintResponseTypeDef(BaseModel):
    Blueprint: BlueprintTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetClassifierResponseTypeDef(BaseModel):
    Classifier: ClassifierTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetClassifiersResponseTypeDef(BaseModel):
    Classifiers: List[ClassifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDataflowGraphResponseTypeDef(BaseModel):
    DagNodes: List[CodeGenNodeOutputTypeDef]
    DagEdges: List[CodeGenEdgeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMappingRequestRequestTypeDef(BaseModel):
    Source: CatalogEntryTypeDef
    Sinks: Optional[Sequence[CatalogEntryTypeDef]] = None
    Location: Optional[LocationTypeDef] = None

class GetPlanRequestRequestTypeDef(BaseModel):
    Mapping: Sequence[MappingEntryTypeDef]
    Source: CatalogEntryTypeDef
    Sinks: Optional[Sequence[CatalogEntryTypeDef]] = None
    Location: Optional[LocationTypeDef] = None
    Language: Optional[LanguageType] = None
    AdditionalPlanOptionsMap: Optional[Mapping[str, str]] = None

class CatalogKafkaSourceTypeDef(BaseModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KafkaStreamingSourceOptionsTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class DirectKafkaSourceTypeDef(BaseModel):
    Name: str
    StreamingOptions: Optional[KafkaStreamingSourceOptionsTypeDef] = None
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class CatalogKinesisSourceTypeDef(BaseModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class DirectKinesisSourceTypeDef(BaseModel):
    Name: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class GetUnfilteredPartitionMetadataRequestRequestTypeDef(BaseModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    SupportedPermissionTypes: Sequence[PermissionTypeType]
    Region: Optional[str] = None
    AuditContext: Optional[AuditContextTypeDef] = None
    QuerySessionContext: Optional[QuerySessionContextTypeDef] = None

class GetUnfilteredPartitionsMetadataRequestRequestTypeDef(BaseModel):
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

class GetUnfilteredTableMetadataRequestRequestTypeDef(BaseModel):
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

class GetMLTaskRunsRequestRequestTypeDef(BaseModel):
    TransformId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[TaskRunFilterCriteriaTypeDef] = None
    Sort: Optional[TaskRunSortCriteriaTypeDef] = None

class TriggerTypeDef(BaseModel):
    Name: Optional[str] = None
    WorkflowName: Optional[str] = None
    Id: Optional[str] = None
    Type: Optional[TriggerTypeType] = None
    State: Optional[TriggerStateType] = None
    Description: Optional[str] = None
    Schedule: Optional[str] = None
    Actions: Optional[List[ActionOutputTypeDef]] = None
    Predicate: Optional[PredicateOutputTypeDef] = None
    EventBatchingCondition: Optional[EventBatchingConditionTypeDef] = None

class TriggerUpdateTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Schedule: Optional[str] = None
    Actions: Optional[Sequence[ActionTypeDef]] = None
    Predicate: Optional[PredicateTypeDef] = None
    EventBatchingCondition: Optional[EventBatchingConditionTypeDef] = None

class GetUsageProfileResponseTypeDef(BaseModel):
    Name: str
    Description: str
    Configuration: ProfileConfigurationOutputTypeDef
    CreatedOn: datetime
    LastModifiedOn: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUsageProfileRequestRequestTypeDef(BaseModel):
    Name: str
    Configuration: ProfileConfigurationTypeDef
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateUsageProfileRequestRequestTypeDef(BaseModel):
    Name: str
    Configuration: ProfileConfigurationTypeDef
    Description: Optional[str] = None

class EvaluationMetricsTypeDef(BaseModel):
    TransformType: Literal["FIND_MATCHES"]
    FindMatchesMetrics: Optional[FindMatchesMetricsTypeDef] = None

class CrawlerTypeDef(BaseModel):
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

class CreateCrawlerRequestRequestTypeDef(BaseModel):
    Name: str
    Role: str
    Targets: CrawlerTargetsTypeDef
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

class UpdateCrawlerRequestRequestTypeDef(BaseModel):
    Name: str
    Role: Optional[str] = None
    DatabaseName: Optional[str] = None
    Description: Optional[str] = None
    Targets: Optional[CrawlerTargetsTypeDef] = None
    Schedule: Optional[str] = None
    Classifiers: Optional[Sequence[str]] = None
    TablePrefix: Optional[str] = None
    SchemaChangePolicy: Optional[SchemaChangePolicyTypeDef] = None
    RecrawlPolicy: Optional[RecrawlPolicyTypeDef] = None
    LineageConfiguration: Optional[LineageConfigurationTypeDef] = None
    LakeFormationConfiguration: Optional[LakeFormationConfigurationTypeDef] = None
    Configuration: Optional[str] = None
    CrawlerSecurityConfiguration: Optional[str] = None

class ListDataQualityRulesetsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[DataQualityRulesetFilterCriteriaTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class ListDataQualityRulesetsResponseTypeDef(BaseModel):
    Rulesets: List[DataQualityRulesetListDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateSessionResponseTypeDef(BaseModel):
    Session: SessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSessionResponseTypeDef(BaseModel):
    Session: SessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSessionsResponseTypeDef(BaseModel):
    Ids: List[str]
    Sessions: List[SessionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDataCatalogEncryptionSettingsResponseTypeDef(BaseModel):
    DataCatalogEncryptionSettings: DataCatalogEncryptionSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDataCatalogEncryptionSettingsRequestRequestTypeDef(BaseModel):
    DataCatalogEncryptionSettings: DataCatalogEncryptionSettingsTypeDef
    CatalogId: Optional[str] = None

class DatabaseTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    LocationUri: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None
    CreateTime: Optional[datetime] = None
    CreateTableDefaultPermissions: Optional[List[PrincipalPermissionsOutputTypeDef]] = None
    TargetDatabase: Optional[DatabaseIdentifierTypeDef] = None
    CatalogId: Optional[str] = None
    FederatedDatabase: Optional[FederatedDatabaseTypeDef] = None

class DatabaseInputTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    LocationUri: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    CreateTableDefaultPermissions: Optional[Sequence[PrincipalPermissionsTypeDef]] = None
    TargetDatabase: Optional[DatabaseIdentifierTypeDef] = None
    FederatedDatabase: Optional[FederatedDatabaseTypeDef] = None

class DataQualityObservationTypeDef(BaseModel):
    Description: Optional[str] = None
    MetricBasedObservation: Optional[MetricBasedObservationTypeDef] = None

class DataQualityResultDescriptionTypeDef(BaseModel):
    ResultId: Optional[str] = None
    DataSource: Optional[DataSourceOutputTypeDef] = None
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None
    StartedOn: Optional[datetime] = None

class DataQualityRuleRecommendationRunDescriptionTypeDef(BaseModel):
    RunId: Optional[str] = None
    Status: Optional[TaskStatusTypeType] = None
    StartedOn: Optional[datetime] = None
    DataSource: Optional[DataSourceOutputTypeDef] = None

class DataQualityRulesetEvaluationRunDescriptionTypeDef(BaseModel):
    RunId: Optional[str] = None
    Status: Optional[TaskStatusTypeType] = None
    StartedOn: Optional[datetime] = None
    DataSource: Optional[DataSourceOutputTypeDef] = None

class GetDataQualityRuleRecommendationRunResponseTypeDef(BaseModel):
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
    ResponseMetadata: ResponseMetadataTypeDef

class GetDataQualityRulesetEvaluationRunResponseTypeDef(BaseModel):
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

class DataQualityResultFilterCriteriaTypeDef(BaseModel):
    DataSource: Optional[DataSourceTypeDef] = None
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None
    StartedAfter: Optional[TimestampTypeDef] = None
    StartedBefore: Optional[TimestampTypeDef] = None

class DataQualityRuleRecommendationRunFilterTypeDef(BaseModel):
    DataSource: DataSourceTypeDef
    StartedBefore: Optional[TimestampTypeDef] = None
    StartedAfter: Optional[TimestampTypeDef] = None

class DataQualityRulesetEvaluationRunFilterTypeDef(BaseModel):
    DataSource: DataSourceTypeDef
    StartedBefore: Optional[TimestampTypeDef] = None
    StartedAfter: Optional[TimestampTypeDef] = None

class StartDataQualityRuleRecommendationRunRequestRequestTypeDef(BaseModel):
    DataSource: DataSourceTypeDef
    Role: str
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    CreatedRulesetName: Optional[str] = None
    ClientToken: Optional[str] = None

class DropNullFieldsExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    NullCheckBoxList: Optional[NullCheckBoxListTypeDef] = None
    NullTextList: Optional[List[NullValueFieldTypeDef]] = None

class DropNullFieldsOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    NullCheckBoxList: Optional[NullCheckBoxListTypeDef] = None
    NullTextList: Optional[List[NullValueFieldTypeDef]] = None

class DropNullFieldsTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    NullCheckBoxList: Optional[NullCheckBoxListTypeDef] = None
    NullTextList: Optional[Sequence[NullValueFieldTypeDef]] = None

class ColumnStatisticsDataOutputTypeDef(BaseModel):
    Type: ColumnStatisticsTypeType
    BooleanColumnStatisticsData: Optional[BooleanColumnStatisticsDataTypeDef] = None
    DateColumnStatisticsData: Optional[DateColumnStatisticsDataOutputTypeDef] = None
    DecimalColumnStatisticsData: Optional[DecimalColumnStatisticsDataOutputTypeDef] = None
    DoubleColumnStatisticsData: Optional[DoubleColumnStatisticsDataTypeDef] = None
    LongColumnStatisticsData: Optional[LongColumnStatisticsDataTypeDef] = None
    StringColumnStatisticsData: Optional[StringColumnStatisticsDataTypeDef] = None
    BinaryColumnStatisticsData: Optional[BinaryColumnStatisticsDataTypeDef] = None

class StorageDescriptorOutputTypeDef(BaseModel):
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

class StorageDescriptorTypeDef(BaseModel):
    Columns: Optional[Sequence[ColumnTypeDef]] = None
    Location: Optional[str] = None
    AdditionalLocations: Optional[Sequence[str]] = None
    InputFormat: Optional[str] = None
    OutputFormat: Optional[str] = None
    Compressed: Optional[bool] = None
    NumberOfBuckets: Optional[int] = None
    SerdeInfo: Optional[SerDeInfoTypeDef] = None
    BucketColumns: Optional[Sequence[str]] = None
    SortColumns: Optional[Sequence[OrderTypeDef]] = None
    Parameters: Optional[Mapping[str, str]] = None
    SkewedInfo: Optional[SkewedInfoTypeDef] = None
    StoredAsSubDirectories: Optional[bool] = None
    SchemaReference: Optional[SchemaReferenceTypeDef] = None

class SecurityConfigurationTypeDef(BaseModel):
    Name: Optional[str] = None
    CreatedTimeStamp: Optional[datetime] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationOutputTypeDef] = None

class CreateSecurityConfigurationRequestRequestTypeDef(BaseModel):
    Name: str
    EncryptionConfiguration: EncryptionConfigurationTypeDef

class DeleteSchemaVersionsResponseTypeDef(BaseModel):
    SchemaVersionErrors: List[SchemaVersionErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FilterExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    LogicalOperator: FilterLogicalOperatorType
    Filters: List[FilterExpressionExtraOutputTypeDef]

class FilterOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    LogicalOperator: FilterLogicalOperatorType
    Filters: List[FilterExpressionOutputTypeDef]

class FilterTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    LogicalOperator: FilterLogicalOperatorType
    Filters: Sequence[FilterExpressionTypeDef]

class UpdateMLTransformRequestRequestTypeDef(BaseModel):
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

class GetMLTransformsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[TransformFilterCriteriaTypeDef] = None
    Sort: Optional[TransformSortCriteriaTypeDef] = None

class ListMLTransformsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[TransformFilterCriteriaTypeDef] = None
    Sort: Optional[TransformSortCriteriaTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class AthenaConnectorSourceExtraOutputTypeDef(BaseModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    SchemaName: str
    ConnectionTable: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class CatalogDeltaSourceExtraOutputTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class CatalogHudiSourceExtraOutputTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class ConnectorDataSourceExtraOutputTypeDef(BaseModel):
    Name: str
    ConnectionType: str
    Data: Dict[str, str]
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class CustomCodeExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Code: str
    ClassName: str
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class DynamicTransformExtraOutputTypeDef(BaseModel):
    Name: str
    TransformName: str
    Inputs: List[str]
    FunctionName: str
    Path: str
    Parameters: Optional[List[TransformConfigParameterExtraOutputTypeDef]] = None
    Version: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class JDBCConnectorSourceExtraOutputTypeDef(BaseModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[JDBCConnectorOptionsExtraOutputTypeDef] = None
    ConnectionTable: Optional[str] = None
    Query: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class JDBCConnectorTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    ConnectionName: str
    ConnectionTable: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class S3CatalogDeltaSourceExtraOutputTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class S3CatalogHudiSourceExtraOutputTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class S3CsvSourceExtraOutputTypeDef(BaseModel):
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
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class S3DeltaSourceExtraOutputTypeDef(BaseModel):
    Name: str
    Paths: List[str]
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class S3HudiSourceExtraOutputTypeDef(BaseModel):
    Name: str
    Paths: List[str]
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class S3JsonSourceExtraOutputTypeDef(BaseModel):
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
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class S3ParquetSourceExtraOutputTypeDef(BaseModel):
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
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class SnowflakeSourceExtraOutputTypeDef(BaseModel):
    Name: str
    Data: SnowflakeNodeDataExtraOutputTypeDef
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class SparkConnectorSourceExtraOutputTypeDef(BaseModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class SparkConnectorTargetExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class SparkSQLExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    SqlQuery: str
    SqlAliases: List[SqlAliasTypeDef]
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class AthenaConnectorSourceOutputTypeDef(BaseModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    SchemaName: str
    ConnectionTable: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class CatalogDeltaSourceOutputTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class CatalogHudiSourceOutputTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class ConnectorDataSourceOutputTypeDef(BaseModel):
    Name: str
    ConnectionType: str
    Data: Dict[str, str]
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class CustomCodeOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    Code: str
    ClassName: str
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class DynamicTransformOutputTypeDef(BaseModel):
    Name: str
    TransformName: str
    Inputs: List[str]
    FunctionName: str
    Path: str
    Parameters: Optional[List[TransformConfigParameterOutputTypeDef]] = None
    Version: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class JDBCConnectorSourceOutputTypeDef(BaseModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[JDBCConnectorOptionsOutputTypeDef] = None
    ConnectionTable: Optional[str] = None
    Query: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class JDBCConnectorTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    ConnectionName: str
    ConnectionTable: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class S3CatalogDeltaSourceOutputTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class S3CatalogHudiSourceOutputTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class S3CsvSourceOutputTypeDef(BaseModel):
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

class S3DeltaSourceOutputTypeDef(BaseModel):
    Name: str
    Paths: List[str]
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class S3HudiSourceOutputTypeDef(BaseModel):
    Name: str
    Paths: List[str]
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class S3JsonSourceOutputTypeDef(BaseModel):
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

class S3ParquetSourceOutputTypeDef(BaseModel):
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

class SnowflakeSourceOutputTypeDef(BaseModel):
    Name: str
    Data: SnowflakeNodeDataOutputTypeDef
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class SparkConnectorSourceOutputTypeDef(BaseModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class SparkConnectorTargetOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class SparkSQLOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    SqlQuery: str
    SqlAliases: List[SqlAliasTypeDef]
    OutputSchemas: Optional[List[GlueSchemaOutputTypeDef]] = None

class AthenaConnectorSourceTypeDef(BaseModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    SchemaName: str
    ConnectionTable: Optional[str] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class CatalogDeltaSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class CatalogHudiSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class ConnectorDataSourceTypeDef(BaseModel):
    Name: str
    ConnectionType: str
    Data: Mapping[str, str]
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class CustomCodeTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    Code: str
    ClassName: str
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class DynamicTransformTypeDef(BaseModel):
    Name: str
    TransformName: str
    Inputs: Sequence[str]
    FunctionName: str
    Path: str
    Parameters: Optional[Sequence[TransformConfigParameterTypeDef]] = None
    Version: Optional[str] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class JDBCConnectorSourceTypeDef(BaseModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[JDBCConnectorOptionsTypeDef] = None
    ConnectionTable: Optional[str] = None
    Query: Optional[str] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class JDBCConnectorTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    ConnectionName: str
    ConnectionTable: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class S3CatalogDeltaSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class S3CatalogHudiSourceTypeDef(BaseModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class S3CsvSourceTypeDef(BaseModel):
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

class S3DeltaSourceTypeDef(BaseModel):
    Name: str
    Paths: Sequence[str]
    AdditionalDeltaOptions: Optional[Mapping[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class S3HudiSourceTypeDef(BaseModel):
    Name: str
    Paths: Sequence[str]
    AdditionalHudiOptions: Optional[Mapping[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class S3JsonSourceTypeDef(BaseModel):
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

class S3ParquetSourceTypeDef(BaseModel):
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

class SnowflakeSourceTypeDef(BaseModel):
    Name: str
    Data: SnowflakeNodeDataTypeDef
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class SparkConnectorSourceTypeDef(BaseModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class SparkConnectorTargetTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Mapping[str, str]] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class SparkSQLTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    SqlQuery: str
    SqlAliases: Sequence[SqlAliasTypeDef]
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class GetJobRunResponseTypeDef(BaseModel):
    JobRun: JobRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobRunsResponseTypeDef(BaseModel):
    JobRuns: List[JobRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class JobNodeDetailsTypeDef(BaseModel):
    JobRuns: Optional[List[JobRunTypeDef]] = None

class GetMLTaskRunResponseTypeDef(BaseModel):
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

class TaskRunTypeDef(BaseModel):
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

class CreateMLTransformRequestRequestTypeDef(BaseModel):
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

class QuerySchemaVersionMetadataResponseTypeDef(BaseModel):
    MetadataInfoMap: Dict[str, MetadataInfoTypeDef]
    SchemaVersionId: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AuthenticationConfigurationInputTypeDef(BaseModel):
    AuthenticationType: Optional[AuthenticationTypeType] = None
    SecretArn: Optional[str] = None
    OAuth2Properties: Optional[OAuth2PropertiesInputTypeDef] = None

class AuthenticationConfigurationTypeDef(BaseModel):
    AuthenticationType: Optional[AuthenticationTypeType] = None
    SecretArn: Optional[str] = None
    OAuth2Properties: Optional[OAuth2PropertiesTypeDef] = None

class BatchDeletePartitionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    PartitionsToDelete: Sequence[PartitionValueListUnionTypeDef]
    CatalogId: Optional[str] = None

class BatchGetPartitionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    PartitionsToGet: Sequence[PartitionValueListUnionTypeDef]
    CatalogId: Optional[str] = None

class RecipeExtraOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    RecipeSteps: Optional[List[RecipeStepExtraOutputTypeDef]] = None

class RecipeOutputTypeDef(BaseModel):
    Name: str
    Inputs: List[str]
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    RecipeSteps: Optional[List[RecipeStepOutputTypeDef]] = None

class RecipeTypeDef(BaseModel):
    Name: str
    Inputs: Sequence[str]
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    RecipeSteps: Optional[Sequence[RecipeStepTypeDef]] = None

class CreateUserDefinedFunctionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    FunctionInput: UserDefinedFunctionInputTypeDef
    CatalogId: Optional[str] = None

class UpdateUserDefinedFunctionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    FunctionName: str
    FunctionInput: UserDefinedFunctionInputTypeDef
    CatalogId: Optional[str] = None

class GetUserDefinedFunctionResponseTypeDef(BaseModel):
    UserDefinedFunction: UserDefinedFunctionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserDefinedFunctionsResponseTypeDef(BaseModel):
    UserDefinedFunctions: List[UserDefinedFunctionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTableOptimizerRunsResponseTypeDef(BaseModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    TableOptimizerRuns: List[TableOptimizerRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TableOptimizerTypeDef(BaseModel):
    type: Optional[Literal["compaction"]] = None
    configuration: Optional[TableOptimizerConfigurationTypeDef] = None
    lastRun: Optional[TableOptimizerRunTypeDef] = None

class StatementTypeDef(BaseModel):
    Id: Optional[int] = None
    Code: Optional[str] = None
    State: Optional[StatementStateType] = None
    Output: Optional[StatementOutputTypeDef] = None
    Progress: Optional[float] = None
    StartedOn: Optional[int] = None
    CompletedOn: Optional[int] = None

class CreateTriggerRequestRequestTypeDef(BaseModel):
    Name: str
    Type: TriggerTypeType
    Actions: Sequence[ActionUnionTypeDef]
    WorkflowName: Optional[str] = None
    Schedule: Optional[str] = None
    Predicate: Optional[PredicateTypeDef] = None
    Description: Optional[str] = None
    StartOnCreation: Optional[bool] = None
    Tags: Optional[Mapping[str, str]] = None
    EventBatchingCondition: Optional[EventBatchingConditionTypeDef] = None

class GetPartitionIndexesResponseTypeDef(BaseModel):
    PartitionIndexDescriptorList: List[PartitionIndexDescriptorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ColumnStatisticsDataTypeDef(BaseModel):
    Type: ColumnStatisticsTypeType
    BooleanColumnStatisticsData: Optional[BooleanColumnStatisticsDataTypeDef] = None
    DateColumnStatisticsData: Optional[DateColumnStatisticsDataTypeDef] = None
    DecimalColumnStatisticsData: Optional[DecimalColumnStatisticsDataTypeDef] = None
    DoubleColumnStatisticsData: Optional[DoubleColumnStatisticsDataTypeDef] = None
    LongColumnStatisticsData: Optional[LongColumnStatisticsDataTypeDef] = None
    StringColumnStatisticsData: Optional[StringColumnStatisticsDataTypeDef] = None
    BinaryColumnStatisticsData: Optional[BinaryColumnStatisticsDataTypeDef] = None

class CreateScriptRequestRequestTypeDef(BaseModel):
    DagNodes: Optional[Sequence[CodeGenNodeUnionTypeDef]] = None
    DagEdges: Optional[Sequence[CodeGenEdgeTypeDef]] = None
    Language: Optional[LanguageType] = None

class BatchGetTriggersResponseTypeDef(BaseModel):
    Triggers: List[TriggerTypeDef]
    TriggersNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetTriggerResponseTypeDef(BaseModel):
    Trigger: TriggerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTriggersResponseTypeDef(BaseModel):
    Triggers: List[TriggerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TriggerNodeDetailsTypeDef(BaseModel):
    Trigger: Optional[TriggerTypeDef] = None

class UpdateTriggerResponseTypeDef(BaseModel):
    Trigger: TriggerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTriggerRequestRequestTypeDef(BaseModel):
    Name: str
    TriggerUpdate: TriggerUpdateTypeDef

class GetMLTransformResponseTypeDef(BaseModel):
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

class MLTransformTypeDef(BaseModel):
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

class BatchGetCrawlersResponseTypeDef(BaseModel):
    Crawlers: List[CrawlerTypeDef]
    CrawlersNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetCrawlerResponseTypeDef(BaseModel):
    Crawler: CrawlerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetCrawlersResponseTypeDef(BaseModel):
    Crawlers: List[CrawlerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetDatabaseResponseTypeDef(BaseModel):
    Database: DatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDatabasesResponseTypeDef(BaseModel):
    DatabaseList: List[DatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateDatabaseRequestRequestTypeDef(BaseModel):
    DatabaseInput: DatabaseInputTypeDef
    CatalogId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateDatabaseRequestRequestTypeDef(BaseModel):
    Name: str
    DatabaseInput: DatabaseInputTypeDef
    CatalogId: Optional[str] = None

class DataQualityResultTypeDef(BaseModel):
    ResultId: Optional[str] = None
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

class GetDataQualityResultResponseTypeDef(BaseModel):
    ResultId: str
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

class ListDataQualityResultsResponseTypeDef(BaseModel):
    Results: List[DataQualityResultDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDataQualityRuleRecommendationRunsResponseTypeDef(BaseModel):
    Runs: List[DataQualityRuleRecommendationRunDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDataQualityRulesetEvaluationRunsResponseTypeDef(BaseModel):
    Runs: List[DataQualityRulesetEvaluationRunDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListDataQualityResultsRequestRequestTypeDef(BaseModel):
    Filter: Optional[DataQualityResultFilterCriteriaTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataQualityRuleRecommendationRunsRequestRequestTypeDef(BaseModel):
    Filter: Optional[DataQualityRuleRecommendationRunFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataQualityRulesetEvaluationRunsRequestRequestTypeDef(BaseModel):
    Filter: Optional[DataQualityRulesetEvaluationRunFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class StartDataQualityRulesetEvaluationRunRequestRequestTypeDef(BaseModel):
    DataSource: DataSourceTypeDef
    Role: str
    RulesetNames: Sequence[str]
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    ClientToken: Optional[str] = None
    AdditionalRunOptions: Optional[DataQualityEvaluationRunAdditionalRunOptionsTypeDef] = None
    AdditionalDataSources: Optional[Mapping[str, DataSourceUnionTypeDef]] = None

class ColumnStatisticsOutputTypeDef(BaseModel):
    ColumnName: str
    ColumnType: str
    AnalyzedTime: datetime
    StatisticsData: ColumnStatisticsDataOutputTypeDef

class PartitionTypeDef(BaseModel):
    Values: Optional[List[str]] = None
    DatabaseName: Optional[str] = None
    TableName: Optional[str] = None
    CreationTime: Optional[datetime] = None
    LastAccessTime: Optional[datetime] = None
    StorageDescriptor: Optional[StorageDescriptorOutputTypeDef] = None
    Parameters: Optional[Dict[str, str]] = None
    LastAnalyzedTime: Optional[datetime] = None
    CatalogId: Optional[str] = None

class TableTypeDef(BaseModel):
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

class PartitionInputTypeDef(BaseModel):
    Values: Optional[Sequence[str]] = None
    LastAccessTime: Optional[TimestampTypeDef] = None
    StorageDescriptor: Optional[StorageDescriptorTypeDef] = None
    Parameters: Optional[Mapping[str, str]] = None
    LastAnalyzedTime: Optional[TimestampTypeDef] = None

class TableInputTypeDef(BaseModel):
    Name: str
    Description: Optional[str] = None
    Owner: Optional[str] = None
    LastAccessTime: Optional[TimestampTypeDef] = None
    LastAnalyzedTime: Optional[TimestampTypeDef] = None
    Retention: Optional[int] = None
    StorageDescriptor: Optional[StorageDescriptorTypeDef] = None
    PartitionKeys: Optional[Sequence[ColumnTypeDef]] = None
    ViewOriginalText: Optional[str] = None
    ViewExpandedText: Optional[str] = None
    TableType: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    TargetTable: Optional[TableIdentifierTypeDef] = None
    ViewDefinition: Optional[ViewDefinitionInputTypeDef] = None

class GetSecurityConfigurationResponseTypeDef(BaseModel):
    SecurityConfiguration: SecurityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSecurityConfigurationsResponseTypeDef(BaseModel):
    SecurityConfigurations: List[SecurityConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetMLTaskRunsResponseTypeDef(BaseModel):
    TaskRuns: List[TaskRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ConnectionInputTypeDef(BaseModel):
    Name: str
    ConnectionType: ConnectionTypeType
    ConnectionProperties: Mapping[ConnectionPropertyKeyType, str]
    Description: Optional[str] = None
    MatchCriteria: Optional[Sequence[str]] = None
    PhysicalConnectionRequirements: Optional[PhysicalConnectionRequirementsTypeDef] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationInputTypeDef] = None
    ValidateCredentials: Optional[bool] = None

class ConnectionTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    ConnectionType: Optional[ConnectionTypeType] = None
    MatchCriteria: Optional[List[str]] = None
    ConnectionProperties: Optional[Dict[ConnectionPropertyKeyType, str]] = None
    PhysicalConnectionRequirements: Optional[PhysicalConnectionRequirementsOutputTypeDef] = None
    CreationTime: Optional[datetime] = None
    LastUpdatedTime: Optional[datetime] = None
    LastUpdatedBy: Optional[str] = None
    Status: Optional[ConnectionStatusType] = None
    StatusReason: Optional[str] = None
    LastConnectionValidationTime: Optional[datetime] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationTypeDef] = None

class CodeGenConfigurationNodeExtraOutputTypeDef(BaseModel):
    AthenaConnectorSource: Optional[AthenaConnectorSourceExtraOutputTypeDef] = None
    JDBCConnectorSource: Optional[JDBCConnectorSourceExtraOutputTypeDef] = None
    SparkConnectorSource: Optional[SparkConnectorSourceExtraOutputTypeDef] = None
    CatalogSource: Optional[CatalogSourceTypeDef] = None
    RedshiftSource: Optional[RedshiftSourceTypeDef] = None
    S3CatalogSource: Optional[S3CatalogSourceTypeDef] = None
    S3CsvSource: Optional[S3CsvSourceExtraOutputTypeDef] = None
    S3JsonSource: Optional[S3JsonSourceExtraOutputTypeDef] = None
    S3ParquetSource: Optional[S3ParquetSourceExtraOutputTypeDef] = None
    RelationalCatalogSource: Optional[RelationalCatalogSourceTypeDef] = None
    DynamoDBCatalogSource: Optional[DynamoDBCatalogSourceTypeDef] = None
    JDBCConnectorTarget: Optional[JDBCConnectorTargetExtraOutputTypeDef] = None
    SparkConnectorTarget: Optional[SparkConnectorTargetExtraOutputTypeDef] = None
    CatalogTarget: Optional[BasicCatalogTargetExtraOutputTypeDef] = None
    RedshiftTarget: Optional[RedshiftTargetExtraOutputTypeDef] = None
    S3CatalogTarget: Optional[S3CatalogTargetExtraOutputTypeDef] = None
    S3GlueParquetTarget: Optional[S3GlueParquetTargetExtraOutputTypeDef] = None
    S3DirectTarget: Optional[S3DirectTargetExtraOutputTypeDef] = None
    ApplyMapping: Optional[ApplyMappingExtraOutputTypeDef] = None
    SelectFields: Optional[SelectFieldsExtraOutputTypeDef] = None
    DropFields: Optional[DropFieldsExtraOutputTypeDef] = None
    RenameField: Optional[RenameFieldExtraOutputTypeDef] = None
    Spigot: Optional[SpigotExtraOutputTypeDef] = None
    Join: Optional[JoinExtraOutputTypeDef] = None
    SplitFields: Optional[SplitFieldsExtraOutputTypeDef] = None
    SelectFromCollection: Optional[SelectFromCollectionExtraOutputTypeDef] = None
    FillMissingValues: Optional[FillMissingValuesExtraOutputTypeDef] = None
    Filter: Optional[FilterExtraOutputTypeDef] = None
    CustomCode: Optional[CustomCodeExtraOutputTypeDef] = None
    SparkSQL: Optional[SparkSQLExtraOutputTypeDef] = None
    DirectKinesisSource: Optional[DirectKinesisSourceExtraOutputTypeDef] = None
    DirectKafkaSource: Optional[DirectKafkaSourceExtraOutputTypeDef] = None
    CatalogKinesisSource: Optional[CatalogKinesisSourceExtraOutputTypeDef] = None
    CatalogKafkaSource: Optional[CatalogKafkaSourceExtraOutputTypeDef] = None
    DropNullFields: Optional[DropNullFieldsExtraOutputTypeDef] = None
    Merge: Optional[MergeExtraOutputTypeDef] = None
    Union: Optional[UnionExtraOutputTypeDef] = None
    PIIDetection: Optional[PIIDetectionExtraOutputTypeDef] = None
    Aggregate: Optional[AggregateExtraOutputTypeDef] = None
    DropDuplicates: Optional[DropDuplicatesExtraOutputTypeDef] = None
    GovernedCatalogTarget: Optional[GovernedCatalogTargetExtraOutputTypeDef] = None
    GovernedCatalogSource: Optional[GovernedCatalogSourceTypeDef] = None
    MicrosoftSQLServerCatalogSource: Optional[MicrosoftSQLServerCatalogSourceTypeDef] = None
    MySQLCatalogSource: Optional[MySQLCatalogSourceTypeDef] = None
    OracleSQLCatalogSource: Optional[OracleSQLCatalogSourceTypeDef] = None
    PostgreSQLCatalogSource: Optional[PostgreSQLCatalogSourceTypeDef] = None
    MicrosoftSQLServerCatalogTarget: Optional[       MicrosoftSQLServerCatalogTargetExtraOutputTypeDef     ] = None
    MySQLCatalogTarget: Optional[MySQLCatalogTargetExtraOutputTypeDef] = None
    OracleSQLCatalogTarget: Optional[OracleSQLCatalogTargetExtraOutputTypeDef] = None
    PostgreSQLCatalogTarget: Optional[PostgreSQLCatalogTargetExtraOutputTypeDef] = None
    DynamicTransform: Optional[DynamicTransformExtraOutputTypeDef] = None
    EvaluateDataQuality: Optional[EvaluateDataQualityExtraOutputTypeDef] = None
    S3CatalogHudiSource: Optional[S3CatalogHudiSourceExtraOutputTypeDef] = None
    CatalogHudiSource: Optional[CatalogHudiSourceExtraOutputTypeDef] = None
    S3HudiSource: Optional[S3HudiSourceExtraOutputTypeDef] = None
    S3HudiCatalogTarget: Optional[S3HudiCatalogTargetExtraOutputTypeDef] = None
    S3HudiDirectTarget: Optional[S3HudiDirectTargetExtraOutputTypeDef] = None
    DirectJDBCSource: Optional[DirectJDBCSourceTypeDef] = None
    S3CatalogDeltaSource: Optional[S3CatalogDeltaSourceExtraOutputTypeDef] = None
    CatalogDeltaSource: Optional[CatalogDeltaSourceExtraOutputTypeDef] = None
    S3DeltaSource: Optional[S3DeltaSourceExtraOutputTypeDef] = None
    S3DeltaCatalogTarget: Optional[S3DeltaCatalogTargetExtraOutputTypeDef] = None
    S3DeltaDirectTarget: Optional[S3DeltaDirectTargetExtraOutputTypeDef] = None
    AmazonRedshiftSource: Optional[AmazonRedshiftSourceExtraOutputTypeDef] = None
    AmazonRedshiftTarget: Optional[AmazonRedshiftTargetExtraOutputTypeDef] = None
    EvaluateDataQualityMultiFrame: Optional[       EvaluateDataQualityMultiFrameExtraOutputTypeDef     ] = None
    Recipe: Optional[RecipeExtraOutputTypeDef] = None
    SnowflakeSource: Optional[SnowflakeSourceExtraOutputTypeDef] = None
    SnowflakeTarget: Optional[SnowflakeTargetExtraOutputTypeDef] = None
    ConnectorDataSource: Optional[ConnectorDataSourceExtraOutputTypeDef] = None
    ConnectorDataTarget: Optional[ConnectorDataTargetExtraOutputTypeDef] = None

class CodeGenConfigurationNodeOutputTypeDef(BaseModel):
    AthenaConnectorSource: Optional[AthenaConnectorSourceOutputTypeDef] = None
    JDBCConnectorSource: Optional[JDBCConnectorSourceOutputTypeDef] = None
    SparkConnectorSource: Optional[SparkConnectorSourceOutputTypeDef] = None
    CatalogSource: Optional[CatalogSourceTypeDef] = None
    RedshiftSource: Optional[RedshiftSourceTypeDef] = None
    S3CatalogSource: Optional[S3CatalogSourceTypeDef] = None
    S3CsvSource: Optional[S3CsvSourceOutputTypeDef] = None
    S3JsonSource: Optional[S3JsonSourceOutputTypeDef] = None
    S3ParquetSource: Optional[S3ParquetSourceOutputTypeDef] = None
    RelationalCatalogSource: Optional[RelationalCatalogSourceTypeDef] = None
    DynamoDBCatalogSource: Optional[DynamoDBCatalogSourceTypeDef] = None
    JDBCConnectorTarget: Optional[JDBCConnectorTargetOutputTypeDef] = None
    SparkConnectorTarget: Optional[SparkConnectorTargetOutputTypeDef] = None
    CatalogTarget: Optional[BasicCatalogTargetOutputTypeDef] = None
    RedshiftTarget: Optional[RedshiftTargetOutputTypeDef] = None
    S3CatalogTarget: Optional[S3CatalogTargetOutputTypeDef] = None
    S3GlueParquetTarget: Optional[S3GlueParquetTargetOutputTypeDef] = None
    S3DirectTarget: Optional[S3DirectTargetOutputTypeDef] = None
    ApplyMapping: Optional[ApplyMappingOutputTypeDef] = None
    SelectFields: Optional[SelectFieldsOutputTypeDef] = None
    DropFields: Optional[DropFieldsOutputTypeDef] = None
    RenameField: Optional[RenameFieldOutputTypeDef] = None
    Spigot: Optional[SpigotOutputTypeDef] = None
    Join: Optional[JoinOutputTypeDef] = None
    SplitFields: Optional[SplitFieldsOutputTypeDef] = None
    SelectFromCollection: Optional[SelectFromCollectionOutputTypeDef] = None
    FillMissingValues: Optional[FillMissingValuesOutputTypeDef] = None
    Filter: Optional[FilterOutputTypeDef] = None
    CustomCode: Optional[CustomCodeOutputTypeDef] = None
    SparkSQL: Optional[SparkSQLOutputTypeDef] = None
    DirectKinesisSource: Optional[DirectKinesisSourceOutputTypeDef] = None
    DirectKafkaSource: Optional[DirectKafkaSourceOutputTypeDef] = None
    CatalogKinesisSource: Optional[CatalogKinesisSourceOutputTypeDef] = None
    CatalogKafkaSource: Optional[CatalogKafkaSourceOutputTypeDef] = None
    DropNullFields: Optional[DropNullFieldsOutputTypeDef] = None
    Merge: Optional[MergeOutputTypeDef] = None
    Union: Optional[UnionOutputTypeDef] = None
    PIIDetection: Optional[PIIDetectionOutputTypeDef] = None
    Aggregate: Optional[AggregateOutputTypeDef] = None
    DropDuplicates: Optional[DropDuplicatesOutputTypeDef] = None
    GovernedCatalogTarget: Optional[GovernedCatalogTargetOutputTypeDef] = None
    GovernedCatalogSource: Optional[GovernedCatalogSourceTypeDef] = None
    MicrosoftSQLServerCatalogSource: Optional[MicrosoftSQLServerCatalogSourceTypeDef] = None
    MySQLCatalogSource: Optional[MySQLCatalogSourceTypeDef] = None
    OracleSQLCatalogSource: Optional[OracleSQLCatalogSourceTypeDef] = None
    PostgreSQLCatalogSource: Optional[PostgreSQLCatalogSourceTypeDef] = None
    MicrosoftSQLServerCatalogTarget: Optional[       MicrosoftSQLServerCatalogTargetOutputTypeDef     ] = None
    MySQLCatalogTarget: Optional[MySQLCatalogTargetOutputTypeDef] = None
    OracleSQLCatalogTarget: Optional[OracleSQLCatalogTargetOutputTypeDef] = None
    PostgreSQLCatalogTarget: Optional[PostgreSQLCatalogTargetOutputTypeDef] = None
    DynamicTransform: Optional[DynamicTransformOutputTypeDef] = None
    EvaluateDataQuality: Optional[EvaluateDataQualityOutputTypeDef] = None
    S3CatalogHudiSource: Optional[S3CatalogHudiSourceOutputTypeDef] = None
    CatalogHudiSource: Optional[CatalogHudiSourceOutputTypeDef] = None
    S3HudiSource: Optional[S3HudiSourceOutputTypeDef] = None
    S3HudiCatalogTarget: Optional[S3HudiCatalogTargetOutputTypeDef] = None
    S3HudiDirectTarget: Optional[S3HudiDirectTargetOutputTypeDef] = None
    DirectJDBCSource: Optional[DirectJDBCSourceTypeDef] = None
    S3CatalogDeltaSource: Optional[S3CatalogDeltaSourceOutputTypeDef] = None
    CatalogDeltaSource: Optional[CatalogDeltaSourceOutputTypeDef] = None
    S3DeltaSource: Optional[S3DeltaSourceOutputTypeDef] = None
    S3DeltaCatalogTarget: Optional[S3DeltaCatalogTargetOutputTypeDef] = None
    S3DeltaDirectTarget: Optional[S3DeltaDirectTargetOutputTypeDef] = None
    AmazonRedshiftSource: Optional[AmazonRedshiftSourceOutputTypeDef] = None
    AmazonRedshiftTarget: Optional[AmazonRedshiftTargetOutputTypeDef] = None
    EvaluateDataQualityMultiFrame: Optional[EvaluateDataQualityMultiFrameOutputTypeDef] = None
    Recipe: Optional[RecipeOutputTypeDef] = None
    SnowflakeSource: Optional[SnowflakeSourceOutputTypeDef] = None
    SnowflakeTarget: Optional[SnowflakeTargetOutputTypeDef] = None
    ConnectorDataSource: Optional[ConnectorDataSourceOutputTypeDef] = None
    ConnectorDataTarget: Optional[ConnectorDataTargetOutputTypeDef] = None

class CodeGenConfigurationNodeTypeDef(BaseModel):
    AthenaConnectorSource: Optional[AthenaConnectorSourceTypeDef] = None
    JDBCConnectorSource: Optional[JDBCConnectorSourceTypeDef] = None
    SparkConnectorSource: Optional[SparkConnectorSourceTypeDef] = None
    CatalogSource: Optional[CatalogSourceTypeDef] = None
    RedshiftSource: Optional[RedshiftSourceTypeDef] = None
    S3CatalogSource: Optional[S3CatalogSourceTypeDef] = None
    S3CsvSource: Optional[S3CsvSourceTypeDef] = None
    S3JsonSource: Optional[S3JsonSourceTypeDef] = None
    S3ParquetSource: Optional[S3ParquetSourceTypeDef] = None
    RelationalCatalogSource: Optional[RelationalCatalogSourceTypeDef] = None
    DynamoDBCatalogSource: Optional[DynamoDBCatalogSourceTypeDef] = None
    JDBCConnectorTarget: Optional[JDBCConnectorTargetTypeDef] = None
    SparkConnectorTarget: Optional[SparkConnectorTargetTypeDef] = None
    CatalogTarget: Optional[BasicCatalogTargetTypeDef] = None
    RedshiftTarget: Optional[RedshiftTargetTypeDef] = None
    S3CatalogTarget: Optional[S3CatalogTargetTypeDef] = None
    S3GlueParquetTarget: Optional[S3GlueParquetTargetTypeDef] = None
    S3DirectTarget: Optional[S3DirectTargetTypeDef] = None
    ApplyMapping: Optional[ApplyMappingTypeDef] = None
    SelectFields: Optional[SelectFieldsTypeDef] = None
    DropFields: Optional[DropFieldsTypeDef] = None
    RenameField: Optional[RenameFieldTypeDef] = None
    Spigot: Optional[SpigotTypeDef] = None
    Join: Optional[JoinTypeDef] = None
    SplitFields: Optional[SplitFieldsTypeDef] = None
    SelectFromCollection: Optional[SelectFromCollectionTypeDef] = None
    FillMissingValues: Optional[FillMissingValuesTypeDef] = None
    Filter: Optional[FilterTypeDef] = None
    CustomCode: Optional[CustomCodeTypeDef] = None
    SparkSQL: Optional[SparkSQLTypeDef] = None
    DirectKinesisSource: Optional[DirectKinesisSourceTypeDef] = None
    DirectKafkaSource: Optional[DirectKafkaSourceTypeDef] = None
    CatalogKinesisSource: Optional[CatalogKinesisSourceTypeDef] = None
    CatalogKafkaSource: Optional[CatalogKafkaSourceTypeDef] = None
    DropNullFields: Optional[DropNullFieldsTypeDef] = None
    Merge: Optional[MergeTypeDef] = None
    Union: Optional[UnionTypeDef] = None
    PIIDetection: Optional[PIIDetectionTypeDef] = None
    Aggregate: Optional[AggregateTypeDef] = None
    DropDuplicates: Optional[DropDuplicatesTypeDef] = None
    GovernedCatalogTarget: Optional[GovernedCatalogTargetTypeDef] = None
    GovernedCatalogSource: Optional[GovernedCatalogSourceTypeDef] = None
    MicrosoftSQLServerCatalogSource: Optional[MicrosoftSQLServerCatalogSourceTypeDef] = None
    MySQLCatalogSource: Optional[MySQLCatalogSourceTypeDef] = None
    OracleSQLCatalogSource: Optional[OracleSQLCatalogSourceTypeDef] = None
    PostgreSQLCatalogSource: Optional[PostgreSQLCatalogSourceTypeDef] = None
    MicrosoftSQLServerCatalogTarget: Optional[MicrosoftSQLServerCatalogTargetTypeDef] = None
    MySQLCatalogTarget: Optional[MySQLCatalogTargetTypeDef] = None
    OracleSQLCatalogTarget: Optional[OracleSQLCatalogTargetTypeDef] = None
    PostgreSQLCatalogTarget: Optional[PostgreSQLCatalogTargetTypeDef] = None
    DynamicTransform: Optional[DynamicTransformTypeDef] = None
    EvaluateDataQuality: Optional[EvaluateDataQualityTypeDef] = None
    S3CatalogHudiSource: Optional[S3CatalogHudiSourceTypeDef] = None
    CatalogHudiSource: Optional[CatalogHudiSourceTypeDef] = None
    S3HudiSource: Optional[S3HudiSourceTypeDef] = None
    S3HudiCatalogTarget: Optional[S3HudiCatalogTargetTypeDef] = None
    S3HudiDirectTarget: Optional[S3HudiDirectTargetTypeDef] = None
    DirectJDBCSource: Optional[DirectJDBCSourceTypeDef] = None
    S3CatalogDeltaSource: Optional[S3CatalogDeltaSourceTypeDef] = None
    CatalogDeltaSource: Optional[CatalogDeltaSourceTypeDef] = None
    S3DeltaSource: Optional[S3DeltaSourceTypeDef] = None
    S3DeltaCatalogTarget: Optional[S3DeltaCatalogTargetTypeDef] = None
    S3DeltaDirectTarget: Optional[S3DeltaDirectTargetTypeDef] = None
    AmazonRedshiftSource: Optional[AmazonRedshiftSourceTypeDef] = None
    AmazonRedshiftTarget: Optional[AmazonRedshiftTargetTypeDef] = None
    EvaluateDataQualityMultiFrame: Optional[EvaluateDataQualityMultiFrameTypeDef] = None
    Recipe: Optional[RecipeTypeDef] = None
    SnowflakeSource: Optional[SnowflakeSourceTypeDef] = None
    SnowflakeTarget: Optional[SnowflakeTargetTypeDef] = None
    ConnectorDataSource: Optional[ConnectorDataSourceTypeDef] = None
    ConnectorDataTarget: Optional[ConnectorDataTargetTypeDef] = None

class BatchTableOptimizerTypeDef(BaseModel):
    catalogId: Optional[str] = None
    databaseName: Optional[str] = None
    tableName: Optional[str] = None
    tableOptimizer: Optional[TableOptimizerTypeDef] = None

class GetTableOptimizerResponseTypeDef(BaseModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    TableOptimizer: TableOptimizerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStatementResponseTypeDef(BaseModel):
    Statement: StatementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStatementsResponseTypeDef(BaseModel):
    Statements: List[StatementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ColumnStatisticsTypeDef(BaseModel):
    ColumnName: str
    ColumnType: str
    AnalyzedTime: TimestampTypeDef
    StatisticsData: ColumnStatisticsDataTypeDef

class NodeTypeDef(BaseModel):
    Type: Optional[NodeTypeType] = None
    Name: Optional[str] = None
    UniqueId: Optional[str] = None
    TriggerDetails: Optional[TriggerNodeDetailsTypeDef] = None
    JobDetails: Optional[JobNodeDetailsTypeDef] = None
    CrawlerDetails: Optional[CrawlerNodeDetailsTypeDef] = None

class GetMLTransformsResponseTypeDef(BaseModel):
    Transforms: List[MLTransformTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchGetDataQualityResultResponseTypeDef(BaseModel):
    Results: List[DataQualityResultTypeDef]
    ResultsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class ColumnStatisticsErrorTypeDef(BaseModel):
    ColumnStatistics: Optional[ColumnStatisticsOutputTypeDef] = None
    Error: Optional[ErrorDetailTypeDef] = None

class GetColumnStatisticsForPartitionResponseTypeDef(BaseModel):
    ColumnStatisticsList: List[ColumnStatisticsOutputTypeDef]
    Errors: List[ColumnErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetColumnStatisticsForTableResponseTypeDef(BaseModel):
    ColumnStatisticsList: List[ColumnStatisticsOutputTypeDef]
    Errors: List[ColumnErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetPartitionResponseTypeDef(BaseModel):
    Partitions: List[PartitionTypeDef]
    UnprocessedKeys: List[PartitionValueListOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPartitionResponseTypeDef(BaseModel):
    Partition: PartitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPartitionsResponseTypeDef(BaseModel):
    Partitions: List[PartitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetUnfilteredPartitionMetadataResponseTypeDef(BaseModel):
    Partition: PartitionTypeDef
    AuthorizedColumns: List[str]
    IsRegisteredWithLakeFormation: bool
    ResponseMetadata: ResponseMetadataTypeDef

class UnfilteredPartitionTypeDef(BaseModel):
    Partition: Optional[PartitionTypeDef] = None
    AuthorizedColumns: Optional[List[str]] = None
    IsRegisteredWithLakeFormation: Optional[bool] = None

class GetTableResponseTypeDef(BaseModel):
    Table: TableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTablesResponseTypeDef(BaseModel):
    TableList: List[TableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetUnfilteredTableMetadataResponseTypeDef(BaseModel):
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

class SearchTablesResponseTypeDef(BaseModel):
    TableList: List[TableTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TableVersionTypeDef(BaseModel):
    Table: Optional[TableTypeDef] = None
    VersionId: Optional[str] = None

class BatchCreatePartitionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    PartitionInputList: Sequence[PartitionInputTypeDef]
    CatalogId: Optional[str] = None

class BatchUpdatePartitionRequestEntryTypeDef(BaseModel):
    PartitionValueList: Sequence[str]
    PartitionInput: PartitionInputTypeDef

class CreatePartitionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    PartitionInput: PartitionInputTypeDef
    CatalogId: Optional[str] = None

class UpdatePartitionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    PartitionValueList: Sequence[str]
    PartitionInput: PartitionInputTypeDef
    CatalogId: Optional[str] = None

class CreateTableRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableInput: TableInputTypeDef
    CatalogId: Optional[str] = None
    PartitionIndexes: Optional[Sequence[PartitionIndexTypeDef]] = None
    TransactionId: Optional[str] = None
    OpenTableFormatInput: Optional[OpenTableFormatInputTypeDef] = None

class UpdateTableRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableInput: TableInputTypeDef
    CatalogId: Optional[str] = None
    SkipArchive: Optional[bool] = None
    TransactionId: Optional[str] = None
    VersionId: Optional[str] = None
    ViewUpdateAction: Optional[ViewUpdateActionType] = None
    Force: Optional[bool] = None

class CreateConnectionRequestRequestTypeDef(BaseModel):
    ConnectionInput: ConnectionInputTypeDef
    CatalogId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateConnectionRequestRequestTypeDef(BaseModel):
    Name: str
    ConnectionInput: ConnectionInputTypeDef
    CatalogId: Optional[str] = None

class GetConnectionResponseTypeDef(BaseModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionsResponseTypeDef(BaseModel):
    ConnectionList: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class JobTypeDef(BaseModel):
    Name: Optional[str] = None
    JobMode: Optional[JobModeType] = None
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

class JobUpdateTypeDef(BaseModel):
    JobMode: Optional[JobModeType] = None
    Description: Optional[str] = None
    LogUri: Optional[str] = None
    Role: Optional[str] = None
    ExecutionProperty: Optional[ExecutionPropertyTypeDef] = None
    Command: Optional[JobCommandTypeDef] = None
    DefaultArguments: Optional[Mapping[str, str]] = None
    NonOverridableArguments: Optional[Mapping[str, str]] = None
    Connections: Optional[ConnectionsListTypeDef] = None
    MaxRetries: Optional[int] = None
    AllocatedCapacity: Optional[int] = None
    Timeout: Optional[int] = None
    MaxCapacity: Optional[float] = None
    WorkerType: Optional[WorkerTypeType] = None
    NumberOfWorkers: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationPropertyTypeDef] = None
    GlueVersion: Optional[str] = None
    CodeGenConfigurationNodes: Optional[Mapping[str, CodeGenConfigurationNodeTypeDef]] = None
    ExecutionClass: Optional[ExecutionClassType] = None
    SourceControlDetails: Optional[SourceControlDetailsTypeDef] = None
    MaintenanceWindow: Optional[str] = None

class BatchGetTableOptimizerResponseTypeDef(BaseModel):
    TableOptimizers: List[BatchTableOptimizerTypeDef]
    Failures: List[BatchGetTableOptimizerErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class WorkflowGraphTypeDef(BaseModel):
    Nodes: Optional[List[NodeTypeDef]] = None
    Edges: Optional[List[EdgeTypeDef]] = None

class UpdateColumnStatisticsForPartitionResponseTypeDef(BaseModel):
    Errors: List[ColumnStatisticsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateColumnStatisticsForTableResponseTypeDef(BaseModel):
    Errors: List[ColumnStatisticsErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetUnfilteredPartitionsMetadataResponseTypeDef(BaseModel):
    UnfilteredPartitions: List[UnfilteredPartitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTableVersionResponseTypeDef(BaseModel):
    TableVersion: TableVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableVersionsResponseTypeDef(BaseModel):
    TableVersions: List[TableVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchUpdatePartitionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    Entries: Sequence[BatchUpdatePartitionRequestEntryTypeDef]
    CatalogId: Optional[str] = None

class BatchGetJobsResponseTypeDef(BaseModel):
    Jobs: List[JobTypeDef]
    JobsNotFound: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobResponseTypeDef(BaseModel):
    Job: JobTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobsResponseTypeDef(BaseModel):
    Jobs: List[JobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateJobRequestRequestTypeDef(BaseModel):
    Name: str
    Role: str
    Command: JobCommandTypeDef
    JobMode: Optional[JobModeType] = None
    Description: Optional[str] = None
    LogUri: Optional[str] = None
    ExecutionProperty: Optional[ExecutionPropertyTypeDef] = None
    DefaultArguments: Optional[Mapping[str, str]] = None
    NonOverridableArguments: Optional[Mapping[str, str]] = None
    Connections: Optional[ConnectionsListTypeDef] = None
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
    CodeGenConfigurationNodes: Optional[       Mapping[str, CodeGenConfigurationNodeUnionTypeDef] = None
    ExecutionClass: Optional[ExecutionClassType] = None
    SourceControlDetails: Optional[SourceControlDetailsTypeDef] = None
    MaintenanceWindow: Optional[str] = None

class UpdateJobRequestRequestTypeDef(BaseModel):
    JobName: str
    JobUpdate: JobUpdateTypeDef

class UpdateColumnStatisticsForPartitionRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnStatisticsList: Sequence[ColumnStatisticsUnionTypeDef]
    CatalogId: Optional[str] = None

class UpdateColumnStatisticsForTableRequestRequestTypeDef(BaseModel):
    DatabaseName: str
    TableName: str
    ColumnStatisticsList: Sequence[ColumnStatisticsUnionTypeDef]
    CatalogId: Optional[str] = None

class WorkflowRunTypeDef(BaseModel):
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

class GetWorkflowRunResponseTypeDef(BaseModel):
    Run: WorkflowRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowRunsResponseTypeDef(BaseModel):
    Runs: List[WorkflowRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class WorkflowTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    DefaultRunProperties: Optional[Dict[str, str]] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None
    LastRun: Optional[WorkflowRunTypeDef] = None
    Graph: Optional[WorkflowGraphTypeDef] = None
    MaxConcurrentRuns: Optional[int] = None
    BlueprintDetails: Optional[BlueprintDetailsTypeDef] = None

class BatchGetWorkflowsResponseTypeDef(BaseModel):
    Workflows: List[WorkflowTypeDef]
    MissingWorkflows: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowResponseTypeDef(BaseModel):
    Workflow: WorkflowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

