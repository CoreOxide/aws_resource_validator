# Chime Classes

# AccountSettingsTypeDef

### DisableRemoteControl
- **Type**: typing.Optional[bool]

### EnableDialOut
- **Type**: typing.Optional[bool]


# AccountTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_classes.SigninDelegateGroupTypeDef]]


# AlexaForBusinessMetadataTypeDef

### IsAlexaForBusinessEnabled
- **Type**: typing.Optional[bool]

### AlexaForBusinessRoomArn
- **Type**: typing.Optional[str]


# AssociatePhoneNumberWithUserRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateSigninDelegateGroupsWithAccountRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### SigninDelegateGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.SigninDelegateGroupTypeDef]
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateRoomMembershipRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes

### MembershipItemList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.MembershipItemTypeDef]
- **Required**: Yes


# BatchCreateRoomMembershipResponseTypeDef

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.MemberErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchDeletePhoneNumberRequestTypeDef

### PhoneNumberIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchDeletePhoneNumberResponseTypeDef

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.PhoneNumberErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchSuspendUserRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserIdList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchSuspendUserResponseTypeDef

### UserErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.UserErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUnsuspendUserRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserIdList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchUnsuspendUserResponseTypeDef

### UserErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.UserErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUpdatePhoneNumberRequestTypeDef

### UpdatePhoneNumberRequestItems
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.UpdatePhoneNumberRequestItemTypeDef]
- **Required**: Yes


# BatchUpdatePhoneNumberResponseTypeDef

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.PhoneNumberErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchUpdateUserRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateUserRequestItems
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.UpdateUserRequestItemTypeDef]
- **Required**: Yes


# BatchUpdateUserResponseTypeDef

### UserErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.UserErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BotTypeDef

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


# BusinessCallingSettingsTypeDef

### CdrBucket
- **Type**: typing.Optional[str]


# ConversationRetentionSettingsTypeDef

### RetentionDays
- **Type**: typing.Optional[int]


# CreateAccountRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAccountResponseTypeDef

### Account
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AccountTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBotRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]


# CreateBotResponseTypeDef

### Bot
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.BotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMeetingDialOutRequestTypeDef

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


# CreateMeetingDialOutResponseTypeDef

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePhoneNumberOrderRequestTypeDef

### ProductType
- **Type**: typing.Literal['BusinessCalling', 'SipMediaApplicationDialIn', 'VoiceConnector']
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CreatePhoneNumberOrderResponseTypeDef

### PhoneNumberOrder
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.PhoneNumberOrderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRoomMembershipRequestTypeDef

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


# CreateRoomMembershipResponseTypeDef

### RoomMembership
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.RoomMembershipTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRoomRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateRoomResponseTypeDef

### Room
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.RoomTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### UserType
- **Type**: typing.Optional[typing.Literal['PrivateUser', 'SharedDevice']]


# CreateUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAccountRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEventsConfigurationRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BotId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePhoneNumberRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoomMembershipRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoomRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociatePhoneNumberFromUserRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateSigninDelegateGroupsFromAccountRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventsConfigurationTypeDef

### BotId
- **Type**: typing.Optional[str]

### OutboundEventsHTTPSEndpoint
- **Type**: typing.Optional[str]

### LambdaFunctionArn
- **Type**: typing.Optional[str]


# GetAccountRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccountResponseTypeDef

### Account
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AccountTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccountSettingsRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccountSettingsResponseTypeDef

### AccountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AccountSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBotRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BotId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBotResponseTypeDef

### Bot
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.BotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventsConfigurationRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BotId
- **Type**: <class 'str'>
- **Required**: Yes


# GetEventsConfigurationResponseTypeDef

### EventsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.EventsConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGlobalSettingsResponseTypeDef

### BusinessCalling
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.BusinessCallingSettingsTypeDef'>
- **Required**: Yes

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.VoiceConnectorSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPhoneNumberOrderRequestTypeDef

### PhoneNumberOrderId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPhoneNumberOrderResponseTypeDef

### PhoneNumberOrder
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.PhoneNumberOrderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPhoneNumberRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPhoneNumberResponseTypeDef

### PhoneNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.PhoneNumberTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPhoneNumberSettingsResponseTypeDef

### CallingName
- **Type**: <class 'str'>
- **Required**: Yes

### CallingNameUpdatedTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRetentionSettingsRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRetentionSettingsResponseTypeDef

### RetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.RetentionSettingsTypeDef'>
- **Required**: Yes

### InitiateDeletionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRoomRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes


# GetRoomResponseTypeDef

### Room
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.RoomTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserSettingsRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserSettingsResponseTypeDef

### UserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.UserSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InviteTypeDef

### InviteId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Accepted', 'Failed', 'Pending']]

### EmailAddress
- **Type**: typing.Optional[str]

### EmailStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'NotSent', 'Sent']]


# InviteUsersRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserEmailList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### UserType
- **Type**: typing.Optional[typing.Literal['PrivateUser', 'SharedDevice']]


# InviteUsersResponseTypeDef

### Invites
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.InviteTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccountsRequestPaginateTypeDef

### Name
- **Type**: typing.Optional[str]

### UserEmail
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.PaginatorConfigTypeDef]


# ListAccountsRequestTypeDef

### Name
- **Type**: typing.Optional[str]

### UserEmail
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAccountsResponseTypeDef

### Accounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.AccountTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListBotsRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListBotsResponseTypeDef

### Bots
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.BotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumberOrdersRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPhoneNumberOrdersResponseTypeDef

### PhoneNumberOrders
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.PhoneNumberOrderTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPhoneNumbersRequestTypeDef

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


# ListPhoneNumbersResponseTypeDef

### PhoneNumbers
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.PhoneNumberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRoomMembershipsRequestTypeDef

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


# ListRoomMembershipsResponseTypeDef

### RoomMemberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.RoomMembershipTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListRoomsRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListRoomsResponseTypeDef

### Rooms
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.RoomTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSupportedPhoneNumberCountriesRequestTypeDef

### ProductType
- **Type**: typing.Literal['BusinessCalling', 'SipMediaApplicationDialIn', 'VoiceConnector']
- **Required**: Yes


# ListSupportedPhoneNumberCountriesResponseTypeDef

### PhoneNumberCountries
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.PhoneNumberCountryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUsersRequestPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserEmail
- **Type**: typing.Optional[str]

### UserType
- **Type**: typing.Optional[typing.Literal['PrivateUser', 'SharedDevice']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.PaginatorConfigTypeDef]


# ListUsersRequestTypeDef

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


# ListUsersResponseTypeDef

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.UserTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LogoutUserRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# MemberErrorTypeDef

### MemberId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'BadRequest', 'Conflict', 'Forbidden', 'NotFound', 'PhoneNumberAssociationsExist', 'PreconditionFailed', 'ResourceLimitExceeded', 'ServiceFailure', 'ServiceUnavailable', 'Throttled', 'Throttling', 'Unauthorized', 'Unprocessable', 'VoiceConnectorGroupAssociationsExist']]

### ErrorMessage
- **Type**: typing.Optional[str]


# MemberTypeDef

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


# MembershipItemTypeDef

### MemberId
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['Administrator', 'Member']]


# OrderedPhoneNumberTypeDef

### E164PhoneNumber
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Acquired', 'Failed', 'Processing']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PhoneNumberAssociationTypeDef

### Value
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[typing.Literal['AccountId', 'SipRuleId', 'UserId', 'VoiceConnectorGroupId', 'VoiceConnectorId']]

### AssociatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# PhoneNumberCapabilitiesTypeDef

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


# PhoneNumberCountryTypeDef

### CountryCode
- **Type**: typing.Optional[str]

### SupportedPhoneNumberTypes
- **Type**: typing.Optional[typing.List[typing.Literal['Local', 'TollFree']]]


# PhoneNumberErrorTypeDef

### PhoneNumberId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'BadRequest', 'Conflict', 'Forbidden', 'NotFound', 'PhoneNumberAssociationsExist', 'PreconditionFailed', 'ResourceLimitExceeded', 'ServiceFailure', 'ServiceUnavailable', 'Throttled', 'Throttling', 'Unauthorized', 'Unprocessable', 'VoiceConnectorGroupAssociationsExist']]

### ErrorMessage
- **Type**: typing.Optional[str]


# PhoneNumberOrderTypeDef

### PhoneNumberOrderId
- **Type**: typing.Optional[str]

### ProductType
- **Type**: typing.Optional[typing.Literal['BusinessCalling', 'SipMediaApplicationDialIn', 'VoiceConnector']]

### Status
- **Type**: typing.Optional[typing.Literal['Failed', 'Partial', 'Processing', 'Successful']]

### OrderedPhoneNumbers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_classes.OrderedPhoneNumberTypeDef]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# PhoneNumberTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutEventsConfigurationRequestTypeDef

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


# PutEventsConfigurationResponseTypeDef

### EventsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.EventsConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutRetentionSettingsRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.RetentionSettingsTypeDef'>
- **Required**: Yes


# PutRetentionSettingsResponseTypeDef

### RetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.RetentionSettingsTypeDef'>
- **Required**: Yes

### InitiateDeletionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RedactConversationMessageRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ConversationId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes


# RedactRoomMessageRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes


# RegenerateSecurityTokenRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BotId
- **Type**: <class 'str'>
- **Required**: Yes


# RegenerateSecurityTokenResponseTypeDef

### Bot
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.BotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResetPersonalPINRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# ResetPersonalPINResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResponseMetadataTypeDef

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


# RestorePhoneNumberRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# RestorePhoneNumberResponseTypeDef

### PhoneNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.PhoneNumberTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RetentionSettingsTypeDef

### RoomRetentionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.RoomRetentionSettingsTypeDef]

### ConversationRetentionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.ConversationRetentionSettingsTypeDef]


# RoomMembershipTypeDef

### RoomId
- **Type**: typing.Optional[str]

### Member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.MemberTypeDef]

### Role
- **Type**: typing.Optional[typing.Literal['Administrator', 'Member']]

### InvitedBy
- **Type**: typing.Optional[str]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# RoomRetentionSettingsTypeDef

### RetentionDays
- **Type**: typing.Optional[int]


# RoomTypeDef

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


# SearchAvailablePhoneNumbersRequestTypeDef

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


# SearchAvailablePhoneNumbersResponseTypeDef

### E164PhoneNumbers
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SigninDelegateGroupTypeDef

### GroupName
- **Type**: typing.Optional[str]


# TelephonySettingsTypeDef

### InboundCalling
- **Type**: <class 'bool'>
- **Required**: Yes

### OutboundCalling
- **Type**: <class 'bool'>
- **Required**: Yes

### SMS
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateAccountRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### DefaultLicense
- **Type**: typing.Optional[typing.Literal['Basic', 'Plus', 'Pro', 'ProTrial']]


# UpdateAccountResponseTypeDef

### Account
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AccountTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAccountSettingsRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AccountSettingsTypeDef'>
- **Required**: Yes


# UpdateBotRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BotId
- **Type**: <class 'str'>
- **Required**: Yes

### Disabled
- **Type**: typing.Optional[bool]


# UpdateBotResponseTypeDef

### Bot
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.BotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGlobalSettingsRequestTypeDef

### BusinessCalling
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.BusinessCallingSettingsTypeDef]

### VoiceConnector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.VoiceConnectorSettingsTypeDef]


# UpdatePhoneNumberRequestItemTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### ProductType
- **Type**: typing.Optional[typing.Literal['BusinessCalling', 'SipMediaApplicationDialIn', 'VoiceConnector']]

### CallingName
- **Type**: typing.Optional[str]


# UpdatePhoneNumberRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes

### ProductType
- **Type**: typing.Optional[typing.Literal['BusinessCalling', 'SipMediaApplicationDialIn', 'VoiceConnector']]

### CallingName
- **Type**: typing.Optional[str]


# UpdatePhoneNumberResponseTypeDef

### PhoneNumber
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.PhoneNumberTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePhoneNumberSettingsRequestTypeDef

### CallingName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRoomMembershipRequestTypeDef

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


# UpdateRoomMembershipResponseTypeDef

### RoomMembership
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.RoomMembershipTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRoomRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateRoomResponseTypeDef

### Room
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.RoomTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserRequestItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserSettingsRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### UserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.UserSettingsTypeDef'>
- **Required**: Yes


# UserErrorTypeDef

### UserId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'BadRequest', 'Conflict', 'Forbidden', 'NotFound', 'PhoneNumberAssociationsExist', 'PreconditionFailed', 'ResourceLimitExceeded', 'ServiceFailure', 'ServiceUnavailable', 'Throttled', 'Throttling', 'Unauthorized', 'Unprocessable', 'VoiceConnectorGroupAssociationsExist']]

### ErrorMessage
- **Type**: typing.Optional[str]


# UserSettingsTypeDef

### Telephony
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.TelephonySettingsTypeDef'>
- **Required**: Yes


# UserTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VoiceConnectorSettingsTypeDef

### CdrBucket
- **Type**: typing.Optional[str]


