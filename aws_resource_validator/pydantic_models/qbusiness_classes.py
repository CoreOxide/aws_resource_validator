from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.eventstream import EventStream
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

class S3TypeDef(BaseValidatorModel):
    bucket: str
    key: str


class ActionExecutionPayloadFieldOutputTypeDef(BaseValidatorModel):
    value: Dict[str, Any]


class ActionExecutionPayloadFieldTypeDef(BaseValidatorModel):
    value: Mapping[str, Any]


class ActionReviewPayloadFieldAllowedValueTypeDef(BaseValidatorModel):
    value: Optional[Dict[str, Any]] = None
    displayValue: Optional[Dict[str, Any]] = None


class ActionSummaryTypeDef(BaseValidatorModel):
    actionIdentifier: Optional[str] = None
    displayName: Optional[str] = None
    instructionExample: Optional[str] = None
    description: Optional[str] = None


class QuickSightConfigurationTypeDef(BaseValidatorModel):
    clientNamespace: str


class AppliedAttachmentsConfigurationTypeDef(BaseValidatorModel):
    attachmentsControlMode: Optional[AttachmentsControlModeType] = None


class AppliedCreatorModeConfigurationTypeDef(BaseValidatorModel):
    creatorModeControl: CreatorModeControlType


class AppliedOrchestrationConfigurationTypeDef(BaseValidatorModel):
    control: OrchestrationControlType


class AssociatePermissionRequestTypeDef(BaseValidatorModel):
    applicationId: str
    statementId: str
    actions: Sequence[str]
    principal: str


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class ErrorDetailTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None


class AttachmentsConfigurationTypeDef(BaseValidatorModel):
    attachmentsControlMode: AttachmentsControlModeType


class AudioExtractionConfigurationTypeDef(BaseValidatorModel):
    audioExtractionStatus: AudioExtractionStatusType


class AudioSourceDetailsTypeDef(BaseValidatorModel):
    mediaId: Optional[str] = None
    mediaMimeType: Optional[str] = None
    startTimeMilliseconds: Optional[int] = None
    endTimeMilliseconds: Optional[int] = None
    audioExtractionType: Optional[AudioExtractionTypeType] = None


class AuthChallengeRequestEventTypeDef(BaseValidatorModel):
    authorizationUrl: str


class AuthChallengeRequestTypeDef(BaseValidatorModel):
    authorizationUrl: str


class AuthChallengeResponseEventTypeDef(BaseValidatorModel):
    responseMap: Mapping[str, str]


class AuthChallengeResponseTypeDef(BaseValidatorModel):
    responseMap: Mapping[str, str]


class AutoSubscriptionConfigurationTypeDef(BaseValidatorModel):
    autoSubscribe: AutoSubscriptionStatusType
    defaultSubscriptionType: Optional[SubscriptionTypeType] = None


class BasicAuthConfigurationTypeDef(BaseValidatorModel):
    secretArn: str
    roleArn: str


class DeleteDocumentTypeDef(BaseValidatorModel):
    documentId: str


class BlockedPhrasesConfigurationTypeDef(BaseValidatorModel):
    blockedPhrases: Optional[List[str]] = None
    systemMessageOverride: Optional[str] = None


class BlockedPhrasesConfigurationUpdateTypeDef(BaseValidatorModel):
    blockedPhrasesToCreateOrUpdate: Optional[Sequence[str]] = None
    blockedPhrasesToDelete: Optional[Sequence[str]] = None
    systemMessageOverride: Optional[str] = None


class BrowserExtensionConfigurationOutputTypeDef(BaseValidatorModel):
    enabledBrowserExtensions: List[BrowserExtensionType]


class BrowserExtensionConfigurationTypeDef(BaseValidatorModel):
    enabledBrowserExtensions: Sequence[BrowserExtensionType]


class CancelSubscriptionRequestTypeDef(BaseValidatorModel):
    applicationId: str
    subscriptionId: str


class TextInputEventTypeDef(BaseValidatorModel):
    userMessage: str


class PluginConfigurationTypeDef(BaseValidatorModel):
    pluginId: str


class TextOutputEventTypeDef(BaseValidatorModel):
    conversationId: Optional[str] = None
    userMessageId: Optional[str] = None
    systemMessageId: Optional[str] = None
    systemMessage: Optional[str] = None


class ContentBlockerRuleTypeDef(BaseValidatorModel):
    systemMessageOverride: Optional[str] = None


class EligibleDataSourceTypeDef(BaseValidatorModel):
    indexId: Optional[str] = None
    dataSourceId: Optional[str] = None


class RetrieverContentSourceTypeDef(BaseValidatorModel):
    retrieverId: str


class ConversationSourceTypeDef(BaseValidatorModel):
    conversationId: str
    attachmentId: str


class ConversationTypeDef(BaseValidatorModel):
    conversationId: Optional[str] = None
    title: Optional[str] = None
    startTime: Optional[datetime] = None


class EncryptionConfigurationTypeDef(BaseValidatorModel):
    kmsKeyId: Optional[str] = None


class PersonalizationConfigurationTypeDef(BaseValidatorModel):
    personalizationControlMode: PersonalizationControlModeType


class QAppsConfigurationTypeDef(BaseValidatorModel):
    qAppsControlMode: QAppsControlModeType


class TagTypeDef(BaseValidatorModel):
    key: str
    value: str


class IndexCapacityConfigurationTypeDef(BaseValidatorModel):
    units: Optional[int] = None


class SubscriptionPrincipalTypeDef(BaseValidatorModel):
    user: Optional[str] = None
    group: Optional[str] = None


class UserAliasTypeDef(BaseValidatorModel):
    userId: str
    indexId: Optional[str] = None
    dataSourceId: Optional[str] = None


class CustomizationConfigurationTypeDef(BaseValidatorModel):
    customCSSUrl: Optional[str] = None
    logoUrl: Optional[str] = None
    fontUrl: Optional[str] = None
    faviconUrl: Optional[str] = None


class CreatorModeConfigurationTypeDef(BaseValidatorModel):
    creatorModeControl: CreatorModeControlType


class DataAccessorTypeDef(BaseValidatorModel):
    displayName: Optional[str] = None
    dataAccessorId: Optional[str] = None
    dataAccessorArn: Optional[str] = None
    idcApplicationArn: Optional[str] = None
    principal: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class DataSourceSyncJobMetricsTypeDef(BaseValidatorModel):
    documentsAdded: Optional[str] = None
    documentsModified: Optional[str] = None
    documentsDeleted: Optional[str] = None
    documentsFailed: Optional[str] = None
    documentsScanned: Optional[str] = None


class DataSourceVpcConfigurationOutputTypeDef(BaseValidatorModel):
    subnetIds: List[str]
    securityGroupIds: List[str]


class DataSourceVpcConfigurationTypeDef(BaseValidatorModel):
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]


class DateAttributeBoostingConfigurationTypeDef(BaseValidatorModel):
    boostingLevel: DocumentAttributeBoostingLevelType
    boostingDurationInSeconds: Optional[int] = None


class DeleteApplicationRequestTypeDef(BaseValidatorModel):
    applicationId: str


class DeleteAttachmentRequestTypeDef(BaseValidatorModel):
    applicationId: str
    conversationId: str
    attachmentId: str
    userId: Optional[str] = None


class DeleteChatControlsConfigurationRequestTypeDef(BaseValidatorModel):
    applicationId: str


class DeleteConversationRequestTypeDef(BaseValidatorModel):
    conversationId: str
    applicationId: str
    userId: Optional[str] = None


class DeleteDataAccessorRequestTypeDef(BaseValidatorModel):
    applicationId: str
    dataAccessorId: str


class DeleteDataSourceRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceId: str


class DeleteGroupRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    groupName: str
    dataSourceId: Optional[str] = None


class DeleteIndexRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str


class DeletePluginRequestTypeDef(BaseValidatorModel):
    applicationId: str
    pluginId: str


class DeleteRetrieverRequestTypeDef(BaseValidatorModel):
    applicationId: str
    retrieverId: str


class DeleteUserRequestTypeDef(BaseValidatorModel):
    applicationId: str
    userId: str


class DeleteWebExperienceRequestTypeDef(BaseValidatorModel):
    applicationId: str
    webExperienceId: str


class DisassociatePermissionRequestTypeDef(BaseValidatorModel):
    applicationId: str
    statementId: str


class NumberAttributeBoostingConfigurationTypeDef(BaseValidatorModel):
    boostingLevel: DocumentAttributeBoostingLevelType
    boostingType: Optional[NumberAttributeBoostingTypeType] = None


class StringAttributeBoostingConfigurationOutputTypeDef(BaseValidatorModel):
    boostingLevel: DocumentAttributeBoostingLevelType
    attributeValueBoosting: Optional[Dict[str, StringAttributeValueBoostingLevelType]] = None


class StringListAttributeBoostingConfigurationTypeDef(BaseValidatorModel):
    boostingLevel: DocumentAttributeBoostingLevelType


class StringAttributeBoostingConfigurationTypeDef(BaseValidatorModel):
    boostingLevel: DocumentAttributeBoostingLevelType
    attributeValueBoosting: Optional[Mapping[str, StringAttributeValueBoostingLevelType]] = None


class DocumentAttributeValueOutputTypeDef(BaseValidatorModel):
    stringValue: Optional[str] = None
    stringListValue: Optional[List[str]] = None
    longValue: Optional[int] = None
    dateValue: Optional[datetime] = None


class GetApplicationRequestTypeDef(BaseValidatorModel):
    applicationId: str


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class GetChatControlsConfigurationRequestTypeDef(BaseValidatorModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class GetDataAccessorRequestTypeDef(BaseValidatorModel):
    applicationId: str
    dataAccessorId: str


class GetDataSourceRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceId: str


class GetGroupRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    groupName: str
    dataSourceId: Optional[str] = None


class GetIndexRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str


class GetMediaRequestTypeDef(BaseValidatorModel):
    applicationId: str
    conversationId: str
    messageId: str
    mediaId: str


class GetPluginRequestTypeDef(BaseValidatorModel):
    applicationId: str
    pluginId: str


class GetPolicyRequestTypeDef(BaseValidatorModel):
    applicationId: str


class GetRetrieverRequestTypeDef(BaseValidatorModel):
    applicationId: str
    retrieverId: str


class GetUserRequestTypeDef(BaseValidatorModel):
    applicationId: str
    userId: str


class GetWebExperienceRequestTypeDef(BaseValidatorModel):
    applicationId: str
    webExperienceId: str


class GroupSummaryTypeDef(BaseValidatorModel):
    groupName: Optional[str] = None


class IdcAuthConfigurationTypeDef(BaseValidatorModel):
    idcApplicationArn: str
    roleArn: str


class OpenIDConnectProviderConfigurationTypeDef(BaseValidatorModel):
    secretsArn: str
    secretsRole: str


class SamlProviderConfigurationTypeDef(BaseValidatorModel):
    authenticationUrl: str


class ImageExtractionConfigurationTypeDef(BaseValidatorModel):
    imageExtractionStatus: ImageExtractionStatusType


class ImageSourceDetailsTypeDef(BaseValidatorModel):
    mediaId: Optional[str] = None
    mediaMimeType: Optional[str] = None


class TextDocumentStatisticsTypeDef(BaseValidatorModel):
    indexedTextBytes: Optional[int] = None
    indexedTextDocumentCount: Optional[int] = None


class IndexTypeDef(BaseValidatorModel):
    displayName: Optional[str] = None
    indexId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    status: Optional[IndexStatusType] = None


class KendraIndexConfigurationTypeDef(BaseValidatorModel):
    indexId: str


class ListApplicationsRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListAttachmentsRequestTypeDef(BaseValidatorModel):
    applicationId: str
    conversationId: Optional[str] = None
    userId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListConversationsRequestTypeDef(BaseValidatorModel):
    applicationId: str
    userId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDataAccessorsRequestTypeDef(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDataSourcesRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListDocumentsRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListIndicesRequestTypeDef(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListMessagesRequestTypeDef(BaseValidatorModel):
    conversationId: str
    applicationId: str
    userId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPluginActionsRequestTypeDef(BaseValidatorModel):
    applicationId: str
    pluginId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPluginTypeActionsRequestTypeDef(BaseValidatorModel):
    pluginType: PluginTypeType
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPluginTypeMetadataRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListPluginsRequestTypeDef(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListRetrieversRequestTypeDef(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListSubscriptionsRequestTypeDef(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str


class ListWebExperiencesRequestTypeDef(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class WebExperienceTypeDef(BaseValidatorModel):
    webExperienceId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    defaultEndpoint: Optional[str] = None
    status: Optional[WebExperienceStatusType] = None


class VideoExtractionConfigurationTypeDef(BaseValidatorModel):
    videoExtractionStatus: VideoExtractionStatusType


class OAuth2ClientCredentialConfigurationTypeDef(BaseValidatorModel):
    secretArn: str
    roleArn: str
    authorizationUrl: Optional[str] = None
    tokenUrl: Optional[str] = None


class OrchestrationConfigurationTypeDef(BaseValidatorModel):
    control: OrchestrationControlType


class PrincipalGroupTypeDef(BaseValidatorModel):
    access: ReadAccessTypeType
    name: Optional[str] = None
    membershipType: Optional[MembershipTypeType] = None


class ScoreAttributesTypeDef(BaseValidatorModel):
    scoreConfidence: Optional[ScoreConfidenceType] = None


class UsersAndGroupsOutputTypeDef(BaseValidatorModel):
    userIds: Optional[List[str]] = None
    userGroups: Optional[List[str]] = None


class SamlConfigurationTypeDef(BaseValidatorModel):
    metadataXML: str
    roleArn: str
    userIdAttribute: str
    userGroupAttribute: Optional[str] = None


class SnippetExcerptTypeDef(BaseValidatorModel):
    text: Optional[str] = None


class VideoSourceDetailsTypeDef(BaseValidatorModel):
    mediaId: Optional[str] = None
    mediaMimeType: Optional[str] = None
    startTimeMilliseconds: Optional[int] = None
    endTimeMilliseconds: Optional[int] = None
    videoExtractionType: Optional[VideoExtractionTypeType] = None


class StartDataSourceSyncJobRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    applicationId: str
    indexId: str


class StopDataSourceSyncJobRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    applicationId: str
    indexId: str


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]


class UsersAndGroupsTypeDef(BaseValidatorModel):
    userIds: Optional[Sequence[str]] = None
    userGroups: Optional[Sequence[str]] = None


class APISchemaTypeDef(BaseValidatorModel):
    payload: Optional[str] = None
    s3: Optional[S3TypeDef] = None


class ActionExecutionOutputTypeDef(BaseValidatorModel):
    pluginId: str
    payload: Dict[str, ActionExecutionPayloadFieldOutputTypeDef]
    payloadFieldNameSeparator: str


class ActionExecutionTypeDef(BaseValidatorModel):
    pluginId: str
    payload: Mapping[str, ActionExecutionPayloadFieldTypeDef]
    payloadFieldNameSeparator: str


class ApplicationTypeDef(BaseValidatorModel):
    displayName: Optional[str] = None
    applicationId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    status: Optional[ApplicationStatusType] = None
    identityType: Optional[IdentityTypeType] = None
    quickSightConfiguration: Optional[QuickSightConfigurationTypeDef] = None


class AssociatePermissionResponseTypeDef(BaseValidatorModel):
    statement: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateApplicationResponseTypeDef(BaseValidatorModel):
    applicationId: str
    applicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataAccessorResponseTypeDef(BaseValidatorModel):
    dataAccessorId: str
    idcApplicationArn: str
    dataAccessorArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateDataSourceResponseTypeDef(BaseValidatorModel):
    dataSourceId: str
    dataSourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateIndexResponseTypeDef(BaseValidatorModel):
    indexId: str
    indexArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreatePluginResponseTypeDef(BaseValidatorModel):
    pluginId: str
    pluginArn: str
    buildStatus: PluginBuildStatusType
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRetrieverResponseTypeDef(BaseValidatorModel):
    retrieverId: str
    retrieverArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateWebExperienceResponseTypeDef(BaseValidatorModel):
    webExperienceId: str
    webExperienceArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetMediaResponseTypeDef(BaseValidatorModel):
    mediaBytes: bytes
    mediaMimeType: str
    ResponseMetadata: ResponseMetadataTypeDef


class GetPolicyResponseTypeDef(BaseValidatorModel):
    policy: str
    ResponseMetadata: ResponseMetadataTypeDef


class ListPluginActionsResponseTypeDef(BaseValidatorModel):
    items: List[ActionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListPluginTypeActionsResponseTypeDef(BaseValidatorModel):
    items: List[ActionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class StartDataSourceSyncJobResponseTypeDef(BaseValidatorModel):
    executionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class BlobTypeDef(BaseValidatorModel):
    pass


class DocumentContentTypeDef(BaseValidatorModel):
    blob: Optional[BlobTypeDef] = None
    s3: Optional[S3TypeDef] = None


class AttachmentOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    status: Optional[AttachmentStatusType] = None
    error: Optional[ErrorDetailTypeDef] = None
    attachmentId: Optional[str] = None
    conversationId: Optional[str] = None


class DocumentDetailsTypeDef(BaseValidatorModel):
    documentId: Optional[str] = None
    status: Optional[DocumentStatusType] = None
    error: Optional[ErrorDetailTypeDef] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None


class GroupStatusDetailTypeDef(BaseValidatorModel):
    status: Optional[GroupStatusType] = None
    lastUpdatedAt: Optional[datetime] = None
    errorDetail: Optional[ErrorDetailTypeDef] = None


class BatchDeleteDocumentRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    documents: Sequence[DeleteDocumentTypeDef]
    dataSourceSyncId: Optional[str] = None


class SubscriptionDetailsTypeDef(BaseValidatorModel):
    pass


class CancelSubscriptionResponseTypeDef(BaseValidatorModel):
    subscriptionArn: str
    currentSubscription: SubscriptionDetailsTypeDef
    nextSubscription: SubscriptionDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateSubscriptionResponseTypeDef(BaseValidatorModel):
    subscriptionId: str
    subscriptionArn: str
    currentSubscription: SubscriptionDetailsTypeDef
    nextSubscription: SubscriptionDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateSubscriptionResponseTypeDef(BaseValidatorModel):
    subscriptionArn: str
    currentSubscription: SubscriptionDetailsTypeDef
    nextSubscription: SubscriptionDetailsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ChatModeConfigurationTypeDef(BaseValidatorModel):
    pluginConfiguration: Optional[PluginConfigurationTypeDef] = None


class ContentRetrievalRuleOutputTypeDef(BaseValidatorModel):
    eligibleDataSources: Optional[List[EligibleDataSourceTypeDef]] = None


class ContentRetrievalRuleTypeDef(BaseValidatorModel):
    eligibleDataSources: Optional[Sequence[EligibleDataSourceTypeDef]] = None


class ContentSourceTypeDef(BaseValidatorModel):
    retriever: Optional[RetrieverContentSourceTypeDef] = None


class CopyFromSourceTypeDef(BaseValidatorModel):
    conversation: Optional[ConversationSourceTypeDef] = None


class ListConversationsResponseTypeDef(BaseValidatorModel):
    conversations: List[ConversationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class GetApplicationResponseTypeDef(BaseValidatorModel):
    displayName: str
    applicationId: str
    applicationArn: str
    identityType: IdentityTypeType
    iamIdentityProviderArn: str
    identityCenterApplicationArn: str
    roleArn: str
    status: ApplicationStatusType
    description: str
    encryptionConfiguration: EncryptionConfigurationTypeDef
    createdAt: datetime
    updatedAt: datetime
    error: ErrorDetailTypeDef
    attachmentsConfiguration: AppliedAttachmentsConfigurationTypeDef
    qAppsConfiguration: QAppsConfigurationTypeDef
    personalizationConfiguration: PersonalizationConfigurationTypeDef
    autoSubscriptionConfiguration: AutoSubscriptionConfigurationTypeDef
    clientIdsForOIDC: List[str]
    quickSightConfiguration: QuickSightConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateApplicationRequestTypeDef(BaseValidatorModel):
    applicationId: str
    identityCenterInstanceArn: Optional[str] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    roleArn: Optional[str] = None
    attachmentsConfiguration: Optional[AttachmentsConfigurationTypeDef] = None
    qAppsConfiguration: Optional[QAppsConfigurationTypeDef] = None
    personalizationConfiguration: Optional[PersonalizationConfigurationTypeDef] = None
    autoSubscriptionConfiguration: Optional[AutoSubscriptionConfigurationTypeDef] = None


class CreateApplicationRequestTypeDef(BaseValidatorModel):
    displayName: str
    roleArn: Optional[str] = None
    identityType: Optional[IdentityTypeType] = None
    iamIdentityProviderArn: Optional[str] = None
    identityCenterInstanceArn: Optional[str] = None
    clientIdsForOIDC: Optional[Sequence[str]] = None
    description: Optional[str] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    clientToken: Optional[str] = None
    attachmentsConfiguration: Optional[AttachmentsConfigurationTypeDef] = None
    qAppsConfiguration: Optional[QAppsConfigurationTypeDef] = None
    personalizationConfiguration: Optional[PersonalizationConfigurationTypeDef] = None
    quickSightConfiguration: Optional[QuickSightConfigurationTypeDef] = None


class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tags: Sequence[TagTypeDef]


class SubscriptionTypeDef(BaseValidatorModel):
    subscriptionId: Optional[str] = None
    subscriptionArn: Optional[str] = None
    principal: Optional[SubscriptionPrincipalTypeDef] = None
    currentSubscription: Optional[SubscriptionDetailsTypeDef] = None
    nextSubscription: Optional[SubscriptionDetailsTypeDef] = None


class CreateUserRequestTypeDef(BaseValidatorModel):
    applicationId: str
    userId: str
    userAliases: Optional[Sequence[UserAliasTypeDef]] = None
    clientToken: Optional[str] = None


class GetUserResponseTypeDef(BaseValidatorModel):
    userAliases: List[UserAliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateUserRequestTypeDef(BaseValidatorModel):
    applicationId: str
    userId: str
    userAliasesToUpdate: Optional[Sequence[UserAliasTypeDef]] = None
    userAliasesToDelete: Optional[Sequence[UserAliasTypeDef]] = None


class UpdateUserResponseTypeDef(BaseValidatorModel):
    userAliasesAdded: List[UserAliasTypeDef]
    userAliasesUpdated: List[UserAliasTypeDef]
    userAliasesDeleted: List[UserAliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListDataAccessorsResponseTypeDef(BaseValidatorModel):
    dataAccessors: List[DataAccessorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DataSourceSyncJobTypeDef(BaseValidatorModel):
    executionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    status: Optional[DataSourceSyncJobStatusType] = None
    error: Optional[ErrorDetailTypeDef] = None
    dataSourceErrorCode: Optional[str] = None
    metrics: Optional[DataSourceSyncJobMetricsTypeDef] = None


class DataSourceTypeDef(BaseValidatorModel):
    pass


class ListDataSourcesResponseTypeDef(BaseValidatorModel):
    dataSources: List[DataSourceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DocumentAttributeBoostingConfigurationOutputTypeDef(BaseValidatorModel):
    numberConfiguration: Optional[NumberAttributeBoostingConfigurationTypeDef] = None
    stringConfiguration: Optional[StringAttributeBoostingConfigurationOutputTypeDef] = None
    dateConfiguration: Optional[DateAttributeBoostingConfigurationTypeDef] = None
    stringListConfiguration: Optional[StringListAttributeBoostingConfigurationTypeDef] = None


class DocumentAttributeBoostingConfigurationTypeDef(BaseValidatorModel):
    numberConfiguration: Optional[NumberAttributeBoostingConfigurationTypeDef] = None
    stringConfiguration: Optional[StringAttributeBoostingConfigurationTypeDef] = None
    dateConfiguration: Optional[DateAttributeBoostingConfigurationTypeDef] = None
    stringListConfiguration: Optional[StringListAttributeBoostingConfigurationTypeDef] = None


class DocumentAttributeOutputTypeDef(BaseValidatorModel):
    name: str
    value: DocumentAttributeValueOutputTypeDef


class DocumentAttributeTargetOutputTypeDef(BaseValidatorModel):
    key: str
    value: Optional[DocumentAttributeValueOutputTypeDef] = None
    attributeValueOperator: Optional[Literal["DELETE"]] = None


class DocumentAttributeConfigurationTypeDef(BaseValidatorModel):
    pass


class UpdateIndexRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    displayName: Optional[str] = None
    description: Optional[str] = None
    capacityConfiguration: Optional[IndexCapacityConfigurationTypeDef] = None
    documentAttributeConfigurations: Optional[Sequence[DocumentAttributeConfigurationTypeDef]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class DocumentAttributeValueTypeDef(BaseValidatorModel):
    stringValue: Optional[str] = None
    stringListValue: Optional[Sequence[str]] = None
    longValue: Optional[int] = None
    dateValue: Optional[TimestampTypeDef] = None


class ListDataSourceSyncJobsRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    applicationId: str
    indexId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    statusFilter: Optional[DataSourceSyncJobStatusType] = None


class ListGroupsRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    updatedEarlierThan: TimestampTypeDef
    dataSourceId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class MessageUsefulnessFeedbackTypeDef(BaseValidatorModel):
    usefulness: MessageUsefulnessType
    submittedAt: TimestampTypeDef
    reason: Optional[MessageUsefulnessReasonType] = None
    comment: Optional[str] = None


class GetChatControlsConfigurationRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApplicationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAttachmentsRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    conversationId: Optional[str] = None
    userId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListConversationsRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    userId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataAccessorsRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataSourceSyncJobsRequestPaginateTypeDef(BaseValidatorModel):
    dataSourceId: str
    applicationId: str
    indexId: str
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    statusFilter: Optional[DataSourceSyncJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDataSourcesRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDocumentsRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListGroupsRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    updatedEarlierThan: TimestampTypeDef
    dataSourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIndicesRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListMessagesRequestPaginateTypeDef(BaseValidatorModel):
    conversationId: str
    applicationId: str
    userId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPluginActionsRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    pluginId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPluginTypeActionsRequestPaginateTypeDef(BaseValidatorModel):
    pluginType: PluginTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPluginTypeMetadataRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPluginsRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRetrieversRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSubscriptionsRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListWebExperiencesRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class MemberUserTypeDef(BaseValidatorModel):
    pass


class MemberGroupTypeDef(BaseValidatorModel):
    pass


class GroupMembersTypeDef(BaseValidatorModel):
    memberGroups: Optional[Sequence[MemberGroupTypeDef]] = None
    memberUsers: Optional[Sequence[MemberUserTypeDef]] = None
    s3PathForGroupMembers: Optional[S3TypeDef] = None


class ListGroupsResponseTypeDef(BaseValidatorModel):
    items: List[GroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class IdentityProviderConfigurationTypeDef(BaseValidatorModel):
    samlConfiguration: Optional[SamlProviderConfigurationTypeDef] = None
    openIDConnectConfiguration: Optional[OpenIDConnectProviderConfigurationTypeDef] = None


class IndexStatisticsTypeDef(BaseValidatorModel):
    textDocumentStatistics: Optional[TextDocumentStatisticsTypeDef] = None


class ListIndicesResponseTypeDef(BaseValidatorModel):
    indices: List[IndexTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PluginTypeMetadataSummaryTypeDef(BaseValidatorModel):
    pass


class ListPluginTypeMetadataResponseTypeDef(BaseValidatorModel):
    items: List[PluginTypeMetadataSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class PluginTypeDef(BaseValidatorModel):
    pass


class ListPluginsResponseTypeDef(BaseValidatorModel):
    plugins: List[PluginTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RetrieverTypeDef(BaseValidatorModel):
    pass


class ListRetrieversResponseTypeDef(BaseValidatorModel):
    retrievers: List[RetrieverTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListWebExperiencesResponseTypeDef(BaseValidatorModel):
    webExperiences: List[WebExperienceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class MediaExtractionConfigurationTypeDef(BaseValidatorModel):
    imageExtractionConfiguration: Optional[ImageExtractionConfigurationTypeDef] = None
    audioExtractionConfiguration: Optional[AudioExtractionConfigurationTypeDef] = None
    videoExtractionConfiguration: Optional[VideoExtractionConfigurationTypeDef] = None


class PluginAuthConfigurationOutputTypeDef(BaseValidatorModel):
    basicAuthConfiguration: Optional[BasicAuthConfigurationTypeDef] = None
    oAuth2ClientCredentialConfiguration: Optional[OAuth2ClientCredentialConfigurationTypeDef] = None
    noAuthConfiguration: Optional[Dict[str, Any]] = None
    idcAuthConfiguration: Optional[IdcAuthConfigurationTypeDef] = None


class PluginAuthConfigurationTypeDef(BaseValidatorModel):
    basicAuthConfiguration: Optional[BasicAuthConfigurationTypeDef] = None
    oAuth2ClientCredentialConfiguration: Optional[OAuth2ClientCredentialConfigurationTypeDef] = None
    noAuthConfiguration: Optional[Mapping[str, Any]] = None
    idcAuthConfiguration: Optional[IdcAuthConfigurationTypeDef] = None


class PrincipalUserTypeDef(BaseValidatorModel):
    pass


class PrincipalTypeDef(BaseValidatorModel):
    user: Optional[PrincipalUserTypeDef] = None
    group: Optional[PrincipalGroupTypeDef] = None


class WebExperienceAuthConfigurationTypeDef(BaseValidatorModel):
    samlConfiguration: Optional[SamlConfigurationTypeDef] = None


class SourceDetailsTypeDef(BaseValidatorModel):
    imageSourceDetails: Optional[ImageSourceDetailsTypeDef] = None
    audioSourceDetails: Optional[AudioSourceDetailsTypeDef] = None
    videoSourceDetails: Optional[VideoSourceDetailsTypeDef] = None


class CustomPluginConfigurationTypeDef(BaseValidatorModel):
    description: str
    apiSchemaType: Literal["OPEN_API_V3"]
    apiSchema: APISchemaTypeDef


class ActionExecutionPayloadFieldUnionTypeDef(BaseValidatorModel):
    pass


class ActionExecutionEventTypeDef(BaseValidatorModel):
    pluginId: str
    payload: Mapping[str, ActionExecutionPayloadFieldUnionTypeDef]
    payloadFieldNameSeparator: str


class ActionReviewPayloadFieldTypeDef(BaseValidatorModel):
    pass


class ActionReviewEventTypeDef(BaseValidatorModel):
    conversationId: Optional[str] = None
    userMessageId: Optional[str] = None
    systemMessageId: Optional[str] = None
    pluginId: Optional[str] = None
    pluginType: Optional[PluginTypeType] = None
    payload: Optional[Dict[str, ActionReviewPayloadFieldTypeDef]] = None
    payloadFieldNameSeparator: Optional[str] = None


class ActionReviewTypeDef(BaseValidatorModel):
    pluginId: Optional[str] = None
    pluginType: Optional[PluginTypeType] = None
    payload: Optional[Dict[str, ActionReviewPayloadFieldTypeDef]] = None
    payloadFieldNameSeparator: Optional[str] = None


class ListApplicationsResponseTypeDef(BaseValidatorModel):
    applications: List[ApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FailedAttachmentEventTypeDef(BaseValidatorModel):
    conversationId: Optional[str] = None
    userMessageId: Optional[str] = None
    systemMessageId: Optional[str] = None
    attachment: Optional[AttachmentOutputTypeDef] = None


class ListDocumentsResponseTypeDef(BaseValidatorModel):
    documentDetailList: List[DocumentDetailsTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class FailedDocumentTypeDef(BaseValidatorModel):
    pass


class BatchDeleteDocumentResponseTypeDef(BaseValidatorModel):
    failedDocuments: List[FailedDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchPutDocumentResponseTypeDef(BaseValidatorModel):
    failedDocuments: List[FailedDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class GetGroupResponseTypeDef(BaseValidatorModel):
    status: GroupStatusDetailTypeDef
    statusHistory: List[GroupStatusDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RuleConfigurationOutputTypeDef(BaseValidatorModel):
    contentBlockerRule: Optional[ContentBlockerRuleTypeDef] = None
    contentRetrievalRule: Optional[ContentRetrievalRuleOutputTypeDef] = None


class AttachmentInputTypeDef(BaseValidatorModel):
    data: Optional[BlobTypeDef] = None
    name: Optional[str] = None
    copyFrom: Optional[CopyFromSourceTypeDef] = None


class AttachmentTypeDef(BaseValidatorModel):
    attachmentId: Optional[str] = None
    conversationId: Optional[str] = None
    name: Optional[str] = None
    copyFrom: Optional[CopyFromSourceTypeDef] = None
    fileType: Optional[str] = None
    fileSize: Optional[int] = None
    md5chksum: Optional[str] = None
    createdAt: Optional[datetime] = None
    status: Optional[AttachmentStatusType] = None
    error: Optional[ErrorDetailTypeDef] = None


class ListSubscriptionsResponseTypeDef(BaseValidatorModel):
    subscriptions: List[SubscriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListDataSourceSyncJobsResponseTypeDef(BaseValidatorModel):
    history: List[DataSourceSyncJobTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class NativeIndexConfigurationOutputTypeDef(BaseValidatorModel):
    indexId: str
    boostingOverride: Optional[Dict[str, DocumentAttributeBoostingConfigurationOutputTypeDef]] = None


class NativeIndexConfigurationTypeDef(BaseValidatorModel):
    indexId: str
    boostingOverride: Optional[Mapping[str, DocumentAttributeBoostingConfigurationTypeDef]] = None


class DocumentAttributeConditionOutputTypeDef(BaseValidatorModel):
    pass


class HookConfigurationOutputTypeDef(BaseValidatorModel):
    invocationCondition: Optional[DocumentAttributeConditionOutputTypeDef] = None
    lambdaArn: Optional[str] = None
    s3BucketName: Optional[str] = None
    roleArn: Optional[str] = None


class AttributeFilterOutputTypeDef(BaseValidatorModel):
    andAllFilters: Optional[List[Dict[str, Any]]] = None
    orAllFilters: Optional[List[Dict[str, Any]]] = None
    notFilter: Optional[Dict[str, Any]] = None
    equalsTo: Optional[DocumentAttributeOutputTypeDef] = None
    containsAll: Optional[DocumentAttributeOutputTypeDef] = None
    containsAny: Optional[DocumentAttributeOutputTypeDef] = None
    greaterThan: Optional[DocumentAttributeOutputTypeDef] = None
    greaterThanOrEquals: Optional[DocumentAttributeOutputTypeDef] = None
    lessThan: Optional[DocumentAttributeOutputTypeDef] = None
    lessThanOrEquals: Optional[DocumentAttributeOutputTypeDef] = None


class RelevantContentTypeDef(BaseValidatorModel):
    content: Optional[str] = None
    documentId: Optional[str] = None
    documentTitle: Optional[str] = None
    documentUri: Optional[str] = None
    documentAttributes: Optional[List[DocumentAttributeOutputTypeDef]] = None
    scoreAttributes: Optional[ScoreAttributesTypeDef] = None


class InlineDocumentEnrichmentConfigurationOutputTypeDef(BaseValidatorModel):
    condition: Optional[DocumentAttributeConditionOutputTypeDef] = None
    target: Optional[DocumentAttributeTargetOutputTypeDef] = None
    documentContentOperator: Optional[Literal["DELETE"]] = None


class PutFeedbackRequestTypeDef(BaseValidatorModel):
    applicationId: str
    conversationId: str
    messageId: str
    userId: Optional[str] = None
    messageCopiedAt: Optional[TimestampTypeDef] = None
    messageUsefulness: Optional[MessageUsefulnessFeedbackTypeDef] = None


class BrowserExtensionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateWebExperienceRequestTypeDef(BaseValidatorModel):
    applicationId: str
    title: Optional[str] = None
    subtitle: Optional[str] = None
    welcomeMessage: Optional[str] = None
    samplePromptsControlMode: Optional[WebExperienceSamplePromptsControlModeType] = None
    origins: Optional[Sequence[str]] = None
    roleArn: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    clientToken: Optional[str] = None
    identityProviderConfiguration: Optional[IdentityProviderConfigurationTypeDef] = None
    browserExtensionConfiguration: Optional[BrowserExtensionConfigurationUnionTypeDef] = None
    customizationConfiguration: Optional[CustomizationConfigurationTypeDef] = None


class AccessControlTypeDef(BaseValidatorModel):
    principals: Sequence[PrincipalTypeDef]
    memberRelation: Optional[MemberRelationType] = None


class GetWebExperienceResponseTypeDef(BaseValidatorModel):
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
    identityProviderConfiguration: IdentityProviderConfigurationTypeDef
    authenticationConfiguration: WebExperienceAuthConfigurationTypeDef
    error: ErrorDetailTypeDef
    browserExtensionConfiguration: BrowserExtensionConfigurationOutputTypeDef
    customizationConfiguration: CustomizationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateWebExperienceRequestTypeDef(BaseValidatorModel):
    applicationId: str
    webExperienceId: str
    roleArn: Optional[str] = None
    authenticationConfiguration: Optional[WebExperienceAuthConfigurationTypeDef] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    welcomeMessage: Optional[str] = None
    samplePromptsControlMode: Optional[WebExperienceSamplePromptsControlModeType] = None
    identityProviderConfiguration: Optional[IdentityProviderConfigurationTypeDef] = None
    origins: Optional[Sequence[str]] = None
    browserExtensionConfiguration: Optional[BrowserExtensionConfigurationUnionTypeDef] = None
    customizationConfiguration: Optional[CustomizationConfigurationTypeDef] = None


class TextSegmentTypeDef(BaseValidatorModel):
    beginOffset: Optional[int] = None
    endOffset: Optional[int] = None
    snippetExcerpt: Optional[SnippetExcerptTypeDef] = None
    mediaId: Optional[str] = None
    mediaMimeType: Optional[str] = None
    sourceDetails: Optional[SourceDetailsTypeDef] = None


class RuleOutputTypeDef(BaseValidatorModel):
    ruleType: RuleTypeType
    includedUsersAndGroups: Optional[UsersAndGroupsOutputTypeDef] = None
    excludedUsersAndGroups: Optional[UsersAndGroupsOutputTypeDef] = None
    ruleConfiguration: Optional[RuleConfigurationOutputTypeDef] = None


class ContentRetrievalRuleUnionTypeDef(BaseValidatorModel):
    pass


class RuleConfigurationTypeDef(BaseValidatorModel):
    contentBlockerRule: Optional[ContentBlockerRuleTypeDef] = None
    contentRetrievalRule: Optional[ContentRetrievalRuleUnionTypeDef] = None


class AttachmentInputEventTypeDef(BaseValidatorModel):
    attachment: Optional[AttachmentInputTypeDef] = None


class ListAttachmentsResponseTypeDef(BaseValidatorModel):
    attachments: List[AttachmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class RetrieverConfigurationOutputTypeDef(BaseValidatorModel):
    nativeIndexConfiguration: Optional[NativeIndexConfigurationOutputTypeDef] = None
    kendraIndexConfiguration: Optional[KendraIndexConfigurationTypeDef] = None


class RetrieverConfigurationTypeDef(BaseValidatorModel):
    nativeIndexConfiguration: Optional[NativeIndexConfigurationTypeDef] = None
    kendraIndexConfiguration: Optional[KendraIndexConfigurationTypeDef] = None


class ActionFilterConfigurationOutputTypeDef(BaseValidatorModel):
    documentAttributeFilter: AttributeFilterOutputTypeDef


class SearchRelevantContentResponseTypeDef(BaseValidatorModel):
    relevantContent: List[RelevantContentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class DocumentEnrichmentConfigurationOutputTypeDef(BaseValidatorModel):
    inlineConfigurations: Optional[List[InlineDocumentEnrichmentConfigurationOutputTypeDef]] = None
    preExtractionHookConfiguration: Optional[HookConfigurationOutputTypeDef] = None
    postExtractionHookConfiguration: Optional[HookConfigurationOutputTypeDef] = None


class DocumentAttributeValueUnionTypeDef(BaseValidatorModel):
    pass


class DocumentAttributeTargetTypeDef(BaseValidatorModel):
    key: str
    value: Optional[DocumentAttributeValueUnionTypeDef] = None
    attributeValueOperator: Optional[Literal["DELETE"]] = None


class DocumentAttributeTypeDef(BaseValidatorModel):
    name: str
    value: DocumentAttributeValueUnionTypeDef


class PluginAuthConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdatePluginRequestTypeDef(BaseValidatorModel):
    applicationId: str
    pluginId: str
    displayName: Optional[str] = None
    state: Optional[PluginStateType] = None
    serverUrl: Optional[str] = None
    customPluginConfiguration: Optional[CustomPluginConfigurationTypeDef] = None
    authConfiguration: Optional[PluginAuthConfigurationUnionTypeDef] = None


class AccessConfigurationTypeDef(BaseValidatorModel):
    accessControls: Sequence[AccessControlTypeDef]
    memberRelation: Optional[MemberRelationType] = None


class SourceAttributionTypeDef(BaseValidatorModel):
    title: Optional[str] = None
    snippet: Optional[str] = None
    url: Optional[str] = None
    citationNumber: Optional[int] = None
    updatedAt: Optional[datetime] = None
    textMessageSegments: Optional[List[TextSegmentTypeDef]] = None


class TopicConfigurationOutputTypeDef(BaseValidatorModel):
    name: str
    rules: List[RuleOutputTypeDef]
    description: Optional[str] = None
    exampleChatMessages: Optional[List[str]] = None


class ActionConfigurationOutputTypeDef(BaseValidatorModel):
    action: str
    filterConfiguration: Optional[ActionFilterConfigurationOutputTypeDef] = None


class ChatSyncOutputTypeDef(BaseValidatorModel):
    conversationId: str
    systemMessage: str
    systemMessageId: str
    userMessageId: str
    actionReview: ActionReviewTypeDef
    authChallengeRequest: AuthChallengeRequestTypeDef
    sourceAttributions: List[SourceAttributionTypeDef]
    failedAttachments: List[AttachmentOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class MetadataEventTypeDef(BaseValidatorModel):
    conversationId: Optional[str] = None
    userMessageId: Optional[str] = None
    systemMessageId: Optional[str] = None
    sourceAttributions: Optional[List[SourceAttributionTypeDef]] = None
    finalTextMessage: Optional[str] = None


class GetChatControlsConfigurationResponseTypeDef(BaseValidatorModel):
    responseScope: ResponseScopeType
    orchestrationConfiguration: AppliedOrchestrationConfigurationTypeDef
    blockedPhrases: BlockedPhrasesConfigurationTypeDef
    topicConfigurations: List[TopicConfigurationOutputTypeDef]
    creatorModeConfiguration: AppliedCreatorModeConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class UsersAndGroupsUnionTypeDef(BaseValidatorModel):
    pass


class RuleConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class RuleTypeDef(BaseValidatorModel):
    ruleType: RuleTypeType
    includedUsersAndGroups: Optional[UsersAndGroupsUnionTypeDef] = None
    excludedUsersAndGroups: Optional[UsersAndGroupsUnionTypeDef] = None
    ruleConfiguration: Optional[RuleConfigurationUnionTypeDef] = None


class RetrieverConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateRetrieverRequestTypeDef(BaseValidatorModel):
    applicationId: str
    retrieverId: str
    configuration: Optional[RetrieverConfigurationUnionTypeDef] = None
    displayName: Optional[str] = None
    roleArn: Optional[str] = None


class GetDataAccessorResponseTypeDef(BaseValidatorModel):
    displayName: str
    dataAccessorId: str
    dataAccessorArn: str
    applicationId: str
    idcApplicationArn: str
    principal: str
    actionConfigurations: List[ActionConfigurationOutputTypeDef]
    createdAt: datetime
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class DocumentAttributeConditionUnionTypeDef(BaseValidatorModel):
    pass


class HookConfigurationTypeDef(BaseValidatorModel):
    invocationCondition: Optional[DocumentAttributeConditionUnionTypeDef] = None
    lambdaArn: Optional[str] = None
    s3BucketName: Optional[str] = None
    roleArn: Optional[str] = None


class DocumentAttributeTargetUnionTypeDef(BaseValidatorModel):
    pass


class InlineDocumentEnrichmentConfigurationTypeDef(BaseValidatorModel):
    condition: Optional[DocumentAttributeConditionUnionTypeDef] = None
    target: Optional[DocumentAttributeTargetUnionTypeDef] = None
    documentContentOperator: Optional[Literal["DELETE"]] = None


class DocumentAttributeUnionTypeDef(BaseValidatorModel):
    pass


class AttributeFilterPaginatorTypeDef(BaseValidatorModel):
    andAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    orAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    notFilter: Optional[Mapping[str, Any]] = None
    equalsTo: Optional[DocumentAttributeUnionTypeDef] = None
    containsAll: Optional[DocumentAttributeUnionTypeDef] = None
    containsAny: Optional[DocumentAttributeUnionTypeDef] = None
    greaterThan: Optional[DocumentAttributeUnionTypeDef] = None
    greaterThanOrEquals: Optional[DocumentAttributeUnionTypeDef] = None
    lessThan: Optional[DocumentAttributeUnionTypeDef] = None
    lessThanOrEquals: Optional[DocumentAttributeUnionTypeDef] = None


class AttributeFilterTypeDef(BaseValidatorModel):
    andAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    orAllFilters: Optional[Sequence[Mapping[str, Any]]] = None
    notFilter: Optional[Mapping[str, Any]] = None
    equalsTo: Optional[DocumentAttributeUnionTypeDef] = None
    containsAll: Optional[DocumentAttributeUnionTypeDef] = None
    containsAny: Optional[DocumentAttributeUnionTypeDef] = None
    greaterThan: Optional[DocumentAttributeUnionTypeDef] = None
    greaterThanOrEquals: Optional[DocumentAttributeUnionTypeDef] = None
    lessThan: Optional[DocumentAttributeUnionTypeDef] = None
    lessThanOrEquals: Optional[DocumentAttributeUnionTypeDef] = None


class MessageTypeDef(BaseValidatorModel):
    pass


class ListMessagesResponseTypeDef(BaseValidatorModel):
    messages: List[MessageTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ChatOutputStreamTypeDef(BaseValidatorModel):
    textEvent: Optional[TextOutputEventTypeDef] = None
    metadataEvent: Optional[MetadataEventTypeDef] = None
    actionReviewEvent: Optional[ActionReviewEventTypeDef] = None
    failedAttachmentEvent: Optional[FailedAttachmentEventTypeDef] = None
    authChallengeRequestEvent: Optional[AuthChallengeRequestEventTypeDef] = None


class SearchRelevantContentRequestPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    queryText: str
    contentSource: ContentSourceTypeDef
    attributeFilter: Optional[AttributeFilterPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ChatOutputTypeDef(BaseValidatorModel):
    outputStream: EventStream[ChatOutputStreamTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class RuleUnionTypeDef(BaseValidatorModel):
    pass


class TopicConfigurationTypeDef(BaseValidatorModel):
    name: str
    rules: Sequence[RuleUnionTypeDef]
    description: Optional[str] = None
    exampleChatMessages: Optional[Sequence[str]] = None


class InlineDocumentEnrichmentConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class HookConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class DocumentEnrichmentConfigurationTypeDef(BaseValidatorModel):
    inlineConfigurations: Optional[Sequence[InlineDocumentEnrichmentConfigurationUnionTypeDef]] = None
    preExtractionHookConfiguration: Optional[HookConfigurationUnionTypeDef] = None
    postExtractionHookConfiguration: Optional[HookConfigurationUnionTypeDef] = None


class AttributeFilterUnionTypeDef(BaseValidatorModel):
    pass


class ActionFilterConfigurationTypeDef(BaseValidatorModel):
    documentAttributeFilter: AttributeFilterUnionTypeDef


class ActionExecutionUnionTypeDef(BaseValidatorModel):
    pass


class ChatSyncInputTypeDef(BaseValidatorModel):
    applicationId: str
    userId: Optional[str] = None
    userGroups: Optional[Sequence[str]] = None
    userMessage: Optional[str] = None
    attachments: Optional[Sequence[AttachmentInputTypeDef]] = None
    actionExecution: Optional[ActionExecutionUnionTypeDef] = None
    authChallengeResponse: Optional[AuthChallengeResponseTypeDef] = None
    conversationId: Optional[str] = None
    parentMessageId: Optional[str] = None
    attributeFilter: Optional[AttributeFilterUnionTypeDef] = None
    chatMode: Optional[ChatModeType] = None
    chatModeConfiguration: Optional[ChatModeConfigurationTypeDef] = None
    clientToken: Optional[str] = None


class ConfigurationEventTypeDef(BaseValidatorModel):
    chatMode: Optional[ChatModeType] = None
    chatModeConfiguration: Optional[ChatModeConfigurationTypeDef] = None
    attributeFilter: Optional[AttributeFilterUnionTypeDef] = None


class SearchRelevantContentRequestTypeDef(BaseValidatorModel):
    applicationId: str
    queryText: str
    contentSource: ContentSourceTypeDef
    attributeFilter: Optional[AttributeFilterUnionTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ChatInputStreamTypeDef(BaseValidatorModel):
    configurationEvent: Optional[ConfigurationEventTypeDef] = None
    textEvent: Optional[TextInputEventTypeDef] = None
    attachmentEvent: Optional[AttachmentInputEventTypeDef] = None
    actionExecutionEvent: Optional[ActionExecutionEventTypeDef] = None
    endOfInputEvent: Optional[Mapping[str, Any]] = None
    authChallengeResponseEvent: Optional[AuthChallengeResponseEventTypeDef] = None


class TopicConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class UpdateChatControlsConfigurationRequestTypeDef(BaseValidatorModel):
    applicationId: str
    clientToken: Optional[str] = None
    responseScope: Optional[ResponseScopeType] = None
    orchestrationConfiguration: Optional[OrchestrationConfigurationTypeDef] = None
    blockedPhrasesConfigurationUpdate: Optional[BlockedPhrasesConfigurationUpdateTypeDef] = None
    topicConfigurationsToCreateOrUpdate: Optional[Sequence[TopicConfigurationUnionTypeDef]] = None
    topicConfigurationsToDelete: Optional[Sequence[TopicConfigurationUnionTypeDef]] = None
    creatorModeConfiguration: Optional[CreatorModeConfigurationTypeDef] = None


class DataSourceVpcConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class DocumentEnrichmentConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataSourceRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    displayName: str
    configuration: Mapping[str, Any]
    vpcConfiguration: Optional[DataSourceVpcConfigurationUnionTypeDef] = None
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    syncSchedule: Optional[str] = None
    roleArn: Optional[str] = None
    clientToken: Optional[str] = None
    documentEnrichmentConfiguration: Optional[DocumentEnrichmentConfigurationUnionTypeDef] = None
    mediaExtractionConfiguration: Optional[MediaExtractionConfigurationTypeDef] = None


class UpdateDataSourceRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceId: str
    displayName: Optional[str] = None
    configuration: Optional[Mapping[str, Any]] = None
    vpcConfiguration: Optional[DataSourceVpcConfigurationUnionTypeDef] = None
    description: Optional[str] = None
    syncSchedule: Optional[str] = None
    roleArn: Optional[str] = None
    documentEnrichmentConfiguration: Optional[DocumentEnrichmentConfigurationUnionTypeDef] = None
    mediaExtractionConfiguration: Optional[MediaExtractionConfigurationTypeDef] = None


class ActionFilterConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ActionConfigurationTypeDef(BaseValidatorModel):
    action: str
    filterConfiguration: Optional[ActionFilterConfigurationUnionTypeDef] = None


class ChatInputTypeDef(BaseValidatorModel):
    applicationId: str
    userId: Optional[str] = None
    userGroups: Optional[Sequence[str]] = None
    conversationId: Optional[str] = None
    parentMessageId: Optional[str] = None
    clientToken: Optional[str] = None
    inputStream: Optional[EventStream[ChatInputStreamTypeDef]] = None


class DocumentTypeDef(BaseValidatorModel):
    pass


class BatchPutDocumentRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    documents: Sequence[DocumentTypeDef]
    roleArn: Optional[str] = None
    dataSourceSyncId: Optional[str] = None


class ActionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateDataAccessorRequestTypeDef(BaseValidatorModel):
    applicationId: str
    principal: str
    actionConfigurations: Sequence[ActionConfigurationUnionTypeDef]
    displayName: str
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None


class UpdateDataAccessorRequestTypeDef(BaseValidatorModel):
    applicationId: str
    dataAccessorId: str
    actionConfigurations: Sequence[ActionConfigurationUnionTypeDef]
    displayName: Optional[str] = None


