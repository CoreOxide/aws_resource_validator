# Serverlessrepo Classes

# ApplicationDependencySummaryTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: <class 'str'>
- **Required**: Yes


# ApplicationPolicyStatementTypeDef

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

# CreateApplicationRequestRequestTypeDef

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


# CreateApplicationVersionRequestRequestTypeDef

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


# CreateCloudFormationChangeSetRequestRequestTypeDef

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


# CreateCloudFormationTemplateRequestRequestTypeDef

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


# DeleteApplicationRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationPolicyRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationPolicyResponseTypeDef

### Statements
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationPolicyStatementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationRequestRequestTypeDef

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


# GetCloudFormationTemplateRequestRequestTypeDef

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


# ListApplicationDependenciesRequestListApplicationDependenciesPaginateTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.serverlessrepo_classes.PaginatorConfigTypeDef]


# ListApplicationDependenciesRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationVersionsRequestListApplicationVersionsPaginateTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.serverlessrepo_classes.PaginatorConfigTypeDef]


# ListApplicationVersionsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationVersionsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.VersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationsRequestListApplicationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.serverlessrepo_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestRequestTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsResponseTypeDef

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterDefinitionTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ReferencedByResources
- **Type**: typing.List[str]
- **Required**: Yes

### AllowedPattern
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[typing.List[str]]

### ConstraintDescription
- **Type**: typing.Optional[str]

### DefaultValue
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### MaxLength
- **Type**: typing.Optional[int]

### MaxValue
- **Type**: typing.Optional[int]

### MinLength
- **Type**: typing.Optional[int]

### MinValue
- **Type**: typing.Optional[int]

### NoEcho
- **Type**: typing.Optional[bool]

### Type
- **Type**: typing.Optional[str]


# ParameterValueTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PutApplicationPolicyRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Statements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationPolicyStatementTypeDef]
- **Required**: Yes


# PutApplicationPolicyResponseTypeDef

### Statements
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationPolicyStatementTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# RollbackConfigurationTypeDef

### MonitoringTimeInMinutes
- **Type**: typing.Optional[int]

### RollbackTriggers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.serverlessrepo_classes.RollbackTriggerTypeDef]]


# RollbackTriggerTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UnshareApplicationRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApplicationRequestRequestTypeDef

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


