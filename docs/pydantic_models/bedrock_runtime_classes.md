# bedrock_runtime_classes

# ApplyGuardrailRequestRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

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


# ContentBlockOutputTypeDef

### text
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ImageBlockOutputTypeDef]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.DocumentBlockOutputTypeDef]

### toolUse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolUseBlockOutputTypeDef]

### toolResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolResultBlockOutputTypeDef]

### guardContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailConverseContentBlockOutputTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ImageBlockTypeDef]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.DocumentBlockTypeDef]

### toolUse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolUseBlockTypeDef]

### toolResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolResultBlockTypeDef]

### guardContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailConverseContentBlockTypeDef]


# ConverseMetricsTypeDef

### latencyMs
- **Type**: <class 'int'>
- **Required**: Yes


# ConverseOutputTypeDef

### message
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.MessageOutputTypeDef]


# ConverseRequestRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime_classes.MessageTypeDef, aws_resource_validator.pydantic_models.bedrock_runtime_classes.MessageOutputTypeDef]]
- **Required**: Yes

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

### additionalModelResponseFieldPaths
- **Type**: typing.Optional[typing.Sequence[str]]


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


# ConverseStreamRequestRequestTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### messages
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.bedrock_runtime_classes.MessageTypeDef, aws_resource_validator.pydantic_models.bedrock_runtime_classes.MessageOutputTypeDef]]
- **Required**: Yes

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

### additionalModelResponseFieldPaths
- **Type**: typing.Optional[typing.Sequence[str]]


# ConverseStreamResponseTypeDef

### stream
- **Type**: ForwardRef('EventStream[ConverseStreamOutputTypeDef]')
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConverseStreamTraceTypeDef

### guardrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailTraceAssessmentTypeDef]


# ConverseTraceTypeDef

### guardrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailTraceAssessmentTypeDef]


# DocumentBlockOutputTypeDef

### format
- **Type**: typing.Literal['csv', 'doc', 'docx', 'html', 'md', 'pdf', 'txt', 'xls', 'xlsx']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.DocumentSourceOutputTypeDef'>
- **Required**: Yes


# DocumentBlockTypeDef

### format
- **Type**: typing.Literal['csv', 'doc', 'docx', 'html', 'md', 'pdf', 'txt', 'xls', 'xlsx']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.DocumentSourceTypeDef'>
- **Required**: Yes


# DocumentSourceOutputTypeDef

### bytes
- **Type**: <class 'NoneType'>


# DocumentSourceTypeDef

### bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


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


# GuardrailContentFilterTypeDef

### type
- **Type**: typing.Literal['HATE', 'INSULTS', 'MISCONDUCT', 'PROMPT_ATTACK', 'SEXUAL', 'VIOLENCE']
- **Required**: Yes

### confidence
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes

### action
- **Type**: typing.Literal['BLOCKED']
- **Required**: Yes


# GuardrailContentPolicyAssessmentTypeDef

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailContentFilterTypeDef]
- **Required**: Yes


# GuardrailContextualGroundingFilterTypeDef

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


# GuardrailContextualGroundingPolicyAssessmentTypeDef

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailContextualGroundingFilterTypeDef]]


# GuardrailConverseContentBlockOutputTypeDef

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailConverseTextBlockOutputTypeDef]


# GuardrailConverseContentBlockTypeDef

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailConverseTextBlockTypeDef]


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


# GuardrailCustomWordTypeDef

### match
- **Type**: <class 'str'>
- **Required**: Yes

### action
- **Type**: typing.Literal['BLOCKED']
- **Required**: Yes


# GuardrailManagedWordTypeDef

### match
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['PROFANITY']
- **Required**: Yes

### action
- **Type**: typing.Literal['BLOCKED']
- **Required**: Yes


# GuardrailOutputContentTypeDef

### text
- **Type**: typing.Optional[str]


# GuardrailPiiEntityFilterTypeDef

### match
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ADDRESS', 'AGE', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CARD_CVV', 'CREDIT_DEBIT_CARD_EXPIRY', 'CREDIT_DEBIT_CARD_NUMBER', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSWORD', 'PHONE', 'PIN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_BANK_ACCOUNT_NUMBER', 'US_BANK_ROUTING_NUMBER', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'US_PASSPORT_NUMBER', 'US_SOCIAL_SECURITY_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']
- **Required**: Yes

### action
- **Type**: typing.Literal['ANONYMIZED', 'BLOCKED']
- **Required**: Yes


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


# GuardrailTopicPolicyAssessmentTypeDef

### topics
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailTopicTypeDef]
- **Required**: Yes


# GuardrailTopicTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DENY']
- **Required**: Yes

### action
- **Type**: typing.Literal['BLOCKED']
- **Required**: Yes


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

### format
- **Type**: typing.Literal['gif', 'jpeg', 'png', 'webp']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ImageSourceOutputTypeDef'>
- **Required**: Yes


# ImageBlockTypeDef

### format
- **Type**: typing.Literal['gif', 'jpeg', 'png', 'webp']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ImageSourceTypeDef'>
- **Required**: Yes


# ImageSourceOutputTypeDef

### bytes
- **Type**: <class 'NoneType'>


# ImageSourceTypeDef

### bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


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


# InvokeModelRequestRequestTypeDef

### body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

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


# InvokeModelResponseTypeDef

### body
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InvokeModelWithResponseStreamRequestRequestTypeDef

### body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

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


# InvokeModelWithResponseStreamResponseTypeDef

### body
- **Type**: ForwardRef('EventStream[ResponseStreamTypeDef]')
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ContentBlockTypeDef]
- **Required**: Yes


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


# PayloadPartTypeDef

### bytes
- **Type**: <class 'NoneType'>


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


# SpecificToolChoiceTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# SystemContentBlockTypeDef

### text
- **Type**: typing.Optional[str]

### guardContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.GuardrailConverseContentBlockTypeDef]


# ThrottlingExceptionTypeDef

### message
- **Type**: typing.Optional[str]


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

### auto
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### any
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### tool
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.SpecificToolChoiceTypeDef]


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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ToolResultContentBlockTypeDef]
- **Required**: Yes

### status
- **Type**: typing.Optional[typing.Literal['error', 'success']]


# ToolResultContentBlockOutputTypeDef

### json
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### text
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ImageBlockOutputTypeDef]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.DocumentBlockOutputTypeDef]


# ToolResultContentBlockTypeDef

### json
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### text
- **Type**: typing.Optional[str]

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.ImageBlockTypeDef]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_runtime_classes.DocumentBlockTypeDef]


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

### input
- **Type**: <class 'str'>
- **Required**: Yes


# ToolUseBlockOutputTypeDef

### toolUseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### input
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# ToolUseBlockStartTypeDef

### toolUseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# ToolUseBlockTypeDef

### toolUseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### input
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# ValidationExceptionTypeDef

### message
- **Type**: typing.Optional[str]


