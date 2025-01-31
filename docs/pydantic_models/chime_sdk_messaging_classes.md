# Chime Sdk Messaging Classes

# AppInstanceUserMembershipSummaryTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HIDDEN']]

### ReadMarkerTimestamp
- **Type**: typing.Optional[datetime.datetime]

### SubChannelId
- **Type**: typing.Optional[str]


# AssociateChannelFlowRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchChannelMembershipsTypeDef

### InvitedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HIDDEN']]

### Members
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]]

### ChannelArn
- **Type**: typing.Optional[str]

### SubChannelId
- **Type**: typing.Optional[str]


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

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HIDDEN']]

### SubChannelId
- **Type**: typing.Optional[str]


# BatchCreateChannelMembershipResponseTypeDef

### BatchChannelMemberships
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.BatchChannelMembershipsTypeDef'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.BatchCreateChannelMembershipErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChannelAssociatedWithFlowSummaryTypeDef

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


# ChannelBanSummaryTypeDef

### Member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]


# ChannelBanTypeDef

### Member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]

### ChannelArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]


# ChannelFlowCallbackRequestRequestTypeDef

### CallbackId
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageCallbackTypeDef'>
- **Required**: Yes

### DeleteResource
- **Type**: typing.Optional[bool]


# ChannelFlowCallbackResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### CallbackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChannelFlowSummaryTypeDef

### ChannelFlowArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Processors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ProcessorTypeDef]]


# ChannelFlowTypeDef

### ChannelFlowArn
- **Type**: typing.Optional[str]

### Processors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ProcessorTypeDef]]

### Name
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ChannelMembershipForAppInstanceUserSummaryTypeDef

### ChannelSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelSummaryTypeDef]

### AppInstanceUserMembershipSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.AppInstanceUserMembershipSummaryTypeDef]


# ChannelMembershipPreferencesTypeDef

### PushNotifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.PushNotificationPreferencesTypeDef]


# ChannelMembershipSummaryTypeDef

### Member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]


# ChannelMembershipTypeDef

### InvitedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]

### Type
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HIDDEN']]

### Member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]

### ChannelArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### SubChannelId
- **Type**: typing.Optional[str]


# ChannelMessageCallbackTypeDef

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]

### PushNotification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.PushNotificationConfigurationTypeDef]

### MessageAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.MessageAttributeValueTypeDef]]

### SubChannelId
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]


# ChannelMessageStatusStructureTypeDef

### Value
- **Type**: typing.Optional[typing.Literal['DENIED', 'FAILED', 'PENDING', 'SENT']]

### Detail
- **Type**: typing.Optional[str]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]

### Redacted
- **Type**: typing.Optional[bool]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageStatusStructureTypeDef]

### MessageAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.MessageAttributeValueTypeDef]]

### ContentType
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.TargetTypeDef]]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]

### Redacted
- **Type**: typing.Optional[bool]

### Persistence
- **Type**: typing.Optional[typing.Literal['NON_PERSISTENT', 'PERSISTENT']]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageStatusStructureTypeDef]

### MessageAttributes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.MessageAttributeValueTypeDef]]

### SubChannelId
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.TargetTypeDef]]


# ChannelModeratedByAppInstanceUserSummaryTypeDef

### ChannelSummary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelSummaryTypeDef]


# ChannelModeratorSummaryTypeDef

### Moderator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]


# ChannelModeratorTypeDef

### Moderator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]

### ChannelArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastMessageTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ChannelFlowArn
- **Type**: typing.Optional[str]

### ElasticChannelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ElasticChannelConfigurationTypeDef]

### ExpirationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ExpirationSettingsTypeDef]


# CreateChannelBanRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# CreateChannelBanResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Member
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateChannelFlowRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Processors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ProcessorTypeDef]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.TagTypeDef]]


# CreateChannelFlowResponseTypeDef

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'str'>
- **Required**: Yes

### SubChannelId
- **Type**: typing.Optional[str]


# CreateChannelMembershipResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Member
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef'>
- **Required**: Yes

### SubChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateChannelModeratorRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModeratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# CreateChannelModeratorResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModerator
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
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

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### Mode
- **Type**: typing.Optional[typing.Literal['RESTRICTED', 'UNRESTRICTED']]

### Privacy
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### Metadata
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.TagTypeDef]]

### ChannelId
- **Type**: typing.Optional[str]

### MemberArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ModeratorArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ElasticChannelConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ElasticChannelConfigurationTypeDef]

### ExpirationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ExpirationSettingsTypeDef]


# CreateChannelResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteChannelBanRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelFlowRequestRequestTypeDef

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelMembershipRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### SubChannelId
- **Type**: typing.Optional[str]


# DeleteChannelMessageRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### SubChannelId
- **Type**: typing.Optional[str]


# DeleteChannelModeratorRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModeratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMessagingStreamingConfigurationsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelBanRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelBanResponseTypeDef

### ChannelBan
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelBanTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChannelFlowRequestRequestTypeDef

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelFlowResponseTypeDef

### ChannelFlow
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelFlowTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChannelMembershipForAppInstanceUserRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelMembershipForAppInstanceUserResponseTypeDef

### ChannelMembership
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipForAppInstanceUserSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChannelMembershipRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### SubChannelId
- **Type**: typing.Optional[str]


# DescribeChannelMembershipResponseTypeDef

### ChannelMembership
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChannelModeratedByAppInstanceUserRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelModeratedByAppInstanceUserResponseTypeDef

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelModeratedByAppInstanceUserSummaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChannelModeratorRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModeratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelModeratorResponseTypeDef

### ChannelModerator
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelModeratorTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChannelRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelResponseTypeDef

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateChannelFlowRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# ElasticChannelConfigurationTypeDef

### MaximumSubChannels
- **Type**: <class 'int'>
- **Required**: Yes

### TargetMembershipsPerSubChannel
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumMembershipPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ExpirationSettingsTypeDef

### ExpirationDays
- **Type**: <class 'int'>
- **Required**: Yes

### ExpirationCriterion
- **Type**: typing.Literal['CREATED_TIMESTAMP', 'LAST_MESSAGE_TIMESTAMP']
- **Required**: Yes


# GetChannelMembershipPreferencesRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelMembershipPreferencesResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Member
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef'>
- **Required**: Yes

### Preferences
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipPreferencesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChannelMessageRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### SubChannelId
- **Type**: typing.Optional[str]


# GetChannelMessageResponseTypeDef

### ChannelMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChannelMessageStatusRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### SubChannelId
- **Type**: typing.Optional[str]


# GetChannelMessageStatusResponseTypeDef

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageStatusStructureTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMessagingSessionEndpointResponseTypeDef

### Endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.MessagingSessionEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMessagingStreamingConfigurationsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetMessagingStreamingConfigurationsResponseTypeDef

### StreamingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.StreamingConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdentityTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# LambdaConfigurationTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationType
- **Type**: typing.Literal['ASYNC']
- **Required**: Yes


# ListChannelBansRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelBansResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelBans
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelBanSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelFlowsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelFlowsResponseTypeDef

### ChannelFlows
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelFlowSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelMembershipsForAppInstanceUserRequestRequestTypeDef

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceUserArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelMembershipsForAppInstanceUserResponseTypeDef

### ChannelMemberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipForAppInstanceUserSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelMembershipsRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'HIDDEN']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SubChannelId
- **Type**: typing.Optional[str]


# ListChannelMembershipsResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelMemberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelMessagesRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
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

### SubChannelId
- **Type**: typing.Optional[str]


# ListChannelMessagesResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelMessages
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageSummaryTypeDef]
- **Required**: Yes

### SubChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelModeratorsRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelModeratorsResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModerators
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelModeratorSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelsAssociatedWithChannelFlowRequestRequestTypeDef

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsAssociatedWithChannelFlowResponseTypeDef

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelAssociatedWithFlowSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelsModeratedByAppInstanceUserRequestRequestTypeDef

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceUserArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsModeratedByAppInstanceUserResponseTypeDef

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelModeratedByAppInstanceUserSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### Privacy
- **Type**: typing.Optional[typing.Literal['PRIVATE', 'PUBLIC']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsResponseTypeDef

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSubChannelsRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSubChannelsResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubChannels
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.SubChannelSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MessageAttributeValueTypeDef

### StringValues
- **Type**: typing.Optional[typing.Sequence[str]]


# MessagingSessionEndpointTypeDef

### Url
- **Type**: typing.Optional[str]


# ProcessorConfigurationTypeDef

### Lambda
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.LambdaConfigurationTypeDef'>
- **Required**: Yes


# ProcessorTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ProcessorConfigurationTypeDef'>
- **Required**: Yes

### ExecutionOrder
- **Type**: <class 'int'>
- **Required**: Yes

### FallbackAction
- **Type**: typing.Literal['ABORT', 'CONTINUE']
- **Required**: Yes


# PushNotificationConfigurationTypeDef

### Title
- **Type**: typing.Optional[str]

### Body
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'VOIP']]


# PushNotificationPreferencesTypeDef

### AllowNotifications
- **Type**: typing.Literal['ALL', 'FILTERED', 'NONE']
- **Required**: Yes

### FilterRule
- **Type**: typing.Optional[str]


# PutChannelExpirationSettingsRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]

### ExpirationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ExpirationSettingsTypeDef]


# PutChannelExpirationSettingsResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ExpirationSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutChannelMembershipPreferencesRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### Preferences
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipPreferencesTypeDef'>
- **Required**: Yes


# PutChannelMembershipPreferencesResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Member
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.IdentityTypeDef'>
- **Required**: Yes

### Preferences
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipPreferencesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutMessagingStreamingConfigurationsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.StreamingConfigurationTypeDef]
- **Required**: Yes


# PutMessagingStreamingConfigurationsResponseTypeDef

### StreamingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.StreamingConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RedactChannelMessageRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### SubChannelId
- **Type**: typing.Optional[str]


# RedactChannelMessageResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### SubChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
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


# SearchChannelsRequestRequestTypeDef

### Fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.SearchFieldTypeDef]
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchChannelsResponseTypeDef

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SearchFieldTypeDef

### Key
- **Type**: typing.Literal['MEMBERS']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['EQUALS', 'INCLUDES']
- **Required**: Yes


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

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Optional[str]

### PushNotification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.PushNotificationConfigurationTypeDef]

### MessageAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.MessageAttributeValueTypeDef]]

### SubChannelId
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.TargetTypeDef]]


# SendChannelMessageResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageStatusStructureTypeDef'>
- **Required**: Yes

### SubChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StreamingConfigurationTypeDef

### DataType
- **Type**: typing.Literal['Channel', 'ChannelMessage']
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# SubChannelSummaryTypeDef

### SubChannelId
- **Type**: typing.Optional[str]

### MembershipCount
- **Type**: typing.Optional[int]


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TargetTypeDef

### MemberArn
- **Type**: typing.Optional[str]


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateChannelFlowRequestRequestTypeDef

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Processors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ProcessorTypeDef]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateChannelFlowResponseTypeDef

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChannelMessageRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Optional[str]

### SubChannelId
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]


# UpdateChannelMessageResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageStatusStructureTypeDef'>
- **Required**: Yes

### SubChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChannelReadMarkerRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateChannelReadMarkerResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChannelRequestRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Mode
- **Type**: typing.Optional[typing.Literal['RESTRICTED', 'UNRESTRICTED']]

### Metadata
- **Type**: typing.Optional[str]


# UpdateChannelResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


