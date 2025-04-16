# Bedrock Agent Classes

# APISchema

### payload
- **Type**: typing.Optional[str]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.S3Identifier]


# ActionGroupExecutor

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionGroupSummary

### actionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### actionGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### actionGroupState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# Agent

### agentArn
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentName
- **Type**: <class 'str'>
- **Required**: Yes

### agentResourceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### agentStatus
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'NOT_PREPARED', 'PREPARED', 'PREPARING', 'UPDATING', 'VERSIONING']
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### agentCollaboration
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SUPERVISOR', 'SUPERVISOR_ROUTER']]

### clientToken
- **Type**: typing.Optional[str]

### customOrchestration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomOrchestration]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]

### foundationModel
- **Type**: typing.Optional[str]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfiguration]

### instruction
- **Type**: typing.Optional[str]

### memoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MemoryConfigurationOutput]

### orchestrationType
- **Type**: typing.Optional[typing.Literal['CUSTOM_ORCHESTRATION', 'DEFAULT']]

### preparedAt
- **Type**: typing.Optional[datetime.datetime]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptOverrideConfigurationOutput]

### recommendedActions
- **Type**: typing.Optional[typing.List[str]]


# AgentActionGroup

### actionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### actionGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### actionGroupState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### actionGroupExecutor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ActionGroupExecutor]

### apiSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.APISchema]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### functionSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FunctionSchemaOutput]

### parentActionGroupSignatureParams
- **Type**: typing.Optional[typing.Dict[str, str]]

### parentActionSignature
- **Type**: typing.Optional[typing.Literal['AMAZON.CodeInterpreter', 'AMAZON.UserInput', 'ANTHROPIC.Bash', 'ANTHROPIC.Computer', 'ANTHROPIC.TextEditor']]


# AgentAlias

### agentAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentAliasName
- **Type**: <class 'str'>
- **Required**: Yes

### agentAliasStatus
- **Type**: typing.Literal['CREATING', 'DELETING', 'DISSOCIATED', 'FAILED', 'PREPARED', 'UPDATING']
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### routingConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasRoutingConfigurationListItem]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### agentAliasHistoryEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasHistoryEvent]]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]


# AgentAliasHistoryEvent

### endDate
- **Type**: typing.Optional[datetime.datetime]

### routingConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasRoutingConfigurationListItem]]

### startDate
- **Type**: typing.Optional[datetime.datetime]


# AgentAliasRoutingConfigurationListItem

### agentVersion
- **Type**: typing.Optional[str]

### provisionedThroughput
- **Type**: typing.Optional[str]


# AgentAliasSummary

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentAliasName
- **Type**: <class 'str'>
- **Required**: Yes

### agentAliasStatus
- **Type**: typing.Literal['CREATING', 'DELETING', 'DISSOCIATED', 'FAILED', 'PREPARED', 'UPDATING']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### routingConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasRoutingConfigurationListItem]]


# AgentCollaborator

### agentDescriptor
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentDescriptor'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationInstruction
- **Type**: <class 'str'>
- **Required**: Yes

### collaboratorId
- **Type**: <class 'str'>
- **Required**: Yes

### collaboratorName
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### relayConversationHistory
- **Type**: typing.Optional[typing.Literal['DISABLED', 'TO_COLLABORATOR']]


# AgentCollaboratorSummary

### agentDescriptor
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentDescriptor'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationInstruction
- **Type**: <class 'str'>
- **Required**: Yes

### collaboratorId
- **Type**: <class 'str'>
- **Required**: Yes

### collaboratorName
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### lastUpdatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### relayConversationHistory
- **Type**: typing.Literal['DISABLED', 'TO_COLLABORATOR']
- **Required**: Yes


# AgentDescriptor

### aliasArn
- **Type**: typing.Optional[str]


# AgentFlowNodeConfiguration

### agentAliasArn
- **Type**: <class 'str'>
- **Required**: Yes


# AgentKnowledgeBase

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# AgentKnowledgeBaseSummary

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseState
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# AgentSummary

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentName
- **Type**: <class 'str'>
- **Required**: Yes

### agentStatus
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'NOT_PREPARED', 'PREPARED', 'PREPARING', 'UPDATING', 'VERSIONING']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfiguration]

### latestAgentVersion
- **Type**: typing.Optional[str]


# AgentVersion

### agentArn
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentName
- **Type**: <class 'str'>
- **Required**: Yes

### agentResourceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### agentStatus
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'NOT_PREPARED', 'PREPARED', 'PREPARING', 'UPDATING', 'VERSIONING']
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### idleSessionTTLInSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### agentCollaboration
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SUPERVISOR', 'SUPERVISOR_ROUTER']]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]

### foundationModel
- **Type**: typing.Optional[str]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfiguration]

### instruction
- **Type**: typing.Optional[str]

### memoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MemoryConfigurationOutput]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptOverrideConfigurationOutput]

### recommendedActions
- **Type**: typing.Optional[typing.List[str]]


# AgentVersionSummary

### agentName
- **Type**: <class 'str'>
- **Required**: Yes

### agentStatus
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'NOT_PREPARED', 'PREPARED', 'PREPARING', 'UPDATING', 'VERSIONING']
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfiguration]


# AssociateAgentCollaboratorRequest

### agentDescriptor
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentDescriptor'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationInstruction
- **Type**: <class 'str'>
- **Required**: Yes

### collaboratorName
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### relayConversationHistory
- **Type**: typing.Optional[typing.Literal['DISABLED', 'TO_COLLABORATOR']]


# AssociateAgentCollaboratorResponse

### agentCollaborator
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentCollaborator'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateAgentKnowledgeBaseRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AssociateAgentKnowledgeBaseResponse

### agentKnowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentKnowledgeBase'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BedrockDataAutomationConfiguration

### parsingModality
- **Type**: typing.Optional[typing.Literal['MULTIMODAL']]


# BedrockEmbeddingModelConfiguration

### dimensions
- **Type**: typing.Optional[int]

### embeddingDataType
- **Type**: typing.Optional[typing.Literal['BINARY', 'FLOAT32']]


# BedrockFoundationModelConfiguration

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### parsingModality
- **Type**: typing.Optional[typing.Literal['MULTIMODAL']]

### parsingPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ParsingPrompt]


# BedrockFoundationModelContextEnrichmentConfiguration

### enrichmentStrategyConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.EnrichmentStrategyConfiguration'>
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes


# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ByteContentDoc

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.Blob'>
- **Required**: Yes

### mimeType
- **Type**: <class 'str'>
- **Required**: Yes


# CachePointBlock

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChatPromptTemplateConfiguration

### messages
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.MessageUnion]
- **Required**: Yes

### inputVariables
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInputVariable]]

### system
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.SystemContentBlock]]

### toolConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolConfigurationUnion]


# ChatPromptTemplateConfigurationOutput

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.MessageOutput]
- **Required**: Yes

### inputVariables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInputVariable]]

### system
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.SystemContentBlock]]

### toolConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolConfigurationOutput]


# ChatPromptTemplateConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChunkingConfiguration

### chunkingStrategy
- **Type**: typing.Literal['FIXED_SIZE', 'HIERARCHICAL', 'NONE', 'SEMANTIC']
- **Required**: Yes

### fixedSizeChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FixedSizeChunkingConfiguration]

### hierarchicalChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.HierarchicalChunkingConfiguration]

### semanticChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SemanticChunkingConfiguration]


# ChunkingConfigurationOutput

### chunkingStrategy
- **Type**: typing.Literal['FIXED_SIZE', 'HIERARCHICAL', 'NONE', 'SEMANTIC']
- **Required**: Yes

### fixedSizeChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FixedSizeChunkingConfiguration]

### hierarchicalChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.HierarchicalChunkingConfigurationOutput]

### semanticChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SemanticChunkingConfiguration]


# ConditionFlowNodeConfiguration

### conditions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowCondition]
- **Required**: Yes


# ConditionFlowNodeConfigurationOutput

### conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowCondition]
- **Required**: Yes


# ConfluenceCrawlerConfiguration

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CrawlFilterConfiguration]


# ConfluenceCrawlerConfigurationOutput

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CrawlFilterConfigurationOutput]


# ConfluenceDataSourceConfiguration

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ConfluenceSourceConfiguration'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ConfluenceCrawlerConfiguration]


# ConfluenceDataSourceConfigurationOutput

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ConfluenceSourceConfiguration'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ConfluenceCrawlerConfigurationOutput]


# ConfluenceSourceConfiguration

### authType
- **Type**: typing.Literal['BASIC', 'OAUTH2_CLIENT_CREDENTIALS']
- **Required**: Yes

### credentialsSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### hostType
- **Type**: typing.Literal['SAAS']
- **Required**: Yes

### hostUrl
- **Type**: <class 'str'>
- **Required**: Yes


# ContentBlock

### cachePoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CachePointBlock]

### text
- **Type**: typing.Optional[str]


# ContextEnrichmentConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CrawlFilterConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CrawlFilterConfigurationOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAgentActionGroupRequest

### actionGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### actionGroupExecutor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ActionGroupExecutor]

### actionGroupState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### apiSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.APISchema]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### functionSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FunctionSchemaUnion]

### parentActionGroupSignature
- **Type**: typing.Optional[typing.Literal['AMAZON.CodeInterpreter', 'AMAZON.UserInput', 'ANTHROPIC.Bash', 'ANTHROPIC.Computer', 'ANTHROPIC.TextEditor']]

### parentActionGroupSignatureParams
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAgentActionGroupResponse

### agentActionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentActionGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAgentAliasRequest

### agentAliasName
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### routingConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasRoutingConfigurationListItem]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAgentAliasResponse

### agentAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAlias'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAgentRequest

### agentName
- **Type**: <class 'str'>
- **Required**: Yes

### agentCollaboration
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SUPERVISOR', 'SUPERVISOR_ROUTER']]

### agentResourceRoleArn
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

### customOrchestration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomOrchestration]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### foundationModel
- **Type**: typing.Optional[str]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfiguration]

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### instruction
- **Type**: typing.Optional[str]

### memoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MemoryConfigurationUnion]

### orchestrationType
- **Type**: typing.Optional[typing.Literal['CUSTOM_ORCHESTRATION', 'DEFAULT']]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptOverrideConfigurationUnion]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAgentResponse

### agent
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.Agent'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataSourceRequest

### dataSourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceConfigurationUnion'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### dataDeletionPolicy
- **Type**: typing.Optional[typing.Literal['DELETE', 'RETAIN']]

### description
- **Type**: typing.Optional[str]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ServerSideEncryptionConfiguration]

### vectorIngestionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.VectorIngestionConfigurationUnion]


# CreateDataSourceResponse

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFlowAliasRequest

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### routingConfiguration
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowAliasRoutingConfigurationListItem]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFlowRequest

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDefinitionUnion]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFlowVersionRequest

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateKnowledgeBaseRequest

### knowledgeBaseConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseConfigurationUnion'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### storageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageConfiguration]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateKnowledgeBaseResponse

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBase'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePromptRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### defaultVariant
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### variants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptVariantUnion]]


# CreatePromptVersionRequest

### promptIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CuratedQuery

### naturalLanguage
- **Type**: <class 'str'>
- **Required**: Yes

### sql
- **Type**: <class 'str'>
- **Required**: Yes


# CustomContent

### customDocumentIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomDocumentIdentifier'>
- **Required**: Yes

### sourceType
- **Type**: typing.Literal['IN_LINE', 'S3_LOCATION']
- **Required**: Yes

### inlineContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.InlineContent]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomS3Location]


# CustomDocumentIdentifier

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomOrchestration

### executor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.OrchestrationExecutor]


# CustomS3Location

### uri
- **Type**: <class 'str'>
- **Required**: Yes

### bucketOwnerAccountId
- **Type**: typing.Optional[str]


# CustomTransformationConfiguration

### intermediateStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.IntermediateStorage'>
- **Required**: Yes

### transformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.Transformation]
- **Required**: Yes


# CustomTransformationConfigurationOutput

### intermediateStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.IntermediateStorage'>
- **Required**: Yes

### transformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.Transformation]
- **Required**: Yes


# CyclicConnectionFlowValidationDetails

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# DataSource

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dataSourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceConfigurationOutput'>
- **Required**: Yes

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'DELETE_UNSUCCESSFUL', 'DELETING']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dataDeletionPolicy
- **Type**: typing.Optional[typing.Literal['DELETE', 'RETAIN']]

### description
- **Type**: typing.Optional[str]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ServerSideEncryptionConfiguration]

### vectorIngestionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.VectorIngestionConfigurationOutput]


# DataSourceConfigurationOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceSummary

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'DELETE_UNSUCCESSFUL', 'DELETING']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# DeleteAgentActionGroupRequest

### actionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteAgentAliasRequest

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAgentAliasResponse

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentAliasStatus
- **Type**: typing.Literal['CREATING', 'DELETING', 'DISSOCIATED', 'FAILED', 'PREPARED', 'UPDATING']
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAgentRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteAgentResponse

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentStatus
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'NOT_PREPARED', 'PREPARED', 'PREPARING', 'UPDATING', 'VERSIONING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAgentVersionRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteAgentVersionResponse

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentStatus
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'NOT_PREPARED', 'PREPARED', 'PREPARING', 'UPDATING', 'VERSIONING']
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDataSourceRequest

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceResponse

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['AVAILABLE', 'DELETE_UNSUCCESSFUL', 'DELETING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFlowAliasRequest

### aliasIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFlowRequest

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteFlowVersionRequest

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowVersion
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteKnowledgeBaseDocumentsRequest

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### documentIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.DocumentIdentifier]
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteKnowledgeBaseDocumentsResponse

### documentDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseDocumentDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteKnowledgeBaseRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKnowledgeBaseResponse

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETE_UNSUCCESSFUL', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePromptRequest

### promptIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### promptVersion
- **Type**: typing.Optional[str]


# DisassociateAgentCollaboratorRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### collaboratorId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateAgentKnowledgeBaseRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DocumentContent

### dataSourceType
- **Type**: typing.Literal['CUSTOM', 'S3']
- **Required**: Yes

### custom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomContent]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.S3Content]


# DocumentIdentifier

### dataSourceType
- **Type**: typing.Literal['CUSTOM', 'S3']
- **Required**: Yes

### custom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomDocumentIdentifier]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.S3Location]


# DocumentMetadata

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DuplicateConditionExpressionFlowValidationDetails

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### node
- **Type**: <class 'str'>
- **Required**: Yes


# DuplicateConnectionsFlowValidationDetails

### source
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes


# EmbeddingModelConfiguration

### bedrockEmbeddingModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.BedrockEmbeddingModelConfiguration]


# EnrichmentStrategyConfiguration

### method
- **Type**: typing.Literal['CHUNK_ENTITY_EXTRACTION']
- **Required**: Yes


# FixedSizeChunkingConfiguration

### maxTokens
- **Type**: <class 'int'>
- **Required**: Yes

### overlapPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# FlowAliasRoutingConfigurationListItem

### flowVersion
- **Type**: typing.Optional[str]


# FlowAliasSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowCondition

### name
- **Type**: <class 'str'>
- **Required**: Yes

### expression
- **Type**: typing.Optional[str]


# FlowConditionalConnectionConfiguration

### condition
- **Type**: <class 'str'>
- **Required**: Yes


# FlowConnection

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowConnectionConfiguration

### conditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowConditionalConnectionConfiguration]

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDataConnectionConfiguration]


# FlowDataConnectionConfiguration

### sourceOutput
- **Type**: <class 'str'>
- **Required**: Yes

### targetInput
- **Type**: <class 'str'>
- **Required**: Yes


# FlowDefinition

### connections
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowConnection]]

### nodes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowNode]]


# FlowDefinitionOutput

### connections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowConnection]]

### nodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowNodeExtra]]


# FlowDefinitionUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowNode

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowNodeExtra

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowValidation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowValidationDetails

### cyclicConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CyclicConnectionFlowValidationDetails]

### duplicateConditionExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.DuplicateConditionExpressionFlowValidationDetails]

### duplicateConnections
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.DuplicateConnectionsFlowValidationDetails]

### incompatibleConnectionDataType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.IncompatibleConnectionDataTypeFlowValidationDetails]

### malformedConditionExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MalformedConditionExpressionFlowValidationDetails]

### malformedNodeInputExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MalformedNodeInputExpressionFlowValidationDetails]

### mismatchedNodeInputType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MismatchedNodeInputTypeFlowValidationDetails]

### mismatchedNodeOutputType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MismatchedNodeOutputTypeFlowValidationDetails]

### missingConnectionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MissingConnectionConfigurationFlowValidationDetails]

### missingDefaultCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MissingDefaultConditionFlowValidationDetails]

### missingEndingNodes
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### missingNodeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MissingNodeConfigurationFlowValidationDetails]

### missingNodeInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MissingNodeInputFlowValidationDetails]

### missingNodeOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MissingNodeOutputFlowValidationDetails]

### missingStartingNodes
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### multipleNodeInputConnections
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MultipleNodeInputConnectionsFlowValidationDetails]

### unfulfilledNodeInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnfulfilledNodeInputFlowValidationDetails]

### unknownConnectionCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownConnectionConditionFlowValidationDetails]

### unknownConnectionSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownConnectionSourceFlowValidationDetails]

### unknownConnectionSourceOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownConnectionSourceOutputFlowValidationDetails]

### unknownConnectionTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownConnectionTargetFlowValidationDetails]

### unknownConnectionTargetInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownConnectionTargetInputFlowValidationDetails]

### unknownNodeInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownNodeInputFlowValidationDetails]

### unknownNodeOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownNodeOutputFlowValidationDetails]

### unreachableNode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnreachableNodeFlowValidationDetails]

### unsatisfiedConnectionConditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnsatisfiedConnectionConditionsFlowValidationDetails]

### unspecified
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowVersionSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Function

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.bedrock_agent_classes.ParameterDetail]]

### requireConfirmation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FunctionOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_classes.ParameterDetail]]

### requireConfirmation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FunctionSchema

### functions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.Function]]


# FunctionSchemaOutput

### functions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FunctionOutput]]


# FunctionSchemaUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetAgentActionGroupRequest

### actionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentActionGroupResponse

### agentActionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentActionGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# GetAgentAliasRequest

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentAliasResponse

### agentAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAlias'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# GetAgentCollaboratorRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### collaboratorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentCollaboratorResponse

### agentCollaborator
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentCollaborator'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# GetAgentKnowledgeBaseRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentKnowledgeBaseResponse

### agentKnowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentKnowledgeBase'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# GetAgentRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentResponse

### agent
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.Agent'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# GetAgentVersionRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentVersionResponse

### agentVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataSourceRequest

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSourceResponse

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# GetFlowAliasRequest

### aliasIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetFlowRequest

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetFlowVersionRequest

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetIngestionJobRequest

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionJobId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIngestionJobResponse

### ingestionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# GetKnowledgeBaseDocumentsRequest

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### documentIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.DocumentIdentifier]
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKnowledgeBaseDocumentsResponse

### documentDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseDocumentDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# GetKnowledgeBaseRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKnowledgeBaseResponse

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBase'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# GetPromptRequest

### promptIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### promptVersion
- **Type**: typing.Optional[str]


# GuardrailConfiguration

### guardrailIdentifier
- **Type**: typing.Optional[str]

### guardrailVersion
- **Type**: typing.Optional[str]


# HierarchicalChunkingConfiguration

### levelConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.HierarchicalChunkingLevelConfiguration]
- **Required**: Yes

### overlapTokens
- **Type**: <class 'int'>
- **Required**: Yes


# HierarchicalChunkingConfigurationOutput

### levelConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.HierarchicalChunkingLevelConfiguration]
- **Required**: Yes

### overlapTokens
- **Type**: <class 'int'>
- **Required**: Yes


# HierarchicalChunkingLevelConfiguration

### maxTokens
- **Type**: <class 'int'>
- **Required**: Yes


# IncompatibleConnectionDataTypeFlowValidationDetails

### connection
- **Type**: <class 'str'>
- **Required**: Yes


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


# IngestKnowledgeBaseDocumentsRequest

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### documents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseDocument]
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# IngestKnowledgeBaseDocumentsResponse

### documentDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseDocumentDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# IngestionJob

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionJobId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]

### statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobStatistics]


# IngestionJobFilter

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IngestionJobSortBy

### attribute
- **Type**: typing.Literal['STARTED_AT', 'STATUS']
- **Required**: Yes

### order
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# IngestionJobStatistics

### numberOfDocumentsDeleted
- **Type**: typing.Optional[int]

### numberOfDocumentsFailed
- **Type**: typing.Optional[int]

### numberOfDocumentsScanned
- **Type**: typing.Optional[int]

### numberOfMetadataDocumentsModified
- **Type**: typing.Optional[int]

### numberOfMetadataDocumentsScanned
- **Type**: typing.Optional[int]

### numberOfModifiedDocumentsIndexed
- **Type**: typing.Optional[int]

### numberOfNewDocumentsIndexed
- **Type**: typing.Optional[int]


# IngestionJobSummary

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionJobId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### startedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### statistics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobStatistics]


# InlineContent

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IntermediateStorage

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.S3Location'>
- **Required**: Yes


# KendraKnowledgeBaseConfiguration

### kendraIndexArn
- **Type**: <class 'str'>
- **Required**: Yes


# KnowledgeBase

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseConfigurationOutput'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETE_UNSUCCESSFUL', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]

### storageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageConfiguration]


# KnowledgeBaseConfigurationOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KnowledgeBaseConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KnowledgeBaseDocument

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DocumentContent'>
- **Required**: Yes

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.DocumentMetadata]


# KnowledgeBaseDocumentDetail

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DocumentIdentifier'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['DELETE_IN_PROGRESS', 'DELETING', 'FAILED', 'IGNORED', 'INDEXED', 'IN_PROGRESS', 'METADATA_PARTIALLY_INDEXED', 'METADATA_UPDATE_FAILED', 'NOT_FOUND', 'PARTIALLY_INDEXED', 'PENDING', 'STARTING']
- **Required**: Yes

### statusReason
- **Type**: typing.Optional[str]

### updatedAt
- **Type**: typing.Optional[datetime.datetime]


# KnowledgeBaseFlowNodeConfiguration

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfiguration]

### modelId
- **Type**: typing.Optional[str]


# KnowledgeBaseSummary

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETE_UNSUCCESSFUL', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# LambdaFunctionFlowNodeConfiguration

### lambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# LexFlowNodeConfiguration

### botAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# ListAgentActionGroupsRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAgentActionGroupsRequestPaginate

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListAgentActionGroupsResponse

### actionGroupSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.ActionGroupSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAgentAliasesRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAgentAliasesRequestPaginate

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListAgentAliasesResponse

### agentAliasSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAgentCollaboratorsRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAgentCollaboratorsRequestPaginate

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListAgentCollaboratorsResponse

### agentCollaboratorSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentCollaboratorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAgentKnowledgeBasesRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAgentKnowledgeBasesRequestPaginate

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListAgentKnowledgeBasesResponse

### agentKnowledgeBaseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentKnowledgeBaseSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAgentVersionsRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAgentVersionsRequestPaginate

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListAgentVersionsResponse

### agentVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAgentsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAgentsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListAgentsResponse

### agentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourcesRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourcesRequestPaginate

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListDataSourcesResponse

### dataSourceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFlowAliasesRequest

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFlowAliasesRequestPaginate

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListFlowAliasesResponse

### flowAliasSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowAliasSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFlowVersionsRequest

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFlowVersionsRequestPaginate

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListFlowVersionsResponse

### flowVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFlowsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFlowsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListFlowsResponse

### flowSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIngestionJobsRequest

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobFilter]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobSortBy]


# ListIngestionJobsRequestPaginate

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobFilter]]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobSortBy]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListIngestionJobsResponse

### ingestionJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKnowledgeBaseDocumentsRequest

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListKnowledgeBaseDocumentsRequestPaginate

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListKnowledgeBaseDocumentsResponse

### documentDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseDocumentDetail]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKnowledgeBasesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListKnowledgeBasesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListKnowledgeBasesResponse

### knowledgeBaseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPromptsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### promptIdentifier
- **Type**: typing.Optional[str]


# ListPromptsRequestPaginate

### promptIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfig]


# ListPromptsResponse

### promptSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# MalformedConditionExpressionFlowValidationDetails

### cause
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: <class 'str'>
- **Required**: Yes

### node
- **Type**: <class 'str'>
- **Required**: Yes


# MalformedNodeInputExpressionFlowValidationDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MemoryConfiguration

### enabledMemoryTypes
- **Type**: typing.Sequence[typing.Literal['SESSION_SUMMARY']]
- **Required**: Yes

### sessionSummaryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SessionSummaryConfiguration]

### storageDays
- **Type**: typing.Optional[int]


# MemoryConfigurationOutput

### enabledMemoryTypes
- **Type**: typing.List[typing.Literal['SESSION_SUMMARY']]
- **Required**: Yes

### sessionSummaryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SessionSummaryConfiguration]

### storageDays
- **Type**: typing.Optional[int]


# MemoryConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Message

### content
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.ContentBlock]
- **Required**: Yes

### role
- **Type**: typing.Literal['assistant', 'user']
- **Required**: Yes


# MessageOutput

### content
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.ContentBlock]
- **Required**: Yes

### role
- **Type**: typing.Literal['assistant', 'user']
- **Required**: Yes


# MessageUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetadataAttribute

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.MetadataAttributeValue'>
- **Required**: Yes


# MetadataAttributeValue

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MismatchedNodeInputTypeFlowValidationDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MismatchedNodeOutputTypeFlowValidationDetails

### expectedType
- **Type**: typing.Literal['Array', 'Boolean', 'Number', 'Object', 'String']
- **Required**: Yes

### node
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: <class 'str'>
- **Required**: Yes


# MissingConnectionConfigurationFlowValidationDetails

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# MissingDefaultConditionFlowValidationDetails

### node
- **Type**: <class 'str'>
- **Required**: Yes


# MissingNodeConfigurationFlowValidationDetails

### node
- **Type**: <class 'str'>
- **Required**: Yes


# MissingNodeInputFlowValidationDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MissingNodeOutputFlowValidationDetails

### node
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: <class 'str'>
- **Required**: Yes


# MongoDbAtlasConfiguration

### collectionName
- **Type**: <class 'str'>
- **Required**: Yes

### credentialsSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### fieldMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.MongoDbAtlasFieldMapping'>
- **Required**: Yes

### vectorIndexName
- **Type**: <class 'str'>
- **Required**: Yes

### endpointServiceName
- **Type**: typing.Optional[str]


# MongoDbAtlasFieldMapping

### metadataField
- **Type**: <class 'str'>
- **Required**: Yes

### textField
- **Type**: <class 'str'>
- **Required**: Yes

### vectorField
- **Type**: <class 'str'>
- **Required**: Yes


# MultipleNodeInputConnectionsFlowValidationDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NeptuneAnalyticsConfiguration

### fieldMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.NeptuneAnalyticsFieldMapping'>
- **Required**: Yes

### graphArn
- **Type**: <class 'str'>
- **Required**: Yes


# NeptuneAnalyticsFieldMapping

### metadataField
- **Type**: <class 'str'>
- **Required**: Yes

### textField
- **Type**: <class 'str'>
- **Required**: Yes


# OpenSearchServerlessConfiguration

### collectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### fieldMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.OpenSearchServerlessFieldMapping'>
- **Required**: Yes

### vectorIndexName
- **Type**: <class 'str'>
- **Required**: Yes


# OpenSearchServerlessFieldMapping

### metadataField
- **Type**: <class 'str'>
- **Required**: Yes

### textField
- **Type**: <class 'str'>
- **Required**: Yes

### vectorField
- **Type**: <class 'str'>
- **Required**: Yes


# OrchestrationExecutor

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterDetail

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ParsingConfiguration

### parsingStrategy
- **Type**: typing.Literal['BEDROCK_DATA_AUTOMATION', 'BEDROCK_FOUNDATION_MODEL']
- **Required**: Yes

### bedrockDataAutomationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.BedrockDataAutomationConfiguration]

### bedrockFoundationModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.BedrockFoundationModelConfiguration]


# ParsingPrompt

### parsingPromptText
- **Type**: <class 'str'>
- **Required**: Yes


# PatternObjectFilter

### objectType
- **Type**: <class 'str'>
- **Required**: Yes

### exclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### inclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]


# PatternObjectFilterConfiguration

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PatternObjectFilter]
- **Required**: Yes


# PatternObjectFilterConfigurationOutput

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PatternObjectFilterOutput]
- **Required**: Yes


# PatternObjectFilterOutput

### objectType
- **Type**: <class 'str'>
- **Required**: Yes

### exclusionFilters
- **Type**: typing.Optional[typing.List[str]]

### inclusionFilters
- **Type**: typing.Optional[typing.List[str]]


# PineconeConfiguration

### connectionString
- **Type**: <class 'str'>
- **Required**: Yes

### credentialsSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### fieldMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PineconeFieldMapping'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[str]


# PineconeFieldMapping

### metadataField
- **Type**: <class 'str'>
- **Required**: Yes

### textField
- **Type**: <class 'str'>
- **Required**: Yes


# PrepareAgentRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes


# PrepareAgentResponse

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentStatus
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'NOT_PREPARED', 'PREPARED', 'PREPARING', 'UPDATING', 'VERSIONING']
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### preparedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# PrepareFlowRequest

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PromptAgentResource

### agentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PromptConfiguration

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### basePromptTemplate
- **Type**: typing.Optional[str]

### foundationModel
- **Type**: typing.Optional[str]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.InferenceConfiguration]

### parserMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### promptCreationMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### promptState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### promptType
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE_RESPONSE_GENERATION', 'MEMORY_SUMMARIZATION', 'ORCHESTRATION', 'POST_PROCESSING', 'PRE_PROCESSING']]


# PromptConfigurationOutput

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### basePromptTemplate
- **Type**: typing.Optional[str]

### foundationModel
- **Type**: typing.Optional[str]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.InferenceConfigurationOutput]

### parserMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### promptCreationMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### promptState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### promptType
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE_RESPONSE_GENERATION', 'MEMORY_SUMMARIZATION', 'ORCHESTRATION', 'POST_PROCESSING', 'PRE_PROCESSING']]


# PromptFlowNodeConfiguration

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeSourceConfiguration'>
- **Required**: Yes

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfiguration]


# PromptFlowNodeConfigurationOutput

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeSourceConfigurationOutput'>
- **Required**: Yes

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfiguration]


# PromptFlowNodeInlineConfiguration

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### templateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptTemplateConfiguration'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['CHAT', 'TEXT']
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInferenceConfiguration]


# PromptFlowNodeInlineConfigurationOutput

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### templateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptTemplateConfigurationOutput'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['CHAT', 'TEXT']
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInferenceConfigurationOutput]


# PromptFlowNodeResourceConfiguration

### promptArn
- **Type**: <class 'str'>
- **Required**: Yes


# PromptFlowNodeSourceConfiguration

### inline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeInlineConfiguration]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeResourceConfiguration]


# PromptFlowNodeSourceConfigurationOutput

### inline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeInlineConfigurationOutput]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeResourceConfiguration]


# PromptGenAiResource

### agent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptAgentResource]


# PromptInferenceConfiguration

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptModelInferenceConfigurationUnion]


# PromptInferenceConfigurationOutput

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptModelInferenceConfigurationOutput]


# PromptInferenceConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PromptInputVariable

### name
- **Type**: typing.Optional[str]


# PromptMetadataEntry

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# PromptModelInferenceConfiguration

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.Sequence[str]]

### temperature
- **Type**: typing.Optional[float]

### topP
- **Type**: typing.Optional[float]


# PromptModelInferenceConfigurationOutput

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.List[str]]

### temperature
- **Type**: typing.Optional[float]

### topP
- **Type**: typing.Optional[float]


# PromptModelInferenceConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PromptOverrideConfiguration

### promptConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptConfiguration]
- **Required**: Yes

### overrideLambda
- **Type**: typing.Optional[str]


# PromptOverrideConfigurationOutput

### promptConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptConfigurationOutput]
- **Required**: Yes

### overrideLambda
- **Type**: typing.Optional[str]


# PromptOverrideConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PromptSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PromptTemplateConfiguration

### chat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ChatPromptTemplateConfigurationUnion]

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.TextPromptTemplateConfigurationUnion]


# PromptTemplateConfigurationOutput

### chat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ChatPromptTemplateConfigurationOutput]

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.TextPromptTemplateConfigurationOutput]


# PromptTemplateConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PromptVariant

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptTemplateConfigurationUnion'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['CHAT', 'TEXT']
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### genAiResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptGenAiResource]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInferenceConfigurationUnion]

### metadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptMetadataEntry]]

### modelId
- **Type**: typing.Optional[str]


# PromptVariantOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptTemplateConfigurationOutput'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['CHAT', 'TEXT']
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### genAiResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptGenAiResource]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInferenceConfigurationOutput]

### metadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptMetadataEntry]]

### modelId
- **Type**: typing.Optional[str]


# PromptVariantUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueryGenerationColumn

### description
- **Type**: typing.Optional[str]

### inclusion
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### name
- **Type**: typing.Optional[str]


# QueryGenerationConfiguration

### executionTimeoutSeconds
- **Type**: typing.Optional[int]

### generationContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationContext]


# QueryGenerationConfigurationOutput

### executionTimeoutSeconds
- **Type**: typing.Optional[int]

### generationContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationContextOutput]


# QueryGenerationContext

### curatedQueries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.CuratedQuery]]

### tables
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationTable]]


# QueryGenerationContextOutput

### curatedQueries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.CuratedQuery]]

### tables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationTableOutput]]


# QueryGenerationTable

### name
- **Type**: <class 'str'>
- **Required**: Yes

### columns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationColumn]]

### description
- **Type**: typing.Optional[str]

### inclusion
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]


# QueryGenerationTableOutput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationColumn]]

### description
- **Type**: typing.Optional[str]

### inclusion
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]


# RdsConfiguration

### credentialsSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### fieldMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RdsFieldMapping'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes


# RdsFieldMapping

### metadataField
- **Type**: <class 'str'>
- **Required**: Yes

### primaryKeyField
- **Type**: <class 'str'>
- **Required**: Yes

### textField
- **Type**: <class 'str'>
- **Required**: Yes

### vectorField
- **Type**: <class 'str'>
- **Required**: Yes


# RedisEnterpriseCloudConfiguration

### credentialsSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### fieldMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RedisEnterpriseCloudFieldMapping'>
- **Required**: Yes

### vectorIndexName
- **Type**: <class 'str'>
- **Required**: Yes


# RedisEnterpriseCloudFieldMapping

### metadataField
- **Type**: <class 'str'>
- **Required**: Yes

### textField
- **Type**: <class 'str'>
- **Required**: Yes

### vectorField
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftConfiguration

### queryEngineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RedshiftQueryEngineConfiguration'>
- **Required**: Yes

### storageConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.RedshiftQueryEngineStorageConfiguration]
- **Required**: Yes

### queryGenerationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationConfiguration]


# RedshiftConfigurationOutput

### queryEngineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RedshiftQueryEngineConfiguration'>
- **Required**: Yes

### storageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.RedshiftQueryEngineStorageConfigurationOutput]
- **Required**: Yes

### queryGenerationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationConfigurationOutput]


# RedshiftProvisionedAuthConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RedshiftProvisionedConfiguration

### authConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RedshiftProvisionedAuthConfiguration'>
- **Required**: Yes

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftQueryEngineAwsDataCatalogStorageConfiguration

### tableNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutput

### tableNames
- **Type**: typing.List[str]
- **Required**: Yes


# RedshiftQueryEngineConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RedshiftQueryEngineRedshiftStorageConfiguration

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftQueryEngineStorageConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RedshiftQueryEngineStorageConfigurationOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RedshiftServerlessAuthConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RedshiftServerlessConfiguration

### authConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RedshiftServerlessAuthConfiguration'>
- **Required**: Yes

### workgroupArn
- **Type**: <class 'str'>
- **Required**: Yes


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


# RetrievalFlowNodeConfiguration

### serviceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RetrievalFlowNodeServiceConfiguration'>
- **Required**: Yes


# RetrievalFlowNodeS3Configuration

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# RetrievalFlowNodeServiceConfiguration

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.RetrievalFlowNodeS3Configuration]


# S3Content

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.S3Location'>
- **Required**: Yes


# S3DataSourceConfiguration

### bucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### bucketOwnerAccountId
- **Type**: typing.Optional[str]

### inclusionPrefixes
- **Type**: typing.Optional[typing.Sequence[str]]


# S3DataSourceConfigurationOutput

### bucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### bucketOwnerAccountId
- **Type**: typing.Optional[str]

### inclusionPrefixes
- **Type**: typing.Optional[typing.List[str]]


# S3Identifier

### s3BucketName
- **Type**: typing.Optional[str]

### s3ObjectKey
- **Type**: typing.Optional[str]


# S3Location

### uri
- **Type**: <class 'str'>
- **Required**: Yes


# SalesforceCrawlerConfiguration

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CrawlFilterConfiguration]


# SalesforceCrawlerConfigurationOutput

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CrawlFilterConfigurationOutput]


# SalesforceDataSourceConfiguration

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.SalesforceSourceConfiguration'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SalesforceCrawlerConfiguration]


# SalesforceDataSourceConfigurationOutput

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.SalesforceSourceConfiguration'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SalesforceCrawlerConfigurationOutput]


# SalesforceSourceConfiguration

### authType
- **Type**: typing.Literal['OAUTH2_CLIENT_CREDENTIALS']
- **Required**: Yes

### credentialsSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### hostUrl
- **Type**: <class 'str'>
- **Required**: Yes


# SeedUrl

### url
- **Type**: typing.Optional[str]


# SemanticChunkingConfiguration

### breakpointPercentileThreshold
- **Type**: <class 'int'>
- **Required**: Yes

### bufferSize
- **Type**: <class 'int'>
- **Required**: Yes

### maxTokens
- **Type**: <class 'int'>
- **Required**: Yes


# ServerSideEncryptionConfiguration

### kmsKeyArn
- **Type**: typing.Optional[str]


# SessionSummaryConfiguration

### maxRecentSessions
- **Type**: typing.Optional[int]


# SharePointCrawlerConfiguration

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CrawlFilterConfiguration]


# SharePointCrawlerConfigurationOutput

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CrawlFilterConfigurationOutput]


# SharePointDataSourceConfiguration

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.SharePointSourceConfiguration'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SharePointCrawlerConfiguration]


# SharePointDataSourceConfigurationOutput

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.SharePointSourceConfigurationOutput'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SharePointCrawlerConfigurationOutput]


# SharePointSourceConfiguration

### authType
- **Type**: typing.Literal['OAUTH2_CLIENT_CREDENTIALS', 'OAUTH2_SHAREPOINT_APP_ONLY_CLIENT_CREDENTIALS']
- **Required**: Yes

### credentialsSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### hostType
- **Type**: typing.Literal['ONLINE']
- **Required**: Yes

### siteUrls
- **Type**: typing.Sequence[str]
- **Required**: Yes

### tenantId
- **Type**: typing.Optional[str]


# SharePointSourceConfigurationOutput

### authType
- **Type**: typing.Literal['OAUTH2_CLIENT_CREDENTIALS', 'OAUTH2_SHAREPOINT_APP_ONLY_CLIENT_CREDENTIALS']
- **Required**: Yes

### credentialsSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### hostType
- **Type**: typing.Literal['ONLINE']
- **Required**: Yes

### siteUrls
- **Type**: typing.List[str]
- **Required**: Yes

### tenantId
- **Type**: typing.Optional[str]


# SpecificToolChoice

### name
- **Type**: <class 'str'>
- **Required**: Yes


# StartIngestionJobRequest

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# StartIngestionJobResponse

### ingestionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# StopIngestionJobRequest

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionJobId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# StopIngestionJobResponse

### ingestionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJob'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# StorageConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StorageFlowNodeConfiguration

### serviceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageFlowNodeServiceConfiguration'>
- **Required**: Yes


# StorageFlowNodeS3Configuration

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# StorageFlowNodeServiceConfiguration

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageFlowNodeS3Configuration]


# SupplementalDataStorageConfiguration

### storageLocations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.SupplementalDataStorageLocation]
- **Required**: Yes


# SupplementalDataStorageConfigurationOutput

### storageLocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.SupplementalDataStorageLocation]
- **Required**: Yes


# SupplementalDataStorageLocation

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SystemContentBlock

### cachePoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CachePointBlock]

### text
- **Type**: typing.Optional[str]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TextContentDoc

### data
- **Type**: <class 'str'>
- **Required**: Yes


# TextPromptTemplateConfiguration

### text
- **Type**: <class 'str'>
- **Required**: Yes

### cachePoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CachePointBlock]

### inputVariables
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInputVariable]]


# TextPromptTemplateConfigurationOutput

### text
- **Type**: <class 'str'>
- **Required**: Yes

### cachePoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CachePointBlock]

### inputVariables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInputVariable]]


# TextPromptTemplateConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Tool

### cachePoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CachePointBlock]

### toolSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolSpecificationUnion]


# ToolChoiceOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolChoiceUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolConfiguration

### tools
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolUnion]
- **Required**: Yes

### toolChoice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolChoiceUnion]


# ToolConfigurationOutput

### tools
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolOutput]
- **Required**: Yes

### toolChoice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolChoiceOutput]


# ToolConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolInputSchema

### json
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ToolInputSchemaOutput

### json
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ToolInputSchemaUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolOutput

### cachePoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CachePointBlock]

### toolSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolSpecificationOutput]


# ToolSpecification

### inputSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolInputSchemaUnion'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ToolSpecificationOutput

### inputSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolInputSchemaOutput'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ToolSpecificationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Transformation

### stepToApply
- **Type**: typing.Literal['POST_CHUNKING']
- **Required**: Yes

### transformationFunction
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.TransformationFunction'>
- **Required**: Yes


# TransformationFunction

### transformationLambdaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.TransformationLambdaConfiguration'>
- **Required**: Yes


# TransformationLambdaConfiguration

### lambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# UnfulfilledNodeInputFlowValidationDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnknownConnectionConditionFlowValidationDetails

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# UnknownConnectionSourceFlowValidationDetails

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# UnknownConnectionSourceOutputFlowValidationDetails

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# UnknownConnectionTargetFlowValidationDetails

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# UnknownConnectionTargetInputFlowValidationDetails

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# UnknownNodeInputFlowValidationDetails

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnknownNodeOutputFlowValidationDetails

### node
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: <class 'str'>
- **Required**: Yes


# UnreachableNodeFlowValidationDetails

### node
- **Type**: <class 'str'>
- **Required**: Yes


# UnsatisfiedConnectionConditionsFlowValidationDetails

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAgentActionGroupRequest

### actionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### actionGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### actionGroupExecutor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ActionGroupExecutor]

### actionGroupState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### apiSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.APISchema]

### description
- **Type**: typing.Optional[str]

### functionSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FunctionSchemaUnion]

### parentActionGroupSignature
- **Type**: typing.Optional[typing.Literal['AMAZON.CodeInterpreter', 'AMAZON.UserInput', 'ANTHROPIC.Bash', 'ANTHROPIC.Computer', 'ANTHROPIC.TextEditor']]

### parentActionGroupSignatureParams
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateAgentActionGroupResponse

### agentActionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentActionGroup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAgentAliasRequest

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentAliasName
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### routingConfiguration
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasRoutingConfigurationListItem]]


# UpdateAgentAliasResponse

### agentAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAlias'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAgentCollaboratorRequest

### agentDescriptor
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentDescriptor'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### collaborationInstruction
- **Type**: <class 'str'>
- **Required**: Yes

### collaboratorId
- **Type**: <class 'str'>
- **Required**: Yes

### collaboratorName
- **Type**: <class 'str'>
- **Required**: Yes

### relayConversationHistory
- **Type**: typing.Optional[typing.Literal['DISABLED', 'TO_COLLABORATOR']]


# UpdateAgentCollaboratorResponse

### agentCollaborator
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentCollaborator'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAgentKnowledgeBaseRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### knowledgeBaseState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateAgentKnowledgeBaseResponse

### agentKnowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentKnowledgeBase'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAgentRequest

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentName
- **Type**: <class 'str'>
- **Required**: Yes

### agentResourceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### foundationModel
- **Type**: <class 'str'>
- **Required**: Yes

### agentCollaboration
- **Type**: typing.Optional[typing.Literal['DISABLED', 'SUPERVISOR', 'SUPERVISOR_ROUTER']]

### customOrchestration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomOrchestration]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfiguration]

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### instruction
- **Type**: typing.Optional[str]

### memoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MemoryConfigurationUnion]

### orchestrationType
- **Type**: typing.Optional[typing.Literal['CUSTOM_ORCHESTRATION', 'DEFAULT']]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptOverrideConfigurationUnion]


# UpdateAgentResponse

### agent
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.Agent'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDataSourceRequest

### dataSourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceConfigurationUnion'>
- **Required**: Yes

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### dataDeletionPolicy
- **Type**: typing.Optional[typing.Literal['DELETE', 'RETAIN']]

### description
- **Type**: typing.Optional[str]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ServerSideEncryptionConfiguration]

### vectorIngestionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.VectorIngestionConfigurationUnion]


# UpdateDataSourceResponse

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSource'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFlowAliasRequest

### aliasIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### routingConfiguration
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowAliasRoutingConfigurationListItem]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateFlowRequest

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### definition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDefinitionUnion]

### description
- **Type**: typing.Optional[str]


# UpdateKnowledgeBaseRequest

### knowledgeBaseConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseConfigurationUnion'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### storageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageConfiguration]


# UpdateKnowledgeBaseResponse

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBase'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePromptRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### promptIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### defaultVariant
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### variants
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptVariantUnion]]


# UrlConfiguration

### seedUrls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.SeedUrl]]


# UrlConfigurationOutput

### seedUrls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.SeedUrl]]


# ValidateFlowDefinitionRequest

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDefinitionUnion'>
- **Required**: Yes


# ValidateFlowDefinitionResponse

### validations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowValidation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadata'>
- **Required**: Yes


# VectorIngestionConfiguration

### chunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ChunkingConfiguration]

### contextEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ContextEnrichmentConfiguration]

### customTransformationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomTransformationConfiguration]

### parsingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ParsingConfiguration]


# VectorIngestionConfigurationOutput

### chunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ChunkingConfigurationOutput]

### contextEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ContextEnrichmentConfiguration]

### customTransformationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomTransformationConfigurationOutput]

### parsingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ParsingConfiguration]


# VectorIngestionConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VectorKnowledgeBaseConfiguration

### embeddingModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### embeddingModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.EmbeddingModelConfiguration]

### supplementalDataStorageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SupplementalDataStorageConfiguration]


# VectorKnowledgeBaseConfigurationOutput

### embeddingModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### embeddingModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.EmbeddingModelConfiguration]

### supplementalDataStorageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SupplementalDataStorageConfigurationOutput]


# WebCrawlerConfiguration

### crawlerLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.WebCrawlerLimits]

### exclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### inclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### scope
- **Type**: typing.Optional[typing.Literal['HOST_ONLY', 'SUBDOMAINS']]

### userAgent
- **Type**: typing.Optional[str]

### userAgentHeader
- **Type**: typing.Optional[str]


# WebCrawlerConfigurationOutput

### crawlerLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.WebCrawlerLimits]

### exclusionFilters
- **Type**: typing.Optional[typing.List[str]]

### inclusionFilters
- **Type**: typing.Optional[typing.List[str]]

### scope
- **Type**: typing.Optional[typing.Literal['HOST_ONLY', 'SUBDOMAINS']]

### userAgent
- **Type**: typing.Optional[str]

### userAgentHeader
- **Type**: typing.Optional[str]


# WebCrawlerLimits

### maxPages
- **Type**: typing.Optional[int]

### rateLimit
- **Type**: typing.Optional[int]


# WebDataSourceConfiguration

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.WebSourceConfiguration'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.WebCrawlerConfiguration]


# WebDataSourceConfigurationOutput

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.WebSourceConfigurationOutput'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.WebCrawlerConfigurationOutput]


# WebSourceConfiguration

### urlConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.UrlConfiguration'>
- **Required**: Yes


# WebSourceConfigurationOutput

### urlConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.UrlConfigurationOutput'>
- **Required**: Yes


