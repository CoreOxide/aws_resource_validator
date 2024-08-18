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
from aws_resource_validator.pydantic_models.connect_constants import *

class ActionSummaryTypeDef(BaseValidatorModel):
    ActionType: ActionTypeType

class ActivateEvaluationFormRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class DistributionTypeDef(BaseValidatorModel):
    Region: str
    Percentage: int

class QueueReferenceTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None

class AgentHierarchyGroupTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None

class AgentHierarchyGroupsTypeDef(BaseValidatorModel):
    L1Ids: Optional[Sequence[str]] = None
    L2Ids: Optional[Sequence[str]] = None
    L3Ids: Optional[Sequence[str]] = None
    L4Ids: Optional[Sequence[str]] = None
    L5Ids: Optional[Sequence[str]] = None

class DeviceInfoTypeDef(BaseValidatorModel):
    PlatformName: Optional[str] = None
    PlatformVersion: Optional[str] = None
    OperatingSystem: Optional[str] = None

class ParticipantCapabilitiesTypeDef(BaseValidatorModel):
    Video: Optional[Literal["SEND"]] = None

class AudioQualityMetricsInfoTypeDef(BaseValidatorModel):
    QualityScore: Optional[float] = None
    PotentialQualityIssues: Optional[List[str]] = None

class AgentStatusReferenceTypeDef(BaseValidatorModel):
    StatusStartTimestamp: Optional[datetime] = None
    StatusArn: Optional[str] = None
    StatusName: Optional[str] = None

class AgentStatusSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[AgentStatusTypeType] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class AgentStatusTypeDef(BaseValidatorModel):
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

class AgentsCriteriaTypeDef(BaseValidatorModel):
    AgentIds: Optional[List[str]] = None

class AnalyticsDataAssociationResultTypeDef(BaseValidatorModel):
    DataSetId: Optional[str] = None
    TargetAccountId: Optional[str] = None
    ResourceShareId: Optional[str] = None
    ResourceShareArn: Optional[str] = None

class AnswerMachineDetectionConfigTypeDef(BaseValidatorModel):
    EnableAnswerMachineDetection: Optional[bool] = None
    AwaitAnswerMachinePrompt: Optional[bool] = None

class ApplicationExtraOutputTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    ApplicationPermissions: Optional[List[str]] = None

class ApplicationOutputTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    ApplicationPermissions: Optional[List[str]] = None

class ApplicationTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    ApplicationPermissions: Optional[Sequence[str]] = None

class AssociateAnalyticsDataSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DataSetId: str
    TargetAccountId: Optional[str] = None

class AssociateApprovedOriginRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Origin: str

class LexBotTypeDef(BaseValidatorModel):
    Name: str
    LexRegion: str

class LexV2BotTypeDef(BaseValidatorModel):
    AliasArn: Optional[str] = None

class AssociateDefaultVocabularyRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LanguageCode: VocabularyLanguageCodeType
    VocabularyId: Optional[str] = None

class AssociateFlowRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceId: str
    FlowId: str
    ResourceType: Literal["SMS_PHONE_NUMBER"]

class AssociateLambdaFunctionRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FunctionArn: str

class AssociatePhoneNumberContactFlowRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    InstanceId: str
    ContactFlowId: str

class AssociateQueueQuickConnectsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    QuickConnectIds: Sequence[str]

class AssociateSecurityKeyRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Key: str

class AssociateTrafficDistributionGroupUserRequestRequestTypeDef(BaseValidatorModel):
    TrafficDistributionGroupId: str
    UserId: str
    InstanceId: str

class UserProficiencyTypeDef(BaseValidatorModel):
    AttributeName: str
    AttributeValue: str
    Level: float

class AttachedFileErrorTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None
    FileId: Optional[str] = None

class CreatedByInfoTypeDef(BaseValidatorModel):
    ConnectUserArn: Optional[str] = None
    AWSIdentityArn: Optional[str] = None

class AttachmentReferenceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    Status: Optional[ReferenceStatusType] = None

class AttendeeTypeDef(BaseValidatorModel):
    AttendeeId: Optional[str] = None
    JoinToken: Optional[str] = None

class HierarchyGroupConditionTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    HierarchyGroupMatchType: Optional[HierarchyGroupMatchTypeType] = None

class TagConditionTypeDef(BaseValidatorModel):
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None

class AttributeTypeDef(BaseValidatorModel):
    AttributeType: Optional[InstanceAttributeTypeType] = None
    Value: Optional[str] = None

class AudioFeaturesTypeDef(BaseValidatorModel):
    EchoReduction: Optional[MeetingFeatureStatusType] = None

class AuthenticationProfileSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    IsDefault: Optional[bool] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class AuthenticationProfileTypeDef(BaseValidatorModel):
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

class AvailableNumberSummaryTypeDef(BaseValidatorModel):
    PhoneNumber: Optional[str] = None
    PhoneNumberCountryCode: Optional[PhoneNumberCountryCodeType] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None

class BatchAssociateAnalyticsDataSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DataSetIds: Sequence[str]
    TargetAccountId: Optional[str] = None

class ErrorResultTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class BatchDisassociateAnalyticsDataSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DataSetIds: Sequence[str]
    TargetAccountId: Optional[str] = None

class BatchGetAttachedFileMetadataRequestRequestTypeDef(BaseValidatorModel):
    FileIds: Sequence[str]
    InstanceId: str
    AssociatedResourceArn: str

class BatchGetFlowAssociationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceIds: Sequence[str]
    ResourceType: Optional[Literal["VOICE_PHONE_NUMBER"]] = None

class FlowAssociationSummaryTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    FlowId: Optional[str] = None
    ResourceType: Optional[Literal["VOICE_PHONE_NUMBER"]] = None

class FailedRequestTypeDef(BaseValidatorModel):
    RequestIdentifier: Optional[str] = None
    FailureReasonCode: Optional[FailureReasonCodeType] = None
    FailureReasonMessage: Optional[str] = None

class SuccessfulRequestTypeDef(BaseValidatorModel):
    RequestIdentifier: Optional[str] = None
    ContactId: Optional[str] = None

class CampaignTypeDef(BaseValidatorModel):
    CampaignId: Optional[str] = None

class ChatEventTypeDef(BaseValidatorModel):
    Type: ChatEventTypeType
    ContentType: Optional[str] = None
    Content: Optional[str] = None

class ChatMessageTypeDef(BaseValidatorModel):
    ContentType: str
    Content: str

class ChatStreamingConfigurationTypeDef(BaseValidatorModel):
    StreamingEndpointArn: str

class ClaimPhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumber: str
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberDescription: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None

class PhoneNumberStatusTypeDef(BaseValidatorModel):
    Status: Optional[PhoneNumberWorkflowStatusType] = None
    Message: Optional[str] = None

class CompleteAttachedFileUploadRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str

class EndpointTypeDef(BaseValidatorModel):
    Type: Optional[EndpointTypeType] = None
    Address: Optional[str] = None

class ContactFilterTypeDef(BaseValidatorModel):
    ContactStates: Optional[Sequence[ContactStateType]] = None

class StringConditionTypeDef(BaseValidatorModel):
    FieldName: Optional[str] = None
    Value: Optional[str] = None
    ComparisonType: Optional[StringComparisonTypeType] = None

class ContactFlowModuleSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    State: Optional[ContactFlowModuleStateType] = None

class ContactFlowModuleTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Content: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[ContactFlowModuleStateType] = None
    Status: Optional[ContactFlowModuleStatusType] = None
    Tags: Optional[Dict[str, str]] = None

class ContactFlowSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    ContactFlowType: Optional[ContactFlowTypeType] = None
    ContactFlowState: Optional[ContactFlowStateType] = None
    ContactFlowStatus: Optional[ContactFlowStatusType] = None

class ContactFlowTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ContactFlowTypeType] = None
    State: Optional[ContactFlowStateType] = None
    Status: Optional[ContactFlowStatusType] = None
    Description: Optional[str] = None
    Content: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class ContactSearchSummaryAgentInfoTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ConnectedToAgentTimestamp: Optional[datetime] = None

class ContactSearchSummaryQueueInfoTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    EnqueueTimestamp: Optional[datetime] = None

class CustomerVoiceActivityTypeDef(BaseValidatorModel):
    GreetingStartTimestamp: Optional[datetime] = None
    GreetingEndTimestamp: Optional[datetime] = None

class DisconnectDetailsTypeDef(BaseValidatorModel):
    PotentialDisconnectIssue: Optional[str] = None

class QueueInfoTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    EnqueueTimestamp: Optional[datetime] = None

class SegmentAttributeValueTypeDef(BaseValidatorModel):
    ValueString: Optional[str] = None

class WisdomInfoTypeDef(BaseValidatorModel):
    SessionArn: Optional[str] = None

class CreateAgentStatusRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    State: AgentStatusStateType
    Description: Optional[str] = None
    DisplayOrder: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateContactFlowModuleRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    Content: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None

class CreateContactFlowRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    Type: ContactFlowTypeType
    Content: str
    Description: Optional[str] = None
    Status: Optional[ContactFlowStatusType] = None
    Tags: Optional[Mapping[str, str]] = None

class EvaluationFormScoringStrategyTypeDef(BaseValidatorModel):
    Mode: EvaluationFormScoringModeType
    Status: EvaluationFormScoringStatusType

class CreateInstanceRequestRequestTypeDef(BaseValidatorModel):
    IdentityManagementType: DirectoryTypeType
    InboundCallsEnabled: bool
    OutboundCallsEnabled: bool
    ClientToken: Optional[str] = None
    InstanceAlias: Optional[str] = None
    DirectoryId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateIntegrationAssociationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationType: IntegrationTypeType
    IntegrationArn: str
    SourceApplicationUrl: Optional[str] = None
    SourceApplicationName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Tags: Optional[Mapping[str, str]] = None

class ParticipantDetailsToAddTypeDef(BaseValidatorModel):
    ParticipantRole: Optional[ParticipantRoleType] = None
    DisplayName: Optional[str] = None

class ParticipantTokenCredentialsTypeDef(BaseValidatorModel):
    ParticipantToken: Optional[str] = None
    Expiry: Optional[str] = None

class CreatePersistentContactAssociationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    InitialContactId: str
    RehydrationType: RehydrationTypeType
    SourceContactId: str
    ClientToken: Optional[str] = None

class PredefinedAttributeValuesTypeDef(BaseValidatorModel):
    StringList: Optional[Sequence[str]] = None

class CreatePromptRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    S3Uri: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class OutboundCallerConfigTypeDef(BaseValidatorModel):
    OutboundCallerIdName: Optional[str] = None
    OutboundCallerIdNumberId: Optional[str] = None
    OutboundFlowId: Optional[str] = None

class RuleTriggerEventSourceTypeDef(BaseValidatorModel):
    EventSourceName: EventSourceNameType
    IntegrationAssociationId: Optional[str] = None

class CreateTrafficDistributionGroupRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    InstanceId: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CreateUseCaseRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    UseCaseType: UseCaseTypeType
    Tags: Optional[Mapping[str, str]] = None

class CreateUserHierarchyGroupRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    InstanceId: str
    ParentGroupId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UserIdentityInfoTypeDef(BaseValidatorModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None
    Email: Optional[str] = None
    SecondaryEmail: Optional[str] = None
    Mobile: Optional[str] = None

class UserPhoneConfigTypeDef(BaseValidatorModel):
    PhoneType: PhoneTypeType
    AutoAccept: Optional[bool] = None
    AfterContactWorkTimeLimit: Optional[int] = None
    DeskPhoneNumber: Optional[str] = None

class ViewInputContentTypeDef(BaseValidatorModel):
    Template: Optional[str] = None
    Actions: Optional[Sequence[str]] = None

class CreateViewVersionRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    VersionDescription: Optional[str] = None
    ViewContentSha256: Optional[str] = None

class CreateVocabularyRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    VocabularyName: str
    LanguageCode: VocabularyLanguageCodeType
    Content: str
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class CredentialsTypeDef(BaseValidatorModel):
    AccessToken: Optional[str] = None
    AccessTokenExpiration: Optional[datetime] = None
    RefreshToken: Optional[str] = None
    RefreshTokenExpiration: Optional[datetime] = None

class CrossChannelBehaviorTypeDef(BaseValidatorModel):
    BehaviorType: BehaviorTypeType

class CurrentMetricTypeDef(BaseValidatorModel):
    Name: Optional[CurrentMetricNameType] = None
    Unit: Optional[UnitType] = None

class CurrentMetricSortCriteriaTypeDef(BaseValidatorModel):
    SortByMetric: Optional[CurrentMetricNameType] = None
    SortOrder: Optional[SortOrderType] = None

class DateReferenceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class DeactivateEvaluationFormRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int

class DefaultVocabularyTypeDef(BaseValidatorModel):
    InstanceId: str
    LanguageCode: VocabularyLanguageCodeType
    VocabularyId: str
    VocabularyName: str

class DeleteAttachedFileRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str

class DeleteContactEvaluationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str

class DeleteContactFlowModuleRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleId: str

class DeleteContactFlowRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str

class DeleteEvaluationFormRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: Optional[int] = None

class DeleteHoursOfOperationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str

class DeleteInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str

class DeleteIntegrationAssociationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str

class DeletePredefinedAttributeRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str

class DeletePromptRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    PromptId: str

class DeleteQueueRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str

class DeleteQuickConnectRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str

class DeleteRoutingProfileRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str

class DeleteRuleRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RuleId: str

class DeleteSecurityProfileRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    SecurityProfileId: str

class DeleteTaskTemplateRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    TaskTemplateId: str

class DeleteTrafficDistributionGroupRequestRequestTypeDef(BaseValidatorModel):
    TrafficDistributionGroupId: str

class DeleteUseCaseRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    UseCaseId: str

class DeleteUserHierarchyGroupRequestRequestTypeDef(BaseValidatorModel):
    HierarchyGroupId: str
    InstanceId: str

class DeleteUserRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    UserId: str

class DeleteViewRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str

class DeleteViewVersionRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    ViewVersion: int

class DeleteVocabularyRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    VocabularyId: str

class DescribeAgentStatusRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AgentStatusId: str

class DescribeAuthenticationProfileRequestRequestTypeDef(BaseValidatorModel):
    AuthenticationProfileId: str
    InstanceId: str

class DescribeContactEvaluationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str

class DescribeContactFlowModuleRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleId: str

class DescribeContactFlowRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str

class DescribeContactRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str

class DescribeEvaluationFormRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: Optional[int] = None

class DescribeHoursOfOperationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str

class DescribeInstanceAttributeRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AttributeType: InstanceAttributeTypeType

class DescribeInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str

class DescribeInstanceStorageConfigRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType

class DescribePhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str

class DescribePredefinedAttributeRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str

class DescribePromptRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    PromptId: str

class PromptTypeDef(BaseValidatorModel):
    PromptARN: Optional[str] = None
    PromptId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class DescribeQueueRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str

class DescribeQuickConnectRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str

class DescribeRoutingProfileRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str

class DescribeRuleRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RuleId: str

class DescribeSecurityProfileRequestRequestTypeDef(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str

class SecurityProfileTypeDef(BaseValidatorModel):
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

class DescribeTrafficDistributionGroupRequestRequestTypeDef(BaseValidatorModel):
    TrafficDistributionGroupId: str

class TrafficDistributionGroupTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    InstanceArn: Optional[str] = None
    Status: Optional[TrafficDistributionGroupStatusType] = None
    Tags: Optional[Dict[str, str]] = None
    IsDefault: Optional[bool] = None

class DescribeUserHierarchyGroupRequestRequestTypeDef(BaseValidatorModel):
    HierarchyGroupId: str
    InstanceId: str

class DescribeUserHierarchyStructureRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str

class DescribeUserRequestRequestTypeDef(BaseValidatorModel):
    UserId: str
    InstanceId: str

class DescribeViewRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str

class DescribeVocabularyRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    VocabularyId: str

class VocabularyTypeDef(BaseValidatorModel):
    Name: str
    Id: str
    Arn: str
    LanguageCode: VocabularyLanguageCodeType
    State: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: Optional[str] = None
    Content: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class RoutingProfileReferenceTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None

class DisassociateAnalyticsDataSetRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DataSetId: str
    TargetAccountId: Optional[str] = None

class DisassociateApprovedOriginRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Origin: str

class DisassociateFlowRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceId: str
    ResourceType: Literal["SMS_PHONE_NUMBER"]

class DisassociateInstanceStorageConfigRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType

class DisassociateLambdaFunctionRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FunctionArn: str

class DisassociateLexBotRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    BotName: str
    LexRegion: str

class DisassociatePhoneNumberContactFlowRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    InstanceId: str

class DisassociateQueueQuickConnectsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    QuickConnectIds: Sequence[str]

class RoutingProfileQueueReferenceTypeDef(BaseValidatorModel):
    QueueId: str
    Channel: ChannelType

class DisassociateSecurityKeyRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AssociationId: str

class DisassociateTrafficDistributionGroupUserRequestRequestTypeDef(BaseValidatorModel):
    TrafficDistributionGroupId: str
    UserId: str
    InstanceId: str

class UserProficiencyDisassociateTypeDef(BaseValidatorModel):
    AttributeName: str
    AttributeValue: str

class DisconnectReasonTypeDef(BaseValidatorModel):
    Code: Optional[str] = None

class DismissUserContactRequestRequestTypeDef(BaseValidatorModel):
    UserId: str
    InstanceId: str
    ContactId: str

class DownloadUrlMetadataTypeDef(BaseValidatorModel):
    Url: Optional[str] = None
    UrlExpiry: Optional[str] = None

class EmailReferenceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class EncryptionConfigTypeDef(BaseValidatorModel):
    EncryptionType: Literal["KMS"]
    KeyId: str

class EvaluationAnswerDataTypeDef(BaseValidatorModel):
    StringValue: Optional[str] = None
    NumericValue: Optional[float] = None
    NotApplicable: Optional[bool] = None

class NumericQuestionPropertyValueAutomationTypeDef(BaseValidatorModel):
    Label: NumericQuestionPropertyAutomationLabelType

class EvaluationFormNumericQuestionOptionTypeDef(BaseValidatorModel):
    MinValue: int
    MaxValue: int
    Score: Optional[int] = None
    AutomaticFail: Optional[bool] = None

class EvaluationFormSectionOutputTypeDef(BaseValidatorModel):
    Title: str
    RefId: str
    Items: List["EvaluationFormItemOutputTypeDef"]
    Instructions: Optional[str] = None
    Weight: Optional[float] = None

class EvaluationFormSectionTypeDef(BaseValidatorModel):
    Title: str
    RefId: str
    Items: Sequence["EvaluationFormItemTypeDef"]
    Instructions: Optional[str] = None
    Weight: Optional[float] = None

class SingleSelectQuestionRuleCategoryAutomationTypeDef(BaseValidatorModel):
    Category: str
    Condition: SingleSelectQuestionRuleCategoryAutomationConditionType
    OptionRefId: str

class EvaluationFormSingleSelectQuestionOptionTypeDef(BaseValidatorModel):
    RefId: str
    Text: str
    Score: Optional[int] = None
    AutomaticFail: Optional[bool] = None

class EvaluationFormSummaryTypeDef(BaseValidatorModel):
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

class EvaluationFormVersionSummaryTypeDef(BaseValidatorModel):
    EvaluationFormArn: str
    EvaluationFormId: str
    EvaluationFormVersion: int
    Locked: bool
    Status: EvaluationFormVersionStatusType
    CreatedTime: datetime
    CreatedBy: str
    LastModifiedTime: datetime
    LastModifiedBy: str

class EvaluationScoreTypeDef(BaseValidatorModel):
    Percentage: Optional[float] = None
    NotApplicable: Optional[bool] = None
    AutomaticFail: Optional[bool] = None

class EvaluationNoteTypeDef(BaseValidatorModel):
    Value: Optional[str] = None

class EventBridgeActionDefinitionTypeDef(BaseValidatorModel):
    Name: str

class ExpiryTypeDef(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None
    ExpiryTimestamp: Optional[datetime] = None

class FieldValueUnionOutputTypeDef(BaseValidatorModel):
    BooleanValue: Optional[bool] = None
    DoubleValue: Optional[float] = None
    EmptyValue: Optional[Dict[str, Any]] = None
    StringValue: Optional[str] = None

class FieldValueUnionTypeDef(BaseValidatorModel):
    BooleanValue: Optional[bool] = None
    DoubleValue: Optional[float] = None
    EmptyValue: Optional[Mapping[str, Any]] = None
    StringValue: Optional[str] = None

class FilterV2TypeDef(BaseValidatorModel):
    FilterKey: Optional[str] = None
    FilterValues: Optional[Sequence[str]] = None

class FiltersTypeDef(BaseValidatorModel):
    Queues: Optional[Sequence[str]] = None
    Channels: Optional[Sequence[ChannelType]] = None
    RoutingProfiles: Optional[Sequence[str]] = None
    RoutingStepExpressions: Optional[Sequence[str]] = None

class GetAttachedFileRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str
    UrlExpiryInSeconds: Optional[int] = None

class GetContactAttributesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    InitialContactId: str

class GetFederationTokenRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str

class GetFlowAssociationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceId: str
    ResourceType: Literal["SMS_PHONE_NUMBER"]

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class IntervalDetailsTypeDef(BaseValidatorModel):
    TimeZone: Optional[str] = None
    IntervalPeriod: Optional[IntervalPeriodType] = None

class GetPromptFileRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    PromptId: str

class GetTaskTemplateRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    TaskTemplateId: str
    SnapshotVersion: Optional[str] = None

class GetTrafficDistributionRequestRequestTypeDef(BaseValidatorModel):
    Id: str

class HierarchyGroupSummaryReferenceTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None

class HierarchyGroupSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class HierarchyLevelTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class HierarchyLevelUpdateTypeDef(BaseValidatorModel):
    Name: str

class ThresholdTypeDef(BaseValidatorModel):
    Comparison: Optional[Literal["LT"]] = None
    ThresholdValue: Optional[float] = None

class HoursOfOperationTimeSliceTypeDef(BaseValidatorModel):
    Hours: int
    Minutes: int

class HoursOfOperationSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ImportPhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    SourcePhoneNumberArn: str
    PhoneNumberDescription: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None

class InstanceStatusReasonTypeDef(BaseValidatorModel):
    Message: Optional[str] = None

class KinesisFirehoseConfigTypeDef(BaseValidatorModel):
    FirehoseArn: str

class KinesisStreamConfigTypeDef(BaseValidatorModel):
    StreamArn: str

class InstanceSummaryTypeDef(BaseValidatorModel):
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

class IntegrationAssociationSummaryTypeDef(BaseValidatorModel):
    IntegrationAssociationId: Optional[str] = None
    IntegrationAssociationArn: Optional[str] = None
    InstanceId: Optional[str] = None
    IntegrationType: Optional[IntegrationTypeType] = None
    IntegrationArn: Optional[str] = None
    SourceApplicationUrl: Optional[str] = None
    SourceApplicationName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None

class TaskTemplateFieldIdentifierTypeDef(BaseValidatorModel):
    Name: Optional[str] = None

class ListAgentStatusRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AgentStatusTypes: Optional[Sequence[AgentStatusTypeType]] = None

class ListAnalyticsDataAssociationsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DataSetId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListApprovedOriginsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAuthenticationProfilesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListBotsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LexVersion: LexVersionType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListContactEvaluationsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    NextToken: Optional[str] = None

class ListContactFlowModulesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ContactFlowModuleState: Optional[ContactFlowModuleStateType] = None

class ListContactFlowsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowTypes: Optional[Sequence[ContactFlowTypeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListContactReferencesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ReferenceTypes: Sequence[ReferenceTypeType]
    NextToken: Optional[str] = None

class ListDefaultVocabulariesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LanguageCode: Optional[VocabularyLanguageCodeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListEvaluationFormVersionsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListEvaluationFormsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListFlowAssociationsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceType: Optional[Literal["VOICE_PHONE_NUMBER"]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListHoursOfOperationsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListInstanceAttributesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListInstanceStorageConfigsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListInstancesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListIntegrationAssociationsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationType: Optional[IntegrationTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IntegrationArn: Optional[str] = None

class ListLambdaFunctionsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListLexBotsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPhoneNumbersRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PhoneNumberSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    PhoneNumberCountryCode: Optional[PhoneNumberCountryCodeType] = None

class ListPhoneNumbersSummaryTypeDef(BaseValidatorModel):
    PhoneNumberId: Optional[str] = None
    PhoneNumberArn: Optional[str] = None
    PhoneNumber: Optional[str] = None
    PhoneNumberCountryCode: Optional[PhoneNumberCountryCodeType] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberDescription: Optional[str] = None
    SourcePhoneNumberArn: Optional[str] = None

class ListPhoneNumbersV2RequestRequestTypeDef(BaseValidatorModel):
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberPrefix: Optional[str] = None

class ListPredefinedAttributesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PredefinedAttributeSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListPromptsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class PromptSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListQueueQuickConnectsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class QuickConnectSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    QuickConnectType: Optional[QuickConnectTypeType] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListQueuesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueTypes: Optional[Sequence[QueueTypeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class QueueSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    QueueType: Optional[QueueTypeType] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListQuickConnectsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuickConnectTypes: Optional[Sequence[QuickConnectTypeType]] = None

class ListRealtimeContactAnalysisSegmentsV2RequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    OutputType: RealTimeContactAnalysisOutputTypeType
    SegmentTypes: Sequence[RealTimeContactAnalysisSegmentTypeType]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRoutingProfileQueuesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RoutingProfileQueueConfigSummaryTypeDef(BaseValidatorModel):
    QueueId: str
    QueueArn: str
    QueueName: str
    Priority: int
    Delay: int
    Channel: ChannelType

class ListRoutingProfilesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class RoutingProfileSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListRulesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    PublishStatus: Optional[RulePublishStatusType] = None
    EventSourceName: Optional[EventSourceNameType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSecurityKeysRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SecurityKeyTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    Key: Optional[str] = None
    CreationTime: Optional[datetime] = None

class ListSecurityProfileApplicationsRequestRequestTypeDef(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListSecurityProfilePermissionsRequestRequestTypeDef(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListSecurityProfilesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SecurityProfileSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class ListTaskTemplatesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    Status: Optional[TaskTemplateStatusType] = None
    Name: Optional[str] = None

class TaskTemplateMetadataTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Status: Optional[TaskTemplateStatusType] = None
    LastModifiedTime: Optional[datetime] = None
    CreatedTime: Optional[datetime] = None

class ListTrafficDistributionGroupUsersRequestRequestTypeDef(BaseValidatorModel):
    TrafficDistributionGroupId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class TrafficDistributionGroupUserSummaryTypeDef(BaseValidatorModel):
    UserId: Optional[str] = None

class ListTrafficDistributionGroupsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    InstanceId: Optional[str] = None

class TrafficDistributionGroupSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    InstanceArn: Optional[str] = None
    Status: Optional[TrafficDistributionGroupStatusType] = None
    IsDefault: Optional[bool] = None

class ListUseCasesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class UseCaseTypeDef(BaseValidatorModel):
    UseCaseId: Optional[str] = None
    UseCaseArn: Optional[str] = None
    UseCaseType: Optional[UseCaseTypeType] = None

class ListUserHierarchyGroupsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListUserProficienciesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    UserId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListUsersRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class UserSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Username: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class ListViewVersionsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ViewVersionSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ViewTypeType] = None
    Version: Optional[int] = None
    VersionDescription: Optional[str] = None

class ListViewsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Type: Optional[ViewTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ViewSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ViewTypeType] = None
    Status: Optional[ViewStatusType] = None
    Description: Optional[str] = None

class MediaPlacementTypeDef(BaseValidatorModel):
    AudioHostUrl: Optional[str] = None
    AudioFallbackUrl: Optional[str] = None
    SignalingUrl: Optional[str] = None
    TurnControlUrl: Optional[str] = None
    EventIngestionUrl: Optional[str] = None

class MetricFilterV2OutputTypeDef(BaseValidatorModel):
    MetricFilterKey: Optional[str] = None
    MetricFilterValues: Optional[List[str]] = None
    Negate: Optional[bool] = None

class MetricFilterV2TypeDef(BaseValidatorModel):
    MetricFilterKey: Optional[str] = None
    MetricFilterValues: Optional[Sequence[str]] = None
    Negate: Optional[bool] = None

class MetricIntervalTypeDef(BaseValidatorModel):
    Interval: Optional[IntervalPeriodType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None

class ThresholdV2TypeDef(BaseValidatorModel):
    Comparison: Optional[str] = None
    ThresholdValue: Optional[float] = None

class MonitorContactRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    UserId: str
    AllowedMonitorCapabilities: Optional[Sequence[MonitorCapabilityType]] = None
    ClientToken: Optional[str] = None

class ParticipantDetailsTypeDef(BaseValidatorModel):
    DisplayName: str

class NotificationRecipientTypeOutputTypeDef(BaseValidatorModel):
    UserTags: Optional[Dict[str, str]] = None
    UserIds: Optional[List[str]] = None

class NotificationRecipientTypeTypeDef(BaseValidatorModel):
    UserTags: Optional[Mapping[str, str]] = None
    UserIds: Optional[Sequence[str]] = None

class NumberReferenceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class ParticipantTimerValueTypeDef(BaseValidatorModel):
    ParticipantTimerAction: Optional[Literal["Unset"]] = None
    ParticipantTimerDurationInMinutes: Optional[int] = None

class PauseContactRequestRequestTypeDef(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    ContactFlowId: Optional[str] = None

class PersistentChatTypeDef(BaseValidatorModel):
    RehydrationType: Optional[RehydrationTypeType] = None
    SourceContactId: Optional[str] = None

class PhoneNumberQuickConnectConfigTypeDef(BaseValidatorModel):
    PhoneNumber: str

class PredefinedAttributeValuesOutputTypeDef(BaseValidatorModel):
    StringList: Optional[List[str]] = None

class PredefinedAttributeValuesExtraOutputTypeDef(BaseValidatorModel):
    StringList: Optional[List[str]] = None

class PutUserStatusRequestRequestTypeDef(BaseValidatorModel):
    UserId: str
    InstanceId: str
    AgentStatusId: str

class QueueQuickConnectConfigTypeDef(BaseValidatorModel):
    QueueId: str
    ContactFlowId: str

class UserQuickConnectConfigTypeDef(BaseValidatorModel):
    UserId: str
    ContactFlowId: str

class RealTimeContactAnalysisAttachmentTypeDef(BaseValidatorModel):
    AttachmentName: str
    AttachmentId: str
    ContentType: Optional[str] = None
    Status: Optional[ArtifactStatusType] = None

class RealTimeContactAnalysisCharacterIntervalTypeDef(BaseValidatorModel):
    BeginOffsetChar: int
    EndOffsetChar: int

class RealTimeContactAnalysisTimeDataTypeDef(BaseValidatorModel):
    AbsoluteTime: Optional[datetime] = None

class StringReferenceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class UrlReferenceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None

class ReferenceTypeDef(BaseValidatorModel):
    Value: str
    Type: ReferenceTypeType

class ReleasePhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    ClientToken: Optional[str] = None

class ReplicateInstanceRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ReplicaRegion: str
    ReplicaAlias: str
    ClientToken: Optional[str] = None

class TagSearchConditionTypeDef(BaseValidatorModel):
    tagKey: Optional[str] = None
    tagValue: Optional[str] = None
    tagKeyComparisonType: Optional[StringComparisonTypeType] = None
    tagValueComparisonType: Optional[StringComparisonTypeType] = None

class ResumeContactRecordingRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str

class ResumeContactRequestRequestTypeDef(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    ContactFlowId: Optional[str] = None

class SubmitAutoEvaluationActionDefinitionTypeDef(BaseValidatorModel):
    EvaluationFormId: str

class SearchAvailablePhoneNumbersRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberCountryCode: PhoneNumberCountryCodeType
    PhoneNumberType: PhoneNumberTypeType
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberPrefix: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SortTypeDef(BaseValidatorModel):
    FieldName: SortableFieldNameType
    Order: SortOrderType

class SearchPredefinedAttributesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchCriteria: Optional["PredefinedAttributeSearchCriteriaTypeDef"] = None

class TagSetTypeDef(BaseValidatorModel):
    key: Optional[str] = None
    value: Optional[str] = None

class SecurityProfileSearchSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    OrganizationResourceId: Optional[str] = None
    Arn: Optional[str] = None
    SecurityProfileName: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None

class SearchVocabulariesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    State: Optional[VocabularyStateType] = None
    NameStartsWith: Optional[str] = None
    LanguageCode: Optional[VocabularyLanguageCodeType] = None

class VocabularySummaryTypeDef(BaseValidatorModel):
    Name: str
    Id: str
    Arn: str
    LanguageCode: VocabularyLanguageCodeType
    State: VocabularyStateType
    LastModifiedTime: datetime
    FailureReason: Optional[str] = None

class SearchableContactAttributesCriteriaTypeDef(BaseValidatorModel):
    Key: str
    Values: Sequence[str]

class SignInDistributionTypeDef(BaseValidatorModel):
    Region: str
    Enabled: bool

class UploadUrlMetadataTypeDef(BaseValidatorModel):
    Url: Optional[str] = None
    UrlExpiry: Optional[str] = None
    HeadersToInclude: Optional[Dict[str, str]] = None

class StartContactEvaluationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    EvaluationFormId: str
    ClientToken: Optional[str] = None

class VoiceRecordingConfigurationTypeDef(BaseValidatorModel):
    VoiceRecordingTrack: Optional[VoiceRecordingTrackType] = None

class StopContactRecordingRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str

class StopContactStreamingRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    StreamingId: str

class SuspendContactRecordingRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str

class TagContactRequestRequestTypeDef(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    Tags: Mapping[str, str]

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class TranscriptCriteriaTypeDef(BaseValidatorModel):
    ParticipantRole: ParticipantRoleType
    SearchText: Sequence[str]
    MatchType: SearchContactsMatchTypeType

class TransferContactRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ContactFlowId: str
    QueueId: Optional[str] = None
    UserId: Optional[str] = None
    ClientToken: Optional[str] = None

class UntagContactRequestRequestTypeDef(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    TagKeys: Sequence[str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateAgentStatusRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AgentStatusId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[AgentStatusStateType] = None
    DisplayOrder: Optional[int] = None
    ResetOrderNumber: Optional[bool] = None

class UpdateAuthenticationProfileRequestRequestTypeDef(BaseValidatorModel):
    AuthenticationProfileId: str
    InstanceId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    AllowedIps: Optional[Sequence[str]] = None
    BlockedIps: Optional[Sequence[str]] = None
    PeriodicSessionDuration: Optional[int] = None

class UpdateContactAttributesRequestRequestTypeDef(BaseValidatorModel):
    InitialContactId: str
    InstanceId: str
    Attributes: Mapping[str, str]

class UpdateContactFlowContentRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    Content: str

class UpdateContactFlowMetadataRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ContactFlowState: Optional[ContactFlowStateType] = None

class UpdateContactFlowModuleContentRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleId: str
    Content: str

class UpdateContactFlowModuleMetadataRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[ContactFlowModuleStateType] = None

class UpdateContactFlowNameRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateContactRoutingDataRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    QueueTimeAdjustmentSeconds: Optional[int] = None
    QueuePriority: Optional[int] = None

class UpdateInstanceAttributeRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AttributeType: InstanceAttributeTypeType
    Value: str

class UpdatePhoneNumberMetadataRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    PhoneNumberDescription: Optional[str] = None
    ClientToken: Optional[str] = None

class UpdatePhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    ClientToken: Optional[str] = None

class UpdatePromptRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    PromptId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    S3Uri: Optional[str] = None

class UpdateQueueHoursOfOperationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    HoursOfOperationId: str

class UpdateQueueMaxContactsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    MaxContacts: Optional[int] = None

class UpdateQueueNameRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateQueueStatusRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    Status: QueueStatusType

class UpdateQuickConnectNameRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateRoutingProfileAgentAvailabilityTimerRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    AgentAvailabilityTimer: AgentAvailabilityTimerType

class UpdateRoutingProfileDefaultOutboundQueueRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    DefaultOutboundQueueId: str

class UpdateRoutingProfileNameRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UpdateUserHierarchyGroupNameRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    HierarchyGroupId: str
    InstanceId: str

class UpdateUserHierarchyRequestRequestTypeDef(BaseValidatorModel):
    UserId: str
    InstanceId: str
    HierarchyGroupId: Optional[str] = None

class UpdateUserRoutingProfileRequestRequestTypeDef(BaseValidatorModel):
    RoutingProfileId: str
    UserId: str
    InstanceId: str

class UpdateUserSecurityProfilesRequestRequestTypeDef(BaseValidatorModel):
    SecurityProfileIds: Sequence[str]
    UserId: str
    InstanceId: str

class UpdateViewMetadataRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    Name: Optional[str] = None
    Description: Optional[str] = None

class UserReferenceTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None

class UserIdentityInfoLiteTypeDef(BaseValidatorModel):
    FirstName: Optional[str] = None
    LastName: Optional[str] = None

class ViewContentTypeDef(BaseValidatorModel):
    InputSchema: Optional[str] = None
    Template: Optional[str] = None
    Actions: Optional[List[str]] = None

class RuleSummaryTypeDef(BaseValidatorModel):
    Name: str
    RuleId: str
    RuleArn: str
    EventSourceName: EventSourceNameType
    PublishStatus: RulePublishStatusType
    ActionSummaries: List[ActionSummaryTypeDef]
    CreatedTime: datetime
    LastUpdatedTime: datetime

class ActivateEvaluationFormResponseTypeDef(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateAnalyticsDataSetResponseTypeDef(BaseValidatorModel):
    DataSetId: str
    TargetAccountId: str
    ResourceShareId: str
    ResourceShareArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateInstanceStorageConfigResponseTypeDef(BaseValidatorModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateSecurityKeyResponseTypeDef(BaseValidatorModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ClaimPhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAgentStatusResponseTypeDef(BaseValidatorModel):
    AgentStatusARN: str
    AgentStatusId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContactFlowModuleResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateContactFlowResponseTypeDef(BaseValidatorModel):
    ContactFlowId: str
    ContactFlowArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateEvaluationFormResponseTypeDef(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateHoursOfOperationResponseTypeDef(BaseValidatorModel):
    HoursOfOperationId: str
    HoursOfOperationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateInstanceResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateIntegrationAssociationResponseTypeDef(BaseValidatorModel):
    IntegrationAssociationId: str
    IntegrationAssociationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePersistentContactAssociationResponseTypeDef(BaseValidatorModel):
    ContinuedFromContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePromptResponseTypeDef(BaseValidatorModel):
    PromptARN: str
    PromptId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQueueResponseTypeDef(BaseValidatorModel):
    QueueArn: str
    QueueId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateQuickConnectResponseTypeDef(BaseValidatorModel):
    QuickConnectARN: str
    QuickConnectId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRoutingProfileResponseTypeDef(BaseValidatorModel):
    RoutingProfileArn: str
    RoutingProfileId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleResponseTypeDef(BaseValidatorModel):
    RuleArn: str
    RuleId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSecurityProfileResponseTypeDef(BaseValidatorModel):
    SecurityProfileId: str
    SecurityProfileArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTaskTemplateResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTrafficDistributionGroupResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUseCaseResponseTypeDef(BaseValidatorModel):
    UseCaseId: str
    UseCaseArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserHierarchyGroupResponseTypeDef(BaseValidatorModel):
    HierarchyGroupId: str
    HierarchyGroupArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateUserResponseTypeDef(BaseValidatorModel):
    UserId: str
    UserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVocabularyResponseTypeDef(BaseValidatorModel):
    VocabularyArn: str
    VocabularyId: str
    State: VocabularyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class DeactivateEvaluationFormResponseTypeDef(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVocabularyResponseTypeDef(BaseValidatorModel):
    VocabularyArn: str
    VocabularyId: str
    State: VocabularyStateType
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetContactAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class GetFlowAssociationResponseTypeDef(BaseValidatorModel):
    ResourceId: str
    FlowId: str
    ResourceType: Literal["SMS_PHONE_NUMBER"]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPromptFileResponseTypeDef(BaseValidatorModel):
    PromptPresignedUrl: str
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef

class ImportPhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListApprovedOriginsResponseTypeDef(BaseValidatorModel):
    Origins: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListLambdaFunctionsResponseTypeDef(BaseValidatorModel):
    LambdaFunctions: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSecurityProfilePermissionsResponseTypeDef(BaseValidatorModel):
    Permissions: List[str]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class MonitorContactResponseTypeDef(BaseValidatorModel):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicateInstanceResponseTypeDef(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendChatIntegrationEventResponseTypeDef(BaseValidatorModel):
    InitialContactId: str
    NewChatCreated: bool
    ResponseMetadata: ResponseMetadataTypeDef

class StartChatContactResponseTypeDef(BaseValidatorModel):
    ContactId: str
    ParticipantId: str
    ParticipantToken: str
    ContinuedFromContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartContactEvaluationResponseTypeDef(BaseValidatorModel):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartContactStreamingResponseTypeDef(BaseValidatorModel):
    StreamingId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartOutboundVoiceContactResponseTypeDef(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartTaskContactResponseTypeDef(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SubmitContactEvaluationResponseTypeDef(BaseValidatorModel):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class TransferContactResponseTypeDef(BaseValidatorModel):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateContactEvaluationResponseTypeDef(BaseValidatorModel):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateEvaluationFormResponseTypeDef(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePromptResponseTypeDef(BaseValidatorModel):
    PromptARN: str
    PromptId: str
    ResponseMetadata: ResponseMetadataTypeDef

class AgentConfigOutputTypeDef(BaseValidatorModel):
    Distributions: List[DistributionTypeDef]

class AgentConfigTypeDef(BaseValidatorModel):
    Distributions: Sequence[DistributionTypeDef]

class TelephonyConfigOutputTypeDef(BaseValidatorModel):
    Distributions: List[DistributionTypeDef]

class TelephonyConfigTypeDef(BaseValidatorModel):
    Distributions: Sequence[DistributionTypeDef]

class AgentContactReferenceTypeDef(BaseValidatorModel):
    ContactId: Optional[str] = None
    Channel: Optional[ChannelType] = None
    InitiationMethod: Optional[ContactInitiationMethodType] = None
    AgentContactState: Optional[ContactStateType] = None
    StateStartTimestamp: Optional[datetime] = None
    ConnectedToAgentTimestamp: Optional[datetime] = None
    Queue: Optional[QueueReferenceTypeDef] = None

class HierarchyGroupsTypeDef(BaseValidatorModel):
    Level1: Optional[AgentHierarchyGroupTypeDef] = None
    Level2: Optional[AgentHierarchyGroupTypeDef] = None
    Level3: Optional[AgentHierarchyGroupTypeDef] = None
    Level4: Optional[AgentHierarchyGroupTypeDef] = None
    Level5: Optional[AgentHierarchyGroupTypeDef] = None

class AllowedCapabilitiesTypeDef(BaseValidatorModel):
    Customer: Optional[ParticipantCapabilitiesTypeDef] = None
    Agent: Optional[ParticipantCapabilitiesTypeDef] = None

class CustomerTypeDef(BaseValidatorModel):
    DeviceInfo: Optional[DeviceInfoTypeDef] = None
    Capabilities: Optional[ParticipantCapabilitiesTypeDef] = None

class AgentQualityMetricsTypeDef(BaseValidatorModel):
    Audio: Optional[AudioQualityMetricsInfoTypeDef] = None

class CustomerQualityMetricsTypeDef(BaseValidatorModel):
    Audio: Optional[AudioQualityMetricsInfoTypeDef] = None

class ListAgentStatusResponseTypeDef(BaseValidatorModel):
    AgentStatusSummaryList: List[AgentStatusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeAgentStatusResponseTypeDef(BaseValidatorModel):
    AgentStatus: AgentStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MatchCriteriaTypeDef(BaseValidatorModel):
    AgentsCriteria: Optional[AgentsCriteriaTypeDef] = None

class ListAnalyticsDataAssociationsResponseTypeDef(BaseValidatorModel):
    Results: List[AnalyticsDataAssociationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSecurityProfileApplicationsResponseTypeDef(BaseValidatorModel):
    Applications: List[ApplicationOutputTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateLexBotRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LexBot: LexBotTypeDef

class ListLexBotsResponseTypeDef(BaseValidatorModel):
    LexBots: List[LexBotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateBotRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LexBot: Optional[LexBotTypeDef] = None
    LexV2Bot: Optional[LexV2BotTypeDef] = None

class DisassociateBotRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LexBot: Optional[LexBotTypeDef] = None
    LexV2Bot: Optional[LexV2BotTypeDef] = None

class LexBotConfigTypeDef(BaseValidatorModel):
    LexBot: Optional[LexBotTypeDef] = None
    LexV2Bot: Optional[LexV2BotTypeDef] = None

class AssociateUserProficienciesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiencyTypeDef]

class ListUserProficienciesResponseTypeDef(BaseValidatorModel):
    UserProficiencyList: List[UserProficiencyTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateUserProficienciesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiencyTypeDef]

class AttachedFileTypeDef(BaseValidatorModel):
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

class StartAttachedFileUploadRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FileName: str
    FileSizeInBytes: int
    FileUseCaseType: Literal["ATTACHMENT"]
    AssociatedResourceArn: str
    ClientToken: Optional[str] = None
    UrlExpiryInSeconds: Optional[int] = None
    CreatedBy: Optional[CreatedByInfoTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None

class AttributeAndConditionTypeDef(BaseValidatorModel):
    TagConditions: Optional[Sequence[TagConditionTypeDef]] = None
    HierarchyGroupCondition: Optional[HierarchyGroupConditionTypeDef] = None

class ControlPlaneTagFilterTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Sequence[TagConditionTypeDef]]] = None
    AndConditions: Optional[Sequence[TagConditionTypeDef]] = None
    TagCondition: Optional[TagConditionTypeDef] = None

class DescribeInstanceAttributeResponseTypeDef(BaseValidatorModel):
    Attribute: AttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: List[AttributeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MeetingFeaturesConfigurationTypeDef(BaseValidatorModel):
    Audio: Optional[AudioFeaturesTypeDef] = None

class ListAuthenticationProfilesResponseTypeDef(BaseValidatorModel):
    AuthenticationProfileSummaryList: List[AuthenticationProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeAuthenticationProfileResponseTypeDef(BaseValidatorModel):
    AuthenticationProfile: AuthenticationProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchAvailablePhoneNumbersResponseTypeDef(BaseValidatorModel):
    AvailableNumbersList: List[AvailableNumberSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchAssociateAnalyticsDataSetResponseTypeDef(BaseValidatorModel):
    Created: List[AnalyticsDataAssociationResultTypeDef]
    Errors: List[ErrorResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDisassociateAnalyticsDataSetResponseTypeDef(BaseValidatorModel):
    Deleted: List[str]
    Errors: List[ErrorResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetFlowAssociationResponseTypeDef(BaseValidatorModel):
    FlowAssociationSummaryList: List[FlowAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListFlowAssociationsResponseTypeDef(BaseValidatorModel):
    FlowAssociationSummaryList: List[FlowAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchPutContactResponseTypeDef(BaseValidatorModel):
    SuccessfulRequestList: List[SuccessfulRequestTypeDef]
    FailedRequestList: List[FailedRequestTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class StartContactStreamingRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ChatStreamingConfiguration: ChatStreamingConfigurationTypeDef
    ClientToken: str

class ClaimedPhoneNumberSummaryTypeDef(BaseValidatorModel):
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

class ContactDataRequestTypeDef(BaseValidatorModel):
    SystemEndpoint: Optional[EndpointTypeDef] = None
    CustomerEndpoint: Optional[EndpointTypeDef] = None
    RequestIdentifier: Optional[str] = None
    QueueId: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    Campaign: Optional[CampaignTypeDef] = None

class UserDataFiltersTypeDef(BaseValidatorModel):
    Queues: Optional[Sequence[str]] = None
    ContactFilter: Optional[ContactFilterTypeDef] = None
    RoutingProfiles: Optional[Sequence[str]] = None
    Agents: Optional[Sequence[str]] = None
    UserHierarchyGroups: Optional[Sequence[str]] = None

class ContactFlowModuleSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class ContactFlowSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    TypeCondition: Optional[ContactFlowTypeType] = None
    StateCondition: Optional[ContactFlowStateType] = None
    StatusCondition: Optional[ContactFlowStatusType] = None

class HoursOfOperationSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class PredefinedAttributeSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class PromptSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class QueueSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    QueueTypeCondition: Optional[Literal["STANDARD"]] = None

class QuickConnectSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class RoutingProfileSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class SecurityProfileSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None

class UserSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Dict[str, Any]]] = None
    AndConditions: Optional[Sequence[Dict[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    HierarchyGroupCondition: Optional[HierarchyGroupConditionTypeDef] = None

class ListContactFlowModulesResponseTypeDef(BaseValidatorModel):
    ContactFlowModulesSummaryList: List[ContactFlowModuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeContactFlowModuleResponseTypeDef(BaseValidatorModel):
    ContactFlowModule: ContactFlowModuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchContactFlowModulesResponseTypeDef(BaseValidatorModel):
    ContactFlowModules: List[ContactFlowModuleTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListContactFlowsResponseTypeDef(BaseValidatorModel):
    ContactFlowSummaryList: List[ContactFlowSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeContactFlowResponseTypeDef(BaseValidatorModel):
    ContactFlow: ContactFlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchContactFlowsResponseTypeDef(BaseValidatorModel):
    ContactFlows: List[ContactFlowTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ContactSearchSummaryTypeDef(BaseValidatorModel):
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

class CreateEvaluationFormRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Title: str
    Items: Sequence[EvaluationFormItemUnionTypeDef]
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategyTypeDef] = None
    ClientToken: Optional[str] = None

class EvaluationFormContentTypeDef(BaseValidatorModel):
    EvaluationFormVersion: int
    EvaluationFormId: str
    EvaluationFormArn: str
    Title: str
    Items: List["EvaluationFormItemOutputTypeDef"]
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategyTypeDef] = None

class EvaluationFormTypeDef(BaseValidatorModel):
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

class UpdateEvaluationFormRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int
    Title: str
    Items: Sequence[EvaluationFormItemUnionTypeDef]
    CreateNewVersion: Optional[bool] = None
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategyTypeDef] = None
    ClientToken: Optional[str] = None

class CreateParticipantRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ParticipantDetails: ParticipantDetailsToAddTypeDef
    ClientToken: Optional[str] = None

class CreateParticipantResponseTypeDef(BaseValidatorModel):
    ParticipantCredentials: ParticipantTokenCredentialsTypeDef
    ParticipantId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePredefinedAttributeRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    Values: PredefinedAttributeValuesTypeDef

class UpdatePredefinedAttributeRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    Values: Optional[PredefinedAttributeValuesTypeDef] = None

class CreateQueueRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    HoursOfOperationId: str
    Description: Optional[str] = None
    OutboundCallerConfig: Optional[OutboundCallerConfigTypeDef] = None
    MaxContacts: Optional[int] = None
    QuickConnectIds: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None

class QueueTypeDef(BaseValidatorModel):
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

class UpdateQueueOutboundCallerConfigRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    OutboundCallerConfig: OutboundCallerConfigTypeDef

class UpdateUserIdentityInfoRequestRequestTypeDef(BaseValidatorModel):
    IdentityInfo: UserIdentityInfoTypeDef
    UserId: str
    InstanceId: str

class CreateUserRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateUserPhoneConfigRequestRequestTypeDef(BaseValidatorModel):
    PhoneConfig: UserPhoneConfigTypeDef
    UserId: str
    InstanceId: str

class UserTypeDef(BaseValidatorModel):
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

class CreateViewRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Status: ViewStatusType
    Content: ViewInputContentTypeDef
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class UpdateViewContentRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    Status: ViewStatusType
    Content: ViewInputContentTypeDef

class GetFederationTokenResponseTypeDef(BaseValidatorModel):
    Credentials: CredentialsTypeDef
    SignInUrl: str
    UserArn: str
    UserId: str
    ResponseMetadata: ResponseMetadataTypeDef

class MediaConcurrencyTypeDef(BaseValidatorModel):
    Channel: ChannelType
    Concurrency: int
    CrossChannelBehavior: Optional[CrossChannelBehaviorTypeDef] = None

class CurrentMetricDataTypeDef(BaseValidatorModel):
    Metric: Optional[CurrentMetricTypeDef] = None
    Value: Optional[float] = None

class ListDefaultVocabulariesResponseTypeDef(BaseValidatorModel):
    DefaultVocabularyList: List[DefaultVocabularyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribePromptResponseTypeDef(BaseValidatorModel):
    Prompt: PromptTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchPromptsResponseTypeDef(BaseValidatorModel):
    Prompts: List[PromptTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeSecurityProfileResponseTypeDef(BaseValidatorModel):
    SecurityProfile: SecurityProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTrafficDistributionGroupResponseTypeDef(BaseValidatorModel):
    TrafficDistributionGroup: TrafficDistributionGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVocabularyResponseTypeDef(BaseValidatorModel):
    Vocabulary: VocabularyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DimensionsTypeDef(BaseValidatorModel):
    Queue: Optional[QueueReferenceTypeDef] = None
    Channel: Optional[ChannelType] = None
    RoutingProfile: Optional[RoutingProfileReferenceTypeDef] = None
    RoutingStepExpression: Optional[str] = None

class DisassociateRoutingProfileQueuesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    QueueReferences: Sequence[RoutingProfileQueueReferenceTypeDef]

class RoutingProfileQueueConfigTypeDef(BaseValidatorModel):
    QueueReference: RoutingProfileQueueReferenceTypeDef
    Priority: int
    Delay: int

class DisassociateUserProficienciesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiencyDisassociateTypeDef]

class StopContactRequestRequestTypeDef(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    DisconnectReason: Optional[DisconnectReasonTypeDef] = None

class GetAttachedFileResponseTypeDef(BaseValidatorModel):
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

class KinesisVideoStreamConfigTypeDef(BaseValidatorModel):
    Prefix: str
    RetentionPeriodHours: int
    EncryptionConfig: EncryptionConfigTypeDef

class S3ConfigTypeDef(BaseValidatorModel):
    BucketName: str
    BucketPrefix: str
    EncryptionConfig: Optional[EncryptionConfigTypeDef] = None

class EvaluationAnswerInputTypeDef(BaseValidatorModel):
    Value: Optional[EvaluationAnswerDataTypeDef] = None

class EvaluationAnswerOutputTypeDef(BaseValidatorModel):
    Value: Optional[EvaluationAnswerDataTypeDef] = None
    SystemSuggestedValue: Optional[EvaluationAnswerDataTypeDef] = None

class EvaluationFormNumericQuestionAutomationTypeDef(BaseValidatorModel):
    PropertyValue: Optional[NumericQuestionPropertyValueAutomationTypeDef] = None

class EvaluationFormSingleSelectQuestionAutomationOptionTypeDef(BaseValidatorModel):
    RuleCategory: Optional[SingleSelectQuestionRuleCategoryAutomationTypeDef] = None

class ListEvaluationFormsResponseTypeDef(BaseValidatorModel):
    EvaluationFormSummaryList: List[EvaluationFormSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListEvaluationFormVersionsResponseTypeDef(BaseValidatorModel):
    EvaluationFormVersionSummaryList: List[EvaluationFormVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class EvaluationMetadataTypeDef(BaseValidatorModel):
    ContactId: str
    EvaluatorArn: str
    ContactAgentId: Optional[str] = None
    Score: Optional[EvaluationScoreTypeDef] = None

class EvaluationSummaryTypeDef(BaseValidatorModel):
    EvaluationId: str
    EvaluationArn: str
    EvaluationFormTitle: str
    EvaluationFormId: str
    Status: EvaluationStatusType
    EvaluatorArn: str
    CreatedTime: datetime
    LastModifiedTime: datetime
    Score: Optional[EvaluationScoreTypeDef] = None

class StepTypeDef(BaseValidatorModel):
    Expiry: Optional[ExpiryTypeDef] = None
    Expression: Optional["ExpressionTypeDef"] = None
    Status: Optional[RoutingCriteriaStepStatusType] = None

class FieldValueOutputTypeDef(BaseValidatorModel):
    Id: str
    Value: FieldValueUnionOutputTypeDef

class FieldValueTypeDef(BaseValidatorModel):
    Id: str
    Value: FieldValueUnionTypeDef

class GetCurrentMetricDataRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Filters: FiltersTypeDef
    CurrentMetrics: Sequence[CurrentMetricTypeDef]
    Groupings: Optional[Sequence[GroupingType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortCriteria: Optional[Sequence[CurrentMetricSortCriteriaTypeDef]] = None

class ListAgentStatusRequestListAgentStatusesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    AgentStatusTypes: Optional[Sequence[AgentStatusTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListApprovedOriginsRequestListApprovedOriginsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListAuthenticationProfilesRequestListAuthenticationProfilesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListBotsRequestListBotsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    LexVersion: LexVersionType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContactEvaluationsRequestListContactEvaluationsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContactFlowModulesRequestListContactFlowModulesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleState: Optional[ContactFlowModuleStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContactFlowsRequestListContactFlowsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowTypes: Optional[Sequence[ContactFlowTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListContactReferencesRequestListContactReferencesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ReferenceTypes: Sequence[ReferenceTypeType]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListDefaultVocabulariesRequestListDefaultVocabulariesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    LanguageCode: Optional[VocabularyLanguageCodeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEvaluationFormVersionsRequestListEvaluationFormVersionsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListEvaluationFormsRequestListEvaluationFormsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListFlowAssociationsRequestListFlowAssociationsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceType: Optional[Literal["VOICE_PHONE_NUMBER"]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListHoursOfOperationsRequestListHoursOfOperationsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceAttributesRequestListInstanceAttributesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstanceStorageConfigsRequestListInstanceStorageConfigsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListInstancesRequestListInstancesPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListIntegrationAssociationsRequestListIntegrationAssociationsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationType: Optional[IntegrationTypeType] = None
    IntegrationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLambdaFunctionsRequestListLambdaFunctionsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListLexBotsRequestListLexBotsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPhoneNumbersRequestListPhoneNumbersPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPhoneNumbersV2RequestListPhoneNumbersV2PaginateTypeDef(BaseValidatorModel):
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPredefinedAttributesRequestListPredefinedAttributesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPromptsRequestListPromptsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueueQuickConnectsRequestListQueueQuickConnectsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQueuesRequestListQueuesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueTypes: Optional[Sequence[QueueTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListQuickConnectsRequestListQuickConnectsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    QuickConnectTypes: Optional[Sequence[QuickConnectTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoutingProfileQueuesRequestListRoutingProfileQueuesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRoutingProfilesRequestListRoutingProfilesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRulesRequestListRulesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PublishStatus: Optional[RulePublishStatusType] = None
    EventSourceName: Optional[EventSourceNameType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityKeysRequestListSecurityKeysPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityProfileApplicationsRequestListSecurityProfileApplicationsPaginateTypeDef(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityProfilePermissionsRequestListSecurityProfilePermissionsPaginateTypeDef(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListSecurityProfilesRequestListSecurityProfilesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTaskTemplatesRequestListTaskTemplatesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    Status: Optional[TaskTemplateStatusType] = None
    Name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListTrafficDistributionGroupsRequestListTrafficDistributionGroupsPaginateTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUseCasesRequestListUseCasesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserHierarchyGroupsRequestListUserHierarchyGroupsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUserProficienciesRequestListUserProficienciesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    UserId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListViewVersionsRequestListViewVersionsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListViewsRequestListViewsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    Type: Optional[ViewTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchAvailablePhoneNumbersRequestSearchAvailablePhoneNumbersPaginateTypeDef(BaseValidatorModel):
    PhoneNumberCountryCode: PhoneNumberCountryCodeType
    PhoneNumberType: PhoneNumberTypeType
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchVocabulariesRequestSearchVocabulariesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    State: Optional[VocabularyStateType] = None
    NameStartsWith: Optional[str] = None
    LanguageCode: Optional[VocabularyLanguageCodeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchContactsTimeRangeTypeDef(BaseValidatorModel):
    Type: SearchContactsTimeRangeTypeType
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef

class UpdateContactScheduleRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ScheduledTime: TimestampTypeDef

class HierarchyPathReferenceTypeDef(BaseValidatorModel):
    LevelOne: Optional[HierarchyGroupSummaryReferenceTypeDef] = None
    LevelTwo: Optional[HierarchyGroupSummaryReferenceTypeDef] = None
    LevelThree: Optional[HierarchyGroupSummaryReferenceTypeDef] = None
    LevelFour: Optional[HierarchyGroupSummaryReferenceTypeDef] = None
    LevelFive: Optional[HierarchyGroupSummaryReferenceTypeDef] = None

class HierarchyPathTypeDef(BaseValidatorModel):
    LevelOne: Optional[HierarchyGroupSummaryTypeDef] = None
    LevelTwo: Optional[HierarchyGroupSummaryTypeDef] = None
    LevelThree: Optional[HierarchyGroupSummaryTypeDef] = None
    LevelFour: Optional[HierarchyGroupSummaryTypeDef] = None
    LevelFive: Optional[HierarchyGroupSummaryTypeDef] = None

class ListUserHierarchyGroupsResponseTypeDef(BaseValidatorModel):
    UserHierarchyGroupSummaryList: List[HierarchyGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class HierarchyStructureTypeDef(BaseValidatorModel):
    LevelOne: Optional[HierarchyLevelTypeDef] = None
    LevelTwo: Optional[HierarchyLevelTypeDef] = None
    LevelThree: Optional[HierarchyLevelTypeDef] = None
    LevelFour: Optional[HierarchyLevelTypeDef] = None
    LevelFive: Optional[HierarchyLevelTypeDef] = None

class HierarchyStructureUpdateTypeDef(BaseValidatorModel):
    LevelOne: Optional[HierarchyLevelUpdateTypeDef] = None
    LevelTwo: Optional[HierarchyLevelUpdateTypeDef] = None
    LevelThree: Optional[HierarchyLevelUpdateTypeDef] = None
    LevelFour: Optional[HierarchyLevelUpdateTypeDef] = None
    LevelFive: Optional[HierarchyLevelUpdateTypeDef] = None

class HistoricalMetricTypeDef(BaseValidatorModel):
    Name: Optional[HistoricalMetricNameType] = None
    Threshold: Optional[ThresholdTypeDef] = None
    Statistic: Optional[StatisticType] = None
    Unit: Optional[UnitType] = None

class HoursOfOperationConfigTypeDef(BaseValidatorModel):
    Day: HoursOfOperationDaysType
    StartTime: HoursOfOperationTimeSliceTypeDef
    EndTime: HoursOfOperationTimeSliceTypeDef

class ListHoursOfOperationsResponseTypeDef(BaseValidatorModel):
    HoursOfOperationSummaryList: List[HoursOfOperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InstanceTypeDef(BaseValidatorModel):
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

class ListInstancesResponseTypeDef(BaseValidatorModel):
    InstanceSummaryList: List[InstanceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListIntegrationAssociationsResponseTypeDef(BaseValidatorModel):
    IntegrationAssociationSummaryList: List[IntegrationAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class InvisibleFieldInfoTypeDef(BaseValidatorModel):
    Id: Optional[TaskTemplateFieldIdentifierTypeDef] = None

class ReadOnlyFieldInfoTypeDef(BaseValidatorModel):
    Id: Optional[TaskTemplateFieldIdentifierTypeDef] = None

class RequiredFieldInfoTypeDef(BaseValidatorModel):
    Id: Optional[TaskTemplateFieldIdentifierTypeDef] = None

class TaskTemplateDefaultFieldValueTypeDef(BaseValidatorModel):
    Id: Optional[TaskTemplateFieldIdentifierTypeDef] = None
    DefaultValue: Optional[str] = None

class TaskTemplateFieldOutputTypeDef(BaseValidatorModel):
    Id: TaskTemplateFieldIdentifierTypeDef
    Description: Optional[str] = None
    Type: Optional[TaskTemplateFieldTypeType] = None
    SingleSelectOptions: Optional[List[str]] = None

class TaskTemplateFieldTypeDef(BaseValidatorModel):
    Id: TaskTemplateFieldIdentifierTypeDef
    Description: Optional[str] = None
    Type: Optional[TaskTemplateFieldTypeType] = None
    SingleSelectOptions: Optional[Sequence[str]] = None

class ListPhoneNumbersResponseTypeDef(BaseValidatorModel):
    PhoneNumberSummaryList: List[PhoneNumberSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPhoneNumbersV2ResponseTypeDef(BaseValidatorModel):
    ListPhoneNumbersSummaryList: List[ListPhoneNumbersSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPredefinedAttributesResponseTypeDef(BaseValidatorModel):
    PredefinedAttributeSummaryList: List[PredefinedAttributeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListPromptsResponseTypeDef(BaseValidatorModel):
    PromptSummaryList: List[PromptSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListQueueQuickConnectsResponseTypeDef(BaseValidatorModel):
    QuickConnectSummaryList: List[QuickConnectSummaryTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListQuickConnectsResponseTypeDef(BaseValidatorModel):
    QuickConnectSummaryList: List[QuickConnectSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListQueuesResponseTypeDef(BaseValidatorModel):
    QueueSummaryList: List[QueueSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRoutingProfileQueuesResponseTypeDef(BaseValidatorModel):
    RoutingProfileQueueConfigSummaryList: List[RoutingProfileQueueConfigSummaryTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListRoutingProfilesResponseTypeDef(BaseValidatorModel):
    RoutingProfileSummaryList: List[RoutingProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSecurityKeysResponseTypeDef(BaseValidatorModel):
    SecurityKeys: List[SecurityKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListSecurityProfilesResponseTypeDef(BaseValidatorModel):
    SecurityProfileSummaryList: List[SecurityProfileSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTaskTemplatesResponseTypeDef(BaseValidatorModel):
    TaskTemplates: List[TaskTemplateMetadataTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTrafficDistributionGroupUsersResponseTypeDef(BaseValidatorModel):
    TrafficDistributionGroupUserSummaryList: List[TrafficDistributionGroupUserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListTrafficDistributionGroupsResponseTypeDef(BaseValidatorModel):
    TrafficDistributionGroupSummaryList: List[TrafficDistributionGroupSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUseCasesResponseTypeDef(BaseValidatorModel):
    UseCaseSummaryList: List[UseCaseTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListUsersResponseTypeDef(BaseValidatorModel):
    UserSummaryList: List[UserSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListViewVersionsResponseTypeDef(BaseValidatorModel):
    ViewVersionSummaryList: List[ViewVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListViewsResponseTypeDef(BaseValidatorModel):
    ViewsSummaryList: List[ViewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class MetricV2OutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Threshold: Optional[List[ThresholdV2TypeDef]] = None
    MetricFilters: Optional[List[MetricFilterV2OutputTypeDef]] = None

class MetricV2TypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Threshold: Optional[Sequence[ThresholdV2TypeDef]] = None
    MetricFilters: Optional[Sequence[MetricFilterV2TypeDef]] = None

class NewSessionDetailsTypeDef(BaseValidatorModel):
    SupportedMessagingContentTypes: Optional[Sequence[str]] = None
    ParticipantDetails: Optional[ParticipantDetailsTypeDef] = None
    Attributes: Optional[Mapping[str, str]] = None
    StreamingConfiguration: Optional[ChatStreamingConfigurationTypeDef] = None

class SendNotificationActionDefinitionOutputTypeDef(BaseValidatorModel):
    DeliveryMethod: Literal["EMAIL"]
    Content: str
    ContentType: Literal["PLAIN_TEXT"]
    Recipient: NotificationRecipientTypeOutputTypeDef
    Subject: Optional[str] = None

class SendNotificationActionDefinitionTypeDef(BaseValidatorModel):
    DeliveryMethod: Literal["EMAIL"]
    Content: str
    ContentType: Literal["PLAIN_TEXT"]
    Recipient: NotificationRecipientTypeTypeDef
    Subject: Optional[str] = None

class ParticipantTimerConfigurationTypeDef(BaseValidatorModel):
    ParticipantRole: TimerEligibleParticipantRolesType
    TimerType: ParticipantTimerTypeType
    TimerValue: ParticipantTimerValueTypeDef

class StartChatContactRequestRequestTypeDef(BaseValidatorModel):
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

class PredefinedAttributeTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[PredefinedAttributeValuesOutputTypeDef] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class QuickConnectConfigTypeDef(BaseValidatorModel):
    QuickConnectType: QuickConnectTypeType
    UserConfig: Optional[UserQuickConnectConfigTypeDef] = None
    QueueConfig: Optional[QueueQuickConnectConfigTypeDef] = None
    PhoneConfig: Optional[PhoneNumberQuickConnectConfigTypeDef] = None

class RealTimeContactAnalysisTranscriptItemRedactionTypeDef(BaseValidatorModel):
    CharacterOffsets: Optional[List[RealTimeContactAnalysisCharacterIntervalTypeDef]] = None

class RealTimeContactAnalysisTranscriptItemWithCharacterOffsetsTypeDef(BaseValidatorModel):
    Id: str
    CharacterOffsets: Optional[RealTimeContactAnalysisCharacterIntervalTypeDef] = None

class RealTimeContactAnalysisTranscriptItemWithContentTypeDef(BaseValidatorModel):
    Id: str
    Content: Optional[str] = None
    CharacterOffsets: Optional[RealTimeContactAnalysisCharacterIntervalTypeDef] = None

class RealTimeContactAnalysisSegmentAttachmentsTypeDef(BaseValidatorModel):
    Id: str
    ParticipantId: str
    ParticipantRole: ParticipantRoleType
    Attachments: List[RealTimeContactAnalysisAttachmentTypeDef]
    Time: RealTimeContactAnalysisTimeDataTypeDef
    DisplayName: Optional[str] = None

class RealTimeContactAnalysisSegmentEventTypeDef(BaseValidatorModel):
    Id: str
    EventType: str
    Time: RealTimeContactAnalysisTimeDataTypeDef
    ParticipantId: Optional[str] = None
    ParticipantRole: Optional[ParticipantRoleType] = None
    DisplayName: Optional[str] = None

class ReferenceSummaryTypeDef(BaseValidatorModel):
    Url: Optional[UrlReferenceTypeDef] = None
    Attachment: Optional[AttachmentReferenceTypeDef] = None
    String: Optional[StringReferenceTypeDef] = None
    Number: Optional[NumberReferenceTypeDef] = None
    Date: Optional[DateReferenceTypeDef] = None
    Email: Optional[EmailReferenceTypeDef] = None

class StartOutboundVoiceContactRequestRequestTypeDef(BaseValidatorModel):
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

class StartTaskContactRequestRequestTypeDef(BaseValidatorModel):
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

class TaskActionDefinitionOutputTypeDef(BaseValidatorModel):
    Name: str
    ContactFlowId: str
    Description: Optional[str] = None
    References: Optional[Dict[str, ReferenceTypeDef]] = None

class TaskActionDefinitionTypeDef(BaseValidatorModel):
    Name: str
    ContactFlowId: str
    Description: Optional[str] = None
    References: Optional[Mapping[str, ReferenceTypeDef]] = None

class UpdateContactRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    References: Optional[Mapping[str, ReferenceTypeDef]] = None

class ResourceTagsSearchCriteriaTypeDef(BaseValidatorModel):
    TagSearchCondition: Optional[TagSearchConditionTypeDef] = None

class SearchResourceTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagSetTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchSecurityProfilesResponseTypeDef(BaseValidatorModel):
    SecurityProfiles: List[SecurityProfileSearchSummaryTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchVocabulariesResponseTypeDef(BaseValidatorModel):
    VocabularySummaryList: List[VocabularySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchableContactAttributesTypeDef(BaseValidatorModel):
    Criteria: Sequence[SearchableContactAttributesCriteriaTypeDef]
    MatchType: Optional[SearchContactsMatchTypeType] = None

class SignInConfigOutputTypeDef(BaseValidatorModel):
    Distributions: List[SignInDistributionTypeDef]

class SignInConfigTypeDef(BaseValidatorModel):
    Distributions: Sequence[SignInDistributionTypeDef]

class StartAttachedFileUploadResponseTypeDef(BaseValidatorModel):
    FileArn: str
    FileId: str
    CreationTime: str
    FileStatus: FileStatusTypeType
    CreatedBy: CreatedByInfoTypeDef
    UploadUrlMetadata: UploadUrlMetadataTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartContactRecordingRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    VoiceRecordingConfiguration: VoiceRecordingConfigurationTypeDef

class TranscriptTypeDef(BaseValidatorModel):
    Criteria: Sequence[TranscriptCriteriaTypeDef]
    MatchType: Optional[SearchContactsMatchTypeType] = None

class UserSearchSummaryTypeDef(BaseValidatorModel):
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

class ViewTypeDef(BaseValidatorModel):
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

class ListRulesResponseTypeDef(BaseValidatorModel):
    RuleSummaryList: List[RuleSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AgentInfoTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ConnectedToAgentTimestamp: Optional[datetime] = None
    AgentPauseDurationInSeconds: Optional[int] = None
    HierarchyGroups: Optional[HierarchyGroupsTypeDef] = None
    DeviceInfo: Optional[DeviceInfoTypeDef] = None
    Capabilities: Optional[ParticipantCapabilitiesTypeDef] = None

class StartWebRTCContactRequestRequestTypeDef(BaseValidatorModel):
    ContactFlowId: str
    InstanceId: str
    ParticipantDetails: ParticipantDetailsTypeDef
    Attributes: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None
    AllowedCapabilities: Optional[AllowedCapabilitiesTypeDef] = None
    RelatedContactId: Optional[str] = None
    References: Optional[Mapping[str, ReferenceTypeDef]] = None
    Description: Optional[str] = None

class QualityMetricsTypeDef(BaseValidatorModel):
    Agent: Optional[AgentQualityMetricsTypeDef] = None
    Customer: Optional[CustomerQualityMetricsTypeDef] = None

class AttributeConditionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    ProficiencyLevel: Optional[float] = None
    MatchCriteria: Optional[MatchCriteriaTypeDef] = None
    ComparisonOperator: Optional[str] = None

class CreateSecurityProfileRequestRequestTypeDef(BaseValidatorModel):
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

class UpdateSecurityProfileRequestRequestTypeDef(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    Description: Optional[str] = None
    Permissions: Optional[Sequence[str]] = None
    AllowedAccessControlTags: Optional[Mapping[str, str]] = None
    TagRestrictedResources: Optional[Sequence[str]] = None
    Applications: Optional[Sequence[ApplicationUnionTypeDef]] = None
    HierarchyRestrictedResources: Optional[Sequence[str]] = None
    AllowedAccessControlHierarchyGroupId: Optional[str] = None

class ListBotsResponseTypeDef(BaseValidatorModel):
    LexBots: List[LexBotConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class BatchGetAttachedFileMetadataResponseTypeDef(BaseValidatorModel):
    Files: List[AttachedFileTypeDef]
    Errors: List[AttachedFileErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ControlPlaneUserAttributeFilterTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[AttributeAndConditionTypeDef]] = None
    AndCondition: Optional[AttributeAndConditionTypeDef] = None
    TagCondition: Optional[TagConditionTypeDef] = None
    HierarchyGroupCondition: Optional[HierarchyGroupConditionTypeDef] = None

class ContactFlowModuleSearchFilterTypeDef(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class ContactFlowSearchFilterTypeDef(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class HoursOfOperationSearchFilterTypeDef(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class PromptSearchFilterTypeDef(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class QueueSearchFilterTypeDef(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class QuickConnectSearchFilterTypeDef(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class RoutingProfileSearchFilterTypeDef(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class SecurityProfilesSearchFilterTypeDef(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None

class MeetingTypeDef(BaseValidatorModel):
    MediaRegion: Optional[str] = None
    MediaPlacement: Optional[MediaPlacementTypeDef] = None
    MeetingFeatures: Optional[MeetingFeaturesConfigurationTypeDef] = None
    MeetingId: Optional[str] = None

class DescribePhoneNumberResponseTypeDef(BaseValidatorModel):
    ClaimedPhoneNumberSummary: ClaimedPhoneNumberSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchPutContactRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactDataRequestList: Sequence[ContactDataRequestTypeDef]
    ClientToken: Optional[str] = None

class GetCurrentUserDataRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Filters: UserDataFiltersTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class SearchPredefinedAttributesRequestSearchPredefinedAttributesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchCriteria: Optional[PredefinedAttributeSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchContactsResponseTypeDef(BaseValidatorModel):
    Contacts: List[ContactSearchSummaryTypeDef]
    TotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeEvaluationFormResponseTypeDef(BaseValidatorModel):
    EvaluationForm: EvaluationFormTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeQueueResponseTypeDef(BaseValidatorModel):
    Queue: QueueTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchQueuesResponseTypeDef(BaseValidatorModel):
    Queues: List[QueueTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RoutingProfileTypeDef(BaseValidatorModel):
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

class UpdateRoutingProfileConcurrencyRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    MediaConcurrencies: Sequence[MediaConcurrencyTypeDef]

class CurrentMetricResultTypeDef(BaseValidatorModel):
    Dimensions: Optional[DimensionsTypeDef] = None
    Collections: Optional[List[CurrentMetricDataTypeDef]] = None

class AssociateRoutingProfileQueuesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    QueueConfigs: Sequence[RoutingProfileQueueConfigTypeDef]

class CreateRoutingProfileRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    Description: str
    DefaultOutboundQueueId: str
    MediaConcurrencies: Sequence[MediaConcurrencyTypeDef]
    QueueConfigs: Optional[Sequence[RoutingProfileQueueConfigTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None
    AgentAvailabilityTimer: Optional[AgentAvailabilityTimerType] = None

class UpdateRoutingProfileQueuesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    QueueConfigs: Sequence[RoutingProfileQueueConfigTypeDef]

class InstanceStorageConfigTypeDef(BaseValidatorModel):
    StorageType: StorageTypeType
    AssociationId: Optional[str] = None
    S3Config: Optional[S3ConfigTypeDef] = None
    KinesisVideoStreamConfig: Optional[KinesisVideoStreamConfigTypeDef] = None
    KinesisStreamConfig: Optional[KinesisStreamConfigTypeDef] = None
    KinesisFirehoseConfig: Optional[KinesisFirehoseConfigTypeDef] = None

class SubmitContactEvaluationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str
    Answers: Optional[Mapping[str, EvaluationAnswerInputTypeDef]] = None
    Notes: Optional[Mapping[str, EvaluationNoteTypeDef]] = None

class UpdateContactEvaluationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str
    Answers: Optional[Mapping[str, EvaluationAnswerInputTypeDef]] = None
    Notes: Optional[Mapping[str, EvaluationNoteTypeDef]] = None

class EvaluationFormNumericQuestionPropertiesOutputTypeDef(BaseValidatorModel):
    MinValue: int
    MaxValue: int
    Options: Optional[List[EvaluationFormNumericQuestionOptionTypeDef]] = None
    Automation: Optional[EvaluationFormNumericQuestionAutomationTypeDef] = None

class EvaluationFormNumericQuestionPropertiesTypeDef(BaseValidatorModel):
    MinValue: int
    MaxValue: int
    Options: Optional[Sequence[EvaluationFormNumericQuestionOptionTypeDef]] = None
    Automation: Optional[EvaluationFormNumericQuestionAutomationTypeDef] = None

class EvaluationFormSingleSelectQuestionAutomationOutputTypeDef(BaseValidatorModel):
    Options: List[EvaluationFormSingleSelectQuestionAutomationOptionTypeDef]
    DefaultOptionRefId: Optional[str] = None

class EvaluationFormSingleSelectQuestionAutomationTypeDef(BaseValidatorModel):
    Options: Sequence[EvaluationFormSingleSelectQuestionAutomationOptionTypeDef]
    DefaultOptionRefId: Optional[str] = None

class EvaluationTypeDef(BaseValidatorModel):
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

class ListContactEvaluationsResponseTypeDef(BaseValidatorModel):
    EvaluationSummaryList: List[EvaluationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RoutingCriteriaTypeDef(BaseValidatorModel):
    Steps: Optional[List[StepTypeDef]] = None
    ActivationTimestamp: Optional[datetime] = None
    Index: Optional[int] = None

class CreateCaseActionDefinitionOutputTypeDef(BaseValidatorModel):
    Fields: List[FieldValueOutputTypeDef]
    TemplateId: str

class UpdateCaseActionDefinitionOutputTypeDef(BaseValidatorModel):
    Fields: List[FieldValueOutputTypeDef]

class CreateCaseActionDefinitionTypeDef(BaseValidatorModel):
    Fields: Sequence[FieldValueTypeDef]
    TemplateId: str

class UpdateCaseActionDefinitionTypeDef(BaseValidatorModel):
    Fields: Sequence[FieldValueTypeDef]

class UserDataTypeDef(BaseValidatorModel):
    User: Optional[UserReferenceTypeDef] = None
    RoutingProfile: Optional[RoutingProfileReferenceTypeDef] = None
    HierarchyPath: Optional[HierarchyPathReferenceTypeDef] = None
    Status: Optional[AgentStatusReferenceTypeDef] = None
    AvailableSlotsByChannel: Optional[Dict[ChannelType, int]] = None
    MaxSlotsByChannel: Optional[Dict[ChannelType, int]] = None
    ActiveSlotsByChannel: Optional[Dict[ChannelType, int]] = None
    Contacts: Optional[List[AgentContactReferenceTypeDef]] = None
    NextStatus: Optional[str] = None

class HierarchyGroupTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LevelId: Optional[str] = None
    HierarchyPath: Optional[HierarchyPathTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class DescribeUserHierarchyStructureResponseTypeDef(BaseValidatorModel):
    HierarchyStructure: HierarchyStructureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserHierarchyStructureRequestRequestTypeDef(BaseValidatorModel):
    HierarchyStructure: HierarchyStructureUpdateTypeDef
    InstanceId: str

class GetMetricDataRequestGetMetricDataPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Filters: FiltersTypeDef
    HistoricalMetrics: Sequence[HistoricalMetricTypeDef]
    Groupings: Optional[Sequence[GroupingType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetMetricDataRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Filters: FiltersTypeDef
    HistoricalMetrics: Sequence[HistoricalMetricTypeDef]
    Groupings: Optional[Sequence[GroupingType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class HistoricalMetricDataTypeDef(BaseValidatorModel):
    Metric: Optional[HistoricalMetricTypeDef] = None
    Value: Optional[float] = None

class CreateHoursOfOperationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    TimeZone: str
    Config: Sequence[HoursOfOperationConfigTypeDef]
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class HoursOfOperationTypeDef(BaseValidatorModel):
    HoursOfOperationId: Optional[str] = None
    HoursOfOperationArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    TimeZone: Optional[str] = None
    Config: Optional[List[HoursOfOperationConfigTypeDef]] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class UpdateHoursOfOperationRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    TimeZone: Optional[str] = None
    Config: Optional[Sequence[HoursOfOperationConfigTypeDef]] = None

class DescribeInstanceResponseTypeDef(BaseValidatorModel):
    Instance: InstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class TaskTemplateConstraintsOutputTypeDef(BaseValidatorModel):
    RequiredFields: Optional[List[RequiredFieldInfoTypeDef]] = None
    ReadOnlyFields: Optional[List[ReadOnlyFieldInfoTypeDef]] = None
    InvisibleFields: Optional[List[InvisibleFieldInfoTypeDef]] = None

class TaskTemplateConstraintsTypeDef(BaseValidatorModel):
    RequiredFields: Optional[Sequence[RequiredFieldInfoTypeDef]] = None
    ReadOnlyFields: Optional[Sequence[ReadOnlyFieldInfoTypeDef]] = None
    InvisibleFields: Optional[Sequence[InvisibleFieldInfoTypeDef]] = None

class TaskTemplateDefaultsOutputTypeDef(BaseValidatorModel):
    DefaultFieldValues: Optional[List[TaskTemplateDefaultFieldValueTypeDef]] = None

class TaskTemplateDefaultsTypeDef(BaseValidatorModel):
    DefaultFieldValues: Optional[Sequence[TaskTemplateDefaultFieldValueTypeDef]] = None

class MetricDataV2TypeDef(BaseValidatorModel):
    Metric: Optional[MetricV2OutputTypeDef] = None
    Value: Optional[float] = None

class SendChatIntegrationEventRequestRequestTypeDef(BaseValidatorModel):
    SourceId: str
    DestinationId: str
    Event: ChatEventTypeDef
    Subtype: Optional[str] = None
    NewSessionDetails: Optional[NewSessionDetailsTypeDef] = None

class ChatParticipantRoleConfigTypeDef(BaseValidatorModel):
    ParticipantTimerConfigList: Sequence[ParticipantTimerConfigurationTypeDef]

class DescribePredefinedAttributeResponseTypeDef(BaseValidatorModel):
    PredefinedAttribute: PredefinedAttributeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchPredefinedAttributesResponseTypeDef(BaseValidatorModel):
    PredefinedAttributes: List[PredefinedAttributeTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateQuickConnectRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    QuickConnectConfig: QuickConnectConfigTypeDef
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None

class QuickConnectTypeDef(BaseValidatorModel):
    QuickConnectARN: Optional[str] = None
    QuickConnectId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    QuickConnectConfig: Optional[QuickConnectConfigTypeDef] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

class UpdateQuickConnectConfigRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str
    QuickConnectConfig: QuickConnectConfigTypeDef

class RealTimeContactAnalysisSegmentTranscriptTypeDef(BaseValidatorModel):
    Id: str
    ParticipantId: str
    ParticipantRole: ParticipantRoleType
    Content: str
    Time: RealTimeContactAnalysisTimeDataTypeDef
    DisplayName: Optional[str] = None
    ContentType: Optional[str] = None
    Redaction: Optional[RealTimeContactAnalysisTranscriptItemRedactionTypeDef] = None
    Sentiment: Optional[RealTimeContactAnalysisSentimentLabelType] = None

class RealTimeContactAnalysisPointOfInterestTypeDef(BaseValidatorModel):
    TranscriptItems: Optional[       List[RealTimeContactAnalysisTranscriptItemWithCharacterOffsetsTypeDef]     ] = None

class RealTimeContactAnalysisIssueDetectedTypeDef(BaseValidatorModel):
    TranscriptItems: List[RealTimeContactAnalysisTranscriptItemWithContentTypeDef]

class ListContactReferencesResponseTypeDef(BaseValidatorModel):
    ReferenceSummaryList: List[ReferenceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class SearchResourceTagsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceTypes: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchCriteria: Optional[ResourceTagsSearchCriteriaTypeDef] = None

class SearchResourceTagsRequestSearchResourceTagsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceTypes: Optional[Sequence[str]] = None
    SearchCriteria: Optional[ResourceTagsSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class GetTrafficDistributionResponseTypeDef(BaseValidatorModel):
    TelephonyConfig: TelephonyConfigOutputTypeDef
    Id: str
    Arn: str
    SignInConfig: SignInConfigOutputTypeDef
    AgentConfig: AgentConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateTrafficDistributionRequestRequestTypeDef(BaseValidatorModel):
    Id: str
    TelephonyConfig: Optional[TelephonyConfigTypeDef] = None
    SignInConfig: Optional[SignInConfigTypeDef] = None
    AgentConfig: Optional[AgentConfigTypeDef] = None

class ContactAnalysisTypeDef(BaseValidatorModel):
    Transcript: Optional[TranscriptTypeDef] = None

class SearchUsersResponseTypeDef(BaseValidatorModel):
    Users: List[UserSearchSummaryTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class CreateViewResponseTypeDef(BaseValidatorModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateViewVersionResponseTypeDef(BaseValidatorModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeViewResponseTypeDef(BaseValidatorModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateViewContentResponseTypeDef(BaseValidatorModel):
    View: ViewTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ExpressionTypeDef(BaseValidatorModel):
    AttributeCondition: Optional[AttributeConditionTypeDef] = None
    AndExpression: Optional[List[Dict[str, Any]]] = None
    OrExpression: Optional[List[Dict[str, Any]]] = None

class UserSearchFilterTypeDef(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None
    UserAttributeFilter: Optional[ControlPlaneUserAttributeFilterTypeDef] = None

class SearchContactFlowModulesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[ContactFlowModuleSearchFilterTypeDef] = None
    SearchCriteria: Optional["ContactFlowModuleSearchCriteriaTypeDef"] = None

class SearchContactFlowModulesRequestSearchContactFlowModulesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[ContactFlowModuleSearchFilterTypeDef] = None
    SearchCriteria: Optional[ContactFlowModuleSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchContactFlowsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[ContactFlowSearchFilterTypeDef] = None
    SearchCriteria: Optional["ContactFlowSearchCriteriaTypeDef"] = None

class SearchContactFlowsRequestSearchContactFlowsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[ContactFlowSearchFilterTypeDef] = None
    SearchCriteria: Optional[ContactFlowSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchHoursOfOperationsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[HoursOfOperationSearchFilterTypeDef] = None
    SearchCriteria: Optional["HoursOfOperationSearchCriteriaTypeDef"] = None

class SearchHoursOfOperationsRequestSearchHoursOfOperationsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[HoursOfOperationSearchFilterTypeDef] = None
    SearchCriteria: Optional[HoursOfOperationSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchPromptsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[PromptSearchFilterTypeDef] = None
    SearchCriteria: Optional["PromptSearchCriteriaTypeDef"] = None

class SearchPromptsRequestSearchPromptsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[PromptSearchFilterTypeDef] = None
    SearchCriteria: Optional[PromptSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchQueuesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[QueueSearchFilterTypeDef] = None
    SearchCriteria: Optional["QueueSearchCriteriaTypeDef"] = None

class SearchQueuesRequestSearchQueuesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[QueueSearchFilterTypeDef] = None
    SearchCriteria: Optional[QueueSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchQuickConnectsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[QuickConnectSearchFilterTypeDef] = None
    SearchCriteria: Optional["QuickConnectSearchCriteriaTypeDef"] = None

class SearchQuickConnectsRequestSearchQuickConnectsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[QuickConnectSearchFilterTypeDef] = None
    SearchCriteria: Optional[QuickConnectSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchRoutingProfilesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[RoutingProfileSearchFilterTypeDef] = None
    SearchCriteria: Optional["RoutingProfileSearchCriteriaTypeDef"] = None

class SearchRoutingProfilesRequestSearchRoutingProfilesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[RoutingProfileSearchFilterTypeDef] = None
    SearchCriteria: Optional[RoutingProfileSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class SearchSecurityProfilesRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchCriteria: Optional["SecurityProfileSearchCriteriaTypeDef"] = None
    SearchFilter: Optional[SecurityProfilesSearchFilterTypeDef] = None

class SearchSecurityProfilesRequestSearchSecurityProfilesPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchCriteria: Optional[SecurityProfileSearchCriteriaTypeDef] = None
    SearchFilter: Optional[SecurityProfilesSearchFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ConnectionDataTypeDef(BaseValidatorModel):
    Attendee: Optional[AttendeeTypeDef] = None
    Meeting: Optional[MeetingTypeDef] = None

class DescribeRoutingProfileResponseTypeDef(BaseValidatorModel):
    RoutingProfile: RoutingProfileTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchRoutingProfilesResponseTypeDef(BaseValidatorModel):
    RoutingProfiles: List[RoutingProfileTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetCurrentMetricDataResponseTypeDef(BaseValidatorModel):
    MetricResults: List[CurrentMetricResultTypeDef]
    DataSnapshotTime: datetime
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class AssociateInstanceStorageConfigRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    StorageConfig: InstanceStorageConfigTypeDef

class DescribeInstanceStorageConfigResponseTypeDef(BaseValidatorModel):
    StorageConfig: InstanceStorageConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceStorageConfigsResponseTypeDef(BaseValidatorModel):
    StorageConfigs: List[InstanceStorageConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateInstanceStorageConfigRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType
    StorageConfig: InstanceStorageConfigTypeDef

class EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef(BaseValidatorModel):
    Options: List[EvaluationFormSingleSelectQuestionOptionTypeDef]
    DisplayAs: Optional[EvaluationFormSingleSelectQuestionDisplayModeType] = None
    Automation: Optional[EvaluationFormSingleSelectQuestionAutomationOutputTypeDef] = None

class EvaluationFormSingleSelectQuestionPropertiesTypeDef(BaseValidatorModel):
    Options: Sequence[EvaluationFormSingleSelectQuestionOptionTypeDef]
    DisplayAs: Optional[EvaluationFormSingleSelectQuestionDisplayModeType] = None
    Automation: Optional[EvaluationFormSingleSelectQuestionAutomationTypeDef] = None

class DescribeContactEvaluationResponseTypeDef(BaseValidatorModel):
    Evaluation: EvaluationTypeDef
    EvaluationForm: EvaluationFormContentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ContactTypeDef(BaseValidatorModel):
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

class RuleActionOutputTypeDef(BaseValidatorModel):
    ActionType: ActionTypeType
    TaskAction: Optional[TaskActionDefinitionOutputTypeDef] = None
    EventBridgeAction: Optional[EventBridgeActionDefinitionTypeDef] = None
    AssignContactCategoryAction: Optional[Dict[str, Any]] = None
    SendNotificationAction: Optional[SendNotificationActionDefinitionOutputTypeDef] = None
    CreateCaseAction: Optional[CreateCaseActionDefinitionOutputTypeDef] = None
    UpdateCaseAction: Optional[UpdateCaseActionDefinitionOutputTypeDef] = None
    EndAssociatedTasksAction: Optional[Dict[str, Any]] = None
    SubmitAutoEvaluationAction: Optional[SubmitAutoEvaluationActionDefinitionTypeDef] = None

class RuleActionTypeDef(BaseValidatorModel):
    ActionType: ActionTypeType
    TaskAction: Optional[TaskActionDefinitionTypeDef] = None
    EventBridgeAction: Optional[EventBridgeActionDefinitionTypeDef] = None
    AssignContactCategoryAction: Optional[Mapping[str, Any]] = None
    SendNotificationAction: Optional[SendNotificationActionDefinitionTypeDef] = None
    CreateCaseAction: Optional[CreateCaseActionDefinitionTypeDef] = None
    UpdateCaseAction: Optional[UpdateCaseActionDefinitionTypeDef] = None
    EndAssociatedTasksAction: Optional[Mapping[str, Any]] = None
    SubmitAutoEvaluationAction: Optional[SubmitAutoEvaluationActionDefinitionTypeDef] = None

class GetCurrentUserDataResponseTypeDef(BaseValidatorModel):
    UserDataList: List[UserDataTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class DescribeUserHierarchyGroupResponseTypeDef(BaseValidatorModel):
    HierarchyGroup: HierarchyGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class HistoricalMetricResultTypeDef(BaseValidatorModel):
    Dimensions: Optional[DimensionsTypeDef] = None
    Collections: Optional[List[HistoricalMetricDataTypeDef]] = None

class DescribeHoursOfOperationResponseTypeDef(BaseValidatorModel):
    HoursOfOperation: HoursOfOperationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchHoursOfOperationsResponseTypeDef(BaseValidatorModel):
    HoursOfOperations: List[HoursOfOperationTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetTaskTemplateResponseTypeDef(BaseValidatorModel):
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

class UpdateTaskTemplateResponseTypeDef(BaseValidatorModel):
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

class CreateTaskTemplateRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    Fields: Sequence[TaskTemplateFieldUnionTypeDef]
    Description: Optional[str] = None
    ContactFlowId: Optional[str] = None
    Constraints: Optional[TaskTemplateConstraintsTypeDef] = None
    Defaults: Optional[TaskTemplateDefaultsTypeDef] = None
    Status: Optional[TaskTemplateStatusType] = None
    ClientToken: Optional[str] = None

class UpdateTaskTemplateRequestRequestTypeDef(BaseValidatorModel):
    TaskTemplateId: str
    InstanceId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ContactFlowId: Optional[str] = None
    Constraints: Optional[TaskTemplateConstraintsTypeDef] = None
    Defaults: Optional[TaskTemplateDefaultsTypeDef] = None
    Status: Optional[TaskTemplateStatusType] = None
    Fields: Optional[Sequence[TaskTemplateFieldUnionTypeDef]] = None

class MetricResultV2TypeDef(BaseValidatorModel):
    Dimensions: Optional[Dict[str, str]] = None
    MetricInterval: Optional[MetricIntervalTypeDef] = None
    Collections: Optional[List[MetricDataV2TypeDef]] = None

class GetMetricDataV2RequestRequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Filters: Sequence[FilterV2TypeDef]
    Metrics: Sequence[MetricV2UnionTypeDef]
    Interval: Optional[IntervalDetailsTypeDef] = None
    Groupings: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class UpdateParticipantRoleConfigChannelInfoTypeDef(BaseValidatorModel):
    Chat: Optional[ChatParticipantRoleConfigTypeDef] = None

class DescribeQuickConnectResponseTypeDef(BaseValidatorModel):
    QuickConnect: QuickConnectTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class SearchQuickConnectsResponseTypeDef(BaseValidatorModel):
    QuickConnects: List[QuickConnectTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class RealTimeContactAnalysisCategoryDetailsTypeDef(BaseValidatorModel):
    PointsOfInterest: List[RealTimeContactAnalysisPointOfInterestTypeDef]

class RealTimeContactAnalysisSegmentIssuesTypeDef(BaseValidatorModel):
    IssuesDetected: List[RealTimeContactAnalysisIssueDetectedTypeDef]

class SearchCriteriaTypeDef(BaseValidatorModel):
    AgentIds: Optional[Sequence[str]] = None
    AgentHierarchyGroups: Optional[AgentHierarchyGroupsTypeDef] = None
    Channels: Optional[Sequence[ChannelType]] = None
    ContactAnalysis: Optional[ContactAnalysisTypeDef] = None
    InitiationMethods: Optional[Sequence[ContactInitiationMethodType]] = None
    QueueIds: Optional[Sequence[str]] = None
    SearchableContactAttributes: Optional[SearchableContactAttributesTypeDef] = None

class SearchUsersRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[UserSearchFilterTypeDef] = None
    SearchCriteria: Optional["UserSearchCriteriaTypeDef"] = None

class SearchUsersRequestSearchUsersPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[UserSearchFilterTypeDef] = None
    SearchCriteria: Optional[UserSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class StartWebRTCContactResponseTypeDef(BaseValidatorModel):
    ConnectionData: ConnectionDataTypeDef
    ContactId: str
    ParticipantId: str
    ParticipantToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class EvaluationFormQuestionTypePropertiesOutputTypeDef(BaseValidatorModel):
    Numeric: Optional[EvaluationFormNumericQuestionPropertiesOutputTypeDef] = None
    SingleSelect: Optional[EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef] = None

class EvaluationFormQuestionTypePropertiesTypeDef(BaseValidatorModel):
    Numeric: Optional[EvaluationFormNumericQuestionPropertiesTypeDef] = None
    SingleSelect: Optional[EvaluationFormSingleSelectQuestionPropertiesTypeDef] = None

class DescribeContactResponseTypeDef(BaseValidatorModel):
    Contact: ContactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class RuleTypeDef(BaseValidatorModel):
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

class GetMetricDataResponseTypeDef(BaseValidatorModel):
    MetricResults: List[HistoricalMetricResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class GetMetricDataV2ResponseTypeDef(BaseValidatorModel):
    MetricResults: List[MetricResultV2TypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class UpdateParticipantRoleConfigRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ChannelConfiguration: UpdateParticipantRoleConfigChannelInfoTypeDef

class RealTimeContactAnalysisSegmentCategoriesTypeDef(BaseValidatorModel):
    MatchedDetails: Dict[str, RealTimeContactAnalysisCategoryDetailsTypeDef]

class SearchContactsRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    TimeRange: SearchContactsTimeRangeTypeDef
    SearchCriteria: Optional[SearchCriteriaTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Sort: Optional[SortTypeDef] = None

class SearchContactsRequestSearchContactsPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    TimeRange: SearchContactsTimeRangeTypeDef
    SearchCriteria: Optional[SearchCriteriaTypeDef] = None
    Sort: Optional[SortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class EvaluationFormQuestionOutputTypeDef(BaseValidatorModel):
    Title: str
    RefId: str
    QuestionType: EvaluationFormQuestionTypeType
    Instructions: Optional[str] = None
    NotApplicableEnabled: Optional[bool] = None
    QuestionTypeProperties: Optional[EvaluationFormQuestionTypePropertiesOutputTypeDef] = None
    Weight: Optional[float] = None

class EvaluationFormQuestionTypeDef(BaseValidatorModel):
    Title: str
    RefId: str
    QuestionType: EvaluationFormQuestionTypeType
    Instructions: Optional[str] = None
    NotApplicableEnabled: Optional[bool] = None
    QuestionTypeProperties: Optional[EvaluationFormQuestionTypePropertiesTypeDef] = None
    Weight: Optional[float] = None

class DescribeRuleResponseTypeDef(BaseValidatorModel):
    Rule: RuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRuleRequestRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    TriggerEventSource: RuleTriggerEventSourceTypeDef
    Function: str
    Actions: Sequence[RuleActionUnionTypeDef]
    PublishStatus: RulePublishStatusType
    ClientToken: Optional[str] = None

class UpdateRuleRequestRequestTypeDef(BaseValidatorModel):
    RuleId: str
    InstanceId: str
    Name: str
    Function: str
    Actions: Sequence[RuleActionUnionTypeDef]
    PublishStatus: RulePublishStatusType

class RealtimeContactAnalysisSegmentTypeDef(BaseValidatorModel):
    Transcript: Optional[RealTimeContactAnalysisSegmentTranscriptTypeDef] = None
    Categories: Optional[RealTimeContactAnalysisSegmentCategoriesTypeDef] = None
    Issues: Optional[RealTimeContactAnalysisSegmentIssuesTypeDef] = None
    Event: Optional[RealTimeContactAnalysisSegmentEventTypeDef] = None
    Attachments: Optional[RealTimeContactAnalysisSegmentAttachmentsTypeDef] = None

class EvaluationFormItemOutputTypeDef(BaseValidatorModel):
    Section: Optional[Dict[str, Any]] = None
    Question: Optional[EvaluationFormQuestionOutputTypeDef] = None

class EvaluationFormItemTypeDef(BaseValidatorModel):
    Section: Optional[Dict[str, Any]] = None
    Question: Optional[EvaluationFormQuestionTypeDef] = None

class ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef(BaseValidatorModel):
    Channel: RealTimeContactAnalysisSupportedChannelType
    Status: RealTimeContactAnalysisStatusType
    Segments: List[RealtimeContactAnalysisSegmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

