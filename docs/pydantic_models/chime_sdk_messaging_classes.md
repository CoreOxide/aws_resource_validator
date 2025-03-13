# Chime Sdk Messaging Classes

# AppInstanceUserMembershipSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateChannelFlowRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateChannelMembershipErrorTypeDef

### MemberArn
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'BadRequest', 'Conflict', 'Forbidden', 'NotFound', 'PhoneNumberAssociationsExist', 'PreconditionFailed', 'ResourceLimitExceeded', 'ServiceFailure', 'ServiceUnavailable', 'Throttled', 'Throttling', 'Unauthorized', 'Unprocessable', 'VoiceConnectorGroupAssociationsExist']]

### ErrorMessage
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


# ChannelFlowCallbackRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.MessageAttributeValueUnionTypeDef]]

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelMessageTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# CreateChannelBanRequestTypeDef

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


# CreateChannelFlowRequestTypeDef

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


# CreateChannelModeratorRequestTypeDef

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


# CreateChannelRequestTypeDef

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


# DeleteChannelBanRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelFlowRequestTypeDef

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelMembershipRequestTypeDef

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


# DeleteChannelMessageRequestTypeDef

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


# DeleteChannelModeratorRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModeratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMessagingStreamingConfigurationsRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelBanRequestTypeDef

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


# DescribeChannelFlowRequestTypeDef

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


# DescribeChannelMembershipForAppInstanceUserRequestTypeDef

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


# DescribeChannelMembershipRequestTypeDef

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


# DescribeChannelModeratedByAppInstanceUserRequestTypeDef

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


# DescribeChannelModeratorRequestTypeDef

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


# DescribeChannelRequestTypeDef

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


# DisassociateChannelFlowRequestTypeDef

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


# GetChannelMembershipPreferencesRequestTypeDef

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


# GetChannelMessageRequestTypeDef

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


# GetChannelMessageStatusRequestTypeDef

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


# GetMessagingStreamingConfigurationsRequestTypeDef

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


# ListChannelBansRequestTypeDef

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

### ChannelBans
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelBanSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelFlowsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelMembershipsForAppInstanceUserRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelMembershipsResponseTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelMemberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelMessagesRequestTypeDef

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### NotBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.TimestampTypeDef]

### NotAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.TimestampTypeDef]

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

### ChannelMessages
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageSummaryTypeDef]
- **Required**: Yes

### SubChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelModeratorsRequestTypeDef

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

### ChannelModerators
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelModeratorSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsAssociatedWithChannelFlowRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsModeratedByAppInstanceUserRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubChannelsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

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


# MessageAttributeValueOutputTypeDef

### StringValues
- **Type**: typing.Optional[typing.List[str]]


# MessageAttributeValueTypeDef

### StringValues
- **Type**: typing.Optional[typing.Sequence[str]]


# MessageAttributeValueUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PushNotificationPreferencesTypeDef

### AllowNotifications
- **Type**: typing.Literal['ALL', 'FILTERED', 'NONE']
- **Required**: Yes

### FilterRule
- **Type**: typing.Optional[str]


# PutChannelExpirationSettingsRequestTypeDef

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


# PutChannelMembershipPreferencesRequestTypeDef

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


# PutMessagingStreamingConfigurationsRequestTypeDef

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


# RedactChannelMessageRequestTypeDef

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


# SearchChannelsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


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


# TagResourceRequestTypeDef

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


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateChannelFlowRequestTypeDef

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


# UpdateChannelMessageRequestTypeDef

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


# UpdateChannelReadMarkerRequestTypeDef

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


# UpdateChannelRequestTypeDef

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


