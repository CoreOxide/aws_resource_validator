# eks_auth_classes

# AssumeRoleForPodIdentityRequestRequestTypeDef

### clusterName
- **Type**: <class 'str'>
- **Required**: Yes

### token
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeRoleForPodIdentityResponseTypeDef

### subject
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_auth_classes.SubjectTypeDef'>
- **Required**: Yes

### audience
- **Type**: <class 'str'>
- **Required**: Yes

### podIdentityAssociation
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_auth_classes.PodIdentityAssociationTypeDef'>
- **Required**: Yes

### assumedRoleUser
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_auth_classes.AssumedRoleUserTypeDef'>
- **Required**: Yes

### credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_auth_classes.CredentialsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.eks_auth_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssumedRoleUserTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### assumeRoleId
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CredentialsTypeDef

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


# PodIdentityAssociationTypeDef

### associationArn
- **Type**: <class 'str'>
- **Required**: Yes

### associationId
- **Type**: <class 'str'>
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


# SubjectTypeDef

### namespace
- **Type**: <class 'str'>
- **Required**: Yes

### serviceAccount
- **Type**: <class 'str'>
- **Required**: Yes


