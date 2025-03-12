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

class SlurmCustomSettingTypeDef(BaseValidatorModel):
    parameterName: str
    parameterValue: str


class SlurmAuthKeyTypeDef(BaseValidatorModel):
    secretArn: str
    secretVersion: str


class ErrorInfoTypeDef(BaseValidatorModel):
    code: Optional[str] = None
    message: Optional[str] = None


class NetworkingTypeDef(BaseValidatorModel):
    subnetIds: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None


class ComputeNodeGroupConfigurationTypeDef(BaseValidatorModel):
    computeNodeGroupId: Optional[str] = None


class InstanceConfigTypeDef(BaseValidatorModel):
    instanceType: Optional[str] = None


class ScalingConfigurationTypeDef(BaseValidatorModel):
    minInstanceCount: int
    maxInstanceCount: int


class SpotOptionsTypeDef(BaseValidatorModel):
    allocationStrategy: Optional[SpotAllocationStrategyType] = None


class NetworkingRequestTypeDef(BaseValidatorModel):
    subnetIds: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ScalingConfigurationRequestTypeDef(BaseValidatorModel):
    minInstanceCount: int
    maxInstanceCount: int


class DeleteClusterRequestTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    clientToken: Optional[str] = None


class DeleteComputeNodeGroupRequestTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    computeNodeGroupIdentifier: str
    clientToken: Optional[str] = None


class DeleteQueueRequestTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    queueIdentifier: str
    clientToken: Optional[str] = None


class GetClusterRequestTypeDef(BaseValidatorModel):
    clusterIdentifier: str


class GetComputeNodeGroupRequestTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    computeNodeGroupIdentifier: str


class GetQueueRequestTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    queueIdentifier: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListClustersRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListComputeNodeGroupsRequestTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListQueuesRequestTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class RegisterComputeNodeGroupInstanceRequestTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    bootstrapId: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class ClusterSlurmConfigurationRequestTypeDef(BaseValidatorModel):
    scaleDownIdleTimeInSeconds: Optional[int] = None
    slurmCustomSettings: Optional[Sequence[SlurmCustomSettingTypeDef]] = None


class ComputeNodeGroupSlurmConfigurationRequestTypeDef(BaseValidatorModel):
    slurmCustomSettings: Optional[Sequence[SlurmCustomSettingTypeDef]] = None


class ComputeNodeGroupSlurmConfigurationTypeDef(BaseValidatorModel):
    slurmCustomSettings: Optional[List[SlurmCustomSettingTypeDef]] = None


class UpdateComputeNodeGroupSlurmConfigurationRequestTypeDef(BaseValidatorModel):
    slurmCustomSettings: Optional[Sequence[SlurmCustomSettingTypeDef]] = None


class ClusterSlurmConfigurationTypeDef(BaseValidatorModel):
    scaleDownIdleTimeInSeconds: Optional[int] = None
    slurmCustomSettings: Optional[List[SlurmCustomSettingTypeDef]] = None
    authKey: Optional[SlurmAuthKeyTypeDef] = None


class CreateQueueRequestTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    queueName: str
    computeNodeGroupConfigurations: Optional[Sequence[ComputeNodeGroupConfigurationTypeDef]] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateQueueRequestTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    queueIdentifier: str
    computeNodeGroupConfigurations: Optional[Sequence[ComputeNodeGroupConfigurationTypeDef]] = None
    clientToken: Optional[str] = None


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class ClusterSummaryTypeDef(BaseValidatorModel):
    pass


class ListClustersResponseTypeDef(BaseValidatorModel):
    clusters: List[ClusterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ComputeNodeGroupSummaryTypeDef(BaseValidatorModel):
    pass


class ListComputeNodeGroupsResponseTypeDef(BaseValidatorModel):
    computeNodeGroups: List[ComputeNodeGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class EndpointTypeDef(BaseValidatorModel):
    pass


class RegisterComputeNodeGroupInstanceResponseTypeDef(BaseValidatorModel):
    nodeID: str
    sharedSecret: str
    endpoints: List[EndpointTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListClustersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListComputeNodeGroupsRequestPaginateTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQueuesRequestPaginateTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class QueueSummaryTypeDef(BaseValidatorModel):
    pass


class ListQueuesResponseTypeDef(BaseValidatorModel):
    queues: List[QueueSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SchedulerRequestTypeDef(BaseValidatorModel):
    pass


class CreateClusterRequestTypeDef(BaseValidatorModel):
    clusterName: str
    scheduler: SchedulerRequestTypeDef
    size: SizeType
    networking: NetworkingRequestTypeDef
    slurmConfiguration: Optional[ClusterSlurmConfigurationRequestTypeDef] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class CustomLaunchTemplateTypeDef(BaseValidatorModel):
    pass


class CreateComputeNodeGroupRequestTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    computeNodeGroupName: str
    subnetIds: Sequence[str]
    customLaunchTemplate: CustomLaunchTemplateTypeDef
    iamInstanceProfileArn: str
    scalingConfiguration: ScalingConfigurationRequestTypeDef
    instanceConfigs: Sequence[InstanceConfigTypeDef]
    amiId: Optional[str] = None
    purchaseOption: Optional[PurchaseOptionType] = None
    spotOptions: Optional[SpotOptionsTypeDef] = None
    slurmConfiguration: Optional[ComputeNodeGroupSlurmConfigurationRequestTypeDef] = None
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateComputeNodeGroupRequestTypeDef(BaseValidatorModel):
    clusterIdentifier: str
    computeNodeGroupIdentifier: str
    amiId: Optional[str] = None
    subnetIds: Optional[Sequence[str]] = None
    customLaunchTemplate: Optional[CustomLaunchTemplateTypeDef] = None
    purchaseOption: Optional[PurchaseOptionType] = None
    spotOptions: Optional[SpotOptionsTypeDef] = None
    scalingConfiguration: Optional[ScalingConfigurationRequestTypeDef] = None
    iamInstanceProfileArn: Optional[str] = None
    slurmConfiguration: Optional[UpdateComputeNodeGroupSlurmConfigurationRequestTypeDef] = None
    clientToken: Optional[str] = None


class QueueTypeDef(BaseValidatorModel):
    pass


class CreateQueueResponseTypeDef(BaseValidatorModel):
    queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetQueueResponseTypeDef(BaseValidatorModel):
    queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateQueueResponseTypeDef(BaseValidatorModel):
    queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ComputeNodeGroupTypeDef(BaseValidatorModel):
    pass


class CreateComputeNodeGroupResponseTypeDef(BaseValidatorModel):
    computeNodeGroup: ComputeNodeGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetComputeNodeGroupResponseTypeDef(BaseValidatorModel):
    computeNodeGroup: ComputeNodeGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateComputeNodeGroupResponseTypeDef(BaseValidatorModel):
    computeNodeGroup: ComputeNodeGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ClusterTypeDef(BaseValidatorModel):
    pass


class CreateClusterResponseTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetClusterResponseTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


