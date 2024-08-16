from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.qconnect_constants import *

class AmazonConnectGuideAssociationDataTypeDef(BaseValidatorModel):
    flowId: Optional[str] = None

class AppIntegrationsConfigurationExtraOutputTypeDef(BaseValidatorModel):
    appIntegrationArn: str
    objectFields: Optional[List[str]] = None

class AppIntegrationsConfigurationOutputTypeDef(BaseValidatorModel):
    appIntegrationArn: str
    objectFields: Optional[List[str]] = None

class AppIntegrationsConfigurationTypeDef(BaseValidatorModel):
    appIntegrationArn: str
    objectFields: Optional[Sequence[str]] = None

class AssistantAssociationInputDataTypeDef(BaseValidatorModel):
    knowledgeBaseId: Optional[str] = None

class KnowledgeBaseAssociationDataTypeDef(BaseValidatorModel):
    knowledgeBaseArn: Optional[str] = None
    knowledgeBaseId: Optional[str] = None

class AssistantCapabilityConfigurationTypeDef(BaseValidatorModel):
    type: Optional[AssistantCapabilityTypeType] = None

class AssistantIntegrationConfigurationTypeDef(BaseValidatorModel):
    topicIntegrationArn: Optional[str] = None

class ServerSideEncryptionConfigurationTypeDef(BaseValidatorModel):
    kmsKeyId: Optional[str] = None

class ConnectConfigurationTypeDef(BaseValidatorModel):
    instanceId: Optional[str] = None

class RankingDataTypeDef(BaseValidatorModel):
    relevanceLevel: Optional[RelevanceLevelType] = None
    relevanceScore: Optional[float] = None

class ContentDataTypeDef(BaseValidatorModel):
    contentArn: str
    contentId: str
    contentType: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    metadata: Dict[str, str]
    name: str
    revisionId: str
    status: ContentStatusType
    title: str
    url: str
    urlExpiry: datetime
    linkOutUri: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class GenerativeContentFeedbackDataTypeDef(BaseValidatorModel):
    relevance: RelevanceType

class ContentReferenceTypeDef(BaseValidatorModel):
    contentArn: Optional[str] = None
    contentId: Optional[str] = None
    knowledgeBaseArn: Optional[str] = None
    knowledgeBaseId: Optional[str] = None

class ContentSummaryTypeDef(BaseValidatorModel):
    contentArn: str
    contentId: str
    contentType: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    metadata: Dict[str, str]
    name: str
    revisionId: str
    status: ContentStatusType
    title: str
    tags: Optional[Dict[str, str]] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateContentRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    name: str
    uploadId: str
    clientToken: Optional[str] = None
    metadata: Optional[Mapping[str, str]] = None
    overrideLinkOutUri: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    title: Optional[str] = None

class RenderingConfigurationTypeDef(BaseValidatorModel):
    templateUri: Optional[str] = None

class GroupingConfigurationTypeDef(BaseValidatorModel):
    criteria: Optional[str] = None
    values: Optional[Sequence[str]] = None

class QuickResponseDataProviderTypeDef(BaseValidatorModel):
    content: Optional[str] = None

class GenerativeReferenceTypeDef(BaseValidatorModel):
    generationId: Optional[str] = None
    modelId: Optional[str] = None

class DeleteAssistantAssociationRequestRequestTypeDef(BaseValidatorModel):
    assistantAssociationId: str
    assistantId: str

class DeleteAssistantRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str

class DeleteContentAssociationRequestRequestTypeDef(BaseValidatorModel):
    contentAssociationId: str
    contentId: str
    knowledgeBaseId: str

class DeleteContentRequestRequestTypeDef(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str

class DeleteImportJobRequestRequestTypeDef(BaseValidatorModel):
    importJobId: str
    knowledgeBaseId: str

class DeleteKnowledgeBaseRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str

class DeleteQuickResponseRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    quickResponseId: str

class HighlightTypeDef(BaseValidatorModel):
    beginOffsetInclusive: Optional[int] = None
    endOffsetExclusive: Optional[int] = None

class FilterTypeDef(BaseValidatorModel):
    field: Literal["NAME"]
    operator: Literal["EQUALS"]
    value: str

class GetAssistantAssociationRequestRequestTypeDef(BaseValidatorModel):
    assistantAssociationId: str
    assistantId: str

class GetAssistantRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str

class GetContentAssociationRequestRequestTypeDef(BaseValidatorModel):
    contentAssociationId: str
    contentId: str
    knowledgeBaseId: str

class GetContentRequestRequestTypeDef(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str

class GetContentSummaryRequestRequestTypeDef(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str

class GetImportJobRequestRequestTypeDef(BaseValidatorModel):
    importJobId: str
    knowledgeBaseId: str

class GetKnowledgeBaseRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str

class GetQuickResponseRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    quickResponseId: str

class GetRecommendationsRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str
    sessionId: str
    maxResults: Optional[int] = None
    waitTimeSeconds: Optional[int] = None

class GetSessionRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str
    sessionId: str

class GroupingConfigurationExtraOutputTypeDef(BaseValidatorModel):
    criteria: Optional[str] = None
    values: Optional[List[str]] = None

class GroupingConfigurationOutputTypeDef(BaseValidatorModel):
    criteria: Optional[str] = None
    values: Optional[List[str]] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAssistantAssociationsRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAssistantsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListContentAssociationsRequestRequestTypeDef(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListContentsRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImportJobsRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListKnowledgeBasesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListQuickResponsesRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class QuickResponseSummaryTypeDef(BaseValidatorModel):
    contentType: str
    createdTime: datetime
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedTime: datetime
    name: str
    quickResponseArn: str
    quickResponseId: str
    status: QuickResponseStatusType
    channels: Optional[List[str]] = None
    description: Optional[str] = None
    isActive: Optional[bool] = None
    lastModifiedBy: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class NotifyRecommendationsReceivedErrorTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    recommendationId: Optional[str] = None

class NotifyRecommendationsReceivedRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str
    recommendationIds: Sequence[str]
    sessionId: str

class TagConditionTypeDef(BaseValidatorModel):
    key: str
    value: Optional[str] = None

class QueryConditionItemTypeDef(BaseValidatorModel):
    comparator: Literal["EQUALS"]
    field: Literal["RESULT_TYPE"]
    value: str

class QueryRecommendationTriggerDataTypeDef(BaseValidatorModel):
    text: Optional[str] = None

class QuickResponseContentProviderTypeDef(BaseValidatorModel):
    content: Optional[str] = None

class QuickResponseFilterFieldTypeDef(BaseValidatorModel):
    name: str
    operator: QuickResponseFilterOperatorType
    includeNoExistence: Optional[bool] = None
    values: Optional[Sequence[str]] = None

class QuickResponseOrderFieldTypeDef(BaseValidatorModel):
    name: str
    order: Optional[OrderType] = None

class QuickResponseQueryFieldTypeDef(BaseValidatorModel):
    name: str
    operator: QuickResponseQueryOperatorType
    values: Sequence[str]
    allowFuzziness: Optional[bool] = None
    priority: Optional[PriorityType] = None

class RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str

class SessionSummaryTypeDef(BaseValidatorModel):
    assistantArn: str
    assistantId: str
    sessionArn: str
    sessionId: str

class SessionIntegrationConfigurationTypeDef(BaseValidatorModel):
    topicIntegrationArn: Optional[str] = None

class StartContentUploadRequestRequestTypeDef(BaseValidatorModel):
    contentType: str
    knowledgeBaseId: str
    presignedUrlTimeToLive: Optional[int] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateContentRequestRequestTypeDef(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str
    metadata: Optional[Mapping[str, str]] = None
    overrideLinkOutUri: Optional[str] = None
    removeOverrideLinkOutUri: Optional[bool] = None
    revisionId: Optional[str] = None
    title: Optional[str] = None
    uploadId: Optional[str] = None

class UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    templateUri: str

class ContentAssociationContentsTypeDef(BaseValidatorModel):
    amazonConnectGuideAssociation: Optional[AmazonConnectGuideAssociationDataTypeDef] = None

class SourceConfigurationExtraOutputTypeDef(BaseValidatorModel):
    appIntegrations: Optional[AppIntegrationsConfigurationExtraOutputTypeDef] = None

class SourceConfigurationOutputTypeDef(BaseValidatorModel):
    appIntegrations: Optional[AppIntegrationsConfigurationOutputTypeDef] = None

class SourceConfigurationTypeDef(BaseValidatorModel):
    appIntegrations: Optional[AppIntegrationsConfigurationTypeDef] = None

class CreateAssistantAssociationRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str
    association: AssistantAssociationInputDataTypeDef
    associationType: Literal["KNOWLEDGE_BASE"]
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class AssistantAssociationOutputDataTypeDef(BaseValidatorModel):
    knowledgeBaseAssociation: Optional[KnowledgeBaseAssociationDataTypeDef] = None

class AssistantDataTypeDef(BaseValidatorModel):
    assistantArn: str
    assistantId: str
    name: str
    status: AssistantStatusType
    type: Literal["AGENT"]
    capabilityConfiguration: Optional[AssistantCapabilityConfigurationTypeDef] = None
    description: Optional[str] = None
    integrationConfiguration: Optional[AssistantIntegrationConfigurationTypeDef] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class AssistantSummaryTypeDef(BaseValidatorModel):
    assistantArn: str
    assistantId: str
    name: str
    status: AssistantStatusType
    type: Literal["AGENT"]
    capabilityConfiguration: Optional[AssistantCapabilityConfigurationTypeDef] = None
    description: Optional[str] = None
    integrationConfiguration: Optional[AssistantIntegrationConfigurationTypeDef] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class CreateAssistantRequestRequestTypeDef(BaseValidatorModel):
    name: str
    type: Literal["AGENT"]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class ConfigurationTypeDef(BaseValidatorModel):
    connectConfiguration: Optional[ConnectConfigurationTypeDef] = None

class GenerativeDataDetailsTypeDef(BaseValidatorModel):
    completion: str
    rankingData: RankingDataTypeDef
    references: List["DataSummaryTypeDef"]

class ContentFeedbackDataTypeDef(BaseValidatorModel):
    generativeContentFeedbackData: Optional[GenerativeContentFeedbackDataTypeDef] = None

class CreateContentResponseTypeDef(BaseValidatorModel):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContentResponseTypeDef(BaseValidatorModel):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContentSummaryResponseTypeDef(BaseValidatorModel):
    contentSummary: ContentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListContentsResponseTypeDef(BaseValidatorModel):
    contentSummaries: List[ContentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchContentResponseTypeDef(BaseValidatorModel):
    contentSummaries: List[ContentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartContentUploadResponseTypeDef(BaseValidatorModel):
    headersToInclude: Dict[str, str]
    uploadId: str
    url: str
    urlExpiry: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContentResponseTypeDef(BaseValidatorModel):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQuickResponseRequestRequestTypeDef(BaseValidatorModel):
    content: QuickResponseDataProviderTypeDef
    knowledgeBaseId: str
    name: str
    channels: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None
    contentType: Optional[str] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationTypeDef] = None
    isActive: Optional[bool] = None
    language: Optional[str] = None
    shortcutKey: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateQuickResponseRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    quickResponseId: str
    channels: Optional[Sequence[str]] = None
    content: Optional[QuickResponseDataProviderTypeDef] = None
    contentType: Optional[str] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationTypeDef] = None
    isActive: Optional[bool] = None
    language: Optional[str] = None
    name: Optional[str] = None
    removeDescription: Optional[bool] = None
    removeGroupingConfiguration: Optional[bool] = None
    removeShortcutKey: Optional[bool] = None
    shortcutKey: Optional[str] = None

class DataReferenceTypeDef(BaseValidatorModel):
    contentReference: Optional[ContentReferenceTypeDef] = None
    generativeReference: Optional[GenerativeReferenceTypeDef] = None

class DocumentTextTypeDef(BaseValidatorModel):
    highlights: Optional[List[HighlightTypeDef]] = None
    text: Optional[str] = None

class SearchExpressionTypeDef(BaseValidatorModel):
    filters: Sequence[FilterTypeDef]

class ListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef(BaseValidatorModel):
    assistantId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssistantsRequestListAssistantsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContentAssociationsRequestListContentAssociationsPaginateTypeDef(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContentsRequestListContentsPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportJobsRequestListImportJobsPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQuickResponsesRequestListQuickResponsesPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQuickResponsesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    quickResponseSummaries: List[QuickResponseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NotifyRecommendationsReceivedResponseTypeDef(BaseValidatorModel):
    errors: List[NotifyRecommendationsReceivedErrorTypeDef]
    recommendationIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class OrConditionOutputTypeDef(BaseValidatorModel):
    andConditions: Optional[List[TagConditionTypeDef]] = None
    tagCondition: Optional[TagConditionTypeDef] = None

class OrConditionTypeDef(BaseValidatorModel):
    andConditions: Optional[Sequence[TagConditionTypeDef]] = None
    tagCondition: Optional[TagConditionTypeDef] = None

class QueryConditionTypeDef(BaseValidatorModel):
    single: Optional[QueryConditionItemTypeDef] = None

class RecommendationTriggerDataTypeDef(BaseValidatorModel):
    query: Optional[QueryRecommendationTriggerDataTypeDef] = None

class QuickResponseContentsTypeDef(BaseValidatorModel):
    markdown: Optional[QuickResponseContentProviderTypeDef] = None
    plainText: Optional[QuickResponseContentProviderTypeDef] = None

class QuickResponseSearchExpressionTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[QuickResponseFilterFieldTypeDef]] = None
    orderOnField: Optional[QuickResponseOrderFieldTypeDef] = None
    queries: Optional[Sequence[QuickResponseQueryFieldTypeDef]] = None

class SearchSessionsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    sessionSummaries: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ContentAssociationDataTypeDef(BaseValidatorModel):
    associationData: ContentAssociationContentsTypeDef
    associationType: Literal["AMAZON_CONNECT_GUIDE"]
    contentArn: str
    contentAssociationArn: str
    contentAssociationId: str
    contentId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    tags: Optional[Dict[str, str]] = None

class ContentAssociationSummaryTypeDef(BaseValidatorModel):
    associationData: ContentAssociationContentsTypeDef
    associationType: Literal["AMAZON_CONNECT_GUIDE"]
    contentArn: str
    contentAssociationArn: str
    contentAssociationId: str
    contentId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    tags: Optional[Dict[str, str]] = None

class CreateContentAssociationRequestRequestTypeDef(BaseValidatorModel):
    association: ContentAssociationContentsTypeDef
    associationType: Literal["AMAZON_CONNECT_GUIDE"]
    contentId: str
    knowledgeBaseId: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class KnowledgeBaseDataTypeDef(BaseValidatorModel):
    knowledgeBaseArn: str
    knowledgeBaseId: str
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    status: KnowledgeBaseStatusType
    description: Optional[str] = None
    lastContentModificationTime: Optional[datetime] = None
    renderingConfiguration: Optional[RenderingConfigurationTypeDef] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    sourceConfiguration: Optional[SourceConfigurationOutputTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class KnowledgeBaseSummaryTypeDef(BaseValidatorModel):
    knowledgeBaseArn: str
    knowledgeBaseId: str
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    status: KnowledgeBaseStatusType
    description: Optional[str] = None
    renderingConfiguration: Optional[RenderingConfigurationTypeDef] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    sourceConfiguration: Optional[SourceConfigurationOutputTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class CreateKnowledgeBaseRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    renderingConfiguration: Optional[RenderingConfigurationTypeDef] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    sourceConfiguration: Optional[SourceConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class AssistantAssociationDataTypeDef(BaseValidatorModel):
    assistantArn: str
    assistantAssociationArn: str
    assistantAssociationId: str
    assistantId: str
    associationData: AssistantAssociationOutputDataTypeDef
    associationType: Literal["KNOWLEDGE_BASE"]
    tags: Optional[Dict[str, str]] = None

class AssistantAssociationSummaryTypeDef(BaseValidatorModel):
    assistantArn: str
    assistantAssociationArn: str
    assistantAssociationId: str
    assistantId: str
    associationData: AssistantAssociationOutputDataTypeDef
    associationType: Literal["KNOWLEDGE_BASE"]
    tags: Optional[Dict[str, str]] = None

class CreateAssistantResponseTypeDef(BaseValidatorModel):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssistantResponseTypeDef(BaseValidatorModel):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssistantsResponseTypeDef(BaseValidatorModel):
    assistantSummaries: List[AssistantSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExternalSourceConfigurationTypeDef(BaseValidatorModel):
    configuration: ConfigurationTypeDef
    source: Literal["AMAZON_CONNECT"]

class PutFeedbackRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str
    contentFeedback: ContentFeedbackDataTypeDef
    targetId: str
    targetType: TargetTypeType

class PutFeedbackResponseTypeDef(BaseValidatorModel):
    assistantArn: str
    assistantId: str
    contentFeedback: ContentFeedbackDataTypeDef
    targetId: str
    targetType: TargetTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DataSummaryTypeDef(BaseValidatorModel):
    details: "DataDetailsTypeDef"
    reference: DataReferenceTypeDef

class DocumentTypeDef(BaseValidatorModel):
    contentReference: ContentReferenceTypeDef
    excerpt: Optional[DocumentTextTypeDef] = None
    title: Optional[DocumentTextTypeDef] = None

class TextDataTypeDef(BaseValidatorModel):
    excerpt: Optional[DocumentTextTypeDef] = None
    title: Optional[DocumentTextTypeDef] = None

class SearchContentRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: SearchExpressionTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchContentRequestSearchContentPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: SearchExpressionTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchSessionsRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str
    searchExpression: SearchExpressionTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchSessionsRequestSearchSessionsPaginateTypeDef(BaseValidatorModel):
    assistantId: str
    searchExpression: SearchExpressionTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class TagFilterOutputTypeDef(BaseValidatorModel):
    andConditions: Optional[List[TagConditionTypeDef]] = None
    orConditions: Optional[List[OrConditionOutputTypeDef]] = None
    tagCondition: Optional[TagConditionTypeDef] = None

class TagFilterTypeDef(BaseValidatorModel):
    andConditions: Optional[Sequence[TagConditionTypeDef]] = None
    orConditions: Optional[Sequence[OrConditionTypeDef]] = None
    tagCondition: Optional[TagConditionTypeDef] = None

class QueryAssistantRequestQueryAssistantPaginateTypeDef(BaseValidatorModel):
    assistantId: str
    queryText: str
    queryCondition: Optional[Sequence[QueryConditionTypeDef]] = None
    sessionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class QueryAssistantRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str
    queryText: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    queryCondition: Optional[Sequence[QueryConditionTypeDef]] = None
    sessionId: Optional[str] = None

class RecommendationTriggerTypeDef(BaseValidatorModel):
    data: RecommendationTriggerDataTypeDef
    id: str
    recommendationIds: List[str]
    source: RecommendationSourceTypeType
    type: RecommendationTriggerTypeType

class QuickResponseDataTypeDef(BaseValidatorModel):
    contentType: str
    createdTime: datetime
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedTime: datetime
    name: str
    quickResponseArn: str
    quickResponseId: str
    status: QuickResponseStatusType
    channels: Optional[List[str]] = None
    contents: Optional[QuickResponseContentsTypeDef] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationOutputTypeDef] = None
    isActive: Optional[bool] = None
    language: Optional[str] = None
    lastModifiedBy: Optional[str] = None
    shortcutKey: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class QuickResponseSearchResultDataTypeDef(BaseValidatorModel):
    contentType: str
    contents: QuickResponseContentsTypeDef
    createdTime: datetime
    isActive: bool
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedTime: datetime
    name: str
    quickResponseArn: str
    quickResponseId: str
    status: QuickResponseStatusType
    attributesInterpolated: Optional[List[str]] = None
    attributesNotInterpolated: Optional[List[str]] = None
    channels: Optional[List[str]] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationOutputTypeDef] = None
    language: Optional[str] = None
    lastModifiedBy: Optional[str] = None
    shortcutKey: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class SearchQuickResponsesRequestRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: QuickResponseSearchExpressionTypeDef
    attributes: Optional[Mapping[str, str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchQuickResponsesRequestSearchQuickResponsesPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: QuickResponseSearchExpressionTypeDef
    attributes: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class CreateContentAssociationResponseTypeDef(BaseValidatorModel):
    contentAssociation: ContentAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContentAssociationResponseTypeDef(BaseValidatorModel):
    contentAssociation: ContentAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListContentAssociationsResponseTypeDef(BaseValidatorModel):
    contentAssociationSummaries: List[ContentAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    knowledgeBase: KnowledgeBaseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKnowledgeBaseResponseTypeDef(BaseValidatorModel):
    knowledgeBase: KnowledgeBaseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKnowledgeBaseTemplateUriResponseTypeDef(BaseValidatorModel):
    knowledgeBase: KnowledgeBaseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListKnowledgeBasesResponseTypeDef(BaseValidatorModel):
    knowledgeBaseSummaries: List[KnowledgeBaseSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssistantAssociationResponseTypeDef(BaseValidatorModel):
    assistantAssociation: AssistantAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssistantAssociationResponseTypeDef(BaseValidatorModel):
    assistantAssociation: AssistantAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssistantAssociationsResponseTypeDef(BaseValidatorModel):
    assistantAssociationSummaries: List[AssistantAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportJobDataTypeDef(BaseValidatorModel):
    createdTime: datetime
    importJobId: str
    importJobType: Literal["QUICK_RESPONSES"]
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedTime: datetime
    status: ImportJobStatusType
    uploadId: str
    url: str
    urlExpiry: datetime
    externalSourceConfiguration: Optional[ExternalSourceConfigurationTypeDef] = None
    failedRecordReport: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None

class ImportJobSummaryTypeDef(BaseValidatorModel):
    createdTime: datetime
    importJobId: str
    importJobType: Literal["QUICK_RESPONSES"]
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedTime: datetime
    status: ImportJobStatusType
    uploadId: str
    externalSourceConfiguration: Optional[ExternalSourceConfigurationTypeDef] = None
    metadata: Optional[Dict[str, str]] = None

class StartImportJobRequestRequestTypeDef(BaseValidatorModel):
    importJobType: Literal["QUICK_RESPONSES"]
    knowledgeBaseId: str
    uploadId: str
    clientToken: Optional[str] = None
    externalSourceConfiguration: Optional[ExternalSourceConfigurationTypeDef] = None
    metadata: Optional[Mapping[str, str]] = None

class RecommendationDataTypeDef(BaseValidatorModel):
    recommendationId: str
    data: Optional["DataSummaryTypeDef"] = None
    document: Optional[DocumentTypeDef] = None
    relevanceLevel: Optional[RelevanceLevelType] = None
    relevanceScore: Optional[float] = None
    type: Optional[RecommendationTypeType] = None

class ResultDataTypeDef(BaseValidatorModel):
    resultId: str
    data: Optional["DataSummaryTypeDef"] = None
    document: Optional[DocumentTypeDef] = None
    relevanceScore: Optional[float] = None
    type: Optional[QueryResultTypeType] = None

class ContentDataDetailsTypeDef(BaseValidatorModel):
    rankingData: RankingDataTypeDef
    textData: TextDataTypeDef

class SourceContentDataDetailsTypeDef(BaseValidatorModel):
    id: str
    rankingData: RankingDataTypeDef
    textData: TextDataTypeDef
    type: Literal["KNOWLEDGE_CONTENT"]

class SessionDataTypeDef(BaseValidatorModel):
    name: str
    sessionArn: str
    sessionId: str
    description: Optional[str] = None
    integrationConfiguration: Optional[SessionIntegrationConfigurationTypeDef] = None
    tagFilter: Optional[TagFilterOutputTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class CreateSessionRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tagFilter: Optional[TagFilterTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateSessionRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str
    sessionId: str
    description: Optional[str] = None
    tagFilter: Optional[TagFilterTypeDef] = None

class CreateQuickResponseResponseTypeDef(BaseValidatorModel):
    quickResponse: QuickResponseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetQuickResponseResponseTypeDef(BaseValidatorModel):
    quickResponse: QuickResponseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQuickResponseResponseTypeDef(BaseValidatorModel):
    quickResponse: QuickResponseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchQuickResponsesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    results: List[QuickResponseSearchResultDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetImportJobResponseTypeDef(BaseValidatorModel):
    importJob: ImportJobDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportJobResponseTypeDef(BaseValidatorModel):
    importJob: ImportJobDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListImportJobsResponseTypeDef(BaseValidatorModel):
    importJobSummaries: List[ImportJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationsResponseTypeDef(BaseValidatorModel):
    recommendations: List[RecommendationDataTypeDef]
    triggers: List[RecommendationTriggerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class QueryAssistantResponseTypeDef(BaseValidatorModel):
    nextToken: str
    results: List[ResultDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DataDetailsTypeDef(BaseValidatorModel):
    contentData: Optional[ContentDataDetailsTypeDef] = None
    generativeData: Optional["GenerativeDataDetailsTypeDef"] = None
    sourceContentData: Optional[SourceContentDataDetailsTypeDef] = None

class CreateSessionResponseTypeDef(BaseValidatorModel):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSessionResponseTypeDef(BaseValidatorModel):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSessionResponseTypeDef(BaseValidatorModel):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

