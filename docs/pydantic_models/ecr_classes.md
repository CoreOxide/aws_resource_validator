# Pydantic Models in ecr_classes

# AttributeTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# AuthorizationDataTypeDef

### authorizationToken
- **Type**: typing.Optional[str]

### expiresAt
- **Type**: typing.Optional[datetime.datetime]

### proxyEndpoint
- **Type**: typing.Optional[str]


# AwsEcrContainerImageDetailsTypeDef

### architecture
- **Type**: typing.Optional[str]

### author
- **Type**: typing.Optional[str]

### imageHash
- **Type**: typing.Optional[str]

### imageTags
- **Type**: typing.Optional[typing.List[str]]

### platform
- **Type**: typing.Optional[str]

### pushedAt
- **Type**: typing.Optional[datetime.datetime]

### registry
- **Type**: typing.Optional[str]

### repositoryName
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCheckLayerAvailabilityRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### layerDigests
- **Type**: typing.Sequence[str]
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# BatchCheckLayerAvailabilityResponseTypeDef

### layers
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.LayerTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.LayerFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeleteImageRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageIds
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef]
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# BatchDeleteImageResponseTypeDef

### imageIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.ImageFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetImageRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageIds
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef]
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### acceptedMediaTypes
- **Type**: typing.Optional[typing.Sequence[str]]


# BatchGetImageResponseTypeDef

### images
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.ImageTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.ImageFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetRepositoryScanningConfigurationRequestRequestTypeDef

### repositoryNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetRepositoryScanningConfigurationResponseTypeDef

### scanningConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.RepositoryScanningConfigurationTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.RepositoryScanningConfigurationFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CompleteLayerUploadRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### layerDigests
- **Type**: typing.Sequence[str]
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# CompleteLayerUploadResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### layerDigest
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePullThroughCacheRuleRequestRequestTypeDef

### ecrRepositoryPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### upstreamRegistryUrl
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### upstreamRegistry
- **Type**: typing.Optional[typing.Literal['azure-container-registry', 'docker-hub', 'ecr-public', 'github-container-registry', 'gitlab-container-registry', 'k8s', 'quay']]

### credentialArn
- **Type**: typing.Optional[str]


# CreatePullThroughCacheRuleResponseTypeDef

### ecrRepositoryPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### upstreamRegistryUrl
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### upstreamRegistry
- **Type**: typing.Literal['azure-container-registry', 'docker-hub', 'ecr-public', 'github-container-registry', 'gitlab-container-registry', 'k8s', 'quay']
- **Required**: Yes

### credentialArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRepositoryRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecr_classes.TagTypeDef]]

### imageTagMutability
- **Type**: typing.Optional[typing.Literal['IMMUTABLE', 'MUTABLE']]

### imageScanningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.ImageScanningConfigurationTypeDef]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.EncryptionConfigurationTypeDef]


# CreateRepositoryResponseTypeDef

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.RepositoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CvssScoreAdjustmentTypeDef

### metric
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# CvssScoreDetailsTypeDef

### adjustments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr_classes.CvssScoreAdjustmentTypeDef]]

### score
- **Type**: typing.Optional[float]

### scoreSource
- **Type**: typing.Optional[str]

### scoringVector
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# CvssScoreTypeDef

### baseScore
- **Type**: typing.Optional[float]

### scoringVector
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# DeleteLifecyclePolicyRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# DeleteLifecyclePolicyResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### lifecyclePolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### lastEvaluatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePullThroughCacheRuleRequestRequestTypeDef

### ecrRepositoryPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# DeletePullThroughCacheRuleResponseTypeDef

### ecrRepositoryPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### upstreamRegistryUrl
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### credentialArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRegistryPolicyResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### policyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRepositoryPolicyRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# DeleteRepositoryPolicyResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### policyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRepositoryRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### force
- **Type**: typing.Optional[bool]


# DeleteRepositoryResponseTypeDef

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.RepositoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImageReplicationStatusRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# DescribeImageReplicationStatusResponseTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef'>
- **Required**: Yes

### replicationStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.ImageReplicationStatusTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImageScanFindingsRequestDescribeImageScanFindingsPaginateTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.PaginatorConfigTypeDef]


# DescribeImageScanFindingsRequestImageScanCompleteWaitTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.WaiterConfigTypeDef]


# DescribeImageScanFindingsRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeImageScanFindingsResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef'>
- **Required**: Yes

### imageScanStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageScanStatusTypeDef'>
- **Required**: Yes

### imageScanFindings
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageScanFindingsTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImagesFilterTypeDef

### tagStatus
- **Type**: typing.Optional[typing.Literal['ANY', 'TAGGED', 'UNTAGGED']]


# DescribeImagesRequestDescribeImagesPaginateTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.DescribeImagesFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.PaginatorConfigTypeDef]


# DescribeImagesRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.DescribeImagesFilterTypeDef]


# DescribeImagesResponseTypeDef

### imageDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.ImageDetailTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePullThroughCacheRulesRequestDescribePullThroughCacheRulesPaginateTypeDef

### registryId
- **Type**: typing.Optional[str]

### ecrRepositoryPrefixes
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.PaginatorConfigTypeDef]


# DescribePullThroughCacheRulesRequestRequestTypeDef

### registryId
- **Type**: typing.Optional[str]

### ecrRepositoryPrefixes
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribePullThroughCacheRulesResponseTypeDef

### pullThroughCacheRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.PullThroughCacheRuleTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRegistryResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### replicationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ReplicationConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef

### registryId
- **Type**: typing.Optional[str]

### repositoryNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.PaginatorConfigTypeDef]


# DescribeRepositoriesRequestRequestTypeDef

### registryId
- **Type**: typing.Optional[str]

### repositoryNames
- **Type**: typing.Optional[typing.Sequence[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeRepositoriesResponseTypeDef

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.RepositoryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionConfigurationTypeDef

### encryptionType
- **Type**: typing.Literal['AES256', 'KMS']
- **Required**: Yes

### kmsKey
- **Type**: typing.Optional[str]


# EnhancedImageScanFindingTypeDef

### awsAccountId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### findingArn
- **Type**: typing.Optional[str]

### firstObservedAt
- **Type**: typing.Optional[datetime.datetime]

### lastObservedAt
- **Type**: typing.Optional[datetime.datetime]

### packageVulnerabilityDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.PackageVulnerabilityDetailsTypeDef]

### remediation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.RemediationTypeDef]

### resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr_classes.ResourceTypeDef]]

### score
- **Type**: typing.Optional[float]

### scoreDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.ScoreDetailsTypeDef]

### severity
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# GetAuthorizationTokenRequestRequestTypeDef

### registryIds
- **Type**: typing.Optional[typing.Sequence[str]]


# GetAuthorizationTokenResponseTypeDef

### authorizationData
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.AuthorizationDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDownloadUrlForLayerRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### layerDigest
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# GetDownloadUrlForLayerResponseTypeDef

### downloadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### layerDigest
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLifecyclePolicyPreviewRequestGetLifecyclePolicyPreviewPaginateTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.LifecyclePolicyPreviewFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.PaginatorConfigTypeDef]


# GetLifecyclePolicyPreviewRequestLifecyclePolicyPreviewCompleteWaitTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.LifecyclePolicyPreviewFilterTypeDef]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.WaiterConfigTypeDef]


# GetLifecyclePolicyPreviewRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.LifecyclePolicyPreviewFilterTypeDef]


# GetLifecyclePolicyPreviewResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### lifecyclePolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETE', 'EXPIRED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### previewResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.LifecyclePolicyPreviewResultTypeDef]
- **Required**: Yes

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.LifecyclePolicyPreviewSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLifecyclePolicyRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# GetLifecyclePolicyResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### lifecyclePolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### lastEvaluatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRegistryPolicyResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### policyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRegistryScanningConfigurationResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### scanningConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.RegistryScanningConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRepositoryPolicyRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# GetRepositoryPolicyResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### policyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImageDetailTypeDef

### registryId
- **Type**: typing.Optional[str]

### repositoryName
- **Type**: typing.Optional[str]

### imageDigest
- **Type**: typing.Optional[str]

### imageTags
- **Type**: typing.Optional[typing.List[str]]

### imageSizeInBytes
- **Type**: typing.Optional[int]

### imagePushedAt
- **Type**: typing.Optional[datetime.datetime]

### imageScanStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.ImageScanStatusTypeDef]

### imageScanFindingsSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.ImageScanFindingsSummaryTypeDef]

### imageManifestMediaType
- **Type**: typing.Optional[str]

### artifactMediaType
- **Type**: typing.Optional[str]

### lastRecordedPullTime
- **Type**: typing.Optional[datetime.datetime]


# ImageFailureTypeDef

### imageId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef]

### failureCode
- **Type**: typing.Optional[typing.Literal['ImageNotFound', 'ImageReferencedByManifestList', 'ImageTagDoesNotMatchDigest', 'InvalidImageDigest', 'InvalidImageTag', 'KmsError', 'MissingDigestAndTag', 'UpstreamAccessDenied', 'UpstreamTooManyRequests', 'UpstreamUnavailable']]

### failureReason
- **Type**: typing.Optional[str]


# ImageIdentifierTypeDef

### imageDigest
- **Type**: typing.Optional[str]

### imageTag
- **Type**: typing.Optional[str]


# ImageReplicationStatusTypeDef

### region
- **Type**: typing.Optional[str]

### registryId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']]

### failureCode
- **Type**: typing.Optional[str]


# ImageScanFindingTypeDef

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### uri
- **Type**: typing.Optional[str]

### severity
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNDEFINED']]

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr_classes.AttributeTypeDef]]


# ImageScanFindingsSummaryTypeDef

### imageScanCompletedAt
- **Type**: typing.Optional[datetime.datetime]

### vulnerabilitySourceUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### findingSeverityCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNDEFINED'], int]]


# ImageScanFindingsTypeDef

### imageScanCompletedAt
- **Type**: typing.Optional[datetime.datetime]

### vulnerabilitySourceUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### findingSeverityCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNDEFINED'], int]]

### findings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr_classes.ImageScanFindingTypeDef]]

### enhancedFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr_classes.EnhancedImageScanFindingTypeDef]]


# ImageScanStatusTypeDef

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COMPLETE', 'FAILED', 'FINDINGS_UNAVAILABLE', 'IN_PROGRESS', 'PENDING', 'SCAN_ELIGIBILITY_EXPIRED', 'UNSUPPORTED_IMAGE']]

### description
- **Type**: typing.Optional[str]


# ImageScanningConfigurationTypeDef

### scanOnPush
- **Type**: typing.Optional[bool]


# ImageTypeDef

### registryId
- **Type**: typing.Optional[str]

### repositoryName
- **Type**: typing.Optional[str]

### imageId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef]

### imageManifest
- **Type**: typing.Optional[str]

### imageManifestMediaType
- **Type**: typing.Optional[str]


# InitiateLayerUploadRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# InitiateLayerUploadResponseTypeDef

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### partSize
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LayerFailureTypeDef

### layerDigest
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['InvalidLayerDigest', 'MissingLayerDigest']]

### failureReason
- **Type**: typing.Optional[str]


# LayerTypeDef

### layerDigest
- **Type**: typing.Optional[str]

### layerAvailability
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'UNAVAILABLE']]

### layerSize
- **Type**: typing.Optional[int]

### mediaType
- **Type**: typing.Optional[str]


# LifecyclePolicyPreviewFilterTypeDef

### tagStatus
- **Type**: typing.Optional[typing.Literal['ANY', 'TAGGED', 'UNTAGGED']]


# LifecyclePolicyPreviewResultTypeDef

### imageTags
- **Type**: typing.Optional[typing.List[str]]

### imageDigest
- **Type**: typing.Optional[str]

### imagePushedAt
- **Type**: typing.Optional[datetime.datetime]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.LifecyclePolicyRuleActionTypeDef]

### appliedRulePriority
- **Type**: typing.Optional[int]


# LifecyclePolicyPreviewSummaryTypeDef

### expiringImageTotalCount
- **Type**: typing.Optional[int]


# LifecyclePolicyRuleActionTypeDef

### type
- **Type**: typing.Optional[typing.Literal['EXPIRE']]


# ListImagesFilterTypeDef

### tagStatus
- **Type**: typing.Optional[typing.Literal['ANY', 'TAGGED', 'UNTAGGED']]


# ListImagesRequestListImagesPaginateTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.ListImagesFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.PaginatorConfigTypeDef]


# ListImagesRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.ListImagesFilterTypeDef]


# ListImagesResponseTypeDef

### imageIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PackageVulnerabilityDetailsTypeDef

### cvss
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr_classes.CvssScoreTypeDef]]

### referenceUrls
- **Type**: typing.Optional[typing.List[str]]

### relatedVulnerabilities
- **Type**: typing.Optional[typing.List[str]]

### source
- **Type**: typing.Optional[str]

### sourceUrl
- **Type**: typing.Optional[str]

### vendorCreatedAt
- **Type**: typing.Optional[datetime.datetime]

### vendorSeverity
- **Type**: typing.Optional[str]

### vendorUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### vulnerabilityId
- **Type**: typing.Optional[str]

### vulnerablePackages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr_classes.VulnerablePackageTypeDef]]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PullThroughCacheRuleTypeDef

### ecrRepositoryPrefix
- **Type**: typing.Optional[str]

### upstreamRegistryUrl
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### registryId
- **Type**: typing.Optional[str]

### credentialArn
- **Type**: typing.Optional[str]

### upstreamRegistry
- **Type**: typing.Optional[typing.Literal['azure-container-registry', 'docker-hub', 'ecr-public', 'github-container-registry', 'gitlab-container-registry', 'k8s', 'quay']]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# PutImageRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageManifest
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageManifestMediaType
- **Type**: typing.Optional[str]

### imageTag
- **Type**: typing.Optional[str]

### imageDigest
- **Type**: typing.Optional[str]


# PutImageResponseTypeDef

### image
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutImageScanningConfigurationRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageScanningConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageScanningConfigurationTypeDef'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# PutImageScanningConfigurationResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageScanningConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageScanningConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutImageTagMutabilityRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageTagMutability
- **Type**: typing.Literal['IMMUTABLE', 'MUTABLE']
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# PutImageTagMutabilityResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageTagMutability
- **Type**: typing.Literal['IMMUTABLE', 'MUTABLE']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutLifecyclePolicyRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### lifecyclePolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# PutLifecyclePolicyResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### lifecyclePolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRegistryPolicyRequestRequestTypeDef

### policyText
- **Type**: <class 'str'>
- **Required**: Yes


# PutRegistryPolicyResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### policyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRegistryScanningConfigurationRequestRequestTypeDef

### scanType
- **Type**: typing.Optional[typing.Literal['BASIC', 'ENHANCED']]

### rules
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.ecr_classes.RegistryScanningRuleTypeDef, aws_resource_validator.pydantic_models.ecr_classes.RegistryScanningRuleOutputTypeDef]]]


# PutRegistryScanningConfigurationResponseTypeDef

### registryScanningConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.RegistryScanningConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutReplicationConfigurationRequestRequestTypeDef

### replicationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ReplicationConfigurationTypeDef'>
- **Required**: Yes


# PutReplicationConfigurationResponseTypeDef

### replicationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ReplicationConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RecommendationTypeDef

### url
- **Type**: typing.Optional[str]

### text
- **Type**: typing.Optional[str]


# RegistryScanningConfigurationTypeDef

### scanType
- **Type**: typing.Optional[typing.Literal['BASIC', 'ENHANCED']]

### rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr_classes.RegistryScanningRuleOutputTypeDef]]


# RegistryScanningRuleOutputTypeDef

### scanFrequency
- **Type**: typing.Literal['CONTINUOUS_SCAN', 'MANUAL', 'SCAN_ON_PUSH']
- **Required**: Yes

### repositoryFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.ScanningRepositoryFilterTypeDef]
- **Required**: Yes


# RegistryScanningRuleTypeDef

### scanFrequency
- **Type**: typing.Literal['CONTINUOUS_SCAN', 'MANUAL', 'SCAN_ON_PUSH']
- **Required**: Yes

### repositoryFilters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecr_classes.ScanningRepositoryFilterTypeDef]
- **Required**: Yes


# RemediationTypeDef

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.RecommendationTypeDef]


# ReplicationConfigurationOutputTypeDef

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.ReplicationRuleOutputTypeDef]
- **Required**: Yes


# ReplicationConfigurationTypeDef

### rules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecr_classes.ReplicationRuleTypeDef]
- **Required**: Yes


# ReplicationDestinationTypeDef

### region
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: <class 'str'>
- **Required**: Yes


# ReplicationRuleOutputTypeDef

### destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_classes.ReplicationDestinationTypeDef]
- **Required**: Yes

### repositoryFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr_classes.RepositoryFilterTypeDef]]


# ReplicationRuleTypeDef

### destinations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecr_classes.ReplicationDestinationTypeDef]
- **Required**: Yes

### repositoryFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecr_classes.RepositoryFilterTypeDef]]


# RepositoryFilterTypeDef

### filter
- **Type**: <class 'str'>
- **Required**: Yes

### filterType
- **Type**: typing.Literal['PREFIX_MATCH']
- **Required**: Yes


# RepositoryScanningConfigurationFailureTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['REPOSITORY_NOT_FOUND']]

### failureReason
- **Type**: typing.Optional[str]


# RepositoryScanningConfigurationTypeDef

### repositoryArn
- **Type**: typing.Optional[str]

### repositoryName
- **Type**: typing.Optional[str]

### scanOnPush
- **Type**: typing.Optional[bool]

### scanFrequency
- **Type**: typing.Optional[typing.Literal['CONTINUOUS_SCAN', 'MANUAL', 'SCAN_ON_PUSH']]

### appliedScanFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr_classes.ScanningRepositoryFilterTypeDef]]


# RepositoryTypeDef

### repositoryArn
- **Type**: typing.Optional[str]

### registryId
- **Type**: typing.Optional[str]

### repositoryName
- **Type**: typing.Optional[str]

### repositoryUri
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### imageTagMutability
- **Type**: typing.Optional[typing.Literal['IMMUTABLE', 'MUTABLE']]

### imageScanningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.ImageScanningConfigurationTypeDef]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.EncryptionConfigurationTypeDef]


# ResourceDetailsTypeDef

### awsEcrContainerImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.AwsEcrContainerImageDetailsTypeDef]


# ResourceTypeDef

### details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.ResourceDetailsTypeDef]

### id
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### type
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# ScanningRepositoryFilterTypeDef

### filter
- **Type**: <class 'str'>
- **Required**: Yes

### filterType
- **Type**: typing.Literal['WILDCARD']
- **Required**: Yes


# ScoreDetailsTypeDef

### cvss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_classes.CvssScoreDetailsTypeDef]


# SetRepositoryPolicyRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### policyText
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### force
- **Type**: typing.Optional[bool]


# SetRepositoryPolicyResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### policyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartImageScanRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# StartImageScanResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageIdentifierTypeDef'>
- **Required**: Yes

### imageScanStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ImageScanStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartLifecyclePolicyPreviewRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### lifecyclePolicyText
- **Type**: typing.Optional[str]


# StartLifecyclePolicyPreviewResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### lifecyclePolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETE', 'EXPIRED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecr_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdatePullThroughCacheRuleRequestRequestTypeDef

### ecrRepositoryPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### credentialArn
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# UpdatePullThroughCacheRuleResponseTypeDef

### ecrRepositoryPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### credentialArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UploadLayerPartRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### partFirstByte
- **Type**: <class 'int'>
- **Required**: Yes

### partLastByte
- **Type**: <class 'int'>
- **Required**: Yes

### layerPartBlob
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# UploadLayerPartResponseTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### lastByteReceived
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ValidatePullThroughCacheRuleRequestRequestTypeDef

### ecrRepositoryPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# ValidatePullThroughCacheRuleResponseTypeDef

### ecrRepositoryPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### upstreamRegistryUrl
- **Type**: <class 'str'>
- **Required**: Yes

### credentialArn
- **Type**: <class 'str'>
- **Required**: Yes

### isValid
- **Type**: <class 'bool'>
- **Required**: Yes

### failure
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VulnerablePackageTypeDef

### arch
- **Type**: typing.Optional[str]

### epoch
- **Type**: typing.Optional[int]

### filePath
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### packageManager
- **Type**: typing.Optional[str]

### release
- **Type**: typing.Optional[str]

### sourceLayerHash
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


