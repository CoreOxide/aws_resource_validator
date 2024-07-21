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
from aws_resource_validator.pydantic_models.ecr_constants import *

class AttributeTypeDef(BaseModel):
    key: str
    value: Optional[str] = None

class AuthorizationDataTypeDef(BaseModel):
    authorizationToken: Optional[str] = None
    expiresAt: Optional[datetime] = None
    proxyEndpoint: Optional[str] = None

class AwsEcrContainerImageDetailsTypeDef(BaseModel):
    architecture: Optional[str] = None
    author: Optional[str] = None
    imageHash: Optional[str] = None
    imageTags: Optional[List[str]] = None
    platform: Optional[str] = None
    pushedAt: Optional[datetime] = None
    registry: Optional[str] = None
    repositoryName: Optional[str] = None

class BatchCheckLayerAvailabilityRequestRequestTypeDef(BaseModel):
    repositoryName: str
    layerDigests: Sequence[str]
    registryId: Optional[str] = None

class LayerFailureTypeDef(BaseModel):
    layerDigest: Optional[str] = None
    failureCode: Optional[LayerFailureCodeType] = None
    failureReason: Optional[str] = None

class LayerTypeDef(BaseModel):
    layerDigest: Optional[str] = None
    layerAvailability: Optional[LayerAvailabilityType] = None
    layerSize: Optional[int] = None
    mediaType: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class ImageIdentifierTypeDef(BaseModel):
    imageDigest: Optional[str] = None
    imageTag: Optional[str] = None

class BatchGetRepositoryScanningConfigurationRequestRequestTypeDef(BaseModel):
    repositoryNames: Sequence[str]

class RepositoryScanningConfigurationFailureTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    failureCode: Optional[Literal["REPOSITORY_NOT_FOUND"]] = None
    failureReason: Optional[str] = None

class CompleteLayerUploadRequestRequestTypeDef(BaseModel):
    repositoryName: str
    uploadId: str
    layerDigests: Sequence[str]
    registryId: Optional[str] = None

class CreatePullThroughCacheRuleRequestRequestTypeDef(BaseModel):
    ecrRepositoryPrefix: str
    upstreamRegistryUrl: str
    registryId: Optional[str] = None
    upstreamRegistry: Optional[UpstreamRegistryType] = None
    credentialArn: Optional[str] = None

class EncryptionConfigurationTypeDef(BaseModel):
    encryptionType: EncryptionTypeType
    kmsKey: Optional[str] = None

class ImageScanningConfigurationTypeDef(BaseModel):
    scanOnPush: Optional[bool] = None

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CvssScoreAdjustmentTypeDef(BaseModel):
    metric: Optional[str] = None
    reason: Optional[str] = None

class CvssScoreTypeDef(BaseModel):
    baseScore: Optional[float] = None
    scoringVector: Optional[str] = None
    source: Optional[str] = None
    version: Optional[str] = None

class DeleteLifecyclePolicyRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None

class DeletePullThroughCacheRuleRequestRequestTypeDef(BaseModel):
    ecrRepositoryPrefix: str
    registryId: Optional[str] = None

class DeleteRepositoryPolicyRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None

class DeleteRepositoryRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    force: Optional[bool] = None

class ImageReplicationStatusTypeDef(BaseModel):
    region: Optional[str] = None
    registryId: Optional[str] = None
    status: Optional[ReplicationStatusType] = None
    failureCode: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class WaiterConfigTypeDef(BaseModel):
    Delay: Optional[int] = None
    MaxAttempts: Optional[int] = None

class ImageScanStatusTypeDef(BaseModel):
    status: Optional[ScanStatusType] = None
    description: Optional[str] = None

class DescribeImagesFilterTypeDef(BaseModel):
    tagStatus: Optional[TagStatusType] = None

class DescribePullThroughCacheRulesRequestRequestTypeDef(BaseModel):
    registryId: Optional[str] = None
    ecrRepositoryPrefixes: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PullThroughCacheRuleTypeDef(BaseModel):
    ecrRepositoryPrefix: Optional[str] = None
    upstreamRegistryUrl: Optional[str] = None
    createdAt: Optional[datetime] = None
    registryId: Optional[str] = None
    credentialArn: Optional[str] = None
    upstreamRegistry: Optional[UpstreamRegistryType] = None
    updatedAt: Optional[datetime] = None

class DescribeRepositoriesRequestRequestTypeDef(BaseModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class GetAuthorizationTokenRequestRequestTypeDef(BaseModel):
    registryIds: Optional[Sequence[str]] = None

class GetDownloadUrlForLayerRequestRequestTypeDef(BaseModel):
    repositoryName: str
    layerDigest: str
    registryId: Optional[str] = None

class LifecyclePolicyPreviewFilterTypeDef(BaseModel):
    tagStatus: Optional[TagStatusType] = None

class LifecyclePolicyPreviewSummaryTypeDef(BaseModel):
    expiringImageTotalCount: Optional[int] = None

class GetLifecyclePolicyRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None

class GetRepositoryPolicyRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None

class ImageScanFindingsSummaryTypeDef(BaseModel):
    imageScanCompletedAt: Optional[datetime] = None
    vulnerabilitySourceUpdatedAt: Optional[datetime] = None
    findingSeverityCounts: Optional[Dict[FindingSeverityType, int]] = None

class InitiateLayerUploadRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None

class LifecyclePolicyRuleActionTypeDef(BaseModel):
    type: Optional[Literal["EXPIRE"]] = None

class ListImagesFilterTypeDef(BaseModel):
    tagStatus: Optional[TagStatusType] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class VulnerablePackageTypeDef(BaseModel):
    arch: Optional[str] = None
    epoch: Optional[int] = None
    filePath: Optional[str] = None
    name: Optional[str] = None
    packageManager: Optional[str] = None
    release: Optional[str] = None
    sourceLayerHash: Optional[str] = None
    version: Optional[str] = None

class PutImageRequestRequestTypeDef(BaseModel):
    repositoryName: str
    imageManifest: str
    registryId: Optional[str] = None
    imageManifestMediaType: Optional[str] = None
    imageTag: Optional[str] = None
    imageDigest: Optional[str] = None

class PutImageTagMutabilityRequestRequestTypeDef(BaseModel):
    repositoryName: str
    imageTagMutability: ImageTagMutabilityType
    registryId: Optional[str] = None

class PutLifecyclePolicyRequestRequestTypeDef(BaseModel):
    repositoryName: str
    lifecyclePolicyText: str
    registryId: Optional[str] = None

class PutRegistryPolicyRequestRequestTypeDef(BaseModel):
    policyText: str

class RecommendationTypeDef(BaseModel):
    url: Optional[str] = None
    text: Optional[str] = None

class ScanningRepositoryFilterTypeDef(BaseModel):
    filter: str
    filterType: Literal["WILDCARD"]

class ReplicationDestinationTypeDef(BaseModel):
    region: str
    registryId: str

class RepositoryFilterTypeDef(BaseModel):
    filter: str
    filterType: Literal["PREFIX_MATCH"]

class SetRepositoryPolicyRequestRequestTypeDef(BaseModel):
    repositoryName: str
    policyText: str
    registryId: Optional[str] = None
    force: Optional[bool] = None

class StartLifecyclePolicyPreviewRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    lifecyclePolicyText: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdatePullThroughCacheRuleRequestRequestTypeDef(BaseModel):
    ecrRepositoryPrefix: str
    credentialArn: str
    registryId: Optional[str] = None

class ValidatePullThroughCacheRuleRequestRequestTypeDef(BaseModel):
    ecrRepositoryPrefix: str
    registryId: Optional[str] = None

class ImageScanFindingTypeDef(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    uri: Optional[str] = None
    severity: Optional[FindingSeverityType] = None
    attributes: Optional[List[AttributeTypeDef]] = None

class ResourceDetailsTypeDef(BaseModel):
    awsEcrContainerImage: Optional[AwsEcrContainerImageDetailsTypeDef] = None

class BatchCheckLayerAvailabilityResponseTypeDef(BaseModel):
    layers: List[LayerTypeDef]
    failures: List[LayerFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CompleteLayerUploadResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    uploadId: str
    layerDigest: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePullThroughCacheRuleResponseTypeDef(BaseModel):
    ecrRepositoryPrefix: str
    upstreamRegistryUrl: str
    createdAt: datetime
    registryId: str
    upstreamRegistry: UpstreamRegistryType
    credentialArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteLifecyclePolicyResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    lastEvaluatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePullThroughCacheRuleResponseTypeDef(BaseModel):
    ecrRepositoryPrefix: str
    upstreamRegistryUrl: str
    createdAt: datetime
    registryId: str
    credentialArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRegistryPolicyResponseTypeDef(BaseModel):
    registryId: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryPolicyResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAuthorizationTokenResponseTypeDef(BaseModel):
    authorizationData: List[AuthorizationDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetDownloadUrlForLayerResponseTypeDef(BaseModel):
    downloadUrl: str
    layerDigest: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLifecyclePolicyResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    lastEvaluatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegistryPolicyResponseTypeDef(BaseModel):
    registryId: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryPolicyResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class InitiateLayerUploadResponseTypeDef(BaseModel):
    uploadId: str
    partSize: int
    ResponseMetadata: ResponseMetadataTypeDef

class PutImageTagMutabilityResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    imageTagMutability: ImageTagMutabilityType
    ResponseMetadata: ResponseMetadataTypeDef

class PutLifecyclePolicyResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class PutRegistryPolicyResponseTypeDef(BaseModel):
    registryId: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetRepositoryPolicyResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartLifecyclePolicyPreviewResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    status: LifecyclePolicyPreviewStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePullThroughCacheRuleResponseTypeDef(BaseModel):
    ecrRepositoryPrefix: str
    registryId: str
    updatedAt: datetime
    credentialArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UploadLayerPartResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    uploadId: str
    lastByteReceived: int
    ResponseMetadata: ResponseMetadataTypeDef

class ValidatePullThroughCacheRuleResponseTypeDef(BaseModel):
    ecrRepositoryPrefix: str
    registryId: str
    upstreamRegistryUrl: str
    credentialArn: str
    isValid: bool
    failure: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteImageRequestRequestTypeDef(BaseModel):
    repositoryName: str
    imageIds: Sequence[ImageIdentifierTypeDef]
    registryId: Optional[str] = None

class BatchGetImageRequestRequestTypeDef(BaseModel):
    repositoryName: str
    imageIds: Sequence[ImageIdentifierTypeDef]
    registryId: Optional[str] = None
    acceptedMediaTypes: Optional[Sequence[str]] = None

class DescribeImageReplicationStatusRequestRequestTypeDef(BaseModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    registryId: Optional[str] = None

class DescribeImageScanFindingsRequestRequestTypeDef(BaseModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    registryId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ImageFailureTypeDef(BaseModel):
    imageId: Optional[ImageIdentifierTypeDef] = None
    failureCode: Optional[ImageFailureCodeType] = None
    failureReason: Optional[str] = None

class ImageTypeDef(BaseModel):
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    imageId: Optional[ImageIdentifierTypeDef] = None
    imageManifest: Optional[str] = None
    imageManifestMediaType: Optional[str] = None

class ListImagesResponseTypeDef(BaseModel):
    imageIds: List[ImageIdentifierTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartImageScanRequestRequestTypeDef(BaseModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    registryId: Optional[str] = None

class UploadLayerPartRequestRequestTypeDef(BaseModel):
    repositoryName: str
    uploadId: str
    partFirstByte: int
    partLastByte: int
    layerPartBlob: BlobTypeDef
    registryId: Optional[str] = None

class PutImageScanningConfigurationRequestRequestTypeDef(BaseModel):
    repositoryName: str
    imageScanningConfiguration: ImageScanningConfigurationTypeDef
    registryId: Optional[str] = None

class PutImageScanningConfigurationResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    imageScanningConfiguration: ImageScanningConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RepositoryTypeDef(BaseModel):
    repositoryArn: Optional[str] = None
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    repositoryUri: Optional[str] = None
    createdAt: Optional[datetime] = None
    imageTagMutability: Optional[ImageTagMutabilityType] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationTypeDef] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class CreateRepositoryRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    imageTagMutability: Optional[ImageTagMutabilityType] = None
    imageScanningConfiguration: Optional[ImageScanningConfigurationTypeDef] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CvssScoreDetailsTypeDef(BaseModel):
    adjustments: Optional[List[CvssScoreAdjustmentTypeDef]] = None
    score: Optional[float] = None
    scoreSource: Optional[str] = None
    scoringVector: Optional[str] = None
    version: Optional[str] = None

class DescribeImageReplicationStatusResponseTypeDef(BaseModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    replicationStatuses: List[ImageReplicationStatusTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef(BaseModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    registryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribePullThroughCacheRulesRequestDescribePullThroughCacheRulesPaginateTypeDef(BaseModel):
    registryId: Optional[str] = None
    ecrRepositoryPrefixes: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef(BaseModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef(BaseModel):
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    registryId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class StartImageScanResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    imageScanStatus: ImageScanStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImagesRequestDescribeImagesPaginateTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
    filter: Optional[DescribeImagesFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImagesRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[DescribeImagesFilterTypeDef] = None

class DescribePullThroughCacheRulesResponseTypeDef(BaseModel):
    pullThroughCacheRules: List[PullThroughCacheRuleTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
    filter: Optional[LifecyclePolicyPreviewFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[LifecyclePolicyPreviewFilterTypeDef] = None
    WaiterConfig: Optional[WaiterConfigTypeDef] = None

class GetLifecyclePolicyPreviewRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[LifecyclePolicyPreviewFilterTypeDef] = None

class ImageDetailTypeDef(BaseModel):
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

class LifecyclePolicyPreviewResultTypeDef(BaseModel):
    imageTags: Optional[List[str]] = None
    imageDigest: Optional[str] = None
    imagePushedAt: Optional[datetime] = None
    action: Optional[LifecyclePolicyRuleActionTypeDef] = None
    appliedRulePriority: Optional[int] = None

class ListImagesRequestListImagesPaginateTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    filter: Optional[ListImagesFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImagesRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filter: Optional[ListImagesFilterTypeDef] = None

class PackageVulnerabilityDetailsTypeDef(BaseModel):
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

class RemediationTypeDef(BaseModel):
    recommendation: Optional[RecommendationTypeDef] = None

class RegistryScanningRuleOutputTypeDef(BaseModel):
    scanFrequency: ScanFrequencyType
    repositoryFilters: List[ScanningRepositoryFilterTypeDef]

class RegistryScanningRuleTypeDef(BaseModel):
    scanFrequency: ScanFrequencyType
    repositoryFilters: Sequence[ScanningRepositoryFilterTypeDef]

class RepositoryScanningConfigurationTypeDef(BaseModel):
    repositoryArn: Optional[str] = None
    repositoryName: Optional[str] = None
    scanOnPush: Optional[bool] = None
    scanFrequency: Optional[ScanFrequencyType] = None
    appliedScanFilters: Optional[List[ScanningRepositoryFilterTypeDef]] = None

class ReplicationRuleOutputTypeDef(BaseModel):
    destinations: List[ReplicationDestinationTypeDef]
    repositoryFilters: Optional[List[RepositoryFilterTypeDef]] = None

class ReplicationRuleTypeDef(BaseModel):
    destinations: Sequence[ReplicationDestinationTypeDef]
    repositoryFilters: Optional[Sequence[RepositoryFilterTypeDef]] = None

class ResourceTypeDef(BaseModel):
    details: Optional[ResourceDetailsTypeDef] = None
    id: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[str] = None

class BatchDeleteImageResponseTypeDef(BaseModel):
    imageIds: List[ImageIdentifierTypeDef]
    failures: List[ImageFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetImageResponseTypeDef(BaseModel):
    images: List[ImageTypeDef]
    failures: List[ImageFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutImageResponseTypeDef(BaseModel):
    image: ImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryResponseTypeDef(BaseModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryResponseTypeDef(BaseModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRepositoriesResponseTypeDef(BaseModel):
    repositories: List[RepositoryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ScoreDetailsTypeDef(BaseModel):
    cvss: Optional[CvssScoreDetailsTypeDef] = None

class DescribeImagesResponseTypeDef(BaseModel):
    imageDetails: List[ImageDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetLifecyclePolicyPreviewResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    lifecyclePolicyText: str
    status: LifecyclePolicyPreviewStatusType
    nextToken: str
    previewResults: List[LifecyclePolicyPreviewResultTypeDef]
    summary: LifecyclePolicyPreviewSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RegistryScanningConfigurationTypeDef(BaseModel):
    scanType: Optional[ScanTypeType] = None
    rules: Optional[List[RegistryScanningRuleOutputTypeDef]] = None

class BatchGetRepositoryScanningConfigurationResponseTypeDef(BaseModel):
    scanningConfigurations: List[RepositoryScanningConfigurationTypeDef]
    failures: List[RepositoryScanningConfigurationFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationConfigurationOutputTypeDef(BaseModel):
    rules: List[ReplicationRuleOutputTypeDef]

class ReplicationConfigurationTypeDef(BaseModel):
    rules: Sequence[ReplicationRuleTypeDef]

class EnhancedImageScanFindingTypeDef(BaseModel):
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

class GetRegistryScanningConfigurationResponseTypeDef(BaseModel):
    registryId: str
    scanningConfiguration: RegistryScanningConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutRegistryScanningConfigurationResponseTypeDef(BaseModel):
    registryScanningConfiguration: RegistryScanningConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutRegistryScanningConfigurationRequestRequestTypeDef(BaseModel):
    scanType: Optional[ScanTypeType] = None
    rules: Optional[Sequence[RegistryScanningRuleUnionTypeDef]] = None

class DescribeRegistryResponseTypeDef(BaseModel):
    registryId: str
    replicationConfiguration: ReplicationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutReplicationConfigurationResponseTypeDef(BaseModel):
    replicationConfiguration: ReplicationConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutReplicationConfigurationRequestRequestTypeDef(BaseModel):
    replicationConfiguration: ReplicationConfigurationTypeDef

class ImageScanFindingsTypeDef(BaseModel):
    imageScanCompletedAt: Optional[datetime] = None
    vulnerabilitySourceUpdatedAt: Optional[datetime] = None
    findingSeverityCounts: Optional[Dict[FindingSeverityType, int]] = None
    findings: Optional[List[ImageScanFindingTypeDef]] = None
    enhancedFindings: Optional[List[EnhancedImageScanFindingTypeDef]] = None

class DescribeImageScanFindingsResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    imageId: ImageIdentifierTypeDef
    imageScanStatus: ImageScanStatusTypeDef
    imageScanFindings: ImageScanFindingsTypeDef
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

