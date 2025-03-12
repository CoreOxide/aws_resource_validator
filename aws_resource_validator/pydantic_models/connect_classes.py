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

class ActionSummaryTypeDef(BaseValidatorModel):
    ActionType: ActionTypeType


class ActivateEvaluationFormRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class EmailRecipientTypeDef(BaseValidatorModel):
    Address: Optional[str] = None
    DisplayName: Optional[str] = None


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
    ScreenShare: Optional[Literal["SEND"]] = None


class AudioQualityMetricsInfoTypeDef(BaseValidatorModel):
    QualityScore: Optional[float] = None
    PotentialQualityIssues: Optional[List[str]] = None


class AgentStatusReferenceTypeDef(BaseValidatorModel):
    StatusStartTimestamp: Optional[datetime] = None
    StatusArn: Optional[str] = None
    StatusName: Optional[str] = None


class AgentsCriteriaOutputTypeDef(BaseValidatorModel):
    AgentIds: Optional[List[str]] = None


class AgentsCriteriaTypeDef(BaseValidatorModel):
    AgentIds: Optional[Sequence[str]] = None


class AnalyticsDataAssociationResultTypeDef(BaseValidatorModel):
    DataSetId: Optional[str] = None
    TargetAccountId: Optional[str] = None
    ResourceShareId: Optional[str] = None
    ResourceShareArn: Optional[str] = None
    ResourceShareStatus: Optional[str] = None


class AnalyticsDataSetsResultTypeDef(BaseValidatorModel):
    DataSetId: Optional[str] = None
    DataSetName: Optional[str] = None


class AnswerMachineDetectionConfigTypeDef(BaseValidatorModel):
    EnableAnswerMachineDetection: Optional[bool] = None
    AwaitAnswerMachinePrompt: Optional[bool] = None


class ApplicationOutputTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    ApplicationPermissions: Optional[List[str]] = None


class ApplicationTypeDef(BaseValidatorModel):
    Namespace: Optional[str] = None
    ApplicationPermissions: Optional[Sequence[str]] = None


class AssociateAnalyticsDataSetRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DataSetId: str
    TargetAccountId: Optional[str] = None


class AssociateApprovedOriginRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Origin: str
    ClientToken: Optional[str] = None


class LexBotTypeDef(BaseValidatorModel):
    Name: str
    LexRegion: str


class LexV2BotTypeDef(BaseValidatorModel):
    AliasArn: Optional[str] = None


class AssociateDefaultVocabularyRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LanguageCode: VocabularyLanguageCodeType
    VocabularyId: Optional[str] = None


class AssociateFlowRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceId: str
    FlowId: str
    ResourceType: FlowAssociationResourceTypeType


class AssociateLambdaFunctionRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FunctionArn: str
    ClientToken: Optional[str] = None


class AssociatePhoneNumberContactFlowRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    InstanceId: str
    ContactFlowId: str


class AssociateQueueQuickConnectsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    QuickConnectIds: Sequence[str]


class AssociateSecurityKeyRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Key: str
    ClientToken: Optional[str] = None


class AssociateTrafficDistributionGroupUserRequestTypeDef(BaseValidatorModel):
    TrafficDistributionGroupId: str
    UserId: str
    InstanceId: str


class UserProficiencyTypeDef(BaseValidatorModel):
    AttributeName: str
    AttributeValue: str
    Level: float


class AssociatedContactSummaryTypeDef(BaseValidatorModel):
    ContactId: Optional[str] = None
    ContactArn: Optional[str] = None
    InitiationTimestamp: Optional[datetime] = None
    DisconnectTimestamp: Optional[datetime] = None
    InitialContactId: Optional[str] = None
    PreviousContactId: Optional[str] = None
    RelatedContactId: Optional[str] = None
    InitiationMethod: Optional[ContactInitiationMethodType] = None
    Channel: Optional[ChannelType] = None


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
    Arn: Optional[str] = None


class AttendeeTypeDef(BaseValidatorModel):
    AttendeeId: Optional[str] = None
    JoinToken: Optional[str] = None


class HierarchyGroupConditionTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    HierarchyGroupMatchType: Optional[HierarchyGroupMatchTypeType] = None


class TagConditionTypeDef(BaseValidatorModel):
    TagKey: Optional[str] = None
    TagValue: Optional[str] = None


class RangeTypeDef(BaseValidatorModel):
    MinProficiencyLevel: Optional[float] = None
    MaxProficiencyLevel: Optional[float] = None


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


class BatchAssociateAnalyticsDataSetRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DataSetIds: Sequence[str]
    TargetAccountId: Optional[str] = None


class ErrorResultTypeDef(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


class BatchDisassociateAnalyticsDataSetRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DataSetIds: Sequence[str]
    TargetAccountId: Optional[str] = None


class BatchGetAttachedFileMetadataRequestTypeDef(BaseValidatorModel):
    FileIds: Sequence[str]
    InstanceId: str
    AssociatedResourceArn: str


class BatchGetFlowAssociationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceIds: Sequence[str]
    ResourceType: Optional[ListFlowAssociationResourceTypeType] = None


class FlowAssociationSummaryTypeDef(BaseValidatorModel):
    ResourceId: Optional[str] = None
    FlowId: Optional[str] = None
    ResourceType: Optional[ListFlowAssociationResourceTypeType] = None


class FailedRequestTypeDef(BaseValidatorModel):
    RequestIdentifier: Optional[str] = None
    FailureReasonCode: Optional[FailureReasonCodeType] = None
    FailureReasonMessage: Optional[str] = None


class SuccessfulRequestTypeDef(BaseValidatorModel):
    RequestIdentifier: Optional[str] = None
    ContactId: Optional[str] = None


class CampaignTypeDef(BaseValidatorModel):
    CampaignId: Optional[str] = None


class ChatMessageTypeDef(BaseValidatorModel):
    ContentType: str
    Content: str


class ChatStreamingConfigurationTypeDef(BaseValidatorModel):
    StreamingEndpointArn: str


class ClaimPhoneNumberRequestTypeDef(BaseValidatorModel):
    PhoneNumber: str
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberDescription: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None


class PhoneNumberStatusTypeDef(BaseValidatorModel):
    Status: Optional[PhoneNumberWorkflowStatusType] = None
    Message: Optional[str] = None


class CompleteAttachedFileUploadRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str


class ContactConfigurationTypeDef(BaseValidatorModel):
    ContactId: str
    ParticipantRole: Optional[ParticipantRoleType] = None
    IncludeRawMessage: Optional[bool] = None


class ContactFilterTypeDef(BaseValidatorModel):
    ContactStates: Optional[Sequence[ContactStateType]] = None


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


class ContactFlowVersionSummaryTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    VersionDescription: Optional[str] = None
    Version: Optional[int] = None


class ContactSearchSummaryAgentInfoTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    ConnectedToAgentTimestamp: Optional[datetime] = None


class ContactSearchSummaryQueueInfoTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    EnqueueTimestamp: Optional[datetime] = None


class ContactSearchSummarySegmentAttributeValueTypeDef(BaseValidatorModel):
    ValueString: Optional[str] = None


class CustomerVoiceActivityTypeDef(BaseValidatorModel):
    GreetingStartTimestamp: Optional[datetime] = None
    GreetingEndTimestamp: Optional[datetime] = None


class DisconnectDetailsTypeDef(BaseValidatorModel):
    PotentialDisconnectIssue: Optional[str] = None


class QueueInfoTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    EnqueueTimestamp: Optional[datetime] = None


class SegmentAttributeValueOutputTypeDef(BaseValidatorModel):
    ValueString: Optional[str] = None
    ValueMap: Optional[Dict[str, Dict[str, Any]]] = None
    ValueInteger: Optional[int] = None


class WisdomInfoTypeDef(BaseValidatorModel):
    SessionArn: Optional[str] = None


class CreateAgentStatusRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    State: AgentStatusStateType
    Description: Optional[str] = None
    DisplayOrder: Optional[int] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateContactFlowModuleRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    Content: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None


class UserInfoTypeDef(BaseValidatorModel):
    UserId: Optional[str] = None


class CreateEmailAddressRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EmailAddress: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None


class EvaluationFormScoringStrategyTypeDef(BaseValidatorModel):
    Mode: EvaluationFormScoringModeType
    Status: EvaluationFormScoringStatusType


class CreateInstanceRequestTypeDef(BaseValidatorModel):
    IdentityManagementType: DirectoryTypeType
    InboundCallsEnabled: bool
    OutboundCallsEnabled: bool
    ClientToken: Optional[str] = None
    InstanceAlias: Optional[str] = None
    DirectoryId: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateIntegrationAssociationRequestTypeDef(BaseValidatorModel):
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


class CreatePersistentContactAssociationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    InitialContactId: str
    RehydrationType: RehydrationTypeType
    SourceContactId: str
    ClientToken: Optional[str] = None


class CreatePromptRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    S3Uri: str
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class OutboundCallerConfigTypeDef(BaseValidatorModel):
    OutboundCallerIdName: Optional[str] = None
    OutboundCallerIdNumberId: Optional[str] = None
    OutboundFlowId: Optional[str] = None


class OutboundEmailConfigTypeDef(BaseValidatorModel):
    OutboundEmailAddressId: Optional[str] = None


class RuleTriggerEventSourceTypeDef(BaseValidatorModel):
    EventSourceName: EventSourceNameType
    IntegrationAssociationId: Optional[str] = None


class CreateTrafficDistributionGroupRequestTypeDef(BaseValidatorModel):
    Name: str
    InstanceId: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class CreateUseCaseRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    UseCaseType: UseCaseTypeType
    Tags: Optional[Mapping[str, str]] = None


class CreateUserHierarchyGroupRequestTypeDef(BaseValidatorModel):
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


class CreateViewVersionRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    VersionDescription: Optional[str] = None
    ViewContentSha256: Optional[str] = None


class CreateVocabularyRequestTypeDef(BaseValidatorModel):
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


class DeactivateEvaluationFormRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int


class DefaultVocabularyTypeDef(BaseValidatorModel):
    InstanceId: str
    LanguageCode: VocabularyLanguageCodeType
    VocabularyId: str
    VocabularyName: str


class DeleteAttachedFileRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str


class DeleteContactEvaluationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str


class DeleteContactFlowModuleRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleId: str


class DeleteContactFlowRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str


class DeleteContactFlowVersionRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    ContactFlowVersion: int


class DeleteEmailAddressRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EmailAddressId: str


class DeleteEvaluationFormRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: Optional[int] = None


class DeleteHoursOfOperationOverrideRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    HoursOfOperationOverrideId: str


class DeleteHoursOfOperationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str


class DeleteInstanceRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ClientToken: Optional[str] = None


class DeleteIntegrationAssociationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str


class DeletePredefinedAttributeRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str


class DeletePromptRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    PromptId: str


class DeletePushNotificationRegistrationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RegistrationId: str
    ContactId: str


class DeleteQueueRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str


class DeleteQuickConnectRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str


class DeleteRoutingProfileRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str


class DeleteRuleRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RuleId: str


class DeleteSecurityProfileRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    SecurityProfileId: str


class DeleteTaskTemplateRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    TaskTemplateId: str


class DeleteTrafficDistributionGroupRequestTypeDef(BaseValidatorModel):
    TrafficDistributionGroupId: str


class DeleteUseCaseRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    UseCaseId: str


class DeleteUserHierarchyGroupRequestTypeDef(BaseValidatorModel):
    HierarchyGroupId: str
    InstanceId: str


class DeleteUserRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    UserId: str


class DeleteViewRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str


class DeleteViewVersionRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    ViewVersion: int


class DeleteVocabularyRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    VocabularyId: str


class DescribeAgentStatusRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AgentStatusId: str


class DescribeAuthenticationProfileRequestTypeDef(BaseValidatorModel):
    AuthenticationProfileId: str
    InstanceId: str


class DescribeContactEvaluationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str


class DescribeContactFlowModuleRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleId: str


class DescribeContactFlowRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str


class DescribeContactRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str


class DescribeEmailAddressRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EmailAddressId: str


class DescribeEvaluationFormRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: Optional[int] = None


class DescribeHoursOfOperationOverrideRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    HoursOfOperationOverrideId: str


class DescribeHoursOfOperationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str


class DescribeInstanceAttributeRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AttributeType: InstanceAttributeTypeType


class DescribeInstanceRequestTypeDef(BaseValidatorModel):
    InstanceId: str


class DescribeInstanceStorageConfigRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType


class DescribePhoneNumberRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str


class DescribePredefinedAttributeRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str


class DescribePromptRequestTypeDef(BaseValidatorModel):
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


class DescribeQueueRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str


class DescribeQuickConnectRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str


class DescribeRoutingProfileRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str


class DescribeRuleRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RuleId: str


class DescribeSecurityProfileRequestTypeDef(BaseValidatorModel):
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


class DescribeTrafficDistributionGroupRequestTypeDef(BaseValidatorModel):
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


class DescribeUserHierarchyGroupRequestTypeDef(BaseValidatorModel):
    HierarchyGroupId: str
    InstanceId: str


class DescribeUserHierarchyStructureRequestTypeDef(BaseValidatorModel):
    InstanceId: str


class DescribeUserRequestTypeDef(BaseValidatorModel):
    UserId: str
    InstanceId: str


class DescribeViewRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str


class DescribeVocabularyRequestTypeDef(BaseValidatorModel):
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


class DisassociateAnalyticsDataSetRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DataSetId: str
    TargetAccountId: Optional[str] = None


class DisassociateApprovedOriginRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Origin: str
    ClientToken: Optional[str] = None


class DisassociateFlowRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceId: str
    ResourceType: FlowAssociationResourceTypeType


class DisassociateInstanceStorageConfigRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType
    ClientToken: Optional[str] = None


class DisassociateLambdaFunctionRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FunctionArn: str
    ClientToken: Optional[str] = None


class DisassociateLexBotRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    BotName: str
    LexRegion: str
    ClientToken: Optional[str] = None


class DisassociatePhoneNumberContactFlowRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    InstanceId: str


class DisassociateQueueQuickConnectsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    QuickConnectIds: Sequence[str]


class RoutingProfileQueueReferenceTypeDef(BaseValidatorModel):
    QueueId: str
    Channel: ChannelType


class DisassociateSecurityKeyRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ClientToken: Optional[str] = None


class DisassociateTrafficDistributionGroupUserRequestTypeDef(BaseValidatorModel):
    TrafficDistributionGroupId: str
    UserId: str
    InstanceId: str


class UserProficiencyDisassociateTypeDef(BaseValidatorModel):
    AttributeName: str
    AttributeValue: str


class DisconnectReasonTypeDef(BaseValidatorModel):
    Code: Optional[str] = None


class DismissUserContactRequestTypeDef(BaseValidatorModel):
    UserId: str
    InstanceId: str
    ContactId: str


class DownloadUrlMetadataTypeDef(BaseValidatorModel):
    Url: Optional[str] = None
    UrlExpiry: Optional[str] = None


class EmailAddressInfoTypeDef(BaseValidatorModel):
    EmailAddress: str
    DisplayName: Optional[str] = None


class EmailAddressMetadataTypeDef(BaseValidatorModel):
    EmailAddressId: Optional[str] = None
    EmailAddressArn: Optional[str] = None
    EmailAddress: Optional[str] = None
    Description: Optional[str] = None
    DisplayName: Optional[str] = None


class EmailAttachmentTypeDef(BaseValidatorModel):
    FileName: str
    S3Url: str


class EmailMessageReferenceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Arn: Optional[str] = None


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


class EvaluationFormSectionOutputTypeDef(BaseValidatorModel):
    Title: str
    RefId: str
    Items: List[Dict[str, Any]]
    Instructions: Optional[str] = None
    Weight: Optional[float] = None


class NumericQuestionPropertyValueAutomationTypeDef(BaseValidatorModel):
    Label: NumericQuestionPropertyAutomationLabelType


class EvaluationFormNumericQuestionOptionTypeDef(BaseValidatorModel):
    MinValue: int
    MaxValue: int
    Score: Optional[int] = None
    AutomaticFail: Optional[bool] = None


class EvaluationFormSectionTypeDef(BaseValidatorModel):
    Title: str
    RefId: str
    Items: Sequence[Mapping[str, Any]]
    Instructions: Optional[str] = None
    Weight: Optional[float] = None


class SingleSelectQuestionRuleCategoryAutomationTypeDef(BaseValidatorModel):
    Category: str
    Condition: SingleSelectQuestionRuleCategoryAutomationConditionType
    OptionRefId: str


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


class GetAttachedFileRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str
    UrlExpiryInSeconds: Optional[int] = None


class GetContactAttributesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    InitialContactId: str


class GetEffectiveHoursOfOperationsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    FromDate: str
    ToDate: str


class GetFederationTokenRequestTypeDef(BaseValidatorModel):
    InstanceId: str


class GetFlowAssociationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceId: str
    ResourceType: FlowAssociationResourceTypeType


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class IntervalDetailsTypeDef(BaseValidatorModel):
    TimeZone: Optional[str] = None
    IntervalPeriod: Optional[IntervalPeriodType] = None


class GetPromptFileRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    PromptId: str


class GetTaskTemplateRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    TaskTemplateId: str
    SnapshotVersion: Optional[str] = None


class GetTrafficDistributionRequestTypeDef(BaseValidatorModel):
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


class OverrideTimeSliceTypeDef(BaseValidatorModel):
    Hours: int
    Minutes: int


class HoursOfOperationSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ImportPhoneNumberRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    SourcePhoneNumberArn: str
    PhoneNumberDescription: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None
    ClientToken: Optional[str] = None


class InboundRawMessageTypeDef(BaseValidatorModel):
    Subject: str
    Body: str
    ContentType: str
    Headers: Optional[Mapping[EmailHeaderTypeType, str]] = None


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


class ListAgentStatusRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AgentStatusTypes: Optional[Sequence[AgentStatusTypeType]] = None


class ListAnalyticsDataAssociationsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    DataSetId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAnalyticsDataLakeDataSetsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListApprovedOriginsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListAssociatedContactsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListAuthenticationProfilesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListBotsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LexVersion: LexVersionType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListContactEvaluationsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    NextToken: Optional[str] = None


class ListContactFlowModulesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ContactFlowModuleState: Optional[ContactFlowModuleStateType] = None


class ListContactFlowVersionsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListContactFlowsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowTypes: Optional[Sequence[ContactFlowTypeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListContactReferencesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ReferenceTypes: Sequence[ReferenceTypeType]
    NextToken: Optional[str] = None


class ListDefaultVocabulariesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LanguageCode: Optional[VocabularyLanguageCodeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEvaluationFormVersionsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListEvaluationFormsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListFlowAssociationsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceType: Optional[ListFlowAssociationResourceTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListHoursOfOperationOverridesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListHoursOfOperationsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListInstanceAttributesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListInstanceStorageConfigsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListInstancesRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListIntegrationAssociationsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationType: Optional[IntegrationTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IntegrationArn: Optional[str] = None


class ListLambdaFunctionsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListLexBotsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPhoneNumbersRequestTypeDef(BaseValidatorModel):
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


class ListPhoneNumbersV2RequestTypeDef(BaseValidatorModel):
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberPrefix: Optional[str] = None


class ListPredefinedAttributesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PredefinedAttributeSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ListPromptsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PromptSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ListQueueQuickConnectsRequestTypeDef(BaseValidatorModel):
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


class ListQueuesRequestTypeDef(BaseValidatorModel):
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


class ListQuickConnectsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuickConnectTypes: Optional[Sequence[QuickConnectTypeType]] = None


class ListRealtimeContactAnalysisSegmentsV2RequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    OutputType: RealTimeContactAnalysisOutputTypeType
    SegmentTypes: Sequence[RealTimeContactAnalysisSegmentTypeType]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRoutingProfileQueuesRequestTypeDef(BaseValidatorModel):
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


class ListRoutingProfilesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class RoutingProfileSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ListRulesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    PublishStatus: Optional[RulePublishStatusType] = None
    EventSourceName: Optional[EventSourceNameType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSecurityKeysRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SecurityKeyTypeDef(BaseValidatorModel):
    AssociationId: Optional[str] = None
    Key: Optional[str] = None
    CreationTime: Optional[datetime] = None


class ListSecurityProfileApplicationsRequestTypeDef(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSecurityProfilePermissionsRequestTypeDef(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListSecurityProfilesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SecurityProfileSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class ListTaskTemplatesRequestTypeDef(BaseValidatorModel):
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


class ListTrafficDistributionGroupUsersRequestTypeDef(BaseValidatorModel):
    TrafficDistributionGroupId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TrafficDistributionGroupUserSummaryTypeDef(BaseValidatorModel):
    UserId: Optional[str] = None


class ListTrafficDistributionGroupsRequestTypeDef(BaseValidatorModel):
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


class ListUseCasesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class UseCaseTypeDef(BaseValidatorModel):
    UseCaseId: Optional[str] = None
    UseCaseArn: Optional[str] = None
    UseCaseType: Optional[UseCaseTypeType] = None


class ListUserHierarchyGroupsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListUserProficienciesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    UserId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListUsersRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class UserSummaryTypeDef(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Username: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class ListViewVersionsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


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


class MonitorContactRequestTypeDef(BaseValidatorModel):
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


class OutboundRawMessageTypeDef(BaseValidatorModel):
    Subject: str
    Body: str
    ContentType: str


class ParticipantTimerValueTypeDef(BaseValidatorModel):
    ParticipantTimerAction: Optional[Literal["Unset"]] = None
    ParticipantTimerDurationInMinutes: Optional[int] = None


class PauseContactRequestTypeDef(BaseValidatorModel):
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


class PredefinedAttributeValuesTypeDef(BaseValidatorModel):
    StringList: Optional[Sequence[str]] = None


class PutUserStatusRequestTypeDef(BaseValidatorModel):
    UserId: str
    InstanceId: str
    AgentStatusId: str


class QueueInfoInputTypeDef(BaseValidatorModel):
    Id: Optional[str] = None


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


class RealTimeContactAnalysisSegmentPostContactSummaryTypeDef(BaseValidatorModel):
    Status: RealTimeContactAnalysisPostContactSummaryStatusType
    Content: Optional[str] = None
    FailureCode: Optional[RealTimeContactAnalysisPostContactSummaryFailureCodeType] = None


class StringReferenceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class UrlReferenceTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class ReleasePhoneNumberRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    ClientToken: Optional[str] = None


class ReplicateInstanceRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ReplicaRegion: str
    ReplicaAlias: str
    ClientToken: Optional[str] = None


class ReplicationStatusSummaryTypeDef(BaseValidatorModel):
    Region: Optional[str] = None
    ReplicationStatus: Optional[InstanceReplicationStatusType] = None
    ReplicationStatusReason: Optional[str] = None


class TagSearchConditionTypeDef(BaseValidatorModel):
    tagKey: Optional[str] = None
    tagValue: Optional[str] = None
    tagKeyComparisonType: Optional[StringComparisonTypeType] = None
    tagValueComparisonType: Optional[StringComparisonTypeType] = None


class ResumeContactRecordingRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    ContactRecordingType: Optional[ContactRecordingTypeType] = None


class ResumeContactRequestTypeDef(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    ContactFlowId: Optional[str] = None


class RoutingCriteriaInputStepExpiryTypeDef(BaseValidatorModel):
    DurationInSeconds: Optional[int] = None


class SubmitAutoEvaluationActionDefinitionTypeDef(BaseValidatorModel):
    EvaluationFormId: str


class SearchAvailablePhoneNumbersRequestTypeDef(BaseValidatorModel):
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


class SearchVocabulariesRequestTypeDef(BaseValidatorModel):
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


class SearchableSegmentAttributesCriteriaTypeDef(BaseValidatorModel):
    Key: str
    Values: Sequence[str]


class SegmentAttributeValueTypeDef(BaseValidatorModel):
    ValueString: Optional[str] = None
    ValueMap: Optional[Mapping[str, Mapping[str, Any]]] = None
    ValueInteger: Optional[int] = None


class SourceCampaignTypeDef(BaseValidatorModel):
    CampaignId: Optional[str] = None
    OutboundRequestId: Optional[str] = None


class SignInDistributionTypeDef(BaseValidatorModel):
    Region: str
    Enabled: bool


class UploadUrlMetadataTypeDef(BaseValidatorModel):
    Url: Optional[str] = None
    UrlExpiry: Optional[str] = None
    HeadersToInclude: Optional[Dict[str, str]] = None


class StartContactEvaluationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    EvaluationFormId: str
    ClientToken: Optional[str] = None


class VoiceRecordingConfigurationTypeDef(BaseValidatorModel):
    VoiceRecordingTrack: Optional[VoiceRecordingTrackType] = None
    IvrRecordingTrack: Optional[Literal["ALL"]] = None


class StartScreenSharingRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ClientToken: Optional[str] = None


class StopContactRecordingRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    ContactRecordingType: Optional[ContactRecordingTypeType] = None


class StopContactStreamingRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    StreamingId: str


class SuspendContactRecordingRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    ContactRecordingType: Optional[ContactRecordingTypeType] = None


class TagContactRequestTypeDef(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    Tags: Mapping[str, str]


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class TemplateAttributesTypeDef(BaseValidatorModel):
    CustomAttributes: Optional[Mapping[str, str]] = None
    CustomerProfileAttributes: Optional[str] = None


class TranscriptCriteriaTypeDef(BaseValidatorModel):
    ParticipantRole: ParticipantRoleType
    SearchText: Sequence[str]
    MatchType: SearchContactsMatchTypeType


class TransferContactRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ContactFlowId: str
    QueueId: Optional[str] = None
    UserId: Optional[str] = None
    ClientToken: Optional[str] = None


class UntagContactRequestTypeDef(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    TagKeys: Sequence[str]


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateAgentStatusRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AgentStatusId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[AgentStatusStateType] = None
    DisplayOrder: Optional[int] = None
    ResetOrderNumber: Optional[bool] = None


class UpdateAuthenticationProfileRequestTypeDef(BaseValidatorModel):
    AuthenticationProfileId: str
    InstanceId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    AllowedIps: Optional[Sequence[str]] = None
    BlockedIps: Optional[Sequence[str]] = None
    PeriodicSessionDuration: Optional[int] = None


class UpdateContactAttributesRequestTypeDef(BaseValidatorModel):
    InitialContactId: str
    InstanceId: str
    Attributes: Mapping[str, str]


class UpdateContactFlowContentRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    Content: str


class UpdateContactFlowMetadataRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ContactFlowState: Optional[ContactFlowStateType] = None


class UpdateContactFlowModuleContentRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleId: str
    Content: str


class UpdateContactFlowModuleMetadataRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[ContactFlowModuleStateType] = None


class UpdateContactFlowNameRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateEmailAddressMetadataRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EmailAddressId: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    ClientToken: Optional[str] = None


class UpdateInstanceAttributeRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AttributeType: InstanceAttributeTypeType
    Value: str
    ClientToken: Optional[str] = None


class UpdateParticipantAuthenticationRequestTypeDef(BaseValidatorModel):
    State: str
    InstanceId: str
    Code: Optional[str] = None
    Error: Optional[str] = None
    ErrorDescription: Optional[str] = None


class UpdatePhoneNumberMetadataRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    PhoneNumberDescription: Optional[str] = None
    ClientToken: Optional[str] = None


class UpdatePhoneNumberRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    ClientToken: Optional[str] = None


class UpdatePromptRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    PromptId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    S3Uri: Optional[str] = None


class UpdateQueueHoursOfOperationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    HoursOfOperationId: str


class UpdateQueueMaxContactsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    MaxContacts: Optional[int] = None


class UpdateQueueNameRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateQueueStatusRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    Status: QueueStatusType


class UpdateQuickConnectNameRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateRoutingProfileAgentAvailabilityTimerRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    AgentAvailabilityTimer: AgentAvailabilityTimerType


class UpdateRoutingProfileDefaultOutboundQueueRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    DefaultOutboundQueueId: str


class UpdateRoutingProfileNameRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


class UpdateUserHierarchyGroupNameRequestTypeDef(BaseValidatorModel):
    Name: str
    HierarchyGroupId: str
    InstanceId: str


class UpdateUserHierarchyRequestTypeDef(BaseValidatorModel):
    UserId: str
    InstanceId: str
    HierarchyGroupId: Optional[str] = None


class UpdateUserRoutingProfileRequestTypeDef(BaseValidatorModel):
    RoutingProfileId: str
    UserId: str
    InstanceId: str


class UpdateUserSecurityProfilesRequestTypeDef(BaseValidatorModel):
    SecurityProfileIds: Sequence[str]
    UserId: str
    InstanceId: str


class UpdateViewMetadataRequestTypeDef(BaseValidatorModel):
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
    FlowContentSha256: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateContactFlowVersionResponseTypeDef(BaseValidatorModel):
    ContactFlowArn: str
    Version: int
    ResponseMetadata: ResponseMetadataTypeDef


class CreateContactResponseTypeDef(BaseValidatorModel):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEmailAddressResponseTypeDef(BaseValidatorModel):
    EmailAddressId: str
    EmailAddressArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateEvaluationFormResponseTypeDef(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    ResponseMetadata: ResponseMetadataTypeDef


class CreateHoursOfOperationOverrideResponseTypeDef(BaseValidatorModel):
    HoursOfOperationOverrideId: str
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


class CreatePushNotificationRegistrationResponseTypeDef(BaseValidatorModel):
    RegistrationId: str
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


class DescribeEmailAddressResponseTypeDef(BaseValidatorModel):
    EmailAddressId: str
    EmailAddressArn: str
    EmailAddress: str
    DisplayName: str
    Description: str
    CreateTimestamp: str
    ModifiedTimestamp: str
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetContactAttributesResponseTypeDef(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class GetFlowAssociationResponseTypeDef(BaseValidatorModel):
    ResourceId: str
    FlowId: str
    ResourceType: FlowAssociationResourceTypeType
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


class StartEmailContactResponseTypeDef(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartOutboundChatContactResponseTypeDef(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadataTypeDef


class StartOutboundEmailContactResponseTypeDef(BaseValidatorModel):
    ContactId: str
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


class UpdateEmailAddressMetadataResponseTypeDef(BaseValidatorModel):
    EmailAddressId: str
    EmailAddressArn: str
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


class AdditionalEmailRecipientsTypeDef(BaseValidatorModel):
    ToList: Optional[List[EmailRecipientTypeDef]] = None
    CcList: Optional[List[EmailRecipientTypeDef]] = None


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


class StringConditionTypeDef(BaseValidatorModel):
    pass


class AgentStatusSearchCriteriaPaginatorTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class AgentStatusSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class ContactFlowModuleSearchCriteriaPaginatorTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    StateCondition: Optional[ContactFlowModuleStateType] = None
    StatusCondition: Optional[ContactFlowModuleStatusType] = None


class ContactFlowModuleSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    StateCondition: Optional[ContactFlowModuleStateType] = None
    StatusCondition: Optional[ContactFlowModuleStatusType] = None


class ContactFlowSearchCriteriaPaginatorTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    TypeCondition: Optional[ContactFlowTypeType] = None
    StateCondition: Optional[ContactFlowStateType] = None
    StatusCondition: Optional[ContactFlowStatusType] = None


class ContactFlowSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    TypeCondition: Optional[ContactFlowTypeType] = None
    StateCondition: Optional[ContactFlowStateType] = None
    StatusCondition: Optional[ContactFlowStatusType] = None


class EmailAddressSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class HoursOfOperationSearchCriteriaPaginatorTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class HoursOfOperationSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class PredefinedAttributeSearchCriteriaPaginatorTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class PredefinedAttributeSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class PromptSearchCriteriaPaginatorTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class PromptSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class QueueSearchCriteriaPaginatorTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    QueueTypeCondition: Optional[Literal["STANDARD"]] = None


class QueueSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    QueueTypeCondition: Optional[Literal["STANDARD"]] = None


class QuickConnectSearchCriteriaPaginatorTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class QuickConnectSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class RoutingProfileSearchCriteriaPaginatorTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class RoutingProfileSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class SecurityProfileSearchCriteriaPaginatorTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class SecurityProfileSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class UserHierarchyGroupSearchCriteriaPaginatorTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class UserHierarchyGroupSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None


class AgentStatusSummaryTypeDef(BaseValidatorModel):
    pass


class ListAgentStatusResponseTypeDef(BaseValidatorModel):
    AgentStatusSummaryList: List[AgentStatusSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AgentStatusTypeDef(BaseValidatorModel):
    pass


class DescribeAgentStatusResponseTypeDef(BaseValidatorModel):
    AgentStatus: AgentStatusTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SearchAgentStatusesResponseTypeDef(BaseValidatorModel):
    AgentStatuses: List[AgentStatusTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MatchCriteriaOutputTypeDef(BaseValidatorModel):
    AgentsCriteria: Optional[AgentsCriteriaOutputTypeDef] = None


class ListAnalyticsDataAssociationsResponseTypeDef(BaseValidatorModel):
    Results: List[AnalyticsDataAssociationResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListAnalyticsDataLakeDataSetsResponseTypeDef(BaseValidatorModel):
    Results: List[AnalyticsDataSetsResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListSecurityProfileApplicationsResponseTypeDef(BaseValidatorModel):
    Applications: List[ApplicationOutputTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AssociateLexBotRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LexBot: LexBotTypeDef
    ClientToken: Optional[str] = None


class ListLexBotsResponseTypeDef(BaseValidatorModel):
    LexBots: List[LexBotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AssociateBotRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LexBot: Optional[LexBotTypeDef] = None
    LexV2Bot: Optional[LexV2BotTypeDef] = None
    ClientToken: Optional[str] = None


class DisassociateBotRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    LexBot: Optional[LexBotTypeDef] = None
    LexV2Bot: Optional[LexV2BotTypeDef] = None
    ClientToken: Optional[str] = None


class LexBotConfigTypeDef(BaseValidatorModel):
    LexBot: Optional[LexBotTypeDef] = None
    LexV2Bot: Optional[LexV2BotTypeDef] = None


class AssociateUserProficienciesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiencyTypeDef]


class ListUserProficienciesResponseTypeDef(BaseValidatorModel):
    UserProficiencyList: List[UserProficiencyTypeDef]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateUserProficienciesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiencyTypeDef]


class ListAssociatedContactsResponseTypeDef(BaseValidatorModel):
    ContactSummaryList: List[AssociatedContactSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class AttachedFileTypeDef(BaseValidatorModel):
    CreationTime: str
    FileArn: str
    FileId: str
    FileName: str
    FileSizeInBytes: int
    FileStatus: FileStatusTypeType
    CreatedBy: Optional[CreatedByInfoTypeDef] = None
    FileUseCaseType: Optional[FileUseCaseTypeType] = None
    AssociatedResourceArn: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class StartAttachedFileUploadRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FileName: str
    FileSizeInBytes: int
    FileUseCaseType: FileUseCaseTypeType
    AssociatedResourceArn: str
    ClientToken: Optional[str] = None
    UrlExpiryInSeconds: Optional[int] = None
    CreatedBy: Optional[CreatedByInfoTypeDef] = None
    Tags: Optional[Mapping[str, str]] = None


class AttributeAndConditionTypeDef(BaseValidatorModel):
    TagConditions: Optional[Sequence[TagConditionTypeDef]] = None
    HierarchyGroupCondition: Optional[HierarchyGroupConditionTypeDef] = None


class CommonAttributeAndConditionTypeDef(BaseValidatorModel):
    TagConditions: Optional[Sequence[TagConditionTypeDef]] = None


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


class StartContactStreamingRequestTypeDef(BaseValidatorModel):
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


class NumberConditionTypeDef(BaseValidatorModel):
    pass


class ConditionTypeDef(BaseValidatorModel):
    StringCondition: Optional[StringConditionTypeDef] = None
    NumberCondition: Optional[NumberConditionTypeDef] = None


class CreatePushNotificationRegistrationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    PinpointAppArn: str
    DeviceToken: str
    DeviceType: DeviceTypeType
    ContactConfiguration: ContactConfigurationTypeDef
    ClientToken: Optional[str] = None


class EndpointTypeDef(BaseValidatorModel):
    pass


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


class ContactFlowTypeDef(BaseValidatorModel):
    pass


class DescribeContactFlowResponseTypeDef(BaseValidatorModel):
    ContactFlow: ContactFlowTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SearchContactFlowsResponseTypeDef(BaseValidatorModel):
    ContactFlows: List[ContactFlowTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ListContactFlowVersionsResponseTypeDef(BaseValidatorModel):
    ContactFlowVersionSummaryList: List[ContactFlowVersionSummaryTypeDef]
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
    SegmentAttributes: Optional[Dict[str, ContactSearchSummarySegmentAttributeValueTypeDef]] = None


class TimestampTypeDef(BaseValidatorModel):
    pass


class CreateContactFlowVersionRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    Description: Optional[str] = None
    FlowContentSha256: Optional[str] = None
    ContactFlowVersion: Optional[int] = None
    LastModifiedTime: Optional[TimestampTypeDef] = None
    LastModifiedRegion: Optional[str] = None


class UpdateContactScheduleRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ScheduledTime: TimestampTypeDef


class ReferenceTypeDef(BaseValidatorModel):
    pass


class StartOutboundVoiceContactRequestTypeDef(BaseValidatorModel):
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


class CreateParticipantRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ParticipantDetails: ParticipantDetailsToAddTypeDef
    ClientToken: Optional[str] = None


class CreateParticipantResponseTypeDef(BaseValidatorModel):
    ParticipantCredentials: ParticipantTokenCredentialsTypeDef
    ParticipantId: str
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateQueueOutboundCallerConfigRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    OutboundCallerConfig: OutboundCallerConfigTypeDef


class CreateQueueRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    HoursOfOperationId: str
    Description: Optional[str] = None
    OutboundCallerConfig: Optional[OutboundCallerConfigTypeDef] = None
    OutboundEmailConfig: Optional[OutboundEmailConfigTypeDef] = None
    MaxContacts: Optional[int] = None
    QuickConnectIds: Optional[Sequence[str]] = None
    Tags: Optional[Mapping[str, str]] = None


class QueueTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    QueueArn: Optional[str] = None
    QueueId: Optional[str] = None
    Description: Optional[str] = None
    OutboundCallerConfig: Optional[OutboundCallerConfigTypeDef] = None
    OutboundEmailConfig: Optional[OutboundEmailConfigTypeDef] = None
    HoursOfOperationId: Optional[str] = None
    MaxContacts: Optional[int] = None
    Status: Optional[QueueStatusType] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class UpdateQueueOutboundEmailConfigRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    OutboundEmailConfig: OutboundEmailConfigTypeDef


class UpdateUserIdentityInfoRequestTypeDef(BaseValidatorModel):
    IdentityInfo: UserIdentityInfoTypeDef
    UserId: str
    InstanceId: str


class CreateUserRequestTypeDef(BaseValidatorModel):
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


class UpdateUserPhoneConfigRequestTypeDef(BaseValidatorModel):
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


class CreateViewRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Status: ViewStatusType
    Content: ViewInputContentTypeDef
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Mapping[str, str]] = None


class UpdateViewContentRequestTypeDef(BaseValidatorModel):
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


class DateConditionTypeDef(BaseValidatorModel):
    pass


class HoursOfOperationOverrideSearchCriteriaPaginatorTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    DateCondition: Optional[DateConditionTypeDef] = None


class HoursOfOperationOverrideSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    DateCondition: Optional[DateConditionTypeDef] = None


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


class DisassociateRoutingProfileQueuesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    QueueReferences: Sequence[RoutingProfileQueueReferenceTypeDef]


class RoutingProfileQueueConfigTypeDef(BaseValidatorModel):
    QueueReference: RoutingProfileQueueReferenceTypeDef
    Priority: int
    Delay: int


class DisassociateUserProficienciesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    UserId: str
    UserProficiencies: Sequence[UserProficiencyDisassociateTypeDef]


class StopContactRequestTypeDef(BaseValidatorModel):
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
    FileUseCaseType: FileUseCaseTypeType
    CreatedBy: CreatedByInfoTypeDef
    DownloadUrlMetadata: DownloadUrlMetadataTypeDef
    Tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef


class InboundAdditionalRecipientsTypeDef(BaseValidatorModel):
    ToAddresses: Optional[Sequence[EmailAddressInfoTypeDef]] = None
    CcAddresses: Optional[Sequence[EmailAddressInfoTypeDef]] = None


class OutboundAdditionalRecipientsTypeDef(BaseValidatorModel):
    CcEmailAddresses: Optional[Sequence[EmailAddressInfoTypeDef]] = None


class SearchEmailAddressesResponseTypeDef(BaseValidatorModel):
    EmailAddresses: List[EmailAddressMetadataTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class FieldValueOutputTypeDef(BaseValidatorModel):
    Id: str
    Value: FieldValueUnionOutputTypeDef


class GetCurrentMetricDataRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Filters: FiltersTypeDef
    CurrentMetrics: Sequence[CurrentMetricTypeDef]
    Groupings: Optional[Sequence[GroupingType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortCriteria: Optional[Sequence[CurrentMetricSortCriteriaTypeDef]] = None


class ListAgentStatusRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    AgentStatusTypes: Optional[Sequence[AgentStatusTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListApprovedOriginsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListAuthenticationProfilesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListBotsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    LexVersion: LexVersionType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListContactEvaluationsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListContactFlowModulesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleState: Optional[ContactFlowModuleStateType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListContactFlowVersionsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListContactFlowsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactFlowTypes: Optional[Sequence[ContactFlowTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListContactReferencesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ReferenceTypes: Sequence[ReferenceTypeType]
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListDefaultVocabulariesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    LanguageCode: Optional[VocabularyLanguageCodeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEvaluationFormVersionsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListEvaluationFormsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListFlowAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceType: Optional[ListFlowAssociationResourceTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListHoursOfOperationOverridesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListHoursOfOperationsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInstanceAttributesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInstanceStorageConfigsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListInstancesRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListIntegrationAssociationsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationType: Optional[IntegrationTypeType] = None
    IntegrationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLambdaFunctionsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListLexBotsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPhoneNumbersRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPhoneNumbersV2RequestPaginateTypeDef(BaseValidatorModel):
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberCountryCodes: Optional[Sequence[PhoneNumberCountryCodeType]] = None
    PhoneNumberTypes: Optional[Sequence[PhoneNumberTypeType]] = None
    PhoneNumberPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPredefinedAttributesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPromptsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQueueQuickConnectsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQueuesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    QueueTypes: Optional[Sequence[QueueTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListQuickConnectsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    QuickConnectTypes: Optional[Sequence[QuickConnectTypeType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRoutingProfileQueuesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRoutingProfilesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRulesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PublishStatus: Optional[RulePublishStatusType] = None
    EventSourceName: Optional[EventSourceNameType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSecurityKeysRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSecurityProfileApplicationsRequestPaginateTypeDef(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSecurityProfilePermissionsRequestPaginateTypeDef(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSecurityProfilesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTaskTemplatesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    Status: Optional[TaskTemplateStatusType] = None
    Name: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTrafficDistributionGroupUsersRequestPaginateTypeDef(BaseValidatorModel):
    TrafficDistributionGroupId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListTrafficDistributionGroupsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUseCasesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUserHierarchyGroupsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUserProficienciesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    UserId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsersRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListViewVersionsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchAvailablePhoneNumbersRequestPaginateTypeDef(BaseValidatorModel):
    PhoneNumberCountryCode: PhoneNumberCountryCodeType
    PhoneNumberType: PhoneNumberTypeType
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberPrefix: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchVocabulariesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    State: Optional[VocabularyStateType] = None
    NameStartsWith: Optional[str] = None
    LanguageCode: Optional[VocabularyLanguageCodeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


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


class HoursOfOperationOverrideConfigTypeDef(BaseValidatorModel):
    Day: Optional[OverrideDaysType] = None
    StartTime: Optional[OverrideTimeSliceTypeDef] = None
    EndTime: Optional[OverrideTimeSliceTypeDef] = None


class OperationalHourTypeDef(BaseValidatorModel):
    Start: Optional[OverrideTimeSliceTypeDef] = None
    End: Optional[OverrideTimeSliceTypeDef] = None


class ListHoursOfOperationsResponseTypeDef(BaseValidatorModel):
    HoursOfOperationSummaryList: List[HoursOfOperationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class InboundEmailContentTypeDef(BaseValidatorModel):
    MessageSourceType: Literal["RAW"]
    RawMessage: Optional[InboundRawMessageTypeDef] = None


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


class ViewVersionSummaryTypeDef(BaseValidatorModel):
    pass


class ListViewVersionsResponseTypeDef(BaseValidatorModel):
    ViewVersionSummaryList: List[ViewVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ViewSummaryTypeDef(BaseValidatorModel):
    pass


class ListViewsResponseTypeDef(BaseValidatorModel):
    ViewsSummaryList: List[ViewSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class MetricV2OutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Threshold: Optional[List[ThresholdV2TypeDef]] = None
    MetricFilters: Optional[List[MetricFilterV2OutputTypeDef]] = None


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


class ParticipantTimerConfigurationTypeDef(BaseValidatorModel):
    ParticipantRole: TimerEligibleParticipantRolesType
    TimerType: ParticipantTimerTypeType
    TimerValue: ParticipantTimerValueTypeDef


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
    EmailMessage: Optional[EmailMessageReferenceTypeDef] = None
    String: Optional[StringReferenceTypeDef] = None
    Number: Optional[NumberReferenceTypeDef] = None
    Date: Optional[DateReferenceTypeDef] = None
    Email: Optional[EmailReferenceTypeDef] = None


class ReplicationConfigurationTypeDef(BaseValidatorModel):
    ReplicationStatusSummaryList: Optional[List[ReplicationStatusSummaryTypeDef]] = None
    SourceRegion: Optional[str] = None
    GlobalSignInEndpoint: Optional[str] = None


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


class SearchableSegmentAttributesTypeDef(BaseValidatorModel):
    Criteria: Sequence[SearchableSegmentAttributesCriteriaTypeDef]
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


class StartContactRecordingRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    InitialContactId: str
    VoiceRecordingConfiguration: VoiceRecordingConfigurationTypeDef


class TemplatedMessageConfigTypeDef(BaseValidatorModel):
    KnowledgeBaseId: str
    MessageTemplateId: str
    TemplateAttributes: TemplateAttributesTypeDef


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


class StartWebRTCContactRequestTypeDef(BaseValidatorModel):
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


class SearchPredefinedAttributesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchCriteria: Optional[PredefinedAttributeSearchCriteriaPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchPredefinedAttributesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchCriteria: Optional[PredefinedAttributeSearchCriteriaTypeDef] = None


class AttributeConditionOutputTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    ProficiencyLevel: Optional[float] = None
    Range: Optional[RangeTypeDef] = None
    MatchCriteria: Optional[MatchCriteriaOutputTypeDef] = None
    ComparisonOperator: Optional[str] = None


class AgentsCriteriaUnionTypeDef(BaseValidatorModel):
    pass


class MatchCriteriaTypeDef(BaseValidatorModel):
    AgentsCriteria: Optional[AgentsCriteriaUnionTypeDef] = None


class ApplicationUnionTypeDef(BaseValidatorModel):
    pass


class CreateSecurityProfileRequestTypeDef(BaseValidatorModel):
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


class UpdateSecurityProfileRequestTypeDef(BaseValidatorModel):
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


class ControlPlaneAttributeFilterTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[CommonAttributeAndConditionTypeDef]] = None
    AndCondition: Optional[CommonAttributeAndConditionTypeDef] = None
    TagCondition: Optional[TagConditionTypeDef] = None


class ContactFlowModuleSearchFilterTypeDef(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None


class ContactFlowSearchFilterTypeDef(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None


class EmailAddressSearchFilterTypeDef(BaseValidatorModel):
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


class ListConditionTypeDef(BaseValidatorModel):
    TargetListType: Optional[Literal["PROFICIENCIES"]] = None
    Conditions: Optional[Sequence[ConditionTypeDef]] = None


class BatchPutContactRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactDataRequestList: Sequence[ContactDataRequestTypeDef]
    ClientToken: Optional[str] = None


class GetCurrentUserDataRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Filters: UserDataFiltersTypeDef
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SearchContactsResponseTypeDef(BaseValidatorModel):
    Contacts: List[ContactSearchSummaryTypeDef]
    TotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class UpdateRoutingProfileConcurrencyRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    MediaConcurrencies: Sequence[MediaConcurrencyTypeDef]


class CurrentMetricResultTypeDef(BaseValidatorModel):
    Dimensions: Optional[DimensionsTypeDef] = None
    Collections: Optional[List[CurrentMetricDataTypeDef]] = None


class AssociateRoutingProfileQueuesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    QueueConfigs: Sequence[RoutingProfileQueueConfigTypeDef]


class CreateRoutingProfileRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    Description: str
    DefaultOutboundQueueId: str
    MediaConcurrencies: Sequence[MediaConcurrencyTypeDef]
    QueueConfigs: Optional[Sequence[RoutingProfileQueueConfigTypeDef]] = None
    Tags: Optional[Mapping[str, str]] = None
    AgentAvailabilityTimer: Optional[AgentAvailabilityTimerType] = None


class UpdateRoutingProfileQueuesRequestTypeDef(BaseValidatorModel):
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


class SubmitContactEvaluationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str
    Answers: Optional[Mapping[str, EvaluationAnswerInputTypeDef]] = None
    Notes: Optional[Mapping[str, EvaluationNoteTypeDef]] = None


class UpdateContactEvaluationRequestTypeDef(BaseValidatorModel):
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


class CreateCaseActionDefinitionOutputTypeDef(BaseValidatorModel):
    Fields: List[FieldValueOutputTypeDef]
    TemplateId: str


class UpdateCaseActionDefinitionOutputTypeDef(BaseValidatorModel):
    Fields: List[FieldValueOutputTypeDef]


class FieldValueUnionUnionTypeDef(BaseValidatorModel):
    pass


class FieldValueTypeDef(BaseValidatorModel):
    Id: str
    Value: FieldValueUnionUnionTypeDef


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


class UpdateUserHierarchyStructureRequestTypeDef(BaseValidatorModel):
    HierarchyStructure: HierarchyStructureUpdateTypeDef
    InstanceId: str


class GetMetricDataRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Filters: FiltersTypeDef
    HistoricalMetrics: Sequence[HistoricalMetricTypeDef]
    Groupings: Optional[Sequence[GroupingType]] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class GetMetricDataRequestTypeDef(BaseValidatorModel):
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


class CreateHoursOfOperationRequestTypeDef(BaseValidatorModel):
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


class UpdateHoursOfOperationRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    TimeZone: Optional[str] = None
    Config: Optional[Sequence[HoursOfOperationConfigTypeDef]] = None


class CreateHoursOfOperationOverrideRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    Name: str
    Config: Sequence[HoursOfOperationOverrideConfigTypeDef]
    EffectiveFrom: str
    EffectiveTill: str
    Description: Optional[str] = None


class HoursOfOperationOverrideTypeDef(BaseValidatorModel):
    HoursOfOperationOverrideId: Optional[str] = None
    HoursOfOperationId: Optional[str] = None
    HoursOfOperationArn: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    Config: Optional[List[HoursOfOperationOverrideConfigTypeDef]] = None
    EffectiveFrom: Optional[str] = None
    EffectiveTill: Optional[str] = None


class UpdateHoursOfOperationOverrideRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    HoursOfOperationOverrideId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Config: Optional[Sequence[HoursOfOperationOverrideConfigTypeDef]] = None
    EffectiveFrom: Optional[str] = None
    EffectiveTill: Optional[str] = None


class EffectiveHoursOfOperationsTypeDef(BaseValidatorModel):
    Date: Optional[str] = None
    OperationalHours: Optional[List[OperationalHourTypeDef]] = None


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


class MetricFilterV2UnionTypeDef(BaseValidatorModel):
    pass


class MetricV2TypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Threshold: Optional[Sequence[ThresholdV2TypeDef]] = None
    MetricFilters: Optional[Sequence[MetricFilterV2UnionTypeDef]] = None


class MetricDataV2TypeDef(BaseValidatorModel):
    Metric: Optional[MetricV2OutputTypeDef] = None
    Value: Optional[float] = None


class ChatEventTypeDef(BaseValidatorModel):
    pass


class SendChatIntegrationEventRequestTypeDef(BaseValidatorModel):
    SourceId: str
    DestinationId: str
    Event: ChatEventTypeDef
    Subtype: Optional[str] = None
    NewSessionDetails: Optional[NewSessionDetailsTypeDef] = None


class NotificationRecipientTypeUnionTypeDef(BaseValidatorModel):
    pass


class SendNotificationActionDefinitionTypeDef(BaseValidatorModel):
    DeliveryMethod: Literal["EMAIL"]
    Content: str
    ContentType: Literal["PLAIN_TEXT"]
    Recipient: NotificationRecipientTypeUnionTypeDef
    Subject: Optional[str] = None


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


class PredefinedAttributeValuesUnionTypeDef(BaseValidatorModel):
    pass


class CreatePredefinedAttributeRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    Values: PredefinedAttributeValuesUnionTypeDef


class UpdatePredefinedAttributeRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    Values: Optional[PredefinedAttributeValuesUnionTypeDef] = None


class CreateQuickConnectRequestTypeDef(BaseValidatorModel):
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


class UpdateQuickConnectConfigRequestTypeDef(BaseValidatorModel):
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
    TranscriptItems: Optional[ List[RealTimeContactAnalysisTranscriptItemWithCharacterOffsetsTypeDef] ] = None


class RealTimeContactAnalysisIssueDetectedTypeDef(BaseValidatorModel):
    TranscriptItems: List[RealTimeContactAnalysisTranscriptItemWithContentTypeDef]


class ListContactReferencesResponseTypeDef(BaseValidatorModel):
    ReferenceSummaryList: List[ReferenceSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeInstanceResponseTypeDef(BaseValidatorModel):
    Instance: InstanceTypeDef
    ReplicationConfiguration: ReplicationConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SearchResourceTagsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceTypes: Optional[Sequence[str]] = None
    SearchCriteria: Optional[ResourceTagsSearchCriteriaTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchResourceTagsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceTypes: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchCriteria: Optional[ResourceTagsSearchCriteriaTypeDef] = None


class SegmentAttributeValueUnionTypeDef(BaseValidatorModel):
    pass


class CreateContactRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Channel: ChannelType
    InitiationMethod: ContactInitiationMethodType
    ClientToken: Optional[str] = None
    RelatedContactId: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    References: Optional[Mapping[str, ReferenceTypeDef]] = None
    ExpiryDurationInMinutes: Optional[int] = None
    UserInfo: Optional[UserInfoTypeDef] = None
    InitiateAs: Optional[Literal["CONNECTED_TO_USER"]] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    SegmentAttributes: Optional[Mapping[str, SegmentAttributeValueUnionTypeDef]] = None
    PreviousContactId: Optional[str] = None


class StartChatContactRequestTypeDef(BaseValidatorModel):
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
    SegmentAttributes: Optional[Mapping[str, SegmentAttributeValueUnionTypeDef]] = None
    CustomerId: Optional[str] = None


class StartEmailContactRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FromEmailAddress: EmailAddressInfoTypeDef
    DestinationEmailAddress: str
    EmailMessage: InboundEmailContentTypeDef
    Description: Optional[str] = None
    References: Optional[Mapping[str, ReferenceTypeDef]] = None
    Name: Optional[str] = None
    AdditionalRecipients: Optional[InboundAdditionalRecipientsTypeDef] = None
    Attachments: Optional[Sequence[EmailAttachmentTypeDef]] = None
    ContactFlowId: Optional[str] = None
    RelatedContactId: Optional[str] = None
    Attributes: Optional[Mapping[str, str]] = None
    SegmentAttributes: Optional[Mapping[str, SegmentAttributeValueUnionTypeDef]] = None
    ClientToken: Optional[str] = None


class StartOutboundChatContactRequestTypeDef(BaseValidatorModel):
    SourceEndpoint: EndpointTypeDef
    DestinationEndpoint: EndpointTypeDef
    InstanceId: str
    SegmentAttributes: Mapping[str, SegmentAttributeValueUnionTypeDef]
    ContactFlowId: str
    Attributes: Optional[Mapping[str, str]] = None
    ChatDurationInMinutes: Optional[int] = None
    ParticipantDetails: Optional[ParticipantDetailsTypeDef] = None
    InitialSystemMessage: Optional[ChatMessageTypeDef] = None
    RelatedContactId: Optional[str] = None
    SupportedMessagingContentTypes: Optional[Sequence[str]] = None
    ClientToken: Optional[str] = None


class StartTaskContactRequestTypeDef(BaseValidatorModel):
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
    SegmentAttributes: Optional[Mapping[str, SegmentAttributeValueUnionTypeDef]] = None


class UpdateContactRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    References: Optional[Mapping[str, ReferenceTypeDef]] = None
    SegmentAttributes: Optional[Mapping[str, SegmentAttributeValueUnionTypeDef]] = None
    QueueInfo: Optional[QueueInfoInputTypeDef] = None
    UserInfo: Optional[UserInfoTypeDef] = None
    CustomerEndpoint: Optional[EndpointTypeDef] = None
    SystemEndpoint: Optional[EndpointTypeDef] = None


class GetTrafficDistributionResponseTypeDef(BaseValidatorModel):
    TelephonyConfig: TelephonyConfigOutputTypeDef
    Id: str
    Arn: str
    SignInConfig: SignInConfigOutputTypeDef
    AgentConfig: AgentConfigOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class OutboundEmailContentTypeDef(BaseValidatorModel):
    MessageSourceType: OutboundMessageSourceTypeType
    TemplatedMessageConfig: Optional[TemplatedMessageConfigTypeDef] = None
    RawMessage: Optional[OutboundRawMessageTypeDef] = None


class ContactAnalysisTypeDef(BaseValidatorModel):
    Transcript: Optional[TranscriptTypeDef] = None


class SearchUsersResponseTypeDef(BaseValidatorModel):
    Users: List[UserSearchSummaryTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ViewTypeDef(BaseValidatorModel):
    pass


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


class ExpressionOutputTypeDef(BaseValidatorModel):
    AttributeCondition: Optional[AttributeConditionOutputTypeDef] = None
    AndExpression: Optional[List[Dict[str, Any]]] = None
    OrExpression: Optional[List[Dict[str, Any]]] = None
    NotAttributeCondition: Optional[AttributeConditionOutputTypeDef] = None


class UserSearchFilterTypeDef(BaseValidatorModel):
    TagFilter: Optional[ControlPlaneTagFilterTypeDef] = None
    UserAttributeFilter: Optional[ControlPlaneUserAttributeFilterTypeDef] = None


class AgentStatusSearchFilterTypeDef(BaseValidatorModel):
    AttributeFilter: Optional[ControlPlaneAttributeFilterTypeDef] = None


class UserHierarchyGroupSearchFilterTypeDef(BaseValidatorModel):
    AttributeFilter: Optional[ControlPlaneAttributeFilterTypeDef] = None


class SearchContactFlowModulesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[ContactFlowModuleSearchFilterTypeDef] = None
    SearchCriteria: Optional[ContactFlowModuleSearchCriteriaPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchContactFlowModulesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[ContactFlowModuleSearchFilterTypeDef] = None
    SearchCriteria: Optional[ContactFlowModuleSearchCriteriaTypeDef] = None


class SearchContactFlowsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[ContactFlowSearchFilterTypeDef] = None
    SearchCriteria: Optional[ContactFlowSearchCriteriaPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchContactFlowsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[ContactFlowSearchFilterTypeDef] = None
    SearchCriteria: Optional[ContactFlowSearchCriteriaTypeDef] = None


class SearchEmailAddressesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    SearchCriteria: Optional[EmailAddressSearchCriteriaTypeDef] = None
    SearchFilter: Optional[EmailAddressSearchFilterTypeDef] = None


class SearchHoursOfOperationOverridesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[HoursOfOperationSearchFilterTypeDef] = None
    SearchCriteria: Optional[HoursOfOperationOverrideSearchCriteriaPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchHoursOfOperationOverridesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[HoursOfOperationSearchFilterTypeDef] = None
    SearchCriteria: Optional[HoursOfOperationOverrideSearchCriteriaTypeDef] = None


class SearchHoursOfOperationsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[HoursOfOperationSearchFilterTypeDef] = None
    SearchCriteria: Optional[HoursOfOperationSearchCriteriaPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchHoursOfOperationsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[HoursOfOperationSearchFilterTypeDef] = None
    SearchCriteria: Optional[HoursOfOperationSearchCriteriaTypeDef] = None


class SearchPromptsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[PromptSearchFilterTypeDef] = None
    SearchCriteria: Optional[PromptSearchCriteriaPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchPromptsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[PromptSearchFilterTypeDef] = None
    SearchCriteria: Optional[PromptSearchCriteriaTypeDef] = None


class SearchQueuesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[QueueSearchFilterTypeDef] = None
    SearchCriteria: Optional[QueueSearchCriteriaPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchQueuesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[QueueSearchFilterTypeDef] = None
    SearchCriteria: Optional[QueueSearchCriteriaTypeDef] = None


class SearchQuickConnectsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[QuickConnectSearchFilterTypeDef] = None
    SearchCriteria: Optional[QuickConnectSearchCriteriaPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchQuickConnectsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[QuickConnectSearchFilterTypeDef] = None
    SearchCriteria: Optional[QuickConnectSearchCriteriaTypeDef] = None


class SearchRoutingProfilesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[RoutingProfileSearchFilterTypeDef] = None
    SearchCriteria: Optional[RoutingProfileSearchCriteriaPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchRoutingProfilesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[RoutingProfileSearchFilterTypeDef] = None
    SearchCriteria: Optional[RoutingProfileSearchCriteriaTypeDef] = None


class SearchSecurityProfilesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchCriteria: Optional[SecurityProfileSearchCriteriaPaginatorTypeDef] = None
    SearchFilter: Optional[SecurityProfilesSearchFilterTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchSecurityProfilesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchCriteria: Optional[SecurityProfileSearchCriteriaTypeDef] = None
    SearchFilter: Optional[SecurityProfilesSearchFilterTypeDef] = None


class ConnectionDataTypeDef(BaseValidatorModel):
    Attendee: Optional[AttendeeTypeDef] = None
    Meeting: Optional[MeetingTypeDef] = None


class UserSearchCriteriaPaginatorTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    ListCondition: Optional[ListConditionTypeDef] = None
    HierarchyGroupCondition: Optional[HierarchyGroupConditionTypeDef] = None


class UserSearchCriteriaTypeDef(BaseValidatorModel):
    OrConditions: Optional[Sequence[Mapping[str, Any]]] = None
    AndConditions: Optional[Sequence[Mapping[str, Any]]] = None
    StringCondition: Optional[StringConditionTypeDef] = None
    ListCondition: Optional[ListConditionTypeDef] = None
    HierarchyGroupCondition: Optional[HierarchyGroupConditionTypeDef] = None


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


class AssociateInstanceStorageConfigRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    StorageConfig: InstanceStorageConfigTypeDef
    ClientToken: Optional[str] = None


class DescribeInstanceStorageConfigResponseTypeDef(BaseValidatorModel):
    StorageConfig: InstanceStorageConfigTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListInstanceStorageConfigsResponseTypeDef(BaseValidatorModel):
    StorageConfigs: List[InstanceStorageConfigTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateInstanceStorageConfigRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType
    StorageConfig: InstanceStorageConfigTypeDef
    ClientToken: Optional[str] = None


class EvaluationFormSingleSelectQuestionOptionTypeDef(BaseValidatorModel):
    pass


class EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef(BaseValidatorModel):
    Options: List[EvaluationFormSingleSelectQuestionOptionTypeDef]
    DisplayAs: Optional[EvaluationFormSingleSelectQuestionDisplayModeType] = None
    Automation: Optional[EvaluationFormSingleSelectQuestionAutomationOutputTypeDef] = None


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


class GetCurrentUserDataResponseTypeDef(BaseValidatorModel):
    UserDataList: List[UserDataTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeUserHierarchyGroupResponseTypeDef(BaseValidatorModel):
    HierarchyGroup: HierarchyGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class SearchUserHierarchyGroupsResponseTypeDef(BaseValidatorModel):
    UserHierarchyGroups: List[HierarchyGroupTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class DescribeHoursOfOperationOverrideResponseTypeDef(BaseValidatorModel):
    HoursOfOperationOverride: HoursOfOperationOverrideTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListHoursOfOperationOverridesResponseTypeDef(BaseValidatorModel):
    HoursOfOperationOverrideList: List[HoursOfOperationOverrideTypeDef]
    LastModifiedRegion: str
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class SearchHoursOfOperationOverridesResponseTypeDef(BaseValidatorModel):
    HoursOfOperationOverrides: List[HoursOfOperationOverrideTypeDef]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class GetEffectiveHoursOfOperationsResponseTypeDef(BaseValidatorModel):
    EffectiveHoursOfOperationList: List[EffectiveHoursOfOperationsTypeDef]
    TimeZone: str
    ResponseMetadata: ResponseMetadataTypeDef


class TaskTemplateFieldOutputTypeDef(BaseValidatorModel):
    pass


class GetTaskTemplateResponseTypeDef(BaseValidatorModel):
    InstanceId: str
    Id: str
    Arn: str
    Name: str
    Description: str
    ContactFlowId: str
    SelfAssignFlowId: str
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
    SelfAssignFlowId: str
    Constraints: TaskTemplateConstraintsOutputTypeDef
    Defaults: TaskTemplateDefaultsOutputTypeDef
    Fields: List[TaskTemplateFieldOutputTypeDef]
    Status: TaskTemplateStatusType
    LastModifiedTime: datetime
    CreatedTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class MetricResultV2TypeDef(BaseValidatorModel):
    Dimensions: Optional[Dict[str, str]] = None
    MetricInterval: Optional[MetricIntervalTypeDef] = None
    Collections: Optional[List[MetricDataV2TypeDef]] = None


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


class TelephonyConfigUnionTypeDef(BaseValidatorModel):
    pass


class AgentConfigUnionTypeDef(BaseValidatorModel):
    pass


class SignInConfigUnionTypeDef(BaseValidatorModel):
    pass


class UpdateTrafficDistributionRequestTypeDef(BaseValidatorModel):
    Id: str
    TelephonyConfig: Optional[TelephonyConfigUnionTypeDef] = None
    SignInConfig: Optional[SignInConfigUnionTypeDef] = None
    AgentConfig: Optional[AgentConfigUnionTypeDef] = None


class SendOutboundEmailRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    FromEmailAddress: EmailAddressInfoTypeDef
    DestinationEmailAddress: EmailAddressInfoTypeDef
    EmailMessage: OutboundEmailContentTypeDef
    TrafficType: TrafficTypeType
    AdditionalRecipients: Optional[OutboundAdditionalRecipientsTypeDef] = None
    SourceCampaign: Optional[SourceCampaignTypeDef] = None
    ClientToken: Optional[str] = None


class StartOutboundEmailContactRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    DestinationEmailAddress: EmailAddressInfoTypeDef
    EmailMessage: OutboundEmailContentTypeDef
    FromEmailAddress: Optional[EmailAddressInfoTypeDef] = None
    AdditionalRecipients: Optional[OutboundAdditionalRecipientsTypeDef] = None
    ClientToken: Optional[str] = None


class SearchCriteriaTypeDef(BaseValidatorModel):
    AgentIds: Optional[Sequence[str]] = None
    AgentHierarchyGroups: Optional[AgentHierarchyGroupsTypeDef] = None
    Channels: Optional[Sequence[ChannelType]] = None
    ContactAnalysis: Optional[ContactAnalysisTypeDef] = None
    InitiationMethods: Optional[Sequence[ContactInitiationMethodType]] = None
    QueueIds: Optional[Sequence[str]] = None
    SearchableContactAttributes: Optional[SearchableContactAttributesTypeDef] = None
    SearchableSegmentAttributes: Optional[SearchableSegmentAttributesTypeDef] = None


class StepTypeDef(BaseValidatorModel):
    Expiry: Optional[ExpiryTypeDef] = None
    Expression: Optional[ExpressionOutputTypeDef] = None
    Status: Optional[RoutingCriteriaStepStatusType] = None


class MatchCriteriaUnionTypeDef(BaseValidatorModel):
    pass


class AttributeConditionTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None
    ProficiencyLevel: Optional[float] = None
    Range: Optional[RangeTypeDef] = None
    MatchCriteria: Optional[MatchCriteriaUnionTypeDef] = None
    ComparisonOperator: Optional[str] = None


class SearchAgentStatusesRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[AgentStatusSearchFilterTypeDef] = None
    SearchCriteria: Optional[AgentStatusSearchCriteriaPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchAgentStatusesRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[AgentStatusSearchFilterTypeDef] = None
    SearchCriteria: Optional[AgentStatusSearchCriteriaTypeDef] = None


class SearchUserHierarchyGroupsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[UserHierarchyGroupSearchFilterTypeDef] = None
    SearchCriteria: Optional[UserHierarchyGroupSearchCriteriaPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchUserHierarchyGroupsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[UserHierarchyGroupSearchFilterTypeDef] = None
    SearchCriteria: Optional[UserHierarchyGroupSearchCriteriaTypeDef] = None


class StartWebRTCContactResponseTypeDef(BaseValidatorModel):
    ConnectionData: ConnectionDataTypeDef
    ContactId: str
    ParticipantId: str
    ParticipantToken: str
    ResponseMetadata: ResponseMetadataTypeDef


class SearchUsersRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    SearchFilter: Optional[UserSearchFilterTypeDef] = None
    SearchCriteria: Optional[UserSearchCriteriaPaginatorTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchUsersRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[UserSearchFilterTypeDef] = None
    SearchCriteria: Optional[UserSearchCriteriaTypeDef] = None


class EvaluationFormQuestionTypePropertiesOutputTypeDef(BaseValidatorModel):
    Numeric: Optional[EvaluationFormNumericQuestionPropertiesOutputTypeDef] = None
    SingleSelect: Optional[EvaluationFormSingleSelectQuestionPropertiesOutputTypeDef] = None


class EvaluationFormSingleSelectQuestionAutomationUnionTypeDef(BaseValidatorModel):
    pass


class EvaluationFormSingleSelectQuestionPropertiesTypeDef(BaseValidatorModel):
    Options: Sequence[EvaluationFormSingleSelectQuestionOptionTypeDef]
    DisplayAs: Optional[EvaluationFormSingleSelectQuestionDisplayModeType] = None
    Automation: Optional[EvaluationFormSingleSelectQuestionAutomationUnionTypeDef] = None


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


class FieldValueUnionExtraTypeDef(BaseValidatorModel):
    pass


class CreateCaseActionDefinitionTypeDef(BaseValidatorModel):
    Fields: Sequence[FieldValueUnionExtraTypeDef]
    TemplateId: str


class UpdateCaseActionDefinitionTypeDef(BaseValidatorModel):
    Fields: Sequence[FieldValueUnionExtraTypeDef]


class GetMetricDataResponseTypeDef(BaseValidatorModel):
    MetricResults: List[HistoricalMetricResultTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class TaskTemplateFieldUnionTypeDef(BaseValidatorModel):
    pass


class TaskTemplateDefaultsUnionTypeDef(BaseValidatorModel):
    pass


class TaskTemplateConstraintsUnionTypeDef(BaseValidatorModel):
    pass


class CreateTaskTemplateRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    Fields: Sequence[TaskTemplateFieldUnionTypeDef]
    Description: Optional[str] = None
    ContactFlowId: Optional[str] = None
    SelfAssignFlowId: Optional[str] = None
    Constraints: Optional[TaskTemplateConstraintsUnionTypeDef] = None
    Defaults: Optional[TaskTemplateDefaultsUnionTypeDef] = None
    Status: Optional[TaskTemplateStatusType] = None
    ClientToken: Optional[str] = None


class UpdateTaskTemplateRequestTypeDef(BaseValidatorModel):
    TaskTemplateId: str
    InstanceId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    ContactFlowId: Optional[str] = None
    SelfAssignFlowId: Optional[str] = None
    Constraints: Optional[TaskTemplateConstraintsUnionTypeDef] = None
    Defaults: Optional[TaskTemplateDefaultsUnionTypeDef] = None
    Status: Optional[TaskTemplateStatusType] = None
    Fields: Optional[Sequence[TaskTemplateFieldUnionTypeDef]] = None


class MetricV2UnionTypeDef(BaseValidatorModel):
    pass


class GetMetricDataV2RequestTypeDef(BaseValidatorModel):
    ResourceArn: str
    StartTime: TimestampTypeDef
    EndTime: TimestampTypeDef
    Filters: Sequence[FilterV2TypeDef]
    Metrics: Sequence[MetricV2UnionTypeDef]
    Interval: Optional[IntervalDetailsTypeDef] = None
    Groupings: Optional[Sequence[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class GetMetricDataV2ResponseTypeDef(BaseValidatorModel):
    MetricResults: List[MetricResultV2TypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateParticipantRoleConfigRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ChannelConfiguration: UpdateParticipantRoleConfigChannelInfoTypeDef


class RealTimeContactAnalysisSegmentCategoriesTypeDef(BaseValidatorModel):
    MatchedDetails: Dict[str, RealTimeContactAnalysisCategoryDetailsTypeDef]


class SearchContactsTimeRangeTypeDef(BaseValidatorModel):
    pass


class SearchContactsRequestPaginateTypeDef(BaseValidatorModel):
    InstanceId: str
    TimeRange: SearchContactsTimeRangeTypeDef
    SearchCriteria: Optional[SearchCriteriaTypeDef] = None
    Sort: Optional[SortTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class SearchContactsRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    TimeRange: SearchContactsTimeRangeTypeDef
    SearchCriteria: Optional[SearchCriteriaTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    Sort: Optional[SortTypeDef] = None


class RoutingCriteriaTypeDef(BaseValidatorModel):
    Steps: Optional[List[StepTypeDef]] = None
    ActivationTimestamp: Optional[datetime] = None
    Index: Optional[int] = None


class EvaluationFormQuestionOutputTypeDef(BaseValidatorModel):
    Title: str
    RefId: str
    QuestionType: EvaluationFormQuestionTypeType
    Instructions: Optional[str] = None
    NotApplicableEnabled: Optional[bool] = None
    QuestionTypeProperties: Optional[EvaluationFormQuestionTypePropertiesOutputTypeDef] = None
    Weight: Optional[float] = None


class DescribeRuleResponseTypeDef(BaseValidatorModel):
    Rule: RuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class RealtimeContactAnalysisSegmentTypeDef(BaseValidatorModel):
    Transcript: Optional[RealTimeContactAnalysisSegmentTranscriptTypeDef] = None
    Categories: Optional[RealTimeContactAnalysisSegmentCategoriesTypeDef] = None
    Issues: Optional[RealTimeContactAnalysisSegmentIssuesTypeDef] = None
    Event: Optional[RealTimeContactAnalysisSegmentEventTypeDef] = None
    Attachments: Optional[RealTimeContactAnalysisSegmentAttachmentsTypeDef] = None
    PostContactSummary: Optional[RealTimeContactAnalysisSegmentPostContactSummaryTypeDef] = None


class EndpointInfoTypeDef(BaseValidatorModel):
    pass


class ContactTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    InitialContactId: Optional[str] = None
    PreviousContactId: Optional[str] = None
    ContactAssociationId: Optional[str] = None
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
    CustomerId: Optional[str] = None
    CustomerEndpoint: Optional[EndpointInfoTypeDef] = None
    SystemEndpoint: Optional[EndpointInfoTypeDef] = None
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
    AdditionalEmailRecipients: Optional[AdditionalEmailRecipientsTypeDef] = None
    SegmentAttributes: Optional[Dict[str, SegmentAttributeValueOutputTypeDef]] = None


class AttributeConditionUnionTypeDef(BaseValidatorModel):
    pass


class ExpressionTypeDef(BaseValidatorModel):
    AttributeCondition: Optional[AttributeConditionUnionTypeDef] = None
    AndExpression: Optional[Sequence[Mapping[str, Any]]] = None
    OrExpression: Optional[Sequence[Mapping[str, Any]]] = None
    NotAttributeCondition: Optional[AttributeConditionUnionTypeDef] = None


class EvaluationFormItemOutputTypeDef(BaseValidatorModel):
    Section: Optional[EvaluationFormSectionOutputTypeDef] = None
    Question: Optional[EvaluationFormQuestionOutputTypeDef] = None


class EvaluationFormSingleSelectQuestionPropertiesUnionTypeDef(BaseValidatorModel):
    pass


class EvaluationFormNumericQuestionPropertiesUnionTypeDef(BaseValidatorModel):
    pass


class EvaluationFormQuestionTypePropertiesTypeDef(BaseValidatorModel):
    Numeric: Optional[EvaluationFormNumericQuestionPropertiesUnionTypeDef] = None
    SingleSelect: Optional[EvaluationFormSingleSelectQuestionPropertiesUnionTypeDef] = None


class CreateCaseActionDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class UpdateCaseActionDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class SendNotificationActionDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class TaskActionDefinitionUnionTypeDef(BaseValidatorModel):
    pass


class RuleActionTypeDef(BaseValidatorModel):
    ActionType: ActionTypeType
    TaskAction: Optional[TaskActionDefinitionUnionTypeDef] = None
    EventBridgeAction: Optional[EventBridgeActionDefinitionTypeDef] = None
    AssignContactCategoryAction: Optional[Mapping[str, Any]] = None
    SendNotificationAction: Optional[SendNotificationActionDefinitionUnionTypeDef] = None
    CreateCaseAction: Optional[CreateCaseActionDefinitionUnionTypeDef] = None
    UpdateCaseAction: Optional[UpdateCaseActionDefinitionUnionTypeDef] = None
    EndAssociatedTasksAction: Optional[Mapping[str, Any]] = None
    SubmitAutoEvaluationAction: Optional[SubmitAutoEvaluationActionDefinitionTypeDef] = None


class ListRealtimeContactAnalysisSegmentsV2ResponseTypeDef(BaseValidatorModel):
    Channel: RealTimeContactAnalysisSupportedChannelType
    Status: RealTimeContactAnalysisStatusType
    Segments: List[RealtimeContactAnalysisSegmentTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class DescribeContactResponseTypeDef(BaseValidatorModel):
    Contact: ContactTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EvaluationFormContentTypeDef(BaseValidatorModel):
    EvaluationFormVersion: int
    EvaluationFormId: str
    EvaluationFormArn: str
    Title: str
    Items: List[EvaluationFormItemOutputTypeDef]
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategyTypeDef] = None


class EvaluationFormTypeDef(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormVersion: int
    Locked: bool
    EvaluationFormArn: str
    Title: str
    Status: EvaluationFormVersionStatusType
    Items: List[EvaluationFormItemOutputTypeDef]
    CreatedTime: datetime
    CreatedBy: str
    LastModifiedTime: datetime
    LastModifiedBy: str
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategyTypeDef] = None
    Tags: Optional[Dict[str, str]] = None


class ExpressionUnionTypeDef(BaseValidatorModel):
    pass


class RoutingCriteriaInputStepTypeDef(BaseValidatorModel):
    Expiry: Optional[RoutingCriteriaInputStepExpiryTypeDef] = None
    Expression: Optional[ExpressionUnionTypeDef] = None


class DescribeContactEvaluationResponseTypeDef(BaseValidatorModel):
    Evaluation: EvaluationTypeDef
    EvaluationForm: EvaluationFormContentTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class DescribeEvaluationFormResponseTypeDef(BaseValidatorModel):
    EvaluationForm: EvaluationFormTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class EvaluationFormQuestionTypePropertiesUnionTypeDef(BaseValidatorModel):
    pass


class EvaluationFormQuestionTypeDef(BaseValidatorModel):
    Title: str
    RefId: str
    QuestionType: EvaluationFormQuestionTypeType
    Instructions: Optional[str] = None
    NotApplicableEnabled: Optional[bool] = None
    QuestionTypeProperties: Optional[EvaluationFormQuestionTypePropertiesUnionTypeDef] = None
    Weight: Optional[float] = None


class RuleActionUnionTypeDef(BaseValidatorModel):
    pass


class CreateRuleRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Name: str
    TriggerEventSource: RuleTriggerEventSourceTypeDef
    Function: str
    Actions: Sequence[RuleActionUnionTypeDef]
    PublishStatus: RulePublishStatusType
    ClientToken: Optional[str] = None


class UpdateRuleRequestTypeDef(BaseValidatorModel):
    RuleId: str
    InstanceId: str
    Name: str
    Function: str
    Actions: Sequence[RuleActionUnionTypeDef]
    PublishStatus: RulePublishStatusType


class RoutingCriteriaInputTypeDef(BaseValidatorModel):
    Steps: Optional[Sequence[RoutingCriteriaInputStepTypeDef]] = None


class UpdateContactRoutingDataRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    QueueTimeAdjustmentSeconds: Optional[int] = None
    QueuePriority: Optional[int] = None
    RoutingCriteria: Optional[RoutingCriteriaInputTypeDef] = None


class EvaluationFormQuestionUnionTypeDef(BaseValidatorModel):
    pass


class EvaluationFormSectionUnionTypeDef(BaseValidatorModel):
    pass


class EvaluationFormItemTypeDef(BaseValidatorModel):
    Section: Optional[EvaluationFormSectionUnionTypeDef] = None
    Question: Optional[EvaluationFormQuestionUnionTypeDef] = None


class EvaluationFormItemUnionTypeDef(BaseValidatorModel):
    pass


class CreateEvaluationFormRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    Title: str
    Items: Sequence[EvaluationFormItemUnionTypeDef]
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategyTypeDef] = None
    ClientToken: Optional[str] = None


class UpdateEvaluationFormRequestTypeDef(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int
    Title: str
    Items: Sequence[EvaluationFormItemUnionTypeDef]
    CreateNewVersion: Optional[bool] = None
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategyTypeDef] = None
    ClientToken: Optional[str] = None


