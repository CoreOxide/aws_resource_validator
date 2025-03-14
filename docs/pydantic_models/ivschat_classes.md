# Ivschat Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudWatchLogsDestinationConfigurationTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateChatTokenRequestTypeDef

### roomIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### capabilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DELETE_MESSAGE', 'DISCONNECT_USER', 'SEND_MESSAGE']]]

### sessionDurationInMinutes
- **Type**: typing.Optional[int]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateChatTokenResponseTypeDef

### token
- **Type**: <class 'str'>
- **Required**: Yes

### tokenExpirationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### sessionExpirationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLoggingConfigurationRequestTypeDef

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.DestinationConfigurationTypeDef'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRoomRequestTypeDef

### name
- **Type**: typing.Optional[str]

### maximumMessageRatePerSecond
- **Type**: typing.Optional[int]

### maximumMessageLength
- **Type**: typing.Optional[int]

### messageReviewHandler
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.MessageReviewHandlerTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### loggingConfigurationIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# DeleteLoggingConfigurationRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoomRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationConfigurationTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.S3DestinationConfigurationTypeDef]

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.CloudWatchLogsDestinationConfigurationTypeDef]

### firehose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.FirehoseDestinationConfigurationTypeDef]


# DisconnectUserRequestTypeDef

### roomIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FirehoseDestinationConfigurationTypeDef

### deliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoggingConfigurationRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetRoomRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# ListLoggingConfigurationsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListLoggingConfigurationsResponseTypeDef

### loggingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivschat_classes.LoggingConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRoomsRequestTypeDef

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### messageReviewHandlerUri
- **Type**: typing.Optional[str]

### loggingConfigurationIdentifier
- **Type**: typing.Optional[str]


# ListRoomsResponseTypeDef

### rooms
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivschat_classes.RoomSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoggingConfigurationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MessageReviewHandlerTypeDef

### uri
- **Type**: typing.Optional[str]

### fallbackResult
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]


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


# RoomSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3DestinationConfigurationTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# SendEventRequestTypeDef

### roomIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### eventName
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLoggingConfigurationRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### destinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.DestinationConfigurationTypeDef]


# UpdateRoomRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### maximumMessageRatePerSecond
- **Type**: typing.Optional[int]

### maximumMessageLength
- **Type**: typing.Optional[int]

### messageReviewHandler
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.MessageReviewHandlerTypeDef]

### loggingConfigurationIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]


