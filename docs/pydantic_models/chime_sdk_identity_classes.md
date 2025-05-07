# Chime Sdk Identity Classes

# AppInstance

### AppInstanceArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Metadata
- **Type**: typing.Optional[str]


# AppInstanceAdmin

### Admin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.Identity]

### AppInstanceArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# AppInstanceAdminSummary

### Admin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.Identity]


# AppInstanceBot

### AppInstanceBotArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Configuration
- **Type**: <class 'NoneType'>

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Metadata
- **Type**: typing.Optional[str]


# AppInstanceBotSummary

### AppInstanceBotArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]


# AppInstanceRetentionSettings

### ChannelRetentionSettings
- **Type**: <class 'NoneType'>


# AppInstanceSummary

### AppInstanceArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]


# AppInstanceUser

### AppInstanceUserArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ExpirationSettings
- **Type**: <class 'NoneType'>


# AppInstanceUserEndpoint

### AppInstanceUserArn
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['APNS', 'APNS_SANDBOX', 'GCM']]

### ResourceArn
- **Type**: typing.Optional[str]

### EndpointAttributes
- **Type**: <class 'NoneType'>

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### AllowMessages
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE']]

### EndpointState
- **Type**: <class 'NoneType'>


# AppInstanceUserEndpointSummary

### AppInstanceUserArn
- **Type**: typing.Optional[str]

### EndpointId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['APNS', 'APNS_SANDBOX', 'GCM']]

### AllowMessages
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE']]

### EndpointState
- **Type**: <class 'NoneType'>


# AppInstanceUserSummary

### AppInstanceUserArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelRetentionSettings

### RetentionDays
- **Type**: typing.Optional[int]


# Configuration

### Lex
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.LexConfiguration'>
- **Required**: Yes


# CreateAppInstanceAdminRequest

### AppInstanceAdminArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAppInstanceAdminResponse

### AppInstanceAdmin
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.Identity'>
- **Required**: Yes

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAppInstanceBotRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.Configuration'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.Tag]]


# CreateAppInstanceBotResponse

### AppInstanceBotArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAppInstanceRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.Tag]]


# CreateAppInstanceResponse

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAppInstanceUserRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.Tag]]

### ExpirationSettings
- **Type**: <class 'NoneType'>


# CreateAppInstanceUserResponse

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAppInstanceAdminRequest

### AppInstanceAdminArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppInstanceBotRequest

### AppInstanceBotArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppInstanceRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppInstanceUserRequest

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterAppInstanceUserEndpointRequest

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceAdminRequest

### AppInstanceAdminArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceAdminResponse

### AppInstanceAdmin
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.AppInstanceAdmin'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppInstanceBotRequest

### AppInstanceBotArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceBotResponse

### AppInstanceBot
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.AppInstanceBot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppInstanceRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceResponse

### AppInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.AppInstance'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppInstanceUserEndpointRequest

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceUserEndpointResponse

### AppInstanceUserEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.AppInstanceUserEndpoint'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAppInstanceUserRequest

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceUserResponse

### AppInstanceUser
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.AppInstanceUser'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# EndpointAttributes

### DeviceToken
- **Type**: <class 'str'>
- **Required**: Yes

### VoipDeviceToken
- **Type**: typing.Optional[str]


# EndpointState

### Status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### StatusReason
- **Type**: typing.Optional[typing.Literal['INVALID_DEVICE_TOKEN', 'INVALID_PINPOINT_ARN']]


# ExpirationSettings

### ExpirationDays
- **Type**: <class 'int'>
- **Required**: Yes

### ExpirationCriterion
- **Type**: typing.Literal['CREATED_TIMESTAMP']
- **Required**: Yes


# GetAppInstanceRetentionSettingsRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppInstanceRetentionSettingsResponse

### AppInstanceRetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.AppInstanceRetentionSettings'>
- **Required**: Yes

### InitiateDeletionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# Identity

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# InvokedBy

### StandardMessages
- **Type**: typing.Literal['ALL', 'AUTO', 'MENTIONS', 'NONE']
- **Required**: Yes

### TargetedMessages
- **Type**: typing.Literal['ALL', 'NONE']
- **Required**: Yes


# LexConfiguration

### LexBotAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocaleId
- **Type**: <class 'str'>
- **Required**: Yes

### RespondsTo
- **Type**: typing.Optional[typing.Literal['STANDARD_MESSAGES']]

### InvokedBy
- **Type**: <class 'NoneType'>

### WelcomeIntent
- **Type**: typing.Optional[str]


# ListAppInstanceAdminsRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstanceAdminsResponse

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceAdmins
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.AppInstanceAdminSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstanceBotsRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstanceBotsResponse

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceBots
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.AppInstanceBotSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstanceUserEndpointsRequest

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstanceUserEndpointsResponse

### AppInstanceUserEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.AppInstanceUserEndpointSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstanceUsersRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstanceUsersResponse

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceUsers
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.AppInstanceUserSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstancesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstancesResponse

### AppInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.AppInstanceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# PutAppInstanceRetentionSettingsRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceRetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.AppInstanceRetentionSettings'>
- **Required**: Yes


# PutAppInstanceRetentionSettingsResponse

### AppInstanceRetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.AppInstanceRetentionSettings'>
- **Required**: Yes

### InitiateDeletionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# PutAppInstanceUserExpirationSettingsRequest

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationSettings
- **Type**: <class 'NoneType'>


# PutAppInstanceUserExpirationSettingsResponse

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ExpirationSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterAppInstanceUserEndpointRequest

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['APNS', 'APNS_SANDBOX', 'GCM']
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointAttributes
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.EndpointAttributes'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### AllowMessages
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE']]


# RegisterAppInstanceUserEndpointResponse

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAppInstanceBotRequest

### AppInstanceBotArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'NoneType'>


# UpdateAppInstanceBotResponse

### AppInstanceBotArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAppInstanceRequest

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAppInstanceResponse

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAppInstanceUserEndpointRequest

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### AllowMessages
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE']]


# UpdateAppInstanceUserEndpointResponse

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateAppInstanceUserRequest

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAppInstanceUserResponse

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity.chime_sdk_identity_classes.ResponseMetadata'>
- **Required**: Yes


