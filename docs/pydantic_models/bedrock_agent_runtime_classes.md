# Bedrock Agent Runtime Classes

# APISchemaTypeDef

### payload
- **Type**: typing.Optional[str]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.S3IdentifierTypeDef]


# AccessDeniedExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# ActionGroupExecutorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# AgentActionGroupTypeDef

### actionGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### actionGroupExecutor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ActionGroupExecutorTypeDef]

### apiSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.APISchemaTypeDef]

### description
- **Type**: typing.Optional[str]

### functionSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionSchemaTypeDef]

### parentActionGroupSignature
- **Type**: typing.Optional[typing.Literal['AMAZON.CodeInterpreter', 'AMAZON.UserInput', 'ANTHROPIC.Bash', 'ANTHROPIC.Computer', 'ANTHROPIC.TextEditor']]

### parentActionGroupSignatureParams
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AgentCollaboratorInvocationInputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AgentCollaboratorInvocationOutputTypeDef

### agentCollaboratorAliasArn
- **Type**: typing.Optional[str]

### agentCollaboratorName
- **Type**: typing.Optional[str]

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AgentCollaboratorOutputPayloadTypeDef]


# AgentCollaboratorOutputPayloadTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AnalyzePromptEventTypeDef

### message
- **Type**: typing.Optional[str]


# ApiInvocationInputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiParameterTypeDef]]

### requestBody
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiRequestBodyTypeDef]


# ApiParameterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ApiRequestBodyTypeDef

### content
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PropertyParametersTypeDef]]


# ApiResultOutputTypeDef

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ContentBodyOutputTypeDef]]

### responseState
- **Type**: typing.Optional[typing.Literal['FAILURE', 'REPROMPT']]


# ApiResultTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ContentBodyUnionTypeDef]]

### responseState
- **Type**: typing.Optional[typing.Literal['FAILURE', 'REPROMPT']]


# ApiResultUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

# BedrockModelConfigurationsTypeDef

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PerformanceConfigurationTypeDef]


# BedrockRerankingConfigurationTypeDef

### modelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BedrockRerankingModelConfigurationTypeDef'>
- **Required**: Yes

### numberOfResults
- **Type**: typing.Optional[int]


# BedrockRerankingModelConfigurationTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]


# BedrockSessionContentBlockOutputTypeDef

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ImageBlockOutputTypeDef]

### text
- **Type**: typing.Optional[str]


# BedrockSessionContentBlockTypeDef

### image
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ImageBlockTypeDef]

### text
- **Type**: typing.Optional[str]


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ByteContentDocTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BlobTypeDef'>
- **Required**: Yes

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# ByteContentFileTypeDef

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BlobTypeDef'>
- **Required**: Yes

### mediaType
- **Type**: <class 'str'>
- **Required**: Yes


# CallerTypeDef

### agentAliasArn
- **Type**: typing.Optional[str]


# CitationEventTypeDef

### citation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CitationTypeDef]

### generatedResponsePart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GeneratedResponsePartTypeDef]

### retrievedReferences
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrievedReferenceTypeDef]]


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


# CollaboratorConfigurationTypeDef

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


# CollaboratorTypeDef

### foundationModel
- **Type**: <class 'str'>
- **Required**: Yes

### instruction
- **Type**: <class 'str'>
- **Required**: Yes

### actionGroups
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AgentActionGroupTypeDef]]

### agentCollaboration
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SUPERVISOR', 'SUPERVISOR_ROUTER']]

### agentName
- **Type**: typing.Optional[str]

### collaboratorConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CollaboratorConfigurationTypeDef]]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailConfigurationWithArnTypeDef]

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### knowledgeBases
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseTypeDef]]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PromptOverrideConfigurationTypeDef]


# ConflictExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# ContentBlockTypeDef

### text
- **Type**: typing.Optional[str]


# ContentBodyOutputTypeDef

### body
- **Type**: typing.Optional[str]

### images
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ImageInputOutputTypeDef]]


# ContentBodyTypeDef

### body
- **Type**: typing.Optional[str]

### images
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ImageInputUnionTypeDef]]


# ContentBodyUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConversationHistoryTypeDef

### messages
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.MessageTypeDef]]


# CreateInvocationRequestTypeDef

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### invocationId
- **Type**: typing.Optional[str]


# CreateInvocationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSessionRequestTypeDef

### encryptionKeyArn
- **Type**: typing.Optional[str]

### sessionMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSessionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomOrchestrationTraceEventTypeDef

### text
- **Type**: typing.Optional[str]


# CustomOrchestrationTraceTypeDef

### event
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CustomOrchestrationTraceEventTypeDef]

### traceId
- **Type**: typing.Optional[str]


# DeleteAgentMemoryRequestTypeDef

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


# DeleteSessionRequestTypeDef

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DependencyFailedExceptionTypeDef

### message
- **Type**: typing.Optional[str]

### resourceName
- **Type**: typing.Optional[str]


# EndSessionRequestTypeDef

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# EndSessionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PerformanceConfigurationTypeDef]

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


# FieldForRerankingTypeDef

### fieldName
- **Type**: <class 'str'>
- **Required**: Yes


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
- **Type**: typing.Literal['INPUT_REQUIRED', 'SUCCESS']
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

### nodeInputName
- **Type**: typing.Optional[str]

### nodeOutputName
- **Type**: typing.Optional[str]


# FlowMultiTurnInputContentTypeDef

### document
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowMultiTurnInputRequestEventTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowMultiTurnInputContentTypeDef'>
- **Required**: Yes

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### nodeType
- **Type**: typing.Literal['ConditionNode', 'FlowInputNode', 'FlowOutputNode', 'KnowledgeBaseNode', 'LambdaFunctionNode', 'LexNode', 'PromptNode']
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

### flowMultiTurnInputRequestEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowMultiTurnInputRequestEventTypeDef]

### flowOutputEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowOutputEventTypeDef]

### flowTraceEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceEventTypeDef]

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


# FlowTraceConditionNodeResultEventTypeDef

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### satisfiedConditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceConditionTypeDef]
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# FlowTraceConditionTypeDef

### conditionName
- **Type**: <class 'str'>
- **Required**: Yes


# FlowTraceEventTypeDef

### trace
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceTypeDef'>
- **Required**: Yes


# FlowTraceNodeInputContentTypeDef

### document
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowTraceNodeInputEventTypeDef

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceNodeInputFieldTypeDef]
- **Required**: Yes

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# FlowTraceNodeInputFieldTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceNodeInputContentTypeDef'>
- **Required**: Yes

### nodeInputName
- **Type**: <class 'str'>
- **Required**: Yes


# FlowTraceNodeOutputContentTypeDef

### document
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowTraceNodeOutputEventTypeDef

### fields
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceNodeOutputFieldTypeDef]
- **Required**: Yes

### nodeName
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# FlowTraceNodeOutputFieldTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceNodeOutputContentTypeDef'>
- **Required**: Yes

### nodeOutputName
- **Type**: <class 'str'>
- **Required**: Yes


# FlowTraceTypeDef

### conditionNodeResultTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceConditionNodeResultEventTypeDef]

### nodeInputTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceNodeInputEventTypeDef]

### nodeOutputTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowTraceNodeOutputEventTypeDef]


# FunctionDefinitionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ParameterDetailTypeDef]]

### requireConfirmation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FunctionInvocationInputTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionParameterTypeDef]]


# FunctionParameterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionResultOutputTypeDef

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
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ContentBodyOutputTypeDef]]

### responseState
- **Type**: typing.Optional[typing.Literal['FAILURE', 'REPROMPT']]


# FunctionResultTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ContentBodyUnionTypeDef]]

### responseState
- **Type**: typing.Optional[typing.Literal['FAILURE', 'REPROMPT']]


# FunctionResultUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionSchemaTypeDef

### functions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionDefinitionTypeDef]]


# GenerateQueryRequestTypeDef

### queryGenerationInput
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.QueryGenerationInputTypeDef'>
- **Required**: Yes

### transformationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TransformationConfigurationTypeDef'>
- **Required**: Yes


# GenerateQueryResponseTypeDef

### queries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GeneratedQueryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GeneratedQueryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PerformanceConfigurationTypeDef]

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PromptTemplateTypeDef]


# GetAgentMemoryRequestPaginateTypeDef

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


# GetAgentMemoryRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# GetInvocationStepRequestTypeDef

### invocationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### invocationStepId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetInvocationStepResponseTypeDef

### invocationStep
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationStepTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSessionRequestTypeDef

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionResponseTypeDef

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


# GuardrailConfigurationWithArnTypeDef

### guardrailIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GuardrailContentFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailContentPolicyAssessmentTypeDef

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailContentFilterTypeDef]]


# GuardrailCustomWordTypeDef

### action
- **Type**: typing.Optional[typing.Literal['BLOCKED']]

### match
- **Type**: typing.Optional[str]


# GuardrailEventTypeDef

### action
- **Type**: typing.Optional[typing.Literal['INTERVENED', 'NONE']]


# GuardrailManagedWordTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailPiiEntityFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# ImageBlockOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageBlockTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageInputOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageInputUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImplicitFilterConfigurationTypeDef

### metadataAttributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.MetadataAttributeSchemaTypeDef]
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes


# InferenceConfigTypeDef

### textInferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TextInferenceConfigTypeDef]


# InferenceConfigurationOutputTypeDef

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


# InferenceConfigurationTypeDef

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


# InferenceConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InlineAgentFilePartTypeDef

### files
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OutputFileTypeDef]]


# InlineAgentPayloadPartTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InlineAgentResponseStreamTypeDef

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AccessDeniedExceptionTypeDef]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BadGatewayExceptionTypeDef]

### chunk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineAgentPayloadPartTypeDef]

### conflictException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ConflictExceptionTypeDef]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.DependencyFailedExceptionTypeDef]

### files
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineAgentFilePartTypeDef]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InternalServerExceptionTypeDef]

### resourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResourceNotFoundExceptionTypeDef]

### returnControl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineAgentReturnControlPayloadTypeDef]

### serviceQuotaExceededException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ServiceQuotaExceededExceptionTypeDef]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ThrottlingExceptionTypeDef]

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineAgentTracePartTypeDef]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ValidationExceptionTypeDef]


# InlineAgentReturnControlPayloadTypeDef

### invocationId
- **Type**: typing.Optional[str]

### invocationInputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationInputMemberTypeDef]]


# InlineAgentTracePartTypeDef

### sessionId
- **Type**: typing.Optional[str]

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TraceTypeDef]


# InlineBedrockModelConfigurationsTypeDef

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PerformanceConfigurationTypeDef]


# InlineSessionStateTypeDef

### conversationHistory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ConversationHistoryTypeDef]

### files
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InputFileTypeDef]]

### invocationId
- **Type**: typing.Optional[str]

### promptSessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### returnControlInvocationResults
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationResultMemberUnionTypeDef]]

### sessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


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


# InputPromptTypeDef

### textPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TextPromptTypeDef]


# InternalServerExceptionTypeDef

### message
- **Type**: typing.Optional[str]

### reason
- **Type**: typing.Optional[str]


# InvocationInputMemberTypeDef

### apiInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiInvocationInputTypeDef]

### functionInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionInvocationInputTypeDef]


# InvocationInputTypeDef

### actionGroupInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ActionGroupInvocationInputTypeDef]

### agentCollaboratorInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AgentCollaboratorInvocationInputTypeDef]

### codeInterpreterInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CodeInterpreterInvocationInputTypeDef]

### invocationType
- **Type**: typing.Optional[typing.Literal['ACTION_GROUP', 'ACTION_GROUP_CODE_INTERPRETER', 'AGENT_COLLABORATOR', 'FINISH', 'KNOWLEDGE_BASE']]

### knowledgeBaseLookupInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseLookupInputTypeDef]

### traceId
- **Type**: typing.Optional[str]


# InvocationResultMemberOutputTypeDef

### apiResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiResultOutputTypeDef]

### functionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionResultOutputTypeDef]


# InvocationResultMemberTypeDef

### apiResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ApiResultUnionTypeDef]

### functionResult
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FunctionResultUnionTypeDef]


# InvocationResultMemberUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InvocationStepPayloadOutputTypeDef

### contentBlocks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BedrockSessionContentBlockOutputTypeDef]]


# InvocationStepPayloadTypeDef

### contentBlocks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BedrockSessionContentBlockTypeDef]]


# InvocationStepPayloadUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InvocationStepSummaryTypeDef

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


# InvocationStepTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationStepPayloadOutputTypeDef'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# InvocationSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### invocationId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# InvokeAgentRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BedrockModelConfigurationsTypeDef]

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

### sourceArn
- **Type**: typing.Optional[str]

### streamingConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.StreamingConfigurationsTypeDef]


# InvokeAgentResponseTypeDef

### completion
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseStreamTypeDef]
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


# InvokeFlowRequestTypeDef

### flowAliasIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### inputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowInputTypeDef]
- **Required**: Yes

### enableTrace
- **Type**: typing.Optional[bool]

### executionId
- **Type**: typing.Optional[str]

### modelPerformanceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ModelPerformanceConfigurationTypeDef]


# InvokeFlowResponseTypeDef

### executionId
- **Type**: <class 'str'>
- **Required**: Yes

### responseStream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FlowResponseStreamTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InvokeInlineAgentRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AgentActionGroupTypeDef]]

### agentCollaboration
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SUPERVISOR', 'SUPERVISOR_ROUTER']]

### bedrockModelConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineBedrockModelConfigurationsTypeDef]

### collaboratorConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CollaboratorConfigurationTypeDef]]

### collaborators
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CollaboratorTypeDef]]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### enableTrace
- **Type**: typing.Optional[bool]

### endSession
- **Type**: typing.Optional[bool]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailConfigurationWithArnTypeDef]

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### inlineSessionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineSessionStateTypeDef]

### inputText
- **Type**: typing.Optional[str]

### knowledgeBases
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseTypeDef]]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PromptOverrideConfigurationTypeDef]

### streamingConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.StreamingConfigurationsTypeDef]


# InvokeInlineAgentResponseTypeDef

### completion
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InlineAgentResponseStreamTypeDef]
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
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


# KnowledgeBaseRetrievalConfigurationPaginatorTypeDef

### vectorSearchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseVectorSearchConfigurationPaginatorTypeDef'>
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


# KnowledgeBaseTypeDef

### description
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfigurationTypeDef]


# KnowledgeBaseVectorSearchConfigurationPaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KnowledgeBaseVectorSearchConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListInvocationStepsRequestPaginateTypeDef

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### invocationIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PaginatorConfigTypeDef]


# ListInvocationStepsRequestTypeDef

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### invocationIdentifier
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInvocationStepsResponseTypeDef

### invocationStepSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationStepSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListInvocationsRequestPaginateTypeDef

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PaginatorConfigTypeDef]


# ListInvocationsRequestTypeDef

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListInvocationsResponseTypeDef

### invocationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSessionsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PaginatorConfigTypeDef]


# ListSessionsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListSessionsResponseTypeDef

### sessionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.SessionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# MessageTypeDef

### content
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ContentBlockTypeDef]
- **Required**: Yes

### role
- **Type**: typing.Literal['assistant', 'user']
- **Required**: Yes


# MetadataAttributeSchemaTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetadataConfigurationForRerankingTypeDef

### selectionMode
- **Type**: typing.Literal['ALL', 'SELECTIVE']
- **Required**: Yes

### selectiveModeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankingMetadataSelectiveModeConfigurationTypeDef]


# MetadataTypeDef

### usage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.UsageTypeDef]


# ModelInvocationInputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ModelNotReadyExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# ModelPerformanceConfigurationTypeDef

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PerformanceConfigurationTypeDef]


# ObservationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# OptimizePromptResponseTypeDef

### optimizedPrompt
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OptimizedPromptStreamTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OptimizedPromptEventTypeDef

### optimizedPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OptimizedPromptTypeDef]


# OptimizedPromptStreamTypeDef

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AccessDeniedExceptionTypeDef]

### analyzePromptEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AnalyzePromptEventTypeDef]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BadGatewayExceptionTypeDef]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.DependencyFailedExceptionTypeDef]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InternalServerExceptionTypeDef]

### optimizedPromptEvent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OptimizedPromptEventTypeDef]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ThrottlingExceptionTypeDef]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ValidationExceptionTypeDef]


# OptimizedPromptTypeDef

### textPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TextPromptTypeDef]


# OrchestrationConfigurationTypeDef

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]

### inferenceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InferenceConfigTypeDef]

### performanceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PerformanceConfigurationTypeDef]

### promptTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PromptTemplateTypeDef]

### queryTransformationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.QueryTransformationConfigurationTypeDef]


# OrchestrationModelInvocationOutputTypeDef

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.MetadataTypeDef]

### rawResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RawResponseTypeDef]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ReasoningContentBlockTypeDef]

### traceId
- **Type**: typing.Optional[str]


# OrchestrationTraceTypeDef

### invocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationInputTypeDef]

### modelInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ModelInvocationInputTypeDef]

### modelInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.OrchestrationModelInvocationOutputTypeDef]

### observation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ObservationTypeDef]

### rationale
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RationaleTypeDef]


# OutputFileTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParameterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PayloadPartTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PerformanceConfigurationTypeDef

### latency
- **Type**: typing.Optional[typing.Literal['optimized', 'standard']]


# PostProcessingModelInvocationOutputTypeDef

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.MetadataTypeDef]

### parsedResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PostProcessingParsedResponseTypeDef]

### rawResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RawResponseTypeDef]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ReasoningContentBlockTypeDef]

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

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.MetadataTypeDef]

### parsedResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PreProcessingParsedResponseTypeDef]

### rawResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RawResponseTypeDef]

### reasoningContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ReasoningContentBlockTypeDef]

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


# PromptConfigurationTypeDef

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### basePromptTemplate
- **Type**: typing.Optional[str]

### foundationModel
- **Type**: typing.Optional[str]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InferenceConfigurationUnionTypeDef]

### parserMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### promptCreationMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### promptState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### promptType
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE_RESPONSE_GENERATION', 'ORCHESTRATION', 'POST_PROCESSING', 'PRE_PROCESSING', 'ROUTING_CLASSIFIER']]


# PromptOverrideConfigurationTypeDef

### promptConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PromptConfigurationTypeDef]
- **Required**: Yes

### overrideLambda
- **Type**: typing.Optional[str]


# PromptTemplateTypeDef

### textPromptTemplate
- **Type**: typing.Optional[str]


# PropertyParametersTypeDef

### properties
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ParameterTypeDef]]


# PutInvocationStepRequestTypeDef

### invocationIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### invocationStepTime
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TimestampTypeDef'>
- **Required**: Yes

### payload
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationStepPayloadUnionTypeDef'>
- **Required**: Yes

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### invocationStepId
- **Type**: typing.Optional[str]


# PutInvocationStepResponseTypeDef

### invocationStepId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QueryGenerationInputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueryTransformationConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RationaleTypeDef

### text
- **Type**: typing.Optional[str]

### traceId
- **Type**: typing.Optional[str]


# RawResponseTypeDef

### content
- **Type**: typing.Optional[str]


# ReasoningContentBlockTypeDef

### reasoningText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ReasoningTextBlockTypeDef]

### redactedContent
- **Type**: typing.Optional[bytes]


# ReasoningTextBlockTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes

### signature
- **Type**: typing.Optional[str]


# RepromptResponseTypeDef

### source
- **Type**: typing.Optional[typing.Literal['ACTION_GROUP', 'KNOWLEDGE_BASE', 'PARSER']]

### text
- **Type**: typing.Optional[str]


# RequestBodyTypeDef

### content
- **Type**: typing.Optional[typing.Dict[str, typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ParameterTypeDef]]]


# RerankDocumentOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RerankQueryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RerankRequestPaginateTypeDef

### queries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankQueryTypeDef]
- **Required**: Yes

### rerankingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankingConfigurationTypeDef'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankSourceTypeDef]
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PaginatorConfigTypeDef]


# RerankRequestTypeDef

### queries
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankQueryTypeDef]
- **Required**: Yes

### rerankingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankingConfigurationTypeDef'>
- **Required**: Yes

### sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankSourceTypeDef]
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# RerankResponseTypeDef

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# RerankResultTypeDef

### index
- **Type**: <class 'int'>
- **Required**: Yes

### relevanceScore
- **Type**: <class 'float'>
- **Required**: Yes

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RerankDocumentOutputTypeDef]


# RerankSourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RerankTextDocumentTypeDef

### text
- **Type**: typing.Optional[str]


# RerankingConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RerankingMetadataSelectiveModeConfigurationTypeDef

### fieldsToExclude
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FieldForRerankingTypeDef]]

### fieldsToInclude
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.FieldForRerankingTypeDef]]


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

### modelNotReadyException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ModelNotReadyExceptionTypeDef]

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


# RetrievalResultConfluenceLocationTypeDef

### url
- **Type**: typing.Optional[str]


# RetrievalResultContentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RetrievalResultKendraDocumentLocationTypeDef

### uri
- **Type**: typing.Optional[str]


# RetrievalResultLocationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RetrievalResultS3LocationTypeDef

### uri
- **Type**: typing.Optional[str]


# RetrievalResultSalesforceLocationTypeDef

### url
- **Type**: typing.Optional[str]


# RetrievalResultSharePointLocationTypeDef

### url
- **Type**: typing.Optional[str]


# RetrievalResultSqlLocationTypeDef

### query
- **Type**: typing.Optional[str]


# RetrievalResultWebLocationTypeDef

### url
- **Type**: typing.Optional[str]


# RetrieveAndGenerateInputTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveAndGenerateOutputEventTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveAndGenerateOutputTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes


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


# RetrieveAndGenerateStreamResponseOutputTypeDef

### accessDeniedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.AccessDeniedExceptionTypeDef]

### badGatewayException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.BadGatewayExceptionTypeDef]

### citation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CitationEventTypeDef]

### conflictException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ConflictExceptionTypeDef]

### dependencyFailedException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.DependencyFailedExceptionTypeDef]

### guardrail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailEventTypeDef]

### internalServerException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InternalServerExceptionTypeDef]

### output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrieveAndGenerateOutputEventTypeDef]

### resourceNotFoundException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResourceNotFoundExceptionTypeDef]

### serviceQuotaExceededException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ServiceQuotaExceededExceptionTypeDef]

### throttlingException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ThrottlingExceptionTypeDef]

### validationException
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ValidationExceptionTypeDef]


# RetrieveAndGenerateStreamResponseTypeDef

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### stream
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RetrieveAndGenerateStreamResponseOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RetrieveRequestPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseQueryTypeDef'>
- **Required**: Yes

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailConfigurationTypeDef]

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfigurationPaginatorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.PaginatorConfigTypeDef]


# RetrieveRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### retrievalQuery
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseQueryTypeDef'>
- **Required**: Yes

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.GuardrailConfigurationTypeDef]

### nextToken
- **Type**: typing.Optional[str]

### retrievalConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalConfigurationTypeDef]


# RetrieveResponseTypeDef

### guardrailAction
- **Type**: typing.Literal['INTERVENED', 'NONE']
- **Required**: Yes

### retrievalResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseRetrievalResultTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


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


# ReturnControlResultsTypeDef

### invocationId
- **Type**: typing.Optional[str]

### returnControlInvocationResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationResultMemberOutputTypeDef]]


# RoutingClassifierModelInvocationOutputTypeDef

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.MetadataTypeDef]

### rawResponse
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RawResponseTypeDef]

### traceId
- **Type**: typing.Optional[str]


# RoutingClassifierTraceTypeDef

### invocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationInputTypeDef]

### modelInvocationInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ModelInvocationInputTypeDef]

### modelInvocationOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RoutingClassifierModelInvocationOutputTypeDef]

### observation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ObservationTypeDef]


# S3IdentifierTypeDef

### s3BucketName
- **Type**: typing.Optional[str]

### s3ObjectKey
- **Type**: typing.Optional[str]


# S3LocationTypeDef

### uri
- **Type**: <class 'str'>
- **Required**: Yes


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

### conversationHistory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ConversationHistoryTypeDef]

### files
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InputFileTypeDef]]

### invocationId
- **Type**: typing.Optional[str]

### knowledgeBaseConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.KnowledgeBaseConfigurationTypeDef]]

### promptSessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### returnControlInvocationResults
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.InvocationResultMemberUnionTypeDef]]

### sessionAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# SessionSummaryTypeDef

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


# SpanTypeDef

### end
- **Type**: typing.Optional[int]

### start
- **Type**: typing.Optional[int]


# StreamingConfigurationsTypeDef

### applyGuardrailInterval
- **Type**: typing.Optional[int]

### streamFinalResponse
- **Type**: typing.Optional[bool]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TextInferenceConfigTypeDef

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.Sequence[str]]

### temperature
- **Type**: typing.Optional[float]

### topP
- **Type**: typing.Optional[float]


# TextPromptTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes


# TextResponsePartTypeDef

### span
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.SpanTypeDef]

### text
- **Type**: typing.Optional[str]


# TextToSqlConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TextToSqlKnowledgeBaseConfigurationTypeDef

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes


# ThrottlingExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TracePartTypeDef

### agentAliasId
- **Type**: typing.Optional[str]

### agentId
- **Type**: typing.Optional[str]

### agentVersion
- **Type**: typing.Optional[str]

### callerChain
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CallerTypeDef]]

### collaboratorName
- **Type**: typing.Optional[str]

### eventTime
- **Type**: typing.Optional[datetime.datetime]

### sessionId
- **Type**: typing.Optional[str]

### trace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TraceTypeDef]


# TraceTypeDef

### customOrchestrationTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.CustomOrchestrationTraceTypeDef]

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

### routingClassifierTrace
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.RoutingClassifierTraceTypeDef]


# TransformationConfigurationTypeDef

### mode
- **Type**: typing.Literal['TEXT_TO_SQL']
- **Required**: Yes

### textToSqlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.TextToSqlConfigurationTypeDef]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateSessionRequestTypeDef

### sessionIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### sessionMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateSessionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UsageTypeDef

### inputTokens
- **Type**: typing.Optional[int]

### outputTokens
- **Type**: typing.Optional[int]


# ValidationExceptionTypeDef

### message
- **Type**: typing.Optional[str]


# VectorSearchBedrockRerankingConfigurationTypeDef

### modelConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.VectorSearchBedrockRerankingModelConfigurationTypeDef'>
- **Required**: Yes

### metadataConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_runtime_classes.MetadataConfigurationForRerankingTypeDef]

### numberOfRerankedResults
- **Type**: typing.Optional[int]


# VectorSearchBedrockRerankingModelConfigurationTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, typing.Any]]]


