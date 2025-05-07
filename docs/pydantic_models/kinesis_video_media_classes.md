# Kinesis Video Media Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetMediaInput

### StartSelector
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_media.kinesis_video_media_classes.StartSelector'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# GetMediaOutput

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_media.kinesis_video_media_classes.ResponseMetadata'>
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


# StartSelector

### StartSelectorType
- **Type**: typing.Literal['CONTINUATION_TOKEN', 'EARLIEST', 'FRAGMENT_NUMBER', 'NOW', 'PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']
- **Required**: Yes

### AfterFragmentNumber
- **Type**: typing.Optional[str]

### StartTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### ContinuationToken
- **Type**: typing.Optional[str]


