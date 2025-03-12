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
from aws_resource_validator.pydantic_models.ecr_public_constants import *

class AuthorizationDataTypeDef(BaseValidatorModel):
    authorizationToken: Optional[str] = None
    expiresAt: Optional[datetime] = None


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


class CompleteLayerUploadRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    uploadId: str
    layerDigests: Sequence[str]
    registryId: Optional[str] = None


class TagTypeDef(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class RepositoryCatalogDataTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    architectures: Optional[List[str]] = None
    operatingSystems: Optional[List[str]] = None
    logoUrl: Optional[str] = None
    aboutText: Optional[str] = None
    usageText: Optional[str] = None
    marketplaceCertified: Optional[bool] = None


class RepositoryTypeDef(BaseValidatorModel):
    repositoryArn: Optional[str] = None
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    repositoryUri: Optional[str] = None
    createdAt: Optional[datetime] = None


class DeleteRepositoryPolicyRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class DeleteRepositoryRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    force: Optional[bool] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeImageTagsRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ImageDetailTypeDef(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    imageDigest: Optional[str] = None
    imageTags: Optional[List[str]] = None
    imageSizeInBytes: Optional[int] = None
    imagePushedAt: Optional[datetime] = None
    imageManifestMediaType: Optional[str] = None
    artifactMediaType: Optional[str] = None


class DescribeRegistriesRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeRepositoriesRequestTypeDef(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RegistryCatalogDataTypeDef(BaseValidatorModel):
    displayName: Optional[str] = None


class GetRepositoryCatalogDataRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class GetRepositoryPolicyRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class ReferencedImageDetailTypeDef(BaseValidatorModel):
    imageDigest: Optional[str] = None
    imageSizeInBytes: Optional[int] = None
    imagePushedAt: Optional[datetime] = None
    imageManifestMediaType: Optional[str] = None
    artifactMediaType: Optional[str] = None


class InitiateLayerUploadRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class PutImageRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageManifest: str
    registryId: Optional[str] = None
    imageManifestMediaType: Optional[str] = None
    imageTag: Optional[str] = None
    imageDigest: Optional[str] = None


class PutRegistryCatalogDataRequestTypeDef(BaseValidatorModel):
    displayName: Optional[str] = None


class RegistryAliasTypeDef(BaseValidatorModel):
    name: str
    status: RegistryAliasStatusType
    primaryRegistryAlias: bool
    defaultRegistryAlias: bool


class SetRepositoryPolicyRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    policyText: str
    registryId: Optional[str] = None
    force: Optional[bool] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


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


class DeleteRepositoryPolicyResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetAuthorizationTokenResponseTypeDef(BaseValidatorModel):
    authorizationData: AuthorizationDataTypeDef
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


class SetRepositoryPolicyResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadataTypeDef


class UploadLayerPartResponseTypeDef(BaseValidatorModel):
    registryId: str
    repositoryName: str
    uploadId: str
    lastByteReceived: int
    ResponseMetadata: ResponseMetadataTypeDef


class BatchDeleteImageRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    imageIds: Sequence[ImageIdentifierTypeDef]
    registryId: Optional[str] = None


class DescribeImagesRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
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


class BlobTypeDef(BaseValidatorModel):
    pass


class RepositoryCatalogDataInputTypeDef(BaseValidatorModel):
    description: Optional[str] = None
    architectures: Optional[Sequence[str]] = None
    operatingSystems: Optional[Sequence[str]] = None
    logoImageBlob: Optional[BlobTypeDef] = None
    aboutText: Optional[str] = None
    usageText: Optional[str] = None


class UploadLayerPartRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    uploadId: str
    partFirstByte: int
    partLastByte: int
    layerPartBlob: BlobTypeDef
    registryId: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]


class GetRepositoryCatalogDataResponseTypeDef(BaseValidatorModel):
    catalogData: RepositoryCatalogDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutRepositoryCatalogDataResponseTypeDef(BaseValidatorModel):
    catalogData: RepositoryCatalogDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRepositoryResponseTypeDef(BaseValidatorModel):
    repository: RepositoryTypeDef
    catalogData: RepositoryCatalogDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DeleteRepositoryResponseTypeDef(BaseValidatorModel):
    repository: RepositoryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeRepositoriesResponseTypeDef(BaseValidatorModel):
    repositories: List[RepositoryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeImageTagsRequestPaginateTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeImagesRequestPaginateTypeDef(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[Sequence[ImageIdentifierTypeDef]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRegistriesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeRepositoriesRequestPaginateTypeDef(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class DescribeImagesResponseTypeDef(BaseValidatorModel):
    imageDetails: List[ImageDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetRegistryCatalogDataResponseTypeDef(BaseValidatorModel):
    registryCatalogData: RegistryCatalogDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PutRegistryCatalogDataResponseTypeDef(BaseValidatorModel):
    registryCatalogData: RegistryCatalogDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ImageTagDetailTypeDef(BaseValidatorModel):
    imageTag: Optional[str] = None
    createdAt: Optional[datetime] = None
    imageDetail: Optional[ReferencedImageDetailTypeDef] = None


class RegistryTypeDef(BaseValidatorModel):
    registryId: str
    registryArn: str
    registryUri: str
    verified: bool
    aliases: List[RegistryAliasTypeDef]


class BatchDeleteImageResponseTypeDef(BaseValidatorModel):
    imageIds: List[ImageIdentifierTypeDef]
    failures: List[ImageFailureTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class PutImageResponseTypeDef(BaseValidatorModel):
    image: ImageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRepositoryRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    catalogData: Optional[RepositoryCatalogDataInputTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class PutRepositoryCatalogDataRequestTypeDef(BaseValidatorModel):
    repositoryName: str
    catalogData: RepositoryCatalogDataInputTypeDef
    registryId: Optional[str] = None


class DescribeImageTagsResponseTypeDef(BaseValidatorModel):
    imageTagDetails: List[ImageTagDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DescribeRegistriesResponseTypeDef(BaseValidatorModel):
    registries: List[RegistryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


