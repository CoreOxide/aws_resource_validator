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
from aws_resource_validator.pydantic_models.dax_constants import *

class EndpointTypeDef(BaseModel):
    Address: Optional[str] = None
    Port: Optional[int] = None
    URL: Optional[str] = None

class NotificationConfigurationTypeDef(BaseModel):
    TopicArn: Optional[str] = None
    TopicStatus: Optional[str] = None

class ParameterGroupStatusTypeDef(BaseModel):
    ParameterGroupName: Optional[str] = None
    ParameterApplyStatus: Optional[str] = None
    NodeIdsToReboot: Optional[List[str]] = None

class SSEDescriptionTypeDef(BaseModel):
    Status: Optional[SSEStatusType] = None

class SecurityGroupMembershipTypeDef(BaseModel):
    SecurityGroupIdentifier: Optional[str] = None
    Status: Optional[str] = None

class SSESpecificationTypeDef(BaseModel):
    Enabled: bool

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateParameterGroupRequestRequestTypeDef(BaseModel):
    ParameterGroupName: str
    Description: Optional[str] = None

class ParameterGroupTypeDef(BaseModel):
    ParameterGroupName: Optional[str] = None
    Description: Optional[str] = None

class CreateSubnetGroupRequestRequestTypeDef(BaseModel):
    SubnetGroupName: str
    SubnetIds: Sequence[str]
    Description: Optional[str] = None

class DecreaseReplicationFactorRequestRequestTypeDef(BaseModel):
    ClusterName: str
    NewReplicationFactor: int
    AvailabilityZones: Optional[Sequence[str]] = None
    NodeIdsToRemove: Optional[Sequence[str]] = None

class DeleteClusterRequestRequestTypeDef(BaseModel):
    ClusterName: str

class DeleteParameterGroupRequestRequestTypeDef(BaseModel):
    ParameterGroupName: str

class DeleteSubnetGroupRequestRequestTypeDef(BaseModel):
    SubnetGroupName: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeClustersRequestRequestTypeDef(BaseModel):
    ClusterNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeDefaultParametersRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class EventTypeDef(BaseModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    Date: Optional[datetime] = None

class DescribeParameterGroupsRequestRequestTypeDef(BaseModel):
    ParameterGroupNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeParametersRequestRequestTypeDef(BaseModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeSubnetGroupsRequestRequestTypeDef(BaseModel):
    SubnetGroupNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class IncreaseReplicationFactorRequestRequestTypeDef(BaseModel):
    ClusterName: str
    NewReplicationFactor: int
    AvailabilityZones: Optional[Sequence[str]] = None

class ListTagsRequestRequestTypeDef(BaseModel):
    ResourceName: str
    NextToken: Optional[str] = None

class NodeTypeSpecificValueTypeDef(BaseModel):
    NodeType: Optional[str] = None
    Value: Optional[str] = None

class ParameterNameValueTypeDef(BaseModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None

class RebootNodeRequestRequestTypeDef(BaseModel):
    ClusterName: str
    NodeId: str

class SubnetTypeDef(BaseModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceName: str
    TagKeys: Sequence[str]

class UpdateClusterRequestRequestTypeDef(BaseModel):
    ClusterName: str
    Description: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    NotificationTopicArn: Optional[str] = None
    NotificationTopicStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class UpdateSubnetGroupRequestRequestTypeDef(BaseModel):
    SubnetGroupName: str
    Description: Optional[str] = None
    SubnetIds: Optional[Sequence[str]] = None

class NodeTypeDef(BaseModel):
    NodeId: Optional[str] = None
    Endpoint: Optional[EndpointTypeDef] = None
    NodeCreateTime: Optional[datetime] = None
    AvailabilityZone: Optional[str] = None
    NodeStatus: Optional[str] = None
    ParameterGroupStatus: Optional[str] = None

class CreateClusterRequestRequestTypeDef(BaseModel):
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

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceName: str
    Tags: Sequence[TagTypeDef]

class DeleteParameterGroupResponseTypeDef(BaseModel):
    DeletionMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSubnetGroupResponseTypeDef(BaseModel):
    DeletionMessage: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UntagResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateParameterGroupResponseTypeDef(BaseModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeParameterGroupsResponseTypeDef(BaseModel):
    NextToken: str
    ParameterGroups: List[ParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateParameterGroupResponseTypeDef(BaseModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClustersRequestDescribeClustersPaginateTypeDef(BaseModel):
    ClusterNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDefaultParametersRequestDescribeDefaultParametersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeParameterGroupsRequestDescribeParameterGroupsPaginateTypeDef(BaseModel):
    ParameterGroupNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeParametersRequestDescribeParametersPaginateTypeDef(BaseModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateTypeDef(BaseModel):
    SubnetGroupNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsRequestListTagsPaginateTypeDef(BaseModel):
    ResourceName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

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

class ParameterTypeDef(BaseModel):
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

class UpdateParameterGroupRequestRequestTypeDef(BaseModel):
    ParameterGroupName: str
    ParameterNameValues: Sequence[ParameterNameValueTypeDef]

class SubnetGroupTypeDef(BaseModel):
    SubnetGroupName: Optional[str] = None
    Description: Optional[str] = None
    VpcId: Optional[str] = None
    Subnets: Optional[List[SubnetTypeDef]] = None

class ClusterTypeDef(BaseModel):
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

class DescribeDefaultParametersResponseTypeDef(BaseModel):
    NextToken: str
    Parameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeParametersResponseTypeDef(BaseModel):
    NextToken: str
    Parameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubnetGroupResponseTypeDef(BaseModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSubnetGroupsResponseTypeDef(BaseModel):
    NextToken: str
    SubnetGroups: List[SubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSubnetGroupResponseTypeDef(BaseModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DecreaseReplicationFactorResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClustersResponseTypeDef(BaseModel):
    NextToken: str
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IncreaseReplicationFactorResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootNodeResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterResponseTypeDef(BaseModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

