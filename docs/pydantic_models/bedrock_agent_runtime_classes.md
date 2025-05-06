# Bedrock Agent Runtime Classes

# APISchema

### payload
- **Type**: typing.Optional[str]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.S3Identifier]


# AccessDeniedException

### message
- **Type**: typing.Optional[str]


# ActionGroupExecutor

### customControl
- **Type**: typing.Optional[typing.Literal['RETURN_CONTROL']]

### lambda_
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Parameter]]

### requestBody
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RequestBody]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ActionGroupExecutor]

### apiSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.APISchema]

### description
- **Type**: typing.Optional[str]

### functionSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FunctionSchema]

### parentActionGroupSignature
- **Type**: typing.Optional[typing.Literal['AMAZON.CodeInterpreter', 'AMAZON.UserInput', 'ANTHROPIC.Bash', 'ANTHROPIC.Computer', 'ANTHROPIC.TextEditor']]

### parentActionGroupSignatureParams
- **Type**: typing.Optional[typing.Dict[str, str]]


# AgentCollaboratorInputPayload

### returnControlResults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ReturnControlResults]

### text
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['RETURN_CONTROL', 'TEXT']]


# AgentCollaboratorInvocationInput

### agentCollaboratorAliasArn
- **Type**: typing.Optional[str]

### agentCollaboratorName
- **Type**: typing.Optional[str]

### input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.AgentCollaboratorInputPayload]


# AgentCollaboratorInvocationOutput

### agentCollaboratorAliasArn
- **Type**: typing.Optional[str]

### agentCollaboratorName
- **Type**: typing.Optional[str]

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.AgentCollaboratorOutputPayload]


# AgentCollaboratorOutputPayload

### returnControlPayload
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ReturnControlPayload]

### text
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['RETURN_CONTROL', 'TEXT']]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ApiParameter]]

### requestBody
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ApiRequestBody]


# ApiParameter

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# ApiRequestBody

### content
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PropertyParameters]]


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
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ContentBody, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ContentBodyOutput]]]

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ContentBodyOutput]]

### responseState
- **Type**: typing.Optional[typing.Literal['FAILURE', 'REPROMPT']]


# Attribution

### citations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Citation]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PerformanceConfiguration]


# BedrockRerankingConfiguration

### modelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.BedrockRerankingModelConfiguration'>
- **Required**: Yes

### numberOfResults
- **Type**: typing.Optional[int]


# BedrockRerankingModelConfiguration

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# BedrockSessionContentBlock

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ImageBlock]

### text
- **Type**: typing.Optional[str]


# BedrockSessionContentBlockOutput

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ImageBlockOutput]

### text
- **Type**: typing.Optional[str]


# ByteContentDoc

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# ByteContentFile

### data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### mediaType
- **Type**: <class 'str'>
- **Required**: Yes


# Caller

### agentAliasArn
- **Type**: typing.Optional[str]


# Citation

### generatedResponsePart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GeneratedResponsePart]

### retrievedReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievedReference]]


# CitationEvent

### citation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Citation]

### generatedResponsePart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GeneratedResponsePart]

### retrievedReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievedReference]]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.AgentActionGroup]]

### agentCollaboration
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SUPERVISOR', 'SUPERVISOR_ROUTER']]

### agentName
- **Type**: typing.Optional[str]

### collaboratorConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.CollaboratorConfiguration]]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailConfigurationWithArn]

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### knowledgeBases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBase]]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PromptOverrideConfiguration]


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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ImageInput, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ImageInputOutput]]]


# ContentBodyOutput

### body
- **Type**: typing.Optional[str]

### images
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ImageInputOutput]]


# ConversationHistory

### messages
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Message]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSessionRequest

### encryptionKeyArn
- **Type**: typing.Optional[str]

### sessionMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# CustomOrchestrationTrace

### event
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.CustomOrchestrationTraceEvent]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# ExternalSource

### sourceType
- **Type**: typing.Literal['BYTE_CONTENT', 'S3']
- **Required**: Yes

### byteContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ByteContentDoc]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.S3ObjectDoc]


# ExternalSourcesGenerationConfiguration

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailConfiguration]

### inferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InferenceConfig]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PerformanceConfiguration]

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PromptTemplate]


# ExternalSourcesRetrieveAndGenerateConfiguration

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ExternalSource]
- **Required**: Yes

### generationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ExternalSourcesGenerationConfiguration]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.OutputFile]]


# FileSource

### sourceType
- **Type**: typing.Literal['BYTE_CONTENT', 'S3']
- **Required**: Yes

### byteContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ByteContentFile]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.S3ObjectFile]


# FilterAttribute

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Dict[str, typing.Any]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowInputContent'>
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
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowMultiTurnInputContent

### document
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowMultiTurnInputRequestEvent

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowMultiTurnInputContent'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowOutputContent'>
- **Required**: Yes

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### nodeType
- **Type**: typing.Literal['ConditionNode', 'FlowInputNode', 'FlowOutputNode', 'KnowledgeBaseNode', 'LambdaFunctionNode', 'LexNode', 'PromptNode']
- **Required**: Yes


# FlowResponseStream

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.AccessDeniedException]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.BadGatewayException]

### conflictException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ConflictException]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.DependencyFailedException]

### flowCompletionEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowCompletionEvent]

### flowMultiTurnInputRequestEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowMultiTurnInputRequestEvent]

### flowOutputEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowOutputEvent]

### flowTraceEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowTraceEvent]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InternalServerException]

### resourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResourceNotFoundException]

### serviceQuotaExceededException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ServiceQuotaExceededException]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ThrottlingException]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ValidationException]


# FlowTrace

### conditionNodeResultTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowTraceConditionNodeResultEvent]

### nodeInputTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowTraceNodeInputEvent]

### nodeOutputTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowTraceNodeOutputEvent]


# FlowTraceCondition

### conditionName
- **Type**: <class 'str'>
- **Required**: Yes


# FlowTraceConditionNodeResultEvent

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### satisfiedConditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowTraceCondition]
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# FlowTraceEvent

### trace
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowTrace'>
- **Required**: Yes


# FlowTraceNodeInputContent

### document
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowTraceNodeInputEvent

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowTraceNodeInputField]
- **Required**: Yes

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# FlowTraceNodeInputField

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowTraceNodeInputContent'>
- **Required**: Yes

### nodeInputName
- **Type**: <class 'str'>
- **Required**: Yes


# FlowTraceNodeOutputContent

### document
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowTraceNodeOutputEvent

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowTraceNodeOutputField]
- **Required**: Yes

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# FlowTraceNodeOutputField

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowTraceNodeOutputContent'>
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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ParameterDetail]]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FunctionParameter]]


# FunctionParameter

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[typing.Dict[str, typing.Union[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ContentBody, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ContentBodyOutput]]]

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ContentBodyOutput]]

### responseState
- **Type**: typing.Optional[typing.Literal['FAILURE', 'REPROMPT']]


# FunctionSchema

### functions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FunctionDefinition]]


# GenerateQueryRequest

### queryGenerationInput
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.QueryGenerationInput'>
- **Required**: Yes

### transformationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.TransformationConfiguration'>
- **Required**: Yes


# GenerateQueryResponse

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GeneratedQuery]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# GeneratedQuery

### sql
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['REDSHIFT_SQL']]


# GeneratedResponsePart

### textResponsePart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.TextResponsePart]


# GenerationConfiguration

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailConfiguration]

### inferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InferenceConfig]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PerformanceConfiguration]

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PromptTemplate]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PaginatorConfig]


# GetAgentMemoryResponse

### memoryContents
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Memory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationStep'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# GuardrailAssessment

### contentPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailContentPolicyAssessment]

### sensitiveInformationPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailSensitiveInformationPolicyAssessment]

### topicPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailTopicPolicyAssessment]

### wordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailWordPolicyAssessment]


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

### action
- **Type**: typing.Optional[typing.Literal['BLOCKED']]

### confidence
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']]

### type
- **Type**: typing.Optional[typing.Literal['HATE', 'INSULTS', 'MISCONDUCT', 'PROMPT_ATTACK', 'SEXUAL', 'VIOLENCE']]


# GuardrailContentPolicyAssessment

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailContentFilter]]


# GuardrailCustomWord

### action
- **Type**: typing.Optional[typing.Literal['BLOCKED']]

### match
- **Type**: typing.Optional[str]


# GuardrailEvent

### action
- **Type**: typing.Optional[typing.Literal['INTERVENED', 'NONE']]


# GuardrailManagedWord

### action
- **Type**: typing.Optional[typing.Literal['BLOCKED']]

### match
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['PROFANITY']]


# GuardrailPiiEntityFilter

### action
- **Type**: typing.Optional[typing.Literal['ANONYMIZED', 'BLOCKED']]

### match
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['ADDRESS', 'AGE', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CARD_CVV', 'CREDIT_DEBIT_CARD_EXPIRY', 'CREDIT_DEBIT_CARD_NUMBER', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSWORD', 'PHONE', 'PIN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_BANK_ACCOUNT_NUMBER', 'US_BANK_ROUTING_NUMBER', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'US_PASSPORT_NUMBER', 'US_SOCIAL_SECURITY_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailPiiEntityFilter]]

### regexes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailRegexFilter]]


# GuardrailTopic

### action
- **Type**: typing.Optional[typing.Literal['BLOCKED']]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['DENY']]


# GuardrailTopicPolicyAssessment

### topics
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailTopic]]


# GuardrailTrace

### action
- **Type**: typing.Optional[typing.Literal['INTERVENED', 'NONE']]

### inputAssessments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailAssessment]]

### outputAssessments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailAssessment]]

### traceId
- **Type**: typing.Optional[str]


# GuardrailWordPolicyAssessment

### customWords
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailCustomWord]]

### managedWordLists
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailManagedWord]]


# ImageBlock

### format
- **Type**: typing.Literal['gif', 'jpeg', 'png', 'webp']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ImageSource'>
- **Required**: Yes


# ImageBlockOutput

### format
- **Type**: typing.Literal['gif', 'jpeg', 'png', 'webp']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ImageSourceOutput'>
- **Required**: Yes


# ImageInput

### format
- **Type**: typing.Literal['gif', 'jpeg', 'png', 'webp']
- **Required**: Yes

### source
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ImageInputSource, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ImageInputSourceOutput]
- **Required**: Yes


# ImageInputOutput

### format
- **Type**: typing.Literal['gif', 'jpeg', 'png', 'webp']
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ImageInputSourceOutput'>
- **Required**: Yes


# ImageInputSource

### bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]


# ImageInputSourceOutput

### bytes
- **Type**: <class 'NoneType'>


# ImageSource

### bytes
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.S3Location]


# ImageSourceOutput

### bytes
- **Type**: <class 'NoneType'>

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.S3Location]


# ImplicitFilterConfiguration

### metadataAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.MetadataAttributeSchema]
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes


# InferenceConfig

### textInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.TextInferenceConfig]


# InferenceConfiguration

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


# InlineAgentFilePart

### files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.OutputFile]]


# InlineAgentPayloadPart

### attribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Attribution]

### bytes
- **Type**: <class 'NoneType'>


# InlineAgentResponseStream

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.AccessDeniedException]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.BadGatewayException]

### chunk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InlineAgentPayloadPart]

### conflictException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ConflictException]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.DependencyFailedException]

### files
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InlineAgentFilePart]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InternalServerException]

### resourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResourceNotFoundException]

### returnControl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InlineAgentReturnControlPayload]

### serviceQuotaExceededException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ServiceQuotaExceededException]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ThrottlingException]

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InlineAgentTracePart]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ValidationException]


# InlineAgentReturnControlPayload

### invocationId
- **Type**: typing.Optional[str]

### invocationInputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationInputMember]]


# InlineAgentTracePart

### sessionId
- **Type**: typing.Optional[str]

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Trace]


# InlineBedrockModelConfigurations

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PerformanceConfiguration]


# InlineSessionState

### conversationHistory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ConversationHistory]

### files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InputFile]]

### invocationId
- **Type**: typing.Optional[str]

### promptSessionAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### returnControlInvocationResults
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationResultMember, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationResultMemberOutput]]]

### sessionAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# InputFile

### name
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FileSource'>
- **Required**: Yes

### useCase
- **Type**: typing.Literal['CHAT', 'CODE_INTERPRETER']
- **Required**: Yes


# InputPrompt

### textPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.TextPrompt]


# InternalServerException

### message
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# InvocationInput

### actionGroupInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ActionGroupInvocationInput]

### agentCollaboratorInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.AgentCollaboratorInvocationInput]

### codeInterpreterInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.CodeInterpreterInvocationInput]

### invocationType
- **Type**: typing.Optional[typing.Literal['ACTION_GROUP', 'ACTION_GROUP_CODE_INTERPRETER', 'AGENT_COLLABORATOR', 'FINISH', 'KNOWLEDGE_BASE']]

### knowledgeBaseLookupInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseLookupInput]

### traceId
- **Type**: typing.Optional[str]


# InvocationInputMember

### apiInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ApiInvocationInput]

### functionInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FunctionInvocationInput]


# InvocationResultMember

### apiResult
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ApiResult, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ApiResultOutput, NoneType]

### functionResult
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FunctionResult, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FunctionResultOutput, NoneType]


# InvocationResultMemberOutput

### apiResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ApiResultOutput]

### functionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FunctionResultOutput]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationStepPayloadOutput'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# InvocationStepPayload

### contentBlocks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.BedrockSessionContentBlock]]


# InvocationStepPayloadOutput

### contentBlocks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.BedrockSessionContentBlockOutput]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.BedrockModelConfigurations]

### enableTrace
- **Type**: typing.Optional[bool]

### endSession
- **Type**: typing.Optional[bool]

### inputText
- **Type**: typing.Optional[str]

### memoryId
- **Type**: typing.Optional[str]

### sessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.SessionState]

### sourceArn
- **Type**: typing.Optional[str]

### streamingConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.StreamingConfigurations]


# InvokeAgentResponse

### completion
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseStream]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# InvokeFlowRequest

### flowAliasIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### inputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowInput]
- **Required**: Yes

### enableTrace
- **Type**: typing.Optional[bool]

### executionId
- **Type**: typing.Optional[str]

### modelPerformanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ModelPerformanceConfiguration]


# InvokeFlowResponse

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### responseStream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FlowResponseStream]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.AgentActionGroup]]

### agentCollaboration
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SUPERVISOR', 'SUPERVISOR_ROUTER']]

### bedrockModelConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InlineBedrockModelConfigurations]

### collaboratorConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.CollaboratorConfiguration]]

### collaborators
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Collaborator]]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### enableTrace
- **Type**: typing.Optional[bool]

### endSession
- **Type**: typing.Optional[bool]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailConfigurationWithArn]

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### inlineSessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InlineSessionState]

### inputText
- **Type**: typing.Optional[str]

### knowledgeBases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBase]]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PromptOverrideConfiguration]

### streamingConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.StreamingConfigurations]


# InvokeInlineAgentResponse

### completion
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InlineAgentResponseStream]
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# KnowledgeBase

### description
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfiguration]


# KnowledgeBaseConfiguration

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfiguration'>
- **Required**: Yes


# KnowledgeBaseLookupInput

### knowledgeBaseId
- **Type**: typing.Optional[str]

### text
- **Type**: typing.Optional[str]


# KnowledgeBaseLookupOutput

### retrievedReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievedReference]]


# KnowledgeBaseQuery

### text
- **Type**: <class 'str'>
- **Required**: Yes


# KnowledgeBaseRetrievalConfiguration

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseVectorSearchConfiguration'>
- **Required**: Yes


# KnowledgeBaseRetrievalConfigurationPaginator

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseVectorSearchConfigurationPaginator'>
- **Required**: Yes


# KnowledgeBaseRetrievalResult

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalResultContent'>
- **Required**: Yes

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalResultLocation]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GenerationConfiguration]

### orchestrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.OrchestrationConfiguration]

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfiguration]


# KnowledgeBaseVectorSearchConfiguration

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalFilter]

### implicitFilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ImplicitFilterConfiguration]

### numberOfResults
- **Type**: typing.Optional[int]

### overrideSearchType
- **Type**: typing.Optional[typing.Literal['HYBRID', 'SEMANTIC']]

### rerankingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.VectorSearchRerankingConfiguration]


# KnowledgeBaseVectorSearchConfigurationPaginator

### filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalFilterPaginator]

### implicitFilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ImplicitFilterConfiguration]

### numberOfResults
- **Type**: typing.Optional[int]

### overrideSearchType
- **Type**: typing.Optional[typing.Literal['HYBRID', 'SEMANTIC']]

### rerankingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.VectorSearchRerankingConfiguration]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PaginatorConfig]


# ListInvocationStepsResponse

### invocationStepSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationStepSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PaginatorConfig]


# ListInvocationsResponse

### invocationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PaginatorConfig]


# ListSessionsResponse

### sessionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.SessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# Memory

### sessionSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.MemorySessionSummary]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ContentBlock]
- **Required**: Yes

### role
- **Type**: typing.Literal['assistant', 'user']
- **Required**: Yes


# Metadata

### usage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Usage]


# MetadataAttributeSchema

### description
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['BOOLEAN', 'NUMBER', 'STRING', 'STRING_LIST']
- **Required**: Yes


# MetadataConfigurationForReranking

### selectionMode
- **Type**: typing.Literal['ALL', 'SELECTIVE']
- **Required**: Yes

### selectiveModeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankingMetadataSelectiveModeConfiguration]


# ModelInvocationInput

### foundationModel
- **Type**: typing.Optional[str]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InferenceConfigurationOutput]

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
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE_RESPONSE_GENERATION', 'ORCHESTRATION', 'POST_PROCESSING', 'PRE_PROCESSING', 'ROUTING_CLASSIFIER']]


# ModelNotReadyException

### message
- **Type**: typing.Optional[str]


# ModelPerformanceConfiguration

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PerformanceConfiguration]


# Observation

### actionGroupInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ActionGroupInvocationOutput]

### agentCollaboratorInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.AgentCollaboratorInvocationOutput]

### codeInterpreterInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.CodeInterpreterInvocationOutput]

### finalResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FinalResponse]

### knowledgeBaseLookupOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseLookupOutput]

### repromptResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RepromptResponse]

### traceId
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['ACTION_GROUP', 'AGENT_COLLABORATOR', 'ASK_USER', 'FINISH', 'KNOWLEDGE_BASE', 'REPROMPT']]


# OptimizePromptRequest

### input
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InputPrompt'>
- **Required**: Yes

### targetModelId
- **Type**: <class 'str'>
- **Required**: Yes


# OptimizePromptResponse

### optimizedPrompt
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.OptimizedPromptStream]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# OptimizedPrompt

### textPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.TextPrompt]


# OptimizedPromptEvent

### optimizedPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.OptimizedPrompt]


# OptimizedPromptStream

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.AccessDeniedException]

### analyzePromptEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.AnalyzePromptEvent]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.BadGatewayException]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.DependencyFailedException]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InternalServerException]

### optimizedPromptEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.OptimizedPromptEvent]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ThrottlingException]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ValidationException]


# OrchestrationConfiguration

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]

### inferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InferenceConfig]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PerformanceConfiguration]

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PromptTemplate]

### queryTransformationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.QueryTransformationConfiguration]


# OrchestrationModelInvocationOutput

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Metadata]

### rawResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RawResponse]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ReasoningContentBlock]

### traceId
- **Type**: typing.Optional[str]


# OrchestrationTrace

### invocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationInput]

### modelInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ModelInvocationInput]

### modelInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.OrchestrationModelInvocationOutput]

### observation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Observation]

### rationale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Rationale]


# OutputFile

### bytes
- **Type**: <class 'NoneType'>

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Parameter

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# ParameterDetail

### type
- **Type**: typing.Literal['array', 'boolean', 'integer', 'number', 'string']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### required
- **Type**: typing.Optional[bool]


# PayloadPart

### attribution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Attribution]

### bytes
- **Type**: <class 'NoneType'>


# PerformanceConfiguration

### latency
- **Type**: typing.Optional[typing.Literal['optimized', 'standard']]


# PostProcessingModelInvocationOutput

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Metadata]

### parsedResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PostProcessingParsedResponse]

### rawResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RawResponse]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ReasoningContentBlock]

### traceId
- **Type**: typing.Optional[str]


# PostProcessingParsedResponse

### text
- **Type**: typing.Optional[str]


# PostProcessingTrace

### modelInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ModelInvocationInput]

### modelInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PostProcessingModelInvocationOutput]


# PreProcessingModelInvocationOutput

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Metadata]

### parsedResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PreProcessingParsedResponse]

### rawResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RawResponse]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ReasoningContentBlock]

### traceId
- **Type**: typing.Optional[str]


# PreProcessingParsedResponse

### isValid
- **Type**: typing.Optional[bool]

### rationale
- **Type**: typing.Optional[str]


# PreProcessingTrace

### modelInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ModelInvocationInput]

### modelInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PreProcessingModelInvocationOutput]


# PromptConfiguration

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### basePromptTemplate
- **Type**: typing.Optional[str]

### foundationModel
- **Type**: typing.Optional[str]

### inferenceConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InferenceConfiguration, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InferenceConfigurationOutput, NoneType]

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PromptConfiguration]
- **Required**: Yes

### overrideLambda
- **Type**: typing.Optional[str]


# PromptTemplate

### textPromptTemplate
- **Type**: typing.Optional[str]


# PropertyParameters

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Parameter]]


# PutInvocationStepRequest

### invocationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### invocationStepTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### payload
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationStepPayload, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationStepPayloadOutput]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# QueryGenerationInput

### text
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['TEXT']
- **Required**: Yes


# QueryTransformationConfiguration

### type
- **Type**: typing.Literal['QUERY_DECOMPOSITION']
- **Required**: Yes


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ReasoningTextBlock]

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
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Parameter]]]


# RerankDocument

### type
- **Type**: typing.Literal['JSON', 'TEXT']
- **Required**: Yes

### jsonDocument
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### textDocument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankTextDocument]


# RerankDocumentOutput

### type
- **Type**: typing.Literal['JSON', 'TEXT']
- **Required**: Yes

### jsonDocument
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### textDocument
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankTextDocument]


# RerankQuery

### textQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankTextDocument'>
- **Required**: Yes

### type
- **Type**: typing.Literal['TEXT']
- **Required**: Yes


# RerankRequest

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankQuery]
- **Required**: Yes

### rerankingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankingConfiguration'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankSource]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# RerankRequestPaginate

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankQuery]
- **Required**: Yes

### rerankingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankingConfiguration'>
- **Required**: Yes

### sources
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankSource]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PaginatorConfig]


# RerankResponse

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankDocumentOutput]


# RerankSource

### inlineDocumentSource
- **Type**: typing.Union[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankDocument, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RerankDocumentOutput]
- **Required**: Yes

### type
- **Type**: typing.Literal['INLINE']
- **Required**: Yes


# RerankTextDocument

### text
- **Type**: typing.Optional[str]


# RerankingConfiguration

### bedrockRerankingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.BedrockRerankingConfiguration'>
- **Required**: Yes

### type
- **Type**: typing.Literal['BEDROCK_RERANKING_MODEL']
- **Required**: Yes


# RerankingMetadataSelectiveModeConfiguration

### fieldsToExclude
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FieldForReranking]]

### fieldsToInclude
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FieldForReranking]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.AccessDeniedException]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.BadGatewayException]

### chunk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PayloadPart]

### conflictException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ConflictException]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.DependencyFailedException]

### files
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilePart]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InternalServerException]

### modelNotReadyException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ModelNotReadyException]

### resourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResourceNotFoundException]

### returnControl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ReturnControlPayload]

### serviceQuotaExceededException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ServiceQuotaExceededException]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ThrottlingException]

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.TracePart]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ValidationException]


# RetrievalFilter

### andAll
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### equals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### in_
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### listContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### notEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### notIn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### orAll
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### startsWith
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### stringContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]


# RetrievalFilterPaginator

### andAll
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### equals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### greaterThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### greaterThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### in_
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### lessThan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### lessThanOrEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### listContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### notEquals
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### notIn
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### orAll
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### startsWith
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]

### stringContains
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FilterAttribute]


# RetrievalResultConfluenceLocation

### url
- **Type**: typing.Optional[str]


# RetrievalResultContent

### byteContent
- **Type**: typing.Optional[str]

### row
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalResultContentColumn]]

### text
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['IMAGE', 'ROW', 'TEXT']]


# RetrievalResultContentColumn

### columnName
- **Type**: typing.Optional[str]

### columnValue
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['BLOB', 'BOOLEAN', 'DOUBLE', 'LONG', 'NULL', 'STRING']]


# RetrievalResultCustomDocumentLocation

### id
- **Type**: typing.Optional[str]


# RetrievalResultKendraDocumentLocation

### uri
- **Type**: typing.Optional[str]


# RetrievalResultLocation

### type
- **Type**: typing.Literal['CONFLUENCE', 'CUSTOM', 'KENDRA', 'S3', 'SALESFORCE', 'SHAREPOINT', 'SQL', 'WEB']
- **Required**: Yes

### confluenceLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalResultConfluenceLocation]

### customDocumentLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalResultCustomDocumentLocation]

### kendraDocumentLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalResultKendraDocumentLocation]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalResultS3Location]

### salesforceLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalResultSalesforceLocation]

### sharePointLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalResultSharePointLocation]

### sqlLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalResultSqlLocation]

### webLocation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalResultWebLocation]


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


# RetrieveAndGenerateConfiguration

### type
- **Type**: typing.Literal['EXTERNAL_SOURCES', 'KNOWLEDGE_BASE']
- **Required**: Yes

### externalSourcesConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ExternalSourcesRetrieveAndGenerateConfiguration]

### knowledgeBaseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseRetrieveAndGenerateConfiguration]


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


# RetrieveAndGenerateRequest

### input
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrieveAndGenerateInput'>
- **Required**: Yes

### retrieveAndGenerateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrieveAndGenerateConfiguration]

### sessionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrieveAndGenerateSessionConfiguration]

### sessionId
- **Type**: typing.Optional[str]


# RetrieveAndGenerateResponse

### citations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Citation]
- **Required**: Yes

### guardrailAction
- **Type**: typing.Literal['INTERVENED', 'NONE']
- **Required**: Yes

### output
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrieveAndGenerateOutput'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# RetrieveAndGenerateSessionConfiguration

### kmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveAndGenerateStreamRequest

### input
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrieveAndGenerateInput'>
- **Required**: Yes

### retrieveAndGenerateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrieveAndGenerateConfiguration]

### sessionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrieveAndGenerateSessionConfiguration]

### sessionId
- **Type**: typing.Optional[str]


# RetrieveAndGenerateStreamResponse

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### stream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrieveAndGenerateStreamResponseOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# RetrieveAndGenerateStreamResponseOutput

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.AccessDeniedException]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.BadGatewayException]

### citation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.CitationEvent]

### conflictException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ConflictException]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.DependencyFailedException]

### guardrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailEvent]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InternalServerException]

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrieveAndGenerateOutputEvent]

### resourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResourceNotFoundException]

### serviceQuotaExceededException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ServiceQuotaExceededException]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ThrottlingException]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ValidationException]


# RetrieveRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseQuery'>
- **Required**: Yes

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailConfiguration]

### nextToken
- **Type**: typing.Optional[str]

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfiguration]


# RetrieveRequestPaginate

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseQuery'>
- **Required**: Yes

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailConfiguration]

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfigurationPaginator]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PaginatorConfig]


# RetrieveResponse

### guardrailAction
- **Type**: typing.Literal['INTERVENED', 'NONE']
- **Required**: Yes

### retrievalResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalResult]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# RetrievedReference

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalResultContent]

### location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RetrievalResultLocation]

### metadata
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# ReturnControlPayload

### invocationId
- **Type**: typing.Optional[str]

### invocationInputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationInputMember]]


# ReturnControlResults

### invocationId
- **Type**: typing.Optional[str]

### returnControlInvocationResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationResultMemberOutput]]


# RoutingClassifierModelInvocationOutput

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Metadata]

### rawResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RawResponse]

### traceId
- **Type**: typing.Optional[str]


# RoutingClassifierTrace

### invocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationInput]

### modelInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ModelInvocationInput]

### modelInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RoutingClassifierModelInvocationOutput]

### observation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Observation]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ConversationHistory]

### files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InputFile]]

### invocationId
- **Type**: typing.Optional[str]

### knowledgeBaseConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.KnowledgeBaseConfiguration]]

### promptSessionAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### returnControlInvocationResults
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationResultMember, aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.InvocationResultMemberOutput]]]

### sessionAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TextInferenceConfig

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.List[str]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Span]

### text
- **Type**: typing.Optional[str]


# TextToSqlConfiguration

### type
- **Type**: typing.Literal['KNOWLEDGE_BASE']
- **Required**: Yes

### knowledgeBaseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.TextToSqlKnowledgeBaseConfiguration]


# TextToSqlKnowledgeBaseConfiguration

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes


# ThrottlingException

### message
- **Type**: typing.Optional[str]


# Trace

### customOrchestrationTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.CustomOrchestrationTrace]

### failureTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.FailureTrace]

### guardrailTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.GuardrailTrace]

### orchestrationTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.OrchestrationTrace]

### postProcessingTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PostProcessingTrace]

### preProcessingTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.PreProcessingTrace]

### routingClassifierTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.RoutingClassifierTrace]


# TracePart

### agentAliasId
- **Type**: typing.Optional[str]

### agentId
- **Type**: typing.Optional[str]

### agentVersion
- **Type**: typing.Optional[str]

### callerChain
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Caller]]

### collaboratorName
- **Type**: typing.Optional[str]

### eventTime
- **Type**: typing.Optional[datetime.datetime]

### sessionId
- **Type**: typing.Optional[str]

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.Trace]


# TransformationConfiguration

### mode
- **Type**: typing.Literal['TEXT_TO_SQL']
- **Required**: Yes

### textToSqlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.TextToSqlConfiguration]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateSessionRequest

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sessionMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.VectorSearchBedrockRerankingModelConfiguration'>
- **Required**: Yes

### metadataConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.MetadataConfigurationForReranking]

### numberOfRerankedResults
- **Type**: typing.Optional[int]


# VectorSearchBedrockRerankingModelConfiguration

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]]


# VectorSearchRerankingConfiguration

### type
- **Type**: typing.Literal['BEDROCK_RERANKING_MODEL']
- **Required**: Yes

### bedrockRerankingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime.bedrock_agent_runtime_classes.VectorSearchBedrockRerankingConfiguration]


