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
from aws_resource_validator.pydantic_models.memorydb_constants import *

class ACLPendingChangesTypeDef(BaseModel):
    UserNamesToRemove: Optional[List[str]] = None
    UserNamesToAdd: Optional[List[str]] = None

class ACLsUpdateStatusTypeDef(BaseModel):
    ACLToApply: Optional[str] = None

class AuthenticationModeTypeDef(BaseModel):
    Type: Optional[InputAuthenticationTypeType] = None
    Passwords: Optional[Sequence[str]] = None

class AuthenticationTypeDef(BaseModel):
    Type: Optional[AuthenticationTypeType] = None
    PasswordCount: Optional[int] = None

class AvailabilityZoneTypeDef(BaseModel):
    Name: Optional[str] = None

class ServiceUpdateRequestTypeDef(BaseModel):
    ServiceUpdateNameToApply: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class UnprocessedClusterTypeDef(BaseModel):
    ClusterName: Optional[str] = None
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None

class PendingModifiedServiceUpdateTypeDef(BaseModel):
    ServiceUpdateName: Optional[str] = None
    Status: Optional[ServiceUpdateStatusType] = None

class EndpointTypeDef(BaseModel):
    Address: Optional[str] = None
    Port: Optional[int] = None

class SecurityGroupMembershipTypeDef(BaseModel):
    SecurityGroupId: Optional[str] = None
    Status: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ParameterGroupTypeDef(BaseModel):
    Name: Optional[str] = None
    Family: Optional[str] = None
    Description: Optional[str] = None
    ARN: Optional[str] = None

class DeleteACLRequestRequestTypeDef(BaseModel):
    ACLName: str

class DeleteClusterRequestRequestTypeDef(BaseModel):
    ClusterName: str
    FinalSnapshotName: Optional[str] = None

class DeleteParameterGroupRequestRequestTypeDef(BaseModel):
    ParameterGroupName: str

class DeleteSnapshotRequestRequestTypeDef(BaseModel):
    SnapshotName: str

class DeleteSubnetGroupRequestRequestTypeDef(BaseModel):
    SubnetGroupName: str

class DeleteUserRequestRequestTypeDef(BaseModel):
    UserName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeACLsRequestRequestTypeDef(BaseModel):
    ACLName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeClustersRequestRequestTypeDef(BaseModel):
    ClusterName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ShowShardDetails: Optional[bool] = None

class DescribeEngineVersionsRequestRequestTypeDef(BaseModel):
    EngineVersion: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DefaultOnly: Optional[bool] = None

class EngineVersionInfoTypeDef(BaseModel):
    EngineVersion: Optional[str] = None
    EnginePatchVersion: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None

class EventTypeDef(BaseModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    Date: Optional[datetime] = None

class DescribeParameterGroupsRequestRequestTypeDef(BaseModel):
    ParameterGroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeParametersRequestRequestTypeDef(BaseModel):
    ParameterGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ParameterTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    Description: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    MinimumEngineVersion: Optional[str] = None

class DescribeReservedNodesOfferingsRequestRequestTypeDef(BaseModel):
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeReservedNodesRequestRequestTypeDef(BaseModel):
    ReservationId: Optional[str] = None
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeServiceUpdatesRequestRequestTypeDef(BaseModel):
    ServiceUpdateName: Optional[str] = None
    ClusterNames: Optional[Sequence[str]] = None
    Status: Optional[Sequence[ServiceUpdateStatusType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ServiceUpdateTypeDef(BaseModel):
    ClusterName: Optional[str] = None
    ServiceUpdateName: Optional[str] = None
    ReleaseDate: Optional[datetime] = None
    Description: Optional[str] = None
    Status: Optional[ServiceUpdateStatusType] = None
    Type: Optional[Literal["security-update"]] = None
    NodesUpdated: Optional[str] = None
    AutoUpdateStartDate: Optional[datetime] = None

class DescribeSnapshotsRequestRequestTypeDef(BaseModel):
    ClusterName: Optional[str] = None
    SnapshotName: Optional[str] = None
    Source: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ShowDetail: Optional[bool] = None

class DescribeSubnetGroupsRequestRequestTypeDef(BaseModel):
    SubnetGroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class FilterTypeDef(BaseModel):
    Name: str
    Values: Sequence[str]

class FailoverShardRequestRequestTypeDef(BaseModel):
    ClusterName: str
    ShardName: str

class ListAllowedNodeTypeUpdatesRequestRequestTypeDef(BaseModel):
    ClusterName: str

class ListTagsRequestRequestTypeDef(BaseModel):
    ResourceArn: str

class ParameterNameValueTypeDef(BaseModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None

class RecurringChargeTypeDef(BaseModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None

class ReplicaConfigurationRequestTypeDef(BaseModel):
    ReplicaCount: Optional[int] = None

class ResetParameterGroupRequestRequestTypeDef(BaseModel):
    ParameterGroupName: str
    AllParameters: Optional[bool] = None
    ParameterNames: Optional[Sequence[str]] = None

class SlotMigrationTypeDef(BaseModel):
    ProgressPercentage: Optional[float] = None

class ShardConfigurationRequestTypeDef(BaseModel):
    ShardCount: Optional[int] = None

class ShardConfigurationTypeDef(BaseModel):
    Slots: Optional[str] = None
    ReplicaCount: Optional[int] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateACLRequestRequestTypeDef(BaseModel):
    ACLName: str
    UserNamesToAdd: Optional[Sequence[str]] = None
    UserNamesToRemove: Optional[Sequence[str]] = None

class UpdateSubnetGroupRequestRequestTypeDef(BaseModel):
    SubnetGroupName: str
    Description: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None

class ACLTypeDef(BaseModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    UserNames: Optional[List[str]] = None
    MinimumEngineVersion: Optional[str] = None
    PendingChanges: Optional[ACLPendingChangesTypeDef] = None
    Clusters: Optional[List[str]] = None
    ARN: Optional[str] = None

class UpdateUserRequestRequestTypeDef(BaseModel):
    UserName: str
    AuthenticationMode: Optional[AuthenticationModeTypeDef] = None
    AccessString: Optional[str] = None

class UserTypeDef(BaseModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    AccessString: Optional[str] = None
    ACLNames: Optional[List[str]] = None
    MinimumEngineVersion: Optional[str] = None
    Authentication: Optional[AuthenticationTypeDef] = None
    ARN: Optional[str] = None

class SubnetTypeDef(BaseModel):
    Identifier: Optional[str] = None
    AvailabilityZone: Optional[AvailabilityZoneTypeDef] = None

class BatchUpdateClusterRequestRequestTypeDef(BaseModel):
    ClusterNames: Sequence[str]
    ServiceUpdate: Optional[ServiceUpdateRequestTypeDef] = None

class ListAllowedNodeTypeUpdatesResponseTypeDef(BaseModel):
    ScaleUpNodeTypes: List[str]
    ScaleDownNodeTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class NodeTypeDef(BaseModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    CreateTime: Optional[datetime] = None
    Endpoint: Optional[EndpointTypeDef] = None

class CopySnapshotRequestRequestTypeDef(BaseModel):
    SourceSnapshotName: str
    TargetSnapshotName: str
    TargetBucket: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateACLRequestRequestTypeDef(BaseModel):
    ACLName: str
    UserNames: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateClusterRequestRequestTypeDef(BaseModel):
    ClusterName: str
    NodeType: str
    ACLName: str
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
    Tags: Optional[Sequence[TagTypeDef]] = None
    SnapshotWindow: Optional[str] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    DataTiering: Optional[bool] = None

class CreateParameterGroupRequestRequestTypeDef(BaseModel):
    ParameterGroupName: str
    Family: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSnapshotRequestRequestTypeDef(BaseModel):
    ClusterName: str
    SnapshotName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSubnetGroupRequestRequestTypeDef(BaseModel):
    SubnetGroupName: str
    SubnetIds: Sequence[str]
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateUserRequestRequestTypeDef(BaseModel):
    UserName: str
    AuthenticationMode: AuthenticationModeTypeDef
    AccessString: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsResponseTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseReservedNodesOfferingRequestRequestTypeDef(BaseModel):
    ReservedNodesOfferingId: str
    ReservationId: Optional[str] = None
    NodeCount: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class TagResourceResponseTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UntagResourceResponseTypeDef(BaseModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateParameterGroupResponseTypeDef(BaseModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteParameterGroupResponseTypeDef(BaseModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeParameterGroupsResponseTypeDef(BaseModel):
    NextToken: str
    ParameterGroups: List[ParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResetParameterGroupResponseTypeDef(BaseModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateParameterGroupResponseTypeDef(BaseModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeACLsRequestDescribeACLsPaginateTypeDef(BaseModel):
    ACLName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClustersRequestDescribeClustersPaginateTypeDef(BaseModel):
    ClusterName: Optional[str] = None
    ShowShardDetails: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEngineVersionsRequestDescribeEngineVersionsPaginateTypeDef(BaseModel):
    EngineVersion: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeParameterGroupsRequestDescribeParameterGroupsPaginateTypeDef(BaseModel):
    ParameterGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeParametersRequestDescribeParametersPaginateTypeDef(BaseModel):
    ParameterGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedNodesOfferingsRequestDescribeReservedNodesOfferingsPaginateTypeDef(BaseModel):
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedNodesRequestDescribeReservedNodesPaginateTypeDef(BaseModel):
    ReservationId: Optional[str] = None
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeServiceUpdatesRequestDescribeServiceUpdatesPaginateTypeDef(BaseModel):
    ServiceUpdateName: Optional[str] = None
    ClusterNames: Optional[Sequence[str]] = None
    Status: Optional[Sequence[ServiceUpdateStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef(BaseModel):
    ClusterName: Optional[str] = None
    SnapshotName: Optional[str] = None
    Source: Optional[str] = None
    ShowDetail: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateTypeDef(BaseModel):
    SubnetGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEngineVersionsResponseTypeDef(BaseModel):
    NextToken: str
    EngineVersions: List[EngineVersionInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventsRequestDescribeEventsPaginateTypeDef(BaseModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsRequestRequestTypeDef(BaseModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeEventsResponseTypeDef(BaseModel):
    NextToken: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeParametersResponseTypeDef(BaseModel):
    NextToken: str
    Parameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServiceUpdatesResponseTypeDef(BaseModel):
    NextToken: str
    ServiceUpdates: List[ServiceUpdateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUsersRequestDescribeUsersPaginateTypeDef(BaseModel):
    UserName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUsersRequestRequestTypeDef(BaseModel):
    UserName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UpdateParameterGroupRequestRequestTypeDef(BaseModel):
    ParameterGroupName: str
    ParameterNameValues: Sequence[ParameterNameValueTypeDef]

class ReservedNodeTypeDef(BaseModel):
    ReservationId: Optional[str] = None
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    StartTime: Optional[datetime] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    NodeCount: Optional[int] = None
    OfferingType: Optional[str] = None
    State: Optional[str] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None
    ARN: Optional[str] = None

class ReservedNodesOfferingTypeDef(BaseModel):
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    OfferingType: Optional[str] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None

class ReshardingStatusTypeDef(BaseModel):
    SlotMigration: Optional[SlotMigrationTypeDef] = None

class UpdateClusterRequestRequestTypeDef(BaseModel):
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
    EngineVersion: Optional[str] = None
    ReplicaConfiguration: Optional[ReplicaConfigurationRequestTypeDef] = None
    ShardConfiguration: Optional[ShardConfigurationRequestTypeDef] = None
    ACLName: Optional[str] = None

class ShardDetailTypeDef(BaseModel):
    Name: Optional[str] = None
    Configuration: Optional[ShardConfigurationTypeDef] = None
    Size: Optional[str] = None
    SnapshotCreationTime: Optional[datetime] = None

class CreateACLResponseTypeDef(BaseModel):
    ACL: ACLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteACLResponseTypeDef(BaseModel):
    ACL: ACLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeACLsResponseTypeDef(BaseModel):
    ACLs: List[ACLTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateACLResponseTypeDef(BaseModel):
    ACL: ACLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUsersResponseTypeDef(BaseModel):
    Users: List[UserTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SubnetGroupTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    VpcId: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None
    ARN: Optional[str] = None

class ShardTypeDef(BaseModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Slots: Optional[str] = None
    Nodes: Optional[List[NodeTypeDef]] = None
    NumberOfNodes: Optional[int] = None

class DescribeReservedNodesResponseTypeDef(BaseModel):
    NextToken: str
    ReservedNodes: List[ReservedNodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseReservedNodesOfferingResponseTypeDef(BaseModel):
    ReservedNode: ReservedNodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReservedNodesOfferingsResponseTypeDef(BaseModel):
    NextToken: str
    ReservedNodesOfferings: List[ReservedNodesOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterPendingUpdatesTypeDef(BaseModel):
    Resharding: Optional[ReshardingStatusTypeDef] = None
    ACLs: Optional[ACLsUpdateStatusTypeDef] = None
    ServiceUpdates: Optional[List[PendingModifiedServiceUpdateTypeDef]] = None

class ClusterConfigurationTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    NodeType: Optional[str] = None
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
    Shards: Optional[List[ShardDetailTypeDef]] = None

class CreateSubnetGroupResponseTypeDef(BaseModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSubnetGroupResponseTypeDef(BaseModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSubnetGroupsResponseTypeDef(BaseModel):
    NextToken: str
    SubnetGroups: List[SubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSubnetGroupResponseTypeDef(BaseModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterTypeDef(BaseModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[str] = None
    PendingUpdates: Optional[ClusterPendingUpdatesTypeDef] = None
    NumberOfShards: Optional[int] = None
    Shards: Optional[List[ShardTypeDef]] = None
    AvailabilityMode: Optional[AZStatusType] = None
    ClusterEndpoint: Optional[EndpointTypeDef] = None
    NodeType: Optional[str] = None
    EngineVersion: Optional[str] = None
    EnginePatchVersion: Optional[str] = None
    ParameterGroupName: Optional[str] = None
    ParameterGroupStatus: Optional[str] = None
    SecurityGroups: Optional[List[SecurityGroupMembershipTypeDef]] = None
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

class SnapshotTypeDef(BaseModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Source: Optional[str] = None
    KmsKeyId: Optional[str] = None
    ARN: Optional[str] = None
    ClusterConfiguration: Optional[ClusterConfigurationTypeDef] = None
    DataTiering: Optional[DataTieringStatusType] = None

class BatchUpdateClusterResponseTypeDef(BaseModel):
    ProcessedClusters: List[ClusterTypeDef]
    UnprocessedClusters: List[UnprocessedClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClustersResponseTypeDef(BaseModel):
    NextToken: str
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverShardResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopySnapshotResponseTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSnapshotResponseTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotResponseTypeDef(BaseModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotsResponseTypeDef(BaseModel):
    NextToken: str
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

