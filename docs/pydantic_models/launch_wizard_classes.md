# Launch Wizard Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDeploymentInput

### deploymentPatternName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### specifications
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### workloadName
- **Type**: <class 'str'>
- **Required**: Yes

### dryRun
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateDeploymentOutput

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDeploymentInput

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentOutput

### status
- **Type**: typing.Literal['COMPLETED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETE_INITIATING', 'DELETE_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'VALIDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.ResponseMetadata'>
- **Required**: Yes


# DeploymentConditionalField

### comparator
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# DeploymentData

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### deletedAt
- **Type**: typing.Optional[datetime.datetime]

### deploymentArn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### patternName
- **Type**: typing.Optional[str]

### resourceGroup
- **Type**: typing.Optional[str]

### specifications
- **Type**: typing.Optional[typing.Dict[str, str]]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETE_INITIATING', 'DELETE_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'VALIDATING']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### workloadName
- **Type**: typing.Optional[str]


# DeploymentDataSummary

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### patternName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETE_INITIATING', 'DELETE_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'VALIDATING']]

### workloadName
- **Type**: typing.Optional[str]


# DeploymentEventDataSummary

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CANCELED', 'CANCELING', 'COMPLETED', 'CREATED', 'FAILED', 'IN_PROGRESS', 'PENDING', 'TIMED_OUT']]

### statusReason
- **Type**: typing.Optional[str]

### timestamp
- **Type**: typing.Optional[datetime.datetime]


# DeploymentFilter

### name
- **Type**: typing.Optional[typing.Literal['DEPLOYMENT_STATUS', 'WORKLOAD_NAME']]

### values
- **Type**: typing.Optional[typing.List[str]]


# DeploymentSpecificationsField

### allowedValues
- **Type**: typing.Optional[typing.List[str]]

### conditionals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.DeploymentConditionalField]]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### required
- **Type**: typing.Optional[str]


# GetDeploymentInput

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentOutput

### deployment
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.DeploymentData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkloadDeploymentPatternInput

### deploymentPatternName
- **Type**: <class 'str'>
- **Required**: Yes

### workloadName
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkloadDeploymentPatternOutput

### workloadDeploymentPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.WorkloadDeploymentPatternData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkloadInput

### workloadName
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkloadOutput

### workload
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.WorkloadData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.ResponseMetadata'>
- **Required**: Yes


# ListDeploymentEventsInput

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentEventsInputPaginate

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.PaginatorConfig]


# ListDeploymentEventsOutput

### deploymentEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.DeploymentEventDataSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsInput

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.DeploymentFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsInputPaginate

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.DeploymentFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.PaginatorConfig]


# ListDeploymentsOutput

### deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.DeploymentDataSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutput

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.ResponseMetadata'>
- **Required**: Yes


# ListWorkloadDeploymentPatternsInput

### workloadName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkloadDeploymentPatternsInputPaginate

### workloadName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.PaginatorConfig]


# ListWorkloadDeploymentPatternsOutput

### workloadDeploymentPatterns
- **Type**: typing.List[aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.WorkloadDeploymentPatternDataSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkloadsInput

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkloadsInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.PaginatorConfig]


# ListWorkloadsOutput

### workloads
- **Type**: typing.List[aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.WorkloadDataSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# WorkloadData

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### documentationUrl
- **Type**: typing.Optional[str]

### iconUrl
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DISABLED', 'INACTIVE']]

### statusMessage
- **Type**: typing.Optional[str]

### workloadName
- **Type**: typing.Optional[str]


# WorkloadDataSummary

### displayName
- **Type**: typing.Optional[str]

### workloadName
- **Type**: typing.Optional[str]


# WorkloadDeploymentPatternData

### deploymentPatternName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### specifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.launch_wizard.launch_wizard_classes.DeploymentSpecificationsField]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DISABLED', 'INACTIVE']]

### statusMessage
- **Type**: typing.Optional[str]

### workloadName
- **Type**: typing.Optional[str]

### workloadVersionName
- **Type**: typing.Optional[str]


# WorkloadDeploymentPatternDataSummary

### deploymentPatternName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DISABLED', 'INACTIVE']]

### statusMessage
- **Type**: typing.Optional[str]

### workloadName
- **Type**: typing.Optional[str]

### workloadVersionName
- **Type**: typing.Optional[str]


