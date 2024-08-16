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

class BatchCheckLayerAvailabilityRequestRequestTypeDef(BaseValidatorModel):
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

class BatchGetRepositoryScanningConfigurationRequestRequestTypeDef(BaseValidatorModel):
    repositoryNames: Sequence[str]

class RepositoryScanningConfigurationFailureTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    failureCode: Optional[Literal["REPOSITORY_NOT_FOUND"]] = None
    failureReason: Optional[str] = None

class CompleteLayerUploadRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    uploadId: str
    layerDigests: Sequence[str]
    registryId: Optional[str] = None

class CreatePullThroughCacheRuleRequestRequestTypeDef(BaseValidatorModel):
    ecrRepositoryPrefix: str
    upstreamRegistryUrl: str
    registryId: Optional[str] = None
    upstreamRegistry: Optional[UpstreamRegistryType] = None
    credentialArn: Optional[str] = None

class EncryptionConfigurationTypeDef(BaseValidatorModel):
    encryptionType: EncryptionTypeType
    kmsKey: Optional[str] = None

class ImageScanningConfigurationTypeDef(BaseValidatorModel):
    scanOnPush: Optional[bool] = None

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class CvssScoreAdjustmentTypeDef(BaseValidatorModel):
    metric: Optional[str] = None
    reason: Optional[str] = None

class CvssScoreTypeDef(BaseValidatorModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None
    source: Optional[str] = None
    version: Optional[str] = None

class DeleteLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None

class DeletePullThroughCacheRuleRequestRequestTypeDef(BaseValidatorModel):
    ecrRepositoryPrefix: str
    registryId: Optional[str] = None

class DeleteRepositoryPolicyRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None

class DeleteRepositoryRequestRequestTypeDef(BaseValidatorModel):
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

class DescribePullThroughCacheRulesRequestRequestTypeDef(BaseValidatorModel):
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

class DescribeRepositoriesRequestRequestTypeDef(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetAuthorizationTokenRequestRequestTypeDef(BaseValidatorModel):
    registryIds: Optional[Sequence[str]] = None

class GetDownloadUrlForLayerRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    layerDigest: str
    registryId: Optional[str] = None

class LifecyclePolicyPreviewFilterTypeDef(BaseValidatorModel):
    tagStatus: Optional[TagStatusType] = None

class LifecyclePolicyPreviewSummaryTypeDef(BaseValidatorModel):
    expiringImageTotalCount: Optional[int] = None

class GetLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None

class GetRepositoryPolicyRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None

class ImageScanFindingsSummaryTypeDef(BaseValidatorModel):
    imageScanCompletedAt: Optional[datetime] = None
    vulnerabilitySourceUpdatedAt: Optional[datetime] = None
    findingSeverityCounts: Optional[Dict[FindingSeverityType, int]] = None

class InitiateLayerUploadRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None

class LifecyclePolicyRuleActionTypeDef(BaseValidatorModel):
    type: Optional[Literal["EXPIRE"]] = None

class ListImagesFilterTypeDef(BaseValidatorModel):
    tagStatus: Optional[TagStatusType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
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

class PutImageRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageManifest: str
    registryId: Optional[str] = None
    imageManifestMediaType: Optional[str] = None
    imageTag: Optional[str] = None
    imageDigest: Optional[str] = None

class PutImageTagMutabilityRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageTagMutability: ImageTagMutabilityType
    registryId: Optional[str] = None

class PutLifecyclePolicyRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    lifecyclePolicyText: str
    registryId: Optional[str] = None

class PutRegistryPolicyRequestRequestTypeDef(BaseValidatorModel):
    policyText: str

class RecommendationTypeDef(BaseValidatorModel):
    url: Optional[str] = None
    text: Optional[str] = None

class ScanningRepositoryFilterTypeDef(BaseValidatorModel):
    filter: str
    filterType: Literal["WILDCARD"]

class ReplicationDestinationTypeDef(BaseValidatorModel):
    region: str
    registryId: str

class RepositoryFilterTypeDef(BaseValidatorModel):
    filter: str
    filterType: Literal["PREFIX_MATCH"]

class SetRepositoryPolicyRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    policyText: str
    registryId: Optional[str] = None
    force: Optional[bool] = None

class StartLifecyclePolicyPreviewRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    lifecyclePolicyText: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdatePullThroughCacheRuleRequestRequestTypeDef(BaseValidatorModel):
    ecrRepositoryPrefix: str
    credentialArn: str
    registryId: Optional[str] = None

class ValidatePullThroughCacheRuleRequestRequestTypeDef(BaseValidatorModel):
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

class BatchDeleteImageRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageIds: Sequence[ImageIdentifierTypeDef]
    registryId: Optional[str] = None

class BatchGetImageRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageIds: Sequence[ImageIdentifierTypeDef]
    registryId: Optional[str] = None
    acceptedMediaTypes: Optional[Sequence[str]] = None

class DescribeImageReplicationStatusRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    registryId: Optional[str] = None

class DescribeImageScanFindingsRequestRequestTypeDef(BaseValidatorModel):
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
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartImageScanRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    registryId: Optional[str] = None

class UploadLayerPartRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    uploadId: str
    partFirstByte: int
    partLastByte: int
    layerPartBlob: BlobTypeDef
    registryId: Optional[str] = None

class PutImageScanningConfigurationRequestRequestTypeDef(BaseValidatorModel):
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

class CreateRepositoryRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    imageTagMutability: Optional[ImageTagMutabilityType] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationTypeDef] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

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

class DescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef(BaseValidatorModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    registryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePullThroughCacheRulesRequestDescribePullThroughCacheRulesPaginateTypeDef(BaseValidatorModel):
    registryId: Optional[str] = None
    ecrRepositoryPrefixes: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef(BaseValidatorModel):
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

class DescribeImagesRequestDescribeImagesPaginateTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
    filter: Optional[DescribeImagesFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImagesRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[DescribeImagesFilterTypeDef] = None

class DescribePullThroughCacheRulesResponseTypeDef(BaseValidatorModel):
    pullThroughCacheRules: List[PullThroughCacheRuleTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
    filter: Optional[LifecyclePolicyPreviewFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[LifecyclePolicyPreviewFilterTypeDef] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetLifecyclePolicyPreviewRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[LifecyclePolicyPreviewFilterTypeDef] = None

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

class LifecyclePolicyPreviewResultTypeDef(BaseValidatorModel):
    imageTags: Optional[List[str]] = None
    imageDigest: Optional[str] = None
    imagePushedAt: Optional[datetime] = None
    action: Optional[LifecyclePolicyRuleActionTypeDef] = None
    appliedRulePriority: Optional[int] = None

class ListImagesRequestListImagesPaginateTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    filter: Optional[ListImagesFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImagesRequestRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ListImagesFilterTypeDef] = None

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

class ReplicationRuleOutputTypeDef(BaseValidatorModel):
    destinations: List[ReplicationDestinationTypeDef]
    repositoryFilters: Optional[List[RepositoryFilterTypeDef]] = None

class ReplicationRuleTypeDef(BaseValidatorModel):
    destinations: Sequence[ReplicationDestinationTypeDef]
    repositoryFilters: Optional[Sequence[RepositoryFilterTypeDef]] = None

class ResourceTypeDef(BaseValidatorModel):
    details: Optional[ResourceDetailsTypeDef] = None
    id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[str] = None

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

class CreateRepositoryResponseTypeDef(BaseValidatorModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryResponseTypeDef(BaseValidatorModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRepositoriesResponseTypeDef(BaseValidatorModel):
    repositories: List[RepositoryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ScoreDetailsTypeDef(BaseValidatorModel):
    cvss: Optional[CvssScoreDetailsTypeDef] = None

class DescribeImagesResponseTypeDef(BaseValidatorModel):
    imageDetails: List[ImageDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLifecyclePolicyPreviewResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    status: LifecyclePolicyPreviewStatusType
    nextToken: str
    previewResults: List[LifecyclePolicyPreviewResultTypeDef]
    summary: LifecyclePolicyPreviewSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

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

class EnhancedImageScanFindingTypeDef(BaseValidatorModel):
    awsAccountId: Optional[str] = None
    description: Optional[str] = None
    findingArn: Optional[str] = None
    firstObservedAt: Optional[datetime] = None
    lastObservedAt: Optional[datetime] = None
    packageVulnerabilityDetails: Optional[PackageVulnerabilityDetailsTypeDef] = None
    remediation: Optional[RemediationTypeDef] = None
    resources: Optional[List[ResourceTypeDef]] = None
    score: Optional[float] = None
    scoreDetails: Optional[ScoreDetailsTypeDef] = None
    severity: Optional[str] = None
    status: Optional[str] = None
    title: Optional[str] = None
    type: Optional[str] = None
    updatedAt: Optional[datetime] = None

class GetRegistryScanningConfigurationResponseTypeDef(BaseValidatorModel):
    registryId: str
    scanningConfiguration: RegistryScanningConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutRegistryScanningConfigurationResponseTypeDef(BaseValidatorModel):
    registryScanningConfiguration: RegistryScanningConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutRegistryScanningConfigurationRequestRequestTypeDef(BaseValidatorModel):
    scanType: Optional[ScanTypeType] = None
    rules: Optional[Sequence[RegistryScanningRuleUnionTypeDef]] = None

class DescribeRegistryResponseTypeDef(BaseValidatorModel):
    registryId: str
    replicationConfiguration: ReplicationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutReplicationConfigurationResponseTypeDef(BaseValidatorModel):
    replicationConfiguration: ReplicationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutReplicationConfigurationRequestRequestTypeDef(BaseValidatorModel):
    replicationConfiguration: ReplicationConfigurationTypeDef

class ImageScanFindingsTypeDef(BaseValidatorModel):
    imageScanCompletedAt: Optional[datetime] = None
    vulnerabilitySourceUpdatedAt: Optional[datetime] = None
    findingSeverityCounts: Optional[Dict[FindingSeverityType, int]] = None
    findings: Optional[List[ImageScanFindingTypeDef]] = None
    enhancedFindings: Optional[List[EnhancedImageScanFindingTypeDef]] = None

class DescribeImageScanFindingsResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    imageScanStatus: ImageScanStatusTypeDef
    imageScanFindings: ImageScanFindingsTypeDef
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

