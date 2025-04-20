# Wisdom Wisdom Classes

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.AssistantAssociationOutputData'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.KnowledgeBaseAssociationData]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.AssistantAssociationOutputData'>
- **Required**: Yes

### associationType
- **Type**: typing.Literal['KNOWLEDGE_BASE']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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

### description
- **Type**: typing.Optional[str]

### integrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.AssistantIntegrationConfiguration]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ServerSideEncryptionConfiguration]

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

### description
- **Type**: typing.Optional[str]

### integrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.AssistantIntegrationConfiguration]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ServerSideEncryptionConfiguration]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Configuration

### connectConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ConnectConfiguration]


# ConnectConfiguration

### instanceId
- **Type**: typing.Optional[str]


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


# ContentReference

### contentArn
- **Type**: typing.Optional[str]

### contentId
- **Type**: typing.Optional[str]

### knowledgeBaseArn
- **Type**: typing.Optional[str]

### knowledgeBaseId
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


# CreateAssistantAssociationRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### association
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.AssistantAssociationInputData'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.AssistantAssociationData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ServerSideEncryptionConfiguration]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAssistantResponse

### assistant
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.AssistantData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ContentData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
- **Required**: Yes


# CreateKnowledgeBaseRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.RenderingConfiguration]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ServerSideEncryptionConfiguration]

### sourceConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.SourceConfiguration, aws_resource_validator.pydantic_models.wisdom.wisdom_classes.SourceConfigurationOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateKnowledgeBaseResponse

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.KnowledgeBaseData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
- **Required**: Yes


# CreateQuickResponseRequest

### content
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseDataProvider'>
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.GroupingConfiguration, aws_resource_validator.pydantic_models.wisdom.wisdom_classes.GroupingConfigurationOutput, NoneType]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSessionRequest

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSessionResponse

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.SessionData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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


# DeleteQuickResponseRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### quickResponseId
- **Type**: <class 'str'>
- **Required**: Yes


# Document

### contentReference
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ContentReference'>
- **Required**: Yes

### excerpt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.DocumentText]

### title
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.DocumentText]


# DocumentText

### highlights
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.Highlight]]

### text
- **Type**: typing.Optional[str]


# ExternalSourceConfiguration

### configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.Configuration'>
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


# GetAssistantAssociationRequest

### assistantAssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssistantAssociationResponse

### assistantAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.AssistantAssociationData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
- **Required**: Yes


# GetAssistantRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAssistantResponse

### assistant
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.AssistantData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ContentData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ContentSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ImportJobData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
- **Required**: Yes


# GetKnowledgeBaseRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes


# GetKnowledgeBaseResponse

### knowledgeBase
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.KnowledgeBaseData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.RecommendationData]
- **Required**: Yes

### triggers
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.RecommendationTrigger]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.SessionData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ExternalSourceConfiguration]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ExternalSourceConfiguration]

### metadata
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.RenderingConfiguration]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ServerSideEncryptionConfiguration]

### sourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.SourceConfigurationOutput]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# KnowledgeBaseSummary

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.RenderingConfiguration]

### serverSideEncryptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ServerSideEncryptionConfiguration]

### sourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.SourceConfigurationOutput]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.PaginatorConfig]


# ListAssistantAssociationsResponse

### assistantAssociationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.AssistantAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.PaginatorConfig]


# ListAssistantsResponse

### assistantSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.AssistantSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.PaginatorConfig]


# ListContentsResponse

### contentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ContentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.PaginatorConfig]


# ListImportJobsResponse

### importJobSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ImportJobSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.PaginatorConfig]


# ListKnowledgeBasesResponse

### knowledgeBaseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.KnowledgeBaseSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.PaginatorConfig]


# ListQuickResponsesResponse

### quickResponseSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.NotifyRecommendationsReceivedError]
- **Required**: Yes

### recommendationIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# QueryAssistantRequest

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


# QueryAssistantRequestPaginate

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### queryText
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.PaginatorConfig]


# QueryAssistantResponse

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResultData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# QueryRecommendationTriggerData

### text
- **Type**: typing.Optional[str]


# QuickResponseContentProvider

### content
- **Type**: typing.Optional[str]


# QuickResponseContents

### markdown
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseContentProvider]

### plainText
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseContentProvider]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseContents]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.GroupingConfigurationOutput]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseFilterField]]

### orderOnField
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseOrderField]

### queries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseQueryField]]


# QuickResponseSearchResultData

### contentType
- **Type**: <class 'str'>
- **Required**: Yes

### contents
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseContents'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.GroupingConfigurationOutput]

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


# RecommendationData

### document
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.Document'>
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


# RecommendationTrigger

### data
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.RecommendationTriggerData'>
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


# RecommendationTriggerData

### query
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QueryRecommendationTriggerData]


# RemoveKnowledgeBaseTemplateUriRequest

### knowledgeBaseId
- **Type**: <class 'str'>
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

### document
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.Document'>
- **Required**: Yes

### resultId
- **Type**: <class 'str'>
- **Required**: Yes

### relevanceScore
- **Type**: typing.Optional[float]


# SearchContentRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.SearchExpression'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.SearchExpression'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.PaginatorConfig]


# SearchContentResponse

### contentSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ContentSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchExpression

### filters
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.Filter]
- **Required**: Yes


# SearchQuickResponsesRequest

### knowledgeBaseId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseSearchExpression'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseSearchExpression'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.PaginatorConfig]


# SearchQuickResponsesResponse

### results
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseSearchResultData]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# SearchSessionsRequest

### assistantId
- **Type**: <class 'str'>
- **Required**: Yes

### searchExpression
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.SearchExpression'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.SearchExpression'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.PaginatorConfig]


# SearchSessionsResponse

### sessionSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.SessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


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

### description
- **Type**: typing.Optional[str]

### integrationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.SessionIntegrationConfiguration]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.AppIntegrationsConfiguration]


# SourceConfigurationOutput

### appIntegrations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.AppIntegrationsConfigurationOutput]


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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ExternalSourceConfiguration]

### metadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartImportJobResponse

### importJob
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ImportJobData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ContentData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.KnowledgeBaseData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseDataProvider]

### contentType
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### groupingConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.wisdom.wisdom_classes.GroupingConfiguration, aws_resource_validator.pydantic_models.wisdom.wisdom_classes.GroupingConfigurationOutput, NoneType]

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
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.QuickResponseData'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.wisdom.wisdom_classes.ResponseMetadata'>
- **Required**: Yes


