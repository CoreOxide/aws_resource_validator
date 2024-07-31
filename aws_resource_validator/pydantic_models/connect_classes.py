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
from aws_resource_validator.pydantic_models.connect_constants import *

class ActionSummaryTypeDef(BaseModel):
    ActionType: ActionTypeType

class ActivateEvaluationFormRequestRequestTypeDef(BaseModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DistributionTypeDef(BaseModel):
    Region: str
    Percentage: int

class QueueReferenceTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None

class AgentHierarchyGroupTypeDef(BaseModel):
    Arn: Optional[str] = None

class AgentHierarchyGroupsTypeDef(BaseModel):
    L1Ids: Optional[Sequence[str]] = None
    L2Ids: Optional[Sequence[str]] = None
    L3Ids: Optional[Sequence[str]] = None
    L4Ids: Optional[Sequence[str]] = None
    L5Ids: Optional[Sequence[str]] = None

class DeviceInfoTypeDef(BaseModel):
    PlatformName: Optional[str] = None
    PlatformVersion: Optional[str] = None
    OperatingSystem: Optional[str] = None

class ParticipantCapabilitiesTypeDef(BaseModel):
    Video: Optional[Literal["SEND"]] = None

class AudioQualityMetricsInfoTypeDef(BaseModel):
    QualityScore: Optional[float] = None
    PotentialQualityIssues: Optional[List[str]] = None

class AgentStatusReferenceTypeDef(BaseModel):
    StatusStartTimestamp: Optional[datetime] = None
    StatusArn: Optional[str] = None
    StatusName: Optional[str] = None

class AgentStatusSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[AgentStatusTypeType] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class AgentStatusTypeDef(BaseModel):
    AgentStatusARN: Optional[str] = None
    AgentStatusId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Type: Optional[AgentStatusTypeType] = None
    DisplayOrder: Optional[int] = None
    State: Optional[AgentStatusStateType] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class AgentsCriteriaTypeDef(BaseModel):
    AgentIds: Optional[List[str]] = None

class AnalyticsDataAssociationResultTypeDef(BaseModel):
    DataSetId: Optional[str] = None
    TargetAccountId: Optional[str] = None
    ResourceShareId: Optional[str] = None
    ResourceShareArn: Optional[str] = None

class AnswerMachineDetectionConfigTypeDef(BaseModel):
    EnableAnswerMachineDetection: Optional[bool] = None
    AwaitAnswerMachinePrompt: Optional[bool] = None

class ApplicationExtraOutputTypeDef(BaseModel):
    Namespace: Optional[str] = None
    ApplicationPermissions: Optional[List[str]] = None

class ApplicationOutputTypeDef(BaseModel):
    Namespace: Optional[str] = None
    ApplicationPermissions: Optional[List[str]] = None

class ApplicationTypeDef(BaseModel):
    Namespace: Optional[str] = None
    ApplicationPermissions: Optional[Sequence[str]] = None

class AssociateAnalyticsDataSetRequestRequestTypeDef(BaseModel):
    InstanceId: str
    DataSetId: str
    TargetAccountId: Optional[str] = None

class AssociateApprovedOriginRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Origin: str

class LexBotTypeDef(BaseModel):
    Name: str
    LexRegion: str

class LexV2BotTypeDef(BaseModel):
    AliasArn: Optional[str] = None

class AssociateDefaultVocabularyRequestRequestTypeDef(BaseModel):
    InstanceId: str
    LanguageCode: VocabularyLanguageCodeType
    VocabularyId: Optional[str] = None

class AssociateFlowRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ResourceId: str
    FlowId: str
    ResourceType: Literal["SMS_PHONE_NUMBER"]

class AssociateLambdaFunctionRequestRequestTypeDef(BaseModel):
    InstanceId: str
    FunctionArn: str

class AssociatePhoneNumberContactFlowRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str
    InstanceId: str
    ContactFlowId: str

class AssociateQueueQuickConnectsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QueueId: str
    QuickConnectIds: Sequence[str]

class AssociateSecurityKeyRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Key: str

class AssociateTrafficDistributionGroupUserRequestRequestTypeDef(BaseModel):
    TrafficDistributionGroupId: str
    UserId: str
    InstanceId: str

class UserProficiencyTypeDef(BaseModel):
    AttributeName: str
    AttributeValue: str
    Level: float

class AttachedFileErrorTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    FileId: Optional[str] = None

class CreatedByInfoTypeDef(BaseModel):
    ConnectUserArn: Optional[str] = None
    AWSIdentityArn: Optional[str] = None

class AttachmentReferenceTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    Status: Optional[ReferenceStatusType] = None

class AttendeeTypeDef(BaseModel):
    AttendeeId: Optional[str] = None
    JoinToken: Optional[str] = None

class HierarchyGroupConditionTypeDef(BaseModel):
    Value: Optional[str] = None
    HierarchyGroupMatchType: Optional[HierarchyGroupMatchTypeType] = None

class TagConditionTypeDef(BaseModel):
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None

class AttributeTypeDef(BaseModel):
    AttributeType: Optional[InstanceAttributeTypeType] = None
    Value: Optional[str] = None

class AudioFeaturesTypeDef(BaseModel):
    EchoReduction: Optional[MeetingFeatureStatusType] = None

class AuthenticationProfileSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    IsDefault: Optional[bool] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class AuthenticationProfileTypeDef(BaseModel):
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

class AvailableNumberSummaryTypeDef(BaseModel):
    PhoneNumber: Optional[str] = None
    PhoneNumberCountryCode: Optional[PhoneNumberCountryCodeType] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None

class BatchAssociateAnalyticsDataSetRequestRequestTypeDef(BaseModel):
    InstanceId: str
    DataSetIds: Sequence[str]
    TargetAccountId: Optional[str] = None

class ErrorResultTypeDef(BaseModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class BatchDisassociateAnalyticsDataSetRequestRequestTypeDef(BaseModel):
    InstanceId: str
    DataSetIds: Sequence[str]
    TargetAccountId: Optional[str] = None

class BatchGetAttachedFileMetadataRequestRequestTypeDef(BaseModel):
    FileIds: Sequence[str]
    InstanceId: str
    AssociatedResourceArn: str

class BatchGetFlowAssociationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ResourceIds: Sequence[str]
    ResourceType: Optional[Literal["VOICE_PHONE_NUMBER"]] = None

class FlowAssociationSummaryTypeDef(BaseModel):
    ResourceId: Optional[str] = None
    FlowId: Optional[str] = None
    ResourceType: Optional[Literal["VOICE_PHONE_NUMBER"]] = None

class FailedRequestTypeDef(BaseModel):
    RequestIdentifier: Optional[str] = None
    FailureReasonCode: Optional[FailureReasonCodeType] = None
    FailureReasonMessage: Optional[str] = None

class SuccessfulRequestTypeDef(BaseModel):
    RequestIdentifier: Optional[str] = None
    ContactId: Optional[str] = None

class CampaignTypeDef(BaseModel):
    CampaignId: Optional[str] = None

class ChatEventTypeDef(BaseModel):
    Type: ChatEventTypeType
    ContentType: Optional[str] = None
    Content: Optional[str] = None

class ChatMessageTypeDef(BaseModel):
    ContentType: str
    Content: str

class ChatStreamingConfigurationTypeDef(BaseModel):
    StreamingEndpointArn: str

class ClaimPhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumber: str
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberDescription: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None

class PhoneNumberStatusTypeDef(BaseModel):
    Status: Optional[PhoneNumberWorkflowStatusType] = None
    Message: Optional[str] = None

class CompleteAttachedFileUploadRequestRequestTypeDef(BaseModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str

class EndpointTypeDef(BaseModel):
    Type: Optional[EndpointTypeType] = None
    Address: Optional[str] = None

class ContactFilterTypeDef(BaseModel):
    ContactStates: Optional[Sequence[ContactStateType]] = None

class StringConditionTypeDef(BaseModel):
    FieldName: Optional[str] = None
    Value: Optional[str] = None
    ComparisonType: Optional[StringComparisonTypeType] = None

class ContactFlowModuleSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[ContactFlowModuleStateType] = None

class ContactFlowModuleTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Content: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[ContactFlowModuleStateType] = None
    Status: Optional[ContactFlowModuleStatusType] = None
    Tags: Optional[Dict[str, str]] = None

class ContactFlowSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ContactFlowType: Optional[ContactFlowTypeType] = None
    ContactFlowState: Optional[ContactFlowStateType] = None
    ContactFlowStatus: Optional[ContactFlowStatusType] = None

class ContactFlowTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ContactFlowTypeType] = None
    State: Optional[ContactFlowStateType] = None
    Status: Optional[ContactFlowStatusType] = None
    Description: Optional[str] = None
    Content: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ContactSearchSummaryAgentInfoTypeDef(BaseModel):
    Id: Optional[str] = None
    ConnectedToAgentTimestamp: Optional[datetime] = None

class ContactSearchSummaryQueueInfoTypeDef(BaseModel):
    Id: Optional[str] = None
    EnqueueTimestamp: Optional[datetime] = None

class CustomerVoiceActivityTypeDef(BaseModel):
    GreetingStartTimestamp: Optional[datetime] = None
    GreetingEndTimestamp: Optional[datetime] = None

class DisconnectDetailsTypeDef(BaseModel):
    PotentialDisconnectIssue: Optional[str] = None

class QueueInfoTypeDef(BaseModel):
    Id: Optional[str] = None
    EnqueueTimestamp: Optional[datetime] = None

class SegmentAttributeValueTypeDef(BaseModel):
    ValueString: Optional[str] = None

class WisdomInfoTypeDef(BaseModel):
    SessionArn: Optional[str] = None

class CreateAgentStatusRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    State: AgentStatusStateType
    Description: Optional[str] = None
    DisplayOrder: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateContactFlowModuleRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    Content: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None

class CreateContactFlowRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    Type: ContactFlowTypeType
    Content: str
    Description: Optional[str] = None
    Status: Optional[ContactFlowStatusType] = None
    Tags: Optional[Mapping[str, str]] = None

class EvaluationFormScoringStrategyTypeDef(BaseModel):
    Mode: EvaluationFormScoringModeType
    Status: EvaluationFormScoringStatusType

class CreateInstanceRequestRequestTypeDef(BaseModel):
    IdentityManagementType: DirectoryTypeType
    InboundCallsEnabled: bool
    OutboundCallsEnabled: bool
    ClientToken: Optional[str] = None
    InstanceAlias: Optional[str] = None
    DirectoryId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateIntegrationAssociationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    IntegrationType: IntegrationTypeType
    IntegrationArn: str
    SourceApplicationUrl: Optional[str] = None
    SourceApplicationName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Tags: Optional[Mapping[str, str]] = None

class ParticipantDetailsToAddTypeDef(BaseModel):
    ParticipantRole: Optional[ParticipantRoleType] = None
    DisplayName: Optional[str] = None

class ParticipantTokenCredentialsTypeDef(BaseModel):
    ParticipantToken: Optional[str] = None
    Expiry: Optional[str] = None

class CreatePersistentContactAssociationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    InitialContactId: str
    RehydrationType: RehydrationTypeType
    SourceContactId: str
    ClientToken: Optional[str] = None

class PredefinedAttributeValuesTypeDef(BaseModel):
    StringList: Optional[Sequence[str]] = None

class CreatePromptRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    S3Uri: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class OutboundCallerConfigTypeDef(BaseModel):
    OutboundCallerIdName: Optional[str] = None
    OutboundCallerIdNumberId: Optional[str] = None
    OutboundFlowId: Optional[str] = None

class RuleTriggerEventSourceTypeDef(BaseModel):
    EventSourceName: EventSourceNameType
    IntegrationAssociationId: Optional[str] = None

class CreateTrafficDistributionGroupRequestRequestTypeDef(BaseModel):
    Name: str
    InstanceId: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateUseCaseRequestRequestTypeDef(BaseModel):
    InstanceId: str
    IntegrationAssociationId: str
    UseCaseType: UseCaseTypeType
    Tags: Optional[Mapping[str, str]] = None

class CreateUserHierarchyGroupRequestRequestTypeDef(BaseModel):
    Name: str
    InstanceId: str
    ParentGroupId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UserIdentityInfoTypeDef(BaseModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Email: Optional[str] = None
    SecondaryEmail: Optional[str] = None
    Mobile: Optional[str] = None

class UserPhoneConfigTypeDef(BaseModel):
    PhoneType: PhoneTypeType
    AutoAccept: Optional[bool] = None
    AfterContactWorkTimeLimit: Optional[int] = None
    DeskPhoneNumber: Optional[str] = None

class ViewInputContentTypeDef(BaseModel):
    Template: Optional[str] = None
    Actions: Optional[Sequence[str]] = None

class CreateViewVersionRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ViewId: str
    VersionDescription: Optional[str] = None
    ViewContentSha256: Optional[str] = None

class CreateVocabularyRequestRequestTypeDef(BaseModel):
    InstanceId: str
    VocabularyName: str
    LanguageCode: VocabularyLanguageCodeType
    Content: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CredentialsTypeDef(BaseModel):
    AccessToken: Optional[str] = None
    AccessTokenExpiration: Optional[datetime] = None
    RefreshToken: Optional[str] = None
    RefreshTokenExpiration: Optional[datetime] = None

class CrossChannelBehaviorTypeDef(BaseModel):
    BehaviorType: BehaviorTypeType

class CurrentMetricTypeDef(BaseModel):
    Name: Optional[CurrentMetricNameType] = None
    Unit: Optional[UnitType] = None

class CurrentMetricSortCriteriaTypeDef(BaseModel):
    SortByMetric: Optional[CurrentMetricNameType] = None
    SortOrder: Optional[SortOrderType] = None

class DateReferenceTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class DeactivateEvaluationFormRequestRequestTypeDef(BaseModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int

class DefaultVocabularyTypeDef(BaseModel):
    InstanceId: str
    LanguageCode: VocabularyLanguageCodeType
    VocabularyId: str
    VocabularyName: str

class DeleteAttachedFileRequestRequestTypeDef(BaseModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str

class DeleteContactEvaluationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    EvaluationId: str

class DeleteContactFlowModuleRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactFlowModuleId: str

class DeleteContactFlowRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactFlowId: str

class DeleteEvaluationFormRequestRequestTypeDef(BaseModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: Optional[int] = None

class DeleteHoursOfOperationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    HoursOfOperationId: str

class DeleteInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str

class DeleteIntegrationAssociationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    IntegrationAssociationId: str

class DeletePredefinedAttributeRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str

class DeletePromptRequestRequestTypeDef(BaseModel):
    InstanceId: str
    PromptId: str

class DeleteQueueRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QueueId: str

class DeleteQuickConnectRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QuickConnectId: str

class DeleteRoutingProfileRequestRequestTypeDef(BaseModel):
    InstanceId: str
    RoutingProfileId: str

class DeleteRuleRequestRequestTypeDef(BaseModel):
    InstanceId: str
    RuleId: str

class DeleteSecurityProfileRequestRequestTypeDef(BaseModel):
    InstanceId: str
    SecurityProfileId: str

class DeleteTaskTemplateRequestRequestTypeDef(BaseModel):
    InstanceId: str
    TaskTemplateId: str

class DeleteTrafficDistributionGroupRequestRequestTypeDef(BaseModel):
    TrafficDistributionGroupId: str

class DeleteUseCaseRequestRequestTypeDef(BaseModel):
    InstanceId: str
    IntegrationAssociationId: str
    UseCaseId: str

class DeleteUserHierarchyGroupRequestRequestTypeDef(BaseModel):
    HierarchyGroupId: str
    InstanceId: str

class DeleteUserRequestRequestTypeDef(BaseModel):
    InstanceId: str
    UserId: str

class DeleteViewRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ViewId: str

class DeleteViewVersionRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ViewId: str
    ViewVersion: int

class DeleteVocabularyRequestRequestTypeDef(BaseModel):
    InstanceId: str
    VocabularyId: str

class DescribeAgentStatusRequestRequestTypeDef(BaseModel):
    InstanceId: str
    AgentStatusId: str

class DescribeAuthenticationProfileRequestRequestTypeDef(BaseModel):
    AuthenticationProfileId: str
    InstanceId: str

class DescribeContactEvaluationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    EvaluationId: str

class DescribeContactFlowModuleRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactFlowModuleId: str

class DescribeContactFlowRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactFlowId: str

class DescribeContactRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str

class DescribeEvaluationFormRequestRequestTypeDef(BaseModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: Optional[int] = None

class DescribeHoursOfOperationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    HoursOfOperationId: str

class DescribeInstanceAttributeRequestRequestTypeDef(BaseModel):
    InstanceId: str
    AttributeType: InstanceAttributeTypeType

class DescribeInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str

class DescribeInstanceStorageConfigRequestRequestTypeDef(BaseModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType

class DescribePhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str

class DescribePredefinedAttributeRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str

class DescribePromptRequestRequestTypeDef(BaseModel):
    InstanceId: str
    PromptId: str

class PromptTypeDef(BaseModel):
    PromptARN: Optional[str] = None
    PromptId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class DescribeQueueRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QueueId: str

class DescribeQuickConnectRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QuickConnectId: str

class DescribeRoutingProfileRequestRequestTypeDef(BaseModel):
    InstanceId: str
    RoutingProfileId: str

class DescribeRuleRequestRequestTypeDef(BaseModel):
    InstanceId: str
    RuleId: str

class DescribeSecurityProfileRequestRequestTypeDef(BaseModel):
    SecurityProfileId: str
    InstanceId: str

class SecurityProfileTypeDef(BaseModel):
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

class DescribeTrafficDistributionGroupRequestRequestTypeDef(BaseModel):
    TrafficDistributionGroupId: str

class TrafficDistributionGroupTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    InstanceArn: Optional[str] = None
    Status: Optional[TrafficDistributionGroupStatusType] = None
    Tags: Optional[Dict[str, str]] = None
    IsDefault: Optional[bool] = None

class DescribeUserHierarchyGroupRequestRequestTypeDef(BaseModel):
    HierarchyGroupId: str
    InstanceId: str

class DescribeUserHierarchyStructureRequestRequestTypeDef(BaseModel):
    InstanceId: str

class DescribeUserRequestRequestTypeDef(BaseModel):
    UserId: str
    InstanceId: str

class DescribeViewRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ViewId: str

class DescribeVocabularyRequestRequestTypeDef(BaseModel):
    InstanceId: str
    VocabularyId: str

class VocabularyTypeDef(BaseModel):
    Name: str
    Id: str
    Arn: str
    LanguageCode: VocabularyLanguageCodeType
    State: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: Optional[str] = None
    Content: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class RoutingProfileReferenceTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None

class DisassociateAnalyticsDataSetRequestRequestTypeDef(BaseModel):
    InstanceId: str
    DataSetId: str
    TargetAccountId: Optional[str] = None

class DisassociateApprovedOriginRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Origin: str

class DisassociateFlowRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ResourceId: str
    ResourceType: Literal["SMS_PHONE_NUMBER"]

class DisassociateInstanceStorageConfigRequestRequestTypeDef(BaseModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType

class DisassociateLambdaFunctionRequestRequestTypeDef(BaseModel):
    InstanceId: str
    FunctionArn: str

class DisassociateLexBotRequestRequestTypeDef(BaseModel):
    InstanceId: str
    BotName: str
    LexRegion: str

class DisassociatePhoneNumberContactFlowRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str
    InstanceId: str

class DisassociateQueueQuickConnectsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QueueId: str
    QuickConnectIds: Sequence[str]

class RoutingProfileQueueReferenceTypeDef(BaseModel):
    QueueId: str
    Channel: ChannelType

class DisassociateSecurityKeyRequestRequestTypeDef(BaseModel):
    InstanceId: str
    AssociationId: str

class DisassociateTrafficDistributionGroupUserRequestRequestTypeDef(BaseModel):
    TrafficDistributionGroupId: str
    UserId: str
    InstanceId: str

class UserProficiencyDisassociateTypeDef(BaseModel):
    AttributeName: str
    AttributeValue: str

class DisconnectReasonTypeDef(BaseModel):
    Code: Optional[str] = None

class DismissUserContactRequestRequestTypeDef(BaseModel):
    UserId: str
    InstanceId: str
    ContactId: str

class DownloadUrlMetadataTypeDef(BaseModel):
    Url: Optional[str] = None
    UrlExpiry: Optional[str] = None

class EmailReferenceTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class EncryptionConfigTypeDef(BaseModel):
    EncryptionType: Literal["KMS"]
    KeyId: str

class EvaluationAnswerDataTypeDef(BaseModel):
    StringValue: Optional[str] = None
    NumericValue: Optional[float] = None
    NotApplicable: Optional[bool] = None

class NumericQuestionPropertyValueAutomationTypeDef(BaseModel):
    Label: NumericQuestionPropertyAutomationLabelType

class EvaluationFormNumericQuestionOptionTypeDef(BaseModel):
    MinValue: int
    MaxValue: int
    Score: Optional[int] = None
    AutomaticFail: Optional[bool] = None

class EvaluationFormSectionOutputTypeDef(BaseModel):
    Title: str
    RefId: str
    Items: List["EvaluationFormItemOutputTypeDef"]
    Instructions: Optional[str] = None
    Weight: Optional[float] = None

class EvaluationFormSectionTypeDef(BaseModel):
    Title: str
    RefId: str
    Items: Sequence["EvaluationFormItemTypeDef"]
    Instructions: Optional[str] = None
    Weight: Optional[float] = None

class SingleSelectQuestionRuleCategoryAutomationTypeDef(BaseModel):
    Category: str
    Condition: SingleSelectQuestionRuleCategoryAutomationConditionType
    OptionRefId: str

class EvaluationFormSingleSelectQuestionOptionTypeDef(BaseModel):
    RefId: str
    Text: str
    Score: Optional[int] = None
    AutomaticFail: Optional[bool] = None

class EvaluationFormSummaryTypeDef(BaseModel):
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

class EvaluationFormVersionSummaryTypeDef(BaseModel):
    EvaluationFormArn: str
    EvaluationFormId: str
    EvaluationFormVersion: int
    Locked: bool
    Status: EvaluationFormVersionStatusType
    CreatedTime: datetime
    CreatedBy: str
    LastModifiedTime: datetime
    LastModifiedBy: str

class EvaluationScoreTypeDef(BaseModel):
    Percentage: Optional[float] = None
    NotApplicable: Optional[bool] = None
    AutomaticFail: Optional[bool] = None

class EvaluationNoteTypeDef(BaseModel):
    Value: Optional[str] = None

class EventBridgeActionDefinitionTypeDef(BaseModel):
    Name: str

class ExpiryTypeDef(BaseModel):
    DurationInSeconds: Optional[int] = None
    ExpiryTimestamp: Optional[datetime] = None

class FieldValueUnionOutputTypeDef(BaseModel):
    BooleanValue: Optional[bool] = None
    DoubleValue: Optional[float] = None
    EmptyValue: Optional[Dict[str, Any]] = None
    StringValue: Optional[str] = None

class FieldValueUnionTypeDef(BaseModel):
    BooleanValue: Optional[bool] = None
    DoubleValue: Optional[float] = None
    EmptyValue: Optional[Mapping[str, Any]] = None
    StringValue: Optional[str] = None

class FilterV2TypeDef(BaseModel):
    FilterKey: Optional[str] = None
    FilterValues: Optional[Sequence[str]] = None

class FiltersTypeDef(BaseModel):
    Queues: Optional[Sequence[str]] = None
    Channels: Optional[Sequence[ChannelType]] = None
    RoutingProfiles: Optional[Sequence[str]] = None
    RoutingStepExpressions: Optional[Sequence[str]] = None

class GetAttachedFileRequestRequestTypeDef(BaseModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str
    UrlExpiryInSeconds: Optional[int] = None

class GetContactAttributesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    InitialContactId: str

class GetFederationTokenRequestRequestTypeDef(BaseModel):
    InstanceId: str

class GetFlowAssociationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ResourceId: str
    ResourceType: Literal["SMS_PHONE_NUMBER"]

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class IntervalDetailsTypeDef(BaseModel):
    TimeZone: Optional[str] = None
    IntervalPeriod: Optional[IntervalPeriodType] = None

class GetPromptFileRequestRequestTypeDef(BaseModel):
    InstanceId: str
    PromptId: str

class GetTaskTemplateRequestRequestTypeDef(BaseModel):
    InstanceId: str
    TaskTemplateId: str
    SnapshotVersion: Optional[str] = None

class GetTrafficDistributionRequestRequestTypeDef(BaseModel):
    Id: str

class HierarchyGroupSummaryReferenceTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None

class HierarchyGroupSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class HierarchyLevelTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class HierarchyLevelUpdateTypeDef(BaseModel):
    Name: str

class ThresholdTypeDef(BaseModel):
    Comparison: Optional[Literal["LT"]] = None
    ThresholdValue: Optional[float] = None

class HoursOfOperationTimeSliceTypeDef(BaseModel):
    Hours: int
    Minutes: int

class HoursOfOperationSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ImportPhoneNumberRequestRequestTypeDef(BaseModel):
    InstanceId: str
    SourcePhoneNumberArn: str
    PhoneNumberDescription: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None

class InstanceStatusReasonTypeDef(BaseModel):
    Message: Optional[str] = None

class KinesisFirehoseConfigTypeDef(BaseModel):
    FirehoseArn: str

class KinesisStreamConfigTypeDef(BaseModel):
    StreamArn: str

class InstanceSummaryTypeDef(BaseModel):
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

class IntegrationAssociationSummaryTypeDef(BaseModel):
    IntegrationAssociationId: Optional[str] = None
    IntegrationAssociationArn: Optional[str] = None
    InstanceId: Optional[str] = None
    IntegrationType: Optional[IntegrationTypeType] = None
    IntegrationArn: Optional[str] = None
    SourceApplicationUrl: Optional[str] = None
    SourceApplicationName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None

class TaskTemplateFieldIdentifierTypeDef(BaseModel):
    Name: Optional[str] = None

class ListAgentStatusRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AgentStatusTypes: Optional[Sequence[AgentStatusTypeType]] = None

class ListAnalyticsDataAssociationsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    DataSetId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListApprovedOriginsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAuthenticationProfilesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListBotsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    LexVersion: LexVersionType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListContactEvaluationsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    NextToken: Optional[str] = None

class ListContactFlowModulesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ContactFlowModuleState: Optional[ContactFlowModuleStateType] = None

class ListContactFlowsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactFlowTypes: Optional[Sequence[ContactFlowTypeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListContactReferencesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    ReferenceTypes: Sequence[ReferenceTypeType]
    NextToken: Optional[str] = None

class ListDefaultVocabulariesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    LanguageCode: Optional[VocabularyLanguageCodeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListEvaluationFormVersionsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    EvaluationFormId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListEvaluationFormsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFlowAssociationsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ResourceType: Optional[Literal["VOICE_PHONE_NUMBER"]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListHoursOfOperationsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListInstanceAttributesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListInstanceStorageConfigsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListInstancesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIntegrationAssociationsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    IntegrationType: Optional[IntegrationTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IntegrationArn: Optional[str] = None

class ListLambdaFunctionsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListLexBotsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPhoneNumbersRequestRequestTypeDef(BaseModel):
    InstanceId: str
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PhoneNumberSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    PhoneNumberCountryCode: Optional[PhoneNumberCountryCodeType] = None

class ListPhoneNumbersSummaryTypeDef(BaseModel):
    PhoneNumberId: Optional[str] = None
    PhoneNumberArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    PhoneNumberCountryCode: Optional[PhoneNumberCountryCodeType] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberDescription: Optional[str] = None
    SourcePhoneNumberArn: Optional[str] = None

class ListPhoneNumbersV2RequestRequestTypeDef(BaseModel):
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberPrefix: Optional[str] = None

class ListPredefinedAttributesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PredefinedAttributeSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListPromptsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PromptSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListQueueQuickConnectsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QueueId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class QuickConnectSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    QuickConnectType: Optional[QuickConnectTypeType] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListQueuesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QueueTypes: Optional[Sequence[QueueTypeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class QueueSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    QueueType: Optional[QueueTypeType] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListQuickConnectsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuickConnectTypes: Optional[Sequence[QuickConnectTypeType]] = None

class ListRealtimeContactAnalysisSegmentsV2RequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    OutputType: RealTimeContactAnalysisOutputTypeType
    SegmentTypes: Sequence[RealTimeContactAnalysisSegmentTypeType]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRoutingProfileQueuesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    RoutingProfileId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RoutingProfileQueueConfigSummaryTypeDef(BaseModel):
    QueueId: str
    QueueArn: str
    QueueName: str
    Priority: int
    Delay: int
    Channel: ChannelType

class ListRoutingProfilesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RoutingProfileSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListRulesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    PublishStatus: Optional[RulePublishStatusType] = None
    EventSourceName: Optional[EventSourceNameType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSecurityKeysRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SecurityKeyTypeDef(BaseModel):
    AssociationId: Optional[str] = None
    Key: Optional[str] = None
    CreationTime: Optional[datetime] = None

class ListSecurityProfileApplicationsRequestRequestTypeDef(BaseModel):
    SecurityProfileId: str
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListSecurityProfilePermissionsRequestRequestTypeDef(BaseModel):
    SecurityProfileId: str
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListSecurityProfilesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SecurityProfileSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class ListTaskTemplatesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[TaskTemplateStatusType] = None
    Name: Optional[str] = None

class TaskTemplateMetadataTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[TaskTemplateStatusType] = None
    LastModifiedTime: Optional[datetime] = None
    CreatedTime: Optional[datetime] = None

class ListTrafficDistributionGroupUsersRequestRequestTypeDef(BaseModel):
    TrafficDistributionGroupId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class TrafficDistributionGroupUserSummaryTypeDef(BaseModel):
    UserId: Optional[str] = None

class ListTrafficDistributionGroupsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    InstanceId: Optional[str] = None

class TrafficDistributionGroupSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    InstanceArn: Optional[str] = None
    Status: Optional[TrafficDistributionGroupStatusType] = None
    IsDefault: Optional[bool] = None

class ListUseCasesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    IntegrationAssociationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class UseCaseTypeDef(BaseModel):
    UseCaseId: Optional[str] = None
    UseCaseArn: Optional[str] = None
    UseCaseType: Optional[UseCaseTypeType] = None

class ListUserHierarchyGroupsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListUserProficienciesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    UserId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListUsersRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class UserSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Username: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListViewVersionsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ViewId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ViewVersionSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ViewTypeType] = None
    Version: Optional[int] = None
    VersionDescription: Optional[str] = None

class ListViewsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Type: Optional[ViewTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ViewSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ViewTypeType] = None
    Status: Optional[ViewStatusType] = None
    Description: Optional[str] = None

class MediaPlacementTypeDef(BaseModel):
    AudioHostUrl: Optional[str] = None
    AudioFallbackUrl: Optional[str] = None
    SignalingUrl: Optional[str] = None
    TurnControlUrl: Optional[str] = None
    EventIngestionUrl: Optional[str] = None

class MetricFilterV2OutputTypeDef(BaseModel):
    MetricFilterKey: Optional[str] = None
    MetricFilterValues: Optional[List[str]] = None
    Negate: Optional[bool] = None

class MetricFilterV2TypeDef(BaseModel):
    MetricFilterKey: Optional[str] = None
    MetricFilterValues: Optional[Sequence[str]] = None
    Negate: Optional[bool] = None

class MetricIntervalTypeDef(BaseModel):
    Interval: Optional[IntervalPeriodType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class ThresholdV2TypeDef(BaseModel):
    Comparison: Optional[str] = None
    ThresholdValue: Optional[float] = None

class MonitorContactRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    UserId: str
    AllowedMonitorCapabilities: Optional[Sequence[MonitorCapabilityType]] = None
    ClientToken: Optional[str] = None

class ParticipantDetailsTypeDef(BaseModel):
    DisplayName: str

class NotificationRecipientTypeOutputTypeDef(BaseModel):
    UserTags: Optional[Dict[str, str]] = None
    UserIds: Optional[List[str]] = None

class NotificationRecipientTypeTypeDef(BaseModel):
    UserTags: Optional[Mapping[str, str]] = None
    UserIds: Optional[Sequence[str]] = None

class NumberReferenceTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class ParticipantTimerValueTypeDef(BaseModel):
    ParticipantTimerAction: Optional[Literal["Unset"]] = None
    ParticipantTimerDurationInMinutes: Optional[int] = None

class PauseContactRequestRequestTypeDef(BaseModel):
    ContactId: str
    InstanceId: str
    ContactFlowId: Optional[str] = None

class PersistentChatTypeDef(BaseModel):
    RehydrationType: Optional[RehydrationTypeType] = None
    SourceContactId: Optional[str] = None

class PhoneNumberQuickConnectConfigTypeDef(BaseModel):
    PhoneNumber: str

class PredefinedAttributeValuesOutputTypeDef(BaseModel):
    StringList: Optional[List[str]] = None

class PredefinedAttributeValuesExtraOutputTypeDef(BaseModel):
    StringList: Optional[List[str]] = None

class PutUserStatusRequestRequestTypeDef(BaseModel):
    UserId: str
    InstanceId: str
    AgentStatusId: str

class QueueQuickConnectConfigTypeDef(BaseModel):
    QueueId: str
    ContactFlowId: str

class UserQuickConnectConfigTypeDef(BaseModel):
    UserId: str
    ContactFlowId: str

class RealTimeContactAnalysisAttachmentTypeDef(BaseModel):
    AttachmentName: str
    AttachmentId: str
    ContentType: Optional[str] = None
    Status: Optional[ArtifactStatusType] = None

class RealTimeContactAnalysisCharacterIntervalTypeDef(BaseModel):
    BeginOffsetChar: int
    EndOffsetChar: int

class RealTimeContactAnalysisTimeDataTypeDef(BaseModel):
    AbsoluteTime: Optional[datetime] = None

class StringReferenceTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class UrlReferenceTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class ReferenceTypeDef(BaseModel):
    Value: str
    Type: ReferenceTypeType

class ReleasePhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str
    ClientToken: Optional[str] = None

class ReplicateInstanceRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ReplicaRegion: str
    ReplicaAlias: str
    ClientToken: Optional[str] = None

class TagSearchConditionTypeDef(BaseModel):
    tagKey: Optional[str] = None
    tagValue: Optional[str] = None
    tagKeyComparisonType: Optional[StringComparisonTypeType] = None
    tagValueComparisonType: Optional[StringComparisonTypeType] = None

class ResumeContactRecordingRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str

class ResumeContactRequestRequestTypeDef(BaseModel):
    ContactId: str
    InstanceId: str
    ContactFlowId: Optional[str] = None

class SubmitAutoEvaluationActionDefinitionTypeDef(BaseModel):
    EvaluationFormId: str

class SearchAvailablePhoneNumbersRequestRequestTypeDef(BaseModel):
    PhoneNumberCountryCode: PhoneNumberCountryCodeType
    PhoneNumberType: PhoneNumberTypeType
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberPrefix: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SortTypeDef(BaseModel):
    FieldName: SortableFieldNameType
    Order: SortOrderType

class SearchPredefinedAttributesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchCriteria: Optional["PredefinedAttributeSearchCriteriaTypeDef"] = None

class TagSetTypeDef(BaseModel):
    key: Optional[str] = None
    value: Optional[str] = None

class SecurityProfileSearchSummaryTypeDef(BaseModel):
    Id: Optional[str] = None
    OrganizationResourceId: Optional[str] = None
    Arn: Optional[str] = None
    SecurityProfileName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class SearchVocabulariesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    State: Optional[VocabularyStateType] = None
    NameStartsWith: Optional[str] = None
    LanguageCode: Optional[VocabularyLanguageCodeType] = None

class VocabularySummaryTypeDef(BaseModel):
    Name: str
    Id: str
    Arn: str
    LanguageCode: VocabularyLanguageCodeType
    State: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: Optional[str] = None

class SearchableContactAttributesCriteriaTypeDef(BaseModel):
    Key: str
    Values: Sequence[str]

class SignInDistributionTypeDef(BaseModel):
    Region: str
    Enabled: bool

class UploadUrlMetadataTypeDef(BaseModel):
    Url: Optional[str] = None
    UrlExpiry: Optional[str] = None
    HeadersToInclude: Optional[Dict[str, str]] = None

class StartContactEvaluationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    EvaluationFormId: str
    ClientToken: Optional[str] = None

class VoiceRecordingConfigurationTypeDef(BaseModel):
    VoiceRecordingTrack: Optional[VoiceRecordingTrackType] = None

class StopContactRecordingRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str

class StopContactStreamingRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    StreamingId: str

class SuspendContactRecordingRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str

class TagContactRequestRequestTypeDef(BaseModel):
    ContactId: str
    InstanceId: str
    Tags: Mapping[str, str]

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class TranscriptCriteriaTypeDef(BaseModel):
    ParticipantRole: ParticipantRoleType
    SearchText: Sequence[str]
    MatchType: SearchContactsMatchTypeType

class TransferContactRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    ContactFlowId: str
    QueueId: Optional[str] = None
    UserId: Optional[str] = None
    ClientToken: Optional[str] = None

class UntagContactRequestRequestTypeDef(BaseModel):
    ContactId: str
    InstanceId: str
    TagKeys: Sequence[str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAgentStatusRequestRequestTypeDef(BaseModel):
    InstanceId: str
    AgentStatusId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[AgentStatusStateType] = None
    DisplayOrder: Optional[int] = None
    ResetOrderNumber: Optional[bool] = None

class UpdateAuthenticationProfileRequestRequestTypeDef(BaseModel):
    AuthenticationProfileId: str
    InstanceId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    AllowedIps: Optional[Sequence[str]] = None
    BlockedIps: Optional[Sequence[str]] = None
    PeriodicSessionDuration: Optional[int] = None

class UpdateContactAttributesRequestRequestTypeDef(BaseModel):
    InitialContactId: str
    InstanceId: str
    Attributes: Mapping[str, str]

class UpdateContactFlowContentRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactFlowId: str
    Content: str

class UpdateContactFlowMetadataRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactFlowId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ContactFlowState: Optional[ContactFlowStateType] = None

class UpdateContactFlowModuleContentRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactFlowModuleId: str
    Content: str

class UpdateContactFlowModuleMetadataRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactFlowModuleId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[ContactFlowModuleStateType] = None

class UpdateContactFlowNameRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactFlowId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateContactRoutingDataRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    QueueTimeAdjustmentSeconds: Optional[int] = None
    QueuePriority: Optional[int] = None

class UpdateInstanceAttributeRequestRequestTypeDef(BaseModel):
    InstanceId: str
    AttributeType: InstanceAttributeTypeType
    Value: str

class UpdatePhoneNumberMetadataRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str
    PhoneNumberDescription: Optional[str] = None
    ClientToken: Optional[str] = None

class UpdatePhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    ClientToken: Optional[str] = None

class UpdatePromptRequestRequestTypeDef(BaseModel):
    InstanceId: str
    PromptId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    S3Uri: Optional[str] = None

class UpdateQueueHoursOfOperationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QueueId: str
    HoursOfOperationId: str

class UpdateQueueMaxContactsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QueueId: str
    MaxContacts: Optional[int] = None

class UpdateQueueNameRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QueueId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateQueueStatusRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QueueId: str
    Status: QueueStatusType

class UpdateQuickConnectNameRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QuickConnectId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateRoutingProfileAgentAvailabilityTimerRequestRequestTypeDef(BaseModel):
    InstanceId: str
    RoutingProfileId: str
    AgentAvailabilityTimer: AgentAvailabilityTimerType

class UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef(BaseModel):
    InstanceId: str
    RoutingProfileId: str
    DefaultOutboundQueueId: str

class UpdateRoutingProfileNameRequestRequestTypeDef(BaseModel):
    InstanceId: str
    RoutingProfileId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateUserHierarchyGroupNameRequestRequestTypeDef(BaseModel):
    Name: str
    HierarchyGroupId: str
    InstanceId: str

class UpdateUserHierarchyRequestRequestTypeDef(BaseModel):
    UserId: str
    InstanceId: str
    HierarchyGroupId: Optional[str] = None

class UpdateUserRoutingProfileRequestRequestTypeDef(BaseModel):
    RoutingProfileId: str
    UserId: str
    InstanceId: str

class UpdateUserSecurityProfilesRequestRequestTypeDef(BaseModel):
    SecurityProfileIds: Sequence[str]
    UserId: str
    InstanceId: str

class UpdateViewMetadataRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ViewId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UserReferenceTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None

class UserIdentityInfoLiteTypeDef(BaseModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None

class ViewContentTypeDef(BaseModel):
    InputSchema: Optional[str] = None
    Template: Optional[str] = None
    Actions: Optional[List[str]] = None

class RuleSummaryTypeDef(BaseModel):
    Name: str
    RuleId: str
    RuleArn: str
    EventSourceName: EventSourceNameType
    PublishStatus: RulePublishStatusType
    ActionSummaries: List[ActionSummaryTypeDef]
    CreatedTime: datetime
    LastUpdatedTime: datetime

class ActivateEvaluationFormResponseTypeDef(BaseModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateAnalyticsDataSetResponseTypeDef(BaseModel):
    DataSetId: str
    TargetAccountId: str
    ResourceShareId: str
    ResourceShareArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateInstanceStorageConfigResponseTypeDef(BaseModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateSecurityKeyResponseTypeDef(BaseModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClaimPhoneNumberResponseTypeDef(BaseModel):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAgentStatusResponseTypeDef(BaseModel):
    AgentStatusARN: str
    AgentStatusId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContactFlowModuleResponseTypeDef(BaseModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContactFlowResponseTypeDef(BaseModel):
    ContactFlowId: str
    ContactFlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEvaluationFormResponseTypeDef(BaseModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHoursOfOperationResponseTypeDef(BaseModel):
    HoursOfOperationId: str
    HoursOfOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceResponseTypeDef(BaseModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIntegrationAssociationResponseTypeDef(BaseModel):
    IntegrationAssociationId: str
    IntegrationAssociationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePersistentContactAssociationResponseTypeDef(BaseModel):
    ContinuedFromContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePromptResponseTypeDef(BaseModel):
    PromptARN: str
    PromptId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueueResponseTypeDef(BaseModel):
    QueueArn: str
    QueueId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQuickConnectResponseTypeDef(BaseModel):
    QuickConnectARN: str
    QuickConnectId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRoutingProfileResponseTypeDef(BaseModel):
    RoutingProfileArn: str
    RoutingProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleResponseTypeDef(BaseModel):
    RuleArn: str
    RuleId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityProfileResponseTypeDef(BaseModel):
    SecurityProfileId: str
    SecurityProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskTemplateResponseTypeDef(BaseModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrafficDistributionGroupResponseTypeDef(BaseModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUseCaseResponseTypeDef(BaseModel):
    UseCaseId: str
    UseCaseArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserHierarchyGroupResponseTypeDef(BaseModel):
    HierarchyGroupId: str
    HierarchyGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(BaseModel):
    UserId: str
    UserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVocabularyResponseTypeDef(BaseModel):
    VocabularyArn: str
    VocabularyId: str
    State: VocabularyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeactivateEvaluationFormResponseTypeDef(BaseModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVocabularyResponseTypeDef(BaseModel):
    VocabularyArn: str
    VocabularyId: str
    State: VocabularyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetContactAttributesResponseTypeDef(BaseModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetFlowAssociationResponseTypeDef(BaseModel):
    ResourceId: str
    FlowId: str
    ResourceType: Literal["SMS_PHONE_NUMBER"]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPromptFileResponseTypeDef(BaseModel):
    PromptPresignedUrl: str
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportPhoneNumberResponseTypeDef(BaseModel):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApprovedOriginsResponseTypeDef(BaseModel):
    Origins: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListLambdaFunctionsResponseTypeDef(BaseModel):
    LambdaFunctions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSecurityProfilePermissionsResponseTypeDef(BaseModel):
    Permissions: List[str]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class MonitorContactResponseTypeDef(BaseModel):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicateInstanceResponseTypeDef(BaseModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendChatIntegrationEventResponseTypeDef(BaseModel):
    InitialContactId: str
    NewChatCreated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class StartChatContactResponseTypeDef(BaseModel):
    ContactId: str
    ParticipantId: str
    ParticipantToken: str
    ContinuedFromContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartContactEvaluationResponseTypeDef(BaseModel):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartContactStreamingResponseTypeDef(BaseModel):
    StreamingId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartOutboundVoiceContactResponseTypeDef(BaseModel):
    ContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartTaskContactResponseTypeDef(BaseModel):
    ContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitContactEvaluationResponseTypeDef(BaseModel):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class TransferContactResponseTypeDef(BaseModel):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContactEvaluationResponseTypeDef(BaseModel):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEvaluationFormResponseTypeDef(BaseModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePhoneNumberResponseTypeDef(BaseModel):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePromptResponseTypeDef(BaseModel):
    PromptARN: str
    PromptId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AgentConfigOutputTypeDef(BaseModel):
    Distributions: List[DistributionTypeDef]

class AgentConfigTypeDef(BaseModel):
    Distributions: Sequence[DistributionTypeDef]

class TelephonyConfigOutputTypeDef(BaseModel):
    Distributions: List[DistributionTypeDef]

class TelephonyConfigTypeDef(BaseModel):
    Distributions: Sequence[DistributionTypeDef]

class AgentContactReferenceTypeDef(BaseModel):
    ContactId: Optional[str] = None
    Channel: Optional[ChannelType] = None
    InitiationMethod: Optional[ContactInitiationMethodType] = None
    AgentContactState: Optional[ContactStateType] = None
    StateStartTimestamp: Optional[datetime] = None
    ConnectedToAgentTimestamp: Optional[datetime] = None
    Queue: Optional[QueueReferenceTypeDef] = None

class HierarchyGroupsTypeDef(BaseModel):
    Level1: Optional[AgentHierarchyGroupTypeDef] = None
    Level2: Optional[AgentHierarchyGroupTypeDef] = None
    Level3: Optional[AgentHierarchyGroupTypeDef] = None
    Level4: Optional[AgentHierarchyGroupTypeDef] = None
    Level5: Optional[AgentHierarchyGroupTypeDef] = None

class AllowedCapabilitiesTypeDef(BaseModel):
    Customer: Optional[ParticipantCapabilitiesTypeDef] = None
    Agent: Optional[ParticipantCapabilitiesTypeDef] = None

class CustomerTypeDef(BaseModel):
    DeviceInfo: Optional[DeviceInfoTypeDef] = None
    Capabilities: Optional[ParticipantCapabilitiesTypeDef] = None

class AgentQualityMetricsTypeDef(BaseModel):
    Audio: Optional[AudioQualityMetricsInfoTypeDef] = None

class CustomerQualityMetricsTypeDef(BaseModel):
    Audio: Optional[AudioQualityMetricsInfoTypeDef] = None

class ListAgentStatusResponseTypeDef(BaseModel):
    AgentStatusSummaryList: List[AgentStatusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeAgentStatusResponseTypeDef(BaseModel):
    AgentStatus: AgentStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MatchCriteriaTypeDef(BaseModel):
    AgentsCriteria: Optional[AgentsCriteriaTypeDef] = None

class ListAnalyticsDataAssociationsResponseTypeDef(BaseModel):
    Results: List[AnalyticsDataAssociationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSecurityProfileApplicationsResponseTypeDef(BaseModel):
    Applications: List[ApplicationOutputTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateLexBotRequestRequestTypeDef(BaseModel):
    InstanceId: str
    LexBot: LexBotTypeDef

class ListLexBotsResponseTypeDef(BaseModel):
    LexBots: List[LexBotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateBotRequestRequestTypeDef(BaseModel):
    InstanceId: str
    LexBot: Optional[LexBotTypeDef] = None
    LexV2Bot: Optional[LexV2BotTypeDef] = None

class DisassociateBotRequestRequestTypeDef(BaseModel):
    InstanceId: str
    LexBot: Optional[LexBotTypeDef] = None
    LexV2Bot: Optional[LexV2BotTypeDef] = None

class LexBotConfigTypeDef(BaseModel):
    LexBot: Optional[LexBotTypeDef] = None
    LexV2Bot: Optional[LexV2BotTypeDef] = None

class AssociateUserProficienciesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiencyTypeDef]

class ListUserProficienciesResponseTypeDef(BaseModel):
    UserProficiencyList: List[UserProficiencyTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateUserProficienciesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiencyTypeDef]

class AttachedFileTypeDef(BaseModel):
    CreationTime: str
    FileArn: str
    FileId: str
    FileName: str
    FileSizeInBytes: int
    FileStatus: FileStatusTypeType
    CreatedBy: Optional[CreatedByInfoTypeDef] = None
    FileUseCaseType: Optional[Literal["ATTACHMENT"]] = None
    AssociatedResourceArn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class StartAttachedFileUploadRequestRequestTypeDef(BaseModel):
    InstanceId: str
    FileName: str
    FileSizeInBytes: int
    FileUseCaseType: Literal["ATTACHMENT"]
    AssociatedResourceArn: str
    ClientToken: Optional[str] = None
    UrlExpiryInSeconds: Optional[int] = None
    CreatedBy: Optional[CreatedByInfoTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class AttributeAndConditionTypeDef(BaseModel):
    TagConditions: Optional[Sequence[TagConditionTypeDef]] = None
    HierarchyGroupCondition: Optional[HierarchyGroupConditionTypeDef] = None

class ControlPlaneTagFilterTypeDef(BaseModel):
    OrConditions: Optional[Sequence[Sequence[TagConditionTypeDef]]] = None
    AndConditions: Optional[Sequence[TagConditionTypeDef]] = None
    TagCondition: Optional[TagConditionTypeDef] = None

class DescribeInstanceAttributeResponseTypeDef(BaseModel):
    Attribute: AttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceAttributesResponseTypeDef(BaseModel):
    Attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MeetingFeaturesConfigurationTypeDef(BaseModel):
    Audio: Optional[AudioFeaturesTypeDef] = None

class ListAuthenticationProfilesResponseTypeDef(BaseModel):
    AuthenticationProfileSummaryList: List[AuthenticationProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeAuthenticationProfileResponseTypeDef(BaseModel):
    AuthenticationProfile: AuthenticationProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchAvailablePhoneNumbersResponseTypeDef(BaseModel):
    AvailableNumbersList: List[AvailableNumberSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchAssociateAnalyticsDataSetResponseTypeDef(BaseModel):
    Created: List[AnalyticsDataAssociationResultTypeDef]
    Errors: List[ErrorResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateAnalyticsDataSetResponseTypeDef(BaseModel):
    Deleted: List[str]
    Errors: List[ErrorResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetFlowAssociationResponseTypeDef(BaseModel):
    FlowAssociationSummaryList: List[FlowAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFlowAssociationsResponseTypeDef(BaseModel):
    FlowAssociationSummaryList: List[FlowAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchPutContactResponseTypeDef(BaseModel):
    SuccessfulRequestList: List[SuccessfulRequestTypeDef]
    FailedRequestList: List[FailedRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartContactStreamingRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    ChatStreamingConfiguration: ChatStreamingConfigurationTypeDef
    ClientToken: str

class ClaimedPhoneNumberSummaryTypeDef(BaseModel):
    PhoneNumberId: Optional[str] = None
    PhoneNumberArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    PhoneNumberCountryCode: Optional[PhoneNumberCountryCodeType] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    PhoneNumberDescription: Optional[str] = None
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    PhoneNumberStatus: Optional[PhoneNumberStatusTypeDef] = None
    SourcePhoneNumberArn: Optional[str] = None

class ContactDataRequestTypeDef(BaseModel):
    SystemEndpoint: Optional[EndpointTypeDef] = None
    CustomerEndpoint: Optional[EndpointTypeDef] = None
    RequestIdentifier: Optional[str] = None
    QueueId: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    Campaign: Optional[CampaignTypeDef] = None

class UserDataFiltersTypeDef(BaseModel):
    Queues: Optional[Sequence[str]] = None
    ContactFilter: Optional[ContactFilterTypeDef] = None
    RoutingProfiles: Optional[Sequence[str]] = None
    Agents: Optional[Sequence[str]] = None
    UserHierarchyGroups: Optional[Sequence[str]] = None

class ContactFlowModuleSearchCriteriaTypeDef(BaseModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class ContactFlowSearchCriteriaTypeDef(BaseModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    TypeCondition: Optional[ContactFlowTypeType] = None
    StateCondition: Optional[ContactFlowStateType] = None
    StatusCondition: Optional[ContactFlowStatusType] = None

class HoursOfOperationSearchCriteriaTypeDef(BaseModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class PredefinedAttributeSearchCriteriaTypeDef(BaseModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class PromptSearchCriteriaTypeDef(BaseModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class QueueSearchCriteriaTypeDef(BaseModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    QueueTypeCondition: Optional[Literal["STANDARD"]] = None

class QuickConnectSearchCriteriaTypeDef(BaseModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class RoutingProfileSearchCriteriaTypeDef(BaseModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class SecurityProfileSearchCriteriaTypeDef(BaseModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class UserSearchCriteriaTypeDef(BaseModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    HierarchyGroupCondition: Optional[HierarchyGroupConditionTypeDef] = None

class ListContactFlowModulesResponseTypeDef(BaseModel):
    ContactFlowModulesSummaryList: List[ContactFlowModuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeContactFlowModuleResponseTypeDef(BaseModel):
    ContactFlowModule: ContactFlowModuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchContactFlowModulesResponseTypeDef(BaseModel):
    ContactFlowModules: List[ContactFlowModuleTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListContactFlowsResponseTypeDef(BaseModel):
    ContactFlowSummaryList: List[ContactFlowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeContactFlowResponseTypeDef(BaseModel):
    ContactFlow: ContactFlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchContactFlowsResponseTypeDef(BaseModel):
    ContactFlows: List[ContactFlowTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ContactSearchSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    InitialContactId: Optional[str] = None
    PreviousContactId: Optional[str] = None
    InitiationMethod: Optional[ContactInitiationMethodType] = None
    Channel: Optional[ChannelType] = None
    QueueInfo: Optional[ContactSearchSummaryQueueInfoTypeDef] = None
    AgentInfo: Optional[ContactSearchSummaryAgentInfoTypeDef] = None
    InitiationTimestamp: Optional[datetime] = None
    DisconnectTimestamp: Optional[datetime] = None
    ScheduledTimestamp: Optional[datetime] = None

class CreateEvaluationFormRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Title: str
    Items: Sequence[EvaluationFormItemUnionTypeDef]
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategyTypeDef] = None
    ClientToken: Optional[str] = None

class EvaluationFormContentTypeDef(BaseModel):
    EvaluationFormVersion: int
    EvaluationFormId: str
    EvaluationFormArn: str
    Title: str
    Items: List["EvaluationFormItemOutputTypeDef"]
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategyTypeDef] = None

class EvaluationFormTypeDef(BaseModel):
    EvaluationFormId: str
    EvaluationFormVersion: int
    Locked: bool
    EvaluationFormArn: str
    Title: str
    Status: EvaluationFormVersionStatusType
    Items: List["EvaluationFormItemOutputTypeDef"]
    CreatedTime: datetime
    CreatedBy: str
    LastModifiedTime: datetime
    LastModifiedBy: str
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategyTypeDef] = None
    Tags: Optional[Dict[str, str]] = None

class UpdateEvaluationFormRequestRequestTypeDef(BaseModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int
    Title: str
    Items: Sequence[EvaluationFormItemUnionTypeDef]
    CreateNewVersion: Optional[bool] = None
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategyTypeDef] = None
    ClientToken: Optional[str] = None

class CreateParticipantRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    ParticipantDetails: ParticipantDetailsToAddTypeDef
    ClientToken: Optional[str] = None

class CreateParticipantResponseTypeDef(BaseModel):
    ParticipantCredentials: ParticipantTokenCredentialsTypeDef
    ParticipantId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePredefinedAttributeRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    Values: PredefinedAttributeValuesTypeDef

class UpdatePredefinedAttributeRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    Values: Optional[PredefinedAttributeValuesTypeDef] = None

class CreateQueueRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    HoursOfOperationId: str
    Description: Optional[str] = None
    OutboundCallerConfig: Optional[OutboundCallerConfigTypeDef] = None
    MaxContacts: Optional[int] = None
    QuickConnectIds: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class QueueTypeDef(BaseModel):
    Name: Optional[str] = None
    QueueArn: Optional[str] = None
    QueueId: Optional[str] = None
    Description: Optional[str] = None
    OutboundCallerConfig: Optional[OutboundCallerConfigTypeDef] = None
    HoursOfOperationId: Optional[str] = None
    MaxContacts: Optional[int] = None
    Status: Optional[QueueStatusType] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class UpdateQueueOutboundCallerConfigRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QueueId: str
    OutboundCallerConfig: OutboundCallerConfigTypeDef

class UpdateUserIdentityInfoRequestRequestTypeDef(BaseModel):
    IdentityInfo: UserIdentityInfoTypeDef
    UserId: str
    InstanceId: str

class CreateUserRequestRequestTypeDef(BaseModel):
    Username: str
    PhoneConfig: UserPhoneConfigTypeDef
    SecurityProfileIds: Sequence[str]
    RoutingProfileId: str
    InstanceId: str
    Password: Optional[str] = None
    IdentityInfo: Optional[UserIdentityInfoTypeDef] = None
    DirectoryUserId: Optional[str] = None
    HierarchyGroupId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateUserPhoneConfigRequestRequestTypeDef(BaseModel):
    PhoneConfig: UserPhoneConfigTypeDef
    UserId: str
    InstanceId: str

class UserTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Username: Optional[str] = None
    IdentityInfo: Optional[UserIdentityInfoTypeDef] = None
    PhoneConfig: Optional[UserPhoneConfigTypeDef] = None
    DirectoryUserId: Optional[str] = None
    SecurityProfileIds: Optional[List[str]] = None
    RoutingProfileId: Optional[str] = None
    HierarchyGroupId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class CreateViewRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Status: ViewStatusType
    Content: ViewInputContentTypeDef
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateViewContentRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ViewId: str
    Status: ViewStatusType
    Content: ViewInputContentTypeDef

class GetFederationTokenResponseTypeDef(BaseModel):
    Credentials: CredentialsTypeDef
    SignInUrl: str
    UserArn: str
    UserId: str
    ResponseMetadata: ResponseMetadataTypeDef

class MediaConcurrencyTypeDef(BaseModel):
    Channel: ChannelType
    Concurrency: int
    CrossChannelBehavior: Optional[CrossChannelBehaviorTypeDef] = None

class CurrentMetricDataTypeDef(BaseModel):
    Metric: Optional[CurrentMetricTypeDef] = None
    Value: Optional[float] = None

class ListDefaultVocabulariesResponseTypeDef(BaseModel):
    DefaultVocabularyList: List[DefaultVocabularyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribePromptResponseTypeDef(BaseModel):
    Prompt: PromptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchPromptsResponseTypeDef(BaseModel):
    Prompts: List[PromptTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSecurityProfileResponseTypeDef(BaseModel):
    SecurityProfile: SecurityProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrafficDistributionGroupResponseTypeDef(BaseModel):
    TrafficDistributionGroup: TrafficDistributionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVocabularyResponseTypeDef(BaseModel):
    Vocabulary: VocabularyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DimensionsTypeDef(BaseModel):
    Queue: Optional[QueueReferenceTypeDef] = None
    Channel: Optional[ChannelType] = None
    RoutingProfile: Optional[RoutingProfileReferenceTypeDef] = None
    RoutingStepExpression: Optional[str] = None

class DisassociateRoutingProfileQueuesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    RoutingProfileId: str
    QueueReferences: Sequence[RoutingProfileQueueReferenceTypeDef]

class RoutingProfileQueueConfigTypeDef(BaseModel):
    QueueReference: RoutingProfileQueueReferenceTypeDef
    Priority: int
    Delay: int

class DisassociateUserProficienciesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiencyDisassociateTypeDef]

class StopContactRequestRequestTypeDef(BaseModel):
    ContactId: str
    InstanceId: str
    DisconnectReason: Optional[DisconnectReasonTypeDef] = None

class GetAttachedFileResponseTypeDef(BaseModel):
    FileArn: str
    FileId: str
    CreationTime: str
    FileStatus: FileStatusTypeType
    FileName: str
    FileSizeInBytes: int
    AssociatedResourceArn: str
    FileUseCaseType: Literal["ATTACHMENT"]
    CreatedBy: CreatedByInfoTypeDef
    DownloadUrlMetadata: DownloadUrlMetadataTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class KinesisVideoStreamConfigTypeDef(BaseModel):
    Prefix: str
    RetentionPeriodHours: int
    EncryptionConfig: EncryptionConfigTypeDef

class S3ConfigTypeDef(BaseModel):
    BucketName: str
    BucketPrefix: str
    EncryptionConfig: Optional[EncryptionConfigTypeDef] = None

class EvaluationAnswerInputTypeDef(BaseModel):
    Value: Optional[EvaluationAnswerDataTypeDef] = None

class EvaluationAnswerOutputTypeDef(BaseModel):
    Value: Optional[EvaluationAnswerDataTypeDef] = None
    SystemSuggestedValue: Optional[EvaluationAnswerDataTypeDef] = None

class EvaluationFormNumericQuestionAutomationTypeDef(BaseModel):
    PropertyValue: Optional[NumericQuestionPropertyValueAutomationTypeDef] = None

class EvaluationFormSingleSelectQuestionAutomationOptionTypeDef(BaseModel):
    RuleCategory: Optional[SingleSelectQuestionRuleCategoryAutomationTypeDef] = None

class ListEvaluationFormsResponseTypeDef(BaseModel):
    EvaluationFormSummaryList: List[EvaluationFormSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListEvaluationFormVersionsResponseTypeDef(BaseModel):
    EvaluationFormVersionSummaryList: List[EvaluationFormVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EvaluationMetadataTypeDef(BaseModel):
    ContactId: str
    EvaluatorArn: str
    ContactAgentId: Optional[str] = None
    Score: Optional[EvaluationScoreTypeDef] = None

class EvaluationSummaryTypeDef(BaseModel):
    EvaluationId: str
    EvaluationArn: str
    EvaluationFormTitle: str
    EvaluationFormId: str
    Status: EvaluationStatusType
    EvaluatorArn: str
    CreatedTime: datetime
    LastModifiedTime: datetime
    Score: Optional[EvaluationScoreTypeDef] = None

class StepTypeDef(BaseModel):
    Expiry: Optional[ExpiryTypeDef] = None
    Expression: Optional["ExpressionTypeDef"] = None
    Status: Optional[RoutingCriteriaStepStatusType] = None

class FieldValueOutputTypeDef(BaseModel):
    Id: str
    Value: FieldValueUnionOutputTypeDef

class FieldValueTypeDef(BaseModel):
    Id: str
    Value: FieldValueUnionTypeDef

class GetCurrentMetricDataRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Filters: FiltersTypeDef
    CurrentMetrics: Sequence[CurrentMetricTypeDef]
    Groupings: Optional[Sequence[GroupingType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortCriteria: Optional[Sequence[CurrentMetricSortCriteriaTypeDef]] = None

class ListAgentStatusRequestListAgentStatusesPaginateTypeDef(BaseModel):
    InstanceId: str
    AgentStatusTypes: Optional[Sequence[AgentStatusTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApprovedOriginsRequestListApprovedOriginsPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuthenticationProfilesRequestListAuthenticationProfilesPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBotsRequestListBotsPaginateTypeDef(BaseModel):
    InstanceId: str
    LexVersion: LexVersionType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContactEvaluationsRequestListContactEvaluationsPaginateTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContactFlowModulesRequestListContactFlowModulesPaginateTypeDef(BaseModel):
    InstanceId: str
    ContactFlowModuleState: Optional[ContactFlowModuleStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContactFlowsRequestListContactFlowsPaginateTypeDef(BaseModel):
    InstanceId: str
    ContactFlowTypes: Optional[Sequence[ContactFlowTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContactReferencesRequestListContactReferencesPaginateTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    ReferenceTypes: Sequence[ReferenceTypeType]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDefaultVocabulariesRequestListDefaultVocabulariesPaginateTypeDef(BaseModel):
    InstanceId: str
    LanguageCode: Optional[VocabularyLanguageCodeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEvaluationFormVersionsRequestListEvaluationFormVersionsPaginateTypeDef(BaseModel):
    InstanceId: str
    EvaluationFormId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEvaluationFormsRequestListEvaluationFormsPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowAssociationsRequestListFlowAssociationsPaginateTypeDef(BaseModel):
    InstanceId: str
    ResourceType: Optional[Literal["VOICE_PHONE_NUMBER"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHoursOfOperationsRequestListHoursOfOperationsPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceAttributesRequestListInstanceAttributesPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceStorageConfigsRequestListInstanceStorageConfigsPaginateTypeDef(BaseModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstancesRequestListInstancesPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIntegrationAssociationsRequestListIntegrationAssociationsPaginateTypeDef(BaseModel):
    InstanceId: str
    IntegrationType: Optional[IntegrationTypeType] = None
    IntegrationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLambdaFunctionsRequestListLambdaFunctionsPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLexBotsRequestListLexBotsPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPhoneNumbersRequestListPhoneNumbersPaginateTypeDef(BaseModel):
    InstanceId: str
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPhoneNumbersV2RequestListPhoneNumbersV2PaginateTypeDef(BaseModel):
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPredefinedAttributesRequestListPredefinedAttributesPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPromptsRequestListPromptsPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueueQuickConnectsRequestListQueueQuickConnectsPaginateTypeDef(BaseModel):
    InstanceId: str
    QueueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueuesRequestListQueuesPaginateTypeDef(BaseModel):
    InstanceId: str
    QueueTypes: Optional[Sequence[QueueTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQuickConnectsRequestListQuickConnectsPaginateTypeDef(BaseModel):
    InstanceId: str
    QuickConnectTypes: Optional[Sequence[QuickConnectTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoutingProfileQueuesRequestListRoutingProfileQueuesPaginateTypeDef(BaseModel):
    InstanceId: str
    RoutingProfileId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoutingProfilesRequestListRoutingProfilesPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesRequestListRulesPaginateTypeDef(BaseModel):
    InstanceId: str
    PublishStatus: Optional[RulePublishStatusType] = None
    EventSourceName: Optional[EventSourceNameType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityKeysRequestListSecurityKeysPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityProfileApplicationsRequestListSecurityProfileApplicationsPaginateTypeDef(BaseModel):
    SecurityProfileId: str
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityProfilePermissionsRequestListSecurityProfilePermissionsPaginateTypeDef(BaseModel):
    SecurityProfileId: str
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTaskTemplatesRequestListTaskTemplatesPaginateTypeDef(BaseModel):
    InstanceId: str
    Status: Optional[TaskTemplateStatusType] = None
    Name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrafficDistributionGroupsRequestListTrafficDistributionGroupsPaginateTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUseCasesRequestListUseCasesPaginateTypeDef(BaseModel):
    InstanceId: str
    IntegrationAssociationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserHierarchyGroupsRequestListUserHierarchyGroupsPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserProficienciesRequestListUserProficienciesPaginateTypeDef(BaseModel):
    InstanceId: str
    UserId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListViewVersionsRequestListViewVersionsPaginateTypeDef(BaseModel):
    InstanceId: str
    ViewId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListViewsRequestListViewsPaginateTypeDef(BaseModel):
    InstanceId: str
    Type: Optional[ViewTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchAvailablePhoneNumbersRequestSearchAvailablePhoneNumbersPaginateTypeDef(BaseModel):
    PhoneNumberCountryCode: PhoneNumberCountryCodeType
    PhoneNumberType: PhoneNumberTypeType
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchVocabulariesRequestSearchVocabulariesPaginateTypeDef(BaseModel):
    InstanceId: str
    State: Optional[VocabularyStateType] = None
    NameStartsWith: Optional[str] = None
    LanguageCode: Optional[VocabularyLanguageCodeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchContactsTimeRangeTypeDef(BaseModel):
    Type: SearchContactsTimeRangeTypeType
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class UpdateContactScheduleRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    ScheduledTime: TimestampTypeDef

class HierarchyPathReferenceTypeDef(BaseModel):
    LevelOne: Optional[HierarchyGroupSummaryReferenceTypeDef] = None
    LevelTwo: Optional[HierarchyGroupSummaryReferenceTypeDef] = None
    LevelThree: Optional[HierarchyGroupSummaryReferenceTypeDef] = None
    LevelFour: Optional[HierarchyGroupSummaryReferenceTypeDef] = None
    LevelFive: Optional[HierarchyGroupSummaryReferenceTypeDef] = None

class HierarchyPathTypeDef(BaseModel):
    LevelOne: Optional[HierarchyGroupSummaryTypeDef] = None
    LevelTwo: Optional[HierarchyGroupSummaryTypeDef] = None
    LevelThree: Optional[HierarchyGroupSummaryTypeDef] = None
    LevelFour: Optional[HierarchyGroupSummaryTypeDef] = None
    LevelFive: Optional[HierarchyGroupSummaryTypeDef] = None

class ListUserHierarchyGroupsResponseTypeDef(BaseModel):
    UserHierarchyGroupSummaryList: List[HierarchyGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class HierarchyStructureTypeDef(BaseModel):
    LevelOne: Optional[HierarchyLevelTypeDef] = None
    LevelTwo: Optional[HierarchyLevelTypeDef] = None
    LevelThree: Optional[HierarchyLevelTypeDef] = None
    LevelFour: Optional[HierarchyLevelTypeDef] = None
    LevelFive: Optional[HierarchyLevelTypeDef] = None

class HierarchyStructureUpdateTypeDef(BaseModel):
    LevelOne: Optional[HierarchyLevelUpdateTypeDef] = None
    LevelTwo: Optional[HierarchyLevelUpdateTypeDef] = None
    LevelThree: Optional[HierarchyLevelUpdateTypeDef] = None
    LevelFour: Optional[HierarchyLevelUpdateTypeDef] = None
    LevelFive: Optional[HierarchyLevelUpdateTypeDef] = None

class HistoricalMetricTypeDef(BaseModel):
    Name: Optional[HistoricalMetricNameType] = None
    Threshold: Optional[ThresholdTypeDef] = None
    Statistic: Optional[StatisticType] = None
    Unit: Optional[UnitType] = None

class HoursOfOperationConfigTypeDef(BaseModel):
    Day: HoursOfOperationDaysType
    StartTime: HoursOfOperationTimeSliceTypeDef
    EndTime: HoursOfOperationTimeSliceTypeDef

class ListHoursOfOperationsResponseTypeDef(BaseModel):
    HoursOfOperationSummaryList: List[HoursOfOperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InstanceTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    IdentityManagementType: Optional[DirectoryTypeType] = None
    InstanceAlias: Optional[str] = None
    CreatedTime: Optional[datetime] = None
    ServiceRole: Optional[str] = None
    InstanceStatus: Optional[InstanceStatusType] = None
    StatusReason: Optional[InstanceStatusReasonTypeDef] = None
    InboundCallsEnabled: Optional[bool] = None
    OutboundCallsEnabled: Optional[bool] = None
    InstanceAccessUrl: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ListInstancesResponseTypeDef(BaseModel):
    InstanceSummaryList: List[InstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIntegrationAssociationsResponseTypeDef(BaseModel):
    IntegrationAssociationSummaryList: List[IntegrationAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InvisibleFieldInfoTypeDef(BaseModel):
    Id: Optional[TaskTemplateFieldIdentifierTypeDef] = None

class ReadOnlyFieldInfoTypeDef(BaseModel):
    Id: Optional[TaskTemplateFieldIdentifierTypeDef] = None

class RequiredFieldInfoTypeDef(BaseModel):
    Id: Optional[TaskTemplateFieldIdentifierTypeDef] = None

class TaskTemplateDefaultFieldValueTypeDef(BaseModel):
    Id: Optional[TaskTemplateFieldIdentifierTypeDef] = None
    DefaultValue: Optional[str] = None

class TaskTemplateFieldOutputTypeDef(BaseModel):
    Id: TaskTemplateFieldIdentifierTypeDef
    Description: Optional[str] = None
    Type: Optional[TaskTemplateFieldTypeType] = None
    SingleSelectOptions: Optional[List[str]] = None

class TaskTemplateFieldTypeDef(BaseModel):
    Id: TaskTemplateFieldIdentifierTypeDef
    Description: Optional[str] = None
    Type: Optional[TaskTemplateFieldTypeType] = None
    SingleSelectOptions: Optional[Sequence[str]] = None

class ListPhoneNumbersResponseTypeDef(BaseModel):
    PhoneNumberSummaryList: List[PhoneNumberSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPhoneNumbersV2ResponseTypeDef(BaseModel):
    ListPhoneNumbersSummaryList: List[ListPhoneNumbersSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPredefinedAttributesResponseTypeDef(BaseModel):
    PredefinedAttributeSummaryList: List[PredefinedAttributeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPromptsResponseTypeDef(BaseModel):
    PromptSummaryList: List[PromptSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListQueueQuickConnectsResponseTypeDef(BaseModel):
    QuickConnectSummaryList: List[QuickConnectSummaryTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListQuickConnectsResponseTypeDef(BaseModel):
    QuickConnectSummaryList: List[QuickConnectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListQueuesResponseTypeDef(BaseModel):
    QueueSummaryList: List[QueueSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRoutingProfileQueuesResponseTypeDef(BaseModel):
    RoutingProfileQueueConfigSummaryList: List[RoutingProfileQueueConfigSummaryTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRoutingProfilesResponseTypeDef(BaseModel):
    RoutingProfileSummaryList: List[RoutingProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSecurityKeysResponseTypeDef(BaseModel):
    SecurityKeys: List[SecurityKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSecurityProfilesResponseTypeDef(BaseModel):
    SecurityProfileSummaryList: List[SecurityProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTaskTemplatesResponseTypeDef(BaseModel):
    TaskTemplates: List[TaskTemplateMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTrafficDistributionGroupUsersResponseTypeDef(BaseModel):
    TrafficDistributionGroupUserSummaryList: List[TrafficDistributionGroupUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTrafficDistributionGroupsResponseTypeDef(BaseModel):
    TrafficDistributionGroupSummaryList: List[TrafficDistributionGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUseCasesResponseTypeDef(BaseModel):
    UseCaseSummaryList: List[UseCaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUsersResponseTypeDef(BaseModel):
    UserSummaryList: List[UserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListViewVersionsResponseTypeDef(BaseModel):
    ViewVersionSummaryList: List[ViewVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListViewsResponseTypeDef(BaseModel):
    ViewsSummaryList: List[ViewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MetricV2OutputTypeDef(BaseModel):
    Name: Optional[str] = None
    Threshold: Optional[List[ThresholdV2TypeDef]] = None
    MetricFilters: Optional[List[MetricFilterV2OutputTypeDef]] = None

class MetricV2TypeDef(BaseModel):
    Name: Optional[str] = None
    Threshold: Optional[Sequence[ThresholdV2TypeDef]] = None
    MetricFilters: Optional[Sequence[MetricFilterV2TypeDef]] = None

class NewSessionDetailsTypeDef(BaseModel):
    SupportedMessagingContentTypes: Optional[Sequence[str]] = None
    ParticipantDetails: Optional[ParticipantDetailsTypeDef] = None
    Attributes: Optional[Mapping[str, str]] = None
    StreamingConfiguration: Optional[ChatStreamingConfigurationTypeDef] = None

class SendNotificationActionDefinitionOutputTypeDef(BaseModel):
    DeliveryMethod: Literal["EMAIL"]
    Content: str
    ContentType: Literal["PLAIN_TEXT"]
    Recipient: NotificationRecipientTypeOutputTypeDef
    Subject: Optional[str] = None

class SendNotificationActionDefinitionTypeDef(BaseModel):
    DeliveryMethod: Literal["EMAIL"]
    Content: str
    ContentType: Literal["PLAIN_TEXT"]
    Recipient: NotificationRecipientTypeTypeDef
    Subject: Optional[str] = None

class ParticipantTimerConfigurationTypeDef(BaseModel):
    ParticipantRole: TimerEligibleParticipantRolesType
    TimerType: ParticipantTimerTypeType
    TimerValue: ParticipantTimerValueTypeDef

class StartChatContactRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactFlowId: str
    ParticipantDetails: ParticipantDetailsTypeDef
    Attributes: Optional[Mapping[str, str]] = None
    InitialMessage: Optional[ChatMessageTypeDef] = None
    ClientToken: Optional[str] = None
    ChatDurationInMinutes: Optional[int] = None
    SupportedMessagingContentTypes: Optional[Sequence[str]] = None
    PersistentChat: Optional[PersistentChatTypeDef] = None
    RelatedContactId: Optional[str] = None
    SegmentAttributes: Optional[Mapping[str, SegmentAttributeValueTypeDef]] = None

class PredefinedAttributeTypeDef(BaseModel):
    Name: Optional[str] = None
    Values: Optional[PredefinedAttributeValuesOutputTypeDef] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class QuickConnectConfigTypeDef(BaseModel):
    QuickConnectType: QuickConnectTypeType
    UserConfig: Optional[UserQuickConnectConfigTypeDef] = None
    QueueConfig: Optional[QueueQuickConnectConfigTypeDef] = None
    PhoneConfig: Optional[PhoneNumberQuickConnectConfigTypeDef] = None

class RealTimeContactAnalysisTranscriptItemRedactionTypeDef(BaseModel):
    CharacterOffsets: Optional[List[RealTimeContactAnalysisCharacterIntervalTypeDef]] = None

class RealTimeContactAnalysisTranscriptItemWithCharacterOffsetsTypeDef(BaseModel):
    Id: str
    CharacterOffsets: Optional[RealTimeContactAnalysisCharacterIntervalTypeDef] = None

class RealTimeContactAnalysisTranscriptItemWithContentTypeDef(BaseModel):
    Id: str
    Content: Optional[str] = None
    CharacterOffsets: Optional[RealTimeContactAnalysisCharacterIntervalTypeDef] = None

class RealTimeContactAnalysisSegmentAttachmentsTypeDef(BaseModel):
    Id: str
    ParticipantId: str
    ParticipantRole: ParticipantRoleType
    Attachments: List[RealTimeContactAnalysisAttachmentTypeDef]
    Time: RealTimeContactAnalysisTimeDataTypeDef
    DisplayName: Optional[str] = None

class RealTimeContactAnalysisSegmentEventTypeDef(BaseModel):
    Id: str
    EventType: str
    Time: RealTimeContactAnalysisTimeDataTypeDef
    ParticipantId: Optional[str] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    DisplayName: Optional[str] = None

class ReferenceSummaryTypeDef(BaseModel):
    Url: Optional[UrlReferenceTypeDef] = None
    Attachment: Optional[AttachmentReferenceTypeDef] = None
    String: Optional[StringReferenceTypeDef] = None
    Number: Optional[NumberReferenceTypeDef] = None
    Date: Optional[DateReferenceTypeDef] = None
    Email: Optional[EmailReferenceTypeDef] = None

class StartOutboundVoiceContactRequestRequestTypeDef(BaseModel):
    DestinationPhoneNumber: str
    ContactFlowId: str
    InstanceId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    References: Optional[Mapping[str, ReferenceTypeDef]] = None
    RelatedContactId: Optional[str] = None
    ClientToken: Optional[str] = None
    SourcePhoneNumber: Optional[str] = None
    QueueId: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    AnswerMachineDetectionConfig: Optional[AnswerMachineDetectionConfigTypeDef] = None
    CampaignId: Optional[str] = None
    TrafficType: Optional[TrafficTypeType] = None

class StartTaskContactRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    PreviousContactId: Optional[str] = None
    ContactFlowId: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    References: Optional[Mapping[str, ReferenceTypeDef]] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    ScheduledTime: Optional[TimestampTypeDef] = None
    TaskTemplateId: Optional[str] = None
    QuickConnectId: Optional[str] = None
    RelatedContactId: Optional[str] = None

class TaskActionDefinitionOutputTypeDef(BaseModel):
    Name: str
    ContactFlowId: str
    Description: Optional[str] = None
    References: Optional[Dict[str, ReferenceTypeDef]] = None

class TaskActionDefinitionTypeDef(BaseModel):
    Name: str
    ContactFlowId: str
    Description: Optional[str] = None
    References: Optional[Mapping[str, ReferenceTypeDef]] = None

class UpdateContactRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    References: Optional[Mapping[str, ReferenceTypeDef]] = None

class ResourceTagsSearchCriteriaTypeDef(BaseModel):
    TagSearchCondition: Optional[TagSearchConditionTypeDef] = None

class SearchResourceTagsResponseTypeDef(BaseModel):
    Tags: List[TagSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchSecurityProfilesResponseTypeDef(BaseModel):
    SecurityProfiles: List[SecurityProfileSearchSummaryTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchVocabulariesResponseTypeDef(BaseModel):
    VocabularySummaryList: List[VocabularySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchableContactAttributesTypeDef(BaseModel):
    Criteria: Sequence[SearchableContactAttributesCriteriaTypeDef]
    MatchType: Optional[SearchContactsMatchTypeType] = None

class SignInConfigOutputTypeDef(BaseModel):
    Distributions: List[SignInDistributionTypeDef]

class SignInConfigTypeDef(BaseModel):
    Distributions: Sequence[SignInDistributionTypeDef]

class StartAttachedFileUploadResponseTypeDef(BaseModel):
    FileArn: str
    FileId: str
    CreationTime: str
    FileStatus: FileStatusTypeType
    CreatedBy: CreatedByInfoTypeDef
    UploadUrlMetadata: UploadUrlMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartContactRecordingRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    VoiceRecordingConfiguration: VoiceRecordingConfigurationTypeDef

class TranscriptTypeDef(BaseModel):
    Criteria: Sequence[TranscriptCriteriaTypeDef]
    MatchType: Optional[SearchContactsMatchTypeType] = None

class UserSearchSummaryTypeDef(BaseModel):
    Arn: Optional[str] = None
    DirectoryUserId: Optional[str] = None
    HierarchyGroupId: Optional[str] = None
    Id: Optional[str] = None
    IdentityInfo: Optional[UserIdentityInfoLiteTypeDef] = None
    PhoneConfig: Optional[UserPhoneConfigTypeDef] = None
    RoutingProfileId: Optional[str] = None
    SecurityProfileIds: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None
    Username: Optional[str] = None

class ViewTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ViewStatusType] = None
    Type: Optional[ViewTypeType] = None
    Description: Optional[str] = None
    Version: Optional[int] = None
    VersionDescription: Optional[str] = None
    Content: Optional[ViewContentTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    ViewContentSha256: Optional[str] = None

class ListRulesResponseTypeDef(BaseModel):
    RuleSummaryList: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AgentInfoTypeDef(BaseModel):
    Id: Optional[str] = None
    ConnectedToAgentTimestamp: Optional[datetime] = None
    AgentPauseDurationInSeconds: Optional[int] = None
    HierarchyGroups: Optional[HierarchyGroupsTypeDef] = None
    DeviceInfo: Optional[DeviceInfoTypeDef] = None
    Capabilities: Optional[ParticipantCapabilitiesTypeDef] = None

class StartWebRTCContactRequestRequestTypeDef(BaseModel):
    ContactFlowId: str
    InstanceId: str
    ParticipantDetails: ParticipantDetailsTypeDef
    Attributes: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None
    AllowedCapabilities: Optional[AllowedCapabilitiesTypeDef] = None
    RelatedContactId: Optional[str] = None
    References: Optional[Mapping[str, ReferenceTypeDef]] = None
    Description: Optional[str] = None

class QualityMetricsTypeDef(BaseModel):
    Agent: Optional[AgentQualityMetricsTypeDef] = None
    Customer: Optional[CustomerQualityMetricsTypeDef] = None

class AttributeConditionTypeDef(BaseModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    ProficiencyLevel: Optional[float] = None
    MatchCriteria: Optional[MatchCriteriaTypeDef] = None
    ComparisonOperator: Optional[str] = None

class CreateSecurityProfileRequestRequestTypeDef(BaseModel):
    SecurityProfileName: str
    InstanceId: str
    Description: Optional[str] = None
    Permissions: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None
    AllowedAccessControlTags: Optional[Mapping[str, str]] = None
    TagRestrictedResources: Optional[Sequence[str]] = None
    Applications: Optional[Sequence[ApplicationUnionTypeDef]] = None
    HierarchyRestrictedResources: Optional[Sequence[str]] = None
    AllowedAccessControlHierarchyGroupId: Optional[str] = None

class UpdateSecurityProfileRequestRequestTypeDef(BaseModel):
    SecurityProfileId: str
    InstanceId: str
    Description: Optional[str] = None
    Permissions: Optional[Sequence[str]] = None
    AllowedAccessControlTags: Optional[Mapping[str, str]] = None
    TagRestrictedResources: Optional[Sequence[str]] = None
    Applications: Optional[Sequence[ApplicationUnionTypeDef]] = None
    HierarchyRestrictedResources: Optional[Sequence[str]] = None
    AllowedAccessControlHierarchyGroupId: Optional[str] = None

class ListBotsResponseTypeDef(BaseModel):
    LexBots: List[LexBotConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchGetAttachedFileMetadataResponseTypeDef(BaseModel):
    Files: List[AttachedFileTypeDef]
    Errors: List[AttachedFileErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ControlPlaneUserAttributeFilterTypeDef(BaseModel):
    OrConditions: Optional[Sequence[AttributeAndConditionTypeDef]] = None
    AndCondition: Optional[AttributeAndConditionTypeDef] = None
    TagCondition: Optional[TagConditionTypeDef] = None
    HierarchyGroupCondition: Optional[HierarchyGroupConditionTypeDef] = None

class ContactFlowModuleSearchFilterTypeDef(BaseModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class ContactFlowSearchFilterTypeDef(BaseModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class HoursOfOperationSearchFilterTypeDef(BaseModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class PromptSearchFilterTypeDef(BaseModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class QueueSearchFilterTypeDef(BaseModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class QuickConnectSearchFilterTypeDef(BaseModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class RoutingProfileSearchFilterTypeDef(BaseModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class SecurityProfilesSearchFilterTypeDef(BaseModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class MeetingTypeDef(BaseModel):
    MediaRegion: Optional[str] = None
    MediaPlacement: Optional[MediaPlacementTypeDef] = None
    MeetingFeatures: Optional[MeetingFeaturesConfigurationTypeDef] = None
    MeetingId: Optional[str] = None

class DescribePhoneNumberResponseTypeDef(BaseModel):
    ClaimedPhoneNumberSummary: ClaimedPhoneNumberSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutContactRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactDataRequestList: Sequence[ContactDataRequestTypeDef]
    ClientToken: Optional[str] = None

class GetCurrentUserDataRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Filters: UserDataFiltersTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SearchPredefinedAttributesRequestSearchPredefinedAttributesPaginateTypeDef(BaseModel):
    InstanceId: str
    SearchCriteria: Optional[PredefinedAttributeSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchContactsResponseTypeDef(BaseModel):
    Contacts: List[ContactSearchSummaryTypeDef]
    TotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeEvaluationFormResponseTypeDef(BaseModel):
    EvaluationForm: EvaluationFormTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeQueueResponseTypeDef(BaseModel):
    Queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchQueuesResponseTypeDef(BaseModel):
    Queues: List[QueueTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RoutingProfileTypeDef(BaseModel):
    InstanceId: Optional[str] = None
    Name: Optional[str] = None
    RoutingProfileArn: Optional[str] = None
    RoutingProfileId: Optional[str] = None
    Description: Optional[str] = None
    MediaConcurrencies: Optional[List[MediaConcurrencyTypeDef]] = None
    DefaultOutboundQueueId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    NumberOfAssociatedQueues: Optional[int] = None
    NumberOfAssociatedUsers: Optional[int] = None
    AgentAvailabilityTimer: Optional[AgentAvailabilityTimerType] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None
    IsDefault: Optional[bool] = None
    AssociatedQueueIds: Optional[List[str]] = None

class UpdateRoutingProfileConcurrencyRequestRequestTypeDef(BaseModel):
    InstanceId: str
    RoutingProfileId: str
    MediaConcurrencies: Sequence[MediaConcurrencyTypeDef]

class CurrentMetricResultTypeDef(BaseModel):
    Dimensions: Optional[DimensionsTypeDef] = None
    Collections: Optional[List[CurrentMetricDataTypeDef]] = None

class AssociateRoutingProfileQueuesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    RoutingProfileId: str
    QueueConfigs: Sequence[RoutingProfileQueueConfigTypeDef]

class CreateRoutingProfileRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    Description: str
    DefaultOutboundQueueId: str
    MediaConcurrencies: Sequence[MediaConcurrencyTypeDef]
    QueueConfigs: Optional[Sequence[RoutingProfileQueueConfigTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None
    AgentAvailabilityTimer: Optional[AgentAvailabilityTimerType] = None

class UpdateRoutingProfileQueuesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    RoutingProfileId: str
    QueueConfigs: Sequence[RoutingProfileQueueConfigTypeDef]

class InstanceStorageConfigTypeDef(BaseModel):
    StorageType: StorageTypeType
    AssociationId: Optional[str] = None
    S3Config: Optional[S3ConfigTypeDef] = None
    KinesisVideoStreamConfig: Optional[KinesisVideoStreamConfigTypeDef] = None
    KinesisStreamConfig: Optional[KinesisStreamConfigTypeDef] = None
    KinesisFirehoseConfig: Optional[KinesisFirehoseConfigTypeDef] = None

class SubmitContactEvaluationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    EvaluationId: str
    Answers: Optional[Mapping[str, EvaluationAnswerInputTypeDef]] = None
    Notes: Optional[Mapping[str, EvaluationNoteTypeDef]] = None

class UpdateContactEvaluationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    EvaluationId: str
    Answers: Optional[Mapping[str, EvaluationAnswerInputTypeDef]] = None
    Notes: Optional[Mapping[str, EvaluationNoteTypeDef]] = None

class EvaluationFormNumericQuestionPropertiesOutputTypeDef(BaseModel):
    MinValue: int
    MaxValue: int
    Options: Optional[List[EvaluationFormNumericQuestionOptionTypeDef]] = None
    Automation: Optional[EvaluationFormNumericQuestionAutomationTypeDef] = None

class EvaluationFormNumericQuestionPropertiesTypeDef(BaseModel):
    MinValue: int
    MaxValue: int
    Options: Optional[Sequence[EvaluationFormNumericQuestionOptionTypeDef]] = None
    Automation: Optional[EvaluationFormNumericQuestionAutomationTypeDef] = None

class EvaluationFormSingleSelectQuestionAutomationOutputTypeDef(BaseModel):
    Options: List[EvaluationFormSingleSelectQuestionAutomationOptionTypeDef]
    DefaultOptionRefId: Optional[str] = None

class EvaluationFormSingleSelectQuestionAutomationTypeDef(BaseModel):
    Options: Sequence[EvaluationFormSingleSelectQuestionAutomationOptionTypeDef]
    DefaultOptionRefId: Optional[str] = None

class EvaluationTypeDef(BaseModel):
    EvaluationId: str
    EvaluationArn: str
    Metadata: EvaluationMetadataTypeDef
    Answers: Dict[str, EvaluationAnswerOutputTypeDef]
    Notes: Dict[str, EvaluationNoteTypeDef]
    Status: EvaluationStatusType
    CreatedTime: datetime
    LastModifiedTime: datetime
    Scores: Optional[Dict[str, EvaluationScoreTypeDef]] = None
    Tags: Optional[Dict[str, str]] = None

class ListContactEvaluationsResponseTypeDef(BaseModel):
    EvaluationSummaryList: List[EvaluationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RoutingCriteriaTypeDef(BaseModel):
    Steps: Optional[List[StepTypeDef]] = None
    ActivationTimestamp: Optional[datetime] = None
    Index: Optional[int] = None

class CreateCaseActionDefinitionOutputTypeDef(BaseModel):
    Fields: List[FieldValueOutputTypeDef]
    TemplateId: str

class UpdateCaseActionDefinitionOutputTypeDef(BaseModel):
    Fields: List[FieldValueOutputTypeDef]

class CreateCaseActionDefinitionTypeDef(BaseModel):
    Fields: Sequence[FieldValueTypeDef]
    TemplateId: str

class UpdateCaseActionDefinitionTypeDef(BaseModel):
    Fields: Sequence[FieldValueTypeDef]

class UserDataTypeDef(BaseModel):
    User: Optional[UserReferenceTypeDef] = None
    RoutingProfile: Optional[RoutingProfileReferenceTypeDef] = None
    HierarchyPath: Optional[HierarchyPathReferenceTypeDef] = None
    Status: Optional[AgentStatusReferenceTypeDef] = None
    AvailableSlotsByChannel: Optional[Dict[ChannelType, int]] = None
    MaxSlotsByChannel: Optional[Dict[ChannelType, int]] = None
    ActiveSlotsByChannel: Optional[Dict[ChannelType, int]] = None
    Contacts: Optional[List[AgentContactReferenceTypeDef]] = None
    NextStatus: Optional[str] = None

class HierarchyGroupTypeDef(BaseModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LevelId: Optional[str] = None
    HierarchyPath: Optional[HierarchyPathTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class DescribeUserHierarchyStructureResponseTypeDef(BaseModel):
    HierarchyStructure: HierarchyStructureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserHierarchyStructureRequestRequestTypeDef(BaseModel):
    HierarchyStructure: HierarchyStructureUpdateTypeDef
    InstanceId: str

class GetMetricDataRequestGetMetricDataPaginateTypeDef(BaseModel):
    InstanceId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Filters: FiltersTypeDef
    HistoricalMetrics: Sequence[HistoricalMetricTypeDef]
    Groupings: Optional[Sequence[GroupingType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetMetricDataRequestRequestTypeDef(BaseModel):
    InstanceId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Filters: FiltersTypeDef
    HistoricalMetrics: Sequence[HistoricalMetricTypeDef]
    Groupings: Optional[Sequence[GroupingType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class HistoricalMetricDataTypeDef(BaseModel):
    Metric: Optional[HistoricalMetricTypeDef] = None
    Value: Optional[float] = None

class CreateHoursOfOperationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    TimeZone: str
    Config: Sequence[HoursOfOperationConfigTypeDef]
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class HoursOfOperationTypeDef(BaseModel):
    HoursOfOperationId: Optional[str] = None
    HoursOfOperationArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    TimeZone: Optional[str] = None
    Config: Optional[List[HoursOfOperationConfigTypeDef]] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class UpdateHoursOfOperationRequestRequestTypeDef(BaseModel):
    InstanceId: str
    HoursOfOperationId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    TimeZone: Optional[str] = None
    Config: Optional[Sequence[HoursOfOperationConfigTypeDef]] = None

class DescribeInstanceResponseTypeDef(BaseModel):
    Instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TaskTemplateConstraintsOutputTypeDef(BaseModel):
    RequiredFields: Optional[List[RequiredFieldInfoTypeDef]] = None
    ReadOnlyFields: Optional[List[ReadOnlyFieldInfoTypeDef]] = None
    InvisibleFields: Optional[List[InvisibleFieldInfoTypeDef]] = None

class TaskTemplateConstraintsTypeDef(BaseModel):
    RequiredFields: Optional[Sequence[RequiredFieldInfoTypeDef]] = None
    ReadOnlyFields: Optional[Sequence[ReadOnlyFieldInfoTypeDef]] = None
    InvisibleFields: Optional[Sequence[InvisibleFieldInfoTypeDef]] = None

class TaskTemplateDefaultsOutputTypeDef(BaseModel):
    DefaultFieldValues: Optional[List[TaskTemplateDefaultFieldValueTypeDef]] = None

class TaskTemplateDefaultsTypeDef(BaseModel):
    DefaultFieldValues: Optional[Sequence[TaskTemplateDefaultFieldValueTypeDef]] = None

class MetricDataV2TypeDef(BaseModel):
    Metric: Optional[MetricV2OutputTypeDef] = None
    Value: Optional[float] = None

class SendChatIntegrationEventRequestRequestTypeDef(BaseModel):
    SourceId: str
    DestinationId: str
    Event: ChatEventTypeDef
    Subtype: Optional[str] = None
    NewSessionDetails: Optional[NewSessionDetailsTypeDef] = None

class ChatParticipantRoleConfigTypeDef(BaseModel):
    ParticipantTimerConfigList: Sequence[ParticipantTimerConfigurationTypeDef]

class DescribePredefinedAttributeResponseTypeDef(BaseModel):
    PredefinedAttribute: PredefinedAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchPredefinedAttributesResponseTypeDef(BaseModel):
    PredefinedAttributes: List[PredefinedAttributeTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateQuickConnectRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    QuickConnectConfig: QuickConnectConfigTypeDef
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class QuickConnectTypeDef(BaseModel):
    QuickConnectARN: Optional[str] = None
    QuickConnectId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    QuickConnectConfig: Optional[QuickConnectConfigTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class UpdateQuickConnectConfigRequestRequestTypeDef(BaseModel):
    InstanceId: str
    QuickConnectId: str
    QuickConnectConfig: QuickConnectConfigTypeDef

class RealTimeContactAnalysisSegmentTranscriptTypeDef(BaseModel):
    Id: str
    ParticipantId: str
    ParticipantRole: ParticipantRoleType
    Content: str
    Time: RealTimeContactAnalysisTimeDataTypeDef
    DisplayName: Optional[str] = None
    ContentType: Optional[str] = None
    Redaction: Optional[RealTimeContactAnalysisTranscriptItemRedactionTypeDef] = None
    Sentiment: Optional[RealTimeContactAnalysisSentimentLabelType] = None

class RealTimeContactAnalysisPointOfInterestTypeDef(BaseModel):
    TranscriptItems: Optional[       List[RealTimeContactAnalysisTranscriptItemWithCharacterOffsetsTypeDef]     ] = None

class RealTimeContactAnalysisIssueDetectedTypeDef(BaseModel):
    TranscriptItems: List[RealTimeContactAnalysisTranscriptItemWithContentTypeDef]

class ListContactReferencesResponseTypeDef(BaseModel):
    ReferenceSummaryList: List[ReferenceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchResourceTagsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ResourceTypes: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchCriteria: Optional[ResourceTagsSearchCriteriaTypeDef] = None

class SearchResourceTagsRequestSearchResourceTagsPaginateTypeDef(BaseModel):
    InstanceId: str
    ResourceTypes: Optional[Sequence[str]] = None
    SearchCriteria: Optional[ResourceTagsSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTrafficDistributionResponseTypeDef(BaseModel):
    TelephonyConfig: TelephonyConfigOutputTypeDef
    Id: str
    Arn: str
    SignInConfig: SignInConfigOutputTypeDef
    AgentConfig: AgentConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrafficDistributionRequestRequestTypeDef(BaseModel):
    Id: str
    TelephonyConfig: Optional[TelephonyConfigTypeDef] = None
    SignInConfig: Optional[SignInConfigTypeDef] = None
    AgentConfig: Optional[AgentConfigTypeDef] = None

class ContactAnalysisTypeDef(BaseModel):
    Transcript: Optional[TranscriptTypeDef] = None

class SearchUsersResponseTypeDef(BaseModel):
    Users: List[UserSearchSummaryTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateViewResponseTypeDef(BaseModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateViewVersionResponseTypeDef(BaseModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeViewResponseTypeDef(BaseModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateViewContentResponseTypeDef(BaseModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExpressionTypeDef(BaseModel):
    AttributeCondition: Optional[AttributeConditionTypeDef] = None
    AndExpression: Optional[List[Dict[str, Any]]] = None
    OrExpression: Optional[List[Dict[str, Any]]] = None

class UserSearchFilterTypeDef(BaseModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None
    UserAttributeFilter: Optional[ControlPlaneUserAttributeFilterTypeDef] = None

class SearchContactFlowModulesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[ContactFlowModuleSearchFilterTypeDef] = None
    SearchCriteria: Optional["ContactFlowModuleSearchCriteriaTypeDef"] = None

class SearchContactFlowModulesRequestSearchContactFlowModulesPaginateTypeDef(BaseModel):
    InstanceId: str
    SearchFilter: Optional[ContactFlowModuleSearchFilterTypeDef] = None
    SearchCriteria: Optional[ContactFlowModuleSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchContactFlowsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[ContactFlowSearchFilterTypeDef] = None
    SearchCriteria: Optional["ContactFlowSearchCriteriaTypeDef"] = None

class SearchContactFlowsRequestSearchContactFlowsPaginateTypeDef(BaseModel):
    InstanceId: str
    SearchFilter: Optional[ContactFlowSearchFilterTypeDef] = None
    SearchCriteria: Optional[ContactFlowSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchHoursOfOperationsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[HoursOfOperationSearchFilterTypeDef] = None
    SearchCriteria: Optional["HoursOfOperationSearchCriteriaTypeDef"] = None

class SearchHoursOfOperationsRequestSearchHoursOfOperationsPaginateTypeDef(BaseModel):
    InstanceId: str
    SearchFilter: Optional[HoursOfOperationSearchFilterTypeDef] = None
    SearchCriteria: Optional[HoursOfOperationSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchPromptsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[PromptSearchFilterTypeDef] = None
    SearchCriteria: Optional["PromptSearchCriteriaTypeDef"] = None

class SearchPromptsRequestSearchPromptsPaginateTypeDef(BaseModel):
    InstanceId: str
    SearchFilter: Optional[PromptSearchFilterTypeDef] = None
    SearchCriteria: Optional[PromptSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchQueuesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[QueueSearchFilterTypeDef] = None
    SearchCriteria: Optional["QueueSearchCriteriaTypeDef"] = None

class SearchQueuesRequestSearchQueuesPaginateTypeDef(BaseModel):
    InstanceId: str
    SearchFilter: Optional[QueueSearchFilterTypeDef] = None
    SearchCriteria: Optional[QueueSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchQuickConnectsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[QuickConnectSearchFilterTypeDef] = None
    SearchCriteria: Optional["QuickConnectSearchCriteriaTypeDef"] = None

class SearchQuickConnectsRequestSearchQuickConnectsPaginateTypeDef(BaseModel):
    InstanceId: str
    SearchFilter: Optional[QuickConnectSearchFilterTypeDef] = None
    SearchCriteria: Optional[QuickConnectSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchRoutingProfilesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[RoutingProfileSearchFilterTypeDef] = None
    SearchCriteria: Optional["RoutingProfileSearchCriteriaTypeDef"] = None

class SearchRoutingProfilesRequestSearchRoutingProfilesPaginateTypeDef(BaseModel):
    InstanceId: str
    SearchFilter: Optional[RoutingProfileSearchFilterTypeDef] = None
    SearchCriteria: Optional[RoutingProfileSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchSecurityProfilesRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchCriteria: Optional["SecurityProfileSearchCriteriaTypeDef"] = None
    SearchFilter: Optional[SecurityProfilesSearchFilterTypeDef] = None

class SearchSecurityProfilesRequestSearchSecurityProfilesPaginateTypeDef(BaseModel):
    InstanceId: str
    SearchCriteria: Optional[SecurityProfileSearchCriteriaTypeDef] = None
    SearchFilter: Optional[SecurityProfilesSearchFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ConnectionDataTypeDef(BaseModel):
    Attendee: Optional[AttendeeTypeDef] = None
    Meeting: Optional[MeetingTypeDef] = None

class DescribeRoutingProfileResponseTypeDef(BaseModel):
    RoutingProfile: RoutingProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchRoutingProfilesResponseTypeDef(BaseModel):
    RoutingProfiles: List[RoutingProfileTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCurrentMetricDataResponseTypeDef(BaseModel):
    MetricResults: List[CurrentMetricResultTypeDef]
    DataSnapshotTime: datetime
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateInstanceStorageConfigRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    StorageConfig: InstanceStorageConfigTypeDef

class DescribeInstanceStorageConfigResponseTypeDef(BaseModel):
    StorageConfig: InstanceStorageConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceStorageConfigsResponseTypeDef(BaseModel):
    StorageConfigs: List[InstanceStorageConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateInstanceStorageConfigRequestRequestTypeDef(BaseModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType
    StorageConfig: InstanceStorageConfigTypeDef

class EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef(BaseModel):
    Options: List[EvaluationFormSingleSelectQuestionOptionTypeDef]
    DisplayAs: Optional[EvaluationFormSingleSelectQuestionDisplayModeType] = None
    Automation: Optional[EvaluationFormSingleSelectQuestionAutomationOutputTypeDef] = None

class EvaluationFormSingleSelectQuestionPropertiesTypeDef(BaseModel):
    Options: Sequence[EvaluationFormSingleSelectQuestionOptionTypeDef]
    DisplayAs: Optional[EvaluationFormSingleSelectQuestionDisplayModeType] = None
    Automation: Optional[EvaluationFormSingleSelectQuestionAutomationTypeDef] = None

class DescribeContactEvaluationResponseTypeDef(BaseModel):
    Evaluation: EvaluationTypeDef
    EvaluationForm: EvaluationFormContentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ContactTypeDef(BaseModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    InitialContactId: Optional[str] = None
    PreviousContactId: Optional[str] = None
    InitiationMethod: Optional[ContactInitiationMethodType] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Channel: Optional[ChannelType] = None
    QueueInfo: Optional[QueueInfoTypeDef] = None
    AgentInfo: Optional[AgentInfoTypeDef] = None
    InitiationTimestamp: Optional[datetime] = None
    DisconnectTimestamp: Optional[datetime] = None
    LastUpdateTimestamp: Optional[datetime] = None
    LastPausedTimestamp: Optional[datetime] = None
    LastResumedTimestamp: Optional[datetime] = None
    TotalPauseCount: Optional[int] = None
    TotalPauseDurationInSeconds: Optional[int] = None
    ScheduledTimestamp: Optional[datetime] = None
    RelatedContactId: Optional[str] = None
    WisdomInfo: Optional[WisdomInfoTypeDef] = None
    QueueTimeAdjustmentSeconds: Optional[int] = None
    QueuePriority: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None
    ConnectedToSystemTimestamp: Optional[datetime] = None
    RoutingCriteria: Optional[RoutingCriteriaTypeDef] = None
    Customer: Optional[CustomerTypeDef] = None
    Campaign: Optional[CampaignTypeDef] = None
    AnsweringMachineDetectionStatus: Optional[AnsweringMachineDetectionStatusType] = None
    CustomerVoiceActivity: Optional[CustomerVoiceActivityTypeDef] = None
    QualityMetrics: Optional[QualityMetricsTypeDef] = None
    DisconnectDetails: Optional[DisconnectDetailsTypeDef] = None
    SegmentAttributes: Optional[Dict[str, SegmentAttributeValueTypeDef]] = None

class RuleActionOutputTypeDef(BaseModel):
    ActionType: ActionTypeType
    TaskAction: Optional[TaskActionDefinitionOutputTypeDef] = None
    EventBridgeAction: Optional[EventBridgeActionDefinitionTypeDef] = None
    AssignContactCategoryAction: Optional[Dict[str, Any]] = None
    SendNotificationAction: Optional[SendNotificationActionDefinitionOutputTypeDef] = None
    CreateCaseAction: Optional[CreateCaseActionDefinitionOutputTypeDef] = None
    UpdateCaseAction: Optional[UpdateCaseActionDefinitionOutputTypeDef] = None
    EndAssociatedTasksAction: Optional[Dict[str, Any]] = None
    SubmitAutoEvaluationAction: Optional[SubmitAutoEvaluationActionDefinitionTypeDef] = None

class RuleActionTypeDef(BaseModel):
    ActionType: ActionTypeType
    TaskAction: Optional[TaskActionDefinitionTypeDef] = None
    EventBridgeAction: Optional[EventBridgeActionDefinitionTypeDef] = None
    AssignContactCategoryAction: Optional[Mapping[str, Any]] = None
    SendNotificationAction: Optional[SendNotificationActionDefinitionTypeDef] = None
    CreateCaseAction: Optional[CreateCaseActionDefinitionTypeDef] = None
    UpdateCaseAction: Optional[UpdateCaseActionDefinitionTypeDef] = None
    EndAssociatedTasksAction: Optional[Mapping[str, Any]] = None
    SubmitAutoEvaluationAction: Optional[SubmitAutoEvaluationActionDefinitionTypeDef] = None

class GetCurrentUserDataResponseTypeDef(BaseModel):
    UserDataList: List[UserDataTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeUserHierarchyGroupResponseTypeDef(BaseModel):
    HierarchyGroup: HierarchyGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HistoricalMetricResultTypeDef(BaseModel):
    Dimensions: Optional[DimensionsTypeDef] = None
    Collections: Optional[List[HistoricalMetricDataTypeDef]] = None

class DescribeHoursOfOperationResponseTypeDef(BaseModel):
    HoursOfOperation: HoursOfOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchHoursOfOperationsResponseTypeDef(BaseModel):
    HoursOfOperations: List[HoursOfOperationTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTaskTemplateResponseTypeDef(BaseModel):
    InstanceId: str
    Id: str
    Arn: str
    Name: str
    Description: str
    ContactFlowId: str
    Constraints: TaskTemplateConstraintsOutputTypeDef
    Defaults: TaskTemplateDefaultsOutputTypeDef
    Fields: List[TaskTemplateFieldOutputTypeDef]
    Status: TaskTemplateStatusType
    LastModifiedTime: datetime
    CreatedTime: datetime
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTaskTemplateResponseTypeDef(BaseModel):
    InstanceId: str
    Id: str
    Arn: str
    Name: str
    Description: str
    ContactFlowId: str
    Constraints: TaskTemplateConstraintsOutputTypeDef
    Defaults: TaskTemplateDefaultsOutputTypeDef
    Fields: List[TaskTemplateFieldOutputTypeDef]
    Status: TaskTemplateStatusType
    LastModifiedTime: datetime
    CreatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskTemplateRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    Fields: Sequence[TaskTemplateFieldUnionTypeDef]
    Description: Optional[str] = None
    ContactFlowId: Optional[str] = None
    Constraints: Optional[TaskTemplateConstraintsTypeDef] = None
    Defaults: Optional[TaskTemplateDefaultsTypeDef] = None
    Status: Optional[TaskTemplateStatusType] = None
    ClientToken: Optional[str] = None

class UpdateTaskTemplateRequestRequestTypeDef(BaseModel):
    TaskTemplateId: str
    InstanceId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ContactFlowId: Optional[str] = None
    Constraints: Optional[TaskTemplateConstraintsTypeDef] = None
    Defaults: Optional[TaskTemplateDefaultsTypeDef] = None
    Status: Optional[TaskTemplateStatusType] = None
    Fields: Optional[Sequence[TaskTemplateFieldUnionTypeDef]] = None

class MetricResultV2TypeDef(BaseModel):
    Dimensions: Optional[Dict[str, str]] = None
    MetricInterval: Optional[MetricIntervalTypeDef] = None
    Collections: Optional[List[MetricDataV2TypeDef]] = None

class GetMetricDataV2RequestRequestTypeDef(BaseModel):
    ResourceArn: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Filters: Sequence[FilterV2TypeDef]
    Metrics: Sequence[MetricV2UnionTypeDef]
    Interval: Optional[IntervalDetailsTypeDef] = None
    Groupings: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class UpdateParticipantRoleConfigChannelInfoTypeDef(BaseModel):
    Chat: Optional[ChatParticipantRoleConfigTypeDef] = None

class DescribeQuickConnectResponseTypeDef(BaseModel):
    QuickConnect: QuickConnectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchQuickConnectsResponseTypeDef(BaseModel):
    QuickConnects: List[QuickConnectTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RealTimeContactAnalysisCategoryDetailsTypeDef(BaseModel):
    PointsOfInterest: List[RealTimeContactAnalysisPointOfInterestTypeDef]

class RealTimeContactAnalysisSegmentIssuesTypeDef(BaseModel):
    IssuesDetected: List[RealTimeContactAnalysisIssueDetectedTypeDef]

class SearchCriteriaTypeDef(BaseModel):
    AgentIds: Optional[Sequence[str]] = None
    AgentHierarchyGroups: Optional[AgentHierarchyGroupsTypeDef] = None
    Channels: Optional[Sequence[ChannelType]] = None
    ContactAnalysis: Optional[ContactAnalysisTypeDef] = None
    InitiationMethods: Optional[Sequence[ContactInitiationMethodType]] = None
    QueueIds: Optional[Sequence[str]] = None
    SearchableContactAttributes: Optional[SearchableContactAttributesTypeDef] = None

class SearchUsersRequestRequestTypeDef(BaseModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[UserSearchFilterTypeDef] = None
    SearchCriteria: Optional["UserSearchCriteriaTypeDef"] = None

class SearchUsersRequestSearchUsersPaginateTypeDef(BaseModel):
    InstanceId: str
    SearchFilter: Optional[UserSearchFilterTypeDef] = None
    SearchCriteria: Optional[UserSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class StartWebRTCContactResponseTypeDef(BaseModel):
    ConnectionData: ConnectionDataTypeDef
    ContactId: str
    ParticipantId: str
    ParticipantToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EvaluationFormQuestionTypePropertiesOutputTypeDef(BaseModel):
    Numeric: Optional[EvaluationFormNumericQuestionPropertiesOutputTypeDef] = None
    SingleSelect: Optional[EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef] = None

class EvaluationFormQuestionTypePropertiesTypeDef(BaseModel):
    Numeric: Optional[EvaluationFormNumericQuestionPropertiesTypeDef] = None
    SingleSelect: Optional[EvaluationFormSingleSelectQuestionPropertiesTypeDef] = None

class DescribeContactResponseTypeDef(BaseModel):
    Contact: ContactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RuleTypeDef(BaseModel):
    Name: str
    RuleId: str
    RuleArn: str
    TriggerEventSource: RuleTriggerEventSourceTypeDef
    Function: str
    Actions: List[RuleActionOutputTypeDef]
    PublishStatus: RulePublishStatusType
    CreatedTime: datetime
    LastUpdatedTime: datetime
    LastUpdatedBy: str
    Tags: Optional[Dict[str, str]] = None

class GetMetricDataResponseTypeDef(BaseModel):
    MetricResults: List[HistoricalMetricResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetMetricDataV2ResponseTypeDef(BaseModel):
    MetricResults: List[MetricResultV2TypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateParticipantRoleConfigRequestRequestTypeDef(BaseModel):
    InstanceId: str
    ContactId: str
    ChannelConfiguration: UpdateParticipantRoleConfigChannelInfoTypeDef

class RealTimeContactAnalysisSegmentCategoriesTypeDef(BaseModel):
    MatchedDetails: Dict[str, RealTimeContactAnalysisCategoryDetailsTypeDef]

class SearchContactsRequestRequestTypeDef(BaseModel):
    InstanceId: str
    TimeRange: SearchContactsTimeRangeTypeDef
    SearchCriteria: Optional[SearchCriteriaTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Sort: Optional[SortTypeDef] = None

class SearchContactsRequestSearchContactsPaginateTypeDef(BaseModel):
    InstanceId: str
    TimeRange: SearchContactsTimeRangeTypeDef
    SearchCriteria: Optional[SearchCriteriaTypeDef] = None
    Sort: Optional[SortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class EvaluationFormQuestionOutputTypeDef(BaseModel):
    Title: str
    RefId: str
    QuestionType: EvaluationFormQuestionTypeType
    Instructions: Optional[str] = None
    NotApplicableEnabled: Optional[bool] = None
    QuestionTypeProperties: Optional[EvaluationFormQuestionTypePropertiesOutputTypeDef] = None
    Weight: Optional[float] = None

class EvaluationFormQuestionTypeDef(BaseModel):
    Title: str
    RefId: str
    QuestionType: EvaluationFormQuestionTypeType
    Instructions: Optional[str] = None
    NotApplicableEnabled: Optional[bool] = None
    QuestionTypeProperties: Optional[EvaluationFormQuestionTypePropertiesTypeDef] = None
    Weight: Optional[float] = None

class DescribeRuleResponseTypeDef(BaseModel):
    Rule: RuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleRequestRequestTypeDef(BaseModel):
    InstanceId: str
    Name: str
    TriggerEventSource: RuleTriggerEventSourceTypeDef
    Function: str
    Actions: Sequence[RuleActionUnionTypeDef]
    PublishStatus: RulePublishStatusType
    ClientToken: Optional[str] = None

class UpdateRuleRequestRequestTypeDef(BaseModel):
    RuleId: str
    InstanceId: str
    Name: str
    Function: str
    Actions: Sequence[RuleActionUnionTypeDef]
    PublishStatus: RulePublishStatusType

class RealtimeContactAnalysisSegmentTypeDef(BaseModel):
    Transcript: Optional[RealTimeContactAnalysisSegmentTranscriptTypeDef] = None
    Categories: Optional[RealTimeContactAnalysisSegmentCategoriesTypeDef] = None
    Issues: Optional[RealTimeContactAnalysisSegmentIssuesTypeDef] = None
    Event: Optional[RealTimeContactAnalysisSegmentEventTypeDef] = None
    Attachments: Optional[RealTimeContactAnalysisSegmentAttachmentsTypeDef] = None

class EvaluationFormItemOutputTypeDef(BaseModel):
    Section: Optional[Dict[str, Any]] = None
    Question: Optional[EvaluationFormQuestionOutputTypeDef] = None

class EvaluationFormItemTypeDef(BaseModel):
    Section: Optional[Dict[str, Any]] = None
    Question: Optional[EvaluationFormQuestionTypeDef] = None

class ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef(BaseModel):
    Channel: RealTimeContactAnalysisSupportedChannelType
    Status: RealTimeContactAnalysisStatusType
    Segments: List[RealtimeContactAnalysisSegmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

