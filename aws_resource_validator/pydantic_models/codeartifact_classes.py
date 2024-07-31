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
from aws_resource_validator.pydantic_models.codeartifact_constants import *

class AssetSummaryTypeDef(BaseModel):
    name: str
    size: Optional[int] = None
    hashes: Optional[Dict[HashAlgorithmType, str]] = None

class AssociateExternalConnectionRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    externalConnection: str
    domainOwner: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssociatedPackageTypeDef(BaseModel):
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    package: Optional[str] = None
    associationType: Optional[PackageGroupAssociationTypeType] = None

class CopyPackageVersionsRequestRequestTypeDef(BaseModel):
    domain: str
    sourceRepository: str
    destinationRepository: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    versions: Optional[Sequence[str]] = None
    versionRevisions: Optional[Mapping[str, str]] = None
    allowOverwrite: Optional[bool] = None
    includeFromUpstream: Optional[bool] = None

class PackageVersionErrorTypeDef(BaseModel):
    errorCode: Optional[PackageVersionErrorCodeType] = None
    errorMessage: Optional[str] = None

class SuccessfulPackageVersionInfoTypeDef(BaseModel):
    revision: Optional[str] = None
    status: Optional[PackageVersionStatusType] = None

class TagTypeDef(BaseModel):
    key: str
    value: str

class DomainDescriptionTypeDef(BaseModel):
    name: Optional[str] = None
    owner: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[DomainStatusType] = None
    createdTime: Optional[datetime] = None
    encryptionKey: Optional[str] = None
    repositoryCount: Optional[int] = None
    assetSizeBytes: Optional[int] = None
    s3BucketArn: Optional[str] = None

class UpstreamRepositoryTypeDef(BaseModel):
    repositoryName: str

class DeleteDomainPermissionsPolicyRequestRequestTypeDef(BaseModel):
    domain: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None

class ResourcePolicyTypeDef(BaseModel):
    resourceArn: Optional[str] = None
    revision: Optional[str] = None
    document: Optional[str] = None

class DeleteDomainRequestRequestTypeDef(BaseModel):
    domain: str
    domainOwner: Optional[str] = None

class DeletePackageGroupRequestRequestTypeDef(BaseModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None

class DeletePackageRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None

class DeletePackageVersionsRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    versions: Sequence[str]
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    expectedStatus: Optional[PackageVersionStatusType] = None

class DeleteRepositoryPermissionsPolicyRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None

class DeleteRepositoryRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None

class DescribeDomainRequestRequestTypeDef(BaseModel):
    domain: str
    domainOwner: Optional[str] = None

class DescribePackageGroupRequestRequestTypeDef(BaseModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None

class DescribePackageRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None

class DescribePackageVersionRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None

class DescribeRepositoryRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None

class DisassociateExternalConnectionRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    externalConnection: str
    domainOwner: Optional[str] = None

class DisposePackageVersionsRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    versions: Sequence[str]
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    versionRevisions: Optional[Mapping[str, str]] = None
    expectedStatus: Optional[PackageVersionStatusType] = None

class DomainEntryPointTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    externalConnectionName: Optional[str] = None

class DomainSummaryTypeDef(BaseModel):
    name: Optional[str] = None
    owner: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[DomainStatusType] = None
    createdTime: Optional[datetime] = None
    encryptionKey: Optional[str] = None

class GetAssociatedPackageGroupRequestRequestTypeDef(BaseModel):
    domain: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None

class GetAuthorizationTokenRequestRequestTypeDef(BaseModel):
    domain: str
    domainOwner: Optional[str] = None
    durationSeconds: Optional[int] = None

class GetDomainPermissionsPolicyRequestRequestTypeDef(BaseModel):
    domain: str
    domainOwner: Optional[str] = None

class GetPackageVersionAssetRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    asset: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    packageVersionRevision: Optional[str] = None

class GetPackageVersionReadmeRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None

class GetRepositoryEndpointRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    domainOwner: Optional[str] = None

class GetRepositoryPermissionsPolicyRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None

class LicenseInfoTypeDef(BaseModel):
    name: Optional[str] = None
    url: Optional[str] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAllowedRepositoriesForGroupRequestRequestTypeDef(BaseModel):
    domain: str
    packageGroup: str
    originRestrictionType: PackageGroupOriginRestrictionTypeType
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAssociatedPackagesRequestRequestTypeDef(BaseModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    preview: Optional[bool] = None

class ListDomainsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListPackageGroupsRequestRequestTypeDef(BaseModel):
    domain: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    prefix: Optional[str] = None

class ListPackageVersionAssetsRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListPackageVersionDependenciesRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    nextToken: Optional[str] = None

class PackageDependencyTypeDef(BaseModel):
    namespace: Optional[str] = None
    package: Optional[str] = None
    dependencyType: Optional[str] = None
    versionRequirement: Optional[str] = None

class ListPackageVersionsRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    status: Optional[PackageVersionStatusType] = None
    sortBy: Optional[Literal["PUBLISHED_TIME"]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    originType: Optional[PackageVersionOriginTypeType] = None

class ListPackagesRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    packagePrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    publish: Optional[AllowPublishType] = None
    upstream: Optional[AllowUpstreamType] = None

class ListRepositoriesInDomainRequestRequestTypeDef(BaseModel):
    domain: str
    domainOwner: Optional[str] = None
    administratorAccount: Optional[str] = None
    repositoryPrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RepositorySummaryTypeDef(BaseModel):
    name: Optional[str] = None
    administratorAccount: Optional[str] = None
    domainName: Optional[str] = None
    domainOwner: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    createdTime: Optional[datetime] = None

class ListRepositoriesRequestRequestTypeDef(BaseModel):
    repositoryPrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSubPackageGroupsRequestRequestTypeDef(BaseModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class PackageGroupAllowedRepositoryTypeDef(BaseModel):
    repositoryName: Optional[str] = None
    originRestrictionType: Optional[PackageGroupOriginRestrictionTypeType] = None

class PackageGroupReferenceTypeDef(BaseModel):
    arn: Optional[str] = None
    pattern: Optional[str] = None

class PackageOriginRestrictionsTypeDef(BaseModel):
    publish: AllowPublishType
    upstream: AllowUpstreamType

class PutDomainPermissionsPolicyRequestRequestTypeDef(BaseModel):
    domain: str
    policyDocument: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None

class PutRepositoryPermissionsPolicyRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    policyDocument: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None

class RepositoryExternalConnectionInfoTypeDef(BaseModel):
    externalConnectionName: Optional[str] = None
    packageFormat: Optional[PackageFormatType] = None
    status: Optional[Literal["Available"]] = None

class UpstreamRepositoryInfoTypeDef(BaseModel):
    repositoryName: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdatePackageGroupRequestRequestTypeDef(BaseModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None

class UpdatePackageVersionsStatusRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    versions: Sequence[str]
    targetStatus: PackageVersionStatusType
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    versionRevisions: Optional[Mapping[str, str]] = None
    expectedStatus: Optional[PackageVersionStatusType] = None

class GetAuthorizationTokenResultTypeDef(BaseModel):
    authorizationToken: str
    expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPackageVersionAssetResultTypeDef(BaseModel):
    asset: StreamingBody
    assetName: str
    packageVersion: str
    packageVersionRevision: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPackageVersionReadmeResultTypeDef(BaseModel):
    format: PackageFormatType
    namespace: str
    package: str
    version: str
    versionRevision: str
    readme: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryEndpointResultTypeDef(BaseModel):
    repositoryEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAllowedRepositoriesForGroupResultTypeDef(BaseModel):
    allowedRepositories: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackageVersionAssetsResultTypeDef(BaseModel):
    format: PackageFormatType
    namespace: str
    package: str
    version: str
    versionRevision: str
    nextToken: str
    assets: List[AssetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PublishPackageVersionResultTypeDef(BaseModel):
    format: PackageFormatType
    namespace: str
    package: str
    version: str
    versionRevision: str
    status: PackageVersionStatusType
    asset: AssetSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedPackagesResultTypeDef(BaseModel):
    packages: List[AssociatedPackageTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PublishPackageVersionRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    assetContent: BlobTypeDef
    assetName: str
    assetSHA256: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    unfinished: Optional[bool] = None

class CopyPackageVersionsResultTypeDef(BaseModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfoTypeDef]
    failedVersions: Dict[str, PackageVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePackageVersionsResultTypeDef(BaseModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfoTypeDef]
    failedVersions: Dict[str, PackageVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisposePackageVersionsResultTypeDef(BaseModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfoTypeDef]
    failedVersions: Dict[str, PackageVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackageVersionsStatusResultTypeDef(BaseModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfoTypeDef]
    failedVersions: Dict[str, PackageVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainRequestRequestTypeDef(BaseModel):
    domain: str
    encryptionKey: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreatePackageGroupRequestRequestTypeDef(BaseModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResultTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateDomainResultTypeDef(BaseModel):
    domain: DomainDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResultTypeDef(BaseModel):
    domain: DomainDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainResultTypeDef(BaseModel):
    domain: DomainDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    description: Optional[str] = None
    upstreams: Optional[Sequence[UpstreamRepositoryTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateRepositoryRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    description: Optional[str] = None
    upstreams: Optional[Sequence[UpstreamRepositoryTypeDef]] = None

class DeleteDomainPermissionsPolicyResultTypeDef(BaseModel):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryPermissionsPolicyResultTypeDef(BaseModel):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainPermissionsPolicyResultTypeDef(BaseModel):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryPermissionsPolicyResultTypeDef(BaseModel):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDomainPermissionsPolicyResultTypeDef(BaseModel):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutRepositoryPermissionsPolicyResultTypeDef(BaseModel):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PackageVersionOriginTypeDef(BaseModel):
    domainEntryPoint: Optional[DomainEntryPointTypeDef] = None
    originType: Optional[PackageVersionOriginTypeType] = None

class ListDomainsResultTypeDef(BaseModel):
    domains: List[DomainSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAllowedRepositoriesForGroupRequestListAllowedRepositoriesForGroupPaginateTypeDef(BaseModel):
    domain: str
    packageGroup: str
    originRestrictionType: PackageGroupOriginRestrictionTypeType
    domainOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedPackagesRequestListAssociatedPackagesPaginateTypeDef(BaseModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    preview: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainsRequestListDomainsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackageGroupsRequestListPackageGroupsPaginateTypeDef(BaseModel):
    domain: str
    domainOwner: Optional[str] = None
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackageVersionsRequestListPackageVersionsPaginateTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    status: Optional[PackageVersionStatusType] = None
    sortBy: Optional[Literal["PUBLISHED_TIME"]] = None
    originType: Optional[PackageVersionOriginTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackagesRequestListPackagesPaginateTypeDef(BaseModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    packagePrefix: Optional[str] = None
    publish: Optional[AllowPublishType] = None
    upstream: Optional[AllowUpstreamType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef(BaseModel):
    domain: str
    domainOwner: Optional[str] = None
    administratorAccount: Optional[str] = None
    repositoryPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRepositoriesRequestListRepositoriesPaginateTypeDef(BaseModel):
    repositoryPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubPackageGroupsRequestListSubPackageGroupsPaginateTypeDef(BaseModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackageVersionDependenciesResultTypeDef(BaseModel):
    format: PackageFormatType
    namespace: str
    package: str
    version: str
    versionRevision: str
    nextToken: str
    dependencies: List[PackageDependencyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositoriesInDomainResultTypeDef(BaseModel):
    repositories: List[RepositorySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositoriesResultTypeDef(BaseModel):
    repositories: List[RepositorySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackageGroupOriginConfigurationRequestRequestTypeDef(BaseModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    restrictions: Optional[       Mapping[PackageGroupOriginRestrictionTypeType, PackageGroupOriginRestrictionModeType] = None
    addAllowedRepositories: Optional[Sequence[PackageGroupAllowedRepositoryTypeDef]] = None
    removeAllowedRepositories: Optional[Sequence[PackageGroupAllowedRepositoryTypeDef]] = None

class PackageGroupOriginRestrictionTypeDef(BaseModel):
    mode: Optional[PackageGroupOriginRestrictionModeType] = None
    effectiveMode: Optional[PackageGroupOriginRestrictionModeType] = None
    inheritedFrom: Optional[PackageGroupReferenceTypeDef] = None
    repositoriesCount: Optional[int] = None

class PackageOriginConfigurationTypeDef(BaseModel):
    restrictions: Optional[PackageOriginRestrictionsTypeDef] = None

class PutPackageOriginConfigurationRequestRequestTypeDef(BaseModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    restrictions: PackageOriginRestrictionsTypeDef
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None

class RepositoryDescriptionTypeDef(BaseModel):
    name: Optional[str] = None
    administratorAccount: Optional[str] = None
    domainName: Optional[str] = None
    domainOwner: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    upstreams: Optional[List[UpstreamRepositoryInfoTypeDef]] = None
    externalConnections: Optional[List[RepositoryExternalConnectionInfoTypeDef]] = None
    createdTime: Optional[datetime] = None

class PackageVersionDescriptionTypeDef(BaseModel):
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    packageName: Optional[str] = None
    displayName: Optional[str] = None
    version: Optional[str] = None
    summary: Optional[str] = None
    homePage: Optional[str] = None
    sourceCodeRepository: Optional[str] = None
    publishedTime: Optional[datetime] = None
    licenses: Optional[List[LicenseInfoTypeDef]] = None
    revision: Optional[str] = None
    status: Optional[PackageVersionStatusType] = None
    origin: Optional[PackageVersionOriginTypeDef] = None

class PackageVersionSummaryTypeDef(BaseModel):
    version: str
    status: PackageVersionStatusType
    revision: Optional[str] = None
    origin: Optional[PackageVersionOriginTypeDef] = None

class PackageGroupOriginConfigurationTypeDef(BaseModel):
    restrictions: Optional[       Dict[PackageGroupOriginRestrictionTypeType, PackageGroupOriginRestrictionTypeDef] = None

class PackageDescriptionTypeDef(BaseModel):
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    name: Optional[str] = None
    originConfiguration: Optional[PackageOriginConfigurationTypeDef] = None

class PackageSummaryTypeDef(BaseModel):
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    package: Optional[str] = None
    originConfiguration: Optional[PackageOriginConfigurationTypeDef] = None

class PutPackageOriginConfigurationResultTypeDef(BaseModel):
    originConfiguration: PackageOriginConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateExternalConnectionResultTypeDef(BaseModel):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryResultTypeDef(BaseModel):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryResultTypeDef(BaseModel):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRepositoryResultTypeDef(BaseModel):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateExternalConnectionResultTypeDef(BaseModel):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRepositoryResultTypeDef(BaseModel):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackageVersionResultTypeDef(BaseModel):
    packageVersion: PackageVersionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackageVersionsResultTypeDef(BaseModel):
    defaultDisplayVersion: str
    format: PackageFormatType
    namespace: str
    package: str
    versions: List[PackageVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PackageGroupDescriptionTypeDef(BaseModel):
    arn: Optional[str] = None
    pattern: Optional[str] = None
    domainName: Optional[str] = None
    domainOwner: Optional[str] = None
    createdTime: Optional[datetime] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None
    originConfiguration: Optional[PackageGroupOriginConfigurationTypeDef] = None
    parent: Optional[PackageGroupReferenceTypeDef] = None

class PackageGroupSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    pattern: Optional[str] = None
    domainName: Optional[str] = None
    domainOwner: Optional[str] = None
    createdTime: Optional[datetime] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None
    originConfiguration: Optional[PackageGroupOriginConfigurationTypeDef] = None
    parent: Optional[PackageGroupReferenceTypeDef] = None

class DescribePackageResultTypeDef(BaseModel):
    package: PackageDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePackageResultTypeDef(BaseModel):
    deletedPackage: PackageSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackagesResultTypeDef(BaseModel):
    packages: List[PackageSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePackageGroupResultTypeDef(BaseModel):
    packageGroup: PackageGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePackageGroupResultTypeDef(BaseModel):
    packageGroup: PackageGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackageGroupResultTypeDef(BaseModel):
    packageGroup: PackageGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssociatedPackageGroupResultTypeDef(BaseModel):
    packageGroup: PackageGroupDescriptionTypeDef
    associationType: PackageGroupAssociationTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackageGroupOriginConfigurationResultTypeDef(BaseModel):
    packageGroup: PackageGroupDescriptionTypeDef
    allowedRepositoryUpdates: Dict[       PackageGroupOriginRestrictionTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackageGroupResultTypeDef(BaseModel):
    packageGroup: PackageGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackageGroupsResultTypeDef(BaseModel):
    packageGroups: List[PackageGroupSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubPackageGroupsResultTypeDef(BaseModel):
    packageGroups: List[PackageGroupSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

