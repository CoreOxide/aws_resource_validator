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
from aws_resource_validator.pydantic_models.dynamodb_constants import *

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ArchivalSummaryTypeDef(BaseModel):
    ArchivalDateTime: Optional[datetime] = None
    ArchivalReason: Optional[str] = None
    ArchivalBackupArn: Optional[str] = None

class AttributeDefinitionTypeDef(BaseModel):
    AttributeName: str
    AttributeType: ScalarAttributeTypeType

class AttributeValueTypeDef(BaseModel):
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

class AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef(BaseModel):
    TargetValue: float
    DisableScaleIn: Optional[bool] = None
    ScaleInCooldown: Optional[int] = None
    ScaleOutCooldown: Optional[int] = None

class AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef(BaseModel):
    TargetValue: float
    DisableScaleIn: Optional[bool] = None
    ScaleInCooldown: Optional[int] = None
    ScaleOutCooldown: Optional[int] = None

class BackupDetailsTypeDef(BaseModel):
    BackupArn: str
    BackupName: str
    BackupStatus: BackupStatusType
    BackupType: BackupTypeType
    BackupCreationDateTime: datetime
    BackupSizeBytes: Optional[int] = None
    BackupExpiryDateTime: Optional[datetime] = None

class BackupSummaryTypeDef(BaseModel):
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

class BillingModeSummaryTypeDef(BaseModel):
    BillingMode: Optional[BillingModeType] = None
    LastUpdateToPayPerRequestDateTime: Optional[datetime] = None

class CapacityTypeDef(BaseModel):
    ReadCapacityUnits: Optional[float] = None
    WriteCapacityUnits: Optional[float] = None
    CapacityUnits: Optional[float] = None

class PointInTimeRecoveryDescriptionTypeDef(BaseModel):
    PointInTimeRecoveryStatus: Optional[PointInTimeRecoveryStatusType] = None
    EarliestRestorableDateTime: Optional[datetime] = None
    LatestRestorableDateTime: Optional[datetime] = None

class ContributorInsightsSummaryTypeDef(BaseModel):
    TableName: Optional[str] = None
    IndexName: Optional[str] = None
    ContributorInsightsStatus: Optional[ContributorInsightsStatusType] = None

class CreateBackupInputRequestTypeDef(BaseModel):
    TableName: str
    BackupName: str

class KeySchemaElementTypeDef(BaseModel):
    AttributeName: str
    KeyType: KeyTypeType

class OnDemandThroughputTypeDef(BaseModel):
    MaxReadRequestUnits: Optional[int] = None
    MaxWriteRequestUnits: Optional[int] = None

class ProjectionTypeDef(BaseModel):
    ProjectionType: Optional[ProjectionTypeType] = None
    NonKeyAttributes: Optional[Sequence[str]] = None

class ProvisionedThroughputTypeDef(BaseModel):
    ReadCapacityUnits: int
    WriteCapacityUnits: int

class ReplicaTypeDef(BaseModel):
    RegionName: Optional[str] = None

class CreateReplicaActionTypeDef(BaseModel):
    RegionName: str

class OnDemandThroughputOverrideTypeDef(BaseModel):
    MaxReadRequestUnits: Optional[int] = None

class ProvisionedThroughputOverrideTypeDef(BaseModel):
    ReadCapacityUnits: Optional[int] = None

class SSESpecificationTypeDef(BaseModel):
    Enabled: Optional[bool] = None
    SSEType: Optional[SSETypeType] = None
    KMSMasterKeyId: Optional[str] = None

class StreamSpecificationTypeDef(BaseModel):
    StreamEnabled: bool
    StreamViewType: Optional[StreamViewTypeType] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CsvOptionsOutputTypeDef(BaseModel):
    Delimiter: Optional[str] = None
    HeaderList: Optional[List[str]] = None

class CsvOptionsTypeDef(BaseModel):
    Delimiter: Optional[str] = None
    HeaderList: Optional[Sequence[str]] = None

class DeleteBackupInputRequestTypeDef(BaseModel):
    BackupArn: str

class DeleteGlobalSecondaryIndexActionTypeDef(BaseModel):
    IndexName: str

class DeleteReplicaActionTypeDef(BaseModel):
    RegionName: str

class DeleteReplicationGroupMemberActionTypeDef(BaseModel):
    RegionName: str

class DeleteResourcePolicyInputRequestTypeDef(BaseModel):
    ResourceArn: str
    ExpectedRevisionId: Optional[str] = None

class DeleteTableInputRequestTypeDef(BaseModel):
    TableName: str

class DescribeBackupInputRequestTypeDef(BaseModel):
    BackupArn: str

class DescribeContinuousBackupsInputRequestTypeDef(BaseModel):
    TableName: str

class DescribeContributorInsightsInputRequestTypeDef(BaseModel):
    TableName: str
    IndexName: Optional[str] = None

class FailureExceptionTypeDef(BaseModel):
    ExceptionName: Optional[str] = None
    ExceptionDescription: Optional[str] = None

class EndpointTypeDef(BaseModel):
    Address: str
    CachePeriodInMinutes: int

class DescribeExportInputRequestTypeDef(BaseModel):
    ExportArn: str

class DescribeGlobalTableInputRequestTypeDef(BaseModel):
    GlobalTableName: str

class DescribeGlobalTableSettingsInputRequestTypeDef(BaseModel):
    GlobalTableName: str

class DescribeImportInputRequestTypeDef(BaseModel):
    ImportArn: str

class DescribeKinesisStreamingDestinationInputRequestTypeDef(BaseModel):
    TableName: str

class KinesisDataStreamDestinationTypeDef(BaseModel):
    StreamArn: Optional[str] = None
    DestinationStatus: Optional[DestinationStatusType] = None
    DestinationStatusDescription: Optional[str] = None
    ApproximateCreationDateTimePrecision: Optional[       ApproximateCreationDateTimePrecisionType     ] = None

class DescribeTableInputRequestTypeDef(BaseModel):
    TableName: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeTableReplicaAutoScalingInputRequestTypeDef(BaseModel):
    TableName: str

class DescribeTimeToLiveInputRequestTypeDef(BaseModel):
    TableName: str

class TimeToLiveDescriptionTypeDef(BaseModel):
    TimeToLiveStatus: Optional[TimeToLiveStatusType] = None
    AttributeName: Optional[str] = None

class EnableKinesisStreamingConfigurationTypeDef(BaseModel):
    ApproximateCreationDateTimePrecision: Optional[       ApproximateCreationDateTimePrecisionType     ] = None

class IncrementalExportSpecificationOutputTypeDef(BaseModel):
    ExportFromTime: Optional[datetime] = None
    ExportToTime: Optional[datetime] = None
    ExportViewType: Optional[ExportViewTypeType] = None

class ExportSummaryTypeDef(BaseModel):
    ExportArn: Optional[str] = None
    ExportStatus: Optional[ExportStatusType] = None
    ExportType: Optional[ExportTypeType] = None

class GetResourcePolicyInputRequestTypeDef(BaseModel):
    ResourceArn: str

class ProjectionExtraOutputTypeDef(BaseModel):
    ProjectionType: Optional[ProjectionTypeType] = None
    NonKeyAttributes: Optional[List[str]] = None

class ProvisionedThroughputDescriptionTypeDef(BaseModel):
    LastIncreaseDateTime: Optional[datetime] = None
    LastDecreaseDateTime: Optional[datetime] = None
    NumberOfDecreasesToday: Optional[int] = None
    ReadCapacityUnits: Optional[int] = None
    WriteCapacityUnits: Optional[int] = None

class ProjectionOutputTypeDef(BaseModel):
    ProjectionType: Optional[ProjectionTypeType] = None
    NonKeyAttributes: Optional[List[str]] = None

class S3BucketSourceTypeDef(BaseModel):
    S3Bucket: str
    S3BucketOwner: Optional[str] = None
    S3KeyPrefix: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListContributorInsightsInputRequestTypeDef(BaseModel):
    TableName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListExportsInputRequestTypeDef(BaseModel):
    TableArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListGlobalTablesInputRequestTypeDef(BaseModel):
    ExclusiveStartGlobalTableName: Optional[str] = None
    Limit: Optional[int] = None
    RegionName: Optional[str] = None

class ListImportsInputRequestTypeDef(BaseModel):
    TableArn: Optional[str] = None
    PageSize: Optional[int] = None
    NextToken: Optional[str] = None

class ListTablesInputRequestTypeDef(BaseModel):
    ExclusiveStartTableName: Optional[str] = None
    Limit: Optional[int] = None

class ListTagsOfResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    NextToken: Optional[str] = None

class PointInTimeRecoverySpecificationTypeDef(BaseModel):
    PointInTimeRecoveryEnabled: bool

class PutResourcePolicyInputRequestTypeDef(BaseModel):
    ResourceArn: str
    Policy: str
    ExpectedRevisionId: Optional[str] = None
    ConfirmRemoveSelfResourceAccess: Optional[bool] = None

class TableClassSummaryTypeDef(BaseModel):
    TableClass: Optional[TableClassType] = None
    LastUpdateDateTime: Optional[datetime] = None

class RestoreSummaryTypeDef(BaseModel):
    RestoreDateTime: datetime
    RestoreInProgress: bool
    SourceBackupArn: Optional[str] = None
    SourceTableArn: Optional[str] = None

class SSEDescriptionTypeDef(BaseModel):
    Status: Optional[SSEStatusType] = None
    SSEType: Optional[SSETypeType] = None
    KMSMasterKeyArn: Optional[str] = None
    InaccessibleEncryptionDateTime: Optional[datetime] = None

class TableBatchWriterRequestTypeDef(BaseModel):
    overwrite_by_pkeys: Optional[List[str]] = None

class TimeToLiveSpecificationTypeDef(BaseModel):
    Enabled: bool
    AttributeName: str

class UntagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateContributorInsightsInputRequestTypeDef(BaseModel):
    TableName: str
    ContributorInsightsAction: ContributorInsightsActionType
    IndexName: Optional[str] = None

class UpdateKinesisStreamingConfigurationTypeDef(BaseModel):
    ApproximateCreationDateTimePrecision: Optional[       ApproximateCreationDateTimePrecisionType     ] = None

class ArchivalSummaryResponseTypeDef(BaseModel):
    ArchivalDateTime: datetime
    ArchivalReason: str
    ArchivalBackupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class BillingModeSummaryResponseTypeDef(BaseModel):
    BillingMode: BillingModeType
    LastUpdateToPayPerRequestDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourcePolicyOutputTypeDef(BaseModel):
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLimitsOutputTypeDef(BaseModel):
    AccountMaxReadCapacityUnits: int
    AccountMaxWriteCapacityUnits: int
    TableMaxReadCapacityUnits: int
    TableMaxWriteCapacityUnits: int
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyOutputTypeDef(BaseModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTablesOutputTypeDef(BaseModel):
    TableNames: List[str]
    LastEvaluatedTableName: str
    ResponseMetadata: ResponseMetadataTypeDef

class OnDemandThroughputResponseTypeDef(BaseModel):
    MaxReadRequestUnits: int
    MaxWriteRequestUnits: int
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionedThroughputDescriptionResponseTypeDef(BaseModel):
    LastIncreaseDateTime: datetime
    LastDecreaseDateTime: datetime
    NumberOfDecreasesToday: int
    ReadCapacityUnits: int
    WriteCapacityUnits: int
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyOutputTypeDef(BaseModel):
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreSummaryResponseTypeDef(BaseModel):
    SourceBackupArn: str
    SourceTableArn: str
    RestoreDateTime: datetime
    RestoreInProgress: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SSEDescriptionResponseTypeDef(BaseModel):
    Status: SSEStatusType
    SSEType: SSETypeType
    KMSMasterKeyArn: str
    InaccessibleEncryptionDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StreamSpecificationResponseTypeDef(BaseModel):
    StreamEnabled: bool
    StreamViewType: StreamViewTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class TableClassSummaryResponseTypeDef(BaseModel):
    TableClass: TableClassType
    LastUpdateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContributorInsightsOutputTypeDef(BaseModel):
    TableName: str
    IndexName: str
    ContributorInsightsStatus: ContributorInsightsStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class BatchStatementErrorTypeDef(BaseModel):
    Code: Optional[BatchStatementErrorCodeEnumType] = None
    Message: Optional[str] = None
    Item: Optional[Dict[str, AttributeValueTypeDef]] = None

class DeleteRequestOutputTypeDef(BaseModel):
    Key: Dict[str, AttributeValueTypeDef]

class ItemCollectionMetricsTypeDef(BaseModel):
    ItemCollectionKey: Optional[Dict[str, AttributeValueTypeDef]] = None
    SizeEstimateRangeGB: Optional[List[float]] = None

class ItemResponseTypeDef(BaseModel):
    Item: Optional[Dict[str, AttributeValueTypeDef]] = None

class KeysAndAttributesOutputTypeDef(BaseModel):
    Keys: List[Dict[str, AttributeValueTypeDef]]
    AttributesToGet: Optional[List[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None

class PutRequestOutputTypeDef(BaseModel):
    Item: Dict[str, AttributeValueTypeDef]

class AttributeValueUpdateTableTypeDef(BaseModel):
    Value: Optional[TableAttributeValueTypeDef] = None
    Action: Optional[AttributeActionType] = None

class ConditionTableTypeDef(BaseModel):
    ComparisonOperator: ComparisonOperatorType
    AttributeValueList: Optional[Sequence[TableAttributeValueTypeDef]] = None

class DeleteRequestServiceResourceOutputTypeDef(BaseModel):
    Key: Dict[str, TableAttributeValueTypeDef]

class DeleteRequestServiceResourceTypeDef(BaseModel):
    Key: Mapping[str, TableAttributeValueTypeDef]

class ExpectedAttributeValueTableTypeDef(BaseModel):
    Value: Optional[TableAttributeValueTypeDef] = None
    Exists: Optional[bool] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    AttributeValueList: Optional[Sequence[TableAttributeValueTypeDef]] = None

class GetItemInputTableGetItemTypeDef(BaseModel):
    Key: Mapping[str, TableAttributeValueTypeDef]
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None

class ItemCollectionMetricsServiceResourceTypeDef(BaseModel):
    ItemCollectionKey: Optional[Dict[str, TableAttributeValueTypeDef]] = None
    SizeEstimateRangeGB: Optional[List[float]] = None

class ItemCollectionMetricsTableTypeDef(BaseModel):
    ItemCollectionKey: Optional[Dict[str, TableAttributeValueTypeDef]] = None
    SizeEstimateRangeGB: Optional[List[float]] = None

class KeysAndAttributesServiceResourceOutputTypeDef(BaseModel):
    Keys: List[Dict[str, TableAttributeValueTypeDef]]
    AttributesToGet: Optional[List[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None

class KeysAndAttributesServiceResourceTypeDef(BaseModel):
    Keys: Sequence[Mapping[str, TableAttributeValueTypeDef]]
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None

class PutRequestServiceResourceOutputTypeDef(BaseModel):
    Item: Dict[str, TableAttributeValueTypeDef]

class PutRequestServiceResourceTypeDef(BaseModel):
    Item: Mapping[str, TableAttributeValueTypeDef]

class AutoScalingPolicyDescriptionTypeDef(BaseModel):
    PolicyName: Optional[str] = None
    TargetTrackingScalingPolicyConfiguration: Optional[       AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef     ] = None

class AutoScalingPolicyUpdateTypeDef(BaseModel):
    TargetTrackingScalingPolicyConfiguration: AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef
    PolicyName: Optional[str] = None

class CreateBackupOutputTypeDef(BaseModel):
    BackupDetails: BackupDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupsOutputTypeDef(BaseModel):
    BackupSummaries: List[BackupSummaryTypeDef]
    LastEvaluatedBackupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConsumedCapacityTypeDef(BaseModel):
    TableName: Optional[str] = None
    CapacityUnits: Optional[float] = None
    ReadCapacityUnits: Optional[float] = None
    WriteCapacityUnits: Optional[float] = None
    Table: Optional[CapacityTypeDef] = None
    LocalSecondaryIndexes: Optional[Dict[str, CapacityTypeDef]] = None
    GlobalSecondaryIndexes: Optional[Dict[str, CapacityTypeDef]] = None

class ContinuousBackupsDescriptionTypeDef(BaseModel):
    ContinuousBackupsStatus: ContinuousBackupsStatusType
    PointInTimeRecoveryDescription: Optional[PointInTimeRecoveryDescriptionTypeDef] = None

class ListContributorInsightsOutputTypeDef(BaseModel):
    ContributorInsightsSummaries: List[ContributorInsightsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LocalSecondaryIndexTypeDef(BaseModel):
    IndexName: str
    KeySchema: Sequence[KeySchemaElementTypeDef]
    Projection: ProjectionTypeDef

class CreateGlobalSecondaryIndexActionTypeDef(BaseModel):
    IndexName: str
    KeySchema: Sequence[KeySchemaElementTypeDef]
    Projection: ProjectionTypeDef
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class GlobalSecondaryIndexTypeDef(BaseModel):
    IndexName: str
    KeySchema: Sequence[KeySchemaElementTypeDef]
    Projection: ProjectionTypeDef
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class SourceTableDetailsTypeDef(BaseModel):
    TableName: str
    TableId: str
    KeySchema: List[KeySchemaElementTypeDef]
    TableCreationDateTime: datetime
    ProvisionedThroughput: ProvisionedThroughputTypeDef
    TableArn: Optional[str] = None
    TableSizeBytes: Optional[int] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None
    ItemCount: Optional[int] = None
    BillingMode: Optional[BillingModeType] = None

class UpdateGlobalSecondaryIndexActionTypeDef(BaseModel):
    IndexName: str
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class CreateGlobalTableInputRequestTypeDef(BaseModel):
    GlobalTableName: str
    ReplicationGroup: Sequence[ReplicaTypeDef]

class GlobalTableTypeDef(BaseModel):
    GlobalTableName: Optional[str] = None
    ReplicationGroup: Optional[List[ReplicaTypeDef]] = None

class ReplicaGlobalSecondaryIndexDescriptionTypeDef(BaseModel):
    IndexName: Optional[str] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverrideTypeDef] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverrideTypeDef] = None

class ReplicaGlobalSecondaryIndexTypeDef(BaseModel):
    IndexName: str
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverrideTypeDef] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverrideTypeDef] = None

class ListTagsOfResourceOutputTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class InputFormatOptionsOutputTypeDef(BaseModel):
    Csv: Optional[CsvOptionsOutputTypeDef] = None

class InputFormatOptionsTypeDef(BaseModel):
    Csv: Optional[CsvOptionsTypeDef] = None

class ReplicaUpdateTypeDef(BaseModel):
    Create: Optional[CreateReplicaActionTypeDef] = None
    Delete: Optional[DeleteReplicaActionTypeDef] = None

class DescribeContributorInsightsOutputTypeDef(BaseModel):
    TableName: str
    IndexName: str
    ContributorInsightsRuleList: List[str]
    ContributorInsightsStatus: ContributorInsightsStatusType
    LastUpdateDateTime: datetime
    FailureException: FailureExceptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointsResponseTypeDef(BaseModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKinesisStreamingDestinationOutputTypeDef(BaseModel):
    TableName: str
    KinesisDataStreamDestinations: List[KinesisDataStreamDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTableInputTableExistsWaitTypeDef(BaseModel):
    TableName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTableInputTableNotExistsWaitTypeDef(BaseModel):
    TableName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTimeToLiveOutputTypeDef(BaseModel):
    TimeToLiveDescription: TimeToLiveDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class KinesisStreamingDestinationInputRequestTypeDef(BaseModel):
    TableName: str
    StreamArn: str
    EnableKinesisStreamingConfiguration: Optional[       EnableKinesisStreamingConfigurationTypeDef     ] = None

class KinesisStreamingDestinationOutputTypeDef(BaseModel):
    TableName: str
    StreamArn: str
    DestinationStatus: DestinationStatusType
    EnableKinesisStreamingConfiguration: EnableKinesisStreamingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportDescriptionTypeDef(BaseModel):
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
    IncrementalExportSpecification: Optional[IncrementalExportSpecificationOutputTypeDef] = None

class ListExportsOutputTypeDef(BaseModel):
    ExportSummaries: List[ExportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class IncrementalExportSpecificationTypeDef(BaseModel):
    ExportFromTime: Optional[TimestampTypeDef] = None
    ExportToTime: Optional[TimestampTypeDef] = None
    ExportViewType: Optional[ExportViewTypeType] = None

class ListBackupsInputRequestTypeDef(BaseModel):
    TableName: Optional[str] = None
    Limit: Optional[int] = None
    TimeRangeLowerBound: Optional[TimestampTypeDef] = None
    TimeRangeUpperBound: Optional[TimestampTypeDef] = None
    ExclusiveStartBackupArn: Optional[str] = None
    BackupType: Optional[BackupTypeFilterType] = None

class LocalSecondaryIndexDescriptionTypeDef(BaseModel):
    IndexName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElementTypeDef]] = None
    Projection: Optional[ProjectionExtraOutputTypeDef] = None
    IndexSizeBytes: Optional[int] = None
    ItemCount: Optional[int] = None
    IndexArn: Optional[str] = None

class GlobalSecondaryIndexDescriptionTypeDef(BaseModel):
    IndexName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElementTypeDef]] = None
    Projection: Optional[ProjectionExtraOutputTypeDef] = None
    IndexStatus: Optional[IndexStatusType] = None
    Backfilling: Optional[bool] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputDescriptionTypeDef] = None
    IndexSizeBytes: Optional[int] = None
    ItemCount: Optional[int] = None
    IndexArn: Optional[str] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class GlobalSecondaryIndexInfoTypeDef(BaseModel):
    IndexName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElementTypeDef]] = None
    Projection: Optional[ProjectionOutputTypeDef] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class GlobalSecondaryIndexOutputTypeDef(BaseModel):
    IndexName: str
    KeySchema: List[KeySchemaElementTypeDef]
    Projection: ProjectionOutputTypeDef
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class LocalSecondaryIndexInfoTypeDef(BaseModel):
    IndexName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElementTypeDef]] = None
    Projection: Optional[ProjectionOutputTypeDef] = None

class ImportSummaryTypeDef(BaseModel):
    ImportArn: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    TableArn: Optional[str] = None
    S3BucketSource: Optional[S3BucketSourceTypeDef] = None
    CloudWatchLogGroupArn: Optional[str] = None
    InputFormat: Optional[InputFormatType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class ListBackupsInputListBackupsPaginateTypeDef(BaseModel):
    TableName: Optional[str] = None
    TimeRangeLowerBound: Optional[TimestampTypeDef] = None
    TimeRangeUpperBound: Optional[TimestampTypeDef] = None
    BackupType: Optional[BackupTypeFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTablesInputListTablesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsOfResourceInputListTagsOfResourcePaginateTypeDef(BaseModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class UpdateContinuousBackupsInputRequestTypeDef(BaseModel):
    TableName: str
    PointInTimeRecoverySpecification: PointInTimeRecoverySpecificationTypeDef

class UpdateTimeToLiveInputRequestTypeDef(BaseModel):
    TableName: str
    TimeToLiveSpecification: TimeToLiveSpecificationTypeDef

class UpdateTimeToLiveOutputTypeDef(BaseModel):
    TimeToLiveSpecification: TimeToLiveSpecificationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKinesisStreamingDestinationInputRequestTypeDef(BaseModel):
    TableName: str
    StreamArn: str
    UpdateKinesisStreamingConfiguration: Optional[       UpdateKinesisStreamingConfigurationTypeDef     ] = None

class UpdateKinesisStreamingDestinationOutputTypeDef(BaseModel):
    TableName: str
    StreamArn: str
    DestinationStatus: DestinationStatusType
    UpdateKinesisStreamingConfiguration: UpdateKinesisStreamingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchStatementResponseTypeDef(BaseModel):
    Error: Optional[BatchStatementErrorTypeDef] = None
    TableName: Optional[str] = None
    Item: Optional[Dict[str, AttributeValueTypeDef]] = None

class WriteRequestOutputTypeDef(BaseModel):
    PutRequest: Optional[PutRequestOutputTypeDef] = None
    DeleteRequest: Optional[DeleteRequestOutputTypeDef] = None

class AttributeValueUpdateTypeDef(BaseModel):
    Value: Optional[UniversalAttributeValueTypeDef] = None
    Action: Optional[AttributeActionType] = None

class BatchStatementRequestTypeDef(BaseModel):
    Statement: str
    Parameters: Optional[Sequence[UniversalAttributeValueTypeDef]] = None
    ConsistentRead: Optional[bool] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class ConditionCheckTypeDef(BaseModel):
    Key: Mapping[str, UniversalAttributeValueTypeDef]
    TableName: str
    ConditionExpression: str
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class ConditionTypeDef(BaseModel):
    ComparisonOperator: ComparisonOperatorType
    AttributeValueList: Optional[Sequence[UniversalAttributeValueTypeDef]] = None

class DeleteRequestTypeDef(BaseModel):
    Key: Mapping[str, UniversalAttributeValueTypeDef]

class DeleteTypeDef(BaseModel):
    Key: Mapping[str, UniversalAttributeValueTypeDef]
    TableName: str
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class ExecuteStatementInputRequestTypeDef(BaseModel):
    Statement: str
    Parameters: Optional[Sequence[UniversalAttributeValueTypeDef]] = None
    ConsistentRead: Optional[bool] = None
    NextToken: Optional[str] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    Limit: Optional[int] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class ExpectedAttributeValueTypeDef(BaseModel):
    Value: Optional[UniversalAttributeValueTypeDef] = None
    Exists: Optional[bool] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    AttributeValueList: Optional[Sequence[UniversalAttributeValueTypeDef]] = None

class GetItemInputRequestTypeDef(BaseModel):
    TableName: str
    Key: Mapping[str, UniversalAttributeValueTypeDef]
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None

class GetTypeDef(BaseModel):
    Key: Mapping[str, UniversalAttributeValueTypeDef]
    TableName: str
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None

class KeysAndAttributesTypeDef(BaseModel):
    Keys: Sequence[Mapping[str, UniversalAttributeValueTypeDef]]
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None

class ParameterizedStatementTypeDef(BaseModel):
    Statement: str
    Parameters: Optional[Sequence[UniversalAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class PutRequestTypeDef(BaseModel):
    Item: Mapping[str, UniversalAttributeValueTypeDef]

class PutTypeDef(BaseModel):
    Item: Mapping[str, UniversalAttributeValueTypeDef]
    TableName: str
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class UpdateTypeDef(BaseModel):
    Key: Mapping[str, UniversalAttributeValueTypeDef]
    UpdateExpression: str
    TableName: str
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class QueryInputTableQueryTypeDef(BaseModel):
    IndexName: Optional[str] = None
    Select: Optional[SelectType] = None
    AttributesToGet: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    ConsistentRead: Optional[bool] = None
    KeyConditions: Optional[Mapping[str, ConditionTableTypeDef]] = None
    QueryFilter: Optional[Mapping[str, ConditionTableTypeDef]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ScanIndexForward: Optional[bool] = None
    ExclusiveStartKey: Optional[Mapping[str, TableAttributeValueTypeDef]] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[ConditionBaseImportTypeDef] = None
    KeyConditionExpression: Optional[ConditionBaseImportTypeDef] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, TableAttributeValueTypeDef]] = None

class ScanInputTableScanTypeDef(BaseModel):
    IndexName: Optional[str] = None
    AttributesToGet: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    Select: Optional[SelectType] = None
    ScanFilter: Optional[Mapping[str, ConditionTableTypeDef]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ExclusiveStartKey: Optional[Mapping[str, TableAttributeValueTypeDef]] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    TotalSegments: Optional[int] = None
    Segment: Optional[int] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[ConditionBaseImportTypeDef] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, TableAttributeValueTypeDef]] = None
    ConsistentRead: Optional[bool] = None

class DeleteItemInputTableDeleteItemTypeDef(BaseModel):
    Key: Mapping[str, TableAttributeValueTypeDef]
    Expected: Optional[Mapping[str, ExpectedAttributeValueTableTypeDef]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ConditionExpression: Optional[ConditionBaseImportTypeDef] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, TableAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class PutItemInputTablePutItemTypeDef(BaseModel):
    Item: Mapping[str, TableAttributeValueTypeDef]
    Expected: Optional[Mapping[str, ExpectedAttributeValueTableTypeDef]] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ConditionExpression: Optional[ConditionBaseImportTypeDef] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, TableAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class UpdateItemInputTableUpdateItemTypeDef(BaseModel):
    Key: Mapping[str, TableAttributeValueTypeDef]
    AttributeUpdates: Optional[Mapping[str, AttributeValueUpdateTableTypeDef]] = None
    Expected: Optional[Mapping[str, ExpectedAttributeValueTableTypeDef]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    UpdateExpression: Optional[str] = None
    ConditionExpression: Optional[ConditionBaseImportTypeDef] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, TableAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class WriteRequestServiceResourceOutputTypeDef(BaseModel):
    PutRequest: Optional[PutRequestServiceResourceOutputTypeDef] = None
    DeleteRequest: Optional[DeleteRequestServiceResourceOutputTypeDef] = None

class WriteRequestServiceResourceTypeDef(BaseModel):
    PutRequest: Optional[PutRequestServiceResourceTypeDef] = None
    DeleteRequest: Optional[DeleteRequestServiceResourceTypeDef] = None

class AutoScalingSettingsDescriptionTypeDef(BaseModel):
    MinimumUnits: Optional[int] = None
    MaximumUnits: Optional[int] = None
    AutoScalingDisabled: Optional[bool] = None
    AutoScalingRoleArn: Optional[str] = None
    ScalingPolicies: Optional[List[AutoScalingPolicyDescriptionTypeDef]] = None

class AutoScalingSettingsUpdateTypeDef(BaseModel):
    MinimumUnits: Optional[int] = None
    MaximumUnits: Optional[int] = None
    AutoScalingDisabled: Optional[bool] = None
    AutoScalingRoleArn: Optional[str] = None
    ScalingPolicyUpdate: Optional[AutoScalingPolicyUpdateTypeDef] = None

class BatchGetItemOutputServiceResourceTypeDef(BaseModel):
    Responses: Dict[str, List[Dict[str, TableAttributeValueTypeDef]]]
    UnprocessedKeys: Dict[str, KeysAndAttributesServiceResourceOutputTypeDef]
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetItemOutputTypeDef(BaseModel):
    Responses: Dict[str, List[Dict[str, AttributeValueTypeDef]]]
    UnprocessedKeys: Dict[str, KeysAndAttributesOutputTypeDef]
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteItemOutputTableTypeDef(BaseModel):
    Attributes: Dict[str, TableAttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ItemCollectionMetrics: ItemCollectionMetricsTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteItemOutputTypeDef(BaseModel):
    Attributes: Dict[str, AttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ItemCollectionMetrics: ItemCollectionMetricsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteStatementOutputTypeDef(BaseModel):
    Items: List[Dict[str, AttributeValueTypeDef]]
    ConsumedCapacity: ConsumedCapacityTypeDef
    LastEvaluatedKey: Dict[str, AttributeValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ExecuteTransactionOutputTypeDef(BaseModel):
    Responses: List[ItemResponseTypeDef]
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetItemOutputTableTypeDef(BaseModel):
    ConsumedCapacity: ConsumedCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    Item: Optional[Dict[str, TableAttributeValueTypeDef]] = None

class GetItemOutputTypeDef(BaseModel):
    ConsumedCapacity: ConsumedCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    Item: Optional[Dict[str, AttributeValueTypeDef]] = None

class PutItemOutputTableTypeDef(BaseModel):
    Attributes: Dict[str, TableAttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ItemCollectionMetrics: ItemCollectionMetricsTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutItemOutputTypeDef(BaseModel):
    Attributes: Dict[str, AttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ItemCollectionMetrics: ItemCollectionMetricsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class QueryOutputTableTypeDef(BaseModel):
    Items: List[Dict[str, TableAttributeValueTypeDef]]
    Count: int
    ScannedCount: int
    LastEvaluatedKey: Dict[str, TableAttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class QueryOutputTypeDef(BaseModel):
    Items: List[Dict[str, AttributeValueTypeDef]]
    Count: int
    ScannedCount: int
    LastEvaluatedKey: Dict[str, AttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ScanOutputTableTypeDef(BaseModel):
    Items: List[Dict[str, TableAttributeValueTypeDef]]
    Count: int
    ScannedCount: int
    LastEvaluatedKey: Dict[str, TableAttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ScanOutputTypeDef(BaseModel):
    Items: List[Dict[str, AttributeValueTypeDef]]
    Count: int
    ScannedCount: int
    LastEvaluatedKey: Dict[str, AttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TransactGetItemsOutputTypeDef(BaseModel):
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    Responses: List[ItemResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TransactWriteItemsOutputTypeDef(BaseModel):
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ItemCollectionMetrics: Dict[str, List[ItemCollectionMetricsTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateItemOutputTableTypeDef(BaseModel):
    Attributes: Dict[str, TableAttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ItemCollectionMetrics: ItemCollectionMetricsTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateItemOutputTypeDef(BaseModel):
    Attributes: Dict[str, AttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ItemCollectionMetrics: ItemCollectionMetricsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeContinuousBackupsOutputTypeDef(BaseModel):
    ContinuousBackupsDescription: ContinuousBackupsDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContinuousBackupsOutputTypeDef(BaseModel):
    ContinuousBackupsDescription: ContinuousBackupsDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TableCreationParametersTypeDef(BaseModel):
    TableName: str
    AttributeDefinitions: Sequence[AttributeDefinitionTypeDef]
    KeySchema: Sequence[KeySchemaElementTypeDef]
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None
    SSESpecification: Optional[SSESpecificationTypeDef] = None
    GlobalSecondaryIndexes: Optional[Sequence[GlobalSecondaryIndexTypeDef]] = None

class GlobalSecondaryIndexUpdateTypeDef(BaseModel):
    Update: Optional[UpdateGlobalSecondaryIndexActionTypeDef] = None
    Create: Optional[CreateGlobalSecondaryIndexActionTypeDef] = None
    Delete: Optional[DeleteGlobalSecondaryIndexActionTypeDef] = None

class ListGlobalTablesOutputTypeDef(BaseModel):
    GlobalTables: List[GlobalTableTypeDef]
    LastEvaluatedGlobalTableName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicaDescriptionTypeDef(BaseModel):
    RegionName: Optional[str] = None
    ReplicaStatus: Optional[ReplicaStatusType] = None
    ReplicaStatusDescription: Optional[str] = None
    ReplicaStatusPercentProgress: Optional[str] = None
    KMSMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverrideTypeDef] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverrideTypeDef] = None
    GlobalSecondaryIndexes: Optional[List[ReplicaGlobalSecondaryIndexDescriptionTypeDef]] = None
    ReplicaInaccessibleDateTime: Optional[datetime] = None
    ReplicaTableClassSummary: Optional[TableClassSummaryTypeDef] = None

class CreateReplicationGroupMemberActionTypeDef(BaseModel):
    RegionName: str
    KMSMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverrideTypeDef] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverrideTypeDef] = None
    GlobalSecondaryIndexes: Optional[Sequence[ReplicaGlobalSecondaryIndexTypeDef]] = None
    TableClassOverride: Optional[TableClassType] = None

class UpdateReplicationGroupMemberActionTypeDef(BaseModel):
    RegionName: str
    KMSMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverrideTypeDef] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverrideTypeDef] = None
    GlobalSecondaryIndexes: Optional[Sequence[ReplicaGlobalSecondaryIndexTypeDef]] = None
    TableClassOverride: Optional[TableClassType] = None

class UpdateGlobalTableInputRequestTypeDef(BaseModel):
    GlobalTableName: str
    ReplicaUpdates: Sequence[ReplicaUpdateTypeDef]

class DescribeExportOutputTypeDef(BaseModel):
    ExportDescription: ExportDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTableToPointInTimeOutputTypeDef(BaseModel):
    ExportDescription: ExportDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTableToPointInTimeInputRequestTypeDef(BaseModel):
    TableArn: str
    S3Bucket: str
    ExportTime: Optional[TimestampTypeDef] = None
    ClientToken: Optional[str] = None
    S3BucketOwner: Optional[str] = None
    S3Prefix: Optional[str] = None
    S3SseAlgorithm: Optional[S3SseAlgorithmType] = None
    S3SseKmsKeyId: Optional[str] = None
    ExportFormat: Optional[ExportFormatType] = None
    ExportType: Optional[ExportTypeType] = None
    IncrementalExportSpecification: Optional[IncrementalExportSpecificationTypeDef] = None

class TableCreationParametersOutputTypeDef(BaseModel):
    TableName: str
    AttributeDefinitions: List[AttributeDefinitionTypeDef]
    KeySchema: List[KeySchemaElementTypeDef]
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None
    SSESpecification: Optional[SSESpecificationTypeDef] = None
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndexOutputTypeDef]] = None

class SourceTableFeatureDetailsTypeDef(BaseModel):
    LocalSecondaryIndexes: Optional[List[LocalSecondaryIndexInfoTypeDef]] = None
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndexInfoTypeDef]] = None
    StreamDescription: Optional[StreamSpecificationTypeDef] = None
    TimeToLiveDescription: Optional[TimeToLiveDescriptionTypeDef] = None
    SSEDescription: Optional[SSEDescriptionTypeDef] = None

class ListImportsOutputTypeDef(BaseModel):
    ImportSummaryList: List[ImportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchExecuteStatementOutputTypeDef(BaseModel):
    Responses: List[BatchStatementResponseTypeDef]
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchWriteItemOutputTypeDef(BaseModel):
    UnprocessedItems: Dict[str, List[WriteRequestOutputTypeDef]]
    ItemCollectionMetrics: Dict[str, List[ItemCollectionMetricsTypeDef]]
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchExecuteStatementInputRequestTypeDef(BaseModel):
    Statements: Sequence[BatchStatementRequestTypeDef]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None

class QueryInputQueryPaginateTypeDef(BaseModel):
    TableName: str
    IndexName: Optional[str] = None
    Select: Optional[SelectType] = None
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    KeyConditions: Optional[Mapping[str, ConditionTypeDef]] = None
    QueryFilter: Optional[Mapping[str, ConditionTypeDef]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ScanIndexForward: Optional[bool] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[str] = None
    KeyConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class QueryInputRequestTypeDef(BaseModel):
    TableName: str
    IndexName: Optional[str] = None
    Select: Optional[SelectType] = None
    AttributesToGet: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    ConsistentRead: Optional[bool] = None
    KeyConditions: Optional[Mapping[str, ConditionTypeDef]] = None
    QueryFilter: Optional[Mapping[str, ConditionTypeDef]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ScanIndexForward: Optional[bool] = None
    ExclusiveStartKey: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[str] = None
    KeyConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None

class ScanInputRequestTypeDef(BaseModel):
    TableName: str
    IndexName: Optional[str] = None
    AttributesToGet: Optional[Sequence[str]] = None
    Limit: Optional[int] = None
    Select: Optional[SelectType] = None
    ScanFilter: Optional[Mapping[str, ConditionTypeDef]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ExclusiveStartKey: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    TotalSegments: Optional[int] = None
    Segment: Optional[int] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ConsistentRead: Optional[bool] = None

class ScanInputScanPaginateTypeDef(BaseModel):
    TableName: str
    IndexName: Optional[str] = None
    AttributesToGet: Optional[Sequence[str]] = None
    Select: Optional[SelectType] = None
    ScanFilter: Optional[Mapping[str, ConditionTypeDef]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    TotalSegments: Optional[int] = None
    Segment: Optional[int] = None
    ProjectionExpression: Optional[str] = None
    FilterExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ConsistentRead: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DeleteItemInputRequestTypeDef(BaseModel):
    TableName: str
    Key: Mapping[str, UniversalAttributeValueTypeDef]
    Expected: Optional[Mapping[str, ExpectedAttributeValueTypeDef]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class PutItemInputRequestTypeDef(BaseModel):
    TableName: str
    Item: Mapping[str, UniversalAttributeValueTypeDef]
    Expected: Optional[Mapping[str, ExpectedAttributeValueTypeDef]] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class UpdateItemInputRequestTypeDef(BaseModel):
    TableName: str
    Key: Mapping[str, UniversalAttributeValueTypeDef]
    AttributeUpdates: Optional[Mapping[str, AttributeValueUpdateTypeDef]] = None
    Expected: Optional[Mapping[str, ExpectedAttributeValueTypeDef]] = None
    ConditionalOperator: Optional[ConditionalOperatorType] = None
    ReturnValues: Optional[ReturnValueType] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    UpdateExpression: Optional[str] = None
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class TransactGetItemTypeDef(BaseModel):
    Get: GetTypeDef

class ExecuteTransactionInputRequestTypeDef(BaseModel):
    TransactStatements: Sequence[ParameterizedStatementTypeDef]
    ClientRequestToken: Optional[str] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None

class WriteRequestTypeDef(BaseModel):
    PutRequest: Optional[PutRequestTypeDef] = None
    DeleteRequest: Optional[DeleteRequestTypeDef] = None

class TransactWriteItemTypeDef(BaseModel):
    ConditionCheck: Optional[ConditionCheckTypeDef] = None
    Put: Optional[PutTypeDef] = None
    Delete: Optional[DeleteTypeDef] = None
    Update: Optional[UpdateTypeDef] = None

class BatchGetItemInputServiceResourceBatchGetItemTypeDef(BaseModel):
    RequestItems: Mapping[str, KeysAndAttributesServiceResourceUnionTypeDef]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None

class BatchWriteItemOutputServiceResourceTypeDef(BaseModel):
    UnprocessedItems: Dict[str, List[WriteRequestServiceResourceOutputTypeDef]]
    ItemCollectionMetrics: Dict[str, List[ItemCollectionMetricsServiceResourceTypeDef]]
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef(BaseModel):
    IndexName: Optional[str] = None
    IndexStatus: Optional[IndexStatusType] = None
    ProvisionedReadCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None
    ProvisionedWriteCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None

class ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef(BaseModel):
    IndexName: str
    IndexStatus: Optional[IndexStatusType] = None
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedReadCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None
    ProvisionedWriteCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None

class GlobalSecondaryIndexAutoScalingUpdateTypeDef(BaseModel):
    IndexName: Optional[str] = None
    ProvisionedWriteCapacityAutoScalingUpdate: Optional[AutoScalingSettingsUpdateTypeDef] = None

class GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef(BaseModel):
    IndexName: str
    ProvisionedWriteCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityAutoScalingSettingsUpdate: Optional[       AutoScalingSettingsUpdateTypeDef     ] = None

class ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef(BaseModel):
    IndexName: Optional[str] = None
    ProvisionedReadCapacityAutoScalingUpdate: Optional[AutoScalingSettingsUpdateTypeDef] = None

class ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef(BaseModel):
    IndexName: str
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedReadCapacityAutoScalingSettingsUpdate: Optional[       AutoScalingSettingsUpdateTypeDef     ] = None

class ImportTableInputRequestTypeDef(BaseModel):
    S3BucketSource: S3BucketSourceTypeDef
    InputFormat: InputFormatType
    TableCreationParameters: TableCreationParametersTypeDef
    ClientToken: Optional[str] = None
    InputFormatOptions: Optional[InputFormatOptionsTypeDef] = None
    InputCompressionType: Optional[InputCompressionTypeType] = None

class GlobalTableDescriptionTypeDef(BaseModel):
    ReplicationGroup: Optional[List[ReplicaDescriptionTypeDef]] = None
    GlobalTableArn: Optional[str] = None
    CreationDateTime: Optional[datetime] = None
    GlobalTableStatus: Optional[GlobalTableStatusType] = None
    GlobalTableName: Optional[str] = None

class TableDescriptionTypeDef(BaseModel):
    AttributeDefinitions: Optional[List[AttributeDefinitionTypeDef]] = None
    TableName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElementTypeDef]] = None
    TableStatus: Optional[TableStatusType] = None
    CreationDateTime: Optional[datetime] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputDescriptionTypeDef] = None
    TableSizeBytes: Optional[int] = None
    ItemCount: Optional[int] = None
    TableArn: Optional[str] = None
    TableId: Optional[str] = None
    BillingModeSummary: Optional[BillingModeSummaryTypeDef] = None
    LocalSecondaryIndexes: Optional[List[LocalSecondaryIndexDescriptionTypeDef]] = None
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndexDescriptionTypeDef]] = None
    StreamSpecification: Optional[StreamSpecificationTypeDef] = None
    LatestStreamLabel: Optional[str] = None
    LatestStreamArn: Optional[str] = None
    GlobalTableVersion: Optional[str] = None
    Replicas: Optional[List[ReplicaDescriptionTypeDef]] = None
    RestoreSummary: Optional[RestoreSummaryTypeDef] = None
    SSEDescription: Optional[SSEDescriptionTypeDef] = None
    ArchivalSummary: Optional[ArchivalSummaryTypeDef] = None
    TableClassSummary: Optional[TableClassSummaryTypeDef] = None
    DeletionProtectionEnabled: Optional[bool] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class ReplicationGroupUpdateTypeDef(BaseModel):
    Create: Optional[CreateReplicationGroupMemberActionTypeDef] = None
    Update: Optional[UpdateReplicationGroupMemberActionTypeDef] = None
    Delete: Optional[DeleteReplicationGroupMemberActionTypeDef] = None

class CreateTableInputRequestTypeDef(BaseModel):
    AttributeDefinitions: Sequence[AttributeDefinitionTypeDef]
    TableName: str
    KeySchema: Sequence[KeySchemaElementTypeDef]
    LocalSecondaryIndexes: Optional[Sequence[LocalSecondaryIndexTypeDef]] = None
    GlobalSecondaryIndexes: Optional[Sequence[GlobalSecondaryIndexUnionTypeDef]] = None
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    StreamSpecification: Optional[StreamSpecificationTypeDef] = None
    SSESpecification: Optional[SSESpecificationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    TableClass: Optional[TableClassType] = None
    DeletionProtectionEnabled: Optional[bool] = None
    ResourcePolicy: Optional[str] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class CreateTableInputServiceResourceCreateTableTypeDef(BaseModel):
    AttributeDefinitions: Sequence[AttributeDefinitionTypeDef]
    TableName: str
    KeySchema: Sequence[KeySchemaElementTypeDef]
    LocalSecondaryIndexes: Optional[Sequence[LocalSecondaryIndexTypeDef]] = None
    GlobalSecondaryIndexes: Optional[Sequence[GlobalSecondaryIndexUnionTypeDef]] = None
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    StreamSpecification: Optional[StreamSpecificationTypeDef] = None
    SSESpecification: Optional[SSESpecificationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    TableClass: Optional[TableClassType] = None
    DeletionProtectionEnabled: Optional[bool] = None
    ResourcePolicy: Optional[str] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class RestoreTableFromBackupInputRequestTypeDef(BaseModel):
    TargetTableName: str
    BackupArn: str
    BillingModeOverride: Optional[BillingModeType] = None
    GlobalSecondaryIndexOverride: Optional[Sequence[GlobalSecondaryIndexUnionTypeDef]] = None
    LocalSecondaryIndexOverride: Optional[Sequence[LocalSecondaryIndexTypeDef]] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputTypeDef] = None
    SSESpecificationOverride: Optional[SSESpecificationTypeDef] = None

class RestoreTableToPointInTimeInputRequestTypeDef(BaseModel):
    TargetTableName: str
    SourceTableArn: Optional[str] = None
    SourceTableName: Optional[str] = None
    UseLatestRestorableTime: Optional[bool] = None
    RestoreDateTime: Optional[TimestampTypeDef] = None
    BillingModeOverride: Optional[BillingModeType] = None
    GlobalSecondaryIndexOverride: Optional[Sequence[GlobalSecondaryIndexUnionTypeDef]] = None
    LocalSecondaryIndexOverride: Optional[Sequence[LocalSecondaryIndexTypeDef]] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputTypeDef] = None
    SSESpecificationOverride: Optional[SSESpecificationTypeDef] = None

class ImportTableDescriptionTypeDef(BaseModel):
    ImportArn: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    TableArn: Optional[str] = None
    TableId: Optional[str] = None
    ClientToken: Optional[str] = None
    S3BucketSource: Optional[S3BucketSourceTypeDef] = None
    ErrorCount: Optional[int] = None
    CloudWatchLogGroupArn: Optional[str] = None
    InputFormat: Optional[InputFormatType] = None
    InputFormatOptions: Optional[InputFormatOptionsOutputTypeDef] = None
    InputCompressionType: Optional[InputCompressionTypeType] = None
    TableCreationParameters: Optional[TableCreationParametersOutputTypeDef] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None
    ProcessedSizeBytes: Optional[int] = None
    ProcessedItemCount: Optional[int] = None
    ImportedItemCount: Optional[int] = None
    FailureCode: Optional[str] = None
    FailureMessage: Optional[str] = None

class BackupDescriptionTypeDef(BaseModel):
    BackupDetails: Optional[BackupDetailsTypeDef] = None
    SourceTableDetails: Optional[SourceTableDetailsTypeDef] = None
    SourceTableFeatureDetails: Optional[SourceTableFeatureDetailsTypeDef] = None

class TransactGetItemsInputRequestTypeDef(BaseModel):
    TransactItems: Sequence[TransactGetItemTypeDef]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None

class BatchGetItemInputRequestTypeDef(BaseModel):
    RequestItems: Mapping[str, KeysAndAttributesUnionTypeDef]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None

class TransactWriteItemsInputRequestTypeDef(BaseModel):
    TransactItems: Sequence[TransactWriteItemTypeDef]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ClientRequestToken: Optional[str] = None

class BatchWriteItemInputServiceResourceBatchWriteItemTypeDef(BaseModel):
    RequestItems: Mapping[str, Sequence[WriteRequestServiceResourceUnionTypeDef]]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None

class ReplicaAutoScalingDescriptionTypeDef(BaseModel):
    RegionName: Optional[str] = None
    GlobalSecondaryIndexes: Optional[       List[ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef]     ] = None
    ReplicaProvisionedReadCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None
    ReplicaProvisionedWriteCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None
    ReplicaStatus: Optional[ReplicaStatusType] = None

class ReplicaSettingsDescriptionTypeDef(BaseModel):
    RegionName: str
    ReplicaStatus: Optional[ReplicaStatusType] = None
    ReplicaBillingModeSummary: Optional[BillingModeSummaryTypeDef] = None
    ReplicaProvisionedReadCapacityUnits: Optional[int] = None
    ReplicaProvisionedReadCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None
    ReplicaProvisionedWriteCapacityUnits: Optional[int] = None
    ReplicaProvisionedWriteCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None
    ReplicaGlobalSecondaryIndexSettings: Optional[       List[ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef]     ] = None
    ReplicaTableClassSummary: Optional[TableClassSummaryTypeDef] = None

class ReplicaAutoScalingUpdateTypeDef(BaseModel):
    RegionName: str
    ReplicaGlobalSecondaryIndexUpdates: Optional[       Sequence[ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef]     ] = None
    ReplicaProvisionedReadCapacityAutoScalingUpdate: Optional[       AutoScalingSettingsUpdateTypeDef     ] = None

class ReplicaSettingsUpdateTypeDef(BaseModel):
    RegionName: str
    ReplicaProvisionedReadCapacityUnits: Optional[int] = None
    ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate: Optional[       AutoScalingSettingsUpdateTypeDef     ] = None
    ReplicaGlobalSecondaryIndexSettingsUpdate: Optional[       Sequence[ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef]     ] = None
    ReplicaTableClass: Optional[TableClassType] = None

class CreateGlobalTableOutputTypeDef(BaseModel):
    GlobalTableDescription: GlobalTableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGlobalTableOutputTypeDef(BaseModel):
    GlobalTableDescription: GlobalTableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGlobalTableOutputTypeDef(BaseModel):
    GlobalTableDescription: GlobalTableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTableOutputTypeDef(BaseModel):
    TableDescription: TableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTableOutputTypeDef(BaseModel):
    TableDescription: TableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTableOutputTypeDef(BaseModel):
    Table: TableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTableFromBackupOutputTypeDef(BaseModel):
    TableDescription: TableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTableToPointInTimeOutputTypeDef(BaseModel):
    TableDescription: TableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableOutputTypeDef(BaseModel):
    TableDescription: TableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableInputRequestTypeDef(BaseModel):
    TableName: str
    AttributeDefinitions: Optional[Sequence[AttributeDefinitionTypeDef]] = None
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    GlobalSecondaryIndexUpdates: Optional[Sequence[GlobalSecondaryIndexUpdateTypeDef]] = None
    StreamSpecification: Optional[StreamSpecificationTypeDef] = None
    SSESpecification: Optional[SSESpecificationTypeDef] = None
    ReplicaUpdates: Optional[Sequence[ReplicationGroupUpdateTypeDef]] = None
    TableClass: Optional[TableClassType] = None
    DeletionProtectionEnabled: Optional[bool] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class UpdateTableInputTableUpdateTypeDef(BaseModel):
    AttributeDefinitions: Optional[Sequence[AttributeDefinitionTypeDef]] = None
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    GlobalSecondaryIndexUpdates: Optional[Sequence[GlobalSecondaryIndexUpdateTypeDef]] = None
    StreamSpecification: Optional[StreamSpecificationTypeDef] = None
    SSESpecification: Optional[SSESpecificationTypeDef] = None
    ReplicaUpdates: Optional[Sequence[ReplicationGroupUpdateTypeDef]] = None
    TableClass: Optional[TableClassType] = None
    DeletionProtectionEnabled: Optional[bool] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class DescribeImportOutputTypeDef(BaseModel):
    ImportTableDescription: ImportTableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportTableOutputTypeDef(BaseModel):
    ImportTableDescription: ImportTableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackupOutputTypeDef(BaseModel):
    BackupDescription: BackupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupOutputTypeDef(BaseModel):
    BackupDescription: BackupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchWriteItemInputRequestTypeDef(BaseModel):
    RequestItems: Mapping[str, Sequence[WriteRequestUnionTypeDef]]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None

class TableAutoScalingDescriptionTypeDef(BaseModel):
    TableName: Optional[str] = None
    TableStatus: Optional[TableStatusType] = None
    Replicas: Optional[List[ReplicaAutoScalingDescriptionTypeDef]] = None

class DescribeGlobalTableSettingsOutputTypeDef(BaseModel):
    GlobalTableName: str
    ReplicaSettings: List[ReplicaSettingsDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGlobalTableSettingsOutputTypeDef(BaseModel):
    GlobalTableName: str
    ReplicaSettings: List[ReplicaSettingsDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableReplicaAutoScalingInputRequestTypeDef(BaseModel):
    TableName: str
    GlobalSecondaryIndexUpdates: Optional[       Sequence[GlobalSecondaryIndexAutoScalingUpdateTypeDef]     ] = None
    ProvisionedWriteCapacityAutoScalingUpdate: Optional[AutoScalingSettingsUpdateTypeDef] = None
    ReplicaUpdates: Optional[Sequence[ReplicaAutoScalingUpdateTypeDef]] = None

class UpdateGlobalTableSettingsInputRequestTypeDef(BaseModel):
    GlobalTableName: str
    GlobalTableBillingMode: Optional[BillingModeType] = None
    GlobalTableProvisionedWriteCapacityUnits: Optional[int] = None
    GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: Optional[       AutoScalingSettingsUpdateTypeDef     ] = None
    GlobalTableGlobalSecondaryIndexSettingsUpdate: Optional[       Sequence[GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef]     ] = None
    ReplicaSettingsUpdate: Optional[Sequence[ReplicaSettingsUpdateTypeDef]] = None

class DescribeTableReplicaAutoScalingOutputTypeDef(BaseModel):
    TableAutoScalingDescription: TableAutoScalingDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableReplicaAutoScalingOutputTypeDef(BaseModel):
    TableAutoScalingDescription: TableAutoScalingDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

