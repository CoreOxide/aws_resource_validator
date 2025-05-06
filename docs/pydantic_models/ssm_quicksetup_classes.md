# Ssm Quicksetup Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigurationDefinition

### Parameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: typing.Optional[str]

### LocalDeploymentAdministrationRoleArn
- **Type**: typing.Optional[str]

### LocalDeploymentExecutionRoleName
- **Type**: typing.Optional[str]

### TypeVersion
- **Type**: typing.Optional[str]


# ConfigurationDefinitionInput

### Parameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### LocalDeploymentAdministrationRoleArn
- **Type**: typing.Optional[str]

### LocalDeploymentExecutionRoleName
- **Type**: typing.Optional[str]

### TypeVersion
- **Type**: typing.Optional[str]


# ConfigurationDefinitionSummary

### FirstClassParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### Id
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[str]

### TypeVersion
- **Type**: typing.Optional[str]


# ConfigurationManagerSummary

### ManagerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationDefinitionSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ConfigurationDefinitionSummary]]

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### StatusSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.StatusSummary]]


# ConfigurationSummary

### Account
- **Type**: typing.Optional[str]

### ConfigurationDefinitionId
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### FirstClassParameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### Id
- **Type**: typing.Optional[str]

### ManagerArn
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[str]

### StatusSummaries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.StatusSummary]]

### Type
- **Type**: typing.Optional[str]

### TypeVersion
- **Type**: typing.Optional[str]


# CreateConfigurationManagerInput

### ConfigurationDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ConfigurationDefinitionInput]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateConfigurationManagerOutput

### ManagerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteConfigurationManagerInput

### ManagerArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ResponseMetadata'>
- **Required**: Yes


# Filter

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# GetConfigurationInput

### ConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationManagerInput

### ManagerArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetConfigurationManagerOutput

### ConfigurationDefinitions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ConfigurationDefinition]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ManagerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### StatusSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.StatusSummary]
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ResponseMetadata'>
- **Required**: Yes


# GetConfigurationOutput

### Account
- **Type**: <class 'str'>
- **Required**: Yes

### ConfigurationDefinitionId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ManagerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Parameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### StatusSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.StatusSummary]
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### TypeVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceSettingsOutput

### ServiceSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ServiceSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ResponseMetadata'>
- **Required**: Yes


# ListConfigurationManagersInput

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.Filter]]

### MaxItems
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ListConfigurationManagersInputPaginate

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.PaginatorConfig]


# ListConfigurationManagersOutput

### ConfigurationManagersList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ConfigurationManagerSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListConfigurationsInput

### ConfigurationDefinitionId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.Filter]]

### ManagerArn
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ListConfigurationsInputPaginate

### ConfigurationDefinitionId
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.Filter]]

### ManagerArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.PaginatorConfig]


# ListConfigurationsOutput

### ConfigurationsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListQuickSetupTypesOutput

### QuickSetupTypeList
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.QuickSetupTypeOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.TagEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ssm_quicksetup.ssm_quicksetup_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# QuickSetupTypeOutput

### LatestVersion
- **Type**: typing.Optional[str]

### Type
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


# ServiceSettings

### ExplorerEnablingRoleArn
- **Type**: typing.Optional[str]


# StatusSummary

### LastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StatusType
- **Type**: typing.Literal['AsyncExecutions', 'Deployment']
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DELETE_FAILED', 'DELETING', 'DEPLOYING', 'FAILED', 'INITIALIZING', 'NONE', 'STOPPED', 'STOPPING', 'STOP_FAILED', 'SUCCEEDED']]

### StatusDetails
- **Type**: typing.Optional[typing.Dict[str, str]]

### StatusMessage
- **Type**: typing.Optional[str]


# TagEntry

### Key
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# TagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceInput

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateConfigurationDefinitionInput

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ManagerArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocalDeploymentAdministrationRoleArn
- **Type**: typing.Optional[str]

### LocalDeploymentExecutionRoleName
- **Type**: typing.Optional[str]

### Parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### TypeVersion
- **Type**: typing.Optional[str]


# UpdateConfigurationManagerInput

### ManagerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# UpdateServiceSettingsInput

### ExplorerEnablingRoleArn
- **Type**: typing.Optional[str]


