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

class AddSourceIdentifierToSubscriptionMessageTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SourceIdentifier: str


class EventSubscriptionTypeDef(BaseValidatorModel):
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


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ApplyPendingMaintenanceActionMessageTypeDef(BaseValidatorModel):
    ResourceIdentifier: str
    ApplyAction: str
    OptInType: str


class AvailabilityZoneTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class CertificateDetailsTypeDef(BaseValidatorModel):
    CAIdentifier: Optional[str] = None
    ValidTill: Optional[datetime] = None


class CertificateTypeDef(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    CertificateType: Optional[str] = None
    Thumbprint: Optional[str] = None
    ValidFrom: Optional[datetime] = None
    ValidTill: Optional[datetime] = None
    CertificateArn: Optional[str] = None


class CloudwatchLogsExportConfigurationTypeDef(BaseValidatorModel):
    EnableLogTypes: Optional[Sequence[str]] = None
    DisableLogTypes: Optional[Sequence[str]] = None


class ClusterMasterUserSecretTypeDef(BaseValidatorModel):
    SecretArn: Optional[str] = None
    SecretStatus: Optional[str] = None
    KmsKeyId: Optional[str] = None


class DBClusterParameterGroupTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    DBClusterParameterGroupArn: Optional[str] = None


class DBClusterSnapshotTypeDef(BaseValidatorModel):
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


class CreateGlobalClusterMessageTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str
    SourceDBClusterIdentifier: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    DatabaseName: Optional[str] = None
    StorageEncrypted: Optional[bool] = None


class DBClusterMemberTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    IsClusterWriter: Optional[bool] = None
    DBClusterParameterGroupStatus: Optional[str] = None
    PromotionTier: Optional[int] = None


class ParameterTypeDef(BaseValidatorModel):
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


class DBClusterRoleTypeDef(BaseValidatorModel):
    RoleArn: Optional[str] = None
    Status: Optional[str] = None


class DBClusterSnapshotAttributeTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None


class VpcSecurityGroupMembershipTypeDef(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None


class UpgradeTargetTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    Description: Optional[str] = None
    AutoUpgrade: Optional[bool] = None
    IsMajorVersionUpgrade: Optional[bool] = None


class DBInstanceStatusInfoTypeDef(BaseValidatorModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None


class EndpointTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    HostedZoneId: Optional[str] = None


class DeleteDBClusterMessageTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None


class DeleteDBClusterParameterGroupMessageTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str


class DeleteDBClusterSnapshotMessageTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str


class DeleteDBInstanceMessageTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str


class DeleteDBSubnetGroupMessageTypeDef(BaseValidatorModel):
    DBSubnetGroupName: str


class DeleteEventSubscriptionMessageTypeDef(BaseValidatorModel):
    SubscriptionName: str


class DeleteGlobalClusterMessageTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str


class FilterTypeDef(BaseValidatorModel):
    Name: str
    Values: Sequence[str]


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeDBClusterSnapshotAttributesMessageTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class EventCategoriesMapTypeDef(BaseValidatorModel):
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None


class EventTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Date: Optional[datetime] = None
    SourceArn: Optional[str] = None


class FailoverDBClusterMessageTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    TargetDBInstanceIdentifier: Optional[str] = None


class FailoverGlobalClusterMessageTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str
    AllowDataLoss: Optional[bool] = None
    Switchover: Optional[bool] = None


class GlobalClusterMemberTypeDef(BaseValidatorModel):
    DBClusterArn: Optional[str] = None
    Readers: Optional[List[str]] = None
    IsWriter: Optional[bool] = None


class ModifyDBClusterSnapshotAttributeMessageTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: Optional[Sequence[str]] = None
    ValuesToRemove: Optional[Sequence[str]] = None


class ModifyDBInstanceMessageTypeDef(BaseValidatorModel):
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


class ModifyDBSubnetGroupMessageTypeDef(BaseValidatorModel):
    DBSubnetGroupName: str
    SubnetIds: Sequence[str]
    DBSubnetGroupDescription: Optional[str] = None


class ModifyEventSubscriptionMessageTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None


class ModifyGlobalClusterMessageTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str
    NewGlobalClusterIdentifier: Optional[str] = None
    DeletionProtection: Optional[bool] = None


class PendingCloudwatchLogsExportsTypeDef(BaseValidatorModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None


class PendingMaintenanceActionTypeDef(BaseValidatorModel):
    Action: Optional[str] = None
    AutoAppliedAfterDate: Optional[datetime] = None
    ForcedApplyDate: Optional[datetime] = None
    OptInStatus: Optional[str] = None
    CurrentApplyDate: Optional[datetime] = None
    Description: Optional[str] = None


class RebootDBInstanceMessageTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    ForceFailover: Optional[bool] = None


class RemoveFromGlobalClusterMessageTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str
    DbClusterIdentifier: str


class RemoveSourceIdentifierFromSubscriptionMessageTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SourceIdentifier: str


class RemoveTagsFromResourceMessageTypeDef(BaseValidatorModel):
    ResourceName: str
    TagKeys: Sequence[str]


class StartDBClusterMessageTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str


class StopDBClusterMessageTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str


class SwitchoverGlobalClusterMessageTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str


class AddSourceIdentifierToSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEventSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DBClusterParameterGroupNameMessageTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteEventSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class EventSubscriptionsMessageTypeDef(BaseValidatorModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyEventSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RemoveSourceIdentifierFromSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AddTagsToResourceMessageTypeDef(BaseValidatorModel):
    ResourceName: str
    Tags: Sequence[TagTypeDef]


class CopyDBClusterParameterGroupMessageTypeDef(BaseValidatorModel):
    SourceDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CopyDBClusterSnapshotMessageTypeDef(BaseValidatorModel):
    SourceDBClusterSnapshotIdentifier: str
    TargetDBClusterSnapshotIdentifier: str
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    CopyTags: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SourceRegion: Optional[str] = None


class CreateDBClusterMessageTypeDef(BaseValidatorModel):
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
    Tags: Optional[Sequence[TagTypeDef]] = None
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


class CreateDBClusterParameterGroupMessageTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateDBClusterSnapshotMessageTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str
    DBClusterIdentifier: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateDBInstanceMessageTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    DBInstanceClass: str
    Engine: str
    DBClusterIdentifier: str
    AvailabilityZone: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    PromotionTier: Optional[int] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None


class CreateDBSubnetGroupMessageTypeDef(BaseValidatorModel):
    DBSubnetGroupName: str
    DBSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateEventSubscriptionMessageTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    SourceIds: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class RestoreDBClusterFromSnapshotMessageTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    SnapshotIdentifier: str
    Engine: str
    AvailabilityZones: Optional[Sequence[str]] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    DBSubnetGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    DeletionProtection: Optional[bool] = None
    DBClusterParameterGroupName: Optional[str] = None
    StorageType: Optional[str] = None


class TagListMessageTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class OrderableDBInstanceOptionTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    AvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None
    Vpc: Optional[bool] = None
    StorageType: Optional[str] = None


class SubnetTypeDef(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZoneTypeDef] = None
    SubnetStatus: Optional[str] = None


class CertificateMessageTypeDef(BaseValidatorModel):
    Certificates: List[CertificateTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyDBClusterMessageTypeDef(BaseValidatorModel):
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
    CloudwatchLogsExportConfiguration: Optional[CloudwatchLogsExportConfigurationTypeDef] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None
    DeletionProtection: Optional[bool] = None
    StorageType: Optional[str] = None
    ManageMasterUserPassword: Optional[bool] = None
    MasterUserSecretKmsKeyId: Optional[str] = None
    RotateMasterUserPassword: Optional[bool] = None


class CopyDBClusterParameterGroupResultTypeDef(BaseValidatorModel):
    DBClusterParameterGroup: DBClusterParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDBClusterParameterGroupResultTypeDef(BaseValidatorModel):
    DBClusterParameterGroup: DBClusterParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DBClusterParameterGroupsMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBClusterParameterGroups: List[DBClusterParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CopyDBClusterSnapshotResultTypeDef(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDBClusterSnapshotResultTypeDef(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DBClusterSnapshotMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBClusterSnapshots: List[DBClusterSnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDBClusterSnapshotResultTypeDef(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DBClusterParameterGroupDetailsTypeDef(BaseValidatorModel):
    Parameters: List[ParameterTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class EngineDefaultsTypeDef(BaseValidatorModel):
    DBParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[ParameterTypeDef]] = None


class ModifyDBClusterParameterGroupMessageTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Parameters: Sequence[ParameterTypeDef]


class ResetDBClusterParameterGroupMessageTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None


class DBClusterSnapshotAttributesResultTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: Optional[str] = None
    DBClusterSnapshotAttributes: Optional[List[DBClusterSnapshotAttributeTypeDef]] = None


class DBClusterTypeDef(BaseValidatorModel):
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
    DBClusterMembers: Optional[List[DBClusterMemberTypeDef]] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembershipTypeDef]] = None
    HostedZoneId: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbClusterResourceId: Optional[str] = None
    DBClusterArn: Optional[str] = None
    AssociatedRoles: Optional[List[DBClusterRoleTypeDef]] = None
    CloneGroupId: Optional[str] = None
    ClusterCreateTime: Optional[datetime] = None
    EnabledCloudwatchLogsExports: Optional[List[str]] = None
    DeletionProtection: Optional[bool] = None
    StorageType: Optional[str] = None
    MasterUserSecret: Optional[ClusterMasterUserSecretTypeDef] = None


class DBEngineVersionTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    DBEngineDescription: Optional[str] = None
    DBEngineVersionDescription: Optional[str] = None
    ValidUpgradeTarget: Optional[List[UpgradeTargetTypeDef]] = None
    ExportableLogTypes: Optional[List[str]] = None
    SupportsLogExportsToCloudwatchLogs: Optional[bool] = None
    SupportedCACertificateIdentifiers: Optional[List[str]] = None
    SupportsCertificateRotationWithoutRestart: Optional[bool] = None


class DescribeCertificatesMessageTypeDef(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDBClusterParameterGroupsMessageTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDBClusterParametersMessageTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDBClusterSnapshotsMessageTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None


class DescribeDBClustersMessageTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDBEngineVersionsMessageTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None


class DescribeDBInstancesMessageTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeDBSubnetGroupsMessageTypeDef(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEngineDefaultClusterParametersMessageTypeDef(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEventCategoriesMessageTypeDef(BaseValidatorModel):
    SourceType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None


class DescribeEventSubscriptionsMessageTypeDef(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeGlobalClustersMessageTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeOrderableDBInstanceOptionsMessageTypeDef(BaseValidatorModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribePendingMaintenanceActionsMessageTypeDef(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


class ListTagsForResourceMessageTypeDef(BaseValidatorModel):
    ResourceName: str
    Filters: Optional[Sequence[FilterTypeDef]] = None


class DescribeCertificatesMessagePaginateTypeDef(BaseValidatorModel):
    CertificateIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDBClusterParameterGroupsMessagePaginateTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDBClusterParametersMessagePaginateTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDBClusterSnapshotsMessagePaginateTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDBClustersMessagePaginateTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDBEngineVersionsMessagePaginateTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDBInstancesMessagePaginateTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDBSubnetGroupsMessagePaginateTypeDef(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEventSubscriptionsMessagePaginateTypeDef(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeGlobalClustersMessagePaginateTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeOrderableDBInstanceOptionsMessagePaginateTypeDef(BaseValidatorModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribePendingMaintenanceActionsMessagePaginateTypeDef(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDBInstancesMessageWaitExtraTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeDBInstancesMessageWaitTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class DescribeEventsMessagePaginateTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEventsMessageTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class RestoreDBClusterToPointInTimeMessageTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    SourceDBClusterIdentifier: str
    RestoreType: Optional[str] = None
    RestoreToTime: Optional[TimestampTypeDef] = None
    UseLatestRestorableTime: Optional[bool] = None
    Port: Optional[int] = None
    DBSubnetGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    DeletionProtection: Optional[bool] = None
    StorageType: Optional[str] = None


class EventCategoriesMessageTypeDef(BaseValidatorModel):
    EventCategoriesMapList: List[EventCategoriesMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class EventsMessageTypeDef(BaseValidatorModel):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GlobalClusterTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    GlobalClusterResourceId: Optional[str] = None
    GlobalClusterArn: Optional[str] = None
    Status: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DatabaseName: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    DeletionProtection: Optional[bool] = None
    GlobalClusterMembers: Optional[List[GlobalClusterMemberTypeDef]] = None


class PendingModifiedValuesTypeDef(BaseValidatorModel):
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
    PendingCloudwatchLogsExports: Optional[PendingCloudwatchLogsExportsTypeDef] = None


class ResourcePendingMaintenanceActionsTypeDef(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    PendingMaintenanceActionDetails: Optional[List[PendingMaintenanceActionTypeDef]] = None


class OrderableDBInstanceOptionsMessageTypeDef(BaseValidatorModel):
    OrderableDBInstanceOptions: List[OrderableDBInstanceOptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class DBSubnetGroupTypeDef(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    DBSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None
    DBSubnetGroupArn: Optional[str] = None


class DescribeEngineDefaultClusterParametersResultTypeDef(BaseValidatorModel):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeDBClusterSnapshotAttributesResultTypeDef(BaseValidatorModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyDBClusterSnapshotAttributeResultTypeDef(BaseValidatorModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DBClusterMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBClusters: List[DBClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FailoverDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RestoreDBClusterFromSnapshotResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RestoreDBClusterToPointInTimeResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StopDBClusterResultTypeDef(BaseValidatorModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DBEngineVersionMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBEngineVersions: List[DBEngineVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateGlobalClusterResultTypeDef(BaseValidatorModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteGlobalClusterResultTypeDef(BaseValidatorModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FailoverGlobalClusterResultTypeDef(BaseValidatorModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GlobalClustersMessageTypeDef(BaseValidatorModel):
    Marker: str
    GlobalClusters: List[GlobalClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyGlobalClusterResultTypeDef(BaseValidatorModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RemoveFromGlobalClusterResultTypeDef(BaseValidatorModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SwitchoverGlobalClusterResultTypeDef(BaseValidatorModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ApplyPendingMaintenanceActionResultTypeDef(BaseValidatorModel):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PendingMaintenanceActionsMessageTypeDef(BaseValidatorModel):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActionsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDBSubnetGroupResultTypeDef(BaseValidatorModel):
    DBSubnetGroup: DBSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DBInstanceTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Engine: Optional[str] = None
    DBInstanceStatus: Optional[str] = None
    Endpoint: Optional[EndpointTypeDef] = None
    InstanceCreateTime: Optional[datetime] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembershipTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    DBSubnetGroup: Optional[DBSubnetGroupTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[PendingModifiedValuesTypeDef] = None
    LatestRestorableTime: Optional[datetime] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    PubliclyAccessible: Optional[bool] = None
    StatusInfos: Optional[List[DBInstanceStatusInfoTypeDef]] = None
    DBClusterIdentifier: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbiResourceId: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    PromotionTier: Optional[int] = None
    DBInstanceArn: Optional[str] = None
    EnabledCloudwatchLogsExports: Optional[List[str]] = None
    CertificateDetails: Optional[CertificateDetailsTypeDef] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None


class DBSubnetGroupMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBSubnetGroups: List[DBSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyDBSubnetGroupResultTypeDef(BaseValidatorModel):
    DBSubnetGroup: DBSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDBInstanceResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DBInstanceMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBInstances: List[DBInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDBInstanceResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyDBInstanceResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RebootDBInstanceResultTypeDef(BaseValidatorModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


