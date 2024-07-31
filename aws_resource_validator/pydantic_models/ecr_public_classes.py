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
from aws_resource_validator.pydantic_models.ecr_public_constants import *

class AuthorizationDataTypeDef(BaseModel):
    authorizationToken: Optional[str] = None
    expiresAt: Optional[datetime] = None

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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class ImageIdentifierTypeDef(BaseModel):
    imageDigest: Optional[str] = None
    imageTag: Optional[str] = None

class CompleteLayerUploadRequestRequestTypeDef(BaseModel):
    repositoryName: str
    uploadId: str
    layerDigests: Sequence[str]
    registryId: Optional[str] = None

class TagTypeDef(BaseModel):
    Key: Optional[str] = None
    Value: Optional[str] = None

class RepositoryCatalogDataTypeDef(BaseModel):
    description: Optional[str] = None
    architectures: Optional[List[str]] = None
    operatingSystems: Optional[List[str]] = None
    logoUrl: Optional[str] = None
    aboutText: Optional[str] = None
    usageText: Optional[str] = None
    marketplaceCertified: Optional[bool] = None

class RepositoryTypeDef(BaseModel):
    repositoryArn: Optional[str] = None
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    repositoryUri: Optional[str] = None
    createdAt: Optional[datetime] = None

class DeleteRepositoryPolicyRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None

class DeleteRepositoryRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    force: Optional[bool] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class DescribeImageTagsRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ImageDetailTypeDef(BaseModel):
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    imageDigest: Optional[str] = None
    imageTags: Optional[List[str]] = None
    imageSizeInBytes: Optional[int] = None
    imagePushedAt: Optional[datetime] = None
    imageManifestMediaType: Optional[str] = None
    artifactMediaType: Optional[str] = None

class DescribeRegistriesRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class DescribeRepositoriesRequestRequestTypeDef(BaseModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RegistryCatalogDataTypeDef(BaseModel):
    displayName: Optional[str] = None

class GetRepositoryCatalogDataRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None

class GetRepositoryPolicyRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None

class ReferencedImageDetailTypeDef(BaseModel):
    imageDigest: Optional[str] = None
    imageSizeInBytes: Optional[int] = None
    imagePushedAt: Optional[datetime] = None
    imageManifestMediaType: Optional[str] = None
    artifactMediaType: Optional[str] = None

class InitiateLayerUploadRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class PutImageRequestRequestTypeDef(BaseModel):
    repositoryName: str
    imageManifest: str
    registryId: Optional[str] = None
    imageManifestMediaType: Optional[str] = None
    imageTag: Optional[str] = None
    imageDigest: Optional[str] = None

class PutRegistryCatalogDataRequestRequestTypeDef(BaseModel):
    displayName: Optional[str] = None

class RegistryAliasTypeDef(BaseModel):
    name: str
    status: RegistryAliasStatusType
    primaryRegistryAlias: bool
    defaultRegistryAlias: bool

class SetRepositoryPolicyRequestRequestTypeDef(BaseModel):
    repositoryName: str
    policyText: str
    registryId: Optional[str] = None
    force: Optional[bool] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

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

class DeleteRepositoryPolicyResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetAuthorizationTokenResponseTypeDef(BaseModel):
    authorizationData: AuthorizationDataTypeDef
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

class SetRepositoryPolicyResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef

class UploadLayerPartResponseTypeDef(BaseModel):
    registryId: str
    repositoryName: str
    uploadId: str
    lastByteReceived: int
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteImageRequestRequestTypeDef(BaseModel):
    repositoryName: str
    imageIds: Sequence[ImageIdentifierTypeDef]
    registryId: Optional[str] = None

class DescribeImagesRequestRequestTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
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

class RepositoryCatalogDataInputTypeDef(BaseModel):
    description: Optional[str] = None
    architectures: Optional[Sequence[str]] = None
    operatingSystems: Optional[Sequence[str]] = None
    logoImageBlob: Optional[BlobTypeDef] = None
    aboutText: Optional[str] = None
    usageText: Optional[str] = None

class UploadLayerPartRequestRequestTypeDef(BaseModel):
    repositoryName: str
    uploadId: str
    partFirstByte: int
    partLastByte: int
    layerPartBlob: BlobTypeDef
    registryId: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class GetRepositoryCatalogDataResponseTypeDef(BaseModel):
    catalogData: RepositoryCatalogDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutRepositoryCatalogDataResponseTypeDef(BaseModel):
    catalogData: RepositoryCatalogDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryResponseTypeDef(BaseModel):
    repository: RepositoryTypeDef
    catalogData: RepositoryCatalogDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryResponseTypeDef(BaseModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRepositoriesResponseTypeDef(BaseModel):
    repositories: List[RepositoryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeImageTagsRequestDescribeImageTagsPaginateTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImagesRequestDescribeImagesPaginateTypeDef(BaseModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRegistriesRequestDescribeRegistriesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeRepositoriesRequestDescribeRepositoriesPaginateTypeDef(BaseModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class DescribeImagesResponseTypeDef(BaseModel):
    imageDetails: List[ImageDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRegistryCatalogDataResponseTypeDef(BaseModel):
    registryCatalogData: RegistryCatalogDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutRegistryCatalogDataResponseTypeDef(BaseModel):
    registryCatalogData: RegistryCatalogDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImageTagDetailTypeDef(BaseModel):
    imageTag: Optional[str] = None
    createdAt: Optional[datetime] = None
    imageDetail: Optional[ReferencedImageDetailTypeDef] = None

class RegistryTypeDef(BaseModel):
    registryId: str
    registryArn: str
    registryUri: str
    verified: bool
    aliases: List[RegistryAliasTypeDef]

class BatchDeleteImageResponseTypeDef(BaseModel):
    imageIds: List[ImageIdentifierTypeDef]
    failures: List[ImageFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutImageResponseTypeDef(BaseModel):
    image: ImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryRequestRequestTypeDef(BaseModel):
    repositoryName: str
    catalogData: Optional[RepositoryCatalogDataInputTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class PutRepositoryCatalogDataRequestRequestTypeDef(BaseModel):
    repositoryName: str
    catalogData: RepositoryCatalogDataInputTypeDef
    registryId: Optional[str] = None

class DescribeImageTagsResponseTypeDef(BaseModel):
    imageTagDetails: List[ImageTagDetailTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRegistriesResponseTypeDef(BaseModel):
    registries: List[RegistryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

