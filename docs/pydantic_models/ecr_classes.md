# Ecr Classes

# Attribute

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# AuthorizationData

### authorizationToken
- **Type**: typing.Optional[str]

### expiresAt
- **Type**: typing.Optional[datetime.datetime]

### proxyEndpoint
- **Type**: typing.Optional[str]


# AwsEcrContainerImageDetails

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

# BatchCheckLayerAvailabilityRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### layerDigests
- **Type**: typing.List[str]
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# BatchCheckLayerAvailabilityResponse

### layers
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.Layer]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.LayerFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteImageRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier]
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# BatchDeleteImageResponse

### imageIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetImageRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier]
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### acceptedMediaTypes
- **Type**: typing.Optional[typing.List[str]]


# BatchGetImageResponse

### images
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.Image]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetRepositoryScanningConfigurationRequest

### repositoryNames
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetRepositoryScanningConfigurationResponse

### scanningConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.RepositoryScanningConfiguration]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.RepositoryScanningConfigurationFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# CompleteLayerUploadRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### layerDigests
- **Type**: typing.List[str]
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# CompleteLayerUploadResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePullThroughCacheRuleRequest

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


# CreatePullThroughCacheRuleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRepositoryCreationTemplateRequest

### prefix
- **Type**: <class 'str'>
- **Required**: Yes

### appliedFor
- **Type**: typing.List[typing.Literal['PULL_THROUGH_CACHE', 'REPLICATION']]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.EncryptionConfigurationForRepositoryCreationTemplate]

### resourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.Tag]]

### imageTagMutability
- **Type**: typing.Optional[typing.Literal['IMMUTABLE', 'MUTABLE']]

### repositoryPolicy
- **Type**: typing.Optional[str]

### lifecyclePolicy
- **Type**: typing.Optional[str]

### customRoleArn
- **Type**: typing.Optional[str]


# CreateRepositoryCreationTemplateResponse

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryCreationTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.RepositoryCreationTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRepositoryRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.Tag]]

### imageTagMutability
- **Type**: typing.Optional[typing.Literal['IMMUTABLE', 'MUTABLE']]

### imageScanningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageScanningConfiguration]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.EncryptionConfiguration]


# CreateRepositoryResponse

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.Repository'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# CvssScore

### baseScore
- **Type**: typing.Optional[float]

### scoringVector
- **Type**: typing.Optional[str]

### source
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# CvssScoreAdjustment

### metric
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# CvssScoreDetails

### adjustments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.CvssScoreAdjustment]]

### score
- **Type**: typing.Optional[float]

### scoreSource
- **Type**: typing.Optional[str]

### scoringVector
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]


# DeleteLifecyclePolicyRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# DeleteLifecyclePolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePullThroughCacheRuleRequest

### ecrRepositoryPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# DeletePullThroughCacheRuleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRegistryPolicyResponse

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### policyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRepositoryCreationTemplateRequest

### prefix
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRepositoryCreationTemplateResponse

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryCreationTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.RepositoryCreationTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRepositoryPolicyRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# DeleteRepositoryPolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRepositoryRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### force
- **Type**: typing.Optional[bool]


# DeleteRepositoryResponse

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.Repository'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeImageReplicationStatusRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# DescribeImageReplicationStatusResponse

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier'>
- **Required**: Yes

### replicationStatuses
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageReplicationStatus]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeImageScanFindingsRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeImageScanFindingsRequestPaginate

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.PaginatorConfig]


# DescribeImageScanFindingsRequestWait

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### WaiterConfig
- **Type**: <class 'NoneType'>


# DescribeImageScanFindingsResponse

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier'>
- **Required**: Yes

### imageScanStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageScanStatus'>
- **Required**: Yes

### imageScanFindings
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageScanFindings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeImagesFilter

### tagStatus
- **Type**: typing.Optional[typing.Literal['ANY', 'TAGGED', 'UNTAGGED']]


# DescribeImagesRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.DescribeImagesFilter]


# DescribeImagesRequestPaginate

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.DescribeImagesFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.PaginatorConfig]


# DescribeImagesResponse

### imageDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribePullThroughCacheRulesRequest

### registryId
- **Type**: typing.Optional[str]

### ecrRepositoryPrefixes
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribePullThroughCacheRulesRequestPaginate

### registryId
- **Type**: typing.Optional[str]

### ecrRepositoryPrefixes
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.PaginatorConfig]


# DescribePullThroughCacheRulesResponse

### pullThroughCacheRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.PullThroughCacheRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeRegistryResponse

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### replicationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ReplicationConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRepositoriesRequest

### registryId
- **Type**: typing.Optional[str]

### repositoryNames
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeRepositoriesRequestPaginate

### registryId
- **Type**: typing.Optional[str]

### repositoryNames
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.PaginatorConfig]


# DescribeRepositoriesResponse

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.Repository]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeRepositoryCreationTemplatesRequest

### prefixes
- **Type**: typing.Optional[typing.List[str]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeRepositoryCreationTemplatesRequestPaginate

### prefixes
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.PaginatorConfig]


# DescribeRepositoryCreationTemplatesResponse

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryCreationTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.RepositoryCreationTemplate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# EncryptionConfiguration

### encryptionType
- **Type**: typing.Literal['AES256', 'KMS', 'KMS_DSSE']
- **Required**: Yes

### kmsKey
- **Type**: typing.Optional[str]


# EncryptionConfigurationForRepositoryCreationTemplate

### encryptionType
- **Type**: typing.Literal['AES256', 'KMS', 'KMS_DSSE']
- **Required**: Yes

### kmsKey
- **Type**: typing.Optional[str]


# EnhancedImageScanFinding

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.PackageVulnerabilityDetails]

### remediation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.Remediation]

### resources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.Resource]]

### score
- **Type**: typing.Optional[float]

### scoreDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.ScoreDetails]

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

### fixAvailable
- **Type**: typing.Optional[str]

### exploitAvailable
- **Type**: typing.Optional[str]


# GetAccountSettingRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccountSettingResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# GetAuthorizationTokenRequest

### registryIds
- **Type**: typing.Optional[typing.List[str]]


# GetAuthorizationTokenResponse

### authorizationData
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.AuthorizationData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# GetDownloadUrlForLayerRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### layerDigest
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# GetDownloadUrlForLayerResponse

### downloadUrl
- **Type**: <class 'str'>
- **Required**: Yes

### layerDigest
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# GetLifecyclePolicyPreviewRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.LifecyclePolicyPreviewFilter]


# GetLifecyclePolicyPreviewRequestPaginate

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier]]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.LifecyclePolicyPreviewFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.PaginatorConfig]


# GetLifecyclePolicyPreviewRequestWait

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.LifecyclePolicyPreviewFilter]

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetLifecyclePolicyPreviewResponse

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

### previewResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.LifecyclePolicyPreviewResult]
- **Required**: Yes

### summary
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.LifecyclePolicyPreviewSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetLifecyclePolicyRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# GetLifecyclePolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# GetRegistryPolicyResponse

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### policyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# GetRegistryScanningConfigurationResponse

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### scanningConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.RegistryScanningConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# GetRepositoryPolicyRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# GetRepositoryPolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# Image

### registryId
- **Type**: typing.Optional[str]

### repositoryName
- **Type**: typing.Optional[str]

### imageId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier]

### imageManifest
- **Type**: typing.Optional[str]

### imageManifestMediaType
- **Type**: typing.Optional[str]


# ImageDetail

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageScanStatus]

### imageScanFindingsSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageScanFindingsSummary]

### imageManifestMediaType
- **Type**: typing.Optional[str]

### artifactMediaType
- **Type**: typing.Optional[str]

### lastRecordedPullTime
- **Type**: typing.Optional[datetime.datetime]


# ImageFailure

### imageId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier]

### failureCode
- **Type**: typing.Optional[typing.Literal['ImageNotFound', 'ImageReferencedByManifestList', 'ImageTagDoesNotMatchDigest', 'InvalidImageDigest', 'InvalidImageTag', 'KmsError', 'MissingDigestAndTag', 'UpstreamAccessDenied', 'UpstreamTooManyRequests', 'UpstreamUnavailable']]

### failureReason
- **Type**: typing.Optional[str]


# ImageIdentifier

### imageDigest
- **Type**: typing.Optional[str]

### imageTag
- **Type**: typing.Optional[str]


# ImageReplicationStatus

### region
- **Type**: typing.Optional[str]

### registryId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS']]

### failureCode
- **Type**: typing.Optional[str]


# ImageScanFinding

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### uri
- **Type**: typing.Optional[str]

### severity
- **Type**: typing.Optional[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNDEFINED']]

### attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.Attribute]]


# ImageScanFindings

### imageScanCompletedAt
- **Type**: typing.Optional[datetime.datetime]

### vulnerabilitySourceUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### findingSeverityCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNDEFINED'], int]]

### findings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageScanFinding]]

### enhancedFindings
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.EnhancedImageScanFinding]]


# ImageScanFindingsSummary

### imageScanCompletedAt
- **Type**: typing.Optional[datetime.datetime]

### vulnerabilitySourceUpdatedAt
- **Type**: typing.Optional[datetime.datetime]

### findingSeverityCounts
- **Type**: typing.Optional[typing.Dict[typing.Literal['CRITICAL', 'HIGH', 'INFORMATIONAL', 'LOW', 'MEDIUM', 'UNDEFINED'], int]]


# ImageScanStatus

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'COMPLETE', 'FAILED', 'FINDINGS_UNAVAILABLE', 'IN_PROGRESS', 'LIMIT_EXCEEDED', 'PENDING', 'SCAN_ELIGIBILITY_EXPIRED', 'UNSUPPORTED_IMAGE']]

### description
- **Type**: typing.Optional[str]


# ImageScanningConfiguration

### scanOnPush
- **Type**: typing.Optional[bool]


# InitiateLayerUploadRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# InitiateLayerUploadResponse

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### partSize
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# Layer

### layerDigest
- **Type**: typing.Optional[str]

### layerAvailability
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'UNAVAILABLE']]

### layerSize
- **Type**: typing.Optional[int]

### mediaType
- **Type**: typing.Optional[str]


# LayerFailure

### layerDigest
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['InvalidLayerDigest', 'MissingLayerDigest']]

### failureReason
- **Type**: typing.Optional[str]


# LifecyclePolicyPreviewFilter

### tagStatus
- **Type**: typing.Optional[typing.Literal['ANY', 'TAGGED', 'UNTAGGED']]


# LifecyclePolicyPreviewResult

### imageTags
- **Type**: typing.Optional[typing.List[str]]

### imageDigest
- **Type**: typing.Optional[str]

### imagePushedAt
- **Type**: typing.Optional[datetime.datetime]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.LifecyclePolicyRuleAction]

### appliedRulePriority
- **Type**: typing.Optional[int]


# LifecyclePolicyPreviewSummary

### expiringImageTotalCount
- **Type**: typing.Optional[int]


# LifecyclePolicyRuleAction

### type
- **Type**: typing.Optional[typing.Literal['EXPIRE']]


# ListImagesFilter

### tagStatus
- **Type**: typing.Optional[typing.Literal['ANY', 'TAGGED', 'UNTAGGED']]


# ListImagesRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.ListImagesFilter]


# ListImagesRequestPaginate

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.ListImagesFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.PaginatorConfig]


# ListImagesResponse

### imageIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# PackageVulnerabilityDetails

### cvss
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.CvssScore]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.VulnerablePackage]]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PullThroughCacheRule

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


# PutAccountSettingRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# PutAccountSettingResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# PutImageRequest

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


# PutImageResponse

### image
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.Image'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# PutImageScanningConfigurationRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageScanningConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageScanningConfiguration'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# PutImageScanningConfigurationResponse

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageScanningConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageScanningConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# PutImageTagMutabilityRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageTagMutability
- **Type**: typing.Literal['IMMUTABLE', 'MUTABLE']
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# PutImageTagMutabilityResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# PutLifecyclePolicyRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### lifecyclePolicyText
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# PutLifecyclePolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# PutRegistryPolicyRequest

### policyText
- **Type**: <class 'str'>
- **Required**: Yes


# PutRegistryPolicyResponse

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### policyText
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# PutRegistryScanningConfigurationRequest

### scanType
- **Type**: typing.Optional[typing.Literal['BASIC', 'ENHANCED']]

### rules
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.ecr.ecr_classes.RegistryScanningRule, aws_resource_validator.pydantic_models.ecr.ecr_classes.RegistryScanningRuleOutput]]]


# PutRegistryScanningConfigurationResponse

### registryScanningConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.RegistryScanningConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# PutReplicationConfigurationRequest

### replicationConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ecr.ecr_classes.ReplicationConfiguration, aws_resource_validator.pydantic_models.ecr.ecr_classes.ReplicationConfigurationOutput]
- **Required**: Yes


# PutReplicationConfigurationResponse

### replicationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ReplicationConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# Recommendation

### url
- **Type**: typing.Optional[str]

### text
- **Type**: typing.Optional[str]


# RegistryScanningConfiguration

### scanType
- **Type**: typing.Optional[typing.Literal['BASIC', 'ENHANCED']]

### rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.RegistryScanningRuleOutput]]


# RegistryScanningRule

### scanFrequency
- **Type**: typing.Literal['CONTINUOUS_SCAN', 'MANUAL', 'SCAN_ON_PUSH']
- **Required**: Yes

### repositoryFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ScanningRepositoryFilter]
- **Required**: Yes


# RegistryScanningRuleOutput

### scanFrequency
- **Type**: typing.Literal['CONTINUOUS_SCAN', 'MANUAL', 'SCAN_ON_PUSH']
- **Required**: Yes

### repositoryFilters
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ScanningRepositoryFilter]
- **Required**: Yes


# Remediation

### recommendation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.Recommendation]


# ReplicationConfiguration

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ReplicationRule]
- **Required**: Yes


# ReplicationConfigurationOutput

### rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ReplicationRuleOutput]
- **Required**: Yes


# ReplicationDestination

### region
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: <class 'str'>
- **Required**: Yes


# ReplicationRule

### destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ReplicationDestination]
- **Required**: Yes

### repositoryFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.RepositoryFilter]]


# ReplicationRuleOutput

### destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ReplicationDestination]
- **Required**: Yes

### repositoryFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.RepositoryFilter]]


# Repository

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageScanningConfiguration]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.EncryptionConfiguration]


# RepositoryCreationTemplate

### prefix
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.EncryptionConfigurationForRepositoryCreationTemplate]

### resourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.Tag]]

### imageTagMutability
- **Type**: typing.Optional[typing.Literal['IMMUTABLE', 'MUTABLE']]

### repositoryPolicy
- **Type**: typing.Optional[str]

### lifecyclePolicy
- **Type**: typing.Optional[str]

### appliedFor
- **Type**: typing.Optional[typing.List[typing.Literal['PULL_THROUGH_CACHE', 'REPLICATION']]]

### customRoleArn
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# RepositoryFilter

### filter
- **Type**: <class 'str'>
- **Required**: Yes

### filterType
- **Type**: typing.Literal['PREFIX_MATCH']
- **Required**: Yes


# RepositoryScanningConfiguration

### repositoryArn
- **Type**: typing.Optional[str]

### repositoryName
- **Type**: typing.Optional[str]

### scanOnPush
- **Type**: typing.Optional[bool]

### scanFrequency
- **Type**: typing.Optional[typing.Literal['CONTINUOUS_SCAN', 'MANUAL', 'SCAN_ON_PUSH']]

### appliedScanFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.ScanningRepositoryFilter]]


# RepositoryScanningConfigurationFailure

### repositoryName
- **Type**: typing.Optional[str]

### failureCode
- **Type**: typing.Optional[typing.Literal['REPOSITORY_NOT_FOUND']]

### failureReason
- **Type**: typing.Optional[str]


# Resource

### details
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.ResourceDetails]

### id
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### type
- **Type**: typing.Optional[str]


# ResourceDetails

### awsEcrContainerImage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.AwsEcrContainerImageDetails]


# ResponseMetadata

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


# ScanningRepositoryFilter

### filter
- **Type**: <class 'str'>
- **Required**: Yes

### filterType
- **Type**: typing.Literal['WILDCARD']
- **Required**: Yes


# ScoreDetails

### cvss
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.CvssScoreDetails]


# SetRepositoryPolicyRequest

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


# SetRepositoryPolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# StartImageScanRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# StartImageScanResponse

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageId
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageIdentifier'>
- **Required**: Yes

### imageScanStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ImageScanStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# StartLifecyclePolicyPreviewRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### lifecyclePolicyText
- **Type**: typing.Optional[str]


# StartLifecyclePolicyPreviewResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdatePullThroughCacheRuleRequest

### ecrRepositoryPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### credentialArn
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# UpdatePullThroughCacheRuleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRepositoryCreationTemplateRequest

### prefix
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### encryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr.ecr_classes.EncryptionConfigurationForRepositoryCreationTemplate]

### resourceTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr.ecr_classes.Tag]]

### imageTagMutability
- **Type**: typing.Optional[typing.Literal['IMMUTABLE', 'MUTABLE']]

### repositoryPolicy
- **Type**: typing.Optional[str]

### lifecyclePolicy
- **Type**: typing.Optional[str]

### appliedFor
- **Type**: typing.Optional[typing.List[typing.Literal['PULL_THROUGH_CACHE', 'REPLICATION']]]

### customRoleArn
- **Type**: typing.Optional[str]


# UpdateRepositoryCreationTemplateResponse

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### repositoryCreationTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.RepositoryCreationTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# UploadLayerPartRequest

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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# UploadLayerPartResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# ValidatePullThroughCacheRuleRequest

### ecrRepositoryPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# ValidatePullThroughCacheRuleResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr.ecr_classes.ResponseMetadata'>
- **Required**: Yes


# VulnerablePackage

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

### fixedInVersion
- **Type**: typing.Optional[str]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


