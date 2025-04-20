# Qconnect Qconnect Classes

# AIAgentConfiguration

### answerRecommendationAIAgentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AnswerRecommendationAIAgentConfiguration]

### manualSearchAIAgentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ManualSearchAIAgentConfiguration]

### selfServiceAIAgentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SelfServiceAIAgentConfiguration]


# AIAgentConfigurationData

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes


# AIAgentConfigurationOutput

### answerRecommendationAIAgentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AnswerRecommendationAIAgentConfigurationOutput]

### manualSearchAIAgentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ManualSearchAIAgentConfigurationOutput]

### selfServiceAIAgentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SelfServiceAIAgentConfigurationOutput]


# AIAgentData

### aiAgentArn
- **Type**: <class 'str'>
- **Required**: Yes

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentConfigurationOutput'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE']
- **Required**: Yes

### visibilityStatus
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### modifiedTime
- **Type**: typing.Optional[datetime.datetime]

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AIAgentSummary

### aiAgentArn
- **Type**: <class 'str'>
- **Required**: Yes

### aiAgentId
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

### type
- **Type**: typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE']
- **Required**: Yes

### visibilityStatus
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentConfigurationOutput]

### description
- **Type**: typing.Optional[str]

### modifiedTime
- **Type**: typing.Optional[datetime.datetime]

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AIAgentVersionSummary

### aiAgentSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentSummary]

### versionNumber
- **Type**: typing.Optional[int]


# AIGuardrailContentPolicyConfig

### filtersConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailContentFilterConfig]
- **Required**: Yes


# AIGuardrailContentPolicyConfigOutput

### filtersConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailContentFilterConfig]
- **Required**: Yes


# AIGuardrailContextualGroundingPolicyConfig

### filtersConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailContextualGroundingFilterConfig]
- **Required**: Yes


# AIGuardrailContextualGroundingPolicyConfigOutput

### filtersConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailContextualGroundingFilterConfig]
- **Required**: Yes


# AIGuardrailData

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailContentPolicyConfigOutput]

### contextualGroundingPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailContextualGroundingPolicyConfigOutput]

### description
- **Type**: typing.Optional[str]

### modifiedTime
- **Type**: typing.Optional[datetime.datetime]

### sensitiveInformationPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailSensitiveInformationPolicyConfigOutput]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### topicPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailTopicPolicyConfigOutput]

### wordPolicyConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailWordPolicyConfigOutput]


# AIGuardrailSensitiveInformationPolicyConfig

### piiEntitiesConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailPiiEntityConfig]]

### regexesConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailRegexConfig]]


# AIGuardrailSensitiveInformationPolicyConfigOutput

### piiEntitiesConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailPiiEntityConfig]]

### regexesConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailRegexConfig]]


# AIGuardrailSummary

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


# AIGuardrailTopicPolicyConfig

### topicsConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailTopicConfig]
- **Required**: Yes


# AIGuardrailTopicPolicyConfigOutput

### topicsConfig
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailTopicConfigOutput]
- **Required**: Yes


# AIGuardrailVersionSummary

### aiGuardrailSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailSummary]

### versionNumber
- **Type**: typing.Optional[int]


# AIGuardrailWordPolicyConfig

### managedWordListsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailManagedWordsConfig]]

### wordsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailWordConfig]]


# AIGuardrailWordPolicyConfigOutput

### managedWordListsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailManagedWordsConfig]]

### wordsConfig
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GuardrailWordConfig]]


# AIPromptData

### aiPromptArn
- **Type**: <class 'str'>
- **Required**: Yes

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### apiFormat
- **Type**: typing.Literal['ANTHROPIC_CLAUDE_MESSAGES', 'ANTHROPIC_CLAUDE_TEXT_COMPLETIONS']
- **Required**: Yes

### assistantArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIPromptTemplateConfiguration'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['TEXT']
- **Required**: Yes

### type
- **Type**: typing.Literal['ANSWER_GENERATION', 'INTENT_LABELING_GENERATION', 'QUERY_REFORMULATION', 'SELF_SERVICE_ANSWER_GENERATION', 'SELF_SERVICE_PRE_PROCESSING']
- **Required**: Yes

### visibilityStatus
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### modifiedTime
- **Type**: typing.Optional[datetime.datetime]

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AIPromptSummary

### aiPromptArn
- **Type**: <class 'str'>
- **Required**: Yes

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### apiFormat
- **Type**: typing.Literal['ANTHROPIC_CLAUDE_MESSAGES', 'ANTHROPIC_CLAUDE_TEXT_COMPLETIONS']
- **Required**: Yes

### assistantArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['TEXT']
- **Required**: Yes

### type
- **Type**: typing.Literal['ANSWER_GENERATION', 'INTENT_LABELING_GENERATION', 'QUERY_REFORMULATION', 'SELF_SERVICE_ANSWER_GENERATION', 'SELF_SERVICE_PRE_PROCESSING']
- **Required**: Yes

### visibilityStatus
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### modifiedTime
- **Type**: typing.Optional[datetime.datetime]

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]

### status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AIPromptTemplateConfiguration

### textFullAIPromptEditTemplateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TextFullAIPromptEditTemplateConfiguration]


# AIPromptVersionSummary

### aiPromptSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIPromptSummary]

### versionNumber
- **Type**: typing.Optional[int]


# ActivateMessageTemplateRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# ActivateMessageTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# AgentAttributes

### firstName
- **Type**: typing.Optional[str]

### lastName
- **Type**: typing.Optional[str]


# AmazonConnectGuideAssociationData

### flowId
- **Type**: typing.Optional[str]


# AnswerRecommendationAIAgentConfiguration

### answerGenerationAIGuardrailId
- **Type**: typing.Optional[str]

### answerGenerationAIPromptId
- **Type**: typing.Optional[str]

### associationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssociationConfiguration]]

### intentLabelingGenerationAIPromptId
- **Type**: typing.Optional[str]

### locale
- **Type**: typing.Optional[str]

### queryReformulationAIPromptId
- **Type**: typing.Optional[str]


# AnswerRecommendationAIAgentConfigurationOutput

### answerGenerationAIGuardrailId
- **Type**: typing.Optional[str]

### answerGenerationAIPromptId
- **Type**: typing.Optional[str]

### associationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssociationConfigurationOutput]]

### intentLabelingGenerationAIPromptId
- **Type**: typing.Optional[str]

### locale
- **Type**: typing.Optional[str]

### queryReformulationAIPromptId
- **Type**: typing.Optional[str]


# AppIntegrationsConfiguration

### appIntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### objectFields
- **Type**: typing.Optional[typing.List[str]]


# AppIntegrationsConfigurationOutput

### appIntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### objectFields
- **Type**: typing.Optional[typing.List[str]]


# AssistantAssociationData

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantAssociationOutputData'>
- **Required**: Yes

### associationType
- **Type**: typing.Literal['KNOWLEDGE_BASE']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AssistantAssociationInputData

### knowledgeBaseId
- **Type**: typing.Optional[str]


# AssistantAssociationOutputData

### knowledgeBaseAssociation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.KnowledgeBaseAssociationData]


# AssistantAssociationSummary

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantAssociationOutputData'>
- **Required**: Yes

### associationType
- **Type**: typing.Literal['KNOWLEDGE_BASE']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AssistantCapabilityConfiguration

### type
- **Type**: typing.Optional[typing.Literal['V1', 'V2']]


# AssistantData

### assistantArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### type
- **Type**: typing.Literal['AGENT']
- **Required**: Yes

### aiAgentConfiguration
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE'], aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentConfigurationData]]

### capabilityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantCapabilityConfiguration]

### description
- **Type**: typing.Optional[str]

### integrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantIntegrationConfiguration]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ServerSideEncryptionConfiguration]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AssistantIntegrationConfiguration

### topicIntegrationArn
- **Type**: typing.Optional[str]


# AssistantSummary

### assistantArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### type
- **Type**: typing.Literal['AGENT']
- **Required**: Yes

### aiAgentConfiguration
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE'], aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentConfigurationData]]

### capabilityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantCapabilityConfiguration]

### description
- **Type**: typing.Optional[str]

### integrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantIntegrationConfiguration]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ServerSideEncryptionConfiguration]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AssociationConfiguration

### associationConfigurationData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssociationConfigurationData]

### associationId
- **Type**: typing.Optional[str]

### associationType
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE']]


# AssociationConfigurationData

### knowledgeBaseAssociationConfigurationData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.KnowledgeBaseAssociationConfigurationData]


# AssociationConfigurationDataOutput

### knowledgeBaseAssociationConfigurationData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.KnowledgeBaseAssociationConfigurationDataOutput]


# AssociationConfigurationOutput

### associationConfigurationData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssociationConfigurationDataOutput]

### associationId
- **Type**: typing.Optional[str]

### associationType
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_BASE']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BedrockFoundationModelConfigurationForParsing

### modelArn
- **Type**: <class 'str'>
- **Required**: Yes

### parsingPrompt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ParsingPrompt]


# ChunkingConfiguration

### chunkingStrategy
- **Type**: typing.Literal['FIXED_SIZE', 'HIERARCHICAL', 'NONE', 'SEMANTIC']
- **Required**: Yes

### fixedSizeChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.FixedSizeChunkingConfiguration]

### hierarchicalChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.HierarchicalChunkingConfiguration]

### semanticChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SemanticChunkingConfiguration]


# ChunkingConfigurationOutput

### chunkingStrategy
- **Type**: typing.Literal['FIXED_SIZE', 'HIERARCHICAL', 'NONE', 'SEMANTIC']
- **Required**: Yes

### fixedSizeChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.FixedSizeChunkingConfiguration]

### hierarchicalChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.HierarchicalChunkingConfigurationOutput]

### semanticChunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SemanticChunkingConfiguration]


# CitationSpan

### beginOffsetInclusive
- **Type**: typing.Optional[int]

### endOffsetExclusive
- **Type**: typing.Optional[int]


# Configuration

### connectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ConnectConfiguration]


# ConnectConfiguration

### instanceId
- **Type**: typing.Optional[str]


# ContentAssociationContents

### amazonConnectGuideAssociation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AmazonConnectGuideAssociationData]


# ContentAssociationData

### associationData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentAssociationContents'>
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


# ContentAssociationSummary

### associationData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentAssociationContents'>
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


# ContentData

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


# ContentDataDetails

### rankingData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RankingData'>
- **Required**: Yes

### textData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TextData'>
- **Required**: Yes


# ContentFeedbackData

### generativeContentFeedbackData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GenerativeContentFeedbackData]


# ContentReference

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


# ContentSummary

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


# ConversationContext

### selfServiceConversationHistory
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SelfServiceConversationHistory]
- **Required**: Yes


# ConversationState

### status
- **Type**: typing.Literal['CLOSED', 'PROCESSING', 'READY']
- **Required**: Yes

### reason
- **Type**: typing.Optional[typing.Literal['FAILED', 'REJECTED', 'SUCCESS']]


# CreateAIAgentRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentConfiguration, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentConfigurationOutput]
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE']
- **Required**: Yes

### visibilityStatus
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAIAgentResponse

### aiAgent
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAIAgentVersionRequest

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### modifiedTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# CreateAIAgentVersionResponse

### aiAgent
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentData'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAIGuardrailRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailContentPolicyConfig, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailContentPolicyConfigOutput, NoneType]

### contextualGroundingPolicyConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailContextualGroundingPolicyConfig, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailContextualGroundingPolicyConfigOutput, NoneType]

### description
- **Type**: typing.Optional[str]

### sensitiveInformationPolicyConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailSensitiveInformationPolicyConfig, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailSensitiveInformationPolicyConfigOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### topicPolicyConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailTopicPolicyConfig, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailTopicPolicyConfigOutput, NoneType]

### wordPolicyConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailWordPolicyConfig, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailWordPolicyConfigOutput, NoneType]


# CreateAIGuardrailResponse

### aiGuardrail
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAIGuardrailVersionRequest

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### modifiedTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# CreateAIGuardrailVersionResponse

### aiGuardrail
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailData'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAIPromptRequest

### apiFormat
- **Type**: typing.Literal['ANTHROPIC_CLAUDE_MESSAGES', 'ANTHROPIC_CLAUDE_TEXT_COMPLETIONS']
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### modelId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### templateConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIPromptTemplateConfiguration'>
- **Required**: Yes

### templateType
- **Type**: typing.Literal['TEXT']
- **Required**: Yes

### type
- **Type**: typing.Literal['ANSWER_GENERATION', 'INTENT_LABELING_GENERATION', 'QUERY_REFORMULATION', 'SELF_SERVICE_ANSWER_GENERATION', 'SELF_SERVICE_PRE_PROCESSING']
- **Required**: Yes

### visibilityStatus
- **Type**: typing.Literal['PUBLISHED', 'SAVED']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAIPromptResponse

### aiPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIPromptData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAIPromptVersionRequest

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### modifiedTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# CreateAIPromptVersionResponse

### aiPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIPromptData'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssistantAssociationRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### association
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantAssociationInputData'>
- **Required**: Yes

### associationType
- **Type**: typing.Literal['KNOWLEDGE_BASE']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAssistantAssociationResponse

### assistantAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantAssociationData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssistantRequest

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['AGENT']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ServerSideEncryptionConfiguration]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAssistantResponse

### assistant
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContentAssociationRequest

### association
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentAssociationContents'>
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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateContentAssociationResponse

### contentAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentAssociationData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateContentRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]

### overrideLinkOutUri
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### title
- **Type**: typing.Optional[str]


# CreateContentResponse

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKnowledgeBaseRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RenderingConfiguration]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ServerSideEncryptionConfiguration]

### sourceConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SourceConfiguration, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SourceConfigurationOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### vectorIngestionConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.VectorIngestionConfiguration, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.VectorIngestionConfigurationOutput, NoneType]


# CreateKnowledgeBaseResponse

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.KnowledgeBaseData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMessageTemplateAttachmentRequest

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


# CreateMessageTemplateAttachmentResponse

### attachment
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateAttachment'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMessageTemplateRequest

### channelSubtype
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### content
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateContentProvider, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateContentProviderOutput]
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateAttributes, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateAttributesOutput, NoneType]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GroupingConfiguration, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GroupingConfigurationOutput, NoneType]

### language
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateMessageTemplateResponse

### messageTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMessageTemplateVersionRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateContentSha256
- **Type**: typing.Optional[str]


# CreateMessageTemplateVersionResponse

### messageTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ExtendedMessageTemplateData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateQuickResponseRequest

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseDataProvider'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### channels
- **Type**: typing.Optional[typing.List[str]]

### clientToken
- **Type**: typing.Optional[str]

### contentType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GroupingConfiguration, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GroupingConfigurationOutput, NoneType]

### isActive
- **Type**: typing.Optional[bool]

### language
- **Type**: typing.Optional[str]

### shortcutKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateQuickResponseResponse

### quickResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSessionRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### aiAgentConfiguration
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE'], aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentConfigurationData]]

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tagFilter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagFilter, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagFilterOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSessionResponse

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SessionData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# CustomerProfileAttributes

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


# CustomerProfileAttributesOutput

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


# DataDetails

### contentData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentDataDetails]

### generativeData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GenerativeDataDetails]

### intentDetectedData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.IntentDetectedDataDetails]

### sourceContentData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SourceContentDataDetails]


# DataDetailsPaginator

### contentData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentDataDetails]

### generativeData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GenerativeDataDetailsPaginator]

### intentDetectedData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.IntentDetectedDataDetails]

### sourceContentData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SourceContentDataDetails]


# DataReference

### contentReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentReference]

### generativeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GenerativeReference]


# DataSummary

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.DataDetails'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.DataReference'>
- **Required**: Yes


# DataSummaryPaginator

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.DataDetailsPaginator'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.DataReference'>
- **Required**: Yes


# DeactivateMessageTemplateRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeactivateMessageTemplateResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAIAgentRequest

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAIAgentVersionRequest

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteAIGuardrailRequest

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAIGuardrailVersionRequest

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteAIPromptRequest

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAIPromptVersionRequest

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes


# DeleteAssistantAssociationRequest

### assistantAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssistantRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContentAssociationRequest

### contentAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContentRequest

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImportJobRequest

### importJobId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKnowledgeBaseRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMessageTemplateAttachmentRequest

### attachmentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMessageTemplateRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQuickResponseRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# Document

### contentReference
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentReference'>
- **Required**: Yes

### excerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.DocumentText]

### title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.DocumentText]


# DocumentText

### highlights
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.Highlight]]

### text
- **Type**: typing.Optional[str]


# EmailHeader

### name
- **Type**: typing.Optional[str]

### value
- **Type**: typing.Optional[str]


# EmailMessageTemplateContent

### body
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.EmailMessageTemplateContentBody]

### headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.EmailHeader]]

### subject
- **Type**: typing.Optional[str]


# EmailMessageTemplateContentBody

### html
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateBodyContentProvider]

### plainText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateBodyContentProvider]


# EmailMessageTemplateContentOutput

### body
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.EmailMessageTemplateContentBody]

### headers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.EmailHeader]]

### subject
- **Type**: typing.Optional[str]


# ExtendedMessageTemplateData

### channelSubtype
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateContentProviderOutput'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateAttachment]]

### attributeTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AGENT', 'CUSTOM', 'CUSTOMER_PROFILE', 'SYSTEM']]]

### defaultAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateAttributesOutput]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GroupingConfigurationOutput]

### isActive
- **Type**: typing.Optional[bool]

### language
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### versionNumber
- **Type**: typing.Optional[int]


# ExternalSourceConfiguration

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.Configuration'>
- **Required**: Yes

### source
- **Type**: typing.Literal['AMAZON_CONNECT']
- **Required**: Yes


# Filter

### field
- **Type**: typing.Literal['NAME']
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# FixedSizeChunkingConfiguration

### maxTokens
- **Type**: <class 'int'>
- **Required**: Yes

### overlapPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# GenerativeContentFeedbackData

### relevance
- **Type**: typing.Literal['HELPFUL', 'NOT_HELPFUL']
- **Required**: Yes


# GenerativeDataDetails

### completion
- **Type**: <class 'str'>
- **Required**: Yes

### rankingData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RankingData'>
- **Required**: Yes

### references
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# GenerativeDataDetailsPaginator

### completion
- **Type**: <class 'str'>
- **Required**: Yes

### rankingData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RankingData'>
- **Required**: Yes

### references
- **Type**: typing.List[typing.Dict[str, typing.Any]]
- **Required**: Yes


# GenerativeReference

### generationId
- **Type**: typing.Optional[str]

### modelId
- **Type**: typing.Optional[str]


# GetAIAgentRequest

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAIAgentResponse

### aiAgent
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentData'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetAIGuardrailRequest

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAIGuardrailResponse

### aiGuardrail
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailData'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetAIPromptRequest

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAIPromptResponse

### aiPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIPromptData'>
- **Required**: Yes

### versionNumber
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetAssistantAssociationRequest

### assistantAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssistantAssociationResponse

### assistantAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantAssociationData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetAssistantRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssistantResponse

### assistant
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetContentAssociationRequest

### contentAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetContentAssociationResponse

### contentAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentAssociationData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetContentRequest

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetContentResponse

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetContentSummaryRequest

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetContentSummaryResponse

### contentSummary
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetImportJobRequest

### importJobId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetImportJobResponse

### importJob
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ImportJobData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetKnowledgeBaseRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKnowledgeBaseResponse

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.KnowledgeBaseData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetMessageTemplateRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMessageTemplateResponse

### messageTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ExtendedMessageTemplateData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetNextMessageRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### nextMessageToken
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetNextMessageResponse

### conversationSessionData
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RuntimeSessionData]
- **Required**: Yes

### conversationState
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ConversationState'>
- **Required**: Yes

### nextMessageToken
- **Type**: <class 'str'>
- **Required**: Yes

### requestMessageId
- **Type**: <class 'str'>
- **Required**: Yes

### response
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageOutput'>
- **Required**: Yes

### type
- **Type**: typing.Literal['TEXT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetQuickResponseRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetQuickResponseResponse

### quickResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecommendationsRequest

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


# GetRecommendationsResponse

### recommendations
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RecommendationData]
- **Required**: Yes

### triggers
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RecommendationTrigger]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GetSessionRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionResponse

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SessionData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# GroupingConfiguration

### criteria
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


# GroupingConfigurationOutput

### criteria
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


# GuardrailContentFilterConfig

### inputStrength
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes

### outputStrength
- **Type**: typing.Literal['HIGH', 'LOW', 'MEDIUM', 'NONE']
- **Required**: Yes

### type
- **Type**: typing.Literal['HATE', 'INSULTS', 'MISCONDUCT', 'PROMPT_ATTACK', 'SEXUAL', 'VIOLENCE']
- **Required**: Yes


# GuardrailContextualGroundingFilterConfig

### threshold
- **Type**: <class 'float'>
- **Required**: Yes

### type
- **Type**: typing.Literal['GROUNDING', 'RELEVANCE']
- **Required**: Yes


# GuardrailManagedWordsConfig

### type
- **Type**: typing.Literal['PROFANITY']
- **Required**: Yes


# GuardrailPiiEntityConfig

### action
- **Type**: typing.Literal['ANONYMIZE', 'BLOCK']
- **Required**: Yes

### type
- **Type**: typing.Literal['ADDRESS', 'AGE', 'AWS_ACCESS_KEY', 'AWS_SECRET_KEY', 'CA_HEALTH_NUMBER', 'CA_SOCIAL_INSURANCE_NUMBER', 'CREDIT_DEBIT_CARD_CVV', 'CREDIT_DEBIT_CARD_EXPIRY', 'CREDIT_DEBIT_CARD_NUMBER', 'DRIVER_ID', 'EMAIL', 'INTERNATIONAL_BANK_ACCOUNT_NUMBER', 'IP_ADDRESS', 'LICENSE_PLATE', 'MAC_ADDRESS', 'NAME', 'PASSWORD', 'PHONE', 'PIN', 'SWIFT_CODE', 'UK_NATIONAL_HEALTH_SERVICE_NUMBER', 'UK_NATIONAL_INSURANCE_NUMBER', 'UK_UNIQUE_TAXPAYER_REFERENCE_NUMBER', 'URL', 'USERNAME', 'US_BANK_ACCOUNT_NUMBER', 'US_BANK_ROUTING_NUMBER', 'US_INDIVIDUAL_TAX_IDENTIFICATION_NUMBER', 'US_PASSPORT_NUMBER', 'US_SOCIAL_SECURITY_NUMBER', 'VEHICLE_IDENTIFICATION_NUMBER']
- **Required**: Yes


# GuardrailRegexConfig

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


# GuardrailTopicConfig

### definition
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DENY']
- **Required**: Yes

### examples
- **Type**: typing.Optional[typing.List[str]]


# GuardrailTopicConfigOutput

### definition
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['DENY']
- **Required**: Yes

### examples
- **Type**: typing.Optional[typing.List[str]]


# GuardrailWordConfig

### text
- **Type**: <class 'str'>
- **Required**: Yes


# HierarchicalChunkingConfiguration

### levelConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.HierarchicalChunkingLevelConfiguration]
- **Required**: Yes

### overlapTokens
- **Type**: <class 'int'>
- **Required**: Yes


# HierarchicalChunkingConfigurationOutput

### levelConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.HierarchicalChunkingLevelConfiguration]
- **Required**: Yes

### overlapTokens
- **Type**: <class 'int'>
- **Required**: Yes


# HierarchicalChunkingLevelConfiguration

### maxTokens
- **Type**: <class 'int'>
- **Required**: Yes


# Highlight

### beginOffsetInclusive
- **Type**: typing.Optional[int]

### endOffsetExclusive
- **Type**: typing.Optional[int]


# ImportJobData

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ExternalSourceConfiguration]

### failedRecordReport
- **Type**: typing.Optional[str]

### metadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# ImportJobSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ExternalSourceConfiguration]

### metadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# IntentDetectedDataDetails

### intent
- **Type**: <class 'str'>
- **Required**: Yes

### intentId
- **Type**: <class 'str'>
- **Required**: Yes


# IntentInputData

### intentId
- **Type**: <class 'str'>
- **Required**: Yes


# KnowledgeBaseAssociationConfigurationData

### contentTagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagFilter]

### maxResults
- **Type**: typing.Optional[int]

### overrideKnowledgeBaseSearchType
- **Type**: typing.Optional[typing.Literal['HYBRID', 'SEMANTIC']]


# KnowledgeBaseAssociationConfigurationDataOutput

### contentTagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagFilterOutput]

### maxResults
- **Type**: typing.Optional[int]

### overrideKnowledgeBaseSearchType
- **Type**: typing.Optional[typing.Literal['HYBRID', 'SEMANTIC']]


# KnowledgeBaseAssociationData

### knowledgeBaseArn
- **Type**: typing.Optional[str]

### knowledgeBaseId
- **Type**: typing.Optional[str]


# KnowledgeBaseData

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RenderingConfiguration]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ServerSideEncryptionConfiguration]

### sourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SourceConfigurationOutput]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### vectorIngestionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.VectorIngestionConfigurationOutput]


# KnowledgeBaseSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RenderingConfiguration]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ServerSideEncryptionConfiguration]

### sourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SourceConfigurationOutput]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### vectorIngestionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.VectorIngestionConfigurationOutput]


# ListAIAgentVersionsRequest

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


# ListAIAgentVersionsRequestPaginate

### aiAgentId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListAIAgentVersionsResponse

### aiAgentVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAIAgentsRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]


# ListAIAgentsRequestPaginate

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListAIAgentsResponse

### aiAgentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAIGuardrailVersionsRequest

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


# ListAIGuardrailVersionsRequestPaginate

### aiGuardrailId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListAIGuardrailVersionsResponse

### aiGuardrailVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAIGuardrailsRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAIGuardrailsRequestPaginate

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListAIGuardrailsResponse

### aiGuardrailSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAIPromptVersionsRequest

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


# ListAIPromptVersionsRequestPaginate

### aiPromptId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListAIPromptVersionsResponse

### aiPromptVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIPromptVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAIPromptsRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]


# ListAIPromptsRequestPaginate

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### origin
- **Type**: typing.Optional[typing.Literal['CUSTOMER', 'SYSTEM']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListAIPromptsResponse

### aiPromptSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIPromptSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssistantAssociationsRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAssistantAssociationsRequestPaginate

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListAssistantAssociationsResponse

### assistantAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListAssistantsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAssistantsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListAssistantsResponse

### assistantSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListContentAssociationsRequest

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


# ListContentAssociationsRequestPaginate

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListContentAssociationsResponse

### contentAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListContentsRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListContentsRequestPaginate

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListContentsResponse

### contentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListImportJobsRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListImportJobsRequestPaginate

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListImportJobsResponse

### importJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ImportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListKnowledgeBasesResponse

### knowledgeBaseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.KnowledgeBaseSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMessageTemplateVersionsRequest

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


# ListMessageTemplateVersionsRequestPaginate

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListMessageTemplateVersionsResponse

### messageTemplateVersionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateVersionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMessageTemplatesRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListMessageTemplatesRequestPaginate

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListMessageTemplatesResponse

### messageTemplateSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListMessagesRequest

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


# ListMessagesRequestPaginate

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListMessagesResponse

### messages
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListQuickResponsesRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListQuickResponsesRequestPaginate

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# ListQuickResponsesResponse

### quickResponseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# ManagedSourceConfiguration

### webCrawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.WebCrawlerConfiguration]


# ManagedSourceConfigurationOutput

### webCrawlerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.WebCrawlerConfigurationOutput]


# ManualSearchAIAgentConfiguration

### answerGenerationAIGuardrailId
- **Type**: typing.Optional[str]

### answerGenerationAIPromptId
- **Type**: typing.Optional[str]

### associationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssociationConfiguration]]

### locale
- **Type**: typing.Optional[str]


# ManualSearchAIAgentConfigurationOutput

### answerGenerationAIGuardrailId
- **Type**: typing.Optional[str]

### answerGenerationAIPromptId
- **Type**: typing.Optional[str]

### associationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssociationConfigurationOutput]]

### locale
- **Type**: typing.Optional[str]


# MessageData

### text
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TextMessage]


# MessageInput

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageData'>
- **Required**: Yes


# MessageOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageData'>
- **Required**: Yes


# MessageTemplateAttachment

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


# MessageTemplateAttributes

### agentAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AgentAttributes]

### customAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### customerProfileAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.CustomerProfileAttributes]

### systemAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SystemAttributes]


# MessageTemplateAttributesOutput

### agentAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AgentAttributes]

### customAttributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### customerProfileAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.CustomerProfileAttributesOutput]

### systemAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SystemAttributes]


# MessageTemplateBodyContentProvider

### content
- **Type**: typing.Optional[str]


# MessageTemplateContentProvider

### email
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.EmailMessageTemplateContent]

### sms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SMSMessageTemplateContent]


# MessageTemplateContentProviderOutput

### email
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.EmailMessageTemplateContentOutput]

### sms
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SMSMessageTemplateContent]


# MessageTemplateData

### channelSubtype
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateContentProviderOutput'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateAttributesOutput]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GroupingConfigurationOutput]

### language
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# MessageTemplateFilterField

### name
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQUALS', 'PREFIX']
- **Required**: Yes

### includeNoExistence
- **Type**: typing.Optional[bool]

### values
- **Type**: typing.Optional[typing.List[str]]


# MessageTemplateOrderField

### name
- **Type**: <class 'str'>
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# MessageTemplateQueryField

### name
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['CONTAINS', 'CONTAINS_AND_PREFIX']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes

### allowFuzziness
- **Type**: typing.Optional[bool]

### priority
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


# MessageTemplateSearchExpression

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateFilterField]]

### orderOnField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateOrderField]

### queries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateQueryField]]


# MessageTemplateSearchResultData

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GroupingConfigurationOutput]

### isActive
- **Type**: typing.Optional[bool]

### language
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### versionNumber
- **Type**: typing.Optional[int]


# MessageTemplateSummary

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


# MessageTemplateVersionSummary

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


# NotifyRecommendationsReceivedError

### message
- **Type**: typing.Optional[str]

### recommendationId
- **Type**: typing.Optional[str]


# NotifyRecommendationsReceivedRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationIds
- **Type**: typing.List[str]
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# NotifyRecommendationsReceivedResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.NotifyRecommendationsReceivedError]
- **Required**: Yes

### recommendationIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# OrCondition

### andConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagCondition]]

### tagCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagCondition]


# OrConditionOutput

### andConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagCondition]]

### tagCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagCondition]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParsingConfiguration

### parsingStrategy
- **Type**: typing.Literal['BEDROCK_FOUNDATION_MODEL']
- **Required**: Yes

### bedrockFoundationModelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.BedrockFoundationModelConfigurationForParsing]


# ParsingPrompt

### parsingPromptText
- **Type**: <class 'str'>
- **Required**: Yes


# PutFeedbackRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### contentFeedback
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentFeedbackData'>
- **Required**: Yes

### targetId
- **Type**: <class 'str'>
- **Required**: Yes

### targetType
- **Type**: typing.Literal['RECOMMENDATION', 'RESULT']
- **Required**: Yes


# PutFeedbackResponse

### assistantArn
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### contentFeedback
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentFeedbackData'>
- **Required**: Yes

### targetId
- **Type**: <class 'str'>
- **Required**: Yes

### targetType
- **Type**: typing.Literal['RECOMMENDATION', 'RESULT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# QueryAssistantRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QueryCondition]]

### queryInputData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QueryInputData]

### queryText
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]


# QueryAssistantRequestPaginate

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### overrideKnowledgeBaseSearchType
- **Type**: typing.Optional[typing.Literal['HYBRID', 'SEMANTIC']]

### queryCondition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QueryCondition]]

### queryInputData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QueryInputData]

### queryText
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# QueryAssistantResponse

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResultData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# QueryAssistantResponsePaginator

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResultDataPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# QueryCondition

### single
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QueryConditionItem]


# QueryConditionItem

### comparator
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### field
- **Type**: typing.Literal['RESULT_TYPE']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# QueryInputData

### intentInputData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.IntentInputData]

### queryTextInputData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QueryTextInputData]


# QueryRecommendationTriggerData

### text
- **Type**: typing.Optional[str]


# QueryTextInputData

### text
- **Type**: <class 'str'>
- **Required**: Yes


# QuickResponseContentProvider

### content
- **Type**: typing.Optional[str]


# QuickResponseContents

### markdown
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseContentProvider]

### plainText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseContentProvider]


# QuickResponseData

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseContents]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GroupingConfigurationOutput]

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


# QuickResponseDataProvider

### content
- **Type**: typing.Optional[str]


# QuickResponseFilterField

### name
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQUALS', 'PREFIX']
- **Required**: Yes

### includeNoExistence
- **Type**: typing.Optional[bool]

### values
- **Type**: typing.Optional[typing.List[str]]


# QuickResponseOrderField

### name
- **Type**: <class 'str'>
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# QuickResponseQueryField

### name
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['CONTAINS', 'CONTAINS_AND_PREFIX']
- **Required**: Yes

### values
- **Type**: typing.List[str]
- **Required**: Yes

### allowFuzziness
- **Type**: typing.Optional[bool]

### priority
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


# QuickResponseSearchExpression

### filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseFilterField]]

### orderOnField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseOrderField]

### queries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseQueryField]]


# QuickResponseSearchResultData

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### contents
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseContents'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GroupingConfigurationOutput]

### language
- **Type**: typing.Optional[str]

### lastModifiedBy
- **Type**: typing.Optional[str]

### shortcutKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# QuickResponseSummary

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


# RankingData

### relevanceLevel
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### relevanceScore
- **Type**: typing.Optional[float]


# RecommendationData

### recommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.DataSummary]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.Document]

### relevanceLevel
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### relevanceScore
- **Type**: typing.Optional[float]

### type
- **Type**: typing.Optional[typing.Literal['DETECTED_INTENT', 'GENERATIVE_ANSWER', 'GENERATIVE_RESPONSE', 'KNOWLEDGE_CONTENT']]


# RecommendationTrigger

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RecommendationTriggerData'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### recommendationIds
- **Type**: typing.List[str]
- **Required**: Yes

### source
- **Type**: typing.Literal['ISSUE_DETECTION', 'OTHER', 'RULE_EVALUATION']
- **Required**: Yes

### type
- **Type**: typing.Literal['GENERATIVE', 'QUERY']
- **Required**: Yes


# RecommendationTriggerData

### query
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QueryRecommendationTriggerData]


# RemoveAssistantAIAgentRequest

### aiAgentType
- **Type**: typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE']
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveKnowledgeBaseTemplateUriRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# RenderMessageTemplateRequest

### attributes
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateAttributes, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateAttributesOutput]
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes


# RenderMessageTemplateResponse

### attachments
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateAttachment]
- **Required**: Yes

### attributesNotInterpolated
- **Type**: typing.List[str]
- **Required**: Yes

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateContentProviderOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# RenderingConfiguration

### templateUri
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


# ResultData

### resultId
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.DataSummary]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.Document]

### relevanceScore
- **Type**: typing.Optional[float]

### type
- **Type**: typing.Optional[typing.Literal['GENERATIVE_ANSWER', 'INTENT_ANSWER', 'KNOWLEDGE_CONTENT']]


# ResultDataPaginator

### resultId
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.DataSummaryPaginator]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.Document]

### relevanceScore
- **Type**: typing.Optional[float]

### type
- **Type**: typing.Optional[typing.Literal['GENERATIVE_ANSWER', 'INTENT_ANSWER', 'KNOWLEDGE_CONTENT']]


# RuntimeSessionData

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RuntimeSessionDataValue'>
- **Required**: Yes


# RuntimeSessionDataValue

### stringValue
- **Type**: typing.Optional[str]


# SMSMessageTemplateContent

### body
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SMSMessageTemplateContentBody]


# SMSMessageTemplateContentBody

### plainText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateBodyContentProvider]


# SearchContentRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SearchExpression'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchContentRequestPaginate

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SearchExpression'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# SearchContentResponse

### contentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchExpression

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.Filter]
- **Required**: Yes


# SearchMessageTemplatesRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateSearchExpression'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchMessageTemplatesRequestPaginate

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateSearchExpression'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# SearchMessageTemplatesResponse

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateSearchResultData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchQuickResponsesRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseSearchExpression'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchQuickResponsesRequestPaginate

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseSearchExpression'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# SearchQuickResponsesResponse

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseSearchResultData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchSessionsRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SearchExpression'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# SearchSessionsRequestPaginate

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SearchExpression'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.PaginatorConfig]


# SearchSessionsResponse

### sessionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SeedUrl

### url
- **Type**: typing.Optional[str]


# SelfServiceAIAgentConfiguration

### associationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssociationConfiguration]]

### selfServiceAIGuardrailId
- **Type**: typing.Optional[str]

### selfServiceAnswerGenerationAIPromptId
- **Type**: typing.Optional[str]

### selfServicePreProcessingAIPromptId
- **Type**: typing.Optional[str]


# SelfServiceAIAgentConfigurationOutput

### associationConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssociationConfigurationOutput]]

### selfServiceAIGuardrailId
- **Type**: typing.Optional[str]

### selfServiceAnswerGenerationAIPromptId
- **Type**: typing.Optional[str]

### selfServicePreProcessingAIPromptId
- **Type**: typing.Optional[str]


# SelfServiceConversationHistory

### turnNumber
- **Type**: <class 'int'>
- **Required**: Yes

### botResponse
- **Type**: typing.Optional[str]

### inputTranscript
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


# SendMessageRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### message
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageInput'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['TEXT']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### conversationContext
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ConversationContext]


# SendMessageResponse

### nextMessageToken
- **Type**: <class 'str'>
- **Required**: Yes

### requestMessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# ServerSideEncryptionConfiguration

### kmsKeyId
- **Type**: typing.Optional[str]


# SessionData

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
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE'], aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentConfigurationData]]

### description
- **Type**: typing.Optional[str]

### integrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SessionIntegrationConfiguration]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagFilterOutput]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SessionIntegrationConfiguration

### topicIntegrationArn
- **Type**: typing.Optional[str]


# SessionSummary

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


# SourceConfiguration

### appIntegrations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AppIntegrationsConfiguration]

### managedSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ManagedSourceConfiguration]


# SourceConfigurationOutput

### appIntegrations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AppIntegrationsConfigurationOutput]

### managedSourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ManagedSourceConfigurationOutput]


# SourceContentDataDetails

### id
- **Type**: <class 'str'>
- **Required**: Yes

### rankingData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RankingData'>
- **Required**: Yes

### textData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TextData'>
- **Required**: Yes

### type
- **Type**: typing.Literal['KNOWLEDGE_CONTENT']
- **Required**: Yes

### citationSpan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.CitationSpan]


# StartContentUploadRequest

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### presignedUrlTimeToLive
- **Type**: typing.Optional[int]


# StartContentUploadResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# StartImportJobRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ExternalSourceConfiguration]

### metadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartImportJobResponse

### importJob
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ImportJobData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# SystemAttributes

### customerEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SystemEndpointAttributes]

### name
- **Type**: typing.Optional[str]

### systemEndpoint
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SystemEndpointAttributes]


# SystemEndpointAttributes

### address
- **Type**: typing.Optional[str]


# TagCondition

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: typing.Optional[str]


# TagFilter

### andConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagCondition]]

### orConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.OrCondition]]

### tagCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagCondition]


# TagFilterOutput

### andConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagCondition]]

### orConditions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.OrConditionOutput]]

### tagCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagCondition]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TextData

### excerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.DocumentText]

### title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.DocumentText]


# TextFullAIPromptEditTemplateConfiguration

### text
- **Type**: <class 'str'>
- **Required**: Yes


# TextMessage

### value
- **Type**: typing.Optional[str]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAIAgentRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentConfiguration, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentConfigurationOutput, NoneType]

### description
- **Type**: typing.Optional[str]


# UpdateAIAgentResponse

### aiAgent
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAIGuardrailRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailContentPolicyConfig, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailContentPolicyConfigOutput, NoneType]

### contextualGroundingPolicyConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailContextualGroundingPolicyConfig, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailContextualGroundingPolicyConfigOutput, NoneType]

### description
- **Type**: typing.Optional[str]

### sensitiveInformationPolicyConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailSensitiveInformationPolicyConfig, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailSensitiveInformationPolicyConfigOutput, NoneType]

### topicPolicyConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailTopicPolicyConfig, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailTopicPolicyConfigOutput, NoneType]

### wordPolicyConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailWordPolicyConfig, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailWordPolicyConfigOutput, NoneType]


# UpdateAIGuardrailResponse

### aiGuardrail
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIGuardrailData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAIPromptRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIPromptTemplateConfiguration]


# UpdateAIPromptResponse

### aiPrompt
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIPromptData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAssistantAIAgentRequest

### aiAgentType
- **Type**: typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE']
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentConfigurationData'>
- **Required**: Yes


# UpdateAssistantAIAgentResponse

### assistant
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AssistantData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateContentRequest

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: typing.Optional[typing.Dict[str, str]]

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


# UpdateContentResponse

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ContentData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateKnowledgeBaseTemplateUriRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### templateUri
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateKnowledgeBaseTemplateUriResponse

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.KnowledgeBaseData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMessageTemplateMetadataRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GroupingConfiguration, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GroupingConfigurationOutput, NoneType]

### name
- **Type**: typing.Optional[str]


# UpdateMessageTemplateMetadataResponse

### messageTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMessageTemplateRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### messageTemplateId
- **Type**: <class 'str'>
- **Required**: Yes

### content
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateContentProvider, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateContentProviderOutput, NoneType]

### defaultAttributes
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateAttributes, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateAttributesOutput, NoneType]

### language
- **Type**: typing.Optional[str]


# UpdateMessageTemplateResponse

### messageTemplate
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.MessageTemplateData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateQuickResponseRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseId
- **Type**: <class 'str'>
- **Required**: Yes

### channels
- **Type**: typing.Optional[typing.List[str]]

### content
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseDataProvider]

### contentType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GroupingConfiguration, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.GroupingConfigurationOutput, NoneType]

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


# UpdateQuickResponseResponse

### quickResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.QuickResponseData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSessionDataRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RuntimeSessionData]
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### namespace
- **Type**: typing.Optional[typing.Literal['Custom']]


# UpdateSessionDataResponse

### data
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.RuntimeSessionData]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSessionRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### aiAgentConfiguration
- **Type**: typing.Optional[typing.Dict[typing.Literal['ANSWER_RECOMMENDATION', 'MANUAL_SEARCH', 'SELF_SERVICE'], aws_resource_validator.pydantic_models.qconnect.qconnect_classes.AIAgentConfigurationData]]

### description
- **Type**: typing.Optional[str]

### tagFilter
- **Type**: typing.Union[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagFilter, aws_resource_validator.pydantic_models.qconnect.qconnect_classes.TagFilterOutput, NoneType]


# UpdateSessionResponse

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SessionData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ResponseMetadata'>
- **Required**: Yes


# UrlConfiguration

### seedUrls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SeedUrl]]


# UrlConfigurationOutput

### seedUrls
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.SeedUrl]]


# VectorIngestionConfiguration

### chunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ChunkingConfiguration]

### parsingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ParsingConfiguration]


# VectorIngestionConfigurationOutput

### chunkingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ChunkingConfigurationOutput]

### parsingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.ParsingConfiguration]


# WebCrawlerConfiguration

### urlConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.UrlConfiguration'>
- **Required**: Yes

### crawlerLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.WebCrawlerLimits]

### exclusionFilters
- **Type**: typing.Optional[typing.List[str]]

### inclusionFilters
- **Type**: typing.Optional[typing.List[str]]

### scope
- **Type**: typing.Optional[typing.Literal['HOST_ONLY', 'SUBDOMAINS']]


# WebCrawlerConfigurationOutput

### urlConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect.qconnect_classes.UrlConfigurationOutput'>
- **Required**: Yes

### crawlerLimits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect.qconnect_classes.WebCrawlerLimits]

### exclusionFilters
- **Type**: typing.Optional[typing.List[str]]

### inclusionFilters
- **Type**: typing.Optional[typing.List[str]]

### scope
- **Type**: typing.Optional[typing.Literal['HOST_ONLY', 'SUBDOMAINS']]


# WebCrawlerLimits

### rateLimit
- **Type**: typing.Optional[int]


