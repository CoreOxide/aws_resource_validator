# Appconfig Classes

# AccountSettings

### DeletionProtection
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.DeletionProtectionSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes


# Action

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Uri
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# ActionInvocation

### ExtensionIdentifier
- **Type**: typing.Optional[str]

### ActionName
- **Type**: typing.Optional[str]

### Uri
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### InvocationId
- **Type**: typing.Optional[str]


# Application

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ApplicationResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes


# Applications

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Application]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# AppliedExtension

### ExtensionId
- **Type**: typing.Optional[str]

### ExtensionAssociationId
- **Type**: typing.Optional[str]

### VersionNumber
- **Type**: typing.Optional[int]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Configuration

### Content
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ConfigurationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes


# ConfigurationProfile

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### RetrievalRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Validators
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Validator]
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes


# ConfigurationProfileSummary

### ApplicationId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### LocationUri
- **Type**: typing.Optional[str]

### ValidatorTypes
- **Type**: typing.Optional[typing.List[typing.Literal['JSON_SCHEMA', 'LAMBDA']]]

### Type
- **Type**: typing.Optional[str]


# ConfigurationProfiles

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ConfigurationProfileSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# CreateApplicationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConfigurationProfileRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### RetrievalRoleArn
- **Type**: typing.Optional[str]

### Validators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Validator]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Type
- **Type**: typing.Optional[str]

### KmsKeyIdentifier
- **Type**: typing.Optional[str]


# CreateDeploymentStrategyRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentDurationInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### GrowthFactor
- **Type**: <class 'float'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### FinalBakeTimeInMinutes
- **Type**: typing.Optional[int]

### GrowthType
- **Type**: typing.Optional[typing.Literal['EXPONENTIAL', 'LINEAR']]

### ReplicateTo
- **Type**: typing.Optional[typing.Literal['NONE', 'SSM_DOCUMENT']]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateEnvironmentRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Monitors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Monitor]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateExtensionAssociationRequest

### ExtensionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ExtensionVersionNumber
- **Type**: typing.Optional[int]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateExtensionRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.Dict[typing.Literal['AT_DEPLOYMENT_TICK', 'ON_DEPLOYMENT_BAKING', 'ON_DEPLOYMENT_COMPLETE', 'ON_DEPLOYMENT_ROLLED_BACK', 'ON_DEPLOYMENT_START', 'ON_DEPLOYMENT_STEP', 'PRE_CREATE_HOSTED_CONFIGURATION_VERSION', 'PRE_START_DEPLOYMENT'], typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Action]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Parameter]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### LatestVersionNumber
- **Type**: typing.Optional[int]


# CreateHostedConfigurationVersionRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### LatestVersionNumber
- **Type**: typing.Optional[int]

### VersionLabel
- **Type**: typing.Optional[str]


# DeleteApplicationRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationProfileRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionCheck
- **Type**: typing.Optional[typing.Literal['ACCOUNT_DEFAULT', 'APPLY', 'BYPASS']]


# DeleteDeploymentStrategyRequest

### DeploymentStrategyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentRequest

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionCheck
- **Type**: typing.Optional[typing.Literal['ACCOUNT_DEFAULT', 'APPLY', 'BYPASS']]


# DeleteExtensionAssociationRequest

### ExtensionAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExtensionRequest

### ExtensionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]


# DeleteHostedConfigurationVersionRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeletionProtectionSettings

### Enabled
- **Type**: typing.Optional[bool]

### ProtectionPeriodInMinutes
- **Type**: typing.Optional[int]


# Deployment

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentStrategyId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationLocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentDurationInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### GrowthType
- **Type**: typing.Literal['EXPONENTIAL', 'LINEAR']
- **Required**: Yes

### GrowthFactor
- **Type**: <class 'float'>
- **Required**: Yes

### FinalBakeTimeInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### State
- **Type**: typing.Literal['BAKING', 'COMPLETE', 'DEPLOYING', 'REVERTED', 'ROLLED_BACK', 'ROLLING_BACK', 'VALIDATING']
- **Required**: Yes

### EventLog
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.DeploymentEvent]
- **Required**: Yes

### PercentageComplete
- **Type**: <class 'float'>
- **Required**: Yes

### StartedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CompletedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AppliedExtensions
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.AppliedExtension]
- **Required**: Yes

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### VersionLabel
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes


# DeploymentEvent

### EventType
- **Type**: typing.Optional[typing.Literal['BAKE_TIME_STARTED', 'DEPLOYMENT_COMPLETED', 'DEPLOYMENT_STARTED', 'PERCENTAGE_UPDATED', 'REVERT_COMPLETED', 'ROLLBACK_COMPLETED', 'ROLLBACK_STARTED']]

### TriggeredBy
- **Type**: typing.Optional[typing.Literal['APPCONFIG', 'CLOUDWATCH_ALARM', 'INTERNAL_ERROR', 'USER']]

### Description
- **Type**: typing.Optional[str]

### ActionInvocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ActionInvocation]]

### OccurredAt
- **Type**: typing.Optional[datetime.datetime]


# DeploymentStrategies

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.DeploymentStrategy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DeploymentStrategy

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DeploymentDurationInMinutes
- **Type**: typing.Optional[int]

### GrowthType
- **Type**: typing.Optional[typing.Literal['EXPONENTIAL', 'LINEAR']]

### GrowthFactor
- **Type**: typing.Optional[float]

### FinalBakeTimeInMinutes
- **Type**: typing.Optional[int]

### ReplicateTo
- **Type**: typing.Optional[typing.Literal['NONE', 'SSM_DOCUMENT']]


# DeploymentStrategyResponse

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentDurationInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### GrowthType
- **Type**: typing.Literal['EXPONENTIAL', 'LINEAR']
- **Required**: Yes

### GrowthFactor
- **Type**: <class 'float'>
- **Required**: Yes

### FinalBakeTimeInMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### ReplicateTo
- **Type**: typing.Literal['NONE', 'SSM_DOCUMENT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes


# DeploymentSummary

### DeploymentNumber
- **Type**: typing.Optional[int]

### ConfigurationName
- **Type**: typing.Optional[str]

### ConfigurationVersion
- **Type**: typing.Optional[str]

### DeploymentDurationInMinutes
- **Type**: typing.Optional[int]

### GrowthType
- **Type**: typing.Optional[typing.Literal['EXPONENTIAL', 'LINEAR']]

### GrowthFactor
- **Type**: typing.Optional[float]

### FinalBakeTimeInMinutes
- **Type**: typing.Optional[int]

### State
- **Type**: typing.Optional[typing.Literal['BAKING', 'COMPLETE', 'DEPLOYING', 'REVERTED', 'ROLLED_BACK', 'ROLLING_BACK', 'VALIDATING']]

### PercentageComplete
- **Type**: typing.Optional[float]

### StartedAt
- **Type**: typing.Optional[datetime.datetime]

### CompletedAt
- **Type**: typing.Optional[datetime.datetime]

### VersionLabel
- **Type**: typing.Optional[str]


# Deployments

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.DeploymentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes


# Environment

### ApplicationId
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DEPLOYING', 'READY_FOR_DEPLOYMENT', 'REVERTED', 'ROLLED_BACK', 'ROLLING_BACK']]

### Monitors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Monitor]]


# EnvironmentResponse

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DEPLOYING', 'READY_FOR_DEPLOYMENT', 'REVERTED', 'ROLLED_BACK', 'ROLLING_BACK']
- **Required**: Yes

### Monitors
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Monitor]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes


# Environments

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Environment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# Extension

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.Dict[typing.Literal['AT_DEPLOYMENT_TICK', 'ON_DEPLOYMENT_BAKING', 'ON_DEPLOYMENT_COMPLETE', 'ON_DEPLOYMENT_ROLLED_BACK', 'ON_DEPLOYMENT_START', 'ON_DEPLOYMENT_STEP', 'PRE_CREATE_HOSTED_CONFIGURATION_VERSION', 'PRE_START_DEPLOYMENT'], typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Action]]
- **Required**: Yes

### Parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Parameter]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes


# ExtensionAssociation

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ExtensionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ExtensionVersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes


# ExtensionAssociationSummary

### Id
- **Type**: typing.Optional[str]

### ExtensionArn
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]


# ExtensionAssociations

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ExtensionAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ExtensionSummary

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### VersionNumber
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# Extensions

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ExtensionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetApplicationRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationProfileRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationRequest

### Application
- **Type**: <class 'str'>
- **Required**: Yes

### Environment
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientConfigurationVersion
- **Type**: typing.Optional[str]


# GetDeploymentRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentNumber
- **Type**: <class 'int'>
- **Required**: Yes


# GetDeploymentStrategyRequest

### DeploymentStrategyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExtensionAssociationRequest

### ExtensionAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExtensionRequest

### ExtensionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]


# GetHostedConfigurationVersionRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# HostedConfigurationVersion

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### VersionLabel
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes


# HostedConfigurationVersionSummary

### ApplicationId
- **Type**: typing.Optional[str]

### ConfigurationProfileId
- **Type**: typing.Optional[str]

### VersionNumber
- **Type**: typing.Optional[int]

### Description
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]

### KmsKeyArn
- **Type**: typing.Optional[str]


# HostedConfigurationVersions

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.HostedConfigurationVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.PaginatorConfig]


# ListConfigurationProfilesRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# ListConfigurationProfilesRequestPaginate

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.PaginatorConfig]


# ListDeploymentStrategiesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDeploymentStrategiesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.PaginatorConfig]


# ListDeploymentsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDeploymentsRequestPaginate

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.PaginatorConfig]


# ListEnvironmentsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEnvironmentsRequestPaginate

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.PaginatorConfig]


# ListExtensionAssociationsRequest

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ExtensionIdentifier
- **Type**: typing.Optional[str]

### ExtensionVersionNumber
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListExtensionAssociationsRequestPaginate

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ExtensionIdentifier
- **Type**: typing.Optional[str]

### ExtensionVersionNumber
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.PaginatorConfig]


# ListExtensionsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ListExtensionsRequestPaginate

### Name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.PaginatorConfig]


# ListHostedConfigurationVersionsRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### VersionLabel
- **Type**: typing.Optional[str]


# ListHostedConfigurationVersionsRequestPaginate

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionLabel
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.PaginatorConfig]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# Monitor

### AlarmArn
- **Type**: <class 'str'>
- **Required**: Yes

### AlarmRoleArn
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Parameter

### Description
- **Type**: typing.Optional[str]

### Required
- **Type**: typing.Optional[bool]

### Dynamic
- **Type**: typing.Optional[bool]


# ResourceTags

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig.appconfig_classes.ResponseMetadata'>
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


# StartDeploymentRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentStrategyId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### KmsKeyIdentifier
- **Type**: typing.Optional[str]

### DynamicExtensionParameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# StopDeploymentRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentNumber
- **Type**: <class 'int'>
- **Required**: Yes

### AllowRevert
- **Type**: typing.Optional[bool]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAccountSettingsRequest

### DeletionProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.DeletionProtectionSettings]


# UpdateApplicationRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateConfigurationProfileRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RetrievalRoleArn
- **Type**: typing.Optional[str]

### Validators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Validator]]

### KmsKeyIdentifier
- **Type**: typing.Optional[str]


# UpdateDeploymentStrategyRequest

### DeploymentStrategyId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DeploymentDurationInMinutes
- **Type**: typing.Optional[int]

### FinalBakeTimeInMinutes
- **Type**: typing.Optional[int]

### GrowthFactor
- **Type**: typing.Optional[float]

### GrowthType
- **Type**: typing.Optional[typing.Literal['EXPONENTIAL', 'LINEAR']]


# UpdateEnvironmentRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Monitors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Monitor]]


# UpdateExtensionAssociationRequest

### ExtensionAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# UpdateExtensionRequest

### ExtensionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.Dict[typing.Literal['AT_DEPLOYMENT_TICK', 'ON_DEPLOYMENT_BAKING', 'ON_DEPLOYMENT_COMPLETE', 'ON_DEPLOYMENT_ROLLED_BACK', 'ON_DEPLOYMENT_START', 'ON_DEPLOYMENT_STEP', 'PRE_CREATE_HOSTED_CONFIGURATION_VERSION', 'PRE_START_DEPLOYMENT'], typing.List[aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Action]]]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.appconfig.appconfig_classes.Parameter]]

### VersionNumber
- **Type**: typing.Optional[int]


# ValidateConfigurationRequest

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationVersion
- **Type**: <class 'str'>
- **Required**: Yes


# Validator

### Type
- **Type**: typing.Literal['JSON_SCHEMA', 'LAMBDA']
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes


