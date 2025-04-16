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
from aws_resource_validator.pydantic_models.greengrassv2_constants import *

class AssociateClientDeviceWithCoreDeviceEntry(BaseValidatorModel):
    thingName: str


class AssociateClientDeviceWithCoreDeviceErrorEntry(BaseValidatorModel):
    thingName: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None


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
    versionRequirements: Optional[Mapping[str, str]] = None


class ComponentConfigurationUpdateOutput(BaseValidatorModel):
    merge: Optional[str] = None
    reset: Optional[List[str]] = None


class ComponentConfigurationUpdate(BaseValidatorModel):
    merge: Optional[str] = None
    reset: Optional[Sequence[str]] = None


class ComponentDependencyRequirement(BaseValidatorModel):
    versionRequirement: Optional[str] = None
    dependencyType: Optional[ComponentDependencyTypeType] = None


class ComponentPlatformOutput(BaseValidatorModel):
    name: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None


class ComponentPlatform(BaseValidatorModel):
    name: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None


class SystemResourceLimits(BaseValidatorModel):
    memory: Optional[int] = None
    cpus: Optional[float] = None


class ComponentVersionListItem(BaseValidatorModel):
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    arn: Optional[str] = None


class CoreDevice(BaseValidatorModel):
    coreDeviceThingName: Optional[str] = None
    status: Optional[CoreDeviceStatusType] = None
    lastStatusUpdateTimestamp: Optional[datetime] = None
    platform: Optional[str] = None
    architecture: Optional[str] = None
    runtime: Optional[str] = None


class DeleteComponentRequest(BaseValidatorModel):
    arn: str


class DeleteCoreDeviceRequest(BaseValidatorModel):
    coreDeviceThingName: str


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


class DescribeComponentRequest(BaseValidatorModel):
    arn: str


class EffectiveDeploymentStatusDetails(BaseValidatorModel):
    errorStack: Optional[List[str]] = None
    errorTypes: Optional[List[str]] = None


class GetComponentRequest(BaseValidatorModel):
    arn: str
    recipeOutputFormat: Optional[RecipeOutputFormatType] = None


class GetComponentVersionArtifactRequest(BaseValidatorModel):
    arn: str
    artifactName: str
    s3EndpointType: Optional[S3EndpointTypeType] = None
    iotEndpointType: Optional[IotEndpointTypeType] = None


class GetConnectivityInfoRequest(BaseValidatorModel):
    thingName: str


class GetCoreDeviceRequest(BaseValidatorModel):
    coreDeviceThingName: str


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
    action: Literal["CANCEL"]
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


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListClientDevicesAssociatedWithCoreDeviceRequest(BaseValidatorModel):
    coreDeviceThingName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListComponentVersionsRequest(BaseValidatorModel):
    arn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListComponentsRequest(BaseValidatorModel):
    scope: Optional[ComponentVisibilityScopeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListCoreDevicesRequest(BaseValidatorModel):
    thingGroupArn: Optional[str] = None
    status: Optional[CoreDeviceStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    runtime: Optional[str] = None


class ListDeploymentsRequest(BaseValidatorModel):
    targetArn: Optional[str] = None
    historyFilter: Optional[DeploymentHistoryFilterType] = None
    parentTargetArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListEffectiveDeploymentsRequest(BaseValidatorModel):
    coreDeviceThingName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListInstalledComponentsRequest(BaseValidatorModel):
    coreDeviceThingName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    topologyFilter: Optional[InstalledComponentTopologyFilterType] = None


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
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class BatchAssociateClientDeviceWithCoreDeviceRequest(BaseValidatorModel):
    coreDeviceThingName: str
    entries: Optional[Sequence[AssociateClientDeviceWithCoreDeviceEntry]] = None


class AssociateServiceRoleToAccountResponse(BaseValidatorModel):
    associatedAt: str
    ResponseMetadata: ResponseMetadata


class BatchAssociateClientDeviceWithCoreDeviceResponse(BaseValidatorModel):
    errorEntries: List[AssociateClientDeviceWithCoreDeviceErrorEntry]
    ResponseMetadata: ResponseMetadata


class CancelDeploymentResponse(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadata


class CreateDeploymentResponse(BaseValidatorModel):
    deploymentId: str
    iotJobId: str
    iotJobArn: str
    ResponseMetadata: ResponseMetadata


class DisassociateServiceRoleFromAccountResponse(BaseValidatorModel):
    disassociatedAt: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetComponentResponse(BaseValidatorModel):
    recipeOutputFormat: RecipeOutputFormatType
    recipe: bytes
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetComponentVersionArtifactResponse(BaseValidatorModel):
    preSignedUrl: str
    ResponseMetadata: ResponseMetadata


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


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateConnectivityInfoResponse(BaseValidatorModel):
    version: str
    message: str
    ResponseMetadata: ResponseMetadata


class ListClientDevicesAssociatedWithCoreDeviceResponse(BaseValidatorModel):
    associatedClientDevices: List[AssociatedClientDevice]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class BatchDisassociateClientDeviceFromCoreDeviceRequest(BaseValidatorModel):
    coreDeviceThingName: str
    entries: Optional[Sequence[DisassociateClientDeviceFromCoreDeviceEntry]] = None


class BatchDisassociateClientDeviceFromCoreDeviceResponse(BaseValidatorModel):
    errorEntries: List[DisassociateClientDeviceFromCoreDeviceErrorEntry]
    ResponseMetadata: ResponseMetadata


class CreateComponentVersionResponse(BaseValidatorModel):
    arn: str
    componentName: str
    componentVersion: str
    creationTimestamp: datetime
    status: CloudComponentStatus
    ResponseMetadata: ResponseMetadata


class ComponentLatestVersion(BaseValidatorModel):
    arn: Optional[str] = None
    componentVersion: Optional[str] = None
    creationTimestamp: Optional[datetime] = None
    description: Optional[str] = None
    publisher: Optional[str] = None
    platforms: Optional[List[ComponentPlatformOutput]] = None


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


class ComponentRunWith(BaseValidatorModel):
    posixUser: Optional[str] = None
    systemResourceLimits: Optional[SystemResourceLimits] = None
    windowsUser: Optional[str] = None


class ListComponentVersionsResponse(BaseValidatorModel):
    componentVersions: List[ComponentVersionListItem]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConnectivityInfo(BaseValidatorModel):
    pass


class GetConnectivityInfoResponse(BaseValidatorModel):
    connectivityInfo: List[ConnectivityInfo]
    message: str
    ResponseMetadata: ResponseMetadata


class UpdateConnectivityInfoRequest(BaseValidatorModel):
    thingName: str
    connectivityInfo: Sequence[ConnectivityInfo]


class ListCoreDevicesResponse(BaseValidatorModel):
    coreDevices: List[CoreDevice]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DeploymentPolicies(BaseValidatorModel):
    failureHandlingPolicy: Optional[DeploymentFailureHandlingPolicyType] = None
    componentUpdatePolicy: Optional[DeploymentComponentUpdatePolicy] = None
    configurationValidationPolicy: Optional[DeploymentConfigurationValidationPolicy] = None


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


class ListInstalledComponentsResponse(BaseValidatorModel):
    installedComponents: List[InstalledComponent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IoTJobAbortConfigOutput(BaseValidatorModel):
    criteriaList: List[IoTJobAbortCriteria]


class IoTJobAbortConfig(BaseValidatorModel):
    criteriaList: Sequence[IoTJobAbortCriteria]


class IoTJobExponentialRolloutRate(BaseValidatorModel):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: IoTJobRateIncreaseCriteria


class LambdaContainerParams(BaseValidatorModel):
    memorySizeInKB: Optional[int] = None
    mountROSysfs: Optional[bool] = None
    volumes: Optional[Sequence[LambdaVolumeMount]] = None
    devices: Optional[Sequence[LambdaDeviceMount]] = None


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


class ResolveComponentCandidatesResponse(BaseValidatorModel):
    resolvedComponentVersions: List[ResolvedComponentVersion]
    ResponseMetadata: ResponseMetadata


class Component(BaseValidatorModel):
    arn: Optional[str] = None
    componentName: Optional[str] = None
    latestVersion: Optional[ComponentLatestVersion] = None


class ComponentPlatformUnion(BaseValidatorModel):
    pass


class ResolveComponentCandidatesRequest(BaseValidatorModel):
    platform: Optional[ComponentPlatformUnion] = None
    componentCandidates: Optional[Sequence[ComponentCandidate]] = None


class ComponentDeploymentSpecificationOutput(BaseValidatorModel):
    componentVersion: str
    configurationUpdate: Optional[ComponentConfigurationUpdateOutput] = None
    runWith: Optional[ComponentRunWith] = None


class ComponentConfigurationUpdateUnion(BaseValidatorModel):
    pass


class ComponentDeploymentSpecification(BaseValidatorModel):
    componentVersion: str
    configurationUpdate: Optional[ComponentConfigurationUpdateUnion] = None
    runWith: Optional[ComponentRunWith] = None


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


class ListComponentsResponse(BaseValidatorModel):
    components: List[Component]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DeploymentIoTJobConfigurationOutput(BaseValidatorModel):
    jobExecutionsRolloutConfig: Optional[IoTJobExecutionsRolloutConfig] = None
    abortConfig: Optional[IoTJobAbortConfigOutput] = None
    timeoutConfig: Optional[IoTJobTimeoutConfig] = None


class DeploymentIoTJobConfiguration(BaseValidatorModel):
    jobExecutionsRolloutConfig: Optional[IoTJobExecutionsRolloutConfig] = None
    abortConfig: Optional[IoTJobAbortConfig] = None
    timeoutConfig: Optional[IoTJobTimeoutConfig] = None


class LambdaEventSource(BaseValidatorModel):
    pass


class LambdaExecutionParameters(BaseValidatorModel):
    eventSources: Optional[Sequence[LambdaEventSource]] = None
    maxQueueSize: Optional[int] = None
    maxInstancesCount: Optional[int] = None
    maxIdleTimeInSeconds: Optional[int] = None
    timeoutInSeconds: Optional[int] = None
    statusTimeoutInSeconds: Optional[int] = None
    pinned: Optional[bool] = None
    inputPayloadEncodingType: Optional[LambdaInputPayloadEncodingTypeType] = None
    execArgs: Optional[Sequence[str]] = None
    environmentVariables: Optional[Mapping[str, str]] = None
    linuxProcessParams: Optional[LambdaLinuxProcessParams] = None


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


class LambdaFunctionRecipeSource(BaseValidatorModel):
    lambdaArn: str
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    componentPlatforms: Optional[Sequence[ComponentPlatformUnion]] = None
    componentDependencies: Optional[Mapping[str, ComponentDependencyRequirement]] = None
    componentLambdaParameters: Optional[LambdaExecutionParameters] = None


class DeploymentIoTJobConfigurationUnion(BaseValidatorModel):
    pass


class ComponentDeploymentSpecificationUnion(BaseValidatorModel):
    pass


class CreateDeploymentRequest(BaseValidatorModel):
    targetArn: str
    deploymentName: Optional[str] = None
    components: Optional[Mapping[str, ComponentDeploymentSpecificationUnion]] = None
    iotJobConfiguration: Optional[DeploymentIoTJobConfigurationUnion] = None
    deploymentPolicies: Optional[DeploymentPolicies] = None
    parentTargetArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None


class Blob(BaseValidatorModel):
    pass


class CreateComponentVersionRequest(BaseValidatorModel):
    inlineRecipe: Optional[Blob] = None
    lambdaFunction: Optional[LambdaFunctionRecipeSource] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None


