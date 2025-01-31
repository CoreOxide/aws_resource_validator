# wisdom_classes

# AppIntegrationsConfigurationPaginatorTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.AssistantAssociationOutputDataTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.KnowledgeBaseAssociationDataTypeDef]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.AssistantAssociationOutputDataTypeDef'>
- **Required**: Yes

### associationType
- **Type**: typing.Literal['KNOWLEDGE_BASE']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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

### description
- **Type**: typing.Optional[str]

### integrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.AssistantIntegrationConfigurationTypeDef]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.ServerSideEncryptionConfigurationTypeDef]

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

### description
- **Type**: typing.Optional[str]

### integrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.AssistantIntegrationConfigurationTypeDef]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.ServerSideEncryptionConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfigurationTypeDef

### connectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.ConnectConfigurationTypeDef]


# ConnectConfigurationTypeDef

### instanceId
- **Type**: typing.Optional[str]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.AssistantAssociationInputDataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.AssistantAssociationDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.ServerSideEncryptionConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAssistantResponseTypeDef

### assistant
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.AssistantDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ContentDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.RenderingConfigurationTypeDef]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.ServerSideEncryptionConfigurationTypeDef]

### sourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.SourceConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateKnowledgeBaseResponseTypeDef

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.KnowledgeBaseDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateQuickResponseRequestRequestTypeDef

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseDataProviderTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.GroupingConfigurationTypeDef]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSessionResponseTypeDef

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.SessionDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wisdom_classes.HighlightTypeDef]]

### text
- **Type**: typing.Optional[str]


# DocumentTypeDef

### contentReference
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ContentReferenceTypeDef'>
- **Required**: Yes

### excerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.DocumentTextTypeDef]

### title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.DocumentTextTypeDef]


# ExternalSourceConfigurationTypeDef

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ConfigurationTypeDef'>
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


# GetAssistantAssociationRequestRequestTypeDef

### assistantAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssistantAssociationResponseTypeDef

### assistantAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.AssistantAssociationDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAssistantRequestRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssistantResponseTypeDef

### assistant
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.AssistantDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ContentDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ContentSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ImportJobDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetKnowledgeBaseRequestRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKnowledgeBaseResponseTypeDef

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.KnowledgeBaseDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.RecommendationDataTypeDef]
- **Required**: Yes

### triggers
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.RecommendationTriggerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.SessionDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupingConfigurationPaginatorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.ExternalSourceConfigurationTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.ExternalSourceConfigurationTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.RenderingConfigurationTypeDef]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.ServerSideEncryptionConfigurationTypeDef]

### sourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.SourceConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# KnowledgeBaseSummaryPaginatorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.RenderingConfigurationTypeDef]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.ServerSideEncryptionConfigurationTypeDef]

### sourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.SourceConfigurationPaginatorTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.RenderingConfigurationTypeDef]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.ServerSideEncryptionConfigurationTypeDef]

### sourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.SourceConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.PaginatorConfigTypeDef]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.AssistantAssociationSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAssistantsRequestListAssistantsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.PaginatorConfigTypeDef]


# ListAssistantsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListAssistantsResponseTypeDef

### assistantSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.AssistantSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListContentsRequestListContentsPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.PaginatorConfigTypeDef]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.ContentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListImportJobsRequestListImportJobsPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.PaginatorConfigTypeDef]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.ImportJobSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.PaginatorConfigTypeDef]


# ListKnowledgeBasesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListKnowledgeBasesResponsePaginatorTypeDef

### knowledgeBaseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.KnowledgeBaseSummaryPaginatorTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListKnowledgeBasesResponseTypeDef

### knowledgeBaseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.KnowledgeBaseSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListQuickResponsesRequestListQuickResponsesPaginateTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.PaginatorConfigTypeDef]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.NotifyRecommendationsReceivedErrorTypeDef]
- **Required**: Yes

### recommendationIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# QueryAssistantRequestQueryAssistantPaginateTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### queryText
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.PaginatorConfigTypeDef]


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


# QueryAssistantResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.ResultDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# QueryRecommendationTriggerDataTypeDef

### text
- **Type**: typing.Optional[str]


# QuickResponseContentProviderTypeDef

### content
- **Type**: typing.Optional[str]


# QuickResponseContentsTypeDef

### markdown
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseContentProviderTypeDef]

### plainText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseContentProviderTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseContentsTypeDef]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.GroupingConfigurationTypeDef]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseFilterFieldTypeDef]]

### orderOnField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseOrderFieldTypeDef]

### queries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseQueryFieldTypeDef]]


# QuickResponseSearchResultDataPaginatorTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### contents
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseContentsTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.GroupingConfigurationPaginatorTypeDef]

### language
- **Type**: typing.Optional[str]

### lastModifiedBy
- **Type**: typing.Optional[str]

### shortcutKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# QuickResponseSearchResultDataTypeDef

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### contents
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseContentsTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.GroupingConfigurationTypeDef]

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


# RecommendationDataTypeDef

### document
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.DocumentTypeDef'>
- **Required**: Yes

### recommendationId
- **Type**: <class 'str'>
- **Required**: Yes

### relevanceLevel
- **Type**: typing.Optional[typing.Literal['HIGH', 'LOW', 'MEDIUM']]

### relevanceScore
- **Type**: typing.Optional[float]

### type
- **Type**: typing.Optional[typing.Literal['KNOWLEDGE_CONTENT']]


# RecommendationTriggerDataTypeDef

### query
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.QueryRecommendationTriggerDataTypeDef]


# RecommendationTriggerTypeDef

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.RecommendationTriggerDataTypeDef'>
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
- **Type**: typing.Literal['QUERY']
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

### HostId
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


# ResultDataTypeDef

### document
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.DocumentTypeDef'>
- **Required**: Yes

### resultId
- **Type**: <class 'str'>
- **Required**: Yes

### relevanceScore
- **Type**: typing.Optional[float]


# SearchContentRequestRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.SearchExpressionTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.SearchExpressionTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.PaginatorConfigTypeDef]


# SearchContentResponseTypeDef

### contentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.ContentSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchExpressionTypeDef

### filters
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.wisdom_classes.FilterTypeDef]
- **Required**: Yes


# SearchQuickResponsesRequestRequestTypeDef

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseSearchExpressionTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseSearchExpressionTypeDef'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.PaginatorConfigTypeDef]


# SearchQuickResponsesResponsePaginatorTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseSearchResultDataPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchQuickResponsesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseSearchResultDataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchSessionsRequestRequestTypeDef

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.SearchExpressionTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.SearchExpressionTypeDef'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.PaginatorConfigTypeDef]


# SearchSessionsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### sessionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom_classes.SessionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.SessionIntegrationConfigurationTypeDef]

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


# SourceConfigurationPaginatorTypeDef

### appIntegrations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.AppIntegrationsConfigurationPaginatorTypeDef]


# SourceConfigurationTypeDef

### appIntegrations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.AppIntegrationsConfigurationTypeDef]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.ExternalSourceConfigurationTypeDef]

### metadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartImportJobResponseTypeDef

### importJob
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ImportJobDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ContentDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.KnowledgeBaseDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseDataProviderTypeDef]

### contentType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom_classes.GroupingConfigurationTypeDef]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.QuickResponseDataTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


