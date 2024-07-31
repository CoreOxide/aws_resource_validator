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
from aws_resource_validator.pydantic_models.chime_constants import *

class AccountSettingsTypeDef(BaseModel):
    DisableRemoteControl: Optional[bool] = None
    EnableDialOut: Optional[bool] = None

class SigninDelegateGroupTypeDef(BaseModel):
    GroupName: Optional[str] = None

class AddressTypeDef(BaseModel):
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

class AlexaForBusinessMetadataTypeDef(BaseModel):
    IsAlexaForBusinessEnabled: Optional[bool] = None
    AlexaForBusinessRoomArn: Optional[str] = None

class IdentityTypeDef(BaseModel):
    Arn: Optional[str] = None
    Name: Optional[str] = None

class ChannelRetentionSettingsTypeDef(BaseModel):
    RetentionDays: Optional[int] = None

class AppInstanceStreamingConfigurationTypeDef(BaseModel):
    AppInstanceDataType: AppInstanceDataTypeType
    ResourceArn: str

class AppInstanceSummaryTypeDef(BaseModel):
    AppInstanceArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None

class AppInstanceTypeDef(BaseModel):
    AppInstanceArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class AppInstanceUserMembershipSummaryTypeDef(BaseModel):
    Type: Optional[ChannelMembershipTypeType] = None
    ReadMarkerTimestamp: Optional[datetime] = None

class AppInstanceUserSummaryTypeDef(BaseModel):
    AppInstanceUserArn: Optional[str] = None
    Name: Optional[str] = None
    Metadata: Optional[str] = None

class AppInstanceUserTypeDef(BaseModel):
    AppInstanceUserArn: Optional[str] = None
    Name: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    Metadata: Optional[str] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class AudioArtifactsConfigurationTypeDef(BaseModel):
    MuxType: AudioMuxTypeType

class ContentArtifactsConfigurationTypeDef(BaseModel):
    State: ArtifactsStateType
    MuxType: Optional[Literal["ContentOnly"]] = None

class VideoArtifactsConfigurationTypeDef(BaseModel):
    State: ArtifactsStateType
    MuxType: Optional[Literal["VideoOnly"]] = None

class AssociatePhoneNumberWithUserRequestRequestTypeDef(BaseModel):
    AccountId: str
    UserId: str
    E164PhoneNumber: str

class AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef(BaseModel):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: Sequence[str]
    ForceAssociate: Optional[bool] = None

class PhoneNumberErrorTypeDef(BaseModel):
    PhoneNumberId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HostId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int

class AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    E164PhoneNumbers: Sequence[str]
    ForceAssociate: Optional[bool] = None

class AttendeeTypeDef(BaseModel):
    ExternalUserId: Optional[str] = None
    AttendeeId: Optional[str] = None
    JoinToken: Optional[str] = None

class CreateAttendeeErrorTypeDef(BaseModel):
    ExternalUserId: Optional[str] = None
    ErrorCode: Optional[str] = None
    ErrorMessage: Optional[str] = None

class BatchCreateChannelMembershipErrorTypeDef(BaseModel):
    MemberArn: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class BatchCreateChannelMembershipRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArns: Sequence[str]
    Type: Optional[ChannelMembershipTypeType] = None
    ChimeBearer: Optional[str] = None

class MembershipItemTypeDef(BaseModel):
    MemberId: Optional[str] = None
    Role: Optional[RoomMembershipRoleType] = None

class MemberErrorTypeDef(BaseModel):
    MemberId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class BatchDeletePhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberIds: Sequence[str]

class BatchSuspendUserRequestRequestTypeDef(BaseModel):
    AccountId: str
    UserIdList: Sequence[str]

class UserErrorTypeDef(BaseModel):
    UserId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None

class BatchUnsuspendUserRequestRequestTypeDef(BaseModel):
    AccountId: str
    UserIdList: Sequence[str]

class UpdatePhoneNumberRequestItemTypeDef(BaseModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None

class BotTypeDef(BaseModel):
    BotId: Optional[str] = None
    UserId: Optional[str] = None
    DisplayName: Optional[str] = None
    BotType: Optional[Literal["ChatBot"]] = None
    Disabled: Optional[bool] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    BotEmail: Optional[str] = None
    SecurityToken: Optional[str] = None

class BusinessCallingSettingsTypeDef(BaseModel):
    CdrBucket: Optional[str] = None

class CandidateAddressTypeDef(BaseModel):
    streetInfo: Optional[str] = None
    streetNumber: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postalCode: Optional[str] = None
    postalCodePlus4: Optional[str] = None
    country: Optional[str] = None

class ChannelSummaryTypeDef(BaseModel):
    Name: Optional[str] = None
    ChannelArn: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    LastMessageTimestamp: Optional[datetime] = None

class ConversationRetentionSettingsTypeDef(BaseModel):
    RetentionDays: Optional[int] = None

class CreateAccountRequestRequestTypeDef(BaseModel):
    Name: str

class CreateAppInstanceAdminRequestRequestTypeDef(BaseModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class CreateBotRequestRequestTypeDef(BaseModel):
    AccountId: str
    DisplayName: str
    Domain: Optional[str] = None

class CreateChannelBanRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: Optional[str] = None

class CreateChannelMembershipRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    Type: ChannelMembershipTypeType
    ChimeBearer: Optional[str] = None

class CreateChannelModeratorRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: Optional[str] = None

class CreateMeetingDialOutRequestRequestTypeDef(BaseModel):
    MeetingId: str
    FromPhoneNumber: str
    ToPhoneNumber: str
    JoinToken: str

class MeetingNotificationConfigurationTypeDef(BaseModel):
    SnsTopicArn: Optional[str] = None
    SqsQueueArn: Optional[str] = None

class CreatePhoneNumberOrderRequestRequestTypeDef(BaseModel):
    ProductType: PhoneNumberProductTypeType
    E164PhoneNumbers: Sequence[str]

class GeoMatchParamsTypeDef(BaseModel):
    Country: str
    AreaCode: str

class CreateRoomMembershipRequestRequestTypeDef(BaseModel):
    AccountId: str
    RoomId: str
    MemberId: str
    Role: Optional[RoomMembershipRoleType] = None

class CreateRoomRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: str
    ClientRequestToken: Optional[str] = None

class RoomTypeDef(BaseModel):
    RoomId: Optional[str] = None
    Name: Optional[str] = None
    AccountId: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class CreateSipMediaApplicationCallRequestRequestTypeDef(BaseModel):
    FromPhoneNumber: str
    ToPhoneNumber: str
    SipMediaApplicationId: str
    SipHeaders: Optional[Mapping[str, str]] = None

class SipMediaApplicationCallTypeDef(BaseModel):
    TransactionId: Optional[str] = None

class SipMediaApplicationEndpointTypeDef(BaseModel):
    LambdaArn: Optional[str] = None

class SipRuleTargetApplicationTypeDef(BaseModel):
    SipMediaApplicationId: Optional[str] = None
    Priority: Optional[int] = None
    AwsRegion: Optional[str] = None

class CreateUserRequestRequestTypeDef(BaseModel):
    AccountId: str
    Username: Optional[str] = None
    Email: Optional[str] = None
    UserType: Optional[UserTypeType] = None

class VoiceConnectorItemTypeDef(BaseModel):
    VoiceConnectorId: str
    Priority: int

class CreateVoiceConnectorRequestRequestTypeDef(BaseModel):
    Name: str
    RequireEncryption: bool
    AwsRegion: Optional[VoiceConnectorAwsRegionType] = None

class VoiceConnectorTypeDef(BaseModel):
    VoiceConnectorId: Optional[str] = None
    AwsRegion: Optional[VoiceConnectorAwsRegionType] = None
    Name: Optional[str] = None
    OutboundHostName: Optional[str] = None
    RequireEncryption: Optional[bool] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    VoiceConnectorArn: Optional[str] = None

class CredentialTypeDef(BaseModel):
    Username: Optional[str] = None
    Password: Optional[str] = None

class DNISEmergencyCallingConfigurationTypeDef(BaseModel):
    EmergencyPhoneNumber: str
    CallingCountry: str
    TestPhoneNumber: Optional[str] = None

class DeleteAccountRequestRequestTypeDef(BaseModel):
    AccountId: str

class DeleteAppInstanceAdminRequestRequestTypeDef(BaseModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class DeleteAppInstanceRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str

class DeleteAppInstanceStreamingConfigurationsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str

class DeleteAppInstanceUserRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: str

class DeleteAttendeeRequestRequestTypeDef(BaseModel):
    MeetingId: str
    AttendeeId: str

class DeleteChannelBanRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: Optional[str] = None

class DeleteChannelMembershipRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: Optional[str] = None

class DeleteChannelMessageRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: Optional[str] = None

class DeleteChannelModeratorRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: Optional[str] = None

class DeleteChannelRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChimeBearer: Optional[str] = None

class DeleteEventsConfigurationRequestRequestTypeDef(BaseModel):
    AccountId: str
    BotId: str

class DeleteMediaCapturePipelineRequestRequestTypeDef(BaseModel):
    MediaPipelineId: str

class DeleteMeetingRequestRequestTypeDef(BaseModel):
    MeetingId: str

class DeletePhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str

class DeleteProxySessionRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    ProxySessionId: str

class DeleteRoomMembershipRequestRequestTypeDef(BaseModel):
    AccountId: str
    RoomId: str
    MemberId: str

class DeleteRoomRequestRequestTypeDef(BaseModel):
    AccountId: str
    RoomId: str

class DeleteSipMediaApplicationRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str

class DeleteSipRuleRequestRequestTypeDef(BaseModel):
    SipRuleId: str

class DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorGroupRequestRequestTypeDef(BaseModel):
    VoiceConnectorGroupId: str

class DeleteVoiceConnectorOriginationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorProxyRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    Usernames: Sequence[str]

class DeleteVoiceConnectorTerminationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class DescribeAppInstanceAdminRequestRequestTypeDef(BaseModel):
    AppInstanceAdminArn: str
    AppInstanceArn: str

class DescribeAppInstanceRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str

class DescribeAppInstanceUserRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: str

class DescribeChannelBanRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: Optional[str] = None

class DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: Optional[str] = None

class DescribeChannelMembershipRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MemberArn: str
    ChimeBearer: Optional[str] = None

class DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    AppInstanceUserArn: str
    ChimeBearer: Optional[str] = None

class DescribeChannelModeratorRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChannelModeratorArn: str
    ChimeBearer: Optional[str] = None

class DescribeChannelRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChimeBearer: Optional[str] = None

class DisassociatePhoneNumberFromUserRequestRequestTypeDef(BaseModel):
    AccountId: str
    UserId: str

class DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef(BaseModel):
    VoiceConnectorGroupId: str
    E164PhoneNumbers: Sequence[str]

class DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    E164PhoneNumbers: Sequence[str]

class DisassociateSigninDelegateGroupsFromAccountRequestRequestTypeDef(BaseModel):
    AccountId: str
    GroupNames: Sequence[str]

class EngineTranscribeMedicalSettingsTypeDef(BaseModel):
    LanguageCode: Literal["en-US"]
    Specialty: TranscribeMedicalSpecialtyType
    Type: TranscribeMedicalTypeType
    VocabularyName: Optional[str] = None
    Region: Optional[TranscribeMedicalRegionType] = None
    ContentIdentificationType: Optional[Literal["PHI"]] = None

class EngineTranscribeSettingsTypeDef(BaseModel):
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

class EventsConfigurationTypeDef(BaseModel):
    BotId: Optional[str] = None
    OutboundEventsHTTPSEndpoint: Optional[str] = None
    LambdaFunctionArn: Optional[str] = None

class GetAccountRequestRequestTypeDef(BaseModel):
    AccountId: str

class GetAccountSettingsRequestRequestTypeDef(BaseModel):
    AccountId: str

class GetAppInstanceRetentionSettingsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str

class GetAppInstanceStreamingConfigurationsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str

class GetAttendeeRequestRequestTypeDef(BaseModel):
    MeetingId: str
    AttendeeId: str

class GetBotRequestRequestTypeDef(BaseModel):
    AccountId: str
    BotId: str

class GetChannelMessageRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: Optional[str] = None

class GetEventsConfigurationRequestRequestTypeDef(BaseModel):
    AccountId: str
    BotId: str

class VoiceConnectorSettingsTypeDef(BaseModel):
    CdrBucket: Optional[str] = None

class GetMediaCapturePipelineRequestRequestTypeDef(BaseModel):
    MediaPipelineId: str

class GetMeetingRequestRequestTypeDef(BaseModel):
    MeetingId: str

class MessagingSessionEndpointTypeDef(BaseModel):
    Url: Optional[str] = None

class GetPhoneNumberOrderRequestRequestTypeDef(BaseModel):
    PhoneNumberOrderId: str

class GetPhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str

class GetProxySessionRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    ProxySessionId: str

class GetRetentionSettingsRequestRequestTypeDef(BaseModel):
    AccountId: str

class GetRoomRequestRequestTypeDef(BaseModel):
    AccountId: str
    RoomId: str

class GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str

class SipMediaApplicationLoggingConfigurationTypeDef(BaseModel):
    EnableSipMediaApplicationMessageLogs: Optional[bool] = None

class GetSipMediaApplicationRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str

class GetSipRuleRequestRequestTypeDef(BaseModel):
    SipRuleId: str

class GetUserRequestRequestTypeDef(BaseModel):
    AccountId: str
    UserId: str

class GetUserSettingsRequestRequestTypeDef(BaseModel):
    AccountId: str
    UserId: str

class GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class GetVoiceConnectorGroupRequestRequestTypeDef(BaseModel):
    VoiceConnectorGroupId: str

class GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class LoggingConfigurationTypeDef(BaseModel):
    EnableSIPLogs: Optional[bool] = None
    EnableMediaMetricLogs: Optional[bool] = None

class GetVoiceConnectorOriginationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class GetVoiceConnectorProxyRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class ProxyTypeDef(BaseModel):
    DefaultSessionExpiryMinutes: Optional[int] = None
    Disabled: Optional[bool] = None
    FallBackPhoneNumber: Optional[str] = None
    PhoneNumberCountries: Optional[List[str]] = None

class GetVoiceConnectorRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class GetVoiceConnectorTerminationHealthRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class TerminationHealthTypeDef(BaseModel):
    Timestamp: Optional[datetime] = None
    Source: Optional[str] = None

class GetVoiceConnectorTerminationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class TerminationTypeDef(BaseModel):
    CpsLimit: Optional[int] = None
    DefaultPhoneNumber: Optional[str] = None
    CallingRegions: Optional[List[str]] = None
    CidrAllowedList: Optional[List[str]] = None
    Disabled: Optional[bool] = None

class InviteTypeDef(BaseModel):
    InviteId: Optional[str] = None
    Status: Optional[InviteStatusType] = None
    EmailAddress: Optional[str] = None
    EmailStatus: Optional[EmailStatusType] = None

class InviteUsersRequestRequestTypeDef(BaseModel):
    AccountId: str
    UserEmailList: Sequence[str]
    UserType: Optional[UserTypeType] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListAccountsRequestRequestTypeDef(BaseModel):
    Name: Optional[str] = None
    UserEmail: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListAppInstanceAdminsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppInstanceUsersRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAppInstancesRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListAttendeeTagsRequestRequestTypeDef(BaseModel):
    MeetingId: str
    AttendeeId: str

class ListAttendeesRequestRequestTypeDef(BaseModel):
    MeetingId: str
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListBotsRequestRequestTypeDef(BaseModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListChannelBansRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListChannelMembershipsRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    Type: Optional[ChannelMembershipTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListChannelModeratorsRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    Privacy: Optional[ChannelPrivacyType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListMediaCapturePipelinesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMeetingTagsRequestRequestTypeDef(BaseModel):
    MeetingId: str

class ListMeetingsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPhoneNumberOrdersRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListPhoneNumbersRequestRequestTypeDef(BaseModel):
    Status: Optional[PhoneNumberStatusType] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    FilterName: Optional[PhoneNumberAssociationNameType] = None
    FilterValue: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListProxySessionsRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    Status: Optional[ProxySessionStatusType] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListRoomMembershipsRequestRequestTypeDef(BaseModel):
    AccountId: str
    RoomId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListRoomsRequestRequestTypeDef(BaseModel):
    AccountId: str
    MemberId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSipMediaApplicationsRequestRequestTypeDef(BaseModel):
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSipRulesRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListSupportedPhoneNumberCountriesRequestRequestTypeDef(BaseModel):
    ProductType: PhoneNumberProductTypeType

class PhoneNumberCountryTypeDef(BaseModel):
    CountryCode: Optional[str] = None
    SupportedPhoneNumberTypes: Optional[List[PhoneNumberTypeType]] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class ListUsersRequestRequestTypeDef(BaseModel):
    AccountId: str
    UserEmail: Optional[str] = None
    UserType: Optional[UserTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class ListVoiceConnectorGroupsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str

class ListVoiceConnectorsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class LogoutUserRequestRequestTypeDef(BaseModel):
    AccountId: str
    UserId: str

class MediaPlacementTypeDef(BaseModel):
    AudioHostUrl: Optional[str] = None
    AudioFallbackUrl: Optional[str] = None
    ScreenDataUrl: Optional[str] = None
    ScreenSharingUrl: Optional[str] = None
    ScreenViewingUrl: Optional[str] = None
    SignalingUrl: Optional[str] = None
    TurnControlUrl: Optional[str] = None
    EventIngestionUrl: Optional[str] = None

class MemberTypeDef(BaseModel):
    MemberId: Optional[str] = None
    MemberType: Optional[MemberTypeType] = None
    Email: Optional[str] = None
    FullName: Optional[str] = None
    AccountId: Optional[str] = None

class OrderedPhoneNumberTypeDef(BaseModel):
    E164PhoneNumber: Optional[str] = None
    Status: Optional[OrderedPhoneNumberStatusType] = None

class OriginationRouteTypeDef(BaseModel):
    Host: Optional[str] = None
    Port: Optional[int] = None
    Protocol: Optional[OriginationRouteProtocolType] = None
    Priority: Optional[int] = None
    Weight: Optional[int] = None

class ParticipantTypeDef(BaseModel):
    PhoneNumber: Optional[str] = None
    ProxyPhoneNumber: Optional[str] = None

class PhoneNumberAssociationTypeDef(BaseModel):
    Value: Optional[str] = None
    Name: Optional[PhoneNumberAssociationNameType] = None
    AssociatedTimestamp: Optional[datetime] = None

class PhoneNumberCapabilitiesTypeDef(BaseModel):
    InboundCall: Optional[bool] = None
    OutboundCall: Optional[bool] = None
    InboundSMS: Optional[bool] = None
    OutboundSMS: Optional[bool] = None
    InboundMMS: Optional[bool] = None
    OutboundMMS: Optional[bool] = None

class PutEventsConfigurationRequestRequestTypeDef(BaseModel):
    AccountId: str
    BotId: str
    OutboundEventsHTTPSEndpoint: Optional[str] = None
    LambdaFunctionArn: Optional[str] = None

class PutVoiceConnectorProxyRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    DefaultSessionExpiryMinutes: int
    PhoneNumberPoolCountries: Sequence[str]
    FallBackPhoneNumber: Optional[str] = None
    Disabled: Optional[bool] = None

class RedactChannelMessageRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    ChimeBearer: Optional[str] = None

class RedactConversationMessageRequestRequestTypeDef(BaseModel):
    AccountId: str
    ConversationId: str
    MessageId: str

class RedactRoomMessageRequestRequestTypeDef(BaseModel):
    AccountId: str
    RoomId: str
    MessageId: str

class RegenerateSecurityTokenRequestRequestTypeDef(BaseModel):
    AccountId: str
    BotId: str

class ResetPersonalPINRequestRequestTypeDef(BaseModel):
    AccountId: str
    UserId: str

class RestorePhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str

class RoomRetentionSettingsTypeDef(BaseModel):
    RetentionDays: Optional[int] = None

class SearchAvailablePhoneNumbersRequestRequestTypeDef(BaseModel):
    AreaCode: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None
    State: Optional[str] = None
    TollFreePrefix: Optional[str] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None

class SelectedVideoStreamsTypeDef(BaseModel):
    AttendeeIds: Optional[Sequence[str]] = None
    ExternalUserIds: Optional[Sequence[str]] = None

class SendChannelMessageRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    Content: str
    Type: ChannelMessageTypeType
    Persistence: ChannelMessagePersistenceTypeType
    ClientRequestToken: str
    Metadata: Optional[str] = None
    ChimeBearer: Optional[str] = None

class StopMeetingTranscriptionRequestRequestTypeDef(BaseModel):
    MeetingId: str

class StreamingNotificationTargetTypeDef(BaseModel):
    NotificationTarget: NotificationTargetType

class TelephonySettingsTypeDef(BaseModel):
    InboundCalling: bool
    OutboundCalling: bool
    SMS: bool

class UntagAttendeeRequestRequestTypeDef(BaseModel):
    MeetingId: str
    AttendeeId: str
    TagKeys: Sequence[str]

class UntagMeetingRequestRequestTypeDef(BaseModel):
    MeetingId: str
    TagKeys: Sequence[str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateAccountRequestRequestTypeDef(BaseModel):
    AccountId: str
    Name: Optional[str] = None
    DefaultLicense: Optional[LicenseType] = None

class UpdateAppInstanceRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    Name: str
    Metadata: Optional[str] = None

class UpdateAppInstanceUserRequestRequestTypeDef(BaseModel):
    AppInstanceUserArn: str
    Name: str
    Metadata: Optional[str] = None

class UpdateBotRequestRequestTypeDef(BaseModel):
    AccountId: str
    BotId: str
    Disabled: Optional[bool] = None

class UpdateChannelMessageRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    ChimeBearer: Optional[str] = None

class UpdateChannelReadMarkerRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    ChimeBearer: Optional[str] = None

class UpdateChannelRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    Name: str
    Mode: ChannelModeType
    Metadata: Optional[str] = None
    ChimeBearer: Optional[str] = None

class UpdatePhoneNumberRequestRequestTypeDef(BaseModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None

class UpdatePhoneNumberSettingsRequestRequestTypeDef(BaseModel):
    CallingName: str

class UpdateProxySessionRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    ProxySessionId: str
    Capabilities: Sequence[CapabilityType]
    ExpiryMinutes: Optional[int] = None

class UpdateRoomMembershipRequestRequestTypeDef(BaseModel):
    AccountId: str
    RoomId: str
    MemberId: str
    Role: Optional[RoomMembershipRoleType] = None

class UpdateRoomRequestRequestTypeDef(BaseModel):
    AccountId: str
    RoomId: str
    Name: Optional[str] = None

class UpdateSipMediaApplicationCallRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str
    TransactionId: str
    Arguments: Mapping[str, str]

class UpdateVoiceConnectorRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    Name: str
    RequireEncryption: bool

class ValidateE911AddressRequestRequestTypeDef(BaseModel):
    AwsAccountId: str
    StreetNumber: str
    StreetInfo: str
    City: str
    State: str
    Country: str
    PostalCode: str

class UpdateAccountSettingsRequestRequestTypeDef(BaseModel):
    AccountId: str
    AccountSettings: AccountSettingsTypeDef

class AccountTypeDef(BaseModel):
    AwsAccountId: str
    AccountId: str
    Name: str
    AccountType: Optional[AccountTypeType] = None
    CreatedTimestamp: Optional[datetime] = None
    DefaultLicense: Optional[LicenseType] = None
    SupportedLicenses: Optional[List[LicenseType]] = None
    AccountStatus: Optional[AccountStatusType] = None
    SigninDelegateGroups: Optional[List[SigninDelegateGroupTypeDef]] = None

class AssociateSigninDelegateGroupsWithAccountRequestRequestTypeDef(BaseModel):
    AccountId: str
    SigninDelegateGroups: Sequence[SigninDelegateGroupTypeDef]

class UpdateUserRequestItemTypeDef(BaseModel):
    UserId: str
    LicenseType: Optional[LicenseType] = None
    UserType: Optional[UserTypeType] = None
    AlexaForBusinessMetadata: Optional[AlexaForBusinessMetadataTypeDef] = None

class UpdateUserRequestRequestTypeDef(BaseModel):
    AccountId: str
    UserId: str
    LicenseType: Optional[LicenseType] = None
    UserType: Optional[UserTypeType] = None
    AlexaForBusinessMetadata: Optional[AlexaForBusinessMetadataTypeDef] = None

class UserTypeDef(BaseModel):
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

class AppInstanceAdminSummaryTypeDef(BaseModel):
    Admin: Optional[IdentityTypeDef] = None

class AppInstanceAdminTypeDef(BaseModel):
    Admin: Optional[IdentityTypeDef] = None
    AppInstanceArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None

class BatchChannelMembershipsTypeDef(BaseModel):
    InvitedBy: Optional[IdentityTypeDef] = None
    Type: Optional[ChannelMembershipTypeType] = None
    Members: Optional[List[IdentityTypeDef]] = None
    ChannelArn: Optional[str] = None

class ChannelBanSummaryTypeDef(BaseModel):
    Member: Optional[IdentityTypeDef] = None

class ChannelBanTypeDef(BaseModel):
    Member: Optional[IdentityTypeDef] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    CreatedBy: Optional[IdentityTypeDef] = None

class ChannelMembershipSummaryTypeDef(BaseModel):
    Member: Optional[IdentityTypeDef] = None

class ChannelMembershipTypeDef(BaseModel):
    InvitedBy: Optional[IdentityTypeDef] = None
    Type: Optional[ChannelMembershipTypeType] = None
    Member: Optional[IdentityTypeDef] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class ChannelMessageSummaryTypeDef(BaseModel):
    MessageId: Optional[str] = None
    Content: Optional[str] = None
    Metadata: Optional[str] = None
    Type: Optional[ChannelMessageTypeType] = None
    CreatedTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None
    LastEditedTimestamp: Optional[datetime] = None
    Sender: Optional[IdentityTypeDef] = None
    Redacted: Optional[bool] = None

class ChannelMessageTypeDef(BaseModel):
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

class ChannelModeratorSummaryTypeDef(BaseModel):
    Moderator: Optional[IdentityTypeDef] = None

class ChannelModeratorTypeDef(BaseModel):
    Moderator: Optional[IdentityTypeDef] = None
    ChannelArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    CreatedBy: Optional[IdentityTypeDef] = None

class ChannelTypeDef(BaseModel):
    Name: Optional[str] = None
    ChannelArn: Optional[str] = None
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    CreatedBy: Optional[IdentityTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    LastMessageTimestamp: Optional[datetime] = None
    LastUpdatedTimestamp: Optional[datetime] = None

class AppInstanceRetentionSettingsTypeDef(BaseModel):
    ChannelRetentionSettings: Optional[ChannelRetentionSettingsTypeDef] = None

class PutAppInstanceStreamingConfigurationsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    AppInstanceStreamingConfigurations: Sequence[AppInstanceStreamingConfigurationTypeDef]

class ArtifactsConfigurationTypeDef(BaseModel):
    Audio: AudioArtifactsConfigurationTypeDef
    Video: VideoArtifactsConfigurationTypeDef
    Content: ContentArtifactsConfigurationTypeDef

class AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef(BaseModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef(BaseModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchDeletePhoneNumberResponseTypeDef(BaseModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdatePhoneNumberResponseTypeDef(BaseModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceAdminResponseTypeDef(BaseModel):
    AppInstanceAdmin: IdentityTypeDef
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceResponseTypeDef(BaseModel):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceUserResponseTypeDef(BaseModel):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelBanResponseTypeDef(BaseModel):
    ChannelArn: str
    Member: IdentityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelMembershipResponseTypeDef(BaseModel):
    ChannelArn: str
    Member: IdentityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelModeratorResponseTypeDef(BaseModel):
    ChannelArn: str
    ChannelModerator: IdentityTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelResponseTypeDef(BaseModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMeetingDialOutResponseTypeDef(BaseModel):
    TransactionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppInstanceResponseTypeDef(BaseModel):
    AppInstance: AppInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppInstanceUserResponseTypeDef(BaseModel):
    AppInstanceUser: AppInstanceUserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef(BaseModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef(BaseModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountSettingsResponseTypeDef(BaseModel):
    AccountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppInstanceStreamingConfigurationsResponseTypeDef(BaseModel):
    AppInstanceStreamingConfigurations: List[AppInstanceStreamingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberSettingsResponseTypeDef(BaseModel):
    CallingName: str
    CallingNameUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstanceUsersResponseTypeDef(BaseModel):
    AppInstanceArn: str
    AppInstanceUsers: List[AppInstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstancesResponseTypeDef(BaseModel):
    AppInstances: List[AppInstanceSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorTerminationCredentialsResponseTypeDef(BaseModel):
    Usernames: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppInstanceStreamingConfigurationsResponseTypeDef(BaseModel):
    AppInstanceStreamingConfigurations: List[AppInstanceStreamingConfigurationTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class RedactChannelMessageResponseTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class SearchAvailablePhoneNumbersResponseTypeDef(BaseModel):
    E164PhoneNumbers: List[str]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class SendChannelMessageResponseTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppInstanceResponseTypeDef(BaseModel):
    AppInstanceArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAppInstanceUserResponseTypeDef(BaseModel):
    AppInstanceUserArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelMessageResponseTypeDef(BaseModel):
    ChannelArn: str
    MessageId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelReadMarkerResponseTypeDef(BaseModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(BaseModel):
    ChannelArn: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAttendeeResponseTypeDef(BaseModel):
    Attendee: AttendeeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAttendeeResponseTypeDef(BaseModel):
    Attendee: AttendeeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAttendeesResponseTypeDef(BaseModel):
    Attendees: List[AttendeeTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateAttendeeResponseTypeDef(BaseModel):
    Attendees: List[AttendeeTypeDef]
    Errors: List[CreateAttendeeErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateRoomMembershipRequestRequestTypeDef(BaseModel):
    AccountId: str
    RoomId: str
    MembershipItemList: Sequence[MembershipItemTypeDef]

class BatchCreateRoomMembershipResponseTypeDef(BaseModel):
    Errors: List[MemberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchSuspendUserResponseTypeDef(BaseModel):
    UserErrors: List[UserErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUnsuspendUserResponseTypeDef(BaseModel):
    UserErrors: List[UserErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateUserResponseTypeDef(BaseModel):
    UserErrors: List[UserErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdatePhoneNumberRequestRequestTypeDef(BaseModel):
    UpdatePhoneNumberRequestItems: Sequence[UpdatePhoneNumberRequestItemTypeDef]

class CreateBotResponseTypeDef(BaseModel):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetBotResponseTypeDef(BaseModel):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListBotsResponseTypeDef(BaseModel):
    Bots: List[BotTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RegenerateSecurityTokenResponseTypeDef(BaseModel):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBotResponseTypeDef(BaseModel):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ValidateE911AddressResponseTypeDef(BaseModel):
    ValidationResult: int
    AddressExternalId: str
    Address: AddressTypeDef
    CandidateAddressList: List[CandidateAddressTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelMembershipForAppInstanceUserSummaryTypeDef(BaseModel):
    ChannelSummary: Optional[ChannelSummaryTypeDef] = None
    AppInstanceUserMembershipSummary: Optional[AppInstanceUserMembershipSummaryTypeDef] = None

class ChannelModeratedByAppInstanceUserSummaryTypeDef(BaseModel):
    ChannelSummary: Optional[ChannelSummaryTypeDef] = None

class ListChannelsResponseTypeDef(BaseModel):
    Channels: List[ChannelSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAppInstanceRequestRequestTypeDef(BaseModel):
    Name: str
    ClientRequestToken: str
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateAppInstanceUserRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    AppInstanceUserId: str
    Name: str
    ClientRequestToken: str
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateAttendeeRequestItemTypeDef(BaseModel):
    ExternalUserId: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateAttendeeRequestRequestTypeDef(BaseModel):
    MeetingId: str
    ExternalUserId: str
    Tags: Optional[Sequence[TagTypeDef]] = None

class CreateChannelRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    Name: str
    ClientRequestToken: str
    Mode: Optional[ChannelModeType] = None
    Privacy: Optional[ChannelPrivacyType] = None
    Metadata: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ChimeBearer: Optional[str] = None

class ListAttendeeTagsResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListMeetingTagsResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagAttendeeRequestRequestTypeDef(BaseModel):
    MeetingId: str
    AttendeeId: str
    Tags: Sequence[TagTypeDef]

class TagMeetingRequestRequestTypeDef(BaseModel):
    MeetingId: str
    Tags: Sequence[TagTypeDef]

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateMeetingRequestRequestTypeDef(BaseModel):
    ClientRequestToken: str
    ExternalMeetingId: Optional[str] = None
    MeetingHostId: Optional[str] = None
    MediaRegion: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    NotificationsConfiguration: Optional[MeetingNotificationConfigurationTypeDef] = None

class CreateProxySessionRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    ParticipantPhoneNumbers: Sequence[str]
    Capabilities: Sequence[CapabilityType]
    Name: Optional[str] = None
    ExpiryMinutes: Optional[int] = None
    NumberSelectionBehavior: Optional[NumberSelectionBehaviorType] = None
    GeoMatchLevel: Optional[GeoMatchLevelType] = None
    GeoMatchParams: Optional[GeoMatchParamsTypeDef] = None

class CreateRoomResponseTypeDef(BaseModel):
    Room: RoomTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRoomResponseTypeDef(BaseModel):
    Room: RoomTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoomsResponseTypeDef(BaseModel):
    Rooms: List[RoomTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoomResponseTypeDef(BaseModel):
    Room: RoomTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSipMediaApplicationCallResponseTypeDef(BaseModel):
    SipMediaApplicationCall: SipMediaApplicationCallTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSipMediaApplicationCallResponseTypeDef(BaseModel):
    SipMediaApplicationCall: SipMediaApplicationCallTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSipMediaApplicationRequestRequestTypeDef(BaseModel):
    AwsRegion: str
    Name: str
    Endpoints: Sequence[SipMediaApplicationEndpointTypeDef]

class SipMediaApplicationTypeDef(BaseModel):
    SipMediaApplicationId: Optional[str] = None
    AwsRegion: Optional[str] = None
    Name: Optional[str] = None
    Endpoints: Optional[List[SipMediaApplicationEndpointTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class UpdateSipMediaApplicationRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str
    Name: Optional[str] = None
    Endpoints: Optional[Sequence[SipMediaApplicationEndpointTypeDef]] = None

class CreateSipRuleRequestRequestTypeDef(BaseModel):
    Name: str
    TriggerType: SipRuleTriggerTypeType
    TriggerValue: str
    TargetApplications: Sequence[SipRuleTargetApplicationTypeDef]
    Disabled: Optional[bool] = None

class SipRuleTypeDef(BaseModel):
    SipRuleId: Optional[str] = None
    Name: Optional[str] = None
    Disabled: Optional[bool] = None
    TriggerType: Optional[SipRuleTriggerTypeType] = None
    TriggerValue: Optional[str] = None
    TargetApplications: Optional[List[SipRuleTargetApplicationTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class UpdateSipRuleRequestRequestTypeDef(BaseModel):
    SipRuleId: str
    Name: str
    Disabled: Optional[bool] = None
    TargetApplications: Optional[Sequence[SipRuleTargetApplicationTypeDef]] = None

class CreateVoiceConnectorGroupRequestRequestTypeDef(BaseModel):
    Name: str
    VoiceConnectorItems: Optional[Sequence[VoiceConnectorItemTypeDef]] = None

class UpdateVoiceConnectorGroupRequestRequestTypeDef(BaseModel):
    VoiceConnectorGroupId: str
    Name: str
    VoiceConnectorItems: Sequence[VoiceConnectorItemTypeDef]

class VoiceConnectorGroupTypeDef(BaseModel):
    VoiceConnectorGroupId: Optional[str] = None
    Name: Optional[str] = None
    VoiceConnectorItems: Optional[List[VoiceConnectorItemTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    VoiceConnectorGroupArn: Optional[str] = None

class CreateVoiceConnectorResponseTypeDef(BaseModel):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorResponseTypeDef(BaseModel):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorsResponseTypeDef(BaseModel):
    VoiceConnectors: List[VoiceConnectorTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVoiceConnectorResponseTypeDef(BaseModel):
    VoiceConnector: VoiceConnectorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    Credentials: Optional[Sequence[CredentialTypeDef]] = None

class EmergencyCallingConfigurationTypeDef(BaseModel):
    DNIS: Optional[List[DNISEmergencyCallingConfigurationTypeDef]] = None

class TranscriptionConfigurationTypeDef(BaseModel):
    EngineTranscribeSettings: Optional[EngineTranscribeSettingsTypeDef] = None
    EngineTranscribeMedicalSettings: Optional[EngineTranscribeMedicalSettingsTypeDef] = None

class GetEventsConfigurationResponseTypeDef(BaseModel):
    EventsConfiguration: EventsConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutEventsConfigurationResponseTypeDef(BaseModel):
    EventsConfiguration: EventsConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetGlobalSettingsResponseTypeDef(BaseModel):
    BusinessCalling: BusinessCallingSettingsTypeDef
    VoiceConnector: VoiceConnectorSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGlobalSettingsRequestRequestTypeDef(BaseModel):
    BusinessCalling: Optional[BusinessCallingSettingsTypeDef] = None
    VoiceConnector: Optional[VoiceConnectorSettingsTypeDef] = None

class GetMessagingSessionEndpointResponseTypeDef(BaseModel):
    Endpoint: MessagingSessionEndpointTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipMediaApplicationLoggingConfigurationResponseTypeDef(BaseModel):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef(BaseModel):
    SipMediaApplicationId: str
    SipMediaApplicationLoggingConfiguration: Optional[       SipMediaApplicationLoggingConfigurationTypeDef     ] = None

class PutSipMediaApplicationLoggingConfigurationResponseTypeDef(BaseModel):
    SipMediaApplicationLoggingConfiguration: SipMediaApplicationLoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorLoggingConfigurationResponseTypeDef(BaseModel):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    LoggingConfiguration: LoggingConfigurationTypeDef

class PutVoiceConnectorLoggingConfigurationResponseTypeDef(BaseModel):
    LoggingConfiguration: LoggingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorProxyResponseTypeDef(BaseModel):
    Proxy: ProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorProxyResponseTypeDef(BaseModel):
    Proxy: ProxyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorTerminationHealthResponseTypeDef(BaseModel):
    TerminationHealth: TerminationHealthTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorTerminationResponseTypeDef(BaseModel):
    Termination: TerminationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorTerminationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    Termination: TerminationTypeDef

class PutVoiceConnectorTerminationResponseTypeDef(BaseModel):
    Termination: TerminationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class InviteUsersResponseTypeDef(BaseModel):
    Invites: List[InviteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsRequestListAccountsPaginateTypeDef(BaseModel):
    Name: Optional[str] = None
    UserEmail: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListUsersRequestListUsersPaginateTypeDef(BaseModel):
    AccountId: str
    UserEmail: Optional[str] = None
    UserType: Optional[UserTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListChannelMessagesRequestRequestTypeDef(BaseModel):
    ChannelArn: str
    SortOrder: Optional[SortOrderType] = None
    NotBefore: Optional[TimestampTypeDef] = None
    NotAfter: Optional[TimestampTypeDef] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None
    ChimeBearer: Optional[str] = None

class ListSupportedPhoneNumberCountriesResponseTypeDef(BaseModel):
    PhoneNumberCountries: List[PhoneNumberCountryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class MeetingTypeDef(BaseModel):
    MeetingId: Optional[str] = None
    ExternalMeetingId: Optional[str] = None
    MediaPlacement: Optional[MediaPlacementTypeDef] = None
    MediaRegion: Optional[str] = None

class RoomMembershipTypeDef(BaseModel):
    RoomId: Optional[str] = None
    Member: Optional[MemberTypeDef] = None
    Role: Optional[RoomMembershipRoleType] = None
    InvitedBy: Optional[str] = None
    UpdatedTimestamp: Optional[datetime] = None

class PhoneNumberOrderTypeDef(BaseModel):
    PhoneNumberOrderId: Optional[str] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    Status: Optional[PhoneNumberOrderStatusType] = None
    OrderedPhoneNumbers: Optional[List[OrderedPhoneNumberTypeDef]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class OriginationTypeDef(BaseModel):
    Routes: Optional[List[OriginationRouteTypeDef]] = None
    Disabled: Optional[bool] = None

class ProxySessionTypeDef(BaseModel):
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

class PhoneNumberTypeDef(BaseModel):
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

class RetentionSettingsTypeDef(BaseModel):
    RoomRetentionSettings: Optional[RoomRetentionSettingsTypeDef] = None
    ConversationRetentionSettings: Optional[ConversationRetentionSettingsTypeDef] = None

class SourceConfigurationTypeDef(BaseModel):
    SelectedVideoStreams: Optional[SelectedVideoStreamsTypeDef] = None

class StreamingConfigurationTypeDef(BaseModel):
    DataRetentionInHours: int
    Disabled: Optional[bool] = None
    StreamingNotificationTargets: Optional[List[StreamingNotificationTargetTypeDef]] = None

class UserSettingsTypeDef(BaseModel):
    Telephony: TelephonySettingsTypeDef

class CreateAccountResponseTypeDef(BaseModel):
    Account: AccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAccountResponseTypeDef(BaseModel):
    Account: AccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAccountsResponseTypeDef(BaseModel):
    Accounts: List[AccountTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAccountResponseTypeDef(BaseModel):
    Account: AccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchUpdateUserRequestRequestTypeDef(BaseModel):
    AccountId: str
    UpdateUserRequestItems: Sequence[UpdateUserRequestItemTypeDef]

class CreateUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListUsersResponseTypeDef(BaseModel):
    Users: List[UserTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetPersonalPINResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserResponseTypeDef(BaseModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListAppInstanceAdminsResponseTypeDef(BaseModel):
    AppInstanceArn: str
    AppInstanceAdmins: List[AppInstanceAdminSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAppInstanceAdminResponseTypeDef(BaseModel):
    AppInstanceAdmin: AppInstanceAdminTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateChannelMembershipResponseTypeDef(BaseModel):
    BatchChannelMemberships: BatchChannelMembershipsTypeDef
    Errors: List[BatchCreateChannelMembershipErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelBansResponseTypeDef(BaseModel):
    ChannelArn: str
    NextToken: str
    ChannelBans: List[ChannelBanSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelBanResponseTypeDef(BaseModel):
    ChannelBan: ChannelBanTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelMembershipsResponseTypeDef(BaseModel):
    ChannelArn: str
    ChannelMemberships: List[ChannelMembershipSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelMembershipResponseTypeDef(BaseModel):
    ChannelMembership: ChannelMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelMessagesResponseTypeDef(BaseModel):
    ChannelArn: str
    NextToken: str
    ChannelMessages: List[ChannelMessageSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelMessageResponseTypeDef(BaseModel):
    ChannelMessage: ChannelMessageTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelModeratorsResponseTypeDef(BaseModel):
    ChannelArn: str
    NextToken: str
    ChannelModerators: List[ChannelModeratorSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelModeratorResponseTypeDef(BaseModel):
    ChannelModerator: ChannelModeratorTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelResponseTypeDef(BaseModel):
    Channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetAppInstanceRetentionSettingsResponseTypeDef(BaseModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutAppInstanceRetentionSettingsRequestRequestTypeDef(BaseModel):
    AppInstanceArn: str
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef

class PutAppInstanceRetentionSettingsResponseTypeDef(BaseModel):
    AppInstanceRetentionSettings: AppInstanceRetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelMembershipForAppInstanceUserResponseTypeDef(BaseModel):
    ChannelMembership: ChannelMembershipForAppInstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelMembershipsForAppInstanceUserResponseTypeDef(BaseModel):
    ChannelMemberships: List[ChannelMembershipForAppInstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeChannelModeratedByAppInstanceUserResponseTypeDef(BaseModel):
    Channel: ChannelModeratedByAppInstanceUserSummaryTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListChannelsModeratedByAppInstanceUserResponseTypeDef(BaseModel):
    Channels: List[ChannelModeratedByAppInstanceUserSummaryTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class BatchCreateAttendeeRequestRequestTypeDef(BaseModel):
    MeetingId: str
    Attendees: Sequence[CreateAttendeeRequestItemTypeDef]

class CreateMeetingWithAttendeesRequestRequestTypeDef(BaseModel):
    ClientRequestToken: str
    ExternalMeetingId: Optional[str] = None
    MeetingHostId: Optional[str] = None
    MediaRegion: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    NotificationsConfiguration: Optional[MeetingNotificationConfigurationTypeDef] = None
    Attendees: Optional[Sequence[CreateAttendeeRequestItemTypeDef]] = None

class CreateSipMediaApplicationResponseTypeDef(BaseModel):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipMediaApplicationResponseTypeDef(BaseModel):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSipMediaApplicationsResponseTypeDef(BaseModel):
    SipMediaApplications: List[SipMediaApplicationTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSipMediaApplicationResponseTypeDef(BaseModel):
    SipMediaApplication: SipMediaApplicationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSipRuleResponseTypeDef(BaseModel):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetSipRuleResponseTypeDef(BaseModel):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListSipRulesResponseTypeDef(BaseModel):
    SipRules: List[SipRuleTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSipRuleResponseTypeDef(BaseModel):
    SipRule: SipRuleTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateVoiceConnectorGroupResponseTypeDef(BaseModel):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorGroupResponseTypeDef(BaseModel):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListVoiceConnectorGroupsResponseTypeDef(BaseModel):
    VoiceConnectorGroups: List[VoiceConnectorGroupTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVoiceConnectorGroupResponseTypeDef(BaseModel):
    VoiceConnectorGroup: VoiceConnectorGroupTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef(BaseModel):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    EmergencyCallingConfiguration: EmergencyCallingConfigurationTypeDef

class PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef(BaseModel):
    EmergencyCallingConfiguration: EmergencyCallingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartMeetingTranscriptionRequestRequestTypeDef(BaseModel):
    MeetingId: str
    TranscriptionConfiguration: TranscriptionConfigurationTypeDef

class CreateMeetingResponseTypeDef(BaseModel):
    Meeting: MeetingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMeetingWithAttendeesResponseTypeDef(BaseModel):
    Meeting: MeetingTypeDef
    Attendees: List[AttendeeTypeDef]
    Errors: List[CreateAttendeeErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class GetMeetingResponseTypeDef(BaseModel):
    Meeting: MeetingTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMeetingsResponseTypeDef(BaseModel):
    Meetings: List[MeetingTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRoomMembershipResponseTypeDef(BaseModel):
    RoomMembership: RoomMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListRoomMembershipsResponseTypeDef(BaseModel):
    RoomMemberships: List[RoomMembershipTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateRoomMembershipResponseTypeDef(BaseModel):
    RoomMembership: RoomMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreatePhoneNumberOrderResponseTypeDef(BaseModel):
    PhoneNumberOrder: PhoneNumberOrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberOrderResponseTypeDef(BaseModel):
    PhoneNumberOrder: PhoneNumberOrderTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumberOrdersResponseTypeDef(BaseModel):
    PhoneNumberOrders: List[PhoneNumberOrderTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceConnectorOriginationResponseTypeDef(BaseModel):
    Origination: OriginationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorOriginationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    Origination: OriginationTypeDef

class PutVoiceConnectorOriginationResponseTypeDef(BaseModel):
    Origination: OriginationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateProxySessionResponseTypeDef(BaseModel):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetProxySessionResponseTypeDef(BaseModel):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListProxySessionsResponseTypeDef(BaseModel):
    ProxySessions: List[ProxySessionTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateProxySessionResponseTypeDef(BaseModel):
    ProxySession: ProxySessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPhoneNumberResponseTypeDef(BaseModel):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListPhoneNumbersResponseTypeDef(BaseModel):
    PhoneNumbers: List[PhoneNumberTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class RestorePhoneNumberResponseTypeDef(BaseModel):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePhoneNumberResponseTypeDef(BaseModel):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRetentionSettingsResponseTypeDef(BaseModel):
    RetentionSettings: RetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class PutRetentionSettingsRequestRequestTypeDef(BaseModel):
    AccountId: str
    RetentionSettings: RetentionSettingsTypeDef

class PutRetentionSettingsResponseTypeDef(BaseModel):
    RetentionSettings: RetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class ChimeSdkMeetingConfigurationTypeDef(BaseModel):
    SourceConfiguration: Optional[SourceConfigurationTypeDef] = None
    ArtifactsConfiguration: Optional[ArtifactsConfigurationTypeDef] = None

class GetVoiceConnectorStreamingConfigurationResponseTypeDef(BaseModel):
    StreamingConfiguration: StreamingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef(BaseModel):
    VoiceConnectorId: str
    StreamingConfiguration: StreamingConfigurationTypeDef

class PutVoiceConnectorStreamingConfigurationResponseTypeDef(BaseModel):
    StreamingConfiguration: StreamingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetUserSettingsResponseTypeDef(BaseModel):
    UserSettings: UserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateUserSettingsRequestRequestTypeDef(BaseModel):
    AccountId: str
    UserId: str
    UserSettings: UserSettingsTypeDef

class CreateMediaCapturePipelineRequestRequestTypeDef(BaseModel):
    SourceType: Literal["ChimeSdkMeeting"]
    SourceArn: str
    SinkType: Literal["S3Bucket"]
    SinkArn: str
    ClientRequestToken: Optional[str] = None
    ChimeSdkMeetingConfiguration: Optional[ChimeSdkMeetingConfigurationTypeDef] = None

class MediaCapturePipelineTypeDef(BaseModel):
    MediaPipelineId: Optional[str] = None
    SourceType: Optional[Literal["ChimeSdkMeeting"]] = None
    SourceArn: Optional[str] = None
    Status: Optional[MediaPipelineStatusType] = None
    SinkType: Optional[Literal["S3Bucket"]] = None
    SinkArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    ChimeSdkMeetingConfiguration: Optional[ChimeSdkMeetingConfigurationTypeDef] = None

class CreateMediaCapturePipelineResponseTypeDef(BaseModel):
    MediaCapturePipeline: MediaCapturePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMediaCapturePipelineResponseTypeDef(BaseModel):
    MediaCapturePipeline: MediaCapturePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListMediaCapturePipelinesResponseTypeDef(BaseModel):
    MediaCapturePipelines: List[MediaCapturePipelineTypeDef]
    NextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

