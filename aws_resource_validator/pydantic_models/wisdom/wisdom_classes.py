from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.wisdom.wisdom_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AppIntegrationsConfigurationOutput(BaseValidatorModel):
    appIntegrationArn: str
    objectFields: Optional[List[str]] = None


class AppIntegrationsConfiguration(BaseValidatorModel):
    appIntegrationArn: str
    objectFields: Optional[List[str]] = None


class AssistantAssociationInputData(BaseValidatorModel):
    knowledgeBaseId: Optional[str] = None


class KnowledgeBaseAssociationData(BaseValidatorModel):
    knowledgeBaseArn: Optional[str] = None
    knowledgeBaseId: Optional[str] = None


class AssistantIntegrationConfiguration(BaseValidatorModel):
    topicIntegrationArn: Optional[str] = None


class ServerSideEncryptionConfiguration(BaseValidatorModel):
    kmsKeyId: Optional[str] = None


class ConnectConfiguration(BaseValidatorModel):
    instanceId: Optional[str] = None


class ContentData(BaseValidatorModel):
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


class ContentReference(BaseValidatorModel):
    contentArn: Optional[str] = None
    contentId: Optional[str] = None
    knowledgeBaseArn: Optional[str] = None
    knowledgeBaseId: Optional[str] = None


class ContentSummary(BaseValidatorModel):
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


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateContentRequest(BaseValidatorModel):
    knowledgeBaseId: str
    name: str
    uploadId: str
    clientToken: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
    overrideLinkOutUri: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    title: Optional[str] = None


class RenderingConfiguration(BaseValidatorModel):
    templateUri: Optional[str] = None


class QuickResponseDataProvider(BaseValidatorModel):
    content: Optional[str] = None


class CreateSessionRequest(BaseValidatorModel):
    assistantId: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class DeleteAssistantAssociationRequest(BaseValidatorModel):
    assistantAssociationId: str
    assistantId: str


class DeleteAssistantRequest(BaseValidatorModel):
    assistantId: str


class DeleteContentRequest(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str


class DeleteImportJobRequest(BaseValidatorModel):
    importJobId: str
    knowledgeBaseId: str


class DeleteKnowledgeBaseRequest(BaseValidatorModel):
    knowledgeBaseId: str


class DeleteQuickResponseRequest(BaseValidatorModel):
    knowledgeBaseId: str
    quickResponseId: str


class Highlight(BaseValidatorModel):
    beginOffsetInclusive: Optional[int] = None
    endOffsetExclusive: Optional[int] = None


class Filter(BaseValidatorModel):
    field: Literal['NAME']
    operator: Literal['EQUALS']
    value: str


class GetAssistantAssociationRequest(BaseValidatorModel):
    assistantAssociationId: str
    assistantId: str


class GetAssistantRequest(BaseValidatorModel):
    assistantId: str


class GetContentRequest(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str


class GetContentSummaryRequest(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str


class GetImportJobRequest(BaseValidatorModel):
    importJobId: str
    knowledgeBaseId: str


class GetKnowledgeBaseRequest(BaseValidatorModel):
    knowledgeBaseId: str


class GetQuickResponseRequest(BaseValidatorModel):
    knowledgeBaseId: str
    quickResponseId: str


class GetRecommendationsRequest(BaseValidatorModel):
    assistantId: str
    sessionId: str
    maxResults: Optional[int] = None
    waitTimeSeconds: Optional[int] = None


class GetSessionRequest(BaseValidatorModel):
    assistantId: str
    sessionId: str


class GroupingConfigurationOutput(BaseValidatorModel):
    criteria: Optional[str] = None
    values: Optional[List[str]] = None


class GroupingConfiguration(BaseValidatorModel):
    criteria: Optional[str] = None
    values: Optional[List[str]] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAssistantAssociationsRequest(BaseValidatorModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAssistantsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListContentsRequest(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImportJobsRequest(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListKnowledgeBasesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListQuickResponsesRequest(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class QuickResponseSummary(BaseValidatorModel):
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


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class NotifyRecommendationsReceivedError(BaseValidatorModel):
    message: Optional[str] = None
    recommendationId: Optional[str] = None


class NotifyRecommendationsReceivedRequest(BaseValidatorModel):
    assistantId: str
    recommendationIds: List[str]
    sessionId: str


class QueryAssistantRequest(BaseValidatorModel):
    assistantId: str
    queryText: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class QueryRecommendationTriggerData(BaseValidatorModel):
    text: Optional[str] = None


class QuickResponseContentProvider(BaseValidatorModel):
    content: Optional[str] = None


class QuickResponseFilterField(BaseValidatorModel):
    name: str
    operator: QuickResponseFilterOperatorType
    includeNoExistence: Optional[bool] = None
    values: Optional[List[str]] = None


class QuickResponseOrderField(BaseValidatorModel):
    name: str
    order: Optional[OrderType] = None


class QuickResponseQueryField(BaseValidatorModel):
    name: str
    operator: QuickResponseQueryOperatorType
    values: List[str]
    allowFuzziness: Optional[bool] = None
    priority: Optional[PriorityType] = None


class RemoveKnowledgeBaseTemplateUriRequest(BaseValidatorModel):
    knowledgeBaseId: str


class SessionSummary(BaseValidatorModel):
    assistantArn: str
    assistantId: str
    sessionArn: str
    sessionId: str


class SessionIntegrationConfiguration(BaseValidatorModel):
    topicIntegrationArn: Optional[str] = None


class StartContentUploadRequest(BaseValidatorModel):
    contentType: str
    knowledgeBaseId: str
    presignedUrlTimeToLive: Optional[int] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdateContentRequest(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str
    metadata: Optional[Dict[str, str]] = None
    overrideLinkOutUri: Optional[str] = None
    removeOverrideLinkOutUri: Optional[bool] = None
    revisionId: Optional[str] = None
    title: Optional[str] = None
    uploadId: Optional[str] = None


class UpdateKnowledgeBaseTemplateUriRequest(BaseValidatorModel):
    knowledgeBaseId: str
    templateUri: str


class SourceConfigurationOutput(BaseValidatorModel):
    appIntegrations: Optional[AppIntegrationsConfigurationOutput] = None


class SourceConfiguration(BaseValidatorModel):
    appIntegrations: Optional[AppIntegrationsConfiguration] = None


class CreateAssistantAssociationRequest(BaseValidatorModel):
    assistantId: str
    association: AssistantAssociationInputData
    associationType: Literal['KNOWLEDGE_BASE']
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class AssistantAssociationOutputData(BaseValidatorModel):
    knowledgeBaseAssociation: Optional[KnowledgeBaseAssociationData] = None


class AssistantData(BaseValidatorModel):
    assistantArn: str
    assistantId: str
    name: str
    status: AssistantStatusType
    type: Literal['AGENT']
    description: Optional[str] = None
    integrationConfiguration: Optional[AssistantIntegrationConfiguration] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    tags: Optional[Dict[str, str]] = None


class AssistantSummary(BaseValidatorModel):
    assistantArn: str
    assistantId: str
    name: str
    status: AssistantStatusType
    type: Literal['AGENT']
    description: Optional[str] = None
    integrationConfiguration: Optional[AssistantIntegrationConfiguration] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    tags: Optional[Dict[str, str]] = None


class CreateAssistantRequest(BaseValidatorModel):
    name: str
    type: Literal['AGENT']
    clientToken: Optional[str] = None
    description: Optional[str] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    tags: Optional[Dict[str, str]] = None


class Configuration(BaseValidatorModel):
    connectConfiguration: Optional[ConnectConfiguration] = None


class CreateContentResponse(BaseValidatorModel):
    content: ContentData
    ResponseMetadata: ResponseMetadata


class GetContentResponse(BaseValidatorModel):
    content: ContentData
    ResponseMetadata: ResponseMetadata


class GetContentSummaryResponse(BaseValidatorModel):
    contentSummary: ContentSummary
    ResponseMetadata: ResponseMetadata


class ListContentsResponse(BaseValidatorModel):
    contentSummaries: List[ContentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class SearchContentResponse(BaseValidatorModel):
    contentSummaries: List[ContentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartContentUploadResponse(BaseValidatorModel):
    headersToInclude: Dict[str, str]
    uploadId: str
    url: str
    urlExpiry: datetime
    ResponseMetadata: ResponseMetadata


class UpdateContentResponse(BaseValidatorModel):
    content: ContentData
    ResponseMetadata: ResponseMetadata


class DocumentText(BaseValidatorModel):
    highlights: Optional[List[Highlight]] = None
    text: Optional[str] = None


class SearchExpression(BaseValidatorModel):
    filters: List[Filter]

GroupingConfigurationUnion = Union[GroupingConfiguration, GroupingConfigurationOutput]


class ListAssistantAssociationsRequestPaginate(BaseValidatorModel):
    assistantId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssistantsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContentsRequestPaginate(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListImportJobsRequestPaginate(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListKnowledgeBasesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQuickResponsesRequestPaginate(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class QueryAssistantRequestPaginate(BaseValidatorModel):
    assistantId: str
    queryText: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQuickResponsesResponse(BaseValidatorModel):
    quickResponseSummaries: List[QuickResponseSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class NotifyRecommendationsReceivedResponse(BaseValidatorModel):
    errors: List[NotifyRecommendationsReceivedError]
    recommendationIds: List[str]
    ResponseMetadata: ResponseMetadata


class RecommendationTriggerData(BaseValidatorModel):
    query: Optional[QueryRecommendationTriggerData] = None


class QuickResponseContents(BaseValidatorModel):
    markdown: Optional[QuickResponseContentProvider] = None
    plainText: Optional[QuickResponseContentProvider] = None


class QuickResponseSearchExpression(BaseValidatorModel):
    filters: Optional[List[QuickResponseFilterField]] = None
    orderOnField: Optional[QuickResponseOrderField] = None
    queries: Optional[List[QuickResponseQueryField]] = None


class SearchSessionsResponse(BaseValidatorModel):
    sessionSummaries: List[SessionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SessionData(BaseValidatorModel):
    name: str
    sessionArn: str
    sessionId: str
    description: Optional[str] = None
    integrationConfiguration: Optional[SessionIntegrationConfiguration] = None
    tags: Optional[Dict[str, str]] = None


class KnowledgeBaseData(BaseValidatorModel):
    knowledgeBaseArn: str
    knowledgeBaseId: str
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    status: KnowledgeBaseStatusType
    description: Optional[str] = None
    lastContentModificationTime: Optional[datetime] = None
    renderingConfiguration: Optional[RenderingConfiguration] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    sourceConfiguration: Optional[SourceConfigurationOutput] = None
    tags: Optional[Dict[str, str]] = None


class KnowledgeBaseSummary(BaseValidatorModel):
    knowledgeBaseArn: str
    knowledgeBaseId: str
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    status: KnowledgeBaseStatusType
    description: Optional[str] = None
    renderingConfiguration: Optional[RenderingConfiguration] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    sourceConfiguration: Optional[SourceConfigurationOutput] = None
    tags: Optional[Dict[str, str]] = None

SourceConfigurationUnion = Union[SourceConfiguration, SourceConfigurationOutput]


class AssistantAssociationData(BaseValidatorModel):
    assistantArn: str
    assistantAssociationArn: str
    assistantAssociationId: str
    assistantId: str
    associationData: AssistantAssociationOutputData
    associationType: Literal['KNOWLEDGE_BASE']
    tags: Optional[Dict[str, str]] = None


class AssistantAssociationSummary(BaseValidatorModel):
    assistantArn: str
    assistantAssociationArn: str
    assistantAssociationId: str
    assistantId: str
    associationData: AssistantAssociationOutputData
    associationType: Literal['KNOWLEDGE_BASE']
    tags: Optional[Dict[str, str]] = None


class CreateAssistantResponse(BaseValidatorModel):
    assistant: AssistantData
    ResponseMetadata: ResponseMetadata


class GetAssistantResponse(BaseValidatorModel):
    assistant: AssistantData
    ResponseMetadata: ResponseMetadata


class ListAssistantsResponse(BaseValidatorModel):
    assistantSummaries: List[AssistantSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ExternalSourceConfiguration(BaseValidatorModel):
    configuration: Configuration
    source: Literal['AMAZON_CONNECT']


class Document(BaseValidatorModel):
    contentReference: ContentReference
    excerpt: Optional[DocumentText] = None
    title: Optional[DocumentText] = None


class SearchContentRequestPaginate(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: SearchExpression
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchContentRequest(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: SearchExpression
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SearchSessionsRequestPaginate(BaseValidatorModel):
    assistantId: str
    searchExpression: SearchExpression
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchSessionsRequest(BaseValidatorModel):
    assistantId: str
    searchExpression: SearchExpression
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class CreateQuickResponseRequest(BaseValidatorModel):
    content: QuickResponseDataProvider
    knowledgeBaseId: str
    name: str
    channels: Optional[List[str]] = None
    clientToken: Optional[str] = None
    contentType: Optional[str] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationUnion] = None
    isActive: Optional[bool] = None
    language: Optional[str] = None
    shortcutKey: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class UpdateQuickResponseRequest(BaseValidatorModel):
    knowledgeBaseId: str
    quickResponseId: str
    channels: Optional[List[str]] = None
    content: Optional[QuickResponseDataProvider] = None
    contentType: Optional[str] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationUnion] = None
    isActive: Optional[bool] = None
    language: Optional[str] = None
    name: Optional[str] = None
    removeDescription: Optional[bool] = None
    removeGroupingConfiguration: Optional[bool] = None
    removeShortcutKey: Optional[bool] = None
    shortcutKey: Optional[str] = None


class RecommendationTrigger(BaseValidatorModel):
    data: RecommendationTriggerData
    id: str
    recommendationIds: List[str]
    source: RecommendationSourceTypeType
    type: Literal['QUERY']


class QuickResponseData(BaseValidatorModel):
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
    contents: Optional[QuickResponseContents] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationOutput] = None
    isActive: Optional[bool] = None
    language: Optional[str] = None
    lastModifiedBy: Optional[str] = None
    shortcutKey: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class QuickResponseSearchResultData(BaseValidatorModel):
    contentType: str
    contents: QuickResponseContents
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
    groupingConfiguration: Optional[GroupingConfigurationOutput] = None
    language: Optional[str] = None
    lastModifiedBy: Optional[str] = None
    shortcutKey: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class SearchQuickResponsesRequestPaginate(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: QuickResponseSearchExpression
    attributes: Optional[Dict[str, str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchQuickResponsesRequest(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: QuickResponseSearchExpression
    attributes: Optional[Dict[str, str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class CreateSessionResponse(BaseValidatorModel):
    session: SessionData
    ResponseMetadata: ResponseMetadata


class GetSessionResponse(BaseValidatorModel):
    session: SessionData
    ResponseMetadata: ResponseMetadata


class CreateKnowledgeBaseResponse(BaseValidatorModel):
    knowledgeBase: KnowledgeBaseData
    ResponseMetadata: ResponseMetadata


class GetKnowledgeBaseResponse(BaseValidatorModel):
    knowledgeBase: KnowledgeBaseData
    ResponseMetadata: ResponseMetadata


class UpdateKnowledgeBaseTemplateUriResponse(BaseValidatorModel):
    knowledgeBase: KnowledgeBaseData
    ResponseMetadata: ResponseMetadata


class ListKnowledgeBasesResponse(BaseValidatorModel):
    knowledgeBaseSummaries: List[KnowledgeBaseSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateKnowledgeBaseRequest(BaseValidatorModel):
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    renderingConfiguration: Optional[RenderingConfiguration] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    sourceConfiguration: Optional[SourceConfigurationUnion] = None
    tags: Optional[Dict[str, str]] = None


class CreateAssistantAssociationResponse(BaseValidatorModel):
    assistantAssociation: AssistantAssociationData
    ResponseMetadata: ResponseMetadata


class GetAssistantAssociationResponse(BaseValidatorModel):
    assistantAssociation: AssistantAssociationData
    ResponseMetadata: ResponseMetadata


class ListAssistantAssociationsResponse(BaseValidatorModel):
    assistantAssociationSummaries: List[AssistantAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ImportJobData(BaseValidatorModel):
    createdTime: datetime
    importJobId: str
    importJobType: Literal['QUICK_RESPONSES']
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedTime: datetime
    status: ImportJobStatusType
    uploadId: str
    url: str
    urlExpiry: datetime
    externalSourceConfiguration: Optional[ExternalSourceConfiguration] = None
    failedRecordReport: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None


class ImportJobSummary(BaseValidatorModel):
    createdTime: datetime
    importJobId: str
    importJobType: Literal['QUICK_RESPONSES']
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedTime: datetime
    status: ImportJobStatusType
    uploadId: str
    externalSourceConfiguration: Optional[ExternalSourceConfiguration] = None
    metadata: Optional[Dict[str, str]] = None


class StartImportJobRequest(BaseValidatorModel):
    importJobType: Literal['QUICK_RESPONSES']
    knowledgeBaseId: str
    uploadId: str
    clientToken: Optional[str] = None
    externalSourceConfiguration: Optional[ExternalSourceConfiguration] = None
    metadata: Optional[Dict[str, str]] = None


class RecommendationData(BaseValidatorModel):
    document: Document
    recommendationId: str
    relevanceLevel: Optional[RelevanceLevelType] = None
    relevanceScore: Optional[float] = None
    type: Optional[Literal['KNOWLEDGE_CONTENT']] = None


class ResultData(BaseValidatorModel):
    document: Document
    resultId: str
    relevanceScore: Optional[float] = None


class CreateQuickResponseResponse(BaseValidatorModel):
    quickResponse: QuickResponseData
    ResponseMetadata: ResponseMetadata


class GetQuickResponseResponse(BaseValidatorModel):
    quickResponse: QuickResponseData
    ResponseMetadata: ResponseMetadata


class UpdateQuickResponseResponse(BaseValidatorModel):
    quickResponse: QuickResponseData
    ResponseMetadata: ResponseMetadata


class SearchQuickResponsesResponse(BaseValidatorModel):
    results: List[QuickResponseSearchResultData]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetImportJobResponse(BaseValidatorModel):
    importJob: ImportJobData
    ResponseMetadata: ResponseMetadata


class StartImportJobResponse(BaseValidatorModel):
    importJob: ImportJobData
    ResponseMetadata: ResponseMetadata


class ListImportJobsResponse(BaseValidatorModel):
    importJobSummaries: List[ImportJobSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetRecommendationsResponse(BaseValidatorModel):
    recommendations: List[RecommendationData]
    triggers: List[RecommendationTrigger]
    ResponseMetadata: ResponseMetadata


class QueryAssistantResponse(BaseValidatorModel):
    results: List[ResultData]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None