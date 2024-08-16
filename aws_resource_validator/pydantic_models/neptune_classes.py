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
from aws_resource_validator.pydantic_models.neptune_constants import *

class AddRoleToDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: Optional[str] = None

class AddSourceIdentifierToSubscriptionMessageRequestTypeDef(BaseValidatorModel):
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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ApplyPendingMaintenanceActionMessageRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: str
    ApplyAction: str
    OptInType: str

class AvailabilityZoneTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class CharacterSetTypeDef(BaseValidatorModel):
    CharacterSetName: Optional[str] = None
    CharacterSetDescription: Optional[str] = None

class CloudwatchLogsExportConfigurationTypeDef(BaseValidatorModel):
    EnableLogTypes: Optional[Sequence[str]] = None
    DisableLogTypes: Optional[Sequence[str]] = None

class PendingCloudwatchLogsExportsTypeDef(BaseValidatorModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None

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

class DBParameterGroupTypeDef(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    DBParameterGroupArn: Optional[str] = None

class ServerlessV2ScalingConfigurationTypeDef(BaseValidatorModel):
    MinCapacity: Optional[float] = None
    MaxCapacity: Optional[float] = None

class CreateGlobalClusterMessageRequestTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str
    SourceDBClusterIdentifier: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    StorageEncrypted: Optional[bool] = None

class DBClusterEndpointTypeDef(BaseValidatorModel):
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

class DBClusterMemberTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    IsClusterWriter: Optional[bool] = None
    DBClusterParameterGroupStatus: Optional[str] = None
    PromotionTier: Optional[int] = None

class DBClusterOptionGroupStatusTypeDef(BaseValidatorModel):
    DBClusterOptionGroupName: Optional[str] = None
    Status: Optional[str] = None

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
    FeatureName: Optional[str] = None

class DBClusterSnapshotAttributeTypeDef(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None

class ServerlessV2ScalingConfigurationInfoTypeDef(BaseValidatorModel):
    MinCapacity: Optional[float] = None
    MaxCapacity: Optional[float] = None

class VpcSecurityGroupMembershipTypeDef(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None

class TimezoneTypeDef(BaseValidatorModel):
    TimezoneName: Optional[str] = None

class UpgradeTargetTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    Description: Optional[str] = None
    AutoUpgrade: Optional[bool] = None
    IsMajorVersionUpgrade: Optional[bool] = None
    SupportsGlobalDatabases: Optional[bool] = None

class DBInstanceStatusInfoTypeDef(BaseValidatorModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None

class DBParameterGroupStatusTypeDef(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None

class DBSecurityGroupMembershipTypeDef(BaseValidatorModel):
    DBSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None

class DomainMembershipTypeDef(BaseValidatorModel):
    Domain: Optional[str] = None
    Status: Optional[str] = None
    FQDN: Optional[str] = None
    IAMRoleName: Optional[str] = None

class EndpointTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    HostedZoneId: Optional[str] = None

class OptionGroupMembershipTypeDef(BaseValidatorModel):
    OptionGroupName: Optional[str] = None
    Status: Optional[str] = None

class DeleteDBClusterEndpointMessageRequestTypeDef(BaseValidatorModel):
    DBClusterEndpointIdentifier: str

class DeleteDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None

class DeleteDBClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str

class DeleteDBClusterSnapshotMessageRequestTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str

class DeleteDBInstanceMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None

class DeleteDBParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupName: str

class DeleteDBSubnetGroupMessageRequestTypeDef(BaseValidatorModel):
    DBSubnetGroupName: str

class DeleteEventSubscriptionMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: str

class DeleteGlobalClusterMessageRequestTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str

class FilterTypeDef(BaseValidatorModel):
    Name: str
    Values: Sequence[str]

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeDBClusterSnapshotAttributesMessageRequestTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str

class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeGlobalClustersMessageRequestTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeValidDBInstanceModificationsMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str

class DoubleRangeTypeDef(BaseValidatorModel):
    From: Optional[float] = None
    To: Optional[float] = None

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

class FailoverDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    TargetDBInstanceIdentifier: Optional[str] = None

class FailoverGlobalClusterMessageRequestTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str

class GlobalClusterMemberTypeDef(BaseValidatorModel):
    DBClusterArn: Optional[str] = None
    Readers: Optional[List[str]] = None
    IsWriter: Optional[bool] = None

class ModifyDBClusterEndpointMessageRequestTypeDef(BaseValidatorModel):
    DBClusterEndpointIdentifier: str
    EndpointType: Optional[str] = None
    StaticMembers: Optional[Sequence[str]] = None
    ExcludedMembers: Optional[Sequence[str]] = None

class ModifyDBClusterSnapshotAttributeMessageRequestTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: Optional[Sequence[str]] = None
    ValuesToRemove: Optional[Sequence[str]] = None

class ModifyDBSubnetGroupMessageRequestTypeDef(BaseValidatorModel):
    DBSubnetGroupName: str
    SubnetIds: Sequence[str]
    DBSubnetGroupDescription: Optional[str] = None

class ModifyEventSubscriptionMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None

class ModifyGlobalClusterMessageRequestTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str
    NewGlobalClusterIdentifier: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None

class PendingMaintenanceActionTypeDef(BaseValidatorModel):
    Action: Optional[str] = None
    AutoAppliedAfterDate: Optional[datetime] = None
    ForcedApplyDate: Optional[datetime] = None
    OptInStatus: Optional[str] = None
    CurrentApplyDate: Optional[datetime] = None
    Description: Optional[str] = None

class PromoteReadReplicaDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str

class RangeTypeDef(BaseValidatorModel):
    From: Optional[int] = None
    To: Optional[int] = None
    Step: Optional[int] = None

class RebootDBInstanceMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: str
    ForceFailover: Optional[bool] = None

class RemoveFromGlobalClusterMessageRequestTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: str
    DbClusterIdentifier: str

class RemoveRoleFromDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: Optional[str] = None

class RemoveSourceIdentifierFromSubscriptionMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SourceIdentifier: str

class RemoveTagsFromResourceMessageRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    TagKeys: Sequence[str]

class StartDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str

class StopDBClusterMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str

class AddSourceIdentifierToSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterEndpointOutputTypeDef(BaseValidatorModel):
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

class CreateEventSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupNameMessageTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupNameMessageTypeDef(BaseValidatorModel):
    DBParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDBClusterEndpointOutputTypeDef(BaseValidatorModel):
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

class DeleteEventSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class EventSubscriptionsMessageTypeDef(BaseValidatorModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBClusterEndpointOutputTypeDef(BaseValidatorModel):
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

class ModifyEventSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveSourceIdentifierFromSubscriptionResultTypeDef(BaseValidatorModel):
    EventSubscription: EventSubscriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsToResourceMessageRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    Tags: Sequence[TagTypeDef]

class CopyDBClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    SourceDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CopyDBClusterSnapshotMessageRequestTypeDef(BaseValidatorModel):
    SourceDBClusterSnapshotIdentifier: str
    TargetDBClusterSnapshotIdentifier: str
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    CopyTags: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SourceRegion: Optional[str] = None

class CopyDBParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    SourceDBParameterGroupIdentifier: str
    TargetDBParameterGroupIdentifier: str
    TargetDBParameterGroupDescription: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBClusterEndpointMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: str
    DBClusterEndpointIdentifier: str
    EndpointType: str
    StaticMembers: Optional[Sequence[str]] = None
    ExcludedMembers: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBClusterSnapshotMessageRequestTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str
    DBClusterIdentifier: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBInstanceMessageRequestTypeDef(BaseValidatorModel):
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

class CreateDBParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateDBSubnetGroupMessageRequestTypeDef(BaseValidatorModel):
    DBSubnetGroupName: str
    DBSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateEventSubscriptionMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    EventCategories: Optional[Sequence[str]] = None
    SourceIds: Optional[Sequence[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagListMessageTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class OrderableDBInstanceOptionTypeDef(BaseValidatorModel):
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

class SubnetTypeDef(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZoneTypeDef] = None
    SubnetStatus: Optional[str] = None

class ModifyDBInstanceMessageRequestTypeDef(BaseValidatorModel):
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

class ClusterPendingModifiedValuesTypeDef(BaseValidatorModel):
    PendingCloudwatchLogsExports: Optional[PendingCloudwatchLogsExportsTypeDef] = None
    DBClusterIdentifier: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    EngineVersion: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    StorageType: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Iops: Optional[int] = None

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

class CopyDBParameterGroupResultTypeDef(BaseValidatorModel):
    DBParameterGroup: DBParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBParameterGroupResultTypeDef(BaseValidatorModel):
    DBParameterGroup: DBParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupsMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBParameterGroups: List[DBParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDBClusterMessageRequestTypeDef(BaseValidatorModel):
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

class ModifyDBClusterMessageRequestTypeDef(BaseValidatorModel):
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

class RestoreDBClusterFromSnapshotMessageRequestTypeDef(BaseValidatorModel):
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

class DBClusterEndpointMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBClusterEndpoints: List[DBClusterEndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DBClusterParameterGroupDetailsTypeDef(BaseValidatorModel):
    Parameters: List[ParameterTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DBParameterGroupDetailsTypeDef(BaseValidatorModel):
    Parameters: List[ParameterTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class EngineDefaultsTypeDef(BaseValidatorModel):
    DBParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[ParameterTypeDef]] = None

class ModifyDBClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Parameters: Sequence[ParameterTypeDef]

class ModifyDBParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupName: str
    Parameters: Sequence[ParameterTypeDef]

class ResetDBClusterParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None

class ResetDBParameterGroupMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[Sequence[ParameterTypeDef]] = None

class DBClusterSnapshotAttributesResultTypeDef(BaseValidatorModel):
    DBClusterSnapshotIdentifier: Optional[str] = None
    DBClusterSnapshotAttributes: Optional[List[DBClusterSnapshotAttributeTypeDef]] = None

class DBEngineVersionTypeDef(BaseValidatorModel):
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

class DescribeDBClusterEndpointsMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterParameterGroupsMessageRequestTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterParametersMessageRequestTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBClusterSnapshotsMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None

class DescribeDBClustersMessageRequestTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBEngineVersionsMessageRequestTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None

class DescribeDBInstancesMessageRequestTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBParameterGroupsMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBParametersMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeDBSubnetGroupsMessageRequestTypeDef(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEngineDefaultClusterParametersMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEngineDefaultParametersMessageRequestTypeDef(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEventCategoriesMessageRequestTypeDef(BaseValidatorModel):
    SourceType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeEventSubscriptionsMessageRequestTypeDef(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeOrderableDBInstanceOptionsMessageRequestTypeDef(BaseValidatorModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribePendingMaintenanceActionsMessageRequestTypeDef(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None

class ListTagsForResourceMessageRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    Filters: Optional[Sequence[FilterTypeDef]] = None

class DescribeDBClusterEndpointsMessageDescribeDBClusterEndpointsPaginateTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterParameterGroupsMessageDescribeDBClusterParameterGroupsPaginateTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterParametersMessageDescribeDBClusterParametersPaginateTypeDef(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClusterSnapshotsMessageDescribeDBClusterSnapshotsPaginateTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBClustersMessageDescribeDBClustersPaginateTypeDef(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBEngineVersionsMessageDescribeDBEngineVersionsPaginateTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBInstancesMessageDescribeDBInstancesPaginateTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBParameterGroupsMessageDescribeDBParameterGroupsPaginateTypeDef(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBParametersMessageDescribeDBParametersPaginateTypeDef(BaseValidatorModel):
    DBParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBSubnetGroupsMessageDescribeDBSubnetGroupsPaginateTypeDef(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventSubscriptionsMessageDescribeEventSubscriptionsPaginateTypeDef(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGlobalClustersMessageDescribeGlobalClustersPaginateTypeDef(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeOrderableDBInstanceOptionsMessageDescribeOrderableDBInstanceOptionsPaginateTypeDef(BaseValidatorModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDBInstancesMessageDBInstanceAvailableWaitTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeDBInstancesMessageDBInstanceDeletedWaitTypeDef(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeEventsMessageDescribeEventsPaginateTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsMessageRequestTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    EventCategories: Optional[Sequence[str]] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class RestoreDBClusterToPointInTimeMessageRequestTypeDef(BaseValidatorModel):
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
    StorageEncrypted: Optional[bool] = None
    DeletionProtection: Optional[bool] = None
    GlobalClusterMembers: Optional[List[GlobalClusterMemberTypeDef]] = None

class ResourcePendingMaintenanceActionsTypeDef(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    PendingMaintenanceActionDetails: Optional[List[PendingMaintenanceActionTypeDef]] = None

class ValidStorageOptionsTypeDef(BaseValidatorModel):
    StorageType: Optional[str] = None
    StorageSize: Optional[List[RangeTypeDef]] = None
    ProvisionedIops: Optional[List[RangeTypeDef]] = None
    IopsToStorageRatio: Optional[List[DoubleRangeTypeDef]] = None

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

class DBClusterTypeDef(BaseValidatorModel):
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

class DescribeEngineDefaultClusterParametersResultTypeDef(BaseValidatorModel):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEngineDefaultParametersResultTypeDef(BaseValidatorModel):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDBClusterSnapshotAttributesResultTypeDef(BaseValidatorModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBClusterSnapshotAttributeResultTypeDef(BaseValidatorModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResultTypeDef
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

class ApplyPendingMaintenanceActionResultTypeDef(BaseValidatorModel):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActionsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PendingMaintenanceActionsMessageTypeDef(BaseValidatorModel):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActionsTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ValidDBInstanceModificationsMessageTypeDef(BaseValidatorModel):
    Storage: Optional[List[ValidStorageOptionsTypeDef]] = None

class CreateDBSubnetGroupResultTypeDef(BaseValidatorModel):
    DBSubnetGroup: DBSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DBInstanceTypeDef(BaseValidatorModel):
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

class DBSubnetGroupMessageTypeDef(BaseValidatorModel):
    Marker: str
    DBSubnetGroups: List[DBSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyDBSubnetGroupResultTypeDef(BaseValidatorModel):
    DBSubnetGroup: DBSubnetGroupTypeDef
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

class PromoteReadReplicaDBClusterResultTypeDef(BaseValidatorModel):
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

class DescribeValidDBInstanceModificationsResultTypeDef(BaseValidatorModel):
    ValidDBInstanceModificationsMessage: ValidDBInstanceModificationsMessageTypeDef
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

