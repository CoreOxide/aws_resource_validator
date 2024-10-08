# Pydantic Models in sagemaker_runtime_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InternalStreamFailureTypeDef

### Message
- **Type**: typing.Optional[str]


# InvokeEndpointAsyncInputRequestTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### InputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### Accept
- **Type**: typing.Optional[str]

### CustomAttributes
- **Type**: typing.Optional[str]

### InferenceId
- **Type**: typing.Optional[str]

### RequestTTLSeconds
- **Type**: typing.Optional[int]

### InvocationTimeoutSeconds
- **Type**: typing.Optional[int]


# InvokeEndpointAsyncOutputTypeDef

### InferenceId
- **Type**: <class 'str'>
- **Required**: Yes

### OutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### FailureLocation
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InvokeEndpointInputRequestTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### Accept
- **Type**: typing.Optional[str]

### CustomAttributes
- **Type**: typing.Optional[str]

### TargetModel
- **Type**: typing.Optional[str]

### TargetVariant
- **Type**: typing.Optional[str]

### TargetContainerHostname
- **Type**: typing.Optional[str]

### InferenceId
- **Type**: typing.Optional[str]

### EnableExplanations
- **Type**: typing.Optional[str]

### InferenceComponentName
- **Type**: typing.Optional[str]


# InvokeEndpointOutputTypeDef

### Body
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### InvokedProductionVariant
- **Type**: <class 'str'>
- **Required**: Yes

### CustomAttributes
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# InvokeEndpointWithResponseStreamInputRequestTypeDef

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any]]
- **Required**: Yes

### ContentType
- **Type**: typing.Optional[str]

### Accept
- **Type**: typing.Optional[str]

### CustomAttributes
- **Type**: typing.Optional[str]

### TargetVariant
- **Type**: typing.Optional[str]

### TargetContainerHostname
- **Type**: typing.Optional[str]

### InferenceId
- **Type**: typing.Optional[str]

### InferenceComponentName
- **Type**: typing.Optional[str]


# InvokeEndpointWithResponseStreamOutputTypeDef

### Body
- **Type**: ForwardRef('EventStream[ResponseStreamTypeDef]')
- **Required**: Yes

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### InvokedProductionVariant
- **Type**: <class 'str'>
- **Required**: Yes

### CustomAttributes
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_runtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ModelStreamErrorTypeDef

### Message
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]


# PayloadPartTypeDef

### Bytes
- **Type**: typing.Optional[bytes]


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


# ResponseStreamTypeDef

### PayloadPart
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_runtime_classes.PayloadPartTypeDef]

### ModelStreamError
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_runtime_classes.ModelStreamErrorTypeDef]

### InternalStreamFailure
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sagemaker_runtime_classes.InternalStreamFailureTypeDef]

