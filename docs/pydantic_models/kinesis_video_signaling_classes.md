# Kinesis Video Signaling Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetIceServerConfigRequest

### ChannelARN
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: typing.Optional[str]

### Service
- **Type**: typing.Optional[typing.Literal['TURN']]

### Username
- **Type**: typing.Optional[str]


# GetIceServerConfigResponse

### IceServerList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_video_signaling.kinesis_video_signaling_classes.IceServer]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_signaling.kinesis_video_signaling_classes.ResponseMetadata'>
- **Required**: Yes


# IceServer

### Uris
- **Type**: typing.Optional[typing.List[str]]

### Username
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### Ttl
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


# SendAlexaOfferToMasterRequest

### ChannelARN
- **Type**: <class 'str'>
- **Required**: Yes

### SenderClientId
- **Type**: <class 'str'>
- **Required**: Yes

### MessagePayload
- **Type**: <class 'str'>
- **Required**: Yes


# SendAlexaOfferToMasterResponse

### Answer
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_signaling.kinesis_video_signaling_classes.ResponseMetadata'>
- **Required**: Yes


