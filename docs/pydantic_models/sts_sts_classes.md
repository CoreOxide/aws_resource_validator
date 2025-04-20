# Sts Sts Classes

# AssumeRoleRequest

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### RoleSessionName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sts.sts_classes.PolicyDescriptorType]]

### Policy
- **Type**: typing.Optional[str]

### DurationSeconds
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sts.sts_classes.Tag]]

### TransitiveTagKeys
- **Type**: typing.Optional[typing.List[str]]

### ExternalId
- **Type**: typing.Optional[str]

### SerialNumber
- **Type**: typing.Optional[str]

### TokenCode
- **Type**: typing.Optional[str]

### SourceIdentity
- **Type**: typing.Optional[str]

### ProvidedContexts
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sts.sts_classes.ProvidedContext]]


# AssumeRoleResponse

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.Credentials'>
- **Required**: Yes

### AssumedRoleUser
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.AssumedRoleUser'>
- **Required**: Yes

### PackedPolicySize
- **Type**: <class 'int'>
- **Required**: Yes

### SourceIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.ResponseMetadata'>
- **Required**: Yes


# AssumeRoleWithSAMLRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sts.sts_classes.PolicyDescriptorType]]

### Policy
- **Type**: typing.Optional[str]

### DurationSeconds
- **Type**: typing.Optional[int]


# AssumeRoleWithSAMLResponse

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.Credentials'>
- **Required**: Yes

### AssumedRoleUser
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.AssumedRoleUser'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.ResponseMetadata'>
- **Required**: Yes


# AssumeRoleWithWebIdentityRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sts.sts_classes.PolicyDescriptorType]]

### Policy
- **Type**: typing.Optional[str]

### DurationSeconds
- **Type**: typing.Optional[int]


# AssumeRoleWithWebIdentityResponse

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.Credentials'>
- **Required**: Yes

### SubjectFromWebIdentityToken
- **Type**: <class 'str'>
- **Required**: Yes

### AssumedRoleUser
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.AssumedRoleUser'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.ResponseMetadata'>
- **Required**: Yes


# AssumeRootRequest

### TargetPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### TaskPolicyArn
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.PolicyDescriptorType'>
- **Required**: Yes

### DurationSeconds
- **Type**: typing.Optional[int]


# AssumeRootResponse

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.Credentials'>
- **Required**: Yes

### SourceIdentity
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.ResponseMetadata'>
- **Required**: Yes


# AssumedRoleUser

### AssumedRoleId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Credentials

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


# DecodeAuthorizationMessageRequest

### EncodedMessage
- **Type**: <class 'str'>
- **Required**: Yes


# DecodeAuthorizationMessageResponse

### DecodedMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.ResponseMetadata'>
- **Required**: Yes


# FederatedUser

### FederatedUserId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessKeyInfoRequest

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessKeyInfoResponse

### Account
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.ResponseMetadata'>
- **Required**: Yes


# GetCallerIdentityResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.ResponseMetadata'>
- **Required**: Yes


# GetFederationTokenRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: typing.Optional[str]

### PolicyArns
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sts.sts_classes.PolicyDescriptorType]]

### DurationSeconds
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sts.sts_classes.Tag]]


# GetFederationTokenResponse

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.Credentials'>
- **Required**: Yes

### FederatedUser
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.FederatedUser'>
- **Required**: Yes

### PackedPolicySize
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.ResponseMetadata'>
- **Required**: Yes


# GetSessionTokenRequest

### DurationSeconds
- **Type**: typing.Optional[int]

### SerialNumber
- **Type**: typing.Optional[str]

### TokenCode
- **Type**: typing.Optional[str]


# GetSessionTokenResponse

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.Credentials'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sts.sts_classes.ResponseMetadata'>
- **Required**: Yes


# PolicyDescriptorType

### arn
- **Type**: typing.Optional[str]


# ProvidedContext

### ProviderArn
- **Type**: typing.Optional[str]

### ContextAssertion
- **Type**: typing.Optional[str]


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


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


