# Pydantic Models in chime_classes

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


# AddressTypeDef

### streetName
- **Type**: typing.Optional[str]

### streetSuffix
- **Type**: typing.Optional[str]

### postDirectional
- **Type**: typing.Optional[str]

### preDirectional
- **Type**: typing.Optional[str]

### streetNumber
- **Type**: typing.Optional[str]

### city
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[str]

### postalCode
- **Type**: typing.Optional[str]

### postalCodePlus4
- **Type**: typing.Optional[str]

### country
- **Type**: typing.Optional[str]


# AlexaForBusinessMetadataTypeDef

### IsAlexaForBusinessEnabled
- **Type**: typing.Optional[bool]

### AlexaForBusinessRoomArn
- **Type**: typing.Optional[str]


# AppInstanceAdminSummaryTypeDef

### Admin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]


# AppInstanceAdminTypeDef

### Admin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]

### AppInstanceArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# AppInstanceRetentionSettingsTypeDef

### ChannelRetentionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.ChannelRetentionSettingsTypeDef]


# AppInstanceStreamingConfigurationTypeDef

### AppInstanceDataType
- **Type**: typing.Literal['Channel', 'ChannelMessage']
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# AppInstanceSummaryTypeDef

### AppInstanceArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]


# AppInstanceTypeDef

### AppInstanceArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# AppInstanceUserMembershipSummaryTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HIDDEN']]

### ReadMarkerTimestamp
- **Type**: typing.Optional[datetime.datetime]


# AppInstanceUserSummaryTypeDef

### AppInstanceUserArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]


# AppInstanceUserTypeDef

### AppInstanceUserArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Metadata
- **Type**: typing.Optional[str]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ArtifactsConfigurationTypeDef

### Audio
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AudioArtifactsConfigurationTypeDef'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.VideoArtifactsConfigurationTypeDef'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ContentArtifactsConfigurationTypeDef'>
- **Required**: Yes


# AssociatePhoneNumberWithUserRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes


# AssociatePhoneNumbersWithVoiceConnectorGroupRequestRequestTypeDef

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ForceAssociate
- **Type**: typing.Optional[bool]


# AssociatePhoneNumbersWithVoiceConnectorGroupResponseTypeDef

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.PhoneNumberErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociatePhoneNumbersWithVoiceConnectorRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ForceAssociate
- **Type**: typing.Optional[bool]


# AssociatePhoneNumbersWithVoiceConnectorResponseTypeDef

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.PhoneNumberErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateSigninDelegateGroupsWithAccountRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### SigninDelegateGroups
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.SigninDelegateGroupTypeDef]
- **Required**: Yes


# AttendeeTypeDef

### ExternalUserId
- **Type**: typing.Optional[str]

### AttendeeId
- **Type**: typing.Optional[str]

### JoinToken
- **Type**: typing.Optional[str]


# AudioArtifactsConfigurationTypeDef

### MuxType
- **Type**: typing.Literal['AudioOnly', 'AudioWithActiveSpeakerVideo']
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchChannelMembershipsTypeDef

### InvitedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HIDDEN']]

### Members
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]]

### ChannelArn
- **Type**: typing.Optional[str]


# BatchCreateAttendeeRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### Attendees
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.CreateAttendeeRequestItemTypeDef]
- **Required**: Yes


# BatchCreateAttendeeResponseTypeDef

### Attendees
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.AttendeeTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.CreateAttendeeErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchCreateChannelMembershipErrorTypeDef

### MemberArn
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'BadRequest', 'Conflict', 'Forbidden', 'NotFound', 'PhoneNumberAssociationsExist', 'PreconditionFailed', 'ResourceLimitExceeded', 'ServiceFailure', 'ServiceUnavailable', 'Throttled', 'Throttling', 'Unauthorized', 'Unprocessable', 'VoiceConnectorGroupAssociationsExist']]

### ErrorMessage
- **Type**: typing.Optional[str]


# BatchCreateChannelMembershipRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HIDDEN']]

### ChimeBearer
- **Type**: typing.Optional[str]


# BatchCreateChannelMembershipResponseTypeDef

### BatchChannelMemberships
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.BatchChannelMembershipsTypeDef'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.BatchCreateChannelMembershipErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchCreateRoomMembershipRequestRequestTypeDef

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


# BatchDeletePhoneNumberRequestRequestTypeDef

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


# BatchSuspendUserRequestRequestTypeDef

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


# BatchUnsuspendUserRequestRequestTypeDef

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


# BatchUpdatePhoneNumberRequestRequestTypeDef

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


# BatchUpdateUserRequestRequestTypeDef

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


# CandidateAddressTypeDef

### streetInfo
- **Type**: typing.Optional[str]

### streetNumber
- **Type**: typing.Optional[str]

### city
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[str]

### postalCode
- **Type**: typing.Optional[str]

### postalCodePlus4
- **Type**: typing.Optional[str]

### country
- **Type**: typing.Optional[str]


# ChannelBanSummaryTypeDef

### Member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]


# ChannelBanTypeDef

### Member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]

### ChannelArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]


# ChannelMembershipForAppInstanceUserSummaryTypeDef

### ChannelSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.ChannelSummaryTypeDef]

### AppInstanceUserMembershipSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.AppInstanceUserMembershipSummaryTypeDef]


# ChannelMembershipSummaryTypeDef

### Member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]


# ChannelMembershipTypeDef

### InvitedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HIDDEN']]

### Member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]

### ChannelArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ChannelMessageSummaryTypeDef

### MessageId
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['CONTROL', 'STANDARD']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastEditedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Sender
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]

### Redacted
- **Type**: typing.Optional[bool]


# ChannelMessageTypeDef

### ChannelArn
- **Type**: typing.Optional[str]

### MessageId
- **Type**: typing.Optional[str]

### Content
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['CONTROL', 'STANDARD']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastEditedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Sender
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]

### Redacted
- **Type**: typing.Optional[bool]

### Persistence
- **Type**: typing.Optional[typing.Literal['NON_PERSISTENT', 'PERSISTENT']]


# ChannelModeratedByAppInstanceUserSummaryTypeDef

### ChannelSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.ChannelSummaryTypeDef]


# ChannelModeratorSummaryTypeDef

### Moderator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]


# ChannelModeratorTypeDef

### Moderator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]

### ChannelArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]


# ChannelRetentionSettingsTypeDef

### RetentionDays
- **Type**: typing.Optional[int]


# ChannelSummaryTypeDef

### Name
- **Type**: typing.Optional[str]

### ChannelArn
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['RESTRICTED', 'UNRESTRICTED']]

### Privacy
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### Metadata
- **Type**: typing.Optional[str]

### LastMessageTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ChannelTypeDef

### Name
- **Type**: typing.Optional[str]

### ChannelArn
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['RESTRICTED', 'UNRESTRICTED']]

### Privacy
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### Metadata
- **Type**: typing.Optional[str]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastMessageTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ChimeSdkMeetingConfigurationTypeDef

### SourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.SourceConfigurationTypeDef]

### ArtifactsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.ArtifactsConfigurationTypeDef]


# ContentArtifactsConfigurationTypeDef

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### MuxType
- **Type**: typing.Optional[typing.Literal['ContentOnly']]


# ConversationRetentionSettingsTypeDef

### RetentionDays
- **Type**: typing.Optional[int]


# CreateAccountRequestRequestTypeDef

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


# CreateAppInstanceAdminRequestRequestTypeDef

### AppInstanceAdminArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAppInstanceAdminResponseTypeDef

### AppInstanceAdmin
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef'>
- **Required**: Yes

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppInstanceRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.TagTypeDef]]


# CreateAppInstanceResponseTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppInstanceUserRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceUserId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.TagTypeDef]]


# CreateAppInstanceUserResponseTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAttendeeErrorTypeDef

### ExternalUserId
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]


# CreateAttendeeRequestItemTypeDef

### ExternalUserId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.TagTypeDef]]


# CreateAttendeeRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalUserId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.TagTypeDef]]


# CreateAttendeeResponseTypeDef

### Attendee
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AttendeeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBotRequestRequestTypeDef

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


# CreateChannelBanRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# CreateChannelBanResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Member
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateChannelMembershipRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['DEFAULT', 'HIDDEN']
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# CreateChannelMembershipResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Member
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateChannelModeratorRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModeratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# CreateChannelModeratorResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModerator
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.IdentityTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateChannelRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Mode
- **Type**: typing.Optional[typing.Literal['RESTRICTED', 'UNRESTRICTED']]

### Privacy
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### Metadata
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.TagTypeDef]]

### ChimeBearer
- **Type**: typing.Optional[str]


# CreateChannelResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMediaCapturePipelineRequestRequestTypeDef

### SourceType
- **Type**: typing.Literal['ChimeSdkMeeting']
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SinkType
- **Type**: typing.Literal['S3Bucket']
- **Required**: Yes

### SinkArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### ChimeSdkMeetingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.ChimeSdkMeetingConfigurationTypeDef]


# CreateMediaCapturePipelineResponseTypeDef

### MediaCapturePipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.MediaCapturePipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMeetingDialOutRequestRequestTypeDef

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


# CreateMeetingRequestRequestTypeDef

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalMeetingId
- **Type**: typing.Optional[str]

### MeetingHostId
- **Type**: typing.Optional[str]

### MediaRegion
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.TagTypeDef]]

### NotificationsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.MeetingNotificationConfigurationTypeDef]


# CreateMeetingResponseTypeDef

### Meeting
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.MeetingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMeetingWithAttendeesRequestRequestTypeDef

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalMeetingId
- **Type**: typing.Optional[str]

### MeetingHostId
- **Type**: typing.Optional[str]

### MediaRegion
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.TagTypeDef]]

### NotificationsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.MeetingNotificationConfigurationTypeDef]

### Attendees
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.CreateAttendeeRequestItemTypeDef]]


# CreateMeetingWithAttendeesResponseTypeDef

### Meeting
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.MeetingTypeDef'>
- **Required**: Yes

### Attendees
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.AttendeeTypeDef]
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.CreateAttendeeErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePhoneNumberOrderRequestRequestTypeDef

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


# CreateProxySessionRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ParticipantPhoneNumbers
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Capabilities
- **Type**: typing.Sequence[typing.Literal['SMS', 'Voice']]
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### ExpiryMinutes
- **Type**: typing.Optional[int]

### NumberSelectionBehavior
- **Type**: typing.Optional[typing.Literal['AvoidSticky', 'PreferSticky']]

### GeoMatchLevel
- **Type**: typing.Optional[typing.Literal['AreaCode', 'Country']]

### GeoMatchParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.GeoMatchParamsTypeDef]


# CreateProxySessionResponseTypeDef

### ProxySession
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ProxySessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRoomMembershipRequestRequestTypeDef

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


# CreateRoomRequestRequestTypeDef

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


# CreateSipMediaApplicationCallRequestRequestTypeDef

### FromPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### ToPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SipHeaders
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSipMediaApplicationCallResponseTypeDef

### SipMediaApplicationCall
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.SipMediaApplicationCallTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSipMediaApplicationRequestRequestTypeDef

### AwsRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Endpoints
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.SipMediaApplicationEndpointTypeDef]
- **Required**: Yes


# CreateSipMediaApplicationResponseTypeDef

### SipMediaApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.SipMediaApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSipRuleRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TriggerType
- **Type**: typing.Literal['RequestUriHostname', 'ToPhoneNumber']
- **Required**: Yes

### TriggerValue
- **Type**: <class 'str'>
- **Required**: Yes

### TargetApplications
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.SipRuleTargetApplicationTypeDef]
- **Required**: Yes

### Disabled
- **Type**: typing.Optional[bool]


# CreateSipRuleResponseTypeDef

### SipRule
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.SipRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserRequestRequestTypeDef

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


# CreateVoiceConnectorGroupRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceConnectorItems
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.VoiceConnectorItemTypeDef]]


# CreateVoiceConnectorGroupResponseTypeDef

### VoiceConnectorGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.VoiceConnectorGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVoiceConnectorRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RequireEncryption
- **Type**: <class 'bool'>
- **Required**: Yes

### AwsRegion
- **Type**: typing.Optional[typing.Literal['us-east-1', 'us-west-2']]


# CreateVoiceConnectorResponseTypeDef

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.VoiceConnectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CredentialTypeDef

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# DNISEmergencyCallingConfigurationTypeDef

### EmergencyPhoneNumber
- **Type**: <class 'str'>
- **Required**: Yes

### CallingCountry
- **Type**: <class 'str'>
- **Required**: Yes

### TestPhoneNumber
- **Type**: typing.Optional[str]


# DeleteAccountRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppInstanceAdminRequestRequestTypeDef

### AppInstanceAdminArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppInstanceRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppInstanceStreamingConfigurationsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppInstanceUserRequestRequestTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAttendeeRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### AttendeeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelBanRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# DeleteChannelMembershipRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# DeleteChannelMessageRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# DeleteChannelModeratorRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModeratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# DeleteChannelRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# DeleteEventsConfigurationRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### BotId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMediaCapturePipelineRequestRequestTypeDef

### MediaPipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMeetingRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePhoneNumberRequestRequestTypeDef

### PhoneNumberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProxySessionRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ProxySessionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoomMembershipRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoomRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSipMediaApplicationRequestRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSipRuleRequestRequestTypeDef

### SipRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorGroupRequestRequestTypeDef

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorOriginationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorProxyRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorStreamingConfigurationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVoiceConnectorTerminationCredentialsRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Usernames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DeleteVoiceConnectorTerminationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceAdminRequestRequestTypeDef

### AppInstanceAdminArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceAdminResponseTypeDef

### AppInstanceAdmin
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AppInstanceAdminTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppInstanceRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceResponseTypeDef

### AppInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AppInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppInstanceUserRequestRequestTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceUserResponseTypeDef

### AppInstanceUser
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AppInstanceUserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChannelBanRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# DescribeChannelBanResponseTypeDef

### ChannelBan
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ChannelBanTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# DescribeChannelMembershipForAppInstanceUserResponseTypeDef

### ChannelMembership
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ChannelMembershipForAppInstanceUserSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChannelMembershipRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# DescribeChannelMembershipResponseTypeDef

### ChannelMembership
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ChannelMembershipTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# DescribeChannelModeratedByAppInstanceUserResponseTypeDef

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ChannelModeratedByAppInstanceUserSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChannelModeratorRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModeratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# DescribeChannelModeratorResponseTypeDef

### ChannelModerator
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ChannelModeratorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChannelRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# DescribeChannelResponseTypeDef

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ChannelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociatePhoneNumberFromUserRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociatePhoneNumbersFromVoiceConnectorGroupRequestRequestTypeDef

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisassociatePhoneNumbersFromVoiceConnectorGroupResponseTypeDef

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.PhoneNumberErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociatePhoneNumbersFromVoiceConnectorRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### E164PhoneNumbers
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisassociatePhoneNumbersFromVoiceConnectorResponseTypeDef

### PhoneNumberErrors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.PhoneNumberErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateSigninDelegateGroupsFromAccountRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# EmergencyCallingConfigurationTypeDef

### DNIS
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_classes.DNISEmergencyCallingConfigurationTypeDef]]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EngineTranscribeMedicalSettingsTypeDef

### LanguageCode
- **Type**: typing.Literal['en-US']
- **Required**: Yes

### Specialty
- **Type**: typing.Literal['CARDIOLOGY', 'NEUROLOGY', 'ONCOLOGY', 'PRIMARYCARE', 'RADIOLOGY', 'UROLOGY']
- **Required**: Yes

### Type
- **Type**: typing.Literal['CONVERSATION', 'DICTATION']
- **Required**: Yes

### VocabularyName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[typing.Literal['ap-southeast-2', 'auto', 'ca-central-1', 'eu-west-1', 'us-east-1', 'us-east-2', 'us-west-2']]

### ContentIdentificationType
- **Type**: typing.Optional[typing.Literal['PHI']]


# EngineTranscribeSettingsTypeDef

### LanguageCode
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-US', 'es-US', 'fr-CA', 'fr-FR', 'hi-IN', 'it-IT', 'ja-JP', 'ko-KR', 'pt-BR', 'th-TH', 'zh-CN']]

### VocabularyFilterMethod
- **Type**: typing.Optional[typing.Literal['mask', 'remove', 'tag']]

### VocabularyFilterName
- **Type**: typing.Optional[str]

### VocabularyName
- **Type**: typing.Optional[str]

### Region
- **Type**: typing.Optional[typing.Literal['ap-northeast-1', 'ap-northeast-2', 'ap-southeast-2', 'auto', 'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-west-2']]

### EnablePartialResultsStabilization
- **Type**: typing.Optional[bool]

### PartialResultsStability
- **Type**: typing.Optional[typing.Literal['high', 'low', 'medium']]

### ContentIdentificationType
- **Type**: typing.Optional[typing.Literal['PII']]

### ContentRedactionType
- **Type**: typing.Optional[typing.Literal['PII']]

### PiiEntityTypes
- **Type**: typing.Optional[str]

### LanguageModelName
- **Type**: typing.Optional[str]

### IdentifyLanguage
- **Type**: typing.Optional[bool]

### LanguageOptions
- **Type**: typing.Optional[str]

### PreferredLanguage
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-US', 'es-US', 'fr-CA', 'fr-FR', 'hi-IN', 'it-IT', 'ja-JP', 'ko-KR', 'pt-BR', 'th-TH', 'zh-CN']]

### VocabularyNames
- **Type**: typing.Optional[str]

### VocabularyFilterNames
- **Type**: typing.Optional[str]


# EventsConfigurationTypeDef

### BotId
- **Type**: typing.Optional[str]

### OutboundEventsHTTPSEndpoint
- **Type**: typing.Optional[str]

### LambdaFunctionArn
- **Type**: typing.Optional[str]


# GeoMatchParamsTypeDef

### Country
- **Type**: <class 'str'>
- **Required**: Yes

### AreaCode
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccountRequestRequestTypeDef

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


# GetAccountSettingsRequestRequestTypeDef

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


# GetAppInstanceRetentionSettingsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppInstanceRetentionSettingsResponseTypeDef

### AppInstanceRetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AppInstanceRetentionSettingsTypeDef'>
- **Required**: Yes

### InitiateDeletionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAppInstanceStreamingConfigurationsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppInstanceStreamingConfigurationsResponseTypeDef

### AppInstanceStreamingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.AppInstanceStreamingConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAttendeeRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### AttendeeId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAttendeeResponseTypeDef

### Attendee
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AttendeeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBotRequestRequestTypeDef

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


# GetChannelMessageRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# GetChannelMessageResponseTypeDef

### ChannelMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ChannelMessageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEventsConfigurationRequestRequestTypeDef

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


# GetMediaCapturePipelineRequestRequestTypeDef

### MediaPipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaCapturePipelineResponseTypeDef

### MediaCapturePipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.MediaCapturePipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMeetingRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMeetingResponseTypeDef

### Meeting
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.MeetingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMessagingSessionEndpointResponseTypeDef

### Endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.MessagingSessionEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPhoneNumberOrderRequestRequestTypeDef

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


# GetPhoneNumberRequestRequestTypeDef

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


# GetProxySessionRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ProxySessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetProxySessionResponseTypeDef

### ProxySession
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ProxySessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRetentionSettingsRequestRequestTypeDef

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


# GetRoomRequestRequestTypeDef

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


# GetSipMediaApplicationLoggingConfigurationRequestRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSipMediaApplicationLoggingConfigurationResponseTypeDef

### SipMediaApplicationLoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.SipMediaApplicationLoggingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSipMediaApplicationRequestRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSipMediaApplicationResponseTypeDef

### SipMediaApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.SipMediaApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSipRuleRequestRequestTypeDef

### SipRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSipRuleResponseTypeDef

### SipRule
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.SipRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserRequestRequestTypeDef

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


# GetUserSettingsRequestRequestTypeDef

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


# GetVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorEmergencyCallingConfigurationResponseTypeDef

### EmergencyCallingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.EmergencyCallingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorGroupRequestRequestTypeDef

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorGroupResponseTypeDef

### VoiceConnectorGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.VoiceConnectorGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorLoggingConfigurationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorLoggingConfigurationResponseTypeDef

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.LoggingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorOriginationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorOriginationResponseTypeDef

### Origination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.OriginationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorProxyRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorProxyResponseTypeDef

### Proxy
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ProxyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorResponseTypeDef

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.VoiceConnectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorStreamingConfigurationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorStreamingConfigurationResponseTypeDef

### StreamingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.StreamingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorTerminationHealthRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorTerminationHealthResponseTypeDef

### TerminationHealth
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.TerminationHealthTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceConnectorTerminationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceConnectorTerminationResponseTypeDef

### Termination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.TerminationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdentityTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# InviteTypeDef

### InviteId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Accepted', 'Failed', 'Pending']]

### EmailAddress
- **Type**: typing.Optional[str]

### EmailStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'NotSent', 'Sent']]


# InviteUsersRequestRequestTypeDef

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


# ListAccountsRequestListAccountsPaginateTypeDef

### Name
- **Type**: typing.Optional[str]

### UserEmail
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.PaginatorConfigTypeDef]


# ListAccountsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppInstanceAdminsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstanceAdminsResponseTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceAdmins
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.AppInstanceAdminSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppInstanceUsersRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstanceUsersResponseTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceUsers
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.AppInstanceUserSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppInstancesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstancesResponseTypeDef

### AppInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.AppInstanceSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAttendeeTagsRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### AttendeeId
- **Type**: <class 'str'>
- **Required**: Yes


# ListAttendeeTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAttendeesRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAttendeesResponseTypeDef

### Attendees
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.AttendeeTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBotsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelBansRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ChimeBearer
- **Type**: typing.Optional[str]


# ListChannelBansResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelBans
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.ChannelBanSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef

### AppInstanceUserArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ChimeBearer
- **Type**: typing.Optional[str]


# ListChannelMembershipsForAppInstanceUserResponseTypeDef

### ChannelMemberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.ChannelMembershipForAppInstanceUserSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelMembershipsRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HIDDEN']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ChimeBearer
- **Type**: typing.Optional[str]


# ListChannelMembershipsResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelMemberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.ChannelMembershipSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelMessagesRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### NotBefore
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### NotAfter
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ChimeBearer
- **Type**: typing.Optional[str]


# ListChannelMessagesResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelMessages
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.ChannelMessageSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelModeratorsRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ChimeBearer
- **Type**: typing.Optional[str]


# ListChannelModeratorsResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModerators
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.ChannelModeratorSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef

### AppInstanceUserArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ChimeBearer
- **Type**: typing.Optional[str]


# ListChannelsModeratedByAppInstanceUserResponseTypeDef

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.ChannelModeratedByAppInstanceUserSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Privacy
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ChimeBearer
- **Type**: typing.Optional[str]


# ListChannelsResponseTypeDef

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.ChannelSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMediaCapturePipelinesRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMediaCapturePipelinesResponseTypeDef

### MediaCapturePipelines
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.MediaCapturePipelineTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMeetingTagsRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes


# ListMeetingTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMeetingsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMeetingsResponseTypeDef

### Meetings
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.MeetingTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPhoneNumberOrdersRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPhoneNumberOrdersResponseTypeDef

### PhoneNumberOrders
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.PhoneNumberOrderTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPhoneNumbersRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListProxySessionsRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['Closed', 'InProgress', 'Open']]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListProxySessionsResponseTypeDef

### ProxySessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.ProxySessionTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRoomMembershipsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRoomsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSipMediaApplicationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSipMediaApplicationsResponseTypeDef

### SipMediaApplications
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.SipMediaApplicationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSipRulesRequestRequestTypeDef

### SipMediaApplicationId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSipRulesResponseTypeDef

### SipRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.SipRuleTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSupportedPhoneNumberCountriesRequestRequestTypeDef

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


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUsersRequestListUsersPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserEmail
- **Type**: typing.Optional[str]

### UserType
- **Type**: typing.Optional[typing.Literal['PrivateUser', 'SharedDevice']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.PaginatorConfigTypeDef]


# ListUsersRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVoiceConnectorGroupsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListVoiceConnectorGroupsResponseTypeDef

### VoiceConnectorGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.VoiceConnectorGroupTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVoiceConnectorTerminationCredentialsRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes


# ListVoiceConnectorTerminationCredentialsResponseTypeDef

### Usernames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVoiceConnectorsRequestRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListVoiceConnectorsResponseTypeDef

### VoiceConnectors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.VoiceConnectorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoggingConfigurationTypeDef

### EnableSIPLogs
- **Type**: typing.Optional[bool]

### EnableMediaMetricLogs
- **Type**: typing.Optional[bool]


# LogoutUserRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# MediaCapturePipelineTypeDef

### MediaPipelineId
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['ChimeSdkMeeting']]

### SourceArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Initializing', 'Stopped', 'Stopping']]

### SinkType
- **Type**: typing.Optional[typing.Literal['S3Bucket']]

### SinkArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ChimeSdkMeetingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.ChimeSdkMeetingConfigurationTypeDef]


# MediaPlacementTypeDef

### AudioHostUrl
- **Type**: typing.Optional[str]

### AudioFallbackUrl
- **Type**: typing.Optional[str]

### ScreenDataUrl
- **Type**: typing.Optional[str]

### ScreenSharingUrl
- **Type**: typing.Optional[str]

### ScreenViewingUrl
- **Type**: typing.Optional[str]

### SignalingUrl
- **Type**: typing.Optional[str]

### TurnControlUrl
- **Type**: typing.Optional[str]

### EventIngestionUrl
- **Type**: typing.Optional[str]


# MeetingNotificationConfigurationTypeDef

### SnsTopicArn
- **Type**: typing.Optional[str]

### SqsQueueArn
- **Type**: typing.Optional[str]


# MeetingTypeDef

### MeetingId
- **Type**: typing.Optional[str]

### ExternalMeetingId
- **Type**: typing.Optional[str]

### MediaPlacement
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.MediaPlacementTypeDef]

### MediaRegion
- **Type**: typing.Optional[str]


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


# MessagingSessionEndpointTypeDef

### Url
- **Type**: typing.Optional[str]


# OrderedPhoneNumberTypeDef

### E164PhoneNumber
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Acquired', 'Failed', 'Processing']]


# OriginationRouteTypeDef

### Host
- **Type**: typing.Optional[str]

### Port
- **Type**: typing.Optional[int]

### Protocol
- **Type**: typing.Optional[typing.Literal['TCP', 'UDP']]

### Priority
- **Type**: typing.Optional[int]

### Weight
- **Type**: typing.Optional[int]


# OriginationTypeDef

### Routes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_classes.OriginationRouteTypeDef]]

### Disabled
- **Type**: typing.Optional[bool]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParticipantTypeDef

### PhoneNumber
- **Type**: typing.Optional[str]

### ProxyPhoneNumber
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.PhoneNumberCapabilitiesTypeDef]

### Associations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_classes.PhoneNumberAssociationTypeDef]]

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


# ProxySessionTypeDef

### VoiceConnectorId
- **Type**: typing.Optional[str]

### ProxySessionId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Closed', 'InProgress', 'Open']]

### ExpiryMinutes
- **Type**: typing.Optional[int]

### Capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['SMS', 'Voice']]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### EndedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Participants
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_classes.ParticipantTypeDef]]

### NumberSelectionBehavior
- **Type**: typing.Optional[typing.Literal['AvoidSticky', 'PreferSticky']]

### GeoMatchLevel
- **Type**: typing.Optional[typing.Literal['AreaCode', 'Country']]

### GeoMatchParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.GeoMatchParamsTypeDef]


# ProxyTypeDef

### DefaultSessionExpiryMinutes
- **Type**: typing.Optional[int]

### Disabled
- **Type**: typing.Optional[bool]

### FallBackPhoneNumber
- **Type**: typing.Optional[str]

### PhoneNumberCountries
- **Type**: typing.Optional[typing.List[str]]


# PutAppInstanceRetentionSettingsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceRetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AppInstanceRetentionSettingsTypeDef'>
- **Required**: Yes


# PutAppInstanceRetentionSettingsResponseTypeDef

### AppInstanceRetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AppInstanceRetentionSettingsTypeDef'>
- **Required**: Yes

### InitiateDeletionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutAppInstanceStreamingConfigurationsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceStreamingConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.AppInstanceStreamingConfigurationTypeDef]
- **Required**: Yes


# PutAppInstanceStreamingConfigurationsResponseTypeDef

### AppInstanceStreamingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.AppInstanceStreamingConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutEventsConfigurationRequestRequestTypeDef

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


# PutRetentionSettingsRequestRequestTypeDef

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


# PutSipMediaApplicationLoggingConfigurationRequestRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### SipMediaApplicationLoggingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.SipMediaApplicationLoggingConfigurationTypeDef]


# PutSipMediaApplicationLoggingConfigurationResponseTypeDef

### SipMediaApplicationLoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.SipMediaApplicationLoggingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorEmergencyCallingConfigurationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### EmergencyCallingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.EmergencyCallingConfigurationTypeDef'>
- **Required**: Yes


# PutVoiceConnectorEmergencyCallingConfigurationResponseTypeDef

### EmergencyCallingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.EmergencyCallingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorLoggingConfigurationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.LoggingConfigurationTypeDef'>
- **Required**: Yes


# PutVoiceConnectorLoggingConfigurationResponseTypeDef

### LoggingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.LoggingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorOriginationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Origination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.OriginationTypeDef'>
- **Required**: Yes


# PutVoiceConnectorOriginationResponseTypeDef

### Origination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.OriginationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorProxyRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultSessionExpiryMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### PhoneNumberPoolCountries
- **Type**: typing.Sequence[str]
- **Required**: Yes

### FallBackPhoneNumber
- **Type**: typing.Optional[str]

### Disabled
- **Type**: typing.Optional[bool]


# PutVoiceConnectorProxyResponseTypeDef

### Proxy
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ProxyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorStreamingConfigurationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.StreamingConfigurationTypeDef'>
- **Required**: Yes


# PutVoiceConnectorStreamingConfigurationResponseTypeDef

### StreamingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.StreamingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutVoiceConnectorTerminationCredentialsRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Credentials
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.CredentialTypeDef]]


# PutVoiceConnectorTerminationRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Termination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.TerminationTypeDef'>
- **Required**: Yes


# PutVoiceConnectorTerminationResponseTypeDef

### Termination
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.TerminationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RedactChannelMessageRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# RedactChannelMessageResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RedactConversationMessageRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### ConversationId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes


# RedactRoomMessageRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### RoomId
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes


# RegenerateSecurityTokenRequestRequestTypeDef

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


# ResetPersonalPINRequestRequestTypeDef

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

### HostId
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


# RestorePhoneNumberRequestRequestTypeDef

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


# SearchAvailablePhoneNumbersRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SelectedVideoStreamsTypeDef

### AttendeeIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ExternalUserIds
- **Type**: typing.Optional[typing.Sequence[str]]


# SendChannelMessageRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['CONTROL', 'STANDARD']
- **Required**: Yes

### Persistence
- **Type**: typing.Literal['NON_PERSISTENT', 'PERSISTENT']
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Optional[str]

### ChimeBearer
- **Type**: typing.Optional[str]


# SendChannelMessageResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SigninDelegateGroupTypeDef

### GroupName
- **Type**: typing.Optional[str]


# SipMediaApplicationCallTypeDef

### TransactionId
- **Type**: typing.Optional[str]


# SipMediaApplicationEndpointTypeDef

### LambdaArn
- **Type**: typing.Optional[str]


# SipMediaApplicationLoggingConfigurationTypeDef

### EnableSipMediaApplicationMessageLogs
- **Type**: typing.Optional[bool]


# SipMediaApplicationTypeDef

### SipMediaApplicationId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_classes.SipMediaApplicationEndpointTypeDef]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# SipRuleTargetApplicationTypeDef

### SipMediaApplicationId
- **Type**: typing.Optional[str]

### Priority
- **Type**: typing.Optional[int]

### AwsRegion
- **Type**: typing.Optional[str]


# SipRuleTypeDef

### SipRuleId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Disabled
- **Type**: typing.Optional[bool]

### TriggerType
- **Type**: typing.Optional[typing.Literal['RequestUriHostname', 'ToPhoneNumber']]

### TriggerValue
- **Type**: typing.Optional[str]

### TargetApplications
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_classes.SipRuleTargetApplicationTypeDef]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# SourceConfigurationTypeDef

### SelectedVideoStreams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.SelectedVideoStreamsTypeDef]


# StartMeetingTranscriptionRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### TranscriptionConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.TranscriptionConfigurationTypeDef'>
- **Required**: Yes


# StopMeetingTranscriptionRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes


# StreamingConfigurationTypeDef

### DataRetentionInHours
- **Type**: <class 'int'>
- **Required**: Yes

### Disabled
- **Type**: typing.Optional[bool]

### StreamingNotificationTargets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_classes.StreamingNotificationTargetTypeDef]]


# StreamingNotificationTargetTypeDef

### NotificationTarget
- **Type**: typing.Literal['EventBridge', 'SNS', 'SQS']
- **Required**: Yes


# TagAttendeeRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### AttendeeId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.TagTypeDef]
- **Required**: Yes


# TagMeetingRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.TagTypeDef]
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


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


# TerminationHealthTypeDef

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### Source
- **Type**: typing.Optional[str]


# TerminationTypeDef

### CpsLimit
- **Type**: typing.Optional[int]

### DefaultPhoneNumber
- **Type**: typing.Optional[str]

### CallingRegions
- **Type**: typing.Optional[typing.List[str]]

### CidrAllowedList
- **Type**: typing.Optional[typing.List[str]]

### Disabled
- **Type**: typing.Optional[bool]


# TranscriptionConfigurationTypeDef

### EngineTranscribeSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.EngineTranscribeSettingsTypeDef]

### EngineTranscribeMedicalSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.EngineTranscribeMedicalSettingsTypeDef]


# UntagAttendeeRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### AttendeeId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagMeetingRequestRequestTypeDef

### MeetingId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccountRequestRequestTypeDef

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


# UpdateAccountSettingsRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### AccountSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AccountSettingsTypeDef'>
- **Required**: Yes


# UpdateAppInstanceRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Optional[str]


# UpdateAppInstanceResponseTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAppInstanceUserRequestRequestTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Optional[str]


# UpdateAppInstanceUserResponseTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBotRequestRequestTypeDef

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


# UpdateChannelMessageRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]

### ChimeBearer
- **Type**: typing.Optional[str]


# UpdateChannelMessageResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChannelReadMarkerRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]


# UpdateChannelReadMarkerResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChannelRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Mode
- **Type**: typing.Literal['RESTRICTED', 'UNRESTRICTED']
- **Required**: Yes

### Metadata
- **Type**: typing.Optional[str]

### ChimeBearer
- **Type**: typing.Optional[str]


# UpdateChannelResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGlobalSettingsRequestRequestTypeDef

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


# UpdatePhoneNumberRequestRequestTypeDef

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


# UpdatePhoneNumberSettingsRequestRequestTypeDef

### CallingName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateProxySessionRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### ProxySessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Capabilities
- **Type**: typing.Sequence[typing.Literal['SMS', 'Voice']]
- **Required**: Yes

### ExpiryMinutes
- **Type**: typing.Optional[int]


# UpdateProxySessionResponseTypeDef

### ProxySession
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ProxySessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRoomMembershipRequestRequestTypeDef

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


# UpdateRoomRequestRequestTypeDef

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


# UpdateSipMediaApplicationCallRequestRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### TransactionId
- **Type**: <class 'str'>
- **Required**: Yes

### Arguments
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UpdateSipMediaApplicationCallResponseTypeDef

### SipMediaApplicationCall
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.SipMediaApplicationCallTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSipMediaApplicationRequestRequestTypeDef

### SipMediaApplicationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.SipMediaApplicationEndpointTypeDef]]


# UpdateSipMediaApplicationResponseTypeDef

### SipMediaApplication
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.SipMediaApplicationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSipRuleRequestRequestTypeDef

### SipRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Disabled
- **Type**: typing.Optional[bool]

### TargetApplications
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.SipRuleTargetApplicationTypeDef]]


# UpdateSipRuleResponseTypeDef

### SipRule
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.SipRuleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserRequestItemTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### LicenseType
- **Type**: <class 'NoneType'>

### UserType
- **Type**: typing.Optional[typing.Literal['PrivateUser', 'SharedDevice']]

### AlexaForBusinessMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.AlexaForBusinessMetadataTypeDef]


# UpdateUserRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.AlexaForBusinessMetadataTypeDef]


# UpdateUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserSettingsRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### UserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.UserSettingsTypeDef'>
- **Required**: Yes


# UpdateVoiceConnectorGroupRequestRequestTypeDef

### VoiceConnectorGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceConnectorItems
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_classes.VoiceConnectorItemTypeDef]
- **Required**: Yes


# UpdateVoiceConnectorGroupResponseTypeDef

### VoiceConnectorGroup
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.VoiceConnectorGroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVoiceConnectorRequestRequestTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### RequireEncryption
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateVoiceConnectorResponseTypeDef

### VoiceConnector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.VoiceConnectorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_classes.AlexaForBusinessMetadataTypeDef]

### PersonalPIN
- **Type**: typing.Optional[str]


# ValidateE911AddressRequestRequestTypeDef

### AwsAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### StreetNumber
- **Type**: <class 'str'>
- **Required**: Yes

### StreetInfo
- **Type**: <class 'str'>
- **Required**: Yes

### City
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: <class 'str'>
- **Required**: Yes

### Country
- **Type**: <class 'str'>
- **Required**: Yes

### PostalCode
- **Type**: <class 'str'>
- **Required**: Yes


# ValidateE911AddressResponseTypeDef

### ValidationResult
- **Type**: <class 'int'>
- **Required**: Yes

### AddressExternalId
- **Type**: <class 'str'>
- **Required**: Yes

### Address
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.AddressTypeDef'>
- **Required**: Yes

### CandidateAddressList
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_classes.CandidateAddressTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VideoArtifactsConfigurationTypeDef

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### MuxType
- **Type**: typing.Optional[typing.Literal['VideoOnly']]


# VoiceConnectorGroupTypeDef

### VoiceConnectorGroupId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### VoiceConnectorItems
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_classes.VoiceConnectorItemTypeDef]]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### VoiceConnectorGroupArn
- **Type**: typing.Optional[str]


# VoiceConnectorItemTypeDef

### VoiceConnectorId
- **Type**: <class 'str'>
- **Required**: Yes

### Priority
- **Type**: <class 'int'>
- **Required**: Yes


# VoiceConnectorSettingsTypeDef

### CdrBucket
- **Type**: typing.Optional[str]


# VoiceConnectorTypeDef

### VoiceConnectorId
- **Type**: typing.Optional[str]

### AwsRegion
- **Type**: typing.Optional[typing.Literal['us-east-1', 'us-west-2']]

### Name
- **Type**: typing.Optional[str]

### OutboundHostName
- **Type**: typing.Optional[str]

### RequireEncryption
- **Type**: typing.Optional[bool]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### VoiceConnectorArn
- **Type**: typing.Optional[str]


