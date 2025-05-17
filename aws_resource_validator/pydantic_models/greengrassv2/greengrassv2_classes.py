from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.greengrassv2.greengrassv2_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AssociateClientDeviceWithCoreDeviceEntry(BaseValidatorModel):
    thingName: str


class AssociateClientDeviceWithCoreDeviceErrorEntry(BaseValidatorModel):
    thingName: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None


# This class is the input for the 'associate_service_role_to_account' function.
class AssociateServiceRoleToAccountRequest(BaseValidatorModel):
    roleArn: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociatedClientDevice(BaseValidatorModel):
    thingName: Optional[str] = None
    associationTimestamp: Optional[datetime] = None


class DisassociateClientDeviceFromCoreDeviceEntry(BaseValidatorModel):
    thingName: str


class DisassociateClientDeviceFromCoreDeviceErrorEntry(BaseValidatorModel):
    thingName: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


# This class is the input for the 'cancel_deployment' function.
class CancelDeploymentRequest(BaseValidatorModel):
    deploymentId: str


class CloudComponentStatus(BaseValidatorModel):
    componentState: Optional[CloudComponentStateType] = None
    message: Optional[str] = None
    errors: Optional[Dict[str, str]] = None
    vendorGuidance: Optional[VendorGuidanceType] = None
    vendorGuidanceMessage: Optional[str] = None


class ComponentCandidate(BaseValidatorModel):
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    versionRequirements: Optional[Dict[str, str]] = None


class ComponentConfigurationUpdateOutput(BaseValidatorModel):
    merge: Optional[str] = None
    reset: Optional[List[str]] = None


class ComponentConfigurationUpdate(BaseValidatorModel):
    merge: Optional[str] = None
    reset: Optional[List[str]] = None


class ComponentDependencyRequirement(BaseValidatorModel):
    versionRequirement: Optional[str] = None
    dependencyType: Optional[ComponentDependencyTypeType] = None


class ComponentPlatformOutput(BaseValidatorModel):
    name: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None


class ComponentPlatform(BaseValidatorModel):
    name: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None


class SystemResourceLimits(BaseValidatorModel):
    memory: Optional[int] = None
    cpus: Optional[float] = None


class ComponentVersionListItem(BaseValidatorModel):
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    arn: Optional[str] = None


class ConnectivityInfo(BaseValidatorModel):
    id: Optional[str] = None
    hostAddress: Optional[str] = None
    portNumber: Optional[int] = None
    metadata: Optional[str] = None


class CoreDevice(BaseValidatorModel):
    coreDeviceThingName: Optional[str] = None
    status: Optional[CoreDeviceStatusType] = None
    lastStatusUpdateTimestamp: Optional[datetime] = None
    platform: Optional[str] = None
    architecture: Optional[str] = None
    runtime: Optional[str] = None


# This class is the input for the 'delete_component' function.
class DeleteComponentRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'delete_core_device' function.
class DeleteCoreDeviceRequest(BaseValidatorModel):
    coreDeviceThingName: str


# This class is the input for the 'delete_deployment' function.
class DeleteDeploymentRequest(BaseValidatorModel):
    deploymentId: str


class DeploymentComponentUpdatePolicy(BaseValidatorModel):
    timeoutInSeconds: Optional[int] = None
    action: Optional[DeploymentComponentUpdatePolicyActionType] = None


class DeploymentConfigurationValidationPolicy(BaseValidatorModel):
    timeoutInSeconds: Optional[int] = None


class IoTJobTimeoutConfig(BaseValidatorModel):
    inProgressTimeoutInMinutes: Optional[int] = None


class Deployment(BaseValidatorModel):
    targetArn: Optional[str] = None
    revisionId: Optional[str] = None
    deploymentId: Optional[str] = None
    deploymentName: Optional[str] = None
    creationTimestamp: Optional[datetime] = None
    deploymentStatus: Optional[DeploymentStatusType] = None
    isLatestForTarget: Optional[bool] = None
    parentTargetArn: Optional[str] = None


# This class is the input for the 'describe_component' function.
class DescribeComponentRequest(BaseValidatorModel):
    arn: str


class EffectiveDeploymentStatusDetails(BaseValidatorModel):
    errorStack: Optional[List[str]] = None
    errorTypes: Optional[List[str]] = None


# This class is the input for the 'get_component' function.
class GetComponentRequest(BaseValidatorModel):
    arn: str
    recipeOutputFormat: Optional[RecipeOutputFormatType] = None


# This class is the input for the 'get_component_version_artifact' function.
class GetComponentVersionArtifactRequest(BaseValidatorModel):
    arn: str
    artifactName: str
    s3EndpointType: Optional[S3EndpointTypeType] = None
    iotEndpointType: Optional[IotEndpointTypeType] = None


# This class is the input for the 'get_connectivity_info' function.
class GetConnectivityInfoRequest(BaseValidatorModel):
    thingName: str


# This class is the input for the 'get_core_device' function.
class GetCoreDeviceRequest(BaseValidatorModel):
    coreDeviceThingName: str


# This class is the input for the 'get_deployment' function.
class GetDeploymentRequest(BaseValidatorModel):
    deploymentId: str


class InstalledComponent(BaseValidatorModel):
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    lifecycleState: Optional[InstalledComponentLifecycleStateType] = None
    lifecycleStateDetails: Optional[str] = None
    isRoot: Optional[bool] = None
    lastStatusChangeTimestamp: Optional[datetime] = None
    lastReportedTimestamp: Optional[datetime] = None
    lastInstallationSource: Optional[str] = None
    lifecycleStatusCodes: Optional[List[str]] = None


class IoTJobAbortCriteria(BaseValidatorModel):
    failureType: IoTJobExecutionFailureTypeType
    action: Literal['CANCEL']
    thresholdPercentage: float
    minNumberOfExecutedThings: int


class IoTJobRateIncreaseCriteria(BaseValidatorModel):
    numberOfNotifiedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None


class LambdaDeviceMount(BaseValidatorModel):
    path: str
    permission: Optional[LambdaFilesystemPermissionType] = None
    addGroupOwner: Optional[bool] = None


class LambdaVolumeMount(BaseValidatorModel):
    sourcePath: str
    destinationPath: str
    permission: Optional[LambdaFilesystemPermissionType] = None
    addGroupOwner: Optional[bool] = None


class LambdaEventSource(BaseValidatorModel):
    topic: str
    type: LambdaEventSourceTypeType


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_client_devices_associated_with_core_device' function.
class ListClientDevicesAssociatedWithCoreDeviceRequest(BaseValidatorModel):
    coreDeviceThingName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_component_versions' function.
class ListComponentVersionsRequest(BaseValidatorModel):
    arn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_components' function.
class ListComponentsRequest(BaseValidatorModel):
    scope: Optional[ComponentVisibilityScopeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_core_devices' function.
class ListCoreDevicesRequest(BaseValidatorModel):
    thingGroupArn: Optional[str] = None
    status: Optional[CoreDeviceStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    runtime: Optional[str] = None


# This class is the input for the 'list_deployments' function.
class ListDeploymentsRequest(BaseValidatorModel):
    targetArn: Optional[str] = None
    historyFilter: Optional[DeploymentHistoryFilterType] = None
    parentTargetArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_effective_deployments' function.
class ListEffectiveDeploymentsRequest(BaseValidatorModel):
    coreDeviceThingName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_installed_components' function.
class ListInstalledComponentsRequest(BaseValidatorModel):
    coreDeviceThingName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    topologyFilter: Optional[InstalledComponentTopologyFilterType] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ResolvedComponentVersion(BaseValidatorModel):
    arn: Optional[str] = None
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    recipe: Optional[bytes] = None
    vendorGuidance: Optional[VendorGuidanceType] = None
    message: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'batch_associate_client_device_with_core_device' function.
class BatchAssociateClientDeviceWithCoreDeviceRequest(BaseValidatorModel):
    coreDeviceThingName: str
    entries: Optional[List[AssociateClientDeviceWithCoreDeviceEntry]] = None


# This class is the output for the 'associate_service_role_to_account' function.
class AssociateServiceRoleToAccountResponse(BaseValidatorModel):
    associatedAt: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_associate_client_device_with_core_device' function.
class BatchAssociateClientDeviceWithCoreDeviceResponse(BaseValidatorModel):
    errorEntries: List[AssociateClientDeviceWithCoreDeviceErrorEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'cancel_deployment' function.
class CancelDeploymentResponse(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_deployment' function.
class CreateDeploymentResponse(BaseValidatorModel):
    deploymentId: str
    iotJobId: str
    iotJobArn: str
    ResponseMetadata: ResponseMetadata


class DisassociateServiceRoleFromAccountResponse(BaseValidatorModel):
    disassociatedAt: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_deployment' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_component' function.
class GetComponentResponse(BaseValidatorModel):
    recipeOutputFormat: RecipeOutputFormatType
    recipe: bytes
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_component_version_artifact' function.
class GetComponentVersionArtifactResponse(BaseValidatorModel):
    preSignedUrl: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_core_device' function.
class GetCoreDeviceResponse(BaseValidatorModel):
    coreDeviceThingName: str
    coreVersion: str
    platform: str
    architecture: str
    runtime: str
    status: CoreDeviceStatusType
    lastStatusUpdateTimestamp: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetServiceRoleForAccountResponse(BaseValidatorModel):
    associatedAt: str
    roleArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_connectivity_info' function.
class UpdateConnectivityInfoResponse(BaseValidatorModel):
    version: str
    message: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_client_devices_associated_with_core_device' function.
class ListClientDevicesAssociatedWithCoreDeviceResponse(BaseValidatorModel):
    associatedClientDevices: List[AssociatedClientDevice]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'batch_disassociate_client_device_from_core_device' function.
class BatchDisassociateClientDeviceFromCoreDeviceRequest(BaseValidatorModel):
    coreDeviceThingName: str
    entries: Optional[List[DisassociateClientDeviceFromCoreDeviceEntry]] = None


# This class is the output for the 'batch_disassociate_client_device_from_core_device' function.
class BatchDisassociateClientDeviceFromCoreDeviceResponse(BaseValidatorModel):
    errorEntries: List[DisassociateClientDeviceFromCoreDeviceErrorEntry]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_component_version' function.
class CreateComponentVersionResponse(BaseValidatorModel):
    arn: str
    componentName: str
    componentVersion: str
    creationTimestamp: datetime
    status: CloudComponentStatus
    ResponseMetadata: ResponseMetadata

ComponentConfigurationUpdateUnion = Union[ComponentConfigurationUpdate, ComponentConfigurationUpdateOutput]


class ComponentLatestVersion(BaseValidatorModel):
    arn: Optional[str] = None
    componentVersion: Optional[str] = None
    creationTimestamp: Optional[datetime] = None
    description: Optional[str] = None
    publisher: Optional[str] = None
    platforms: Optional[List[ComponentPlatformOutput]] = None


# This class is the output for the 'describe_component' function.
class DescribeComponentResponse(BaseValidatorModel):
    arn: str
    componentName: str
    componentVersion: str
    creationTimestamp: datetime
    publisher: str
    description: str
    status: CloudComponentStatus
    platforms: List[ComponentPlatformOutput]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

ComponentPlatformUnion = Union[ComponentPlatform, ComponentPlatformOutput]


class ComponentRunWith(BaseValidatorModel):
    posixUser: Optional[str] = None
    systemResourceLimits: Optional[SystemResourceLimits] = None
    windowsUser: Optional[str] = None


# This class is the output for the 'list_component_versions' function.
class ListComponentVersionsResponse(BaseValidatorModel):
    componentVersions: List[ComponentVersionListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_connectivity_info' function.
class GetConnectivityInfoResponse(BaseValidatorModel):
    connectivityInfo: List[ConnectivityInfo]
    message: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_connectivity_info' function.
class UpdateConnectivityInfoRequest(BaseValidatorModel):
    thingName: str
    connectivityInfo: List[ConnectivityInfo]


# This class is the output for the 'list_core_devices' function.
class ListCoreDevicesResponse(BaseValidatorModel):
    coreDevices: List[CoreDevice]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DeploymentPolicies(BaseValidatorModel):
    failureHandlingPolicy: Optional[DeploymentFailureHandlingPolicyType] = None
    componentUpdatePolicy: Optional[DeploymentComponentUpdatePolicy] = None
    configurationValidationPolicy: Optional[DeploymentConfigurationValidationPolicy] = None


# This class is the output for the 'list_deployments' function.
class ListDeploymentsResponse(BaseValidatorModel):
    deployments: List[Deployment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class EffectiveDeployment(BaseValidatorModel):
    deploymentId: str
    deploymentName: str
    targetArn: str
    coreDeviceExecutionStatus: EffectiveDeploymentExecutionStatusType
    creationTimestamp: datetime
    modifiedTimestamp: datetime
    iotJobId: Optional[str] = None
    iotJobArn: Optional[str] = None
    description: Optional[str] = None
    reason: Optional[str] = None
    statusDetails: Optional[EffectiveDeploymentStatusDetails] = None


# This class is the output for the 'list_installed_components' function.
class ListInstalledComponentsResponse(BaseValidatorModel):
    installedComponents: List[InstalledComponent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IoTJobAbortConfigOutput(BaseValidatorModel):
    criteriaList: List[IoTJobAbortCriteria]


class IoTJobAbortConfig(BaseValidatorModel):
    criteriaList: List[IoTJobAbortCriteria]


class IoTJobExponentialRolloutRate(BaseValidatorModel):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: IoTJobRateIncreaseCriteria


class LambdaContainerParams(BaseValidatorModel):
    memorySizeInKB: Optional[int] = None
    mountROSysfs: Optional[bool] = None
    volumes: Optional[List[LambdaVolumeMount]] = None
    devices: Optional[List[LambdaDeviceMount]] = None


class ListClientDevicesAssociatedWithCoreDeviceRequestPaginate(BaseValidatorModel):
    coreDeviceThingName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListComponentVersionsRequestPaginate(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListComponentsRequestPaginate(BaseValidatorModel):
    scope: Optional[ComponentVisibilityScopeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListCoreDevicesRequestPaginate(BaseValidatorModel):
    thingGroupArn: Optional[str] = None
    status: Optional[CoreDeviceStatusType] = None
    runtime: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDeploymentsRequestPaginate(BaseValidatorModel):
    targetArn: Optional[str] = None
    historyFilter: Optional[DeploymentHistoryFilterType] = None
    parentTargetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEffectiveDeploymentsRequestPaginate(BaseValidatorModel):
    coreDeviceThingName: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstalledComponentsRequestPaginate(BaseValidatorModel):
    coreDeviceThingName: str
    topologyFilter: Optional[InstalledComponentTopologyFilterType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'resolve_component_candidates' function.
class ResolveComponentCandidatesResponse(BaseValidatorModel):
    resolvedComponentVersions: List[ResolvedComponentVersion]
    ResponseMetadata: ResponseMetadata


class Component(BaseValidatorModel):
    arn: Optional[str] = None
    componentName: Optional[str] = None
    latestVersion: Optional[ComponentLatestVersion] = None


# This class is the input for the 'resolve_component_candidates' function.
class ResolveComponentCandidatesRequest(BaseValidatorModel):
    platform: Optional[ComponentPlatformUnion] = None
    componentCandidates: Optional[List[ComponentCandidate]] = None


class ComponentDeploymentSpecificationOutput(BaseValidatorModel):
    componentVersion: str
    configurationUpdate: Optional[ComponentConfigurationUpdateOutput] = None
    runWith: Optional[ComponentRunWith] = None


class ComponentDeploymentSpecification(BaseValidatorModel):
    componentVersion: str
    configurationUpdate: Optional[ComponentConfigurationUpdateUnion] = None
    runWith: Optional[ComponentRunWith] = None


# This class is the output for the 'list_effective_deployments' function.
class ListEffectiveDeploymentsResponse(BaseValidatorModel):
    effectiveDeployments: List[EffectiveDeployment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IoTJobExecutionsRolloutConfig(BaseValidatorModel):
    exponentialRate: Optional[IoTJobExponentialRolloutRate] = None
    maximumPerMinute: Optional[int] = None


class LambdaLinuxProcessParams(BaseValidatorModel):
    isolationMode: Optional[LambdaIsolationModeType] = None
    containerParams: Optional[LambdaContainerParams] = None


# This class is the output for the 'list_components' function.
class ListComponentsResponse(BaseValidatorModel):
    components: List[Component]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

ComponentDeploymentSpecificationUnion = Union[ComponentDeploymentSpecification, ComponentDeploymentSpecificationOutput]


class DeploymentIoTJobConfigurationOutput(BaseValidatorModel):
    jobExecutionsRolloutConfig: Optional[IoTJobExecutionsRolloutConfig] = None
    abortConfig: Optional[IoTJobAbortConfigOutput] = None
    timeoutConfig: Optional[IoTJobTimeoutConfig] = None


class DeploymentIoTJobConfiguration(BaseValidatorModel):
    jobExecutionsRolloutConfig: Optional[IoTJobExecutionsRolloutConfig] = None
    abortConfig: Optional[IoTJobAbortConfig] = None
    timeoutConfig: Optional[IoTJobTimeoutConfig] = None


class LambdaExecutionParameters(BaseValidatorModel):
    eventSources: Optional[List[LambdaEventSource]] = None
    maxQueueSize: Optional[int] = None
    maxInstancesCount: Optional[int] = None
    maxIdleTimeInSeconds: Optional[int] = None
    timeoutInSeconds: Optional[int] = None
    statusTimeoutInSeconds: Optional[int] = None
    pinned: Optional[bool] = None
    inputPayloadEncodingType: Optional[LambdaInputPayloadEncodingTypeType] = None
    execArgs: Optional[List[str]] = None
    environmentVariables: Optional[Dict[str, str]] = None
    linuxProcessParams: Optional[LambdaLinuxProcessParams] = None


# This class is the output for the 'get_deployment' function.
class GetDeploymentResponse(BaseValidatorModel):
    targetArn: str
    revisionId: str
    deploymentId: str
    deploymentName: str
    deploymentStatus: DeploymentStatusType
    iotJobId: str
    iotJobArn: str
    components: Dict[str, ComponentDeploymentSpecificationOutput]
    deploymentPolicies: DeploymentPolicies
    iotJobConfiguration: DeploymentIoTJobConfigurationOutput
    creationTimestamp: datetime
    isLatestForTarget: bool
    parentTargetArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata

DeploymentIoTJobConfigurationUnion = Union[DeploymentIoTJobConfiguration, DeploymentIoTJobConfigurationOutput]


class LambdaFunctionRecipeSource(BaseValidatorModel):
    lambdaArn: str
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    componentPlatforms: Optional[List[ComponentPlatformUnion]] = None
    componentDependencies: Optional[Dict[str, ComponentDependencyRequirement]] = None
    componentLambdaParameters: Optional[LambdaExecutionParameters] = None


# This class is the input for the 'create_deployment' function.
class CreateDeploymentRequest(BaseValidatorModel):
    targetArn: str
    deploymentName: Optional[str] = None
    components: Optional[Dict[str, ComponentDeploymentSpecificationUnion]] = None
    iotJobConfiguration: Optional[DeploymentIoTJobConfigurationUnion] = None
    deploymentPolicies: Optional[DeploymentPolicies] = None
    parentTargetArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None


# This class is the input for the 'create_component_version' function.
class CreateComponentVersionRequest(BaseValidatorModel):
    inlineRecipe: Optional[Blob] = None
    lambdaFunction: Optional[LambdaFunctionRecipeSource] = None
    tags: Optional[Dict[str, str]] = None
    clientToken: Optional[str] = None