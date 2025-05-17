from decimal import Decimal
from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union, Set
from datetime import datetime

from boto3.dynamodb.conditions import ConditionBase
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.dynamodb.dynamodb_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




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
    SS: Optional[List[str]] = None
    NS: Optional[List[str]] = None
    BS: Optional[List[bytes]] = None
    M: Optional[Dict[str, Any]] = None
    L: Optional[List[Any]] = None
    NULL: Optional[bool] = None
    BOOL: Optional[bool] = None

TableAttributeValue = Union[bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]


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

ConditionBaseImport = Union[str, ConditionBase]


class PointInTimeRecoveryDescription(BaseValidatorModel):
    PointInTimeRecoveryStatus: Optional[PointInTimeRecoveryStatusType] = None
    RecoveryPeriodInDays: Optional[int] = None
    EarliestRestorableDateTime: Optional[datetime] = None
    LatestRestorableDateTime: Optional[datetime] = None


class ContributorInsightsSummary(BaseValidatorModel):
    TableName: Optional[str] = None
    IndexName: Optional[str] = None
    ContributorInsightsStatus: Optional[ContributorInsightsStatusType] = None


# This class is the input for the 'create_backup' function.
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


class Replica(BaseValidatorModel):
    RegionName: Optional[str] = None


class CreateReplicaAction(BaseValidatorModel):
    RegionName: str


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
    HeaderList: Optional[List[str]] = None


# This class is the input for the 'delete_backup' function.
class DeleteBackupInput(BaseValidatorModel):
    BackupArn: str


class DeleteGlobalSecondaryIndexAction(BaseValidatorModel):
    IndexName: str


class DeleteReplicaAction(BaseValidatorModel):
    RegionName: str


class DeleteReplicationGroupMemberAction(BaseValidatorModel):
    RegionName: str


# This class is the input for the 'delete_resource_policy' function.
class DeleteResourcePolicyInput(BaseValidatorModel):
    ResourceArn: str
    ExpectedRevisionId: Optional[str] = None


# This class is the input for the 'delete_table' function.
class DeleteTableInput(BaseValidatorModel):
    TableName: str


# This class is the input for the 'describe_backup' function.
class DescribeBackupInput(BaseValidatorModel):
    BackupArn: str


# This class is the input for the 'describe_continuous_backups' function.
class DescribeContinuousBackupsInput(BaseValidatorModel):
    TableName: str


# This class is the input for the 'describe_contributor_insights' function.
class DescribeContributorInsightsInput(BaseValidatorModel):
    TableName: str
    IndexName: Optional[str] = None


class FailureException(BaseValidatorModel):
    ExceptionName: Optional[str] = None
    ExceptionDescription: Optional[str] = None


class Endpoint(BaseValidatorModel):
    Address: str
    CachePeriodInMinutes: int


# This class is the input for the 'describe_export' function.
class DescribeExportInput(BaseValidatorModel):
    ExportArn: str


# This class is the input for the 'describe_global_table' function.
class DescribeGlobalTableInput(BaseValidatorModel):
    GlobalTableName: str


# This class is the input for the 'describe_global_table_settings' function.
class DescribeGlobalTableSettingsInput(BaseValidatorModel):
    GlobalTableName: str


# This class is the input for the 'describe_import' function.
class DescribeImportInput(BaseValidatorModel):
    ImportArn: str


# This class is the input for the 'describe_kinesis_streaming_destination' function.
class DescribeKinesisStreamingDestinationInput(BaseValidatorModel):
    TableName: str


class KinesisDataStreamDestination(BaseValidatorModel):
    StreamArn: Optional[str] = None
    DestinationStatus: Optional[DestinationStatusType] = None
    DestinationStatusDescription: Optional[str] = None
    ApproximateCreationDateTimePrecision: Optional[ApproximateCreationDateTimePrecisionType] = None


# This class is the input for the 'describe_table' function.
class DescribeTableInput(BaseValidatorModel):
    TableName: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_table_replica_auto_scaling' function.
class DescribeTableReplicaAutoScalingInput(BaseValidatorModel):
    TableName: str


# This class is the input for the 'describe_time_to_live' function.
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

Timestamp = Union[datetime, str]


# This class is the input for the 'get_resource_policy' function.
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


# This class is the input for the 'list_contributor_insights' function.
class ListContributorInsightsInput(BaseValidatorModel):
    TableName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_exports' function.
class ListExportsInput(BaseValidatorModel):
    TableArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_global_tables' function.
class ListGlobalTablesInput(BaseValidatorModel):
    ExclusiveStartGlobalTableName: Optional[str] = None
    Limit: Optional[int] = None
    RegionName: Optional[str] = None


# This class is the input for the 'list_imports' function.
class ListImportsInput(BaseValidatorModel):
    TableArn: Optional[str] = None
    PageSize: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_tables' function.
class ListTablesInput(BaseValidatorModel):
    ExclusiveStartTableName: Optional[str] = None
    Limit: Optional[int] = None


# This class is the input for the 'list_tags_of_resource' function.
class ListTagsOfResourceInput(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None


class PointInTimeRecoverySpecification(BaseValidatorModel):
    PointInTimeRecoveryEnabled: bool
    RecoveryPeriodInDays: Optional[int] = None


class Projection(BaseValidatorModel):
    ProjectionType: Optional[ProjectionTypeType] = None
    NonKeyAttributes: Optional[List[str]] = None


# This class is the input for the 'put_resource_policy' function.
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


# This class is the input for the 'untag_resource' function.
class UntagResourceInput(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_contributor_insights' function.
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

UniversalAttributeValue = Union[AttributeValue, bytes, bytearray, str, int, Decimal, bool, Set[int], Set[Decimal], Set[str], Set[bytes], Set[bytearray], List[Any], Dict[str, Any], None]


class AttributeValueUpdateTable(BaseValidatorModel):
    Value: Optional[TableAttributeValue] = None
    Action: Optional[AttributeActionType] = None


class ConditionTable(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    AttributeValueList: Optional[List[TableAttributeValue]] = None


class DeleteRequestServiceResourceOutput(BaseValidatorModel):
    Key: Dict[str, TableAttributeValue]


class DeleteRequestServiceResource(BaseValidatorModel):
    Key: Dict[str, TableAttributeValue]


class ExpectedAttributeValueTable(BaseValidatorModel):
    Value: Optional[TableAttributeValue] = None
    Exists: Optional[bool] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    AttributeValueList: Optional[List[TableAttributeValue]] = None


class GetItemInputTableGetItem(BaseValidatorModel):
    Key: Dict[str, TableAttributeValue]
    AttributesToGet: Optional[List[str]] = None
    ConsistentRead: Optional[bool] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None


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
    Keys: List[Dict[str, TableAttributeValue]]
    AttributesToGet: Optional[List[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None


class PutRequestServiceResourceOutput(BaseValidatorModel):
    Item: Dict[str, TableAttributeValue]


class PutRequestServiceResource(BaseValidatorModel):
    Item: Dict[str, TableAttributeValue]


class AutoScalingPolicyDescription(BaseValidatorModel):
    PolicyName: Optional[str] = None
    TargetTrackingScalingPolicyConfiguration: Optional[AutoScalingTargetTrackingScalingPolicyConfigurationDescription] = None


class AutoScalingPolicyUpdate(BaseValidatorModel):
    TargetTrackingScalingPolicyConfiguration: AutoScalingTargetTrackingScalingPolicyConfigurationUpdate
    PolicyName: Optional[str] = None


# This class is the output for the 'create_backup' function.
class CreateBackupOutput(BaseValidatorModel):
    BackupDetails: BackupDetails
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_resource_policy' function.
class DeleteResourcePolicyOutput(BaseValidatorModel):
    RevisionId: str
    ResponseMetadata: ResponseMetadata


class DescribeLimitsOutput(BaseValidatorModel):
    AccountMaxReadCapacityUnits: int
    AccountMaxWriteCapacityUnits: int
    TableMaxReadCapacityUnits: int
    TableMaxWriteCapacityUnits: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_resource_policy' function.
class GetResourcePolicyOutput(BaseValidatorModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_backups' function.
class ListBackupsOutput(BaseValidatorModel):
    BackupSummaries: List[BackupSummary]
    LastEvaluatedBackupArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tables' function.
class ListTablesOutput(BaseValidatorModel):
    TableNames: List[str]
    LastEvaluatedTableName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_resource_policy' function.
class PutResourcePolicyOutput(BaseValidatorModel):
    RevisionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_contributor_insights' function.
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


# This class is the output for the 'list_contributor_insights' function.
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


# This class is the input for the 'create_global_table' function.
class CreateGlobalTableInput(BaseValidatorModel):
    GlobalTableName: str
    ReplicationGroup: List[Replica]


class GlobalTable(BaseValidatorModel):
    GlobalTableName: Optional[str] = None
    ReplicationGroup: Optional[List[Replica]] = None


class ReplicaGlobalSecondaryIndex(BaseValidatorModel):
    IndexName: str
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverride] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverride] = None


# This class is the output for the 'list_tags_of_resource' function.
class ListTagsOfResourceOutput(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'tag_resource' function.
class TagResourceInput(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


class InputFormatOptionsOutput(BaseValidatorModel):
    Csv: Optional[CsvOptionsOutput] = None


class InputFormatOptions(BaseValidatorModel):
    Csv: Optional[CsvOptions] = None


class ReplicaUpdate(BaseValidatorModel):
    Create: Optional[CreateReplicaAction] = None
    Delete: Optional[DeleteReplicaAction] = None


# This class is the output for the 'describe_contributor_insights' function.
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


# This class is the output for the 'describe_kinesis_streaming_destination' function.
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


# This class is the output for the 'describe_time_to_live' function.
class DescribeTimeToLiveOutput(BaseValidatorModel):
    TimeToLiveDescription: TimeToLiveDescription
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'enable_kinesis_streaming_destination' function.
class KinesisStreamingDestinationInputRequest(BaseValidatorModel):
    TableName: str
    StreamArn: str
    EnableKinesisStreamingConfiguration: Optional[EnableKinesisStreamingConfiguration] = None


# This class is the input for the 'disable_kinesis_streaming_destination' function.
class KinesisStreamingDestinationInput(BaseValidatorModel):
    TableName: str
    StreamArn: str
    EnableKinesisStreamingConfiguration: Optional[EnableKinesisStreamingConfiguration] = None


# This class is the output for the 'enable_kinesis_streaming_destination' function.
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


# This class is the output for the 'list_exports' function.
class ListExportsOutput(BaseValidatorModel):
    ExportSummaries: List[ExportSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IncrementalExportSpecification(BaseValidatorModel):
    ExportFromTime: Optional[Timestamp] = None
    ExportToTime: Optional[Timestamp] = None
    ExportViewType: Optional[ExportViewTypeType] = None


# This class is the input for the 'list_backups' function.
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


# This class is the input for the 'update_continuous_backups' function.
class UpdateContinuousBackupsInput(BaseValidatorModel):
    TableName: str
    PointInTimeRecoverySpecification: PointInTimeRecoverySpecification

ProjectionUnion = Union[Projection, ProjectionOutput]


# This class is the input for the 'update_time_to_live' function.
class UpdateTimeToLiveInput(BaseValidatorModel):
    TableName: str
    TimeToLiveSpecification: TimeToLiveSpecification


# This class is the output for the 'update_time_to_live' function.
class UpdateTimeToLiveOutput(BaseValidatorModel):
    TimeToLiveSpecification: TimeToLiveSpecification
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_kinesis_streaming_destination' function.
class UpdateKinesisStreamingDestinationInput(BaseValidatorModel):
    TableName: str
    StreamArn: str
    UpdateKinesisStreamingConfiguration: Optional[UpdateKinesisStreamingConfiguration] = None


# This class is the output for the 'update_kinesis_streaming_destination' function.
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


class AttributeValueUpdate(BaseValidatorModel):
    Value: Optional[UniversalAttributeValue] = None
    Action: Optional[AttributeActionType] = None


class BatchStatementRequest(BaseValidatorModel):
    Statement: str
    Parameters: Optional[List[UniversalAttributeValue]] = None
    ConsistentRead: Optional[bool] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class ConditionCheck(BaseValidatorModel):
    Key: Dict[str, UniversalAttributeValue]
    TableName: str
    ConditionExpression: str
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class Condition(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    AttributeValueList: Optional[List[UniversalAttributeValue]] = None


class DeleteRequest(BaseValidatorModel):
    Key: Dict[str, UniversalAttributeValue]


class Delete(BaseValidatorModel):
    Key: Dict[str, UniversalAttributeValue]
    TableName: str
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


# This class is the input for the 'execute_statement' function.
class ExecuteStatementInput(BaseValidatorModel):
    Statement: str
    Parameters: Optional[List[UniversalAttributeValue]] = None
    ConsistentRead: Optional[bool] = None
    NextToken: Optional[str] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    Limit: Optional[int] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class ExpectedAttributeValue(BaseValidatorModel):
    Value: Optional[UniversalAttributeValue] = None
    Exists: Optional[bool] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    AttributeValueList: Optional[List[UniversalAttributeValue]] = None


# This class is the input for the 'get_item' function.
class GetItemInput(BaseValidatorModel):
    TableName: str
    Key: Dict[str, UniversalAttributeValue]
    AttributesToGet: Optional[List[str]] = None
    ConsistentRead: Optional[bool] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None


class Get(BaseValidatorModel):
    Key: Dict[str, UniversalAttributeValue]
    TableName: str
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None


class KeysAndAttributes(BaseValidatorModel):
    Keys: List[Dict[str, UniversalAttributeValue]]
    AttributesToGet: Optional[List[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None


class ParameterizedStatement(BaseValidatorModel):
    Statement: str
    Parameters: Optional[List[UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class PutRequest(BaseValidatorModel):
    Item: Dict[str, UniversalAttributeValue]


class Put(BaseValidatorModel):
    Item: Dict[str, UniversalAttributeValue]
    TableName: str
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class Update(BaseValidatorModel):
    Key: Dict[str, UniversalAttributeValue]
    UpdateExpression: str
    TableName: str
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class QueryInputTableQuery(BaseValidatorModel):
    IndexName: Optional[str] = None
    Select: Optional[SelectType] = None
    AttributesToGet: Optional[List[str]] = None
    Limit: Optional[int] = None
    ConsistentRead: Optional[bool] = None
    KeyConditions: Optional[Dict[str, ConditionTable]] = None
    QueryFilter: Optional[Dict[str, ConditionTable]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ScanIndexForward: Optional[bool] = None
    ExclusiveStartKey: Optional[Dict[str, TableAttributeValue]] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[ConditionBaseImport] = None
    KeyConditionExpression: Optional[ConditionBaseImport] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, TableAttributeValue]] = None


class ScanInputTableScan(BaseValidatorModel):
    IndexName: Optional[str] = None
    AttributesToGet: Optional[List[str]] = None
    Limit: Optional[int] = None
    Select: Optional[SelectType] = None
    ScanFilter: Optional[Dict[str, ConditionTable]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ExclusiveStartKey: Optional[Dict[str, TableAttributeValue]] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    TotalSegments: Optional[int] = None
    Segment: Optional[int] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[ConditionBaseImport] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, TableAttributeValue]] = None
    ConsistentRead: Optional[bool] = None

DeleteRequestServiceResourceUnion = Union[DeleteRequestServiceResource, DeleteRequestServiceResourceOutput]


class DeleteItemInputTableDeleteItem(BaseValidatorModel):
    Key: Dict[str, TableAttributeValue]
    Expected: Optional[Dict[str, ExpectedAttributeValueTable]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ConditionExpression: Optional[ConditionBaseImport] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, TableAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class PutItemInputTablePutItem(BaseValidatorModel):
    Item: Dict[str, TableAttributeValue]
    Expected: Optional[Dict[str, ExpectedAttributeValueTable]] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ConditionExpression: Optional[ConditionBaseImport] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, TableAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class UpdateItemInputTableUpdateItem(BaseValidatorModel):
    Key: Dict[str, TableAttributeValue]
    AttributeUpdates: Optional[Dict[str, AttributeValueUpdateTable]] = None
    Expected: Optional[Dict[str, ExpectedAttributeValueTable]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    UpdateExpression: Optional[str] = None
    ConditionExpression: Optional[ConditionBaseImport] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, TableAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

KeysAndAttributesServiceResourceUnion = Union[KeysAndAttributesServiceResource, KeysAndAttributesServiceResourceOutput]


class WriteRequestServiceResourceOutput(BaseValidatorModel):
    PutRequest: Optional[PutRequestServiceResourceOutput] = None
    DeleteRequest: Optional[DeleteRequestServiceResourceOutput] = None

PutRequestServiceResourceUnion = Union[PutRequestServiceResource, PutRequestServiceResourceOutput]


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


# This class is the output for the 'batch_get_item' function.
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


# This class is the output for the 'delete_item' function.
class DeleteItemOutput(BaseValidatorModel):
    Attributes: Dict[str, AttributeValue]
    ConsumedCapacity: ConsumedCapacity
    ItemCollectionMetrics: ItemCollectionMetrics
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'execute_statement' function.
class ExecuteStatementOutput(BaseValidatorModel):
    Items: List[Dict[str, AttributeValue]]
    ConsumedCapacity: ConsumedCapacity
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None
    LastEvaluatedKey: Optional[Dict[str, AttributeValue]] = None


# This class is the output for the 'execute_transaction' function.
class ExecuteTransactionOutput(BaseValidatorModel):
    Responses: List[ItemResponse]
    ConsumedCapacity: List[ConsumedCapacity]
    ResponseMetadata: ResponseMetadata


class GetItemOutputTable(BaseValidatorModel):
    ConsumedCapacity: ConsumedCapacity
    ResponseMetadata: ResponseMetadata
    Item: Optional[Dict[str, TableAttributeValue]] = None


# This class is the output for the 'get_item' function.
class GetItemOutput(BaseValidatorModel):
    ConsumedCapacity: ConsumedCapacity
    ResponseMetadata: ResponseMetadata
    Item: Optional[Dict[str, AttributeValue]] = None


class PutItemOutputTable(BaseValidatorModel):
    Attributes: Dict[str, TableAttributeValue]
    ConsumedCapacity: ConsumedCapacity
    ItemCollectionMetrics: ItemCollectionMetricsTable
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_item' function.
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


# This class is the output for the 'query' function.
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


# This class is the output for the 'scan' function.
class ScanOutput(BaseValidatorModel):
    Items: List[Dict[str, AttributeValue]]
    Count: int
    ScannedCount: int
    ConsumedCapacity: ConsumedCapacity
    ResponseMetadata: ResponseMetadata
    LastEvaluatedKey: Optional[Dict[str, AttributeValue]] = None


# This class is the output for the 'transact_get_items' function.
class TransactGetItemsOutput(BaseValidatorModel):
    ConsumedCapacity: List[ConsumedCapacity]
    Responses: List[ItemResponse]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'transact_write_items' function.
class TransactWriteItemsOutput(BaseValidatorModel):
    ConsumedCapacity: List[ConsumedCapacity]
    ItemCollectionMetrics: Dict[str, List[ItemCollectionMetrics]]
    ResponseMetadata: ResponseMetadata


class UpdateItemOutputTable(BaseValidatorModel):
    Attributes: Dict[str, TableAttributeValue]
    ConsumedCapacity: ConsumedCapacity
    ItemCollectionMetrics: ItemCollectionMetricsTable
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_item' function.
class UpdateItemOutput(BaseValidatorModel):
    Attributes: Dict[str, AttributeValue]
    ConsumedCapacity: ConsumedCapacity
    ItemCollectionMetrics: ItemCollectionMetrics
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_continuous_backups' function.
class DescribeContinuousBackupsOutput(BaseValidatorModel):
    ContinuousBackupsDescription: ContinuousBackupsDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_continuous_backups' function.
class UpdateContinuousBackupsOutput(BaseValidatorModel):
    ContinuousBackupsDescription: ContinuousBackupsDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_global_tables' function.
class ListGlobalTablesOutput(BaseValidatorModel):
    GlobalTables: List[GlobalTable]
    LastEvaluatedGlobalTableName: str
    ResponseMetadata: ResponseMetadata


class CreateReplicationGroupMemberAction(BaseValidatorModel):
    RegionName: str
    KMSMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverride] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverride] = None
    GlobalSecondaryIndexes: Optional[List[ReplicaGlobalSecondaryIndex]] = None
    TableClassOverride: Optional[TableClassType] = None


class UpdateReplicationGroupMemberAction(BaseValidatorModel):
    RegionName: str
    KMSMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverride] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverride] = None
    GlobalSecondaryIndexes: Optional[List[ReplicaGlobalSecondaryIndex]] = None
    TableClassOverride: Optional[TableClassType] = None

InputFormatOptionsUnion = Union[InputFormatOptions, InputFormatOptionsOutput]


# This class is the input for the 'update_global_table' function.
class UpdateGlobalTableInput(BaseValidatorModel):
    GlobalTableName: str
    ReplicaUpdates: List[ReplicaUpdate]


# This class is the output for the 'describe_export' function.
class DescribeExportOutput(BaseValidatorModel):
    ExportDescription: ExportDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'export_table_to_point_in_time' function.
class ExportTableToPointInTimeOutput(BaseValidatorModel):
    ExportDescription: ExportDescription
    ResponseMetadata: ResponseMetadata

IncrementalExportSpecificationUnion = Union[IncrementalExportSpecification, IncrementalExportSpecificationOutput]


class ReplicaDescription(BaseValidatorModel):
    RegionName: Optional[str] = None
    ReplicaStatus: Optional[ReplicaStatusType] = None
    ReplicaStatusDescription: Optional[str] = None
    ReplicaStatusPercentProgress: Optional[str] = None
    KMSMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverride] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverride] = None
    WarmThroughput: Optional[TableWarmThroughputDescription] = None
    GlobalSecondaryIndexes: Optional[List[ReplicaGlobalSecondaryIndexDescription]] = None
    ReplicaInaccessibleDateTime: Optional[datetime] = None
    ReplicaTableClassSummary: Optional[TableClassSummary] = None


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


# This class is the output for the 'list_imports' function.
class ListImportsOutput(BaseValidatorModel):
    ImportSummaryList: List[ImportSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateGlobalSecondaryIndexAction(BaseValidatorModel):
    IndexName: str
    KeySchema: List[KeySchemaElement]
    Projection: ProjectionUnion
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    WarmThroughput: Optional[WarmThroughput] = None


class GlobalSecondaryIndex(BaseValidatorModel):
    IndexName: str
    KeySchema: List[KeySchemaElement]
    Projection: ProjectionUnion
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    WarmThroughput: Optional[WarmThroughput] = None


class LocalSecondaryIndex(BaseValidatorModel):
    IndexName: str
    KeySchema: List[KeySchemaElement]
    Projection: ProjectionUnion


# This class is the output for the 'batch_execute_statement' function.
class BatchExecuteStatementOutput(BaseValidatorModel):
    Responses: List[BatchStatementResponse]
    ConsumedCapacity: List[ConsumedCapacity]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_write_item' function.
class BatchWriteItemOutput(BaseValidatorModel):
    UnprocessedItems: Dict[str, List[WriteRequestOutput]]
    ItemCollectionMetrics: Dict[str, List[ItemCollectionMetrics]]
    ConsumedCapacity: List[ConsumedCapacity]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_execute_statement' function.
class BatchExecuteStatementInput(BaseValidatorModel):
    Statements: List[BatchStatementRequest]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None


class QueryInputPaginate(BaseValidatorModel):
    TableName: str
    IndexName: Optional[str] = None
    Select: Optional[SelectType] = None
    AttributesToGet: Optional[List[str]] = None
    ConsistentRead: Optional[bool] = None
    KeyConditions: Optional[Dict[str, Condition]] = None
    QueryFilter: Optional[Dict[str, Condition]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ScanIndexForward: Optional[bool] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[str] = None
    KeyConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, UniversalAttributeValue]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'query' function.
class QueryInput(BaseValidatorModel):
    TableName: str
    IndexName: Optional[str] = None
    Select: Optional[SelectType] = None
    AttributesToGet: Optional[List[str]] = None
    Limit: Optional[int] = None
    ConsistentRead: Optional[bool] = None
    KeyConditions: Optional[Dict[str, Condition]] = None
    QueryFilter: Optional[Dict[str, Condition]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ScanIndexForward: Optional[bool] = None
    ExclusiveStartKey: Optional[Dict[str, UniversalAttributeValue]] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[str] = None
    KeyConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, UniversalAttributeValue]] = None


class ScanInputPaginate(BaseValidatorModel):
    TableName: str
    IndexName: Optional[str] = None
    AttributesToGet: Optional[List[str]] = None
    Select: Optional[SelectType] = None
    ScanFilter: Optional[Dict[str, Condition]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    TotalSegments: Optional[int] = None
    Segment: Optional[int] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, UniversalAttributeValue]] = None
    ConsistentRead: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'scan' function.
class ScanInput(BaseValidatorModel):
    TableName: str
    IndexName: Optional[str] = None
    AttributesToGet: Optional[List[str]] = None
    Limit: Optional[int] = None
    Select: Optional[SelectType] = None
    ScanFilter: Optional[Dict[str, Condition]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ExclusiveStartKey: Optional[Dict[str, UniversalAttributeValue]] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    TotalSegments: Optional[int] = None
    Segment: Optional[int] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, UniversalAttributeValue]] = None
    ConsistentRead: Optional[bool] = None

DeleteRequestUnion = Union[DeleteRequest, DeleteRequestOutput]


# This class is the input for the 'delete_item' function.
class DeleteItemInput(BaseValidatorModel):
    TableName: str
    Key: Dict[str, UniversalAttributeValue]
    Expected: Optional[Dict[str, ExpectedAttributeValue]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


# This class is the input for the 'put_item' function.
class PutItemInput(BaseValidatorModel):
    TableName: str
    Item: Dict[str, UniversalAttributeValue]
    Expected: Optional[Dict[str, ExpectedAttributeValue]] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


# This class is the input for the 'update_item' function.
class UpdateItemInput(BaseValidatorModel):
    TableName: str
    Key: Dict[str, UniversalAttributeValue]
    AttributeUpdates: Optional[Dict[str, AttributeValueUpdate]] = None
    Expected: Optional[Dict[str, ExpectedAttributeValue]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    UpdateExpression: Optional[str] = None
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None
    ExpressionAttributeValues: Optional[Dict[str, UniversalAttributeValue]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None


class TransactGetItem(BaseValidatorModel):
    Get: Get

KeysAndAttributesUnion = Union[KeysAndAttributes, KeysAndAttributesOutput]


# This class is the input for the 'execute_transaction' function.
class ExecuteTransactionInput(BaseValidatorModel):
    TransactStatements: List[ParameterizedStatement]
    ClientRequestToken: Optional[str] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None

PutRequestUnion = Union[PutRequest, PutRequestOutput]


class TransactWriteItem(BaseValidatorModel):
    ConditionCheck: Optional[ConditionCheck] = None
    Put: Optional[Put] = None
    Delete: Optional[Delete] = None
    Update: Optional[Update] = None


class BatchGetItemInputServiceResourceBatchGetItem(BaseValidatorModel):
    RequestItems: Dict[str, KeysAndAttributesServiceResourceUnion]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None


class BatchWriteItemOutputServiceResource(BaseValidatorModel):
    UnprocessedItems: Dict[str, List[WriteRequestServiceResourceOutput]]
    ItemCollectionMetrics: Dict[str, List[ItemCollectionMetricsServiceResource]]
    ConsumedCapacity: List[ConsumedCapacity]
    ResponseMetadata: ResponseMetadata


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


class ReplicationGroupUpdate(BaseValidatorModel):
    Create: Optional[CreateReplicationGroupMemberAction] = None
    Update: Optional[UpdateReplicationGroupMemberAction] = None
    Delete: Optional[DeleteReplicationGroupMemberAction] = None


# This class is the input for the 'export_table_to_point_in_time' function.
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

GlobalSecondaryIndexUnion = Union[GlobalSecondaryIndex, GlobalSecondaryIndexOutput]


class TableCreationParameters(BaseValidatorModel):
    TableName: str
    AttributeDefinitions: List[AttributeDefinition]
    KeySchema: List[KeySchemaElement]
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    SSESpecification: Optional[SSESpecification] = None
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndex]] = None


# This class is the input for the 'transact_get_items' function.
class TransactGetItemsInput(BaseValidatorModel):
    TransactItems: List[TransactGetItem]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None


# This class is the input for the 'batch_get_item' function.
class BatchGetItemInput(BaseValidatorModel):
    RequestItems: Dict[str, KeysAndAttributesUnion]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None


class WriteRequest(BaseValidatorModel):
    PutRequest: Optional[PutRequestUnion] = None
    DeleteRequest: Optional[DeleteRequestUnion] = None


# This class is the input for the 'transact_write_items' function.
class TransactWriteItemsInput(BaseValidatorModel):
    TransactItems: List[TransactWriteItem]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ClientRequestToken: Optional[str] = None

WriteRequestServiceResourceUnion = Union[WriteRequestServiceResource, WriteRequestServiceResourceOutput]


class ReplicaAutoScalingDescription(BaseValidatorModel):
    RegionName: Optional[str] = None
    GlobalSecondaryIndexes: Optional[List[ReplicaGlobalSecondaryIndexAutoScalingDescription]] = None
    ReplicaProvisionedReadCapacityAutoScalingSettings: Optional[AutoScalingSettingsDescription] = None
    ReplicaProvisionedWriteCapacityAutoScalingSettings: Optional[AutoScalingSettingsDescription] = None
    ReplicaStatus: Optional[ReplicaStatusType] = None


class ReplicaSettingsDescription(BaseValidatorModel):
    RegionName: str
    ReplicaStatus: Optional[ReplicaStatusType] = None
    ReplicaBillingModeSummary: Optional[BillingModeSummary] = None
    ReplicaProvisionedReadCapacityUnits: Optional[int] = None
    ReplicaProvisionedReadCapacityAutoScalingSettings: Optional[AutoScalingSettingsDescription] = None
    ReplicaProvisionedWriteCapacityUnits: Optional[int] = None
    ReplicaProvisionedWriteCapacityAutoScalingSettings: Optional[AutoScalingSettingsDescription] = None
    ReplicaGlobalSecondaryIndexSettings: Optional[List[ReplicaGlobalSecondaryIndexSettingsDescription]] = None
    ReplicaTableClassSummary: Optional[TableClassSummary] = None


class ReplicaAutoScalingUpdate(BaseValidatorModel):
    RegionName: str
    ReplicaGlobalSecondaryIndexUpdates: Optional[List[ReplicaGlobalSecondaryIndexAutoScalingUpdate]] = None
    ReplicaProvisionedReadCapacityAutoScalingUpdate: Optional[AutoScalingSettingsUpdate] = None


class ReplicaSettingsUpdate(BaseValidatorModel):
    RegionName: str
    ReplicaProvisionedReadCapacityUnits: Optional[int] = None
    ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate: Optional[AutoScalingSettingsUpdate] = None
    ReplicaGlobalSecondaryIndexSettingsUpdate: Optional[List[ReplicaGlobalSecondaryIndexSettingsUpdate]] = None
    ReplicaTableClass: Optional[TableClassType] = None


# This class is the output for the 'create_global_table' function.
class CreateGlobalTableOutput(BaseValidatorModel):
    GlobalTableDescription: GlobalTableDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_global_table' function.
class DescribeGlobalTableOutput(BaseValidatorModel):
    GlobalTableDescription: GlobalTableDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_global_table' function.
class UpdateGlobalTableOutput(BaseValidatorModel):
    GlobalTableDescription: GlobalTableDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_table' function.
class CreateTableOutput(BaseValidatorModel):
    TableDescription: TableDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_table' function.
class DeleteTableOutput(BaseValidatorModel):
    TableDescription: TableDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_table' function.
class DescribeTableOutput(BaseValidatorModel):
    Table: TableDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_table_from_backup' function.
class RestoreTableFromBackupOutput(BaseValidatorModel):
    TableDescription: TableDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_table_to_point_in_time' function.
class RestoreTableToPointInTimeOutput(BaseValidatorModel):
    TableDescription: TableDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_table' function.
class UpdateTableOutput(BaseValidatorModel):
    TableDescription: TableDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_import' function.
class DescribeImportOutput(BaseValidatorModel):
    ImportTableDescription: ImportTableDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_table' function.
class ImportTableOutput(BaseValidatorModel):
    ImportTableDescription: ImportTableDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_backup' function.
class DeleteBackupOutput(BaseValidatorModel):
    BackupDescription: BackupDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_backup' function.
class DescribeBackupOutput(BaseValidatorModel):
    BackupDescription: BackupDescription
    ResponseMetadata: ResponseMetadata


class UpdateTableInputTableUpdate(BaseValidatorModel):
    AttributeDefinitions: Optional[List[AttributeDefinition]] = None
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    GlobalSecondaryIndexUpdates: Optional[List[GlobalSecondaryIndexUpdate]] = None
    StreamSpecification: Optional[StreamSpecification] = None
    SSESpecification: Optional[SSESpecification] = None
    ReplicaUpdates: Optional[List[ReplicationGroupUpdate]] = None
    TableClass: Optional[TableClassType] = None
    DeletionProtectionEnabled: Optional[bool] = None
    MultiRegionConsistency: Optional[MultiRegionConsistencyType] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    WarmThroughput: Optional[WarmThroughput] = None


# This class is the input for the 'update_table' function.
class UpdateTableInput(BaseValidatorModel):
    TableName: str
    AttributeDefinitions: Optional[List[AttributeDefinition]] = None
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    GlobalSecondaryIndexUpdates: Optional[List[GlobalSecondaryIndexUpdate]] = None
    StreamSpecification: Optional[StreamSpecification] = None
    SSESpecification: Optional[SSESpecification] = None
    ReplicaUpdates: Optional[List[ReplicationGroupUpdate]] = None
    TableClass: Optional[TableClassType] = None
    DeletionProtectionEnabled: Optional[bool] = None
    MultiRegionConsistency: Optional[MultiRegionConsistencyType] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None
    WarmThroughput: Optional[WarmThroughput] = None


class CreateTableInputServiceResourceCreateTable(BaseValidatorModel):
    AttributeDefinitions: List[AttributeDefinition]
    TableName: str
    KeySchema: List[KeySchemaElement]
    LocalSecondaryIndexes: Optional[List[LocalSecondaryIndex]] = None
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndexUnion]] = None
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    StreamSpecification: Optional[StreamSpecification] = None
    SSESpecification: Optional[SSESpecification] = None
    Tags: Optional[List[Tag]] = None
    TableClass: Optional[TableClassType] = None
    DeletionProtectionEnabled: Optional[bool] = None
    WarmThroughput: Optional[WarmThroughput] = None
    ResourcePolicy: Optional[str] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None


# This class is the input for the 'create_table' function.
class CreateTableInput(BaseValidatorModel):
    AttributeDefinitions: List[AttributeDefinition]
    TableName: str
    KeySchema: List[KeySchemaElement]
    LocalSecondaryIndexes: Optional[List[LocalSecondaryIndex]] = None
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndexUnion]] = None
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughput] = None
    StreamSpecification: Optional[StreamSpecification] = None
    SSESpecification: Optional[SSESpecification] = None
    Tags: Optional[List[Tag]] = None
    TableClass: Optional[TableClassType] = None
    DeletionProtectionEnabled: Optional[bool] = None
    WarmThroughput: Optional[WarmThroughput] = None
    ResourcePolicy: Optional[str] = None
    OnDemandThroughput: Optional[OnDemandThroughput] = None


# This class is the input for the 'restore_table_from_backup' function.
class RestoreTableFromBackupInput(BaseValidatorModel):
    TargetTableName: str
    BackupArn: str
    BillingModeOverride: Optional[BillingModeType] = None
    GlobalSecondaryIndexOverride: Optional[List[GlobalSecondaryIndexUnion]] = None
    LocalSecondaryIndexOverride: Optional[List[LocalSecondaryIndex]] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughput] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughput] = None
    SSESpecificationOverride: Optional[SSESpecification] = None


# This class is the input for the 'restore_table_to_point_in_time' function.
class RestoreTableToPointInTimeInput(BaseValidatorModel):
    TargetTableName: str
    SourceTableArn: Optional[str] = None
    SourceTableName: Optional[str] = None
    UseLatestRestorableTime: Optional[bool] = None
    RestoreDateTime: Optional[Timestamp] = None
    BillingModeOverride: Optional[BillingModeType] = None
    GlobalSecondaryIndexOverride: Optional[List[GlobalSecondaryIndexUnion]] = None
    LocalSecondaryIndexOverride: Optional[List[LocalSecondaryIndex]] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughput] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughput] = None
    SSESpecificationOverride: Optional[SSESpecification] = None

TableCreationParametersUnion = Union[TableCreationParameters, TableCreationParametersOutput]

WriteRequestUnion = Union[WriteRequest, WriteRequestOutput]


class BatchWriteItemInputServiceResourceBatchWriteItem(BaseValidatorModel):
    RequestItems: Dict[str, List[WriteRequestServiceResourceUnion]]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None


class TableAutoScalingDescription(BaseValidatorModel):
    TableName: Optional[str] = None
    TableStatus: Optional[TableStatusType] = None
    Replicas: Optional[List[ReplicaAutoScalingDescription]] = None


# This class is the output for the 'describe_global_table_settings' function.
class DescribeGlobalTableSettingsOutput(BaseValidatorModel):
    GlobalTableName: str
    ReplicaSettings: List[ReplicaSettingsDescription]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_global_table_settings' function.
class UpdateGlobalTableSettingsOutput(BaseValidatorModel):
    GlobalTableName: str
    ReplicaSettings: List[ReplicaSettingsDescription]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_table_replica_auto_scaling' function.
class UpdateTableReplicaAutoScalingInput(BaseValidatorModel):
    TableName: str
    GlobalSecondaryIndexUpdates: Optional[List[GlobalSecondaryIndexAutoScalingUpdate]] = None
    ProvisionedWriteCapacityAutoScalingUpdate: Optional[AutoScalingSettingsUpdate] = None
    ReplicaUpdates: Optional[List[ReplicaAutoScalingUpdate]] = None


# This class is the input for the 'update_global_table_settings' function.
class UpdateGlobalTableSettingsInput(BaseValidatorModel):
    GlobalTableName: str
    GlobalTableBillingMode: Optional[BillingModeType] = None
    GlobalTableProvisionedWriteCapacityUnits: Optional[int] = None
    GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: Optional[AutoScalingSettingsUpdate] = None
    GlobalTableGlobalSecondaryIndexSettingsUpdate: Optional[List[GlobalTableGlobalSecondaryIndexSettingsUpdate]] = None
    ReplicaSettingsUpdate: Optional[List[ReplicaSettingsUpdate]] = None


# This class is the input for the 'import_table' function.
class ImportTableInput(BaseValidatorModel):
    S3BucketSource: S3BucketSource
    InputFormat: InputFormatType
    TableCreationParameters: TableCreationParametersUnion
    ClientToken: Optional[str] = None
    InputFormatOptions: Optional[InputFormatOptionsUnion] = None
    InputCompressionType: Optional[InputCompressionTypeType] = None


# This class is the input for the 'batch_write_item' function.
class BatchWriteItemInput(BaseValidatorModel):
    RequestItems: Dict[str, List[WriteRequestUnion]]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None


# This class is the output for the 'describe_table_replica_auto_scaling' function.
class DescribeTableReplicaAutoScalingOutput(BaseValidatorModel):
    TableAutoScalingDescription: TableAutoScalingDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_table_replica_auto_scaling' function.
class UpdateTableReplicaAutoScalingOutput(BaseValidatorModel):
    TableAutoScalingDescription: TableAutoScalingDescription
    ResponseMetadata: ResponseMetadata