# Apigatewaymanagementapi Apigatewaymanagementapi Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteConnectionRequest

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewaymanagementapi.apigatewaymanagementapi_classes.ResponseMetadata'>
- **Required**: Yes


# GetConnectionRequest

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectionResponse

### ConnectedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Identity
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewaymanagementapi.apigatewaymanagementapi_classes.Identity'>
- **Required**: Yes

### LastActiveAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewaymanagementapi.apigatewaymanagementapi_classes.ResponseMetadata'>
- **Required**: Yes


# Identity

### SourceIp
- **Type**: <class 'str'>
- **Required**: Yes

### UserAgent
- **Type**: <class 'str'>
- **Required**: Yes


# PostToConnectionRequest

### Data
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
- **Required**: Yes

### ConnectionId
- **Type**: <class 'str'>
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


