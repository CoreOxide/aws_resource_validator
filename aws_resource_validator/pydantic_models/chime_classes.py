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
from aws_resource_validator.pydantic_models.chime_constants import *

class AccountSettingsTypeDef(BaseValidatorModel):
    DisableRemoteControl: Optional[bool] = None
    EnableDialOut: Optional[bool] = None


class SigninDelegateGroupTypeDef(BaseValidatorModel):
    GroupName: Optional[str] = None


class AlexaForBusinessMetadataTypeDef(BaseValidatorModel):
    IsAlexaForBusinessEnabled: Optional[bool] = None
    AlexaForBusinessRoomArn: Optional[str] = None


class AssociatePhoneNumberWithUserRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str
    E164PhoneNumber: str


class MembershipItemTypeDef(BaseValidatorModel):
    MemberId: Optional[str] = None
    Role: Optional[RoomMembershipRoleType] = None


class MemberErrorTypeDef(BaseValidatorModel):
    MemberId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchDeletePhoneNumberRequestTypeDef(BaseValidatorModel):
    PhoneNumberIds: Sequence[str]


class PhoneNumberErrorTypeDef(BaseValidatorModel):
    PhoneNumberId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class BatchSuspendUserRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserIdList: Sequence[str]


class UserErrorTypeDef(BaseValidatorModel):
    UserId: Optional[str] = None
    ErrorCode: Optional[ErrorCodeType] = None
    ErrorMessage: Optional[str] = None


class BatchUnsuspendUserRequestTypeDef(BaseValidatorModel):
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


class ConversationRetentionSettingsTypeDef(BaseValidatorModel):
    RetentionDays: Optional[int] = None


class CreateAccountRequestTypeDef(BaseValidatorModel):
    Name: str


class CreateBotRequestTypeDef(BaseValidatorModel):
    AccountId: str
    DisplayName: str
    Domain: Optional[str] = None


class CreateMeetingDialOutRequestTypeDef(BaseValidatorModel):
    MeetingId: str
    FromPhoneNumber: str
    ToPhoneNumber: str
    JoinToken: str


class CreatePhoneNumberOrderRequestTypeDef(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType
    E164PhoneNumbers: Sequence[str]


class CreateRoomMembershipRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MemberId: str
    Role: Optional[RoomMembershipRoleType] = None


class CreateRoomRequestTypeDef(BaseValidatorModel):
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


class CreateUserRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Username: Optional[str] = None
    Email: Optional[str] = None
    UserType: Optional[UserTypeType] = None


class DeleteAccountRequestTypeDef(BaseValidatorModel):
    AccountId: str


class DeleteEventsConfigurationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BotId: str


class DeletePhoneNumberRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str


class DeleteRoomMembershipRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MemberId: str


class DeleteRoomRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str


class DisassociatePhoneNumberFromUserRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str


class DisassociateSigninDelegateGroupsFromAccountRequestTypeDef(BaseValidatorModel):
    AccountId: str
    GroupNames: Sequence[str]


class EventsConfigurationTypeDef(BaseValidatorModel):
    BotId: Optional[str] = None
    OutboundEventsHTTPSEndpoint: Optional[str] = None
    LambdaFunctionArn: Optional[str] = None


class GetAccountRequestTypeDef(BaseValidatorModel):
    AccountId: str


class GetAccountSettingsRequestTypeDef(BaseValidatorModel):
    AccountId: str


class GetBotRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BotId: str


class GetEventsConfigurationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BotId: str


class VoiceConnectorSettingsTypeDef(BaseValidatorModel):
    CdrBucket: Optional[str] = None


class GetPhoneNumberOrderRequestTypeDef(BaseValidatorModel):
    PhoneNumberOrderId: str


class GetPhoneNumberRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str


class GetRetentionSettingsRequestTypeDef(BaseValidatorModel):
    AccountId: str


class GetRoomRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str


class GetUserRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str


class GetUserSettingsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str


class InviteTypeDef(BaseValidatorModel):
    InviteId: Optional[str] = None
    Status: Optional[InviteStatusType] = None
    EmailAddress: Optional[str] = None
    EmailStatus: Optional[EmailStatusType] = None


class InviteUsersRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserEmailList: Sequence[str]
    UserType: Optional[UserTypeType] = None


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListAccountsRequestTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    UserEmail: Optional[str] = None
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListBotsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListPhoneNumberOrdersRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListPhoneNumbersRequestTypeDef(BaseValidatorModel):
    Status: Optional[PhoneNumberStatusType] = None
    ProductType: Optional[PhoneNumberProductTypeType] = None
    FilterName: Optional[PhoneNumberAssociationNameType] = None
    FilterValue: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRoomMembershipsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListRoomsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    MemberId: Optional[str] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class ListSupportedPhoneNumberCountriesRequestTypeDef(BaseValidatorModel):
    ProductType: PhoneNumberProductTypeType


class PhoneNumberCountryTypeDef(BaseValidatorModel):
    CountryCode: Optional[str] = None
    SupportedPhoneNumberTypes: Optional[List[PhoneNumberTypeType]] = None


class ListUsersRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserEmail: Optional[str] = None
    UserType: Optional[UserTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class LogoutUserRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str


class MemberTypeDef(BaseValidatorModel):
    MemberId: Optional[str] = None
    MemberType: Optional[MemberTypeType] = None
    Email: Optional[str] = None
    FullName: Optional[str] = None
    AccountId: Optional[str] = None


class OrderedPhoneNumberTypeDef(BaseValidatorModel):
    E164PhoneNumber: Optional[str] = None
    Status: Optional[OrderedPhoneNumberStatusType] = None


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


class PutEventsConfigurationRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BotId: str
    OutboundEventsHTTPSEndpoint: Optional[str] = None
    LambdaFunctionArn: Optional[str] = None


class RedactConversationMessageRequestTypeDef(BaseValidatorModel):
    AccountId: str
    ConversationId: str
    MessageId: str


class RedactRoomMessageRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MessageId: str


class RegenerateSecurityTokenRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BotId: str


class ResetPersonalPINRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str


class RestorePhoneNumberRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str


class RoomRetentionSettingsTypeDef(BaseValidatorModel):
    RetentionDays: Optional[int] = None


class SearchAvailablePhoneNumbersRequestTypeDef(BaseValidatorModel):
    AreaCode: Optional[str] = None
    City: Optional[str] = None
    Country: Optional[str] = None
    State: Optional[str] = None
    TollFreePrefix: Optional[str] = None
    PhoneNumberType: Optional[PhoneNumberTypeType] = None
    MaxResults: Optional[int] = None
    NextToken: Optional[str] = None


class TelephonySettingsTypeDef(BaseValidatorModel):
    InboundCalling: bool
    OutboundCalling: bool
    SMS: bool


class UpdateAccountRequestTypeDef(BaseValidatorModel):
    AccountId: str
    Name: Optional[str] = None
    DefaultLicense: Optional[LicenseType] = None


class UpdateBotRequestTypeDef(BaseValidatorModel):
    AccountId: str
    BotId: str
    Disabled: Optional[bool] = None


class UpdatePhoneNumberRequestTypeDef(BaseValidatorModel):
    PhoneNumberId: str
    ProductType: Optional[PhoneNumberProductTypeType] = None
    CallingName: Optional[str] = None


class UpdatePhoneNumberSettingsRequestTypeDef(BaseValidatorModel):
    CallingName: str


class UpdateRoomMembershipRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MemberId: str
    Role: Optional[RoomMembershipRoleType] = None


class UpdateRoomRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    Name: Optional[str] = None


class UpdateAccountSettingsRequestTypeDef(BaseValidatorModel):
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


class AssociateSigninDelegateGroupsWithAccountRequestTypeDef(BaseValidatorModel):
    AccountId: str
    SigninDelegateGroups: Sequence[SigninDelegateGroupTypeDef]


class BatchCreateRoomMembershipRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RoomId: str
    MembershipItemList: Sequence[MembershipItemTypeDef]


class BatchCreateRoomMembershipResponseTypeDef(BaseValidatorModel):
    Errors: List[MemberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class CreateMeetingDialOutResponseTypeDef(BaseValidatorModel):
    TransactionId: str
    ResponseMetadata: ResponseMetadataTypeDef


class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef


class GetAccountSettingsResponseTypeDef(BaseValidatorModel):
    AccountSettings: AccountSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetPhoneNumberSettingsResponseTypeDef(BaseValidatorModel):
    CallingName: str
    CallingNameUpdatedTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class SearchAvailablePhoneNumbersResponseTypeDef(BaseValidatorModel):
    E164PhoneNumbers: List[str]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class BatchDeletePhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class BatchUpdatePhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumberErrors: List[PhoneNumberErrorTypeDef]
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


class BatchUpdatePhoneNumberRequestTypeDef(BaseValidatorModel):
    UpdatePhoneNumberRequestItems: Sequence[UpdatePhoneNumberRequestItemTypeDef]


class CreateBotResponseTypeDef(BaseValidatorModel):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetBotResponseTypeDef(BaseValidatorModel):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListBotsResponseTypeDef(BaseValidatorModel):
    Bots: List[BotTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class RegenerateSecurityTokenResponseTypeDef(BaseValidatorModel):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateBotResponseTypeDef(BaseValidatorModel):
    Bot: BotTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRoomResponseTypeDef(BaseValidatorModel):
    Room: RoomTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetRoomResponseTypeDef(BaseValidatorModel):
    Room: RoomTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRoomsResponseTypeDef(BaseValidatorModel):
    Rooms: List[RoomTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateRoomResponseTypeDef(BaseValidatorModel):
    Room: RoomTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


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


class UpdateGlobalSettingsRequestTypeDef(BaseValidatorModel):
    BusinessCalling: Optional[BusinessCallingSettingsTypeDef] = None
    VoiceConnector: Optional[VoiceConnectorSettingsTypeDef] = None


class InviteUsersResponseTypeDef(BaseValidatorModel):
    Invites: List[InviteTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


class ListAccountsRequestPaginateTypeDef(BaseValidatorModel):
    Name: Optional[str] = None
    UserEmail: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListUsersRequestPaginateTypeDef(BaseValidatorModel):
    AccountId: str
    UserEmail: Optional[str] = None
    UserType: Optional[UserTypeType] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListSupportedPhoneNumberCountriesResponseTypeDef(BaseValidatorModel):
    PhoneNumberCountries: List[PhoneNumberCountryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef


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


class RetentionSettingsTypeDef(BaseValidatorModel):
    RoomRetentionSettings: Optional[RoomRetentionSettingsTypeDef] = None
    ConversationRetentionSettings: Optional[ConversationRetentionSettingsTypeDef] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class UpdateAccountResponseTypeDef(BaseValidatorModel):
    Account: AccountTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateUserRequestItemTypeDef(BaseValidatorModel):
    pass


class BatchUpdateUserRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UpdateUserRequestItems: Sequence[UpdateUserRequestItemTypeDef]


class UserTypeDef(BaseValidatorModel):
    pass


class CreateUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListUsersResponseTypeDef(BaseValidatorModel):
    Users: List[UserTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class ResetPersonalPINResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateUserResponseTypeDef(BaseValidatorModel):
    User: UserTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class CreateRoomMembershipResponseTypeDef(BaseValidatorModel):
    RoomMembership: RoomMembershipTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListRoomMembershipsResponseTypeDef(BaseValidatorModel):
    RoomMemberships: List[RoomMembershipTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


class PhoneNumberTypeDef(BaseValidatorModel):
    pass


class GetPhoneNumberResponseTypeDef(BaseValidatorModel):
    PhoneNumber: PhoneNumberTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class ListPhoneNumbersResponseTypeDef(BaseValidatorModel):
    PhoneNumbers: List[PhoneNumberTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None


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


class PutRetentionSettingsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    RetentionSettings: RetentionSettingsTypeDef


class PutRetentionSettingsResponseTypeDef(BaseValidatorModel):
    RetentionSettings: RetentionSettingsTypeDef
    InitiateDeletionTimestamp: datetime
    ResponseMetadata: ResponseMetadataTypeDef


class GetUserSettingsResponseTypeDef(BaseValidatorModel):
    UserSettings: UserSettingsTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class UpdateUserSettingsRequestTypeDef(BaseValidatorModel):
    AccountId: str
    UserId: str
    UserSettings: UserSettingsTypeDef


