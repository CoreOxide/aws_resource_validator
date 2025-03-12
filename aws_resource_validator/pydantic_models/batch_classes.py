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
from aws_resource_validator.pydantic_models.batch_constants import *

class ArrayPropertiesDetailTypeDef(BaseValidatorModel):
    statusSummary: Optional[Dict[str, int]] = None
    size: Optional[int] = None
    index: Optional[int] = None


class ArrayPropertiesSummaryTypeDef(BaseValidatorModel):
    size: Optional[int] = None
    index: Optional[int] = None


class ArrayPropertiesTypeDef(BaseValidatorModel):
    size: Optional[int] = None


class NetworkInterfaceTypeDef(BaseValidatorModel):
    attachmentId: Optional[str] = None
    ipv6Address: Optional[str] = None
    privateIpv4Address: Optional[str] = None


class CancelJobRequestTypeDef(BaseValidatorModel):
    jobId: str
    reason: str


class EksConfigurationTypeDef(BaseValidatorModel):
    eksClusterArn: str
    kubernetesNamespace: str


class UpdatePolicyTypeDef(BaseValidatorModel):
    terminateJobsOnUpdate: Optional[bool] = None
    jobExecutionTimeoutMinutes: Optional[int] = None


class ComputeEnvironmentOrderTypeDef(BaseValidatorModel):
    order: int
    computeEnvironment: str


class Ec2ConfigurationTypeDef(BaseValidatorModel):
    imageType: str
    imageIdOverride: Optional[str] = None
    imageKubernetesVersion: Optional[str] = None


class ConsumableResourceRequirementTypeDef(BaseValidatorModel):
    consumableResource: Optional[str] = None
    quantity: Optional[int] = None


class ConsumableResourceSummaryTypeDef(BaseValidatorModel):
    consumableResourceArn: str
    consumableResourceName: str
    totalQuantity: Optional[int] = None
    inUseQuantity: Optional[int] = None
    resourceType: Optional[str] = None


class EphemeralStorageTypeDef(BaseValidatorModel):
    sizeInGiB: int


class FargatePlatformConfigurationTypeDef(BaseValidatorModel):
    platformVersion: Optional[str] = None


class KeyValuePairTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None


class MountPointTypeDef(BaseValidatorModel):
    containerPath: Optional[str] = None
    readOnly: Optional[bool] = None
    sourceVolume: Optional[str] = None


class NetworkConfigurationTypeDef(BaseValidatorModel):
    assignPublicIp: Optional[AssignPublicIpType] = None


class RepositoryCredentialsTypeDef(BaseValidatorModel):
    credentialsParameter: str


class RuntimePlatformTypeDef(BaseValidatorModel):
    operatingSystemFamily: Optional[str] = None
    cpuArchitecture: Optional[str] = None


class SecretTypeDef(BaseValidatorModel):
    name: str
    valueFrom: str


class UlimitTypeDef(BaseValidatorModel):
    hardLimit: int
    name: str
    softLimit: int


class ContainerSummaryTypeDef(BaseValidatorModel):
    exitCode: Optional[int] = None
    reason: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateConsumableResourceRequestTypeDef(BaseValidatorModel):
    consumableResourceName: str
    totalQuantity: Optional[int] = None
    resourceType: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class JobStateTimeLimitActionTypeDef(BaseValidatorModel):
    reason: str
    state: Literal["RUNNABLE"]
    maxTimeSeconds: int
    action: Literal["CANCEL"]


class DeleteComputeEnvironmentRequestTypeDef(BaseValidatorModel):
    computeEnvironment: str


class DeleteConsumableResourceRequestTypeDef(BaseValidatorModel):
    consumableResource: str


class DeleteJobQueueRequestTypeDef(BaseValidatorModel):
    jobQueue: str


class DeleteSchedulingPolicyRequestTypeDef(BaseValidatorModel):
    arn: str


class DeregisterJobDefinitionRequestTypeDef(BaseValidatorModel):
    jobDefinition: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeComputeEnvironmentsRequestTypeDef(BaseValidatorModel):
    computeEnvironments: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeConsumableResourceRequestTypeDef(BaseValidatorModel):
    consumableResource: str


class DescribeJobDefinitionsRequestTypeDef(BaseValidatorModel):
    jobDefinitions: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    jobDefinitionName: Optional[str] = None
    status: Optional[str] = None
    nextToken: Optional[str] = None


class DescribeJobQueuesRequestTypeDef(BaseValidatorModel):
    jobQueues: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeJobsRequestTypeDef(BaseValidatorModel):
    jobs: Sequence[str]


class DescribeSchedulingPoliciesRequestTypeDef(BaseValidatorModel):
    arns: Sequence[str]


class DeviceOutputTypeDef(BaseValidatorModel):
    hostPath: str
    containerPath: Optional[str] = None
    permissions: Optional[List[DeviceCgroupPermissionType]] = None


class DeviceTypeDef(BaseValidatorModel):
    hostPath: str
    containerPath: Optional[str] = None
    permissions: Optional[Sequence[DeviceCgroupPermissionType]] = None


class EFSAuthorizationConfigTypeDef(BaseValidatorModel):
    accessPointId: Optional[str] = None
    iam: Optional[EFSAuthorizationConfigIAMType] = None


class EksAttemptContainerDetailTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    containerID: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None


class EksContainerEnvironmentVariableTypeDef(BaseValidatorModel):
    name: str
    value: Optional[str] = None


class EksContainerResourceRequirementsOutputTypeDef(BaseValidatorModel):
    limits: Optional[Dict[str, str]] = None
    requests: Optional[Dict[str, str]] = None


class EksContainerSecurityContextTypeDef(BaseValidatorModel):
    runAsUser: Optional[int] = None
    runAsGroup: Optional[int] = None
    privileged: Optional[bool] = None
    allowPrivilegeEscalation: Optional[bool] = None
    readOnlyRootFilesystem: Optional[bool] = None
    runAsNonRoot: Optional[bool] = None


class EksContainerVolumeMountTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    mountPath: Optional[str] = None
    subPath: Optional[str] = None
    readOnly: Optional[bool] = None


class EksContainerResourceRequirementsTypeDef(BaseValidatorModel):
    limits: Optional[Mapping[str, str]] = None
    requests: Optional[Mapping[str, str]] = None


class EksEmptyDirTypeDef(BaseValidatorModel):
    medium: Optional[str] = None
    sizeLimit: Optional[str] = None


class EksHostPathTypeDef(BaseValidatorModel):
    path: Optional[str] = None


class EksMetadataOutputTypeDef(BaseValidatorModel):
    labels: Optional[Dict[str, str]] = None
    annotations: Optional[Dict[str, str]] = None
    namespace: Optional[str] = None


class EksMetadataTypeDef(BaseValidatorModel):
    labels: Optional[Mapping[str, str]] = None
    annotations: Optional[Mapping[str, str]] = None
    namespace: Optional[str] = None


class EksPersistentVolumeClaimTypeDef(BaseValidatorModel):
    claimName: str
    readOnly: Optional[bool] = None


class ImagePullSecretTypeDef(BaseValidatorModel):
    name: str


class EksSecretTypeDef(BaseValidatorModel):
    secretName: str
    optional: Optional[bool] = None


class EvaluateOnExitTypeDef(BaseValidatorModel):
    action: RetryActionType
    onStatusReason: Optional[str] = None
    onReason: Optional[str] = None
    onExitCode: Optional[str] = None


class ShareAttributesTypeDef(BaseValidatorModel):
    shareIdentifier: str
    weightFactor: Optional[float] = None


class FrontOfQueueJobSummaryTypeDef(BaseValidatorModel):
    jobArn: Optional[str] = None
    earliestTimeAtPosition: Optional[int] = None


class GetJobQueueSnapshotRequestTypeDef(BaseValidatorModel):
    jobQueue: str


class HostTypeDef(BaseValidatorModel):
    sourcePath: Optional[str] = None


class JobTimeoutTypeDef(BaseValidatorModel):
    attemptDurationSeconds: Optional[int] = None


class NodeDetailsTypeDef(BaseValidatorModel):
    nodeIndex: Optional[int] = None
    isMainNode: Optional[bool] = None


class NodePropertiesSummaryTypeDef(BaseValidatorModel):
    isMainNode: Optional[bool] = None
    numNodes: Optional[int] = None
    nodeIndex: Optional[int] = None


class KeyValuesPairTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None


class LaunchTemplateSpecificationOverrideOutputTypeDef(BaseValidatorModel):
    launchTemplateId: Optional[str] = None
    launchTemplateName: Optional[str] = None
    version: Optional[str] = None
    targetInstanceTypes: Optional[List[str]] = None


class LaunchTemplateSpecificationOverrideTypeDef(BaseValidatorModel):
    launchTemplateId: Optional[str] = None
    launchTemplateName: Optional[str] = None
    version: Optional[str] = None
    targetInstanceTypes: Optional[Sequence[str]] = None


class TmpfsOutputTypeDef(BaseValidatorModel):
    containerPath: str
    size: int
    mountOptions: Optional[List[str]] = None


class TmpfsTypeDef(BaseValidatorModel):
    containerPath: str
    size: int
    mountOptions: Optional[Sequence[str]] = None


class ListSchedulingPoliciesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SchedulingPolicyListingDetailTypeDef(BaseValidatorModel):
    arn: str


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TaskContainerDependencyTypeDef(BaseValidatorModel):
    containerName: Optional[str] = None
    condition: Optional[str] = None


class TerminateJobRequestTypeDef(BaseValidatorModel):
    jobId: str
    reason: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateConsumableResourceRequestTypeDef(BaseValidatorModel):
    consumableResource: str
    operation: Optional[str] = None
    quantity: Optional[int] = None
    clientToken: Optional[str] = None


class AttemptContainerDetailTypeDef(BaseValidatorModel):
    containerInstanceArn: Optional[str] = None
    taskArn: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    logStreamName: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None


class AttemptTaskContainerDetailsTypeDef(BaseValidatorModel):
    exitCode: Optional[int] = None
    name: Optional[str] = None
    reason: Optional[str] = None
    logStreamName: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None


class ConsumableResourcePropertiesOutputTypeDef(BaseValidatorModel):
    consumableResourceList: Optional[List[ConsumableResourceRequirementTypeDef]] = None


class ConsumableResourcePropertiesTypeDef(BaseValidatorModel):
    consumableResourceList: Optional[Sequence[ConsumableResourceRequirementTypeDef]] = None


class ResourceRequirementTypeDef(BaseValidatorModel):
    pass


class ContainerOverridesTypeDef(BaseValidatorModel):
    vcpus: Optional[int] = None
    memory: Optional[int] = None
    command: Optional[Sequence[str]] = None
    instanceType: Optional[str] = None
    environment: Optional[Sequence[KeyValuePairTypeDef]] = None
    resourceRequirements: Optional[Sequence[ResourceRequirementTypeDef]] = None


class TaskContainerOverridesTypeDef(BaseValidatorModel):
    command: Optional[Sequence[str]] = None
    environment: Optional[Sequence[KeyValuePairTypeDef]] = None
    name: Optional[str] = None
    resourceRequirements: Optional[Sequence[ResourceRequirementTypeDef]] = None


class LogConfigurationOutputTypeDef(BaseValidatorModel):
    logDriver: LogDriverType
    options: Optional[Dict[str, str]] = None
    secretOptions: Optional[List[SecretTypeDef]] = None


class LogConfigurationTypeDef(BaseValidatorModel):
    logDriver: LogDriverType
    options: Optional[Mapping[str, str]] = None
    secretOptions: Optional[Sequence[SecretTypeDef]] = None


class CreateComputeEnvironmentResponseTypeDef(BaseValidatorModel):
    computeEnvironmentName: str
    computeEnvironmentArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateConsumableResourceResponseTypeDef(BaseValidatorModel):
    consumableResourceName: str
    consumableResourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateJobQueueResponseTypeDef(BaseValidatorModel):
    jobQueueName: str
    jobQueueArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSchedulingPolicyResponseTypeDef(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeConsumableResourceResponseTypeDef(BaseValidatorModel):
    consumableResourceName: str
    consumableResourceArn: str
    totalQuantity: int
    inUseQuantity: int
    availableQuantity: int
    resourceType: str
    createdAt: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class ListConsumableResourcesResponseTypeDef(BaseValidatorModel):
    consumableResources: List[ConsumableResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterJobDefinitionResponseTypeDef(BaseValidatorModel):
    jobDefinitionName: str
    jobDefinitionArn: str
    revision: int
    ResponseMetadata: ResponseMetadataTypeDef


class SubmitJobResponseTypeDef(BaseValidatorModel):
    jobArn: str
    jobName: str
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateComputeEnvironmentResponseTypeDef(BaseValidatorModel):
    computeEnvironmentName: str
    computeEnvironmentArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateConsumableResourceResponseTypeDef(BaseValidatorModel):
    consumableResourceName: str
    consumableResourceArn: str
    totalQuantity: int
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateJobQueueResponseTypeDef(BaseValidatorModel):
    jobQueueName: str
    jobQueueArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateJobQueueRequestTypeDef(BaseValidatorModel):
    jobQueueName: str
    priority: int
    computeEnvironmentOrder: Sequence[ComputeEnvironmentOrderTypeDef]
    state: Optional[JQStateType] = None
    schedulingPolicyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    jobStateTimeLimitActions: Optional[Sequence[JobStateTimeLimitActionTypeDef]] = None


class JobQueueDetailTypeDef(BaseValidatorModel):
    jobQueueName: str
    jobQueueArn: str
    state: JQStateType
    priority: int
    computeEnvironmentOrder: List[ComputeEnvironmentOrderTypeDef]
    schedulingPolicyArn: Optional[str] = None
    status: Optional[JQStatusType] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    jobStateTimeLimitActions: Optional[List[JobStateTimeLimitActionTypeDef]] = None


class UpdateJobQueueRequestTypeDef(BaseValidatorModel):
    jobQueue: str
    state: Optional[JQStateType] = None
    schedulingPolicyArn: Optional[str] = None
    priority: Optional[int] = None
    computeEnvironmentOrder: Optional[Sequence[ComputeEnvironmentOrderTypeDef]] = None
    jobStateTimeLimitActions: Optional[Sequence[JobStateTimeLimitActionTypeDef]] = None


class DescribeComputeEnvironmentsRequestPaginateTypeDef(BaseValidatorModel):
    computeEnvironments: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeJobDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    jobDefinitions: Optional[Sequence[str]] = None
    jobDefinitionName: Optional[str] = None
    status: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeJobQueuesRequestPaginateTypeDef(BaseValidatorModel):
    jobQueues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSchedulingPoliciesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class EFSVolumeConfigurationTypeDef(BaseValidatorModel):
    fileSystemId: str
    rootDirectory: Optional[str] = None
    transitEncryption: Optional[EFSTransitEncryptionType] = None
    transitEncryptionPort: Optional[int] = None
    authorizationConfig: Optional[EFSAuthorizationConfigTypeDef] = None


class EksAttemptDetailTypeDef(BaseValidatorModel):
    containers: Optional[List[EksAttemptContainerDetailTypeDef]] = None
    initContainers: Optional[List[EksAttemptContainerDetailTypeDef]] = None
    eksClusterArn: Optional[str] = None
    podName: Optional[str] = None
    podNamespace: Optional[str] = None
    nodeName: Optional[str] = None
    startedAt: Optional[int] = None
    stoppedAt: Optional[int] = None
    statusReason: Optional[str] = None


class EksContainerDetailTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    image: Optional[str] = None
    imagePullPolicy: Optional[str] = None
    command: Optional[List[str]] = None
    args: Optional[List[str]] = None
    env: Optional[List[EksContainerEnvironmentVariableTypeDef]] = None
    resources: Optional[EksContainerResourceRequirementsOutputTypeDef] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    volumeMounts: Optional[List[EksContainerVolumeMountTypeDef]] = None
    securityContext: Optional[EksContainerSecurityContextTypeDef] = None


class EksContainerOutputTypeDef(BaseValidatorModel):
    image: str
    name: Optional[str] = None
    imagePullPolicy: Optional[str] = None
    command: Optional[List[str]] = None
    args: Optional[List[str]] = None
    env: Optional[List[EksContainerEnvironmentVariableTypeDef]] = None
    resources: Optional[EksContainerResourceRequirementsOutputTypeDef] = None
    volumeMounts: Optional[List[EksContainerVolumeMountTypeDef]] = None
    securityContext: Optional[EksContainerSecurityContextTypeDef] = None


class EksContainerTypeDef(BaseValidatorModel):
    image: str
    name: Optional[str] = None
    imagePullPolicy: Optional[str] = None
    command: Optional[Sequence[str]] = None
    args: Optional[Sequence[str]] = None
    env: Optional[Sequence[EksContainerEnvironmentVariableTypeDef]] = None
    resources: Optional[EksContainerResourceRequirementsTypeDef] = None
    volumeMounts: Optional[Sequence[EksContainerVolumeMountTypeDef]] = None
    securityContext: Optional[EksContainerSecurityContextTypeDef] = None


class EksVolumeTypeDef(BaseValidatorModel):
    name: str
    hostPath: Optional[EksHostPathTypeDef] = None
    emptyDir: Optional[EksEmptyDirTypeDef] = None
    secret: Optional[EksSecretTypeDef] = None
    persistentVolumeClaim: Optional[EksPersistentVolumeClaimTypeDef] = None


class RetryStrategyOutputTypeDef(BaseValidatorModel):
    attempts: Optional[int] = None
    evaluateOnExit: Optional[List[EvaluateOnExitTypeDef]] = None


class RetryStrategyTypeDef(BaseValidatorModel):
    attempts: Optional[int] = None
    evaluateOnExit: Optional[Sequence[EvaluateOnExitTypeDef]] = None


class FairsharePolicyOutputTypeDef(BaseValidatorModel):
    shareDecaySeconds: Optional[int] = None
    computeReservation: Optional[int] = None
    shareDistribution: Optional[List[ShareAttributesTypeDef]] = None


class FairsharePolicyTypeDef(BaseValidatorModel):
    shareDecaySeconds: Optional[int] = None
    computeReservation: Optional[int] = None
    shareDistribution: Optional[Sequence[ShareAttributesTypeDef]] = None


class FrontOfQueueDetailTypeDef(BaseValidatorModel):
    jobs: Optional[List[FrontOfQueueJobSummaryTypeDef]] = None
    lastUpdatedAt: Optional[int] = None


class JobSummaryTypeDef(BaseValidatorModel):
    jobId: str
    jobName: str
    jobArn: Optional[str] = None
    createdAt: Optional[int] = None
    status: Optional[JobStatusType] = None
    statusReason: Optional[str] = None
    startedAt: Optional[int] = None
    stoppedAt: Optional[int] = None
    container: Optional[ContainerSummaryTypeDef] = None
    arrayProperties: Optional[ArrayPropertiesSummaryTypeDef] = None
    nodeProperties: Optional[NodePropertiesSummaryTypeDef] = None
    jobDefinition: Optional[str] = None


class ListConsumableResourcesRequestPaginateTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[KeyValuesPairTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConsumableResourcesRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[KeyValuesPairTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobsByConsumableResourceRequestPaginateTypeDef(BaseValidatorModel):
    consumableResource: str
    filters: Optional[Sequence[KeyValuesPairTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobsByConsumableResourceRequestTypeDef(BaseValidatorModel):
    consumableResource: str
    filters: Optional[Sequence[KeyValuesPairTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobsRequestPaginateTypeDef(BaseValidatorModel):
    jobQueue: Optional[str] = None
    arrayJobId: Optional[str] = None
    multiNodeJobId: Optional[str] = None
    jobStatus: Optional[JobStatusType] = None
    filters: Optional[Sequence[KeyValuesPairTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListJobsRequestTypeDef(BaseValidatorModel):
    jobQueue: Optional[str] = None
    arrayJobId: Optional[str] = None
    multiNodeJobId: Optional[str] = None
    jobStatus: Optional[JobStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filters: Optional[Sequence[KeyValuesPairTypeDef]] = None


class LaunchTemplateSpecificationOutputTypeDef(BaseValidatorModel):
    launchTemplateId: Optional[str] = None
    launchTemplateName: Optional[str] = None
    version: Optional[str] = None
    overrides: Optional[List[LaunchTemplateSpecificationOverrideOutputTypeDef]] = None


class LinuxParametersOutputTypeDef(BaseValidatorModel):
    devices: Optional[List[DeviceOutputTypeDef]] = None
    initProcessEnabled: Optional[bool] = None
    sharedMemorySize: Optional[int] = None
    tmpfs: Optional[List[TmpfsOutputTypeDef]] = None
    maxSwap: Optional[int] = None
    swappiness: Optional[int] = None


class LinuxParametersTypeDef(BaseValidatorModel):
    devices: Optional[Sequence[DeviceTypeDef]] = None
    initProcessEnabled: Optional[bool] = None
    sharedMemorySize: Optional[int] = None
    tmpfs: Optional[Sequence[TmpfsTypeDef]] = None
    maxSwap: Optional[int] = None
    swappiness: Optional[int] = None


class ListSchedulingPoliciesResponseTypeDef(BaseValidatorModel):
    schedulingPolicies: List[SchedulingPolicyListingDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AttemptEcsTaskDetailsTypeDef(BaseValidatorModel):
    containerInstanceArn: Optional[str] = None
    taskArn: Optional[str] = None
    containers: Optional[List[AttemptTaskContainerDetailsTypeDef]] = None


class ListJobsByConsumableResourceSummaryTypeDef(BaseValidatorModel):
    jobArn: str
    jobQueueArn: str
    jobName: str
    jobStatus: str
    quantity: int
    createdAt: int
    consumableResourceProperties: ConsumableResourcePropertiesOutputTypeDef
    jobDefinitionArn: Optional[str] = None
    shareIdentifier: Optional[str] = None
    statusReason: Optional[str] = None
    startedAt: Optional[int] = None


class TaskPropertiesOverrideTypeDef(BaseValidatorModel):
    containers: Optional[Sequence[TaskContainerOverridesTypeDef]] = None


class DescribeJobQueuesResponseTypeDef(BaseValidatorModel):
    jobQueues: List[JobQueueDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class VolumeTypeDef(BaseValidatorModel):
    host: Optional[HostTypeDef] = None
    name: Optional[str] = None
    efsVolumeConfiguration: Optional[EFSVolumeConfigurationTypeDef] = None


class EksContainerResourceRequirementsUnionTypeDef(BaseValidatorModel):
    pass


class EksContainerOverrideTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    image: Optional[str] = None
    command: Optional[Sequence[str]] = None
    args: Optional[Sequence[str]] = None
    env: Optional[Sequence[EksContainerEnvironmentVariableTypeDef]] = None
    resources: Optional[EksContainerResourceRequirementsUnionTypeDef] = None


class EksPodPropertiesDetailTypeDef(BaseValidatorModel):
    serviceAccountName: Optional[str] = None
    hostNetwork: Optional[bool] = None
    dnsPolicy: Optional[str] = None
    imagePullSecrets: Optional[List[ImagePullSecretTypeDef]] = None
    containers: Optional[List[EksContainerDetailTypeDef]] = None
    initContainers: Optional[List[EksContainerDetailTypeDef]] = None
    volumes: Optional[List[EksVolumeTypeDef]] = None
    podName: Optional[str] = None
    nodeName: Optional[str] = None
    metadata: Optional[EksMetadataOutputTypeDef] = None
    shareProcessNamespace: Optional[bool] = None


class EksPodPropertiesOutputTypeDef(BaseValidatorModel):
    serviceAccountName: Optional[str] = None
    hostNetwork: Optional[bool] = None
    dnsPolicy: Optional[str] = None
    imagePullSecrets: Optional[List[ImagePullSecretTypeDef]] = None
    containers: Optional[List[EksContainerOutputTypeDef]] = None
    initContainers: Optional[List[EksContainerOutputTypeDef]] = None
    volumes: Optional[List[EksVolumeTypeDef]] = None
    metadata: Optional[EksMetadataOutputTypeDef] = None
    shareProcessNamespace: Optional[bool] = None


class EksPodPropertiesTypeDef(BaseValidatorModel):
    serviceAccountName: Optional[str] = None
    hostNetwork: Optional[bool] = None
    dnsPolicy: Optional[str] = None
    imagePullSecrets: Optional[Sequence[ImagePullSecretTypeDef]] = None
    containers: Optional[Sequence[EksContainerTypeDef]] = None
    initContainers: Optional[Sequence[EksContainerTypeDef]] = None
    volumes: Optional[Sequence[EksVolumeTypeDef]] = None
    metadata: Optional[EksMetadataTypeDef] = None
    shareProcessNamespace: Optional[bool] = None


class SchedulingPolicyDetailTypeDef(BaseValidatorModel):
    name: str
    arn: str
    fairsharePolicy: Optional[FairsharePolicyOutputTypeDef] = None
    tags: Optional[Dict[str, str]] = None


class GetJobQueueSnapshotResponseTypeDef(BaseValidatorModel):
    frontOfQueue: FrontOfQueueDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListJobsResponseTypeDef(BaseValidatorModel):
    jobSummaryList: List[JobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class LaunchTemplateSpecificationOverrideUnionTypeDef(BaseValidatorModel):
    pass


class LaunchTemplateSpecificationTypeDef(BaseValidatorModel):
    launchTemplateId: Optional[str] = None
    launchTemplateName: Optional[str] = None
    version: Optional[str] = None
    overrides: Optional[Sequence[LaunchTemplateSpecificationOverrideUnionTypeDef]] = None


class TaskContainerDetailsTypeDef(BaseValidatorModel):
    command: Optional[List[str]] = None
    dependsOn: Optional[List[TaskContainerDependencyTypeDef]] = None
    environment: Optional[List[KeyValuePairTypeDef]] = None
    essential: Optional[bool] = None
    image: Optional[str] = None
    linuxParameters: Optional[LinuxParametersOutputTypeDef] = None
    logConfiguration: Optional[LogConfigurationOutputTypeDef] = None
    mountPoints: Optional[List[MountPointTypeDef]] = None
    name: Optional[str] = None
    privileged: Optional[bool] = None
    readonlyRootFilesystem: Optional[bool] = None
    repositoryCredentials: Optional[RepositoryCredentialsTypeDef] = None
    resourceRequirements: Optional[List[ResourceRequirementTypeDef]] = None
    secrets: Optional[List[SecretTypeDef]] = None
    ulimits: Optional[List[UlimitTypeDef]] = None
    user: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    logStreamName: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None


class TaskContainerPropertiesOutputTypeDef(BaseValidatorModel):
    image: str
    command: Optional[List[str]] = None
    dependsOn: Optional[List[TaskContainerDependencyTypeDef]] = None
    environment: Optional[List[KeyValuePairTypeDef]] = None
    essential: Optional[bool] = None
    linuxParameters: Optional[LinuxParametersOutputTypeDef] = None
    logConfiguration: Optional[LogConfigurationOutputTypeDef] = None
    mountPoints: Optional[List[MountPointTypeDef]] = None
    name: Optional[str] = None
    privileged: Optional[bool] = None
    readonlyRootFilesystem: Optional[bool] = None
    repositoryCredentials: Optional[RepositoryCredentialsTypeDef] = None
    resourceRequirements: Optional[List[ResourceRequirementTypeDef]] = None
    secrets: Optional[List[SecretTypeDef]] = None
    ulimits: Optional[List[UlimitTypeDef]] = None
    user: Optional[str] = None


class TaskContainerPropertiesTypeDef(BaseValidatorModel):
    image: str
    command: Optional[Sequence[str]] = None
    dependsOn: Optional[Sequence[TaskContainerDependencyTypeDef]] = None
    environment: Optional[Sequence[KeyValuePairTypeDef]] = None
    essential: Optional[bool] = None
    linuxParameters: Optional[LinuxParametersTypeDef] = None
    logConfiguration: Optional[LogConfigurationTypeDef] = None
    mountPoints: Optional[Sequence[MountPointTypeDef]] = None
    name: Optional[str] = None
    privileged: Optional[bool] = None
    readonlyRootFilesystem: Optional[bool] = None
    repositoryCredentials: Optional[RepositoryCredentialsTypeDef] = None
    resourceRequirements: Optional[Sequence[ResourceRequirementTypeDef]] = None
    secrets: Optional[Sequence[SecretTypeDef]] = None
    ulimits: Optional[Sequence[UlimitTypeDef]] = None
    user: Optional[str] = None


class AttemptDetailTypeDef(BaseValidatorModel):
    container: Optional[AttemptContainerDetailTypeDef] = None
    startedAt: Optional[int] = None
    stoppedAt: Optional[int] = None
    statusReason: Optional[str] = None
    taskProperties: Optional[List[AttemptEcsTaskDetailsTypeDef]] = None


class ListJobsByConsumableResourceResponseTypeDef(BaseValidatorModel):
    jobs: List[ListJobsByConsumableResourceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EcsPropertiesOverrideTypeDef(BaseValidatorModel):
    taskProperties: Optional[Sequence[TaskPropertiesOverrideTypeDef]] = None


class ContainerDetailTypeDef(BaseValidatorModel):
    image: Optional[str] = None
    vcpus: Optional[int] = None
    memory: Optional[int] = None
    command: Optional[List[str]] = None
    jobRoleArn: Optional[str] = None
    executionRoleArn: Optional[str] = None
    volumes: Optional[List[VolumeTypeDef]] = None
    environment: Optional[List[KeyValuePairTypeDef]] = None
    mountPoints: Optional[List[MountPointTypeDef]] = None
    readonlyRootFilesystem: Optional[bool] = None
    ulimits: Optional[List[UlimitTypeDef]] = None
    privileged: Optional[bool] = None
    user: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    containerInstanceArn: Optional[str] = None
    taskArn: Optional[str] = None
    logStreamName: Optional[str] = None
    instanceType: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    resourceRequirements: Optional[List[ResourceRequirementTypeDef]] = None
    linuxParameters: Optional[LinuxParametersOutputTypeDef] = None
    logConfiguration: Optional[LogConfigurationOutputTypeDef] = None
    secrets: Optional[List[SecretTypeDef]] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    fargatePlatformConfiguration: Optional[FargatePlatformConfigurationTypeDef] = None
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None
    runtimePlatform: Optional[RuntimePlatformTypeDef] = None
    repositoryCredentials: Optional[RepositoryCredentialsTypeDef] = None


class ContainerPropertiesOutputTypeDef(BaseValidatorModel):
    image: Optional[str] = None
    vcpus: Optional[int] = None
    memory: Optional[int] = None
    command: Optional[List[str]] = None
    jobRoleArn: Optional[str] = None
    executionRoleArn: Optional[str] = None
    volumes: Optional[List[VolumeTypeDef]] = None
    environment: Optional[List[KeyValuePairTypeDef]] = None
    mountPoints: Optional[List[MountPointTypeDef]] = None
    readonlyRootFilesystem: Optional[bool] = None
    privileged: Optional[bool] = None
    ulimits: Optional[List[UlimitTypeDef]] = None
    user: Optional[str] = None
    instanceType: Optional[str] = None
    resourceRequirements: Optional[List[ResourceRequirementTypeDef]] = None
    linuxParameters: Optional[LinuxParametersOutputTypeDef] = None
    logConfiguration: Optional[LogConfigurationOutputTypeDef] = None
    secrets: Optional[List[SecretTypeDef]] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    fargatePlatformConfiguration: Optional[FargatePlatformConfigurationTypeDef] = None
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None
    runtimePlatform: Optional[RuntimePlatformTypeDef] = None
    repositoryCredentials: Optional[RepositoryCredentialsTypeDef] = None


class ContainerPropertiesTypeDef(BaseValidatorModel):
    image: Optional[str] = None
    vcpus: Optional[int] = None
    memory: Optional[int] = None
    command: Optional[Sequence[str]] = None
    jobRoleArn: Optional[str] = None
    executionRoleArn: Optional[str] = None
    volumes: Optional[Sequence[VolumeTypeDef]] = None
    environment: Optional[Sequence[KeyValuePairTypeDef]] = None
    mountPoints: Optional[Sequence[MountPointTypeDef]] = None
    readonlyRootFilesystem: Optional[bool] = None
    privileged: Optional[bool] = None
    ulimits: Optional[Sequence[UlimitTypeDef]] = None
    user: Optional[str] = None
    instanceType: Optional[str] = None
    resourceRequirements: Optional[Sequence[ResourceRequirementTypeDef]] = None
    linuxParameters: Optional[LinuxParametersTypeDef] = None
    logConfiguration: Optional[LogConfigurationTypeDef] = None
    secrets: Optional[Sequence[SecretTypeDef]] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    fargatePlatformConfiguration: Optional[FargatePlatformConfigurationTypeDef] = None
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None
    runtimePlatform: Optional[RuntimePlatformTypeDef] = None
    repositoryCredentials: Optional[RepositoryCredentialsTypeDef] = None


class EksMetadataUnionTypeDef(BaseValidatorModel):
    pass


class EksPodPropertiesOverrideTypeDef(BaseValidatorModel):
    containers: Optional[Sequence[EksContainerOverrideTypeDef]] = None
    initContainers: Optional[Sequence[EksContainerOverrideTypeDef]] = None
    metadata: Optional[EksMetadataUnionTypeDef] = None


class EksPropertiesDetailTypeDef(BaseValidatorModel):
    podProperties: Optional[EksPodPropertiesDetailTypeDef] = None


class EksPropertiesOutputTypeDef(BaseValidatorModel):
    podProperties: Optional[EksPodPropertiesOutputTypeDef] = None


class EksPropertiesTypeDef(BaseValidatorModel):
    podProperties: Optional[EksPodPropertiesTypeDef] = None


class DescribeSchedulingPoliciesResponseTypeDef(BaseValidatorModel):
    schedulingPolicies: List[SchedulingPolicyDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class FairsharePolicyUnionTypeDef(BaseValidatorModel):
    pass


class CreateSchedulingPolicyRequestTypeDef(BaseValidatorModel):
    name: str
    fairsharePolicy: Optional[FairsharePolicyUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateSchedulingPolicyRequestTypeDef(BaseValidatorModel):
    arn: str
    fairsharePolicy: Optional[FairsharePolicyUnionTypeDef] = None


class EcsTaskDetailsTypeDef(BaseValidatorModel):
    containers: Optional[List[TaskContainerDetailsTypeDef]] = None
    containerInstanceArn: Optional[str] = None
    taskArn: Optional[str] = None
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None
    executionRoleArn: Optional[str] = None
    platformVersion: Optional[str] = None
    ipcMode: Optional[str] = None
    taskRoleArn: Optional[str] = None
    pidMode: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    runtimePlatform: Optional[RuntimePlatformTypeDef] = None
    volumes: Optional[List[VolumeTypeDef]] = None


class EcsTaskPropertiesOutputTypeDef(BaseValidatorModel):
    containers: List[TaskContainerPropertiesOutputTypeDef]
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None
    executionRoleArn: Optional[str] = None
    platformVersion: Optional[str] = None
    ipcMode: Optional[str] = None
    taskRoleArn: Optional[str] = None
    pidMode: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    runtimePlatform: Optional[RuntimePlatformTypeDef] = None
    volumes: Optional[List[VolumeTypeDef]] = None


class EcsTaskPropertiesTypeDef(BaseValidatorModel):
    containers: Sequence[TaskContainerPropertiesTypeDef]
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None
    executionRoleArn: Optional[str] = None
    platformVersion: Optional[str] = None
    ipcMode: Optional[str] = None
    taskRoleArn: Optional[str] = None
    pidMode: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    runtimePlatform: Optional[RuntimePlatformTypeDef] = None
    volumes: Optional[Sequence[VolumeTypeDef]] = None


class EksPropertiesOverrideTypeDef(BaseValidatorModel):
    podProperties: Optional[EksPodPropertiesOverrideTypeDef] = None


class ComputeEnvironmentDetailTypeDef(BaseValidatorModel):
    pass


class DescribeComputeEnvironmentsResponseTypeDef(BaseValidatorModel):
    computeEnvironments: List[ComputeEnvironmentDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class EcsPropertiesDetailTypeDef(BaseValidatorModel):
    taskProperties: Optional[List[EcsTaskDetailsTypeDef]] = None


class EcsPropertiesOutputTypeDef(BaseValidatorModel):
    taskProperties: List[EcsTaskPropertiesOutputTypeDef]


class EcsPropertiesTypeDef(BaseValidatorModel):
    taskProperties: Sequence[EcsTaskPropertiesTypeDef]


class ConsumableResourcePropertiesUnionTypeDef(BaseValidatorModel):
    pass


class NodePropertyOverrideTypeDef(BaseValidatorModel):
    targetNodes: str
    containerOverrides: Optional[ContainerOverridesTypeDef] = None
    ecsPropertiesOverride: Optional[EcsPropertiesOverrideTypeDef] = None
    instanceTypes: Optional[Sequence[str]] = None
    eksPropertiesOverride: Optional[EksPropertiesOverrideTypeDef] = None
    consumableResourcePropertiesOverride: Optional[ConsumableResourcePropertiesUnionTypeDef] = None


class ComputeResourceUpdateTypeDef(BaseValidatorModel):
    pass


class UpdateComputeEnvironmentRequestTypeDef(BaseValidatorModel):
    computeEnvironment: str
    state: Optional[CEStateType] = None
    unmanagedvCpus: Optional[int] = None
    computeResources: Optional[ComputeResourceUpdateTypeDef] = None
    serviceRole: Optional[str] = None
    updatePolicy: Optional[UpdatePolicyTypeDef] = None
    context: Optional[str] = None


class NodeRangePropertyOutputTypeDef(BaseValidatorModel):
    targetNodes: str
    container: Optional[ContainerPropertiesOutputTypeDef] = None
    instanceTypes: Optional[List[str]] = None
    ecsProperties: Optional[EcsPropertiesOutputTypeDef] = None
    eksProperties: Optional[EksPropertiesOutputTypeDef] = None
    consumableResourceProperties: Optional[ConsumableResourcePropertiesOutputTypeDef] = None


class NodeRangePropertyTypeDef(BaseValidatorModel):
    targetNodes: str
    container: Optional[ContainerPropertiesTypeDef] = None
    instanceTypes: Optional[Sequence[str]] = None
    ecsProperties: Optional[EcsPropertiesTypeDef] = None
    eksProperties: Optional[EksPropertiesTypeDef] = None
    consumableResourceProperties: Optional[ConsumableResourcePropertiesTypeDef] = None


class NodeOverridesTypeDef(BaseValidatorModel):
    numNodes: Optional[int] = None
    nodePropertyOverrides: Optional[Sequence[NodePropertyOverrideTypeDef]] = None


class NodePropertiesOutputTypeDef(BaseValidatorModel):
    numNodes: int
    mainNode: int
    nodeRangeProperties: List[NodeRangePropertyOutputTypeDef]


class NodePropertiesTypeDef(BaseValidatorModel):
    numNodes: int
    mainNode: int
    nodeRangeProperties: Sequence[NodeRangePropertyTypeDef]


class JobDependencyTypeDef(BaseValidatorModel):
    pass


class RetryStrategyUnionTypeDef(BaseValidatorModel):
    pass


class SubmitJobRequestTypeDef(BaseValidatorModel):
    jobName: str
    jobQueue: str
    jobDefinition: str
    shareIdentifier: Optional[str] = None
    schedulingPriorityOverride: Optional[int] = None
    arrayProperties: Optional[ArrayPropertiesTypeDef] = None
    dependsOn: Optional[Sequence[JobDependencyTypeDef]] = None
    parameters: Optional[Mapping[str, str]] = None
    containerOverrides: Optional[ContainerOverridesTypeDef] = None
    nodeOverrides: Optional[NodeOverridesTypeDef] = None
    retryStrategy: Optional[RetryStrategyUnionTypeDef] = None
    propagateTags: Optional[bool] = None
    timeout: Optional[JobTimeoutTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    eksPropertiesOverride: Optional[EksPropertiesOverrideTypeDef] = None
    ecsPropertiesOverride: Optional[EcsPropertiesOverrideTypeDef] = None
    consumableResourcePropertiesOverride: Optional[ConsumableResourcePropertiesUnionTypeDef] = None


class JobDetailTypeDef(BaseValidatorModel):
    jobName: str
    jobId: str
    jobQueue: str
    status: JobStatusType
    startedAt: int
    jobDefinition: str
    jobArn: Optional[str] = None
    shareIdentifier: Optional[str] = None
    schedulingPriority: Optional[int] = None
    attempts: Optional[List[AttemptDetailTypeDef]] = None
    statusReason: Optional[str] = None
    createdAt: Optional[int] = None
    retryStrategy: Optional[RetryStrategyOutputTypeDef] = None
    stoppedAt: Optional[int] = None
    dependsOn: Optional[List[JobDependencyTypeDef]] = None
    parameters: Optional[Dict[str, str]] = None
    container: Optional[ContainerDetailTypeDef] = None
    nodeDetails: Optional[NodeDetailsTypeDef] = None
    nodeProperties: Optional[NodePropertiesOutputTypeDef] = None
    arrayProperties: Optional[ArrayPropertiesDetailTypeDef] = None
    timeout: Optional[JobTimeoutTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    propagateTags: Optional[bool] = None
    platformCapabilities: Optional[List[PlatformCapabilityType]] = None
    eksProperties: Optional[EksPropertiesDetailTypeDef] = None
    eksAttempts: Optional[List[EksAttemptDetailTypeDef]] = None
    ecsProperties: Optional[EcsPropertiesDetailTypeDef] = None
    isCancelled: Optional[bool] = None
    isTerminated: Optional[bool] = None
    consumableResourceProperties: Optional[ConsumableResourcePropertiesOutputTypeDef] = None


class JobDefinitionTypeDef(BaseValidatorModel):
    pass


class DescribeJobDefinitionsResponseTypeDef(BaseValidatorModel):
    jobDefinitions: List[JobDefinitionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeJobsResponseTypeDef(BaseValidatorModel):
    jobs: List[JobDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


