# Bedrock Runtime Classes

# ApplyGuardrailRequestTypeDef

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: typing.Literal['INPUT', 'OUTPUT']
- **Required**: Yes

### content
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailContentBlockTypeDef]
- **Required**: Yes


# ApplyGuardrailResponseTypeDef

### usage
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailUsageTypeDef'>
- **Required**: Yes

### action
- **Type**: typing.Literal['GUARDRAIL_INTERVENED', 'NONE']
- **Required**: Yes

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailOutputContentTypeDef]
- **Required**: Yes

### assessments
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailAssessmentTypeDef]
- **Required**: Yes

### guardrailCoverage
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailCoverageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AsyncInvokeOutputDataConfigTypeDef

### s3OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.AsyncInvokeS3OutputDataConfigTypeDef]


# AsyncInvokeS3OutputDataConfigTypeDef

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]

### bucketOwner
- **Type**: typing.Optional[str]


# AsyncInvokeSummaryTypeDef

### invocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### submitTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.AsyncInvokeOutputDataConfigTypeDef'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress']]

### failureMessage
- **Type**: typing.Optional[str]

### lastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContentBlockDeltaEventTypeDef

### delta
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ContentBlockDeltaTypeDef'>
- **Required**: Yes

### contentBlockIndex
- **Type**: <class 'int'>
- **Required**: Yes


# ContentBlockDeltaTypeDef

### text
- **Type**: typing.Optional[str]

### toolUse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolUseBlockDeltaTypeDef]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ReasoningContentBlockDeltaTypeDef]


# ContentBlockOutputTypeDef

### text
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ImageBlockOutputTypeDef]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.DocumentBlockOutputTypeDef]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.VideoBlockOutputTypeDef]

### toolUse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolUseBlockOutputTypeDef]

### toolResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolResultBlockOutputTypeDef]

### guardContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailConverseContentBlockOutputTypeDef]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ReasoningContentBlockOutputTypeDef]


# ContentBlockStartEventTypeDef

### start
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ContentBlockStartTypeDef'>
- **Required**: Yes

### contentBlockIndex
- **Type**: <class 'int'>
- **Required**: Yes


# ContentBlockStartTypeDef

### toolUse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolUseBlockStartTypeDef]


# ContentBlockStopEventTypeDef

### contentBlockIndex
- **Type**: <class 'int'>
- **Required**: Yes


# ContentBlockTypeDef

### text
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ImageBlockUnionTypeDef]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.DocumentBlockUnionTypeDef]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.VideoBlockUnionTypeDef]

### toolUse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolUseBlockUnionTypeDef]

### toolResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolResultBlockUnionTypeDef]

### guardContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailConverseContentBlockUnionTypeDef]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ReasoningContentBlockUnionTypeDef]


# ContentBlockUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConverseMetricsTypeDef

### latencyMs
- **Type**: <class 'int'>
- **Required**: Yes


# ConverseOutputTypeDef

### message
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.MessageOutputTypeDef]


# ConverseRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_runtime_classes.MessageUnionTypeDef]]

### system
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_runtime_classes.SystemContentBlockTypeDef]]

### inferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.InferenceConfigurationTypeDef]

### toolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolConfigurationTypeDef]

### guardrailConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailConfigurationTypeDef]

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### promptVariables
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.bedrock_runtime_classes.PromptVariableValuesTypeDef]]

### additionalModelResponseFieldPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### requestMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.PerformanceConfigurationTypeDef]


# ConverseResponseTypeDef

### output
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ConverseOutputTypeDef'>
- **Required**: Yes

### stopReason
- **Type**: typing.Literal['content_filtered', 'end_turn', 'guardrail_intervened', 'max_tokens', 'stop_sequence', 'tool_use']
- **Required**: Yes

### usage
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.TokenUsageTypeDef'>
- **Required**: Yes

### metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ConverseMetricsTypeDef'>
- **Required**: Yes

### additionalModelResponseFields
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### trace
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ConverseTraceTypeDef'>
- **Required**: Yes

### performanceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.PerformanceConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConverseStreamMetadataEventTypeDef

### usage
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.TokenUsageTypeDef'>
- **Required**: Yes

### metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ConverseStreamMetricsTypeDef'>
- **Required**: Yes

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ConverseStreamTraceTypeDef]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.PerformanceConfigurationTypeDef]


# ConverseStreamMetricsTypeDef

### latencyMs
- **Type**: <class 'int'>
- **Required**: Yes


# ConverseStreamOutputTypeDef

### messageStart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.MessageStartEventTypeDef]

### contentBlockStart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ContentBlockStartEventTypeDef]

### contentBlockDelta
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ContentBlockDeltaEventTypeDef]

### contentBlockStop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ContentBlockStopEventTypeDef]

### messageStop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.MessageStopEventTypeDef]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ConverseStreamMetadataEventTypeDef]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.InternalServerExceptionTypeDef]

### modelStreamErrorException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ModelStreamErrorExceptionTypeDef]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ValidationExceptionTypeDef]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ThrottlingExceptionTypeDef]

### serviceUnavailableException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ServiceUnavailableExceptionTypeDef]


# ConverseStreamRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_runtime_classes.MessageUnionTypeDef]]

### system
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_runtime_classes.SystemContentBlockTypeDef]]

### inferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.InferenceConfigurationTypeDef]

### toolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolConfigurationTypeDef]

### guardrailConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailStreamConfigurationTypeDef]

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### promptVariables
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.bedrock_runtime_classes.PromptVariableValuesTypeDef]]

### additionalModelResponseFieldPaths
- **Type**: typing.Optional[typing.Sequence[str]]

### requestMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.PerformanceConfigurationTypeDef]


# ConverseStreamResponseTypeDef

### stream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ConverseStreamOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConverseStreamTraceTypeDef

### guardrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailTraceAssessmentTypeDef]

### promptRouter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.PromptRouterTraceTypeDef]


# ConverseTraceTypeDef

### guardrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailTraceAssessmentTypeDef]

### promptRouter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.PromptRouterTraceTypeDef]


# DocumentBlockOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DocumentBlockUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAsyncInvokeRequestTypeDef

### invocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAsyncInvokeResponseTypeDef

### invocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Completed', 'Failed', 'InProgress']
- **Required**: Yes

### failureMessage
- **Type**: <class 'str'>
- **Required**: Yes

### submitTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.AsyncInvokeOutputDataConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GuardrailAssessmentTypeDef

### topicPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailTopicPolicyAssessmentTypeDef]

### contentPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailContentPolicyAssessmentTypeDef]

### wordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailWordPolicyAssessmentTypeDef]

### sensitiveInformationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailSensitiveInformationPolicyAssessmentTypeDef]

### contextualGroundingPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailContextualGroundingPolicyAssessmentTypeDef]

### invocationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailInvocationMetricsTypeDef]


# GuardrailConfigurationTypeDef

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: <class 'str'>
- **Required**: Yes

### trace
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]


# GuardrailContentBlockTypeDef

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailTextBlockTypeDef]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailImageBlockTypeDef]


# GuardrailContentFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailContentPolicyAssessmentTypeDef

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailContentFilterTypeDef]
- **Required**: Yes


# GuardrailContextualGroundingFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailContextualGroundingPolicyAssessmentTypeDef

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailContextualGroundingFilterTypeDef]]


# GuardrailConverseContentBlockOutputTypeDef

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailConverseTextBlockOutputTypeDef]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailConverseImageBlockOutputTypeDef]


# GuardrailConverseContentBlockTypeDef

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailConverseTextBlockUnionTypeDef]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailConverseImageBlockUnionTypeDef]


# GuardrailConverseContentBlockUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailConverseImageBlockOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailConverseImageBlockUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailConverseTextBlockOutputTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes

### qualifiers
- **Type**: typing.Optional[typing.List[typing.Literal['grounding_source', 'guard_content', 'query']]]


# GuardrailConverseTextBlockTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes

### qualifiers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['grounding_source', 'guard_content', 'query']]]


# GuardrailConverseTextBlockUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailCoverageTypeDef

### textCharacters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailTextCharactersCoverageTypeDef]

### images
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailImageCoverageTypeDef]


# GuardrailCustomWordTypeDef

### match
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Literal['BLOCKED']
- **Required**: Yes


# GuardrailImageBlockTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailImageCoverageTypeDef

### guarded
- **Type**: typing.Optional[int]

### total
- **Type**: typing.Optional[int]


# GuardrailInvocationMetricsTypeDef

### guardrailProcessingLatency
- **Type**: typing.Optional[int]

### usage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailUsageTypeDef]

### guardrailCoverage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailCoverageTypeDef]


# GuardrailManagedWordTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailOutputContentTypeDef

### text
- **Type**: typing.Optional[str]


# GuardrailPiiEntityFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailRegexFilterTypeDef

### action
- **Type**: typing.Literal['ANONYMIZED', 'BLOCKED']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### match
- **Type**: typing.Optional[str]

### regex
- **Type**: typing.Optional[str]


# GuardrailSensitiveInformationPolicyAssessmentTypeDef

### piiEntities
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailPiiEntityFilterTypeDef]
- **Required**: Yes

### regexes
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailRegexFilterTypeDef]
- **Required**: Yes


# GuardrailStreamConfigurationTypeDef

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: <class 'str'>
- **Required**: Yes

### trace
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]

### streamProcessingMode
- **Type**: typing.Optional[typing.Literal['async', 'sync']]


# GuardrailTextBlockTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes

### qualifiers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['grounding_source', 'guard_content', 'query']]]


# GuardrailTextCharactersCoverageTypeDef

### guarded
- **Type**: typing.Optional[int]

### total
- **Type**: typing.Optional[int]


# GuardrailTopicPolicyAssessmentTypeDef

### topics
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailTopicTypeDef]
- **Required**: Yes


# GuardrailTopicTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailTraceAssessmentTypeDef

### modelOutput
- **Type**: typing.Optional[typing.List[str]]

### inputAssessment
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailAssessmentTypeDef]]

### outputAssessments
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailAssessmentTypeDef]]]


# GuardrailUsageTypeDef

### topicPolicyUnits
- **Type**: <class 'int'>
- **Required**: Yes

### contentPolicyUnits
- **Type**: <class 'int'>
- **Required**: Yes

### wordPolicyUnits
- **Type**: <class 'int'>
- **Required**: Yes

### sensitiveInformationPolicyUnits
- **Type**: <class 'int'>
- **Required**: Yes

### sensitiveInformationPolicyFreeUnits
- **Type**: <class 'int'>
- **Required**: Yes

### contextualGroundingPolicyUnits
- **Type**: <class 'int'>
- **Required**: Yes


# GuardrailWordPolicyAssessmentTypeDef

### customWords
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailCustomWordTypeDef]
- **Required**: Yes

### managedWordLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailManagedWordTypeDef]
- **Required**: Yes


# ImageBlockOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageBlockUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InferenceConfigurationTypeDef

### maxTokens
- **Type**: typing.Optional[int]

### temperature
- **Type**: typing.Optional[float]

### topP
- **Type**: typing.Optional[float]

### stopSequences
- **Type**: typing.Optional[typing.Sequence[str]]


# InternalServerExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# InvokeModelRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.BlobTypeDef]

### contentType
- **Type**: typing.Optional[str]

### accept
- **Type**: typing.Optional[str]

### trace
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### guardrailIdentifier
- **Type**: typing.Optional[str]

### guardrailVersion
- **Type**: typing.Optional[str]

### performanceConfigLatency
- **Type**: typing.Optional[typing.Literal['optimized', 'standard']]


# InvokeModelResponseTypeDef

### body
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### performanceConfigLatency
- **Type**: typing.Literal['optimized', 'standard']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InvokeModelWithResponseStreamRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.BlobTypeDef]

### contentType
- **Type**: typing.Optional[str]

### accept
- **Type**: typing.Optional[str]

### trace
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### guardrailIdentifier
- **Type**: typing.Optional[str]

### guardrailVersion
- **Type**: typing.Optional[str]

### performanceConfigLatency
- **Type**: typing.Optional[typing.Literal['optimized', 'standard']]


# InvokeModelWithResponseStreamResponseTypeDef

### body
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ResponseStreamTypeDef]
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### performanceConfigLatency
- **Type**: typing.Literal['optimized', 'standard']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAsyncInvokesRequestPaginateTypeDef

### submitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.TimestampTypeDef]

### submitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress']]

### sortBy
- **Type**: typing.Optional[typing.Literal['SubmissionTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.PaginatorConfigTypeDef]


# ListAsyncInvokesRequestTypeDef

### submitTimeAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.TimestampTypeDef]

### submitTimeBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.TimestampTypeDef]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress']]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['SubmissionTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]


# ListAsyncInvokesResponseTypeDef

### asyncInvokeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.AsyncInvokeSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# MessageOutputTypeDef

### role
- **Type**: typing.Literal['assistant', 'user']
- **Required**: Yes

### content
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ContentBlockOutputTypeDef]
- **Required**: Yes


# MessageStartEventTypeDef

### role
- **Type**: typing.Literal['assistant', 'user']
- **Required**: Yes


# MessageStopEventTypeDef

### stopReason
- **Type**: typing.Literal['content_filtered', 'end_turn', 'guardrail_intervened', 'max_tokens', 'stop_sequence', 'tool_use']
- **Required**: Yes

### additionalModelResponseFields
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# MessageTypeDef

### role
- **Type**: typing.Literal['assistant', 'user']
- **Required**: Yes

### content
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ContentBlockUnionTypeDef]
- **Required**: Yes


# MessageUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelStreamErrorExceptionTypeDef

### message
- **Type**: typing.Optional[str]

### originalStatusCode
- **Type**: typing.Optional[int]

### originalMessage
- **Type**: typing.Optional[str]


# ModelTimeoutExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PayloadPartTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PerformanceConfigurationTypeDef

### latency
- **Type**: typing.Optional[typing.Literal['optimized', 'standard']]


# PromptRouterTraceTypeDef

### invokedModelId
- **Type**: typing.Optional[str]


# PromptVariableValuesTypeDef

### text
- **Type**: typing.Optional[str]


# ReasoningContentBlockDeltaTypeDef

### text
- **Type**: typing.Optional[str]

### redactedContent
- **Type**: typing.Optional[bytes]

### signature
- **Type**: typing.Optional[str]


# ReasoningContentBlockOutputTypeDef

### reasoningText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ReasoningTextBlockTypeDef]

### redactedContent
- **Type**: typing.Optional[bytes]


# ReasoningContentBlockTypeDef

### reasoningText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ReasoningTextBlockTypeDef]

### redactedContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.BlobTypeDef]


# ReasoningContentBlockUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ReasoningTextBlockTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes

### signature
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


# ResponseStreamTypeDef

### chunk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.PayloadPartTypeDef]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.InternalServerExceptionTypeDef]

### modelStreamErrorException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ModelStreamErrorExceptionTypeDef]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ValidationExceptionTypeDef]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ThrottlingExceptionTypeDef]

### modelTimeoutException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ModelTimeoutExceptionTypeDef]

### serviceUnavailableException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ServiceUnavailableExceptionTypeDef]


# S3LocationTypeDef

### uri
- **Type**: <class 'str'>
- **Required**: Yes

### bucketOwner
- **Type**: typing.Optional[str]


# ServiceUnavailableExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# SpecificToolChoiceTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# StartAsyncInvokeRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelInput
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.AsyncInvokeOutputDataConfigTypeDef'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_runtime_classes.TagTypeDef]]


# StartAsyncInvokeResponseTypeDef

### invocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SystemContentBlockTypeDef

### text
- **Type**: typing.Optional[str]

### guardContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailConverseContentBlockUnionTypeDef]


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ThrottlingExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TokenUsageTypeDef

### inputTokens
- **Type**: <class 'int'>
- **Required**: Yes

### outputTokens
- **Type**: <class 'int'>
- **Required**: Yes

### totalTokens
- **Type**: <class 'int'>
- **Required**: Yes


# ToolChoiceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolConfigurationTypeDef

### tools
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolTypeDef]
- **Required**: Yes

### toolChoice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolChoiceTypeDef]


# ToolInputSchemaTypeDef

### json
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ToolResultBlockOutputTypeDef

### toolUseId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolResultContentBlockOutputTypeDef]
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['error', 'success']]


# ToolResultBlockTypeDef

### toolUseId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolResultContentBlockUnionTypeDef]
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['error', 'success']]


# ToolResultBlockUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolResultContentBlockOutputTypeDef

### json
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### text
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ImageBlockOutputTypeDef]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.DocumentBlockOutputTypeDef]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.VideoBlockOutputTypeDef]


# ToolResultContentBlockTypeDef

### json
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### text
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ImageBlockUnionTypeDef]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.DocumentBlockUnionTypeDef]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.VideoBlockUnionTypeDef]


# ToolResultContentBlockUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolSpecificationTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### inputSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolInputSchemaTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ToolTypeDef

### toolSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolSpecificationTypeDef]


# ToolUseBlockDeltaTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolUseBlockOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolUseBlockStartTypeDef

### toolUseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# ToolUseBlockUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ValidationExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# VideoBlockOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VideoBlockUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

