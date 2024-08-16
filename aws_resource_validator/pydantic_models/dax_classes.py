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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class CreateParameterGroupRequestRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    Description: Optional[str] = None

class ParameterGroupTypeDef(BaseValidatorModel):
    ParameterGroupName: Optional[str] = None
    Description: Optional[str] = None

class CreateSubnetGroupRequestRequestTypeDef(BaseValidatorModel):
    SubnetGroupName: str
    SubnetIds: Sequence[str]
    Description: Optional[str] = None

class DecreaseReplicationFactorRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    NewReplicationFactor: int
    AvailabilityZones: Optional[Sequence[str]] = None
    NodeIdsToRemove: Optional[Sequence[str]] = None

class DeleteClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str

class DeleteParameterGroupRequestRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str

class DeleteSubnetGroupRequestRequestTypeDef(BaseValidatorModel):
    SubnetGroupName: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeClustersRequestRequestTypeDef(BaseValidatorModel):
    ClusterNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeDefaultParametersRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class EventTypeDef(BaseValidatorModel):
    SourceName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Message: Optional[str] = None
    Date: Optional[datetime] = None

class DescribeParameterGroupsRequestRequestTypeDef(BaseValidatorModel):
    ParameterGroupNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeParametersRequestRequestTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class DescribeSubnetGroupsRequestRequestTypeDef(BaseValidatorModel):
    SubnetGroupNames: Optional[Sequence[str]] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class IncreaseReplicationFactorRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    NewReplicationFactor: int
    AvailabilityZones: Optional[Sequence[str]] = None

class ListTagsRequestRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    NextToken: Optional[str] = None

class NodeTypeSpecificValueTypeDef(BaseValidatorModel):
    NodeType: Optional[str] = None
    Value: Optional[str] = None

class ParameterNameValueTypeDef(BaseValidatorModel):
    ParameterName: Optional[str] = None
    ParameterValue: Optional[str] = None

class RebootNodeRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    NodeId: str

class SubnetTypeDef(BaseValidatorModel):
    SubnetIdentifier: Optional[str] = None
    SubnetAvailabilityZone: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceName: str
    TagKeys: Sequence[str]

class UpdateClusterRequestRequestTypeDef(BaseValidatorModel):
    ClusterName: str
    Description: Optional[str] = None
    PreferredMaintenanceWindow: Optional[str] = None
    NotificationTopicArn: Optional[str] = None
    NotificationTopicStatus: Optional[str] = None
    ParameterGroupName: Optional[str] = None
    SecurityGroupIds: Optional[Sequence[str]] = None

class UpdateSubnetGroupRequestRequestTypeDef(BaseValidatorModel):
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

class CreateClusterRequestRequestTypeDef(BaseValidatorModel):
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

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    NextToken: str
    ParameterGroups: List[ParameterGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateParameterGroupResponseTypeDef(BaseValidatorModel):
    ParameterGroup: ParameterGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClustersRequestDescribeClustersPaginateTypeDef(BaseValidatorModel):
    ClusterNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeDefaultParametersRequestDescribeDefaultParametersPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeParameterGroupsRequestDescribeParameterGroupsPaginateTypeDef(BaseValidatorModel):
    ParameterGroupNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeParametersRequestDescribeParametersPaginateTypeDef(BaseValidatorModel):
    ParameterGroupName: str
    Source: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeSubnetGroupsRequestDescribeSubnetGroupsPaginateTypeDef(BaseValidatorModel):
    SubnetGroupNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTagsRequestListTagsPaginateTypeDef(BaseValidatorModel):
    ResourceName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

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

class UpdateParameterGroupRequestRequestTypeDef(BaseValidatorModel):
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
    NextToken: str
    Parameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeParametersResponseTypeDef(BaseValidatorModel):
    NextToken: str
    Parameters: List[ParameterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSubnetGroupResponseTypeDef(BaseValidatorModel):
    SubnetGroup: SubnetGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSubnetGroupsResponseTypeDef(BaseValidatorModel):
    NextToken: str
    SubnetGroups: List[SubnetGroupTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

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
    NextToken: str
    Clusters: List[ClusterTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IncreaseReplicationFactorResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RebootNodeResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterResponseTypeDef(BaseValidatorModel):
    Cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

