# Sts Classes

# AssumeRoleRequestRequestTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleSessionName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sts_classes.PolicyDescriptorTypeTypeDef]]

### Policy
- **Type**: typing.Optional[str]

### DurationSeconds
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sts_classes.TagTypeDef]]

### TransitiveTagKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### ExternalId
- **Type**: typing.Optional[str]

### SerialNumber
- **Type**: typing.Optional[str]

### TokenCode
- **Type**: typing.Optional[str]

### SourceIdentity
- **Type**: typing.Optional[str]

### ProvidedContexts
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sts_classes.ProvidedContextTypeDef]]


# AssumeRoleResponseTypeDef

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.CredentialsTypeDef'>
- **Required**: Yes

### AssumedRoleUser
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.AssumedRoleUserTypeDef'>
- **Required**: Yes

### PackedPolicySize
- **Type**: <class 'int'>
- **Required**: Yes

### SourceIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssumeRoleWithSAMLRequestRequestTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalArn
- **Type**: <class 'str'>
- **Required**: Yes

### SAMLAssertion
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sts_classes.PolicyDescriptorTypeTypeDef]]

### Policy
- **Type**: typing.Optional[str]

### DurationSeconds
- **Type**: typing.Optional[int]


# AssumeRoleWithSAMLResponseTypeDef

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.CredentialsTypeDef'>
- **Required**: Yes

### AssumedRoleUser
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.AssumedRoleUserTypeDef'>
- **Required**: Yes

### PackedPolicySize
- **Type**: <class 'int'>
- **Required**: Yes

### Subject
- **Type**: <class 'str'>
- **Required**: Yes

### SubjectType
- **Type**: <class 'str'>
- **Required**: Yes

### Issuer
- **Type**: <class 'str'>
- **Required**: Yes

### Audience
- **Type**: <class 'str'>
- **Required**: Yes

### NameQualifier
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssumeRoleWithWebIdentityRequestRequestTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleSessionName
- **Type**: <class 'str'>
- **Required**: Yes

### WebIdentityToken
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderId
- **Type**: typing.Optional[str]

### PolicyArns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sts_classes.PolicyDescriptorTypeTypeDef]]

### Policy
- **Type**: typing.Optional[str]

### DurationSeconds
- **Type**: typing.Optional[int]


# AssumeRoleWithWebIdentityResponseTypeDef

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.CredentialsTypeDef'>
- **Required**: Yes

### SubjectFromWebIdentityToken
- **Type**: <class 'str'>
- **Required**: Yes

### AssumedRoleUser
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.AssumedRoleUserTypeDef'>
- **Required**: Yes

### PackedPolicySize
- **Type**: <class 'int'>
- **Required**: Yes

### Provider
- **Type**: <class 'str'>
- **Required**: Yes

### Audience
- **Type**: <class 'str'>
- **Required**: Yes

### SourceIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssumedRoleUserTypeDef

### AssumedRoleId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CredentialsTypeDef

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### SecretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes

### SessionToken
- **Type**: <class 'str'>
- **Required**: Yes

### Expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# DecodeAuthorizationMessageRequestRequestTypeDef

### EncodedMessage
- **Type**: <class 'str'>
- **Required**: Yes


# DecodeAuthorizationMessageResponseTypeDef

### DecodedMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FederatedUserTypeDef

### FederatedUserId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessKeyInfoRequestRequestTypeDef

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessKeyInfoResponseTypeDef

### Account
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCallerIdentityResponseTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### Account
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetFederationTokenRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: typing.Optional[str]

### PolicyArns
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sts_classes.PolicyDescriptorTypeTypeDef]]

### DurationSeconds
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sts_classes.TagTypeDef]]


# GetFederationTokenResponseTypeDef

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.CredentialsTypeDef'>
- **Required**: Yes

### FederatedUser
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.FederatedUserTypeDef'>
- **Required**: Yes

### PackedPolicySize
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSessionTokenRequestRequestTypeDef

### DurationSeconds
- **Type**: typing.Optional[int]

### SerialNumber
- **Type**: typing.Optional[str]

### TokenCode
- **Type**: typing.Optional[str]


# GetSessionTokenResponseTypeDef

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.CredentialsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PolicyDescriptorTypeTypeDef

### arn
- **Type**: typing.Optional[str]


# ProvidedContextTypeDef

### ProviderArn
- **Type**: typing.Optional[str]

### ContextAssertion
- **Type**: typing.Optional[str]


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


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


