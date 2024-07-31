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
from aws_resource_validator.pydantic_models.imagebuilder_constants import *

class SeverityCountsTypeDef(BaseModel):
    all: Optional[int] = None
    critical: Optional[int] = None
    high: Optional[int] = None
    medium: Optional[int] = None

class SystemsManagerAgentTypeDef(BaseModel):
    uninstallAfterBuild: Optional[bool] = None

class LaunchPermissionConfigurationOutputTypeDef(BaseModel):
    userIds: Optional[List[str]] = None
    userGroups: Optional[List[str]] = None
    organizationArns: Optional[List[str]] = None
    organizationalUnitArns: Optional[List[str]] = None

class LaunchPermissionConfigurationTypeDef(BaseModel):
    userIds: Optional[Sequence[str]] = None
    userGroups: Optional[Sequence[str]] = None
    organizationArns: Optional[Sequence[str]] = None
    organizationalUnitArns: Optional[Sequence[str]] = None

class ImageStateTypeDef(BaseModel):
    status: Optional[ImageStatusType] = None
    reason: Optional[str] = None

class CancelImageCreationRequestRequestTypeDef(BaseModel):
    imageBuildVersionArn: str
    clientToken: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CancelLifecycleExecutionRequestRequestTypeDef(BaseModel):
    lifecycleExecutionId: str
    clientToken: str

class ComponentParameterOutputTypeDef(BaseModel):
    name: str
    value: List[str]

class ComponentParameterTypeDef(BaseModel):
    name: str
    value: Sequence[str]

class ComponentParameterDetailTypeDef(BaseModel):
    name: str
    type: str
    defaultValue: Optional[List[str]] = None
    description: Optional[str] = None

class ComponentStateTypeDef(BaseModel):
    status: Optional[Literal["DEPRECATED"]] = None
    reason: Optional[str] = None

class ComponentVersionTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    platform: Optional[PlatformType] = None
    supportedOsVersions: Optional[List[str]] = None
    type: Optional[ComponentTypeType] = None
    owner: Optional[str] = None
    dateCreated: Optional[str] = None

class TargetContainerRepositoryTypeDef(BaseModel):
    service: Literal["ECR"]
    repositoryName: str

class ContainerRecipeSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    containerType: Optional[Literal["DOCKER"]] = None
    name: Optional[str] = None
    platform: Optional[PlatformType] = None
    owner: Optional[str] = None
    parentImage: Optional[str] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ContainerTypeDef(BaseModel):
    region: Optional[str] = None
    imageUris: Optional[List[str]] = None

class CreateComponentRequestRequestTypeDef(BaseModel):
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

class ImageTestsConfigurationTypeDef(BaseModel):
    imageTestsEnabled: Optional[bool] = None
    timeoutMinutes: Optional[int] = None

class ScheduleTypeDef(BaseModel):
    scheduleExpression: Optional[str] = None
    timezone: Optional[str] = None
    pipelineExecutionStartCondition: Optional[PipelineExecutionStartConditionType] = None

class InstanceMetadataOptionsTypeDef(BaseModel):
    httpTokens: Optional[str] = None
    httpPutResponseHopLimit: Optional[int] = None

class CreateWorkflowRequestRequestTypeDef(BaseModel):
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

class CvssScoreAdjustmentTypeDef(BaseModel):
    metric: Optional[str] = None
    reason: Optional[str] = None

class CvssScoreTypeDef(BaseModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None
    version: Optional[str] = None
    source: Optional[str] = None

class DeleteComponentRequestRequestTypeDef(BaseModel):
    componentBuildVersionArn: str

class DeleteContainerRecipeRequestRequestTypeDef(BaseModel):
    containerRecipeArn: str

class DeleteDistributionConfigurationRequestRequestTypeDef(BaseModel):
    distributionConfigurationArn: str

class DeleteImagePipelineRequestRequestTypeDef(BaseModel):
    imagePipelineArn: str

class DeleteImageRecipeRequestRequestTypeDef(BaseModel):
    imageRecipeArn: str

class DeleteImageRequestRequestTypeDef(BaseModel):
    imageBuildVersionArn: str

class DeleteInfrastructureConfigurationRequestRequestTypeDef(BaseModel):
    infrastructureConfigurationArn: str

class DeleteLifecyclePolicyRequestRequestTypeDef(BaseModel):
    lifecyclePolicyArn: str

class DeleteWorkflowRequestRequestTypeDef(BaseModel):
    workflowBuildVersionArn: str

class DistributionConfigurationSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    dateCreated: Optional[str] = None
    dateUpdated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    regions: Optional[List[str]] = None

class LaunchTemplateConfigurationTypeDef(BaseModel):
    launchTemplateId: str
    accountId: Optional[str] = None
    setDefaultVersion: Optional[bool] = None

class S3ExportConfigurationTypeDef(BaseModel):
    roleName: str
    diskImageFormat: DiskImageFormatType
    s3Bucket: str
    s3Prefix: Optional[str] = None

class EbsInstanceBlockDeviceSpecificationTypeDef(BaseModel):
    encrypted: Optional[bool] = None
    deleteOnTermination: Optional[bool] = None
    iops: Optional[int] = None
    kmsKeyId: Optional[str] = None
    snapshotId: Optional[str] = None
    volumeSize: Optional[int] = None
    volumeType: Optional[EbsVolumeTypeType] = None
    throughput: Optional[int] = None

class EcrConfigurationOutputTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    containerTags: Optional[List[str]] = None

class EcrConfigurationTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    containerTags: Optional[Sequence[str]] = None

class FastLaunchLaunchTemplateSpecificationTypeDef(BaseModel):
    launchTemplateId: Optional[str] = None
    launchTemplateName: Optional[str] = None
    launchTemplateVersion: Optional[str] = None

class FastLaunchSnapshotConfigurationTypeDef(BaseModel):
    targetResourceCount: Optional[int] = None

class FilterTypeDef(BaseModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None

class GetComponentPolicyRequestRequestTypeDef(BaseModel):
    componentArn: str

class GetComponentRequestRequestTypeDef(BaseModel):
    componentBuildVersionArn: str

class GetContainerRecipePolicyRequestRequestTypeDef(BaseModel):
    containerRecipeArn: str

class GetContainerRecipeRequestRequestTypeDef(BaseModel):
    containerRecipeArn: str

class GetDistributionConfigurationRequestRequestTypeDef(BaseModel):
    distributionConfigurationArn: str

class GetImagePipelineRequestRequestTypeDef(BaseModel):
    imagePipelineArn: str

class GetImagePolicyRequestRequestTypeDef(BaseModel):
    imageArn: str

class GetImageRecipePolicyRequestRequestTypeDef(BaseModel):
    imageRecipeArn: str

class GetImageRecipeRequestRequestTypeDef(BaseModel):
    imageRecipeArn: str

class GetImageRequestRequestTypeDef(BaseModel):
    imageBuildVersionArn: str

class GetInfrastructureConfigurationRequestRequestTypeDef(BaseModel):
    infrastructureConfigurationArn: str

class GetLifecycleExecutionRequestRequestTypeDef(BaseModel):
    lifecycleExecutionId: str

class GetLifecyclePolicyRequestRequestTypeDef(BaseModel):
    lifecyclePolicyArn: str

class GetWorkflowExecutionRequestRequestTypeDef(BaseModel):
    workflowExecutionId: str

class GetWorkflowRequestRequestTypeDef(BaseModel):
    workflowBuildVersionArn: str

class GetWorkflowStepExecutionRequestRequestTypeDef(BaseModel):
    stepExecutionId: str

class ImagePackageTypeDef(BaseModel):
    packageName: Optional[str] = None
    packageVersion: Optional[str] = None

class ImageRecipeSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    platform: Optional[PlatformType] = None
    owner: Optional[str] = None
    parentImage: Optional[str] = None
    dateCreated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ImageScanFindingsFilterTypeDef(BaseModel):
    name: Optional[str] = None
    values: Optional[Sequence[str]] = None

class ImageScanStateTypeDef(BaseModel):
    status: Optional[ImageScanStatusType] = None
    reason: Optional[str] = None

class ImageVersionTypeDef(BaseModel):
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

class ImportComponentRequestRequestTypeDef(BaseModel):
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

class ImportVmImageRequestRequestTypeDef(BaseModel):
    name: str
    semanticVersion: str
    platform: PlatformType
    vmImportTaskId: str
    clientToken: str
    description: Optional[str] = None
    osVersion: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class InfrastructureConfigurationSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    dateCreated: Optional[str] = None
    dateUpdated: Optional[str] = None
    resourceTags: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None
    instanceTypes: Optional[List[str]] = None
    instanceProfileName: Optional[str] = None

class LifecycleExecutionResourceActionTypeDef(BaseModel):
    name: Optional[LifecycleExecutionResourceActionNameType] = None
    reason: Optional[str] = None

class LifecycleExecutionResourceStateTypeDef(BaseModel):
    status: Optional[LifecycleExecutionResourceStatusType] = None
    reason: Optional[str] = None

class LifecycleExecutionResourcesImpactedSummaryTypeDef(BaseModel):
    hasImpactedResources: Optional[bool] = None

class LifecycleExecutionStateTypeDef(BaseModel):
    status: Optional[LifecycleExecutionStatusType] = None
    reason: Optional[str] = None

class LifecyclePolicyDetailActionIncludeResourcesTypeDef(BaseModel):
    amis: Optional[bool] = None
    snapshots: Optional[bool] = None
    containers: Optional[bool] = None

class LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef(BaseModel):
    value: int
    unit: LifecyclePolicyTimeUnitType

class LifecyclePolicyDetailFilterTypeDef(BaseModel):
    type: LifecyclePolicyDetailFilterTypeType
    value: int
    unit: Optional[LifecyclePolicyTimeUnitType] = None
    retainAtLeast: Optional[int] = None

class LifecyclePolicyResourceSelectionRecipeTypeDef(BaseModel):
    name: str
    semanticVersion: str

class LifecyclePolicySummaryTypeDef(BaseModel):
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

class ListComponentBuildVersionsRequestRequestTypeDef(BaseModel):
    componentVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImagePackagesRequestRequestTypeDef(BaseModel):
    imageBuildVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLifecycleExecutionResourcesRequestRequestTypeDef(BaseModel):
    lifecycleExecutionId: str
    parentResourceId: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLifecycleExecutionsRequestRequestTypeDef(BaseModel):
    resourceArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListWaitingWorkflowStepsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class WorkflowStepExecutionTypeDef(BaseModel):
    stepExecutionId: Optional[str] = None
    imageBuildVersionArn: Optional[str] = None
    workflowExecutionId: Optional[str] = None
    workflowBuildVersionArn: Optional[str] = None
    name: Optional[str] = None
    action: Optional[str] = None
    startTime: Optional[str] = None

class ListWorkflowBuildVersionsRequestRequestTypeDef(BaseModel):
    workflowVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListWorkflowExecutionsRequestRequestTypeDef(BaseModel):
    imageBuildVersionArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class WorkflowExecutionMetadataTypeDef(BaseModel):
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

class ListWorkflowStepExecutionsRequestRequestTypeDef(BaseModel):
    workflowExecutionId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class WorkflowStepMetadataTypeDef(BaseModel):
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

class WorkflowVersionTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    version: Optional[str] = None
    description: Optional[str] = None
    type: Optional[WorkflowTypeType] = None
    owner: Optional[str] = None
    dateCreated: Optional[str] = None

class S3LogsTypeDef(BaseModel):
    s3BucketName: Optional[str] = None
    s3KeyPrefix: Optional[str] = None

class VulnerablePackageTypeDef(BaseModel):
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

class PutComponentPolicyRequestRequestTypeDef(BaseModel):
    componentArn: str
    policy: str

class PutContainerRecipePolicyRequestRequestTypeDef(BaseModel):
    containerRecipeArn: str
    policy: str

class PutImagePolicyRequestRequestTypeDef(BaseModel):
    imageArn: str
    policy: str

class PutImageRecipePolicyRequestRequestTypeDef(BaseModel):
    imageRecipeArn: str
    policy: str

class RemediationRecommendationTypeDef(BaseModel):
    text: Optional[str] = None
    url: Optional[str] = None

class ResourceStateTypeDef(BaseModel):
    status: Optional[ResourceStatusType] = None

class ResourceStateUpdateIncludeResourcesTypeDef(BaseModel):
    amis: Optional[bool] = None
    snapshots: Optional[bool] = None
    containers: Optional[bool] = None

class SendWorkflowStepActionRequestRequestTypeDef(BaseModel):
    stepExecutionId: str
    imageBuildVersionArn: str
    action: WorkflowStepActionTypeType
    clientToken: str
    reason: Optional[str] = None

class StartImagePipelineExecutionRequestRequestTypeDef(BaseModel):
    imagePipelineArn: str
    clientToken: str

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class WorkflowParameterOutputTypeDef(BaseModel):
    name: str
    value: List[str]

class WorkflowParameterTypeDef(BaseModel):
    name: str
    value: Sequence[str]

class WorkflowParameterDetailTypeDef(BaseModel):
    name: str
    type: str
    defaultValue: Optional[List[str]] = None
    description: Optional[str] = None

class WorkflowStateTypeDef(BaseModel):
    status: Optional[Literal["DEPRECATED"]] = None
    reason: Optional[str] = None

class AccountAggregationTypeDef(BaseModel):
    accountId: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None

class ImageAggregationTypeDef(BaseModel):
    imageBuildVersionArn: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None

class ImagePipelineAggregationTypeDef(BaseModel):
    imagePipelineArn: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None

class VulnerabilityIdAggregationTypeDef(BaseModel):
    vulnerabilityId: Optional[str] = None
    severityCounts: Optional[SeverityCountsTypeDef] = None

class AdditionalInstanceConfigurationTypeDef(BaseModel):
    systemsManagerAgent: Optional[SystemsManagerAgentTypeDef] = None
    userDataOverride: Optional[str] = None

class AmiDistributionConfigurationOutputTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    targetAccountIds: Optional[List[str]] = None
    amiTags: Optional[Dict[str, str]] = None
    kmsKeyId: Optional[str] = None
    launchPermission: Optional[LaunchPermissionConfigurationOutputTypeDef] = None

class AmiDistributionConfigurationTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    targetAccountIds: Optional[Sequence[str]] = None
    amiTags: Optional[Mapping[str, str]] = None
    kmsKeyId: Optional[str] = None
    launchPermission: Optional[LaunchPermissionConfigurationTypeDef] = None

class AmiTypeDef(BaseModel):
    region: Optional[str] = None
    image: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    state: Optional[ImageStateTypeDef] = None
    accountId: Optional[str] = None

class CancelImageCreationResponseTypeDef(BaseModel):
    requestId: str
    clientToken: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelLifecycleExecutionResponseTypeDef(BaseModel):
    lifecycleExecutionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateComponentResponseTypeDef(BaseModel):
    requestId: str
    clientToken: str
    componentBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContainerRecipeResponseTypeDef(BaseModel):
    requestId: str
    clientToken: str
    containerRecipeArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDistributionConfigurationResponseTypeDef(BaseModel):
    requestId: str
    clientToken: str
    distributionConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImagePipelineResponseTypeDef(BaseModel):
    requestId: str
    clientToken: str
    imagePipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageRecipeResponseTypeDef(BaseModel):
    requestId: str
    clientToken: str
    imageRecipeArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImageResponseTypeDef(BaseModel):
    requestId: str
    clientToken: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInfrastructureConfigurationResponseTypeDef(BaseModel):
    requestId: str
    clientToken: str
    infrastructureConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLifecyclePolicyResponseTypeDef(BaseModel):
    clientToken: str
    lifecyclePolicyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkflowResponseTypeDef(BaseModel):
    clientToken: str
    workflowBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteComponentResponseTypeDef(BaseModel):
    requestId: str
    componentBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteContainerRecipeResponseTypeDef(BaseModel):
    requestId: str
    containerRecipeArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDistributionConfigurationResponseTypeDef(BaseModel):
    requestId: str
    distributionConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteImagePipelineResponseTypeDef(BaseModel):
    requestId: str
    imagePipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteImageRecipeResponseTypeDef(BaseModel):
    requestId: str
    imageRecipeArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteImageResponseTypeDef(BaseModel):
    requestId: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteInfrastructureConfigurationResponseTypeDef(BaseModel):
    requestId: str
    infrastructureConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLifecyclePolicyResponseTypeDef(BaseModel):
    lifecyclePolicyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteWorkflowResponseTypeDef(BaseModel):
    workflowBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentPolicyResponseTypeDef(BaseModel):
    requestId: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetContainerRecipePolicyResponseTypeDef(BaseModel):
    requestId: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImagePolicyResponseTypeDef(BaseModel):
    requestId: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetImageRecipePolicyResponseTypeDef(BaseModel):
    requestId: str
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowExecutionResponseTypeDef(BaseModel):
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

class GetWorkflowStepExecutionResponseTypeDef(BaseModel):
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

class ImportComponentResponseTypeDef(BaseModel):
    requestId: str
    clientToken: str
    componentBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportVmImageResponseTypeDef(BaseModel):
    requestId: str
    imageArn: str
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutComponentPolicyResponseTypeDef(BaseModel):
    requestId: str
    componentArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutContainerRecipePolicyResponseTypeDef(BaseModel):
    requestId: str
    containerRecipeArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutImagePolicyResponseTypeDef(BaseModel):
    requestId: str
    imageArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutImageRecipePolicyResponseTypeDef(BaseModel):
    requestId: str
    imageRecipeArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendWorkflowStepActionResponseTypeDef(BaseModel):
    stepExecutionId: str
    imageBuildVersionArn: str
    clientToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartImagePipelineExecutionResponseTypeDef(BaseModel):
    requestId: str
    clientToken: str
    imageBuildVersionArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartResourceStateUpdateResponseTypeDef(BaseModel):
    lifecycleExecutionId: str
    resourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateDistributionConfigurationResponseTypeDef(BaseModel):
    requestId: str
    clientToken: str
    distributionConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateImagePipelineResponseTypeDef(BaseModel):
    requestId: str
    clientToken: str
    imagePipelineArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateInfrastructureConfigurationResponseTypeDef(BaseModel):
    requestId: str
    clientToken: str
    infrastructureConfigurationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateLifecyclePolicyResponseTypeDef(BaseModel):
    lifecyclePolicyArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ComponentConfigurationOutputTypeDef(BaseModel):
    componentArn: str
    parameters: Optional[List[ComponentParameterOutputTypeDef]] = None

class ComponentConfigurationTypeDef(BaseModel):
    componentArn: str
    parameters: Optional[Sequence[ComponentParameterTypeDef]] = None

class ComponentSummaryTypeDef(BaseModel):
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

class ComponentTypeDef(BaseModel):
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

class ListComponentsResponseTypeDef(BaseModel):
    requestId: str
    componentVersionList: List[ComponentVersionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ContainerDistributionConfigurationOutputTypeDef(BaseModel):
    targetRepository: TargetContainerRepositoryTypeDef
    description: Optional[str] = None
    containerTags: Optional[List[str]] = None

class ContainerDistributionConfigurationTypeDef(BaseModel):
    targetRepository: TargetContainerRepositoryTypeDef
    description: Optional[str] = None
    containerTags: Optional[Sequence[str]] = None

class ListContainerRecipesResponseTypeDef(BaseModel):
    requestId: str
    containerRecipeSummaryList: List[ContainerRecipeSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CvssScoreDetailsTypeDef(BaseModel):
    scoreSource: Optional[str] = None
    cvssSource: Optional[str] = None
    version: Optional[str] = None
    score: Optional[float] = None
    scoringVector: Optional[str] = None
    adjustments: Optional[List[CvssScoreAdjustmentTypeDef]] = None

class ListDistributionConfigurationsResponseTypeDef(BaseModel):
    requestId: str
    distributionConfigurationSummaryList: List[DistributionConfigurationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class InstanceBlockDeviceMappingTypeDef(BaseModel):
    deviceName: Optional[str] = None
    ebs: Optional[EbsInstanceBlockDeviceSpecificationTypeDef] = None
    virtualName: Optional[str] = None
    noDevice: Optional[str] = None

class ImageScanningConfigurationOutputTypeDef(BaseModel):
    imageScanningEnabled: Optional[bool] = None
    ecrConfiguration: Optional[EcrConfigurationOutputTypeDef] = None

class ImageScanningConfigurationTypeDef(BaseModel):
    imageScanningEnabled: Optional[bool] = None
    ecrConfiguration: Optional[EcrConfigurationTypeDef] = None

class FastLaunchConfigurationTypeDef(BaseModel):
    enabled: bool
    snapshotConfiguration: Optional[FastLaunchSnapshotConfigurationTypeDef] = None
    maxParallelLaunches: Optional[int] = None
    launchTemplate: Optional[FastLaunchLaunchTemplateSpecificationTypeDef] = None
    accountId: Optional[str] = None

class ListComponentsRequestRequestTypeDef(BaseModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    byName: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListContainerRecipesRequestRequestTypeDef(BaseModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListDistributionConfigurationsRequestRequestTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImageBuildVersionsRequestRequestTypeDef(BaseModel):
    imageVersionArn: str
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImagePipelineImagesRequestRequestTypeDef(BaseModel):
    imagePipelineArn: str
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImagePipelinesRequestRequestTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImageRecipesRequestRequestTypeDef(BaseModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImageScanFindingAggregationsRequestRequestTypeDef(BaseModel):
    filter: Optional[FilterTypeDef] = None
    nextToken: Optional[str] = None

class ListImagesRequestRequestTypeDef(BaseModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    byName: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    includeDeprecated: Optional[bool] = None

class ListInfrastructureConfigurationsRequestRequestTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListLifecyclePoliciesRequestRequestTypeDef(BaseModel):
    filters: Optional[Sequence[FilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListWorkflowsRequestRequestTypeDef(BaseModel):
    owner: Optional[OwnershipType] = None
    filters: Optional[Sequence[FilterTypeDef]] = None
    byName: Optional[bool] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImagePackagesResponseTypeDef(BaseModel):
    requestId: str
    imagePackageList: List[ImagePackageTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImageRecipesResponseTypeDef(BaseModel):
    requestId: str
    imageRecipeSummaryList: List[ImageRecipeSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImageScanFindingsRequestRequestTypeDef(BaseModel):
    filters: Optional[Sequence[ImageScanFindingsFilterTypeDef]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImagesResponseTypeDef(BaseModel):
    requestId: str
    imageVersionList: List[ImageVersionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListInfrastructureConfigurationsResponseTypeDef(BaseModel):
    requestId: str
    infrastructureConfigurationSummaryList: List[InfrastructureConfigurationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LifecycleExecutionSnapshotResourceTypeDef(BaseModel):
    snapshotId: Optional[str] = None
    state: Optional[LifecycleExecutionResourceStateTypeDef] = None

class LifecycleExecutionTypeDef(BaseModel):
    lifecycleExecutionId: Optional[str] = None
    lifecyclePolicyArn: Optional[str] = None
    resourcesImpactedSummary: Optional[LifecycleExecutionResourcesImpactedSummaryTypeDef] = None
    state: Optional[LifecycleExecutionStateTypeDef] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class LifecyclePolicyDetailActionTypeDef(BaseModel):
    type: LifecyclePolicyDetailActionTypeType
    includeResources: Optional[LifecyclePolicyDetailActionIncludeResourcesTypeDef] = None

class LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef(BaseModel):
    isPublic: Optional[bool] = None
    regions: Optional[List[str]] = None
    sharedAccounts: Optional[List[str]] = None
    lastLaunched: Optional[LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef] = None
    tagMap: Optional[Dict[str, str]] = None

class LifecyclePolicyDetailExclusionRulesAmisTypeDef(BaseModel):
    isPublic: Optional[bool] = None
    regions: Optional[Sequence[str]] = None
    sharedAccounts: Optional[Sequence[str]] = None
    lastLaunched: Optional[LifecyclePolicyDetailExclusionRulesAmisLastLaunchedTypeDef] = None
    tagMap: Optional[Mapping[str, str]] = None

class LifecyclePolicyResourceSelectionOutputTypeDef(BaseModel):
    recipes: Optional[List[LifecyclePolicyResourceSelectionRecipeTypeDef]] = None
    tagMap: Optional[Dict[str, str]] = None

class LifecyclePolicyResourceSelectionTypeDef(BaseModel):
    recipes: Optional[Sequence[LifecyclePolicyResourceSelectionRecipeTypeDef]] = None
    tagMap: Optional[Mapping[str, str]] = None

class ListLifecyclePoliciesResponseTypeDef(BaseModel):
    lifecyclePolicySummaryList: List[LifecyclePolicySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWaitingWorkflowStepsResponseTypeDef(BaseModel):
    steps: List[WorkflowStepExecutionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowExecutionsResponseTypeDef(BaseModel):
    requestId: str
    workflowExecutions: List[WorkflowExecutionMetadataTypeDef]
    imageBuildVersionArn: str
    message: str
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowStepExecutionsResponseTypeDef(BaseModel):
    requestId: str
    steps: List[WorkflowStepMetadataTypeDef]
    workflowBuildVersionArn: str
    workflowExecutionId: str
    imageBuildVersionArn: str
    message: str
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWorkflowsResponseTypeDef(BaseModel):
    workflowVersionList: List[WorkflowVersionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LoggingTypeDef(BaseModel):
    s3Logs: Optional[S3LogsTypeDef] = None

class PackageVulnerabilityDetailsTypeDef(BaseModel):
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

class RemediationTypeDef(BaseModel):
    recommendation: Optional[RemediationRecommendationTypeDef] = None

class WorkflowConfigurationOutputTypeDef(BaseModel):
    workflowArn: str
    parameters: Optional[List[WorkflowParameterOutputTypeDef]] = None
    parallelGroup: Optional[str] = None
    onFailure: Optional[OnWorkflowFailureType] = None

class WorkflowConfigurationTypeDef(BaseModel):
    workflowArn: str
    parameters: Optional[Sequence[WorkflowParameterTypeDef]] = None
    parallelGroup: Optional[str] = None
    onFailure: Optional[OnWorkflowFailureType] = None

class WorkflowSummaryTypeDef(BaseModel):
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

class WorkflowTypeDef(BaseModel):
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

class ImageScanFindingAggregationTypeDef(BaseModel):
    accountAggregation: Optional[AccountAggregationTypeDef] = None
    imageAggregation: Optional[ImageAggregationTypeDef] = None
    imagePipelineAggregation: Optional[ImagePipelineAggregationTypeDef] = None
    vulnerabilityIdAggregation: Optional[VulnerabilityIdAggregationTypeDef] = None

class OutputResourcesTypeDef(BaseModel):
    amis: Optional[List[AmiTypeDef]] = None
    containers: Optional[List[ContainerTypeDef]] = None

class ListComponentBuildVersionsResponseTypeDef(BaseModel):
    requestId: str
    componentSummaryList: List[ComponentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetComponentResponseTypeDef(BaseModel):
    requestId: str
    component: ComponentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InspectorScoreDetailsTypeDef(BaseModel):
    adjustedCvss: Optional[CvssScoreDetailsTypeDef] = None

class ImageRecipeTypeDef(BaseModel):
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

class InstanceConfigurationOutputTypeDef(BaseModel):
    image: Optional[str] = None
    blockDeviceMappings: Optional[List[InstanceBlockDeviceMappingTypeDef]] = None

class InstanceConfigurationTypeDef(BaseModel):
    image: Optional[str] = None
    blockDeviceMappings: Optional[Sequence[InstanceBlockDeviceMappingTypeDef]] = None

class DistributionOutputTypeDef(BaseModel):
    region: str
    amiDistributionConfiguration: Optional[AmiDistributionConfigurationOutputTypeDef] = None
    containerDistributionConfiguration: Optional[       ContainerDistributionConfigurationOutputTypeDef     ] = None
    licenseConfigurationArns: Optional[List[str]] = None
    launchTemplateConfigurations: Optional[List[LaunchTemplateConfigurationTypeDef]] = None
    s3ExportConfiguration: Optional[S3ExportConfigurationTypeDef] = None
    fastLaunchConfigurations: Optional[List[FastLaunchConfigurationTypeDef]] = None

class DistributionTypeDef(BaseModel):
    region: str
    amiDistributionConfiguration: Optional[AmiDistributionConfigurationTypeDef] = None
    containerDistributionConfiguration: Optional[       ContainerDistributionConfigurationTypeDef     ] = None
    licenseConfigurationArns: Optional[Sequence[str]] = None
    launchTemplateConfigurations: Optional[Sequence[LaunchTemplateConfigurationTypeDef]] = None
    s3ExportConfiguration: Optional[S3ExportConfigurationTypeDef] = None
    fastLaunchConfigurations: Optional[Sequence[FastLaunchConfigurationTypeDef]] = None

class LifecycleExecutionResourceTypeDef(BaseModel):
    accountId: Optional[str] = None
    resourceId: Optional[str] = None
    state: Optional[LifecycleExecutionResourceStateTypeDef] = None
    action: Optional[LifecycleExecutionResourceActionTypeDef] = None
    region: Optional[str] = None
    snapshots: Optional[List[LifecycleExecutionSnapshotResourceTypeDef]] = None
    imageUris: Optional[List[str]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

class GetLifecycleExecutionResponseTypeDef(BaseModel):
    lifecycleExecution: LifecycleExecutionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListLifecycleExecutionsResponseTypeDef(BaseModel):
    lifecycleExecutions: List[LifecycleExecutionTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LifecyclePolicyDetailExclusionRulesOutputTypeDef(BaseModel):
    tagMap: Optional[Dict[str, str]] = None
    amis: Optional[LifecyclePolicyDetailExclusionRulesAmisOutputTypeDef] = None

class LifecyclePolicyDetailExclusionRulesTypeDef(BaseModel):
    tagMap: Optional[Mapping[str, str]] = None
    amis: Optional[LifecyclePolicyDetailExclusionRulesAmisTypeDef] = None

class ResourceStateUpdateExclusionRulesTypeDef(BaseModel):
    amis: Optional[LifecyclePolicyDetailExclusionRulesAmisTypeDef] = None

class CreateInfrastructureConfigurationRequestRequestTypeDef(BaseModel):
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

class InfrastructureConfigurationTypeDef(BaseModel):
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

class UpdateInfrastructureConfigurationRequestRequestTypeDef(BaseModel):
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

class ImagePipelineTypeDef(BaseModel):
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

class ListWorkflowBuildVersionsResponseTypeDef(BaseModel):
    workflowSummaryList: List[WorkflowSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetWorkflowResponseTypeDef(BaseModel):
    workflow: WorkflowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListImageScanFindingAggregationsResponseTypeDef(BaseModel):
    requestId: str
    aggregationType: str
    responses: List[ImageScanFindingAggregationTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImageSummaryTypeDef(BaseModel):
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

class CreateImageRecipeRequestRequestTypeDef(BaseModel):
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

class ImageScanFindingTypeDef(BaseModel):
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

class GetImageRecipeResponseTypeDef(BaseModel):
    requestId: str
    imageRecipe: ImageRecipeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ContainerRecipeTypeDef(BaseModel):
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

class CreateContainerRecipeRequestRequestTypeDef(BaseModel):
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

class DistributionConfigurationTypeDef(BaseModel):
    timeoutMinutes: int
    arn: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    distributions: Optional[List[DistributionOutputTypeDef]] = None
    dateCreated: Optional[str] = None
    dateUpdated: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListLifecycleExecutionResourcesResponseTypeDef(BaseModel):
    lifecycleExecutionId: str
    lifecycleExecutionState: LifecycleExecutionStateTypeDef
    resources: List[LifecycleExecutionResourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class LifecyclePolicyDetailOutputTypeDef(BaseModel):
    action: LifecyclePolicyDetailActionTypeDef
    filter: LifecyclePolicyDetailFilterTypeDef
    exclusionRules: Optional[LifecyclePolicyDetailExclusionRulesOutputTypeDef] = None

class LifecyclePolicyDetailTypeDef(BaseModel):
    action: LifecyclePolicyDetailActionTypeDef
    filter: LifecyclePolicyDetailFilterTypeDef
    exclusionRules: Optional[LifecyclePolicyDetailExclusionRulesTypeDef] = None

class StartResourceStateUpdateRequestRequestTypeDef(BaseModel):
    resourceArn: str
    state: ResourceStateTypeDef
    clientToken: str
    executionRole: Optional[str] = None
    includeResources: Optional[ResourceStateUpdateIncludeResourcesTypeDef] = None
    exclusionRules: Optional[ResourceStateUpdateExclusionRulesTypeDef] = None
    updateAt: Optional[TimestampTypeDef] = None

class GetInfrastructureConfigurationResponseTypeDef(BaseModel):
    requestId: str
    infrastructureConfiguration: InfrastructureConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetImagePipelineResponseTypeDef(BaseModel):
    requestId: str
    imagePipeline: ImagePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListImagePipelinesResponseTypeDef(BaseModel):
    requestId: str
    imagePipelineList: List[ImagePipelineTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateImagePipelineRequestRequestTypeDef(BaseModel):
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

class CreateImageRequestRequestTypeDef(BaseModel):
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

class UpdateImagePipelineRequestRequestTypeDef(BaseModel):
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

class ListImageBuildVersionsResponseTypeDef(BaseModel):
    requestId: str
    imageSummaryList: List[ImageSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImagePipelineImagesResponseTypeDef(BaseModel):
    requestId: str
    imageSummaryList: List[ImageSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListImageScanFindingsResponseTypeDef(BaseModel):
    requestId: str
    findings: List[ImageScanFindingTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetContainerRecipeResponseTypeDef(BaseModel):
    requestId: str
    containerRecipe: ContainerRecipeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDistributionConfigurationResponseTypeDef(BaseModel):
    requestId: str
    distributionConfiguration: DistributionConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImageTypeDef(BaseModel):
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

class CreateDistributionConfigurationRequestRequestTypeDef(BaseModel):
    name: str
    distributions: Sequence[DistributionUnionTypeDef]
    clientToken: str
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateDistributionConfigurationRequestRequestTypeDef(BaseModel):
    distributionConfigurationArn: str
    distributions: Sequence[DistributionUnionTypeDef]
    clientToken: str
    description: Optional[str] = None

class LifecyclePolicyTypeDef(BaseModel):
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

class GetImageResponseTypeDef(BaseModel):
    requestId: str
    image: ImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetLifecyclePolicyResponseTypeDef(BaseModel):
    lifecyclePolicy: LifecyclePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateLifecyclePolicyRequestRequestTypeDef(BaseModel):
    name: str
    executionRole: str
    resourceType: LifecyclePolicyResourceTypeType
    policyDetails: Sequence[LifecyclePolicyDetailUnionTypeDef]
    resourceSelection: LifecyclePolicyResourceSelectionTypeDef
    clientToken: str
    description: Optional[str] = None
    status: Optional[LifecyclePolicyStatusType] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateLifecyclePolicyRequestRequestTypeDef(BaseModel):
    lifecyclePolicyArn: str
    executionRole: str
    resourceType: LifecyclePolicyResourceTypeType
    policyDetails: Sequence[LifecyclePolicyDetailUnionTypeDef]
    resourceSelection: LifecyclePolicyResourceSelectionTypeDef
    clientToken: str
    description: Optional[str] = None
    status: Optional[LifecyclePolicyStatusType] = None

