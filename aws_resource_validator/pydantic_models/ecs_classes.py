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
from aws_resource_validator.pydantic_models.ecs_constants import *

class AttachmentStateChangeTypeDef(BaseModel):
    attachmentArn: str
    status: str

class KeyValuePairTypeDef(BaseModel):
    name: Optional[str] = None
    value: Optional[str] = None

class AttributeTypeDef(BaseModel):
    name: str
    value: Optional[str] = None
    targetType: Optional[Literal["container-instance"]] = None
    targetId: Optional[str] = None

class ManagedScalingTypeDef(BaseModel):
    status: Optional[ManagedScalingStatusType] = None
    targetCapacity: Optional[int] = None
    minimumScalingStepSize: Optional[int] = None
    maximumScalingStepSize: Optional[int] = None
    instanceWarmupPeriod: Optional[int] = None

class AwsVpcConfigurationOutputTypeDef(BaseModel):
    subnets: List[str]
    securityGroups: Optional[List[str]] = None
    assignPublicIp: Optional[AssignPublicIpType] = None

class AwsVpcConfigurationTypeDef(BaseModel):
    subnets: Sequence[str]
    securityGroups: Optional[Sequence[str]] = None
    assignPublicIp: Optional[AssignPublicIpType] = None

class CapacityProviderStrategyItemTypeDef(BaseModel):
    capacityProvider: str
    weight: Optional[int] = None
    base: Optional[int] = None

class TagTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class ManagedStorageConfigurationTypeDef(BaseModel):
    kmsKeyId: Optional[str] = None
    fargateEphemeralStorageKmsKeyId: Optional[str] = None

class ClusterServiceConnectDefaultsRequestTypeDef(BaseModel):
    namespace: str

class ClusterServiceConnectDefaultsTypeDef(BaseModel):
    namespace: Optional[str] = None

class ClusterSettingTypeDef(BaseModel):
    name: Optional[Literal["containerInsights"]] = None
    value: Optional[str] = None

class ContainerDependencyTypeDef(BaseModel):
    containerName: str
    condition: ContainerConditionType

class EnvironmentFileTypeDef(BaseModel):
    value: str
    type: Literal["s3"]

class FirelensConfigurationOutputTypeDef(BaseModel):
    type: FirelensConfigurationTypeType
    options: Optional[Dict[str, str]] = None

class HealthCheckOutputTypeDef(BaseModel):
    command: List[str]
    interval: Optional[int] = None
    timeout: Optional[int] = None
    retries: Optional[int] = None
    startPeriod: Optional[int] = None

class HostEntryTypeDef(BaseModel):
    hostname: str
    ipAddress: str

class MountPointTypeDef(BaseModel):
    sourceVolume: Optional[str] = None
    containerPath: Optional[str] = None
    readOnly: Optional[bool] = None

class PortMappingTypeDef(BaseModel):
    containerPort: Optional[int] = None
    hostPort: Optional[int] = None
    protocol: Optional[TransportProtocolType] = None
    name: Optional[str] = None
    appProtocol: Optional[ApplicationProtocolType] = None
    containerPortRange: Optional[str] = None

class RepositoryCredentialsTypeDef(BaseModel):
    credentialsParameter: str

class ResourceRequirementTypeDef(BaseModel):
    value: str
    type: ResourceTypeType

class SecretTypeDef(BaseModel):
    name: str
    valueFrom: str

class SystemControlTypeDef(BaseModel):
    namespace: Optional[str] = None
    value: Optional[str] = None

class UlimitTypeDef(BaseModel):
    name: UlimitNameType
    softLimit: int
    hardLimit: int

class VolumeFromTypeDef(BaseModel):
    sourceContainer: Optional[str] = None
    readOnly: Optional[bool] = None

class FirelensConfigurationTypeDef(BaseModel):
    type: FirelensConfigurationTypeType
    options: Optional[Mapping[str, str]] = None

class HealthCheckTypeDef(BaseModel):
    command: Sequence[str]
    interval: Optional[int] = None
    timeout: Optional[int] = None
    retries: Optional[int] = None
    startPeriod: Optional[int] = None

class InstanceHealthCheckResultTypeDef(BaseModel):
    type: Optional[Literal["CONTAINER_RUNTIME"]] = None
    status: Optional[InstanceHealthCheckStateType] = None
    lastUpdated: Optional[datetime] = None
    lastStatusChange: Optional[datetime] = None

class ResourceOutputTypeDef(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    doubleValue: Optional[float] = None
    longValue: Optional[int] = None
    integerValue: Optional[int] = None
    stringSetValue: Optional[List[str]] = None

class VersionInfoTypeDef(BaseModel):
    agentVersion: Optional[str] = None
    agentHash: Optional[str] = None
    dockerVersion: Optional[str] = None

class NetworkBindingTypeDef(BaseModel):
    bindIP: Optional[str] = None
    containerPort: Optional[int] = None
    hostPort: Optional[int] = None
    protocol: Optional[TransportProtocolType] = None
    containerPortRange: Optional[str] = None
    hostPortRange: Optional[str] = None

class ManagedAgentTypeDef(BaseModel):
    lastStartedAt: Optional[datetime] = None
    name: Optional[Literal["ExecuteCommandAgent"]] = None
    reason: Optional[str] = None
    lastStatus: Optional[str] = None

class NetworkInterfaceTypeDef(BaseModel):
    attachmentId: Optional[str] = None
    privateIpv4Address: Optional[str] = None
    ipv6Address: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DeploymentControllerTypeDef(BaseModel):
    type: DeploymentControllerTypeType

class LoadBalancerTypeDef(BaseModel):
    targetGroupArn: Optional[str] = None
    loadBalancerName: Optional[str] = None
    containerName: Optional[str] = None
    containerPort: Optional[int] = None

class PlacementConstraintTypeDef(BaseModel):
    type: Optional[PlacementConstraintTypeType] = None
    expression: Optional[str] = None

class PlacementStrategyTypeDef(BaseModel):
    type: Optional[PlacementStrategyTypeType] = None
    field: Optional[str] = None

class ServiceRegistryTypeDef(BaseModel):
    registryArn: Optional[str] = None
    port: Optional[int] = None
    containerName: Optional[str] = None
    containerPort: Optional[int] = None

class ScaleTypeDef(BaseModel):
    value: Optional[float] = None
    unit: Optional[Literal["PERCENT"]] = None

class DeleteAccountSettingRequestRequestTypeDef(BaseModel):
    name: SettingNameType
    principalArn: Optional[str] = None

class SettingTypeDef(BaseModel):
    name: Optional[SettingNameType] = None
    value: Optional[str] = None
    principalArn: Optional[str] = None
    type: Optional[SettingTypeType] = None

class DeleteCapacityProviderRequestRequestTypeDef(BaseModel):
    capacityProvider: str

class DeleteClusterRequestRequestTypeDef(BaseModel):
    cluster: str

class DeleteServiceRequestRequestTypeDef(BaseModel):
    service: str
    cluster: Optional[str] = None
    force: Optional[bool] = None

class DeleteTaskDefinitionsRequestRequestTypeDef(BaseModel):
    taskDefinitions: Sequence[str]

class FailureTypeDef(BaseModel):
    arn: Optional[str] = None
    reason: Optional[str] = None
    detail: Optional[str] = None

class DeleteTaskSetRequestRequestTypeDef(BaseModel):
    cluster: str
    service: str
    taskSet: str
    force: Optional[bool] = None

class DeploymentAlarmsOutputTypeDef(BaseModel):
    alarmNames: List[str]
    enable: bool
    rollback: bool

class DeploymentAlarmsTypeDef(BaseModel):
    alarmNames: Sequence[str]
    enable: bool
    rollback: bool

class DeploymentCircuitBreakerTypeDef(BaseModel):
    enable: bool
    rollback: bool

class DeploymentEphemeralStorageTypeDef(BaseModel):
    kmsKeyId: Optional[str] = None

class ServiceConnectServiceResourceTypeDef(BaseModel):
    discoveryName: Optional[str] = None
    discoveryArn: Optional[str] = None

class DeregisterContainerInstanceRequestRequestTypeDef(BaseModel):
    containerInstance: str
    cluster: Optional[str] = None
    force: Optional[bool] = None

class DeregisterTaskDefinitionRequestRequestTypeDef(BaseModel):
    taskDefinition: str

class DescribeCapacityProvidersRequestRequestTypeDef(BaseModel):
    capacityProviders: Optional[Sequence[str]] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class DescribeClustersRequestRequestTypeDef(BaseModel):
    clusters: Optional[Sequence[str]] = None
    include: Optional[Sequence[ClusterFieldType]] = None

class DescribeContainerInstancesRequestRequestTypeDef(BaseModel):
    containerInstances: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[ContainerInstanceFieldType]] = None

class DescribeServicesRequestRequestTypeDef(BaseModel):
    services: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class DescribeTaskDefinitionRequestRequestTypeDef(BaseModel):
    taskDefinition: str
    include: Optional[Sequence[Literal["TAGS"]]] = None

class DescribeTaskSetsRequestRequestTypeDef(BaseModel):
    cluster: str
    service: str
    taskSets: Optional[Sequence[str]] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None

class DescribeTasksRequestRequestTypeDef(BaseModel):
    tasks: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None

class DeviceOutputTypeDef(BaseModel):
    hostPath: str
    containerPath: Optional[str] = None
    permissions: Optional[List[DeviceCgroupPermissionType]] = None

class DeviceTypeDef(BaseModel):
    hostPath: str
    containerPath: Optional[str] = None
    permissions: Optional[Sequence[DeviceCgroupPermissionType]] = None

class DiscoverPollEndpointRequestRequestTypeDef(BaseModel):
    containerInstance: Optional[str] = None
    cluster: Optional[str] = None

class DockerVolumeConfigurationOutputTypeDef(BaseModel):
    scope: Optional[ScopeType] = None
    autoprovision: Optional[bool] = None
    driver: Optional[str] = None
    driverOpts: Optional[Dict[str, str]] = None
    labels: Optional[Dict[str, str]] = None

class DockerVolumeConfigurationTypeDef(BaseModel):
    scope: Optional[ScopeType] = None
    autoprovision: Optional[bool] = None
    driver: Optional[str] = None
    driverOpts: Optional[Mapping[str, str]] = None
    labels: Optional[Mapping[str, str]] = None

class EFSAuthorizationConfigTypeDef(BaseModel):
    accessPointId: Optional[str] = None
    iam: Optional[EFSAuthorizationConfigIAMType] = None

class EphemeralStorageTypeDef(BaseModel):
    sizeInGiB: int

class ExecuteCommandLogConfigurationTypeDef(BaseModel):
    cloudWatchLogGroupName: Optional[str] = None
    cloudWatchEncryptionEnabled: Optional[bool] = None
    s3BucketName: Optional[str] = None
    s3EncryptionEnabled: Optional[bool] = None
    s3KeyPrefix: Optional[str] = None

class ExecuteCommandRequestRequestTypeDef(BaseModel):
    command: str
    interactive: bool
    task: str
    cluster: Optional[str] = None
    container: Optional[str] = None

class SessionTypeDef(BaseModel):
    sessionId: Optional[str] = None
    streamUrl: Optional[str] = None
    tokenValue: Optional[str] = None

class FSxWindowsFileServerAuthorizationConfigTypeDef(BaseModel):
    credentialsParameter: str
    domain: str

class GetTaskProtectionRequestRequestTypeDef(BaseModel):
    cluster: str
    tasks: Optional[Sequence[str]] = None

class ProtectedTaskTypeDef(BaseModel):
    taskArn: Optional[str] = None
    protectionEnabled: Optional[bool] = None
    expirationDate: Optional[datetime] = None

class HostVolumePropertiesTypeDef(BaseModel):
    sourcePath: Optional[str] = None

class InferenceAcceleratorOverrideTypeDef(BaseModel):
    deviceName: Optional[str] = None
    deviceType: Optional[str] = None

class InferenceAcceleratorTypeDef(BaseModel):
    deviceName: str
    deviceType: str

class KernelCapabilitiesOutputTypeDef(BaseModel):
    add: Optional[List[str]] = None
    drop: Optional[List[str]] = None

class KernelCapabilitiesTypeDef(BaseModel):
    add: Optional[Sequence[str]] = None
    drop: Optional[Sequence[str]] = None

class TmpfsOutputTypeDef(BaseModel):
    containerPath: str
    size: int
    mountOptions: Optional[List[str]] = None

class TmpfsTypeDef(BaseModel):
    containerPath: str
    size: int
    mountOptions: Optional[Sequence[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccountSettingsRequestRequestTypeDef(BaseModel):
    name: Optional[SettingNameType] = None
    value: Optional[str] = None
    principalArn: Optional[str] = None
    effectiveSettings: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListAttributesRequestRequestTypeDef(BaseModel):
    targetType: Literal["container-instance"]
    cluster: Optional[str] = None
    attributeName: Optional[str] = None
    attributeValue: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListClustersRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListContainerInstancesRequestRequestTypeDef(BaseModel):
    cluster: Optional[str] = None
    filter: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[ContainerInstanceStatusType] = None

class ListServicesByNamespaceRequestRequestTypeDef(BaseModel):
    namespace: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListServicesRequestRequestTypeDef(BaseModel):
    cluster: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    launchType: Optional[LaunchTypeType] = None
    schedulingStrategy: Optional[SchedulingStrategyType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListTaskDefinitionFamiliesRequestRequestTypeDef(BaseModel):
    familyPrefix: Optional[str] = None
    status: Optional[TaskDefinitionFamilyStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTaskDefinitionsRequestRequestTypeDef(BaseModel):
    familyPrefix: Optional[str] = None
    status: Optional[TaskDefinitionStatusType] = None
    sort: Optional[SortOrderType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListTasksRequestRequestTypeDef(BaseModel):
    cluster: Optional[str] = None
    containerInstance: Optional[str] = None
    family: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    startedBy: Optional[str] = None
    serviceName: Optional[str] = None
    desiredStatus: Optional[DesiredStatusType] = None
    launchType: Optional[LaunchTypeType] = None

class ManagedAgentStateChangeTypeDef(BaseModel):
    containerName: str
    managedAgentName: Literal["ExecuteCommandAgent"]
    status: str
    reason: Optional[str] = None

class PlatformDeviceTypeDef(BaseModel):
    id: str
    type: Literal["GPU"]

class PutAccountSettingDefaultRequestRequestTypeDef(BaseModel):
    name: SettingNameType
    value: str

class PutAccountSettingRequestRequestTypeDef(BaseModel):
    name: SettingNameType
    value: str
    principalArn: Optional[str] = None

class RuntimePlatformTypeDef(BaseModel):
    cpuArchitecture: Optional[CPUArchitectureType] = None
    operatingSystemFamily: Optional[OSFamilyType] = None

class TaskDefinitionPlacementConstraintTypeDef(BaseModel):
    type: Optional[Literal["memberOf"]] = None
    expression: Optional[str] = None

class ResourceTypeDef(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    doubleValue: Optional[float] = None
    longValue: Optional[int] = None
    integerValue: Optional[int] = None
    stringSetValue: Optional[Sequence[str]] = None

class ServiceConnectClientAliasTypeDef(BaseModel):
    port: int
    dnsName: Optional[str] = None

class TimeoutConfigurationTypeDef(BaseModel):
    idleTimeoutSeconds: Optional[int] = None
    perRequestTimeoutSeconds: Optional[int] = None

class ServiceConnectTlsCertificateAuthorityTypeDef(BaseModel):
    awsPcaAuthorityArn: Optional[str] = None

class ServiceEventTypeDef(BaseModel):
    id: Optional[str] = None
    createdAt: Optional[datetime] = None
    message: Optional[str] = None

class StopTaskRequestRequestTypeDef(BaseModel):
    task: str
    cluster: Optional[str] = None
    reason: Optional[str] = None

class TaskEphemeralStorageTypeDef(BaseModel):
    sizeInGiB: Optional[int] = None
    kmsKeyId: Optional[str] = None

class TaskManagedEBSVolumeTerminationPolicyTypeDef(BaseModel):
    deleteOnTermination: bool

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateContainerAgentRequestRequestTypeDef(BaseModel):
    containerInstance: str
    cluster: Optional[str] = None

class UpdateContainerInstancesStateRequestRequestTypeDef(BaseModel):
    containerInstances: Sequence[str]
    status: ContainerInstanceStatusType
    cluster: Optional[str] = None

class UpdateServicePrimaryTaskSetRequestRequestTypeDef(BaseModel):
    cluster: str
    service: str
    primaryTaskSet: str

class UpdateTaskProtectionRequestRequestTypeDef(BaseModel):
    cluster: str
    tasks: Sequence[str]
    protectionEnabled: bool
    expiresInMinutes: Optional[int] = None

class SubmitAttachmentStateChangesRequestRequestTypeDef(BaseModel):
    attachments: Sequence[AttachmentStateChangeTypeDef]
    cluster: Optional[str] = None

class AttachmentTypeDef(BaseModel):
    id: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    details: Optional[List[KeyValuePairTypeDef]] = None

class ProxyConfigurationOutputTypeDef(BaseModel):
    containerName: str
    type: Optional[Literal["APPMESH"]] = None
    properties: Optional[List[KeyValuePairTypeDef]] = None

class ProxyConfigurationTypeDef(BaseModel):
    containerName: str
    type: Optional[Literal["APPMESH"]] = None
    properties: Optional[Sequence[KeyValuePairTypeDef]] = None

class DeleteAttributesRequestRequestTypeDef(BaseModel):
    attributes: Sequence[AttributeTypeDef]
    cluster: Optional[str] = None

class PutAttributesRequestRequestTypeDef(BaseModel):
    attributes: Sequence[AttributeTypeDef]
    cluster: Optional[str] = None

class AutoScalingGroupProviderTypeDef(BaseModel):
    autoScalingGroupArn: str
    managedScaling: Optional[ManagedScalingTypeDef] = None
    managedTerminationProtection: Optional[ManagedTerminationProtectionType] = None
    managedDraining: Optional[ManagedDrainingType] = None

class AutoScalingGroupProviderUpdateTypeDef(BaseModel):
    managedScaling: Optional[ManagedScalingTypeDef] = None
    managedTerminationProtection: Optional[ManagedTerminationProtectionType] = None
    managedDraining: Optional[ManagedDrainingType] = None

class NetworkConfigurationOutputTypeDef(BaseModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationOutputTypeDef] = None

class NetworkConfigurationTypeDef(BaseModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationTypeDef] = None

class PutClusterCapacityProvidersRequestRequestTypeDef(BaseModel):
    cluster: str
    capacityProviders: Sequence[str]
    defaultCapacityProviderStrategy: Sequence[CapacityProviderStrategyItemTypeDef]

class EBSTagSpecificationOutputTypeDef(BaseModel):
    resourceType: Literal["volume"]
    tags: Optional[List[TagTypeDef]] = None
    propagateTags: Optional[PropagateTagsType] = None

class EBSTagSpecificationTypeDef(BaseModel):
    resourceType: Literal["volume"]
    tags: Optional[Sequence[TagTypeDef]] = None
    propagateTags: Optional[PropagateTagsType] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class UpdateClusterSettingsRequestRequestTypeDef(BaseModel):
    cluster: str
    settings: Sequence[ClusterSettingTypeDef]

class ContainerOverrideOutputTypeDef(BaseModel):
    name: Optional[str] = None
    command: Optional[List[str]] = None
    environment: Optional[List[KeyValuePairTypeDef]] = None
    environmentFiles: Optional[List[EnvironmentFileTypeDef]] = None
    cpu: Optional[int] = None
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None
    resourceRequirements: Optional[List[ResourceRequirementTypeDef]] = None

class ContainerOverrideTypeDef(BaseModel):
    name: Optional[str] = None
    command: Optional[Sequence[str]] = None
    environment: Optional[Sequence[KeyValuePairTypeDef]] = None
    environmentFiles: Optional[Sequence[EnvironmentFileTypeDef]] = None
    cpu: Optional[int] = None
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None
    resourceRequirements: Optional[Sequence[ResourceRequirementTypeDef]] = None

class LogConfigurationOutputTypeDef(BaseModel):
    logDriver: LogDriverType
    options: Optional[Dict[str, str]] = None
    secretOptions: Optional[List[SecretTypeDef]] = None

class LogConfigurationTypeDef(BaseModel):
    logDriver: LogDriverType
    options: Optional[Mapping[str, str]] = None
    secretOptions: Optional[Sequence[SecretTypeDef]] = None

class ContainerInstanceHealthStatusTypeDef(BaseModel):
    overallStatus: Optional[InstanceHealthCheckStateType] = None
    details: Optional[List[InstanceHealthCheckResultTypeDef]] = None

class ContainerStateChangeTypeDef(BaseModel):
    containerName: Optional[str] = None
    imageDigest: Optional[str] = None
    runtimeId: Optional[str] = None
    exitCode: Optional[int] = None
    networkBindings: Optional[Sequence[NetworkBindingTypeDef]] = None
    reason: Optional[str] = None
    status: Optional[str] = None

class SubmitContainerStateChangeRequestRequestTypeDef(BaseModel):
    cluster: Optional[str] = None
    task: Optional[str] = None
    containerName: Optional[str] = None
    runtimeId: Optional[str] = None
    status: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    networkBindings: Optional[Sequence[NetworkBindingTypeDef]] = None

class ContainerTypeDef(BaseModel):
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

class DeleteAttributesResponseTypeDef(BaseModel):
    attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DiscoverPollEndpointResponseTypeDef(BaseModel):
    endpoint: str
    telemetryEndpoint: str
    serviceConnectEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttributesResponseTypeDef(BaseModel):
    attributes: List[AttributeTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListClustersResponseTypeDef(BaseModel):
    clusterArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListContainerInstancesResponseTypeDef(BaseModel):
    containerInstanceArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicesByNamespaceResponseTypeDef(BaseModel):
    serviceArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListServicesResponseTypeDef(BaseModel):
    serviceArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTaskDefinitionFamiliesResponseTypeDef(BaseModel):
    families: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTaskDefinitionsResponseTypeDef(BaseModel):
    taskDefinitionArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTasksResponseTypeDef(BaseModel):
    taskArns: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutAttributesResponseTypeDef(BaseModel):
    attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitAttachmentStateChangesResponseTypeDef(BaseModel):
    acknowledgment: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitContainerStateChangeResponseTypeDef(BaseModel):
    acknowledgment: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitTaskStateChangeResponseTypeDef(BaseModel):
    acknowledgment: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTaskSetRequestRequestTypeDef(BaseModel):
    cluster: str
    service: str
    taskSet: str
    scale: ScaleTypeDef

class DeleteAccountSettingResponseTypeDef(BaseModel):
    setting: SettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountSettingsResponseTypeDef(BaseModel):
    settings: List[SettingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutAccountSettingDefaultResponseTypeDef(BaseModel):
    setting: SettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutAccountSettingResponseTypeDef(BaseModel):
    setting: SettingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentConfigurationOutputTypeDef(BaseModel):
    deploymentCircuitBreaker: Optional[DeploymentCircuitBreakerTypeDef] = None
    maximumPercent: Optional[int] = None
    minimumHealthyPercent: Optional[int] = None
    alarms: Optional[DeploymentAlarmsOutputTypeDef] = None

class DeploymentConfigurationTypeDef(BaseModel):
    deploymentCircuitBreaker: Optional[DeploymentCircuitBreakerTypeDef] = None
    maximumPercent: Optional[int] = None
    minimumHealthyPercent: Optional[int] = None
    alarms: Optional[DeploymentAlarmsTypeDef] = None

class DescribeServicesRequestServicesInactiveWaitTypeDef(BaseModel):
    services: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeServicesRequestServicesStableWaitTypeDef(BaseModel):
    services: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTasksRequestTasksRunningWaitTypeDef(BaseModel):
    tasks: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class DescribeTasksRequestTasksStoppedWaitTypeDef(BaseModel):
    tasks: Sequence[str]
    cluster: Optional[str] = None
    include: Optional[Sequence[Literal["TAGS"]]] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class EFSVolumeConfigurationTypeDef(BaseModel):
    fileSystemId: str
    rootDirectory: Optional[str] = None
    transitEncryption: Optional[EFSTransitEncryptionType] = None
    transitEncryptionPort: Optional[int] = None
    authorizationConfig: Optional[EFSAuthorizationConfigTypeDef] = None

class ExecuteCommandConfigurationTypeDef(BaseModel):
    kmsKeyId: Optional[str] = None
    logging: Optional[ExecuteCommandLoggingType] = None
    logConfiguration: Optional[ExecuteCommandLogConfigurationTypeDef] = None

class ExecuteCommandResponseTypeDef(BaseModel):
    clusterArn: str
    containerArn: str
    containerName: str
    interactive: bool
    session: SessionTypeDef
    taskArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class FSxWindowsFileServerVolumeConfigurationTypeDef(BaseModel):
    fileSystemId: str
    rootDirectory: str
    authorizationConfig: FSxWindowsFileServerAuthorizationConfigTypeDef

class GetTaskProtectionResponseTypeDef(BaseModel):
    protectedTasks: List[ProtectedTaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTaskProtectionResponseTypeDef(BaseModel):
    protectedTasks: List[ProtectedTaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class LinuxParametersOutputTypeDef(BaseModel):
    capabilities: Optional[KernelCapabilitiesOutputTypeDef] = None
    devices: Optional[List[DeviceOutputTypeDef]] = None
    initProcessEnabled: Optional[bool] = None
    sharedMemorySize: Optional[int] = None
    tmpfs: Optional[List[TmpfsOutputTypeDef]] = None
    maxSwap: Optional[int] = None
    swappiness: Optional[int] = None

class LinuxParametersTypeDef(BaseModel):
    capabilities: Optional[KernelCapabilitiesTypeDef] = None
    devices: Optional[Sequence[DeviceTypeDef]] = None
    initProcessEnabled: Optional[bool] = None
    sharedMemorySize: Optional[int] = None
    tmpfs: Optional[Sequence[TmpfsTypeDef]] = None
    maxSwap: Optional[int] = None
    swappiness: Optional[int] = None

class ListAccountSettingsRequestListAccountSettingsPaginateTypeDef(BaseModel):
    name: Optional[SettingNameType] = None
    value: Optional[str] = None
    principalArn: Optional[str] = None
    effectiveSettings: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAttributesRequestListAttributesPaginateTypeDef(BaseModel):
    targetType: Literal["container-instance"]
    cluster: Optional[str] = None
    attributeName: Optional[str] = None
    attributeValue: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListClustersRequestListClustersPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContainerInstancesRequestListContainerInstancesPaginateTypeDef(BaseModel):
    cluster: Optional[str] = None
    filter: Optional[str] = None
    status: Optional[ContainerInstanceStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicesByNamespaceRequestListServicesByNamespacePaginateTypeDef(BaseModel):
    namespace: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListServicesRequestListServicesPaginateTypeDef(BaseModel):
    cluster: Optional[str] = None
    launchType: Optional[LaunchTypeType] = None
    schedulingStrategy: Optional[SchedulingStrategyType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTaskDefinitionFamiliesRequestListTaskDefinitionFamiliesPaginateTypeDef(BaseModel):
    familyPrefix: Optional[str] = None
    status: Optional[TaskDefinitionFamilyStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTaskDefinitionsRequestListTaskDefinitionsPaginateTypeDef(BaseModel):
    familyPrefix: Optional[str] = None
    status: Optional[TaskDefinitionStatusType] = None
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTasksRequestListTasksPaginateTypeDef(BaseModel):
    cluster: Optional[str] = None
    containerInstance: Optional[str] = None
    family: Optional[str] = None
    startedBy: Optional[str] = None
    serviceName: Optional[str] = None
    desiredStatus: Optional[DesiredStatusType] = None
    launchType: Optional[LaunchTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ServiceConnectTlsConfigurationTypeDef(BaseModel):
    issuerCertificateAuthority: ServiceConnectTlsCertificateAuthorityTypeDef
    kmsKey: Optional[str] = None
    roleArn: Optional[str] = None

class CapacityProviderTypeDef(BaseModel):
    capacityProviderArn: Optional[str] = None
    name: Optional[str] = None
    status: Optional[CapacityProviderStatusType] = None
    autoScalingGroupProvider: Optional[AutoScalingGroupProviderTypeDef] = None
    updateStatus: Optional[CapacityProviderUpdateStatusType] = None
    updateStatusReason: Optional[str] = None
    tags: Optional[List[TagTypeDef]] = None

class CreateCapacityProviderRequestRequestTypeDef(BaseModel):
    name: str
    autoScalingGroupProvider: AutoScalingGroupProviderTypeDef
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateCapacityProviderRequestRequestTypeDef(BaseModel):
    name: str
    autoScalingGroupProvider: AutoScalingGroupProviderUpdateTypeDef

class TaskSetTypeDef(BaseModel):
    id: Optional[str] = None
    taskSetArn: Optional[str] = None
    serviceArn: Optional[str] = None
    clusterArn: Optional[str] = None
    startedBy: Optional[str] = None
    externalId: Optional[str] = None
    status: Optional[str] = None
    taskDefinition: Optional[str] = None
    computedDesiredCount: Optional[int] = None
    pendingCount: Optional[int] = None
    runningCount: Optional[int] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    launchType: Optional[LaunchTypeType] = None
    capacityProviderStrategy: Optional[List[CapacityProviderStrategyItemTypeDef]] = None
    platformVersion: Optional[str] = None
    platformFamily: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationOutputTypeDef] = None
    loadBalancers: Optional[List[LoadBalancerTypeDef]] = None
    serviceRegistries: Optional[List[ServiceRegistryTypeDef]] = None
    scale: Optional[ScaleTypeDef] = None
    stabilityStatus: Optional[StabilityStatusType] = None
    stabilityStatusAt: Optional[datetime] = None
    tags: Optional[List[TagTypeDef]] = None
    fargateEphemeralStorage: Optional[DeploymentEphemeralStorageTypeDef] = None

class CreateTaskSetRequestRequestTypeDef(BaseModel):
    service: str
    cluster: str
    taskDefinition: str
    externalId: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    loadBalancers: Optional[Sequence[LoadBalancerTypeDef]] = None
    serviceRegistries: Optional[Sequence[ServiceRegistryTypeDef]] = None
    launchType: Optional[LaunchTypeType] = None
    capacityProviderStrategy: Optional[Sequence[CapacityProviderStrategyItemTypeDef]] = None
    platformVersion: Optional[str] = None
    scale: Optional[ScaleTypeDef] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ServiceManagedEBSVolumeConfigurationOutputTypeDef(BaseModel):
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

class ServiceManagedEBSVolumeConfigurationTypeDef(BaseModel):
    roleArn: str
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None
    volumeType: Optional[str] = None
    sizeInGiB: Optional[int] = None
    snapshotId: Optional[str] = None
    iops: Optional[int] = None
    throughput: Optional[int] = None
    tagSpecifications: Optional[Sequence[EBSTagSpecificationTypeDef]] = None
    filesystemType: Optional[TaskFilesystemTypeType] = None

class TaskManagedEBSVolumeConfigurationTypeDef(BaseModel):
    roleArn: str
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None
    volumeType: Optional[str] = None
    sizeInGiB: Optional[int] = None
    snapshotId: Optional[str] = None
    iops: Optional[int] = None
    throughput: Optional[int] = None
    tagSpecifications: Optional[Sequence[EBSTagSpecificationTypeDef]] = None
    terminationPolicy: Optional[TaskManagedEBSVolumeTerminationPolicyTypeDef] = None
    filesystemType: Optional[TaskFilesystemTypeType] = None

class TaskOverrideOutputTypeDef(BaseModel):
    containerOverrides: Optional[List[ContainerOverrideOutputTypeDef]] = None
    cpu: Optional[str] = None
    inferenceAcceleratorOverrides: Optional[List[InferenceAcceleratorOverrideTypeDef]] = None
    executionRoleArn: Optional[str] = None
    memory: Optional[str] = None
    taskRoleArn: Optional[str] = None
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None

class TaskOverrideTypeDef(BaseModel):
    containerOverrides: Optional[Sequence[ContainerOverrideTypeDef]] = None
    cpu: Optional[str] = None
    inferenceAcceleratorOverrides: Optional[Sequence[InferenceAcceleratorOverrideTypeDef]] = None
    executionRoleArn: Optional[str] = None
    memory: Optional[str] = None
    taskRoleArn: Optional[str] = None
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None

class ContainerInstanceTypeDef(BaseModel):
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

class SubmitTaskStateChangeRequestRequestTypeDef(BaseModel):
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

class ClusterConfigurationTypeDef(BaseModel):
    executeCommandConfiguration: Optional[ExecuteCommandConfigurationTypeDef] = None
    managedStorageConfiguration: Optional[ManagedStorageConfigurationTypeDef] = None

class VolumeOutputTypeDef(BaseModel):
    name: Optional[str] = None
    host: Optional[HostVolumePropertiesTypeDef] = None
    dockerVolumeConfiguration: Optional[DockerVolumeConfigurationOutputTypeDef] = None
    efsVolumeConfiguration: Optional[EFSVolumeConfigurationTypeDef] = None
    fsxWindowsFileServerVolumeConfiguration: Optional[       FSxWindowsFileServerVolumeConfigurationTypeDef     ] = None
    configuredAtLaunch: Optional[bool] = None

class VolumeTypeDef(BaseModel):
    name: Optional[str] = None
    host: Optional[HostVolumePropertiesTypeDef] = None
    dockerVolumeConfiguration: Optional[DockerVolumeConfigurationTypeDef] = None
    efsVolumeConfiguration: Optional[EFSVolumeConfigurationTypeDef] = None
    fsxWindowsFileServerVolumeConfiguration: Optional[       FSxWindowsFileServerVolumeConfigurationTypeDef     ] = None
    configuredAtLaunch: Optional[bool] = None

class ContainerDefinitionOutputTypeDef(BaseModel):
    name: Optional[str] = None
    image: Optional[str] = None
    repositoryCredentials: Optional[RepositoryCredentialsTypeDef] = None
    cpu: Optional[int] = None
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None
    links: Optional[List[str]] = None
    portMappings: Optional[List[PortMappingTypeDef]] = None
    essential: Optional[bool] = None
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

class ContainerDefinitionTypeDef(BaseModel):
    name: Optional[str] = None
    image: Optional[str] = None
    repositoryCredentials: Optional[RepositoryCredentialsTypeDef] = None
    cpu: Optional[int] = None
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None
    links: Optional[Sequence[str]] = None
    portMappings: Optional[Sequence[PortMappingTypeDef]] = None
    essential: Optional[bool] = None
    entryPoint: Optional[Sequence[str]] = None
    command: Optional[Sequence[str]] = None
    environment: Optional[Sequence[KeyValuePairTypeDef]] = None
    environmentFiles: Optional[Sequence[EnvironmentFileTypeDef]] = None
    mountPoints: Optional[Sequence[MountPointTypeDef]] = None
    volumesFrom: Optional[Sequence[VolumeFromTypeDef]] = None
    linuxParameters: Optional[LinuxParametersTypeDef] = None
    secrets: Optional[Sequence[SecretTypeDef]] = None
    dependsOn: Optional[Sequence[ContainerDependencyTypeDef]] = None
    startTimeout: Optional[int] = None
    stopTimeout: Optional[int] = None
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
    logConfiguration: Optional[LogConfigurationTypeDef] = None
    healthCheck: Optional[HealthCheckTypeDef] = None
    systemControls: Optional[Sequence[SystemControlTypeDef]] = None
    resourceRequirements: Optional[Sequence[ResourceRequirementTypeDef]] = None
    firelensConfiguration: Optional[FirelensConfigurationTypeDef] = None
    credentialSpecs: Optional[Sequence[str]] = None

class RegisterContainerInstanceRequestRequestTypeDef(BaseModel):
    cluster: Optional[str] = None
    instanceIdentityDocument: Optional[str] = None
    instanceIdentityDocumentSignature: Optional[str] = None
    totalResources: Optional[Sequence[ResourceUnionTypeDef]] = None
    versionInfo: Optional[VersionInfoTypeDef] = None
    containerInstanceArn: Optional[str] = None
    attributes: Optional[Sequence[AttributeTypeDef]] = None
    platformDevices: Optional[Sequence[PlatformDeviceTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ServiceConnectServiceOutputTypeDef(BaseModel):
    portName: str
    discoveryName: Optional[str] = None
    clientAliases: Optional[List[ServiceConnectClientAliasTypeDef]] = None
    ingressPortOverride: Optional[int] = None
    timeout: Optional[TimeoutConfigurationTypeDef] = None
    tls: Optional[ServiceConnectTlsConfigurationTypeDef] = None

class ServiceConnectServiceTypeDef(BaseModel):
    portName: str
    discoveryName: Optional[str] = None
    clientAliases: Optional[Sequence[ServiceConnectClientAliasTypeDef]] = None
    ingressPortOverride: Optional[int] = None
    timeout: Optional[TimeoutConfigurationTypeDef] = None
    tls: Optional[ServiceConnectTlsConfigurationTypeDef] = None

class CreateCapacityProviderResponseTypeDef(BaseModel):
    capacityProvider: CapacityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCapacityProviderResponseTypeDef(BaseModel):
    capacityProvider: CapacityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCapacityProvidersResponseTypeDef(BaseModel):
    capacityProviders: List[CapacityProviderTypeDef]
    failures: List[FailureTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCapacityProviderResponseTypeDef(BaseModel):
    capacityProvider: CapacityProviderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskSetResponseTypeDef(BaseModel):
    taskSet: TaskSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTaskSetResponseTypeDef(BaseModel):
    taskSet: TaskSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTaskSetsResponseTypeDef(BaseModel):
    taskSets: List[TaskSetTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServicePrimaryTaskSetResponseTypeDef(BaseModel):
    taskSet: TaskSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTaskSetResponseTypeDef(BaseModel):
    taskSet: TaskSetTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ServiceVolumeConfigurationOutputTypeDef(BaseModel):
    name: str
    managedEBSVolume: Optional[ServiceManagedEBSVolumeConfigurationOutputTypeDef] = None

class ServiceVolumeConfigurationTypeDef(BaseModel):
    name: str
    managedEBSVolume: Optional[ServiceManagedEBSVolumeConfigurationTypeDef] = None

class TaskVolumeConfigurationTypeDef(BaseModel):
    name: str
    managedEBSVolume: Optional[TaskManagedEBSVolumeConfigurationTypeDef] = None

class TaskTypeDef(BaseModel):
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

class DeregisterContainerInstanceResponseTypeDef(BaseModel):
    containerInstance: ContainerInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeContainerInstancesResponseTypeDef(BaseModel):
    containerInstances: List[ContainerInstanceTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterContainerInstanceResponseTypeDef(BaseModel):
    containerInstance: ContainerInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContainerAgentResponseTypeDef(BaseModel):
    containerInstance: ContainerInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContainerInstancesStateResponseTypeDef(BaseModel):
    containerInstances: List[ContainerInstanceTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ClusterTypeDef(BaseModel):
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

class CreateClusterRequestRequestTypeDef(BaseModel):
    clusterName: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    settings: Optional[Sequence[ClusterSettingTypeDef]] = None
    configuration: Optional[ClusterConfigurationTypeDef] = None
    capacityProviders: Optional[Sequence[str]] = None
    defaultCapacityProviderStrategy: Optional[       Sequence[CapacityProviderStrategyItemTypeDef]     ] = None
    serviceConnectDefaults: Optional[ClusterServiceConnectDefaultsRequestTypeDef] = None

class UpdateClusterRequestRequestTypeDef(BaseModel):
    cluster: str
    settings: Optional[Sequence[ClusterSettingTypeDef]] = None
    configuration: Optional[ClusterConfigurationTypeDef] = None
    serviceConnectDefaults: Optional[ClusterServiceConnectDefaultsRequestTypeDef] = None

class TaskDefinitionTypeDef(BaseModel):
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

class ServiceConnectConfigurationOutputTypeDef(BaseModel):
    enabled: bool
    namespace: Optional[str] = None
    services: Optional[List[ServiceConnectServiceOutputTypeDef]] = None
    logConfiguration: Optional[LogConfigurationOutputTypeDef] = None

class ServiceConnectConfigurationTypeDef(BaseModel):
    enabled: bool
    namespace: Optional[str] = None
    services: Optional[Sequence[ServiceConnectServiceTypeDef]] = None
    logConfiguration: Optional[LogConfigurationTypeDef] = None

class RunTaskRequestRequestTypeDef(BaseModel):
    taskDefinition: str
    capacityProviderStrategy: Optional[Sequence[CapacityProviderStrategyItemTypeDef]] = None
    cluster: Optional[str] = None
    count: Optional[int] = None
    enableECSManagedTags: Optional[bool] = None
    enableExecuteCommand: Optional[bool] = None
    group: Optional[str] = None
    launchType: Optional[LaunchTypeType] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    overrides: Optional[TaskOverrideTypeDef] = None
    placementConstraints: Optional[Sequence[PlacementConstraintTypeDef]] = None
    placementStrategy: Optional[Sequence[PlacementStrategyTypeDef]] = None
    platformVersion: Optional[str] = None
    propagateTags: Optional[PropagateTagsType] = None
    referenceId: Optional[str] = None
    startedBy: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    clientToken: Optional[str] = None
    volumeConfigurations: Optional[Sequence[TaskVolumeConfigurationTypeDef]] = None

class StartTaskRequestRequestTypeDef(BaseModel):
    containerInstances: Sequence[str]
    taskDefinition: str
    cluster: Optional[str] = None
    enableECSManagedTags: Optional[bool] = None
    enableExecuteCommand: Optional[bool] = None
    group: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    overrides: Optional[TaskOverrideTypeDef] = None
    propagateTags: Optional[PropagateTagsType] = None
    referenceId: Optional[str] = None
    startedBy: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    volumeConfigurations: Optional[Sequence[TaskVolumeConfigurationTypeDef]] = None

class DescribeTasksResponseTypeDef(BaseModel):
    tasks: List[TaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RunTaskResponseTypeDef(BaseModel):
    tasks: List[TaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartTaskResponseTypeDef(BaseModel):
    tasks: List[TaskTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StopTaskResponseTypeDef(BaseModel):
    task: TaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateClusterResponseTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteClusterResponseTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeClustersResponseTypeDef(BaseModel):
    clusters: List[ClusterTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutClusterCapacityProvidersResponseTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterResponseTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateClusterSettingsResponseTypeDef(BaseModel):
    cluster: ClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTaskDefinitionsResponseTypeDef(BaseModel):
    taskDefinitions: List[TaskDefinitionTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeregisterTaskDefinitionResponseTypeDef(BaseModel):
    taskDefinition: TaskDefinitionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTaskDefinitionResponseTypeDef(BaseModel):
    taskDefinition: TaskDefinitionTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTaskDefinitionResponseTypeDef(BaseModel):
    taskDefinition: TaskDefinitionTypeDef
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RegisterTaskDefinitionRequestRequestTypeDef(BaseModel):
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
    proxyConfiguration: Optional[ProxyConfigurationTypeDef] = None
    inferenceAccelerators: Optional[Sequence[InferenceAcceleratorTypeDef]] = None
    ephemeralStorage: Optional[EphemeralStorageTypeDef] = None
    runtimePlatform: Optional[RuntimePlatformTypeDef] = None

class DeploymentTypeDef(BaseModel):
    id: Optional[str] = None
    status: Optional[str] = None
    taskDefinition: Optional[str] = None
    desiredCount: Optional[int] = None
    pendingCount: Optional[int] = None
    runningCount: Optional[int] = None
    failedTasks: Optional[int] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    capacityProviderStrategy: Optional[List[CapacityProviderStrategyItemTypeDef]] = None
    launchType: Optional[LaunchTypeType] = None
    platformVersion: Optional[str] = None
    platformFamily: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationOutputTypeDef] = None
    rolloutState: Optional[DeploymentRolloutStateType] = None
    rolloutStateReason: Optional[str] = None
    serviceConnectConfiguration: Optional[ServiceConnectConfigurationOutputTypeDef] = None
    serviceConnectResources: Optional[List[ServiceConnectServiceResourceTypeDef]] = None
    volumeConfigurations: Optional[List[ServiceVolumeConfigurationOutputTypeDef]] = None
    fargateEphemeralStorage: Optional[DeploymentEphemeralStorageTypeDef] = None

class CreateServiceRequestRequestTypeDef(BaseModel):
    serviceName: str
    cluster: Optional[str] = None
    taskDefinition: Optional[str] = None
    loadBalancers: Optional[Sequence[LoadBalancerTypeDef]] = None
    serviceRegistries: Optional[Sequence[ServiceRegistryTypeDef]] = None
    desiredCount: Optional[int] = None
    clientToken: Optional[str] = None
    launchType: Optional[LaunchTypeType] = None
    capacityProviderStrategy: Optional[Sequence[CapacityProviderStrategyItemTypeDef]] = None
    platformVersion: Optional[str] = None
    role: Optional[str] = None
    deploymentConfiguration: Optional[DeploymentConfigurationTypeDef] = None
    placementConstraints: Optional[Sequence[PlacementConstraintTypeDef]] = None
    placementStrategy: Optional[Sequence[PlacementStrategyTypeDef]] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
    healthCheckGracePeriodSeconds: Optional[int] = None
    schedulingStrategy: Optional[SchedulingStrategyType] = None
    deploymentController: Optional[DeploymentControllerTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    enableECSManagedTags: Optional[bool] = None
    propagateTags: Optional[PropagateTagsType] = None
    enableExecuteCommand: Optional[bool] = None
    serviceConnectConfiguration: Optional[ServiceConnectConfigurationTypeDef] = None
    volumeConfigurations: Optional[Sequence[ServiceVolumeConfigurationUnionTypeDef]] = None

class UpdateServiceRequestRequestTypeDef(BaseModel):
    service: str
    cluster: Optional[str] = None
    desiredCount: Optional[int] = None
    taskDefinition: Optional[str] = None
    capacityProviderStrategy: Optional[Sequence[CapacityProviderStrategyItemTypeDef]] = None
    deploymentConfiguration: Optional[DeploymentConfigurationTypeDef] = None
    networkConfiguration: Optional[NetworkConfigurationTypeDef] = None
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
    serviceConnectConfiguration: Optional[ServiceConnectConfigurationTypeDef] = None
    volumeConfigurations: Optional[Sequence[ServiceVolumeConfigurationUnionTypeDef]] = None

class ServiceTypeDef(BaseModel):
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

class CreateServiceResponseTypeDef(BaseModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteServiceResponseTypeDef(BaseModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeServicesResponseTypeDef(BaseModel):
    services: List[ServiceTypeDef]
    failures: List[FailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateServiceResponseTypeDef(BaseModel):
    service: ServiceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

