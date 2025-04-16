# Fis Classes

# Action

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionParameter

### description
- **Type**: typing.Optional[str]

### required
- **Type**: typing.Optional[bool]


# ActionSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### targets
- **Type**: typing.Optional[typing.Mapping[str, str]]

### startAfter
- **Type**: typing.Optional[typing.Sequence[str]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateCloudWatchLogsLogConfigurationInput]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateS3LogConfigurationInput]


# CreateExperimentTemplateReportConfigurationInput

### outputs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationOutputsInput]

### dataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationDataSourcesInput]

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.fis_classes.CreateExperimentTemplateStopConditionInput]
- **Required**: Yes

### actions
- **Type**: typing.Mapping[str, aws_resource_validator.pydantic_models.fis_classes.CreateExperimentTemplateActionInput]
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### targets
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.fis_classes.CreateExperimentTemplateTargetInput]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.CreateExperimentTemplateLogConfigurationInput]

### experimentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.CreateExperimentTemplateExperimentOptionsInput]

### experimentReportConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.CreateExperimentTemplateReportConfigurationInput]


# CreateExperimentTemplateResponse

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateTargetInputFilter]]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.TargetAccountConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteExperimentTemplateResponse

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.TargetAccountConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
- **Required**: Yes


# Experiment

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentActionState]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentCloudWatchLogsLogConfiguration]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentS3LogConfiguration]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportState]

### s3Reports
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportS3Report]]


# ExperimentReportConfiguration

### outputs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportConfigurationOutputs]

### dataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportConfigurationDataSources]

### preExperimentDuration
- **Type**: typing.Optional[str]

### postExperimentDuration
- **Type**: typing.Optional[str]


# ExperimentReportConfigurationCloudWatchDashboard

### dashboardIdentifier
- **Type**: typing.Optional[str]


# ExperimentReportConfigurationDataSources

### cloudWatchDashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportConfigurationCloudWatchDashboard]]


# ExperimentReportConfigurationOutputs

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportConfigurationOutputsS3Configuration]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentReportError]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentError]


# ExperimentStopCondition

### source
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# ExperimentSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExperimentTarget

### resourceType
- **Type**: typing.Optional[str]

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### resourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentTargetFilter]]

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateCloudWatchLogsLogConfiguration]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateS3LogConfiguration]

### logSchemaVersion
- **Type**: typing.Optional[int]


# ExperimentTemplateReportConfiguration

### outputs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationOutputs]

### dataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationDataSources]

### preExperimentDuration
- **Type**: typing.Optional[str]

### postExperimentDuration
- **Type**: typing.Optional[str]


# ExperimentTemplateReportConfigurationCloudWatchDashboard

### dashboardIdentifier
- **Type**: typing.Optional[str]


# ExperimentTemplateReportConfigurationDataSources

### cloudWatchDashboards
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationCloudWatchDashboard]]


# ExperimentTemplateReportConfigurationDataSourcesInput

### cloudWatchDashboards
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fis_classes.ReportConfigurationCloudWatchDashboardInput]]


# ExperimentTemplateReportConfigurationOutputs

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ReportConfigurationS3Output]


# ExperimentTemplateReportConfigurationOutputsInput

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ReportConfigurationS3OutputInput]


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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ExperimentTemplateTarget

### resourceType
- **Type**: typing.Optional[str]

### resourceArns
- **Type**: typing.Optional[typing.List[str]]

### resourceTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateTargetFilter]]

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
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetActionResponse

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.Action'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
- **Required**: Yes


# GetExperimentResponse

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.Experiment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTargetAccountConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
- **Required**: Yes


# GetExperimentTemplateResponse

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
- **Required**: Yes


# GetSafetyLeverResponse

### safetyLever
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.SafetyLever'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.TargetAccountConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
- **Required**: Yes


# GetTargetResourceTypeRequest

### resourceType
- **Type**: <class 'str'>
- **Required**: Yes


# GetTargetResourceTypeResponse

### targetResourceType
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.TargetResourceType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
- **Required**: Yes


# ListActionsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListActionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.PaginatorConfig]


# ListActionsResponse

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.ActionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.PaginatorConfig]


# ListExperimentResolvedTargetsResponse

### resolvedTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.ResolvedTarget]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentTargetAccountConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.PaginatorConfig]


# ListExperimentTemplatesResponse

### experimentTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.PaginatorConfig]


# ListExperimentsResponse

### experiments
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.PaginatorConfig]


# ListTargetAccountConfigurationsResponse

### targetAccountConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.TargetAccountConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.PaginatorConfig]


# ListTargetResourceTypesResponse

### targetResourceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.TargetResourceTypeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.StartExperimentExperimentOptionsInput]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartExperimentResponse

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.Experiment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
- **Required**: Yes


# StopExperimentResponse

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.Experiment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis_classes.TargetResourceTypeParameter]]


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
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateExperimentTemplateActionInputItem

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


# UpdateExperimentTemplateExperimentOptionsInput

### emptyTargetResolutionMode
- **Type**: typing.Optional[typing.Literal['fail', 'skip']]


# UpdateExperimentTemplateLogConfigurationInput

### cloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateCloudWatchLogsLogConfigurationInput]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateS3LogConfigurationInput]

### logSchemaVersion
- **Type**: typing.Optional[int]


# UpdateExperimentTemplateReportConfigurationInput

### outputs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationOutputsInput]

### dataSources
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateReportConfigurationDataSourcesInput]

### preExperimentDuration
- **Type**: typing.Optional[str]

### postExperimentDuration
- **Type**: typing.Optional[str]


# UpdateExperimentTemplateResponse

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.Sequence[str]]

### resourceTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateTargetInputFilter]]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateSafetyLeverStateInput

### status
- **Type**: typing.Literal['disengaged', 'engaged']
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSafetyLeverStateResponse

### safetyLever
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.SafetyLever'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.TargetAccountConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadata'>
- **Required**: Yes


