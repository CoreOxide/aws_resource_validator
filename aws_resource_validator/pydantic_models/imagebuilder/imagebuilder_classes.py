from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.imagebuilder.imagebuilder_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class SeverityCounts(BaseValidatorModel):
    all: Optional[int] = None
    critical: Optional[int] = None
    high: Optional[int] = None
    medium: Optional[int] = None


class SystemsManagerAgent(BaseValidatorModel):
    uninstallAfterBuild: Optional[bool] = None


class LaunchPermissionConfigurationOutput(BaseValidatorModel):
    userIds: Optional[List[str]] = None
    userGroups: Optional[List[str]] = None
    organizationArns: Optional[List[str]] = None
    organizationalUnitArns: Optional[List[str]] = None


class ImageState(BaseValidatorModel):
    status: Optional[ImageStatusType] = None
    reason: Optional[str] = None


class CancelImageCreationRequest(BaseValidatorModel):
    imageBuildVersionArn: str
    clientToken: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelLifecycleExecutionRequest(BaseValidatorModel):
    lifecycleExecutionId: str
    clientToken: str


class ComponentParameterOutput(BaseValidatorModel):
    name: str
    value: List[str]


class ComponentParameterDetail(BaseValidatorModel):
    name: str
    type: str
    defaultValue: Optional[List[str]] = None
    description: Optional[str] = None


class ComponentParameter(BaseValidatorModel):
    name: str
    value: List[str]


class ComponentState(BaseValidatorModel):
    status: Optional[ComponentStatusType] = None
    reason: Optional[str] = None


class ProductCodeListItem(BaseValidatorModel):
    productCodeId: str
    productCodeType: Literal['marketplace']


class TargetContainerRepository(BaseValidatorModel):
    service: Literal['ECR']
    repositoryName: str


class ContainerRecipeSummary(BaseValidatorModel):
    arn: Optional[str] = None
    containerType: Optional[Literal['DOCKER']] = None
    name: Optional[str] = None
    platform: Optional[PlatformType] = None
    owner: Optional[str] = None
    parentImage: Optional[str] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Container(BaseValidatorModel):
    region: Optional[str] = None
    imageUris: Optional[List[str]] = None


class CreateComponentRequest(BaseValidatorModel):
    name: str
    semanticVersion: str
    platform: PlatformType
    clientToken: str
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    supportedOsVersions: Optional[List[str]] = None
    data: Optional[str] = None
    uri: Optional[str] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ImageTestsConfiguration(BaseValidatorModel):
    imageTestsEnabled: Optional[bool] = None
    timeoutMinutes: Optional[int] = None


class Schedule(BaseValidatorModel):
    scheduleExpression: Optional[str] = None
    timezone: Optional[str] = None
    pipelineExecutionStartCondition: Optional[PipelineExecutionStartConditionType] = None


class InstanceMetadataOptions(BaseValidatorModel):
    httpTokens: Optional[str] = None
    httpPutResponseHopLimit: Optional[int] = None


class Placement(BaseValidatorModel):
    availabilityZone: Optional[str] = None
    tenancy: Optional[TenancyTypeType] = None
    hostId: Optional[str] = None
    hostResourceGroupArn: Optional[str] = None


class CreateWorkflowRequest(BaseValidatorModel):
    name: str
    semanticVersion: str
    clientToken: str
    type: WorkflowTypeType
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    data: Optional[str] = None
    uri: Optional[str] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CvssScoreAdjustment(BaseValidatorModel):
    metric: Optional[str] = None
    reason: Optional[str] = None


class CvssScore(BaseValidatorModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None
    version: Optional[str] = None
    source: Optional[str] = None


class DeleteComponentRequest(BaseValidatorModel):
    componentBuildVersionArn: str


class DeleteContainerRecipeRequest(BaseValidatorModel):
    containerRecipeArn: str


class DeleteDistributionConfigurationRequest(BaseValidatorModel):
    distributionConfigurationArn: str


class DeleteImagePipelineRequest(BaseValidatorModel):
    imagePipelineArn: str


class DeleteImageRecipeRequest(BaseValidatorModel):
    imageRecipeArn: str


class DeleteImageRequest(BaseValidatorModel):
    imageBuildVersionArn: str


class DeleteInfrastructureConfigurationRequest(BaseValidatorModel):
    infrastructureConfigurationArn: str


class DeleteLifecyclePolicyRequest(BaseValidatorModel):
    lifecyclePolicyArn: str


class DeleteWorkflowRequest(BaseValidatorModel):
    workflowBuildVersionArn: str


class DistributionConfigurationSummary(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    dateCreated: Optional[str] = None
    dateUpdated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    regions: Optional[List[str]] = None


class LaunchTemplateConfiguration(BaseValidatorModel):
    launchTemplateId: str
    accountId: Optional[str] = None
    setDefaultVersion: Optional[bool] = None


class S3ExportConfiguration(BaseValidatorModel):
    roleName: str
    diskImageFormat: DiskImageFormatType
    s3Bucket: str
    s3Prefix: Optional[str] = None


class EbsInstanceBlockDeviceSpecification(BaseValidatorModel):
    encrypted: Optional[bool] = None
    deleteOnTermination: Optional[bool] = None
    iops: Optional[int] = None
    kmsKeyId: Optional[str] = None
    snapshotId: Optional[str] = None
    volumeSize: Optional[int] = None
    volumeType: Optional[EbsVolumeTypeType] = None
    throughput: Optional[int] = None


class EcrConfigurationOutput(BaseValidatorModel):
    repositoryName: Optional[str] = None
    containerTags: Optional[List[str]] = None


class EcrConfiguration(BaseValidatorModel):
    repositoryName: Optional[str] = None
    containerTags: Optional[List[str]] = None


class FastLaunchLaunchTemplateSpecification(BaseValidatorModel):
    launchTemplateId: Optional[str] = None
    launchTemplateName: Optional[str] = None
    launchTemplateVersion: Optional[str] = None


class FastLaunchSnapshotConfiguration(BaseValidatorModel):
    targetResourceCount: Optional[int] = None


class Filter(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[List[str]] = None


class GetComponentPolicyRequest(BaseValidatorModel):
    componentArn: str


class GetComponentRequest(BaseValidatorModel):
    componentBuildVersionArn: str


class GetContainerRecipePolicyRequest(BaseValidatorModel):
    containerRecipeArn: str


class GetContainerRecipeRequest(BaseValidatorModel):
    containerRecipeArn: str


class GetDistributionConfigurationRequest(BaseValidatorModel):
    distributionConfigurationArn: str


class GetImagePipelineRequest(BaseValidatorModel):
    imagePipelineArn: str


class GetImagePolicyRequest(BaseValidatorModel):
    imageArn: str


class GetImageRecipePolicyRequest(BaseValidatorModel):
    imageRecipeArn: str


class GetImageRecipeRequest(BaseValidatorModel):
    imageRecipeArn: str


class GetImageRequest(BaseValidatorModel):
    imageBuildVersionArn: str


class GetInfrastructureConfigurationRequest(BaseValidatorModel):
    infrastructureConfigurationArn: str


class GetLifecycleExecutionRequest(BaseValidatorModel):
    lifecycleExecutionId: str


class GetLifecyclePolicyRequest(BaseValidatorModel):
    lifecyclePolicyArn: str


class GetMarketplaceResourceRequest(BaseValidatorModel):
    resourceType: MarketplaceResourceTypeType
    resourceArn: str
    resourceLocation: Optional[str] = None


class GetWorkflowExecutionRequest(BaseValidatorModel):
    workflowExecutionId: str


class GetWorkflowRequest(BaseValidatorModel):
    workflowBuildVersionArn: str


class GetWorkflowStepExecutionRequest(BaseValidatorModel):
    stepExecutionId: str


class ImagePackage(BaseValidatorModel):
    packageName: Optional[str] = None
    packageVersion: Optional[str] = None


class ImageRecipeSummary(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    platform: Optional[PlatformType] = None
    owner: Optional[str] = None
    parentImage: Optional[str] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ImageScanFindingsFilter(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[List[str]] = None


class ImageScanState(BaseValidatorModel):
    status: Optional[ImageScanStatusType] = None
    reason: Optional[str] = None


class ImageVersion(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    type: Optional[ImageTypeType] = None
    version: Optional[str] = None
    platform: Optional[PlatformType] = None
    osVersion: Optional[str] = None
    owner: Optional[str] = None
    dateCreated: Optional[str] = None
    buildType: Optional[BuildTypeType] = None
    imageSource: Optional[ImageSourceType] = None


class ImportComponentRequest(BaseValidatorModel):
    name: str
    semanticVersion: str
    type: ComponentTypeType
    format: Literal['SHELL']
    platform: PlatformType
    clientToken: str
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    data: Optional[str] = None
    uri: Optional[str] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ImportDiskImageRequest(BaseValidatorModel):
    name: str
    semanticVersion: str
    platform: str
    osVersion: str
    infrastructureConfigurationArn: str
    uri: str
    clientToken: str
    description: Optional[str] = None
    executionRole: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ImportVmImageRequest(BaseValidatorModel):
    name: str
    semanticVersion: str
    platform: PlatformType
    vmImportTaskId: str
    clientToken: str
    description: Optional[str] = None
    osVersion: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class LaunchPermissionConfiguration(BaseValidatorModel):
    userIds: Optional[List[str]] = None
    userGroups: Optional[List[str]] = None
    organizationArns: Optional[List[str]] = None
    organizationalUnitArns: Optional[List[str]] = None


class LifecycleExecutionResourceAction(BaseValidatorModel):
    name: Optional[LifecycleExecutionResourceActionNameType] = None
    reason: Optional[str] = None


class LifecycleExecutionResourceState(BaseValidatorModel):
    status: Optional[LifecycleExecutionResourceStatusType] = None
    reason: Optional[str] = None


class LifecycleExecutionResourcesImpactedSummary(BaseValidatorModel):
    hasImpactedResources: Optional[bool] = None


class LifecycleExecutionState(BaseValidatorModel):
    status: Optional[LifecycleExecutionStatusType] = None
    reason: Optional[str] = None


class LifecyclePolicyDetailActionIncludeResources(BaseValidatorModel):
    amis: Optional[bool] = None
    snapshots: Optional[bool] = None
    containers: Optional[bool] = None


class LifecyclePolicyDetailExclusionRulesAmisLastLaunched(BaseValidatorModel):
    value: int
    unit: LifecyclePolicyTimeUnitType


class LifecyclePolicyDetailFilter(BaseValidatorModel):
    type: LifecyclePolicyDetailFilterTypeType
    value: int
    unit: Optional[LifecyclePolicyTimeUnitType] = None
    retainAtLeast: Optional[int] = None


class LifecyclePolicyResourceSelectionRecipe(BaseValidatorModel):
    name: str
    semanticVersion: str


class LifecyclePolicySummary(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[LifecyclePolicyStatusType] = None
    executionRole: Optional[str] = None
    resourceType: Optional[LifecyclePolicyResourceTypeType] = None
    dateCreated: Optional[datetime] = None
    dateUpdated: Optional[datetime] = None
    dateLastRun: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None


class ListComponentBuildVersionsRequest(BaseValidatorModel):
    componentVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImagePackagesRequest(BaseValidatorModel):
    imageBuildVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListLifecycleExecutionResourcesRequest(BaseValidatorModel):
    lifecycleExecutionId: str
    parentResourceId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListLifecycleExecutionsRequest(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListWaitingWorkflowStepsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class WorkflowStepExecution(BaseValidatorModel):
    stepExecutionId: Optional[str] = None
    imageBuildVersionArn: Optional[str] = None
    workflowExecutionId: Optional[str] = None
    workflowBuildVersionArn: Optional[str] = None
    name: Optional[str] = None
    action: Optional[str] = None
    startTime: Optional[str] = None


class ListWorkflowBuildVersionsRequest(BaseValidatorModel):
    workflowVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkflowExecutionsRequest(BaseValidatorModel):
    imageBuildVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class WorkflowExecutionMetadata(BaseValidatorModel):
    workflowBuildVersionArn: Optional[str] = None
    workflowExecutionId: Optional[str] = None
    type: Optional[WorkflowTypeType] = None
    status: Optional[WorkflowExecutionStatusType] = None
    message: Optional[str] = None
    totalStepCount: Optional[int] = None
    totalStepsSucceeded: Optional[int] = None
    totalStepsFailed: Optional[int] = None
    totalStepsSkipped: Optional[int] = None
    startTime: Optional[str] = None
    endTime: Optional[str] = None
    parallelGroup: Optional[str] = None


class ListWorkflowStepExecutionsRequest(BaseValidatorModel):
    workflowExecutionId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class WorkflowStepMetadata(BaseValidatorModel):
    stepExecutionId: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    action: Optional[str] = None
    status: Optional[WorkflowStepExecutionStatusType] = None
    rollbackStatus: Optional[WorkflowStepExecutionRollbackStatusType] = None
    message: Optional[str] = None
    inputs: Optional[str] = None
    outputs: Optional[str] = None
    startTime: Optional[str] = None
    endTime: Optional[str] = None


class WorkflowVersion(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    type: Optional[WorkflowTypeType] = None
    owner: Optional[str] = None
    dateCreated: Optional[str] = None


class S3Logs(BaseValidatorModel):
    s3BucketName: Optional[str] = None
    s3KeyPrefix: Optional[str] = None


class VulnerablePackage(BaseValidatorModel):
    name: Optional[str] = None
    version: Optional[str] = None
    sourceLayerHash: Optional[str] = None
    epoch: Optional[int] = None
    release: Optional[str] = None
    arch: Optional[str] = None
    packageManager: Optional[str] = None
    filePath: Optional[str] = None
    fixedInVersion: Optional[str] = None
    remediation: Optional[str] = None


class PutComponentPolicyRequest(BaseValidatorModel):
    componentArn: str
    policy: str


class PutContainerRecipePolicyRequest(BaseValidatorModel):
    containerRecipeArn: str
    policy: str


class PutImagePolicyRequest(BaseValidatorModel):
    imageArn: str
    policy: str


class PutImageRecipePolicyRequest(BaseValidatorModel):
    imageRecipeArn: str
    policy: str


class RemediationRecommendation(BaseValidatorModel):
    text: Optional[str] = None
    url: Optional[str] = None


class ResourceState(BaseValidatorModel):
    status: Optional[ResourceStatusType] = None


class ResourceStateUpdateIncludeResources(BaseValidatorModel):
    amis: Optional[bool] = None
    snapshots: Optional[bool] = None
    containers: Optional[bool] = None


class SendWorkflowStepActionRequest(BaseValidatorModel):
    stepExecutionId: str
    imageBuildVersionArn: str
    action: WorkflowStepActionTypeType
    clientToken: str
    reason: Optional[str] = None


class StartImagePipelineExecutionRequest(BaseValidatorModel):
    imagePipelineArn: str
    clientToken: str

Timestamp = Union[datetime, str]


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class WorkflowParameterOutput(BaseValidatorModel):
    name: str
    value: List[str]


class WorkflowParameterDetail(BaseValidatorModel):
    name: str
    type: str
    defaultValue: Optional[List[str]] = None
    description: Optional[str] = None


class WorkflowParameter(BaseValidatorModel):
    name: str
    value: List[str]


class WorkflowState(BaseValidatorModel):
    status: Optional[Literal['DEPRECATED']] = None
    reason: Optional[str] = None


class AccountAggregation(BaseValidatorModel):
    accountId: Optional[str] = None
    severityCounts: Optional[SeverityCounts] = None


class ImageAggregation(BaseValidatorModel):
    imageBuildVersionArn: Optional[str] = None
    severityCounts: Optional[SeverityCounts] = None


class ImagePipelineAggregation(BaseValidatorModel):
    imagePipelineArn: Optional[str] = None
    severityCounts: Optional[SeverityCounts] = None


class VulnerabilityIdAggregation(BaseValidatorModel):
    vulnerabilityId: Optional[str] = None
    severityCounts: Optional[SeverityCounts] = None


class AdditionalInstanceConfiguration(BaseValidatorModel):
    systemsManagerAgent: Optional[SystemsManagerAgent] = None
    userDataOverride: Optional[str] = None


class AmiDistributionConfigurationOutput(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    targetAccountIds: Optional[List[str]] = None
    amiTags: Optional[Dict[str, str]] = None
    kmsKeyId: Optional[str] = None
    launchPermission: Optional[LaunchPermissionConfigurationOutput] = None


class Ami(BaseValidatorModel):
    region: Optional[str] = None
    image: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    state: Optional[ImageState] = None
    accountId: Optional[str] = None


class CancelImageCreationResponse(BaseValidatorModel):
    requestId: str
    clientToken: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadata


class CancelLifecycleExecutionResponse(BaseValidatorModel):
    lifecycleExecutionId: str
    ResponseMetadata: ResponseMetadata


class CreateComponentResponse(BaseValidatorModel):
    requestId: str
    clientToken: str
    componentBuildVersionArn: str
    ResponseMetadata: ResponseMetadata


class CreateContainerRecipeResponse(BaseValidatorModel):
    requestId: str
    clientToken: str
    containerRecipeArn: str
    ResponseMetadata: ResponseMetadata


class CreateDistributionConfigurationResponse(BaseValidatorModel):
    requestId: str
    clientToken: str
    distributionConfigurationArn: str
    ResponseMetadata: ResponseMetadata


class CreateImagePipelineResponse(BaseValidatorModel):
    requestId: str
    clientToken: str
    imagePipelineArn: str
    ResponseMetadata: ResponseMetadata


class CreateImageRecipeResponse(BaseValidatorModel):
    requestId: str
    clientToken: str
    imageRecipeArn: str
    ResponseMetadata: ResponseMetadata


class CreateImageResponse(BaseValidatorModel):
    requestId: str
    clientToken: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadata


class CreateInfrastructureConfigurationResponse(BaseValidatorModel):
    requestId: str
    clientToken: str
    infrastructureConfigurationArn: str
    ResponseMetadata: ResponseMetadata


class CreateLifecyclePolicyResponse(BaseValidatorModel):
    clientToken: str
    lifecyclePolicyArn: str
    ResponseMetadata: ResponseMetadata


class CreateWorkflowResponse(BaseValidatorModel):
    clientToken: str
    workflowBuildVersionArn: str
    ResponseMetadata: ResponseMetadata


class DeleteComponentResponse(BaseValidatorModel):
    requestId: str
    componentBuildVersionArn: str
    ResponseMetadata: ResponseMetadata


class DeleteContainerRecipeResponse(BaseValidatorModel):
    requestId: str
    containerRecipeArn: str
    ResponseMetadata: ResponseMetadata


class DeleteDistributionConfigurationResponse(BaseValidatorModel):
    requestId: str
    distributionConfigurationArn: str
    ResponseMetadata: ResponseMetadata


class DeleteImagePipelineResponse(BaseValidatorModel):
    requestId: str
    imagePipelineArn: str
    ResponseMetadata: ResponseMetadata


class DeleteImageRecipeResponse(BaseValidatorModel):
    requestId: str
    imageRecipeArn: str
    ResponseMetadata: ResponseMetadata


class DeleteImageResponse(BaseValidatorModel):
    requestId: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadata


class DeleteInfrastructureConfigurationResponse(BaseValidatorModel):
    requestId: str
    infrastructureConfigurationArn: str
    ResponseMetadata: ResponseMetadata


class DeleteLifecyclePolicyResponse(BaseValidatorModel):
    lifecyclePolicyArn: str
    ResponseMetadata: ResponseMetadata


class DeleteWorkflowResponse(BaseValidatorModel):
    workflowBuildVersionArn: str
    ResponseMetadata: ResponseMetadata


class GetComponentPolicyResponse(BaseValidatorModel):
    requestId: str
    policy: str
    ResponseMetadata: ResponseMetadata


class GetContainerRecipePolicyResponse(BaseValidatorModel):
    requestId: str
    policy: str
    ResponseMetadata: ResponseMetadata


class GetImagePolicyResponse(BaseValidatorModel):
    requestId: str
    policy: str
    ResponseMetadata: ResponseMetadata


class GetImageRecipePolicyResponse(BaseValidatorModel):
    requestId: str
    policy: str
    ResponseMetadata: ResponseMetadata


class GetMarketplaceResourceResponse(BaseValidatorModel):
    resourceArn: str
    url: str
    data: str
    ResponseMetadata: ResponseMetadata


class GetWorkflowExecutionResponse(BaseValidatorModel):
    requestId: str
    workflowBuildVersionArn: str
    workflowExecutionId: str
    imageBuildVersionArn: str
    type: WorkflowTypeType
    status: WorkflowExecutionStatusType
    message: str
    totalStepCount: int
    totalStepsSucceeded: int
    totalStepsFailed: int
    totalStepsSkipped: int
    startTime: str
    endTime: str
    parallelGroup: str
    ResponseMetadata: ResponseMetadata


class GetWorkflowStepExecutionResponse(BaseValidatorModel):
    requestId: str
    stepExecutionId: str
    workflowBuildVersionArn: str
    workflowExecutionId: str
    imageBuildVersionArn: str
    name: str
    description: str
    action: str
    status: WorkflowStepExecutionStatusType
    rollbackStatus: WorkflowStepExecutionRollbackStatusType
    message: str
    inputs: str
    outputs: str
    startTime: str
    endTime: str
    onFailure: str
    timeoutSeconds: int
    ResponseMetadata: ResponseMetadata


class ImportComponentResponse(BaseValidatorModel):
    requestId: str
    clientToken: str
    componentBuildVersionArn: str
    ResponseMetadata: ResponseMetadata


class ImportDiskImageResponse(BaseValidatorModel):
    clientToken: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadata


class ImportVmImageResponse(BaseValidatorModel):
    requestId: str
    imageArn: str
    clientToken: str
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class PutComponentPolicyResponse(BaseValidatorModel):
    requestId: str
    componentArn: str
    ResponseMetadata: ResponseMetadata


class PutContainerRecipePolicyResponse(BaseValidatorModel):
    requestId: str
    containerRecipeArn: str
    ResponseMetadata: ResponseMetadata


class PutImagePolicyResponse(BaseValidatorModel):
    requestId: str
    imageArn: str
    ResponseMetadata: ResponseMetadata


class PutImageRecipePolicyResponse(BaseValidatorModel):
    requestId: str
    imageRecipeArn: str
    ResponseMetadata: ResponseMetadata


class SendWorkflowStepActionResponse(BaseValidatorModel):
    stepExecutionId: str
    imageBuildVersionArn: str
    clientToken: str
    ResponseMetadata: ResponseMetadata


class StartImagePipelineExecutionResponse(BaseValidatorModel):
    requestId: str
    clientToken: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadata


class StartResourceStateUpdateResponse(BaseValidatorModel):
    lifecycleExecutionId: str
    resourceArn: str
    ResponseMetadata: ResponseMetadata


class UpdateDistributionConfigurationResponse(BaseValidatorModel):
    requestId: str
    clientToken: str
    distributionConfigurationArn: str
    ResponseMetadata: ResponseMetadata


class UpdateImagePipelineResponse(BaseValidatorModel):
    requestId: str
    clientToken: str
    imagePipelineArn: str
    ResponseMetadata: ResponseMetadata


class UpdateInfrastructureConfigurationResponse(BaseValidatorModel):
    requestId: str
    clientToken: str
    infrastructureConfigurationArn: str
    ResponseMetadata: ResponseMetadata


class UpdateLifecyclePolicyResponse(BaseValidatorModel):
    lifecyclePolicyArn: str
    ResponseMetadata: ResponseMetadata


class ComponentConfigurationOutput(BaseValidatorModel):
    componentArn: str
    parameters: Optional[List[ComponentParameterOutput]] = None

ComponentParameterUnion = Union[ComponentParameter, ComponentParameterOutput]


class ComponentSummary(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    platform: Optional[PlatformType] = None
    supportedOsVersions: Optional[List[str]] = None
    state: Optional[ComponentState] = None
    type: Optional[ComponentTypeType] = None
    owner: Optional[str] = None
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    publisher: Optional[str] = None
    obfuscate: Optional[bool] = None


class Component(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    type: Optional[ComponentTypeType] = None
    platform: Optional[PlatformType] = None
    supportedOsVersions: Optional[List[str]] = None
    state: Optional[ComponentState] = None
    parameters: Optional[List[ComponentParameterDetail]] = None
    owner: Optional[str] = None
    data: Optional[str] = None
    kmsKeyId: Optional[str] = None
    encrypted: Optional[bool] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    publisher: Optional[str] = None
    obfuscate: Optional[bool] = None
    productCodes: Optional[List[ProductCodeListItem]] = None


class ComponentVersion(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[PlatformType] = None
    supportedOsVersions: Optional[List[str]] = None
    type: Optional[ComponentTypeType] = None
    owner: Optional[str] = None
    dateCreated: Optional[str] = None
    status: Optional[ComponentStatusType] = None
    productCodes: Optional[List[ProductCodeListItem]] = None


class ContainerDistributionConfigurationOutput(BaseValidatorModel):
    targetRepository: TargetContainerRepository
    description: Optional[str] = None
    containerTags: Optional[List[str]] = None


class ContainerDistributionConfiguration(BaseValidatorModel):
    targetRepository: TargetContainerRepository
    description: Optional[str] = None
    containerTags: Optional[List[str]] = None


class ListContainerRecipesResponse(BaseValidatorModel):
    requestId: str
    containerRecipeSummaryList: List[ContainerRecipeSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class InfrastructureConfigurationSummary(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    dateCreated: Optional[str] = None
    dateUpdated: Optional[str] = None
    resourceTags: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    instanceTypes: Optional[List[str]] = None
    instanceProfileName: Optional[str] = None
    placement: Optional[Placement] = None


class CvssScoreDetails(BaseValidatorModel):
    scoreSource: Optional[str] = None
    cvssSource: Optional[str] = None
    version: Optional[str] = None
    score: Optional[float] = None
    scoringVector: Optional[str] = None
    adjustments: Optional[List[CvssScoreAdjustment]] = None


class ListDistributionConfigurationsResponse(BaseValidatorModel):
    requestId: str
    distributionConfigurationSummaryList: List[DistributionConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class InstanceBlockDeviceMapping(BaseValidatorModel):
    deviceName: Optional[str] = None
    ebs: Optional[EbsInstanceBlockDeviceSpecification] = None
    virtualName: Optional[str] = None
    noDevice: Optional[str] = None


class ImageScanningConfigurationOutput(BaseValidatorModel):
    imageScanningEnabled: Optional[bool] = None
    ecrConfiguration: Optional[EcrConfigurationOutput] = None


class ImageScanningConfiguration(BaseValidatorModel):
    imageScanningEnabled: Optional[bool] = None
    ecrConfiguration: Optional[EcrConfiguration] = None


class FastLaunchConfiguration(BaseValidatorModel):
    enabled: bool
    snapshotConfiguration: Optional[FastLaunchSnapshotConfiguration] = None
    maxParallelLaunches: Optional[int] = None
    launchTemplate: Optional[FastLaunchLaunchTemplateSpecification] = None
    accountId: Optional[str] = None


class ListComponentsRequest(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[List[Filter]] = None
    byName: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListContainerRecipesRequest(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[List[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDistributionConfigurationsRequest(BaseValidatorModel):
    filters: Optional[List[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImageBuildVersionsRequest(BaseValidatorModel):
    imageVersionArn: str
    filters: Optional[List[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImagePipelineImagesRequest(BaseValidatorModel):
    imagePipelineArn: str
    filters: Optional[List[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImagePipelinesRequest(BaseValidatorModel):
    filters: Optional[List[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImageRecipesRequest(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[List[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImageScanFindingAggregationsRequest(BaseValidatorModel):
    filter: Optional[Filter] = None
    nextToken: Optional[str] = None


class ListImagesRequest(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[List[Filter]] = None
    byName: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    includeDeprecated: Optional[bool] = None


class ListInfrastructureConfigurationsRequest(BaseValidatorModel):
    filters: Optional[List[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListLifecyclePoliciesRequest(BaseValidatorModel):
    filters: Optional[List[Filter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkflowsRequest(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[List[Filter]] = None
    byName: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImagePackagesResponse(BaseValidatorModel):
    requestId: str
    imagePackageList: List[ImagePackage]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListImageRecipesResponse(BaseValidatorModel):
    requestId: str
    imageRecipeSummaryList: List[ImageRecipeSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListImageScanFindingsRequest(BaseValidatorModel):
    filters: Optional[List[ImageScanFindingsFilter]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImagesResponse(BaseValidatorModel):
    requestId: str
    imageVersionList: List[ImageVersion]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

LaunchPermissionConfigurationUnion = Union[LaunchPermissionConfiguration, LaunchPermissionConfigurationOutput]


class LifecycleExecutionSnapshotResource(BaseValidatorModel):
    snapshotId: Optional[str] = None
    state: Optional[LifecycleExecutionResourceState] = None


class LifecycleExecution(BaseValidatorModel):
    lifecycleExecutionId: Optional[str] = None
    lifecyclePolicyArn: Optional[str] = None
    resourcesImpactedSummary: Optional[LifecycleExecutionResourcesImpactedSummary] = None
    state: Optional[LifecycleExecutionState] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class LifecyclePolicyDetailAction(BaseValidatorModel):
    type: LifecyclePolicyDetailActionTypeType
    includeResources: Optional[LifecyclePolicyDetailActionIncludeResources] = None


class LifecyclePolicyDetailExclusionRulesAmisOutput(BaseValidatorModel):
    isPublic: Optional[bool] = None
    regions: Optional[List[str]] = None
    sharedAccounts: Optional[List[str]] = None
    lastLaunched: Optional[LifecyclePolicyDetailExclusionRulesAmisLastLaunched] = None
    tagMap: Optional[Dict[str, str]] = None


class LifecyclePolicyDetailExclusionRulesAmis(BaseValidatorModel):
    isPublic: Optional[bool] = None
    regions: Optional[List[str]] = None
    sharedAccounts: Optional[List[str]] = None
    lastLaunched: Optional[LifecyclePolicyDetailExclusionRulesAmisLastLaunched] = None
    tagMap: Optional[Dict[str, str]] = None


class LifecyclePolicyResourceSelectionOutput(BaseValidatorModel):
    recipes: Optional[List[LifecyclePolicyResourceSelectionRecipe]] = None
    tagMap: Optional[Dict[str, str]] = None


class LifecyclePolicyResourceSelection(BaseValidatorModel):
    recipes: Optional[List[LifecyclePolicyResourceSelectionRecipe]] = None
    tagMap: Optional[Dict[str, str]] = None


class ListLifecyclePoliciesResponse(BaseValidatorModel):
    lifecyclePolicySummaryList: List[LifecyclePolicySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListWaitingWorkflowStepsResponse(BaseValidatorModel):
    steps: List[WorkflowStepExecution]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListWorkflowExecutionsResponse(BaseValidatorModel):
    requestId: str
    workflowExecutions: List[WorkflowExecutionMetadata]
    imageBuildVersionArn: str
    message: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListWorkflowStepExecutionsResponse(BaseValidatorModel):
    requestId: str
    steps: List[WorkflowStepMetadata]
    workflowBuildVersionArn: str
    workflowExecutionId: str
    imageBuildVersionArn: str
    message: str
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListWorkflowsResponse(BaseValidatorModel):
    workflowVersionList: List[WorkflowVersion]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Logging(BaseValidatorModel):
    s3Logs: Optional[S3Logs] = None


class PackageVulnerabilityDetails(BaseValidatorModel):
    vulnerabilityId: str
    vulnerablePackages: Optional[List[VulnerablePackage]] = None
    source: Optional[str] = None
    cvss: Optional[List[CvssScore]] = None
    relatedVulnerabilities: Optional[List[str]] = None
    sourceUrl: Optional[str] = None
    vendorSeverity: Optional[str] = None
    vendorCreatedAt: Optional[datetime] = None
    vendorUpdatedAt: Optional[datetime] = None
    referenceUrls: Optional[List[str]] = None


class Remediation(BaseValidatorModel):
    recommendation: Optional[RemediationRecommendation] = None


class WorkflowConfigurationOutput(BaseValidatorModel):
    workflowArn: str
    parameters: Optional[List[WorkflowParameterOutput]] = None
    parallelGroup: Optional[str] = None
    onFailure: Optional[OnWorkflowFailureType] = None

WorkflowParameterUnion = Union[WorkflowParameter, WorkflowParameterOutput]


class WorkflowSummary(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    type: Optional[WorkflowTypeType] = None
    owner: Optional[str] = None
    state: Optional[WorkflowState] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Workflow(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    type: Optional[WorkflowTypeType] = None
    state: Optional[WorkflowState] = None
    owner: Optional[str] = None
    data: Optional[str] = None
    kmsKeyId: Optional[str] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    parameters: Optional[List[WorkflowParameterDetail]] = None


class ImageScanFindingAggregation(BaseValidatorModel):
    accountAggregation: Optional[AccountAggregation] = None
    imageAggregation: Optional[ImageAggregation] = None
    imagePipelineAggregation: Optional[ImagePipelineAggregation] = None
    vulnerabilityIdAggregation: Optional[VulnerabilityIdAggregation] = None


class OutputResources(BaseValidatorModel):
    amis: Optional[List[Ami]] = None
    containers: Optional[List[Container]] = None


class ComponentConfiguration(BaseValidatorModel):
    componentArn: str
    parameters: Optional[List[ComponentParameterUnion]] = None


class ListComponentBuildVersionsResponse(BaseValidatorModel):
    requestId: str
    componentSummaryList: List[ComponentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetComponentResponse(BaseValidatorModel):
    requestId: str
    component: Component
    ResponseMetadata: ResponseMetadata


class ListComponentsResponse(BaseValidatorModel):
    requestId: str
    componentVersionList: List[ComponentVersion]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

ContainerDistributionConfigurationUnion = Union[ContainerDistributionConfiguration, ContainerDistributionConfigurationOutput]


class ListInfrastructureConfigurationsResponse(BaseValidatorModel):
    requestId: str
    infrastructureConfigurationSummaryList: List[InfrastructureConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class InspectorScoreDetails(BaseValidatorModel):
    adjustedCvss: Optional[CvssScoreDetails] = None


class ImageRecipe(BaseValidatorModel):
    arn: Optional[str] = None
    type: Optional[ImageTypeType] = None
    name: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[PlatformType] = None
    owner: Optional[str] = None
    version: Optional[str] = None
    components: Optional[List[ComponentConfigurationOutput]] = None
    parentImage: Optional[str] = None
    blockDeviceMappings: Optional[List[InstanceBlockDeviceMapping]] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    workingDirectory: Optional[str] = None
    additionalInstanceConfiguration: Optional[AdditionalInstanceConfiguration] = None


class InstanceConfigurationOutput(BaseValidatorModel):
    image: Optional[str] = None
    blockDeviceMappings: Optional[List[InstanceBlockDeviceMapping]] = None


class InstanceConfiguration(BaseValidatorModel):
    image: Optional[str] = None
    blockDeviceMappings: Optional[List[InstanceBlockDeviceMapping]] = None

ImageScanningConfigurationUnion = Union[ImageScanningConfiguration, ImageScanningConfigurationOutput]


class DistributionOutput(BaseValidatorModel):
    region: str
    amiDistributionConfiguration: Optional[AmiDistributionConfigurationOutput] = None
    containerDistributionConfiguration: Optional[ContainerDistributionConfigurationOutput] = None
    licenseConfigurationArns: Optional[List[str]] = None
    launchTemplateConfigurations: Optional[List[LaunchTemplateConfiguration]] = None
    s3ExportConfiguration: Optional[S3ExportConfiguration] = None
    fastLaunchConfigurations: Optional[List[FastLaunchConfiguration]] = None


class AmiDistributionConfiguration(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    targetAccountIds: Optional[List[str]] = None
    amiTags: Optional[Dict[str, str]] = None
    kmsKeyId: Optional[str] = None
    launchPermission: Optional[LaunchPermissionConfigurationUnion] = None


class LifecycleExecutionResource(BaseValidatorModel):
    accountId: Optional[str] = None
    resourceId: Optional[str] = None
    state: Optional[LifecycleExecutionResourceState] = None
    action: Optional[LifecycleExecutionResourceAction] = None
    region: Optional[str] = None
    snapshots: Optional[List[LifecycleExecutionSnapshotResource]] = None
    imageUris: Optional[List[str]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class GetLifecycleExecutionResponse(BaseValidatorModel):
    lifecycleExecution: LifecycleExecution
    ResponseMetadata: ResponseMetadata


class ListLifecycleExecutionsResponse(BaseValidatorModel):
    lifecycleExecutions: List[LifecycleExecution]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class LifecyclePolicyDetailExclusionRulesOutput(BaseValidatorModel):
    tagMap: Optional[Dict[str, str]] = None
    amis: Optional[LifecyclePolicyDetailExclusionRulesAmisOutput] = None

LifecyclePolicyDetailExclusionRulesAmisUnion = Union[LifecyclePolicyDetailExclusionRulesAmis, LifecyclePolicyDetailExclusionRulesAmisOutput]

LifecyclePolicyResourceSelectionUnion = Union[LifecyclePolicyResourceSelection, LifecyclePolicyResourceSelectionOutput]


class CreateInfrastructureConfigurationRequest(BaseValidatorModel):
    name: str
    instanceProfileName: str
    clientToken: str
    description: Optional[str] = None
    instanceTypes: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    subnetId: Optional[str] = None
    logging: Optional[Logging] = None
    keyPair: Optional[str] = None
    terminateInstanceOnFailure: Optional[bool] = None
    snsTopicArn: Optional[str] = None
    resourceTags: Optional[Dict[str, str]] = None
    instanceMetadataOptions: Optional[InstanceMetadataOptions] = None
    tags: Optional[Dict[str, str]] = None
    placement: Optional[Placement] = None


class InfrastructureConfiguration(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    instanceTypes: Optional[List[str]] = None
    instanceProfileName: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    subnetId: Optional[str] = None
    logging: Optional[Logging] = None
    keyPair: Optional[str] = None
    terminateInstanceOnFailure: Optional[bool] = None
    snsTopicArn: Optional[str] = None
    dateCreated: Optional[str] = None
    dateUpdated: Optional[str] = None
    resourceTags: Optional[Dict[str, str]] = None
    instanceMetadataOptions: Optional[InstanceMetadataOptions] = None
    tags: Optional[Dict[str, str]] = None
    placement: Optional[Placement] = None


class UpdateInfrastructureConfigurationRequest(BaseValidatorModel):
    infrastructureConfigurationArn: str
    instanceProfileName: str
    clientToken: str
    description: Optional[str] = None
    instanceTypes: Optional[List[str]] = None
    securityGroupIds: Optional[List[str]] = None
    subnetId: Optional[str] = None
    logging: Optional[Logging] = None
    keyPair: Optional[str] = None
    terminateInstanceOnFailure: Optional[bool] = None
    snsTopicArn: Optional[str] = None
    resourceTags: Optional[Dict[str, str]] = None
    instanceMetadataOptions: Optional[InstanceMetadataOptions] = None
    placement: Optional[Placement] = None


class ImagePipeline(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[PlatformType] = None
    enhancedImageMetadataEnabled: Optional[bool] = None
    imageRecipeArn: Optional[str] = None
    containerRecipeArn: Optional[str] = None
    infrastructureConfigurationArn: Optional[str] = None
    distributionConfigurationArn: Optional[str] = None
    imageTestsConfiguration: Optional[ImageTestsConfiguration] = None
    schedule: Optional[Schedule] = None
    status: Optional[PipelineStatusType] = None
    dateCreated: Optional[str] = None
    dateUpdated: Optional[str] = None
    dateLastRun: Optional[str] = None
    dateNextRun: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationOutput] = None
    executionRole: Optional[str] = None
    workflows: Optional[List[WorkflowConfigurationOutput]] = None


class WorkflowConfiguration(BaseValidatorModel):
    workflowArn: str
    parameters: Optional[List[WorkflowParameterUnion]] = None
    parallelGroup: Optional[str] = None
    onFailure: Optional[OnWorkflowFailureType] = None


class ListWorkflowBuildVersionsResponse(BaseValidatorModel):
    workflowSummaryList: List[WorkflowSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetWorkflowResponse(BaseValidatorModel):
    workflow: Workflow
    ResponseMetadata: ResponseMetadata


class ListImageScanFindingAggregationsResponse(BaseValidatorModel):
    requestId: str
    aggregationType: str
    responses: List[ImageScanFindingAggregation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ImageSummary(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    type: Optional[ImageTypeType] = None
    version: Optional[str] = None
    platform: Optional[PlatformType] = None
    osVersion: Optional[str] = None
    state: Optional[ImageState] = None
    owner: Optional[str] = None
    dateCreated: Optional[str] = None
    outputResources: Optional[OutputResources] = None
    tags: Optional[Dict[str, str]] = None
    buildType: Optional[BuildTypeType] = None
    imageSource: Optional[ImageSourceType] = None
    deprecationTime: Optional[datetime] = None
    lifecycleExecutionId: Optional[str] = None

ComponentConfigurationUnion = Union[ComponentConfiguration, ComponentConfigurationOutput]


class ImageScanFinding(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    imageBuildVersionArn: Optional[str] = None
    imagePipelineArn: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    title: Optional[str] = None
    remediation: Optional[Remediation] = None
    severity: Optional[str] = None
    firstObservedAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    inspectorScore: Optional[float] = None
    inspectorScoreDetails: Optional[InspectorScoreDetails] = None
    packageVulnerabilityDetails: Optional[PackageVulnerabilityDetails] = None
    fixAvailable: Optional[str] = None


class GetImageRecipeResponse(BaseValidatorModel):
    requestId: str
    imageRecipe: ImageRecipe
    ResponseMetadata: ResponseMetadata


class ContainerRecipe(BaseValidatorModel):
    arn: Optional[str] = None
    containerType: Optional[Literal['DOCKER']] = None
    name: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[PlatformType] = None
    owner: Optional[str] = None
    version: Optional[str] = None
    components: Optional[List[ComponentConfigurationOutput]] = None
    instanceConfiguration: Optional[InstanceConfigurationOutput] = None
    dockerfileTemplateData: Optional[str] = None
    kmsKeyId: Optional[str] = None
    encrypted: Optional[bool] = None
    parentImage: Optional[str] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    workingDirectory: Optional[str] = None
    targetRepository: Optional[TargetContainerRepository] = None

InstanceConfigurationUnion = Union[InstanceConfiguration, InstanceConfigurationOutput]


class DistributionConfiguration(BaseValidatorModel):
    timeoutMinutes: int
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    distributions: Optional[List[DistributionOutput]] = None
    dateCreated: Optional[str] = None
    dateUpdated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

AmiDistributionConfigurationUnion = Union[AmiDistributionConfiguration, AmiDistributionConfigurationOutput]


class ListLifecycleExecutionResourcesResponse(BaseValidatorModel):
    lifecycleExecutionId: str
    lifecycleExecutionState: LifecycleExecutionState
    resources: List[LifecycleExecutionResource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class LifecyclePolicyDetailOutput(BaseValidatorModel):
    action: LifecyclePolicyDetailAction
    filter: LifecyclePolicyDetailFilter
    exclusionRules: Optional[LifecyclePolicyDetailExclusionRulesOutput] = None


class LifecyclePolicyDetailExclusionRules(BaseValidatorModel):
    tagMap: Optional[Dict[str, str]] = None
    amis: Optional[LifecyclePolicyDetailExclusionRulesAmisUnion] = None


class ResourceStateUpdateExclusionRules(BaseValidatorModel):
    amis: Optional[LifecyclePolicyDetailExclusionRulesAmisUnion] = None


class GetInfrastructureConfigurationResponse(BaseValidatorModel):
    requestId: str
    infrastructureConfiguration: InfrastructureConfiguration
    ResponseMetadata: ResponseMetadata


class GetImagePipelineResponse(BaseValidatorModel):
    requestId: str
    imagePipeline: ImagePipeline
    ResponseMetadata: ResponseMetadata


class ListImagePipelinesResponse(BaseValidatorModel):
    requestId: str
    imagePipelineList: List[ImagePipeline]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

WorkflowConfigurationUnion = Union[WorkflowConfiguration, WorkflowConfigurationOutput]


class ListImageBuildVersionsResponse(BaseValidatorModel):
    requestId: str
    imageSummaryList: List[ImageSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListImagePipelineImagesResponse(BaseValidatorModel):
    requestId: str
    imageSummaryList: List[ImageSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateImageRecipeRequest(BaseValidatorModel):
    name: str
    semanticVersion: str
    components: List[ComponentConfigurationUnion]
    parentImage: str
    clientToken: str
    description: Optional[str] = None
    blockDeviceMappings: Optional[List[InstanceBlockDeviceMapping]] = None
    tags: Optional[Dict[str, str]] = None
    workingDirectory: Optional[str] = None
    additionalInstanceConfiguration: Optional[AdditionalInstanceConfiguration] = None


class ListImageScanFindingsResponse(BaseValidatorModel):
    requestId: str
    findings: List[ImageScanFinding]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetContainerRecipeResponse(BaseValidatorModel):
    requestId: str
    containerRecipe: ContainerRecipe
    ResponseMetadata: ResponseMetadata


class CreateContainerRecipeRequest(BaseValidatorModel):
    containerType: Literal['DOCKER']
    name: str
    semanticVersion: str
    components: List[ComponentConfigurationUnion]
    parentImage: str
    targetRepository: TargetContainerRepository
    clientToken: str
    description: Optional[str] = None
    instanceConfiguration: Optional[InstanceConfigurationUnion] = None
    dockerfileTemplateData: Optional[str] = None
    dockerfileTemplateUri: Optional[str] = None
    platformOverride: Optional[PlatformType] = None
    imageOsVersionOverride: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    workingDirectory: Optional[str] = None
    kmsKeyId: Optional[str] = None


class GetDistributionConfigurationResponse(BaseValidatorModel):
    requestId: str
    distributionConfiguration: DistributionConfiguration
    ResponseMetadata: ResponseMetadata


class Image(BaseValidatorModel):
    arn: Optional[str] = None
    type: Optional[ImageTypeType] = None
    name: Optional[str] = None
    version: Optional[str] = None
    platform: Optional[PlatformType] = None
    enhancedImageMetadataEnabled: Optional[bool] = None
    osVersion: Optional[str] = None
    state: Optional[ImageState] = None
    imageRecipe: Optional[ImageRecipe] = None
    containerRecipe: Optional[ContainerRecipe] = None
    sourcePipelineName: Optional[str] = None
    sourcePipelineArn: Optional[str] = None
    infrastructureConfiguration: Optional[InfrastructureConfiguration] = None
    distributionConfiguration: Optional[DistributionConfiguration] = None
    imageTestsConfiguration: Optional[ImageTestsConfiguration] = None
    dateCreated: Optional[str] = None
    outputResources: Optional[OutputResources] = None
    tags: Optional[Dict[str, str]] = None
    buildType: Optional[BuildTypeType] = None
    imageSource: Optional[ImageSourceType] = None
    scanState: Optional[ImageScanState] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationOutput] = None
    deprecationTime: Optional[datetime] = None
    lifecycleExecutionId: Optional[str] = None
    executionRole: Optional[str] = None
    workflows: Optional[List[WorkflowConfigurationOutput]] = None


class Distribution(BaseValidatorModel):
    region: str
    amiDistributionConfiguration: Optional[AmiDistributionConfigurationUnion] = None
    containerDistributionConfiguration: Optional[ContainerDistributionConfigurationUnion] = None
    licenseConfigurationArns: Optional[List[str]] = None
    launchTemplateConfigurations: Optional[List[LaunchTemplateConfiguration]] = None
    s3ExportConfiguration: Optional[S3ExportConfiguration] = None
    fastLaunchConfigurations: Optional[List[FastLaunchConfiguration]] = None


class LifecyclePolicy(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[LifecyclePolicyStatusType] = None
    executionRole: Optional[str] = None
    resourceType: Optional[LifecyclePolicyResourceTypeType] = None
    policyDetails: Optional[List[LifecyclePolicyDetailOutput]] = None
    resourceSelection: Optional[LifecyclePolicyResourceSelectionOutput] = None
    dateCreated: Optional[datetime] = None
    dateUpdated: Optional[datetime] = None
    dateLastRun: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None

LifecyclePolicyDetailExclusionRulesUnion = Union[LifecyclePolicyDetailExclusionRules, LifecyclePolicyDetailExclusionRulesOutput]


class StartResourceStateUpdateRequest(BaseValidatorModel):
    resourceArn: str
    state: ResourceState
    clientToken: str
    executionRole: Optional[str] = None
    includeResources: Optional[ResourceStateUpdateIncludeResources] = None
    exclusionRules: Optional[ResourceStateUpdateExclusionRules] = None
    updateAt: Optional[Timestamp] = None


class CreateImagePipelineRequest(BaseValidatorModel):
    name: str
    infrastructureConfigurationArn: str
    clientToken: str
    description: Optional[str] = None
    imageRecipeArn: Optional[str] = None
    containerRecipeArn: Optional[str] = None
    distributionConfigurationArn: Optional[str] = None
    imageTestsConfiguration: Optional[ImageTestsConfiguration] = None
    enhancedImageMetadataEnabled: Optional[bool] = None
    schedule: Optional[Schedule] = None
    status: Optional[PipelineStatusType] = None
    tags: Optional[Dict[str, str]] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationUnion] = None
    workflows: Optional[List[WorkflowConfigurationUnion]] = None
    executionRole: Optional[str] = None


class CreateImageRequest(BaseValidatorModel):
    infrastructureConfigurationArn: str
    clientToken: str
    imageRecipeArn: Optional[str] = None
    containerRecipeArn: Optional[str] = None
    distributionConfigurationArn: Optional[str] = None
    imageTestsConfiguration: Optional[ImageTestsConfiguration] = None
    enhancedImageMetadataEnabled: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationUnion] = None
    workflows: Optional[List[WorkflowConfigurationUnion]] = None
    executionRole: Optional[str] = None


class UpdateImagePipelineRequest(BaseValidatorModel):
    imagePipelineArn: str
    infrastructureConfigurationArn: str
    clientToken: str
    description: Optional[str] = None
    imageRecipeArn: Optional[str] = None
    containerRecipeArn: Optional[str] = None
    distributionConfigurationArn: Optional[str] = None
    imageTestsConfiguration: Optional[ImageTestsConfiguration] = None
    enhancedImageMetadataEnabled: Optional[bool] = None
    schedule: Optional[Schedule] = None
    status: Optional[PipelineStatusType] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationUnion] = None
    workflows: Optional[List[WorkflowConfigurationUnion]] = None
    executionRole: Optional[str] = None


class GetImageResponse(BaseValidatorModel):
    requestId: str
    image: Image
    ResponseMetadata: ResponseMetadata

DistributionUnion = Union[Distribution, DistributionOutput]


class GetLifecyclePolicyResponse(BaseValidatorModel):
    lifecyclePolicy: LifecyclePolicy
    ResponseMetadata: ResponseMetadata


class LifecyclePolicyDetail(BaseValidatorModel):
    action: LifecyclePolicyDetailAction
    filter: LifecyclePolicyDetailFilter
    exclusionRules: Optional[LifecyclePolicyDetailExclusionRulesUnion] = None


class CreateDistributionConfigurationRequest(BaseValidatorModel):
    name: str
    distributions: List[DistributionUnion]
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class UpdateDistributionConfigurationRequest(BaseValidatorModel):
    distributionConfigurationArn: str
    distributions: List[DistributionUnion]
    clientToken: str
    description: Optional[str] = None

LifecyclePolicyDetailUnion = Union[LifecyclePolicyDetail, LifecyclePolicyDetailOutput]


class CreateLifecyclePolicyRequest(BaseValidatorModel):
    name: str
    executionRole: str
    resourceType: LifecyclePolicyResourceTypeType
    policyDetails: List[LifecyclePolicyDetailUnion]
    resourceSelection: LifecyclePolicyResourceSelectionUnion
    clientToken: str
    description: Optional[str] = None
    status: Optional[LifecyclePolicyStatusType] = None
    tags: Optional[Dict[str, str]] = None


class UpdateLifecyclePolicyRequest(BaseValidatorModel):
    lifecyclePolicyArn: str
    executionRole: str
    resourceType: LifecyclePolicyResourceTypeType
    policyDetails: List[LifecyclePolicyDetailUnion]
    resourceSelection: LifecyclePolicyResourceSelectionUnion
    clientToken: str
    description: Optional[str] = None
    status: Optional[LifecyclePolicyStatusType] = None