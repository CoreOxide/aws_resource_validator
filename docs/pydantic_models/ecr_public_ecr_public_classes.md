# Ecr Public Ecr Public Classes

# AuthorizationData

### authorizationToken
- **Type**: typing.Optional[str]

### expiresAt
- **Type**: typing.Optional[datetime.datetime]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.Layer]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.LayerFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeleteImageRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### imageIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ImageIdentifier]
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# BatchDeleteImageResponse

### imageIds
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ImageIdentifier]
- **Required**: Yes

### failures
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ImageFailure]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRepositoryRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### catalogData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.RepositoryCatalogDataInput]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.Tag]]


# CreateRepositoryResponse

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.Repository'>
- **Required**: Yes

### catalogData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.RepositoryCatalogData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.Repository'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeImageTagsRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeImageTagsRequestPaginate

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.PaginatorConfig]


# DescribeImageTagsResponse

### imageTagDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ImageTagDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeImagesRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ImageIdentifier]]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeImagesRequestPaginate

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]

### imageIds
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ImageIdentifier]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.PaginatorConfig]


# DescribeImagesResponse

### imageDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ImageDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# DescribeRegistriesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# DescribeRegistriesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.PaginatorConfig]


# DescribeRegistriesResponse

### registries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.Registry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.PaginatorConfig]


# DescribeRepositoriesResponse

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.Repository]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetAuthorizationTokenResponse

### authorizationData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.AuthorizationData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes


# GetRegistryCatalogDataResponse

### registryCatalogData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.RegistryCatalogData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes


# GetRepositoryCatalogDataRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# GetRepositoryCatalogDataResponse

### catalogData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.RepositoryCatalogData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes


# Image

### registryId
- **Type**: typing.Optional[str]

### repositoryName
- **Type**: typing.Optional[str]

### imageId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ImageIdentifier]

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

### imageManifestMediaType
- **Type**: typing.Optional[str]

### artifactMediaType
- **Type**: typing.Optional[str]


# ImageFailure

### imageId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ImageIdentifier]

### failureCode
- **Type**: typing.Optional[typing.Literal['ImageNotFound', 'ImageReferencedByManifestList', 'ImageTagDoesNotMatchDigest', 'InvalidImageDigest', 'InvalidImageTag', 'KmsError', 'MissingDigestAndTag']]

### failureReason
- **Type**: typing.Optional[str]


# ImageIdentifier

### imageDigest
- **Type**: typing.Optional[str]

### imageTag
- **Type**: typing.Optional[str]


# ImageTagDetail

### imageTag
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### imageDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ReferencedImageDetail]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
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


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.Image'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes


# PutRegistryCatalogDataRequest

### displayName
- **Type**: typing.Optional[str]


# PutRegistryCatalogDataResponse

### registryCatalogData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.RegistryCatalogData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes


# PutRepositoryCatalogDataRequest

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes

### catalogData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.RepositoryCatalogDataInput'>
- **Required**: Yes

### registryId
- **Type**: typing.Optional[str]


# PutRepositoryCatalogDataResponse

### catalogData
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.RepositoryCatalogData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes


# ReferencedImageDetail

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


# Registry

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.RegistryAlias]
- **Required**: Yes


# RegistryAlias

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


# RegistryCatalogData

### displayName
- **Type**: typing.Optional[str]


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


# RepositoryCatalogData

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


# RepositoryCatalogDataInput

### description
- **Type**: typing.Optional[str]

### architectures
- **Type**: typing.Optional[typing.List[str]]

### operatingSystems
- **Type**: typing.Optional[typing.List[str]]

### logoImageBlob
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### aboutText
- **Type**: typing.Optional[str]

### usageText
- **Type**: typing.Optional[str]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ecr_public.ecr_public_classes.ResponseMetadata'>
- **Required**: Yes


