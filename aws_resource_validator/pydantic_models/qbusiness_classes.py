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
from aws_resource_validator.pydantic_models.qbusiness_constants import *

class S3TypeDef(BaseValidatorModel):
    bucket: str
    key: str

class ActionExecutionPayloadFieldExtraOutputTypeDef(BaseValidatorModel):
    value: Dict[str, Any]

class ActionExecutionPayloadFieldOutputTypeDef(BaseValidatorModel):
    value: Dict[str, Any]

class ActionExecutionPayloadFieldTypeDef(BaseValidatorModel):
    value: Mapping[str, Any]

class ActionReviewPayloadFieldAllowedValueTypeDef(BaseValidatorModel):
    value: Optional[Dict[str, Any]] = None
    displayValue: Optional[Dict[str, Any]] = None

class ApplicationTypeDef(BaseValidatorModel):
    displayName: Optional[str] = None
    applicationId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    status: Optional[ApplicationStatusType] = None

class AppliedAttachmentsConfigurationTypeDef(BaseValidatorModel):
    attachmentsControlMode: Optional[AttachmentsControlModeType] = None

class AppliedCreatorModeConfigurationTypeDef(BaseValidatorModel):
    creatorModeControl: CreatorModeControlType

class ErrorDetailTypeDef(BaseValidatorModel):
    errorMessage: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None

class AttachmentsConfigurationTypeDef(BaseValidatorModel):
    attachmentsControlMode: AttachmentsControlModeType

class AuthChallengeRequestTypeDef(BaseValidatorModel):
    authorizationUrl: str

class AuthChallengeResponseTypeDef(BaseValidatorModel):
    responseMap: Mapping[str, str]

class BasicAuthConfigurationTypeDef(BaseValidatorModel):
    secretArn: str
    roleArn: str

class DeleteDocumentTypeDef(BaseValidatorModel):
    documentId: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BlockedPhrasesConfigurationTypeDef(BaseValidatorModel):
    blockedPhrases: Optional[List[str]] = None
    systemMessageOverride: Optional[str] = None

class BlockedPhrasesConfigurationUpdateTypeDef(BaseValidatorModel):
    blockedPhrasesToCreateOrUpdate: Optional[Sequence[str]] = None
    blockedPhrasesToDelete: Optional[Sequence[str]] = None
    systemMessageOverride: Optional[str] = None

class PluginConfigurationTypeDef(BaseValidatorModel):
    pluginId: str

class ContentBlockerRuleTypeDef(BaseValidatorModel):
    systemMessageOverride: Optional[str] = None

class EligibleDataSourceTypeDef(BaseValidatorModel):
    indexId: Optional[str] = None
    dataSourceId: Optional[str] = None

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

class DataSourceVpcConfigurationTypeDef(BaseValidatorModel):
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]

class IndexCapacityConfigurationTypeDef(BaseValidatorModel):
    units: Optional[int] = None

class UserAliasTypeDef(BaseValidatorModel):
    userId: str
    indexId: Optional[str] = None
    dataSourceId: Optional[str] = None

class CreatorModeConfigurationTypeDef(BaseValidatorModel):
    creatorModeControl: CreatorModeControlType

class DataSourceSyncJobMetricsTypeDef(BaseValidatorModel):
    documentsAdded: Optional[str] = None
    documentsModified: Optional[str] = None
    documentsDeleted: Optional[str] = None
    documentsFailed: Optional[str] = None
    documentsScanned: Optional[str] = None

class DataSourceTypeDef(BaseValidatorModel):
    displayName: Optional[str] = None
    dataSourceId: Optional[str] = None
    type: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    status: Optional[DataSourceStatusType] = None

class DataSourceVpcConfigurationOutputTypeDef(BaseValidatorModel):
    subnetIds: List[str]
    securityGroupIds: List[str]

class DateAttributeBoostingConfigurationTypeDef(BaseValidatorModel):
    boostingLevel: DocumentAttributeBoostingLevelType
    boostingDurationInSeconds: Optional[int] = None

class DeleteApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str

class DeleteChatControlsConfigurationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str

class DeleteConversationRequestRequestTypeDef(BaseValidatorModel):
    conversationId: str
    applicationId: str
    userId: Optional[str] = None

class DeleteDataSourceRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceId: str

class DeleteGroupRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    groupName: str
    dataSourceId: Optional[str] = None

class DeleteIndexRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str

class DeletePluginRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    pluginId: str

class DeleteRetrieverRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    retrieverId: str

class DeleteUserRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    userId: str

class DeleteWebExperienceRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    webExperienceId: str

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

class DocumentAttributeConfigurationTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    type: Optional[AttributeTypeType] = None
    search: Optional[StatusType] = None

class GetApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetChatControlsConfigurationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetDataSourceRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceId: str

class GetGroupRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    groupName: str
    dataSourceId: Optional[str] = None

class GetIndexRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str

class GetPluginRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    pluginId: str

class GetRetrieverRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    retrieverId: str

class GetUserRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    userId: str

class GetWebExperienceRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    webExperienceId: str

class MemberGroupTypeDef(BaseValidatorModel):
    groupName: str
    type: Optional[MembershipTypeType] = None

class MemberUserTypeDef(BaseValidatorModel):
    userId: str
    type: Optional[MembershipTypeType] = None

class GroupSummaryTypeDef(BaseValidatorModel):
    groupName: Optional[str] = None

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

class ListApplicationsRequestRequestTypeDef(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListConversationsRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    userId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDataSourcesRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDocumentsRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListIndicesRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListMessagesRequestRequestTypeDef(BaseValidatorModel):
    conversationId: str
    applicationId: str
    userId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPluginsRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PluginTypeDef(BaseValidatorModel):
    pluginId: Optional[str] = None
    displayName: Optional[str] = None
    type: Optional[PluginTypeType] = None
    serverUrl: Optional[str] = None
    state: Optional[PluginStateType] = None
    buildStatus: Optional[PluginBuildStatusType] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class ListRetrieversRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RetrieverTypeDef(BaseValidatorModel):
    applicationId: Optional[str] = None
    retrieverId: Optional[str] = None
    type: Optional[RetrieverTypeType] = None
    status: Optional[RetrieverStatusType] = None
    displayName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str

class ListWebExperiencesRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class WebExperienceTypeDef(BaseValidatorModel):
    webExperienceId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    defaultEndpoint: Optional[str] = None
    status: Optional[WebExperienceStatusType] = None

class OAuth2ClientCredentialConfigurationTypeDef(BaseValidatorModel):
    secretArn: str
    roleArn: str

class PrincipalGroupTypeDef(BaseValidatorModel):
    access: ReadAccessTypeType
    name: Optional[str] = None
    membershipType: Optional[MembershipTypeType] = None

class PrincipalUserTypeDef(BaseValidatorModel):
    access: ReadAccessTypeType
    id: Optional[str] = None
    membershipType: Optional[MembershipTypeType] = None

class UsersAndGroupsExtraOutputTypeDef(BaseValidatorModel):
    userIds: Optional[List[str]] = None
    userGroups: Optional[List[str]] = None

class UsersAndGroupsOutputTypeDef(BaseValidatorModel):
    userIds: Optional[List[str]] = None
    userGroups: Optional[List[str]] = None

class UsersAndGroupsTypeDef(BaseValidatorModel):
    userIds: Optional[Sequence[str]] = None
    userGroups: Optional[Sequence[str]] = None

class SamlConfigurationTypeDef(BaseValidatorModel):
    metadataXML: str
    roleArn: str
    userIdAttribute: str
    userGroupAttribute: Optional[str] = None

class SnippetExcerptTypeDef(BaseValidatorModel):
    text: Optional[str] = None

class StartDataSourceSyncJobRequestRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    applicationId: str
    indexId: str

class StopDataSourceSyncJobRequestRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    applicationId: str
    indexId: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tagKeys: Sequence[str]

class APISchemaTypeDef(BaseValidatorModel):
    payload: Optional[str] = None
    s3: Optional[S3TypeDef] = None

class ActionExecutionExtraOutputTypeDef(BaseValidatorModel):
    pluginId: str
    payload: Dict[str, ActionExecutionPayloadFieldExtraOutputTypeDef]
    payloadFieldNameSeparator: str

class ActionExecutionOutputTypeDef(BaseValidatorModel):
    pluginId: str
    payload: Dict[str, ActionExecutionPayloadFieldOutputTypeDef]
    payloadFieldNameSeparator: str

class ActionExecutionTypeDef(BaseValidatorModel):
    pluginId: str
    payload: Mapping[str, ActionExecutionPayloadFieldTypeDef]
    payloadFieldNameSeparator: str

class ActionReviewPayloadFieldTypeDef(BaseValidatorModel):
    displayName: Optional[str] = None
    displayOrder: Optional[int] = None
    displayDescription: Optional[str] = None
    type: Optional[ActionPayloadFieldTypeType] = None
    value: Optional[Dict[str, Any]] = None
    allowedValues: Optional[List[ActionReviewPayloadFieldAllowedValueTypeDef]] = None
    allowedFormat: Optional[str] = None
    required: Optional[bool] = None

class AttachmentInputTypeDef(BaseValidatorModel):
    name: str
    data: BlobTypeDef

class DocumentContentTypeDef(BaseValidatorModel):
    blob: Optional[BlobTypeDef] = None
    s3: Optional[S3TypeDef] = None

class AttachmentOutputTypeDef(BaseValidatorModel):
    name: Optional[str] = None
    status: Optional[AttachmentStatusType] = None
    error: Optional[ErrorDetailTypeDef] = None

class DocumentDetailsTypeDef(BaseValidatorModel):
    documentId: Optional[str] = None
    status: Optional[DocumentStatusType] = None
    error: Optional[ErrorDetailTypeDef] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class FailedDocumentTypeDef(BaseValidatorModel):
    id: Optional[str] = None
    error: Optional[ErrorDetailTypeDef] = None
    dataSourceId: Optional[str] = None

class GroupStatusDetailTypeDef(BaseValidatorModel):
    status: Optional[GroupStatusType] = None
    lastUpdatedAt: Optional[datetime] = None
    errorDetail: Optional[ErrorDetailTypeDef] = None

class BatchDeleteDocumentRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    documents: Sequence[DeleteDocumentTypeDef]
    dataSourceSyncId: Optional[str] = None

class CreateApplicationResponseTypeDef(BaseValidatorModel):
    applicationId: str
    applicationArn: str
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

class ListApplicationsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    applications: List[ApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataSourceSyncJobResponseTypeDef(BaseValidatorModel):
    executionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChatModeConfigurationTypeDef(BaseValidatorModel):
    pluginConfiguration: Optional[PluginConfigurationTypeDef] = None

class ContentRetrievalRuleExtraOutputTypeDef(BaseValidatorModel):
    eligibleDataSources: Optional[List[EligibleDataSourceTypeDef]] = None

class ContentRetrievalRuleOutputTypeDef(BaseValidatorModel):
    eligibleDataSources: Optional[List[EligibleDataSourceTypeDef]] = None

class ContentRetrievalRuleTypeDef(BaseValidatorModel):
    eligibleDataSources: Optional[Sequence[EligibleDataSourceTypeDef]] = None

class ListConversationsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    conversations: List[ConversationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationResponseTypeDef(BaseValidatorModel):
    displayName: str
    applicationId: str
    applicationArn: str
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
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateApplicationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    identityCenterInstanceArn: Optional[str] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    roleArn: Optional[str] = None
    attachmentsConfiguration: Optional[AttachmentsConfigurationTypeDef] = None
    qAppsConfiguration: Optional[QAppsConfigurationTypeDef] = None
    personalizationConfiguration: Optional[PersonalizationConfigurationTypeDef] = None

class CreateApplicationRequestRequestTypeDef(BaseValidatorModel):
    displayName: str
    roleArn: Optional[str] = None
    identityCenterInstanceArn: Optional[str] = None
    description: Optional[str] = None
    encryptionConfiguration: Optional[EncryptionConfigurationTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    clientToken: Optional[str] = None
    attachmentsConfiguration: Optional[AttachmentsConfigurationTypeDef] = None
    qAppsConfiguration: Optional[QAppsConfigurationTypeDef] = None
    personalizationConfiguration: Optional[PersonalizationConfigurationTypeDef] = None

class CreateWebExperienceRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    title: Optional[str] = None
    subtitle: Optional[str] = None
    welcomeMessage: Optional[str] = None
    samplePromptsControlMode: Optional[WebExperienceSamplePromptsControlModeType] = None
    roleArn: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    clientToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceARN: str
    tags: Sequence[TagTypeDef]

class CreateIndexRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    displayName: str
    type: Optional[IndexTypeType] = None
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    capacityConfiguration: Optional[IndexCapacityConfigurationTypeDef] = None
    clientToken: Optional[str] = None

class CreateUserRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    userId: str
    userAliases: Optional[Sequence[UserAliasTypeDef]] = None
    clientToken: Optional[str] = None

class GetUserResponseTypeDef(BaseValidatorModel):
    userAliases: List[UserAliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    userId: str
    userAliasesToUpdate: Optional[Sequence[UserAliasTypeDef]] = None
    userAliasesToDelete: Optional[Sequence[UserAliasTypeDef]] = None

class UpdateUserResponseTypeDef(BaseValidatorModel):
    userAliasesAdded: List[UserAliasTypeDef]
    userAliasesUpdated: List[UserAliasTypeDef]
    userAliasesDeleted: List[UserAliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceSyncJobTypeDef(BaseValidatorModel):
    executionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    status: Optional[DataSourceSyncJobStatusType] = None
    error: Optional[ErrorDetailTypeDef] = None
    dataSourceErrorCode: Optional[str] = None
    metrics: Optional[DataSourceSyncJobMetricsTypeDef] = None

class ListDataSourcesResponseTypeDef(BaseValidatorModel):
    dataSources: List[DataSourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class DocumentAttributeConditionOutputTypeDef(BaseValidatorModel):
    key: str
    operator: DocumentEnrichmentConditionOperatorType
    value: Optional[DocumentAttributeValueOutputTypeDef] = None

class DocumentAttributeTargetOutputTypeDef(BaseValidatorModel):
    key: str
    value: Optional[DocumentAttributeValueOutputTypeDef] = None
    attributeValueOperator: Optional[Literal["DELETE"]] = None

class UpdateIndexRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    displayName: Optional[str] = None
    description: Optional[str] = None
    capacityConfiguration: Optional[IndexCapacityConfigurationTypeDef] = None
    documentAttributeConfigurations: Optional[       Sequence[DocumentAttributeConfigurationTypeDef]     ] = None

class DocumentAttributeValueTypeDef(BaseValidatorModel):
    stringValue: Optional[str] = None
    stringListValue: Optional[Sequence[str]] = None
    longValue: Optional[int] = None
    dateValue: Optional[TimestampTypeDef] = None

class ListDataSourceSyncJobsRequestRequestTypeDef(BaseValidatorModel):
    dataSourceId: str
    applicationId: str
    indexId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    statusFilter: Optional[DataSourceSyncJobStatusType] = None

class ListGroupsRequestRequestTypeDef(BaseValidatorModel):
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

class GetChatControlsConfigurationRequestGetChatControlsConfigurationPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConversationsRequestListConversationsPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    userId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourceSyncJobsRequestListDataSourceSyncJobsPaginateTypeDef(BaseValidatorModel):
    dataSourceId: str
    applicationId: str
    indexId: str
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    statusFilter: Optional[DataSourceSyncJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourcesRequestListDataSourcesPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDocumentsRequestListDocumentsPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsRequestListGroupsPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    updatedEarlierThan: TimestampTypeDef
    dataSourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIndicesRequestListIndicesPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMessagesRequestListMessagesPaginateTypeDef(BaseValidatorModel):
    conversationId: str
    applicationId: str
    userId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPluginsRequestListPluginsPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRetrieversRequestListRetrieversPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWebExperiencesRequestListWebExperiencesPaginateTypeDef(BaseValidatorModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GroupMembersTypeDef(BaseValidatorModel):
    memberGroups: Optional[Sequence[MemberGroupTypeDef]] = None
    memberUsers: Optional[Sequence[MemberUserTypeDef]] = None

class ListGroupsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    items: List[GroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IndexStatisticsTypeDef(BaseValidatorModel):
    textDocumentStatistics: Optional[TextDocumentStatisticsTypeDef] = None

class ListIndicesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    indices: List[IndexTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPluginsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    plugins: List[PluginTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRetrieversResponseTypeDef(BaseValidatorModel):
    retrievers: List[RetrieverTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebExperiencesResponseTypeDef(BaseValidatorModel):
    webExperiences: List[WebExperienceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PluginAuthConfigurationOutputTypeDef(BaseValidatorModel):
    basicAuthConfiguration: Optional[BasicAuthConfigurationTypeDef] = None
    oAuth2ClientCredentialConfiguration: Optional[       OAuth2ClientCredentialConfigurationTypeDef     ] = None
    noAuthConfiguration: Optional[Dict[str, Any]] = None

class PluginAuthConfigurationTypeDef(BaseValidatorModel):
    basicAuthConfiguration: Optional[BasicAuthConfigurationTypeDef] = None
    oAuth2ClientCredentialConfiguration: Optional[       OAuth2ClientCredentialConfigurationTypeDef     ] = None
    noAuthConfiguration: Optional[Mapping[str, Any]] = None

class PrincipalTypeDef(BaseValidatorModel):
    user: Optional[PrincipalUserTypeDef] = None
    group: Optional[PrincipalGroupTypeDef] = None

class WebExperienceAuthConfigurationTypeDef(BaseValidatorModel):
    samlConfiguration: Optional[SamlConfigurationTypeDef] = None

class TextSegmentTypeDef(BaseValidatorModel):
    beginOffset: Optional[int] = None
    endOffset: Optional[int] = None
    snippetExcerpt: Optional[SnippetExcerptTypeDef] = None

class CustomPluginConfigurationTypeDef(BaseValidatorModel):
    description: str
    apiSchemaType: Literal["OPEN_API_V3"]
    apiSchema: APISchemaTypeDef

class ActionReviewTypeDef(BaseValidatorModel):
    pluginId: Optional[str] = None
    pluginType: Optional[PluginTypeType] = None
    payload: Optional[Dict[str, ActionReviewPayloadFieldTypeDef]] = None
    payloadFieldNameSeparator: Optional[str] = None

class ListDocumentsResponseTypeDef(BaseValidatorModel):
    documentDetailList: List[DocumentDetailsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

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

class ChatSyncInputRequestTypeDef(BaseValidatorModel):
    applicationId: str
    userId: Optional[str] = None
    userGroups: Optional[Sequence[str]] = None
    userMessage: Optional[str] = None
    attachments: Optional[Sequence[AttachmentInputTypeDef]] = None
    actionExecution: Optional[ActionExecutionTypeDef] = None
    authChallengeResponse: Optional[AuthChallengeResponseTypeDef] = None
    conversationId: Optional[str] = None
    parentMessageId: Optional[str] = None
    attributeFilter: Optional["AttributeFilterTypeDef"] = None
    chatMode: Optional[ChatModeType] = None
    chatModeConfiguration: Optional[ChatModeConfigurationTypeDef] = None
    clientToken: Optional[str] = None

class RuleConfigurationExtraOutputTypeDef(BaseValidatorModel):
    contentBlockerRule: Optional[ContentBlockerRuleTypeDef] = None
    contentRetrievalRule: Optional[ContentRetrievalRuleExtraOutputTypeDef] = None

class RuleConfigurationOutputTypeDef(BaseValidatorModel):
    contentBlockerRule: Optional[ContentBlockerRuleTypeDef] = None
    contentRetrievalRule: Optional[ContentRetrievalRuleOutputTypeDef] = None

class RuleConfigurationTypeDef(BaseValidatorModel):
    contentBlockerRule: Optional[ContentBlockerRuleTypeDef] = None
    contentRetrievalRule: Optional[ContentRetrievalRuleTypeDef] = None

class ListDataSourceSyncJobsResponseTypeDef(BaseValidatorModel):
    history: List[DataSourceSyncJobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class NativeIndexConfigurationOutputTypeDef(BaseValidatorModel):
    indexId: str
    boostingOverride: Optional[       Dict[str, DocumentAttributeBoostingConfigurationOutputTypeDef] = None

class NativeIndexConfigurationTypeDef(BaseValidatorModel):
    indexId: str
    boostingOverride: Optional[       Mapping[str, DocumentAttributeBoostingConfigurationTypeDef] = None

class HookConfigurationOutputTypeDef(BaseValidatorModel):
    invocationCondition: Optional[DocumentAttributeConditionOutputTypeDef] = None
    lambdaArn: Optional[str] = None
    s3BucketName: Optional[str] = None
    roleArn: Optional[str] = None

class InlineDocumentEnrichmentConfigurationOutputTypeDef(BaseValidatorModel):
    condition: Optional[DocumentAttributeConditionOutputTypeDef] = None
    target: Optional[DocumentAttributeTargetOutputTypeDef] = None
    documentContentOperator: Optional[Literal["DELETE"]] = None

class DocumentAttributeConditionTypeDef(BaseValidatorModel):
    key: str
    operator: DocumentEnrichmentConditionOperatorType
    value: Optional[DocumentAttributeValueTypeDef] = None

class DocumentAttributeTargetTypeDef(BaseValidatorModel):
    key: str
    value: Optional[DocumentAttributeValueTypeDef] = None
    attributeValueOperator: Optional[Literal["DELETE"]] = None

class DocumentAttributeTypeDef(BaseValidatorModel):
    name: str
    value: DocumentAttributeValueTypeDef

class PutFeedbackRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    conversationId: str
    messageId: str
    userId: Optional[str] = None
    messageCopiedAt: Optional[TimestampTypeDef] = None
    messageUsefulness: Optional[MessageUsefulnessFeedbackTypeDef] = None

class PutGroupRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    groupName: str
    type: MembershipTypeType
    groupMembers: GroupMembersTypeDef
    dataSourceId: Optional[str] = None

class GetIndexResponseTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    displayName: str
    type: IndexTypeType
    indexArn: str
    status: IndexStatusType
    description: str
    createdAt: datetime
    updatedAt: datetime
    capacityConfiguration: IndexCapacityConfigurationTypeDef
    documentAttributeConfigurations: List[DocumentAttributeConfigurationTypeDef]
    error: ErrorDetailTypeDef
    indexStatistics: IndexStatisticsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

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
    roleArn: str
    authenticationConfiguration: WebExperienceAuthConfigurationTypeDef
    error: ErrorDetailTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateWebExperienceRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    webExperienceId: str
    roleArn: Optional[str] = None
    authenticationConfiguration: Optional[WebExperienceAuthConfigurationTypeDef] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    welcomeMessage: Optional[str] = None
    samplePromptsControlMode: Optional[WebExperienceSamplePromptsControlModeType] = None

class SourceAttributionTypeDef(BaseValidatorModel):
    title: Optional[str] = None
    snippet: Optional[str] = None
    url: Optional[str] = None
    citationNumber: Optional[int] = None
    updatedAt: Optional[datetime] = None
    textMessageSegments: Optional[List[TextSegmentTypeDef]] = None

class CreatePluginRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    displayName: str
    type: PluginTypeType
    authConfiguration: PluginAuthConfigurationTypeDef
    serverUrl: Optional[str] = None
    customPluginConfiguration: Optional[CustomPluginConfigurationTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    clientToken: Optional[str] = None

class GetPluginResponseTypeDef(BaseValidatorModel):
    applicationId: str
    pluginId: str
    displayName: str
    type: PluginTypeType
    serverUrl: str
    authConfiguration: PluginAuthConfigurationOutputTypeDef
    customPluginConfiguration: CustomPluginConfigurationTypeDef
    buildStatus: PluginBuildStatusType
    pluginArn: str
    state: PluginStateType
    createdAt: datetime
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePluginRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    pluginId: str
    displayName: Optional[str] = None
    state: Optional[PluginStateType] = None
    serverUrl: Optional[str] = None
    customPluginConfiguration: Optional[CustomPluginConfigurationTypeDef] = None
    authConfiguration: Optional[PluginAuthConfigurationTypeDef] = None

class RuleExtraOutputTypeDef(BaseValidatorModel):
    ruleType: RuleTypeType
    includedUsersAndGroups: Optional[UsersAndGroupsExtraOutputTypeDef] = None
    excludedUsersAndGroups: Optional[UsersAndGroupsExtraOutputTypeDef] = None
    ruleConfiguration: Optional[RuleConfigurationExtraOutputTypeDef] = None

class RuleOutputTypeDef(BaseValidatorModel):
    ruleType: RuleTypeType
    includedUsersAndGroups: Optional[UsersAndGroupsOutputTypeDef] = None
    excludedUsersAndGroups: Optional[UsersAndGroupsOutputTypeDef] = None
    ruleConfiguration: Optional[RuleConfigurationOutputTypeDef] = None

class RuleTypeDef(BaseValidatorModel):
    ruleType: RuleTypeType
    includedUsersAndGroups: Optional[UsersAndGroupsTypeDef] = None
    excludedUsersAndGroups: Optional[UsersAndGroupsTypeDef] = None
    ruleConfiguration: Optional[RuleConfigurationTypeDef] = None

class RetrieverConfigurationOutputTypeDef(BaseValidatorModel):
    nativeIndexConfiguration: Optional[NativeIndexConfigurationOutputTypeDef] = None
    kendraIndexConfiguration: Optional[KendraIndexConfigurationTypeDef] = None

class RetrieverConfigurationTypeDef(BaseValidatorModel):
    nativeIndexConfiguration: Optional[NativeIndexConfigurationTypeDef] = None
    kendraIndexConfiguration: Optional[KendraIndexConfigurationTypeDef] = None

class DocumentEnrichmentConfigurationOutputTypeDef(BaseValidatorModel):
    inlineConfigurations: Optional[       List[InlineDocumentEnrichmentConfigurationOutputTypeDef]     ] = None
    preExtractionHookConfiguration: Optional[HookConfigurationOutputTypeDef] = None
    postExtractionHookConfiguration: Optional[HookConfigurationOutputTypeDef] = None

class HookConfigurationTypeDef(BaseValidatorModel):
    invocationCondition: Optional[DocumentAttributeConditionTypeDef] = None
    lambdaArn: Optional[str] = None
    s3BucketName: Optional[str] = None
    roleArn: Optional[str] = None

class InlineDocumentEnrichmentConfigurationTypeDef(BaseValidatorModel):
    condition: Optional[DocumentAttributeConditionTypeDef] = None
    target: Optional[DocumentAttributeTargetTypeDef] = None
    documentContentOperator: Optional[Literal["DELETE"]] = None

class AttributeFilterTypeDef(BaseValidatorModel):
    andAllFilters: Optional[Sequence[Dict[str, Any]]] = None
    orAllFilters: Optional[Sequence[Dict[str, Any]]] = None
    notFilter: Optional[Dict[str, Any]] = None
    equalsTo: Optional[DocumentAttributeTypeDef] = None
    containsAll: Optional[DocumentAttributeTypeDef] = None
    containsAny: Optional[DocumentAttributeTypeDef] = None
    greaterThan: Optional[DocumentAttributeTypeDef] = None
    greaterThanOrEquals: Optional[DocumentAttributeTypeDef] = None
    lessThan: Optional[DocumentAttributeTypeDef] = None
    lessThanOrEquals: Optional[DocumentAttributeTypeDef] = None

class AccessConfigurationTypeDef(BaseValidatorModel):
    accessControls: Sequence[AccessControlTypeDef]
    memberRelation: Optional[MemberRelationType] = None

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

class MessageTypeDef(BaseValidatorModel):
    messageId: Optional[str] = None
    body: Optional[str] = None
    time: Optional[datetime] = None
    type: Optional[MessageTypeType] = None
    attachments: Optional[List[AttachmentOutputTypeDef]] = None
    sourceAttribution: Optional[List[SourceAttributionTypeDef]] = None
    actionReview: Optional[ActionReviewTypeDef] = None
    actionExecution: Optional[ActionExecutionOutputTypeDef] = None

class TopicConfigurationExtraOutputTypeDef(BaseValidatorModel):
    name: str
    rules: List[RuleExtraOutputTypeDef]
    description: Optional[str] = None
    exampleChatMessages: Optional[List[str]] = None

class TopicConfigurationOutputTypeDef(BaseValidatorModel):
    name: str
    rules: List[RuleOutputTypeDef]
    description: Optional[str] = None
    exampleChatMessages: Optional[List[str]] = None

class TopicConfigurationTypeDef(BaseValidatorModel):
    name: str
    rules: Sequence[RuleTypeDef]
    description: Optional[str] = None
    exampleChatMessages: Optional[Sequence[str]] = None

class GetRetrieverResponseTypeDef(BaseValidatorModel):
    applicationId: str
    retrieverId: str
    retrieverArn: str
    type: RetrieverTypeType
    status: RetrieverStatusType
    displayName: str
    configuration: RetrieverConfigurationOutputTypeDef
    roleArn: str
    createdAt: datetime
    updatedAt: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRetrieverRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    type: RetrieverTypeType
    displayName: str
    configuration: RetrieverConfigurationTypeDef
    roleArn: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateRetrieverRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    retrieverId: str
    configuration: Optional[RetrieverConfigurationTypeDef] = None
    displayName: Optional[str] = None
    roleArn: Optional[str] = None

class GetDataSourceResponseTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceId: str
    dataSourceArn: str
    displayName: str
    type: str
    configuration: Dict[str, Any]
    vpcConfiguration: DataSourceVpcConfigurationOutputTypeDef
    createdAt: datetime
    updatedAt: datetime
    description: str
    status: DataSourceStatusType
    syncSchedule: str
    roleArn: str
    error: ErrorDetailTypeDef
    documentEnrichmentConfiguration: DocumentEnrichmentConfigurationOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentEnrichmentConfigurationTypeDef(BaseValidatorModel):
    inlineConfigurations: Optional[Sequence[InlineDocumentEnrichmentConfigurationTypeDef]] = None
    preExtractionHookConfiguration: Optional[HookConfigurationTypeDef] = None
    postExtractionHookConfiguration: Optional[HookConfigurationTypeDef] = None

class ListMessagesResponseTypeDef(BaseValidatorModel):
    messages: List[MessageTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChatControlsConfigurationResponseTypeDef(BaseValidatorModel):
    responseScope: ResponseScopeType
    blockedPhrases: BlockedPhrasesConfigurationTypeDef
    topicConfigurations: List[TopicConfigurationExtraOutputTypeDef]
    creatorModeConfiguration: AppliedCreatorModeConfigurationTypeDef
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    displayName: str
    configuration: Mapping[str, Any]
    vpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    syncSchedule: Optional[str] = None
    roleArn: Optional[str] = None
    clientToken: Optional[str] = None
    documentEnrichmentConfiguration: Optional[DocumentEnrichmentConfigurationTypeDef] = None

class DocumentTypeDef(BaseValidatorModel):
    id: str
    attributes: Optional[Sequence[DocumentAttributeTypeDef]] = None
    content: Optional[DocumentContentTypeDef] = None
    contentType: Optional[ContentTypeType] = None
    title: Optional[str] = None
    accessConfiguration: Optional[AccessConfigurationTypeDef] = None
    documentEnrichmentConfiguration: Optional[DocumentEnrichmentConfigurationTypeDef] = None

class UpdateDataSourceRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    dataSourceId: str
    displayName: Optional[str] = None
    configuration: Optional[Mapping[str, Any]] = None
    vpcConfiguration: Optional[DataSourceVpcConfigurationTypeDef] = None
    description: Optional[str] = None
    syncSchedule: Optional[str] = None
    roleArn: Optional[str] = None
    documentEnrichmentConfiguration: Optional[DocumentEnrichmentConfigurationTypeDef] = None

class UpdateChatControlsConfigurationRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    clientToken: Optional[str] = None
    responseScope: Optional[ResponseScopeType] = None
    blockedPhrasesConfigurationUpdate: Optional[BlockedPhrasesConfigurationUpdateTypeDef] = None
    topicConfigurationsToCreateOrUpdate: Optional[       Sequence[TopicConfigurationUnionTypeDef]     ] = None
    topicConfigurationsToDelete: Optional[Sequence[TopicConfigurationUnionTypeDef]] = None
    creatorModeConfiguration: Optional[CreatorModeConfigurationTypeDef] = None

class BatchPutDocumentRequestRequestTypeDef(BaseValidatorModel):
    applicationId: str
    indexId: str
    documents: Sequence[DocumentTypeDef]
    roleArn: Optional[str] = None
    dataSourceSyncId: Optional[str] = None

