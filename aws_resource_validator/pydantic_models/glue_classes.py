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
from aws_resource_validator.pydantic_models.glue_constants import *

class NotificationPropertyTypeDef(BaseValidatorModel):
    NotifyDelayAfter: Optional[int] = None

class AggregateOperationExtraOutputTypeDef(BaseValidatorModel):
    Column: List[str]
    AggFunc: AggFunctionType

class AggregateOperationOutputTypeDef(BaseValidatorModel):
    Column: List[str]
    AggFunc: AggFunctionType

class AggregateOperationTypeDef(BaseValidatorModel):
    Column: Sequence[str]
    AggFunc: AggFunctionType

class AmazonRedshiftAdvancedOptionTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class OptionTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    Label: Optional[str] = None
    Description: Optional[str] = None

class ApplyMappingExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Mapping: List["MappingExtraOutputTypeDef"]

class ApplyMappingOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Mapping: List["MappingOutputTypeDef"]

class ApplyMappingTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Mapping: Sequence["MappingTypeDef"]

class AuditContextTypeDef(BaseValidatorModel):
    AdditionalAuditContext: Optional[str] = None
    RequestedColumns: Optional[Sequence[str]] = None
    AllColumnsRequested: Optional[bool] = None

class AuthorizationCodePropertiesTypeDef(BaseValidatorModel):
    AuthorizationCode: Optional[str] = None
    RedirectUri: Optional[str] = None

class PartitionValueListOutputTypeDef(BaseValidatorModel):
    Values: List[str]

class BasicCatalogTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class BasicCatalogTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class BasicCatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchDeleteConnectionRequestRequestTypeDef(BaseValidatorModel):
    ConnectionNameList: Sequence[str]
    CatalogId: Optional[str] = None

class ErrorDetailTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class BatchDeleteTableRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TablesToDelete: Sequence[str]
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None

class BatchDeleteTableVersionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    VersionIds: Sequence[str]
    CatalogId: Optional[str] = None

class BatchGetBlueprintsRequestRequestTypeDef(BaseValidatorModel):
    Names: Sequence[str]
    IncludeBlueprint: Optional[bool] = None
    IncludeParameterSpec: Optional[bool] = None

class BatchGetCrawlersRequestRequestTypeDef(BaseValidatorModel):
    CrawlerNames: Sequence[str]

class BatchGetCustomEntityTypesRequestRequestTypeDef(BaseValidatorModel):
    Names: Sequence[str]

class CustomEntityTypeTypeDef(BaseValidatorModel):
    Name: str
    RegexString: str
    ContextWords: Optional[List[str]] = None

class BatchGetDataQualityResultRequestRequestTypeDef(BaseValidatorModel):
    ResultIds: Sequence[str]

class BatchGetDevEndpointsRequestRequestTypeDef(BaseValidatorModel):
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

class BatchGetJobsRequestRequestTypeDef(BaseValidatorModel):
    JobNames: Sequence[str]

class BatchGetTableOptimizerEntryTypeDef(BaseValidatorModel):
    catalogId: Optional[str] = None
    databaseName: Optional[str] = None
    tableName: Optional[str] = None
    type: Optional[Literal["compaction"]] = None

class BatchGetTriggersRequestRequestTypeDef(BaseValidatorModel):
    TriggerNames: Sequence[str]

class BatchGetWorkflowsRequestRequestTypeDef(BaseValidatorModel):
    Names: Sequence[str]
    IncludeGraph: Optional[bool] = None

class BatchStopJobRunRequestRequestTypeDef(BaseValidatorModel):
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

class CancelDataQualityRuleRecommendationRunRequestRequestTypeDef(BaseValidatorModel):
    RunId: str

class CancelDataQualityRulesetEvaluationRunRequestRequestTypeDef(BaseValidatorModel):
    RunId: str

class CancelMLTaskRunRequestRequestTypeDef(BaseValidatorModel):
    TransformId: str
    TaskRunId: str

class CancelStatementRequestRequestTypeDef(BaseValidatorModel):
    SessionId: str
    Id: int
    RequestOrigin: Optional[str] = None

class CatalogEntryTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str

class CatalogImportStatusTypeDef(BaseValidatorModel):
    ImportCompleted: Optional[bool] = None
    ImportTime: Optional[datetime] = None
    ImportedBy: Optional[str] = None

class KafkaStreamingSourceOptionsExtraOutputTypeDef(BaseValidatorModel):
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

class KinesisStreamingSourceOptionsExtraOutputTypeDef(BaseValidatorModel):
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

class CatalogSchemaChangePolicyTypeDef(BaseValidatorModel):
    EnableUpdateCatalog: Optional[bool] = None
    UpdateBehavior: Optional[UpdateCatalogBehaviorType] = None

class CatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str

class CatalogTargetExtraOutputTypeDef(BaseValidatorModel):
    DatabaseName: str
    Tables: List[str]
    ConnectionName: Optional[str] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None

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

class CheckSchemaVersionValidityInputRequestTypeDef(BaseValidatorModel):
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

class ConnectorDataTargetExtraOutputTypeDef(BaseValidatorModel):
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

class DropDuplicatesExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Columns: Optional[List[List[str]]] = None

class DropFieldsExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]

class DynamoDBCatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str

class FillMissingValuesExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    ImputedPath: str
    FilledPath: Optional[str] = None

class MergeExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Source: str
    PrimaryKeys: List[List[str]]

class MicrosoftSQLServerCatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str

class MicrosoftSQLServerCatalogTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class MySQLCatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str

class MySQLCatalogTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class OracleSQLCatalogSourceTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str

class OracleSQLCatalogTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class PIIDetectionExtraOutputTypeDef(BaseValidatorModel):
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

class PostgreSQLCatalogTargetExtraOutputTypeDef(BaseValidatorModel):
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

class RenameFieldExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    SourcePath: List[str]
    TargetPath: List[str]

class SelectFieldsExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]

class SelectFromCollectionExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Index: int

class SpigotExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    Topk: Optional[int] = None
    Prob: Optional[float] = None

class SplitFieldsExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]

class UnionExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    UnionType: UnionTypeType

class ConnectorDataTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    ConnectionType: str
    Data: Dict[str, str]
    Inputs: Optional[List[str]] = None

class DropDuplicatesOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Columns: Optional[List[List[str]]] = None

class DropFieldsOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Paths: List[List[str]]

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

class MicrosoftSQLServerCatalogTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str

class MySQLCatalogTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
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

class PostgreSQLCatalogTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
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

class ConnectorDataTargetTypeDef(BaseValidatorModel):
    Name: str
    ConnectionType: str
    Data: Mapping[str, str]
    Inputs: Optional[Sequence[str]] = None

class DropDuplicatesTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Columns: Optional[Sequence[Sequence[str]]] = None

class DropFieldsTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]

class FillMissingValuesTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    ImputedPath: str
    FilledPath: Optional[str] = None

class MergeTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Source: str
    PrimaryKeys: Sequence[Sequence[str]]

class MicrosoftSQLServerCatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class MySQLCatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class OracleSQLCatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class PIIDetectionTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    PiiType: PiiTypeType
    EntityTypesToDetect: Sequence[str]
    OutputColumnName: Optional[str] = None
    SampleFraction: Optional[float] = None
    ThresholdFraction: Optional[float] = None
    MaskValue: Optional[str] = None

class PostgreSQLCatalogTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str

class RenameFieldTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    SourcePath: Sequence[str]
    TargetPath: Sequence[str]

class SelectFieldsTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Paths: Sequence[Sequence[str]]

class SelectFromCollectionTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Index: int

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

class UnionTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
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

class ColumnOutputTypeDef(BaseValidatorModel):
    Name: str
    Type: Optional[str] = None
    Comment: Optional[str] = None
    Parameters: Optional[Dict[str, str]] = None

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
    Status: Optional[ColumnStatisticsStateType] = None
    CreationTime: Optional[datetime] = None
    LastUpdated: Optional[datetime] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ErrorMessage: Optional[str] = None
    DPUSeconds: Optional[float] = None

class ColumnTypeDef(BaseValidatorModel):
    Name: str
    Type: Optional[str] = None
    Comment: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None

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

class PhysicalConnectionRequirementsTypeDef(BaseValidatorModel):
    SubnetId: Optional[str] = None
    SecurityGroupIdList: Optional[Sequence[str]] = None
    AvailabilityZone: Optional[str] = None

class ConnectionPasswordEncryptionTypeDef(BaseValidatorModel):
    ReturnConnectionPasswordEncrypted: bool
    AwsKmsKeyId: Optional[str] = None

class PhysicalConnectionRequirementsOutputTypeDef(BaseValidatorModel):
    SubnetId: Optional[str] = None
    SecurityGroupIdList: Optional[List[str]] = None
    AvailabilityZone: Optional[str] = None

class ConnectionsListExtraOutputTypeDef(BaseValidatorModel):
    Connections: Optional[List[str]] = None

class ConnectionsListOutputTypeDef(BaseValidatorModel):
    Connections: Optional[List[str]] = None

class ConnectionsListTypeDef(BaseValidatorModel):
    Connections: Optional[Sequence[str]] = None

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

class DeltaTargetExtraOutputTypeDef(BaseValidatorModel):
    DeltaTables: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    WriteManifest: Optional[bool] = None
    CreateNativeDeltaTable: Optional[bool] = None

class DynamoDBTargetTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    scanAll: Optional[bool] = None
    scanRate: Optional[float] = None

class HudiTargetExtraOutputTypeDef(BaseValidatorModel):
    Paths: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    MaximumTraversalDepth: Optional[int] = None

class IcebergTargetExtraOutputTypeDef(BaseValidatorModel):
    Paths: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    MaximumTraversalDepth: Optional[int] = None

class JdbcTargetExtraOutputTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    Path: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    EnableAdditionalMetadata: Optional[List[JdbcMetadataEntryType]] = None

class MongoDBTargetTypeDef(BaseValidatorModel):
    ConnectionName: Optional[str] = None
    Path: Optional[str] = None
    ScanAll: Optional[bool] = None

class S3TargetExtraOutputTypeDef(BaseValidatorModel):
    Path: Optional[str] = None
    Exclusions: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    SampleSize: Optional[int] = None
    EventQueueArn: Optional[str] = None
    DlqEventQueueArn: Optional[str] = None

class DeltaTargetOutputTypeDef(BaseValidatorModel):
    DeltaTables: Optional[List[str]] = None
    ConnectionName: Optional[str] = None
    WriteManifest: Optional[bool] = None
    CreateNativeDeltaTable: Optional[bool] = None

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

class ScheduleTypeDef(BaseValidatorModel):
    ScheduleExpression: Optional[str] = None
    State: Optional[ScheduleStateType] = None

class SchemaChangePolicyTypeDef(BaseValidatorModel):
    UpdateBehavior: Optional[UpdateBehaviorType] = None
    DeleteBehavior: Optional[DeleteBehaviorType] = None

class CrawlsFilterTypeDef(BaseValidatorModel):
    FieldName: Optional[FieldNameType] = None
    FilterOperator: Optional[FilterOperatorType] = None
    FieldValue: Optional[str] = None

class CreateBlueprintRequestRequestTypeDef(BaseValidatorModel):
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

class CreateCustomEntityTypeRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RegexString: str
    ContextWords: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class DataQualityTargetTableTypeDef(BaseValidatorModel):
    TableName: str
    DatabaseName: str
    CatalogId: Optional[str] = None

class CreateDevEndpointRequestRequestTypeDef(BaseValidatorModel):
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

class CreateRegistryInputRequestTypeDef(BaseValidatorModel):
    RegistryName: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class RegistryIdTypeDef(BaseValidatorModel):
    RegistryName: Optional[str] = None
    RegistryArn: Optional[str] = None

class SessionCommandTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    PythonVersion: Optional[str] = None

class TableOptimizerConfigurationTypeDef(BaseValidatorModel):
    roleArn: Optional[str] = None
    enabled: Optional[bool] = None

class EventBatchingConditionTypeDef(BaseValidatorModel):
    BatchSize: int
    BatchWindow: Optional[int] = None

class CreateWorkflowRequestRequestTypeDef(BaseValidatorModel):
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

class GlueTableOutputTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    ConnectionName: Optional[str] = None
    AdditionalOptions: Optional[Dict[str, str]] = None

class GlueTableTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    ConnectionName: Optional[str] = None
    AdditionalOptions: Optional[Mapping[str, str]] = None

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

class DeleteBlueprintRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteClassifierRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteColumnStatisticsForPartitionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnName: str
    CatalogId: Optional[str] = None

class DeleteColumnStatisticsForTableRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    ColumnName: str
    CatalogId: Optional[str] = None

class DeleteConnectionRequestRequestTypeDef(BaseValidatorModel):
    ConnectionName: str
    CatalogId: Optional[str] = None

class DeleteCrawlerRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteCustomEntityTypeRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteDataQualityRulesetRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteDatabaseRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None

class DeleteDevEndpointRequestRequestTypeDef(BaseValidatorModel):
    EndpointName: str

class DeleteJobRequestRequestTypeDef(BaseValidatorModel):
    JobName: str

class DeleteMLTransformRequestRequestTypeDef(BaseValidatorModel):
    TransformId: str

class DeletePartitionIndexRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    IndexName: str
    CatalogId: Optional[str] = None

class DeletePartitionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    CatalogId: Optional[str] = None

class DeleteResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyHashCondition: Optional[str] = None
    ResourceArn: Optional[str] = None

class SchemaIdTypeDef(BaseValidatorModel):
    SchemaArn: Optional[str] = None
    SchemaName: Optional[str] = None
    RegistryName: Optional[str] = None

class DeleteSecurityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteSessionRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    RequestOrigin: Optional[str] = None

class DeleteTableOptimizerRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    Type: Literal["compaction"]

class DeleteTableRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None

class DeleteTableVersionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    VersionId: str
    CatalogId: Optional[str] = None

class DeleteTriggerRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteUsageProfileRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DeleteUserDefinedFunctionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    FunctionName: str
    CatalogId: Optional[str] = None

class DeleteWorkflowRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class DevEndpointCustomLibrariesTypeDef(BaseValidatorModel):
    ExtraPythonLibsS3Path: Optional[str] = None
    ExtraJarsS3Path: Optional[str] = None

class DirectSchemaChangePolicyTypeDef(BaseValidatorModel):
    EnableUpdateCatalog: Optional[bool] = None
    UpdateBehavior: Optional[UpdateCatalogBehaviorType] = None
    Table: Optional[str] = None
    Database: Optional[str] = None

class NullCheckBoxListTypeDef(BaseValidatorModel):
    IsEmpty: Optional[bool] = None
    IsNullString: Optional[bool] = None
    IsNegOne: Optional[bool] = None

class TransformConfigParameterExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Type: ParamTypeType
    ValidationRule: Optional[str] = None
    ValidationMessage: Optional[str] = None
    Value: Optional[List[str]] = None
    ListType: Optional[ParamTypeType] = None
    IsOptional: Optional[bool] = None

class TransformConfigParameterOutputTypeDef(BaseValidatorModel):
    Name: str
    Type: ParamTypeType
    ValidationRule: Optional[str] = None
    ValidationMessage: Optional[str] = None
    Value: Optional[List[str]] = None
    ListType: Optional[ParamTypeType] = None
    IsOptional: Optional[bool] = None

class TransformConfigParameterTypeDef(BaseValidatorModel):
    Name: str
    Type: ParamTypeType
    ValidationRule: Optional[str] = None
    ValidationMessage: Optional[str] = None
    Value: Optional[Sequence[str]] = None
    ListType: Optional[ParamTypeType] = None
    IsOptional: Optional[bool] = None

class EdgeTypeDef(BaseValidatorModel):
    SourceId: Optional[str] = None
    DestinationId: Optional[str] = None

class JobBookmarksEncryptionTypeDef(BaseValidatorModel):
    JobBookmarksEncryptionMode: Optional[JobBookmarksEncryptionModeType] = None
    KmsKeyArn: Optional[str] = None

class S3EncryptionTypeDef(BaseValidatorModel):
    S3EncryptionMode: Optional[S3EncryptionModeType] = None
    KmsKeyArn: Optional[str] = None

class ErrorDetailsTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class ExportLabelsTaskRunPropertiesTypeDef(BaseValidatorModel):
    OutputS3Path: Optional[str] = None

class FederatedTableTypeDef(BaseValidatorModel):
    Identifier: Optional[str] = None
    DatabaseIdentifier: Optional[str] = None
    ConnectionName: Optional[str] = None

class FilterValueExtraOutputTypeDef(BaseValidatorModel):
    Type: FilterValueTypeType
    Value: List[str]

class FilterValueOutputTypeDef(BaseValidatorModel):
    Type: FilterValueTypeType
    Value: List[str]

class FilterValueTypeDef(BaseValidatorModel):
    Type: FilterValueTypeType
    Value: Sequence[str]

class FindMatchesParametersTypeDef(BaseValidatorModel):
    PrimaryKeyColumnName: Optional[str] = None
    PrecisionRecallTradeoff: Optional[float] = None
    AccuracyCostTradeoff: Optional[float] = None
    EnforceProvidedLabels: Optional[bool] = None

class FindMatchesTaskRunPropertiesTypeDef(BaseValidatorModel):
    JobId: Optional[str] = None
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None

class GetBlueprintRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    IncludeBlueprint: Optional[bool] = None
    IncludeParameterSpec: Optional[bool] = None

class GetBlueprintRunRequestRequestTypeDef(BaseValidatorModel):
    BlueprintName: str
    RunId: str

class GetBlueprintRunsRequestRequestTypeDef(BaseValidatorModel):
    BlueprintName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetCatalogImportStatusRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None

class GetClassifierRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetClassifiersRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetColumnStatisticsForPartitionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnNames: Sequence[str]
    CatalogId: Optional[str] = None

class GetColumnStatisticsForTableRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    ColumnNames: Sequence[str]
    CatalogId: Optional[str] = None

class GetColumnStatisticsTaskRunRequestRequestTypeDef(BaseValidatorModel):
    ColumnStatisticsTaskRunId: str

class GetColumnStatisticsTaskRunsRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetConnectionRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None
    HidePassword: Optional[bool] = None

class GetConnectionsFilterTypeDef(BaseValidatorModel):
    MatchCriteria: Optional[Sequence[str]] = None
    ConnectionType: Optional[ConnectionTypeType] = None

class GetCrawlerMetricsRequestRequestTypeDef(BaseValidatorModel):
    CrawlerNameList: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetCrawlerRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class GetCrawlersRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetCustomEntityTypeRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class GetDataCatalogEncryptionSettingsRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None

class GetDataQualityResultRequestRequestTypeDef(BaseValidatorModel):
    ResultId: str

class GetDataQualityRuleRecommendationRunRequestRequestTypeDef(BaseValidatorModel):
    RunId: str

class GetDataQualityRulesetEvaluationRunRequestRequestTypeDef(BaseValidatorModel):
    RunId: str

class GetDataQualityRulesetRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class GetDatabaseRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    CatalogId: Optional[str] = None

class GetDatabasesRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    AttributesToGet: Optional[Sequence[Literal["NAME"]]] = None

class GetDataflowGraphRequestRequestTypeDef(BaseValidatorModel):
    PythonScript: Optional[str] = None

class GetDevEndpointRequestRequestTypeDef(BaseValidatorModel):
    EndpointName: str

class GetDevEndpointsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetJobBookmarkRequestRequestTypeDef(BaseValidatorModel):
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

class GetJobRequestRequestTypeDef(BaseValidatorModel):
    JobName: str

class GetJobRunRequestRequestTypeDef(BaseValidatorModel):
    JobName: str
    RunId: str
    PredecessorsIncluded: Optional[bool] = None

class GetJobRunsRequestRequestTypeDef(BaseValidatorModel):
    JobName: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetJobsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetMLTaskRunRequestRequestTypeDef(BaseValidatorModel):
    TransformId: str
    TaskRunId: str

class TaskRunSortCriteriaTypeDef(BaseValidatorModel):
    Column: TaskRunSortColumnTypeType
    SortDirection: SortDirectionTypeType

class GetMLTransformRequestRequestTypeDef(BaseValidatorModel):
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

class GetPartitionIndexesRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None

class GetPartitionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    CatalogId: Optional[str] = None

class SegmentTypeDef(BaseValidatorModel):
    SegmentNumber: int
    TotalSegments: int

class GetResourcePoliciesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GluePolicyTypeDef(BaseValidatorModel):
    PolicyInJson: Optional[str] = None
    PolicyHash: Optional[str] = None
    CreateTime: Optional[datetime] = None
    UpdateTime: Optional[datetime] = None

class GetResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: Optional[str] = None

class SchemaVersionNumberTypeDef(BaseValidatorModel):
    LatestVersion: Optional[bool] = None
    VersionNumber: Optional[int] = None

class GetSecurityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class GetSecurityConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class GetSessionRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    RequestOrigin: Optional[str] = None

class GetStatementRequestRequestTypeDef(BaseValidatorModel):
    SessionId: str
    Id: int
    RequestOrigin: Optional[str] = None

class GetTableOptimizerRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    Type: Literal["compaction"]

class GetTableVersionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    VersionId: Optional[str] = None

class GetTableVersionsRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetTagsRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class GetTriggerRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class GetTriggersRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    DependentJobName: Optional[str] = None
    MaxResults: Optional[int] = None

class SupportedDialectTypeDef(BaseValidatorModel):
    Dialect: Optional[ViewDialectType] = None
    DialectVersion: Optional[str] = None

class GetUsageProfileRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class GetUserDefinedFunctionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    FunctionName: str
    CatalogId: Optional[str] = None

class GetUserDefinedFunctionsRequestRequestTypeDef(BaseValidatorModel):
    Pattern: str
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GetWorkflowRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    IncludeGraph: Optional[bool] = None

class GetWorkflowRunPropertiesRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str

class GetWorkflowRunRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str
    IncludeGraph: Optional[bool] = None

class GetWorkflowRunsRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    IncludeGraph: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class GlueStudioSchemaColumnTypeDef(BaseValidatorModel):
    Name: str
    Type: Optional[str] = None

class S3SourceAdditionalOptionsTypeDef(BaseValidatorModel):
    BoundedSize: Optional[int] = None
    BoundedFiles: Optional[int] = None

class IcebergInputTypeDef(BaseValidatorModel):
    MetadataOperation: Literal["CREATE"]
    Version: Optional[str] = None

class ImportCatalogToGlueRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None

class ImportLabelsTaskRunPropertiesTypeDef(BaseValidatorModel):
    InputS3Path: Optional[str] = None
    Replace: Optional[bool] = None

class JDBCConnectorOptionsExtraOutputTypeDef(BaseValidatorModel):
    FilterPredicate: Optional[str] = None
    PartitionColumn: Optional[str] = None
    LowerBound: Optional[int] = None
    UpperBound: Optional[int] = None
    NumPartitions: Optional[int] = None
    JobBookmarkKeys: Optional[List[str]] = None
    JobBookmarkKeysSortOrder: Optional[str] = None
    DataTypeMapping: Optional[Dict[JDBCDataTypeType, GlueRecordTypeType]] = None

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

class JoinColumnExtraOutputTypeDef(BaseValidatorModel):
    From: str
    Keys: List[List[str]]

class JoinColumnOutputTypeDef(BaseValidatorModel):
    From: str
    Keys: List[List[str]]

class JoinColumnTypeDef(BaseValidatorModel):
    From: str
    Keys: Sequence[Sequence[str]]

class KeySchemaElementTypeDef(BaseValidatorModel):
    Name: str
    Type: str

class LabelingSetGenerationTaskRunPropertiesTypeDef(BaseValidatorModel):
    OutputS3Path: Optional[str] = None

class ListBlueprintsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class ListColumnStatisticsTaskRunsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListCrawlersRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class ListCustomEntityTypesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class ListDevEndpointsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class ListJobsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class ListRegistriesInputRequestTypeDef(BaseValidatorModel):
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

class ListSessionsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None
    RequestOrigin: Optional[str] = None

class ListStatementsRequestRequestTypeDef(BaseValidatorModel):
    SessionId: str
    RequestOrigin: Optional[str] = None
    NextToken: Optional[str] = None

class ListTableOptimizerRunsRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    Type: Literal["compaction"]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListTriggersRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    DependentJobName: Optional[str] = None
    MaxResults: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class ListUsageProfilesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class UsageProfileDefinitionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    CreatedOn: Optional[datetime] = None
    LastModifiedOn: Optional[datetime] = None

class ListWorkflowsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MLUserDataEncryptionTypeDef(BaseValidatorModel):
    MlUserDataEncryptionMode: MLUserDataEncryptionModeStringType
    KmsKeyId: Optional[str] = None

class MappingExtraOutputTypeDef(BaseValidatorModel):
    ToKey: Optional[str] = None
    FromPath: Optional[List[str]] = None
    FromType: Optional[str] = None
    ToType: Optional[str] = None
    Dropped: Optional[bool] = None
    Children: Optional[List[Dict[str, Any]]] = None

class MappingOutputTypeDef(BaseValidatorModel):
    ToKey: Optional[str] = None
    FromPath: Optional[List[str]] = None
    FromType: Optional[str] = None
    ToType: Optional[str] = None
    Dropped: Optional[bool] = None
    Children: Optional[List[Dict[str, Any]]] = None

class MappingTypeDef(BaseValidatorModel):
    ToKey: Optional[str] = None
    FromPath: Optional[Sequence[str]] = None
    FromType: Optional[str] = None
    ToType: Optional[str] = None
    Dropped: Optional[bool] = None
    Children: Optional[Sequence[Dict[str, Any]]] = None

class OtherMetadataValueListItemTypeDef(BaseValidatorModel):
    MetadataValue: Optional[str] = None
    CreatedTime: Optional[str] = None

class MetadataKeyValuePairTypeDef(BaseValidatorModel):
    MetadataKey: Optional[str] = None
    MetadataValue: Optional[str] = None

class OAuth2ClientApplicationTypeDef(BaseValidatorModel):
    UserManagedClientApplicationClientId: Optional[str] = None
    AWSManagedClientApplicationReference: Optional[str] = None

class OrderTypeDef(BaseValidatorModel):
    Column: str
    SortOrder: int

class PartitionValueListExtraOutputTypeDef(BaseValidatorModel):
    Values: List[str]

class PartitionValueListTypeDef(BaseValidatorModel):
    Values: Sequence[str]

class PropertyPredicateTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None
    Comparator: Optional[ComparatorType] = None

class PutResourcePolicyRequestRequestTypeDef(BaseValidatorModel):
    PolicyInJson: str
    ResourceArn: Optional[str] = None
    PolicyHashCondition: Optional[str] = None
    PolicyExistsCondition: Optional[ExistConditionType] = None
    EnableHybrid: Optional[EnableHybridValuesType] = None

class PutWorkflowRunPropertiesRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str
    RunProperties: Mapping[str, str]

class RecipeActionExtraOutputTypeDef(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Dict[str, str]] = None

class RecipeActionOutputTypeDef(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Dict[str, str]] = None

class RecipeActionTypeDef(BaseValidatorModel):
    Operation: str
    Parameters: Optional[Mapping[str, str]] = None

class RecipeReferenceTypeDef(BaseValidatorModel):
    RecipeArn: str
    RecipeVersion: str

class UpsertRedshiftTargetOptionsExtraOutputTypeDef(BaseValidatorModel):
    TableLocation: Optional[str] = None
    ConnectionName: Optional[str] = None
    UpsertKeys: Optional[List[str]] = None

class UpsertRedshiftTargetOptionsOutputTypeDef(BaseValidatorModel):
    TableLocation: Optional[str] = None
    ConnectionName: Optional[str] = None
    UpsertKeys: Optional[List[str]] = None

class UpsertRedshiftTargetOptionsTypeDef(BaseValidatorModel):
    TableLocation: Optional[str] = None
    ConnectionName: Optional[str] = None
    UpsertKeys: Optional[Sequence[str]] = None

class ResetJobBookmarkRequestRequestTypeDef(BaseValidatorModel):
    JobName: str
    RunId: Optional[str] = None

class ResourceUriTypeDef(BaseValidatorModel):
    ResourceType: Optional[ResourceTypeType] = None
    Uri: Optional[str] = None

class ResumeWorkflowRunRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str
    NodeIds: Sequence[str]

class RunMetricsTypeDef(BaseValidatorModel):
    NumberOfBytesCompacted: Optional[str] = None
    NumberOfFilesCompacted: Optional[str] = None
    NumberOfDpus: Optional[str] = None
    JobDurationInHour: Optional[str] = None

class RunStatementRequestRequestTypeDef(BaseValidatorModel):
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

class SqlAliasTypeDef(BaseValidatorModel):
    From: str
    Alias: str

class StartBlueprintRunRequestRequestTypeDef(BaseValidatorModel):
    BlueprintName: str
    RoleArn: str
    Parameters: Optional[str] = None

class StartColumnStatisticsTaskRunRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    Role: str
    ColumnNameList: Optional[Sequence[str]] = None
    SampleSize: Optional[float] = None
    CatalogID: Optional[str] = None
    SecurityConfiguration: Optional[str] = None

class StartCrawlerRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class StartCrawlerScheduleRequestRequestTypeDef(BaseValidatorModel):
    CrawlerName: str

class StartExportLabelsTaskRunRequestRequestTypeDef(BaseValidatorModel):
    TransformId: str
    OutputS3Path: str

class StartImportLabelsTaskRunRequestRequestTypeDef(BaseValidatorModel):
    TransformId: str
    InputS3Path: str
    ReplaceAllLabels: Optional[bool] = None

class StartMLEvaluationTaskRunRequestRequestTypeDef(BaseValidatorModel):
    TransformId: str

class StartMLLabelingSetGenerationTaskRunRequestRequestTypeDef(BaseValidatorModel):
    TransformId: str
    OutputS3Path: str

class StartTriggerRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class StartWorkflowRunRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RunProperties: Optional[Mapping[str, str]] = None

class StartingEventBatchConditionTypeDef(BaseValidatorModel):
    BatchSize: Optional[int] = None
    BatchWindow: Optional[int] = None

class StatementOutputDataTypeDef(BaseValidatorModel):
    TextPlain: Optional[str] = None

class StopColumnStatisticsTaskRunRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str

class StopCrawlerRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class StopCrawlerScheduleRequestRequestTypeDef(BaseValidatorModel):
    CrawlerName: str

class StopSessionRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    RequestOrigin: Optional[str] = None

class StopTriggerRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class StopWorkflowRunRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RunId: str

class TableIdentifierTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    Name: Optional[str] = None
    Region: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagsToAdd: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagsToRemove: Sequence[str]

class UpdateBlueprintRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateCrawlerScheduleRequestRequestTypeDef(BaseValidatorModel):
    CrawlerName: str
    Schedule: Optional[str] = None

class UpdateDataQualityRulesetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    Ruleset: Optional[str] = None

class UpdateJobFromSourceControlRequestRequestTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    Provider: Optional[SourceControlProviderType] = None
    RepositoryName: Optional[str] = None
    RepositoryOwner: Optional[str] = None
    BranchName: Optional[str] = None
    Folder: Optional[str] = None
    CommitId: Optional[str] = None
    AuthStrategy: Optional[SourceControlAuthStrategyType] = None
    AuthToken: Optional[str] = None

class UpdateSourceControlFromJobRequestRequestTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    Provider: Optional[SourceControlProviderType] = None
    RepositoryName: Optional[str] = None
    RepositoryOwner: Optional[str] = None
    BranchName: Optional[str] = None
    Folder: Optional[str] = None
    CommitId: Optional[str] = None
    AuthStrategy: Optional[SourceControlAuthStrategyType] = None
    AuthToken: Optional[str] = None

class UpdateWorkflowRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    DefaultRunProperties: Optional[Mapping[str, str]] = None
    MaxConcurrentRuns: Optional[int] = None

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

class ActionExtraOutputTypeDef(BaseValidatorModel):
    JobName: Optional[str] = None
    Arguments: Optional[Dict[str, str]] = None
    Timeout: Optional[int] = None
    SecurityConfiguration: Optional[str] = None
    NotificationProperty: Optional[NotificationPropertyTypeDef] = None
    CrawlerName: Optional[str] = None

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

class StartJobRunRequestRequestTypeDef(BaseValidatorModel):
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

class AggregateExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Groups: List[List[str]]
    Aggs: List[AggregateOperationExtraOutputTypeDef]

class AggregateOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Groups: List[List[str]]
    Aggs: List[AggregateOperationOutputTypeDef]

class AggregateTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Groups: Sequence[Sequence[str]]
    Aggs: Sequence[AggregateOperationTypeDef]

class AmazonRedshiftNodeDataExtraOutputTypeDef(BaseValidatorModel):
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

class SnowflakeNodeDataExtraOutputTypeDef(BaseValidatorModel):
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

class BatchGetTableOptimizerErrorTypeDef(BaseValidatorModel):
    error: Optional[ErrorDetailTypeDef] = None
    catalogId: Optional[str] = None
    databaseName: Optional[str] = None
    tableName: Optional[str] = None
    type: Optional[Literal["compaction"]] = None

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

class BatchGetTableOptimizerRequestRequestTypeDef(BaseValidatorModel):
    Entries: Sequence[BatchGetTableOptimizerEntryTypeDef]

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

class GetCatalogImportStatusResponseTypeDef(BaseValidatorModel):
    ImportStatus: CatalogImportStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CatalogKafkaSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KafkaStreamingSourceOptionsExtraOutputTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class DirectKafkaSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    StreamingOptions: Optional[KafkaStreamingSourceOptionsExtraOutputTypeDef] = None
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

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

class CatalogKinesisSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsExtraOutputTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class DirectKinesisSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsExtraOutputTypeDef] = None
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

class GovernedCatalogTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    SchemaChangePolicy: Optional[CatalogSchemaChangePolicyTypeDef] = None

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

class S3CatalogTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
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

class S3DeltaCatalogTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    PartitionKeys: Optional[List[List[str]]] = None
    AdditionalOptions: Optional[Dict[str, str]] = None
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

class S3HudiCatalogTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Table: str
    Database: str
    AdditionalOptions: Dict[str, str]
    PartitionKeys: Optional[List[List[str]]] = None
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

class DateColumnStatisticsDataTypeDef(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[TimestampTypeDef] = None
    MaximumValue: Optional[TimestampTypeDef] = None

class GetTableRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    Name: str
    CatalogId: Optional[str] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None

class GetTablesRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None

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

class PredicateExtraOutputTypeDef(BaseValidatorModel):
    Logical: Optional[LogicalType] = None
    Conditions: Optional[List[ConditionTypeDef]] = None

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

class CrawlerTargetsExtraOutputTypeDef(BaseValidatorModel):
    S3Targets: Optional[List[S3TargetExtraOutputTypeDef]] = None
    JdbcTargets: Optional[List[JdbcTargetExtraOutputTypeDef]] = None
    MongoDBTargets: Optional[List[MongoDBTargetTypeDef]] = None
    DynamoDBTargets: Optional[List[DynamoDBTargetTypeDef]] = None
    CatalogTargets: Optional[List[CatalogTargetExtraOutputTypeDef]] = None
    DeltaTargets: Optional[List[DeltaTargetExtraOutputTypeDef]] = None
    IcebergTargets: Optional[List[IcebergTargetExtraOutputTypeDef]] = None
    HudiTargets: Optional[List[HudiTargetExtraOutputTypeDef]] = None

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

class ListCrawlsRequestRequestTypeDef(BaseValidatorModel):
    CrawlerName: str
    MaxResults: Optional[int] = None
    Filters: Optional[Sequence[CrawlsFilterTypeDef]] = None
    NextToken: Optional[str] = None

class CreateClassifierRequestRequestTypeDef(BaseValidatorModel):
    GrokClassifier: Optional[CreateGrokClassifierRequestTypeDef] = None
    XMLClassifier: Optional[CreateXMLClassifierRequestTypeDef] = None
    JsonClassifier: Optional[CreateJsonClassifierRequestTypeDef] = None
    CsvClassifier: Optional[CreateCsvClassifierRequestTypeDef] = None

class CreateDataQualityRulesetRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Ruleset: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    TargetTable: Optional[DataQualityTargetTableTypeDef] = None
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
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePartitionIndexRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionIndex: PartitionIndexTypeDef
    CatalogId: Optional[str] = None

class CreateSchemaInputRequestTypeDef(BaseValidatorModel):
    SchemaName: str
    DataFormat: DataFormatType
    RegistryId: Optional[RegistryIdTypeDef] = None
    Compatibility: Optional[CompatibilityType] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    SchemaDefinition: Optional[str] = None

class DeleteRegistryInputRequestTypeDef(BaseValidatorModel):
    RegistryId: RegistryIdTypeDef

class GetRegistryInputRequestTypeDef(BaseValidatorModel):
    RegistryId: RegistryIdTypeDef

class ListSchemasInputRequestTypeDef(BaseValidatorModel):
    RegistryId: Optional[RegistryIdTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UpdateRegistryInputRequestTypeDef(BaseValidatorModel):
    RegistryId: RegistryIdTypeDef
    Description: str

class CreateSessionRequestRequestTypeDef(BaseValidatorModel):
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

class CreateTableOptimizerRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    Type: Literal["compaction"]
    TableOptimizerConfiguration: TableOptimizerConfigurationTypeDef

class UpdateTableOptimizerRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    Type: Literal["compaction"]
    TableOptimizerConfiguration: TableOptimizerConfigurationTypeDef

class EvaluateDataQualityExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Ruleset: str
    Output: Optional[DQTransformOutputType] = None
    PublishingOptions: Optional[DQResultsPublishingOptionsTypeDef] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptionsTypeDef] = None

class EvaluateDataQualityMultiFrameExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Ruleset: str
    AdditionalDataSources: Optional[Dict[str, str]] = None
    PublishingOptions: Optional[DQResultsPublishingOptionsTypeDef] = None
    AdditionalOptions: Optional[Dict[AdditionalOptionKeysType, str]] = None
    StopJobOnFailureOptions: Optional[DQStopJobOnFailureOptionsTypeDef] = None

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
    MetricValues: Optional[DataQualityMetricValuesTypeDef] = None
    NewRules: Optional[List[str]] = None

class DataSourceOutputTypeDef(BaseValidatorModel):
    GlueTable: GlueTableOutputTypeDef

class DataSourceTypeDef(BaseValidatorModel):
    GlueTable: GlueTableTypeDef

class NullValueFieldTypeDef(BaseValidatorModel):
    Value: str
    Datatype: DatatypeTypeDef

class DecimalColumnStatisticsDataOutputTypeDef(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[DecimalNumberOutputTypeDef] = None
    MaximumValue: Optional[DecimalNumberOutputTypeDef] = None

class DeleteSchemaInputRequestTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef

class DeleteSchemaVersionsInputRequestTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    Versions: str

class GetSchemaByDefinitionInputRequestTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    SchemaDefinition: str

class GetSchemaInputRequestTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef

class ListSchemaVersionsInputRequestTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RegisterSchemaVersionInputRequestTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    SchemaDefinition: str

class SchemaReferenceTypeDef(BaseValidatorModel):
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionId: Optional[str] = None
    SchemaVersionNumber: Optional[int] = None

class UpdateDevEndpointRequestRequestTypeDef(BaseValidatorModel):
    EndpointName: str
    PublicKey: Optional[str] = None
    AddPublicKeys: Optional[Sequence[str]] = None
    DeletePublicKeys: Optional[Sequence[str]] = None
    CustomLibraries: Optional[DevEndpointCustomLibrariesTypeDef] = None
    UpdateEtlLibraries: Optional[bool] = None
    DeleteArguments: Optional[Sequence[str]] = None
    AddArguments: Optional[Mapping[str, str]] = None

class S3DeltaDirectTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    Compression: DeltaTargetCompressionTypeType
    Format: TargetFormatType
    PartitionKeys: Optional[List[List[str]]] = None
    AdditionalOptions: Optional[Dict[str, str]] = None
    SchemaChangePolicy: Optional[DirectSchemaChangePolicyTypeDef] = None

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

class S3DirectTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    Format: TargetFormatType
    PartitionKeys: Optional[List[List[str]]] = None
    Compression: Optional[str] = None
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

class S3GlueParquetTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    PartitionKeys: Optional[List[List[str]]] = None
    Compression: Optional[ParquetCompressionTypeType] = None
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

class S3HudiDirectTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Path: str
    Compression: HudiTargetCompressionTypeType
    Format: TargetFormatType
    AdditionalOptions: Dict[str, str]
    PartitionKeys: Optional[List[List[str]]] = None
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

class EncryptionConfigurationExtraOutputTypeDef(BaseValidatorModel):
    S3Encryption: Optional[List[S3EncryptionTypeDef]] = None
    CloudWatchEncryption: Optional[CloudWatchEncryptionTypeDef] = None
    JobBookmarksEncryption: Optional[JobBookmarksEncryptionTypeDef] = None

class EncryptionConfigurationOutputTypeDef(BaseValidatorModel):
    S3Encryption: Optional[List[S3EncryptionTypeDef]] = None
    CloudWatchEncryption: Optional[CloudWatchEncryptionTypeDef] = None
    JobBookmarksEncryption: Optional[JobBookmarksEncryptionTypeDef] = None

class EncryptionConfigurationTypeDef(BaseValidatorModel):
    S3Encryption: Optional[Sequence[S3EncryptionTypeDef]] = None
    CloudWatchEncryption: Optional[CloudWatchEncryptionTypeDef] = None
    JobBookmarksEncryption: Optional[JobBookmarksEncryptionTypeDef] = None

class SchemaVersionErrorItemTypeDef(BaseValidatorModel):
    VersionNumber: Optional[int] = None
    ErrorDetails: Optional[ErrorDetailsTypeDef] = None

class FilterExpressionExtraOutputTypeDef(BaseValidatorModel):
    Operation: FilterOperationType
    Values: List[FilterValueExtraOutputTypeDef]
    Negated: Optional[bool] = None

class FilterExpressionOutputTypeDef(BaseValidatorModel):
    Operation: FilterOperationType
    Values: List[FilterValueOutputTypeDef]
    Negated: Optional[bool] = None

class FilterExpressionTypeDef(BaseValidatorModel):
    Operation: FilterOperationType
    Values: Sequence[FilterValueTypeDef]
    Negated: Optional[bool] = None

class TransformParametersTypeDef(BaseValidatorModel):
    TransformType: Literal["FIND_MATCHES"]
    FindMatchesParameters: Optional[FindMatchesParametersTypeDef] = None

class GetClassifiersRequestGetClassifiersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCrawlerMetricsRequestGetCrawlerMetricsPaginateTypeDef(BaseValidatorModel):
    CrawlerNameList: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetCrawlersRequestGetCrawlersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDatabasesRequestGetDatabasesPaginateTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None
    AttributesToGet: Optional[Sequence[Literal["NAME"]]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetDevEndpointsRequestGetDevEndpointsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetJobRunsRequestGetJobRunsPaginateTypeDef(BaseValidatorModel):
    JobName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetJobsRequestGetJobsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetPartitionIndexesRequestGetPartitionIndexesPaginateTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetResourcePoliciesRequestGetResourcePoliciesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetSecurityConfigurationsRequestGetSecurityConfigurationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTableVersionsRequestGetTableVersionsPaginateTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTablesRequestGetTablesPaginateTypeDef(BaseValidatorModel):
    DatabaseName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTriggersRequestGetTriggersPaginateTypeDef(BaseValidatorModel):
    DependentJobName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetUserDefinedFunctionsRequestGetUserDefinedFunctionsPaginateTypeDef(BaseValidatorModel):
    Pattern: str
    CatalogId: Optional[str] = None
    DatabaseName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetWorkflowRunsRequestGetWorkflowRunsPaginateTypeDef(BaseValidatorModel):
    Name: str
    IncludeGraph: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBlueprintsRequestListBlueprintsPaginateTypeDef(BaseValidatorModel):
    Tags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestListJobsPaginateTypeDef(BaseValidatorModel):
    Tags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRegistriesInputListRegistriesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemaVersionsInputListSchemaVersionsPaginateTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchemasInputListSchemasPaginateTypeDef(BaseValidatorModel):
    RegistryId: Optional[RegistryIdTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTriggersRequestListTriggersPaginateTypeDef(BaseValidatorModel):
    DependentJobName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsageProfilesRequestListUsageProfilesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWorkflowsRequestListWorkflowsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetConnectionsRequestGetConnectionsPaginateTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    Filter: Optional[GetConnectionsFilterTypeDef] = None
    HidePassword: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetConnectionsRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    Filter: Optional[GetConnectionsFilterTypeDef] = None
    HidePassword: Optional[bool] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

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

class GetMappingResponseTypeDef(BaseValidatorModel):
    Mapping: List[MappingEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPartitionsRequestGetPartitionsPaginateTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    CatalogId: Optional[str] = None
    Expression: Optional[str] = None
    Segment: Optional[SegmentTypeDef] = None
    ExcludeColumnSchema: Optional[bool] = None
    TransactionId: Optional[str] = None
    QueryAsOfTime: Optional[TimestampTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetPartitionsRequestRequestTypeDef(BaseValidatorModel):
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

class GetSchemaVersionInputRequestTypeDef(BaseValidatorModel):
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionId: Optional[str] = None
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None

class GetSchemaVersionsDiffInputRequestTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    FirstSchemaVersionNumber: SchemaVersionNumberTypeDef
    SecondSchemaVersionNumber: SchemaVersionNumberTypeDef
    SchemaDiffType: Literal["SYNTAX_DIFF"]

class UpdateSchemaInputRequestTypeDef(BaseValidatorModel):
    SchemaId: SchemaIdTypeDef
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None
    Compatibility: Optional[CompatibilityType] = None
    Description: Optional[str] = None

class GlueSchemaExtraOutputTypeDef(BaseValidatorModel):
    Columns: Optional[List[GlueStudioSchemaColumnTypeDef]] = None

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

class JobRunTypeDef(BaseValidatorModel):
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

class JoinExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    JoinType: JoinTypeType
    Columns: List[JoinColumnExtraOutputTypeDef]

class JoinOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    JoinType: JoinTypeType
    Columns: List[JoinColumnOutputTypeDef]

class JoinTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    JoinType: JoinTypeType
    Columns: Sequence[JoinColumnTypeDef]

class TaskRunPropertiesTypeDef(BaseValidatorModel):
    TaskType: Optional[TaskTypeType] = None
    ImportLabelsTaskRunProperties: Optional[ImportLabelsTaskRunPropertiesTypeDef] = None
    ExportLabelsTaskRunProperties: Optional[ExportLabelsTaskRunPropertiesTypeDef] = None
    LabelingSetGenerationTaskRunProperties: Optional[       LabelingSetGenerationTaskRunPropertiesTypeDef     ] = None
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

class PutSchemaVersionMetadataInputRequestTypeDef(BaseValidatorModel):
    MetadataKeyValue: MetadataKeyValuePairTypeDef
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None
    SchemaVersionId: Optional[str] = None

class QuerySchemaVersionMetadataInputRequestTypeDef(BaseValidatorModel):
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None
    SchemaVersionId: Optional[str] = None
    MetadataList: Optional[Sequence[MetadataKeyValuePairTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class RemoveSchemaVersionMetadataInputRequestTypeDef(BaseValidatorModel):
    MetadataKeyValue: MetadataKeyValuePairTypeDef
    SchemaId: Optional[SchemaIdTypeDef] = None
    SchemaVersionNumber: Optional[SchemaVersionNumberTypeDef] = None
    SchemaVersionId: Optional[str] = None

class OAuth2PropertiesInputTypeDef(BaseValidatorModel):
    OAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    OAuth2ClientApplication: Optional[OAuth2ClientApplicationTypeDef] = None
    TokenUrl: Optional[str] = None
    TokenUrlParametersMap: Optional[Mapping[str, str]] = None
    AuthorizationCodeProperties: Optional[AuthorizationCodePropertiesTypeDef] = None

class OAuth2PropertiesTypeDef(BaseValidatorModel):
    OAuth2GrantType: Optional[OAuth2GrantTypeType] = None
    OAuth2ClientApplication: Optional[OAuth2ClientApplicationTypeDef] = None
    TokenUrl: Optional[str] = None
    TokenUrlParametersMap: Optional[Dict[str, str]] = None

class RecipeStepExtraOutputTypeDef(BaseValidatorModel):
    Action: RecipeActionExtraOutputTypeDef
    ConditionExpressions: Optional[List[ConditionExpressionTypeDef]] = None

class RecipeStepOutputTypeDef(BaseValidatorModel):
    Action: RecipeActionOutputTypeDef
    ConditionExpressions: Optional[List[ConditionExpressionTypeDef]] = None

class RecipeStepTypeDef(BaseValidatorModel):
    Action: RecipeActionTypeDef
    ConditionExpressions: Optional[Sequence[ConditionExpressionTypeDef]] = None

class RedshiftTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str
    RedshiftTmpDir: Optional[str] = None
    TmpDirIAMRole: Optional[str] = None
    UpsertRedshiftOptions: Optional[UpsertRedshiftTargetOptionsExtraOutputTypeDef] = None

class RedshiftTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Database: str
    Table: str
    RedshiftTmpDir: Optional[str] = None
    TmpDirIAMRole: Optional[str] = None
    UpsertRedshiftOptions: Optional[UpsertRedshiftTargetOptionsOutputTypeDef] = None

class RedshiftTargetTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Database: str
    Table: str
    RedshiftTmpDir: Optional[str] = None
    TmpDirIAMRole: Optional[str] = None
    UpsertRedshiftOptions: Optional[UpsertRedshiftTargetOptionsTypeDef] = None

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

class TableOptimizerRunTypeDef(BaseValidatorModel):
    eventType: Optional[TableOptimizerEventTypeType] = None
    startTimestamp: Optional[datetime] = None
    endTimestamp: Optional[datetime] = None
    metrics: Optional[RunMetricsTypeDef] = None
    error: Optional[str] = None

class SearchTablesRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: Optional[str] = None
    NextToken: Optional[str] = None
    Filters: Optional[Sequence[PropertyPredicateTypeDef]] = None
    SearchText: Optional[str] = None
    SortCriteria: Optional[Sequence[SortCriterionTypeDef]] = None
    MaxResults: Optional[int] = None
    ResourceShareType: Optional[ResourceShareTypeType] = None

class StatementOutputTypeDef(BaseValidatorModel):
    Data: Optional[StatementOutputDataTypeDef] = None
    ExecutionCount: Optional[int] = None
    Status: Optional[StatementStateType] = None
    ErrorName: Optional[str] = None
    ErrorValue: Optional[str] = None
    Traceback: Optional[List[str]] = None

class UpdateClassifierRequestRequestTypeDef(BaseValidatorModel):
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

class AmazonRedshiftSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataExtraOutputTypeDef] = None

class AmazonRedshiftTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataExtraOutputTypeDef] = None
    Inputs: Optional[List[str]] = None

class AmazonRedshiftSourceOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataOutputTypeDef] = None

class AmazonRedshiftTargetOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataOutputTypeDef] = None
    Inputs: Optional[List[str]] = None

class AmazonRedshiftSourceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataTypeDef] = None

class AmazonRedshiftTargetTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Data: Optional[AmazonRedshiftNodeDataTypeDef] = None
    Inputs: Optional[Sequence[str]] = None

class SnowflakeTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Data: SnowflakeNodeDataExtraOutputTypeDef
    Inputs: Optional[List[str]] = None

class SnowflakeTargetOutputTypeDef(BaseValidatorModel):
    Name: str
    Data: SnowflakeNodeDataOutputTypeDef
    Inputs: Optional[List[str]] = None

class SnowflakeTargetTypeDef(BaseValidatorModel):
    Name: str
    Data: SnowflakeNodeDataTypeDef
    Inputs: Optional[Sequence[str]] = None

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

class DecimalColumnStatisticsDataTypeDef(BaseValidatorModel):
    NumberOfNulls: int
    NumberOfDistinctValues: int
    MinimumValue: Optional[DecimalNumberTypeDef] = None
    MaximumValue: Optional[DecimalNumberTypeDef] = None

class BatchGetBlueprintsResponseTypeDef(BaseValidatorModel):
    Blueprints: List[BlueprintTypeDef]
    MissingBlueprints: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetBlueprintResponseTypeDef(BaseValidatorModel):
    Blueprint: BlueprintTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

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

class GetMappingRequestRequestTypeDef(BaseValidatorModel):
    Source: CatalogEntryTypeDef
    Sinks: Optional[Sequence[CatalogEntryTypeDef]] = None
    Location: Optional[LocationTypeDef] = None

class GetPlanRequestRequestTypeDef(BaseValidatorModel):
    Mapping: Sequence[MappingEntryTypeDef]
    Source: CatalogEntryTypeDef
    Sinks: Optional[Sequence[CatalogEntryTypeDef]] = None
    Location: Optional[LocationTypeDef] = None
    Language: Optional[LanguageType] = None
    AdditionalPlanOptionsMap: Optional[Mapping[str, str]] = None

class CatalogKafkaSourceTypeDef(BaseValidatorModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KafkaStreamingSourceOptionsTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class DirectKafkaSourceTypeDef(BaseValidatorModel):
    Name: str
    StreamingOptions: Optional[KafkaStreamingSourceOptionsTypeDef] = None
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class CatalogKinesisSourceTypeDef(BaseValidatorModel):
    Name: str
    Table: str
    Database: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class DirectKinesisSourceTypeDef(BaseValidatorModel):
    Name: str
    WindowSize: Optional[int] = None
    DetectSchema: Optional[bool] = None
    StreamingOptions: Optional[KinesisStreamingSourceOptionsTypeDef] = None
    DataPreviewOptions: Optional[StreamingDataPreviewOptionsTypeDef] = None

class GetUnfilteredPartitionMetadataRequestRequestTypeDef(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    SupportedPermissionTypes: Sequence[PermissionTypeType]
    Region: Optional[str] = None
    AuditContext: Optional[AuditContextTypeDef] = None
    QuerySessionContext: Optional[QuerySessionContextTypeDef] = None

class GetUnfilteredPartitionsMetadataRequestRequestTypeDef(BaseValidatorModel):
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

class GetUnfilteredTableMetadataRequestRequestTypeDef(BaseValidatorModel):
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

class GetMLTaskRunsRequestRequestTypeDef(BaseValidatorModel):
    TransformId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[TaskRunFilterCriteriaTypeDef] = None
    Sort: Optional[TaskRunSortCriteriaTypeDef] = None

class TriggerTypeDef(BaseValidatorModel):
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

class TriggerUpdateTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Schedule: Optional[str] = None
    Actions: Optional[Sequence[ActionTypeDef]] = None
    Predicate: Optional[PredicateTypeDef] = None
    EventBatchingCondition: Optional[EventBatchingConditionTypeDef] = None

class GetUsageProfileResponseTypeDef(BaseValidatorModel):
    Name: str
    Description: str
    Configuration: ProfileConfigurationOutputTypeDef
    CreatedOn: datetime
    LastModifiedOn: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUsageProfileRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Configuration: ProfileConfigurationTypeDef
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateUsageProfileRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    Configuration: ProfileConfigurationTypeDef
    Description: Optional[str] = None

class EvaluationMetricsTypeDef(BaseValidatorModel):
    TransformType: Literal["FIND_MATCHES"]
    FindMatchesMetrics: Optional[FindMatchesMetricsTypeDef] = None

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

class CreateCrawlerRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateCrawlerRequestRequestTypeDef(BaseValidatorModel):
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

class ListDataQualityRulesetsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[DataQualityRulesetFilterCriteriaTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class ListDataQualityRulesetsResponseTypeDef(BaseValidatorModel):
    Rulesets: List[DataQualityRulesetListDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

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

class PutDataCatalogEncryptionSettingsRequestRequestTypeDef(BaseValidatorModel):
    DataCatalogEncryptionSettings: DataCatalogEncryptionSettingsTypeDef
    CatalogId: Optional[str] = None

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

class DatabaseInputTypeDef(BaseValidatorModel):
    Name: str
    Description: Optional[str] = None
    LocationUri: Optional[str] = None
    Parameters: Optional[Mapping[str, str]] = None
    CreateTableDefaultPermissions: Optional[Sequence[PrincipalPermissionsTypeDef]] = None
    TargetDatabase: Optional[DatabaseIdentifierTypeDef] = None
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

class DataQualityResultFilterCriteriaTypeDef(BaseValidatorModel):
    DataSource: Optional[DataSourceTypeDef] = None
    JobName: Optional[str] = None
    JobRunId: Optional[str] = None
    StartedAfter: Optional[TimestampTypeDef] = None
    StartedBefore: Optional[TimestampTypeDef] = None

class DataQualityRuleRecommendationRunFilterTypeDef(BaseValidatorModel):
    DataSource: DataSourceTypeDef
    StartedBefore: Optional[TimestampTypeDef] = None
    StartedAfter: Optional[TimestampTypeDef] = None

class DataQualityRulesetEvaluationRunFilterTypeDef(BaseValidatorModel):
    DataSource: DataSourceTypeDef
    StartedBefore: Optional[TimestampTypeDef] = None
    StartedAfter: Optional[TimestampTypeDef] = None

class StartDataQualityRuleRecommendationRunRequestRequestTypeDef(BaseValidatorModel):
    DataSource: DataSourceTypeDef
    Role: str
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    CreatedRulesetName: Optional[str] = None
    ClientToken: Optional[str] = None

class DropNullFieldsExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    NullCheckBoxList: Optional[NullCheckBoxListTypeDef] = None
    NullTextList: Optional[List[NullValueFieldTypeDef]] = None

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

class ColumnStatisticsDataOutputTypeDef(BaseValidatorModel):
    Type: ColumnStatisticsTypeType
    BooleanColumnStatisticsData: Optional[BooleanColumnStatisticsDataTypeDef] = None
    DateColumnStatisticsData: Optional[DateColumnStatisticsDataOutputTypeDef] = None
    DecimalColumnStatisticsData: Optional[DecimalColumnStatisticsDataOutputTypeDef] = None
    DoubleColumnStatisticsData: Optional[DoubleColumnStatisticsDataTypeDef] = None
    LongColumnStatisticsData: Optional[LongColumnStatisticsDataTypeDef] = None
    StringColumnStatisticsData: Optional[StringColumnStatisticsDataTypeDef] = None
    BinaryColumnStatisticsData: Optional[BinaryColumnStatisticsDataTypeDef] = None

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

class StorageDescriptorTypeDef(BaseValidatorModel):
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

class SecurityConfigurationTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    CreatedTimeStamp: Optional[datetime] = None
    EncryptionConfiguration: Optional[EncryptionConfigurationOutputTypeDef] = None

class CreateSecurityConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    EncryptionConfiguration: EncryptionConfigurationTypeDef

class DeleteSchemaVersionsResponseTypeDef(BaseValidatorModel):
    SchemaVersionErrors: List[SchemaVersionErrorItemTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FilterExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    LogicalOperator: FilterLogicalOperatorType
    Filters: List[FilterExpressionExtraOutputTypeDef]

class FilterOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    LogicalOperator: FilterLogicalOperatorType
    Filters: List[FilterExpressionOutputTypeDef]

class FilterTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    LogicalOperator: FilterLogicalOperatorType
    Filters: Sequence[FilterExpressionTypeDef]

class UpdateMLTransformRequestRequestTypeDef(BaseValidatorModel):
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

class GetMLTransformsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[TransformFilterCriteriaTypeDef] = None
    Sort: Optional[TransformSortCriteriaTypeDef] = None

class ListMLTransformsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Filter: Optional[TransformFilterCriteriaTypeDef] = None
    Sort: Optional[TransformSortCriteriaTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class AthenaConnectorSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    SchemaName: str
    ConnectionTable: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class CatalogDeltaSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class CatalogHudiSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class ConnectorDataSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    ConnectionType: str
    Data: Dict[str, str]
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class CustomCodeExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    Code: str
    ClassName: str
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class DynamicTransformExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    TransformName: str
    Inputs: List[str]
    FunctionName: str
    Path: str
    Parameters: Optional[List[TransformConfigParameterExtraOutputTypeDef]] = None
    Version: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class JDBCConnectorSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[JDBCConnectorOptionsExtraOutputTypeDef] = None
    ConnectionTable: Optional[str] = None
    Query: Optional[str] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class JDBCConnectorTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    ConnectionName: str
    ConnectionTable: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class S3CatalogDeltaSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class S3CatalogHudiSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Database: str
    Table: str
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class S3CsvSourceExtraOutputTypeDef(BaseValidatorModel):
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

class S3DeltaSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Paths: List[str]
    AdditionalDeltaOptions: Optional[Dict[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class S3HudiSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Paths: List[str]
    AdditionalHudiOptions: Optional[Dict[str, str]] = None
    AdditionalOptions: Optional[S3DirectSourceAdditionalOptionsTypeDef] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class S3JsonSourceExtraOutputTypeDef(BaseValidatorModel):
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

class S3ParquetSourceExtraOutputTypeDef(BaseValidatorModel):
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

class SnowflakeSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Data: SnowflakeNodeDataExtraOutputTypeDef
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class SparkConnectorSourceExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class SparkConnectorTargetExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[Dict[str, str]] = None
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

class SparkSQLExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    SqlQuery: str
    SqlAliases: List[SqlAliasTypeDef]
    OutputSchemas: Optional[List[GlueSchemaExtraOutputTypeDef]] = None

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

class ConnectorDataSourceTypeDef(BaseValidatorModel):
    Name: str
    ConnectionType: str
    Data: Mapping[str, str]
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class CustomCodeTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    Code: str
    ClassName: str
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class DynamicTransformTypeDef(BaseValidatorModel):
    Name: str
    TransformName: str
    Inputs: Sequence[str]
    FunctionName: str
    Path: str
    Parameters: Optional[Sequence[TransformConfigParameterTypeDef]] = None
    Version: Optional[str] = None
    OutputSchemas: Optional[Sequence[GlueSchemaTypeDef]] = None

class JDBCConnectorSourceTypeDef(BaseValidatorModel):
    Name: str
    ConnectionName: str
    ConnectorName: str
    ConnectionType: str
    AdditionalOptions: Optional[JDBCConnectorOptionsTypeDef] = None
    ConnectionTable: Optional[str] = None
    Query: Optional[str] = None
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

class SnowflakeSourceTypeDef(BaseValidatorModel):
    Name: str
    Data: SnowflakeNodeDataTypeDef
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

class GetJobRunResponseTypeDef(BaseValidatorModel):
    JobRun: JobRunTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetJobRunsResponseTypeDef(BaseValidatorModel):
    JobRuns: List[JobRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class JobNodeDetailsTypeDef(BaseValidatorModel):
    JobRuns: Optional[List[JobRunTypeDef]] = None

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

class CreateMLTransformRequestRequestTypeDef(BaseValidatorModel):
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

class AuthenticationConfigurationInputTypeDef(BaseValidatorModel):
    AuthenticationType: Optional[AuthenticationTypeType] = None
    SecretArn: Optional[str] = None
    OAuth2Properties: Optional[OAuth2PropertiesInputTypeDef] = None

class AuthenticationConfigurationTypeDef(BaseValidatorModel):
    AuthenticationType: Optional[AuthenticationTypeType] = None
    SecretArn: Optional[str] = None
    OAuth2Properties: Optional[OAuth2PropertiesTypeDef] = None

class BatchDeletePartitionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionsToDelete: Sequence[PartitionValueListUnionTypeDef]
    CatalogId: Optional[str] = None

class BatchGetPartitionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionsToGet: Sequence[PartitionValueListUnionTypeDef]
    CatalogId: Optional[str] = None

class RecipeExtraOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    RecipeSteps: Optional[List[RecipeStepExtraOutputTypeDef]] = None

class RecipeOutputTypeDef(BaseValidatorModel):
    Name: str
    Inputs: List[str]
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    RecipeSteps: Optional[List[RecipeStepOutputTypeDef]] = None

class RecipeTypeDef(BaseValidatorModel):
    Name: str
    Inputs: Sequence[str]
    RecipeReference: Optional[RecipeReferenceTypeDef] = None
    RecipeSteps: Optional[Sequence[RecipeStepTypeDef]] = None

class CreateUserDefinedFunctionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    FunctionInput: UserDefinedFunctionInputTypeDef
    CatalogId: Optional[str] = None

class UpdateUserDefinedFunctionRequestRequestTypeDef(BaseValidatorModel):
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

class ListTableOptimizerRunsResponseTypeDef(BaseValidatorModel):
    CatalogId: str
    DatabaseName: str
    TableName: str
    TableOptimizerRuns: List[TableOptimizerRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TableOptimizerTypeDef(BaseValidatorModel):
    type: Optional[Literal["compaction"]] = None
    configuration: Optional[TableOptimizerConfigurationTypeDef] = None
    lastRun: Optional[TableOptimizerRunTypeDef] = None

class StatementTypeDef(BaseValidatorModel):
    Id: Optional[int] = None
    Code: Optional[str] = None
    State: Optional[StatementStateType] = None
    Output: Optional[StatementOutputTypeDef] = None
    Progress: Optional[float] = None
    StartedOn: Optional[int] = None
    CompletedOn: Optional[int] = None

class CreateTriggerRequestRequestTypeDef(BaseValidatorModel):
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

class GetPartitionIndexesResponseTypeDef(BaseValidatorModel):
    PartitionIndexDescriptorList: List[PartitionIndexDescriptorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ColumnStatisticsDataTypeDef(BaseValidatorModel):
    Type: ColumnStatisticsTypeType
    BooleanColumnStatisticsData: Optional[BooleanColumnStatisticsDataTypeDef] = None
    DateColumnStatisticsData: Optional[DateColumnStatisticsDataTypeDef] = None
    DecimalColumnStatisticsData: Optional[DecimalColumnStatisticsDataTypeDef] = None
    DoubleColumnStatisticsData: Optional[DoubleColumnStatisticsDataTypeDef] = None
    LongColumnStatisticsData: Optional[LongColumnStatisticsDataTypeDef] = None
    StringColumnStatisticsData: Optional[StringColumnStatisticsDataTypeDef] = None
    BinaryColumnStatisticsData: Optional[BinaryColumnStatisticsDataTypeDef] = None

class CreateScriptRequestRequestTypeDef(BaseValidatorModel):
    DagNodes: Optional[Sequence[CodeGenNodeUnionTypeDef]] = None
    DagEdges: Optional[Sequence[CodeGenEdgeTypeDef]] = None
    Language: Optional[LanguageType] = None

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

class UpdateTriggerRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    TriggerUpdate: TriggerUpdateTypeDef

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

class GetDatabaseResponseTypeDef(BaseValidatorModel):
    Database: DatabaseTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDatabasesResponseTypeDef(BaseValidatorModel):
    DatabaseList: List[DatabaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateDatabaseRequestRequestTypeDef(BaseValidatorModel):
    DatabaseInput: DatabaseInputTypeDef
    CatalogId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateDatabaseRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    DatabaseInput: DatabaseInputTypeDef
    CatalogId: Optional[str] = None

class DataQualityResultTypeDef(BaseValidatorModel):
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

class GetDataQualityResultResponseTypeDef(BaseValidatorModel):
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

class ListDataQualityResultsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[DataQualityResultFilterCriteriaTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataQualityRuleRecommendationRunsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[DataQualityRuleRecommendationRunFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListDataQualityRulesetEvaluationRunsRequestRequestTypeDef(BaseValidatorModel):
    Filter: Optional[DataQualityRulesetEvaluationRunFilterTypeDef] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class StartDataQualityRulesetEvaluationRunRequestRequestTypeDef(BaseValidatorModel):
    DataSource: DataSourceTypeDef
    Role: str
    RulesetNames: Sequence[str]
    NumberOfWorkers: Optional[int] = None
    Timeout: Optional[int] = None
    ClientToken: Optional[str] = None
    AdditionalRunOptions: Optional[DataQualityEvaluationRunAdditionalRunOptionsTypeDef] = None
    AdditionalDataSources: Optional[Mapping[str, DataSourceUnionTypeDef]] = None

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

class PartitionInputTypeDef(BaseValidatorModel):
    Values: Optional[Sequence[str]] = None
    LastAccessTime: Optional[TimestampTypeDef] = None
    StorageDescriptor: Optional[StorageDescriptorTypeDef] = None
    Parameters: Optional[Mapping[str, str]] = None
    LastAnalyzedTime: Optional[TimestampTypeDef] = None

class TableInputTypeDef(BaseValidatorModel):
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

class GetSecurityConfigurationResponseTypeDef(BaseValidatorModel):
    SecurityConfiguration: SecurityConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSecurityConfigurationsResponseTypeDef(BaseValidatorModel):
    SecurityConfigurations: List[SecurityConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetMLTaskRunsResponseTypeDef(BaseValidatorModel):
    TaskRuns: List[TaskRunTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ConnectionInputTypeDef(BaseValidatorModel):
    Name: str
    ConnectionType: ConnectionTypeType
    ConnectionProperties: Mapping[ConnectionPropertyKeyType, str]
    Description: Optional[str] = None
    MatchCriteria: Optional[Sequence[str]] = None
    PhysicalConnectionRequirements: Optional[PhysicalConnectionRequirementsTypeDef] = None
    AuthenticationConfiguration: Optional[AuthenticationConfigurationInputTypeDef] = None
    ValidateCredentials: Optional[bool] = None

class ConnectionTypeDef(BaseValidatorModel):
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

class CodeGenConfigurationNodeExtraOutputTypeDef(BaseValidatorModel):
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

class CodeGenConfigurationNodeOutputTypeDef(BaseValidatorModel):
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

class CodeGenConfigurationNodeTypeDef(BaseValidatorModel):
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

class GetStatementResponseTypeDef(BaseValidatorModel):
    Statement: StatementTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListStatementsResponseTypeDef(BaseValidatorModel):
    Statements: List[StatementTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ColumnStatisticsTypeDef(BaseValidatorModel):
    ColumnName: str
    ColumnType: str
    AnalyzedTime: TimestampTypeDef
    StatisticsData: ColumnStatisticsDataTypeDef

class NodeTypeDef(BaseValidatorModel):
    Type: Optional[NodeTypeType] = None
    Name: Optional[str] = None
    UniqueId: Optional[str] = None
    TriggerDetails: Optional[TriggerNodeDetailsTypeDef] = None
    JobDetails: Optional[JobNodeDetailsTypeDef] = None
    CrawlerDetails: Optional[CrawlerNodeDetailsTypeDef] = None

class GetMLTransformsResponseTypeDef(BaseValidatorModel):
    Transforms: List[MLTransformTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

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

class BatchCreatePartitionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionInputList: Sequence[PartitionInputTypeDef]
    CatalogId: Optional[str] = None

class BatchUpdatePartitionRequestEntryTypeDef(BaseValidatorModel):
    PartitionValueList: Sequence[str]
    PartitionInput: PartitionInputTypeDef

class CreatePartitionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionInput: PartitionInputTypeDef
    CatalogId: Optional[str] = None

class UpdatePartitionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValueList: Sequence[str]
    PartitionInput: PartitionInputTypeDef
    CatalogId: Optional[str] = None

class CreateTableRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableInput: TableInputTypeDef
    CatalogId: Optional[str] = None
    PartitionIndexes: Optional[Sequence[PartitionIndexTypeDef]] = None
    TransactionId: Optional[str] = None
    OpenTableFormatInput: Optional[OpenTableFormatInputTypeDef] = None

class UpdateTableRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableInput: TableInputTypeDef
    CatalogId: Optional[str] = None
    SkipArchive: Optional[bool] = None
    TransactionId: Optional[str] = None
    VersionId: Optional[str] = None
    ViewUpdateAction: Optional[ViewUpdateActionType] = None
    Force: Optional[bool] = None

class CreateConnectionRequestRequestTypeDef(BaseValidatorModel):
    ConnectionInput: ConnectionInputTypeDef
    CatalogId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateConnectionRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ConnectionInput: ConnectionInputTypeDef
    CatalogId: Optional[str] = None

class GetConnectionResponseTypeDef(BaseValidatorModel):
    Connection: ConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectionsResponseTypeDef(BaseValidatorModel):
    ConnectionList: List[ConnectionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class JobTypeDef(BaseValidatorModel):
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

class JobUpdateTypeDef(BaseValidatorModel):
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

class BatchGetTableOptimizerResponseTypeDef(BaseValidatorModel):
    TableOptimizers: List[BatchTableOptimizerTypeDef]
    Failures: List[BatchGetTableOptimizerErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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

class GetTableVersionResponseTypeDef(BaseValidatorModel):
    TableVersion: TableVersionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetTableVersionsResponseTypeDef(BaseValidatorModel):
    TableVersions: List[TableVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchUpdatePartitionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    Entries: Sequence[BatchUpdatePartitionRequestEntryTypeDef]
    CatalogId: Optional[str] = None

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

class CreateJobRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateJobRequestRequestTypeDef(BaseValidatorModel):
    JobName: str
    JobUpdate: JobUpdateTypeDef

class UpdateColumnStatisticsForPartitionRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    PartitionValues: Sequence[str]
    ColumnStatisticsList: Sequence[ColumnStatisticsUnionTypeDef]
    CatalogId: Optional[str] = None

class UpdateColumnStatisticsForTableRequestRequestTypeDef(BaseValidatorModel):
    DatabaseName: str
    TableName: str
    ColumnStatisticsList: Sequence[ColumnStatisticsUnionTypeDef]
    CatalogId: Optional[str] = None

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

