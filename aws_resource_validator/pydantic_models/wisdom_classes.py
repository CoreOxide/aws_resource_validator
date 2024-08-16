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
from aws_resource_validator.pydantic_models.wisdom_constants import *

class AppIntegrationsConfigurationPaginatorTypeDef(BaseValidatorModel):
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
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

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

class CreateSessionRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str
    name: str
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class DeleteAssistantAssociationRequestRequestTypeDef(BaseValidatorModel):
    assistantAssociationId: str
    assistantId: str

class DeleteAssistantRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str

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

class GroupingConfigurationPaginatorTypeDef(BaseValidatorModel):
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

class QueryAssistantRequestRequestTypeDef(BaseValidatorModel):
    assistantId: str
    queryText: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

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

class SourceConfigurationPaginatorTypeDef(BaseValidatorModel):
    appIntegrations: Optional[AppIntegrationsConfigurationPaginatorTypeDef] = None

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

class QueryAssistantRequestQueryAssistantPaginateTypeDef(BaseValidatorModel):
    assistantId: str
    queryText: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQuickResponsesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    quickResponseSummaries: List[QuickResponseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class NotifyRecommendationsReceivedResponseTypeDef(BaseValidatorModel):
    errors: List[NotifyRecommendationsReceivedErrorTypeDef]
    recommendationIds: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

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

class SessionDataTypeDef(BaseValidatorModel):
    name: str
    sessionArn: str
    sessionId: str
    description: Optional[str] = None
    integrationConfiguration: Optional[SessionIntegrationConfigurationTypeDef] = None
    tags: Optional[Dict[str, str]] = None

class KnowledgeBaseSummaryPaginatorTypeDef(BaseValidatorModel):
    knowledgeBaseArn: str
    knowledgeBaseId: str
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    status: KnowledgeBaseStatusType
    description: Optional[str] = None
    renderingConfiguration: Optional[RenderingConfigurationTypeDef] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    sourceConfiguration: Optional[SourceConfigurationPaginatorTypeDef] = None
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
    sourceConfiguration: Optional[SourceConfigurationTypeDef] = None
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
    sourceConfiguration: Optional[SourceConfigurationTypeDef] = None
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

class DocumentTypeDef(BaseValidatorModel):
    contentReference: ContentReferenceTypeDef
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

class RecommendationTriggerTypeDef(BaseValidatorModel):
    data: RecommendationTriggerDataTypeDef
    id: str
    recommendationIds: List[str]
    source: RecommendationSourceTypeType
    type: Literal["QUERY"]

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
    groupingConfiguration: Optional[GroupingConfigurationTypeDef] = None
    isActive: Optional[bool] = None
    language: Optional[str] = None
    lastModifiedBy: Optional[str] = None
    shortcutKey: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class QuickResponseSearchResultDataPaginatorTypeDef(BaseValidatorModel):
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
    groupingConfiguration: Optional[GroupingConfigurationPaginatorTypeDef] = None
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
    groupingConfiguration: Optional[GroupingConfigurationTypeDef] = None
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

class CreateSessionResponseTypeDef(BaseValidatorModel):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSessionResponseTypeDef(BaseValidatorModel):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListKnowledgeBasesResponsePaginatorTypeDef(BaseValidatorModel):
    knowledgeBaseSummaries: List[KnowledgeBaseSummaryPaginatorTypeDef]
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
    document: DocumentTypeDef
    recommendationId: str
    relevanceLevel: Optional[RelevanceLevelType] = None
    relevanceScore: Optional[float] = None
    type: Optional[Literal["KNOWLEDGE_CONTENT"]] = None

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

class SearchQuickResponsesResponsePaginatorTypeDef(BaseValidatorModel):
    nextToken: str
    results: List[QuickResponseSearchResultDataPaginatorTypeDef]
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

