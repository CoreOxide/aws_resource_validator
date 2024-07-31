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
from aws_resource_validator.pydantic_models.neptune_constants import *

class AddRoleToDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: Optional[str] = None

class AddSourceIdentifierToSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str
    SourceIdentifier: str

class EventSubscriptionTypeDef(BaseModel):
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

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ApplyPendingMaintenanceActionMessageRequestTypeDef(BaseModel):
    ResourceIdentifier: str
    ApplyAction: str
    OptInType: str

class AvailabilityZoneTypeDef(BaseModel):
    Name: Optional[str] = None

class CharacterSetTypeDef(BaseModel):
    CharacterSetName: Optional[str] = None
    CharacterSetDescription: Optional[str] = None

class CloudwatchLogsExportConfigurationTypeDef(BaseModel):
    EnableLogTypes: Optional[Sequence[str]] = None
    DisableLogTypes: Optional[Sequence[str]] = None

class PendingCloudwatchLogsExportsTypeDef(BaseModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None

class DBClusterParameterGroupTypeDef(BaseModel):
    DBClusterParameterGroupName: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    DBClusterParameterGroupArn: Optional[str] = None

class DBClusterSnapshotTypeDef(BaseModel):
    AvailabilityZones: Optional[List[str]] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    SnapshotCreateTime: Optional[datetime] = None
    Engine: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Status: Optional[str] = None
    Port: Optional[int] = None
    VpcId: Optional[str] = None
    ClusterCreateTime: Optional[datetime] = None
    MasterUsername: Optional[str] = None
    EngineVersion: Optional[str] = None
    LicenseModel: Optional[str] = None
    SnapshotType: Optional[str] = None
    PercentProgress: Optional[int] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DBClusterSnapshotArn: Optional[str] = None
    SourceDBClusterSnapshotArn: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    StorageType: Optional[str] = None

class DBParameterGroupTypeDef(BaseModel):
    DBParameterGroupName: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    DBParameterGroupArn: Optional[str] = None

class ServerlessV2ScalingConfigurationTypeDef(BaseModel):
    MinCapacity: Optional[float] = None
    MaxCapacity: Optional[float] = None

class CreateGlobalClusterMessageRequestTypeDef(BaseModel):
    GlobalClusterIdentifier: str
    SourceDBClusterIdentifier: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    StorageEncrypted: Optional[bool] = None

class DBClusterEndpointTypeDef(BaseModel):
    DBClusterEndpointIdentifier: Optional[str] = None
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointResourceIdentifier: Optional[str] = None
    Endpoint: Optional[str] = None
    Status: Optional[str] = None
    EndpointType: Optional[str] = None
    CustomEndpointType: Optional[str] = None
    StaticMembers: Optional[List[str]] = None
    ExcludedMembers: Optional[List[str]] = None
    DBClusterEndpointArn: Optional[str] = None

class DBClusterMemberTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    IsClusterWriter: Optional[bool] = None
    DBClusterParameterGroupStatus: Optional[str] = None
    PromotionTier: Optional[int] = None

class DBClusterOptionGroupStatusTypeDef(BaseModel):
    DBClusterOptionGroupName: Optional[str] = None
    Status: Optional[str] = None

class ParameterTypeDef(BaseModel):
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

class DBClusterRoleTypeDef(BaseModel):
    RoleArn: Optional[str] = None
    Status: Optional[str] = None
    FeatureName: Optional[str] = None

class DBClusterSnapshotAttributeTypeDef(BaseModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None

class ServerlessV2ScalingConfigurationInfoTypeDef(BaseModel):
    MinCapacity: Optional[float] = None
    MaxCapacity: Optional[float] = None

class VpcSecurityGroupMembershipTypeDef(BaseModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None

class TimezoneTypeDef(BaseModel):
    TimezoneName: Optional[str] = None

class UpgradeTargetTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    Description: Optional[str] = None
    AutoUpgrade: Optional[bool] = None
    IsMajorVersionUpgrade: Optional[bool] = None
    SupportsGlobalDatabases: Optional[bool] = None

class DBInstanceStatusInfoTypeDef(BaseModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None

class DBParameterGroupStatusTypeDef(BaseModel):
    DBParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None

class DBSecurityGroupMembershipTypeDef(BaseModel):
    DBSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None

class DomainMembershipTypeDef(BaseModel):
    Domain: Optional[str] = None
    Status: Optional[str] = None
    FQDN: Optional[str] = None
    IAMRoleName: Optional[str] = None

class EndpointTypeDef(BaseModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    HostedZoneId: Optional[str] = None

class OptionGroupMembershipTypeDef(BaseModel):
    OptionGroupName: Optional[str] = None
    Status: Optional[str] = None

class DeleteDBClusterEndpointMessageRequestTypeDef(BaseModel):
    DBClusterEndpointIdentifier: str

class DeleteDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None

class DeleteDBClusterParameterGroupMessageRequestTypeDef(BaseModel):
    DBClusterParameterGroupName: str

class DeleteDBClusterSnapshotMessageRequestTypeDef(BaseModel):
    DBClusterSnapshotIdentifier: str

class DeleteDBInstanceMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None

class DeleteDBParameterGroupMessageRequestTypeDef(BaseModel):
    DBParameterGroupName: str

class DeleteDBSubnetGroupMessageRequestTypeDef(BaseModel):
    DBSubnetGroupName: str

class DeleteEventSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str

class DeleteGlobalClusterMessageRequestTypeDef(BaseModel):
    GlobalClusterIdentifier: str

class FilterTypeDef(BaseModel):
    Name: str
    Values: Sequence[str]

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeDBClusterSnapshotAttributesMessageRequestTypeDef(BaseModel):
    DBClusterSnapshotIdentifier: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeGlobalClustersMessageRequestTypeDef(BaseModel):
    GlobalClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeValidDBInstanceModificationsMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str

class DoubleRangeTypeDef(BaseModel):
    From: Optional[float] = None
    To: Optional[float] = None

class EventCategoriesMapTypeDef(BaseModel):
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None

class EventTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Date: Optional[datetime] = None
    SourceArn: Optional[str] = None

class FailoverDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    TargetDBInstanceIdentifier: Optional[str] = None

class FailoverGlobalClusterMessageRequestTypeDef(BaseModel):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str

class GlobalClusterMemberTypeDef(BaseModel):
    DBClusterArn: Optional[str] = None
    Readers: Optional[List[str]] = None
    IsWriter: Optional[bool] = None

class ModifyDBClusterEndpointMessageRequestTypeDef(BaseModel):
    DBClusterEndpointIdentifier: str
    EndpointType: Optional[str] = None
    StaticMembers: Optional[Sequence[str]] = None
    ExcludedMembers: Optional[Sequence[str]] = None

class ModifyDBClusterSnapshotAttributeMessageRequestTypeDef(BaseModel):
    DBClusterSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: Optional[Sequence[str]] = None
    ValuesToRemove: Optional[Sequence[str]] = None

class ModifyDBSubnetGroupMessageRequestTypeDef(BaseModel):
    DBSubnetGroupName: str
    SubnetIds: Sequence[str]
    DBSubnetGroupDescription: Optional[str] = None

class ModifyEventSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None

class ModifyGlobalClusterMessageRequestTypeDef(BaseModel):
    GlobalClusterIdentifier: str
    NewGlobalClusterIdentifier: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None

class PendingMaintenanceActionTypeDef(BaseModel):
    Action: Optional[str] = None
    AutoAppliedAfterDate: Optional[datetime] = None
    ForcedApplyDate: Optional[datetime] = None
    OptInStatus: Optional[str] = None
    CurrentApplyDate: Optional[datetime] = None
    Description: Optional[str] = None

class PromoteReadReplicaDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str

class RangeTypeDef(BaseModel):
    From: Optional[int] = None
    To: Optional[int] = None
    Step: Optional[int] = None

class RebootDBInstanceMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    ForceFailover: Optional[bool] = None

class RemoveFromGlobalClusterMessageRequestTypeDef(BaseModel):
    GlobalClusterIdentifier: str
    DbClusterIdentifier: str

class RemoveRoleFromDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: Optional[str] = None

class RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str
    SourceIdentifier: str

class RemoveTagsFromResourceMessageRequestTypeDef(BaseModel):
    ResourceName: str
    TagKeys: Sequence[str]

class StartDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str

class StopDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str

class AddSourceIdentifierToSubscriptionResultTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterEndpointOutputTypeDef(BaseModel):
    DBClusterEndpointIdentifier: str
    DBClusterIdentifier: str
    DBClusterEndpointResourceIdentifier: str
    Endpoint: str
    Status: str
    EndpointType: str
    CustomEndpointType: str
    StaticMembers: List[str]
    ExcludedMembers: List[str]
    DBClusterEndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEventSubscriptionResultTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupNameMessageTypeDef(BaseModel):
    DBClusterParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupNameMessageTypeDef(BaseModel):
    DBParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBClusterEndpointOutputTypeDef(BaseModel):
    DBClusterEndpointIdentifier: str
    DBClusterIdentifier: str
    DBClusterEndpointResourceIdentifier: str
    Endpoint: str
    Status: str
    EndpointType: str
    CustomEndpointType: str
    StaticMembers: List[str]
    ExcludedMembers: List[str]
    DBClusterEndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteEventSubscriptionResultTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EventSubscriptionsMessageTypeDef(BaseModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBClusterEndpointOutputTypeDef(BaseModel):
    DBClusterEndpointIdentifier: str
    DBClusterIdentifier: str
    DBClusterEndpointResourceIdentifier: str
    Endpoint: str
    Status: str
    EndpointType: str
    CustomEndpointType: str
    StaticMembers: List[str]
    ExcludedMembers: List[str]
    DBClusterEndpointArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyEventSubscriptionResultTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveSourceIdentifierFromSubscriptionResultTypeDef(BaseModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsToResourceMessageRequestTypeDef(BaseModel):
    ResourceName: str
    Tags: Sequence[TagTypeDef]

class CopyDBClusterParameterGroupMessageRequestTypeDef(BaseModel):
    SourceDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CopyDBClusterSnapshotMessageRequestTypeDef(BaseModel):
    SourceDBClusterSnapshotIdentifier: str
    TargetDBClusterSnapshotIdentifier: str
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    CopyTags: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SourceRegion: Optional[str] = None

class CopyDBParameterGroupMessageRequestTypeDef(BaseModel):
    SourceDBParameterGroupIdentifier: str
    TargetDBParameterGroupIdentifier: str
    TargetDBParameterGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBClusterEndpointMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    DBClusterEndpointIdentifier: str
    EndpointType: str
    StaticMembers: Optional[Sequence[str]] = None
    ExcludedMembers: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBClusterParameterGroupMessageRequestTypeDef(BaseModel):
    DBClusterParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBClusterSnapshotMessageRequestTypeDef(BaseModel):
    DBClusterSnapshotIdentifier: str
    DBClusterIdentifier: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBInstanceMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    DBInstanceClass: str
    Engine: str
    DBClusterIdentifier: str
    DBName: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MasterUsername: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    DBSecurityGroups: Optional[Sequence[str]] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    AvailabilityZone: Optional[str] = None
    DBSubnetGroupName: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    DBParameterGroupName: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    Port: Optional[int] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    CharacterSetName: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    TdeCredentialPassword: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    Domain: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    MonitoringRoleArn: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    PromotionTier: Optional[int] = None
    Timezone: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    DeletionProtection: Optional[bool] = None

class CreateDBParameterGroupMessageRequestTypeDef(BaseModel):
    DBParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBSubnetGroupMessageRequestTypeDef(BaseModel):
    DBSubnetGroupName: str
    DBSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateEventSubscriptionMessageRequestTypeDef(BaseModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    SourceIds: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagListMessageTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OrderableDBInstanceOptionTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    AvailabilityZones: Optional[List[AvailabilityZoneTypeDef]] = None
    MultiAZCapable: Optional[bool] = None
    ReadReplicaCapable: Optional[bool] = None
    Vpc: Optional[bool] = None
    SupportsStorageEncryption: Optional[bool] = None
    StorageType: Optional[str] = None
    SupportsIops: Optional[bool] = None
    SupportsEnhancedMonitoring: Optional[bool] = None
    SupportsIAMDatabaseAuthentication: Optional[bool] = None
    SupportsPerformanceInsights: Optional[bool] = None
    MinStorageSize: Optional[int] = None
    MaxStorageSize: Optional[int] = None
    MinIopsPerDbInstance: Optional[int] = None
    MaxIopsPerDbInstance: Optional[int] = None
    MinIopsPerGib: Optional[float] = None
    MaxIopsPerGib: Optional[float] = None
    SupportsGlobalDatabases: Optional[bool] = None

class SubnetTypeDef(BaseModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZoneTypeDef] = None
    SubnetStatus: Optional[str] = None

class ModifyDBInstanceMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: str
    AllocatedStorage: Optional[int] = None
    DBInstanceClass: Optional[str] = None
    DBSubnetGroupName: Optional[str] = None
    DBSecurityGroups: Optional[Sequence[str]] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    ApplyImmediately: Optional[bool] = None
    MasterUserPassword: Optional[str] = None
    DBParameterGroupName: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupName: Optional[str] = None
    NewDBInstanceIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    TdeCredentialPassword: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None
    Domain: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    DBPortNumber: Optional[int] = None
    PubliclyAccessible: Optional[bool] = None
    MonitoringRoleArn: Optional[str] = None
    DomainIAMRoleName: Optional[str] = None
    PromotionTier: Optional[int] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnablePerformanceInsights: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    CloudwatchLogsExportConfiguration: Optional[CloudwatchLogsExportConfigurationTypeDef] = None
    DeletionProtection: Optional[bool] = None

class ClusterPendingModifiedValuesTypeDef(BaseModel):
    PendingCloudwatchLogsExports: Optional[PendingCloudwatchLogsExportsTypeDef] = None
    DBClusterIdentifier: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    EngineVersion: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    StorageType: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Iops: Optional[int] = None

class PendingModifiedValuesTypeDef(BaseModel):
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

class CopyDBClusterParameterGroupResultTypeDef(BaseModel):
    DBClusterParameterGroup: DBClusterParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterParameterGroupResultTypeDef(BaseModel):
    DBClusterParameterGroup: DBClusterParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupsMessageTypeDef(BaseModel):
    Marker: str
    DBClusterParameterGroups: List[DBClusterParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CopyDBClusterSnapshotResultTypeDef(BaseModel):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterSnapshotResultTypeDef(BaseModel):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterSnapshotMessageTypeDef(BaseModel):
    Marker: str
    DBClusterSnapshots: List[DBClusterSnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBClusterSnapshotResultTypeDef(BaseModel):
    DBClusterSnapshot: DBClusterSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopyDBParameterGroupResultTypeDef(BaseModel):
    DBParameterGroup: DBParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBParameterGroupResultTypeDef(BaseModel):
    DBParameterGroup: DBParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupsMessageTypeDef(BaseModel):
    Marker: str
    DBParameterGroups: List[DBParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    Engine: str
    AvailabilityZones: Optional[Sequence[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    CharacterSetName: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    DatabaseName: Optional[str] = None
    DBClusterParameterGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    DBSubnetGroupName: Optional[str] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    MasterUsername: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    OptionGroupName: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReplicationSourceIdentifier: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    DeletionProtection: Optional[bool] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfigurationTypeDef] = None
    GlobalClusterIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    SourceRegion: Optional[str] = None

class ModifyDBClusterMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    NewDBClusterIdentifier: Optional[str] = None
    ApplyImmediately: Optional[bool] = None
    BackupRetentionPeriod: Optional[int] = None
    DBClusterParameterGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    Port: Optional[int] = None
    MasterUserPassword: Optional[str] = None
    OptionGroupName: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    CloudwatchLogsExportConfiguration: Optional[CloudwatchLogsExportConfigurationTypeDef] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None
    DBInstanceParameterGroupName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    CopyTagsToSnapshot: Optional[bool] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfigurationTypeDef] = None
    StorageType: Optional[str] = None

class RestoreDBClusterFromSnapshotMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    SnapshotIdentifier: str
    Engine: str
    AvailabilityZones: Optional[Sequence[str]] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    DBSubnetGroupName: Optional[str] = None
    DatabaseName: Optional[str] = None
    OptionGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    DBClusterParameterGroupName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    CopyTagsToSnapshot: Optional[bool] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfigurationTypeDef] = None
    StorageType: Optional[str] = None

class DBClusterEndpointMessageTypeDef(BaseModel):
    Marker: str
    DBClusterEndpoints: List[DBClusterEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupDetailsTypeDef(BaseModel):
    Parameters: List[ParameterTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupDetailsTypeDef(BaseModel):
    Parameters: List[ParameterTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EngineDefaultsTypeDef(BaseModel):
    DBParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[ParameterTypeDef]] = None

class ModifyDBClusterParameterGroupMessageRequestTypeDef(BaseModel):
    DBClusterParameterGroupName: str
    Parameters: Sequence[ParameterTypeDef]

class ModifyDBParameterGroupMessageRequestTypeDef(BaseModel):
    DBParameterGroupName: str
    Parameters: Sequence[ParameterTypeDef]

class ResetDBClusterParameterGroupMessageRequestTypeDef(BaseModel):
    DBClusterParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None

class ResetDBParameterGroupMessageRequestTypeDef(BaseModel):
    DBParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None

class DBClusterSnapshotAttributesResultTypeDef(BaseModel):
    DBClusterSnapshotIdentifier: Optional[str] = None
    DBClusterSnapshotAttributes: Optional[List[DBClusterSnapshotAttributeTypeDef]] = None

class DBEngineVersionTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    DBEngineDescription: Optional[str] = None
    DBEngineVersionDescription: Optional[str] = None
    DefaultCharacterSet: Optional[CharacterSetTypeDef] = None
    SupportedCharacterSets: Optional[List[CharacterSetTypeDef]] = None
    ValidUpgradeTarget: Optional[List[UpgradeTargetTypeDef]] = None
    SupportedTimezones: Optional[List[TimezoneTypeDef]] = None
    ExportableLogTypes: Optional[List[str]] = None
    SupportsLogExportsToCloudwatchLogs: Optional[bool] = None
    SupportsReadReplica: Optional[bool] = None
    SupportsGlobalDatabases: Optional[bool] = None

class DescribeDBClusterEndpointsMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterParameterGroupsMessageRequestTypeDef(BaseModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterParametersMessageRequestTypeDef(BaseModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterSnapshotsMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None

class DescribeDBClustersMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBEngineVersionsMessageRequestTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None

class DescribeDBInstancesMessageRequestTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBParameterGroupsMessageRequestTypeDef(BaseModel):
    DBParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBParametersMessageRequestTypeDef(BaseModel):
    DBParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBSubnetGroupsMessageRequestTypeDef(BaseModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEngineDefaultClusterParametersMessageRequestTypeDef(BaseModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEngineDefaultParametersMessageRequestTypeDef(BaseModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEventCategoriesMessageRequestTypeDef(BaseModel):
    SourceType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeEventSubscriptionsMessageRequestTypeDef(BaseModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeOrderableDBInstanceOptionsMessageRequestTypeDef(BaseModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribePendingMaintenanceActionsMessageRequestTypeDef(BaseModel):
    ResourceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class ListTagsForResourceMessageRequestTypeDef(BaseModel):
    ResourceName: str
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeDBClusterEndpointsMessageDescribeDBClusterEndpointsPaginateTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterParameterGroupsMessageDescribeDBClusterParameterGroupsPaginateTypeDef(BaseModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterParametersMessageDescribeDBClusterParametersPaginateTypeDef(BaseModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterSnapshotsMessageDescribeDBClusterSnapshotsPaginateTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClustersMessageDescribeDBClustersPaginateTypeDef(BaseModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBEngineVersionsMessageDescribeDBEngineVersionsPaginateTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBInstancesMessageDescribeDBInstancesPaginateTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBParameterGroupsMessageDescribeDBParameterGroupsPaginateTypeDef(BaseModel):
    DBParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBParametersMessageDescribeDBParametersPaginateTypeDef(BaseModel):
    DBParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateTypeDef(BaseModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef(BaseModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef(BaseModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGlobalClustersMessageDescribeGlobalClustersPaginateTypeDef(BaseModel):
    GlobalClusterIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrderableDBInstanceOptionsMessageDescribeOrderableDBInstanceOptionsPaginateTypeDef(BaseModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBInstancesMessageDBInstanceAvailableWaitTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBInstancesMessageDBInstanceDeletedWaitTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEventsMessageDescribeEventsPaginateTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsMessageRequestTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class RestoreDBClusterToPointInTimeMessageRequestTypeDef(BaseModel):
    DBClusterIdentifier: str
    SourceDBClusterIdentifier: str
    RestoreType: Optional[str] = None
    RestoreToTime: Optional[TimestampTypeDef] = None
    UseLatestRestorableTime: Optional[bool] = None
    Port: Optional[int] = None
    DBSubnetGroupName: Optional[str] = None
    OptionGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    KmsKeyId: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnableCloudwatchLogsExports: Optional[Sequence[str]] = None
    DBClusterParameterGroupName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfigurationTypeDef] = None
    StorageType: Optional[str] = None

class EventCategoriesMessageTypeDef(BaseModel):
    EventCategoriesMapList: List[EventCategoriesMapTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EventsMessageTypeDef(BaseModel):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GlobalClusterTypeDef(BaseModel):
    GlobalClusterIdentifier: Optional[str] = None
    GlobalClusterResourceId: Optional[str] = None
    GlobalClusterArn: Optional[str] = None
    Status: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    DeletionProtection: Optional[bool] = None
    GlobalClusterMembers: Optional[List[GlobalClusterMemberTypeDef]] = None

class ResourcePendingMaintenanceActionsTypeDef(BaseModel):
    ResourceIdentifier: Optional[str] = None
    PendingMaintenanceActionDetails: Optional[List[PendingMaintenanceActionTypeDef]] = None

class ValidStorageOptionsTypeDef(BaseModel):
    StorageType: Optional[str] = None
    StorageSize: Optional[List[RangeTypeDef]] = None
    ProvisionedIops: Optional[List[RangeTypeDef]] = None
    IopsToStorageRatio: Optional[List[DoubleRangeTypeDef]] = None

class OrderableDBInstanceOptionsMessageTypeDef(BaseModel):
    OrderableDBInstanceOptions: List[OrderableDBInstanceOptionTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBSubnetGroupTypeDef(BaseModel):
    DBSubnetGroupName: Optional[str] = None
    DBSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    SubnetGroupStatus: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None
    DBSubnetGroupArn: Optional[str] = None

class DBClusterTypeDef(BaseModel):
    AllocatedStorage: Optional[int] = None
    AvailabilityZones: Optional[List[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    CharacterSetName: Optional[str] = None
    DatabaseName: Optional[str] = None
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
    DBClusterOptionGroupMemberships: Optional[List[DBClusterOptionGroupStatusTypeDef]] = None
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
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    CloneGroupId: Optional[str] = None
    ClusterCreateTime: Optional[datetime] = None
    CopyTagsToSnapshot: Optional[bool] = None
    EnabledCloudwatchLogsExports: Optional[List[str]] = None
    PendingModifiedValues: Optional[ClusterPendingModifiedValuesTypeDef] = None
    DeletionProtection: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    AutomaticRestartTime: Optional[datetime] = None
    ServerlessV2ScalingConfiguration: Optional[       ServerlessV2ScalingConfigurationInfoTypeDef     ] = None
    GlobalClusterIdentifier: Optional[str] = None
    IOOptimizedNextAllowedModificationTime: Optional[datetime] = None
    StorageType: Optional[str] = None

class DescribeEngineDefaultClusterParametersResultTypeDef(BaseModel):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEngineDefaultParametersResultTypeDef(BaseModel):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBClusterSnapshotAttributesResultTypeDef(BaseModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBClusterSnapshotAttributeResultTypeDef(BaseModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBEngineVersionMessageTypeDef(BaseModel):
    Marker: str
    DBEngineVersions: List[DBEngineVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateGlobalClusterResultTypeDef(BaseModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGlobalClusterResultTypeDef(BaseModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverGlobalClusterResultTypeDef(BaseModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GlobalClustersMessageTypeDef(BaseModel):
    Marker: str
    GlobalClusters: List[GlobalClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyGlobalClusterResultTypeDef(BaseModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveFromGlobalClusterResultTypeDef(BaseModel):
    GlobalCluster: GlobalClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ApplyPendingMaintenanceActionResultTypeDef(BaseModel):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PendingMaintenanceActionsMessageTypeDef(BaseModel):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActionsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ValidDBInstanceModificationsMessageTypeDef(BaseModel):
    Storage: Optional[List[ValidStorageOptionsTypeDef]] = None

class CreateDBSubnetGroupResultTypeDef(BaseModel):
    DBSubnetGroup: DBSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBInstanceTypeDef(BaseModel):
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Engine: Optional[str] = None
    DBInstanceStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    DBName: Optional[str] = None
    Endpoint: Optional[EndpointTypeDef] = None
    AllocatedStorage: Optional[int] = None
    InstanceCreateTime: Optional[datetime] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DBSecurityGroups: Optional[List[DBSecurityGroupMembershipTypeDef]] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembershipTypeDef]] = None
    DBParameterGroups: Optional[List[DBParameterGroupStatusTypeDef]] = None
    AvailabilityZone: Optional[str] = None
    DBSubnetGroup: Optional[DBSubnetGroupTypeDef] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[PendingModifiedValuesTypeDef] = None
    LatestRestorableTime: Optional[datetime] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReadReplicaSourceDBInstanceIdentifier: Optional[str] = None
    ReadReplicaDBInstanceIdentifiers: Optional[List[str]] = None
    ReadReplicaDBClusterIdentifiers: Optional[List[str]] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupMemberships: Optional[List[OptionGroupMembershipTypeDef]] = None
    CharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StatusInfos: Optional[List[DBInstanceStatusInfoTypeDef]] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DBClusterIdentifier: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbiResourceId: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None
    DomainMemberships: Optional[List[DomainMembershipTypeDef]] = None
    CopyTagsToSnapshot: Optional[bool] = None
    MonitoringInterval: Optional[int] = None
    EnhancedMonitoringResourceArn: Optional[str] = None
    MonitoringRoleArn: Optional[str] = None
    PromotionTier: Optional[int] = None
    DBInstanceArn: Optional[str] = None
    Timezone: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    PerformanceInsightsEnabled: Optional[bool] = None
    PerformanceInsightsKMSKeyId: Optional[str] = None
    EnabledCloudwatchLogsExports: Optional[List[str]] = None
    DeletionProtection: Optional[bool] = None

class DBSubnetGroupMessageTypeDef(BaseModel):
    Marker: str
    DBSubnetGroups: List[DBSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBSubnetGroupResultTypeDef(BaseModel):
    DBSubnetGroup: DBSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterMessageTypeDef(BaseModel):
    Marker: str
    DBClusters: List[DBClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PromoteReadReplicaDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBClusterFromSnapshotResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RestoreDBClusterToPointInTimeResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StopDBClusterResultTypeDef(BaseModel):
    DBCluster: DBClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeValidDBInstanceModificationsResultTypeDef(BaseModel):
    ValidDBInstanceModificationsMessage: ValidDBInstanceModificationsMessageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBInstanceResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBInstanceMessageTypeDef(BaseModel):
    Marker: str
    DBInstances: List[DBInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBInstanceResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBInstanceResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootDBInstanceResultTypeDef(BaseModel):
    DBInstance: DBInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

