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


# AcknowledgeJobInputRequestTypeDef

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


# AcknowledgeThirdPartyJobInputRequestTypeDef

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

### outputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.OutputArtifactTypeDef]]

### inputArtifacts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.InputArtifactTypeDef]]

### roleArn
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### timeoutInMinutes
- **Type**: typing.Optional[int]


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

### outputArtifacts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.OutputArtifactTypeDef]]

### inputArtifacts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.InputArtifactTypeDef]]

### roleArn
- **Type**: typing.Optional[str]

### region
- **Type**: typing.Optional[str]

### namespace
- **Type**: typing.Optional[str]

### timeoutInMinutes
- **Type**: typing.Optional[int]


# ActionExecutionDetailTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionExecutionInputTypeDef]

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionExecutionOutputTypeDef]


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
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


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

### executor
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeExecutorOutputTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeIdentifierTypeDef'>
- **Required**: Yes

### inputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeArtifactDetailsTypeDef'>
- **Required**: Yes

### outputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeArtifactDetailsTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypePermissionsOutputTypeDef]

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypePropertyTypeDef]]

### urls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeUrlsTypeDef]


# ActionTypeDeclarationTypeDef

### executor
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeExecutorTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeIdentifierTypeDef'>
- **Required**: Yes

### inputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeArtifactDetailsTypeDef'>
- **Required**: Yes

### outputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeArtifactDetailsTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypePermissionsTypeDef]

### properties
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypePropertyTypeDef]]

### urls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeUrlsTypeDef]


# ActionTypeExecutorOutputTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ExecutorConfigurationOutputTypeDef'>
- **Required**: Yes

### type
- **Type**: typing.Literal['JobWorker', 'Lambda']
- **Required**: Yes

### policyStatementsTemplate
- **Type**: typing.Optional[str]

### jobTimeout
- **Type**: typing.Optional[int]


# ActionTypeExecutorTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ExecutorConfigurationTypeDef'>
- **Required**: Yes

### type
- **Type**: typing.Literal['JobWorker', 'Lambda']
- **Required**: Yes

### policyStatementsTemplate
- **Type**: typing.Optional[str]

### jobTimeout
- **Type**: typing.Optional[int]


# ActionTypeIdTypeDef

### category
- **Type**: typing.Literal['Approval', 'Build', 'Deploy', 'Invoke', 'Source', 'Test']
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
- **Type**: typing.Literal['Approval', 'Build', 'Deploy', 'Invoke', 'Source', 'Test']
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

### id
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeIdTypeDef'>
- **Required**: Yes

### inputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactDetailsTypeDef'>
- **Required**: Yes

### outputArtifactDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ArtifactDetailsTypeDef'>
- **Required**: Yes

### settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeSettingsTypeDef]

### actionConfigurationProperties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ActionConfigurationPropertyTypeDef]]


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

### type
- **Type**: typing.Optional[typing.Literal['S3']]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.S3ArtifactLocationTypeDef]


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

### type
- **Type**: typing.Literal['S3']
- **Required**: Yes

### location
- **Type**: <class 'str'>
- **Required**: Yes

### encryptionKey
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.EncryptionKeyTypeDef]


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

# BlockerDeclarationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Schedule']
- **Required**: Yes


# CreateCustomActionTypeInputRequestTypeDef

### category
- **Type**: typing.Literal['Approval', 'Build', 'Deploy', 'Invoke', 'Source', 'Test']
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


# CreatePipelineInputRequestTypeDef

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.PipelineDeclarationTypeDef'>
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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### revisionSummary
- **Type**: typing.Optional[str]


# DeleteCustomActionTypeInputRequestTypeDef

### category
- **Type**: typing.Literal['Approval', 'Build', 'Deploy', 'Invoke', 'Source', 'Test']
- **Required**: Yes

### provider
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePipelineInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebhookInputRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterWebhookWithThirdPartyInputRequestTypeDef

### webhookName
- **Type**: typing.Optional[str]


# DisableStageTransitionInputRequestTypeDef

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


# EnableStageTransitionInputRequestTypeDef

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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['KMS']
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


# FailureConditionsTypeDef

### result
- **Type**: typing.Optional[typing.Literal['ROLLBACK']]


# FailureDetailsTypeDef

### type
- **Type**: typing.Literal['ConfigurationError', 'JobFailed', 'PermissionError', 'RevisionOutOfSync', 'RevisionUnavailable', 'SystemUnavailable']
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes

### externalExecutionId
- **Type**: typing.Optional[str]


# GetActionTypeInputRequestTypeDef

### category
- **Type**: typing.Literal['Approval', 'Build', 'Deploy', 'Invoke', 'Source', 'Test']
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


# GetJobDetailsInputRequestTypeDef

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


# GetPipelineExecutionInputRequestTypeDef

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


# GetPipelineInputRequestTypeDef

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


# GetPipelineStateInputRequestTypeDef

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


# GetThirdPartyJobDetailsInputRequestTypeDef

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

### id
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.JobDataTypeDef]

### accountId
- **Type**: typing.Optional[str]


# JobTypeDef

### id
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.JobDataTypeDef]

### nonce
- **Type**: typing.Optional[str]

### accountId
- **Type**: typing.Optional[str]


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


# ListActionExecutionsInputListActionExecutionsPaginateTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionExecutionFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PaginatorConfigTypeDef]


# ListActionExecutionsInputRequestTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ActionExecutionFilterTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListActionExecutionsOutputTypeDef

### actionExecutionDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.ActionExecutionDetailTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListActionTypesInputListActionTypesPaginateTypeDef

### actionOwnerFilter
- **Type**: typing.Optional[typing.Literal['AWS', 'Custom', 'ThirdParty']]

### regionFilter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PaginatorConfigTypeDef]


# ListActionTypesInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPipelineExecutionsInputListPipelineExecutionsPaginateTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineExecutionFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PaginatorConfigTypeDef]


# ListPipelineExecutionsInputRequestTypeDef

### pipelineName
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineExecutionFilterTypeDef]

### nextToken
- **Type**: typing.Optional[str]


# ListPipelineExecutionsOutputTypeDef

### pipelineExecutionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineExecutionSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPipelinesInputListPipelinesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PaginatorConfigTypeDef]


# ListPipelinesInputRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPipelinesOutputTypeDef

### pipelines
- **Type**: typing.List[aws_resource_validator.pydantic_models.codepipeline_classes.PipelineSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputListTagsForResourcePaginateTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PaginatorConfigTypeDef]


# ListTagsForResourceInputRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# ListWebhooksInputListWebhooksPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.PaginatorConfigTypeDef]


# ListWebhooksInputRequestTypeDef

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


# OutputArtifactTypeDef

### name
- **Type**: <class 'str'>
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


# PollForJobsInputRequestTypeDef

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


# PollForThirdPartyJobsInputRequestTypeDef

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


# PutActionRevisionInputRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionRevisionTypeDef'>
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


# PutApprovalResultInputRequestTypeDef

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


# PutJobFailureResultInputRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### failureDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.FailureDetailsTypeDef'>
- **Required**: Yes


# PutJobSuccessResultInputRequestTypeDef

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


# PutThirdPartyJobFailureResultInputRequestTypeDef

### jobId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: <class 'str'>
- **Required**: Yes

### failureDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.FailureDetailsTypeDef'>
- **Required**: Yes


# PutThirdPartyJobSuccessResultInputRequestTypeDef

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


# PutWebhookInputRequestTypeDef

### webhook
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.WebhookDefinitionTypeDef'>
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


# RegisterWebhookWithThirdPartyInputRequestTypeDef

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


# RetryStageExecutionInputRequestTypeDef

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


# RollbackStageInputRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.FailureConditionsTypeDef]


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


# StageExecutionTypeDef

### pipelineExecutionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Cancelled', 'Failed', 'InProgress', 'Stopped', 'Stopping', 'Succeeded']
- **Required**: Yes

### type
- **Type**: typing.Optional[typing.Literal['ROLLBACK', 'STANDARD']]


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


# StartPipelineExecutionInputRequestTypeDef

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


# StopPipelineExecutionInputRequestTypeDef

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


# TagResourceInputRequestTypeDef

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

### id
- **Type**: typing.Optional[str]

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.codepipeline_classes.ThirdPartyJobDataTypeDef]

### nonce
- **Type**: typing.Optional[str]


# ThirdPartyJobTypeDef

### clientId
- **Type**: typing.Optional[str]

### jobId
- **Type**: typing.Optional[str]


# TransitionStateTypeDef

### enabled
- **Type**: typing.Optional[bool]

### lastChangedBy
- **Type**: typing.Optional[str]

### lastChangedAt
- **Type**: typing.Optional[datetime.datetime]

### disabledReason
- **Type**: typing.Optional[str]


# UntagResourceInputRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateActionTypeInputRequestTypeDef

### actionType
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.ActionTypeDeclarationTypeDef'>
- **Required**: Yes


# UpdatePipelineInputRequestTypeDef

### pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.codepipeline_classes.PipelineDeclarationTypeDef'>
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


# WebhookDefinitionExtraOutputTypeDef

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


# WebhookFilterRuleTypeDef

### jsonPath
- **Type**: <class 'str'>
- **Required**: Yes

### matchEquals
- **Type**: typing.Optional[str]


