from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.wisdom_constants import *

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


class AssistantIntegrationConfigurationTypeDef(BaseValidatorModel):
    topicIntegrationArn: Optional[str] = None


class ServerSideEncryptionConfigurationTypeDef(BaseValidatorModel):
    kmsKeyId: Optional[str] = None


class ConnectConfigurationTypeDef(BaseValidatorModel):
    instanceId: Optional[str] = None


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


class CreateContentRequestTypeDef(BaseValidatorModel):
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


class QuickResponseDataProviderTypeDef(BaseValidatorModel):
    content: Optional[str] = None


class CreateSessionRequestTypeDef(BaseValidatorModel):
    assistantId: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class DeleteAssistantAssociationRequestTypeDef(BaseValidatorModel):
    assistantAssociationId: str
    assistantId: str


class DeleteAssistantRequestTypeDef(BaseValidatorModel):
    assistantId: str


class DeleteContentRequestTypeDef(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str


class DeleteImportJobRequestTypeDef(BaseValidatorModel):
    importJobId: str
    knowledgeBaseId: str


class DeleteKnowledgeBaseRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str


class DeleteQuickResponseRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    quickResponseId: str


class HighlightTypeDef(BaseValidatorModel):
    beginOffsetInclusive: Optional[int] = None
    endOffsetExclusive: Optional[int] = None


class GetAssistantAssociationRequestTypeDef(BaseValidatorModel):
    assistantAssociationId: str
    assistantId: str


class GetAssistantRequestTypeDef(BaseValidatorModel):
    assistantId: str


class GetContentRequestTypeDef(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str


class GetContentSummaryRequestTypeDef(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str


class GetImportJobRequestTypeDef(BaseValidatorModel):
    importJobId: str
    knowledgeBaseId: str


class GetKnowledgeBaseRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str


class GetQuickResponseRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    quickResponseId: str


class GetRecommendationsRequestTypeDef(BaseValidatorModel):
    assistantId: str
    sessionId: str
    maxResults: Optional[int] = None
    waitTimeSeconds: Optional[int] = None


class GetSessionRequestTypeDef(BaseValidatorModel):
    assistantId: str
    sessionId: str


class GroupingConfigurationOutputTypeDef(BaseValidatorModel):
    criteria: Optional[str] = None
    values: Optional[List[str]] = None


class GroupingConfigurationTypeDef(BaseValidatorModel):
    criteria: Optional[str] = None
    values: Optional[Sequence[str]] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAssistantAssociationsRequestTypeDef(BaseValidatorModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAssistantsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListContentsRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListImportJobsRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListKnowledgeBasesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListQuickResponsesRequestTypeDef(BaseValidatorModel):
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


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class NotifyRecommendationsReceivedErrorTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    recommendationId: Optional[str] = None


class NotifyRecommendationsReceivedRequestTypeDef(BaseValidatorModel):
    assistantId: str
    recommendationIds: Sequence[str]
    sessionId: str


class QueryAssistantRequestTypeDef(BaseValidatorModel):
    assistantId: str
    queryText: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class QueryRecommendationTriggerDataTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class QuickResponseContentProviderTypeDef(BaseValidatorModel):
    content: Optional[str] = None


class QuickResponseOrderFieldTypeDef(BaseValidatorModel):
    name: str
    order: Optional[OrderType] = None


class RemoveKnowledgeBaseTemplateUriRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str


class SessionSummaryTypeDef(BaseValidatorModel):
    assistantArn: str
    assistantId: str
    sessionArn: str
    sessionId: str


class SessionIntegrationConfigurationTypeDef(BaseValidatorModel):
    topicIntegrationArn: Optional[str] = None


class StartContentUploadRequestTypeDef(BaseValidatorModel):
    contentType: str
    knowledgeBaseId: str
    presignedUrlTimeToLive: Optional[int] = None


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateContentRequestTypeDef(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str
    metadata: Optional[Mapping[str, str]] = None
    overrideLinkOutUri: Optional[str] = None
    removeOverrideLinkOutUri: Optional[bool] = None
    revisionId: Optional[str] = None
    title: Optional[str] = None
    uploadId: Optional[str] = None


class UpdateKnowledgeBaseTemplateUriRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    templateUri: str


class SourceConfigurationOutputTypeDef(BaseValidatorModel):
    appIntegrations: Optional[AppIntegrationsConfigurationOutputTypeDef] = None


class SourceConfigurationTypeDef(BaseValidatorModel):
    appIntegrations: Optional[AppIntegrationsConfigurationTypeDef] = None


class CreateAssistantAssociationRequestTypeDef(BaseValidatorModel):
    assistantId: str
    association: AssistantAssociationInputDataTypeDef
    associationType: Literal["KNOWLEDGE_BASE"]
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class AssistantAssociationOutputDataTypeDef(BaseValidatorModel):
    knowledgeBaseAssociation: Optional[KnowledgeBaseAssociationDataTypeDef] = None


class ConfigurationTypeDef(BaseValidatorModel):
    connectConfiguration: Optional[ConnectConfigurationTypeDef] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class SearchContentResponseTypeDef(BaseValidatorModel):
    contentSummaries: List[ContentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartContentUploadResponseTypeDef(BaseValidatorModel):
    headersToInclude: Dict[str, str]
    uploadId: str
    url: str
    urlExpiry: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateContentResponseTypeDef(BaseValidatorModel):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DocumentTextTypeDef(BaseValidatorModel):
    highlights: Optional[List[HighlightTypeDef]] = None
    text: Optional[str] = None


class FilterTypeDef(BaseValidatorModel):
    pass


class SearchExpressionTypeDef(BaseValidatorModel):
    filters: Sequence[FilterTypeDef]


class ListAssistantAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    assistantId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssistantsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListContentsRequestPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListImportJobsRequestPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListKnowledgeBasesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQuickResponsesRequestPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class QueryAssistantRequestPaginateTypeDef(BaseValidatorModel):
    assistantId: str
    queryText: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQuickResponsesResponseTypeDef(BaseValidatorModel):
    quickResponseSummaries: List[QuickResponseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class NotifyRecommendationsReceivedResponseTypeDef(BaseValidatorModel):
    errors: List[NotifyRecommendationsReceivedErrorTypeDef]
    recommendationIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef


class RecommendationTriggerDataTypeDef(BaseValidatorModel):
    query: Optional[QueryRecommendationTriggerDataTypeDef] = None


class QuickResponseContentsTypeDef(BaseValidatorModel):
    markdown: Optional[QuickResponseContentProviderTypeDef] = None
    plainText: Optional[QuickResponseContentProviderTypeDef] = None


class QuickResponseQueryFieldTypeDef(BaseValidatorModel):
    pass


class QuickResponseFilterFieldTypeDef(BaseValidatorModel):
    pass


class QuickResponseSearchExpressionTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[QuickResponseFilterFieldTypeDef]] = None
    orderOnField: Optional[QuickResponseOrderFieldTypeDef] = None
    queries: Optional[Sequence[QuickResponseQueryFieldTypeDef]] = None


class SearchSessionsResponseTypeDef(BaseValidatorModel):
    sessionSummaries: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SessionDataTypeDef(BaseValidatorModel):
    name: str
    sessionArn: str
    sessionId: str
    description: Optional[str] = None
    integrationConfiguration: Optional[SessionIntegrationConfigurationTypeDef] = None
    tags: Optional[Dict[str, str]] = None


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


class AssistantDataTypeDef(BaseValidatorModel):
    pass


class CreateAssistantResponseTypeDef(BaseValidatorModel):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAssistantResponseTypeDef(BaseValidatorModel):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssistantSummaryTypeDef(BaseValidatorModel):
    pass


class ListAssistantsResponseTypeDef(BaseValidatorModel):
    assistantSummaries: List[AssistantSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ExternalSourceConfigurationTypeDef(BaseValidatorModel):
    configuration: ConfigurationTypeDef
    source: Literal["AMAZON_CONNECT"]


class DocumentTypeDef(BaseValidatorModel):
    contentReference: ContentReferenceTypeDef
    excerpt: Optional[DocumentTextTypeDef] = None
    title: Optional[DocumentTextTypeDef] = None


class SearchContentRequestPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: SearchExpressionTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchContentRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: SearchExpressionTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class SearchSessionsRequestPaginateTypeDef(BaseValidatorModel):
    assistantId: str
    searchExpression: SearchExpressionTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchSessionsRequestTypeDef(BaseValidatorModel):
    assistantId: str
    searchExpression: SearchExpressionTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GroupingConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateQuickResponseRequestTypeDef(BaseValidatorModel):
    content: QuickResponseDataProviderTypeDef
    knowledgeBaseId: str
    name: str
    channels: Optional[Sequence[str]] = None
    clientToken: Optional[str] = None
    contentType: Optional[str] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationUnionTypeDef] = None
    isActive: Optional[bool] = None
    language: Optional[str] = None
    shortcutKey: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateQuickResponseRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    quickResponseId: str
    channels: Optional[Sequence[str]] = None
    content: Optional[QuickResponseDataProviderTypeDef] = None
    contentType: Optional[str] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationUnionTypeDef] = None
    isActive: Optional[bool] = None
    language: Optional[str] = None
    name: Optional[str] = None
    removeDescription: Optional[bool] = None
    removeGroupingConfiguration: Optional[bool] = None
    removeShortcutKey: Optional[bool] = None
    shortcutKey: Optional[str] = None


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


class SearchQuickResponsesRequestPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: QuickResponseSearchExpressionTypeDef
    attributes: Optional[Mapping[str, str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchQuickResponsesRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: QuickResponseSearchExpressionTypeDef
    attributes: Optional[Mapping[str, str]] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class CreateSessionResponseTypeDef(BaseValidatorModel):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSessionResponseTypeDef(BaseValidatorModel):
    session: SessionDataTypeDef
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
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SourceConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateKnowledgeBaseRequestTypeDef(BaseValidatorModel):
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    renderingConfiguration: Optional[RenderingConfigurationTypeDef] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    sourceConfiguration: Optional[SourceConfigurationUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class CreateAssistantAssociationResponseTypeDef(BaseValidatorModel):
    assistantAssociation: AssistantAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAssistantAssociationResponseTypeDef(BaseValidatorModel):
    assistantAssociation: AssistantAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListAssistantAssociationsResponseTypeDef(BaseValidatorModel):
    assistantAssociationSummaries: List[AssistantAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class StartImportJobRequestTypeDef(BaseValidatorModel):
    importJobType: Literal["QUICK_RESPONSES"]
    knowledgeBaseId: str
    uploadId: str
    clientToken: Optional[str] = None
    externalSourceConfiguration: Optional[ExternalSourceConfigurationTypeDef] = None
    metadata: Optional[Mapping[str, str]] = None


class ResultDataTypeDef(BaseValidatorModel):
    document: DocumentTypeDef
    resultId: str
    relevanceScore: Optional[float] = None


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
    results: List[QuickResponseSearchResultDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetImportJobResponseTypeDef(BaseValidatorModel):
    importJob: ImportJobDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StartImportJobResponseTypeDef(BaseValidatorModel):
    importJob: ImportJobDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListImportJobsResponseTypeDef(BaseValidatorModel):
    importJobSummaries: List[ImportJobSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RecommendationTriggerTypeDef(BaseValidatorModel):
    pass


class RecommendationDataTypeDef(BaseValidatorModel):
    pass


class GetRecommendationsResponseTypeDef(BaseValidatorModel):
    recommendations: List[RecommendationDataTypeDef]
    triggers: List[RecommendationTriggerTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class QueryAssistantResponseTypeDef(BaseValidatorModel):
    results: List[ResultDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


