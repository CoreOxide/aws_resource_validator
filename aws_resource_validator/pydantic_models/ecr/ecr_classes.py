from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ecr.ecr_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class Attribute(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class AuthorizationData(BaseValidatorModel):
    authorizationToken: Optional[str] = None
    expiresAt: Optional[datetime] = None
    proxyEndpoint: Optional[str] = None


class AwsEcrContainerImageDetails(BaseValidatorModel):
    architecture: Optional[str] = None
    author: Optional[str] = None
    imageHash: Optional[str] = None
    imageTags: Optional[List[str]] = None
    platform: Optional[str] = None
    pushedAt: Optional[datetime] = None
    registry: Optional[str] = None
    repositoryName: Optional[str] = None


# This class is the input for the 'batch_check_layer_availability' function.
class BatchCheckLayerAvailabilityRequest(BaseValidatorModel):
    repositoryName: str
    layerDigests: List[str]
    registryId: Optional[str] = None


class LayerFailure(BaseValidatorModel):
    layerDigest: Optional[str] = None
    failureCode: Optional[LayerFailureCodeType] = None
    failureReason: Optional[str] = None


class Layer(BaseValidatorModel):
    layerDigest: Optional[str] = None
    layerAvailability: Optional[LayerAvailabilityType] = None
    layerSize: Optional[int] = None
    mediaType: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ImageIdentifier(BaseValidatorModel):
    imageDigest: Optional[str] = None
    imageTag: Optional[str] = None


# This class is the input for the 'batch_get_repository_scanning_configuration' function.
class BatchGetRepositoryScanningConfigurationRequest(BaseValidatorModel):
    repositoryNames: List[str]


class RepositoryScanningConfigurationFailure(BaseValidatorModel):
    repositoryName: Optional[str] = None
    failureCode: Optional[Literal['REPOSITORY_NOT_FOUND']] = None
    failureReason: Optional[str] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


# This class is the input for the 'complete_layer_upload' function.
class CompleteLayerUploadRequest(BaseValidatorModel):
    repositoryName: str
    uploadId: str
    layerDigests: List[str]
    registryId: Optional[str] = None


# This class is the input for the 'create_pull_through_cache_rule' function.
class CreatePullThroughCacheRuleRequest(BaseValidatorModel):
    ecrRepositoryPrefix: str
    upstreamRegistryUrl: str
    registryId: Optional[str] = None
    upstreamRegistry: Optional[UpstreamRegistryType] = None
    credentialArn: Optional[str] = None


class EncryptionConfigurationForRepositoryCreationTemplate(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKey: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class EncryptionConfiguration(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKey: Optional[str] = None


class ImageScanningConfiguration(BaseValidatorModel):
    scanOnPush: Optional[bool] = None


class CvssScoreAdjustment(BaseValidatorModel):
    metric: Optional[str] = None
    reason: Optional[str] = None


class CvssScore(BaseValidatorModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None
    source: Optional[str] = None
    version: Optional[str] = None


# This class is the input for the 'delete_lifecycle_policy' function.
class DeleteLifecyclePolicyRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


# This class is the input for the 'delete_pull_through_cache_rule' function.
class DeletePullThroughCacheRuleRequest(BaseValidatorModel):
    ecrRepositoryPrefix: str
    registryId: Optional[str] = None


# This class is the input for the 'delete_repository_creation_template' function.
class DeleteRepositoryCreationTemplateRequest(BaseValidatorModel):
    prefix: str


# This class is the input for the 'delete_repository_policy' function.
class DeleteRepositoryPolicyRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


# This class is the input for the 'delete_repository' function.
class DeleteRepositoryRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    force: Optional[bool] = None


class ImageReplicationStatus(BaseValidatorModel):
    region: Optional[str] = None
    registryId: Optional[str] = None
    status: Optional[ReplicationStatusType] = None
    failureCode: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class WaiterConfig(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class ImageScanStatus(BaseValidatorModel):
    status: Optional[ScanStatusType] = None
    description: Optional[str] = None


class DescribeImagesFilter(BaseValidatorModel):
    tagStatus: Optional[TagStatusType] = None


# This class is the input for the 'describe_pull_through_cache_rules' function.
class DescribePullThroughCacheRulesRequest(BaseValidatorModel):
    registryId: Optional[str] = None
    ecrRepositoryPrefixes: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PullThroughCacheRule(BaseValidatorModel):
    ecrRepositoryPrefix: Optional[str] = None
    upstreamRegistryUrl: Optional[str] = None
    createdAt: Optional[datetime] = None
    registryId: Optional[str] = None
    credentialArn: Optional[str] = None
    upstreamRegistry: Optional[UpstreamRegistryType] = None
    updatedAt: Optional[datetime] = None


# This class is the input for the 'describe_repositories' function.
class DescribeRepositoriesRequest(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'describe_repository_creation_templates' function.
class DescribeRepositoryCreationTemplatesRequest(BaseValidatorModel):
    prefixes: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'get_account_setting' function.
class GetAccountSettingRequest(BaseValidatorModel):
    name: str


# This class is the input for the 'get_authorization_token' function.
class GetAuthorizationTokenRequest(BaseValidatorModel):
    registryIds: Optional[List[str]] = None


# This class is the input for the 'get_download_url_for_layer' function.
class GetDownloadUrlForLayerRequest(BaseValidatorModel):
    repositoryName: str
    layerDigest: str
    registryId: Optional[str] = None


class LifecyclePolicyPreviewFilter(BaseValidatorModel):
    tagStatus: Optional[TagStatusType] = None


class LifecyclePolicyPreviewSummary(BaseValidatorModel):
    expiringImageTotalCount: Optional[int] = None


# This class is the input for the 'get_lifecycle_policy' function.
class GetLifecyclePolicyRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


# This class is the input for the 'get_repository_policy' function.
class GetRepositoryPolicyRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class ImageScanFindingsSummary(BaseValidatorModel):
    imageScanCompletedAt: Optional[datetime] = None
    vulnerabilitySourceUpdatedAt: Optional[datetime] = None
    findingSeverityCounts: Optional[Dict[FindingSeverityType, int]] = None


# This class is the input for the 'initiate_layer_upload' function.
class InitiateLayerUploadRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class LifecyclePolicyRuleAction(BaseValidatorModel):
    type: Optional[Literal['EXPIRE']] = None


class ListImagesFilter(BaseValidatorModel):
    tagStatus: Optional[TagStatusType] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class VulnerablePackage(BaseValidatorModel):
    arch: Optional[str] = None
    epoch: Optional[int] = None
    filePath: Optional[str] = None
    name: Optional[str] = None
    packageManager: Optional[str] = None
    release: Optional[str] = None
    sourceLayerHash: Optional[str] = None
    version: Optional[str] = None
    fixedInVersion: Optional[str] = None


# This class is the input for the 'put_account_setting' function.
class PutAccountSettingRequest(BaseValidatorModel):
    name: str
    value: str


# This class is the input for the 'put_image' function.
class PutImageRequest(BaseValidatorModel):
    repositoryName: str
    imageManifest: str
    registryId: Optional[str] = None
    imageManifestMediaType: Optional[str] = None
    imageTag: Optional[str] = None
    imageDigest: Optional[str] = None


# This class is the input for the 'put_image_tag_mutability' function.
class PutImageTagMutabilityRequest(BaseValidatorModel):
    repositoryName: str
    imageTagMutability: ImageTagMutabilityType
    registryId: Optional[str] = None


# This class is the input for the 'put_lifecycle_policy' function.
class PutLifecyclePolicyRequest(BaseValidatorModel):
    repositoryName: str
    lifecyclePolicyText: str
    registryId: Optional[str] = None


# This class is the input for the 'put_registry_policy' function.
class PutRegistryPolicyRequest(BaseValidatorModel):
    policyText: str


class Recommendation(BaseValidatorModel):
    url: Optional[str] = None
    text: Optional[str] = None


class ScanningRepositoryFilter(BaseValidatorModel):
    filter: str
    filterType: Literal['WILDCARD']


class ReplicationDestination(BaseValidatorModel):
    region: str
    registryId: str


class RepositoryFilter(BaseValidatorModel):
    filter: str
    filterType: Literal['PREFIX_MATCH']


# This class is the input for the 'set_repository_policy' function.
class SetRepositoryPolicyRequest(BaseValidatorModel):
    repositoryName: str
    policyText: str
    registryId: Optional[str] = None
    force: Optional[bool] = None


# This class is the input for the 'start_lifecycle_policy_preview' function.
class StartLifecyclePolicyPreviewRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    lifecyclePolicyText: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_pull_through_cache_rule' function.
class UpdatePullThroughCacheRuleRequest(BaseValidatorModel):
    ecrRepositoryPrefix: str
    credentialArn: str
    registryId: Optional[str] = None


# This class is the input for the 'validate_pull_through_cache_rule' function.
class ValidatePullThroughCacheRuleRequest(BaseValidatorModel):
    ecrRepositoryPrefix: str
    registryId: Optional[str] = None


class ImageScanFinding(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    uri: Optional[str] = None
    severity: Optional[FindingSeverityType] = None
    attributes: Optional[List[Attribute]] = None


class ResourceDetails(BaseValidatorModel):
    awsEcrContainerImage: Optional[AwsEcrContainerImageDetails] = None


# This class is the output for the 'batch_check_layer_availability' function.
class BatchCheckLayerAvailabilityResponse(BaseValidatorModel):
    layers: List[Layer]
    failures: List[LayerFailure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'complete_layer_upload' function.
class CompleteLayerUploadResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    uploadId: str
    layerDigest: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_pull_through_cache_rule' function.
class CreatePullThroughCacheRuleResponse(BaseValidatorModel):
    ecrRepositoryPrefix: str
    upstreamRegistryUrl: str
    createdAt: datetime
    registryId: str
    upstreamRegistry: UpstreamRegistryType
    credentialArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_lifecycle_policy' function.
class DeleteLifecyclePolicyResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    lastEvaluatedAt: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_pull_through_cache_rule' function.
class DeletePullThroughCacheRuleResponse(BaseValidatorModel):
    ecrRepositoryPrefix: str
    upstreamRegistryUrl: str
    createdAt: datetime
    registryId: str
    credentialArn: str
    ResponseMetadata: ResponseMetadata


class DeleteRegistryPolicyResponse(BaseValidatorModel):
    registryId: str
    policyText: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_repository_policy' function.
class DeleteRepositoryPolicyResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_account_setting' function.
class GetAccountSettingResponse(BaseValidatorModel):
    name: str
    value: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_authorization_token' function.
class GetAuthorizationTokenResponse(BaseValidatorModel):
    authorizationData: List[AuthorizationData]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_download_url_for_layer' function.
class GetDownloadUrlForLayerResponse(BaseValidatorModel):
    downloadUrl: str
    layerDigest: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_lifecycle_policy' function.
class GetLifecyclePolicyResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    lastEvaluatedAt: datetime
    ResponseMetadata: ResponseMetadata


class GetRegistryPolicyResponse(BaseValidatorModel):
    registryId: str
    policyText: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_repository_policy' function.
class GetRepositoryPolicyResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'initiate_layer_upload' function.
class InitiateLayerUploadResponse(BaseValidatorModel):
    uploadId: str
    partSize: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_account_setting' function.
class PutAccountSettingResponse(BaseValidatorModel):
    name: str
    value: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_image_tag_mutability' function.
class PutImageTagMutabilityResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    imageTagMutability: ImageTagMutabilityType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_lifecycle_policy' function.
class PutLifecyclePolicyResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_registry_policy' function.
class PutRegistryPolicyResponse(BaseValidatorModel):
    registryId: str
    policyText: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'set_repository_policy' function.
class SetRepositoryPolicyResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_lifecycle_policy_preview' function.
class StartLifecyclePolicyPreviewResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    status: LifecyclePolicyPreviewStatusType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_pull_through_cache_rule' function.
class UpdatePullThroughCacheRuleResponse(BaseValidatorModel):
    ecrRepositoryPrefix: str
    registryId: str
    updatedAt: datetime
    credentialArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'upload_layer_part' function.
class UploadLayerPartResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    uploadId: str
    lastByteReceived: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'validate_pull_through_cache_rule' function.
class ValidatePullThroughCacheRuleResponse(BaseValidatorModel):
    ecrRepositoryPrefix: str
    registryId: str
    upstreamRegistryUrl: str
    credentialArn: str
    isValid: bool
    failure: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_delete_image' function.
class BatchDeleteImageRequest(BaseValidatorModel):
    repositoryName: str
    imageIds: List[ImageIdentifier]
    registryId: Optional[str] = None


# This class is the input for the 'batch_get_image' function.
class BatchGetImageRequest(BaseValidatorModel):
    repositoryName: str
    imageIds: List[ImageIdentifier]
    registryId: Optional[str] = None
    acceptedMediaTypes: Optional[List[str]] = None


# This class is the input for the 'describe_image_replication_status' function.
class DescribeImageReplicationStatusRequest(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifier
    registryId: Optional[str] = None


# This class is the input for the 'describe_image_scan_findings' function.
class DescribeImageScanFindingsRequest(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifier
    registryId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ImageFailure(BaseValidatorModel):
    imageId: Optional[ImageIdentifier] = None
    failureCode: Optional[ImageFailureCodeType] = None
    failureReason: Optional[str] = None


class Image(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    imageId: Optional[ImageIdentifier] = None
    imageManifest: Optional[str] = None
    imageManifestMediaType: Optional[str] = None


# This class is the output for the 'list_images' function.
class ListImagesResponse(BaseValidatorModel):
    imageIds: List[ImageIdentifier]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'start_image_scan' function.
class StartImageScanRequest(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifier
    registryId: Optional[str] = None


# This class is the input for the 'upload_layer_part' function.
class UploadLayerPartRequest(BaseValidatorModel):
    repositoryName: str
    uploadId: str
    partFirstByte: int
    partLastByte: int
    layerPartBlob: Blob
    registryId: Optional[str] = None


# This class is the input for the 'create_repository_creation_template' function.
class CreateRepositoryCreationTemplateRequest(BaseValidatorModel):
    prefix: str
    appliedFor: List[RCTAppliedForType]
    description: Optional[str] = None
    encryptionConfiguration: Optional[EncryptionConfigurationForRepositoryCreationTemplate] = None
    resourceTags: Optional[List[Tag]] = None
    imageTagMutability: Optional[ImageTagMutabilityType] = None
    repositoryPolicy: Optional[str] = None
    lifecyclePolicy: Optional[str] = None
    customRoleArn: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class RepositoryCreationTemplate(BaseValidatorModel):
    prefix: Optional[str] = None
    description: Optional[str] = None
    encryptionConfiguration: Optional[EncryptionConfigurationForRepositoryCreationTemplate] = None
    resourceTags: Optional[List[Tag]] = None
    imageTagMutability: Optional[ImageTagMutabilityType] = None
    repositoryPolicy: Optional[str] = None
    lifecyclePolicy: Optional[str] = None
    appliedFor: Optional[List[RCTAppliedForType]] = None
    customRoleArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


# This class is the input for the 'update_repository_creation_template' function.
class UpdateRepositoryCreationTemplateRequest(BaseValidatorModel):
    prefix: str
    description: Optional[str] = None
    encryptionConfiguration: Optional[EncryptionConfigurationForRepositoryCreationTemplate] = None
    resourceTags: Optional[List[Tag]] = None
    imageTagMutability: Optional[ImageTagMutabilityType] = None
    repositoryPolicy: Optional[str] = None
    lifecyclePolicy: Optional[str] = None
    appliedFor: Optional[List[RCTAppliedForType]] = None
    customRoleArn: Optional[str] = None


# This class is the input for the 'create_repository' function.
class CreateRepositoryRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    tags: Optional[List[Tag]] = None
    imageTagMutability: Optional[ImageTagMutabilityType] = None
    imageScanningConfiguration: Optional[ImageScanningConfiguration] = None
    encryptionConfiguration: Optional[EncryptionConfiguration] = None


# This class is the input for the 'put_image_scanning_configuration' function.
class PutImageScanningConfigurationRequest(BaseValidatorModel):
    repositoryName: str
    imageScanningConfiguration: ImageScanningConfiguration
    registryId: Optional[str] = None


# This class is the output for the 'put_image_scanning_configuration' function.
class PutImageScanningConfigurationResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    imageScanningConfiguration: ImageScanningConfiguration
    ResponseMetadata: ResponseMetadata


class Repository(BaseValidatorModel):
    repositoryArn: Optional[str] = None
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    repositoryUri: Optional[str] = None
    createdAt: Optional[datetime] = None
    imageTagMutability: Optional[ImageTagMutabilityType] = None
    imageScanningConfiguration: Optional[ImageScanningConfiguration] = None
    encryptionConfiguration: Optional[EncryptionConfiguration] = None


class CvssScoreDetails(BaseValidatorModel):
    adjustments: Optional[List[CvssScoreAdjustment]] = None
    score: Optional[float] = None
    scoreSource: Optional[str] = None
    scoringVector: Optional[str] = None
    version: Optional[str] = None


# This class is the output for the 'describe_image_replication_status' function.
class DescribeImageReplicationStatusResponse(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifier
    replicationStatuses: List[ImageReplicationStatus]
    ResponseMetadata: ResponseMetadata


class DescribeImageScanFindingsRequestPaginate(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifier
    registryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribePullThroughCacheRulesRequestPaginate(BaseValidatorModel):
    registryId: Optional[str] = None
    ecrRepositoryPrefixes: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRepositoriesRequestPaginate(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRepositoryCreationTemplatesRequestPaginate(BaseValidatorModel):
    prefixes: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeImageScanFindingsRequestWait(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifier
    registryId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfig] = None


# This class is the output for the 'start_image_scan' function.
class StartImageScanResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    imageId: ImageIdentifier
    imageScanStatus: ImageScanStatus
    ResponseMetadata: ResponseMetadata


class DescribeImagesRequestPaginate(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[List[ImageIdentifier]] = None
    filter: Optional[DescribeImagesFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'describe_images' function.
class DescribeImagesRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[List[ImageIdentifier]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[DescribeImagesFilter] = None


# This class is the output for the 'describe_pull_through_cache_rules' function.
class DescribePullThroughCacheRulesResponse(BaseValidatorModel):
    pullThroughCacheRules: List[PullThroughCacheRule]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetLifecyclePolicyPreviewRequestPaginate(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[List[ImageIdentifier]] = None
    filter: Optional[LifecyclePolicyPreviewFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_lifecycle_policy_preview' function.
class GetLifecyclePolicyPreviewRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[List[ImageIdentifier]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[LifecyclePolicyPreviewFilter] = None


class GetLifecyclePolicyPreviewRequestWait(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[List[ImageIdentifier]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[LifecyclePolicyPreviewFilter] = None
    WaiterConfig: Optional[WaiterConfig] = None


class ImageDetail(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    imageDigest: Optional[str] = None
    imageTags: Optional[List[str]] = None
    imageSizeInBytes: Optional[int] = None
    imagePushedAt: Optional[datetime] = None
    imageScanStatus: Optional[ImageScanStatus] = None
    imageScanFindingsSummary: Optional[ImageScanFindingsSummary] = None
    imageManifestMediaType: Optional[str] = None
    artifactMediaType: Optional[str] = None
    lastRecordedPullTime: Optional[datetime] = None


class LifecyclePolicyPreviewResult(BaseValidatorModel):
    imageTags: Optional[List[str]] = None
    imageDigest: Optional[str] = None
    imagePushedAt: Optional[datetime] = None
    action: Optional[LifecyclePolicyRuleAction] = None
    appliedRulePriority: Optional[int] = None


class ListImagesRequestPaginate(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    filter: Optional[ListImagesFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_images' function.
class ListImagesRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ListImagesFilter] = None


class PackageVulnerabilityDetails(BaseValidatorModel):
    cvss: Optional[List[CvssScore]] = None
    referenceUrls: Optional[List[str]] = None
    relatedVulnerabilities: Optional[List[str]] = None
    source: Optional[str] = None
    sourceUrl: Optional[str] = None
    vendorCreatedAt: Optional[datetime] = None
    vendorSeverity: Optional[str] = None
    vendorUpdatedAt: Optional[datetime] = None
    vulnerabilityId: Optional[str] = None
    vulnerablePackages: Optional[List[VulnerablePackage]] = None


class Remediation(BaseValidatorModel):
    recommendation: Optional[Recommendation] = None


class RegistryScanningRuleOutput(BaseValidatorModel):
    scanFrequency: ScanFrequencyType
    repositoryFilters: List[ScanningRepositoryFilter]


class RegistryScanningRule(BaseValidatorModel):
    scanFrequency: ScanFrequencyType
    repositoryFilters: List[ScanningRepositoryFilter]


class RepositoryScanningConfiguration(BaseValidatorModel):
    repositoryArn: Optional[str] = None
    repositoryName: Optional[str] = None
    scanOnPush: Optional[bool] = None
    scanFrequency: Optional[ScanFrequencyType] = None
    appliedScanFilters: Optional[List[ScanningRepositoryFilter]] = None


class ReplicationRuleOutput(BaseValidatorModel):
    destinations: List[ReplicationDestination]
    repositoryFilters: Optional[List[RepositoryFilter]] = None


class ReplicationRule(BaseValidatorModel):
    destinations: List[ReplicationDestination]
    repositoryFilters: Optional[List[RepositoryFilter]] = None


class Resource(BaseValidatorModel):
    details: Optional[ResourceDetails] = None
    id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[str] = None


# This class is the output for the 'batch_delete_image' function.
class BatchDeleteImageResponse(BaseValidatorModel):
    imageIds: List[ImageIdentifier]
    failures: List[ImageFailure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_get_image' function.
class BatchGetImageResponse(BaseValidatorModel):
    images: List[Image]
    failures: List[ImageFailure]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_image' function.
class PutImageResponse(BaseValidatorModel):
    image: Image
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_repository_creation_template' function.
class CreateRepositoryCreationTemplateResponse(BaseValidatorModel):
    registryId: str
    repositoryCreationTemplate: RepositoryCreationTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_repository_creation_template' function.
class DeleteRepositoryCreationTemplateResponse(BaseValidatorModel):
    registryId: str
    repositoryCreationTemplate: RepositoryCreationTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_repository_creation_templates' function.
class DescribeRepositoryCreationTemplatesResponse(BaseValidatorModel):
    registryId: str
    repositoryCreationTemplates: List[RepositoryCreationTemplate]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'update_repository_creation_template' function.
class UpdateRepositoryCreationTemplateResponse(BaseValidatorModel):
    registryId: str
    repositoryCreationTemplate: RepositoryCreationTemplate
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_repository' function.
class CreateRepositoryResponse(BaseValidatorModel):
    repository: Repository
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_repository' function.
class DeleteRepositoryResponse(BaseValidatorModel):
    repository: Repository
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_repositories' function.
class DescribeRepositoriesResponse(BaseValidatorModel):
    repositories: List[Repository]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ScoreDetails(BaseValidatorModel):
    cvss: Optional[CvssScoreDetails] = None


# This class is the output for the 'describe_images' function.
class DescribeImagesResponse(BaseValidatorModel):
    imageDetails: List[ImageDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_lifecycle_policy_preview' function.
class GetLifecyclePolicyPreviewResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    status: LifecyclePolicyPreviewStatusType
    previewResults: List[LifecyclePolicyPreviewResult]
    summary: LifecyclePolicyPreviewSummary
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RegistryScanningConfiguration(BaseValidatorModel):
    scanType: Optional[ScanTypeType] = None
    rules: Optional[List[RegistryScanningRuleOutput]] = None

RegistryScanningRuleUnion = Union[RegistryScanningRule, RegistryScanningRuleOutput]


# This class is the output for the 'batch_get_repository_scanning_configuration' function.
class BatchGetRepositoryScanningConfigurationResponse(BaseValidatorModel):
    scanningConfigurations: List[RepositoryScanningConfiguration]
    failures: List[RepositoryScanningConfigurationFailure]
    ResponseMetadata: ResponseMetadata


class ReplicationConfigurationOutput(BaseValidatorModel):
    rules: List[ReplicationRuleOutput]


class ReplicationConfiguration(BaseValidatorModel):
    rules: List[ReplicationRule]


class EnhancedImageScanFinding(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    description: Optional[str] = None
    findingArn: Optional[str] = None
    firstObservedAt: Optional[datetime] = None
    lastObservedAt: Optional[datetime] = None
    packageVulnerabilityDetails: Optional[PackageVulnerabilityDetails] = None
    remediation: Optional[Remediation] = None
    resources: Optional[List[Resource]] = None
    score: Optional[float] = None
    scoreDetails: Optional[ScoreDetails] = None
    severity: Optional[str] = None
    status: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None
    updatedAt: Optional[datetime] = None
    fixAvailable: Optional[str] = None
    exploitAvailable: Optional[str] = None


class GetRegistryScanningConfigurationResponse(BaseValidatorModel):
    registryId: str
    scanningConfiguration: RegistryScanningConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_registry_scanning_configuration' function.
class PutRegistryScanningConfigurationResponse(BaseValidatorModel):
    registryScanningConfiguration: RegistryScanningConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_registry_scanning_configuration' function.
class PutRegistryScanningConfigurationRequest(BaseValidatorModel):
    scanType: Optional[ScanTypeType] = None
    rules: Optional[List[RegistryScanningRuleUnion]] = None


class DescribeRegistryResponse(BaseValidatorModel):
    registryId: str
    replicationConfiguration: ReplicationConfigurationOutput
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_replication_configuration' function.
class PutReplicationConfigurationResponse(BaseValidatorModel):
    replicationConfiguration: ReplicationConfigurationOutput
    ResponseMetadata: ResponseMetadata

ReplicationConfigurationUnion = Union[ReplicationConfiguration, ReplicationConfigurationOutput]


class ImageScanFindings(BaseValidatorModel):
    imageScanCompletedAt: Optional[datetime] = None
    vulnerabilitySourceUpdatedAt: Optional[datetime] = None
    findingSeverityCounts: Optional[Dict[FindingSeverityType, int]] = None
    findings: Optional[List[ImageScanFinding]] = None
    enhancedFindings: Optional[List[EnhancedImageScanFinding]] = None


# This class is the input for the 'put_replication_configuration' function.
class PutReplicationConfigurationRequest(BaseValidatorModel):
    replicationConfiguration: ReplicationConfigurationUnion


# This class is the output for the 'describe_image_scan_findings' function.
class DescribeImageScanFindingsResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    imageId: ImageIdentifier
    imageScanStatus: ImageScanStatus
    imageScanFindings: ImageScanFindings
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None