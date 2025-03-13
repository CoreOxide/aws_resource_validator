# Fis Classes

# ActionParameterTypeDef

### description
- **Type**: typing.Optional[str]

### required
- **Type**: typing.Optional[bool]


# ActionSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionTargetTypeDef

### resourceType
- **Type**: typing.Optional[str]


# ActionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateExperimentTemplateActionInputTypeDef

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### targets
- **Type**: typing.Optional[typing.Mapping[str, str]]

### startAfter
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateExperimentTemplateExperimentOptionsInputTypeDef

### accountTargeting
- **Type**: typing.Optional[typing.Literal['multi-account', 'single-account']]

### emptyTargetResolutionMode
- **Type**: typing.Optional[typing.Literal['fail', 'skip']]


# CreateExperimentTemplateLogConfigurationInputTypeDef

### logSchemaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### cloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateS3LogConfigurationInputTypeDef]


# CreateExperimentTemplateReportConfigurationInputTypeDef

### outputs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationOutputsInputTypeDef]

### dataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationDataSourcesInputTypeDef]

### preExperimentDuration
- **Type**: typing.Optional[str]

### postExperimentDuration
- **Type**: typing.Optional[str]


# CreateExperimentTemplateRequestTypeDef

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### stopConditions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.fis_classes.CreateExperimentTemplateStopConditionInputTypeDef]
- **Required**: Yes

### actions
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.fis_classes.CreateExperimentTemplateActionInputTypeDef]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.fis_classes.CreateExperimentTemplateTargetInputTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.CreateExperimentTemplateLogConfigurationInputTypeDef]

### experimentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.CreateExperimentTemplateExperimentOptionsInputTypeDef]

### experimentReportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.CreateExperimentTemplateReportConfigurationInputTypeDef]


# CreateExperimentTemplateResponseTypeDef

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateExperimentTemplateStopConditionInputTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# CreateExperimentTemplateTargetInputTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### selectionMode
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateTargetInputFilterTypeDef]]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateTargetAccountConfigurationRequestTypeDef

### experimentTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateTargetAccountConfigurationResponseTypeDef

### targetAccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.TargetAccountConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteExperimentTemplateResponseTypeDef

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTargetAccountConfigurationRequestTypeDef

### experimentTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTargetAccountConfigurationResponseTypeDef

### targetAccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.TargetAccountConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExperimentActionStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['cancelled', 'completed', 'failed', 'initiating', 'pending', 'running', 'skipped', 'stopped', 'stopping']]

### reason
- **Type**: typing.Optional[str]


# ExperimentActionTypeDef

### actionId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### targets
- **Type**: typing.Optional[typing.Dict[str, str]]

### startAfter
- **Type**: typing.Optional[typing.List[str]]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentActionStateTypeDef]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# ExperimentCloudWatchLogsLogConfigurationTypeDef

### logGroupArn
- **Type**: typing.Optional[str]


# ExperimentErrorTypeDef

### accountId
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[str]


# ExperimentLogConfigurationTypeDef

### cloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentCloudWatchLogsLogConfigurationTypeDef]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentS3LogConfigurationTypeDef]

### logSchemaVersion
- **Type**: typing.Optional[int]


# ExperimentOptionsTypeDef

### accountTargeting
- **Type**: typing.Optional[typing.Literal['multi-account', 'single-account']]

### emptyTargetResolutionMode
- **Type**: typing.Optional[typing.Literal['fail', 'skip']]

### actionsMode
- **Type**: typing.Optional[typing.Literal['run-all', 'skip-all']]


# ExperimentReportConfigurationCloudWatchDashboardTypeDef

### dashboardIdentifier
- **Type**: typing.Optional[str]


# ExperimentReportConfigurationDataSourcesTypeDef

### cloudWatchDashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportConfigurationCloudWatchDashboardTypeDef]]


# ExperimentReportConfigurationOutputsS3ConfigurationTypeDef

### bucketName
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ExperimentReportConfigurationOutputsTypeDef

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportConfigurationOutputsS3ConfigurationTypeDef]


# ExperimentReportConfigurationTypeDef

### outputs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportConfigurationOutputsTypeDef]

### dataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportConfigurationDataSourcesTypeDef]

### preExperimentDuration
- **Type**: typing.Optional[str]

### postExperimentDuration
- **Type**: typing.Optional[str]


# ExperimentReportErrorTypeDef

### code
- **Type**: typing.Optional[str]


# ExperimentReportS3ReportTypeDef

### arn
- **Type**: typing.Optional[str]

### reportType
- **Type**: typing.Optional[str]


# ExperimentReportStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['cancelled', 'completed', 'failed', 'pending', 'running']]

### reason
- **Type**: typing.Optional[str]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportErrorTypeDef]


# ExperimentReportTypeDef

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportStateTypeDef]

### s3Reports
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportS3ReportTypeDef]]


# ExperimentS3LogConfigurationTypeDef

### bucketName
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ExperimentStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['cancelled', 'completed', 'failed', 'initiating', 'pending', 'running', 'stopped', 'stopping']]

### reason
- **Type**: typing.Optional[str]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentErrorTypeDef]


# ExperimentStopConditionTypeDef

### source
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# ExperimentSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExperimentTargetAccountConfigurationSummaryTypeDef

### roleArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# ExperimentTargetAccountConfigurationTypeDef

### roleArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# ExperimentTargetFilterTypeDef

### path
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


# ExperimentTargetTypeDef

### resourceType
- **Type**: typing.Optional[str]

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### resourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentTargetFilterTypeDef]]

### selectionMode
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ExperimentTemplateActionTypeDef

### actionId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### targets
- **Type**: typing.Optional[typing.Dict[str, str]]

### startAfter
- **Type**: typing.Optional[typing.List[str]]


# ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef

### logGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef

### logGroupArn
- **Type**: typing.Optional[str]


# ExperimentTemplateExperimentOptionsTypeDef

### accountTargeting
- **Type**: typing.Optional[typing.Literal['multi-account', 'single-account']]

### emptyTargetResolutionMode
- **Type**: typing.Optional[typing.Literal['fail', 'skip']]


# ExperimentTemplateLogConfigurationTypeDef

### cloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateCloudWatchLogsLogConfigurationTypeDef]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateS3LogConfigurationTypeDef]

### logSchemaVersion
- **Type**: typing.Optional[int]


# ExperimentTemplateReportConfigurationCloudWatchDashboardTypeDef

### dashboardIdentifier
- **Type**: typing.Optional[str]


# ExperimentTemplateReportConfigurationDataSourcesInputTypeDef

### cloudWatchDashboards
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fis_classes.ReportConfigurationCloudWatchDashboardInputTypeDef]]


# ExperimentTemplateReportConfigurationDataSourcesTypeDef

### cloudWatchDashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationCloudWatchDashboardTypeDef]]


# ExperimentTemplateReportConfigurationOutputsInputTypeDef

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ReportConfigurationS3OutputInputTypeDef]


# ExperimentTemplateReportConfigurationOutputsTypeDef

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ReportConfigurationS3OutputTypeDef]


# ExperimentTemplateReportConfigurationTypeDef

### outputs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationOutputsTypeDef]

### dataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationDataSourcesTypeDef]

### preExperimentDuration
- **Type**: typing.Optional[str]

### postExperimentDuration
- **Type**: typing.Optional[str]


# ExperimentTemplateS3LogConfigurationInputTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]


# ExperimentTemplateS3LogConfigurationTypeDef

### bucketName
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ExperimentTemplateStopConditionTypeDef

### source
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# ExperimentTemplateSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExperimentTemplateTargetFilterTypeDef

### path
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


# ExperimentTemplateTargetInputFilterTypeDef

### path
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ExperimentTemplateTargetTypeDef

### resourceType
- **Type**: typing.Optional[str]

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### resourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateTargetFilterTypeDef]]

### selectionMode
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ExperimentTemplateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExperimentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetActionResponseTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ActionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExperimentResponseTypeDef

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExperimentTargetAccountConfigurationRequestTypeDef

### experimentId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExperimentTargetAccountConfigurationResponseTypeDef

### targetAccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTargetAccountConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExperimentTemplateResponseTypeDef

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSafetyLeverResponseTypeDef

### safetyLever
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.SafetyLeverTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTargetAccountConfigurationRequestTypeDef

### experimentTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTargetAccountConfigurationResponseTypeDef

### targetAccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.TargetAccountConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTargetResourceTypeRequestTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes


# GetTargetResourceTypeResponseTypeDef

### targetResourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.TargetResourceTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListActionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.PaginatorConfigTypeDef]


# ListActionsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListActionsResponseTypeDef

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.ActionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentResolvedTargetsRequestPaginateTypeDef

### experimentId
- **Type**: <class 'str'>
- **Required**: Yes

### targetName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.PaginatorConfigTypeDef]


# ListExperimentResolvedTargetsRequestTypeDef

### experimentId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### targetName
- **Type**: typing.Optional[str]


# ListExperimentResolvedTargetsResponseTypeDef

### resolvedTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.ResolvedTargetTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentTargetAccountConfigurationsRequestTypeDef

### experimentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentTargetAccountConfigurationsResponseTypeDef

### targetAccountConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentTargetAccountConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentTemplatesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.PaginatorConfigTypeDef]


# ListExperimentTemplatesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentTemplatesResponseTypeDef

### experimentTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentsRequestPaginateTypeDef

### experimentTemplateId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.PaginatorConfigTypeDef]


# ListExperimentsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### experimentTemplateId
- **Type**: typing.Optional[str]


# ListExperimentsResponseTypeDef

### experiments
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTargetAccountConfigurationsRequestPaginateTypeDef

### experimentTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.PaginatorConfigTypeDef]


# ListTargetAccountConfigurationsRequestTypeDef

### experimentTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTargetAccountConfigurationsResponseTypeDef

### targetAccountConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.TargetAccountConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTargetResourceTypesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.PaginatorConfigTypeDef]


# ListTargetResourceTypesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTargetResourceTypesResponseTypeDef

### targetResourceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.TargetResourceTypeSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
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


# ReportConfigurationCloudWatchDashboardInputTypeDef

### dashboardIdentifier
- **Type**: typing.Optional[str]


# ReportConfigurationS3OutputInputTypeDef

### bucketName
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ReportConfigurationS3OutputTypeDef

### bucketName
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ResolvedTargetTypeDef

### resourceType
- **Type**: typing.Optional[str]

### targetName
- **Type**: typing.Optional[str]

### targetInformation
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# SafetyLeverStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['disengaged', 'engaged', 'engaging']]

### reason
- **Type**: typing.Optional[str]


# SafetyLeverTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartExperimentExperimentOptionsInputTypeDef

### actionsMode
- **Type**: typing.Optional[typing.Literal['run-all', 'skip-all']]


# StartExperimentRequestTypeDef

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### experimentTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### experimentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.StartExperimentExperimentOptionsInputTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartExperimentResponseTypeDef

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopExperimentResponseTypeDef

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TargetAccountConfigurationSummaryTypeDef

### roleArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# TargetAccountConfigurationTypeDef

### roleArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# TargetResourceTypeParameterTypeDef

### description
- **Type**: typing.Optional[str]

### required
- **Type**: typing.Optional[bool]


# TargetResourceTypeSummaryTypeDef

### resourceType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# TargetResourceTypeTypeDef

### resourceType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis_classes.TargetResourceTypeParameterTypeDef]]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateExperimentTemplateActionInputItemTypeDef

### actionId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### targets
- **Type**: typing.Optional[typing.Mapping[str, str]]

### startAfter
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateExperimentTemplateExperimentOptionsInputTypeDef

### emptyTargetResolutionMode
- **Type**: typing.Optional[typing.Literal['fail', 'skip']]


# UpdateExperimentTemplateLogConfigurationInputTypeDef

### cloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateCloudWatchLogsLogConfigurationInputTypeDef]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateS3LogConfigurationInputTypeDef]

### logSchemaVersion
- **Type**: typing.Optional[int]


# UpdateExperimentTemplateReportConfigurationInputTypeDef

### outputs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationOutputsInputTypeDef]

### dataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationDataSourcesInputTypeDef]

### preExperimentDuration
- **Type**: typing.Optional[str]

### postExperimentDuration
- **Type**: typing.Optional[str]


# UpdateExperimentTemplateResponseTypeDef

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateExperimentTemplateStopConditionInputTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# UpdateExperimentTemplateTargetInputTypeDef

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### selectionMode
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateTargetInputFilterTypeDef]]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateSafetyLeverStateInputTypeDef

### status
- **Type**: typing.Literal['disengaged', 'engaged']
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSafetyLeverStateResponseTypeDef

### safetyLever
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.SafetyLeverTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTargetAccountConfigurationRequestTypeDef

### experimentTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UpdateTargetAccountConfigurationResponseTypeDef

### targetAccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.TargetAccountConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


