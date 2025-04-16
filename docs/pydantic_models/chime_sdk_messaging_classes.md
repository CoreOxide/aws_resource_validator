# Chime Sdk Messaging Classes

# AppInstanceUserMembershipSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateChannelFlowRequest

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

# BatchChannelMemberships

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchCreateChannelMembershipError

### MemberArn
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[typing.Literal['AccessDenied', 'BadRequest', 'Conflict', 'Forbidden', 'NotFound', 'PhoneNumberAssociationsExist', 'PreconditionFailed', 'ResourceLimitExceeded', 'ServiceFailure', 'ServiceUnavailable', 'Throttled', 'Throttling', 'Unauthorized', 'Unprocessable', 'VoiceConnectorGroupAssociationsExist']]

### ErrorMessage
- **Type**: typing.Optional[str]


# BatchCreateChannelMembershipResponse

### BatchChannelMemberships
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.BatchChannelMemberships'>
- **Required**: Yes

### Errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.BatchCreateChannelMembershipError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# Channel

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Identity]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastMessageTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ChannelFlowArn
- **Type**: typing.Optional[str]

### ElasticChannelConfiguration
- **Type**: <class 'NoneType'>

### ExpirationSettings
- **Type**: <class 'NoneType'>


# ChannelAssociatedWithFlowSummary

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


# ChannelBan

### Member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Identity]

### ChannelArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Identity]


# ChannelBanSummary

### Member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Identity]


# ChannelFlow

### ChannelFlowArn
- **Type**: typing.Optional[str]

### Processors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Processor]]

### Name
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# ChannelFlowCallbackRequest

### CallbackId
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageCallback'>
- **Required**: Yes

### DeleteResource
- **Type**: typing.Optional[bool]


# ChannelFlowCallbackResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### CallbackId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# ChannelFlowSummary

### ChannelFlowArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Processors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Processor]]


# ChannelMembership

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelMembershipForAppInstanceUserSummary

### ChannelSummary
- **Type**: <class 'NoneType'>

### AppInstanceUserMembershipSummary
- **Type**: <class 'NoneType'>


# ChannelMembershipPreferences

### PushNotifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.PushNotificationPreferences]


# ChannelMembershipSummary

### Member
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Identity]


# ChannelMessage

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelMessageCallback

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### Content
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]

### PushNotification
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.PushNotificationConfiguration]

### MessageAttributes
- **Type**: typing.Optional[typing.Mapping[str, aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.MessageAttributeValueUnion]]

### SubChannelId
- **Type**: typing.Optional[str]

### ContentType
- **Type**: typing.Optional[str]


# ChannelMessageStatusStructure

### Value
- **Type**: typing.Optional[typing.Literal['DENIED', 'FAILED', 'PENDING', 'SENT']]

### Detail
- **Type**: typing.Optional[str]


# ChannelMessageSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelModeratedByAppInstanceUserSummary

### ChannelSummary
- **Type**: <class 'NoneType'>


# ChannelModerator

### Moderator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Identity]

### ChannelArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### CreatedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Identity]


# ChannelModeratorSummary

### Moderator
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Identity]


# ChannelSummary

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


# CreateChannelBanRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# CreateChannelBanResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Member
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Identity'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# CreateChannelFlowRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Processors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Processor]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Tag]]


# CreateChannelFlowResponse

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# CreateChannelMembershipResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Member
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Identity'>
- **Required**: Yes

### SubChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# CreateChannelModeratorRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModeratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# CreateChannelModeratorResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModerator
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Identity'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# CreateChannelRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Tag]]

### ChannelId
- **Type**: typing.Optional[str]

### MemberArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ModeratorArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ElasticChannelConfiguration
- **Type**: <class 'NoneType'>

### ExpirationSettings
- **Type**: <class 'NoneType'>


# CreateChannelResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteChannelBanRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelFlowRequest

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelMembershipRequest

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


# DeleteChannelMessageRequest

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


# DeleteChannelModeratorRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModeratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMessagingStreamingConfigurationsRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelBanRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelBanResponse

### ChannelBan
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelBan'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeChannelFlowRequest

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelFlowResponse

### ChannelFlow
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelFlow'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeChannelMembershipForAppInstanceUserRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelMembershipForAppInstanceUserResponse

### ChannelMembership
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipForAppInstanceUserSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeChannelMembershipRequest

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


# DescribeChannelMembershipResponse

### ChannelMembership
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembership'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeChannelModeratedByAppInstanceUserRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelModeratedByAppInstanceUserResponse

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelModeratedByAppInstanceUserSummary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeChannelModeratorRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModeratorArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelModeratorResponse

### ChannelModerator
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelModerator'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeChannelRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelResponse

### Channel
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Channel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateChannelFlowRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# ElasticChannelConfiguration

### MaximumSubChannels
- **Type**: <class 'int'>
- **Required**: Yes

### TargetMembershipsPerSubChannel
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumMembershipPercentage
- **Type**: <class 'int'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# ExpirationSettings

### ExpirationDays
- **Type**: <class 'int'>
- **Required**: Yes

### ExpirationCriterion
- **Type**: typing.Literal['CREATED_TIMESTAMP', 'LAST_MESSAGE_TIMESTAMP']
- **Required**: Yes


# GetChannelMembershipPreferencesRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MemberArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelMembershipPreferencesResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Member
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Identity'>
- **Required**: Yes

### Preferences
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipPreferences'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# GetChannelMessageRequest

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


# GetChannelMessageResponse

### ChannelMessage
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessage'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# GetChannelMessageStatusRequest

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


# GetChannelMessageStatusResponse

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageStatusStructure'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# GetMessagingSessionEndpointResponse

### Endpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.MessagingSessionEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# GetMessagingStreamingConfigurationsRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetMessagingStreamingConfigurationsResponse

### StreamingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.StreamingConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# Identity

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# LambdaConfiguration

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InvocationType
- **Type**: typing.Literal['ASYNC']
- **Required**: Yes


# ListChannelBansRequest

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


# ListChannelBansResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelBans
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelBanSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelFlowsRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelFlowsResponse

### ChannelFlows
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelFlowSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelMembershipsForAppInstanceUserRequest

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceUserArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelMembershipsForAppInstanceUserResponse

### ChannelMemberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipForAppInstanceUserSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelMembershipsResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelMemberships
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelMessagesRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### SortOrder
- **Type**: typing.Optional[typing.Literal['ASCENDING', 'DESCENDING']]

### NotBefore
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Timestamp]

### NotAfter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Timestamp]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### SubChannelId
- **Type**: typing.Optional[str]


# ListChannelMessagesResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelMessages
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageSummary]
- **Required**: Yes

### SubChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelModeratorsRequest

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


# ListChannelModeratorsResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelModerators
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelModeratorSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsAssociatedWithChannelFlowRequest

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsAssociatedWithChannelFlowResponse

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelAssociatedWithFlowSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsModeratedByAppInstanceUserRequest

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceUserArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsModeratedByAppInstanceUserResponse

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelModeratedByAppInstanceUserSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsRequest

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


# ListChannelsResponse

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSubChannelsRequest

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


# ListSubChannelsResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### SubChannels
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.SubChannelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# MessageAttributeValue

### StringValues
- **Type**: typing.Optional[typing.Sequence[str]]


# MessageAttributeValueOutput

### StringValues
- **Type**: typing.Optional[typing.List[str]]


# MessageAttributeValueUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MessagingSessionEndpoint

### Url
- **Type**: typing.Optional[str]


# Processor

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ProcessorConfiguration'>
- **Required**: Yes

### ExecutionOrder
- **Type**: <class 'int'>
- **Required**: Yes

### FallbackAction
- **Type**: typing.Literal['ABORT', 'CONTINUE']
- **Required**: Yes


# ProcessorConfiguration

### Lambda
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.LambdaConfiguration'>
- **Required**: Yes


# PushNotificationConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PushNotificationPreferences

### AllowNotifications
- **Type**: typing.Literal['ALL', 'FILTERED', 'NONE']
- **Required**: Yes

### FilterRule
- **Type**: typing.Optional[str]


# PutChannelExpirationSettingsRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]

### ExpirationSettings
- **Type**: <class 'NoneType'>


# PutChannelExpirationSettingsResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ExpirationSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# PutChannelMembershipPreferencesRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipPreferences'>
- **Required**: Yes


# PutChannelMembershipPreferencesResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### Member
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Identity'>
- **Required**: Yes

### Preferences
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMembershipPreferences'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# PutMessagingStreamingConfigurationsRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### StreamingConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.StreamingConfiguration]
- **Required**: Yes


# PutMessagingStreamingConfigurationsResponse

### StreamingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.StreamingConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# RedactChannelMessageRequest

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


# RedactChannelMessageResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
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


# SearchChannelsRequest

### Fields
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.SearchField]
- **Required**: Yes

### ChimeBearer
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# SearchChannelsResponse

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# SearchField

### Key
- **Type**: typing.Literal['MEMBERS']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['EQUALS', 'INCLUDES']
- **Required**: Yes


# SendChannelMessageResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageStatusStructure'>
- **Required**: Yes

### SubChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# StreamingConfiguration

### DataType
- **Type**: typing.Literal['Channel', 'ChannelMessage']
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# SubChannelSummary

### SubChannelId
- **Type**: typing.Optional[str]

### MembershipCount
- **Type**: typing.Optional[int]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Tag]
- **Required**: Yes


# Target

### MemberArn
- **Type**: typing.Optional[str]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateChannelFlowRequest

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### Processors
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.Processor]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateChannelFlowResponse

### ChannelFlowArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateChannelMessageRequest

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


# UpdateChannelMessageResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### MessageId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ChannelMessageStatusStructure'>
- **Required**: Yes

### SubChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateChannelReadMarkerRequest

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeBearer
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateChannelReadMarkerResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateChannelRequest

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


# UpdateChannelResponse

### ChannelArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_messaging_classes.ResponseMetadata'>
- **Required**: Yes


