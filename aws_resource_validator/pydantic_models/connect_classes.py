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
from aws_resource_validator.pydantic_models.connect_constants import *

class ActionSummary(BaseValidatorModel):
    ActionType: ActionTypeType


class ActivateEvaluationFormRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class EmailRecipient(BaseValidatorModel):
    Address: Optional[str] = None
    DisplayName: Optional[str] = None


class Distribution(BaseValidatorModel):
    Region: str
    Percentage: int


class QueueReference(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None


class AgentHierarchyGroup(BaseValidatorModel):
    Arn: Optional[str] = None


class AgentHierarchyGroups(BaseValidatorModel):
    L1Ids: Optional[Sequence[str]] = None
    L2Ids: Optional[Sequence[str]] = None
    L3Ids: Optional[Sequence[str]] = None
    L4Ids: Optional[Sequence[str]] = None
    L5Ids: Optional[Sequence[str]] = None


class DeviceInfo(BaseValidatorModel):
    PlatformName: Optional[str] = None
    PlatformVersion: Optional[str] = None
    OperatingSystem: Optional[str] = None


class ParticipantCapabilities(BaseValidatorModel):
    Video: Optional[Literal["SEND"]] = None
    ScreenShare: Optional[Literal["SEND"]] = None


class AudioQualityMetricsInfo(BaseValidatorModel):
    QualityScore: Optional[float] = None
    PotentialQualityIssues: Optional[List[str]] = None


class AgentStatusReference(BaseValidatorModel):
    StatusStartTimestamp: Optional[datetime] = None
    StatusArn: Optional[str] = None
    StatusName: Optional[str] = None


class AgentsCriteriaOutput(BaseValidatorModel):
    AgentIds: Optional[List[str]] = None


class AgentsCriteria(BaseValidatorModel):
    AgentIds: Optional[Sequence[str]] = None


class AnalyticsDataAssociationResult(BaseValidatorModel):
    DataSetId: Optional[str] = None
    TargetAccountId: Optional[str] = None
    ResourceShareId: Optional[str] = None
    ResourceShareArn: Optional[str] = None
    ResourceShareStatus: Optional[str] = None


class AnalyticsDataSetsResult(BaseValidatorModel):
    DataSetId: Optional[str] = None
    DataSetName: Optional[str] = None


class AnswerMachineDetectionConfig(BaseValidatorModel):
    EnableAnswerMachineDetection: Optional[bool] = None
    AwaitAnswerMachinePrompt: Optional[bool] = None


class ApplicationOutput(BaseValidatorModel):
    Namespace: Optional[str] = None
    ApplicationPermissions: Optional[List[str]] = None


class Application(BaseValidatorModel):
    Namespace: Optional[str] = None
    ApplicationPermissions: Optional[Sequence[str]] = None


class AssociateAnalyticsDataSetRequest(BaseValidatorModel):
    InstanceId: str
    DataSetId: str
    TargetAccountId: Optional[str] = None


class AssociateApprovedOriginRequest(BaseValidatorModel):
    InstanceId: str
    Origin: str
    ClientToken: Optional[str] = None


class LexBot(BaseValidatorModel):
    Name: str
    LexRegion: str


class LexV2Bot(BaseValidatorModel):
    AliasArn: Optional[str] = None


class AssociateDefaultVocabularyRequest(BaseValidatorModel):
    InstanceId: str
    LanguageCode: VocabularyLanguageCodeType
    VocabularyId: Optional[str] = None


class AssociateFlowRequest(BaseValidatorModel):
    InstanceId: str
    ResourceId: str
    FlowId: str
    ResourceType: FlowAssociationResourceTypeType


class AssociateLambdaFunctionRequest(BaseValidatorModel):
    InstanceId: str
    FunctionArn: str
    ClientToken: Optional[str] = None


class AssociatePhoneNumberContactFlowRequest(BaseValidatorModel):
    PhoneNumberId: str
    InstanceId: str
    ContactFlowId: str


class AssociateQueueQuickConnectsRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    QuickConnectIds: Sequence[str]


class AssociateSecurityKeyRequest(BaseValidatorModel):
    InstanceId: str
    Key: str
    ClientToken: Optional[str] = None


class AssociateTrafficDistributionGroupUserRequest(BaseValidatorModel):
    TrafficDistributionGroupId: str
    UserId: str
    InstanceId: str


class UserProficiency(BaseValidatorModel):
    AttributeName: str
    AttributeValue: str
    Level: float


class AssociatedContactSummary(BaseValidatorModel):
    ContactId: Optional[str] = None
    ContactArn: Optional[str] = None
    InitiationTimestamp: Optional[datetime] = None
    DisconnectTimestamp: Optional[datetime] = None
    InitialContactId: Optional[str] = None
    PreviousContactId: Optional[str] = None
    RelatedContactId: Optional[str] = None
    InitiationMethod: Optional[ContactInitiationMethodType] = None
    Channel: Optional[ChannelType] = None


class AttachedFileError(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    FileId: Optional[str] = None


class CreatedByInfo(BaseValidatorModel):
    ConnectUserArn: Optional[str] = None
    AWSIdentityArn: Optional[str] = None


class AttachmentReference(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    Status: Optional[ReferenceStatusType] = None
    Arn: Optional[str] = None


class Attendee(BaseValidatorModel):
    AttendeeId: Optional[str] = None
    JoinToken: Optional[str] = None


class HierarchyGroupCondition(BaseValidatorModel):
    Value: Optional[str] = None
    HierarchyGroupMatchType: Optional[HierarchyGroupMatchTypeType] = None


class TagCondition(BaseValidatorModel):
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None


class Range(BaseValidatorModel):
    MinProficiencyLevel: Optional[float] = None
    MaxProficiencyLevel: Optional[float] = None


class Attribute(BaseValidatorModel):
    AttributeType: Optional[InstanceAttributeTypeType] = None
    Value: Optional[str] = None


class AudioFeatures(BaseValidatorModel):
    EchoReduction: Optional[MeetingFeatureStatusType] = None


class AuthenticationProfileSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    IsDefault: Optional[bool] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class AuthenticationProfile(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    AllowedIps: Optional[List[str]] = None
    BlockedIps: Optional[List[str]] = None
    IsDefault: Optional[bool] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None
    PeriodicSessionDuration: Optional[int] = None
    MaxSessionDuration: Optional[int] = None


class AvailableNumberSummary(BaseValidatorModel):
    PhoneNumber: Optional[str] = None
    PhoneNumberCountryCode: Optional[PhoneNumberCountryCodeType] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None


class BatchAssociateAnalyticsDataSetRequest(BaseValidatorModel):
    InstanceId: str
    DataSetIds: Sequence[str]
    TargetAccountId: Optional[str] = None


class ErrorResult(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class BatchDisassociateAnalyticsDataSetRequest(BaseValidatorModel):
    InstanceId: str
    DataSetIds: Sequence[str]
    TargetAccountId: Optional[str] = None


class BatchGetAttachedFileMetadataRequest(BaseValidatorModel):
    FileIds: Sequence[str]
    InstanceId: str
    AssociatedResourceArn: str


class BatchGetFlowAssociationRequest(BaseValidatorModel):
    InstanceId: str
    ResourceIds: Sequence[str]
    ResourceType: Optional[ListFlowAssociationResourceTypeType] = None


class FlowAssociationSummary(BaseValidatorModel):
    ResourceId: Optional[str] = None
    FlowId: Optional[str] = None
    ResourceType: Optional[ListFlowAssociationResourceTypeType] = None


class FailedRequest(BaseValidatorModel):
    RequestIdentifier: Optional[str] = None
    FailureReasonCode: Optional[FailureReasonCodeType] = None
    FailureReasonMessage: Optional[str] = None


class SuccessfulRequest(BaseValidatorModel):
    RequestIdentifier: Optional[str] = None
    ContactId: Optional[str] = None


class Campaign(BaseValidatorModel):
    CampaignId: Optional[str] = None


class ChatMessage(BaseValidatorModel):
    ContentType: str
    Content: str


class ChatStreamingConfiguration(BaseValidatorModel):
    StreamingEndpointArn: str


class ClaimPhoneNumberRequest(BaseValidatorModel):
    PhoneNumber: str
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberDescription: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None


class PhoneNumberStatus(BaseValidatorModel):
    Status: Optional[PhoneNumberWorkflowStatusType] = None
    Message: Optional[str] = None


class CompleteAttachedFileUploadRequest(BaseValidatorModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str


class ContactConfiguration(BaseValidatorModel):
    ContactId: str
    ParticipantRole: Optional[ParticipantRoleType] = None
    IncludeRawMessage: Optional[bool] = None


class ContactFilter(BaseValidatorModel):
    ContactStates: Optional[Sequence[ContactStateType]] = None


class ContactFlowModuleSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[ContactFlowModuleStateType] = None


class ContactFlowModule(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Content: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[ContactFlowModuleStateType] = None
    Status: Optional[ContactFlowModuleStatusType] = None
    Tags: Optional[Dict[str, str]] = None


class ContactFlowSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ContactFlowType: Optional[ContactFlowTypeType] = None
    ContactFlowState: Optional[ContactFlowStateType] = None
    ContactFlowStatus: Optional[ContactFlowStatusType] = None


class ContactFlowVersionSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    VersionDescription: Optional[str] = None
    Version: Optional[int] = None


class ContactSearchSummaryAgentInfo(BaseValidatorModel):
    Id: Optional[str] = None
    ConnectedToAgentTimestamp: Optional[datetime] = None


class ContactSearchSummaryQueueInfo(BaseValidatorModel):
    Id: Optional[str] = None
    EnqueueTimestamp: Optional[datetime] = None


class ContactSearchSummarySegmentAttributeValue(BaseValidatorModel):
    ValueString: Optional[str] = None


class CustomerVoiceActivity(BaseValidatorModel):
    GreetingStartTimestamp: Optional[datetime] = None
    GreetingEndTimestamp: Optional[datetime] = None


class DisconnectDetails(BaseValidatorModel):
    PotentialDisconnectIssue: Optional[str] = None


class QueueInfo(BaseValidatorModel):
    Id: Optional[str] = None
    EnqueueTimestamp: Optional[datetime] = None


class SegmentAttributeValueOutput(BaseValidatorModel):
    ValueString: Optional[str] = None
    ValueMap: Optional[Dict[str, Dict[str, Any]]] = None
    ValueInteger: Optional[int] = None


class WisdomInfo(BaseValidatorModel):
    SessionArn: Optional[str] = None


class CreateAgentStatusRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    State: AgentStatusStateType
    Description: Optional[str] = None
    DisplayOrder: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateContactFlowModuleRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    Content: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None


class UserInfo(BaseValidatorModel):
    UserId: Optional[str] = None


class CreateEmailAddressRequest(BaseValidatorModel):
    InstanceId: str
    EmailAddress: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None


class EvaluationFormScoringStrategy(BaseValidatorModel):
    Mode: EvaluationFormScoringModeType
    Status: EvaluationFormScoringStatusType


class CreateInstanceRequest(BaseValidatorModel):
    IdentityManagementType: DirectoryTypeType
    InboundCallsEnabled: bool
    OutboundCallsEnabled: bool
    ClientToken: Optional[str] = None
    InstanceAlias: Optional[str] = None
    DirectoryId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateIntegrationAssociationRequest(BaseValidatorModel):
    InstanceId: str
    IntegrationType: IntegrationTypeType
    IntegrationArn: str
    SourceApplicationUrl: Optional[str] = None
    SourceApplicationName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Tags: Optional[Mapping[str, str]] = None


class ParticipantDetailsToAdd(BaseValidatorModel):
    ParticipantRole: Optional[ParticipantRoleType] = None
    DisplayName: Optional[str] = None


class ParticipantTokenCredentials(BaseValidatorModel):
    ParticipantToken: Optional[str] = None
    Expiry: Optional[str] = None


class CreatePersistentContactAssociationRequest(BaseValidatorModel):
    InstanceId: str
    InitialContactId: str
    RehydrationType: RehydrationTypeType
    SourceContactId: str
    ClientToken: Optional[str] = None


class CreatePromptRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    S3Uri: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class OutboundCallerConfig(BaseValidatorModel):
    OutboundCallerIdName: Optional[str] = None
    OutboundCallerIdNumberId: Optional[str] = None
    OutboundFlowId: Optional[str] = None


class OutboundEmailConfig(BaseValidatorModel):
    OutboundEmailAddressId: Optional[str] = None


class RuleTriggerEventSource(BaseValidatorModel):
    EventSourceName: EventSourceNameType
    IntegrationAssociationId: Optional[str] = None


class CreateTrafficDistributionGroupRequest(BaseValidatorModel):
    Name: str
    InstanceId: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateUseCaseRequest(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    UseCaseType: UseCaseTypeType
    Tags: Optional[Mapping[str, str]] = None


class CreateUserHierarchyGroupRequest(BaseValidatorModel):
    Name: str
    InstanceId: str
    ParentGroupId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UserIdentityInfo(BaseValidatorModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Email: Optional[str] = None
    SecondaryEmail: Optional[str] = None
    Mobile: Optional[str] = None


class UserPhoneConfig(BaseValidatorModel):
    PhoneType: PhoneTypeType
    AutoAccept: Optional[bool] = None
    AfterContactWorkTimeLimit: Optional[int] = None
    DeskPhoneNumber: Optional[str] = None


class ViewInputContent(BaseValidatorModel):
    Template: Optional[str] = None
    Actions: Optional[Sequence[str]] = None


class CreateViewVersionRequest(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    VersionDescription: Optional[str] = None
    ViewContentSha256: Optional[str] = None


class CreateVocabularyRequest(BaseValidatorModel):
    InstanceId: str
    VocabularyName: str
    LanguageCode: VocabularyLanguageCodeType
    Content: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class Credentials(BaseValidatorModel):
    AccessToken: Optional[str] = None
    AccessTokenExpiration: Optional[datetime] = None
    RefreshToken: Optional[str] = None
    RefreshTokenExpiration: Optional[datetime] = None


class CrossChannelBehavior(BaseValidatorModel):
    BehaviorType: BehaviorTypeType


class CurrentMetric(BaseValidatorModel):
    Name: Optional[CurrentMetricNameType] = None
    Unit: Optional[UnitType] = None


class CurrentMetricSortCriteria(BaseValidatorModel):
    SortByMetric: Optional[CurrentMetricNameType] = None
    SortOrder: Optional[SortOrderType] = None


class DateReference(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class DeactivateEvaluationFormRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int


class DefaultVocabulary(BaseValidatorModel):
    InstanceId: str
    LanguageCode: VocabularyLanguageCodeType
    VocabularyId: str
    VocabularyName: str


class DeleteAttachedFileRequest(BaseValidatorModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str


class DeleteContactEvaluationRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str


class DeleteContactFlowModuleRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleId: str


class DeleteContactFlowRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str


class DeleteContactFlowVersionRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    ContactFlowVersion: int


class DeleteEmailAddressRequest(BaseValidatorModel):
    InstanceId: str
    EmailAddressId: str


class DeleteEvaluationFormRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: Optional[int] = None


class DeleteHoursOfOperationOverrideRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    HoursOfOperationOverrideId: str


class DeleteHoursOfOperationRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str


class DeleteInstanceRequest(BaseValidatorModel):
    InstanceId: str
    ClientToken: Optional[str] = None


class DeleteIntegrationAssociationRequest(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str


class DeletePredefinedAttributeRequest(BaseValidatorModel):
    InstanceId: str
    Name: str


class DeletePromptRequest(BaseValidatorModel):
    InstanceId: str
    PromptId: str


class DeletePushNotificationRegistrationRequest(BaseValidatorModel):
    InstanceId: str
    RegistrationId: str
    ContactId: str


class DeleteQueueRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str


class DeleteQuickConnectRequest(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str


class DeleteRoutingProfileRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str


class DeleteRuleRequest(BaseValidatorModel):
    InstanceId: str
    RuleId: str


class DeleteSecurityProfileRequest(BaseValidatorModel):
    InstanceId: str
    SecurityProfileId: str


class DeleteTaskTemplateRequest(BaseValidatorModel):
    InstanceId: str
    TaskTemplateId: str


class DeleteTrafficDistributionGroupRequest(BaseValidatorModel):
    TrafficDistributionGroupId: str


class DeleteUseCaseRequest(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    UseCaseId: str


class DeleteUserHierarchyGroupRequest(BaseValidatorModel):
    HierarchyGroupId: str
    InstanceId: str


class DeleteUserRequest(BaseValidatorModel):
    InstanceId: str
    UserId: str


class DeleteViewRequest(BaseValidatorModel):
    InstanceId: str
    ViewId: str


class DeleteViewVersionRequest(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    ViewVersion: int


class DeleteVocabularyRequest(BaseValidatorModel):
    InstanceId: str
    VocabularyId: str


class DescribeAgentStatusRequest(BaseValidatorModel):
    InstanceId: str
    AgentStatusId: str


class DescribeAuthenticationProfileRequest(BaseValidatorModel):
    AuthenticationProfileId: str
    InstanceId: str


class DescribeContactEvaluationRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str


class DescribeContactFlowModuleRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleId: str


class DescribeContactFlowRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str


class DescribeContactRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str


class DescribeEmailAddressRequest(BaseValidatorModel):
    InstanceId: str
    EmailAddressId: str


class DescribeEvaluationFormRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: Optional[int] = None


class DescribeHoursOfOperationOverrideRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    HoursOfOperationOverrideId: str


class DescribeHoursOfOperationRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str


class DescribeInstanceAttributeRequest(BaseValidatorModel):
    InstanceId: str
    AttributeType: InstanceAttributeTypeType


class DescribeInstanceRequest(BaseValidatorModel):
    InstanceId: str


class DescribeInstanceStorageConfigRequest(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType


class DescribePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


class DescribePredefinedAttributeRequest(BaseValidatorModel):
    InstanceId: str
    Name: str


class DescribePromptRequest(BaseValidatorModel):
    InstanceId: str
    PromptId: str


class Prompt(BaseValidatorModel):
    PromptARN: Optional[str] = None
    PromptId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class DescribeQueueRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str


class DescribeQuickConnectRequest(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str


class DescribeRoutingProfileRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str


class DescribeRuleRequest(BaseValidatorModel):
    InstanceId: str
    RuleId: str


class DescribeSecurityProfileRequest(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str


class SecurityProfile(BaseValidatorModel):
    Id: Optional[str] = None
    OrganizationResourceId: Optional[str] = None
    Arn: Optional[str] = None
    SecurityProfileName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    AllowedAccessControlTags: Optional[Dict[str, str]] = None
    TagRestrictedResources: Optional[List[str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None
    HierarchyRestrictedResources: Optional[List[str]] = None
    AllowedAccessControlHierarchyGroupId: Optional[str] = None


class DescribeTrafficDistributionGroupRequest(BaseValidatorModel):
    TrafficDistributionGroupId: str


class TrafficDistributionGroup(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    InstanceArn: Optional[str] = None
    Status: Optional[TrafficDistributionGroupStatusType] = None
    Tags: Optional[Dict[str, str]] = None
    IsDefault: Optional[bool] = None


class DescribeUserHierarchyGroupRequest(BaseValidatorModel):
    HierarchyGroupId: str
    InstanceId: str


class DescribeUserHierarchyStructureRequest(BaseValidatorModel):
    InstanceId: str


class DescribeUserRequest(BaseValidatorModel):
    UserId: str
    InstanceId: str


class DescribeViewRequest(BaseValidatorModel):
    InstanceId: str
    ViewId: str


class DescribeVocabularyRequest(BaseValidatorModel):
    InstanceId: str
    VocabularyId: str


class Vocabulary(BaseValidatorModel):
    Name: str
    Id: str
    Arn: str
    LanguageCode: VocabularyLanguageCodeType
    State: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: Optional[str] = None
    Content: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class RoutingProfileReference(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None


class DisassociateAnalyticsDataSetRequest(BaseValidatorModel):
    InstanceId: str
    DataSetId: str
    TargetAccountId: Optional[str] = None


class DisassociateApprovedOriginRequest(BaseValidatorModel):
    InstanceId: str
    Origin: str
    ClientToken: Optional[str] = None


class DisassociateFlowRequest(BaseValidatorModel):
    InstanceId: str
    ResourceId: str
    ResourceType: FlowAssociationResourceTypeType


class DisassociateInstanceStorageConfigRequest(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType
    ClientToken: Optional[str] = None


class DisassociateLambdaFunctionRequest(BaseValidatorModel):
    InstanceId: str
    FunctionArn: str
    ClientToken: Optional[str] = None


class DisassociateLexBotRequest(BaseValidatorModel):
    InstanceId: str
    BotName: str
    LexRegion: str
    ClientToken: Optional[str] = None


class DisassociatePhoneNumberContactFlowRequest(BaseValidatorModel):
    PhoneNumberId: str
    InstanceId: str


class DisassociateQueueQuickConnectsRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    QuickConnectIds: Sequence[str]


class RoutingProfileQueueReference(BaseValidatorModel):
    QueueId: str
    Channel: ChannelType


class DisassociateSecurityKeyRequest(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ClientToken: Optional[str] = None


class DisassociateTrafficDistributionGroupUserRequest(BaseValidatorModel):
    TrafficDistributionGroupId: str
    UserId: str
    InstanceId: str


class UserProficiencyDisassociate(BaseValidatorModel):
    AttributeName: str
    AttributeValue: str


class DisconnectReason(BaseValidatorModel):
    Code: Optional[str] = None


class DismissUserContactRequest(BaseValidatorModel):
    UserId: str
    InstanceId: str
    ContactId: str


class DownloadUrlMetadata(BaseValidatorModel):
    Url: Optional[str] = None
    UrlExpiry: Optional[str] = None


class EmailAddressInfo(BaseValidatorModel):
    EmailAddress: str
    DisplayName: Optional[str] = None


class EmailAddressMetadata(BaseValidatorModel):
    EmailAddressId: Optional[str] = None
    EmailAddressArn: Optional[str] = None
    EmailAddress: Optional[str] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None


class EmailAttachment(BaseValidatorModel):
    FileName: str
    S3Url: str


class EmailMessageReference(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None


class EmailReference(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class EncryptionConfig(BaseValidatorModel):
    EncryptionType: Literal["KMS"]
    KeyId: str


class EvaluationAnswerData(BaseValidatorModel):
    StringValue: Optional[str] = None
    NumericValue: Optional[float] = None
    NotApplicable: Optional[bool] = None


class EvaluationFormSectionOutput(BaseValidatorModel):
    Title: str
    RefId: str
    Items: List[Dict[str, Any]]
    Instructions: Optional[str] = None
    Weight: Optional[float] = None


class NumericQuestionPropertyValueAutomation(BaseValidatorModel):
    Label: NumericQuestionPropertyAutomationLabelType


class EvaluationFormNumericQuestionOption(BaseValidatorModel):
    MinValue: int
    MaxValue: int
    Score: Optional[int] = None
    AutomaticFail: Optional[bool] = None


class EvaluationFormSection(BaseValidatorModel):
    Title: str
    RefId: str
    Items: Sequence[Mapping[str, Any]]
    Instructions: Optional[str] = None
    Weight: Optional[float] = None


class SingleSelectQuestionRuleCategoryAutomation(BaseValidatorModel):
    Category: str
    Condition: SingleSelectQuestionRuleCategoryAutomationConditionType
    OptionRefId: str


class EvaluationFormSummary(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    Title: str
    CreatedTime: datetime
    CreatedBy: str
    LastModifiedTime: datetime
    LastModifiedBy: str
    LatestVersion: int
    LastActivatedTime: Optional[datetime] = None
    LastActivatedBy: Optional[str] = None
    ActiveVersion: Optional[int] = None


class EvaluationFormVersionSummary(BaseValidatorModel):
    EvaluationFormArn: str
    EvaluationFormId: str
    EvaluationFormVersion: int
    Locked: bool
    Status: EvaluationFormVersionStatusType
    CreatedTime: datetime
    CreatedBy: str
    LastModifiedTime: datetime
    LastModifiedBy: str


class EvaluationScore(BaseValidatorModel):
    Percentage: Optional[float] = None
    NotApplicable: Optional[bool] = None
    AutomaticFail: Optional[bool] = None


class EvaluationNote(BaseValidatorModel):
    Value: Optional[str] = None


class EventBridgeActionDefinition(BaseValidatorModel):
    Name: str


class Expiry(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None
    ExpiryTimestamp: Optional[datetime] = None


class FieldValueUnionOutput(BaseValidatorModel):
    BooleanValue: Optional[bool] = None
    DoubleValue: Optional[float] = None
    EmptyValue: Optional[Dict[str, Any]] = None
    StringValue: Optional[str] = None


class FieldValueUnion(BaseValidatorModel):
    BooleanValue: Optional[bool] = None
    DoubleValue: Optional[float] = None
    EmptyValue: Optional[Mapping[str, Any]] = None
    StringValue: Optional[str] = None


class FilterV2(BaseValidatorModel):
    FilterKey: Optional[str] = None
    FilterValues: Optional[Sequence[str]] = None


class Filters(BaseValidatorModel):
    Queues: Optional[Sequence[str]] = None
    Channels: Optional[Sequence[ChannelType]] = None
    RoutingProfiles: Optional[Sequence[str]] = None
    RoutingStepExpressions: Optional[Sequence[str]] = None


class GetAttachedFileRequest(BaseValidatorModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str
    UrlExpiryInSeconds: Optional[int] = None


class GetContactAttributesRequest(BaseValidatorModel):
    InstanceId: str
    InitialContactId: str


class GetEffectiveHoursOfOperationsRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    FromDate: str
    ToDate: str


class GetFederationTokenRequest(BaseValidatorModel):
    InstanceId: str


class GetFlowAssociationRequest(BaseValidatorModel):
    InstanceId: str
    ResourceId: str
    ResourceType: FlowAssociationResourceTypeType


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class IntervalDetails(BaseValidatorModel):
    TimeZone: Optional[str] = None
    IntervalPeriod: Optional[IntervalPeriodType] = None


class GetPromptFileRequest(BaseValidatorModel):
    InstanceId: str
    PromptId: str


class GetTaskTemplateRequest(BaseValidatorModel):
    InstanceId: str
    TaskTemplateId: str
    SnapshotVersion: Optional[str] = None


class GetTrafficDistributionRequest(BaseValidatorModel):
    Id: str


class HierarchyGroupSummaryReference(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None


class HierarchyGroupSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class HierarchyLevel(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class HierarchyLevelUpdate(BaseValidatorModel):
    Name: str


class Threshold(BaseValidatorModel):
    Comparison: Optional[Literal["LT"]] = None
    ThresholdValue: Optional[float] = None


class HoursOfOperationTimeSlice(BaseValidatorModel):
    Hours: int
    Minutes: int


class OverrideTimeSlice(BaseValidatorModel):
    Hours: int
    Minutes: int


class HoursOfOperationSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ImportPhoneNumberRequest(BaseValidatorModel):
    InstanceId: str
    SourcePhoneNumberArn: str
    PhoneNumberDescription: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None


class InboundRawMessage(BaseValidatorModel):
    Subject: str
    Body: str
    ContentType: str
    Headers: Optional[Mapping[EmailHeaderTypeType, str]] = None


class InstanceStatusReason(BaseValidatorModel):
    Message: Optional[str] = None


class KinesisFirehoseConfig(BaseValidatorModel):
    FirehoseArn: str


class KinesisStreamConfig(BaseValidatorModel):
    StreamArn: str


class InstanceSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    IdentityManagementType: Optional[DirectoryTypeType] = None
    InstanceAlias: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    ServiceRole: Optional[str] = None
    InstanceStatus: Optional[InstanceStatusType] = None
    InboundCallsEnabled: Optional[bool] = None
    OutboundCallsEnabled: Optional[bool] = None
    InstanceAccessUrl: Optional[str] = None


class IntegrationAssociationSummary(BaseValidatorModel):
    IntegrationAssociationId: Optional[str] = None
    IntegrationAssociationArn: Optional[str] = None
    InstanceId: Optional[str] = None
    IntegrationType: Optional[IntegrationTypeType] = None
    IntegrationArn: Optional[str] = None
    SourceApplicationUrl: Optional[str] = None
    SourceApplicationName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None


class TaskTemplateFieldIdentifier(BaseValidatorModel):
    Name: Optional[str] = None


class ListAgentStatusRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AgentStatusTypes: Optional[Sequence[AgentStatusTypeType]] = None


class ListAnalyticsDataAssociationsRequest(BaseValidatorModel):
    InstanceId: str
    DataSetId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAnalyticsDataLakeDataSetsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListApprovedOriginsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAssociatedContactsRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAuthenticationProfilesRequest(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListBotsRequest(BaseValidatorModel):
    InstanceId: str
    LexVersion: LexVersionType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListContactEvaluationsRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    NextToken: Optional[str] = None


class ListContactFlowModulesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ContactFlowModuleState: Optional[ContactFlowModuleStateType] = None


class ListContactFlowVersionsRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListContactFlowsRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowTypes: Optional[Sequence[ContactFlowTypeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListContactReferencesRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ReferenceTypes: Sequence[ReferenceTypeType]
    NextToken: Optional[str] = None


class ListDefaultVocabulariesRequest(BaseValidatorModel):
    InstanceId: str
    LanguageCode: Optional[VocabularyLanguageCodeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEvaluationFormVersionsRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEvaluationFormsRequest(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFlowAssociationsRequest(BaseValidatorModel):
    InstanceId: str
    ResourceType: Optional[ListFlowAssociationResourceTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListHoursOfOperationOverridesRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListHoursOfOperationsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListInstanceAttributesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListInstanceStorageConfigsRequest(BaseValidatorModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListInstancesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIntegrationAssociationsRequest(BaseValidatorModel):
    InstanceId: str
    IntegrationType: Optional[IntegrationTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IntegrationArn: Optional[str] = None


class ListLambdaFunctionsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListLexBotsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPhoneNumbersRequest(BaseValidatorModel):
    InstanceId: str
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PhoneNumberSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    PhoneNumberCountryCode: Optional[PhoneNumberCountryCodeType] = None


class ListPhoneNumbersSummary(BaseValidatorModel):
    PhoneNumberId: Optional[str] = None
    PhoneNumberArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    PhoneNumberCountryCode: Optional[PhoneNumberCountryCodeType] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberDescription: Optional[str] = None
    SourcePhoneNumberArn: Optional[str] = None


class ListPhoneNumbersV2Request(BaseValidatorModel):
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberPrefix: Optional[str] = None


class ListPredefinedAttributesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PredefinedAttributeSummary(BaseValidatorModel):
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ListPromptsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PromptSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ListQueueQuickConnectsRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class QuickConnectSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    QuickConnectType: Optional[QuickConnectTypeType] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ListQueuesRequest(BaseValidatorModel):
    InstanceId: str
    QueueTypes: Optional[Sequence[QueueTypeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class QueueSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    QueueType: Optional[QueueTypeType] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ListQuickConnectsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuickConnectTypes: Optional[Sequence[QuickConnectTypeType]] = None


class ListRealtimeContactAnalysisSegmentsV2Request(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    OutputType: RealTimeContactAnalysisOutputTypeType
    SegmentTypes: Sequence[RealTimeContactAnalysisSegmentTypeType]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRoutingProfileQueuesRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RoutingProfileQueueConfigSummary(BaseValidatorModel):
    QueueId: str
    QueueArn: str
    QueueName: str
    Priority: int
    Delay: int
    Channel: ChannelType


class ListRoutingProfilesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RoutingProfileSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ListRulesRequest(BaseValidatorModel):
    InstanceId: str
    PublishStatus: Optional[RulePublishStatusType] = None
    EventSourceName: Optional[EventSourceNameType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSecurityKeysRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SecurityKey(BaseValidatorModel):
    AssociationId: Optional[str] = None
    Key: Optional[str] = None
    CreationTime: Optional[datetime] = None


class ListSecurityProfileApplicationsRequest(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSecurityProfilePermissionsRequest(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSecurityProfilesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SecurityProfileSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class ListTaskTemplatesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[TaskTemplateStatusType] = None
    Name: Optional[str] = None


class TaskTemplateMetadata(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[TaskTemplateStatusType] = None
    LastModifiedTime: Optional[datetime] = None
    CreatedTime: Optional[datetime] = None


class ListTrafficDistributionGroupUsersRequest(BaseValidatorModel):
    TrafficDistributionGroupId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TrafficDistributionGroupUserSummary(BaseValidatorModel):
    UserId: Optional[str] = None


class ListTrafficDistributionGroupsRequest(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    InstanceId: Optional[str] = None


class TrafficDistributionGroupSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    InstanceArn: Optional[str] = None
    Status: Optional[TrafficDistributionGroupStatusType] = None
    IsDefault: Optional[bool] = None


class ListUseCasesRequest(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class UseCase(BaseValidatorModel):
    UseCaseId: Optional[str] = None
    UseCaseArn: Optional[str] = None
    UseCaseType: Optional[UseCaseTypeType] = None


class ListUserHierarchyGroupsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListUserProficienciesRequest(BaseValidatorModel):
    InstanceId: str
    UserId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListUsersRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class UserSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Username: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ListViewVersionsRequest(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MediaPlacement(BaseValidatorModel):
    AudioHostUrl: Optional[str] = None
    AudioFallbackUrl: Optional[str] = None
    SignalingUrl: Optional[str] = None
    TurnControlUrl: Optional[str] = None
    EventIngestionUrl: Optional[str] = None


class MetricFilterV2Output(BaseValidatorModel):
    MetricFilterKey: Optional[str] = None
    MetricFilterValues: Optional[List[str]] = None
    Negate: Optional[bool] = None


class MetricFilterV2(BaseValidatorModel):
    MetricFilterKey: Optional[str] = None
    MetricFilterValues: Optional[Sequence[str]] = None
    Negate: Optional[bool] = None


class MetricInterval(BaseValidatorModel):
    Interval: Optional[IntervalPeriodType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class ThresholdV2(BaseValidatorModel):
    Comparison: Optional[str] = None
    ThresholdValue: Optional[float] = None


class MonitorContactRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    UserId: str
    AllowedMonitorCapabilities: Optional[Sequence[MonitorCapabilityType]] = None
    ClientToken: Optional[str] = None


class ParticipantDetails(BaseValidatorModel):
    DisplayName: str


class NotificationRecipientTypeOutput(BaseValidatorModel):
    UserTags: Optional[Dict[str, str]] = None
    UserIds: Optional[List[str]] = None


class NotificationRecipientType(BaseValidatorModel):
    UserTags: Optional[Mapping[str, str]] = None
    UserIds: Optional[Sequence[str]] = None


class NumberReference(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class OutboundRawMessage(BaseValidatorModel):
    Subject: str
    Body: str
    ContentType: str


class ParticipantTimerValue(BaseValidatorModel):
    ParticipantTimerAction: Optional[Literal["Unset"]] = None
    ParticipantTimerDurationInMinutes: Optional[int] = None


class PauseContactRequest(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    ContactFlowId: Optional[str] = None


class PersistentChat(BaseValidatorModel):
    RehydrationType: Optional[RehydrationTypeType] = None
    SourceContactId: Optional[str] = None


class PhoneNumberQuickConnectConfig(BaseValidatorModel):
    PhoneNumber: str


class PredefinedAttributeValuesOutput(BaseValidatorModel):
    StringList: Optional[List[str]] = None


class PredefinedAttributeValues(BaseValidatorModel):
    StringList: Optional[Sequence[str]] = None


class PutUserStatusRequest(BaseValidatorModel):
    UserId: str
    InstanceId: str
    AgentStatusId: str


class QueueInfoInput(BaseValidatorModel):
    Id: Optional[str] = None


class QueueQuickConnectConfig(BaseValidatorModel):
    QueueId: str
    ContactFlowId: str


class UserQuickConnectConfig(BaseValidatorModel):
    UserId: str
    ContactFlowId: str


class RealTimeContactAnalysisAttachment(BaseValidatorModel):
    AttachmentName: str
    AttachmentId: str
    ContentType: Optional[str] = None
    Status: Optional[ArtifactStatusType] = None


class RealTimeContactAnalysisCharacterInterval(BaseValidatorModel):
    BeginOffsetChar: int
    EndOffsetChar: int


class RealTimeContactAnalysisTimeData(BaseValidatorModel):
    AbsoluteTime: Optional[datetime] = None


class RealTimeContactAnalysisSegmentPostContactSummary(BaseValidatorModel):
    Status: RealTimeContactAnalysisPostContactSummaryStatusType
    Content: Optional[str] = None
    FailureCode: Optional[RealTimeContactAnalysisPostContactSummaryFailureCodeType] = None


class StringReference(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class UrlReference(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class ReleasePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str
    ClientToken: Optional[str] = None


class ReplicateInstanceRequest(BaseValidatorModel):
    InstanceId: str
    ReplicaRegion: str
    ReplicaAlias: str
    ClientToken: Optional[str] = None


class ReplicationStatusSummary(BaseValidatorModel):
    Region: Optional[str] = None
    ReplicationStatus: Optional[InstanceReplicationStatusType] = None
    ReplicationStatusReason: Optional[str] = None


class TagSearchCondition(BaseValidatorModel):
    tagKey: Optional[str] = None
    tagValue: Optional[str] = None
    tagKeyComparisonType: Optional[StringComparisonTypeType] = None
    tagValueComparisonType: Optional[StringComparisonTypeType] = None


class ResumeContactRecordingRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    ContactRecordingType: Optional[ContactRecordingTypeType] = None


class ResumeContactRequest(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    ContactFlowId: Optional[str] = None


class RoutingCriteriaInputStepExpiry(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None


class SubmitAutoEvaluationActionDefinition(BaseValidatorModel):
    EvaluationFormId: str


class SearchAvailablePhoneNumbersRequest(BaseValidatorModel):
    PhoneNumberCountryCode: PhoneNumberCountryCodeType
    PhoneNumberType: PhoneNumberTypeType
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberPrefix: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class Sort(BaseValidatorModel):
    FieldName: SortableFieldNameType
    Order: SortOrderType


class TagSet(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None


class SecurityProfileSearchSummary(BaseValidatorModel):
    Id: Optional[str] = None
    OrganizationResourceId: Optional[str] = None
    Arn: Optional[str] = None
    SecurityProfileName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class SearchVocabulariesRequest(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    State: Optional[VocabularyStateType] = None
    NameStartsWith: Optional[str] = None
    LanguageCode: Optional[VocabularyLanguageCodeType] = None


class VocabularySummary(BaseValidatorModel):
    Name: str
    Id: str
    Arn: str
    LanguageCode: VocabularyLanguageCodeType
    State: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: Optional[str] = None


class SearchableContactAttributesCriteria(BaseValidatorModel):
    Key: str
    Values: Sequence[str]


class SearchableSegmentAttributesCriteria(BaseValidatorModel):
    Key: str
    Values: Sequence[str]


class SegmentAttributeValue(BaseValidatorModel):
    ValueString: Optional[str] = None
    ValueMap: Optional[Mapping[str, Mapping[str, Any]]] = None
    ValueInteger: Optional[int] = None


class SourceCampaign(BaseValidatorModel):
    CampaignId: Optional[str] = None
    OutboundRequestId: Optional[str] = None


class SignInDistribution(BaseValidatorModel):
    Region: str
    Enabled: bool


class UploadUrlMetadata(BaseValidatorModel):
    Url: Optional[str] = None
    UrlExpiry: Optional[str] = None
    HeadersToInclude: Optional[Dict[str, str]] = None


class StartContactEvaluationRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    EvaluationFormId: str
    ClientToken: Optional[str] = None


class VoiceRecordingConfiguration(BaseValidatorModel):
    VoiceRecordingTrack: Optional[VoiceRecordingTrackType] = None
    IvrRecordingTrack: Optional[Literal["ALL"]] = None


class StartScreenSharingRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ClientToken: Optional[str] = None


class StopContactRecordingRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    ContactRecordingType: Optional[ContactRecordingTypeType] = None


class StopContactStreamingRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    StreamingId: str


class SuspendContactRecordingRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    ContactRecordingType: Optional[ContactRecordingTypeType] = None


class TagContactRequest(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    Tags: Mapping[str, str]


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TemplateAttributes(BaseValidatorModel):
    CustomAttributes: Optional[Mapping[str, str]] = None
    CustomerProfileAttributes: Optional[str] = None


class TranscriptCriteria(BaseValidatorModel):
    ParticipantRole: ParticipantRoleType
    SearchText: Sequence[str]
    MatchType: SearchContactsMatchTypeType


class TransferContactRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ContactFlowId: str
    QueueId: Optional[str] = None
    UserId: Optional[str] = None
    ClientToken: Optional[str] = None


class UntagContactRequest(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    TagKeys: Sequence[str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAgentStatusRequest(BaseValidatorModel):
    InstanceId: str
    AgentStatusId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[AgentStatusStateType] = None
    DisplayOrder: Optional[int] = None
    ResetOrderNumber: Optional[bool] = None


class UpdateAuthenticationProfileRequest(BaseValidatorModel):
    AuthenticationProfileId: str
    InstanceId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    AllowedIps: Optional[Sequence[str]] = None
    BlockedIps: Optional[Sequence[str]] = None
    PeriodicSessionDuration: Optional[int] = None


class UpdateContactAttributesRequest(BaseValidatorModel):
    InitialContactId: str
    InstanceId: str
    Attributes: Mapping[str, str]


class UpdateContactFlowContentRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    Content: str


class UpdateContactFlowMetadataRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ContactFlowState: Optional[ContactFlowStateType] = None


class UpdateContactFlowModuleContentRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleId: str
    Content: str


class UpdateContactFlowModuleMetadataRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[ContactFlowModuleStateType] = None


class UpdateContactFlowNameRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateEmailAddressMetadataRequest(BaseValidatorModel):
    InstanceId: str
    EmailAddressId: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    ClientToken: Optional[str] = None


class UpdateInstanceAttributeRequest(BaseValidatorModel):
    InstanceId: str
    AttributeType: InstanceAttributeTypeType
    Value: str
    ClientToken: Optional[str] = None


class UpdateParticipantAuthenticationRequest(BaseValidatorModel):
    State: str
    InstanceId: str
    Code: Optional[str] = None
    Error: Optional[str] = None
    ErrorDescription: Optional[str] = None


class UpdatePhoneNumberMetadataRequest(BaseValidatorModel):
    PhoneNumberId: str
    PhoneNumberDescription: Optional[str] = None
    ClientToken: Optional[str] = None


class UpdatePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    ClientToken: Optional[str] = None


class UpdatePromptRequest(BaseValidatorModel):
    InstanceId: str
    PromptId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    S3Uri: Optional[str] = None


class UpdateQueueHoursOfOperationRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    HoursOfOperationId: str


class UpdateQueueMaxContactsRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    MaxContacts: Optional[int] = None


class UpdateQueueNameRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateQueueStatusRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    Status: QueueStatusType


class UpdateQuickConnectNameRequest(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateRoutingProfileAgentAvailabilityTimerRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    AgentAvailabilityTimer: AgentAvailabilityTimerType


class UpdateRoutingProfileDefaultOutboundQueueRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    DefaultOutboundQueueId: str


class UpdateRoutingProfileNameRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateUserHierarchyGroupNameRequest(BaseValidatorModel):
    Name: str
    HierarchyGroupId: str
    InstanceId: str


class UpdateUserHierarchyRequest(BaseValidatorModel):
    UserId: str
    InstanceId: str
    HierarchyGroupId: Optional[str] = None


class UpdateUserRoutingProfileRequest(BaseValidatorModel):
    RoutingProfileId: str
    UserId: str
    InstanceId: str


class UpdateUserSecurityProfilesRequest(BaseValidatorModel):
    SecurityProfileIds: Sequence[str]
    UserId: str
    InstanceId: str


class UpdateViewMetadataRequest(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UserReference(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None


class UserIdentityInfoLite(BaseValidatorModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None


class ViewContent(BaseValidatorModel):
    InputSchema: Optional[str] = None
    Template: Optional[str] = None
    Actions: Optional[List[str]] = None


class RuleSummary(BaseValidatorModel):
    Name: str
    RuleId: str
    RuleArn: str
    EventSourceName: EventSourceNameType
    PublishStatus: RulePublishStatusType
    ActionSummaries: List[ActionSummary]
    CreatedTime: datetime
    LastUpdatedTime: datetime


class ActivateEvaluationFormResponse(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadata


class AssociateAnalyticsDataSetResponse(BaseValidatorModel):
    DataSetId: str
    TargetAccountId: str
    ResourceShareId: str
    ResourceShareArn: str
    ResponseMetadata: ResponseMetadata


class AssociateInstanceStorageConfigResponse(BaseValidatorModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadata


class AssociateSecurityKeyResponse(BaseValidatorModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadata


class ClaimPhoneNumberResponse(BaseValidatorModel):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadata


class CreateAgentStatusResponse(BaseValidatorModel):
    AgentStatusARN: str
    AgentStatusId: str
    ResponseMetadata: ResponseMetadata


class CreateContactFlowModuleResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


class CreateContactFlowResponse(BaseValidatorModel):
    ContactFlowId: str
    ContactFlowArn: str
    FlowContentSha256: str
    ResponseMetadata: ResponseMetadata


class CreateContactFlowVersionResponse(BaseValidatorModel):
    ContactFlowArn: str
    Version: int
    ResponseMetadata: ResponseMetadata


class CreateContactResponse(BaseValidatorModel):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadata


class CreateEmailAddressResponse(BaseValidatorModel):
    EmailAddressId: str
    EmailAddressArn: str
    ResponseMetadata: ResponseMetadata


class CreateEvaluationFormResponse(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    ResponseMetadata: ResponseMetadata


class CreateHoursOfOperationOverrideResponse(BaseValidatorModel):
    HoursOfOperationOverrideId: str
    ResponseMetadata: ResponseMetadata


class CreateHoursOfOperationResponse(BaseValidatorModel):
    HoursOfOperationId: str
    HoursOfOperationArn: str
    ResponseMetadata: ResponseMetadata


class CreateInstanceResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


class CreateIntegrationAssociationResponse(BaseValidatorModel):
    IntegrationAssociationId: str
    IntegrationAssociationArn: str
    ResponseMetadata: ResponseMetadata


class CreatePersistentContactAssociationResponse(BaseValidatorModel):
    ContinuedFromContactId: str
    ResponseMetadata: ResponseMetadata


class CreatePromptResponse(BaseValidatorModel):
    PromptARN: str
    PromptId: str
    ResponseMetadata: ResponseMetadata


class CreatePushNotificationRegistrationResponse(BaseValidatorModel):
    RegistrationId: str
    ResponseMetadata: ResponseMetadata


class CreateQueueResponse(BaseValidatorModel):
    QueueArn: str
    QueueId: str
    ResponseMetadata: ResponseMetadata


class CreateQuickConnectResponse(BaseValidatorModel):
    QuickConnectARN: str
    QuickConnectId: str
    ResponseMetadata: ResponseMetadata


class CreateRoutingProfileResponse(BaseValidatorModel):
    RoutingProfileArn: str
    RoutingProfileId: str
    ResponseMetadata: ResponseMetadata


class CreateRuleResponse(BaseValidatorModel):
    RuleArn: str
    RuleId: str
    ResponseMetadata: ResponseMetadata


class CreateSecurityProfileResponse(BaseValidatorModel):
    SecurityProfileId: str
    SecurityProfileArn: str
    ResponseMetadata: ResponseMetadata


class CreateTaskTemplateResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


class CreateTrafficDistributionGroupResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


class CreateUseCaseResponse(BaseValidatorModel):
    UseCaseId: str
    UseCaseArn: str
    ResponseMetadata: ResponseMetadata


class CreateUserHierarchyGroupResponse(BaseValidatorModel):
    HierarchyGroupId: str
    HierarchyGroupArn: str
    ResponseMetadata: ResponseMetadata


class CreateUserResponse(BaseValidatorModel):
    UserId: str
    UserArn: str
    ResponseMetadata: ResponseMetadata


class CreateVocabularyResponse(BaseValidatorModel):
    VocabularyArn: str
    VocabularyId: str
    State: VocabularyStateType
    ResponseMetadata: ResponseMetadata


class DeactivateEvaluationFormResponse(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadata


class DeleteVocabularyResponse(BaseValidatorModel):
    VocabularyArn: str
    VocabularyId: str
    State: VocabularyStateType
    ResponseMetadata: ResponseMetadata


class DescribeEmailAddressResponse(BaseValidatorModel):
    EmailAddressId: str
    EmailAddressArn: str
    EmailAddress: str
    DisplayName: str
    Description: str
    CreateTimestamp: str
    ModifiedTimestamp: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetContactAttributesResponse(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class GetFlowAssociationResponse(BaseValidatorModel):
    ResourceId: str
    FlowId: str
    ResourceType: FlowAssociationResourceTypeType
    ResponseMetadata: ResponseMetadata


class GetPromptFileResponse(BaseValidatorModel):
    PromptPresignedUrl: str
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadata


class ImportPhoneNumberResponse(BaseValidatorModel):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadata


class ListApprovedOriginsResponse(BaseValidatorModel):
    Origins: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListLambdaFunctionsResponse(BaseValidatorModel):
    LambdaFunctions: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSecurityProfilePermissionsResponse(BaseValidatorModel):
    Permissions: List[str]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class MonitorContactResponse(BaseValidatorModel):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadata


class ReplicateInstanceResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


class SendChatIntegrationEventResponse(BaseValidatorModel):
    InitialContactId: str
    NewChatCreated: bool
    ResponseMetadata: ResponseMetadata


class StartChatContactResponse(BaseValidatorModel):
    ContactId: str
    ParticipantId: str
    ParticipantToken: str
    ContinuedFromContactId: str
    ResponseMetadata: ResponseMetadata


class StartContactEvaluationResponse(BaseValidatorModel):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadata


class StartContactStreamingResponse(BaseValidatorModel):
    StreamingId: str
    ResponseMetadata: ResponseMetadata


class StartEmailContactResponse(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadata


class StartOutboundChatContactResponse(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadata


class StartOutboundEmailContactResponse(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadata


class StartOutboundVoiceContactResponse(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadata


class StartTaskContactResponse(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadata


class SubmitContactEvaluationResponse(BaseValidatorModel):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadata


class TransferContactResponse(BaseValidatorModel):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadata


class UpdateContactEvaluationResponse(BaseValidatorModel):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadata


class UpdateEmailAddressMetadataResponse(BaseValidatorModel):
    EmailAddressId: str
    EmailAddressArn: str
    ResponseMetadata: ResponseMetadata


class UpdateEvaluationFormResponse(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadata


class UpdatePhoneNumberResponse(BaseValidatorModel):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadata


class UpdatePromptResponse(BaseValidatorModel):
    PromptARN: str
    PromptId: str
    ResponseMetadata: ResponseMetadata


class AdditionalEmailRecipients(BaseValidatorModel):
    ToList: Optional[List[EmailRecipient]] = None
    CcList: Optional[List[EmailRecipient]] = None


class AgentConfigOutput(BaseValidatorModel):
    Distributions: List[Distribution]


class AgentConfig(BaseValidatorModel):
    Distributions: Sequence[Distribution]


class TelephonyConfigOutput(BaseValidatorModel):
    Distributions: List[Distribution]


class TelephonyConfig(BaseValidatorModel):
    Distributions: Sequence[Distribution]


class AgentContactReference(BaseValidatorModel):
    ContactId: Optional[str] = None
    Channel: Optional[ChannelType] = None
    InitiationMethod: Optional[ContactInitiationMethodType] = None
    AgentContactState: Optional[ContactStateType] = None
    StateStartTimestamp: Optional[datetime] = None
    ConnectedToAgentTimestamp: Optional[datetime] = None
    Queue: Optional[QueueReference] = None


class HierarchyGroups(BaseValidatorModel):
    Level1: Optional[AgentHierarchyGroup] = None
    Level2: Optional[AgentHierarchyGroup] = None
    Level3: Optional[AgentHierarchyGroup] = None
    Level4: Optional[AgentHierarchyGroup] = None
    Level5: Optional[AgentHierarchyGroup] = None


class AllowedCapabilities(BaseValidatorModel):
    Customer: Optional[ParticipantCapabilities] = None
    Agent: Optional[ParticipantCapabilities] = None


class Customer(BaseValidatorModel):
    DeviceInfo: Optional[DeviceInfo] = None
    Capabilities: Optional[ParticipantCapabilities] = None


class AgentQualityMetrics(BaseValidatorModel):
    Audio: Optional[AudioQualityMetricsInfo] = None


class CustomerQualityMetrics(BaseValidatorModel):
    Audio: Optional[AudioQualityMetricsInfo] = None


class StringCondition(BaseValidatorModel):
    pass


class AgentStatusSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class AgentStatusSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class ContactFlowModuleSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    StateCondition: Optional[ContactFlowModuleStateType] = None
    StatusCondition: Optional[ContactFlowModuleStatusType] = None


class ContactFlowModuleSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    StateCondition: Optional[ContactFlowModuleStateType] = None
    StatusCondition: Optional[ContactFlowModuleStatusType] = None


class ContactFlowSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    TypeCondition: Optional[ContactFlowTypeType] = None
    StateCondition: Optional[ContactFlowStateType] = None
    StatusCondition: Optional[ContactFlowStatusType] = None


class ContactFlowSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    TypeCondition: Optional[ContactFlowTypeType] = None
    StateCondition: Optional[ContactFlowStateType] = None
    StatusCondition: Optional[ContactFlowStatusType] = None


class EmailAddressSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class HoursOfOperationSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class HoursOfOperationSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class PredefinedAttributeSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class PredefinedAttributeSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class PromptSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class PromptSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class QueueSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    QueueTypeCondition: Optional[Literal["STANDARD"]] = None


class QueueSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    QueueTypeCondition: Optional[Literal["STANDARD"]] = None


class QuickConnectSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class QuickConnectSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class RoutingProfileSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class RoutingProfileSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class SecurityProfileSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class SecurityProfileSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class UserHierarchyGroupSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class UserHierarchyGroupSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class AgentStatusSummary(BaseValidatorModel):
    pass


class ListAgentStatusResponse(BaseValidatorModel):
    AgentStatusSummaryList: List[AgentStatusSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AgentStatus(BaseValidatorModel):
    pass


class DescribeAgentStatusResponse(BaseValidatorModel):
    AgentStatus: AgentStatus
    ResponseMetadata: ResponseMetadata


class SearchAgentStatusesResponse(BaseValidatorModel):
    AgentStatuses: List[AgentStatus]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MatchCriteriaOutput(BaseValidatorModel):
    AgentsCriteria: Optional[AgentsCriteriaOutput] = None


class ListAnalyticsDataAssociationsResponse(BaseValidatorModel):
    Results: List[AnalyticsDataAssociationResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListAnalyticsDataLakeDataSetsResponse(BaseValidatorModel):
    Results: List[AnalyticsDataSetsResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSecurityProfileApplicationsResponse(BaseValidatorModel):
    Applications: List[ApplicationOutput]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AssociateLexBotRequest(BaseValidatorModel):
    InstanceId: str
    LexBot: LexBot
    ClientToken: Optional[str] = None


class ListLexBotsResponse(BaseValidatorModel):
    LexBots: List[LexBot]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AssociateBotRequest(BaseValidatorModel):
    InstanceId: str
    LexBot: Optional[LexBot] = None
    LexV2Bot: Optional[LexV2Bot] = None
    ClientToken: Optional[str] = None


class DisassociateBotRequest(BaseValidatorModel):
    InstanceId: str
    LexBot: Optional[LexBot] = None
    LexV2Bot: Optional[LexV2Bot] = None
    ClientToken: Optional[str] = None


class LexBotConfig(BaseValidatorModel):
    LexBot: Optional[LexBot] = None
    LexV2Bot: Optional[LexV2Bot] = None


class AssociateUserProficienciesRequest(BaseValidatorModel):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiency]


class ListUserProficienciesResponse(BaseValidatorModel):
    UserProficiencyList: List[UserProficiency]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateUserProficienciesRequest(BaseValidatorModel):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiency]


class ListAssociatedContactsResponse(BaseValidatorModel):
    ContactSummaryList: List[AssociatedContactSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AttachedFile(BaseValidatorModel):
    CreationTime: str
    FileArn: str
    FileId: str
    FileName: str
    FileSizeInBytes: int
    FileStatus: FileStatusTypeType
    CreatedBy: Optional[CreatedByInfo] = None
    FileUseCaseType: Optional[FileUseCaseTypeType] = None
    AssociatedResourceArn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class StartAttachedFileUploadRequest(BaseValidatorModel):
    InstanceId: str
    FileName: str
    FileSizeInBytes: int
    FileUseCaseType: FileUseCaseTypeType
    AssociatedResourceArn: str
    ClientToken: Optional[str] = None
    UrlExpiryInSeconds: Optional[int] = None
    CreatedBy: Optional[CreatedByInfo] = None
    Tags: Optional[Mapping[str, str]] = None


class AttributeAndCondition(BaseValidatorModel):
    TagConditions: Optional[Sequence[TagCondition]] = None
    HierarchyGroupCondition: Optional[HierarchyGroupCondition] = None


class CommonAttributeAndCondition(BaseValidatorModel):
    TagConditions: Optional[Sequence[TagCondition]] = None


class ControlPlaneTagFilter(BaseValidatorModel):
    OrConditions: Optional[Sequence[Sequence[TagCondition]]] = None
    AndConditions: Optional[Sequence[TagCondition]] = None
    TagCondition: Optional[TagCondition] = None


class DescribeInstanceAttributeResponse(BaseValidatorModel):
    Attribute: Attribute
    ResponseMetadata: ResponseMetadata


class ListInstanceAttributesResponse(BaseValidatorModel):
    Attributes: List[Attribute]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MeetingFeaturesConfiguration(BaseValidatorModel):
    Audio: Optional[AudioFeatures] = None


class ListAuthenticationProfilesResponse(BaseValidatorModel):
    AuthenticationProfileSummaryList: List[AuthenticationProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeAuthenticationProfileResponse(BaseValidatorModel):
    AuthenticationProfile: AuthenticationProfile
    ResponseMetadata: ResponseMetadata


class SearchAvailablePhoneNumbersResponse(BaseValidatorModel):
    AvailableNumbersList: List[AvailableNumberSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchAssociateAnalyticsDataSetResponse(BaseValidatorModel):
    Created: List[AnalyticsDataAssociationResult]
    Errors: List[ErrorResult]
    ResponseMetadata: ResponseMetadata


class BatchDisassociateAnalyticsDataSetResponse(BaseValidatorModel):
    Deleted: List[str]
    Errors: List[ErrorResult]
    ResponseMetadata: ResponseMetadata


class BatchGetFlowAssociationResponse(BaseValidatorModel):
    FlowAssociationSummaryList: List[FlowAssociationSummary]
    ResponseMetadata: ResponseMetadata


class ListFlowAssociationsResponse(BaseValidatorModel):
    FlowAssociationSummaryList: List[FlowAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchPutContactResponse(BaseValidatorModel):
    SuccessfulRequestList: List[SuccessfulRequest]
    FailedRequestList: List[FailedRequest]
    ResponseMetadata: ResponseMetadata


class StartContactStreamingRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ChatStreamingConfiguration: ChatStreamingConfiguration
    ClientToken: str


class ClaimedPhoneNumberSummary(BaseValidatorModel):
    PhoneNumberId: Optional[str] = None
    PhoneNumberArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    PhoneNumberCountryCode: Optional[PhoneNumberCountryCodeType] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    PhoneNumberDescription: Optional[str] = None
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    PhoneNumberStatus: Optional[PhoneNumberStatus] = None
    SourcePhoneNumberArn: Optional[str] = None


class NumberCondition(BaseValidatorModel):
    pass


class Condition(BaseValidatorModel):
    StringCondition: Optional[StringCondition] = None
    NumberCondition: Optional[NumberCondition] = None


class CreatePushNotificationRegistrationRequest(BaseValidatorModel):
    InstanceId: str
    PinpointAppArn: str
    DeviceToken: str
    DeviceType: DeviceTypeType
    ContactConfiguration: ContactConfiguration
    ClientToken: Optional[str] = None


class Endpoint(BaseValidatorModel):
    pass


class ContactDataRequest(BaseValidatorModel):
    SystemEndpoint: Optional[Endpoint] = None
    CustomerEndpoint: Optional[Endpoint] = None
    RequestIdentifier: Optional[str] = None
    QueueId: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    Campaign: Optional[Campaign] = None


class UserDataFilters(BaseValidatorModel):
    Queues: Optional[Sequence[str]] = None
    ContactFilter: Optional[ContactFilter] = None
    RoutingProfiles: Optional[Sequence[str]] = None
    Agents: Optional[Sequence[str]] = None
    UserHierarchyGroups: Optional[Sequence[str]] = None


class ListContactFlowModulesResponse(BaseValidatorModel):
    ContactFlowModulesSummaryList: List[ContactFlowModuleSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeContactFlowModuleResponse(BaseValidatorModel):
    ContactFlowModule: ContactFlowModule
    ResponseMetadata: ResponseMetadata


class SearchContactFlowModulesResponse(BaseValidatorModel):
    ContactFlowModules: List[ContactFlowModule]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListContactFlowsResponse(BaseValidatorModel):
    ContactFlowSummaryList: List[ContactFlowSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ContactFlow(BaseValidatorModel):
    pass


class DescribeContactFlowResponse(BaseValidatorModel):
    ContactFlow: ContactFlow
    ResponseMetadata: ResponseMetadata


class SearchContactFlowsResponse(BaseValidatorModel):
    ContactFlows: List[ContactFlow]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListContactFlowVersionsResponse(BaseValidatorModel):
    ContactFlowVersionSummaryList: List[ContactFlowVersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ContactSearchSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    InitialContactId: Optional[str] = None
    PreviousContactId: Optional[str] = None
    InitiationMethod: Optional[ContactInitiationMethodType] = None
    Channel: Optional[ChannelType] = None
    QueueInfo: Optional[ContactSearchSummaryQueueInfo] = None
    AgentInfo: Optional[ContactSearchSummaryAgentInfo] = None
    InitiationTimestamp: Optional[datetime] = None
    DisconnectTimestamp: Optional[datetime] = None
    ScheduledTimestamp: Optional[datetime] = None
    SegmentAttributes: Optional[Dict[str, ContactSearchSummarySegmentAttributeValue]] = None


class Timestamp(BaseValidatorModel):
    pass


class CreateContactFlowVersionRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    Description: Optional[str] = None
    FlowContentSha256: Optional[str] = None
    ContactFlowVersion: Optional[int] = None
    LastModifiedTime: Optional[Timestamp] = None
    LastModifiedRegion: Optional[str] = None


class UpdateContactScheduleRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ScheduledTime: Timestamp


class Reference(BaseValidatorModel):
    pass


class StartOutboundVoiceContactRequest(BaseValidatorModel):
    DestinationPhoneNumber: str
    ContactFlowId: str
    InstanceId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    References: Optional[Mapping[str, Reference]] = None
    RelatedContactId: Optional[str] = None
    ClientToken: Optional[str] = None
    SourcePhoneNumber: Optional[str] = None
    QueueId: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    AnswerMachineDetectionConfig: Optional[AnswerMachineDetectionConfig] = None
    CampaignId: Optional[str] = None
    TrafficType: Optional[TrafficTypeType] = None


class TaskActionDefinitionOutput(BaseValidatorModel):
    Name: str
    ContactFlowId: str
    Description: Optional[str] = None
    References: Optional[Dict[str, Reference]] = None


class TaskActionDefinition(BaseValidatorModel):
    Name: str
    ContactFlowId: str
    Description: Optional[str] = None
    References: Optional[Mapping[str, Reference]] = None


class CreateParticipantRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ParticipantDetails: ParticipantDetailsToAdd
    ClientToken: Optional[str] = None


class CreateParticipantResponse(BaseValidatorModel):
    ParticipantCredentials: ParticipantTokenCredentials
    ParticipantId: str
    ResponseMetadata: ResponseMetadata


class UpdateQueueOutboundCallerConfigRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    OutboundCallerConfig: OutboundCallerConfig


class CreateQueueRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    HoursOfOperationId: str
    Description: Optional[str] = None
    OutboundCallerConfig: Optional[OutboundCallerConfig] = None
    OutboundEmailConfig: Optional[OutboundEmailConfig] = None
    MaxContacts: Optional[int] = None
    QuickConnectIds: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None


class Queue(BaseValidatorModel):
    Name: Optional[str] = None
    QueueArn: Optional[str] = None
    QueueId: Optional[str] = None
    Description: Optional[str] = None
    OutboundCallerConfig: Optional[OutboundCallerConfig] = None
    OutboundEmailConfig: Optional[OutboundEmailConfig] = None
    HoursOfOperationId: Optional[str] = None
    MaxContacts: Optional[int] = None
    Status: Optional[QueueStatusType] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class UpdateQueueOutboundEmailConfigRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    OutboundEmailConfig: OutboundEmailConfig


class UpdateUserIdentityInfoRequest(BaseValidatorModel):
    IdentityInfo: UserIdentityInfo
    UserId: str
    InstanceId: str


class CreateUserRequest(BaseValidatorModel):
    Username: str
    PhoneConfig: UserPhoneConfig
    SecurityProfileIds: Sequence[str]
    RoutingProfileId: str
    InstanceId: str
    Password: Optional[str] = None
    IdentityInfo: Optional[UserIdentityInfo] = None
    DirectoryUserId: Optional[str] = None
    HierarchyGroupId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateUserPhoneConfigRequest(BaseValidatorModel):
    PhoneConfig: UserPhoneConfig
    UserId: str
    InstanceId: str


class User(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Username: Optional[str] = None
    IdentityInfo: Optional[UserIdentityInfo] = None
    PhoneConfig: Optional[UserPhoneConfig] = None
    DirectoryUserId: Optional[str] = None
    SecurityProfileIds: Optional[List[str]] = None
    RoutingProfileId: Optional[str] = None
    HierarchyGroupId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class CreateViewRequest(BaseValidatorModel):
    InstanceId: str
    Status: ViewStatusType
    Content: ViewInputContent
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateViewContentRequest(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    Status: ViewStatusType
    Content: ViewInputContent


class GetFederationTokenResponse(BaseValidatorModel):
    Credentials: Credentials
    SignInUrl: str
    UserArn: str
    UserId: str
    ResponseMetadata: ResponseMetadata


class MediaConcurrency(BaseValidatorModel):
    Channel: ChannelType
    Concurrency: int
    CrossChannelBehavior: Optional[CrossChannelBehavior] = None


class CurrentMetricData(BaseValidatorModel):
    Metric: Optional[CurrentMetric] = None
    Value: Optional[float] = None


class DateCondition(BaseValidatorModel):
    pass


class HoursOfOperationOverrideSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    DateCondition: Optional[DateCondition] = None


class HoursOfOperationOverrideSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    DateCondition: Optional[DateCondition] = None


class ListDefaultVocabulariesResponse(BaseValidatorModel):
    DefaultVocabularyList: List[DefaultVocabulary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribePromptResponse(BaseValidatorModel):
    Prompt: Prompt
    ResponseMetadata: ResponseMetadata


class SearchPromptsResponse(BaseValidatorModel):
    Prompts: List[Prompt]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeSecurityProfileResponse(BaseValidatorModel):
    SecurityProfile: SecurityProfile
    ResponseMetadata: ResponseMetadata


class DescribeTrafficDistributionGroupResponse(BaseValidatorModel):
    TrafficDistributionGroup: TrafficDistributionGroup
    ResponseMetadata: ResponseMetadata


class DescribeVocabularyResponse(BaseValidatorModel):
    Vocabulary: Vocabulary
    ResponseMetadata: ResponseMetadata


class Dimensions(BaseValidatorModel):
    Queue: Optional[QueueReference] = None
    Channel: Optional[ChannelType] = None
    RoutingProfile: Optional[RoutingProfileReference] = None
    RoutingStepExpression: Optional[str] = None


class DisassociateRoutingProfileQueuesRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    QueueReferences: Sequence[RoutingProfileQueueReference]


class RoutingProfileQueueConfig(BaseValidatorModel):
    QueueReference: RoutingProfileQueueReference
    Priority: int
    Delay: int


class DisassociateUserProficienciesRequest(BaseValidatorModel):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiencyDisassociate]


class StopContactRequest(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    DisconnectReason: Optional[DisconnectReason] = None


class GetAttachedFileResponse(BaseValidatorModel):
    FileArn: str
    FileId: str
    CreationTime: str
    FileStatus: FileStatusTypeType
    FileName: str
    FileSizeInBytes: int
    AssociatedResourceArn: str
    FileUseCaseType: FileUseCaseTypeType
    CreatedBy: CreatedByInfo
    DownloadUrlMetadata: DownloadUrlMetadata
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class InboundAdditionalRecipients(BaseValidatorModel):
    ToAddresses: Optional[Sequence[EmailAddressInfo]] = None
    CcAddresses: Optional[Sequence[EmailAddressInfo]] = None


class OutboundAdditionalRecipients(BaseValidatorModel):
    CcEmailAddresses: Optional[Sequence[EmailAddressInfo]] = None


class SearchEmailAddressesResponse(BaseValidatorModel):
    EmailAddresses: List[EmailAddressMetadata]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class KinesisVideoStreamConfig(BaseValidatorModel):
    Prefix: str
    RetentionPeriodHours: int
    EncryptionConfig: EncryptionConfig


class S3Config(BaseValidatorModel):
    BucketName: str
    BucketPrefix: str
    EncryptionConfig: Optional[EncryptionConfig] = None


class EvaluationAnswerInput(BaseValidatorModel):
    Value: Optional[EvaluationAnswerData] = None


class EvaluationAnswerOutput(BaseValidatorModel):
    Value: Optional[EvaluationAnswerData] = None
    SystemSuggestedValue: Optional[EvaluationAnswerData] = None


class EvaluationFormNumericQuestionAutomation(BaseValidatorModel):
    PropertyValue: Optional[NumericQuestionPropertyValueAutomation] = None


class EvaluationFormSingleSelectQuestionAutomationOption(BaseValidatorModel):
    RuleCategory: Optional[SingleSelectQuestionRuleCategoryAutomation] = None


class ListEvaluationFormsResponse(BaseValidatorModel):
    EvaluationFormSummaryList: List[EvaluationFormSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListEvaluationFormVersionsResponse(BaseValidatorModel):
    EvaluationFormVersionSummaryList: List[EvaluationFormVersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class EvaluationMetadata(BaseValidatorModel):
    ContactId: str
    EvaluatorArn: str
    ContactAgentId: Optional[str] = None
    Score: Optional[EvaluationScore] = None


class EvaluationSummary(BaseValidatorModel):
    EvaluationId: str
    EvaluationArn: str
    EvaluationFormTitle: str
    EvaluationFormId: str
    Status: EvaluationStatusType
    EvaluatorArn: str
    CreatedTime: datetime
    LastModifiedTime: datetime
    Score: Optional[EvaluationScore] = None


class FieldValueOutput(BaseValidatorModel):
    Id: str
    Value: FieldValueUnionOutput


class GetCurrentMetricDataRequest(BaseValidatorModel):
    InstanceId: str
    Filters: Filters
    CurrentMetrics: Sequence[CurrentMetric]
    Groupings: Optional[Sequence[GroupingType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortCriteria: Optional[Sequence[CurrentMetricSortCriteria]] = None


class ListAgentStatusRequestPaginate(BaseValidatorModel):
    InstanceId: str
    AgentStatusTypes: Optional[Sequence[AgentStatusTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListApprovedOriginsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListAuthenticationProfilesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListBotsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    LexVersion: LexVersionType
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContactEvaluationsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContactFlowModulesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleState: Optional[ContactFlowModuleStateType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContactFlowVersionsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContactFlowsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    ContactFlowTypes: Optional[Sequence[ContactFlowTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContactReferencesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ReferenceTypes: Sequence[ReferenceTypeType]
    PaginationConfig: Optional[PaginatorConfig] = None


class ListDefaultVocabulariesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    LanguageCode: Optional[VocabularyLanguageCodeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEvaluationFormVersionsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListEvaluationFormsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListFlowAssociationsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    ResourceType: Optional[ListFlowAssociationResourceTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHoursOfOperationOverridesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListHoursOfOperationsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstanceAttributesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstanceStorageConfigsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    PaginationConfig: Optional[PaginatorConfig] = None


class ListInstancesRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListIntegrationAssociationsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    IntegrationType: Optional[IntegrationTypeType] = None
    IntegrationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLambdaFunctionsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListLexBotsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPhoneNumbersRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPhoneNumbersV2RequestPaginate(BaseValidatorModel):
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPredefinedAttributesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPromptsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQueueQuickConnectsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQueuesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    QueueTypes: Optional[Sequence[QueueTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQuickConnectsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    QuickConnectTypes: Optional[Sequence[QuickConnectTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRoutingProfileQueuesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRoutingProfilesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRulesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PublishStatus: Optional[RulePublishStatusType] = None
    EventSourceName: Optional[EventSourceNameType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSecurityKeysRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSecurityProfileApplicationsRequestPaginate(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSecurityProfilePermissionsRequestPaginate(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSecurityProfilesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTaskTemplatesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    Status: Optional[TaskTemplateStatusType] = None
    Name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrafficDistributionGroupUsersRequestPaginate(BaseValidatorModel):
    TrafficDistributionGroupId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListTrafficDistributionGroupsRequestPaginate(BaseValidatorModel):
    InstanceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUseCasesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUserHierarchyGroupsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUserProficienciesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    UserId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsersRequestPaginate(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListViewVersionsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchAvailablePhoneNumbersRequestPaginate(BaseValidatorModel):
    PhoneNumberCountryCode: PhoneNumberCountryCodeType
    PhoneNumberType: PhoneNumberTypeType
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchVocabulariesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    State: Optional[VocabularyStateType] = None
    NameStartsWith: Optional[str] = None
    LanguageCode: Optional[VocabularyLanguageCodeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class HierarchyPathReference(BaseValidatorModel):
    LevelOne: Optional[HierarchyGroupSummaryReference] = None
    LevelTwo: Optional[HierarchyGroupSummaryReference] = None
    LevelThree: Optional[HierarchyGroupSummaryReference] = None
    LevelFour: Optional[HierarchyGroupSummaryReference] = None
    LevelFive: Optional[HierarchyGroupSummaryReference] = None


class HierarchyPath(BaseValidatorModel):
    LevelOne: Optional[HierarchyGroupSummary] = None
    LevelTwo: Optional[HierarchyGroupSummary] = None
    LevelThree: Optional[HierarchyGroupSummary] = None
    LevelFour: Optional[HierarchyGroupSummary] = None
    LevelFive: Optional[HierarchyGroupSummary] = None


class ListUserHierarchyGroupsResponse(BaseValidatorModel):
    UserHierarchyGroupSummaryList: List[HierarchyGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class HierarchyStructure(BaseValidatorModel):
    LevelOne: Optional[HierarchyLevel] = None
    LevelTwo: Optional[HierarchyLevel] = None
    LevelThree: Optional[HierarchyLevel] = None
    LevelFour: Optional[HierarchyLevel] = None
    LevelFive: Optional[HierarchyLevel] = None


class HierarchyStructureUpdate(BaseValidatorModel):
    LevelOne: Optional[HierarchyLevelUpdate] = None
    LevelTwo: Optional[HierarchyLevelUpdate] = None
    LevelThree: Optional[HierarchyLevelUpdate] = None
    LevelFour: Optional[HierarchyLevelUpdate] = None
    LevelFive: Optional[HierarchyLevelUpdate] = None


class HistoricalMetric(BaseValidatorModel):
    Name: Optional[HistoricalMetricNameType] = None
    Threshold: Optional[Threshold] = None
    Statistic: Optional[StatisticType] = None
    Unit: Optional[UnitType] = None


class HoursOfOperationConfig(BaseValidatorModel):
    Day: HoursOfOperationDaysType
    StartTime: HoursOfOperationTimeSlice
    EndTime: HoursOfOperationTimeSlice


class HoursOfOperationOverrideConfig(BaseValidatorModel):
    Day: Optional[OverrideDaysType] = None
    StartTime: Optional[OverrideTimeSlice] = None
    EndTime: Optional[OverrideTimeSlice] = None


class OperationalHour(BaseValidatorModel):
    Start: Optional[OverrideTimeSlice] = None
    End: Optional[OverrideTimeSlice] = None


class ListHoursOfOperationsResponse(BaseValidatorModel):
    HoursOfOperationSummaryList: List[HoursOfOperationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InboundEmailContent(BaseValidatorModel):
    MessageSourceType: Literal["RAW"]
    RawMessage: Optional[InboundRawMessage] = None


class Instance(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    IdentityManagementType: Optional[DirectoryTypeType] = None
    InstanceAlias: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    ServiceRole: Optional[str] = None
    InstanceStatus: Optional[InstanceStatusType] = None
    StatusReason: Optional[InstanceStatusReason] = None
    InboundCallsEnabled: Optional[bool] = None
    OutboundCallsEnabled: Optional[bool] = None
    InstanceAccessUrl: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class ListInstancesResponse(BaseValidatorModel):
    InstanceSummaryList: List[InstanceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListIntegrationAssociationsResponse(BaseValidatorModel):
    IntegrationAssociationSummaryList: List[IntegrationAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InvisibleFieldInfo(BaseValidatorModel):
    Id: Optional[TaskTemplateFieldIdentifier] = None


class ReadOnlyFieldInfo(BaseValidatorModel):
    Id: Optional[TaskTemplateFieldIdentifier] = None


class RequiredFieldInfo(BaseValidatorModel):
    Id: Optional[TaskTemplateFieldIdentifier] = None


class TaskTemplateDefaultFieldValue(BaseValidatorModel):
    Id: Optional[TaskTemplateFieldIdentifier] = None
    DefaultValue: Optional[str] = None


class ListPhoneNumbersResponse(BaseValidatorModel):
    PhoneNumberSummaryList: List[PhoneNumberSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPhoneNumbersV2Response(BaseValidatorModel):
    ListPhoneNumbersSummaryList: List[ListPhoneNumbersSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPredefinedAttributesResponse(BaseValidatorModel):
    PredefinedAttributeSummaryList: List[PredefinedAttributeSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListPromptsResponse(BaseValidatorModel):
    PromptSummaryList: List[PromptSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListQueueQuickConnectsResponse(BaseValidatorModel):
    QuickConnectSummaryList: List[QuickConnectSummary]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListQuickConnectsResponse(BaseValidatorModel):
    QuickConnectSummaryList: List[QuickConnectSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListQueuesResponse(BaseValidatorModel):
    QueueSummaryList: List[QueueSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRoutingProfileQueuesResponse(BaseValidatorModel):
    RoutingProfileQueueConfigSummaryList: List[RoutingProfileQueueConfigSummary]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListRoutingProfilesResponse(BaseValidatorModel):
    RoutingProfileSummaryList: List[RoutingProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSecurityKeysResponse(BaseValidatorModel):
    SecurityKeys: List[SecurityKey]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListSecurityProfilesResponse(BaseValidatorModel):
    SecurityProfileSummaryList: List[SecurityProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTaskTemplatesResponse(BaseValidatorModel):
    TaskTemplates: List[TaskTemplateMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTrafficDistributionGroupUsersResponse(BaseValidatorModel):
    TrafficDistributionGroupUserSummaryList: List[TrafficDistributionGroupUserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListTrafficDistributionGroupsResponse(BaseValidatorModel):
    TrafficDistributionGroupSummaryList: List[TrafficDistributionGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListUseCasesResponse(BaseValidatorModel):
    UseCaseSummaryList: List[UseCase]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListUsersResponse(BaseValidatorModel):
    UserSummaryList: List[UserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ViewVersionSummary(BaseValidatorModel):
    pass


class ListViewVersionsResponse(BaseValidatorModel):
    ViewVersionSummaryList: List[ViewVersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ViewSummary(BaseValidatorModel):
    pass


class ListViewsResponse(BaseValidatorModel):
    ViewsSummaryList: List[ViewSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MetricV2Output(BaseValidatorModel):
    Name: Optional[str] = None
    Threshold: Optional[List[ThresholdV2]] = None
    MetricFilters: Optional[List[MetricFilterV2Output]] = None


class NewSessionDetails(BaseValidatorModel):
    SupportedMessagingContentTypes: Optional[Sequence[str]] = None
    ParticipantDetails: Optional[ParticipantDetails] = None
    Attributes: Optional[Mapping[str, str]] = None
    StreamingConfiguration: Optional[ChatStreamingConfiguration] = None


class SendNotificationActionDefinitionOutput(BaseValidatorModel):
    DeliveryMethod: Literal["EMAIL"]
    Content: str
    ContentType: Literal["PLAIN_TEXT"]
    Recipient: NotificationRecipientTypeOutput
    Subject: Optional[str] = None


class ParticipantTimerConfiguration(BaseValidatorModel):
    ParticipantRole: TimerEligibleParticipantRolesType
    TimerType: ParticipantTimerTypeType
    TimerValue: ParticipantTimerValue


class PredefinedAttribute(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[PredefinedAttributeValuesOutput] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class QuickConnectConfig(BaseValidatorModel):
    QuickConnectType: QuickConnectTypeType
    UserConfig: Optional[UserQuickConnectConfig] = None
    QueueConfig: Optional[QueueQuickConnectConfig] = None
    PhoneConfig: Optional[PhoneNumberQuickConnectConfig] = None


class RealTimeContactAnalysisTranscriptItemRedaction(BaseValidatorModel):
    CharacterOffsets: Optional[List[RealTimeContactAnalysisCharacterInterval]] = None


class RealTimeContactAnalysisTranscriptItemWithCharacterOffsets(BaseValidatorModel):
    Id: str
    CharacterOffsets: Optional[RealTimeContactAnalysisCharacterInterval] = None


class RealTimeContactAnalysisTranscriptItemWithContent(BaseValidatorModel):
    Id: str
    Content: Optional[str] = None
    CharacterOffsets: Optional[RealTimeContactAnalysisCharacterInterval] = None


class RealTimeContactAnalysisSegmentAttachments(BaseValidatorModel):
    Id: str
    ParticipantId: str
    ParticipantRole: ParticipantRoleType
    Attachments: List[RealTimeContactAnalysisAttachment]
    Time: RealTimeContactAnalysisTimeData
    DisplayName: Optional[str] = None


class RealTimeContactAnalysisSegmentEvent(BaseValidatorModel):
    Id: str
    EventType: str
    Time: RealTimeContactAnalysisTimeData
    ParticipantId: Optional[str] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    DisplayName: Optional[str] = None


class ReferenceSummary(BaseValidatorModel):
    Url: Optional[UrlReference] = None
    Attachment: Optional[AttachmentReference] = None
    EmailMessage: Optional[EmailMessageReference] = None
    String: Optional[StringReference] = None
    Number: Optional[NumberReference] = None
    Date: Optional[DateReference] = None
    Email: Optional[EmailReference] = None


class ReplicationConfiguration(BaseValidatorModel):
    ReplicationStatusSummaryList: Optional[List[ReplicationStatusSummary]] = None
    SourceRegion: Optional[str] = None
    GlobalSignInEndpoint: Optional[str] = None


class ResourceTagsSearchCriteria(BaseValidatorModel):
    TagSearchCondition: Optional[TagSearchCondition] = None


class SearchResourceTagsResponse(BaseValidatorModel):
    Tags: List[TagSet]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchSecurityProfilesResponse(BaseValidatorModel):
    SecurityProfiles: List[SecurityProfileSearchSummary]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchVocabulariesResponse(BaseValidatorModel):
    VocabularySummaryList: List[VocabularySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchableContactAttributes(BaseValidatorModel):
    Criteria: Sequence[SearchableContactAttributesCriteria]
    MatchType: Optional[SearchContactsMatchTypeType] = None


class SearchableSegmentAttributes(BaseValidatorModel):
    Criteria: Sequence[SearchableSegmentAttributesCriteria]
    MatchType: Optional[SearchContactsMatchTypeType] = None


class SignInConfigOutput(BaseValidatorModel):
    Distributions: List[SignInDistribution]


class SignInConfig(BaseValidatorModel):
    Distributions: Sequence[SignInDistribution]


class StartAttachedFileUploadResponse(BaseValidatorModel):
    FileArn: str
    FileId: str
    CreationTime: str
    FileStatus: FileStatusTypeType
    CreatedBy: CreatedByInfo
    UploadUrlMetadata: UploadUrlMetadata
    ResponseMetadata: ResponseMetadata


class StartContactRecordingRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    VoiceRecordingConfiguration: VoiceRecordingConfiguration


class TemplatedMessageConfig(BaseValidatorModel):
    KnowledgeBaseId: str
    MessageTemplateId: str
    TemplateAttributes: TemplateAttributes


class Transcript(BaseValidatorModel):
    Criteria: Sequence[TranscriptCriteria]
    MatchType: Optional[SearchContactsMatchTypeType] = None


class UserSearchSummary(BaseValidatorModel):
    Arn: Optional[str] = None
    DirectoryUserId: Optional[str] = None
    HierarchyGroupId: Optional[str] = None
    Id: Optional[str] = None
    IdentityInfo: Optional[UserIdentityInfoLite] = None
    PhoneConfig: Optional[UserPhoneConfig] = None
    RoutingProfileId: Optional[str] = None
    SecurityProfileIds: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None
    Username: Optional[str] = None


class ListRulesResponse(BaseValidatorModel):
    RuleSummaryList: List[RuleSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AgentInfo(BaseValidatorModel):
    Id: Optional[str] = None
    ConnectedToAgentTimestamp: Optional[datetime] = None
    AgentPauseDurationInSeconds: Optional[int] = None
    HierarchyGroups: Optional[HierarchyGroups] = None
    DeviceInfo: Optional[DeviceInfo] = None
    Capabilities: Optional[ParticipantCapabilities] = None


class StartWebRTCContactRequest(BaseValidatorModel):
    ContactFlowId: str
    InstanceId: str
    ParticipantDetails: ParticipantDetails
    Attributes: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None
    AllowedCapabilities: Optional[AllowedCapabilities] = None
    RelatedContactId: Optional[str] = None
    References: Optional[Mapping[str, Reference]] = None
    Description: Optional[str] = None


class QualityMetrics(BaseValidatorModel):
    Agent: Optional[AgentQualityMetrics] = None
    Customer: Optional[CustomerQualityMetrics] = None


class SearchPredefinedAttributesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchCriteria: Optional[PredefinedAttributeSearchCriteriaPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchPredefinedAttributesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchCriteria: Optional[PredefinedAttributeSearchCriteria] = None


class AttributeConditionOutput(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    ProficiencyLevel: Optional[float] = None
    Range: Optional[Range] = None
    MatchCriteria: Optional[MatchCriteriaOutput] = None
    ComparisonOperator: Optional[str] = None


class AgentsCriteriaUnion(BaseValidatorModel):
    pass


class MatchCriteria(BaseValidatorModel):
    AgentsCriteria: Optional[AgentsCriteriaUnion] = None


class ApplicationUnion(BaseValidatorModel):
    pass


class CreateSecurityProfileRequest(BaseValidatorModel):
    SecurityProfileName: str
    InstanceId: str
    Description: Optional[str] = None
    Permissions: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None
    AllowedAccessControlTags: Optional[Mapping[str, str]] = None
    TagRestrictedResources: Optional[Sequence[str]] = None
    Applications: Optional[Sequence[ApplicationUnion]] = None
    HierarchyRestrictedResources: Optional[Sequence[str]] = None
    AllowedAccessControlHierarchyGroupId: Optional[str] = None


class UpdateSecurityProfileRequest(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    Description: Optional[str] = None
    Permissions: Optional[Sequence[str]] = None
    AllowedAccessControlTags: Optional[Mapping[str, str]] = None
    TagRestrictedResources: Optional[Sequence[str]] = None
    Applications: Optional[Sequence[ApplicationUnion]] = None
    HierarchyRestrictedResources: Optional[Sequence[str]] = None
    AllowedAccessControlHierarchyGroupId: Optional[str] = None


class ListBotsResponse(BaseValidatorModel):
    LexBots: List[LexBotConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchGetAttachedFileMetadataResponse(BaseValidatorModel):
    Files: List[AttachedFile]
    Errors: List[AttachedFileError]
    ResponseMetadata: ResponseMetadata


class ControlPlaneUserAttributeFilter(BaseValidatorModel):
    OrConditions: Optional[Sequence[AttributeAndCondition]] = None
    AndCondition: Optional[AttributeAndCondition] = None
    TagCondition: Optional[TagCondition] = None
    HierarchyGroupCondition: Optional[HierarchyGroupCondition] = None


class ControlPlaneAttributeFilter(BaseValidatorModel):
    OrConditions: Optional[Sequence[CommonAttributeAndCondition]] = None
    AndCondition: Optional[CommonAttributeAndCondition] = None
    TagCondition: Optional[TagCondition] = None


class ContactFlowModuleSearchFilter(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilter] = None


class ContactFlowSearchFilter(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilter] = None


class EmailAddressSearchFilter(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilter] = None


class HoursOfOperationSearchFilter(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilter] = None


class PromptSearchFilter(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilter] = None


class QueueSearchFilter(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilter] = None


class QuickConnectSearchFilter(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilter] = None


class RoutingProfileSearchFilter(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilter] = None


class SecurityProfilesSearchFilter(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilter] = None


class Meeting(BaseValidatorModel):
    MediaRegion: Optional[str] = None
    MediaPlacement: Optional[MediaPlacement] = None
    MeetingFeatures: Optional[MeetingFeaturesConfiguration] = None
    MeetingId: Optional[str] = None


class DescribePhoneNumberResponse(BaseValidatorModel):
    ClaimedPhoneNumberSummary: ClaimedPhoneNumberSummary
    ResponseMetadata: ResponseMetadata


class ListCondition(BaseValidatorModel):
    TargetListType: Optional[Literal["PROFICIENCIES"]] = None
    Conditions: Optional[Sequence[Condition]] = None


class BatchPutContactRequest(BaseValidatorModel):
    InstanceId: str
    ContactDataRequestList: Sequence[ContactDataRequest]
    ClientToken: Optional[str] = None


class GetCurrentUserDataRequest(BaseValidatorModel):
    InstanceId: str
    Filters: UserDataFilters
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SearchContactsResponse(BaseValidatorModel):
    Contacts: List[ContactSearchSummary]
    TotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeQueueResponse(BaseValidatorModel):
    Queue: Queue
    ResponseMetadata: ResponseMetadata


class SearchQueuesResponse(BaseValidatorModel):
    Queues: List[Queue]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class RoutingProfile(BaseValidatorModel):
    InstanceId: Optional[str] = None
    Name: Optional[str] = None
    RoutingProfileArn: Optional[str] = None
    RoutingProfileId: Optional[str] = None
    Description: Optional[str] = None
    MediaConcurrencies: Optional[List[MediaConcurrency]] = None
    DefaultOutboundQueueId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    NumberOfAssociatedQueues: Optional[int] = None
    NumberOfAssociatedUsers: Optional[int] = None
    AgentAvailabilityTimer: Optional[AgentAvailabilityTimerType] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None
    IsDefault: Optional[bool] = None
    AssociatedQueueIds: Optional[List[str]] = None


class UpdateRoutingProfileConcurrencyRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    MediaConcurrencies: Sequence[MediaConcurrency]


class CurrentMetricResult(BaseValidatorModel):
    Dimensions: Optional[Dimensions] = None
    Collections: Optional[List[CurrentMetricData]] = None


class AssociateRoutingProfileQueuesRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    QueueConfigs: Sequence[RoutingProfileQueueConfig]


class CreateRoutingProfileRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    Description: str
    DefaultOutboundQueueId: str
    MediaConcurrencies: Sequence[MediaConcurrency]
    QueueConfigs: Optional[Sequence[RoutingProfileQueueConfig]] = None
    Tags: Optional[Mapping[str, str]] = None
    AgentAvailabilityTimer: Optional[AgentAvailabilityTimerType] = None


class UpdateRoutingProfileQueuesRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    QueueConfigs: Sequence[RoutingProfileQueueConfig]


class InstanceStorageConfig(BaseValidatorModel):
    StorageType: StorageTypeType
    AssociationId: Optional[str] = None
    S3Config: Optional[S3Config] = None
    KinesisVideoStreamConfig: Optional[KinesisVideoStreamConfig] = None
    KinesisStreamConfig: Optional[KinesisStreamConfig] = None
    KinesisFirehoseConfig: Optional[KinesisFirehoseConfig] = None


class SubmitContactEvaluationRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str
    Answers: Optional[Mapping[str, EvaluationAnswerInput]] = None
    Notes: Optional[Mapping[str, EvaluationNote]] = None


class UpdateContactEvaluationRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str
    Answers: Optional[Mapping[str, EvaluationAnswerInput]] = None
    Notes: Optional[Mapping[str, EvaluationNote]] = None


class EvaluationFormNumericQuestionPropertiesOutput(BaseValidatorModel):
    MinValue: int
    MaxValue: int
    Options: Optional[List[EvaluationFormNumericQuestionOption]] = None
    Automation: Optional[EvaluationFormNumericQuestionAutomation] = None


class EvaluationFormNumericQuestionProperties(BaseValidatorModel):
    MinValue: int
    MaxValue: int
    Options: Optional[Sequence[EvaluationFormNumericQuestionOption]] = None
    Automation: Optional[EvaluationFormNumericQuestionAutomation] = None


class EvaluationFormSingleSelectQuestionAutomationOutput(BaseValidatorModel):
    Options: List[EvaluationFormSingleSelectQuestionAutomationOption]
    DefaultOptionRefId: Optional[str] = None


class EvaluationFormSingleSelectQuestionAutomation(BaseValidatorModel):
    Options: Sequence[EvaluationFormSingleSelectQuestionAutomationOption]
    DefaultOptionRefId: Optional[str] = None


class Evaluation(BaseValidatorModel):
    EvaluationId: str
    EvaluationArn: str
    Metadata: EvaluationMetadata
    Answers: Dict[str, EvaluationAnswerOutput]
    Notes: Dict[str, EvaluationNote]
    Status: EvaluationStatusType
    CreatedTime: datetime
    LastModifiedTime: datetime
    Scores: Optional[Dict[str, EvaluationScore]] = None
    Tags: Optional[Dict[str, str]] = None


class ListContactEvaluationsResponse(BaseValidatorModel):
    EvaluationSummaryList: List[EvaluationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateCaseActionDefinitionOutput(BaseValidatorModel):
    Fields: List[FieldValueOutput]
    TemplateId: str


class UpdateCaseActionDefinitionOutput(BaseValidatorModel):
    Fields: List[FieldValueOutput]


class FieldValueUnionUnion(BaseValidatorModel):
    pass


class FieldValue(BaseValidatorModel):
    Id: str
    Value: FieldValueUnionUnion


class UserData(BaseValidatorModel):
    User: Optional[UserReference] = None
    RoutingProfile: Optional[RoutingProfileReference] = None
    HierarchyPath: Optional[HierarchyPathReference] = None
    Status: Optional[AgentStatusReference] = None
    AvailableSlotsByChannel: Optional[Dict[ChannelType, int]] = None
    MaxSlotsByChannel: Optional[Dict[ChannelType, int]] = None
    ActiveSlotsByChannel: Optional[Dict[ChannelType, int]] = None
    Contacts: Optional[List[AgentContactReference]] = None
    NextStatus: Optional[str] = None


class HierarchyGroup(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LevelId: Optional[str] = None
    HierarchyPath: Optional[HierarchyPath] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class DescribeUserHierarchyStructureResponse(BaseValidatorModel):
    HierarchyStructure: HierarchyStructure
    ResponseMetadata: ResponseMetadata


class UpdateUserHierarchyStructureRequest(BaseValidatorModel):
    HierarchyStructure: HierarchyStructureUpdate
    InstanceId: str


class GetMetricDataRequestPaginate(BaseValidatorModel):
    InstanceId: str
    StartTime: Timestamp
    EndTime: Timestamp
    Filters: Filters
    HistoricalMetrics: Sequence[HistoricalMetric]
    Groupings: Optional[Sequence[GroupingType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class GetMetricDataRequest(BaseValidatorModel):
    InstanceId: str
    StartTime: Timestamp
    EndTime: Timestamp
    Filters: Filters
    HistoricalMetrics: Sequence[HistoricalMetric]
    Groupings: Optional[Sequence[GroupingType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class HistoricalMetricData(BaseValidatorModel):
    Metric: Optional[HistoricalMetric] = None
    Value: Optional[float] = None


class CreateHoursOfOperationRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    TimeZone: str
    Config: Sequence[HoursOfOperationConfig]
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class HoursOfOperation(BaseValidatorModel):
    HoursOfOperationId: Optional[str] = None
    HoursOfOperationArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    TimeZone: Optional[str] = None
    Config: Optional[List[HoursOfOperationConfig]] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class UpdateHoursOfOperationRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    TimeZone: Optional[str] = None
    Config: Optional[Sequence[HoursOfOperationConfig]] = None


class CreateHoursOfOperationOverrideRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    Name: str
    Config: Sequence[HoursOfOperationOverrideConfig]
    EffectiveFrom: str
    EffectiveTill: str
    Description: Optional[str] = None


class HoursOfOperationOverride(BaseValidatorModel):
    HoursOfOperationOverrideId: Optional[str] = None
    HoursOfOperationId: Optional[str] = None
    HoursOfOperationArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Config: Optional[List[HoursOfOperationOverrideConfig]] = None
    EffectiveFrom: Optional[str] = None
    EffectiveTill: Optional[str] = None


class UpdateHoursOfOperationOverrideRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    HoursOfOperationOverrideId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Config: Optional[Sequence[HoursOfOperationOverrideConfig]] = None
    EffectiveFrom: Optional[str] = None
    EffectiveTill: Optional[str] = None


class EffectiveHoursOfOperations(BaseValidatorModel):
    Date: Optional[str] = None
    OperationalHours: Optional[List[OperationalHour]] = None


class TaskTemplateConstraintsOutput(BaseValidatorModel):
    RequiredFields: Optional[List[RequiredFieldInfo]] = None
    ReadOnlyFields: Optional[List[ReadOnlyFieldInfo]] = None
    InvisibleFields: Optional[List[InvisibleFieldInfo]] = None


class TaskTemplateConstraints(BaseValidatorModel):
    RequiredFields: Optional[Sequence[RequiredFieldInfo]] = None
    ReadOnlyFields: Optional[Sequence[ReadOnlyFieldInfo]] = None
    InvisibleFields: Optional[Sequence[InvisibleFieldInfo]] = None


class TaskTemplateDefaultsOutput(BaseValidatorModel):
    DefaultFieldValues: Optional[List[TaskTemplateDefaultFieldValue]] = None


class TaskTemplateDefaults(BaseValidatorModel):
    DefaultFieldValues: Optional[Sequence[TaskTemplateDefaultFieldValue]] = None


class MetricFilterV2Union(BaseValidatorModel):
    pass


class MetricV2(BaseValidatorModel):
    Name: Optional[str] = None
    Threshold: Optional[Sequence[ThresholdV2]] = None
    MetricFilters: Optional[Sequence[MetricFilterV2Union]] = None


class MetricDataV2(BaseValidatorModel):
    Metric: Optional[MetricV2Output] = None
    Value: Optional[float] = None


class ChatEvent(BaseValidatorModel):
    pass


class SendChatIntegrationEventRequest(BaseValidatorModel):
    SourceId: str
    DestinationId: str
    Event: ChatEvent
    Subtype: Optional[str] = None
    NewSessionDetails: Optional[NewSessionDetails] = None


class NotificationRecipientTypeUnion(BaseValidatorModel):
    pass


class SendNotificationActionDefinition(BaseValidatorModel):
    DeliveryMethod: Literal["EMAIL"]
    Content: str
    ContentType: Literal["PLAIN_TEXT"]
    Recipient: NotificationRecipientTypeUnion
    Subject: Optional[str] = None


class ChatParticipantRoleConfig(BaseValidatorModel):
    ParticipantTimerConfigList: Sequence[ParticipantTimerConfiguration]


class DescribePredefinedAttributeResponse(BaseValidatorModel):
    PredefinedAttribute: PredefinedAttribute
    ResponseMetadata: ResponseMetadata


class SearchPredefinedAttributesResponse(BaseValidatorModel):
    PredefinedAttributes: List[PredefinedAttribute]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class PredefinedAttributeValuesUnion(BaseValidatorModel):
    pass


class CreatePredefinedAttributeRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    Values: PredefinedAttributeValuesUnion


class UpdatePredefinedAttributeRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    Values: Optional[PredefinedAttributeValuesUnion] = None


class CreateQuickConnectRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    QuickConnectConfig: QuickConnectConfig
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class QuickConnect(BaseValidatorModel):
    QuickConnectARN: Optional[str] = None
    QuickConnectId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    QuickConnectConfig: Optional[QuickConnectConfig] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class UpdateQuickConnectConfigRequest(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str
    QuickConnectConfig: QuickConnectConfig


class RealTimeContactAnalysisSegmentTranscript(BaseValidatorModel):
    Id: str
    ParticipantId: str
    ParticipantRole: ParticipantRoleType
    Content: str
    Time: RealTimeContactAnalysisTimeData
    DisplayName: Optional[str] = None
    ContentType: Optional[str] = None
    Redaction: Optional[RealTimeContactAnalysisTranscriptItemRedaction] = None
    Sentiment: Optional[RealTimeContactAnalysisSentimentLabelType] = None


class RealTimeContactAnalysisPointOfInterest(BaseValidatorModel):
    TranscriptItems: Optional[ List[RealTimeContactAnalysisTranscriptItemWithCharacterOffsets] ] = None


class RealTimeContactAnalysisIssueDetected(BaseValidatorModel):
    TranscriptItems: List[RealTimeContactAnalysisTranscriptItemWithContent]


class ListContactReferencesResponse(BaseValidatorModel):
    ReferenceSummaryList: List[ReferenceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeInstanceResponse(BaseValidatorModel):
    Instance: Instance
    ReplicationConfiguration: ReplicationConfiguration
    ResponseMetadata: ResponseMetadata


class SearchResourceTagsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    ResourceTypes: Optional[Sequence[str]] = None
    SearchCriteria: Optional[ResourceTagsSearchCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchResourceTagsRequest(BaseValidatorModel):
    InstanceId: str
    ResourceTypes: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchCriteria: Optional[ResourceTagsSearchCriteria] = None


class SegmentAttributeValueUnion(BaseValidatorModel):
    pass


class CreateContactRequest(BaseValidatorModel):
    InstanceId: str
    Channel: ChannelType
    InitiationMethod: ContactInitiationMethodType
    ClientToken: Optional[str] = None
    RelatedContactId: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    References: Optional[Mapping[str, Reference]] = None
    ExpiryDurationInMinutes: Optional[int] = None
    UserInfo: Optional[UserInfo] = None
    InitiateAs: Optional[Literal["CONNECTED_TO_USER"]] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    SegmentAttributes: Optional[Mapping[str, SegmentAttributeValueUnion]] = None
    PreviousContactId: Optional[str] = None


class StartChatContactRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    ParticipantDetails: ParticipantDetails
    Attributes: Optional[Mapping[str, str]] = None
    InitialMessage: Optional[ChatMessage] = None
    ClientToken: Optional[str] = None
    ChatDurationInMinutes: Optional[int] = None
    SupportedMessagingContentTypes: Optional[Sequence[str]] = None
    PersistentChat: Optional[PersistentChat] = None
    RelatedContactId: Optional[str] = None
    SegmentAttributes: Optional[Mapping[str, SegmentAttributeValueUnion]] = None
    CustomerId: Optional[str] = None


class StartEmailContactRequest(BaseValidatorModel):
    InstanceId: str
    FromEmailAddress: EmailAddressInfo
    DestinationEmailAddress: str
    EmailMessage: InboundEmailContent
    Description: Optional[str] = None
    References: Optional[Mapping[str, Reference]] = None
    Name: Optional[str] = None
    AdditionalRecipients: Optional[InboundAdditionalRecipients] = None
    Attachments: Optional[Sequence[EmailAttachment]] = None
    ContactFlowId: Optional[str] = None
    RelatedContactId: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    SegmentAttributes: Optional[Mapping[str, SegmentAttributeValueUnion]] = None
    ClientToken: Optional[str] = None


class StartOutboundChatContactRequest(BaseValidatorModel):
    SourceEndpoint: Endpoint
    DestinationEndpoint: Endpoint
    InstanceId: str
    SegmentAttributes: Mapping[str, SegmentAttributeValueUnion]
    ContactFlowId: str
    Attributes: Optional[Mapping[str, str]] = None
    ChatDurationInMinutes: Optional[int] = None
    ParticipantDetails: Optional[ParticipantDetails] = None
    InitialSystemMessage: Optional[ChatMessage] = None
    RelatedContactId: Optional[str] = None
    SupportedMessagingContentTypes: Optional[Sequence[str]] = None
    ClientToken: Optional[str] = None


class StartTaskContactRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    PreviousContactId: Optional[str] = None
    ContactFlowId: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    References: Optional[Mapping[str, Reference]] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    ScheduledTime: Optional[Timestamp] = None
    TaskTemplateId: Optional[str] = None
    QuickConnectId: Optional[str] = None
    RelatedContactId: Optional[str] = None
    SegmentAttributes: Optional[Mapping[str, SegmentAttributeValueUnion]] = None


class UpdateContactRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    References: Optional[Mapping[str, Reference]] = None
    SegmentAttributes: Optional[Mapping[str, SegmentAttributeValueUnion]] = None
    QueueInfo: Optional[QueueInfoInput] = None
    UserInfo: Optional[UserInfo] = None
    CustomerEndpoint: Optional[Endpoint] = None
    SystemEndpoint: Optional[Endpoint] = None


class GetTrafficDistributionResponse(BaseValidatorModel):
    TelephonyConfig: TelephonyConfigOutput
    Id: str
    Arn: str
    SignInConfig: SignInConfigOutput
    AgentConfig: AgentConfigOutput
    ResponseMetadata: ResponseMetadata


class OutboundEmailContent(BaseValidatorModel):
    MessageSourceType: OutboundMessageSourceTypeType
    TemplatedMessageConfig: Optional[TemplatedMessageConfig] = None
    RawMessage: Optional[OutboundRawMessage] = None


class ContactAnalysis(BaseValidatorModel):
    Transcript: Optional[Transcript] = None


class SearchUsersResponse(BaseValidatorModel):
    Users: List[UserSearchSummary]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class View(BaseValidatorModel):
    pass


class CreateViewResponse(BaseValidatorModel):
    View: View
    ResponseMetadata: ResponseMetadata


class CreateViewVersionResponse(BaseValidatorModel):
    View: View
    ResponseMetadata: ResponseMetadata


class DescribeViewResponse(BaseValidatorModel):
    View: View
    ResponseMetadata: ResponseMetadata


class UpdateViewContentResponse(BaseValidatorModel):
    View: View
    ResponseMetadata: ResponseMetadata


class ExpressionOutput(BaseValidatorModel):
    AttributeCondition: Optional[AttributeConditionOutput] = None
    AndExpression: Optional[List[Dict[str, Any]]] = None
    OrExpression: Optional[List[Dict[str, Any]]] = None
    NotAttributeCondition: Optional[AttributeConditionOutput] = None


class UserSearchFilter(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilter] = None
    UserAttributeFilter: Optional[ControlPlaneUserAttributeFilter] = None


class AgentStatusSearchFilter(BaseValidatorModel):
    AttributeFilter: Optional[ControlPlaneAttributeFilter] = None


class UserHierarchyGroupSearchFilter(BaseValidatorModel):
    AttributeFilter: Optional[ControlPlaneAttributeFilter] = None


class SearchContactFlowModulesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[ContactFlowModuleSearchFilter] = None
    SearchCriteria: Optional[ContactFlowModuleSearchCriteriaPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchContactFlowModulesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[ContactFlowModuleSearchFilter] = None
    SearchCriteria: Optional[ContactFlowModuleSearchCriteria] = None


class SearchContactFlowsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[ContactFlowSearchFilter] = None
    SearchCriteria: Optional[ContactFlowSearchCriteriaPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchContactFlowsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[ContactFlowSearchFilter] = None
    SearchCriteria: Optional[ContactFlowSearchCriteria] = None


class SearchEmailAddressesRequest(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SearchCriteria: Optional[EmailAddressSearchCriteria] = None
    SearchFilter: Optional[EmailAddressSearchFilter] = None


class SearchHoursOfOperationOverridesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[HoursOfOperationSearchFilter] = None
    SearchCriteria: Optional[HoursOfOperationOverrideSearchCriteriaPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchHoursOfOperationOverridesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[HoursOfOperationSearchFilter] = None
    SearchCriteria: Optional[HoursOfOperationOverrideSearchCriteria] = None


class SearchHoursOfOperationsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[HoursOfOperationSearchFilter] = None
    SearchCriteria: Optional[HoursOfOperationSearchCriteriaPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchHoursOfOperationsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[HoursOfOperationSearchFilter] = None
    SearchCriteria: Optional[HoursOfOperationSearchCriteria] = None


class SearchPromptsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[PromptSearchFilter] = None
    SearchCriteria: Optional[PromptSearchCriteriaPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchPromptsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[PromptSearchFilter] = None
    SearchCriteria: Optional[PromptSearchCriteria] = None


class SearchQueuesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[QueueSearchFilter] = None
    SearchCriteria: Optional[QueueSearchCriteriaPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchQueuesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[QueueSearchFilter] = None
    SearchCriteria: Optional[QueueSearchCriteria] = None


class SearchQuickConnectsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[QuickConnectSearchFilter] = None
    SearchCriteria: Optional[QuickConnectSearchCriteriaPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchQuickConnectsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[QuickConnectSearchFilter] = None
    SearchCriteria: Optional[QuickConnectSearchCriteria] = None


class SearchRoutingProfilesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[RoutingProfileSearchFilter] = None
    SearchCriteria: Optional[RoutingProfileSearchCriteriaPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchRoutingProfilesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[RoutingProfileSearchFilter] = None
    SearchCriteria: Optional[RoutingProfileSearchCriteria] = None


class SearchSecurityProfilesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchCriteria: Optional[SecurityProfileSearchCriteriaPaginator] = None
    SearchFilter: Optional[SecurityProfilesSearchFilter] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchSecurityProfilesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchCriteria: Optional[SecurityProfileSearchCriteria] = None
    SearchFilter: Optional[SecurityProfilesSearchFilter] = None


class ConnectionData(BaseValidatorModel):
    Attendee: Optional[Attendee] = None
    Meeting: Optional[Meeting] = None


class UserSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    ListCondition: Optional[ListCondition] = None
    HierarchyGroupCondition: Optional[HierarchyGroupCondition] = None


class UserSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    ListCondition: Optional[ListCondition] = None
    HierarchyGroupCondition: Optional[HierarchyGroupCondition] = None


class DescribeRoutingProfileResponse(BaseValidatorModel):
    RoutingProfile: RoutingProfile
    ResponseMetadata: ResponseMetadata


class SearchRoutingProfilesResponse(BaseValidatorModel):
    RoutingProfiles: List[RoutingProfile]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetCurrentMetricDataResponse(BaseValidatorModel):
    MetricResults: List[CurrentMetricResult]
    DataSnapshotTime: datetime
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class AssociateInstanceStorageConfigRequest(BaseValidatorModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    StorageConfig: InstanceStorageConfig
    ClientToken: Optional[str] = None


class DescribeInstanceStorageConfigResponse(BaseValidatorModel):
    StorageConfig: InstanceStorageConfig
    ResponseMetadata: ResponseMetadata


class ListInstanceStorageConfigsResponse(BaseValidatorModel):
    StorageConfigs: List[InstanceStorageConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateInstanceStorageConfigRequest(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType
    StorageConfig: InstanceStorageConfig
    ClientToken: Optional[str] = None


class EvaluationFormSingleSelectQuestionOption(BaseValidatorModel):
    pass


class EvaluationFormSingleSelectQuestionPropertiesOutput(BaseValidatorModel):
    Options: List[EvaluationFormSingleSelectQuestionOption]
    DisplayAs: Optional[EvaluationFormSingleSelectQuestionDisplayModeType] = None
    Automation: Optional[EvaluationFormSingleSelectQuestionAutomationOutput] = None


class RuleActionOutput(BaseValidatorModel):
    ActionType: ActionTypeType
    TaskAction: Optional[TaskActionDefinitionOutput] = None
    EventBridgeAction: Optional[EventBridgeActionDefinition] = None
    AssignContactCategoryAction: Optional[Dict[str, Any]] = None
    SendNotificationAction: Optional[SendNotificationActionDefinitionOutput] = None
    CreateCaseAction: Optional[CreateCaseActionDefinitionOutput] = None
    UpdateCaseAction: Optional[UpdateCaseActionDefinitionOutput] = None
    EndAssociatedTasksAction: Optional[Dict[str, Any]] = None
    SubmitAutoEvaluationAction: Optional[SubmitAutoEvaluationActionDefinition] = None


class GetCurrentUserDataResponse(BaseValidatorModel):
    UserDataList: List[UserData]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeUserHierarchyGroupResponse(BaseValidatorModel):
    HierarchyGroup: HierarchyGroup
    ResponseMetadata: ResponseMetadata


class SearchUserHierarchyGroupsResponse(BaseValidatorModel):
    UserHierarchyGroups: List[HierarchyGroup]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class HistoricalMetricResult(BaseValidatorModel):
    Dimensions: Optional[Dimensions] = None
    Collections: Optional[List[HistoricalMetricData]] = None


class DescribeHoursOfOperationResponse(BaseValidatorModel):
    HoursOfOperation: HoursOfOperation
    ResponseMetadata: ResponseMetadata


class SearchHoursOfOperationsResponse(BaseValidatorModel):
    HoursOfOperations: List[HoursOfOperation]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeHoursOfOperationOverrideResponse(BaseValidatorModel):
    HoursOfOperationOverride: HoursOfOperationOverride
    ResponseMetadata: ResponseMetadata


class ListHoursOfOperationOverridesResponse(BaseValidatorModel):
    HoursOfOperationOverrideList: List[HoursOfOperationOverride]
    LastModifiedRegion: str
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchHoursOfOperationOverridesResponse(BaseValidatorModel):
    HoursOfOperationOverrides: List[HoursOfOperationOverride]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetEffectiveHoursOfOperationsResponse(BaseValidatorModel):
    EffectiveHoursOfOperationList: List[EffectiveHoursOfOperations]
    TimeZone: str
    ResponseMetadata: ResponseMetadata


class TaskTemplateFieldOutput(BaseValidatorModel):
    pass


class GetTaskTemplateResponse(BaseValidatorModel):
    InstanceId: str
    Id: str
    Arn: str
    Name: str
    Description: str
    ContactFlowId: str
    SelfAssignFlowId: str
    Constraints: TaskTemplateConstraintsOutput
    Defaults: TaskTemplateDefaultsOutput
    Fields: List[TaskTemplateFieldOutput]
    Status: TaskTemplateStatusType
    LastModifiedTime: datetime
    CreatedTime: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class UpdateTaskTemplateResponse(BaseValidatorModel):
    InstanceId: str
    Id: str
    Arn: str
    Name: str
    Description: str
    ContactFlowId: str
    SelfAssignFlowId: str
    Constraints: TaskTemplateConstraintsOutput
    Defaults: TaskTemplateDefaultsOutput
    Fields: List[TaskTemplateFieldOutput]
    Status: TaskTemplateStatusType
    LastModifiedTime: datetime
    CreatedTime: datetime
    ResponseMetadata: ResponseMetadata


class MetricResultV2(BaseValidatorModel):
    Dimensions: Optional[Dict[str, str]] = None
    MetricInterval: Optional[MetricInterval] = None
    Collections: Optional[List[MetricDataV2]] = None


class UpdateParticipantRoleConfigChannelInfo(BaseValidatorModel):
    Chat: Optional[ChatParticipantRoleConfig] = None


class DescribeQuickConnectResponse(BaseValidatorModel):
    QuickConnect: QuickConnect
    ResponseMetadata: ResponseMetadata


class SearchQuickConnectsResponse(BaseValidatorModel):
    QuickConnects: List[QuickConnect]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RealTimeContactAnalysisCategoryDetails(BaseValidatorModel):
    PointsOfInterest: List[RealTimeContactAnalysisPointOfInterest]


class RealTimeContactAnalysisSegmentIssues(BaseValidatorModel):
    IssuesDetected: List[RealTimeContactAnalysisIssueDetected]


class TelephonyConfigUnion(BaseValidatorModel):
    pass


class AgentConfigUnion(BaseValidatorModel):
    pass


class SignInConfigUnion(BaseValidatorModel):
    pass


class UpdateTrafficDistributionRequest(BaseValidatorModel):
    Id: str
    TelephonyConfig: Optional[TelephonyConfigUnion] = None
    SignInConfig: Optional[SignInConfigUnion] = None
    AgentConfig: Optional[AgentConfigUnion] = None


class SendOutboundEmailRequest(BaseValidatorModel):
    InstanceId: str
    FromEmailAddress: EmailAddressInfo
    DestinationEmailAddress: EmailAddressInfo
    EmailMessage: OutboundEmailContent
    TrafficType: TrafficTypeType
    AdditionalRecipients: Optional[OutboundAdditionalRecipients] = None
    SourceCampaign: Optional[SourceCampaign] = None
    ClientToken: Optional[str] = None


class StartOutboundEmailContactRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    DestinationEmailAddress: EmailAddressInfo
    EmailMessage: OutboundEmailContent
    FromEmailAddress: Optional[EmailAddressInfo] = None
    AdditionalRecipients: Optional[OutboundAdditionalRecipients] = None
    ClientToken: Optional[str] = None


class SearchCriteria(BaseValidatorModel):
    AgentIds: Optional[Sequence[str]] = None
    AgentHierarchyGroups: Optional[AgentHierarchyGroups] = None
    Channels: Optional[Sequence[ChannelType]] = None
    ContactAnalysis: Optional[ContactAnalysis] = None
    InitiationMethods: Optional[Sequence[ContactInitiationMethodType]] = None
    QueueIds: Optional[Sequence[str]] = None
    SearchableContactAttributes: Optional[SearchableContactAttributes] = None
    SearchableSegmentAttributes: Optional[SearchableSegmentAttributes] = None


class Step(BaseValidatorModel):
    Expiry: Optional[Expiry] = None
    Expression: Optional[ExpressionOutput] = None
    Status: Optional[RoutingCriteriaStepStatusType] = None


class MatchCriteriaUnion(BaseValidatorModel):
    pass


class AttributeCondition(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    ProficiencyLevel: Optional[float] = None
    Range: Optional[Range] = None
    MatchCriteria: Optional[MatchCriteriaUnion] = None
    ComparisonOperator: Optional[str] = None


class SearchAgentStatusesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[AgentStatusSearchFilter] = None
    SearchCriteria: Optional[AgentStatusSearchCriteriaPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchAgentStatusesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[AgentStatusSearchFilter] = None
    SearchCriteria: Optional[AgentStatusSearchCriteria] = None


class SearchUserHierarchyGroupsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[UserHierarchyGroupSearchFilter] = None
    SearchCriteria: Optional[UserHierarchyGroupSearchCriteriaPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchUserHierarchyGroupsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[UserHierarchyGroupSearchFilter] = None
    SearchCriteria: Optional[UserHierarchyGroupSearchCriteria] = None


class StartWebRTCContactResponse(BaseValidatorModel):
    ConnectionData: ConnectionData
    ContactId: str
    ParticipantId: str
    ParticipantToken: str
    ResponseMetadata: ResponseMetadata


class SearchUsersRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[UserSearchFilter] = None
    SearchCriteria: Optional[UserSearchCriteriaPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchUsersRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[UserSearchFilter] = None
    SearchCriteria: Optional[UserSearchCriteria] = None


class EvaluationFormQuestionTypePropertiesOutput(BaseValidatorModel):
    Numeric: Optional[EvaluationFormNumericQuestionPropertiesOutput] = None
    SingleSelect: Optional[EvaluationFormSingleSelectQuestionPropertiesOutput] = None


class EvaluationFormSingleSelectQuestionAutomationUnion(BaseValidatorModel):
    pass


class EvaluationFormSingleSelectQuestionProperties(BaseValidatorModel):
    Options: Sequence[EvaluationFormSingleSelectQuestionOption]
    DisplayAs: Optional[EvaluationFormSingleSelectQuestionDisplayModeType] = None
    Automation: Optional[EvaluationFormSingleSelectQuestionAutomationUnion] = None


class Rule(BaseValidatorModel):
    Name: str
    RuleId: str
    RuleArn: str
    TriggerEventSource: RuleTriggerEventSource
    Function: str
    Actions: List[RuleActionOutput]
    PublishStatus: RulePublishStatusType
    CreatedTime: datetime
    LastUpdatedTime: datetime
    LastUpdatedBy: str
    Tags: Optional[Dict[str, str]] = None


class FieldValueUnionExtra(BaseValidatorModel):
    pass


class CreateCaseActionDefinition(BaseValidatorModel):
    Fields: Sequence[FieldValueUnionExtra]
    TemplateId: str


class UpdateCaseActionDefinition(BaseValidatorModel):
    Fields: Sequence[FieldValueUnionExtra]


class GetMetricDataResponse(BaseValidatorModel):
    MetricResults: List[HistoricalMetricResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class TaskTemplateFieldUnion(BaseValidatorModel):
    pass


class TaskTemplateDefaultsUnion(BaseValidatorModel):
    pass


class TaskTemplateConstraintsUnion(BaseValidatorModel):
    pass


class CreateTaskTemplateRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    Fields: Sequence[TaskTemplateFieldUnion]
    Description: Optional[str] = None
    ContactFlowId: Optional[str] = None
    SelfAssignFlowId: Optional[str] = None
    Constraints: Optional[TaskTemplateConstraintsUnion] = None
    Defaults: Optional[TaskTemplateDefaultsUnion] = None
    Status: Optional[TaskTemplateStatusType] = None
    ClientToken: Optional[str] = None


class UpdateTaskTemplateRequest(BaseValidatorModel):
    TaskTemplateId: str
    InstanceId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ContactFlowId: Optional[str] = None
    SelfAssignFlowId: Optional[str] = None
    Constraints: Optional[TaskTemplateConstraintsUnion] = None
    Defaults: Optional[TaskTemplateDefaultsUnion] = None
    Status: Optional[TaskTemplateStatusType] = None
    Fields: Optional[Sequence[TaskTemplateFieldUnion]] = None


class MetricV2Union(BaseValidatorModel):
    pass


class GetMetricDataV2Request(BaseValidatorModel):
    ResourceArn: str
    StartTime: Timestamp
    EndTime: Timestamp
    Filters: Sequence[FilterV2]
    Metrics: Sequence[MetricV2Union]
    Interval: Optional[IntervalDetails] = None
    Groupings: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetMetricDataV2Response(BaseValidatorModel):
    MetricResults: List[MetricResultV2]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateParticipantRoleConfigRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ChannelConfiguration: UpdateParticipantRoleConfigChannelInfo


class RealTimeContactAnalysisSegmentCategories(BaseValidatorModel):
    MatchedDetails: Dict[str, RealTimeContactAnalysisCategoryDetails]


class SearchContactsTimeRange(BaseValidatorModel):
    pass


class SearchContactsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    TimeRange: SearchContactsTimeRange
    SearchCriteria: Optional[SearchCriteria] = None
    Sort: Optional[Sort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class SearchContactsRequest(BaseValidatorModel):
    InstanceId: str
    TimeRange: SearchContactsTimeRange
    SearchCriteria: Optional[SearchCriteria] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Sort: Optional[Sort] = None


class RoutingCriteria(BaseValidatorModel):
    Steps: Optional[List[Step]] = None
    ActivationTimestamp: Optional[datetime] = None
    Index: Optional[int] = None


class EvaluationFormQuestionOutput(BaseValidatorModel):
    Title: str
    RefId: str
    QuestionType: EvaluationFormQuestionTypeType
    Instructions: Optional[str] = None
    NotApplicableEnabled: Optional[bool] = None
    QuestionTypeProperties: Optional[EvaluationFormQuestionTypePropertiesOutput] = None
    Weight: Optional[float] = None


class DescribeRuleResponse(BaseValidatorModel):
    Rule: Rule
    ResponseMetadata: ResponseMetadata


class RealtimeContactAnalysisSegment(BaseValidatorModel):
    Transcript: Optional[RealTimeContactAnalysisSegmentTranscript] = None
    Categories: Optional[RealTimeContactAnalysisSegmentCategories] = None
    Issues: Optional[RealTimeContactAnalysisSegmentIssues] = None
    Event: Optional[RealTimeContactAnalysisSegmentEvent] = None
    Attachments: Optional[RealTimeContactAnalysisSegmentAttachments] = None
    PostContactSummary: Optional[RealTimeContactAnalysisSegmentPostContactSummary] = None


class EndpointInfo(BaseValidatorModel):
    pass


class Contact(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    InitialContactId: Optional[str] = None
    PreviousContactId: Optional[str] = None
    ContactAssociationId: Optional[str] = None
    InitiationMethod: Optional[ContactInitiationMethodType] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Channel: Optional[ChannelType] = None
    QueueInfo: Optional[QueueInfo] = None
    AgentInfo: Optional[AgentInfo] = None
    InitiationTimestamp: Optional[datetime] = None
    DisconnectTimestamp: Optional[datetime] = None
    LastUpdateTimestamp: Optional[datetime] = None
    LastPausedTimestamp: Optional[datetime] = None
    LastResumedTimestamp: Optional[datetime] = None
    TotalPauseCount: Optional[int] = None
    TotalPauseDurationInSeconds: Optional[int] = None
    ScheduledTimestamp: Optional[datetime] = None
    RelatedContactId: Optional[str] = None
    WisdomInfo: Optional[WisdomInfo] = None
    CustomerId: Optional[str] = None
    CustomerEndpoint: Optional[EndpointInfo] = None
    SystemEndpoint: Optional[EndpointInfo] = None
    QueueTimeAdjustmentSeconds: Optional[int] = None
    QueuePriority: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None
    ConnectedToSystemTimestamp: Optional[datetime] = None
    RoutingCriteria: Optional[RoutingCriteria] = None
    Customer: Optional[Customer] = None
    Campaign: Optional[Campaign] = None
    AnsweringMachineDetectionStatus: Optional[AnsweringMachineDetectionStatusType] = None
    CustomerVoiceActivity: Optional[CustomerVoiceActivity] = None
    QualityMetrics: Optional[QualityMetrics] = None
    DisconnectDetails: Optional[DisconnectDetails] = None
    AdditionalEmailRecipients: Optional[AdditionalEmailRecipients] = None
    SegmentAttributes: Optional[Dict[str, SegmentAttributeValueOutput]] = None


class AttributeConditionUnion(BaseValidatorModel):
    pass


class Expression(BaseValidatorModel):
    AttributeCondition: Optional[AttributeConditionUnion] = None
    AndExpression: Optional[Sequence[Mapping[str, Any]]] = None
    OrExpression: Optional[Sequence[Mapping[str, Any]]] = None
    NotAttributeCondition: Optional[AttributeConditionUnion] = None


class EvaluationFormItemOutput(BaseValidatorModel):
    Section: Optional[EvaluationFormSectionOutput] = None
    Question: Optional[EvaluationFormQuestionOutput] = None


class EvaluationFormSingleSelectQuestionPropertiesUnion(BaseValidatorModel):
    pass


class EvaluationFormNumericQuestionPropertiesUnion(BaseValidatorModel):
    pass


class EvaluationFormQuestionTypeProperties(BaseValidatorModel):
    Numeric: Optional[EvaluationFormNumericQuestionPropertiesUnion] = None
    SingleSelect: Optional[EvaluationFormSingleSelectQuestionPropertiesUnion] = None


class CreateCaseActionDefinitionUnion(BaseValidatorModel):
    pass


class UpdateCaseActionDefinitionUnion(BaseValidatorModel):
    pass


class SendNotificationActionDefinitionUnion(BaseValidatorModel):
    pass


class TaskActionDefinitionUnion(BaseValidatorModel):
    pass


class RuleAction(BaseValidatorModel):
    ActionType: ActionTypeType
    TaskAction: Optional[TaskActionDefinitionUnion] = None
    EventBridgeAction: Optional[EventBridgeActionDefinition] = None
    AssignContactCategoryAction: Optional[Mapping[str, Any]] = None
    SendNotificationAction: Optional[SendNotificationActionDefinitionUnion] = None
    CreateCaseAction: Optional[CreateCaseActionDefinitionUnion] = None
    UpdateCaseAction: Optional[UpdateCaseActionDefinitionUnion] = None
    EndAssociatedTasksAction: Optional[Mapping[str, Any]] = None
    SubmitAutoEvaluationAction: Optional[SubmitAutoEvaluationActionDefinition] = None


class ListRealtimeContactAnalysisSegmentsV2Response(BaseValidatorModel):
    Channel: RealTimeContactAnalysisSupportedChannelType
    Status: RealTimeContactAnalysisStatusType
    Segments: List[RealtimeContactAnalysisSegment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class DescribeContactResponse(BaseValidatorModel):
    Contact: Contact
    ResponseMetadata: ResponseMetadata


class EvaluationFormContent(BaseValidatorModel):
    EvaluationFormVersion: int
    EvaluationFormId: str
    EvaluationFormArn: str
    Title: str
    Items: List[EvaluationFormItemOutput]
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategy] = None


class EvaluationForm(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormVersion: int
    Locked: bool
    EvaluationFormArn: str
    Title: str
    Status: EvaluationFormVersionStatusType
    Items: List[EvaluationFormItemOutput]
    CreatedTime: datetime
    CreatedBy: str
    LastModifiedTime: datetime
    LastModifiedBy: str
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategy] = None
    Tags: Optional[Dict[str, str]] = None


class ExpressionUnion(BaseValidatorModel):
    pass


class RoutingCriteriaInputStep(BaseValidatorModel):
    Expiry: Optional[RoutingCriteriaInputStepExpiry] = None
    Expression: Optional[ExpressionUnion] = None


class DescribeContactEvaluationResponse(BaseValidatorModel):
    Evaluation: Evaluation
    EvaluationForm: EvaluationFormContent
    ResponseMetadata: ResponseMetadata


class DescribeEvaluationFormResponse(BaseValidatorModel):
    EvaluationForm: EvaluationForm
    ResponseMetadata: ResponseMetadata


class EvaluationFormQuestionTypePropertiesUnion(BaseValidatorModel):
    pass


class EvaluationFormQuestion(BaseValidatorModel):
    Title: str
    RefId: str
    QuestionType: EvaluationFormQuestionTypeType
    Instructions: Optional[str] = None
    NotApplicableEnabled: Optional[bool] = None
    QuestionTypeProperties: Optional[EvaluationFormQuestionTypePropertiesUnion] = None
    Weight: Optional[float] = None


class RuleActionUnion(BaseValidatorModel):
    pass


class CreateRuleRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    TriggerEventSource: RuleTriggerEventSource
    Function: str
    Actions: Sequence[RuleActionUnion]
    PublishStatus: RulePublishStatusType
    ClientToken: Optional[str] = None


class UpdateRuleRequest(BaseValidatorModel):
    RuleId: str
    InstanceId: str
    Name: str
    Function: str
    Actions: Sequence[RuleActionUnion]
    PublishStatus: RulePublishStatusType


class RoutingCriteriaInput(BaseValidatorModel):
    Steps: Optional[Sequence[RoutingCriteriaInputStep]] = None


class UpdateContactRoutingDataRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    QueueTimeAdjustmentSeconds: Optional[int] = None
    QueuePriority: Optional[int] = None
    RoutingCriteria: Optional[RoutingCriteriaInput] = None


class EvaluationFormQuestionUnion(BaseValidatorModel):
    pass


class EvaluationFormSectionUnion(BaseValidatorModel):
    pass


class EvaluationFormItem(BaseValidatorModel):
    Section: Optional[EvaluationFormSectionUnion] = None
    Question: Optional[EvaluationFormQuestionUnion] = None


class EvaluationFormItemUnion(BaseValidatorModel):
    pass


class CreateEvaluationFormRequest(BaseValidatorModel):
    InstanceId: str
    Title: str
    Items: Sequence[EvaluationFormItemUnion]
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategy] = None
    ClientToken: Optional[str] = None


class UpdateEvaluationFormRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int
    Title: str
    Items: Sequence[EvaluationFormItemUnion]
    CreateNewVersion: Optional[bool] = None
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategy] = None
    ClientToken: Optional[str] = None


