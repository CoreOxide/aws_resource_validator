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
from aws_resource_validator.pydantic_models.elasticache_constants import *

class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AuthorizeCacheSecurityGroupIngressMessage(BaseValidatorModel):
    CacheSecurityGroupName: str
    EC2SecurityGroupName: str
    EC2SecurityGroupOwnerId: str


class AvailabilityZone(BaseValidatorModel):
    Name: Optional[str] = None


class BatchApplyUpdateActionMessage(BaseValidatorModel):
    ServiceUpdateName: str
    ReplicationGroupIds: Optional[Sequence[str]] = None
    CacheClusterIds: Optional[Sequence[str]] = None


class BatchStopUpdateActionMessage(BaseValidatorModel):
    ServiceUpdateName: str
    ReplicationGroupIds: Optional[Sequence[str]] = None
    CacheClusterIds: Optional[Sequence[str]] = None


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
    Unit: Literal["GB"]
    Maximum: Optional[int] = None
    Minimum: Optional[int] = None


class ECPUPerSecond(BaseValidatorModel):
    Maximum: Optional[int] = None
    Minimum: Optional[int] = None


class CloudWatchLogsDestinationDetails(BaseValidatorModel):
    LogGroup: Optional[str] = None


class CompleteMigrationMessage(BaseValidatorModel):
    ReplicationGroupId: str
    Force: Optional[bool] = None


class ConfigureShard(BaseValidatorModel):
    NodeGroupId: str
    NewReplicaCount: int
    PreferredAvailabilityZones: Optional[Sequence[str]] = None
    PreferredOutpostArns: Optional[Sequence[str]] = None


class CreateGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupIdSuffix: str
    PrimaryReplicationGroupId: str
    GlobalReplicationGroupDescription: Optional[str] = None


class CustomerNodeEndpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None


class DecreaseNodeGroupsInGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    GlobalNodeGroupsToRemove: Optional[Sequence[str]] = None
    GlobalNodeGroupsToRetain: Optional[Sequence[str]] = None


class DeleteCacheClusterMessage(BaseValidatorModel):
    CacheClusterId: str
    FinalSnapshotIdentifier: Optional[str] = None


class DeleteCacheParameterGroupMessage(BaseValidatorModel):
    CacheParameterGroupName: str


class DeleteCacheSecurityGroupMessage(BaseValidatorModel):
    CacheSecurityGroupName: str


class DeleteCacheSubnetGroupMessage(BaseValidatorModel):
    CacheSubnetGroupName: str


class DeleteGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupId: str
    RetainPrimaryReplicationGroup: bool


class DeleteReplicationGroupMessage(BaseValidatorModel):
    ReplicationGroupId: str
    RetainPrimaryCluster: Optional[bool] = None
    FinalSnapshotIdentifier: Optional[str] = None


class DeleteServerlessCacheRequest(BaseValidatorModel):
    ServerlessCacheName: str
    FinalSnapshotName: Optional[str] = None


class DeleteServerlessCacheSnapshotRequest(BaseValidatorModel):
    ServerlessCacheSnapshotName: str


class DeleteSnapshotMessage(BaseValidatorModel):
    SnapshotName: str


class DeleteUserGroupMessage(BaseValidatorModel):
    UserGroupId: str


class DeleteUserMessage(BaseValidatorModel):
    UserId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeCacheClustersMessage(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowCacheNodeInfo: Optional[bool] = None
    ShowCacheClustersNotInReplicationGroups: Optional[bool] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeCacheEngineVersionsMessage(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupFamily: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DefaultOnly: Optional[bool] = None


class DescribeCacheParameterGroupsMessage(BaseValidatorModel):
    CacheParameterGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeCacheParametersMessage(BaseValidatorModel):
    CacheParameterGroupName: str
    Source: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeCacheSecurityGroupsMessage(BaseValidatorModel):
    CacheSecurityGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeCacheSubnetGroupsMessage(BaseValidatorModel):
    CacheSubnetGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEngineDefaultParametersMessage(BaseValidatorModel):
    CacheParameterGroupFamily: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeGlobalReplicationGroupsMessage(BaseValidatorModel):
    GlobalReplicationGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowMemberInfo: Optional[bool] = None


class DescribeReplicationGroupsMessage(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReservedCacheNodesMessage(BaseValidatorModel):
    ReservedCacheNodeId: Optional[str] = None
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReservedCacheNodesOfferingsMessage(BaseValidatorModel):
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeServerlessCacheSnapshotsRequest(BaseValidatorModel):
    ServerlessCacheName: Optional[str] = None
    ServerlessCacheSnapshotName: Optional[str] = None
    SnapshotType: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeServerlessCachesRequest(BaseValidatorModel):
    ServerlessCacheName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeServiceUpdatesMessage(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ServiceUpdateStatus: Optional[Sequence[ServiceUpdateStatusType]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeSnapshotsMessage(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    SnapshotName: Optional[str] = None
    SnapshotSource: Optional[str] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    ShowNodeGroupConfig: Optional[bool] = None


class DescribeUserGroupsMessage(BaseValidatorModel):
    UserGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class Filter(BaseValidatorModel):
    Name: str
    Values: Sequence[str]


class KinesisFirehoseDestinationDetails(BaseValidatorModel):
    DeliveryStream: Optional[str] = None


class DisassociateGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupId: str
    ReplicationGroupId: str
    ReplicationGroupRegion: str


class Event(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    Date: Optional[datetime] = None


class ExportServerlessCacheSnapshotRequest(BaseValidatorModel):
    ServerlessCacheSnapshotName: str
    S3BucketName: str


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


class ListAllowedNodeTypeModificationsMessage(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    ReplicationGroupId: Optional[str] = None


class ListTagsForResourceMessage(BaseValidatorModel):
    ResourceName: str


class ParameterNameValue(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None


class ModifyCacheSubnetGroupMessage(BaseValidatorModel):
    CacheSubnetGroupName: str
    CacheSubnetGroupDescription: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None


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
    PreferredAvailabilityZones: Optional[Sequence[str]] = None


class ModifyUserGroupMessage(BaseValidatorModel):
    UserGroupId: str
    UserIdsToAdd: Optional[Sequence[str]] = None
    UserIdsToRemove: Optional[Sequence[str]] = None
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
    ReplicaAvailabilityZones: Optional[Sequence[str]] = None
    PrimaryOutpostArn: Optional[str] = None
    ReplicaOutpostArns: Optional[Sequence[str]] = None


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


class RebalanceSlotsInGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupId: str
    ApplyImmediately: bool


class RebootCacheClusterMessage(BaseValidatorModel):
    CacheClusterId: str
    CacheNodeIdsToReboot: Sequence[str]


class RecurringCharge(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None


class RemoveTagsFromResourceMessage(BaseValidatorModel):
    ResourceName: str
    TagKeys: Sequence[str]


class UserGroupsUpdateStatus(BaseValidatorModel):
    UserGroupIdsToAdd: Optional[List[str]] = None
    UserGroupIdsToRemove: Optional[List[str]] = None


class SlotMigration(BaseValidatorModel):
    ProgressPercentage: Optional[float] = None


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
    ServiceUpdateType: Optional[Literal["security-update"]] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    AutoUpdateAfterRecommendedApplyByDate: Optional[bool] = None
    EstimatedUpdateTime: Optional[str] = None


class SubnetOutpost(BaseValidatorModel):
    SubnetOutpostArn: Optional[str] = None


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


class AddTagsToResourceMessage(BaseValidatorModel):
    ResourceName: str
    Tags: Sequence[Tag]


class CopyServerlessCacheSnapshotRequest(BaseValidatorModel):
    SourceServerlessCacheSnapshotName: str
    TargetServerlessCacheSnapshotName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CopySnapshotMessage(BaseValidatorModel):
    SourceSnapshotName: str
    TargetSnapshotName: str
    TargetBucket: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateCacheParameterGroupMessage(BaseValidatorModel):
    CacheParameterGroupName: str
    CacheParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[Tag]] = None


class CreateCacheSecurityGroupMessage(BaseValidatorModel):
    CacheSecurityGroupName: str
    Description: str
    Tags: Optional[Sequence[Tag]] = None


class CreateCacheSubnetGroupMessage(BaseValidatorModel):
    CacheSubnetGroupName: str
    CacheSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: Optional[Sequence[Tag]] = None


class CreateServerlessCacheSnapshotRequest(BaseValidatorModel):
    ServerlessCacheSnapshotName: str
    ServerlessCacheName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateSnapshotMessage(BaseValidatorModel):
    SnapshotName: str
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateUserGroupMessage(BaseValidatorModel):
    UserGroupId: str
    Engine: str
    UserIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None


class PurchaseReservedCacheNodesOfferingMessage(BaseValidatorModel):
    ReservedCacheNodesOfferingId: str
    ReservedCacheNodeId: Optional[str] = None
    CacheNodeCount: Optional[int] = None
    Tags: Optional[Sequence[Tag]] = None


class AllowedNodeTypeModificationsMessage(BaseValidatorModel):
    ScaleUpModifications: List[str]
    ScaleDownModifications: List[str]
    ResponseMetadata: ResponseMetadata


class CacheParameterGroupNameMessage(BaseValidatorModel):
    CacheParameterGroupName: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class TagListMessage(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class AuthenticationMode(BaseValidatorModel):
    pass


class CreateUserMessage(BaseValidatorModel):
    UserId: str
    UserName: str
    Engine: str
    AccessString: str
    Passwords: Optional[Sequence[str]] = None
    NoPasswordRequired: Optional[bool] = None
    Tags: Optional[Sequence[Tag]] = None
    AuthenticationMode: Optional[AuthenticationMode] = None


class ModifyUserMessage(BaseValidatorModel):
    UserId: str
    AccessString: Optional[str] = None
    AppendAccessString: Optional[str] = None
    Passwords: Optional[Sequence[str]] = None
    NoPasswordRequired: Optional[bool] = None
    AuthenticationMode: Optional[AuthenticationMode] = None
    Engine: Optional[str] = None


class Authentication(BaseValidatorModel):
    pass


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


class CacheParameterGroupsMessage(BaseValidatorModel):
    Marker: str
    CacheParameterGroups: List[CacheParameterGroup]
    ResponseMetadata: ResponseMetadata


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


class DecreaseReplicaCountMessage(BaseValidatorModel):
    ReplicationGroupId: str
    ApplyImmediately: bool
    NewReplicaCount: Optional[int] = None
    ReplicaConfiguration: Optional[Sequence[ConfigureShard]] = None
    ReplicasToRemove: Optional[Sequence[str]] = None


class IncreaseReplicaCountMessage(BaseValidatorModel):
    ReplicationGroupId: str
    ApplyImmediately: bool
    NewReplicaCount: Optional[int] = None
    ReplicaConfiguration: Optional[Sequence[ConfigureShard]] = None


class StartMigrationMessage(BaseValidatorModel):
    ReplicationGroupId: str
    CustomerNodeEndpointList: Sequence[CustomerNodeEndpoint]


class TestMigrationMessage(BaseValidatorModel):
    ReplicationGroupId: str
    CustomerNodeEndpointList: Sequence[CustomerNodeEndpoint]


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
    ServiceUpdateStatus: Optional[Sequence[ServiceUpdateStatusType]] = None
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


class Timestamp(BaseValidatorModel):
    pass


class DescribeEventsMessagePaginate(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


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
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeUsersMessage(BaseValidatorModel):
    Engine: Optional[str] = None
    UserId: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DestinationDetails(BaseValidatorModel):
    CloudWatchLogsDetails: Optional[CloudWatchLogsDestinationDetails] = None
    KinesisFirehoseDetails: Optional[KinesisFirehoseDestinationDetails] = None


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


class ModifyCacheParameterGroupMessage(BaseValidatorModel):
    CacheParameterGroupName: str
    ParameterNameValues: Sequence[ParameterNameValue]


class ResetCacheParameterGroupMessage(BaseValidatorModel):
    CacheParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    ParameterNameValues: Optional[Sequence[ParameterNameValue]] = None


class ModifyReplicationGroupShardConfigurationMessage(BaseValidatorModel):
    ReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    ReshardingConfiguration: Optional[Sequence[ReshardingConfiguration]] = None
    NodeGroupsToRemove: Optional[Sequence[str]] = None
    NodeGroupsToRetain: Optional[Sequence[str]] = None


class RegionalConfiguration(BaseValidatorModel):
    ReplicationGroupId: str
    ReplicationGroupRegion: str
    ReshardingConfiguration: Sequence[ReshardingConfiguration]


class NodeSnapshot(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    NodeGroupId: Optional[str] = None
    CacheNodeId: Optional[str] = None
    NodeGroupConfiguration: Optional[NodeGroupConfigurationOutput] = None
    CacheSize: Optional[str] = None
    CacheNodeCreateTime: Optional[datetime] = None
    SnapshotCreateTime: Optional[datetime] = None


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


class ServiceUpdatesMessage(BaseValidatorModel):
    Marker: str
    ServiceUpdates: List[ServiceUpdate]
    ResponseMetadata: ResponseMetadata


class Subnet(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZone] = None
    SubnetOutpost: Optional[SubnetOutpost] = None
    SupportedNetworkTypes: Optional[List[NetworkTypeType]] = None


class UpdateActionResultsMessage(BaseValidatorModel):
    ProcessedUpdateActions: List[ProcessedUpdateAction]
    UnprocessedUpdateActions: List[UnprocessedUpdateAction]
    ResponseMetadata: ResponseMetadata


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


class AuthorizeCacheSecurityGroupIngressResult(BaseValidatorModel):
    CacheSecurityGroup: CacheSecurityGroup
    ResponseMetadata: ResponseMetadata


class CacheSecurityGroupMessage(BaseValidatorModel):
    Marker: str
    CacheSecurityGroups: List[CacheSecurityGroup]
    ResponseMetadata: ResponseMetadata


class CreateCacheSecurityGroupResult(BaseValidatorModel):
    CacheSecurityGroup: CacheSecurityGroup
    ResponseMetadata: ResponseMetadata


class RevokeCacheSecurityGroupIngressResult(BaseValidatorModel):
    CacheSecurityGroup: CacheSecurityGroup
    ResponseMetadata: ResponseMetadata


class CreateServerlessCacheRequest(BaseValidatorModel):
    ServerlessCacheName: str
    Engine: str
    Description: Optional[str] = None
    MajorEngineVersion: Optional[str] = None
    CacheUsageLimits: Optional[CacheUsageLimits] = None
    KmsKeyId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    SnapshotArnsToRestore: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None
    UserGroupId: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None
    SnapshotRetentionLimit: Optional[int] = None
    DailySnapshotTime: Optional[str] = None


class ModifyServerlessCacheRequest(BaseValidatorModel):
    ServerlessCacheName: str
    Description: Optional[str] = None
    CacheUsageLimits: Optional[CacheUsageLimits] = None
    RemoveUserGroup: Optional[bool] = None
    UserGroupId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
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
    ReplicationGroupIds: Optional[Sequence[str]] = None
    CacheClusterIds: Optional[Sequence[str]] = None
    Engine: Optional[str] = None
    ServiceUpdateStatus: Optional[Sequence[ServiceUpdateStatusType]] = None
    ServiceUpdateTimeRange: Optional[TimeRangeFilter] = None
    UpdateActionStatus: Optional[Sequence[UpdateActionStatusType]] = None
    ShowNodeLevelUpdateStatus: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeUpdateActionsMessage(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ReplicationGroupIds: Optional[Sequence[str]] = None
    CacheClusterIds: Optional[Sequence[str]] = None
    Engine: Optional[str] = None
    ServiceUpdateStatus: Optional[Sequence[ServiceUpdateStatusType]] = None
    ServiceUpdateTimeRange: Optional[TimeRangeFilter] = None
    UpdateActionStatus: Optional[Sequence[UpdateActionStatusType]] = None
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


class CreateGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


class DecreaseNodeGroupsInGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


class DeleteGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


class DescribeGlobalReplicationGroupsResult(BaseValidatorModel):
    Marker: str
    GlobalReplicationGroups: List[GlobalReplicationGroup]
    ResponseMetadata: ResponseMetadata


class DisassociateGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


class FailoverGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


class IncreaseNodeGroupsInGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


class ModifyGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


class RebalanceSlotsInGlobalReplicationGroupResult(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroup
    ResponseMetadata: ResponseMetadata


class IncreaseNodeGroupsInGlobalReplicationGroupMessage(BaseValidatorModel):
    GlobalReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    RegionalConfigurations: Optional[Sequence[RegionalConfiguration]] = None


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
    ServiceUpdateType: Optional[Literal["security-update"]] = None
    UpdateActionAvailableDate: Optional[datetime] = None
    UpdateActionStatus: Optional[UpdateActionStatusType] = None
    NodesUpdated: Optional[str] = None
    UpdateActionStatusModifiedDate: Optional[datetime] = None
    SlaMet: Optional[SlaMetType] = None
    NodeGroupUpdateStatus: Optional[List[NodeGroupUpdateStatus]] = None
    CacheNodeUpdateStatus: Optional[List[CacheNodeUpdateStatus]] = None
    EstimatedUpdateTime: Optional[str] = None
    Engine: Optional[str] = None


class PurchaseReservedCacheNodesOfferingResult(BaseValidatorModel):
    ReservedCacheNode: ReservedCacheNode
    ResponseMetadata: ResponseMetadata


class ReservedCacheNodeMessage(BaseValidatorModel):
    Marker: str
    ReservedCacheNodes: List[ReservedCacheNode]
    ResponseMetadata: ResponseMetadata


class ReservedCacheNodesOfferingMessage(BaseValidatorModel):
    Marker: str
    ReservedCacheNodesOfferings: List[ReservedCacheNodesOffering]
    ResponseMetadata: ResponseMetadata


class CopyServerlessCacheSnapshotResponse(BaseValidatorModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshot
    ResponseMetadata: ResponseMetadata


class CreateServerlessCacheSnapshotResponse(BaseValidatorModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshot
    ResponseMetadata: ResponseMetadata


class DeleteServerlessCacheSnapshotResponse(BaseValidatorModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshot
    ResponseMetadata: ResponseMetadata


class DescribeServerlessCacheSnapshotsResponse(BaseValidatorModel):
    ServerlessCacheSnapshots: List[ServerlessCacheSnapshot]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


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


class DescribeUserGroupsResult(BaseValidatorModel):
    UserGroups: List[UserGroup]
    Marker: str
    ResponseMetadata: ResponseMetadata


class DescribeEngineDefaultParametersResult(BaseValidatorModel):
    EngineDefaults: EngineDefaults
    ResponseMetadata: ResponseMetadata


class CreateServerlessCacheResponse(BaseValidatorModel):
    ServerlessCache: ServerlessCache
    ResponseMetadata: ResponseMetadata


class DeleteServerlessCacheResponse(BaseValidatorModel):
    ServerlessCache: ServerlessCache
    ResponseMetadata: ResponseMetadata


class DescribeServerlessCachesResponse(BaseValidatorModel):
    ServerlessCaches: List[ServerlessCache]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ModifyServerlessCacheResponse(BaseValidatorModel):
    ServerlessCache: ServerlessCache
    ResponseMetadata: ResponseMetadata


class CreateCacheClusterMessage(BaseValidatorModel):
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
    Tags: Optional[Sequence[Tag]] = None
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
    LogDeliveryConfigurations: Optional[Sequence[LogDeliveryConfigurationRequest]] = None
    TransitEncryptionEnabled: Optional[bool] = None
    NetworkType: Optional[NetworkTypeType] = None
    IpDiscovery: Optional[IpDiscoveryType] = None


class NodeGroupConfigurationUnion(BaseValidatorModel):
    pass


class CreateReplicationGroupMessage(BaseValidatorModel):
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
    NodeGroupConfiguration: Optional[Sequence[NodeGroupConfigurationUnion]] = None
    CacheNodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupName: Optional[str] = None
    CacheSubnetGroupName: Optional[str] = None
    CacheSecurityGroupNames: Optional[Sequence[str]] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None
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
    LogDeliveryConfigurations: Optional[Sequence[LogDeliveryConfigurationRequest]] = None
    DataTieringEnabled: Optional[bool] = None
    NetworkType: Optional[NetworkTypeType] = None
    IpDiscovery: Optional[IpDiscoveryType] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None
    ClusterMode: Optional[ClusterModeType] = None
    ServerlessCacheSnapshotName: Optional[str] = None


class ModifyCacheClusterMessage(BaseValidatorModel):
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
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    SnapshotRetentionLimit: Optional[int] = None
    SnapshotWindow: Optional[str] = None
    CacheNodeType: Optional[str] = None
    AuthToken: Optional[str] = None
    AuthTokenUpdateStrategy: Optional[AuthTokenUpdateStrategyTypeType] = None
    LogDeliveryConfigurations: Optional[Sequence[LogDeliveryConfigurationRequest]] = None
    IpDiscovery: Optional[IpDiscoveryType] = None


class ModifyReplicationGroupMessage(BaseValidatorModel):
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
    Engine: Optional[str] = None
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
    LogDeliveryConfigurations: Optional[Sequence[LogDeliveryConfigurationRequest]] = None
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


class CopySnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class CreateSnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class DeleteSnapshotResult(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class DescribeSnapshotsListMessage(BaseValidatorModel):
    Marker: str
    Snapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata


class UpdateActionsMessage(BaseValidatorModel):
    Marker: str
    UpdateActions: List[UpdateAction]
    ResponseMetadata: ResponseMetadata


class CacheSubnetGroupMessage(BaseValidatorModel):
    Marker: str
    CacheSubnetGroups: List[CacheSubnetGroup]
    ResponseMetadata: ResponseMetadata


class CreateCacheSubnetGroupResult(BaseValidatorModel):
    CacheSubnetGroup: CacheSubnetGroup
    ResponseMetadata: ResponseMetadata


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


class CacheClusterMessage(BaseValidatorModel):
    Marker: str
    CacheClusters: List[CacheCluster]
    ResponseMetadata: ResponseMetadata


class CreateCacheClusterResult(BaseValidatorModel):
    CacheCluster: CacheCluster
    ResponseMetadata: ResponseMetadata


class DeleteCacheClusterResult(BaseValidatorModel):
    CacheCluster: CacheCluster
    ResponseMetadata: ResponseMetadata


class ModifyCacheClusterResult(BaseValidatorModel):
    CacheCluster: CacheCluster
    ResponseMetadata: ResponseMetadata


class RebootCacheClusterResult(BaseValidatorModel):
    CacheCluster: CacheCluster
    ResponseMetadata: ResponseMetadata


class CompleteMigrationResponse(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


class CreateReplicationGroupResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


class DecreaseReplicaCountResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


class DeleteReplicationGroupResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


class IncreaseReplicaCountResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


class ModifyReplicationGroupResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


class ModifyReplicationGroupShardConfigurationResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


class ReplicationGroupMessage(BaseValidatorModel):
    Marker: str
    ReplicationGroups: List[ReplicationGroup]
    ResponseMetadata: ResponseMetadata


class StartMigrationResponse(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


class TestFailoverResult(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


class TestMigrationResponse(BaseValidatorModel):
    ReplicationGroup: ReplicationGroup
    ResponseMetadata: ResponseMetadata


