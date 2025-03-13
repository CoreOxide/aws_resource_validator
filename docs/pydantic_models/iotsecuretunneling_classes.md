# Iotsecuretunneling Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloseTunnelRequestTypeDef

### tunnelId
- **Type**: <class 'str'>
- **Required**: Yes

### delete
- **Type**: typing.Optional[bool]


# ConnectionStateTypeDef

### status
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'DISCONNECTED']]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# DescribeTunnelRequestTypeDef

### tunnelId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTunnelResponseTypeDef

### tunnel
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsecuretunneling_classes.TunnelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationConfigOutputTypeDef

### services
- **Type**: typing.List[str]
- **Required**: Yes

### thingName
- **Type**: typing.Optional[str]


# DestinationConfigTypeDef

### services
- **Type**: typing.Sequence[str]
- **Required**: Yes

### thingName
- **Type**: typing.Optional[str]


# DestinationConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTunnelsRequestTypeDef

### thingName
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTunnelsResponseTypeDef

### tunnelSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.TunnelSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# OpenTunnelRequestTypeDef

### description
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.TagTypeDef]]

### destinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.DestinationConfigUnionTypeDef]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.TimeoutConfigTypeDef]


# OpenTunnelResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# RotateTunnelAccessTokenRequestTypeDef

### tunnelId
- **Type**: <class 'str'>
- **Required**: Yes

### clientMode
- **Type**: typing.Literal['ALL', 'DESTINATION', 'SOURCE']
- **Required**: Yes

### destinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.DestinationConfigUnionTypeDef]


# RotateTunnelAccessTokenResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### value
- **Type**: <class 'str'>
- **Required**: Yes


# TimeoutConfigTypeDef

### maxLifetimeTimeoutMinutes
- **Type**: typing.Optional[int]


# TunnelSummaryTypeDef

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


# TunnelTypeDef

### tunnelId
- **Type**: typing.Optional[str]

### tunnelArn
- **Type**: typing.Optional[str]

### status
- **Type**: typing.Optional[typing.Literal['CLOSED', 'OPEN']]

### sourceConnectionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ConnectionStateTypeDef]

### destinationConnectionState
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.ConnectionStateTypeDef]

### description
- **Type**: typing.Optional[str]

### destinationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.DestinationConfigOutputTypeDef]

### timeoutConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.TimeoutConfigTypeDef]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iotsecuretunneling_classes.TagTypeDef]]

### createdAt
- **Type**: typing.Optional[datetime.datetime]

### lastUpdatedAt
- **Type**: typing.Optional[datetime.datetime]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


