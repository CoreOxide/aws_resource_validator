from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.batch.batch_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ArrayPropertiesDetail(BaseValidatorModel):
    statusSummary: Optional[Dict[str, int]] = None
    size: Optional[int] = None
    index: Optional[int] = None


class ArrayPropertiesSummary(BaseValidatorModel):
    size: Optional[int] = None
    index: Optional[int] = None


class ArrayProperties(BaseValidatorModel):
    size: Optional[int] = None


class NetworkInterface(BaseValidatorModel):
    attachmentId: Optional[str] = None
    ipv6Address: Optional[str] = None
    privateIpv4Address: Optional[str] = None


class CancelJobRequest(BaseValidatorModel):
    jobId: str
    reason: str


class EksConfiguration(BaseValidatorModel):
    eksClusterArn: str
    kubernetesNamespace: str


class UpdatePolicy(BaseValidatorModel):
    terminateJobsOnUpdate: Optional[bool] = None
    jobExecutionTimeoutMinutes: Optional[int] = None


class ComputeEnvironmentOrder(BaseValidatorModel):
    order: int
    computeEnvironment: str


class Ec2Configuration(BaseValidatorModel):
    imageType: str
    imageIdOverride: Optional[str] = None
    imageKubernetesVersion: Optional[str] = None


class ConsumableResourceRequirement(BaseValidatorModel):
    consumableResource: Optional[str] = None
    quantity: Optional[int] = None


class ConsumableResourceSummary(BaseValidatorModel):
    consumableResourceArn: str
    consumableResourceName: str
    totalQuantity: Optional[int] = None
    inUseQuantity: Optional[int] = None
    resourceType: Optional[str] = None


class EphemeralStorage(BaseValidatorModel):
    sizeInGiB: int


class FargatePlatformConfiguration(BaseValidatorModel):
    platformVersion: Optional[str] = None


class KeyValuePair(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None


class MountPoint(BaseValidatorModel):
    containerPath: Optional[str] = None
    readOnly: Optional[bool] = None
    sourceVolume: Optional[str] = None


class NetworkConfiguration(BaseValidatorModel):
    assignPublicIp: Optional[AssignPublicIpType] = None


class RepositoryCredentials(BaseValidatorModel):
    credentialsParameter: str


class ResourceRequirement(BaseValidatorModel):
    value: str
    type: ResourceTypeType


class RuntimePlatform(BaseValidatorModel):
    operatingSystemFamily: Optional[str] = None
    cpuArchitecture: Optional[str] = None


class Secret(BaseValidatorModel):
    name: str
    valueFrom: str


class Ulimit(BaseValidatorModel):
    hardLimit: int
    name: str
    softLimit: int


class ContainerSummary(BaseValidatorModel):
    exitCode: Optional[int] = None
    reason: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateConsumableResourceRequest(BaseValidatorModel):
    consumableResourceName: str
    totalQuantity: Optional[int] = None
    resourceType: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class JobStateTimeLimitAction(BaseValidatorModel):
    reason: str
    state: Literal['RUNNABLE']
    maxTimeSeconds: int
    action: Literal['CANCEL']


class DeleteComputeEnvironmentRequest(BaseValidatorModel):
    computeEnvironment: str


class DeleteConsumableResourceRequest(BaseValidatorModel):
    consumableResource: str


class DeleteJobQueueRequest(BaseValidatorModel):
    jobQueue: str


class DeleteSchedulingPolicyRequest(BaseValidatorModel):
    arn: str


class DeregisterJobDefinitionRequest(BaseValidatorModel):
    jobDefinition: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeComputeEnvironmentsRequest(BaseValidatorModel):
    computeEnvironments: Optional[List[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeConsumableResourceRequest(BaseValidatorModel):
    consumableResource: str


class DescribeJobDefinitionsRequest(BaseValidatorModel):
    jobDefinitions: Optional[List[str]] = None
    maxResults: Optional[int] = None
    jobDefinitionName: Optional[str] = None
    status: Optional[str] = None
    nextToken: Optional[str] = None


class DescribeJobQueuesRequest(BaseValidatorModel):
    jobQueues: Optional[List[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeJobsRequest(BaseValidatorModel):
    jobs: List[str]


class DescribeSchedulingPoliciesRequest(BaseValidatorModel):
    arns: List[str]


class DeviceOutput(BaseValidatorModel):
    hostPath: str
    containerPath: Optional[str] = None
    permissions: Optional[List[DeviceCgroupPermissionType]] = None


class Device(BaseValidatorModel):
    hostPath: str
    containerPath: Optional[str] = None
    permissions: Optional[List[DeviceCgroupPermissionType]] = None


class EFSAuthorizationConfig(BaseValidatorModel):
    accessPointId: Optional[str] = None
    iam: Optional[EFSAuthorizationConfigIAMType] = None


class EksAttemptContainerDetail(BaseValidatorModel):
    name: Optional[str] = None
    containerID: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None


class EksContainerEnvironmentVariable(BaseValidatorModel):
    name: str
    value: Optional[str] = None


class EksContainerResourceRequirementsOutput(BaseValidatorModel):
    limits: Optional[Dict[str, str]] = None
    requests: Optional[Dict[str, str]] = None


class EksContainerSecurityContext(BaseValidatorModel):
    runAsUser: Optional[int] = None
    runAsGroup: Optional[int] = None
    privileged: Optional[bool] = None
    allowPrivilegeEscalation: Optional[bool] = None
    readOnlyRootFilesystem: Optional[bool] = None
    runAsNonRoot: Optional[bool] = None


class EksContainerVolumeMount(BaseValidatorModel):
    name: Optional[str] = None
    mountPath: Optional[str] = None
    subPath: Optional[str] = None
    readOnly: Optional[bool] = None


class EksContainerResourceRequirements(BaseValidatorModel):
    limits: Optional[Dict[str, str]] = None
    requests: Optional[Dict[str, str]] = None


class EksEmptyDir(BaseValidatorModel):
    medium: Optional[str] = None
    sizeLimit: Optional[str] = None


class EksHostPath(BaseValidatorModel):
    path: Optional[str] = None


class EksMetadataOutput(BaseValidatorModel):
    labels: Optional[Dict[str, str]] = None
    annotations: Optional[Dict[str, str]] = None
    namespace: Optional[str] = None


class EksMetadata(BaseValidatorModel):
    labels: Optional[Dict[str, str]] = None
    annotations: Optional[Dict[str, str]] = None
    namespace: Optional[str] = None


class EksPersistentVolumeClaim(BaseValidatorModel):
    claimName: str
    readOnly: Optional[bool] = None


class ImagePullSecret(BaseValidatorModel):
    name: str


class EksSecret(BaseValidatorModel):
    secretName: str
    optional: Optional[bool] = None


class EvaluateOnExit(BaseValidatorModel):
    action: RetryActionType
    onStatusReason: Optional[str] = None
    onReason: Optional[str] = None
    onExitCode: Optional[str] = None


class ShareAttributes(BaseValidatorModel):
    shareIdentifier: str
    weightFactor: Optional[float] = None


class FrontOfQueueJobSummary(BaseValidatorModel):
    jobArn: Optional[str] = None
    earliestTimeAtPosition: Optional[int] = None


class GetJobQueueSnapshotRequest(BaseValidatorModel):
    jobQueue: str


class Host(BaseValidatorModel):
    sourcePath: Optional[str] = None


class JobTimeout(BaseValidatorModel):
    attemptDurationSeconds: Optional[int] = None


class JobDependency(BaseValidatorModel):
    jobId: Optional[str] = None
    type: Optional[ArrayJobDependencyType] = None


class NodeDetails(BaseValidatorModel):
    nodeIndex: Optional[int] = None
    isMainNode: Optional[bool] = None


class NodePropertiesSummary(BaseValidatorModel):
    isMainNode: Optional[bool] = None
    numNodes: Optional[int] = None
    nodeIndex: Optional[int] = None


class KeyValuesPair(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[List[str]] = None


class LaunchTemplateSpecificationOverrideOutput(BaseValidatorModel):
    launchTemplateId: Optional[str] = None
    launchTemplateName: Optional[str] = None
    version: Optional[str] = None
    targetInstanceTypes: Optional[List[str]] = None


class LaunchTemplateSpecificationOverride(BaseValidatorModel):
    launchTemplateId: Optional[str] = None
    launchTemplateName: Optional[str] = None
    version: Optional[str] = None
    targetInstanceTypes: Optional[List[str]] = None


class TmpfsOutput(BaseValidatorModel):
    containerPath: str
    size: int
    mountOptions: Optional[List[str]] = None


class Tmpfs(BaseValidatorModel):
    containerPath: str
    size: int
    mountOptions: Optional[List[str]] = None


class ListSchedulingPoliciesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SchedulingPolicyListingDetail(BaseValidatorModel):
    arn: str


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class TaskContainerDependency(BaseValidatorModel):
    containerName: Optional[str] = None
    condition: Optional[str] = None


class TerminateJobRequest(BaseValidatorModel):
    jobId: str
    reason: str


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateConsumableResourceRequest(BaseValidatorModel):
    consumableResource: str
    operation: Optional[str] = None
    quantity: Optional[int] = None
    clientToken: Optional[str] = None


class AttemptContainerDetail(BaseValidatorModel):
    containerInstanceArn: Optional[str] = None
    taskArn: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    logStreamName: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterface]] = None


class AttemptTaskContainerDetails(BaseValidatorModel):
    exitCode: Optional[int] = None
    name: Optional[str] = None
    reason: Optional[str] = None
    logStreamName: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterface]] = None


class ConsumableResourcePropertiesOutput(BaseValidatorModel):
    consumableResourceList: Optional[List[ConsumableResourceRequirement]] = None


class ConsumableResourceProperties(BaseValidatorModel):
    consumableResourceList: Optional[List[ConsumableResourceRequirement]] = None


class ContainerOverrides(BaseValidatorModel):
    vcpus: Optional[int] = None
    memory: Optional[int] = None
    command: Optional[List[str]] = None
    instanceType: Optional[str] = None
    environment: Optional[List[KeyValuePair]] = None
    resourceRequirements: Optional[List[ResourceRequirement]] = None


class TaskContainerOverrides(BaseValidatorModel):
    command: Optional[List[str]] = None
    environment: Optional[List[KeyValuePair]] = None
    name: Optional[str] = None
    resourceRequirements: Optional[List[ResourceRequirement]] = None


class LogConfigurationOutput(BaseValidatorModel):
    logDriver: LogDriverType
    options: Optional[Dict[str, str]] = None
    secretOptions: Optional[List[Secret]] = None


class LogConfiguration(BaseValidatorModel):
    logDriver: LogDriverType
    options: Optional[Dict[str, str]] = None
    secretOptions: Optional[List[Secret]] = None


class CreateComputeEnvironmentResponse(BaseValidatorModel):
    computeEnvironmentName: str
    computeEnvironmentArn: str
    ResponseMetadata: ResponseMetadata


class CreateConsumableResourceResponse(BaseValidatorModel):
    consumableResourceName: str
    consumableResourceArn: str
    ResponseMetadata: ResponseMetadata


class CreateJobQueueResponse(BaseValidatorModel):
    jobQueueName: str
    jobQueueArn: str
    ResponseMetadata: ResponseMetadata


class CreateSchedulingPolicyResponse(BaseValidatorModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadata


class DescribeConsumableResourceResponse(BaseValidatorModel):
    consumableResourceName: str
    consumableResourceArn: str
    totalQuantity: int
    inUseQuantity: int
    availableQuantity: int
    resourceType: str
    createdAt: int
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class ListConsumableResourcesResponse(BaseValidatorModel):
    consumableResources: List[ConsumableResourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class RegisterJobDefinitionResponse(BaseValidatorModel):
    jobDefinitionName: str
    jobDefinitionArn: str
    revision: int
    ResponseMetadata: ResponseMetadata


class SubmitJobResponse(BaseValidatorModel):
    jobArn: str
    jobName: str
    jobId: str
    ResponseMetadata: ResponseMetadata


class UpdateComputeEnvironmentResponse(BaseValidatorModel):
    computeEnvironmentName: str
    computeEnvironmentArn: str
    ResponseMetadata: ResponseMetadata


class UpdateConsumableResourceResponse(BaseValidatorModel):
    consumableResourceName: str
    consumableResourceArn: str
    totalQuantity: int
    ResponseMetadata: ResponseMetadata


class UpdateJobQueueResponse(BaseValidatorModel):
    jobQueueName: str
    jobQueueArn: str
    ResponseMetadata: ResponseMetadata


class CreateJobQueueRequest(BaseValidatorModel):
    jobQueueName: str
    priority: int
    computeEnvironmentOrder: List[ComputeEnvironmentOrder]
    state: Optional[JQStateType] = None
    schedulingPolicyArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    jobStateTimeLimitActions: Optional[List[JobStateTimeLimitAction]] = None


class JobQueueDetail(BaseValidatorModel):
    jobQueueName: str
    jobQueueArn: str
    state: JQStateType
    priority: int
    computeEnvironmentOrder: List[ComputeEnvironmentOrder]
    schedulingPolicyArn: Optional[str] = None
    status: Optional[JQStatusType] = None
    statusReason: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    jobStateTimeLimitActions: Optional[List[JobStateTimeLimitAction]] = None


class UpdateJobQueueRequest(BaseValidatorModel):
    jobQueue: str
    state: Optional[JQStateType] = None
    schedulingPolicyArn: Optional[str] = None
    priority: Optional[int] = None
    computeEnvironmentOrder: Optional[List[ComputeEnvironmentOrder]] = None
    jobStateTimeLimitActions: Optional[List[JobStateTimeLimitAction]] = None


class DescribeComputeEnvironmentsRequestPaginate(BaseValidatorModel):
    computeEnvironments: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeJobDefinitionsRequestPaginate(BaseValidatorModel):
    jobDefinitions: Optional[List[str]] = None
    jobDefinitionName: Optional[str] = None
    status: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeJobQueuesRequestPaginate(BaseValidatorModel):
    jobQueues: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSchedulingPoliciesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class EFSVolumeConfiguration(BaseValidatorModel):
    fileSystemId: str
    rootDirectory: Optional[str] = None
    transitEncryption: Optional[EFSTransitEncryptionType] = None
    transitEncryptionPort: Optional[int] = None
    authorizationConfig: Optional[EFSAuthorizationConfig] = None


class EksAttemptDetail(BaseValidatorModel):
    containers: Optional[List[EksAttemptContainerDetail]] = None
    initContainers: Optional[List[EksAttemptContainerDetail]] = None
    eksClusterArn: Optional[str] = None
    podName: Optional[str] = None
    podNamespace: Optional[str] = None
    nodeName: Optional[str] = None
    startedAt: Optional[int] = None
    stoppedAt: Optional[int] = None
    statusReason: Optional[str] = None


class EksContainerDetail(BaseValidatorModel):
    name: Optional[str] = None
    image: Optional[str] = None
    imagePullPolicy: Optional[str] = None
    command: Optional[List[str]] = None
    args: Optional[List[str]] = None
    env: Optional[List[EksContainerEnvironmentVariable]] = None
    resources: Optional[EksContainerResourceRequirementsOutput] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    volumeMounts: Optional[List[EksContainerVolumeMount]] = None
    securityContext: Optional[EksContainerSecurityContext] = None


class EksContainerOutput(BaseValidatorModel):
    image: str
    name: Optional[str] = None
    imagePullPolicy: Optional[str] = None
    command: Optional[List[str]] = None
    args: Optional[List[str]] = None
    env: Optional[List[EksContainerEnvironmentVariable]] = None
    resources: Optional[EksContainerResourceRequirementsOutput] = None
    volumeMounts: Optional[List[EksContainerVolumeMount]] = None
    securityContext: Optional[EksContainerSecurityContext] = None

EksContainerResourceRequirementsUnion = Union[EksContainerResourceRequirements, EksContainerResourceRequirementsOutput]


class EksContainer(BaseValidatorModel):
    image: str
    name: Optional[str] = None
    imagePullPolicy: Optional[str] = None
    command: Optional[List[str]] = None
    args: Optional[List[str]] = None
    env: Optional[List[EksContainerEnvironmentVariable]] = None
    resources: Optional[EksContainerResourceRequirements] = None
    volumeMounts: Optional[List[EksContainerVolumeMount]] = None
    securityContext: Optional[EksContainerSecurityContext] = None

EksMetadataUnion = Union[EksMetadata, EksMetadataOutput]


class EksVolume(BaseValidatorModel):
    name: str
    hostPath: Optional[EksHostPath] = None
    emptyDir: Optional[EksEmptyDir] = None
    secret: Optional[EksSecret] = None
    persistentVolumeClaim: Optional[EksPersistentVolumeClaim] = None


class RetryStrategyOutput(BaseValidatorModel):
    attempts: Optional[int] = None
    evaluateOnExit: Optional[List[EvaluateOnExit]] = None


class RetryStrategy(BaseValidatorModel):
    attempts: Optional[int] = None
    evaluateOnExit: Optional[List[EvaluateOnExit]] = None


class FairsharePolicyOutput(BaseValidatorModel):
    shareDecaySeconds: Optional[int] = None
    computeReservation: Optional[int] = None
    shareDistribution: Optional[List[ShareAttributes]] = None


class FairsharePolicy(BaseValidatorModel):
    shareDecaySeconds: Optional[int] = None
    computeReservation: Optional[int] = None
    shareDistribution: Optional[List[ShareAttributes]] = None


class FrontOfQueueDetail(BaseValidatorModel):
    jobs: Optional[List[FrontOfQueueJobSummary]] = None
    lastUpdatedAt: Optional[int] = None


class JobSummary(BaseValidatorModel):
    jobId: str
    jobName: str
    jobArn: Optional[str] = None
    createdAt: Optional[int] = None
    status: Optional[JobStatusType] = None
    statusReason: Optional[str] = None
    startedAt: Optional[int] = None
    stoppedAt: Optional[int] = None
    container: Optional[ContainerSummary] = None
    arrayProperties: Optional[ArrayPropertiesSummary] = None
    nodeProperties: Optional[NodePropertiesSummary] = None
    jobDefinition: Optional[str] = None


class ListConsumableResourcesRequestPaginate(BaseValidatorModel):
    filters: Optional[List[KeyValuesPair]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConsumableResourcesRequest(BaseValidatorModel):
    filters: Optional[List[KeyValuesPair]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobsByConsumableResourceRequestPaginate(BaseValidatorModel):
    consumableResource: str
    filters: Optional[List[KeyValuesPair]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobsByConsumableResourceRequest(BaseValidatorModel):
    consumableResource: str
    filters: Optional[List[KeyValuesPair]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListJobsRequestPaginate(BaseValidatorModel):
    jobQueue: Optional[str] = None
    arrayJobId: Optional[str] = None
    multiNodeJobId: Optional[str] = None
    jobStatus: Optional[JobStatusType] = None
    filters: Optional[List[KeyValuesPair]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListJobsRequest(BaseValidatorModel):
    jobQueue: Optional[str] = None
    arrayJobId: Optional[str] = None
    multiNodeJobId: Optional[str] = None
    jobStatus: Optional[JobStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filters: Optional[List[KeyValuesPair]] = None


class LaunchTemplateSpecificationOutput(BaseValidatorModel):
    launchTemplateId: Optional[str] = None
    launchTemplateName: Optional[str] = None
    version: Optional[str] = None
    overrides: Optional[List[LaunchTemplateSpecificationOverrideOutput]] = None

LaunchTemplateSpecificationOverrideUnion = Union[LaunchTemplateSpecificationOverride, LaunchTemplateSpecificationOverrideOutput]


class LinuxParametersOutput(BaseValidatorModel):
    devices: Optional[List[DeviceOutput]] = None
    initProcessEnabled: Optional[bool] = None
    sharedMemorySize: Optional[int] = None
    tmpfs: Optional[List[TmpfsOutput]] = None
    maxSwap: Optional[int] = None
    swappiness: Optional[int] = None


class LinuxParameters(BaseValidatorModel):
    devices: Optional[List[Device]] = None
    initProcessEnabled: Optional[bool] = None
    sharedMemorySize: Optional[int] = None
    tmpfs: Optional[List[Tmpfs]] = None
    maxSwap: Optional[int] = None
    swappiness: Optional[int] = None


class ListSchedulingPoliciesResponse(BaseValidatorModel):
    schedulingPolicies: List[SchedulingPolicyListingDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AttemptEcsTaskDetails(BaseValidatorModel):
    containerInstanceArn: Optional[str] = None
    taskArn: Optional[str] = None
    containers: Optional[List[AttemptTaskContainerDetails]] = None


class ListJobsByConsumableResourceSummary(BaseValidatorModel):
    jobArn: str
    jobQueueArn: str
    jobName: str
    jobStatus: str
    quantity: int
    createdAt: int
    consumableResourceProperties: ConsumableResourcePropertiesOutput
    jobDefinitionArn: Optional[str] = None
    shareIdentifier: Optional[str] = None
    statusReason: Optional[str] = None
    startedAt: Optional[int] = None

ConsumableResourcePropertiesUnion = Union[ConsumableResourceProperties, ConsumableResourcePropertiesOutput]


class TaskPropertiesOverride(BaseValidatorModel):
    containers: Optional[List[TaskContainerOverrides]] = None


class DescribeJobQueuesResponse(BaseValidatorModel):
    jobQueues: List[JobQueueDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Volume(BaseValidatorModel):
    host: Optional[Host] = None
    name: Optional[str] = None
    efsVolumeConfiguration: Optional[EFSVolumeConfiguration] = None


class EksContainerOverride(BaseValidatorModel):
    name: Optional[str] = None
    image: Optional[str] = None
    command: Optional[List[str]] = None
    args: Optional[List[str]] = None
    env: Optional[List[EksContainerEnvironmentVariable]] = None
    resources: Optional[EksContainerResourceRequirementsUnion] = None


class EksPodPropertiesDetail(BaseValidatorModel):
    serviceAccountName: Optional[str] = None
    hostNetwork: Optional[bool] = None
    dnsPolicy: Optional[str] = None
    imagePullSecrets: Optional[List[ImagePullSecret]] = None
    containers: Optional[List[EksContainerDetail]] = None
    initContainers: Optional[List[EksContainerDetail]] = None
    volumes: Optional[List[EksVolume]] = None
    podName: Optional[str] = None
    nodeName: Optional[str] = None
    metadata: Optional[EksMetadataOutput] = None
    shareProcessNamespace: Optional[bool] = None


class EksPodPropertiesOutput(BaseValidatorModel):
    serviceAccountName: Optional[str] = None
    hostNetwork: Optional[bool] = None
    dnsPolicy: Optional[str] = None
    imagePullSecrets: Optional[List[ImagePullSecret]] = None
    containers: Optional[List[EksContainerOutput]] = None
    initContainers: Optional[List[EksContainerOutput]] = None
    volumes: Optional[List[EksVolume]] = None
    metadata: Optional[EksMetadataOutput] = None
    shareProcessNamespace: Optional[bool] = None


class EksPodProperties(BaseValidatorModel):
    serviceAccountName: Optional[str] = None
    hostNetwork: Optional[bool] = None
    dnsPolicy: Optional[str] = None
    imagePullSecrets: Optional[List[ImagePullSecret]] = None
    containers: Optional[List[EksContainer]] = None
    initContainers: Optional[List[EksContainer]] = None
    volumes: Optional[List[EksVolume]] = None
    metadata: Optional[EksMetadata] = None
    shareProcessNamespace: Optional[bool] = None

RetryStrategyUnion = Union[RetryStrategy, RetryStrategyOutput]


class SchedulingPolicyDetail(BaseValidatorModel):
    name: str
    arn: str
    fairsharePolicy: Optional[FairsharePolicyOutput] = None
    tags: Optional[Dict[str, str]] = None

FairsharePolicyUnion = Union[FairsharePolicy, FairsharePolicyOutput]


class GetJobQueueSnapshotResponse(BaseValidatorModel):
    frontOfQueue: FrontOfQueueDetail
    ResponseMetadata: ResponseMetadata


class ListJobsResponse(BaseValidatorModel):
    jobSummaryList: List[JobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ComputeResourceOutput(BaseValidatorModel):
    type: CRTypeType
    maxvCpus: int
    subnets: List[str]
    allocationStrategy: Optional[CRAllocationStrategyType] = None
    minvCpus: Optional[int] = None
    desiredvCpus: Optional[int] = None
    instanceTypes: Optional[List[str]] = None
    imageId: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    ec2KeyPair: Optional[str] = None
    instanceRole: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    placementGroup: Optional[str] = None
    bidPercentage: Optional[int] = None
    spotIamFleetRole: Optional[str] = None
    launchTemplate: Optional[LaunchTemplateSpecificationOutput] = None
    ec2Configuration: Optional[List[Ec2Configuration]] = None


class LaunchTemplateSpecification(BaseValidatorModel):
    launchTemplateId: Optional[str] = None
    launchTemplateName: Optional[str] = None
    version: Optional[str] = None
    overrides: Optional[List[LaunchTemplateSpecificationOverrideUnion]] = None


class TaskContainerDetails(BaseValidatorModel):
    command: Optional[List[str]] = None
    dependsOn: Optional[List[TaskContainerDependency]] = None
    environment: Optional[List[KeyValuePair]] = None
    essential: Optional[bool] = None
    image: Optional[str] = None
    linuxParameters: Optional[LinuxParametersOutput] = None
    logConfiguration: Optional[LogConfigurationOutput] = None
    mountPoints: Optional[List[MountPoint]] = None
    name: Optional[str] = None
    privileged: Optional[bool] = None
    readonlyRootFilesystem: Optional[bool] = None
    repositoryCredentials: Optional[RepositoryCredentials] = None
    resourceRequirements: Optional[List[ResourceRequirement]] = None
    secrets: Optional[List[Secret]] = None
    ulimits: Optional[List[Ulimit]] = None
    user: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    logStreamName: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterface]] = None


class TaskContainerPropertiesOutput(BaseValidatorModel):
    image: str
    command: Optional[List[str]] = None
    dependsOn: Optional[List[TaskContainerDependency]] = None
    environment: Optional[List[KeyValuePair]] = None
    essential: Optional[bool] = None
    linuxParameters: Optional[LinuxParametersOutput] = None
    logConfiguration: Optional[LogConfigurationOutput] = None
    mountPoints: Optional[List[MountPoint]] = None
    name: Optional[str] = None
    privileged: Optional[bool] = None
    readonlyRootFilesystem: Optional[bool] = None
    repositoryCredentials: Optional[RepositoryCredentials] = None
    resourceRequirements: Optional[List[ResourceRequirement]] = None
    secrets: Optional[List[Secret]] = None
    ulimits: Optional[List[Ulimit]] = None
    user: Optional[str] = None


class TaskContainerProperties(BaseValidatorModel):
    image: str
    command: Optional[List[str]] = None
    dependsOn: Optional[List[TaskContainerDependency]] = None
    environment: Optional[List[KeyValuePair]] = None
    essential: Optional[bool] = None
    linuxParameters: Optional[LinuxParameters] = None
    logConfiguration: Optional[LogConfiguration] = None
    mountPoints: Optional[List[MountPoint]] = None
    name: Optional[str] = None
    privileged: Optional[bool] = None
    readonlyRootFilesystem: Optional[bool] = None
    repositoryCredentials: Optional[RepositoryCredentials] = None
    resourceRequirements: Optional[List[ResourceRequirement]] = None
    secrets: Optional[List[Secret]] = None
    ulimits: Optional[List[Ulimit]] = None
    user: Optional[str] = None


class AttemptDetail(BaseValidatorModel):
    container: Optional[AttemptContainerDetail] = None
    startedAt: Optional[int] = None
    stoppedAt: Optional[int] = None
    statusReason: Optional[str] = None
    taskProperties: Optional[List[AttemptEcsTaskDetails]] = None


class ListJobsByConsumableResourceResponse(BaseValidatorModel):
    jobs: List[ListJobsByConsumableResourceSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EcsPropertiesOverride(BaseValidatorModel):
    taskProperties: Optional[List[TaskPropertiesOverride]] = None


class ContainerDetail(BaseValidatorModel):
    image: Optional[str] = None
    vcpus: Optional[int] = None
    memory: Optional[int] = None
    command: Optional[List[str]] = None
    jobRoleArn: Optional[str] = None
    executionRoleArn: Optional[str] = None
    volumes: Optional[List[Volume]] = None
    environment: Optional[List[KeyValuePair]] = None
    mountPoints: Optional[List[MountPoint]] = None
    readonlyRootFilesystem: Optional[bool] = None
    ulimits: Optional[List[Ulimit]] = None
    privileged: Optional[bool] = None
    user: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    containerInstanceArn: Optional[str] = None
    taskArn: Optional[str] = None
    logStreamName: Optional[str] = None
    instanceType: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterface]] = None
    resourceRequirements: Optional[List[ResourceRequirement]] = None
    linuxParameters: Optional[LinuxParametersOutput] = None
    logConfiguration: Optional[LogConfigurationOutput] = None
    secrets: Optional[List[Secret]] = None
    networkConfiguration: Optional[NetworkConfiguration] = None
    fargatePlatformConfiguration: Optional[FargatePlatformConfiguration] = None
    ephemeralStorage: Optional[EphemeralStorage] = None
    runtimePlatform: Optional[RuntimePlatform] = None
    repositoryCredentials: Optional[RepositoryCredentials] = None


class ContainerPropertiesOutput(BaseValidatorModel):
    image: Optional[str] = None
    vcpus: Optional[int] = None
    memory: Optional[int] = None
    command: Optional[List[str]] = None
    jobRoleArn: Optional[str] = None
    executionRoleArn: Optional[str] = None
    volumes: Optional[List[Volume]] = None
    environment: Optional[List[KeyValuePair]] = None
    mountPoints: Optional[List[MountPoint]] = None
    readonlyRootFilesystem: Optional[bool] = None
    privileged: Optional[bool] = None
    ulimits: Optional[List[Ulimit]] = None
    user: Optional[str] = None
    instanceType: Optional[str] = None
    resourceRequirements: Optional[List[ResourceRequirement]] = None
    linuxParameters: Optional[LinuxParametersOutput] = None
    logConfiguration: Optional[LogConfigurationOutput] = None
    secrets: Optional[List[Secret]] = None
    networkConfiguration: Optional[NetworkConfiguration] = None
    fargatePlatformConfiguration: Optional[FargatePlatformConfiguration] = None
    ephemeralStorage: Optional[EphemeralStorage] = None
    runtimePlatform: Optional[RuntimePlatform] = None
    repositoryCredentials: Optional[RepositoryCredentials] = None


class ContainerProperties(BaseValidatorModel):
    image: Optional[str] = None
    vcpus: Optional[int] = None
    memory: Optional[int] = None
    command: Optional[List[str]] = None
    jobRoleArn: Optional[str] = None
    executionRoleArn: Optional[str] = None
    volumes: Optional[List[Volume]] = None
    environment: Optional[List[KeyValuePair]] = None
    mountPoints: Optional[List[MountPoint]] = None
    readonlyRootFilesystem: Optional[bool] = None
    privileged: Optional[bool] = None
    ulimits: Optional[List[Ulimit]] = None
    user: Optional[str] = None
    instanceType: Optional[str] = None
    resourceRequirements: Optional[List[ResourceRequirement]] = None
    linuxParameters: Optional[LinuxParameters] = None
    logConfiguration: Optional[LogConfiguration] = None
    secrets: Optional[List[Secret]] = None
    networkConfiguration: Optional[NetworkConfiguration] = None
    fargatePlatformConfiguration: Optional[FargatePlatformConfiguration] = None
    ephemeralStorage: Optional[EphemeralStorage] = None
    runtimePlatform: Optional[RuntimePlatform] = None
    repositoryCredentials: Optional[RepositoryCredentials] = None


class EksPodPropertiesOverride(BaseValidatorModel):
    containers: Optional[List[EksContainerOverride]] = None
    initContainers: Optional[List[EksContainerOverride]] = None
    metadata: Optional[EksMetadataUnion] = None


class EksPropertiesDetail(BaseValidatorModel):
    podProperties: Optional[EksPodPropertiesDetail] = None


class EksPropertiesOutput(BaseValidatorModel):
    podProperties: Optional[EksPodPropertiesOutput] = None


class EksProperties(BaseValidatorModel):
    podProperties: Optional[EksPodProperties] = None


class DescribeSchedulingPoliciesResponse(BaseValidatorModel):
    schedulingPolicies: List[SchedulingPolicyDetail]
    ResponseMetadata: ResponseMetadata


class CreateSchedulingPolicyRequest(BaseValidatorModel):
    name: str
    fairsharePolicy: Optional[FairsharePolicyUnion] = None
    tags: Optional[Dict[str, str]] = None


class UpdateSchedulingPolicyRequest(BaseValidatorModel):
    arn: str
    fairsharePolicy: Optional[FairsharePolicyUnion] = None


class ComputeEnvironmentDetail(BaseValidatorModel):
    computeEnvironmentName: str
    computeEnvironmentArn: str
    unmanagedvCpus: Optional[int] = None
    ecsClusterArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[CETypeType] = None
    state: Optional[CEStateType] = None
    status: Optional[CEStatusType] = None
    statusReason: Optional[str] = None
    computeResources: Optional[ComputeResourceOutput] = None
    serviceRole: Optional[str] = None
    updatePolicy: Optional[UpdatePolicy] = None
    eksConfiguration: Optional[EksConfiguration] = None
    containerOrchestrationType: Optional[OrchestrationTypeType] = None
    uuid: Optional[str] = None
    context: Optional[str] = None


class ComputeResource(BaseValidatorModel):
    type: CRTypeType
    maxvCpus: int
    subnets: List[str]
    allocationStrategy: Optional[CRAllocationStrategyType] = None
    minvCpus: Optional[int] = None
    desiredvCpus: Optional[int] = None
    instanceTypes: Optional[List[str]] = None
    imageId: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    ec2KeyPair: Optional[str] = None
    instanceRole: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    placementGroup: Optional[str] = None
    bidPercentage: Optional[int] = None
    spotIamFleetRole: Optional[str] = None
    launchTemplate: Optional[LaunchTemplateSpecification] = None
    ec2Configuration: Optional[List[Ec2Configuration]] = None

LaunchTemplateSpecificationUnion = Union[LaunchTemplateSpecification, LaunchTemplateSpecificationOutput]


class EcsTaskDetails(BaseValidatorModel):
    containers: Optional[List[TaskContainerDetails]] = None
    containerInstanceArn: Optional[str] = None
    taskArn: Optional[str] = None
    ephemeralStorage: Optional[EphemeralStorage] = None
    executionRoleArn: Optional[str] = None
    platformVersion: Optional[str] = None
    ipcMode: Optional[str] = None
    taskRoleArn: Optional[str] = None
    pidMode: Optional[str] = None
    networkConfiguration: Optional[NetworkConfiguration] = None
    runtimePlatform: Optional[RuntimePlatform] = None
    volumes: Optional[List[Volume]] = None


class EcsTaskPropertiesOutput(BaseValidatorModel):
    containers: List[TaskContainerPropertiesOutput]
    ephemeralStorage: Optional[EphemeralStorage] = None
    executionRoleArn: Optional[str] = None
    platformVersion: Optional[str] = None
    ipcMode: Optional[str] = None
    taskRoleArn: Optional[str] = None
    pidMode: Optional[str] = None
    networkConfiguration: Optional[NetworkConfiguration] = None
    runtimePlatform: Optional[RuntimePlatform] = None
    volumes: Optional[List[Volume]] = None


class EcsTaskProperties(BaseValidatorModel):
    containers: List[TaskContainerProperties]
    ephemeralStorage: Optional[EphemeralStorage] = None
    executionRoleArn: Optional[str] = None
    platformVersion: Optional[str] = None
    ipcMode: Optional[str] = None
    taskRoleArn: Optional[str] = None
    pidMode: Optional[str] = None
    networkConfiguration: Optional[NetworkConfiguration] = None
    runtimePlatform: Optional[RuntimePlatform] = None
    volumes: Optional[List[Volume]] = None

ContainerPropertiesUnion = Union[ContainerProperties, ContainerPropertiesOutput]


class EksPropertiesOverride(BaseValidatorModel):
    podProperties: Optional[EksPodPropertiesOverride] = None

EksPropertiesUnion = Union[EksProperties, EksPropertiesOutput]


class DescribeComputeEnvironmentsResponse(BaseValidatorModel):
    computeEnvironments: List[ComputeEnvironmentDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

ComputeResourceUnion = Union[ComputeResource, ComputeResourceOutput]


class ComputeResourceUpdate(BaseValidatorModel):
    minvCpus: Optional[int] = None
    maxvCpus: Optional[int] = None
    desiredvCpus: Optional[int] = None
    subnets: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    allocationStrategy: Optional[CRUpdateAllocationStrategyType] = None
    instanceTypes: Optional[List[str]] = None
    ec2KeyPair: Optional[str] = None
    instanceRole: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    placementGroup: Optional[str] = None
    bidPercentage: Optional[int] = None
    launchTemplate: Optional[LaunchTemplateSpecificationUnion] = None
    ec2Configuration: Optional[List[Ec2Configuration]] = None
    updateToLatestImageVersion: Optional[bool] = None
    type: Optional[CRTypeType] = None
    imageId: Optional[str] = None


class EcsPropertiesDetail(BaseValidatorModel):
    taskProperties: Optional[List[EcsTaskDetails]] = None


class EcsPropertiesOutput(BaseValidatorModel):
    taskProperties: List[EcsTaskPropertiesOutput]


class EcsProperties(BaseValidatorModel):
    taskProperties: List[EcsTaskProperties]


class NodePropertyOverride(BaseValidatorModel):
    targetNodes: str
    containerOverrides: Optional[ContainerOverrides] = None
    ecsPropertiesOverride: Optional[EcsPropertiesOverride] = None
    instanceTypes: Optional[List[str]] = None
    eksPropertiesOverride: Optional[EksPropertiesOverride] = None
    consumableResourcePropertiesOverride: Optional[ConsumableResourcePropertiesUnion] = None


class CreateComputeEnvironmentRequest(BaseValidatorModel):
    computeEnvironmentName: str
    type: CETypeType
    state: Optional[CEStateType] = None
    unmanagedvCpus: Optional[int] = None
    computeResources: Optional[ComputeResourceUnion] = None
    serviceRole: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    eksConfiguration: Optional[EksConfiguration] = None
    context: Optional[str] = None


class UpdateComputeEnvironmentRequest(BaseValidatorModel):
    computeEnvironment: str
    state: Optional[CEStateType] = None
    unmanagedvCpus: Optional[int] = None
    computeResources: Optional[ComputeResourceUpdate] = None
    serviceRole: Optional[str] = None
    updatePolicy: Optional[UpdatePolicy] = None
    context: Optional[str] = None


class NodeRangePropertyOutput(BaseValidatorModel):
    targetNodes: str
    container: Optional[ContainerPropertiesOutput] = None
    instanceTypes: Optional[List[str]] = None
    ecsProperties: Optional[EcsPropertiesOutput] = None
    eksProperties: Optional[EksPropertiesOutput] = None
    consumableResourceProperties: Optional[ConsumableResourcePropertiesOutput] = None

EcsPropertiesUnion = Union[EcsProperties, EcsPropertiesOutput]


class NodeRangeProperty(BaseValidatorModel):
    targetNodes: str
    container: Optional[ContainerProperties] = None
    instanceTypes: Optional[List[str]] = None
    ecsProperties: Optional[EcsProperties] = None
    eksProperties: Optional[EksProperties] = None
    consumableResourceProperties: Optional[ConsumableResourceProperties] = None


class NodeOverrides(BaseValidatorModel):
    numNodes: Optional[int] = None
    nodePropertyOverrides: Optional[List[NodePropertyOverride]] = None


class NodePropertiesOutput(BaseValidatorModel):
    numNodes: int
    mainNode: int
    nodeRangeProperties: List[NodeRangePropertyOutput]


class NodeProperties(BaseValidatorModel):
    numNodes: int
    mainNode: int
    nodeRangeProperties: List[NodeRangeProperty]


class SubmitJobRequest(BaseValidatorModel):
    jobName: str
    jobQueue: str
    jobDefinition: str
    shareIdentifier: Optional[str] = None
    schedulingPriorityOverride: Optional[int] = None
    arrayProperties: Optional[ArrayProperties] = None
    dependsOn: Optional[List[JobDependency]] = None
    parameters: Optional[Dict[str, str]] = None
    containerOverrides: Optional[ContainerOverrides] = None
    nodeOverrides: Optional[NodeOverrides] = None
    retryStrategy: Optional[RetryStrategyUnion] = None
    propagateTags: Optional[bool] = None
    timeout: Optional[JobTimeout] = None
    tags: Optional[Dict[str, str]] = None
    eksPropertiesOverride: Optional[EksPropertiesOverride] = None
    ecsPropertiesOverride: Optional[EcsPropertiesOverride] = None
    consumableResourcePropertiesOverride: Optional[ConsumableResourcePropertiesUnion] = None


class JobDefinition(BaseValidatorModel):
    jobDefinitionName: str
    jobDefinitionArn: str
    revision: int
    type: str
    status: Optional[str] = None
    schedulingPriority: Optional[int] = None
    parameters: Optional[Dict[str, str]] = None
    retryStrategy: Optional[RetryStrategyOutput] = None
    containerProperties: Optional[ContainerPropertiesOutput] = None
    timeout: Optional[JobTimeout] = None
    nodeProperties: Optional[NodePropertiesOutput] = None
    tags: Optional[Dict[str, str]] = None
    propagateTags: Optional[bool] = None
    platformCapabilities: Optional[List[PlatformCapabilityType]] = None
    ecsProperties: Optional[EcsPropertiesOutput] = None
    eksProperties: Optional[EksPropertiesOutput] = None
    containerOrchestrationType: Optional[OrchestrationTypeType] = None
    consumableResourceProperties: Optional[ConsumableResourcePropertiesOutput] = None


class JobDetail(BaseValidatorModel):
    jobName: str
    jobId: str
    jobQueue: str
    status: JobStatusType
    startedAt: int
    jobDefinition: str
    jobArn: Optional[str] = None
    shareIdentifier: Optional[str] = None
    schedulingPriority: Optional[int] = None
    attempts: Optional[List[AttemptDetail]] = None
    statusReason: Optional[str] = None
    createdAt: Optional[int] = None
    retryStrategy: Optional[RetryStrategyOutput] = None
    stoppedAt: Optional[int] = None
    dependsOn: Optional[List[JobDependency]] = None
    parameters: Optional[Dict[str, str]] = None
    container: Optional[ContainerDetail] = None
    nodeDetails: Optional[NodeDetails] = None
    nodeProperties: Optional[NodePropertiesOutput] = None
    arrayProperties: Optional[ArrayPropertiesDetail] = None
    timeout: Optional[JobTimeout] = None
    tags: Optional[Dict[str, str]] = None
    propagateTags: Optional[bool] = None
    platformCapabilities: Optional[List[PlatformCapabilityType]] = None
    eksProperties: Optional[EksPropertiesDetail] = None
    eksAttempts: Optional[List[EksAttemptDetail]] = None
    ecsProperties: Optional[EcsPropertiesDetail] = None
    isCancelled: Optional[bool] = None
    isTerminated: Optional[bool] = None
    consumableResourceProperties: Optional[ConsumableResourcePropertiesOutput] = None

NodePropertiesUnion = Union[NodeProperties, NodePropertiesOutput]


class DescribeJobDefinitionsResponse(BaseValidatorModel):
    jobDefinitions: List[JobDefinition]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeJobsResponse(BaseValidatorModel):
    jobs: List[JobDetail]
    ResponseMetadata: ResponseMetadata


class RegisterJobDefinitionRequest(BaseValidatorModel):
    jobDefinitionName: str
    type: JobDefinitionTypeType
    parameters: Optional[Dict[str, str]] = None
    schedulingPriority: Optional[int] = None
    containerProperties: Optional[ContainerPropertiesUnion] = None
    nodeProperties: Optional[NodePropertiesUnion] = None
    retryStrategy: Optional[RetryStrategyUnion] = None
    propagateTags: Optional[bool] = None
    timeout: Optional[JobTimeout] = None
    tags: Optional[Dict[str, str]] = None
    platformCapabilities: Optional[List[PlatformCapabilityType]] = None
    eksProperties: Optional[EksPropertiesUnion] = None
    ecsProperties: Optional[EcsPropertiesUnion] = None
    consumableResourceProperties: Optional[ConsumableResourcePropertiesUnion] = None