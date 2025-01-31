# Iot Data Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteThingShadowRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### shadowName
- **Type**: typing.Optional[str]


# DeleteThingShadowResponseTypeDef

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRetainedMessageRequestRequestTypeDef

### topic
- **Type**: <class 'str'>
- **Required**: Yes


# GetRetainedMessageResponseTypeDef

### topic
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: <class 'bytes'>
- **Required**: Yes

### qos
- **Type**: <class 'int'>
- **Required**: Yes

### lastModifiedTime
- **Type**: <class 'int'>
- **Required**: Yes

### userProperties
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetThingShadowRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### shadowName
- **Type**: typing.Optional[str]


# GetThingShadowResponseTypeDef

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNamedShadowsForThingRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListNamedShadowsForThingResponseTypeDef

### results
- **Type**: typing.List[str]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### timestamp
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRetainedMessagesRequestListRetainedMessagesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_data_classes.PaginatorConfigTypeDef]


# ListRetainedMessagesRequestRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRetainedMessagesResponseTypeDef

### retainedTopics
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_data_classes.RetainedMessageSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PublishRequestRequestTypeDef

### topic
- **Type**: <class 'str'>
- **Required**: Yes

### qos
- **Type**: typing.Optional[int]

### retain
- **Type**: typing.Optional[bool]

### payload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### userProperties
- **Type**: typing.Optional[str]

### payloadFormatIndicator
- **Type**: typing.Optional[typing.Literal['UNSPECIFIED_BYTES', 'UTF8_DATA']]

### contentType
- **Type**: typing.Optional[str]

### responseTopic
- **Type**: typing.Optional[str]

### correlationData
- **Type**: typing.Optional[str]

### messageExpiry
- **Type**: typing.Optional[int]


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


# RetainedMessageSummaryTypeDef

### topic
- **Type**: typing.Optional[str]

### payloadSize
- **Type**: typing.Optional[int]

### qos
- **Type**: typing.Optional[int]

### lastModifiedTime
- **Type**: typing.Optional[int]


# UpdateThingShadowRequestRequestTypeDef

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### shadowName
- **Type**: typing.Optional[str]


# UpdateThingShadowResponseTypeDef

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


