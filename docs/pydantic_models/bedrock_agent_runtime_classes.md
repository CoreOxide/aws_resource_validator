# Bedrock Agent Runtime Classes

# AccessDeniedExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# ActionGroupInvocationInputTypeDef

### actionGroupName
- **Type**: typing.Optional[str]

### apiPath
- **Type**: typing.Optional[str]

### executionType
- **Type**: typing.Optional[typing.Literal['LAMBDA', 'RETURN_CONTROL']]

### function
- **Type**: typing.Optional[str]

### invocationId
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ParameterTypeDef]]

### requestBody
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RequestBodyTypeDef]

### verb
- **Type**: typing.Optional[str]


# ActionGroupInvocationOutputTypeDef

### text
- **Type**: typing.Optional[str]


# ApiInvocationInputTypeDef

### actionGroup
- **Type**: <class 'str'>
- **Required**: Yes

### apiPath
- **Type**: typing.Optional[str]

### httpMethod
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiParameterTypeDef]]

### requestBody
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiRequestBodyTypeDef]


# ApiParameterTypeDef

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# ApiRequestBodyTypeDef

### content
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PropertyParametersTypeDef]]


# ApiResultTypeDef

### actionGroup
- **Type**: <class 'str'>
- **Required**: Yes

### apiPath
- **Type**: typing.Optional[str]

### httpMethod
- **Type**: typing.Optional[str]

### httpStatusCode
- **Type**: typing.Optional[int]

### responseBody
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ContentBodyTypeDef]]

### responseState
- **Type**: typing.Optional[typing.Literal['FAILURE', 'REPROMPT']]


# AttributionTypeDef

### citations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CitationTypeDef]]


# BadGatewayExceptionTypeDef

### message
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ByteContentDocTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# ByteContentFileTypeDef

### data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### mediaType
- **Type**: <class 'str'>
- **Required**: Yes


# CitationTypeDef

### generatedResponsePart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GeneratedResponsePartTypeDef]

### retrievedReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievedReferenceTypeDef]]


# CodeInterpreterInvocationInputTypeDef

### code
- **Type**: typing.Optional[str]

### files
- **Type**: typing.Optional[typing.List[str]]


# CodeInterpreterInvocationOutputTypeDef

### executionError
- **Type**: typing.Optional[str]

### executionOutput
- **Type**: typing.Optional[str]

### executionTimeout
- **Type**: typing.Optional[bool]

### files
- **Type**: typing.Optional[typing.List[str]]


# ConflictExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# ContentBodyTypeDef

### body
- **Type**: typing.Optional[str]


# DeleteAgentMemoryRequestRequestTypeDef

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### memoryId
- **Type**: typing.Optional[str]


# DependencyFailedExceptionTypeDef

### message
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]


# ExternalSourceTypeDef

### sourceType
- **Type**: typing.Literal['BYTE_CONTENT', 'S3']
- **Required**: Yes

### byteContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ByteContentDocTypeDef]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.S3ObjectDocTypeDef]


# ExternalSourcesGenerationConfigurationTypeDef

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailConfigurationTypeDef]

### inferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InferenceConfigTypeDef]

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PromptTemplateTypeDef]


# ExternalSourcesRetrieveAndGenerateConfigurationTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ExternalSourceTypeDef]
- **Required**: Yes

### generationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ExternalSourcesGenerationConfigurationTypeDef]


# FailureTraceTypeDef

### failureReason
- **Type**: typing.Optional[str]

### traceId
- **Type**: typing.Optional[str]


# FilePartTypeDef

### files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OutputFileTypeDef]]


# FileSourceTypeDef

### sourceType
- **Type**: typing.Literal['BYTE_CONTENT', 'S3']
- **Required**: Yes

### byteContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ByteContentFileTypeDef]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.S3ObjectFileTypeDef]


# FilterAttributeTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# FinalResponseTypeDef

### text
- **Type**: typing.Optional[str]


# FlowCompletionEventTypeDef

### completionReason
- **Type**: typing.Literal['SUCCESS']
- **Required**: Yes


# FlowInputContentTypeDef

### document
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# FlowInputTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowInputContentTypeDef'>
- **Required**: Yes

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### nodeOutputName
- **Type**: <class 'str'>
- **Required**: Yes


# FlowOutputContentTypeDef

### document
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowOutputEventTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowOutputContentTypeDef'>
- **Required**: Yes

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### nodeType
- **Type**: typing.Literal['ConditionNode', 'FlowInputNode', 'FlowOutputNode', 'KnowledgeBaseNode', 'LambdaFunctionNode', 'LexNode', 'PromptNode']
- **Required**: Yes


# FlowResponseStreamTypeDef

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AccessDeniedExceptionTypeDef]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BadGatewayExceptionTypeDef]

### conflictException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ConflictExceptionTypeDef]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.DependencyFailedExceptionTypeDef]

### flowCompletionEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowCompletionEventTypeDef]

### flowOutputEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowOutputEventTypeDef]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InternalServerExceptionTypeDef]

### resourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResourceNotFoundExceptionTypeDef]

### serviceQuotaExceededException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ServiceQuotaExceededExceptionTypeDef]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ThrottlingExceptionTypeDef]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ValidationExceptionTypeDef]


# FunctionInvocationInputTypeDef

### actionGroup
- **Type**: <class 'str'>
- **Required**: Yes

### function
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionParameterTypeDef]]


# FunctionParameterTypeDef

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# FunctionResultTypeDef

### actionGroup
- **Type**: <class 'str'>
- **Required**: Yes

### function
- **Type**: typing.Optional[str]

### responseBody
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ContentBodyTypeDef]]

### responseState
- **Type**: typing.Optional[typing.Literal['FAILURE', 'REPROMPT']]


# GeneratedResponsePartTypeDef

### textResponsePart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TextResponsePartTypeDef]


# GenerationConfigurationTypeDef

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailConfigurationTypeDef]

### inferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InferenceConfigTypeDef]

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PromptTemplateTypeDef]


# GetAgentMemoryRequestGetAgentMemoryPaginateTypeDef

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### memoryId
- **Type**: <class 'str'>
- **Required**: Yes

### memoryType
- **Type**: typing.Literal['SESSION_SUMMARY']
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PaginatorConfigTypeDef]


# GetAgentMemoryRequestRequestTypeDef

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### memoryId
- **Type**: <class 'str'>
- **Required**: Yes

### memoryType
- **Type**: typing.Literal['SESSION_SUMMARY']
- **Required**: Yes

### maxItems
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# GetAgentMemoryResponseTypeDef

### memoryContents
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.MemoryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GuardrailAssessmentTypeDef

### contentPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailContentPolicyAssessmentTypeDef]

### sensitiveInformationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailSensitiveInformationPolicyAssessmentTypeDef]

### topicPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailTopicPolicyAssessmentTypeDef]

### wordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailWordPolicyAssessmentTypeDef]


# GuardrailConfigurationTypeDef

### guardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GuardrailContentFilterTypeDef

### action
- **Type**: typing.Optional[typing.Literal['BLOCKED']]

### confidence
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']]

### type
- **Type**: typing.Optional[typing.Literal['HATE', 'INSULTS', 'MISCONDUCT', 'PROMPT_ATTACK', 'SEXUAL', 'VIOLENCE']]


# GuardrailContentPolicyAssessmentTypeDef

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailContentFilterTypeDef]]


# GuardrailCustomWordTypeDef

### action
- **Type**: typing.Optional[typing.Literal['BLOCKED']]

### match
- **Type**: typing.Optional[str]


# GuardrailManagedWordTypeDef

### action
- **Type**: typing.Optional[typing.Literal['BLOCKED']]

### match
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['PROFANITY']]


# GuardrailPiiEntityFilterTypeDef

### action
- **Type**: typing.Optional[typing.Literal['ANONYMIZED', 'BLOCKED']]

### match
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['ADDRESS', 'AGE', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CARD_CVV', 'CREDIT_DEBIT_CARD_EXPIRY', 'CREDIT_DEBIT_CARD_NUMBER', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSWORD', 'PHONE', 'PIN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_BANK_ACCOUNT_NUMBER', 'US_BANK_ROUTING_NUMBER', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'US_PASSPORT_NUMBER', 'US_SOCIAL_SECURITY_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']]


# GuardrailRegexFilterTypeDef

### action
- **Type**: typing.Optional[typing.Literal['ANONYMIZED', 'BLOCKED']]

### match
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### regex
- **Type**: typing.Optional[str]


# GuardrailSensitiveInformationPolicyAssessmentTypeDef

### piiEntities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailPiiEntityFilterTypeDef]]

### regexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailRegexFilterTypeDef]]


# GuardrailTopicPolicyAssessmentTypeDef

### topics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailTopicTypeDef]]


# GuardrailTopicTypeDef

### action
- **Type**: typing.Optional[typing.Literal['BLOCKED']]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['DENY']]


# GuardrailTraceTypeDef

### action
- **Type**: typing.Optional[typing.Literal['INTERVENED', 'NONE']]

### inputAssessments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailAssessmentTypeDef]]

### outputAssessments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailAssessmentTypeDef]]

### traceId
- **Type**: typing.Optional[str]


# GuardrailWordPolicyAssessmentTypeDef

### customWords
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailCustomWordTypeDef]]

### managedWordLists
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailManagedWordTypeDef]]


# InferenceConfigTypeDef

### textInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TextInferenceConfigTypeDef]


# InferenceConfigurationTypeDef

### maximumLength
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.List[str]]

### temperature
- **Type**: typing.Optional[float]

### topK
- **Type**: typing.Optional[int]

### topP
- **Type**: typing.Optional[float]


# InputFileTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FileSourceTypeDef'>
- **Required**: Yes

### useCase
- **Type**: typing.Literal['CHAT', 'CODE_INTERPRETER']
- **Required**: Yes


# InternalServerExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# InvocationInputMemberTypeDef

### apiInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiInvocationInputTypeDef]

### functionInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionInvocationInputTypeDef]


# InvocationInputTypeDef

### actionGroupInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ActionGroupInvocationInputTypeDef]

### codeInterpreterInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CodeInterpreterInvocationInputTypeDef]

### invocationType
- **Type**: typing.Optional[typing.Literal['ACTION_GROUP', 'ACTION_GROUP_CODE_INTERPRETER', 'FINISH', 'KNOWLEDGE_BASE']]

### knowledgeBaseLookupInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseLookupInputTypeDef]

### traceId
- **Type**: typing.Optional[str]


# InvocationResultMemberTypeDef

### apiResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiResultTypeDef]

### functionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionResultTypeDef]


# InvokeAgentRequestRequestTypeDef

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### enableTrace
- **Type**: typing.Optional[bool]

### endSession
- **Type**: typing.Optional[bool]

### inputText
- **Type**: typing.Optional[str]

### memoryId
- **Type**: typing.Optional[str]

### sessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.SessionStateTypeDef]


# InvokeAgentResponseTypeDef

### completion
- **Type**: ForwardRef('EventStream[ResponseStreamTypeDef]')
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### memoryId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InvokeFlowRequestRequestTypeDef

### flowAliasIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### inputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowInputTypeDef]
- **Required**: Yes


# InvokeFlowResponseTypeDef

### responseStream
- **Type**: ForwardRef('EventStream[FlowResponseStreamTypeDef]')
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# KnowledgeBaseConfigurationTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfigurationTypeDef'>
- **Required**: Yes


# KnowledgeBaseLookupInputTypeDef

### knowledgeBaseId
- **Type**: typing.Optional[str]

### text
- **Type**: typing.Optional[str]


# KnowledgeBaseLookupOutputTypeDef

### retrievedReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievedReferenceTypeDef]]


# KnowledgeBaseQueryTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes


# KnowledgeBaseRetrievalConfigurationTypeDef

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseVectorSearchConfigurationTypeDef'>
- **Required**: Yes


# KnowledgeBaseRetrievalResultTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalResultContentTypeDef'>
- **Required**: Yes

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalResultLocationTypeDef]

### metadata
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

### score
- **Type**: typing.Optional[float]


# KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### generationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GenerationConfigurationTypeDef]

### orchestrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OrchestrationConfigurationTypeDef]

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfigurationTypeDef]


# KnowledgeBaseVectorSearchConfigurationTypeDef

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalFilterTypeDef]

### numberOfResults
- **Type**: typing.Optional[int]

### overrideSearchType
- **Type**: typing.Optional[typing.Literal['HYBRID', 'SEMANTIC']]


# MemorySessionSummaryTypeDef

### memoryId
- **Type**: typing.Optional[str]

### sessionExpiryTime
- **Type**: typing.Optional[datetime.datetime]

### sessionId
- **Type**: typing.Optional[str]

### sessionStartTime
- **Type**: typing.Optional[datetime.datetime]

### summaryText
- **Type**: typing.Optional[str]


# MemoryTypeDef

### sessionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.MemorySessionSummaryTypeDef]


# ModelInvocationInputTypeDef

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InferenceConfigurationTypeDef]

### overrideLambda
- **Type**: typing.Optional[str]

### parserMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### promptCreationMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### text
- **Type**: typing.Optional[str]

### traceId
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE_RESPONSE_GENERATION', 'ORCHESTRATION', 'POST_PROCESSING', 'PRE_PROCESSING']]


# ObservationTypeDef

### actionGroupInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ActionGroupInvocationOutputTypeDef]

### codeInterpreterInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CodeInterpreterInvocationOutputTypeDef]

### finalResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FinalResponseTypeDef]

### knowledgeBaseLookupOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseLookupOutputTypeDef]

### repromptResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RepromptResponseTypeDef]

### traceId
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['ACTION_GROUP', 'ASK_USER', 'FINISH', 'KNOWLEDGE_BASE', 'REPROMPT']]


# OrchestrationConfigurationTypeDef

### queryTransformationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.QueryTransformationConfigurationTypeDef'>
- **Required**: Yes


# OrchestrationTraceTypeDef

### invocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationInputTypeDef]

### modelInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ModelInvocationInputTypeDef]

### observation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ObservationTypeDef]

### rationale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RationaleTypeDef]


# OutputFileTypeDef

### bytes
- **Type**: <class 'NoneType'>

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterTypeDef

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# PayloadPartTypeDef

### attribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AttributionTypeDef]

### bytes
- **Type**: <class 'NoneType'>


# PostProcessingModelInvocationOutputTypeDef

### parsedResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PostProcessingParsedResponseTypeDef]

### traceId
- **Type**: typing.Optional[str]


# PostProcessingParsedResponseTypeDef

### text
- **Type**: typing.Optional[str]


# PostProcessingTraceTypeDef

### modelInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ModelInvocationInputTypeDef]

### modelInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PostProcessingModelInvocationOutputTypeDef]


# PreProcessingModelInvocationOutputTypeDef

### parsedResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PreProcessingParsedResponseTypeDef]

### traceId
- **Type**: typing.Optional[str]


# PreProcessingParsedResponseTypeDef

### isValid
- **Type**: typing.Optional[bool]

### rationale
- **Type**: typing.Optional[str]


# PreProcessingTraceTypeDef

### modelInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ModelInvocationInputTypeDef]

### modelInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PreProcessingModelInvocationOutputTypeDef]


# PromptTemplateTypeDef

### textPromptTemplate
- **Type**: typing.Optional[str]


# PropertyParametersTypeDef

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ParameterTypeDef]]


# QueryTransformationConfigurationTypeDef

### type
- **Type**: typing.Literal['QUERY_DECOMPOSITION']
- **Required**: Yes


# RationaleTypeDef

### text
- **Type**: typing.Optional[str]

### traceId
- **Type**: typing.Optional[str]


# RepromptResponseTypeDef

### source
- **Type**: typing.Optional[typing.Literal['ACTION_GROUP', 'KNOWLEDGE_BASE', 'PARSER']]

### text
- **Type**: typing.Optional[str]


# RequestBodyTypeDef

### content
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ParameterTypeDef]]]


# ResourceNotFoundExceptionTypeDef

### message
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

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AccessDeniedExceptionTypeDef]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BadGatewayExceptionTypeDef]

### chunk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PayloadPartTypeDef]

### conflictException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ConflictExceptionTypeDef]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.DependencyFailedExceptionTypeDef]

### files
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FilePartTypeDef]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InternalServerExceptionTypeDef]

### resourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResourceNotFoundExceptionTypeDef]

### returnControl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ReturnControlPayloadTypeDef]

### serviceQuotaExceededException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ServiceQuotaExceededExceptionTypeDef]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ThrottlingExceptionTypeDef]

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TracePartTypeDef]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ValidationExceptionTypeDef]


# RetrievalFilterTypeDef

### andAll
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

### equals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FilterAttributeTypeDef]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FilterAttributeTypeDef]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FilterAttributeTypeDef]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FilterAttributeTypeDef]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FilterAttributeTypeDef]

### listContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FilterAttributeTypeDef]

### notEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FilterAttributeTypeDef]

### notIn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FilterAttributeTypeDef]

### orAll
- **Type**: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

### startsWith
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FilterAttributeTypeDef]

### stringContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FilterAttributeTypeDef]


# RetrievalResultConfluenceLocationTypeDef

### url
- **Type**: typing.Optional[str]


# RetrievalResultContentTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes


# RetrievalResultLocationTypeDef

### type
- **Type**: typing.Literal['CONFLUENCE', 'S3', 'SALESFORCE', 'SHAREPOINT', 'WEB']
- **Required**: Yes

### confluenceLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalResultConfluenceLocationTypeDef]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalResultS3LocationTypeDef]

### salesforceLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalResultSalesforceLocationTypeDef]

### sharePointLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalResultSharePointLocationTypeDef]

### webLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalResultWebLocationTypeDef]


# RetrievalResultS3LocationTypeDef

### uri
- **Type**: typing.Optional[str]


# RetrievalResultSalesforceLocationTypeDef

### url
- **Type**: typing.Optional[str]


# RetrievalResultSharePointLocationTypeDef

### url
- **Type**: typing.Optional[str]


# RetrievalResultWebLocationTypeDef

### url
- **Type**: typing.Optional[str]


# RetrieveAndGenerateConfigurationTypeDef

### type
- **Type**: typing.Literal['EXTERNAL_SOURCES', 'KNOWLEDGE_BASE']
- **Required**: Yes

### externalSourcesConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ExternalSourcesRetrieveAndGenerateConfigurationTypeDef]

### knowledgeBaseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrieveAndGenerateConfigurationTypeDef]


# RetrieveAndGenerateInputTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveAndGenerateOutputTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveAndGenerateRequestRequestTypeDef

### input
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrieveAndGenerateInputTypeDef'>
- **Required**: Yes

### retrieveAndGenerateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrieveAndGenerateConfigurationTypeDef]

### sessionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrieveAndGenerateSessionConfigurationTypeDef]

### sessionId
- **Type**: typing.Optional[str]


# RetrieveAndGenerateResponseTypeDef

### citations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CitationTypeDef]
- **Required**: Yes

### guardrailAction
- **Type**: typing.Literal['INTERVENED', 'NONE']
- **Required**: Yes

### output
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrieveAndGenerateOutputTypeDef'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RetrieveAndGenerateSessionConfigurationTypeDef

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveRequestRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseQueryTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfigurationTypeDef]


# RetrieveRequestRetrievePaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseQueryTypeDef'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfigurationTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PaginatorConfigTypeDef]


# RetrieveResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RetrievedReferenceTypeDef

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalResultContentTypeDef]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalResultLocationTypeDef]

### metadata
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# ReturnControlPayloadTypeDef

### invocationId
- **Type**: typing.Optional[str]

### invocationInputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationInputMemberTypeDef]]


# S3ObjectDocTypeDef

### uri
- **Type**: <class 'str'>
- **Required**: Yes


# S3ObjectFileTypeDef

### uri
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceQuotaExceededExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# SessionStateTypeDef

### files
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InputFileTypeDef]]

### invocationId
- **Type**: typing.Optional[str]

### knowledgeBaseConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseConfigurationTypeDef]]

### promptSessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### returnControlInvocationResults
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationResultMemberTypeDef]]

### sessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# SpanTypeDef

### end
- **Type**: typing.Optional[int]

### start
- **Type**: typing.Optional[int]


# TextInferenceConfigTypeDef

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.Sequence[str]]

### temperature
- **Type**: typing.Optional[float]

### topP
- **Type**: typing.Optional[float]


# TextResponsePartTypeDef

### span
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.SpanTypeDef]

### text
- **Type**: typing.Optional[str]


# ThrottlingExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# TracePartTypeDef

### agentAliasId
- **Type**: typing.Optional[str]

### agentId
- **Type**: typing.Optional[str]

### agentVersion
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TraceTypeDef]


# TraceTypeDef

### failureTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FailureTraceTypeDef]

### guardrailTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailTraceTypeDef]

### orchestrationTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OrchestrationTraceTypeDef]

### postProcessingTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PostProcessingTraceTypeDef]

### preProcessingTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PreProcessingTraceTypeDef]


# ValidationExceptionTypeDef

### message
- **Type**: typing.Optional[str]


