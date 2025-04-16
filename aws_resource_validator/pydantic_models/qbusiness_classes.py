from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel, EventStream
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
from aws_resource_validator.pydantic_models.qbusiness_constants import *

class S3(BaseValidatorModel):
    bucket: str
    key: str


class ActionExecutionPayloadFieldOutput(BaseValidatorModel):
    value: Dict[str, Any]


class ActionExecutionPayloadField(BaseValidatorModel):
    value: Mapping[str, Any]


class ActionReviewPayloadFieldAllowedValue(BaseValidatorModel):
    value: Optional[Dict[str, Any]] = None
    displayValue: Optional[Dict[str, Any]] = None


class ActionSummary(BaseValidatorModel):
    actionIdentifier: Optional[str] = None
    displayName: Optional[str] = None
    instructionExample: Optional[str] = None
    description: Optional[str] = None


class QuickSightConfiguration(BaseValidatorModel):
    clientNamespace: str


class AppliedAttachmentsConfiguration(BaseValidatorModel):
    attachmentsControlMode: Optional[AttachmentsControlModeType] = None


class AppliedCreatorModeConfiguration(BaseValidatorModel):
    creatorModeControl: CreatorModeControlType


class AppliedOrchestrationConfiguration(BaseValidatorModel):
    control: OrchestrationControlType


class AssociatePermissionRequest(BaseValidatorModel):
    applicationId: str
    statementId: str
    actions: Sequence[str]
    principal: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ErrorDetail(BaseValidatorModel):
    errorMessage: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None


class AttachmentsConfiguration(BaseValidatorModel):
    attachmentsControlMode: AttachmentsControlModeType


class AudioExtractionConfiguration(BaseValidatorModel):
    audioExtractionStatus: AudioExtractionStatusType


class AudioSourceDetails(BaseValidatorModel):
    mediaId: Optional[str] = None
    mediaMimeType: Optional[str] = None
    startTimeMilliseconds: Optional[int] = None
    endTimeMilliseconds: Optional[int] = None
    audioExtractionType: Optional[AudioExtractionTypeType] = None


class AuthChallengeRequestEvent(BaseValidatorModel):
    authorizationUrl: str


class AuthChallengeRequest(BaseValidatorModel):
    authorizationUrl: str


class AuthChallengeResponseEvent(BaseValidatorModel):
    responseMap: Mapping[str, str]


class AuthChallengeResponse(BaseValidatorModel):
    responseMap: Mapping[str, str]


class AutoSubscriptionConfiguration(BaseValidatorModel):
    autoSubscribe: AutoSubscriptionStatusType
    defaultSubscriptionType: Optional[SubscriptionTypeType] = None


class BasicAuthConfiguration(BaseValidatorModel):
    secretArn: str
    roleArn: str


class DeleteDocument(BaseValidatorModel):
    documentId: str


class BlockedPhrasesConfiguration(BaseValidatorModel):
    blockedPhrases: Optional[List[str]] = None
    systemMessageOverride: Optional[str] = None


class BlockedPhrasesConfigurationUpdate(BaseValidatorModel):
    blockedPhrasesToCreateOrUpdate: Optional[Sequence[str]] = None
    blockedPhrasesToDelete: Optional[Sequence[str]] = None
    systemMessageOverride: Optional[str] = None


class BrowserExtensionConfigurationOutput(BaseValidatorModel):
    enabledBrowserExtensions: List[BrowserExtensionType]


class BrowserExtensionConfiguration(BaseValidatorModel):
    enabledBrowserExtensions: Sequence[BrowserExtensionType]


class CancelSubscriptionRequest(BaseValidatorModel):
    applicationId: str
    subscriptionId: str


class TextInputEvent(BaseValidatorModel):
    userMessage: str


class PluginConfiguration(BaseValidatorModel):
    pluginId: str


class TextOutputEvent(BaseValidatorModel):
    conversationId: Optional[str] = None
    userMessageId: Optional[str] = None
    systemMessageId: Optional[str] = None
    systemMessage: Optional[str] = None


class ContentBlockerRule(BaseValidatorModel):
    systemMessageOverride: Optional[str] = None


class EligibleDataSource(BaseValidatorModel):
    indexId: Optional[str] = None
    dataSourceId: Optional[str] = None


class RetrieverContentSource(BaseValidatorModel):
    retrieverId: str


class ConversationSource(BaseValidatorModel):
    conversationId: str
    attachmentId: str


class Conversation(BaseValidatorModel):
    conversationId: Optional[str] = None
    title: Optional[str] = None
    startTime: Optional[datetime] = None


class EncryptionConfiguration(BaseValidatorModel):
    kmsKeyId: Optional[str] = None


class PersonalizationConfiguration(BaseValidatorModel):
    personalizationControlMode: PersonalizationControlModeType


class QAppsConfiguration(BaseValidatorModel):
    qAppsControlMode: QAppsControlModeType


class Tag(BaseValidatorModel):
    key: str
    value: str


class IndexCapacityConfiguration(BaseValidatorModel):
    units: Optional[int] = None


class SubscriptionPrincipal(BaseValidatorModel):
    user: Optional[str] = None
    group: Optional[str] = None


class UserAlias(BaseValidatorModel):
    userId: str
    indexId: Optional[str] = None
    dataSourceId: Optional[str] = None


class CustomizationConfiguration(BaseValidatorModel):
    customCSSUrl: Optional[str] = None
    logoUrl: Optional[str] = None
    fontUrl: Optional[str] = None
    faviconUrl: Optional[str] = None


class CreatorModeConfiguration(BaseValidatorModel):
    creatorModeControl: CreatorModeControlType


class DataAccessor(BaseValidatorModel):
    displayName: Optional[str] = None
    dataAccessorId: Optional[str] = None
    dataAccessorArn: Optional[str] = None
    idcApplicationArn: Optional[str] = None
    principal: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class DataSourceSyncJobMetrics(BaseValidatorModel):
    documentsAdded: Optional[str] = None
    documentsModified: Optional[str] = None
    documentsDeleted: Optional[str] = None
    documentsFailed: Optional[str] = None
    documentsScanned: Optional[str] = None


class DataSourceVpcConfigurationOutput(BaseValidatorModel):
    subnetIds: List[str]
    securityGroupIds: List[str]


class DataSourceVpcConfiguration(BaseValidatorModel):
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]


class DateAttributeBoostingConfiguration(BaseValidatorModel):
    boostingLevel: DocumentAttributeBoostingLevelType
    boostingDurationInSeconds: Optional[int] = None


class DeleteApplicationRequest(BaseValidatorModel):
    applicationId: str


class DeleteAttachmentRequest(BaseValidatorModel):
    applicationId: str
    conversationId: str
    attachmentId: str
    userId: Optional[str] = None


class DeleteChatControlsConfigurationRequest(BaseValidatorModel):
    applicationId: str


class DeleteConversationRequest(BaseValidatorModel):
    conversationId: str
    applicationId: str
    userId: Optional[str] = None


class DeleteDataAccessorRequest(BaseValidatorModel):
    applicationId: str
    dataAccessorId: str


class DeleteDataSourceRequest(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceId: str


class DeleteGroupRequest(BaseValidatorModel):
    applicationId: str
    indexId: str
    groupName: str
    dataSourceId: Optional[str] = None


class DeleteIndexRequest(BaseValidatorModel):
    applicationId: str
    indexId: str


class DeletePluginRequest(BaseValidatorModel):
    applicationId: str
    pluginId: str


class DeleteRetrieverRequest(BaseValidatorModel):
    applicationId: str
    retrieverId: str


class DeleteUserRequest(BaseValidatorModel):
    applicationId: str
    userId: str


class DeleteWebExperienceRequest(BaseValidatorModel):
    applicationId: str
    webExperienceId: str


class DisassociatePermissionRequest(BaseValidatorModel):
    applicationId: str
    statementId: str


class NumberAttributeBoostingConfiguration(BaseValidatorModel):
    boostingLevel: DocumentAttributeBoostingLevelType
    boostingType: Optional[NumberAttributeBoostingTypeType] = None


class StringAttributeBoostingConfigurationOutput(BaseValidatorModel):
    boostingLevel: DocumentAttributeBoostingLevelType
    attributeValueBoosting: Optional[Dict[str, StringAttributeValueBoostingLevelType]] = None


class StringListAttributeBoostingConfiguration(BaseValidatorModel):
    boostingLevel: DocumentAttributeBoostingLevelType


class StringAttributeBoostingConfiguration(BaseValidatorModel):
    boostingLevel: DocumentAttributeBoostingLevelType
    attributeValueBoosting: Optional[Mapping[str, StringAttributeValueBoostingLevelType]] = None


class DocumentAttributeValueOutput(BaseValidatorModel):
    stringValue: Optional[str] = None
    stringListValue: Optional[List[str]] = None
    longValue: Optional[int] = None
    dateValue: Optional[datetime] = None


class GetApplicationRequest(BaseValidatorModel):
    applicationId: str


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetChatControlsConfigurationRequest(BaseValidatorModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetDataAccessorRequest(BaseValidatorModel):
    applicationId: str
    dataAccessorId: str


class GetDataSourceRequest(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceId: str


class GetGroupRequest(BaseValidatorModel):
    applicationId: str
    indexId: str
    groupName: str
    dataSourceId: Optional[str] = None


class GetIndexRequest(BaseValidatorModel):
    applicationId: str
    indexId: str


class GetMediaRequest(BaseValidatorModel):
    applicationId: str
    conversationId: str
    messageId: str
    mediaId: str


class GetPluginRequest(BaseValidatorModel):
    applicationId: str
    pluginId: str


class GetPolicyRequest(BaseValidatorModel):
    applicationId: str


class GetRetrieverRequest(BaseValidatorModel):
    applicationId: str
    retrieverId: str


class GetUserRequest(BaseValidatorModel):
    applicationId: str
    userId: str


class GetWebExperienceRequest(BaseValidatorModel):
    applicationId: str
    webExperienceId: str


class GroupSummary(BaseValidatorModel):
    groupName: Optional[str] = None


class IdcAuthConfiguration(BaseValidatorModel):
    idcApplicationArn: str
    roleArn: str


class OpenIDConnectProviderConfiguration(BaseValidatorModel):
    secretsArn: str
    secretsRole: str


class SamlProviderConfiguration(BaseValidatorModel):
    authenticationUrl: str


class ImageExtractionConfiguration(BaseValidatorModel):
    imageExtractionStatus: ImageExtractionStatusType


class ImageSourceDetails(BaseValidatorModel):
    mediaId: Optional[str] = None
    mediaMimeType: Optional[str] = None


class TextDocumentStatistics(BaseValidatorModel):
    indexedTextBytes: Optional[int] = None
    indexedTextDocumentCount: Optional[int] = None


class Index(BaseValidatorModel):
    displayName: Optional[str] = None
    indexId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    status: Optional[IndexStatusType] = None


class KendraIndexConfiguration(BaseValidatorModel):
    indexId: str


class ListApplicationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAttachmentsRequest(BaseValidatorModel):
    applicationId: str
    conversationId: Optional[str] = None
    userId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListConversationsRequest(BaseValidatorModel):
    applicationId: str
    userId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDataAccessorsRequest(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDataSourcesRequest(BaseValidatorModel):
    applicationId: str
    indexId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDocumentsRequest(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListIndicesRequest(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMessagesRequest(BaseValidatorModel):
    conversationId: str
    applicationId: str
    userId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPluginActionsRequest(BaseValidatorModel):
    applicationId: str
    pluginId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPluginTypeActionsRequest(BaseValidatorModel):
    pluginType: PluginTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPluginTypeMetadataRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPluginsRequest(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListRetrieversRequest(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSubscriptionsRequest(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceARN: str


class ListWebExperiencesRequest(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class WebExperience(BaseValidatorModel):
    webExperienceId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    defaultEndpoint: Optional[str] = None
    status: Optional[WebExperienceStatusType] = None


class VideoExtractionConfiguration(BaseValidatorModel):
    videoExtractionStatus: VideoExtractionStatusType


class OAuth2ClientCredentialConfiguration(BaseValidatorModel):
    secretArn: str
    roleArn: str
    authorizationUrl: Optional[str] = None
    tokenUrl: Optional[str] = None


class OrchestrationConfiguration(BaseValidatorModel):
    control: OrchestrationControlType


class PrincipalGroup(BaseValidatorModel):
    access: ReadAccessTypeType
    name: Optional[str] = None
    membershipType: Optional[MembershipTypeType] = None


class ScoreAttributes(BaseValidatorModel):
    scoreConfidence: Optional[ScoreConfidenceType] = None


class UsersAndGroupsOutput(BaseValidatorModel):
    userIds: Optional[List[str]] = None
    userGroups: Optional[List[str]] = None


class SamlConfiguration(BaseValidatorModel):
    metadataXML: str
    roleArn: str
    userIdAttribute: str
    userGroupAttribute: Optional[str] = None


class SnippetExcerpt(BaseValidatorModel):
    text: Optional[str] = None


class VideoSourceDetails(BaseValidatorModel):
    mediaId: Optional[str] = None
    mediaMimeType: Optional[str] = None
    startTimeMilliseconds: Optional[int] = None
    endTimeMilliseconds: Optional[int] = None
    videoExtractionType: Optional[VideoExtractionTypeType] = None


class StartDataSourceSyncJobRequest(BaseValidatorModel):
    dataSourceId: str
    applicationId: str
    indexId: str


class StopDataSourceSyncJobRequest(BaseValidatorModel):
    dataSourceId: str
    applicationId: str
    indexId: str


class UntagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]


class UsersAndGroups(BaseValidatorModel):
    userIds: Optional[Sequence[str]] = None
    userGroups: Optional[Sequence[str]] = None


class APISchema(BaseValidatorModel):
    payload: Optional[str] = None
    s3: Optional[S3] = None


class ActionExecutionOutput(BaseValidatorModel):
    pluginId: str
    payload: Dict[str, ActionExecutionPayloadFieldOutput]
    payloadFieldNameSeparator: str


class ActionExecution(BaseValidatorModel):
    pluginId: str
    payload: Mapping[str, ActionExecutionPayloadField]
    payloadFieldNameSeparator: str


class Application(BaseValidatorModel):
    displayName: Optional[str] = None
    applicationId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    status: Optional[ApplicationStatusType] = None
    identityType: Optional[IdentityTypeType] = None
    quickSightConfiguration: Optional[QuickSightConfiguration] = None


class AssociatePermissionResponse(BaseValidatorModel):
    statement: str
    ResponseMetadata: ResponseMetadata


class CreateApplicationResponse(BaseValidatorModel):
    applicationId: str
    applicationArn: str
    ResponseMetadata: ResponseMetadata


class CreateDataAccessorResponse(BaseValidatorModel):
    dataAccessorId: str
    idcApplicationArn: str
    dataAccessorArn: str
    ResponseMetadata: ResponseMetadata


class CreateDataSourceResponse(BaseValidatorModel):
    dataSourceId: str
    dataSourceArn: str
    ResponseMetadata: ResponseMetadata


class CreateIndexResponse(BaseValidatorModel):
    indexId: str
    indexArn: str
    ResponseMetadata: ResponseMetadata


class CreatePluginResponse(BaseValidatorModel):
    pluginId: str
    pluginArn: str
    buildStatus: PluginBuildStatusType
    ResponseMetadata: ResponseMetadata


class CreateRetrieverResponse(BaseValidatorModel):
    retrieverId: str
    retrieverArn: str
    ResponseMetadata: ResponseMetadata


class CreateWebExperienceResponse(BaseValidatorModel):
    webExperienceId: str
    webExperienceArn: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetMediaResponse(BaseValidatorModel):
    mediaBytes: bytes
    mediaMimeType: str
    ResponseMetadata: ResponseMetadata


class GetPolicyResponse(BaseValidatorModel):
    policy: str
    ResponseMetadata: ResponseMetadata


class ListPluginActionsResponse(BaseValidatorModel):
    items: List[ActionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListPluginTypeActionsResponse(BaseValidatorModel):
    items: List[ActionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class StartDataSourceSyncJobResponse(BaseValidatorModel):
    executionId: str
    ResponseMetadata: ResponseMetadata


class Blob(BaseValidatorModel):
    pass


class DocumentContent(BaseValidatorModel):
    blob: Optional[Blob] = None
    s3: Optional[S3] = None


class AttachmentOutput(BaseValidatorModel):
    name: Optional[str] = None
    status: Optional[AttachmentStatusType] = None
    error: Optional[ErrorDetail] = None
    attachmentId: Optional[str] = None
    conversationId: Optional[str] = None


class DocumentDetails(BaseValidatorModel):
    documentId: Optional[str] = None
    status: Optional[DocumentStatusType] = None
    error: Optional[ErrorDetail] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class GroupStatusDetail(BaseValidatorModel):
    status: Optional[GroupStatusType] = None
    lastUpdatedAt: Optional[datetime] = None
    errorDetail: Optional[ErrorDetail] = None


class BatchDeleteDocumentRequest(BaseValidatorModel):
    applicationId: str
    indexId: str
    documents: Sequence[DeleteDocument]
    dataSourceSyncId: Optional[str] = None


class SubscriptionDetails(BaseValidatorModel):
    pass


class CancelSubscriptionResponse(BaseValidatorModel):
    subscriptionArn: str
    currentSubscription: SubscriptionDetails
    nextSubscription: SubscriptionDetails
    ResponseMetadata: ResponseMetadata


class CreateSubscriptionResponse(BaseValidatorModel):
    subscriptionId: str
    subscriptionArn: str
    currentSubscription: SubscriptionDetails
    nextSubscription: SubscriptionDetails
    ResponseMetadata: ResponseMetadata


class UpdateSubscriptionResponse(BaseValidatorModel):
    subscriptionArn: str
    currentSubscription: SubscriptionDetails
    nextSubscription: SubscriptionDetails
    ResponseMetadata: ResponseMetadata


class ChatModeConfiguration(BaseValidatorModel):
    pluginConfiguration: Optional[PluginConfiguration] = None


class ContentRetrievalRuleOutput(BaseValidatorModel):
    eligibleDataSources: Optional[List[EligibleDataSource]] = None


class ContentRetrievalRule(BaseValidatorModel):
    eligibleDataSources: Optional[Sequence[EligibleDataSource]] = None


class ContentSource(BaseValidatorModel):
    retriever: Optional[RetrieverContentSource] = None


class CopyFromSource(BaseValidatorModel):
    conversation: Optional[ConversationSource] = None


class ListConversationsResponse(BaseValidatorModel):
    conversations: List[Conversation]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetApplicationResponse(BaseValidatorModel):
    displayName: str
    applicationId: str
    applicationArn: str
    identityType: IdentityTypeType
    iamIdentityProviderArn: str
    identityCenterApplicationArn: str
    roleArn: str
    status: ApplicationStatusType
    description: str
    encryptionConfiguration: EncryptionConfiguration
    createdAt: datetime
    updatedAt: datetime
    error: ErrorDetail
    attachmentsConfiguration: AppliedAttachmentsConfiguration
    qAppsConfiguration: QAppsConfiguration
    personalizationConfiguration: PersonalizationConfiguration
    autoSubscriptionConfiguration: AutoSubscriptionConfiguration
    clientIdsForOIDC: List[str]
    quickSightConfiguration: QuickSightConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateApplicationRequest(BaseValidatorModel):
    applicationId: str
    identityCenterInstanceArn: Optional[str] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    roleArn: Optional[str] = None
    attachmentsConfiguration: Optional[AttachmentsConfiguration] = None
    qAppsConfiguration: Optional[QAppsConfiguration] = None
    personalizationConfiguration: Optional[PersonalizationConfiguration] = None
    autoSubscriptionConfiguration: Optional[AutoSubscriptionConfiguration] = None


class CreateApplicationRequest(BaseValidatorModel):
    displayName: str
    roleArn: Optional[str] = None
    identityType: Optional[IdentityTypeType] = None
    iamIdentityProviderArn: Optional[str] = None
    identityCenterInstanceArn: Optional[str] = None
    clientIdsForOIDC: Optional[Sequence[str]] = None
    description: Optional[str] = None
    encryptionConfiguration: Optional[EncryptionConfiguration] = None
    tags: Optional[Sequence[Tag]] = None
    clientToken: Optional[str] = None
    attachmentsConfiguration: Optional[AttachmentsConfiguration] = None
    qAppsConfiguration: Optional[QAppsConfiguration] = None
    personalizationConfiguration: Optional[PersonalizationConfiguration] = None
    quickSightConfiguration: Optional[QuickSightConfiguration] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class TagResourceRequest(BaseValidatorModel):
    resourceARN: str
    tags: Sequence[Tag]


class Subscription(BaseValidatorModel):
    subscriptionId: Optional[str] = None
    subscriptionArn: Optional[str] = None
    principal: Optional[SubscriptionPrincipal] = None
    currentSubscription: Optional[SubscriptionDetails] = None
    nextSubscription: Optional[SubscriptionDetails] = None


class CreateUserRequest(BaseValidatorModel):
    applicationId: str
    userId: str
    userAliases: Optional[Sequence[UserAlias]] = None
    clientToken: Optional[str] = None


class GetUserResponse(BaseValidatorModel):
    userAliases: List[UserAlias]
    ResponseMetadata: ResponseMetadata


class UpdateUserRequest(BaseValidatorModel):
    applicationId: str
    userId: str
    userAliasesToUpdate: Optional[Sequence[UserAlias]] = None
    userAliasesToDelete: Optional[Sequence[UserAlias]] = None


class UpdateUserResponse(BaseValidatorModel):
    userAliasesAdded: List[UserAlias]
    userAliasesUpdated: List[UserAlias]
    userAliasesDeleted: List[UserAlias]
    ResponseMetadata: ResponseMetadata


class ListDataAccessorsResponse(BaseValidatorModel):
    dataAccessors: List[DataAccessor]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DataSourceSyncJob(BaseValidatorModel):
    executionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    status: Optional[DataSourceSyncJobStatusType] = None
    error: Optional[ErrorDetail] = None
    dataSourceErrorCode: Optional[str] = None
    metrics: Optional[DataSourceSyncJobMetrics] = None


class DataSource(BaseValidatorModel):
    pass


class ListDataSourcesResponse(BaseValidatorModel):
    dataSources: List[DataSource]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DocumentAttributeBoostingConfigurationOutput(BaseValidatorModel):
    numberConfiguration: Optional[NumberAttributeBoostingConfiguration] = None
    stringConfiguration: Optional[StringAttributeBoostingConfigurationOutput] = None
    dateConfiguration: Optional[DateAttributeBoostingConfiguration] = None
    stringListConfiguration: Optional[StringListAttributeBoostingConfiguration] = None


class DocumentAttributeBoostingConfiguration(BaseValidatorModel):
    numberConfiguration: Optional[NumberAttributeBoostingConfiguration] = None
    stringConfiguration: Optional[StringAttributeBoostingConfiguration] = None
    dateConfiguration: Optional[DateAttributeBoostingConfiguration] = None
    stringListConfiguration: Optional[StringListAttributeBoostingConfiguration] = None


class DocumentAttributeOutput(BaseValidatorModel):
    name: str
    value: DocumentAttributeValueOutput


class DocumentAttributeTargetOutput(BaseValidatorModel):
    key: str
    value: Optional[DocumentAttributeValueOutput] = None
    attributeValueOperator: Optional[Literal["DELETE"]] = None


class DocumentAttributeConfiguration(BaseValidatorModel):
    pass


class UpdateIndexRequest(BaseValidatorModel):
    applicationId: str
    indexId: str
    displayName: Optional[str] = None
    description: Optional[str] = None
    capacityConfiguration: Optional[IndexCapacityConfiguration] = None
    documentAttributeConfigurations: Optional[Sequence[DocumentAttributeConfiguration]] = None


class Timestamp(BaseValidatorModel):
    pass


class DocumentAttributeValue(BaseValidatorModel):
    stringValue: Optional[str] = None
    stringListValue: Optional[Sequence[str]] = None
    longValue: Optional[int] = None
    dateValue: Optional[Timestamp] = None


class ListDataSourceSyncJobsRequest(BaseValidatorModel):
    dataSourceId: str
    applicationId: str
    indexId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    statusFilter: Optional[DataSourceSyncJobStatusType] = None


class ListGroupsRequest(BaseValidatorModel):
    applicationId: str
    indexId: str
    updatedEarlierThan: Timestamp
    dataSourceId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class MessageUsefulnessFeedback(BaseValidatorModel):
    usefulness: MessageUsefulnessType
    submittedAt: Timestamp
    reason: Optional[MessageUsefulnessReasonType] = None
    comment: Optional[str] = None


class GetChatControlsConfigurationRequestPaginate(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApplicationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAttachmentsRequestPaginate(BaseValidatorModel):
    applicationId: str
    conversationId: Optional[str] = None
    userId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListConversationsRequestPaginate(BaseValidatorModel):
    applicationId: str
    userId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataAccessorsRequestPaginate(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataSourceSyncJobsRequestPaginate(BaseValidatorModel):
    dataSourceId: str
    applicationId: str
    indexId: str
    startTime: Optional[Timestamp] = None
    endTime: Optional[Timestamp] = None
    statusFilter: Optional[DataSourceSyncJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDataSourcesRequestPaginate(BaseValidatorModel):
    applicationId: str
    indexId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDocumentsRequestPaginate(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListGroupsRequestPaginate(BaseValidatorModel):
    applicationId: str
    indexId: str
    updatedEarlierThan: Timestamp
    dataSourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIndicesRequestPaginate(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListMessagesRequestPaginate(BaseValidatorModel):
    conversationId: str
    applicationId: str
    userId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPluginActionsRequestPaginate(BaseValidatorModel):
    applicationId: str
    pluginId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPluginTypeActionsRequestPaginate(BaseValidatorModel):
    pluginType: PluginTypeType
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPluginTypeMetadataRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPluginsRequestPaginate(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRetrieversRequestPaginate(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSubscriptionsRequestPaginate(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListWebExperiencesRequestPaginate(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class MemberUser(BaseValidatorModel):
    pass


class MemberGroup(BaseValidatorModel):
    pass


class GroupMembers(BaseValidatorModel):
    memberGroups: Optional[Sequence[MemberGroup]] = None
    memberUsers: Optional[Sequence[MemberUser]] = None
    s3PathForGroupMembers: Optional[S3] = None


class ListGroupsResponse(BaseValidatorModel):
    items: List[GroupSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class IdentityProviderConfiguration(BaseValidatorModel):
    samlConfiguration: Optional[SamlProviderConfiguration] = None
    openIDConnectConfiguration: Optional[OpenIDConnectProviderConfiguration] = None


class IndexStatistics(BaseValidatorModel):
    textDocumentStatistics: Optional[TextDocumentStatistics] = None


class ListIndicesResponse(BaseValidatorModel):
    indices: List[Index]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class PluginTypeMetadataSummary(BaseValidatorModel):
    pass


class ListPluginTypeMetadataResponse(BaseValidatorModel):
    items: List[PluginTypeMetadataSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Plugin(BaseValidatorModel):
    pass


class ListPluginsResponse(BaseValidatorModel):
    plugins: List[Plugin]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class Retriever(BaseValidatorModel):
    pass


class ListRetrieversResponse(BaseValidatorModel):
    retrievers: List[Retriever]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListWebExperiencesResponse(BaseValidatorModel):
    webExperiences: List[WebExperience]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class MediaExtractionConfiguration(BaseValidatorModel):
    imageExtractionConfiguration: Optional[ImageExtractionConfiguration] = None
    audioExtractionConfiguration: Optional[AudioExtractionConfiguration] = None
    videoExtractionConfiguration: Optional[VideoExtractionConfiguration] = None


class PluginAuthConfigurationOutput(BaseValidatorModel):
    basicAuthConfiguration: Optional[BasicAuthConfiguration] = None
    oAuth2ClientCredentialConfiguration: Optional[OAuth2ClientCredentialConfiguration] = None
    noAuthConfiguration: Optional[Dict[str, Any]] = None
    idcAuthConfiguration: Optional[IdcAuthConfiguration] = None


class PluginAuthConfiguration(BaseValidatorModel):
    basicAuthConfiguration: Optional[BasicAuthConfiguration] = None
    oAuth2ClientCredentialConfiguration: Optional[OAuth2ClientCredentialConfiguration] = None
    noAuthConfiguration: Optional[Mapping[str, Any]] = None
    idcAuthConfiguration: Optional[IdcAuthConfiguration] = None


class PrincipalUser(BaseValidatorModel):
    pass


class Principal(BaseValidatorModel):
    user: Optional[PrincipalUser] = None
    group: Optional[PrincipalGroup] = None


class WebExperienceAuthConfiguration(BaseValidatorModel):
    samlConfiguration: Optional[SamlConfiguration] = None


class SourceDetails(BaseValidatorModel):
    imageSourceDetails: Optional[ImageSourceDetails] = None
    audioSourceDetails: Optional[AudioSourceDetails] = None
    videoSourceDetails: Optional[VideoSourceDetails] = None


class CustomPluginConfiguration(BaseValidatorModel):
    description: str
    apiSchemaType: Literal["OPEN_API_V3"]
    apiSchema: APISchema


class ActionExecutionPayloadFieldUnion(BaseValidatorModel):
    pass


class ActionExecutionEvent(BaseValidatorModel):
    pluginId: str
    payload: Mapping[str, ActionExecutionPayloadFieldUnion]
    payloadFieldNameSeparator: str


class ActionReviewPayloadField(BaseValidatorModel):
    pass


class ActionReviewEvent(BaseValidatorModel):
    conversationId: Optional[str] = None
    userMessageId: Optional[str] = None
    systemMessageId: Optional[str] = None
    pluginId: Optional[str] = None
    pluginType: Optional[PluginTypeType] = None
    payload: Optional[Dict[str, ActionReviewPayloadField]] = None
    payloadFieldNameSeparator: Optional[str] = None


class ActionReview(BaseValidatorModel):
    pluginId: Optional[str] = None
    pluginType: Optional[PluginTypeType] = None
    payload: Optional[Dict[str, ActionReviewPayloadField]] = None
    payloadFieldNameSeparator: Optional[str] = None


class ListApplicationsResponse(BaseValidatorModel):
    applications: List[Application]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FailedAttachmentEvent(BaseValidatorModel):
    conversationId: Optional[str] = None
    userMessageId: Optional[str] = None
    systemMessageId: Optional[str] = None
    attachment: Optional[AttachmentOutput] = None


class ListDocumentsResponse(BaseValidatorModel):
    documentDetailList: List[DocumentDetails]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class FailedDocument(BaseValidatorModel):
    pass


class BatchDeleteDocumentResponse(BaseValidatorModel):
    failedDocuments: List[FailedDocument]
    ResponseMetadata: ResponseMetadata


class BatchPutDocumentResponse(BaseValidatorModel):
    failedDocuments: List[FailedDocument]
    ResponseMetadata: ResponseMetadata


class GetGroupResponse(BaseValidatorModel):
    status: GroupStatusDetail
    statusHistory: List[GroupStatusDetail]
    ResponseMetadata: ResponseMetadata


class RuleConfigurationOutput(BaseValidatorModel):
    contentBlockerRule: Optional[ContentBlockerRule] = None
    contentRetrievalRule: Optional[ContentRetrievalRuleOutput] = None


class AttachmentInput(BaseValidatorModel):
    data: Optional[Blob] = None
    name: Optional[str] = None
    copyFrom: Optional[CopyFromSource] = None


class Attachment(BaseValidatorModel):
    attachmentId: Optional[str] = None
    conversationId: Optional[str] = None
    name: Optional[str] = None
    copyFrom: Optional[CopyFromSource] = None
    fileType: Optional[str] = None
    fileSize: Optional[int] = None
    md5chksum: Optional[str] = None
    createdAt: Optional[datetime] = None
    status: Optional[AttachmentStatusType] = None
    error: Optional[ErrorDetail] = None


class ListSubscriptionsResponse(BaseValidatorModel):
    subscriptions: List[Subscription]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListDataSourceSyncJobsResponse(BaseValidatorModel):
    history: List[DataSourceSyncJob]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class NativeIndexConfigurationOutput(BaseValidatorModel):
    indexId: str
    boostingOverride: Optional[Dict[str, DocumentAttributeBoostingConfigurationOutput]] = None


class NativeIndexConfiguration(BaseValidatorModel):
    indexId: str
    boostingOverride: Optional[Mapping[str, DocumentAttributeBoostingConfiguration]] = None


class DocumentAttributeConditionOutput(BaseValidatorModel):
    pass


class HookConfigurationOutput(BaseValidatorModel):
    invocationCondition: Optional[DocumentAttributeConditionOutput] = None
    lambdaArn: Optional[str] = None
    s3BucketName: Optional[str] = None
    roleArn: Optional[str] = None


class AttributeFilterOutput(BaseValidatorModel):
    andAllFilters: Optional[List[Dict[str, Any]]] = None
    orAllFilters: Optional[List[Dict[str, Any]]] = None
    notFilter: Optional[Dict[str, Any]] = None
    equalsTo: Optional[DocumentAttributeOutput] = None
    containsAll: Optional[DocumentAttributeOutput] = None
    containsAny: Optional[DocumentAttributeOutput] = None
    greaterThan: Optional[DocumentAttributeOutput] = None
    greaterThanOrEquals: Optional[DocumentAttributeOutput] = None
    lessThan: Optional[DocumentAttributeOutput] = None
    lessThanOrEquals: Optional[DocumentAttributeOutput] = None


class RelevantContent(BaseValidatorModel):
    content: Optional[str] = None
    documentId: Optional[str] = None
    documentTitle: Optional[str] = None
    documentUri: Optional[str] = None
    documentAttributes: Optional[List[DocumentAttributeOutput]] = None
    scoreAttributes: Optional[ScoreAttributes] = None


class InlineDocumentEnrichmentConfigurationOutput(BaseValidatorModel):
    condition: Optional[DocumentAttributeConditionOutput] = None
    target: Optional[DocumentAttributeTargetOutput] = None
    documentContentOperator: Optional[Literal["DELETE"]] = None


class PutFeedbackRequest(BaseValidatorModel):
    applicationId: str
    conversationId: str
    messageId: str
    userId: Optional[str] = None
    messageCopiedAt: Optional[Timestamp] = None
    messageUsefulness: Optional[MessageUsefulnessFeedback] = None


class BrowserExtensionConfigurationUnion(BaseValidatorModel):
    pass


class CreateWebExperienceRequest(BaseValidatorModel):
    applicationId: str
    title: Optional[str] = None
    subtitle: Optional[str] = None
    welcomeMessage: Optional[str] = None
    samplePromptsControlMode: Optional[WebExperienceSamplePromptsControlModeType] = None
    origins: Optional[Sequence[str]] = None
    roleArn: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None
    clientToken: Optional[str] = None
    identityProviderConfiguration: Optional[IdentityProviderConfiguration] = None
    browserExtensionConfiguration: Optional[BrowserExtensionConfigurationUnion] = None
    customizationConfiguration: Optional[CustomizationConfiguration] = None


class AccessControl(BaseValidatorModel):
    principals: Sequence[Principal]
    memberRelation: Optional[MemberRelationType] = None


class GetWebExperienceResponse(BaseValidatorModel):
    applicationId: str
    webExperienceId: str
    webExperienceArn: str
    defaultEndpoint: str
    status: WebExperienceStatusType
    createdAt: datetime
    updatedAt: datetime
    title: str
    subtitle: str
    welcomeMessage: str
    samplePromptsControlMode: WebExperienceSamplePromptsControlModeType
    origins: List[str]
    roleArn: str
    identityProviderConfiguration: IdentityProviderConfiguration
    authenticationConfiguration: WebExperienceAuthConfiguration
    error: ErrorDetail
    browserExtensionConfiguration: BrowserExtensionConfigurationOutput
    customizationConfiguration: CustomizationConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateWebExperienceRequest(BaseValidatorModel):
    applicationId: str
    webExperienceId: str
    roleArn: Optional[str] = None
    authenticationConfiguration: Optional[WebExperienceAuthConfiguration] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    welcomeMessage: Optional[str] = None
    samplePromptsControlMode: Optional[WebExperienceSamplePromptsControlModeType] = None
    identityProviderConfiguration: Optional[IdentityProviderConfiguration] = None
    origins: Optional[Sequence[str]] = None
    browserExtensionConfiguration: Optional[BrowserExtensionConfigurationUnion] = None
    customizationConfiguration: Optional[CustomizationConfiguration] = None


class TextSegment(BaseValidatorModel):
    beginOffset: Optional[int] = None
    endOffset: Optional[int] = None
    snippetExcerpt: Optional[SnippetExcerpt] = None
    mediaId: Optional[str] = None
    mediaMimeType: Optional[str] = None
    sourceDetails: Optional[SourceDetails] = None


class RuleOutput(BaseValidatorModel):
    ruleType: RuleTypeType
    includedUsersAndGroups: Optional[UsersAndGroupsOutput] = None
    excludedUsersAndGroups: Optional[UsersAndGroupsOutput] = None
    ruleConfiguration: Optional[RuleConfigurationOutput] = None


class ContentRetrievalRuleUnion(BaseValidatorModel):
    pass


class RuleConfiguration(BaseValidatorModel):
    contentBlockerRule: Optional[ContentBlockerRule] = None
    contentRetrievalRule: Optional[ContentRetrievalRuleUnion] = None


class AttachmentInputEvent(BaseValidatorModel):
    attachment: Optional[AttachmentInput] = None


class ListAttachmentsResponse(BaseValidatorModel):
    attachments: List[Attachment]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RetrieverConfigurationOutput(BaseValidatorModel):
    nativeIndexConfiguration: Optional[NativeIndexConfigurationOutput] = None
    kendraIndexConfiguration: Optional[KendraIndexConfiguration] = None


class RetrieverConfiguration(BaseValidatorModel):
    nativeIndexConfiguration: Optional[NativeIndexConfiguration] = None
    kendraIndexConfiguration: Optional[KendraIndexConfiguration] = None


class ActionFilterConfigurationOutput(BaseValidatorModel):
    documentAttributeFilter: AttributeFilterOutput


class SearchRelevantContentResponse(BaseValidatorModel):
    relevantContent: List[RelevantContent]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class DocumentEnrichmentConfigurationOutput(BaseValidatorModel):
    inlineConfigurations: Optional[List[InlineDocumentEnrichmentConfigurationOutput]] = None
    preExtractionHookConfiguration: Optional[HookConfigurationOutput] = None
    postExtractionHookConfiguration: Optional[HookConfigurationOutput] = None


class DocumentAttributeValueUnion(BaseValidatorModel):
    pass


class DocumentAttributeTarget(BaseValidatorModel):
    key: str
    value: Optional[DocumentAttributeValueUnion] = None
    attributeValueOperator: Optional[Literal["DELETE"]] = None


class DocumentAttribute(BaseValidatorModel):
    name: str
    value: DocumentAttributeValueUnion


class PluginAuthConfigurationUnion(BaseValidatorModel):
    pass


class UpdatePluginRequest(BaseValidatorModel):
    applicationId: str
    pluginId: str
    displayName: Optional[str] = None
    state: Optional[PluginStateType] = None
    serverUrl: Optional[str] = None
    customPluginConfiguration: Optional[CustomPluginConfiguration] = None
    authConfiguration: Optional[PluginAuthConfigurationUnion] = None


class AccessConfiguration(BaseValidatorModel):
    accessControls: Sequence[AccessControl]
    memberRelation: Optional[MemberRelationType] = None


class SourceAttribution(BaseValidatorModel):
    title: Optional[str] = None
    snippet: Optional[str] = None
    url: Optional[str] = None
    citationNumber: Optional[int] = None
    updatedAt: Optional[datetime] = None
    textMessageSegments: Optional[List[TextSegment]] = None


class TopicConfigurationOutput(BaseValidatorModel):
    name: str
    rules: List[RuleOutput]
    description: Optional[str] = None
    exampleChatMessages: Optional[List[str]] = None


class ActionConfigurationOutput(BaseValidatorModel):
    action: str
    filterConfiguration: Optional[ActionFilterConfigurationOutput] = None


class ChatSyncOutput(BaseValidatorModel):
    conversationId: str
    systemMessage: str
    systemMessageId: str
    userMessageId: str
    actionReview: ActionReview
    authChallengeRequest: AuthChallengeRequest
    sourceAttributions: List[SourceAttribution]
    failedAttachments: List[AttachmentOutput]
    ResponseMetadata: ResponseMetadata


class MetadataEvent(BaseValidatorModel):
    conversationId: Optional[str] = None
    userMessageId: Optional[str] = None
    systemMessageId: Optional[str] = None
    sourceAttributions: Optional[List[SourceAttribution]] = None
    finalTextMessage: Optional[str] = None


class GetChatControlsConfigurationResponse(BaseValidatorModel):
    responseScope: ResponseScopeType
    orchestrationConfiguration: AppliedOrchestrationConfiguration
    blockedPhrases: BlockedPhrasesConfiguration
    topicConfigurations: List[TopicConfigurationOutput]
    creatorModeConfiguration: AppliedCreatorModeConfiguration
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class UsersAndGroupsUnion(BaseValidatorModel):
    pass


class RuleConfigurationUnion(BaseValidatorModel):
    pass


class Rule(BaseValidatorModel):
    ruleType: RuleTypeType
    includedUsersAndGroups: Optional[UsersAndGroupsUnion] = None
    excludedUsersAndGroups: Optional[UsersAndGroupsUnion] = None
    ruleConfiguration: Optional[RuleConfigurationUnion] = None


class RetrieverConfigurationUnion(BaseValidatorModel):
    pass


class UpdateRetrieverRequest(BaseValidatorModel):
    applicationId: str
    retrieverId: str
    configuration: Optional[RetrieverConfigurationUnion] = None
    displayName: Optional[str] = None
    roleArn: Optional[str] = None


class GetDataAccessorResponse(BaseValidatorModel):
    displayName: str
    dataAccessorId: str
    dataAccessorArn: str
    applicationId: str
    idcApplicationArn: str
    principal: str
    actionConfigurations: List[ActionConfigurationOutput]
    createdAt: datetime
    updatedAt: datetime
    ResponseMetadata: ResponseMetadata


class DocumentAttributeConditionUnion(BaseValidatorModel):
    pass


class HookConfiguration(BaseValidatorModel):
    invocationCondition: Optional[DocumentAttributeConditionUnion] = None
    lambdaArn: Optional[str] = None
    s3BucketName: Optional[str] = None
    roleArn: Optional[str] = None


class DocumentAttributeTargetUnion(BaseValidatorModel):
    pass


class InlineDocumentEnrichmentConfiguration(BaseValidatorModel):
    condition: Optional[DocumentAttributeConditionUnion] = None
    target: Optional[DocumentAttributeTargetUnion] = None
    documentContentOperator: Optional[Literal["DELETE"]] = None


class DocumentAttributeUnion(BaseValidatorModel):
    pass


class AttributeFilterPaginator(BaseValidatorModel):
    andAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    orAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    notFilter: Optional[Mapping[str, Any]] = None
    equalsTo: Optional[DocumentAttributeUnion] = None
    containsAll: Optional[DocumentAttributeUnion] = None
    containsAny: Optional[DocumentAttributeUnion] = None
    greaterThan: Optional[DocumentAttributeUnion] = None
    greaterThanOrEquals: Optional[DocumentAttributeUnion] = None
    lessThan: Optional[DocumentAttributeUnion] = None
    lessThanOrEquals: Optional[DocumentAttributeUnion] = None


class AttributeFilter(BaseValidatorModel):
    andAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    orAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    notFilter: Optional[Mapping[str, Any]] = None
    equalsTo: Optional[DocumentAttributeUnion] = None
    containsAll: Optional[DocumentAttributeUnion] = None
    containsAny: Optional[DocumentAttributeUnion] = None
    greaterThan: Optional[DocumentAttributeUnion] = None
    greaterThanOrEquals: Optional[DocumentAttributeUnion] = None
    lessThan: Optional[DocumentAttributeUnion] = None
    lessThanOrEquals: Optional[DocumentAttributeUnion] = None


class Message(BaseValidatorModel):
    pass


class ListMessagesResponse(BaseValidatorModel):
    messages: List[Message]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ChatOutputStream(BaseValidatorModel):
    textEvent: Optional[TextOutputEvent] = None
    metadataEvent: Optional[MetadataEvent] = None
    actionReviewEvent: Optional[ActionReviewEvent] = None
    failedAttachmentEvent: Optional[FailedAttachmentEvent] = None
    authChallengeRequestEvent: Optional[AuthChallengeRequestEvent] = None


class SearchRelevantContentRequestPaginate(BaseValidatorModel):
    applicationId: str
    queryText: str
    contentSource: ContentSource
    attributeFilter: Optional[AttributeFilterPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ChatOutput(BaseValidatorModel):
    outputStream: EventStream[ChatOutputStream]
    ResponseMetadata: ResponseMetadata


class RuleUnion(BaseValidatorModel):
    pass


class TopicConfiguration(BaseValidatorModel):
    name: str
    rules: Sequence[RuleUnion]
    description: Optional[str] = None
    exampleChatMessages: Optional[Sequence[str]] = None


class InlineDocumentEnrichmentConfigurationUnion(BaseValidatorModel):
    pass


class HookConfigurationUnion(BaseValidatorModel):
    pass


class DocumentEnrichmentConfiguration(BaseValidatorModel):
    inlineConfigurations: Optional[Sequence[InlineDocumentEnrichmentConfigurationUnion]] = None
    preExtractionHookConfiguration: Optional[HookConfigurationUnion] = None
    postExtractionHookConfiguration: Optional[HookConfigurationUnion] = None


class AttributeFilterUnion(BaseValidatorModel):
    pass


class ActionFilterConfiguration(BaseValidatorModel):
    documentAttributeFilter: AttributeFilterUnion


class ActionExecutionUnion(BaseValidatorModel):
    pass


class ChatSyncInput(BaseValidatorModel):
    applicationId: str
    userId: Optional[str] = None
    userGroups: Optional[Sequence[str]] = None
    userMessage: Optional[str] = None
    attachments: Optional[Sequence[AttachmentInput]] = None
    actionExecution: Optional[ActionExecutionUnion] = None
    authChallengeResponse: Optional[AuthChallengeResponse] = None
    conversationId: Optional[str] = None
    parentMessageId: Optional[str] = None
    attributeFilter: Optional[AttributeFilterUnion] = None
    chatMode: Optional[ChatModeType] = None
    chatModeConfiguration: Optional[ChatModeConfiguration] = None
    clientToken: Optional[str] = None


class ConfigurationEvent(BaseValidatorModel):
    chatMode: Optional[ChatModeType] = None
    chatModeConfiguration: Optional[ChatModeConfiguration] = None
    attributeFilter: Optional[AttributeFilterUnion] = None


class SearchRelevantContentRequest(BaseValidatorModel):
    applicationId: str
    queryText: str
    contentSource: ContentSource
    attributeFilter: Optional[AttributeFilterUnion] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ChatInputStream(BaseValidatorModel):
    configurationEvent: Optional[ConfigurationEvent] = None
    textEvent: Optional[TextInputEvent] = None
    attachmentEvent: Optional[AttachmentInputEvent] = None
    actionExecutionEvent: Optional[ActionExecutionEvent] = None
    endOfInputEvent: Optional[Mapping[str, Any]] = None
    authChallengeResponseEvent: Optional[AuthChallengeResponseEvent] = None


class TopicConfigurationUnion(BaseValidatorModel):
    pass


class UpdateChatControlsConfigurationRequest(BaseValidatorModel):
    applicationId: str
    clientToken: Optional[str] = None
    responseScope: Optional[ResponseScopeType] = None
    orchestrationConfiguration: Optional[OrchestrationConfiguration] = None
    blockedPhrasesConfigurationUpdate: Optional[BlockedPhrasesConfigurationUpdate] = None
    topicConfigurationsToCreateOrUpdate: Optional[Sequence[TopicConfigurationUnion]] = None
    topicConfigurationsToDelete: Optional[Sequence[TopicConfigurationUnion]] = None
    creatorModeConfiguration: Optional[CreatorModeConfiguration] = None


class DataSourceVpcConfigurationUnion(BaseValidatorModel):
    pass


class DocumentEnrichmentConfigurationUnion(BaseValidatorModel):
    pass


class CreateDataSourceRequest(BaseValidatorModel):
    applicationId: str
    indexId: str
    displayName: str
    configuration: Mapping[str, Any]
    vpcConfiguration: Optional[DataSourceVpcConfigurationUnion] = None
    description: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None
    syncSchedule: Optional[str] = None
    roleArn: Optional[str] = None
    clientToken: Optional[str] = None
    documentEnrichmentConfiguration: Optional[DocumentEnrichmentConfigurationUnion] = None
    mediaExtractionConfiguration: Optional[MediaExtractionConfiguration] = None


class UpdateDataSourceRequest(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceId: str
    displayName: Optional[str] = None
    configuration: Optional[Mapping[str, Any]] = None
    vpcConfiguration: Optional[DataSourceVpcConfigurationUnion] = None
    description: Optional[str] = None
    syncSchedule: Optional[str] = None
    roleArn: Optional[str] = None
    documentEnrichmentConfiguration: Optional[DocumentEnrichmentConfigurationUnion] = None
    mediaExtractionConfiguration: Optional[MediaExtractionConfiguration] = None


class ActionFilterConfigurationUnion(BaseValidatorModel):
    pass


class ActionConfiguration(BaseValidatorModel):
    action: str
    filterConfiguration: Optional[ActionFilterConfigurationUnion] = None


class ChatInput(BaseValidatorModel):
    applicationId: str
    userId: Optional[str] = None
    userGroups: Optional[Sequence[str]] = None
    conversationId: Optional[str] = None
    parentMessageId: Optional[str] = None
    clientToken: Optional[str] = None
    inputStream: Optional[EventStream[ChatInputStream]] = None


class Document(BaseValidatorModel):
    pass


class BatchPutDocumentRequest(BaseValidatorModel):
    applicationId: str
    indexId: str
    documents: Sequence[Document]
    roleArn: Optional[str] = None
    dataSourceSyncId: Optional[str] = None


class ActionConfigurationUnion(BaseValidatorModel):
    pass


class CreateDataAccessorRequest(BaseValidatorModel):
    applicationId: str
    principal: str
    actionConfigurations: Sequence[ActionConfigurationUnion]
    displayName: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[Tag]] = None


class UpdateDataAccessorRequest(BaseValidatorModel):
    applicationId: str
    dataAccessorId: str
    actionConfigurations: Sequence[ActionConfigurationUnion]
    displayName: Optional[str] = None


