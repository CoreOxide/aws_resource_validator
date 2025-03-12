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
from aws_resource_validator.pydantic_models.qconnect_constants import *

class AIAgentConfigurationDataTypeDef(BaseValidatorModel):
    aiAgentId: str


class GuardrailRegexConfigTypeDef(BaseValidatorModel):
    action: GuardrailSensitiveInformationActionType
    name: str
    pattern: str
    description: Optional[str] = None


class AIGuardrailSummaryTypeDef(BaseValidatorModel):
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


class GuardrailWordConfigTypeDef(BaseValidatorModel):
    text: str


class TextFullAIPromptEditTemplateConfigurationTypeDef(BaseValidatorModel):
    text: str


class ActivateMessageTemplateRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    versionNumber: int


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class AgentAttributesTypeDef(BaseValidatorModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None


class AmazonConnectGuideAssociationDataTypeDef(BaseValidatorModel):
    flowId: Optional[str] = None


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


class ParsingPromptTypeDef(BaseValidatorModel):
    parsingPromptText: str


class FixedSizeChunkingConfigurationTypeDef(BaseValidatorModel):
    maxTokens: int
    overlapPercentage: int


class SemanticChunkingConfigurationTypeDef(BaseValidatorModel):
    breakpointPercentileThreshold: int
    bufferSize: int
    maxTokens: int


class CitationSpanTypeDef(BaseValidatorModel):
    beginOffsetInclusive: Optional[int] = None
    endOffsetExclusive: Optional[int] = None


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
    referenceType: Optional[ReferenceTypeType] = None
    sourceURL: Optional[str] = None


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


class SelfServiceConversationHistoryTypeDef(BaseValidatorModel):
    turnNumber: int
    botResponse: Optional[str] = None
    inputTranscript: Optional[str] = None


class ConversationStateTypeDef(BaseValidatorModel):
    status: ConversationStatusType
    reason: Optional[ConversationStatusReasonType] = None


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


class CreateMessageTemplateAttachmentRequestTypeDef(BaseValidatorModel):
    body: str
    contentDisposition: Literal["ATTACHMENT"]
    knowledgeBaseId: str
    messageTemplateId: str
    name: str
    clientToken: Optional[str] = None


class MessageTemplateAttachmentTypeDef(BaseValidatorModel):
    attachmentId: str
    contentDisposition: Literal["ATTACHMENT"]
    name: str
    uploadedTime: datetime
    url: str
    urlExpiry: datetime


class CreateMessageTemplateVersionRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    messageTemplateContentSha256: Optional[str] = None


class QuickResponseDataProviderTypeDef(BaseValidatorModel):
    content: Optional[str] = None


class CustomerProfileAttributesOutputTypeDef(BaseValidatorModel):
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


class CustomerProfileAttributesTypeDef(BaseValidatorModel):
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
    custom: Optional[Mapping[str, str]] = None
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


class IntentDetectedDataDetailsTypeDef(BaseValidatorModel):
    intent: str
    intentId: str


class GenerativeReferenceTypeDef(BaseValidatorModel):
    generationId: Optional[str] = None
    modelId: Optional[str] = None


class DeactivateMessageTemplateRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    versionNumber: int


class DeleteAIAgentRequestTypeDef(BaseValidatorModel):
    aiAgentId: str
    assistantId: str


class DeleteAIAgentVersionRequestTypeDef(BaseValidatorModel):
    aiAgentId: str
    assistantId: str
    versionNumber: int


class DeleteAIGuardrailRequestTypeDef(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str


class DeleteAIGuardrailVersionRequestTypeDef(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str
    versionNumber: int


class DeleteAIPromptRequestTypeDef(BaseValidatorModel):
    aiPromptId: str
    assistantId: str


class DeleteAIPromptVersionRequestTypeDef(BaseValidatorModel):
    aiPromptId: str
    assistantId: str
    versionNumber: int


class DeleteAssistantAssociationRequestTypeDef(BaseValidatorModel):
    assistantAssociationId: str
    assistantId: str


class DeleteAssistantRequestTypeDef(BaseValidatorModel):
    assistantId: str


class DeleteContentAssociationRequestTypeDef(BaseValidatorModel):
    contentAssociationId: str
    contentId: str
    knowledgeBaseId: str


class DeleteContentRequestTypeDef(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str


class DeleteImportJobRequestTypeDef(BaseValidatorModel):
    importJobId: str
    knowledgeBaseId: str


class DeleteKnowledgeBaseRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str


class DeleteMessageTemplateAttachmentRequestTypeDef(BaseValidatorModel):
    attachmentId: str
    knowledgeBaseId: str
    messageTemplateId: str


class DeleteMessageTemplateRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str


class DeleteQuickResponseRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    quickResponseId: str


class HighlightTypeDef(BaseValidatorModel):
    beginOffsetInclusive: Optional[int] = None
    endOffsetExclusive: Optional[int] = None


class EmailHeaderTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    value: Optional[str] = None


class MessageTemplateBodyContentProviderTypeDef(BaseValidatorModel):
    content: Optional[str] = None


class GroupingConfigurationOutputTypeDef(BaseValidatorModel):
    criteria: Optional[str] = None
    values: Optional[List[str]] = None


class GetAIAgentRequestTypeDef(BaseValidatorModel):
    aiAgentId: str
    assistantId: str


class GetAIGuardrailRequestTypeDef(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str


class GetAIPromptRequestTypeDef(BaseValidatorModel):
    aiPromptId: str
    assistantId: str


class GetAssistantAssociationRequestTypeDef(BaseValidatorModel):
    assistantAssociationId: str
    assistantId: str


class GetAssistantRequestTypeDef(BaseValidatorModel):
    assistantId: str


class GetContentAssociationRequestTypeDef(BaseValidatorModel):
    contentAssociationId: str
    contentId: str
    knowledgeBaseId: str


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


class GetMessageTemplateRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str


class GetNextMessageRequestTypeDef(BaseValidatorModel):
    assistantId: str
    nextMessageToken: str
    sessionId: str


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


class GroupingConfigurationTypeDef(BaseValidatorModel):
    criteria: Optional[str] = None
    values: Optional[Sequence[str]] = None


class HierarchicalChunkingLevelConfigurationTypeDef(BaseValidatorModel):
    maxTokens: int


class IntentInputDataTypeDef(BaseValidatorModel):
    intentId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAIAgentVersionsRequestTypeDef(BaseValidatorModel):
    aiAgentId: str
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    origin: Optional[OriginType] = None


class ListAIAgentsRequestTypeDef(BaseValidatorModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    origin: Optional[OriginType] = None


class ListAIGuardrailVersionsRequestTypeDef(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAIGuardrailsRequestTypeDef(BaseValidatorModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAIPromptVersionsRequestTypeDef(BaseValidatorModel):
    aiPromptId: str
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    origin: Optional[OriginType] = None


class ListAIPromptsRequestTypeDef(BaseValidatorModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    origin: Optional[OriginType] = None


class ListAssistantAssociationsRequestTypeDef(BaseValidatorModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListAssistantsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListContentAssociationsRequestTypeDef(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str
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


class ListMessageTemplateVersionsRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MessageTemplateVersionSummaryTypeDef(BaseValidatorModel):
    channelSubtype: ChannelSubtypeType
    isActive: bool
    knowledgeBaseArn: str
    knowledgeBaseId: str
    messageTemplateArn: str
    messageTemplateId: str
    name: str
    versionNumber: int


class ListMessageTemplatesRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class MessageTemplateSummaryTypeDef(BaseValidatorModel):
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


class ListMessagesRequestTypeDef(BaseValidatorModel):
    assistantId: str
    sessionId: str
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


class TextMessageTypeDef(BaseValidatorModel):
    value: Optional[str] = None


class MessageTemplateOrderFieldTypeDef(BaseValidatorModel):
    name: str
    order: Optional[OrderType] = None


class NotifyRecommendationsReceivedErrorTypeDef(BaseValidatorModel):
    message: Optional[str] = None
    recommendationId: Optional[str] = None


class NotifyRecommendationsReceivedRequestTypeDef(BaseValidatorModel):
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


class QueryTextInputDataTypeDef(BaseValidatorModel):
    text: str


class QueryRecommendationTriggerDataTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class QuickResponseContentProviderTypeDef(BaseValidatorModel):
    content: Optional[str] = None


class QuickResponseOrderFieldTypeDef(BaseValidatorModel):
    name: str
    order: Optional[OrderType] = None


class RemoveAssistantAIAgentRequestTypeDef(BaseValidatorModel):
    aiAgentType: AIAgentTypeType
    assistantId: str


class RemoveKnowledgeBaseTemplateUriRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str


class RuntimeSessionDataValueTypeDef(BaseValidatorModel):
    stringValue: Optional[str] = None


class SessionSummaryTypeDef(BaseValidatorModel):
    assistantArn: str
    assistantId: str
    sessionArn: str
    sessionId: str


class SeedUrlTypeDef(BaseValidatorModel):
    url: Optional[str] = None


class SessionIntegrationConfigurationTypeDef(BaseValidatorModel):
    topicIntegrationArn: Optional[str] = None


class StartContentUploadRequestTypeDef(BaseValidatorModel):
    contentType: str
    knowledgeBaseId: str
    presignedUrlTimeToLive: Optional[int] = None


class SystemEndpointAttributesTypeDef(BaseValidatorModel):
    address: Optional[str] = None


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


class WebCrawlerLimitsTypeDef(BaseValidatorModel):
    rateLimit: Optional[int] = None


class UpdateAssistantAIAgentRequestTypeDef(BaseValidatorModel):
    aiAgentType: AIAgentTypeType
    assistantId: str
    configuration: AIAgentConfigurationDataTypeDef


class GuardrailContentFilterConfigTypeDef(BaseValidatorModel):
    pass


class AIGuardrailContentPolicyConfigOutputTypeDef(BaseValidatorModel):
    filtersConfig: List[GuardrailContentFilterConfigTypeDef]


class AIGuardrailContentPolicyConfigTypeDef(BaseValidatorModel):
    filtersConfig: Sequence[GuardrailContentFilterConfigTypeDef]


class GuardrailContextualGroundingFilterConfigTypeDef(BaseValidatorModel):
    pass


class AIGuardrailContextualGroundingPolicyConfigOutputTypeDef(BaseValidatorModel):
    filtersConfig: List[GuardrailContextualGroundingFilterConfigTypeDef]


class AIGuardrailContextualGroundingPolicyConfigTypeDef(BaseValidatorModel):
    filtersConfig: Sequence[GuardrailContextualGroundingFilterConfigTypeDef]


class GuardrailPiiEntityConfigTypeDef(BaseValidatorModel):
    pass


class AIGuardrailSensitiveInformationPolicyConfigOutputTypeDef(BaseValidatorModel):
    piiEntitiesConfig: Optional[List[GuardrailPiiEntityConfigTypeDef]] = None
    regexesConfig: Optional[List[GuardrailRegexConfigTypeDef]] = None


class AIGuardrailSensitiveInformationPolicyConfigTypeDef(BaseValidatorModel):
    piiEntitiesConfig: Optional[Sequence[GuardrailPiiEntityConfigTypeDef]] = None
    regexesConfig: Optional[Sequence[GuardrailRegexConfigTypeDef]] = None


class AIGuardrailVersionSummaryTypeDef(BaseValidatorModel):
    aiGuardrailSummary: Optional[AIGuardrailSummaryTypeDef] = None
    versionNumber: Optional[int] = None


class GuardrailTopicConfigOutputTypeDef(BaseValidatorModel):
    pass


class AIGuardrailTopicPolicyConfigOutputTypeDef(BaseValidatorModel):
    topicsConfig: List[GuardrailTopicConfigOutputTypeDef]


class GuardrailTopicConfigTypeDef(BaseValidatorModel):
    pass


class AIGuardrailTopicPolicyConfigTypeDef(BaseValidatorModel):
    topicsConfig: Sequence[GuardrailTopicConfigTypeDef]


class GuardrailManagedWordsConfigTypeDef(BaseValidatorModel):
    pass


class AIGuardrailWordPolicyConfigOutputTypeDef(BaseValidatorModel):
    managedWordListsConfig: Optional[List[GuardrailManagedWordsConfigTypeDef]] = None
    wordsConfig: Optional[List[GuardrailWordConfigTypeDef]] = None


class AIGuardrailWordPolicyConfigTypeDef(BaseValidatorModel):
    managedWordListsConfig: Optional[Sequence[GuardrailManagedWordsConfigTypeDef]] = None
    wordsConfig: Optional[Sequence[GuardrailWordConfigTypeDef]] = None


class AIPromptSummaryTypeDef(BaseValidatorModel):
    pass


class AIPromptVersionSummaryTypeDef(BaseValidatorModel):
    aiPromptSummary: Optional[AIPromptSummaryTypeDef] = None
    versionNumber: Optional[int] = None


class AIPromptTemplateConfigurationTypeDef(BaseValidatorModel):
    textFullAIPromptEditTemplateConfiguration: Optional[ TextFullAIPromptEditTemplateConfigurationTypeDef ] = None


class ActivateMessageTemplateResponseTypeDef(BaseValidatorModel):
    messageTemplateArn: str
    messageTemplateId: str
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef


class DeactivateMessageTemplateResponseTypeDef(BaseValidatorModel):
    messageTemplateArn: str
    messageTemplateId: str
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef


class ListAIGuardrailsResponseTypeDef(BaseValidatorModel):
    aiGuardrailSummaries: List[AIGuardrailSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListAIPromptsResponseTypeDef(BaseValidatorModel):
    aiPromptSummaries: List[AIPromptSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class SendMessageResponseTypeDef(BaseValidatorModel):
    nextMessageToken: str
    requestMessageId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartContentUploadResponseTypeDef(BaseValidatorModel):
    headersToInclude: Dict[str, str]
    uploadId: str
    url: str
    urlExpiry: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class ContentAssociationContentsTypeDef(BaseValidatorModel):
    amazonConnectGuideAssociation: Optional[AmazonConnectGuideAssociationDataTypeDef] = None


class CreateAssistantAssociationRequestTypeDef(BaseValidatorModel):
    assistantId: str
    association: AssistantAssociationInputDataTypeDef
    associationType: Literal["KNOWLEDGE_BASE"]
    clientToken: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class AssistantAssociationOutputDataTypeDef(BaseValidatorModel):
    knowledgeBaseAssociation: Optional[KnowledgeBaseAssociationDataTypeDef] = None


class BedrockFoundationModelConfigurationForParsingTypeDef(BaseValidatorModel):
    modelArn: str
    parsingPrompt: Optional[ParsingPromptTypeDef] = None


class ConfigurationTypeDef(BaseValidatorModel):
    connectConfiguration: Optional[ConnectConfigurationTypeDef] = None


class GenerativeDataDetailsPaginatorTypeDef(BaseValidatorModel):
    completion: str
    rankingData: RankingDataTypeDef
    references: List[Dict[str, Any]]


class GenerativeDataDetailsTypeDef(BaseValidatorModel):
    completion: str
    rankingData: RankingDataTypeDef
    references: List[Dict[str, Any]]


class CreateContentResponseTypeDef(BaseValidatorModel):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetContentResponseTypeDef(BaseValidatorModel):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateContentResponseTypeDef(BaseValidatorModel):
    content: ContentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ContentFeedbackDataTypeDef(BaseValidatorModel):
    generativeContentFeedbackData: Optional[GenerativeContentFeedbackDataTypeDef] = None


class GetContentSummaryResponseTypeDef(BaseValidatorModel):
    contentSummary: ContentSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListContentsResponseTypeDef(BaseValidatorModel):
    contentSummaries: List[ContentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class SearchContentResponseTypeDef(BaseValidatorModel):
    contentSummaries: List[ContentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ConversationContextTypeDef(BaseValidatorModel):
    selfServiceConversationHistory: Sequence[SelfServiceConversationHistoryTypeDef]


class TimestampTypeDef(BaseValidatorModel):
    pass


class CreateAIAgentVersionRequestTypeDef(BaseValidatorModel):
    aiAgentId: str
    assistantId: str
    clientToken: Optional[str] = None
    modifiedTime: Optional[TimestampTypeDef] = None


class CreateAIGuardrailVersionRequestTypeDef(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str
    clientToken: Optional[str] = None
    modifiedTime: Optional[TimestampTypeDef] = None


class CreateAIPromptVersionRequestTypeDef(BaseValidatorModel):
    aiPromptId: str
    assistantId: str
    clientToken: Optional[str] = None
    modifiedTime: Optional[TimestampTypeDef] = None


class CreateMessageTemplateAttachmentResponseTypeDef(BaseValidatorModel):
    attachment: MessageTemplateAttachmentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DataReferenceTypeDef(BaseValidatorModel):
    contentReference: Optional[ContentReferenceTypeDef] = None
    generativeReference: Optional[GenerativeReferenceTypeDef] = None


class DocumentTextTypeDef(BaseValidatorModel):
    highlights: Optional[List[HighlightTypeDef]] = None
    text: Optional[str] = None


class EmailMessageTemplateContentBodyTypeDef(BaseValidatorModel):
    html: Optional[MessageTemplateBodyContentProviderTypeDef] = None
    plainText: Optional[MessageTemplateBodyContentProviderTypeDef] = None


class SMSMessageTemplateContentBodyTypeDef(BaseValidatorModel):
    plainText: Optional[MessageTemplateBodyContentProviderTypeDef] = None


class MessageTemplateSearchResultDataTypeDef(BaseValidatorModel):
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
    groupingConfiguration: Optional[GroupingConfigurationOutputTypeDef] = None
    isActive: Optional[bool] = None
    language: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    versionNumber: Optional[int] = None


class FilterTypeDef(BaseValidatorModel):
    pass


class SearchExpressionTypeDef(BaseValidatorModel):
    filters: Sequence[FilterTypeDef]


class HierarchicalChunkingConfigurationOutputTypeDef(BaseValidatorModel):
    levelConfigurations: List[HierarchicalChunkingLevelConfigurationTypeDef]
    overlapTokens: int


class HierarchicalChunkingConfigurationTypeDef(BaseValidatorModel):
    levelConfigurations: Sequence[HierarchicalChunkingLevelConfigurationTypeDef]
    overlapTokens: int


class ListAIAgentVersionsRequestPaginateTypeDef(BaseValidatorModel):
    aiAgentId: str
    assistantId: str
    origin: Optional[OriginType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAIAgentsRequestPaginateTypeDef(BaseValidatorModel):
    assistantId: str
    origin: Optional[OriginType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAIGuardrailVersionsRequestPaginateTypeDef(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAIGuardrailsRequestPaginateTypeDef(BaseValidatorModel):
    assistantId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAIPromptVersionsRequestPaginateTypeDef(BaseValidatorModel):
    aiPromptId: str
    assistantId: str
    origin: Optional[OriginType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAIPromptsRequestPaginateTypeDef(BaseValidatorModel):
    assistantId: str
    origin: Optional[OriginType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssistantAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    assistantId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAssistantsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListContentAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    contentId: str
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListContentsRequestPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListImportJobsRequestPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListKnowledgeBasesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMessageTemplateVersionsRequestPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMessageTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMessagesRequestPaginateTypeDef(BaseValidatorModel):
    assistantId: str
    sessionId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQuickResponsesRequestPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMessageTemplateVersionsResponseTypeDef(BaseValidatorModel):
    messageTemplateVersionSummaries: List[MessageTemplateVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListMessageTemplatesResponseTypeDef(BaseValidatorModel):
    messageTemplateSummaries: List[MessageTemplateSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListQuickResponsesResponseTypeDef(BaseValidatorModel):
    quickResponseSummaries: List[QuickResponseSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MessageDataTypeDef(BaseValidatorModel):
    text: Optional[TextMessageTypeDef] = None


class MessageTemplateFilterFieldTypeDef(BaseValidatorModel):
    pass


class MessageTemplateQueryFieldTypeDef(BaseValidatorModel):
    pass


class MessageTemplateSearchExpressionTypeDef(BaseValidatorModel):
    filters: Optional[Sequence[MessageTemplateFilterFieldTypeDef]] = None
    orderOnField: Optional[MessageTemplateOrderFieldTypeDef] = None
    queries: Optional[Sequence[MessageTemplateQueryFieldTypeDef]] = None


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


class QueryInputDataTypeDef(BaseValidatorModel):
    intentInputData: Optional[IntentInputDataTypeDef] = None
    queryTextInputData: Optional[QueryTextInputDataTypeDef] = None


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


class RuntimeSessionDataTypeDef(BaseValidatorModel):
    key: str
    value: RuntimeSessionDataValueTypeDef


class SearchSessionsResponseTypeDef(BaseValidatorModel):
    sessionSummaries: List[SessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UrlConfigurationOutputTypeDef(BaseValidatorModel):
    seedUrls: Optional[List[SeedUrlTypeDef]] = None


class UrlConfigurationTypeDef(BaseValidatorModel):
    seedUrls: Optional[Sequence[SeedUrlTypeDef]] = None


class SystemAttributesTypeDef(BaseValidatorModel):
    customerEndpoint: Optional[SystemEndpointAttributesTypeDef] = None
    name: Optional[str] = None
    systemEndpoint: Optional[SystemEndpointAttributesTypeDef] = None


class ListAIGuardrailVersionsResponseTypeDef(BaseValidatorModel):
    aiGuardrailVersionSummaries: List[AIGuardrailVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AIGuardrailDataTypeDef(BaseValidatorModel):
    aiGuardrailArn: str
    aiGuardrailId: str
    assistantArn: str
    assistantId: str
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    name: str
    visibilityStatus: VisibilityStatusType
    contentPolicyConfig: Optional[AIGuardrailContentPolicyConfigOutputTypeDef] = None
    contextualGroundingPolicyConfig: Optional[ AIGuardrailContextualGroundingPolicyConfigOutputTypeDef ] = None
    description: Optional[str] = None
    modifiedTime: Optional[datetime] = None
    sensitiveInformationPolicyConfig: Optional[ AIGuardrailSensitiveInformationPolicyConfigOutputTypeDef ] = None
    status: Optional[StatusType] = None
    tags: Optional[Dict[str, str]] = None
    topicPolicyConfig: Optional[AIGuardrailTopicPolicyConfigOutputTypeDef] = None
    wordPolicyConfig: Optional[AIGuardrailWordPolicyConfigOutputTypeDef] = None


class ListAIPromptVersionsResponseTypeDef(BaseValidatorModel):
    aiPromptVersionSummaries: List[AIPromptVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UpdateAIPromptRequestTypeDef(BaseValidatorModel):
    aiPromptId: str
    assistantId: str
    visibilityStatus: VisibilityStatusType
    clientToken: Optional[str] = None
    description: Optional[str] = None
    templateConfiguration: Optional[AIPromptTemplateConfigurationTypeDef] = None


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


class CreateContentAssociationRequestTypeDef(BaseValidatorModel):
    association: ContentAssociationContentsTypeDef
    associationType: Literal["AMAZON_CONNECT_GUIDE"]
    contentId: str
    knowledgeBaseId: str
    clientToken: Optional[str] = None
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


class AssistantDataTypeDef(BaseValidatorModel):
    pass


class CreateAssistantResponseTypeDef(BaseValidatorModel):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetAssistantResponseTypeDef(BaseValidatorModel):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAssistantAIAgentResponseTypeDef(BaseValidatorModel):
    assistant: AssistantDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssistantSummaryTypeDef(BaseValidatorModel):
    pass


class ListAssistantsResponseTypeDef(BaseValidatorModel):
    assistantSummaries: List[AssistantSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ParsingConfigurationTypeDef(BaseValidatorModel):
    parsingStrategy: Literal["BEDROCK_FOUNDATION_MODEL"]
    bedrockFoundationModelConfiguration: Optional[ BedrockFoundationModelConfigurationForParsingTypeDef ] = None


class ExternalSourceConfigurationTypeDef(BaseValidatorModel):
    configuration: ConfigurationTypeDef
    source: Literal["AMAZON_CONNECT"]


class PutFeedbackRequestTypeDef(BaseValidatorModel):
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


class DocumentTypeDef(BaseValidatorModel):
    contentReference: ContentReferenceTypeDef
    excerpt: Optional[DocumentTextTypeDef] = None
    title: Optional[DocumentTextTypeDef] = None


class TextDataTypeDef(BaseValidatorModel):
    excerpt: Optional[DocumentTextTypeDef] = None
    title: Optional[DocumentTextTypeDef] = None


class EmailMessageTemplateContentOutputTypeDef(BaseValidatorModel):
    body: Optional[EmailMessageTemplateContentBodyTypeDef] = None
    headers: Optional[List[EmailHeaderTypeDef]] = None
    subject: Optional[str] = None


class EmailMessageTemplateContentTypeDef(BaseValidatorModel):
    body: Optional[EmailMessageTemplateContentBodyTypeDef] = None
    headers: Optional[Sequence[EmailHeaderTypeDef]] = None
    subject: Optional[str] = None


class SMSMessageTemplateContentTypeDef(BaseValidatorModel):
    body: Optional[SMSMessageTemplateContentBodyTypeDef] = None


class SearchMessageTemplatesResponseTypeDef(BaseValidatorModel):
    results: List[MessageTemplateSearchResultDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class UpdateMessageTemplateMetadataRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationUnionTypeDef] = None
    name: Optional[str] = None


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


class ChunkingConfigurationOutputTypeDef(BaseValidatorModel):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: Optional[FixedSizeChunkingConfigurationTypeDef] = None
    hierarchicalChunkingConfiguration: Optional[HierarchicalChunkingConfigurationOutputTypeDef] = None
    semanticChunkingConfiguration: Optional[SemanticChunkingConfigurationTypeDef] = None


class ChunkingConfigurationTypeDef(BaseValidatorModel):
    chunkingStrategy: ChunkingStrategyType
    fixedSizeChunkingConfiguration: Optional[FixedSizeChunkingConfigurationTypeDef] = None
    hierarchicalChunkingConfiguration: Optional[HierarchicalChunkingConfigurationTypeDef] = None
    semanticChunkingConfiguration: Optional[SemanticChunkingConfigurationTypeDef] = None


class MessageInputTypeDef(BaseValidatorModel):
    value: MessageDataTypeDef


class MessageOutputTypeDef(BaseValidatorModel):
    messageId: str
    participant: ParticipantType
    timestamp: datetime
    value: MessageDataTypeDef


class SearchMessageTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: MessageTemplateSearchExpressionTypeDef
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchMessageTemplatesRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    searchExpression: MessageTemplateSearchExpressionTypeDef
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class TagFilterOutputTypeDef(BaseValidatorModel):
    andConditions: Optional[List[TagConditionTypeDef]] = None
    orConditions: Optional[List[OrConditionOutputTypeDef]] = None
    tagCondition: Optional[TagConditionTypeDef] = None


class TagFilterTypeDef(BaseValidatorModel):
    andConditions: Optional[Sequence[TagConditionTypeDef]] = None
    orConditions: Optional[Sequence[OrConditionTypeDef]] = None
    tagCondition: Optional[TagConditionTypeDef] = None


class QueryAssistantRequestPaginateTypeDef(BaseValidatorModel):
    assistantId: str
    overrideKnowledgeBaseSearchType: Optional[KnowledgeBaseSearchTypeType] = None
    queryCondition: Optional[Sequence[QueryConditionTypeDef]] = None
    queryInputData: Optional[QueryInputDataTypeDef] = None
    queryText: Optional[str] = None
    sessionId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class QueryAssistantRequestTypeDef(BaseValidatorModel):
    assistantId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None
    overrideKnowledgeBaseSearchType: Optional[KnowledgeBaseSearchTypeType] = None
    queryCondition: Optional[Sequence[QueryConditionTypeDef]] = None
    queryInputData: Optional[QueryInputDataTypeDef] = None
    queryText: Optional[str] = None
    sessionId: Optional[str] = None


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


class UpdateSessionDataRequestTypeDef(BaseValidatorModel):
    assistantId: str
    data: Sequence[RuntimeSessionDataTypeDef]
    sessionId: str
    namespace: Optional[Literal["Custom"]] = None


class UpdateSessionDataResponseTypeDef(BaseValidatorModel):
    data: List[RuntimeSessionDataTypeDef]
    namespace: Literal["Custom"]
    sessionArn: str
    sessionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class WebCrawlerConfigurationOutputTypeDef(BaseValidatorModel):
    urlConfiguration: UrlConfigurationOutputTypeDef
    crawlerLimits: Optional[WebCrawlerLimitsTypeDef] = None
    exclusionFilters: Optional[List[str]] = None
    inclusionFilters: Optional[List[str]] = None
    scope: Optional[WebScopeTypeType] = None


class WebCrawlerConfigurationTypeDef(BaseValidatorModel):
    urlConfiguration: UrlConfigurationTypeDef
    crawlerLimits: Optional[WebCrawlerLimitsTypeDef] = None
    exclusionFilters: Optional[Sequence[str]] = None
    inclusionFilters: Optional[Sequence[str]] = None
    scope: Optional[WebScopeTypeType] = None


class MessageTemplateAttributesOutputTypeDef(BaseValidatorModel):
    agentAttributes: Optional[AgentAttributesTypeDef] = None
    customAttributes: Optional[Dict[str, str]] = None
    customerProfileAttributes: Optional[CustomerProfileAttributesOutputTypeDef] = None
    systemAttributes: Optional[SystemAttributesTypeDef] = None


class MessageTemplateAttributesTypeDef(BaseValidatorModel):
    agentAttributes: Optional[AgentAttributesTypeDef] = None
    customAttributes: Optional[Mapping[str, str]] = None
    customerProfileAttributes: Optional[CustomerProfileAttributesTypeDef] = None
    systemAttributes: Optional[SystemAttributesTypeDef] = None


class CreateAIGuardrailResponseTypeDef(BaseValidatorModel):
    aiGuardrail: AIGuardrailDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAIGuardrailVersionResponseTypeDef(BaseValidatorModel):
    aiGuardrail: AIGuardrailDataTypeDef
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetAIGuardrailResponseTypeDef(BaseValidatorModel):
    aiGuardrail: AIGuardrailDataTypeDef
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAIGuardrailResponseTypeDef(BaseValidatorModel):
    aiGuardrail: AIGuardrailDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AIGuardrailWordPolicyConfigUnionTypeDef(BaseValidatorModel):
    pass


class AIGuardrailSensitiveInformationPolicyConfigUnionTypeDef(BaseValidatorModel):
    pass


class AIGuardrailTopicPolicyConfigUnionTypeDef(BaseValidatorModel):
    pass


class AIGuardrailContextualGroundingPolicyConfigUnionTypeDef(BaseValidatorModel):
    pass


class AIGuardrailContentPolicyConfigUnionTypeDef(BaseValidatorModel):
    pass


class CreateAIGuardrailRequestTypeDef(BaseValidatorModel):
    assistantId: str
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    name: str
    visibilityStatus: VisibilityStatusType
    clientToken: Optional[str] = None
    contentPolicyConfig: Optional[AIGuardrailContentPolicyConfigUnionTypeDef] = None
    contextualGroundingPolicyConfig: Optional[ AIGuardrailContextualGroundingPolicyConfigUnionTypeDef ] = None
    description: Optional[str] = None
    sensitiveInformationPolicyConfig: Optional[ AIGuardrailSensitiveInformationPolicyConfigUnionTypeDef ] = None
    tags: Optional[Mapping[str, str]] = None
    topicPolicyConfig: Optional[AIGuardrailTopicPolicyConfigUnionTypeDef] = None
    wordPolicyConfig: Optional[AIGuardrailWordPolicyConfigUnionTypeDef] = None


class UpdateAIGuardrailRequestTypeDef(BaseValidatorModel):
    aiGuardrailId: str
    assistantId: str
    blockedInputMessaging: str
    blockedOutputsMessaging: str
    visibilityStatus: VisibilityStatusType
    clientToken: Optional[str] = None
    contentPolicyConfig: Optional[AIGuardrailContentPolicyConfigUnionTypeDef] = None
    contextualGroundingPolicyConfig: Optional[ AIGuardrailContextualGroundingPolicyConfigUnionTypeDef ] = None
    description: Optional[str] = None
    sensitiveInformationPolicyConfig: Optional[ AIGuardrailSensitiveInformationPolicyConfigUnionTypeDef ] = None
    topicPolicyConfig: Optional[AIGuardrailTopicPolicyConfigUnionTypeDef] = None
    wordPolicyConfig: Optional[AIGuardrailWordPolicyConfigUnionTypeDef] = None


class AIPromptDataTypeDef(BaseValidatorModel):
    pass


class CreateAIPromptResponseTypeDef(BaseValidatorModel):
    aiPrompt: AIPromptDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAIPromptVersionResponseTypeDef(BaseValidatorModel):
    aiPrompt: AIPromptDataTypeDef
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetAIPromptResponseTypeDef(BaseValidatorModel):
    aiPrompt: AIPromptDataTypeDef
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAIPromptResponseTypeDef(BaseValidatorModel):
    aiPrompt: AIPromptDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateContentAssociationResponseTypeDef(BaseValidatorModel):
    contentAssociation: ContentAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetContentAssociationResponseTypeDef(BaseValidatorModel):
    contentAssociation: ContentAssociationDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListContentAssociationsResponseTypeDef(BaseValidatorModel):
    contentAssociationSummaries: List[ContentAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class ContentDataDetailsTypeDef(BaseValidatorModel):
    rankingData: RankingDataTypeDef
    textData: TextDataTypeDef


class MessageTemplateContentProviderOutputTypeDef(BaseValidatorModel):
    email: Optional[EmailMessageTemplateContentOutputTypeDef] = None
    sms: Optional[SMSMessageTemplateContentTypeDef] = None


class MessageTemplateContentProviderTypeDef(BaseValidatorModel):
    email: Optional[EmailMessageTemplateContentTypeDef] = None
    sms: Optional[SMSMessageTemplateContentTypeDef] = None


class VectorIngestionConfigurationOutputTypeDef(BaseValidatorModel):
    chunkingConfiguration: Optional[ChunkingConfigurationOutputTypeDef] = None
    parsingConfiguration: Optional[ParsingConfigurationTypeDef] = None


class VectorIngestionConfigurationTypeDef(BaseValidatorModel):
    chunkingConfiguration: Optional[ChunkingConfigurationTypeDef] = None
    parsingConfiguration: Optional[ParsingConfigurationTypeDef] = None


class ListMessagesResponseTypeDef(BaseValidatorModel):
    messages: List[MessageOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class KnowledgeBaseAssociationConfigurationDataOutputTypeDef(BaseValidatorModel):
    contentTagFilter: Optional[TagFilterOutputTypeDef] = None
    maxResults: Optional[int] = None
    overrideKnowledgeBaseSearchType: Optional[KnowledgeBaseSearchTypeType] = None


class SessionDataTypeDef(BaseValidatorModel):
    name: str
    sessionArn: str
    sessionId: str
    aiAgentConfiguration: Optional[Dict[AIAgentTypeType, AIAgentConfigurationDataTypeDef]] = None
    description: Optional[str] = None
    integrationConfiguration: Optional[SessionIntegrationConfigurationTypeDef] = None
    tagFilter: Optional[TagFilterOutputTypeDef] = None
    tags: Optional[Dict[str, str]] = None


class KnowledgeBaseAssociationConfigurationDataTypeDef(BaseValidatorModel):
    contentTagFilter: Optional[TagFilterTypeDef] = None
    maxResults: Optional[int] = None
    overrideKnowledgeBaseSearchType: Optional[KnowledgeBaseSearchTypeType] = None


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


class ManagedSourceConfigurationOutputTypeDef(BaseValidatorModel):
    webCrawlerConfiguration: Optional[WebCrawlerConfigurationOutputTypeDef] = None


class ManagedSourceConfigurationTypeDef(BaseValidatorModel):
    webCrawlerConfiguration: Optional[WebCrawlerConfigurationTypeDef] = None


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


class SourceContentDataDetailsTypeDef(BaseValidatorModel):
    pass


class DataDetailsPaginatorTypeDef(BaseValidatorModel):
    contentData: Optional[ContentDataDetailsTypeDef] = None
    generativeData: Optional[GenerativeDataDetailsPaginatorTypeDef] = None
    intentDetectedData: Optional[IntentDetectedDataDetailsTypeDef] = None
    sourceContentData: Optional[SourceContentDataDetailsTypeDef] = None


class DataDetailsTypeDef(BaseValidatorModel):
    contentData: Optional[ContentDataDetailsTypeDef] = None
    generativeData: Optional[GenerativeDataDetailsTypeDef] = None
    intentDetectedData: Optional[IntentDetectedDataDetailsTypeDef] = None
    sourceContentData: Optional[SourceContentDataDetailsTypeDef] = None


class ExtendedMessageTemplateDataTypeDef(BaseValidatorModel):
    channelSubtype: ChannelSubtypeType
    content: MessageTemplateContentProviderOutputTypeDef
    createdTime: datetime
    knowledgeBaseArn: str
    knowledgeBaseId: str
    lastModifiedBy: str
    lastModifiedTime: datetime
    messageTemplateArn: str
    messageTemplateContentSha256: str
    messageTemplateId: str
    name: str
    attachments: Optional[List[MessageTemplateAttachmentTypeDef]] = None
    attributeTypes: Optional[List[MessageTemplateAttributeTypeType]] = None
    defaultAttributes: Optional[MessageTemplateAttributesOutputTypeDef] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationOutputTypeDef] = None
    isActive: Optional[bool] = None
    language: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    versionNumber: Optional[int] = None


class MessageTemplateDataTypeDef(BaseValidatorModel):
    channelSubtype: ChannelSubtypeType
    content: MessageTemplateContentProviderOutputTypeDef
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
    defaultAttributes: Optional[MessageTemplateAttributesOutputTypeDef] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationOutputTypeDef] = None
    language: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class RenderMessageTemplateResponseTypeDef(BaseValidatorModel):
    attachments: List[MessageTemplateAttachmentTypeDef]
    attributesNotInterpolated: List[str]
    content: MessageTemplateContentProviderOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssociationConfigurationDataOutputTypeDef(BaseValidatorModel):
    knowledgeBaseAssociationConfigurationData: Optional[ KnowledgeBaseAssociationConfigurationDataOutputTypeDef ] = None


class CreateSessionResponseTypeDef(BaseValidatorModel):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetSessionResponseTypeDef(BaseValidatorModel):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSessionResponseTypeDef(BaseValidatorModel):
    session: SessionDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AssociationConfigurationDataTypeDef(BaseValidatorModel):
    knowledgeBaseAssociationConfigurationData: Optional[ KnowledgeBaseAssociationConfigurationDataTypeDef ] = None


class TagFilterUnionTypeDef(BaseValidatorModel):
    pass


class CreateSessionRequestTypeDef(BaseValidatorModel):
    assistantId: str
    name: str
    aiAgentConfiguration: Optional[Mapping[AIAgentTypeType, AIAgentConfigurationDataTypeDef]] = None
    clientToken: Optional[str] = None
    description: Optional[str] = None
    tagFilter: Optional[TagFilterUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateSessionRequestTypeDef(BaseValidatorModel):
    assistantId: str
    sessionId: str
    aiAgentConfiguration: Optional[Mapping[AIAgentTypeType, AIAgentConfigurationDataTypeDef]] = None
    description: Optional[str] = None
    tagFilter: Optional[TagFilterUnionTypeDef] = None


class SourceConfigurationOutputTypeDef(BaseValidatorModel):
    appIntegrations: Optional[AppIntegrationsConfigurationOutputTypeDef] = None
    managedSourceConfiguration: Optional[ManagedSourceConfigurationOutputTypeDef] = None


class SourceConfigurationTypeDef(BaseValidatorModel):
    appIntegrations: Optional[AppIntegrationsConfigurationTypeDef] = None
    managedSourceConfiguration: Optional[ManagedSourceConfigurationTypeDef] = None


class MessageTemplateAttributesUnionTypeDef(BaseValidatorModel):
    pass


class RenderMessageTemplateRequestTypeDef(BaseValidatorModel):
    attributes: MessageTemplateAttributesUnionTypeDef
    knowledgeBaseId: str
    messageTemplateId: str


class DataSummaryPaginatorTypeDef(BaseValidatorModel):
    details: DataDetailsPaginatorTypeDef
    reference: DataReferenceTypeDef


class DataSummaryTypeDef(BaseValidatorModel):
    details: DataDetailsTypeDef
    reference: DataReferenceTypeDef


class CreateMessageTemplateVersionResponseTypeDef(BaseValidatorModel):
    messageTemplate: ExtendedMessageTemplateDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetMessageTemplateResponseTypeDef(BaseValidatorModel):
    messageTemplate: ExtendedMessageTemplateDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMessageTemplateResponseTypeDef(BaseValidatorModel):
    messageTemplate: MessageTemplateDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMessageTemplateMetadataResponseTypeDef(BaseValidatorModel):
    messageTemplate: MessageTemplateDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateMessageTemplateResponseTypeDef(BaseValidatorModel):
    messageTemplate: MessageTemplateDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class MessageTemplateContentProviderUnionTypeDef(BaseValidatorModel):
    pass


class CreateMessageTemplateRequestTypeDef(BaseValidatorModel):
    channelSubtype: ChannelSubtypeType
    content: MessageTemplateContentProviderUnionTypeDef
    knowledgeBaseId: str
    name: str
    clientToken: Optional[str] = None
    defaultAttributes: Optional[MessageTemplateAttributesUnionTypeDef] = None
    description: Optional[str] = None
    groupingConfiguration: Optional[GroupingConfigurationUnionTypeDef] = None
    language: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class UpdateMessageTemplateRequestTypeDef(BaseValidatorModel):
    knowledgeBaseId: str
    messageTemplateId: str
    content: Optional[MessageTemplateContentProviderUnionTypeDef] = None
    defaultAttributes: Optional[MessageTemplateAttributesUnionTypeDef] = None
    language: Optional[str] = None


class AssociationConfigurationOutputTypeDef(BaseValidatorModel):
    associationConfigurationData: Optional[AssociationConfigurationDataOutputTypeDef] = None
    associationId: Optional[str] = None
    associationType: Optional[Literal["KNOWLEDGE_BASE"]] = None


class AssociationConfigurationTypeDef(BaseValidatorModel):
    associationConfigurationData: Optional[AssociationConfigurationDataTypeDef] = None
    associationId: Optional[str] = None
    associationType: Optional[Literal["KNOWLEDGE_BASE"]] = None


class KnowledgeBaseDataTypeDef(BaseValidatorModel):
    knowledgeBaseArn: str
    knowledgeBaseId: str
    knowledgeBaseType: KnowledgeBaseTypeType
    name: str
    status: KnowledgeBaseStatusType
    description: Optional[str] = None
    ingestionFailureReasons: Optional[List[str]] = None
    ingestionStatus: Optional[SyncStatusType] = None
    lastContentModificationTime: Optional[datetime] = None
    renderingConfiguration: Optional[RenderingConfigurationTypeDef] = None
    serverSideEncryptionConfiguration: Optional[ServerSideEncryptionConfigurationTypeDef] = None
    sourceConfiguration: Optional[SourceConfigurationOutputTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationOutputTypeDef] = None


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
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationOutputTypeDef] = None


class AnswerRecommendationAIAgentConfigurationOutputTypeDef(BaseValidatorModel):
    answerGenerationAIGuardrailId: Optional[str] = None
    answerGenerationAIPromptId: Optional[str] = None
    associationConfigurations: Optional[List[AssociationConfigurationOutputTypeDef]] = None
    intentLabelingGenerationAIPromptId: Optional[str] = None
    locale: Optional[str] = None
    queryReformulationAIPromptId: Optional[str] = None


class ManualSearchAIAgentConfigurationOutputTypeDef(BaseValidatorModel):
    answerGenerationAIGuardrailId: Optional[str] = None
    answerGenerationAIPromptId: Optional[str] = None
    associationConfigurations: Optional[List[AssociationConfigurationOutputTypeDef]] = None
    locale: Optional[str] = None


class SelfServiceAIAgentConfigurationOutputTypeDef(BaseValidatorModel):
    associationConfigurations: Optional[List[AssociationConfigurationOutputTypeDef]] = None
    selfServiceAIGuardrailId: Optional[str] = None
    selfServiceAnswerGenerationAIPromptId: Optional[str] = None
    selfServicePreProcessingAIPromptId: Optional[str] = None


class AnswerRecommendationAIAgentConfigurationTypeDef(BaseValidatorModel):
    answerGenerationAIGuardrailId: Optional[str] = None
    answerGenerationAIPromptId: Optional[str] = None
    associationConfigurations: Optional[Sequence[AssociationConfigurationTypeDef]] = None
    intentLabelingGenerationAIPromptId: Optional[str] = None
    locale: Optional[str] = None
    queryReformulationAIPromptId: Optional[str] = None


class ManualSearchAIAgentConfigurationTypeDef(BaseValidatorModel):
    answerGenerationAIGuardrailId: Optional[str] = None
    answerGenerationAIPromptId: Optional[str] = None
    associationConfigurations: Optional[Sequence[AssociationConfigurationTypeDef]] = None
    locale: Optional[str] = None


class SelfServiceAIAgentConfigurationTypeDef(BaseValidatorModel):
    associationConfigurations: Optional[Sequence[AssociationConfigurationTypeDef]] = None
    selfServiceAIGuardrailId: Optional[str] = None
    selfServiceAnswerGenerationAIPromptId: Optional[str] = None
    selfServicePreProcessingAIPromptId: Optional[str] = None


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


class VectorIngestionConfigurationUnionTypeDef(BaseValidatorModel):
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
    vectorIngestionConfiguration: Optional[VectorIngestionConfigurationUnionTypeDef] = None


class ResultDataPaginatorTypeDef(BaseValidatorModel):
    pass


class QueryAssistantResponsePaginatorTypeDef(BaseValidatorModel):
    results: List[ResultDataPaginatorTypeDef]
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


class ResultDataTypeDef(BaseValidatorModel):
    pass


class QueryAssistantResponseTypeDef(BaseValidatorModel):
    results: List[ResultDataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AIAgentConfigurationOutputTypeDef(BaseValidatorModel):
    answerRecommendationAIAgentConfiguration: Optional[ AnswerRecommendationAIAgentConfigurationOutputTypeDef ] = None
    manualSearchAIAgentConfiguration: Optional[ManualSearchAIAgentConfigurationOutputTypeDef] = None
    selfServiceAIAgentConfiguration: Optional[SelfServiceAIAgentConfigurationOutputTypeDef] = None


class AIAgentConfigurationTypeDef(BaseValidatorModel):
    answerRecommendationAIAgentConfiguration: Optional[ AnswerRecommendationAIAgentConfigurationTypeDef ] = None
    manualSearchAIAgentConfiguration: Optional[ManualSearchAIAgentConfigurationTypeDef] = None
    selfServiceAIAgentConfiguration: Optional[SelfServiceAIAgentConfigurationTypeDef] = None


class AIAgentDataTypeDef(BaseValidatorModel):
    pass


class CreateAIAgentResponseTypeDef(BaseValidatorModel):
    aiAgent: AIAgentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateAIAgentVersionResponseTypeDef(BaseValidatorModel):
    aiAgent: AIAgentDataTypeDef
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef


class GetAIAgentResponseTypeDef(BaseValidatorModel):
    aiAgent: AIAgentDataTypeDef
    versionNumber: int
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateAIAgentResponseTypeDef(BaseValidatorModel):
    aiAgent: AIAgentDataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class AIAgentSummaryTypeDef(BaseValidatorModel):
    pass


class AIAgentVersionSummaryTypeDef(BaseValidatorModel):
    aiAgentSummary: Optional[AIAgentSummaryTypeDef] = None
    versionNumber: Optional[int] = None


class ListAIAgentsResponseTypeDef(BaseValidatorModel):
    aiAgentSummaries: List[AIAgentSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class AIAgentConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateAIAgentRequestTypeDef(BaseValidatorModel):
    aiAgentId: str
    assistantId: str
    visibilityStatus: VisibilityStatusType
    clientToken: Optional[str] = None
    configuration: Optional[AIAgentConfigurationUnionTypeDef] = None
    description: Optional[str] = None


class ListAIAgentVersionsResponseTypeDef(BaseValidatorModel):
    aiAgentVersionSummaries: List[AIAgentVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


