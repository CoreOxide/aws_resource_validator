from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.chime.chime_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AccountSettings(BaseValidatorModel):
    DisableRemoteControl: Optional[bool] = None
    EnableDialOut: Optional[bool] = None


class SigninDelegateGroup(BaseValidatorModel):
    GroupName: Optional[str] = None


class AlexaForBusinessMetadata(BaseValidatorModel):
    IsAlexaForBusinessEnabled: Optional[bool] = None
    AlexaForBusinessRoomArn: Optional[str] = None


class AssociatePhoneNumberWithUserRequest(BaseValidatorModel):
    AccountId: str
    UserId: str
    E164PhoneNumber: str


class MembershipItem(BaseValidatorModel):
    MemberId: Optional[str] = None
    Role: Optional[RoomMembershipRoleType] = None


class MemberError(BaseValidatorModel):
    MemberId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDeletePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberIds: List[str]


class PhoneNumberError(BaseValidatorModel):
    PhoneNumberId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class BatchSuspendUserRequest(BaseValidatorModel):
    AccountId: str
    UserIdList: List[str]


class UserError(BaseValidatorModel):
    UserId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class BatchUnsuspendUserRequest(BaseValidatorModel):
    AccountId: str
    UserIdList: List[str]


class UpdatePhoneNumberRequestItem(BaseValidatorModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None


class Bot(BaseValidatorModel):
    BotId: Optional[str] = None
    UserId: Optional[str] = None
    DisplayName: Optional[str] = None
    BotType: Optional[Literal['ChatBot']] = None
    Disabled: Optional[bool] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    BotEmail: Optional[str] = None
    SecurityToken: Optional[str] = None


class BusinessCallingSettings(BaseValidatorModel):
    CdrBucket: Optional[str] = None


class ConversationRetentionSettings(BaseValidatorModel):
    RetentionDays: Optional[int] = None


class CreateAccountRequest(BaseValidatorModel):
    Name: str


class CreateBotRequest(BaseValidatorModel):
    AccountId: str
    DisplayName: str
    Domain: Optional[str] = None


class CreateMeetingDialOutRequest(BaseValidatorModel):
    MeetingId: str
    FromPhoneNumber: str
    ToPhoneNumber: str
    JoinToken: str


class CreatePhoneNumberOrderRequest(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType
    E164PhoneNumbers: List[str]


class CreateRoomMembershipRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MemberId: str
    Role: Optional[RoomMembershipRoleType] = None


class CreateRoomRequest(BaseValidatorModel):
    AccountId: str
    Name: str
    ClientRequestToken: Optional[str] = None


class Room(BaseValidatorModel):
    RoomId: Optional[str] = None
    Name: Optional[str] = None
    AccountId: Optional[str] = None
    CreatedBy: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class CreateUserRequest(BaseValidatorModel):
    AccountId: str
    Username: Optional[str] = None
    Email: Optional[str] = None
    UserType: Optional[UserTypeType] = None


class DeleteAccountRequest(BaseValidatorModel):
    AccountId: str


class DeleteEventsConfigurationRequest(BaseValidatorModel):
    AccountId: str
    BotId: str


class DeletePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


class DeleteRoomMembershipRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MemberId: str


class DeleteRoomRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str


class DisassociatePhoneNumberFromUserRequest(BaseValidatorModel):
    AccountId: str
    UserId: str


class DisassociateSigninDelegateGroupsFromAccountRequest(BaseValidatorModel):
    AccountId: str
    GroupNames: List[str]


class EventsConfiguration(BaseValidatorModel):
    BotId: Optional[str] = None
    OutboundEventsHTTPSEndpoint: Optional[str] = None
    LambdaFunctionArn: Optional[str] = None


class GetAccountRequest(BaseValidatorModel):
    AccountId: str


class GetAccountSettingsRequest(BaseValidatorModel):
    AccountId: str


class GetBotRequest(BaseValidatorModel):
    AccountId: str
    BotId: str


class GetEventsConfigurationRequest(BaseValidatorModel):
    AccountId: str
    BotId: str


class VoiceConnectorSettings(BaseValidatorModel):
    CdrBucket: Optional[str] = None


class GetPhoneNumberOrderRequest(BaseValidatorModel):
    PhoneNumberOrderId: str


class GetPhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


class GetRetentionSettingsRequest(BaseValidatorModel):
    AccountId: str


class GetRoomRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str


class GetUserRequest(BaseValidatorModel):
    AccountId: str
    UserId: str


class GetUserSettingsRequest(BaseValidatorModel):
    AccountId: str
    UserId: str


class Invite(BaseValidatorModel):
    InviteId: Optional[str] = None
    Status: Optional[InviteStatusType] = None
    EmailAddress: Optional[str] = None
    EmailStatus: Optional[EmailStatusType] = None


class InviteUsersRequest(BaseValidatorModel):
    AccountId: str
    UserEmailList: List[str]
    UserType: Optional[UserTypeType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccountsRequest(BaseValidatorModel):
    Name: Optional[str] = None
    UserEmail: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListBotsRequest(BaseValidatorModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPhoneNumberOrdersRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPhoneNumbersRequest(BaseValidatorModel):
    Status: Optional[PhoneNumberStatusType] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    FilterName: Optional[PhoneNumberAssociationNameType] = None
    FilterValue: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRoomMembershipsRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRoomsRequest(BaseValidatorModel):
    AccountId: str
    MemberId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSupportedPhoneNumberCountriesRequest(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType


class PhoneNumberCountry(BaseValidatorModel):
    CountryCode: Optional[str] = None
    SupportedPhoneNumberTypes: Optional[List[PhoneNumberTypeType]] = None


class ListUsersRequest(BaseValidatorModel):
    AccountId: str
    UserEmail: Optional[str] = None
    UserType: Optional[UserTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LogoutUserRequest(BaseValidatorModel):
    AccountId: str
    UserId: str


class Member(BaseValidatorModel):
    MemberId: Optional[str] = None
    MemberType: Optional[MemberTypeType] = None
    Email: Optional[str] = None
    FullName: Optional[str] = None
    AccountId: Optional[str] = None


class OrderedPhoneNumber(BaseValidatorModel):
    E164PhoneNumber: Optional[str] = None
    Status: Optional[OrderedPhoneNumberStatusType] = None


class PhoneNumberAssociation(BaseValidatorModel):
    Value: Optional[str] = None
    Name: Optional[PhoneNumberAssociationNameType] = None
    AssociatedTimestamp: Optional[datetime] = None


class PhoneNumberCapabilities(BaseValidatorModel):
    InboundCall: Optional[bool] = None
    OutboundCall: Optional[bool] = None
    InboundSMS: Optional[bool] = None
    OutboundSMS: Optional[bool] = None
    InboundMMS: Optional[bool] = None
    OutboundMMS: Optional[bool] = None


class PutEventsConfigurationRequest(BaseValidatorModel):
    AccountId: str
    BotId: str
    OutboundEventsHTTPSEndpoint: Optional[str] = None
    LambdaFunctionArn: Optional[str] = None


class RedactConversationMessageRequest(BaseValidatorModel):
    AccountId: str
    ConversationId: str
    MessageId: str


class RedactRoomMessageRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MessageId: str


class RegenerateSecurityTokenRequest(BaseValidatorModel):
    AccountId: str
    BotId: str


class ResetPersonalPINRequest(BaseValidatorModel):
    AccountId: str
    UserId: str


class RestorePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


class RoomRetentionSettings(BaseValidatorModel):
    RetentionDays: Optional[int] = None


class SearchAvailablePhoneNumbersRequest(BaseValidatorModel):
    AreaCode: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None
    State: Optional[str] = None
    TollFreePrefix: Optional[str] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TelephonySettings(BaseValidatorModel):
    InboundCalling: bool
    OutboundCalling: bool
    SMS: bool


class UpdateAccountRequest(BaseValidatorModel):
    AccountId: str
    Name: Optional[str] = None
    DefaultLicense: Optional[LicenseType] = None


class UpdateBotRequest(BaseValidatorModel):
    AccountId: str
    BotId: str
    Disabled: Optional[bool] = None


class UpdatePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None


class UpdatePhoneNumberSettingsRequest(BaseValidatorModel):
    CallingName: str


class UpdateRoomMembershipRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MemberId: str
    Role: Optional[RoomMembershipRoleType] = None


class UpdateRoomRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str
    Name: Optional[str] = None


class UpdateAccountSettingsRequest(BaseValidatorModel):
    AccountId: str
    AccountSettings: AccountSettings


class Account(BaseValidatorModel):
    AwsAccountId: str
    AccountId: str
    Name: str
    AccountType: Optional[AccountTypeType] = None
    CreatedTimestamp: Optional[datetime] = None
    DefaultLicense: Optional[LicenseType] = None
    SupportedLicenses: Optional[List[LicenseType]] = None
    AccountStatus: Optional[AccountStatusType] = None
    SigninDelegateGroups: Optional[List[SigninDelegateGroup]] = None


class AssociateSigninDelegateGroupsWithAccountRequest(BaseValidatorModel):
    AccountId: str
    SigninDelegateGroups: List[SigninDelegateGroup]


class UpdateUserRequestItem(BaseValidatorModel):
    UserId: str
    LicenseType: Optional[LicenseType] = None
    UserType: Optional[UserTypeType] = None
    AlexaForBusinessMetadata: Optional[AlexaForBusinessMetadata] = None


class UpdateUserRequest(BaseValidatorModel):
    AccountId: str
    UserId: str
    LicenseType: Optional[LicenseType] = None
    UserType: Optional[UserTypeType] = None
    AlexaForBusinessMetadata: Optional[AlexaForBusinessMetadata] = None


class User(BaseValidatorModel):
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
    AlexaForBusinessMetadata: Optional[AlexaForBusinessMetadata] = None
    PersonalPIN: Optional[str] = None


class BatchCreateRoomMembershipRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MembershipItemList: List[MembershipItem]


class BatchCreateRoomMembershipResponse(BaseValidatorModel):
    Errors: List[MemberError]
    ResponseMetadata: ResponseMetadata


class CreateMeetingDialOutResponse(BaseValidatorModel):
    TransactionId: str
    ResponseMetadata: ResponseMetadata


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class GetAccountSettingsResponse(BaseValidatorModel):
    AccountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


class GetPhoneNumberSettingsResponse(BaseValidatorModel):
    CallingName: str
    CallingNameUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class SearchAvailablePhoneNumbersResponse(BaseValidatorModel):
    E164PhoneNumbers: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class BatchDeletePhoneNumberResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


class BatchUpdatePhoneNumberResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


class BatchSuspendUserResponse(BaseValidatorModel):
    UserErrors: List[UserError]
    ResponseMetadata: ResponseMetadata


class BatchUnsuspendUserResponse(BaseValidatorModel):
    UserErrors: List[UserError]
    ResponseMetadata: ResponseMetadata


class BatchUpdateUserResponse(BaseValidatorModel):
    UserErrors: List[UserError]
    ResponseMetadata: ResponseMetadata


class BatchUpdatePhoneNumberRequest(BaseValidatorModel):
    UpdatePhoneNumberRequestItems: List[UpdatePhoneNumberRequestItem]


class CreateBotResponse(BaseValidatorModel):
    Bot: Bot
    ResponseMetadata: ResponseMetadata


class GetBotResponse(BaseValidatorModel):
    Bot: Bot
    ResponseMetadata: ResponseMetadata


class ListBotsResponse(BaseValidatorModel):
    Bots: List[Bot]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RegenerateSecurityTokenResponse(BaseValidatorModel):
    Bot: Bot
    ResponseMetadata: ResponseMetadata


class UpdateBotResponse(BaseValidatorModel):
    Bot: Bot
    ResponseMetadata: ResponseMetadata


class CreateRoomResponse(BaseValidatorModel):
    Room: Room
    ResponseMetadata: ResponseMetadata


class GetRoomResponse(BaseValidatorModel):
    Room: Room
    ResponseMetadata: ResponseMetadata


class ListRoomsResponse(BaseValidatorModel):
    Rooms: List[Room]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateRoomResponse(BaseValidatorModel):
    Room: Room
    ResponseMetadata: ResponseMetadata


class GetEventsConfigurationResponse(BaseValidatorModel):
    EventsConfiguration: EventsConfiguration
    ResponseMetadata: ResponseMetadata


class PutEventsConfigurationResponse(BaseValidatorModel):
    EventsConfiguration: EventsConfiguration
    ResponseMetadata: ResponseMetadata


class GetGlobalSettingsResponse(BaseValidatorModel):
    BusinessCalling: BusinessCallingSettings
    VoiceConnector: VoiceConnectorSettings
    ResponseMetadata: ResponseMetadata


class UpdateGlobalSettingsRequest(BaseValidatorModel):
    BusinessCalling: Optional[BusinessCallingSettings] = None
    VoiceConnector: Optional[VoiceConnectorSettings] = None


class InviteUsersResponse(BaseValidatorModel):
    Invites: List[Invite]
    ResponseMetadata: ResponseMetadata


class ListAccountsRequestPaginate(BaseValidatorModel):
    Name: Optional[str] = None
    UserEmail: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListUsersRequestPaginate(BaseValidatorModel):
    AccountId: str
    UserEmail: Optional[str] = None
    UserType: Optional[UserTypeType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListSupportedPhoneNumberCountriesResponse(BaseValidatorModel):
    PhoneNumberCountries: List[PhoneNumberCountry]
    ResponseMetadata: ResponseMetadata


class RoomMembership(BaseValidatorModel):
    RoomId: Optional[str] = None
    Member: Optional[Member] = None
    Role: Optional[RoomMembershipRoleType] = None
    InvitedBy: Optional[str] = None
    UpdatedTimestamp: Optional[datetime] = None


class PhoneNumberOrder(BaseValidatorModel):
    PhoneNumberOrderId: Optional[str] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    Status: Optional[PhoneNumberOrderStatusType] = None
    OrderedPhoneNumbers: Optional[List[OrderedPhoneNumber]] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class PhoneNumber(BaseValidatorModel):
    PhoneNumberId: Optional[str] = None
    E164PhoneNumber: Optional[str] = None
    Country: Optional[str] = None
    Type: Optional[PhoneNumberTypeType] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    Status: Optional[PhoneNumberStatusType] = None
    Capabilities: Optional[PhoneNumberCapabilities] = None
    Associations: Optional[List[PhoneNumberAssociation]] = None
    CallingName: Optional[str] = None
    CallingNameStatus: Optional[CallingNameStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    DeletionTimestamp: Optional[datetime] = None


class RetentionSettings(BaseValidatorModel):
    RoomRetentionSettings: Optional[RoomRetentionSettings] = None
    ConversationRetentionSettings: Optional[ConversationRetentionSettings] = None


class UserSettings(BaseValidatorModel):
    Telephony: TelephonySettings


class CreateAccountResponse(BaseValidatorModel):
    Account: Account
    ResponseMetadata: ResponseMetadata


class GetAccountResponse(BaseValidatorModel):
    Account: Account
    ResponseMetadata: ResponseMetadata


class ListAccountsResponse(BaseValidatorModel):
    Accounts: List[Account]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateAccountResponse(BaseValidatorModel):
    Account: Account
    ResponseMetadata: ResponseMetadata


class BatchUpdateUserRequest(BaseValidatorModel):
    AccountId: str
    UpdateUserRequestItems: List[UpdateUserRequestItem]


class CreateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class GetUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class ListUsersResponse(BaseValidatorModel):
    Users: List[User]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ResetPersonalPINResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class UpdateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


class CreateRoomMembershipResponse(BaseValidatorModel):
    RoomMembership: RoomMembership
    ResponseMetadata: ResponseMetadata


class ListRoomMembershipsResponse(BaseValidatorModel):
    RoomMemberships: List[RoomMembership]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class UpdateRoomMembershipResponse(BaseValidatorModel):
    RoomMembership: RoomMembership
    ResponseMetadata: ResponseMetadata


class CreatePhoneNumberOrderResponse(BaseValidatorModel):
    PhoneNumberOrder: PhoneNumberOrder
    ResponseMetadata: ResponseMetadata


class GetPhoneNumberOrderResponse(BaseValidatorModel):
    PhoneNumberOrder: PhoneNumberOrder
    ResponseMetadata: ResponseMetadata


class ListPhoneNumberOrdersResponse(BaseValidatorModel):
    PhoneNumberOrders: List[PhoneNumberOrder]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class GetPhoneNumberResponse(BaseValidatorModel):
    PhoneNumber: PhoneNumber
    ResponseMetadata: ResponseMetadata


class ListPhoneNumbersResponse(BaseValidatorModel):
    PhoneNumbers: List[PhoneNumber]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class RestorePhoneNumberResponse(BaseValidatorModel):
    PhoneNumber: PhoneNumber
    ResponseMetadata: ResponseMetadata


class UpdatePhoneNumberResponse(BaseValidatorModel):
    PhoneNumber: PhoneNumber
    ResponseMetadata: ResponseMetadata


class GetRetentionSettingsResponse(BaseValidatorModel):
    RetentionSettings: RetentionSettings
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class PutRetentionSettingsRequest(BaseValidatorModel):
    AccountId: str
    RetentionSettings: RetentionSettings


class PutRetentionSettingsResponse(BaseValidatorModel):
    RetentionSettings: RetentionSettings
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadata


class GetUserSettingsResponse(BaseValidatorModel):
    UserSettings: UserSettings
    ResponseMetadata: ResponseMetadata


class UpdateUserSettingsRequest(BaseValidatorModel):
    AccountId: str
    UserId: str
    UserSettings: UserSettings