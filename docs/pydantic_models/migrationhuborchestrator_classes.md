# Migrationhuborchestrator Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateMigrationWorkflowRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### inputParameters
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.StepInputUnionTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### applicationConfigurationId
- **Type**: typing.Optional[str]

### stepTargets
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateTemplateRequestTypeDef

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateSource
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.TemplateSourceTypeDef'>
- **Required**: Yes

### templateDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateTemplateResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMigrationWorkflowTemplatesRequestPaginateTypeDef

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfigTypeDef]


# ListMigrationWorkflowTemplatesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# ListMigrationWorkflowTemplatesResponseTypeDef

### templateSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.TemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMigrationWorkflowsRequestPaginateTypeDef

### templateId
- **Type**: typing.Optional[str]

### adsApplicationConfigurationName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'PAUSED', 'PAUSING', 'PAUSING_FAILED', 'STARTING', 'USER_ATTENTION_REQUIRED', 'WORKFLOW_FAILED']]

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfigTypeDef]


# ListMigrationWorkflowsRequestTypeDef

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


# ListMigrationWorkflowsResponseTypeDef

### migrationWorkflowSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.MigrationWorkflowSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPluginsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfigTypeDef]


# ListPluginsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPluginsResponseTypeDef

### plugins
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PluginSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTemplateStepGroupsRequestPaginateTypeDef

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfigTypeDef]


# ListTemplateStepGroupsRequestTypeDef

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTemplateStepGroupsResponseTypeDef

### templateStepGroupSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.TemplateStepGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTemplateStepsRequestPaginateTypeDef

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfigTypeDef]


# ListTemplateStepsRequestTypeDef

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


# ListTemplateStepsResponseTypeDef

### templateStepSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.TemplateStepSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowStepGroupsRequestPaginateTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfigTypeDef]


# ListWorkflowStepGroupsRequestTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWorkflowStepGroupsResponseTypeDef

### workflowStepGroupsSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkflowStepsRequestPaginateTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfigTypeDef]


# ListWorkflowStepsRequestTypeDef

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


# ListWorkflowStepsResponseTypeDef

### workflowStepsSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MigrationWorkflowSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlatformCommandTypeDef

### linux
- **Type**: typing.Optional[str]

### windows
- **Type**: typing.Optional[str]


# PlatformScriptKeyTypeDef

### linux
- **Type**: typing.Optional[str]

### windows
- **Type**: typing.Optional[str]


# PluginSummaryTypeDef

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


# StepAutomationConfigurationTypeDef

### scriptLocationS3Bucket
- **Type**: typing.Optional[str]

### scriptLocationS3Key
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PlatformScriptKeyTypeDef]

### command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PlatformCommandTypeDef]

### runEnvironment
- **Type**: typing.Optional[typing.Literal['AWS', 'ONPREMISE']]

### targetType
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE', 'SINGLE']]


# StepInputOutputTypeDef

### integerValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listOfStringsValue
- **Type**: typing.Optional[typing.List[str]]

### mapOfStringValue
- **Type**: typing.Optional[typing.Dict[str, str]]


# StepInputTypeDef

### integerValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listOfStringsValue
- **Type**: typing.Optional[typing.Sequence[str]]

### mapOfStringValue
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StepInputUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StepOutputTypeDef

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[typing.Literal['INTEGER', 'STRING', 'STRINGLIST', 'STRINGMAP']]

### required
- **Type**: typing.Optional[bool]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TemplateInputTypeDef

### inputName
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[typing.Literal['INTEGER', 'STRING', 'STRINGLIST', 'STRINGMAP']]

### required
- **Type**: typing.Optional[bool]


# TemplateSourceTypeDef

### workflowId
- **Type**: typing.Optional[str]


# TemplateStepGroupSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TemplateStepSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TemplateSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolTypeDef

### name
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateTemplateResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WorkflowStepAutomationConfigurationTypeDef

### scriptLocationS3Bucket
- **Type**: typing.Optional[str]

### scriptLocationS3Key
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PlatformScriptKeyTypeDef]

### command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PlatformCommandTypeDef]

### runEnvironment
- **Type**: typing.Optional[typing.Literal['AWS', 'ONPREMISE']]

### targetType
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE', 'SINGLE']]


# WorkflowStepExtraTypeDef

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[typing.Literal['INTEGER', 'STRING', 'STRINGLIST', 'STRINGMAP']]

### required
- **Type**: typing.Optional[bool]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepOutputUnionOutputTypeDef]


# WorkflowStepGroupSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowStepOutputTypeDef

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[typing.Literal['INTEGER', 'STRING', 'STRINGLIST', 'STRINGMAP']]

### required
- **Type**: typing.Optional[bool]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepOutputUnionUnionTypeDef]


# WorkflowStepOutputUnionOutputTypeDef

### integerValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listOfStringValue
- **Type**: typing.Optional[typing.List[str]]


# WorkflowStepOutputUnionTypeDef

### integerValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listOfStringValue
- **Type**: typing.Optional[typing.Sequence[str]]


# WorkflowStepOutputUnionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkflowStepSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

