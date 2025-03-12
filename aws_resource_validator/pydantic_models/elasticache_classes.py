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

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AuthorizeCacheSecurityGroupIngressMessageTypeDef(BaseValidatorModel):
    CacheSecurityGroupName: str
    EC2SecurityGroupName: str
    EC2SecurityGroupOwnerId: str


class AvailabilityZoneTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class BatchApplyUpdateActionMessageTypeDef(BaseValidatorModel):
    ServiceUpdateName: str
    ReplicationGroupIds: Optional[Sequence[str]] = None
    CacheClusterIds: Optional[Sequence[str]] = None


class BatchStopUpdateActionMessageTypeDef(BaseValidatorModel):
    ServiceUpdateName: str
    ReplicationGroupIds: Optional[Sequence[str]] = None
    CacheClusterIds: Optional[Sequence[str]] = None


class CacheParameterGroupStatusTypeDef(BaseValidatorModel):
    CacheParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    CacheNodeIdsToReboot: Optional[List[str]] = None


class CacheSecurityGroupMembershipTypeDef(BaseValidatorModel):
    CacheSecurityGroupName: Optional[str] = None
    Status: Optional[str] = None


class EndpointTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None


class NotificationConfigurationTypeDef(BaseValidatorModel):
    TopicArn: Optional[str] = None
    TopicStatus: Optional[str] = None


class SecurityGroupMembershipTypeDef(BaseValidatorModel):
    SecurityGroupId: Optional[str] = None
    Status: Optional[str] = None


class CacheEngineVersionTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupFamily: Optional[str] = None
    CacheEngineDescription: Optional[str] = None
    CacheEngineVersionDescription: Optional[str] = None


class CacheNodeTypeSpecificValueTypeDef(BaseValidatorModel):
    CacheNodeType: Optional[str] = None
    Value: Optional[str] = None


class CacheNodeUpdateStatusTypeDef(BaseValidatorModel):
    CacheNodeId: Optional[str] = None
    NodeUpdateStatus: Optional[NodeUpdateStatusType] = None
    NodeDeletionDate: Optional[datetime] = None
    NodeUpdateStartDate: Optional[datetime] = None
    NodeUpdateEndDate: Optional[datetime] = None
    NodeUpdateInitiatedBy: Optional[NodeUpdateInitiatedByType] = None
    NodeUpdateInitiatedDate: Optional[datetime] = None
    NodeUpdateStatusModifiedDate: Optional[datetime] = None


class ParameterTypeDef(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None
    ChangeType: Optional[ChangeTypeType] = None


class CacheParameterGroupTypeDef(BaseValidatorModel):
    CacheParameterGroupName: Optional[str] = None
    CacheParameterGroupFamily: Optional[str] = None
    Description: Optional[str] = None
    IsGlobal: Optional[bool] = None
    ARN: Optional[str] = None


class EC2SecurityGroupTypeDef(BaseValidatorModel):
    Status: Optional[str] = None
    EC2SecurityGroupName: Optional[str] = None
    EC2SecurityGroupOwnerId: Optional[str] = None


class DataStorageTypeDef(BaseValidatorModel):
    Unit: Literal["GB"]
    Maximum: Optional[int] = None
    Minimum: Optional[int] = None


class ECPUPerSecondTypeDef(BaseValidatorModel):
    Maximum: Optional[int] = None
    Minimum: Optional[int] = None


class CloudWatchLogsDestinationDetailsTypeDef(BaseValidatorModel):
    LogGroup: Optional[str] = None


class CompleteMigrationMessageTypeDef(BaseValidatorModel):
    ReplicationGroupId: str
    Force: Optional[bool] = None


class ConfigureShardTypeDef(BaseValidatorModel):
    NodeGroupId: str
    NewReplicaCount: int
    PreferredAvailabilityZones: Optional[Sequence[str]] = None
    PreferredOutpostArns: Optional[Sequence[str]] = None


class CreateGlobalReplicationGroupMessageTypeDef(BaseValidatorModel):
    GlobalReplicationGroupIdSuffix: str
    PrimaryReplicationGroupId: str
    GlobalReplicationGroupDescription: Optional[str] = None


class CustomerNodeEndpointTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None


class DecreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef(BaseValidatorModel):
    GlobalReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    GlobalNodeGroupsToRemove: Optional[Sequence[str]] = None
    GlobalNodeGroupsToRetain: Optional[Sequence[str]] = None


class DeleteCacheClusterMessageTypeDef(BaseValidatorModel):
    CacheClusterId: str
    FinalSnapshotIdentifier: Optional[str] = None


class DeleteCacheParameterGroupMessageTypeDef(BaseValidatorModel):
    CacheParameterGroupName: str


class DeleteCacheSecurityGroupMessageTypeDef(BaseValidatorModel):
    CacheSecurityGroupName: str


class DeleteCacheSubnetGroupMessageTypeDef(BaseValidatorModel):
    CacheSubnetGroupName: str


class DeleteGlobalReplicationGroupMessageTypeDef(BaseValidatorModel):
    GlobalReplicationGroupId: str
    RetainPrimaryReplicationGroup: bool


class DeleteReplicationGroupMessageTypeDef(BaseValidatorModel):
    ReplicationGroupId: str
    RetainPrimaryCluster: Optional[bool] = None
    FinalSnapshotIdentifier: Optional[str] = None


class DeleteServerlessCacheRequestTypeDef(BaseValidatorModel):
    ServerlessCacheName: str
    FinalSnapshotName: Optional[str] = None


class DeleteServerlessCacheSnapshotRequestTypeDef(BaseValidatorModel):
    ServerlessCacheSnapshotName: str


class DeleteSnapshotMessageTypeDef(BaseValidatorModel):
    SnapshotName: str


class DeleteUserGroupMessageTypeDef(BaseValidatorModel):
    UserGroupId: str


class DeleteUserMessageTypeDef(BaseValidatorModel):
    UserId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeCacheClustersMessageTypeDef(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowCacheNodeInfo: Optional[bool] = None
    ShowCacheClustersNotInReplicationGroups: Optional[bool] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeCacheEngineVersionsMessageTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupFamily: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    DefaultOnly: Optional[bool] = None


class DescribeCacheParameterGroupsMessageTypeDef(BaseValidatorModel):
    CacheParameterGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeCacheParametersMessageTypeDef(BaseValidatorModel):
    CacheParameterGroupName: str
    Source: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeCacheSecurityGroupsMessageTypeDef(BaseValidatorModel):
    CacheSecurityGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeCacheSubnetGroupsMessageTypeDef(BaseValidatorModel):
    CacheSubnetGroupName: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeEngineDefaultParametersMessageTypeDef(BaseValidatorModel):
    CacheParameterGroupFamily: str
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeGlobalReplicationGroupsMessageTypeDef(BaseValidatorModel):
    GlobalReplicationGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowMemberInfo: Optional[bool] = None


class DescribeReplicationGroupsMessageTypeDef(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReservedCacheNodesMessageTypeDef(BaseValidatorModel):
    ReservedCacheNodeId: Optional[str] = None
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeReservedCacheNodesOfferingsMessageTypeDef(BaseValidatorModel):
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeServerlessCacheSnapshotsRequestTypeDef(BaseValidatorModel):
    ServerlessCacheName: Optional[str] = None
    ServerlessCacheSnapshotName: Optional[str] = None
    SnapshotType: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class DescribeServerlessCachesRequestTypeDef(BaseValidatorModel):
    ServerlessCacheName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeServiceUpdatesMessageTypeDef(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ServiceUpdateStatus: Optional[Sequence[ServiceUpdateStatusType]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DescribeSnapshotsMessageTypeDef(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    SnapshotName: Optional[str] = None
    SnapshotSource: Optional[str] = None
    Marker: Optional[str] = None
    MaxRecords: Optional[int] = None
    ShowNodeGroupConfig: Optional[bool] = None


class DescribeUserGroupsMessageTypeDef(BaseValidatorModel):
    UserGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class FilterTypeDef(BaseValidatorModel):
    Name: str
    Values: Sequence[str]


class KinesisFirehoseDestinationDetailsTypeDef(BaseValidatorModel):
    DeliveryStream: Optional[str] = None


class DisassociateGlobalReplicationGroupMessageTypeDef(BaseValidatorModel):
    GlobalReplicationGroupId: str
    ReplicationGroupId: str
    ReplicationGroupRegion: str


class EventTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    Date: Optional[datetime] = None


class ExportServerlessCacheSnapshotRequestTypeDef(BaseValidatorModel):
    ServerlessCacheSnapshotName: str
    S3BucketName: str


class FailoverGlobalReplicationGroupMessageTypeDef(BaseValidatorModel):
    GlobalReplicationGroupId: str
    PrimaryRegion: str
    PrimaryReplicationGroupId: str


class GlobalNodeGroupTypeDef(BaseValidatorModel):
    GlobalNodeGroupId: Optional[str] = None
    Slots: Optional[str] = None


class GlobalReplicationGroupInfoTypeDef(BaseValidatorModel):
    GlobalReplicationGroupId: Optional[str] = None
    GlobalReplicationGroupMemberRole: Optional[str] = None


class GlobalReplicationGroupMemberTypeDef(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    ReplicationGroupRegion: Optional[str] = None
    Role: Optional[str] = None
    AutomaticFailover: Optional[AutomaticFailoverStatusType] = None
    Status: Optional[str] = None


class ListAllowedNodeTypeModificationsMessageTypeDef(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    ReplicationGroupId: Optional[str] = None


class ListTagsForResourceMessageTypeDef(BaseValidatorModel):
    ResourceName: str


class ParameterNameValueTypeDef(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None


class ModifyCacheSubnetGroupMessageTypeDef(BaseValidatorModel):
    CacheSubnetGroupName: str
    CacheSubnetGroupDescription: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None


class ModifyGlobalReplicationGroupMessageTypeDef(BaseValidatorModel):
    GlobalReplicationGroupId: str
    ApplyImmediately: bool
    CacheNodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupName: Optional[str] = None
    GlobalReplicationGroupDescription: Optional[str] = None
    AutomaticFailoverEnabled: Optional[bool] = None


class ReshardingConfigurationTypeDef(BaseValidatorModel):
    NodeGroupId: Optional[str] = None
    PreferredAvailabilityZones: Optional[Sequence[str]] = None


class ModifyUserGroupMessageTypeDef(BaseValidatorModel):
    UserGroupId: str
    UserIdsToAdd: Optional[Sequence[str]] = None
    UserIdsToRemove: Optional[Sequence[str]] = None
    Engine: Optional[str] = None


class NodeGroupConfigurationOutputTypeDef(BaseValidatorModel):
    NodeGroupId: Optional[str] = None
    Slots: Optional[str] = None
    ReplicaCount: Optional[int] = None
    PrimaryAvailabilityZone: Optional[str] = None
    ReplicaAvailabilityZones: Optional[List[str]] = None
    PrimaryOutpostArn: Optional[str] = None
    ReplicaOutpostArns: Optional[List[str]] = None


class NodeGroupConfigurationTypeDef(BaseValidatorModel):
    NodeGroupId: Optional[str] = None
    Slots: Optional[str] = None
    ReplicaCount: Optional[int] = None
    PrimaryAvailabilityZone: Optional[str] = None
    ReplicaAvailabilityZones: Optional[Sequence[str]] = None
    PrimaryOutpostArn: Optional[str] = None
    ReplicaOutpostArns: Optional[Sequence[str]] = None


class NodeGroupMemberUpdateStatusTypeDef(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    CacheNodeId: Optional[str] = None
    NodeUpdateStatus: Optional[NodeUpdateStatusType] = None
    NodeDeletionDate: Optional[datetime] = None
    NodeUpdateStartDate: Optional[datetime] = None
    NodeUpdateEndDate: Optional[datetime] = None
    NodeUpdateInitiatedBy: Optional[NodeUpdateInitiatedByType] = None
    NodeUpdateInitiatedDate: Optional[datetime] = None
    NodeUpdateStatusModifiedDate: Optional[datetime] = None


class ProcessedUpdateActionTypeDef(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    ServiceUpdateName: Optional[str] = None
    UpdateActionStatus: Optional[UpdateActionStatusType] = None


class RebalanceSlotsInGlobalReplicationGroupMessageTypeDef(BaseValidatorModel):
    GlobalReplicationGroupId: str
    ApplyImmediately: bool


class RebootCacheClusterMessageTypeDef(BaseValidatorModel):
    CacheClusterId: str
    CacheNodeIdsToReboot: Sequence[str]


class RecurringChargeTypeDef(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None


class RemoveTagsFromResourceMessageTypeDef(BaseValidatorModel):
    ResourceName: str
    TagKeys: Sequence[str]


class UserGroupsUpdateStatusTypeDef(BaseValidatorModel):
    UserGroupIdsToAdd: Optional[List[str]] = None
    UserGroupIdsToRemove: Optional[List[str]] = None


class SlotMigrationTypeDef(BaseValidatorModel):
    ProgressPercentage: Optional[float] = None


class RevokeCacheSecurityGroupIngressMessageTypeDef(BaseValidatorModel):
    CacheSecurityGroupName: str
    EC2SecurityGroupName: str
    EC2SecurityGroupOwnerId: str


class ServerlessCacheConfigurationTypeDef(BaseValidatorModel):
    ServerlessCacheName: Optional[str] = None
    Engine: Optional[str] = None
    MajorEngineVersion: Optional[str] = None


class ServiceUpdateTypeDef(BaseValidatorModel):
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


class SubnetOutpostTypeDef(BaseValidatorModel):
    SubnetOutpostArn: Optional[str] = None


class TestFailoverMessageTypeDef(BaseValidatorModel):
    ReplicationGroupId: str
    NodeGroupId: str


class UnprocessedUpdateActionTypeDef(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    ServiceUpdateName: Optional[str] = None
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None


class UserGroupPendingChangesTypeDef(BaseValidatorModel):
    UserIdsToRemove: Optional[List[str]] = None
    UserIdsToAdd: Optional[List[str]] = None


class AddTagsToResourceMessageTypeDef(BaseValidatorModel):
    ResourceName: str
    Tags: Sequence[TagTypeDef]


class CopyServerlessCacheSnapshotRequestTypeDef(BaseValidatorModel):
    SourceServerlessCacheSnapshotName: str
    TargetServerlessCacheSnapshotName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CopySnapshotMessageTypeDef(BaseValidatorModel):
    SourceSnapshotName: str
    TargetSnapshotName: str
    TargetBucket: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateCacheParameterGroupMessageTypeDef(BaseValidatorModel):
    CacheParameterGroupName: str
    CacheParameterGroupFamily: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateCacheSecurityGroupMessageTypeDef(BaseValidatorModel):
    CacheSecurityGroupName: str
    Description: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateCacheSubnetGroupMessageTypeDef(BaseValidatorModel):
    CacheSubnetGroupName: str
    CacheSubnetGroupDescription: str
    SubnetIds: Sequence[str]
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateServerlessCacheSnapshotRequestTypeDef(BaseValidatorModel):
    ServerlessCacheSnapshotName: str
    ServerlessCacheName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateSnapshotMessageTypeDef(BaseValidatorModel):
    SnapshotName: str
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateUserGroupMessageTypeDef(BaseValidatorModel):
    UserGroupId: str
    Engine: str
    UserIds: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class PurchaseReservedCacheNodesOfferingMessageTypeDef(BaseValidatorModel):
    ReservedCacheNodesOfferingId: str
    ReservedCacheNodeId: Optional[str] = None
    CacheNodeCount: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class AllowedNodeTypeModificationsMessageTypeDef(BaseValidatorModel):
    ScaleUpModifications: List[str]
    ScaleDownModifications: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class CacheParameterGroupNameMessageTypeDef(BaseValidatorModel):
    CacheParameterGroupName: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class TagListMessageTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class AuthenticationModeTypeDef(BaseValidatorModel):
    pass


class CreateUserMessageTypeDef(BaseValidatorModel):
    UserId: str
    UserName: str
    Engine: str
    AccessString: str
    Passwords: Optional[Sequence[str]] = None
    NoPasswordRequired: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    AuthenticationMode: Optional[AuthenticationModeTypeDef] = None


class ModifyUserMessageTypeDef(BaseValidatorModel):
    UserId: str
    AccessString: Optional[str] = None
    AppendAccessString: Optional[str] = None
    Passwords: Optional[Sequence[str]] = None
    NoPasswordRequired: Optional[bool] = None
    AuthenticationMode: Optional[AuthenticationModeTypeDef] = None
    Engine: Optional[str] = None


class AuthenticationTypeDef(BaseValidatorModel):
    pass


class UserResponseTypeDef(BaseValidatorModel):
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


class UserTypeDef(BaseValidatorModel):
    UserId: Optional[str] = None
    UserName: Optional[str] = None
    Status: Optional[str] = None
    Engine: Optional[str] = None
    MinimumEngineVersion: Optional[str] = None
    AccessString: Optional[str] = None
    UserGroupIds: Optional[List[str]] = None
    Authentication: Optional[AuthenticationTypeDef] = None
    ARN: Optional[str] = None


class CacheNodeTypeDef(BaseValidatorModel):
    CacheNodeId: Optional[str] = None
    CacheNodeStatus: Optional[str] = None
    CacheNodeCreateTime: Optional[datetime] = None
    Endpoint: Optional[EndpointTypeDef] = None
    ParameterGroupStatus: Optional[str] = None
    SourceCacheNodeId: Optional[str] = None
    CustomerAvailabilityZone: Optional[str] = None
    CustomerOutpostArn: Optional[str] = None


class NodeGroupMemberTypeDef(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    CacheNodeId: Optional[str] = None
    ReadEndpoint: Optional[EndpointTypeDef] = None
    PreferredAvailabilityZone: Optional[str] = None
    PreferredOutpostArn: Optional[str] = None
    CurrentRole: Optional[str] = None


class CacheEngineVersionMessageTypeDef(BaseValidatorModel):
    Marker: str
    CacheEngineVersions: List[CacheEngineVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CacheNodeTypeSpecificParameterTypeDef(BaseValidatorModel):
    ParameterName: Optional[str] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[bool] = None
    MinimumEngineVersion: Optional[str] = None
    CacheNodeTypeSpecificValues: Optional[List[CacheNodeTypeSpecificValueTypeDef]] = None
    ChangeType: Optional[ChangeTypeType] = None


class CacheParameterGroupsMessageTypeDef(BaseValidatorModel):
    Marker: str
    CacheParameterGroups: List[CacheParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCacheParameterGroupResultTypeDef(BaseValidatorModel):
    CacheParameterGroup: CacheParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CacheSecurityGroupTypeDef(BaseValidatorModel):
    OwnerId: Optional[str] = None
    CacheSecurityGroupName: Optional[str] = None
    Description: Optional[str] = None
    EC2SecurityGroups: Optional[List[EC2SecurityGroupTypeDef]] = None
    ARN: Optional[str] = None


class CacheUsageLimitsTypeDef(BaseValidatorModel):
    DataStorage: Optional[DataStorageTypeDef] = None
    ECPUPerSecond: Optional[ECPUPerSecondTypeDef] = None


class DecreaseReplicaCountMessageTypeDef(BaseValidatorModel):
    ReplicationGroupId: str
    ApplyImmediately: bool
    NewReplicaCount: Optional[int] = None
    ReplicaConfiguration: Optional[Sequence[ConfigureShardTypeDef]] = None
    ReplicasToRemove: Optional[Sequence[str]] = None


class IncreaseReplicaCountMessageTypeDef(BaseValidatorModel):
    ReplicationGroupId: str
    ApplyImmediately: bool
    NewReplicaCount: Optional[int] = None
    ReplicaConfiguration: Optional[Sequence[ConfigureShardTypeDef]] = None


class StartMigrationMessageTypeDef(BaseValidatorModel):
    ReplicationGroupId: str
    CustomerNodeEndpointList: Sequence[CustomerNodeEndpointTypeDef]


class TestMigrationMessageTypeDef(BaseValidatorModel):
    ReplicationGroupId: str
    CustomerNodeEndpointList: Sequence[CustomerNodeEndpointTypeDef]


class DescribeCacheClustersMessagePaginateTypeDef(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    ShowCacheNodeInfo: Optional[bool] = None
    ShowCacheClustersNotInReplicationGroups: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeCacheEngineVersionsMessagePaginateTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    CacheParameterGroupFamily: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeCacheParameterGroupsMessagePaginateTypeDef(BaseValidatorModel):
    CacheParameterGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeCacheParametersMessagePaginateTypeDef(BaseValidatorModel):
    CacheParameterGroupName: str
    Source: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeCacheSecurityGroupsMessagePaginateTypeDef(BaseValidatorModel):
    CacheSecurityGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeCacheSubnetGroupsMessagePaginateTypeDef(BaseValidatorModel):
    CacheSubnetGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEngineDefaultParametersMessagePaginateTypeDef(BaseValidatorModel):
    CacheParameterGroupFamily: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeGlobalReplicationGroupsMessagePaginateTypeDef(BaseValidatorModel):
    GlobalReplicationGroupId: Optional[str] = None
    ShowMemberInfo: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeReplicationGroupsMessagePaginateTypeDef(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeReservedCacheNodesMessagePaginateTypeDef(BaseValidatorModel):
    ReservedCacheNodeId: Optional[str] = None
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeReservedCacheNodesOfferingsMessagePaginateTypeDef(BaseValidatorModel):
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[str] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeServerlessCacheSnapshotsRequestPaginateTypeDef(BaseValidatorModel):
    ServerlessCacheName: Optional[str] = None
    ServerlessCacheSnapshotName: Optional[str] = None
    SnapshotType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeServerlessCachesRequestPaginateTypeDef(BaseValidatorModel):
    ServerlessCacheName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeServiceUpdatesMessagePaginateTypeDef(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ServiceUpdateStatus: Optional[Sequence[ServiceUpdateStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSnapshotsMessagePaginateTypeDef(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    CacheClusterId: Optional[str] = None
    SnapshotName: Optional[str] = None
    SnapshotSource: Optional[str] = None
    ShowNodeGroupConfig: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeUserGroupsMessagePaginateTypeDef(BaseValidatorModel):
    UserGroupId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeCacheClustersMessageWaitExtraTypeDef(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowCacheNodeInfo: Optional[bool] = None
    ShowCacheClustersNotInReplicationGroups: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeCacheClustersMessageWaitTypeDef(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    ShowCacheNodeInfo: Optional[bool] = None
    ShowCacheClustersNotInReplicationGroups: Optional[bool] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeReplicationGroupsMessageWaitExtraTypeDef(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeReplicationGroupsMessageWaitTypeDef(BaseValidatorModel):
    ReplicationGroupId: Optional[str] = None
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
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEventsMessageTypeDef(BaseValidatorModel):
    SourceIdentifier: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class TimeRangeFilterTypeDef(BaseValidatorModel):
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None


class DescribeUsersMessagePaginateTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    UserId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeUsersMessageTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    UserId: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxRecords: Optional[int] = None
    Marker: Optional[str] = None


class DestinationDetailsTypeDef(BaseValidatorModel):
    CloudWatchLogsDetails: Optional[CloudWatchLogsDestinationDetailsTypeDef] = None
    KinesisFirehoseDetails: Optional[KinesisFirehoseDestinationDetailsTypeDef] = None


class EventsMessageTypeDef(BaseValidatorModel):
    Marker: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GlobalReplicationGroupTypeDef(BaseValidatorModel):
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


class ModifyCacheParameterGroupMessageTypeDef(BaseValidatorModel):
    CacheParameterGroupName: str
    ParameterNameValues: Sequence[ParameterNameValueTypeDef]


class ResetCacheParameterGroupMessageTypeDef(BaseValidatorModel):
    CacheParameterGroupName: str
    ResetAllParameters: Optional[bool] = None
    ParameterNameValues: Optional[Sequence[ParameterNameValueTypeDef]] = None


class ModifyReplicationGroupShardConfigurationMessageTypeDef(BaseValidatorModel):
    ReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    ReshardingConfiguration: Optional[Sequence[ReshardingConfigurationTypeDef]] = None
    NodeGroupsToRemove: Optional[Sequence[str]] = None
    NodeGroupsToRetain: Optional[Sequence[str]] = None


class RegionalConfigurationTypeDef(BaseValidatorModel):
    ReplicationGroupId: str
    ReplicationGroupRegion: str
    ReshardingConfiguration: Sequence[ReshardingConfigurationTypeDef]


class NodeSnapshotTypeDef(BaseValidatorModel):
    CacheClusterId: Optional[str] = None
    NodeGroupId: Optional[str] = None
    CacheNodeId: Optional[str] = None
    NodeGroupConfiguration: Optional[NodeGroupConfigurationOutputTypeDef] = None
    CacheSize: Optional[str] = None
    CacheNodeCreateTime: Optional[datetime] = None
    SnapshotCreateTime: Optional[datetime] = None


class NodeGroupUpdateStatusTypeDef(BaseValidatorModel):
    NodeGroupId: Optional[str] = None
    NodeGroupMemberUpdateStatus: Optional[List[NodeGroupMemberUpdateStatusTypeDef]] = None


class ReservedCacheNodeTypeDef(BaseValidatorModel):
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


class ReservedCacheNodesOfferingTypeDef(BaseValidatorModel):
    ReservedCacheNodesOfferingId: Optional[str] = None
    CacheNodeType: Optional[str] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    UsagePrice: Optional[float] = None
    ProductDescription: Optional[str] = None
    OfferingType: Optional[str] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None


class ReshardingStatusTypeDef(BaseValidatorModel):
    SlotMigration: Optional[SlotMigrationTypeDef] = None


class ServerlessCacheSnapshotTypeDef(BaseValidatorModel):
    ServerlessCacheSnapshotName: Optional[str] = None
    ARN: Optional[str] = None
    KmsKeyId: Optional[str] = None
    SnapshotType: Optional[str] = None
    Status: Optional[str] = None
    CreateTime: Optional[datetime] = None
    ExpiryTime: Optional[datetime] = None
    BytesUsedForCache: Optional[str] = None
    ServerlessCacheConfiguration: Optional[ServerlessCacheConfigurationTypeDef] = None


class ServiceUpdatesMessageTypeDef(BaseValidatorModel):
    Marker: str
    ServiceUpdates: List[ServiceUpdateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SubnetTypeDef(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[AvailabilityZoneTypeDef] = None
    SubnetOutpost: Optional[SubnetOutpostTypeDef] = None
    SupportedNetworkTypes: Optional[List[NetworkTypeType]] = None


class UpdateActionResultsMessageTypeDef(BaseValidatorModel):
    ProcessedUpdateActions: List[ProcessedUpdateActionTypeDef]
    UnprocessedUpdateActions: List[UnprocessedUpdateActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UserGroupResponseTypeDef(BaseValidatorModel):
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


class UserGroupTypeDef(BaseValidatorModel):
    UserGroupId: Optional[str] = None
    Status: Optional[str] = None
    Engine: Optional[str] = None
    UserIds: Optional[List[str]] = None
    MinimumEngineVersion: Optional[str] = None
    PendingChanges: Optional[UserGroupPendingChangesTypeDef] = None
    ReplicationGroups: Optional[List[str]] = None
    ServerlessCaches: Optional[List[str]] = None
    ARN: Optional[str] = None


class DescribeUsersResultTypeDef(BaseValidatorModel):
    Users: List[UserTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class NodeGroupTypeDef(BaseValidatorModel):
    NodeGroupId: Optional[str] = None
    Status: Optional[str] = None
    PrimaryEndpoint: Optional[EndpointTypeDef] = None
    ReaderEndpoint: Optional[EndpointTypeDef] = None
    Slots: Optional[str] = None
    NodeGroupMembers: Optional[List[NodeGroupMemberTypeDef]] = None


class CacheParameterGroupDetailsTypeDef(BaseValidatorModel):
    Marker: str
    Parameters: List[ParameterTypeDef]
    CacheNodeTypeSpecificParameters: List[CacheNodeTypeSpecificParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class EngineDefaultsTypeDef(BaseValidatorModel):
    CacheParameterGroupFamily: Optional[str] = None
    Marker: Optional[str] = None
    Parameters: Optional[List[ParameterTypeDef]] = None
    CacheNodeTypeSpecificParameters: Optional[List[CacheNodeTypeSpecificParameterTypeDef]] = None


class AuthorizeCacheSecurityGroupIngressResultTypeDef(BaseValidatorModel):
    CacheSecurityGroup: CacheSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CacheSecurityGroupMessageTypeDef(BaseValidatorModel):
    Marker: str
    CacheSecurityGroups: List[CacheSecurityGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCacheSecurityGroupResultTypeDef(BaseValidatorModel):
    CacheSecurityGroup: CacheSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RevokeCacheSecurityGroupIngressResultTypeDef(BaseValidatorModel):
    CacheSecurityGroup: CacheSecurityGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateServerlessCacheRequestTypeDef(BaseValidatorModel):
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


class ModifyServerlessCacheRequestTypeDef(BaseValidatorModel):
    ServerlessCacheName: str
    Description: Optional[str] = None
    CacheUsageLimits: Optional[CacheUsageLimitsTypeDef] = None
    RemoveUserGroup: Optional[bool] = None
    UserGroupId: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    SnapshotRetentionLimit: Optional[int] = None
    DailySnapshotTime: Optional[str] = None
    Engine: Optional[str] = None
    MajorEngineVersion: Optional[str] = None


class ServerlessCacheTypeDef(BaseValidatorModel):
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


class DescribeUpdateActionsMessagePaginateTypeDef(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ReplicationGroupIds: Optional[Sequence[str]] = None
    CacheClusterIds: Optional[Sequence[str]] = None
    Engine: Optional[str] = None
    ServiceUpdateStatus: Optional[Sequence[ServiceUpdateStatusType]] = None
    ServiceUpdateTimeRange: Optional[TimeRangeFilterTypeDef] = None
    UpdateActionStatus: Optional[Sequence[UpdateActionStatusType]] = None
    ShowNodeLevelUpdateStatus: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeUpdateActionsMessageTypeDef(BaseValidatorModel):
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


class LogDeliveryConfigurationRequestTypeDef(BaseValidatorModel):
    LogType: Optional[LogTypeType] = None
    DestinationType: Optional[DestinationTypeType] = None
    DestinationDetails: Optional[DestinationDetailsTypeDef] = None
    LogFormat: Optional[LogFormatType] = None
    Enabled: Optional[bool] = None


class LogDeliveryConfigurationTypeDef(BaseValidatorModel):
    LogType: Optional[LogTypeType] = None
    DestinationType: Optional[DestinationTypeType] = None
    DestinationDetails: Optional[DestinationDetailsTypeDef] = None
    LogFormat: Optional[LogFormatType] = None
    Status: Optional[LogDeliveryConfigurationStatusType] = None
    Message: Optional[str] = None


class PendingLogDeliveryConfigurationTypeDef(BaseValidatorModel):
    LogType: Optional[LogTypeType] = None
    DestinationType: Optional[DestinationTypeType] = None
    DestinationDetails: Optional[DestinationDetailsTypeDef] = None
    LogFormat: Optional[LogFormatType] = None


class CreateGlobalReplicationGroupResultTypeDef(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DecreaseNodeGroupsInGlobalReplicationGroupResultTypeDef(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteGlobalReplicationGroupResultTypeDef(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeGlobalReplicationGroupsResultTypeDef(BaseValidatorModel):
    Marker: str
    GlobalReplicationGroups: List[GlobalReplicationGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DisassociateGlobalReplicationGroupResultTypeDef(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class FailoverGlobalReplicationGroupResultTypeDef(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class IncreaseNodeGroupsInGlobalReplicationGroupResultTypeDef(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyGlobalReplicationGroupResultTypeDef(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RebalanceSlotsInGlobalReplicationGroupResultTypeDef(BaseValidatorModel):
    GlobalReplicationGroup: GlobalReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class IncreaseNodeGroupsInGlobalReplicationGroupMessageTypeDef(BaseValidatorModel):
    GlobalReplicationGroupId: str
    NodeGroupCount: int
    ApplyImmediately: bool
    RegionalConfigurations: Optional[Sequence[RegionalConfigurationTypeDef]] = None


class SnapshotTypeDef(BaseValidatorModel):
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


class UpdateActionTypeDef(BaseValidatorModel):
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


class PurchaseReservedCacheNodesOfferingResultTypeDef(BaseValidatorModel):
    ReservedCacheNode: ReservedCacheNodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ReservedCacheNodeMessageTypeDef(BaseValidatorModel):
    Marker: str
    ReservedCacheNodes: List[ReservedCacheNodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ReservedCacheNodesOfferingMessageTypeDef(BaseValidatorModel):
    Marker: str
    ReservedCacheNodesOfferings: List[ReservedCacheNodesOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CopyServerlessCacheSnapshotResponseTypeDef(BaseValidatorModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateServerlessCacheSnapshotResponseTypeDef(BaseValidatorModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteServerlessCacheSnapshotResponseTypeDef(BaseValidatorModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeServerlessCacheSnapshotsResponseTypeDef(BaseValidatorModel):
    ServerlessCacheSnapshots: List[ServerlessCacheSnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ExportServerlessCacheSnapshotResponseTypeDef(BaseValidatorModel):
    ServerlessCacheSnapshot: ServerlessCacheSnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CacheSubnetGroupTypeDef(BaseValidatorModel):
    CacheSubnetGroupName: Optional[str] = None
    CacheSubnetGroupDescription: Optional[str] = None
    VpcId: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None
    ARN: Optional[str] = None
    SupportedNetworkTypes: Optional[List[NetworkTypeType]] = None


class DescribeUserGroupsResultTypeDef(BaseValidatorModel):
    UserGroups: List[UserGroupTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEngineDefaultParametersResultTypeDef(BaseValidatorModel):
    EngineDefaults: EngineDefaultsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateServerlessCacheResponseTypeDef(BaseValidatorModel):
    ServerlessCache: ServerlessCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteServerlessCacheResponseTypeDef(BaseValidatorModel):
    ServerlessCache: ServerlessCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeServerlessCachesResponseTypeDef(BaseValidatorModel):
    ServerlessCaches: List[ServerlessCacheTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ModifyServerlessCacheResponseTypeDef(BaseValidatorModel):
    ServerlessCache: ServerlessCacheTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCacheClusterMessageTypeDef(BaseValidatorModel):
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


class NodeGroupConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateReplicationGroupMessageTypeDef(BaseValidatorModel):
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


class ModifyCacheClusterMessageTypeDef(BaseValidatorModel):
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
    LogDeliveryConfigurations: Optional[Sequence[LogDeliveryConfigurationRequestTypeDef]] = None
    IpDiscovery: Optional[IpDiscoveryType] = None


class ModifyReplicationGroupMessageTypeDef(BaseValidatorModel):
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
    LogDeliveryConfigurations: Optional[Sequence[LogDeliveryConfigurationRequestTypeDef]] = None
    IpDiscovery: Optional[IpDiscoveryType] = None
    TransitEncryptionEnabled: Optional[bool] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None
    ClusterMode: Optional[ClusterModeType] = None


class PendingModifiedValuesTypeDef(BaseValidatorModel):
    NumCacheNodes: Optional[int] = None
    CacheNodeIdsToRemove: Optional[List[str]] = None
    EngineVersion: Optional[str] = None
    CacheNodeType: Optional[str] = None
    AuthTokenStatus: Optional[AuthTokenUpdateStatusType] = None
    LogDeliveryConfigurations: Optional[List[PendingLogDeliveryConfigurationTypeDef]] = None
    TransitEncryptionEnabled: Optional[bool] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None


class ReplicationGroupPendingModifiedValuesTypeDef(BaseValidatorModel):
    PrimaryClusterId: Optional[str] = None
    AutomaticFailoverStatus: Optional[PendingAutomaticFailoverStatusType] = None
    Resharding: Optional[ReshardingStatusTypeDef] = None
    AuthTokenStatus: Optional[AuthTokenUpdateStatusType] = None
    UserGroups: Optional[UserGroupsUpdateStatusTypeDef] = None
    LogDeliveryConfigurations: Optional[List[PendingLogDeliveryConfigurationTypeDef]] = None
    TransitEncryptionEnabled: Optional[bool] = None
    TransitEncryptionMode: Optional[TransitEncryptionModeType] = None
    ClusterMode: Optional[ClusterModeType] = None


class CopySnapshotResultTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSnapshotResultTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSnapshotResultTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSnapshotsListMessageTypeDef(BaseValidatorModel):
    Marker: str
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateActionsMessageTypeDef(BaseValidatorModel):
    Marker: str
    UpdateActions: List[UpdateActionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CacheSubnetGroupMessageTypeDef(BaseValidatorModel):
    Marker: str
    CacheSubnetGroups: List[CacheSubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCacheSubnetGroupResultTypeDef(BaseValidatorModel):
    CacheSubnetGroup: CacheSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyCacheSubnetGroupResultTypeDef(BaseValidatorModel):
    CacheSubnetGroup: CacheSubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CacheClusterTypeDef(BaseValidatorModel):
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


class ReplicationGroupTypeDef(BaseValidatorModel):
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
    Engine: Optional[str] = None


class CacheClusterMessageTypeDef(BaseValidatorModel):
    Marker: str
    CacheClusters: List[CacheClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateCacheClusterResultTypeDef(BaseValidatorModel):
    CacheCluster: CacheClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCacheClusterResultTypeDef(BaseValidatorModel):
    CacheCluster: CacheClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyCacheClusterResultTypeDef(BaseValidatorModel):
    CacheCluster: CacheClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RebootCacheClusterResultTypeDef(BaseValidatorModel):
    CacheCluster: CacheClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CompleteMigrationResponseTypeDef(BaseValidatorModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateReplicationGroupResultTypeDef(BaseValidatorModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DecreaseReplicaCountResultTypeDef(BaseValidatorModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteReplicationGroupResultTypeDef(BaseValidatorModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class IncreaseReplicaCountResultTypeDef(BaseValidatorModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyReplicationGroupResultTypeDef(BaseValidatorModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ModifyReplicationGroupShardConfigurationResultTypeDef(BaseValidatorModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ReplicationGroupMessageTypeDef(BaseValidatorModel):
    Marker: str
    ReplicationGroups: List[ReplicationGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartMigrationResponseTypeDef(BaseValidatorModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TestFailoverResultTypeDef(BaseValidatorModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TestMigrationResponseTypeDef(BaseValidatorModel):
    ReplicationGroup: ReplicationGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


