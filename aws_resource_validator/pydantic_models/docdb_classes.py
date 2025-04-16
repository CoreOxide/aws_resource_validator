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
from aws_resource_validator.pydantic_models.docdb_constants import *

class AddSourceIdentifierToSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SourceIdentifier: str


class EventSubscription(BaseValidatorModel):
    CustomerAwsId: Optional[str] = None
    CustSubscriptionId: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    Status: Optional[str] = None
    SubscriptionCreationTime: Optional[str] = None
    SourceType: Optional[str] = None
    SourceIdsList: Optional[List[str]] = None
    EventCategoriesList: Optional[List[str]] = None
    Enabled: Optional[bool] = None
    EventSubscriptionArn: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ApplyPendingMaintenanceActionMessage(BaseValidatorModel):
    ResourceIdentifier: str
    ApplyAction: str
    OptInType: str


class AvailabilityZone(BaseValidatorModel):
    Name: Optional[str] = None


class CertificateDetails(BaseValidatorModel):
    CAIdentifier: Optional[str] = None
    ValidTill: Optional[datetime] = None


class Certificate(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    CertificateType: Optional[str] = None
    Thumbprint: Optional[str] = None
    ValidFrom: Optional[datetime] = None
    ValidTill: Optional[datetime] = None
    CertificateArn: Optional[str] = None


class CloudwatchLogsExportConfiguration(BaseValidatorModel):
    EnableLogTypes: Optional[Sequence[str]] = None
    DisableLogTypes: Optional[Sequence[str]] = None


class ClusterMasterUserSecret(BaseValidatorModel):
    SecretArn: Optional[str] = None
    SecretStatus: Optional[str] = None
    KmsKeyId: Optional[str] = None


class DBClusterParameterGroup(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    DBClusterParameterGroupArn: Optional[str] = None


class DBClusterSnapshot(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    SnapshotCreateTime: Optional[datetime] = None
    Engine: Optional[str] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    VpcId: Optional[str] = None
    ClusterCreateTime: Optional[datetime] = None
    MasterUsername: Optional[str] = None
    EngineVersion: Optional[str] = None
    SnapshotType: Optional[str] = None
    PercentProgress: Optional[int] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DBClusterSnapshotArn: Optional[str] = None
    SourceDBClusterSnapshotArn: Optional[str] = None
    StorageType: Optional[str] = None


class CreateGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str
    SourceDBClusterIdentifier: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    DatabaseName: Optional[str] = None
    StorageEncrypted: Optional[bool] = None


class DBClusterMember(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    IsClusterWriter: Optional[bool] = None
    DBClusterParameterGroupStatus: Optional[str] = None
    PromotionTier: Optional[int] = None


class Parameter(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    ApplyType: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None
    ApplyMethod: Optional[ApplyMethodType] = None


class DBClusterRole(BaseValidatorModel):
    RoleArn: Optional[str] = None
    Status: Optional[str] = None


class DBClusterSnapshotAttribute(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None


class VpcSecurityGroupMembership(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None


class UpgradeTarget(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    Description: Optional[str] = None
    AutoUpgrade: Optional[bool] = None
    IsMajorVersionUpgrade: Optional[bool] = None


class DBInstanceStatusInfo(BaseValidatorModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None


class Endpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    HostedZoneId: Optional[str] = None


class DeleteDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None


class DeleteDBClusterParameterGroupMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str


class DeleteDBClusterSnapshotMessage(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str


class DeleteDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str


class DeleteDBSubnetGroupMessage(BaseValidatorModel):
    DBSubnetGroupName: str


class DeleteEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str


class DeleteGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str


class Filter(BaseValidatorModel):
    Name: str
    Values: Sequence[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeDBClusterSnapshotAttributesMessage(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class EventCategoriesMap(BaseValidatorModel):
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None


class Event(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Date: Optional[datetime] = None
    SourceArn: Optional[str] = None


class FailoverDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    TargetDBInstanceIdentifier: Optional[str] = None


class FailoverGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str
    AllowDataLoss: Optional[bool] = None
    Switchover: Optional[bool] = None


class GlobalClusterMember(BaseValidatorModel):
    DBClusterArn: Optional[str] = None
    Readers: Optional[List[str]] = None
    IsWriter: Optional[bool] = None


class ModifyDBClusterSnapshotAttributeMessage(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: Optional[Sequence[str]] = None
    ValuesToRemove: Optional[Sequence[str]] = None


class ModifyDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    DBInstanceClass: Optional[str] = None
    ApplyImmediately: Optional[bool] = None
    PreferredMaintenanceWindow: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    NewDBInstanceIdentifier: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    PromotionTier: Optional[int] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    CertificateRotationRestart: Optional[bool] = None


class ModifyDBSubnetGroupMessage(BaseValidatorModel):
    DBSubnetGroupName: str
    SubnetIds: Sequence[str]
    DBSubnetGroupDescription: Optional[str] = None


class ModifyEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None


class ModifyGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str
    NewGlobalClusterIdentifier: Optional[str] = None
    DeletionProtection: Optional[bool] = None


class PendingCloudwatchLogsExports(BaseValidatorModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None


class PendingMaintenanceAction(BaseValidatorModel):
    Action: Optional[str] = None
    AutoAppliedAfterDate: Optional[datetime] = None
    ForcedApplyDate: Optional[datetime] = None
    OptInStatus: Optional[str] = None
    CurrentApplyDate: Optional[datetime] = None
    Description: Optional[str] = None


class RebootDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    ForceFailover: Optional[bool] = None


class RemoveFromGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str
    DbClusterIdentifier: str


class RemoveSourceIdentifierFromSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SourceIdentifier: str


class RemoveTagsFromResourceMessage(BaseValidatorModel):
    ResourceName: str
    TagKeys: Sequence[str]


class StartDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str


class StopDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str


class SwitchoverGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str


class AddSourceIdentifierToSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


class CreateEventSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


class DBClusterParameterGroupNameMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    ResponseMetadata: ResponseMetadata


class DeleteEventSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class EventSubscriptionsMessage(BaseValidatorModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscription]
    ResponseMetadata: ResponseMetadata


class ModifyEventSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


class RemoveSourceIdentifierFromSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


class AddTagsToResourceMessage(BaseValidatorModel):
    ResourceName: str
    Tags: Sequence[Tag]


class CopyDBClusterParameterGroupMessage(BaseValidatorModel):
    SourceDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupDescription: str
    Tags: Optional[Sequence[Tag]] = None


class CopyDBClusterSnapshotMessage(BaseValidatorModel):
    SourceDBClusterSnapshotIdentifier: str
    TargetDBClusterSnapshotIdentifier: str
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    CopyTags: Optional[bool] = None
    Tags: Optional[Sequence[Tag]] = None
    SourceRegion: Optional[str] = None


class CreateDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    Engine: str
    AvailabilityZones: Optional[Sequence[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    DBClusterParameterGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    DBSubnetGroupName: Optional[str] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    MasterUsername: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    DeletionProtection: Optional[bool] = None
    GlobalClusterIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    ManageMasterUserPassword: Optional[bool] = None
    MasterUserSecretKmsKeyId: Optional[str] = None
    SourceRegion: Optional[str] = None


class CreateDBClusterParameterGroupMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[Tag]] = None


class CreateDBClusterSnapshotMessage(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str
    DBClusterIdentifier: str
    Tags: Optional[Sequence[Tag]] = None


class CreateDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    DBInstanceClass: str
    Engine: str
    DBClusterIdentifier: str
    AvailabilityZone: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    Tags: Optional[Sequence[Tag]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    PromotionTier: Optional[int] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None


class CreateDBSubnetGroupMessage(BaseValidatorModel):
    DBSubnetGroupName: str
    DBSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: Optional[Sequence[Tag]] = None


class CreateEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    SourceIds: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[Tag]] = None


class RestoreDBClusterFromSnapshotMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    SnapshotIdentifier: str
    Engine: str
    AvailabilityZones: Optional[Sequence[str]] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    DBSubnetGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None
    KmsKeyId: Optional[str] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    DeletionProtection: Optional[bool] = None
    DBClusterParameterGroupName: Optional[str] = None
    StorageType: Optional[str] = None


class TagListMessage(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class OrderableDBInstanceOption(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    AvailabilityZones: Optional[List[AvailabilityZone]] = None
    Vpc: Optional[bool] = None
    StorageType: Optional[str] = None


class Subnet(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZone] = None
    SubnetStatus: Optional[str] = None


class CertificateMessage(BaseValidatorModel):
    Certificates: List[Certificate]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ModifyDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    NewDBClusterIdentifier: Optional[str] = None
    ApplyImmediately: Optional[bool] = None
    BackupRetentionPeriod: Optional[int] = None
    DBClusterParameterGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    Port: Optional[int] = None
    MasterUserPassword: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    CloudwatchLogsExportConfiguration: Optional[CloudwatchLogsExportConfiguration] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None
    DeletionProtection: Optional[bool] = None
    StorageType: Optional[str] = None
    ManageMasterUserPassword: Optional[bool] = None
    MasterUserSecretKmsKeyId: Optional[str] = None
    RotateMasterUserPassword: Optional[bool] = None


class CopyDBClusterParameterGroupResult(BaseValidatorModel):
    DBClusterParameterGroup: DBClusterParameterGroup
    ResponseMetadata: ResponseMetadata


class CreateDBClusterParameterGroupResult(BaseValidatorModel):
    DBClusterParameterGroup: DBClusterParameterGroup
    ResponseMetadata: ResponseMetadata


class DBClusterParameterGroupsMessage(BaseValidatorModel):
    Marker: str
    DBClusterParameterGroups: List[DBClusterParameterGroup]
    ResponseMetadata: ResponseMetadata


class CopyDBClusterSnapshotResult(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshot
    ResponseMetadata: ResponseMetadata


class CreateDBClusterSnapshotResult(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshot
    ResponseMetadata: ResponseMetadata


class DBClusterSnapshotMessage(BaseValidatorModel):
    Marker: str
    DBClusterSnapshots: List[DBClusterSnapshot]
    ResponseMetadata: ResponseMetadata


class DeleteDBClusterSnapshotResult(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshot
    ResponseMetadata: ResponseMetadata


class DBClusterParameterGroupDetails(BaseValidatorModel):
    Parameters: List[Parameter]
    Marker: str
    ResponseMetadata: ResponseMetadata


class EngineDefaults(BaseValidatorModel):
    DBParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[Parameter]] = None


class ModifyDBClusterParameterGroupMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Parameters: Sequence[Parameter]


class ResetDBClusterParameterGroupMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[Sequence[Parameter]] = None


class DBClusterSnapshotAttributesResult(BaseValidatorModel):
    DBClusterSnapshotIdentifier: Optional[str] = None
    DBClusterSnapshotAttributes: Optional[List[DBClusterSnapshotAttribute]] = None


class DBCluster(BaseValidatorModel):
    AvailabilityZones: Optional[List[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    DBClusterIdentifier: Optional[str] = None
    DBClusterParameterGroup: Optional[str] = None
    DBSubnetGroup: Optional[str] = None
    Status: Optional[str] = None
    PercentProgress: Optional[str] = None
    EarliestRestorableTime: Optional[datetime] = None
    Endpoint: Optional[str] = None
    ReaderEndpoint: Optional[str] = None
    MultiAZ: Optional[bool] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    LatestRestorableTime: Optional[datetime] = None
    Port: Optional[int] = None
    MasterUsername: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReplicationSourceIdentifier: Optional[str] = None
    ReadReplicaIdentifiers: Optional[List[str]] = None
    DBClusterMembers: Optional[List[DBClusterMember]] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembership]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    DBClusterArn: Optional[str] = None
    AssociatedRoles: Optional[List[DBClusterRole]] = None
    CloneGroupId: Optional[str] = None
    ClusterCreateTime: Optional[datetime] = None
    EnabledCloudwatchLogsExports: Optional[List[str]] = None
    DeletionProtection: Optional[bool] = None
    StorageType: Optional[str] = None
    MasterUserSecret: Optional[ClusterMasterUserSecret] = None


class DBEngineVersion(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    DBEngineDescription: Optional[str] = None
    DBEngineVersionDescription: Optional[str] = None
    ValidUpgradeTarget: Optional[List[UpgradeTarget]] = None
    ExportableLogTypes: Optional[List[str]] = None
    SupportsLogExportsToCloudwatchLogs: Optional[bool] = None
    SupportedCACertificateIdentifiers: Optional[List[str]] = None
    SupportsCertificateRotationWithoutRestart: Optional[bool] = None


class DescribeCertificatesMessage(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDBClusterParameterGroupsMessage(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDBClusterParametersMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDBClusterSnapshotsMessage(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None


class DescribeDBClustersMessage(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDBEngineVersionsMessage(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None


class DescribeDBInstancesMessage(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDBSubnetGroupsMessage(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEngineDefaultClusterParametersMessage(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEventCategoriesMessage(BaseValidatorModel):
    SourceType: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None


class DescribeEventSubscriptionsMessage(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeGlobalClustersMessage(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeOrderableDBInstanceOptionsMessage(BaseValidatorModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribePendingMaintenanceActionsMessage(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class ListTagsForResourceMessage(BaseValidatorModel):
    ResourceName: str
    Filters: Optional[Sequence[Filter]] = None


class DescribeCertificatesMessagePaginate(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClusterParameterGroupsMessagePaginate(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClusterParametersMessagePaginate(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClusterSnapshotsMessagePaginate(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClustersMessagePaginate(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBEngineVersionsMessagePaginate(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBInstancesMessagePaginate(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBSubnetGroupsMessagePaginate(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventSubscriptionsMessagePaginate(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeGlobalClustersMessagePaginate(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOrderableDBInstanceOptionsMessagePaginate(BaseValidatorModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribePendingMaintenanceActionsMessagePaginate(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBInstancesMessageWaitExtra(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeDBInstancesMessageWait(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class Timestamp(BaseValidatorModel):
    pass


class DescribeEventsMessagePaginate(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventsMessage(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class RestoreDBClusterToPointInTimeMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    SourceDBClusterIdentifier: str
    RestoreType: Optional[str] = None
    RestoreToTime: Optional[Timestamp] = None
    UseLatestRestorableTime: Optional[bool] = None
    Port: Optional[int] = None
    DBSubnetGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None
    KmsKeyId: Optional[str] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    DeletionProtection: Optional[bool] = None
    StorageType: Optional[str] = None


class EventCategoriesMessage(BaseValidatorModel):
    EventCategoriesMapList: List[EventCategoriesMap]
    ResponseMetadata: ResponseMetadata


class EventsMessage(BaseValidatorModel):
    Marker: str
    Events: List[Event]
    ResponseMetadata: ResponseMetadata


class GlobalCluster(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    GlobalClusterResourceId: Optional[str] = None
    GlobalClusterArn: Optional[str] = None
    Status: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DatabaseName: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    DeletionProtection: Optional[bool] = None
    GlobalClusterMembers: Optional[List[GlobalClusterMember]] = None


class PendingModifiedValues(BaseValidatorModel):
    DBInstanceClass: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MasterUserPassword: Optional[str] = None
    Port: Optional[int] = None
    BackupRetentionPeriod: Optional[int] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    DBInstanceIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None
    DBSubnetGroupName: Optional[str] = None
    PendingCloudwatchLogsExports: Optional[PendingCloudwatchLogsExports] = None


class ResourcePendingMaintenanceActions(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    PendingMaintenanceActionDetails: Optional[List[PendingMaintenanceAction]] = None


class OrderableDBInstanceOptionsMessage(BaseValidatorModel):
    OrderableDBInstanceOptions: List[OrderableDBInstanceOption]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DBSubnetGroup(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    DBSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[Subnet]] = None
    DBSubnetGroupArn: Optional[str] = None


class DescribeEngineDefaultClusterParametersResult(BaseValidatorModel):
    EngineDefaults: EngineDefaults
    ResponseMetadata: ResponseMetadata


class DescribeDBClusterSnapshotAttributesResult(BaseValidatorModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResult
    ResponseMetadata: ResponseMetadata


class ModifyDBClusterSnapshotAttributeResult(BaseValidatorModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResult
    ResponseMetadata: ResponseMetadata


class CreateDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


class DBClusterMessage(BaseValidatorModel):
    Marker: str
    DBClusters: List[DBCluster]
    ResponseMetadata: ResponseMetadata


class DeleteDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


class FailoverDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


class ModifyDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


class RestoreDBClusterFromSnapshotResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


class RestoreDBClusterToPointInTimeResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


class StartDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


class StopDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


class DBEngineVersionMessage(BaseValidatorModel):
    Marker: str
    DBEngineVersions: List[DBEngineVersion]
    ResponseMetadata: ResponseMetadata


class CreateGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


class DeleteGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


class FailoverGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


class GlobalClustersMessage(BaseValidatorModel):
    Marker: str
    GlobalClusters: List[GlobalCluster]
    ResponseMetadata: ResponseMetadata


class ModifyGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


class RemoveFromGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


class SwitchoverGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


class ApplyPendingMaintenanceActionResult(BaseValidatorModel):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActions
    ResponseMetadata: ResponseMetadata


class PendingMaintenanceActionsMessage(BaseValidatorModel):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActions]
    Marker: str
    ResponseMetadata: ResponseMetadata


class CreateDBSubnetGroupResult(BaseValidatorModel):
    DBSubnetGroup: DBSubnetGroup
    ResponseMetadata: ResponseMetadata


class DBInstance(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Engine: Optional[str] = None
    DBInstanceStatus: Optional[str] = None
    Endpoint: Optional[Endpoint] = None
    InstanceCreateTime: Optional[datetime] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembership]] = None
    AvailabilityZone: Optional[str] = None
    DBSubnetGroup: Optional[DBSubnetGroup] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[PendingModifiedValues] = None
    LatestRestorableTime: Optional[datetime] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    PubliclyAccessible: Optional[bool] = None
    StatusInfos: Optional[List[DBInstanceStatusInfo]] = None
    DBClusterIdentifier: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbiResourceId: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    PromotionTier: Optional[int] = None
    DBInstanceArn: Optional[str] = None
    EnabledCloudwatchLogsExports: Optional[List[str]] = None
    CertificateDetails: Optional[CertificateDetails] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None


class DBSubnetGroupMessage(BaseValidatorModel):
    Marker: str
    DBSubnetGroups: List[DBSubnetGroup]
    ResponseMetadata: ResponseMetadata


class ModifyDBSubnetGroupResult(BaseValidatorModel):
    DBSubnetGroup: DBSubnetGroup
    ResponseMetadata: ResponseMetadata


class CreateDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


class DBInstanceMessage(BaseValidatorModel):
    Marker: str
    DBInstances: List[DBInstance]
    ResponseMetadata: ResponseMetadata


class DeleteDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


class ModifyDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


class RebootDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


