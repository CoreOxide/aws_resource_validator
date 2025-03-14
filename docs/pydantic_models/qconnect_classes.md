# Qconnect Classes

# AIAgentConfigurationDataTypeDef

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes


# AIAgentConfigurationOutputTypeDef

### answerRecommendationAIAgentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AnswerRecommendationAIAgentConfigurationOutputTypeDef]

### manualSearchAIAgentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ManualSearchAIAgentConfigurationOutputTypeDef]

### selfServiceAIAgentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SelfServiceAIAgentConfigurationOutputTypeDef]


# AIAgentConfigurationTypeDef

### answerRecommendationAIAgentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AnswerRecommendationAIAgentConfigurationTypeDef]

### manualSearchAIAgentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ManualSearchAIAgentConfigurationTypeDef]

### selfServiceAIAgentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SelfServiceAIAgentConfigurationTypeDef]


# AIAgentConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AIAgentDataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AIAgentSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AIAgentVersionSummaryTypeDef

### aiAgentSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIAgentSummaryTypeDef]

### versionNumber
- **Type**: typing.Optional[int]


# AIGuardrailContentPolicyConfigOutputTypeDef

### filtersConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailContentFilterConfigTypeDef]
- **Required**: Yes


# AIGuardrailContentPolicyConfigTypeDef

### filtersConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailContentFilterConfigTypeDef]
- **Required**: Yes


# AIGuardrailContentPolicyConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AIGuardrailContextualGroundingPolicyConfigOutputTypeDef

### filtersConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailContextualGroundingFilterConfigTypeDef]
- **Required**: Yes


# AIGuardrailContextualGroundingPolicyConfigTypeDef

### filtersConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailContextualGroundingFilterConfigTypeDef]
- **Required**: Yes


# AIGuardrailContextualGroundingPolicyConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AIGuardrailDataTypeDef

### aiGuardrailArn
- **Type**: <class 'str'>
- **Required**: Yes

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### blockedInputMessaging
- **Type**: <class 'str'>
- **Required**: Yes

### blockedOutputsMessaging
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### visibilityStatus
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### contentPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailContentPolicyConfigOutputTypeDef]

### contextualGroundingPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailContextualGroundingPolicyConfigOutputTypeDef]

### description
- **Type**: typing.Optional[str]

### modifiedTime
- **Type**: typing.Optional[datetime.datetime]

### sensitiveInformationPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailSensitiveInformationPolicyConfigOutputTypeDef]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### topicPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailTopicPolicyConfigOutputTypeDef]

### wordPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailWordPolicyConfigOutputTypeDef]


# AIGuardrailSensitiveInformationPolicyConfigOutputTypeDef

### piiEntitiesConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailPiiEntityConfigTypeDef]]

### regexesConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailRegexConfigTypeDef]]


# AIGuardrailSensitiveInformationPolicyConfigTypeDef

### piiEntitiesConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailPiiEntityConfigTypeDef]]

### regexesConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailRegexConfigTypeDef]]


# AIGuardrailSensitiveInformationPolicyConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AIGuardrailSummaryTypeDef

### aiGuardrailArn
- **Type**: <class 'str'>
- **Required**: Yes

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### visibilityStatus
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### modifiedTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AIGuardrailTopicPolicyConfigOutputTypeDef

### topicsConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailTopicConfigOutputTypeDef]
- **Required**: Yes


# AIGuardrailTopicPolicyConfigTypeDef

### topicsConfig
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailTopicConfigTypeDef]
- **Required**: Yes


# AIGuardrailTopicPolicyConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AIGuardrailVersionSummaryTypeDef

### aiGuardrailSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailSummaryTypeDef]

### versionNumber
- **Type**: typing.Optional[int]


# AIGuardrailWordPolicyConfigOutputTypeDef

### managedWordListsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailManagedWordsConfigTypeDef]]

### wordsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailWordConfigTypeDef]]


# AIGuardrailWordPolicyConfigTypeDef

### managedWordListsConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailManagedWordsConfigTypeDef]]

### wordsConfig
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.GuardrailWordConfigTypeDef]]


# AIGuardrailWordPolicyConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AIPromptDataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AIPromptSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AIPromptTemplateConfigurationTypeDef

### textFullAIPromptEditTemplateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TextFullAIPromptEditTemplateConfigurationTypeDef]


# AIPromptVersionSummaryTypeDef

### aiPromptSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIPromptSummaryTypeDef]

### versionNumber
- **Type**: typing.Optional[int]


# ActivateMessageTemplateRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# ActivateMessageTemplateResponseTypeDef

### messageTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AgentAttributesTypeDef

### firstName
- **Type**: typing.Optional[str]

### lastName
- **Type**: typing.Optional[str]


# AmazonConnectGuideAssociationDataTypeDef

### flowId
- **Type**: typing.Optional[str]


# AnswerRecommendationAIAgentConfigurationOutputTypeDef

### answerGenerationAIGuardrailId
- **Type**: typing.Optional[str]

### answerGenerationAIPromptId
- **Type**: typing.Optional[str]

### associationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.AssociationConfigurationOutputTypeDef]]

### intentLabelingGenerationAIPromptId
- **Type**: typing.Optional[str]

### locale
- **Type**: typing.Optional[str]

### queryReformulationAIPromptId
- **Type**: typing.Optional[str]


# AnswerRecommendationAIAgentConfigurationTypeDef

### answerGenerationAIGuardrailId
- **Type**: typing.Optional[str]

### answerGenerationAIPromptId
- **Type**: typing.Optional[str]

### associationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.AssociationConfigurationTypeDef]]

### intentLabelingGenerationAIPromptId
- **Type**: typing.Optional[str]

### locale
- **Type**: typing.Optional[str]

### queryReformulationAIPromptId
- **Type**: typing.Optional[str]


# AppIntegrationsConfigurationOutputTypeDef

### appIntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### objectFields
- **Type**: typing.Optional[typing.List[str]]


# AppIntegrationsConfigurationTypeDef

### appIntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### objectFields
- **Type**: typing.Optional[typing.Sequence[str]]


# AssistantAssociationDataTypeDef

### assistantArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### associationData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AssistantAssociationOutputDataTypeDef'>
- **Required**: Yes

### associationType
- **Type**: typing.Literal['KNOWLEDGE_BASE']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AssistantAssociationInputDataTypeDef

### knowledgeBaseId
- **Type**: typing.Optional[str]


# AssistantAssociationOutputDataTypeDef

### knowledgeBaseAssociation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.KnowledgeBaseAssociationDataTypeDef]


# AssistantAssociationSummaryTypeDef

### assistantArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### associationData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AssistantAssociationOutputDataTypeDef'>
- **Required**: Yes

### associationType
- **Type**: typing.Literal['KNOWLEDGE_BASE']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AssistantDataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssistantIntegrationConfigurationTypeDef

### topicIntegrationArn
- **Type**: typing.Optional[str]


# AssistantSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociationConfigurationDataOutputTypeDef

### knowledgeBaseAssociationConfigurationData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.KnowledgeBaseAssociationConfigurationDataOutputTypeDef]


# AssociationConfigurationDataTypeDef

### knowledgeBaseAssociationConfigurationData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.KnowledgeBaseAssociationConfigurationDataTypeDef]


# AssociationConfigurationOutputTypeDef

### associationConfigurationData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AssociationConfigurationDataOutputTypeDef]

### associationId
- **Type**: typing.Optional[str]

### associationType
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE']]


# AssociationConfigurationTypeDef

### associationConfigurationData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AssociationConfigurationDataTypeDef]

### associationId
- **Type**: typing.Optional[str]

### associationType
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BedrockFoundationModelConfigurationForParsingTypeDef

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### parsingPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ParsingPromptTypeDef]


# ChunkingConfigurationOutputTypeDef

### chunkingStrategy
- **Type**: typing.Literal['FIXED_SIZE', 'HIERARCHICAL', 'NONE', 'SEMANTIC']
- **Required**: Yes

### fixedSizeChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.FixedSizeChunkingConfigurationTypeDef]

### hierarchicalChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.HierarchicalChunkingConfigurationOutputTypeDef]

### semanticChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SemanticChunkingConfigurationTypeDef]


# ChunkingConfigurationTypeDef

### chunkingStrategy
- **Type**: typing.Literal['FIXED_SIZE', 'HIERARCHICAL', 'NONE', 'SEMANTIC']
- **Required**: Yes

### fixedSizeChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.FixedSizeChunkingConfigurationTypeDef]

### hierarchicalChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.HierarchicalChunkingConfigurationTypeDef]

### semanticChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SemanticChunkingConfigurationTypeDef]


# CitationSpanTypeDef

### beginOffsetInclusive
- **Type**: typing.Optional[int]

### endOffsetExclusive
- **Type**: typing.Optional[int]


# ConfigurationTypeDef

### connectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ConnectConfigurationTypeDef]


# ConnectConfigurationTypeDef

### instanceId
- **Type**: typing.Optional[str]


# ContentAssociationContentsTypeDef

### amazonConnectGuideAssociation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AmazonConnectGuideAssociationDataTypeDef]


# ContentAssociationDataTypeDef

### associationData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ContentAssociationContentsTypeDef'>
- **Required**: Yes

### associationType
- **Type**: typing.Literal['AMAZON_CONNECT_GUIDE']
- **Required**: Yes

### contentArn
- **Type**: <class 'str'>
- **Required**: Yes

### contentAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### contentAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ContentAssociationSummaryTypeDef

### associationData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ContentAssociationContentsTypeDef'>
- **Required**: Yes

### associationType
- **Type**: typing.Literal['AMAZON_CONNECT_GUIDE']
- **Required**: Yes

### contentArn
- **Type**: <class 'str'>
- **Required**: Yes

### contentAssociationArn
- **Type**: <class 'str'>
- **Required**: Yes

### contentAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ContentDataDetailsTypeDef

### rankingData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.RankingDataTypeDef'>
- **Required**: Yes

### textData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.TextDataTypeDef'>
- **Required**: Yes


# ContentDataTypeDef

### contentArn
- **Type**: <class 'str'>
- **Required**: Yes

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED']
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### urlExpiry
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### linkOutUri
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ContentFeedbackDataTypeDef

### generativeContentFeedbackData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GenerativeContentFeedbackDataTypeDef]


# ContentReferenceTypeDef

### contentArn
- **Type**: typing.Optional[str]

### contentId
- **Type**: typing.Optional[str]

### knowledgeBaseArn
- **Type**: typing.Optional[str]

### knowledgeBaseId
- **Type**: typing.Optional[str]

### referenceType
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE', 'WEB_CRAWLER']]

### sourceURL
- **Type**: typing.Optional[str]


# ContentSummaryTypeDef

### contentArn
- **Type**: <class 'str'>
- **Required**: Yes

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### revisionId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED']
- **Required**: Yes

### title
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ConversationContextTypeDef

### selfServiceConversationHistory
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.SelfServiceConversationHistoryTypeDef]
- **Required**: Yes


# ConversationStateTypeDef

### status
- **Type**: typing.Literal['CLOSED', 'PROCESSING', 'READY']
- **Required**: Yes

### reason
- **Type**: typing.Optional[typing.Literal['FAILED', 'REJECTED', 'SUCCESS']]


# CreateAIAgentResponseTypeDef

### aiAgent
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AIAgentDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAIAgentVersionRequestTypeDef

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### modifiedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TimestampTypeDef]


# CreateAIAgentVersionResponseTypeDef

### aiAgent
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AIAgentDataTypeDef'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAIGuardrailRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### blockedInputMessaging
- **Type**: <class 'str'>
- **Required**: Yes

### blockedOutputsMessaging
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### visibilityStatus
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### contentPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailContentPolicyConfigUnionTypeDef]

### contextualGroundingPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailContextualGroundingPolicyConfigUnionTypeDef]

### description
- **Type**: typing.Optional[str]

### sensitiveInformationPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailSensitiveInformationPolicyConfigUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### topicPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailTopicPolicyConfigUnionTypeDef]

### wordPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailWordPolicyConfigUnionTypeDef]


# CreateAIGuardrailResponseTypeDef

### aiGuardrail
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAIGuardrailVersionRequestTypeDef

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### modifiedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TimestampTypeDef]


# CreateAIGuardrailVersionResponseTypeDef

### aiGuardrail
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailDataTypeDef'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAIPromptResponseTypeDef

### aiPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AIPromptDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAIPromptVersionRequestTypeDef

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### modifiedTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TimestampTypeDef]


# CreateAIPromptVersionResponseTypeDef

### aiPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AIPromptDataTypeDef'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssistantAssociationRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### association
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AssistantAssociationInputDataTypeDef'>
- **Required**: Yes

### associationType
- **Type**: typing.Literal['KNOWLEDGE_BASE']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAssistantAssociationResponseTypeDef

### assistantAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AssistantAssociationDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssistantResponseTypeDef

### assistant
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AssistantDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContentAssociationRequestTypeDef

### association
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ContentAssociationContentsTypeDef'>
- **Required**: Yes

### associationType
- **Type**: typing.Literal['AMAZON_CONNECT_GUIDE']
- **Required**: Yes

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateContentAssociationResponseTypeDef

### contentAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ContentAssociationDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContentRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### metadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### overrideLinkOutUri
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### title
- **Type**: typing.Optional[str]


# CreateContentResponseTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ContentDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateKnowledgeBaseRequestTypeDef

### knowledgeBaseType
- **Type**: typing.Literal['CUSTOM', 'EXTERNAL', 'MANAGED', 'MESSAGE_TEMPLATES', 'QUICK_RESPONSES']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### renderingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.RenderingConfigurationTypeDef]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ServerSideEncryptionConfigurationTypeDef]

### sourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SourceConfigurationUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### vectorIngestionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.VectorIngestionConfigurationUnionTypeDef]


# CreateKnowledgeBaseResponseTypeDef

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.KnowledgeBaseDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMessageTemplateAttachmentRequestTypeDef

### body
- **Type**: <class 'str'>
- **Required**: Yes

### contentDisposition
- **Type**: typing.Literal['ATTACHMENT']
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# CreateMessageTemplateAttachmentResponseTypeDef

### attachment
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateAttachmentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMessageTemplateRequestTypeDef

### channelSubtype
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateContentProviderUnionTypeDef'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### defaultAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateAttributesUnionTypeDef]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GroupingConfigurationUnionTypeDef]

### language
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateMessageTemplateResponseTypeDef

### messageTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMessageTemplateVersionRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateContentSha256
- **Type**: typing.Optional[str]


# CreateMessageTemplateVersionResponseTypeDef

### messageTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ExtendedMessageTemplateDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQuickResponseRequestTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseDataProviderTypeDef'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### channels
- **Type**: typing.Optional[typing.Sequence[str]]

### clientToken
- **Type**: typing.Optional[str]

### contentType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GroupingConfigurationUnionTypeDef]

### isActive
- **Type**: typing.Optional[bool]

### language
- **Type**: typing.Optional[str]

### shortcutKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateQuickResponseResponseTypeDef

### quickResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSessionRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### aiAgentConfiguration
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE'], aws_resource_validator.pydantic_models.qconnect_classes.AIAgentConfigurationDataTypeDef]]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TagFilterUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSessionResponseTypeDef

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.SessionDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomerProfileAttributesOutputTypeDef

### accountNumber
- **Type**: typing.Optional[str]

### additionalInformation
- **Type**: typing.Optional[str]

### address1
- **Type**: typing.Optional[str]

### address2
- **Type**: typing.Optional[str]

### address3
- **Type**: typing.Optional[str]

### address4
- **Type**: typing.Optional[str]

### billingAddress1
- **Type**: typing.Optional[str]

### billingAddress2
- **Type**: typing.Optional[str]

### billingAddress3
- **Type**: typing.Optional[str]

### billingAddress4
- **Type**: typing.Optional[str]

### billingCity
- **Type**: typing.Optional[str]

### billingCountry
- **Type**: typing.Optional[str]

### billingCounty
- **Type**: typing.Optional[str]

### billingPostalCode
- **Type**: typing.Optional[str]

### billingProvince
- **Type**: typing.Optional[str]

### billingState
- **Type**: typing.Optional[str]

### birthDate
- **Type**: typing.Optional[str]

### businessEmailAddress
- **Type**: typing.Optional[str]

### businessName
- **Type**: typing.Optional[str]

### businessPhoneNumber
- **Type**: typing.Optional[str]

### city
- **Type**: typing.Optional[str]

### country
- **Type**: typing.Optional[str]

### county
- **Type**: typing.Optional[str]

### custom
- **Type**: typing.Optional[typing.Dict[str, str]]

### emailAddress
- **Type**: typing.Optional[str]

### firstName
- **Type**: typing.Optional[str]

### gender
- **Type**: typing.Optional[str]

### homePhoneNumber
- **Type**: typing.Optional[str]

### lastName
- **Type**: typing.Optional[str]

### mailingAddress1
- **Type**: typing.Optional[str]

### mailingAddress2
- **Type**: typing.Optional[str]

### mailingAddress3
- **Type**: typing.Optional[str]

### mailingAddress4
- **Type**: typing.Optional[str]

### mailingCity
- **Type**: typing.Optional[str]

### mailingCountry
- **Type**: typing.Optional[str]

### mailingCounty
- **Type**: typing.Optional[str]

### mailingPostalCode
- **Type**: typing.Optional[str]

### mailingProvince
- **Type**: typing.Optional[str]

### mailingState
- **Type**: typing.Optional[str]

### middleName
- **Type**: typing.Optional[str]

### mobilePhoneNumber
- **Type**: typing.Optional[str]

### partyType
- **Type**: typing.Optional[str]

### phoneNumber
- **Type**: typing.Optional[str]

### postalCode
- **Type**: typing.Optional[str]

### profileARN
- **Type**: typing.Optional[str]

### profileId
- **Type**: typing.Optional[str]

### province
- **Type**: typing.Optional[str]

### shippingAddress1
- **Type**: typing.Optional[str]

### shippingAddress2
- **Type**: typing.Optional[str]

### shippingAddress3
- **Type**: typing.Optional[str]

### shippingAddress4
- **Type**: typing.Optional[str]

### shippingCity
- **Type**: typing.Optional[str]

### shippingCountry
- **Type**: typing.Optional[str]

### shippingCounty
- **Type**: typing.Optional[str]

### shippingPostalCode
- **Type**: typing.Optional[str]

### shippingProvince
- **Type**: typing.Optional[str]

### shippingState
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[str]


# CustomerProfileAttributesTypeDef

### accountNumber
- **Type**: typing.Optional[str]

### additionalInformation
- **Type**: typing.Optional[str]

### address1
- **Type**: typing.Optional[str]

### address2
- **Type**: typing.Optional[str]

### address3
- **Type**: typing.Optional[str]

### address4
- **Type**: typing.Optional[str]

### billingAddress1
- **Type**: typing.Optional[str]

### billingAddress2
- **Type**: typing.Optional[str]

### billingAddress3
- **Type**: typing.Optional[str]

### billingAddress4
- **Type**: typing.Optional[str]

### billingCity
- **Type**: typing.Optional[str]

### billingCountry
- **Type**: typing.Optional[str]

### billingCounty
- **Type**: typing.Optional[str]

### billingPostalCode
- **Type**: typing.Optional[str]

### billingProvince
- **Type**: typing.Optional[str]

### billingState
- **Type**: typing.Optional[str]

### birthDate
- **Type**: typing.Optional[str]

### businessEmailAddress
- **Type**: typing.Optional[str]

### businessName
- **Type**: typing.Optional[str]

### businessPhoneNumber
- **Type**: typing.Optional[str]

### city
- **Type**: typing.Optional[str]

### country
- **Type**: typing.Optional[str]

### county
- **Type**: typing.Optional[str]

### custom
- **Type**: typing.Optional[typing.Mapping[str, str]]

### emailAddress
- **Type**: typing.Optional[str]

### firstName
- **Type**: typing.Optional[str]

### gender
- **Type**: typing.Optional[str]

### homePhoneNumber
- **Type**: typing.Optional[str]

### lastName
- **Type**: typing.Optional[str]

### mailingAddress1
- **Type**: typing.Optional[str]

### mailingAddress2
- **Type**: typing.Optional[str]

### mailingAddress3
- **Type**: typing.Optional[str]

### mailingAddress4
- **Type**: typing.Optional[str]

### mailingCity
- **Type**: typing.Optional[str]

### mailingCountry
- **Type**: typing.Optional[str]

### mailingCounty
- **Type**: typing.Optional[str]

### mailingPostalCode
- **Type**: typing.Optional[str]

### mailingProvince
- **Type**: typing.Optional[str]

### mailingState
- **Type**: typing.Optional[str]

### middleName
- **Type**: typing.Optional[str]

### mobilePhoneNumber
- **Type**: typing.Optional[str]

### partyType
- **Type**: typing.Optional[str]

### phoneNumber
- **Type**: typing.Optional[str]

### postalCode
- **Type**: typing.Optional[str]

### profileARN
- **Type**: typing.Optional[str]

### profileId
- **Type**: typing.Optional[str]

### province
- **Type**: typing.Optional[str]

### shippingAddress1
- **Type**: typing.Optional[str]

### shippingAddress2
- **Type**: typing.Optional[str]

### shippingAddress3
- **Type**: typing.Optional[str]

### shippingAddress4
- **Type**: typing.Optional[str]

### shippingCity
- **Type**: typing.Optional[str]

### shippingCountry
- **Type**: typing.Optional[str]

### shippingCounty
- **Type**: typing.Optional[str]

### shippingPostalCode
- **Type**: typing.Optional[str]

### shippingProvince
- **Type**: typing.Optional[str]

### shippingState
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[str]


# DataDetailsPaginatorTypeDef

### contentData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ContentDataDetailsTypeDef]

### generativeData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GenerativeDataDetailsPaginatorTypeDef]

### intentDetectedData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.IntentDetectedDataDetailsTypeDef]

### sourceContentData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SourceContentDataDetailsTypeDef]


# DataDetailsTypeDef

### contentData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ContentDataDetailsTypeDef]

### generativeData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GenerativeDataDetailsTypeDef]

### intentDetectedData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.IntentDetectedDataDetailsTypeDef]

### sourceContentData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SourceContentDataDetailsTypeDef]


# DataReferenceTypeDef

### contentReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ContentReferenceTypeDef]

### generativeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GenerativeReferenceTypeDef]


# DataSummaryPaginatorTypeDef

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.DataDetailsPaginatorTypeDef'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.DataReferenceTypeDef'>
- **Required**: Yes


# DataSummaryTypeDef

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.DataDetailsTypeDef'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.DataReferenceTypeDef'>
- **Required**: Yes


# DeactivateMessageTemplateRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeactivateMessageTemplateResponseTypeDef

### messageTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAIAgentRequestTypeDef

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAIAgentVersionRequestTypeDef

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteAIGuardrailRequestTypeDef

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAIGuardrailVersionRequestTypeDef

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteAIPromptRequestTypeDef

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAIPromptVersionRequestTypeDef

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteAssistantAssociationRequestTypeDef

### assistantAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssistantRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContentAssociationRequestTypeDef

### contentAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContentRequestTypeDef

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImportJobRequestTypeDef

### importJobId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKnowledgeBaseRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMessageTemplateAttachmentRequestTypeDef

### attachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMessageTemplateRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQuickResponseRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# DocumentTextTypeDef

### highlights
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.HighlightTypeDef]]

### text
- **Type**: typing.Optional[str]


# DocumentTypeDef

### contentReference
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ContentReferenceTypeDef'>
- **Required**: Yes

### excerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.DocumentTextTypeDef]

### title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.DocumentTextTypeDef]


# EmailHeaderTypeDef

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# EmailMessageTemplateContentBodyTypeDef

### html
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateBodyContentProviderTypeDef]

### plainText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateBodyContentProviderTypeDef]


# EmailMessageTemplateContentOutputTypeDef

### body
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.EmailMessageTemplateContentBodyTypeDef]

### headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.EmailHeaderTypeDef]]

### subject
- **Type**: typing.Optional[str]


# EmailMessageTemplateContentTypeDef

### body
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.EmailMessageTemplateContentBodyTypeDef]

### headers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.EmailHeaderTypeDef]]

### subject
- **Type**: typing.Optional[str]


# ExtendedMessageTemplateDataTypeDef

### channelSubtype
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateContentProviderOutputTypeDef'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### messageTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateContentSha256
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attachments
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateAttachmentTypeDef]]

### attributeTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AGENT', 'CUSTOM', 'CUSTOMER_PROFILE', 'SYSTEM']]]

### defaultAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateAttributesOutputTypeDef]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GroupingConfigurationOutputTypeDef]

### isActive
- **Type**: typing.Optional[bool]

### language
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### versionNumber
- **Type**: typing.Optional[int]


# ExternalSourceConfigurationTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ConfigurationTypeDef'>
- **Required**: Yes

### source
- **Type**: typing.Literal['AMAZON_CONNECT']
- **Required**: Yes


# FilterTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FixedSizeChunkingConfigurationTypeDef

### maxTokens
- **Type**: <class 'int'>
- **Required**: Yes

### overlapPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# GenerativeContentFeedbackDataTypeDef

### relevance
- **Type**: typing.Literal['HELPFUL', 'NOT_HELPFUL']
- **Required**: Yes


# GenerativeDataDetailsPaginatorTypeDef

### completion
- **Type**: <class 'str'>
- **Required**: Yes

### rankingData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.RankingDataTypeDef'>
- **Required**: Yes

### references
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# GenerativeDataDetailsTypeDef

### completion
- **Type**: <class 'str'>
- **Required**: Yes

### rankingData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.RankingDataTypeDef'>
- **Required**: Yes

### references
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# GenerativeReferenceTypeDef

### generationId
- **Type**: typing.Optional[str]

### modelId
- **Type**: typing.Optional[str]


# GetAIAgentRequestTypeDef

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAIAgentResponseTypeDef

### aiAgent
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AIAgentDataTypeDef'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAIGuardrailRequestTypeDef

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAIGuardrailResponseTypeDef

### aiGuardrail
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailDataTypeDef'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAIPromptRequestTypeDef

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAIPromptResponseTypeDef

### aiPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AIPromptDataTypeDef'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAssistantAssociationRequestTypeDef

### assistantAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssistantAssociationResponseTypeDef

### assistantAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AssistantAssociationDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAssistantRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssistantResponseTypeDef

### assistant
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AssistantDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContentAssociationRequestTypeDef

### contentAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetContentAssociationResponseTypeDef

### contentAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ContentAssociationDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContentRequestTypeDef

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetContentResponseTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ContentDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContentSummaryRequestTypeDef

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetContentSummaryResponseTypeDef

### contentSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ContentSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImportJobRequestTypeDef

### importJobId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportJobResponseTypeDef

### importJob
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ImportJobDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKnowledgeBaseRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKnowledgeBaseResponseTypeDef

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.KnowledgeBaseDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMessageTemplateRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMessageTemplateResponseTypeDef

### messageTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ExtendedMessageTemplateDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNextMessageRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### nextMessageToken
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQuickResponseRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQuickResponseResponseTypeDef

### quickResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecommendationsRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### waitTimeSeconds
- **Type**: typing.Optional[int]


# GetRecommendationsResponseTypeDef

### recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.RecommendationDataTypeDef]
- **Required**: Yes

### triggers
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.RecommendationTriggerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSessionRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionResponseTypeDef

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.SessionDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupingConfigurationOutputTypeDef

### criteria
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


# GroupingConfigurationTypeDef

### criteria
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# GroupingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailContentFilterConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailContextualGroundingFilterConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailManagedWordsConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailPiiEntityConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailRegexConfigTypeDef

### action
- **Type**: typing.Literal['ANONYMIZE', 'BLOCK']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### pattern
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# GuardrailTopicConfigOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailTopicConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GuardrailWordConfigTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes


# HierarchicalChunkingConfigurationOutputTypeDef

### levelConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.HierarchicalChunkingLevelConfigurationTypeDef]
- **Required**: Yes

### overlapTokens
- **Type**: <class 'int'>
- **Required**: Yes


# HierarchicalChunkingConfigurationTypeDef

### levelConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.HierarchicalChunkingLevelConfigurationTypeDef]
- **Required**: Yes

### overlapTokens
- **Type**: <class 'int'>
- **Required**: Yes


# HierarchicalChunkingLevelConfigurationTypeDef

### maxTokens
- **Type**: <class 'int'>
- **Required**: Yes


# HighlightTypeDef

### beginOffsetInclusive
- **Type**: typing.Optional[int]

### endOffsetExclusive
- **Type**: typing.Optional[int]


# ImportJobDataTypeDef

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### importJobId
- **Type**: <class 'str'>
- **Required**: Yes

### importJobType
- **Type**: typing.Literal['QUICK_RESPONSES']
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETE', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'FAILED', 'START_IN_PROGRESS']
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### urlExpiry
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### externalSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ExternalSourceConfigurationTypeDef]

### failedRecordReport
- **Type**: typing.Optional[str]

### metadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# ImportJobSummaryTypeDef

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### importJobId
- **Type**: <class 'str'>
- **Required**: Yes

### importJobType
- **Type**: typing.Literal['QUICK_RESPONSES']
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['COMPLETE', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'FAILED', 'START_IN_PROGRESS']
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### externalSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ExternalSourceConfigurationTypeDef]

### metadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# IntentDetectedDataDetailsTypeDef

### intent
- **Type**: <class 'str'>
- **Required**: Yes

### intentId
- **Type**: <class 'str'>
- **Required**: Yes


# IntentInputDataTypeDef

### intentId
- **Type**: <class 'str'>
- **Required**: Yes


# KnowledgeBaseAssociationConfigurationDataOutputTypeDef

### contentTagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TagFilterOutputTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### overrideKnowledgeBaseSearchType
- **Type**: typing.Optional[typing.Literal['HYBRID', 'SEMANTIC']]


# KnowledgeBaseAssociationConfigurationDataTypeDef

### contentTagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TagFilterTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### overrideKnowledgeBaseSearchType
- **Type**: typing.Optional[typing.Literal['HYBRID', 'SEMANTIC']]


# KnowledgeBaseAssociationDataTypeDef

### knowledgeBaseArn
- **Type**: typing.Optional[str]

### knowledgeBaseId
- **Type**: typing.Optional[str]


# KnowledgeBaseDataTypeDef

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseType
- **Type**: typing.Literal['CUSTOM', 'EXTERNAL', 'MANAGED', 'MESSAGE_TEMPLATES', 'QUICK_RESPONSES']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### ingestionFailureReasons
- **Type**: typing.Optional[typing.List[str]]

### ingestionStatus
- **Type**: typing.Optional[typing.Literal['CREATE_IN_PROGRESS', 'SYNCING_IN_PROGRESS', 'SYNC_FAILED', 'SYNC_SUCCESS']]

### lastContentModificationTime
- **Type**: typing.Optional[datetime.datetime]

### renderingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.RenderingConfigurationTypeDef]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ServerSideEncryptionConfigurationTypeDef]

### sourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SourceConfigurationOutputTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### vectorIngestionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.VectorIngestionConfigurationOutputTypeDef]


# KnowledgeBaseSummaryTypeDef

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseType
- **Type**: typing.Literal['CUSTOM', 'EXTERNAL', 'MANAGED', 'MESSAGE_TEMPLATES', 'QUICK_RESPONSES']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### renderingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.RenderingConfigurationTypeDef]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ServerSideEncryptionConfigurationTypeDef]

### sourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SourceConfigurationOutputTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### vectorIngestionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.VectorIngestionConfigurationOutputTypeDef]


# ListAIAgentVersionsRequestPaginateTypeDef

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListAIAgentVersionsRequestTypeDef

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]


# ListAIAgentVersionsResponseTypeDef

### aiAgentVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.AIAgentVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAIAgentsRequestPaginateTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListAIAgentsRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]


# ListAIAgentsResponseTypeDef

### aiAgentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.AIAgentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAIGuardrailVersionsRequestPaginateTypeDef

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListAIGuardrailVersionsRequestTypeDef

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAIGuardrailVersionsResponseTypeDef

### aiGuardrailVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAIGuardrailsRequestPaginateTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListAIGuardrailsRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAIGuardrailsResponseTypeDef

### aiGuardrailSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAIPromptVersionsRequestPaginateTypeDef

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListAIPromptVersionsRequestTypeDef

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]


# ListAIPromptVersionsResponseTypeDef

### aiPromptVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.AIPromptVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAIPromptsRequestPaginateTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListAIPromptsRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]


# ListAIPromptsResponseTypeDef

### aiPromptSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.AIPromptSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssistantAssociationsRequestPaginateTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListAssistantAssociationsRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAssistantAssociationsResponseTypeDef

### assistantAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.AssistantAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssistantsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListAssistantsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAssistantsResponseTypeDef

### assistantSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.AssistantSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListContentAssociationsRequestPaginateTypeDef

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListContentAssociationsRequestTypeDef

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListContentAssociationsResponseTypeDef

### contentAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.ContentAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListContentsRequestPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListContentsRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListContentsResponseTypeDef

### contentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.ContentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImportJobsRequestPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListImportJobsRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImportJobsResponseTypeDef

### importJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.ImportJobSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListKnowledgeBasesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListKnowledgeBasesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListKnowledgeBasesResponseTypeDef

### knowledgeBaseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.KnowledgeBaseSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMessageTemplateVersionsRequestPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListMessageTemplateVersionsRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMessageTemplateVersionsResponseTypeDef

### messageTemplateVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateVersionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMessageTemplatesRequestPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListMessageTemplatesRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMessageTemplatesResponseTypeDef

### messageTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMessagesRequestPaginateTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListMessagesRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMessagesResponseTypeDef

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.MessageOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQuickResponsesRequestPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListQuickResponsesRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListQuickResponsesResponseTypeDef

### quickResponseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ManagedSourceConfigurationOutputTypeDef

### webCrawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.WebCrawlerConfigurationOutputTypeDef]


# ManagedSourceConfigurationTypeDef

### webCrawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.WebCrawlerConfigurationTypeDef]


# ManualSearchAIAgentConfigurationOutputTypeDef

### answerGenerationAIGuardrailId
- **Type**: typing.Optional[str]

### answerGenerationAIPromptId
- **Type**: typing.Optional[str]

### associationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.AssociationConfigurationOutputTypeDef]]

### locale
- **Type**: typing.Optional[str]


# ManualSearchAIAgentConfigurationTypeDef

### answerGenerationAIGuardrailId
- **Type**: typing.Optional[str]

### answerGenerationAIPromptId
- **Type**: typing.Optional[str]

### associationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.AssociationConfigurationTypeDef]]

### locale
- **Type**: typing.Optional[str]


# MessageDataTypeDef

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TextMessageTypeDef]


# MessageInputTypeDef

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.MessageDataTypeDef'>
- **Required**: Yes


# MessageOutputTypeDef

### messageId
- **Type**: <class 'str'>
- **Required**: Yes

### participant
- **Type**: typing.Literal['AGENT', 'BOT', 'CUSTOMER']
- **Required**: Yes

### timestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.MessageDataTypeDef'>
- **Required**: Yes


# MessageTemplateAttachmentTypeDef

### attachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### contentDisposition
- **Type**: typing.Literal['ATTACHMENT']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### uploadedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### urlExpiry
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# MessageTemplateAttributesOutputTypeDef

### agentAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AgentAttributesTypeDef]

### customAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### customerProfileAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.CustomerProfileAttributesOutputTypeDef]

### systemAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SystemAttributesTypeDef]


# MessageTemplateAttributesTypeDef

### agentAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AgentAttributesTypeDef]

### customAttributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### customerProfileAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.CustomerProfileAttributesTypeDef]

### systemAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SystemAttributesTypeDef]


# MessageTemplateAttributesUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MessageTemplateBodyContentProviderTypeDef

### content
- **Type**: typing.Optional[str]


# MessageTemplateContentProviderOutputTypeDef

### email
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.EmailMessageTemplateContentOutputTypeDef]

### sms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SMSMessageTemplateContentTypeDef]


# MessageTemplateContentProviderTypeDef

### email
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.EmailMessageTemplateContentTypeDef]

### sms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SMSMessageTemplateContentTypeDef]


# MessageTemplateContentProviderUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MessageTemplateDataTypeDef

### channelSubtype
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateContentProviderOutputTypeDef'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### messageTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateContentSha256
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### attributeTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AGENT', 'CUSTOM', 'CUSTOMER_PROFILE', 'SYSTEM']]]

### defaultAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateAttributesOutputTypeDef]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GroupingConfigurationOutputTypeDef]

### language
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# MessageTemplateFilterFieldTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MessageTemplateOrderFieldTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# MessageTemplateQueryFieldTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MessageTemplateSearchExpressionTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateFilterFieldTypeDef]]

### orderOnField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateOrderFieldTypeDef]

### queries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateQueryFieldTypeDef]]


# MessageTemplateSearchResultDataTypeDef

### channelSubtype
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### messageTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GroupingConfigurationOutputTypeDef]

### isActive
- **Type**: typing.Optional[bool]

### language
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### versionNumber
- **Type**: typing.Optional[int]


# MessageTemplateSummaryTypeDef

### channelSubtype
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedBy
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### messageTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### activeVersionNumber
- **Type**: typing.Optional[int]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# MessageTemplateVersionSummaryTypeDef

### channelSubtype
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### isActive
- **Type**: <class 'bool'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateArn
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# NotifyRecommendationsReceivedErrorTypeDef

### message
- **Type**: typing.Optional[str]

### recommendationId
- **Type**: typing.Optional[str]


# NotifyRecommendationsReceivedRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# NotifyRecommendationsReceivedResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.NotifyRecommendationsReceivedErrorTypeDef]
- **Required**: Yes

### recommendationIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OrConditionOutputTypeDef

### andConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.TagConditionTypeDef]]

### tagCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TagConditionTypeDef]


# OrConditionTypeDef

### andConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.TagConditionTypeDef]]

### tagCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TagConditionTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParsingConfigurationTypeDef

### parsingStrategy
- **Type**: typing.Literal['BEDROCK_FOUNDATION_MODEL']
- **Required**: Yes

### bedrockFoundationModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.BedrockFoundationModelConfigurationForParsingTypeDef]


# ParsingPromptTypeDef

### parsingPromptText
- **Type**: <class 'str'>
- **Required**: Yes


# PutFeedbackRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### contentFeedback
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ContentFeedbackDataTypeDef'>
- **Required**: Yes

### targetId
- **Type**: <class 'str'>
- **Required**: Yes

### targetType
- **Type**: typing.Literal['RECOMMENDATION', 'RESULT']
- **Required**: Yes


# PutFeedbackResponseTypeDef

### assistantArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### contentFeedback
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ContentFeedbackDataTypeDef'>
- **Required**: Yes

### targetId
- **Type**: <class 'str'>
- **Required**: Yes

### targetType
- **Type**: typing.Literal['RECOMMENDATION', 'RESULT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QueryAssistantRequestPaginateTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### overrideKnowledgeBaseSearchType
- **Type**: typing.Optional[typing.Literal['HYBRID', 'SEMANTIC']]

### queryCondition
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.QueryConditionTypeDef]]

### queryInputData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.QueryInputDataTypeDef]

### queryText
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# QueryAssistantRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### overrideKnowledgeBaseSearchType
- **Type**: typing.Optional[typing.Literal['HYBRID', 'SEMANTIC']]

### queryCondition
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.QueryConditionTypeDef]]

### queryInputData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.QueryInputDataTypeDef]

### queryText
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]


# QueryAssistantResponsePaginatorTypeDef

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.ResultDataPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# QueryAssistantResponseTypeDef

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.ResultDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# QueryConditionItemTypeDef

### comparator
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### field
- **Type**: typing.Literal['RESULT_TYPE']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# QueryConditionTypeDef

### single
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.QueryConditionItemTypeDef]


# QueryInputDataTypeDef

### intentInputData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.IntentInputDataTypeDef]

### queryTextInputData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.QueryTextInputDataTypeDef]


# QueryRecommendationTriggerDataTypeDef

### text
- **Type**: typing.Optional[str]


# QueryTextInputDataTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes


# QuickResponseContentProviderTypeDef

### content
- **Type**: typing.Optional[str]


# QuickResponseContentsTypeDef

### markdown
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseContentProviderTypeDef]

### plainText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseContentProviderTypeDef]


# QuickResponseDataProviderTypeDef

### content
- **Type**: typing.Optional[str]


# QuickResponseDataTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseArn
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### channels
- **Type**: typing.Optional[typing.List[str]]

### contents
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseContentsTypeDef]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GroupingConfigurationOutputTypeDef]

### isActive
- **Type**: typing.Optional[bool]

### language
- **Type**: typing.Optional[str]

### lastModifiedBy
- **Type**: typing.Optional[str]

### shortcutKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# QuickResponseFilterFieldTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QuickResponseOrderFieldTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# QuickResponseQueryFieldTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# QuickResponseSearchExpressionTypeDef

### filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseFilterFieldTypeDef]]

### orderOnField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseOrderFieldTypeDef]

### queries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseQueryFieldTypeDef]]


# QuickResponseSearchResultDataTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### contents
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseContentsTypeDef'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### isActive
- **Type**: <class 'bool'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseArn
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### attributesInterpolated
- **Type**: typing.Optional[typing.List[str]]

### attributesNotInterpolated
- **Type**: typing.Optional[typing.List[str]]

### channels
- **Type**: typing.Optional[typing.List[str]]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GroupingConfigurationOutputTypeDef]

### language
- **Type**: typing.Optional[str]

### lastModifiedBy
- **Type**: typing.Optional[str]

### shortcutKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# QuickResponseSummaryTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### createdTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseArn
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['CREATED', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS', 'UPDATE_FAILED', 'UPDATE_IN_PROGRESS']
- **Required**: Yes

### channels
- **Type**: typing.Optional[typing.List[str]]

### description
- **Type**: typing.Optional[str]

### isActive
- **Type**: typing.Optional[bool]

### lastModifiedBy
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# RankingDataTypeDef

### relevanceLevel
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### relevanceScore
- **Type**: typing.Optional[float]


# RecommendationDataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecommendationTriggerDataTypeDef

### query
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.QueryRecommendationTriggerDataTypeDef]


# RecommendationTriggerTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RemoveAssistantAIAgentRequestTypeDef

### aiAgentType
- **Type**: typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE']
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveKnowledgeBaseTemplateUriRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# RenderMessageTemplateRequestTypeDef

### attributes
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateAttributesUnionTypeDef'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# RenderMessageTemplateResponseTypeDef

### attachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateAttachmentTypeDef]
- **Required**: Yes

### attributesNotInterpolated
- **Type**: typing.List[str]
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateContentProviderOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RenderingConfigurationTypeDef

### templateUri
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


# ResultDataPaginatorTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ResultDataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RuntimeSessionDataTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.RuntimeSessionDataValueTypeDef'>
- **Required**: Yes


# RuntimeSessionDataValueTypeDef

### stringValue
- **Type**: typing.Optional[str]


# SMSMessageTemplateContentBodyTypeDef

### plainText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateBodyContentProviderTypeDef]


# SMSMessageTemplateContentTypeDef

### body
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SMSMessageTemplateContentBodyTypeDef]


# SearchContentRequestPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.SearchExpressionTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# SearchContentRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.SearchExpressionTypeDef'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchContentResponseTypeDef

### contentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.ContentSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchExpressionTypeDef

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.FilterTypeDef]
- **Required**: Yes


# SearchMessageTemplatesRequestPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateSearchExpressionTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# SearchMessageTemplatesRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateSearchExpressionTypeDef'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchMessageTemplatesResponseTypeDef

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateSearchResultDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchQuickResponsesRequestPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseSearchExpressionTypeDef'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# SearchQuickResponsesRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseSearchExpressionTypeDef'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchQuickResponsesResponseTypeDef

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseSearchResultDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchSessionsRequestPaginateTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.SearchExpressionTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# SearchSessionsRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.SearchExpressionTypeDef'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchSessionsResponseTypeDef

### sessionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.SessionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SeedUrlTypeDef

### url
- **Type**: typing.Optional[str]


# SelfServiceAIAgentConfigurationOutputTypeDef

### associationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.AssociationConfigurationOutputTypeDef]]

### selfServiceAIGuardrailId
- **Type**: typing.Optional[str]

### selfServiceAnswerGenerationAIPromptId
- **Type**: typing.Optional[str]

### selfServicePreProcessingAIPromptId
- **Type**: typing.Optional[str]


# SelfServiceAIAgentConfigurationTypeDef

### associationConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.AssociationConfigurationTypeDef]]

### selfServiceAIGuardrailId
- **Type**: typing.Optional[str]

### selfServiceAnswerGenerationAIPromptId
- **Type**: typing.Optional[str]

### selfServicePreProcessingAIPromptId
- **Type**: typing.Optional[str]


# SelfServiceConversationHistoryTypeDef

### turnNumber
- **Type**: <class 'int'>
- **Required**: Yes

### botResponse
- **Type**: typing.Optional[str]

### inputTranscript
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


# SendMessageResponseTypeDef

### nextMessageToken
- **Type**: <class 'str'>
- **Required**: Yes

### requestMessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ServerSideEncryptionConfigurationTypeDef

### kmsKeyId
- **Type**: typing.Optional[str]


# SessionDataTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### aiAgentConfiguration
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE'], aws_resource_validator.pydantic_models.qconnect_classes.AIAgentConfigurationDataTypeDef]]

### description
- **Type**: typing.Optional[str]

### integrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SessionIntegrationConfigurationTypeDef]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TagFilterOutputTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SessionIntegrationConfigurationTypeDef

### topicIntegrationArn
- **Type**: typing.Optional[str]


# SessionSummaryTypeDef

### assistantArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# SourceConfigurationOutputTypeDef

### appIntegrations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AppIntegrationsConfigurationOutputTypeDef]

### managedSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ManagedSourceConfigurationOutputTypeDef]


# SourceConfigurationTypeDef

### appIntegrations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AppIntegrationsConfigurationTypeDef]

### managedSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ManagedSourceConfigurationTypeDef]


# SourceConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SourceContentDataDetailsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartContentUploadRequestTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### presignedUrlTimeToLive
- **Type**: typing.Optional[int]


# StartContentUploadResponseTypeDef

### headersToInclude
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### url
- **Type**: <class 'str'>
- **Required**: Yes

### urlExpiry
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartImportJobRequestTypeDef

### importJobType
- **Type**: typing.Literal['QUICK_RESPONSES']
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### uploadId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### externalSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ExternalSourceConfigurationTypeDef]

### metadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartImportJobResponseTypeDef

### importJob
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ImportJobDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SystemAttributesTypeDef

### customerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SystemEndpointAttributesTypeDef]

### name
- **Type**: typing.Optional[str]

### systemEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SystemEndpointAttributesTypeDef]


# SystemEndpointAttributesTypeDef

### address
- **Type**: typing.Optional[str]


# TagConditionTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# TagFilterOutputTypeDef

### andConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.TagConditionTypeDef]]

### orConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.OrConditionOutputTypeDef]]

### tagCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TagConditionTypeDef]


# TagFilterTypeDef

### andConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.TagConditionTypeDef]]

### orConditions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.OrConditionTypeDef]]

### tagCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TagConditionTypeDef]


# TagFilterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TextDataTypeDef

### excerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.DocumentTextTypeDef]

### title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.DocumentTextTypeDef]


# TextFullAIPromptEditTemplateConfigurationTypeDef

### text
- **Type**: <class 'str'>
- **Required**: Yes


# TextMessageTypeDef

### value
- **Type**: typing.Optional[str]


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAIAgentRequestTypeDef

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### visibilityStatus
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIAgentConfigurationUnionTypeDef]

### description
- **Type**: typing.Optional[str]


# UpdateAIAgentResponseTypeDef

### aiAgent
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AIAgentDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAIGuardrailRequestTypeDef

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### blockedInputMessaging
- **Type**: <class 'str'>
- **Required**: Yes

### blockedOutputsMessaging
- **Type**: <class 'str'>
- **Required**: Yes

### visibilityStatus
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### contentPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailContentPolicyConfigUnionTypeDef]

### contextualGroundingPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailContextualGroundingPolicyConfigUnionTypeDef]

### description
- **Type**: typing.Optional[str]

### sensitiveInformationPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailSensitiveInformationPolicyConfigUnionTypeDef]

### topicPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailTopicPolicyConfigUnionTypeDef]

### wordPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailWordPolicyConfigUnionTypeDef]


# UpdateAIGuardrailResponseTypeDef

### aiGuardrail
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AIGuardrailDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAIPromptRequestTypeDef

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### visibilityStatus
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### templateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AIPromptTemplateConfigurationTypeDef]


# UpdateAIPromptResponseTypeDef

### aiPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AIPromptDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAssistantAIAgentRequestTypeDef

### aiAgentType
- **Type**: typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE']
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AIAgentConfigurationDataTypeDef'>
- **Required**: Yes


# UpdateAssistantAIAgentResponseTypeDef

### assistant
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AssistantDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateContentRequestTypeDef

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### overrideLinkOutUri
- **Type**: typing.Optional[str]

### removeOverrideLinkOutUri
- **Type**: typing.Optional[bool]

### revisionId
- **Type**: typing.Optional[str]

### title
- **Type**: typing.Optional[str]

### uploadId
- **Type**: typing.Optional[str]


# UpdateContentResponseTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ContentDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateKnowledgeBaseTemplateUriRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### templateUri
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateKnowledgeBaseTemplateUriResponseTypeDef

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.KnowledgeBaseDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMessageTemplateMetadataRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GroupingConfigurationUnionTypeDef]

### name
- **Type**: typing.Optional[str]


# UpdateMessageTemplateMetadataResponseTypeDef

### messageTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMessageTemplateRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateContentProviderUnionTypeDef]

### defaultAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateAttributesUnionTypeDef]

### language
- **Type**: typing.Optional[str]


# UpdateMessageTemplateResponseTypeDef

### messageTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.MessageTemplateDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateQuickResponseRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### channels
- **Type**: typing.Optional[typing.Sequence[str]]

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseDataProviderTypeDef]

### contentType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GroupingConfigurationUnionTypeDef]

### isActive
- **Type**: typing.Optional[bool]

### language
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### removeDescription
- **Type**: typing.Optional[bool]

### removeGroupingConfiguration
- **Type**: typing.Optional[bool]

### removeShortcutKey
- **Type**: typing.Optional[bool]

### shortcutKey
- **Type**: typing.Optional[str]


# UpdateQuickResponseResponseTypeDef

### quickResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSessionDataRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.RuntimeSessionDataTypeDef]
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[typing.Literal['Custom']]


# UpdateSessionDataResponseTypeDef

### data
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.RuntimeSessionDataTypeDef]
- **Required**: Yes

### namespace
- **Type**: typing.Literal['Custom']
- **Required**: Yes

### sessionArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSessionRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### aiAgentConfiguration
- **Type**: typing.Optional[typing.Mapping[typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE'], aws_resource_validator.pydantic_models.qconnect_classes.AIAgentConfigurationDataTypeDef]]

### description
- **Type**: typing.Optional[str]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TagFilterUnionTypeDef]


# UpdateSessionResponseTypeDef

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.SessionDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UrlConfigurationOutputTypeDef

### seedUrls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect_classes.SeedUrlTypeDef]]


# UrlConfigurationTypeDef

### seedUrls
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.SeedUrlTypeDef]]


# VectorIngestionConfigurationOutputTypeDef

### chunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ChunkingConfigurationOutputTypeDef]

### parsingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ParsingConfigurationTypeDef]


# VectorIngestionConfigurationTypeDef

### chunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ChunkingConfigurationTypeDef]

### parsingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ParsingConfigurationTypeDef]


# VectorIngestionConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WebCrawlerConfigurationOutputTypeDef

### urlConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.UrlConfigurationOutputTypeDef'>
- **Required**: Yes

### crawlerLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.WebCrawlerLimitsTypeDef]

### exclusionFilters
- **Type**: typing.Optional[typing.List[str]]

### inclusionFilters
- **Type**: typing.Optional[typing.List[str]]

### scope
- **Type**: typing.Optional[typing.Literal['HOST_ONLY', 'SUBDOMAINS']]


# WebCrawlerConfigurationTypeDef

### urlConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.UrlConfigurationTypeDef'>
- **Required**: Yes

### crawlerLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.WebCrawlerLimitsTypeDef]

### exclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### inclusionFilters
- **Type**: typing.Optional[typing.Sequence[str]]

### scope
- **Type**: typing.Optional[typing.Literal['HOST_ONLY', 'SUBDOMAINS']]


# WebCrawlerLimitsTypeDef

### rateLimit
- **Type**: typing.Optional[int]


