# Codepipeline Classes

# AWSSessionCredentials

### accessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### secretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes


# AcknowledgeJobInput

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### nonce
- **Type**: <class 'str'>
- **Required**: Yes


# AcknowledgeJobOutput

### status
- **Type**: typing.Literal['Created', 'Dispatched', 'Failed', 'InProgress', 'Queued', 'Succeeded', 'TimedOut']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# AcknowledgeThirdPartyJobInput

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### nonce
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# AcknowledgeThirdPartyJobOutput

### status
- **Type**: typing.Literal['Created', 'Dispatched', 'Failed', 'InProgress', 'Queued', 'Succeeded', 'TimedOut']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# ActionConfiguration

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]


# ActionConfigurationProperty

### name
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: <class 'bool'>
- **Required**: Yes

### key
- **Type**: <class 'bool'>
- **Required**: Yes

### secret
- **Type**: <class 'bool'>
- **Required**: Yes

### queryable
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['Boolean', 'Number', 'String']]


# ActionContext

### name
- **Type**: typing.Optional[str]

### actionExecutionId
- **Type**: typing.Optional[str]


# ActionDeclaration

### name
- **Type**: <class 'str'>
- **Required**: Yes

### actionTypeId
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeId'>
- **Required**: Yes

### runOrder
- **Type**: typing.Optional[int]

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]

### commands
- **Type**: typing.Optional[typing.List[str]]

### outputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.OutputArtifact]]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.InputArtifact]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.EnvironmentVariable]]


# ActionDeclarationOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### actionTypeId
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeId'>
- **Required**: Yes

### runOrder
- **Type**: typing.Optional[int]

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]

### commands
- **Type**: typing.Optional[typing.List[str]]

### outputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.OutputArtifactOutput]]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.InputArtifact]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.EnvironmentVariable]]


# ActionExecution

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ErrorDetails]

### logStreamARN
- **Type**: typing.Optional[str]


# ActionExecutionDetail

### pipelineExecutionId
- **Type**: typing.Optional[str]

### actionExecutionId
- **Type**: typing.Optional[str]

### pipelineVersion
- **Type**: typing.Optional[int]

### stageName
- **Type**: typing.Optional[str]

### actionName
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Abandoned', 'Failed', 'InProgress', 'Succeeded']]

### input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionExecutionInput]

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionExecutionOutput]


# ActionExecutionFilter

### pipelineExecutionId
- **Type**: typing.Optional[str]

### latestInPipelineExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.LatestInPipelineExecutionFilter]


# ActionExecutionInput

### actionTypeId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeId]

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]

### resolvedConfiguration
- **Type**: typing.Optional[typing.Dict[str, str]]

### roleArn
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactDetail]]

### namespace
- **Type**: typing.Optional[str]


# ActionExecutionOutput

### outputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactDetail]]

### executionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionExecutionResult]

### outputVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# ActionExecutionResult

### externalExecutionId
- **Type**: typing.Optional[str]

### externalExecutionSummary
- **Type**: typing.Optional[str]

### externalExecutionUrl
- **Type**: typing.Optional[str]

### errorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ErrorDetails]

### logStreamARN
- **Type**: typing.Optional[str]


# ActionRevision

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionChangeId
- **Type**: <class 'str'>
- **Required**: Yes

### created
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# ActionRevisionOutput

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionChangeId
- **Type**: <class 'str'>
- **Required**: Yes

### created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ActionState

### actionName
- **Type**: typing.Optional[str]

### currentRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionRevisionOutput]

### latestExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionExecution]

### entityUrl
- **Type**: typing.Optional[str]

### revisionUrl
- **Type**: typing.Optional[str]


# ActionType

### id
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeId'>
- **Required**: Yes

### inputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactDetails'>
- **Required**: Yes

### outputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactDetails'>
- **Required**: Yes

### settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeSettings]

### actionConfigurationProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionConfigurationProperty]]


# ActionTypeArtifactDetails

### minimumCount
- **Type**: <class 'int'>
- **Required**: Yes

### maximumCount
- **Type**: <class 'int'>
- **Required**: Yes


# ActionTypeDeclaration

### executor
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeExecutor'>
- **Required**: Yes

### id
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeIdentifier'>
- **Required**: Yes

### inputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeArtifactDetails'>
- **Required**: Yes

### outputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeArtifactDetails'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypePermissions]

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeProperty]]

### urls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeUrls]


# ActionTypeDeclarationOutput

### executor
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeExecutorOutput'>
- **Required**: Yes

### id
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeIdentifier'>
- **Required**: Yes

### inputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeArtifactDetails'>
- **Required**: Yes

### outputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeArtifactDetails'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypePermissionsOutput]

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeProperty]]

### urls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeUrls]


# ActionTypeExecutor

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ExecutorConfiguration'>
- **Required**: Yes

### type
- **Type**: typing.Literal['JobWorker', 'Lambda']
- **Required**: Yes

### policyStatementsTemplate
- **Type**: typing.Optional[str]

### jobTimeout
- **Type**: typing.Optional[int]


# ActionTypeExecutorOutput

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ExecutorConfigurationOutput'>
- **Required**: Yes

### type
- **Type**: typing.Literal['JobWorker', 'Lambda']
- **Required**: Yes

### policyStatementsTemplate
- **Type**: typing.Optional[str]

### jobTimeout
- **Type**: typing.Optional[int]


# ActionTypeId

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


# ActionTypeIdentifier

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


# ActionTypePermissions

### allowedAccounts
- **Type**: typing.List[str]
- **Required**: Yes


# ActionTypePermissionsOutput

### allowedAccounts
- **Type**: typing.List[str]
- **Required**: Yes


# ActionTypeProperty

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


# ActionTypeSettings

### thirdPartyConfigurationUrl
- **Type**: typing.Optional[str]

### entityUrlTemplate
- **Type**: typing.Optional[str]

### executionUrlTemplate
- **Type**: typing.Optional[str]

### revisionUrlTemplate
- **Type**: typing.Optional[str]


# ActionTypeUrls

### configurationUrl
- **Type**: typing.Optional[str]

### entityUrlTemplate
- **Type**: typing.Optional[str]

### executionUrlTemplate
- **Type**: typing.Optional[str]

### revisionUrlTemplate
- **Type**: typing.Optional[str]


# ApprovalResult

### summary
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Approved', 'Rejected']
- **Required**: Yes


# Artifact

### name
- **Type**: typing.Optional[str]

### revision
- **Type**: typing.Optional[str]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactLocation]


# ArtifactDetail

### name
- **Type**: typing.Optional[str]

### s3location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.S3Location]


# ArtifactDetails

### minimumCount
- **Type**: <class 'int'>
- **Required**: Yes

### maximumCount
- **Type**: <class 'int'>
- **Required**: Yes


# ArtifactLocation

### type
- **Type**: typing.Optional[typing.Literal['S3']]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.S3ArtifactLocation]


# ArtifactRevision

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


# ArtifactStore

### type
- **Type**: typing.Literal['S3']
- **Required**: Yes

### location
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.EncryptionKey]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BeforeEntryConditions

### conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Condition]
- **Required**: Yes


# BeforeEntryConditionsOutput

### conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ConditionOutput]
- **Required**: Yes


# BlockerDeclaration

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Schedule']
- **Required**: Yes


# Condition

### result
- **Type**: typing.Optional[typing.Literal['FAIL', 'RETRY', 'ROLLBACK', 'SKIP']]

### rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleDeclaration]]


# ConditionExecution

### status
- **Type**: typing.Optional[typing.Literal['Abandoned', 'Cancelled', 'Errored', 'Failed', 'InProgress', 'Overridden', 'Succeeded']]

### summary
- **Type**: typing.Optional[str]

### lastStatusChange
- **Type**: typing.Optional[datetime.datetime]


# ConditionOutput

### result
- **Type**: typing.Optional[typing.Literal['FAIL', 'RETRY', 'ROLLBACK', 'SKIP']]

### rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleDeclarationOutput]]


# ConditionState

### latestExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ConditionExecution]

### ruleStates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleState]]


# CreateCustomActionTypeInput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactDetails'>
- **Required**: Yes

### outputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactDetails'>
- **Required**: Yes

### settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeSettings]

### configurationProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionConfigurationProperty]]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Tag]]


# CreateCustomActionTypeOutput

### actionType
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionType'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePipelineInput

### pipeline
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineDeclaration, aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineDeclarationOutput]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Tag]]


# CreatePipelineOutput

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineDeclarationOutput'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# CurrentRevision

### revision
- **Type**: <class 'str'>
- **Required**: Yes

### changeIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### created
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### revisionSummary
- **Type**: typing.Optional[str]


# DeleteCustomActionTypeInput

### category
- **Type**: typing.Literal['Approval', 'Build', 'Compute', 'Deploy', 'Invoke', 'Source', 'Test']
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePipelineInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebhookInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterWebhookWithThirdPartyInput

### webhookName
- **Type**: typing.Optional[str]


# DisableStageTransitionInput

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


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# EnableStageTransitionInput

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### transitionType
- **Type**: typing.Literal['Inbound', 'Outbound']
- **Required**: Yes


# EncryptionKey

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['KMS']
- **Required**: Yes


# EnvironmentVariable

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ErrorDetails

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# ExecutionDetails

### summary
- **Type**: typing.Optional[str]

### externalExecutionId
- **Type**: typing.Optional[str]

### percentComplete
- **Type**: typing.Optional[int]


# ExecutionTrigger

### triggerType
- **Type**: typing.Optional[typing.Literal['AutomatedRollback', 'CloudWatchEvent', 'CreatePipeline', 'ManualRollback', 'PollForSourceChanges', 'PutActionRevision', 'StartPipelineExecution', 'Webhook', 'WebhookV2']]

### triggerDetail
- **Type**: typing.Optional[str]


# ExecutorConfiguration

### lambdaExecutorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.LambdaExecutorConfiguration]

### jobWorkerExecutorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.JobWorkerExecutorConfiguration]


# ExecutorConfigurationOutput

### lambdaExecutorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.LambdaExecutorConfiguration]

### jobWorkerExecutorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.JobWorkerExecutorConfigurationOutput]


# FailureConditions

### result
- **Type**: typing.Optional[typing.Literal['FAIL', 'RETRY', 'ROLLBACK', 'SKIP']]

### retryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RetryConfiguration]

### conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Condition]]


# FailureConditionsOutput

### result
- **Type**: typing.Optional[typing.Literal['FAIL', 'RETRY', 'ROLLBACK', 'SKIP']]

### retryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RetryConfiguration]

### conditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ConditionOutput]]


# FailureDetails

### type
- **Type**: typing.Literal['ConfigurationError', 'JobFailed', 'PermissionError', 'RevisionOutOfSync', 'RevisionUnavailable', 'SystemUnavailable']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### externalExecutionId
- **Type**: typing.Optional[str]


# GetActionTypeInput

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


# GetActionTypeOutput

### actionType
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeDeclarationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# GetJobDetailsInput

### jobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetJobDetailsOutput

### jobDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.JobDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# GetPipelineExecutionInput

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPipelineExecutionOutput

### pipelineExecution
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineExecution'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# GetPipelineInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: typing.Optional[int]


# GetPipelineOutput

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineDeclarationOutput'>
- **Required**: Yes

### metadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineMetadata'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# GetPipelineStateInput

### name
- **Type**: <class 'str'>
- **Required**: Yes


# GetPipelineStateOutput

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### pipelineVersion
- **Type**: <class 'int'>
- **Required**: Yes

### stageStates
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.StageState]
- **Required**: Yes

### created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# GetThirdPartyJobDetailsInput

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetThirdPartyJobDetailsOutput

### jobDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ThirdPartyJobDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# GitBranchFilterCriteria

### includes
- **Type**: typing.Optional[typing.List[str]]

### excludes
- **Type**: typing.Optional[typing.List[str]]


# GitBranchFilterCriteriaOutput

### includes
- **Type**: typing.Optional[typing.List[str]]

### excludes
- **Type**: typing.Optional[typing.List[str]]


# GitConfiguration

### sourceActionName
- **Type**: <class 'str'>
- **Required**: Yes

### push
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitPushFilter]]

### pullRequest
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitPullRequestFilter]]


# GitConfigurationOutput

### sourceActionName
- **Type**: <class 'str'>
- **Required**: Yes

### push
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitPushFilterOutput]]

### pullRequest
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitPullRequestFilterOutput]]


# GitFilePathFilterCriteria

### includes
- **Type**: typing.Optional[typing.List[str]]

### excludes
- **Type**: typing.Optional[typing.List[str]]


# GitFilePathFilterCriteriaOutput

### includes
- **Type**: typing.Optional[typing.List[str]]

### excludes
- **Type**: typing.Optional[typing.List[str]]


# GitPullRequestFilter

### events
- **Type**: typing.Optional[typing.List[typing.Literal['CLOSED', 'OPEN', 'UPDATED']]]

### branches
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitBranchFilterCriteria]

### filePaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitFilePathFilterCriteria]


# GitPullRequestFilterOutput

### events
- **Type**: typing.Optional[typing.List[typing.Literal['CLOSED', 'OPEN', 'UPDATED']]]

### branches
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitBranchFilterCriteriaOutput]

### filePaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitFilePathFilterCriteriaOutput]


# GitPushFilter

### tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitTagFilterCriteria]

### branches
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitBranchFilterCriteria]

### filePaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitFilePathFilterCriteria]


# GitPushFilterOutput

### tags
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitTagFilterCriteriaOutput]

### branches
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitBranchFilterCriteriaOutput]

### filePaths
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitFilePathFilterCriteriaOutput]


# GitTagFilterCriteria

### includes
- **Type**: typing.Optional[typing.List[str]]

### excludes
- **Type**: typing.Optional[typing.List[str]]


# GitTagFilterCriteriaOutput

### includes
- **Type**: typing.Optional[typing.List[str]]

### excludes
- **Type**: typing.Optional[typing.List[str]]


# InputArtifact

### name
- **Type**: <class 'str'>
- **Required**: Yes


# Job

### id
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.JobData]

### nonce
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]


# JobData

### actionTypeId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeId]

### actionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionConfiguration]

### pipelineContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineContext]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Artifact]]

### outputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Artifact]]

### artifactCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.AWSSessionCredentials]

### continuationToken
- **Type**: typing.Optional[str]

### encryptionKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.EncryptionKey]


# JobDetails

### id
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.JobData]

### accountId
- **Type**: typing.Optional[str]


# JobWorkerExecutorConfiguration

### pollingAccounts
- **Type**: typing.Optional[typing.List[str]]

### pollingServicePrincipals
- **Type**: typing.Optional[typing.List[str]]


# JobWorkerExecutorConfigurationOutput

### pollingAccounts
- **Type**: typing.Optional[typing.List[str]]

### pollingServicePrincipals
- **Type**: typing.Optional[typing.List[str]]


# LambdaExecutorConfiguration

### lambdaFunctionArn
- **Type**: <class 'str'>
- **Required**: Yes


# LatestInPipelineExecutionFilter

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### startTimeRange
- **Type**: typing.Literal['All', 'Latest']
- **Required**: Yes


# ListActionExecutionsInput

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionExecutionFilter]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListActionExecutionsInputPaginate

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionExecutionFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PaginatorConfig]


# ListActionExecutionsOutput

### actionExecutionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionExecutionDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListActionTypesInput

### actionOwnerFilter
- **Type**: typing.Optional[typing.Literal['AWS', 'Custom', 'ThirdParty']]

### nextToken
- **Type**: typing.Optional[str]

### regionFilter
- **Type**: typing.Optional[str]


# ListActionTypesInputPaginate

### actionOwnerFilter
- **Type**: typing.Optional[typing.Literal['AWS', 'Custom', 'ThirdParty']]

### regionFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PaginatorConfig]


# ListActionTypesOutput

### actionTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPipelineExecutionsInput

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineExecutionFilter]

### nextToken
- **Type**: typing.Optional[str]


# ListPipelineExecutionsInputPaginate

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineExecutionFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PaginatorConfig]


# ListPipelineExecutionsOutput

### pipelineExecutionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineExecutionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPipelinesInput

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPipelinesInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PaginatorConfig]


# ListPipelinesOutput

### pipelines
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRuleExecutionsInput

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleExecutionFilter]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRuleExecutionsInputPaginate

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleExecutionFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PaginatorConfig]


# ListRuleExecutionsOutput

### ruleExecutionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleExecutionDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRuleTypesInput

### ruleOwnerFilter
- **Type**: typing.Optional[typing.Literal['AWS']]

### regionFilter
- **Type**: typing.Optional[str]


# ListRuleTypesOutput

### ruleTypes
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListTagsForResourceInputPaginate

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PaginatorConfig]


# ListTagsForResourceOutput

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWebhookItem

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.WebhookDefinitionOutput'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Tag]]


# ListWebhooksInput

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWebhooksInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PaginatorConfig]


# ListWebhooksOutput

### webhooks
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ListWebhookItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# OutputArtifact

### name
- **Type**: <class 'str'>
- **Required**: Yes

### files
- **Type**: typing.Optional[typing.List[str]]


# OutputArtifactOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### files
- **Type**: typing.Optional[typing.List[str]]


# OverrideStageConditionInput

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


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PipelineContext

### pipelineName
- **Type**: typing.Optional[str]

### stage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.StageContext]

### action
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionContext]

### pipelineArn
- **Type**: typing.Optional[str]

### pipelineExecutionId
- **Type**: typing.Optional[str]


# PipelineDeclaration

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### stages
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.StageDeclaration]
- **Required**: Yes

### artifactStore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactStore]

### artifactStores
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactStore]]

### version
- **Type**: typing.Optional[int]

### executionMode
- **Type**: typing.Optional[typing.Literal['PARALLEL', 'QUEUED', 'SUPERSEDED']]

### pipelineType
- **Type**: typing.Optional[typing.Literal['V1', 'V2']]

### variables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineVariableDeclaration]]

### triggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineTriggerDeclaration]]


# PipelineDeclarationOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### stages
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.StageDeclarationOutput]
- **Required**: Yes

### artifactStore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactStore]

### artifactStores
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactStore]]

### version
- **Type**: typing.Optional[int]

### executionMode
- **Type**: typing.Optional[typing.Literal['PARALLEL', 'QUEUED', 'SUPERSEDED']]

### pipelineType
- **Type**: typing.Optional[typing.Literal['V1', 'V2']]

### variables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineVariableDeclaration]]

### triggers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineTriggerDeclarationOutput]]


# PipelineExecution

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactRevision]]

### variables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResolvedPipelineVariable]]

### trigger
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ExecutionTrigger]

### executionMode
- **Type**: typing.Optional[typing.Literal['PARALLEL', 'QUEUED', 'SUPERSEDED']]

### executionType
- **Type**: typing.Optional[typing.Literal['ROLLBACK', 'STANDARD']]

### rollbackMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineRollbackMetadata]


# PipelineExecutionFilter

### succeededInStage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.SucceededInStageFilter]


# PipelineExecutionSummary

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.SourceRevision]]

### trigger
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ExecutionTrigger]

### stopTrigger
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.StopExecutionTrigger]

### executionMode
- **Type**: typing.Optional[typing.Literal['PARALLEL', 'QUEUED', 'SUPERSEDED']]

### executionType
- **Type**: typing.Optional[typing.Literal['ROLLBACK', 'STANDARD']]

### rollbackMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineRollbackMetadata]


# PipelineMetadata

### pipelineArn
- **Type**: typing.Optional[str]

### created
- **Type**: typing.Optional[datetime.datetime]

### updated
- **Type**: typing.Optional[datetime.datetime]

### pollingDisabledAt
- **Type**: typing.Optional[datetime.datetime]


# PipelineRollbackMetadata

### rollbackTargetPipelineExecutionId
- **Type**: typing.Optional[str]


# PipelineSummary

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


# PipelineTriggerDeclaration

### providerType
- **Type**: typing.Literal['CodeStarSourceConnection']
- **Required**: Yes

### gitConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitConfiguration'>
- **Required**: Yes


# PipelineTriggerDeclarationOutput

### providerType
- **Type**: typing.Literal['CodeStarSourceConnection']
- **Required**: Yes

### gitConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.GitConfigurationOutput'>
- **Required**: Yes


# PipelineVariable

### name
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# PipelineVariableDeclaration

### name
- **Type**: <class 'str'>
- **Required**: Yes

### defaultValue
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# PollForJobsInput

### actionTypeId
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeId'>
- **Required**: Yes

### maxBatchSize
- **Type**: typing.Optional[int]

### queryParam
- **Type**: typing.Optional[typing.Dict[str, str]]


# PollForJobsOutput

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Job]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# PollForThirdPartyJobsInput

### actionTypeId
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeId'>
- **Required**: Yes

### maxBatchSize
- **Type**: typing.Optional[int]


# PollForThirdPartyJobsOutput

### jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ThirdPartyJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# PutActionRevisionInput

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionRevision, aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionRevisionOutput]
- **Required**: Yes


# PutActionRevisionOutput

### newRevision
- **Type**: <class 'bool'>
- **Required**: Yes

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# PutApprovalResultInput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ApprovalResult'>
- **Required**: Yes

### token
- **Type**: <class 'str'>
- **Required**: Yes


# PutApprovalResultOutput

### approvedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# PutJobFailureResultInput

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### failureDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.FailureDetails'>
- **Required**: Yes


# PutJobSuccessResultInput

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### currentRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.CurrentRevision]

### continuationToken
- **Type**: typing.Optional[str]

### executionDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ExecutionDetails]

### outputVariables
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutThirdPartyJobFailureResultInput

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### failureDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.FailureDetails'>
- **Required**: Yes


# PutThirdPartyJobSuccessResultInput

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### currentRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.CurrentRevision]

### continuationToken
- **Type**: typing.Optional[str]

### executionDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ExecutionDetails]


# PutWebhookInput

### webhook
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.WebhookDefinition, aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.WebhookDefinitionOutput]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Tag]]


# PutWebhookOutput

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ListWebhookItem'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterWebhookWithThirdPartyInput

### webhookName
- **Type**: typing.Optional[str]


# ResolvedPipelineVariable

### name
- **Type**: typing.Optional[str]

### resolvedValue
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


# RetryConfiguration

### retryMode
- **Type**: typing.Optional[typing.Literal['ALL_ACTIONS', 'FAILED_ACTIONS']]


# RetryStageExecutionInput

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


# RetryStageExecutionOutput

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# RetryStageMetadata

### autoStageRetryAttempt
- **Type**: typing.Optional[int]

### manualStageRetryAttempt
- **Type**: typing.Optional[int]

### latestRetryTrigger
- **Type**: typing.Optional[typing.Literal['AutomatedStageRetry', 'ManualStageRetry']]


# RollbackStageInput

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### stageName
- **Type**: <class 'str'>
- **Required**: Yes

### targetPipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes


# RollbackStageOutput

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# RuleConfigurationProperty

### name
- **Type**: <class 'str'>
- **Required**: Yes

### required
- **Type**: <class 'bool'>
- **Required**: Yes

### key
- **Type**: <class 'bool'>
- **Required**: Yes

### secret
- **Type**: <class 'bool'>
- **Required**: Yes

### queryable
- **Type**: typing.Optional[bool]

### description
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['Boolean', 'Number', 'String']]


# RuleDeclaration

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ruleTypeId
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleTypeId'>
- **Required**: Yes

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]

### commands
- **Type**: typing.Optional[typing.List[str]]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.InputArtifact]]

### roleArn
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### timeoutInMinutes
- **Type**: typing.Optional[int]


# RuleDeclarationOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### ruleTypeId
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleTypeId'>
- **Required**: Yes

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]

### commands
- **Type**: typing.Optional[typing.List[str]]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.InputArtifact]]

### roleArn
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### timeoutInMinutes
- **Type**: typing.Optional[int]


# RuleExecution

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ErrorDetails]


# RuleExecutionDetail

### pipelineExecutionId
- **Type**: typing.Optional[str]

### ruleExecutionId
- **Type**: typing.Optional[str]

### pipelineVersion
- **Type**: typing.Optional[int]

### stageName
- **Type**: typing.Optional[str]

### ruleName
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### lastUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### updatedBy
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Abandoned', 'Failed', 'InProgress', 'Succeeded']]

### input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleExecutionInput]

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleExecutionOutput]


# RuleExecutionFilter

### pipelineExecutionId
- **Type**: typing.Optional[str]

### latestInPipelineExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.LatestInPipelineExecutionFilter]


# RuleExecutionInput

### ruleTypeId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleTypeId]

### configuration
- **Type**: typing.Optional[typing.Dict[str, str]]

### resolvedConfiguration
- **Type**: typing.Optional[typing.Dict[str, str]]

### roleArn
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactDetail]]


# RuleExecutionOutput

### executionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleExecutionResult]


# RuleExecutionResult

### externalExecutionId
- **Type**: typing.Optional[str]

### externalExecutionSummary
- **Type**: typing.Optional[str]

### externalExecutionUrl
- **Type**: typing.Optional[str]

### errorDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ErrorDetails]


# RuleRevision

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### revisionChangeId
- **Type**: <class 'str'>
- **Required**: Yes

### created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# RuleState

### ruleName
- **Type**: typing.Optional[str]

### currentRevision
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleRevision]

### latestExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleExecution]

### entityUrl
- **Type**: typing.Optional[str]

### revisionUrl
- **Type**: typing.Optional[str]


# RuleType

### id
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleTypeId'>
- **Required**: Yes

### inputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ArtifactDetails'>
- **Required**: Yes

### settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleTypeSettings]

### ruleConfigurationProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RuleConfigurationProperty]]


# RuleTypeId

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


# RuleTypeSettings

### thirdPartyConfigurationUrl
- **Type**: typing.Optional[str]

### entityUrlTemplate
- **Type**: typing.Optional[str]

### executionUrlTemplate
- **Type**: typing.Optional[str]

### revisionUrlTemplate
- **Type**: typing.Optional[str]


# S3ArtifactLocation

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes

### objectKey
- **Type**: <class 'str'>
- **Required**: Yes


# S3Location

### bucket
- **Type**: typing.Optional[str]

### key
- **Type**: typing.Optional[str]


# SourceRevision

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: typing.Optional[str]

### revisionSummary
- **Type**: typing.Optional[str]

### revisionUrl
- **Type**: typing.Optional[str]


# SourceRevisionOverride

### actionName
- **Type**: <class 'str'>
- **Required**: Yes

### revisionType
- **Type**: typing.Literal['COMMIT_ID', 'IMAGE_DIGEST', 'S3_OBJECT_KEY', 'S3_OBJECT_VERSION_ID']
- **Required**: Yes

### revisionValue
- **Type**: <class 'str'>
- **Required**: Yes


# StageConditionState

### latestExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.StageConditionsExecution]

### conditionStates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ConditionState]]


# StageConditionsExecution

### status
- **Type**: typing.Optional[typing.Literal['Abandoned', 'Cancelled', 'Errored', 'Failed', 'InProgress', 'Overridden', 'Succeeded']]

### summary
- **Type**: typing.Optional[str]


# StageContext

### name
- **Type**: typing.Optional[str]


# StageDeclaration

### name
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionDeclaration]
- **Required**: Yes

### blockers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.BlockerDeclaration]]

### onFailure
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.FailureConditions]

### onSuccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.SuccessConditions]

### beforeEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.BeforeEntryConditions]


# StageDeclarationOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### actions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionDeclarationOutput]
- **Required**: Yes

### blockers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.BlockerDeclaration]]

### onFailure
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.FailureConditionsOutput]

### onSuccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.SuccessConditionsOutput]

### beforeEntry
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.BeforeEntryConditionsOutput]


# StageExecution

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Cancelled', 'Failed', 'InProgress', 'Skipped', 'Stopped', 'Stopping', 'Succeeded']
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['ROLLBACK', 'STANDARD']]


# StageState

### stageName
- **Type**: typing.Optional[str]

### inboundExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.StageExecution]

### inboundExecutions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.StageExecution]]

### inboundTransitionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.TransitionState]

### actionStates
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionState]]

### latestExecution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.StageExecution]

### beforeEntryConditionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.StageConditionState]

### onSuccessConditionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.StageConditionState]

### onFailureConditionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.StageConditionState]

### retryStageMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.RetryStageMetadata]


# StartPipelineExecutionInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### variables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineVariable]]

### clientRequestToken
- **Type**: typing.Optional[str]

### sourceRevisions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.SourceRevisionOverride]]


# StartPipelineExecutionOutput

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# StopExecutionTrigger

### reason
- **Type**: typing.Optional[str]


# StopPipelineExecutionInput

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


# StopPipelineExecutionOutput

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# SucceededInStageFilter

### stageName
- **Type**: typing.Optional[str]


# SuccessConditions

### conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Condition]
- **Required**: Yes


# SuccessConditionsOutput

### conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ConditionOutput]
- **Required**: Yes


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Tag]
- **Required**: Yes


# ThirdPartyJob

### clientId
- **Type**: typing.Optional[str]

### jobId
- **Type**: typing.Optional[str]


# ThirdPartyJobData

### actionTypeId
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeId]

### actionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionConfiguration]

### pipelineContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineContext]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Artifact]]

### outputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.Artifact]]

### artifactCredentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.AWSSessionCredentials]

### continuationToken
- **Type**: typing.Optional[str]

### encryptionKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.EncryptionKey]


# ThirdPartyJobDetails

### id
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ThirdPartyJobData]

### nonce
- **Type**: typing.Optional[str]


# TransitionState

### enabled
- **Type**: typing.Optional[bool]

### lastChangedBy
- **Type**: typing.Optional[str]

### lastChangedAt
- **Type**: typing.Optional[datetime.datetime]

### disabledReason
- **Type**: typing.Optional[str]


# UntagResourceInput

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateActionTypeInput

### actionType
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeDeclaration, aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ActionTypeDeclarationOutput]
- **Required**: Yes


# UpdatePipelineInput

### pipeline
- **Type**: typing.Union[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineDeclaration, aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineDeclarationOutput]
- **Required**: Yes


# UpdatePipelineOutput

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.PipelineDeclarationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.ResponseMetadata'>
- **Required**: Yes


# WebhookAuthConfiguration

### AllowedIPRange
- **Type**: typing.Optional[str]

### SecretToken
- **Type**: typing.Optional[str]


# WebhookDefinition

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.WebhookFilterRule]
- **Required**: Yes

### authentication
- **Type**: typing.Literal['GITHUB_HMAC', 'IP', 'UNAUTHENTICATED']
- **Required**: Yes

### authenticationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.WebhookAuthConfiguration'>
- **Required**: Yes


# WebhookDefinitionOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.WebhookFilterRule]
- **Required**: Yes

### authentication
- **Type**: typing.Literal['GITHUB_HMAC', 'IP', 'UNAUTHENTICATED']
- **Required**: Yes

### authenticationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline.codepipeline_classes.WebhookAuthConfiguration'>
- **Required**: Yes


# WebhookFilterRule

### jsonPath
- **Type**: <class 'str'>
- **Required**: Yes

### matchEquals
- **Type**: typing.Optional[str]


