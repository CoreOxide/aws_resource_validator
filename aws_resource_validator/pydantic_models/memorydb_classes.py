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
from aws_resource_validator.pydantic_models.memorydb_constants import *

class ACLPendingChanges(BaseValidatorModel):
    UserNamesToRemove: Optional[List[str]] = None
    UserNamesToAdd: Optional[List[str]] = None


class ACLsUpdateStatus(BaseValidatorModel):
    ACLToApply: Optional[str] = None


class AvailabilityZone(BaseValidatorModel):
    Name: Optional[str] = None


class ServiceUpdateRequest(BaseValidatorModel):
    ServiceUpdateNameToApply: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class UnprocessedCluster(BaseValidatorModel):
    ClusterName: Optional[str] = None
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None


class PendingModifiedServiceUpdate(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    Status: Optional[ServiceUpdateStatusType] = None


class Endpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None


class SecurityGroupMembership(BaseValidatorModel):
    SecurityGroupId: Optional[str] = None
    Status: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ParameterGroup(BaseValidatorModel):
    Name: Optional[str] = None
    Family: Optional[str] = None
    Description: Optional[str] = None
    ARN: Optional[str] = None


class DeleteACLRequest(BaseValidatorModel):
    ACLName: str


class DeleteClusterRequest(BaseValidatorModel):
    ClusterName: str
    MultiRegionClusterName: Optional[str] = None
    FinalSnapshotName: Optional[str] = None


class DeleteMultiRegionClusterRequest(BaseValidatorModel):
    MultiRegionClusterName: str


class DeleteParameterGroupRequest(BaseValidatorModel):
    ParameterGroupName: str


class DeleteSnapshotRequest(BaseValidatorModel):
    SnapshotName: str


class DeleteSubnetGroupRequest(BaseValidatorModel):
    SubnetGroupName: str


class DeleteUserRequest(BaseValidatorModel):
    UserName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeACLsRequest(BaseValidatorModel):
    ACLName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeClustersRequest(BaseValidatorModel):
    ClusterName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ShowShardDetails: Optional[bool] = None


class DescribeEngineVersionsRequest(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DefaultOnly: Optional[bool] = None


class EngineVersionInfo(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    EnginePatchVersion: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None


class Event(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    Date: Optional[datetime] = None


class DescribeMultiRegionClustersRequest(BaseValidatorModel):
    MultiRegionClusterName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ShowClusterDetails: Optional[bool] = None


class DescribeParameterGroupsRequest(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeParametersRequest(BaseValidatorModel):
    ParameterGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Parameter(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    Description: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    MinimumEngineVersion: Optional[str] = None


class DescribeReservedNodesOfferingsRequest(BaseValidatorModel):
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeReservedNodesRequest(BaseValidatorModel):
    ReservationId: Optional[str] = None
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeServiceUpdatesRequest(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ClusterNames: Optional[Sequence[str]] = None
    Status: Optional[Sequence[ServiceUpdateStatusType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeSnapshotsRequest(BaseValidatorModel):
    ClusterName: Optional[str] = None
    SnapshotName: Optional[str] = None
    Source: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ShowDetail: Optional[bool] = None


class DescribeSubnetGroupsRequest(BaseValidatorModel):
    SubnetGroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Filter(BaseValidatorModel):
    Name: str
    Values: Sequence[str]


class FailoverShardRequest(BaseValidatorModel):
    ClusterName: str
    ShardName: str


class ListAllowedMultiRegionClusterUpdatesRequest(BaseValidatorModel):
    MultiRegionClusterName: str


class ListAllowedNodeTypeUpdatesRequest(BaseValidatorModel):
    ClusterName: str


class ListTagsRequest(BaseValidatorModel):
    ResourceArn: str


class RegionalCluster(BaseValidatorModel):
    ClusterName: Optional[str] = None
    Region: Optional[str] = None
    Status: Optional[str] = None
    ARN: Optional[str] = None


class ParameterNameValue(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None


class RecurringCharge(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None


class ReplicaConfigurationRequest(BaseValidatorModel):
    ReplicaCount: Optional[int] = None


class ResetParameterGroupRequest(BaseValidatorModel):
    ParameterGroupName: str
    AllParameters: Optional[bool] = None
    ParameterNames: Optional[Sequence[str]] = None


class SlotMigration(BaseValidatorModel):
    ProgressPercentage: Optional[float] = None


class ShardConfigurationRequest(BaseValidatorModel):
    ShardCount: Optional[int] = None


class ShardConfiguration(BaseValidatorModel):
    Slots: Optional[str] = None
    ReplicaCount: Optional[int] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateACLRequest(BaseValidatorModel):
    ACLName: str
    UserNamesToAdd: Optional[Sequence[str]] = None
    UserNamesToRemove: Optional[Sequence[str]] = None


class UpdateSubnetGroupRequest(BaseValidatorModel):
    SubnetGroupName: str
    Description: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None


class ACL(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    UserNames: Optional[List[str]] = None
    MinimumEngineVersion: Optional[str] = None
    PendingChanges: Optional[ACLPendingChanges] = None
    Clusters: Optional[List[str]] = None
    ARN: Optional[str] = None


class AuthenticationMode(BaseValidatorModel):
    pass


class UpdateUserRequest(BaseValidatorModel):
    UserName: str
    AuthenticationMode: Optional[AuthenticationMode] = None
    AccessString: Optional[str] = None


class Authentication(BaseValidatorModel):
    pass


class User(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    AccessString: Optional[str] = None
    ACLNames: Optional[List[str]] = None
    MinimumEngineVersion: Optional[str] = None
    Authentication: Optional[Authentication] = None
    ARN: Optional[str] = None


class Subnet(BaseValidatorModel):
    Identifier: Optional[str] = None
    AvailabilityZone: Optional[AvailabilityZone] = None


class BatchUpdateClusterRequest(BaseValidatorModel):
    ClusterNames: Sequence[str]
    ServiceUpdate: Optional[ServiceUpdateRequest] = None


class ListAllowedMultiRegionClusterUpdatesResponse(BaseValidatorModel):
    ScaleUpNodeTypes: List[str]
    ScaleDownNodeTypes: List[str]
    ResponseMetadata: ResponseMetadata


class ListAllowedNodeTypeUpdatesResponse(BaseValidatorModel):
    ScaleUpNodeTypes: List[str]
    ScaleDownNodeTypes: List[str]
    ResponseMetadata: ResponseMetadata


class Node(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    CreateTime: Optional[datetime] = None
    Endpoint: Optional[Endpoint] = None


class CopySnapshotRequest(BaseValidatorModel):
    SourceSnapshotName: str
    TargetSnapshotName: str
    TargetBucket: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateACLRequest(BaseValidatorModel):
    ACLName: str
    UserNames: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateClusterRequest(BaseValidatorModel):
    ClusterName: str
    NodeType: str
    ACLName: str
    MultiRegionClusterName: Optional[str] = None
    ParameterGroupName: Optional[str] = None
    Description: Optional[str] = None
    NumShards: Optional[int] = None
    NumReplicasPerShard: Optional[int] = None
    SubnetGroupName: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    MaintenanceWindow: Optional[str] = None
    Port: Optional[int] = None
    SnsTopicArn: Optional[str] = None
    TLSEnabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    SnapshotArns: Optional[Sequence[str]] = None
    SnapshotName: Optional[str] = None
    SnapshotRetentionLimit: Optional[int] = None
    Tags: Optional[Sequence[Tag]] = None
    SnapshotWindow: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    DataTiering: Optional[bool] = None


class CreateMultiRegionClusterRequest(BaseValidatorModel):
    MultiRegionClusterNameSuffix: str
    NodeType: str
    Description: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    MultiRegionParameterGroupName: Optional[str] = None
    NumShards: Optional[int] = None
    TLSEnabled: Optional[bool] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateParameterGroupRequest(BaseValidatorModel):
    ParameterGroupName: str
    Family: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateSnapshotRequest(BaseValidatorModel):
    ClusterName: str
    SnapshotName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateSubnetGroupRequest(BaseValidatorModel):
    SubnetGroupName: str
    SubnetIds: Sequence[str]
    Description: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateUserRequest(BaseValidatorModel):
    UserName: str
    AuthenticationMode: AuthenticationMode
    AccessString: str
    Tags: Optional[Sequence[Tag]] = None


class ListTagsResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class PurchaseReservedNodesOfferingRequest(BaseValidatorModel):
    ReservedNodesOfferingId: str
    ReservationId: Optional[str] = None
    NodeCount: Optional[int] = None
    Tags: Optional[Sequence[Tag]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[Tag]


class TagResourceResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class UntagResourceResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


class CreateParameterGroupResponse(BaseValidatorModel):
    ParameterGroup: ParameterGroup
    ResponseMetadata: ResponseMetadata


class DeleteParameterGroupResponse(BaseValidatorModel):
    ParameterGroup: ParameterGroup
    ResponseMetadata: ResponseMetadata


class DescribeParameterGroupsResponse(BaseValidatorModel):
    ParameterGroups: List[ParameterGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ResetParameterGroupResponse(BaseValidatorModel):
    ParameterGroup: ParameterGroup
    ResponseMetadata: ResponseMetadata


class UpdateParameterGroupResponse(BaseValidatorModel):
    ParameterGroup: ParameterGroup
    ResponseMetadata: ResponseMetadata


class DescribeACLsRequestPaginate(BaseValidatorModel):
    ACLName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeClustersRequestPaginate(BaseValidatorModel):
    ClusterName: Optional[str] = None
    ShowShardDetails: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEngineVersionsRequestPaginate(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeMultiRegionClustersRequestPaginate(BaseValidatorModel):
    MultiRegionClusterName: Optional[str] = None
    ShowClusterDetails: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeParameterGroupsRequestPaginate(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeParametersRequestPaginate(BaseValidatorModel):
    ParameterGroupName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedNodesOfferingsRequestPaginate(BaseValidatorModel):
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeReservedNodesRequestPaginate(BaseValidatorModel):
    ReservationId: Optional[str] = None
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeServiceUpdatesRequestPaginate(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ClusterNames: Optional[Sequence[str]] = None
    Status: Optional[Sequence[ServiceUpdateStatusType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSnapshotsRequestPaginate(BaseValidatorModel):
    ClusterName: Optional[str] = None
    SnapshotName: Optional[str] = None
    Source: Optional[str] = None
    ShowDetail: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSubnetGroupsRequestPaginate(BaseValidatorModel):
    SubnetGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEngineVersionsResponse(BaseValidatorModel):
    EngineVersions: List[EngineVersionInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class Timestamp(BaseValidatorModel):
    pass


class DescribeEventsRequestPaginate(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeEventsRequest(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeEventsResponse(BaseValidatorModel):
    Events: List[Event]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeParametersResponse(BaseValidatorModel):
    Parameters: List[Parameter]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ServiceUpdate(BaseValidatorModel):
    pass


class DescribeServiceUpdatesResponse(BaseValidatorModel):
    ServiceUpdates: List[ServiceUpdate]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeUsersRequestPaginate(BaseValidatorModel):
    UserName: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeUsersRequest(BaseValidatorModel):
    UserName: Optional[str] = None
    Filters: Optional[Sequence[Filter]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MultiRegionCluster(BaseValidatorModel):
    MultiRegionClusterName: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[str] = None
    NodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    NumberOfShards: Optional[int] = None
    Clusters: Optional[List[RegionalCluster]] = None
    MultiRegionParameterGroupName: Optional[str] = None
    TLSEnabled: Optional[bool] = None
    ARN: Optional[str] = None


class UpdateParameterGroupRequest(BaseValidatorModel):
    ParameterGroupName: str
    ParameterNameValues: Sequence[ParameterNameValue]


class ReservedNode(BaseValidatorModel):
    ReservationId: Optional[str] = None
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    StartTime: Optional[datetime] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    NodeCount: Optional[int] = None
    OfferingType: Optional[str] = None
    State: Optional[str] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None
    ARN: Optional[str] = None


class ReservedNodesOffering(BaseValidatorModel):
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    OfferingType: Optional[str] = None
    RecurringCharges: Optional[List[RecurringCharge]] = None


class ReshardingStatus(BaseValidatorModel):
    SlotMigration: Optional[SlotMigration] = None


class UpdateClusterRequest(BaseValidatorModel):
    ClusterName: str
    Description: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    MaintenanceWindow: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    SnsTopicStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None
    SnapshotWindow: Optional[str] = None
    SnapshotRetentionLimit: Optional[int] = None
    NodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    ReplicaConfiguration: Optional[ReplicaConfigurationRequest] = None
    ShardConfiguration: Optional[ShardConfigurationRequest] = None
    ACLName: Optional[str] = None


class UpdateMultiRegionClusterRequest(BaseValidatorModel):
    MultiRegionClusterName: str
    NodeType: Optional[str] = None
    Description: Optional[str] = None
    EngineVersion: Optional[str] = None
    ShardConfiguration: Optional[ShardConfigurationRequest] = None
    MultiRegionParameterGroupName: Optional[str] = None
    UpdateStrategy: Optional[UpdateStrategyType] = None


class ShardDetail(BaseValidatorModel):
    Name: Optional[str] = None
    Configuration: Optional[ShardConfiguration] = None
    Size: Optional[str] = None
    SnapshotCreationTime: Optional[datetime] = None


class CreateACLResponse(BaseValidatorModel):
    ACL: ACL
    ResponseMetadata: ResponseMetadata


class DeleteACLResponse(BaseValidatorModel):
    ACL: ACL
    ResponseMetadata: ResponseMetadata


class DescribeACLsResponse(BaseValidatorModel):
    ACLs: List[ACL]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateACLResponse(BaseValidatorModel):
    ACL: ACL
    ResponseMetadata: ResponseMetadata


class CreateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class DeleteUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class DescribeUsersResponse(BaseValidatorModel):
    Users: List[User]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class SubnetGroup(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    VpcId: Optional[str] = None
    Subnets: Optional[List[Subnet]] = None
    ARN: Optional[str] = None


class Shard(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Slots: Optional[str] = None
    Nodes: Optional[List[Node]] = None
    NumberOfNodes: Optional[int] = None


class CreateMultiRegionClusterResponse(BaseValidatorModel):
    MultiRegionCluster: MultiRegionCluster
    ResponseMetadata: ResponseMetadata


class DeleteMultiRegionClusterResponse(BaseValidatorModel):
    MultiRegionCluster: MultiRegionCluster
    ResponseMetadata: ResponseMetadata


class DescribeMultiRegionClustersResponse(BaseValidatorModel):
    MultiRegionClusters: List[MultiRegionCluster]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateMultiRegionClusterResponse(BaseValidatorModel):
    MultiRegionCluster: MultiRegionCluster
    ResponseMetadata: ResponseMetadata


class DescribeReservedNodesResponse(BaseValidatorModel):
    ReservedNodes: List[ReservedNode]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PurchaseReservedNodesOfferingResponse(BaseValidatorModel):
    ReservedNode: ReservedNode
    ResponseMetadata: ResponseMetadata


class DescribeReservedNodesOfferingsResponse(BaseValidatorModel):
    ReservedNodesOfferings: List[ReservedNodesOffering]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ClusterPendingUpdates(BaseValidatorModel):
    Resharding: Optional[ReshardingStatus] = None
    ACLs: Optional[ACLsUpdateStatus] = None
    ServiceUpdates: Optional[List[PendingModifiedServiceUpdate]] = None


class ClusterConfiguration(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    NodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    MaintenanceWindow: Optional[str] = None
    TopicArn: Optional[str] = None
    Port: Optional[int] = None
    ParameterGroupName: Optional[str] = None
    SubnetGroupName: Optional[str] = None
    VpcId: Optional[str] = None
    SnapshotRetentionLimit: Optional[int] = None
    SnapshotWindow: Optional[str] = None
    NumShards: Optional[int] = None
    Shards: Optional[List[ShardDetail]] = None
    MultiRegionParameterGroupName: Optional[str] = None
    MultiRegionClusterName: Optional[str] = None


class CreateSubnetGroupResponse(BaseValidatorModel):
    SubnetGroup: SubnetGroup
    ResponseMetadata: ResponseMetadata


class DeleteSubnetGroupResponse(BaseValidatorModel):
    SubnetGroup: SubnetGroup
    ResponseMetadata: ResponseMetadata


class DescribeSubnetGroupsResponse(BaseValidatorModel):
    SubnetGroups: List[SubnetGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateSubnetGroupResponse(BaseValidatorModel):
    SubnetGroup: SubnetGroup
    ResponseMetadata: ResponseMetadata


class Cluster(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[str] = None
    PendingUpdates: Optional[ClusterPendingUpdates] = None
    MultiRegionClusterName: Optional[str] = None
    NumberOfShards: Optional[int] = None
    Shards: Optional[List[Shard]] = None
    AvailabilityMode: Optional[AZStatusType] = None
    ClusterEndpoint: Optional[Endpoint] = None
    NodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    EnginePatchVersion: Optional[str] = None
    ParameterGroupName: Optional[str] = None
    ParameterGroupStatus: Optional[str] = None
    SecurityGroups: Optional[List[SecurityGroupMembership]] = None
    SubnetGroupName: Optional[str] = None
    TLSEnabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    ARN: Optional[str] = None
    SnsTopicArn: Optional[str] = None
    SnsTopicStatus: Optional[str] = None
    SnapshotRetentionLimit: Optional[int] = None
    MaintenanceWindow: Optional[str] = None
    SnapshotWindow: Optional[str] = None
    ACLName: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    DataTiering: Optional[DataTieringStatusType] = None


class Snapshot(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Source: Optional[str] = None
    KmsKeyId: Optional[str] = None
    ARN: Optional[str] = None
    ClusterConfiguration: Optional[ClusterConfiguration] = None
    DataTiering: Optional[DataTieringStatusType] = None


class BatchUpdateClusterResponse(BaseValidatorModel):
    ProcessedClusters: List[Cluster]
    UnprocessedClusters: List[UnprocessedCluster]
    ResponseMetadata: ResponseMetadata


class CreateClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DeleteClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DescribeClustersResponse(BaseValidatorModel):
    Clusters: List[Cluster]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class FailoverShardResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class UpdateClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class CopySnapshotResponse(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class CreateSnapshotResponse(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class DeleteSnapshotResponse(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


class DescribeSnapshotsResponse(BaseValidatorModel):
    Snapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


