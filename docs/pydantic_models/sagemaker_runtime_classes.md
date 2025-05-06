# Sagemaker Runtime Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InternalStreamFailure

### Message
- **Type**: typing.Optional[str]


# InvokeEndpointAsyncInput

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


# InvokeEndpointAsyncOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_runtime.sagemaker_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# InvokeEndpointInput

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
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

### SessionId
- **Type**: typing.Optional[str]


# InvokeEndpointOutput

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

### NewSessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ClosedSessionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_runtime.sagemaker_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# InvokeEndpointWithResponseStreamInput

### EndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Body
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]
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

### SessionId
- **Type**: typing.Optional[str]


# InvokeEndpointWithResponseStreamOutput

### Body
- **Type**: aws_resource_validator.pydantic_models.base_validator_model.EventStream[aws_resource_validator.pydantic_models.sagemaker_runtime.sagemaker_runtime_classes.ResponseStream]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sagemaker_runtime.sagemaker_runtime_classes.ResponseMetadata'>
- **Required**: Yes


# ModelStreamError

### Message
- **Type**: typing.Optional[str]

### ErrorCode
- **Type**: typing.Optional[str]


# PayloadPart

### Bytes
- **Type**: typing.Optional[bytes]


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


# ResponseStream

### PayloadPart
- **Type**: <class 'NoneType'>

### ModelStreamError
- **Type**: <class 'NoneType'>

### InternalStreamFailure
- **Type**: <class 'NoneType'>


