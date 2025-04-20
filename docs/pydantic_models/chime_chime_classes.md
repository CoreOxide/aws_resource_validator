# Chime Chime Classes

# Account

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AccountType
- **Type**: typing.Optional[typing.Literal['EnterpriseDirectory', 'EnterpriseLWA', 'EnterpriseOIDC', 'Team']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DefaultLicense
- **Type**: typing.Optional[typing.Literal['Basic', 'Plus', 'Pro', 'ProTrial']]

### SupportedLicenses
- **Type**: typing.Optional[typing.List[typing.Literal['Basic', 'Plus', 'Pro', 'ProTrial']]]

### AccountStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Suspended']]

### SigninDelegateGroups
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.SigninDelegateGroup]]


# AccountSettings

### DisableRemoteControl
- **Type**: typing.Optional[bool]

### EnableDialOut
- **Type**: typing.Optional[bool]


# AlexaForBusinessMetadata

### IsAlexaForBusinessEnabled
- **Type**: typing.Optional[bool]

### AlexaForBusinessRoomArn
- **Type**: typing.Optional[str]


# AssociatePhoneNumberWithUserRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateSigninDelegateGroupsWithAccountRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### SigninDelegateGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.SigninDelegateGroup]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateRoomMembershipRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes

### MembershipItemList
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.MembershipItem]
- **Required**: Yes


# BatchCreateRoomMembershipResponse

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.MemberError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# BatchDeletePhoneNumberRequest

### PhoneNumberIds
- **Type**: typing.List[str]
- **Required**: Yes


# BatchDeletePhoneNumberResponse

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.PhoneNumberError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# BatchSuspendUserRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserIdList
- **Type**: typing.List[str]
- **Required**: Yes


# BatchSuspendUserResponse

### UserErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.UserError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUnsuspendUserRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserIdList
- **Type**: typing.List[str]
- **Required**: Yes


# BatchUnsuspendUserResponse

### UserErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.UserError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdatePhoneNumberRequest

### UpdatePhoneNumberRequestItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.UpdatePhoneNumberRequestItem]
- **Required**: Yes


# BatchUpdatePhoneNumberResponse

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.PhoneNumberError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# BatchUpdateUserRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateUserRequestItems
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.UpdateUserRequestItem]
- **Required**: Yes


# BatchUpdateUserResponse

### UserErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.UserError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# Bot

### BotId
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### BotType
- **Type**: typing.Optional[typing.Literal['ChatBot']]

### Disabled
- **Type**: typing.Optional[bool]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### BotEmail
- **Type**: typing.Optional[str]

### SecurityToken
- **Type**: typing.Optional[str]


# BusinessCallingSettings

### CdrBucket
- **Type**: typing.Optional[str]


# ConversationRetentionSettings

### RetentionDays
- **Type**: typing.Optional[int]


# CreateAccountRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAccountResponse

### Account
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.Account'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBotRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]


# CreateBotResponse

### Bot
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.Bot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMeetingDialOutRequest

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### FromPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ToPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### JoinToken
- **Type**: <class 'str'>
- **Required**: Yes


# CreateMeetingDialOutResponse

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePhoneNumberOrderRequest

### ProductType
- **Type**: typing.Literal['BusinessCalling', 'SipMediaApplicationDialIn', 'VoiceConnector']
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.List[str]
- **Required**: Yes


# CreatePhoneNumberOrderResponse

### PhoneNumberOrder
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.PhoneNumberOrder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRoomMembershipRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: typing.Optional[typing.Literal['Administrator', 'Member']]


# CreateRoomMembershipResponse

### RoomMembership
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.RoomMembership'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRoomRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateRoomResponse

### Room
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.Room'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### UserType
- **Type**: typing.Optional[typing.Literal['PrivateUser', 'SharedDevice']]


# CreateUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAccountRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventsConfigurationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BotId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePhoneNumberRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoomMembershipRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoomRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociatePhoneNumberFromUserRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateSigninDelegateGroupsFromAccountRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupNames
- **Type**: typing.List[str]
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# EventsConfiguration

### BotId
- **Type**: typing.Optional[str]

### OutboundEventsHTTPSEndpoint
- **Type**: typing.Optional[str]

### LambdaFunctionArn
- **Type**: typing.Optional[str]


# GetAccountRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccountResponse

### Account
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.Account'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccountSettingsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccountSettingsResponse

### AccountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.AccountSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# GetBotRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BotId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBotResponse

### Bot
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.Bot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# GetEventsConfigurationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BotId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventsConfigurationResponse

### EventsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.EventsConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# GetGlobalSettingsResponse

### BusinessCalling
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.BusinessCallingSettings'>
- **Required**: Yes

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.VoiceConnectorSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# GetPhoneNumberOrderRequest

### PhoneNumberOrderId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPhoneNumberOrderResponse

### PhoneNumberOrder
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.PhoneNumberOrder'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# GetPhoneNumberRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPhoneNumberResponse

### PhoneNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.PhoneNumber'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# GetPhoneNumberSettingsResponse

### CallingName
- **Type**: <class 'str'>
- **Required**: Yes

### CallingNameUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# GetRetentionSettingsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRetentionSettingsResponse

### RetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.RetentionSettings'>
- **Required**: Yes

### InitiateDeletionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# GetRoomRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRoomResponse

### Room
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.Room'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserSettingsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserSettingsResponse

### UserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.UserSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# Invite

### InviteId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Accepted', 'Failed', 'Pending']]

### EmailAddress
- **Type**: typing.Optional[str]

### EmailStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'NotSent', 'Sent']]


# InviteUsersRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserEmailList
- **Type**: typing.List[str]
- **Required**: Yes

### UserType
- **Type**: typing.Optional[typing.Literal['PrivateUser', 'SharedDevice']]


# InviteUsersResponse

### Invites
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.Invite]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# ListAccountsRequest

### Name
- **Type**: typing.Optional[str]

### UserEmail
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccountsRequestPaginate

### Name
- **Type**: typing.Optional[str]

### UserEmail
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime.chime_classes.PaginatorConfig]


# ListAccountsResponse

### Accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.Account]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBotsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListBotsResponse

### Bots
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.Bot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumberOrdersRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPhoneNumberOrdersResponse

### PhoneNumberOrders
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.PhoneNumberOrder]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersRequest

### Status
- **Type**: typing.Optional[typing.Literal['AcquireFailed', 'AcquireInProgress', 'Assigned', 'DeleteFailed', 'DeleteInProgress', 'ReleaseFailed', 'ReleaseInProgress', 'Unassigned']]

### ProductType
- **Type**: typing.Optional[typing.Literal['BusinessCalling', 'SipMediaApplicationDialIn', 'VoiceConnector']]

### FilterName
- **Type**: typing.Optional[typing.Literal['AccountId', 'SipRuleId', 'UserId', 'VoiceConnectorGroupId', 'VoiceConnectorId']]

### FilterValue
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersResponse

### PhoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.PhoneNumber]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRoomMembershipsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRoomMembershipsResponse

### RoomMemberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.RoomMembership]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRoomsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRoomsResponse

### Rooms
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.Room]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSupportedPhoneNumberCountriesRequest

### ProductType
- **Type**: typing.Literal['BusinessCalling', 'SipMediaApplicationDialIn', 'VoiceConnector']
- **Required**: Yes


# ListSupportedPhoneNumberCountriesResponse

### PhoneNumberCountries
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.PhoneNumberCountry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# ListUsersRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserEmail
- **Type**: typing.Optional[str]

### UserType
- **Type**: typing.Optional[typing.Literal['PrivateUser', 'SharedDevice']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequestPaginate

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserEmail
- **Type**: typing.Optional[str]

### UserType
- **Type**: typing.Optional[typing.Literal['PrivateUser', 'SharedDevice']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime.chime_classes.PaginatorConfig]


# ListUsersResponse

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.User]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LogoutUserRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# Member

### MemberId
- **Type**: typing.Optional[str]

### MemberType
- **Type**: typing.Optional[typing.Literal['Bot', 'User', 'Webhook']]

### Email
- **Type**: typing.Optional[str]

### FullName
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]


# MemberError

### MemberId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'BadRequest', 'Conflict', 'Forbidden', 'NotFound', 'PhoneNumberAssociationsExist', 'PreconditionFailed', 'ResourceLimitExceeded', 'ServiceFailure', 'ServiceUnavailable', 'Throttled', 'Throttling', 'Unauthorized', 'Unprocessable', 'VoiceConnectorGroupAssociationsExist']]

### ErrorMessage
- **Type**: typing.Optional[str]


# MembershipItem

### MemberId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['Administrator', 'Member']]


# OrderedPhoneNumber

### E164PhoneNumber
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Acquired', 'Failed', 'Processing']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhoneNumber

### PhoneNumberId
- **Type**: typing.Optional[str]

### E164PhoneNumber
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['Local', 'TollFree']]

### ProductType
- **Type**: typing.Optional[typing.Literal['BusinessCalling', 'SipMediaApplicationDialIn', 'VoiceConnector']]

### Status
- **Type**: typing.Optional[typing.Literal['AcquireFailed', 'AcquireInProgress', 'Assigned', 'DeleteFailed', 'DeleteInProgress', 'ReleaseFailed', 'ReleaseInProgress', 'Unassigned']]

### Capabilities
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime.chime_classes.PhoneNumberCapabilities]

### Associations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.PhoneNumberAssociation]]

### CallingName
- **Type**: typing.Optional[str]

### CallingNameStatus
- **Type**: typing.Optional[typing.Literal['Unassigned', 'UpdateFailed', 'UpdateInProgress', 'UpdateSucceeded']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### DeletionTimestamp
- **Type**: typing.Optional[datetime.datetime]


# PhoneNumberAssociation

### Value
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[typing.Literal['AccountId', 'SipRuleId', 'UserId', 'VoiceConnectorGroupId', 'VoiceConnectorId']]

### AssociatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# PhoneNumberCapabilities

### InboundCall
- **Type**: typing.Optional[bool]

### OutboundCall
- **Type**: typing.Optional[bool]

### InboundSMS
- **Type**: typing.Optional[bool]

### OutboundSMS
- **Type**: typing.Optional[bool]

### InboundMMS
- **Type**: typing.Optional[bool]

### OutboundMMS
- **Type**: typing.Optional[bool]


# PhoneNumberCountry

### CountryCode
- **Type**: typing.Optional[str]

### SupportedPhoneNumberTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Local', 'TollFree']]]


# PhoneNumberError

### PhoneNumberId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'BadRequest', 'Conflict', 'Forbidden', 'NotFound', 'PhoneNumberAssociationsExist', 'PreconditionFailed', 'ResourceLimitExceeded', 'ServiceFailure', 'ServiceUnavailable', 'Throttled', 'Throttling', 'Unauthorized', 'Unprocessable', 'VoiceConnectorGroupAssociationsExist']]

### ErrorMessage
- **Type**: typing.Optional[str]


# PhoneNumberOrder

### PhoneNumberOrderId
- **Type**: typing.Optional[str]

### ProductType
- **Type**: typing.Optional[typing.Literal['BusinessCalling', 'SipMediaApplicationDialIn', 'VoiceConnector']]

### Status
- **Type**: typing.Optional[typing.Literal['Failed', 'Partial', 'Processing', 'Successful']]

### OrderedPhoneNumbers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime.chime_classes.OrderedPhoneNumber]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# PutEventsConfigurationRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BotId
- **Type**: <class 'str'>
- **Required**: Yes

### OutboundEventsHTTPSEndpoint
- **Type**: typing.Optional[str]

### LambdaFunctionArn
- **Type**: typing.Optional[str]


# PutEventsConfigurationResponse

### EventsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.EventsConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# PutRetentionSettingsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.RetentionSettings'>
- **Required**: Yes


# PutRetentionSettingsResponse

### RetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.RetentionSettings'>
- **Required**: Yes

### InitiateDeletionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# RedactConversationMessageRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ConversationId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes


# RedactRoomMessageRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes


# RegenerateSecurityTokenRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BotId
- **Type**: <class 'str'>
- **Required**: Yes


# RegenerateSecurityTokenResponse

### Bot
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.Bot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# ResetPersonalPINRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# ResetPersonalPINResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# ResponseMetadata

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HTTPStatusCode
- **Type**: <class 'int'>
- **Required**: Yes

### HTTPHeaders
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### RetryAttempts
- **Type**: <class 'int'>
- **Required**: Yes

### HostId
- **Type**: typing.Optional[str]


# RestorePhoneNumberRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# RestorePhoneNumberResponse

### PhoneNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.PhoneNumber'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# RetentionSettings

### RoomRetentionSettings
- **Type**: <class 'NoneType'>

### ConversationRetentionSettings
- **Type**: <class 'NoneType'>


# Room

### RoomId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# RoomMembership

### RoomId
- **Type**: typing.Optional[str]

### Member
- **Type**: <class 'NoneType'>

### Role
- **Type**: typing.Optional[typing.Literal['Administrator', 'Member']]

### InvitedBy
- **Type**: typing.Optional[str]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# RoomRetentionSettings

### RetentionDays
- **Type**: typing.Optional[int]


# SearchAvailablePhoneNumbersRequest

### AreaCode
- **Type**: typing.Optional[str]

### City
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]

### TollFreePrefix
- **Type**: typing.Optional[str]

### PhoneNumberType
- **Type**: typing.Optional[typing.Literal['Local', 'TollFree']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchAvailablePhoneNumbersResponse

### E164PhoneNumbers
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SigninDelegateGroup

### GroupName
- **Type**: typing.Optional[str]


# TelephonySettings

### InboundCalling
- **Type**: <class 'bool'>
- **Required**: Yes

### OutboundCalling
- **Type**: <class 'bool'>
- **Required**: Yes

### SMS
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateAccountRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### DefaultLicense
- **Type**: typing.Optional[typing.Literal['Basic', 'Plus', 'Pro', 'ProTrial']]


# UpdateAccountResponse

### Account
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.Account'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAccountSettingsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.AccountSettings'>
- **Required**: Yes


# UpdateBotRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BotId
- **Type**: <class 'str'>
- **Required**: Yes

### Disabled
- **Type**: typing.Optional[bool]


# UpdateBotResponse

### Bot
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.Bot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGlobalSettingsRequest

### BusinessCalling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime.chime_classes.BusinessCallingSettings]

### VoiceConnector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime.chime_classes.VoiceConnectorSettings]


# UpdatePhoneNumberRequest

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### ProductType
- **Type**: typing.Optional[typing.Literal['BusinessCalling', 'SipMediaApplicationDialIn', 'VoiceConnector']]

### CallingName
- **Type**: typing.Optional[str]


# UpdatePhoneNumberRequestItem

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### ProductType
- **Type**: typing.Optional[typing.Literal['BusinessCalling', 'SipMediaApplicationDialIn', 'VoiceConnector']]

### CallingName
- **Type**: typing.Optional[str]


# UpdatePhoneNumberResponse

### PhoneNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.PhoneNumber'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePhoneNumberSettingsRequest

### CallingName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRoomMembershipRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: typing.Optional[typing.Literal['Administrator', 'Member']]


# UpdateRoomMembershipResponse

### RoomMembership
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.RoomMembership'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRoomRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateRoomResponse

### Room
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.Room'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseType
- **Type**: <class 'NoneType'>

### UserType
- **Type**: typing.Optional[typing.Literal['PrivateUser', 'SharedDevice']]

### AlexaForBusinessMetadata
- **Type**: <class 'NoneType'>


# UpdateUserRequestItem

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseType
- **Type**: <class 'NoneType'>

### UserType
- **Type**: typing.Optional[typing.Literal['PrivateUser', 'SharedDevice']]

### AlexaForBusinessMetadata
- **Type**: <class 'NoneType'>


# UpdateUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserSettingsRequest

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### UserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.UserSettings'>
- **Required**: Yes


# User

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountId
- **Type**: typing.Optional[str]

### PrimaryEmail
- **Type**: typing.Optional[str]

### PrimaryProvisionedNumber
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### LicenseType
- **Type**: <class 'NoneType'>

### UserType
- **Type**: typing.Optional[typing.Literal['PrivateUser', 'SharedDevice']]

### UserRegistrationStatus
- **Type**: typing.Optional[typing.Literal['Registered', 'Suspended', 'Unregistered']]

### UserInvitationStatus
- **Type**: typing.Optional[typing.Literal['Accepted', 'Failed', 'Pending']]

### RegisteredOn
- **Type**: typing.Optional[datetime.datetime]

### InvitedOn
- **Type**: typing.Optional[datetime.datetime]

### AlexaForBusinessMetadata
- **Type**: <class 'NoneType'>

### PersonalPIN
- **Type**: typing.Optional[str]


# UserError

### UserId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'BadRequest', 'Conflict', 'Forbidden', 'NotFound', 'PhoneNumberAssociationsExist', 'PreconditionFailed', 'ResourceLimitExceeded', 'ServiceFailure', 'ServiceUnavailable', 'Throttled', 'Throttling', 'Unauthorized', 'Unprocessable', 'VoiceConnectorGroupAssociationsExist']]

### ErrorMessage
- **Type**: typing.Optional[str]


# UserSettings

### Telephony
- **Type**: <class 'aws_resource_validator.pydantic_models.chime.chime_classes.TelephonySettings'>
- **Required**: Yes


# VoiceConnectorSettings

### CdrBucket
- **Type**: typing.Optional[str]


