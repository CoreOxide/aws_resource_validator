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
from aws_resource_validator.pydantic_models.imagebuilder_constants import *

class SeverityCountsTypeDef(BaseValidatorModel):
    all: Optional[int] = None
    critical: Optional[int] = None
    high: Optional[int] = None
    medium: Optional[int] = None

class SystemsManagerAgentTypeDef(BaseValidatorModel):
    uninstallAfterBuild: Optional[bool] = None

class LaunchPermissionConfigurationOutputTypeDef(BaseValidatorModel):
    userIds: Optional[List[str]] = None
    userGroups: Optional[List[str]] = None
    organizationArns: Optional[List[str]] = None
    organizationalUnitArns: Optional[List[str]] = None

class LaunchPermissionConfigurationTypeDef(BaseValidatorModel):
    userIds: Optional[Sequence[str]] = None
    userGroups: Optional[Sequence[str]] = None
    organizationArns: Optional[Sequence[str]] = None
    organizationalUnitArns: Optional[Sequence[str]] = None

class ImageStateTypeDef(BaseValidatorModel):
    status: Optional[ImageStatusType] = None
    reason: Optional[str] = None

class CancelImageCreationRequestRequestTypeDef(BaseValidatorModel):
    imageBuildVersionArn: str
    clientToken: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CancelLifecycleExecutionRequestRequestTypeDef(BaseValidatorModel):
    lifecycleExecutionId: str
    clientToken: str

class ComponentParameterOutputTypeDef(BaseValidatorModel):
    name: str
    value: List[str]

class ComponentParameterTypeDef(BaseValidatorModel):
    name: str
    value: Sequence[str]

class ComponentParameterDetailTypeDef(BaseValidatorModel):
    name: str
    type: str
    defaultValue: Optional[List[str]] = None
    description: Optional[str] = None

class ComponentStateTypeDef(BaseValidatorModel):
    status: Optional[Literal["DEPRECATED"]] = None
    reason: Optional[str] = None

class ComponentVersionTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[PlatformType] = None
    supportedOsVersions: Optional[List[str]] = None
    type: Optional[ComponentTypeType] = None
    owner: Optional[str] = None
    dateCreated: Optional[str] = None

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

class CreateComponentRequestRequestTypeDef(BaseValidatorModel):
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

class CreateWorkflowRequestRequestTypeDef(BaseValidatorModel):
    name: str
    semanticVersion: str
    clientToken: str
    type: WorkflowTypeType
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    data: Optional[str] = None
    uri: Optional[str] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class CvssScoreAdjustmentTypeDef(BaseValidatorModel):
    metric: Optional[str] = None
    reason: Optional[str] = None

class CvssScoreTypeDef(BaseValidatorModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None
    version: Optional[str] = None
    source: Optional[str] = None

class DeleteComponentRequestRequestTypeDef(BaseValidatorModel):
    componentBuildVersionArn: str

class DeleteContainerRecipeRequestRequestTypeDef(BaseValidatorModel):
    containerRecipeArn: str

class DeleteDistributionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    distributionConfigurationArn: str

class DeleteImagePipelineRequestRequestTypeDef(BaseValidatorModel):
    imagePipelineArn: str

class DeleteImageRecipeRequestRequestTypeDef(BaseValidatorModel):
    imageRecipeArn: str

class DeleteImageRequestRequestTypeDef(BaseValidatorModel):
    imageBuildVersionArn: str

class DeleteInfrastructureConfigurationRequestRequestTypeDef(BaseValidatorModel):
    infrastructureConfigurationArn: str

class DeleteLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    lifecyclePolicyArn: str

class DeleteWorkflowRequestRequestTypeDef(BaseValidatorModel):
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

class GetComponentPolicyRequestRequestTypeDef(BaseValidatorModel):
    componentArn: str

class GetComponentRequestRequestTypeDef(BaseValidatorModel):
    componentBuildVersionArn: str

class GetContainerRecipePolicyRequestRequestTypeDef(BaseValidatorModel):
    containerRecipeArn: str

class GetContainerRecipeRequestRequestTypeDef(BaseValidatorModel):
    containerRecipeArn: str

class GetDistributionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    distributionConfigurationArn: str

class GetImagePipelineRequestRequestTypeDef(BaseValidatorModel):
    imagePipelineArn: str

class GetImagePolicyRequestRequestTypeDef(BaseValidatorModel):
    imageArn: str

class GetImageRecipePolicyRequestRequestTypeDef(BaseValidatorModel):
    imageRecipeArn: str

class GetImageRecipeRequestRequestTypeDef(BaseValidatorModel):
    imageRecipeArn: str

class GetImageRequestRequestTypeDef(BaseValidatorModel):
    imageBuildVersionArn: str

class GetInfrastructureConfigurationRequestRequestTypeDef(BaseValidatorModel):
    infrastructureConfigurationArn: str

class GetLifecycleExecutionRequestRequestTypeDef(BaseValidatorModel):
    lifecycleExecutionId: str

class GetLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    lifecyclePolicyArn: str

class GetWorkflowExecutionRequestRequestTypeDef(BaseValidatorModel):
    workflowExecutionId: str

class GetWorkflowRequestRequestTypeDef(BaseValidatorModel):
    workflowBuildVersionArn: str

class GetWorkflowStepExecutionRequestRequestTypeDef(BaseValidatorModel):
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

class ImageVersionTypeDef(BaseValidatorModel):
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

class ImportComponentRequestRequestTypeDef(BaseValidatorModel):
    name: str
    semanticVersion: str
    type: ComponentTypeType
    format: Literal["SHELL"]
    platform: PlatformType
    clientToken: str
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    data: Optional[str] = None
    uri: Optional[str] = None
    kmsKeyId: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class ImportVmImageRequestRequestTypeDef(BaseValidatorModel):
    name: str
    semanticVersion: str
    platform: PlatformType
    vmImportTaskId: str
    clientToken: str
    description: Optional[str] = None
    osVersion: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

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

class LifecyclePolicyDetailFilterTypeDef(BaseValidatorModel):
    type: LifecyclePolicyDetailFilterTypeType
    value: int
    unit: Optional[LifecyclePolicyTimeUnitType] = None
    retainAtLeast: Optional[int] = None

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

class ListComponentBuildVersionsRequestRequestTypeDef(BaseValidatorModel):
    componentVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImagePackagesRequestRequestTypeDef(BaseValidatorModel):
    imageBuildVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLifecycleExecutionResourcesRequestRequestTypeDef(BaseValidatorModel):
    lifecycleExecutionId: str
    parentResourceId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLifecycleExecutionsRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListWaitingWorkflowStepsRequestRequestTypeDef(BaseValidatorModel):
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

class ListWorkflowBuildVersionsRequestRequestTypeDef(BaseValidatorModel):
    workflowVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListWorkflowExecutionsRequestRequestTypeDef(BaseValidatorModel):
    imageBuildVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class WorkflowExecutionMetadataTypeDef(BaseValidatorModel):
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

class ListWorkflowStepExecutionsRequestRequestTypeDef(BaseValidatorModel):
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

class WorkflowVersionTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    type: Optional[WorkflowTypeType] = None
    owner: Optional[str] = None
    dateCreated: Optional[str] = None

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

class PutComponentPolicyRequestRequestTypeDef(BaseValidatorModel):
    componentArn: str
    policy: str

class PutContainerRecipePolicyRequestRequestTypeDef(BaseValidatorModel):
    containerRecipeArn: str
    policy: str

class PutImagePolicyRequestRequestTypeDef(BaseValidatorModel):
    imageArn: str
    policy: str

class PutImageRecipePolicyRequestRequestTypeDef(BaseValidatorModel):
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

class SendWorkflowStepActionRequestRequestTypeDef(BaseValidatorModel):
    stepExecutionId: str
    imageBuildVersionArn: str
    action: WorkflowStepActionTypeType
    clientToken: str
    reason: Optional[str] = None

class StartImagePipelineExecutionRequestRequestTypeDef(BaseValidatorModel):
    imagePipelineArn: str
    clientToken: str

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class WorkflowParameterOutputTypeDef(BaseValidatorModel):
    name: str
    value: List[str]

class WorkflowParameterTypeDef(BaseValidatorModel):
    name: str
    value: Sequence[str]

class WorkflowParameterDetailTypeDef(BaseValidatorModel):
    name: str
    type: str
    defaultValue: Optional[List[str]] = None
    description: Optional[str] = None

class WorkflowStateTypeDef(BaseValidatorModel):
    status: Optional[Literal["DEPRECATED"]] = None
    reason: Optional[str] = None

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

class AmiDistributionConfigurationTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    targetAccountIds: Optional[Sequence[str]] = None
    amiTags: Optional[Mapping[str, str]] = None
    kmsKeyId: Optional[str] = None
    launchPermission: Optional[LaunchPermissionConfigurationTypeDef] = None

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

class GetWorkflowExecutionResponseTypeDef(BaseValidatorModel):
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

class ComponentConfigurationTypeDef(BaseValidatorModel):
    componentArn: str
    parameters: Optional[Sequence[ComponentParameterTypeDef]] = None

class ComponentSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    platform: Optional[PlatformType] = None
    supportedOsVersions: Optional[List[str]] = None
    state: Optional[ComponentStateTypeDef] = None
    type: Optional[ComponentTypeType] = None
    owner: Optional[str] = None
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    publisher: Optional[str] = None
    obfuscate: Optional[bool] = None

class ComponentTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    type: Optional[ComponentTypeType] = None
    platform: Optional[PlatformType] = None
    supportedOsVersions: Optional[List[str]] = None
    state: Optional[ComponentStateTypeDef] = None
    parameters: Optional[List[ComponentParameterDetailTypeDef]] = None
    owner: Optional[str] = None
    data: Optional[str] = None
    kmsKeyId: Optional[str] = None
    encrypted: Optional[bool] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    publisher: Optional[str] = None
    obfuscate: Optional[bool] = None

class ListComponentsResponseTypeDef(BaseValidatorModel):
    requestId: str
    componentVersionList: List[ComponentVersionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class ListComponentsRequestRequestTypeDef(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    byName: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListContainerRecipesRequestRequestTypeDef(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDistributionConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImageBuildVersionsRequestRequestTypeDef(BaseValidatorModel):
    imageVersionArn: str
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImagePipelineImagesRequestRequestTypeDef(BaseValidatorModel):
    imagePipelineArn: str
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImagePipelinesRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImageRecipesRequestRequestTypeDef(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImageScanFindingAggregationsRequestRequestTypeDef(BaseValidatorModel):
    filter: Optional[FilterTypeDef] = None
    nextToken: Optional[str] = None

class ListImagesRequestRequestTypeDef(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    byName: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    includeDeprecated: Optional[bool] = None

class ListInfrastructureConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLifecyclePoliciesRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListWorkflowsRequestRequestTypeDef(BaseValidatorModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    byName: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImagePackagesResponseTypeDef(BaseValidatorModel):
    requestId: str
    imagePackageList: List[ImagePackageTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImageRecipesResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageRecipeSummaryList: List[ImageRecipeSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImageScanFindingsRequestRequestTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[ImageScanFindingsFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImagesResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageVersionList: List[ImageVersionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListInfrastructureConfigurationsResponseTypeDef(BaseValidatorModel):
    requestId: str
    infrastructureConfigurationSummaryList: List[InfrastructureConfigurationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class LifecyclePolicyDetailActionTypeDef(BaseValidatorModel):
    type: LifecyclePolicyDetailActionTypeType
    includeResources: Optional[LifecyclePolicyDetailActionIncludeResourcesTypeDef] = None

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWaitingWorkflowStepsResponseTypeDef(BaseValidatorModel):
    steps: List[WorkflowStepExecutionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowExecutionsResponseTypeDef(BaseValidatorModel):
    requestId: str
    workflowExecutions: List[WorkflowExecutionMetadataTypeDef]
    imageBuildVersionArn: str
    message: str
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowStepExecutionsResponseTypeDef(BaseValidatorModel):
    requestId: str
    steps: List[WorkflowStepMetadataTypeDef]
    workflowBuildVersionArn: str
    workflowExecutionId: str
    imageBuildVersionArn: str
    message: str
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowsResponseTypeDef(BaseValidatorModel):
    workflowVersionList: List[WorkflowVersionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class WorkflowConfigurationTypeDef(BaseValidatorModel):
    workflowArn: str
    parameters: Optional[Sequence[WorkflowParameterTypeDef]] = None
    parallelGroup: Optional[str] = None
    onFailure: Optional[OnWorkflowFailureType] = None

class WorkflowSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    type: Optional[WorkflowTypeType] = None
    owner: Optional[str] = None
    state: Optional[WorkflowStateTypeDef] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class WorkflowTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    changeDescription: Optional[str] = None
    type: Optional[WorkflowTypeType] = None
    state: Optional[WorkflowStateTypeDef] = None
    owner: Optional[str] = None
    data: Optional[str] = None
    kmsKeyId: Optional[str] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    parameters: Optional[List[WorkflowParameterDetailTypeDef]] = None

class ImageScanFindingAggregationTypeDef(BaseValidatorModel):
    accountAggregation: Optional[AccountAggregationTypeDef] = None
    imageAggregation: Optional[ImageAggregationTypeDef] = None
    imagePipelineAggregation: Optional[ImagePipelineAggregationTypeDef] = None
    vulnerabilityIdAggregation: Optional[VulnerabilityIdAggregationTypeDef] = None

class OutputResourcesTypeDef(BaseValidatorModel):
    amis: Optional[List[AmiTypeDef]] = None
    containers: Optional[List[ContainerTypeDef]] = None

class ListComponentBuildVersionsResponseTypeDef(BaseValidatorModel):
    requestId: str
    componentSummaryList: List[ComponentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentResponseTypeDef(BaseValidatorModel):
    requestId: str
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InspectorScoreDetailsTypeDef(BaseValidatorModel):
    adjustedCvss: Optional[CvssScoreDetailsTypeDef] = None

class ImageRecipeTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    type: Optional[ImageTypeType] = None
    name: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[PlatformType] = None
    owner: Optional[str] = None
    version: Optional[str] = None
    components: Optional[List[ComponentConfigurationOutputTypeDef]] = None
    parentImage: Optional[str] = None
    blockDeviceMappings: Optional[List[InstanceBlockDeviceMappingTypeDef]] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    workingDirectory: Optional[str] = None
    additionalInstanceConfiguration: Optional[AdditionalInstanceConfigurationTypeDef] = None

class InstanceConfigurationOutputTypeDef(BaseValidatorModel):
    image: Optional[str] = None
    blockDeviceMappings: Optional[List[InstanceBlockDeviceMappingTypeDef]] = None

class InstanceConfigurationTypeDef(BaseValidatorModel):
    image: Optional[str] = None
    blockDeviceMappings: Optional[Sequence[InstanceBlockDeviceMappingTypeDef]] = None

class DistributionOutputTypeDef(BaseValidatorModel):
    region: str
    amiDistributionConfiguration: Optional[AmiDistributionConfigurationOutputTypeDef] = None
    containerDistributionConfiguration: Optional[       ContainerDistributionConfigurationOutputTypeDef     ] = None
    licenseConfigurationArns: Optional[List[str]] = None
    launchTemplateConfigurations: Optional[List[LaunchTemplateConfigurationTypeDef]] = None
    s3ExportConfiguration: Optional[S3ExportConfigurationTypeDef] = None
    fastLaunchConfigurations: Optional[List[FastLaunchConfigurationTypeDef]] = None

class DistributionTypeDef(BaseValidatorModel):
    region: str
    amiDistributionConfiguration: Optional[AmiDistributionConfigurationTypeDef] = None
    containerDistributionConfiguration: Optional[       ContainerDistributionConfigurationTypeDef     ] = None
    licenseConfigurationArns: Optional[Sequence[str]] = None
    launchTemplateConfigurations: Optional[Sequence[LaunchTemplateConfigurationTypeDef]] = None
    s3ExportConfiguration: Optional[S3ExportConfigurationTypeDef] = None
    fastLaunchConfigurations: Optional[Sequence[FastLaunchConfigurationTypeDef]] = None

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LifecyclePolicyDetailExclusionRulesOutputTypeDef(BaseValidatorModel):
    tagMap: Optional[Dict[str, str]] = None
    amis: Optional[LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef] = None

class LifecyclePolicyDetailExclusionRulesTypeDef(BaseValidatorModel):
    tagMap: Optional[Mapping[str, str]] = None
    amis: Optional[LifecyclePolicyDetailExclusionRulesAmisTypeDef] = None

class ResourceStateUpdateExclusionRulesTypeDef(BaseValidatorModel):
    amis: Optional[LifecyclePolicyDetailExclusionRulesAmisTypeDef] = None

class CreateInfrastructureConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateInfrastructureConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class ListWorkflowBuildVersionsResponseTypeDef(BaseValidatorModel):
    workflowSummaryList: List[WorkflowSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowResponseTypeDef(BaseValidatorModel):
    workflow: WorkflowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListImageScanFindingAggregationsResponseTypeDef(BaseValidatorModel):
    requestId: str
    aggregationType: str
    responses: List[ImageScanFindingAggregationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImageSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    type: Optional[ImageTypeType] = None
    version: Optional[str] = None
    platform: Optional[PlatformType] = None
    osVersion: Optional[str] = None
    state: Optional[ImageStateTypeDef] = None
    owner: Optional[str] = None
    dateCreated: Optional[str] = None
    outputResources: Optional[OutputResourcesTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    buildType: Optional[BuildTypeType] = None
    imageSource: Optional[ImageSourceType] = None
    deprecationTime: Optional[datetime] = None
    lifecycleExecutionId: Optional[str] = None

class CreateImageRecipeRequestRequestTypeDef(BaseValidatorModel):
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
    awsAccountId: Optional[str] = None
    imageBuildVersionArn: Optional[str] = None
    imagePipelineArn: Optional[str] = None
    type: Optional[str] = None
    description: Optional[str] = None
    title: Optional[str] = None
    remediation: Optional[RemediationTypeDef] = None
    severity: Optional[str] = None
    firstObservedAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    inspectorScore: Optional[float] = None
    inspectorScoreDetails: Optional[InspectorScoreDetailsTypeDef] = None
    packageVulnerabilityDetails: Optional[PackageVulnerabilityDetailsTypeDef] = None
    fixAvailable: Optional[str] = None

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

class CreateContainerRecipeRequestRequestTypeDef(BaseValidatorModel):
    containerType: Literal["DOCKER"]
    name: str
    semanticVersion: str
    components: Sequence[ComponentConfigurationUnionTypeDef]
    parentImage: str
    targetRepository: TargetContainerRepositoryTypeDef
    clientToken: str
    description: Optional[str] = None
    instanceConfiguration: Optional[InstanceConfigurationTypeDef] = None
    dockerfileTemplateData: Optional[str] = None
    dockerfileTemplateUri: Optional[str] = None
    platformOverride: Optional[PlatformType] = None
    imageOsVersionOverride: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    workingDirectory: Optional[str] = None
    kmsKeyId: Optional[str] = None

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LifecyclePolicyDetailOutputTypeDef(BaseValidatorModel):
    action: LifecyclePolicyDetailActionTypeDef
    filter: LifecyclePolicyDetailFilterTypeDef
    exclusionRules: Optional[LifecyclePolicyDetailExclusionRulesOutputTypeDef] = None

class LifecyclePolicyDetailTypeDef(BaseValidatorModel):
    action: LifecyclePolicyDetailActionTypeDef
    filter: LifecyclePolicyDetailFilterTypeDef
    exclusionRules: Optional[LifecyclePolicyDetailExclusionRulesTypeDef] = None

class StartResourceStateUpdateRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    state: ResourceStateTypeDef
    clientToken: str
    executionRole: Optional[str] = None
    includeResources: Optional[ResourceStateUpdateIncludeResourcesTypeDef] = None
    exclusionRules: Optional[ResourceStateUpdateExclusionRulesTypeDef] = None
    updateAt: Optional[TimestampTypeDef] = None

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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImagePipelineRequestRequestTypeDef(BaseValidatorModel):
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
    imageScanningConfiguration: Optional[ImageScanningConfigurationTypeDef] = None
    workflows: Optional[Sequence[WorkflowConfigurationUnionTypeDef]] = None
    executionRole: Optional[str] = None

class CreateImageRequestRequestTypeDef(BaseValidatorModel):
    infrastructureConfigurationArn: str
    clientToken: str
    imageRecipeArn: Optional[str] = None
    containerRecipeArn: Optional[str] = None
    distributionConfigurationArn: Optional[str] = None
    imageTestsConfiguration: Optional[ImageTestsConfigurationTypeDef] = None
    enhancedImageMetadataEnabled: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationTypeDef] = None
    workflows: Optional[Sequence[WorkflowConfigurationUnionTypeDef]] = None
    executionRole: Optional[str] = None

class UpdateImagePipelineRequestRequestTypeDef(BaseValidatorModel):
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
    imageScanningConfiguration: Optional[ImageScanningConfigurationTypeDef] = None
    workflows: Optional[Sequence[WorkflowConfigurationUnionTypeDef]] = None
    executionRole: Optional[str] = None

class ListImageBuildVersionsResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageSummaryList: List[ImageSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImagePipelineImagesResponseTypeDef(BaseValidatorModel):
    requestId: str
    imageSummaryList: List[ImageSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImageScanFindingsResponseTypeDef(BaseValidatorModel):
    requestId: str
    findings: List[ImageScanFindingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetContainerRecipeResponseTypeDef(BaseValidatorModel):
    requestId: str
    containerRecipe: ContainerRecipeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDistributionConfigurationResponseTypeDef(BaseValidatorModel):
    requestId: str
    distributionConfiguration: DistributionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImageTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    type: Optional[ImageTypeType] = None
    name: Optional[str] = None
    version: Optional[str] = None
    platform: Optional[PlatformType] = None
    enhancedImageMetadataEnabled: Optional[bool] = None
    osVersion: Optional[str] = None
    state: Optional[ImageStateTypeDef] = None
    imageRecipe: Optional[ImageRecipeTypeDef] = None
    containerRecipe: Optional[ContainerRecipeTypeDef] = None
    sourcePipelineName: Optional[str] = None
    sourcePipelineArn: Optional[str] = None
    infrastructureConfiguration: Optional[InfrastructureConfigurationTypeDef] = None
    distributionConfiguration: Optional[DistributionConfigurationTypeDef] = None
    imageTestsConfiguration: Optional[ImageTestsConfigurationTypeDef] = None
    dateCreated: Optional[str] = None
    outputResources: Optional[OutputResourcesTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    buildType: Optional[BuildTypeType] = None
    imageSource: Optional[ImageSourceType] = None
    scanState: Optional[ImageScanStateTypeDef] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationOutputTypeDef] = None
    deprecationTime: Optional[datetime] = None
    lifecycleExecutionId: Optional[str] = None
    executionRole: Optional[str] = None
    workflows: Optional[List[WorkflowConfigurationOutputTypeDef]] = None

class CreateDistributionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    name: str
    distributions: Sequence[DistributionUnionTypeDef]
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateDistributionConfigurationRequestRequestTypeDef(BaseValidatorModel):
    distributionConfigurationArn: str
    distributions: Sequence[DistributionUnionTypeDef]
    clientToken: str
    description: Optional[str] = None

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

class GetImageResponseTypeDef(BaseValidatorModel):
    requestId: str
    image: ImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    lifecyclePolicy: LifecyclePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    name: str
    executionRole: str
    resourceType: LifecyclePolicyResourceTypeType
    policyDetails: Sequence[LifecyclePolicyDetailUnionTypeDef]
    resourceSelection: LifecyclePolicyResourceSelectionTypeDef
    clientToken: str
    description: Optional[str] = None
    status: Optional[LifecyclePolicyStatusType] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    lifecyclePolicyArn: str
    executionRole: str
    resourceType: LifecyclePolicyResourceTypeType
    policyDetails: Sequence[LifecyclePolicyDetailUnionTypeDef]
    resourceSelection: LifecyclePolicyResourceSelectionTypeDef
    clientToken: str
    description: Optional[str] = None
    status: Optional[LifecyclePolicyStatusType] = None

