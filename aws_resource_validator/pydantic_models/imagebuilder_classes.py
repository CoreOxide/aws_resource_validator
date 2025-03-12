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
from aws_resource_validator.pydantic_models.imagebuilder_constants import *

class SystemsManagerAgentTypeDef(BaseValidatorModel):
    uninstallAfterBuild: Optional[bool] = None


class LaunchPermissionConfigurationOutputTypeDef(BaseValidatorModel):
    userIds: Optional[List[str]] = None
    userGroups: Optional[List[str]] = None
    organizationArns: Optional[List[str]] = None
    organizationalUnitArns: Optional[List[str]] = None


class ImageStateTypeDef(BaseValidatorModel):
    status: Optional[ImageStatusType] = None
    reason: Optional[str] = None


class CancelImageCreationRequestTypeDef(BaseValidatorModel):
    imageBuildVersionArn: str
    clientToken: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CancelLifecycleExecutionRequestTypeDef(BaseValidatorModel):
    lifecycleExecutionId: str
    clientToken: str


class ComponentParameterOutputTypeDef(BaseValidatorModel):
    name: str
    value: List[str]


class ComponentParameterTypeDef(BaseValidatorModel):
    name: str
    value: Sequence[str]


class ComponentStateTypeDef(BaseValidatorModel):
    status: Optional[ComponentStatusType] = None
    reason: Optional[str] = None


class ProductCodeListItemTypeDef(BaseValidatorModel):
    productCodeId: str
    productCodeType: Literal["marketplace"]


class TargetContainerRepositoryTypeDef(BaseValidatorModel):
    service: Literal["ECR"]
    repositoryName: str


class ContainerRecipeSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    containerType: Optional[Literal["DOCKER"]] = None
    name: Optional[str] = None
    platform: Optional[PlatformType] = None
    owner: Optional[str] = None
    parentImage: Optional[str] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ContainerTypeDef(BaseValidatorModel):
    region: Optional[str] = None
    imageUris: Optional[List[str]] = None


class CreateComponentRequestTypeDef(BaseValidatorModel):
    name: str
    semanticVersion: str
    platform: PlatformType
    clientToken: str
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    supportedOsVersions: Optional[Sequence[str]] = None
    data: Optional[str] = None
    uri: Optional[str] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class ImageTestsConfigurationTypeDef(BaseValidatorModel):
    imageTestsEnabled: Optional[bool] = None
    timeoutMinutes: Optional[int] = None


class ScheduleTypeDef(BaseValidatorModel):
    scheduleExpression: Optional[str] = None
    timezone: Optional[str] = None
    pipelineExecutionStartCondition: Optional[PipelineExecutionStartConditionType] = None


class InstanceMetadataOptionsTypeDef(BaseValidatorModel):
    httpTokens: Optional[str] = None
    httpPutResponseHopLimit: Optional[int] = None


class PlacementTypeDef(BaseValidatorModel):
    availabilityZone: Optional[str] = None
    tenancy: Optional[TenancyTypeType] = None
    hostId: Optional[str] = None
    hostResourceGroupArn: Optional[str] = None


class CvssScoreAdjustmentTypeDef(BaseValidatorModel):
    metric: Optional[str] = None
    reason: Optional[str] = None


class CvssScoreTypeDef(BaseValidatorModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None
    version: Optional[str] = None
    source: Optional[str] = None


class DeleteComponentRequestTypeDef(BaseValidatorModel):
    componentBuildVersionArn: str


class DeleteContainerRecipeRequestTypeDef(BaseValidatorModel):
    containerRecipeArn: str


class DeleteDistributionConfigurationRequestTypeDef(BaseValidatorModel):
    distributionConfigurationArn: str


class DeleteImagePipelineRequestTypeDef(BaseValidatorModel):
    imagePipelineArn: str


class DeleteImageRecipeRequestTypeDef(BaseValidatorModel):
    imageRecipeArn: str


class DeleteImageRequestTypeDef(BaseValidatorModel):
    imageBuildVersionArn: str


class DeleteInfrastructureConfigurationRequestTypeDef(BaseValidatorModel):
    infrastructureConfigurationArn: str


class DeleteLifecyclePolicyRequestTypeDef(BaseValidatorModel):
    lifecyclePolicyArn: str


class DeleteWorkflowRequestTypeDef(BaseValidatorModel):
    workflowBuildVersionArn: str


class DistributionConfigurationSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    dateCreated: Optional[str] = None
    dateUpdated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    regions: Optional[List[str]] = None


class LaunchTemplateConfigurationTypeDef(BaseValidatorModel):
    launchTemplateId: str
    accountId: Optional[str] = None
    setDefaultVersion: Optional[bool] = None


class S3ExportConfigurationTypeDef(BaseValidatorModel):
    roleName: str
    diskImageFormat: DiskImageFormatType
    s3Bucket: str
    s3Prefix: Optional[str] = None


class EbsInstanceBlockDeviceSpecificationTypeDef(BaseValidatorModel):
    encrypted: Optional[bool] = None
    deleteOnTermination: Optional[bool] = None
    iops: Optional[int] = None
    kmsKeyId: Optional[str] = None
    snapshotId: Optional[str] = None
    volumeSize: Optional[int] = None
    volumeType: Optional[EbsVolumeTypeType] = None
    throughput: Optional[int] = None


class EcrConfigurationOutputTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    containerTags: Optional[List[str]] = None


class EcrConfigurationTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    containerTags: Optional[Sequence[str]] = None


class FastLaunchLaunchTemplateSpecificationTypeDef(BaseValidatorModel):
    launchTemplateId: Optional[str] = None
    launchTemplateName: Optional[str] = None
    launchTemplateVersion: Optional[str] = None


class FastLaunchSnapshotConfigurationTypeDef(BaseValidatorModel):
    targetResourceCount: Optional[int] = None


class FilterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None


class GetComponentPolicyRequestTypeDef(BaseValidatorModel):
    componentArn: str


class GetComponentRequestTypeDef(BaseValidatorModel):
    componentBuildVersionArn: str


class GetContainerRecipePolicyRequestTypeDef(BaseValidatorModel):
    containerRecipeArn: str


class GetContainerRecipeRequestTypeDef(BaseValidatorModel):
    containerRecipeArn: str


class GetDistributionConfigurationRequestTypeDef(BaseValidatorModel):
    distributionConfigurationArn: str


class GetImagePipelineRequestTypeDef(BaseValidatorModel):
    imagePipelineArn: str


class GetImagePolicyRequestTypeDef(BaseValidatorModel):
    imageArn: str


class GetImageRecipePolicyRequestTypeDef(BaseValidatorModel):
    imageRecipeArn: str


class GetImageRecipeRequestTypeDef(BaseValidatorModel):
    imageRecipeArn: str


class GetImageRequestTypeDef(BaseValidatorModel):
    imageBuildVersionArn: str


class GetInfrastructureConfigurationRequestTypeDef(BaseValidatorModel):
    infrastructureConfigurationArn: str


class GetLifecycleExecutionRequestTypeDef(BaseValidatorModel):
    lifecycleExecutionId: str


class GetLifecyclePolicyRequestTypeDef(BaseValidatorModel):
    lifecyclePolicyArn: str


class GetMarketplaceResourceRequestTypeDef(BaseValidatorModel):
    resourceType: MarketplaceResourceTypeType
    resourceArn: str
    resourceLocation: Optional[str] = None


class GetWorkflowExecutionRequestTypeDef(BaseValidatorModel):
    workflowExecutionId: str


class GetWorkflowRequestTypeDef(BaseValidatorModel):
    workflowBuildVersionArn: str


class GetWorkflowStepExecutionRequestTypeDef(BaseValidatorModel):
    stepExecutionId: str


class ImagePackageTypeDef(BaseValidatorModel):
    packageName: Optional[str] = None
    packageVersion: Optional[str] = None


class ImageRecipeSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    platform: Optional[PlatformType] = None
    owner: Optional[str] = None
    parentImage: Optional[str] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ImageScanFindingsFilterTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None


class ImageScanStateTypeDef(BaseValidatorModel):
    status: Optional[ImageScanStatusType] = None
    reason: Optional[str] = None


class ImportDiskImageRequestTypeDef(BaseValidatorModel):
    name: str
    semanticVersion: str
    platform: str
    osVersion: str
    infrastructureConfigurationArn: str
    uri: str
    clientToken: str
    description: Optional[str] = None
    executionRole: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class ImportVmImageRequestTypeDef(BaseValidatorModel):
    name: str
    semanticVersion: str
    platform: PlatformType
    vmImportTaskId: str
    clientToken: str
    description: Optional[str] = None
    osVersion: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class LaunchPermissionConfigurationTypeDef(BaseValidatorModel):
    userIds: Optional[Sequence[str]] = None
    userGroups: Optional[Sequence[str]] = None
    organizationArns: Optional[Sequence[str]] = None
    organizationalUnitArns: Optional[Sequence[str]] = None


class LifecycleExecutionResourceActionTypeDef(BaseValidatorModel):
    name: Optional[LifecycleExecutionResourceActionNameType] = None
    reason: Optional[str] = None


class LifecycleExecutionResourceStateTypeDef(BaseValidatorModel):
    status: Optional[LifecycleExecutionResourceStatusType] = None
    reason: Optional[str] = None


class LifecycleExecutionResourcesImpactedSummaryTypeDef(BaseValidatorModel):
    hasImpactedResources: Optional[bool] = None


class LifecycleExecutionStateTypeDef(BaseValidatorModel):
    status: Optional[LifecycleExecutionStatusType] = None
    reason: Optional[str] = None


class LifecyclePolicyDetailActionIncludeResourcesTypeDef(BaseValidatorModel):
    amis: Optional[bool] = None
    snapshots: Optional[bool] = None
    containers: Optional[bool] = None


class LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef(BaseValidatorModel):
    value: int
    unit: LifecyclePolicyTimeUnitType


class LifecyclePolicyResourceSelectionRecipeTypeDef(BaseValidatorModel):
    name: str
    semanticVersion: str


class LifecyclePolicySummaryTypeDef(BaseValidatorModel):
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


class ListComponentBuildVersionsRequestTypeDef(BaseValidatorModel):
    componentVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImagePackagesRequestTypeDef(BaseValidatorModel):
    imageBuildVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListLifecycleExecutionResourcesRequestTypeDef(BaseValidatorModel):
    lifecycleExecutionId: str
    parentResourceId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListLifecycleExecutionsRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListWaitingWorkflowStepsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class WorkflowStepExecutionTypeDef(BaseValidatorModel):
    stepExecutionId: Optional[str] = None
    imageBuildVersionArn: Optional[str] = None
    workflowExecutionId: Optional[str] = None
    workflowBuildVersionArn: Optional[str] = None
    name: Optional[str] = None
    action: Optional[str] = None
    startTime: Optional[str] = None


class ListWorkflowBuildVersionsRequestTypeDef(BaseValidatorModel):
    workflowVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkflowExecutionsRequestTypeDef(BaseValidatorModel):
    imageBuildVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkflowStepExecutionsRequestTypeDef(BaseValidatorModel):
    workflowExecutionId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class WorkflowStepMetadataTypeDef(BaseValidatorModel):
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


class S3LogsTypeDef(BaseValidatorModel):
    s3BucketName: Optional[str] = None
    s3KeyPrefix: Optional[str] = None


class VulnerablePackageTypeDef(BaseValidatorModel):
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


class PutComponentPolicyRequestTypeDef(BaseValidatorModel):
    componentArn: str
    policy: str


class PutContainerRecipePolicyRequestTypeDef(BaseValidatorModel):
    containerRecipeArn: str
    policy: str


class PutImagePolicyRequestTypeDef(BaseValidatorModel):
    imageArn: str
    policy: str


class PutImageRecipePolicyRequestTypeDef(BaseValidatorModel):
    imageRecipeArn: str
    policy: str


class RemediationRecommendationTypeDef(BaseValidatorModel):
    text: Optional[str] = None
    url: Optional[str] = None


class ResourceStateTypeDef(BaseValidatorModel):
    status: Optional[ResourceStatusType] = None


class ResourceStateUpdateIncludeResourcesTypeDef(BaseValidatorModel):
    amis: Optional[bool] = None
    snapshots: Optional[bool] = None
    containers: Optional[bool] = None


class SendWorkflowStepActionRequestTypeDef(BaseValidatorModel):
    stepExecutionId: str
    imageBuildVersionArn: str
    action: WorkflowStepActionTypeType
    clientToken: str
    reason: Optional[str] = None


class StartImagePipelineExecutionRequestTypeDef(BaseValidatorModel):
    imagePipelineArn: str
    clientToken: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class WorkflowParameterOutputTypeDef(BaseValidatorModel):
    name: str
    value: List[str]


class WorkflowParameterTypeDef(BaseValidatorModel):
    name: str
    value: Sequence[str]


class WorkflowStateTypeDef(BaseValidatorModel):
    status: Optional[Literal["DEPRECATED"]] = None
    reason: Optional[str] = None


class SeverityCountsTypeDef(BaseValidatorModel):
    pass


class AccountAggregationTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None


class ImageAggregationTypeDef(BaseValidatorModel):
    imageBuildVersionArn: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None


class ImagePipelineAggregationTypeDef(BaseValidatorModel):
    imagePipelineArn: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None


class VulnerabilityIdAggregationTypeDef(BaseValidatorModel):
    vulnerabilityId: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None


class AdditionalInstanceConfigurationTypeDef(BaseValidatorModel):
    systemsManagerAgent: Optional[SystemsManagerAgentTypeDef] = None
    userDataOverride: Optional[str] = None


class AmiDistributionConfigurationOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    targetAccountIds: Optional[List[str]] = None
    amiTags: Optional[Dict[str, str]] = None
    kmsKeyId: Optional[str] = None
    launchPermission: Optional[LaunchPermissionConfigurationOutputTypeDef] = None


class AmiTypeDef(BaseValidatorModel):
    region: Optional[str] = None
    image: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    state: Optional[ImageStateTypeDef] = None
    accountId: Optional[str] = None


class CancelImageCreationResponseTypeDef(BaseValidatorModel):
    requestId: str
    clientToken: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CancelLifecycleExecutionResponseTypeDef(BaseValidatorModel):
    lifecycleExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateComponentResponseTypeDef(BaseValidatorModel):
    requestId: str
    clientToken: str
    componentBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateContainerRecipeResponseTypeDef(BaseValidatorModel):
    requestId: str
    clientToken: str
    containerRecipeArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDistributionConfigurationResponseTypeDef(BaseValidatorModel):
    requestId: str
    clientToken: str
    distributionConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateImagePipelineResponseTypeDef(BaseValidatorModel):
    requestId: str
    clientToken: str
    imagePipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateImageRecipeResponseTypeDef(BaseValidatorModel):
    requestId: str
    clientToken: str
    imageRecipeArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateImageResponseTypeDef(BaseValidatorModel):
    requestId: str
    clientToken: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateInfrastructureConfigurationResponseTypeDef(BaseValidatorModel):
    requestId: str
    clientToken: str
    infrastructureConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    clientToken: str
    lifecyclePolicyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWorkflowResponseTypeDef(BaseValidatorModel):
    clientToken: str
    workflowBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteComponentResponseTypeDef(BaseValidatorModel):
    requestId: str
    componentBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteContainerRecipeResponseTypeDef(BaseValidatorModel):
    requestId: str
    containerRecipeArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteDistributionConfigurationResponseTypeDef(BaseValidatorModel):
    requestId: str
    distributionConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteImagePipelineResponseTypeDef(BaseValidatorModel):
    requestId: str
    imagePipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteImageRecipeResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageRecipeArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteImageResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteInfrastructureConfigurationResponseTypeDef(BaseValidatorModel):
    requestId: str
    infrastructureConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    lifecyclePolicyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteWorkflowResponseTypeDef(BaseValidatorModel):
    workflowBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetComponentPolicyResponseTypeDef(BaseValidatorModel):
    requestId: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetContainerRecipePolicyResponseTypeDef(BaseValidatorModel):
    requestId: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetImagePolicyResponseTypeDef(BaseValidatorModel):
    requestId: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetImageRecipePolicyResponseTypeDef(BaseValidatorModel):
    requestId: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetMarketplaceResourceResponseTypeDef(BaseValidatorModel):
    resourceArn: str
    url: str
    data: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetWorkflowStepExecutionResponseTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef


class ImportComponentResponseTypeDef(BaseValidatorModel):
    requestId: str
    clientToken: str
    componentBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ImportDiskImageResponseTypeDef(BaseValidatorModel):
    clientToken: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ImportVmImageResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageArn: str
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class PutComponentPolicyResponseTypeDef(BaseValidatorModel):
    requestId: str
    componentArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutContainerRecipePolicyResponseTypeDef(BaseValidatorModel):
    requestId: str
    containerRecipeArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutImagePolicyResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutImageRecipePolicyResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageRecipeArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class SendWorkflowStepActionResponseTypeDef(BaseValidatorModel):
    stepExecutionId: str
    imageBuildVersionArn: str
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartImagePipelineExecutionResponseTypeDef(BaseValidatorModel):
    requestId: str
    clientToken: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartResourceStateUpdateResponseTypeDef(BaseValidatorModel):
    lifecycleExecutionId: str
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateDistributionConfigurationResponseTypeDef(BaseValidatorModel):
    requestId: str
    clientToken: str
    distributionConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateImagePipelineResponseTypeDef(BaseValidatorModel):
    requestId: str
    clientToken: str
    imagePipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateInfrastructureConfigurationResponseTypeDef(BaseValidatorModel):
    requestId: str
    clientToken: str
    infrastructureConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    lifecyclePolicyArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class ComponentConfigurationOutputTypeDef(BaseValidatorModel):
    componentArn: str
    parameters: Optional[List[ComponentParameterOutputTypeDef]] = None


class ContainerDistributionConfigurationOutputTypeDef(BaseValidatorModel):
    targetRepository: TargetContainerRepositoryTypeDef
    description: Optional[str] = None
    containerTags: Optional[List[str]] = None


class ContainerDistributionConfigurationTypeDef(BaseValidatorModel):
    targetRepository: TargetContainerRepositoryTypeDef
    description: Optional[str] = None
    containerTags: Optional[Sequence[str]] = None


class ListContainerRecipesResponseTypeDef(BaseValidatorModel):
    requestId: str
    containerRecipeSummaryList: List[ContainerRecipeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class InfrastructureConfigurationSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    dateCreated: Optional[str] = None
    dateUpdated: Optional[str] = None
    resourceTags: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    instanceTypes: Optional[List[str]] = None
    instanceProfileName: Optional[str] = None
    placement: Optional[PlacementTypeDef] = None


class CvssScoreDetailsTypeDef(BaseValidatorModel):
    scoreSource: Optional[str] = None
    cvssSource: Optional[str] = None
    version: Optional[str] = None
    score: Optional[float] = None
    scoringVector: Optional[str] = None
    adjustments: Optional[List[CvssScoreAdjustmentTypeDef]] = None


class ListDistributionConfigurationsResponseTypeDef(BaseValidatorModel):
    requestId: str
    distributionConfigurationSummaryList: List[DistributionConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class InstanceBlockDeviceMappingTypeDef(BaseValidatorModel):
    deviceName: Optional[str] = None
    ebs: Optional[EbsInstanceBlockDeviceSpecificationTypeDef] = None
    virtualName: Optional[str] = None
    noDevice: Optional[str] = None


class ImageScanningConfigurationOutputTypeDef(BaseValidatorModel):
    imageScanningEnabled: Optional[bool] = None
    ecrConfiguration: Optional[EcrConfigurationOutputTypeDef] = None


class ImageScanningConfigurationTypeDef(BaseValidatorModel):
    imageScanningEnabled: Optional[bool] = None
    ecrConfiguration: Optional[EcrConfigurationTypeDef] = None


class FastLaunchConfigurationTypeDef(BaseValidatorModel):
    enabled: bool
    snapshotConfiguration: Optional[FastLaunchSnapshotConfigurationTypeDef] = None
    maxParallelLaunches: Optional[int] = None
    launchTemplate: Optional[FastLaunchLaunchTemplateSpecificationTypeDef] = None
    accountId: Optional[str] = None


class ListComponentsRequestTypeDef(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    byName: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListContainerRecipesRequestTypeDef(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListDistributionConfigurationsRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImageBuildVersionsRequestTypeDef(BaseValidatorModel):
    imageVersionArn: str
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImagePipelineImagesRequestTypeDef(BaseValidatorModel):
    imagePipelineArn: str
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImagePipelinesRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImageRecipesRequestTypeDef(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImagesRequestTypeDef(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    byName: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    includeDeprecated: Optional[bool] = None


class ListInfrastructureConfigurationsRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListLifecyclePoliciesRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListWorkflowsRequestTypeDef(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    byName: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImagePackagesResponseTypeDef(BaseValidatorModel):
    requestId: str
    imagePackageList: List[ImagePackageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListImageRecipesResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageRecipeSummaryList: List[ImageRecipeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListImageScanFindingsRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[ImageScanFindingsFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ImageVersionTypeDef(BaseValidatorModel):
    pass


class ListImagesResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageVersionList: List[ImageVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class LifecycleExecutionSnapshotResourceTypeDef(BaseValidatorModel):
    snapshotId: Optional[str] = None
    state: Optional[LifecycleExecutionResourceStateTypeDef] = None


class LifecycleExecutionTypeDef(BaseValidatorModel):
    lifecycleExecutionId: Optional[str] = None
    lifecyclePolicyArn: Optional[str] = None
    resourcesImpactedSummary: Optional[LifecycleExecutionResourcesImpactedSummaryTypeDef] = None
    state: Optional[LifecycleExecutionStateTypeDef] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef(BaseValidatorModel):
    isPublic: Optional[bool] = None
    regions: Optional[List[str]] = None
    sharedAccounts: Optional[List[str]] = None
    lastLaunched: Optional[LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef] = None
    tagMap: Optional[Dict[str, str]] = None


class LifecyclePolicyDetailExclusionRulesAmisTypeDef(BaseValidatorModel):
    isPublic: Optional[bool] = None
    regions: Optional[Sequence[str]] = None
    sharedAccounts: Optional[Sequence[str]] = None
    lastLaunched: Optional[LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef] = None
    tagMap: Optional[Mapping[str, str]] = None


class LifecyclePolicyResourceSelectionOutputTypeDef(BaseValidatorModel):
    recipes: Optional[List[LifecyclePolicyResourceSelectionRecipeTypeDef]] = None
    tagMap: Optional[Dict[str, str]] = None


class LifecyclePolicyResourceSelectionTypeDef(BaseValidatorModel):
    recipes: Optional[Sequence[LifecyclePolicyResourceSelectionRecipeTypeDef]] = None
    tagMap: Optional[Mapping[str, str]] = None


class ListLifecyclePoliciesResponseTypeDef(BaseValidatorModel):
    lifecyclePolicySummaryList: List[LifecyclePolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListWaitingWorkflowStepsResponseTypeDef(BaseValidatorModel):
    steps: List[WorkflowStepExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class WorkflowExecutionMetadataTypeDef(BaseValidatorModel):
    pass


class ListWorkflowExecutionsResponseTypeDef(BaseValidatorModel):
    requestId: str
    workflowExecutions: List[WorkflowExecutionMetadataTypeDef]
    imageBuildVersionArn: str
    message: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListWorkflowStepExecutionsResponseTypeDef(BaseValidatorModel):
    requestId: str
    steps: List[WorkflowStepMetadataTypeDef]
    workflowBuildVersionArn: str
    workflowExecutionId: str
    imageBuildVersionArn: str
    message: str
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class WorkflowVersionTypeDef(BaseValidatorModel):
    pass


class ListWorkflowsResponseTypeDef(BaseValidatorModel):
    workflowVersionList: List[WorkflowVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class LoggingTypeDef(BaseValidatorModel):
    s3Logs: Optional[S3LogsTypeDef] = None


class PackageVulnerabilityDetailsTypeDef(BaseValidatorModel):
    vulnerabilityId: str
    vulnerablePackages: Optional[List[VulnerablePackageTypeDef]] = None
    source: Optional[str] = None
    cvss: Optional[List[CvssScoreTypeDef]] = None
    relatedVulnerabilities: Optional[List[str]] = None
    sourceUrl: Optional[str] = None
    vendorSeverity: Optional[str] = None
    vendorCreatedAt: Optional[datetime] = None
    vendorUpdatedAt: Optional[datetime] = None
    referenceUrls: Optional[List[str]] = None


class RemediationTypeDef(BaseValidatorModel):
    recommendation: Optional[RemediationRecommendationTypeDef] = None


class WorkflowConfigurationOutputTypeDef(BaseValidatorModel):
    workflowArn: str
    parameters: Optional[List[WorkflowParameterOutputTypeDef]] = None
    parallelGroup: Optional[str] = None
    onFailure: Optional[OnWorkflowFailureType] = None


class ImageScanFindingAggregationTypeDef(BaseValidatorModel):
    accountAggregation: Optional[AccountAggregationTypeDef] = None
    imageAggregation: Optional[ImageAggregationTypeDef] = None
    imagePipelineAggregation: Optional[ImagePipelineAggregationTypeDef] = None
    vulnerabilityIdAggregation: Optional[VulnerabilityIdAggregationTypeDef] = None


class OutputResourcesTypeDef(BaseValidatorModel):
    amis: Optional[List[AmiTypeDef]] = None
    containers: Optional[List[ContainerTypeDef]] = None


class ComponentParameterUnionTypeDef(BaseValidatorModel):
    pass


class ComponentConfigurationTypeDef(BaseValidatorModel):
    componentArn: str
    parameters: Optional[Sequence[ComponentParameterUnionTypeDef]] = None


class ComponentSummaryTypeDef(BaseValidatorModel):
    pass


class ListComponentBuildVersionsResponseTypeDef(BaseValidatorModel):
    requestId: str
    componentSummaryList: List[ComponentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ComponentTypeDef(BaseValidatorModel):
    pass


class GetComponentResponseTypeDef(BaseValidatorModel):
    requestId: str
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ComponentVersionTypeDef(BaseValidatorModel):
    pass


class ListComponentsResponseTypeDef(BaseValidatorModel):
    requestId: str
    componentVersionList: List[ComponentVersionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListInfrastructureConfigurationsResponseTypeDef(BaseValidatorModel):
    requestId: str
    infrastructureConfigurationSummaryList: List[InfrastructureConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class InspectorScoreDetailsTypeDef(BaseValidatorModel):
    adjustedCvss: Optional[CvssScoreDetailsTypeDef] = None


class InstanceConfigurationOutputTypeDef(BaseValidatorModel):
    image: Optional[str] = None
    blockDeviceMappings: Optional[List[InstanceBlockDeviceMappingTypeDef]] = None


class InstanceConfigurationTypeDef(BaseValidatorModel):
    image: Optional[str] = None
    blockDeviceMappings: Optional[Sequence[InstanceBlockDeviceMappingTypeDef]] = None


class DistributionOutputTypeDef(BaseValidatorModel):
    region: str
    amiDistributionConfiguration: Optional[AmiDistributionConfigurationOutputTypeDef] = None
    containerDistributionConfiguration: Optional[ContainerDistributionConfigurationOutputTypeDef] = None
    licenseConfigurationArns: Optional[List[str]] = None
    launchTemplateConfigurations: Optional[List[LaunchTemplateConfigurationTypeDef]] = None
    s3ExportConfiguration: Optional[S3ExportConfigurationTypeDef] = None
    fastLaunchConfigurations: Optional[List[FastLaunchConfigurationTypeDef]] = None


class LaunchPermissionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class AmiDistributionConfigurationTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    targetAccountIds: Optional[Sequence[str]] = None
    amiTags: Optional[Mapping[str, str]] = None
    kmsKeyId: Optional[str] = None
    launchPermission: Optional[LaunchPermissionConfigurationUnionTypeDef] = None


class LifecycleExecutionResourceTypeDef(BaseValidatorModel):
    accountId: Optional[str] = None
    resourceId: Optional[str] = None
    state: Optional[LifecycleExecutionResourceStateTypeDef] = None
    action: Optional[LifecycleExecutionResourceActionTypeDef] = None
    region: Optional[str] = None
    snapshots: Optional[List[LifecycleExecutionSnapshotResourceTypeDef]] = None
    imageUris: Optional[List[str]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class GetLifecycleExecutionResponseTypeDef(BaseValidatorModel):
    lifecycleExecution: LifecycleExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListLifecycleExecutionsResponseTypeDef(BaseValidatorModel):
    lifecycleExecutions: List[LifecycleExecutionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class LifecyclePolicyDetailExclusionRulesOutputTypeDef(BaseValidatorModel):
    tagMap: Optional[Dict[str, str]] = None
    amis: Optional[LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef] = None


class CreateInfrastructureConfigurationRequestTypeDef(BaseValidatorModel):
    name: str
    instanceProfileName: str
    clientToken: str
    description: Optional[str] = None
    instanceTypes: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None
    subnetId: Optional[str] = None
    logging: Optional[LoggingTypeDef] = None
    keyPair: Optional[str] = None
    terminateInstanceOnFailure: Optional[bool] = None
    snsTopicArn: Optional[str] = None
    resourceTags: Optional[Mapping[str, str]] = None
    instanceMetadataOptions: Optional[InstanceMetadataOptionsTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    placement: Optional[PlacementTypeDef] = None


class InfrastructureConfigurationTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    instanceTypes: Optional[List[str]] = None
    instanceProfileName: Optional[str] = None
    securityGroupIds: Optional[List[str]] = None
    subnetId: Optional[str] = None
    logging: Optional[LoggingTypeDef] = None
    keyPair: Optional[str] = None
    terminateInstanceOnFailure: Optional[bool] = None
    snsTopicArn: Optional[str] = None
    dateCreated: Optional[str] = None
    dateUpdated: Optional[str] = None
    resourceTags: Optional[Dict[str, str]] = None
    instanceMetadataOptions: Optional[InstanceMetadataOptionsTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    placement: Optional[PlacementTypeDef] = None


class UpdateInfrastructureConfigurationRequestTypeDef(BaseValidatorModel):
    infrastructureConfigurationArn: str
    instanceProfileName: str
    clientToken: str
    description: Optional[str] = None
    instanceTypes: Optional[Sequence[str]] = None
    securityGroupIds: Optional[Sequence[str]] = None
    subnetId: Optional[str] = None
    logging: Optional[LoggingTypeDef] = None
    keyPair: Optional[str] = None
    terminateInstanceOnFailure: Optional[bool] = None
    snsTopicArn: Optional[str] = None
    resourceTags: Optional[Mapping[str, str]] = None
    instanceMetadataOptions: Optional[InstanceMetadataOptionsTypeDef] = None
    placement: Optional[PlacementTypeDef] = None


class ImagePipelineTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[PlatformType] = None
    enhancedImageMetadataEnabled: Optional[bool] = None
    imageRecipeArn: Optional[str] = None
    containerRecipeArn: Optional[str] = None
    infrastructureConfigurationArn: Optional[str] = None
    distributionConfigurationArn: Optional[str] = None
    imageTestsConfiguration: Optional[ImageTestsConfigurationTypeDef] = None
    schedule: Optional[ScheduleTypeDef] = None
    status: Optional[PipelineStatusType] = None
    dateCreated: Optional[str] = None
    dateUpdated: Optional[str] = None
    dateLastRun: Optional[str] = None
    dateNextRun: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationOutputTypeDef] = None
    executionRole: Optional[str] = None
    workflows: Optional[List[WorkflowConfigurationOutputTypeDef]] = None


class WorkflowParameterUnionTypeDef(BaseValidatorModel):
    pass


class WorkflowConfigurationTypeDef(BaseValidatorModel):
    workflowArn: str
    parameters: Optional[Sequence[WorkflowParameterUnionTypeDef]] = None
    parallelGroup: Optional[str] = None
    onFailure: Optional[OnWorkflowFailureType] = None


class WorkflowSummaryTypeDef(BaseValidatorModel):
    pass


class ListWorkflowBuildVersionsResponseTypeDef(BaseValidatorModel):
    workflowSummaryList: List[WorkflowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class WorkflowTypeDef(BaseValidatorModel):
    pass


class GetWorkflowResponseTypeDef(BaseValidatorModel):
    workflow: WorkflowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListImageScanFindingAggregationsResponseTypeDef(BaseValidatorModel):
    requestId: str
    aggregationType: str
    responses: List[ImageScanFindingAggregationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ImageRecipeTypeDef(BaseValidatorModel):
    pass


class GetImageRecipeResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageRecipe: ImageRecipeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ContainerRecipeTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    containerType: Optional[Literal["DOCKER"]] = None
    name: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[PlatformType] = None
    owner: Optional[str] = None
    version: Optional[str] = None
    components: Optional[List[ComponentConfigurationOutputTypeDef]] = None
    instanceConfiguration: Optional[InstanceConfigurationOutputTypeDef] = None
    dockerfileTemplateData: Optional[str] = None
    kmsKeyId: Optional[str] = None
    encrypted: Optional[bool] = None
    parentImage: Optional[str] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    workingDirectory: Optional[str] = None
    targetRepository: Optional[TargetContainerRepositoryTypeDef] = None


class DistributionConfigurationTypeDef(BaseValidatorModel):
    timeoutMinutes: int
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    distributions: Optional[List[DistributionOutputTypeDef]] = None
    dateCreated: Optional[str] = None
    dateUpdated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListLifecycleExecutionResourcesResponseTypeDef(BaseValidatorModel):
    lifecycleExecutionId: str
    lifecycleExecutionState: LifecycleExecutionStateTypeDef
    resources: List[LifecycleExecutionResourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class LifecyclePolicyDetailExclusionRulesAmisUnionTypeDef(BaseValidatorModel):
    pass


class LifecyclePolicyDetailExclusionRulesTypeDef(BaseValidatorModel):
    tagMap: Optional[Mapping[str, str]] = None
    amis: Optional[LifecyclePolicyDetailExclusionRulesAmisUnionTypeDef] = None


class ResourceStateUpdateExclusionRulesTypeDef(BaseValidatorModel):
    amis: Optional[LifecyclePolicyDetailExclusionRulesAmisUnionTypeDef] = None


class GetInfrastructureConfigurationResponseTypeDef(BaseValidatorModel):
    requestId: str
    infrastructureConfiguration: InfrastructureConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetImagePipelineResponseTypeDef(BaseValidatorModel):
    requestId: str
    imagePipeline: ImagePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListImagePipelinesResponseTypeDef(BaseValidatorModel):
    requestId: str
    imagePipelineList: List[ImagePipelineTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ImageSummaryTypeDef(BaseValidatorModel):
    pass


class ListImageBuildVersionsResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageSummaryList: List[ImageSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListImagePipelineImagesResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageSummaryList: List[ImageSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ComponentConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateImageRecipeRequestTypeDef(BaseValidatorModel):
    name: str
    semanticVersion: str
    components: Sequence[ComponentConfigurationUnionTypeDef]
    parentImage: str
    clientToken: str
    description: Optional[str] = None
    blockDeviceMappings: Optional[Sequence[InstanceBlockDeviceMappingTypeDef]] = None
    tags: Optional[Mapping[str, str]] = None
    workingDirectory: Optional[str] = None
    additionalInstanceConfiguration: Optional[AdditionalInstanceConfigurationTypeDef] = None


class ImageScanFindingTypeDef(BaseValidatorModel):
    pass


class ListImageScanFindingsResponseTypeDef(BaseValidatorModel):
    requestId: str
    findings: List[ImageScanFindingTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetContainerRecipeResponseTypeDef(BaseValidatorModel):
    requestId: str
    containerRecipe: ContainerRecipeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class InstanceConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateContainerRecipeRequestTypeDef(BaseValidatorModel):
    containerType: Literal["DOCKER"]
    name: str
    semanticVersion: str
    components: Sequence[ComponentConfigurationUnionTypeDef]
    parentImage: str
    targetRepository: TargetContainerRepositoryTypeDef
    clientToken: str
    description: Optional[str] = None
    instanceConfiguration: Optional[InstanceConfigurationUnionTypeDef] = None
    dockerfileTemplateData: Optional[str] = None
    dockerfileTemplateUri: Optional[str] = None
    platformOverride: Optional[PlatformType] = None
    imageOsVersionOverride: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    workingDirectory: Optional[str] = None
    kmsKeyId: Optional[str] = None


class GetDistributionConfigurationResponseTypeDef(BaseValidatorModel):
    requestId: str
    distributionConfiguration: DistributionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ContainerDistributionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class AmiDistributionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class DistributionTypeDef(BaseValidatorModel):
    region: str
    amiDistributionConfiguration: Optional[AmiDistributionConfigurationUnionTypeDef] = None
    containerDistributionConfiguration: Optional[ContainerDistributionConfigurationUnionTypeDef] = None
    licenseConfigurationArns: Optional[Sequence[str]] = None
    launchTemplateConfigurations: Optional[Sequence[LaunchTemplateConfigurationTypeDef]] = None
    s3ExportConfiguration: Optional[S3ExportConfigurationTypeDef] = None
    fastLaunchConfigurations: Optional[Sequence[FastLaunchConfigurationTypeDef]] = None


class LifecyclePolicyDetailOutputTypeDef(BaseValidatorModel):
    pass


class LifecyclePolicyTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[LifecyclePolicyStatusType] = None
    executionRole: Optional[str] = None
    resourceType: Optional[LifecyclePolicyResourceTypeType] = None
    policyDetails: Optional[List[LifecyclePolicyDetailOutputTypeDef]] = None
    resourceSelection: Optional[LifecyclePolicyResourceSelectionOutputTypeDef] = None
    dateCreated: Optional[datetime] = None
    dateUpdated: Optional[datetime] = None
    dateLastRun: Optional[datetime] = None
    tags: Optional[Dict[str, str]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class StartResourceStateUpdateRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    state: ResourceStateTypeDef
    clientToken: str
    executionRole: Optional[str] = None
    includeResources: Optional[ResourceStateUpdateIncludeResourcesTypeDef] = None
    exclusionRules: Optional[ResourceStateUpdateExclusionRulesTypeDef] = None
    updateAt: Optional[TimestampTypeDef] = None


class WorkflowConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ImageScanningConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateImagePipelineRequestTypeDef(BaseValidatorModel):
    name: str
    infrastructureConfigurationArn: str
    clientToken: str
    description: Optional[str] = None
    imageRecipeArn: Optional[str] = None
    containerRecipeArn: Optional[str] = None
    distributionConfigurationArn: Optional[str] = None
    imageTestsConfiguration: Optional[ImageTestsConfigurationTypeDef] = None
    enhancedImageMetadataEnabled: Optional[bool] = None
    schedule: Optional[ScheduleTypeDef] = None
    status: Optional[PipelineStatusType] = None
    tags: Optional[Mapping[str, str]] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationUnionTypeDef] = None
    workflows: Optional[Sequence[WorkflowConfigurationUnionTypeDef]] = None
    executionRole: Optional[str] = None


class CreateImageRequestTypeDef(BaseValidatorModel):
    infrastructureConfigurationArn: str
    clientToken: str
    imageRecipeArn: Optional[str] = None
    containerRecipeArn: Optional[str] = None
    distributionConfigurationArn: Optional[str] = None
    imageTestsConfiguration: Optional[ImageTestsConfigurationTypeDef] = None
    enhancedImageMetadataEnabled: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationUnionTypeDef] = None
    workflows: Optional[Sequence[WorkflowConfigurationUnionTypeDef]] = None
    executionRole: Optional[str] = None


class UpdateImagePipelineRequestTypeDef(BaseValidatorModel):
    imagePipelineArn: str
    infrastructureConfigurationArn: str
    clientToken: str
    description: Optional[str] = None
    imageRecipeArn: Optional[str] = None
    containerRecipeArn: Optional[str] = None
    distributionConfigurationArn: Optional[str] = None
    imageTestsConfiguration: Optional[ImageTestsConfigurationTypeDef] = None
    enhancedImageMetadataEnabled: Optional[bool] = None
    schedule: Optional[ScheduleTypeDef] = None
    status: Optional[PipelineStatusType] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationUnionTypeDef] = None
    workflows: Optional[Sequence[WorkflowConfigurationUnionTypeDef]] = None
    executionRole: Optional[str] = None


class ImageTypeDef(BaseValidatorModel):
    pass


class GetImageResponseTypeDef(BaseValidatorModel):
    requestId: str
    image: ImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    lifecyclePolicy: LifecyclePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DistributionUnionTypeDef(BaseValidatorModel):
    pass


class CreateDistributionConfigurationRequestTypeDef(BaseValidatorModel):
    name: str
    distributions: Sequence[DistributionUnionTypeDef]
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateDistributionConfigurationRequestTypeDef(BaseValidatorModel):
    distributionConfigurationArn: str
    distributions: Sequence[DistributionUnionTypeDef]
    clientToken: str
    description: Optional[str] = None


class LifecyclePolicyDetailUnionTypeDef(BaseValidatorModel):
    pass


class LifecyclePolicyResourceSelectionUnionTypeDef(BaseValidatorModel):
    pass


class CreateLifecyclePolicyRequestTypeDef(BaseValidatorModel):
    name: str
    executionRole: str
    resourceType: LifecyclePolicyResourceTypeType
    policyDetails: Sequence[LifecyclePolicyDetailUnionTypeDef]
    resourceSelection: LifecyclePolicyResourceSelectionUnionTypeDef
    clientToken: str
    description: Optional[str] = None
    status: Optional[LifecyclePolicyStatusType] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateLifecyclePolicyRequestTypeDef(BaseValidatorModel):
    lifecyclePolicyArn: str
    executionRole: str
    resourceType: LifecyclePolicyResourceTypeType
    policyDetails: Sequence[LifecyclePolicyDetailUnionTypeDef]
    resourceSelection: LifecyclePolicyResourceSelectionUnionTypeDef
    clientToken: str
    description: Optional[str] = None
    status: Optional[LifecyclePolicyStatusType] = None


