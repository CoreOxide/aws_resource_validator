# Codeartifact Classes

# AssetSummaryTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### size
- **Type**: typing.Optional[int]

### hashes
- **Type**: typing.Optional[typing.Dict[typing.Literal['MD5', 'SHA-1', 'SHA-256', 'SHA-512'], str]]


# AssociateExternalConnectionRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# CreateDomainRequestTypeDef

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


# CreatePackageGroupRequestTypeDef

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


# CreateRepositoryRequestTypeDef

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


# DeleteDomainPermissionsPolicyRequestTypeDef

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


# DeleteDomainRequestTypeDef

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


# DeletePackageGroupRequestTypeDef

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


# DeletePackageResultTypeDef

### deletedPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# DeleteRepositoryPermissionsPolicyRequestTypeDef

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


# DeleteRepositoryRequestTypeDef

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


# DescribeDomainRequestTypeDef

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


# DescribePackageGroupRequestTypeDef

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


# DescribePackageResultTypeDef

### package
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePackageVersionResultTypeDef

### packageVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageVersionDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRepositoryRequestTypeDef

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


# DisassociateExternalConnectionRequestTypeDef

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


# GetAuthorizationTokenRequestTypeDef

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


# GetDomainPermissionsPolicyRequestTypeDef

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


# GetRepositoryEndpointResultTypeDef

### repositoryEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRepositoryPermissionsPolicyRequestTypeDef

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


# ListAllowedRepositoriesForGroupRequestPaginateTypeDef

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


# ListAllowedRepositoriesForGroupRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssociatedPackagesRequestPaginateTypeDef

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


# ListAssociatedPackagesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDomainsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PaginatorConfigTypeDef]


# ListDomainsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDomainsResultTypeDef

### domains
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.DomainSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPackageGroupsRequestPaginateTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### domainOwner
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PaginatorConfigTypeDef]


# ListPackageGroupsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPackagesResultTypeDef

### packages
- **Type**: typing.List[aws_resource_validator.pydantic_models.codeartifact_classes.PackageSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesInDomainRequestPaginateTypeDef

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


# ListRepositoriesInDomainRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRepositoriesRequestPaginateTypeDef

### repositoryPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codeartifact_classes.PaginatorConfigTypeDef]


# ListRepositoriesRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSubPackageGroupsRequestPaginateTypeDef

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


# ListSubPackageGroupsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PackageVersionDescriptionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# PutDomainPermissionsPolicyRequestTypeDef

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


# PutPackageOriginConfigurationResultTypeDef

### originConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.PackageOriginConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRepositoryPermissionsPolicyRequestTypeDef

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


# TagResourceRequestTypeDef

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


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdatePackageGroupOriginConfigurationRequestTypeDef

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
- **Type**: typing.Dict[typing.Literal['EXTERNAL_UPSTREAM', 'INTERNAL_UPSTREAM', 'PUBLISH'], typing.Dict[typing.Literal['ADDED', 'REMOVED'], typing.List[str]]]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codeartifact_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePackageGroupRequestTypeDef

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


# UpdateRepositoryRequestTypeDef

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


