from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.elasticache.elasticache_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AuthenticationMode(BaseValidatorModel):
    Type: Optional[InputAuthenticationTypeType] = None
    Passwords: Optional[List[str]] = None


class Authentication(BaseValidatorModel):
    Type: Optional[AuthenticationTypeType] = None
    PasswordCount: Optional[int] = None


# This class is the input for the 'authorize_cache_security_group_ingress' function.
class AuthorizeCacheSecurityGroupIngressMessage(BaseValidatorModel):
    CacheSecurityGroupName: str
    EC2SecurityGroupName: str
    EC2SecurityGroupOwnerId: str


class AvailabilityZone(BaseValidatorModel):
    Name: Optional[str] = None


# This class is the input for the 'batch_apply_update_action' function.
class BatchApplyUpdateActionMessage(BaseValidatorModel):
    ServiceUpdateName: str
    ReplicationGroupIds: Optional[List[str]] = None
    CacheClusterIds: Optional[List[str]] = None


# This class is the input for the 'batch_stop_update_action' function.
class BatchStopUpdateActionMessage(BaseValidatorModel):
    ServiceUpdateName: str
    ReplicationGroupIds: Optional[List[str]] = None
    CacheClusterIds: Optional[List[str]] = None


class CacheParameterGroupStatus(BaseValidatorModel):
    CacheParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    CacheNodeIdsToReboot: Optional[List[str]] = None


class CacheSecurityGroupMembership(BaseValidatorModel):
    CacheSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None


class Endpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None


class NotificationConfiguration(BaseValidatorModel):
    TopicArn: Optional[str] = None
    TopicStatus: Optional[str] = None


class SecurityGroupMembership(BaseValidatorModel):
    SecurityGroupId: Optional[str] = None
    Status: Optional[str] = None


class CacheEngineVersion(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupFamily: Optional[str] = None
    CacheEngineDescription: Optional[str] = None
    CacheEngineVersionDescription: Optional[str] = None


class CacheNodeTypeSpecificValue(BaseValidatorModel):
    CacheNodeType: Optional[str] = None
    Value: Optional[str] = None


class CacheNodeUpdateStatus(BaseValidatorModel):
    CacheNodeId: Optional[str] = None
    NodeUpdateStatus: Optional[NodeUpdateStatusType] = None
    NodeDeletionDate: Optional[datetime] = None
    NodeUpdateStartDate: Optional[datetime] = None
    NodeUpdateEndDate: Optional[datetime] = None
    NodeUpdateInitiatedBy: Optional[NodeUpdateInitiatedByType] = None
    NodeUpdateInitiatedDate: Optional[datetime] = None
    NodeUpdateStatusModifiedDate: Optional[datetime] = None


class Parameter(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None
    ChangeType: Optional[ChangeTypeType] = None


class CacheParameterGroup(BaseValidatorModel):
    CacheParameterGroupName: Optional[str] = None
    CacheParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    IsGlobal: Optional[bool] = None
    ARN: Optional[str] = None


class EC2SecurityGroup(BaseValidatorModel):
    Status: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None


class DataStorage(BaseValidatorModel):
    Unit: Literal['GB']
    Maximum: Optional[int] = None
    Minimum: Optional[int] = None


class ECPUPerSecond(BaseValidatorModel):
    Maximum: Optional[int] = None
    Minimum: Optional[int] = None


class CloudWatchLogsDestinationDetails(BaseValidatorModel):
    LogGroup: Optional[str] = None


# This class is the input for the 'complete_migration' function.
class CompleteMigrationMessage(BaseValidatorModel):
    ReplicationGroupId: str
    Force: Optional[bool] = None


class ConfigureShard(BaseValidatorModel):
    NodeGroupId: str
    NewReplicaCount: int
    PreferredAvailabilityZones: Optional[List[str]] = None
    PreferredOutpostArns: Optional[List[str]] = None


# This class is the input for the 'create_global_replication_group' function.
class CreateGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupIdSuffix: str
    PrimaryReplicationGroupId: str
    GlobalReplicationGroupDescription: Optional[str] = None


class CustomerNodeEndpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None


# This class is the input for the 'decrease_node_groups_in_global_replication_group' function.
class DecreaseNodeGroupsInGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    GlobalNodeGroupsToRemove: Optional[List[str]] = None
    GlobalNodeGroupsToRetain: Optional[List[str]] = None


# This class is the input for the 'delete_cache_cluster' function.
class DeleteCacheClusterMessage(BaseValidatorModel):
    CacheClusterId: str
    FinalSnapshotIdentifier: Optional[str] = None


# This class is the input for the 'delete_cache_parameter_group' function.
class DeleteCacheParameterGroupMessage(BaseValidatorModel):
    CacheParameterGroupName: str


# This class is the input for the 'delete_cache_security_group' function.
class DeleteCacheSecurityGroupMessage(BaseValidatorModel):
    CacheSecurityGroupName: str


# This class is the input for the 'delete_cache_subnet_group' function.
class DeleteCacheSubnetGroupMessage(BaseValidatorModel):
    CacheSubnetGroupName: str


# This class is the input for the 'delete_global_replication_group' function.
class DeleteGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupId: str
    RetainPrimaryReplicationGroup: bool


# This class is the input for the 'delete_replication_group' function.
class DeleteReplicationGroupMessage(BaseValidatorModel):
    ReplicationGroupId: str
    RetainPrimaryCluster: Optional[bool] = None
    FinalSnapshotIdentifier: Optional[str] = None


# This class is the input for the 'delete_serverless_cache' function.
class DeleteServerlessCacheRequest(BaseValidatorModel):
    ServerlessCacheName: str
    FinalSnapshotName: Optional[str] = None


# This class is the input for the 'delete_serverless_cache_snapshot' function.
class DeleteServerlessCacheSnapshotRequest(BaseValidatorModel):
    ServerlessCacheSnapshotName: str


# This class is the input for the 'delete_snapshot' function.
class DeleteSnapshotMessage(BaseValidatorModel):
    SnapshotName: str


# This class is the input for the 'delete_user_group' function.
class DeleteUserGroupMessage(BaseValidatorModel):
    UserGroupId: str


# This class is the input for the 'delete_user' function.
class DeleteUserMessage(BaseValidatorModel):
    UserId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_cache_clusters' function.
class DescribeCacheClustersMessage(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowCacheNodeInfo: Optional[bool] = None
    ShowCacheClustersNotInReplicationGroups: Optional[bool] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_cache_engine_versions' function.
class DescribeCacheEngineVersionsMessage(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupFamily: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DefaultOnly: Optional[bool] = None


# This class is the input for the 'describe_cache_parameter_groups' function.
class DescribeCacheParameterGroupsMessage(BaseValidatorModel):
    CacheParameterGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_cache_parameters' function.
class DescribeCacheParametersMessage(BaseValidatorModel):
    CacheParameterGroupName: str
    Source: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_cache_security_groups' function.
class DescribeCacheSecurityGroupsMessage(BaseValidatorModel):
    CacheSecurityGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_cache_subnet_groups' function.
class DescribeCacheSubnetGroupsMessage(BaseValidatorModel):
    CacheSubnetGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_engine_default_parameters' function.
class DescribeEngineDefaultParametersMessage(BaseValidatorModel):
    CacheParameterGroupFamily: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'describe_global_replication_groups' function.
class DescribeGlobalReplicationGroupsMessage(BaseValidatorModel):
    GlobalReplicationGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowMemberInfo: Optional[bool] = None


# This class is the input for the 'describe_replication_groups' function.
class DescribeReplicationGroupsMessage(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_reserved_cache_nodes' function.
class DescribeReservedCacheNodesMessage(BaseValidatorModel):
    ReservedCacheNodeId: Optional[str] = None
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_reserved_cache_nodes_offerings' function.
class DescribeReservedCacheNodesOfferingsMessage(BaseValidatorModel):
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_serverless_cache_snapshots' function.
class DescribeServerlessCacheSnapshotsRequest(BaseValidatorModel):
    ServerlessCacheName: Optional[str] = None
    ServerlessCacheSnapshotName: Optional[str] = None
    SnapshotType: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'describe_serverless_caches' function.
class DescribeServerlessCachesRequest(BaseValidatorModel):
    ServerlessCacheName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_service_updates' function.
class DescribeServiceUpdatesMessage(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ServiceUpdateStatus: Optional[List[ServiceUpdateStatusType]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


# This class is the input for the 'describe_snapshots' function.
class DescribeSnapshotsMessage(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    SnapshotName: Optional[str] = None
    SnapshotSource: Optional[str] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    ShowNodeGroupConfig: Optional[bool] = None


# This class is the input for the 'describe_user_groups' function.
class DescribeUserGroupsMessage(BaseValidatorModel):
    UserGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class Filter(BaseValidatorModel):
    Name: str
    Values: List[str]


class KinesisFirehoseDestinationDetails(BaseValidatorModel):
    DeliveryStream: Optional[str] = None


# This class is the input for the 'disassociate_global_replication_group' function.
class DisassociateGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupId: str
    ReplicationGroupId: str
    ReplicationGroupRegion: str


class Event(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    Date: Optional[datetime] = None


# This class is the input for the 'export_serverless_cache_snapshot' function.
class ExportServerlessCacheSnapshotRequest(BaseValidatorModel):
    ServerlessCacheSnapshotName: str
    S3BucketName: str


# This class is the input for the 'failover_global_replication_group' function.
class FailoverGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupId: str
    PrimaryRegion: str
    PrimaryReplicationGroupId: str


class GlobalNodeGroup(BaseValidatorModel):
    GlobalNodeGroupId: Optional[str] = None
    Slots: Optional[str] = None


class GlobalReplicationGroupInfo(BaseValidatorModel):
    GlobalReplicationGroupId: Optional[str] = None
    GlobalReplicationGroupMemberRole: Optional[str] = None


class GlobalReplicationGroupMember(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    ReplicationGroupRegion: Optional[str] = None
    Role: Optional[str] = None
    AutomaticFailover: Optional[AutomaticFailoverStatusType] = None
    Status: Optional[str] = None


# This class is the input for the 'list_allowed_node_type_modifications' function.
class ListAllowedNodeTypeModificationsMessage(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    ReplicationGroupId: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceMessage(BaseValidatorModel):
    ResourceName: str


class ParameterNameValue(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None


# This class is the input for the 'modify_cache_subnet_group' function.
class ModifyCacheSubnetGroupMessage(BaseValidatorModel):
    CacheSubnetGroupName: str
    CacheSubnetGroupDescription: Optional[str] = None
    SubnetIds: Optional[List[str]] = None


# This class is the input for the 'modify_global_replication_group' function.
class ModifyGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupId: str
    ApplyImmediately: bool
    CacheNodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupName: Optional[str] = None
    GlobalReplicationGroupDescription: Optional[str] = None
    AutomaticFailoverEnabled: Optional[bool] = None


class ReshardingConfiguration(BaseValidatorModel):
    NodeGroupId: Optional[str] = None
    PreferredAvailabilityZones: Optional[List[str]] = None


# This class is the input for the 'modify_user_group' function.
class ModifyUserGroupMessage(BaseValidatorModel):
    UserGroupId: str
    UserIdsToAdd: Optional[List[str]] = None
    UserIdsToRemove: Optional[List[str]] = None
    Engine: Optional[str] = None


class NodeGroupConfigurationOutput(BaseValidatorModel):
    NodeGroupId: Optional[str] = None
    Slots: Optional[str] = None
    ReplicaCount: Optional[int] = None
    PrimaryAvailabilityZone: Optional[str] = None
    ReplicaAvailabilityZones: Optional[List[str]] = None
    PrimaryOutpostArn: Optional[str] = None
    ReplicaOutpostArns: Optional[List[str]] = None


class NodeGroupConfiguration(BaseValidatorModel):
    NodeGroupId: Optional[str] = None
    Slots: Optional[str] = None
    ReplicaCount: Optional[int] = None
    PrimaryAvailabilityZone: Optional[str] = None
    ReplicaAvailabilityZones: Optional[List[str]] = None
    PrimaryOutpostArn: Optional[str] = None
    ReplicaOutpostArns: Optional[List[str]] = None


class NodeGroupMemberUpdateStatus(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    CacheNodeId: Optional[str] = None
    NodeUpdateStatus: Optional[NodeUpdateStatusType] = None
    NodeDeletionDate: Optional[datetime] = None
    NodeUpdateStartDate: Optional[datetime] = None
    NodeUpdateEndDate: Optional[datetime] = None
    NodeUpdateInitiatedBy: Optional[NodeUpdateInitiatedByType] = None
    NodeUpdateInitiatedDate: Optional[datetime] = None
    NodeUpdateStatusModifiedDate: Optional[datetime] = None


class ProcessedUpdateAction(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    ServiceUpdateName: Optional[str] = None
    UpdateActionStatus: Optional[UpdateActionStatusType] = None


# This class is the input for the 'rebalance_slots_in_global_replication_group' function.
class RebalanceSlotsInGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupId: str
    ApplyImmediately: bool


# This class is the input for the 'reboot_cache_cluster' function.
class RebootCacheClusterMessage(BaseValidatorModel):
    CacheClusterId: str
    CacheNodeIdsToReboot: List[str]


class RecurringCharge(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None


# This class is the input for the 'remove_tags_from_resource' function.
class RemoveTagsFromResourceMessage(BaseValidatorModel):
    ResourceName: str
    TagKeys: List[str]


class UserGroupsUpdateStatus(BaseValidatorModel):
    UserGroupIdsToAdd: Optional[List[str]] = None
    UserGroupIdsToRemove: Optional[List[str]] = None


class SlotMigration(BaseValidatorModel):
    ProgressPercentage: Optional[float] = None


# This class is the input for the 'revoke_cache_security_group_ingress' function.
class RevokeCacheSecurityGroupIngressMessage(BaseValidatorModel):
    CacheSecurityGroupName: str
    EC2SecurityGroupName: str
    EC2SecurityGroupOwnerId: str


class ServerlessCacheConfiguration(BaseValidatorModel):
    ServerlessCacheName: Optional[str] = None
    Engine: Optional[str] = None
    MajorEngineVersion: Optional[str] = None


class ServiceUpdate(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ServiceUpdateReleaseDate: Optional[datetime] = None
    ServiceUpdateEndDate: Optional[datetime] = None
    ServiceUpdateSeverity: Optional[ServiceUpdateSeverityType] = None
    ServiceUpdateRecommendedApplyByDate: Optional[datetime] = None
    ServiceUpdateStatus: Optional[ServiceUpdateStatusType] = None
    ServiceUpdateDescription: Optional[str] = None
    ServiceUpdateType: Optional[Literal['security-update']] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    AutoUpdateAfterRecommendedApplyByDate: Optional[bool] = None
    EstimatedUpdateTime: Optional[str] = None


class SubnetOutpost(BaseValidatorModel):
    SubnetOutpostArn: Optional[str] = None


# This class is the input for the 'test_failover' function.
class TestFailoverMessage(BaseValidatorModel):
    ReplicationGroupId: str
    NodeGroupId: str


class UnprocessedUpdateAction(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    ServiceUpdateName: Optional[str] = None
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None


class UserGroupPendingChanges(BaseValidatorModel):
    UserIdsToRemove: Optional[List[str]] = None
    UserIdsToAdd: Optional[List[str]] = None


# This class is the input for the 'add_tags_to_resource' function.
class AddTagsToResourceMessage(BaseValidatorModel):
    ResourceName: str
    Tags: List[Tag]


# This class is the input for the 'copy_serverless_cache_snapshot' function.
class CopyServerlessCacheSnapshotRequest(BaseValidatorModel):
    SourceServerlessCacheSnapshotName: str
    TargetServerlessCacheSnapshotName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'copy_snapshot' function.
class CopySnapshotMessage(BaseValidatorModel):
    SourceSnapshotName: str
    TargetSnapshotName: str
    TargetBucket: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_cache_parameter_group' function.
class CreateCacheParameterGroupMessage(BaseValidatorModel):
    CacheParameterGroupName: str
    CacheParameterGroupFamily: str
    Description: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_cache_security_group' function.
class CreateCacheSecurityGroupMessage(BaseValidatorModel):
    CacheSecurityGroupName: str
    Description: str
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_cache_subnet_group' function.
class CreateCacheSubnetGroupMessage(BaseValidatorModel):
    CacheSubnetGroupName: str
    CacheSubnetGroupDescription: str
    SubnetIds: List[str]
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_serverless_cache_snapshot' function.
class CreateServerlessCacheSnapshotRequest(BaseValidatorModel):
    ServerlessCacheSnapshotName: str
    ServerlessCacheName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_snapshot' function.
class CreateSnapshotMessage(BaseValidatorModel):
    SnapshotName: str
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_user_group' function.
class CreateUserGroupMessage(BaseValidatorModel):
    UserGroupId: str
    Engine: str
    UserIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'purchase_reserved_cache_nodes_offering' function.
class PurchaseReservedCacheNodesOfferingMessage(BaseValidatorModel):
    ReservedCacheNodesOfferingId: str
    ReservedCacheNodeId: Optional[str] = None
    CacheNodeCount: Optional[int] = None
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_allowed_node_type_modifications' function.
class AllowedNodeTypeModificationsMessage(BaseValidatorModel):
    ScaleUpModifications: List[str]
    ScaleDownModifications: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reset_cache_parameter_group' function.
class CacheParameterGroupNameMessage(BaseValidatorModel):
    CacheParameterGroupName: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_cache_subnet_group' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'remove_tags_from_resource' function.
class TagListMessage(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_user' function.
class CreateUserMessage(BaseValidatorModel):
    UserId: str
    UserName: str
    Engine: str
    AccessString: str
    Passwords: Optional[List[str]] = None
    NoPasswordRequired: Optional[bool] = None
    Tags: Optional[List[Tag]] = None
    AuthenticationMode: Optional[AuthenticationMode] = None


# This class is the input for the 'modify_user' function.
class ModifyUserMessage(BaseValidatorModel):
    UserId: str
    AccessString: Optional[str] = None
    AppendAccessString: Optional[str] = None
    Passwords: Optional[List[str]] = None
    NoPasswordRequired: Optional[bool] = None
    AuthenticationMode: Optional[AuthenticationMode] = None
    Engine: Optional[str] = None


# This class is the output for the 'modify_user' function.
class UserResponse(BaseValidatorModel):
    UserId: str
    UserName: str
    Status: str
    Engine: str
    MinimumEngineVersion: str
    AccessString: str
    UserGroupIds: List[str]
    Authentication: Authentication
    ARN: str
    ResponseMetadata: ResponseMetadata


class User(BaseValidatorModel):
    UserId: Optional[str] = None
    UserName: Optional[str] = None
    Status: Optional[str] = None
    Engine: Optional[str] = None
    MinimumEngineVersion: Optional[str] = None
    AccessString: Optional[str] = None
    UserGroupIds: Optional[List[str]] = None
    Authentication: Optional[Authentication] = None
    ARN: Optional[str] = None


class CacheNode(BaseValidatorModel):
    CacheNodeId: Optional[str] = None
    CacheNodeStatus: Optional[str] = None
    CacheNodeCreateTime: Optional[datetime] = None
    Endpoint: Optional[Endpoint] = None
    ParameterGroupStatus: Optional[str] = None
    SourceCacheNodeId: Optional[str] = None
    CustomerAvailabilityZone: Optional[str] = None
    CustomerOutpostArn: Optional[str] = None


class NodeGroupMember(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    CacheNodeId: Optional[str] = None
    ReadEndpoint: Optional[Endpoint] = None
    PreferredAvailabilityZone: Optional[str] = None
    PreferredOutpostArn: Optional[str] = None
    CurrentRole: Optional[str] = None


# This class is the output for the 'describe_cache_engine_versions' function.
class CacheEngineVersionMessage(BaseValidatorModel):
    Marker: str
    CacheEngineVersions: List[CacheEngineVersion]
    ResponseMetadata: ResponseMetadata


class CacheNodeTypeSpecificParameter(BaseValidatorModel):
    ParameterName: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None
    CacheNodeTypeSpecificValues: Optional[List[CacheNodeTypeSpecificValue]] = None
    ChangeType: Optional[ChangeTypeType] = None


# This class is the output for the 'describe_cache_parameter_groups' function.
class CacheParameterGroupsMessage(BaseValidatorModel):
    Marker: str
    CacheParameterGroups: List[CacheParameterGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cache_parameter_group' function.
class CreateCacheParameterGroupResult(BaseValidatorModel):
    CacheParameterGroup: CacheParameterGroup
    ResponseMetadata: ResponseMetadata


class CacheSecurityGroup(BaseValidatorModel):
    OwnerId: Optional[str] = None
    CacheSecurityGroupName: Optional[str] = None
    Description: Optional[str] = None
    EC2SecurityGroups: Optional[List[EC2SecurityGroup]] = None
    ARN: Optional[str] = None


class CacheUsageLimits(BaseValidatorModel):
    DataStorage: Optional[DataStorage] = None
    ECPUPerSecond: Optional[ECPUPerSecond] = None


# This class is the input for the 'decrease_replica_count' function.
class DecreaseReplicaCountMessage(BaseValidatorModel):
    ReplicationGroupId: str
    ApplyImmediately: bool
    NewReplicaCount: Optional[int] = None
    ReplicaConfiguration: Optional[List[ConfigureShard]] = None
    ReplicasToRemove: Optional[List[str]] = None


# This class is the input for the 'increase_replica_count' function.
class IncreaseReplicaCountMessage(BaseValidatorModel):
    ReplicationGroupId: str
    ApplyImmediately: bool
    NewReplicaCount: Optional[int] = None
    ReplicaConfiguration: Optional[List[ConfigureShard]] = None


# This class is the input for the 'start_migration' function.
class StartMigrationMessage(BaseValidatorModel):
    ReplicationGroupId: str
    CustomerNodeEndpointList: List[CustomerNodeEndpoint]


# This class is the input for the 'test_migration' function.
class TestMigrationMessage(BaseValidatorModel):
    ReplicationGroupId: str
    CustomerNodeEndpointList: List[CustomerNodeEndpoint]


class DescribeCacheClustersMessagePaginate(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    ShowCacheNodeInfo: Optional[bool] = None
    ShowCacheClustersNotInReplicationGroups: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeCacheEngineVersionsMessagePaginate(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupFamily: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeCacheParameterGroupsMessagePaginate(BaseValidatorModel):
    CacheParameterGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeCacheParametersMessagePaginate(BaseValidatorModel):
    CacheParameterGroupName: str
    Source: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeCacheSecurityGroupsMessagePaginate(BaseValidatorModel):
    CacheSecurityGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeCacheSubnetGroupsMessagePaginate(BaseValidatorModel):
    CacheSubnetGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEngineDefaultParametersMessagePaginate(BaseValidatorModel):
    CacheParameterGroupFamily: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeGlobalReplicationGroupsMessagePaginate(BaseValidatorModel):
    GlobalReplicationGroupId: Optional[str] = None
    ShowMemberInfo: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReplicationGroupsMessagePaginate(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedCacheNodesMessagePaginate(BaseValidatorModel):
    ReservedCacheNodeId: Optional[str] = None
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedCacheNodesOfferingsMessagePaginate(BaseValidatorModel):
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeServerlessCacheSnapshotsRequestPaginate(BaseValidatorModel):
    ServerlessCacheName: Optional[str] = None
    ServerlessCacheSnapshotName: Optional[str] = None
    SnapshotType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeServerlessCachesRequestPaginate(BaseValidatorModel):
    ServerlessCacheName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeServiceUpdatesMessagePaginate(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ServiceUpdateStatus: Optional[List[ServiceUpdateStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSnapshotsMessagePaginate(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    SnapshotName: Optional[str] = None
    SnapshotSource: Optional[str] = None
    ShowNodeGroupConfig: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeUserGroupsMessagePaginate(BaseValidatorModel):
    UserGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeCacheClustersMessageWaitExtra(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowCacheNodeInfo: Optional[bool] = None
    ShowCacheClustersNotInReplicationGroups: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeCacheClustersMessageWait(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowCacheNodeInfo: Optional[bool] = None
    ShowCacheClustersNotInReplicationGroups: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeReplicationGroupsMessageWaitExtra(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeReplicationGroupsMessageWait(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeEventsMessagePaginate(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_events' function.
class DescribeEventsMessage(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class TimeRangeFilter(BaseValidatorModel):
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None


class DescribeUsersMessagePaginate(BaseValidatorModel):
    Engine: Optional[str] = None
    UserId: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_users' function.
class DescribeUsersMessage(BaseValidatorModel):
    Engine: Optional[str] = None
    UserId: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DestinationDetails(BaseValidatorModel):
    CloudWatchLogsDetails: Optional[CloudWatchLogsDestinationDetails] = None
    KinesisFirehoseDetails: Optional[KinesisFirehoseDestinationDetails] = None


# This class is the output for the 'describe_events' function.
class EventsMessage(BaseValidatorModel):
    Marker: str
    Events: List[Event]
    ResponseMetadata: ResponseMetadata


class GlobalReplicationGroup(BaseValidatorModel):
    GlobalReplicationGroupId: Optional[str] = None
    GlobalReplicationGroupDescription: Optional[str] = None
    Status: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    Members: Optional[List[GlobalReplicationGroupMember]] = None
    ClusterEnabled: Optional[bool] = None
    GlobalNodeGroups: Optional[List[GlobalNodeGroup]] = None
    AuthTokenEnabled: Optional[bool] = None
    TransitEncryptionEnabled: Optional[bool] = None
    AtRestEncryptionEnabled: Optional[bool] = None
    ARN: Optional[str] = None


# This class is the input for the 'modify_cache_parameter_group' function.
class ModifyCacheParameterGroupMessage(BaseValidatorModel):
    CacheParameterGroupName: str
    ParameterNameValues: List[ParameterNameValue]


# This class is the input for the 'reset_cache_parameter_group' function.
class ResetCacheParameterGroupMessage(BaseValidatorModel):
    CacheParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    ParameterNameValues: Optional[List[ParameterNameValue]] = None


# This class is the input for the 'modify_replication_group_shard_configuration' function.
class ModifyReplicationGroupShardConfigurationMessage(BaseValidatorModel):
    ReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    ReshardingConfiguration: Optional[List[ReshardingConfiguration]] = None
    NodeGroupsToRemove: Optional[List[str]] = None
    NodeGroupsToRetain: Optional[List[str]] = None


class RegionalConfiguration(BaseValidatorModel):
    ReplicationGroupId: str
    ReplicationGroupRegion: str
    ReshardingConfiguration: List[ReshardingConfiguration]


class NodeSnapshot(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    NodeGroupId: Optional[str] = None
    CacheNodeId: Optional[str] = None
    NodeGroupConfiguration: Optional[NodeGroupConfigurationOutput] = None
    CacheSize: Optional[str] = None
    CacheNodeCreateTime: Optional[datetime] = None
    SnapshotCreateTime: Optional[datetime] = None

NodeGroupConfigurationUnion = Union[NodeGroupConfiguration, NodeGroupConfigurationOutput]


class NodeGroupUpdateStatus(BaseValidatorModel):
    NodeGroupId: Optional[str] = None
    NodeGroupMemberUpdateStatus: Optional[List[NodeGroupMemberUpdateStatus]] = None


class ReservedCacheNode(BaseValidatorModel):
    ReservedCacheNodeId: Optional[str] = None
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    StartTime: Optional[datetime] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    CacheNodeCount: Optional[int] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    State: Optional[str] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None
    ReservationARN: Optional[str] = None


class ReservedCacheNodesOffering(BaseValidatorModel):
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None


class ReshardingStatus(BaseValidatorModel):
    SlotMigration: Optional[SlotMigration] = None


class ServerlessCacheSnapshot(BaseValidatorModel):
    ServerlessCacheSnapshotName: Optional[str] = None
    ARN: Optional[str] = None
    KmsKeyId: Optional[str] = None
    SnapshotType: Optional[str] = None
    Status: Optional[str] = None
    CreateTime: Optional[datetime] = None
    ExpiryTime: Optional[datetime] = None
    BytesUsedForCache: Optional[str] = None
    ServerlessCacheConfiguration: Optional[ServerlessCacheConfiguration] = None


# This class is the output for the 'describe_service_updates' function.
class ServiceUpdatesMessage(BaseValidatorModel):
    Marker: str
    ServiceUpdates: List[ServiceUpdate]
    ResponseMetadata: ResponseMetadata


class Subnet(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZone] = None
    SubnetOutpost: Optional[SubnetOutpost] = None
    SupportedNetworkTypes: Optional[List[NetworkTypeType]] = None


# This class is the output for the 'batch_stop_update_action' function.
class UpdateActionResultsMessage(BaseValidatorModel):
    ProcessedUpdateActions: List[ProcessedUpdateAction]
    UnprocessedUpdateActions: List[UnprocessedUpdateAction]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_user_group' function.
class UserGroupResponse(BaseValidatorModel):
    UserGroupId: str
    Status: str
    Engine: str
    UserIds: List[str]
    MinimumEngineVersion: str
    PendingChanges: UserGroupPendingChanges
    ReplicationGroups: List[str]
    ServerlessCaches: List[str]
    ARN: str
    ResponseMetadata: ResponseMetadata


class UserGroup(BaseValidatorModel):
    UserGroupId: Optional[str] = None
    Status: Optional[str] = None
    Engine: Optional[str] = None
    UserIds: Optional[List[str]] = None
    MinimumEngineVersion: Optional[str] = None
    PendingChanges: Optional[UserGroupPendingChanges] = None
    ReplicationGroups: Optional[List[str]] = None
    ServerlessCaches: Optional[List[str]] = None
    ARN: Optional[str] = None


# This class is the output for the 'describe_users' function.
class DescribeUsersResult(BaseValidatorModel):
    Users: List[User]
    Marker: str
    ResponseMetadata: ResponseMetadata


class NodeGroup(BaseValidatorModel):
    NodeGroupId: Optional[str] = None
    Status: Optional[str] = None
    PrimaryEndpoint: Optional[Endpoint] = None
    ReaderEndpoint: Optional[Endpoint] = None
    Slots: Optional[str] = None
    NodeGroupMembers: Optional[List[NodeGroupMember]] = None


# This class is the output for the 'describe_cache_parameters' function.
class CacheParameterGroupDetails(BaseValidatorModel):
    Marker: str
    Parameters: List[Parameter]
    CacheNodeTypeSpecificParameters: List[CacheNodeTypeSpecificParameter]
    ResponseMetadata: ResponseMetadata


class EngineDefaults(BaseValidatorModel):
    CacheParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[Parameter]] = None
    CacheNodeTypeSpecificParameters: Optional[List[CacheNodeTypeSpecificParameter]] = None


# This class is the output for the 'authorize_cache_security_group_ingress' function.
class AuthorizeCacheSecurityGroupIngressResult(BaseValidatorModel):
    CacheSecurityGroup: CacheSecurityGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_cache_security_groups' function.
class CacheSecurityGroupMessage(BaseValidatorModel):
    Marker: str
    CacheSecurityGroups: List[CacheSecurityGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cache_security_group' function.
class CreateCacheSecurityGroupResult(BaseValidatorModel):
    CacheSecurityGroup: CacheSecurityGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'revoke_cache_security_group_ingress' function.
class RevokeCacheSecurityGroupIngressResult(BaseValidatorModel):
    CacheSecurityGroup: CacheSecurityGroup
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_serverless_cache' function.
class CreateServerlessCacheRequest(BaseValidatorModel):
    ServerlessCacheName: str
    Engine: str
    Description: Optional[str] = None
    MajorEngineVersion: Optional[str] = None
    CacheUsageLimits: Optional[CacheUsageLimits] = None
    KmsKeyId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    SnapshotArnsToRestore: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    UserGroupId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    SnapshotRetentionLimit: Optional[int] = None
    DailySnapshotTime: Optional[str] = None


# This class is the input for the 'modify_serverless_cache' function.
class ModifyServerlessCacheRequest(BaseValidatorModel):
    ServerlessCacheName: str
    Description: Optional[str] = None
    CacheUsageLimits: Optional[CacheUsageLimits] = None
    RemoveUserGroup: Optional[bool] = None
    UserGroupId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    SnapshotRetentionLimit: Optional[int] = None
    DailySnapshotTime: Optional[str] = None
    Engine: Optional[str] = None
    MajorEngineVersion: Optional[str] = None


class ServerlessCache(BaseValidatorModel):
    ServerlessCacheName: Optional[str] = None
    Description: Optional[str] = None
    CreateTime: Optional[datetime] = None
    Status: Optional[str] = None
    Engine: Optional[str] = None
    MajorEngineVersion: Optional[str] = None
    FullEngineVersion: Optional[str] = None
    CacheUsageLimits: Optional[CacheUsageLimits] = None
    KmsKeyId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    Endpoint: Optional[Endpoint] = None
    ReaderEndpoint: Optional[Endpoint] = None
    ARN: Optional[str] = None
    UserGroupId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    SnapshotRetentionLimit: Optional[int] = None
    DailySnapshotTime: Optional[str] = None


class DescribeUpdateActionsMessagePaginate(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ReplicationGroupIds: Optional[List[str]] = None
    CacheClusterIds: Optional[List[str]] = None
    Engine: Optional[str] = None
    ServiceUpdateStatus: Optional[List[ServiceUpdateStatusType]] = None
    ServiceUpdateTimeRange: Optional[TimeRangeFilter] = None
    UpdateActionStatus: Optional[List[UpdateActionStatusType]] = None
    ShowNodeLevelUpdateStatus: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_update_actions' function.
class DescribeUpdateActionsMessage(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ReplicationGroupIds: Optional[List[str]] = None
    CacheClusterIds: Optional[List[str]] = None
    Engine: Optional[str] = None
    ServiceUpdateStatus: Optional[List[ServiceUpdateStatusType]] = None
    ServiceUpdateTimeRange: Optional[TimeRangeFilter] = None
    UpdateActionStatus: Optional[List[UpdateActionStatusType]] = None
    ShowNodeLevelUpdateStatus: Optional[bool] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class LogDeliveryConfigurationRequest(BaseValidatorModel):
    LogType: Optional[LogTypeType] = None
    DestinationType: Optional[DestinationTypeType] = None
    DestinationDetails: Optional[DestinationDetails] = None
    LogFormat: Optional[LogFormatType] = None
    Enabled: Optional[bool] = None


class LogDeliveryConfiguration(BaseValidatorModel):
    LogType: Optional[LogTypeType] = None
    DestinationType: Optional[DestinationTypeType] = None
    DestinationDetails: Optional[DestinationDetails] = None
    LogFormat: Optional[LogFormatType] = None
    Status: Optional[LogDeliveryConfigurationStatusType] = None
    Message: Optional[str] = None


class PendingLogDeliveryConfiguration(BaseValidatorModel):
    LogType: Optional[LogTypeType] = None
    DestinationType: Optional[DestinationTypeType] = None
    DestinationDetails: Optional[DestinationDetails] = None
    LogFormat: Optional[LogFormatType] = None


# This class is the output for the 'create_global_replication_group' function.
class CreateGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'decrease_node_groups_in_global_replication_group' function.
class DecreaseNodeGroupsInGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_global_replication_group' function.
class DeleteGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_global_replication_groups' function.
class DescribeGlobalReplicationGroupsResult(BaseValidatorModel):
    Marker: str
    GlobalReplicationGroups: List[GlobalReplicationGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_global_replication_group' function.
class DisassociateGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'failover_global_replication_group' function.
class FailoverGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'increase_node_groups_in_global_replication_group' function.
class IncreaseNodeGroupsInGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_global_replication_group' function.
class ModifyGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'rebalance_slots_in_global_replication_group' function.
class RebalanceSlotsInGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'increase_node_groups_in_global_replication_group' function.
class IncreaseNodeGroupsInGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    RegionalConfigurations: Optional[List[RegionalConfiguration]] = None


class Snapshot(BaseValidatorModel):
    SnapshotName: Optional[str] = None
    ReplicationGroupId: Optional[str] = None
    ReplicationGroupDescription: Optional[str] = None
    CacheClusterId: Optional[str] = None
    SnapshotStatus: Optional[str] = None
    SnapshotSource: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    NumCacheNodes: Optional[int] = None
    PreferredAvailabilityZone: Optional[str] = None
    PreferredOutpostArn: Optional[str] = None
    CacheClusterCreateTime: Optional[datetime] = None
    PreferredMaintenanceWindow: Optional[str] = None
    TopicArn: Optional[str] = None
    Port: Optional[int] = None
    CacheParameterGroupName: Optional[str] = None
    CacheSubnetGroupName: Optional[str] = None
    VpcId: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    SnapshotRetentionLimit: Optional[int] = None
    SnapshotWindow: Optional[str] = None
    NumNodeGroups: Optional[int] = None
    AutomaticFailover: Optional[AutomaticFailoverStatusType] = None
    NodeSnapshots: Optional[List[NodeSnapshot]] = None
    KmsKeyId: Optional[str] = None
    ARN: Optional[str] = None
    DataTiering: Optional[DataTieringStatusType] = None


class UpdateAction(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    ServiceUpdateName: Optional[str] = None
    ServiceUpdateReleaseDate: Optional[datetime] = None
    ServiceUpdateSeverity: Optional[ServiceUpdateSeverityType] = None
    ServiceUpdateStatus: Optional[ServiceUpdateStatusType] = None
    ServiceUpdateRecommendedApplyByDate: Optional[datetime] = None
    ServiceUpdateType: Optional[Literal['security-update']] = None
    UpdateActionAvailableDate: Optional[datetime] = None
    UpdateActionStatus: Optional[UpdateActionStatusType] = None
    NodesUpdated: Optional[str] = None
    UpdateActionStatusModifiedDate: Optional[datetime] = None
    SlaMet: Optional[SlaMetType] = None
    NodeGroupUpdateStatus: Optional[List[NodeGroupUpdateStatus]] = None
    CacheNodeUpdateStatus: Optional[List[CacheNodeUpdateStatus]] = None
    EstimatedUpdateTime: Optional[str] = None
    Engine: Optional[str] = None


# This class is the output for the 'purchase_reserved_cache_nodes_offering' function.
class PurchaseReservedCacheNodesOfferingResult(BaseValidatorModel):
    ReservedCacheNode: ReservedCacheNode
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_reserved_cache_nodes' function.
class ReservedCacheNodeMessage(BaseValidatorModel):
    Marker: str
    ReservedCacheNodes: List[ReservedCacheNode]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_reserved_cache_nodes_offerings' function.
class ReservedCacheNodesOfferingMessage(BaseValidatorModel):
    Marker: str
    ReservedCacheNodesOfferings: List[ReservedCacheNodesOffering]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_serverless_cache_snapshot' function.
class CopyServerlessCacheSnapshotResponse(BaseValidatorModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_serverless_cache_snapshot' function.
class CreateServerlessCacheSnapshotResponse(BaseValidatorModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_serverless_cache_snapshot' function.
class DeleteServerlessCacheSnapshotResponse(BaseValidatorModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_serverless_cache_snapshots' function.
class DescribeServerlessCacheSnapshotsResponse(BaseValidatorModel):
    ServerlessCacheSnapshots: List[ServerlessCacheSnapshot]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'export_serverless_cache_snapshot' function.
class ExportServerlessCacheSnapshotResponse(BaseValidatorModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshot
    ResponseMetadata: ResponseMetadata


class CacheSubnetGroup(BaseValidatorModel):
    CacheSubnetGroupName: Optional[str] = None
    CacheSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    Subnets: Optional[List[Subnet]] = None
    ARN: Optional[str] = None
    SupportedNetworkTypes: Optional[List[NetworkTypeType]] = None


# This class is the output for the 'describe_user_groups' function.
class DescribeUserGroupsResult(BaseValidatorModel):
    UserGroups: List[UserGroup]
    Marker: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_engine_default_parameters' function.
class DescribeEngineDefaultParametersResult(BaseValidatorModel):
    EngineDefaults: EngineDefaults
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_serverless_cache' function.
class CreateServerlessCacheResponse(BaseValidatorModel):
    ServerlessCache: ServerlessCache
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_serverless_cache' function.
class DeleteServerlessCacheResponse(BaseValidatorModel):
    ServerlessCache: ServerlessCache
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_serverless_caches' function.
class DescribeServerlessCachesResponse(BaseValidatorModel):
    ServerlessCaches: List[ServerlessCache]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'modify_serverless_cache' function.
class ModifyServerlessCacheResponse(BaseValidatorModel):
    ServerlessCache: ServerlessCache
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_cache_cluster' function.
class CreateCacheClusterMessage(BaseValidatorModel):
    CacheClusterId: str
    ReplicationGroupId: Optional[str] = None
    AZMode: Optional[AZModeType] = None
    PreferredAvailabilityZone: Optional[str] = None
    PreferredAvailabilityZones: Optional[List[str]] = None
    NumCacheNodes: Optional[int] = None
    CacheNodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupName: Optional[str] = None
    CacheSubnetGroupName: Optional[str] = None
    CacheSecurityGroupNames: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    SnapshotArns: Optional[List[str]] = None
    SnapshotName: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    Port: Optional[int] = None
    NotificationTopicArn: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    SnapshotRetentionLimit: Optional[int] = None
    SnapshotWindow: Optional[str] = None
    AuthToken: Optional[str] = None
    OutpostMode: Optional[OutpostModeType] = None
    PreferredOutpostArn: Optional[str] = None
    PreferredOutpostArns: Optional[List[str]] = None
    LogDeliveryConfigurations: Optional[List[LogDeliveryConfigurationRequest]] = None
    TransitEncryptionEnabled: Optional[bool] = None
    NetworkType: Optional[NetworkTypeType] = None
    IpDiscovery: Optional[IpDiscoveryType] = None


# This class is the input for the 'create_replication_group' function.
class CreateReplicationGroupMessage(BaseValidatorModel):
    ReplicationGroupId: str
    ReplicationGroupDescription: str
    GlobalReplicationGroupId: Optional[str] = None
    PrimaryClusterId: Optional[str] = None
    AutomaticFailoverEnabled: Optional[bool] = None
    MultiAZEnabled: Optional[bool] = None
    NumCacheClusters: Optional[int] = None
    PreferredCacheClusterAZs: Optional[List[str]] = None
    NumNodeGroups: Optional[int] = None
    ReplicasPerNodeGroup: Optional[int] = None
    NodeGroupConfiguration: Optional[List[NodeGroupConfigurationUnion]] = None
    CacheNodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupName: Optional[str] = None
    CacheSubnetGroupName: Optional[str] = None
    CacheSecurityGroupNames: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None
    SnapshotArns: Optional[List[str]] = None
    SnapshotName: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    Port: Optional[int] = None
    NotificationTopicArn: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    SnapshotRetentionLimit: Optional[int] = None
    SnapshotWindow: Optional[str] = None
    AuthToken: Optional[str] = None
    TransitEncryptionEnabled: Optional[bool] = None
    AtRestEncryptionEnabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    UserGroupIds: Optional[List[str]] = None
    LogDeliveryConfigurations: Optional[List[LogDeliveryConfigurationRequest]] = None
    DataTieringEnabled: Optional[bool] = None
    NetworkType: Optional[NetworkTypeType] = None
    IpDiscovery: Optional[IpDiscoveryType] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None
    ClusterMode: Optional[ClusterModeType] = None
    ServerlessCacheSnapshotName: Optional[str] = None


# This class is the input for the 'modify_cache_cluster' function.
class ModifyCacheClusterMessage(BaseValidatorModel):
    CacheClusterId: str
    NumCacheNodes: Optional[int] = None
    CacheNodeIdsToRemove: Optional[List[str]] = None
    AZMode: Optional[AZModeType] = None
    NewAvailabilityZones: Optional[List[str]] = None
    CacheSecurityGroupNames: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    PreferredMaintenanceWindow: Optional[str] = None
    NotificationTopicArn: Optional[str] = None
    CacheParameterGroupName: Optional[str] = None
    NotificationTopicStatus: Optional[str] = None
    ApplyImmediately: Optional[bool] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    SnapshotRetentionLimit: Optional[int] = None
    SnapshotWindow: Optional[str] = None
    CacheNodeType: Optional[str] = None
    AuthToken: Optional[str] = None
    AuthTokenUpdateStrategy: Optional[AuthTokenUpdateStrategyTypeType] = None
    LogDeliveryConfigurations: Optional[List[LogDeliveryConfigurationRequest]] = None
    IpDiscovery: Optional[IpDiscoveryType] = None


# This class is the input for the 'modify_replication_group' function.
class ModifyReplicationGroupMessage(BaseValidatorModel):
    ReplicationGroupId: str
    ReplicationGroupDescription: Optional[str] = None
    PrimaryClusterId: Optional[str] = None
    SnapshottingClusterId: Optional[str] = None
    AutomaticFailoverEnabled: Optional[bool] = None
    MultiAZEnabled: Optional[bool] = None
    NodeGroupId: Optional[str] = None
    CacheSecurityGroupNames: Optional[List[str]] = None
    SecurityGroupIds: Optional[List[str]] = None
    PreferredMaintenanceWindow: Optional[str] = None
    NotificationTopicArn: Optional[str] = None
    CacheParameterGroupName: Optional[str] = None
    NotificationTopicStatus: Optional[str] = None
    ApplyImmediately: Optional[bool] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    SnapshotRetentionLimit: Optional[int] = None
    SnapshotWindow: Optional[str] = None
    CacheNodeType: Optional[str] = None
    AuthToken: Optional[str] = None
    AuthTokenUpdateStrategy: Optional[AuthTokenUpdateStrategyTypeType] = None
    UserGroupIdsToAdd: Optional[List[str]] = None
    UserGroupIdsToRemove: Optional[List[str]] = None
    RemoveUserGroups: Optional[bool] = None
    LogDeliveryConfigurations: Optional[List[LogDeliveryConfigurationRequest]] = None
    IpDiscovery: Optional[IpDiscoveryType] = None
    TransitEncryptionEnabled: Optional[bool] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None
    ClusterMode: Optional[ClusterModeType] = None


class PendingModifiedValues(BaseValidatorModel):
    NumCacheNodes: Optional[int] = None
    CacheNodeIdsToRemove: Optional[List[str]] = None
    EngineVersion: Optional[str] = None
    CacheNodeType: Optional[str] = None
    AuthTokenStatus: Optional[AuthTokenUpdateStatusType] = None
    LogDeliveryConfigurations: Optional[List[PendingLogDeliveryConfiguration]] = None
    TransitEncryptionEnabled: Optional[bool] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None


class ReplicationGroupPendingModifiedValues(BaseValidatorModel):
    PrimaryClusterId: Optional[str] = None
    AutomaticFailoverStatus: Optional[PendingAutomaticFailoverStatusType] = None
    Resharding: Optional[ReshardingStatus] = None
    AuthTokenStatus: Optional[AuthTokenUpdateStatusType] = None
    UserGroups: Optional[UserGroupsUpdateStatus] = None
    LogDeliveryConfigurations: Optional[List[PendingLogDeliveryConfiguration]] = None
    TransitEncryptionEnabled: Optional[bool] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None
    ClusterMode: Optional[ClusterModeType] = None


# This class is the output for the 'copy_snapshot' function.
class CopySnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_snapshot' function.
class CreateSnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_snapshot' function.
class DeleteSnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_snapshots' function.
class DescribeSnapshotsListMessage(BaseValidatorModel):
    Marker: str
    Snapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_update_actions' function.
class UpdateActionsMessage(BaseValidatorModel):
    Marker: str
    UpdateActions: List[UpdateAction]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_cache_subnet_groups' function.
class CacheSubnetGroupMessage(BaseValidatorModel):
    Marker: str
    CacheSubnetGroups: List[CacheSubnetGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cache_subnet_group' function.
class CreateCacheSubnetGroupResult(BaseValidatorModel):
    CacheSubnetGroup: CacheSubnetGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_cache_subnet_group' function.
class ModifyCacheSubnetGroupResult(BaseValidatorModel):
    CacheSubnetGroup: CacheSubnetGroup
    ResponseMetadata: ResponseMetadata


class CacheCluster(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    ConfigurationEndpoint: Optional[Endpoint] = None
    ClientDownloadLandingPage: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheClusterStatus: Optional[str] = None
    NumCacheNodes: Optional[int] = None
    PreferredAvailabilityZone: Optional[str] = None
    PreferredOutpostArn: Optional[str] = None
    CacheClusterCreateTime: Optional[datetime] = None
    PreferredMaintenanceWindow: Optional[str] = None
    PendingModifiedValues: Optional[PendingModifiedValues] = None
    NotificationConfiguration: Optional[NotificationConfiguration] = None
    CacheSecurityGroups: Optional[List[CacheSecurityGroupMembership]] = None
    CacheParameterGroup: Optional[CacheParameterGroupStatus] = None
    CacheSubnetGroupName: Optional[str] = None
    CacheNodes: Optional[List[CacheNode]] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    SecurityGroups: Optional[List[SecurityGroupMembership]] = None
    ReplicationGroupId: Optional[str] = None
    SnapshotRetentionLimit: Optional[int] = None
    SnapshotWindow: Optional[str] = None
    AuthTokenEnabled: Optional[bool] = None
    AuthTokenLastModifiedDate: Optional[datetime] = None
    TransitEncryptionEnabled: Optional[bool] = None
    AtRestEncryptionEnabled: Optional[bool] = None
    ARN: Optional[str] = None
    ReplicationGroupLogDeliveryEnabled: Optional[bool] = None
    LogDeliveryConfigurations: Optional[List[LogDeliveryConfiguration]] = None
    NetworkType: Optional[NetworkTypeType] = None
    IpDiscovery: Optional[IpDiscoveryType] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None


class ReplicationGroup(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    Description: Optional[str] = None
    GlobalReplicationGroupInfo: Optional[GlobalReplicationGroupInfo] = None
    Status: Optional[str] = None
    PendingModifiedValues: Optional[ReplicationGroupPendingModifiedValues] = None
    MemberClusters: Optional[List[str]] = None
    NodeGroups: Optional[List[NodeGroup]] = None
    SnapshottingClusterId: Optional[str] = None
    AutomaticFailover: Optional[AutomaticFailoverStatusType] = None
    MultiAZ: Optional[MultiAZStatusType] = None
    ConfigurationEndpoint: Optional[Endpoint] = None
    SnapshotRetentionLimit: Optional[int] = None
    SnapshotWindow: Optional[str] = None
    ClusterEnabled: Optional[bool] = None
    CacheNodeType: Optional[str] = None
    AuthTokenEnabled: Optional[bool] = None
    AuthTokenLastModifiedDate: Optional[datetime] = None
    TransitEncryptionEnabled: Optional[bool] = None
    AtRestEncryptionEnabled: Optional[bool] = None
    MemberClustersOutpostArns: Optional[List[str]] = None
    KmsKeyId: Optional[str] = None
    ARN: Optional[str] = None
    UserGroupIds: Optional[List[str]] = None
    LogDeliveryConfigurations: Optional[List[LogDeliveryConfiguration]] = None
    ReplicationGroupCreateTime: Optional[datetime] = None
    DataTiering: Optional[DataTieringStatusType] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    NetworkType: Optional[NetworkTypeType] = None
    IpDiscovery: Optional[IpDiscoveryType] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None
    ClusterMode: Optional[ClusterModeType] = None
    Engine: Optional[str] = None


# This class is the output for the 'describe_cache_clusters' function.
class CacheClusterMessage(BaseValidatorModel):
    Marker: str
    CacheClusters: List[CacheCluster]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cache_cluster' function.
class CreateCacheClusterResult(BaseValidatorModel):
    CacheCluster: CacheCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_cache_cluster' function.
class DeleteCacheClusterResult(BaseValidatorModel):
    CacheCluster: CacheCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_cache_cluster' function.
class ModifyCacheClusterResult(BaseValidatorModel):
    CacheCluster: CacheCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'reboot_cache_cluster' function.
class RebootCacheClusterResult(BaseValidatorModel):
    CacheCluster: CacheCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'complete_migration' function.
class CompleteMigrationResponse(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_replication_group' function.
class CreateReplicationGroupResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'decrease_replica_count' function.
class DecreaseReplicaCountResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_replication_group' function.
class DeleteReplicationGroupResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'increase_replica_count' function.
class IncreaseReplicaCountResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_replication_group' function.
class ModifyReplicationGroupResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'modify_replication_group_shard_configuration' function.
class ModifyReplicationGroupShardConfigurationResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_replication_groups' function.
class ReplicationGroupMessage(BaseValidatorModel):
    Marker: str
    ReplicationGroups: List[ReplicationGroup]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_migration' function.
class StartMigrationResponse(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_failover' function.
class TestFailoverResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'test_migration' function.
class TestMigrationResponse(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata