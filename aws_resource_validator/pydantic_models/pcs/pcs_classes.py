from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.pcs.pcs_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class SlurmCustomSetting(BaseValidatorModel):
    parameterName: str
    parameterValue: str


class SlurmAuthKey(BaseValidatorModel):
    secretArn: str
    secretVersion: str


class ClusterSummary(BaseValidatorModel):
    name: str
    id: str
    arn: str
    createdAt: datetime
    modifiedAt: datetime
    status: ClusterStatusType


class Endpoint(BaseValidatorModel):
    type: EndpointTypeType
    privateIpAddress: str
    port: str
    publicIpAddress: Optional[str] = None


class ErrorInfo(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class Networking(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None


class Scheduler(BaseValidatorModel):
    type: Literal['SLURM']
    version: str


class ComputeNodeGroupConfiguration(BaseValidatorModel):
    computeNodeGroupId: Optional[str] = None


class ComputeNodeGroupSummary(BaseValidatorModel):
    name: str
    id: str
    arn: str
    clusterId: str
    createdAt: datetime
    modifiedAt: datetime
    status: ComputeNodeGroupStatusType


class CustomLaunchTemplate(BaseValidatorModel):
    id: str
    version: str


class InstanceConfig(BaseValidatorModel):
    instanceType: Optional[str] = None


class ScalingConfiguration(BaseValidatorModel):
    minInstanceCount: int
    maxInstanceCount: int


class SpotOptions(BaseValidatorModel):
    allocationStrategy: Optional[SpotAllocationStrategyType] = None


class NetworkingRequest(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None


class SchedulerRequest(BaseValidatorModel):
    type: Literal['SLURM']
    version: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ScalingConfigurationRequest(BaseValidatorModel):
    minInstanceCount: int
    maxInstanceCount: int


class DeleteClusterRequest(BaseValidatorModel):
    clusterIdentifier: str
    clientToken: Optional[str] = None


class DeleteComputeNodeGroupRequest(BaseValidatorModel):
    clusterIdentifier: str
    computeNodeGroupIdentifier: str
    clientToken: Optional[str] = None


class DeleteQueueRequest(BaseValidatorModel):
    clusterIdentifier: str
    queueIdentifier: str
    clientToken: Optional[str] = None


# This class is the input for the 'get_cluster' function.
class GetClusterRequest(BaseValidatorModel):
    clusterIdentifier: str


# This class is the input for the 'get_compute_node_group' function.
class GetComputeNodeGroupRequest(BaseValidatorModel):
    clusterIdentifier: str
    computeNodeGroupIdentifier: str


# This class is the input for the 'get_queue' function.
class GetQueueRequest(BaseValidatorModel):
    clusterIdentifier: str
    queueIdentifier: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_clusters' function.
class ListClustersRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_compute_node_groups' function.
class ListComputeNodeGroupsRequest(BaseValidatorModel):
    clusterIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_queues' function.
class ListQueuesRequest(BaseValidatorModel):
    clusterIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class QueueSummary(BaseValidatorModel):
    name: str
    id: str
    arn: str
    clusterId: str
    createdAt: datetime
    modifiedAt: datetime
    status: QueueStatusType


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'register_compute_node_group_instance' function.
class RegisterComputeNodeGroupInstanceRequest(BaseValidatorModel):
    clusterIdentifier: str
    bootstrapId: str


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class ClusterSlurmConfigurationRequest(BaseValidatorModel):
    scaleDownIdleTimeInSeconds: Optional[int] = None
    slurmCustomSettings: Optional[List[SlurmCustomSetting]] = None


class ComputeNodeGroupSlurmConfigurationRequest(BaseValidatorModel):
    slurmCustomSettings: Optional[List[SlurmCustomSetting]] = None


class ComputeNodeGroupSlurmConfiguration(BaseValidatorModel):
    slurmCustomSettings: Optional[List[SlurmCustomSetting]] = None


class UpdateComputeNodeGroupSlurmConfigurationRequest(BaseValidatorModel):
    slurmCustomSettings: Optional[List[SlurmCustomSetting]] = None


class ClusterSlurmConfiguration(BaseValidatorModel):
    scaleDownIdleTimeInSeconds: Optional[int] = None
    slurmCustomSettings: Optional[List[SlurmCustomSetting]] = None
    authKey: Optional[SlurmAuthKey] = None


# This class is the input for the 'create_queue' function.
class CreateQueueRequest(BaseValidatorModel):
    clusterIdentifier: str
    queueName: str
    computeNodeGroupConfigurations: Optional[List[ComputeNodeGroupConfiguration]] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Queue(BaseValidatorModel):
    name: str
    id: str
    arn: str
    clusterId: str
    createdAt: datetime
    modifiedAt: datetime
    status: QueueStatusType
    computeNodeGroupConfigurations: List[ComputeNodeGroupConfiguration]
    errorInfo: Optional[List[ErrorInfo]] = None


# This class is the input for the 'update_queue' function.
class UpdateQueueRequest(BaseValidatorModel):
    clusterIdentifier: str
    queueIdentifier: str
    computeNodeGroupConfigurations: Optional[List[ComputeNodeGroupConfiguration]] = None
    clientToken: Optional[str] = None


# This class is the output for the 'untag_resource' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_clusters' function.
class ListClustersResponse(BaseValidatorModel):
    clusters: List[ClusterSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_compute_node_groups' function.
class ListComputeNodeGroupsResponse(BaseValidatorModel):
    computeNodeGroups: List[ComputeNodeGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_compute_node_group_instance' function.
class RegisterComputeNodeGroupInstanceResponse(BaseValidatorModel):
    nodeID: str
    sharedSecret: str
    endpoints: List[Endpoint]
    ResponseMetadata: ResponseMetadata


class ListClustersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListComputeNodeGroupsRequestPaginate(BaseValidatorModel):
    clusterIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQueuesRequestPaginate(BaseValidatorModel):
    clusterIdentifier: str
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_queues' function.
class ListQueuesResponse(BaseValidatorModel):
    queues: List[QueueSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_cluster' function.
class CreateClusterRequest(BaseValidatorModel):
    clusterName: str
    scheduler: SchedulerRequest
    size: SizeType
    networking: NetworkingRequest
    slurmConfiguration: Optional[ClusterSlurmConfigurationRequest] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_compute_node_group' function.
class CreateComputeNodeGroupRequest(BaseValidatorModel):
    clusterIdentifier: str
    computeNodeGroupName: str
    subnetIds: List[str]
    customLaunchTemplate: CustomLaunchTemplate
    iamInstanceProfileArn: str
    scalingConfiguration: ScalingConfigurationRequest
    instanceConfigs: List[InstanceConfig]
    amiId: Optional[str] = None
    purchaseOption: Optional[PurchaseOptionType] = None
    spotOptions: Optional[SpotOptions] = None
    slurmConfiguration: Optional[ComputeNodeGroupSlurmConfigurationRequest] = None
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ComputeNodeGroup(BaseValidatorModel):
    name: str
    id: str
    arn: str
    clusterId: str
    createdAt: datetime
    modifiedAt: datetime
    status: ComputeNodeGroupStatusType
    subnetIds: List[str]
    customLaunchTemplate: CustomLaunchTemplate
    iamInstanceProfileArn: str
    scalingConfiguration: ScalingConfiguration
    instanceConfigs: List[InstanceConfig]
    amiId: Optional[str] = None
    purchaseOption: Optional[PurchaseOptionType] = None
    spotOptions: Optional[SpotOptions] = None
    slurmConfiguration: Optional[ComputeNodeGroupSlurmConfiguration] = None
    errorInfo: Optional[List[ErrorInfo]] = None


# This class is the input for the 'update_compute_node_group' function.
class UpdateComputeNodeGroupRequest(BaseValidatorModel):
    clusterIdentifier: str
    computeNodeGroupIdentifier: str
    amiId: Optional[str] = None
    subnetIds: Optional[List[str]] = None
    customLaunchTemplate: Optional[CustomLaunchTemplate] = None
    purchaseOption: Optional[PurchaseOptionType] = None
    spotOptions: Optional[SpotOptions] = None
    scalingConfiguration: Optional[ScalingConfigurationRequest] = None
    iamInstanceProfileArn: Optional[str] = None
    slurmConfiguration: Optional[UpdateComputeNodeGroupSlurmConfigurationRequest] = None
    clientToken: Optional[str] = None


class Cluster(BaseValidatorModel):
    name: str
    id: str
    arn: str
    status: ClusterStatusType
    createdAt: datetime
    modifiedAt: datetime
    scheduler: Scheduler
    size: SizeType
    networking: Networking
    slurmConfiguration: Optional[ClusterSlurmConfiguration] = None
    endpoints: Optional[List[Endpoint]] = None
    errorInfo: Optional[List[ErrorInfo]] = None


# This class is the output for the 'create_queue' function.
class CreateQueueResponse(BaseValidatorModel):
    queue: Queue
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_queue' function.
class GetQueueResponse(BaseValidatorModel):
    queue: Queue
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_queue' function.
class UpdateQueueResponse(BaseValidatorModel):
    queue: Queue
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_compute_node_group' function.
class CreateComputeNodeGroupResponse(BaseValidatorModel):
    computeNodeGroup: ComputeNodeGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_compute_node_group' function.
class GetComputeNodeGroupResponse(BaseValidatorModel):
    computeNodeGroup: ComputeNodeGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_compute_node_group' function.
class UpdateComputeNodeGroupResponse(BaseValidatorModel):
    computeNodeGroup: ComputeNodeGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cluster' function.
class CreateClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_cluster' function.
class GetClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata