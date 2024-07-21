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
from aws_resource_validator.pydantic_models.greengrassv2_constants import *

class AssociateClientDeviceWithCoreDeviceEntryTypeDef(BaseModel):
    thingName: str

class AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef(BaseModel):
    thingName: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None

class AssociateServiceRoleToAccountRequestRequestTypeDef(BaseModel):
    roleArn: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssociatedClientDeviceTypeDef(BaseModel):
    thingName: Optional[str] = None
    associationTimestamp: Optional[datetime] = None

class DisassociateClientDeviceFromCoreDeviceEntryTypeDef(BaseModel):
    thingName: str

class DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef(BaseModel):
    thingName: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None

class CancelDeploymentRequestRequestTypeDef(BaseModel):
    deploymentId: str

class CloudComponentStatusTypeDef(BaseModel):
    componentState: Optional[CloudComponentStateType] = None
    message: Optional[str] = None
    errors: Optional[Dict[str, str]] = None
    vendorGuidance: Optional[VendorGuidanceType] = None
    vendorGuidanceMessage: Optional[str] = None

class ComponentCandidateTypeDef(BaseModel):
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    versionRequirements: Optional[Mapping[str, str]] = None

class ComponentConfigurationUpdateOutputTypeDef(BaseModel):
    merge: Optional[str] = None
    reset: Optional[List[str]] = None

class ComponentConfigurationUpdateTypeDef(BaseModel):
    merge: Optional[str] = None
    reset: Optional[Sequence[str]] = None

class ComponentDependencyRequirementTypeDef(BaseModel):
    versionRequirement: Optional[str] = None
    dependencyType: Optional[ComponentDependencyTypeType] = None

class ComponentPlatformOutputTypeDef(BaseModel):
    name: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None

class ComponentPlatformExtraOutputTypeDef(BaseModel):
    name: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None

class ComponentPlatformTypeDef(BaseModel):
    name: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None

class SystemResourceLimitsTypeDef(BaseModel):
    memory: Optional[int] = None
    cpus: Optional[float] = None

class ComponentVersionListItemTypeDef(BaseModel):
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    arn: Optional[str] = None

class ConnectivityInfoTypeDef(BaseModel):
    id: Optional[str] = None
    hostAddress: Optional[str] = None
    portNumber: Optional[int] = None
    metadata: Optional[str] = None

class CoreDeviceTypeDef(BaseModel):
    coreDeviceThingName: Optional[str] = None
    status: Optional[CoreDeviceStatusType] = None
    lastStatusUpdateTimestamp: Optional[datetime] = None

class DeleteComponentRequestRequestTypeDef(BaseModel):
    arn: str

class DeleteCoreDeviceRequestRequestTypeDef(BaseModel):
    coreDeviceThingName: str

class DeleteDeploymentRequestRequestTypeDef(BaseModel):
    deploymentId: str

class DeploymentComponentUpdatePolicyTypeDef(BaseModel):
    timeoutInSeconds: Optional[int] = None
    action: Optional[DeploymentComponentUpdatePolicyActionType] = None

class DeploymentConfigurationValidationPolicyTypeDef(BaseModel):
    timeoutInSeconds: Optional[int] = None

class IoTJobTimeoutConfigTypeDef(BaseModel):
    inProgressTimeoutInMinutes: Optional[int] = None

class DeploymentTypeDef(BaseModel):
    targetArn: Optional[str] = None
    revisionId: Optional[str] = None
    deploymentId: Optional[str] = None
    deploymentName: Optional[str] = None
    creationTimestamp: Optional[datetime] = None
    deploymentStatus: Optional[DeploymentStatusType] = None
    isLatestForTarget: Optional[bool] = None
    parentTargetArn: Optional[str] = None

class DescribeComponentRequestRequestTypeDef(BaseModel):
    arn: str

class EffectiveDeploymentStatusDetailsTypeDef(BaseModel):
    errorStack: Optional[List[str]] = None
    errorTypes: Optional[List[str]] = None

class GetComponentRequestRequestTypeDef(BaseModel):
    arn: str
    recipeOutputFormat: Optional[RecipeOutputFormatType] = None

class GetComponentVersionArtifactRequestRequestTypeDef(BaseModel):
    arn: str
    artifactName: str
    s3EndpointType: Optional[S3EndpointTypeType] = None
    iotEndpointType: Optional[IotEndpointTypeType] = None

class GetConnectivityInfoRequestRequestTypeDef(BaseModel):
    thingName: str

class GetCoreDeviceRequestRequestTypeDef(BaseModel):
    coreDeviceThingName: str

class GetDeploymentRequestRequestTypeDef(BaseModel):
    deploymentId: str

class InstalledComponentTypeDef(BaseModel):
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    lifecycleState: Optional[InstalledComponentLifecycleStateType] = None
    lifecycleStateDetails: Optional[str] = None
    isRoot: Optional[bool] = None
    lastStatusChangeTimestamp: Optional[datetime] = None
    lastReportedTimestamp: Optional[datetime] = None
    lastInstallationSource: Optional[str] = None
    lifecycleStatusCodes: Optional[List[str]] = None

class IoTJobAbortCriteriaTypeDef(BaseModel):
    failureType: IoTJobExecutionFailureTypeType
    action: Literal["CANCEL"]
    thresholdPercentage: float
    minNumberOfExecutedThings: int

class IoTJobRateIncreaseCriteriaTypeDef(BaseModel):
    numberOfNotifiedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None

class LambdaDeviceMountTypeDef(BaseModel):
    path: str
    permission: Optional[LambdaFilesystemPermissionType] = None
    addGroupOwner: Optional[bool] = None

class LambdaVolumeMountTypeDef(BaseModel):
    sourcePath: str
    destinationPath: str
    permission: Optional[LambdaFilesystemPermissionType] = None
    addGroupOwner: Optional[bool] = None

class LambdaEventSourceTypeDef(BaseModel):
    topic: str
    type: LambdaEventSourceTypeType

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef(BaseModel):
    coreDeviceThingName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListComponentVersionsRequestRequestTypeDef(BaseModel):
    arn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListComponentsRequestRequestTypeDef(BaseModel):
    scope: Optional[ComponentVisibilityScopeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListCoreDevicesRequestRequestTypeDef(BaseModel):
    thingGroupArn: Optional[str] = None
    status: Optional[CoreDeviceStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDeploymentsRequestRequestTypeDef(BaseModel):
    targetArn: Optional[str] = None
    historyFilter: Optional[DeploymentHistoryFilterType] = None
    parentTargetArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEffectiveDeploymentsRequestRequestTypeDef(BaseModel):
    coreDeviceThingName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListInstalledComponentsRequestRequestTypeDef(BaseModel):
    coreDeviceThingName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    topologyFilter: Optional[InstalledComponentTopologyFilterType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ResolvedComponentVersionTypeDef(BaseModel):
    arn: Optional[str] = None
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    recipe: Optional[bytes] = None
    vendorGuidance: Optional[VendorGuidanceType] = None
    message: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class BatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef(BaseModel):
    coreDeviceThingName: str
    entries: Optional[Sequence[AssociateClientDeviceWithCoreDeviceEntryTypeDef]] = None

class AssociateServiceRoleToAccountResponseTypeDef(BaseModel):
    associatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef(BaseModel):
    errorEntries: List[AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelDeploymentResponseTypeDef(BaseModel):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResponseTypeDef(BaseModel):
    deploymentId: str
    iotJobId: str
    iotJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateServiceRoleFromAccountResponseTypeDef(BaseModel):
    disassociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentResponseTypeDef(BaseModel):
    recipeOutputFormat: RecipeOutputFormatType
    recipe: bytes
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentVersionArtifactResponseTypeDef(BaseModel):
    preSignedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreDeviceResponseTypeDef(BaseModel):
    coreDeviceThingName: str
    coreVersion: str
    platform: str
    architecture: str
    status: CoreDeviceStatusType
    lastStatusUpdateTimestamp: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceRoleForAccountResponseTypeDef(BaseModel):
    associatedAt: str
    roleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityInfoResponseTypeDef(BaseModel):
    version: str
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef(BaseModel):
    associatedClientDevices: List[AssociatedClientDeviceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef(BaseModel):
    coreDeviceThingName: str
    entries: Optional[Sequence[DisassociateClientDeviceFromCoreDeviceEntryTypeDef]] = None

class BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef(BaseModel):
    errorEntries: List[DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateComponentVersionResponseTypeDef(BaseModel):
    arn: str
    componentName: str
    componentVersion: str
    creationTimestamp: datetime
    status: CloudComponentStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ComponentLatestVersionTypeDef(BaseModel):
    arn: Optional[str] = None
    componentVersion: Optional[str] = None
    creationTimestamp: Optional[datetime] = None
    description: Optional[str] = None
    publisher: Optional[str] = None
    platforms: Optional[List[ComponentPlatformOutputTypeDef]] = None

class DescribeComponentResponseTypeDef(BaseModel):
    arn: str
    componentName: str
    componentVersion: str
    creationTimestamp: datetime
    publisher: str
    description: str
    status: CloudComponentStatusTypeDef
    platforms: List[ComponentPlatformOutputTypeDef]
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class ResolveComponentCandidatesRequestRequestTypeDef(BaseModel):
    platform: Optional[ComponentPlatformTypeDef] = None
    componentCandidates: Optional[Sequence[ComponentCandidateTypeDef]] = None

class ComponentRunWithTypeDef(BaseModel):
    posixUser: Optional[str] = None
    systemResourceLimits: Optional[SystemResourceLimitsTypeDef] = None
    windowsUser: Optional[str] = None

class ListComponentVersionsResponseTypeDef(BaseModel):
    componentVersions: List[ComponentVersionListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectivityInfoResponseTypeDef(BaseModel):
    connectivityInfo: List[ConnectivityInfoTypeDef]
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityInfoRequestRequestTypeDef(BaseModel):
    thingName: str
    connectivityInfo: Sequence[ConnectivityInfoTypeDef]

class ListCoreDevicesResponseTypeDef(BaseModel):
    coreDevices: List[CoreDeviceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentPoliciesTypeDef(BaseModel):
    failureHandlingPolicy: Optional[DeploymentFailureHandlingPolicyType] = None
    componentUpdatePolicy: Optional[DeploymentComponentUpdatePolicyTypeDef] = None
    configurationValidationPolicy: Optional[       DeploymentConfigurationValidationPolicyTypeDef     ] = None

class ListDeploymentsResponseTypeDef(BaseModel):
    deployments: List[DeploymentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EffectiveDeploymentTypeDef(BaseModel):
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
    statusDetails: Optional[EffectiveDeploymentStatusDetailsTypeDef] = None

class ListInstalledComponentsResponseTypeDef(BaseModel):
    installedComponents: List[InstalledComponentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IoTJobAbortConfigOutputTypeDef(BaseModel):
    criteriaList: List[IoTJobAbortCriteriaTypeDef]

class IoTJobAbortConfigTypeDef(BaseModel):
    criteriaList: Sequence[IoTJobAbortCriteriaTypeDef]

class IoTJobExponentialRolloutRateTypeDef(BaseModel):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: IoTJobRateIncreaseCriteriaTypeDef

class LambdaContainerParamsTypeDef(BaseModel):
    memorySizeInKB: Optional[int] = None
    mountROSysfs: Optional[bool] = None
    volumes: Optional[Sequence[LambdaVolumeMountTypeDef]] = None
    devices: Optional[Sequence[LambdaDeviceMountTypeDef]] = None

class ListClientDevicesAssociatedWithCoreDeviceRequestListClientDevicesAssociatedWithCoreDevicePaginateTypeDef(BaseModel):
    coreDeviceThingName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentVersionsRequestListComponentVersionsPaginateTypeDef(BaseModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentsRequestListComponentsPaginateTypeDef(BaseModel):
    scope: Optional[ComponentVisibilityScopeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCoreDevicesRequestListCoreDevicesPaginateTypeDef(BaseModel):
    thingGroupArn: Optional[str] = None
    status: Optional[CoreDeviceStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsRequestListDeploymentsPaginateTypeDef(BaseModel):
    targetArn: Optional[str] = None
    historyFilter: Optional[DeploymentHistoryFilterType] = None
    parentTargetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEffectiveDeploymentsRequestListEffectiveDeploymentsPaginateTypeDef(BaseModel):
    coreDeviceThingName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstalledComponentsRequestListInstalledComponentsPaginateTypeDef(BaseModel):
    coreDeviceThingName: str
    topologyFilter: Optional[InstalledComponentTopologyFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ResolveComponentCandidatesResponseTypeDef(BaseModel):
    resolvedComponentVersions: List[ResolvedComponentVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ComponentTypeDef(BaseModel):
    arn: Optional[str] = None
    componentName: Optional[str] = None
    latestVersion: Optional[ComponentLatestVersionTypeDef] = None

class ComponentDeploymentSpecificationOutputTypeDef(BaseModel):
    componentVersion: str
    configurationUpdate: Optional[ComponentConfigurationUpdateOutputTypeDef] = None
    runWith: Optional[ComponentRunWithTypeDef] = None

class ComponentDeploymentSpecificationTypeDef(BaseModel):
    componentVersion: str
    configurationUpdate: Optional[ComponentConfigurationUpdateTypeDef] = None
    runWith: Optional[ComponentRunWithTypeDef] = None

class ListEffectiveDeploymentsResponseTypeDef(BaseModel):
    effectiveDeployments: List[EffectiveDeploymentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IoTJobExecutionsRolloutConfigTypeDef(BaseModel):
    exponentialRate: Optional[IoTJobExponentialRolloutRateTypeDef] = None
    maximumPerMinute: Optional[int] = None

class LambdaLinuxProcessParamsTypeDef(BaseModel):
    isolationMode: Optional[LambdaIsolationModeType] = None
    containerParams: Optional[LambdaContainerParamsTypeDef] = None

class ListComponentsResponseTypeDef(BaseModel):
    components: List[ComponentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentIoTJobConfigurationOutputTypeDef(BaseModel):
    jobExecutionsRolloutConfig: Optional[IoTJobExecutionsRolloutConfigTypeDef] = None
    abortConfig: Optional[IoTJobAbortConfigOutputTypeDef] = None
    timeoutConfig: Optional[IoTJobTimeoutConfigTypeDef] = None

class DeploymentIoTJobConfigurationTypeDef(BaseModel):
    jobExecutionsRolloutConfig: Optional[IoTJobExecutionsRolloutConfigTypeDef] = None
    abortConfig: Optional[IoTJobAbortConfigTypeDef] = None
    timeoutConfig: Optional[IoTJobTimeoutConfigTypeDef] = None

class LambdaExecutionParametersTypeDef(BaseModel):
    eventSources: Optional[Sequence[LambdaEventSourceTypeDef]] = None
    maxQueueSize: Optional[int] = None
    maxInstancesCount: Optional[int] = None
    maxIdleTimeInSeconds: Optional[int] = None
    timeoutInSeconds: Optional[int] = None
    statusTimeoutInSeconds: Optional[int] = None
    pinned: Optional[bool] = None
    inputPayloadEncodingType: Optional[LambdaInputPayloadEncodingTypeType] = None
    execArgs: Optional[Sequence[str]] = None
    environmentVariables: Optional[Mapping[str, str]] = None
    linuxProcessParams: Optional[LambdaLinuxProcessParamsTypeDef] = None

class GetDeploymentResponseTypeDef(BaseModel):
    targetArn: str
    revisionId: str
    deploymentId: str
    deploymentName: str
    deploymentStatus: DeploymentStatusType
    iotJobId: str
    iotJobArn: str
    components: Dict[str, ComponentDeploymentSpecificationOutputTypeDef]
    deploymentPolicies: DeploymentPoliciesTypeDef
    iotJobConfiguration: DeploymentIoTJobConfigurationOutputTypeDef
    creationTimestamp: datetime
    isLatestForTarget: bool
    parentTargetArn: str
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentRequestRequestTypeDef(BaseModel):
    targetArn: str
    deploymentName: Optional[str] = None
    components: Optional[Mapping[str, ComponentDeploymentSpecificationUnionTypeDef]] = None
    iotJobConfiguration: Optional[DeploymentIoTJobConfigurationTypeDef] = None
    deploymentPolicies: Optional[DeploymentPoliciesTypeDef] = None
    parentTargetArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

class LambdaFunctionRecipeSourceTypeDef(BaseModel):
    lambdaArn: str
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    componentPlatforms: Optional[Sequence[ComponentPlatformTypeDef]] = None
    componentDependencies: Optional[Mapping[str, ComponentDependencyRequirementTypeDef]] = None
    componentLambdaParameters: Optional[LambdaExecutionParametersTypeDef] = None

class CreateComponentVersionRequestRequestTypeDef(BaseModel):
    inlineRecipe: Optional[BlobTypeDef] = None
    lambdaFunction: Optional[LambdaFunctionRecipeSourceTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

