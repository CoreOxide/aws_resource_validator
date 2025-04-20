# Ivschat Ivschat Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudWatchLogsDestinationConfiguration

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateChatTokenRequest

### roomIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['DELETE_MESSAGE', 'DISCONNECT_USER', 'SEND_MESSAGE']]]

### sessionDurationInMinutes
- **Type**: typing.Optional[int]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateChatTokenResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLoggingConfigurationRequest

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.DestinationConfiguration'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateLoggingConfigurationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.DestinationConfiguration'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRoomRequest

### name
- **Type**: typing.Optional[str]

### maximumMessageRatePerSecond
- **Type**: typing.Optional[int]

### maximumMessageLength
- **Type**: typing.Optional[int]

### messageReviewHandler
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat.ivschat_classes.MessageReviewHandler]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### loggingConfigurationIdentifiers
- **Type**: typing.Optional[typing.List[str]]


# CreateRoomResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### maximumMessageRatePerSecond
- **Type**: <class 'int'>
- **Required**: Yes

### maximumMessageLength
- **Type**: <class 'int'>
- **Required**: Yes

### messageReviewHandler
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.MessageReviewHandler'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### loggingConfigurationIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLoggingConfigurationRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMessageRequest

### roomIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]


# DeleteMessageResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteRoomRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationConfiguration

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat.ivschat_classes.S3DestinationConfiguration]

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat.ivschat_classes.CloudWatchLogsDestinationConfiguration]

### firehose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat.ivschat_classes.FirehoseDestinationConfiguration]


# DisconnectUserRequest

### roomIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.ResponseMetadata'>
- **Required**: Yes


# FirehoseDestinationConfiguration

### deliveryStreamName
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoggingConfigurationRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoggingConfigurationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.DestinationConfiguration'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.ResponseMetadata'>
- **Required**: Yes


# GetRoomRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetRoomResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### maximumMessageRatePerSecond
- **Type**: <class 'int'>
- **Required**: Yes

### maximumMessageLength
- **Type**: <class 'int'>
- **Required**: Yes

### messageReviewHandler
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.MessageReviewHandler'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### loggingConfigurationIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.ResponseMetadata'>
- **Required**: Yes


# ListLoggingConfigurationsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListLoggingConfigurationsResponse

### loggingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivschat.ivschat_classes.LoggingConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRoomsRequest

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


# ListRoomsResponse

### rooms
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivschat.ivschat_classes.RoomSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.ResponseMetadata'>
- **Required**: Yes


# LoggingConfigurationSummary

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### createTime
- **Type**: typing.Optional[datetime.datetime]

### updateTime
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### destinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat.ivschat_classes.DestinationConfiguration]

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# MessageReviewHandler

### uri
- **Type**: typing.Optional[str]

### fallbackResult
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]


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


# RoomSummary

### arn
- **Type**: typing.Optional[str]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### messageReviewHandler
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat.ivschat_classes.MessageReviewHandler]

### createTime
- **Type**: typing.Optional[datetime.datetime]

### updateTime
- **Type**: typing.Optional[datetime.datetime]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### loggingConfigurationIdentifiers
- **Type**: typing.Optional[typing.List[str]]


# S3DestinationConfiguration

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# SendEventRequest

### roomIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### eventName
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]


# SendEventResponse

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.ResponseMetadata'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateLoggingConfigurationRequest

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### destinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat.ivschat_classes.DestinationConfiguration]


# UpdateLoggingConfigurationResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.DestinationConfiguration'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRoomRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat.ivschat_classes.MessageReviewHandler]

### loggingConfigurationIdentifiers
- **Type**: typing.Optional[typing.List[str]]


# UpdateRoomResponse

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### maximumMessageRatePerSecond
- **Type**: <class 'int'>
- **Required**: Yes

### maximumMessageLength
- **Type**: <class 'int'>
- **Required**: Yes

### messageReviewHandler
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.MessageReviewHandler'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### loggingConfigurationIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat.ivschat_classes.ResponseMetadata'>
- **Required**: Yes


