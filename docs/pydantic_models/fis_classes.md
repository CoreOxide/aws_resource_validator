# Fis Classes

# ActionParameterTypeDef

### description
- **Type**: typing.Optional[str]

### required
- **Type**: typing.Optional[bool]


# ActionSummaryTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### targets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis_classes.ActionTargetTypeDef]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ActionTargetTypeDef

### resourceType
- **Type**: typing.Optional[str]


# ActionTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis_classes.ActionParameterTypeDef]]

### targets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis_classes.ActionTargetTypeDef]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# CreateExperimentTemplateRequestRequestTypeDef

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


# CreateTargetAccountConfigurationRequestRequestTypeDef

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


# DeleteExperimentTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteExperimentTemplateResponseTypeDef

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTargetAccountConfigurationRequestRequestTypeDef

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


# ExperimentS3LogConfigurationTypeDef

### bucketName
- **Type**: typing.Optional[str]

### prefix
- **Type**: typing.Optional[str]


# ExperimentStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['completed', 'failed', 'initiating', 'pending', 'running', 'stopped', 'stopping']]

### reason
- **Type**: typing.Optional[str]


# ExperimentStopConditionTypeDef

### source
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# ExperimentSummaryTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### experimentTemplateId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentStateTypeDef]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### experimentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentOptionsTypeDef]


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

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### targets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateTargetTypeDef]]

### actions
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateActionTypeDef]]

### stopConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateStopConditionTypeDef]]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### roleArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateLogConfigurationTypeDef]

### experimentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateExperimentOptionsTypeDef]

### targetAccountConfigurationsCount
- **Type**: typing.Optional[int]


# ExperimentTypeDef

### id
- **Type**: typing.Optional[str]

### arn
- **Type**: typing.Optional[str]

### experimentTemplateId
- **Type**: typing.Optional[str]

### roleArn
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentStateTypeDef]

### targets
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis_classes.ExperimentTargetTypeDef]]

### actions
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.fis_classes.ExperimentActionTypeDef]]

### stopConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentStopConditionTypeDef]]

### creationTime
- **Type**: typing.Optional[datetime.datetime]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentLogConfigurationTypeDef]

### experimentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.ExperimentOptionsTypeDef]

### targetAccountConfigurationsCount
- **Type**: typing.Optional[int]


# GetActionRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetActionResponseTypeDef

### action
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ActionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExperimentRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetExperimentResponseTypeDef

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetExperimentTargetAccountConfigurationRequestRequestTypeDef

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


# GetExperimentTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# GetExperimentTemplateResponseTypeDef

### experimentTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTargetAccountConfigurationRequestRequestTypeDef

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


# GetTargetResourceTypeRequestRequestTypeDef

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


# ListActionsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListActionsResponseTypeDef

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.ActionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExperimentResolvedTargetsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExperimentTargetAccountConfigurationsRequestRequestTypeDef

### experimentId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentTargetAccountConfigurationsResponseTypeDef

### targetAccountConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentTargetAccountConfigurationSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExperimentTemplatesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListExperimentTemplatesResponseTypeDef

### experimentTemplates
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.ExperimentTemplateSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListExperimentsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTargetAccountConfigurationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTargetResourceTypesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTargetResourceTypesResponseTypeDef

### targetResourceTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.fis_classes.TargetResourceTypeSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# StartExperimentExperimentOptionsInputTypeDef

### actionsMode
- **Type**: typing.Optional[typing.Literal['run-all', 'skip-all']]


# StartExperimentRequestRequestTypeDef

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


# StopExperimentRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes


# StopExperimentResponseTypeDef

### experiment
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ExperimentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fis_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

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


# UpdateExperimentTemplateRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### stopConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fis_classes.UpdateExperimentTemplateStopConditionInputTypeDef]]

### targets
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.fis_classes.UpdateExperimentTemplateTargetInputTypeDef]]

### actions
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.fis_classes.UpdateExperimentTemplateActionInputItemTypeDef]]

### roleArn
- **Type**: typing.Optional[str]

### logConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.UpdateExperimentTemplateLogConfigurationInputTypeDef]

### experimentOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fis_classes.UpdateExperimentTemplateExperimentOptionsInputTypeDef]


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


# UpdateTargetAccountConfigurationRequestRequestTypeDef

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


