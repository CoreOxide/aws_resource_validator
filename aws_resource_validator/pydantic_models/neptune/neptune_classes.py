from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.neptune.neptune_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




# This class is the input for the 'add_role_to_db_cluster' function.
class AddRoleToDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: Optional[str] = None


# This class is the input for the 'add_source_identifier_to_subscription' function.
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


# This class is the input for the 'apply_pending_maintenance_action' function.
class ApplyPendingMaintenanceActionMessage(BaseValidatorModel):
    ResourceIdentifier: str
    ApplyAction: str
    OptInType: str


class AvailabilityZone(BaseValidatorModel):
    Name: Optional[str] = None


class CharacterSet(BaseValidatorModel):
    CharacterSetName: Optional[str] = None
    CharacterSetDescription: Optional[str] = None


class CloudwatchLogsExportConfiguration(BaseValidatorModel):
    EnableLogTypes: Optional[List[str]] = None
    DisableLogTypes: Optional[List[str]] = None


class PendingCloudwatchLogsExports(BaseValidatorModel):
    LogTypesToEnable: Optional[List[str]] = None
    LogTypesToDisable: Optional[List[str]] = None


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


class DBParameterGroup(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    DBParameterGroupArn: Optional[str] = None


class ServerlessV2ScalingConfiguration(BaseValidatorModel):
    MinCapacity: Optional[float] = None
    MaxCapacity: Optional[float] = None


# This class is the input for the 'create_global_cluster' function.
class CreateGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str
    SourceDBClusterIdentifier: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    StorageEncrypted: Optional[bool] = None


class DBClusterEndpoint(BaseValidatorModel):
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


class DBClusterMember(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    IsClusterWriter: Optional[bool] = None
    DBClusterParameterGroupStatus: Optional[str] = None
    PromotionTier: Optional[int] = None


class DBClusterOptionGroupStatus(BaseValidatorModel):
    DBClusterOptionGroupName: Optional[str] = None
    Status: Optional[str] = None


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
    FeatureName: Optional[str] = None


class DBClusterSnapshotAttribute(BaseValidatorModel):
    AttributeName: Optional[str] = None
    AttributeValues: Optional[List[str]] = None


class ServerlessV2ScalingConfigurationInfo(BaseValidatorModel):
    MinCapacity: Optional[float] = None
    MaxCapacity: Optional[float] = None


class VpcSecurityGroupMembership(BaseValidatorModel):
    VpcSecurityGroupId: Optional[str] = None
    Status: Optional[str] = None


class Timezone(BaseValidatorModel):
    TimezoneName: Optional[str] = None


class UpgradeTarget(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    Description: Optional[str] = None
    AutoUpgrade: Optional[bool] = None
    IsMajorVersionUpgrade: Optional[bool] = None
    SupportsGlobalDatabases: Optional[bool] = None


class DBInstanceStatusInfo(BaseValidatorModel):
    StatusType: Optional[str] = None
    Normal: Optional[bool] = None
    Status: Optional[str] = None
    Message: Optional[str] = None


class DBParameterGroupStatus(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None


class DBSecurityGroupMembership(BaseValidatorModel):
    DBSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None


class DomainMembership(BaseValidatorModel):
    Domain: Optional[str] = None
    Status: Optional[str] = None
    FQDN: Optional[str] = None
    IAMRoleName: Optional[str] = None


class Endpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    HostedZoneId: Optional[str] = None


class OptionGroupMembership(BaseValidatorModel):
    OptionGroupName: Optional[str] = None
    Status: Optional[str] = None


# This class is the input for the 'delete_db_cluster_endpoint' function.
class DeleteDBClusterEndpointMessage(BaseValidatorModel):
    DBClusterEndpointIdentifier: str


# This class is the input for the 'delete_db_cluster' function.
class DeleteDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None


# This class is the input for the 'delete_db_cluster_parameter_group' function.
class DeleteDBClusterParameterGroupMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str


# This class is the input for the 'delete_db_cluster_snapshot' function.
class DeleteDBClusterSnapshotMessage(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str


# This class is the input for the 'delete_db_instance' function.
class DeleteDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    SkipFinalSnapshot: Optional[bool] = None
    FinalDBSnapshotIdentifier: Optional[str] = None


# This class is the input for the 'delete_db_parameter_group' function.
class DeleteDBParameterGroupMessage(BaseValidatorModel):
    DBParameterGroupName: str


# This class is the input for the 'delete_db_subnet_group' function.
class DeleteDBSubnetGroupMessage(BaseValidatorModel):
    DBSubnetGroupName: str


# This class is the input for the 'delete_event_subscription' function.
class DeleteEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str


# This class is the input for the 'delete_global_cluster' function.
class DeleteGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str


class Filter(BaseValidatorModel):
    Name: str
    Values: List[str]


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_db_cluster_snapshot_attributes' function.
class DescribeDBClusterSnapshotAttributesMessage(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'describe_global_clusters' function.
class DescribeGlobalClustersMessage(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_valid_db_instance_modifications' function.
class DescribeValidDBInstanceModificationsMessage(BaseValidatorModel):
    DBInstanceIdentifier: str


class DoubleRange(BaseValidatorModel):
    From: Optional[float] = None
    To: Optional[float] = None


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


# This class is the input for the 'failover_db_cluster' function.
class FailoverDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    TargetDBInstanceIdentifier: Optional[str] = None


# This class is the input for the 'failover_global_cluster' function.
class FailoverGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str
    TargetDbClusterIdentifier: str


class GlobalClusterMember(BaseValidatorModel):
    DBClusterArn: Optional[str] = None
    Readers: Optional[List[str]] = None
    IsWriter: Optional[bool] = None


# This class is the input for the 'modify_db_cluster_endpoint' function.
class ModifyDBClusterEndpointMessage(BaseValidatorModel):
    DBClusterEndpointIdentifier: str
    EndpointType: Optional[str] = None
    StaticMembers: Optional[List[str]] = None
    ExcludedMembers: Optional[List[str]] = None


# This class is the input for the 'modify_db_cluster_snapshot_attribute' function.
class ModifyDBClusterSnapshotAttributeMessage(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str
    AttributeName: str
    ValuesToAdd: Optional[List[str]] = None
    ValuesToRemove: Optional[List[str]] = None


# This class is the input for the 'modify_db_subnet_group' function.
class ModifyDBSubnetGroupMessage(BaseValidatorModel):
    DBSubnetGroupName: str
    SubnetIds: List[str]
    DBSubnetGroupDescription: Optional[str] = None


# This class is the input for the 'modify_event_subscription' function.
class ModifyEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: Optional[str] = None
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    Enabled: Optional[bool] = None


# This class is the input for the 'modify_global_cluster' function.
class ModifyGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str
    NewGlobalClusterIdentifier: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None


class PendingMaintenanceAction(BaseValidatorModel):
    Action: Optional[str] = None
    AutoAppliedAfterDate: Optional[datetime] = None
    ForcedApplyDate: Optional[datetime] = None
    OptInStatus: Optional[str] = None
    CurrentApplyDate: Optional[datetime] = None
    Description: Optional[str] = None


# This class is the input for the 'promote_read_replica_db_cluster' function.
class PromoteReadReplicaDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str


class Range(BaseValidatorModel):
    From: Optional[int] = None
    To: Optional[int] = None
    Step: Optional[int] = None


# This class is the input for the 'reboot_db_instance' function.
class RebootDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    ForceFailover: Optional[bool] = None


# This class is the input for the 'remove_from_global_cluster' function.
class RemoveFromGlobalClusterMessage(BaseValidatorModel):
    GlobalClusterIdentifier: str
    DbClusterIdentifier: str


# This class is the input for the 'remove_role_from_db_cluster' function.
class RemoveRoleFromDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    RoleArn: str
    FeatureName: Optional[str] = None


# This class is the input for the 'remove_source_identifier_from_subscription' function.
class RemoveSourceIdentifierFromSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SourceIdentifier: str


# This class is the input for the 'remove_tags_from_resource' function.
class RemoveTagsFromResourceMessage(BaseValidatorModel):
    ResourceName: str
    TagKeys: List[str]


# This class is the input for the 'start_db_cluster' function.
class StartDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str


# This class is the input for the 'stop_db_cluster' function.
class StopDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str


# This class is the output for the 'add_source_identifier_to_subscription' function.
class AddSourceIdentifierToSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_cluster_endpoint' function.
class CreateDBClusterEndpointOutput(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_event_subscription' function.
class CreateEventSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_db_cluster_parameter_group' function.
class DBClusterParameterGroupNameMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_db_parameter_group' function.
class DBParameterGroupNameMessage(BaseValidatorModel):
    DBParameterGroupName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_cluster_endpoint' function.
class DeleteDBClusterEndpointOutput(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_event_subscription' function.
class DeleteEventSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_tags_from_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_event_subscriptions' function.
class EventSubscriptionsMessage(BaseValidatorModel):
    Marker: str
    EventSubscriptionsList: List[EventSubscription]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_cluster_endpoint' function.
class ModifyDBClusterEndpointOutput(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_event_subscription' function.
class ModifyEventSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_source_identifier_from_subscription' function.
class RemoveSourceIdentifierFromSubscriptionResult(BaseValidatorModel):
    EventSubscription: EventSubscription
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'add_tags_to_resource' function.
class AddTagsToResourceMessage(BaseValidatorModel):
    ResourceName: str
    Tags: List[Tag]


# This class is the input for the 'copy_db_cluster_parameter_group' function.
class CopyDBClusterParameterGroupMessage(BaseValidatorModel):
    SourceDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupIdentifier: str
    TargetDBClusterParameterGroupDescription: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'copy_db_cluster_snapshot' function.
class CopyDBClusterSnapshotMessage(BaseValidatorModel):
    SourceDBClusterSnapshotIdentifier: str
    TargetDBClusterSnapshotIdentifier: str
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    CopyTags: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    SourceRegion: Optional[str] = None


# This class is the input for the 'copy_db_parameter_group' function.
class CopyDBParameterGroupMessage(BaseValidatorModel):
    SourceDBParameterGroupIdentifier: str
    TargetDBParameterGroupIdentifier: str
    TargetDBParameterGroupDescription: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_db_cluster_endpoint' function.
class CreateDBClusterEndpointMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    DBClusterEndpointIdentifier: str
    EndpointType: str
    StaticMembers: Optional[List[str]] = None
    ExcludedMembers: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_db_cluster_parameter_group' function.
class CreateDBClusterParameterGroupMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_db_cluster_snapshot' function.
class CreateDBClusterSnapshotMessage(BaseValidatorModel):
    DBClusterSnapshotIdentifier: str
    DBClusterIdentifier: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_db_instance' function.
class CreateDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    DBInstanceClass: str
    Engine: str
    DBClusterIdentifier: str
    DBName: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    MasterUsername: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    DBSecurityGroups: Optional[List[str]] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
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
    Tags: Optional[List[Tag]] = None
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
    EnableCloudwatchLogsExports: Optional[List[str]] = None
    DeletionProtection: Optional[bool] = None


# This class is the input for the 'create_db_parameter_group' function.
class CreateDBParameterGroupMessage(BaseValidatorModel):
    DBParameterGroupName: str
    DBParameterGroupFamily: str
    Description: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_db_subnet_group' function.
class CreateDBSubnetGroupMessage(BaseValidatorModel):
    DBSubnetGroupName: str
    DBSubnetGroupDescription: str
    SubnetIds: List[str]
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_event_subscription' function.
class CreateEventSubscriptionMessage(BaseValidatorModel):
    SubscriptionName: str
    SnsTopicArn: str
    SourceType: Optional[str] = None
    EventCategories: Optional[List[str]] = None
    SourceIds: Optional[List[str]] = None
    Enabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class TagListMessage(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class OrderableDBInstanceOption(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    AvailabilityZones: Optional[List[AvailabilityZone]] = None
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


class Subnet(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZone] = None
    SubnetStatus: Optional[str] = None


# This class is the input for the 'modify_db_instance' function.
class ModifyDBInstanceMessage(BaseValidatorModel):
    DBInstanceIdentifier: str
    AllocatedStorage: Optional[int] = None
    DBInstanceClass: Optional[str] = None
    DBSubnetGroupName: Optional[str] = None
    DBSecurityGroups: Optional[List[str]] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
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
    CloudwatchLogsExportConfiguration: Optional[CloudwatchLogsExportConfiguration] = None
    DeletionProtection: Optional[bool] = None


class ClusterPendingModifiedValues(BaseValidatorModel):
    PendingCloudwatchLogsExports: Optional[PendingCloudwatchLogsExports] = None
    DBClusterIdentifier: Optional[str] = None
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    EngineVersion: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    StorageType: Optional[str] = None
    AllocatedStorage: Optional[int] = None
    Iops: Optional[int] = None


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


# This class is the output for the 'copy_db_cluster_parameter_group' function.
class CopyDBClusterParameterGroupResult(BaseValidatorModel):
    DBClusterParameterGroup: DBClusterParameterGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_cluster_parameter_group' function.
class CreateDBClusterParameterGroupResult(BaseValidatorModel):
    DBClusterParameterGroup: DBClusterParameterGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_cluster_parameter_groups' function.
class DBClusterParameterGroupsMessage(BaseValidatorModel):
    Marker: str
    DBClusterParameterGroups: List[DBClusterParameterGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_db_cluster_snapshot' function.
class CopyDBClusterSnapshotResult(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_cluster_snapshot' function.
class CreateDBClusterSnapshotResult(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_cluster_snapshots' function.
class DBClusterSnapshotMessage(BaseValidatorModel):
    Marker: str
    DBClusterSnapshots: List[DBClusterSnapshot]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_cluster_snapshot' function.
class DeleteDBClusterSnapshotResult(BaseValidatorModel):
    DBClusterSnapshot: DBClusterSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_db_parameter_group' function.
class CopyDBParameterGroupResult(BaseValidatorModel):
    DBParameterGroup: DBParameterGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_parameter_group' function.
class CreateDBParameterGroupResult(BaseValidatorModel):
    DBParameterGroup: DBParameterGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_parameter_groups' function.
class DBParameterGroupsMessage(BaseValidatorModel):
    Marker: str
    DBParameterGroups: List[DBParameterGroup]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_db_cluster' function.
class CreateDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    Engine: str
    AvailabilityZones: Optional[List[str]] = None
    BackupRetentionPeriod: Optional[int] = None
    CharacterSetName: Optional[str] = None
    CopyTagsToSnapshot: Optional[bool] = None
    DatabaseName: Optional[str] = None
    DBClusterParameterGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    DBSubnetGroupName: Optional[str] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    MasterUsername: Optional[str] = None
    MasterUserPassword: Optional[str] = None
    OptionGroupName: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    ReplicationSourceIdentifier: Optional[str] = None
    Tags: Optional[List[Tag]] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    PreSignedUrl: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnableCloudwatchLogsExports: Optional[List[str]] = None
    DeletionProtection: Optional[bool] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration] = None
    GlobalClusterIdentifier: Optional[str] = None
    StorageType: Optional[str] = None
    SourceRegion: Optional[str] = None


# This class is the input for the 'modify_db_cluster' function.
class ModifyDBClusterMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    NewDBClusterIdentifier: Optional[str] = None
    ApplyImmediately: Optional[bool] = None
    BackupRetentionPeriod: Optional[int] = None
    DBClusterParameterGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    Port: Optional[int] = None
    MasterUserPassword: Optional[str] = None
    OptionGroupName: Optional[str] = None
    PreferredBackupWindow: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    CloudwatchLogsExportConfiguration: Optional[CloudwatchLogsExportConfiguration] = None
    EngineVersion: Optional[str] = None
    AllowMajorVersionUpgrade: Optional[bool] = None
    DBInstanceParameterGroupName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    CopyTagsToSnapshot: Optional[bool] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration] = None
    StorageType: Optional[str] = None


# This class is the input for the 'restore_db_cluster_from_snapshot' function.
class RestoreDBClusterFromSnapshotMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    SnapshotIdentifier: str
    Engine: str
    AvailabilityZones: Optional[List[str]] = None
    EngineVersion: Optional[str] = None
    Port: Optional[int] = None
    DBSubnetGroupName: Optional[str] = None
    DatabaseName: Optional[str] = None
    OptionGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    KmsKeyId: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnableCloudwatchLogsExports: Optional[List[str]] = None
    DBClusterParameterGroupName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    CopyTagsToSnapshot: Optional[bool] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration] = None
    StorageType: Optional[str] = None


# This class is the output for the 'describe_db_cluster_endpoints' function.
class DBClusterEndpointMessage(BaseValidatorModel):
    Marker: str
    DBClusterEndpoints: List[DBClusterEndpoint]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_cluster_parameters' function.
class DBClusterParameterGroupDetails(BaseValidatorModel):
    Parameters: List[Parameter]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_parameters' function.
class DBParameterGroupDetails(BaseValidatorModel):
    Parameters: List[Parameter]
    Marker: str
    ResponseMetadata: ResponseMetadata


class EngineDefaults(BaseValidatorModel):
    DBParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[Parameter]] = None


# This class is the input for the 'modify_db_cluster_parameter_group' function.
class ModifyDBClusterParameterGroupMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Parameters: List[Parameter]


# This class is the input for the 'modify_db_parameter_group' function.
class ModifyDBParameterGroupMessage(BaseValidatorModel):
    DBParameterGroupName: str
    Parameters: List[Parameter]


# This class is the input for the 'reset_db_cluster_parameter_group' function.
class ResetDBClusterParameterGroupMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[List[Parameter]] = None


# This class is the input for the 'reset_db_parameter_group' function.
class ResetDBParameterGroupMessage(BaseValidatorModel):
    DBParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    Parameters: Optional[List[Parameter]] = None


class DBClusterSnapshotAttributesResult(BaseValidatorModel):
    DBClusterSnapshotIdentifier: Optional[str] = None
    DBClusterSnapshotAttributes: Optional[List[DBClusterSnapshotAttribute]] = None


class DBEngineVersion(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    DBEngineDescription: Optional[str] = None
    DBEngineVersionDescription: Optional[str] = None
    DefaultCharacterSet: Optional[CharacterSet] = None
    SupportedCharacterSets: Optional[List[CharacterSet]] = None
    ValidUpgradeTarget: Optional[List[UpgradeTarget]] = None
    SupportedTimezones: Optional[List[Timezone]] = None
    ExportableLogTypes: Optional[List[str]] = None
    SupportsLogExportsToCloudwatchLogs: Optional[bool] = None
    SupportsReadReplica: Optional[bool] = None
    SupportsGlobalDatabases: Optional[bool] = None


# This class is the input for the 'describe_db_cluster_endpoints' function.
class DescribeDBClusterEndpointsMessage(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_cluster_parameter_groups' function.
class DescribeDBClusterParameterGroupsMessage(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_cluster_parameters' function.
class DescribeDBClusterParametersMessage(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_cluster_snapshots' function.
class DescribeDBClusterSnapshotsMessage(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None


# This class is the input for the 'describe_db_clusters' function.
class DescribeDBClustersMessage(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_engine_versions' function.
class DescribeDBEngineVersionsMessage(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None


# This class is the input for the 'describe_db_instances' function.
class DescribeDBInstancesMessage(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_parameter_groups' function.
class DescribeDBParameterGroupsMessage(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_parameters' function.
class DescribeDBParametersMessage(BaseValidatorModel):
    DBParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_db_subnet_groups' function.
class DescribeDBSubnetGroupsMessage(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_engine_default_cluster_parameters' function.
class DescribeEngineDefaultClusterParametersMessage(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_engine_default_parameters' function.
class DescribeEngineDefaultParametersMessage(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_event_categories' function.
class DescribeEventCategoriesMessage(BaseValidatorModel):
    SourceType: Optional[str] = None
    Filters: Optional[List[Filter]] = None


# This class is the input for the 'describe_event_subscriptions' function.
class DescribeEventSubscriptionsMessage(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_orderable_db_instance_options' function.
class DescribeOrderableDBInstanceOptionsMessage(BaseValidatorModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_pending_maintenance_actions' function.
class DescribePendingMaintenanceActionsMessage(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceMessage(BaseValidatorModel):
    ResourceName: str
    Filters: Optional[List[Filter]] = None


class DescribeDBClusterEndpointsMessagePaginate(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterEndpointIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClusterParameterGroupsMessagePaginate(BaseValidatorModel):
    DBClusterParameterGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClusterParametersMessagePaginate(BaseValidatorModel):
    DBClusterParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClusterSnapshotsMessagePaginate(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    DBClusterSnapshotIdentifier: Optional[str] = None
    SnapshotType: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    IncludeShared: Optional[bool] = None
    IncludePublic: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBClustersMessagePaginate(BaseValidatorModel):
    DBClusterIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBEngineVersionsMessagePaginate(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    DBParameterGroupFamily: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    DefaultOnly: Optional[bool] = None
    ListSupportedCharacterSets: Optional[bool] = None
    ListSupportedTimezones: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBInstancesMessagePaginate(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBParameterGroupsMessagePaginate(BaseValidatorModel):
    DBParameterGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBParametersMessagePaginate(BaseValidatorModel):
    DBParameterGroupName: str
    Source: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBSubnetGroupsMessagePaginate(BaseValidatorModel):
    DBSubnetGroupName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEngineDefaultParametersMessagePaginate(BaseValidatorModel):
    DBParameterGroupFamily: str
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventSubscriptionsMessagePaginate(BaseValidatorModel):
    SubscriptionName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeGlobalClustersMessagePaginate(BaseValidatorModel):
    GlobalClusterIdentifier: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeOrderableDBInstanceOptionsMessagePaginate(BaseValidatorModel):
    Engine: str
    EngineVersion: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    LicenseModel: Optional[str] = None
    Vpc: Optional[bool] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribePendingMaintenanceActionsMessagePaginate(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDBInstancesMessageWaitExtra(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeDBInstancesMessageWait(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeEventsMessagePaginate(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    EventCategories: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_events' function.
class DescribeEventsMessage(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    EventCategories: Optional[List[str]] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'restore_db_cluster_to_point_in_time' function.
class RestoreDBClusterToPointInTimeMessage(BaseValidatorModel):
    DBClusterIdentifier: str
    SourceDBClusterIdentifier: str
    RestoreType: Optional[str] = None
    RestoreToTime: Optional[Timestamp] = None
    UseLatestRestorableTime: Optional[bool] = None
    Port: Optional[int] = None
    DBSubnetGroupName: Optional[str] = None
    OptionGroupName: Optional[str] = None
    VpcSecurityGroupIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    KmsKeyId: Optional[str] = None
    EnableIAMDatabaseAuthentication: Optional[bool] = None
    EnableCloudwatchLogsExports: Optional[List[str]] = None
    DBClusterParameterGroupName: Optional[str] = None
    DeletionProtection: Optional[bool] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfiguration] = None
    StorageType: Optional[str] = None


# This class is the output for the 'describe_event_categories' function.
class EventCategoriesMessage(BaseValidatorModel):
    EventCategoriesMapList: List[EventCategoriesMap]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_events' function.
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
    StorageEncrypted: Optional[bool] = None
    DeletionProtection: Optional[bool] = None
    GlobalClusterMembers: Optional[List[GlobalClusterMember]] = None


class ResourcePendingMaintenanceActions(BaseValidatorModel):
    ResourceIdentifier: Optional[str] = None
    PendingMaintenanceActionDetails: Optional[List[PendingMaintenanceAction]] = None


class ValidStorageOptions(BaseValidatorModel):
    StorageType: Optional[str] = None
    StorageSize: Optional[List[Range]] = None
    ProvisionedIops: Optional[List[Range]] = None
    IopsToStorageRatio: Optional[List[DoubleRange]] = None


# This class is the output for the 'describe_orderable_db_instance_options' function.
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


class DBCluster(BaseValidatorModel):
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
    DBClusterOptionGroupMemberships: Optional[List[DBClusterOptionGroupStatus]] = None
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
    IAMDatabaseAuthenticationEnabled: Optional[bool] = None
    CloneGroupId: Optional[str] = None
    ClusterCreateTime: Optional[datetime] = None
    CopyTagsToSnapshot: Optional[bool] = None
    EnabledCloudwatchLogsExports: Optional[List[str]] = None
    PendingModifiedValues: Optional[ClusterPendingModifiedValues] = None
    DeletionProtection: Optional[bool] = None
    CrossAccountClone: Optional[bool] = None
    AutomaticRestartTime: Optional[datetime] = None
    ServerlessV2ScalingConfiguration: Optional[ServerlessV2ScalingConfigurationInfo] = None
    GlobalClusterIdentifier: Optional[str] = None
    IOOptimizedNextAllowedModificationTime: Optional[datetime] = None
    StorageType: Optional[str] = None


# This class is the output for the 'describe_engine_default_cluster_parameters' function.
class DescribeEngineDefaultClusterParametersResult(BaseValidatorModel):
    EngineDefaults: EngineDefaults
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_engine_default_parameters' function.
class DescribeEngineDefaultParametersResult(BaseValidatorModel):
    EngineDefaults: EngineDefaults
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_cluster_snapshot_attributes' function.
class DescribeDBClusterSnapshotAttributesResult(BaseValidatorModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResult
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_cluster_snapshot_attribute' function.
class ModifyDBClusterSnapshotAttributeResult(BaseValidatorModel):
    DBClusterSnapshotAttributesResult: DBClusterSnapshotAttributesResult
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_engine_versions' function.
class DBEngineVersionMessage(BaseValidatorModel):
    Marker: str
    DBEngineVersions: List[DBEngineVersion]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_global_cluster' function.
class CreateGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_global_cluster' function.
class DeleteGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'failover_global_cluster' function.
class FailoverGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_global_clusters' function.
class GlobalClustersMessage(BaseValidatorModel):
    Marker: str
    GlobalClusters: List[GlobalCluster]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_global_cluster' function.
class ModifyGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_from_global_cluster' function.
class RemoveFromGlobalClusterResult(BaseValidatorModel):
    GlobalCluster: GlobalCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'apply_pending_maintenance_action' function.
class ApplyPendingMaintenanceActionResult(BaseValidatorModel):
    ResourcePendingMaintenanceActions: ResourcePendingMaintenanceActions
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_pending_maintenance_actions' function.
class PendingMaintenanceActionsMessage(BaseValidatorModel):
    PendingMaintenanceActions: List[ResourcePendingMaintenanceActions]
    Marker: str
    ResponseMetadata: ResponseMetadata


class ValidDBInstanceModificationsMessage(BaseValidatorModel):
    Storage: Optional[List[ValidStorageOptions]] = None


# This class is the output for the 'create_db_subnet_group' function.
class CreateDBSubnetGroupResult(BaseValidatorModel):
    DBSubnetGroup: DBSubnetGroup
    ResponseMetadata: ResponseMetadata


class DBInstance(BaseValidatorModel):
    DBInstanceIdentifier: Optional[str] = None
    DBInstanceClass: Optional[str] = None
    Engine: Optional[str] = None
    DBInstanceStatus: Optional[str] = None
    MasterUsername: Optional[str] = None
    DBName: Optional[str] = None
    Endpoint: Optional[Endpoint] = None
    AllocatedStorage: Optional[int] = None
    InstanceCreateTime: Optional[datetime] = None
    PreferredBackupWindow: Optional[str] = None
    BackupRetentionPeriod: Optional[int] = None
    DBSecurityGroups: Optional[List[DBSecurityGroupMembership]] = None
    VpcSecurityGroups: Optional[List[VpcSecurityGroupMembership]] = None
    DBParameterGroups: Optional[List[DBParameterGroupStatus]] = None
    AvailabilityZone: Optional[str] = None
    DBSubnetGroup: Optional[DBSubnetGroup] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[PendingModifiedValues] = None
    LatestRestorableTime: Optional[datetime] = None
    MultiAZ: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    ReadReplicaSourceDBInstanceIdentifier: Optional[str] = None
    ReadReplicaDBInstanceIdentifiers: Optional[List[str]] = None
    ReadReplicaDBClusterIdentifiers: Optional[List[str]] = None
    LicenseModel: Optional[str] = None
    Iops: Optional[int] = None
    OptionGroupMemberships: Optional[List[OptionGroupMembership]] = None
    CharacterSetName: Optional[str] = None
    SecondaryAvailabilityZone: Optional[str] = None
    PubliclyAccessible: Optional[bool] = None
    StatusInfos: Optional[List[DBInstanceStatusInfo]] = None
    StorageType: Optional[str] = None
    TdeCredentialArn: Optional[str] = None
    DbInstancePort: Optional[int] = None
    DBClusterIdentifier: Optional[str] = None
    StorageEncrypted: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    DbiResourceId: Optional[str] = None
    CACertificateIdentifier: Optional[str] = None
    DomainMemberships: Optional[List[DomainMembership]] = None
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


# This class is the output for the 'describe_db_subnet_groups' function.
class DBSubnetGroupMessage(BaseValidatorModel):
    Marker: str
    DBSubnetGroups: List[DBSubnetGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_subnet_group' function.
class ModifyDBSubnetGroupResult(BaseValidatorModel):
    DBSubnetGroup: DBSubnetGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_cluster' function.
class CreateDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_clusters' function.
class DBClusterMessage(BaseValidatorModel):
    Marker: str
    DBClusters: List[DBCluster]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_cluster' function.
class DeleteDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'failover_db_cluster' function.
class FailoverDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_cluster' function.
class ModifyDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'promote_read_replica_db_cluster' function.
class PromoteReadReplicaDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_db_cluster_from_snapshot' function.
class RestoreDBClusterFromSnapshotResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'restore_db_cluster_to_point_in_time' function.
class RestoreDBClusterToPointInTimeResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_db_cluster' function.
class StartDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_db_cluster' function.
class StopDBClusterResult(BaseValidatorModel):
    DBCluster: DBCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_valid_db_instance_modifications' function.
class DescribeValidDBInstanceModificationsResult(BaseValidatorModel):
    ValidDBInstanceModificationsMessage: ValidDBInstanceModificationsMessage
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_db_instance' function.
class CreateDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_db_instances' function.
class DBInstanceMessage(BaseValidatorModel):
    Marker: str
    DBInstances: List[DBInstance]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_db_instance' function.
class DeleteDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_db_instance' function.
class ModifyDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reboot_db_instance' function.
class RebootDBInstanceResult(BaseValidatorModel):
    DBInstance: DBInstance
    ResponseMetadata: ResponseMetadata