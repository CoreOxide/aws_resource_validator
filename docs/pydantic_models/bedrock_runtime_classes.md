# Bedrock Runtime Classes

# ApplyGuardrailRequest

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailContentBlock]
- **Required**: Yes


# ApplyGuardrailResponse

### usage
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailUsage'>
- **Required**: Yes

### action
- **Type**: typing.Literal['GUARDRAIL_INTERVENED', 'NONE']
- **Required**: Yes

### outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailOutputContent]
- **Required**: Yes

### assessments
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailAssessment]
- **Required**: Yes

### guardrailCoverage
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailCoverage'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# AsyncInvokeOutputDataConfig

### s3OutputDataConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.AsyncInvokeS3OutputDataConfig]


# AsyncInvokeS3OutputDataConfig

### s3Uri
- **Type**: <class 'str'>
- **Required**: Yes

### kmsKeyId
- **Type**: typing.Optional[str]

### bucketOwner
- **Type**: typing.Optional[str]


# AsyncInvokeSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.AsyncInvokeOutputDataConfig'>
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

# ContentBlock

### text
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ImageBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ImageBlockOutput, NoneType]

### document
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.DocumentBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.DocumentBlockOutput, NoneType]

### video
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.VideoBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.VideoBlockOutput, NoneType]

### toolUse
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolUseBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolUseBlockOutput, NoneType]

### toolResult
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolResultBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolResultBlockOutput, NoneType]

### guardContent
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseContentBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseContentBlockOutput, NoneType]

### reasoningContent
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ReasoningContentBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ReasoningContentBlockOutput, NoneType]


# ContentBlockDelta

### text
- **Type**: typing.Optional[str]

### toolUse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolUseBlockDelta]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ReasoningContentBlockDelta]


# ContentBlockDeltaEvent

### delta
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ContentBlockDelta'>
- **Required**: Yes

### contentBlockIndex
- **Type**: <class 'int'>
- **Required**: Yes


# ContentBlockOutput

### text
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ImageBlockOutput]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.DocumentBlockOutput]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.VideoBlockOutput]

### toolUse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolUseBlockOutput]

### toolResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolResultBlockOutput]

### guardContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseContentBlockOutput]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ReasoningContentBlockOutput]


# ContentBlockStart

### toolUse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolUseBlockStart]


# ContentBlockStartEvent

### start
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ContentBlockStart'>
- **Required**: Yes

### contentBlockIndex
- **Type**: <class 'int'>
- **Required**: Yes


# ContentBlockStopEvent

### contentBlockIndex
- **Type**: <class 'int'>
- **Required**: Yes


# ConverseMetrics

### latencyMs
- **Type**: <class 'int'>
- **Required**: Yes


# ConverseOutput

### message
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.MessageOutput]


# ConverseRequest

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.Message, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.MessageOutput]]]

### system
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.SystemContentBlock]]

### inferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.InferenceConfiguration]

### toolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolConfiguration]

### guardrailConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConfiguration]

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### promptVariables
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.PromptVariableValues]]

### additionalModelResponseFieldPaths
- **Type**: typing.Optional[typing.List[str]]

### requestMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.PerformanceConfiguration]


# ConverseResponse

### output
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ConverseOutput'>
- **Required**: Yes

### stopReason
- **Type**: typing.Literal['content_filtered', 'end_turn', 'guardrail_intervened', 'max_tokens', 'stop_sequence', 'tool_use']
- **Required**: Yes

### usage
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.TokenUsage'>
- **Required**: Yes

### metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ConverseMetrics'>
- **Required**: Yes

### additionalModelResponseFields
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### trace
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ConverseTrace'>
- **Required**: Yes

### performanceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.PerformanceConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# ConverseStreamMetadataEvent

### usage
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.TokenUsage'>
- **Required**: Yes

### metrics
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ConverseStreamMetrics'>
- **Required**: Yes

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ConverseStreamTrace]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.PerformanceConfiguration]


# ConverseStreamMetrics

### latencyMs
- **Type**: <class 'int'>
- **Required**: Yes


# ConverseStreamOutput

### messageStart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.MessageStartEvent]

### contentBlockStart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ContentBlockStartEvent]

### contentBlockDelta
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ContentBlockDeltaEvent]

### contentBlockStop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ContentBlockStopEvent]

### messageStop
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.MessageStopEvent]

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ConverseStreamMetadataEvent]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.InternalServerException]

### modelStreamErrorException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ModelStreamErrorException]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ValidationException]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ThrottlingException]

### serviceUnavailableException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ServiceUnavailableException]


# ConverseStreamRequest

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.Message, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.MessageOutput]]]

### system
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.SystemContentBlock]]

### inferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.InferenceConfiguration]

### toolConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolConfiguration]

### guardrailConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailStreamConfiguration]

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### promptVariables
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.PromptVariableValues]]

### additionalModelResponseFieldPaths
- **Type**: typing.Optional[typing.List[str]]

### requestMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.PerformanceConfiguration]


# ConverseStreamResponse

### stream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ConverseStreamOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# ConverseStreamTrace

### guardrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailTraceAssessment]

### promptRouter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.PromptRouterTrace]


# ConverseTrace

### guardrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailTraceAssessment]

### promptRouter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.PromptRouterTrace]


# DocumentBlock

### format
- **Type**: typing.Literal['csv', 'doc', 'docx', 'html', 'md', 'pdf', 'txt', 'xls', 'xlsx']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.DocumentSource, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.DocumentSourceOutput]
- **Required**: Yes


# DocumentBlockOutput

### format
- **Type**: typing.Literal['csv', 'doc', 'docx', 'html', 'md', 'pdf', 'txt', 'xls', 'xlsx']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.DocumentSourceOutput'>
- **Required**: Yes


# DocumentSource

### bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# DocumentSourceOutput

### bytes
- **Type**: <class 'NoneType'>


# GetAsyncInvokeRequest

### invocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAsyncInvokeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.AsyncInvokeOutputDataConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# GuardrailAssessment

### topicPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailTopicPolicyAssessment]

### contentPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailContentPolicyAssessment]

### wordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailWordPolicyAssessment]

### sensitiveInformationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailSensitiveInformationPolicyAssessment]

### contextualGroundingPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailContextualGroundingPolicyAssessment]

### invocationMetrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailInvocationMetrics]


# GuardrailConfiguration

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: <class 'str'>
- **Required**: Yes

### trace
- **Type**: typing.Optional[typing.Literal['disabled', 'enabled']]


# GuardrailContentBlock

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailTextBlock]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailImageBlock]


# GuardrailContentFilter

### type
- **Type**: typing.Literal['HATE', 'INSULTS', 'MISCONDUCT', 'PROMPT_ATTACK', 'SEXUAL', 'VIOLENCE']
- **Required**: Yes

### confidence
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes

### action
- **Type**: typing.Literal['BLOCKED']
- **Required**: Yes

### filterStrength
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']]


# GuardrailContentPolicyAssessment

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailContentFilter]
- **Required**: Yes


# GuardrailContextualGroundingFilter

### type
- **Type**: typing.Literal['GROUNDING', 'RELEVANCE']
- **Required**: Yes

### threshold
- **Type**: <class 'float'>
- **Required**: Yes

### score
- **Type**: <class 'float'>
- **Required**: Yes

### action
- **Type**: typing.Literal['BLOCKED', 'NONE']
- **Required**: Yes


# GuardrailContextualGroundingPolicyAssessment

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailContextualGroundingFilter]]


# GuardrailConverseContentBlock

### text
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseTextBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseTextBlockOutput, NoneType]

### image
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseImageBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseImageBlockOutput, NoneType]


# GuardrailConverseContentBlockOutput

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseTextBlockOutput]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseImageBlockOutput]


# GuardrailConverseImageBlock

### format
- **Type**: typing.Literal['jpeg', 'png']
- **Required**: Yes

### source
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseImageSource, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseImageSourceOutput]
- **Required**: Yes


# GuardrailConverseImageBlockOutput

### format
- **Type**: typing.Literal['jpeg', 'png']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseImageSourceOutput'>
- **Required**: Yes


# GuardrailConverseImageSource

### bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# GuardrailConverseImageSourceOutput

### bytes
- **Type**: <class 'NoneType'>


# GuardrailConverseTextBlock

### text
- **Type**: <class 'str'>
- **Required**: Yes

### qualifiers
- **Type**: typing.Optional[typing.List[typing.Literal['grounding_source', 'guard_content', 'query']]]


# GuardrailConverseTextBlockOutput

### text
- **Type**: <class 'str'>
- **Required**: Yes

### qualifiers
- **Type**: typing.Optional[typing.List[typing.Literal['grounding_source', 'guard_content', 'query']]]


# GuardrailCoverage

### textCharacters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailTextCharactersCoverage]

### images
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailImageCoverage]


# GuardrailCustomWord

### match
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Literal['BLOCKED']
- **Required**: Yes


# GuardrailImageBlock

### format
- **Type**: typing.Literal['jpeg', 'png']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailImageSource'>
- **Required**: Yes


# GuardrailImageCoverage

### guarded
- **Type**: typing.Optional[int]

### total
- **Type**: typing.Optional[int]


# GuardrailImageSource

### bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# GuardrailInvocationMetrics

### guardrailProcessingLatency
- **Type**: typing.Optional[int]

### usage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailUsage]

### guardrailCoverage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailCoverage]


# GuardrailManagedWord

### match
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['PROFANITY']
- **Required**: Yes

### action
- **Type**: typing.Literal['BLOCKED']
- **Required**: Yes


# GuardrailOutputContent

### text
- **Type**: typing.Optional[str]


# GuardrailPiiEntityFilter

### match
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ADDRESS', 'AGE', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CARD_CVV', 'CREDIT_DEBIT_CARD_EXPIRY', 'CREDIT_DEBIT_CARD_NUMBER', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSWORD', 'PHONE', 'PIN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_BANK_ACCOUNT_NUMBER', 'US_BANK_ROUTING_NUMBER', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'US_PASSPORT_NUMBER', 'US_SOCIAL_SECURITY_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']
- **Required**: Yes

### action
- **Type**: typing.Literal['ANONYMIZED', 'BLOCKED']
- **Required**: Yes


# GuardrailRegexFilter

### action
- **Type**: typing.Literal['ANONYMIZED', 'BLOCKED']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### match
- **Type**: typing.Optional[str]

### regex
- **Type**: typing.Optional[str]


# GuardrailSensitiveInformationPolicyAssessment

### piiEntities
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailPiiEntityFilter]
- **Required**: Yes

### regexes
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailRegexFilter]
- **Required**: Yes


# GuardrailStreamConfiguration

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


# GuardrailTextBlock

### text
- **Type**: <class 'str'>
- **Required**: Yes

### qualifiers
- **Type**: typing.Optional[typing.List[typing.Literal['grounding_source', 'guard_content', 'query']]]


# GuardrailTextCharactersCoverage

### guarded
- **Type**: typing.Optional[int]

### total
- **Type**: typing.Optional[int]


# GuardrailTopic

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DENY']
- **Required**: Yes

### action
- **Type**: typing.Literal['BLOCKED']
- **Required**: Yes


# GuardrailTopicPolicyAssessment

### topics
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailTopic]
- **Required**: Yes


# GuardrailTraceAssessment

### modelOutput
- **Type**: typing.Optional[typing.List[str]]

### inputAssessment
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailAssessment]]

### outputAssessments
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailAssessment]]]


# GuardrailUsage

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


# GuardrailWordPolicyAssessment

### customWords
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailCustomWord]
- **Required**: Yes

### managedWordLists
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailManagedWord]
- **Required**: Yes


# ImageBlock

### format
- **Type**: typing.Literal['gif', 'jpeg', 'png', 'webp']
- **Required**: Yes

### source
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ImageSource, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ImageSourceOutput]
- **Required**: Yes


# ImageBlockOutput

### format
- **Type**: typing.Literal['gif', 'jpeg', 'png', 'webp']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ImageSourceOutput'>
- **Required**: Yes


# ImageSource

### bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# ImageSourceOutput

### bytes
- **Type**: <class 'NoneType'>


# InferenceConfiguration

### maxTokens
- **Type**: typing.Optional[int]

### temperature
- **Type**: typing.Optional[float]

### topP
- **Type**: typing.Optional[float]

### stopSequences
- **Type**: typing.Optional[typing.List[str]]


# InternalServerException

### message
- **Type**: typing.Optional[str]


# InvokeModelRequest

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

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


# InvokeModelResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# InvokeModelWithResponseStreamRequest

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

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


# InvokeModelWithResponseStreamResponse

### body
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ResponseStream]
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### performanceConfigLatency
- **Type**: typing.Literal['optimized', 'standard']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# ListAsyncInvokesRequest

### submitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### submitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

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


# ListAsyncInvokesRequestPaginate

### submitTimeAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### submitTimeBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### statusEquals
- **Type**: typing.Optional[typing.Literal['Completed', 'Failed', 'InProgress']]

### sortBy
- **Type**: typing.Optional[typing.Literal['SubmissionTime']]

### sortOrder
- **Type**: typing.Optional[typing.Literal['Ascending', 'Descending']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.PaginatorConfig]


# ListAsyncInvokesResponse

### asyncInvokeSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.AsyncInvokeSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# Message

### role
- **Type**: typing.Literal['assistant', 'user']
- **Required**: Yes

### content
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ContentBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ContentBlockOutput]]
- **Required**: Yes


# MessageOutput

### role
- **Type**: typing.Literal['assistant', 'user']
- **Required**: Yes

### content
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ContentBlockOutput]
- **Required**: Yes


# MessageStartEvent

### role
- **Type**: typing.Literal['assistant', 'user']
- **Required**: Yes


# MessageStopEvent

### stopReason
- **Type**: typing.Literal['content_filtered', 'end_turn', 'guardrail_intervened', 'max_tokens', 'stop_sequence', 'tool_use']
- **Required**: Yes

### additionalModelResponseFields
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ModelStreamErrorException

### message
- **Type**: typing.Optional[str]

### originalStatusCode
- **Type**: typing.Optional[int]

### originalMessage
- **Type**: typing.Optional[str]


# ModelTimeoutException

### message
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PayloadPart

### bytes
- **Type**: <class 'NoneType'>


# PerformanceConfiguration

### latency
- **Type**: typing.Optional[typing.Literal['optimized', 'standard']]


# PromptRouterTrace

### invokedModelId
- **Type**: typing.Optional[str]


# PromptVariableValues

### text
- **Type**: typing.Optional[str]


# ReasoningContentBlock

### reasoningText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ReasoningTextBlock]

### redactedContent
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# ReasoningContentBlockDelta

### text
- **Type**: typing.Optional[str]

### redactedContent
- **Type**: typing.Optional[bytes]

### signature
- **Type**: typing.Optional[str]


# ReasoningContentBlockOutput

### reasoningText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ReasoningTextBlock]

### redactedContent
- **Type**: typing.Optional[bytes]


# ReasoningTextBlock

### text
- **Type**: <class 'str'>
- **Required**: Yes

### signature
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


# ResponseStream

### chunk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.PayloadPart]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.InternalServerException]

### modelStreamErrorException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ModelStreamErrorException]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ValidationException]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ThrottlingException]

### modelTimeoutException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ModelTimeoutException]

### serviceUnavailableException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ServiceUnavailableException]


# S3Location

### uri
- **Type**: <class 'str'>
- **Required**: Yes

### bucketOwner
- **Type**: typing.Optional[str]


# ServiceUnavailableException

### message
- **Type**: typing.Optional[str]


# SpecificToolChoice

### name
- **Type**: <class 'str'>
- **Required**: Yes


# StartAsyncInvokeRequest

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### modelInput
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### outputDataConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.AsyncInvokeOutputDataConfig'>
- **Required**: Yes

### clientRequestToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.Tag]]


# StartAsyncInvokeResponse

### invocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# SystemContentBlock

### text
- **Type**: typing.Optional[str]

### guardContent
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseContentBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.GuardrailConverseContentBlockOutput, NoneType]


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# ThrottlingException

### message
- **Type**: typing.Optional[str]


# TokenUsage

### inputTokens
- **Type**: <class 'int'>
- **Required**: Yes

### outputTokens
- **Type**: <class 'int'>
- **Required**: Yes

### totalTokens
- **Type**: <class 'int'>
- **Required**: Yes


# Tool

### toolSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolSpecification]


# ToolChoice

### auto
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### any
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### tool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.SpecificToolChoice]


# ToolConfiguration

### tools
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.Tool]
- **Required**: Yes

### toolChoice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolChoice]


# ToolInputSchema

### json
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ToolResultBlock

### toolUseId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolResultContentBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolResultContentBlockOutput]]
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['error', 'success']]


# ToolResultBlockOutput

### toolUseId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolResultContentBlockOutput]
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['error', 'success']]


# ToolResultContentBlock

### json
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### text
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ImageBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ImageBlockOutput, NoneType]

### document
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.DocumentBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.DocumentBlockOutput, NoneType]

### video
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.VideoBlock, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.VideoBlockOutput, NoneType]


# ToolResultContentBlockOutput

### json
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### text
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ImageBlockOutput]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.DocumentBlockOutput]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.VideoBlockOutput]


# ToolSpecification

### name
- **Type**: <class 'str'>
- **Required**: Yes

### inputSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.ToolInputSchema'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ToolUseBlock

### toolUseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### input
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# ToolUseBlockDelta

### input
- **Type**: <class 'str'>
- **Required**: Yes


# ToolUseBlockOutput

### toolUseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### input
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# ToolUseBlockStart

### toolUseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# ValidationException

### message
- **Type**: typing.Optional[str]


# VideoBlock

### format
- **Type**: typing.Literal['flv', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'three_gp', 'webm', 'wmv']
- **Required**: Yes

### source
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.VideoSource, aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.VideoSourceOutput]
- **Required**: Yes


# VideoBlockOutput

### format
- **Type**: typing.Literal['flv', 'mkv', 'mov', 'mp4', 'mpeg', 'mpg', 'three_gp', 'webm', 'wmv']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.VideoSourceOutput'>
- **Required**: Yes


# VideoSource

### bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.S3Location]


# VideoSourceOutput

### bytes
- **Type**: <class 'NoneType'>

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime.bedrock_runtime_classes.S3Location]


