# Pydantic Models in ivschat_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloudWatchLogsDestinationConfigurationTypeDef

### logGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateChatTokenRequestRequestTypeDef

### roomIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### userId
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### capabilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DELETE_MESSAGE', 'DISCONNECT_USER', 'SEND_MESSAGE']]]

### sessionDurationInMinutes
- **Type**: typing.Optional[int]


# CreateChatTokenResponseTypeDef

### sessionExpirationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### token
- **Type**: <class 'str'>
- **Required**: Yes

### tokenExpirationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLoggingConfigurationRequestRequestTypeDef

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.DestinationConfigurationTypeDef'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLoggingConfigurationResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.DestinationConfigurationTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRoomRequestRequestTypeDef

### loggingConfigurationIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### maximumMessageLength
- **Type**: typing.Optional[int]

### maximumMessageRatePerSecond
- **Type**: typing.Optional[int]

### messageReviewHandler
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.MessageReviewHandlerTypeDef]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateRoomResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### loggingConfigurationIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### maximumMessageLength
- **Type**: <class 'int'>
- **Required**: Yes

### maximumMessageRatePerSecond
- **Type**: <class 'int'>
- **Required**: Yes

### messageReviewHandler
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.MessageReviewHandlerTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLoggingConfigurationRequestRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMessageRequestRequestTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### roomIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]


# DeleteMessageResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteRoomRequestRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationConfigurationTypeDef

### cloudWatchLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.CloudWatchLogsDestinationConfigurationTypeDef]

### firehose
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.FirehoseDestinationConfigurationTypeDef]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.S3DestinationConfigurationTypeDef]


# DisconnectUserRequestRequestTypeDef

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


# GetLoggingConfigurationRequestRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoggingConfigurationResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.DestinationConfigurationTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRoomRequestRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetRoomResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### loggingConfigurationIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### maximumMessageLength
- **Type**: <class 'int'>
- **Required**: Yes

### maximumMessageRatePerSecond
- **Type**: <class 'int'>
- **Required**: Yes

### messageReviewHandler
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.MessageReviewHandlerTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLoggingConfigurationsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListLoggingConfigurationsResponseTypeDef

### loggingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivschat_classes.LoggingConfigurationSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRoomsRequestRequestTypeDef

### loggingConfigurationIdentifier
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### messageReviewHandlerUri
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]


# ListRoomsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### rooms
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivschat_classes.RoomSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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

### arn
- **Type**: typing.Optional[str]

### createTime
- **Type**: typing.Optional[datetime.datetime]

### destinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.DestinationConfigurationTypeDef]

### id
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING', 'UPDATE_FAILED', 'UPDATING']]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### updateTime
- **Type**: typing.Optional[datetime.datetime]


# MessageReviewHandlerTypeDef

### fallbackResult
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### uri
- **Type**: typing.Optional[str]


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

### arn
- **Type**: typing.Optional[str]

### createTime
- **Type**: typing.Optional[datetime.datetime]

### id
- **Type**: typing.Optional[str]

### loggingConfigurationIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### messageReviewHandler
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.MessageReviewHandlerTypeDef]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### updateTime
- **Type**: typing.Optional[datetime.datetime]


# S3DestinationConfigurationTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# SendEventRequestRequestTypeDef

### eventName
- **Type**: <class 'str'>
- **Required**: Yes

### roomIdentifier
- **Type**: <class 'str'>
- **Required**: Yes

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]


# SendEventResponseTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateLoggingConfigurationRequestRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### destinationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.DestinationConfigurationTypeDef]

### name
- **Type**: typing.Optional[str]


# UpdateLoggingConfigurationResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.DestinationConfigurationTypeDef'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE']
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRoomRequestRequestTypeDef

### identifier
- **Type**: <class 'str'>
- **Required**: Yes

### loggingConfigurationIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]

### maximumMessageLength
- **Type**: typing.Optional[int]

### maximumMessageRatePerSecond
- **Type**: typing.Optional[int]

### messageReviewHandler
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivschat_classes.MessageReviewHandlerTypeDef]

### name
- **Type**: typing.Optional[str]


# UpdateRoomResponseTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### createTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### loggingConfigurationIdentifiers
- **Type**: typing.List[str]
- **Required**: Yes

### maximumMessageLength
- **Type**: <class 'int'>
- **Required**: Yes

### maximumMessageRatePerSecond
- **Type**: <class 'int'>
- **Required**: Yes

### messageReviewHandler
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.MessageReviewHandlerTypeDef'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### updateTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivschat_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


