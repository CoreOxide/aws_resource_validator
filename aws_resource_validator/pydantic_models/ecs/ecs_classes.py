from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ecs.ecs_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AttachmentStateChange(BaseValidatorModel):
    attachmentArn: str
    status: str


class KeyValuePair(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None


class Attribute(BaseValidatorModel):
    name: str
    value: Optional[str] = None
    targetType: Optional[Literal['container-instance']] = None
    targetId: Optional[str] = None


class ManagedScaling(BaseValidatorModel):
    status: Optional[ManagedScalingStatusType] = None
    targetCapacity: Optional[int] = None
    minimumScalingStepSize: Optional[int] = None
    maximumScalingStepSize: Optional[int] = None
    instanceWarmupPeriod: Optional[int] = None


class AwsVpcConfigurationOutput(BaseValidatorModel):
    subnets: List[str]
    securityGroups: Optional[List[str]] = None
    assignPublicIp: Optional[AssignPublicIpType] = None


class AwsVpcConfiguration(BaseValidatorModel):
    subnets: List[str]
    securityGroups: Optional[List[str]] = None
    assignPublicIp: Optional[AssignPublicIpType] = None


class CapacityProviderStrategyItem(BaseValidatorModel):
    capacityProvider: str
    weight: Optional[int] = None
    base: Optional[int] = None


class Tag(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class ManagedStorageConfiguration(BaseValidatorModel):
    kmsKeyId: Optional[str] = None
    fargateEphemeralStorageKmsKeyId: Optional[str] = None


class ClusterServiceConnectDefaultsRequest(BaseValidatorModel):
    namespace: str


class ClusterServiceConnectDefaults(BaseValidatorModel):
    namespace: Optional[str] = None


class ClusterSetting(BaseValidatorModel):
    name: Optional[Literal['containerInsights']] = None
    value: Optional[str] = None


class ContainerDependency(BaseValidatorModel):
    containerName: str
    condition: ContainerConditionType


class ContainerRestartPolicyOutput(BaseValidatorModel):
    enabled: bool
    ignoredExitCodes: Optional[List[int]] = None
    restartAttemptPeriod: Optional[int] = None


class EnvironmentFile(BaseValidatorModel):
    value: str
    type: Literal['s3']


class FirelensConfigurationOutput(BaseValidatorModel):
    type: FirelensConfigurationTypeType
    options: Optional[Dict[str, str]] = None


class HealthCheckOutput(BaseValidatorModel):
    command: List[str]
    interval: Optional[int] = None
    timeout: Optional[int] = None
    retries: Optional[int] = None
    startPeriod: Optional[int] = None


class HostEntry(BaseValidatorModel):
    hostname: str
    ipAddress: str


class MountPoint(BaseValidatorModel):
    sourceVolume: Optional[str] = None
    containerPath: Optional[str] = None
    readOnly: Optional[bool] = None


class PortMapping(BaseValidatorModel):
    containerPort: Optional[int] = None
    hostPort: Optional[int] = None
    protocol: Optional[TransportProtocolType] = None
    name: Optional[str] = None
    appProtocol: Optional[ApplicationProtocolType] = None
    containerPortRange: Optional[str] = None


class RepositoryCredentials(BaseValidatorModel):
    credentialsParameter: str


class ResourceRequirement(BaseValidatorModel):
    value: str
    type: ResourceTypeType


class Secret(BaseValidatorModel):
    name: str
    valueFrom: str


class SystemControl(BaseValidatorModel):
    namespace: Optional[str] = None
    value: Optional[str] = None


class Ulimit(BaseValidatorModel):
    name: UlimitNameType
    softLimit: int
    hardLimit: int


class VolumeFrom(BaseValidatorModel):
    sourceContainer: Optional[str] = None
    readOnly: Optional[bool] = None


class ContainerImage(BaseValidatorModel):
    containerName: Optional[str] = None
    imageDigest: Optional[str] = None
    image: Optional[str] = None


class InstanceHealthCheckResult(BaseValidatorModel):
    type: Optional[Literal['CONTAINER_RUNTIME']] = None
    status: Optional[InstanceHealthCheckStateType] = None
    lastUpdated: Optional[datetime] = None
    lastStatusChange: Optional[datetime] = None


class ResourceOutput(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[str] = None
    doubleValue: Optional[float] = None
    longValue: Optional[int] = None
    integerValue: Optional[int] = None
    stringSetValue: Optional[List[str]] = None


class VersionInfo(BaseValidatorModel):
    agentVersion: Optional[str] = None
    agentHash: Optional[str] = None
    dockerVersion: Optional[str] = None


class ContainerRestartPolicy(BaseValidatorModel):
    enabled: bool
    ignoredExitCodes: Optional[List[int]] = None
    restartAttemptPeriod: Optional[int] = None


class NetworkBinding(BaseValidatorModel):
    bindIP: Optional[str] = None
    containerPort: Optional[int] = None
    hostPort: Optional[int] = None
    protocol: Optional[TransportProtocolType] = None
    containerPortRange: Optional[str] = None
    hostPortRange: Optional[str] = None


class ManagedAgent(BaseValidatorModel):
    lastStartedAt: Optional[datetime] = None
    name: Optional[Literal['ExecuteCommandAgent']] = None
    reason: Optional[str] = None
    lastStatus: Optional[str] = None


class NetworkInterface(BaseValidatorModel):
    attachmentId: Optional[str] = None
    privateIpv4Address: Optional[str] = None
    ipv6Address: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class DeploymentController(BaseValidatorModel):
    type: DeploymentControllerTypeType


class LoadBalancer(BaseValidatorModel):
    targetGroupArn: Optional[str] = None
    loadBalancerName: Optional[str] = None
    containerName: Optional[str] = None
    containerPort: Optional[int] = None


class PlacementConstraint(BaseValidatorModel):
    type: Optional[PlacementConstraintTypeType] = None
    expression: Optional[str] = None


class PlacementStrategy(BaseValidatorModel):
    type: Optional[PlacementStrategyTypeType] = None
    field: Optional[str] = None


class ServiceRegistry(BaseValidatorModel):
    registryArn: Optional[str] = None
    port: Optional[int] = None
    containerName: Optional[str] = None
    containerPort: Optional[int] = None


class VpcLatticeConfiguration(BaseValidatorModel):
    roleArn: str
    targetGroupArn: str
    portName: str


class Scale(BaseValidatorModel):
    value: Optional[float] = None
    unit: Optional[Literal['PERCENT']] = None

Timestamp = Union[datetime, str]


# This class is the input for the 'delete_account_setting' function.
class DeleteAccountSettingRequest(BaseValidatorModel):
    name: SettingNameType
    principalArn: Optional[str] = None


class Setting(BaseValidatorModel):
    name: Optional[SettingNameType] = None
    value: Optional[str] = None
    principalArn: Optional[str] = None
    type: Optional[SettingTypeType] = None


# This class is the input for the 'delete_capacity_provider' function.
class DeleteCapacityProviderRequest(BaseValidatorModel):
    capacityProvider: str


# This class is the input for the 'delete_cluster' function.
class DeleteClusterRequest(BaseValidatorModel):
    cluster: str


# This class is the input for the 'delete_service' function.
class DeleteServiceRequest(BaseValidatorModel):
    service: str
    cluster: Optional[str] = None
    force: Optional[bool] = None


# This class is the input for the 'delete_task_definitions' function.
class DeleteTaskDefinitionsRequest(BaseValidatorModel):
    taskDefinitions: List[str]


class Failure(BaseValidatorModel):
    arn: Optional[str] = None
    reason: Optional[str] = None
    detail: Optional[str] = None


# This class is the input for the 'delete_task_set' function.
class DeleteTaskSetRequest(BaseValidatorModel):
    cluster: str
    service: str
    taskSet: str
    force: Optional[bool] = None


class DeploymentAlarmsOutput(BaseValidatorModel):
    alarmNames: List[str]
    rollback: bool
    enable: bool


class DeploymentAlarms(BaseValidatorModel):
    alarmNames: List[str]
    rollback: bool
    enable: bool


class DeploymentCircuitBreaker(BaseValidatorModel):
    enable: bool
    rollback: bool


class DeploymentEphemeralStorage(BaseValidatorModel):
    kmsKeyId: Optional[str] = None


class ServiceConnectServiceResource(BaseValidatorModel):
    discoveryName: Optional[str] = None
    discoveryArn: Optional[str] = None


# This class is the input for the 'deregister_container_instance' function.
class DeregisterContainerInstanceRequest(BaseValidatorModel):
    containerInstance: str
    cluster: Optional[str] = None
    force: Optional[bool] = None


# This class is the input for the 'deregister_task_definition' function.
class DeregisterTaskDefinitionRequest(BaseValidatorModel):
    taskDefinition: str


# This class is the input for the 'describe_capacity_providers' function.
class DescribeCapacityProvidersRequest(BaseValidatorModel):
    capacityProviders: Optional[List[str]] = None
    include: Optional[List[Literal['TAGS']]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'describe_clusters' function.
class DescribeClustersRequest(BaseValidatorModel):
    clusters: Optional[List[str]] = None
    include: Optional[List[ClusterFieldType]] = None


# This class is the input for the 'describe_container_instances' function.
class DescribeContainerInstancesRequest(BaseValidatorModel):
    containerInstances: List[str]
    cluster: Optional[str] = None
    include: Optional[List[ContainerInstanceFieldType]] = None


# This class is the input for the 'describe_service_deployments' function.
class DescribeServiceDeploymentsRequest(BaseValidatorModel):
    serviceDeploymentArns: List[str]


# This class is the input for the 'describe_service_revisions' function.
class DescribeServiceRevisionsRequest(BaseValidatorModel):
    serviceRevisionArns: List[str]


# This class is the input for the 'describe_services' function.
class DescribeServicesRequest(BaseValidatorModel):
    services: List[str]
    cluster: Optional[str] = None
    include: Optional[List[Literal['TAGS']]] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


# This class is the input for the 'describe_task_definition' function.
class DescribeTaskDefinitionRequest(BaseValidatorModel):
    taskDefinition: str
    include: Optional[List[Literal['TAGS']]] = None


# This class is the input for the 'describe_task_sets' function.
class DescribeTaskSetsRequest(BaseValidatorModel):
    cluster: str
    service: str
    taskSets: Optional[List[str]] = None
    include: Optional[List[Literal['TAGS']]] = None


# This class is the input for the 'describe_tasks' function.
class DescribeTasksRequest(BaseValidatorModel):
    tasks: List[str]
    cluster: Optional[str] = None
    include: Optional[List[Literal['TAGS']]] = None


class DeviceOutput(BaseValidatorModel):
    hostPath: str
    containerPath: Optional[str] = None
    permissions: Optional[List[DeviceCgroupPermissionType]] = None


class Device(BaseValidatorModel):
    hostPath: str
    containerPath: Optional[str] = None
    permissions: Optional[List[DeviceCgroupPermissionType]] = None


# This class is the input for the 'discover_poll_endpoint' function.
class DiscoverPollEndpointRequest(BaseValidatorModel):
    containerInstance: Optional[str] = None
    cluster: Optional[str] = None


class DockerVolumeConfigurationOutput(BaseValidatorModel):
    scope: Optional[ScopeType] = None
    autoprovision: Optional[bool] = None
    driver: Optional[str] = None
    driverOpts: Optional[Dict[str, str]] = None
    labels: Optional[Dict[str, str]] = None


class DockerVolumeConfiguration(BaseValidatorModel):
    scope: Optional[ScopeType] = None
    autoprovision: Optional[bool] = None
    driver: Optional[str] = None
    driverOpts: Optional[Dict[str, str]] = None
    labels: Optional[Dict[str, str]] = None


class EFSAuthorizationConfig(BaseValidatorModel):
    accessPointId: Optional[str] = None
    iam: Optional[EFSAuthorizationConfigIAMType] = None


class EphemeralStorage(BaseValidatorModel):
    sizeInGiB: int


class ExecuteCommandLogConfiguration(BaseValidatorModel):
    cloudWatchLogGroupName: Optional[str] = None
    cloudWatchEncryptionEnabled: Optional[bool] = None
    s3BucketName: Optional[str] = None
    s3EncryptionEnabled: Optional[bool] = None
    s3KeyPrefix: Optional[str] = None


# This class is the input for the 'execute_command' function.
class ExecuteCommandRequest(BaseValidatorModel):
    command: str
    interactive: bool
    task: str
    cluster: Optional[str] = None
    container: Optional[str] = None


class Session(BaseValidatorModel):
    sessionId: Optional[str] = None
    streamUrl: Optional[str] = None
    tokenValue: Optional[str] = None


class FSxWindowsFileServerAuthorizationConfig(BaseValidatorModel):
    credentialsParameter: str
    domain: str


class FirelensConfiguration(BaseValidatorModel):
    type: FirelensConfigurationTypeType
    options: Optional[Dict[str, str]] = None


# This class is the input for the 'get_task_protection' function.
class GetTaskProtectionRequest(BaseValidatorModel):
    cluster: str
    tasks: Optional[List[str]] = None


class ProtectedTask(BaseValidatorModel):
    taskArn: Optional[str] = None
    protectionEnabled: Optional[bool] = None
    expirationDate: Optional[datetime] = None


class HealthCheck(BaseValidatorModel):
    command: List[str]
    interval: Optional[int] = None
    timeout: Optional[int] = None
    retries: Optional[int] = None
    startPeriod: Optional[int] = None


class HostVolumeProperties(BaseValidatorModel):
    sourcePath: Optional[str] = None


class InferenceAcceleratorOverride(BaseValidatorModel):
    deviceName: Optional[str] = None
    deviceType: Optional[str] = None


class InferenceAccelerator(BaseValidatorModel):
    deviceName: str
    deviceType: str


class KernelCapabilitiesOutput(BaseValidatorModel):
    add: Optional[List[str]] = None
    drop: Optional[List[str]] = None


class KernelCapabilities(BaseValidatorModel):
    add: Optional[List[str]] = None
    drop: Optional[List[str]] = None


class TmpfsOutput(BaseValidatorModel):
    containerPath: str
    size: int
    mountOptions: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_account_settings' function.
class ListAccountSettingsRequest(BaseValidatorModel):
    name: Optional[SettingNameType] = None
    value: Optional[str] = None
    principalArn: Optional[str] = None
    effectiveSettings: Optional[bool] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_attributes' function.
class ListAttributesRequest(BaseValidatorModel):
    targetType: Literal['container-instance']
    cluster: Optional[str] = None
    attributeName: Optional[str] = None
    attributeValue: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_clusters' function.
class ListClustersRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_container_instances' function.
class ListContainerInstancesRequest(BaseValidatorModel):
    cluster: Optional[str] = None
    filter: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    status: Optional[ContainerInstanceStatusType] = None


class ServiceDeploymentBrief(BaseValidatorModel):
    serviceDeploymentArn: Optional[str] = None
    serviceArn: Optional[str] = None
    clusterArn: Optional[str] = None
    startedAt: Optional[datetime] = None
    createdAt: Optional[datetime] = None
    finishedAt: Optional[datetime] = None
    targetServiceRevisionArn: Optional[str] = None
    status: Optional[ServiceDeploymentStatusType] = None
    statusReason: Optional[str] = None


# This class is the input for the 'list_services_by_namespace' function.
class ListServicesByNamespaceRequest(BaseValidatorModel):
    namespace: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_services' function.
class ListServicesRequest(BaseValidatorModel):
    cluster: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    launchType: Optional[LaunchTypeType] = None
    schedulingStrategy: Optional[SchedulingStrategyType] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_task_definition_families' function.
class ListTaskDefinitionFamiliesRequest(BaseValidatorModel):
    familyPrefix: Optional[str] = None
    status: Optional[TaskDefinitionFamilyStatusType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_task_definitions' function.
class ListTaskDefinitionsRequest(BaseValidatorModel):
    familyPrefix: Optional[str] = None
    status: Optional[TaskDefinitionStatusType] = None
    sort: Optional[SortOrderType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_tasks' function.
class ListTasksRequest(BaseValidatorModel):
    cluster: Optional[str] = None
    containerInstance: Optional[str] = None
    family: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    startedBy: Optional[str] = None
    serviceName: Optional[str] = None
    desiredStatus: Optional[DesiredStatusType] = None
    launchType: Optional[LaunchTypeType] = None


class ManagedAgentStateChange(BaseValidatorModel):
    containerName: str
    managedAgentName: Literal['ExecuteCommandAgent']
    status: str
    reason: Optional[str] = None


class PlatformDevice(BaseValidatorModel):
    id: str
    type: Literal['GPU']


# This class is the input for the 'put_account_setting_default' function.
class PutAccountSettingDefaultRequest(BaseValidatorModel):
    name: SettingNameType
    value: str


# This class is the input for the 'put_account_setting' function.
class PutAccountSettingRequest(BaseValidatorModel):
    name: SettingNameType
    value: str
    principalArn: Optional[str] = None


class RuntimePlatform(BaseValidatorModel):
    cpuArchitecture: Optional[CPUArchitectureType] = None
    operatingSystemFamily: Optional[OSFamilyType] = None


class TaskDefinitionPlacementConstraint(BaseValidatorModel):
    type: Optional[Literal['memberOf']] = None
    expression: Optional[str] = None


class Resource(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[str] = None
    doubleValue: Optional[float] = None
    longValue: Optional[int] = None
    integerValue: Optional[int] = None
    stringSetValue: Optional[List[str]] = None


class Rollback(BaseValidatorModel):
    reason: Optional[str] = None
    startedAt: Optional[datetime] = None
    serviceRevisionArn: Optional[str] = None


class ServiceConnectClientAlias(BaseValidatorModel):
    port: int
    dnsName: Optional[str] = None


class TimeoutConfiguration(BaseValidatorModel):
    idleTimeoutSeconds: Optional[int] = None
    perRequestTimeoutSeconds: Optional[int] = None


class ServiceConnectTlsCertificateAuthority(BaseValidatorModel):
    awsPcaAuthorityArn: Optional[str] = None


class ServiceDeploymentAlarms(BaseValidatorModel):
    status: Optional[ServiceDeploymentRollbackMonitorsStatusType] = None
    alarmNames: Optional[List[str]] = None
    triggeredAlarmNames: Optional[List[str]] = None


class ServiceDeploymentCircuitBreaker(BaseValidatorModel):
    status: Optional[ServiceDeploymentRollbackMonitorsStatusType] = None
    failureCount: Optional[int] = None
    threshold: Optional[int] = None


class ServiceRevisionSummary(BaseValidatorModel):
    arn: Optional[str] = None
    requestedTaskCount: Optional[int] = None
    runningTaskCount: Optional[int] = None
    pendingTaskCount: Optional[int] = None


class ServiceEvent(BaseValidatorModel):
    id: Optional[str] = None
    createdAt: Optional[datetime] = None
    message: Optional[str] = None


# This class is the input for the 'stop_task' function.
class StopTaskRequest(BaseValidatorModel):
    task: str
    cluster: Optional[str] = None
    reason: Optional[str] = None


class TaskEphemeralStorage(BaseValidatorModel):
    sizeInGiB: Optional[int] = None
    kmsKeyId: Optional[str] = None


class TaskManagedEBSVolumeTerminationPolicy(BaseValidatorModel):
    deleteOnTermination: bool


class Tmpfs(BaseValidatorModel):
    containerPath: str
    size: int
    mountOptions: Optional[List[str]] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_container_agent' function.
class UpdateContainerAgentRequest(BaseValidatorModel):
    containerInstance: str
    cluster: Optional[str] = None


# This class is the input for the 'update_container_instances_state' function.
class UpdateContainerInstancesStateRequest(BaseValidatorModel):
    containerInstances: List[str]
    status: ContainerInstanceStatusType
    cluster: Optional[str] = None


# This class is the input for the 'update_service_primary_task_set' function.
class UpdateServicePrimaryTaskSetRequest(BaseValidatorModel):
    cluster: str
    service: str
    primaryTaskSet: str


# This class is the input for the 'update_task_protection' function.
class UpdateTaskProtectionRequest(BaseValidatorModel):
    cluster: str
    tasks: List[str]
    protectionEnabled: bool
    expiresInMinutes: Optional[int] = None


# This class is the input for the 'submit_attachment_state_changes' function.
class SubmitAttachmentStateChangesRequest(BaseValidatorModel):
    attachments: List[AttachmentStateChange]
    cluster: Optional[str] = None


class Attachment(BaseValidatorModel):
    id: Optional[str] = None
    type: Optional[str] = None
    status: Optional[str] = None
    details: Optional[List[KeyValuePair]] = None


class ProxyConfigurationOutput(BaseValidatorModel):
    containerName: str
    type: Optional[Literal['APPMESH']] = None
    properties: Optional[List[KeyValuePair]] = None


class ProxyConfiguration(BaseValidatorModel):
    containerName: str
    type: Optional[Literal['APPMESH']] = None
    properties: Optional[List[KeyValuePair]] = None


# This class is the input for the 'delete_attributes' function.
class DeleteAttributesRequest(BaseValidatorModel):
    attributes: List[Attribute]
    cluster: Optional[str] = None


# This class is the input for the 'put_attributes' function.
class PutAttributesRequest(BaseValidatorModel):
    attributes: List[Attribute]
    cluster: Optional[str] = None


class AutoScalingGroupProvider(BaseValidatorModel):
    autoScalingGroupArn: str
    managedScaling: Optional[ManagedScaling] = None
    managedTerminationProtection: Optional[ManagedTerminationProtectionType] = None
    managedDraining: Optional[ManagedDrainingType] = None


class AutoScalingGroupProviderUpdate(BaseValidatorModel):
    managedScaling: Optional[ManagedScaling] = None
    managedTerminationProtection: Optional[ManagedTerminationProtectionType] = None
    managedDraining: Optional[ManagedDrainingType] = None


class NetworkConfigurationOutput(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfigurationOutput] = None


class NetworkConfiguration(BaseValidatorModel):
    awsvpcConfiguration: Optional[AwsVpcConfiguration] = None


# This class is the input for the 'put_cluster_capacity_providers' function.
class PutClusterCapacityProvidersRequest(BaseValidatorModel):
    cluster: str
    capacityProviders: List[str]
    defaultCapacityProviderStrategy: List[CapacityProviderStrategyItem]


class EBSTagSpecificationOutput(BaseValidatorModel):
    resourceType: Literal['volume']
    tags: Optional[List[Tag]] = None
    propagateTags: Optional[PropagateTagsType] = None


class EBSTagSpecification(BaseValidatorModel):
    resourceType: Literal['volume']
    tags: Optional[List[Tag]] = None
    propagateTags: Optional[PropagateTagsType] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


# This class is the input for the 'update_cluster_settings' function.
class UpdateClusterSettingsRequest(BaseValidatorModel):
    cluster: str
    settings: List[ClusterSetting]


class ContainerOverrideOutput(BaseValidatorModel):
    name: Optional[str] = None
    command: Optional[List[str]] = None
    environment: Optional[List[KeyValuePair]] = None
    environmentFiles: Optional[List[EnvironmentFile]] = None
    cpu: Optional[int] = None
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None
    resourceRequirements: Optional[List[ResourceRequirement]] = None


class ContainerOverride(BaseValidatorModel):
    name: Optional[str] = None
    command: Optional[List[str]] = None
    environment: Optional[List[KeyValuePair]] = None
    environmentFiles: Optional[List[EnvironmentFile]] = None
    cpu: Optional[int] = None
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None
    resourceRequirements: Optional[List[ResourceRequirement]] = None


class LogConfigurationOutput(BaseValidatorModel):
    logDriver: LogDriverType
    options: Optional[Dict[str, str]] = None
    secretOptions: Optional[List[Secret]] = None


class LogConfiguration(BaseValidatorModel):
    logDriver: LogDriverType
    options: Optional[Dict[str, str]] = None
    secretOptions: Optional[List[Secret]] = None


class ContainerInstanceHealthStatus(BaseValidatorModel):
    overallStatus: Optional[InstanceHealthCheckStateType] = None
    details: Optional[List[InstanceHealthCheckResult]] = None

ContainerRestartPolicyUnion = Union[ContainerRestartPolicy, ContainerRestartPolicyOutput]


class ContainerStateChange(BaseValidatorModel):
    containerName: Optional[str] = None
    imageDigest: Optional[str] = None
    runtimeId: Optional[str] = None
    exitCode: Optional[int] = None
    networkBindings: Optional[List[NetworkBinding]] = None
    reason: Optional[str] = None
    status: Optional[str] = None


# This class is the input for the 'submit_container_state_change' function.
class SubmitContainerStateChangeRequest(BaseValidatorModel):
    cluster: Optional[str] = None
    task: Optional[str] = None
    containerName: Optional[str] = None
    runtimeId: Optional[str] = None
    status: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    networkBindings: Optional[List[NetworkBinding]] = None


class Container(BaseValidatorModel):
    containerArn: Optional[str] = None
    taskArn: Optional[str] = None
    name: Optional[str] = None
    image: Optional[str] = None
    imageDigest: Optional[str] = None
    runtimeId: Optional[str] = None
    lastStatus: Optional[str] = None
    exitCode: Optional[int] = None
    reason: Optional[str] = None
    networkBindings: Optional[List[NetworkBinding]] = None
    networkInterfaces: Optional[List[NetworkInterface]] = None
    healthStatus: Optional[HealthStatusType] = None
    managedAgents: Optional[List[ManagedAgent]] = None
    cpu: Optional[str] = None
    memory: Optional[str] = None
    memoryReservation: Optional[str] = None
    gpuIds: Optional[List[str]] = None


# This class is the output for the 'delete_attributes' function.
class DeleteAttributesResponse(BaseValidatorModel):
    attributes: List[Attribute]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'discover_poll_endpoint' function.
class DiscoverPollEndpointResponse(BaseValidatorModel):
    endpoint: str
    telemetryEndpoint: str
    serviceConnectEndpoint: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_attributes' function.
class ListAttributesResponse(BaseValidatorModel):
    attributes: List[Attribute]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_clusters' function.
class ListClustersResponse(BaseValidatorModel):
    clusterArns: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_container_instances' function.
class ListContainerInstancesResponse(BaseValidatorModel):
    containerInstanceArns: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_services_by_namespace' function.
class ListServicesByNamespaceResponse(BaseValidatorModel):
    serviceArns: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_services' function.
class ListServicesResponse(BaseValidatorModel):
    serviceArns: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_task_definition_families' function.
class ListTaskDefinitionFamiliesResponse(BaseValidatorModel):
    families: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_task_definitions' function.
class ListTaskDefinitionsResponse(BaseValidatorModel):
    taskDefinitionArns: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_tasks' function.
class ListTasksResponse(BaseValidatorModel):
    taskArns: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'put_attributes' function.
class PutAttributesResponse(BaseValidatorModel):
    attributes: List[Attribute]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'submit_attachment_state_changes' function.
class SubmitAttachmentStateChangesResponse(BaseValidatorModel):
    acknowledgment: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'submit_container_state_change' function.
class SubmitContainerStateChangeResponse(BaseValidatorModel):
    acknowledgment: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'submit_task_state_change' function.
class SubmitTaskStateChangeResponse(BaseValidatorModel):
    acknowledgment: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_task_set' function.
class UpdateTaskSetRequest(BaseValidatorModel):
    cluster: str
    service: str
    taskSet: str
    scale: Scale


class CreatedAt(BaseValidatorModel):
    before: Optional[Timestamp] = None
    after: Optional[Timestamp] = None


# This class is the output for the 'delete_account_setting' function.
class DeleteAccountSettingResponse(BaseValidatorModel):
    setting: Setting
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_account_settings' function.
class ListAccountSettingsResponse(BaseValidatorModel):
    settings: List[Setting]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'put_account_setting_default' function.
class PutAccountSettingDefaultResponse(BaseValidatorModel):
    setting: Setting
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_account_setting' function.
class PutAccountSettingResponse(BaseValidatorModel):
    setting: Setting
    ResponseMetadata: ResponseMetadata


class DeploymentConfigurationOutput(BaseValidatorModel):
    deploymentCircuitBreaker: Optional[DeploymentCircuitBreaker] = None
    maximumPercent: Optional[int] = None
    minimumHealthyPercent: Optional[int] = None
    alarms: Optional[DeploymentAlarmsOutput] = None


class DeploymentConfiguration(BaseValidatorModel):
    deploymentCircuitBreaker: Optional[DeploymentCircuitBreaker] = None
    maximumPercent: Optional[int] = None
    minimumHealthyPercent: Optional[int] = None
    alarms: Optional[DeploymentAlarms] = None


class DescribeServicesRequestWaitExtra(BaseValidatorModel):
    services: List[str]
    cluster: Optional[str] = None
    include: Optional[List[Literal['TAGS']]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeServicesRequestWait(BaseValidatorModel):
    services: List[str]
    cluster: Optional[str] = None
    include: Optional[List[Literal['TAGS']]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTasksRequestWaitExtra(BaseValidatorModel):
    tasks: List[str]
    cluster: Optional[str] = None
    include: Optional[List[Literal['TAGS']]] = None
    WaiterConfig: Optional[WaiterConfig] = None


class DescribeTasksRequestWait(BaseValidatorModel):
    tasks: List[str]
    cluster: Optional[str] = None
    include: Optional[List[Literal['TAGS']]] = None
    WaiterConfig: Optional[WaiterConfig] = None

DeviceUnion = Union[Device, DeviceOutput]

DockerVolumeConfigurationUnion = Union[DockerVolumeConfiguration, DockerVolumeConfigurationOutput]


class EFSVolumeConfiguration(BaseValidatorModel):
    fileSystemId: str
    rootDirectory: Optional[str] = None
    transitEncryption: Optional[EFSTransitEncryptionType] = None
    transitEncryptionPort: Optional[int] = None
    authorizationConfig: Optional[EFSAuthorizationConfig] = None


class ExecuteCommandConfiguration(BaseValidatorModel):
    kmsKeyId: Optional[str] = None
    logging: Optional[ExecuteCommandLoggingType] = None
    logConfiguration: Optional[ExecuteCommandLogConfiguration] = None


# This class is the output for the 'execute_command' function.
class ExecuteCommandResponse(BaseValidatorModel):
    clusterArn: str
    containerArn: str
    containerName: str
    interactive: bool
    session: Session
    taskArn: str
    ResponseMetadata: ResponseMetadata


class FSxWindowsFileServerVolumeConfiguration(BaseValidatorModel):
    fileSystemId: str
    rootDirectory: str
    authorizationConfig: FSxWindowsFileServerAuthorizationConfig

FirelensConfigurationUnion = Union[FirelensConfiguration, FirelensConfigurationOutput]


# This class is the output for the 'get_task_protection' function.
class GetTaskProtectionResponse(BaseValidatorModel):
    protectedTasks: List[ProtectedTask]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_task_protection' function.
class UpdateTaskProtectionResponse(BaseValidatorModel):
    protectedTasks: List[ProtectedTask]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata

HealthCheckUnion = Union[HealthCheck, HealthCheckOutput]

KernelCapabilitiesUnion = Union[KernelCapabilities, KernelCapabilitiesOutput]


class LinuxParametersOutput(BaseValidatorModel):
    capabilities: Optional[KernelCapabilitiesOutput] = None
    devices: Optional[List[DeviceOutput]] = None
    initProcessEnabled: Optional[bool] = None
    sharedMemorySize: Optional[int] = None
    tmpfs: Optional[List[TmpfsOutput]] = None
    maxSwap: Optional[int] = None
    swappiness: Optional[int] = None


class ListAccountSettingsRequestPaginate(BaseValidatorModel):
    name: Optional[SettingNameType] = None
    value: Optional[str] = None
    principalArn: Optional[str] = None
    effectiveSettings: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAttributesRequestPaginate(BaseValidatorModel):
    targetType: Literal['container-instance']
    cluster: Optional[str] = None
    attributeName: Optional[str] = None
    attributeValue: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListClustersRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContainerInstancesRequestPaginate(BaseValidatorModel):
    cluster: Optional[str] = None
    filter: Optional[str] = None
    status: Optional[ContainerInstanceStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServicesByNamespaceRequestPaginate(BaseValidatorModel):
    namespace: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListServicesRequestPaginate(BaseValidatorModel):
    cluster: Optional[str] = None
    launchType: Optional[LaunchTypeType] = None
    schedulingStrategy: Optional[SchedulingStrategyType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTaskDefinitionFamiliesRequestPaginate(BaseValidatorModel):
    familyPrefix: Optional[str] = None
    status: Optional[TaskDefinitionFamilyStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTaskDefinitionsRequestPaginate(BaseValidatorModel):
    familyPrefix: Optional[str] = None
    status: Optional[TaskDefinitionStatusType] = None
    sort: Optional[SortOrderType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTasksRequestPaginate(BaseValidatorModel):
    cluster: Optional[str] = None
    containerInstance: Optional[str] = None
    family: Optional[str] = None
    startedBy: Optional[str] = None
    serviceName: Optional[str] = None
    desiredStatus: Optional[DesiredStatusType] = None
    launchType: Optional[LaunchTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_service_deployments' function.
class ListServiceDeploymentsResponse(BaseValidatorModel):
    serviceDeployments: List[ServiceDeploymentBrief]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

ResourceUnion = Union[Resource, ResourceOutput]


class ServiceConnectTlsConfiguration(BaseValidatorModel):
    issuerCertificateAuthority: ServiceConnectTlsCertificateAuthority
    kmsKey: Optional[str] = None
    roleArn: Optional[str] = None

TmpfsUnion = Union[Tmpfs, TmpfsOutput]

ProxyConfigurationUnion = Union[ProxyConfiguration, ProxyConfigurationOutput]


class CapacityProvider(BaseValidatorModel):
    capacityProviderArn: Optional[str] = None
    name: Optional[str] = None
    status: Optional[CapacityProviderStatusType] = None
    autoScalingGroupProvider: Optional[AutoScalingGroupProvider] = None
    updateStatus: Optional[CapacityProviderUpdateStatusType] = None
    updateStatusReason: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_capacity_provider' function.
class CreateCapacityProviderRequest(BaseValidatorModel):
    name: str
    autoScalingGroupProvider: AutoScalingGroupProvider
    tags: Optional[List[Tag]] = None


# This class is the input for the 'update_capacity_provider' function.
class UpdateCapacityProviderRequest(BaseValidatorModel):
    name: str
    autoScalingGroupProvider: AutoScalingGroupProviderUpdate


class TaskSet(BaseValidatorModel):
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
    capacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    platformVersion: Optional[str] = None
    platformFamily: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationOutput] = None
    loadBalancers: Optional[List[LoadBalancer]] = None
    serviceRegistries: Optional[List[ServiceRegistry]] = None
    scale: Optional[Scale] = None
    stabilityStatus: Optional[StabilityStatusType] = None
    stabilityStatusAt: Optional[datetime] = None
    tags: Optional[List[Tag]] = None
    fargateEphemeralStorage: Optional[DeploymentEphemeralStorage] = None

NetworkConfigurationUnion = Union[NetworkConfiguration, NetworkConfigurationOutput]


class ServiceManagedEBSVolumeConfigurationOutput(BaseValidatorModel):
    roleArn: str
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None
    volumeType: Optional[str] = None
    sizeInGiB: Optional[int] = None
    snapshotId: Optional[str] = None
    iops: Optional[int] = None
    throughput: Optional[int] = None
    tagSpecifications: Optional[List[EBSTagSpecificationOutput]] = None
    filesystemType: Optional[TaskFilesystemTypeType] = None

EBSTagSpecificationUnion = Union[EBSTagSpecification, EBSTagSpecificationOutput]


class TaskOverrideOutput(BaseValidatorModel):
    containerOverrides: Optional[List[ContainerOverrideOutput]] = None
    cpu: Optional[str] = None
    inferenceAcceleratorOverrides: Optional[List[InferenceAcceleratorOverride]] = None
    executionRoleArn: Optional[str] = None
    memory: Optional[str] = None
    taskRoleArn: Optional[str] = None
    ephemeralStorage: Optional[EphemeralStorage] = None


class TaskOverride(BaseValidatorModel):
    containerOverrides: Optional[List[ContainerOverride]] = None
    cpu: Optional[str] = None
    inferenceAcceleratorOverrides: Optional[List[InferenceAcceleratorOverride]] = None
    executionRoleArn: Optional[str] = None
    memory: Optional[str] = None
    taskRoleArn: Optional[str] = None
    ephemeralStorage: Optional[EphemeralStorage] = None

LogConfigurationUnion = Union[LogConfiguration, LogConfigurationOutput]


class ContainerInstance(BaseValidatorModel):
    containerInstanceArn: Optional[str] = None
    ec2InstanceId: Optional[str] = None
    capacityProviderName: Optional[str] = None
    version: Optional[int] = None
    versionInfo: Optional[VersionInfo] = None
    remainingResources: Optional[List[ResourceOutput]] = None
    registeredResources: Optional[List[ResourceOutput]] = None
    status: Optional[str] = None
    statusReason: Optional[str] = None
    agentConnected: Optional[bool] = None
    runningTasksCount: Optional[int] = None
    pendingTasksCount: Optional[int] = None
    agentUpdateStatus: Optional[AgentUpdateStatusType] = None
    attributes: Optional[List[Attribute]] = None
    registeredAt: Optional[datetime] = None
    attachments: Optional[List[Attachment]] = None
    tags: Optional[List[Tag]] = None
    healthStatus: Optional[ContainerInstanceHealthStatus] = None


# This class is the input for the 'submit_task_state_change' function.
class SubmitTaskStateChangeRequest(BaseValidatorModel):
    cluster: Optional[str] = None
    task: Optional[str] = None
    status: Optional[str] = None
    reason: Optional[str] = None
    containers: Optional[List[ContainerStateChange]] = None
    attachments: Optional[List[AttachmentStateChange]] = None
    managedAgents: Optional[List[ManagedAgentStateChange]] = None
    pullStartedAt: Optional[Timestamp] = None
    pullStoppedAt: Optional[Timestamp] = None
    executionStoppedAt: Optional[Timestamp] = None


# This class is the input for the 'list_service_deployments' function.
class ListServiceDeploymentsRequest(BaseValidatorModel):
    service: str
    cluster: Optional[str] = None
    status: Optional[List[ServiceDeploymentStatusType]] = None
    createdAt: Optional[CreatedAt] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ServiceDeployment(BaseValidatorModel):
    serviceDeploymentArn: Optional[str] = None
    serviceArn: Optional[str] = None
    clusterArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    startedAt: Optional[datetime] = None
    finishedAt: Optional[datetime] = None
    stoppedAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    sourceServiceRevisions: Optional[List[ServiceRevisionSummary]] = None
    targetServiceRevision: Optional[ServiceRevisionSummary] = None
    status: Optional[ServiceDeploymentStatusType] = None
    statusReason: Optional[str] = None
    deploymentConfiguration: Optional[DeploymentConfigurationOutput] = None
    rollback: Optional[Rollback] = None
    deploymentCircuitBreaker: Optional[ServiceDeploymentCircuitBreaker] = None
    alarms: Optional[ServiceDeploymentAlarms] = None

DeploymentConfigurationUnion = Union[DeploymentConfiguration, DeploymentConfigurationOutput]


class ClusterConfiguration(BaseValidatorModel):
    executeCommandConfiguration: Optional[ExecuteCommandConfiguration] = None
    managedStorageConfiguration: Optional[ManagedStorageConfiguration] = None


class VolumeOutput(BaseValidatorModel):
    name: Optional[str] = None
    host: Optional[HostVolumeProperties] = None
    dockerVolumeConfiguration: Optional[DockerVolumeConfigurationOutput] = None
    efsVolumeConfiguration: Optional[EFSVolumeConfiguration] = None
    fsxWindowsFileServerVolumeConfiguration: Optional[FSxWindowsFileServerVolumeConfiguration] = None
    configuredAtLaunch: Optional[bool] = None


class Volume(BaseValidatorModel):
    name: Optional[str] = None
    host: Optional[HostVolumeProperties] = None
    dockerVolumeConfiguration: Optional[DockerVolumeConfigurationUnion] = None
    efsVolumeConfiguration: Optional[EFSVolumeConfiguration] = None
    fsxWindowsFileServerVolumeConfiguration: Optional[FSxWindowsFileServerVolumeConfiguration] = None
    configuredAtLaunch: Optional[bool] = None


class ContainerDefinitionOutput(BaseValidatorModel):
    name: Optional[str] = None
    image: Optional[str] = None
    repositoryCredentials: Optional[RepositoryCredentials] = None
    cpu: Optional[int] = None
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None
    links: Optional[List[str]] = None
    portMappings: Optional[List[PortMapping]] = None
    essential: Optional[bool] = None
    restartPolicy: Optional[ContainerRestartPolicyOutput] = None
    entryPoint: Optional[List[str]] = None
    command: Optional[List[str]] = None
    environment: Optional[List[KeyValuePair]] = None
    environmentFiles: Optional[List[EnvironmentFile]] = None
    mountPoints: Optional[List[MountPoint]] = None
    volumesFrom: Optional[List[VolumeFrom]] = None
    linuxParameters: Optional[LinuxParametersOutput] = None
    secrets: Optional[List[Secret]] = None
    dependsOn: Optional[List[ContainerDependency]] = None
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
    extraHosts: Optional[List[HostEntry]] = None
    dockerSecurityOptions: Optional[List[str]] = None
    interactive: Optional[bool] = None
    pseudoTerminal: Optional[bool] = None
    dockerLabels: Optional[Dict[str, str]] = None
    ulimits: Optional[List[Ulimit]] = None
    logConfiguration: Optional[LogConfigurationOutput] = None
    healthCheck: Optional[HealthCheckOutput] = None
    systemControls: Optional[List[SystemControl]] = None
    resourceRequirements: Optional[List[ResourceRequirement]] = None
    firelensConfiguration: Optional[FirelensConfigurationOutput] = None
    credentialSpecs: Optional[List[str]] = None


# This class is the input for the 'register_container_instance' function.
class RegisterContainerInstanceRequest(BaseValidatorModel):
    cluster: Optional[str] = None
    instanceIdentityDocument: Optional[str] = None
    instanceIdentityDocumentSignature: Optional[str] = None
    totalResources: Optional[List[ResourceUnion]] = None
    versionInfo: Optional[VersionInfo] = None
    containerInstanceArn: Optional[str] = None
    attributes: Optional[List[Attribute]] = None
    platformDevices: Optional[List[PlatformDevice]] = None
    tags: Optional[List[Tag]] = None


class ServiceConnectServiceOutput(BaseValidatorModel):
    portName: str
    discoveryName: Optional[str] = None
    clientAliases: Optional[List[ServiceConnectClientAlias]] = None
    ingressPortOverride: Optional[int] = None
    timeout: Optional[TimeoutConfiguration] = None
    tls: Optional[ServiceConnectTlsConfiguration] = None


class ServiceConnectService(BaseValidatorModel):
    portName: str
    discoveryName: Optional[str] = None
    clientAliases: Optional[List[ServiceConnectClientAlias]] = None
    ingressPortOverride: Optional[int] = None
    timeout: Optional[TimeoutConfiguration] = None
    tls: Optional[ServiceConnectTlsConfiguration] = None


class LinuxParameters(BaseValidatorModel):
    capabilities: Optional[KernelCapabilitiesUnion] = None
    devices: Optional[List[DeviceUnion]] = None
    initProcessEnabled: Optional[bool] = None
    sharedMemorySize: Optional[int] = None
    tmpfs: Optional[List[TmpfsUnion]] = None
    maxSwap: Optional[int] = None
    swappiness: Optional[int] = None


# This class is the output for the 'create_capacity_provider' function.
class CreateCapacityProviderResponse(BaseValidatorModel):
    capacityProvider: CapacityProvider
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_capacity_provider' function.
class DeleteCapacityProviderResponse(BaseValidatorModel):
    capacityProvider: CapacityProvider
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_capacity_providers' function.
class DescribeCapacityProvidersResponse(BaseValidatorModel):
    capacityProviders: List[CapacityProvider]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_capacity_provider' function.
class UpdateCapacityProviderResponse(BaseValidatorModel):
    capacityProvider: CapacityProvider
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_task_set' function.
class CreateTaskSetResponse(BaseValidatorModel):
    taskSet: TaskSet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_task_set' function.
class DeleteTaskSetResponse(BaseValidatorModel):
    taskSet: TaskSet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_task_sets' function.
class DescribeTaskSetsResponse(BaseValidatorModel):
    taskSets: List[TaskSet]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service_primary_task_set' function.
class UpdateServicePrimaryTaskSetResponse(BaseValidatorModel):
    taskSet: TaskSet
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_task_set' function.
class UpdateTaskSetResponse(BaseValidatorModel):
    taskSet: TaskSet
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_task_set' function.
class CreateTaskSetRequest(BaseValidatorModel):
    service: str
    cluster: str
    taskDefinition: str
    externalId: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationUnion] = None
    loadBalancers: Optional[List[LoadBalancer]] = None
    serviceRegistries: Optional[List[ServiceRegistry]] = None
    launchType: Optional[LaunchTypeType] = None
    capacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    platformVersion: Optional[str] = None
    scale: Optional[Scale] = None
    clientToken: Optional[str] = None
    tags: Optional[List[Tag]] = None


class ServiceVolumeConfigurationOutput(BaseValidatorModel):
    name: str
    managedEBSVolume: Optional[ServiceManagedEBSVolumeConfigurationOutput] = None


class ServiceManagedEBSVolumeConfiguration(BaseValidatorModel):
    roleArn: str
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None
    volumeType: Optional[str] = None
    sizeInGiB: Optional[int] = None
    snapshotId: Optional[str] = None
    iops: Optional[int] = None
    throughput: Optional[int] = None
    tagSpecifications: Optional[List[EBSTagSpecificationUnion]] = None
    filesystemType: Optional[TaskFilesystemTypeType] = None


class TaskManagedEBSVolumeConfiguration(BaseValidatorModel):
    roleArn: str
    encrypted: Optional[bool] = None
    kmsKeyId: Optional[str] = None
    volumeType: Optional[str] = None
    sizeInGiB: Optional[int] = None
    snapshotId: Optional[str] = None
    iops: Optional[int] = None
    throughput: Optional[int] = None
    tagSpecifications: Optional[List[EBSTagSpecificationUnion]] = None
    terminationPolicy: Optional[TaskManagedEBSVolumeTerminationPolicy] = None
    filesystemType: Optional[TaskFilesystemTypeType] = None


class Task(BaseValidatorModel):
    attachments: Optional[List[Attachment]] = None
    attributes: Optional[List[Attribute]] = None
    availabilityZone: Optional[str] = None
    capacityProviderName: Optional[str] = None
    clusterArn: Optional[str] = None
    connectivity: Optional[ConnectivityType] = None
    connectivityAt: Optional[datetime] = None
    containerInstanceArn: Optional[str] = None
    containers: Optional[List[Container]] = None
    cpu: Optional[str] = None
    createdAt: Optional[datetime] = None
    desiredStatus: Optional[str] = None
    enableExecuteCommand: Optional[bool] = None
    executionStoppedAt: Optional[datetime] = None
    group: Optional[str] = None
    healthStatus: Optional[HealthStatusType] = None
    inferenceAccelerators: Optional[List[InferenceAccelerator]] = None
    lastStatus: Optional[str] = None
    launchType: Optional[LaunchTypeType] = None
    memory: Optional[str] = None
    overrides: Optional[TaskOverrideOutput] = None
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
    tags: Optional[List[Tag]] = None
    taskArn: Optional[str] = None
    taskDefinitionArn: Optional[str] = None
    version: Optional[int] = None
    ephemeralStorage: Optional[EphemeralStorage] = None
    fargateEphemeralStorage: Optional[TaskEphemeralStorage] = None

TaskOverrideUnion = Union[TaskOverride, TaskOverrideOutput]


# This class is the output for the 'deregister_container_instance' function.
class DeregisterContainerInstanceResponse(BaseValidatorModel):
    containerInstance: ContainerInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_container_instances' function.
class DescribeContainerInstancesResponse(BaseValidatorModel):
    containerInstances: List[ContainerInstance]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_container_instance' function.
class RegisterContainerInstanceResponse(BaseValidatorModel):
    containerInstance: ContainerInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_container_agent' function.
class UpdateContainerAgentResponse(BaseValidatorModel):
    containerInstance: ContainerInstance
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_container_instances_state' function.
class UpdateContainerInstancesStateResponse(BaseValidatorModel):
    containerInstances: List[ContainerInstance]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_service_deployments' function.
class DescribeServiceDeploymentsResponse(BaseValidatorModel):
    serviceDeployments: List[ServiceDeployment]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata


class Cluster(BaseValidatorModel):
    clusterArn: Optional[str] = None
    clusterName: Optional[str] = None
    configuration: Optional[ClusterConfiguration] = None
    status: Optional[str] = None
    registeredContainerInstancesCount: Optional[int] = None
    runningTasksCount: Optional[int] = None
    pendingTasksCount: Optional[int] = None
    activeServicesCount: Optional[int] = None
    statistics: Optional[List[KeyValuePair]] = None
    tags: Optional[List[Tag]] = None
    settings: Optional[List[ClusterSetting]] = None
    capacityProviders: Optional[List[str]] = None
    defaultCapacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    attachments: Optional[List[Attachment]] = None
    attachmentsStatus: Optional[str] = None
    serviceConnectDefaults: Optional[ClusterServiceConnectDefaults] = None


# This class is the input for the 'create_cluster' function.
class CreateClusterRequest(BaseValidatorModel):
    clusterName: Optional[str] = None
    tags: Optional[List[Tag]] = None
    settings: Optional[List[ClusterSetting]] = None
    configuration: Optional[ClusterConfiguration] = None
    capacityProviders: Optional[List[str]] = None
    defaultCapacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    serviceConnectDefaults: Optional[ClusterServiceConnectDefaultsRequest] = None


# This class is the input for the 'update_cluster' function.
class UpdateClusterRequest(BaseValidatorModel):
    cluster: str
    settings: Optional[List[ClusterSetting]] = None
    configuration: Optional[ClusterConfiguration] = None
    serviceConnectDefaults: Optional[ClusterServiceConnectDefaultsRequest] = None

VolumeUnion = Union[Volume, VolumeOutput]


class TaskDefinition(BaseValidatorModel):
    taskDefinitionArn: Optional[str] = None
    containerDefinitions: Optional[List[ContainerDefinitionOutput]] = None
    family: Optional[str] = None
    taskRoleArn: Optional[str] = None
    executionRoleArn: Optional[str] = None
    networkMode: Optional[NetworkModeType] = None
    revision: Optional[int] = None
    volumes: Optional[List[VolumeOutput]] = None
    status: Optional[TaskDefinitionStatusType] = None
    requiresAttributes: Optional[List[Attribute]] = None
    placementConstraints: Optional[List[TaskDefinitionPlacementConstraint]] = None
    compatibilities: Optional[List[CompatibilityType]] = None
    runtimePlatform: Optional[RuntimePlatform] = None
    requiresCompatibilities: Optional[List[CompatibilityType]] = None
    cpu: Optional[str] = None
    memory: Optional[str] = None
    inferenceAccelerators: Optional[List[InferenceAccelerator]] = None
    pidMode: Optional[PidModeType] = None
    ipcMode: Optional[IpcModeType] = None
    proxyConfiguration: Optional[ProxyConfigurationOutput] = None
    registeredAt: Optional[datetime] = None
    deregisteredAt: Optional[datetime] = None
    registeredBy: Optional[str] = None
    ephemeralStorage: Optional[EphemeralStorage] = None
    enableFaultInjection: Optional[bool] = None


class ServiceConnectConfigurationOutput(BaseValidatorModel):
    enabled: bool
    namespace: Optional[str] = None
    services: Optional[List[ServiceConnectServiceOutput]] = None
    logConfiguration: Optional[LogConfigurationOutput] = None


class ServiceConnectConfiguration(BaseValidatorModel):
    enabled: bool
    namespace: Optional[str] = None
    services: Optional[List[ServiceConnectService]] = None
    logConfiguration: Optional[LogConfiguration] = None

LinuxParametersUnion = Union[LinuxParameters, LinuxParametersOutput]

ServiceManagedEBSVolumeConfigurationUnion = Union[ServiceManagedEBSVolumeConfiguration, ServiceManagedEBSVolumeConfigurationOutput]


class TaskVolumeConfiguration(BaseValidatorModel):
    name: str
    managedEBSVolume: Optional[TaskManagedEBSVolumeConfiguration] = None


# This class is the output for the 'describe_tasks' function.
class DescribeTasksResponse(BaseValidatorModel):
    tasks: List[Task]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'run_task' function.
class RunTaskResponse(BaseValidatorModel):
    tasks: List[Task]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_task' function.
class StartTaskResponse(BaseValidatorModel):
    tasks: List[Task]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'stop_task' function.
class StopTaskResponse(BaseValidatorModel):
    task: Task
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_cluster' function.
class CreateClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_cluster' function.
class DeleteClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_clusters' function.
class DescribeClustersResponse(BaseValidatorModel):
    clusters: List[Cluster]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_cluster_capacity_providers' function.
class PutClusterCapacityProvidersResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_cluster' function.
class UpdateClusterResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_cluster_settings' function.
class UpdateClusterSettingsResponse(BaseValidatorModel):
    cluster: Cluster
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_task_definitions' function.
class DeleteTaskDefinitionsResponse(BaseValidatorModel):
    taskDefinitions: List[TaskDefinition]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deregister_task_definition' function.
class DeregisterTaskDefinitionResponse(BaseValidatorModel):
    taskDefinition: TaskDefinition
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_task_definition' function.
class DescribeTaskDefinitionResponse(BaseValidatorModel):
    taskDefinition: TaskDefinition
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'register_task_definition' function.
class RegisterTaskDefinitionResponse(BaseValidatorModel):
    taskDefinition: TaskDefinition
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class Deployment(BaseValidatorModel):
    id: Optional[str] = None
    status: Optional[str] = None
    taskDefinition: Optional[str] = None
    desiredCount: Optional[int] = None
    pendingCount: Optional[int] = None
    runningCount: Optional[int] = None
    failedTasks: Optional[int] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    capacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    launchType: Optional[LaunchTypeType] = None
    platformVersion: Optional[str] = None
    platformFamily: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationOutput] = None
    rolloutState: Optional[DeploymentRolloutStateType] = None
    rolloutStateReason: Optional[str] = None
    serviceConnectConfiguration: Optional[ServiceConnectConfigurationOutput] = None
    serviceConnectResources: Optional[List[ServiceConnectServiceResource]] = None
    volumeConfigurations: Optional[List[ServiceVolumeConfigurationOutput]] = None
    fargateEphemeralStorage: Optional[DeploymentEphemeralStorage] = None
    vpcLatticeConfigurations: Optional[List[VpcLatticeConfiguration]] = None


class ServiceRevision(BaseValidatorModel):
    serviceRevisionArn: Optional[str] = None
    serviceArn: Optional[str] = None
    clusterArn: Optional[str] = None
    taskDefinition: Optional[str] = None
    capacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    launchType: Optional[LaunchTypeType] = None
    platformVersion: Optional[str] = None
    platformFamily: Optional[str] = None
    loadBalancers: Optional[List[LoadBalancer]] = None
    serviceRegistries: Optional[List[ServiceRegistry]] = None
    networkConfiguration: Optional[NetworkConfigurationOutput] = None
    containerImages: Optional[List[ContainerImage]] = None
    guardDutyEnabled: Optional[bool] = None
    serviceConnectConfiguration: Optional[ServiceConnectConfigurationOutput] = None
    volumeConfigurations: Optional[List[ServiceVolumeConfigurationOutput]] = None
    fargateEphemeralStorage: Optional[DeploymentEphemeralStorage] = None
    createdAt: Optional[datetime] = None
    vpcLatticeConfigurations: Optional[List[VpcLatticeConfiguration]] = None

ServiceConnectConfigurationUnion = Union[ServiceConnectConfiguration, ServiceConnectConfigurationOutput]


class ContainerDefinition(BaseValidatorModel):
    name: Optional[str] = None
    image: Optional[str] = None
    repositoryCredentials: Optional[RepositoryCredentials] = None
    cpu: Optional[int] = None
    memory: Optional[int] = None
    memoryReservation: Optional[int] = None
    links: Optional[List[str]] = None
    portMappings: Optional[List[PortMapping]] = None
    essential: Optional[bool] = None
    restartPolicy: Optional[ContainerRestartPolicyUnion] = None
    entryPoint: Optional[List[str]] = None
    command: Optional[List[str]] = None
    environment: Optional[List[KeyValuePair]] = None
    environmentFiles: Optional[List[EnvironmentFile]] = None
    mountPoints: Optional[List[MountPoint]] = None
    volumesFrom: Optional[List[VolumeFrom]] = None
    linuxParameters: Optional[LinuxParametersUnion] = None
    secrets: Optional[List[Secret]] = None
    dependsOn: Optional[List[ContainerDependency]] = None
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
    extraHosts: Optional[List[HostEntry]] = None
    dockerSecurityOptions: Optional[List[str]] = None
    interactive: Optional[bool] = None
    pseudoTerminal: Optional[bool] = None
    dockerLabels: Optional[Dict[str, str]] = None
    ulimits: Optional[List[Ulimit]] = None
    logConfiguration: Optional[LogConfigurationUnion] = None
    healthCheck: Optional[HealthCheckUnion] = None
    systemControls: Optional[List[SystemControl]] = None
    resourceRequirements: Optional[List[ResourceRequirement]] = None
    firelensConfiguration: Optional[FirelensConfigurationUnion] = None
    credentialSpecs: Optional[List[str]] = None


class ServiceVolumeConfiguration(BaseValidatorModel):
    name: str
    managedEBSVolume: Optional[ServiceManagedEBSVolumeConfigurationUnion] = None


# This class is the input for the 'run_task' function.
class RunTaskRequest(BaseValidatorModel):
    taskDefinition: str
    capacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    cluster: Optional[str] = None
    count: Optional[int] = None
    enableECSManagedTags: Optional[bool] = None
    enableExecuteCommand: Optional[bool] = None
    group: Optional[str] = None
    launchType: Optional[LaunchTypeType] = None
    networkConfiguration: Optional[NetworkConfigurationUnion] = None
    overrides: Optional[TaskOverrideUnion] = None
    placementConstraints: Optional[List[PlacementConstraint]] = None
    placementStrategy: Optional[List[PlacementStrategy]] = None
    platformVersion: Optional[str] = None
    propagateTags: Optional[PropagateTagsType] = None
    referenceId: Optional[str] = None
    startedBy: Optional[str] = None
    tags: Optional[List[Tag]] = None
    clientToken: Optional[str] = None
    volumeConfigurations: Optional[List[TaskVolumeConfiguration]] = None


# This class is the input for the 'start_task' function.
class StartTaskRequest(BaseValidatorModel):
    containerInstances: List[str]
    taskDefinition: str
    cluster: Optional[str] = None
    enableECSManagedTags: Optional[bool] = None
    enableExecuteCommand: Optional[bool] = None
    group: Optional[str] = None
    networkConfiguration: Optional[NetworkConfigurationUnion] = None
    overrides: Optional[TaskOverrideUnion] = None
    propagateTags: Optional[PropagateTagsType] = None
    referenceId: Optional[str] = None
    startedBy: Optional[str] = None
    tags: Optional[List[Tag]] = None
    volumeConfigurations: Optional[List[TaskVolumeConfiguration]] = None


class Service(BaseValidatorModel):
    serviceArn: Optional[str] = None
    serviceName: Optional[str] = None
    clusterArn: Optional[str] = None
    loadBalancers: Optional[List[LoadBalancer]] = None
    serviceRegistries: Optional[List[ServiceRegistry]] = None
    status: Optional[str] = None
    desiredCount: Optional[int] = None
    runningCount: Optional[int] = None
    pendingCount: Optional[int] = None
    launchType: Optional[LaunchTypeType] = None
    capacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    platformVersion: Optional[str] = None
    platformFamily: Optional[str] = None
    taskDefinition: Optional[str] = None
    deploymentConfiguration: Optional[DeploymentConfigurationOutput] = None
    taskSets: Optional[List[TaskSet]] = None
    deployments: Optional[List[Deployment]] = None
    roleArn: Optional[str] = None
    events: Optional[List[ServiceEvent]] = None
    createdAt: Optional[datetime] = None
    placementConstraints: Optional[List[PlacementConstraint]] = None
    placementStrategy: Optional[List[PlacementStrategy]] = None
    networkConfiguration: Optional[NetworkConfigurationOutput] = None
    healthCheckGracePeriodSeconds: Optional[int] = None
    schedulingStrategy: Optional[SchedulingStrategyType] = None
    deploymentController: Optional[DeploymentController] = None
    tags: Optional[List[Tag]] = None
    createdBy: Optional[str] = None
    enableECSManagedTags: Optional[bool] = None
    propagateTags: Optional[PropagateTagsType] = None
    enableExecuteCommand: Optional[bool] = None
    availabilityZoneRebalancing: Optional[AvailabilityZoneRebalancingType] = None


# This class is the output for the 'describe_service_revisions' function.
class DescribeServiceRevisionsResponse(BaseValidatorModel):
    serviceRevisions: List[ServiceRevision]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata

ContainerDefinitionUnion = Union[ContainerDefinition, ContainerDefinitionOutput]

ServiceVolumeConfigurationUnion = Union[ServiceVolumeConfiguration, ServiceVolumeConfigurationOutput]


# This class is the output for the 'create_service' function.
class CreateServiceResponse(BaseValidatorModel):
    service: Service
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_service' function.
class DeleteServiceResponse(BaseValidatorModel):
    service: Service
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_services' function.
class DescribeServicesResponse(BaseValidatorModel):
    services: List[Service]
    failures: List[Failure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_service' function.
class UpdateServiceResponse(BaseValidatorModel):
    service: Service
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'register_task_definition' function.
class RegisterTaskDefinitionRequest(BaseValidatorModel):
    family: str
    containerDefinitions: List[ContainerDefinitionUnion]
    taskRoleArn: Optional[str] = None
    executionRoleArn: Optional[str] = None
    networkMode: Optional[NetworkModeType] = None
    volumes: Optional[List[VolumeUnion]] = None
    placementConstraints: Optional[List[TaskDefinitionPlacementConstraint]] = None
    requiresCompatibilities: Optional[List[CompatibilityType]] = None
    cpu: Optional[str] = None
    memory: Optional[str] = None
    tags: Optional[List[Tag]] = None
    pidMode: Optional[PidModeType] = None
    ipcMode: Optional[IpcModeType] = None
    proxyConfiguration: Optional[ProxyConfigurationUnion] = None
    inferenceAccelerators: Optional[List[InferenceAccelerator]] = None
    ephemeralStorage: Optional[EphemeralStorage] = None
    runtimePlatform: Optional[RuntimePlatform] = None
    enableFaultInjection: Optional[bool] = None


# This class is the input for the 'create_service' function.
class CreateServiceRequest(BaseValidatorModel):
    serviceName: str
    cluster: Optional[str] = None
    taskDefinition: Optional[str] = None
    availabilityZoneRebalancing: Optional[AvailabilityZoneRebalancingType] = None
    loadBalancers: Optional[List[LoadBalancer]] = None
    serviceRegistries: Optional[List[ServiceRegistry]] = None
    desiredCount: Optional[int] = None
    clientToken: Optional[str] = None
    launchType: Optional[LaunchTypeType] = None
    capacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    platformVersion: Optional[str] = None
    role: Optional[str] = None
    deploymentConfiguration: Optional[DeploymentConfigurationUnion] = None
    placementConstraints: Optional[List[PlacementConstraint]] = None
    placementStrategy: Optional[List[PlacementStrategy]] = None
    networkConfiguration: Optional[NetworkConfigurationUnion] = None
    healthCheckGracePeriodSeconds: Optional[int] = None
    schedulingStrategy: Optional[SchedulingStrategyType] = None
    deploymentController: Optional[DeploymentController] = None
    tags: Optional[List[Tag]] = None
    enableECSManagedTags: Optional[bool] = None
    propagateTags: Optional[PropagateTagsType] = None
    enableExecuteCommand: Optional[bool] = None
    serviceConnectConfiguration: Optional[ServiceConnectConfigurationUnion] = None
    volumeConfigurations: Optional[List[ServiceVolumeConfigurationUnion]] = None
    vpcLatticeConfigurations: Optional[List[VpcLatticeConfiguration]] = None


# This class is the input for the 'update_service' function.
class UpdateServiceRequest(BaseValidatorModel):
    service: str
    cluster: Optional[str] = None
    desiredCount: Optional[int] = None
    taskDefinition: Optional[str] = None
    capacityProviderStrategy: Optional[List[CapacityProviderStrategyItem]] = None
    deploymentConfiguration: Optional[DeploymentConfigurationUnion] = None
    availabilityZoneRebalancing: Optional[AvailabilityZoneRebalancingType] = None
    networkConfiguration: Optional[NetworkConfigurationUnion] = None
    placementConstraints: Optional[List[PlacementConstraint]] = None
    placementStrategy: Optional[List[PlacementStrategy]] = None
    platformVersion: Optional[str] = None
    forceNewDeployment: Optional[bool] = None
    healthCheckGracePeriodSeconds: Optional[int] = None
    enableExecuteCommand: Optional[bool] = None
    enableECSManagedTags: Optional[bool] = None
    loadBalancers: Optional[List[LoadBalancer]] = None
    propagateTags: Optional[PropagateTagsType] = None
    serviceRegistries: Optional[List[ServiceRegistry]] = None
    serviceConnectConfiguration: Optional[ServiceConnectConfigurationUnion] = None
    volumeConfigurations: Optional[List[ServiceVolumeConfigurationUnion]] = None
    vpcLatticeConfigurations: Optional[List[VpcLatticeConfiguration]] = None