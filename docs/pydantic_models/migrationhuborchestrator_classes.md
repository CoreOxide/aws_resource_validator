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
- **Type**: typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.StepInput, aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.StepInputOutput]]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### applicationConfigurationId
- **Type**: typing.Optional[str]

### stepTargets
- **Type**: typing.Optional[typing.List[str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateMigrationWorkflowResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### adsApplicationConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowInputs
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.StepInputOutput]
- **Required**: Yes

### stepTargets
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'PAUSED', 'PAUSING', 'PAUSING_FAILED', 'STARTING', 'USER_ATTENTION_REQUIRED', 'WORKFLOW_FAILED']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTemplateRequest

### templateName
- **Type**: <class 'str'>
- **Required**: Yes

### templateSource
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.TemplateSource'>
- **Required**: Yes

### templateDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkflowStepGroupRequest

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### next
- **Type**: typing.Optional[typing.List[str]]

### previous
- **Type**: typing.Optional[typing.List[str]]


# CreateWorkflowStepGroupResponse

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### tools
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.Tool]
- **Required**: Yes

### next
- **Type**: typing.List[str]
- **Required**: Yes

### previous
- **Type**: typing.List[str]
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkflowStepRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### stepActionType
- **Type**: typing.Literal['AUTOMATED', 'MANUAL']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### workflowStepAutomationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.WorkflowStepAutomationConfiguration]

### stepTarget
- **Type**: typing.Optional[typing.List[str]]

### outputs
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.WorkflowStepOutput, aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.WorkflowStepExtra]]]

### previous
- **Type**: typing.Optional[typing.List[str]]

### next
- **Type**: typing.Optional[typing.List[str]]


# CreateWorkflowStepResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteMigrationWorkflowRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMigrationWorkflowResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'PAUSED', 'PAUSING', 'PAUSING_FAILED', 'STARTING', 'USER_ATTENTION_REQUIRED', 'WORKFLOW_FAILED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkflowStepGroupRequest

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkflowStepRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMigrationWorkflowRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetMigrationWorkflowResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### adsApplicationConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### adsApplicationName
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'PAUSED', 'PAUSING', 'PAUSING_FAILED', 'STARTING', 'USER_ATTENTION_REQUIRED', 'WORKFLOW_FAILED']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastStopTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tools
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.Tool]
- **Required**: Yes

### totalSteps
- **Type**: <class 'int'>
- **Required**: Yes

### completedSteps
- **Type**: <class 'int'>
- **Required**: Yes

### workflowInputs
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.StepInputOutput]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### workflowBucket
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# GetMigrationWorkflowTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetMigrationWorkflowTemplateResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### templateArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### inputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.TemplateInput]
- **Required**: Yes

### tools
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.Tool]
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### owner
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'CREATING', 'CREATION_FAILED', 'PENDING_CREATION', 'READY']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### templateClass
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# GetTemplateStepGroupRequest

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateStepGroupResponse

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AWAITING_DEPENDENCIES', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'PAUSED', 'PAUSING', 'READY', 'USER_ATTENTION_REQUIRED']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tools
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.Tool]
- **Required**: Yes

### previous
- **Type**: typing.List[str]
- **Required**: Yes

### next
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# GetTemplateStepRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateStepResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### stepActionType
- **Type**: typing.Literal['AUTOMATED', 'MANUAL']
- **Required**: Yes

### creationTime
- **Type**: <class 'str'>
- **Required**: Yes

### previous
- **Type**: typing.List[str]
- **Required**: Yes

### next
- **Type**: typing.List[str]
- **Required**: Yes

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.StepOutput]
- **Required**: Yes

### stepAutomationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.StepAutomationConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkflowStepGroupRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowStepGroupResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AWAITING_DEPENDENCIES', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'PAUSED', 'PAUSING', 'READY', 'USER_ATTENTION_REQUIRED']
- **Required**: Yes

### owner
- **Type**: typing.Literal['AWS_MANAGED', 'CUSTOM']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tools
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.Tool]
- **Required**: Yes

### previous
- **Type**: typing.List[str]
- **Required**: Yes

### next
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# GetWorkflowStepRequest

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowStepResponse

### name
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### stepId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### stepActionType
- **Type**: typing.Literal['AUTOMATED', 'MANUAL']
- **Required**: Yes

### owner
- **Type**: typing.Literal['AWS_MANAGED', 'CUSTOM']
- **Required**: Yes

### workflowStepAutomationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.WorkflowStepAutomationConfiguration'>
- **Required**: Yes

### stepTarget
- **Type**: typing.List[str]
- **Required**: Yes

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.WorkflowStepExtra]
- **Required**: Yes

### previous
- **Type**: typing.List[str]
- **Required**: Yes

### next
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['AWAITING_DEPENDENCIES', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'PAUSED', 'READY', 'SKIPPED', 'USER_ATTENTION_REQUIRED']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### scriptOutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### noOfSrvCompleted
- **Type**: <class 'int'>
- **Required**: Yes

### noOfSrvFailed
- **Type**: <class 'int'>
- **Required**: Yes

### totalNoOfSrv
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.PaginatorConfig]


# ListMigrationWorkflowTemplatesResponse

### templateSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.TemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.PaginatorConfig]


# ListMigrationWorkflowsResponse

### migrationWorkflowSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.MigrationWorkflowSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.PaginatorConfig]


# ListPluginsResponse

### plugins
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.PluginSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.PaginatorConfig]


# ListTemplateStepGroupsResponse

### templateStepGroupSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.TemplateStepGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.PaginatorConfig]


# ListTemplateStepsResponse

### templateStepSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.TemplateStepSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.PaginatorConfig]


# ListWorkflowStepGroupsResponse

### workflowStepGroupsSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.WorkflowStepGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.PaginatorConfig]


# ListWorkflowStepsResponse

### workflowStepsSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.WorkflowStepSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MigrationWorkflowSummary

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### templateId
- **Type**: typing.Optional[str]

### adsApplicationConfigurationName
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'PAUSED', 'PAUSING', 'PAUSING_FAILED', 'STARTING', 'USER_ATTENTION_REQUIRED', 'WORKFLOW_FAILED']]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### statusMessage
- **Type**: typing.Optional[str]

### completedSteps
- **Type**: typing.Optional[int]

### totalSteps
- **Type**: typing.Optional[int]


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


# RetryWorkflowStepRequest

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# RetryWorkflowStepResponse

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AWAITING_DEPENDENCIES', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'PAUSED', 'READY', 'SKIPPED', 'USER_ATTENTION_REQUIRED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# StartMigrationWorkflowRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# StartMigrationWorkflowResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'PAUSED', 'PAUSING', 'PAUSING_FAILED', 'STARTING', 'USER_ATTENTION_REQUIRED', 'WORKFLOW_FAILED']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### lastStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# StepAutomationConfiguration

### scriptLocationS3Bucket
- **Type**: typing.Optional[str]

### scriptLocationS3Key
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.PlatformScriptKey]

### command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.PlatformCommand]

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
- **Type**: typing.Optional[typing.List[str]]

### mapOfStringValue
- **Type**: typing.Optional[typing.Dict[str, str]]


# StepInputOutput

### integerValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listOfStringsValue
- **Type**: typing.Optional[typing.List[str]]

### mapOfStringValue
- **Type**: typing.Optional[typing.Dict[str, str]]


# StepOutput

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[typing.Literal['INTEGER', 'STRING', 'STRINGLIST', 'STRINGMAP']]

### required
- **Type**: typing.Optional[bool]


# StopMigrationWorkflowRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# StopMigrationWorkflowResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'PAUSED', 'PAUSING', 'PAUSING_FAILED', 'STARTING', 'USER_ATTENTION_REQUIRED', 'WORKFLOW_FAILED']
- **Required**: Yes

### statusMessage
- **Type**: <class 'str'>
- **Required**: Yes

### lastStopTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
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

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### previous
- **Type**: typing.Optional[typing.List[str]]

### next
- **Type**: typing.Optional[typing.List[str]]


# TemplateStepSummary

### id
- **Type**: typing.Optional[str]

### stepGroupId
- **Type**: typing.Optional[str]

### templateId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### stepActionType
- **Type**: typing.Optional[typing.Literal['AUTOMATED', 'MANUAL']]

### targetType
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE', 'SINGLE']]

### owner
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'CUSTOM']]

### previous
- **Type**: typing.Optional[typing.List[str]]

### next
- **Type**: typing.Optional[typing.List[str]]


# TemplateSummary

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


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
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateMigrationWorkflowRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### inputParameters
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.StepInput, aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.StepInputOutput]]]

### stepTargets
- **Type**: typing.Optional[typing.List[str]]


# UpdateMigrationWorkflowResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### adsApplicationConfigurationId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowInputs
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.StepInputOutput]
- **Required**: Yes

### stepTargets
- **Type**: typing.List[str]
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETED', 'CREATING', 'CREATION_FAILED', 'DELETED', 'DELETING', 'DELETION_FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'PAUSED', 'PAUSING', 'PAUSING_FAILED', 'STARTING', 'USER_ATTENTION_REQUIRED', 'WORKFLOW_FAILED']
- **Required**: Yes

### creationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: typing.Optional[str]

### templateDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkflowStepGroupRequest

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### next
- **Type**: typing.Optional[typing.List[str]]

### previous
- **Type**: typing.Optional[typing.List[str]]


# UpdateWorkflowStepGroupResponse

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### tools
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.Tool]
- **Required**: Yes

### next
- **Type**: typing.List[str]
- **Required**: Yes

### previous
- **Type**: typing.List[str]
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkflowStepRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### stepActionType
- **Type**: typing.Optional[typing.Literal['AUTOMATED', 'MANUAL']]

### workflowStepAutomationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.WorkflowStepAutomationConfiguration]

### stepTarget
- **Type**: typing.Optional[typing.List[str]]

### outputs
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.WorkflowStepOutput, aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.WorkflowStepExtra]]]

### previous
- **Type**: typing.Optional[typing.List[str]]

### next
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['AWAITING_DEPENDENCIES', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'PAUSED', 'READY', 'SKIPPED', 'USER_ATTENTION_REQUIRED']]


# UpdateWorkflowStepResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.ResponseMetadata'>
- **Required**: Yes


# WorkflowStepAutomationConfiguration

### scriptLocationS3Bucket
- **Type**: typing.Optional[str]

### scriptLocationS3Key
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.PlatformScriptKey]

### command
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.PlatformCommand]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.WorkflowStepOutputUnionOutput]


# WorkflowStepGroupSummary

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### owner
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'CUSTOM']]

### status
- **Type**: typing.Optional[typing.Literal['AWAITING_DEPENDENCIES', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'PAUSED', 'PAUSING', 'READY', 'USER_ATTENTION_REQUIRED']]

### previous
- **Type**: typing.Optional[typing.List[str]]

### next
- **Type**: typing.Optional[typing.List[str]]


# WorkflowStepOutput

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[typing.Literal['INTEGER', 'STRING', 'STRINGLIST', 'STRINGMAP']]

### required
- **Type**: typing.Optional[bool]

### value
- **Type**: typing.Union[aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.WorkflowStepOutputUnion, aws_resource_validator.pydantic_models.migrationhuborchestrator.migrationhuborchestrator_classes.WorkflowStepOutputUnionOutput, NoneType]


# WorkflowStepOutputUnion

### integerValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listOfStringValue
- **Type**: typing.Optional[typing.List[str]]


# WorkflowStepOutputUnionOutput

### integerValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listOfStringValue
- **Type**: typing.Optional[typing.List[str]]


# WorkflowStepSummary

### stepId
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### stepActionType
- **Type**: typing.Optional[typing.Literal['AUTOMATED', 'MANUAL']]

### owner
- **Type**: typing.Optional[typing.Literal['AWS_MANAGED', 'CUSTOM']]

### previous
- **Type**: typing.Optional[typing.List[str]]

### next
- **Type**: typing.Optional[typing.List[str]]

### status
- **Type**: typing.Optional[typing.Literal['AWAITING_DEPENDENCIES', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'PAUSED', 'READY', 'SKIPPED', 'USER_ATTENTION_REQUIRED']]

### statusMessage
- **Type**: typing.Optional[str]

### noOfSrvCompleted
- **Type**: typing.Optional[int]

### noOfSrvFailed
- **Type**: typing.Optional[int]

### totalNoOfSrv
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### scriptLocation
- **Type**: typing.Optional[str]


