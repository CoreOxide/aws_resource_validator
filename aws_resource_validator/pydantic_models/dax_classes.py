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
from aws_resource_validator.pydantic_models.dax_constants import *

class Endpoint(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    URL: Optional[str] = None


class NotificationConfiguration(BaseValidatorModel):
    TopicArn: Optional[str] = None
    TopicStatus: Optional[str] = None


class ParameterGroupStatus(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    NodeIdsToReboot: Optional[List[str]] = None


class SSEDescription(BaseValidatorModel):
    Status: Optional[SSEStatusType] = None


class SecurityGroupMembership(BaseValidatorModel):
    SecurityGroupIdentifier: Optional[str] = None
    Status: Optional[str] = None


class SSESpecification(BaseValidatorModel):
    Enabled: bool


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateParameterGroupRequest(BaseValidatorModel):
    ParameterGroupName: str
    Description: Optional[str] = None


class ParameterGroup(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    Description: Optional[str] = None


class CreateSubnetGroupRequest(BaseValidatorModel):
    SubnetGroupName: str
    SubnetIds: Sequence[str]
    Description: Optional[str] = None


class DecreaseReplicationFactorRequest(BaseValidatorModel):
    ClusterName: str
    NewReplicationFactor: int
    AvailabilityZones: Optional[Sequence[str]] = None
    NodeIdsToRemove: Optional[Sequence[str]] = None


class DeleteClusterRequest(BaseValidatorModel):
    ClusterName: str


class DeleteParameterGroupRequest(BaseValidatorModel):
    ParameterGroupName: str


class DeleteSubnetGroupRequest(BaseValidatorModel):
    SubnetGroupName: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeClustersRequest(BaseValidatorModel):
    ClusterNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeDefaultParametersRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Event(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    Date: Optional[datetime] = None


class DescribeParameterGroupsRequest(BaseValidatorModel):
    ParameterGroupNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeParametersRequest(BaseValidatorModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeSubnetGroupsRequest(BaseValidatorModel):
    SubnetGroupNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class IncreaseReplicationFactorRequest(BaseValidatorModel):
    ClusterName: str
    NewReplicationFactor: int
    AvailabilityZones: Optional[Sequence[str]] = None


class ListTagsRequest(BaseValidatorModel):
    ResourceName: str
    NextToken: Optional[str] = None


class NodeTypeSpecificValue(BaseValidatorModel):
    NodeType: Optional[str] = None
    Value: Optional[str] = None


class ParameterNameValue(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None


class RebootNodeRequest(BaseValidatorModel):
    ClusterName: str
    NodeId: str


class Subnet(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    ResourceName: str
    TagKeys: Sequence[str]


class UpdateClusterRequest(BaseValidatorModel):
    ClusterName: str
    Description: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    NotificationTopicArn: Optional[str] = None
    NotificationTopicStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None


class UpdateSubnetGroupRequest(BaseValidatorModel):
    SubnetGroupName: str
    Description: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None


class Node(BaseValidatorModel):
    NodeId: Optional[str] = None
    Endpoint: Optional[Endpoint] = None
    NodeCreateTime: Optional[datetime] = None
    AvailabilityZone: Optional[str] = None
    NodeStatus: Optional[str] = None
    ParameterGroupStatus: Optional[str] = None


class CreateClusterRequest(BaseValidatorModel):
    ClusterName: str
    NodeType: str
    ReplicationFactor: int
    IamRoleArn: str
    Description: Optional[str] = None
    AvailabilityZones: Optional[Sequence[str]] = None
    SubnetGroupName: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None
    PreferredMaintenanceWindow: Optional[str] = None
    NotificationTopicArn: Optional[str] = None
    ParameterGroupName: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None
    SSESpecification: Optional[SSESpecification] = None
    ClusterEndpointEncryptionType: Optional[ClusterEndpointEncryptionTypeType] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceName: str
    Tags: Sequence[Tag]


class DeleteParameterGroupResponse(BaseValidatorModel):
    DeletionMessage: str
    ResponseMetadata: ResponseMetadata


class DeleteSubnetGroupResponse(BaseValidatorModel):
    DeletionMessage: str
    ResponseMetadata: ResponseMetadata


class ListTagsResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TagResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class UntagResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class CreateParameterGroupResponse(BaseValidatorModel):
    ParameterGroup: ParameterGroup
    ResponseMetadata: ResponseMetadata


class DescribeParameterGroupsResponse(BaseValidatorModel):
    ParameterGroups: List[ParameterGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateParameterGroupResponse(BaseValidatorModel):
    ParameterGroup: ParameterGroup
    ResponseMetadata: ResponseMetadata


class DescribeClustersRequestPaginate(BaseValidatorModel):
    ClusterNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeDefaultParametersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeParameterGroupsRequestPaginate(BaseValidatorModel):
    ParameterGroupNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeParametersRequestPaginate(BaseValidatorModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeSubnetGroupsRequestPaginate(BaseValidatorModel):
    SubnetGroupNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTagsRequestPaginate(BaseValidatorModel):
    ResourceName: str
    PaginationConfig: Optional[PaginatorConfig] = None


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


class Parameter(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterType: Optional[ParameterTypeType] = None
    ParameterValue: Optional[str] = None
    NodeTypeSpecificValues: Optional[List[NodeTypeSpecificValue]] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[IsModifiableType] = None
    ChangeType: Optional[ChangeTypeType] = None


class UpdateParameterGroupRequest(BaseValidatorModel):
    ParameterGroupName: str
    ParameterNameValues: Sequence[ParameterNameValue]


class SubnetGroup(BaseValidatorModel):
    SubnetGroupName: Optional[str] = None
    Description: Optional[str] = None
    VpcId: Optional[str] = None
    Subnets: Optional[List[Subnet]] = None


class Cluster(BaseValidatorModel):
    ClusterName: Optional[str] = None
    Description: Optional[str] = None
    ClusterArn: Optional[str] = None
    TotalNodes: Optional[int] = None
    ActiveNodes: Optional[int] = None
    NodeType: Optional[str] = None
    Status: Optional[str] = None
    ClusterDiscoveryEndpoint: Optional[Endpoint] = None
    NodeIdsToRemove: Optional[List[str]] = None
    Nodes: Optional[List[Node]] = None
    PreferredMaintenanceWindow: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfiguration] = None
    SubnetGroup: Optional[str] = None
    SecurityGroups: Optional[List[SecurityGroupMembership]] = None
    IamRoleArn: Optional[str] = None
    ParameterGroup: Optional[ParameterGroupStatus] = None
    SSEDescription: Optional[SSEDescription] = None
    ClusterEndpointEncryptionType: Optional[ClusterEndpointEncryptionTypeType] = None


class DescribeDefaultParametersResponse(BaseValidatorModel):
    Parameters: List[Parameter]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeParametersResponse(BaseValidatorModel):
    Parameters: List[Parameter]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateSubnetGroupResponse(BaseValidatorModel):
    SubnetGroup: SubnetGroup
    ResponseMetadata: ResponseMetadata


class DescribeSubnetGroupsResponse(BaseValidatorModel):
    SubnetGroups: List[SubnetGroup]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateSubnetGroupResponse(BaseValidatorModel):
    SubnetGroup: SubnetGroup
    ResponseMetadata: ResponseMetadata


class CreateClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DecreaseReplicationFactorResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DeleteClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class DescribeClustersResponse(BaseValidatorModel):
    Clusters: List[Cluster]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class IncreaseReplicationFactorResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class RebootNodeResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


class UpdateClusterResponse(BaseValidatorModel):
    Cluster: Cluster
    ResponseMetadata: ResponseMetadata


