from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.memorydb.memorydb_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ACLPendingChanges(BaseValidatorModel):
    UserNamesToRemove: Optional[List[str]] = None
    UserNamesToAdd: Optional[List[str]] = None


class ACLsUpdateStatus(BaseValidatorModel):
    ACLToApply: Optional[str] = None


class AuthenticationMode(BaseValidatorModel):
    Type: Optional[InputAuthenticationTypeType] = None
    Passwords: Optional[List[str]] = None


class Authentication(BaseValidatorModel):
    Type: Optional[AuthenticationTypeType] = None
    PasswordCount: Optional[int] = None


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


# This class is the input for the 'delete_acl' function.
class DeleteACLRequest(BaseValidatorModel):
    ACLName: str


# This class is the input for the 'delete_cluster' function.
class DeleteClusterRequest(BaseValidatorModel):
    ClusterName: str
    MultiRegionClusterName: Optional[str] = None
    FinalSnapshotName: Optional[str] = None


# This class is the input for the 'delete_multi_region_cluster' function.
class DeleteMultiRegionClusterRequest(BaseValidatorModel):
    MultiRegionClusterName: str


# This class is the input for the 'delete_parameter_group' function.
class DeleteParameterGroupRequest(BaseValidatorModel):
    ParameterGroupName: str


# This class is the input for the 'delete_snapshot' function.
class DeleteSnapshotRequest(BaseValidatorModel):
    SnapshotName: str


# This class is the input for the 'delete_subnet_group' function.
class DeleteSubnetGroupRequest(BaseValidatorModel):
    SubnetGroupName: str


# This class is the input for the 'delete_user' function.
class DeleteUserRequest(BaseValidatorModel):
    UserName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'describe_acls' function.
class DescribeACLsRequest(BaseValidatorModel):
    ACLName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_clusters' function.
class DescribeClustersRequest(BaseValidatorModel):
    ClusterName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ShowShardDetails: Optional[bool] = None


# This class is the input for the 'describe_engine_versions' function.
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

Timestamp = Union[datetime, str]


class Event(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    Date: Optional[datetime] = None


# This class is the input for the 'describe_multi_region_clusters' function.
class DescribeMultiRegionClustersRequest(BaseValidatorModel):
    MultiRegionClusterName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ShowClusterDetails: Optional[bool] = None


# This class is the input for the 'describe_parameter_groups' function.
class DescribeParameterGroupsRequest(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_parameters' function.
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


# This class is the input for the 'describe_reserved_nodes_offerings' function.
class DescribeReservedNodesOfferingsRequest(BaseValidatorModel):
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_reserved_nodes' function.
class DescribeReservedNodesRequest(BaseValidatorModel):
    ReservationId: Optional[str] = None
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'describe_service_updates' function.
class DescribeServiceUpdatesRequest(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ClusterNames: Optional[List[str]] = None
    Status: Optional[List[ServiceUpdateStatusType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ServiceUpdate(BaseValidatorModel):
    ClusterName: Optional[str] = None
    ServiceUpdateName: Optional[str] = None
    ReleaseDate: Optional[datetime] = None
    Description: Optional[str] = None
    Status: Optional[ServiceUpdateStatusType] = None
    Type: Optional[Literal['security-update']] = None
    Engine: Optional[str] = None
    NodesUpdated: Optional[str] = None
    AutoUpdateStartDate: Optional[datetime] = None


# This class is the input for the 'describe_snapshots' function.
class DescribeSnapshotsRequest(BaseValidatorModel):
    ClusterName: Optional[str] = None
    SnapshotName: Optional[str] = None
    Source: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ShowDetail: Optional[bool] = None


# This class is the input for the 'describe_subnet_groups' function.
class DescribeSubnetGroupsRequest(BaseValidatorModel):
    SubnetGroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Filter(BaseValidatorModel):
    Name: str
    Values: List[str]


# This class is the input for the 'failover_shard' function.
class FailoverShardRequest(BaseValidatorModel):
    ClusterName: str
    ShardName: str


# This class is the input for the 'list_allowed_multi_region_cluster_updates' function.
class ListAllowedMultiRegionClusterUpdatesRequest(BaseValidatorModel):
    MultiRegionClusterName: str


# This class is the input for the 'list_allowed_node_type_updates' function.
class ListAllowedNodeTypeUpdatesRequest(BaseValidatorModel):
    ClusterName: str


# This class is the input for the 'list_tags' function.
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


# This class is the input for the 'reset_parameter_group' function.
class ResetParameterGroupRequest(BaseValidatorModel):
    ParameterGroupName: str
    AllParameters: Optional[bool] = None
    ParameterNames: Optional[List[str]] = None


class SlotMigration(BaseValidatorModel):
    ProgressPercentage: Optional[float] = None


class ShardConfigurationRequest(BaseValidatorModel):
    ShardCount: Optional[int] = None


class ShardConfiguration(BaseValidatorModel):
    Slots: Optional[str] = None
    ReplicaCount: Optional[int] = None


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    TagKeys: List[str]


# This class is the input for the 'update_acl' function.
class UpdateACLRequest(BaseValidatorModel):
    ACLName: str
    UserNamesToAdd: Optional[List[str]] = None
    UserNamesToRemove: Optional[List[str]] = None


# This class is the input for the 'update_subnet_group' function.
class UpdateSubnetGroupRequest(BaseValidatorModel):
    SubnetGroupName: str
    Description: Optional[str] = None
    SubnetIds: Optional[List[str]] = None


class ACL(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    UserNames: Optional[List[str]] = None
    MinimumEngineVersion: Optional[str] = None
    PendingChanges: Optional[ACLPendingChanges] = None
    Clusters: Optional[List[str]] = None
    ARN: Optional[str] = None


# This class is the input for the 'update_user' function.
class UpdateUserRequest(BaseValidatorModel):
    UserName: str
    AuthenticationMode: Optional[AuthenticationMode] = None
    AccessString: Optional[str] = None


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


# This class is the input for the 'batch_update_cluster' function.
class BatchUpdateClusterRequest(BaseValidatorModel):
    ClusterNames: List[str]
    ServiceUpdate: Optional[ServiceUpdateRequest] = None


# This class is the output for the 'list_allowed_multi_region_cluster_updates' function.
class ListAllowedMultiRegionClusterUpdatesResponse(BaseValidatorModel):
    ScaleUpNodeTypes: List[str]
    ScaleDownNodeTypes: List[str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_allowed_node_type_updates' function.
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


# This class is the input for the 'copy_snapshot' function.
class CopySnapshotRequest(BaseValidatorModel):
    SourceSnapshotName: str
    TargetSnapshotName: str
    TargetBucket: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_acl' function.
class CreateACLRequest(BaseValidatorModel):
    ACLName: str
    UserNames: Optional[List[str]] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_cluster' function.
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
    SecurityGroupIds: Optional[List[str]] = None
    MaintenanceWindow: Optional[str] = None
    Port: Optional[int] = None
    SnsTopicArn: Optional[str] = None
    TLSEnabled: Optional[bool] = None
    KmsKeyId: Optional[str] = None
    SnapshotArns: Optional[List[str]] = None
    SnapshotName: Optional[str] = None
    SnapshotRetentionLimit: Optional[int] = None
    Tags: Optional[List[Tag]] = None
    SnapshotWindow: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    DataTiering: Optional[bool] = None


# This class is the input for the 'create_multi_region_cluster' function.
class CreateMultiRegionClusterRequest(BaseValidatorModel):
    MultiRegionClusterNameSuffix: str
    NodeType: str
    Description: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    MultiRegionParameterGroupName: Optional[str] = None
    NumShards: Optional[int] = None
    TLSEnabled: Optional[bool] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_parameter_group' function.
class CreateParameterGroupRequest(BaseValidatorModel):
    ParameterGroupName: str
    Family: str
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_snapshot' function.
class CreateSnapshotRequest(BaseValidatorModel):
    ClusterName: str
    SnapshotName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_subnet_group' function.
class CreateSubnetGroupRequest(BaseValidatorModel):
    SubnetGroupName: str
    SubnetIds: List[str]
    Description: Optional[str] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'create_user' function.
class CreateUserRequest(BaseValidatorModel):
    UserName: str
    AuthenticationMode: AuthenticationMode
    AccessString: str
    Tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags' function.
class ListTagsResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'purchase_reserved_nodes_offering' function.
class PurchaseReservedNodesOfferingRequest(BaseValidatorModel):
    ReservedNodesOfferingId: str
    ReservationId: Optional[str] = None
    NodeCount: Optional[int] = None
    Tags: Optional[List[Tag]] = None


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    ResourceArn: str
    Tags: List[Tag]


# This class is the output for the 'tag_resource' function.
class TagResourceResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'untag_resource' function.
class UntagResourceResponse(BaseValidatorModel):
    TagList: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_parameter_group' function.
class CreateParameterGroupResponse(BaseValidatorModel):
    ParameterGroup: ParameterGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_parameter_group' function.
class DeleteParameterGroupResponse(BaseValidatorModel):
    ParameterGroup: ParameterGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_parameter_groups' function.
class DescribeParameterGroupsResponse(BaseValidatorModel):
    ParameterGroups: List[ParameterGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'reset_parameter_group' function.
class ResetParameterGroupResponse(BaseValidatorModel):
    ParameterGroup: ParameterGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_parameter_group' function.
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
    ClusterNames: Optional[List[str]] = None
    Status: Optional[List[ServiceUpdateStatusType]] = None
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


# This class is the output for the 'describe_engine_versions' function.
class DescribeEngineVersionsResponse(BaseValidatorModel):
    EngineVersions: List[EngineVersionInfo]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeEventsRequestPaginate(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_events' function.
class DescribeEventsRequest(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[Timestamp] = None
    EndTime: Optional[Timestamp] = None
    Duration: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the output for the 'describe_events' function.
class DescribeEventsResponse(BaseValidatorModel):
    Events: List[Event]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_parameters' function.
class DescribeParametersResponse(BaseValidatorModel):
    Parameters: List[Parameter]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_service_updates' function.
class DescribeServiceUpdatesResponse(BaseValidatorModel):
    ServiceUpdates: List[ServiceUpdate]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeUsersRequestPaginate(BaseValidatorModel):
    UserName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_users' function.
class DescribeUsersRequest(BaseValidatorModel):
    UserName: Optional[str] = None
    Filters: Optional[List[Filter]] = None
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


# This class is the input for the 'update_parameter_group' function.
class UpdateParameterGroupRequest(BaseValidatorModel):
    ParameterGroupName: str
    ParameterNameValues: List[ParameterNameValue]


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


# This class is the input for the 'update_cluster' function.
class UpdateClusterRequest(BaseValidatorModel):
    ClusterName: str
    Description: Optional[str] = None
    SecurityGroupIds: Optional[List[str]] = None
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


# This class is the input for the 'update_multi_region_cluster' function.
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


# This class is the output for the 'create_acl' function.
class CreateACLResponse(BaseValidatorModel):
    ACL: ACL
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_acl' function.
class DeleteACLResponse(BaseValidatorModel):
    ACL: ACL
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_acls' function.
class DescribeACLsResponse(BaseValidatorModel):
    ACLs: List[ACL]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_acl' function.
class UpdateACLResponse(BaseValidatorModel):
    ACL: ACL
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_user' function.
class CreateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_user' function.
class DeleteUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_users' function.
class DescribeUsersResponse(BaseValidatorModel):
    Users: List[User]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_user' function.
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


# This class is the output for the 'create_multi_region_cluster' function.
class CreateMultiRegionClusterResponse(BaseValidatorModel):
    MultiRegionCluster: MultiRegionCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_multi_region_cluster' function.
class DeleteMultiRegionClusterResponse(BaseValidatorModel):
    MultiRegionCluster: MultiRegionCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_multi_region_clusters' function.
class DescribeMultiRegionClustersResponse(BaseValidatorModel):
    MultiRegionClusters: List[MultiRegionCluster]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_multi_region_cluster' function.
class UpdateMultiRegionClusterResponse(BaseValidatorModel):
    MultiRegionCluster: MultiRegionCluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_reserved_nodes' function.
class DescribeReservedNodesResponse(BaseValidatorModel):
    ReservedNodes: List[ReservedNode]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'purchase_reserved_nodes_offering' function.
class PurchaseReservedNodesOfferingResponse(BaseValidatorModel):
    ReservedNode: ReservedNode
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_reserved_nodes_offerings' function.
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


# This class is the output for the 'create_subnet_group' function.
class CreateSubnetGroupResponse(BaseValidatorModel):
    SubnetGroup: SubnetGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_subnet_group' function.
class DeleteSubnetGroupResponse(BaseValidatorModel):
    SubnetGroup: SubnetGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_subnet_groups' function.
class DescribeSubnetGroupsResponse(BaseValidatorModel):
    SubnetGroups: List[SubnetGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_subnet_group' function.
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


# This class is the output for the 'batch_update_cluster' function.
class BatchUpdateClusterResponse(BaseValidatorModel):
    ProcessedClusters: List[Cluster]
    UnprocessedClusters: List[UnprocessedCluster]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cluster' function.
class CreateClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_cluster' function.
class DeleteClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_clusters' function.
class DescribeClustersResponse(BaseValidatorModel):
    Clusters: List[Cluster]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'failover_shard' function.
class FailoverShardResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_cluster' function.
class UpdateClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'copy_snapshot' function.
class CopySnapshotResponse(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_snapshot' function.
class CreateSnapshotResponse(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_snapshot' function.
class DeleteSnapshotResponse(BaseValidatorModel):
    Snapshot: Snapshot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_snapshots' function.
class DescribeSnapshotsResponse(BaseValidatorModel):
    Snapshots: List[Snapshot]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None