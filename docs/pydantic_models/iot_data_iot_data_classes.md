# Iot Data Iot Data Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteThingShadowRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### shadowName
- **Type**: typing.Optional[str]


# DeleteThingShadowResponse

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data.iot_data_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data.iot_data_classes.ResponseMetadata'>
- **Required**: Yes


# GetRetainedMessageRequest

### topic
- **Type**: <class 'str'>
- **Required**: Yes


# GetRetainedMessageResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data.iot_data_classes.ResponseMetadata'>
- **Required**: Yes


# GetThingShadowRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### shadowName
- **Type**: typing.Optional[str]


# GetThingShadowResponse

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data.iot_data_classes.ResponseMetadata'>
- **Required**: Yes


# ListNamedShadowsForThingRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### pageSize
- **Type**: typing.Optional[int]


# ListNamedShadowsForThingResponse

### results
- **Type**: typing.List[str]
- **Required**: Yes

### timestamp
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data.iot_data_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRetainedMessagesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListRetainedMessagesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iot_data.iot_data_classes.PaginatorConfig]


# ListRetainedMessagesResponse

### retainedTopics
- **Type**: typing.List[aws_resource_validator.pydantic_models.iot_data.iot_data_classes.RetainedMessageSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data.iot_data_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PublishRequest

### topic
- **Type**: <class 'str'>
- **Required**: Yes

### qos
- **Type**: typing.Optional[int]

### retain
- **Type**: typing.Optional[bool]

### payload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody, NoneType]

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


# RetainedMessageSummary

### topic
- **Type**: typing.Optional[str]

### payloadSize
- **Type**: typing.Optional[int]

### qos
- **Type**: typing.Optional[int]

### lastModifiedTime
- **Type**: typing.Optional[int]


# UpdateThingShadowRequest

### thingName
- **Type**: <class 'str'>
- **Required**: Yes

### payload
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### shadowName
- **Type**: typing.Optional[str]


# UpdateThingShadowResponse

### payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iot_data.iot_data_classes.ResponseMetadata'>
- **Required**: Yes


