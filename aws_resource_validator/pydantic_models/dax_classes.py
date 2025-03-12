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

class EndpointTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    URL: Optional[str] = None


class NotificationConfigurationTypeDef(BaseValidatorModel):
    TopicArn: Optional[str] = None
    TopicStatus: Optional[str] = None


class ParameterGroupStatusTypeDef(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    NodeIdsToReboot: Optional[List[str]] = None


class SSEDescriptionTypeDef(BaseValidatorModel):
    Status: Optional[SSEStatusType] = None


class SecurityGroupMembershipTypeDef(BaseValidatorModel):
    SecurityGroupIdentifier: Optional[str] = None
    Status: Optional[str] = None


class SSESpecificationTypeDef(BaseValidatorModel):
    Enabled: bool


class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateParameterGroupRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    Description: Optional[str] = None


class ParameterGroupTypeDef(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    Description: Optional[str] = None


class CreateSubnetGroupRequestTypeDef(BaseValidatorModel):
    SubnetGroupName: str
    SubnetIds: Sequence[str]
    Description: Optional[str] = None


class DecreaseReplicationFactorRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    NewReplicationFactor: int
    AvailabilityZones: Optional[Sequence[str]] = None
    NodeIdsToRemove: Optional[Sequence[str]] = None


class DeleteClusterRequestTypeDef(BaseValidatorModel):
    ClusterName: str


class DeleteParameterGroupRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str


class DeleteSubnetGroupRequestTypeDef(BaseValidatorModel):
    SubnetGroupName: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeClustersRequestTypeDef(BaseValidatorModel):
    ClusterNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeDefaultParametersRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class EventTypeDef(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    Date: Optional[datetime] = None


class DescribeParameterGroupsRequestTypeDef(BaseValidatorModel):
    ParameterGroupNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeParametersRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class DescribeSubnetGroupsRequestTypeDef(BaseValidatorModel):
    SubnetGroupNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class IncreaseReplicationFactorRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    NewReplicationFactor: int
    AvailabilityZones: Optional[Sequence[str]] = None


class ListTagsRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    NextToken: Optional[str] = None


class NodeTypeSpecificValueTypeDef(BaseValidatorModel):
    NodeType: Optional[str] = None
    Value: Optional[str] = None


class ParameterNameValueTypeDef(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None


class RebootNodeRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    NodeId: str


class SubnetTypeDef(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    TagKeys: Sequence[str]


class UpdateClusterRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    Description: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    NotificationTopicArn: Optional[str] = None
    NotificationTopicStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None


class UpdateSubnetGroupRequestTypeDef(BaseValidatorModel):
    SubnetGroupName: str
    Description: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None


class NodeTypeDef(BaseValidatorModel):
    NodeId: Optional[str] = None
    Endpoint: Optional[EndpointTypeDef] = None
    NodeCreateTime: Optional[datetime] = None
    AvailabilityZone: Optional[str] = None
    NodeStatus: Optional[str] = None
    ParameterGroupStatus: Optional[str] = None


class CreateClusterRequestTypeDef(BaseValidatorModel):
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
    Tags: Optional[Sequence[TagTypeDef]] = None
    SSESpecification: Optional[SSESpecificationTypeDef] = None
    ClusterEndpointEncryptionType: Optional[ClusterEndpointEncryptionTypeType] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    Tags: Sequence[TagTypeDef]


class DeleteParameterGroupResponseTypeDef(BaseValidatorModel):
    DeletionMessage: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteSubnetGroupResponseTypeDef(BaseValidatorModel):
    DeletionMessage: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TagResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UntagResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateParameterGroupResponseTypeDef(BaseValidatorModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeParameterGroupsResponseTypeDef(BaseValidatorModel):
    ParameterGroups: List[ParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateParameterGroupResponseTypeDef(BaseValidatorModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeClustersRequestPaginateTypeDef(BaseValidatorModel):
    ClusterNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeDefaultParametersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeParameterGroupsRequestPaginateTypeDef(BaseValidatorModel):
    ParameterGroupNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeParametersRequestPaginateTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeSubnetGroupsRequestPaginateTypeDef(BaseValidatorModel):
    SubnetGroupNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTagsRequestPaginateTypeDef(BaseValidatorModel):
    ResourceName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


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


class ParameterTypeDef(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterType: Optional[ParameterTypeType] = None
    ParameterValue: Optional[str] = None
    NodeTypeSpecificValues: Optional[List[NodeTypeSpecificValueTypeDef]] = None
    Description: Optional[str] = None
    Source: Optional[str] = None
    DataType: Optional[str] = None
    AllowedValues: Optional[str] = None
    IsModifiable: Optional[IsModifiableType] = None
    ChangeType: Optional[ChangeTypeType] = None


class UpdateParameterGroupRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    ParameterNameValues: Sequence[ParameterNameValueTypeDef]


class SubnetGroupTypeDef(BaseValidatorModel):
    SubnetGroupName: Optional[str] = None
    Description: Optional[str] = None
    VpcId: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None


class ClusterTypeDef(BaseValidatorModel):
    ClusterName: Optional[str] = None
    Description: Optional[str] = None
    ClusterArn: Optional[str] = None
    TotalNodes: Optional[int] = None
    ActiveNodes: Optional[int] = None
    NodeType: Optional[str] = None
    Status: Optional[str] = None
    ClusterDiscoveryEndpoint: Optional[EndpointTypeDef] = None
    NodeIdsToRemove: Optional[List[str]] = None
    Nodes: Optional[List[NodeTypeDef]] = None
    PreferredMaintenanceWindow: Optional[str] = None
    NotificationConfiguration: Optional[NotificationConfigurationTypeDef] = None
    SubnetGroup: Optional[str] = None
    SecurityGroups: Optional[List[SecurityGroupMembershipTypeDef]] = None
    IamRoleArn: Optional[str] = None
    ParameterGroup: Optional[ParameterGroupStatusTypeDef] = None
    SSEDescription: Optional[SSEDescriptionTypeDef] = None
    ClusterEndpointEncryptionType: Optional[ClusterEndpointEncryptionTypeType] = None


class DescribeDefaultParametersResponseTypeDef(BaseValidatorModel):
    Parameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeParametersResponseTypeDef(BaseValidatorModel):
    Parameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class CreateSubnetGroupResponseTypeDef(BaseValidatorModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeSubnetGroupsResponseTypeDef(BaseValidatorModel):
    SubnetGroups: List[SubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateSubnetGroupResponseTypeDef(BaseValidatorModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateClusterResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DecreaseReplicationFactorResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteClusterResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeClustersResponseTypeDef(BaseValidatorModel):
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class IncreaseReplicationFactorResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RebootNodeResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateClusterResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


