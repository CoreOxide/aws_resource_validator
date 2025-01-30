# marketplace_deployment_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentParameterInputTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### secretString
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_deployment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutDeploymentParameterRequestRequestTypeDef

### agreementId
- **Type**: <class 'str'>
- **Required**: Yes

### catalog
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentParameter
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_deployment_classes.DeploymentParameterInputTypeDef'>
- **Required**: Yes

### productId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### expirationDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# PutDeploymentParameterResponseTypeDef

### agreementId
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentParameterId
- **Type**: <class 'str'>
- **Required**: Yes

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_deployment_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


