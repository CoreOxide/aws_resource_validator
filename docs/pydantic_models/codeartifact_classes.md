# Pydantic Models in codeartifact_classes

# AssetSummaryTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### size
- **Type**: typing.Optional[int]

### hashes
- **Type**: typing.Optional[typing.Dict[typing.Literal['MD5', 'SHA-1', 'SHA-256', 'SHA-512'], str]]


# AssociateExternalConnectionRequestRequestTypeDef

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


# AssociateExternalConnectionResultTypeDef

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.RepositoryDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociatedPackageTypeDef

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

# CopyPackageVersionsRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### versionRevisions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### allowOverwrite
- **Type**: typing.Optional[bool]

### includeFromUpstream
- **Type**: typing.Optional[bool]


# CopyPackageVersionsResultTypeDef

### successfulVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact_classes.SuccessfulPackageVersionInfoTypeDef]
- **Required**: Yes

### failedVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact_classes.PackageVersionErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDomainRequestRequestTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeartifact_classes.TagTypeDef]]


# CreateDomainResultTypeDef

### domain
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.DomainDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePackageGroupRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeartifact_classes.TagTypeDef]]


# CreatePackageGroupResultTypeDef

### packageGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRepositoryRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeartifact_classes.UpstreamRepositoryTypeDef]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeartifact_classes.TagTypeDef]]


# CreateRepositoryResultTypeDef

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.RepositoryDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDomainPermissionsPolicyRequestRequestTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### policyRevision
- **Type**: typing.Optional[str]


# DeleteDomainPermissionsPolicyResultTypeDef

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDomainRequestRequestTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# DeleteDomainResultTypeDef

### domain
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.DomainDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePackageGroupRequestRequestTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# DeletePackageGroupResultTypeDef

### packageGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePackageRequestRequestTypeDef

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


# DeletePackageResultTypeDef

### deletedPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePackageVersionsRequestRequestTypeDef

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
- **Type**: typing.Sequence[str]
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### expectedStatus
- **Type**: typing.Optional[typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']]


# DeletePackageVersionsResultTypeDef

### successfulVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact_classes.SuccessfulPackageVersionInfoTypeDef]
- **Required**: Yes

### failedVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact_classes.PackageVersionErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRepositoryPermissionsPolicyRequestRequestTypeDef

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


# DeleteRepositoryPermissionsPolicyResultTypeDef

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRepositoryRequestRequestTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# DeleteRepositoryResultTypeDef

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.RepositoryDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDomainRequestRequestTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# DescribeDomainResultTypeDef

### domain
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.DomainDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePackageGroupRequestRequestTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# DescribePackageGroupResultTypeDef

### packageGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePackageRequestRequestTypeDef

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


# DescribePackageResultTypeDef

### package
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePackageVersionRequestRequestTypeDef

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


# DescribePackageVersionResultTypeDef

### packageVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageVersionDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRepositoryRequestRequestTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# DescribeRepositoryResultTypeDef

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.RepositoryDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateExternalConnectionRequestRequestTypeDef

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


# DisassociateExternalConnectionResultTypeDef

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.RepositoryDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisposePackageVersionsRequestRequestTypeDef

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
- **Type**: typing.Sequence[str]
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### versionRevisions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### expectedStatus
- **Type**: typing.Optional[typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']]


# DisposePackageVersionsResultTypeDef

### successfulVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact_classes.SuccessfulPackageVersionInfoTypeDef]
- **Required**: Yes

### failedVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact_classes.PackageVersionErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DomainDescriptionTypeDef

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


# DomainEntryPointTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### externalConnectionName
- **Type**: typing.Optional[str]


# DomainSummaryTypeDef

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


# GetAssociatedPackageGroupRequestRequestTypeDef

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


# GetAssociatedPackageGroupResultTypeDef

### packageGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupDescriptionTypeDef'>
- **Required**: Yes

### associationType
- **Type**: typing.Literal['STRONG', 'WEAK']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAuthorizationTokenRequestRequestTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### durationSeconds
- **Type**: typing.Optional[int]


# GetAuthorizationTokenResultTypeDef

### authorizationToken
- **Type**: <class 'str'>
- **Required**: Yes

### expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDomainPermissionsPolicyRequestRequestTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# GetDomainPermissionsPolicyResultTypeDef

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPackageVersionAssetRequestRequestTypeDef

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


# GetPackageVersionAssetResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPackageVersionReadmeRequestRequestTypeDef

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


# GetPackageVersionReadmeResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRepositoryEndpointRequestRequestTypeDef

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


# GetRepositoryEndpointResultTypeDef

### repositoryEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRepositoryPermissionsPolicyRequestRequestTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### repository
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]


# GetRepositoryPermissionsPolicyResultTypeDef

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LicenseInfoTypeDef

### name
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]


# ListAllowedRepositoriesForGroupRequestListAllowedRepositoriesForGroupPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PaginatorConfigTypeDef]


# ListAllowedRepositoriesForGroupRequestRequestTypeDef

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


# ListAllowedRepositoriesForGroupResultTypeDef

### allowedRepositories
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssociatedPackagesRequestListAssociatedPackagesPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PaginatorConfigTypeDef]


# ListAssociatedPackagesRequestRequestTypeDef

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


# ListAssociatedPackagesResultTypeDef

### packages
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.AssociatedPackageTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDomainsRequestListDomainsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PaginatorConfigTypeDef]


# ListDomainsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDomainsResultTypeDef

### domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.DomainSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPackageGroupsRequestListPackageGroupsPaginateTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PaginatorConfigTypeDef]


# ListPackageGroupsRequestRequestTypeDef

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


# ListPackageGroupsResultTypeDef

### packageGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPackageVersionAssetsRequestListPackageVersionAssetsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PaginatorConfigTypeDef]


# ListPackageVersionAssetsRequestRequestTypeDef

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


# ListPackageVersionAssetsResultTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.AssetSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPackageVersionDependenciesRequestRequestTypeDef

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


# ListPackageVersionDependenciesResultTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### dependencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.PackageDependencyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPackageVersionsRequestListPackageVersionsPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PaginatorConfigTypeDef]


# ListPackageVersionsRequestRequestTypeDef

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


# ListPackageVersionsResultTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.PackageVersionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPackagesRequestListPackagesPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PaginatorConfigTypeDef]


# ListPackagesRequestRequestTypeDef

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


# ListPackagesResultTypeDef

### packages
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.PackageSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRepositoriesInDomainRequestListRepositoriesInDomainPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PaginatorConfigTypeDef]


# ListRepositoriesInDomainRequestRequestTypeDef

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


# ListRepositoriesInDomainResultTypeDef

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.RepositorySummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRepositoriesRequestListRepositoriesPaginateTypeDef

### repositoryPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PaginatorConfigTypeDef]


# ListRepositoriesRequestRequestTypeDef

### repositoryPrefix
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesResultTypeDef

### repositories
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.RepositorySummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSubPackageGroupsRequestListSubPackageGroupsPaginateTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PaginatorConfigTypeDef]


# ListSubPackageGroupsRequestRequestTypeDef

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


# ListSubPackageGroupsResultTypeDef

### packageGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResultTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PackageDependencyTypeDef

### namespace
- **Type**: typing.Optional[str]

### package
- **Type**: typing.Optional[str]

### dependencyType
- **Type**: typing.Optional[str]

### versionRequirement
- **Type**: typing.Optional[str]


# PackageDescriptionTypeDef

### format
- **Type**: typing.Optional[typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']]

### namespace
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### originConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PackageOriginConfigurationTypeDef]


# PackageGroupAllowedRepositoryTypeDef

### repositoryName
- **Type**: typing.Optional[str]

### originRestrictionType
- **Type**: typing.Optional[typing.Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH']]


# PackageGroupDescriptionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupOriginConfigurationTypeDef]

### parent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupReferenceTypeDef]


# PackageGroupOriginConfigurationTypeDef

### restrictions
- **Type**: typing.Optional[typing.Dict[typing.Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH'], aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupOriginRestrictionTypeDef]]


# PackageGroupOriginRestrictionTypeDef

### mode
- **Type**: typing.Optional[typing.Literal['ALLOW', 'ALLOW_SPECIFIC_REPOSITORIES', 'BLOCK', 'INHERIT']]

### effectiveMode
- **Type**: typing.Optional[typing.Literal['ALLOW', 'ALLOW_SPECIFIC_REPOSITORIES', 'BLOCK', 'INHERIT']]

### inheritedFrom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupReferenceTypeDef]

### repositoriesCount
- **Type**: typing.Optional[int]


# PackageGroupReferenceTypeDef

### arn
- **Type**: typing.Optional[str]

### pattern
- **Type**: typing.Optional[str]


# PackageGroupSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupOriginConfigurationTypeDef]

### parent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupReferenceTypeDef]


# PackageOriginConfigurationTypeDef

### restrictions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PackageOriginRestrictionsTypeDef]


# PackageOriginRestrictionsTypeDef

### publish
- **Type**: typing.Literal['ALLOW', 'BLOCK']
- **Required**: Yes

### upstream
- **Type**: typing.Literal['ALLOW', 'BLOCK']
- **Required**: Yes


# PackageSummaryTypeDef

### format
- **Type**: typing.Optional[typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']]

### namespace
- **Type**: typing.Optional[str]

### package
- **Type**: typing.Optional[str]

### originConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PackageOriginConfigurationTypeDef]


# PackageVersionDescriptionTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.LicenseInfoTypeDef]]

### revision
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']]

### origin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PackageVersionOriginTypeDef]


# PackageVersionErrorTypeDef

### errorCode
- **Type**: typing.Optional[typing.Literal['ALREADY_EXISTS', 'MISMATCHED_REVISION', 'MISMATCHED_STATUS', 'NOT_ALLOWED', 'NOT_FOUND', 'SKIPPED']]

### errorMessage
- **Type**: typing.Optional[str]


# PackageVersionOriginTypeDef

### domainEntryPoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.DomainEntryPointTypeDef]

### originType
- **Type**: typing.Optional[typing.Literal['EXTERNAL', 'INTERNAL', 'UNKNOWN']]


# PackageVersionSummaryTypeDef

### version
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']
- **Required**: Yes

### revision
- **Type**: typing.Optional[str]

### origin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PackageVersionOriginTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PublishPackageVersionRequestRequestTypeDef

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
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
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


# PublishPackageVersionResultTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.AssetSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutDomainPermissionsPolicyRequestRequestTypeDef

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


# PutDomainPermissionsPolicyResultTypeDef

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutPackageOriginConfigurationRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageOriginRestrictionsTypeDef'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]


# PutPackageOriginConfigurationResultTypeDef

### originConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageOriginConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRepositoryPermissionsPolicyRequestRequestTypeDef

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


# PutRepositoryPermissionsPolicyResultTypeDef

### policy
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResourcePolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RepositoryDescriptionTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.UpstreamRepositoryInfoTypeDef]]

### externalConnections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.RepositoryExternalConnectionInfoTypeDef]]

### createdTime
- **Type**: typing.Optional[datetime.datetime]


# RepositoryExternalConnectionInfoTypeDef

### externalConnectionName
- **Type**: typing.Optional[str]

### packageFormat
- **Type**: typing.Optional[typing.Literal['cargo', 'generic', 'maven', 'npm', 'nuget', 'pypi', 'ruby', 'swift']]

### status
- **Type**: typing.Optional[typing.Literal['Available']]


# RepositorySummaryTypeDef

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


# ResourcePolicyTypeDef

### resourceArn
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[str]

### document
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

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


# SuccessfulPackageVersionInfoTypeDef

### revision
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codeartifact_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdatePackageGroupOriginConfigurationRequestRequestTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### packageGroup
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### restrictions
- **Type**: typing.Optional[typing.Mapping[typing.Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH'], typing.Literal['ALLOW', 'ALLOW_SPECIFIC_REPOSITORIES', 'BLOCK', 'INHERIT']]]

### addAllowedRepositories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupAllowedRepositoryTypeDef]]

### removeAllowedRepositories
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupAllowedRepositoryTypeDef]]


# UpdatePackageGroupOriginConfigurationResultTypeDef

### packageGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupDescriptionTypeDef'>
- **Required**: Yes

### allowedRepositoryUpdates
- **Type**: typing.List[typing.Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePackageGroupRequestRequestTypeDef

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


# UpdatePackageGroupResultTypeDef

### packageGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageGroupDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePackageVersionsStatusRequestRequestTypeDef

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
- **Type**: typing.Sequence[str]
- **Required**: Yes

### targetStatus
- **Type**: typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### versionRevisions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### expectedStatus
- **Type**: typing.Optional[typing.Literal['Archived', 'Deleted', 'Disposed', 'Published', 'Unfinished', 'Unlisted']]


# UpdatePackageVersionsStatusResultTypeDef

### successfulVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact_classes.SuccessfulPackageVersionInfoTypeDef]
- **Required**: Yes

### failedVersions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.codeartifact_classes.PackageVersionErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRepositoryRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codeartifact_classes.UpstreamRepositoryTypeDef]]


# UpdateRepositoryResultTypeDef

### repository
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.RepositoryDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpstreamRepositoryInfoTypeDef

### repositoryName
- **Type**: typing.Optional[str]


# UpstreamRepositoryTypeDef

### repositoryName
- **Type**: <class 'str'>
- **Required**: Yes


