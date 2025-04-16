# Eks Auth Classes

# AssumeRoleForPodIdentityRequest

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### token
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeRoleForPodIdentityResponse

### subject
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_auth_classes.Subject'>
- **Required**: Yes

### audience
- **Type**: <class 'str'>
- **Required**: Yes

### podIdentityAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_auth_classes.PodIdentityAssociation'>
- **Required**: Yes

### assumedRoleUser
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_auth_classes.AssumedRoleUser'>
- **Required**: Yes

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_auth_classes.Credentials'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_auth_classes.ResponseMetadata'>
- **Required**: Yes


# AssumedRoleUser

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### assumeRoleId
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Credentials

### sessionToken
- **Type**: <class 'str'>
- **Required**: Yes

### secretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes

### accessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# PodIdentityAssociation

### associationArn
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
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


# Subject

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### serviceAccount
- **Type**: <class 'str'>
- **Required**: Yes


