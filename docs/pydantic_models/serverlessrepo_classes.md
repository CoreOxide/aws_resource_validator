# Serverlessrepo Classes

# ApplicationDependencySummaryTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: <class 'str'>
- **Required**: Yes


# ApplicationPolicyStatementOutputTypeDef

### Actions
- **Type**: typing.List[str]
- **Required**: Yes

### Principals
- **Type**: typing.List[str]
- **Required**: Yes

### PrincipalOrgIDs
- **Type**: typing.Optional[typing.List[str]]

### StatementId
- **Type**: typing.Optional[str]


# ApplicationPolicyStatementTypeDef

### Actions
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Principals
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PrincipalOrgIDs
- **Type**: typing.Optional[typing.Sequence[str]]

### StatementId
- **Type**: typing.Optional[str]


# ApplicationPolicyStatementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApplicationSummaryTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Author
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[str]

### HomePageUrl
- **Type**: typing.Optional[str]

### Labels
- **Type**: typing.Optional[typing.List[str]]

### SpdxLicenseId
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateApplicationRequestTypeDef

### Author
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HomePageUrl
- **Type**: typing.Optional[str]

### Labels
- **Type**: typing.Optional[typing.Sequence[str]]

### LicenseBody
- **Type**: typing.Optional[str]

### LicenseUrl
- **Type**: typing.Optional[str]

### ReadmeBody
- **Type**: typing.Optional[str]

### ReadmeUrl
- **Type**: typing.Optional[str]

### SemanticVersion
- **Type**: typing.Optional[str]

### SourceCodeArchiveUrl
- **Type**: typing.Optional[str]

### SourceCodeUrl
- **Type**: typing.Optional[str]

### SpdxLicenseId
- **Type**: typing.Optional[str]

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateUrl
- **Type**: typing.Optional[str]


# CreateApplicationResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Author
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### HomePageUrl
- **Type**: <class 'str'>
- **Required**: Yes

### IsVerifiedAuthor
- **Type**: <class 'bool'>
- **Required**: Yes

### Labels
- **Type**: typing.List[str]
- **Required**: Yes

### LicenseUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ReadmeUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SpdxLicenseId
- **Type**: <class 'str'>
- **Required**: Yes

### VerifiedAuthorUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.VersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateApplicationVersionRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SourceCodeArchiveUrl
- **Type**: typing.Optional[str]

### SourceCodeUrl
- **Type**: typing.Optional[str]

### TemplateBody
- **Type**: typing.Optional[str]

### TemplateUrl
- **Type**: typing.Optional[str]


# CreateApplicationVersionResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ParameterDefinitionTypeDef]
- **Required**: Yes

### RequiredCapabilities
- **Type**: typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM', 'CAPABILITY_RESOURCE_POLICY']]
- **Required**: Yes

### ResourcesSupported
- **Type**: <class 'bool'>
- **Required**: Yes

### SemanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SourceCodeArchiveUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SourceCodeUrl
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCloudFormationChangeSetRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### StackName
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: typing.Optional[typing.Sequence[str]]

### ChangeSetName
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### NotificationArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ParameterOverrides
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.serverlessrepo_classes.ParameterValueTypeDef]]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### RollbackConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.serverlessrepo_classes.RollbackConfigurationTypeDef]

### SemanticVersion
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.serverlessrepo_classes.TagTypeDef]]

### TemplateId
- **Type**: typing.Optional[str]


# CreateCloudFormationChangeSetResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ChangeSetId
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### StackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateCloudFormationTemplateRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: typing.Optional[str]


# CreateCloudFormationTemplateResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationTime
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'EXPIRED', 'PREPARING']
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApplicationRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationPolicyRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationPolicyResponseTypeDef

### Statements
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationPolicyStatementOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: typing.Optional[str]


# GetApplicationResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Author
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### HomePageUrl
- **Type**: <class 'str'>
- **Required**: Yes

### IsVerifiedAuthor
- **Type**: <class 'bool'>
- **Required**: Yes

### Labels
- **Type**: typing.List[str]
- **Required**: Yes

### LicenseUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ReadmeUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SpdxLicenseId
- **Type**: <class 'str'>
- **Required**: Yes

### VerifiedAuthorUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.VersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCloudFormationTemplateRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCloudFormationTemplateResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationTime
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'EXPIRED', 'PREPARING']
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateUrl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationDependenciesRequestPaginateTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.serverlessrepo_classes.PaginatorConfigTypeDef]


# ListApplicationDependenciesRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SemanticVersion
- **Type**: typing.Optional[str]


# ListApplicationDependenciesResponseTypeDef

### Dependencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationDependencySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationVersionsRequestPaginateTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.serverlessrepo_classes.PaginatorConfigTypeDef]


# ListApplicationVersionsRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationVersionsResponseTypeDef

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.VersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.serverlessrepo_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsResponseTypeDef

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterDefinitionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterValueTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PutApplicationPolicyRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Statements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationPolicyStatementUnionTypeDef]
- **Required**: Yes


# PutApplicationPolicyResponseTypeDef

### Statements
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationPolicyStatementOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# RollbackConfigurationTypeDef

### MonitoringTimeInMinutes
- **Type**: typing.Optional[int]

### RollbackTriggers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.serverlessrepo_classes.RollbackTriggerTypeDef]]


# RollbackTriggerTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UnshareApplicationRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApplicationRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Author
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### HomePageUrl
- **Type**: typing.Optional[str]

### Labels
- **Type**: typing.Optional[typing.Sequence[str]]

### ReadmeBody
- **Type**: typing.Optional[str]

### ReadmeUrl
- **Type**: typing.Optional[str]


# UpdateApplicationResponseTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Author
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### HomePageUrl
- **Type**: <class 'str'>
- **Required**: Yes

### IsVerifiedAuthor
- **Type**: <class 'bool'>
- **Required**: Yes

### Labels
- **Type**: typing.List[str]
- **Required**: Yes

### LicenseUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ReadmeUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SpdxLicenseId
- **Type**: <class 'str'>
- **Required**: Yes

### VerifiedAuthorUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Version
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.VersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VersionSummaryTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SourceCodeUrl
- **Type**: typing.Optional[str]


# VersionTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ParameterDefinitionTypeDef]
- **Required**: Yes

### RequiredCapabilities
- **Type**: typing.List[typing.Literal['CAPABILITY_AUTO_EXPAND', 'CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM', 'CAPABILITY_RESOURCE_POLICY']]
- **Required**: Yes

### ResourcesSupported
- **Type**: <class 'bool'>
- **Required**: Yes

### SemanticVersion
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SourceCodeArchiveUrl
- **Type**: typing.Optional[str]

### SourceCodeUrl
- **Type**: typing.Optional[str]


