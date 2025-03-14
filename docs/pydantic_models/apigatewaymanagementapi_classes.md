# Apigatewaymanagementapi Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteConnectionRequestTypeDef

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewaymanagementapi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetConnectionRequestTypeDef

### ConnectionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetConnectionResponseTypeDef

### ConnectedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Identity
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewaymanagementapi_classes.IdentityTypeDef'>
- **Required**: Yes

### LastActiveAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewaymanagementapi_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdentityTypeDef

### SourceIp
- **Type**: <class 'str'>
- **Required**: Yes

### UserAgent
- **Type**: <class 'str'>
- **Required**: Yes


# PostToConnectionRequestTypeDef

### Data
- **Type**: <class 'aws_resource_validator.pydantic_models.apigatewaymanagementapi_classes.BlobTypeDef'>
- **Required**: Yes

### ConnectionId
- **Type**: <class 'str'>
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


