# Appconfig Classes

# AccountSettingsTypeDef

### DeletionProtection
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.DeletionProtectionSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ActionInvocationTypeDef

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


# ActionTypeDef

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Uri
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# ApplicationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ApplicationTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# ApplicationsTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.ApplicationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# AppliedExtensionTypeDef

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

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigurationProfileSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigurationProfilesTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.ConfigurationProfileSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ConfigurationTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateApplicationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDeploymentStrategyRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEnvironmentRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Monitors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appconfig_classes.MonitorTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateExtensionAssociationRequestTypeDef

### ExtensionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### ExtensionVersionNumber
- **Type**: typing.Optional[int]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateExtensionRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.Mapping[typing.Literal['AT_DEPLOYMENT_TICK', 'ON_DEPLOYMENT_BAKING', 'ON_DEPLOYMENT_COMPLETE', 'ON_DEPLOYMENT_ROLLED_BACK', 'ON_DEPLOYMENT_START', 'ON_DEPLOYMENT_STEP', 'PRE_CREATE_HOSTED_CONFIGURATION_VERSION', 'PRE_START_DEPLOYMENT'], typing.Sequence[aws_resource_validator.pydantic_models.appconfig_classes.ActionTypeDef]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.appconfig_classes.ParameterTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### LatestVersionNumber
- **Type**: typing.Optional[int]


# CreateHostedConfigurationVersionRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.BlobTypeDef'>
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


# DeleteApplicationRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationProfileRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionCheck
- **Type**: typing.Optional[typing.Literal['ACCOUNT_DEFAULT', 'APPLY', 'BYPASS']]


# DeleteDeploymentStrategyRequestTypeDef

### DeploymentStrategyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentRequestTypeDef

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionProtectionCheck
- **Type**: typing.Optional[typing.Literal['ACCOUNT_DEFAULT', 'APPLY', 'BYPASS']]


# DeleteExtensionAssociationRequestTypeDef

### ExtensionAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExtensionRequestTypeDef

### ExtensionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]


# DeleteHostedConfigurationVersionRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeletionProtectionSettingsTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### ProtectionPeriodInMinutes
- **Type**: typing.Optional[int]


# DeploymentEventTypeDef

### EventType
- **Type**: typing.Optional[typing.Literal['BAKE_TIME_STARTED', 'DEPLOYMENT_COMPLETED', 'DEPLOYMENT_STARTED', 'PERCENTAGE_UPDATED', 'REVERT_COMPLETED', 'ROLLBACK_COMPLETED', 'ROLLBACK_STARTED']]

### TriggeredBy
- **Type**: typing.Optional[typing.Literal['APPCONFIG', 'CLOUDWATCH_ALARM', 'INTERNAL_ERROR', 'USER']]

### Description
- **Type**: typing.Optional[str]

### ActionInvocations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appconfig_classes.ActionInvocationTypeDef]]

### OccurredAt
- **Type**: typing.Optional[datetime.datetime]


# DeploymentStrategiesTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.DeploymentStrategyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DeploymentStrategyResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeploymentStrategyTypeDef

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


# DeploymentSummaryTypeDef

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


# DeploymentTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.DeploymentEventTypeDef]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.AppliedExtensionTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeploymentsTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.DeploymentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.MonitorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnvironmentTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appconfig_classes.MonitorTypeDef]]


# EnvironmentsTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.EnvironmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ExtensionAssociationSummaryTypeDef

### Id
- **Type**: typing.Optional[str]

### ExtensionArn
- **Type**: typing.Optional[str]

### ResourceArn
- **Type**: typing.Optional[str]


# ExtensionAssociationTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExtensionAssociationsTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.ExtensionAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ExtensionSummaryTypeDef

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


# ExtensionTypeDef

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
- **Type**: typing.Dict[typing.Literal['AT_DEPLOYMENT_TICK', 'ON_DEPLOYMENT_BAKING', 'ON_DEPLOYMENT_COMPLETE', 'ON_DEPLOYMENT_ROLLED_BACK', 'ON_DEPLOYMENT_START', 'ON_DEPLOYMENT_STEP', 'PRE_CREATE_HOSTED_CONFIGURATION_VERSION', 'PRE_START_DEPLOYMENT'], typing.List[aws_resource_validator.pydantic_models.appconfig_classes.ActionTypeDef]]
- **Required**: Yes

### Parameters
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.appconfig_classes.ParameterTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExtensionsTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.ExtensionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetApplicationRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationProfileRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationRequestTypeDef

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


# GetDeploymentRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentNumber
- **Type**: <class 'int'>
- **Required**: Yes


# GetDeploymentStrategyRequestTypeDef

### DeploymentStrategyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExtensionAssociationRequestTypeDef

### ExtensionAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExtensionRequestTypeDef

### ExtensionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]


# GetHostedConfigurationVersionRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# HostedConfigurationVersionSummaryTypeDef

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


# HostedConfigurationVersionTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HostedConfigurationVersionsTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.HostedConfigurationVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDeploymentStrategiesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListDeploymentStrategiesRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDeploymentsRequestPaginateTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListDeploymentsRequestTypeDef

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


# ListEnvironmentsRequestPaginateTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListEnvironmentsRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListExtensionAssociationsRequestPaginateTypeDef

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ExtensionIdentifier
- **Type**: typing.Optional[str]

### ExtensionVersionNumber
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListExtensionAssociationsRequestTypeDef

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


# ListExtensionsRequestPaginateTypeDef

### Name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListExtensionsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ListHostedConfigurationVersionsRequestPaginateTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionLabel
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListHostedConfigurationVersionsRequestTypeDef

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


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# MonitorTypeDef

### AlarmArn
- **Type**: <class 'str'>
- **Required**: Yes

### AlarmRoleArn
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResourceTagsTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
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


# StartDeploymentRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### KmsKeyIdentifier
- **Type**: typing.Optional[str]

### DynamicExtensionParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StopDeploymentRequestTypeDef

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


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountSettingsRequestTypeDef

### DeletionProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.DeletionProtectionSettingsTypeDef]


# UpdateApplicationRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateConfigurationProfileRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appconfig_classes.ValidatorTypeDef]]

### KmsKeyIdentifier
- **Type**: typing.Optional[str]


# UpdateDeploymentStrategyRequestTypeDef

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


# UpdateEnvironmentRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appconfig_classes.MonitorTypeDef]]


# UpdateExtensionAssociationRequestTypeDef

### ExtensionAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateExtensionRequestTypeDef

### ExtensionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.Mapping[typing.Literal['AT_DEPLOYMENT_TICK', 'ON_DEPLOYMENT_BAKING', 'ON_DEPLOYMENT_COMPLETE', 'ON_DEPLOYMENT_ROLLED_BACK', 'ON_DEPLOYMENT_START', 'ON_DEPLOYMENT_STEP', 'PRE_CREATE_HOSTED_CONFIGURATION_VERSION', 'PRE_START_DEPLOYMENT'], typing.Sequence[aws_resource_validator.pydantic_models.appconfig_classes.ActionTypeDef]]]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.appconfig_classes.ParameterTypeDef]]

### VersionNumber
- **Type**: typing.Optional[int]


# ValidateConfigurationRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationVersion
- **Type**: <class 'str'>
- **Required**: Yes


# ValidatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

