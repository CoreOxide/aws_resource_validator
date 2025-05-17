from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.connect.connect_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ActionSummary(BaseValidatorModel):
    ActionType: ActionTypeType


# This class is the input for the 'activate_evaluation_form' function.
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
    L1Ids: Optional[List[str]] = None
    L2Ids: Optional[List[str]] = None
    L3Ids: Optional[List[str]] = None
    L4Ids: Optional[List[str]] = None
    L5Ids: Optional[List[str]] = None


class DeviceInfo(BaseValidatorModel):
    PlatformName: Optional[str] = None
    PlatformVersion: Optional[str] = None
    OperatingSystem: Optional[str] = None


class ParticipantCapabilities(BaseValidatorModel):
    Video: Optional[Literal['SEND']] = None
    ScreenShare: Optional[Literal['SEND']] = None


class AudioQualityMetricsInfo(BaseValidatorModel):
    QualityScore: Optional[float] = None
    PotentialQualityIssues: Optional[List[str]] = None


class AgentStatusReference(BaseValidatorModel):
    StatusStartTimestamp: Optional[datetime] = None
    StatusArn: Optional[str] = None
    StatusName: Optional[str] = None


class StringCondition(BaseValidatorModel):
    FieldName: Optional[str] = None
    Value: Optional[str] = None
    ComparisonType: Optional[StringComparisonTypeType] = None


class AgentStatusSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[AgentStatusTypeType] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


class AgentStatus(BaseValidatorModel):
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


class AgentsCriteriaOutput(BaseValidatorModel):
    AgentIds: Optional[List[str]] = None


class AgentsCriteria(BaseValidatorModel):
    AgentIds: Optional[List[str]] = None


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
    ApplicationPermissions: Optional[List[str]] = None


# This class is the input for the 'associate_analytics_data_set' function.
class AssociateAnalyticsDataSetRequest(BaseValidatorModel):
    InstanceId: str
    DataSetId: str
    TargetAccountId: Optional[str] = None


# This class is the input for the 'associate_approved_origin' function.
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


# This class is the input for the 'associate_lambda_function' function.
class AssociateLambdaFunctionRequest(BaseValidatorModel):
    InstanceId: str
    FunctionArn: str
    ClientToken: Optional[str] = None


# This class is the input for the 'associate_phone_number_contact_flow' function.
class AssociatePhoneNumberContactFlowRequest(BaseValidatorModel):
    PhoneNumberId: str
    InstanceId: str
    ContactFlowId: str


# This class is the input for the 'associate_queue_quick_connects' function.
class AssociateQueueQuickConnectsRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    QuickConnectIds: List[str]


# This class is the input for the 'associate_security_key' function.
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


# This class is the input for the 'batch_associate_analytics_data_set' function.
class BatchAssociateAnalyticsDataSetRequest(BaseValidatorModel):
    InstanceId: str
    DataSetIds: List[str]
    TargetAccountId: Optional[str] = None


class ErrorResult(BaseValidatorModel):
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None


# This class is the input for the 'batch_disassociate_analytics_data_set' function.
class BatchDisassociateAnalyticsDataSetRequest(BaseValidatorModel):
    InstanceId: str
    DataSetIds: List[str]
    TargetAccountId: Optional[str] = None


# This class is the input for the 'batch_get_attached_file_metadata' function.
class BatchGetAttachedFileMetadataRequest(BaseValidatorModel):
    FileIds: List[str]
    InstanceId: str
    AssociatedResourceArn: str


# This class is the input for the 'batch_get_flow_association' function.
class BatchGetFlowAssociationRequest(BaseValidatorModel):
    InstanceId: str
    ResourceIds: List[str]
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


class ChatEvent(BaseValidatorModel):
    Type: ChatEventTypeType
    ContentType: Optional[str] = None
    Content: Optional[str] = None


class ChatMessage(BaseValidatorModel):
    ContentType: str
    Content: str


class ChatStreamingConfiguration(BaseValidatorModel):
    StreamingEndpointArn: str


# This class is the input for the 'claim_phone_number' function.
class ClaimPhoneNumberRequest(BaseValidatorModel):
    PhoneNumber: str
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberDescription: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    ClientToken: Optional[str] = None


class PhoneNumberStatus(BaseValidatorModel):
    Status: Optional[PhoneNumberWorkflowStatusType] = None
    Message: Optional[str] = None


class CompleteAttachedFileUploadRequest(BaseValidatorModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str


class NumberCondition(BaseValidatorModel):
    FieldName: Optional[str] = None
    MinValue: Optional[int] = None
    MaxValue: Optional[int] = None
    ComparisonType: Optional[NumberComparisonTypeType] = None


class ContactConfiguration(BaseValidatorModel):
    ContactId: str
    ParticipantRole: Optional[ParticipantRoleType] = None
    IncludeRawMessage: Optional[bool] = None


class Endpoint(BaseValidatorModel):
    Type: Optional[EndpointTypeType] = None
    Address: Optional[str] = None


class ContactFilter(BaseValidatorModel):
    ContactStates: Optional[List[ContactStateType]] = None


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


class ContactFlow(BaseValidatorModel):
    Arn: Optional[str] = None
    Id: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ContactFlowTypeType] = None
    State: Optional[ContactFlowStateType] = None
    Status: Optional[ContactFlowStatusType] = None
    Description: Optional[str] = None
    Content: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    FlowContentSha256: Optional[str] = None
    Version: Optional[int] = None
    VersionDescription: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


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


class EndpointInfo(BaseValidatorModel):
    Type: Optional[EndpointTypeType] = None
    Address: Optional[str] = None
    DisplayName: Optional[str] = None


class QueueInfo(BaseValidatorModel):
    Id: Optional[str] = None
    EnqueueTimestamp: Optional[datetime] = None


class SegmentAttributeValueOutput(BaseValidatorModel):
    ValueString: Optional[str] = None
    ValueMap: Optional[Dict[str, Dict[str, Any]]] = None
    ValueInteger: Optional[int] = None


class WisdomInfo(BaseValidatorModel):
    SessionArn: Optional[str] = None


# This class is the input for the 'create_agent_status' function.
class CreateAgentStatusRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    State: AgentStatusStateType
    Description: Optional[str] = None
    DisplayOrder: Optional[int] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_contact_flow_module' function.
class CreateContactFlowModuleRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    Content: str
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'create_contact_flow' function.
class CreateContactFlowRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    Type: ContactFlowTypeType
    Content: str
    Description: Optional[str] = None
    Status: Optional[ContactFlowStatusType] = None
    Tags: Optional[Dict[str, str]] = None

Timestamp = Union[datetime, str]


class Reference(BaseValidatorModel):
    Type: ReferenceTypeType
    Value: Optional[str] = None
    Status: Optional[ReferenceStatusType] = None
    Arn: Optional[str] = None
    StatusReason: Optional[str] = None


class UserInfo(BaseValidatorModel):
    UserId: Optional[str] = None


# This class is the input for the 'create_email_address' function.
class CreateEmailAddressRequest(BaseValidatorModel):
    InstanceId: str
    EmailAddress: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    ClientToken: Optional[str] = None


class EvaluationFormScoringStrategy(BaseValidatorModel):
    Mode: EvaluationFormScoringModeType
    Status: EvaluationFormScoringStatusType


# This class is the input for the 'create_instance' function.
class CreateInstanceRequest(BaseValidatorModel):
    IdentityManagementType: DirectoryTypeType
    InboundCallsEnabled: bool
    OutboundCallsEnabled: bool
    ClientToken: Optional[str] = None
    InstanceAlias: Optional[str] = None
    DirectoryId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_integration_association' function.
class CreateIntegrationAssociationRequest(BaseValidatorModel):
    InstanceId: str
    IntegrationType: IntegrationTypeType
    IntegrationArn: str
    SourceApplicationUrl: Optional[str] = None
    SourceApplicationName: Optional[str] = None
    SourceType: Optional[SourceTypeType] = None
    Tags: Optional[Dict[str, str]] = None


class ParticipantDetailsToAdd(BaseValidatorModel):
    ParticipantRole: Optional[ParticipantRoleType] = None
    DisplayName: Optional[str] = None


class ParticipantTokenCredentials(BaseValidatorModel):
    ParticipantToken: Optional[str] = None
    Expiry: Optional[str] = None


# This class is the input for the 'create_persistent_contact_association' function.
class CreatePersistentContactAssociationRequest(BaseValidatorModel):
    InstanceId: str
    InitialContactId: str
    RehydrationType: RehydrationTypeType
    SourceContactId: str
    ClientToken: Optional[str] = None


# This class is the input for the 'create_prompt' function.
class CreatePromptRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    S3Uri: str
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class OutboundCallerConfig(BaseValidatorModel):
    OutboundCallerIdName: Optional[str] = None
    OutboundCallerIdNumberId: Optional[str] = None
    OutboundFlowId: Optional[str] = None


class OutboundEmailConfig(BaseValidatorModel):
    OutboundEmailAddressId: Optional[str] = None


class RuleTriggerEventSource(BaseValidatorModel):
    EventSourceName: EventSourceNameType
    IntegrationAssociationId: Optional[str] = None


# This class is the input for the 'create_traffic_distribution_group' function.
class CreateTrafficDistributionGroupRequest(BaseValidatorModel):
    Name: str
    InstanceId: str
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_use_case' function.
class CreateUseCaseRequest(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    UseCaseType: UseCaseTypeType
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'create_user_hierarchy_group' function.
class CreateUserHierarchyGroupRequest(BaseValidatorModel):
    Name: str
    InstanceId: str
    ParentGroupId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


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
    Actions: Optional[List[str]] = None


# This class is the input for the 'create_view_version' function.
class CreateViewVersionRequest(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    VersionDescription: Optional[str] = None
    ViewContentSha256: Optional[str] = None


# This class is the input for the 'create_vocabulary' function.
class CreateVocabularyRequest(BaseValidatorModel):
    InstanceId: str
    VocabularyName: str
    LanguageCode: VocabularyLanguageCodeType
    Content: str
    ClientToken: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


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


class DateCondition(BaseValidatorModel):
    FieldName: Optional[str] = None
    Value: Optional[str] = None
    ComparisonType: Optional[DateComparisonTypeType] = None


class DateReference(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


# This class is the input for the 'deactivate_evaluation_form' function.
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


# This class is the input for the 'delete_contact_evaluation' function.
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


# This class is the input for the 'delete_evaluation_form' function.
class DeleteEvaluationFormRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: Optional[int] = None


# This class is the input for the 'delete_hours_of_operation_override' function.
class DeleteHoursOfOperationOverrideRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    HoursOfOperationOverrideId: str


# This class is the input for the 'delete_hours_of_operation' function.
class DeleteHoursOfOperationRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str


# This class is the input for the 'delete_instance' function.
class DeleteInstanceRequest(BaseValidatorModel):
    InstanceId: str
    ClientToken: Optional[str] = None


# This class is the input for the 'delete_integration_association' function.
class DeleteIntegrationAssociationRequest(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str


# This class is the input for the 'delete_predefined_attribute' function.
class DeletePredefinedAttributeRequest(BaseValidatorModel):
    InstanceId: str
    Name: str


# This class is the input for the 'delete_prompt' function.
class DeletePromptRequest(BaseValidatorModel):
    InstanceId: str
    PromptId: str


class DeletePushNotificationRegistrationRequest(BaseValidatorModel):
    InstanceId: str
    RegistrationId: str
    ContactId: str


# This class is the input for the 'delete_queue' function.
class DeleteQueueRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str


# This class is the input for the 'delete_quick_connect' function.
class DeleteQuickConnectRequest(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str


# This class is the input for the 'delete_routing_profile' function.
class DeleteRoutingProfileRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str


# This class is the input for the 'delete_rule' function.
class DeleteRuleRequest(BaseValidatorModel):
    InstanceId: str
    RuleId: str


# This class is the input for the 'delete_security_profile' function.
class DeleteSecurityProfileRequest(BaseValidatorModel):
    InstanceId: str
    SecurityProfileId: str


class DeleteTaskTemplateRequest(BaseValidatorModel):
    InstanceId: str
    TaskTemplateId: str


class DeleteTrafficDistributionGroupRequest(BaseValidatorModel):
    TrafficDistributionGroupId: str


# This class is the input for the 'delete_use_case' function.
class DeleteUseCaseRequest(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    UseCaseId: str


# This class is the input for the 'delete_user_hierarchy_group' function.
class DeleteUserHierarchyGroupRequest(BaseValidatorModel):
    HierarchyGroupId: str
    InstanceId: str


# This class is the input for the 'delete_user' function.
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


# This class is the input for the 'delete_vocabulary' function.
class DeleteVocabularyRequest(BaseValidatorModel):
    InstanceId: str
    VocabularyId: str


# This class is the input for the 'describe_agent_status' function.
class DescribeAgentStatusRequest(BaseValidatorModel):
    InstanceId: str
    AgentStatusId: str


# This class is the input for the 'describe_authentication_profile' function.
class DescribeAuthenticationProfileRequest(BaseValidatorModel):
    AuthenticationProfileId: str
    InstanceId: str


# This class is the input for the 'describe_contact_evaluation' function.
class DescribeContactEvaluationRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str


# This class is the input for the 'describe_contact_flow_module' function.
class DescribeContactFlowModuleRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowModuleId: str


# This class is the input for the 'describe_contact_flow' function.
class DescribeContactFlowRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str


# This class is the input for the 'describe_contact' function.
class DescribeContactRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str


# This class is the input for the 'describe_email_address' function.
class DescribeEmailAddressRequest(BaseValidatorModel):
    InstanceId: str
    EmailAddressId: str


# This class is the input for the 'describe_evaluation_form' function.
class DescribeEvaluationFormRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: Optional[int] = None


# This class is the input for the 'describe_hours_of_operation_override' function.
class DescribeHoursOfOperationOverrideRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    HoursOfOperationOverrideId: str


# This class is the input for the 'describe_hours_of_operation' function.
class DescribeHoursOfOperationRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str


# This class is the input for the 'describe_instance_attribute' function.
class DescribeInstanceAttributeRequest(BaseValidatorModel):
    InstanceId: str
    AttributeType: InstanceAttributeTypeType


# This class is the input for the 'describe_instance' function.
class DescribeInstanceRequest(BaseValidatorModel):
    InstanceId: str


# This class is the input for the 'describe_instance_storage_config' function.
class DescribeInstanceStorageConfigRequest(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType


# This class is the input for the 'describe_phone_number' function.
class DescribePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


# This class is the input for the 'describe_predefined_attribute' function.
class DescribePredefinedAttributeRequest(BaseValidatorModel):
    InstanceId: str
    Name: str


# This class is the input for the 'describe_prompt' function.
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


# This class is the input for the 'describe_queue' function.
class DescribeQueueRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str


# This class is the input for the 'describe_quick_connect' function.
class DescribeQuickConnectRequest(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str


# This class is the input for the 'describe_routing_profile' function.
class DescribeRoutingProfileRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str


# This class is the input for the 'describe_rule' function.
class DescribeRuleRequest(BaseValidatorModel):
    InstanceId: str
    RuleId: str


# This class is the input for the 'describe_security_profile' function.
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


# This class is the input for the 'describe_traffic_distribution_group' function.
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


# This class is the input for the 'describe_user_hierarchy_group' function.
class DescribeUserHierarchyGroupRequest(BaseValidatorModel):
    HierarchyGroupId: str
    InstanceId: str


# This class is the input for the 'describe_user_hierarchy_structure' function.
class DescribeUserHierarchyStructureRequest(BaseValidatorModel):
    InstanceId: str


# This class is the input for the 'describe_user' function.
class DescribeUserRequest(BaseValidatorModel):
    UserId: str
    InstanceId: str


# This class is the input for the 'describe_view' function.
class DescribeViewRequest(BaseValidatorModel):
    InstanceId: str
    ViewId: str


# This class is the input for the 'describe_vocabulary' function.
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


# This class is the input for the 'disassociate_analytics_data_set' function.
class DisassociateAnalyticsDataSetRequest(BaseValidatorModel):
    InstanceId: str
    DataSetId: str
    TargetAccountId: Optional[str] = None


# This class is the input for the 'disassociate_approved_origin' function.
class DisassociateApprovedOriginRequest(BaseValidatorModel):
    InstanceId: str
    Origin: str
    ClientToken: Optional[str] = None


class DisassociateFlowRequest(BaseValidatorModel):
    InstanceId: str
    ResourceId: str
    ResourceType: FlowAssociationResourceTypeType


# This class is the input for the 'disassociate_instance_storage_config' function.
class DisassociateInstanceStorageConfigRequest(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType
    ClientToken: Optional[str] = None


# This class is the input for the 'disassociate_lambda_function' function.
class DisassociateLambdaFunctionRequest(BaseValidatorModel):
    InstanceId: str
    FunctionArn: str
    ClientToken: Optional[str] = None


# This class is the input for the 'disassociate_lex_bot' function.
class DisassociateLexBotRequest(BaseValidatorModel):
    InstanceId: str
    BotName: str
    LexRegion: str
    ClientToken: Optional[str] = None


# This class is the input for the 'disassociate_phone_number_contact_flow' function.
class DisassociatePhoneNumberContactFlowRequest(BaseValidatorModel):
    PhoneNumberId: str
    InstanceId: str


# This class is the input for the 'disassociate_queue_quick_connects' function.
class DisassociateQueueQuickConnectsRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    QuickConnectIds: List[str]


class RoutingProfileQueueReference(BaseValidatorModel):
    QueueId: str
    Channel: ChannelType


# This class is the input for the 'disassociate_security_key' function.
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
    EncryptionType: Literal['KMS']
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
    Items: List[Dict[str, Any]]
    Instructions: Optional[str] = None
    Weight: Optional[float] = None


class SingleSelectQuestionRuleCategoryAutomation(BaseValidatorModel):
    Category: str
    Condition: SingleSelectQuestionRuleCategoryAutomationConditionType
    OptionRefId: str


class EvaluationFormSingleSelectQuestionOption(BaseValidatorModel):
    RefId: str
    Text: str
    Score: Optional[int] = None
    AutomaticFail: Optional[bool] = None


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
    EmptyValue: Optional[Dict[str, Any]] = None
    StringValue: Optional[str] = None


class FilterV2(BaseValidatorModel):
    FilterKey: Optional[str] = None
    FilterValues: Optional[List[str]] = None


class Filters(BaseValidatorModel):
    Queues: Optional[List[str]] = None
    Channels: Optional[List[ChannelType]] = None
    RoutingProfiles: Optional[List[str]] = None
    RoutingStepExpressions: Optional[List[str]] = None


# This class is the input for the 'get_attached_file' function.
class GetAttachedFileRequest(BaseValidatorModel):
    InstanceId: str
    FileId: str
    AssociatedResourceArn: str
    UrlExpiryInSeconds: Optional[int] = None


# This class is the input for the 'get_contact_attributes' function.
class GetContactAttributesRequest(BaseValidatorModel):
    InstanceId: str
    InitialContactId: str


# This class is the input for the 'get_effective_hours_of_operations' function.
class GetEffectiveHoursOfOperationsRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    FromDate: str
    ToDate: str


# This class is the input for the 'get_federation_token' function.
class GetFederationTokenRequest(BaseValidatorModel):
    InstanceId: str


# This class is the input for the 'get_flow_association' function.
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


# This class is the input for the 'get_prompt_file' function.
class GetPromptFileRequest(BaseValidatorModel):
    InstanceId: str
    PromptId: str


# This class is the input for the 'get_task_template' function.
class GetTaskTemplateRequest(BaseValidatorModel):
    InstanceId: str
    TaskTemplateId: str
    SnapshotVersion: Optional[str] = None


# This class is the input for the 'get_traffic_distribution' function.
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
    Comparison: Optional[Literal['LT']] = None
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


# This class is the input for the 'import_phone_number' function.
class ImportPhoneNumberRequest(BaseValidatorModel):
    InstanceId: str
    SourcePhoneNumberArn: str
    PhoneNumberDescription: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None
    ClientToken: Optional[str] = None


class InboundRawMessage(BaseValidatorModel):
    Subject: str
    Body: str
    ContentType: str
    Headers: Optional[Dict[EmailHeaderTypeType, str]] = None


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


# This class is the input for the 'list_agent_statuses' function.
class ListAgentStatusRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    AgentStatusTypes: Optional[List[AgentStatusTypeType]] = None


# This class is the input for the 'list_analytics_data_associations' function.
class ListAnalyticsDataAssociationsRequest(BaseValidatorModel):
    InstanceId: str
    DataSetId: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_analytics_data_lake_data_sets' function.
class ListAnalyticsDataLakeDataSetsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_approved_origins' function.
class ListApprovedOriginsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_associated_contacts' function.
class ListAssociatedContactsRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_authentication_profiles' function.
class ListAuthenticationProfilesRequest(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_bots' function.
class ListBotsRequest(BaseValidatorModel):
    InstanceId: str
    LexVersion: LexVersionType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_contact_evaluations' function.
class ListContactEvaluationsRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    NextToken: Optional[str] = None


# This class is the input for the 'list_contact_flow_modules' function.
class ListContactFlowModulesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    ContactFlowModuleState: Optional[ContactFlowModuleStateType] = None


# This class is the input for the 'list_contact_flow_versions' function.
class ListContactFlowVersionsRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_contact_flows' function.
class ListContactFlowsRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowTypes: Optional[List[ContactFlowTypeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_contact_references' function.
class ListContactReferencesRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ReferenceTypes: List[ReferenceTypeType]
    NextToken: Optional[str] = None


# This class is the input for the 'list_default_vocabularies' function.
class ListDefaultVocabulariesRequest(BaseValidatorModel):
    InstanceId: str
    LanguageCode: Optional[VocabularyLanguageCodeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_evaluation_form_versions' function.
class ListEvaluationFormVersionsRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_evaluation_forms' function.
class ListEvaluationFormsRequest(BaseValidatorModel):
    InstanceId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_flow_associations' function.
class ListFlowAssociationsRequest(BaseValidatorModel):
    InstanceId: str
    ResourceType: Optional[ListFlowAssociationResourceTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_hours_of_operation_overrides' function.
class ListHoursOfOperationOverridesRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_hours_of_operations' function.
class ListHoursOfOperationsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_instance_attributes' function.
class ListInstanceAttributesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_instance_storage_configs' function.
class ListInstanceStorageConfigsRequest(BaseValidatorModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_instances' function.
class ListInstancesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_integration_associations' function.
class ListIntegrationAssociationsRequest(BaseValidatorModel):
    InstanceId: str
    IntegrationType: Optional[IntegrationTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    IntegrationArn: Optional[str] = None


# This class is the input for the 'list_lambda_functions' function.
class ListLambdaFunctionsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_lex_bots' function.
class ListLexBotsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_phone_numbers' function.
class ListPhoneNumbersRequest(BaseValidatorModel):
    InstanceId: str
    PhoneNumberTypes: Optional[List[PhoneNumberTypeType]] = None
    PhoneNumberCountryCodes: Optional[List[PhoneNumberCountryCodeType]] = None
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


# This class is the input for the 'list_phone_numbers_v2' function.
class ListPhoneNumbersV2Request(BaseValidatorModel):
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    PhoneNumberCountryCodes: Optional[List[PhoneNumberCountryCodeType]] = None
    PhoneNumberTypes: Optional[List[PhoneNumberTypeType]] = None
    PhoneNumberPrefix: Optional[str] = None


# This class is the input for the 'list_predefined_attributes' function.
class ListPredefinedAttributesRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class PredefinedAttributeSummary(BaseValidatorModel):
    Name: Optional[str] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


# This class is the input for the 'list_prompts' function.
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


# This class is the input for the 'list_queue_quick_connects' function.
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


# This class is the input for the 'list_queues' function.
class ListQueuesRequest(BaseValidatorModel):
    InstanceId: str
    QueueTypes: Optional[List[QueueTypeType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class QueueSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    QueueType: Optional[QueueTypeType] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


# This class is the input for the 'list_quick_connects' function.
class ListQuickConnectsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    QuickConnectTypes: Optional[List[QuickConnectTypeType]] = None


# This class is the input for the 'list_realtime_contact_analysis_segments_v2' function.
class ListRealtimeContactAnalysisSegmentsV2Request(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    OutputType: RealTimeContactAnalysisOutputTypeType
    SegmentTypes: List[RealTimeContactAnalysisSegmentTypeType]
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_routing_profile_queues' function.
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


# This class is the input for the 'list_routing_profiles' function.
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


# This class is the input for the 'list_rules' function.
class ListRulesRequest(BaseValidatorModel):
    InstanceId: str
    PublishStatus: Optional[RulePublishStatusType] = None
    EventSourceName: Optional[EventSourceNameType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_security_keys' function.
class ListSecurityKeysRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class SecurityKey(BaseValidatorModel):
    AssociationId: Optional[str] = None
    Key: Optional[str] = None
    CreationTime: Optional[datetime] = None


# This class is the input for the 'list_security_profile_applications' function.
class ListSecurityProfileApplicationsRequest(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_security_profile_permissions' function.
class ListSecurityProfilePermissionsRequest(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_security_profiles' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'list_task_templates' function.
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


# This class is the input for the 'list_traffic_distribution_group_users' function.
class ListTrafficDistributionGroupUsersRequest(BaseValidatorModel):
    TrafficDistributionGroupId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TrafficDistributionGroupUserSummary(BaseValidatorModel):
    UserId: Optional[str] = None


# This class is the input for the 'list_traffic_distribution_groups' function.
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


# This class is the input for the 'list_use_cases' function.
class ListUseCasesRequest(BaseValidatorModel):
    InstanceId: str
    IntegrationAssociationId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class UseCase(BaseValidatorModel):
    UseCaseId: Optional[str] = None
    UseCaseArn: Optional[str] = None
    UseCaseType: Optional[UseCaseTypeType] = None


# This class is the input for the 'list_user_hierarchy_groups' function.
class ListUserHierarchyGroupsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_user_proficiencies' function.
class ListUserProficienciesRequest(BaseValidatorModel):
    InstanceId: str
    UserId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_users' function.
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


# This class is the input for the 'list_view_versions' function.
class ListViewVersionsRequest(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ViewVersionSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Description: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ViewTypeType] = None
    Version: Optional[int] = None
    VersionDescription: Optional[str] = None


# This class is the input for the 'list_views' function.
class ListViewsRequest(BaseValidatorModel):
    InstanceId: str
    Type: Optional[ViewTypeType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ViewSummary(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Type: Optional[ViewTypeType] = None
    Status: Optional[ViewStatusType] = None
    Description: Optional[str] = None


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
    MetricFilterValues: Optional[List[str]] = None
    Negate: Optional[bool] = None


class MetricInterval(BaseValidatorModel):
    Interval: Optional[IntervalPeriodType] = None
    StartTime: Optional[datetime] = None
    EndTime: Optional[datetime] = None


class ThresholdV2(BaseValidatorModel):
    Comparison: Optional[str] = None
    ThresholdValue: Optional[float] = None


# This class is the input for the 'monitor_contact' function.
class MonitorContactRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    UserId: str
    AllowedMonitorCapabilities: Optional[List[MonitorCapabilityType]] = None
    ClientToken: Optional[str] = None


class ParticipantDetails(BaseValidatorModel):
    DisplayName: str


class NotificationRecipientTypeOutput(BaseValidatorModel):
    UserTags: Optional[Dict[str, str]] = None
    UserIds: Optional[List[str]] = None


class NotificationRecipientType(BaseValidatorModel):
    UserTags: Optional[Dict[str, str]] = None
    UserIds: Optional[List[str]] = None


class NumberReference(BaseValidatorModel):
    Name: Optional[str] = None
    Value: Optional[str] = None


class OutboundRawMessage(BaseValidatorModel):
    Subject: str
    Body: str
    ContentType: str


class ParticipantTimerValue(BaseValidatorModel):
    ParticipantTimerAction: Optional[Literal['Unset']] = None
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
    StringList: Optional[List[str]] = None


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


# This class is the input for the 'release_phone_number' function.
class ReleasePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str
    ClientToken: Optional[str] = None


# This class is the input for the 'replicate_instance' function.
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


# This class is the input for the 'search_available_phone_numbers' function.
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


# This class is the input for the 'search_vocabularies' function.
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
    Values: List[str]


class SearchableSegmentAttributesCriteria(BaseValidatorModel):
    Key: str
    Values: List[str]


class SegmentAttributeValue(BaseValidatorModel):
    ValueString: Optional[str] = None
    ValueMap: Optional[Dict[str, Dict[str, Any]]] = None
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


# This class is the input for the 'start_contact_evaluation' function.
class StartContactEvaluationRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    EvaluationFormId: str
    ClientToken: Optional[str] = None


class VoiceRecordingConfiguration(BaseValidatorModel):
    VoiceRecordingTrack: Optional[VoiceRecordingTrackType] = None
    IvrRecordingTrack: Optional[Literal['ALL']] = None


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
    Tags: Dict[str, str]


# This class is the input for the 'tag_resource' function.
class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class TemplateAttributes(BaseValidatorModel):
    CustomAttributes: Optional[Dict[str, str]] = None
    CustomerProfileAttributes: Optional[str] = None


class TranscriptCriteria(BaseValidatorModel):
    ParticipantRole: ParticipantRoleType
    SearchText: List[str]
    MatchType: SearchContactsMatchTypeType


# This class is the input for the 'transfer_contact' function.
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
    TagKeys: List[str]


# This class is the input for the 'untag_resource' function.
class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_agent_status' function.
class UpdateAgentStatusRequest(BaseValidatorModel):
    InstanceId: str
    AgentStatusId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    State: Optional[AgentStatusStateType] = None
    DisplayOrder: Optional[int] = None
    ResetOrderNumber: Optional[bool] = None


# This class is the input for the 'update_authentication_profile' function.
class UpdateAuthenticationProfileRequest(BaseValidatorModel):
    AuthenticationProfileId: str
    InstanceId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    AllowedIps: Optional[List[str]] = None
    BlockedIps: Optional[List[str]] = None
    PeriodicSessionDuration: Optional[int] = None


class UpdateContactAttributesRequest(BaseValidatorModel):
    InitialContactId: str
    InstanceId: str
    Attributes: Dict[str, str]


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


# This class is the input for the 'update_email_address_metadata' function.
class UpdateEmailAddressMetadataRequest(BaseValidatorModel):
    InstanceId: str
    EmailAddressId: str
    Description: Optional[str] = None
    DisplayName: Optional[str] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'update_instance_attribute' function.
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


# This class is the input for the 'update_phone_number_metadata' function.
class UpdatePhoneNumberMetadataRequest(BaseValidatorModel):
    PhoneNumberId: str
    PhoneNumberDescription: Optional[str] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'update_phone_number' function.
class UpdatePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'update_prompt' function.
class UpdatePromptRequest(BaseValidatorModel):
    InstanceId: str
    PromptId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    S3Uri: Optional[str] = None


# This class is the input for the 'update_queue_hours_of_operation' function.
class UpdateQueueHoursOfOperationRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    HoursOfOperationId: str


# This class is the input for the 'update_queue_max_contacts' function.
class UpdateQueueMaxContactsRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    MaxContacts: Optional[int] = None


# This class is the input for the 'update_queue_name' function.
class UpdateQueueNameRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'update_queue_status' function.
class UpdateQueueStatusRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    Status: QueueStatusType


# This class is the input for the 'update_quick_connect_name' function.
class UpdateQuickConnectNameRequest(BaseValidatorModel):
    InstanceId: str
    QuickConnectId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'update_routing_profile_agent_availability_timer' function.
class UpdateRoutingProfileAgentAvailabilityTimerRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    AgentAvailabilityTimer: AgentAvailabilityTimerType


# This class is the input for the 'update_routing_profile_default_outbound_queue' function.
class UpdateRoutingProfileDefaultOutboundQueueRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    DefaultOutboundQueueId: str


# This class is the input for the 'update_routing_profile_name' function.
class UpdateRoutingProfileNameRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    Name: Optional[str] = None
    Description: Optional[str] = None


# This class is the input for the 'update_user_hierarchy_group_name' function.
class UpdateUserHierarchyGroupNameRequest(BaseValidatorModel):
    Name: str
    HierarchyGroupId: str
    InstanceId: str


# This class is the input for the 'update_user_hierarchy' function.
class UpdateUserHierarchyRequest(BaseValidatorModel):
    UserId: str
    InstanceId: str
    HierarchyGroupId: Optional[str] = None


# This class is the input for the 'update_user_routing_profile' function.
class UpdateUserRoutingProfileRequest(BaseValidatorModel):
    RoutingProfileId: str
    UserId: str
    InstanceId: str


# This class is the input for the 'update_user_security_profiles' function.
class UpdateUserSecurityProfilesRequest(BaseValidatorModel):
    SecurityProfileIds: List[str]
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


# This class is the output for the 'activate_evaluation_form' function.
class ActivateEvaluationFormResponse(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_analytics_data_set' function.
class AssociateAnalyticsDataSetResponse(BaseValidatorModel):
    DataSetId: str
    TargetAccountId: str
    ResourceShareId: str
    ResourceShareArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_instance_storage_config' function.
class AssociateInstanceStorageConfigResponse(BaseValidatorModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'associate_security_key' function.
class AssociateSecurityKeyResponse(BaseValidatorModel):
    AssociationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'claim_phone_number' function.
class ClaimPhoneNumberResponse(BaseValidatorModel):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_agent_status' function.
class CreateAgentStatusResponse(BaseValidatorModel):
    AgentStatusARN: str
    AgentStatusId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_contact_flow_module' function.
class CreateContactFlowModuleResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_contact_flow' function.
class CreateContactFlowResponse(BaseValidatorModel):
    ContactFlowId: str
    ContactFlowArn: str
    FlowContentSha256: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_contact_flow_version' function.
class CreateContactFlowVersionResponse(BaseValidatorModel):
    ContactFlowArn: str
    Version: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_contact' function.
class CreateContactResponse(BaseValidatorModel):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_email_address' function.
class CreateEmailAddressResponse(BaseValidatorModel):
    EmailAddressId: str
    EmailAddressArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_evaluation_form' function.
class CreateEvaluationFormResponse(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_hours_of_operation_override' function.
class CreateHoursOfOperationOverrideResponse(BaseValidatorModel):
    HoursOfOperationOverrideId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_hours_of_operation' function.
class CreateHoursOfOperationResponse(BaseValidatorModel):
    HoursOfOperationId: str
    HoursOfOperationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_instance' function.
class CreateInstanceResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_integration_association' function.
class CreateIntegrationAssociationResponse(BaseValidatorModel):
    IntegrationAssociationId: str
    IntegrationAssociationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_persistent_contact_association' function.
class CreatePersistentContactAssociationResponse(BaseValidatorModel):
    ContinuedFromContactId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_prompt' function.
class CreatePromptResponse(BaseValidatorModel):
    PromptARN: str
    PromptId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_push_notification_registration' function.
class CreatePushNotificationRegistrationResponse(BaseValidatorModel):
    RegistrationId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_queue' function.
class CreateQueueResponse(BaseValidatorModel):
    QueueArn: str
    QueueId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_quick_connect' function.
class CreateQuickConnectResponse(BaseValidatorModel):
    QuickConnectARN: str
    QuickConnectId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_routing_profile' function.
class CreateRoutingProfileResponse(BaseValidatorModel):
    RoutingProfileArn: str
    RoutingProfileId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_rule' function.
class CreateRuleResponse(BaseValidatorModel):
    RuleArn: str
    RuleId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_security_profile' function.
class CreateSecurityProfileResponse(BaseValidatorModel):
    SecurityProfileId: str
    SecurityProfileArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_task_template' function.
class CreateTaskTemplateResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_traffic_distribution_group' function.
class CreateTrafficDistributionGroupResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_use_case' function.
class CreateUseCaseResponse(BaseValidatorModel):
    UseCaseId: str
    UseCaseArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_user_hierarchy_group' function.
class CreateUserHierarchyGroupResponse(BaseValidatorModel):
    HierarchyGroupId: str
    HierarchyGroupArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_user' function.
class CreateUserResponse(BaseValidatorModel):
    UserId: str
    UserArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_vocabulary' function.
class CreateVocabularyResponse(BaseValidatorModel):
    VocabularyArn: str
    VocabularyId: str
    State: VocabularyStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'deactivate_evaluation_form' function.
class DeactivateEvaluationFormResponse(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'delete_vocabulary' function.
class DeleteVocabularyResponse(BaseValidatorModel):
    VocabularyArn: str
    VocabularyId: str
    State: VocabularyStateType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_email_address' function.
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


# This class is the output for the 'update_user_security_profiles' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_contact_attributes' function.
class GetContactAttributesResponse(BaseValidatorModel):
    Attributes: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_flow_association' function.
class GetFlowAssociationResponse(BaseValidatorModel):
    ResourceId: str
    FlowId: str
    ResourceType: FlowAssociationResourceTypeType
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_prompt_file' function.
class GetPromptFileResponse(BaseValidatorModel):
    PromptPresignedUrl: str
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_phone_number' function.
class ImportPhoneNumberResponse(BaseValidatorModel):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_approved_origins' function.
class ListApprovedOriginsResponse(BaseValidatorModel):
    Origins: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_lambda_functions' function.
class ListLambdaFunctionsResponse(BaseValidatorModel):
    LambdaFunctions: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_security_profile_permissions' function.
class ListSecurityProfilePermissionsResponse(BaseValidatorModel):
    Permissions: List[str]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'monitor_contact' function.
class MonitorContactResponse(BaseValidatorModel):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'replicate_instance' function.
class ReplicateInstanceResponse(BaseValidatorModel):
    Id: str
    Arn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'send_chat_integration_event' function.
class SendChatIntegrationEventResponse(BaseValidatorModel):
    InitialContactId: str
    NewChatCreated: bool
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_chat_contact' function.
class StartChatContactResponse(BaseValidatorModel):
    ContactId: str
    ParticipantId: str
    ParticipantToken: str
    ContinuedFromContactId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_contact_evaluation' function.
class StartContactEvaluationResponse(BaseValidatorModel):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_contact_streaming' function.
class StartContactStreamingResponse(BaseValidatorModel):
    StreamingId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_email_contact' function.
class StartEmailContactResponse(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_outbound_chat_contact' function.
class StartOutboundChatContactResponse(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_outbound_email_contact' function.
class StartOutboundEmailContactResponse(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_outbound_voice_contact' function.
class StartOutboundVoiceContactResponse(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_task_contact' function.
class StartTaskContactResponse(BaseValidatorModel):
    ContactId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'submit_contact_evaluation' function.
class SubmitContactEvaluationResponse(BaseValidatorModel):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'transfer_contact' function.
class TransferContactResponse(BaseValidatorModel):
    ContactId: str
    ContactArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_contact_evaluation' function.
class UpdateContactEvaluationResponse(BaseValidatorModel):
    EvaluationId: str
    EvaluationArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_email_address_metadata' function.
class UpdateEmailAddressMetadataResponse(BaseValidatorModel):
    EmailAddressId: str
    EmailAddressArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_evaluation_form' function.
class UpdateEvaluationFormResponse(BaseValidatorModel):
    EvaluationFormId: str
    EvaluationFormArn: str
    EvaluationFormVersion: int
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_phone_number' function.
class UpdatePhoneNumberResponse(BaseValidatorModel):
    PhoneNumberId: str
    PhoneNumberArn: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_prompt' function.
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
    Distributions: List[Distribution]


class TelephonyConfigOutput(BaseValidatorModel):
    Distributions: List[Distribution]


class TelephonyConfig(BaseValidatorModel):
    Distributions: List[Distribution]


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


class AgentStatusSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class AgentStatusSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class ContactFlowModuleSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    StateCondition: Optional[ContactFlowModuleStateType] = None
    StatusCondition: Optional[ContactFlowModuleStatusType] = None


class ContactFlowModuleSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    StateCondition: Optional[ContactFlowModuleStateType] = None
    StatusCondition: Optional[ContactFlowModuleStatusType] = None


class ContactFlowSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    TypeCondition: Optional[ContactFlowTypeType] = None
    StateCondition: Optional[ContactFlowStateType] = None
    StatusCondition: Optional[ContactFlowStatusType] = None


class ContactFlowSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    TypeCondition: Optional[ContactFlowTypeType] = None
    StateCondition: Optional[ContactFlowStateType] = None
    StatusCondition: Optional[ContactFlowStatusType] = None


class EmailAddressSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class HoursOfOperationSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class HoursOfOperationSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class PredefinedAttributeSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class PredefinedAttributeSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class PromptSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class PromptSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class QueueSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    QueueTypeCondition: Optional[Literal['STANDARD']] = None


class QueueSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    QueueTypeCondition: Optional[Literal['STANDARD']] = None


class QuickConnectSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class QuickConnectSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class RoutingProfileSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class RoutingProfileSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class SecurityProfileSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class SecurityProfileSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class UserHierarchyGroupSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


class UserHierarchyGroupSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None


# This class is the output for the 'list_agent_statuses' function.
class ListAgentStatusResponse(BaseValidatorModel):
    AgentStatusSummaryList: List[AgentStatusSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_agent_status' function.
class DescribeAgentStatusResponse(BaseValidatorModel):
    AgentStatus: AgentStatus
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_agent_statuses' function.
class SearchAgentStatusesResponse(BaseValidatorModel):
    AgentStatuses: List[AgentStatus]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MatchCriteriaOutput(BaseValidatorModel):
    AgentsCriteria: Optional[AgentsCriteriaOutput] = None

AgentsCriteriaUnion = Union[AgentsCriteria, AgentsCriteriaOutput]


# This class is the output for the 'list_analytics_data_associations' function.
class ListAnalyticsDataAssociationsResponse(BaseValidatorModel):
    Results: List[AnalyticsDataAssociationResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_analytics_data_lake_data_sets' function.
class ListAnalyticsDataLakeDataSetsResponse(BaseValidatorModel):
    Results: List[AnalyticsDataSetsResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_security_profile_applications' function.
class ListSecurityProfileApplicationsResponse(BaseValidatorModel):
    Applications: List[ApplicationOutput]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

ApplicationUnion = Union[Application, ApplicationOutput]


# This class is the input for the 'associate_lex_bot' function.
class AssociateLexBotRequest(BaseValidatorModel):
    InstanceId: str
    LexBot: LexBot
    ClientToken: Optional[str] = None


# This class is the output for the 'list_lex_bots' function.
class ListLexBotsResponse(BaseValidatorModel):
    LexBots: List[LexBot]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'associate_bot' function.
class AssociateBotRequest(BaseValidatorModel):
    InstanceId: str
    LexBot: Optional[LexBot] = None
    LexV2Bot: Optional[LexV2Bot] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'disassociate_bot' function.
class DisassociateBotRequest(BaseValidatorModel):
    InstanceId: str
    LexBot: Optional[LexBot] = None
    LexV2Bot: Optional[LexV2Bot] = None
    ClientToken: Optional[str] = None


class LexBotConfig(BaseValidatorModel):
    LexBot: Optional[LexBot] = None
    LexV2Bot: Optional[LexV2Bot] = None


# This class is the input for the 'associate_user_proficiencies' function.
class AssociateUserProficienciesRequest(BaseValidatorModel):
    InstanceId: str
    UserId: str
    UserProficiencies: List[UserProficiency]


# This class is the output for the 'list_user_proficiencies' function.
class ListUserProficienciesResponse(BaseValidatorModel):
    UserProficiencyList: List[UserProficiency]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'update_user_proficiencies' function.
class UpdateUserProficienciesRequest(BaseValidatorModel):
    InstanceId: str
    UserId: str
    UserProficiencies: List[UserProficiency]


# This class is the output for the 'list_associated_contacts' function.
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


# This class is the input for the 'start_attached_file_upload' function.
class StartAttachedFileUploadRequest(BaseValidatorModel):
    InstanceId: str
    FileName: str
    FileSizeInBytes: int
    FileUseCaseType: FileUseCaseTypeType
    AssociatedResourceArn: str
    ClientToken: Optional[str] = None
    UrlExpiryInSeconds: Optional[int] = None
    CreatedBy: Optional[CreatedByInfo] = None
    Tags: Optional[Dict[str, str]] = None


class AttributeAndCondition(BaseValidatorModel):
    TagConditions: Optional[List[TagCondition]] = None
    HierarchyGroupCondition: Optional[HierarchyGroupCondition] = None


class CommonAttributeAndCondition(BaseValidatorModel):
    TagConditions: Optional[List[TagCondition]] = None


class ControlPlaneTagFilter(BaseValidatorModel):
    OrConditions: Optional[List[List[TagCondition]]] = None
    AndConditions: Optional[List[TagCondition]] = None
    TagCondition: Optional[TagCondition] = None


# This class is the output for the 'describe_instance_attribute' function.
class DescribeInstanceAttributeResponse(BaseValidatorModel):
    Attribute: Attribute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_instance_attributes' function.
class ListInstanceAttributesResponse(BaseValidatorModel):
    Attributes: List[Attribute]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class MeetingFeaturesConfiguration(BaseValidatorModel):
    Audio: Optional[AudioFeatures] = None


# This class is the output for the 'list_authentication_profiles' function.
class ListAuthenticationProfilesResponse(BaseValidatorModel):
    AuthenticationProfileSummaryList: List[AuthenticationProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_authentication_profile' function.
class DescribeAuthenticationProfileResponse(BaseValidatorModel):
    AuthenticationProfile: AuthenticationProfile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_available_phone_numbers' function.
class SearchAvailablePhoneNumbersResponse(BaseValidatorModel):
    AvailableNumbersList: List[AvailableNumberSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'batch_associate_analytics_data_set' function.
class BatchAssociateAnalyticsDataSetResponse(BaseValidatorModel):
    Created: List[AnalyticsDataAssociationResult]
    Errors: List[ErrorResult]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_disassociate_analytics_data_set' function.
class BatchDisassociateAnalyticsDataSetResponse(BaseValidatorModel):
    Deleted: List[str]
    Errors: List[ErrorResult]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_get_flow_association' function.
class BatchGetFlowAssociationResponse(BaseValidatorModel):
    FlowAssociationSummaryList: List[FlowAssociationSummary]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_flow_associations' function.
class ListFlowAssociationsResponse(BaseValidatorModel):
    FlowAssociationSummaryList: List[FlowAssociationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'batch_put_contact' function.
class BatchPutContactResponse(BaseValidatorModel):
    SuccessfulRequestList: List[SuccessfulRequest]
    FailedRequestList: List[FailedRequest]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_contact_streaming' function.
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


class Condition(BaseValidatorModel):
    StringCondition: Optional[StringCondition] = None
    NumberCondition: Optional[NumberCondition] = None


# This class is the input for the 'create_push_notification_registration' function.
class CreatePushNotificationRegistrationRequest(BaseValidatorModel):
    InstanceId: str
    PinpointAppArn: str
    DeviceToken: str
    DeviceType: DeviceTypeType
    ContactConfiguration: ContactConfiguration
    ClientToken: Optional[str] = None


class ContactDataRequest(BaseValidatorModel):
    SystemEndpoint: Optional[Endpoint] = None
    CustomerEndpoint: Optional[Endpoint] = None
    RequestIdentifier: Optional[str] = None
    QueueId: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    Campaign: Optional[Campaign] = None


class UserDataFilters(BaseValidatorModel):
    Queues: Optional[List[str]] = None
    ContactFilter: Optional[ContactFilter] = None
    RoutingProfiles: Optional[List[str]] = None
    Agents: Optional[List[str]] = None
    UserHierarchyGroups: Optional[List[str]] = None


# This class is the output for the 'list_contact_flow_modules' function.
class ListContactFlowModulesResponse(BaseValidatorModel):
    ContactFlowModulesSummaryList: List[ContactFlowModuleSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_contact_flow_module' function.
class DescribeContactFlowModuleResponse(BaseValidatorModel):
    ContactFlowModule: ContactFlowModule
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_contact_flow_modules' function.
class SearchContactFlowModulesResponse(BaseValidatorModel):
    ContactFlowModules: List[ContactFlowModule]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_contact_flows' function.
class ListContactFlowsResponse(BaseValidatorModel):
    ContactFlowSummaryList: List[ContactFlowSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_contact_flow' function.
class DescribeContactFlowResponse(BaseValidatorModel):
    ContactFlow: ContactFlow
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_contact_flows' function.
class SearchContactFlowsResponse(BaseValidatorModel):
    ContactFlows: List[ContactFlow]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_contact_flow_versions' function.
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


# This class is the input for the 'create_contact_flow_version' function.
class CreateContactFlowVersionRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    Description: Optional[str] = None
    FlowContentSha256: Optional[str] = None
    ContactFlowVersion: Optional[int] = None
    LastModifiedTime: Optional[Timestamp] = None
    LastModifiedRegion: Optional[str] = None


class SearchContactsTimeRange(BaseValidatorModel):
    Type: SearchContactsTimeRangeTypeType
    StartTime: Timestamp
    EndTime: Timestamp


class UpdateContactScheduleRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ScheduledTime: Timestamp


# This class is the input for the 'start_outbound_voice_contact' function.
class StartOutboundVoiceContactRequest(BaseValidatorModel):
    DestinationPhoneNumber: str
    ContactFlowId: str
    InstanceId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    References: Optional[Dict[str, Reference]] = None
    RelatedContactId: Optional[str] = None
    ClientToken: Optional[str] = None
    SourcePhoneNumber: Optional[str] = None
    QueueId: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
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
    References: Optional[Dict[str, Reference]] = None


# This class is the input for the 'create_participant' function.
class CreateParticipantRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ParticipantDetails: ParticipantDetailsToAdd
    ClientToken: Optional[str] = None


# This class is the output for the 'create_participant' function.
class CreateParticipantResponse(BaseValidatorModel):
    ParticipantCredentials: ParticipantTokenCredentials
    ParticipantId: str
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_queue_outbound_caller_config' function.
class UpdateQueueOutboundCallerConfigRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    OutboundCallerConfig: OutboundCallerConfig


# This class is the input for the 'create_queue' function.
class CreateQueueRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    HoursOfOperationId: str
    Description: Optional[str] = None
    OutboundCallerConfig: Optional[OutboundCallerConfig] = None
    OutboundEmailConfig: Optional[OutboundEmailConfig] = None
    MaxContacts: Optional[int] = None
    QuickConnectIds: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None


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


# This class is the input for the 'update_queue_outbound_email_config' function.
class UpdateQueueOutboundEmailConfigRequest(BaseValidatorModel):
    InstanceId: str
    QueueId: str
    OutboundEmailConfig: OutboundEmailConfig


# This class is the input for the 'update_user_identity_info' function.
class UpdateUserIdentityInfoRequest(BaseValidatorModel):
    IdentityInfo: UserIdentityInfo
    UserId: str
    InstanceId: str


# This class is the input for the 'create_user' function.
class CreateUserRequest(BaseValidatorModel):
    Username: str
    PhoneConfig: UserPhoneConfig
    SecurityProfileIds: List[str]
    RoutingProfileId: str
    InstanceId: str
    Password: Optional[str] = None
    IdentityInfo: Optional[UserIdentityInfo] = None
    DirectoryUserId: Optional[str] = None
    HierarchyGroupId: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_user_phone_config' function.
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


# This class is the input for the 'create_view' function.
class CreateViewRequest(BaseValidatorModel):
    InstanceId: str
    Status: ViewStatusType
    Content: ViewInputContent
    Name: str
    ClientToken: Optional[str] = None
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


# This class is the input for the 'update_view_content' function.
class UpdateViewContentRequest(BaseValidatorModel):
    InstanceId: str
    ViewId: str
    Status: ViewStatusType
    Content: ViewInputContent


# This class is the output for the 'get_federation_token' function.
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


class HoursOfOperationOverrideSearchCriteriaPaginator(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    DateCondition: Optional[DateCondition] = None


class HoursOfOperationOverrideSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    DateCondition: Optional[DateCondition] = None


# This class is the output for the 'list_default_vocabularies' function.
class ListDefaultVocabulariesResponse(BaseValidatorModel):
    DefaultVocabularyList: List[DefaultVocabulary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_prompt' function.
class DescribePromptResponse(BaseValidatorModel):
    Prompt: Prompt
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_prompts' function.
class SearchPromptsResponse(BaseValidatorModel):
    Prompts: List[Prompt]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_security_profile' function.
class DescribeSecurityProfileResponse(BaseValidatorModel):
    SecurityProfile: SecurityProfile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_traffic_distribution_group' function.
class DescribeTrafficDistributionGroupResponse(BaseValidatorModel):
    TrafficDistributionGroup: TrafficDistributionGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_vocabulary' function.
class DescribeVocabularyResponse(BaseValidatorModel):
    Vocabulary: Vocabulary
    ResponseMetadata: ResponseMetadata


class Dimensions(BaseValidatorModel):
    Queue: Optional[QueueReference] = None
    Channel: Optional[ChannelType] = None
    RoutingProfile: Optional[RoutingProfileReference] = None
    RoutingStepExpression: Optional[str] = None


# This class is the input for the 'disassociate_routing_profile_queues' function.
class DisassociateRoutingProfileQueuesRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    QueueReferences: List[RoutingProfileQueueReference]


class RoutingProfileQueueConfig(BaseValidatorModel):
    QueueReference: RoutingProfileQueueReference
    Priority: int
    Delay: int


# This class is the input for the 'disassociate_user_proficiencies' function.
class DisassociateUserProficienciesRequest(BaseValidatorModel):
    InstanceId: str
    UserId: str
    UserProficiencies: List[UserProficiencyDisassociate]


class StopContactRequest(BaseValidatorModel):
    ContactId: str
    InstanceId: str
    DisconnectReason: Optional[DisconnectReason] = None


# This class is the output for the 'get_attached_file' function.
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
    ToAddresses: Optional[List[EmailAddressInfo]] = None
    CcAddresses: Optional[List[EmailAddressInfo]] = None


class OutboundAdditionalRecipients(BaseValidatorModel):
    CcEmailAddresses: Optional[List[EmailAddressInfo]] = None


# This class is the output for the 'search_email_addresses' function.
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

EvaluationFormSectionUnion = Union[EvaluationFormSection, EvaluationFormSectionOutput]


class EvaluationFormSingleSelectQuestionAutomationOption(BaseValidatorModel):
    RuleCategory: Optional[SingleSelectQuestionRuleCategoryAutomation] = None


# This class is the output for the 'list_evaluation_forms' function.
class ListEvaluationFormsResponse(BaseValidatorModel):
    EvaluationFormSummaryList: List[EvaluationFormSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_evaluation_form_versions' function.
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

FieldValueUnionUnion = Union[FieldValueUnion, FieldValueUnionOutput]


# This class is the input for the 'get_current_metric_data' function.
class GetCurrentMetricDataRequest(BaseValidatorModel):
    InstanceId: str
    Filters: Filters
    CurrentMetrics: List[CurrentMetric]
    Groupings: Optional[List[GroupingType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SortCriteria: Optional[List[CurrentMetricSortCriteria]] = None


class ListAgentStatusRequestPaginate(BaseValidatorModel):
    InstanceId: str
    AgentStatusTypes: Optional[List[AgentStatusTypeType]] = None
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
    ContactFlowTypes: Optional[List[ContactFlowTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListContactReferencesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    ReferenceTypes: List[ReferenceTypeType]
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
    PhoneNumberTypes: Optional[List[PhoneNumberTypeType]] = None
    PhoneNumberCountryCodes: Optional[List[PhoneNumberCountryCodeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPhoneNumbersV2RequestPaginate(BaseValidatorModel):
    TargetArn: Optional[str] = None
    InstanceId: Optional[str] = None
    PhoneNumberCountryCodes: Optional[List[PhoneNumberCountryCodeType]] = None
    PhoneNumberTypes: Optional[List[PhoneNumberTypeType]] = None
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
    QueueTypes: Optional[List[QueueTypeType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListQuickConnectsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    QuickConnectTypes: Optional[List[QuickConnectTypeType]] = None
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


class ListViewsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    Type: Optional[ViewTypeType] = None
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


# This class is the output for the 'list_user_hierarchy_groups' function.
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


# This class is the output for the 'list_hours_of_operations' function.
class ListHoursOfOperationsResponse(BaseValidatorModel):
    HoursOfOperationSummaryList: List[HoursOfOperationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class InboundEmailContent(BaseValidatorModel):
    MessageSourceType: Literal['RAW']
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


# This class is the output for the 'list_instances' function.
class ListInstancesResponse(BaseValidatorModel):
    InstanceSummaryList: List[InstanceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_integration_associations' function.
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


class TaskTemplateFieldOutput(BaseValidatorModel):
    Id: TaskTemplateFieldIdentifier
    Description: Optional[str] = None
    Type: Optional[TaskTemplateFieldTypeType] = None
    SingleSelectOptions: Optional[List[str]] = None


class TaskTemplateField(BaseValidatorModel):
    Id: TaskTemplateFieldIdentifier
    Description: Optional[str] = None
    Type: Optional[TaskTemplateFieldTypeType] = None
    SingleSelectOptions: Optional[List[str]] = None


# This class is the output for the 'list_phone_numbers' function.
class ListPhoneNumbersResponse(BaseValidatorModel):
    PhoneNumberSummaryList: List[PhoneNumberSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_phone_numbers_v2' function.
class ListPhoneNumbersV2Response(BaseValidatorModel):
    ListPhoneNumbersSummaryList: List[ListPhoneNumbersSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_predefined_attributes' function.
class ListPredefinedAttributesResponse(BaseValidatorModel):
    PredefinedAttributeSummaryList: List[PredefinedAttributeSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_prompts' function.
class ListPromptsResponse(BaseValidatorModel):
    PromptSummaryList: List[PromptSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_queue_quick_connects' function.
class ListQueueQuickConnectsResponse(BaseValidatorModel):
    QuickConnectSummaryList: List[QuickConnectSummary]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_quick_connects' function.
class ListQuickConnectsResponse(BaseValidatorModel):
    QuickConnectSummaryList: List[QuickConnectSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_queues' function.
class ListQueuesResponse(BaseValidatorModel):
    QueueSummaryList: List[QueueSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_routing_profile_queues' function.
class ListRoutingProfileQueuesResponse(BaseValidatorModel):
    RoutingProfileQueueConfigSummaryList: List[RoutingProfileQueueConfigSummary]
    LastModifiedTime: datetime
    LastModifiedRegion: str
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_routing_profiles' function.
class ListRoutingProfilesResponse(BaseValidatorModel):
    RoutingProfileSummaryList: List[RoutingProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_security_keys' function.
class ListSecurityKeysResponse(BaseValidatorModel):
    SecurityKeys: List[SecurityKey]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_security_profiles' function.
class ListSecurityProfilesResponse(BaseValidatorModel):
    SecurityProfileSummaryList: List[SecurityProfileSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_task_templates' function.
class ListTaskTemplatesResponse(BaseValidatorModel):
    TaskTemplates: List[TaskTemplateMetadata]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_traffic_distribution_group_users' function.
class ListTrafficDistributionGroupUsersResponse(BaseValidatorModel):
    TrafficDistributionGroupUserSummaryList: List[TrafficDistributionGroupUserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_traffic_distribution_groups' function.
class ListTrafficDistributionGroupsResponse(BaseValidatorModel):
    TrafficDistributionGroupSummaryList: List[TrafficDistributionGroupSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_use_cases' function.
class ListUseCasesResponse(BaseValidatorModel):
    UseCaseSummaryList: List[UseCase]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_users' function.
class ListUsersResponse(BaseValidatorModel):
    UserSummaryList: List[UserSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_view_versions' function.
class ListViewVersionsResponse(BaseValidatorModel):
    ViewVersionSummaryList: List[ViewVersionSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'list_views' function.
class ListViewsResponse(BaseValidatorModel):
    ViewsSummaryList: List[ViewSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

MetricFilterV2Union = Union[MetricFilterV2, MetricFilterV2Output]


class MetricV2Output(BaseValidatorModel):
    Name: Optional[str] = None
    Threshold: Optional[List[ThresholdV2]] = None
    MetricFilters: Optional[List[MetricFilterV2Output]] = None


class NewSessionDetails(BaseValidatorModel):
    SupportedMessagingContentTypes: Optional[List[str]] = None
    ParticipantDetails: Optional[ParticipantDetails] = None
    Attributes: Optional[Dict[str, str]] = None
    StreamingConfiguration: Optional[ChatStreamingConfiguration] = None


class SendNotificationActionDefinitionOutput(BaseValidatorModel):
    DeliveryMethod: Literal['EMAIL']
    Content: str
    ContentType: Literal['PLAIN_TEXT']
    Recipient: NotificationRecipientTypeOutput
    Subject: Optional[str] = None

NotificationRecipientTypeUnion = Union[NotificationRecipientType, NotificationRecipientTypeOutput]


class ParticipantTimerConfiguration(BaseValidatorModel):
    ParticipantRole: TimerEligibleParticipantRolesType
    TimerType: ParticipantTimerTypeType
    TimerValue: ParticipantTimerValue


class PredefinedAttribute(BaseValidatorModel):
    Name: Optional[str] = None
    Values: Optional[PredefinedAttributeValuesOutput] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None

PredefinedAttributeValuesUnion = Union[PredefinedAttributeValues, PredefinedAttributeValuesOutput]


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


# This class is the output for the 'search_resource_tags' function.
class SearchResourceTagsResponse(BaseValidatorModel):
    Tags: List[TagSet]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'search_security_profiles' function.
class SearchSecurityProfilesResponse(BaseValidatorModel):
    SecurityProfiles: List[SecurityProfileSearchSummary]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'search_vocabularies' function.
class SearchVocabulariesResponse(BaseValidatorModel):
    VocabularySummaryList: List[VocabularySummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class SearchableContactAttributes(BaseValidatorModel):
    Criteria: List[SearchableContactAttributesCriteria]
    MatchType: Optional[SearchContactsMatchTypeType] = None


class SearchableSegmentAttributes(BaseValidatorModel):
    Criteria: List[SearchableSegmentAttributesCriteria]
    MatchType: Optional[SearchContactsMatchTypeType] = None

SegmentAttributeValueUnion = Union[SegmentAttributeValue, SegmentAttributeValueOutput]


class SignInConfigOutput(BaseValidatorModel):
    Distributions: List[SignInDistribution]


class SignInConfig(BaseValidatorModel):
    Distributions: List[SignInDistribution]


# This class is the output for the 'start_attached_file_upload' function.
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
    Criteria: List[TranscriptCriteria]
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


class View(BaseValidatorModel):
    Id: Optional[str] = None
    Arn: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ViewStatusType] = None
    Type: Optional[ViewTypeType] = None
    Description: Optional[str] = None
    Version: Optional[int] = None
    VersionDescription: Optional[str] = None
    Content: Optional[ViewContent] = None
    Tags: Optional[Dict[str, str]] = None
    CreatedTime: Optional[datetime] = None
    LastModifiedTime: Optional[datetime] = None
    ViewContentSha256: Optional[str] = None


# This class is the output for the 'list_rules' function.
class ListRulesResponse(BaseValidatorModel):
    RuleSummaryList: List[RuleSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

AgentConfigUnion = Union[AgentConfig, AgentConfigOutput]

TelephonyConfigUnion = Union[TelephonyConfig, TelephonyConfigOutput]


class AgentInfo(BaseValidatorModel):
    Id: Optional[str] = None
    ConnectedToAgentTimestamp: Optional[datetime] = None
    AgentPauseDurationInSeconds: Optional[int] = None
    HierarchyGroups: Optional[HierarchyGroups] = None
    DeviceInfo: Optional[DeviceInfo] = None
    Capabilities: Optional[ParticipantCapabilities] = None


# This class is the input for the 'start_web_rtc_contact' function.
class StartWebRTCContactRequest(BaseValidatorModel):
    ContactFlowId: str
    InstanceId: str
    ParticipantDetails: ParticipantDetails
    Attributes: Optional[Dict[str, str]] = None
    ClientToken: Optional[str] = None
    AllowedCapabilities: Optional[AllowedCapabilities] = None
    RelatedContactId: Optional[str] = None
    References: Optional[Dict[str, Reference]] = None
    Description: Optional[str] = None


class QualityMetrics(BaseValidatorModel):
    Agent: Optional[AgentQualityMetrics] = None
    Customer: Optional[CustomerQualityMetrics] = None


class SearchPredefinedAttributesRequestPaginate(BaseValidatorModel):
    InstanceId: str
    SearchCriteria: Optional[PredefinedAttributeSearchCriteriaPaginator] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_predefined_attributes' function.
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


class MatchCriteria(BaseValidatorModel):
    AgentsCriteria: Optional[AgentsCriteriaUnion] = None


# This class is the input for the 'create_security_profile' function.
class CreateSecurityProfileRequest(BaseValidatorModel):
    SecurityProfileName: str
    InstanceId: str
    Description: Optional[str] = None
    Permissions: Optional[List[str]] = None
    Tags: Optional[Dict[str, str]] = None
    AllowedAccessControlTags: Optional[Dict[str, str]] = None
    TagRestrictedResources: Optional[List[str]] = None
    Applications: Optional[List[ApplicationUnion]] = None
    HierarchyRestrictedResources: Optional[List[str]] = None
    AllowedAccessControlHierarchyGroupId: Optional[str] = None


# This class is the input for the 'update_security_profile' function.
class UpdateSecurityProfileRequest(BaseValidatorModel):
    SecurityProfileId: str
    InstanceId: str
    Description: Optional[str] = None
    Permissions: Optional[List[str]] = None
    AllowedAccessControlTags: Optional[Dict[str, str]] = None
    TagRestrictedResources: Optional[List[str]] = None
    Applications: Optional[List[ApplicationUnion]] = None
    HierarchyRestrictedResources: Optional[List[str]] = None
    AllowedAccessControlHierarchyGroupId: Optional[str] = None


# This class is the output for the 'list_bots' function.
class ListBotsResponse(BaseValidatorModel):
    LexBots: List[LexBotConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'batch_get_attached_file_metadata' function.
class BatchGetAttachedFileMetadataResponse(BaseValidatorModel):
    Files: List[AttachedFile]
    Errors: List[AttachedFileError]
    ResponseMetadata: ResponseMetadata


class ControlPlaneUserAttributeFilter(BaseValidatorModel):
    OrConditions: Optional[List[AttributeAndCondition]] = None
    AndCondition: Optional[AttributeAndCondition] = None
    TagCondition: Optional[TagCondition] = None
    HierarchyGroupCondition: Optional[HierarchyGroupCondition] = None


class ControlPlaneAttributeFilter(BaseValidatorModel):
    OrConditions: Optional[List[CommonAttributeAndCondition]] = None
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


# This class is the output for the 'describe_phone_number' function.
class DescribePhoneNumberResponse(BaseValidatorModel):
    ClaimedPhoneNumberSummary: ClaimedPhoneNumberSummary
    ResponseMetadata: ResponseMetadata


class ListCondition(BaseValidatorModel):
    TargetListType: Optional[Literal['PROFICIENCIES']] = None
    Conditions: Optional[List[Condition]] = None


# This class is the input for the 'batch_put_contact' function.
class BatchPutContactRequest(BaseValidatorModel):
    InstanceId: str
    ContactDataRequestList: List[ContactDataRequest]
    ClientToken: Optional[str] = None


# This class is the input for the 'get_current_user_data' function.
class GetCurrentUserDataRequest(BaseValidatorModel):
    InstanceId: str
    Filters: UserDataFilters
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'search_contacts' function.
class SearchContactsResponse(BaseValidatorModel):
    Contacts: List[ContactSearchSummary]
    TotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None

TaskActionDefinitionUnion = Union[TaskActionDefinition, TaskActionDefinitionOutput]


# This class is the output for the 'describe_queue' function.
class DescribeQueueResponse(BaseValidatorModel):
    Queue: Queue
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_queues' function.
class SearchQueuesResponse(BaseValidatorModel):
    Queues: List[Queue]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_user' function.
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


# This class is the input for the 'update_routing_profile_concurrency' function.
class UpdateRoutingProfileConcurrencyRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    MediaConcurrencies: List[MediaConcurrency]


class CurrentMetricResult(BaseValidatorModel):
    Dimensions: Optional[Dimensions] = None
    Collections: Optional[List[CurrentMetricData]] = None


# This class is the input for the 'associate_routing_profile_queues' function.
class AssociateRoutingProfileQueuesRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    QueueConfigs: List[RoutingProfileQueueConfig]


# This class is the input for the 'create_routing_profile' function.
class CreateRoutingProfileRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    Description: str
    DefaultOutboundQueueId: str
    MediaConcurrencies: List[MediaConcurrency]
    QueueConfigs: Optional[List[RoutingProfileQueueConfig]] = None
    Tags: Optional[Dict[str, str]] = None
    AgentAvailabilityTimer: Optional[AgentAvailabilityTimerType] = None


# This class is the input for the 'update_routing_profile_queues' function.
class UpdateRoutingProfileQueuesRequest(BaseValidatorModel):
    InstanceId: str
    RoutingProfileId: str
    QueueConfigs: List[RoutingProfileQueueConfig]


class InstanceStorageConfig(BaseValidatorModel):
    StorageType: StorageTypeType
    AssociationId: Optional[str] = None
    S3Config: Optional[S3Config] = None
    KinesisVideoStreamConfig: Optional[KinesisVideoStreamConfig] = None
    KinesisStreamConfig: Optional[KinesisStreamConfig] = None
    KinesisFirehoseConfig: Optional[KinesisFirehoseConfig] = None


# This class is the input for the 'submit_contact_evaluation' function.
class SubmitContactEvaluationRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str
    Answers: Optional[Dict[str, EvaluationAnswerInput]] = None
    Notes: Optional[Dict[str, EvaluationNote]] = None


# This class is the input for the 'update_contact_evaluation' function.
class UpdateContactEvaluationRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationId: str
    Answers: Optional[Dict[str, EvaluationAnswerInput]] = None
    Notes: Optional[Dict[str, EvaluationNote]] = None


class EvaluationFormNumericQuestionPropertiesOutput(BaseValidatorModel):
    MinValue: int
    MaxValue: int
    Options: Optional[List[EvaluationFormNumericQuestionOption]] = None
    Automation: Optional[EvaluationFormNumericQuestionAutomation] = None


class EvaluationFormNumericQuestionProperties(BaseValidatorModel):
    MinValue: int
    MaxValue: int
    Options: Optional[List[EvaluationFormNumericQuestionOption]] = None
    Automation: Optional[EvaluationFormNumericQuestionAutomation] = None


class EvaluationFormSingleSelectQuestionAutomationOutput(BaseValidatorModel):
    Options: List[EvaluationFormSingleSelectQuestionAutomationOption]
    DefaultOptionRefId: Optional[str] = None


class EvaluationFormSingleSelectQuestionAutomation(BaseValidatorModel):
    Options: List[EvaluationFormSingleSelectQuestionAutomationOption]
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


# This class is the output for the 'list_contact_evaluations' function.
class ListContactEvaluationsResponse(BaseValidatorModel):
    EvaluationSummaryList: List[EvaluationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class CreateCaseActionDefinitionOutput(BaseValidatorModel):
    Fields: List[FieldValueOutput]
    TemplateId: str


class UpdateCaseActionDefinitionOutput(BaseValidatorModel):
    Fields: List[FieldValueOutput]


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


# This class is the output for the 'describe_user_hierarchy_structure' function.
class DescribeUserHierarchyStructureResponse(BaseValidatorModel):
    HierarchyStructure: HierarchyStructure
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_user_hierarchy_structure' function.
class UpdateUserHierarchyStructureRequest(BaseValidatorModel):
    HierarchyStructure: HierarchyStructureUpdate
    InstanceId: str


class GetMetricDataRequestPaginate(BaseValidatorModel):
    InstanceId: str
    StartTime: Timestamp
    EndTime: Timestamp
    Filters: Filters
    HistoricalMetrics: List[HistoricalMetric]
    Groupings: Optional[List[GroupingType]] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'get_metric_data' function.
class GetMetricDataRequest(BaseValidatorModel):
    InstanceId: str
    StartTime: Timestamp
    EndTime: Timestamp
    Filters: Filters
    HistoricalMetrics: List[HistoricalMetric]
    Groupings: Optional[List[GroupingType]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class HistoricalMetricData(BaseValidatorModel):
    Metric: Optional[HistoricalMetric] = None
    Value: Optional[float] = None


# This class is the input for the 'create_hours_of_operation' function.
class CreateHoursOfOperationRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    TimeZone: str
    Config: List[HoursOfOperationConfig]
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


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


# This class is the input for the 'update_hours_of_operation' function.
class UpdateHoursOfOperationRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    TimeZone: Optional[str] = None
    Config: Optional[List[HoursOfOperationConfig]] = None


# This class is the input for the 'create_hours_of_operation_override' function.
class CreateHoursOfOperationOverrideRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    Name: str
    Config: List[HoursOfOperationOverrideConfig]
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


# This class is the input for the 'update_hours_of_operation_override' function.
class UpdateHoursOfOperationOverrideRequest(BaseValidatorModel):
    InstanceId: str
    HoursOfOperationId: str
    HoursOfOperationOverrideId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    Config: Optional[List[HoursOfOperationOverrideConfig]] = None
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
    RequiredFields: Optional[List[RequiredFieldInfo]] = None
    ReadOnlyFields: Optional[List[ReadOnlyFieldInfo]] = None
    InvisibleFields: Optional[List[InvisibleFieldInfo]] = None


class TaskTemplateDefaultsOutput(BaseValidatorModel):
    DefaultFieldValues: Optional[List[TaskTemplateDefaultFieldValue]] = None


class TaskTemplateDefaults(BaseValidatorModel):
    DefaultFieldValues: Optional[List[TaskTemplateDefaultFieldValue]] = None

TaskTemplateFieldUnion = Union[TaskTemplateField, TaskTemplateFieldOutput]


class MetricV2(BaseValidatorModel):
    Name: Optional[str] = None
    Threshold: Optional[List[ThresholdV2]] = None
    MetricFilters: Optional[List[MetricFilterV2Union]] = None


class MetricDataV2(BaseValidatorModel):
    Metric: Optional[MetricV2Output] = None
    Value: Optional[float] = None


# This class is the input for the 'send_chat_integration_event' function.
class SendChatIntegrationEventRequest(BaseValidatorModel):
    SourceId: str
    DestinationId: str
    Event: ChatEvent
    Subtype: Optional[str] = None
    NewSessionDetails: Optional[NewSessionDetails] = None


class SendNotificationActionDefinition(BaseValidatorModel):
    DeliveryMethod: Literal['EMAIL']
    Content: str
    ContentType: Literal['PLAIN_TEXT']
    Recipient: NotificationRecipientTypeUnion
    Subject: Optional[str] = None


class ChatParticipantRoleConfig(BaseValidatorModel):
    ParticipantTimerConfigList: List[ParticipantTimerConfiguration]


# This class is the output for the 'describe_predefined_attribute' function.
class DescribePredefinedAttributeResponse(BaseValidatorModel):
    PredefinedAttribute: PredefinedAttribute
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_predefined_attributes' function.
class SearchPredefinedAttributesResponse(BaseValidatorModel):
    PredefinedAttributes: List[PredefinedAttribute]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_predefined_attribute' function.
class CreatePredefinedAttributeRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    Values: PredefinedAttributeValuesUnion


# This class is the input for the 'update_predefined_attribute' function.
class UpdatePredefinedAttributeRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    Values: Optional[PredefinedAttributeValuesUnion] = None


# This class is the input for the 'create_quick_connect' function.
class CreateQuickConnectRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    QuickConnectConfig: QuickConnectConfig
    Description: Optional[str] = None
    Tags: Optional[Dict[str, str]] = None


class QuickConnect(BaseValidatorModel):
    QuickConnectARN: Optional[str] = None
    QuickConnectId: Optional[str] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    QuickConnectConfig: Optional[QuickConnectConfig] = None
    Tags: Optional[Dict[str, str]] = None
    LastModifiedTime: Optional[datetime] = None
    LastModifiedRegion: Optional[str] = None


# This class is the input for the 'update_quick_connect_config' function.
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
    TranscriptItems: Optional[List[RealTimeContactAnalysisTranscriptItemWithCharacterOffsets]] = None


class RealTimeContactAnalysisIssueDetected(BaseValidatorModel):
    TranscriptItems: List[RealTimeContactAnalysisTranscriptItemWithContent]


# This class is the output for the 'list_contact_references' function.
class ListContactReferencesResponse(BaseValidatorModel):
    ReferenceSummaryList: List[ReferenceSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_instance' function.
class DescribeInstanceResponse(BaseValidatorModel):
    Instance: Instance
    ReplicationConfiguration: ReplicationConfiguration
    ResponseMetadata: ResponseMetadata


class SearchResourceTagsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    ResourceTypes: Optional[List[str]] = None
    SearchCriteria: Optional[ResourceTagsSearchCriteria] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_resource_tags' function.
class SearchResourceTagsRequest(BaseValidatorModel):
    InstanceId: str
    ResourceTypes: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchCriteria: Optional[ResourceTagsSearchCriteria] = None


# This class is the input for the 'create_contact' function.
class CreateContactRequest(BaseValidatorModel):
    InstanceId: str
    Channel: ChannelType
    InitiationMethod: ContactInitiationMethodType
    ClientToken: Optional[str] = None
    RelatedContactId: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    References: Optional[Dict[str, Reference]] = None
    ExpiryDurationInMinutes: Optional[int] = None
    UserInfo: Optional[UserInfo] = None
    InitiateAs: Optional[Literal['CONNECTED_TO_USER']] = None
    Name: Optional[str] = None
    Description: Optional[str] = None
    SegmentAttributes: Optional[Dict[str, SegmentAttributeValueUnion]] = None
    PreviousContactId: Optional[str] = None


# This class is the input for the 'start_chat_contact' function.
class StartChatContactRequest(BaseValidatorModel):
    InstanceId: str
    ContactFlowId: str
    ParticipantDetails: ParticipantDetails
    Attributes: Optional[Dict[str, str]] = None
    InitialMessage: Optional[ChatMessage] = None
    ClientToken: Optional[str] = None
    ChatDurationInMinutes: Optional[int] = None
    SupportedMessagingContentTypes: Optional[List[str]] = None
    PersistentChat: Optional[PersistentChat] = None
    RelatedContactId: Optional[str] = None
    SegmentAttributes: Optional[Dict[str, SegmentAttributeValueUnion]] = None
    CustomerId: Optional[str] = None


# This class is the input for the 'start_email_contact' function.
class StartEmailContactRequest(BaseValidatorModel):
    InstanceId: str
    FromEmailAddress: EmailAddressInfo
    DestinationEmailAddress: str
    EmailMessage: InboundEmailContent
    Description: Optional[str] = None
    References: Optional[Dict[str, Reference]] = None
    Name: Optional[str] = None
    AdditionalRecipients: Optional[InboundAdditionalRecipients] = None
    Attachments: Optional[List[EmailAttachment]] = None
    ContactFlowId: Optional[str] = None
    RelatedContactId: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    SegmentAttributes: Optional[Dict[str, SegmentAttributeValueUnion]] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'start_outbound_chat_contact' function.
class StartOutboundChatContactRequest(BaseValidatorModel):
    SourceEndpoint: Endpoint
    DestinationEndpoint: Endpoint
    InstanceId: str
    SegmentAttributes: Dict[str, SegmentAttributeValueUnion]
    ContactFlowId: str
    Attributes: Optional[Dict[str, str]] = None
    ChatDurationInMinutes: Optional[int] = None
    ParticipantDetails: Optional[ParticipantDetails] = None
    InitialSystemMessage: Optional[ChatMessage] = None
    RelatedContactId: Optional[str] = None
    SupportedMessagingContentTypes: Optional[List[str]] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'start_task_contact' function.
class StartTaskContactRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    PreviousContactId: Optional[str] = None
    ContactFlowId: Optional[str] = None
    Attributes: Optional[Dict[str, str]] = None
    References: Optional[Dict[str, Reference]] = None
    Description: Optional[str] = None
    ClientToken: Optional[str] = None
    ScheduledTime: Optional[Timestamp] = None
    TaskTemplateId: Optional[str] = None
    QuickConnectId: Optional[str] = None
    RelatedContactId: Optional[str] = None
    SegmentAttributes: Optional[Dict[str, SegmentAttributeValueUnion]] = None


class UpdateContactRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    Name: Optional[str] = None
    Description: Optional[str] = None
    References: Optional[Dict[str, Reference]] = None
    SegmentAttributes: Optional[Dict[str, SegmentAttributeValueUnion]] = None
    QueueInfo: Optional[QueueInfoInput] = None
    UserInfo: Optional[UserInfo] = None
    CustomerEndpoint: Optional[Endpoint] = None
    SystemEndpoint: Optional[Endpoint] = None


# This class is the output for the 'get_traffic_distribution' function.
class GetTrafficDistributionResponse(BaseValidatorModel):
    TelephonyConfig: TelephonyConfigOutput
    Id: str
    Arn: str
    SignInConfig: SignInConfigOutput
    AgentConfig: AgentConfigOutput
    ResponseMetadata: ResponseMetadata

SignInConfigUnion = Union[SignInConfig, SignInConfigOutput]


class OutboundEmailContent(BaseValidatorModel):
    MessageSourceType: OutboundMessageSourceTypeType
    TemplatedMessageConfig: Optional[TemplatedMessageConfig] = None
    RawMessage: Optional[OutboundRawMessage] = None


class ContactAnalysis(BaseValidatorModel):
    Transcript: Optional[Transcript] = None


# This class is the output for the 'search_users' function.
class SearchUsersResponse(BaseValidatorModel):
    Users: List[UserSearchSummary]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'create_view' function.
class CreateViewResponse(BaseValidatorModel):
    View: View
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_view_version' function.
class CreateViewVersionResponse(BaseValidatorModel):
    View: View
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_view' function.
class DescribeViewResponse(BaseValidatorModel):
    View: View
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_view_content' function.
class UpdateViewContentResponse(BaseValidatorModel):
    View: View
    ResponseMetadata: ResponseMetadata


class ExpressionOutput(BaseValidatorModel):
    AttributeCondition: Optional[AttributeConditionOutput] = None
    AndExpression: Optional[List[Dict[str, Any]]] = None
    OrExpression: Optional[List[Dict[str, Any]]] = None
    NotAttributeCondition: Optional[AttributeConditionOutput] = None

MatchCriteriaUnion = Union[MatchCriteria, MatchCriteriaOutput]


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


# This class is the input for the 'search_contact_flow_modules' function.
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


# This class is the input for the 'search_contact_flows' function.
class SearchContactFlowsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[ContactFlowSearchFilter] = None
    SearchCriteria: Optional[ContactFlowSearchCriteria] = None


# This class is the input for the 'search_email_addresses' function.
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


# This class is the input for the 'search_hours_of_operation_overrides' function.
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


# This class is the input for the 'search_hours_of_operations' function.
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


# This class is the input for the 'search_prompts' function.
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


# This class is the input for the 'search_queues' function.
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


# This class is the input for the 'search_quick_connects' function.
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


# This class is the input for the 'search_routing_profiles' function.
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


# This class is the input for the 'search_security_profiles' function.
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
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    ListCondition: Optional[ListCondition] = None
    HierarchyGroupCondition: Optional[HierarchyGroupCondition] = None


class UserSearchCriteria(BaseValidatorModel):
    OrConditions: Optional[List[Dict[str, Any]]] = None
    AndConditions: Optional[List[Dict[str, Any]]] = None
    StringCondition: Optional[StringCondition] = None
    ListCondition: Optional[ListCondition] = None
    HierarchyGroupCondition: Optional[HierarchyGroupCondition] = None


# This class is the output for the 'describe_routing_profile' function.
class DescribeRoutingProfileResponse(BaseValidatorModel):
    RoutingProfile: RoutingProfile
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_routing_profiles' function.
class SearchRoutingProfilesResponse(BaseValidatorModel):
    RoutingProfiles: List[RoutingProfile]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_current_metric_data' function.
class GetCurrentMetricDataResponse(BaseValidatorModel):
    MetricResults: List[CurrentMetricResult]
    DataSnapshotTime: datetime
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'associate_instance_storage_config' function.
class AssociateInstanceStorageConfigRequest(BaseValidatorModel):
    InstanceId: str
    ResourceType: InstanceStorageResourceTypeType
    StorageConfig: InstanceStorageConfig
    ClientToken: Optional[str] = None


# This class is the output for the 'describe_instance_storage_config' function.
class DescribeInstanceStorageConfigResponse(BaseValidatorModel):
    StorageConfig: InstanceStorageConfig
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_instance_storage_configs' function.
class ListInstanceStorageConfigsResponse(BaseValidatorModel):
    StorageConfigs: List[InstanceStorageConfig]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'update_instance_storage_config' function.
class UpdateInstanceStorageConfigRequest(BaseValidatorModel):
    InstanceId: str
    AssociationId: str
    ResourceType: InstanceStorageResourceTypeType
    StorageConfig: InstanceStorageConfig
    ClientToken: Optional[str] = None

EvaluationFormNumericQuestionPropertiesUnion = Union[EvaluationFormNumericQuestionProperties, EvaluationFormNumericQuestionPropertiesOutput]


class EvaluationFormSingleSelectQuestionPropertiesOutput(BaseValidatorModel):
    Options: List[EvaluationFormSingleSelectQuestionOption]
    DisplayAs: Optional[EvaluationFormSingleSelectQuestionDisplayModeType] = None
    Automation: Optional[EvaluationFormSingleSelectQuestionAutomationOutput] = None

EvaluationFormSingleSelectQuestionAutomationUnion = Union[EvaluationFormSingleSelectQuestionAutomation, EvaluationFormSingleSelectQuestionAutomationOutput]


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

FieldValueUnionExtra = Union[FieldValue, FieldValueOutput]


# This class is the output for the 'get_current_user_data' function.
class GetCurrentUserDataResponse(BaseValidatorModel):
    UserDataList: List[UserData]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_user_hierarchy_group' function.
class DescribeUserHierarchyGroupResponse(BaseValidatorModel):
    HierarchyGroup: HierarchyGroup
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_user_hierarchy_groups' function.
class SearchUserHierarchyGroupsResponse(BaseValidatorModel):
    UserHierarchyGroups: List[HierarchyGroup]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class HistoricalMetricResult(BaseValidatorModel):
    Dimensions: Optional[Dimensions] = None
    Collections: Optional[List[HistoricalMetricData]] = None


# This class is the output for the 'describe_hours_of_operation' function.
class DescribeHoursOfOperationResponse(BaseValidatorModel):
    HoursOfOperation: HoursOfOperation
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_hours_of_operations' function.
class SearchHoursOfOperationsResponse(BaseValidatorModel):
    HoursOfOperations: List[HoursOfOperation]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_hours_of_operation_override' function.
class DescribeHoursOfOperationOverrideResponse(BaseValidatorModel):
    HoursOfOperationOverride: HoursOfOperationOverride
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_hours_of_operation_overrides' function.
class ListHoursOfOperationOverridesResponse(BaseValidatorModel):
    HoursOfOperationOverrideList: List[HoursOfOperationOverride]
    LastModifiedRegion: str
    LastModifiedTime: datetime
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'search_hours_of_operation_overrides' function.
class SearchHoursOfOperationOverridesResponse(BaseValidatorModel):
    HoursOfOperationOverrides: List[HoursOfOperationOverride]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_effective_hours_of_operations' function.
class GetEffectiveHoursOfOperationsResponse(BaseValidatorModel):
    EffectiveHoursOfOperationList: List[EffectiveHoursOfOperations]
    TimeZone: str
    ResponseMetadata: ResponseMetadata

TaskTemplateConstraintsUnion = Union[TaskTemplateConstraints, TaskTemplateConstraintsOutput]


# This class is the output for the 'get_task_template' function.
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


# This class is the output for the 'update_task_template' function.
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

TaskTemplateDefaultsUnion = Union[TaskTemplateDefaults, TaskTemplateDefaultsOutput]

MetricV2Union = Union[MetricV2, MetricV2Output]


class MetricResultV2(BaseValidatorModel):
    Dimensions: Optional[Dict[str, str]] = None
    MetricInterval: Optional[MetricInterval] = None
    Collections: Optional[List[MetricDataV2]] = None

SendNotificationActionDefinitionUnion = Union[SendNotificationActionDefinition, SendNotificationActionDefinitionOutput]


class UpdateParticipantRoleConfigChannelInfo(BaseValidatorModel):
    Chat: Optional[ChatParticipantRoleConfig] = None


# This class is the output for the 'describe_quick_connect' function.
class DescribeQuickConnectResponse(BaseValidatorModel):
    QuickConnect: QuickConnect
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_quick_connects' function.
class SearchQuickConnectsResponse(BaseValidatorModel):
    QuickConnects: List[QuickConnect]
    ApproximateTotalCount: int
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RealTimeContactAnalysisCategoryDetails(BaseValidatorModel):
    PointsOfInterest: List[RealTimeContactAnalysisPointOfInterest]


class RealTimeContactAnalysisSegmentIssues(BaseValidatorModel):
    IssuesDetected: List[RealTimeContactAnalysisIssueDetected]


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


# This class is the input for the 'start_outbound_email_contact' function.
class StartOutboundEmailContactRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    DestinationEmailAddress: EmailAddressInfo
    EmailMessage: OutboundEmailContent
    FromEmailAddress: Optional[EmailAddressInfo] = None
    AdditionalRecipients: Optional[OutboundAdditionalRecipients] = None
    ClientToken: Optional[str] = None


class SearchCriteria(BaseValidatorModel):
    AgentIds: Optional[List[str]] = None
    AgentHierarchyGroups: Optional[AgentHierarchyGroups] = None
    Channels: Optional[List[ChannelType]] = None
    ContactAnalysis: Optional[ContactAnalysis] = None
    InitiationMethods: Optional[List[ContactInitiationMethodType]] = None
    QueueIds: Optional[List[str]] = None
    SearchableContactAttributes: Optional[SearchableContactAttributes] = None
    SearchableSegmentAttributes: Optional[SearchableSegmentAttributes] = None


class Step(BaseValidatorModel):
    Expiry: Optional[Expiry] = None
    Expression: Optional[ExpressionOutput] = None
    Status: Optional[RoutingCriteriaStepStatusType] = None


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


# This class is the input for the 'search_agent_statuses' function.
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


# This class is the input for the 'search_user_hierarchy_groups' function.
class SearchUserHierarchyGroupsRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[UserHierarchyGroupSearchFilter] = None
    SearchCriteria: Optional[UserHierarchyGroupSearchCriteria] = None


# This class is the output for the 'start_web_rtc_contact' function.
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


# This class is the input for the 'search_users' function.
class SearchUsersRequest(BaseValidatorModel):
    InstanceId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None
    SearchFilter: Optional[UserSearchFilter] = None
    SearchCriteria: Optional[UserSearchCriteria] = None


class EvaluationFormQuestionTypePropertiesOutput(BaseValidatorModel):
    Numeric: Optional[EvaluationFormNumericQuestionPropertiesOutput] = None
    SingleSelect: Optional[EvaluationFormSingleSelectQuestionPropertiesOutput] = None


class EvaluationFormSingleSelectQuestionProperties(BaseValidatorModel):
    Options: List[EvaluationFormSingleSelectQuestionOption]
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


class CreateCaseActionDefinition(BaseValidatorModel):
    Fields: List[FieldValueUnionExtra]
    TemplateId: str


class UpdateCaseActionDefinition(BaseValidatorModel):
    Fields: List[FieldValueUnionExtra]


# This class is the output for the 'get_metric_data' function.
class GetMetricDataResponse(BaseValidatorModel):
    MetricResults: List[HistoricalMetricResult]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the input for the 'create_task_template' function.
class CreateTaskTemplateRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    Fields: List[TaskTemplateFieldUnion]
    Description: Optional[str] = None
    ContactFlowId: Optional[str] = None
    SelfAssignFlowId: Optional[str] = None
    Constraints: Optional[TaskTemplateConstraintsUnion] = None
    Defaults: Optional[TaskTemplateDefaultsUnion] = None
    Status: Optional[TaskTemplateStatusType] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'update_task_template' function.
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
    Fields: Optional[List[TaskTemplateFieldUnion]] = None


# This class is the input for the 'get_metric_data_v2' function.
class GetMetricDataV2Request(BaseValidatorModel):
    ResourceArn: str
    StartTime: Timestamp
    EndTime: Timestamp
    Filters: List[FilterV2]
    Metrics: List[MetricV2Union]
    Interval: Optional[IntervalDetails] = None
    Groupings: Optional[List[str]] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the output for the 'get_metric_data_v2' function.
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


class SearchContactsRequestPaginate(BaseValidatorModel):
    InstanceId: str
    TimeRange: SearchContactsTimeRange
    SearchCriteria: Optional[SearchCriteria] = None
    Sort: Optional[Sort] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'search_contacts' function.
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

AttributeConditionUnion = Union[AttributeCondition, AttributeConditionOutput]


class EvaluationFormQuestionOutput(BaseValidatorModel):
    Title: str
    RefId: str
    QuestionType: EvaluationFormQuestionTypeType
    Instructions: Optional[str] = None
    NotApplicableEnabled: Optional[bool] = None
    QuestionTypeProperties: Optional[EvaluationFormQuestionTypePropertiesOutput] = None
    Weight: Optional[float] = None

EvaluationFormSingleSelectQuestionPropertiesUnion = Union[EvaluationFormSingleSelectQuestionProperties, EvaluationFormSingleSelectQuestionPropertiesOutput]


# This class is the output for the 'describe_rule' function.
class DescribeRuleResponse(BaseValidatorModel):
    Rule: Rule
    ResponseMetadata: ResponseMetadata

CreateCaseActionDefinitionUnion = Union[CreateCaseActionDefinition, CreateCaseActionDefinitionOutput]

UpdateCaseActionDefinitionUnion = Union[UpdateCaseActionDefinition, UpdateCaseActionDefinitionOutput]


class RealtimeContactAnalysisSegment(BaseValidatorModel):
    Transcript: Optional[RealTimeContactAnalysisSegmentTranscript] = None
    Categories: Optional[RealTimeContactAnalysisSegmentCategories] = None
    Issues: Optional[RealTimeContactAnalysisSegmentIssues] = None
    Event: Optional[RealTimeContactAnalysisSegmentEvent] = None
    Attachments: Optional[RealTimeContactAnalysisSegmentAttachments] = None
    PostContactSummary: Optional[RealTimeContactAnalysisSegmentPostContactSummary] = None


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


class Expression(BaseValidatorModel):
    AttributeCondition: Optional[AttributeConditionUnion] = None
    AndExpression: Optional[List[Dict[str, Any]]] = None
    OrExpression: Optional[List[Dict[str, Any]]] = None
    NotAttributeCondition: Optional[AttributeConditionUnion] = None


class EvaluationFormItemOutput(BaseValidatorModel):
    Section: Optional[EvaluationFormSectionOutput] = None
    Question: Optional[EvaluationFormQuestionOutput] = None


class EvaluationFormQuestionTypeProperties(BaseValidatorModel):
    Numeric: Optional[EvaluationFormNumericQuestionPropertiesUnion] = None
    SingleSelect: Optional[EvaluationFormSingleSelectQuestionPropertiesUnion] = None


class RuleAction(BaseValidatorModel):
    ActionType: ActionTypeType
    TaskAction: Optional[TaskActionDefinitionUnion] = None
    EventBridgeAction: Optional[EventBridgeActionDefinition] = None
    AssignContactCategoryAction: Optional[Dict[str, Any]] = None
    SendNotificationAction: Optional[SendNotificationActionDefinitionUnion] = None
    CreateCaseAction: Optional[CreateCaseActionDefinitionUnion] = None
    UpdateCaseAction: Optional[UpdateCaseActionDefinitionUnion] = None
    EndAssociatedTasksAction: Optional[Dict[str, Any]] = None
    SubmitAutoEvaluationAction: Optional[SubmitAutoEvaluationActionDefinition] = None


# This class is the output for the 'list_realtime_contact_analysis_segments_v2' function.
class ListRealtimeContactAnalysisSegmentsV2Response(BaseValidatorModel):
    Channel: RealTimeContactAnalysisSupportedChannelType
    Status: RealTimeContactAnalysisStatusType
    Segments: List[RealtimeContactAnalysisSegment]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'describe_contact' function.
class DescribeContactResponse(BaseValidatorModel):
    Contact: Contact
    ResponseMetadata: ResponseMetadata

ExpressionUnion = Union[Expression, ExpressionOutput]


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

EvaluationFormQuestionTypePropertiesUnion = Union[EvaluationFormQuestionTypeProperties, EvaluationFormQuestionTypePropertiesOutput]

RuleActionUnion = Union[RuleAction, RuleActionOutput]


class RoutingCriteriaInputStep(BaseValidatorModel):
    Expiry: Optional[RoutingCriteriaInputStepExpiry] = None
    Expression: Optional[ExpressionUnion] = None


# This class is the output for the 'describe_contact_evaluation' function.
class DescribeContactEvaluationResponse(BaseValidatorModel):
    Evaluation: Evaluation
    EvaluationForm: EvaluationFormContent
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'describe_evaluation_form' function.
class DescribeEvaluationFormResponse(BaseValidatorModel):
    EvaluationForm: EvaluationForm
    ResponseMetadata: ResponseMetadata


class EvaluationFormQuestion(BaseValidatorModel):
    Title: str
    RefId: str
    QuestionType: EvaluationFormQuestionTypeType
    Instructions: Optional[str] = None
    NotApplicableEnabled: Optional[bool] = None
    QuestionTypeProperties: Optional[EvaluationFormQuestionTypePropertiesUnion] = None
    Weight: Optional[float] = None


# This class is the input for the 'create_rule' function.
class CreateRuleRequest(BaseValidatorModel):
    InstanceId: str
    Name: str
    TriggerEventSource: RuleTriggerEventSource
    Function: str
    Actions: List[RuleActionUnion]
    PublishStatus: RulePublishStatusType
    ClientToken: Optional[str] = None


# This class is the input for the 'update_rule' function.
class UpdateRuleRequest(BaseValidatorModel):
    RuleId: str
    InstanceId: str
    Name: str
    Function: str
    Actions: List[RuleActionUnion]
    PublishStatus: RulePublishStatusType


class RoutingCriteriaInput(BaseValidatorModel):
    Steps: Optional[List[RoutingCriteriaInputStep]] = None

EvaluationFormQuestionUnion = Union[EvaluationFormQuestion, EvaluationFormQuestionOutput]


class UpdateContactRoutingDataRequest(BaseValidatorModel):
    InstanceId: str
    ContactId: str
    QueueTimeAdjustmentSeconds: Optional[int] = None
    QueuePriority: Optional[int] = None
    RoutingCriteria: Optional[RoutingCriteriaInput] = None


class EvaluationFormItem(BaseValidatorModel):
    Section: Optional[EvaluationFormSectionUnion] = None
    Question: Optional[EvaluationFormQuestionUnion] = None

EvaluationFormItemUnion = Union[EvaluationFormItem, EvaluationFormItemOutput]


# This class is the input for the 'create_evaluation_form' function.
class CreateEvaluationFormRequest(BaseValidatorModel):
    InstanceId: str
    Title: str
    Items: List[EvaluationFormItemUnion]
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategy] = None
    ClientToken: Optional[str] = None


# This class is the input for the 'update_evaluation_form' function.
class UpdateEvaluationFormRequest(BaseValidatorModel):
    InstanceId: str
    EvaluationFormId: str
    EvaluationFormVersion: int
    Title: str
    Items: List[EvaluationFormItemUnion]
    CreateNewVersion: Optional[bool] = None
    Description: Optional[str] = None
    ScoringStrategy: Optional[EvaluationFormScoringStrategy] = None
    ClientToken: Optional[str] = None