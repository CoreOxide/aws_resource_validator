# Marketplace Deployment Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeploymentParameterInput

### name
- **Type**: <class 'str'>
- **Required**: Yes

### secretString
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_deployment.marketplace_deployment_classes.ResponseMetadata'>
- **Required**: Yes


# PutDeploymentParameterRequest

### agreementId
- **Type**: <class 'str'>
- **Required**: Yes

### catalog
- **Type**: <class 'str'>
- **Required**: Yes

### deploymentParameter
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_deployment.marketplace_deployment_classes.DeploymentParameterInput'>
- **Required**: Yes

### productId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### expirationDate
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutDeploymentParameterResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.marketplace_deployment.marketplace_deployment_classes.ResponseMetadata'>
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


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


