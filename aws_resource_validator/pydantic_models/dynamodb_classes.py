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
from aws_resource_validator.pydantic_models.dynamodb_constants import *

class ArchivalSummary(BaseValidatorModel):
    ArchivalDateTime: Optional[datetime] = None
    ArchivalReason: Optional[str] = None
    ArchivalBackupArn: Optional[str] = None


class AttributeDefinition(BaseValidatorModel):
    AttributeName: str
    AttributeType: ScalarAttributeTypeType


class AttributeValue(BaseValidatorModel):
    S: Optional[str] = None
    N: Optional[str] = None
    B: Optional[bytes] = None
    SS: Optional[Sequence[str]] = None
    NS: Optional[Sequence[str]] = None
    BS: Optional[Sequence[bytes]] = None
    M: Optional[Mapping[str, Any]] = None
    L: Optional[Sequence[Any]] = None
    NULL: Optional[bool] = None
    BOOL: Optional[bool] = None


class AutoScalingTargetTrackingScalingPolicyConfigurationDescription(BaseValidatorModel):
    TargetValue: float
    DisableScaleIn: Optional[bool] = None
    ScaleInCooldown: Optional[int] = None
    ScaleOutCooldown: Optional[int] = None


class AutoScalingTargetTrackingScalingPolicyConfigurationUpdate(BaseValidatorModel):
    TargetValue: float
    DisableScaleIn: Optional[bool] = None
    ScaleInCooldown: Optional[int] = None
    ScaleOutCooldown: Optional[int] = None


class BackupDetails(BaseValidatorModel):
    BackupArn: str
    BackupName: str
    BackupStatus: BackupStatusType
    BackupType: BackupTypeType
    BackupCreationDateTime: datetime
    BackupSizeBytes: Optional[int] = None
    BackupExpiryDateTime: Optional[datetime] = None


class BackupSummary(BaseValidatorModel):
    TableName: Optional[str] = None
    TableId: Optional[str] = None
    TableArn: Optional[str] = None
    BackupArn: Optional[str] = None
    BackupName: Optional[str] = None
    BackupCreationDateTime: Optional[datetime] = None
    BackupExpiryDateTime: Optional[datetime] = None
    BackupStatus: Optional[BackupStatusType] = None
    BackupType: Optional[BackupTypeType] = None
    BackupSizeBytes: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BillingModeSummary(BaseValidatorModel):
    BillingMode: Optional[BillingModeType] = None
    LastUpdateToPayPerRequestDateTime: Optional[datetime] = None


class Capacity(BaseValidatorModel):
    ReadCapacityUnits: Optional[float] = None
    WriteCapacityUnits: Optional[float] = None
    CapacityUnits: Optional[float] = None


class PointInTimeRecoveryDescription(BaseValidatorModel):
    PointInTimeRecoveryStatus: Optional[PointInTimeRecoveryStatusType] = None
    RecoveryPeriodInDays: Optional[int] = None
    EarliestRestorableDateTime: Optional[datetime] = None
    LatestRestorableDateTime: Optional[datetime] = None


class ContributorInsightsSummary(BaseValidatorModel):
    TableName: Optional[str] = None
    IndexName: Optional[str] = None
    ContributorInsightsStatus: Optional[ContributorInsightsStatusType] = None


class CreateBackupInput(BaseValidatorModel):
    TableName: str
    BackupName: str


class KeySchemaElement(BaseValidatorModel):
    AttributeName: str
    KeyType: KeyTypeType


class OnDemandThroughput(BaseValidatorModel):
    MaxReadRequestUnits: Optional[int] = None
    MaxWriteRequestUnits: Optional[int] = None


class ProvisionedThroughput(BaseValidatorModel):
    ReadCapacityUnits: int
    WriteCapacityUnits: int


class WarmThroughput(BaseValidatorModel):
    ReadUnitsPerSecond: Optional[int] = None
    WriteUnitsPerSecond: Optional[int] = None


class OnDemandThroughputOverride(BaseValidatorModel):
    MaxReadRequestUnits: Optional[int] = None


class ProvisionedThroughputOverride(BaseValidatorModel):
    ReadCapacityUnits: Optional[int] = None


class SSESpecification(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SSEType: Optional[SSETypeType] = None
    KMSMasterKeyId: Optional[str] = None


class StreamSpecification(BaseValidatorModel):
    StreamEnabled: bool
    StreamViewType: Optional[StreamViewTypeType] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class CsvOptionsOutput(BaseValidatorModel):
    Delimiter: Optional[str] = None
    HeaderList: Optional[List[str]] = None


class CsvOptions(BaseValidatorModel):
    Delimiter: Optional[str] = None
    HeaderList: Optional[Sequence[str]] = None


class DeleteBackupInput(BaseValidatorModel):
    BackupArn: str


class DeleteGlobalSecondaryIndexAction(BaseValidatorModel):
    IndexName: str


class DeleteResourcePolicyInput(BaseValidatorModel):
    ResourceArn: str
    ExpectedRevisionId: Optional[str] = None


class DeleteTableInput(BaseValidatorModel):
    TableName: str


class DescribeBackupInput(BaseValidatorModel):
    BackupArn: str


class DescribeContinuousBackupsInput(BaseValidatorModel):
    TableName: str


class DescribeContributorInsightsInput(BaseValidatorModel):
    TableName: str
    IndexName: Optional[str] = None


class FailureException(BaseValidatorModel):
    ExceptionName: Optional[str] = None
    ExceptionDescription: Optional[str] = None


class Endpoint(BaseValidatorModel):
    Address: str
    CachePeriodInMinutes: int


class DescribeExportInput(BaseValidatorModel):
    ExportArn: str


class DescribeGlobalTableInput(BaseValidatorModel):
    GlobalTableName: str


class DescribeGlobalTableSettingsInput(BaseValidatorModel):
    GlobalTableName: str


class DescribeImportInput(BaseValidatorModel):
    ImportArn: str


class DescribeKinesisStreamingDestinationInput(BaseValidatorModel):
    TableName: str


class KinesisDataStreamDestination(BaseValidatorModel):
    StreamArn: Optional[str] = None
    DestinationStatus: Optional[DestinationStatusType] = None
    DestinationStatusDescription: Optional[str] = None
    ApproximateCreationDateTimePrecision: Optional[ApproximateCreationDateTimePrecisionType] = None


class DescribeTableInput(BaseValidatorModel):
    TableName: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeTableReplicaAutoScalingInput(BaseValidatorModel):
    TableName: str


class DescribeTimeToLiveInput(BaseValidatorModel):
    TableName: str


class TimeToLiveDescription(BaseValidatorModel):
    TimeToLiveStatus: Optional[TimeToLiveStatusType] = None
    AttributeName: Optional[str] = None


class EnableKinesisStreamingConfiguration(BaseValidatorModel):
    ApproximateCreationDateTimePrecision: Optional[ApproximateCreationDateTimePrecisionType] = None


class IncrementalExportSpecificationOutput(BaseValidatorModel):
    ExportFromTime: Optional[datetime] = None
    ExportToTime: Optional[datetime] = None
    ExportViewType: Optional[ExportViewTypeType] = None


class ExportSummary(BaseValidatorModel):
    ExportArn: Optional[str] = None
    ExportStatus: Optional[ExportStatusType] = None
    ExportType: Optional[ExportTypeType] = None


class GetResourcePolicyInput(BaseValidatorModel):
    ResourceArn: str


class GlobalSecondaryIndexWarmThroughputDescription(BaseValidatorModel):
    ReadUnitsPerSecond: Optional[int] = None
    WriteUnitsPerSecond: Optional[int] = None
    Status: Optional[IndexStatusType] = None


class ProjectionOutput(BaseValidatorModel):
    ProjectionType: Optional[ProjectionTypeType] = None
    NonKeyAttributes: Optional[List[str]] = None


class ProvisionedThroughputDescription(BaseValidatorModel):
    LastIncreaseDateTime: Optional[datetime] = None
    LastDecreaseDateTime: Optional[datetime] = None
    NumberOfDecreasesToday: Optional[int] = None
    ReadCapacityUnits: Optional[int] = None
    WriteCapacityUnits: Optional[int] = None


class S3BucketSource(BaseValidatorModel):
    S3Bucket: str
    S3BucketOwner: Optional[str] = None
    S3KeyPrefix: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListContributorInsightsInput(BaseValidatorModel):
    TableName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListExportsInput(BaseValidatorModel):
    TableArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListImportsInput(BaseValidatorModel):
    TableArn: Optional[str] = None
    PageSize: Optional[int] = None
    NextToken: Optional[str] = None


class ListTablesInput(BaseValidatorModel):
    ExclusiveStartTableName: Optional[str] = None
    Limit: Optional[int] = None


class ListTagsOfResourceInput(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None


class PointInTimeRecoverySpecification(BaseValidatorModel):
    PointInTimeRecoveryEnabled: bool
    RecoveryPeriodInDays: Optional[int] = None


class Projection(BaseValidatorModel):
    ProjectionType: Optional[ProjectionTypeType] = None
    NonKeyAttributes: Optional[Sequence[str]] = None


class PutResourcePolicyInput(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    ExpectedRevisionId: Optional[str] = None
    ConfirmRemoveSelfResourceAccess: Optional[bool] = None


class TableClassSummary(BaseValidatorModel):
    TableClass: Optional[TableClassType] = None
    LastUpdateDateTime: Optional[datetime] = None


class TableWarmThroughputDescription(BaseValidatorModel):
    ReadUnitsPerSecond: Optional[int] = None
    WriteUnitsPerSecond: Optional[int] = None
    Status: Optional[TableStatusType] = None


class RestoreSummary(BaseValidatorModel):
    RestoreDateTime: datetime
    RestoreInProgress: bool
    SourceBackupArn: Optional[str] = None
    SourceTableArn: Optional[str] = None


class SSEDescription(BaseValidatorModel):
    Status: Optional[SSEStatusType] = None
    SSEType: Optional[SSETypeType] = None
    KMSMasterKeyArn: Optional[str] = None
    InaccessibleEncryptionDateTime: Optional[datetime] = None


class TableBatchWriterRequest(BaseValidatorModel):
    overwrite_by_pkeys: Optional[List[str]] = None


class TimeToLiveSpecification(BaseValidatorModel):
    Enabled: bool
    AttributeName: str


class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateContributorInsightsInput(BaseValidatorModel):
    TableName: str
    ContributorInsightsAction: ContributorInsightsActionType
    IndexName: Optional[str] = None


class UpdateKinesisStreamingConfiguration(BaseValidatorModel):
    ApproximateCreationDateTimePrecision: Optional[ApproximateCreationDateTimePrecisionType] = None


class BatchStatementError(BaseValidatorModel):
    Code: Optional[BatchStatementErrorCodeEnumType] = None
    Message: Optional[str] = None
    Item: Optional[Dict[str, AttributeValue]] = None


class DeleteRequestOutput(BaseValidatorModel):
    Key: Dict[str, AttributeValue]


class ItemCollectionMetrics(BaseValidatorModel):
    ItemCollectionKey: Optional[Dict[str, AttributeValue]] = None
    SizeEstimateRangeGB: Optional[List[float]] = None


class ItemResponse(BaseValidatorModel):
    Item: Optional[Dict[str, AttributeValue]] = None


class KeysAndAttributesOutput(BaseValidatorModel):
    Keys: List[Dict[str, AttributeValue]]
    AttributesToGet: Optional[List[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None


class PutRequestOutput(BaseValidatorModel):
    Item: Dict[str, AttributeValue]


class TableAttributeValue(BaseValidatorModel):
    pass


class AttributeValueUpdateTable(BaseValidatorModel):
    Value: Optional[TableAttributeValue] = None
    Action: Optional[AttributeActionType] = None


class ConditionTable(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    AttributeValueList: Optional[Sequence[TableAttributeValue]] = None


class DeleteRequestServiceResourceOutput(BaseValidatorModel):
    Key: Dict[str, TableAttributeValue]


class DeleteRequestServiceResource(BaseValidatorModel):
    Key: Mapping[str, TableAttributeValue]


class ExpectedAttributeValueTable(BaseValidatorModel):
    Value: Optional[TableAttributeValue] = None
    Exists: Optional[bool] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    AttributeValueList: Optional[Sequence[TableAttributeValue]] = None


class GetItemInputTableGetItem(BaseValidatorModel):
    Key: Mapping[str, TableAttributeValue]
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None


class ItemCollectionMetricsServiceResource(BaseValidatorModel):
    ItemCollectionKey: Optional[Dict[str, TableAttributeValue]] = None
    SizeEstimateRangeGB: Optional[List[float]] = None


class ItemCollectionMetricsTable(BaseValidatorModel):
    ItemCollectionKey: Optional[Dict[str, TableAttributeValue]] = None
    SizeEstimateRangeGB: Optional[List[float]] = None


class KeysAndAttributesServiceResourceOutput(BaseValidatorModel):
    Keys: List[Dict[str, TableAttributeValue]]
    AttributesToGet: Optional[List[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None


class KeysAndAttributesServiceResource(BaseValidatorModel):
    Keys: Sequence[Mapping[str, TableAttributeValue]]
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None


class PutRequestServiceResourceOutput(BaseValidatorModel):
    Item: Dict[str, TableAttributeValue]


class PutRequestServiceResource(BaseValidatorModel):
    Item: Mapping[str, TableAttributeValue]


class AutoScalingPolicyDescription(BaseValidatorModel):
    PolicyName: Optional[str] = None
    TargetTrackingScalingPolicyConfiguration: Optional[ AutoScalingTargetTrackingScalingPolicyConfigurationDescription ] = None


class AutoScalingPolicyUpdate(BaseValidatorModel):
    TargetTrackingScalingPolicyConfiguration: ( AutoScalingTargetTrackingScalingPolicyConfigurationUpdate )
    PolicyName: Optional[str] = None


class CreateBackupOutput(BaseValidatorModel):
    BackupDetails: BackupDetails
    ResponseMetadata: ResponseMetadata


class DeleteResourcePolicyOutput(BaseValidatorModel):
    RevisionId: str
    ResponseMetadata: ResponseMetadata


class DescribeLimitsOutput(BaseValidatorModel):
    AccountMaxReadCapacityUnits: int
    AccountMaxWriteCapacityUnits: int
    TableMaxReadCapacityUnits: int
    TableMaxWriteCapacityUnits: int
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetResourcePolicyOutput(BaseValidatorModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadata


class ListBackupsOutput(BaseValidatorModel):
    BackupSummaries: List[BackupSummary]
    LastEvaluatedBackupArn: str
    ResponseMetadata: ResponseMetadata


class ListTablesOutput(BaseValidatorModel):
    TableNames: List[str]
    LastEvaluatedTableName: str
    ResponseMetadata: ResponseMetadata


class PutResourcePolicyOutput(BaseValidatorModel):
    RevisionId: str
    ResponseMetadata: ResponseMetadata


class UpdateContributorInsightsOutput(BaseValidatorModel):
    TableName: str
    IndexName: str
    ContributorInsightsStatus: ContributorInsightsStatusType
    ResponseMetadata: ResponseMetadata


class ConsumedCapacity(BaseValidatorModel):
    TableName: Optional[str] = None
    CapacityUnits: Optional[float] = None
    ReadCapacityUnits: Optional[float] = None
    WriteCapacityUnits: Optional[float] = None
    Table: Optional[Capacity] = None
    LocalSecondaryIndexes: Optional[Dict[str, Capacity]] = None
    GlobalSecondaryIndexes: Optional[Dict[str, Capacity]] = None


class ContinuousBackupsDescription(BaseValidatorModel):
    ContinuousBackupsStatus: ContinuousBackupsStatusType
    PointInTimeRecoveryDescription: Optional[PointInTimeRecoveryDescription] = None


class ListContributorInsightsOutput(BaseValidatorModel):
    ContributorInsightsSummaries: List[ContributorInsightsSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SourceTableDetails(BaseValidatorModel):
    TableName: str
    TableId: str
    KeySchema: List[KeySchemaElement]
    TableCreationDateTime: datetime
    ProvisionedThroughput: ProvisionedThroughput
    TableArn: Optional[str] = None
    TableSizeBytes: Optional[int] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    ItemCount: Optional[int] = None
    BillingMode: Optional[BillingModeType] = None


class UpdateGlobalSecondaryIndexAction(BaseValidatorModel):
    IndexName: str
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    WarmThroughput: Optional[WarmThroughput] = None


class Replica(BaseValidatorModel):
    pass


class CreateGlobalTableInput(BaseValidatorModel):
    GlobalTableName: str
    ReplicationGroup: Sequence[Replica]


class GlobalTable(BaseValidatorModel):
    GlobalTableName: Optional[str] = None
    ReplicationGroup: Optional[List[Replica]] = None


class ReplicaGlobalSecondaryIndex(BaseValidatorModel):
    IndexName: str
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverride] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverride] = None


class ListTagsOfResourceOutput(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[Tag]


class InputFormatOptionsOutput(BaseValidatorModel):
    Csv: Optional[CsvOptionsOutput] = None


class InputFormatOptions(BaseValidatorModel):
    Csv: Optional[CsvOptions] = None


class DeleteReplicaAction(BaseValidatorModel):
    pass


class CreateReplicaAction(BaseValidatorModel):
    pass


class ReplicaUpdate(BaseValidatorModel):
    Create: Optional[CreateReplicaAction] = None
    Delete: Optional[DeleteReplicaAction] = None


class DescribeContributorInsightsOutput(BaseValidatorModel):
    TableName: str
    IndexName: str
    ContributorInsightsRuleList: List[str]
    ContributorInsightsStatus: ContributorInsightsStatusType
    LastUpdateDateTime: datetime
    FailureException: FailureException
    ResponseMetadata: ResponseMetadata


class DescribeEndpointsResponse(BaseValidatorModel):
    Endpoints: List[Endpoint]
    ResponseMetadata: ResponseMetadata


class DescribeKinesisStreamingDestinationOutput(BaseValidatorModel):
    TableName: str
    KinesisDataStreamDestinations: List[KinesisDataStreamDestination]
    ResponseMetadata: ResponseMetadata


class DescribeTableInputWaitExtra(BaseValidatorModel):
    TableName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTableInputWait(BaseValidatorModel):
    TableName: str
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTimeToLiveOutput(BaseValidatorModel):
    TimeToLiveDescription: TimeToLiveDescription
    ResponseMetadata: ResponseMetadata


class KinesisStreamingDestinationInputRequest(BaseValidatorModel):
    TableName: str
    StreamArn: str
    EnableKinesisStreamingConfiguration: Optional[EnableKinesisStreamingConfiguration] = None


class KinesisStreamingDestinationInput(BaseValidatorModel):
    TableName: str
    StreamArn: str
    EnableKinesisStreamingConfiguration: Optional[EnableKinesisStreamingConfiguration] = None


class KinesisStreamingDestinationOutput(BaseValidatorModel):
    TableName: str
    StreamArn: str
    DestinationStatus: DestinationStatusType
    EnableKinesisStreamingConfiguration: EnableKinesisStreamingConfiguration
    ResponseMetadata: ResponseMetadata


class ExportDescription(BaseValidatorModel):
    ExportArn: Optional[str] = None
    ExportStatus: Optional[ExportStatusType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ExportManifest: Optional[str] = None
    TableArn: Optional[str] = None
    TableId: Optional[str] = None
    ExportTime: Optional[datetime] = None
    ClientToken: Optional[str] = None
    S3Bucket: Optional[str] = None
    S3BucketOwner: Optional[str] = None
    S3Prefix: Optional[str] = None
    S3SseAlgorithm: Optional[S3SseAlgorithmType] = None
    S3SseKmsKeyId: Optional[str] = None
    FailureCode: Optional[str] = None
    FailureMessage: Optional[str] = None
    ExportFormat: Optional[ExportFormatType] = None
    BilledSizeBytes: Optional[int] = None
    ItemCount: Optional[int] = None
    ExportType: Optional[ExportTypeType] = None
    IncrementalExportSpecification: Optional[IncrementalExportSpecificationOutput] = None


class ListExportsOutput(BaseValidatorModel):
    ExportSummaries: List[ExportSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Timestamp(BaseValidatorModel):
    pass


class IncrementalExportSpecification(BaseValidatorModel):
    ExportFromTime: Optional[Timestamp] = None
    ExportToTime: Optional[Timestamp] = None
    ExportViewType: Optional[ExportViewTypeType] = None


class ListBackupsInput(BaseValidatorModel):
    TableName: Optional[str] = None
    Limit: Optional[int] = None
    TimeRangeLowerBound: Optional[Timestamp] = None
    TimeRangeUpperBound: Optional[Timestamp] = None
    ExclusiveStartBackupArn: Optional[str] = None
    BackupType: Optional[BackupTypeFilterType] = None


class ReplicaGlobalSecondaryIndexDescription(BaseValidatorModel):
    IndexName: Optional[str] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverride] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverride] = None
    WarmThroughput: Optional[GlobalSecondaryIndexWarmThroughputDescription] = None


class GlobalSecondaryIndexInfo(BaseValidatorModel):
    IndexName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElement]] = None
    Projection: Optional[ProjectionOutput] = None
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None


class GlobalSecondaryIndexOutput(BaseValidatorModel):
    IndexName: str
    KeySchema: List[KeySchemaElement]
    Projection: ProjectionOutput
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    WarmThroughput: Optional[WarmThroughput] = None


class LocalSecondaryIndexDescription(BaseValidatorModel):
    IndexName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElement]] = None
    Projection: Optional[ProjectionOutput] = None
    IndexSizeBytes: Optional[int] = None
    ItemCount: Optional[int] = None
    IndexArn: Optional[str] = None


class LocalSecondaryIndexInfo(BaseValidatorModel):
    IndexName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElement]] = None
    Projection: Optional[ProjectionOutput] = None


class GlobalSecondaryIndexDescription(BaseValidatorModel):
    IndexName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElement]] = None
    Projection: Optional[ProjectionOutput] = None
    IndexStatus: Optional[IndexStatusType] = None
    Backfilling: Optional[bool] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputDescription] = None
    IndexSizeBytes: Optional[int] = None
    ItemCount: Optional[int] = None
    IndexArn: Optional[str] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    WarmThroughput: Optional[GlobalSecondaryIndexWarmThroughputDescription] = None


class ImportSummary(BaseValidatorModel):
    ImportArn: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    TableArn: Optional[str] = None
    S3BucketSource: Optional[S3BucketSource] = None
    CloudWatchLogGroupArn: Optional[str] = None
    InputFormat: Optional[InputFormatType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class ListBackupsInputPaginate(BaseValidatorModel):
    TableName: Optional[str] = None
    TimeRangeLowerBound: Optional[Timestamp] = None
    TimeRangeUpperBound: Optional[Timestamp] = None
    BackupType: Optional[BackupTypeFilterType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTablesInputPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsOfResourceInputPaginate(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class UpdateContinuousBackupsInput(BaseValidatorModel):
    TableName: str
    PointInTimeRecoverySpecification: PointInTimeRecoverySpecification


class UpdateTimeToLiveInput(BaseValidatorModel):
    TableName: str
    TimeToLiveSpecification: TimeToLiveSpecification


class UpdateTimeToLiveOutput(BaseValidatorModel):
    TimeToLiveSpecification: TimeToLiveSpecification
    ResponseMetadata: ResponseMetadata


class UpdateKinesisStreamingDestinationInput(BaseValidatorModel):
    TableName: str
    StreamArn: str
    UpdateKinesisStreamingConfiguration: Optional[UpdateKinesisStreamingConfiguration] = None


class UpdateKinesisStreamingDestinationOutput(BaseValidatorModel):
    TableName: str
    StreamArn: str
    DestinationStatus: DestinationStatusType
    UpdateKinesisStreamingConfiguration: UpdateKinesisStreamingConfiguration
    ResponseMetadata: ResponseMetadata


class BatchStatementResponse(BaseValidatorModel):
    Error: Optional[BatchStatementError] = None
    TableName: Optional[str] = None
    Item: Optional[Dict[str, AttributeValue]] = None


class WriteRequestOutput(BaseValidatorModel):
    PutRequest: Optional[PutRequestOutput] = None
    DeleteRequest: Optional[DeleteRequestOutput] = None


class UniversalAttributeValue(BaseValidatorModel):
    pass


class AttributeValueUpdate(BaseValidatorModel):
    Value: Optional[UniversalAttributeValue] = None
    Action: Optional[AttributeActionType] = None


class BatchStatementRequest(BaseValidatorModel):
    Statement: str
    Parameters: Optional[Sequence[UniversalAttributeValue]] = None
    ConsistentRead: Optional[bool] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class ConditionCheck(BaseValidatorModel):
    Key: Mapping[str, UniversalAttributeValue]
    TableName: str
    ConditionExpression: str
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class Condition(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    AttributeValueList: Optional[Sequence[UniversalAttributeValue]] = None


class DeleteRequest(BaseValidatorModel):
    Key: Mapping[str, UniversalAttributeValue]


class Delete(BaseValidatorModel):
    Key: Mapping[str, UniversalAttributeValue]
    TableName: str
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class ExecuteStatementInput(BaseValidatorModel):
    Statement: str
    Parameters: Optional[Sequence[UniversalAttributeValue]] = None
    ConsistentRead: Optional[bool] = None
    NextToken: Optional[str] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    Limit: Optional[int] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class ExpectedAttributeValue(BaseValidatorModel):
    Value: Optional[UniversalAttributeValue] = None
    Exists: Optional[bool] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    AttributeValueList: Optional[Sequence[UniversalAttributeValue]] = None


class GetItemInput(BaseValidatorModel):
    TableName: str
    Key: Mapping[str, UniversalAttributeValue]
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None


class Get(BaseValidatorModel):
    Key: Mapping[str, UniversalAttributeValue]
    TableName: str
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None


class KeysAndAttributes(BaseValidatorModel):
    Keys: Sequence[Mapping[str, UniversalAttributeValue]]
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None


class ParameterizedStatement(BaseValidatorModel):
    Statement: str
    Parameters: Optional[Sequence[UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class PutRequest(BaseValidatorModel):
    Item: Mapping[str, UniversalAttributeValue]


class Put(BaseValidatorModel):
    Item: Mapping[str, UniversalAttributeValue]
    TableName: str
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class Update(BaseValidatorModel):
    Key: Mapping[str, UniversalAttributeValue]
    UpdateExpression: str
    TableName: str
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class ConditionBaseImport(BaseValidatorModel):
    pass


class QueryInputTableQuery(BaseValidatorModel):
    IndexName: Optional[str] = None
    Select: Optional[SelectType] = None
    AttributesToGet: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    ConsistentRead: Optional[bool] = None
    KeyConditions: Optional[Mapping[str, ConditionTable]] = None
    QueryFilter: Optional[Mapping[str, ConditionTable]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ScanIndexForward: Optional[bool] = None
    ExclusiveStartKey: Optional[Mapping[str, TableAttributeValue]] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[ConditionBaseImport] = None
    KeyConditionExpression: Optional[ConditionBaseImport] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, TableAttributeValue]] = None


class ScanInputTableScan(BaseValidatorModel):
    IndexName: Optional[str] = None
    AttributesToGet: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    Select: Optional[SelectType] = None
    ScanFilter: Optional[Mapping[str, ConditionTable]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ExclusiveStartKey: Optional[Mapping[str, TableAttributeValue]] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    TotalSegments: Optional[int] = None
    Segment: Optional[int] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[ConditionBaseImport] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, TableAttributeValue]] = None
    ConsistentRead: Optional[bool] = None


class DeleteItemInputTableDeleteItem(BaseValidatorModel):
    Key: Mapping[str, TableAttributeValue]
    Expected: Optional[Mapping[str, ExpectedAttributeValueTable]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ConditionExpression: Optional[ConditionBaseImport] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, TableAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class PutItemInputTablePutItem(BaseValidatorModel):
    Item: Mapping[str, TableAttributeValue]
    Expected: Optional[Mapping[str, ExpectedAttributeValueTable]] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ConditionExpression: Optional[ConditionBaseImport] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, TableAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class UpdateItemInputTableUpdateItem(BaseValidatorModel):
    Key: Mapping[str, TableAttributeValue]
    AttributeUpdates: Optional[Mapping[str, AttributeValueUpdateTable]] = None
    Expected: Optional[Mapping[str, ExpectedAttributeValueTable]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    UpdateExpression: Optional[str] = None
    ConditionExpression: Optional[ConditionBaseImport] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, TableAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class WriteRequestServiceResourceOutput(BaseValidatorModel):
    PutRequest: Optional[PutRequestServiceResourceOutput] = None
    DeleteRequest: Optional[DeleteRequestServiceResourceOutput] = None


class AutoScalingSettingsDescription(BaseValidatorModel):
    MinimumUnits: Optional[int] = None
    MaximumUnits: Optional[int] = None
    AutoScalingDisabled: Optional[bool] = None
    AutoScalingRoleArn: Optional[str] = None
    ScalingPolicies: Optional[List[AutoScalingPolicyDescription]] = None


class AutoScalingSettingsUpdate(BaseValidatorModel):
    MinimumUnits: Optional[int] = None
    MaximumUnits: Optional[int] = None
    AutoScalingDisabled: Optional[bool] = None
    AutoScalingRoleArn: Optional[str] = None
    ScalingPolicyUpdate: Optional[AutoScalingPolicyUpdate] = None


class BatchGetItemOutputServiceResource(BaseValidatorModel):
    Responses: Dict[str, List[Dict[str, TableAttributeValue]]]
    UnprocessedKeys: Dict[str, KeysAndAttributesServiceResourceOutput]
    ConsumedCapacity: List[ConsumedCapacity]
    ResponseMetadata: ResponseMetadata


class BatchGetItemOutput(BaseValidatorModel):
    Responses: Dict[str, List[Dict[str, AttributeValue]]]
    UnprocessedKeys: Dict[str, KeysAndAttributesOutput]
    ConsumedCapacity: List[ConsumedCapacity]
    ResponseMetadata: ResponseMetadata


class DeleteItemOutputTable(BaseValidatorModel):
    Attributes: Dict[str, TableAttributeValue]
    ConsumedCapacity: ConsumedCapacity
    ItemCollectionMetrics: ItemCollectionMetricsTable
    ResponseMetadata: ResponseMetadata


class DeleteItemOutput(BaseValidatorModel):
    Attributes: Dict[str, AttributeValue]
    ConsumedCapacity: ConsumedCapacity
    ItemCollectionMetrics: ItemCollectionMetrics
    ResponseMetadata: ResponseMetadata


class ExecuteStatementOutput(BaseValidatorModel):
    Items: List[Dict[str, AttributeValue]]
    ConsumedCapacity: ConsumedCapacity
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None
    LastEvaluatedKey: Optional[Dict[str, AttributeValue]] = None


class ExecuteTransactionOutput(BaseValidatorModel):
    Responses: List[ItemResponse]
    ConsumedCapacity: List[ConsumedCapacity]
    ResponseMetadata: ResponseMetadata


class GetItemOutputTable(BaseValidatorModel):
    ConsumedCapacity: ConsumedCapacity
    ResponseMetadata: ResponseMetadata
    Item: Optional[Dict[str, TableAttributeValue]] = None


class GetItemOutput(BaseValidatorModel):
    ConsumedCapacity: ConsumedCapacity
    ResponseMetadata: ResponseMetadata
    Item: Optional[Dict[str, AttributeValue]] = None


class PutItemOutputTable(BaseValidatorModel):
    Attributes: Dict[str, TableAttributeValue]
    ConsumedCapacity: ConsumedCapacity
    ItemCollectionMetrics: ItemCollectionMetricsTable
    ResponseMetadata: ResponseMetadata


class PutItemOutput(BaseValidatorModel):
    Attributes: Dict[str, AttributeValue]
    ConsumedCapacity: ConsumedCapacity
    ItemCollectionMetrics: ItemCollectionMetrics
    ResponseMetadata: ResponseMetadata


class QueryOutputTable(BaseValidatorModel):
    Items: List[Dict[str, TableAttributeValue]]
    Count: int
    ScannedCount: int
    ConsumedCapacity: ConsumedCapacity
    ResponseMetadata: ResponseMetadata
    LastEvaluatedKey: Optional[Dict[str, TableAttributeValue]] = None


class QueryOutput(BaseValidatorModel):
    Items: List[Dict[str, AttributeValue]]
    Count: int
    ScannedCount: int
    ConsumedCapacity: ConsumedCapacity
    ResponseMetadata: ResponseMetadata
    LastEvaluatedKey: Optional[Dict[str, AttributeValue]] = None


class ScanOutputTable(BaseValidatorModel):
    Items: List[Dict[str, TableAttributeValue]]
    Count: int
    ScannedCount: int
    ConsumedCapacity: ConsumedCapacity
    ResponseMetadata: ResponseMetadata
    LastEvaluatedKey: Optional[Dict[str, TableAttributeValue]] = None


class ScanOutput(BaseValidatorModel):
    Items: List[Dict[str, AttributeValue]]
    Count: int
    ScannedCount: int
    ConsumedCapacity: ConsumedCapacity
    ResponseMetadata: ResponseMetadata
    LastEvaluatedKey: Optional[Dict[str, AttributeValue]] = None


class TransactGetItemsOutput(BaseValidatorModel):
    ConsumedCapacity: List[ConsumedCapacity]
    Responses: List[ItemResponse]
    ResponseMetadata: ResponseMetadata


class TransactWriteItemsOutput(BaseValidatorModel):
    ConsumedCapacity: List[ConsumedCapacity]
    ItemCollectionMetrics: Dict[str, List[ItemCollectionMetrics]]
    ResponseMetadata: ResponseMetadata


class UpdateItemOutputTable(BaseValidatorModel):
    Attributes: Dict[str, TableAttributeValue]
    ConsumedCapacity: ConsumedCapacity
    ItemCollectionMetrics: ItemCollectionMetricsTable
    ResponseMetadata: ResponseMetadata


class UpdateItemOutput(BaseValidatorModel):
    Attributes: Dict[str, AttributeValue]
    ConsumedCapacity: ConsumedCapacity
    ItemCollectionMetrics: ItemCollectionMetrics
    ResponseMetadata: ResponseMetadata


class DescribeContinuousBackupsOutput(BaseValidatorModel):
    ContinuousBackupsDescription: ContinuousBackupsDescription
    ResponseMetadata: ResponseMetadata


class UpdateContinuousBackupsOutput(BaseValidatorModel):
    ContinuousBackupsDescription: ContinuousBackupsDescription
    ResponseMetadata: ResponseMetadata


class ListGlobalTablesOutput(BaseValidatorModel):
    GlobalTables: List[GlobalTable]
    LastEvaluatedGlobalTableName: str
    ResponseMetadata: ResponseMetadata


class UpdateGlobalTableInput(BaseValidatorModel):
    GlobalTableName: str
    ReplicaUpdates: Sequence[ReplicaUpdate]


class DescribeExportOutput(BaseValidatorModel):
    ExportDescription: ExportDescription
    ResponseMetadata: ResponseMetadata


class ExportTableToPointInTimeOutput(BaseValidatorModel):
    ExportDescription: ExportDescription
    ResponseMetadata: ResponseMetadata


class TableCreationParametersOutput(BaseValidatorModel):
    TableName: str
    AttributeDefinitions: List[AttributeDefinition]
    KeySchema: List[KeySchemaElement]
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    SSESpecification: Optional[SSESpecification] = None
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndexOutput]] = None


class SourceTableFeatureDetails(BaseValidatorModel):
    LocalSecondaryIndexes: Optional[List[LocalSecondaryIndexInfo]] = None
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndexInfo]] = None
    StreamDescription: Optional[StreamSpecification] = None
    TimeToLiveDescription: Optional[TimeToLiveDescription] = None
    SSEDescription: Optional[SSEDescription] = None


class ListImportsOutput(BaseValidatorModel):
    ImportSummaryList: List[ImportSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ProjectionUnion(BaseValidatorModel):
    pass


class CreateGlobalSecondaryIndexAction(BaseValidatorModel):
    IndexName: str
    KeySchema: Sequence[KeySchemaElement]
    Projection: ProjectionUnion
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    WarmThroughput: Optional[WarmThroughput] = None


class GlobalSecondaryIndex(BaseValidatorModel):
    IndexName: str
    KeySchema: Sequence[KeySchemaElement]
    Projection: ProjectionUnion
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    WarmThroughput: Optional[WarmThroughput] = None


class LocalSecondaryIndex(BaseValidatorModel):
    IndexName: str
    KeySchema: Sequence[KeySchemaElement]
    Projection: ProjectionUnion


class BatchExecuteStatementOutput(BaseValidatorModel):
    Responses: List[BatchStatementResponse]
    ConsumedCapacity: List[ConsumedCapacity]
    ResponseMetadata: ResponseMetadata


class BatchWriteItemOutput(BaseValidatorModel):
    UnprocessedItems: Dict[str, List[WriteRequestOutput]]
    ItemCollectionMetrics: Dict[str, List[ItemCollectionMetrics]]
    ConsumedCapacity: List[ConsumedCapacity]
    ResponseMetadata: ResponseMetadata


class BatchExecuteStatementInput(BaseValidatorModel):
    Statements: Sequence[BatchStatementRequest]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None


class QueryInputPaginate(BaseValidatorModel):
    TableName: str
    IndexName: Optional[str] = None
    Select: Optional[SelectType] = None
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    KeyConditions: Optional[Mapping[str, Condition]] = None
    QueryFilter: Optional[Mapping[str, Condition]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ScanIndexForward: Optional[bool] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[str] = None
    KeyConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValue]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class QueryInput(BaseValidatorModel):
    TableName: str
    IndexName: Optional[str] = None
    Select: Optional[SelectType] = None
    AttributesToGet: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    ConsistentRead: Optional[bool] = None
    KeyConditions: Optional[Mapping[str, Condition]] = None
    QueryFilter: Optional[Mapping[str, Condition]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ScanIndexForward: Optional[bool] = None
    ExclusiveStartKey: Optional[Mapping[str, UniversalAttributeValue]] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[str] = None
    KeyConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValue]] = None


class ScanInputPaginate(BaseValidatorModel):
    TableName: str
    IndexName: Optional[str] = None
    AttributesToGet: Optional[Sequence[str]] = None
    Select: Optional[SelectType] = None
    ScanFilter: Optional[Mapping[str, Condition]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    TotalSegments: Optional[int] = None
    Segment: Optional[int] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValue]] = None
    ConsistentRead: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ScanInput(BaseValidatorModel):
    TableName: str
    IndexName: Optional[str] = None
    AttributesToGet: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    Select: Optional[SelectType] = None
    ScanFilter: Optional[Mapping[str, Condition]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ExclusiveStartKey: Optional[Mapping[str, UniversalAttributeValue]] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    TotalSegments: Optional[int] = None
    Segment: Optional[int] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValue]] = None
    ConsistentRead: Optional[bool] = None


class DeleteItemInput(BaseValidatorModel):
    TableName: str
    Key: Mapping[str, UniversalAttributeValue]
    Expected: Optional[Mapping[str, ExpectedAttributeValue]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class PutItemInput(BaseValidatorModel):
    TableName: str
    Item: Mapping[str, UniversalAttributeValue]
    Expected: Optional[Mapping[str, ExpectedAttributeValue]] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class UpdateItemInput(BaseValidatorModel):
    TableName: str
    Key: Mapping[str, UniversalAttributeValue]
    AttributeUpdates: Optional[Mapping[str, AttributeValueUpdate]] = None
    Expected: Optional[Mapping[str, ExpectedAttributeValue]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    UpdateExpression: Optional[str] = None
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class TransactGetItem(BaseValidatorModel):
    Get: Get


class ExecuteTransactionInput(BaseValidatorModel):
    TransactStatements: Sequence[ParameterizedStatement]
    ClientRequestToken: Optional[str] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None


class TransactWriteItem(BaseValidatorModel):
    ConditionCheck: Optional[ConditionCheck] = None
    Put: Optional[Put] = None
    Delete: Optional[Delete] = None
    Update: Optional[Update] = None


class KeysAndAttributesServiceResourceUnion(BaseValidatorModel):
    pass


class BatchGetItemInputServiceResourceBatchGetItem(BaseValidatorModel):
    RequestItems: Mapping[str, KeysAndAttributesServiceResourceUnion]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None


class BatchWriteItemOutputServiceResource(BaseValidatorModel):
    UnprocessedItems: Dict[str, List[WriteRequestServiceResourceOutput]]
    ItemCollectionMetrics: Dict[str, List[ItemCollectionMetricsServiceResource]]
    ConsumedCapacity: List[ConsumedCapacity]
    ResponseMetadata: ResponseMetadata


class PutRequestServiceResourceUnion(BaseValidatorModel):
    pass


class DeleteRequestServiceResourceUnion(BaseValidatorModel):
    pass


class WriteRequestServiceResource(BaseValidatorModel):
    PutRequest: Optional[PutRequestServiceResourceUnion] = None
    DeleteRequest: Optional[DeleteRequestServiceResourceUnion] = None


class ReplicaGlobalSecondaryIndexAutoScalingDescription(BaseValidatorModel):
    IndexName: Optional[str] = None
    IndexStatus: Optional[IndexStatusType] = None
    ProvisionedReadCapacityAutoScalingSettings: Optional[AutoScalingSettingsDescription] = None
    ProvisionedWriteCapacityAutoScalingSettings: Optional[AutoScalingSettingsDescription] = None


class ReplicaGlobalSecondaryIndexSettingsDescription(BaseValidatorModel):
    IndexName: str
    IndexStatus: Optional[IndexStatusType] = None
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedReadCapacityAutoScalingSettings: Optional[AutoScalingSettingsDescription] = None
    ProvisionedWriteCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityAutoScalingSettings: Optional[AutoScalingSettingsDescription] = None


class GlobalSecondaryIndexAutoScalingUpdate(BaseValidatorModel):
    IndexName: Optional[str] = None
    ProvisionedWriteCapacityAutoScalingUpdate: Optional[AutoScalingSettingsUpdate] = None


class GlobalTableGlobalSecondaryIndexSettingsUpdate(BaseValidatorModel):
    IndexName: str
    ProvisionedWriteCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityAutoScalingSettingsUpdate: Optional[AutoScalingSettingsUpdate] = None


class ReplicaGlobalSecondaryIndexAutoScalingUpdate(BaseValidatorModel):
    IndexName: Optional[str] = None
    ProvisionedReadCapacityAutoScalingUpdate: Optional[AutoScalingSettingsUpdate] = None


class ReplicaGlobalSecondaryIndexSettingsUpdate(BaseValidatorModel):
    IndexName: str
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedReadCapacityAutoScalingSettingsUpdate: Optional[AutoScalingSettingsUpdate] = None


class DeleteReplicationGroupMemberAction(BaseValidatorModel):
    pass


class UpdateReplicationGroupMemberAction(BaseValidatorModel):
    pass


class CreateReplicationGroupMemberAction(BaseValidatorModel):
    pass


class ReplicationGroupUpdate(BaseValidatorModel):
    Create: Optional[CreateReplicationGroupMemberAction] = None
    Update: Optional[UpdateReplicationGroupMemberAction] = None
    Delete: Optional[DeleteReplicationGroupMemberAction] = None


class IncrementalExportSpecificationUnion(BaseValidatorModel):
    pass


class ExportTableToPointInTimeInput(BaseValidatorModel):
    TableArn: str
    S3Bucket: str
    ExportTime: Optional[Timestamp] = None
    ClientToken: Optional[str] = None
    S3BucketOwner: Optional[str] = None
    S3Prefix: Optional[str] = None
    S3SseAlgorithm: Optional[S3SseAlgorithmType] = None
    S3SseKmsKeyId: Optional[str] = None
    ExportFormat: Optional[ExportFormatType] = None
    ExportType: Optional[ExportTypeType] = None
    IncrementalExportSpecification: Optional[IncrementalExportSpecificationUnion] = None


class ReplicaDescription(BaseValidatorModel):
    pass


class GlobalTableDescription(BaseValidatorModel):
    ReplicationGroup: Optional[List[ReplicaDescription]] = None
    GlobalTableArn: Optional[str] = None
    CreationDateTime: Optional[datetime] = None
    GlobalTableStatus: Optional[GlobalTableStatusType] = None
    GlobalTableName: Optional[str] = None


class TableDescription(BaseValidatorModel):
    AttributeDefinitions: Optional[List[AttributeDefinition]] = None
    TableName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElement]] = None
    TableStatus: Optional[TableStatusType] = None
    CreationDateTime: Optional[datetime] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputDescription] = None
    TableSizeBytes: Optional[int] = None
    ItemCount: Optional[int] = None
    TableArn: Optional[str] = None
    TableId: Optional[str] = None
    BillingModeSummary: Optional[BillingModeSummary] = None
    LocalSecondaryIndexes: Optional[List[LocalSecondaryIndexDescription]] = None
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndexDescription]] = None
    StreamSpecification: Optional[StreamSpecification] = None
    LatestStreamLabel: Optional[str] = None
    LatestStreamArn: Optional[str] = None
    GlobalTableVersion: Optional[str] = None
    Replicas: Optional[List[ReplicaDescription]] = None
    RestoreSummary: Optional[RestoreSummary] = None
    SSEDescription: Optional[SSEDescription] = None
    ArchivalSummary: Optional[ArchivalSummary] = None
    TableClassSummary: Optional[TableClassSummary] = None
    DeletionProtectionEnabled: Optional[bool] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    WarmThroughput: Optional[TableWarmThroughputDescription] = None
    MultiRegionConsistency: Optional[MultiRegionConsistencyType] = None


class ImportTableDescription(BaseValidatorModel):
    ImportArn: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    TableArn: Optional[str] = None
    TableId: Optional[str] = None
    ClientToken: Optional[str] = None
    S3BucketSource: Optional[S3BucketSource] = None
    ErrorCount: Optional[int] = None
    CloudWatchLogGroupArn: Optional[str] = None
    InputFormat: Optional[InputFormatType] = None
    InputFormatOptions: Optional[InputFormatOptionsOutput] = None
    InputCompressionType: Optional[InputCompressionTypeType] = None
    TableCreationParameters: Optional[TableCreationParametersOutput] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ProcessedSizeBytes: Optional[int] = None
    ProcessedItemCount: Optional[int] = None
    ImportedItemCount: Optional[int] = None
    FailureCode: Optional[str] = None
    FailureMessage: Optional[str] = None


class BackupDescription(BaseValidatorModel):
    BackupDetails: Optional[BackupDetails] = None
    SourceTableDetails: Optional[SourceTableDetails] = None
    SourceTableFeatureDetails: Optional[SourceTableFeatureDetails] = None


class GlobalSecondaryIndexUpdate(BaseValidatorModel):
    Update: Optional[UpdateGlobalSecondaryIndexAction] = None
    Create: Optional[CreateGlobalSecondaryIndexAction] = None
    Delete: Optional[DeleteGlobalSecondaryIndexAction] = None


class TableCreationParameters(BaseValidatorModel):
    TableName: str
    AttributeDefinitions: Sequence[AttributeDefinition]
    KeySchema: Sequence[KeySchemaElement]
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    SSESpecification: Optional[SSESpecification] = None
    GlobalSecondaryIndexes: Optional[Sequence[GlobalSecondaryIndex]] = None


class TransactGetItemsInput(BaseValidatorModel):
    TransactItems: Sequence[TransactGetItem]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None


class KeysAndAttributesUnion(BaseValidatorModel):
    pass


class BatchGetItemInput(BaseValidatorModel):
    RequestItems: Mapping[str, KeysAndAttributesUnion]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None


class PutRequestUnion(BaseValidatorModel):
    pass


class DeleteRequestUnion(BaseValidatorModel):
    pass


class WriteRequest(BaseValidatorModel):
    PutRequest: Optional[PutRequestUnion] = None
    DeleteRequest: Optional[DeleteRequestUnion] = None


class TransactWriteItemsInput(BaseValidatorModel):
    TransactItems: Sequence[TransactWriteItem]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ClientRequestToken: Optional[str] = None


class CreateGlobalTableOutput(BaseValidatorModel):
    GlobalTableDescription: GlobalTableDescription
    ResponseMetadata: ResponseMetadata


class DescribeGlobalTableOutput(BaseValidatorModel):
    GlobalTableDescription: GlobalTableDescription
    ResponseMetadata: ResponseMetadata


class UpdateGlobalTableOutput(BaseValidatorModel):
    GlobalTableDescription: GlobalTableDescription
    ResponseMetadata: ResponseMetadata


class CreateTableOutput(BaseValidatorModel):
    TableDescription: TableDescription
    ResponseMetadata: ResponseMetadata


class DeleteTableOutput(BaseValidatorModel):
    TableDescription: TableDescription
    ResponseMetadata: ResponseMetadata


class DescribeTableOutput(BaseValidatorModel):
    Table: TableDescription
    ResponseMetadata: ResponseMetadata


class RestoreTableFromBackupOutput(BaseValidatorModel):
    TableDescription: TableDescription
    ResponseMetadata: ResponseMetadata


class RestoreTableToPointInTimeOutput(BaseValidatorModel):
    TableDescription: TableDescription
    ResponseMetadata: ResponseMetadata


class UpdateTableOutput(BaseValidatorModel):
    TableDescription: TableDescription
    ResponseMetadata: ResponseMetadata


class DescribeImportOutput(BaseValidatorModel):
    ImportTableDescription: ImportTableDescription
    ResponseMetadata: ResponseMetadata


class ImportTableOutput(BaseValidatorModel):
    ImportTableDescription: ImportTableDescription
    ResponseMetadata: ResponseMetadata


class DeleteBackupOutput(BaseValidatorModel):
    BackupDescription: BackupDescription
    ResponseMetadata: ResponseMetadata


class DescribeBackupOutput(BaseValidatorModel):
    BackupDescription: BackupDescription
    ResponseMetadata: ResponseMetadata


class UpdateTableInputTableUpdate(BaseValidatorModel):
    AttributeDefinitions: Optional[Sequence[AttributeDefinition]] = None
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    GlobalSecondaryIndexUpdates: Optional[Sequence[GlobalSecondaryIndexUpdate]] = None
    StreamSpecification: Optional[StreamSpecification] = None
    SSESpecification: Optional[SSESpecification] = None
    ReplicaUpdates: Optional[Sequence[ReplicationGroupUpdate]] = None
    TableClass: Optional[TableClassType] = None
    DeletionProtectionEnabled: Optional[bool] = None
    MultiRegionConsistency: Optional[MultiRegionConsistencyType] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    WarmThroughput: Optional[WarmThroughput] = None


class UpdateTableInput(BaseValidatorModel):
    TableName: str
    AttributeDefinitions: Optional[Sequence[AttributeDefinition]] = None
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    GlobalSecondaryIndexUpdates: Optional[Sequence[GlobalSecondaryIndexUpdate]] = None
    StreamSpecification: Optional[StreamSpecification] = None
    SSESpecification: Optional[SSESpecification] = None
    ReplicaUpdates: Optional[Sequence[ReplicationGroupUpdate]] = None
    TableClass: Optional[TableClassType] = None
    DeletionProtectionEnabled: Optional[bool] = None
    MultiRegionConsistency: Optional[MultiRegionConsistencyType] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    WarmThroughput: Optional[WarmThroughput] = None


class GlobalSecondaryIndexUnion(BaseValidatorModel):
    pass


class CreateTableInputServiceResourceCreateTable(BaseValidatorModel):
    AttributeDefinitions: Sequence[AttributeDefinition]
    TableName: str
    KeySchema: Sequence[KeySchemaElement]
    LocalSecondaryIndexes: Optional[Sequence[LocalSecondaryIndex]] = None
    GlobalSecondaryIndexes: Optional[Sequence[GlobalSecondaryIndexUnion]] = None
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    StreamSpecification: Optional[StreamSpecification] = None
    SSESpecification: Optional[SSESpecification] = None
    Tags: Optional[Sequence[Tag]] = None
    TableClass: Optional[TableClassType] = None
    DeletionProtectionEnabled: Optional[bool] = None
    WarmThroughput: Optional[WarmThroughput] = None
    ResourcePolicy: Optional[str] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None


class CreateTableInput(BaseValidatorModel):
    AttributeDefinitions: Sequence[AttributeDefinition]
    TableName: str
    KeySchema: Sequence[KeySchemaElement]
    LocalSecondaryIndexes: Optional[Sequence[LocalSecondaryIndex]] = None
    GlobalSecondaryIndexes: Optional[Sequence[GlobalSecondaryIndexUnion]] = None
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    StreamSpecification: Optional[StreamSpecification] = None
    SSESpecification: Optional[SSESpecification] = None
    Tags: Optional[Sequence[Tag]] = None
    TableClass: Optional[TableClassType] = None
    DeletionProtectionEnabled: Optional[bool] = None
    WarmThroughput: Optional[WarmThroughput] = None
    ResourcePolicy: Optional[str] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None


class RestoreTableFromBackupInput(BaseValidatorModel):
    TargetTableName: str
    BackupArn: str
    BillingModeOverride: Optional[BillingModeType] = None
    GlobalSecondaryIndexOverride: Optional[Sequence[GlobalSecondaryIndexUnion]] = None
    LocalSecondaryIndexOverride: Optional[Sequence[LocalSecondaryIndex]] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughput] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughput] = None
    SSESpecificationOverride: Optional[SSESpecification] = None


class RestoreTableToPointInTimeInput(BaseValidatorModel):
    TargetTableName: str
    SourceTableArn: Optional[str] = None
    SourceTableName: Optional[str] = None
    UseLatestRestorableTime: Optional[bool] = None
    RestoreDateTime: Optional[Timestamp] = None
    BillingModeOverride: Optional[BillingModeType] = None
    GlobalSecondaryIndexOverride: Optional[Sequence[GlobalSecondaryIndexUnion]] = None
    LocalSecondaryIndexOverride: Optional[Sequence[LocalSecondaryIndex]] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughput] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughput] = None
    SSESpecificationOverride: Optional[SSESpecification] = None


class WriteRequestServiceResourceUnion(BaseValidatorModel):
    pass


class BatchWriteItemInputServiceResourceBatchWriteItem(BaseValidatorModel):
    RequestItems: Mapping[str, Sequence[WriteRequestServiceResourceUnion]]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None


class ReplicaAutoScalingDescription(BaseValidatorModel):
    pass


class TableAutoScalingDescription(BaseValidatorModel):
    TableName: Optional[str] = None
    TableStatus: Optional[TableStatusType] = None
    Replicas: Optional[List[ReplicaAutoScalingDescription]] = None


class ReplicaSettingsDescription(BaseValidatorModel):
    pass


class DescribeGlobalTableSettingsOutput(BaseValidatorModel):
    GlobalTableName: str
    ReplicaSettings: List[ReplicaSettingsDescription]
    ResponseMetadata: ResponseMetadata


class UpdateGlobalTableSettingsOutput(BaseValidatorModel):
    GlobalTableName: str
    ReplicaSettings: List[ReplicaSettingsDescription]
    ResponseMetadata: ResponseMetadata


class ReplicaAutoScalingUpdate(BaseValidatorModel):
    pass


class UpdateTableReplicaAutoScalingInput(BaseValidatorModel):
    TableName: str
    GlobalSecondaryIndexUpdates: Optional[Sequence[GlobalSecondaryIndexAutoScalingUpdate]] = None
    ProvisionedWriteCapacityAutoScalingUpdate: Optional[AutoScalingSettingsUpdate] = None
    ReplicaUpdates: Optional[Sequence[ReplicaAutoScalingUpdate]] = None


class ReplicaSettingsUpdate(BaseValidatorModel):
    pass


class UpdateGlobalTableSettingsInput(BaseValidatorModel):
    GlobalTableName: str
    GlobalTableBillingMode: Optional[BillingModeType] = None
    GlobalTableProvisionedWriteCapacityUnits: Optional[int] = None
    GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: Optional[ AutoScalingSettingsUpdate ] = None
    GlobalTableGlobalSecondaryIndexSettingsUpdate: Optional[ Sequence[GlobalTableGlobalSecondaryIndexSettingsUpdate] ] = None
    ReplicaSettingsUpdate: Optional[Sequence[ReplicaSettingsUpdate]] = None


class TableCreationParametersUnion(BaseValidatorModel):
    pass


class InputFormatOptionsUnion(BaseValidatorModel):
    pass


class ImportTableInput(BaseValidatorModel):
    S3BucketSource: S3BucketSource
    InputFormat: InputFormatType
    TableCreationParameters: TableCreationParametersUnion
    ClientToken: Optional[str] = None
    InputFormatOptions: Optional[InputFormatOptionsUnion] = None
    InputCompressionType: Optional[InputCompressionTypeType] = None


class WriteRequestUnion(BaseValidatorModel):
    pass


class BatchWriteItemInput(BaseValidatorModel):
    RequestItems: Mapping[str, Sequence[WriteRequestUnion]]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None


class DescribeTableReplicaAutoScalingOutput(BaseValidatorModel):
    TableAutoScalingDescription: TableAutoScalingDescription
    ResponseMetadata: ResponseMetadata


class UpdateTableReplicaAutoScalingOutput(BaseValidatorModel):
    TableAutoScalingDescription: TableAutoScalingDescription
    ResponseMetadata: ResponseMetadata


