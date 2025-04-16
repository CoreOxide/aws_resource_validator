# Serverlessrepo Classes

# ApplicationDependencySummary

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: <class 'str'>
- **Required**: Yes


# ApplicationPolicyStatement

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


# ApplicationPolicyStatementOutput

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


# ApplicationPolicyStatementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApplicationSummary

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

# CreateApplicationRequest

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


# CreateApplicationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.Version'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadata'>
- **Required**: Yes


# CreateApplicationVersionRequest

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


# CreateApplicationVersionResponse

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ParameterDefinition]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCloudFormationChangeSetRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.serverlessrepo_classes.ParameterValue]]

### ResourceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### RollbackConfiguration
- **Type**: <class 'NoneType'>

### SemanticVersion
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.serverlessrepo_classes.Tag]]

### TemplateId
- **Type**: typing.Optional[str]


# CreateCloudFormationChangeSetResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadata'>
- **Required**: Yes


# CreateCloudFormationTemplateRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: typing.Optional[str]


# CreateCloudFormationTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApplicationRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadata'>
- **Required**: Yes


# GetApplicationPolicyRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationPolicyResponse

### Statements
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationPolicyStatementOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadata'>
- **Required**: Yes


# GetApplicationRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: typing.Optional[str]


# GetApplicationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.Version'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadata'>
- **Required**: Yes


# GetCloudFormationTemplateRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### TemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCloudFormationTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadata'>
- **Required**: Yes


# ListApplicationDependenciesRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SemanticVersion
- **Type**: typing.Optional[str]


# ListApplicationDependenciesRequestPaginate

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SemanticVersion
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.serverlessrepo_classes.PaginatorConfig]


# ListApplicationDependenciesResponse

### Dependencies
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationDependencySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationVersionsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationVersionsRequestPaginate

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.serverlessrepo_classes.PaginatorConfig]


# ListApplicationVersionsResponse

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.VersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequest

### MaxItems
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.serverlessrepo_classes.PaginatorConfig]


# ListApplicationsResponse

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterDefinition

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterValue

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# PutApplicationPolicyRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Statements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationPolicyStatementUnion]
- **Required**: Yes


# PutApplicationPolicyResponse

### Statements
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ApplicationPolicyStatementOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadata'>
- **Required**: Yes


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


# RollbackConfiguration

### MonitoringTimeInMinutes
- **Type**: typing.Optional[int]

### RollbackTriggers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.serverlessrepo_classes.RollbackTrigger]]


# RollbackTrigger

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UnshareApplicationRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateApplicationRequest

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


# UpdateApplicationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.Version'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.serverlessrepo_classes.ResponseMetadata'>
- **Required**: Yes


# Version

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'str'>
- **Required**: Yes

### ParameterDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.serverlessrepo_classes.ParameterDefinition]
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


# VersionSummary

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


