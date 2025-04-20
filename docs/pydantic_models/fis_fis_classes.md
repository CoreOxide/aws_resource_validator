# Fis Fis Classes

# Action

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis.fis_classes.ActionParameter]]

### targets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis.fis_classes.ActionTarget]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ActionParameter

### description
- **Type**: typing.Optional[str]

### required
- **Type**: typing.Optional[bool]


# ActionSummary

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### targets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis.fis_classes.ActionTarget]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ActionTarget

### resourceType
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateExperimentTemplateActionInput

### actionId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]

### targets
- **Type**: typing.Optional[typing.Dict[str, str]]

### startAfter
- **Type**: typing.Optional[typing.List[str]]


# CreateExperimentTemplateExperimentOptionsInput

### accountTargeting
- **Type**: typing.Optional[typing.Literal['multi-account', 'single-account']]

### emptyTargetResolutionMode
- **Type**: typing.Optional[typing.Literal['fail', 'skip']]


# CreateExperimentTemplateLogConfigurationInput

### logSchemaVersion
- **Type**: <class 'int'>
- **Required**: Yes

### cloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateCloudWatchLogsLogConfigurationInput]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateS3LogConfigurationInput]


# CreateExperimentTemplateReportConfigurationInput

### outputs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateReportConfigurationOutputsInput]

### dataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateReportConfigurationDataSourcesInput]

### preExperimentDuration
- **Type**: typing.Optional[str]

### postExperimentDuration
- **Type**: typing.Optional[str]


# CreateExperimentTemplateRequest

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### stopConditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.CreateExperimentTemplateStopConditionInput]
- **Required**: Yes

### actions
- **Type**: typing.Dict[str, aws_resource_validator.pydantic_models.fis.fis_classes.CreateExperimentTemplateActionInput]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis.fis_classes.CreateExperimentTemplateTargetInput]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.CreateExperimentTemplateLogConfigurationInput]

### experimentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.CreateExperimentTemplateExperimentOptionsInput]

### experimentReportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.CreateExperimentTemplateReportConfigurationInput]


# CreateExperimentTemplateResponse

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# CreateExperimentTemplateStopConditionInput

### source
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# CreateExperimentTemplateTargetInput

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### selectionMode
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### resourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateTargetInputFilter]]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateTargetAccountConfigurationRequest

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


# CreateTargetAccountConfigurationResponse

### targetAccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.TargetAccountConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteExperimentTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExperimentTemplateResponse

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTargetAccountConfigurationRequest

### experimentTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTargetAccountConfigurationResponse

### targetAccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.TargetAccountConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# Experiment

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### experimentTemplateId
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentState]

### targets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTarget]]

### actions
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentAction]]

### stopConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentStopCondition]]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentLogConfiguration]

### experimentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentOptions]

### targetAccountConfigurationsCount
- **Type**: typing.Optional[int]

### experimentReportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentReportConfiguration]

### experimentReport
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentReport]


# ExperimentAction

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentActionState]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# ExperimentActionState

### status
- **Type**: typing.Optional[typing.Literal['cancelled', 'completed', 'failed', 'initiating', 'pending', 'running', 'skipped', 'stopped', 'stopping']]

### reason
- **Type**: typing.Optional[str]


# ExperimentCloudWatchLogsLogConfiguration

### logGroupArn
- **Type**: typing.Optional[str]


# ExperimentError

### accountId
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[str]


# ExperimentLogConfiguration

### cloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentCloudWatchLogsLogConfiguration]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentS3LogConfiguration]

### logSchemaVersion
- **Type**: typing.Optional[int]


# ExperimentOptions

### accountTargeting
- **Type**: typing.Optional[typing.Literal['multi-account', 'single-account']]

### emptyTargetResolutionMode
- **Type**: typing.Optional[typing.Literal['fail', 'skip']]

### actionsMode
- **Type**: typing.Optional[typing.Literal['run-all', 'skip-all']]


# ExperimentReport

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentReportState]

### s3Reports
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentReportS3Report]]


# ExperimentReportConfiguration

### outputs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentReportConfigurationOutputs]

### dataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentReportConfigurationDataSources]

### preExperimentDuration
- **Type**: typing.Optional[str]

### postExperimentDuration
- **Type**: typing.Optional[str]


# ExperimentReportConfigurationCloudWatchDashboard

### dashboardIdentifier
- **Type**: typing.Optional[str]


# ExperimentReportConfigurationDataSources

### cloudWatchDashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentReportConfigurationCloudWatchDashboard]]


# ExperimentReportConfigurationOutputs

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentReportConfigurationOutputsS3Configuration]


# ExperimentReportConfigurationOutputsS3Configuration

### bucketName
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ExperimentReportError

### code
- **Type**: typing.Optional[str]


# ExperimentReportS3Report

### arn
- **Type**: typing.Optional[str]

### reportType
- **Type**: typing.Optional[str]


# ExperimentReportState

### status
- **Type**: typing.Optional[typing.Literal['cancelled', 'completed', 'failed', 'pending', 'running']]

### reason
- **Type**: typing.Optional[str]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentReportError]


# ExperimentS3LogConfiguration

### bucketName
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ExperimentState

### status
- **Type**: typing.Optional[typing.Literal['cancelled', 'completed', 'failed', 'initiating', 'pending', 'running', 'stopped', 'stopping']]

### reason
- **Type**: typing.Optional[str]

### error
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentError]


# ExperimentStopCondition

### source
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# ExperimentSummary

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### experimentTemplateId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentState]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### experimentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentOptions]


# ExperimentTarget

### resourceType
- **Type**: typing.Optional[str]

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### resourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTargetFilter]]

### selectionMode
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ExperimentTargetAccountConfiguration

### roleArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# ExperimentTargetAccountConfigurationSummary

### roleArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# ExperimentTargetFilter

### path
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


# ExperimentTemplate

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### targets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateTarget]]

### actions
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateAction]]

### stopConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateStopCondition]]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateLogConfiguration]

### experimentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateExperimentOptions]

### targetAccountConfigurationsCount
- **Type**: typing.Optional[int]

### experimentReportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateReportConfiguration]


# ExperimentTemplateAction

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


# ExperimentTemplateCloudWatchLogsLogConfiguration

### logGroupArn
- **Type**: typing.Optional[str]


# ExperimentTemplateCloudWatchLogsLogConfigurationInput

### logGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# ExperimentTemplateExperimentOptions

### accountTargeting
- **Type**: typing.Optional[typing.Literal['multi-account', 'single-account']]

### emptyTargetResolutionMode
- **Type**: typing.Optional[typing.Literal['fail', 'skip']]


# ExperimentTemplateLogConfiguration

### cloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateCloudWatchLogsLogConfiguration]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateS3LogConfiguration]

### logSchemaVersion
- **Type**: typing.Optional[int]


# ExperimentTemplateReportConfiguration

### outputs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateReportConfigurationOutputs]

### dataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateReportConfigurationDataSources]

### preExperimentDuration
- **Type**: typing.Optional[str]

### postExperimentDuration
- **Type**: typing.Optional[str]


# ExperimentTemplateReportConfigurationCloudWatchDashboard

### dashboardIdentifier
- **Type**: typing.Optional[str]


# ExperimentTemplateReportConfigurationDataSources

### cloudWatchDashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateReportConfigurationCloudWatchDashboard]]


# ExperimentTemplateReportConfigurationDataSourcesInput

### cloudWatchDashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ReportConfigurationCloudWatchDashboardInput]]


# ExperimentTemplateReportConfigurationOutputs

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ReportConfigurationS3Output]


# ExperimentTemplateReportConfigurationOutputsInput

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ReportConfigurationS3OutputInput]


# ExperimentTemplateS3LogConfiguration

### bucketName
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ExperimentTemplateS3LogConfigurationInput

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### prefix
- **Type**: typing.Optional[str]


# ExperimentTemplateStopCondition

### source
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# ExperimentTemplateSummary

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ExperimentTemplateTarget

### resourceType
- **Type**: typing.Optional[str]

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### resourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateTargetFilter]]

### selectionMode
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# ExperimentTemplateTargetFilter

### path
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


# ExperimentTemplateTargetInputFilter

### path
- **Type**: <class 'str'>
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes


# GetActionRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetActionResponse

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.Action'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# GetExperimentRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetExperimentResponse

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.Experiment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# GetExperimentTargetAccountConfigurationRequest

### experimentId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetExperimentTargetAccountConfigurationResponse

### targetAccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTargetAccountConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# GetExperimentTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetExperimentTemplateResponse

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# GetSafetyLeverRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetSafetyLeverResponse

### safetyLever
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.SafetyLever'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# GetTargetAccountConfigurationRequest

### experimentTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### accountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTargetAccountConfigurationResponse

### targetAccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.TargetAccountConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# GetTargetResourceTypeRequest

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes


# GetTargetResourceTypeResponse

### targetResourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.TargetResourceType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# ListActionsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListActionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.PaginatorConfig]


# ListActionsResponse

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ActionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentResolvedTargetsRequest

### experimentId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### targetName
- **Type**: typing.Optional[str]


# ListExperimentResolvedTargetsRequestPaginate

### experimentId
- **Type**: <class 'str'>
- **Required**: Yes

### targetName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.PaginatorConfig]


# ListExperimentResolvedTargetsResponse

### resolvedTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ResolvedTarget]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentTargetAccountConfigurationsRequest

### experimentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentTargetAccountConfigurationsResponse

### targetAccountConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTargetAccountConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentTemplatesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentTemplatesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.PaginatorConfig]


# ListExperimentTemplatesResponse

### experimentTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### experimentTemplateId
- **Type**: typing.Optional[str]


# ListExperimentsRequestPaginate

### experimentTemplateId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.PaginatorConfig]


# ListExperimentsResponse

### experiments
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# ListTargetAccountConfigurationsRequest

### experimentTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTargetAccountConfigurationsRequestPaginate

### experimentTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.PaginatorConfig]


# ListTargetAccountConfigurationsResponse

### targetAccountConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.TargetAccountConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTargetResourceTypesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTargetResourceTypesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.PaginatorConfig]


# ListTargetResourceTypesResponse

### targetResourceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.TargetResourceTypeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
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


# ReportConfigurationCloudWatchDashboardInput

### dashboardIdentifier
- **Type**: typing.Optional[str]


# ReportConfigurationS3Output

### bucketName
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ReportConfigurationS3OutputInput

### bucketName
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ResolvedTarget

### resourceType
- **Type**: typing.Optional[str]

### targetName
- **Type**: typing.Optional[str]

### targetInformation
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# SafetyLever

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.SafetyLeverState]


# SafetyLeverState

### status
- **Type**: typing.Optional[typing.Literal['disengaged', 'engaged', 'engaging']]

### reason
- **Type**: typing.Optional[str]


# StartExperimentExperimentOptionsInput

### actionsMode
- **Type**: typing.Optional[typing.Literal['run-all', 'skip-all']]


# StartExperimentRequest

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### experimentTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### experimentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.StartExperimentExperimentOptionsInput]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartExperimentResponse

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.Experiment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# StopExperimentRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes


# StopExperimentResponse

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.Experiment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TargetAccountConfiguration

### roleArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# TargetAccountConfigurationSummary

### roleArn
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# TargetResourceType

### resourceType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis.fis_classes.TargetResourceTypeParameter]]


# TargetResourceTypeParameter

### description
- **Type**: typing.Optional[str]

### required
- **Type**: typing.Optional[bool]


# TargetResourceTypeSummary

### resourceType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Optional[typing.List[str]]


# UpdateExperimentTemplateActionInputItem

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


# UpdateExperimentTemplateExperimentOptionsInput

### emptyTargetResolutionMode
- **Type**: typing.Optional[typing.Literal['fail', 'skip']]


# UpdateExperimentTemplateLogConfigurationInput

### cloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateCloudWatchLogsLogConfigurationInput]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateS3LogConfigurationInput]

### logSchemaVersion
- **Type**: typing.Optional[int]


# UpdateExperimentTemplateReportConfigurationInput

### outputs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateReportConfigurationOutputsInput]

### dataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateReportConfigurationDataSourcesInput]

### preExperimentDuration
- **Type**: typing.Optional[str]

### postExperimentDuration
- **Type**: typing.Optional[str]


# UpdateExperimentTemplateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### stopConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.UpdateExperimentTemplateStopConditionInput]]

### targets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis.fis_classes.UpdateExperimentTemplateTargetInput]]

### actions
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis.fis_classes.UpdateExperimentTemplateActionInputItem]]

### roleArn
- **Type**: typing.Optional[str]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.UpdateExperimentTemplateLogConfigurationInput]

### experimentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.UpdateExperimentTemplateExperimentOptionsInput]

### experimentReportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis.fis_classes.UpdateExperimentTemplateReportConfigurationInput]


# UpdateExperimentTemplateResponse

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateExperimentTemplateStopConditionInput

### source
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# UpdateExperimentTemplateTargetInput

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes

### selectionMode
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### resourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis.fis_classes.ExperimentTemplateTargetInputFilter]]

### parameters
- **Type**: typing.Optional[typing.Dict[str, str]]


# UpdateSafetyLeverStateInput

### status
- **Type**: typing.Literal['disengaged', 'engaged']
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSafetyLeverStateRequest

### id
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.UpdateSafetyLeverStateInput'>
- **Required**: Yes


# UpdateSafetyLeverStateResponse

### safetyLever
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.SafetyLever'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTargetAccountConfigurationRequest

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


# UpdateTargetAccountConfigurationResponse

### targetAccountConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.TargetAccountConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis.fis_classes.ResponseMetadata'>
- **Required**: Yes


