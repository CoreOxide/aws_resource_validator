# Launch Wizard Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateDeploymentInputTypeDef

### deploymentPatternName
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### specifications
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### workloadName
- **Type**: <class 'str'>
- **Required**: Yes

### dryRun
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateDeploymentOutputTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDeploymentInputTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDeploymentOutputTypeDef

### status
- **Type**: typing.Literal['COMPLETED', 'CREATING', 'DELETED', 'DELETE_FAILED', 'DELETE_INITIATING', 'DELETE_IN_PROGRESS', 'FAILED', 'IN_PROGRESS', 'VALIDATING']
- **Required**: Yes

### statusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeploymentConditionalFieldTypeDef

### comparator
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# DeploymentDataSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentDataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentEventDataSummaryTypeDef

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


# DeploymentFilterTypeDef

### name
- **Type**: typing.Optional[typing.Literal['DEPLOYMENT_STATUS', 'WORKLOAD_NAME']]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# DeploymentSpecificationsFieldTypeDef

### allowedValues
- **Type**: typing.Optional[typing.List[str]]

### conditionals
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.launch_wizard_classes.DeploymentConditionalFieldTypeDef]]

### description
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### required
- **Type**: typing.Optional[str]


# GetDeploymentInputTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDeploymentOutputTypeDef

### deployment
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard_classes.DeploymentDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkloadDeploymentPatternInputTypeDef

### deploymentPatternName
- **Type**: <class 'str'>
- **Required**: Yes

### workloadName
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkloadDeploymentPatternOutputTypeDef

### workloadDeploymentPattern
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard_classes.WorkloadDeploymentPatternDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkloadInputTypeDef

### workloadName
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkloadOutputTypeDef

### workload
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard_classes.WorkloadDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDeploymentEventsInputPaginateTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.launch_wizard_classes.PaginatorConfigTypeDef]


# ListDeploymentEventsInputTypeDef

### deploymentId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentEventsOutputTypeDef

### deploymentEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.launch_wizard_classes.DeploymentEventDataSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsInputPaginateTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.launch_wizard_classes.DeploymentFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.launch_wizard_classes.PaginatorConfigTypeDef]


# ListDeploymentsInputTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.launch_wizard_classes.DeploymentFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDeploymentsOutputTypeDef

### deployments
- **Type**: typing.List[aws_resource_validator.pydantic_models.launch_wizard_classes.DeploymentDataSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkloadDeploymentPatternsInputPaginateTypeDef

### workloadName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.launch_wizard_classes.PaginatorConfigTypeDef]


# ListWorkloadDeploymentPatternsInputTypeDef

### workloadName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkloadDeploymentPatternsOutputTypeDef

### workloadDeploymentPatterns
- **Type**: typing.List[aws_resource_validator.pydantic_models.launch_wizard_classes.WorkloadDeploymentPatternDataSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkloadsInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.launch_wizard_classes.PaginatorConfigTypeDef]


# ListWorkloadsInputTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkloadsOutputTypeDef

### workloads
- **Type**: typing.List[aws_resource_validator.pydantic_models.launch_wizard_classes.WorkloadDataSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.launch_wizard_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
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


# TagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# WorkloadDataSummaryTypeDef

### displayName
- **Type**: typing.Optional[str]

### workloadName
- **Type**: typing.Optional[str]


# WorkloadDataTypeDef

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


# WorkloadDeploymentPatternDataSummaryTypeDef

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


# WorkloadDeploymentPatternDataTypeDef

### deploymentPatternName
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### specifications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.launch_wizard_classes.DeploymentSpecificationsFieldTypeDef]]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED', 'DISABLED', 'INACTIVE']]

### statusMessage
- **Type**: typing.Optional[str]

### workloadName
- **Type**: typing.Optional[str]

### workloadVersionName
- **Type**: typing.Optional[str]


