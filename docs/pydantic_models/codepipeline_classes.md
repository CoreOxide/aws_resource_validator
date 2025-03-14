# Codepipeline Classes

# AWSSessionCredentialsTypeDef

### accessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### secretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes


# AcknowledgeJobInputTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### nonce
- **Type**: <class 'str'>
- **Required**: Yes


# AcknowledgeJobOutputTypeDef

### status
- **Type**: typing.Literal['Created', 'Dispatched', 'Failed', 'InProgress', 'Queued', 'Succeeded', 'TimedOut']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AcknowledgeThirdPartyJobInputTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### nonce
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# AcknowledgeThirdPartyJobOutputTypeDef

### status
- **Type**: typing.Literal['Created', 'Dispatched', 'Failed', 'InProgress', 'Queued', 'Succeeded', 'TimedOut']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ActionConfigurationPropertyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionConfigurationTypeDef

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]


# ActionContextTypeDef

### name
- **Type**: typing.Optional[str]

### actionExecutionId
- **Type**: typing.Optional[str]


# ActionDeclarationOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### actionTypeId
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeIdTypeDef'>
- **Required**: Yes

### runOrder
- **Type**: typing.Optional[int]

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]

### commands
- **Type**: typing.Optional[typing.List[str]]

### outputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.OutputArtifactOutputTypeDef]]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.InputArtifactTypeDef]]

### outputVariables
- **Type**: typing.Optional[typing.List[str]]

### roleArn
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### timeoutInMinutes
- **Type**: typing.Optional[int]

### environmentVariables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.EnvironmentVariableTypeDef]]


# ActionDeclarationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### actionTypeId
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeIdTypeDef'>
- **Required**: Yes

### runOrder
- **Type**: typing.Optional[int]

### configuration
- **Type**: typing.Optional[typing.Mapping[str, str]]

### commands
- **Type**: typing.Optional[typing.Sequence[str]]

### outputArtifacts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.OutputArtifactTypeDef]]

### inputArtifacts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.InputArtifactTypeDef]]

### outputVariables
- **Type**: typing.Optional[typing.Sequence[str]]

### roleArn
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### timeoutInMinutes
- **Type**: typing.Optional[int]

### environmentVariables
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.EnvironmentVariableTypeDef]]


# ActionExecutionDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionExecutionFilterTypeDef

### pipelineExecutionId
- **Type**: typing.Optional[str]

### latestInPipelineExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.LatestInPipelineExecutionFilterTypeDef]


# ActionExecutionInputTypeDef

### actionTypeId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeIdTypeDef]

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]

### resolvedConfiguration
- **Type**: typing.Optional[typing.Dict[str, str]]

### roleArn
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactDetailTypeDef]]

### namespace
- **Type**: typing.Optional[str]


# ActionExecutionOutputTypeDef

### outputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactDetailTypeDef]]

### executionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionExecutionResultTypeDef]

### outputVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# ActionExecutionResultTypeDef

### externalExecutionId
- **Type**: typing.Optional[str]

### externalExecutionSummary
- **Type**: typing.Optional[str]

### externalExecutionUrl
- **Type**: typing.Optional[str]

### errorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ErrorDetailsTypeDef]

### logStreamARN
- **Type**: typing.Optional[str]


# ActionExecutionTypeDef

### actionExecutionId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Abandoned', 'Failed', 'InProgress', 'Succeeded']]

### summary
- **Type**: typing.Optional[str]

### lastStatusChange
- **Type**: typing.Optional[datetime.datetime]

### token
- **Type**: typing.Optional[str]

### lastUpdatedBy
- **Type**: typing.Optional[str]

### externalExecutionId
- **Type**: typing.Optional[str]

### externalExecutionUrl
- **Type**: typing.Optional[str]

### percentComplete
- **Type**: typing.Optional[int]

### errorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ErrorDetailsTypeDef]

### logStreamARN
- **Type**: typing.Optional[str]


# ActionRevisionOutputTypeDef

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionChangeId
- **Type**: <class 'str'>
- **Required**: Yes

### created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ActionRevisionTypeDef

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionChangeId
- **Type**: <class 'str'>
- **Required**: Yes

### created
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.TimestampTypeDef'>
- **Required**: Yes


# ActionRevisionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionStateTypeDef

### actionName
- **Type**: typing.Optional[str]

### currentRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionRevisionOutputTypeDef]

### latestExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionExecutionTypeDef]

### entityUrl
- **Type**: typing.Optional[str]

### revisionUrl
- **Type**: typing.Optional[str]


# ActionTypeArtifactDetailsTypeDef

### minimumCount
- **Type**: <class 'int'>
- **Required**: Yes

### maximumCount
- **Type**: <class 'int'>
- **Required**: Yes


# ActionTypeDeclarationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionTypeDeclarationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionTypeIdTypeDef

### category
- **Type**: typing.Literal['Approval', 'Build', 'Compute', 'Deploy', 'Invoke', 'Source', 'Test']
- **Required**: Yes

### owner
- **Type**: typing.Literal['AWS', 'Custom', 'ThirdParty']
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# ActionTypeIdentifierTypeDef

### category
- **Type**: typing.Literal['Approval', 'Build', 'Compute', 'Deploy', 'Invoke', 'Source', 'Test']
- **Required**: Yes

### owner
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# ActionTypePermissionsOutputTypeDef

### allowedAccounts
- **Type**: typing.List[str]
- **Required**: Yes


# ActionTypePermissionsTypeDef

### allowedAccounts
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ActionTypePropertyTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### optional
- **Type**: <class 'bool'>
- **Required**: Yes

### key
- **Type**: <class 'bool'>
- **Required**: Yes

### noEcho
- **Type**: <class 'bool'>
- **Required**: Yes

### queryable
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]


# ActionTypeSettingsTypeDef

### thirdPartyConfigurationUrl
- **Type**: typing.Optional[str]

### entityUrlTemplate
- **Type**: typing.Optional[str]

### executionUrlTemplate
- **Type**: typing.Optional[str]

### revisionUrlTemplate
- **Type**: typing.Optional[str]


# ActionTypeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionTypeUrlsTypeDef

### configurationUrl
- **Type**: typing.Optional[str]

### entityUrlTemplate
- **Type**: typing.Optional[str]

### executionUrlTemplate
- **Type**: typing.Optional[str]

### revisionUrlTemplate
- **Type**: typing.Optional[str]


# ApprovalResultTypeDef

### summary
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Approved', 'Rejected']
- **Required**: Yes


# ArtifactDetailTypeDef

### name
- **Type**: typing.Optional[str]

### s3location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.S3LocationTypeDef]


# ArtifactDetailsTypeDef

### minimumCount
- **Type**: <class 'int'>
- **Required**: Yes

### maximumCount
- **Type**: <class 'int'>
- **Required**: Yes


# ArtifactLocationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ArtifactRevisionTypeDef

### name
- **Type**: typing.Optional[str]

### revisionId
- **Type**: typing.Optional[str]

### revisionChangeIdentifier
- **Type**: typing.Optional[str]

### revisionSummary
- **Type**: typing.Optional[str]

### created
- **Type**: typing.Optional[datetime.datetime]

### revisionUrl
- **Type**: typing.Optional[str]


# ArtifactStoreTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ArtifactTypeDef

### name
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactLocationTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BeforeEntryConditionsOutputTypeDef

### conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ConditionOutputTypeDef]
- **Required**: Yes


# BeforeEntryConditionsTypeDef

### conditions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.ConditionTypeDef]
- **Required**: Yes


# BlockerDeclarationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConditionExecutionTypeDef

### status
- **Type**: typing.Optional[typing.Literal['Abandoned', 'Cancelled', 'Errored', 'Failed', 'InProgress', 'Overridden', 'Succeeded']]

### summary
- **Type**: typing.Optional[str]

### lastStatusChange
- **Type**: typing.Optional[datetime.datetime]


# ConditionOutputTypeDef

### result
- **Type**: typing.Optional[typing.Literal['FAIL', 'RETRY', 'ROLLBACK', 'SKIP']]

### rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.RuleDeclarationOutputTypeDef]]


# ConditionStateTypeDef

### latestExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ConditionExecutionTypeDef]

### ruleStates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.RuleStateTypeDef]]


# ConditionTypeDef

### result
- **Type**: typing.Optional[typing.Literal['FAIL', 'RETRY', 'ROLLBACK', 'SKIP']]

### rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.RuleDeclarationTypeDef]]


# CreateCustomActionTypeInputTypeDef

### category
- **Type**: typing.Literal['Approval', 'Build', 'Compute', 'Deploy', 'Invoke', 'Source', 'Test']
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### inputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactDetailsTypeDef'>
- **Required**: Yes

### outputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactDetailsTypeDef'>
- **Required**: Yes

### settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeSettingsTypeDef]

### configurationProperties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.ActionConfigurationPropertyTypeDef]]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.TagTypeDef]]


# CreateCustomActionTypeOutputTypeDef

### actionType
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePipelineInputTypeDef

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.PipelineDeclarationUnionTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.TagTypeDef]]


# CreatePipelineOutputTypeDef

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.PipelineDeclarationOutputTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CurrentRevisionTypeDef

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### changeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### created
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.TimestampTypeDef]

### revisionSummary
- **Type**: typing.Optional[str]


# DeleteCustomActionTypeInputTypeDef

### category
- **Type**: typing.Literal['Approval', 'Build', 'Compute', 'Deploy', 'Invoke', 'Source', 'Test']
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePipelineInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebhookInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterWebhookWithThirdPartyInputTypeDef

### webhookName
- **Type**: typing.Optional[str]


# DisableStageTransitionInputTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### transitionType
- **Type**: typing.Literal['Inbound', 'Outbound']
- **Required**: Yes

### reason
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableStageTransitionInputTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### transitionType
- **Type**: typing.Literal['Inbound', 'Outbound']
- **Required**: Yes


# EncryptionKeyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EnvironmentVariableTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorDetailsTypeDef

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# ExecutionDetailsTypeDef

### summary
- **Type**: typing.Optional[str]

### externalExecutionId
- **Type**: typing.Optional[str]

### percentComplete
- **Type**: typing.Optional[int]


# ExecutionTriggerTypeDef

### triggerType
- **Type**: typing.Optional[typing.Literal['AutomatedRollback', 'CloudWatchEvent', 'CreatePipeline', 'ManualRollback', 'PollForSourceChanges', 'PutActionRevision', 'StartPipelineExecution', 'Webhook', 'WebhookV2']]

### triggerDetail
- **Type**: typing.Optional[str]


# ExecutorConfigurationOutputTypeDef

### lambdaExecutorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.LambdaExecutorConfigurationTypeDef]

### jobWorkerExecutorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.JobWorkerExecutorConfigurationOutputTypeDef]


# ExecutorConfigurationTypeDef

### lambdaExecutorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.LambdaExecutorConfigurationTypeDef]

### jobWorkerExecutorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.JobWorkerExecutorConfigurationTypeDef]


# FailureConditionsOutputTypeDef

### result
- **Type**: typing.Optional[typing.Literal['FAIL', 'RETRY', 'ROLLBACK', 'SKIP']]

### retryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.RetryConfigurationTypeDef]

### conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ConditionOutputTypeDef]]


# FailureConditionsTypeDef

### result
- **Type**: typing.Optional[typing.Literal['FAIL', 'RETRY', 'ROLLBACK', 'SKIP']]

### retryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.RetryConfigurationTypeDef]

### conditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.ConditionTypeDef]]


# FailureDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetActionTypeInputTypeDef

### category
- **Type**: typing.Literal['Approval', 'Build', 'Compute', 'Deploy', 'Invoke', 'Source', 'Test']
- **Required**: Yes

### owner
- **Type**: <class 'str'>
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# GetActionTypeOutputTypeDef

### actionType
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeDeclarationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetJobDetailsInputTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobDetailsOutputTypeDef

### jobDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.JobDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPipelineExecutionInputTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPipelineExecutionOutputTypeDef

### pipelineExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.PipelineExecutionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPipelineInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: typing.Optional[int]


# GetPipelineOutputTypeDef

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.PipelineDeclarationOutputTypeDef'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.PipelineMetadataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPipelineStateInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetPipelineStateOutputTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineVersion
- **Type**: <class 'int'>
- **Required**: Yes

### stageStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.StageStateTypeDef]
- **Required**: Yes

### created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetThirdPartyJobDetailsInputTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetThirdPartyJobDetailsOutputTypeDef

### jobDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ThirdPartyJobDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GitBranchFilterCriteriaOutputTypeDef

### includes
- **Type**: typing.Optional[typing.List[str]]

### excludes
- **Type**: typing.Optional[typing.List[str]]


# GitBranchFilterCriteriaTypeDef

### includes
- **Type**: typing.Optional[typing.Sequence[str]]

### excludes
- **Type**: typing.Optional[typing.Sequence[str]]


# GitConfigurationOutputTypeDef

### sourceActionName
- **Type**: <class 'str'>
- **Required**: Yes

### push
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.GitPushFilterOutputTypeDef]]

### pullRequest
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.GitPullRequestFilterOutputTypeDef]]


# GitConfigurationTypeDef

### sourceActionName
- **Type**: <class 'str'>
- **Required**: Yes

### push
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.GitPushFilterTypeDef]]

### pullRequest
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.GitPullRequestFilterTypeDef]]


# GitFilePathFilterCriteriaOutputTypeDef

### includes
- **Type**: typing.Optional[typing.List[str]]

### excludes
- **Type**: typing.Optional[typing.List[str]]


# GitFilePathFilterCriteriaTypeDef

### includes
- **Type**: typing.Optional[typing.Sequence[str]]

### excludes
- **Type**: typing.Optional[typing.Sequence[str]]


# GitPullRequestFilterOutputTypeDef

### events
- **Type**: typing.Optional[typing.List[typing.Literal['CLOSED', 'OPEN', 'UPDATED']]]

### branches
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.GitBranchFilterCriteriaOutputTypeDef]

### filePaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.GitFilePathFilterCriteriaOutputTypeDef]


# GitPullRequestFilterTypeDef

### events
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CLOSED', 'OPEN', 'UPDATED']]]

### branches
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.GitBranchFilterCriteriaTypeDef]

### filePaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.GitFilePathFilterCriteriaTypeDef]


# GitPushFilterOutputTypeDef

### tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.GitTagFilterCriteriaOutputTypeDef]

### branches
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.GitBranchFilterCriteriaOutputTypeDef]

### filePaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.GitFilePathFilterCriteriaOutputTypeDef]


# GitPushFilterTypeDef

### tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.GitTagFilterCriteriaTypeDef]

### branches
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.GitBranchFilterCriteriaTypeDef]

### filePaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.GitFilePathFilterCriteriaTypeDef]


# GitTagFilterCriteriaOutputTypeDef

### includes
- **Type**: typing.Optional[typing.List[str]]

### excludes
- **Type**: typing.Optional[typing.List[str]]


# GitTagFilterCriteriaTypeDef

### includes
- **Type**: typing.Optional[typing.Sequence[str]]

### excludes
- **Type**: typing.Optional[typing.Sequence[str]]


# InputArtifactTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# JobDataTypeDef

### actionTypeId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeIdTypeDef]

### actionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionConfigurationTypeDef]

### pipelineContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineContextTypeDef]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactTypeDef]]

### outputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactTypeDef]]

### artifactCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.AWSSessionCredentialsTypeDef]

### continuationToken
- **Type**: typing.Optional[str]

### encryptionKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.EncryptionKeyTypeDef]


# JobDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobWorkerExecutorConfigurationOutputTypeDef

### pollingAccounts
- **Type**: typing.Optional[typing.List[str]]

### pollingServicePrincipals
- **Type**: typing.Optional[typing.List[str]]


# JobWorkerExecutorConfigurationTypeDef

### pollingAccounts
- **Type**: typing.Optional[typing.Sequence[str]]

### pollingServicePrincipals
- **Type**: typing.Optional[typing.Sequence[str]]


# LambdaExecutorConfigurationTypeDef

### lambdaFunctionArn
- **Type**: <class 'str'>
- **Required**: Yes


# LatestInPipelineExecutionFilterTypeDef

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeRange
- **Type**: typing.Literal['All', 'Latest']
- **Required**: Yes


# ListActionExecutionsOutputTypeDef

### actionExecutionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ActionExecutionDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListActionTypesInputPaginateTypeDef

### actionOwnerFilter
- **Type**: typing.Optional[typing.Literal['AWS', 'Custom', 'ThirdParty']]

### regionFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PaginatorConfigTypeDef]


# ListActionTypesInputTypeDef

### actionOwnerFilter
- **Type**: typing.Optional[typing.Literal['AWS', 'Custom', 'ThirdParty']]

### nextToken
- **Type**: typing.Optional[str]

### regionFilter
- **Type**: typing.Optional[str]


# ListActionTypesOutputTypeDef

### actionTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPipelineExecutionsOutputTypeDef

### pipelineExecutionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineExecutionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPipelinesInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PaginatorConfigTypeDef]


# ListPipelinesInputTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPipelinesOutputTypeDef

### pipelines
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRuleExecutionsOutputTypeDef

### ruleExecutionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.RuleExecutionDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRuleTypesInputTypeDef

### ruleOwnerFilter
- **Type**: typing.Optional[typing.Literal['AWS']]

### regionFilter
- **Type**: typing.Optional[str]


# ListRuleTypesOutputTypeDef

### ruleTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.RuleTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputPaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PaginatorConfigTypeDef]


# ListTagsForResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceOutputTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWebhookItemTypeDef

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.WebhookDefinitionOutputTypeDef'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### errorMessage
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[str]

### lastTriggered
- **Type**: typing.Optional[datetime.datetime]

### arn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.TagTypeDef]]


# ListWebhooksInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PaginatorConfigTypeDef]


# ListWebhooksInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWebhooksOutputTypeDef

### webhooks
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ListWebhookItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# OutputArtifactOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### files
- **Type**: typing.Optional[typing.List[str]]


# OutputArtifactTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### files
- **Type**: typing.Optional[typing.Sequence[str]]


# OverrideStageConditionInputTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### conditionType
- **Type**: typing.Literal['BEFORE_ENTRY', 'ON_SUCCESS']
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PipelineContextTypeDef

### pipelineName
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.StageContextTypeDef]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionContextTypeDef]

### pipelineArn
- **Type**: typing.Optional[str]

### pipelineExecutionId
- **Type**: typing.Optional[str]


# PipelineDeclarationOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### stages
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.StageDeclarationOutputTypeDef]
- **Required**: Yes

### artifactStore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactStoreTypeDef]

### artifactStores
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactStoreTypeDef]]

### version
- **Type**: typing.Optional[int]

### executionMode
- **Type**: typing.Optional[typing.Literal['PARALLEL', 'QUEUED', 'SUPERSEDED']]

### pipelineType
- **Type**: typing.Optional[typing.Literal['V1', 'V2']]

### variables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineVariableDeclarationTypeDef]]

### triggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineTriggerDeclarationOutputTypeDef]]


# PipelineDeclarationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### stages
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.StageDeclarationTypeDef]
- **Required**: Yes

### artifactStore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactStoreTypeDef]

### artifactStores
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactStoreTypeDef]]

### version
- **Type**: typing.Optional[int]

### executionMode
- **Type**: typing.Optional[typing.Literal['PARALLEL', 'QUEUED', 'SUPERSEDED']]

### pipelineType
- **Type**: typing.Optional[typing.Literal['V1', 'V2']]

### variables
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineVariableDeclarationTypeDef]]

### triggers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineTriggerDeclarationTypeDef]]


# PipelineDeclarationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PipelineExecutionFilterTypeDef

### succeededInStage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.SucceededInStageFilterTypeDef]


# PipelineExecutionSummaryTypeDef

### pipelineExecutionId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Failed', 'InProgress', 'Stopped', 'Stopping', 'Succeeded', 'Superseded']]

### statusSummary
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### sourceRevisions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.SourceRevisionTypeDef]]

### trigger
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ExecutionTriggerTypeDef]

### stopTrigger
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.StopExecutionTriggerTypeDef]

### executionMode
- **Type**: typing.Optional[typing.Literal['PARALLEL', 'QUEUED', 'SUPERSEDED']]

### executionType
- **Type**: typing.Optional[typing.Literal['ROLLBACK', 'STANDARD']]

### rollbackMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineRollbackMetadataTypeDef]


# PipelineExecutionTypeDef

### pipelineName
- **Type**: typing.Optional[str]

### pipelineVersion
- **Type**: typing.Optional[int]

### pipelineExecutionId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Cancelled', 'Failed', 'InProgress', 'Stopped', 'Stopping', 'Succeeded', 'Superseded']]

### statusSummary
- **Type**: typing.Optional[str]

### artifactRevisions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactRevisionTypeDef]]

### variables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ResolvedPipelineVariableTypeDef]]

### trigger
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ExecutionTriggerTypeDef]

### executionMode
- **Type**: typing.Optional[typing.Literal['PARALLEL', 'QUEUED', 'SUPERSEDED']]

### executionType
- **Type**: typing.Optional[typing.Literal['ROLLBACK', 'STANDARD']]

### rollbackMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineRollbackMetadataTypeDef]


# PipelineMetadataTypeDef

### pipelineArn
- **Type**: typing.Optional[str]

### created
- **Type**: typing.Optional[datetime.datetime]

### updated
- **Type**: typing.Optional[datetime.datetime]

### pollingDisabledAt
- **Type**: typing.Optional[datetime.datetime]


# PipelineRollbackMetadataTypeDef

### rollbackTargetPipelineExecutionId
- **Type**: typing.Optional[str]


# PipelineSummaryTypeDef

### name
- **Type**: typing.Optional[str]

### version
- **Type**: typing.Optional[int]

### pipelineType
- **Type**: typing.Optional[typing.Literal['V1', 'V2']]

### executionMode
- **Type**: typing.Optional[typing.Literal['PARALLEL', 'QUEUED', 'SUPERSEDED']]

### created
- **Type**: typing.Optional[datetime.datetime]

### updated
- **Type**: typing.Optional[datetime.datetime]


# PipelineTriggerDeclarationOutputTypeDef

### providerType
- **Type**: typing.Literal['CodeStarSourceConnection']
- **Required**: Yes

### gitConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.GitConfigurationOutputTypeDef'>
- **Required**: Yes


# PipelineTriggerDeclarationTypeDef

### providerType
- **Type**: typing.Literal['CodeStarSourceConnection']
- **Required**: Yes

### gitConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.GitConfigurationTypeDef'>
- **Required**: Yes


# PipelineVariableDeclarationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### defaultValue
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# PipelineVariableTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# PollForJobsInputTypeDef

### actionTypeId
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeIdTypeDef'>
- **Required**: Yes

### maxBatchSize
- **Type**: typing.Optional[int]

### queryParam
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PollForJobsOutputTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.JobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PollForThirdPartyJobsInputTypeDef

### actionTypeId
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeIdTypeDef'>
- **Required**: Yes

### maxBatchSize
- **Type**: typing.Optional[int]


# PollForThirdPartyJobsOutputTypeDef

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ThirdPartyJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutActionRevisionInputTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### actionRevision
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionRevisionUnionTypeDef'>
- **Required**: Yes


# PutActionRevisionOutputTypeDef

### newRevision
- **Type**: <class 'bool'>
- **Required**: Yes

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutApprovalResultInputTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### result
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ApprovalResultTypeDef'>
- **Required**: Yes

### token
- **Type**: <class 'str'>
- **Required**: Yes


# PutApprovalResultOutputTypeDef

### approvedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutJobFailureResultInputTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### failureDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.FailureDetailsTypeDef'>
- **Required**: Yes


# PutJobSuccessResultInputTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### currentRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.CurrentRevisionTypeDef]

### continuationToken
- **Type**: typing.Optional[str]

### executionDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ExecutionDetailsTypeDef]

### outputVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PutThirdPartyJobFailureResultInputTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### failureDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.FailureDetailsTypeDef'>
- **Required**: Yes


# PutThirdPartyJobSuccessResultInputTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### currentRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.CurrentRevisionTypeDef]

### continuationToken
- **Type**: typing.Optional[str]

### executionDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ExecutionDetailsTypeDef]


# PutWebhookInputTypeDef

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.WebhookDefinitionUnionTypeDef'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.TagTypeDef]]


# PutWebhookOutputTypeDef

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ListWebhookItemTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterWebhookWithThirdPartyInputTypeDef

### webhookName
- **Type**: typing.Optional[str]


# ResolvedPipelineVariableTypeDef

### name
- **Type**: typing.Optional[str]

### resolvedValue
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


# RetryConfigurationTypeDef

### retryMode
- **Type**: typing.Optional[typing.Literal['ALL_ACTIONS', 'FAILED_ACTIONS']]


# RetryStageExecutionInputTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### retryMode
- **Type**: typing.Literal['ALL_ACTIONS', 'FAILED_ACTIONS']
- **Required**: Yes


# RetryStageExecutionOutputTypeDef

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RetryStageMetadataTypeDef

### autoStageRetryAttempt
- **Type**: typing.Optional[int]

### manualStageRetryAttempt
- **Type**: typing.Optional[int]

### latestRetryTrigger
- **Type**: typing.Optional[typing.Literal['AutomatedStageRetry', 'ManualStageRetry']]


# RollbackStageInputTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### targetPipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# RollbackStageOutputTypeDef

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RuleDeclarationOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ruleTypeId
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.RuleTypeIdTypeDef'>
- **Required**: Yes

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]

### commands
- **Type**: typing.Optional[typing.List[str]]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.InputArtifactTypeDef]]

### roleArn
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### timeoutInMinutes
- **Type**: typing.Optional[int]


# RuleDeclarationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ruleTypeId
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.RuleTypeIdTypeDef'>
- **Required**: Yes

### configuration
- **Type**: typing.Optional[typing.Mapping[str, str]]

### commands
- **Type**: typing.Optional[typing.Sequence[str]]

### inputArtifacts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.InputArtifactTypeDef]]

### roleArn
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### timeoutInMinutes
- **Type**: typing.Optional[int]


# RuleExecutionDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuleExecutionFilterTypeDef

### pipelineExecutionId
- **Type**: typing.Optional[str]

### latestInPipelineExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.LatestInPipelineExecutionFilterTypeDef]


# RuleExecutionInputTypeDef

### ruleTypeId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.RuleTypeIdTypeDef]

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]

### resolvedConfiguration
- **Type**: typing.Optional[typing.Dict[str, str]]

### roleArn
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactDetailTypeDef]]


# RuleExecutionOutputTypeDef

### executionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.RuleExecutionResultTypeDef]


# RuleExecutionResultTypeDef

### externalExecutionId
- **Type**: typing.Optional[str]

### externalExecutionSummary
- **Type**: typing.Optional[str]

### externalExecutionUrl
- **Type**: typing.Optional[str]

### errorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ErrorDetailsTypeDef]


# RuleExecutionTypeDef

### ruleExecutionId
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Abandoned', 'Failed', 'InProgress', 'Succeeded']]

### summary
- **Type**: typing.Optional[str]

### lastStatusChange
- **Type**: typing.Optional[datetime.datetime]

### token
- **Type**: typing.Optional[str]

### lastUpdatedBy
- **Type**: typing.Optional[str]

### externalExecutionId
- **Type**: typing.Optional[str]

### externalExecutionUrl
- **Type**: typing.Optional[str]

### errorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ErrorDetailsTypeDef]


# RuleRevisionTypeDef

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionChangeId
- **Type**: <class 'str'>
- **Required**: Yes

### created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# RuleStateTypeDef

### ruleName
- **Type**: typing.Optional[str]

### currentRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.RuleRevisionTypeDef]

### latestExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.RuleExecutionTypeDef]

### entityUrl
- **Type**: typing.Optional[str]

### revisionUrl
- **Type**: typing.Optional[str]


# RuleTypeIdTypeDef

### category
- **Type**: typing.Literal['Rule']
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### owner
- **Type**: typing.Optional[typing.Literal['AWS']]

### version
- **Type**: typing.Optional[str]


# RuleTypeSettingsTypeDef

### thirdPartyConfigurationUrl
- **Type**: typing.Optional[str]

### entityUrlTemplate
- **Type**: typing.Optional[str]

### executionUrlTemplate
- **Type**: typing.Optional[str]

### revisionUrlTemplate
- **Type**: typing.Optional[str]


# RuleTypeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3ArtifactLocationTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### objectKey
- **Type**: <class 'str'>
- **Required**: Yes


# S3LocationTypeDef

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]


# SourceRevisionOverrideTypeDef

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### revisionType
- **Type**: typing.Literal['COMMIT_ID', 'IMAGE_DIGEST', 'S3_OBJECT_KEY', 'S3_OBJECT_VERSION_ID']
- **Required**: Yes

### revisionValue
- **Type**: <class 'str'>
- **Required**: Yes


# SourceRevisionTypeDef

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: typing.Optional[str]

### revisionSummary
- **Type**: typing.Optional[str]

### revisionUrl
- **Type**: typing.Optional[str]


# StageConditionStateTypeDef

### latestExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.StageConditionsExecutionTypeDef]

### conditionStates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ConditionStateTypeDef]]


# StageConditionsExecutionTypeDef

### status
- **Type**: typing.Optional[typing.Literal['Abandoned', 'Cancelled', 'Errored', 'Failed', 'InProgress', 'Overridden', 'Succeeded']]

### summary
- **Type**: typing.Optional[str]


# StageContextTypeDef

### name
- **Type**: typing.Optional[str]


# StageDeclarationOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ActionDeclarationOutputTypeDef]
- **Required**: Yes

### blockers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.BlockerDeclarationTypeDef]]

### onFailure
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.FailureConditionsOutputTypeDef]

### onSuccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.SuccessConditionsOutputTypeDef]

### beforeEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.BeforeEntryConditionsOutputTypeDef]


# StageDeclarationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.ActionDeclarationTypeDef]
- **Required**: Yes

### blockers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.BlockerDeclarationTypeDef]]

### onFailure
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.FailureConditionsTypeDef]

### onSuccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.SuccessConditionsTypeDef]

### beforeEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.BeforeEntryConditionsTypeDef]


# StageExecutionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StageStateTypeDef

### stageName
- **Type**: typing.Optional[str]

### inboundExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.StageExecutionTypeDef]

### inboundExecutions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.StageExecutionTypeDef]]

### inboundTransitionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.TransitionStateTypeDef]

### actionStates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ActionStateTypeDef]]

### latestExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.StageExecutionTypeDef]

### beforeEntryConditionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.StageConditionStateTypeDef]

### onSuccessConditionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.StageConditionStateTypeDef]

### onFailureConditionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.StageConditionStateTypeDef]

### retryStageMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.RetryStageMetadataTypeDef]


# StartPipelineExecutionInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineVariableTypeDef]]

### clientRequestToken
- **Type**: typing.Optional[str]

### sourceRevisions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.SourceRevisionOverrideTypeDef]]


# StartPipelineExecutionOutputTypeDef

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopExecutionTriggerTypeDef

### reason
- **Type**: typing.Optional[str]


# StopPipelineExecutionInputTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### abandon
- **Type**: typing.Optional[bool]

### reason
- **Type**: typing.Optional[str]


# StopPipelineExecutionOutputTypeDef

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SucceededInStageFilterTypeDef

### stageName
- **Type**: typing.Optional[str]


# SuccessConditionsOutputTypeDef

### conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ConditionOutputTypeDef]
- **Required**: Yes


# SuccessConditionsTypeDef

### conditions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.ConditionTypeDef]
- **Required**: Yes


# TagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ThirdPartyJobDataTypeDef

### actionTypeId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeIdTypeDef]

### actionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionConfigurationTypeDef]

### pipelineContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineContextTypeDef]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactTypeDef]]

### outputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactTypeDef]]

### artifactCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.AWSSessionCredentialsTypeDef]

### continuationToken
- **Type**: typing.Optional[str]

### encryptionKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.EncryptionKeyTypeDef]


# ThirdPartyJobDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ThirdPartyJobTypeDef

### clientId
- **Type**: typing.Optional[str]

### jobId
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TransitionStateTypeDef

### enabled
- **Type**: typing.Optional[bool]

### lastChangedBy
- **Type**: typing.Optional[str]

### lastChangedAt
- **Type**: typing.Optional[datetime.datetime]

### disabledReason
- **Type**: typing.Optional[str]


# UntagResourceInputTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateActionTypeInputTypeDef

### actionType
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeDeclarationUnionTypeDef'>
- **Required**: Yes


# UpdatePipelineInputTypeDef

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.PipelineDeclarationUnionTypeDef'>
- **Required**: Yes


# UpdatePipelineOutputTypeDef

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.PipelineDeclarationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WebhookAuthConfigurationTypeDef

### AllowedIPRange
- **Type**: typing.Optional[str]

### SecretToken
- **Type**: typing.Optional[str]


# WebhookDefinitionOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### targetPipeline
- **Type**: <class 'str'>
- **Required**: Yes

### targetAction
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.WebhookFilterRuleTypeDef]
- **Required**: Yes

### authentication
- **Type**: typing.Literal['GITHUB_HMAC', 'IP', 'UNAUTHENTICATED']
- **Required**: Yes

### authenticationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.WebhookAuthConfigurationTypeDef'>
- **Required**: Yes


# WebhookDefinitionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### targetPipeline
- **Type**: <class 'str'>
- **Required**: Yes

### targetAction
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.WebhookFilterRuleTypeDef]
- **Required**: Yes

### authentication
- **Type**: typing.Literal['GITHUB_HMAC', 'IP', 'UNAUTHENTICATED']
- **Required**: Yes

### authenticationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.WebhookAuthConfigurationTypeDef'>
- **Required**: Yes


# WebhookDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WebhookFilterRuleTypeDef

### jsonPath
- **Type**: <class 'str'>
- **Required**: Yes

### matchEquals
- **Type**: typing.Optional[str]


