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
from aws_resource_validator.pydantic_models.chime_constants import *

class AccountSettingsTypeDef(BaseValidatorModel):
    DisableRemoteControl: Optional[bool] = None
    EnableDialOut: Optional[bool] = None

class SigninDelegateGroupTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None

class AddressTypeDef(BaseValidatorModel):
    streetName: Optional[str] = None
    streetSuffix: Optional[str] = None
    postDirectional: Optional[str] = None
    preDirectional: Optional[str] = None
    streetNumber: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    postalCodePlus4: Optional[str] = None
    country: Optional[str] = None

class AlexaForBusinessMetadataTypeDef(BaseValidatorModel):
    IsAlexaForBusinessEnabled: Optional[bool] = None
    AlexaForBusinessRoomArn: Optional[str] = None

class IdentityTypeDef(BaseValidatorModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class ChannelRetentionSettingsTypeDef(BaseValidatorModel):
    RetentionDays: Optional[int] = None

class AppInstanceStreamingConfigurationTypeDef(BaseValidatorModel):
    AppInstanceDataType: AppInstanceDataTypeType
    ResourceArn: str

class AppInstanceSummaryTypeDef(BaseValidatorModel):
    AppInstanceArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None

class AppInstanceTypeDef(BaseValidatorModel):
    AppInstanceArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class AppInstanceUserMembershipSummaryTypeDef(BaseValidatorModel):
    Type: Optional[ChannelMembershipTypeType] = None
    ReadMarkerTimestamp: Optional[datetime] = None

class AppInstanceUserSummaryTypeDef(BaseValidatorModel):
    AppInstanceUserArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None

class AppInstanceUserTypeDef(BaseValidatorModel):
    AppInstanceUserArn: Optional[str] = None
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    Metadata: Optional[str] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class AudioArtifactsConfigurationTypeDef(BaseValidatorModel):
    MuxType: AudioMuxTypeType

class ContentArtifactsConfigurationTypeDef(BaseValidatorModel):
    State: ArtifactsStateType
    MuxType: Optional[Literal["ContentOnly"]] = None

class VideoArtifactsConfigurationTypeDef(BaseValidatorModel):
    State: ArtifactsStateType
    MuxType: Optional[Literal["VideoOnly"]] = None

class AssociatePhoneNumberWithUserRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str
    E164PhoneNumber: str

class AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: Sequence[str]
    ForceAssociate: Optional[bool] = None

class PhoneNumberErrorTypeDef(BaseValidatorModel):
    PhoneNumberId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    E164PhoneNumbers: Sequence[str]
    ForceAssociate: Optional[bool] = None

class AttendeeTypeDef(BaseValidatorModel):
    ExternalUserId: Optional[str] = None
    AttendeeId: Optional[str] = None
    JoinToken: Optional[str] = None

class CreateAttendeeErrorTypeDef(BaseValidatorModel):
    ExternalUserId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class BatchCreateChannelMembershipErrorTypeDef(BaseValidatorModel):
    MemberArn: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class BatchCreateChannelMembershipRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArns: Sequence[str]
    Type: Optional[ChannelMembershipTypeType] = None
    ChimeBearer: Optional[str] = None

class MembershipItemTypeDef(BaseValidatorModel):
    MemberId: Optional[str] = None
    Role: Optional[RoomMembershipRoleType] = None

class MemberErrorTypeDef(BaseValidatorModel):
    MemberId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class BatchDeletePhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberIds: Sequence[str]

class BatchSuspendUserRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserIdList: Sequence[str]

class UserErrorTypeDef(BaseValidatorModel):
    UserId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class BatchUnsuspendUserRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserIdList: Sequence[str]

class UpdatePhoneNumberRequestItemTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None

class BotTypeDef(BaseValidatorModel):
    BotId: Optional[str] = None
    UserId: Optional[str] = None
    DisplayName: Optional[str] = None
    BotType: Optional[Literal["ChatBot"]] = None
    Disabled: Optional[bool] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    BotEmail: Optional[str] = None
    SecurityToken: Optional[str] = None

class BusinessCallingSettingsTypeDef(BaseValidatorModel):
    CdrBucket: Optional[str] = None

class CandidateAddressTypeDef(BaseValidatorModel):
    streetInfo: Optional[str] = None
    streetNumber: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    postalCodePlus4: Optional[str] = None
    country: Optional[str] = None

class ChannelSummaryTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ChannelArn: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    LastMessageTimestamp: Optional[datetime] = None

class ConversationRetentionSettingsTypeDef(BaseValidatorModel):
    RetentionDays: Optional[int] = None

class CreateAccountRequestRequestTypeDef(BaseValidatorModel):
    Name: str

class CreateAppInstanceAdminRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class CreateBotRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    DisplayName: str
    Domain: Optional[str] = None

class CreateChannelBanRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: Optional[str] = None

class CreateChannelMembershipRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    Type: ChannelMembershipTypeType
    ChimeBearer: Optional[str] = None

class CreateChannelModeratorRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: Optional[str] = None

class CreateMeetingDialOutRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    FromPhoneNumber: str
    ToPhoneNumber: str
    JoinToken: str

class MeetingNotificationConfigurationTypeDef(BaseValidatorModel):
    SnsTopicArn: Optional[str] = None
    SqsQueueArn: Optional[str] = None

class CreatePhoneNumberOrderRequestRequestTypeDef(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType
    E164PhoneNumbers: Sequence[str]

class GeoMatchParamsTypeDef(BaseValidatorModel):
    Country: str
    AreaCode: str

class CreateRoomMembershipRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MemberId: str
    Role: Optional[RoomMembershipRoleType] = None

class CreateRoomRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: str
    ClientRequestToken: Optional[str] = None

class RoomTypeDef(BaseValidatorModel):
    RoomId: Optional[str] = None
    Name: Optional[str] = None
    AccountId: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class CreateSipMediaApplicationCallRequestRequestTypeDef(BaseValidatorModel):
    FromPhoneNumber: str
    ToPhoneNumber: str
    SipMediaApplicationId: str
    SipHeaders: Optional[Mapping[str, str]] = None

class SipMediaApplicationCallTypeDef(BaseValidatorModel):
    TransactionId: Optional[str] = None

class SipMediaApplicationEndpointTypeDef(BaseValidatorModel):
    LambdaArn: Optional[str] = None

class SipRuleTargetApplicationTypeDef(BaseValidatorModel):
    SipMediaApplicationId: Optional[str] = None
    Priority: Optional[int] = None
    AwsRegion: Optional[str] = None

class CreateUserRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Username: Optional[str] = None
    Email: Optional[str] = None
    UserType: Optional[UserTypeType] = None

class VoiceConnectorItemTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Priority: int

class CreateVoiceConnectorRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    RequireEncryption: bool
    AwsRegion: Optional[VoiceConnectorAwsRegionType] = None

class VoiceConnectorTypeDef(BaseValidatorModel):
    VoiceConnectorId: Optional[str] = None
    AwsRegion: Optional[VoiceConnectorAwsRegionType] = None
    Name: Optional[str] = None
    OutboundHostName: Optional[str] = None
    RequireEncryption: Optional[bool] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    VoiceConnectorArn: Optional[str] = None

class CredentialTypeDef(BaseValidatorModel):
    Username: Optional[str] = None
    Password: Optional[str] = None

class DNISEmergencyCallingConfigurationTypeDef(BaseValidatorModel):
    EmergencyPhoneNumber: str
    CallingCountry: str
    TestPhoneNumber: Optional[str] = None

class DeleteAccountRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str

class DeleteAppInstanceAdminRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class DeleteAppInstanceRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str

class DeleteAppInstanceStreamingConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str

class DeleteAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str

class DeleteAttendeeRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str

class DeleteChannelBanRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: Optional[str] = None

class DeleteChannelMembershipRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: Optional[str] = None

class DeleteChannelMessageRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: Optional[str] = None

class DeleteChannelModeratorRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: Optional[str] = None

class DeleteChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: Optional[str] = None

class DeleteEventsConfigurationRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BotId: str

class DeleteMediaCapturePipelineRequestRequestTypeDef(BaseValidatorModel):
    MediaPipelineId: str

class DeleteMeetingRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str

class DeletePhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str

class DeleteProxySessionRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    ProxySessionId: str

class DeleteRoomMembershipRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MemberId: str

class DeleteRoomRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str

class DeleteSipMediaApplicationRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str

class DeleteSipRuleRequestRequestTypeDef(BaseValidatorModel):
    SipRuleId: str

class DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorGroupRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorGroupId: str

class DeleteVoiceConnectorOriginationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorProxyRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Usernames: Sequence[str]

class DeleteVoiceConnectorTerminationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class DescribeAppInstanceAdminRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class DescribeAppInstanceRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str

class DescribeAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str

class DescribeChannelBanRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: Optional[str] = None

class DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: Optional[str] = None

class DescribeChannelMembershipRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: Optional[str] = None

class DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: Optional[str] = None

class DescribeChannelModeratorRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: Optional[str] = None

class DescribeChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: Optional[str] = None

class DisassociatePhoneNumberFromUserRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str

class DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: Sequence[str]

class DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    E164PhoneNumbers: Sequence[str]

class DisassociateSigninDelegateGroupsFromAccountRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    GroupNames: Sequence[str]

class EngineTranscribeMedicalSettingsTypeDef(BaseValidatorModel):
    LanguageCode: Literal["en-US"]
    Specialty: TranscribeMedicalSpecialtyType
    Type: TranscribeMedicalTypeType
    VocabularyName: Optional[str] = None
    Region: Optional[TranscribeMedicalRegionType] = None
    ContentIdentificationType: Optional[Literal["PHI"]] = None

class EngineTranscribeSettingsTypeDef(BaseValidatorModel):
    LanguageCode: Optional[TranscribeLanguageCodeType] = None
    VocabularyFilterMethod: Optional[TranscribeVocabularyFilterMethodType] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyName: Optional[str] = None
    Region: Optional[TranscribeRegionType] = None
    EnablePartialResultsStabilization: Optional[bool] = None
    PartialResultsStability: Optional[TranscribePartialResultsStabilityType] = None
    ContentIdentificationType: Optional[Literal["PII"]] = None
    ContentRedactionType: Optional[Literal["PII"]] = None
    PiiEntityTypes: Optional[str] = None
    LanguageModelName: Optional[str] = None
    IdentifyLanguage: Optional[bool] = None
    LanguageOptions: Optional[str] = None
    PreferredLanguage: Optional[TranscribeLanguageCodeType] = None
    VocabularyNames: Optional[str] = None
    VocabularyFilterNames: Optional[str] = None

class EventsConfigurationTypeDef(BaseValidatorModel):
    BotId: Optional[str] = None
    OutboundEventsHTTPSEndpoint: Optional[str] = None
    LambdaFunctionArn: Optional[str] = None

class GetAccountRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str

class GetAccountSettingsRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str

class GetAppInstanceRetentionSettingsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str

class GetAppInstanceStreamingConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str

class GetAttendeeRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str

class GetBotRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BotId: str

class GetChannelMessageRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: Optional[str] = None

class GetEventsConfigurationRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BotId: str

class VoiceConnectorSettingsTypeDef(BaseValidatorModel):
    CdrBucket: Optional[str] = None

class GetMediaCapturePipelineRequestRequestTypeDef(BaseValidatorModel):
    MediaPipelineId: str

class GetMeetingRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str

class MessagingSessionEndpointTypeDef(BaseValidatorModel):
    Url: Optional[str] = None

class GetPhoneNumberOrderRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberOrderId: str

class GetPhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str

class GetProxySessionRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    ProxySessionId: str

class GetRetentionSettingsRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str

class GetRoomRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str

class GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str

class SipMediaApplicationLoggingConfigurationTypeDef(BaseValidatorModel):
    EnableSipMediaApplicationMessageLogs: Optional[bool] = None

class GetSipMediaApplicationRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str

class GetSipRuleRequestRequestTypeDef(BaseValidatorModel):
    SipRuleId: str

class GetUserRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str

class GetUserSettingsRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str

class GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class GetVoiceConnectorGroupRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorGroupId: str

class GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class LoggingConfigurationTypeDef(BaseValidatorModel):
    EnableSIPLogs: Optional[bool] = None
    EnableMediaMetricLogs: Optional[bool] = None

class GetVoiceConnectorOriginationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class GetVoiceConnectorProxyRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class ProxyTypeDef(BaseValidatorModel):
    DefaultSessionExpiryMinutes: Optional[int] = None
    Disabled: Optional[bool] = None
    FallBackPhoneNumber: Optional[str] = None
    PhoneNumberCountries: Optional[List[str]] = None

class GetVoiceConnectorRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class GetVoiceConnectorTerminationHealthRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class TerminationHealthTypeDef(BaseValidatorModel):
    Timestamp: Optional[datetime] = None
    Source: Optional[str] = None

class GetVoiceConnectorTerminationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class TerminationTypeDef(BaseValidatorModel):
    CpsLimit: Optional[int] = None
    DefaultPhoneNumber: Optional[str] = None
    CallingRegions: Optional[List[str]] = None
    CidrAllowedList: Optional[List[str]] = None
    Disabled: Optional[bool] = None

class InviteTypeDef(BaseValidatorModel):
    InviteId: Optional[str] = None
    Status: Optional[InviteStatusType] = None
    EmailAddress: Optional[str] = None
    EmailStatus: Optional[EmailStatusType] = None

class InviteUsersRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserEmailList: Sequence[str]
    UserType: Optional[UserTypeType] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccountsRequestRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    UserEmail: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAppInstanceAdminsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppInstanceUsersRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppInstancesRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAttendeeTagsRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str

class ListAttendeesRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListBotsRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelBansRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListChannelMembershipsRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    Type: Optional[ChannelMembershipTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListChannelModeratorsRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    Privacy: Optional[ChannelPrivacyType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListMediaCapturePipelinesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMeetingTagsRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str

class ListMeetingsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPhoneNumberOrdersRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPhoneNumbersRequestRequestTypeDef(BaseValidatorModel):
    Status: Optional[PhoneNumberStatusType] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    FilterName: Optional[PhoneNumberAssociationNameType] = None
    FilterValue: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListProxySessionsRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Status: Optional[ProxySessionStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRoomMembershipsRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRoomsRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    MemberId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSipMediaApplicationsRequestRequestTypeDef(BaseValidatorModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSipRulesRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSupportedPhoneNumberCountriesRequestRequestTypeDef(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType

class PhoneNumberCountryTypeDef(BaseValidatorModel):
    CountryCode: Optional[str] = None
    SupportedPhoneNumberTypes: Optional[List[PhoneNumberTypeType]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class ListUsersRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserEmail: Optional[str] = None
    UserType: Optional[UserTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListVoiceConnectorGroupsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str

class ListVoiceConnectorsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class LogoutUserRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str

class MediaPlacementTypeDef(BaseValidatorModel):
    AudioHostUrl: Optional[str] = None
    AudioFallbackUrl: Optional[str] = None
    ScreenDataUrl: Optional[str] = None
    ScreenSharingUrl: Optional[str] = None
    ScreenViewingUrl: Optional[str] = None
    SignalingUrl: Optional[str] = None
    TurnControlUrl: Optional[str] = None
    EventIngestionUrl: Optional[str] = None

class MemberTypeDef(BaseValidatorModel):
    MemberId: Optional[str] = None
    MemberType: Optional[MemberTypeType] = None
    Email: Optional[str] = None
    FullName: Optional[str] = None
    AccountId: Optional[str] = None

class OrderedPhoneNumberTypeDef(BaseValidatorModel):
    E164PhoneNumber: Optional[str] = None
    Status: Optional[OrderedPhoneNumberStatusType] = None

class OriginationRouteTypeDef(BaseValidatorModel):
    Host: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[OriginationRouteProtocolType] = None
    Priority: Optional[int] = None
    Weight: Optional[int] = None

class ParticipantTypeDef(BaseValidatorModel):
    PhoneNumber: Optional[str] = None
    ProxyPhoneNumber: Optional[str] = None

class PhoneNumberAssociationTypeDef(BaseValidatorModel):
    Value: Optional[str] = None
    Name: Optional[PhoneNumberAssociationNameType] = None
    AssociatedTimestamp: Optional[datetime] = None

class PhoneNumberCapabilitiesTypeDef(BaseValidatorModel):
    InboundCall: Optional[bool] = None
    OutboundCall: Optional[bool] = None
    InboundSMS: Optional[bool] = None
    OutboundSMS: Optional[bool] = None
    InboundMMS: Optional[bool] = None
    OutboundMMS: Optional[bool] = None

class PutEventsConfigurationRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BotId: str
    OutboundEventsHTTPSEndpoint: Optional[str] = None
    LambdaFunctionArn: Optional[str] = None

class PutVoiceConnectorProxyRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    DefaultSessionExpiryMinutes: int
    PhoneNumberPoolCountries: Sequence[str]
    FallBackPhoneNumber: Optional[str] = None
    Disabled: Optional[bool] = None

class RedactChannelMessageRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: Optional[str] = None

class RedactConversationMessageRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ConversationId: str
    MessageId: str

class RedactRoomMessageRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MessageId: str

class RegenerateSecurityTokenRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BotId: str

class ResetPersonalPINRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str

class RestorePhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str

class RoomRetentionSettingsTypeDef(BaseValidatorModel):
    RetentionDays: Optional[int] = None

class SearchAvailablePhoneNumbersRequestRequestTypeDef(BaseValidatorModel):
    AreaCode: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None
    State: Optional[str] = None
    TollFreePrefix: Optional[str] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SelectedVideoStreamsTypeDef(BaseValidatorModel):
    AttendeeIds: Optional[Sequence[str]] = None
    ExternalUserIds: Optional[Sequence[str]] = None

class SendChannelMessageRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    Content: str
    Type: ChannelMessageTypeType
    Persistence: ChannelMessagePersistenceTypeType
    ClientRequestToken: str
    Metadata: Optional[str] = None
    ChimeBearer: Optional[str] = None

class StopMeetingTranscriptionRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str

class StreamingNotificationTargetTypeDef(BaseValidatorModel):
    NotificationTarget: NotificationTargetType

class TelephonySettingsTypeDef(BaseValidatorModel):
    InboundCalling: bool
    OutboundCalling: bool
    SMS: bool

class UntagAttendeeRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str
    TagKeys: Sequence[str]

class UntagMeetingRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    TagKeys: Sequence[str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateAccountRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: Optional[str] = None
    DefaultLicense: Optional[LicenseType] = None

class UpdateAppInstanceRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    Name: str
    Metadata: Optional[str] = None

class UpdateAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    Name: str
    Metadata: Optional[str] = None

class UpdateBotRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BotId: str
    Disabled: Optional[bool] = None

class UpdateChannelMessageRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    ChimeBearer: Optional[str] = None

class UpdateChannelReadMarkerRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChimeBearer: Optional[str] = None

class UpdateChannelRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    Name: str
    Mode: ChannelModeType
    Metadata: Optional[str] = None
    ChimeBearer: Optional[str] = None

class UpdatePhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None

class UpdatePhoneNumberSettingsRequestRequestTypeDef(BaseValidatorModel):
    CallingName: str

class UpdateProxySessionRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    ProxySessionId: str
    Capabilities: Sequence[CapabilityType]
    ExpiryMinutes: Optional[int] = None

class UpdateRoomMembershipRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MemberId: str
    Role: Optional[RoomMembershipRoleType] = None

class UpdateRoomRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    Name: Optional[str] = None

class UpdateSipMediaApplicationCallRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str
    TransactionId: str
    Arguments: Mapping[str, str]

class UpdateVoiceConnectorRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Name: str
    RequireEncryption: bool

class ValidateE911AddressRequestRequestTypeDef(BaseValidatorModel):
    AwsAccountId: str
    StreetNumber: str
    StreetInfo: str
    City: str
    State: str
    Country: str
    PostalCode: str

class UpdateAccountSettingsRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    AccountSettings: AccountSettingsTypeDef

class AccountTypeDef(BaseValidatorModel):
    AwsAccountId: str
    AccountId: str
    Name: str
    AccountType: Optional[AccountTypeType] = None
    CreatedTimestamp: Optional[datetime] = None
    DefaultLicense: Optional[LicenseType] = None
    SupportedLicenses: Optional[List[LicenseType]] = None
    AccountStatus: Optional[AccountStatusType] = None
    SigninDelegateGroups: Optional[List[SigninDelegateGroupTypeDef]] = None

class AssociateSigninDelegateGroupsWithAccountRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    SigninDelegateGroups: Sequence[SigninDelegateGroupTypeDef]

class UpdateUserRequestItemTypeDef(BaseValidatorModel):
    UserId: str
    LicenseType: Optional[LicenseType] = None
    UserType: Optional[UserTypeType] = None
    AlexaForBusinessMetadata: Optional[AlexaForBusinessMetadataTypeDef] = None

class UpdateUserRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str
    LicenseType: Optional[LicenseType] = None
    UserType: Optional[UserTypeType] = None
    AlexaForBusinessMetadata: Optional[AlexaForBusinessMetadataTypeDef] = None

class UserTypeDef(BaseValidatorModel):
    UserId: str
    AccountId: Optional[str] = None
    PrimaryEmail: Optional[str] = None
    PrimaryProvisionedNumber: Optional[str] = None
    DisplayName: Optional[str] = None
    LicenseType: Optional[LicenseType] = None
    UserType: Optional[UserTypeType] = None
    UserRegistrationStatus: Optional[RegistrationStatusType] = None
    UserInvitationStatus: Optional[InviteStatusType] = None
    RegisteredOn: Optional[datetime] = None
    InvitedOn: Optional[datetime] = None
    AlexaForBusinessMetadata: Optional[AlexaForBusinessMetadataTypeDef] = None
    PersonalPIN: Optional[str] = None

class AppInstanceAdminSummaryTypeDef(BaseValidatorModel):
    Admin: Optional[IdentityTypeDef] = None

class AppInstanceAdminTypeDef(BaseValidatorModel):
    Admin: Optional[IdentityTypeDef] = None
    AppInstanceArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None

class BatchChannelMembershipsTypeDef(BaseValidatorModel):
    InvitedBy: Optional[IdentityTypeDef] = None
    Type: Optional[ChannelMembershipTypeType] = None
    Members: Optional[List[IdentityTypeDef]] = None
    ChannelArn: Optional[str] = None

class ChannelBanSummaryTypeDef(BaseValidatorModel):
    Member: Optional[IdentityTypeDef] = None

class ChannelBanTypeDef(BaseValidatorModel):
    Member: Optional[IdentityTypeDef] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    CreatedBy: Optional[IdentityTypeDef] = None

class ChannelMembershipSummaryTypeDef(BaseValidatorModel):
    Member: Optional[IdentityTypeDef] = None

class ChannelMembershipTypeDef(BaseValidatorModel):
    InvitedBy: Optional[IdentityTypeDef] = None
    Type: Optional[ChannelMembershipTypeType] = None
    Member: Optional[IdentityTypeDef] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class ChannelMessageSummaryTypeDef(BaseValidatorModel):
    MessageId: Optional[str] = None
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    Type: Optional[ChannelMessageTypeType] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    LastEditedTimestamp: Optional[datetime] = None
    Sender: Optional[IdentityTypeDef] = None
    Redacted: Optional[bool] = None

class ChannelMessageTypeDef(BaseValidatorModel):
    ChannelArn: Optional[str] = None
    MessageId: Optional[str] = None
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    Type: Optional[ChannelMessageTypeType] = None
    CreatedTimestamp: Optional[datetime] = None
    LastEditedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    Sender: Optional[IdentityTypeDef] = None
    Redacted: Optional[bool] = None
    Persistence: Optional[ChannelMessagePersistenceTypeType] = None

class ChannelModeratorSummaryTypeDef(BaseValidatorModel):
    Moderator: Optional[IdentityTypeDef] = None

class ChannelModeratorTypeDef(BaseValidatorModel):
    Moderator: Optional[IdentityTypeDef] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    CreatedBy: Optional[IdentityTypeDef] = None

class ChannelTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    ChannelArn: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    CreatedBy: Optional[IdentityTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    LastMessageTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class AppInstanceRetentionSettingsTypeDef(BaseValidatorModel):
    ChannelRetentionSettings: Optional[ChannelRetentionSettingsTypeDef] = None

class PutAppInstanceStreamingConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceStreamingConfigurations: Sequence[AppInstanceStreamingConfigurationTypeDef]

class ArtifactsConfigurationTypeDef(BaseValidatorModel):
    Audio: AudioArtifactsConfigurationTypeDef
    Video: VideoArtifactsConfigurationTypeDef
    Content: ContentArtifactsConfigurationTypeDef

class AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeletePhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdatePhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceAdminResponseTypeDef(BaseValidatorModel):
    AppInstanceAdmin: IdentityTypeDef
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceResponseTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceUserResponseTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelBanResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    Member: IdentityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelMembershipResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    Member: IdentityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelModeratorResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelModerator: IdentityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMeetingDialOutResponseTypeDef(BaseValidatorModel):
    TransactionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppInstanceResponseTypeDef(BaseValidatorModel):
    AppInstance: AppInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppInstanceUserResponseTypeDef(BaseValidatorModel):
    AppInstanceUser: AppInstanceUserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSettingsResponseTypeDef(BaseValidatorModel):
    AccountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppInstanceStreamingConfigurationsResponseTypeDef(BaseValidatorModel):
    AppInstanceStreamingConfigurations: List[AppInstanceStreamingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberSettingsResponseTypeDef(BaseValidatorModel):
    CallingName: str
    CallingNameUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstanceUsersResponseTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceUsers: List[AppInstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstancesResponseTypeDef(BaseValidatorModel):
    AppInstances: List[AppInstanceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorTerminationCredentialsResponseTypeDef(BaseValidatorModel):
    Usernames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppInstanceStreamingConfigurationsResponseTypeDef(BaseValidatorModel):
    AppInstanceStreamingConfigurations: List[AppInstanceStreamingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RedactChannelMessageResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchAvailablePhoneNumbersResponseTypeDef(BaseValidatorModel):
    E164PhoneNumbers: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendChannelMessageResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppInstanceResponseTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppInstanceUserResponseTypeDef(BaseValidatorModel):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelMessageResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelReadMarkerResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAttendeeResponseTypeDef(BaseValidatorModel):
    Attendee: AttendeeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAttendeeResponseTypeDef(BaseValidatorModel):
    Attendee: AttendeeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttendeesResponseTypeDef(BaseValidatorModel):
    Attendees: List[AttendeeTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateAttendeeResponseTypeDef(BaseValidatorModel):
    Attendees: List[AttendeeTypeDef]
    Errors: List[CreateAttendeeErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateRoomMembershipRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MembershipItemList: Sequence[MembershipItemTypeDef]

class BatchCreateRoomMembershipResponseTypeDef(BaseValidatorModel):
    Errors: List[MemberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchSuspendUserResponseTypeDef(BaseValidatorModel):
    UserErrors: List[UserErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUnsuspendUserResponseTypeDef(BaseValidatorModel):
    UserErrors: List[UserErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateUserResponseTypeDef(BaseValidatorModel):
    UserErrors: List[UserErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdatePhoneNumberRequestRequestTypeDef(BaseValidatorModel):
    UpdatePhoneNumberRequestItems: Sequence[UpdatePhoneNumberRequestItemTypeDef]

class CreateBotResponseTypeDef(BaseValidatorModel):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotResponseTypeDef(BaseValidatorModel):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBotsResponseTypeDef(BaseValidatorModel):
    Bots: List[BotTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegenerateSecurityTokenResponseTypeDef(BaseValidatorModel):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBotResponseTypeDef(BaseValidatorModel):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateE911AddressResponseTypeDef(BaseValidatorModel):
    ValidationResult: int
    AddressExternalId: str
    Address: AddressTypeDef
    CandidateAddressList: List[CandidateAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelMembershipForAppInstanceUserSummaryTypeDef(BaseValidatorModel):
    ChannelSummary: Optional[ChannelSummaryTypeDef] = None
    AppInstanceUserMembershipSummary: Optional[AppInstanceUserMembershipSummaryTypeDef] = None

class ChannelModeratedByAppInstanceUserSummaryTypeDef(BaseValidatorModel):
    ChannelSummary: Optional[ChannelSummaryTypeDef] = None

class ListChannelsResponseTypeDef(BaseValidatorModel):
    Channels: List[ChannelSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    ClientRequestToken: str
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateAppInstanceUserRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceUserId: str
    Name: str
    ClientRequestToken: str
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateAttendeeRequestItemTypeDef(BaseValidatorModel):
    ExternalUserId: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateAttendeeRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    ExternalUserId: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateChannelRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    Name: str
    ClientRequestToken: str
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ChimeBearer: Optional[str] = None

class ListAttendeeTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMeetingTagsResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagAttendeeRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    AttendeeId: str
    Tags: Sequence[TagTypeDef]

class TagMeetingRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    Tags: Sequence[TagTypeDef]

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateMeetingRequestRequestTypeDef(BaseValidatorModel):
    ClientRequestToken: str
    ExternalMeetingId: Optional[str] = None
    MeetingHostId: Optional[str] = None
    MediaRegion: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    NotificationsConfiguration: Optional[MeetingNotificationConfigurationTypeDef] = None

class CreateProxySessionRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    ParticipantPhoneNumbers: Sequence[str]
    Capabilities: Sequence[CapabilityType]
    Name: Optional[str] = None
    ExpiryMinutes: Optional[int] = None
    NumberSelectionBehavior: Optional[NumberSelectionBehaviorType] = None
    GeoMatchLevel: Optional[GeoMatchLevelType] = None
    GeoMatchParams: Optional[GeoMatchParamsTypeDef] = None

class CreateRoomResponseTypeDef(BaseValidatorModel):
    Room: RoomTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRoomResponseTypeDef(BaseValidatorModel):
    Room: RoomTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoomsResponseTypeDef(BaseValidatorModel):
    Rooms: List[RoomTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoomResponseTypeDef(BaseValidatorModel):
    Room: RoomTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSipMediaApplicationCallResponseTypeDef(BaseValidatorModel):
    SipMediaApplicationCall: SipMediaApplicationCallTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSipMediaApplicationCallResponseTypeDef(BaseValidatorModel):
    SipMediaApplicationCall: SipMediaApplicationCallTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSipMediaApplicationRequestRequestTypeDef(BaseValidatorModel):
    AwsRegion: str
    Name: str
    Endpoints: Sequence[SipMediaApplicationEndpointTypeDef]

class SipMediaApplicationTypeDef(BaseValidatorModel):
    SipMediaApplicationId: Optional[str] = None
    AwsRegion: Optional[str] = None
    Name: Optional[str] = None
    Endpoints: Optional[List[SipMediaApplicationEndpointTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class UpdateSipMediaApplicationRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str
    Name: Optional[str] = None
    Endpoints: Optional[Sequence[SipMediaApplicationEndpointTypeDef]] = None

class CreateSipRuleRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    TriggerType: SipRuleTriggerTypeType
    TriggerValue: str
    TargetApplications: Sequence[SipRuleTargetApplicationTypeDef]
    Disabled: Optional[bool] = None

class SipRuleTypeDef(BaseValidatorModel):
    SipRuleId: Optional[str] = None
    Name: Optional[str] = None
    Disabled: Optional[bool] = None
    TriggerType: Optional[SipRuleTriggerTypeType] = None
    TriggerValue: Optional[str] = None
    TargetApplications: Optional[List[SipRuleTargetApplicationTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class UpdateSipRuleRequestRequestTypeDef(BaseValidatorModel):
    SipRuleId: str
    Name: str
    Disabled: Optional[bool] = None
    TargetApplications: Optional[Sequence[SipRuleTargetApplicationTypeDef]] = None

class CreateVoiceConnectorGroupRequestRequestTypeDef(BaseValidatorModel):
    Name: str
    VoiceConnectorItems: Optional[Sequence[VoiceConnectorItemTypeDef]] = None

class UpdateVoiceConnectorGroupRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorGroupId: str
    Name: str
    VoiceConnectorItems: Sequence[VoiceConnectorItemTypeDef]

class VoiceConnectorGroupTypeDef(BaseValidatorModel):
    VoiceConnectorGroupId: Optional[str] = None
    Name: Optional[str] = None
    VoiceConnectorItems: Optional[List[VoiceConnectorItemTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    VoiceConnectorGroupArn: Optional[str] = None

class CreateVoiceConnectorResponseTypeDef(BaseValidatorModel):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorResponseTypeDef(BaseValidatorModel):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorsResponseTypeDef(BaseValidatorModel):
    VoiceConnectors: List[VoiceConnectorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVoiceConnectorResponseTypeDef(BaseValidatorModel):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Credentials: Optional[Sequence[CredentialTypeDef]] = None

class EmergencyCallingConfigurationTypeDef(BaseValidatorModel):
    DNIS: Optional[List[DNISEmergencyCallingConfigurationTypeDef]] = None

class TranscriptionConfigurationTypeDef(BaseValidatorModel):
    EngineTranscribeSettings: Optional[EngineTranscribeSettingsTypeDef] = None
    EngineTranscribeMedicalSettings: Optional[EngineTranscribeMedicalSettingsTypeDef] = None

class GetEventsConfigurationResponseTypeDef(BaseValidatorModel):
    EventsConfiguration: EventsConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutEventsConfigurationResponseTypeDef(BaseValidatorModel):
    EventsConfiguration: EventsConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGlobalSettingsResponseTypeDef(BaseValidatorModel):
    BusinessCalling: BusinessCallingSettingsTypeDef
    VoiceConnector: VoiceConnectorSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGlobalSettingsRequestRequestTypeDef(BaseValidatorModel):
    BusinessCalling: Optional[BusinessCallingSettingsTypeDef] = None
    VoiceConnector: Optional[VoiceConnectorSettingsTypeDef] = None

class GetMessagingSessionEndpointResponseTypeDef(BaseValidatorModel):
    Endpoint: MessagingSessionEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipMediaApplicationLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    SipMediaApplicationId: str
    SipMediaApplicationLoggingConfiguration: Optional[       SipMediaApplicationLoggingConfigurationTypeDef     ] = None

class PutSipMediaApplicationLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    LoggingConfiguration: LoggingConfigurationTypeDef

class PutVoiceConnectorLoggingConfigurationResponseTypeDef(BaseValidatorModel):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorProxyResponseTypeDef(BaseValidatorModel):
    Proxy: ProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorProxyResponseTypeDef(BaseValidatorModel):
    Proxy: ProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorTerminationHealthResponseTypeDef(BaseValidatorModel):
    TerminationHealth: TerminationHealthTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorTerminationResponseTypeDef(BaseValidatorModel):
    Termination: TerminationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorTerminationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Termination: TerminationTypeDef

class PutVoiceConnectorTerminationResponseTypeDef(BaseValidatorModel):
    Termination: TerminationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InviteUsersResponseTypeDef(BaseValidatorModel):
    Invites: List[InviteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsRequestListAccountsPaginateTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    UserEmail: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    UserEmail: Optional[str] = None
    UserType: Optional[UserTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListChannelMessagesRequestRequestTypeDef(BaseValidatorModel):
    ChannelArn: str
    SortOrder: Optional[SortOrderType] = None
    NotBefore: Optional[TimestampTypeDef] = None
    NotAfter: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListSupportedPhoneNumberCountriesResponseTypeDef(BaseValidatorModel):
    PhoneNumberCountries: List[PhoneNumberCountryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MeetingTypeDef(BaseValidatorModel):
    MeetingId: Optional[str] = None
    ExternalMeetingId: Optional[str] = None
    MediaPlacement: Optional[MediaPlacementTypeDef] = None
    MediaRegion: Optional[str] = None

class RoomMembershipTypeDef(BaseValidatorModel):
    RoomId: Optional[str] = None
    Member: Optional[MemberTypeDef] = None
    Role: Optional[RoomMembershipRoleType] = None
    InvitedBy: Optional[str] = None
    UpdatedTimestamp: Optional[datetime] = None

class PhoneNumberOrderTypeDef(BaseValidatorModel):
    PhoneNumberOrderId: Optional[str] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    Status: Optional[PhoneNumberOrderStatusType] = None
    OrderedPhoneNumbers: Optional[List[OrderedPhoneNumberTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class OriginationTypeDef(BaseValidatorModel):
    Routes: Optional[List[OriginationRouteTypeDef]] = None
    Disabled: Optional[bool] = None

class ProxySessionTypeDef(BaseValidatorModel):
    VoiceConnectorId: Optional[str] = None
    ProxySessionId: Optional[str] = None
    Name: Optional[str] = None
    Status: Optional[ProxySessionStatusType] = None
    ExpiryMinutes: Optional[int] = None
    Capabilities: Optional[List[CapabilityType]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    EndedTimestamp: Optional[datetime] = None
    Participants: Optional[List[ParticipantTypeDef]] = None
    NumberSelectionBehavior: Optional[NumberSelectionBehaviorType] = None
    GeoMatchLevel: Optional[GeoMatchLevelType] = None
    GeoMatchParams: Optional[GeoMatchParamsTypeDef] = None

class PhoneNumberTypeDef(BaseValidatorModel):
    PhoneNumberId: Optional[str] = None
    E164PhoneNumber: Optional[str] = None
    Country: Optional[str] = None
    Type: Optional[PhoneNumberTypeType] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    Status: Optional[PhoneNumberStatusType] = None
    Capabilities: Optional[PhoneNumberCapabilitiesTypeDef] = None
    Associations: Optional[List[PhoneNumberAssociationTypeDef]] = None
    CallingName: Optional[str] = None
    CallingNameStatus: Optional[CallingNameStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    DeletionTimestamp: Optional[datetime] = None

class RetentionSettingsTypeDef(BaseValidatorModel):
    RoomRetentionSettings: Optional[RoomRetentionSettingsTypeDef] = None
    ConversationRetentionSettings: Optional[ConversationRetentionSettingsTypeDef] = None

class SourceConfigurationTypeDef(BaseValidatorModel):
    SelectedVideoStreams: Optional[SelectedVideoStreamsTypeDef] = None

class StreamingConfigurationTypeDef(BaseValidatorModel):
    DataRetentionInHours: int
    Disabled: Optional[bool] = None
    StreamingNotificationTargets: Optional[List[StreamingNotificationTargetTypeDef]] = None

class UserSettingsTypeDef(BaseValidatorModel):
    Telephony: TelephonySettingsTypeDef

class CreateAccountResponseTypeDef(BaseValidatorModel):
    Account: AccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountResponseTypeDef(BaseValidatorModel):
    Account: AccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsResponseTypeDef(BaseValidatorModel):
    Accounts: List[AccountTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountResponseTypeDef(BaseValidatorModel):
    Account: AccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateUserRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UpdateUserRequestItems: Sequence[UpdateUserRequestItemTypeDef]

class CreateUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersResponseTypeDef(BaseValidatorModel):
    Users: List[UserTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetPersonalPINResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstanceAdminsResponseTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceAdmins: List[AppInstanceAdminSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppInstanceAdminResponseTypeDef(BaseValidatorModel):
    AppInstanceAdmin: AppInstanceAdminTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateChannelMembershipResponseTypeDef(BaseValidatorModel):
    BatchChannelMemberships: BatchChannelMembershipsTypeDef
    Errors: List[BatchCreateChannelMembershipErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelBansResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    NextToken: str
    ChannelBans: List[ChannelBanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelBanResponseTypeDef(BaseValidatorModel):
    ChannelBan: ChannelBanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelMembershipsResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    ChannelMemberships: List[ChannelMembershipSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelMembershipResponseTypeDef(BaseValidatorModel):
    ChannelMembership: ChannelMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelMessagesResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    NextToken: str
    ChannelMessages: List[ChannelMessageSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelMessageResponseTypeDef(BaseValidatorModel):
    ChannelMessage: ChannelMessageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelModeratorsResponseTypeDef(BaseValidatorModel):
    ChannelArn: str
    NextToken: str
    ChannelModerators: List[ChannelModeratorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelModeratorResponseTypeDef(BaseValidatorModel):
    ChannelModerator: ChannelModeratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelResponseTypeDef(BaseValidatorModel):
    Channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppInstanceRetentionSettingsResponseTypeDef(BaseValidatorModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppInstanceRetentionSettingsRequestRequestTypeDef(BaseValidatorModel):
    AppInstanceArn: str
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef

class PutAppInstanceRetentionSettingsResponseTypeDef(BaseValidatorModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelMembershipForAppInstanceUserResponseTypeDef(BaseValidatorModel):
    ChannelMembership: ChannelMembershipForAppInstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelMembershipsForAppInstanceUserResponseTypeDef(BaseValidatorModel):
    ChannelMemberships: List[ChannelMembershipForAppInstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelModeratedByAppInstanceUserResponseTypeDef(BaseValidatorModel):
    Channel: ChannelModeratedByAppInstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsModeratedByAppInstanceUserResponseTypeDef(BaseValidatorModel):
    Channels: List[ChannelModeratedByAppInstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateAttendeeRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    Attendees: Sequence[CreateAttendeeRequestItemTypeDef]

class CreateMeetingWithAttendeesRequestRequestTypeDef(BaseValidatorModel):
    ClientRequestToken: str
    ExternalMeetingId: Optional[str] = None
    MeetingHostId: Optional[str] = None
    MediaRegion: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    NotificationsConfiguration: Optional[MeetingNotificationConfigurationTypeDef] = None
    Attendees: Optional[Sequence[CreateAttendeeRequestItemTypeDef]] = None

class CreateSipMediaApplicationResponseTypeDef(BaseValidatorModel):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipMediaApplicationResponseTypeDef(BaseValidatorModel):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSipMediaApplicationsResponseTypeDef(BaseValidatorModel):
    SipMediaApplications: List[SipMediaApplicationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSipMediaApplicationResponseTypeDef(BaseValidatorModel):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSipRuleResponseTypeDef(BaseValidatorModel):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipRuleResponseTypeDef(BaseValidatorModel):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSipRulesResponseTypeDef(BaseValidatorModel):
    SipRules: List[SipRuleTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSipRuleResponseTypeDef(BaseValidatorModel):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVoiceConnectorGroupResponseTypeDef(BaseValidatorModel):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorGroupResponseTypeDef(BaseValidatorModel):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorGroupsResponseTypeDef(BaseValidatorModel):
    VoiceConnectorGroups: List[VoiceConnectorGroupTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVoiceConnectorGroupResponseTypeDef(BaseValidatorModel):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef(BaseValidatorModel):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    EmergencyCallingConfiguration: EmergencyCallingConfigurationTypeDef

class PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef(BaseValidatorModel):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMeetingTranscriptionRequestRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    TranscriptionConfiguration: TranscriptionConfigurationTypeDef

class CreateMeetingResponseTypeDef(BaseValidatorModel):
    Meeting: MeetingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMeetingWithAttendeesResponseTypeDef(BaseValidatorModel):
    Meeting: MeetingTypeDef
    Attendees: List[AttendeeTypeDef]
    Errors: List[CreateAttendeeErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMeetingResponseTypeDef(BaseValidatorModel):
    Meeting: MeetingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMeetingsResponseTypeDef(BaseValidatorModel):
    Meetings: List[MeetingTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRoomMembershipResponseTypeDef(BaseValidatorModel):
    RoomMembership: RoomMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoomMembershipsResponseTypeDef(BaseValidatorModel):
    RoomMemberships: List[RoomMembershipTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoomMembershipResponseTypeDef(BaseValidatorModel):
    RoomMembership: RoomMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePhoneNumberOrderResponseTypeDef(BaseValidatorModel):
    PhoneNumberOrder: PhoneNumberOrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberOrderResponseTypeDef(BaseValidatorModel):
    PhoneNumberOrder: PhoneNumberOrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumberOrdersResponseTypeDef(BaseValidatorModel):
    PhoneNumberOrders: List[PhoneNumberOrderTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorOriginationResponseTypeDef(BaseValidatorModel):
    Origination: OriginationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorOriginationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    Origination: OriginationTypeDef

class PutVoiceConnectorOriginationResponseTypeDef(BaseValidatorModel):
    Origination: OriginationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProxySessionResponseTypeDef(BaseValidatorModel):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProxySessionResponseTypeDef(BaseValidatorModel):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProxySessionsResponseTypeDef(BaseValidatorModel):
    ProxySessions: List[ProxySessionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProxySessionResponseTypeDef(BaseValidatorModel):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumbersResponseTypeDef(BaseValidatorModel):
    PhoneNumbers: List[PhoneNumberTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestorePhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRetentionSettingsResponseTypeDef(BaseValidatorModel):
    RetentionSettings: RetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutRetentionSettingsRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RetentionSettings: RetentionSettingsTypeDef

class PutRetentionSettingsResponseTypeDef(BaseValidatorModel):
    RetentionSettings: RetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ChimeSdkMeetingConfigurationTypeDef(BaseValidatorModel):
    SourceConfiguration: Optional[SourceConfigurationTypeDef] = None
    ArtifactsConfiguration: Optional[ArtifactsConfigurationTypeDef] = None

class GetVoiceConnectorStreamingConfigurationResponseTypeDef(BaseValidatorModel):
    StreamingConfiguration: StreamingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    VoiceConnectorId: str
    StreamingConfiguration: StreamingConfigurationTypeDef

class PutVoiceConnectorStreamingConfigurationResponseTypeDef(BaseValidatorModel):
    StreamingConfiguration: StreamingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserSettingsResponseTypeDef(BaseValidatorModel):
    UserSettings: UserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserSettingsRequestRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str
    UserSettings: UserSettingsTypeDef

class CreateMediaCapturePipelineRequestRequestTypeDef(BaseValidatorModel):
    SourceType: Literal["ChimeSdkMeeting"]
    SourceArn: str
    SinkType: Literal["S3Bucket"]
    SinkArn: str
    ClientRequestToken: Optional[str] = None
    ChimeSdkMeetingConfiguration: Optional[ChimeSdkMeetingConfigurationTypeDef] = None

class MediaCapturePipelineTypeDef(BaseValidatorModel):
    MediaPipelineId: Optional[str] = None
    SourceType: Optional[Literal["ChimeSdkMeeting"]] = None
    SourceArn: Optional[str] = None
    Status: Optional[MediaPipelineStatusType] = None
    SinkType: Optional[Literal["S3Bucket"]] = None
    SinkArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    ChimeSdkMeetingConfiguration: Optional[ChimeSdkMeetingConfigurationTypeDef] = None

class CreateMediaCapturePipelineResponseTypeDef(BaseValidatorModel):
    MediaCapturePipeline: MediaCapturePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMediaCapturePipelineResponseTypeDef(BaseValidatorModel):
    MediaCapturePipeline: MediaCapturePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMediaCapturePipelinesResponseTypeDef(BaseValidatorModel):
    MediaCapturePipelines: List[MediaCapturePipelineTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

