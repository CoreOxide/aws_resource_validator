from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.codeartifact.codeartifact_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AssetSummary(BaseValidatorModel):
    name: str
    size: Optional[int] = None
    hashes: Optional[Dict[HashAlgorithmType, str]] = None


# This class is the input for the 'associate_external_connection' function.
class AssociateExternalConnectionRequest(BaseValidatorModel):
    domain: str
    repository: str
    externalConnection: str
    domainOwner: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AssociatedPackage(BaseValidatorModel):
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    package: Optional[str] = None
    associationType: Optional[PackageGroupAssociationTypeType] = None

Blob = Union[str, bytes, IO[Any], StreamingBody]


# This class is the input for the 'copy_package_versions' function.
class CopyPackageVersionsRequest(BaseValidatorModel):
    domain: str
    sourceRepository: str
    destinationRepository: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    versions: Optional[List[str]] = None
    versionRevisions: Optional[Dict[str, str]] = None
    allowOverwrite: Optional[bool] = None
    includeFromUpstream: Optional[bool] = None


class PackageVersionError(BaseValidatorModel):
    errorCode: Optional[PackageVersionErrorCodeType] = None
    errorMessage: Optional[str] = None


class SuccessfulPackageVersionInfo(BaseValidatorModel):
    revision: Optional[str] = None
    status: Optional[PackageVersionStatusType] = None


class Tag(BaseValidatorModel):
    key: str
    value: str


class DomainDescription(BaseValidatorModel):
    name: Optional[str] = None
    owner: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[DomainStatusType] = None
    createdTime: Optional[datetime] = None
    encryptionKey: Optional[str] = None
    repositoryCount: Optional[int] = None
    assetSizeBytes: Optional[int] = None
    s3BucketArn: Optional[str] = None


class UpstreamRepository(BaseValidatorModel):
    repositoryName: str


# This class is the input for the 'delete_domain_permissions_policy' function.
class DeleteDomainPermissionsPolicyRequest(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None


class ResourcePolicy(BaseValidatorModel):
    resourceArn: Optional[str] = None
    revision: Optional[str] = None
    document: Optional[str] = None


# This class is the input for the 'delete_domain' function.
class DeleteDomainRequest(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None


# This class is the input for the 'delete_package_group' function.
class DeletePackageGroupRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None


# This class is the input for the 'delete_package' function.
class DeletePackageRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None


# This class is the input for the 'delete_package_versions' function.
class DeletePackageVersionsRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    versions: List[str]
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    expectedStatus: Optional[PackageVersionStatusType] = None


# This class is the input for the 'delete_repository_permissions_policy' function.
class DeleteRepositoryPermissionsPolicyRequest(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None


# This class is the input for the 'delete_repository' function.
class DeleteRepositoryRequest(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None


# This class is the input for the 'describe_domain' function.
class DescribeDomainRequest(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None


# This class is the input for the 'describe_package_group' function.
class DescribePackageGroupRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None


# This class is the input for the 'describe_package' function.
class DescribePackageRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None


# This class is the input for the 'describe_package_version' function.
class DescribePackageVersionRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None


# This class is the input for the 'describe_repository' function.
class DescribeRepositoryRequest(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None


# This class is the input for the 'disassociate_external_connection' function.
class DisassociateExternalConnectionRequest(BaseValidatorModel):
    domain: str
    repository: str
    externalConnection: str
    domainOwner: Optional[str] = None


# This class is the input for the 'dispose_package_versions' function.
class DisposePackageVersionsRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    versions: List[str]
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    versionRevisions: Optional[Dict[str, str]] = None
    expectedStatus: Optional[PackageVersionStatusType] = None


class DomainEntryPoint(BaseValidatorModel):
    repositoryName: Optional[str] = None
    externalConnectionName: Optional[str] = None


class DomainSummary(BaseValidatorModel):
    name: Optional[str] = None
    owner: Optional[str] = None
    arn: Optional[str] = None
    status: Optional[DomainStatusType] = None
    createdTime: Optional[datetime] = None
    encryptionKey: Optional[str] = None


# This class is the input for the 'get_associated_package_group' function.
class GetAssociatedPackageGroupRequest(BaseValidatorModel):
    domain: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None


# This class is the input for the 'get_authorization_token' function.
class GetAuthorizationTokenRequest(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    durationSeconds: Optional[int] = None


# This class is the input for the 'get_domain_permissions_policy' function.
class GetDomainPermissionsPolicyRequest(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None


# This class is the input for the 'get_package_version_asset' function.
class GetPackageVersionAssetRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    asset: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    packageVersionRevision: Optional[str] = None


# This class is the input for the 'get_package_version_readme' function.
class GetPackageVersionReadmeRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None


# This class is the input for the 'get_repository_endpoint' function.
class GetRepositoryEndpointRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    domainOwner: Optional[str] = None
    endpointType: Optional[EndpointTypeType] = None


# This class is the input for the 'get_repository_permissions_policy' function.
class GetRepositoryPermissionsPolicyRequest(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None


class LicenseInfo(BaseValidatorModel):
    name: Optional[str] = None
    url: Optional[str] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_allowed_repositories_for_group' function.
class ListAllowedRepositoriesForGroupRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    originRestrictionType: PackageGroupOriginRestrictionTypeType
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_associated_packages' function.
class ListAssociatedPackagesRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    preview: Optional[bool] = None


# This class is the input for the 'list_domains' function.
class ListDomainsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_package_groups' function.
class ListPackageGroupsRequest(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    prefix: Optional[str] = None


# This class is the input for the 'list_package_version_assets' function.
class ListPackageVersionAssetsRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_package_version_dependencies' function.
class ListPackageVersionDependenciesRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    nextToken: Optional[str] = None


class PackageDependency(BaseValidatorModel):
    namespace: Optional[str] = None
    package: Optional[str] = None
    dependencyType: Optional[str] = None
    versionRequirement: Optional[str] = None


# This class is the input for the 'list_package_versions' function.
class ListPackageVersionsRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    status: Optional[PackageVersionStatusType] = None
    sortBy: Optional[Literal['PUBLISHED_TIME']] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    originType: Optional[PackageVersionOriginTypeType] = None


# This class is the input for the 'list_packages' function.
class ListPackagesRequest(BaseValidatorModel):
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


# This class is the input for the 'list_repositories_in_domain' function.
class ListRepositoriesInDomainRequest(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    administratorAccount: Optional[str] = None
    repositoryPrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class RepositorySummary(BaseValidatorModel):
    name: Optional[str] = None
    administratorAccount: Optional[str] = None
    domainName: Optional[str] = None
    domainOwner: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    createdTime: Optional[datetime] = None


# This class is the input for the 'list_repositories' function.
class ListRepositoriesRequest(BaseValidatorModel):
    repositoryPrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_sub_package_groups' function.
class ListSubPackageGroupsRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class PackageGroupAllowedRepository(BaseValidatorModel):
    repositoryName: Optional[str] = None
    originRestrictionType: Optional[PackageGroupOriginRestrictionTypeType] = None


class PackageGroupReference(BaseValidatorModel):
    arn: Optional[str] = None
    pattern: Optional[str] = None


class PackageOriginRestrictions(BaseValidatorModel):
    publish: AllowPublishType
    upstream: AllowUpstreamType


# This class is the input for the 'put_domain_permissions_policy' function.
class PutDomainPermissionsPolicyRequest(BaseValidatorModel):
    domain: str
    policyDocument: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None


# This class is the input for the 'put_repository_permissions_policy' function.
class PutRepositoryPermissionsPolicyRequest(BaseValidatorModel):
    domain: str
    repository: str
    policyDocument: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None


class RepositoryExternalConnectionInfo(BaseValidatorModel):
    externalConnectionName: Optional[str] = None
    packageFormat: Optional[PackageFormatType] = None
    status: Optional[Literal['Available']] = None


class UpstreamRepositoryInfo(BaseValidatorModel):
    repositoryName: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_package_group' function.
class UpdatePackageGroupRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None


# This class is the input for the 'update_package_versions_status' function.
class UpdatePackageVersionsStatusRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    versions: List[str]
    targetStatus: PackageVersionStatusType
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    versionRevisions: Optional[Dict[str, str]] = None
    expectedStatus: Optional[PackageVersionStatusType] = None


# This class is the output for the 'get_authorization_token' function.
class GetAuthorizationTokenResult(BaseValidatorModel):
    authorizationToken: str
    expiration: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_package_version_asset' function.
class GetPackageVersionAssetResult(BaseValidatorModel):
    asset: StreamingBody
    assetName: str
    packageVersion: str
    packageVersionRevision: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_package_version_readme' function.
class GetPackageVersionReadmeResult(BaseValidatorModel):
    format: PackageFormatType
    namespace: str
    package: str
    version: str
    versionRevision: str
    readme: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_repository_endpoint' function.
class GetRepositoryEndpointResult(BaseValidatorModel):
    repositoryEndpoint: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_allowed_repositories_for_group' function.
class ListAllowedRepositoriesForGroupResult(BaseValidatorModel):
    allowedRepositories: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_package_version_assets' function.
class ListPackageVersionAssetsResult(BaseValidatorModel):
    format: PackageFormatType
    namespace: str
    package: str
    version: str
    versionRevision: str
    assets: List[AssetSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'publish_package_version' function.
class PublishPackageVersionResult(BaseValidatorModel):
    format: PackageFormatType
    namespace: str
    package: str
    version: str
    versionRevision: str
    status: PackageVersionStatusType
    asset: AssetSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_associated_packages' function.
class ListAssociatedPackagesResult(BaseValidatorModel):
    packages: List[AssociatedPackage]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'publish_package_version' function.
class PublishPackageVersionRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    assetContent: Blob
    assetName: str
    assetSHA256: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    unfinished: Optional[bool] = None


# This class is the output for the 'copy_package_versions' function.
class CopyPackageVersionsResult(BaseValidatorModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfo]
    failedVersions: Dict[str, PackageVersionError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_package_versions' function.
class DeletePackageVersionsResult(BaseValidatorModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfo]
    failedVersions: Dict[str, PackageVersionError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'dispose_package_versions' function.
class DisposePackageVersionsResult(BaseValidatorModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfo]
    failedVersions: Dict[str, PackageVersionError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_package_versions_status' function.
class UpdatePackageVersionsStatusResult(BaseValidatorModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfo]
    failedVersions: Dict[str, PackageVersionError]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_domain' function.
class CreateDomainRequest(BaseValidatorModel):
    domain: str
    encryptionKey: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'create_package_group' function.
class CreatePackageGroupRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[Tag]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResult(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: List[Tag]


# This class is the output for the 'create_domain' function.
class CreateDomainResult(BaseValidatorModel):
    domain: DomainDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_domain' function.
class DeleteDomainResult(BaseValidatorModel):
    domain: DomainDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_domain' function.
class DescribeDomainResult(BaseValidatorModel):
    domain: DomainDescription
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_repository' function.
class CreateRepositoryRequest(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    description: Optional[str] = None
    upstreams: Optional[List[UpstreamRepository]] = None
    tags: Optional[List[Tag]] = None


# This class is the input for the 'update_repository' function.
class UpdateRepositoryRequest(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    description: Optional[str] = None
    upstreams: Optional[List[UpstreamRepository]] = None


# This class is the output for the 'delete_domain_permissions_policy' function.
class DeleteDomainPermissionsPolicyResult(BaseValidatorModel):
    policy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_repository_permissions_policy' function.
class DeleteRepositoryPermissionsPolicyResult(BaseValidatorModel):
    policy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_domain_permissions_policy' function.
class GetDomainPermissionsPolicyResult(BaseValidatorModel):
    policy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_repository_permissions_policy' function.
class GetRepositoryPermissionsPolicyResult(BaseValidatorModel):
    policy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_domain_permissions_policy' function.
class PutDomainPermissionsPolicyResult(BaseValidatorModel):
    policy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_repository_permissions_policy' function.
class PutRepositoryPermissionsPolicyResult(BaseValidatorModel):
    policy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


class PackageVersionOrigin(BaseValidatorModel):
    domainEntryPoint: Optional[DomainEntryPoint] = None
    originType: Optional[PackageVersionOriginTypeType] = None


# This class is the output for the 'list_domains' function.
class ListDomainsResult(BaseValidatorModel):
    domains: List[DomainSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAllowedRepositoriesForGroupRequestPaginate(BaseValidatorModel):
    domain: str
    packageGroup: str
    originRestrictionType: PackageGroupOriginRestrictionTypeType
    domainOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssociatedPackagesRequestPaginate(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    preview: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDomainsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPackageGroupsRequestPaginate(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPackageVersionAssetsRequestPaginate(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    packageVersion: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPackageVersionsRequestPaginate(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None
    status: Optional[PackageVersionStatusType] = None
    sortBy: Optional[Literal['PUBLISHED_TIME']] = None
    originType: Optional[PackageVersionOriginTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPackagesRequestPaginate(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    packagePrefix: Optional[str] = None
    publish: Optional[AllowPublishType] = None
    upstream: Optional[AllowUpstreamType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRepositoriesInDomainRequestPaginate(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    administratorAccount: Optional[str] = None
    repositoryPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRepositoriesRequestPaginate(BaseValidatorModel):
    repositoryPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubPackageGroupsRequestPaginate(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the output for the 'list_package_version_dependencies' function.
class ListPackageVersionDependenciesResult(BaseValidatorModel):
    format: PackageFormatType
    namespace: str
    package: str
    version: str
    versionRevision: str
    dependencies: List[PackageDependency]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_repositories_in_domain' function.
class ListRepositoriesInDomainResult(BaseValidatorModel):
    repositories: List[RepositorySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_repositories' function.
class ListRepositoriesResult(BaseValidatorModel):
    repositories: List[RepositorySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'update_package_group_origin_configuration' function.
class UpdatePackageGroupOriginConfigurationRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    restrictions: Optional[Dict[PackageGroupOriginRestrictionTypeType, PackageGroupOriginRestrictionModeType]] = None
    addAllowedRepositories: Optional[List[PackageGroupAllowedRepository]] = None
    removeAllowedRepositories: Optional[List[PackageGroupAllowedRepository]] = None


class PackageGroupOriginRestriction(BaseValidatorModel):
    mode: Optional[PackageGroupOriginRestrictionModeType] = None
    effectiveMode: Optional[PackageGroupOriginRestrictionModeType] = None
    inheritedFrom: Optional[PackageGroupReference] = None
    repositoriesCount: Optional[int] = None


class PackageOriginConfiguration(BaseValidatorModel):
    restrictions: Optional[PackageOriginRestrictions] = None


# This class is the input for the 'put_package_origin_configuration' function.
class PutPackageOriginConfigurationRequest(BaseValidatorModel):
    domain: str
    repository: str
    format: PackageFormatType
    package: str
    restrictions: PackageOriginRestrictions
    domainOwner: Optional[str] = None
    namespace: Optional[str] = None


class RepositoryDescription(BaseValidatorModel):
    name: Optional[str] = None
    administratorAccount: Optional[str] = None
    domainName: Optional[str] = None
    domainOwner: Optional[str] = None
    arn: Optional[str] = None
    description: Optional[str] = None
    upstreams: Optional[List[UpstreamRepositoryInfo]] = None
    externalConnections: Optional[List[RepositoryExternalConnectionInfo]] = None
    createdTime: Optional[datetime] = None


class PackageVersionDescription(BaseValidatorModel):
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    packageName: Optional[str] = None
    displayName: Optional[str] = None
    version: Optional[str] = None
    summary: Optional[str] = None
    homePage: Optional[str] = None
    sourceCodeRepository: Optional[str] = None
    publishedTime: Optional[datetime] = None
    licenses: Optional[List[LicenseInfo]] = None
    revision: Optional[str] = None
    status: Optional[PackageVersionStatusType] = None
    origin: Optional[PackageVersionOrigin] = None


class PackageVersionSummary(BaseValidatorModel):
    version: str
    status: PackageVersionStatusType
    revision: Optional[str] = None
    origin: Optional[PackageVersionOrigin] = None


class PackageGroupOriginConfiguration(BaseValidatorModel):
    restrictions: Optional[Dict[PackageGroupOriginRestrictionTypeType, PackageGroupOriginRestriction]] = None


class PackageDescription(BaseValidatorModel):
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    name: Optional[str] = None
    originConfiguration: Optional[PackageOriginConfiguration] = None


class PackageSummary(BaseValidatorModel):
    format: Optional[PackageFormatType] = None
    namespace: Optional[str] = None
    package: Optional[str] = None
    originConfiguration: Optional[PackageOriginConfiguration] = None


# This class is the output for the 'put_package_origin_configuration' function.
class PutPackageOriginConfigurationResult(BaseValidatorModel):
    originConfiguration: PackageOriginConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_external_connection' function.
class AssociateExternalConnectionResult(BaseValidatorModel):
    repository: RepositoryDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_repository' function.
class CreateRepositoryResult(BaseValidatorModel):
    repository: RepositoryDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_repository' function.
class DeleteRepositoryResult(BaseValidatorModel):
    repository: RepositoryDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_repository' function.
class DescribeRepositoryResult(BaseValidatorModel):
    repository: RepositoryDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'disassociate_external_connection' function.
class DisassociateExternalConnectionResult(BaseValidatorModel):
    repository: RepositoryDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_repository' function.
class UpdateRepositoryResult(BaseValidatorModel):
    repository: RepositoryDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_package_version' function.
class DescribePackageVersionResult(BaseValidatorModel):
    packageVersion: PackageVersionDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_package_versions' function.
class ListPackageVersionsResult(BaseValidatorModel):
    defaultDisplayVersion: str
    format: PackageFormatType
    namespace: str
    package: str
    versions: List[PackageVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PackageGroupDescription(BaseValidatorModel):
    arn: Optional[str] = None
    pattern: Optional[str] = None
    domainName: Optional[str] = None
    domainOwner: Optional[str] = None
    createdTime: Optional[datetime] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None
    originConfiguration: Optional[PackageGroupOriginConfiguration] = None
    parent: Optional[PackageGroupReference] = None


class PackageGroupSummary(BaseValidatorModel):
    arn: Optional[str] = None
    pattern: Optional[str] = None
    domainName: Optional[str] = None
    domainOwner: Optional[str] = None
    createdTime: Optional[datetime] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None
    originConfiguration: Optional[PackageGroupOriginConfiguration] = None
    parent: Optional[PackageGroupReference] = None


# This class is the output for the 'describe_package' function.
class DescribePackageResult(BaseValidatorModel):
    package: PackageDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_package' function.
class DeletePackageResult(BaseValidatorModel):
    deletedPackage: PackageSummary
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_packages' function.
class ListPackagesResult(BaseValidatorModel):
    packages: List[PackageSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_package_group' function.
class CreatePackageGroupResult(BaseValidatorModel):
    packageGroup: PackageGroupDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_package_group' function.
class DeletePackageGroupResult(BaseValidatorModel):
    packageGroup: PackageGroupDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_package_group' function.
class DescribePackageGroupResult(BaseValidatorModel):
    packageGroup: PackageGroupDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_associated_package_group' function.
class GetAssociatedPackageGroupResult(BaseValidatorModel):
    packageGroup: PackageGroupDescription
    associationType: PackageGroupAssociationTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_package_group_origin_configuration' function.
class UpdatePackageGroupOriginConfigurationResult(BaseValidatorModel):
    packageGroup: PackageGroupDescription
    allowedRepositoryUpdates: Dict[PackageGroupOriginRestrictionTypeType, Dict[PackageGroupAllowedRepositoryUpdateTypeType, List[str]]]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_package_group' function.
class UpdatePackageGroupResult(BaseValidatorModel):
    packageGroup: PackageGroupDescription
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_package_groups' function.
class ListPackageGroupsResult(BaseValidatorModel):
    packageGroups: List[PackageGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_sub_package_groups' function.
class ListSubPackageGroupsResult(BaseValidatorModel):
    packageGroups: List[PackageGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None