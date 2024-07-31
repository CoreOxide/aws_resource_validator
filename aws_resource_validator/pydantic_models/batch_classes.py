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
from aws_resource_validator.pydantic_models.batch_constants import *

class ArrayPropertiesDetailTypeDef(BaseModel):
    statusSummary: Optional[Dict[str, int]] = None
    size: Optional[int] = None
    index: Optional[int] = None

class ArrayPropertiesSummaryTypeDef(BaseModel):
    size: Optional[int] = None
    index: Optional[int] = None

class ArrayPropertiesTypeDef(BaseModel):
    size: Optional[int] = None

class NetworkInterfaceTypeDef(BaseModel):
    attachmentId: Optional[str] = None
    ipv6Address: Optional[str] = None
    privateIpv4Address: Optional[str] = None

class CancelJobRequestRequestTypeDef(BaseModel):
    jobId: str
    reason: str

class EksConfigurationTypeDef(BaseModel):
    eksClusterArn: str
    kubernetesNamespace: str

class UpdatePolicyTypeDef(BaseModel):
    terminateJobsOnUpdate: Optional[bool] = None
    jobExecutionTimeoutMinutes: Optional[int] = None

class ComputeEnvironmentOrderTypeDef(BaseModel):
    order: int
    computeEnvironment: str

class Ec2ConfigurationTypeDef(BaseModel):
    imageType: str
    imageIdOverride: Optional[str] = None
    imageKubernetesVersion: Optional[str] = None

class LaunchTemplateSpecificationTypeDef(BaseModel):
    launchTemplateId: Optional[str] = None
    launchTemplateName: Optional[str] = None
    version: Optional[str] = None

class EphemeralStorageTypeDef(BaseModel):
    sizeInGiB: int

class FargatePlatformConfigurationTypeDef(BaseModel):
    platformVersion: Optional[str] = None

class KeyValuePairTypeDef(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class MountPointTypeDef(BaseModel):
    containerPath: Optional[str] = None
    readOnly: Optional[bool] = None
    sourceVolume: Optional[str] = None

class NetworkConfigurationTypeDef(BaseModel):
    assignPublicIp: Optional[AssignPublicIpType] = None

class RepositoryCredentialsTypeDef(BaseModel):
    credentialsParameter: str

class ResourceRequirementTypeDef(BaseModel):
    value: str
    type: ResourceTypeType

class RuntimePlatformTypeDef(BaseModel):
    operatingSystemFamily: Optional[str] = None
    cpuArchitecture: Optional[str] = None

class SecretTypeDef(BaseModel):
    name: str
    valueFrom: str

class UlimitTypeDef(BaseModel):
    hardLimit: int
    name: str
    softLimit: int

class ContainerSummaryTypeDef(BaseModel):
    exitCode: Optional[int] = None
    reason: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class JobStateTimeLimitActionTypeDef(BaseModel):
    reason: str
    state: Literal["RUNNABLE"]
    maxTimeSeconds: int
    action: Literal["CANCEL"]

class DeleteComputeEnvironmentRequestRequestTypeDef(BaseModel):
    computeEnvironment: str

class DeleteJobQueueRequestRequestTypeDef(BaseModel):
    jobQueue: str

class DeleteSchedulingPolicyRequestRequestTypeDef(BaseModel):
    arn: str

class DeregisterJobDefinitionRequestRequestTypeDef(BaseModel):
    jobDefinition: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeComputeEnvironmentsRequestRequestTypeDef(BaseModel):
    computeEnvironments: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeJobDefinitionsRequestRequestTypeDef(BaseModel):
    jobDefinitions: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    jobDefinitionName: Optional[str] = None
    status: Optional[str] = None
    nextToken: Optional[str] = None

class DescribeJobQueuesRequestRequestTypeDef(BaseModel):
    jobQueues: Optional[Sequence[str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeJobsRequestRequestTypeDef(BaseModel):
    jobs: Sequence[str]

class DescribeSchedulingPoliciesRequestRequestTypeDef(BaseModel):
    arns: Sequence[str]

class DeviceExtraOutputTypeDef(BaseModel):
    hostPath: str
    containerPath: Optional[str] = None
    permissions: Optional[List[DeviceCgroupPermissionType]] = None

class DeviceOutputTypeDef(BaseModel):
    hostPath: str
    containerPath: Optional[str] = None
    permissions: Optional[List[DeviceCgroupPermissionType]] = None

class DeviceTypeDef(BaseModel):
    hostPath: str
    containerPath: Optional[str] = None
    permissions: Optional[Sequence[DeviceCgroupPermissionType]] = None

class EFSAuthorizationConfigTypeDef(BaseModel):
    accessPointId: Optional[str] = None
    iam: Optional[EFSAuthorizationConfigIAMType] = None

class EksAttemptContainerDetailTypeDef(BaseModel):
    name: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None

class EksContainerEnvironmentVariableTypeDef(BaseModel):
    name: str
    value: Optional[str] = None

class EksContainerResourceRequirementsOutputTypeDef(BaseModel):
    limits: Optional[Dict[str, str]] = None
    requests: Optional[Dict[str, str]] = None

class EksContainerSecurityContextTypeDef(BaseModel):
    runAsUser: Optional[int] = None
    runAsGroup: Optional[int] = None
    privileged: Optional[bool] = None
    allowPrivilegeEscalation: Optional[bool] = None
    readOnlyRootFilesystem: Optional[bool] = None
    runAsNonRoot: Optional[bool] = None

class EksContainerVolumeMountTypeDef(BaseModel):
    name: Optional[str] = None
    mountPath: Optional[str] = None
    readOnly: Optional[bool] = None

class EksContainerResourceRequirementsExtraOutputTypeDef(BaseModel):
    limits: Optional[Dict[str, str]] = None
    requests: Optional[Dict[str, str]] = None

class EksContainerResourceRequirementsTypeDef(BaseModel):
    limits: Optional[Mapping[str, str]] = None
    requests: Optional[Mapping[str, str]] = None

class EksEmptyDirTypeDef(BaseModel):
    medium: Optional[str] = None
    sizeLimit: Optional[str] = None

class EksHostPathTypeDef(BaseModel):
    path: Optional[str] = None

class EksMetadataExtraOutputTypeDef(BaseModel):
    labels: Optional[Dict[str, str]] = None

class EksMetadataOutputTypeDef(BaseModel):
    labels: Optional[Dict[str, str]] = None

class EksMetadataTypeDef(BaseModel):
    labels: Optional[Mapping[str, str]] = None

class ImagePullSecretTypeDef(BaseModel):
    name: str

class EksSecretTypeDef(BaseModel):
    secretName: str
    optional: Optional[bool] = None

class EvaluateOnExitTypeDef(BaseModel):
    action: RetryActionType
    onStatusReason: Optional[str] = None
    onReason: Optional[str] = None
    onExitCode: Optional[str] = None

class ShareAttributesTypeDef(BaseModel):
    shareIdentifier: str
    weightFactor: Optional[float] = None

class FrontOfQueueJobSummaryTypeDef(BaseModel):
    jobArn: Optional[str] = None
    earliestTimeAtPosition: Optional[int] = None

class GetJobQueueSnapshotRequestRequestTypeDef(BaseModel):
    jobQueue: str

class HostTypeDef(BaseModel):
    sourcePath: Optional[str] = None

class JobTimeoutTypeDef(BaseModel):
    attemptDurationSeconds: Optional[int] = None

class JobDependencyTypeDef(BaseModel):
    jobId: Optional[str] = None
    type: Optional[ArrayJobDependencyType] = None

class NodeDetailsTypeDef(BaseModel):
    nodeIndex: Optional[int] = None
    isMainNode: Optional[bool] = None

class NodePropertiesSummaryTypeDef(BaseModel):
    isMainNode: Optional[bool] = None
    numNodes: Optional[int] = None
    nodeIndex: Optional[int] = None

class KeyValuesPairTypeDef(BaseModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None

class TmpfsExtraOutputTypeDef(BaseModel):
    containerPath: str
    size: int
    mountOptions: Optional[List[str]] = None

class TmpfsOutputTypeDef(BaseModel):
    containerPath: str
    size: int
    mountOptions: Optional[List[str]] = None

class TmpfsTypeDef(BaseModel):
    containerPath: str
    size: int
    mountOptions: Optional[Sequence[str]] = None

class ListSchedulingPoliciesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SchedulingPolicyListingDetailTypeDef(BaseModel):
    arn: str

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TaskContainerDependencyTypeDef(BaseModel):
    containerName: Optional[str] = None
    condition: Optional[str] = None

class TerminateJobRequestRequestTypeDef(BaseModel):
    jobId: str
    reason: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class AttemptContainerDetailTypeDef(BaseModel):
    containerInstanceArn: Optional[str] = None
    taskArn: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    logStreamName: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None

class AttemptTaskContainerDetailsTypeDef(BaseModel):
    exitCode: Optional[int] = None
    name: Optional[str] = None
    reason: Optional[str] = None
    logStreamName: Optional[str] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None

class ComputeResourceExtraOutputTypeDef(BaseModel):
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
    launchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    ec2Configuration: Optional[List[Ec2ConfigurationTypeDef]] = None

class ComputeResourceOutputTypeDef(BaseModel):
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
    launchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    ec2Configuration: Optional[List[Ec2ConfigurationTypeDef]] = None

class ComputeResourceTypeDef(BaseModel):
    type: CRTypeType
    maxvCpus: int
    subnets: Sequence[str]
    allocationStrategy: Optional[CRAllocationStrategyType] = None
    minvCpus: Optional[int] = None
    desiredvCpus: Optional[int] = None
    instanceTypes: Optional[Sequence[str]] = None
    imageId: Optional[str] = None
    securityGroupIds: Optional[Sequence[str]] = None
    ec2KeyPair: Optional[str] = None
    instanceRole: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    placementGroup: Optional[str] = None
    bidPercentage: Optional[int] = None
    spotIamFleetRole: Optional[str] = None
    launchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    ec2Configuration: Optional[Sequence[Ec2ConfigurationTypeDef]] = None

class ComputeResourceUpdateTypeDef(BaseModel):
    minvCpus: Optional[int] = None
    maxvCpus: Optional[int] = None
    desiredvCpus: Optional[int] = None
    subnets: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None
    allocationStrategy: Optional[CRUpdateAllocationStrategyType] = None
    instanceTypes: Optional[Sequence[str]] = None
    ec2KeyPair: Optional[str] = None
    instanceRole: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    placementGroup: Optional[str] = None
    bidPercentage: Optional[int] = None
    launchTemplate: Optional[LaunchTemplateSpecificationTypeDef] = None
    ec2Configuration: Optional[Sequence[Ec2ConfigurationTypeDef]] = None
    updateToLatestImageVersion: Optional[bool] = None
    type: Optional[CRTypeType] = None
    imageId: Optional[str] = None

class ContainerOverridesTypeDef(BaseModel):
    vcpus: Optional[int] = None
    memory: Optional[int] = None
    command: Optional[Sequence[str]] = None
    instanceType: Optional[str] = None
    environment: Optional[Sequence[KeyValuePairTypeDef]] = None
    resourceRequirements: Optional[Sequence[ResourceRequirementTypeDef]] = None

class TaskContainerOverridesTypeDef(BaseModel):
    command: Optional[Sequence[str]] = None
    environment: Optional[Sequence[KeyValuePairTypeDef]] = None
    name: Optional[str] = None
    resourceRequirements: Optional[Sequence[ResourceRequirementTypeDef]] = None

class LogConfigurationExtraOutputTypeDef(BaseModel):
    logDriver: LogDriverType
    options: Optional[Dict[str, str]] = None
    secretOptions: Optional[List[SecretTypeDef]] = None

class LogConfigurationOutputTypeDef(BaseModel):
    logDriver: LogDriverType
    options: Optional[Dict[str, str]] = None
    secretOptions: Optional[List[SecretTypeDef]] = None

class LogConfigurationTypeDef(BaseModel):
    logDriver: LogDriverType
    options: Optional[Mapping[str, str]] = None
    secretOptions: Optional[Sequence[SecretTypeDef]] = None

class CreateComputeEnvironmentResponseTypeDef(BaseModel):
    computeEnvironmentName: str
    computeEnvironmentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobQueueResponseTypeDef(BaseModel):
    jobQueueName: str
    jobQueueArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSchedulingPolicyResponseTypeDef(BaseModel):
    name: str
    arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterJobDefinitionResponseTypeDef(BaseModel):
    jobDefinitionName: str
    jobDefinitionArn: str
    revision: int
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitJobResponseTypeDef(BaseModel):
    jobArn: str
    jobName: str
    jobId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateComputeEnvironmentResponseTypeDef(BaseModel):
    computeEnvironmentName: str
    computeEnvironmentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateJobQueueResponseTypeDef(BaseModel):
    jobQueueName: str
    jobQueueArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateJobQueueRequestRequestTypeDef(BaseModel):
    jobQueueName: str
    priority: int
    computeEnvironmentOrder: Sequence[ComputeEnvironmentOrderTypeDef]
    state: Optional[JQStateType] = None
    schedulingPolicyArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    jobStateTimeLimitActions: Optional[Sequence[JobStateTimeLimitActionTypeDef]] = None

class JobQueueDetailTypeDef(BaseModel):
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

class UpdateJobQueueRequestRequestTypeDef(BaseModel):
    jobQueue: str
    state: Optional[JQStateType] = None
    schedulingPolicyArn: Optional[str] = None
    priority: Optional[int] = None
    computeEnvironmentOrder: Optional[Sequence[ComputeEnvironmentOrderTypeDef]] = None
    jobStateTimeLimitActions: Optional[Sequence[JobStateTimeLimitActionTypeDef]] = None

class DescribeComputeEnvironmentsRequestDescribeComputeEnvironmentsPaginateTypeDef(BaseModel):
    computeEnvironments: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeJobDefinitionsRequestDescribeJobDefinitionsPaginateTypeDef(BaseModel):
    jobDefinitions: Optional[Sequence[str]] = None
    jobDefinitionName: Optional[str] = None
    status: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeJobQueuesRequestDescribeJobQueuesPaginateTypeDef(BaseModel):
    jobQueues: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSchedulingPoliciesRequestListSchedulingPoliciesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class EFSVolumeConfigurationTypeDef(BaseModel):
    fileSystemId: str
    rootDirectory: Optional[str] = None
    transitEncryption: Optional[EFSTransitEncryptionType] = None
    transitEncryptionPort: Optional[int] = None
    authorizationConfig: Optional[EFSAuthorizationConfigTypeDef] = None

class EksAttemptDetailTypeDef(BaseModel):
    containers: Optional[List[EksAttemptContainerDetailTypeDef]] = None
    initContainers: Optional[List[EksAttemptContainerDetailTypeDef]] = None
    eksClusterArn: Optional[str] = None
    podName: Optional[str] = None
    nodeName: Optional[str] = None
    startedAt: Optional[int] = None
    stoppedAt: Optional[int] = None
    statusReason: Optional[str] = None

class EksContainerDetailTypeDef(BaseModel):
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

class EksContainerOutputTypeDef(BaseModel):
    image: str
    name: Optional[str] = None
    imagePullPolicy: Optional[str] = None
    command: Optional[List[str]] = None
    args: Optional[List[str]] = None
    env: Optional[List[EksContainerEnvironmentVariableTypeDef]] = None
    resources: Optional[EksContainerResourceRequirementsOutputTypeDef] = None
    volumeMounts: Optional[List[EksContainerVolumeMountTypeDef]] = None
    securityContext: Optional[EksContainerSecurityContextTypeDef] = None

class EksContainerExtraOutputTypeDef(BaseModel):
    image: str
    name: Optional[str] = None
    imagePullPolicy: Optional[str] = None
    command: Optional[List[str]] = None
    args: Optional[List[str]] = None
    env: Optional[List[EksContainerEnvironmentVariableTypeDef]] = None
    resources: Optional[EksContainerResourceRequirementsExtraOutputTypeDef] = None
    volumeMounts: Optional[List[EksContainerVolumeMountTypeDef]] = None
    securityContext: Optional[EksContainerSecurityContextTypeDef] = None

class EksContainerOverrideTypeDef(BaseModel):
    name: Optional[str] = None
    image: Optional[str] = None
    command: Optional[Sequence[str]] = None
    args: Optional[Sequence[str]] = None
    env: Optional[Sequence[EksContainerEnvironmentVariableTypeDef]] = None
    resources: Optional[EksContainerResourceRequirementsTypeDef] = None

class EksContainerTypeDef(BaseModel):
    image: str
    name: Optional[str] = None
    imagePullPolicy: Optional[str] = None
    command: Optional[Sequence[str]] = None
    args: Optional[Sequence[str]] = None
    env: Optional[Sequence[EksContainerEnvironmentVariableTypeDef]] = None
    resources: Optional[EksContainerResourceRequirementsTypeDef] = None
    volumeMounts: Optional[Sequence[EksContainerVolumeMountTypeDef]] = None
    securityContext: Optional[EksContainerSecurityContextTypeDef] = None

class EksVolumeTypeDef(BaseModel):
    name: str
    hostPath: Optional[EksHostPathTypeDef] = None
    emptyDir: Optional[EksEmptyDirTypeDef] = None
    secret: Optional[EksSecretTypeDef] = None

class RetryStrategyExtraOutputTypeDef(BaseModel):
    attempts: Optional[int] = None
    evaluateOnExit: Optional[List[EvaluateOnExitTypeDef]] = None

class RetryStrategyOutputTypeDef(BaseModel):
    attempts: Optional[int] = None
    evaluateOnExit: Optional[List[EvaluateOnExitTypeDef]] = None

class RetryStrategyTypeDef(BaseModel):
    attempts: Optional[int] = None
    evaluateOnExit: Optional[Sequence[EvaluateOnExitTypeDef]] = None

class FairsharePolicyOutputTypeDef(BaseModel):
    shareDecaySeconds: Optional[int] = None
    computeReservation: Optional[int] = None
    shareDistribution: Optional[List[ShareAttributesTypeDef]] = None

class FairsharePolicyTypeDef(BaseModel):
    shareDecaySeconds: Optional[int] = None
    computeReservation: Optional[int] = None
    shareDistribution: Optional[Sequence[ShareAttributesTypeDef]] = None

class FrontOfQueueDetailTypeDef(BaseModel):
    jobs: Optional[List[FrontOfQueueJobSummaryTypeDef]] = None
    lastUpdatedAt: Optional[int] = None

class JobSummaryTypeDef(BaseModel):
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

class ListJobsRequestListJobsPaginateTypeDef(BaseModel):
    jobQueue: Optional[str] = None
    arrayJobId: Optional[str] = None
    multiNodeJobId: Optional[str] = None
    jobStatus: Optional[JobStatusType] = None
    filters: Optional[Sequence[KeyValuesPairTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListJobsRequestRequestTypeDef(BaseModel):
    jobQueue: Optional[str] = None
    arrayJobId: Optional[str] = None
    multiNodeJobId: Optional[str] = None
    jobStatus: Optional[JobStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    filters: Optional[Sequence[KeyValuesPairTypeDef]] = None

class LinuxParametersExtraOutputTypeDef(BaseModel):
    devices: Optional[List[DeviceExtraOutputTypeDef]] = None
    initProcessEnabled: Optional[bool] = None
    sharedMemorySize: Optional[int] = None
    tmpfs: Optional[List[TmpfsExtraOutputTypeDef]] = None
    maxSwap: Optional[int] = None
    swappiness: Optional[int] = None

class LinuxParametersOutputTypeDef(BaseModel):
    devices: Optional[List[DeviceOutputTypeDef]] = None
    initProcessEnabled: Optional[bool] = None
    sharedMemorySize: Optional[int] = None
    tmpfs: Optional[List[TmpfsOutputTypeDef]] = None
    maxSwap: Optional[int] = None
    swappiness: Optional[int] = None

class LinuxParametersTypeDef(BaseModel):
    devices: Optional[Sequence[DeviceTypeDef]] = None
    initProcessEnabled: Optional[bool] = None
    sharedMemorySize: Optional[int] = None
    tmpfs: Optional[Sequence[TmpfsTypeDef]] = None
    maxSwap: Optional[int] = None
    swappiness: Optional[int] = None

class ListSchedulingPoliciesResponseTypeDef(BaseModel):
    schedulingPolicies: List[SchedulingPolicyListingDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttemptEcsTaskDetailsTypeDef(BaseModel):
    containerInstanceArn: Optional[str] = None
    taskArn: Optional[str] = None
    containers: Optional[List[AttemptTaskContainerDetailsTypeDef]] = None

class ComputeEnvironmentDetailTypeDef(BaseModel):
    computeEnvironmentName: str
    computeEnvironmentArn: str
    unmanagedvCpus: Optional[int] = None
    ecsClusterArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[CETypeType] = None
    state: Optional[CEStateType] = None
    status: Optional[CEStatusType] = None
    statusReason: Optional[str] = None
    computeResources: Optional[ComputeResourceOutputTypeDef] = None
    serviceRole: Optional[str] = None
    updatePolicy: Optional[UpdatePolicyTypeDef] = None
    eksConfiguration: Optional[EksConfigurationTypeDef] = None
    containerOrchestrationType: Optional[OrchestrationTypeType] = None
    uuid: Optional[str] = None

class CreateComputeEnvironmentRequestRequestTypeDef(BaseModel):
    computeEnvironmentName: str
    type: CETypeType
    state: Optional[CEStateType] = None
    unmanagedvCpus: Optional[int] = None
    computeResources: Optional[ComputeResourceTypeDef] = None
    serviceRole: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    eksConfiguration: Optional[EksConfigurationTypeDef] = None

class UpdateComputeEnvironmentRequestRequestTypeDef(BaseModel):
    computeEnvironment: str
    state: Optional[CEStateType] = None
    unmanagedvCpus: Optional[int] = None
    computeResources: Optional[ComputeResourceUpdateTypeDef] = None
    serviceRole: Optional[str] = None
    updatePolicy: Optional[UpdatePolicyTypeDef] = None

class TaskPropertiesOverrideTypeDef(BaseModel):
    containers: Optional[Sequence[TaskContainerOverridesTypeDef]] = None

class DescribeJobQueuesResponseTypeDef(BaseModel):
    jobQueues: List[JobQueueDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class VolumeTypeDef(BaseModel):
    host: Optional[HostTypeDef] = None
    name: Optional[str] = None
    efsVolumeConfiguration: Optional[EFSVolumeConfigurationTypeDef] = None

class EksPodPropertiesOverrideTypeDef(BaseModel):
    containers: Optional[Sequence[EksContainerOverrideTypeDef]] = None
    initContainers: Optional[Sequence[EksContainerOverrideTypeDef]] = None
    metadata: Optional[EksMetadataTypeDef] = None

class EksPodPropertiesDetailTypeDef(BaseModel):
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

class EksPodPropertiesExtraOutputTypeDef(BaseModel):
    serviceAccountName: Optional[str] = None
    hostNetwork: Optional[bool] = None
    dnsPolicy: Optional[str] = None
    imagePullSecrets: Optional[List[ImagePullSecretTypeDef]] = None
    containers: Optional[List[EksContainerExtraOutputTypeDef]] = None
    initContainers: Optional[List[EksContainerExtraOutputTypeDef]] = None
    volumes: Optional[List[EksVolumeTypeDef]] = None
    metadata: Optional[EksMetadataExtraOutputTypeDef] = None
    shareProcessNamespace: Optional[bool] = None

class EksPodPropertiesOutputTypeDef(BaseModel):
    serviceAccountName: Optional[str] = None
    hostNetwork: Optional[bool] = None
    dnsPolicy: Optional[str] = None
    imagePullSecrets: Optional[List[ImagePullSecretTypeDef]] = None
    containers: Optional[List[EksContainerOutputTypeDef]] = None
    initContainers: Optional[List[EksContainerOutputTypeDef]] = None
    volumes: Optional[List[EksVolumeTypeDef]] = None
    metadata: Optional[EksMetadataOutputTypeDef] = None
    shareProcessNamespace: Optional[bool] = None

class EksPodPropertiesTypeDef(BaseModel):
    serviceAccountName: Optional[str] = None
    hostNetwork: Optional[bool] = None
    dnsPolicy: Optional[str] = None
    imagePullSecrets: Optional[Sequence[ImagePullSecretTypeDef]] = None
    containers: Optional[Sequence[EksContainerTypeDef]] = None
    initContainers: Optional[Sequence[EksContainerTypeDef]] = None
    volumes: Optional[Sequence[EksVolumeTypeDef]] = None
    metadata: Optional[EksMetadataTypeDef] = None
    shareProcessNamespace: Optional[bool] = None

class SchedulingPolicyDetailTypeDef(BaseModel):
    name: str
    arn: str
    fairsharePolicy: Optional[FairsharePolicyOutputTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class CreateSchedulingPolicyRequestRequestTypeDef(BaseModel):
    name: str
    fairsharePolicy: Optional[FairsharePolicyTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateSchedulingPolicyRequestRequestTypeDef(BaseModel):
    arn: str
    fairsharePolicy: Optional[FairsharePolicyTypeDef] = None

class GetJobQueueSnapshotResponseTypeDef(BaseModel):
    frontOfQueue: FrontOfQueueDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListJobsResponseTypeDef(BaseModel):
    jobSummaryList: List[JobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class TaskContainerPropertiesExtraOutputTypeDef(BaseModel):
    image: str
    command: Optional[List[str]] = None
    dependsOn: Optional[List[TaskContainerDependencyTypeDef]] = None
    environment: Optional[List[KeyValuePairTypeDef]] = None
    essential: Optional[bool] = None
    linuxParameters: Optional[LinuxParametersExtraOutputTypeDef] = None
    logConfiguration: Optional[LogConfigurationExtraOutputTypeDef] = None
    mountPoints: Optional[List[MountPointTypeDef]] = None
    name: Optional[str] = None
    privileged: Optional[bool] = None
    readonlyRootFilesystem: Optional[bool] = None
    repositoryCredentials: Optional[RepositoryCredentialsTypeDef] = None
    resourceRequirements: Optional[List[ResourceRequirementTypeDef]] = None
    secrets: Optional[List[SecretTypeDef]] = None
    ulimits: Optional[List[UlimitTypeDef]] = None
    user: Optional[str] = None

class TaskContainerDetailsTypeDef(BaseModel):
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

class TaskContainerPropertiesOutputTypeDef(BaseModel):
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

class TaskContainerPropertiesTypeDef(BaseModel):
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

class AttemptDetailTypeDef(BaseModel):
    container: Optional[AttemptContainerDetailTypeDef] = None
    startedAt: Optional[int] = None
    stoppedAt: Optional[int] = None
    statusReason: Optional[str] = None
    taskProperties: Optional[List[AttemptEcsTaskDetailsTypeDef]] = None

class DescribeComputeEnvironmentsResponseTypeDef(BaseModel):
    computeEnvironments: List[ComputeEnvironmentDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EcsPropertiesOverrideTypeDef(BaseModel):
    taskProperties: Optional[Sequence[TaskPropertiesOverrideTypeDef]] = None

class ContainerDetailTypeDef(BaseModel):
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

class ContainerPropertiesExtraOutputTypeDef(BaseModel):
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
    linuxParameters: Optional[LinuxParametersExtraOutputTypeDef] = None
    logConfiguration: Optional[LogConfigurationExtraOutputTypeDef] = None
    secrets: Optional[List[SecretTypeDef]] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    fargatePlatformConfiguration: Optional[FargatePlatformConfigurationTypeDef] = None
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None
    runtimePlatform: Optional[RuntimePlatformTypeDef] = None
    repositoryCredentials: Optional[RepositoryCredentialsTypeDef] = None

class ContainerPropertiesOutputTypeDef(BaseModel):
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

class ContainerPropertiesTypeDef(BaseModel):
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

class EksPropertiesOverrideTypeDef(BaseModel):
    podProperties: Optional[EksPodPropertiesOverrideTypeDef] = None

class EksPropertiesDetailTypeDef(BaseModel):
    podProperties: Optional[EksPodPropertiesDetailTypeDef] = None

class EksPropertiesExtraOutputTypeDef(BaseModel):
    podProperties: Optional[EksPodPropertiesExtraOutputTypeDef] = None

class EksPropertiesOutputTypeDef(BaseModel):
    podProperties: Optional[EksPodPropertiesOutputTypeDef] = None

class EksPropertiesTypeDef(BaseModel):
    podProperties: Optional[EksPodPropertiesTypeDef] = None

class DescribeSchedulingPoliciesResponseTypeDef(BaseModel):
    schedulingPolicies: List[SchedulingPolicyDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EcsTaskPropertiesExtraOutputTypeDef(BaseModel):
    containers: List[TaskContainerPropertiesExtraOutputTypeDef]
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None
    executionRoleArn: Optional[str] = None
    platformVersion: Optional[str] = None
    ipcMode: Optional[str] = None
    taskRoleArn: Optional[str] = None
    pidMode: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    runtimePlatform: Optional[RuntimePlatformTypeDef] = None
    volumes: Optional[List[VolumeTypeDef]] = None

class EcsTaskDetailsTypeDef(BaseModel):
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

class EcsTaskPropertiesOutputTypeDef(BaseModel):
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

class EcsTaskPropertiesTypeDef(BaseModel):
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

class NodePropertyOverrideTypeDef(BaseModel):
    targetNodes: str
    containerOverrides: Optional[ContainerOverridesTypeDef] = None
    ecsPropertiesOverride: Optional[EcsPropertiesOverrideTypeDef] = None
    instanceTypes: Optional[Sequence[str]] = None
    eksPropertiesOverride: Optional[EksPropertiesOverrideTypeDef] = None

class EcsPropertiesExtraOutputTypeDef(BaseModel):
    taskProperties: List[EcsTaskPropertiesExtraOutputTypeDef]

class EcsPropertiesDetailTypeDef(BaseModel):
    taskProperties: Optional[List[EcsTaskDetailsTypeDef]] = None

class EcsPropertiesOutputTypeDef(BaseModel):
    taskProperties: List[EcsTaskPropertiesOutputTypeDef]

class EcsPropertiesTypeDef(BaseModel):
    taskProperties: Sequence[EcsTaskPropertiesTypeDef]

class NodeOverridesTypeDef(BaseModel):
    numNodes: Optional[int] = None
    nodePropertyOverrides: Optional[Sequence[NodePropertyOverrideTypeDef]] = None

class NodeRangePropertyExtraOutputTypeDef(BaseModel):
    targetNodes: str
    container: Optional[ContainerPropertiesExtraOutputTypeDef] = None
    instanceTypes: Optional[List[str]] = None
    ecsProperties: Optional[EcsPropertiesExtraOutputTypeDef] = None
    eksProperties: Optional[EksPropertiesExtraOutputTypeDef] = None

class NodeRangePropertyOutputTypeDef(BaseModel):
    targetNodes: str
    container: Optional[ContainerPropertiesOutputTypeDef] = None
    instanceTypes: Optional[List[str]] = None
    ecsProperties: Optional[EcsPropertiesOutputTypeDef] = None
    eksProperties: Optional[EksPropertiesOutputTypeDef] = None

class NodeRangePropertyTypeDef(BaseModel):
    targetNodes: str
    container: Optional[ContainerPropertiesTypeDef] = None
    instanceTypes: Optional[Sequence[str]] = None
    ecsProperties: Optional[EcsPropertiesTypeDef] = None
    eksProperties: Optional[EksPropertiesTypeDef] = None

class SubmitJobRequestRequestTypeDef(BaseModel):
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
    retryStrategy: Optional[RetryStrategyTypeDef] = None
    propagateTags: Optional[bool] = None
    timeout: Optional[JobTimeoutTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    eksPropertiesOverride: Optional[EksPropertiesOverrideTypeDef] = None
    ecsPropertiesOverride: Optional[EcsPropertiesOverrideTypeDef] = None

class NodePropertiesExtraOutputTypeDef(BaseModel):
    numNodes: int
    mainNode: int
    nodeRangeProperties: List[NodeRangePropertyExtraOutputTypeDef]

class NodePropertiesOutputTypeDef(BaseModel):
    numNodes: int
    mainNode: int
    nodeRangeProperties: List[NodeRangePropertyOutputTypeDef]

class NodePropertiesTypeDef(BaseModel):
    numNodes: int
    mainNode: int
    nodeRangeProperties: Sequence[NodeRangePropertyTypeDef]

class JobDefinitionTypeDef(BaseModel):
    jobDefinitionName: str
    jobDefinitionArn: str
    revision: int
    type: str
    status: Optional[str] = None
    schedulingPriority: Optional[int] = None
    parameters: Optional[Dict[str, str]] = None
    retryStrategy: Optional[RetryStrategyOutputTypeDef] = None
    containerProperties: Optional[ContainerPropertiesOutputTypeDef] = None
    timeout: Optional[JobTimeoutTypeDef] = None
    nodeProperties: Optional[NodePropertiesOutputTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    propagateTags: Optional[bool] = None
    platformCapabilities: Optional[List[PlatformCapabilityType]] = None
    ecsProperties: Optional[EcsPropertiesOutputTypeDef] = None
    eksProperties: Optional[EksPropertiesOutputTypeDef] = None
    containerOrchestrationType: Optional[OrchestrationTypeType] = None

class JobDetailTypeDef(BaseModel):
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

class RegisterJobDefinitionRequestRequestTypeDef(BaseModel):
    jobDefinitionName: str
    type: JobDefinitionTypeType
    parameters: Optional[Mapping[str, str]] = None
    schedulingPriority: Optional[int] = None
    containerProperties: Optional[ContainerPropertiesTypeDef] = None
    nodeProperties: Optional[NodePropertiesTypeDef] = None
    retryStrategy: Optional[RetryStrategyTypeDef] = None
    propagateTags: Optional[bool] = None
    timeout: Optional[JobTimeoutTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    platformCapabilities: Optional[Sequence[PlatformCapabilityType]] = None
    eksProperties: Optional[EksPropertiesTypeDef] = None
    ecsProperties: Optional[EcsPropertiesTypeDef] = None

class DescribeJobDefinitionsResponseTypeDef(BaseModel):
    jobDefinitions: List[JobDefinitionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeJobsResponseTypeDef(BaseModel):
    jobs: List[JobDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

