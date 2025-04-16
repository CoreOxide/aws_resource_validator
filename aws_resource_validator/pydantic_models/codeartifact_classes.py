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
from aws_resource_validator.pydantic_models.codeartifact_constants import *

class AssetSummary(BaseValidatorModel):
    name: str
    size: Optional[int] = None
    hashes: Optional[Dict[HashAlgorithmType, str]] = None


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


class DeleteDomainPermissionsPolicyRequest(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None


class ResourcePolicy(BaseValidatorModel):
    resourceArn: Optional[str] = None
    revision: Optional[str] = None
    document: Optional[str] = None


class DeleteDomainRequest(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None


class DeletePackageGroupRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None


class DeleteRepositoryPermissionsPolicyRequest(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None


class DeleteRepositoryRequest(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None


class DescribeDomainRequest(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None


class DescribePackageGroupRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None


class DescribeRepositoryRequest(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None


class DisassociateExternalConnectionRequest(BaseValidatorModel):
    domain: str
    repository: str
    externalConnection: str
    domainOwner: Optional[str] = None


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


class GetAuthorizationTokenRequest(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    durationSeconds: Optional[int] = None


class GetDomainPermissionsPolicyRequest(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None


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


class ListAllowedRepositoriesForGroupRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    originRestrictionType: PackageGroupOriginRestrictionTypeType
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAssociatedPackagesRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    preview: Optional[bool] = None


class ListDomainsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListPackageGroupsRequest(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    prefix: Optional[str] = None


class PackageDependency(BaseValidatorModel):
    namespace: Optional[str] = None
    package: Optional[str] = None
    dependencyType: Optional[str] = None
    versionRequirement: Optional[str] = None


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


class ListRepositoriesRequest(BaseValidatorModel):
    repositoryPrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSubPackageGroupsRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


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


class PutDomainPermissionsPolicyRequest(BaseValidatorModel):
    domain: str
    policyDocument: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None


class PutRepositoryPermissionsPolicyRequest(BaseValidatorModel):
    domain: str
    repository: str
    policyDocument: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None


class RepositoryExternalConnectionInfo(BaseValidatorModel):
    externalConnectionName: Optional[str] = None
    packageFormat: Optional[PackageFormatType] = None
    status: Optional[Literal["Available"]] = None


class UpstreamRepositoryInfo(BaseValidatorModel):
    repositoryName: Optional[str] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdatePackageGroupRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None


class GetAuthorizationTokenResult(BaseValidatorModel):
    authorizationToken: str
    expiration: datetime
    ResponseMetadata: ResponseMetadata


class GetPackageVersionAssetResult(BaseValidatorModel):
    asset: StreamingBody
    assetName: str
    packageVersion: str
    packageVersionRevision: str
    ResponseMetadata: ResponseMetadata


class GetRepositoryEndpointResult(BaseValidatorModel):
    repositoryEndpoint: str
    ResponseMetadata: ResponseMetadata


class ListAllowedRepositoriesForGroupResult(BaseValidatorModel):
    allowedRepositories: List[str]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AssociatedPackage(BaseValidatorModel):
    pass


class ListAssociatedPackagesResult(BaseValidatorModel):
    packages: List[AssociatedPackage]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CopyPackageVersionsResult(BaseValidatorModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfo]
    failedVersions: Dict[str, PackageVersionError]
    ResponseMetadata: ResponseMetadata


class DeletePackageVersionsResult(BaseValidatorModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfo]
    failedVersions: Dict[str, PackageVersionError]
    ResponseMetadata: ResponseMetadata


class DisposePackageVersionsResult(BaseValidatorModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfo]
    failedVersions: Dict[str, PackageVersionError]
    ResponseMetadata: ResponseMetadata


class UpdatePackageVersionsStatusResult(BaseValidatorModel):
    successfulVersions: Dict[str, SuccessfulPackageVersionInfo]
    failedVersions: Dict[str, PackageVersionError]
    ResponseMetadata: ResponseMetadata


class CreateDomainRequest(BaseValidatorModel):
    domain: str
    encryptionKey: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class CreatePackageGroupRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class ListTagsForResourceResult(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Sequence[Tag]


class CreateDomainResult(BaseValidatorModel):
    domain: DomainDescription
    ResponseMetadata: ResponseMetadata


class DeleteDomainResult(BaseValidatorModel):
    domain: DomainDescription
    ResponseMetadata: ResponseMetadata


class DescribeDomainResult(BaseValidatorModel):
    domain: DomainDescription
    ResponseMetadata: ResponseMetadata


class CreateRepositoryRequest(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    description: Optional[str] = None
    upstreams: Optional[Sequence[UpstreamRepository]] = None
    tags: Optional[Sequence[Tag]] = None


class UpdateRepositoryRequest(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    description: Optional[str] = None
    upstreams: Optional[Sequence[UpstreamRepository]] = None


class DeleteDomainPermissionsPolicyResult(BaseValidatorModel):
    policy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


class DeleteRepositoryPermissionsPolicyResult(BaseValidatorModel):
    policy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


class GetDomainPermissionsPolicyResult(BaseValidatorModel):
    policy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


class GetRepositoryPermissionsPolicyResult(BaseValidatorModel):
    policy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


class PutDomainPermissionsPolicyResult(BaseValidatorModel):
    policy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


class PutRepositoryPermissionsPolicyResult(BaseValidatorModel):
    policy: ResourcePolicy
    ResponseMetadata: ResponseMetadata


class PackageVersionOrigin(BaseValidatorModel):
    domainEntryPoint: Optional[DomainEntryPoint] = None
    originType: Optional[PackageVersionOriginTypeType] = None


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


class ListRepositoriesInDomainResult(BaseValidatorModel):
    repositories: List[RepositorySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListRepositoriesResult(BaseValidatorModel):
    repositories: List[RepositorySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UpdatePackageGroupOriginConfigurationRequest(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    restrictions: Optional[ Mapping[PackageGroupOriginRestrictionTypeType, PackageGroupOriginRestrictionModeType] ] = None
    addAllowedRepositories: Optional[Sequence[PackageGroupAllowedRepository]] = None
    removeAllowedRepositories: Optional[Sequence[PackageGroupAllowedRepository]] = None


class PackageGroupOriginRestriction(BaseValidatorModel):
    mode: Optional[PackageGroupOriginRestrictionModeType] = None
    effectiveMode: Optional[PackageGroupOriginRestrictionModeType] = None
    inheritedFrom: Optional[PackageGroupReference] = None
    repositoriesCount: Optional[int] = None


class PackageOriginConfiguration(BaseValidatorModel):
    restrictions: Optional[PackageOriginRestrictions] = None


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


class PackageVersionSummary(BaseValidatorModel):
    version: str
    status: PackageVersionStatusType
    revision: Optional[str] = None
    origin: Optional[PackageVersionOrigin] = None


class PackageGroupOriginConfiguration(BaseValidatorModel):
    restrictions: Optional[ Dict[PackageGroupOriginRestrictionTypeType, PackageGroupOriginRestriction] ] = None


class PutPackageOriginConfigurationResult(BaseValidatorModel):
    originConfiguration: PackageOriginConfiguration
    ResponseMetadata: ResponseMetadata


class AssociateExternalConnectionResult(BaseValidatorModel):
    repository: RepositoryDescription
    ResponseMetadata: ResponseMetadata


class CreateRepositoryResult(BaseValidatorModel):
    repository: RepositoryDescription
    ResponseMetadata: ResponseMetadata


class DeleteRepositoryResult(BaseValidatorModel):
    repository: RepositoryDescription
    ResponseMetadata: ResponseMetadata


class DescribeRepositoryResult(BaseValidatorModel):
    repository: RepositoryDescription
    ResponseMetadata: ResponseMetadata


class DisassociateExternalConnectionResult(BaseValidatorModel):
    repository: RepositoryDescription
    ResponseMetadata: ResponseMetadata


class UpdateRepositoryResult(BaseValidatorModel):
    repository: RepositoryDescription
    ResponseMetadata: ResponseMetadata


class PackageVersionDescription(BaseValidatorModel):
    pass


class DescribePackageVersionResult(BaseValidatorModel):
    packageVersion: PackageVersionDescription
    ResponseMetadata: ResponseMetadata


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


class PackageDescription(BaseValidatorModel):
    pass


class DescribePackageResult(BaseValidatorModel):
    package: PackageDescription
    ResponseMetadata: ResponseMetadata


class PackageSummary(BaseValidatorModel):
    pass


class DeletePackageResult(BaseValidatorModel):
    deletedPackage: PackageSummary
    ResponseMetadata: ResponseMetadata


class ListPackagesResult(BaseValidatorModel):
    packages: List[PackageSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreatePackageGroupResult(BaseValidatorModel):
    packageGroup: PackageGroupDescription
    ResponseMetadata: ResponseMetadata


class DeletePackageGroupResult(BaseValidatorModel):
    packageGroup: PackageGroupDescription
    ResponseMetadata: ResponseMetadata


class DescribePackageGroupResult(BaseValidatorModel):
    packageGroup: PackageGroupDescription
    ResponseMetadata: ResponseMetadata


class GetAssociatedPackageGroupResult(BaseValidatorModel):
    packageGroup: PackageGroupDescription
    associationType: PackageGroupAssociationTypeType
    ResponseMetadata: ResponseMetadata


class UpdatePackageGroupOriginConfigurationResult(BaseValidatorModel):
    packageGroup: PackageGroupDescription
    allowedRepositoryUpdates: Dict[ PackageGroupOriginRestrictionTypeType, Dict[PackageGroupAllowedRepositoryUpdateTypeType, List[str]], ]
    ResponseMetadata: ResponseMetadata


class UpdatePackageGroupResult(BaseValidatorModel):
    packageGroup: PackageGroupDescription
    ResponseMetadata: ResponseMetadata


class ListPackageGroupsResult(BaseValidatorModel):
    packageGroups: List[PackageGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListSubPackageGroupsResult(BaseValidatorModel):
    packageGroups: List[PackageGroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


