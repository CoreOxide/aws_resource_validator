# Bedrock Agent Classes

# APISchemaTypeDef

### payload
- **Type**: typing.Optional[str]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.S3IdentifierTypeDef]


# ActionGroupExecutorTypeDef

### customControl
- **Type**: typing.Optional[typing.Literal['RETURN_CONTROL']]


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

### parentActionSignature
- **Type**: typing.Optional[typing.Literal['AMAZON.CodeInterpreter', 'AMAZON.UserInput']]


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
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'PREPARED', 'UPDATING']
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
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'PREPARED', 'UPDATING']
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

### clientToken
- **Type**: typing.Optional[str]

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


# AssociateAgentKnowledgeBaseRequestRequestTypeDef

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

# BedrockEmbeddingModelConfigurationTypeDef

### dimensions
- **Type**: typing.Optional[int]


# BedrockFoundationModelConfigurationTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### parsingPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ParsingPromptTypeDef]


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


# CrawlFilterConfigurationOutputTypeDef

### type
- **Type**: typing.Literal['PATTERN']
- **Required**: Yes

### patternObjectFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PatternObjectFilterConfigurationOutputTypeDef]


# CrawlFilterConfigurationTypeDef

### type
- **Type**: typing.Literal['PATTERN']
- **Required**: Yes

### patternObjectFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PatternObjectFilterConfigurationTypeDef]


# CreateAgentActionGroupRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FunctionSchemaTypeDef]

### parentActionGroupSignature
- **Type**: typing.Optional[typing.Literal['AMAZON.CodeInterpreter', 'AMAZON.UserInput']]


# CreateAgentActionGroupResponseTypeDef

### agentActionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentActionGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAgentAliasRequestRequestTypeDef

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


# CreateAgentRequestRequestTypeDef

### agentName
- **Type**: <class 'str'>
- **Required**: Yes

### agentResourceRoleArn
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MemoryConfigurationTypeDef]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptOverrideConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAgentResponseTypeDef

### agent
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataSourceRequestRequestTypeDef

### dataSourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceConfigurationTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.VectorIngestionConfigurationTypeDef]


# CreateDataSourceResponseTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFlowAliasRequestRequestTypeDef

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


# CreateFlowAliasResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### flowId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### routingConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowAliasRoutingConfigurationListItemTypeDef]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFlowRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDefinitionTypeDef]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateFlowResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customerEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDefinitionOutputTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'NotPrepared', 'Prepared', 'Preparing']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFlowVersionRequestRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]


# CreateFlowVersionResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customerEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDefinitionOutputTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'NotPrepared', 'Prepared', 'Preparing']
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKnowledgeBaseRequestRequestTypeDef

### knowledgeBaseConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseConfigurationTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### roleArn
- **Type**: <class 'str'>
- **Required**: Yes

### storageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageConfigurationTypeDef'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateKnowledgeBaseResponseTypeDef

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePromptRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptVariantTypeDef, aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptVariantOutputTypeDef]]]


# CreatePromptResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customerEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### defaultVariant
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### variants
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptVariantOutputTypeDef]
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePromptVersionRequestRequestTypeDef

### promptIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePromptVersionResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customerEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### defaultVariant
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### variants
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptVariantOutputTypeDef]
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# DataSourceConfigurationOutputTypeDef

### type
- **Type**: typing.Literal['CONFLUENCE', 'S3', 'SALESFORCE', 'SHAREPOINT', 'WEB']
- **Required**: Yes

### confluenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ConfluenceDataSourceConfigurationOutputTypeDef]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.S3DataSourceConfigurationOutputTypeDef]

### salesforceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SalesforceDataSourceConfigurationOutputTypeDef]

### sharePointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SharePointDataSourceConfigurationOutputTypeDef]

### webConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.WebDataSourceConfigurationOutputTypeDef]


# DataSourceConfigurationTypeDef

### type
- **Type**: typing.Literal['CONFLUENCE', 'S3', 'SALESFORCE', 'SHAREPOINT', 'WEB']
- **Required**: Yes

### confluenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ConfluenceDataSourceConfigurationTypeDef]

### s3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.S3DataSourceConfigurationTypeDef]

### salesforceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SalesforceDataSourceConfigurationTypeDef]

### sharePointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.SharePointDataSourceConfigurationTypeDef]

### webConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.WebDataSourceConfigurationTypeDef]


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


# DeleteAgentActionGroupRequestRequestTypeDef

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


# DeleteAgentAliasRequestRequestTypeDef

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
- **Type**: typing.Literal['CREATING', 'DELETING', 'FAILED', 'PREPARED', 'UPDATING']
- **Required**: Yes

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAgentRequestRequestTypeDef

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


# DeleteAgentVersionRequestRequestTypeDef

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


# DeleteDataSourceRequestRequestTypeDef

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


# DeleteFlowAliasRequestRequestTypeDef

### aliasIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFlowAliasResponseTypeDef

### flowId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFlowRequestRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteFlowResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFlowVersionRequestRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowVersion
- **Type**: <class 'str'>
- **Required**: Yes

### skipResourceInUseCheck
- **Type**: typing.Optional[bool]


# DeleteFlowVersionResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteKnowledgeBaseRequestRequestTypeDef

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


# DeletePromptRequestRequestTypeDef

### promptIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### promptVersion
- **Type**: typing.Optional[str]


# DeletePromptResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateAgentKnowledgeBaseRequestRequestTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# EmbeddingModelConfigurationTypeDef

### bedrockEmbeddingModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.BedrockEmbeddingModelConfigurationTypeDef]


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

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### flowId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### routingConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowAliasRoutingConfigurationListItemTypeDef]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


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

### name
- **Type**: <class 'str'>
- **Required**: Yes

### source
- **Type**: <class 'str'>
- **Required**: Yes

### target
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Conditional', 'Data']
- **Required**: Yes

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowConnectionConfigurationTypeDef]


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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowNodeExtraOutputTypeDef]]


# FlowDefinitionTypeDef

### connections
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowConnectionTypeDef]]

### nodes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowNodeTypeDef]]


# FlowNodeConfigurationOutputTypeDef

### agent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentFlowNodeConfigurationTypeDef]

### collector
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ConditionFlowNodeConfigurationOutputTypeDef]

### input
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### iterator
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### knowledgeBase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseFlowNodeConfigurationTypeDef]

### lambdaFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.LambdaFunctionFlowNodeConfigurationTypeDef]

### lex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.LexFlowNodeConfigurationTypeDef]

### output
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### prompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeConfigurationOutputTypeDef]

### retrieval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.RetrievalFlowNodeConfigurationTypeDef]

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageFlowNodeConfigurationTypeDef]


# FlowNodeConfigurationTypeDef

### agent
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentFlowNodeConfigurationTypeDef]

### collector
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### condition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ConditionFlowNodeConfigurationTypeDef]

### input
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### iterator
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### knowledgeBase
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseFlowNodeConfigurationTypeDef]

### lambdaFunction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.LambdaFunctionFlowNodeConfigurationTypeDef]

### lex
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.LexFlowNodeConfigurationTypeDef]

### output
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### prompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeConfigurationTypeDef]

### retrieval
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.RetrievalFlowNodeConfigurationTypeDef]

### storage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageFlowNodeConfigurationTypeDef]


# FlowNodeExtraOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Agent', 'Collector', 'Condition', 'Input', 'Iterator', 'KnowledgeBase', 'LambdaFunction', 'Lex', 'Output', 'Prompt', 'Retrieval', 'Storage']
- **Required**: Yes

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowNodeConfigurationOutputTypeDef]

### inputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowNodeInputTypeDef]]

### outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowNodeOutputTypeDef]]


# FlowNodeInputTypeDef

### expression
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Array', 'Boolean', 'Number', 'Object', 'String']
- **Required**: Yes


# FlowNodeOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Array', 'Boolean', 'Number', 'Object', 'String']
- **Required**: Yes


# FlowNodeTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['Agent', 'Collector', 'Condition', 'Input', 'Iterator', 'KnowledgeBase', 'LambdaFunction', 'Lex', 'Output', 'Prompt', 'Retrieval', 'Storage']
- **Required**: Yes

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowNodeConfigurationTypeDef]

### inputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowNodeInputTypeDef]]

### outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowNodeOutputTypeDef]]


# FlowSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'NotPrepared', 'Prepared', 'Preparing']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# FlowValidationTypeDef

### message
- **Type**: <class 'str'>
- **Required**: Yes

### severity
- **Type**: typing.Literal['Error', 'Warning']
- **Required**: Yes


# FlowVersionSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'NotPrepared', 'Prepared', 'Preparing']
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes


# FunctionOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.bedrock_agent_classes.ParameterDetailTypeDef]]


# FunctionSchemaOutputTypeDef

### functions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FunctionOutputTypeDef]]


# FunctionSchemaTypeDef

### functions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.FunctionTypeDef]]


# FunctionTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### parameters
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.bedrock_agent_classes.ParameterDetailTypeDef]]


# GetAgentActionGroupRequestRequestTypeDef

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


# GetAgentAliasRequestRequestTypeDef

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


# GetAgentKnowledgeBaseRequestRequestTypeDef

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


# GetAgentRequestRequestTypeDef

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


# GetAgentVersionRequestRequestTypeDef

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


# GetDataSourceRequestRequestTypeDef

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


# GetFlowAliasRequestRequestTypeDef

### aliasIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetFlowAliasResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### flowId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### routingConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowAliasRoutingConfigurationListItemTypeDef]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFlowRequestRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetFlowResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customerEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDefinitionOutputTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'NotPrepared', 'Prepared', 'Preparing']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### validations
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowValidationTypeDef]
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFlowVersionRequestRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### flowVersion
- **Type**: <class 'str'>
- **Required**: Yes


# GetFlowVersionResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customerEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDefinitionOutputTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'NotPrepared', 'Prepared', 'Preparing']
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIngestionJobRequestRequestTypeDef

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


# GetKnowledgeBaseRequestRequestTypeDef

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


# GetPromptRequestRequestTypeDef

### promptIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### promptVersion
- **Type**: typing.Optional[str]


# GetPromptResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customerEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### defaultVariant
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### variants
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptVariantOutputTypeDef]
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# IngestionJobFilterTypeDef

### attribute
- **Type**: typing.Literal['STATUS']
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQ']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes


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
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS', 'STARTING']
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
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'IN_PROGRESS', 'STARTING']
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


# IntermediateStorageTypeDef

### s3Location
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.S3LocationTypeDef'>
- **Required**: Yes


# KnowledgeBaseConfigurationTypeDef

### type
- **Type**: typing.Literal['VECTOR']
- **Required**: Yes

### vectorKnowledgeBaseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.VectorKnowledgeBaseConfigurationTypeDef]


# KnowledgeBaseFlowNodeConfigurationTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

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
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseConfigurationTypeDef'>
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

### storageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageConfigurationTypeDef'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### failureReasons
- **Type**: typing.Optional[typing.List[str]]


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


# ListAgentActionGroupsRequestListAgentActionGroupsPaginateTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListAgentActionGroupsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAgentAliasesRequestListAgentAliasesPaginateTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListAgentAliasesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAgentKnowledgeBasesRequestListAgentKnowledgeBasesPaginateTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### agentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListAgentKnowledgeBasesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAgentVersionsRequestListAgentVersionsPaginateTypeDef

### agentId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListAgentVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAgentsRequestListAgentsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListAgentsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAgentsResponseTypeDef

### agentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListDataSourcesRequestListDataSourcesPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListDataSourcesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFlowAliasesRequestListFlowAliasesPaginateTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListFlowAliasesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFlowVersionsRequestListFlowVersionsPaginateTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListFlowVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFlowsRequestListFlowsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListFlowsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListFlowsResponseTypeDef

### flowSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIngestionJobsRequestListIngestionJobsPaginateTypeDef

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


# ListIngestionJobsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListKnowledgeBasesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListKnowledgeBasesResponseTypeDef

### knowledgeBaseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPromptsRequestListPromptsPaginateTypeDef

### promptIdentifier
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PaginatorConfigTypeDef]


# ListPromptsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### promptIdentifier
- **Type**: typing.Optional[str]


# ListPromptsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### promptSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# MemoryConfigurationOutputTypeDef

### enabledMemoryTypes
- **Type**: typing.List[typing.Literal['SESSION_SUMMARY']]
- **Required**: Yes

### storageDays
- **Type**: typing.Optional[int]


# MemoryConfigurationTypeDef

### enabledMemoryTypes
- **Type**: typing.Sequence[typing.Literal['SESSION_SUMMARY']]
- **Required**: Yes

### storageDays
- **Type**: typing.Optional[int]


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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParameterDetailTypeDef

### type
- **Type**: typing.Literal['array', 'boolean', 'integer', 'number', 'string']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### required
- **Type**: typing.Optional[bool]


# ParsingConfigurationTypeDef

### parsingStrategy
- **Type**: typing.Literal['BEDROCK_FOUNDATION_MODEL']
- **Required**: Yes

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


# PrepareAgentRequestRequestTypeDef

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


# PrepareFlowRequestRequestTypeDef

### flowIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# PrepareFlowResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'NotPrepared', 'Prepared', 'Preparing']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PromptConfigurationOutputTypeDef

### basePromptTemplate
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
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE_RESPONSE_GENERATION', 'ORCHESTRATION', 'POST_PROCESSING', 'PRE_PROCESSING']]


# PromptConfigurationTypeDef

### basePromptTemplate
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
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE_RESPONSE_GENERATION', 'ORCHESTRATION', 'POST_PROCESSING', 'PRE_PROCESSING']]


# PromptFlowNodeConfigurationOutputTypeDef

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeSourceConfigurationOutputTypeDef'>
- **Required**: Yes


# PromptFlowNodeConfigurationTypeDef

### sourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptFlowNodeSourceConfigurationTypeDef'>
- **Required**: Yes


# PromptFlowNodeInlineConfigurationOutputTypeDef

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### templateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptTemplateConfigurationOutputTypeDef'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['TEXT']
- **Required**: Yes

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
- **Type**: typing.Literal['TEXT']
- **Required**: Yes

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


# PromptInferenceConfigurationOutputTypeDef

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptModelInferenceConfigurationOutputTypeDef]


# PromptInferenceConfigurationTypeDef

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptModelInferenceConfigurationTypeDef]


# PromptInputVariableTypeDef

### name
- **Type**: typing.Optional[str]


# PromptModelInferenceConfigurationOutputTypeDef

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.List[str]]

### temperature
- **Type**: typing.Optional[float]

### topK
- **Type**: typing.Optional[int]

### topP
- **Type**: typing.Optional[float]


# PromptModelInferenceConfigurationTypeDef

### maxTokens
- **Type**: typing.Optional[int]

### stopSequences
- **Type**: typing.Optional[typing.Sequence[str]]

### temperature
- **Type**: typing.Optional[float]

### topK
- **Type**: typing.Optional[int]

### topP
- **Type**: typing.Optional[float]


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


# PromptSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# PromptTemplateConfigurationOutputTypeDef

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.TextPromptTemplateConfigurationOutputTypeDef]


# PromptTemplateConfigurationTypeDef

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.TextPromptTemplateConfigurationTypeDef]


# PromptVariantOutputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['TEXT']
- **Required**: Yes

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInferenceConfigurationOutputTypeDef]

### modelId
- **Type**: typing.Optional[str]

### templateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptTemplateConfigurationOutputTypeDef]


# PromptVariantTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['TEXT']
- **Required**: Yes

### inferenceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInferenceConfigurationTypeDef]

### modelId
- **Type**: typing.Optional[str]

### templateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptTemplateConfigurationTypeDef]


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
- **Type**: typing.Literal['OAUTH2_CLIENT_CREDENTIALS']
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
- **Type**: typing.Literal['OAUTH2_CLIENT_CREDENTIALS']
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


# StartIngestionJobRequestRequestTypeDef

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


# StorageConfigurationTypeDef

### type
- **Type**: typing.Literal['MONGO_DB_ATLAS', 'OPENSEARCH_SERVERLESS', 'PINECONE', 'RDS', 'REDIS_ENTERPRISE_CLOUD']
- **Required**: Yes

### mongoDbAtlasConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MongoDbAtlasConfigurationTypeDef]

### opensearchServerlessConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.OpenSearchServerlessConfigurationTypeDef]

### pineconeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PineconeConfigurationTypeDef]

### rdsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.RdsConfigurationTypeDef]

### redisEnterpriseCloudConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.RedisEnterpriseCloudConfigurationTypeDef]


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


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TextPromptTemplateConfigurationOutputTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes

### inputVariables
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInputVariableTypeDef]]


# TextPromptTemplateConfigurationTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes

### inputVariables
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptInputVariableTypeDef]]


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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAgentActionGroupRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FunctionSchemaTypeDef]

### parentActionGroupSignature
- **Type**: typing.Optional[typing.Literal['AMAZON.CodeInterpreter', 'AMAZON.UserInput']]


# UpdateAgentActionGroupResponseTypeDef

### agentActionGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentActionGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAgentAliasRequestRequestTypeDef

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


# UpdateAgentKnowledgeBaseRequestRequestTypeDef

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


# UpdateAgentRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.MemoryConfigurationTypeDef]

### promptOverrideConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptOverrideConfigurationTypeDef]


# UpdateAgentResponseTypeDef

### agent
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.AgentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDataSourceRequestRequestTypeDef

### dataSourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceConfigurationTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.VectorIngestionConfigurationTypeDef]


# UpdateDataSourceResponseTypeDef

### dataSource
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.DataSourceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFlowAliasRequestRequestTypeDef

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


# UpdateFlowAliasResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### flowId
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### routingConfiguration
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowAliasRoutingConfigurationListItemTypeDef]
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFlowRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDefinitionTypeDef]

### description
- **Type**: typing.Optional[str]


# UpdateFlowResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customerEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### definition
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.FlowDefinitionOutputTypeDef'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### executionRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['Failed', 'NotPrepared', 'Prepared', 'Preparing']
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateKnowledgeBaseRequestRequestTypeDef

### knowledgeBaseConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseConfigurationTypeDef'>
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

### storageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.StorageConfigurationTypeDef'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# UpdateKnowledgeBaseResponseTypeDef

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.KnowledgeBaseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePromptRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptVariantTypeDef, aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptVariantOutputTypeDef]]]


# UpdatePromptResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### customerEncryptionKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### defaultVariant
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### updatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### variants
- **Type**: typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.PromptVariantOutputTypeDef]
- **Required**: Yes

### version
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.bedrock_agent_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UrlConfigurationOutputTypeDef

### seedUrls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.bedrock_agent_classes.SeedUrlTypeDef]]


# UrlConfigurationTypeDef

### seedUrls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.bedrock_agent_classes.SeedUrlTypeDef]]


# VectorIngestionConfigurationOutputTypeDef

### chunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ChunkingConfigurationOutputTypeDef]

### customTransformationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomTransformationConfigurationOutputTypeDef]

### parsingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ParsingConfigurationTypeDef]


# VectorIngestionConfigurationTypeDef

### chunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ChunkingConfigurationTypeDef]

### customTransformationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.CustomTransformationConfigurationTypeDef]

### parsingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.ParsingConfigurationTypeDef]


# VectorKnowledgeBaseConfigurationTypeDef

### embeddingModelArn
- **Type**: <class 'str'>
- **Required**: Yes

### embeddingModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.EmbeddingModelConfigurationTypeDef]


# WebCrawlerConfigurationOutputTypeDef

### crawlerLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.WebCrawlerLimitsTypeDef]

### exclusionFilters
- **Type**: typing.Optional[typing.List[str]]

### inclusionFilters
- **Type**: typing.Optional[typing.List[str]]

### scope
- **Type**: typing.Optional[typing.Literal['HOST_ONLY', 'SUBDOMAINS']]


# WebCrawlerConfigurationTypeDef

### crawlerLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.bedrock_agent_classes.WebCrawlerLimitsTypeDef]

### exclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### inclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### scope
- **Type**: typing.Optional[typing.Literal['HOST_ONLY', 'SUBDOMAINS']]


# WebCrawlerLimitsTypeDef

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


