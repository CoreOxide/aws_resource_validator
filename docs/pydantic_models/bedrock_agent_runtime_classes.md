# Bedrock Agent Runtime Classes

# APISchema

### payload
- **Type**: typing.Optional[str]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.S3Identifier]


# AccessDeniedException

### message
- **Type**: typing.Optional[str]


# ActionGroupExecutor

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionGroupInvocationInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Parameter]]

### requestBody
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RequestBody]

### verb
- **Type**: typing.Optional[str]


# ActionGroupInvocationOutput

### text
- **Type**: typing.Optional[str]


# AgentActionGroup

### actionGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### actionGroupExecutor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ActionGroupExecutor]

### apiSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.APISchema]

### description
- **Type**: typing.Optional[str]

### functionSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionSchema]

### parentActionGroupSignature
- **Type**: typing.Optional[typing.Literal['AMAZON.CodeInterpreter', 'AMAZON.UserInput', 'ANTHROPIC.Bash', 'ANTHROPIC.Computer', 'ANTHROPIC.TextEditor']]

### parentActionGroupSignatureParams
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AgentCollaboratorInvocationInput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AgentCollaboratorInvocationOutput

### agentCollaboratorAliasArn
- **Type**: typing.Optional[str]

### agentCollaboratorName
- **Type**: typing.Optional[str]

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AgentCollaboratorOutputPayload]


# AgentCollaboratorOutputPayload

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalyzePromptEvent

### message
- **Type**: typing.Optional[str]


# ApiInvocationInput

### actionGroup
- **Type**: <class 'str'>
- **Required**: Yes

### actionInvocationType
- **Type**: typing.Optional[typing.Literal['RESULT', 'USER_CONFIRMATION', 'USER_CONFIRMATION_AND_RESULT']]

### agentId
- **Type**: typing.Optional[str]

### apiPath
- **Type**: typing.Optional[str]

### collaboratorName
- **Type**: typing.Optional[str]

### httpMethod
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiParameter]]

### requestBody
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiRequestBody]


# ApiParameter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApiRequestBody

### content
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PropertyParameters]]


# ApiResult

### actionGroup
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: typing.Optional[str]

### apiPath
- **Type**: typing.Optional[str]

### confirmationState
- **Type**: typing.Optional[typing.Literal['CONFIRM', 'DENY']]

### httpMethod
- **Type**: typing.Optional[str]

### httpStatusCode
- **Type**: typing.Optional[int]

### responseBody
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ContentBodyUnion]]

### responseState
- **Type**: typing.Optional[typing.Literal['FAILURE', 'REPROMPT']]


# ApiResultOutput

### actionGroup
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: typing.Optional[str]

### apiPath
- **Type**: typing.Optional[str]

### confirmationState
- **Type**: typing.Optional[typing.Literal['CONFIRM', 'DENY']]

### httpMethod
- **Type**: typing.Optional[str]

### httpStatusCode
- **Type**: typing.Optional[int]

### responseBody
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ContentBodyOutput]]

### responseState
- **Type**: typing.Optional[typing.Literal['FAILURE', 'REPROMPT']]


# ApiResultUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Attribution

### citations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Citation]]


# BadGatewayException

### message
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BedrockModelConfigurations

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PerformanceConfiguration]


# BedrockRerankingConfiguration

### modelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BedrockRerankingModelConfiguration'>
- **Required**: Yes

### numberOfResults
- **Type**: typing.Optional[int]


# BedrockRerankingModelConfiguration

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]


# BedrockSessionContentBlock

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ImageBlock]

### text
- **Type**: typing.Optional[str]


# BedrockSessionContentBlockOutput

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ImageBlockOutput]

### text
- **Type**: typing.Optional[str]


# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ByteContentDoc

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Blob'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# ByteContentFile

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Blob'>
- **Required**: Yes

### mediaType
- **Type**: <class 'str'>
- **Required**: Yes


# Caller

### agentAliasArn
- **Type**: typing.Optional[str]


# Citation

### generatedResponsePart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GeneratedResponsePart]

### retrievedReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievedReference]]


# CitationEvent

### citation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Citation]

### generatedResponsePart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GeneratedResponsePart]

### retrievedReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievedReference]]


# CodeInterpreterInvocationInput

### code
- **Type**: typing.Optional[str]

### files
- **Type**: typing.Optional[typing.List[str]]


# CodeInterpreterInvocationOutput

### executionError
- **Type**: typing.Optional[str]

### executionOutput
- **Type**: typing.Optional[str]

### executionTimeout
- **Type**: typing.Optional[bool]

### files
- **Type**: typing.Optional[typing.List[str]]


# Collaborator

### foundationModel
- **Type**: <class 'str'>
- **Required**: Yes

### instruction
- **Type**: <class 'str'>
- **Required**: Yes

### actionGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AgentActionGroup]]

### agentCollaboration
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SUPERVISOR', 'SUPERVISOR_ROUTER']]

### agentName
- **Type**: typing.Optional[str]

### collaboratorConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CollaboratorConfiguration]]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailConfigurationWithArn]

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### knowledgeBases
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBase]]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PromptOverrideConfiguration]


# CollaboratorConfiguration

### collaboratorInstruction
- **Type**: <class 'str'>
- **Required**: Yes

### collaboratorName
- **Type**: <class 'str'>
- **Required**: Yes

### agentAliasArn
- **Type**: typing.Optional[str]

### relayConversationHistory
- **Type**: typing.Optional[typing.Literal['DISABLED', 'TO_COLLABORATOR']]


# ConflictException

### message
- **Type**: typing.Optional[str]


# ContentBlock

### text
- **Type**: typing.Optional[str]


# ContentBody

### body
- **Type**: typing.Optional[str]

### images
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ImageInputUnion]]


# ContentBodyOutput

### body
- **Type**: typing.Optional[str]

### images
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ImageInputOutput]]


# ContentBodyUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConversationHistory

### messages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Message]]


# CreateInvocationRequest

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### invocationId
- **Type**: typing.Optional[str]


# CreateInvocationResponse

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### invocationId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSessionRequest

### encryptionKeyArn
- **Type**: typing.Optional[str]

### sessionMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSessionResponse

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionStatus
- **Type**: typing.Literal['ACTIVE', 'ENDED', 'EXPIRED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# CustomOrchestrationTrace

### event
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CustomOrchestrationTraceEvent]

### traceId
- **Type**: typing.Optional[str]


# CustomOrchestrationTraceEvent

### text
- **Type**: typing.Optional[str]


# DeleteAgentMemoryRequest

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### memoryId
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]


# DeleteSessionRequest

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DependencyFailedException

### message
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]


# EndSessionRequest

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# EndSessionResponse

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionStatus
- **Type**: typing.Literal['ACTIVE', 'ENDED', 'EXPIRED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# ExternalSource

### sourceType
- **Type**: typing.Literal['BYTE_CONTENT', 'S3']
- **Required**: Yes

### byteContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ByteContentDoc]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.S3ObjectDoc]


# ExternalSourcesGenerationConfiguration

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailConfiguration]

### inferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InferenceConfig]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PerformanceConfiguration]

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PromptTemplate]


# ExternalSourcesRetrieveAndGenerateConfiguration

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ExternalSource]
- **Required**: Yes

### generationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ExternalSourcesGenerationConfiguration]


# FailureTrace

### failureReason
- **Type**: typing.Optional[str]

### traceId
- **Type**: typing.Optional[str]


# FieldForReranking

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes


# FilePart

### files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OutputFile]]


# FileSource

### sourceType
- **Type**: typing.Literal['BYTE_CONTENT', 'S3']
- **Required**: Yes

### byteContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ByteContentFile]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.S3ObjectFile]


# FilterAttribute

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# FinalResponse

### text
- **Type**: typing.Optional[str]


# FlowCompletionEvent

### completionReason
- **Type**: typing.Literal['INPUT_REQUIRED', 'SUCCESS']
- **Required**: Yes


# FlowInput

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowInputContent'>
- **Required**: Yes

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### nodeInputName
- **Type**: typing.Optional[str]

### nodeOutputName
- **Type**: typing.Optional[str]


# FlowInputContent

### document
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# FlowMultiTurnInputContent

### document
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowMultiTurnInputRequestEvent

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowMultiTurnInputContent'>
- **Required**: Yes

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### nodeType
- **Type**: typing.Literal['ConditionNode', 'FlowInputNode', 'FlowOutputNode', 'KnowledgeBaseNode', 'LambdaFunctionNode', 'LexNode', 'PromptNode']
- **Required**: Yes


# FlowOutputContent

### document
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowOutputEvent

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowOutputContent'>
- **Required**: Yes

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### nodeType
- **Type**: typing.Literal['ConditionNode', 'FlowInputNode', 'FlowOutputNode', 'KnowledgeBaseNode', 'LambdaFunctionNode', 'LexNode', 'PromptNode']
- **Required**: Yes


# FlowResponseStream

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AccessDeniedException]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BadGatewayException]

### conflictException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ConflictException]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.DependencyFailedException]

### flowCompletionEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowCompletionEvent]

### flowMultiTurnInputRequestEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowMultiTurnInputRequestEvent]

### flowOutputEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowOutputEvent]

### flowTraceEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceEvent]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InternalServerException]

### resourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResourceNotFoundException]

### serviceQuotaExceededException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ServiceQuotaExceededException]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ThrottlingException]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ValidationException]


# FlowTrace

### conditionNodeResultTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceConditionNodeResultEvent]

### nodeInputTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceNodeInputEvent]

### nodeOutputTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceNodeOutputEvent]


# FlowTraceCondition

### conditionName
- **Type**: <class 'str'>
- **Required**: Yes


# FlowTraceConditionNodeResultEvent

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### satisfiedConditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceCondition]
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# FlowTraceEvent

### trace
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTrace'>
- **Required**: Yes


# FlowTraceNodeInputContent

### document
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowTraceNodeInputEvent

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceNodeInputField]
- **Required**: Yes

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# FlowTraceNodeInputField

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceNodeInputContent'>
- **Required**: Yes

### nodeInputName
- **Type**: <class 'str'>
- **Required**: Yes


# FlowTraceNodeOutputContent

### document
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowTraceNodeOutputEvent

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceNodeOutputField]
- **Required**: Yes

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# FlowTraceNodeOutputField

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceNodeOutputContent'>
- **Required**: Yes

### nodeOutputName
- **Type**: <class 'str'>
- **Required**: Yes


# FunctionDefinition

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ParameterDetail]]

### requireConfirmation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FunctionInvocationInput

### actionGroup
- **Type**: <class 'str'>
- **Required**: Yes

### actionInvocationType
- **Type**: typing.Optional[typing.Literal['RESULT', 'USER_CONFIRMATION', 'USER_CONFIRMATION_AND_RESULT']]

### agentId
- **Type**: typing.Optional[str]

### collaboratorName
- **Type**: typing.Optional[str]

### function
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionParameter]]


# FunctionParameter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionResult

### actionGroup
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: typing.Optional[str]

### confirmationState
- **Type**: typing.Optional[typing.Literal['CONFIRM', 'DENY']]

### function
- **Type**: typing.Optional[str]

### responseBody
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ContentBodyUnion]]

### responseState
- **Type**: typing.Optional[typing.Literal['FAILURE', 'REPROMPT']]


# FunctionResultOutput

### actionGroup
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: typing.Optional[str]

### confirmationState
- **Type**: typing.Optional[typing.Literal['CONFIRM', 'DENY']]

### function
- **Type**: typing.Optional[str]

### responseBody
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ContentBodyOutput]]

### responseState
- **Type**: typing.Optional[typing.Literal['FAILURE', 'REPROMPT']]


# FunctionResultUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionSchema

### functions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionDefinition]]


# GenerateQueryRequest

### queryGenerationInput
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.QueryGenerationInput'>
- **Required**: Yes

### transformationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TransformationConfiguration'>
- **Required**: Yes


# GenerateQueryResponse

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GeneratedQuery]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# GeneratedQuery

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GeneratedResponsePart

### textResponsePart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TextResponsePart]


# GenerationConfiguration

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailConfiguration]

### inferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InferenceConfig]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PerformanceConfiguration]

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PromptTemplate]


# GetAgentMemoryRequest

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


# GetAgentMemoryRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PaginatorConfig]


# GetAgentMemoryResponse

### memoryContents
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Memory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetInvocationStepRequest

### invocationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### invocationStepId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetInvocationStepResponse

### invocationStep
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationStep'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# GetSessionRequest

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionResponse

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### encryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionMetadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### sessionStatus
- **Type**: typing.Literal['ACTIVE', 'ENDED', 'EXPIRED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# GuardrailAssessment

### contentPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailContentPolicyAssessment]

### sensitiveInformationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailSensitiveInformationPolicyAssessment]

### topicPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailTopicPolicyAssessment]

### wordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailWordPolicyAssessment]


# GuardrailConfiguration

### guardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GuardrailConfigurationWithArn

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GuardrailContentFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailContentPolicyAssessment

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailContentFilter]]


# GuardrailCustomWord

### action
- **Type**: typing.Optional[typing.Literal['BLOCKED']]

### match
- **Type**: typing.Optional[str]


# GuardrailEvent

### action
- **Type**: typing.Optional[typing.Literal['INTERVENED', 'NONE']]


# GuardrailManagedWord

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailPiiEntityFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailRegexFilter

### action
- **Type**: typing.Optional[typing.Literal['ANONYMIZED', 'BLOCKED']]

### match
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### regex
- **Type**: typing.Optional[str]


# GuardrailSensitiveInformationPolicyAssessment

### piiEntities
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailPiiEntityFilter]]

### regexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailRegexFilter]]


# GuardrailTopic

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailTopicPolicyAssessment

### topics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailTopic]]


# GuardrailTrace

### action
- **Type**: typing.Optional[typing.Literal['INTERVENED', 'NONE']]

### inputAssessments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailAssessment]]

### outputAssessments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailAssessment]]

### traceId
- **Type**: typing.Optional[str]


# GuardrailWordPolicyAssessment

### customWords
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailCustomWord]]

### managedWordLists
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailManagedWord]]


# ImageBlock

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageBlockOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageInputOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageInputUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImplicitFilterConfiguration

### metadataAttributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.MetadataAttributeSchema]
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes


# InferenceConfig

### textInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TextInferenceConfig]


# InferenceConfiguration

### maximumLength
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.Sequence[str]]

### temperature
- **Type**: typing.Optional[float]

### topK
- **Type**: typing.Optional[int]

### topP
- **Type**: typing.Optional[float]


# InferenceConfigurationOutput

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


# InferenceConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InlineAgentFilePart

### files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OutputFile]]


# InlineAgentPayloadPart

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InlineAgentResponseStream

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AccessDeniedException]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BadGatewayException]

### chunk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineAgentPayloadPart]

### conflictException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ConflictException]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.DependencyFailedException]

### files
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineAgentFilePart]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InternalServerException]

### resourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResourceNotFoundException]

### returnControl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineAgentReturnControlPayload]

### serviceQuotaExceededException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ServiceQuotaExceededException]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ThrottlingException]

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineAgentTracePart]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ValidationException]


# InlineAgentReturnControlPayload

### invocationId
- **Type**: typing.Optional[str]

### invocationInputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationInputMember]]


# InlineAgentTracePart

### sessionId
- **Type**: typing.Optional[str]

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Trace]


# InlineBedrockModelConfigurations

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PerformanceConfiguration]


# InlineSessionState

### conversationHistory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ConversationHistory]

### files
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InputFile]]

### invocationId
- **Type**: typing.Optional[str]

### promptSessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### returnControlInvocationResults
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationResultMemberUnion]]

### sessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# InputFile

### name
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FileSource'>
- **Required**: Yes

### useCase
- **Type**: typing.Literal['CHAT', 'CODE_INTERPRETER']
- **Required**: Yes


# InputPrompt

### textPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TextPrompt]


# InternalServerException

### message
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# InvocationInput

### actionGroupInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ActionGroupInvocationInput]

### agentCollaboratorInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AgentCollaboratorInvocationInput]

### codeInterpreterInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CodeInterpreterInvocationInput]

### invocationType
- **Type**: typing.Optional[typing.Literal['ACTION_GROUP', 'ACTION_GROUP_CODE_INTERPRETER', 'AGENT_COLLABORATOR', 'FINISH', 'KNOWLEDGE_BASE']]

### knowledgeBaseLookupInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseLookupInput]

### traceId
- **Type**: typing.Optional[str]


# InvocationInputMember

### apiInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiInvocationInput]

### functionInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionInvocationInput]


# InvocationResultMember

### apiResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiResultUnion]

### functionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionResultUnion]


# InvocationResultMemberOutput

### apiResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiResultOutput]

### functionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionResultOutput]


# InvocationResultMemberUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InvocationStep

### invocationId
- **Type**: <class 'str'>
- **Required**: Yes

### invocationStepId
- **Type**: <class 'str'>
- **Required**: Yes

### invocationStepTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationStepPayloadOutput'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# InvocationStepPayload

### contentBlocks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BedrockSessionContentBlock]]


# InvocationStepPayloadOutput

### contentBlocks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BedrockSessionContentBlockOutput]]


# InvocationStepPayloadUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InvocationStepSummary

### invocationId
- **Type**: <class 'str'>
- **Required**: Yes

### invocationStepId
- **Type**: <class 'str'>
- **Required**: Yes

### invocationStepTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# InvocationSummary

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### invocationId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# InvokeAgentRequest

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### bedrockModelConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BedrockModelConfigurations]

### enableTrace
- **Type**: typing.Optional[bool]

### endSession
- **Type**: typing.Optional[bool]

### inputText
- **Type**: typing.Optional[str]

### memoryId
- **Type**: typing.Optional[str]

### sessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.SessionState]

### sourceArn
- **Type**: typing.Optional[str]

### streamingConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.StreamingConfigurations]


# InvokeAgentResponse

### completion
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseStream]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# InvokeFlowRequest

### flowAliasIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### inputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowInput]
- **Required**: Yes

### enableTrace
- **Type**: typing.Optional[bool]

### executionId
- **Type**: typing.Optional[str]

### modelPerformanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ModelPerformanceConfiguration]


# InvokeFlowResponse

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### responseStream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowResponseStream]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# InvokeInlineAgentRequest

### foundationModel
- **Type**: <class 'str'>
- **Required**: Yes

### instruction
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### actionGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AgentActionGroup]]

### agentCollaboration
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SUPERVISOR', 'SUPERVISOR_ROUTER']]

### bedrockModelConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineBedrockModelConfigurations]

### collaboratorConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CollaboratorConfiguration]]

### collaborators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Collaborator]]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### enableTrace
- **Type**: typing.Optional[bool]

### endSession
- **Type**: typing.Optional[bool]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailConfigurationWithArn]

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### inlineSessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineSessionState]

### inputText
- **Type**: typing.Optional[str]

### knowledgeBases
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBase]]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PromptOverrideConfiguration]

### streamingConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.StreamingConfigurations]


# InvokeInlineAgentResponse

### completion
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineAgentResponseStream]
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# KnowledgeBase

### description
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfiguration]


# KnowledgeBaseConfiguration

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfiguration'>
- **Required**: Yes


# KnowledgeBaseLookupInput

### knowledgeBaseId
- **Type**: typing.Optional[str]

### text
- **Type**: typing.Optional[str]


# KnowledgeBaseLookupOutput

### retrievedReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievedReference]]


# KnowledgeBaseQuery

### text
- **Type**: <class 'str'>
- **Required**: Yes


# KnowledgeBaseRetrievalConfiguration

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseVectorSearchConfiguration'>
- **Required**: Yes


# KnowledgeBaseRetrievalConfigurationPaginator

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseVectorSearchConfigurationPaginator'>
- **Required**: Yes


# KnowledgeBaseRetrievalResult

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalResultContent'>
- **Required**: Yes

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalResultLocation]

### metadata
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

### score
- **Type**: typing.Optional[float]


# KnowledgeBaseRetrieveAndGenerateConfiguration

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### generationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GenerationConfiguration]

### orchestrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OrchestrationConfiguration]

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfiguration]


# KnowledgeBaseVectorSearchConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KnowledgeBaseVectorSearchConfigurationPaginator

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListInvocationStepsRequest

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### invocationIdentifier
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInvocationStepsRequestPaginate

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### invocationIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PaginatorConfig]


# ListInvocationStepsResponse

### invocationStepSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationStepSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInvocationsRequest

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInvocationsRequestPaginate

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PaginatorConfig]


# ListInvocationsResponse

### invocationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSessionsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSessionsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PaginatorConfig]


# ListSessionsResponse

### sessionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.SessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# Memory

### sessionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.MemorySessionSummary]


# MemorySessionSummary

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


# Message

### content
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ContentBlock]
- **Required**: Yes

### role
- **Type**: typing.Literal['assistant', 'user']
- **Required**: Yes


# Metadata

### usage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Usage]


# MetadataAttributeSchema

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetadataConfigurationForReranking

### selectionMode
- **Type**: typing.Literal['ALL', 'SELECTIVE']
- **Required**: Yes

### selectiveModeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankingMetadataSelectiveModeConfiguration]


# ModelInvocationInput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelNotReadyException

### message
- **Type**: typing.Optional[str]


# ModelPerformanceConfiguration

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PerformanceConfiguration]


# Observation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OptimizePromptResponse

### optimizedPrompt
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OptimizedPromptStream]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# OptimizedPrompt

### textPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TextPrompt]


# OptimizedPromptEvent

### optimizedPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OptimizedPrompt]


# OptimizedPromptStream

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AccessDeniedException]

### analyzePromptEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AnalyzePromptEvent]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BadGatewayException]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.DependencyFailedException]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InternalServerException]

### optimizedPromptEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OptimizedPromptEvent]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ThrottlingException]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ValidationException]


# OrchestrationConfiguration

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]

### inferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InferenceConfig]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PerformanceConfiguration]

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PromptTemplate]

### queryTransformationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.QueryTransformationConfiguration]


# OrchestrationModelInvocationOutput

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Metadata]

### rawResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RawResponse]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ReasoningContentBlock]

### traceId
- **Type**: typing.Optional[str]


# OrchestrationTrace

### invocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationInput]

### modelInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ModelInvocationInput]

### modelInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OrchestrationModelInvocationOutput]

### observation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Observation]

### rationale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Rationale]


# OutputFile

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Parameter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PayloadPart

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PerformanceConfiguration

### latency
- **Type**: typing.Optional[typing.Literal['optimized', 'standard']]


# PostProcessingModelInvocationOutput

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Metadata]

### parsedResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PostProcessingParsedResponse]

### rawResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RawResponse]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ReasoningContentBlock]

### traceId
- **Type**: typing.Optional[str]


# PostProcessingParsedResponse

### text
- **Type**: typing.Optional[str]


# PostProcessingTrace

### modelInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ModelInvocationInput]

### modelInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PostProcessingModelInvocationOutput]


# PreProcessingModelInvocationOutput

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Metadata]

### parsedResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PreProcessingParsedResponse]

### rawResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RawResponse]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ReasoningContentBlock]

### traceId
- **Type**: typing.Optional[str]


# PreProcessingParsedResponse

### isValid
- **Type**: typing.Optional[bool]

### rationale
- **Type**: typing.Optional[str]


# PreProcessingTrace

### modelInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ModelInvocationInput]

### modelInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PreProcessingModelInvocationOutput]


# PromptConfiguration

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### basePromptTemplate
- **Type**: typing.Optional[str]

### foundationModel
- **Type**: typing.Optional[str]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InferenceConfigurationUnion]

### parserMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### promptCreationMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### promptState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### promptType
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE_RESPONSE_GENERATION', 'ORCHESTRATION', 'POST_PROCESSING', 'PRE_PROCESSING', 'ROUTING_CLASSIFIER']]


# PromptOverrideConfiguration

### promptConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PromptConfiguration]
- **Required**: Yes

### overrideLambda
- **Type**: typing.Optional[str]


# PromptTemplate

### textPromptTemplate
- **Type**: typing.Optional[str]


# PropertyParameters

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Parameter]]


# PutInvocationStepRequest

### invocationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### invocationStepTime
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Timestamp'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationStepPayloadUnion'>
- **Required**: Yes

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### invocationStepId
- **Type**: typing.Optional[str]


# PutInvocationStepResponse

### invocationStepId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# QueryGenerationInput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueryTransformationConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Rationale

### text
- **Type**: typing.Optional[str]

### traceId
- **Type**: typing.Optional[str]


# RawResponse

### content
- **Type**: typing.Optional[str]


# ReasoningContentBlock

### reasoningText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ReasoningTextBlock]

### redactedContent
- **Type**: typing.Optional[bytes]


# ReasoningTextBlock

### text
- **Type**: <class 'str'>
- **Required**: Yes

### signature
- **Type**: typing.Optional[str]


# RepromptResponse

### source
- **Type**: typing.Optional[typing.Literal['ACTION_GROUP', 'KNOWLEDGE_BASE', 'PARSER']]

### text
- **Type**: typing.Optional[str]


# RequestBody

### content
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Parameter]]]


# RerankDocumentOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RerankQuery

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RerankRequest

### queries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankQuery]
- **Required**: Yes

### rerankingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankingConfiguration'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankSource]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# RerankRequestPaginate

### queries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankQuery]
- **Required**: Yes

### rerankingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankingConfiguration'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankSource]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PaginatorConfig]


# RerankResponse

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# RerankResult

### index
- **Type**: <class 'int'>
- **Required**: Yes

### relevanceScore
- **Type**: <class 'float'>
- **Required**: Yes

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankDocumentOutput]


# RerankSource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RerankTextDocument

### text
- **Type**: typing.Optional[str]


# RerankingConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RerankingMetadataSelectiveModeConfiguration

### fieldsToExclude
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FieldForReranking]]

### fieldsToInclude
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FieldForReranking]]


# ResourceNotFoundException

### message
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

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AccessDeniedException]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BadGatewayException]

### chunk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PayloadPart]

### conflictException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ConflictException]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.DependencyFailedException]

### files
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FilePart]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InternalServerException]

### modelNotReadyException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ModelNotReadyException]

### resourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResourceNotFoundException]

### returnControl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ReturnControlPayload]

### serviceQuotaExceededException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ServiceQuotaExceededException]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ThrottlingException]

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TracePart]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ValidationException]


# RetrievalResultConfluenceLocation

### url
- **Type**: typing.Optional[str]


# RetrievalResultContent

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RetrievalResultKendraDocumentLocation

### uri
- **Type**: typing.Optional[str]


# RetrievalResultLocation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RetrievalResultS3Location

### uri
- **Type**: typing.Optional[str]


# RetrievalResultSalesforceLocation

### url
- **Type**: typing.Optional[str]


# RetrievalResultSharePointLocation

### url
- **Type**: typing.Optional[str]


# RetrievalResultSqlLocation

### query
- **Type**: typing.Optional[str]


# RetrievalResultWebLocation

### url
- **Type**: typing.Optional[str]


# RetrieveAndGenerateInput

### text
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveAndGenerateOutput

### text
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveAndGenerateOutputEvent

### text
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveAndGenerateResponse

### citations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Citation]
- **Required**: Yes

### guardrailAction
- **Type**: typing.Literal['INTERVENED', 'NONE']
- **Required**: Yes

### output
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrieveAndGenerateOutput'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# RetrieveAndGenerateSessionConfiguration

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveAndGenerateStreamResponse

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### stream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrieveAndGenerateStreamResponseOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# RetrieveAndGenerateStreamResponseOutput

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AccessDeniedException]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BadGatewayException]

### citation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CitationEvent]

### conflictException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ConflictException]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.DependencyFailedException]

### guardrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailEvent]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InternalServerException]

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrieveAndGenerateOutputEvent]

### resourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResourceNotFoundException]

### serviceQuotaExceededException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ServiceQuotaExceededException]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ThrottlingException]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ValidationException]


# RetrieveRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseQuery'>
- **Required**: Yes

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailConfiguration]

### nextToken
- **Type**: typing.Optional[str]

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfiguration]


# RetrieveRequestPaginate

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseQuery'>
- **Required**: Yes

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailConfiguration]

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfigurationPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PaginatorConfig]


# RetrieveResponse

### guardrailAction
- **Type**: typing.Literal['INTERVENED', 'NONE']
- **Required**: Yes

### retrievalResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# RetrievedReference

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalResultContent]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievalResultLocation]

### metadata
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# ReturnControlPayload

### invocationId
- **Type**: typing.Optional[str]

### invocationInputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationInputMember]]


# ReturnControlResults

### invocationId
- **Type**: typing.Optional[str]

### returnControlInvocationResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationResultMemberOutput]]


# RoutingClassifierModelInvocationOutput

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Metadata]

### rawResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RawResponse]

### traceId
- **Type**: typing.Optional[str]


# RoutingClassifierTrace

### invocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationInput]

### modelInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ModelInvocationInput]

### modelInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RoutingClassifierModelInvocationOutput]

### observation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Observation]


# S3Identifier

### s3BucketName
- **Type**: typing.Optional[str]

### s3ObjectKey
- **Type**: typing.Optional[str]


# S3Location

### uri
- **Type**: <class 'str'>
- **Required**: Yes


# S3ObjectDoc

### uri
- **Type**: <class 'str'>
- **Required**: Yes


# S3ObjectFile

### uri
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceQuotaExceededException

### message
- **Type**: typing.Optional[str]


# SessionState

### conversationHistory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ConversationHistory]

### files
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InputFile]]

### invocationId
- **Type**: typing.Optional[str]

### knowledgeBaseConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseConfiguration]]

### promptSessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### returnControlInvocationResults
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationResultMemberUnion]]

### sessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# SessionSummary

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionStatus
- **Type**: typing.Literal['ACTIVE', 'ENDED', 'EXPIRED']
- **Required**: Yes


# Span

### end
- **Type**: typing.Optional[int]

### start
- **Type**: typing.Optional[int]


# StreamingConfigurations

### applyGuardrailInterval
- **Type**: typing.Optional[int]

### streamFinalResponse
- **Type**: typing.Optional[bool]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TextInferenceConfig

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.Sequence[str]]

### temperature
- **Type**: typing.Optional[float]

### topP
- **Type**: typing.Optional[float]


# TextPrompt

### text
- **Type**: <class 'str'>
- **Required**: Yes


# TextResponsePart

### span
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Span]

### text
- **Type**: typing.Optional[str]


# TextToSqlConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TextToSqlKnowledgeBaseConfiguration

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes


# ThrottlingException

### message
- **Type**: typing.Optional[str]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Trace

### customOrchestrationTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CustomOrchestrationTrace]

### failureTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FailureTrace]

### guardrailTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailTrace]

### orchestrationTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OrchestrationTrace]

### postProcessingTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PostProcessingTrace]

### preProcessingTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PreProcessingTrace]

### routingClassifierTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RoutingClassifierTrace]


# TracePart

### agentAliasId
- **Type**: typing.Optional[str]

### agentId
- **Type**: typing.Optional[str]

### agentVersion
- **Type**: typing.Optional[str]

### callerChain
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Caller]]

### collaboratorName
- **Type**: typing.Optional[str]

### eventTime
- **Type**: typing.Optional[datetime.datetime]

### sessionId
- **Type**: typing.Optional[str]

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.Trace]


# TransformationConfiguration

### mode
- **Type**: typing.Literal['TEXT_TO_SQL']
- **Required**: Yes

### textToSqlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TextToSqlConfiguration]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateSessionRequest

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sessionMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateSessionResponse

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionStatus
- **Type**: typing.Literal['ACTIVE', 'ENDED', 'EXPIRED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# Usage

### inputTokens
- **Type**: typing.Optional[int]

### outputTokens
- **Type**: typing.Optional[int]


# ValidationException

### message
- **Type**: typing.Optional[str]


# VectorSearchBedrockRerankingConfiguration

### modelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.VectorSearchBedrockRerankingModelConfiguration'>
- **Required**: Yes

### metadataConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.MetadataConfigurationForReranking]

### numberOfRerankedResults
- **Type**: typing.Optional[int]


# VectorSearchBedrockRerankingModelConfiguration

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]


