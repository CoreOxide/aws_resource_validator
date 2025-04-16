# Iotsecuretunneling Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloseTunnelRequest

### tunnelId
- **Type**: <class 'str'>
- **Required**: Yes

### delete
- **Type**: typing.Optional[bool]


# ConnectionState

### status
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'DISCONNECTED']]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# DescribeTunnelRequest

### tunnelId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTunnelResponse

### tunnel
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsecuretunneling_classes.Tunnel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ResponseMetadata'>
- **Required**: Yes


# DestinationConfig

### services
- **Type**: typing.Sequence[str]
- **Required**: Yes

### thingName
- **Type**: typing.Optional[str]


# DestinationConfigOutput

### services
- **Type**: typing.List[str]
- **Required**: Yes

### thingName
- **Type**: typing.Optional[str]


# DestinationConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ResponseMetadata'>
- **Required**: Yes


# ListTunnelsRequest

### thingName
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTunnelsResponse

### tunnelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.TunnelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# OpenTunnelRequest

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.Tag]]

### destinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.DestinationConfigUnion]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.TimeoutConfig]


# OpenTunnelResponse

### tunnelId
- **Type**: <class 'str'>
- **Required**: Yes

### tunnelArn
- **Type**: <class 'str'>
- **Required**: Yes

### sourceAccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### destinationAccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ResponseMetadata'>
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


# RotateTunnelAccessTokenRequest

### tunnelId
- **Type**: <class 'str'>
- **Required**: Yes

### clientMode
- **Type**: typing.Literal['ALL', 'DESTINATION', 'SOURCE']
- **Required**: Yes

### destinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.DestinationConfigUnion]


# RotateTunnelAccessTokenResponse

### tunnelArn
- **Type**: <class 'str'>
- **Required**: Yes

### sourceAccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### destinationAccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.Tag]
- **Required**: Yes


# TimeoutConfig

### maxLifetimeTimeoutMinutes
- **Type**: typing.Optional[int]


# Tunnel

### tunnelId
- **Type**: typing.Optional[str]

### tunnelArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'OPEN']]

### sourceConnectionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ConnectionState]

### destinationConnectionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ConnectionState]

### description
- **Type**: typing.Optional[str]

### destinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.DestinationConfigOutput]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.TimeoutConfig]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.Tag]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# TunnelSummary

### tunnelId
- **Type**: typing.Optional[str]

### tunnelArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'OPEN']]

### description
- **Type**: typing.Optional[str]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


