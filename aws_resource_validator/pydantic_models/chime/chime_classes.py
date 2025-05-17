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


# This class is the input for the 'batch_delete_phone_number' function.
class BatchDeletePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberIds: List[str]


class PhoneNumberError(BaseValidatorModel):
    PhoneNumberId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


# This class is the input for the 'batch_suspend_user' function.
class BatchSuspendUserRequest(BaseValidatorModel):
    AccountId: str
    UserIdList: List[str]


class UserError(BaseValidatorModel):
    UserId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


# This class is the input for the 'batch_unsuspend_user' function.
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


# This class is the input for the 'create_account' function.
class CreateAccountRequest(BaseValidatorModel):
    Name: str


# This class is the input for the 'create_bot' function.
class CreateBotRequest(BaseValidatorModel):
    AccountId: str
    DisplayName: str
    Domain: Optional[str] = None


# This class is the input for the 'create_meeting_dial_out' function.
class CreateMeetingDialOutRequest(BaseValidatorModel):
    MeetingId: str
    FromPhoneNumber: str
    ToPhoneNumber: str
    JoinToken: str


# This class is the input for the 'create_phone_number_order' function.
class CreatePhoneNumberOrderRequest(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType
    E164PhoneNumbers: List[str]


# This class is the input for the 'create_room_membership' function.
class CreateRoomMembershipRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MemberId: str
    Role: Optional[RoomMembershipRoleType] = None


# This class is the input for the 'create_room' function.
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


# This class is the input for the 'create_user' function.
class CreateUserRequest(BaseValidatorModel):
    AccountId: str
    Username: Optional[str] = None
    Email: Optional[str] = None
    UserType: Optional[UserTypeType] = None


class DeleteAccountRequest(BaseValidatorModel):
    AccountId: str


# This class is the input for the 'delete_events_configuration' function.
class DeleteEventsConfigurationRequest(BaseValidatorModel):
    AccountId: str
    BotId: str


# This class is the input for the 'delete_phone_number' function.
class DeletePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


# This class is the input for the 'delete_room_membership' function.
class DeleteRoomMembershipRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MemberId: str


# This class is the input for the 'delete_room' function.
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


# This class is the input for the 'get_account' function.
class GetAccountRequest(BaseValidatorModel):
    AccountId: str


# This class is the input for the 'get_account_settings' function.
class GetAccountSettingsRequest(BaseValidatorModel):
    AccountId: str


# This class is the input for the 'get_bot' function.
class GetBotRequest(BaseValidatorModel):
    AccountId: str
    BotId: str


# This class is the input for the 'get_events_configuration' function.
class GetEventsConfigurationRequest(BaseValidatorModel):
    AccountId: str
    BotId: str


class VoiceConnectorSettings(BaseValidatorModel):
    CdrBucket: Optional[str] = None


# This class is the input for the 'get_phone_number_order' function.
class GetPhoneNumberOrderRequest(BaseValidatorModel):
    PhoneNumberOrderId: str


# This class is the input for the 'get_phone_number' function.
class GetPhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


# This class is the input for the 'get_retention_settings' function.
class GetRetentionSettingsRequest(BaseValidatorModel):
    AccountId: str


# This class is the input for the 'get_room' function.
class GetRoomRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str


# This class is the input for the 'get_user' function.
class GetUserRequest(BaseValidatorModel):
    AccountId: str
    UserId: str


# This class is the input for the 'get_user_settings' function.
class GetUserSettingsRequest(BaseValidatorModel):
    AccountId: str
    UserId: str


class Invite(BaseValidatorModel):
    InviteId: Optional[str] = None
    Status: Optional[InviteStatusType] = None
    EmailAddress: Optional[str] = None
    EmailStatus: Optional[EmailStatusType] = None


# This class is the input for the 'invite_users' function.
class InviteUsersRequest(BaseValidatorModel):
    AccountId: str
    UserEmailList: List[str]
    UserType: Optional[UserTypeType] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_accounts' function.
class ListAccountsRequest(BaseValidatorModel):
    Name: Optional[str] = None
    UserEmail: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_bots' function.
class ListBotsRequest(BaseValidatorModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_phone_number_orders' function.
class ListPhoneNumberOrdersRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


# This class is the input for the 'list_phone_numbers' function.
class ListPhoneNumbersRequest(BaseValidatorModel):
    Status: Optional[PhoneNumberStatusType] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    FilterName: Optional[PhoneNumberAssociationNameType] = None
    FilterValue: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_room_memberships' function.
class ListRoomMembershipsRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_rooms' function.
class ListRoomsRequest(BaseValidatorModel):
    AccountId: str
    MemberId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


# This class is the input for the 'list_supported_phone_number_countries' function.
class ListSupportedPhoneNumberCountriesRequest(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType


class PhoneNumberCountry(BaseValidatorModel):
    CountryCode: Optional[str] = None
    SupportedPhoneNumberTypes: Optional[List[PhoneNumberTypeType]] = None


# This class is the input for the 'list_users' function.
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


# This class is the input for the 'put_events_configuration' function.
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


# This class is the input for the 'regenerate_security_token' function.
class RegenerateSecurityTokenRequest(BaseValidatorModel):
    AccountId: str
    BotId: str


# This class is the input for the 'reset_personal_pin' function.
class ResetPersonalPINRequest(BaseValidatorModel):
    AccountId: str
    UserId: str


# This class is the input for the 'restore_phone_number' function.
class RestorePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str


class RoomRetentionSettings(BaseValidatorModel):
    RetentionDays: Optional[int] = None


# This class is the input for the 'search_available_phone_numbers' function.
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


# This class is the input for the 'update_account' function.
class UpdateAccountRequest(BaseValidatorModel):
    AccountId: str
    Name: Optional[str] = None
    DefaultLicense: Optional[LicenseType] = None


# This class is the input for the 'update_bot' function.
class UpdateBotRequest(BaseValidatorModel):
    AccountId: str
    BotId: str
    Disabled: Optional[bool] = None


# This class is the input for the 'update_phone_number' function.
class UpdatePhoneNumberRequest(BaseValidatorModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None


# This class is the input for the 'update_phone_number_settings' function.
class UpdatePhoneNumberSettingsRequest(BaseValidatorModel):
    CallingName: str


# This class is the input for the 'update_room_membership' function.
class UpdateRoomMembershipRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MemberId: str
    Role: Optional[RoomMembershipRoleType] = None


# This class is the input for the 'update_room' function.
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


# This class is the input for the 'update_user' function.
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


# This class is the input for the 'batch_create_room_membership' function.
class BatchCreateRoomMembershipRequest(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MembershipItemList: List[MembershipItem]


# This class is the output for the 'batch_create_room_membership' function.
class BatchCreateRoomMembershipResponse(BaseValidatorModel):
    Errors: List[MemberError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_meeting_dial_out' function.
class CreateMeetingDialOutResponse(BaseValidatorModel):
    TransactionId: str
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_user_settings' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_account_settings' function.
class GetAccountSettingsResponse(BaseValidatorModel):
    AccountSettings: AccountSettings
    ResponseMetadata: ResponseMetadata


class GetPhoneNumberSettingsResponse(BaseValidatorModel):
    CallingName: str
    CallingNameUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'search_available_phone_numbers' function.
class SearchAvailablePhoneNumbersResponse(BaseValidatorModel):
    E164PhoneNumbers: List[str]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'batch_delete_phone_number' function.
class BatchDeletePhoneNumberResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_update_phone_number' function.
class BatchUpdatePhoneNumberResponse(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_suspend_user' function.
class BatchSuspendUserResponse(BaseValidatorModel):
    UserErrors: List[UserError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_unsuspend_user' function.
class BatchUnsuspendUserResponse(BaseValidatorModel):
    UserErrors: List[UserError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_update_user' function.
class BatchUpdateUserResponse(BaseValidatorModel):
    UserErrors: List[UserError]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_update_phone_number' function.
class BatchUpdatePhoneNumberRequest(BaseValidatorModel):
    UpdatePhoneNumberRequestItems: List[UpdatePhoneNumberRequestItem]


# This class is the output for the 'create_bot' function.
class CreateBotResponse(BaseValidatorModel):
    Bot: Bot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_bot' function.
class GetBotResponse(BaseValidatorModel):
    Bot: Bot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_bots' function.
class ListBotsResponse(BaseValidatorModel):
    Bots: List[Bot]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'regenerate_security_token' function.
class RegenerateSecurityTokenResponse(BaseValidatorModel):
    Bot: Bot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_bot' function.
class UpdateBotResponse(BaseValidatorModel):
    Bot: Bot
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_room' function.
class CreateRoomResponse(BaseValidatorModel):
    Room: Room
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_room' function.
class GetRoomResponse(BaseValidatorModel):
    Room: Room
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_rooms' function.
class ListRoomsResponse(BaseValidatorModel):
    Rooms: List[Room]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_room' function.
class UpdateRoomResponse(BaseValidatorModel):
    Room: Room
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_events_configuration' function.
class GetEventsConfigurationResponse(BaseValidatorModel):
    EventsConfiguration: EventsConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'put_events_configuration' function.
class PutEventsConfigurationResponse(BaseValidatorModel):
    EventsConfiguration: EventsConfiguration
    ResponseMetadata: ResponseMetadata


class GetGlobalSettingsResponse(BaseValidatorModel):
    BusinessCalling: BusinessCallingSettings
    VoiceConnector: VoiceConnectorSettings
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_global_settings' function.
class UpdateGlobalSettingsRequest(BaseValidatorModel):
    BusinessCalling: Optional[BusinessCallingSettings] = None
    VoiceConnector: Optional[VoiceConnectorSettings] = None


# This class is the output for the 'invite_users' function.
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


# This class is the output for the 'list_supported_phone_number_countries' function.
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


# This class is the output for the 'create_account' function.
class CreateAccountResponse(BaseValidatorModel):
    Account: Account
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_account' function.
class GetAccountResponse(BaseValidatorModel):
    Account: Account
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_accounts' function.
class ListAccountsResponse(BaseValidatorModel):
    Accounts: List[Account]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_account' function.
class UpdateAccountResponse(BaseValidatorModel):
    Account: Account
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_update_user' function.
class BatchUpdateUserRequest(BaseValidatorModel):
    AccountId: str
    UpdateUserRequestItems: List[UpdateUserRequestItem]


# This class is the output for the 'create_user' function.
class CreateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_user' function.
class GetUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_users' function.
class ListUsersResponse(BaseValidatorModel):
    Users: List[User]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'reset_personal_pin' function.
class ResetPersonalPINResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_user' function.
class UpdateUserResponse(BaseValidatorModel):
    User: User
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_room_membership' function.
class CreateRoomMembershipResponse(BaseValidatorModel):
    RoomMembership: RoomMembership
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_room_memberships' function.
class ListRoomMembershipsResponse(BaseValidatorModel):
    RoomMemberships: List[RoomMembership]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'update_room_membership' function.
class UpdateRoomMembershipResponse(BaseValidatorModel):
    RoomMembership: RoomMembership
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_phone_number_order' function.
class CreatePhoneNumberOrderResponse(BaseValidatorModel):
    PhoneNumberOrder: PhoneNumberOrder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_phone_number_order' function.
class GetPhoneNumberOrderResponse(BaseValidatorModel):
    PhoneNumberOrder: PhoneNumberOrder
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_phone_number_orders' function.
class ListPhoneNumberOrdersResponse(BaseValidatorModel):
    PhoneNumberOrders: List[PhoneNumberOrder]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'get_phone_number' function.
class GetPhoneNumberResponse(BaseValidatorModel):
    PhoneNumber: PhoneNumber
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_phone_numbers' function.
class ListPhoneNumbersResponse(BaseValidatorModel):
    PhoneNumbers: List[PhoneNumber]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


# This class is the output for the 'restore_phone_number' function.
class RestorePhoneNumberResponse(BaseValidatorModel):
    PhoneNumber: PhoneNumber
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_phone_number' function.
class UpdatePhoneNumberResponse(BaseValidatorModel):
    PhoneNumber: PhoneNumber
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_retention_settings' function.
class GetRetentionSettingsResponse(BaseValidatorModel):
    RetentionSettings: RetentionSettings
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'put_retention_settings' function.
class PutRetentionSettingsRequest(BaseValidatorModel):
    AccountId: str
    RetentionSettings: RetentionSettings


# This class is the output for the 'put_retention_settings' function.
class PutRetentionSettingsResponse(BaseValidatorModel):
    RetentionSettings: RetentionSettings
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_user_settings' function.
class GetUserSettingsResponse(BaseValidatorModel):
    UserSettings: UserSettings
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'update_user_settings' function.
class UpdateUserSettingsRequest(BaseValidatorModel):
    AccountId: str
    UserId: str
    UserSettings: UserSettings