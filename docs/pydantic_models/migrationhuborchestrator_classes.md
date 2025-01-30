# migrationhuborchestrator_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateMigrationWorkflowRequestRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### inputParameters
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.StepInputTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### applicationConfigurationId
- **Type**: typing.Optional[str]

### stepTargets
- **Type**: typing.Optional[typing.Sequence[str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateMigrationWorkflowResponseTypeDef

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.StepInputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTemplateRequestRequestTypeDef

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


# CreateWorkflowStepGroupRequestRequestTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### next
- **Type**: typing.Optional[typing.Sequence[str]]

### previous
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateWorkflowStepGroupResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ToolTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkflowStepRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepAutomationConfigurationTypeDef]

### stepTarget
- **Type**: typing.Optional[typing.Sequence[str]]

### outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepOutputTypeDef]]

### previous
- **Type**: typing.Optional[typing.Sequence[str]]

### next
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateWorkflowStepResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteMigrationWorkflowRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMigrationWorkflowResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkflowStepGroupRequestRequestTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkflowStepRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMigrationWorkflowRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetMigrationWorkflowResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ToolTypeDef]
- **Required**: Yes

### totalSteps
- **Type**: <class 'int'>
- **Required**: Yes

### completedSteps
- **Type**: <class 'int'>
- **Required**: Yes

### workflowInputs
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.StepInputTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### workflowBucket
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMigrationWorkflowTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetMigrationWorkflowTemplateResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.TemplateInputTypeDef]
- **Required**: Yes

### tools
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ToolTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTemplateStepGroupRequestRequestTypeDef

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateStepGroupResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ToolTypeDef]
- **Required**: Yes

### previous
- **Type**: typing.List[str]
- **Required**: Yes

### next
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTemplateStepRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTemplateStepResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.StepOutputTypeDef]
- **Required**: Yes

### stepAutomationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.StepAutomationConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkflowStepGroupRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowStepGroupResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ToolTypeDef]
- **Required**: Yes

### previous
- **Type**: typing.List[str]
- **Required**: Yes

### next
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetWorkflowStepRequestRequestTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetWorkflowStepResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepAutomationConfigurationTypeDef'>
- **Required**: Yes

### stepTarget
- **Type**: typing.List[str]
- **Required**: Yes

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepOutputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMigrationWorkflowTemplatesRequestListTemplatesPaginateTypeDef

### name
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfigTypeDef]


# ListMigrationWorkflowTemplatesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]


# ListMigrationWorkflowTemplatesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### templateSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.TemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMigrationWorkflowsRequestListWorkflowsPaginateTypeDef

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


# ListMigrationWorkflowsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### migrationWorkflowSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.MigrationWorkflowSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPluginsRequestListPluginsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfigTypeDef]


# ListPluginsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPluginsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### plugins
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PluginSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListTemplateStepGroupsRequestListTemplateStepGroupsPaginateTypeDef

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfigTypeDef]


# ListTemplateStepGroupsRequestRequestTypeDef

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTemplateStepGroupsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### templateStepGroupSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.TemplateStepGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTemplateStepsRequestListTemplateStepsPaginateTypeDef

### templateId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfigTypeDef]


# ListTemplateStepsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### templateStepSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.TemplateStepSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkflowStepGroupsRequestListWorkflowStepGroupsPaginateTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfigTypeDef]


# ListWorkflowStepGroupsRequestRequestTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListWorkflowStepGroupsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### workflowStepGroupsSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkflowStepsRequestListWorkflowStepsPaginateTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.PaginatorConfigTypeDef]


# ListWorkflowStepsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### workflowStepsSummary
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MigrationWorkflowSummaryTypeDef

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


# RetryWorkflowStepRequestRequestTypeDef

### workflowId
- **Type**: <class 'str'>
- **Required**: Yes

### stepGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes


# RetryWorkflowStepResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartMigrationWorkflowRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# StartMigrationWorkflowResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# StepInputTypeDef

### integerValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listOfStringsValue
- **Type**: typing.Optional[typing.Sequence[str]]

### mapOfStringValue
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StepOutputTypeDef

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[typing.Literal['INTEGER', 'STRING', 'STRINGLIST', 'STRINGMAP']]

### required
- **Type**: typing.Optional[bool]


# StopMigrationWorkflowRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# StopMigrationWorkflowResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

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

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### previous
- **Type**: typing.Optional[typing.List[str]]

### next
- **Type**: typing.Optional[typing.List[str]]


# TemplateStepSummaryTypeDef

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


# TemplateSummaryTypeDef

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# ToolTypeDef

### name
- **Type**: typing.Optional[str]

### url
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateMigrationWorkflowRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### inputParameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.StepInputTypeDef]]

### stepTargets
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateMigrationWorkflowResponseTypeDef

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
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.StepInputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### templateName
- **Type**: typing.Optional[str]

### templateDescription
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


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


# UpdateWorkflowStepGroupRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[str]]

### previous
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateWorkflowStepGroupResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ToolTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkflowStepRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepAutomationConfigurationTypeDef]

### stepTarget
- **Type**: typing.Optional[typing.Sequence[str]]

### outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepOutputTypeDef]]

### previous
- **Type**: typing.Optional[typing.Sequence[str]]

### next
- **Type**: typing.Optional[typing.Sequence[str]]

### status
- **Type**: typing.Optional[typing.Literal['AWAITING_DEPENDENCIES', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'PAUSED', 'READY', 'SKIPPED', 'USER_ATTENTION_REQUIRED']]


# UpdateWorkflowStepResponseTypeDef

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


# WorkflowStepGroupSummaryTypeDef

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


# WorkflowStepOutputTypeDef

### name
- **Type**: typing.Optional[str]

### dataType
- **Type**: typing.Optional[typing.Literal['INTEGER', 'STRING', 'STRINGLIST', 'STRINGMAP']]

### required
- **Type**: typing.Optional[bool]

### value
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.migrationhuborchestrator_classes.WorkflowStepOutputUnionTypeDef]


# WorkflowStepOutputUnionTypeDef

### integerValue
- **Type**: typing.Optional[int]

### stringValue
- **Type**: typing.Optional[str]

### listOfStringValue
- **Type**: typing.Optional[typing.Sequence[str]]


# WorkflowStepSummaryTypeDef

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


