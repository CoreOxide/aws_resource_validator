from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
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

class AssociateClientDeviceWithCoreDeviceEntryTypeDef(BaseValidatorModel):
    thingName: str

class AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef(BaseValidatorModel):
    thingName: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None

class AssociateServiceRoleToAccountRequestRequestTypeDef(BaseValidatorModel):
    roleArn: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssociatedClientDeviceTypeDef(BaseValidatorModel):
    thingName: Optional[str] = None
    associationTimestamp: Optional[datetime] = None

class DisassociateClientDeviceFromCoreDeviceEntryTypeDef(BaseValidatorModel):
    thingName: str

class DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef(BaseValidatorModel):
    thingName: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None

class CancelDeploymentRequestRequestTypeDef(BaseValidatorModel):
    deploymentId: str

class CloudComponentStatusTypeDef(BaseValidatorModel):
    componentState: Optional[CloudComponentStateType] = None
    message: Optional[str] = None
    errors: Optional[Dict[str, str]] = None
    vendorGuidance: Optional[VendorGuidanceType] = None
    vendorGuidanceMessage: Optional[str] = None

class ComponentCandidateTypeDef(BaseValidatorModel):
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    versionRequirements: Optional[Mapping[str, str]] = None

class ComponentConfigurationUpdateOutputTypeDef(BaseValidatorModel):
    merge: Optional[str] = None
    reset: Optional[List[str]] = None

class ComponentConfigurationUpdateTypeDef(BaseValidatorModel):
    merge: Optional[str] = None
    reset: Optional[Sequence[str]] = None

class ComponentDependencyRequirementTypeDef(BaseValidatorModel):
    versionRequirement: Optional[str] = None
    dependencyType: Optional[ComponentDependencyTypeType] = None

class ComponentPlatformOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None

class ComponentPlatformExtraOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None

class ComponentPlatformTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None

class SystemResourceLimitsTypeDef(BaseValidatorModel):
    memory: Optional[int] = None
    cpus: Optional[float] = None

class ComponentVersionListItemTypeDef(BaseValidatorModel):
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    arn: Optional[str] = None

class ConnectivityInfoTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    hostAddress: Optional[str] = None
    portNumber: Optional[int] = None
    metadata: Optional[str] = None

class CoreDeviceTypeDef(BaseValidatorModel):
    coreDeviceThingName: Optional[str] = None
    status: Optional[CoreDeviceStatusType] = None
    lastStatusUpdateTimestamp: Optional[datetime] = None

class DeleteComponentRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteCoreDeviceRequestRequestTypeDef(BaseValidatorModel):
    coreDeviceThingName: str

class DeleteDeploymentRequestRequestTypeDef(BaseValidatorModel):
    deploymentId: str

class DeploymentComponentUpdatePolicyTypeDef(BaseValidatorModel):
    timeoutInSeconds: Optional[int] = None
    action: Optional[DeploymentComponentUpdatePolicyActionType] = None

class DeploymentConfigurationValidationPolicyTypeDef(BaseValidatorModel):
    timeoutInSeconds: Optional[int] = None

class IoTJobTimeoutConfigTypeDef(BaseValidatorModel):
    inProgressTimeoutInMinutes: Optional[int] = None

class DeploymentTypeDef(BaseValidatorModel):
    targetArn: Optional[str] = None
    revisionId: Optional[str] = None
    deploymentId: Optional[str] = None
    deploymentName: Optional[str] = None
    creationTimestamp: Optional[datetime] = None
    deploymentStatus: Optional[DeploymentStatusType] = None
    isLatestForTarget: Optional[bool] = None
    parentTargetArn: Optional[str] = None

class DescribeComponentRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class EffectiveDeploymentStatusDetailsTypeDef(BaseValidatorModel):
    errorStack: Optional[List[str]] = None
    errorTypes: Optional[List[str]] = None

class GetComponentRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    recipeOutputFormat: Optional[RecipeOutputFormatType] = None

class GetComponentVersionArtifactRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    artifactName: str
    s3EndpointType: Optional[S3EndpointTypeType] = None
    iotEndpointType: Optional[IotEndpointTypeType] = None

class GetConnectivityInfoRequestRequestTypeDef(BaseValidatorModel):
    thingName: str

class GetCoreDeviceRequestRequestTypeDef(BaseValidatorModel):
    coreDeviceThingName: str

class GetDeploymentRequestRequestTypeDef(BaseValidatorModel):
    deploymentId: str

class InstalledComponentTypeDef(BaseValidatorModel):
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    lifecycleState: Optional[InstalledComponentLifecycleStateType] = None
    lifecycleStateDetails: Optional[str] = None
    isRoot: Optional[bool] = None
    lastStatusChangeTimestamp: Optional[datetime] = None
    lastReportedTimestamp: Optional[datetime] = None
    lastInstallationSource: Optional[str] = None
    lifecycleStatusCodes: Optional[List[str]] = None

class IoTJobAbortCriteriaTypeDef(BaseValidatorModel):
    failureType: IoTJobExecutionFailureTypeType
    action: Literal["CANCEL"]
    thresholdPercentage: float
    minNumberOfExecutedThings: int

class IoTJobRateIncreaseCriteriaTypeDef(BaseValidatorModel):
    numberOfNotifiedThings: Optional[int] = None
    numberOfSucceededThings: Optional[int] = None

class LambdaDeviceMountTypeDef(BaseValidatorModel):
    path: str
    permission: Optional[LambdaFilesystemPermissionType] = None
    addGroupOwner: Optional[bool] = None

class LambdaVolumeMountTypeDef(BaseValidatorModel):
    sourcePath: str
    destinationPath: str
    permission: Optional[LambdaFilesystemPermissionType] = None
    addGroupOwner: Optional[bool] = None

class LambdaEventSourceTypeDef(BaseValidatorModel):
    topic: str
    type: LambdaEventSourceTypeType

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListClientDevicesAssociatedWithCoreDeviceRequestRequestTypeDef(BaseValidatorModel):
    coreDeviceThingName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListComponentVersionsRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListComponentsRequestRequestTypeDef(BaseValidatorModel):
    scope: Optional[ComponentVisibilityScopeType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListCoreDevicesRequestRequestTypeDef(BaseValidatorModel):
    thingGroupArn: Optional[str] = None
    status: Optional[CoreDeviceStatusType] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDeploymentsRequestRequestTypeDef(BaseValidatorModel):
    targetArn: Optional[str] = None
    historyFilter: Optional[DeploymentHistoryFilterType] = None
    parentTargetArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListEffectiveDeploymentsRequestRequestTypeDef(BaseValidatorModel):
    coreDeviceThingName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListInstalledComponentsRequestRequestTypeDef(BaseValidatorModel):
    coreDeviceThingName: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    topologyFilter: Optional[InstalledComponentTopologyFilterType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ResolvedComponentVersionTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    recipe: Optional[bytes] = None
    vendorGuidance: Optional[VendorGuidanceType] = None
    message: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class BatchAssociateClientDeviceWithCoreDeviceRequestRequestTypeDef(BaseValidatorModel):
    coreDeviceThingName: str
    entries: Optional[Sequence[AssociateClientDeviceWithCoreDeviceEntryTypeDef]] = None

class AssociateServiceRoleToAccountResponseTypeDef(BaseValidatorModel):
    associatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchAssociateClientDeviceWithCoreDeviceResponseTypeDef(BaseValidatorModel):
    errorEntries: List[AssociateClientDeviceWithCoreDeviceErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CancelDeploymentResponseTypeDef(BaseValidatorModel):
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDeploymentResponseTypeDef(BaseValidatorModel):
    deploymentId: str
    iotJobId: str
    iotJobArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateServiceRoleFromAccountResponseTypeDef(BaseValidatorModel):
    disassociatedAt: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentResponseTypeDef(BaseValidatorModel):
    recipeOutputFormat: RecipeOutputFormatType
    recipe: bytes
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentVersionArtifactResponseTypeDef(BaseValidatorModel):
    preSignedUrl: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetCoreDeviceResponseTypeDef(BaseValidatorModel):
    coreDeviceThingName: str
    coreVersion: str
    platform: str
    architecture: str
    status: CoreDeviceStatusType
    lastStatusUpdateTimestamp: datetime
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetServiceRoleForAccountResponseTypeDef(BaseValidatorModel):
    associatedAt: str
    roleArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityInfoResponseTypeDef(BaseValidatorModel):
    version: str
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListClientDevicesAssociatedWithCoreDeviceResponseTypeDef(BaseValidatorModel):
    associatedClientDevices: List[AssociatedClientDeviceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateClientDeviceFromCoreDeviceRequestRequestTypeDef(BaseValidatorModel):
    coreDeviceThingName: str
    entries: Optional[Sequence[DisassociateClientDeviceFromCoreDeviceEntryTypeDef]] = None

class BatchDisassociateClientDeviceFromCoreDeviceResponseTypeDef(BaseValidatorModel):
    errorEntries: List[DisassociateClientDeviceFromCoreDeviceErrorEntryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateComponentVersionResponseTypeDef(BaseValidatorModel):
    arn: str
    componentName: str
    componentVersion: str
    creationTimestamp: datetime
    status: CloudComponentStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ComponentLatestVersionTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    componentVersion: Optional[str] = None
    creationTimestamp: Optional[datetime] = None
    description: Optional[str] = None
    publisher: Optional[str] = None
    platforms: Optional[List[ComponentPlatformOutputTypeDef]] = None

class DescribeComponentResponseTypeDef(BaseValidatorModel):
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

class ResolveComponentCandidatesRequestRequestTypeDef(BaseValidatorModel):
    platform: Optional[ComponentPlatformTypeDef] = None
    componentCandidates: Optional[Sequence[ComponentCandidateTypeDef]] = None

class ComponentRunWithTypeDef(BaseValidatorModel):
    posixUser: Optional[str] = None
    systemResourceLimits: Optional[SystemResourceLimitsTypeDef] = None
    windowsUser: Optional[str] = None

class ListComponentVersionsResponseTypeDef(BaseValidatorModel):
    componentVersions: List[ComponentVersionListItemTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetConnectivityInfoResponseTypeDef(BaseValidatorModel):
    connectivityInfo: List[ConnectivityInfoTypeDef]
    message: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateConnectivityInfoRequestRequestTypeDef(BaseValidatorModel):
    thingName: str
    connectivityInfo: Sequence[ConnectivityInfoTypeDef]

class ListCoreDevicesResponseTypeDef(BaseValidatorModel):
    coreDevices: List[CoreDeviceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentPoliciesTypeDef(BaseValidatorModel):
    failureHandlingPolicy: Optional[DeploymentFailureHandlingPolicyType] = None
    componentUpdatePolicy: Optional[DeploymentComponentUpdatePolicyTypeDef] = None
    configurationValidationPolicy: Optional[       DeploymentConfigurationValidationPolicyTypeDef     ] = None

class ListDeploymentsResponseTypeDef(BaseValidatorModel):
    deployments: List[DeploymentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EffectiveDeploymentTypeDef(BaseValidatorModel):
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

class ListInstalledComponentsResponseTypeDef(BaseValidatorModel):
    installedComponents: List[InstalledComponentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IoTJobAbortConfigOutputTypeDef(BaseValidatorModel):
    criteriaList: List[IoTJobAbortCriteriaTypeDef]

class IoTJobAbortConfigTypeDef(BaseValidatorModel):
    criteriaList: Sequence[IoTJobAbortCriteriaTypeDef]

class IoTJobExponentialRolloutRateTypeDef(BaseValidatorModel):
    baseRatePerMinute: int
    incrementFactor: float
    rateIncreaseCriteria: IoTJobRateIncreaseCriteriaTypeDef

class LambdaContainerParamsTypeDef(BaseValidatorModel):
    memorySizeInKB: Optional[int] = None
    mountROSysfs: Optional[bool] = None
    volumes: Optional[Sequence[LambdaVolumeMountTypeDef]] = None
    devices: Optional[Sequence[LambdaDeviceMountTypeDef]] = None

class ListClientDevicesAssociatedWithCoreDeviceRequestListClientDevicesAssociatedWithCoreDevicePaginateTypeDef(BaseValidatorModel):
    coreDeviceThingName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentVersionsRequestListComponentVersionsPaginateTypeDef(BaseValidatorModel):
    arn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListComponentsRequestListComponentsPaginateTypeDef(BaseValidatorModel):
    scope: Optional[ComponentVisibilityScopeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListCoreDevicesRequestListCoreDevicesPaginateTypeDef(BaseValidatorModel):
    thingGroupArn: Optional[str] = None
    status: Optional[CoreDeviceStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDeploymentsRequestListDeploymentsPaginateTypeDef(BaseValidatorModel):
    targetArn: Optional[str] = None
    historyFilter: Optional[DeploymentHistoryFilterType] = None
    parentTargetArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEffectiveDeploymentsRequestListEffectiveDeploymentsPaginateTypeDef(BaseValidatorModel):
    coreDeviceThingName: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstalledComponentsRequestListInstalledComponentsPaginateTypeDef(BaseValidatorModel):
    coreDeviceThingName: str
    topologyFilter: Optional[InstalledComponentTopologyFilterType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ResolveComponentCandidatesResponseTypeDef(BaseValidatorModel):
    resolvedComponentVersions: List[ResolvedComponentVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ComponentTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    componentName: Optional[str] = None
    latestVersion: Optional[ComponentLatestVersionTypeDef] = None

class ComponentDeploymentSpecificationOutputTypeDef(BaseValidatorModel):
    componentVersion: str
    configurationUpdate: Optional[ComponentConfigurationUpdateOutputTypeDef] = None
    runWith: Optional[ComponentRunWithTypeDef] = None

class ComponentDeploymentSpecificationTypeDef(BaseValidatorModel):
    componentVersion: str
    configurationUpdate: Optional[ComponentConfigurationUpdateTypeDef] = None
    runWith: Optional[ComponentRunWithTypeDef] = None

class ListEffectiveDeploymentsResponseTypeDef(BaseValidatorModel):
    effectiveDeployments: List[EffectiveDeploymentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class IoTJobExecutionsRolloutConfigTypeDef(BaseValidatorModel):
    exponentialRate: Optional[IoTJobExponentialRolloutRateTypeDef] = None
    maximumPerMinute: Optional[int] = None

class LambdaLinuxProcessParamsTypeDef(BaseValidatorModel):
    isolationMode: Optional[LambdaIsolationModeType] = None
    containerParams: Optional[LambdaContainerParamsTypeDef] = None

class ListComponentsResponseTypeDef(BaseValidatorModel):
    components: List[ComponentTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeploymentIoTJobConfigurationOutputTypeDef(BaseValidatorModel):
    jobExecutionsRolloutConfig: Optional[IoTJobExecutionsRolloutConfigTypeDef] = None
    abortConfig: Optional[IoTJobAbortConfigOutputTypeDef] = None
    timeoutConfig: Optional[IoTJobTimeoutConfigTypeDef] = None

class DeploymentIoTJobConfigurationTypeDef(BaseValidatorModel):
    jobExecutionsRolloutConfig: Optional[IoTJobExecutionsRolloutConfigTypeDef] = None
    abortConfig: Optional[IoTJobAbortConfigTypeDef] = None
    timeoutConfig: Optional[IoTJobTimeoutConfigTypeDef] = None

class LambdaExecutionParametersTypeDef(BaseValidatorModel):
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

class GetDeploymentResponseTypeDef(BaseValidatorModel):
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

class CreateDeploymentRequestRequestTypeDef(BaseValidatorModel):
    targetArn: str
    deploymentName: Optional[str] = None
    components: Optional[Mapping[str, ComponentDeploymentSpecificationUnionTypeDef]] = None
    iotJobConfiguration: Optional[DeploymentIoTJobConfigurationTypeDef] = None
    deploymentPolicies: Optional[DeploymentPoliciesTypeDef] = None
    parentTargetArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

class LambdaFunctionRecipeSourceTypeDef(BaseValidatorModel):
    lambdaArn: str
    componentName: Optional[str] = None
    componentVersion: Optional[str] = None
    componentPlatforms: Optional[Sequence[ComponentPlatformTypeDef]] = None
    componentDependencies: Optional[Mapping[str, ComponentDependencyRequirementTypeDef]] = None
    componentLambdaParameters: Optional[LambdaExecutionParametersTypeDef] = None

class CreateComponentVersionRequestRequestTypeDef(BaseValidatorModel):
    inlineRecipe: Optional[BlobTypeDef] = None
    lambdaFunction: Optional[LambdaFunctionRecipeSourceTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    clientToken: Optional[str] = None

