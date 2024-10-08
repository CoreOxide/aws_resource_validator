# Pydantic Models in ecr_public_classes

# AuthorizationDataTypeDef

### authorizationToken
- **Type**: typing.Optional[str]

### expiresAt
- **Type**: typing.Optional[datetime.datetime]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public_classes.LayerTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public_classes.LayerFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeleteImageRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageIds
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecr_public_classes.ImageIdentifierTypeDef]
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# BatchDeleteImageResponseTypeDef

### imageIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public_classes.ImageIdentifierTypeDef]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public_classes.ImageFailureTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRepositoryRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### catalogData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public_classes.RepositoryCatalogDataInputTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecr_public_classes.TagTypeDef]]


# CreateRepositoryResponseTypeDef

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.RepositoryTypeDef'>
- **Required**: Yes

### catalogData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.RepositoryCatalogDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.RepositoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImageTagsRequestDescribeImageTagsPaginateTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public_classes.PaginatorConfigTypeDef]


# DescribeImageTagsRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeImageTagsResponseTypeDef

### imageTagDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public_classes.ImageTagDetailTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImagesRequestDescribeImagesPaginateTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecr_public_classes.ImageIdentifierTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public_classes.PaginatorConfigTypeDef]


# DescribeImagesRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ecr_public_classes.ImageIdentifierTypeDef]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeImagesResponseTypeDef

### imageDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public_classes.ImageDetailTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRegistriesRequestDescribeRegistriesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public_classes.PaginatorConfigTypeDef]


# DescribeRegistriesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeRegistriesResponseTypeDef

### registries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public_classes.RegistryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef

### registryId
- **Type**: typing.Optional[str]

### repositoryNames
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public_classes.PaginatorConfigTypeDef]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public_classes.RepositoryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAuthorizationTokenResponseTypeDef

### authorizationData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.AuthorizationDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRegistryCatalogDataResponseTypeDef

### registryCatalogData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.RegistryCatalogDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRepositoryCatalogDataRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# GetRepositoryCatalogDataResponseTypeDef

### catalogData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.RepositoryCatalogDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
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

### imageManifestMediaType
- **Type**: typing.Optional[str]

### artifactMediaType
- **Type**: typing.Optional[str]


# ImageFailureTypeDef

### imageId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public_classes.ImageIdentifierTypeDef]

### failureCode
- **Type**: typing.Optional[typing.Literal['ImageNotFound', 'ImageReferencedByManifestList', 'ImageTagDoesNotMatchDigest', 'InvalidImageDigest', 'InvalidImageTag', 'KmsError', 'MissingDigestAndTag']]

### failureReason
- **Type**: typing.Optional[str]


# ImageIdentifierTypeDef

### imageDigest
- **Type**: typing.Optional[str]

### imageTag
- **Type**: typing.Optional[str]


# ImageTagDetailTypeDef

### imageTag
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### imageDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public_classes.ReferencedImageDetailTypeDef]


# ImageTypeDef

### registryId
- **Type**: typing.Optional[str]

### repositoryName
- **Type**: typing.Optional[str]

### imageId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public_classes.ImageIdentifierTypeDef]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
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


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ImageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRegistryCatalogDataRequestRequestTypeDef

### displayName
- **Type**: typing.Optional[str]


# PutRegistryCatalogDataResponseTypeDef

### registryCatalogData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.RegistryCatalogDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRepositoryCatalogDataRequestRequestTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### catalogData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.RepositoryCatalogDataInputTypeDef'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# PutRepositoryCatalogDataResponseTypeDef

### catalogData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.RepositoryCatalogDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReferencedImageDetailTypeDef

### imageDigest
- **Type**: typing.Optional[str]

### imageSizeInBytes
- **Type**: typing.Optional[int]

### imagePushedAt
- **Type**: typing.Optional[datetime.datetime]

### imageManifestMediaType
- **Type**: typing.Optional[str]

### artifactMediaType
- **Type**: typing.Optional[str]


# RegistryAliasTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'PENDING', 'REJECTED']
- **Required**: Yes

### primaryRegistryAlias
- **Type**: <class 'bool'>
- **Required**: Yes

### defaultRegistryAlias
- **Type**: <class 'bool'>
- **Required**: Yes


# RegistryCatalogDataTypeDef

### displayName
- **Type**: typing.Optional[str]


# RegistryTypeDef

### registryId
- **Type**: <class 'str'>
- **Required**: Yes

### registryArn
- **Type**: <class 'str'>
- **Required**: Yes

### registryUri
- **Type**: <class 'str'>
- **Required**: Yes

### verified
- **Type**: <class 'bool'>
- **Required**: Yes

### aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public_classes.RegistryAliasTypeDef]
- **Required**: Yes


# RepositoryCatalogDataInputTypeDef

### description
- **Type**: typing.Optional[str]

### architectures
- **Type**: typing.Optional[typing.Sequence[str]]

### operatingSystems
- **Type**: typing.Optional[typing.Sequence[str]]

### logoImageBlob
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### aboutText
- **Type**: typing.Optional[str]

### usageText
- **Type**: typing.Optional[str]


# RepositoryCatalogDataTypeDef

### description
- **Type**: typing.Optional[str]

### architectures
- **Type**: typing.Optional[typing.List[str]]

### operatingSystems
- **Type**: typing.Optional[typing.List[str]]

### logoUrl
- **Type**: typing.Optional[str]

### aboutText
- **Type**: typing.Optional[str]

### usageText
- **Type**: typing.Optional[str]

### marketplaceCertified
- **Type**: typing.Optional[bool]


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


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ecr_public_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


