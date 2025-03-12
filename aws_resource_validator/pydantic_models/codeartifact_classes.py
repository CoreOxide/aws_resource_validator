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

class AssetSummaryTypeDef(BaseValidatorModel):
    name: str
    size: Optional[int] = None
    hashes: Optional[Dict[HashAlgorithmType, str]] = None


class AssociateExternalConnectionRequestTypeDef(BaseValidatorModel):
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


class DeleteDomainPermissionsPolicyRequestTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None


class ResourcePolicyTypeDef(BaseValidatorModel):
    resourceArn: Optional[str] = None
    revision: Optional[str] = None
    document: Optional[str] = None


class DeleteDomainRequestTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None


class DeletePackageGroupRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None


class DeleteRepositoryPermissionsPolicyRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None


class DeleteRepositoryRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None


class DescribeDomainRequestTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None


class DescribePackageGroupRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None


class DescribeRepositoryRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None


class DisassociateExternalConnectionRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    externalConnection: str
    domainOwner: Optional[str] = None


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


class GetAuthorizationTokenRequestTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    durationSeconds: Optional[int] = None


class GetDomainPermissionsPolicyRequestTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None


class GetRepositoryPermissionsPolicyRequestTypeDef(BaseValidatorModel):
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


class ListAllowedRepositoriesForGroupRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    originRestrictionType: PackageGroupOriginRestrictionTypeType
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAssociatedPackagesRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    preview: Optional[bool] = None


class ListDomainsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListPackageGroupsRequestTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    prefix: Optional[str] = None


class PackageDependencyTypeDef(BaseValidatorModel):
    namespace: Optional[str] = None
    package: Optional[str] = None
    dependencyType: Optional[str] = None
    versionRequirement: Optional[str] = None


class ListRepositoriesInDomainRequestTypeDef(BaseValidatorModel):
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


class ListRepositoriesRequestTypeDef(BaseValidatorModel):
    repositoryPrefix: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListSubPackageGroupsRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
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


class PutDomainPermissionsPolicyRequestTypeDef(BaseValidatorModel):
    domain: str
    policyDocument: str
    domainOwner: Optional[str] = None
    policyRevision: Optional[str] = None


class PutRepositoryPermissionsPolicyRequestTypeDef(BaseValidatorModel):
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


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdatePackageGroupRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None


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


class GetRepositoryEndpointResultTypeDef(BaseValidatorModel):
    repositoryEndpoint: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListAllowedRepositoriesForGroupResultTypeDef(BaseValidatorModel):
    allowedRepositories: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AssociatedPackageTypeDef(BaseValidatorModel):
    pass


class ListAssociatedPackagesResultTypeDef(BaseValidatorModel):
    packages: List[AssociatedPackageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class CreateDomainRequestTypeDef(BaseValidatorModel):
    domain: str
    encryptionKey: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class CreatePackageGroupRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    contactInfo: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class ListTagsForResourceResultTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
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


class CreateRepositoryRequestTypeDef(BaseValidatorModel):
    domain: str
    repository: str
    domainOwner: Optional[str] = None
    description: Optional[str] = None
    upstreams: Optional[Sequence[UpstreamRepositoryTypeDef]] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateRepositoryRequestTypeDef(BaseValidatorModel):
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAllowedRepositoriesForGroupRequestPaginateTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    originRestrictionType: PackageGroupOriginRestrictionTypeType
    domainOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssociatedPackagesRequestPaginateTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    preview: Optional[bool] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDomainsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPackageGroupsRequestPaginateTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    prefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRepositoriesInDomainRequestPaginateTypeDef(BaseValidatorModel):
    domain: str
    domainOwner: Optional[str] = None
    administratorAccount: Optional[str] = None
    repositoryPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRepositoriesRequestPaginateTypeDef(BaseValidatorModel):
    repositoryPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSubPackageGroupsRequestPaginateTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRepositoriesInDomainResultTypeDef(BaseValidatorModel):
    repositories: List[RepositorySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListRepositoriesResultTypeDef(BaseValidatorModel):
    repositories: List[RepositorySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdatePackageGroupOriginConfigurationRequestTypeDef(BaseValidatorModel):
    domain: str
    packageGroup: str
    domainOwner: Optional[str] = None
    restrictions: Optional[ Mapping[PackageGroupOriginRestrictionTypeType, PackageGroupOriginRestrictionModeType] ] = None
    addAllowedRepositories: Optional[Sequence[PackageGroupAllowedRepositoryTypeDef]] = None
    removeAllowedRepositories: Optional[Sequence[PackageGroupAllowedRepositoryTypeDef]] = None


class PackageGroupOriginRestrictionTypeDef(BaseValidatorModel):
    mode: Optional[PackageGroupOriginRestrictionModeType] = None
    effectiveMode: Optional[PackageGroupOriginRestrictionModeType] = None
    inheritedFrom: Optional[PackageGroupReferenceTypeDef] = None
    repositoriesCount: Optional[int] = None


class PackageOriginConfigurationTypeDef(BaseValidatorModel):
    restrictions: Optional[PackageOriginRestrictionsTypeDef] = None


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


class PackageVersionSummaryTypeDef(BaseValidatorModel):
    version: str
    status: PackageVersionStatusType
    revision: Optional[str] = None
    origin: Optional[PackageVersionOriginTypeDef] = None


class PackageGroupOriginConfigurationTypeDef(BaseValidatorModel):
    restrictions: Optional[ Dict[PackageGroupOriginRestrictionTypeType, PackageGroupOriginRestrictionTypeDef] ] = None


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


class PackageVersionDescriptionTypeDef(BaseValidatorModel):
    pass


class DescribePackageVersionResultTypeDef(BaseValidatorModel):
    packageVersion: PackageVersionDescriptionTypeDef
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


class PackageDescriptionTypeDef(BaseValidatorModel):
    pass


class DescribePackageResultTypeDef(BaseValidatorModel):
    package: PackageDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class PackageSummaryTypeDef(BaseValidatorModel):
    pass


class DeletePackageResultTypeDef(BaseValidatorModel):
    deletedPackage: PackageSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListPackagesResultTypeDef(BaseValidatorModel):
    packages: List[PackageSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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
    allowedRepositoryUpdates: Dict[ PackageGroupOriginRestrictionTypeType, Dict[PackageGroupAllowedRepositoryUpdateTypeType, List[str]], ]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdatePackageGroupResultTypeDef(BaseValidatorModel):
    packageGroup: PackageGroupDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListPackageGroupsResultTypeDef(BaseValidatorModel):
    packageGroups: List[PackageGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListSubPackageGroupsResultTypeDef(BaseValidatorModel):
    packageGroups: List[PackageGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


