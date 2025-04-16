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
from aws_resource_validator.pydantic_models.pcs_constants import *

class SlurmCustomSetting(BaseValidatorModel):
    parameterName: str
    parameterValue: str


class SlurmAuthKey(BaseValidatorModel):
    secretArn: str
    secretVersion: str


class ErrorInfo(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class Networking(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None


class ComputeNodeGroupConfiguration(BaseValidatorModel):
    computeNodeGroupId: Optional[str] = None


class InstanceConfig(BaseValidatorModel):
    instanceType: Optional[str] = None


class ScalingConfiguration(BaseValidatorModel):
    minInstanceCount: int
    maxInstanceCount: int


class SpotOptions(BaseValidatorModel):
    allocationStrategy: Optional[SpotAllocationStrategyType] = None


class NetworkingRequest(BaseValidatorModel):
    subnetIds: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None


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


class GetClusterRequest(BaseValidatorModel):
    clusterIdentifier: str


class GetComputeNodeGroupRequest(BaseValidatorModel):
    clusterIdentifier: str
    computeNodeGroupIdentifier: str


class GetQueueRequest(BaseValidatorModel):
    clusterIdentifier: str
    queueIdentifier: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListClustersRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListComputeNodeGroupsRequest(BaseValidatorModel):
    clusterIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListQueuesRequest(BaseValidatorModel):
    clusterIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class RegisterComputeNodeGroupInstanceRequest(BaseValidatorModel):
    clusterIdentifier: str
    bootstrapId: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class ClusterSlurmConfigurationRequest(BaseValidatorModel):
    scaleDownIdleTimeInSeconds: Optional[int] = None
    slurmCustomSettings: Optional[Sequence[SlurmCustomSetting]] = None


class ComputeNodeGroupSlurmConfigurationRequest(BaseValidatorModel):
    slurmCustomSettings: Optional[Sequence[SlurmCustomSetting]] = None


class ComputeNodeGroupSlurmConfiguration(BaseValidatorModel):
    slurmCustomSettings: Optional[List[SlurmCustomSetting]] = None


class UpdateComputeNodeGroupSlurmConfigurationRequest(BaseValidatorModel):
    slurmCustomSettings: Optional[Sequence[SlurmCustomSetting]] = None


class ClusterSlurmConfiguration(BaseValidatorModel):
    scaleDownIdleTimeInSeconds: Optional[int] = None
    slurmCustomSettings: Optional[List[SlurmCustomSetting]] = None
    authKey: Optional[SlurmAuthKey] = None


class CreateQueueRequest(BaseValidatorModel):
    clusterIdentifier: str
    queueName: str
    computeNodeGroupConfigurations: Optional[Sequence[ComputeNodeGroupConfiguration]] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateQueueRequest(BaseValidatorModel):
    clusterIdentifier: str
    queueIdentifier: str
    computeNodeGroupConfigurations: Optional[Sequence[ComputeNodeGroupConfiguration]] = None
    clientToken: Optional[str] = None


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ClusterSummary(BaseValidatorModel):
    pass


class ListClustersResponse(BaseValidatorModel):
    clusters: List[ClusterSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ComputeNodeGroupSummary(BaseValidatorModel):
    pass


class ListComputeNodeGroupsResponse(BaseValidatorModel):
    computeNodeGroups: List[ComputeNodeGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class Endpoint(BaseValidatorModel):
    pass


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


class QueueSummary(BaseValidatorModel):
    pass


class ListQueuesResponse(BaseValidatorModel):
    queues: List[QueueSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SchedulerRequest(BaseValidatorModel):
    pass


class CreateClusterRequest(BaseValidatorModel):
    clusterName: str
    scheduler: SchedulerRequest
    size: SizeType
    networking: NetworkingRequest
    slurmConfiguration: Optional[ClusterSlurmConfigurationRequest] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CustomLaunchTemplate(BaseValidatorModel):
    pass


class CreateComputeNodeGroupRequest(BaseValidatorModel):
    clusterIdentifier: str
    computeNodeGroupName: str
    subnetIds: Sequence[str]
    customLaunchTemplate: CustomLaunchTemplate
    iamInstanceProfileArn: str
    scalingConfiguration: ScalingConfigurationRequest
    instanceConfigs: Sequence[InstanceConfig]
    amiId: Optional[str] = None
    purchaseOption: Optional[PurchaseOptionType] = None
    spotOptions: Optional[SpotOptions] = None
    slurmConfiguration: Optional[ComputeNodeGroupSlurmConfigurationRequest] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateComputeNodeGroupRequest(BaseValidatorModel):
    clusterIdentifier: str
    computeNodeGroupIdentifier: str
    amiId: Optional[str] = None
    subnetIds: Optional[Sequence[str]] = None
    customLaunchTemplate: Optional[CustomLaunchTemplate] = None
    purchaseOption: Optional[PurchaseOptionType] = None
    spotOptions: Optional[SpotOptions] = None
    scalingConfiguration: Optional[ScalingConfigurationRequest] = None
    iamInstanceProfileArn: Optional[str] = None
    slurmConfiguration: Optional[UpdateComputeNodeGroupSlurmConfigurationRequest] = None
    clientToken: Optional[str] = None


class Queue(BaseValidatorModel):
    pass


class CreateQueueResponse(BaseValidatorModel):
    queue: Queue
    ResponseMetadata: ResponseMetadata


class GetQueueResponse(BaseValidatorModel):
    queue: Queue
    ResponseMetadata: ResponseMetadata


class UpdateQueueResponse(BaseValidatorModel):
    queue: Queue
    ResponseMetadata: ResponseMetadata


class ComputeNodeGroup(BaseValidatorModel):
    pass


class CreateComputeNodeGroupResponse(BaseValidatorModel):
    computeNodeGroup: ComputeNodeGroup
    ResponseMetadata: ResponseMetadata


class GetComputeNodeGroupResponse(BaseValidatorModel):
    computeNodeGroup: ComputeNodeGroup
    ResponseMetadata: ResponseMetadata


class UpdateComputeNodeGroupResponse(BaseValidatorModel):
    computeNodeGroup: ComputeNodeGroup
    ResponseMetadata: ResponseMetadata


class Cluster(BaseValidatorModel):
    pass


class CreateClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


class GetClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


