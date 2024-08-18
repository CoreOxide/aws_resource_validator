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
from aws_resource_validator.pydantic_models.dynamodb_constants import *

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ArchivalSummaryTypeDef(BaseValidatorModel):
    ArchivalDateTime: Optional[datetime] = None
    ArchivalReason: Optional[str] = None
    ArchivalBackupArn: Optional[str] = None

class AttributeDefinitionTypeDef(BaseValidatorModel):
    AttributeName: str
    AttributeType: ScalarAttributeTypeType

class AttributeValueTypeDef(BaseValidatorModel):
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

class AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef(BaseValidatorModel):
    TargetValue: float
    DisableScaleIn: Optional[bool] = None
    ScaleInCooldown: Optional[int] = None
    ScaleOutCooldown: Optional[int] = None

class AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef(BaseValidatorModel):
    TargetValue: float
    DisableScaleIn: Optional[bool] = None
    ScaleInCooldown: Optional[int] = None
    ScaleOutCooldown: Optional[int] = None

class BackupDetailsTypeDef(BaseValidatorModel):
    BackupArn: str
    BackupName: str
    BackupStatus: BackupStatusType
    BackupType: BackupTypeType
    BackupCreationDateTime: datetime
    BackupSizeBytes: Optional[int] = None
    BackupExpiryDateTime: Optional[datetime] = None

class BackupSummaryTypeDef(BaseValidatorModel):
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

class BillingModeSummaryTypeDef(BaseValidatorModel):
    BillingMode: Optional[BillingModeType] = None
    LastUpdateToPayPerRequestDateTime: Optional[datetime] = None

class CapacityTypeDef(BaseValidatorModel):
    ReadCapacityUnits: Optional[float] = None
    WriteCapacityUnits: Optional[float] = None
    CapacityUnits: Optional[float] = None

class PointInTimeRecoveryDescriptionTypeDef(BaseValidatorModel):
    PointInTimeRecoveryStatus: Optional[PointInTimeRecoveryStatusType] = None
    EarliestRestorableDateTime: Optional[datetime] = None
    LatestRestorableDateTime: Optional[datetime] = None

class ContributorInsightsSummaryTypeDef(BaseValidatorModel):
    TableName: Optional[str] = None
    IndexName: Optional[str] = None
    ContributorInsightsStatus: Optional[ContributorInsightsStatusType] = None

class CreateBackupInputRequestTypeDef(BaseValidatorModel):
    TableName: str
    BackupName: str

class KeySchemaElementTypeDef(BaseValidatorModel):
    AttributeName: str
    KeyType: KeyTypeType

class OnDemandThroughputTypeDef(BaseValidatorModel):
    MaxReadRequestUnits: Optional[int] = None
    MaxWriteRequestUnits: Optional[int] = None

class ProjectionTypeDef(BaseValidatorModel):
    ProjectionType: Optional[ProjectionTypeType] = None
    NonKeyAttributes: Optional[Sequence[str]] = None

class ProvisionedThroughputTypeDef(BaseValidatorModel):
    ReadCapacityUnits: int
    WriteCapacityUnits: int

class ReplicaTypeDef(BaseValidatorModel):
    RegionName: Optional[str] = None

class CreateReplicaActionTypeDef(BaseValidatorModel):
    RegionName: str

class OnDemandThroughputOverrideTypeDef(BaseValidatorModel):
    MaxReadRequestUnits: Optional[int] = None

class ProvisionedThroughputOverrideTypeDef(BaseValidatorModel):
    ReadCapacityUnits: Optional[int] = None

class SSESpecificationTypeDef(BaseValidatorModel):
    Enabled: Optional[bool] = None
    SSEType: Optional[SSETypeType] = None
    KMSMasterKeyId: Optional[str] = None

class StreamSpecificationTypeDef(BaseValidatorModel):
    StreamEnabled: bool
    StreamViewType: Optional[StreamViewTypeType] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class CsvOptionsOutputTypeDef(BaseValidatorModel):
    Delimiter: Optional[str] = None
    HeaderList: Optional[List[str]] = None

class CsvOptionsTypeDef(BaseValidatorModel):
    Delimiter: Optional[str] = None
    HeaderList: Optional[Sequence[str]] = None

class DeleteBackupInputRequestTypeDef(BaseValidatorModel):
    BackupArn: str

class DeleteGlobalSecondaryIndexActionTypeDef(BaseValidatorModel):
    IndexName: str

class DeleteReplicaActionTypeDef(BaseValidatorModel):
    RegionName: str

class DeleteReplicationGroupMemberActionTypeDef(BaseValidatorModel):
    RegionName: str

class DeleteResourcePolicyInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    ExpectedRevisionId: Optional[str] = None

class DeleteTableInputRequestTypeDef(BaseValidatorModel):
    TableName: str

class DescribeBackupInputRequestTypeDef(BaseValidatorModel):
    BackupArn: str

class DescribeContinuousBackupsInputRequestTypeDef(BaseValidatorModel):
    TableName: str

class DescribeContributorInsightsInputRequestTypeDef(BaseValidatorModel):
    TableName: str
    IndexName: Optional[str] = None

class FailureExceptionTypeDef(BaseValidatorModel):
    ExceptionName: Optional[str] = None
    ExceptionDescription: Optional[str] = None

class EndpointTypeDef(BaseValidatorModel):
    Address: str
    CachePeriodInMinutes: int

class DescribeExportInputRequestTypeDef(BaseValidatorModel):
    ExportArn: str

class DescribeGlobalTableInputRequestTypeDef(BaseValidatorModel):
    GlobalTableName: str

class DescribeGlobalTableSettingsInputRequestTypeDef(BaseValidatorModel):
    GlobalTableName: str

class DescribeImportInputRequestTypeDef(BaseValidatorModel):
    ImportArn: str

class DescribeKinesisStreamingDestinationInputRequestTypeDef(BaseValidatorModel):
    TableName: str

class KinesisDataStreamDestinationTypeDef(BaseValidatorModel):
    StreamArn: Optional[str] = None
    DestinationStatus: Optional[DestinationStatusType] = None
    DestinationStatusDescription: Optional[str] = None
    ApproximateCreationDateTimePrecision: Optional[       ApproximateCreationDateTimePrecisionType     ] = None

class DescribeTableInputRequestTypeDef(BaseValidatorModel):
    TableName: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeTableReplicaAutoScalingInputRequestTypeDef(BaseValidatorModel):
    TableName: str

class DescribeTimeToLiveInputRequestTypeDef(BaseValidatorModel):
    TableName: str

class TimeToLiveDescriptionTypeDef(BaseValidatorModel):
    TimeToLiveStatus: Optional[TimeToLiveStatusType] = None
    AttributeName: Optional[str] = None

class EnableKinesisStreamingConfigurationTypeDef(BaseValidatorModel):
    ApproximateCreationDateTimePrecision: Optional[       ApproximateCreationDateTimePrecisionType     ] = None

class IncrementalExportSpecificationOutputTypeDef(BaseValidatorModel):
    ExportFromTime: Optional[datetime] = None
    ExportToTime: Optional[datetime] = None
    ExportViewType: Optional[ExportViewTypeType] = None

class ExportSummaryTypeDef(BaseValidatorModel):
    ExportArn: Optional[str] = None
    ExportStatus: Optional[ExportStatusType] = None
    ExportType: Optional[ExportTypeType] = None

class GetResourcePolicyInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ProjectionExtraOutputTypeDef(BaseValidatorModel):
    ProjectionType: Optional[ProjectionTypeType] = None
    NonKeyAttributes: Optional[List[str]] = None

class ProvisionedThroughputDescriptionTypeDef(BaseValidatorModel):
    LastIncreaseDateTime: Optional[datetime] = None
    LastDecreaseDateTime: Optional[datetime] = None
    NumberOfDecreasesToday: Optional[int] = None
    ReadCapacityUnits: Optional[int] = None
    WriteCapacityUnits: Optional[int] = None

class ProjectionOutputTypeDef(BaseValidatorModel):
    ProjectionType: Optional[ProjectionTypeType] = None
    NonKeyAttributes: Optional[List[str]] = None

class S3BucketSourceTypeDef(BaseValidatorModel):
    S3Bucket: str
    S3BucketOwner: Optional[str] = None
    S3KeyPrefix: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListContributorInsightsInputRequestTypeDef(BaseValidatorModel):
    TableName: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListExportsInputRequestTypeDef(BaseValidatorModel):
    TableArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListGlobalTablesInputRequestTypeDef(BaseValidatorModel):
    ExclusiveStartGlobalTableName: Optional[str] = None
    Limit: Optional[int] = None
    RegionName: Optional[str] = None

class ListImportsInputRequestTypeDef(BaseValidatorModel):
    TableArn: Optional[str] = None
    PageSize: Optional[int] = None
    NextToken: Optional[str] = None

class ListTablesInputRequestTypeDef(BaseValidatorModel):
    ExclusiveStartTableName: Optional[str] = None
    Limit: Optional[int] = None

class ListTagsOfResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    NextToken: Optional[str] = None

class PointInTimeRecoverySpecificationTypeDef(BaseValidatorModel):
    PointInTimeRecoveryEnabled: bool

class PutResourcePolicyInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Policy: str
    ExpectedRevisionId: Optional[str] = None
    ConfirmRemoveSelfResourceAccess: Optional[bool] = None

class TableClassSummaryTypeDef(BaseValidatorModel):
    TableClass: Optional[TableClassType] = None
    LastUpdateDateTime: Optional[datetime] = None

class RestoreSummaryTypeDef(BaseValidatorModel):
    RestoreDateTime: datetime
    RestoreInProgress: bool
    SourceBackupArn: Optional[str] = None
    SourceTableArn: Optional[str] = None

class SSEDescriptionTypeDef(BaseValidatorModel):
    Status: Optional[SSEStatusType] = None
    SSEType: Optional[SSETypeType] = None
    KMSMasterKeyArn: Optional[str] = None
    InaccessibleEncryptionDateTime: Optional[datetime] = None

class TableBatchWriterRequestTypeDef(BaseValidatorModel):
    overwrite_by_pkeys: Optional[List[str]] = None

class TimeToLiveSpecificationTypeDef(BaseValidatorModel):
    Enabled: bool
    AttributeName: str

class UntagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateContributorInsightsInputRequestTypeDef(BaseValidatorModel):
    TableName: str
    ContributorInsightsAction: ContributorInsightsActionType
    IndexName: Optional[str] = None

class UpdateKinesisStreamingConfigurationTypeDef(BaseValidatorModel):
    ApproximateCreationDateTimePrecision: Optional[       ApproximateCreationDateTimePrecisionType     ] = None

class ArchivalSummaryResponseTypeDef(BaseValidatorModel):
    ArchivalDateTime: datetime
    ArchivalReason: str
    ArchivalBackupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class BillingModeSummaryResponseTypeDef(BaseValidatorModel):
    BillingMode: BillingModeType
    LastUpdateToPayPerRequestDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteResourcePolicyOutputTypeDef(BaseValidatorModel):
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeLimitsOutputTypeDef(BaseValidatorModel):
    AccountMaxReadCapacityUnits: int
    AccountMaxWriteCapacityUnits: int
    TableMaxReadCapacityUnits: int
    TableMaxWriteCapacityUnits: int
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetResourcePolicyOutputTypeDef(BaseValidatorModel):
    Policy: str
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTablesOutputTypeDef(BaseValidatorModel):
    TableNames: List[str]
    LastEvaluatedTableName: str
    ResponseMetadata: ResponseMetadataTypeDef

class OnDemandThroughputResponseTypeDef(BaseValidatorModel):
    MaxReadRequestUnits: int
    MaxWriteRequestUnits: int
    ResponseMetadata: ResponseMetadataTypeDef

class ProvisionedThroughputDescriptionResponseTypeDef(BaseValidatorModel):
    LastIncreaseDateTime: datetime
    LastDecreaseDateTime: datetime
    NumberOfDecreasesToday: int
    ReadCapacityUnits: int
    WriteCapacityUnits: int
    ResponseMetadata: ResponseMetadataTypeDef

class PutResourcePolicyOutputTypeDef(BaseValidatorModel):
    RevisionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreSummaryResponseTypeDef(BaseValidatorModel):
    SourceBackupArn: str
    SourceTableArn: str
    RestoreDateTime: datetime
    RestoreInProgress: bool
    ResponseMetadata: ResponseMetadataTypeDef

class SSEDescriptionResponseTypeDef(BaseValidatorModel):
    Status: SSEStatusType
    SSEType: SSETypeType
    KMSMasterKeyArn: str
    InaccessibleEncryptionDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class StreamSpecificationResponseTypeDef(BaseValidatorModel):
    StreamEnabled: bool
    StreamViewType: StreamViewTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class TableClassSummaryResponseTypeDef(BaseValidatorModel):
    TableClass: TableClassType
    LastUpdateDateTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContributorInsightsOutputTypeDef(BaseValidatorModel):
    TableName: str
    IndexName: str
    ContributorInsightsStatus: ContributorInsightsStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class BatchStatementErrorTypeDef(BaseValidatorModel):
    Code: Optional[BatchStatementErrorCodeEnumType] = None
    Message: Optional[str] = None
    Item: Optional[Dict[str, AttributeValueTypeDef]] = None

class DeleteRequestOutputTypeDef(BaseValidatorModel):
    Key: Dict[str, AttributeValueTypeDef]

class ItemCollectionMetricsTypeDef(BaseValidatorModel):
    ItemCollectionKey: Optional[Dict[str, AttributeValueTypeDef]] = None
    SizeEstimateRangeGB: Optional[List[float]] = None

class ItemResponseTypeDef(BaseValidatorModel):
    Item: Optional[Dict[str, AttributeValueTypeDef]] = None

class KeysAndAttributesOutputTypeDef(BaseValidatorModel):
    Keys: List[Dict[str, AttributeValueTypeDef]]
    AttributesToGet: Optional[List[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None

class PutRequestOutputTypeDef(BaseValidatorModel):
    Item: Dict[str, AttributeValueTypeDef]

class AttributeValueUpdateTableTypeDef(BaseValidatorModel):
    Value: Optional[TableAttributeValueTypeDef] = None
    Action: Optional[AttributeActionType] = None

class ConditionTableTypeDef(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    AttributeValueList: Optional[Sequence[TableAttributeValueTypeDef]] = None

class DeleteRequestServiceResourceOutputTypeDef(BaseValidatorModel):
    Key: Dict[str, TableAttributeValueTypeDef]

class DeleteRequestServiceResourceTypeDef(BaseValidatorModel):
    Key: Mapping[str, TableAttributeValueTypeDef]

class ExpectedAttributeValueTableTypeDef(BaseValidatorModel):
    Value: Optional[TableAttributeValueTypeDef] = None
    Exists: Optional[bool] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    AttributeValueList: Optional[Sequence[TableAttributeValueTypeDef]] = None

class GetItemInputTableGetItemTypeDef(BaseValidatorModel):
    Key: Mapping[str, TableAttributeValueTypeDef]
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None

class ItemCollectionMetricsServiceResourceTypeDef(BaseValidatorModel):
    ItemCollectionKey: Optional[Dict[str, TableAttributeValueTypeDef]] = None
    SizeEstimateRangeGB: Optional[List[float]] = None

class ItemCollectionMetricsTableTypeDef(BaseValidatorModel):
    ItemCollectionKey: Optional[Dict[str, TableAttributeValueTypeDef]] = None
    SizeEstimateRangeGB: Optional[List[float]] = None

class KeysAndAttributesServiceResourceOutputTypeDef(BaseValidatorModel):
    Keys: List[Dict[str, TableAttributeValueTypeDef]]
    AttributesToGet: Optional[List[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Dict[str, str]] = None

class KeysAndAttributesServiceResourceTypeDef(BaseValidatorModel):
    Keys: Sequence[Mapping[str, TableAttributeValueTypeDef]]
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None

class PutRequestServiceResourceOutputTypeDef(BaseValidatorModel):
    Item: Dict[str, TableAttributeValueTypeDef]

class PutRequestServiceResourceTypeDef(BaseValidatorModel):
    Item: Mapping[str, TableAttributeValueTypeDef]

class AutoScalingPolicyDescriptionTypeDef(BaseValidatorModel):
    PolicyName: Optional[str] = None
    TargetTrackingScalingPolicyConfiguration: Optional[       AutoScalingTargetTrackingScalingPolicyConfigurationDescriptionTypeDef     ] = None

class AutoScalingPolicyUpdateTypeDef(BaseValidatorModel):
    TargetTrackingScalingPolicyConfiguration: AutoScalingTargetTrackingScalingPolicyConfigurationUpdateTypeDef
    PolicyName: Optional[str] = None

class CreateBackupOutputTypeDef(BaseValidatorModel):
    BackupDetails: BackupDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBackupsOutputTypeDef(BaseValidatorModel):
    BackupSummaries: List[BackupSummaryTypeDef]
    LastEvaluatedBackupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ConsumedCapacityTypeDef(BaseValidatorModel):
    TableName: Optional[str] = None
    CapacityUnits: Optional[float] = None
    ReadCapacityUnits: Optional[float] = None
    WriteCapacityUnits: Optional[float] = None
    Table: Optional[CapacityTypeDef] = None
    LocalSecondaryIndexes: Optional[Dict[str, CapacityTypeDef]] = None
    GlobalSecondaryIndexes: Optional[Dict[str, CapacityTypeDef]] = None

class ContinuousBackupsDescriptionTypeDef(BaseValidatorModel):
    ContinuousBackupsStatus: ContinuousBackupsStatusType
    PointInTimeRecoveryDescription: Optional[PointInTimeRecoveryDescriptionTypeDef] = None

class ListContributorInsightsOutputTypeDef(BaseValidatorModel):
    ContributorInsightsSummaries: List[ContributorInsightsSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LocalSecondaryIndexTypeDef(BaseValidatorModel):
    IndexName: str
    KeySchema: Sequence[KeySchemaElementTypeDef]
    Projection: ProjectionTypeDef

class CreateGlobalSecondaryIndexActionTypeDef(BaseValidatorModel):
    IndexName: str
    KeySchema: Sequence[KeySchemaElementTypeDef]
    Projection: ProjectionTypeDef
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class GlobalSecondaryIndexTypeDef(BaseValidatorModel):
    IndexName: str
    KeySchema: Sequence[KeySchemaElementTypeDef]
    Projection: ProjectionTypeDef
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class SourceTableDetailsTypeDef(BaseValidatorModel):
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

class UpdateGlobalSecondaryIndexActionTypeDef(BaseValidatorModel):
    IndexName: str
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class CreateGlobalTableInputRequestTypeDef(BaseValidatorModel):
    GlobalTableName: str
    ReplicationGroup: Sequence[ReplicaTypeDef]

class GlobalTableTypeDef(BaseValidatorModel):
    GlobalTableName: Optional[str] = None
    ReplicationGroup: Optional[List[ReplicaTypeDef]] = None

class ReplicaGlobalSecondaryIndexDescriptionTypeDef(BaseValidatorModel):
    IndexName: Optional[str] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverrideTypeDef] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverrideTypeDef] = None

class ReplicaGlobalSecondaryIndexTypeDef(BaseValidatorModel):
    IndexName: str
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverrideTypeDef] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverrideTypeDef] = None

class ListTagsOfResourceOutputTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class TagResourceInputRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class InputFormatOptionsOutputTypeDef(BaseValidatorModel):
    Csv: Optional[CsvOptionsOutputTypeDef] = None

class InputFormatOptionsTypeDef(BaseValidatorModel):
    Csv: Optional[CsvOptionsTypeDef] = None

class ReplicaUpdateTypeDef(BaseValidatorModel):
    Create: Optional[CreateReplicaActionTypeDef] = None
    Delete: Optional[DeleteReplicaActionTypeDef] = None

class DescribeContributorInsightsOutputTypeDef(BaseValidatorModel):
    TableName: str
    IndexName: str
    ContributorInsightsRuleList: List[str]
    ContributorInsightsStatus: ContributorInsightsStatusType
    LastUpdateDateTime: datetime
    FailureException: FailureExceptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEndpointsResponseTypeDef(BaseValidatorModel):
    Endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeKinesisStreamingDestinationOutputTypeDef(BaseValidatorModel):
    TableName: str
    KinesisDataStreamDestinations: List[KinesisDataStreamDestinationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTableInputTableExistsWaitTypeDef(BaseValidatorModel):
    TableName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTableInputTableNotExistsWaitTypeDef(BaseValidatorModel):
    TableName: str
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTimeToLiveOutputTypeDef(BaseValidatorModel):
    TimeToLiveDescription: TimeToLiveDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class KinesisStreamingDestinationInputRequestTypeDef(BaseValidatorModel):
    TableName: str
    StreamArn: str
    EnableKinesisStreamingConfiguration: Optional[       EnableKinesisStreamingConfigurationTypeDef     ] = None

class KinesisStreamingDestinationOutputTypeDef(BaseValidatorModel):
    TableName: str
    StreamArn: str
    DestinationStatus: DestinationStatusType
    EnableKinesisStreamingConfiguration: EnableKinesisStreamingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportDescriptionTypeDef(BaseValidatorModel):
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

class ListExportsOutputTypeDef(BaseValidatorModel):
    ExportSummaries: List[ExportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class IncrementalExportSpecificationTypeDef(BaseValidatorModel):
    ExportFromTime: Optional[TimestampTypeDef] = None
    ExportToTime: Optional[TimestampTypeDef] = None
    ExportViewType: Optional[ExportViewTypeType] = None

class ListBackupsInputRequestTypeDef(BaseValidatorModel):
    TableName: Optional[str] = None
    Limit: Optional[int] = None
    TimeRangeLowerBound: Optional[TimestampTypeDef] = None
    TimeRangeUpperBound: Optional[TimestampTypeDef] = None
    ExclusiveStartBackupArn: Optional[str] = None
    BackupType: Optional[BackupTypeFilterType] = None

class LocalSecondaryIndexDescriptionTypeDef(BaseValidatorModel):
    IndexName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElementTypeDef]] = None
    Projection: Optional[ProjectionExtraOutputTypeDef] = None
    IndexSizeBytes: Optional[int] = None
    ItemCount: Optional[int] = None
    IndexArn: Optional[str] = None

class GlobalSecondaryIndexDescriptionTypeDef(BaseValidatorModel):
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

class GlobalSecondaryIndexInfoTypeDef(BaseValidatorModel):
    IndexName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElementTypeDef]] = None
    Projection: Optional[ProjectionOutputTypeDef] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class GlobalSecondaryIndexOutputTypeDef(BaseValidatorModel):
    IndexName: str
    KeySchema: List[KeySchemaElementTypeDef]
    Projection: ProjectionOutputTypeDef
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None

class LocalSecondaryIndexInfoTypeDef(BaseValidatorModel):
    IndexName: Optional[str] = None
    KeySchema: Optional[List[KeySchemaElementTypeDef]] = None
    Projection: Optional[ProjectionOutputTypeDef] = None

class ImportSummaryTypeDef(BaseValidatorModel):
    ImportArn: Optional[str] = None
    ImportStatus: Optional[ImportStatusType] = None
    TableArn: Optional[str] = None
    S3BucketSource: Optional[S3BucketSourceTypeDef] = None
    CloudWatchLogGroupArn: Optional[str] = None
    InputFormat: Optional[InputFormatType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class ListBackupsInputListBackupsPaginateTypeDef(BaseValidatorModel):
    TableName: Optional[str] = None
    TimeRangeLowerBound: Optional[TimestampTypeDef] = None
    TimeRangeUpperBound: Optional[TimestampTypeDef] = None
    BackupType: Optional[BackupTypeFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTablesInputListTablesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsOfResourceInputListTagsOfResourcePaginateTypeDef(BaseValidatorModel):
    ResourceArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class UpdateContinuousBackupsInputRequestTypeDef(BaseValidatorModel):
    TableName: str
    PointInTimeRecoverySpecification: PointInTimeRecoverySpecificationTypeDef

class UpdateTimeToLiveInputRequestTypeDef(BaseValidatorModel):
    TableName: str
    TimeToLiveSpecification: TimeToLiveSpecificationTypeDef

class UpdateTimeToLiveOutputTypeDef(BaseValidatorModel):
    TimeToLiveSpecification: TimeToLiveSpecificationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKinesisStreamingDestinationInputRequestTypeDef(BaseValidatorModel):
    TableName: str
    StreamArn: str
    UpdateKinesisStreamingConfiguration: Optional[       UpdateKinesisStreamingConfigurationTypeDef     ] = None

class UpdateKinesisStreamingDestinationOutputTypeDef(BaseValidatorModel):
    TableName: str
    StreamArn: str
    DestinationStatus: DestinationStatusType
    UpdateKinesisStreamingConfiguration: UpdateKinesisStreamingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchStatementResponseTypeDef(BaseValidatorModel):
    Error: Optional[BatchStatementErrorTypeDef] = None
    TableName: Optional[str] = None
    Item: Optional[Dict[str, AttributeValueTypeDef]] = None

class WriteRequestOutputTypeDef(BaseValidatorModel):
    PutRequest: Optional[PutRequestOutputTypeDef] = None
    DeleteRequest: Optional[DeleteRequestOutputTypeDef] = None

class AttributeValueUpdateTypeDef(BaseValidatorModel):
    Value: Optional[UniversalAttributeValueTypeDef] = None
    Action: Optional[AttributeActionType] = None

class BatchStatementRequestTypeDef(BaseValidatorModel):
    Statement: str
    Parameters: Optional[Sequence[UniversalAttributeValueTypeDef]] = None
    ConsistentRead: Optional[bool] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class ConditionCheckTypeDef(BaseValidatorModel):
    Key: Mapping[str, UniversalAttributeValueTypeDef]
    TableName: str
    ConditionExpression: str
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class ConditionTypeDef(BaseValidatorModel):
    ComparisonOperator: ComparisonOperatorType
    AttributeValueList: Optional[Sequence[UniversalAttributeValueTypeDef]] = None

class DeleteRequestTypeDef(BaseValidatorModel):
    Key: Mapping[str, UniversalAttributeValueTypeDef]

class DeleteTypeDef(BaseValidatorModel):
    Key: Mapping[str, UniversalAttributeValueTypeDef]
    TableName: str
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class ExecuteStatementInputRequestTypeDef(BaseValidatorModel):
    Statement: str
    Parameters: Optional[Sequence[UniversalAttributeValueTypeDef]] = None
    ConsistentRead: Optional[bool] = None
    NextToken: Optional[str] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    Limit: Optional[int] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class ExpectedAttributeValueTypeDef(BaseValidatorModel):
    Value: Optional[UniversalAttributeValueTypeDef] = None
    Exists: Optional[bool] = None
    ComparisonOperator: Optional[ComparisonOperatorType] = None
    AttributeValueList: Optional[Sequence[UniversalAttributeValueTypeDef]] = None

class GetItemInputRequestTypeDef(BaseValidatorModel):
    TableName: str
    Key: Mapping[str, UniversalAttributeValueTypeDef]
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None

class GetTypeDef(BaseValidatorModel):
    Key: Mapping[str, UniversalAttributeValueTypeDef]
    TableName: str
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None

class KeysAndAttributesTypeDef(BaseValidatorModel):
    Keys: Sequence[Mapping[str, UniversalAttributeValueTypeDef]]
    AttributesToGet: Optional[Sequence[str]] = None
    ConsistentRead: Optional[bool] = None
    ProjectionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None

class ParameterizedStatementTypeDef(BaseValidatorModel):
    Statement: str
    Parameters: Optional[Sequence[UniversalAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class PutRequestTypeDef(BaseValidatorModel):
    Item: Mapping[str, UniversalAttributeValueTypeDef]

class PutTypeDef(BaseValidatorModel):
    Item: Mapping[str, UniversalAttributeValueTypeDef]
    TableName: str
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class UpdateTypeDef(BaseValidatorModel):
    Key: Mapping[str, UniversalAttributeValueTypeDef]
    UpdateExpression: str
    TableName: str
    ConditionExpression: Optional[str] = None
    ExpressionAttributeNames: Optional[Mapping[str, str]] = None
    ExpressionAttributeValues: Optional[Mapping[str, UniversalAttributeValueTypeDef]] = None
    ReturnValuesOnConditionCheckFailure: Optional[ReturnValuesOnConditionCheckFailureType] = None

class QueryInputTableQueryTypeDef(BaseValidatorModel):
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

class ScanInputTableScanTypeDef(BaseValidatorModel):
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

class DeleteItemInputTableDeleteItemTypeDef(BaseValidatorModel):
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

class PutItemInputTablePutItemTypeDef(BaseValidatorModel):
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

class UpdateItemInputTableUpdateItemTypeDef(BaseValidatorModel):
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

class WriteRequestServiceResourceOutputTypeDef(BaseValidatorModel):
    PutRequest: Optional[PutRequestServiceResourceOutputTypeDef] = None
    DeleteRequest: Optional[DeleteRequestServiceResourceOutputTypeDef] = None

class WriteRequestServiceResourceTypeDef(BaseValidatorModel):
    PutRequest: Optional[PutRequestServiceResourceTypeDef] = None
    DeleteRequest: Optional[DeleteRequestServiceResourceTypeDef] = None

class AutoScalingSettingsDescriptionTypeDef(BaseValidatorModel):
    MinimumUnits: Optional[int] = None
    MaximumUnits: Optional[int] = None
    AutoScalingDisabled: Optional[bool] = None
    AutoScalingRoleArn: Optional[str] = None
    ScalingPolicies: Optional[List[AutoScalingPolicyDescriptionTypeDef]] = None

class AutoScalingSettingsUpdateTypeDef(BaseValidatorModel):
    MinimumUnits: Optional[int] = None
    MaximumUnits: Optional[int] = None
    AutoScalingDisabled: Optional[bool] = None
    AutoScalingRoleArn: Optional[str] = None
    ScalingPolicyUpdate: Optional[AutoScalingPolicyUpdateTypeDef] = None

class BatchGetItemOutputServiceResourceTypeDef(BaseValidatorModel):
    Responses: Dict[str, List[Dict[str, TableAttributeValueTypeDef]]]
    UnprocessedKeys: Dict[str, KeysAndAttributesServiceResourceOutputTypeDef]
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetItemOutputTypeDef(BaseValidatorModel):
    Responses: Dict[str, List[Dict[str, AttributeValueTypeDef]]]
    UnprocessedKeys: Dict[str, KeysAndAttributesOutputTypeDef]
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteItemOutputTableTypeDef(BaseValidatorModel):
    Attributes: Dict[str, TableAttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ItemCollectionMetrics: ItemCollectionMetricsTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteItemOutputTypeDef(BaseValidatorModel):
    Attributes: Dict[str, AttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ItemCollectionMetrics: ItemCollectionMetricsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExecuteStatementOutputTypeDef(BaseValidatorModel):
    Items: List[Dict[str, AttributeValueTypeDef]]
    ConsumedCapacity: ConsumedCapacityTypeDef
    LastEvaluatedKey: Dict[str, AttributeValueTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ExecuteTransactionOutputTypeDef(BaseValidatorModel):
    Responses: List[ItemResponseTypeDef]
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetItemOutputTableTypeDef(BaseValidatorModel):
    ConsumedCapacity: ConsumedCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    Item: Optional[Dict[str, TableAttributeValueTypeDef]] = None

class GetItemOutputTypeDef(BaseValidatorModel):
    ConsumedCapacity: ConsumedCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    Item: Optional[Dict[str, AttributeValueTypeDef]] = None

class PutItemOutputTableTypeDef(BaseValidatorModel):
    Attributes: Dict[str, TableAttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ItemCollectionMetrics: ItemCollectionMetricsTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutItemOutputTypeDef(BaseValidatorModel):
    Attributes: Dict[str, AttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ItemCollectionMetrics: ItemCollectionMetricsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class QueryOutputTableTypeDef(BaseValidatorModel):
    Items: List[Dict[str, TableAttributeValueTypeDef]]
    Count: int
    ScannedCount: int
    LastEvaluatedKey: Dict[str, TableAttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class QueryOutputTypeDef(BaseValidatorModel):
    Items: List[Dict[str, AttributeValueTypeDef]]
    Count: int
    ScannedCount: int
    LastEvaluatedKey: Dict[str, AttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ScanOutputTableTypeDef(BaseValidatorModel):
    Items: List[Dict[str, TableAttributeValueTypeDef]]
    Count: int
    ScannedCount: int
    LastEvaluatedKey: Dict[str, TableAttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ScanOutputTypeDef(BaseValidatorModel):
    Items: List[Dict[str, AttributeValueTypeDef]]
    Count: int
    ScannedCount: int
    LastEvaluatedKey: Dict[str, AttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TransactGetItemsOutputTypeDef(BaseValidatorModel):
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    Responses: List[ItemResponseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TransactWriteItemsOutputTypeDef(BaseValidatorModel):
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ItemCollectionMetrics: Dict[str, List[ItemCollectionMetricsTypeDef]]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateItemOutputTableTypeDef(BaseValidatorModel):
    Attributes: Dict[str, TableAttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ItemCollectionMetrics: ItemCollectionMetricsTableTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateItemOutputTypeDef(BaseValidatorModel):
    Attributes: Dict[str, AttributeValueTypeDef]
    ConsumedCapacity: ConsumedCapacityTypeDef
    ItemCollectionMetrics: ItemCollectionMetricsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeContinuousBackupsOutputTypeDef(BaseValidatorModel):
    ContinuousBackupsDescription: ContinuousBackupsDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContinuousBackupsOutputTypeDef(BaseValidatorModel):
    ContinuousBackupsDescription: ContinuousBackupsDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TableCreationParametersTypeDef(BaseValidatorModel):
    TableName: str
    AttributeDefinitions: Sequence[AttributeDefinitionTypeDef]
    KeySchema: Sequence[KeySchemaElementTypeDef]
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None
    SSESpecification: Optional[SSESpecificationTypeDef] = None
    GlobalSecondaryIndexes: Optional[Sequence[GlobalSecondaryIndexTypeDef]] = None

class GlobalSecondaryIndexUpdateTypeDef(BaseValidatorModel):
    Update: Optional[UpdateGlobalSecondaryIndexActionTypeDef] = None
    Create: Optional[CreateGlobalSecondaryIndexActionTypeDef] = None
    Delete: Optional[DeleteGlobalSecondaryIndexActionTypeDef] = None

class ListGlobalTablesOutputTypeDef(BaseValidatorModel):
    GlobalTables: List[GlobalTableTypeDef]
    LastEvaluatedGlobalTableName: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicaDescriptionTypeDef(BaseValidatorModel):
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

class CreateReplicationGroupMemberActionTypeDef(BaseValidatorModel):
    RegionName: str
    KMSMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverrideTypeDef] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverrideTypeDef] = None
    GlobalSecondaryIndexes: Optional[Sequence[ReplicaGlobalSecondaryIndexTypeDef]] = None
    TableClassOverride: Optional[TableClassType] = None

class UpdateReplicationGroupMemberActionTypeDef(BaseValidatorModel):
    RegionName: str
    KMSMasterKeyId: Optional[str] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputOverrideTypeDef] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputOverrideTypeDef] = None
    GlobalSecondaryIndexes: Optional[Sequence[ReplicaGlobalSecondaryIndexTypeDef]] = None
    TableClassOverride: Optional[TableClassType] = None

class UpdateGlobalTableInputRequestTypeDef(BaseValidatorModel):
    GlobalTableName: str
    ReplicaUpdates: Sequence[ReplicaUpdateTypeDef]

class DescribeExportOutputTypeDef(BaseValidatorModel):
    ExportDescription: ExportDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTableToPointInTimeOutputTypeDef(BaseValidatorModel):
    ExportDescription: ExportDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExportTableToPointInTimeInputRequestTypeDef(BaseValidatorModel):
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

class TableCreationParametersOutputTypeDef(BaseValidatorModel):
    TableName: str
    AttributeDefinitions: List[AttributeDefinitionTypeDef]
    KeySchema: List[KeySchemaElementTypeDef]
    BillingMode: Optional[BillingModeType] = None
    ProvisionedThroughput: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughput: Optional[OnDemandThroughputTypeDef] = None
    SSESpecification: Optional[SSESpecificationTypeDef] = None
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndexOutputTypeDef]] = None

class SourceTableFeatureDetailsTypeDef(BaseValidatorModel):
    LocalSecondaryIndexes: Optional[List[LocalSecondaryIndexInfoTypeDef]] = None
    GlobalSecondaryIndexes: Optional[List[GlobalSecondaryIndexInfoTypeDef]] = None
    StreamDescription: Optional[StreamSpecificationTypeDef] = None
    TimeToLiveDescription: Optional[TimeToLiveDescriptionTypeDef] = None
    SSEDescription: Optional[SSEDescriptionTypeDef] = None

class ListImportsOutputTypeDef(BaseValidatorModel):
    ImportSummaryList: List[ImportSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchExecuteStatementOutputTypeDef(BaseValidatorModel):
    Responses: List[BatchStatementResponseTypeDef]
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchWriteItemOutputTypeDef(BaseValidatorModel):
    UnprocessedItems: Dict[str, List[WriteRequestOutputTypeDef]]
    ItemCollectionMetrics: Dict[str, List[ItemCollectionMetricsTypeDef]]
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchExecuteStatementInputRequestTypeDef(BaseValidatorModel):
    Statements: Sequence[BatchStatementRequestTypeDef]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None

class QueryInputQueryPaginateTypeDef(BaseValidatorModel):
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

class QueryInputRequestTypeDef(BaseValidatorModel):
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

class ScanInputRequestTypeDef(BaseValidatorModel):
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

class ScanInputScanPaginateTypeDef(BaseValidatorModel):
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

class DeleteItemInputRequestTypeDef(BaseValidatorModel):
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

class PutItemInputRequestTypeDef(BaseValidatorModel):
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

class UpdateItemInputRequestTypeDef(BaseValidatorModel):
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

class TransactGetItemTypeDef(BaseValidatorModel):
    Get: GetTypeDef

class ExecuteTransactionInputRequestTypeDef(BaseValidatorModel):
    TransactStatements: Sequence[ParameterizedStatementTypeDef]
    ClientRequestToken: Optional[str] = None
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None

class WriteRequestTypeDef(BaseValidatorModel):
    PutRequest: Optional[PutRequestTypeDef] = None
    DeleteRequest: Optional[DeleteRequestTypeDef] = None

class TransactWriteItemTypeDef(BaseValidatorModel):
    ConditionCheck: Optional[ConditionCheckTypeDef] = None
    Put: Optional[PutTypeDef] = None
    Delete: Optional[DeleteTypeDef] = None
    Update: Optional[UpdateTypeDef] = None

class BatchGetItemInputServiceResourceBatchGetItemTypeDef(BaseValidatorModel):
    RequestItems: Mapping[str, KeysAndAttributesServiceResourceUnionTypeDef]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None

class BatchWriteItemOutputServiceResourceTypeDef(BaseValidatorModel):
    UnprocessedItems: Dict[str, List[WriteRequestServiceResourceOutputTypeDef]]
    ItemCollectionMetrics: Dict[str, List[ItemCollectionMetricsServiceResourceTypeDef]]
    ConsumedCapacity: List[ConsumedCapacityTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef(BaseValidatorModel):
    IndexName: Optional[str] = None
    IndexStatus: Optional[IndexStatusType] = None
    ProvisionedReadCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None
    ProvisionedWriteCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None

class ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef(BaseValidatorModel):
    IndexName: str
    IndexStatus: Optional[IndexStatusType] = None
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedReadCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None
    ProvisionedWriteCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None

class GlobalSecondaryIndexAutoScalingUpdateTypeDef(BaseValidatorModel):
    IndexName: Optional[str] = None
    ProvisionedWriteCapacityAutoScalingUpdate: Optional[AutoScalingSettingsUpdateTypeDef] = None

class GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef(BaseValidatorModel):
    IndexName: str
    ProvisionedWriteCapacityUnits: Optional[int] = None
    ProvisionedWriteCapacityAutoScalingSettingsUpdate: Optional[       AutoScalingSettingsUpdateTypeDef     ] = None

class ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef(BaseValidatorModel):
    IndexName: Optional[str] = None
    ProvisionedReadCapacityAutoScalingUpdate: Optional[AutoScalingSettingsUpdateTypeDef] = None

class ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef(BaseValidatorModel):
    IndexName: str
    ProvisionedReadCapacityUnits: Optional[int] = None
    ProvisionedReadCapacityAutoScalingSettingsUpdate: Optional[       AutoScalingSettingsUpdateTypeDef     ] = None

class ImportTableInputRequestTypeDef(BaseValidatorModel):
    S3BucketSource: S3BucketSourceTypeDef
    InputFormat: InputFormatType
    TableCreationParameters: TableCreationParametersTypeDef
    ClientToken: Optional[str] = None
    InputFormatOptions: Optional[InputFormatOptionsTypeDef] = None
    InputCompressionType: Optional[InputCompressionTypeType] = None

class GlobalTableDescriptionTypeDef(BaseValidatorModel):
    ReplicationGroup: Optional[List[ReplicaDescriptionTypeDef]] = None
    GlobalTableArn: Optional[str] = None
    CreationDateTime: Optional[datetime] = None
    GlobalTableStatus: Optional[GlobalTableStatusType] = None
    GlobalTableName: Optional[str] = None

class TableDescriptionTypeDef(BaseValidatorModel):
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

class ReplicationGroupUpdateTypeDef(BaseValidatorModel):
    Create: Optional[CreateReplicationGroupMemberActionTypeDef] = None
    Update: Optional[UpdateReplicationGroupMemberActionTypeDef] = None
    Delete: Optional[DeleteReplicationGroupMemberActionTypeDef] = None

class CreateTableInputRequestTypeDef(BaseValidatorModel):
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

class CreateTableInputServiceResourceCreateTableTypeDef(BaseValidatorModel):
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

class RestoreTableFromBackupInputRequestTypeDef(BaseValidatorModel):
    TargetTableName: str
    BackupArn: str
    BillingModeOverride: Optional[BillingModeType] = None
    GlobalSecondaryIndexOverride: Optional[Sequence[GlobalSecondaryIndexUnionTypeDef]] = None
    LocalSecondaryIndexOverride: Optional[Sequence[LocalSecondaryIndexTypeDef]] = None
    ProvisionedThroughputOverride: Optional[ProvisionedThroughputTypeDef] = None
    OnDemandThroughputOverride: Optional[OnDemandThroughputTypeDef] = None
    SSESpecificationOverride: Optional[SSESpecificationTypeDef] = None

class RestoreTableToPointInTimeInputRequestTypeDef(BaseValidatorModel):
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

class ImportTableDescriptionTypeDef(BaseValidatorModel):
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

class BackupDescriptionTypeDef(BaseValidatorModel):
    BackupDetails: Optional[BackupDetailsTypeDef] = None
    SourceTableDetails: Optional[SourceTableDetailsTypeDef] = None
    SourceTableFeatureDetails: Optional[SourceTableFeatureDetailsTypeDef] = None

class TransactGetItemsInputRequestTypeDef(BaseValidatorModel):
    TransactItems: Sequence[TransactGetItemTypeDef]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None

class BatchGetItemInputRequestTypeDef(BaseValidatorModel):
    RequestItems: Mapping[str, KeysAndAttributesUnionTypeDef]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None

class TransactWriteItemsInputRequestTypeDef(BaseValidatorModel):
    TransactItems: Sequence[TransactWriteItemTypeDef]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None
    ClientRequestToken: Optional[str] = None

class BatchWriteItemInputServiceResourceBatchWriteItemTypeDef(BaseValidatorModel):
    RequestItems: Mapping[str, Sequence[WriteRequestServiceResourceUnionTypeDef]]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None

class ReplicaAutoScalingDescriptionTypeDef(BaseValidatorModel):
    RegionName: Optional[str] = None
    GlobalSecondaryIndexes: Optional[       List[ReplicaGlobalSecondaryIndexAutoScalingDescriptionTypeDef]     ] = None
    ReplicaProvisionedReadCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None
    ReplicaProvisionedWriteCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None
    ReplicaStatus: Optional[ReplicaStatusType] = None

class ReplicaSettingsDescriptionTypeDef(BaseValidatorModel):
    RegionName: str
    ReplicaStatus: Optional[ReplicaStatusType] = None
    ReplicaBillingModeSummary: Optional[BillingModeSummaryTypeDef] = None
    ReplicaProvisionedReadCapacityUnits: Optional[int] = None
    ReplicaProvisionedReadCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None
    ReplicaProvisionedWriteCapacityUnits: Optional[int] = None
    ReplicaProvisionedWriteCapacityAutoScalingSettings: Optional[       AutoScalingSettingsDescriptionTypeDef     ] = None
    ReplicaGlobalSecondaryIndexSettings: Optional[       List[ReplicaGlobalSecondaryIndexSettingsDescriptionTypeDef]     ] = None
    ReplicaTableClassSummary: Optional[TableClassSummaryTypeDef] = None

class ReplicaAutoScalingUpdateTypeDef(BaseValidatorModel):
    RegionName: str
    ReplicaGlobalSecondaryIndexUpdates: Optional[       Sequence[ReplicaGlobalSecondaryIndexAutoScalingUpdateTypeDef]     ] = None
    ReplicaProvisionedReadCapacityAutoScalingUpdate: Optional[       AutoScalingSettingsUpdateTypeDef     ] = None

class ReplicaSettingsUpdateTypeDef(BaseValidatorModel):
    RegionName: str
    ReplicaProvisionedReadCapacityUnits: Optional[int] = None
    ReplicaProvisionedReadCapacityAutoScalingSettingsUpdate: Optional[       AutoScalingSettingsUpdateTypeDef     ] = None
    ReplicaGlobalSecondaryIndexSettingsUpdate: Optional[       Sequence[ReplicaGlobalSecondaryIndexSettingsUpdateTypeDef]     ] = None
    ReplicaTableClass: Optional[TableClassType] = None

class CreateGlobalTableOutputTypeDef(BaseValidatorModel):
    GlobalTableDescription: GlobalTableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGlobalTableOutputTypeDef(BaseValidatorModel):
    GlobalTableDescription: GlobalTableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGlobalTableOutputTypeDef(BaseValidatorModel):
    GlobalTableDescription: GlobalTableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTableOutputTypeDef(BaseValidatorModel):
    TableDescription: TableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTableOutputTypeDef(BaseValidatorModel):
    TableDescription: TableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTableOutputTypeDef(BaseValidatorModel):
    Table: TableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTableFromBackupOutputTypeDef(BaseValidatorModel):
    TableDescription: TableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreTableToPointInTimeOutputTypeDef(BaseValidatorModel):
    TableDescription: TableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableOutputTypeDef(BaseValidatorModel):
    TableDescription: TableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableInputRequestTypeDef(BaseValidatorModel):
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

class UpdateTableInputTableUpdateTypeDef(BaseValidatorModel):
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

class DescribeImportOutputTypeDef(BaseValidatorModel):
    ImportTableDescription: ImportTableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportTableOutputTypeDef(BaseValidatorModel):
    ImportTableDescription: ImportTableDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBackupOutputTypeDef(BaseValidatorModel):
    BackupDescription: BackupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBackupOutputTypeDef(BaseValidatorModel):
    BackupDescription: BackupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchWriteItemInputRequestTypeDef(BaseValidatorModel):
    RequestItems: Mapping[str, Sequence[WriteRequestUnionTypeDef]]
    ReturnConsumedCapacity: Optional[ReturnConsumedCapacityType] = None
    ReturnItemCollectionMetrics: Optional[ReturnItemCollectionMetricsType] = None

class TableAutoScalingDescriptionTypeDef(BaseValidatorModel):
    TableName: Optional[str] = None
    TableStatus: Optional[TableStatusType] = None
    Replicas: Optional[List[ReplicaAutoScalingDescriptionTypeDef]] = None

class DescribeGlobalTableSettingsOutputTypeDef(BaseValidatorModel):
    GlobalTableName: str
    ReplicaSettings: List[ReplicaSettingsDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGlobalTableSettingsOutputTypeDef(BaseValidatorModel):
    GlobalTableName: str
    ReplicaSettings: List[ReplicaSettingsDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableReplicaAutoScalingInputRequestTypeDef(BaseValidatorModel):
    TableName: str
    GlobalSecondaryIndexUpdates: Optional[       Sequence[GlobalSecondaryIndexAutoScalingUpdateTypeDef]     ] = None
    ProvisionedWriteCapacityAutoScalingUpdate: Optional[AutoScalingSettingsUpdateTypeDef] = None
    ReplicaUpdates: Optional[Sequence[ReplicaAutoScalingUpdateTypeDef]] = None

class UpdateGlobalTableSettingsInputRequestTypeDef(BaseValidatorModel):
    GlobalTableName: str
    GlobalTableBillingMode: Optional[BillingModeType] = None
    GlobalTableProvisionedWriteCapacityUnits: Optional[int] = None
    GlobalTableProvisionedWriteCapacityAutoScalingSettingsUpdate: Optional[       AutoScalingSettingsUpdateTypeDef     ] = None
    GlobalTableGlobalSecondaryIndexSettingsUpdate: Optional[       Sequence[GlobalTableGlobalSecondaryIndexSettingsUpdateTypeDef]     ] = None
    ReplicaSettingsUpdate: Optional[Sequence[ReplicaSettingsUpdateTypeDef]] = None

class DescribeTableReplicaAutoScalingOutputTypeDef(BaseValidatorModel):
    TableAutoScalingDescription: TableAutoScalingDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTableReplicaAutoScalingOutputTypeDef(BaseValidatorModel):
    TableAutoScalingDescription: TableAutoScalingDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

