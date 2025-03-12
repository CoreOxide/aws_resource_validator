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
from aws_resource_validator.pydantic_models.ecs_constants import *

class AttachmentStateChangeTypeDef(BaseValidatorModel):
    attachmentArn: str
    status: str


class KeyValuePairTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None


class AttributeTypeDef(BaseValidatorModel):
    name: str
    value: Optional[str] = None
    targetType: Optional[Literal["container-instance"]] = None
    targetId: Optional[str] = None


class ManagedScalingTypeDef(BaseValidatorModel):
    status: Optional[ManagedScalingStatusType] = None
    targetCapacity: Optional[int] = None
    minimumScalingStepSize: Optional[int] = None
    maximumScalingStepSize: Optional[int] = None
    instanceWarmupPeriod: Optional[int] = None


class AwsVpcConfigurationOutputTypeDef(BaseValidatorModel):
    subnets: List[str]
    securityGroups: Optional[List[str]] = None
    assignPublicIp: Optional[AssignPublicIpType] = None


class AwsVpcConfigurationTypeDef(BaseValidatorModel):
    subnets: Sequence[str]
    securityGroups: Optional[Sequence[str]] = None
    assignPublicIp: Optional[AssignPublicIpType] = None


class CapacityProviderStrategyItemTypeDef(BaseValidatorModel):
    capacityProvider: str
    weight: Optional[int] = None
    base: Optional[int] = None


class TagTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class ManagedStorageConfigurationTypeDef(BaseValidatorModel):
    kmsKeyId: Optional[str] = None
    fargateEphemeralStorageKmsKeyId: Optional[str] = None


class ClusterServiceConnectDefaultsRequestTypeDef(BaseValidatorModel):
    namespace: str


class ClusterServiceConnectDefaultsTypeDef(BaseValidatorModel):
    namespace: Optional[str] = None


class ClusterSettingTypeDef(BaseValidatorModel):
    name: Optional[Literal["containerInsights"]] = None
    value: Optional[str] = None


class ContainerDependencyTypeDef(BaseValidatorModel):
    containerName: str
    condition: ContainerConditionType


class ContainerRestartPolicyOutputTypeDef(BaseValidatorModel):
    enabled: bool
    ignoredExitCodes: Optional[List[int]] = None
    restartAttemptPeriod: Optional[int] = None


class HealthCheckOutputTypeDef(BaseValidatorModel):
    command: List[str]
    interval: Optional[int] = None
    timeout: Optional[int] = None
    retries: Optional[int] = None
    startPeriod: Optional[int] = None


class HostEntryTypeDef(BaseValidatorModel):
    hostname: str
    ipAddress: str


class MountPointTypeDef(BaseValidatorModel):
    sourceVolume: Optional[str] = None
    containerPath: Optional[str] = None
    readOnly: Optional[bool] = None


class PortMappingTypeDef(BaseValidatorModel):
    containerPort: Optional[int] = None
    hostPort: Optional[int] = None
    protocol: Optional[TransportProtocolType] = None
    name: Optional[str] = None
    appProtocol: Optional[ApplicationProtocolType] = None
    containerPortRange: Optional[str] = None


class RepositoryCredentialsTypeDef(BaseValidatorModel):
    credentialsParameter: str


class SecretTypeDef(BaseValidatorModel):
    name: str
    valueFrom: str


class SystemControlTypeDef(BaseValidatorModel):
    namespace: Optional[str] = None
    value: Optional[str] = None


class UlimitTypeDef(BaseValidatorModel):
    name: UlimitNameType
    softLimit: int
    hardLimit: int


class VolumeFromTypeDef(BaseValidatorModel):
    sourceContainer: Optional[str] = None
    readOnly: Optional[bool] = None


class ContainerImageTypeDef(BaseValidatorModel):
    containerName: Optional[str] = None
    imageDigest: Optional[str] = None
    image: Optional[str] = None


class VersionInfoTypeDef(BaseValidatorModel):
    agentVersion: Optional[str] = None
    agentHash: Optional[str] = None
    dockerVersion: Optional[str] = None


class ContainerRestartPolicyTypeDef(BaseValidatorModel):
    enabled: bool
    ignoredExitCodes: Optional[Sequence[int]] = None
    restartAttemptPeriod: Optional[int] = None


class NetworkBindingTypeDef(BaseValidatorModel):
    bindIP: Optional[str] = None
    containerPort: Optional[int] = None
    hostPort: Optional[int] = None
    protocol: Optional[TransportProtocolType] = None
    containerPortRange: Optional[str] = None
    hostPortRange: Optional[str] = None


class ManagedAgentTypeDef(BaseValidatorModel):
    lastStartedAt: Optional[datetime] = None
    name: Optional[Literal["ExecuteCommandAgent"]] = None
    reason: Optional[str] = None
    lastStatus: Optional[str] = None


class NetworkInterfaceTypeDef(BaseValidatorModel):
    attachmentId: Optional[str] = None
    privateIpv4Address: Optional[str] = None
    ipv6Address: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class LoadBalancerTypeDef(BaseValidatorModel):
    targetGroupArn: Optional[str] = None
    loadBalancerName: Optional[str] = None
    containerName: Optional[str] = None
    containerPort: Optional[int] = None


class ServiceRegistryTypeDef(BaseValidatorModel):
    registryArn: Optional[str] = None
    port: Optional[int] = None
    containerName: Optional[str] = None
    containerPort: Optional[int] = None


class VpcLatticeConfigurationTypeDef(BaseValidatorModel):
    roleArn: str
    targetGroupArn: str
    portName: str


class ScaleTypeDef(BaseValidatorModel):
    value: Optional[float] = None
    unit: Optional[Literal["PERCENT"]] = None


class DeleteAccountSettingRequestTypeDef(BaseValidatorModel):
    name: SettingNameType
    principalArn: Optional[str] = None


class DeleteCapacityProviderRequestTypeDef(BaseValidatorModel):
    capacityProvider: str


class DeleteClusterRequestTypeDef(BaseValidatorModel):
    cluster: str


class DeleteServiceRequestTypeDef(BaseValidatorModel):
    service: str
    cluster: Optional[str] = None
    force: Optional[bool] = None


class DeleteTaskDefinitionsRequestTypeDef(BaseValidatorModel):
    taskDefinitions: Sequence[str]


class FailureTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    reason: Optional[str] = None
    detail: Optional[str] = None


class DeleteTaskSetRequestTypeDef(BaseValidatorModel):
    cluster: str
    service: str
    taskSet: str
    force: Optional[bool] = None


class DeploymentAlarmsOutputTypeDef(BaseValidatorModel):
    alarmNames: List[str]
    rollback: bool
    enable: bool


class DeploymentAlarmsTypeDef(BaseValidatorModel):
    alarmNames: Sequence[str]
    rollback: bool
    enable: bool


class DeploymentCircuitBreakerTypeDef(BaseValidatorModel):
    enable: bool
    rollback: bool


class DeploymentEphemeralStorageTypeDef(BaseValidatorModel):
    kmsKeyId: Optional[str] = None


class ServiceConnectServiceResourceTypeDef(BaseValidatorModel):
    discoveryName: Optional[str] = None
    discoveryArn: Optional[str] = None


class DeregisterContainerInstanceRequestTypeDef(BaseValidatorModel):
    containerInstance: str
    cluster: Optional[str] = None
    force: Optional[bool] = None


class DeregisterTaskDefinitionRequestTypeDef(BaseValidatorModel):
    taskDefinition: str


class DescribeCapacityProvidersRequestTypeDef(BaseValidatorModel):
    capacityProviders: Optional[Sequence[str]] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class DescribeClustersRequestTypeDef(BaseValidatorModel):
    clusters: Optional[Sequence[str]] = None
    include: Optional[Sequence[ClusterFieldType]] = None


class DescribeContainerInstancesRequestTypeDef(BaseValidatorModel):
    containerInstances: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[ContainerInstanceFieldType]] = None


class DescribeServiceDeploymentsRequestTypeDef(BaseValidatorModel):
    serviceDeploymentArns: Sequence[str]


class DescribeServiceRevisionsRequestTypeDef(BaseValidatorModel):
    serviceRevisionArns: Sequence[str]


class DescribeServicesRequestTypeDef(BaseValidatorModel):
    services: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class DescribeTaskDefinitionRequestTypeDef(BaseValidatorModel):
    taskDefinition: str
    include: Optional[Sequence[Literal["TAGS"]]] = None


class DescribeTaskSetsRequestTypeDef(BaseValidatorModel):
    cluster: str
    service: str
    taskSets: Optional[Sequence[str]] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None


class DescribeTasksRequestTypeDef(BaseValidatorModel):
    tasks: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None


class DeviceOutputTypeDef(BaseValidatorModel):
    hostPath: str
    containerPath: Optional[str] = None
    permissions: Optional[List[DeviceCgroupPermissionType]] = None


class DeviceTypeDef(BaseValidatorModel):
    hostPath: str
    containerPath: Optional[str] = None
    permissions: Optional[Sequence[DeviceCgroupPermissionType]] = None


class DiscoverPollEndpointRequestTypeDef(BaseValidatorModel):
    containerInstance: Optional[str] = None
    cluster: Optional[str] = None


class DockerVolumeConfigurationOutputTypeDef(BaseValidatorModel):
    scope: Optional[ScopeType] = None
    autoprovision: Optional[bool] = None
    driver: Optional[str] = None
    driverOpts: Optional[Dict[str, str]] = None
    labels: Optional[Dict[str, str]] = None


class DockerVolumeConfigurationTypeDef(BaseValidatorModel):
    scope: Optional[ScopeType] = None
    autoprovision: Optional[bool] = None
    driver: Optional[str] = None
    driverOpts: Optional[Mapping[str, str]] = None
    labels: Optional[Mapping[str, str]] = None


class EFSAuthorizationConfigTypeDef(BaseValidatorModel):
    accessPointId: Optional[str] = None
    iam: Optional[EFSAuthorizationConfigIAMType] = None


class EphemeralStorageTypeDef(BaseValidatorModel):
    sizeInGiB: int


class ExecuteCommandLogConfigurationTypeDef(BaseValidatorModel):
    cloudWatchLogGroupName: Optional[str] = None
    cloudWatchEncryptionEnabled: Optional[bool] = None
    s3BucketName: Optional[str] = None
    s3EncryptionEnabled: Optional[bool] = None
    s3KeyPrefix: Optional[str] = None


class ExecuteCommandRequestTypeDef(BaseValidatorModel):
    command: str
    interactive: bool
    task: str
    cluster: Optional[str] = None
    container: Optional[str] = None


class SessionTypeDef(BaseValidatorModel):
    sessionId: Optional[str] = None
    streamUrl: Optional[str] = None
    tokenValue: Optional[str] = None


class FSxWindowsFileServerAuthorizationConfigTypeDef(BaseValidatorModel):
    credentialsParameter: str
    domain: str


class GetTaskProtectionRequestTypeDef(BaseValidatorModel):
    cluster: str
    tasks: Optional[Sequence[str]] = None


class ProtectedTaskTypeDef(BaseValidatorModel):
    taskArn: Optional[str] = None
    protectionEnabled: Optional[bool] = None
    expirationDate: Optional[datetime] = None


class HealthCheckTypeDef(BaseValidatorModel):
    command: Sequence[str]
    interval: Optional[int] = None
    timeout: Optional[int] = None
    retries: Optional[int] = None
    startPeriod: Optional[int] = None


class HostVolumePropertiesTypeDef(BaseValidatorModel):
    sourcePath: Optional[str] = None


class InferenceAcceleratorOverrideTypeDef(BaseValidatorModel):
    deviceName: Optional[str] = None
    deviceType: Optional[str] = None


class InferenceAcceleratorTypeDef(BaseValidatorModel):
    deviceName: str
    deviceType: str


class KernelCapabilitiesOutputTypeDef(BaseValidatorModel):
    add: Optional[List[str]] = None
    drop: Optional[List[str]] = None


class KernelCapabilitiesTypeDef(BaseValidatorModel):
    add: Optional[Sequence[str]] = None
    drop: Optional[Sequence[str]] = None


class TmpfsOutputTypeDef(BaseValidatorModel):
    containerPath: str
    size: int
    mountOptions: Optional[List[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccountSettingsRequestTypeDef(BaseValidatorModel):
    name: Optional[SettingNameType] = None
    value: Optional[str] = None
    principalArn: Optional[str] = None
    effectiveSettings: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAttributesRequestTypeDef(BaseValidatorModel):
    targetType: Literal["container-instance"]
    cluster: Optional[str] = None
    attributeName: Optional[str] = None
    attributeValue: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListClustersRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ServiceDeploymentBriefTypeDef(BaseValidatorModel):
    serviceDeploymentArn: Optional[str] = None
    serviceArn: Optional[str] = None
    clusterArn: Optional[str] = None
    startedAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    finishedAt: Optional[datetime] = None
    targetServiceRevisionArn: Optional[str] = None
    status: Optional[ServiceDeploymentStatusType] = None
    statusReason: Optional[str] = None


class ListServicesByNamespaceRequestTypeDef(BaseValidatorModel):
    namespace: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListServicesRequestTypeDef(BaseValidatorModel):
    cluster: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    launchType: Optional[LaunchTypeType] = None
    schedulingStrategy: Optional[SchedulingStrategyType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListTaskDefinitionFamiliesRequestTypeDef(BaseValidatorModel):
    familyPrefix: Optional[str] = None
    status: Optional[TaskDefinitionFamilyStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTaskDefinitionsRequestTypeDef(BaseValidatorModel):
    familyPrefix: Optional[str] = None
    status: Optional[TaskDefinitionStatusType] = None
    sort: Optional[SortOrderType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTasksRequestTypeDef(BaseValidatorModel):
    cluster: Optional[str] = None
    containerInstance: Optional[str] = None
    family: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    startedBy: Optional[str] = None
    serviceName: Optional[str] = None
    desiredStatus: Optional[DesiredStatusType] = None
    launchType: Optional[LaunchTypeType] = None


class ManagedAgentStateChangeTypeDef(BaseValidatorModel):
    containerName: str
    managedAgentName: Literal["ExecuteCommandAgent"]
    status: str
    reason: Optional[str] = None


class PutAccountSettingDefaultRequestTypeDef(BaseValidatorModel):
    name: SettingNameType
    value: str


class PutAccountSettingRequestTypeDef(BaseValidatorModel):
    name: SettingNameType
    value: str
    principalArn: Optional[str] = None


class RuntimePlatformTypeDef(BaseValidatorModel):
    cpuArchitecture: Optional[CPUArchitectureType] = None
    operatingSystemFamily: Optional[OSFamilyType] = None


class RollbackTypeDef(BaseValidatorModel):
    reason: Optional[str] = None
    startedAt: Optional[datetime] = None
    serviceRevisionArn: Optional[str] = None


class ServiceConnectClientAliasTypeDef(BaseValidatorModel):
    port: int
    dnsName: Optional[str] = None


class TimeoutConfigurationTypeDef(BaseValidatorModel):
    idleTimeoutSeconds: Optional[int] = None
    perRequestTimeoutSeconds: Optional[int] = None


class ServiceConnectTlsCertificateAuthorityTypeDef(BaseValidatorModel):
    awsPcaAuthorityArn: Optional[str] = None


class ServiceDeploymentAlarmsTypeDef(BaseValidatorModel):
    status: Optional[ServiceDeploymentRollbackMonitorsStatusType] = None
    alarmNames: Optional[List[str]] = None
    triggeredAlarmNames: Optional[List[str]] = None


class ServiceDeploymentCircuitBreakerTypeDef(BaseValidatorModel):
    status: Optional[ServiceDeploymentRollbackMonitorsStatusType] = None
    failureCount: Optional[int] = None
    threshold: Optional[int] = None


class ServiceRevisionSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    requestedTaskCount: Optional[int] = None
    runningTaskCount: Optional[int] = None
    pendingTaskCount: Optional[int] = None


class StopTaskRequestTypeDef(BaseValidatorModel):
    task: str
    cluster: Optional[str] = None
    reason: Optional[str] = None


class TaskEphemeralStorageTypeDef(BaseValidatorModel):
    sizeInGiB: Optional[int] = None
    kmsKeyId: Optional[str] = None


class TaskManagedEBSVolumeTerminationPolicyTypeDef(BaseValidatorModel):
    deleteOnTermination: bool


class TmpfsTypeDef(BaseValidatorModel):
    containerPath: str
    size: int
    mountOptions: Optional[Sequence[str]] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateContainerAgentRequestTypeDef(BaseValidatorModel):
    containerInstance: str
    cluster: Optional[str] = None


class UpdateContainerInstancesStateRequestTypeDef(BaseValidatorModel):
    containerInstances: Sequence[str]
    status: ContainerInstanceStatusType
    cluster: Optional[str] = None


class UpdateServicePrimaryTaskSetRequestTypeDef(BaseValidatorModel):
    cluster: str
    service: str
    primaryTaskSet: str


class UpdateTaskProtectionRequestTypeDef(BaseValidatorModel):
    cluster: str
    tasks: Sequence[str]
    protectionEnabled: bool
    expiresInMinutes: Optional[int] = None


class SubmitAttachmentStateChangesRequestTypeDef(BaseValidatorModel):
    attachments: Sequence[AttachmentStateChangeTypeDef]
    cluster: Optional[str] = None


class DeleteAttributesRequestTypeDef(BaseValidatorModel):
    attributes: Sequence[AttributeTypeDef]
    cluster: Optional[str] = None


class PutAttributesRequestTypeDef(BaseValidatorModel):
    attributes: Sequence[AttributeTypeDef]
    cluster: Optional[str] = None


class AutoScalingGroupProviderTypeDef(BaseValidatorModel):
    autoScalingGroupArn: str
    managedScaling: Optional[ManagedScalingTypeDef] = None
    managedTerminationProtection: Optional[ManagedTerminationProtectionType] = None
    managedDraining: Optional[ManagedDrainingType] = None


class AutoScalingGroupProviderUpdateTypeDef(BaseValidatorModel):
    managedScaling: Optional[ManagedScalingTypeDef] = None
    managedTerminationProtection: Optional[ManagedTerminationProtectionType] = None
    managedDraining: Optional[ManagedDrainingType] = None


class NetworkConfigurationOutputTypeDef(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationOutputTypeDef] = None


class NetworkConfigurationTypeDef(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationTypeDef] = None


class PutClusterCapacityProvidersRequestTypeDef(BaseValidatorModel):
    cluster: str
    capacityProviders: Sequence[str]
    defaultCapacityProviderStrategy: Sequence[CapacityProviderStrategyItemTypeDef]


class EBSTagSpecificationOutputTypeDef(BaseValidatorModel):
    resourceType: Literal["volume"]
    tags: Optional[List[TagTypeDef]] = None
    propagateTags: Optional[PropagateTagsType] = None


class EBSTagSpecificationTypeDef(BaseValidatorModel):
    resourceType: Literal["volume"]
    tags: Optional[Sequence[TagTypeDef]] = None
    propagateTags: Optional[PropagateTagsType] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class UpdateClusterSettingsRequestTypeDef(BaseValidatorModel):
    cluster: str
    settings: Sequence[ClusterSettingTypeDef]


class EnvironmentFileTypeDef(BaseValidatorModel):
    pass


class ResourceRequirementTypeDef(BaseValidatorModel):
    pass


class ContainerOverrideOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    command: Optional[List[str]] = None
    environment: Optional[List[KeyValuePairTypeDef]] = None
    environmentFiles: Optional[List[EnvironmentFileTypeDef]] = None
    cpu: Optional[int] = None
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None
    resourceRequirements: Optional[List[ResourceRequirementTypeDef]] = None


class ContainerOverrideTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    command: Optional[Sequence[str]] = None
    environment: Optional[Sequence[KeyValuePairTypeDef]] = None
    environmentFiles: Optional[Sequence[EnvironmentFileTypeDef]] = None
    cpu: Optional[int] = None
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None
    resourceRequirements: Optional[Sequence[ResourceRequirementTypeDef]] = None


class LogConfigurationOutputTypeDef(BaseValidatorModel):
    logDriver: LogDriverType
    options: Optional[Dict[str, str]] = None
    secretOptions: Optional[List[SecretTypeDef]] = None


class LogConfigurationTypeDef(BaseValidatorModel):
    logDriver: LogDriverType
    options: Optional[Mapping[str, str]] = None
    secretOptions: Optional[Sequence[SecretTypeDef]] = None


class InstanceHealthCheckResultTypeDef(BaseValidatorModel):
    pass


class ContainerInstanceHealthStatusTypeDef(BaseValidatorModel):
    overallStatus: Optional[InstanceHealthCheckStateType] = None
    details: Optional[List[InstanceHealthCheckResultTypeDef]] = None


class ContainerStateChangeTypeDef(BaseValidatorModel):
    containerName: Optional[str] = None
    imageDigest: Optional[str] = None
    runtimeId: Optional[str] = None
    exitCode: Optional[int] = None
    networkBindings: Optional[Sequence[NetworkBindingTypeDef]] = None
    reason: Optional[str] = None
    status: Optional[str] = None


class SubmitContainerStateChangeRequestTypeDef(BaseValidatorModel):
    cluster: Optional[str] = None
    task: Optional[str] = None
    containerName: Optional[str] = None
    runtimeId: Optional[str] = None
    status: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    networkBindings: Optional[Sequence[NetworkBindingTypeDef]] = None


class ContainerTypeDef(BaseValidatorModel):
    containerArn: Optional[str] = None
    taskArn: Optional[str] = None
    name: Optional[str] = None
    image: Optional[str] = None
    imageDigest: Optional[str] = None
    runtimeId: Optional[str] = None
    lastStatus: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    networkBindings: Optional[List[NetworkBindingTypeDef]] = None
    networkInterfaces: Optional[List[NetworkInterfaceTypeDef]] = None
    healthStatus: Optional[HealthStatusType] = None
    managedAgents: Optional[List[ManagedAgentTypeDef]] = None
    cpu: Optional[str] = None
    memory: Optional[str] = None
    memoryReservation: Optional[str] = None
    gpuIds: Optional[List[str]] = None


class DeleteAttributesResponseTypeDef(BaseValidatorModel):
    attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DiscoverPollEndpointResponseTypeDef(BaseValidatorModel):
    endpoint: str
    telemetryEndpoint: str
    serviceConnectEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAttributesResponseTypeDef(BaseValidatorModel):
    attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListClustersResponseTypeDef(BaseValidatorModel):
    clusterArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListContainerInstancesResponseTypeDef(BaseValidatorModel):
    containerInstanceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListServicesByNamespaceResponseTypeDef(BaseValidatorModel):
    serviceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListServicesResponseTypeDef(BaseValidatorModel):
    serviceArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListTaskDefinitionFamiliesResponseTypeDef(BaseValidatorModel):
    families: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTaskDefinitionsResponseTypeDef(BaseValidatorModel):
    taskDefinitionArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTasksResponseTypeDef(BaseValidatorModel):
    taskArns: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PutAttributesResponseTypeDef(BaseValidatorModel):
    attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class SubmitAttachmentStateChangesResponseTypeDef(BaseValidatorModel):
    acknowledgment: str
    ResponseMetadata: ResponseMetadataTypeDef


class SubmitContainerStateChangeResponseTypeDef(BaseValidatorModel):
    acknowledgment: str
    ResponseMetadata: ResponseMetadataTypeDef


class SubmitTaskStateChangeResponseTypeDef(BaseValidatorModel):
    acknowledgment: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTaskSetRequestTypeDef(BaseValidatorModel):
    cluster: str
    service: str
    taskSet: str
    scale: ScaleTypeDef


class TimestampTypeDef(BaseValidatorModel):
    pass


class CreatedAtTypeDef(BaseValidatorModel):
    before: Optional[TimestampTypeDef] = None
    after: Optional[TimestampTypeDef] = None


class SettingTypeDef(BaseValidatorModel):
    pass


class DeleteAccountSettingResponseTypeDef(BaseValidatorModel):
    setting: SettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAccountSettingsResponseTypeDef(BaseValidatorModel):
    settings: List[SettingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PutAccountSettingDefaultResponseTypeDef(BaseValidatorModel):
    setting: SettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutAccountSettingResponseTypeDef(BaseValidatorModel):
    setting: SettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeploymentConfigurationOutputTypeDef(BaseValidatorModel):
    deploymentCircuitBreaker: Optional[DeploymentCircuitBreakerTypeDef] = None
    maximumPercent: Optional[int] = None
    minimumHealthyPercent: Optional[int] = None
    alarms: Optional[DeploymentAlarmsOutputTypeDef] = None


class DeploymentConfigurationTypeDef(BaseValidatorModel):
    deploymentCircuitBreaker: Optional[DeploymentCircuitBreakerTypeDef] = None
    maximumPercent: Optional[int] = None
    minimumHealthyPercent: Optional[int] = None
    alarms: Optional[DeploymentAlarmsTypeDef] = None


class DescribeServicesRequestWaitExtraTypeDef(BaseValidatorModel):
    services: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeServicesRequestWaitTypeDef(BaseValidatorModel):
    services: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeTasksRequestWaitExtraTypeDef(BaseValidatorModel):
    tasks: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class DescribeTasksRequestWaitTypeDef(BaseValidatorModel):
    tasks: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class EFSVolumeConfigurationTypeDef(BaseValidatorModel):
    fileSystemId: str
    rootDirectory: Optional[str] = None
    transitEncryption: Optional[EFSTransitEncryptionType] = None
    transitEncryptionPort: Optional[int] = None
    authorizationConfig: Optional[EFSAuthorizationConfigTypeDef] = None


class ExecuteCommandConfigurationTypeDef(BaseValidatorModel):
    kmsKeyId: Optional[str] = None
    logging: Optional[ExecuteCommandLoggingType] = None
    logConfiguration: Optional[ExecuteCommandLogConfigurationTypeDef] = None


class ExecuteCommandResponseTypeDef(BaseValidatorModel):
    clusterArn: str
    containerArn: str
    containerName: str
    interactive: bool
    session: SessionTypeDef
    taskArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class FSxWindowsFileServerVolumeConfigurationTypeDef(BaseValidatorModel):
    fileSystemId: str
    rootDirectory: str
    authorizationConfig: FSxWindowsFileServerAuthorizationConfigTypeDef


class GetTaskProtectionResponseTypeDef(BaseValidatorModel):
    protectedTasks: List[ProtectedTaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTaskProtectionResponseTypeDef(BaseValidatorModel):
    protectedTasks: List[ProtectedTaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class LinuxParametersOutputTypeDef(BaseValidatorModel):
    capabilities: Optional[KernelCapabilitiesOutputTypeDef] = None
    devices: Optional[List[DeviceOutputTypeDef]] = None
    initProcessEnabled: Optional[bool] = None
    sharedMemorySize: Optional[int] = None
    tmpfs: Optional[List[TmpfsOutputTypeDef]] = None
    maxSwap: Optional[int] = None
    swappiness: Optional[int] = None


class ListAccountSettingsRequestPaginateTypeDef(BaseValidatorModel):
    name: Optional[SettingNameType] = None
    value: Optional[str] = None
    principalArn: Optional[str] = None
    effectiveSettings: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAttributesRequestPaginateTypeDef(BaseValidatorModel):
    targetType: Literal["container-instance"]
    cluster: Optional[str] = None
    attributeName: Optional[str] = None
    attributeValue: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListClustersRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServicesByNamespaceRequestPaginateTypeDef(BaseValidatorModel):
    namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServicesRequestPaginateTypeDef(BaseValidatorModel):
    cluster: Optional[str] = None
    launchType: Optional[LaunchTypeType] = None
    schedulingStrategy: Optional[SchedulingStrategyType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTaskDefinitionFamiliesRequestPaginateTypeDef(BaseValidatorModel):
    familyPrefix: Optional[str] = None
    status: Optional[TaskDefinitionFamilyStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTaskDefinitionsRequestPaginateTypeDef(BaseValidatorModel):
    familyPrefix: Optional[str] = None
    status: Optional[TaskDefinitionStatusType] = None
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTasksRequestPaginateTypeDef(BaseValidatorModel):
    cluster: Optional[str] = None
    containerInstance: Optional[str] = None
    family: Optional[str] = None
    startedBy: Optional[str] = None
    serviceName: Optional[str] = None
    desiredStatus: Optional[DesiredStatusType] = None
    launchType: Optional[LaunchTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListServiceDeploymentsResponseTypeDef(BaseValidatorModel):
    serviceDeployments: List[ServiceDeploymentBriefTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ServiceConnectTlsConfigurationTypeDef(BaseValidatorModel):
    issuerCertificateAuthority: ServiceConnectTlsCertificateAuthorityTypeDef
    kmsKey: Optional[str] = None
    roleArn: Optional[str] = None


class CapacityProviderTypeDef(BaseValidatorModel):
    capacityProviderArn: Optional[str] = None
    name: Optional[str] = None
    status: Optional[CapacityProviderStatusType] = None
    autoScalingGroupProvider: Optional[AutoScalingGroupProviderTypeDef] = None
    updateStatus: Optional[CapacityProviderUpdateStatusType] = None
    updateStatusReason: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None


class CreateCapacityProviderRequestTypeDef(BaseValidatorModel):
    name: str
    autoScalingGroupProvider: AutoScalingGroupProviderTypeDef
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateCapacityProviderRequestTypeDef(BaseValidatorModel):
    name: str
    autoScalingGroupProvider: AutoScalingGroupProviderUpdateTypeDef


class ServiceManagedEBSVolumeConfigurationOutputTypeDef(BaseValidatorModel):
    roleArn: str
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None
    volumeType: Optional[str] = None
    sizeInGiB: Optional[int] = None
    snapshotId: Optional[str] = None
    iops: Optional[int] = None
    throughput: Optional[int] = None
    tagSpecifications: Optional[List[EBSTagSpecificationOutputTypeDef]] = None
    filesystemType: Optional[TaskFilesystemTypeType] = None


class TaskOverrideOutputTypeDef(BaseValidatorModel):
    containerOverrides: Optional[List[ContainerOverrideOutputTypeDef]] = None
    cpu: Optional[str] = None
    inferenceAcceleratorOverrides: Optional[List[InferenceAcceleratorOverrideTypeDef]] = None
    executionRoleArn: Optional[str] = None
    memory: Optional[str] = None
    taskRoleArn: Optional[str] = None
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None


class TaskOverrideTypeDef(BaseValidatorModel):
    containerOverrides: Optional[Sequence[ContainerOverrideTypeDef]] = None
    cpu: Optional[str] = None
    inferenceAcceleratorOverrides: Optional[Sequence[InferenceAcceleratorOverrideTypeDef]] = None
    executionRoleArn: Optional[str] = None
    memory: Optional[str] = None
    taskRoleArn: Optional[str] = None
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None


class AttachmentTypeDef(BaseValidatorModel):
    pass


class ResourceOutputTypeDef(BaseValidatorModel):
    pass


class ContainerInstanceTypeDef(BaseValidatorModel):
    containerInstanceArn: Optional[str] = None
    ec2InstanceId: Optional[str] = None
    capacityProviderName: Optional[str] = None
    version: Optional[int] = None
    versionInfo: Optional[VersionInfoTypeDef] = None
    remainingResources: Optional[List[ResourceOutputTypeDef]] = None
    registeredResources: Optional[List[ResourceOutputTypeDef]] = None
    status: Optional[str] = None
    statusReason: Optional[str] = None
    agentConnected: Optional[bool] = None
    runningTasksCount: Optional[int] = None
    pendingTasksCount: Optional[int] = None
    agentUpdateStatus: Optional[AgentUpdateStatusType] = None
    attributes: Optional[List[AttributeTypeDef]] = None
    registeredAt: Optional[datetime] = None
    attachments: Optional[List[AttachmentTypeDef]] = None
    tags: Optional[List[TagTypeDef]] = None
    healthStatus: Optional[ContainerInstanceHealthStatusTypeDef] = None


class SubmitTaskStateChangeRequestTypeDef(BaseValidatorModel):
    cluster: Optional[str] = None
    task: Optional[str] = None
    status: Optional[str] = None
    reason: Optional[str] = None
    containers: Optional[Sequence[ContainerStateChangeTypeDef]] = None
    attachments: Optional[Sequence[AttachmentStateChangeTypeDef]] = None
    managedAgents: Optional[Sequence[ManagedAgentStateChangeTypeDef]] = None
    pullStartedAt: Optional[TimestampTypeDef] = None
    pullStoppedAt: Optional[TimestampTypeDef] = None
    executionStoppedAt: Optional[TimestampTypeDef] = None


class ListServiceDeploymentsRequestTypeDef(BaseValidatorModel):
    service: str
    cluster: Optional[str] = None
    status: Optional[Sequence[ServiceDeploymentStatusType]] = None
    createdAt: Optional[CreatedAtTypeDef] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ServiceDeploymentTypeDef(BaseValidatorModel):
    serviceDeploymentArn: Optional[str] = None
    serviceArn: Optional[str] = None
    clusterArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    finishedAt: Optional[datetime] = None
    stoppedAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    sourceServiceRevisions: Optional[List[ServiceRevisionSummaryTypeDef]] = None
    targetServiceRevision: Optional[ServiceRevisionSummaryTypeDef] = None
    status: Optional[ServiceDeploymentStatusType] = None
    statusReason: Optional[str] = None
    deploymentConfiguration: Optional[DeploymentConfigurationOutputTypeDef] = None
    rollback: Optional[RollbackTypeDef] = None
    deploymentCircuitBreaker: Optional[ServiceDeploymentCircuitBreakerTypeDef] = None
    alarms: Optional[ServiceDeploymentAlarmsTypeDef] = None


class ClusterConfigurationTypeDef(BaseValidatorModel):
    executeCommandConfiguration: Optional[ExecuteCommandConfigurationTypeDef] = None
    managedStorageConfiguration: Optional[ManagedStorageConfigurationTypeDef] = None


class VolumeOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    host: Optional[HostVolumePropertiesTypeDef] = None
    dockerVolumeConfiguration: Optional[DockerVolumeConfigurationOutputTypeDef] = None
    efsVolumeConfiguration: Optional[EFSVolumeConfigurationTypeDef] = None
    fsxWindowsFileServerVolumeConfiguration: Optional[ FSxWindowsFileServerVolumeConfigurationTypeDef ] = None
    configuredAtLaunch: Optional[bool] = None


class DockerVolumeConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class VolumeTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    host: Optional[HostVolumePropertiesTypeDef] = None
    dockerVolumeConfiguration: Optional[DockerVolumeConfigurationUnionTypeDef] = None
    efsVolumeConfiguration: Optional[EFSVolumeConfigurationTypeDef] = None
    fsxWindowsFileServerVolumeConfiguration: Optional[ FSxWindowsFileServerVolumeConfigurationTypeDef ] = None
    configuredAtLaunch: Optional[bool] = None


class FirelensConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class ContainerDefinitionOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    image: Optional[str] = None
    repositoryCredentials: Optional[RepositoryCredentialsTypeDef] = None
    cpu: Optional[int] = None
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None
    links: Optional[List[str]] = None
    portMappings: Optional[List[PortMappingTypeDef]] = None
    essential: Optional[bool] = None
    restartPolicy: Optional[ContainerRestartPolicyOutputTypeDef] = None
    entryPoint: Optional[List[str]] = None
    command: Optional[List[str]] = None
    environment: Optional[List[KeyValuePairTypeDef]] = None
    environmentFiles: Optional[List[EnvironmentFileTypeDef]] = None
    mountPoints: Optional[List[MountPointTypeDef]] = None
    volumesFrom: Optional[List[VolumeFromTypeDef]] = None
    linuxParameters: Optional[LinuxParametersOutputTypeDef] = None
    secrets: Optional[List[SecretTypeDef]] = None
    dependsOn: Optional[List[ContainerDependencyTypeDef]] = None
    startTimeout: Optional[int] = None
    stopTimeout: Optional[int] = None
    versionConsistency: Optional[VersionConsistencyType] = None
    hostname: Optional[str] = None
    user: Optional[str] = None
    workingDirectory: Optional[str] = None
    disableNetworking: Optional[bool] = None
    privileged: Optional[bool] = None
    readonlyRootFilesystem: Optional[bool] = None
    dnsServers: Optional[List[str]] = None
    dnsSearchDomains: Optional[List[str]] = None
    extraHosts: Optional[List[HostEntryTypeDef]] = None
    dockerSecurityOptions: Optional[List[str]] = None
    interactive: Optional[bool] = None
    pseudoTerminal: Optional[bool] = None
    dockerLabels: Optional[Dict[str, str]] = None
    ulimits: Optional[List[UlimitTypeDef]] = None
    logConfiguration: Optional[LogConfigurationOutputTypeDef] = None
    healthCheck: Optional[HealthCheckOutputTypeDef] = None
    systemControls: Optional[List[SystemControlTypeDef]] = None
    resourceRequirements: Optional[List[ResourceRequirementTypeDef]] = None
    firelensConfiguration: Optional[FirelensConfigurationOutputTypeDef] = None
    credentialSpecs: Optional[List[str]] = None


class PlatformDeviceTypeDef(BaseValidatorModel):
    pass


class ResourceUnionTypeDef(BaseValidatorModel):
    pass


class RegisterContainerInstanceRequestTypeDef(BaseValidatorModel):
    cluster: Optional[str] = None
    instanceIdentityDocument: Optional[str] = None
    instanceIdentityDocumentSignature: Optional[str] = None
    totalResources: Optional[Sequence[ResourceUnionTypeDef]] = None
    versionInfo: Optional[VersionInfoTypeDef] = None
    containerInstanceArn: Optional[str] = None
    attributes: Optional[Sequence[AttributeTypeDef]] = None
    platformDevices: Optional[Sequence[PlatformDeviceTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ServiceConnectServiceOutputTypeDef(BaseValidatorModel):
    portName: str
    discoveryName: Optional[str] = None
    clientAliases: Optional[List[ServiceConnectClientAliasTypeDef]] = None
    ingressPortOverride: Optional[int] = None
    timeout: Optional[TimeoutConfigurationTypeDef] = None
    tls: Optional[ServiceConnectTlsConfigurationTypeDef] = None


class ServiceConnectServiceTypeDef(BaseValidatorModel):
    portName: str
    discoveryName: Optional[str] = None
    clientAliases: Optional[Sequence[ServiceConnectClientAliasTypeDef]] = None
    ingressPortOverride: Optional[int] = None
    timeout: Optional[TimeoutConfigurationTypeDef] = None
    tls: Optional[ServiceConnectTlsConfigurationTypeDef] = None


class DeviceUnionTypeDef(BaseValidatorModel):
    pass


class TmpfsUnionTypeDef(BaseValidatorModel):
    pass


class KernelCapabilitiesUnionTypeDef(BaseValidatorModel):
    pass


class LinuxParametersTypeDef(BaseValidatorModel):
    capabilities: Optional[KernelCapabilitiesUnionTypeDef] = None
    devices: Optional[Sequence[DeviceUnionTypeDef]] = None
    initProcessEnabled: Optional[bool] = None
    sharedMemorySize: Optional[int] = None
    tmpfs: Optional[Sequence[TmpfsUnionTypeDef]] = None
    maxSwap: Optional[int] = None
    swappiness: Optional[int] = None


class CreateCapacityProviderResponseTypeDef(BaseValidatorModel):
    capacityProvider: CapacityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteCapacityProviderResponseTypeDef(BaseValidatorModel):
    capacityProvider: CapacityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeCapacityProvidersResponseTypeDef(BaseValidatorModel):
    capacityProviders: List[CapacityProviderTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateCapacityProviderResponseTypeDef(BaseValidatorModel):
    capacityProvider: CapacityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class TaskSetTypeDef(BaseValidatorModel):
    pass


class CreateTaskSetResponseTypeDef(BaseValidatorModel):
    taskSet: TaskSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteTaskSetResponseTypeDef(BaseValidatorModel):
    taskSet: TaskSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTaskSetsResponseTypeDef(BaseValidatorModel):
    taskSets: List[TaskSetTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateServicePrimaryTaskSetResponseTypeDef(BaseValidatorModel):
    taskSet: TaskSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateTaskSetResponseTypeDef(BaseValidatorModel):
    taskSet: TaskSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class NetworkConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateTaskSetRequestTypeDef(BaseValidatorModel):
    service: str
    cluster: str
    taskDefinition: str
    externalId: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationUnionTypeDef] = None
    loadBalancers: Optional[Sequence[LoadBalancerTypeDef]] = None
    serviceRegistries: Optional[Sequence[ServiceRegistryTypeDef]] = None
    launchType: Optional[LaunchTypeType] = None
    capacityProviderStrategy: Optional[Sequence[CapacityProviderStrategyItemTypeDef]] = None
    platformVersion: Optional[str] = None
    scale: Optional[ScaleTypeDef] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ServiceVolumeConfigurationOutputTypeDef(BaseValidatorModel):
    name: str
    managedEBSVolume: Optional[ServiceManagedEBSVolumeConfigurationOutputTypeDef] = None


class EBSTagSpecificationUnionTypeDef(BaseValidatorModel):
    pass


class ServiceManagedEBSVolumeConfigurationTypeDef(BaseValidatorModel):
    roleArn: str
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None
    volumeType: Optional[str] = None
    sizeInGiB: Optional[int] = None
    snapshotId: Optional[str] = None
    iops: Optional[int] = None
    throughput: Optional[int] = None
    tagSpecifications: Optional[Sequence[EBSTagSpecificationUnionTypeDef]] = None
    filesystemType: Optional[TaskFilesystemTypeType] = None


class TaskManagedEBSVolumeConfigurationTypeDef(BaseValidatorModel):
    roleArn: str
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None
    volumeType: Optional[str] = None
    sizeInGiB: Optional[int] = None
    snapshotId: Optional[str] = None
    iops: Optional[int] = None
    throughput: Optional[int] = None
    tagSpecifications: Optional[Sequence[EBSTagSpecificationUnionTypeDef]] = None
    terminationPolicy: Optional[TaskManagedEBSVolumeTerminationPolicyTypeDef] = None
    filesystemType: Optional[TaskFilesystemTypeType] = None


class TaskTypeDef(BaseValidatorModel):
    attachments: Optional[List[AttachmentTypeDef]] = None
    attributes: Optional[List[AttributeTypeDef]] = None
    availabilityZone: Optional[str] = None
    capacityProviderName: Optional[str] = None
    clusterArn: Optional[str] = None
    connectivity: Optional[ConnectivityType] = None
    connectivityAt: Optional[datetime] = None
    containerInstanceArn: Optional[str] = None
    containers: Optional[List[ContainerTypeDef]] = None
    cpu: Optional[str] = None
    createdAt: Optional[datetime] = None
    desiredStatus: Optional[str] = None
    enableExecuteCommand: Optional[bool] = None
    executionStoppedAt: Optional[datetime] = None
    group: Optional[str] = None
    healthStatus: Optional[HealthStatusType] = None
    inferenceAccelerators: Optional[List[InferenceAcceleratorTypeDef]] = None
    lastStatus: Optional[str] = None
    launchType: Optional[LaunchTypeType] = None
    memory: Optional[str] = None
    overrides: Optional[TaskOverrideOutputTypeDef] = None
    platformVersion: Optional[str] = None
    platformFamily: Optional[str] = None
    pullStartedAt: Optional[datetime] = None
    pullStoppedAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    startedBy: Optional[str] = None
    stopCode: Optional[TaskStopCodeType] = None
    stoppedAt: Optional[datetime] = None
    stoppedReason: Optional[str] = None
    stoppingAt: Optional[datetime] = None
    tags: Optional[List[TagTypeDef]] = None
    taskArn: Optional[str] = None
    taskDefinitionArn: Optional[str] = None
    version: Optional[int] = None
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None
    fargateEphemeralStorage: Optional[TaskEphemeralStorageTypeDef] = None


class DeregisterContainerInstanceResponseTypeDef(BaseValidatorModel):
    containerInstance: ContainerInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeContainerInstancesResponseTypeDef(BaseValidatorModel):
    containerInstances: List[ContainerInstanceTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterContainerInstanceResponseTypeDef(BaseValidatorModel):
    containerInstance: ContainerInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateContainerAgentResponseTypeDef(BaseValidatorModel):
    containerInstance: ContainerInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateContainerInstancesStateResponseTypeDef(BaseValidatorModel):
    containerInstances: List[ContainerInstanceTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeServiceDeploymentsResponseTypeDef(BaseValidatorModel):
    serviceDeployments: List[ServiceDeploymentTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ClusterTypeDef(BaseValidatorModel):
    clusterArn: Optional[str] = None
    clusterName: Optional[str] = None
    configuration: Optional[ClusterConfigurationTypeDef] = None
    status: Optional[str] = None
    registeredContainerInstancesCount: Optional[int] = None
    runningTasksCount: Optional[int] = None
    pendingTasksCount: Optional[int] = None
    activeServicesCount: Optional[int] = None
    statistics: Optional[List[KeyValuePairTypeDef]] = None
    tags: Optional[List[TagTypeDef]] = None
    settings: Optional[List[ClusterSettingTypeDef]] = None
    capacityProviders: Optional[List[str]] = None
    defaultCapacityProviderStrategy: Optional[List[CapacityProviderStrategyItemTypeDef]] = None
    attachments: Optional[List[AttachmentTypeDef]] = None
    attachmentsStatus: Optional[str] = None
    serviceConnectDefaults: Optional[ClusterServiceConnectDefaultsTypeDef] = None


class CreateClusterRequestTypeDef(BaseValidatorModel):
    clusterName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    settings: Optional[Sequence[ClusterSettingTypeDef]] = None
    configuration: Optional[ClusterConfigurationTypeDef] = None
    capacityProviders: Optional[Sequence[str]] = None
    defaultCapacityProviderStrategy: Optional[Sequence[CapacityProviderStrategyItemTypeDef]] = None
    serviceConnectDefaults: Optional[ClusterServiceConnectDefaultsRequestTypeDef] = None


class UpdateClusterRequestTypeDef(BaseValidatorModel):
    cluster: str
    settings: Optional[Sequence[ClusterSettingTypeDef]] = None
    configuration: Optional[ClusterConfigurationTypeDef] = None
    serviceConnectDefaults: Optional[ClusterServiceConnectDefaultsRequestTypeDef] = None


class ProxyConfigurationOutputTypeDef(BaseValidatorModel):
    pass


class TaskDefinitionPlacementConstraintTypeDef(BaseValidatorModel):
    pass


class TaskDefinitionTypeDef(BaseValidatorModel):
    taskDefinitionArn: Optional[str] = None
    containerDefinitions: Optional[List[ContainerDefinitionOutputTypeDef]] = None
    family: Optional[str] = None
    taskRoleArn: Optional[str] = None
    executionRoleArn: Optional[str] = None
    networkMode: Optional[NetworkModeType] = None
    revision: Optional[int] = None
    volumes: Optional[List[VolumeOutputTypeDef]] = None
    status: Optional[TaskDefinitionStatusType] = None
    requiresAttributes: Optional[List[AttributeTypeDef]] = None
    placementConstraints: Optional[List[TaskDefinitionPlacementConstraintTypeDef]] = None
    compatibilities: Optional[List[CompatibilityType]] = None
    runtimePlatform: Optional[RuntimePlatformTypeDef] = None
    requiresCompatibilities: Optional[List[CompatibilityType]] = None
    cpu: Optional[str] = None
    memory: Optional[str] = None
    inferenceAccelerators: Optional[List[InferenceAcceleratorTypeDef]] = None
    pidMode: Optional[PidModeType] = None
    ipcMode: Optional[IpcModeType] = None
    proxyConfiguration: Optional[ProxyConfigurationOutputTypeDef] = None
    registeredAt: Optional[datetime] = None
    deregisteredAt: Optional[datetime] = None
    registeredBy: Optional[str] = None
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None
    enableFaultInjection: Optional[bool] = None


class ServiceConnectConfigurationOutputTypeDef(BaseValidatorModel):
    enabled: bool
    namespace: Optional[str] = None
    services: Optional[List[ServiceConnectServiceOutputTypeDef]] = None
    logConfiguration: Optional[LogConfigurationOutputTypeDef] = None


class ServiceConnectConfigurationTypeDef(BaseValidatorModel):
    enabled: bool
    namespace: Optional[str] = None
    services: Optional[Sequence[ServiceConnectServiceTypeDef]] = None
    logConfiguration: Optional[LogConfigurationTypeDef] = None


class TaskVolumeConfigurationTypeDef(BaseValidatorModel):
    name: str
    managedEBSVolume: Optional[TaskManagedEBSVolumeConfigurationTypeDef] = None


class DescribeTasksResponseTypeDef(BaseValidatorModel):
    tasks: List[TaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RunTaskResponseTypeDef(BaseValidatorModel):
    tasks: List[TaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StartTaskResponseTypeDef(BaseValidatorModel):
    tasks: List[TaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class StopTaskResponseTypeDef(BaseValidatorModel):
    task: TaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateClusterResponseTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteClusterResponseTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeClustersResponseTypeDef(BaseValidatorModel):
    clusters: List[ClusterTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutClusterCapacityProvidersResponseTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateClusterResponseTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateClusterSettingsResponseTypeDef(BaseValidatorModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteTaskDefinitionsResponseTypeDef(BaseValidatorModel):
    taskDefinitions: List[TaskDefinitionTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DeregisterTaskDefinitionResponseTypeDef(BaseValidatorModel):
    taskDefinition: TaskDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeTaskDefinitionResponseTypeDef(BaseValidatorModel):
    taskDefinition: TaskDefinitionTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RegisterTaskDefinitionResponseTypeDef(BaseValidatorModel):
    taskDefinition: TaskDefinitionTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ServiceRevisionTypeDef(BaseValidatorModel):
    serviceRevisionArn: Optional[str] = None
    serviceArn: Optional[str] = None
    clusterArn: Optional[str] = None
    taskDefinition: Optional[str] = None
    capacityProviderStrategy: Optional[List[CapacityProviderStrategyItemTypeDef]] = None
    launchType: Optional[LaunchTypeType] = None
    platformVersion: Optional[str] = None
    platformFamily: Optional[str] = None
    loadBalancers: Optional[List[LoadBalancerTypeDef]] = None
    serviceRegistries: Optional[List[ServiceRegistryTypeDef]] = None
    networkConfiguration: Optional[NetworkConfigurationOutputTypeDef] = None
    containerImages: Optional[List[ContainerImageTypeDef]] = None
    guardDutyEnabled: Optional[bool] = None
    serviceConnectConfiguration: Optional[ServiceConnectConfigurationOutputTypeDef] = None
    volumeConfigurations: Optional[List[ServiceVolumeConfigurationOutputTypeDef]] = None
    fargateEphemeralStorage: Optional[DeploymentEphemeralStorageTypeDef] = None
    createdAt: Optional[datetime] = None
    vpcLatticeConfigurations: Optional[List[VpcLatticeConfigurationTypeDef]] = None


class LogConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class FirelensConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class LinuxParametersUnionTypeDef(BaseValidatorModel):
    pass


class ContainerRestartPolicyUnionTypeDef(BaseValidatorModel):
    pass


class HealthCheckUnionTypeDef(BaseValidatorModel):
    pass


class ContainerDefinitionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    image: Optional[str] = None
    repositoryCredentials: Optional[RepositoryCredentialsTypeDef] = None
    cpu: Optional[int] = None
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None
    links: Optional[Sequence[str]] = None
    portMappings: Optional[Sequence[PortMappingTypeDef]] = None
    essential: Optional[bool] = None
    restartPolicy: Optional[ContainerRestartPolicyUnionTypeDef] = None
    entryPoint: Optional[Sequence[str]] = None
    command: Optional[Sequence[str]] = None
    environment: Optional[Sequence[KeyValuePairTypeDef]] = None
    environmentFiles: Optional[Sequence[EnvironmentFileTypeDef]] = None
    mountPoints: Optional[Sequence[MountPointTypeDef]] = None
    volumesFrom: Optional[Sequence[VolumeFromTypeDef]] = None
    linuxParameters: Optional[LinuxParametersUnionTypeDef] = None
    secrets: Optional[Sequence[SecretTypeDef]] = None
    dependsOn: Optional[Sequence[ContainerDependencyTypeDef]] = None
    startTimeout: Optional[int] = None
    stopTimeout: Optional[int] = None
    versionConsistency: Optional[VersionConsistencyType] = None
    hostname: Optional[str] = None
    user: Optional[str] = None
    workingDirectory: Optional[str] = None
    disableNetworking: Optional[bool] = None
    privileged: Optional[bool] = None
    readonlyRootFilesystem: Optional[bool] = None
    dnsServers: Optional[Sequence[str]] = None
    dnsSearchDomains: Optional[Sequence[str]] = None
    extraHosts: Optional[Sequence[HostEntryTypeDef]] = None
    dockerSecurityOptions: Optional[Sequence[str]] = None
    interactive: Optional[bool] = None
    pseudoTerminal: Optional[bool] = None
    dockerLabels: Optional[Mapping[str, str]] = None
    ulimits: Optional[Sequence[UlimitTypeDef]] = None
    logConfiguration: Optional[LogConfigurationUnionTypeDef] = None
    healthCheck: Optional[HealthCheckUnionTypeDef] = None
    systemControls: Optional[Sequence[SystemControlTypeDef]] = None
    resourceRequirements: Optional[Sequence[ResourceRequirementTypeDef]] = None
    firelensConfiguration: Optional[FirelensConfigurationUnionTypeDef] = None
    credentialSpecs: Optional[Sequence[str]] = None


class ServiceManagedEBSVolumeConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ServiceVolumeConfigurationTypeDef(BaseValidatorModel):
    name: str
    managedEBSVolume: Optional[ServiceManagedEBSVolumeConfigurationUnionTypeDef] = None


class PlacementStrategyTypeDef(BaseValidatorModel):
    pass


class PlacementConstraintTypeDef(BaseValidatorModel):
    pass


class TaskOverrideUnionTypeDef(BaseValidatorModel):
    pass


class RunTaskRequestTypeDef(BaseValidatorModel):
    taskDefinition: str
    capacityProviderStrategy: Optional[Sequence[CapacityProviderStrategyItemTypeDef]] = None
    cluster: Optional[str] = None
    count: Optional[int] = None
    enableECSManagedTags: Optional[bool] = None
    enableExecuteCommand: Optional[bool] = None
    group: Optional[str] = None
    launchType: Optional[LaunchTypeType] = None
    networkConfiguration: Optional[NetworkConfigurationUnionTypeDef] = None
    overrides: Optional[TaskOverrideUnionTypeDef] = None
    placementConstraints: Optional[Sequence[PlacementConstraintTypeDef]] = None
    placementStrategy: Optional[Sequence[PlacementStrategyTypeDef]] = None
    platformVersion: Optional[str] = None
    propagateTags: Optional[PropagateTagsType] = None
    referenceId: Optional[str] = None
    startedBy: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    clientToken: Optional[str] = None
    volumeConfigurations: Optional[Sequence[TaskVolumeConfigurationTypeDef]] = None


class StartTaskRequestTypeDef(BaseValidatorModel):
    containerInstances: Sequence[str]
    taskDefinition: str
    cluster: Optional[str] = None
    enableECSManagedTags: Optional[bool] = None
    enableExecuteCommand: Optional[bool] = None
    group: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationUnionTypeDef] = None
    overrides: Optional[TaskOverrideUnionTypeDef] = None
    propagateTags: Optional[PropagateTagsType] = None
    referenceId: Optional[str] = None
    startedBy: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    volumeConfigurations: Optional[Sequence[TaskVolumeConfigurationTypeDef]] = None


class DeploymentControllerTypeDef(BaseValidatorModel):
    pass


class ServiceEventTypeDef(BaseValidatorModel):
    pass


class DeploymentTypeDef(BaseValidatorModel):
    pass


class ServiceTypeDef(BaseValidatorModel):
    serviceArn: Optional[str] = None
    serviceName: Optional[str] = None
    clusterArn: Optional[str] = None
    loadBalancers: Optional[List[LoadBalancerTypeDef]] = None
    serviceRegistries: Optional[List[ServiceRegistryTypeDef]] = None
    status: Optional[str] = None
    desiredCount: Optional[int] = None
    runningCount: Optional[int] = None
    pendingCount: Optional[int] = None
    launchType: Optional[LaunchTypeType] = None
    capacityProviderStrategy: Optional[List[CapacityProviderStrategyItemTypeDef]] = None
    platformVersion: Optional[str] = None
    platformFamily: Optional[str] = None
    taskDefinition: Optional[str] = None
    deploymentConfiguration: Optional[DeploymentConfigurationOutputTypeDef] = None
    taskSets: Optional[List[TaskSetTypeDef]] = None
    deployments: Optional[List[DeploymentTypeDef]] = None
    roleArn: Optional[str] = None
    events: Optional[List[ServiceEventTypeDef]] = None
    createdAt: Optional[datetime] = None
    placementConstraints: Optional[List[PlacementConstraintTypeDef]] = None
    placementStrategy: Optional[List[PlacementStrategyTypeDef]] = None
    networkConfiguration: Optional[NetworkConfigurationOutputTypeDef] = None
    healthCheckGracePeriodSeconds: Optional[int] = None
    schedulingStrategy: Optional[SchedulingStrategyType] = None
    deploymentController: Optional[DeploymentControllerTypeDef] = None
    tags: Optional[List[TagTypeDef]] = None
    createdBy: Optional[str] = None
    enableECSManagedTags: Optional[bool] = None
    propagateTags: Optional[PropagateTagsType] = None
    enableExecuteCommand: Optional[bool] = None
    availabilityZoneRebalancing: Optional[AvailabilityZoneRebalancingType] = None


class DescribeServiceRevisionsResponseTypeDef(BaseValidatorModel):
    serviceRevisions: List[ServiceRevisionTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateServiceResponseTypeDef(BaseValidatorModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteServiceResponseTypeDef(BaseValidatorModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeServicesResponseTypeDef(BaseValidatorModel):
    services: List[ServiceTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateServiceResponseTypeDef(BaseValidatorModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ProxyConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ContainerDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class VolumeUnionTypeDef(BaseValidatorModel):
    pass


class RegisterTaskDefinitionRequestTypeDef(BaseValidatorModel):
    family: str
    containerDefinitions: Sequence[ContainerDefinitionUnionTypeDef]
    taskRoleArn: Optional[str] = None
    executionRoleArn: Optional[str] = None
    networkMode: Optional[NetworkModeType] = None
    volumes: Optional[Sequence[VolumeUnionTypeDef]] = None
    placementConstraints: Optional[Sequence[TaskDefinitionPlacementConstraintTypeDef]] = None
    requiresCompatibilities: Optional[Sequence[CompatibilityType]] = None
    cpu: Optional[str] = None
    memory: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    pidMode: Optional[PidModeType] = None
    ipcMode: Optional[IpcModeType] = None
    proxyConfiguration: Optional[ProxyConfigurationUnionTypeDef] = None
    inferenceAccelerators: Optional[Sequence[InferenceAcceleratorTypeDef]] = None
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None
    runtimePlatform: Optional[RuntimePlatformTypeDef] = None
    enableFaultInjection: Optional[bool] = None


class DeploymentConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ServiceVolumeConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ServiceConnectConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateServiceRequestTypeDef(BaseValidatorModel):
    serviceName: str
    cluster: Optional[str] = None
    taskDefinition: Optional[str] = None
    availabilityZoneRebalancing: Optional[AvailabilityZoneRebalancingType] = None
    loadBalancers: Optional[Sequence[LoadBalancerTypeDef]] = None
    serviceRegistries: Optional[Sequence[ServiceRegistryTypeDef]] = None
    desiredCount: Optional[int] = None
    clientToken: Optional[str] = None
    launchType: Optional[LaunchTypeType] = None
    capacityProviderStrategy: Optional[Sequence[CapacityProviderStrategyItemTypeDef]] = None
    platformVersion: Optional[str] = None
    role: Optional[str] = None
    deploymentConfiguration: Optional[DeploymentConfigurationUnionTypeDef] = None
    placementConstraints: Optional[Sequence[PlacementConstraintTypeDef]] = None
    placementStrategy: Optional[Sequence[PlacementStrategyTypeDef]] = None
    networkConfiguration: Optional[NetworkConfigurationUnionTypeDef] = None
    healthCheckGracePeriodSeconds: Optional[int] = None
    schedulingStrategy: Optional[SchedulingStrategyType] = None
    deploymentController: Optional[DeploymentControllerTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    enableECSManagedTags: Optional[bool] = None
    propagateTags: Optional[PropagateTagsType] = None
    enableExecuteCommand: Optional[bool] = None
    serviceConnectConfiguration: Optional[ServiceConnectConfigurationUnionTypeDef] = None
    volumeConfigurations: Optional[Sequence[ServiceVolumeConfigurationUnionTypeDef]] = None
    vpcLatticeConfigurations: Optional[Sequence[VpcLatticeConfigurationTypeDef]] = None


class UpdateServiceRequestTypeDef(BaseValidatorModel):
    service: str
    cluster: Optional[str] = None
    desiredCount: Optional[int] = None
    taskDefinition: Optional[str] = None
    capacityProviderStrategy: Optional[Sequence[CapacityProviderStrategyItemTypeDef]] = None
    deploymentConfiguration: Optional[DeploymentConfigurationUnionTypeDef] = None
    availabilityZoneRebalancing: Optional[AvailabilityZoneRebalancingType] = None
    networkConfiguration: Optional[NetworkConfigurationUnionTypeDef] = None
    placementConstraints: Optional[Sequence[PlacementConstraintTypeDef]] = None
    placementStrategy: Optional[Sequence[PlacementStrategyTypeDef]] = None
    platformVersion: Optional[str] = None
    forceNewDeployment: Optional[bool] = None
    healthCheckGracePeriodSeconds: Optional[int] = None
    enableExecuteCommand: Optional[bool] = None
    enableECSManagedTags: Optional[bool] = None
    loadBalancers: Optional[Sequence[LoadBalancerTypeDef]] = None
    propagateTags: Optional[PropagateTagsType] = None
    serviceRegistries: Optional[Sequence[ServiceRegistryTypeDef]] = None
    serviceConnectConfiguration: Optional[ServiceConnectConfigurationUnionTypeDef] = None
    volumeConfigurations: Optional[Sequence[ServiceVolumeConfigurationUnionTypeDef]] = None
    vpcLatticeConfigurations: Optional[Sequence[VpcLatticeConfigurationTypeDef]] = None


