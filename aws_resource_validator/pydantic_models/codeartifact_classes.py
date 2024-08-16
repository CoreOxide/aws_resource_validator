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
from aws_resource_validator.pydantic_models.codeartifact_constants import *

class AssetSummaryTypeDef(BaseValidatorModel):
    name: str
    size: Optional[int] = None
    hashes: Optional[Dict[HashAlgorithmType, str]] = None

class AssociateExternalConnectionRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    externalConnection: str
    domainOwner: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class AssociatedPackageTypeDef(BaseValidatorModel):
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    package: Optional[str] = None
    associationType: Optional[PackageGroupAssociationTypeType] = None

class CopyPackageVersionsRequestRequestTypeDef(BaseValidatorModel):
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

class PackageVersionErrorTypeDef(BaseValidatorModel):
    errorCode: Optional[PackageVersionErrorCodeType] = None
    errorMessage: Optional[str] = None

class SuccessfulPackageVersionInfoTypeDef(BaseValidatorModel):
    revision: Optional[str] = None
    status: Optional[PackageVersionStatusType] = None

class TagTypeDef(BaseValidatorModel):
    key: str
    value: str

class DomainDescriptionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    owner: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[DomainStatusType] = None
    createdTime: Optional[datetime] = None
    encryptionKey: Optional[str] = None
    repositoryCount: Optional[int] = None
    assetSizeBytes: Optional[int] = None
    s3BucketArn: Optional[str] = None

class UpstreamRepositoryTypeDef(BaseValidatorModel):
    repositoryName: str

class DeleteDomainPermissionsPolicyRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None

class ResourcePolicyTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    revision: Optional[str] = None
    document: Optional[str] = None

class DeleteDomainRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None

class DeletePackageGroupRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None

class DeletePackageRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None

class DeletePackageVersionsRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    versions: Sequence[str]
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    expectedStatus: Optional[PackageVersionStatusType] = None

class DeleteRepositoryPermissionsPolicyRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None

class DeleteRepositoryRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None

class DescribeDomainRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None

class DescribePackageGroupRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None

class DescribePackageRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None

class DescribePackageVersionRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None

class DescribeRepositoryRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None

class DisassociateExternalConnectionRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    externalConnection: str
    domainOwner: Optional[str] = None

class DisposePackageVersionsRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    versions: Sequence[str]
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    versionRevisions: Optional[Mapping[str, str]] = None
    expectedStatus: Optional[PackageVersionStatusType] = None

class DomainEntryPointTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    externalConnectionName: Optional[str] = None

class DomainSummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    owner: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[DomainStatusType] = None
    createdTime: Optional[datetime] = None
    encryptionKey: Optional[str] = None

class GetAssociatedPackageGroupRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None

class GetAuthorizationTokenRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    durationSeconds: Optional[int] = None

class GetDomainPermissionsPolicyRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None

class GetPackageVersionAssetRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    asset: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    packageVersionRevision: Optional[str] = None

class GetPackageVersionReadmeRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None

class GetRepositoryEndpointRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    domainOwner: Optional[str] = None

class GetRepositoryPermissionsPolicyRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None

class LicenseInfoTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    url: Optional[str] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAllowedRepositoriesForGroupRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    originRestrictionType: PackageGroupOriginRestrictionTypeType
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAssociatedPackagesRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    preview: Optional[bool] = None

class ListDomainsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListPackageGroupsRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    prefix: Optional[str] = None

class ListPackageVersionAssetsRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListPackageVersionDependenciesRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    nextToken: Optional[str] = None

class PackageDependencyTypeDef(BaseValidatorModel):
    namespace: Optional[str] = None
    package: Optional[str] = None
    dependencyType: Optional[str] = None
    versionRequirement: Optional[str] = None

class ListPackageVersionsRequestRequestTypeDef(BaseValidatorModel):
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

class ListPackagesRequestRequestTypeDef(BaseValidatorModel):
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

class ListRepositoriesInDomainRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    administratorAccount: Optional[str] = None
    repositoryPrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class RepositorySummaryTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    administratorAccount: Optional[str] = None
    domainName: Optional[str] = None
    domainOwner: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    createdTime: Optional[datetime] = None

class ListRepositoriesRequestRequestTypeDef(BaseValidatorModel):
    repositoryPrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListSubPackageGroupsRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class PackageGroupAllowedRepositoryTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None
    originRestrictionType: Optional[PackageGroupOriginRestrictionTypeType] = None

class PackageGroupReferenceTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    pattern: Optional[str] = None

class PackageOriginRestrictionsTypeDef(BaseValidatorModel):
    publish: AllowPublishType
    upstream: AllowUpstreamType

class PutDomainPermissionsPolicyRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    policyDocument: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None

class PutRepositoryPermissionsPolicyRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    policyDocument: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None

class RepositoryExternalConnectionInfoTypeDef(BaseValidatorModel):
    externalConnectionName: Optional[str] = None
    packageFormat: Optional[PackageFormatType] = None
    status: Optional[Literal["Available"]] = None

class UpstreamRepositoryInfoTypeDef(BaseValidatorModel):
    repositoryName: Optional[str] = None

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdatePackageGroupRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None

class UpdatePackageVersionsStatusRequestRequestTypeDef(BaseValidatorModel):
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

class GetAuthorizationTokenResultTypeDef(BaseValidatorModel):
    authorizationToken: str
    expiration: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class GetPackageVersionAssetResultTypeDef(BaseValidatorModel):
    asset: StreamingBody
    assetName: str
    packageVersion: str
    packageVersionRevision: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetPackageVersionReadmeResultTypeDef(BaseValidatorModel):
    format: PackageFormatType
    namespace: str
    package: str
    version: str
    versionRevision: str
    readme: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryEndpointResultTypeDef(BaseValidatorModel):
    repositoryEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAllowedRepositoriesForGroupResultTypeDef(BaseValidatorModel):
    allowedRepositories: List[str]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackageVersionAssetsResultTypeDef(BaseValidatorModel):
    format: PackageFormatType
    namespace: str
    package: str
    version: str
    versionRevision: str
    nextToken: str
    assets: List[AssetSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PublishPackageVersionResultTypeDef(BaseValidatorModel):
    format: PackageFormatType
    namespace: str
    package: str
    version: str
    versionRevision: str
    status: PackageVersionStatusType
    asset: AssetSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssociatedPackagesResultTypeDef(BaseValidatorModel):
    packages: List[AssociatedPackageTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PublishPackageVersionRequestRequestTypeDef(BaseValidatorModel):
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

class CopyPackageVersionsResultTypeDef(BaseValidatorModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfoTypeDef]
    failedVersions: Dict[str, PackageVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePackageVersionsResultTypeDef(BaseValidatorModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfoTypeDef]
    failedVersions: Dict[str, PackageVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisposePackageVersionsResultTypeDef(BaseValidatorModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfoTypeDef]
    failedVersions: Dict[str, PackageVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackageVersionsStatusResultTypeDef(BaseValidatorModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfoTypeDef]
    failedVersions: Dict[str, PackageVersionErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDomainRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    encryptionKey: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class CreatePackageGroupRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[TagTypeDef]

class CreateDomainResultTypeDef(BaseValidatorModel):
    domain: DomainDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteDomainResultTypeDef(BaseValidatorModel):
    domain: DomainDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeDomainResultTypeDef(BaseValidatorModel):
    domain: DomainDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    description: Optional[str] = None
    upstreams: Optional[Sequence[UpstreamRepositoryTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateRepositoryRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    description: Optional[str] = None
    upstreams: Optional[Sequence[UpstreamRepositoryTypeDef]] = None

class DeleteDomainPermissionsPolicyResultTypeDef(BaseValidatorModel):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryPermissionsPolicyResultTypeDef(BaseValidatorModel):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetDomainPermissionsPolicyResultTypeDef(BaseValidatorModel):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRepositoryPermissionsPolicyResultTypeDef(BaseValidatorModel):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutDomainPermissionsPolicyResultTypeDef(BaseValidatorModel):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutRepositoryPermissionsPolicyResultTypeDef(BaseValidatorModel):
    policy: ResourcePolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PackageVersionOriginTypeDef(BaseValidatorModel):
    domainEntryPoint: Optional[DomainEntryPointTypeDef] = None
    originType: Optional[PackageVersionOriginTypeType] = None

class ListDomainsResultTypeDef(BaseValidatorModel):
    domains: List[DomainSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAllowedRepositoriesForGroupRequestListAllowedRepositoriesForGroupPaginateTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    originRestrictionType: PackageGroupOriginRestrictionTypeType
    domainOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssociatedPackagesRequestListAssociatedPackagesPaginateTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    preview: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDomainsRequestListDomainsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackageGroupsRequestListPackageGroupsPaginateTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackageVersionsRequestListPackageVersionsPaginateTypeDef(BaseValidatorModel):
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

class ListPackagesRequestListPackagesPaginateTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    packagePrefix: Optional[str] = None
    publish: Optional[AllowPublishType] = None
    upstream: Optional[AllowUpstreamType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    administratorAccount: Optional[str] = None
    repositoryPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRepositoriesRequestListRepositoriesPaginateTypeDef(BaseValidatorModel):
    repositoryPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSubPackageGroupsRequestListSubPackageGroupsPaginateTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPackageVersionDependenciesResultTypeDef(BaseValidatorModel):
    format: PackageFormatType
    namespace: str
    package: str
    version: str
    versionRevision: str
    nextToken: str
    dependencies: List[PackageDependencyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositoriesInDomainResultTypeDef(BaseValidatorModel):
    repositories: List[RepositorySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListRepositoriesResultTypeDef(BaseValidatorModel):
    repositories: List[RepositorySummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackageGroupOriginConfigurationRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    restrictions: Optional[       Mapping[PackageGroupOriginRestrictionTypeType, PackageGroupOriginRestrictionModeType] = None
    addAllowedRepositories: Optional[Sequence[PackageGroupAllowedRepositoryTypeDef]] = None
    removeAllowedRepositories: Optional[Sequence[PackageGroupAllowedRepositoryTypeDef]] = None

class PackageGroupOriginRestrictionTypeDef(BaseValidatorModel):
    mode: Optional[PackageGroupOriginRestrictionModeType] = None
    effectiveMode: Optional[PackageGroupOriginRestrictionModeType] = None
    inheritedFrom: Optional[PackageGroupReferenceTypeDef] = None
    repositoriesCount: Optional[int] = None

class PackageOriginConfigurationTypeDef(BaseValidatorModel):
    restrictions: Optional[PackageOriginRestrictionsTypeDef] = None

class PutPackageOriginConfigurationRequestRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    restrictions: PackageOriginRestrictionsTypeDef
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None

class RepositoryDescriptionTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    administratorAccount: Optional[str] = None
    domainName: Optional[str] = None
    domainOwner: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    upstreams: Optional[List[UpstreamRepositoryInfoTypeDef]] = None
    externalConnections: Optional[List[RepositoryExternalConnectionInfoTypeDef]] = None
    createdTime: Optional[datetime] = None

class PackageVersionDescriptionTypeDef(BaseValidatorModel):
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

class PackageVersionSummaryTypeDef(BaseValidatorModel):
    version: str
    status: PackageVersionStatusType
    revision: Optional[str] = None
    origin: Optional[PackageVersionOriginTypeDef] = None

class PackageGroupOriginConfigurationTypeDef(BaseValidatorModel):
    restrictions: Optional[       Dict[PackageGroupOriginRestrictionTypeType, PackageGroupOriginRestrictionTypeDef] = None

class PackageDescriptionTypeDef(BaseValidatorModel):
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    name: Optional[str] = None
    originConfiguration: Optional[PackageOriginConfigurationTypeDef] = None

class PackageSummaryTypeDef(BaseValidatorModel):
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    package: Optional[str] = None
    originConfiguration: Optional[PackageOriginConfigurationTypeDef] = None

class PutPackageOriginConfigurationResultTypeDef(BaseValidatorModel):
    originConfiguration: PackageOriginConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateExternalConnectionResultTypeDef(BaseValidatorModel):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRepositoryResultTypeDef(BaseValidatorModel):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteRepositoryResultTypeDef(BaseValidatorModel):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeRepositoryResultTypeDef(BaseValidatorModel):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateExternalConnectionResultTypeDef(BaseValidatorModel):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRepositoryResultTypeDef(BaseValidatorModel):
    repository: RepositoryDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackageVersionResultTypeDef(BaseValidatorModel):
    packageVersion: PackageVersionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackageVersionsResultTypeDef(BaseValidatorModel):
    defaultDisplayVersion: str
    format: PackageFormatType
    namespace: str
    package: str
    versions: List[PackageVersionSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PackageGroupDescriptionTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    pattern: Optional[str] = None
    domainName: Optional[str] = None
    domainOwner: Optional[str] = None
    createdTime: Optional[datetime] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None
    originConfiguration: Optional[PackageGroupOriginConfigurationTypeDef] = None
    parent: Optional[PackageGroupReferenceTypeDef] = None

class PackageGroupSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    pattern: Optional[str] = None
    domainName: Optional[str] = None
    domainOwner: Optional[str] = None
    createdTime: Optional[datetime] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None
    originConfiguration: Optional[PackageGroupOriginConfigurationTypeDef] = None
    parent: Optional[PackageGroupReferenceTypeDef] = None

class DescribePackageResultTypeDef(BaseValidatorModel):
    package: PackageDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePackageResultTypeDef(BaseValidatorModel):
    deletedPackage: PackageSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackagesResultTypeDef(BaseValidatorModel):
    packages: List[PackageSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePackageGroupResultTypeDef(BaseValidatorModel):
    packageGroup: PackageGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DeletePackageGroupResultTypeDef(BaseValidatorModel):
    packageGroup: PackageGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribePackageGroupResultTypeDef(BaseValidatorModel):
    packageGroup: PackageGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssociatedPackageGroupResultTypeDef(BaseValidatorModel):
    packageGroup: PackageGroupDescriptionTypeDef
    associationType: PackageGroupAssociationTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackageGroupOriginConfigurationResultTypeDef(BaseValidatorModel):
    packageGroup: PackageGroupDescriptionTypeDef
    allowedRepositoryUpdates: Dict[       PackageGroupOriginRestrictionTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePackageGroupResultTypeDef(BaseValidatorModel):
    packageGroup: PackageGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPackageGroupsResultTypeDef(BaseValidatorModel):
    packageGroups: List[PackageGroupSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListSubPackageGroupsResultTypeDef(BaseValidatorModel):
    packageGroups: List[PackageGroupSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

