# Migrationhuborchestrator Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateMigrationWorkflowRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### inputParameters
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.StepInputUnion]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### applicationConfigurationId
- **Type**: typing.Optional[str]

### stepTargets
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateTemplateRequest

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateSource
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.TemplateSource'>
- **Required**: Yes

### templateDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateTemplateResponse

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### templateArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# ListMigrationWorkflowTemplatesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# ListMigrationWorkflowTemplatesRequestPaginate

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfig]


# ListMigrationWorkflowTemplatesResponse

### templateSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.TemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMigrationWorkflowsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### templateId
- **Type**: typing.Optional[str]

### adsApplicationConfigurationName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'PAUSED', 'PAUSING', 'PAUSING_FAILED', 'STARTING', 'USER_ATTENTION_REQUIRED', 'WORKFLOW_FAILED']]

### name
- **Type**: typing.Optional[str]


# ListMigrationWorkflowsRequestPaginate

### templateId
- **Type**: typing.Optional[str]

### adsApplicationConfigurationName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'PAUSED', 'PAUSING', 'PAUSING_FAILED', 'STARTING', 'USER_ATTENTION_REQUIRED', 'WORKFLOW_FAILED']]

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfig]


# ListMigrationWorkflowsResponse

### migrationWorkflowSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.MigrationWorkflowSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPluginsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPluginsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfig]


# ListPluginsResponse

### plugins
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PluginSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# ListTemplateStepGroupsRequest

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTemplateStepGroupsRequestPaginate

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfig]


# ListTemplateStepGroupsResponse

### templateStepGroupSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.TemplateStepGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTemplateStepsRequest

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTemplateStepsRequestPaginate

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfig]


# ListTemplateStepsResponse

### templateStepSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.TemplateStepSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowStepGroupsRequest

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWorkflowStepGroupsRequestPaginate

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfig]


# ListWorkflowStepGroupsResponse

### workflowStepGroupsSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowStepsRequest

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWorkflowStepsRequestPaginate

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfig]


# ListWorkflowStepsResponse

### workflowStepsSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MigrationWorkflowSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlatformCommand

### linux
- **Type**: typing.Optional[str]

### windows
- **Type**: typing.Optional[str]


# PlatformScriptKey

### linux
- **Type**: typing.Optional[str]

### windows
- **Type**: typing.Optional[str]


# PluginSummary

### pluginId
- **Type**: typing.Optional[str]

### hostname
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'UNHEALTHY']]

### ipAddress
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[str]

### registeredTime
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


# StepAutomationConfiguration

### scriptLocationS3Bucket
- **Type**: typing.Optional[str]

### scriptLocationS3Key
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PlatformScriptKey]

### command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PlatformCommand]

### runEnvironment
- **Type**: typing.Optional[typing.Literal['AWS', 'ONPREMISE']]

### targetType
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE', 'SINGLE']]


# StepInput

### integerValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listOfStringsValue
- **Type**: typing.Optional[typing.Sequence[str]]

### mapOfStringValue
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StepInputOutput

### integerValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listOfStringsValue
- **Type**: typing.Optional[typing.List[str]]

### mapOfStringValue
- **Type**: typing.Optional[typing.Dict[str, str]]


# StepInputUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StepOutput

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[typing.Literal['INTEGER', 'STRING', 'STRINGLIST', 'STRINGMAP']]

### required
- **Type**: typing.Optional[bool]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemplateInput

### inputName
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[typing.Literal['INTEGER', 'STRING', 'STRINGLIST', 'STRINGMAP']]

### required
- **Type**: typing.Optional[bool]


# TemplateSource

### workflowId
- **Type**: typing.Optional[str]


# TemplateStepGroupSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TemplateStepSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TemplateSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Tool

### name
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateTemplateResponse

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### templateArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# WorkflowStepAutomationConfiguration

### scriptLocationS3Bucket
- **Type**: typing.Optional[str]

### scriptLocationS3Key
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PlatformScriptKey]

### command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PlatformCommand]

### runEnvironment
- **Type**: typing.Optional[typing.Literal['AWS', 'ONPREMISE']]

### targetType
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE', 'SINGLE']]


# WorkflowStepExtra

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[typing.Literal['INTEGER', 'STRING', 'STRINGLIST', 'STRINGMAP']]

### required
- **Type**: typing.Optional[bool]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepOutputUnionOutput]


# WorkflowStepGroupSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowStepOutput

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[typing.Literal['INTEGER', 'STRING', 'STRINGLIST', 'STRINGMAP']]

### required
- **Type**: typing.Optional[bool]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepOutputUnionUnion]


# WorkflowStepOutputUnion

### integerValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listOfStringValue
- **Type**: typing.Optional[typing.Sequence[str]]


# WorkflowStepOutputUnionOutput

### integerValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listOfStringValue
- **Type**: typing.Optional[typing.List[str]]


# WorkflowStepOutputUnionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowStepSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

