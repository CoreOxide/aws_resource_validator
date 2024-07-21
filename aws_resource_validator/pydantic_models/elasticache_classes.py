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
from aws_resource_validator.pydantic_models.elasticache_constants import *

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AuthenticationModeTypeDef(BaseModel):
    Type: Optional[InputAuthenticationTypeType] = None
    Passwords: Optional[Sequence[str]] = None

class AuthenticationTypeDef(BaseModel):
    Type: Optional[AuthenticationTypeType] = None
    PasswordCount: Optional[int] = None

class AuthorizeCacheSecurityGroupIngressMessageRequestTypeDef(BaseModel):
    CacheSecurityGroupName: str
    EC2SecurityGroupName: str
    EC2SecurityGroupOwnerId: str

class AvailabilityZoneTypeDef(BaseModel):
    Name: Optional[str] = None

class BatchApplyUpdateActionMessageRequestTypeDef(BaseModel):
    ServiceUpdateName: str
    ReplicationGroupIds: Optional[Sequence[str]] = None
    CacheClusterIds: Optional[Sequence[str]] = None

class BatchStopUpdateActionMessageRequestTypeDef(BaseModel):
    ServiceUpdateName: str
    ReplicationGroupIds: Optional[Sequence[str]] = None
    CacheClusterIds: Optional[Sequence[str]] = None

class CacheParameterGroupStatusTypeDef(BaseModel):
    CacheParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    CacheNodeIdsToReboot: Optional[List[str]] = None

class CacheSecurityGroupMembershipTypeDef(BaseModel):
    CacheSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None

class EndpointTypeDef(BaseModel):
    Address: Optional[str] = None
    Port: Optional[int] = None

class NotificationConfigurationTypeDef(BaseModel):
    TopicArn: Optional[str] = None
    TopicStatus: Optional[str] = None

class SecurityGroupMembershipTypeDef(BaseModel):
    SecurityGroupId: Optional[str] = None
    Status: Optional[str] = None

class CacheEngineVersionTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupFamily: Optional[str] = None
    CacheEngineDescription: Optional[str] = None
    CacheEngineVersionDescription: Optional[str] = None

class CacheNodeTypeSpecificValueTypeDef(BaseModel):
    CacheNodeType: Optional[str] = None
    Value: Optional[str] = None

class CacheNodeUpdateStatusTypeDef(BaseModel):
    CacheNodeId: Optional[str] = None
    NodeUpdateStatus: Optional[NodeUpdateStatusType] = None
    NodeDeletionDate: Optional[datetime] = None
    NodeUpdateStartDate: Optional[datetime] = None
    NodeUpdateEndDate: Optional[datetime] = None
    NodeUpdateInitiatedBy: Optional[NodeUpdateInitiatedByType] = None
    NodeUpdateInitiatedDate: Optional[datetime] = None
    NodeUpdateStatusModifiedDate: Optional[datetime] = None

class ParameterTypeDef(BaseModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None
    ChangeType: Optional[ChangeTypeType] = None

class CacheParameterGroupTypeDef(BaseModel):
    CacheParameterGroupName: Optional[str] = None
    CacheParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    IsGlobal: Optional[bool] = None
    ARN: Optional[str] = None

class EC2SecurityGroupTypeDef(BaseModel):
    Status: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None

class DataStorageTypeDef(BaseModel):
    Unit: Literal["GB"]
    Maximum: Optional[int] = None
    Minimum: Optional[int] = None

class ECPUPerSecondTypeDef(BaseModel):
    Maximum: Optional[int] = None
    Minimum: Optional[int] = None

class CloudWatchLogsDestinationDetailsTypeDef(BaseModel):
    LogGroup: Optional[str] = None

class CompleteMigrationMessageRequestTypeDef(BaseModel):
    ReplicationGroupId: str
    Force: Optional[bool] = None

class ConfigureShardTypeDef(BaseModel):
    NodeGroupId: str
    NewReplicaCount: int
    PreferredAvailabilityZones: Optional[Sequence[str]] = None
    PreferredOutpostArns: Optional[Sequence[str]] = None

class CreateGlobalReplicationGroupMessageRequestTypeDef(BaseModel):
    GlobalReplicationGroupIdSuffix: str
    PrimaryReplicationGroupId: str
    GlobalReplicationGroupDescription: Optional[str] = None

class CustomerNodeEndpointTypeDef(BaseModel):
    Address: Optional[str] = None
    Port: Optional[int] = None

class DecreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef(BaseModel):
    GlobalReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    GlobalNodeGroupsToRemove: Optional[Sequence[str]] = None
    GlobalNodeGroupsToRetain: Optional[Sequence[str]] = None

class DeleteCacheClusterMessageRequestTypeDef(BaseModel):
    CacheClusterId: str
    FinalSnapshotIdentifier: Optional[str] = None

class DeleteCacheParameterGroupMessageRequestTypeDef(BaseModel):
    CacheParameterGroupName: str

class DeleteCacheSecurityGroupMessageRequestTypeDef(BaseModel):
    CacheSecurityGroupName: str

class DeleteCacheSubnetGroupMessageRequestTypeDef(BaseModel):
    CacheSubnetGroupName: str

class DeleteGlobalReplicationGroupMessageRequestTypeDef(BaseModel):
    GlobalReplicationGroupId: str
    RetainPrimaryReplicationGroup: bool

class DeleteReplicationGroupMessageRequestTypeDef(BaseModel):
    ReplicationGroupId: str
    RetainPrimaryCluster: Optional[bool] = None
    FinalSnapshotIdentifier: Optional[str] = None

class DeleteServerlessCacheRequestRequestTypeDef(BaseModel):
    ServerlessCacheName: str
    FinalSnapshotName: Optional[str] = None

class DeleteServerlessCacheSnapshotRequestRequestTypeDef(BaseModel):
    ServerlessCacheSnapshotName: str

class DeleteSnapshotMessageRequestTypeDef(BaseModel):
    SnapshotName: str

class DeleteUserGroupMessageRequestTypeDef(BaseModel):
    UserGroupId: str

class DeleteUserMessageRequestTypeDef(BaseModel):
    UserId: str

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeCacheClustersMessageRequestTypeDef(BaseModel):
    CacheClusterId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowCacheNodeInfo: Optional[bool] = None
    ShowCacheClustersNotInReplicationGroups: Optional[bool] = None

class DescribeCacheEngineVersionsMessageRequestTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupFamily: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DefaultOnly: Optional[bool] = None

class DescribeCacheParameterGroupsMessageRequestTypeDef(BaseModel):
    CacheParameterGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeCacheParametersMessageRequestTypeDef(BaseModel):
    CacheParameterGroupName: str
    Source: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeCacheSecurityGroupsMessageRequestTypeDef(BaseModel):
    CacheSecurityGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeCacheSubnetGroupsMessageRequestTypeDef(BaseModel):
    CacheSubnetGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeEngineDefaultParametersMessageRequestTypeDef(BaseModel):
    CacheParameterGroupFamily: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeGlobalReplicationGroupsMessageRequestTypeDef(BaseModel):
    GlobalReplicationGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowMemberInfo: Optional[bool] = None

class DescribeReplicationGroupsMessageRequestTypeDef(BaseModel):
    ReplicationGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReservedCacheNodesMessageRequestTypeDef(BaseModel):
    ReservedCacheNodeId: Optional[str] = None
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeReservedCacheNodesOfferingsMessageRequestTypeDef(BaseModel):
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeServerlessCacheSnapshotsRequestRequestTypeDef(BaseModel):
    ServerlessCacheName: Optional[str] = None
    ServerlessCacheSnapshotName: Optional[str] = None
    SnapshotType: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class DescribeServerlessCachesRequestRequestTypeDef(BaseModel):
    ServerlessCacheName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeServiceUpdatesMessageRequestTypeDef(BaseModel):
    ServiceUpdateName: Optional[str] = None
    ServiceUpdateStatus: Optional[Sequence[ServiceUpdateStatusType]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DescribeSnapshotsMessageRequestTypeDef(BaseModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    SnapshotName: Optional[str] = None
    SnapshotSource: Optional[str] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    ShowNodeGroupConfig: Optional[bool] = None

class DescribeUserGroupsMessageRequestTypeDef(BaseModel):
    UserGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class FilterTypeDef(BaseModel):
    Name: str
    Values: Sequence[str]

class KinesisFirehoseDestinationDetailsTypeDef(BaseModel):
    DeliveryStream: Optional[str] = None

class DisassociateGlobalReplicationGroupMessageRequestTypeDef(BaseModel):
    GlobalReplicationGroupId: str
    ReplicationGroupId: str
    ReplicationGroupRegion: str

class EventTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    Date: Optional[datetime] = None

class ExportServerlessCacheSnapshotRequestRequestTypeDef(BaseModel):
    ServerlessCacheSnapshotName: str
    S3BucketName: str

class FailoverGlobalReplicationGroupMessageRequestTypeDef(BaseModel):
    GlobalReplicationGroupId: str
    PrimaryRegion: str
    PrimaryReplicationGroupId: str

class GlobalNodeGroupTypeDef(BaseModel):
    GlobalNodeGroupId: Optional[str] = None
    Slots: Optional[str] = None

class GlobalReplicationGroupInfoTypeDef(BaseModel):
    GlobalReplicationGroupId: Optional[str] = None
    GlobalReplicationGroupMemberRole: Optional[str] = None

class GlobalReplicationGroupMemberTypeDef(BaseModel):
    ReplicationGroupId: Optional[str] = None
    ReplicationGroupRegion: Optional[str] = None
    Role: Optional[str] = None
    AutomaticFailover: Optional[AutomaticFailoverStatusType] = None
    Status: Optional[str] = None

class ListAllowedNodeTypeModificationsMessageRequestTypeDef(BaseModel):
    CacheClusterId: Optional[str] = None
    ReplicationGroupId: Optional[str] = None

class ListTagsForResourceMessageRequestTypeDef(BaseModel):
    ResourceName: str

class ParameterNameValueTypeDef(BaseModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None

class ModifyCacheSubnetGroupMessageRequestTypeDef(BaseModel):
    CacheSubnetGroupName: str
    CacheSubnetGroupDescription: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None

class ModifyGlobalReplicationGroupMessageRequestTypeDef(BaseModel):
    GlobalReplicationGroupId: str
    ApplyImmediately: bool
    CacheNodeType: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupName: Optional[str] = None
    GlobalReplicationGroupDescription: Optional[str] = None
    AutomaticFailoverEnabled: Optional[bool] = None

class ReshardingConfigurationTypeDef(BaseModel):
    NodeGroupId: Optional[str] = None
    PreferredAvailabilityZones: Optional[Sequence[str]] = None

class ModifyUserGroupMessageRequestTypeDef(BaseModel):
    UserGroupId: str
    UserIdsToAdd: Optional[Sequence[str]] = None
    UserIdsToRemove: Optional[Sequence[str]] = None

class NodeGroupConfigurationExtraOutputTypeDef(BaseModel):
    NodeGroupId: Optional[str] = None
    Slots: Optional[str] = None
    ReplicaCount: Optional[int] = None
    PrimaryAvailabilityZone: Optional[str] = None
    ReplicaAvailabilityZones: Optional[List[str]] = None
    PrimaryOutpostArn: Optional[str] = None
    ReplicaOutpostArns: Optional[List[str]] = None

class NodeGroupConfigurationOutputTypeDef(BaseModel):
    NodeGroupId: Optional[str] = None
    Slots: Optional[str] = None
    ReplicaCount: Optional[int] = None
    PrimaryAvailabilityZone: Optional[str] = None
    ReplicaAvailabilityZones: Optional[List[str]] = None
    PrimaryOutpostArn: Optional[str] = None
    ReplicaOutpostArns: Optional[List[str]] = None

class NodeGroupConfigurationTypeDef(BaseModel):
    NodeGroupId: Optional[str] = None
    Slots: Optional[str] = None
    ReplicaCount: Optional[int] = None
    PrimaryAvailabilityZone: Optional[str] = None
    ReplicaAvailabilityZones: Optional[Sequence[str]] = None
    PrimaryOutpostArn: Optional[str] = None
    ReplicaOutpostArns: Optional[Sequence[str]] = None

class NodeGroupMemberUpdateStatusTypeDef(BaseModel):
    CacheClusterId: Optional[str] = None
    CacheNodeId: Optional[str] = None
    NodeUpdateStatus: Optional[NodeUpdateStatusType] = None
    NodeDeletionDate: Optional[datetime] = None
    NodeUpdateStartDate: Optional[datetime] = None
    NodeUpdateEndDate: Optional[datetime] = None
    NodeUpdateInitiatedBy: Optional[NodeUpdateInitiatedByType] = None
    NodeUpdateInitiatedDate: Optional[datetime] = None
    NodeUpdateStatusModifiedDate: Optional[datetime] = None

class ProcessedUpdateActionTypeDef(BaseModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    ServiceUpdateName: Optional[str] = None
    UpdateActionStatus: Optional[UpdateActionStatusType] = None

class RebalanceSlotsInGlobalReplicationGroupMessageRequestTypeDef(BaseModel):
    GlobalReplicationGroupId: str
    ApplyImmediately: bool

class RebootCacheClusterMessageRequestTypeDef(BaseModel):
    CacheClusterId: str
    CacheNodeIdsToReboot: Sequence[str]

class RecurringChargeTypeDef(BaseModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None

class RemoveTagsFromResourceMessageRequestTypeDef(BaseModel):
    ResourceName: str
    TagKeys: Sequence[str]

class UserGroupsUpdateStatusTypeDef(BaseModel):
    UserGroupIdsToAdd: Optional[List[str]] = None
    UserGroupIdsToRemove: Optional[List[str]] = None

class SlotMigrationTypeDef(BaseModel):
    ProgressPercentage: Optional[float] = None

class RevokeCacheSecurityGroupIngressMessageRequestTypeDef(BaseModel):
    CacheSecurityGroupName: str
    EC2SecurityGroupName: str
    EC2SecurityGroupOwnerId: str

class ServerlessCacheConfigurationTypeDef(BaseModel):
    ServerlessCacheName: Optional[str] = None
    Engine: Optional[str] = None
    MajorEngineVersion: Optional[str] = None

class ServiceUpdateTypeDef(BaseModel):
    ServiceUpdateName: Optional[str] = None
    ServiceUpdateReleaseDate: Optional[datetime] = None
    ServiceUpdateEndDate: Optional[datetime] = None
    ServiceUpdateSeverity: Optional[ServiceUpdateSeverityType] = None
    ServiceUpdateRecommendedApplyByDate: Optional[datetime] = None
    ServiceUpdateStatus: Optional[ServiceUpdateStatusType] = None
    ServiceUpdateDescription: Optional[str] = None
    ServiceUpdateType: Optional[Literal["security-update"]] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    AutoUpdateAfterRecommendedApplyByDate: Optional[bool] = None
    EstimatedUpdateTime: Optional[str] = None

class SubnetOutpostTypeDef(BaseModel):
    SubnetOutpostArn: Optional[str] = None

class TestFailoverMessageRequestTypeDef(BaseModel):
    ReplicationGroupId: str
    NodeGroupId: str

class UnprocessedUpdateActionTypeDef(BaseModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    ServiceUpdateName: Optional[str] = None
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None

class UserGroupPendingChangesTypeDef(BaseModel):
    UserIdsToRemove: Optional[List[str]] = None
    UserIdsToAdd: Optional[List[str]] = None

class AddTagsToResourceMessageRequestTypeDef(BaseModel):
    ResourceName: str
    Tags: Sequence[TagTypeDef]

class CopyServerlessCacheSnapshotRequestRequestTypeDef(BaseModel):
    SourceServerlessCacheSnapshotName: str
    TargetServerlessCacheSnapshotName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CopySnapshotMessageRequestTypeDef(BaseModel):
    SourceSnapshotName: str
    TargetSnapshotName: str
    TargetBucket: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateCacheParameterGroupMessageRequestTypeDef(BaseModel):
    CacheParameterGroupName: str
    CacheParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateCacheSecurityGroupMessageRequestTypeDef(BaseModel):
    CacheSecurityGroupName: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateCacheSubnetGroupMessageRequestTypeDef(BaseModel):
    CacheSubnetGroupName: str
    CacheSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateServerlessCacheSnapshotRequestRequestTypeDef(BaseModel):
    ServerlessCacheSnapshotName: str
    ServerlessCacheName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSnapshotMessageRequestTypeDef(BaseModel):
    SnapshotName: str
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateUserGroupMessageRequestTypeDef(BaseModel):
    UserGroupId: str
    Engine: str
    UserIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class PurchaseReservedCacheNodesOfferingMessageRequestTypeDef(BaseModel):
    ReservedCacheNodesOfferingId: str
    ReservedCacheNodeId: Optional[str] = None
    CacheNodeCount: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class AllowedNodeTypeModificationsMessageTypeDef(BaseModel):
    ScaleUpModifications: List[str]
    ScaleDownModifications: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class CacheParameterGroupNameMessageTypeDef(BaseModel):
    CacheParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class TagListMessageTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserMessageRequestTypeDef(BaseModel):
    UserId: str
    UserName: str
    Engine: str
    AccessString: str
    Passwords: Optional[Sequence[str]] = None
    NoPasswordRequired: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AuthenticationMode: Optional[AuthenticationModeTypeDef] = None

class ModifyUserMessageRequestTypeDef(BaseModel):
    UserId: str
    AccessString: Optional[str] = None
    AppendAccessString: Optional[str] = None
    Passwords: Optional[Sequence[str]] = None
    NoPasswordRequired: Optional[bool] = None
    AuthenticationMode: Optional[AuthenticationModeTypeDef] = None

class UserResponseTypeDef(BaseModel):
    UserId: str
    UserName: str
    Status: str
    Engine: str
    MinimumEngineVersion: str
    AccessString: str
    UserGroupIds: List[str]
    Authentication: AuthenticationTypeDef
    ARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UserTypeDef(BaseModel):
    UserId: Optional[str] = None
    UserName: Optional[str] = None
    Status: Optional[str] = None
    Engine: Optional[str] = None
    MinimumEngineVersion: Optional[str] = None
    AccessString: Optional[str] = None
    UserGroupIds: Optional[List[str]] = None
    Authentication: Optional[AuthenticationTypeDef] = None
    ARN: Optional[str] = None

class CacheNodeTypeDef(BaseModel):
    CacheNodeId: Optional[str] = None
    CacheNodeStatus: Optional[str] = None
    CacheNodeCreateTime: Optional[datetime] = None
    Endpoint: Optional[EndpointTypeDef] = None
    ParameterGroupStatus: Optional[str] = None
    SourceCacheNodeId: Optional[str] = None
    CustomerAvailabilityZone: Optional[str] = None
    CustomerOutpostArn: Optional[str] = None

class NodeGroupMemberTypeDef(BaseModel):
    CacheClusterId: Optional[str] = None
    CacheNodeId: Optional[str] = None
    ReadEndpoint: Optional[EndpointTypeDef] = None
    PreferredAvailabilityZone: Optional[str] = None
    PreferredOutpostArn: Optional[str] = None
    CurrentRole: Optional[str] = None

class CacheEngineVersionMessageTypeDef(BaseModel):
    Marker: str
    CacheEngineVersions: List[CacheEngineVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CacheNodeTypeSpecificParameterTypeDef(BaseModel):
    ParameterName: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None
    CacheNodeTypeSpecificValues: Optional[List[CacheNodeTypeSpecificValueTypeDef]] = None
    ChangeType: Optional[ChangeTypeType] = None

class CacheParameterGroupsMessageTypeDef(BaseModel):
    Marker: str
    CacheParameterGroups: List[CacheParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCacheParameterGroupResultTypeDef(BaseModel):
    CacheParameterGroup: CacheParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CacheSecurityGroupTypeDef(BaseModel):
    OwnerId: Optional[str] = None
    CacheSecurityGroupName: Optional[str] = None
    Description: Optional[str] = None
    EC2SecurityGroups: Optional[List[EC2SecurityGroupTypeDef]] = None
    ARN: Optional[str] = None

class CacheUsageLimitsTypeDef(BaseModel):
    DataStorage: Optional[DataStorageTypeDef] = None
    ECPUPerSecond: Optional[ECPUPerSecondTypeDef] = None

class DecreaseReplicaCountMessageRequestTypeDef(BaseModel):
    ReplicationGroupId: str
    ApplyImmediately: bool
    NewReplicaCount: Optional[int] = None
    ReplicaConfiguration: Optional[Sequence[ConfigureShardTypeDef]] = None
    ReplicasToRemove: Optional[Sequence[str]] = None

class IncreaseReplicaCountMessageRequestTypeDef(BaseModel):
    ReplicationGroupId: str
    ApplyImmediately: bool
    NewReplicaCount: Optional[int] = None
    ReplicaConfiguration: Optional[Sequence[ConfigureShardTypeDef]] = None

class StartMigrationMessageRequestTypeDef(BaseModel):
    ReplicationGroupId: str
    CustomerNodeEndpointList: Sequence[CustomerNodeEndpointTypeDef]

class TestMigrationMessageRequestTypeDef(BaseModel):
    ReplicationGroupId: str
    CustomerNodeEndpointList: Sequence[CustomerNodeEndpointTypeDef]

class DescribeCacheClustersMessageCacheClusterAvailableWaitTypeDef(BaseModel):
    CacheClusterId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowCacheNodeInfo: Optional[bool] = None
    ShowCacheClustersNotInReplicationGroups: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeCacheClustersMessageCacheClusterDeletedWaitTypeDef(BaseModel):
    CacheClusterId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowCacheNodeInfo: Optional[bool] = None
    ShowCacheClustersNotInReplicationGroups: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeReplicationGroupsMessageReplicationGroupAvailableWaitTypeDef(BaseModel):
    ReplicationGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeReplicationGroupsMessageReplicationGroupDeletedWaitTypeDef(BaseModel):
    ReplicationGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeCacheClustersMessageDescribeCacheClustersPaginateTypeDef(BaseModel):
    CacheClusterId: Optional[str] = None
    ShowCacheNodeInfo: Optional[bool] = None
    ShowCacheClustersNotInReplicationGroups: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCacheEngineVersionsMessageDescribeCacheEngineVersionsPaginateTypeDef(BaseModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupFamily: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCacheParameterGroupsMessageDescribeCacheParameterGroupsPaginateTypeDef(BaseModel):
    CacheParameterGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCacheParametersMessageDescribeCacheParametersPaginateTypeDef(BaseModel):
    CacheParameterGroupName: str
    Source: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCacheSecurityGroupsMessageDescribeCacheSecurityGroupsPaginateTypeDef(BaseModel):
    CacheSecurityGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeCacheSubnetGroupsMessageDescribeCacheSubnetGroupsPaginateTypeDef(BaseModel):
    CacheSubnetGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEngineDefaultParametersMessageDescribeEngineDefaultParametersPaginateTypeDef(BaseModel):
    CacheParameterGroupFamily: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeGlobalReplicationGroupsMessageDescribeGlobalReplicationGroupsPaginateTypeDef(BaseModel):
    GlobalReplicationGroupId: Optional[str] = None
    ShowMemberInfo: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReplicationGroupsMessageDescribeReplicationGroupsPaginateTypeDef(BaseModel):
    ReplicationGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedCacheNodesMessageDescribeReservedCacheNodesPaginateTypeDef(BaseModel):
    ReservedCacheNodeId: Optional[str] = None
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedCacheNodesOfferingsMessageDescribeReservedCacheNodesOfferingsPaginateTypeDef(BaseModel):
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeServerlessCacheSnapshotsRequestDescribeServerlessCacheSnapshotsPaginateTypeDef(BaseModel):
    ServerlessCacheName: Optional[str] = None
    ServerlessCacheSnapshotName: Optional[str] = None
    SnapshotType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeServerlessCachesRequestDescribeServerlessCachesPaginateTypeDef(BaseModel):
    ServerlessCacheName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeServiceUpdatesMessageDescribeServiceUpdatesPaginateTypeDef(BaseModel):
    ServiceUpdateName: Optional[str] = None
    ServiceUpdateStatus: Optional[Sequence[ServiceUpdateStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotsMessageDescribeSnapshotsPaginateTypeDef(BaseModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    SnapshotName: Optional[str] = None
    SnapshotSource: Optional[str] = None
    ShowNodeGroupConfig: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUserGroupsMessageDescribeUserGroupsPaginateTypeDef(BaseModel):
    UserGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsMessageDescribeEventsPaginateTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsMessageRequestTypeDef(BaseModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class TimeRangeFilterTypeDef(BaseModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None

class DescribeUsersMessageDescribeUsersPaginateTypeDef(BaseModel):
    Engine: Optional[str] = None
    UserId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUsersMessageRequestTypeDef(BaseModel):
    Engine: Optional[str] = None
    UserId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class DestinationDetailsTypeDef(BaseModel):
    CloudWatchLogsDetails: Optional[CloudWatchLogsDestinationDetailsTypeDef] = None
    KinesisFirehoseDetails: Optional[KinesisFirehoseDestinationDetailsTypeDef] = None

class EventsMessageTypeDef(BaseModel):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GlobalReplicationGroupTypeDef(BaseModel):
    GlobalReplicationGroupId: Optional[str] = None
    GlobalReplicationGroupDescription: Optional[str] = None
    Status: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    Members: Optional[List[GlobalReplicationGroupMemberTypeDef]] = None
    ClusterEnabled: Optional[bool] = None
    GlobalNodeGroups: Optional[List[GlobalNodeGroupTypeDef]] = None
    AuthTokenEnabled: Optional[bool] = None
    TransitEncryptionEnabled: Optional[bool] = None
    AtRestEncryptionEnabled: Optional[bool] = None
    ARN: Optional[str] = None

class ModifyCacheParameterGroupMessageRequestTypeDef(BaseModel):
    CacheParameterGroupName: str
    ParameterNameValues: Sequence[ParameterNameValueTypeDef]

class ResetCacheParameterGroupMessageRequestTypeDef(BaseModel):
    CacheParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    ParameterNameValues: Optional[Sequence[ParameterNameValueTypeDef]] = None

class ModifyReplicationGroupShardConfigurationMessageRequestTypeDef(BaseModel):
    ReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    ReshardingConfiguration: Optional[Sequence[ReshardingConfigurationTypeDef]] = None
    NodeGroupsToRemove: Optional[Sequence[str]] = None
    NodeGroupsToRetain: Optional[Sequence[str]] = None

class RegionalConfigurationTypeDef(BaseModel):
    ReplicationGroupId: str
    ReplicationGroupRegion: str
    ReshardingConfiguration: Sequence[ReshardingConfigurationTypeDef]

class NodeSnapshotTypeDef(BaseModel):
    CacheClusterId: Optional[str] = None
    NodeGroupId: Optional[str] = None
    CacheNodeId: Optional[str] = None
    NodeGroupConfiguration: Optional[NodeGroupConfigurationOutputTypeDef] = None
    CacheSize: Optional[str] = None
    CacheNodeCreateTime: Optional[datetime] = None
    SnapshotCreateTime: Optional[datetime] = None

class NodeGroupUpdateStatusTypeDef(BaseModel):
    NodeGroupId: Optional[str] = None
    NodeGroupMemberUpdateStatus: Optional[List[NodeGroupMemberUpdateStatusTypeDef]] = None

class ReservedCacheNodeTypeDef(BaseModel):
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
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None
    ReservationARN: Optional[str] = None

class ReservedCacheNodesOfferingTypeDef(BaseModel):
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None

class ReshardingStatusTypeDef(BaseModel):
    SlotMigration: Optional[SlotMigrationTypeDef] = None

class ServerlessCacheSnapshotTypeDef(BaseModel):
    ServerlessCacheSnapshotName: Optional[str] = None
    ARN: Optional[str] = None
    KmsKeyId: Optional[str] = None
    SnapshotType: Optional[str] = None
    Status: Optional[str] = None
    CreateTime: Optional[datetime] = None
    ExpiryTime: Optional[datetime] = None
    BytesUsedForCache: Optional[str] = None
    ServerlessCacheConfiguration: Optional[ServerlessCacheConfigurationTypeDef] = None

class ServiceUpdatesMessageTypeDef(BaseModel):
    Marker: str
    ServiceUpdates: List[ServiceUpdateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubnetTypeDef(BaseModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZoneTypeDef] = None
    SubnetOutpost: Optional[SubnetOutpostTypeDef] = None
    SupportedNetworkTypes: Optional[List[NetworkTypeType]] = None

class UpdateActionResultsMessageTypeDef(BaseModel):
    ProcessedUpdateActions: List[ProcessedUpdateActionTypeDef]
    UnprocessedUpdateActions: List[UnprocessedUpdateActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UserGroupResponseTypeDef(BaseModel):
    UserGroupId: str
    Status: str
    Engine: str
    UserIds: List[str]
    MinimumEngineVersion: str
    PendingChanges: UserGroupPendingChangesTypeDef
    ReplicationGroups: List[str]
    ServerlessCaches: List[str]
    ARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UserGroupTypeDef(BaseModel):
    UserGroupId: Optional[str] = None
    Status: Optional[str] = None
    Engine: Optional[str] = None
    UserIds: Optional[List[str]] = None
    MinimumEngineVersion: Optional[str] = None
    PendingChanges: Optional[UserGroupPendingChangesTypeDef] = None
    ReplicationGroups: Optional[List[str]] = None
    ServerlessCaches: Optional[List[str]] = None
    ARN: Optional[str] = None

class DescribeUsersResultTypeDef(BaseModel):
    Users: List[UserTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class NodeGroupTypeDef(BaseModel):
    NodeGroupId: Optional[str] = None
    Status: Optional[str] = None
    PrimaryEndpoint: Optional[EndpointTypeDef] = None
    ReaderEndpoint: Optional[EndpointTypeDef] = None
    Slots: Optional[str] = None
    NodeGroupMembers: Optional[List[NodeGroupMemberTypeDef]] = None

class CacheParameterGroupDetailsTypeDef(BaseModel):
    Marker: str
    Parameters: List[ParameterTypeDef]
    CacheNodeTypeSpecificParameters: List[CacheNodeTypeSpecificParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EngineDefaultsTypeDef(BaseModel):
    CacheParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[ParameterTypeDef]] = None
    CacheNodeTypeSpecificParameters: Optional[List[CacheNodeTypeSpecificParameterTypeDef]] = None

class AuthorizeCacheSecurityGroupIngressResultTypeDef(BaseModel):
    CacheSecurityGroup: CacheSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CacheSecurityGroupMessageTypeDef(BaseModel):
    Marker: str
    CacheSecurityGroups: List[CacheSecurityGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCacheSecurityGroupResultTypeDef(BaseModel):
    CacheSecurityGroup: CacheSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RevokeCacheSecurityGroupIngressResultTypeDef(BaseModel):
    CacheSecurityGroup: CacheSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServerlessCacheRequestRequestTypeDef(BaseModel):
    ServerlessCacheName: str
    Engine: str
    Description: Optional[str] = None
    MajorEngineVersion: Optional[str] = None
    CacheUsageLimits: Optional[CacheUsageLimitsTypeDef] = None
    KmsKeyId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    SnapshotArnsToRestore: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    UserGroupId: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    SnapshotRetentionLimit: Optional[int] = None
    DailySnapshotTime: Optional[str] = None

class ModifyServerlessCacheRequestRequestTypeDef(BaseModel):
    ServerlessCacheName: str
    Description: Optional[str] = None
    CacheUsageLimits: Optional[CacheUsageLimitsTypeDef] = None
    RemoveUserGroup: Optional[bool] = None
    UserGroupId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    SnapshotRetentionLimit: Optional[int] = None
    DailySnapshotTime: Optional[str] = None

class ServerlessCacheTypeDef(BaseModel):
    ServerlessCacheName: Optional[str] = None
    Description: Optional[str] = None
    CreateTime: Optional[datetime] = None
    Status: Optional[str] = None
    Engine: Optional[str] = None
    MajorEngineVersion: Optional[str] = None
    FullEngineVersion: Optional[str] = None
    CacheUsageLimits: Optional[CacheUsageLimitsTypeDef] = None
    KmsKeyId: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
    Endpoint: Optional[EndpointTypeDef] = None
    ReaderEndpoint: Optional[EndpointTypeDef] = None
    ARN: Optional[str] = None
    UserGroupId: Optional[str] = None
    SubnetIds: Optional[List[str]] = None
    SnapshotRetentionLimit: Optional[int] = None
    DailySnapshotTime: Optional[str] = None

class DescribeUpdateActionsMessageDescribeUpdateActionsPaginateTypeDef(BaseModel):
    ServiceUpdateName: Optional[str] = None
    ReplicationGroupIds: Optional[Sequence[str]] = None
    CacheClusterIds: Optional[Sequence[str]] = None
    Engine: Optional[str] = None
    ServiceUpdateStatus: Optional[Sequence[ServiceUpdateStatusType]] = None
    ServiceUpdateTimeRange: Optional[TimeRangeFilterTypeDef] = None
    UpdateActionStatus: Optional[Sequence[UpdateActionStatusType]] = None
    ShowNodeLevelUpdateStatus: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUpdateActionsMessageRequestTypeDef(BaseModel):
    ServiceUpdateName: Optional[str] = None
    ReplicationGroupIds: Optional[Sequence[str]] = None
    CacheClusterIds: Optional[Sequence[str]] = None
    Engine: Optional[str] = None
    ServiceUpdateStatus: Optional[Sequence[ServiceUpdateStatusType]] = None
    ServiceUpdateTimeRange: Optional[TimeRangeFilterTypeDef] = None
    UpdateActionStatus: Optional[Sequence[UpdateActionStatusType]] = None
    ShowNodeLevelUpdateStatus: Optional[bool] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None

class LogDeliveryConfigurationRequestTypeDef(BaseModel):
    LogType: Optional[LogTypeType] = None
    DestinationType: Optional[DestinationTypeType] = None
    DestinationDetails: Optional[DestinationDetailsTypeDef] = None
    LogFormat: Optional[LogFormatType] = None
    Enabled: Optional[bool] = None

class LogDeliveryConfigurationTypeDef(BaseModel):
    LogType: Optional[LogTypeType] = None
    DestinationType: Optional[DestinationTypeType] = None
    DestinationDetails: Optional[DestinationDetailsTypeDef] = None
    LogFormat: Optional[LogFormatType] = None
    Status: Optional[LogDeliveryConfigurationStatusType] = None
    Message: Optional[str] = None

class PendingLogDeliveryConfigurationTypeDef(BaseModel):
    LogType: Optional[LogTypeType] = None
    DestinationType: Optional[DestinationTypeType] = None
    DestinationDetails: Optional[DestinationDetailsTypeDef] = None
    LogFormat: Optional[LogFormatType] = None

class CreateGlobalReplicationGroupResultTypeDef(BaseModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef(BaseModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGlobalReplicationGroupResultTypeDef(BaseModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeGlobalReplicationGroupsResultTypeDef(BaseModel):
    Marker: str
    GlobalReplicationGroups: List[GlobalReplicationGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateGlobalReplicationGroupResultTypeDef(BaseModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverGlobalReplicationGroupResultTypeDef(BaseModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef(BaseModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyGlobalReplicationGroupResultTypeDef(BaseModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebalanceSlotsInGlobalReplicationGroupResultTypeDef(BaseModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IncreaseNodeGroupsInGlobalReplicationGroupMessageRequestTypeDef(BaseModel):
    GlobalReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    RegionalConfigurations: Optional[Sequence[RegionalConfigurationTypeDef]] = None

class SnapshotTypeDef(BaseModel):
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
    NodeSnapshots: Optional[List[NodeSnapshotTypeDef]] = None
    KmsKeyId: Optional[str] = None
    ARN: Optional[str] = None
    DataTiering: Optional[DataTieringStatusType] = None

class UpdateActionTypeDef(BaseModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    ServiceUpdateName: Optional[str] = None
    ServiceUpdateReleaseDate: Optional[datetime] = None
    ServiceUpdateSeverity: Optional[ServiceUpdateSeverityType] = None
    ServiceUpdateStatus: Optional[ServiceUpdateStatusType] = None
    ServiceUpdateRecommendedApplyByDate: Optional[datetime] = None
    ServiceUpdateType: Optional[Literal["security-update"]] = None
    UpdateActionAvailableDate: Optional[datetime] = None
    UpdateActionStatus: Optional[UpdateActionStatusType] = None
    NodesUpdated: Optional[str] = None
    UpdateActionStatusModifiedDate: Optional[datetime] = None
    SlaMet: Optional[SlaMetType] = None
    NodeGroupUpdateStatus: Optional[List[NodeGroupUpdateStatusTypeDef]] = None
    CacheNodeUpdateStatus: Optional[List[CacheNodeUpdateStatusTypeDef]] = None
    EstimatedUpdateTime: Optional[str] = None
    Engine: Optional[str] = None

class PurchaseReservedCacheNodesOfferingResultTypeDef(BaseModel):
    ReservedCacheNode: ReservedCacheNodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedCacheNodeMessageTypeDef(BaseModel):
    Marker: str
    ReservedCacheNodes: List[ReservedCacheNodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReservedCacheNodesOfferingMessageTypeDef(BaseModel):
    Marker: str
    ReservedCacheNodesOfferings: List[ReservedCacheNodesOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CopyServerlessCacheSnapshotResponseTypeDef(BaseModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServerlessCacheSnapshotResponseTypeDef(BaseModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServerlessCacheSnapshotResponseTypeDef(BaseModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServerlessCacheSnapshotsResponseTypeDef(BaseModel):
    ServerlessCacheSnapshots: List[ServerlessCacheSnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ExportServerlessCacheSnapshotResponseTypeDef(BaseModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CacheSubnetGroupTypeDef(BaseModel):
    CacheSubnetGroupName: Optional[str] = None
    CacheSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None
    ARN: Optional[str] = None
    SupportedNetworkTypes: Optional[List[NetworkTypeType]] = None

class DescribeUserGroupsResultTypeDef(BaseModel):
    UserGroups: List[UserGroupTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEngineDefaultParametersResultTypeDef(BaseModel):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateServerlessCacheResponseTypeDef(BaseModel):
    ServerlessCache: ServerlessCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServerlessCacheResponseTypeDef(BaseModel):
    ServerlessCache: ServerlessCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServerlessCachesResponseTypeDef(BaseModel):
    ServerlessCaches: List[ServerlessCacheTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ModifyServerlessCacheResponseTypeDef(BaseModel):
    ServerlessCache: ServerlessCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCacheClusterMessageRequestTypeDef(BaseModel):
    CacheClusterId: str
    ReplicationGroupId: Optional[str] = None
    AZMode: Optional[AZModeType] = None
    PreferredAvailabilityZone: Optional[str] = None
    PreferredAvailabilityZones: Optional[Sequence[str]] = None
    NumCacheNodes: Optional[int] = None
    CacheNodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupName: Optional[str] = None
    CacheSubnetGroupName: Optional[str] = None
    CacheSecurityGroupNames: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SnapshotArns: Optional[Sequence[str]] = None
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
    PreferredOutpostArns: Optional[Sequence[str]] = None
    LogDeliveryConfigurations: Optional[Sequence[LogDeliveryConfigurationRequestTypeDef]] = None
    TransitEncryptionEnabled: Optional[bool] = None
    NetworkType: Optional[NetworkTypeType] = None
    IpDiscovery: Optional[IpDiscoveryType] = None

class CreateReplicationGroupMessageRequestTypeDef(BaseModel):
    ReplicationGroupId: str
    ReplicationGroupDescription: str
    GlobalReplicationGroupId: Optional[str] = None
    PrimaryClusterId: Optional[str] = None
    AutomaticFailoverEnabled: Optional[bool] = None
    MultiAZEnabled: Optional[bool] = None
    NumCacheClusters: Optional[int] = None
    PreferredCacheClusterAZs: Optional[Sequence[str]] = None
    NumNodeGroups: Optional[int] = None
    ReplicasPerNodeGroup: Optional[int] = None
    NodeGroupConfiguration: Optional[Sequence[NodeGroupConfigurationUnionTypeDef]] = None
    CacheNodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupName: Optional[str] = None
    CacheSubnetGroupName: Optional[str] = None
    CacheSecurityGroupNames: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    SnapshotArns: Optional[Sequence[str]] = None
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
    UserGroupIds: Optional[Sequence[str]] = None
    LogDeliveryConfigurations: Optional[Sequence[LogDeliveryConfigurationRequestTypeDef]] = None
    DataTieringEnabled: Optional[bool] = None
    NetworkType: Optional[NetworkTypeType] = None
    IpDiscovery: Optional[IpDiscoveryType] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None
    ClusterMode: Optional[ClusterModeType] = None
    ServerlessCacheSnapshotName: Optional[str] = None

class ModifyCacheClusterMessageRequestTypeDef(BaseModel):
    CacheClusterId: str
    NumCacheNodes: Optional[int] = None
    CacheNodeIdsToRemove: Optional[Sequence[str]] = None
    AZMode: Optional[AZModeType] = None
    NewAvailabilityZones: Optional[Sequence[str]] = None
    CacheSecurityGroupNames: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    PreferredMaintenanceWindow: Optional[str] = None
    NotificationTopicArn: Optional[str] = None
    CacheParameterGroupName: Optional[str] = None
    NotificationTopicStatus: Optional[str] = None
    ApplyImmediately: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    SnapshotRetentionLimit: Optional[int] = None
    SnapshotWindow: Optional[str] = None
    CacheNodeType: Optional[str] = None
    AuthToken: Optional[str] = None
    AuthTokenUpdateStrategy: Optional[AuthTokenUpdateStrategyTypeType] = None
    LogDeliveryConfigurations: Optional[Sequence[LogDeliveryConfigurationRequestTypeDef]] = None
    IpDiscovery: Optional[IpDiscoveryType] = None

class ModifyReplicationGroupMessageRequestTypeDef(BaseModel):
    ReplicationGroupId: str
    ReplicationGroupDescription: Optional[str] = None
    PrimaryClusterId: Optional[str] = None
    SnapshottingClusterId: Optional[str] = None
    AutomaticFailoverEnabled: Optional[bool] = None
    MultiAZEnabled: Optional[bool] = None
    NodeGroupId: Optional[str] = None
    CacheSecurityGroupNames: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    PreferredMaintenanceWindow: Optional[str] = None
    NotificationTopicArn: Optional[str] = None
    CacheParameterGroupName: Optional[str] = None
    NotificationTopicStatus: Optional[str] = None
    ApplyImmediately: Optional[bool] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    SnapshotRetentionLimit: Optional[int] = None
    SnapshotWindow: Optional[str] = None
    CacheNodeType: Optional[str] = None
    AuthToken: Optional[str] = None
    AuthTokenUpdateStrategy: Optional[AuthTokenUpdateStrategyTypeType] = None
    UserGroupIdsToAdd: Optional[Sequence[str]] = None
    UserGroupIdsToRemove: Optional[Sequence[str]] = None
    RemoveUserGroups: Optional[bool] = None
    LogDeliveryConfigurations: Optional[Sequence[LogDeliveryConfigurationRequestTypeDef]] = None
    IpDiscovery: Optional[IpDiscoveryType] = None
    TransitEncryptionEnabled: Optional[bool] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None
    ClusterMode: Optional[ClusterModeType] = None

class PendingModifiedValuesTypeDef(BaseModel):
    NumCacheNodes: Optional[int] = None
    CacheNodeIdsToRemove: Optional[List[str]] = None
    EngineVersion: Optional[str] = None
    CacheNodeType: Optional[str] = None
    AuthTokenStatus: Optional[AuthTokenUpdateStatusType] = None
    LogDeliveryConfigurations: Optional[List[PendingLogDeliveryConfigurationTypeDef]] = None
    TransitEncryptionEnabled: Optional[bool] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None

class ReplicationGroupPendingModifiedValuesTypeDef(BaseModel):
    PrimaryClusterId: Optional[str] = None
    AutomaticFailoverStatus: Optional[PendingAutomaticFailoverStatusType] = None
    Resharding: Optional[ReshardingStatusTypeDef] = None
    AuthTokenStatus: Optional[AuthTokenUpdateStatusType] = None
    UserGroups: Optional[UserGroupsUpdateStatusTypeDef] = None
    LogDeliveryConfigurations: Optional[List[PendingLogDeliveryConfigurationTypeDef]] = None
    TransitEncryptionEnabled: Optional[bool] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None
    ClusterMode: Optional[ClusterModeType] = None

class CopySnapshotResultTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSnapshotResultTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotResultTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotsListMessageTypeDef(BaseModel):
    Marker: str
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateActionsMessageTypeDef(BaseModel):
    Marker: str
    UpdateActions: List[UpdateActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CacheSubnetGroupMessageTypeDef(BaseModel):
    Marker: str
    CacheSubnetGroups: List[CacheSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCacheSubnetGroupResultTypeDef(BaseModel):
    CacheSubnetGroup: CacheSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCacheSubnetGroupResultTypeDef(BaseModel):
    CacheSubnetGroup: CacheSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CacheClusterTypeDef(BaseModel):
    CacheClusterId: Optional[str] = None
    ConfigurationEndpoint: Optional[EndpointTypeDef] = None
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
    PendingModifiedValues: Optional[PendingModifiedValuesTypeDef] = None
    NotificationConfiguration: Optional[NotificationConfigurationTypeDef] = None
    CacheSecurityGroups: Optional[List[CacheSecurityGroupMembershipTypeDef]] = None
    CacheParameterGroup: Optional[CacheParameterGroupStatusTypeDef] = None
    CacheSubnetGroupName: Optional[str] = None
    CacheNodes: Optional[List[CacheNodeTypeDef]] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    SecurityGroups: Optional[List[SecurityGroupMembershipTypeDef]] = None
    ReplicationGroupId: Optional[str] = None
    SnapshotRetentionLimit: Optional[int] = None
    SnapshotWindow: Optional[str] = None
    AuthTokenEnabled: Optional[bool] = None
    AuthTokenLastModifiedDate: Optional[datetime] = None
    TransitEncryptionEnabled: Optional[bool] = None
    AtRestEncryptionEnabled: Optional[bool] = None
    ARN: Optional[str] = None
    ReplicationGroupLogDeliveryEnabled: Optional[bool] = None
    LogDeliveryConfigurations: Optional[List[LogDeliveryConfigurationTypeDef]] = None
    NetworkType: Optional[NetworkTypeType] = None
    IpDiscovery: Optional[IpDiscoveryType] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None

class ReplicationGroupTypeDef(BaseModel):
    ReplicationGroupId: Optional[str] = None
    Description: Optional[str] = None
    GlobalReplicationGroupInfo: Optional[GlobalReplicationGroupInfoTypeDef] = None
    Status: Optional[str] = None
    PendingModifiedValues: Optional[ReplicationGroupPendingModifiedValuesTypeDef] = None
    MemberClusters: Optional[List[str]] = None
    NodeGroups: Optional[List[NodeGroupTypeDef]] = None
    SnapshottingClusterId: Optional[str] = None
    AutomaticFailover: Optional[AutomaticFailoverStatusType] = None
    MultiAZ: Optional[MultiAZStatusType] = None
    ConfigurationEndpoint: Optional[EndpointTypeDef] = None
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
    LogDeliveryConfigurations: Optional[List[LogDeliveryConfigurationTypeDef]] = None
    ReplicationGroupCreateTime: Optional[datetime] = None
    DataTiering: Optional[DataTieringStatusType] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    NetworkType: Optional[NetworkTypeType] = None
    IpDiscovery: Optional[IpDiscoveryType] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None
    ClusterMode: Optional[ClusterModeType] = None

class CacheClusterMessageTypeDef(BaseModel):
    Marker: str
    CacheClusters: List[CacheClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCacheClusterResultTypeDef(BaseModel):
    CacheCluster: CacheClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCacheClusterResultTypeDef(BaseModel):
    CacheCluster: CacheClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyCacheClusterResultTypeDef(BaseModel):
    CacheCluster: CacheClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootCacheClusterResultTypeDef(BaseModel):
    CacheCluster: CacheClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CompleteMigrationResponseTypeDef(BaseModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateReplicationGroupResultTypeDef(BaseModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DecreaseReplicaCountResultTypeDef(BaseModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteReplicationGroupResultTypeDef(BaseModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IncreaseReplicaCountResultTypeDef(BaseModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReplicationGroupResultTypeDef(BaseModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ModifyReplicationGroupShardConfigurationResultTypeDef(BaseModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationGroupMessageTypeDef(BaseModel):
    Marker: str
    ReplicationGroups: List[ReplicationGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartMigrationResponseTypeDef(BaseModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TestFailoverResultTypeDef(BaseModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TestMigrationResponseTypeDef(BaseModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

