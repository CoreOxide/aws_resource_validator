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
from aws_resource_validator.pydantic_models.ecr_constants import *

class AttributeTypeDef(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class AuthorizationDataTypeDef(BaseValidatorModel):
    authorizationToken: Optional[str] = None
    expiresAt: Optional[datetime] = None
    proxyEndpoint: Optional[str] = None


class AwsEcrContainerImageDetailsTypeDef(BaseValidatorModel):
    architecture: Optional[str] = None
    author: Optional[str] = None
    imageHash: Optional[str] = None
    imageTags: Optional[List[str]] = None
    platform: Optional[str] = None
    pushedAt: Optional[datetime] = None
    registry: Optional[str] = None
    repositoryName: Optional[str] = None


class BatchCheckLayerAvailabilityRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    layerDigests: Sequence[str]
    registryId: Optional[str] = None


class LayerFailureTypeDef(BaseValidatorModel):
    layerDigest: Optional[str] = None
    failureCode: Optional[LayerFailureCodeType] = None
    failureReason: Optional[str] = None


class LayerTypeDef(BaseValidatorModel):
    layerDigest: Optional[str] = None
    layerAvailability: Optional[LayerAvailabilityType] = None
    layerSize: Optional[int] = None
    mediaType: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ImageIdentifierTypeDef(BaseValidatorModel):
    imageDigest: Optional[str] = None
    imageTag: Optional[str] = None


class BatchGetRepositoryScanningConfigurationRequestTypeDef(BaseValidatorModel):
    repositoryNames: Sequence[str]


class RepositoryScanningConfigurationFailureTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    failureCode: Optional[Literal["REPOSITORY_NOT_FOUND"]] = None
    failureReason: Optional[str] = None


class CompleteLayerUploadRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    uploadId: str
    layerDigests: Sequence[str]
    registryId: Optional[str] = None


class CreatePullThroughCacheRuleRequestTypeDef(BaseValidatorModel):
    ecrRepositoryPrefix: str
    upstreamRegistryUrl: str
    registryId: Optional[str] = None
    upstreamRegistry: Optional[UpstreamRegistryType] = None
    credentialArn: Optional[str] = None


class EncryptionConfigurationForRepositoryCreationTemplateTypeDef(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKey: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str


class EncryptionConfigurationTypeDef(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKey: Optional[str] = None


class ImageScanningConfigurationTypeDef(BaseValidatorModel):
    scanOnPush: Optional[bool] = None


class CvssScoreAdjustmentTypeDef(BaseValidatorModel):
    metric: Optional[str] = None
    reason: Optional[str] = None


class CvssScoreTypeDef(BaseValidatorModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None
    source: Optional[str] = None
    version: Optional[str] = None


class DeleteLifecyclePolicyRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class DeletePullThroughCacheRuleRequestTypeDef(BaseValidatorModel):
    ecrRepositoryPrefix: str
    registryId: Optional[str] = None


class DeleteRepositoryCreationTemplateRequestTypeDef(BaseValidatorModel):
    prefix: str


class DeleteRepositoryPolicyRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class DeleteRepositoryRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    force: Optional[bool] = None


class ImageReplicationStatusTypeDef(BaseValidatorModel):
    region: Optional[str] = None
    registryId: Optional[str] = None
    status: Optional[ReplicationStatusType] = None
    failureCode: Optional[str] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class WaiterConfigTypeDef(BaseValidatorModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None


class ImageScanStatusTypeDef(BaseValidatorModel):
    status: Optional[ScanStatusType] = None
    description: Optional[str] = None


class DescribeImagesFilterTypeDef(BaseValidatorModel):
    tagStatus: Optional[TagStatusType] = None


class DescribePullThroughCacheRulesRequestTypeDef(BaseValidatorModel):
    registryId: Optional[str] = None
    ecrRepositoryPrefixes: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PullThroughCacheRuleTypeDef(BaseValidatorModel):
    ecrRepositoryPrefix: Optional[str] = None
    upstreamRegistryUrl: Optional[str] = None
    createdAt: Optional[datetime] = None
    registryId: Optional[str] = None
    credentialArn: Optional[str] = None
    upstreamRegistry: Optional[UpstreamRegistryType] = None
    updatedAt: Optional[datetime] = None


class DescribeRepositoriesRequestTypeDef(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeRepositoryCreationTemplatesRequestTypeDef(BaseValidatorModel):
    prefixes: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class GetAccountSettingRequestTypeDef(BaseValidatorModel):
    name: str


class GetAuthorizationTokenRequestTypeDef(BaseValidatorModel):
    registryIds: Optional[Sequence[str]] = None


class GetDownloadUrlForLayerRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    layerDigest: str
    registryId: Optional[str] = None


class LifecyclePolicyPreviewFilterTypeDef(BaseValidatorModel):
    tagStatus: Optional[TagStatusType] = None


class LifecyclePolicyPreviewSummaryTypeDef(BaseValidatorModel):
    expiringImageTotalCount: Optional[int] = None


class GetLifecyclePolicyRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class GetRepositoryPolicyRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class ImageScanFindingsSummaryTypeDef(BaseValidatorModel):
    imageScanCompletedAt: Optional[datetime] = None
    vulnerabilitySourceUpdatedAt: Optional[datetime] = None
    findingSeverityCounts: Optional[Dict[FindingSeverityType, int]] = None


class InitiateLayerUploadRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class ListImagesFilterTypeDef(BaseValidatorModel):
    tagStatus: Optional[TagStatusType] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class VulnerablePackageTypeDef(BaseValidatorModel):
    arch: Optional[str] = None
    epoch: Optional[int] = None
    filePath: Optional[str] = None
    name: Optional[str] = None
    packageManager: Optional[str] = None
    release: Optional[str] = None
    sourceLayerHash: Optional[str] = None
    version: Optional[str] = None
    fixedInVersion: Optional[str] = None


class PutAccountSettingRequestTypeDef(BaseValidatorModel):
    name: str
    value: str


class PutImageRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageManifest: str
    registryId: Optional[str] = None
    imageManifestMediaType: Optional[str] = None
    imageTag: Optional[str] = None
    imageDigest: Optional[str] = None


class PutImageTagMutabilityRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageTagMutability: ImageTagMutabilityType
    registryId: Optional[str] = None


class PutLifecyclePolicyRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    lifecyclePolicyText: str
    registryId: Optional[str] = None


class PutRegistryPolicyRequestTypeDef(BaseValidatorModel):
    policyText: str


class RecommendationTypeDef(BaseValidatorModel):
    url: Optional[str] = None
    text: Optional[str] = None


class ReplicationDestinationTypeDef(BaseValidatorModel):
    region: str
    registryId: str


class SetRepositoryPolicyRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    policyText: str
    registryId: Optional[str] = None
    force: Optional[bool] = None


class StartLifecyclePolicyPreviewRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    lifecyclePolicyText: Optional[str] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdatePullThroughCacheRuleRequestTypeDef(BaseValidatorModel):
    ecrRepositoryPrefix: str
    credentialArn: str
    registryId: Optional[str] = None


class ValidatePullThroughCacheRuleRequestTypeDef(BaseValidatorModel):
    ecrRepositoryPrefix: str
    registryId: Optional[str] = None


class ImageScanFindingTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    description: Optional[str] = None
    uri: Optional[str] = None
    severity: Optional[FindingSeverityType] = None
    attributes: Optional[List[AttributeTypeDef]] = None


class ResourceDetailsTypeDef(BaseValidatorModel):
    awsEcrContainerImage: Optional[AwsEcrContainerImageDetailsTypeDef] = None


class BatchCheckLayerAvailabilityResponseTypeDef(BaseValidatorModel):
    layers: List[LayerTypeDef]
    failures: List[LayerFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CompleteLayerUploadResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    uploadId: str
    layerDigest: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePullThroughCacheRuleResponseTypeDef(BaseValidatorModel):
    ecrRepositoryPrefix: str
    upstreamRegistryUrl: str
    createdAt: datetime
    registryId: str
    upstreamRegistry: UpstreamRegistryType
    credentialArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    lastEvaluatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DeletePullThroughCacheRuleResponseTypeDef(BaseValidatorModel):
    ecrRepositoryPrefix: str
    upstreamRegistryUrl: str
    createdAt: datetime
    registryId: str
    credentialArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRegistryPolicyResponseTypeDef(BaseValidatorModel):
    registryId: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRepositoryPolicyResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccountSettingResponseTypeDef(BaseValidatorModel):
    name: str
    value: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAuthorizationTokenResponseTypeDef(BaseValidatorModel):
    authorizationData: List[AuthorizationDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetDownloadUrlForLayerResponseTypeDef(BaseValidatorModel):
    downloadUrl: str
    layerDigest: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    lastEvaluatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetRegistryPolicyResponseTypeDef(BaseValidatorModel):
    registryId: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetRepositoryPolicyResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef


class InitiateLayerUploadResponseTypeDef(BaseValidatorModel):
    uploadId: str
    partSize: int
    ResponseMetadata: ResponseMetadataTypeDef


class PutAccountSettingResponseTypeDef(BaseValidatorModel):
    name: str
    value: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutImageTagMutabilityResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    imageTagMutability: ImageTagMutabilityType
    ResponseMetadata: ResponseMetadataTypeDef


class PutLifecyclePolicyResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    ResponseMetadata: ResponseMetadataTypeDef


class PutRegistryPolicyResponseTypeDef(BaseValidatorModel):
    registryId: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef


class SetRepositoryPolicyResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartLifecyclePolicyPreviewResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    status: LifecyclePolicyPreviewStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePullThroughCacheRuleResponseTypeDef(BaseValidatorModel):
    ecrRepositoryPrefix: str
    registryId: str
    updatedAt: datetime
    credentialArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class UploadLayerPartResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    uploadId: str
    lastByteReceived: int
    ResponseMetadata: ResponseMetadataTypeDef


class ValidatePullThroughCacheRuleResponseTypeDef(BaseValidatorModel):
    ecrRepositoryPrefix: str
    registryId: str
    upstreamRegistryUrl: str
    credentialArn: str
    isValid: bool
    failure: str
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDeleteImageRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageIds: Sequence[ImageIdentifierTypeDef]
    registryId: Optional[str] = None


class BatchGetImageRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageIds: Sequence[ImageIdentifierTypeDef]
    registryId: Optional[str] = None
    acceptedMediaTypes: Optional[Sequence[str]] = None


class DescribeImageReplicationStatusRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    registryId: Optional[str] = None


class DescribeImageScanFindingsRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    registryId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ImageFailureTypeDef(BaseValidatorModel):
    imageId: Optional[ImageIdentifierTypeDef] = None
    failureCode: Optional[ImageFailureCodeType] = None
    failureReason: Optional[str] = None


class ImageTypeDef(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    imageId: Optional[ImageIdentifierTypeDef] = None
    imageManifest: Optional[str] = None
    imageManifestMediaType: Optional[str] = None


class ListImagesResponseTypeDef(BaseValidatorModel):
    imageIds: List[ImageIdentifierTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartImageScanRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    registryId: Optional[str] = None


class BlobTypeDef(BaseValidatorModel):
    pass


class UploadLayerPartRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    uploadId: str
    partFirstByte: int
    partLastByte: int
    layerPartBlob: BlobTypeDef
    registryId: Optional[str] = None


class CreateRepositoryCreationTemplateRequestTypeDef(BaseValidatorModel):
    prefix: str
    appliedFor: Sequence[RCTAppliedForType]
    description: Optional[str] = None
    encryptionConfiguration: Optional[ EncryptionConfigurationForRepositoryCreationTemplateTypeDef ] = None
    resourceTags: Optional[Sequence[TagTypeDef]] = None
    imageTagMutability: Optional[ImageTagMutabilityType] = None
    repositoryPolicy: Optional[str] = None
    lifecyclePolicy: Optional[str] = None
    customRoleArn: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RepositoryCreationTemplateTypeDef(BaseValidatorModel):
    prefix: Optional[str] = None
    description: Optional[str] = None
    encryptionConfiguration: Optional[ EncryptionConfigurationForRepositoryCreationTemplateTypeDef ] = None
    resourceTags: Optional[List[TagTypeDef]] = None
    imageTagMutability: Optional[ImageTagMutabilityType] = None
    repositoryPolicy: Optional[str] = None
    lifecyclePolicy: Optional[str] = None
    appliedFor: Optional[List[RCTAppliedForType]] = None
    customRoleArn: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class UpdateRepositoryCreationTemplateRequestTypeDef(BaseValidatorModel):
    prefix: str
    description: Optional[str] = None
    encryptionConfiguration: Optional[ EncryptionConfigurationForRepositoryCreationTemplateTypeDef ] = None
    resourceTags: Optional[Sequence[TagTypeDef]] = None
    imageTagMutability: Optional[ImageTagMutabilityType] = None
    repositoryPolicy: Optional[str] = None
    lifecyclePolicy: Optional[str] = None
    appliedFor: Optional[Sequence[RCTAppliedForType]] = None
    customRoleArn: Optional[str] = None


class CreateRepositoryRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    imageTagMutability: Optional[ImageTagMutabilityType] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationTypeDef] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None


class PutImageScanningConfigurationRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageScanningConfiguration: ImageScanningConfigurationTypeDef
    registryId: Optional[str] = None


class PutImageScanningConfigurationResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    imageScanningConfiguration: ImageScanningConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RepositoryTypeDef(BaseValidatorModel):
    repositoryArn: Optional[str] = None
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    repositoryUri: Optional[str] = None
    createdAt: Optional[datetime] = None
    imageTagMutability: Optional[ImageTagMutabilityType] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationTypeDef] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None


class CvssScoreDetailsTypeDef(BaseValidatorModel):
    adjustments: Optional[List[CvssScoreAdjustmentTypeDef]] = None
    score: Optional[float] = None
    scoreSource: Optional[str] = None
    scoringVector: Optional[str] = None
    version: Optional[str] = None


class DescribeImageReplicationStatusResponseTypeDef(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    replicationStatuses: List[ImageReplicationStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeImageScanFindingsRequestPaginateTypeDef(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    registryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribePullThroughCacheRulesRequestPaginateTypeDef(BaseValidatorModel):
    registryId: Optional[str] = None
    ecrRepositoryPrefixes: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRepositoriesRequestPaginateTypeDef(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRepositoryCreationTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    prefixes: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeImageScanFindingsRequestWaitTypeDef(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    registryId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None


class StartImageScanResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    imageScanStatus: ImageScanStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribePullThroughCacheRulesResponseTypeDef(BaseValidatorModel):
    pullThroughCacheRules: List[PullThroughCacheRuleTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ImageDetailTypeDef(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    imageDigest: Optional[str] = None
    imageTags: Optional[List[str]] = None
    imageSizeInBytes: Optional[int] = None
    imagePushedAt: Optional[datetime] = None
    imageScanStatus: Optional[ImageScanStatusTypeDef] = None
    imageScanFindingsSummary: Optional[ImageScanFindingsSummaryTypeDef] = None
    imageManifestMediaType: Optional[str] = None
    artifactMediaType: Optional[str] = None
    lastRecordedPullTime: Optional[datetime] = None


class LifecyclePolicyRuleActionTypeDef(BaseValidatorModel):
    pass


class LifecyclePolicyPreviewResultTypeDef(BaseValidatorModel):
    imageTags: Optional[List[str]] = None
    imageDigest: Optional[str] = None
    imagePushedAt: Optional[datetime] = None
    action: Optional[LifecyclePolicyRuleActionTypeDef] = None
    appliedRulePriority: Optional[int] = None


class PackageVulnerabilityDetailsTypeDef(BaseValidatorModel):
    cvss: Optional[List[CvssScoreTypeDef]] = None
    referenceUrls: Optional[List[str]] = None
    relatedVulnerabilities: Optional[List[str]] = None
    source: Optional[str] = None
    sourceUrl: Optional[str] = None
    vendorCreatedAt: Optional[datetime] = None
    vendorSeverity: Optional[str] = None
    vendorUpdatedAt: Optional[datetime] = None
    vulnerabilityId: Optional[str] = None
    vulnerablePackages: Optional[List[VulnerablePackageTypeDef]] = None


class RemediationTypeDef(BaseValidatorModel):
    recommendation: Optional[RecommendationTypeDef] = None


class ScanningRepositoryFilterTypeDef(BaseValidatorModel):
    pass


class RegistryScanningRuleOutputTypeDef(BaseValidatorModel):
    scanFrequency: ScanFrequencyType
    repositoryFilters: List[ScanningRepositoryFilterTypeDef]


class RegistryScanningRuleTypeDef(BaseValidatorModel):
    scanFrequency: ScanFrequencyType
    repositoryFilters: Sequence[ScanningRepositoryFilterTypeDef]


class RepositoryScanningConfigurationTypeDef(BaseValidatorModel):
    repositoryArn: Optional[str] = None
    repositoryName: Optional[str] = None
    scanOnPush: Optional[bool] = None
    scanFrequency: Optional[ScanFrequencyType] = None
    appliedScanFilters: Optional[List[ScanningRepositoryFilterTypeDef]] = None


class RepositoryFilterTypeDef(BaseValidatorModel):
    pass


class ReplicationRuleOutputTypeDef(BaseValidatorModel):
    destinations: List[ReplicationDestinationTypeDef]
    repositoryFilters: Optional[List[RepositoryFilterTypeDef]] = None


class ReplicationRuleTypeDef(BaseValidatorModel):
    destinations: Sequence[ReplicationDestinationTypeDef]
    repositoryFilters: Optional[Sequence[RepositoryFilterTypeDef]] = None


class BatchDeleteImageResponseTypeDef(BaseValidatorModel):
    imageIds: List[ImageIdentifierTypeDef]
    failures: List[ImageFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchGetImageResponseTypeDef(BaseValidatorModel):
    images: List[ImageTypeDef]
    failures: List[ImageFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutImageResponseTypeDef(BaseValidatorModel):
    image: ImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRepositoryCreationTemplateResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryCreationTemplate: RepositoryCreationTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRepositoryCreationTemplateResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryCreationTemplate: RepositoryCreationTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRepositoryCreationTemplatesResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryCreationTemplates: List[RepositoryCreationTemplateTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateRepositoryCreationTemplateResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryCreationTemplate: RepositoryCreationTemplateTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRepositoryResponseTypeDef(BaseValidatorModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRepositoryResponseTypeDef(BaseValidatorModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRepositoriesResponseTypeDef(BaseValidatorModel):
    repositories: List[RepositoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ScoreDetailsTypeDef(BaseValidatorModel):
    cvss: Optional[CvssScoreDetailsTypeDef] = None


class DescribeImagesResponseTypeDef(BaseValidatorModel):
    imageDetails: List[ImageDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetLifecyclePolicyPreviewResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    status: LifecyclePolicyPreviewStatusType
    previewResults: List[LifecyclePolicyPreviewResultTypeDef]
    summary: LifecyclePolicyPreviewSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RegistryScanningConfigurationTypeDef(BaseValidatorModel):
    scanType: Optional[ScanTypeType] = None
    rules: Optional[List[RegistryScanningRuleOutputTypeDef]] = None


class BatchGetRepositoryScanningConfigurationResponseTypeDef(BaseValidatorModel):
    scanningConfigurations: List[RepositoryScanningConfigurationTypeDef]
    failures: List[RepositoryScanningConfigurationFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ReplicationConfigurationOutputTypeDef(BaseValidatorModel):
    rules: List[ReplicationRuleOutputTypeDef]


class ReplicationConfigurationTypeDef(BaseValidatorModel):
    rules: Sequence[ReplicationRuleTypeDef]


class GetRegistryScanningConfigurationResponseTypeDef(BaseValidatorModel):
    registryId: str
    scanningConfiguration: RegistryScanningConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutRegistryScanningConfigurationResponseTypeDef(BaseValidatorModel):
    registryScanningConfiguration: RegistryScanningConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RegistryScanningRuleUnionTypeDef(BaseValidatorModel):
    pass


class PutRegistryScanningConfigurationRequestTypeDef(BaseValidatorModel):
    scanType: Optional[ScanTypeType] = None
    rules: Optional[Sequence[RegistryScanningRuleUnionTypeDef]] = None


class DescribeRegistryResponseTypeDef(BaseValidatorModel):
    registryId: str
    replicationConfiguration: ReplicationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutReplicationConfigurationResponseTypeDef(BaseValidatorModel):
    replicationConfiguration: ReplicationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EnhancedImageScanFindingTypeDef(BaseValidatorModel):
    pass


class ImageScanFindingsTypeDef(BaseValidatorModel):
    imageScanCompletedAt: Optional[datetime] = None
    vulnerabilitySourceUpdatedAt: Optional[datetime] = None
    findingSeverityCounts: Optional[Dict[FindingSeverityType, int]] = None
    findings: Optional[List[ImageScanFindingTypeDef]] = None
    enhancedFindings: Optional[List[EnhancedImageScanFindingTypeDef]] = None


class ReplicationConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class PutReplicationConfigurationRequestTypeDef(BaseValidatorModel):
    replicationConfiguration: ReplicationConfigurationUnionTypeDef


class DescribeImageScanFindingsResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    imageScanStatus: ImageScanStatusTypeDef
    imageScanFindings: ImageScanFindingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


