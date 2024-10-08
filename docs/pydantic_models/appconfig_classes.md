# Pydantic Models in appconfig_classes

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

# ConfigurationProfileSummaryTypeDef

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


# ConfigurationProfileTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.ValidatorTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfigurationProfilesTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.ConfigurationProfileSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# CreateApplicationRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateConfigurationProfileRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.appconfig_classes.ValidatorTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Type
- **Type**: typing.Optional[str]

### KmsKeyIdentifier
- **Type**: typing.Optional[str]


# CreateDeploymentStrategyRequestRequestTypeDef

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


# CreateEnvironmentRequestRequestTypeDef

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


# CreateExtensionAssociationRequestRequestTypeDef

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


# CreateExtensionRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Actions
- **Type**: typing.Mapping[typing.Literal['ON_DEPLOYMENT_BAKING', 'ON_DEPLOYMENT_COMPLETE', 'ON_DEPLOYMENT_ROLLED_BACK', 'ON_DEPLOYMENT_START', 'ON_DEPLOYMENT_STEP', 'PRE_CREATE_HOSTED_CONFIGURATION_VERSION', 'PRE_START_DEPLOYMENT'], typing.Sequence[aws_resource_validator.pydantic_models.appconfig_classes.ActionTypeDef]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.appconfig_classes.ParameterTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### LatestVersionNumber
- **Type**: typing.Optional[int]


# CreateHostedConfigurationVersionRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
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


# DeleteApplicationRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteConfigurationProfileRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentStrategyRequestRequestTypeDef

### DeploymentStrategyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEnvironmentRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExtensionAssociationRequestRequestTypeDef

### ExtensionAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExtensionRequestRequestTypeDef

### ExtensionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]


# DeleteHostedConfigurationVersionRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeploymentEventTypeDef

### EventType
- **Type**: typing.Optional[typing.Literal['BAKE_TIME_STARTED', 'DEPLOYMENT_COMPLETED', 'DEPLOYMENT_STARTED', 'PERCENTAGE_UPDATED', 'ROLLBACK_COMPLETED', 'ROLLBACK_STARTED']]

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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
- **Type**: typing.Optional[typing.Literal['BAKING', 'COMPLETE', 'DEPLOYING', 'ROLLED_BACK', 'ROLLING_BACK', 'VALIDATING']]

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
- **Type**: typing.Literal['BAKING', 'COMPLETE', 'DEPLOYING', 'ROLLED_BACK', 'ROLLING_BACK', 'VALIDATING']
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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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
- **Type**: typing.Literal['DEPLOYING', 'READY_FOR_DEPLOYMENT', 'ROLLED_BACK', 'ROLLING_BACK']
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
- **Type**: typing.Optional[typing.Literal['DEPLOYING', 'READY_FOR_DEPLOYMENT', 'ROLLED_BACK', 'ROLLING_BACK']]

### Monitors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.appconfig_classes.MonitorTypeDef]]


# EnvironmentsTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.appconfig_classes.EnvironmentTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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
- **Type**: typing.Dict[typing.Literal['ON_DEPLOYMENT_BAKING', 'ON_DEPLOYMENT_COMPLETE', 'ON_DEPLOYMENT_ROLLED_BACK', 'ON_DEPLOYMENT_START', 'ON_DEPLOYMENT_STEP', 'PRE_CREATE_HOSTED_CONFIGURATION_VERSION', 'PRE_START_DEPLOYMENT'], typing.List[aws_resource_validator.pydantic_models.appconfig_classes.ActionTypeDef]]
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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationProfileRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationProfileId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationRequestRequestTypeDef

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


# GetDeploymentRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentNumber
- **Type**: <class 'int'>
- **Required**: Yes


# GetDeploymentStrategyRequestRequestTypeDef

### DeploymentStrategyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEnvironmentRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExtensionAssociationRequestRequestTypeDef

### ExtensionAssociationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExtensionRequestRequestTypeDef

### ExtensionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### VersionNumber
- **Type**: typing.Optional[int]


# GetHostedConfigurationVersionRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.appconfig_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationsRequestListApplicationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationProfilesRequestListConfigurationProfilesPaginateTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListConfigurationProfilesRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]


# ListDeploymentStrategiesRequestListDeploymentStrategiesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListDeploymentStrategiesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDeploymentsRequestListDeploymentsPaginateTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListDeploymentsRequestRequestTypeDef

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


# ListEnvironmentsRequestListEnvironmentsPaginateTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListEnvironmentsRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListExtensionAssociationsRequestListExtensionAssociationsPaginateTypeDef

### ResourceIdentifier
- **Type**: typing.Optional[str]

### ExtensionIdentifier
- **Type**: typing.Optional[str]

### ExtensionVersionNumber
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListExtensionAssociationsRequestRequestTypeDef

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


# ListExtensionsRequestListExtensionsPaginateTypeDef

### Name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.appconfig_classes.PaginatorConfigTypeDef]


# ListExtensionsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ListHostedConfigurationVersionsRequestListHostedConfigurationVersionsPaginateTypeDef

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


# ListHostedConfigurationVersionsRequestRequestTypeDef

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


# ListTagsForResourceRequestRequestTypeDef

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

### Description
- **Type**: typing.Optional[str]

### Required
- **Type**: typing.Optional[bool]

### Dynamic
- **Type**: typing.Optional[bool]


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


# StartDeploymentRequestRequestTypeDef

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


# StopDeploymentRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### DeploymentNumber
- **Type**: <class 'int'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateApplicationRequestRequestTypeDef

### ApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateConfigurationProfileRequestRequestTypeDef

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


# UpdateDeploymentStrategyRequestRequestTypeDef

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


# UpdateEnvironmentRequestRequestTypeDef

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


# UpdateExtensionAssociationRequestRequestTypeDef

### ExtensionAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateExtensionRequestRequestTypeDef

### ExtensionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Actions
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ON_DEPLOYMENT_BAKING', 'ON_DEPLOYMENT_COMPLETE', 'ON_DEPLOYMENT_ROLLED_BACK', 'ON_DEPLOYMENT_START', 'ON_DEPLOYMENT_STEP', 'PRE_CREATE_HOSTED_CONFIGURATION_VERSION', 'PRE_START_DEPLOYMENT'], typing.Sequence[aws_resource_validator.pydantic_models.appconfig_classes.ActionTypeDef]]]

### Parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.appconfig_classes.ParameterTypeDef]]

### VersionNumber
- **Type**: typing.Optional[int]


# ValidateConfigurationRequestRequestTypeDef

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

### Type
- **Type**: typing.Literal['JSON_SCHEMA', 'LAMBDA']
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes


