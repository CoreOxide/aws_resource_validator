# Pydantic Models in qconnect_classes

# AmazonConnectGuideAssociationDataTypeDef

### flowId
- **Type**: typing.Optional[str]


# AppIntegrationsConfigurationExtraOutputTypeDef

### appIntegrationArn
- **Type**: <class 'str'>
- **Required**: Yes

### objectFields
- **Type**: typing.Optional[typing.List[str]]


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


# AssistantCapabilityConfigurationTypeDef

### type
- **Type**: typing.Optional[typing.Literal['V1', 'V2']]


# AssistantDataTypeDef

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

### capabilityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AssistantCapabilityConfigurationTypeDef]

### description
- **Type**: typing.Optional[str]

### integrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AssistantIntegrationConfigurationTypeDef]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ServerSideEncryptionConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# AssistantIntegrationConfigurationTypeDef

### topicIntegrationArn
- **Type**: typing.Optional[str]


# AssistantSummaryTypeDef

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

### capabilityConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AssistantCapabilityConfigurationTypeDef]

### description
- **Type**: typing.Optional[str]

### integrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AssistantIntegrationConfigurationTypeDef]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ServerSideEncryptionConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# CreateAssistantAssociationRequestRequestTypeDef

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


# CreateAssistantRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ServerSideEncryptionConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAssistantResponseTypeDef

### assistant
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.AssistantDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateContentAssociationRequestRequestTypeDef

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


# CreateContentRequestRequestTypeDef

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


# CreateKnowledgeBaseRequestRequestTypeDef

### knowledgeBaseType
- **Type**: typing.Literal['CUSTOM', 'EXTERNAL', 'QUICK_RESPONSES']
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SourceConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateKnowledgeBaseResponseTypeDef

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.KnowledgeBaseDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQuickResponseRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GroupingConfigurationTypeDef]

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


# CreateSessionRequestRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TagFilterTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSessionResponseTypeDef

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.SessionDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataDetailsTypeDef

### contentData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ContentDataDetailsTypeDef]

### generativeData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GenerativeDataDetailsTypeDef]

### sourceContentData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.SourceContentDataDetailsTypeDef]


# DataReferenceTypeDef

### contentReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.ContentReferenceTypeDef]

### generativeReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GenerativeReferenceTypeDef]


# DataSummaryTypeDef

### details
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.DataDetailsTypeDef'>
- **Required**: Yes

### reference
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.DataReferenceTypeDef'>
- **Required**: Yes


# DeleteAssistantAssociationRequestRequestTypeDef

### assistantAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAssistantRequestRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContentAssociationRequestRequestTypeDef

### contentAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteContentRequestRequestTypeDef

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImportJobRequestRequestTypeDef

### importJobId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteKnowledgeBaseRequestRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteQuickResponseRequestRequestTypeDef

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


# ExternalSourceConfigurationTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ConfigurationTypeDef'>
- **Required**: Yes

### source
- **Type**: typing.Literal['AMAZON_CONNECT']
- **Required**: Yes


# FilterTypeDef

### field
- **Type**: typing.Literal['NAME']
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# GenerativeContentFeedbackDataTypeDef

### relevance
- **Type**: typing.Literal['HELPFUL', 'NOT_HELPFUL']
- **Required**: Yes


# GenerativeDataDetailsTypeDef

### completion
- **Type**: <class 'str'>
- **Required**: Yes

### rankingData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.RankingDataTypeDef'>
- **Required**: Yes

### references
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.DataSummaryTypeDef]
- **Required**: Yes


# GenerativeReferenceTypeDef

### generationId
- **Type**: typing.Optional[str]

### modelId
- **Type**: typing.Optional[str]


# GetAssistantAssociationRequestRequestTypeDef

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


# GetAssistantRequestRequestTypeDef

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


# GetContentAssociationRequestRequestTypeDef

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


# GetContentRequestRequestTypeDef

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


# GetContentSummaryRequestRequestTypeDef

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


# GetImportJobRequestRequestTypeDef

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


# GetKnowledgeBaseRequestRequestTypeDef

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


# GetQuickResponseRequestRequestTypeDef

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


# GetRecommendationsRequestRequestTypeDef

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


# GetSessionRequestRequestTypeDef

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


# GroupingConfigurationExtraOutputTypeDef

### criteria
- **Type**: typing.Optional[str]

### values
- **Type**: typing.Optional[typing.List[str]]


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
- **Type**: typing.Literal['CUSTOM', 'EXTERNAL', 'QUICK_RESPONSES']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATE_IN_PROGRESS', 'DELETED', 'DELETE_FAILED', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

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


# KnowledgeBaseSummaryTypeDef

### knowledgeBaseArn
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseType
- **Type**: typing.Literal['CUSTOM', 'EXTERNAL', 'QUICK_RESPONSES']
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


# ListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListAssistantAssociationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssistantsRequestListAssistantsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListAssistantsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAssistantsResponseTypeDef

### assistantSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.AssistantSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListContentAssociationsRequestListContentAssociationsPaginateTypeDef

### contentId
- **Type**: <class 'str'>
- **Required**: Yes

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListContentAssociationsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListContentsRequestListContentsPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListContentsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImportJobsRequestListImportJobsPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListImportJobsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListKnowledgeBasesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListKnowledgeBasesResponseTypeDef

### knowledgeBaseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.KnowledgeBaseSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListQuickResponsesRequestListQuickResponsesPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# ListQuickResponsesRequestRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListQuickResponsesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NotifyRecommendationsReceivedErrorTypeDef

### message
- **Type**: typing.Optional[str]

### recommendationId
- **Type**: typing.Optional[str]


# NotifyRecommendationsReceivedRequestRequestTypeDef

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


# PutFeedbackRequestRequestTypeDef

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


# QueryAssistantRequestQueryAssistantPaginateTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### queryText
- **Type**: <class 'str'>
- **Required**: Yes

### queryCondition
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.QueryConditionTypeDef]]

### sessionId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# QueryAssistantRequestRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### queryText
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### queryCondition
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.QueryConditionTypeDef]]

### sessionId
- **Type**: typing.Optional[str]


# QueryAssistantResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.ResultDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# QueryRecommendationTriggerDataTypeDef

### text
- **Type**: typing.Optional[str]


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

### name
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['EQUALS', 'PREFIX']
- **Required**: Yes

### includeNoExistence
- **Type**: typing.Optional[bool]

### values
- **Type**: typing.Optional[typing.Sequence[str]]


# QuickResponseOrderFieldTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### order
- **Type**: typing.Optional[typing.Literal['ASC', 'DESC']]


# QuickResponseQueryFieldTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### operator
- **Type**: typing.Literal['CONTAINS', 'CONTAINS_AND_PREFIX']
- **Required**: Yes

### values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### allowFuzziness
- **Type**: typing.Optional[bool]

### priority
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]


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

### recommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.DataSummaryTypeDef]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.DocumentTypeDef]

### relevanceLevel
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### relevanceScore
- **Type**: typing.Optional[float]

### type
- **Type**: typing.Optional[typing.Literal['GENERATIVE_ANSWER', 'GENERATIVE_RESPONSE', 'KNOWLEDGE_CONTENT']]


# RecommendationTriggerDataTypeDef

### query
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.QueryRecommendationTriggerDataTypeDef]


# RecommendationTriggerTypeDef

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.RecommendationTriggerDataTypeDef'>
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


# RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
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


# ResultDataTypeDef

### resultId
- **Type**: <class 'str'>
- **Required**: Yes

### data
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.DataSummaryTypeDef]

### document
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.DocumentTypeDef]

### relevanceScore
- **Type**: typing.Optional[float]

### type
- **Type**: typing.Optional[typing.Literal['GENERATIVE_ANSWER', 'KNOWLEDGE_CONTENT']]


# SearchContentRequestRequestTypeDef

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


# SearchContentRequestSearchContentPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.SearchExpressionTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# SearchContentResponseTypeDef

### contentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.ContentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchExpressionTypeDef

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.qconnect_classes.FilterTypeDef]
- **Required**: Yes


# SearchQuickResponsesRequestRequestTypeDef

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


# SearchQuickResponsesRequestSearchQuickResponsesPaginateTypeDef

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


# SearchQuickResponsesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.QuickResponseSearchResultDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchSessionsRequestRequestTypeDef

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


# SearchSessionsRequestSearchSessionsPaginateTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.SearchExpressionTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.PaginatorConfigTypeDef]


# SearchSessionsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### sessionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.qconnect_classes.SessionSummaryTypeDef]
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


# SourceConfigurationExtraOutputTypeDef

### appIntegrations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AppIntegrationsConfigurationExtraOutputTypeDef]


# SourceConfigurationOutputTypeDef

### appIntegrations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AppIntegrationsConfigurationOutputTypeDef]


# SourceConfigurationTypeDef

### appIntegrations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.AppIntegrationsConfigurationTypeDef]


# SourceContentDataDetailsTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### rankingData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.RankingDataTypeDef'>
- **Required**: Yes

### textData
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.TextDataTypeDef'>
- **Required**: Yes

### type
- **Type**: typing.Literal['KNOWLEDGE_CONTENT']
- **Required**: Yes


# StartContentUploadRequestRequestTypeDef

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


# StartImportJobRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

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


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateContentRequestRequestTypeDef

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


# UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef

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


# UpdateQuickResponseRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.GroupingConfigurationTypeDef]

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


# UpdateSessionRequestRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### tagFilter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.qconnect_classes.TagFilterTypeDef]


# UpdateSessionResponseTypeDef

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.SessionDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.qconnect_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


