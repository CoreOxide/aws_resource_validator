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
from aws_resource_validator.pydantic_models.qbusiness_constants import *

class S3TypeDef(BaseModel):
    bucket: str
    key: str

class ActionExecutionPayloadFieldExtraOutputTypeDef(BaseModel):
    value: Dict[str, Any]

class ActionExecutionPayloadFieldOutputTypeDef(BaseModel):
    value: Dict[str, Any]

class ActionExecutionPayloadFieldTypeDef(BaseModel):
    value: Mapping[str, Any]

class ActionReviewPayloadFieldAllowedValueTypeDef(BaseModel):
    value: Optional[Dict[str, Any]] = None
    displayValue: Optional[Dict[str, Any]] = None

class ApplicationTypeDef(BaseModel):
    displayName: Optional[str] = None
    applicationId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    status: Optional[ApplicationStatusType] = None

class AppliedAttachmentsConfigurationTypeDef(BaseModel):
    attachmentsControlMode: Optional[AttachmentsControlModeType] = None

class AppliedCreatorModeConfigurationTypeDef(BaseModel):
    creatorModeControl: CreatorModeControlType

class ErrorDetailTypeDef(BaseModel):
    errorMessage: Optional[str] = None
    errorCode: Optional[ErrorCodeType] = None

class AttachmentsConfigurationTypeDef(BaseModel):
    attachmentsControlMode: AttachmentsControlModeType

class AuthChallengeRequestTypeDef(BaseModel):
    authorizationUrl: str

class AuthChallengeResponseTypeDef(BaseModel):
    responseMap: Mapping[str, str]

class BasicAuthConfigurationTypeDef(BaseModel):
    secretArn: str
    roleArn: str

class DeleteDocumentTypeDef(BaseModel):
    documentId: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BlockedPhrasesConfigurationTypeDef(BaseModel):
    blockedPhrases: Optional[List[str]] = None
    systemMessageOverride: Optional[str] = None

class BlockedPhrasesConfigurationUpdateTypeDef(BaseModel):
    blockedPhrasesToCreateOrUpdate: Optional[Sequence[str]] = None
    blockedPhrasesToDelete: Optional[Sequence[str]] = None
    systemMessageOverride: Optional[str] = None

class PluginConfigurationTypeDef(BaseModel):
    pluginId: str

class ContentBlockerRuleTypeDef(BaseModel):
    systemMessageOverride: Optional[str] = None

class EligibleDataSourceTypeDef(BaseModel):
    indexId: Optional[str] = None
    dataSourceId: Optional[str] = None

class ConversationTypeDef(BaseModel):
    conversationId: Optional[str] = None
    title: Optional[str] = None
    startTime: Optional[datetime] = None

class EncryptionConfigurationTypeDef(BaseModel):
    kmsKeyId: Optional[str] = None

class PersonalizationConfigurationTypeDef(BaseModel):
    personalizationControlMode: PersonalizationControlModeType

class QAppsConfigurationTypeDef(BaseModel):
    qAppsControlMode: QAppsControlModeType

class TagTypeDef(BaseModel):
    key: str
    value: str

class DataSourceVpcConfigurationTypeDef(BaseModel):
    subnetIds: Sequence[str]
    securityGroupIds: Sequence[str]

class IndexCapacityConfigurationTypeDef(BaseModel):
    units: Optional[int] = None

class UserAliasTypeDef(BaseModel):
    userId: str
    indexId: Optional[str] = None
    dataSourceId: Optional[str] = None

class CreatorModeConfigurationTypeDef(BaseModel):
    creatorModeControl: CreatorModeControlType

class DataSourceSyncJobMetricsTypeDef(BaseModel):
    documentsAdded: Optional[str] = None
    documentsModified: Optional[str] = None
    documentsDeleted: Optional[str] = None
    documentsFailed: Optional[str] = None
    documentsScanned: Optional[str] = None

class DataSourceTypeDef(BaseModel):
    displayName: Optional[str] = None
    dataSourceId: Optional[str] = None
    type: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    status: Optional[DataSourceStatusType] = None

class DataSourceVpcConfigurationOutputTypeDef(BaseModel):
    subnetIds: List[str]
    securityGroupIds: List[str]

class DateAttributeBoostingConfigurationTypeDef(BaseModel):
    boostingLevel: DocumentAttributeBoostingLevelType
    boostingDurationInSeconds: Optional[int] = None

class DeleteApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str

class DeleteChatControlsConfigurationRequestRequestTypeDef(BaseModel):
    applicationId: str

class DeleteConversationRequestRequestTypeDef(BaseModel):
    conversationId: str
    applicationId: str
    userId: Optional[str] = None

class DeleteDataSourceRequestRequestTypeDef(BaseModel):
    applicationId: str
    indexId: str
    dataSourceId: str

class DeleteGroupRequestRequestTypeDef(BaseModel):
    applicationId: str
    indexId: str
    groupName: str
    dataSourceId: Optional[str] = None

class DeleteIndexRequestRequestTypeDef(BaseModel):
    applicationId: str
    indexId: str

class DeletePluginRequestRequestTypeDef(BaseModel):
    applicationId: str
    pluginId: str

class DeleteRetrieverRequestRequestTypeDef(BaseModel):
    applicationId: str
    retrieverId: str

class DeleteUserRequestRequestTypeDef(BaseModel):
    applicationId: str
    userId: str

class DeleteWebExperienceRequestRequestTypeDef(BaseModel):
    applicationId: str
    webExperienceId: str

class NumberAttributeBoostingConfigurationTypeDef(BaseModel):
    boostingLevel: DocumentAttributeBoostingLevelType
    boostingType: Optional[NumberAttributeBoostingTypeType] = None

class StringAttributeBoostingConfigurationOutputTypeDef(BaseModel):
    boostingLevel: DocumentAttributeBoostingLevelType
    attributeValueBoosting: Optional[Dict[str, StringAttributeValueBoostingLevelType]] = None

class StringListAttributeBoostingConfigurationTypeDef(BaseModel):
    boostingLevel: DocumentAttributeBoostingLevelType

class StringAttributeBoostingConfigurationTypeDef(BaseModel):
    boostingLevel: DocumentAttributeBoostingLevelType
    attributeValueBoosting: Optional[Mapping[str, StringAttributeValueBoostingLevelType]] = None

class DocumentAttributeValueOutputTypeDef(BaseModel):
    stringValue: Optional[str] = None
    stringListValue: Optional[List[str]] = None
    longValue: Optional[int] = None
    dateValue: Optional[datetime] = None

class DocumentAttributeConfigurationTypeDef(BaseModel):
    name: Optional[str] = None
    type: Optional[AttributeTypeType] = None
    search: Optional[StatusType] = None

class GetApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class GetChatControlsConfigurationRequestRequestTypeDef(BaseModel):
    applicationId: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class GetDataSourceRequestRequestTypeDef(BaseModel):
    applicationId: str
    indexId: str
    dataSourceId: str

class GetGroupRequestRequestTypeDef(BaseModel):
    applicationId: str
    indexId: str
    groupName: str
    dataSourceId: Optional[str] = None

class GetIndexRequestRequestTypeDef(BaseModel):
    applicationId: str
    indexId: str

class GetPluginRequestRequestTypeDef(BaseModel):
    applicationId: str
    pluginId: str

class GetRetrieverRequestRequestTypeDef(BaseModel):
    applicationId: str
    retrieverId: str

class GetUserRequestRequestTypeDef(BaseModel):
    applicationId: str
    userId: str

class GetWebExperienceRequestRequestTypeDef(BaseModel):
    applicationId: str
    webExperienceId: str

class MemberGroupTypeDef(BaseModel):
    groupName: str
    type: Optional[MembershipTypeType] = None

class MemberUserTypeDef(BaseModel):
    userId: str
    type: Optional[MembershipTypeType] = None

class GroupSummaryTypeDef(BaseModel):
    groupName: Optional[str] = None

class TextDocumentStatisticsTypeDef(BaseModel):
    indexedTextBytes: Optional[int] = None
    indexedTextDocumentCount: Optional[int] = None

class IndexTypeDef(BaseModel):
    displayName: Optional[str] = None
    indexId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    status: Optional[IndexStatusType] = None

class KendraIndexConfigurationTypeDef(BaseModel):
    indexId: str

class ListApplicationsRequestRequestTypeDef(BaseModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListConversationsRequestRequestTypeDef(BaseModel):
    applicationId: str
    userId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDataSourcesRequestRequestTypeDef(BaseModel):
    applicationId: str
    indexId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListDocumentsRequestRequestTypeDef(BaseModel):
    applicationId: str
    indexId: str
    dataSourceIds: Optional[Sequence[str]] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListIndicesRequestRequestTypeDef(BaseModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListMessagesRequestRequestTypeDef(BaseModel):
    conversationId: str
    applicationId: str
    userId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class ListPluginsRequestRequestTypeDef(BaseModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class PluginTypeDef(BaseModel):
    pluginId: Optional[str] = None
    displayName: Optional[str] = None
    type: Optional[PluginTypeType] = None
    serverUrl: Optional[str] = None
    state: Optional[PluginStateType] = None
    buildStatus: Optional[PluginBuildStatusType] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class ListRetrieversRequestRequestTypeDef(BaseModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class RetrieverTypeDef(BaseModel):
    applicationId: Optional[str] = None
    retrieverId: Optional[str] = None
    type: Optional[RetrieverTypeType] = None
    status: Optional[RetrieverStatusType] = None
    displayName: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str

class ListWebExperiencesRequestRequestTypeDef(BaseModel):
    applicationId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class WebExperienceTypeDef(BaseModel):
    webExperienceId: Optional[str] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None
    defaultEndpoint: Optional[str] = None
    status: Optional[WebExperienceStatusType] = None

class OAuth2ClientCredentialConfigurationTypeDef(BaseModel):
    secretArn: str
    roleArn: str

class PrincipalGroupTypeDef(BaseModel):
    access: ReadAccessTypeType
    name: Optional[str] = None
    membershipType: Optional[MembershipTypeType] = None

class PrincipalUserTypeDef(BaseModel):
    access: ReadAccessTypeType
    id: Optional[str] = None
    membershipType: Optional[MembershipTypeType] = None

class UsersAndGroupsExtraOutputTypeDef(BaseModel):
    userIds: Optional[List[str]] = None
    userGroups: Optional[List[str]] = None

class UsersAndGroupsOutputTypeDef(BaseModel):
    userIds: Optional[List[str]] = None
    userGroups: Optional[List[str]] = None

class UsersAndGroupsTypeDef(BaseModel):
    userIds: Optional[Sequence[str]] = None
    userGroups: Optional[Sequence[str]] = None

class SamlConfigurationTypeDef(BaseModel):
    metadataXML: str
    roleArn: str
    userIdAttribute: str
    userGroupAttribute: Optional[str] = None

class SnippetExcerptTypeDef(BaseModel):
    text: Optional[str] = None

class StartDataSourceSyncJobRequestRequestTypeDef(BaseModel):
    dataSourceId: str
    applicationId: str
    indexId: str

class StopDataSourceSyncJobRequestRequestTypeDef(BaseModel):
    dataSourceId: str
    applicationId: str
    indexId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    tagKeys: Sequence[str]

class APISchemaTypeDef(BaseModel):
    payload: Optional[str] = None
    s3: Optional[S3TypeDef] = None

class ActionExecutionExtraOutputTypeDef(BaseModel):
    pluginId: str
    payload: Dict[str, ActionExecutionPayloadFieldExtraOutputTypeDef]
    payloadFieldNameSeparator: str

class ActionExecutionOutputTypeDef(BaseModel):
    pluginId: str
    payload: Dict[str, ActionExecutionPayloadFieldOutputTypeDef]
    payloadFieldNameSeparator: str

class ActionExecutionTypeDef(BaseModel):
    pluginId: str
    payload: Mapping[str, ActionExecutionPayloadFieldTypeDef]
    payloadFieldNameSeparator: str

class ActionReviewPayloadFieldTypeDef(BaseModel):
    displayName: Optional[str] = None
    displayOrder: Optional[int] = None
    displayDescription: Optional[str] = None
    type: Optional[ActionPayloadFieldTypeType] = None
    value: Optional[Dict[str, Any]] = None
    allowedValues: Optional[List[ActionReviewPayloadFieldAllowedValueTypeDef]] = None
    allowedFormat: Optional[str] = None
    required: Optional[bool] = None

class AttachmentInputTypeDef(BaseModel):
    name: str
    data: BlobTypeDef

class DocumentContentTypeDef(BaseModel):
    blob: Optional[BlobTypeDef] = None
    s3: Optional[S3TypeDef] = None

class AttachmentOutputTypeDef(BaseModel):
    name: Optional[str] = None
    status: Optional[AttachmentStatusType] = None
    error: Optional[ErrorDetailTypeDef] = None

class DocumentDetailsTypeDef(BaseModel):
    documentId: Optional[str] = None
    status: Optional[DocumentStatusType] = None
    error: Optional[ErrorDetailTypeDef] = None
    createdAt: Optional[datetime] = None
    updatedAt: Optional[datetime] = None

class FailedDocumentTypeDef(BaseModel):
    id: Optional[str] = None
    error: Optional[ErrorDetailTypeDef] = None
    dataSourceId: Optional[str] = None

class GroupStatusDetailTypeDef(BaseModel):
    status: Optional[GroupStatusType] = None
    lastUpdatedAt: Optional[datetime] = None
    errorDetail: Optional[ErrorDetailTypeDef] = None

class BatchDeleteDocumentRequestRequestTypeDef(BaseModel):
    applicationId: str
    indexId: str
    documents: Sequence[DeleteDocumentTypeDef]
    dataSourceSyncId: Optional[str] = None

class CreateApplicationResponseTypeDef(BaseModel):
    applicationId: str
    applicationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceResponseTypeDef(BaseModel):
    dataSourceId: str
    dataSourceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIndexResponseTypeDef(BaseModel):
    indexId: str
    indexArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePluginResponseTypeDef(BaseModel):
    pluginId: str
    pluginArn: str
    buildStatus: PluginBuildStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRetrieverResponseTypeDef(BaseModel):
    retrieverId: str
    retrieverArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWebExperienceResponseTypeDef(BaseModel):
    webExperienceId: str
    webExperienceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListApplicationsResponseTypeDef(BaseModel):
    nextToken: str
    applications: List[ApplicationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartDataSourceSyncJobResponseTypeDef(BaseModel):
    executionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChatModeConfigurationTypeDef(BaseModel):
    pluginConfiguration: Optional[PluginConfigurationTypeDef] = None

class ContentRetrievalRuleExtraOutputTypeDef(BaseModel):
    eligibleDataSources: Optional[List[EligibleDataSourceTypeDef]] = None

class ContentRetrievalRuleOutputTypeDef(BaseModel):
    eligibleDataSources: Optional[List[EligibleDataSourceTypeDef]] = None

class ContentRetrievalRuleTypeDef(BaseModel):
    eligibleDataSources: Optional[Sequence[EligibleDataSourceTypeDef]] = None

class ListConversationsResponseTypeDef(BaseModel):
    nextToken: str
    conversations: List[ConversationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetApplicationResponseTypeDef(BaseModel):
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

class UpdateApplicationRequestRequestTypeDef(BaseModel):
    applicationId: str
    identityCenterInstanceArn: Optional[str] = None
    displayName: Optional[str] = None
    description: Optional[str] = None
    roleArn: Optional[str] = None
    attachmentsConfiguration: Optional[AttachmentsConfigurationTypeDef] = None
    qAppsConfiguration: Optional[QAppsConfigurationTypeDef] = None
    personalizationConfiguration: Optional[PersonalizationConfigurationTypeDef] = None

class CreateApplicationRequestRequestTypeDef(BaseModel):
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

class CreateWebExperienceRequestRequestTypeDef(BaseModel):
    applicationId: str
    title: Optional[str] = None
    subtitle: Optional[str] = None
    welcomeMessage: Optional[str] = None
    samplePromptsControlMode: Optional[WebExperienceSamplePromptsControlModeType] = None
    roleArn: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    clientToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceARN: str
    tags: Sequence[TagTypeDef]

class CreateIndexRequestRequestTypeDef(BaseModel):
    applicationId: str
    displayName: str
    type: Optional[IndexTypeType] = None
    description: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    capacityConfiguration: Optional[IndexCapacityConfigurationTypeDef] = None
    clientToken: Optional[str] = None

class CreateUserRequestRequestTypeDef(BaseModel):
    applicationId: str
    userId: str
    userAliases: Optional[Sequence[UserAliasTypeDef]] = None
    clientToken: Optional[str] = None

class GetUserResponseTypeDef(BaseModel):
    userAliases: List[UserAliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserRequestRequestTypeDef(BaseModel):
    applicationId: str
    userId: str
    userAliasesToUpdate: Optional[Sequence[UserAliasTypeDef]] = None
    userAliasesToDelete: Optional[Sequence[UserAliasTypeDef]] = None

class UpdateUserResponseTypeDef(BaseModel):
    userAliasesAdded: List[UserAliasTypeDef]
    userAliasesUpdated: List[UserAliasTypeDef]
    userAliasesDeleted: List[UserAliasTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DataSourceSyncJobTypeDef(BaseModel):
    executionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    status: Optional[DataSourceSyncJobStatusType] = None
    error: Optional[ErrorDetailTypeDef] = None
    dataSourceErrorCode: Optional[str] = None
    metrics: Optional[DataSourceSyncJobMetricsTypeDef] = None

class ListDataSourcesResponseTypeDef(BaseModel):
    dataSources: List[DataSourceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DocumentAttributeBoostingConfigurationOutputTypeDef(BaseModel):
    numberConfiguration: Optional[NumberAttributeBoostingConfigurationTypeDef] = None
    stringConfiguration: Optional[StringAttributeBoostingConfigurationOutputTypeDef] = None
    dateConfiguration: Optional[DateAttributeBoostingConfigurationTypeDef] = None
    stringListConfiguration: Optional[StringListAttributeBoostingConfigurationTypeDef] = None

class DocumentAttributeBoostingConfigurationTypeDef(BaseModel):
    numberConfiguration: Optional[NumberAttributeBoostingConfigurationTypeDef] = None
    stringConfiguration: Optional[StringAttributeBoostingConfigurationTypeDef] = None
    dateConfiguration: Optional[DateAttributeBoostingConfigurationTypeDef] = None
    stringListConfiguration: Optional[StringListAttributeBoostingConfigurationTypeDef] = None

class DocumentAttributeConditionOutputTypeDef(BaseModel):
    key: str
    operator: DocumentEnrichmentConditionOperatorType
    value: Optional[DocumentAttributeValueOutputTypeDef] = None

class DocumentAttributeTargetOutputTypeDef(BaseModel):
    key: str
    value: Optional[DocumentAttributeValueOutputTypeDef] = None
    attributeValueOperator: Optional[Literal["DELETE"]] = None

class UpdateIndexRequestRequestTypeDef(BaseModel):
    applicationId: str
    indexId: str
    displayName: Optional[str] = None
    description: Optional[str] = None
    capacityConfiguration: Optional[IndexCapacityConfigurationTypeDef] = None
    documentAttributeConfigurations: Optional[       Sequence[DocumentAttributeConfigurationTypeDef]     ] = None

class DocumentAttributeValueTypeDef(BaseModel):
    stringValue: Optional[str] = None
    stringListValue: Optional[Sequence[str]] = None
    longValue: Optional[int] = None
    dateValue: Optional[TimestampTypeDef] = None

class ListDataSourceSyncJobsRequestRequestTypeDef(BaseModel):
    dataSourceId: str
    applicationId: str
    indexId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    statusFilter: Optional[DataSourceSyncJobStatusType] = None

class ListGroupsRequestRequestTypeDef(BaseModel):
    applicationId: str
    indexId: str
    updatedEarlierThan: TimestampTypeDef
    dataSourceId: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None

class MessageUsefulnessFeedbackTypeDef(BaseModel):
    usefulness: MessageUsefulnessType
    submittedAt: TimestampTypeDef
    reason: Optional[MessageUsefulnessReasonType] = None
    comment: Optional[str] = None

class GetChatControlsConfigurationRequestGetChatControlsConfigurationPaginateTypeDef(BaseModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApplicationsRequestListApplicationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListConversationsRequestListConversationsPaginateTypeDef(BaseModel):
    applicationId: str
    userId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourceSyncJobsRequestListDataSourceSyncJobsPaginateTypeDef(BaseModel):
    dataSourceId: str
    applicationId: str
    indexId: str
    startTime: Optional[TimestampTypeDef] = None
    endTime: Optional[TimestampTypeDef] = None
    statusFilter: Optional[DataSourceSyncJobStatusType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDataSourcesRequestListDataSourcesPaginateTypeDef(BaseModel):
    applicationId: str
    indexId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDocumentsRequestListDocumentsPaginateTypeDef(BaseModel):
    applicationId: str
    indexId: str
    dataSourceIds: Optional[Sequence[str]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListGroupsRequestListGroupsPaginateTypeDef(BaseModel):
    applicationId: str
    indexId: str
    updatedEarlierThan: TimestampTypeDef
    dataSourceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIndicesRequestListIndicesPaginateTypeDef(BaseModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListMessagesRequestListMessagesPaginateTypeDef(BaseModel):
    conversationId: str
    applicationId: str
    userId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPluginsRequestListPluginsPaginateTypeDef(BaseModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRetrieversRequestListRetrieversPaginateTypeDef(BaseModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListWebExperiencesRequestListWebExperiencesPaginateTypeDef(BaseModel):
    applicationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GroupMembersTypeDef(BaseModel):
    memberGroups: Optional[Sequence[MemberGroupTypeDef]] = None
    memberUsers: Optional[Sequence[MemberUserTypeDef]] = None

class ListGroupsResponseTypeDef(BaseModel):
    nextToken: str
    items: List[GroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class IndexStatisticsTypeDef(BaseModel):
    textDocumentStatistics: Optional[TextDocumentStatisticsTypeDef] = None

class ListIndicesResponseTypeDef(BaseModel):
    nextToken: str
    indices: List[IndexTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListPluginsResponseTypeDef(BaseModel):
    nextToken: str
    plugins: List[PluginTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListRetrieversResponseTypeDef(BaseModel):
    retrievers: List[RetrieverTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListWebExperiencesResponseTypeDef(BaseModel):
    webExperiences: List[WebExperienceTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class PluginAuthConfigurationOutputTypeDef(BaseModel):
    basicAuthConfiguration: Optional[BasicAuthConfigurationTypeDef] = None
    oAuth2ClientCredentialConfiguration: Optional[       OAuth2ClientCredentialConfigurationTypeDef     ] = None
    noAuthConfiguration: Optional[Dict[str, Any]] = None

class PluginAuthConfigurationTypeDef(BaseModel):
    basicAuthConfiguration: Optional[BasicAuthConfigurationTypeDef] = None
    oAuth2ClientCredentialConfiguration: Optional[       OAuth2ClientCredentialConfigurationTypeDef     ] = None
    noAuthConfiguration: Optional[Mapping[str, Any]] = None

class PrincipalTypeDef(BaseModel):
    user: Optional[PrincipalUserTypeDef] = None
    group: Optional[PrincipalGroupTypeDef] = None

class WebExperienceAuthConfigurationTypeDef(BaseModel):
    samlConfiguration: Optional[SamlConfigurationTypeDef] = None

class TextSegmentTypeDef(BaseModel):
    beginOffset: Optional[int] = None
    endOffset: Optional[int] = None
    snippetExcerpt: Optional[SnippetExcerptTypeDef] = None

class CustomPluginConfigurationTypeDef(BaseModel):
    description: str
    apiSchemaType: Literal["OPEN_API_V3"]
    apiSchema: APISchemaTypeDef

class ActionReviewTypeDef(BaseModel):
    pluginId: Optional[str] = None
    pluginType: Optional[PluginTypeType] = None
    payload: Optional[Dict[str, ActionReviewPayloadFieldTypeDef]] = None
    payloadFieldNameSeparator: Optional[str] = None

class ListDocumentsResponseTypeDef(BaseModel):
    documentDetailList: List[DocumentDetailsTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeleteDocumentResponseTypeDef(BaseModel):
    failedDocuments: List[FailedDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutDocumentResponseTypeDef(BaseModel):
    failedDocuments: List[FailedDocumentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetGroupResponseTypeDef(BaseModel):
    status: GroupStatusDetailTypeDef
    statusHistory: List[GroupStatusDetailTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ChatSyncInputRequestTypeDef(BaseModel):
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

class RuleConfigurationExtraOutputTypeDef(BaseModel):
    contentBlockerRule: Optional[ContentBlockerRuleTypeDef] = None
    contentRetrievalRule: Optional[ContentRetrievalRuleExtraOutputTypeDef] = None

class RuleConfigurationOutputTypeDef(BaseModel):
    contentBlockerRule: Optional[ContentBlockerRuleTypeDef] = None
    contentRetrievalRule: Optional[ContentRetrievalRuleOutputTypeDef] = None

class RuleConfigurationTypeDef(BaseModel):
    contentBlockerRule: Optional[ContentBlockerRuleTypeDef] = None
    contentRetrievalRule: Optional[ContentRetrievalRuleTypeDef] = None

class ListDataSourceSyncJobsResponseTypeDef(BaseModel):
    history: List[DataSourceSyncJobTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class NativeIndexConfigurationOutputTypeDef(BaseModel):
    indexId: str
    boostingOverride: Optional[       Dict[str, DocumentAttributeBoostingConfigurationOutputTypeDef] = None

class NativeIndexConfigurationTypeDef(BaseModel):
    indexId: str
    boostingOverride: Optional[       Mapping[str, DocumentAttributeBoostingConfigurationTypeDef] = None

class HookConfigurationOutputTypeDef(BaseModel):
    invocationCondition: Optional[DocumentAttributeConditionOutputTypeDef] = None
    lambdaArn: Optional[str] = None
    s3BucketName: Optional[str] = None
    roleArn: Optional[str] = None

class InlineDocumentEnrichmentConfigurationOutputTypeDef(BaseModel):
    condition: Optional[DocumentAttributeConditionOutputTypeDef] = None
    target: Optional[DocumentAttributeTargetOutputTypeDef] = None
    documentContentOperator: Optional[Literal["DELETE"]] = None

class DocumentAttributeConditionTypeDef(BaseModel):
    key: str
    operator: DocumentEnrichmentConditionOperatorType
    value: Optional[DocumentAttributeValueTypeDef] = None

class DocumentAttributeTargetTypeDef(BaseModel):
    key: str
    value: Optional[DocumentAttributeValueTypeDef] = None
    attributeValueOperator: Optional[Literal["DELETE"]] = None

class DocumentAttributeTypeDef(BaseModel):
    name: str
    value: DocumentAttributeValueTypeDef

class PutFeedbackRequestRequestTypeDef(BaseModel):
    applicationId: str
    conversationId: str
    messageId: str
    userId: Optional[str] = None
    messageCopiedAt: Optional[TimestampTypeDef] = None
    messageUsefulness: Optional[MessageUsefulnessFeedbackTypeDef] = None

class PutGroupRequestRequestTypeDef(BaseModel):
    applicationId: str
    indexId: str
    groupName: str
    type: MembershipTypeType
    groupMembers: GroupMembersTypeDef
    dataSourceId: Optional[str] = None

class GetIndexResponseTypeDef(BaseModel):
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

class AccessControlTypeDef(BaseModel):
    principals: Sequence[PrincipalTypeDef]
    memberRelation: Optional[MemberRelationType] = None

class GetWebExperienceResponseTypeDef(BaseModel):
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

class UpdateWebExperienceRequestRequestTypeDef(BaseModel):
    applicationId: str
    webExperienceId: str
    roleArn: Optional[str] = None
    authenticationConfiguration: Optional[WebExperienceAuthConfigurationTypeDef] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    welcomeMessage: Optional[str] = None
    samplePromptsControlMode: Optional[WebExperienceSamplePromptsControlModeType] = None

class SourceAttributionTypeDef(BaseModel):
    title: Optional[str] = None
    snippet: Optional[str] = None
    url: Optional[str] = None
    citationNumber: Optional[int] = None
    updatedAt: Optional[datetime] = None
    textMessageSegments: Optional[List[TextSegmentTypeDef]] = None

class CreatePluginRequestRequestTypeDef(BaseModel):
    applicationId: str
    displayName: str
    type: PluginTypeType
    authConfiguration: PluginAuthConfigurationTypeDef
    serverUrl: Optional[str] = None
    customPluginConfiguration: Optional[CustomPluginConfigurationTypeDef] = None
    tags: Optional[Sequence[TagTypeDef]] = None
    clientToken: Optional[str] = None

class GetPluginResponseTypeDef(BaseModel):
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

class UpdatePluginRequestRequestTypeDef(BaseModel):
    applicationId: str
    pluginId: str
    displayName: Optional[str] = None
    state: Optional[PluginStateType] = None
    serverUrl: Optional[str] = None
    customPluginConfiguration: Optional[CustomPluginConfigurationTypeDef] = None
    authConfiguration: Optional[PluginAuthConfigurationTypeDef] = None

class RuleExtraOutputTypeDef(BaseModel):
    ruleType: RuleTypeType
    includedUsersAndGroups: Optional[UsersAndGroupsExtraOutputTypeDef] = None
    excludedUsersAndGroups: Optional[UsersAndGroupsExtraOutputTypeDef] = None
    ruleConfiguration: Optional[RuleConfigurationExtraOutputTypeDef] = None

class RuleOutputTypeDef(BaseModel):
    ruleType: RuleTypeType
    includedUsersAndGroups: Optional[UsersAndGroupsOutputTypeDef] = None
    excludedUsersAndGroups: Optional[UsersAndGroupsOutputTypeDef] = None
    ruleConfiguration: Optional[RuleConfigurationOutputTypeDef] = None

class RuleTypeDef(BaseModel):
    ruleType: RuleTypeType
    includedUsersAndGroups: Optional[UsersAndGroupsTypeDef] = None
    excludedUsersAndGroups: Optional[UsersAndGroupsTypeDef] = None
    ruleConfiguration: Optional[RuleConfigurationTypeDef] = None

class RetrieverConfigurationOutputTypeDef(BaseModel):
    nativeIndexConfiguration: Optional[NativeIndexConfigurationOutputTypeDef] = None
    kendraIndexConfiguration: Optional[KendraIndexConfigurationTypeDef] = None

class RetrieverConfigurationTypeDef(BaseModel):
    nativeIndexConfiguration: Optional[NativeIndexConfigurationTypeDef] = None
    kendraIndexConfiguration: Optional[KendraIndexConfigurationTypeDef] = None

class DocumentEnrichmentConfigurationOutputTypeDef(BaseModel):
    inlineConfigurations: Optional[       List[InlineDocumentEnrichmentConfigurationOutputTypeDef]     ] = None
    preExtractionHookConfiguration: Optional[HookConfigurationOutputTypeDef] = None
    postExtractionHookConfiguration: Optional[HookConfigurationOutputTypeDef] = None

class HookConfigurationTypeDef(BaseModel):
    invocationCondition: Optional[DocumentAttributeConditionTypeDef] = None
    lambdaArn: Optional[str] = None
    s3BucketName: Optional[str] = None
    roleArn: Optional[str] = None

class InlineDocumentEnrichmentConfigurationTypeDef(BaseModel):
    condition: Optional[DocumentAttributeConditionTypeDef] = None
    target: Optional[DocumentAttributeTargetTypeDef] = None
    documentContentOperator: Optional[Literal["DELETE"]] = None

class AttributeFilterTypeDef(BaseModel):
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

class AccessConfigurationTypeDef(BaseModel):
    accessControls: Sequence[AccessControlTypeDef]
    memberRelation: Optional[MemberRelationType] = None

class ChatSyncOutputTypeDef(BaseModel):
    conversationId: str
    systemMessage: str
    systemMessageId: str
    userMessageId: str
    actionReview: ActionReviewTypeDef
    authChallengeRequest: AuthChallengeRequestTypeDef
    sourceAttributions: List[SourceAttributionTypeDef]
    failedAttachments: List[AttachmentOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MessageTypeDef(BaseModel):
    messageId: Optional[str] = None
    body: Optional[str] = None
    time: Optional[datetime] = None
    type: Optional[MessageTypeType] = None
    attachments: Optional[List[AttachmentOutputTypeDef]] = None
    sourceAttribution: Optional[List[SourceAttributionTypeDef]] = None
    actionReview: Optional[ActionReviewTypeDef] = None
    actionExecution: Optional[ActionExecutionOutputTypeDef] = None

class TopicConfigurationExtraOutputTypeDef(BaseModel):
    name: str
    rules: List[RuleExtraOutputTypeDef]
    description: Optional[str] = None
    exampleChatMessages: Optional[List[str]] = None

class TopicConfigurationOutputTypeDef(BaseModel):
    name: str
    rules: List[RuleOutputTypeDef]
    description: Optional[str] = None
    exampleChatMessages: Optional[List[str]] = None

class TopicConfigurationTypeDef(BaseModel):
    name: str
    rules: Sequence[RuleTypeDef]
    description: Optional[str] = None
    exampleChatMessages: Optional[Sequence[str]] = None

class GetRetrieverResponseTypeDef(BaseModel):
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

class CreateRetrieverRequestRequestTypeDef(BaseModel):
    applicationId: str
    type: RetrieverTypeType
    displayName: str
    configuration: RetrieverConfigurationTypeDef
    roleArn: Optional[str] = None
    clientToken: Optional[str] = None
    tags: Optional[Sequence[TagTypeDef]] = None

class UpdateRetrieverRequestRequestTypeDef(BaseModel):
    applicationId: str
    retrieverId: str
    configuration: Optional[RetrieverConfigurationTypeDef] = None
    displayName: Optional[str] = None
    roleArn: Optional[str] = None

class GetDataSourceResponseTypeDef(BaseModel):
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

class DocumentEnrichmentConfigurationTypeDef(BaseModel):
    inlineConfigurations: Optional[Sequence[InlineDocumentEnrichmentConfigurationTypeDef]] = None
    preExtractionHookConfiguration: Optional[HookConfigurationTypeDef] = None
    postExtractionHookConfiguration: Optional[HookConfigurationTypeDef] = None

class ListMessagesResponseTypeDef(BaseModel):
    messages: List[MessageTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetChatControlsConfigurationResponseTypeDef(BaseModel):
    responseScope: ResponseScopeType
    blockedPhrases: BlockedPhrasesConfigurationTypeDef
    topicConfigurations: List[TopicConfigurationExtraOutputTypeDef]
    creatorModeConfiguration: AppliedCreatorModeConfigurationTypeDef
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateDataSourceRequestRequestTypeDef(BaseModel):
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

class DocumentTypeDef(BaseModel):
    id: str
    attributes: Optional[Sequence[DocumentAttributeTypeDef]] = None
    content: Optional[DocumentContentTypeDef] = None
    contentType: Optional[ContentTypeType] = None
    title: Optional[str] = None
    accessConfiguration: Optional[AccessConfigurationTypeDef] = None
    documentEnrichmentConfiguration: Optional[DocumentEnrichmentConfigurationTypeDef] = None

class UpdateDataSourceRequestRequestTypeDef(BaseModel):
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

class UpdateChatControlsConfigurationRequestRequestTypeDef(BaseModel):
    applicationId: str
    clientToken: Optional[str] = None
    responseScope: Optional[ResponseScopeType] = None
    blockedPhrasesConfigurationUpdate: Optional[BlockedPhrasesConfigurationUpdateTypeDef] = None
    topicConfigurationsToCreateOrUpdate: Optional[       Sequence[TopicConfigurationUnionTypeDef]     ] = None
    topicConfigurationsToDelete: Optional[Sequence[TopicConfigurationUnionTypeDef]] = None
    creatorModeConfiguration: Optional[CreatorModeConfigurationTypeDef] = None

class BatchPutDocumentRequestRequestTypeDef(BaseModel):
    applicationId: str
    indexId: str
    documents: Sequence[DocumentTypeDef]
    roleArn: Optional[str] = None
    dataSourceSyncId: Optional[str] = None

