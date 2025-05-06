from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ecr_public.ecr_public_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AuthorizationData(BaseValidatorModel):
    authorizationToken: Optional[str] = None
    expiresAt: Optional[datetime] = None


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

Blob = Union[str, bytes, IO[Any], StreamingBody]


class CompleteLayerUploadRequest(BaseValidatorModel):
    repositoryName: str
    uploadId: str
    layerDigests: List[str]
    registryId: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: Optional[str] = None
    Value: Optional[str] = None


class RepositoryCatalogData(BaseValidatorModel):
    description: Optional[str] = None
    architectures: Optional[List[str]] = None
    operatingSystems: Optional[List[str]] = None
    logoUrl: Optional[str] = None
    aboutText: Optional[str] = None
    usageText: Optional[str] = None
    marketplaceCertified: Optional[bool] = None


class Repository(BaseValidatorModel):
    repositoryArn: Optional[str] = None
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    repositoryUri: Optional[str] = None
    createdAt: Optional[datetime] = None


class DeleteRepositoryPolicyRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class DeleteRepositoryRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    force: Optional[bool] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class DescribeImageTagsRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ImageDetail(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryName: Optional[str] = None
    imageDigest: Optional[str] = None
    imageTags: Optional[List[str]] = None
    imageSizeInBytes: Optional[int] = None
    imagePushedAt: Optional[datetime] = None
    imageManifestMediaType: Optional[str] = None
    artifactMediaType: Optional[str] = None


class DescribeRegistriesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class DescribeRepositoriesRequest(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[List[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class RegistryCatalogData(BaseValidatorModel):
    displayName: Optional[str] = None


class GetRepositoryCatalogDataRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class GetRepositoryPolicyRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class ReferencedImageDetail(BaseValidatorModel):
    imageDigest: Optional[str] = None
    imageSizeInBytes: Optional[int] = None
    imagePushedAt: Optional[datetime] = None
    imageManifestMediaType: Optional[str] = None
    artifactMediaType: Optional[str] = None


class InitiateLayerUploadRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class PutImageRequest(BaseValidatorModel):
    repositoryName: str
    imageManifest: str
    registryId: Optional[str] = None
    imageManifestMediaType: Optional[str] = None
    imageTag: Optional[str] = None
    imageDigest: Optional[str] = None


class PutRegistryCatalogDataRequest(BaseValidatorModel):
    displayName: Optional[str] = None


class RegistryAlias(BaseValidatorModel):
    name: str
    status: RegistryAliasStatusType
    primaryRegistryAlias: bool
    defaultRegistryAlias: bool


class SetRepositoryPolicyRequest(BaseValidatorModel):
    repositoryName: str
    policyText: str
    registryId: Optional[str] = None
    force: Optional[bool] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class BatchCheckLayerAvailabilityResponse(BaseValidatorModel):
    layers: List[Layer]
    failures: List[LayerFailure]
    ResponseMetadata: ResponseMetadata


class CompleteLayerUploadResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    uploadId: str
    layerDigest: str
    ResponseMetadata: ResponseMetadata


class DeleteRepositoryPolicyResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadata


class GetAuthorizationTokenResponse(BaseValidatorModel):
    authorizationData: AuthorizationData
    ResponseMetadata: ResponseMetadata


class GetRepositoryPolicyResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadata


class InitiateLayerUploadResponse(BaseValidatorModel):
    uploadId: str
    partSize: int
    ResponseMetadata: ResponseMetadata


class SetRepositoryPolicyResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    policyText: str
    ResponseMetadata: ResponseMetadata


class UploadLayerPartResponse(BaseValidatorModel):
    registryId: str
    repositoryName: str
    uploadId: str
    lastByteReceived: int
    ResponseMetadata: ResponseMetadata


class BatchDeleteImageRequest(BaseValidatorModel):
    repositoryName: str
    imageIds: List[ImageIdentifier]
    registryId: Optional[str] = None


class DescribeImagesRequest(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[List[ImageIdentifier]] = None
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


class RepositoryCatalogDataInput(BaseValidatorModel):
    description: Optional[str] = None
    architectures: Optional[List[str]] = None
    operatingSystems: Optional[List[str]] = None
    logoImageBlob: Optional[Blob] = None
    aboutText: Optional[str] = None
    usageText: Optional[str] = None


class UploadLayerPartRequest(BaseValidatorModel):
    repositoryName: str
    uploadId: str
    partFirstByte: int
    partLastByte: int
    layerPartBlob: Blob
    registryId: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


class GetRepositoryCatalogDataResponse(BaseValidatorModel):
    catalogData: RepositoryCatalogData
    ResponseMetadata: ResponseMetadata


class PutRepositoryCatalogDataResponse(BaseValidatorModel):
    catalogData: RepositoryCatalogData
    ResponseMetadata: ResponseMetadata


class CreateRepositoryResponse(BaseValidatorModel):
    repository: Repository
    catalogData: RepositoryCatalogData
    ResponseMetadata: ResponseMetadata


class DeleteRepositoryResponse(BaseValidatorModel):
    repository: Repository
    ResponseMetadata: ResponseMetadata


class DescribeRepositoriesResponse(BaseValidatorModel):
    repositories: List[Repository]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeImageTagsRequestPaginate(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeImagesRequestPaginate(BaseValidatorModel):
    repositoryName: str
    registryId: Optional[str] = None
    imageIds: Optional[List[ImageIdentifier]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRegistriesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeRepositoriesRequestPaginate(BaseValidatorModel):
    registryId: Optional[str] = None
    repositoryNames: Optional[List[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class DescribeImagesResponse(BaseValidatorModel):
    imageDetails: List[ImageDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetRegistryCatalogDataResponse(BaseValidatorModel):
    registryCatalogData: RegistryCatalogData
    ResponseMetadata: ResponseMetadata


class PutRegistryCatalogDataResponse(BaseValidatorModel):
    registryCatalogData: RegistryCatalogData
    ResponseMetadata: ResponseMetadata


class ImageTagDetail(BaseValidatorModel):
    imageTag: Optional[str] = None
    createdAt: Optional[datetime] = None
    imageDetail: Optional[ReferencedImageDetail] = None


class Registry(BaseValidatorModel):
    registryId: str
    registryArn: str
    registryUri: str
    verified: bool
    aliases: List[RegistryAlias]


class BatchDeleteImageResponse(BaseValidatorModel):
    imageIds: List[ImageIdentifier]
    failures: List[ImageFailure]
    ResponseMetadata: ResponseMetadata


class PutImageResponse(BaseValidatorModel):
    image: Image
    ResponseMetadata: ResponseMetadata


class CreateRepositoryRequest(BaseValidatorModel):
    repositoryName: str
    catalogData: Optional[RepositoryCatalogDataInput] = None
    tags: Optional[List[Tag]] = None


class PutRepositoryCatalogDataRequest(BaseValidatorModel):
    repositoryName: str
    catalogData: RepositoryCatalogDataInput
    registryId: Optional[str] = None


class DescribeImageTagsResponse(BaseValidatorModel):
    imageTagDetails: List[ImageTagDetail]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DescribeRegistriesResponse(BaseValidatorModel):
    registries: List[Registry]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None