from datetime import datetime
from pydantic import BaseModel
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

class AmazonConnectGuideAssociationDataTypeDef(BaseModel):
    flowId: Optional[str] = None

class AppIntegrationsConfigurationExtraOutputTypeDef(BaseModel):
    appIntegrationArn: str
    objectFields: Optional[List[str]] = None

class AppIntegrationsConfigurationOutputTypeDef(BaseModel):
    appIntegrationArn: str
    objectFields: Optional[List[str]] = None

class AppIntegrationsConfigurationTypeDef(BaseModel):
    appIntegrationArn: str
    objectFields: Optional[Sequence[str]] = None

class AssistantAssociationInputDataTypeDef(BaseModel):
    knowledgeBaseId: Optional[str] = None

class KnowledgeBaseAssociationDataTypeDef(BaseModel):
    knowledgeBaseArn: Optional[str] = None
    knowledgeBaseId: Optional[str] = None

class AssistantCapabilityConfigurationTypeDef(BaseModel):
    type: Optional[AssistantCapabilityTypeType] = None

class AssistantIntegrationConfigurationTypeDef(BaseModel):
    topicIntegrationArn: Optional[str] = None

class ServerSideEncryptionConfigurationTypeDef(BaseModel):
    kmsKeyId: Optional[str] = None

class ConnectConfigurationTypeDef(BaseModel):
    instanceId: Optional[str] = None

class RankingDataTypeDef(BaseModel):
    relevanceLevel: Optional[RelevanceLevelType] = None
    relevanceScore: Optional[float] = None

class ContentDataTypeDef(BaseModel):
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

class GenerativeContentFeedbackDataTypeDef(BaseModel):
    relevance: RelevanceType

class ContentReferenceTypeDef(BaseModel):
    contentArn: Optional[str] = None
    contentId: Optional[str] = None
    knowledgeBaseArn: Optional[str] = None
    knowledgeBaseId: Optional[str] = None

class ContentSummaryTypeDef(BaseModel):
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

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class CreateContentRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str
    name: str
    uploadId: str
    clientToken: Optional[str] = None
    metadata: Optional[Mapping[str, str]] = None
    overrideLinkOutUri: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    title: Optional[str] = None

class RenderingConfigurationTypeDef(BaseModel):
    templateUri: Optional[str] = None

class GroupingConfigurationTypeDef(BaseModel):
    criteria: Optional[str] = None
    values: Optional[Sequence[str]] = None

class QuickResponseDataProviderTypeDef(BaseModel):
    content: Optional[str] = None

class GenerativeReferenceTypeDef(BaseModel):
    generationId: Optional[str] = None
    modelId: Optional[str] = None

class DeleteAssistantAssociationRequestRequestTypeDef(BaseModel):
    assistantAssociationId: str
    assistantId: str

class DeleteAssistantRequestRequestTypeDef(BaseModel):
    assistantId: str

class DeleteContentAssociationRequestRequestTypeDef(BaseModel):
    contentAssociationId: str
    contentId: str
    knowledgeBaseId: str

class DeleteContentRequestRequestTypeDef(BaseModel):
    contentId: str
    knowledgeBaseId: str

class DeleteImportJobRequestRequestTypeDef(BaseModel):
    importJobId: str
    knowledgeBaseId: str

class DeleteKnowledgeBaseRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str

class DeleteQuickResponseRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str
    quickResponseId: str

class HighlightTypeDef(BaseModel):
    beginOffsetInclusive: Optional[int] = None
    endOffsetExclusive: Optional[int] = None

class FilterTypeDef(BaseModel):
    field: Literal["NAME"]
    operator: Literal["EQUALS"]
    value: str

class GetAssistantAssociationRequestRequestTypeDef(BaseModel):
    assistantAssociationId: str
    assistantId: str

class GetAssistantRequestRequestTypeDef(BaseModel):
    assistantId: str

class GetContentAssociationRequestRequestTypeDef(BaseModel):
    contentAssociationId: str
    contentId: str
    knowledgeBaseId: str

class GetContentRequestRequestTypeDef(BaseModel):
    contentId: str
    knowledgeBaseId: str

class GetContentSummaryRequestRequestTypeDef(BaseModel):
    contentId: str
    knowledgeBaseId: str

class GetImportJobRequestRequestTypeDef(BaseModel):
    importJobId: str
    knowledgeBaseId: str

class GetKnowledgeBaseRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str

class GetQuickResponseRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str
    quickResponseId: str

class GetRecommendationsRequestRequestTypeDef(BaseModel):
    assistantId: str
    sessionId: str
    maxResults: Optional[int] = None
    waitTimeSeconds: Optional[int] = None

class GetSessionRequestRequestTypeDef(BaseModel):
    assistantId: str
    sessionId: str

class GroupingConfigurationExtraOutputTypeDef(BaseModel):
    criteria: Optional[str] = None
    values: Optional[List[str]] = None

class GroupingConfigurationOutputTypeDef(BaseModel):
    criteria: Optional[str] = None
    values: Optional[List[str]] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAssistantAssociationsRequestRequestTypeDef(BaseModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListAssistantsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListContentAssociationsRequestRequestTypeDef(BaseModel):
    contentId: str
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListContentsRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListImportJobsRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListKnowledgeBasesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListQuickResponsesRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class QuickResponseSummaryTypeDef(BaseModel):
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

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class NotifyRecommendationsReceivedErrorTypeDef(BaseModel):
    message: Optional[str] = None
    recommendationId: Optional[str] = None

class NotifyRecommendationsReceivedRequestRequestTypeDef(BaseModel):
    assistantId: str
    recommendationIds: Sequence[str]
    sessionId: str

class TagConditionTypeDef(BaseModel):
    key: str
    value: Optional[str] = None

class QueryConditionItemTypeDef(BaseModel):
    comparator: Literal["EQUALS"]
    field: Literal["RESULT_TYPE"]
    value: str

class QueryRecommendationTriggerDataTypeDef(BaseModel):
    text: Optional[str] = None

class QuickResponseContentProviderTypeDef(BaseModel):
    content: Optional[str] = None

class QuickResponseFilterFieldTypeDef(BaseModel):
    name: str
    operator: QuickResponseFilterOperatorType
    includeNoExistence: Optional[bool] = None
    values: Optional[Sequence[str]] = None

class QuickResponseOrderFieldTypeDef(BaseModel):
    name: str
    order: Optional[OrderType] = None

class QuickResponseQueryFieldTypeDef(BaseModel):
    name: str
    operator: QuickResponseQueryOperatorType
    values: Sequence[str]
    allowFuzziness: Optional[bool] = None
    priority: Optional[PriorityType] = None

class RemoveKnowledgeBaseTemplateUriRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str

class SessionSummaryTypeDef(BaseModel):
    assistantArn: str
    assistantId: str
    sessionArn: str
    sessionId: str

class SessionIntegrationConfigurationTypeDef(BaseModel):
    topicIntegrationArn: Optional[str] = None

class StartContentUploadRequestRequestTypeDef(BaseModel):
    contentType: str
    knowledgeBaseId: str
    presignedUrlTimeToLive: Optional[int] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateContentRequestRequestTypeDef(BaseModel):
    contentId: str
    knowledgeBaseId: str
    metadata: Optional[Mapping[str, str]] = None
    overrideLinkOutUri: Optional[str] = None
    removeOverrideLinkOutUri: Optional[bool] = None
    revisionId: Optional[str] = None
    title: Optional[str] = None
    uploadId: Optional[str] = None

class UpdateKnowledgeBaseTemplateUriRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str
    templateUri: str

class ContentAssociationContentsTypeDef(BaseModel):
    amazonConnectGuideAssociation: Optional[AmazonConnectGuideAssociationDataTypeDef] = None

class SourceConfigurationExtraOutputTypeDef(BaseModel):
    appIntegrations: Optional[AppIntegrationsConfigurationExtraOutputTypeDef] = None

class SourceConfigurationOutputTypeDef(BaseModel):
    appIntegrations: Optional[AppIntegrationsConfigurationOutputTypeDef] = None

class SourceConfigurationTypeDef(BaseModel):
    appIntegrations: Optional[AppIntegrationsConfigurationTypeDef] = None

class CreateAssistantAssociationRequestRequestTypeDef(BaseModel):
    assistantId: str
    association: AssistantAssociationInputDataTypeDef
    associationType: Literal["KNOWLEDGE_BASE"]
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class AssistantAssociationOutputDataTypeDef(BaseModel):
    knowledgeBaseAssociation: Optional[KnowledgeBaseAssociationDataTypeDef] = None

class AssistantDataTypeDef(BaseModel):
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

class AssistantSummaryTypeDef(BaseModel):
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

class CreateAssistantRequestRequestTypeDef(BaseModel):
    name: str
    type: Literal["AGENT"]
    clientToken: Optional[str] = None
    description: Optional[str] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class ConfigurationTypeDef(BaseModel):
    connectConfiguration: Optional[ConnectConfigurationTypeDef] = None

class GenerativeDataDetailsTypeDef(BaseModel):
    completion: str
    rankingData: RankingDataTypeDef
    references: List["DataSummaryTypeDef"]

class ContentFeedbackDataTypeDef(BaseModel):
    generativeContentFeedbackData: Optional[GenerativeContentFeedbackDataTypeDef] = None

class CreateContentResponseTypeDef(BaseModel):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContentResponseTypeDef(BaseModel):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContentSummaryResponseTypeDef(BaseModel):
    contentSummary: ContentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListContentsResponseTypeDef(BaseModel):
    contentSummaries: List[ContentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class SearchContentResponseTypeDef(BaseModel):
    contentSummaries: List[ContentSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartContentUploadResponseTypeDef(BaseModel):
    headersToInclude: Dict[str, str]
    uploadId: str
    url: str
    urlExpiry: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContentResponseTypeDef(BaseModel):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQuickResponseRequestRequestTypeDef(BaseModel):
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

class UpdateQuickResponseRequestRequestTypeDef(BaseModel):
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

class DataReferenceTypeDef(BaseModel):
    contentReference: Optional[ContentReferenceTypeDef] = None
    generativeReference: Optional[GenerativeReferenceTypeDef] = None

class DocumentTextTypeDef(BaseModel):
    highlights: Optional[List[HighlightTypeDef]] = None
    text: Optional[str] = None

class SearchExpressionTypeDef(BaseModel):
    filters: Sequence[FilterTypeDef]

class ListAssistantAssociationsRequestListAssistantAssociationsPaginateTypeDef(BaseModel):
    assistantId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAssistantsRequestListAssistantsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContentAssociationsRequestListContentAssociationsPaginateTypeDef(BaseModel):
    contentId: str
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContentsRequestListContentsPaginateTypeDef(BaseModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListImportJobsRequestListImportJobsPaginateTypeDef(BaseModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListKnowledgeBasesRequestListKnowledgeBasesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQuickResponsesRequestListQuickResponsesPaginateTypeDef(BaseModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQuickResponsesResponseTypeDef(BaseModel):
    nextToken: str
    quickResponseSummaries: List[QuickResponseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NotifyRecommendationsReceivedResponseTypeDef(BaseModel):
    errors: List[NotifyRecommendationsReceivedErrorTypeDef]
    recommendationIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class OrConditionOutputTypeDef(BaseModel):
    andConditions: Optional[List[TagConditionTypeDef]] = None
    tagCondition: Optional[TagConditionTypeDef] = None

class OrConditionTypeDef(BaseModel):
    andConditions: Optional[Sequence[TagConditionTypeDef]] = None
    tagCondition: Optional[TagConditionTypeDef] = None

class QueryConditionTypeDef(BaseModel):
    single: Optional[QueryConditionItemTypeDef] = None

class RecommendationTriggerDataTypeDef(BaseModel):
    query: Optional[QueryRecommendationTriggerDataTypeDef] = None

class QuickResponseContentsTypeDef(BaseModel):
    markdown: Optional[QuickResponseContentProviderTypeDef] = None
    plainText: Optional[QuickResponseContentProviderTypeDef] = None

class QuickResponseSearchExpressionTypeDef(BaseModel):
    filters: Optional[Sequence[QuickResponseFilterFieldTypeDef]] = None
    orderOnField: Optional[QuickResponseOrderFieldTypeDef] = None
    queries: Optional[Sequence[QuickResponseQueryFieldTypeDef]] = None

class SearchSessionsResponseTypeDef(BaseModel):
    nextToken: str
    sessionSummaries: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ContentAssociationDataTypeDef(BaseModel):
    associationData: ContentAssociationContentsTypeDef
    associationType: Literal["AMAZON_CONNECT_GUIDE"]
    contentArn: str
    contentAssociationArn: str
    contentAssociationId: str
    contentId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    tags: Optional[Dict[str, str]] = None

class ContentAssociationSummaryTypeDef(BaseModel):
    associationData: ContentAssociationContentsTypeDef
    associationType: Literal["AMAZON_CONNECT_GUIDE"]
    contentArn: str
    contentAssociationArn: str
    contentAssociationId: str
    contentId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    tags: Optional[Dict[str, str]] = None

class CreateContentAssociationRequestRequestTypeDef(BaseModel):
    association: ContentAssociationContentsTypeDef
    associationType: Literal["AMAZON_CONNECT_GUIDE"]
    contentId: str
    knowledgeBaseId: str
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class KnowledgeBaseDataTypeDef(BaseModel):
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

class KnowledgeBaseSummaryTypeDef(BaseModel):
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

class CreateKnowledgeBaseRequestRequestTypeDef(BaseModel):
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    renderingConfiguration: Optional[RenderingConfigurationTypeDef] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    sourceConfiguration: Optional[SourceConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class AssistantAssociationDataTypeDef(BaseModel):
    assistantArn: str
    assistantAssociationArn: str
    assistantAssociationId: str
    assistantId: str
    associationData: AssistantAssociationOutputDataTypeDef
    associationType: Literal["KNOWLEDGE_BASE"]
    tags: Optional[Dict[str, str]] = None

class AssistantAssociationSummaryTypeDef(BaseModel):
    assistantArn: str
    assistantAssociationArn: str
    assistantAssociationId: str
    assistantId: str
    associationData: AssistantAssociationOutputDataTypeDef
    associationType: Literal["KNOWLEDGE_BASE"]
    tags: Optional[Dict[str, str]] = None

class CreateAssistantResponseTypeDef(BaseModel):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssistantResponseTypeDef(BaseModel):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssistantsResponseTypeDef(BaseModel):
    assistantSummaries: List[AssistantSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExternalSourceConfigurationTypeDef(BaseModel):
    configuration: ConfigurationTypeDef
    source: Literal["AMAZON_CONNECT"]

class PutFeedbackRequestRequestTypeDef(BaseModel):
    assistantId: str
    contentFeedback: ContentFeedbackDataTypeDef
    targetId: str
    targetType: TargetTypeType

class PutFeedbackResponseTypeDef(BaseModel):
    assistantArn: str
    assistantId: str
    contentFeedback: ContentFeedbackDataTypeDef
    targetId: str
    targetType: TargetTypeType
    ResponseMetadata: ResponseMetadataTypeDef

class DataSummaryTypeDef(BaseModel):
    details: "DataDetailsTypeDef"
    reference: DataReferenceTypeDef

class DocumentTypeDef(BaseModel):
    contentReference: ContentReferenceTypeDef
    excerpt: Optional[DocumentTextTypeDef] = None
    title: Optional[DocumentTextTypeDef] = None

class TextDataTypeDef(BaseModel):
    excerpt: Optional[DocumentTextTypeDef] = None
    title: Optional[DocumentTextTypeDef] = None

class SearchContentRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str
    searchExpression: SearchExpressionTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchContentRequestSearchContentPaginateTypeDef(BaseModel):
    knowledgeBaseId: str
    searchExpression: SearchExpressionTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchSessionsRequestRequestTypeDef(BaseModel):
    assistantId: str
    searchExpression: SearchExpressionTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchSessionsRequestSearchSessionsPaginateTypeDef(BaseModel):
    assistantId: str
    searchExpression: SearchExpressionTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class TagFilterOutputTypeDef(BaseModel):
    andConditions: Optional[List[TagConditionTypeDef]] = None
    orConditions: Optional[List[OrConditionOutputTypeDef]] = None
    tagCondition: Optional[TagConditionTypeDef] = None

class TagFilterTypeDef(BaseModel):
    andConditions: Optional[Sequence[TagConditionTypeDef]] = None
    orConditions: Optional[Sequence[OrConditionTypeDef]] = None
    tagCondition: Optional[TagConditionTypeDef] = None

class QueryAssistantRequestQueryAssistantPaginateTypeDef(BaseModel):
    assistantId: str
    queryText: str
    queryCondition: Optional[Sequence[QueryConditionTypeDef]] = None
    sessionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class QueryAssistantRequestRequestTypeDef(BaseModel):
    assistantId: str
    queryText: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    queryCondition: Optional[Sequence[QueryConditionTypeDef]] = None
    sessionId: Optional[str] = None

class RecommendationTriggerTypeDef(BaseModel):
    data: RecommendationTriggerDataTypeDef
    id: str
    recommendationIds: List[str]
    source: RecommendationSourceTypeType
    type: RecommendationTriggerTypeType

class QuickResponseDataTypeDef(BaseModel):
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

class QuickResponseSearchResultDataTypeDef(BaseModel):
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

class SearchQuickResponsesRequestRequestTypeDef(BaseModel):
    knowledgeBaseId: str
    searchExpression: QuickResponseSearchExpressionTypeDef
    attributes: Optional[Mapping[str, str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class SearchQuickResponsesRequestSearchQuickResponsesPaginateTypeDef(BaseModel):
    knowledgeBaseId: str
    searchExpression: QuickResponseSearchExpressionTypeDef
    attributes: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class CreateContentAssociationResponseTypeDef(BaseModel):
    contentAssociation: ContentAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetContentAssociationResponseTypeDef(BaseModel):
    contentAssociation: ContentAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListContentAssociationsResponseTypeDef(BaseModel):
    contentAssociationSummaries: List[ContentAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateKnowledgeBaseResponseTypeDef(BaseModel):
    knowledgeBase: KnowledgeBaseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetKnowledgeBaseResponseTypeDef(BaseModel):
    knowledgeBase: KnowledgeBaseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateKnowledgeBaseTemplateUriResponseTypeDef(BaseModel):
    knowledgeBase: KnowledgeBaseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListKnowledgeBasesResponseTypeDef(BaseModel):
    knowledgeBaseSummaries: List[KnowledgeBaseSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAssistantAssociationResponseTypeDef(BaseModel):
    assistantAssociation: AssistantAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAssistantAssociationResponseTypeDef(BaseModel):
    assistantAssociation: AssistantAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAssistantAssociationsResponseTypeDef(BaseModel):
    assistantAssociationSummaries: List[AssistantAssociationSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportJobDataTypeDef(BaseModel):
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

class ImportJobSummaryTypeDef(BaseModel):
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

class StartImportJobRequestRequestTypeDef(BaseModel):
    importJobType: Literal["QUICK_RESPONSES"]
    knowledgeBaseId: str
    uploadId: str
    clientToken: Optional[str] = None
    externalSourceConfiguration: Optional[ExternalSourceConfigurationTypeDef] = None
    metadata: Optional[Mapping[str, str]] = None

class RecommendationDataTypeDef(BaseModel):
    recommendationId: str
    data: Optional["DataSummaryTypeDef"] = None
    document: Optional[DocumentTypeDef] = None
    relevanceLevel: Optional[RelevanceLevelType] = None
    relevanceScore: Optional[float] = None
    type: Optional[RecommendationTypeType] = None

class ResultDataTypeDef(BaseModel):
    resultId: str
    data: Optional["DataSummaryTypeDef"] = None
    document: Optional[DocumentTypeDef] = None
    relevanceScore: Optional[float] = None
    type: Optional[QueryResultTypeType] = None

class ContentDataDetailsTypeDef(BaseModel):
    rankingData: RankingDataTypeDef
    textData: TextDataTypeDef

class SourceContentDataDetailsTypeDef(BaseModel):
    id: str
    rankingData: RankingDataTypeDef
    textData: TextDataTypeDef
    type: Literal["KNOWLEDGE_CONTENT"]

class SessionDataTypeDef(BaseModel):
    name: str
    sessionArn: str
    sessionId: str
    description: Optional[str] = None
    integrationConfiguration: Optional[SessionIntegrationConfigurationTypeDef] = None
    tagFilter: Optional[TagFilterOutputTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class CreateSessionRequestRequestTypeDef(BaseModel):
    assistantId: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tagFilter: Optional[TagFilterTypeDef] = None
    tags: Optional[Mapping[str, str]] = None

class UpdateSessionRequestRequestTypeDef(BaseModel):
    assistantId: str
    sessionId: str
    description: Optional[str] = None
    tagFilter: Optional[TagFilterTypeDef] = None

class CreateQuickResponseResponseTypeDef(BaseModel):
    quickResponse: QuickResponseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetQuickResponseResponseTypeDef(BaseModel):
    quickResponse: QuickResponseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateQuickResponseResponseTypeDef(BaseModel):
    quickResponse: QuickResponseDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchQuickResponsesResponseTypeDef(BaseModel):
    nextToken: str
    results: List[QuickResponseSearchResultDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetImportJobResponseTypeDef(BaseModel):
    importJob: ImportJobDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartImportJobResponseTypeDef(BaseModel):
    importJob: ImportJobDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListImportJobsResponseTypeDef(BaseModel):
    importJobSummaries: List[ImportJobSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecommendationsResponseTypeDef(BaseModel):
    recommendations: List[RecommendationDataTypeDef]
    triggers: List[RecommendationTriggerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class QueryAssistantResponseTypeDef(BaseModel):
    nextToken: str
    results: List[ResultDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DataDetailsTypeDef(BaseModel):
    contentData: Optional[ContentDataDetailsTypeDef] = None
    generativeData: Optional["GenerativeDataDetailsTypeDef"] = None
    sourceContentData: Optional[SourceContentDataDetailsTypeDef] = None

class CreateSessionResponseTypeDef(BaseModel):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSessionResponseTypeDef(BaseModel):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSessionResponseTypeDef(BaseModel):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

