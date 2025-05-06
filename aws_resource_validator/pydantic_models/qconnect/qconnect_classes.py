from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.qconnect.qconnect_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AIAgentConfigurationData(BaseValidatorModel):
    aiAgentId: str


class GuardrailContentFilterConfig(BaseValidatorModel):
    inputStrength: GuardrailFilterStrengthType
    outputStrength: GuardrailFilterStrengthType
    type: GuardrailContentFilterTypeType


class GuardrailContextualGroundingFilterConfig(BaseValidatorModel):
    threshold: float
    type: GuardrailContextualGroundingFilterTypeType


class GuardrailPiiEntityConfig(BaseValidatorModel):
    action: GuardrailSensitiveInformationActionType
    type: GuardrailPiiEntityTypeType


class GuardrailRegexConfig(BaseValidatorModel):
    action: GuardrailSensitiveInformationActionType
    name: str
    pattern: str
    description: Optional[str] = None


class AIGuardrailSummary(BaseValidatorModel):
    aiGuardrailArn: str
    aiGuardrailId: str
    assistantArn: str
    assistantId: str
    name: str
    visibilityStatus: VisibilityStatusType
    description: Optional[str] = None
    modifiedTime: Optional[datetime] = None
    status: Optional[StatusType] = None
    tags: Optional[Dict[str, str]] = None


class GuardrailTopicConfigOutput(BaseValidatorModel):
    definition: str
    name: str
    type: Literal['DENY']
    examples: Optional[List[str]] = None


class GuardrailTopicConfig(BaseValidatorModel):
    definition: str
    name: str
    type: Literal['DENY']
    examples: Optional[List[str]] = None


class GuardrailManagedWordsConfig(BaseValidatorModel):
    type: Literal['PROFANITY']


class GuardrailWordConfig(BaseValidatorModel):
    text: str


class AIPromptSummary(BaseValidatorModel):
    aiPromptArn: str
    aiPromptId: str
    apiFormat: AIPromptAPIFormatType
    assistantArn: str
    assistantId: str
    modelId: str
    name: str
    templateType: Literal['TEXT']
    type: AIPromptTypeType
    visibilityStatus: VisibilityStatusType
    description: Optional[str] = None
    modifiedTime: Optional[datetime] = None
    origin: Optional[OriginType] = None
    status: Optional[StatusType] = None
    tags: Optional[Dict[str, str]] = None


class TextFullAIPromptEditTemplateConfiguration(BaseValidatorModel):
    text: str


class ActivateMessageTemplateRequest(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    versionNumber: int


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AgentAttributes(BaseValidatorModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None


class AmazonConnectGuideAssociationData(BaseValidatorModel):
    flowId: Optional[str] = None


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


class AssistantCapabilityConfiguration(BaseValidatorModel):
    type: Optional[AssistantCapabilityTypeType] = None


class AssistantIntegrationConfiguration(BaseValidatorModel):
    topicIntegrationArn: Optional[str] = None


class ServerSideEncryptionConfiguration(BaseValidatorModel):
    kmsKeyId: Optional[str] = None


class ParsingPrompt(BaseValidatorModel):
    parsingPromptText: str


class FixedSizeChunkingConfiguration(BaseValidatorModel):
    maxTokens: int
    overlapPercentage: int


class SemanticChunkingConfiguration(BaseValidatorModel):
    breakpointPercentileThreshold: int
    bufferSize: int
    maxTokens: int


class CitationSpan(BaseValidatorModel):
    beginOffsetInclusive: Optional[int] = None
    endOffsetExclusive: Optional[int] = None


class ConnectConfiguration(BaseValidatorModel):
    instanceId: Optional[str] = None


class RankingData(BaseValidatorModel):
    relevanceLevel: Optional[RelevanceLevelType] = None
    relevanceScore: Optional[float] = None


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


class GenerativeContentFeedbackData(BaseValidatorModel):
    relevance: RelevanceType


class ContentReference(BaseValidatorModel):
    contentArn: Optional[str] = None
    contentId: Optional[str] = None
    knowledgeBaseArn: Optional[str] = None
    knowledgeBaseId: Optional[str] = None
    referenceType: Optional[ReferenceTypeType] = None
    sourceURL: Optional[str] = None


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


class SelfServiceConversationHistory(BaseValidatorModel):
    turnNumber: int
    botResponse: Optional[str] = None
    inputTranscript: Optional[str] = None


class ConversationState(BaseValidatorModel):
    status: ConversationStatusType
    reason: Optional[ConversationStatusReasonType] = None

Timestamp = Union[datetime, str]


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


class CreateMessageTemplateAttachmentRequest(BaseValidatorModel):
    body: str
    contentDisposition: Literal['ATTACHMENT']
    knowledgeBaseId: str
    messageTemplateId: str
    name: str
    clientToken: Optional[str] = None


class MessageTemplateAttachment(BaseValidatorModel):
    attachmentId: str
    contentDisposition: Literal['ATTACHMENT']
    name: str
    uploadedTime: datetime
    url: str
    urlExpiry: datetime


class CreateMessageTemplateVersionRequest(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    messageTemplateContentSha256: Optional[str] = None


class QuickResponseDataProvider(BaseValidatorModel):
    content: Optional[str] = None


class CustomerProfileAttributesOutput(BaseValidatorModel):
    accountNumber: Optional[str] = None
    additionalInformation: Optional[str] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    address3: Optional[str] = None
    address4: Optional[str] = None
    billingAddress1: Optional[str] = None
    billingAddress2: Optional[str] = None
    billingAddress3: Optional[str] = None
    billingAddress4: Optional[str] = None
    billingCity: Optional[str] = None
    billingCountry: Optional[str] = None
    billingCounty: Optional[str] = None
    billingPostalCode: Optional[str] = None
    billingProvince: Optional[str] = None
    billingState: Optional[str] = None
    birthDate: Optional[str] = None
    businessEmailAddress: Optional[str] = None
    businessName: Optional[str] = None
    businessPhoneNumber: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    county: Optional[str] = None
    custom: Optional[Dict[str, str]] = None
    emailAddress: Optional[str] = None
    firstName: Optional[str] = None
    gender: Optional[str] = None
    homePhoneNumber: Optional[str] = None
    lastName: Optional[str] = None
    mailingAddress1: Optional[str] = None
    mailingAddress2: Optional[str] = None
    mailingAddress3: Optional[str] = None
    mailingAddress4: Optional[str] = None
    mailingCity: Optional[str] = None
    mailingCountry: Optional[str] = None
    mailingCounty: Optional[str] = None
    mailingPostalCode: Optional[str] = None
    mailingProvince: Optional[str] = None
    mailingState: Optional[str] = None
    middleName: Optional[str] = None
    mobilePhoneNumber: Optional[str] = None
    partyType: Optional[str] = None
    phoneNumber: Optional[str] = None
    postalCode: Optional[str] = None
    profileARN: Optional[str] = None
    profileId: Optional[str] = None
    province: Optional[str] = None
    shippingAddress1: Optional[str] = None
    shippingAddress2: Optional[str] = None
    shippingAddress3: Optional[str] = None
    shippingAddress4: Optional[str] = None
    shippingCity: Optional[str] = None
    shippingCountry: Optional[str] = None
    shippingCounty: Optional[str] = None
    shippingPostalCode: Optional[str] = None
    shippingProvince: Optional[str] = None
    shippingState: Optional[str] = None
    state: Optional[str] = None


class CustomerProfileAttributes(BaseValidatorModel):
    accountNumber: Optional[str] = None
    additionalInformation: Optional[str] = None
    address1: Optional[str] = None
    address2: Optional[str] = None
    address3: Optional[str] = None
    address4: Optional[str] = None
    billingAddress1: Optional[str] = None
    billingAddress2: Optional[str] = None
    billingAddress3: Optional[str] = None
    billingAddress4: Optional[str] = None
    billingCity: Optional[str] = None
    billingCountry: Optional[str] = None
    billingCounty: Optional[str] = None
    billingPostalCode: Optional[str] = None
    billingProvince: Optional[str] = None
    billingState: Optional[str] = None
    birthDate: Optional[str] = None
    businessEmailAddress: Optional[str] = None
    businessName: Optional[str] = None
    businessPhoneNumber: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    county: Optional[str] = None
    custom: Optional[Dict[str, str]] = None
    emailAddress: Optional[str] = None
    firstName: Optional[str] = None
    gender: Optional[str] = None
    homePhoneNumber: Optional[str] = None
    lastName: Optional[str] = None
    mailingAddress1: Optional[str] = None
    mailingAddress2: Optional[str] = None
    mailingAddress3: Optional[str] = None
    mailingAddress4: Optional[str] = None
    mailingCity: Optional[str] = None
    mailingCountry: Optional[str] = None
    mailingCounty: Optional[str] = None
    mailingPostalCode: Optional[str] = None
    mailingProvince: Optional[str] = None
    mailingState: Optional[str] = None
    middleName: Optional[str] = None
    mobilePhoneNumber: Optional[str] = None
    partyType: Optional[str] = None
    phoneNumber: Optional[str] = None
    postalCode: Optional[str] = None
    profileARN: Optional[str] = None
    profileId: Optional[str] = None
    province: Optional[str] = None
    shippingAddress1: Optional[str] = None
    shippingAddress2: Optional[str] = None
    shippingAddress3: Optional[str] = None
    shippingAddress4: Optional[str] = None
    shippingCity: Optional[str] = None
    shippingCountry: Optional[str] = None
    shippingCounty: Optional[str] = None
    shippingPostalCode: Optional[str] = None
    shippingProvince: Optional[str] = None
    shippingState: Optional[str] = None
    state: Optional[str] = None


class IntentDetectedDataDetails(BaseValidatorModel):
    intent: str
    intentId: str


class GenerativeReference(BaseValidatorModel):
    generationId: Optional[str] = None
    modelId: Optional[str] = None


class DeactivateMessageTemplateRequest(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    versionNumber: int


class DeleteAIAgentRequest(BaseValidatorModel):
    aiAgentId: str
    assistantId: str


class DeleteAIAgentVersionRequest(BaseValidatorModel):
    aiAgentId: str
    assistantId: str
    versionNumber: int


class DeleteAIGuardrailRequest(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str


class DeleteAIGuardrailVersionRequest(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str
    versionNumber: int


class DeleteAIPromptRequest(BaseValidatorModel):
    aiPromptId: str
    assistantId: str


class DeleteAIPromptVersionRequest(BaseValidatorModel):
    aiPromptId: str
    assistantId: str
    versionNumber: int


class DeleteAssistantAssociationRequest(BaseValidatorModel):
    assistantAssociationId: str
    assistantId: str


class DeleteAssistantRequest(BaseValidatorModel):
    assistantId: str


class DeleteContentAssociationRequest(BaseValidatorModel):
    contentAssociationId: str
    contentId: str
    knowledgeBaseId: str


class DeleteContentRequest(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str


class DeleteImportJobRequest(BaseValidatorModel):
    importJobId: str
    knowledgeBaseId: str


class DeleteKnowledgeBaseRequest(BaseValidatorModel):
    knowledgeBaseId: str


class DeleteMessageTemplateAttachmentRequest(BaseValidatorModel):
    attachmentId: str
    knowledgeBaseId: str
    messageTemplateId: str


class DeleteMessageTemplateRequest(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str


class DeleteQuickResponseRequest(BaseValidatorModel):
    knowledgeBaseId: str
    quickResponseId: str


class Highlight(BaseValidatorModel):
    beginOffsetInclusive: Optional[int] = None
    endOffsetExclusive: Optional[int] = None


class EmailHeader(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None


class MessageTemplateBodyContentProvider(BaseValidatorModel):
    content: Optional[str] = None


class GroupingConfigurationOutput(BaseValidatorModel):
    criteria: Optional[str] = None
    values: Optional[List[str]] = None


class Filter(BaseValidatorModel):
    field: Literal['NAME']
    operator: Literal['EQUALS']
    value: str


class GetAIAgentRequest(BaseValidatorModel):
    aiAgentId: str
    assistantId: str


class GetAIGuardrailRequest(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str


class GetAIPromptRequest(BaseValidatorModel):
    aiPromptId: str
    assistantId: str


class GetAssistantAssociationRequest(BaseValidatorModel):
    assistantAssociationId: str
    assistantId: str


class GetAssistantRequest(BaseValidatorModel):
    assistantId: str


class GetContentAssociationRequest(BaseValidatorModel):
    contentAssociationId: str
    contentId: str
    knowledgeBaseId: str


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


class GetMessageTemplateRequest(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str


class GetNextMessageRequest(BaseValidatorModel):
    assistantId: str
    nextMessageToken: str
    sessionId: str


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


class GroupingConfiguration(BaseValidatorModel):
    criteria: Optional[str] = None
    values: Optional[List[str]] = None


class HierarchicalChunkingLevelConfiguration(BaseValidatorModel):
    maxTokens: int


class IntentInputData(BaseValidatorModel):
    intentId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAIAgentVersionsRequest(BaseValidatorModel):
    aiAgentId: str
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    origin: Optional[OriginType] = None


class ListAIAgentsRequest(BaseValidatorModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    origin: Optional[OriginType] = None


class ListAIGuardrailVersionsRequest(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAIGuardrailsRequest(BaseValidatorModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAIPromptVersionsRequest(BaseValidatorModel):
    aiPromptId: str
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    origin: Optional[OriginType] = None


class ListAIPromptsRequest(BaseValidatorModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    origin: Optional[OriginType] = None


class ListAssistantAssociationsRequest(BaseValidatorModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAssistantsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListContentAssociationsRequest(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str
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


class ListMessageTemplateVersionsRequest(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MessageTemplateVersionSummary(BaseValidatorModel):
    channelSubtype: ChannelSubtypeType
    isActive: bool
    knowledgeBaseArn: str
    knowledgeBaseId: str
    messageTemplateArn: str
    messageTemplateId: str
    name: str
    versionNumber: int


class ListMessageTemplatesRequest(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MessageTemplateSummary(BaseValidatorModel):
    channelSubtype: ChannelSubtypeType
    createdTime: datetime
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedBy: str
    lastModifiedTime: datetime
    messageTemplateArn: str
    messageTemplateId: str
    name: str
    activeVersionNumber: Optional[int] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListMessagesRequest(BaseValidatorModel):
    assistantId: str
    sessionId: str
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


class TextMessage(BaseValidatorModel):
    value: Optional[str] = None


class MessageTemplateFilterField(BaseValidatorModel):
    name: str
    operator: MessageTemplateFilterOperatorType
    includeNoExistence: Optional[bool] = None
    values: Optional[List[str]] = None


class MessageTemplateOrderField(BaseValidatorModel):
    name: str
    order: Optional[OrderType] = None


class MessageTemplateQueryField(BaseValidatorModel):
    name: str
    operator: MessageTemplateQueryOperatorType
    values: List[str]
    allowFuzziness: Optional[bool] = None
    priority: Optional[PriorityType] = None


class NotifyRecommendationsReceivedError(BaseValidatorModel):
    message: Optional[str] = None
    recommendationId: Optional[str] = None


class NotifyRecommendationsReceivedRequest(BaseValidatorModel):
    assistantId: str
    recommendationIds: List[str]
    sessionId: str


class TagCondition(BaseValidatorModel):
    key: str
    value: Optional[str] = None


class QueryConditionItem(BaseValidatorModel):
    comparator: Literal['EQUALS']
    field: Literal['RESULT_TYPE']
    value: str


class QueryTextInputData(BaseValidatorModel):
    text: str


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


class RemoveAssistantAIAgentRequest(BaseValidatorModel):
    aiAgentType: AIAgentTypeType
    assistantId: str


class RemoveKnowledgeBaseTemplateUriRequest(BaseValidatorModel):
    knowledgeBaseId: str


class RuntimeSessionDataValue(BaseValidatorModel):
    stringValue: Optional[str] = None


class SessionSummary(BaseValidatorModel):
    assistantArn: str
    assistantId: str
    sessionArn: str
    sessionId: str


class SeedUrl(BaseValidatorModel):
    url: Optional[str] = None


class SessionIntegrationConfiguration(BaseValidatorModel):
    topicIntegrationArn: Optional[str] = None


class StartContentUploadRequest(BaseValidatorModel):
    contentType: str
    knowledgeBaseId: str
    presignedUrlTimeToLive: Optional[int] = None


class SystemEndpointAttributes(BaseValidatorModel):
    address: Optional[str] = None


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


class WebCrawlerLimits(BaseValidatorModel):
    rateLimit: Optional[int] = None


class UpdateAssistantAIAgentRequest(BaseValidatorModel):
    aiAgentType: AIAgentTypeType
    assistantId: str
    configuration: AIAgentConfigurationData


class AIGuardrailContentPolicyConfigOutput(BaseValidatorModel):
    filtersConfig: List[GuardrailContentFilterConfig]


class AIGuardrailContentPolicyConfig(BaseValidatorModel):
    filtersConfig: List[GuardrailContentFilterConfig]


class AIGuardrailContextualGroundingPolicyConfigOutput(BaseValidatorModel):
    filtersConfig: List[GuardrailContextualGroundingFilterConfig]


class AIGuardrailContextualGroundingPolicyConfig(BaseValidatorModel):
    filtersConfig: List[GuardrailContextualGroundingFilterConfig]


class AIGuardrailSensitiveInformationPolicyConfigOutput(BaseValidatorModel):
    piiEntitiesConfig: Optional[List[GuardrailPiiEntityConfig]] = None
    regexesConfig: Optional[List[GuardrailRegexConfig]] = None


class AIGuardrailSensitiveInformationPolicyConfig(BaseValidatorModel):
    piiEntitiesConfig: Optional[List[GuardrailPiiEntityConfig]] = None
    regexesConfig: Optional[List[GuardrailRegexConfig]] = None


class AIGuardrailVersionSummary(BaseValidatorModel):
    aiGuardrailSummary: Optional[AIGuardrailSummary] = None
    versionNumber: Optional[int] = None


class AIGuardrailTopicPolicyConfigOutput(BaseValidatorModel):
    topicsConfig: List[GuardrailTopicConfigOutput]


class AIGuardrailTopicPolicyConfig(BaseValidatorModel):
    topicsConfig: List[GuardrailTopicConfig]


class AIGuardrailWordPolicyConfigOutput(BaseValidatorModel):
    managedWordListsConfig: Optional[List[GuardrailManagedWordsConfig]] = None
    wordsConfig: Optional[List[GuardrailWordConfig]] = None


class AIGuardrailWordPolicyConfig(BaseValidatorModel):
    managedWordListsConfig: Optional[List[GuardrailManagedWordsConfig]] = None
    wordsConfig: Optional[List[GuardrailWordConfig]] = None


class AIPromptVersionSummary(BaseValidatorModel):
    aiPromptSummary: Optional[AIPromptSummary] = None
    versionNumber: Optional[int] = None


class AIPromptTemplateConfiguration(BaseValidatorModel):
    textFullAIPromptEditTemplateConfiguration: Optional[TextFullAIPromptEditTemplateConfiguration] = None


class ActivateMessageTemplateResponse(BaseValidatorModel):
    messageTemplateArn: str
    messageTemplateId: str
    versionNumber: int
    ResponseMetadata: ResponseMetadata


class DeactivateMessageTemplateResponse(BaseValidatorModel):
    messageTemplateArn: str
    messageTemplateId: str
    versionNumber: int
    ResponseMetadata: ResponseMetadata


class ListAIGuardrailsResponse(BaseValidatorModel):
    aiGuardrailSummaries: List[AIGuardrailSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListAIPromptsResponse(BaseValidatorModel):
    aiPromptSummaries: List[AIPromptSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class SendMessageResponse(BaseValidatorModel):
    nextMessageToken: str
    requestMessageId: str
    ResponseMetadata: ResponseMetadata


class StartContentUploadResponse(BaseValidatorModel):
    headersToInclude: Dict[str, str]
    uploadId: str
    url: str
    urlExpiry: datetime
    ResponseMetadata: ResponseMetadata


class ContentAssociationContents(BaseValidatorModel):
    amazonConnectGuideAssociation: Optional[AmazonConnectGuideAssociationData] = None


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
    aiAgentConfiguration: Optional[Dict[AIAgentTypeType, AIAgentConfigurationData]] = None
    capabilityConfiguration: Optional[AssistantCapabilityConfiguration] = None
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
    aiAgentConfiguration: Optional[Dict[AIAgentTypeType, AIAgentConfigurationData]] = None
    capabilityConfiguration: Optional[AssistantCapabilityConfiguration] = None
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


class BedrockFoundationModelConfigurationForParsing(BaseValidatorModel):
    modelArn: str
    parsingPrompt: Optional[ParsingPrompt] = None


class Configuration(BaseValidatorModel):
    connectConfiguration: Optional[ConnectConfiguration] = None


class GenerativeDataDetailsPaginator(BaseValidatorModel):
    completion: str
    rankingData: RankingData
    references: List[Dict[str, Any]]


class GenerativeDataDetails(BaseValidatorModel):
    completion: str
    rankingData: RankingData
    references: List[Dict[str, Any]]


class CreateContentResponse(BaseValidatorModel):
    content: ContentData
    ResponseMetadata: ResponseMetadata


class GetContentResponse(BaseValidatorModel):
    content: ContentData
    ResponseMetadata: ResponseMetadata


class UpdateContentResponse(BaseValidatorModel):
    content: ContentData
    ResponseMetadata: ResponseMetadata


class ContentFeedbackData(BaseValidatorModel):
    generativeContentFeedbackData: Optional[GenerativeContentFeedbackData] = None


class GetContentSummaryResponse(BaseValidatorModel):
    contentSummary: ContentSummary
    ResponseMetadata: ResponseMetadata


class ListContentsResponse(BaseValidatorModel):
    contentSummaries: List[ContentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class SearchContentResponse(BaseValidatorModel):
    contentSummaries: List[ContentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ConversationContext(BaseValidatorModel):
    selfServiceConversationHistory: List[SelfServiceConversationHistory]


class CreateAIAgentVersionRequest(BaseValidatorModel):
    aiAgentId: str
    assistantId: str
    clientToken: Optional[str] = None
    modifiedTime: Optional[Timestamp] = None


class CreateAIGuardrailVersionRequest(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str
    clientToken: Optional[str] = None
    modifiedTime: Optional[Timestamp] = None


class CreateAIPromptVersionRequest(BaseValidatorModel):
    aiPromptId: str
    assistantId: str
    clientToken: Optional[str] = None
    modifiedTime: Optional[Timestamp] = None


class CreateMessageTemplateAttachmentResponse(BaseValidatorModel):
    attachment: MessageTemplateAttachment
    ResponseMetadata: ResponseMetadata


class DataReference(BaseValidatorModel):
    contentReference: Optional[ContentReference] = None
    generativeReference: Optional[GenerativeReference] = None


class DocumentText(BaseValidatorModel):
    highlights: Optional[List[Highlight]] = None
    text: Optional[str] = None


class EmailMessageTemplateContentBody(BaseValidatorModel):
    html: Optional[MessageTemplateBodyContentProvider] = None
    plainText: Optional[MessageTemplateBodyContentProvider] = None


class SMSMessageTemplateContentBody(BaseValidatorModel):
    plainText: Optional[MessageTemplateBodyContentProvider] = None


class MessageTemplateSearchResultData(BaseValidatorModel):
    channelSubtype: ChannelSubtypeType
    createdTime: datetime
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedBy: str
    lastModifiedTime: datetime
    messageTemplateArn: str
    messageTemplateId: str
    name: str
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationOutput] = None
    isActive: Optional[bool] = None
    language: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    versionNumber: Optional[int] = None


class SearchExpression(BaseValidatorModel):
    filters: List[Filter]

GroupingConfigurationUnion = Union[GroupingConfiguration, GroupingConfigurationOutput]


class HierarchicalChunkingConfigurationOutput(BaseValidatorModel):
    levelConfigurations: List[HierarchicalChunkingLevelConfiguration]
    overlapTokens: int


class HierarchicalChunkingConfiguration(BaseValidatorModel):
    levelConfigurations: List[HierarchicalChunkingLevelConfiguration]
    overlapTokens: int


class ListAIAgentVersionsRequestPaginate(BaseValidatorModel):
    aiAgentId: str
    assistantId: str
    origin: Optional[OriginType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAIAgentsRequestPaginate(BaseValidatorModel):
    assistantId: str
    origin: Optional[OriginType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAIGuardrailVersionsRequestPaginate(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAIGuardrailsRequestPaginate(BaseValidatorModel):
    assistantId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAIPromptVersionsRequestPaginate(BaseValidatorModel):
    aiPromptId: str
    assistantId: str
    origin: Optional[OriginType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAIPromptsRequestPaginate(BaseValidatorModel):
    assistantId: str
    origin: Optional[OriginType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssistantAssociationsRequestPaginate(BaseValidatorModel):
    assistantId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAssistantsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContentAssociationsRequestPaginate(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContentsRequestPaginate(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListImportJobsRequestPaginate(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListKnowledgeBasesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMessageTemplateVersionsRequestPaginate(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMessageTemplatesRequestPaginate(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMessagesRequestPaginate(BaseValidatorModel):
    assistantId: str
    sessionId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQuickResponsesRequestPaginate(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMessageTemplateVersionsResponse(BaseValidatorModel):
    messageTemplateVersionSummaries: List[MessageTemplateVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListMessageTemplatesResponse(BaseValidatorModel):
    messageTemplateSummaries: List[MessageTemplateSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListQuickResponsesResponse(BaseValidatorModel):
    quickResponseSummaries: List[QuickResponseSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MessageData(BaseValidatorModel):
    text: Optional[TextMessage] = None


class MessageTemplateSearchExpression(BaseValidatorModel):
    filters: Optional[List[MessageTemplateFilterField]] = None
    orderOnField: Optional[MessageTemplateOrderField] = None
    queries: Optional[List[MessageTemplateQueryField]] = None


class NotifyRecommendationsReceivedResponse(BaseValidatorModel):
    errors: List[NotifyRecommendationsReceivedError]
    recommendationIds: List[str]
    ResponseMetadata: ResponseMetadata


class OrConditionOutput(BaseValidatorModel):
    andConditions: Optional[List[TagCondition]] = None
    tagCondition: Optional[TagCondition] = None


class OrCondition(BaseValidatorModel):
    andConditions: Optional[List[TagCondition]] = None
    tagCondition: Optional[TagCondition] = None


class QueryCondition(BaseValidatorModel):
    single: Optional[QueryConditionItem] = None


class QueryInputData(BaseValidatorModel):
    intentInputData: Optional[IntentInputData] = None
    queryTextInputData: Optional[QueryTextInputData] = None


class RecommendationTriggerData(BaseValidatorModel):
    query: Optional[QueryRecommendationTriggerData] = None


class QuickResponseContents(BaseValidatorModel):
    markdown: Optional[QuickResponseContentProvider] = None
    plainText: Optional[QuickResponseContentProvider] = None


class QuickResponseSearchExpression(BaseValidatorModel):
    filters: Optional[List[QuickResponseFilterField]] = None
    orderOnField: Optional[QuickResponseOrderField] = None
    queries: Optional[List[QuickResponseQueryField]] = None


class RuntimeSessionData(BaseValidatorModel):
    key: str
    value: RuntimeSessionDataValue


class SearchSessionsResponse(BaseValidatorModel):
    sessionSummaries: List[SessionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UrlConfigurationOutput(BaseValidatorModel):
    seedUrls: Optional[List[SeedUrl]] = None


class UrlConfiguration(BaseValidatorModel):
    seedUrls: Optional[List[SeedUrl]] = None


class SystemAttributes(BaseValidatorModel):
    customerEndpoint: Optional[SystemEndpointAttributes] = None
    name: Optional[str] = None
    systemEndpoint: Optional[SystemEndpointAttributes] = None

AIGuardrailContentPolicyConfigUnion = Union[AIGuardrailContentPolicyConfig, AIGuardrailContentPolicyConfigOutput]

AIGuardrailContextualGroundingPolicyConfigUnion = Union[AIGuardrailContextualGroundingPolicyConfig, AIGuardrailContextualGroundingPolicyConfigOutput]

AIGuardrailSensitiveInformationPolicyConfigUnion = Union[AIGuardrailSensitiveInformationPolicyConfig, AIGuardrailSensitiveInformationPolicyConfigOutput]


class ListAIGuardrailVersionsResponse(BaseValidatorModel):
    aiGuardrailVersionSummaries: List[AIGuardrailVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

AIGuardrailTopicPolicyConfigUnion = Union[AIGuardrailTopicPolicyConfig, AIGuardrailTopicPolicyConfigOutput]


class AIGuardrailData(BaseValidatorModel):
    aiGuardrailArn: str
    aiGuardrailId: str
    assistantArn: str
    assistantId: str
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    name: str
    visibilityStatus: VisibilityStatusType
    contentPolicyConfig: Optional[AIGuardrailContentPolicyConfigOutput] = None
    contextualGroundingPolicyConfig: Optional[AIGuardrailContextualGroundingPolicyConfigOutput] = None
    description: Optional[str] = None
    modifiedTime: Optional[datetime] = None
    sensitiveInformationPolicyConfig: Optional[AIGuardrailSensitiveInformationPolicyConfigOutput] = None
    status: Optional[StatusType] = None
    tags: Optional[Dict[str, str]] = None
    topicPolicyConfig: Optional[AIGuardrailTopicPolicyConfigOutput] = None
    wordPolicyConfig: Optional[AIGuardrailWordPolicyConfigOutput] = None

AIGuardrailWordPolicyConfigUnion = Union[AIGuardrailWordPolicyConfig, AIGuardrailWordPolicyConfigOutput]


class ListAIPromptVersionsResponse(BaseValidatorModel):
    aiPromptVersionSummaries: List[AIPromptVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class AIPromptData(BaseValidatorModel):
    aiPromptArn: str
    aiPromptId: str
    apiFormat: AIPromptAPIFormatType
    assistantArn: str
    assistantId: str
    modelId: str
    name: str
    templateConfiguration: AIPromptTemplateConfiguration
    templateType: Literal['TEXT']
    type: AIPromptTypeType
    visibilityStatus: VisibilityStatusType
    description: Optional[str] = None
    modifiedTime: Optional[datetime] = None
    origin: Optional[OriginType] = None
    status: Optional[StatusType] = None
    tags: Optional[Dict[str, str]] = None


class CreateAIPromptRequest(BaseValidatorModel):
    apiFormat: AIPromptAPIFormatType
    assistantId: str
    modelId: str
    name: str
    templateConfiguration: AIPromptTemplateConfiguration
    templateType: Literal['TEXT']
    type: AIPromptTypeType
    visibilityStatus: VisibilityStatusType
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class UpdateAIPromptRequest(BaseValidatorModel):
    aiPromptId: str
    assistantId: str
    visibilityStatus: VisibilityStatusType
    clientToken: Optional[str] = None
    description: Optional[str] = None
    templateConfiguration: Optional[AIPromptTemplateConfiguration] = None


class ContentAssociationData(BaseValidatorModel):
    associationData: ContentAssociationContents
    associationType: Literal['AMAZON_CONNECT_GUIDE']
    contentArn: str
    contentAssociationArn: str
    contentAssociationId: str
    contentId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    tags: Optional[Dict[str, str]] = None


class ContentAssociationSummary(BaseValidatorModel):
    associationData: ContentAssociationContents
    associationType: Literal['AMAZON_CONNECT_GUIDE']
    contentArn: str
    contentAssociationArn: str
    contentAssociationId: str
    contentId: str
    knowledgeBaseArn: str
    knowledgeBaseId: str
    tags: Optional[Dict[str, str]] = None


class CreateContentAssociationRequest(BaseValidatorModel):
    association: ContentAssociationContents
    associationType: Literal['AMAZON_CONNECT_GUIDE']
    contentId: str
    knowledgeBaseId: str
    clientToken: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


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


class UpdateAssistantAIAgentResponse(BaseValidatorModel):
    assistant: AssistantData
    ResponseMetadata: ResponseMetadata


class ListAssistantsResponse(BaseValidatorModel):
    assistantSummaries: List[AssistantSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ParsingConfiguration(BaseValidatorModel):
    parsingStrategy: Literal['BEDROCK_FOUNDATION_MODEL']
    bedrockFoundationModelConfiguration: Optional[BedrockFoundationModelConfigurationForParsing] = None


class ExternalSourceConfiguration(BaseValidatorModel):
    configuration: Configuration
    source: Literal['AMAZON_CONNECT']


class PutFeedbackRequest(BaseValidatorModel):
    assistantId: str
    contentFeedback: ContentFeedbackData
    targetId: str
    targetType: TargetTypeType


class PutFeedbackResponse(BaseValidatorModel):
    assistantArn: str
    assistantId: str
    contentFeedback: ContentFeedbackData
    targetId: str
    targetType: TargetTypeType
    ResponseMetadata: ResponseMetadata


class Document(BaseValidatorModel):
    contentReference: ContentReference
    excerpt: Optional[DocumentText] = None
    title: Optional[DocumentText] = None


class TextData(BaseValidatorModel):
    excerpt: Optional[DocumentText] = None
    title: Optional[DocumentText] = None


class EmailMessageTemplateContentOutput(BaseValidatorModel):
    body: Optional[EmailMessageTemplateContentBody] = None
    headers: Optional[List[EmailHeader]] = None
    subject: Optional[str] = None


class EmailMessageTemplateContent(BaseValidatorModel):
    body: Optional[EmailMessageTemplateContentBody] = None
    headers: Optional[List[EmailHeader]] = None
    subject: Optional[str] = None


class SMSMessageTemplateContent(BaseValidatorModel):
    body: Optional[SMSMessageTemplateContentBody] = None


class SearchMessageTemplatesResponse(BaseValidatorModel):
    results: List[MessageTemplateSearchResultData]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


class UpdateMessageTemplateMetadataRequest(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationUnion] = None
    name: Optional[str] = None


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


class ChunkingConfigurationOutput(BaseValidatorModel):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: Optional[FixedSizeChunkingConfiguration] = None
    hierarchicalChunkingConfiguration: Optional[HierarchicalChunkingConfigurationOutput] = None
    semanticChunkingConfiguration: Optional[SemanticChunkingConfiguration] = None


class ChunkingConfiguration(BaseValidatorModel):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: Optional[FixedSizeChunkingConfiguration] = None
    hierarchicalChunkingConfiguration: Optional[HierarchicalChunkingConfiguration] = None
    semanticChunkingConfiguration: Optional[SemanticChunkingConfiguration] = None


class MessageInput(BaseValidatorModel):
    value: MessageData


class MessageOutput(BaseValidatorModel):
    messageId: str
    participant: ParticipantType
    timestamp: datetime
    value: MessageData


class SearchMessageTemplatesRequestPaginate(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: MessageTemplateSearchExpression
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchMessageTemplatesRequest(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: MessageTemplateSearchExpression
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TagFilterOutput(BaseValidatorModel):
    andConditions: Optional[List[TagCondition]] = None
    orConditions: Optional[List[OrConditionOutput]] = None
    tagCondition: Optional[TagCondition] = None


class TagFilter(BaseValidatorModel):
    andConditions: Optional[List[TagCondition]] = None
    orConditions: Optional[List[OrCondition]] = None
    tagCondition: Optional[TagCondition] = None


class QueryAssistantRequestPaginate(BaseValidatorModel):
    assistantId: str
    overrideKnowledgeBaseSearchType: Optional[KnowledgeBaseSearchTypeType] = None
    queryCondition: Optional[List[QueryCondition]] = None
    queryInputData: Optional[QueryInputData] = None
    queryText: Optional[str] = None
    sessionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class QueryAssistantRequest(BaseValidatorModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    overrideKnowledgeBaseSearchType: Optional[KnowledgeBaseSearchTypeType] = None
    queryCondition: Optional[List[QueryCondition]] = None
    queryInputData: Optional[QueryInputData] = None
    queryText: Optional[str] = None
    sessionId: Optional[str] = None


class RecommendationTrigger(BaseValidatorModel):
    data: RecommendationTriggerData
    id: str
    recommendationIds: List[str]
    source: RecommendationSourceTypeType
    type: RecommendationTriggerTypeType


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


class UpdateSessionDataRequest(BaseValidatorModel):
    assistantId: str
    data: List[RuntimeSessionData]
    sessionId: str
    namespace: Optional[Literal['Custom']] = None


class UpdateSessionDataResponse(BaseValidatorModel):
    data: List[RuntimeSessionData]
    namespace: Literal['Custom']
    sessionArn: str
    sessionId: str
    ResponseMetadata: ResponseMetadata


class WebCrawlerConfigurationOutput(BaseValidatorModel):
    urlConfiguration: UrlConfigurationOutput
    crawlerLimits: Optional[WebCrawlerLimits] = None
    exclusionFilters: Optional[List[str]] = None
    inclusionFilters: Optional[List[str]] = None
    scope: Optional[WebScopeTypeType] = None


class WebCrawlerConfiguration(BaseValidatorModel):
    urlConfiguration: UrlConfiguration
    crawlerLimits: Optional[WebCrawlerLimits] = None
    exclusionFilters: Optional[List[str]] = None
    inclusionFilters: Optional[List[str]] = None
    scope: Optional[WebScopeTypeType] = None


class MessageTemplateAttributesOutput(BaseValidatorModel):
    agentAttributes: Optional[AgentAttributes] = None
    customAttributes: Optional[Dict[str, str]] = None
    customerProfileAttributes: Optional[CustomerProfileAttributesOutput] = None
    systemAttributes: Optional[SystemAttributes] = None


class MessageTemplateAttributes(BaseValidatorModel):
    agentAttributes: Optional[AgentAttributes] = None
    customAttributes: Optional[Dict[str, str]] = None
    customerProfileAttributes: Optional[CustomerProfileAttributes] = None
    systemAttributes: Optional[SystemAttributes] = None


class CreateAIGuardrailResponse(BaseValidatorModel):
    aiGuardrail: AIGuardrailData
    ResponseMetadata: ResponseMetadata


class CreateAIGuardrailVersionResponse(BaseValidatorModel):
    aiGuardrail: AIGuardrailData
    versionNumber: int
    ResponseMetadata: ResponseMetadata


class GetAIGuardrailResponse(BaseValidatorModel):
    aiGuardrail: AIGuardrailData
    versionNumber: int
    ResponseMetadata: ResponseMetadata


class UpdateAIGuardrailResponse(BaseValidatorModel):
    aiGuardrail: AIGuardrailData
    ResponseMetadata: ResponseMetadata


class CreateAIGuardrailRequest(BaseValidatorModel):
    assistantId: str
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    name: str
    visibilityStatus: VisibilityStatusType
    clientToken: Optional[str] = None
    contentPolicyConfig: Optional[AIGuardrailContentPolicyConfigUnion] = None
    contextualGroundingPolicyConfig: Optional[AIGuardrailContextualGroundingPolicyConfigUnion] = None
    description: Optional[str] = None
    sensitiveInformationPolicyConfig: Optional[AIGuardrailSensitiveInformationPolicyConfigUnion] = None
    tags: Optional[Dict[str, str]] = None
    topicPolicyConfig: Optional[AIGuardrailTopicPolicyConfigUnion] = None
    wordPolicyConfig: Optional[AIGuardrailWordPolicyConfigUnion] = None


class UpdateAIGuardrailRequest(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    visibilityStatus: VisibilityStatusType
    clientToken: Optional[str] = None
    contentPolicyConfig: Optional[AIGuardrailContentPolicyConfigUnion] = None
    contextualGroundingPolicyConfig: Optional[AIGuardrailContextualGroundingPolicyConfigUnion] = None
    description: Optional[str] = None
    sensitiveInformationPolicyConfig: Optional[AIGuardrailSensitiveInformationPolicyConfigUnion] = None
    topicPolicyConfig: Optional[AIGuardrailTopicPolicyConfigUnion] = None
    wordPolicyConfig: Optional[AIGuardrailWordPolicyConfigUnion] = None


class CreateAIPromptResponse(BaseValidatorModel):
    aiPrompt: AIPromptData
    ResponseMetadata: ResponseMetadata


class CreateAIPromptVersionResponse(BaseValidatorModel):
    aiPrompt: AIPromptData
    versionNumber: int
    ResponseMetadata: ResponseMetadata


class GetAIPromptResponse(BaseValidatorModel):
    aiPrompt: AIPromptData
    versionNumber: int
    ResponseMetadata: ResponseMetadata


class UpdateAIPromptResponse(BaseValidatorModel):
    aiPrompt: AIPromptData
    ResponseMetadata: ResponseMetadata


class CreateContentAssociationResponse(BaseValidatorModel):
    contentAssociation: ContentAssociationData
    ResponseMetadata: ResponseMetadata


class GetContentAssociationResponse(BaseValidatorModel):
    contentAssociation: ContentAssociationData
    ResponseMetadata: ResponseMetadata


class ListContentAssociationsResponse(BaseValidatorModel):
    contentAssociationSummaries: List[ContentAssociationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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


class ContentDataDetails(BaseValidatorModel):
    rankingData: RankingData
    textData: TextData


class SourceContentDataDetails(BaseValidatorModel):
    id: str
    rankingData: RankingData
    textData: TextData
    type: Literal['KNOWLEDGE_CONTENT']
    citationSpan: Optional[CitationSpan] = None


class MessageTemplateContentProviderOutput(BaseValidatorModel):
    email: Optional[EmailMessageTemplateContentOutput] = None
    sms: Optional[SMSMessageTemplateContent] = None


class MessageTemplateContentProvider(BaseValidatorModel):
    email: Optional[EmailMessageTemplateContent] = None
    sms: Optional[SMSMessageTemplateContent] = None


class VectorIngestionConfigurationOutput(BaseValidatorModel):
    chunkingConfiguration: Optional[ChunkingConfigurationOutput] = None
    parsingConfiguration: Optional[ParsingConfiguration] = None


class VectorIngestionConfiguration(BaseValidatorModel):
    chunkingConfiguration: Optional[ChunkingConfiguration] = None
    parsingConfiguration: Optional[ParsingConfiguration] = None


class SendMessageRequest(BaseValidatorModel):
    assistantId: str
    message: MessageInput
    sessionId: str
    type: Literal['TEXT']
    clientToken: Optional[str] = None
    conversationContext: Optional[ConversationContext] = None


class GetNextMessageResponse(BaseValidatorModel):
    conversationSessionData: List[RuntimeSessionData]
    conversationState: ConversationState
    nextMessageToken: str
    requestMessageId: str
    response: MessageOutput
    type: Literal['TEXT']
    ResponseMetadata: ResponseMetadata


class ListMessagesResponse(BaseValidatorModel):
    messages: List[MessageOutput]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class KnowledgeBaseAssociationConfigurationDataOutput(BaseValidatorModel):
    contentTagFilter: Optional[TagFilterOutput] = None
    maxResults: Optional[int] = None
    overrideKnowledgeBaseSearchType: Optional[KnowledgeBaseSearchTypeType] = None


class SessionData(BaseValidatorModel):
    name: str
    sessionArn: str
    sessionId: str
    aiAgentConfiguration: Optional[Dict[AIAgentTypeType, AIAgentConfigurationData]] = None
    description: Optional[str] = None
    integrationConfiguration: Optional[SessionIntegrationConfiguration] = None
    tagFilter: Optional[TagFilterOutput] = None
    tags: Optional[Dict[str, str]] = None


class KnowledgeBaseAssociationConfigurationData(BaseValidatorModel):
    contentTagFilter: Optional[TagFilter] = None
    maxResults: Optional[int] = None
    overrideKnowledgeBaseSearchType: Optional[KnowledgeBaseSearchTypeType] = None

TagFilterUnion = Union[TagFilter, TagFilterOutput]


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


class ManagedSourceConfigurationOutput(BaseValidatorModel):
    webCrawlerConfiguration: Optional[WebCrawlerConfigurationOutput] = None


class ManagedSourceConfiguration(BaseValidatorModel):
    webCrawlerConfiguration: Optional[WebCrawlerConfiguration] = None

MessageTemplateAttributesUnion = Union[MessageTemplateAttributes, MessageTemplateAttributesOutput]


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


class DataDetailsPaginator(BaseValidatorModel):
    contentData: Optional[ContentDataDetails] = None
    generativeData: Optional[GenerativeDataDetailsPaginator] = None
    intentDetectedData: Optional[IntentDetectedDataDetails] = None
    sourceContentData: Optional[SourceContentDataDetails] = None


class DataDetails(BaseValidatorModel):
    contentData: Optional[ContentDataDetails] = None
    generativeData: Optional[GenerativeDataDetails] = None
    intentDetectedData: Optional[IntentDetectedDataDetails] = None
    sourceContentData: Optional[SourceContentDataDetails] = None


class ExtendedMessageTemplateData(BaseValidatorModel):
    channelSubtype: ChannelSubtypeType
    content: MessageTemplateContentProviderOutput
    createdTime: datetime
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedBy: str
    lastModifiedTime: datetime
    messageTemplateArn: str
    messageTemplateContentSha256: str
    messageTemplateId: str
    name: str
    attachments: Optional[List[MessageTemplateAttachment]] = None
    attributeTypes: Optional[List[MessageTemplateAttributeTypeType]] = None
    defaultAttributes: Optional[MessageTemplateAttributesOutput] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationOutput] = None
    isActive: Optional[bool] = None
    language: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    versionNumber: Optional[int] = None


class MessageTemplateData(BaseValidatorModel):
    channelSubtype: ChannelSubtypeType
    content: MessageTemplateContentProviderOutput
    createdTime: datetime
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedBy: str
    lastModifiedTime: datetime
    messageTemplateArn: str
    messageTemplateContentSha256: str
    messageTemplateId: str
    name: str
    attributeTypes: Optional[List[MessageTemplateAttributeTypeType]] = None
    defaultAttributes: Optional[MessageTemplateAttributesOutput] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationOutput] = None
    language: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class RenderMessageTemplateResponse(BaseValidatorModel):
    attachments: List[MessageTemplateAttachment]
    attributesNotInterpolated: List[str]
    content: MessageTemplateContentProviderOutput
    ResponseMetadata: ResponseMetadata

MessageTemplateContentProviderUnion = Union[MessageTemplateContentProvider, MessageTemplateContentProviderOutput]

VectorIngestionConfigurationUnion = Union[VectorIngestionConfiguration, VectorIngestionConfigurationOutput]


class AssociationConfigurationDataOutput(BaseValidatorModel):
    knowledgeBaseAssociationConfigurationData: Optional[KnowledgeBaseAssociationConfigurationDataOutput] = None


class CreateSessionResponse(BaseValidatorModel):
    session: SessionData
    ResponseMetadata: ResponseMetadata


class GetSessionResponse(BaseValidatorModel):
    session: SessionData
    ResponseMetadata: ResponseMetadata


class UpdateSessionResponse(BaseValidatorModel):
    session: SessionData
    ResponseMetadata: ResponseMetadata


class AssociationConfigurationData(BaseValidatorModel):
    knowledgeBaseAssociationConfigurationData: Optional[KnowledgeBaseAssociationConfigurationData] = None


class CreateSessionRequest(BaseValidatorModel):
    assistantId: str
    name: str
    aiAgentConfiguration: Optional[Dict[AIAgentTypeType, AIAgentConfigurationData]] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tagFilter: Optional[TagFilterUnion] = None
    tags: Optional[Dict[str, str]] = None


class UpdateSessionRequest(BaseValidatorModel):
    assistantId: str
    sessionId: str
    aiAgentConfiguration: Optional[Dict[AIAgentTypeType, AIAgentConfigurationData]] = None
    description: Optional[str] = None
    tagFilter: Optional[TagFilterUnion] = None


class SourceConfigurationOutput(BaseValidatorModel):
    appIntegrations: Optional[AppIntegrationsConfigurationOutput] = None
    managedSourceConfiguration: Optional[ManagedSourceConfigurationOutput] = None


class SourceConfiguration(BaseValidatorModel):
    appIntegrations: Optional[AppIntegrationsConfiguration] = None
    managedSourceConfiguration: Optional[ManagedSourceConfiguration] = None


class RenderMessageTemplateRequest(BaseValidatorModel):
    attributes: MessageTemplateAttributesUnion
    knowledgeBaseId: str
    messageTemplateId: str


class DataSummaryPaginator(BaseValidatorModel):
    details: DataDetailsPaginator
    reference: DataReference


class DataSummary(BaseValidatorModel):
    details: DataDetails
    reference: DataReference


class CreateMessageTemplateVersionResponse(BaseValidatorModel):
    messageTemplate: ExtendedMessageTemplateData
    ResponseMetadata: ResponseMetadata


class GetMessageTemplateResponse(BaseValidatorModel):
    messageTemplate: ExtendedMessageTemplateData
    ResponseMetadata: ResponseMetadata


class CreateMessageTemplateResponse(BaseValidatorModel):
    messageTemplate: MessageTemplateData
    ResponseMetadata: ResponseMetadata


class UpdateMessageTemplateMetadataResponse(BaseValidatorModel):
    messageTemplate: MessageTemplateData
    ResponseMetadata: ResponseMetadata


class UpdateMessageTemplateResponse(BaseValidatorModel):
    messageTemplate: MessageTemplateData
    ResponseMetadata: ResponseMetadata


class CreateMessageTemplateRequest(BaseValidatorModel):
    channelSubtype: ChannelSubtypeType
    content: MessageTemplateContentProviderUnion
    knowledgeBaseId: str
    name: str
    clientToken: Optional[str] = None
    defaultAttributes: Optional[MessageTemplateAttributesUnion] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationUnion] = None
    language: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class UpdateMessageTemplateRequest(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    content: Optional[MessageTemplateContentProviderUnion] = None
    defaultAttributes: Optional[MessageTemplateAttributesUnion] = None
    language: Optional[str] = None


class AssociationConfigurationOutput(BaseValidatorModel):
    associationConfigurationData: Optional[AssociationConfigurationDataOutput] = None
    associationId: Optional[str] = None
    associationType: Optional[Literal['KNOWLEDGE_BASE']] = None


class AssociationConfiguration(BaseValidatorModel):
    associationConfigurationData: Optional[AssociationConfigurationData] = None
    associationId: Optional[str] = None
    associationType: Optional[Literal['KNOWLEDGE_BASE']] = None


class KnowledgeBaseData(BaseValidatorModel):
    knowledgeBaseArn: str
    knowledgeBaseId: str
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    status: KnowledgeBaseStatusType
    description: Optional[str] = None
    ingestionFailureReasons: Optional[List[str]] = None
    ingestionStatus: Optional[SyncStatusType] = None
    lastContentModificationTime: Optional[datetime] = None
    renderingConfiguration: Optional[RenderingConfiguration] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfiguration] = None
    sourceConfiguration: Optional[SourceConfigurationOutput] = None
    tags: Optional[Dict[str, str]] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationOutput] = None


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
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationOutput] = None

SourceConfigurationUnion = Union[SourceConfiguration, SourceConfigurationOutput]


class ResultDataPaginator(BaseValidatorModel):
    resultId: str
    data: Optional[DataSummaryPaginator] = None
    document: Optional[Document] = None
    relevanceScore: Optional[float] = None
    type: Optional[QueryResultTypeType] = None


class RecommendationData(BaseValidatorModel):
    recommendationId: str
    data: Optional[DataSummary] = None
    document: Optional[Document] = None
    relevanceLevel: Optional[RelevanceLevelType] = None
    relevanceScore: Optional[float] = None
    type: Optional[RecommendationTypeType] = None


class ResultData(BaseValidatorModel):
    resultId: str
    data: Optional[DataSummary] = None
    document: Optional[Document] = None
    relevanceScore: Optional[float] = None
    type: Optional[QueryResultTypeType] = None


class AnswerRecommendationAIAgentConfigurationOutput(BaseValidatorModel):
    answerGenerationAIGuardrailId: Optional[str] = None
    answerGenerationAIPromptId: Optional[str] = None
    associationConfigurations: Optional[List[AssociationConfigurationOutput]] = None
    intentLabelingGenerationAIPromptId: Optional[str] = None
    locale: Optional[str] = None
    queryReformulationAIPromptId: Optional[str] = None


class ManualSearchAIAgentConfigurationOutput(BaseValidatorModel):
    answerGenerationAIGuardrailId: Optional[str] = None
    answerGenerationAIPromptId: Optional[str] = None
    associationConfigurations: Optional[List[AssociationConfigurationOutput]] = None
    locale: Optional[str] = None


class SelfServiceAIAgentConfigurationOutput(BaseValidatorModel):
    associationConfigurations: Optional[List[AssociationConfigurationOutput]] = None
    selfServiceAIGuardrailId: Optional[str] = None
    selfServiceAnswerGenerationAIPromptId: Optional[str] = None
    selfServicePreProcessingAIPromptId: Optional[str] = None


class AnswerRecommendationAIAgentConfiguration(BaseValidatorModel):
    answerGenerationAIGuardrailId: Optional[str] = None
    answerGenerationAIPromptId: Optional[str] = None
    associationConfigurations: Optional[List[AssociationConfiguration]] = None
    intentLabelingGenerationAIPromptId: Optional[str] = None
    locale: Optional[str] = None
    queryReformulationAIPromptId: Optional[str] = None


class ManualSearchAIAgentConfiguration(BaseValidatorModel):
    answerGenerationAIGuardrailId: Optional[str] = None
    answerGenerationAIPromptId: Optional[str] = None
    associationConfigurations: Optional[List[AssociationConfiguration]] = None
    locale: Optional[str] = None


class SelfServiceAIAgentConfiguration(BaseValidatorModel):
    associationConfigurations: Optional[List[AssociationConfiguration]] = None
    selfServiceAIGuardrailId: Optional[str] = None
    selfServiceAnswerGenerationAIPromptId: Optional[str] = None
    selfServicePreProcessingAIPromptId: Optional[str] = None


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
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationUnion] = None


class QueryAssistantResponsePaginator(BaseValidatorModel):
    results: List[ResultDataPaginator]
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


class AIAgentConfigurationOutput(BaseValidatorModel):
    answerRecommendationAIAgentConfiguration: Optional[AnswerRecommendationAIAgentConfigurationOutput] = None
    manualSearchAIAgentConfiguration: Optional[ManualSearchAIAgentConfigurationOutput] = None
    selfServiceAIAgentConfiguration: Optional[SelfServiceAIAgentConfigurationOutput] = None


class AIAgentConfiguration(BaseValidatorModel):
    answerRecommendationAIAgentConfiguration: Optional[AnswerRecommendationAIAgentConfiguration] = None
    manualSearchAIAgentConfiguration: Optional[ManualSearchAIAgentConfiguration] = None
    selfServiceAIAgentConfiguration: Optional[SelfServiceAIAgentConfiguration] = None


class AIAgentData(BaseValidatorModel):
    aiAgentArn: str
    aiAgentId: str
    assistantArn: str
    assistantId: str
    configuration: AIAgentConfigurationOutput
    name: str
    type: AIAgentTypeType
    visibilityStatus: VisibilityStatusType
    description: Optional[str] = None
    modifiedTime: Optional[datetime] = None
    origin: Optional[OriginType] = None
    status: Optional[StatusType] = None
    tags: Optional[Dict[str, str]] = None


class AIAgentSummary(BaseValidatorModel):
    aiAgentArn: str
    aiAgentId: str
    assistantArn: str
    assistantId: str
    name: str
    type: AIAgentTypeType
    visibilityStatus: VisibilityStatusType
    configuration: Optional[AIAgentConfigurationOutput] = None
    description: Optional[str] = None
    modifiedTime: Optional[datetime] = None
    origin: Optional[OriginType] = None
    status: Optional[StatusType] = None
    tags: Optional[Dict[str, str]] = None

AIAgentConfigurationUnion = Union[AIAgentConfiguration, AIAgentConfigurationOutput]


class CreateAIAgentResponse(BaseValidatorModel):
    aiAgent: AIAgentData
    ResponseMetadata: ResponseMetadata


class CreateAIAgentVersionResponse(BaseValidatorModel):
    aiAgent: AIAgentData
    versionNumber: int
    ResponseMetadata: ResponseMetadata


class GetAIAgentResponse(BaseValidatorModel):
    aiAgent: AIAgentData
    versionNumber: int
    ResponseMetadata: ResponseMetadata


class UpdateAIAgentResponse(BaseValidatorModel):
    aiAgent: AIAgentData
    ResponseMetadata: ResponseMetadata


class AIAgentVersionSummary(BaseValidatorModel):
    aiAgentSummary: Optional[AIAgentSummary] = None
    versionNumber: Optional[int] = None


class ListAIAgentsResponse(BaseValidatorModel):
    aiAgentSummaries: List[AIAgentSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateAIAgentRequest(BaseValidatorModel):
    assistantId: str
    configuration: AIAgentConfigurationUnion
    name: str
    type: AIAgentTypeType
    visibilityStatus: VisibilityStatusType
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class UpdateAIAgentRequest(BaseValidatorModel):
    aiAgentId: str
    assistantId: str
    visibilityStatus: VisibilityStatusType
    clientToken: Optional[str] = None
    configuration: Optional[AIAgentConfigurationUnion] = None
    description: Optional[str] = None


class ListAIAgentVersionsResponse(BaseValidatorModel):
    aiAgentVersionSummaries: List[AIAgentVersionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None