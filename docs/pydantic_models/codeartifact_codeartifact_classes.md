# Codeartifact Codeartifact Classes

# AssetSummary

### name
- **Type**: <class 'str'>
- **Required**: Yes

### size
- **Type**: typing.Optional[int]

### hashes
- **Type**: typing.Optional[typing.Dict[typing.Literal['MD5', 'SHA-1', 'SHA-256', 'SHA-512'], str]]


# AssociateExternalConnectionRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### externalConnection
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# AssociateExternalConnectionResult

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.RepositoryDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# AssociatedPackage

### format
- **Type**: typing.Optional[typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']]

### namespace
- **Type**: typing.Optional[str]

### package
- **Type**: typing.Optional[str]

### associationType
- **Type**: typing.Optional[typing.Literal['STRONG', 'WEAK']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CopyPackageVersionsRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### sourceRepository
- **Type**: <class 'str'>
- **Required**: Yes

### destinationRepository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### versions
- **Type**: typing.Optional[typing.List[str]]

### versionRevisions
- **Type**: typing.Optional[typing.Dict[str, str]]

### allowOverwrite
- **Type**: typing.Optional[bool]

### includeFromUpstream
- **Type**: typing.Optional[bool]


# CopyPackageVersionsResult

### successfulVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.SuccessfulPackageVersionInfo]
- **Required**: Yes

### failedVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageVersionError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDomainRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.Tag]]


# CreateDomainResult

### domain
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.DomainDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePackageGroupRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### contactInfo
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.Tag]]


# CreatePackageGroupResult

### packageGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRepositoryRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### upstreams
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.UpstreamRepository]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.Tag]]


# CreateRepositoryResult

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.RepositoryDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDomainPermissionsPolicyRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### policyRevision
- **Type**: typing.Optional[str]


# DeleteDomainPermissionsPolicyResult

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDomainRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# DeleteDomainResult

### domain
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.DomainDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePackageGroupRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# DeletePackageGroupResult

### packageGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePackageRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]


# DeletePackageResult

### deletedPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePackageVersionsRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### versions
- **Type**: typing.List[str]
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### expectedStatus
- **Type**: typing.Optional[typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']]


# DeletePackageVersionsResult

### successfulVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.SuccessfulPackageVersionInfo]
- **Required**: Yes

### failedVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageVersionError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRepositoryPermissionsPolicyRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### policyRevision
- **Type**: typing.Optional[str]


# DeleteRepositoryPermissionsPolicyResult

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRepositoryRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# DeleteRepositoryResult

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.RepositoryDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDomainRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# DescribeDomainResult

### domain
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.DomainDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePackageGroupRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# DescribePackageGroupResult

### packageGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePackageRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]


# DescribePackageResult

### package
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePackageVersionRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### packageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]


# DescribePackageVersionResult

### packageVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageVersionDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRepositoryRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# DescribeRepositoryResult

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.RepositoryDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateExternalConnectionRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### externalConnection
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# DisassociateExternalConnectionResult

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.RepositoryDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DisposePackageVersionsRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### versions
- **Type**: typing.List[str]
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### versionRevisions
- **Type**: typing.Optional[typing.Dict[str, str]]

### expectedStatus
- **Type**: typing.Optional[typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']]


# DisposePackageVersionsResult

### successfulVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.SuccessfulPackageVersionInfo]
- **Required**: Yes

### failedVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageVersionError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# DomainDescription

### name
- **Type**: typing.Optional[str]

### owner
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Deleted']]

### createdTime
- **Type**: typing.Optional[datetime.datetime]

### encryptionKey
- **Type**: typing.Optional[str]

### repositoryCount
- **Type**: typing.Optional[int]

### assetSizeBytes
- **Type**: typing.Optional[int]

### s3BucketArn
- **Type**: typing.Optional[str]


# DomainEntryPoint

### repositoryName
- **Type**: typing.Optional[str]

### externalConnectionName
- **Type**: typing.Optional[str]


# DomainSummary

### name
- **Type**: typing.Optional[str]

### owner
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Deleted']]

### createdTime
- **Type**: typing.Optional[datetime.datetime]

### encryptionKey
- **Type**: typing.Optional[str]


# GetAssociatedPackageGroupRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]


# GetAssociatedPackageGroupResult

### packageGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupDescription'>
- **Required**: Yes

### associationType
- **Type**: typing.Literal['STRONG', 'WEAK']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# GetAuthorizationTokenRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### durationSeconds
- **Type**: typing.Optional[int]


# GetAuthorizationTokenResult

### authorizationToken
- **Type**: <class 'str'>
- **Required**: Yes

### expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# GetDomainPermissionsPolicyRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# GetDomainPermissionsPolicyResult

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# GetPackageVersionAssetRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### packageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### asset
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### packageVersionRevision
- **Type**: typing.Optional[str]


# GetPackageVersionAssetResult

### asset
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### assetName
- **Type**: <class 'str'>
- **Required**: Yes

### packageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### packageVersionRevision
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# GetPackageVersionReadmeRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### packageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]


# GetPackageVersionReadmeResult

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### versionRevision
- **Type**: <class 'str'>
- **Required**: Yes

### readme
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# GetRepositoryEndpointRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### endpointType
- **Type**: typing.Optional[typing.Literal['dualstack', 'ipv4']]


# GetRepositoryEndpointResult

### repositoryEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# GetRepositoryPermissionsPolicyRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# GetRepositoryPermissionsPolicyResult

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# LicenseInfo

### name
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]


# ListAllowedRepositoriesForGroupRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### originRestrictionType
- **Type**: typing.Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH']
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAllowedRepositoriesForGroupRequestPaginate

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### originRestrictionType
- **Type**: typing.Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH']
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PaginatorConfig]


# ListAllowedRepositoriesForGroupResult

### allowedRepositories
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssociatedPackagesRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### preview
- **Type**: typing.Optional[bool]


# ListAssociatedPackagesRequestPaginate

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### preview
- **Type**: typing.Optional[bool]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PaginatorConfig]


# ListAssociatedPackagesResult

### packages
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.AssociatedPackage]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDomainsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDomainsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PaginatorConfig]


# ListDomainsResult

### domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.DomainSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPackageGroupsRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ListPackageGroupsRequestPaginate

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PaginatorConfig]


# ListPackageGroupsResult

### packageGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPackageVersionAssetsRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### packageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPackageVersionAssetsRequestPaginate

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### packageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PaginatorConfig]


# ListPackageVersionAssetsResult

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### versionRevision
- **Type**: <class 'str'>
- **Required**: Yes

### assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.AssetSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPackageVersionDependenciesRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### packageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListPackageVersionDependenciesResult

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### versionRevision
- **Type**: <class 'str'>
- **Required**: Yes

### dependencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageDependency]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPackageVersionsRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']]

### sortBy
- **Type**: typing.Optional[typing.Literal['PUBLISHED_TIME']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### originType
- **Type**: typing.Optional[typing.Literal['EXTERNAL', 'INTERNAL', 'UNKNOWN']]


# ListPackageVersionsRequestPaginate

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']]

### sortBy
- **Type**: typing.Optional[typing.Literal['PUBLISHED_TIME']]

### originType
- **Type**: typing.Optional[typing.Literal['EXTERNAL', 'INTERNAL', 'UNKNOWN']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PaginatorConfig]


# ListPackageVersionsResult

### defaultDisplayVersion
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPackagesRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### format
- **Type**: typing.Optional[typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']]

### namespace
- **Type**: typing.Optional[str]

### packagePrefix
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### publish
- **Type**: typing.Optional[typing.Literal['ALLOW', 'BLOCK']]

### upstream
- **Type**: typing.Optional[typing.Literal['ALLOW', 'BLOCK']]


# ListPackagesRequestPaginate

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### format
- **Type**: typing.Optional[typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']]

### namespace
- **Type**: typing.Optional[str]

### packagePrefix
- **Type**: typing.Optional[str]

### publish
- **Type**: typing.Optional[typing.Literal['ALLOW', 'BLOCK']]

### upstream
- **Type**: typing.Optional[typing.Literal['ALLOW', 'BLOCK']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PaginatorConfig]


# ListPackagesResult

### packages
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesInDomainRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### administratorAccount
- **Type**: typing.Optional[str]

### repositoryPrefix
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesInDomainRequestPaginate

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### administratorAccount
- **Type**: typing.Optional[str]

### repositoryPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PaginatorConfig]


# ListRepositoriesInDomainResult

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.RepositorySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesRequest

### repositoryPrefix
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesRequestPaginate

### repositoryPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PaginatorConfig]


# ListRepositoriesResult

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.RepositorySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSubPackageGroupsRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSubPackageGroupsRequestPaginate

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PaginatorConfig]


# ListSubPackageGroupsResult

### packageGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResult

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# PackageDependency

### namespace
- **Type**: typing.Optional[str]

### package
- **Type**: typing.Optional[str]

### dependencyType
- **Type**: typing.Optional[str]

### versionRequirement
- **Type**: typing.Optional[str]


# PackageDescription

### format
- **Type**: typing.Optional[typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']]

### namespace
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### originConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageOriginConfiguration]


# PackageGroupAllowedRepository

### repositoryName
- **Type**: typing.Optional[str]

### originRestrictionType
- **Type**: typing.Optional[typing.Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH']]


# PackageGroupDescription

### arn
- **Type**: typing.Optional[str]

### pattern
- **Type**: typing.Optional[str]

### domainName
- **Type**: typing.Optional[str]

### domainOwner
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[datetime.datetime]

### contactInfo
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### originConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupOriginConfiguration]

### parent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupReference]


# PackageGroupOriginConfiguration

### restrictions
- **Type**: typing.Optional[typing.Dict[typing.Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH'], aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupOriginRestriction]]


# PackageGroupOriginRestriction

### mode
- **Type**: typing.Optional[typing.Literal['ALLOW', 'ALLOW_SPECIFIC_REPOSITORIES', 'BLOCK', 'INHERIT']]

### effectiveMode
- **Type**: typing.Optional[typing.Literal['ALLOW', 'ALLOW_SPECIFIC_REPOSITORIES', 'BLOCK', 'INHERIT']]

### inheritedFrom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupReference]

### repositoriesCount
- **Type**: typing.Optional[int]


# PackageGroupReference

### arn
- **Type**: typing.Optional[str]

### pattern
- **Type**: typing.Optional[str]


# PackageGroupSummary

### arn
- **Type**: typing.Optional[str]

### pattern
- **Type**: typing.Optional[str]

### domainName
- **Type**: typing.Optional[str]

### domainOwner
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[datetime.datetime]

### contactInfo
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### originConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupOriginConfiguration]

### parent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupReference]


# PackageOriginConfiguration

### restrictions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageOriginRestrictions]


# PackageOriginRestrictions

### publish
- **Type**: typing.Literal['ALLOW', 'BLOCK']
- **Required**: Yes

### upstream
- **Type**: typing.Literal['ALLOW', 'BLOCK']
- **Required**: Yes


# PackageSummary

### format
- **Type**: typing.Optional[typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']]

### namespace
- **Type**: typing.Optional[str]

### package
- **Type**: typing.Optional[str]

### originConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageOriginConfiguration]


# PackageVersionDescription

### format
- **Type**: typing.Optional[typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']]

### namespace
- **Type**: typing.Optional[str]

### packageName
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### summary
- **Type**: typing.Optional[str]

### homePage
- **Type**: typing.Optional[str]

### sourceCodeRepository
- **Type**: typing.Optional[str]

### publishedTime
- **Type**: typing.Optional[datetime.datetime]

### licenses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.LicenseInfo]]

### revision
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']]

### origin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageVersionOrigin]


# PackageVersionError

### errorCode
- **Type**: typing.Optional[typing.Literal['ALREADY_EXISTS', 'MISMATCHED_REVISION', 'MISMATCHED_STATUS', 'NOT_ALLOWED', 'NOT_FOUND', 'SKIPPED']]

### errorMessage
- **Type**: typing.Optional[str]


# PackageVersionOrigin

### domainEntryPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.DomainEntryPoint]

### originType
- **Type**: typing.Optional[typing.Literal['EXTERNAL', 'INTERNAL', 'UNKNOWN']]


# PackageVersionSummary

### version
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]

### origin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageVersionOrigin]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PublishPackageVersionRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### packageVersion
- **Type**: <class 'str'>
- **Required**: Yes

### assetContent
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### assetName
- **Type**: <class 'str'>
- **Required**: Yes

### assetSHA256
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### unfinished
- **Type**: typing.Optional[bool]


# PublishPackageVersionResult

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### versionRevision
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']
- **Required**: Yes

### asset
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.AssetSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# PutDomainPermissionsPolicyRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### policyRevision
- **Type**: typing.Optional[str]


# PutDomainPermissionsPolicyResult

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# PutPackageOriginConfigurationRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### restrictions
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageOriginRestrictions'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]


# PutPackageOriginConfigurationResult

### originConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageOriginConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# PutRepositoryPermissionsPolicyRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### policyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### policyRevision
- **Type**: typing.Optional[str]


# PutRepositoryPermissionsPolicyResult

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResourcePolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# RepositoryDescription

### name
- **Type**: typing.Optional[str]

### administratorAccount
- **Type**: typing.Optional[str]

### domainName
- **Type**: typing.Optional[str]

### domainOwner
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### upstreams
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.UpstreamRepositoryInfo]]

### externalConnections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.RepositoryExternalConnectionInfo]]

### createdTime
- **Type**: typing.Optional[datetime.datetime]


# RepositoryExternalConnectionInfo

### externalConnectionName
- **Type**: typing.Optional[str]

### packageFormat
- **Type**: typing.Optional[typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']]

### status
- **Type**: typing.Optional[typing.Literal['Available']]


# RepositorySummary

### name
- **Type**: typing.Optional[str]

### administratorAccount
- **Type**: typing.Optional[str]

### domainName
- **Type**: typing.Optional[str]

### domainOwner
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### createdTime
- **Type**: typing.Optional[datetime.datetime]


# ResourcePolicy

### resourceArn
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[str]

### document
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


# SuccessfulPackageVersionInfo

### revision
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']]


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdatePackageGroupOriginConfigurationRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### restrictions
- **Type**: typing.Optional[typing.Dict[typing.Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH'], typing.Literal['ALLOW', 'ALLOW_SPECIFIC_REPOSITORIES', 'BLOCK', 'INHERIT']]]

### addAllowedRepositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupAllowedRepository]]

### removeAllowedRepositories
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupAllowedRepository]]


# UpdatePackageGroupOriginConfigurationResult

### packageGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupDescription'>
- **Required**: Yes

### allowedRepositoryUpdates
- **Type**: typing.Dict[typing.Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH'], typing.Dict[typing.Literal['ADDED', 'REMOVED'], typing.List[str]]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePackageGroupRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### contactInfo
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdatePackageGroupResult

### packageGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageGroupDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePackageVersionsStatusRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### format
- **Type**: typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']
- **Required**: Yes

### package
- **Type**: <class 'str'>
- **Required**: Yes

### versions
- **Type**: typing.List[str]
- **Required**: Yes

### targetStatus
- **Type**: typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### versionRevisions
- **Type**: typing.Optional[typing.Dict[str, str]]

### expectedStatus
- **Type**: typing.Optional[typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']]


# UpdatePackageVersionsStatusResult

### successfulVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.SuccessfulPackageVersionInfo]
- **Required**: Yes

### failedVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.PackageVersionError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRepositoryRequest

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### upstreams
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.UpstreamRepository]]


# UpdateRepositoryResult

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.RepositoryDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact.codeartifact_classes.ResponseMetadata'>
- **Required**: Yes


# UpstreamRepository

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


# UpstreamRepositoryInfo

### repositoryName
- **Type**: typing.Optional[str]


