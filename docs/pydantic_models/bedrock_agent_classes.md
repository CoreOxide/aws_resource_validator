# Bedrock Agent Classes

# APISchemaTypeDef

### payload
- **Type**: typing.Optional[str]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.S3IdentifierTypeDef]


# ActionGroupExecutorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ActionGroupSummaryTypeDef

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


# AgentActionGroupTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ActionGroupExecutorTypeDef]

### apiSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.APISchemaTypeDef]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### functionSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FunctionSchemaOutputTypeDef]

### parentActionGroupSignatureParams
- **Type**: typing.Optional[typing.Dict[str, str]]

### parentActionSignature
- **Type**: typing.Optional[typing.Literal['AMAZON.CodeInterpreter', 'AMAZON.UserInput', 'ANTHROPIC.Bash', 'ANTHROPIC.Computer', 'ANTHROPIC.TextEditor']]


# AgentAliasHistoryEventTypeDef

### endDate
- **Type**: typing.Optional[datetime.datetime]

### routingConfiguration
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasRoutingConfigurationListItemTypeDef]]

### startDate
- **Type**: typing.Optional[datetime.datetime]


# AgentAliasRoutingConfigurationListItemTypeDef

### agentVersion
- **Type**: typing.Optional[str]

### provisionedThroughput
- **Type**: typing.Optional[str]


# AgentAliasSummaryTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasRoutingConfigurationListItemTypeDef]]


# AgentAliasTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasRoutingConfigurationListItemTypeDef]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### agentAliasHistoryEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasHistoryEventTypeDef]]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]


# AgentCollaboratorSummaryTypeDef

### agentDescriptor
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentDescriptorTypeDef'>
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


# AgentCollaboratorTypeDef

### agentDescriptor
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentDescriptorTypeDef'>
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


# AgentDescriptorTypeDef

### aliasArn
- **Type**: typing.Optional[str]


# AgentFlowNodeConfigurationTypeDef

### agentAliasArn
- **Type**: <class 'str'>
- **Required**: Yes


# AgentKnowledgeBaseSummaryTypeDef

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


# AgentKnowledgeBaseTypeDef

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


# AgentSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfigurationTypeDef]

### latestAgentVersion
- **Type**: typing.Optional[str]


# AgentTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomOrchestrationTypeDef]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]

### foundationModel
- **Type**: typing.Optional[str]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfigurationTypeDef]

### instruction
- **Type**: typing.Optional[str]

### memoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MemoryConfigurationOutputTypeDef]

### orchestrationType
- **Type**: typing.Optional[typing.Literal['CUSTOM_ORCHESTRATION', 'DEFAULT']]

### preparedAt
- **Type**: typing.Optional[datetime.datetime]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptOverrideConfigurationOutputTypeDef]

### recommendedActions
- **Type**: typing.Optional[typing.List[str]]


# AgentVersionSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfigurationTypeDef]


# AgentVersionTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfigurationTypeDef]

### instruction
- **Type**: typing.Optional[str]

### memoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MemoryConfigurationOutputTypeDef]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptOverrideConfigurationOutputTypeDef]

### recommendedActions
- **Type**: typing.Optional[typing.List[str]]


# AssociateAgentCollaboratorRequestTypeDef

### agentDescriptor
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentDescriptorTypeDef'>
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


# AssociateAgentCollaboratorResponseTypeDef

### agentCollaborator
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentCollaboratorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateAgentKnowledgeBaseRequestTypeDef

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


# AssociateAgentKnowledgeBaseResponseTypeDef

### agentKnowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentKnowledgeBaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BedrockDataAutomationConfigurationTypeDef

### parsingModality
- **Type**: typing.Optional[typing.Literal['MULTIMODAL']]


# BedrockEmbeddingModelConfigurationTypeDef

### dimensions
- **Type**: typing.Optional[int]

### embeddingDataType
- **Type**: typing.Optional[typing.Literal['BINARY', 'FLOAT32']]


# BedrockFoundationModelConfigurationTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### parsingModality
- **Type**: typing.Optional[typing.Literal['MULTIMODAL']]

### parsingPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ParsingPromptTypeDef]


# BedrockFoundationModelContextEnrichmentConfigurationTypeDef

### enrichmentStrategyConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.EnrichmentStrategyConfigurationTypeDef'>
- **Required**: Yes

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes


# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ByteContentDocTypeDef

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.BlobTypeDef'>
- **Required**: Yes

### mimeType
- **Type**: <class 'str'>
- **Required**: Yes


# CachePointBlockTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChatPromptTemplateConfigurationOutputTypeDef

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.MessageOutputTypeDef]
- **Required**: Yes

### inputVariables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInputVariableTypeDef]]

### system
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.SystemContentBlockTypeDef]]

### toolConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolConfigurationOutputTypeDef]


# ChatPromptTemplateConfigurationTypeDef

### messages
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.MessageUnionTypeDef]
- **Required**: Yes

### inputVariables
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInputVariableTypeDef]]

### system
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.SystemContentBlockTypeDef]]

### toolConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolConfigurationUnionTypeDef]


# ChatPromptTemplateConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChunkingConfigurationOutputTypeDef

### chunkingStrategy
- **Type**: typing.Literal['FIXED_SIZE', 'HIERARCHICAL', 'NONE', 'SEMANTIC']
- **Required**: Yes

### fixedSizeChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FixedSizeChunkingConfigurationTypeDef]

### hierarchicalChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.HierarchicalChunkingConfigurationOutputTypeDef]

### semanticChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SemanticChunkingConfigurationTypeDef]


# ChunkingConfigurationTypeDef

### chunkingStrategy
- **Type**: typing.Literal['FIXED_SIZE', 'HIERARCHICAL', 'NONE', 'SEMANTIC']
- **Required**: Yes

### fixedSizeChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FixedSizeChunkingConfigurationTypeDef]

### hierarchicalChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.HierarchicalChunkingConfigurationTypeDef]

### semanticChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SemanticChunkingConfigurationTypeDef]


# ConditionFlowNodeConfigurationOutputTypeDef

### conditions
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowConditionTypeDef]
- **Required**: Yes


# ConditionFlowNodeConfigurationTypeDef

### conditions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowConditionTypeDef]
- **Required**: Yes


# ConfluenceCrawlerConfigurationOutputTypeDef

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CrawlFilterConfigurationOutputTypeDef]


# ConfluenceCrawlerConfigurationTypeDef

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CrawlFilterConfigurationTypeDef]


# ConfluenceDataSourceConfigurationOutputTypeDef

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ConfluenceSourceConfigurationTypeDef'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ConfluenceCrawlerConfigurationOutputTypeDef]


# ConfluenceDataSourceConfigurationTypeDef

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ConfluenceSourceConfigurationTypeDef'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ConfluenceCrawlerConfigurationTypeDef]


# ConfluenceSourceConfigurationTypeDef

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


# ContentBlockTypeDef

### cachePoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CachePointBlockTypeDef]

### text
- **Type**: typing.Optional[str]


# ContextEnrichmentConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CrawlFilterConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CrawlFilterConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAgentActionGroupRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ActionGroupExecutorTypeDef]

### actionGroupState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### apiSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.APISchemaTypeDef]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### functionSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FunctionSchemaUnionTypeDef]

### parentActionGroupSignature
- **Type**: typing.Optional[typing.Literal['AMAZON.CodeInterpreter', 'AMAZON.UserInput', 'ANTHROPIC.Bash', 'ANTHROPIC.Computer', 'ANTHROPIC.TextEditor']]

### parentActionGroupSignatureParams
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAgentActionGroupResponseTypeDef

### agentActionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentActionGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAgentAliasRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasRoutingConfigurationListItemTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAgentAliasResponseTypeDef

### agentAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAgentRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomOrchestrationTypeDef]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### foundationModel
- **Type**: typing.Optional[str]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfigurationTypeDef]

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### instruction
- **Type**: typing.Optional[str]

### memoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MemoryConfigurationUnionTypeDef]

### orchestrationType
- **Type**: typing.Optional[typing.Literal['CUSTOM_ORCHESTRATION', 'DEFAULT']]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptOverrideConfigurationUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAgentResponseTypeDef

### agent
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataSourceRequestTypeDef

### dataSourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceConfigurationUnionTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ServerSideEncryptionConfigurationTypeDef]

### vectorIngestionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.VectorIngestionConfigurationUnionTypeDef]


# CreateDataSourceResponseTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFlowAliasRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### routingConfiguration
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowAliasRoutingConfigurationListItemTypeDef]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFlowRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDefinitionUnionTypeDef]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFlowVersionRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateKnowledgeBaseRequestTypeDef

### knowledgeBaseConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseConfigurationUnionTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateKnowledgeBaseResponseTypeDef

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePromptRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptVariantUnionTypeDef]]


# CreatePromptVersionRequestTypeDef

### promptIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CuratedQueryTypeDef

### naturalLanguage
- **Type**: <class 'str'>
- **Required**: Yes

### sql
- **Type**: <class 'str'>
- **Required**: Yes


# CustomContentTypeDef

### customDocumentIdentifier
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomDocumentIdentifierTypeDef'>
- **Required**: Yes

### sourceType
- **Type**: typing.Literal['IN_LINE', 'S3_LOCATION']
- **Required**: Yes

### inlineContent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.InlineContentTypeDef]

### s3Location
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomS3LocationTypeDef]


# CustomDocumentIdentifierTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CustomOrchestrationTypeDef

### executor
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.OrchestrationExecutorTypeDef]


# CustomS3LocationTypeDef

### uri
- **Type**: <class 'str'>
- **Required**: Yes

### bucketOwnerAccountId
- **Type**: typing.Optional[str]


# CustomTransformationConfigurationOutputTypeDef

### intermediateStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.IntermediateStorageTypeDef'>
- **Required**: Yes

### transformations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.TransformationTypeDef]
- **Required**: Yes


# CustomTransformationConfigurationTypeDef

### intermediateStorage
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.IntermediateStorageTypeDef'>
- **Required**: Yes

### transformations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.TransformationTypeDef]
- **Required**: Yes


# CyclicConnectionFlowValidationDetailsTypeDef

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# DataSourceConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DataSourceSummaryTypeDef

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


# DataSourceTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dataSourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceConfigurationOutputTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ServerSideEncryptionConfigurationTypeDef]

### vectorIngestionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.VectorIngestionConfigurationOutputTypeDef]


# DeleteAgentActionGroupRequestTypeDef

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


# DeleteAgentAliasRequestTypeDef

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAgentAliasResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAgentRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteAgentResponseTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentStatus
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'NOT_PREPARED', 'PREPARED', 'PREPARING', 'UPDATING', 'VERSIONING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAgentVersionRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteAgentVersionResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDataSourceRequestTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataSourceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFlowAliasRequestTypeDef

### aliasIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFlowRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteFlowVersionRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowVersion
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteKnowledgeBaseDocumentsRequestTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### documentIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.DocumentIdentifierTypeDef]
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# DeleteKnowledgeBaseDocumentsResponseTypeDef

### documentDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseDocumentDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteKnowledgeBaseRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKnowledgeBaseResponseTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'DELETE_UNSUCCESSFUL', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePromptRequestTypeDef

### promptIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### promptVersion
- **Type**: typing.Optional[str]


# DisassociateAgentCollaboratorRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### collaboratorId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateAgentKnowledgeBaseRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DocumentContentTypeDef

### dataSourceType
- **Type**: typing.Literal['CUSTOM', 'S3']
- **Required**: Yes

### custom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomContentTypeDef]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.S3ContentTypeDef]


# DocumentIdentifierTypeDef

### dataSourceType
- **Type**: typing.Literal['CUSTOM', 'S3']
- **Required**: Yes

### custom
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomDocumentIdentifierTypeDef]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.S3LocationTypeDef]


# DocumentMetadataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DuplicateConditionExpressionFlowValidationDetailsTypeDef

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### node
- **Type**: <class 'str'>
- **Required**: Yes


# DuplicateConnectionsFlowValidationDetailsTypeDef

### source
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes


# EmbeddingModelConfigurationTypeDef

### bedrockEmbeddingModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.BedrockEmbeddingModelConfigurationTypeDef]


# EnrichmentStrategyConfigurationTypeDef

### method
- **Type**: typing.Literal['CHUNK_ENTITY_EXTRACTION']
- **Required**: Yes


# FixedSizeChunkingConfigurationTypeDef

### maxTokens
- **Type**: <class 'int'>
- **Required**: Yes

### overlapPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# FlowAliasRoutingConfigurationListItemTypeDef

### flowVersion
- **Type**: typing.Optional[str]


# FlowAliasSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowConditionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### expression
- **Type**: typing.Optional[str]


# FlowConditionalConnectionConfigurationTypeDef

### condition
- **Type**: <class 'str'>
- **Required**: Yes


# FlowConnectionConfigurationTypeDef

### conditional
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowConditionalConnectionConfigurationTypeDef]

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDataConnectionConfigurationTypeDef]


# FlowConnectionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowDataConnectionConfigurationTypeDef

### sourceOutput
- **Type**: <class 'str'>
- **Required**: Yes

### targetInput
- **Type**: <class 'str'>
- **Required**: Yes


# FlowDefinitionOutputTypeDef

### connections
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowConnectionTypeDef]]

### nodes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowNodeExtraTypeDef]]


# FlowDefinitionTypeDef

### connections
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowConnectionTypeDef]]

### nodes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowNodeTypeDef]]


# FlowDefinitionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowNodeExtraTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowNodeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowValidationDetailsTypeDef

### cyclicConnection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CyclicConnectionFlowValidationDetailsTypeDef]

### duplicateConditionExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.DuplicateConditionExpressionFlowValidationDetailsTypeDef]

### duplicateConnections
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.DuplicateConnectionsFlowValidationDetailsTypeDef]

### incompatibleConnectionDataType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.IncompatibleConnectionDataTypeFlowValidationDetailsTypeDef]

### malformedConditionExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MalformedConditionExpressionFlowValidationDetailsTypeDef]

### malformedNodeInputExpression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MalformedNodeInputExpressionFlowValidationDetailsTypeDef]

### mismatchedNodeInputType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MismatchedNodeInputTypeFlowValidationDetailsTypeDef]

### mismatchedNodeOutputType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MismatchedNodeOutputTypeFlowValidationDetailsTypeDef]

### missingConnectionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MissingConnectionConfigurationFlowValidationDetailsTypeDef]

### missingDefaultCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MissingDefaultConditionFlowValidationDetailsTypeDef]

### missingEndingNodes
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### missingNodeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MissingNodeConfigurationFlowValidationDetailsTypeDef]

### missingNodeInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MissingNodeInputFlowValidationDetailsTypeDef]

### missingNodeOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MissingNodeOutputFlowValidationDetailsTypeDef]

### missingStartingNodes
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### multipleNodeInputConnections
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MultipleNodeInputConnectionsFlowValidationDetailsTypeDef]

### unfulfilledNodeInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnfulfilledNodeInputFlowValidationDetailsTypeDef]

### unknownConnectionCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownConnectionConditionFlowValidationDetailsTypeDef]

### unknownConnectionSource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownConnectionSourceFlowValidationDetailsTypeDef]

### unknownConnectionSourceOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownConnectionSourceOutputFlowValidationDetailsTypeDef]

### unknownConnectionTarget
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownConnectionTargetFlowValidationDetailsTypeDef]

### unknownConnectionTargetInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownConnectionTargetInputFlowValidationDetailsTypeDef]

### unknownNodeInput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownNodeInputFlowValidationDetailsTypeDef]

### unknownNodeOutput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnknownNodeOutputFlowValidationDetailsTypeDef]

### unreachableNode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnreachableNodeFlowValidationDetailsTypeDef]

### unsatisfiedConnectionConditions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.UnsatisfiedConnectionConditionsFlowValidationDetailsTypeDef]

### unspecified
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# FlowValidationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FlowVersionSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_classes.ParameterDetailTypeDef]]

### requireConfirmation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# FunctionSchemaOutputTypeDef

### functions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FunctionOutputTypeDef]]


# FunctionSchemaTypeDef

### functions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FunctionTypeDef]]


# FunctionSchemaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FunctionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.bedrock_agent_classes.ParameterDetailTypeDef]]

### requireConfirmation
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# GetAgentActionGroupRequestTypeDef

### actionGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentActionGroupResponseTypeDef

### agentActionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentActionGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAgentAliasRequestTypeDef

### agentAliasId
- **Type**: <class 'str'>
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentAliasResponseTypeDef

### agentAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAgentCollaboratorRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### collaboratorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentCollaboratorResponseTypeDef

### agentCollaborator
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentCollaboratorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAgentKnowledgeBaseRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentKnowledgeBaseResponseTypeDef

### agentKnowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentKnowledgeBaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAgentRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentResponseTypeDef

### agent
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAgentVersionRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetAgentVersionResponseTypeDef

### agentVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataSourceRequestTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataSourceResponseTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFlowAliasRequestTypeDef

### aliasIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetFlowRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetFlowVersionRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetIngestionJobRequestTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionJobId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetIngestionJobResponseTypeDef

### ingestionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKnowledgeBaseDocumentsRequestTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### documentIdentifiers
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.DocumentIdentifierTypeDef]
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKnowledgeBaseDocumentsResponseTypeDef

### documentDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseDocumentDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKnowledgeBaseRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKnowledgeBaseResponseTypeDef

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPromptRequestTypeDef

### promptIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### promptVersion
- **Type**: typing.Optional[str]


# GuardrailConfigurationTypeDef

### guardrailIdentifier
- **Type**: typing.Optional[str]

### guardrailVersion
- **Type**: typing.Optional[str]


# HierarchicalChunkingConfigurationOutputTypeDef

### levelConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.HierarchicalChunkingLevelConfigurationTypeDef]
- **Required**: Yes

### overlapTokens
- **Type**: <class 'int'>
- **Required**: Yes


# HierarchicalChunkingConfigurationTypeDef

### levelConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.HierarchicalChunkingLevelConfigurationTypeDef]
- **Required**: Yes

### overlapTokens
- **Type**: <class 'int'>
- **Required**: Yes


# HierarchicalChunkingLevelConfigurationTypeDef

### maxTokens
- **Type**: <class 'int'>
- **Required**: Yes


# IncompatibleConnectionDataTypeFlowValidationDetailsTypeDef

### connection
- **Type**: <class 'str'>
- **Required**: Yes


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


# IngestKnowledgeBaseDocumentsRequestTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### documents
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseDocumentTypeDef]
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# IngestKnowledgeBaseDocumentsResponseTypeDef

### documentDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseDocumentDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IngestionJobFilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IngestionJobSortByTypeDef

### attribute
- **Type**: typing.Literal['STARTED_AT', 'STATUS']
- **Required**: Yes

### order
- **Type**: typing.Literal['ASCENDING', 'DESCENDING']
- **Required**: Yes


# IngestionJobStatisticsTypeDef

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


# IngestionJobSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobStatisticsTypeDef]


# IngestionJobTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobStatisticsTypeDef]


# InlineContentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IntermediateStorageTypeDef

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.S3LocationTypeDef'>
- **Required**: Yes


# KendraKnowledgeBaseConfigurationTypeDef

### kendraIndexArn
- **Type**: <class 'str'>
- **Required**: Yes


# KnowledgeBaseConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KnowledgeBaseConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KnowledgeBaseDocumentDetailTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### identifier
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DocumentIdentifierTypeDef'>
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


# KnowledgeBaseDocumentTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DocumentContentTypeDef'>
- **Required**: Yes

### metadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.DocumentMetadataTypeDef]


# KnowledgeBaseFlowNodeConfigurationTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfigurationTypeDef]

### modelId
- **Type**: typing.Optional[str]


# KnowledgeBaseSummaryTypeDef

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


# KnowledgeBaseTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseConfigurationOutputTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageConfigurationTypeDef]


# LambdaFunctionFlowNodeConfigurationTypeDef

### lambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# LexFlowNodeConfigurationTypeDef

### botAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### localeId
- **Type**: <class 'str'>
- **Required**: Yes


# ListAgentActionGroupsRequestPaginateTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListAgentActionGroupsRequestTypeDef

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


# ListAgentActionGroupsResponseTypeDef

### actionGroupSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.ActionGroupSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAgentAliasesRequestPaginateTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListAgentAliasesRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAgentAliasesResponseTypeDef

### agentAliasSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAgentCollaboratorsRequestPaginateTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListAgentCollaboratorsRequestTypeDef

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


# ListAgentCollaboratorsResponseTypeDef

### agentCollaboratorSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentCollaboratorSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAgentKnowledgeBasesRequestPaginateTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListAgentKnowledgeBasesRequestTypeDef

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


# ListAgentKnowledgeBasesResponseTypeDef

### agentKnowledgeBaseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentKnowledgeBaseSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAgentVersionsRequestPaginateTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListAgentVersionsRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAgentVersionsResponseTypeDef

### agentVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAgentsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListAgentsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAgentsResponseTypeDef

### agentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourcesRequestPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListDataSourcesRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDataSourcesResponseTypeDef

### dataSourceSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFlowAliasesRequestPaginateTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListFlowAliasesRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFlowAliasesResponseTypeDef

### flowAliasSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowAliasSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFlowVersionsRequestPaginateTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListFlowVersionsRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFlowVersionsResponseTypeDef

### flowVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListFlowsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListFlowsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFlowsResponseTypeDef

### flowSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIngestionJobsRequestPaginateTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobFilterTypeDef]]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobSortByTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListIngestionJobsRequestTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobFilterTypeDef]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobSortByTypeDef]


# ListIngestionJobsResponseTypeDef

### ingestionJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKnowledgeBaseDocumentsRequestPaginateTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListKnowledgeBaseDocumentsRequestTypeDef

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


# ListKnowledgeBaseDocumentsResponseTypeDef

### documentDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseDocumentDetailTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKnowledgeBasesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListKnowledgeBasesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListKnowledgeBasesResponseTypeDef

### knowledgeBaseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPromptsRequestPaginateTypeDef

### promptIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListPromptsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### promptIdentifier
- **Type**: typing.Optional[str]


# ListPromptsResponseTypeDef

### promptSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MalformedConditionExpressionFlowValidationDetailsTypeDef

### cause
- **Type**: <class 'str'>
- **Required**: Yes

### condition
- **Type**: <class 'str'>
- **Required**: Yes

### node
- **Type**: <class 'str'>
- **Required**: Yes


# MalformedNodeInputExpressionFlowValidationDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MemoryConfigurationOutputTypeDef

### enabledMemoryTypes
- **Type**: typing.List[typing.Literal['SESSION_SUMMARY']]
- **Required**: Yes

### sessionSummaryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SessionSummaryConfigurationTypeDef]

### storageDays
- **Type**: typing.Optional[int]


# MemoryConfigurationTypeDef

### enabledMemoryTypes
- **Type**: typing.Sequence[typing.Literal['SESSION_SUMMARY']]
- **Required**: Yes

### sessionSummaryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SessionSummaryConfigurationTypeDef]

### storageDays
- **Type**: typing.Optional[int]


# MemoryConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MessageOutputTypeDef

### content
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.ContentBlockTypeDef]
- **Required**: Yes

### role
- **Type**: typing.Literal['assistant', 'user']
- **Required**: Yes


# MessageTypeDef

### content
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.ContentBlockTypeDef]
- **Required**: Yes

### role
- **Type**: typing.Literal['assistant', 'user']
- **Required**: Yes


# MessageUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MetadataAttributeTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.MetadataAttributeValueTypeDef'>
- **Required**: Yes


# MetadataAttributeValueTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MismatchedNodeInputTypeFlowValidationDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MismatchedNodeOutputTypeFlowValidationDetailsTypeDef

### expectedType
- **Type**: typing.Literal['Array', 'Boolean', 'Number', 'Object', 'String']
- **Required**: Yes

### node
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: <class 'str'>
- **Required**: Yes


# MissingConnectionConfigurationFlowValidationDetailsTypeDef

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# MissingDefaultConditionFlowValidationDetailsTypeDef

### node
- **Type**: <class 'str'>
- **Required**: Yes


# MissingNodeConfigurationFlowValidationDetailsTypeDef

### node
- **Type**: <class 'str'>
- **Required**: Yes


# MissingNodeInputFlowValidationDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MissingNodeOutputFlowValidationDetailsTypeDef

### node
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: <class 'str'>
- **Required**: Yes


# MongoDbAtlasConfigurationTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.MongoDbAtlasFieldMappingTypeDef'>
- **Required**: Yes

### vectorIndexName
- **Type**: <class 'str'>
- **Required**: Yes

### endpointServiceName
- **Type**: typing.Optional[str]


# MongoDbAtlasFieldMappingTypeDef

### metadataField
- **Type**: <class 'str'>
- **Required**: Yes

### textField
- **Type**: <class 'str'>
- **Required**: Yes

### vectorField
- **Type**: <class 'str'>
- **Required**: Yes


# MultipleNodeInputConnectionsFlowValidationDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NeptuneAnalyticsConfigurationTypeDef

### fieldMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.NeptuneAnalyticsFieldMappingTypeDef'>
- **Required**: Yes

### graphArn
- **Type**: <class 'str'>
- **Required**: Yes


# NeptuneAnalyticsFieldMappingTypeDef

### metadataField
- **Type**: <class 'str'>
- **Required**: Yes

### textField
- **Type**: <class 'str'>
- **Required**: Yes


# OpenSearchServerlessConfigurationTypeDef

### collectionArn
- **Type**: <class 'str'>
- **Required**: Yes

### fieldMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.OpenSearchServerlessFieldMappingTypeDef'>
- **Required**: Yes

### vectorIndexName
- **Type**: <class 'str'>
- **Required**: Yes


# OpenSearchServerlessFieldMappingTypeDef

### metadataField
- **Type**: <class 'str'>
- **Required**: Yes

### textField
- **Type**: <class 'str'>
- **Required**: Yes

### vectorField
- **Type**: <class 'str'>
- **Required**: Yes


# OrchestrationExecutorTypeDef

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

# ParsingConfigurationTypeDef

### parsingStrategy
- **Type**: typing.Literal['BEDROCK_DATA_AUTOMATION', 'BEDROCK_FOUNDATION_MODEL']
- **Required**: Yes

### bedrockDataAutomationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.BedrockDataAutomationConfigurationTypeDef]

### bedrockFoundationModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.BedrockFoundationModelConfigurationTypeDef]


# ParsingPromptTypeDef

### parsingPromptText
- **Type**: <class 'str'>
- **Required**: Yes


# PatternObjectFilterConfigurationOutputTypeDef

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PatternObjectFilterOutputTypeDef]
- **Required**: Yes


# PatternObjectFilterConfigurationTypeDef

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PatternObjectFilterTypeDef]
- **Required**: Yes


# PatternObjectFilterOutputTypeDef

### objectType
- **Type**: <class 'str'>
- **Required**: Yes

### exclusionFilters
- **Type**: typing.Optional[typing.List[str]]

### inclusionFilters
- **Type**: typing.Optional[typing.List[str]]


# PatternObjectFilterTypeDef

### objectType
- **Type**: <class 'str'>
- **Required**: Yes

### exclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### inclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]


# PineconeConfigurationTypeDef

### connectionString
- **Type**: <class 'str'>
- **Required**: Yes

### credentialsSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### fieldMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PineconeFieldMappingTypeDef'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[str]


# PineconeFieldMappingTypeDef

### metadataField
- **Type**: <class 'str'>
- **Required**: Yes

### textField
- **Type**: <class 'str'>
- **Required**: Yes


# PrepareAgentRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes


# PrepareAgentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PrepareFlowRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PromptAgentResourceTypeDef

### agentIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PromptConfigurationOutputTypeDef

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### basePromptTemplate
- **Type**: typing.Optional[str]

### foundationModel
- **Type**: typing.Optional[str]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.InferenceConfigurationOutputTypeDef]

### parserMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### promptCreationMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### promptState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### promptType
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE_RESPONSE_GENERATION', 'MEMORY_SUMMARIZATION', 'ORCHESTRATION', 'POST_PROCESSING', 'PRE_PROCESSING']]


# PromptConfigurationTypeDef

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### basePromptTemplate
- **Type**: typing.Optional[str]

### foundationModel
- **Type**: typing.Optional[str]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.InferenceConfigurationTypeDef]

### parserMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### promptCreationMode
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'OVERRIDDEN']]

### promptState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### promptType
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE_RESPONSE_GENERATION', 'MEMORY_SUMMARIZATION', 'ORCHESTRATION', 'POST_PROCESSING', 'PRE_PROCESSING']]


# PromptFlowNodeConfigurationOutputTypeDef

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeSourceConfigurationOutputTypeDef'>
- **Required**: Yes

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfigurationTypeDef]


# PromptFlowNodeConfigurationTypeDef

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeSourceConfigurationTypeDef'>
- **Required**: Yes

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfigurationTypeDef]


# PromptFlowNodeInlineConfigurationOutputTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### templateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptTemplateConfigurationOutputTypeDef'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['CHAT', 'TEXT']
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInferenceConfigurationOutputTypeDef]


# PromptFlowNodeInlineConfigurationTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### templateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptTemplateConfigurationTypeDef'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['CHAT', 'TEXT']
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInferenceConfigurationTypeDef]


# PromptFlowNodeResourceConfigurationTypeDef

### promptArn
- **Type**: <class 'str'>
- **Required**: Yes


# PromptFlowNodeSourceConfigurationOutputTypeDef

### inline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeInlineConfigurationOutputTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeResourceConfigurationTypeDef]


# PromptFlowNodeSourceConfigurationTypeDef

### inline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeInlineConfigurationTypeDef]

### resource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeResourceConfigurationTypeDef]


# PromptGenAiResourceTypeDef

### agent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptAgentResourceTypeDef]


# PromptInferenceConfigurationOutputTypeDef

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptModelInferenceConfigurationOutputTypeDef]


# PromptInferenceConfigurationTypeDef

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptModelInferenceConfigurationUnionTypeDef]


# PromptInferenceConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PromptInputVariableTypeDef

### name
- **Type**: typing.Optional[str]


# PromptMetadataEntryTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# PromptModelInferenceConfigurationOutputTypeDef

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.List[str]]

### temperature
- **Type**: typing.Optional[float]

### topP
- **Type**: typing.Optional[float]


# PromptModelInferenceConfigurationTypeDef

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.Sequence[str]]

### temperature
- **Type**: typing.Optional[float]

### topP
- **Type**: typing.Optional[float]


# PromptModelInferenceConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PromptOverrideConfigurationOutputTypeDef

### promptConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptConfigurationOutputTypeDef]
- **Required**: Yes

### overrideLambda
- **Type**: typing.Optional[str]


# PromptOverrideConfigurationTypeDef

### promptConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptConfigurationTypeDef]
- **Required**: Yes

### overrideLambda
- **Type**: typing.Optional[str]


# PromptOverrideConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PromptSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PromptTemplateConfigurationOutputTypeDef

### chat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ChatPromptTemplateConfigurationOutputTypeDef]

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.TextPromptTemplateConfigurationOutputTypeDef]


# PromptTemplateConfigurationTypeDef

### chat
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ChatPromptTemplateConfigurationUnionTypeDef]

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.TextPromptTemplateConfigurationUnionTypeDef]


# PromptTemplateConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PromptVariantOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptTemplateConfigurationOutputTypeDef'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['CHAT', 'TEXT']
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### genAiResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptGenAiResourceTypeDef]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInferenceConfigurationOutputTypeDef]

### metadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptMetadataEntryTypeDef]]

### modelId
- **Type**: typing.Optional[str]


# PromptVariantTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptTemplateConfigurationUnionTypeDef'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['CHAT', 'TEXT']
- **Required**: Yes

### additionalModelRequestFields
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### genAiResource
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptGenAiResourceTypeDef]

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInferenceConfigurationUnionTypeDef]

### metadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptMetadataEntryTypeDef]]

### modelId
- **Type**: typing.Optional[str]


# PromptVariantUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QueryGenerationColumnTypeDef

### description
- **Type**: typing.Optional[str]

### inclusion
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]

### name
- **Type**: typing.Optional[str]


# QueryGenerationConfigurationOutputTypeDef

### executionTimeoutSeconds
- **Type**: typing.Optional[int]

### generationContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationContextOutputTypeDef]


# QueryGenerationConfigurationTypeDef

### executionTimeoutSeconds
- **Type**: typing.Optional[int]

### generationContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationContextTypeDef]


# QueryGenerationContextOutputTypeDef

### curatedQueries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.CuratedQueryTypeDef]]

### tables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationTableOutputTypeDef]]


# QueryGenerationContextTypeDef

### curatedQueries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.CuratedQueryTypeDef]]

### tables
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationTableTypeDef]]


# QueryGenerationTableOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### columns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationColumnTypeDef]]

### description
- **Type**: typing.Optional[str]

### inclusion
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]


# QueryGenerationTableTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### columns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationColumnTypeDef]]

### description
- **Type**: typing.Optional[str]

### inclusion
- **Type**: typing.Optional[typing.Literal['EXCLUDE', 'INCLUDE']]


# RdsConfigurationTypeDef

### credentialsSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes

### fieldMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RdsFieldMappingTypeDef'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tableName
- **Type**: <class 'str'>
- **Required**: Yes


# RdsFieldMappingTypeDef

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


# RedisEnterpriseCloudConfigurationTypeDef

### credentialsSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### fieldMapping
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RedisEnterpriseCloudFieldMappingTypeDef'>
- **Required**: Yes

### vectorIndexName
- **Type**: <class 'str'>
- **Required**: Yes


# RedisEnterpriseCloudFieldMappingTypeDef

### metadataField
- **Type**: <class 'str'>
- **Required**: Yes

### textField
- **Type**: <class 'str'>
- **Required**: Yes

### vectorField
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftConfigurationOutputTypeDef

### queryEngineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RedshiftQueryEngineConfigurationTypeDef'>
- **Required**: Yes

### storageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.RedshiftQueryEngineStorageConfigurationOutputTypeDef]
- **Required**: Yes

### queryGenerationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationConfigurationOutputTypeDef]


# RedshiftConfigurationTypeDef

### queryEngineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RedshiftQueryEngineConfigurationTypeDef'>
- **Required**: Yes

### storageConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.RedshiftQueryEngineStorageConfigurationTypeDef]
- **Required**: Yes

### queryGenerationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.QueryGenerationConfigurationTypeDef]


# RedshiftProvisionedAuthConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RedshiftProvisionedConfigurationTypeDef

### authConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RedshiftProvisionedAuthConfigurationTypeDef'>
- **Required**: Yes

### clusterIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftQueryEngineAwsDataCatalogStorageConfigurationOutputTypeDef

### tableNames
- **Type**: typing.List[str]
- **Required**: Yes


# RedshiftQueryEngineAwsDataCatalogStorageConfigurationTypeDef

### tableNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RedshiftQueryEngineConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RedshiftQueryEngineRedshiftStorageConfigurationTypeDef

### databaseName
- **Type**: <class 'str'>
- **Required**: Yes


# RedshiftQueryEngineStorageConfigurationOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RedshiftQueryEngineStorageConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RedshiftServerlessAuthConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RedshiftServerlessConfigurationTypeDef

### authConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RedshiftServerlessAuthConfigurationTypeDef'>
- **Required**: Yes

### workgroupArn
- **Type**: <class 'str'>
- **Required**: Yes


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


# RetrievalFlowNodeConfigurationTypeDef

### serviceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.RetrievalFlowNodeServiceConfigurationTypeDef'>
- **Required**: Yes


# RetrievalFlowNodeS3ConfigurationTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# RetrievalFlowNodeServiceConfigurationTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.RetrievalFlowNodeS3ConfigurationTypeDef]


# S3ContentTypeDef

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.S3LocationTypeDef'>
- **Required**: Yes


# S3DataSourceConfigurationOutputTypeDef

### bucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### bucketOwnerAccountId
- **Type**: typing.Optional[str]

### inclusionPrefixes
- **Type**: typing.Optional[typing.List[str]]


# S3DataSourceConfigurationTypeDef

### bucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### bucketOwnerAccountId
- **Type**: typing.Optional[str]

### inclusionPrefixes
- **Type**: typing.Optional[typing.Sequence[str]]


# S3IdentifierTypeDef

### s3BucketName
- **Type**: typing.Optional[str]

### s3ObjectKey
- **Type**: typing.Optional[str]


# S3LocationTypeDef

### uri
- **Type**: <class 'str'>
- **Required**: Yes


# SalesforceCrawlerConfigurationOutputTypeDef

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CrawlFilterConfigurationOutputTypeDef]


# SalesforceCrawlerConfigurationTypeDef

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CrawlFilterConfigurationTypeDef]


# SalesforceDataSourceConfigurationOutputTypeDef

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.SalesforceSourceConfigurationTypeDef'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SalesforceCrawlerConfigurationOutputTypeDef]


# SalesforceDataSourceConfigurationTypeDef

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.SalesforceSourceConfigurationTypeDef'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SalesforceCrawlerConfigurationTypeDef]


# SalesforceSourceConfigurationTypeDef

### authType
- **Type**: typing.Literal['OAUTH2_CLIENT_CREDENTIALS']
- **Required**: Yes

### credentialsSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### hostUrl
- **Type**: <class 'str'>
- **Required**: Yes


# SeedUrlTypeDef

### url
- **Type**: typing.Optional[str]


# SemanticChunkingConfigurationTypeDef

### breakpointPercentileThreshold
- **Type**: <class 'int'>
- **Required**: Yes

### bufferSize
- **Type**: <class 'int'>
- **Required**: Yes

### maxTokens
- **Type**: <class 'int'>
- **Required**: Yes


# ServerSideEncryptionConfigurationTypeDef

### kmsKeyArn
- **Type**: typing.Optional[str]


# SessionSummaryConfigurationTypeDef

### maxRecentSessions
- **Type**: typing.Optional[int]


# SharePointCrawlerConfigurationOutputTypeDef

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CrawlFilterConfigurationOutputTypeDef]


# SharePointCrawlerConfigurationTypeDef

### filterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CrawlFilterConfigurationTypeDef]


# SharePointDataSourceConfigurationOutputTypeDef

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.SharePointSourceConfigurationOutputTypeDef'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SharePointCrawlerConfigurationOutputTypeDef]


# SharePointDataSourceConfigurationTypeDef

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.SharePointSourceConfigurationTypeDef'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SharePointCrawlerConfigurationTypeDef]


# SharePointSourceConfigurationOutputTypeDef

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


# SharePointSourceConfigurationTypeDef

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


# SpecificToolChoiceTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes


# StartIngestionJobRequestTypeDef

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


# StartIngestionJobResponseTypeDef

### ingestionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopIngestionJobRequestTypeDef

### dataSourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ingestionJobId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# StopIngestionJobResponseTypeDef

### ingestionJob
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.IngestionJobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StorageConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StorageFlowNodeConfigurationTypeDef

### serviceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageFlowNodeServiceConfigurationTypeDef'>
- **Required**: Yes


# StorageFlowNodeS3ConfigurationTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# StorageFlowNodeServiceConfigurationTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageFlowNodeS3ConfigurationTypeDef]


# SupplementalDataStorageConfigurationOutputTypeDef

### storageLocations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.SupplementalDataStorageLocationTypeDef]
- **Required**: Yes


# SupplementalDataStorageConfigurationTypeDef

### storageLocations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.SupplementalDataStorageLocationTypeDef]
- **Required**: Yes


# SupplementalDataStorageLocationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SystemContentBlockTypeDef

### cachePoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CachePointBlockTypeDef]

### text
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TextContentDocTypeDef

### data
- **Type**: <class 'str'>
- **Required**: Yes


# TextPromptTemplateConfigurationOutputTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes

### cachePoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CachePointBlockTypeDef]

### inputVariables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInputVariableTypeDef]]


# TextPromptTemplateConfigurationTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes

### cachePoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CachePointBlockTypeDef]

### inputVariables
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInputVariableTypeDef]]


# TextPromptTemplateConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolChoiceOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolChoiceUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolConfigurationOutputTypeDef

### tools
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolOutputTypeDef]
- **Required**: Yes

### toolChoice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolChoiceOutputTypeDef]


# ToolConfigurationTypeDef

### tools
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolUnionTypeDef]
- **Required**: Yes

### toolChoice
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolChoiceUnionTypeDef]


# ToolConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolInputSchemaOutputTypeDef

### json
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# ToolInputSchemaTypeDef

### json
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# ToolInputSchemaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolOutputTypeDef

### cachePoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CachePointBlockTypeDef]

### toolSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolSpecificationOutputTypeDef]


# ToolSpecificationOutputTypeDef

### inputSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolInputSchemaOutputTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ToolSpecificationTypeDef

### inputSchema
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolInputSchemaUnionTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ToolSpecificationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ToolTypeDef

### cachePoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CachePointBlockTypeDef]

### toolSpec
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ToolSpecificationUnionTypeDef]


# ToolUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TransformationFunctionTypeDef

### transformationLambdaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.TransformationLambdaConfigurationTypeDef'>
- **Required**: Yes


# TransformationLambdaConfigurationTypeDef

### lambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# TransformationTypeDef

### stepToApply
- **Type**: typing.Literal['POST_CHUNKING']
- **Required**: Yes

### transformationFunction
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.TransformationFunctionTypeDef'>
- **Required**: Yes


# UnfulfilledNodeInputFlowValidationDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnknownConnectionConditionFlowValidationDetailsTypeDef

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# UnknownConnectionSourceFlowValidationDetailsTypeDef

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# UnknownConnectionSourceOutputFlowValidationDetailsTypeDef

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# UnknownConnectionTargetFlowValidationDetailsTypeDef

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# UnknownConnectionTargetInputFlowValidationDetailsTypeDef

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# UnknownNodeInputFlowValidationDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UnknownNodeOutputFlowValidationDetailsTypeDef

### node
- **Type**: <class 'str'>
- **Required**: Yes

### output
- **Type**: <class 'str'>
- **Required**: Yes


# UnreachableNodeFlowValidationDetailsTypeDef

### node
- **Type**: <class 'str'>
- **Required**: Yes


# UnsatisfiedConnectionConditionsFlowValidationDetailsTypeDef

### connection
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAgentActionGroupRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ActionGroupExecutorTypeDef]

### actionGroupState
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### apiSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.APISchemaTypeDef]

### description
- **Type**: typing.Optional[str]

### functionSchema
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FunctionSchemaUnionTypeDef]

### parentActionGroupSignature
- **Type**: typing.Optional[typing.Literal['AMAZON.CodeInterpreter', 'AMAZON.UserInput', 'ANTHROPIC.Bash', 'ANTHROPIC.Computer', 'ANTHROPIC.TextEditor']]

### parentActionGroupSignatureParams
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateAgentActionGroupResponseTypeDef

### agentActionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentActionGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAgentAliasRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasRoutingConfigurationListItemTypeDef]]


# UpdateAgentAliasResponseTypeDef

### agentAlias
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentAliasTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAgentCollaboratorRequestTypeDef

### agentDescriptor
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentDescriptorTypeDef'>
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


# UpdateAgentCollaboratorResponseTypeDef

### agentCollaborator
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentCollaboratorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAgentKnowledgeBaseRequestTypeDef

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


# UpdateAgentKnowledgeBaseResponseTypeDef

### agentKnowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentKnowledgeBaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAgentRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomOrchestrationTypeDef]

### customerEncryptionKeyArn
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### guardrailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.GuardrailConfigurationTypeDef]

### idleSessionTTLInSeconds
- **Type**: typing.Optional[int]

### instruction
- **Type**: typing.Optional[str]

### memoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MemoryConfigurationUnionTypeDef]

### orchestrationType
- **Type**: typing.Optional[typing.Literal['CUSTOM_ORCHESTRATION', 'DEFAULT']]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptOverrideConfigurationUnionTypeDef]


# UpdateAgentResponseTypeDef

### agent
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDataSourceRequestTypeDef

### dataSourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceConfigurationUnionTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ServerSideEncryptionConfigurationTypeDef]

### vectorIngestionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.VectorIngestionConfigurationUnionTypeDef]


# UpdateDataSourceResponseTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFlowAliasRequestTypeDef

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowAliasRoutingConfigurationListItemTypeDef]
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateFlowRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDefinitionUnionTypeDef]

### description
- **Type**: typing.Optional[str]


# UpdateKnowledgeBaseRequestTypeDef

### knowledgeBaseConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseConfigurationUnionTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageConfigurationTypeDef]


# UpdateKnowledgeBaseResponseTypeDef

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePromptRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptVariantUnionTypeDef]]


# UrlConfigurationOutputTypeDef

### seedUrls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.SeedUrlTypeDef]]


# UrlConfigurationTypeDef

### seedUrls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.SeedUrlTypeDef]]


# ValidateFlowDefinitionRequestTypeDef

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDefinitionUnionTypeDef'>
- **Required**: Yes


# ValidateFlowDefinitionResponseTypeDef

### validations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowValidationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VectorIngestionConfigurationOutputTypeDef

### chunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ChunkingConfigurationOutputTypeDef]

### contextEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ContextEnrichmentConfigurationTypeDef]

### customTransformationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomTransformationConfigurationOutputTypeDef]

### parsingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ParsingConfigurationTypeDef]


# VectorIngestionConfigurationTypeDef

### chunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ChunkingConfigurationTypeDef]

### contextEnrichmentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ContextEnrichmentConfigurationTypeDef]

### customTransformationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomTransformationConfigurationTypeDef]

### parsingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ParsingConfigurationTypeDef]


# VectorIngestionConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VectorKnowledgeBaseConfigurationOutputTypeDef

### embeddingModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### embeddingModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.EmbeddingModelConfigurationTypeDef]

### supplementalDataStorageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SupplementalDataStorageConfigurationOutputTypeDef]


# VectorKnowledgeBaseConfigurationTypeDef

### embeddingModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### embeddingModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.EmbeddingModelConfigurationTypeDef]

### supplementalDataStorageConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SupplementalDataStorageConfigurationTypeDef]


# WebCrawlerConfigurationOutputTypeDef

### crawlerLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.WebCrawlerLimitsTypeDef]

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


# WebCrawlerConfigurationTypeDef

### crawlerLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.WebCrawlerLimitsTypeDef]

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


# WebCrawlerLimitsTypeDef

### maxPages
- **Type**: typing.Optional[int]

### rateLimit
- **Type**: typing.Optional[int]


# WebDataSourceConfigurationOutputTypeDef

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.WebSourceConfigurationOutputTypeDef'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.WebCrawlerConfigurationOutputTypeDef]


# WebDataSourceConfigurationTypeDef

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.WebSourceConfigurationTypeDef'>
- **Required**: Yes

### crawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.WebCrawlerConfigurationTypeDef]


# WebSourceConfigurationOutputTypeDef

### urlConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.UrlConfigurationOutputTypeDef'>
- **Required**: Yes


# WebSourceConfigurationTypeDef

### urlConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.UrlConfigurationTypeDef'>
- **Required**: Yes


