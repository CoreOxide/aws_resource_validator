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
from aws_resource_validator.pydantic_models.memorydb_constants import *

class ACLPendingChangesTypeDef(BaseValidatorModel):
    UserNamesToRemove: Optional[List[str]] = None
    UserNamesToAdd: Optional[List[str]] = None

class ACLsUpdateStatusTypeDef(BaseValidatorModel):
    ACLToApply: Optional[str] = None

class AuthenticationModeTypeDef(BaseValidatorModel):
    Type: Optional[InputAuthenticationTypeType] = None
    Passwords: Optional[Sequence[str]] = None

class AuthenticationTypeDef(BaseValidatorModel):
    Type: Optional[AuthenticationTypeType] = None
    PasswordCount: Optional[int] = None

class AvailabilityZoneTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class ServiceUpdateRequestTypeDef(BaseValidatorModel):
    ServiceUpdateNameToApply: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class UnprocessedClusterTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    ErrorType: Optional[str] = None
    ErrorMessage: Optional[str] = None

class PendingModifiedServiceUpdateTypeDef(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    Status: Optional[ServiceUpdateStatusType] = None

class EndpointTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None

class SecurityGroupMembershipTypeDef(BaseValidatorModel):
    SecurityGroupId: Optional[str] = None
    Status: Optional[str] = None

class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ParameterGroupTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Family: Optional[str] = None
    Description: Optional[str] = None
    ARN: Optional[str] = None

class DeleteACLRequestRequestTypeDef(BaseValidatorModel):
    ACLName: str

class DeleteClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    FinalSnapshotName: Optional[str] = None

class DeleteParameterGroupRequestRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str

class DeleteSnapshotRequestRequestTypeDef(BaseValidatorModel):
    SnapshotName: str

class DeleteSubnetGroupRequestRequestTypeDef(BaseValidatorModel):
    SubnetGroupName: str

class DeleteUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeACLsRequestRequestTypeDef(BaseValidatorModel):
    ACLName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeClustersRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ShowShardDetails: Optional[bool] = None

class DescribeEngineVersionsRequestRequestTypeDef(BaseValidatorModel):
    EngineVersion: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DefaultOnly: Optional[bool] = None

class EngineVersionInfoTypeDef(BaseValidatorModel):
    EngineVersion: Optional[str] = None
    EnginePatchVersion: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None

class EventTypeDef(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    Date: Optional[datetime] = None

class DescribeParameterGroupsRequestRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeParametersRequestRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ParameterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    Description: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    MinimumEngineVersion: Optional[str] = None

class DescribeReservedNodesOfferingsRequestRequestTypeDef(BaseValidatorModel):
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeReservedNodesRequestRequestTypeDef(BaseValidatorModel):
    ReservationId: Optional[str] = None
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeServiceUpdatesRequestRequestTypeDef(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ClusterNames: Optional[Sequence[str]] = None
    Status: Optional[Sequence[ServiceUpdateStatusType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ServiceUpdateTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    ServiceUpdateName: Optional[str] = None
    ReleaseDate: Optional[datetime] = None
    Description: Optional[str] = None
    Status: Optional[ServiceUpdateStatusType] = None
    Type: Optional[Literal["security-update"]] = None
    NodesUpdated: Optional[str] = None
    AutoUpdateStartDate: Optional[datetime] = None

class DescribeSnapshotsRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    SnapshotName: Optional[str] = None
    Source: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ShowDetail: Optional[bool] = None

class DescribeSubnetGroupsRequestRequestTypeDef(BaseValidatorModel):
    SubnetGroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class FilterTypeDef(BaseValidatorModel):
    Name: str
    Values: Sequence[str]

class FailoverShardRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    ShardName: str

class ListAllowedNodeTypeUpdatesRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str

class ListTagsRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str

class ParameterNameValueTypeDef(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None

class RecurringChargeTypeDef(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None

class ReplicaConfigurationRequestTypeDef(BaseValidatorModel):
    ReplicaCount: Optional[int] = None

class ResetParameterGroupRequestRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    AllParameters: Optional[bool] = None
    ParameterNames: Optional[Sequence[str]] = None

class SlotMigrationTypeDef(BaseValidatorModel):
    ProgressPercentage: Optional[float] = None

class ShardConfigurationRequestTypeDef(BaseValidatorModel):
    ShardCount: Optional[int] = None

class ShardConfigurationTypeDef(BaseValidatorModel):
    Slots: Optional[str] = None
    ReplicaCount: Optional[int] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]

class UpdateACLRequestRequestTypeDef(BaseValidatorModel):
    ACLName: str
    UserNamesToAdd: Optional[Sequence[str]] = None
    UserNamesToRemove: Optional[Sequence[str]] = None

class UpdateSubnetGroupRequestRequestTypeDef(BaseValidatorModel):
    SubnetGroupName: str
    Description: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None

class ACLTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    UserNames: Optional[List[str]] = None
    MinimumEngineVersion: Optional[str] = None
    PendingChanges: Optional[ACLPendingChangesTypeDef] = None
    Clusters: Optional[List[str]] = None
    ARN: Optional[str] = None

class UpdateUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    AuthenticationMode: Optional[AuthenticationModeTypeDef] = None
    AccessString: Optional[str] = None

class UserTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    AccessString: Optional[str] = None
    ACLNames: Optional[List[str]] = None
    MinimumEngineVersion: Optional[str] = None
    Authentication: Optional[AuthenticationTypeDef] = None
    ARN: Optional[str] = None

class SubnetTypeDef(BaseValidatorModel):
    Identifier: Optional[str] = None
    AvailabilityZone: Optional[AvailabilityZoneTypeDef] = None

class BatchUpdateClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterNames: Sequence[str]
    ServiceUpdate: Optional[ServiceUpdateRequestTypeDef] = None

class ListAllowedNodeTypeUpdatesResponseTypeDef(BaseValidatorModel):
    ScaleUpNodeTypes: List[str]
    ScaleDownNodeTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class NodeTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    AvailabilityZone: Optional[str] = None
    CreateTime: Optional[datetime] = None
    Endpoint: Optional[EndpointTypeDef] = None

class CopySnapshotRequestRequestTypeDef(BaseValidatorModel):
    SourceSnapshotName: str
    TargetSnapshotName: str
    TargetBucket: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateACLRequestRequestTypeDef(BaseValidatorModel):
    ACLName: str
    UserNames: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateClusterRequestRequestTypeDef(BaseValidatorModel):
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

class CreateParameterGroupRequestRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    Family: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSnapshotRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    SnapshotName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateSubnetGroupRequestRequestTypeDef(BaseValidatorModel):
    SubnetGroupName: str
    SubnetIds: Sequence[str]
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateUserRequestRequestTypeDef(BaseValidatorModel):
    UserName: str
    AuthenticationMode: AuthenticationModeTypeDef
    AccessString: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsResponseTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseReservedNodesOfferingRequestRequestTypeDef(BaseValidatorModel):
    ReservedNodesOfferingId: str
    ReservationId: Optional[str] = None
    NodeCount: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    Tags: Sequence[TagTypeDef]

class TagResourceResponseTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UntagResourceResponseTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateParameterGroupResponseTypeDef(BaseValidatorModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteParameterGroupResponseTypeDef(BaseValidatorModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeParameterGroupsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    ParameterGroups: List[ParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ResetParameterGroupResponseTypeDef(BaseValidatorModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateParameterGroupResponseTypeDef(BaseValidatorModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeACLsRequestDescribeACLsPaginateTypeDef(BaseValidatorModel):
    ACLName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeClustersRequestDescribeClustersPaginateTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    ShowShardDetails: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEngineVersionsRequestDescribeEngineVersionsPaginateTypeDef(BaseValidatorModel):
    EngineVersion: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeParameterGroupsRequestDescribeParameterGroupsPaginateTypeDef(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeParametersRequestDescribeParametersPaginateTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedNodesOfferingsRequestDescribeReservedNodesOfferingsPaginateTypeDef(BaseValidatorModel):
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeReservedNodesRequestDescribeReservedNodesPaginateTypeDef(BaseValidatorModel):
    ReservationId: Optional[str] = None
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeServiceUpdatesRequestDescribeServiceUpdatesPaginateTypeDef(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ClusterNames: Optional[Sequence[str]] = None
    Status: Optional[Sequence[ServiceUpdateStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    SnapshotName: Optional[str] = None
    Source: Optional[str] = None
    ShowDetail: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateTypeDef(BaseValidatorModel):
    SubnetGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEngineVersionsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    EngineVersions: List[EngineVersionInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeEventsRequestDescribeEventsPaginateTypeDef(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeEventsRequestRequestTypeDef(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeEventsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeParametersResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Parameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServiceUpdatesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    ServiceUpdates: List[ServiceUpdateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUsersRequestDescribeUsersPaginateTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeUsersRequestRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class UpdateParameterGroupRequestRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    ParameterNameValues: Sequence[ParameterNameValueTypeDef]

class ReservedNodeTypeDef(BaseValidatorModel):
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

class ReservedNodesOfferingTypeDef(BaseValidatorModel):
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[int] = None
    FixedPrice: Optional[float] = None
    OfferingType: Optional[str] = None
    RecurringCharges: Optional[List[RecurringChargeTypeDef]] = None

class ReshardingStatusTypeDef(BaseValidatorModel):
    SlotMigration: Optional[SlotMigrationTypeDef] = None

class UpdateClusterRequestRequestTypeDef(BaseValidatorModel):
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

class ShardDetailTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Configuration: Optional[ShardConfigurationTypeDef] = None
    Size: Optional[str] = None
    SnapshotCreationTime: Optional[datetime] = None

class CreateACLResponseTypeDef(BaseValidatorModel):
    ACL: ACLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteACLResponseTypeDef(BaseValidatorModel):
    ACL: ACLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeACLsResponseTypeDef(BaseValidatorModel):
    ACLs: List[ACLTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateACLResponseTypeDef(BaseValidatorModel):
    ACL: ACLTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUsersResponseTypeDef(BaseValidatorModel):
    Users: List[UserTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SubnetGroupTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    VpcId: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None
    ARN: Optional[str] = None

class ShardTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Slots: Optional[str] = None
    Nodes: Optional[List[NodeTypeDef]] = None
    NumberOfNodes: Optional[int] = None

class DescribeReservedNodesResponseTypeDef(BaseValidatorModel):
    NextToken: str
    ReservedNodes: List[ReservedNodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PurchaseReservedNodesOfferingResponseTypeDef(BaseValidatorModel):
    ReservedNode: ReservedNodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeReservedNodesOfferingsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    ReservedNodesOfferings: List[ReservedNodesOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterPendingUpdatesTypeDef(BaseValidatorModel):
    Resharding: Optional[ReshardingStatusTypeDef] = None
    ACLs: Optional[ACLsUpdateStatusTypeDef] = None
    ServiceUpdates: Optional[List[PendingModifiedServiceUpdateTypeDef]] = None

class ClusterConfigurationTypeDef(BaseValidatorModel):
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

class CreateSubnetGroupResponseTypeDef(BaseValidatorModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSubnetGroupResponseTypeDef(BaseValidatorModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSubnetGroupsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    SubnetGroups: List[SubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSubnetGroupResponseTypeDef(BaseValidatorModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterTypeDef(BaseValidatorModel):
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

class SnapshotTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Status: Optional[str] = None
    Source: Optional[str] = None
    KmsKeyId: Optional[str] = None
    ARN: Optional[str] = None
    ClusterConfiguration: Optional[ClusterConfigurationTypeDef] = None
    DataTiering: Optional[DataTieringStatusType] = None

class BatchUpdateClusterResponseTypeDef(BaseValidatorModel):
    ProcessedClusters: List[ClusterTypeDef]
    UnprocessedClusters: List[UnprocessedClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClustersResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FailoverShardResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CopySnapshotResponseTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSnapshotResponseTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotResponseTypeDef(BaseValidatorModel):
    Snapshot: SnapshotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

