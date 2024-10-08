# Pydantic Models in chime_sdk_identity_classes

# AppInstanceAdminSummaryTypeDef

### Admin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.IdentityTypeDef]


# AppInstanceAdminTypeDef

### Admin
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.IdentityTypeDef]

### AppInstanceArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# AppInstanceBotSummaryTypeDef

### AppInstanceBotArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]


# AppInstanceBotTypeDef

### AppInstanceBotArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ConfigurationTypeDef]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Metadata
- **Type**: typing.Optional[str]


# AppInstanceRetentionSettingsTypeDef

### ChannelRetentionSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ChannelRetentionSettingsTypeDef]


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

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Metadata
- **Type**: typing.Optional[str]


# AppInstanceUserEndpointSummaryTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.EndpointStateTypeDef]


# AppInstanceUserEndpointTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.EndpointAttributesTypeDef]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### AllowMessages
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE']]

### EndpointState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.EndpointStateTypeDef]


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

### Metadata
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ExpirationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ExpirationSettingsTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelRetentionSettingsTypeDef

### RetentionDays
- **Type**: typing.Optional[int]


# ConfigurationTypeDef

### Lex
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.LexConfigurationTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.IdentityTypeDef'>
- **Required**: Yes

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAppInstanceBotRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Configuration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ConfigurationTypeDef'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Metadata
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.TagTypeDef]]


# CreateAppInstanceBotResponseTypeDef

### AppInstanceBotArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.TagTypeDef]]


# CreateAppInstanceResponseTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.TagTypeDef]]

### ExpirationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ExpirationSettingsTypeDef]


# CreateAppInstanceUserResponseTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAppInstanceAdminRequestRequestTypeDef

### AppInstanceAdminArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppInstanceBotRequestRequestTypeDef

### AppInstanceBotArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppInstanceRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAppInstanceUserRequestRequestTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterAppInstanceUserEndpointRequestRequestTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
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
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.AppInstanceAdminTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppInstanceBotRequestRequestTypeDef

### AppInstanceBotArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceBotResponseTypeDef

### AppInstanceBot
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.AppInstanceBotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppInstanceRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceResponseTypeDef

### AppInstance
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.AppInstanceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppInstanceUserEndpointRequestRequestTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceUserEndpointResponseTypeDef

### AppInstanceUserEndpoint
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.AppInstanceUserEndpointTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAppInstanceUserRequestRequestTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAppInstanceUserResponseTypeDef

### AppInstanceUser
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.AppInstanceUserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EndpointAttributesTypeDef

### DeviceToken
- **Type**: <class 'str'>
- **Required**: Yes

### VoipDeviceToken
- **Type**: typing.Optional[str]


# EndpointStateTypeDef

### Status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### StatusReason
- **Type**: typing.Optional[typing.Literal['INVALID_DEVICE_TOKEN', 'INVALID_PINPOINT_ARN']]


# ExpirationSettingsTypeDef

### ExpirationDays
- **Type**: <class 'int'>
- **Required**: Yes

### ExpirationCriterion
- **Type**: typing.Literal['CREATED_TIMESTAMP']
- **Required**: Yes


# GetAppInstanceRetentionSettingsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAppInstanceRetentionSettingsResponseTypeDef

### AppInstanceRetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.AppInstanceRetentionSettingsTypeDef'>
- **Required**: Yes

### InitiateDeletionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdentityTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# InvokedByTypeDef

### StandardMessages
- **Type**: typing.Literal['ALL', 'AUTO', 'MENTIONS', 'NONE']
- **Required**: Yes

### TargetedMessages
- **Type**: typing.Literal['ALL', 'NONE']
- **Required**: Yes


# LexConfigurationTypeDef

### LexBotAliasArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocaleId
- **Type**: <class 'str'>
- **Required**: Yes

### RespondsTo
- **Type**: typing.Optional[typing.Literal['STANDARD_MESSAGES']]

### InvokedBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.InvokedByTypeDef]

### WelcomeIntent
- **Type**: typing.Optional[str]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.AppInstanceAdminSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppInstanceBotsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstanceBotsResponseTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceBots
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.AppInstanceBotSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppInstanceUserEndpointsRequestRequestTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstanceUserEndpointsResponseTypeDef

### AppInstanceUserEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.AppInstanceUserEndpointSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.AppInstanceUserSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAppInstancesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAppInstancesResponseTypeDef

### AppInstances
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.AppInstanceSummaryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutAppInstanceRetentionSettingsRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### AppInstanceRetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.AppInstanceRetentionSettingsTypeDef'>
- **Required**: Yes


# PutAppInstanceRetentionSettingsResponseTypeDef

### AppInstanceRetentionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.AppInstanceRetentionSettingsTypeDef'>
- **Required**: Yes

### InitiateDeletionTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutAppInstanceUserExpirationSettingsRequestRequestTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ExpirationSettingsTypeDef]


# PutAppInstanceUserExpirationSettingsResponseTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExpirationSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ExpirationSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterAppInstanceUserEndpointRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.EndpointAttributesTypeDef'>
- **Required**: Yes

### ClientRequestToken
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### AllowMessages
- **Type**: typing.Optional[typing.Literal['ALL', 'NONE']]


# RegisterAppInstanceUserEndpointResponseTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
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


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAppInstanceBotRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ConfigurationTypeDef]


# UpdateAppInstanceBotResponseTypeDef

### AppInstanceBotArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAppInstanceRequestRequestTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAppInstanceResponseTypeDef

### AppInstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAppInstanceUserEndpointRequestRequestTypeDef

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


# UpdateAppInstanceUserEndpointResponseTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### EndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateAppInstanceUserRequestRequestTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Metadata
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAppInstanceUserResponseTypeDef

### AppInstanceUserArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_identity_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


