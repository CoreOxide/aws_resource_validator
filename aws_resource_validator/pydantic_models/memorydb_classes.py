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

class ACLPendingChangesTypeDef(BaseValidatorModel):
    UserNamesToRemove: Optional[List[str]] = None
    UserNamesToAdd: Optional[List[str]] = None


class ACLsUpdateStatusTypeDef(BaseValidatorModel):
    ACLToApply: Optional[str] = None


class AvailabilityZoneTypeDef(BaseValidatorModel):
    Name: Optional[str] = None


class ServiceUpdateRequestTypeDef(BaseValidatorModel):
    ServiceUpdateNameToApply: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


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


class DeleteACLRequestTypeDef(BaseValidatorModel):
    ACLName: str


class DeleteClusterRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    MultiRegionClusterName: Optional[str] = None
    FinalSnapshotName: Optional[str] = None


class DeleteMultiRegionClusterRequestTypeDef(BaseValidatorModel):
    MultiRegionClusterName: str


class DeleteParameterGroupRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str


class DeleteSnapshotRequestTypeDef(BaseValidatorModel):
    SnapshotName: str


class DeleteSubnetGroupRequestTypeDef(BaseValidatorModel):
    SubnetGroupName: str


class DeleteUserRequestTypeDef(BaseValidatorModel):
    UserName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeACLsRequestTypeDef(BaseValidatorModel):
    ACLName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeClustersRequestTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ShowShardDetails: Optional[bool] = None


class DescribeEngineVersionsRequestTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    DefaultOnly: Optional[bool] = None


class EngineVersionInfoTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    EnginePatchVersion: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None


class EventTypeDef(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    Date: Optional[datetime] = None


class DescribeMultiRegionClustersRequestTypeDef(BaseValidatorModel):
    MultiRegionClusterName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ShowClusterDetails: Optional[bool] = None


class DescribeParameterGroupsRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeParametersRequestTypeDef(BaseValidatorModel):
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


class DescribeReservedNodesOfferingsRequestTypeDef(BaseValidatorModel):
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeReservedNodesRequestTypeDef(BaseValidatorModel):
    ReservationId: Optional[str] = None
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeServiceUpdatesRequestTypeDef(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ClusterNames: Optional[Sequence[str]] = None
    Status: Optional[Sequence[ServiceUpdateStatusType]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeSnapshotsRequestTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    SnapshotName: Optional[str] = None
    Source: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ShowDetail: Optional[bool] = None


class DescribeSubnetGroupsRequestTypeDef(BaseValidatorModel):
    SubnetGroupName: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class FilterTypeDef(BaseValidatorModel):
    Name: str
    Values: Sequence[str]


class FailoverShardRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    ShardName: str


class ListAllowedMultiRegionClusterUpdatesRequestTypeDef(BaseValidatorModel):
    MultiRegionClusterName: str


class ListAllowedNodeTypeUpdatesRequestTypeDef(BaseValidatorModel):
    ClusterName: str


class ListTagsRequestTypeDef(BaseValidatorModel):
    ResourceArn: str


class RegionalClusterTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    Region: Optional[str] = None
    Status: Optional[str] = None
    ARN: Optional[str] = None


class ParameterNameValueTypeDef(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None


class RecurringChargeTypeDef(BaseValidatorModel):
    RecurringChargeAmount: Optional[float] = None
    RecurringChargeFrequency: Optional[str] = None


class ReplicaConfigurationRequestTypeDef(BaseValidatorModel):
    ReplicaCount: Optional[int] = None


class ResetParameterGroupRequestTypeDef(BaseValidatorModel):
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


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    TagKeys: Sequence[str]


class UpdateACLRequestTypeDef(BaseValidatorModel):
    ACLName: str
    UserNamesToAdd: Optional[Sequence[str]] = None
    UserNamesToRemove: Optional[Sequence[str]] = None


class UpdateSubnetGroupRequestTypeDef(BaseValidatorModel):
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


class AuthenticationModeTypeDef(BaseValidatorModel):
    pass


class UpdateUserRequestTypeDef(BaseValidatorModel):
    UserName: str
    AuthenticationMode: Optional[AuthenticationModeTypeDef] = None
    AccessString: Optional[str] = None


class AuthenticationTypeDef(BaseValidatorModel):
    pass


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


class BatchUpdateClusterRequestTypeDef(BaseValidatorModel):
    ClusterNames: Sequence[str]
    ServiceUpdate: Optional[ServiceUpdateRequestTypeDef] = None


class ListAllowedMultiRegionClusterUpdatesResponseTypeDef(BaseValidatorModel):
    ScaleUpNodeTypes: List[str]
    ScaleDownNodeTypes: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


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


class CopySnapshotRequestTypeDef(BaseValidatorModel):
    SourceSnapshotName: str
    TargetSnapshotName: str
    TargetBucket: Optional[str] = None
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateACLRequestTypeDef(BaseValidatorModel):
    ACLName: str
    UserNames: Optional[Sequence[str]] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateClusterRequestTypeDef(BaseValidatorModel):
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
    Tags: Optional[Sequence[TagTypeDef]] = None
    SnapshotWindow: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    AutoMinorVersionUpgrade: Optional[bool] = None
    DataTiering: Optional[bool] = None


class CreateMultiRegionClusterRequestTypeDef(BaseValidatorModel):
    MultiRegionClusterNameSuffix: str
    NodeType: str
    Description: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    MultiRegionParameterGroupName: Optional[str] = None
    NumShards: Optional[int] = None
    TLSEnabled: Optional[bool] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateParameterGroupRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    Family: str
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateSnapshotRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    SnapshotName: str
    KmsKeyId: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateSubnetGroupRequestTypeDef(BaseValidatorModel):
    SubnetGroupName: str
    SubnetIds: Sequence[str]
    Description: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class CreateUserRequestTypeDef(BaseValidatorModel):
    UserName: str
    AuthenticationMode: AuthenticationModeTypeDef
    AccessString: str
    Tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsResponseTypeDef(BaseValidatorModel):
    TagList: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PurchaseReservedNodesOfferingRequestTypeDef(BaseValidatorModel):
    ReservedNodesOfferingId: str
    ReservationId: Optional[str] = None
    NodeCount: Optional[int] = None
    Tags: Optional[Sequence[TagTypeDef]] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
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
    ParameterGroups: List[ParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ResetParameterGroupResponseTypeDef(BaseValidatorModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateParameterGroupResponseTypeDef(BaseValidatorModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeACLsRequestPaginateTypeDef(BaseValidatorModel):
    ACLName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeClustersRequestPaginateTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    ShowShardDetails: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEngineVersionsRequestPaginateTypeDef(BaseValidatorModel):
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    ParameterGroupFamily: Optional[str] = None
    DefaultOnly: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeMultiRegionClustersRequestPaginateTypeDef(BaseValidatorModel):
    MultiRegionClusterName: Optional[str] = None
    ShowClusterDetails: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeParameterGroupsRequestPaginateTypeDef(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeParametersRequestPaginateTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeReservedNodesOfferingsRequestPaginateTypeDef(BaseValidatorModel):
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeReservedNodesRequestPaginateTypeDef(BaseValidatorModel):
    ReservationId: Optional[str] = None
    ReservedNodesOfferingId: Optional[str] = None
    NodeType: Optional[str] = None
    Duration: Optional[str] = None
    OfferingType: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeServiceUpdatesRequestPaginateTypeDef(BaseValidatorModel):
    ServiceUpdateName: Optional[str] = None
    ClusterNames: Optional[Sequence[str]] = None
    Status: Optional[Sequence[ServiceUpdateStatusType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSnapshotsRequestPaginateTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    SnapshotName: Optional[str] = None
    Source: Optional[str] = None
    ShowDetail: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSubnetGroupsRequestPaginateTypeDef(BaseValidatorModel):
    SubnetGroupName: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEngineVersionsResponseTypeDef(BaseValidatorModel):
    EngineVersions: List[EngineVersionInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class DescribeEventsRequestPaginateTypeDef(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeEventsRequestTypeDef(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    StartTime: Optional[TimestampTypeDef] = None
    EndTime: Optional[TimestampTypeDef] = None
    Duration: Optional[int] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeEventsResponseTypeDef(BaseValidatorModel):
    Events: List[EventTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeParametersResponseTypeDef(BaseValidatorModel):
    Parameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ServiceUpdateTypeDef(BaseValidatorModel):
    pass


class DescribeServiceUpdatesResponseTypeDef(BaseValidatorModel):
    ServiceUpdates: List[ServiceUpdateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeUsersRequestPaginateTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeUsersRequestTypeDef(BaseValidatorModel):
    UserName: Optional[str] = None
    Filters: Optional[Sequence[FilterTypeDef]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class MultiRegionClusterTypeDef(BaseValidatorModel):
    MultiRegionClusterName: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[str] = None
    NodeType: Optional[str] = None
    Engine: Optional[str] = None
    EngineVersion: Optional[str] = None
    NumberOfShards: Optional[int] = None
    Clusters: Optional[List[RegionalClusterTypeDef]] = None
    MultiRegionParameterGroupName: Optional[str] = None
    TLSEnabled: Optional[bool] = None
    ARN: Optional[str] = None


class UpdateParameterGroupRequestTypeDef(BaseValidatorModel):
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


class UpdateClusterRequestTypeDef(BaseValidatorModel):
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
    ReplicaConfiguration: Optional[ReplicaConfigurationRequestTypeDef] = None
    ShardConfiguration: Optional[ShardConfigurationRequestTypeDef] = None
    ACLName: Optional[str] = None


class UpdateMultiRegionClusterRequestTypeDef(BaseValidatorModel):
    MultiRegionClusterName: str
    NodeType: Optional[str] = None
    Description: Optional[str] = None
    EngineVersion: Optional[str] = None
    ShardConfiguration: Optional[ShardConfigurationRequestTypeDef] = None
    MultiRegionParameterGroupName: Optional[str] = None
    UpdateStrategy: Optional[UpdateStrategyType] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class CreateMultiRegionClusterResponseTypeDef(BaseValidatorModel):
    MultiRegionCluster: MultiRegionClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteMultiRegionClusterResponseTypeDef(BaseValidatorModel):
    MultiRegionCluster: MultiRegionClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeMultiRegionClustersResponseTypeDef(BaseValidatorModel):
    MultiRegionClusters: List[MultiRegionClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateMultiRegionClusterResponseTypeDef(BaseValidatorModel):
    MultiRegionCluster: MultiRegionClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeReservedNodesResponseTypeDef(BaseValidatorModel):
    ReservedNodes: List[ReservedNodeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PurchaseReservedNodesOfferingResponseTypeDef(BaseValidatorModel):
    ReservedNode: ReservedNodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeReservedNodesOfferingsResponseTypeDef(BaseValidatorModel):
    ReservedNodesOfferings: List[ReservedNodesOfferingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ClusterPendingUpdatesTypeDef(BaseValidatorModel):
    Resharding: Optional[ReshardingStatusTypeDef] = None
    ACLs: Optional[ACLsUpdateStatusTypeDef] = None
    ServiceUpdates: Optional[List[PendingModifiedServiceUpdateTypeDef]] = None


class ClusterConfigurationTypeDef(BaseValidatorModel):
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
    Shards: Optional[List[ShardDetailTypeDef]] = None
    MultiRegionParameterGroupName: Optional[str] = None
    MultiRegionClusterName: Optional[str] = None


class CreateSubnetGroupResponseTypeDef(BaseValidatorModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSubnetGroupResponseTypeDef(BaseValidatorModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSubnetGroupsResponseTypeDef(BaseValidatorModel):
    SubnetGroups: List[SubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateSubnetGroupResponseTypeDef(BaseValidatorModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ClusterTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[str] = None
    PendingUpdates: Optional[ClusterPendingUpdatesTypeDef] = None
    MultiRegionClusterName: Optional[str] = None
    NumberOfShards: Optional[int] = None
    Shards: Optional[List[ShardTypeDef]] = None
    AvailabilityMode: Optional[AZStatusType] = None
    ClusterEndpoint: Optional[EndpointTypeDef] = None
    NodeType: Optional[str] = None
    Engine: Optional[str] = None
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
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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
    Snapshots: List[SnapshotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


