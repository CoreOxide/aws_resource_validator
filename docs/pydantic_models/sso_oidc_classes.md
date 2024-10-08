# Pydantic Models in sso_oidc_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateTokenRequestRequestTypeDef

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### clientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### grantType
- **Type**: <class 'str'>
- **Required**: Yes

### deviceCode
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### scope
- **Type**: typing.Optional[typing.Sequence[str]]

### redirectUri
- **Type**: typing.Optional[str]

### codeVerifier
- **Type**: typing.Optional[str]


# CreateTokenResponseTypeDef

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### tokenType
- **Type**: <class 'str'>
- **Required**: Yes

### expiresIn
- **Type**: <class 'int'>
- **Required**: Yes

### refreshToken
- **Type**: <class 'str'>
- **Required**: Yes

### idToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_oidc_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTokenWithIAMRequestRequestTypeDef

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### grantType
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Optional[str]

### refreshToken
- **Type**: typing.Optional[str]

### assertion
- **Type**: typing.Optional[str]

### scope
- **Type**: typing.Optional[typing.Sequence[str]]

### redirectUri
- **Type**: typing.Optional[str]

### subjectToken
- **Type**: typing.Optional[str]

### subjectTokenType
- **Type**: typing.Optional[str]

### requestedTokenType
- **Type**: typing.Optional[str]

### codeVerifier
- **Type**: typing.Optional[str]


# CreateTokenWithIAMResponseTypeDef

### accessToken
- **Type**: <class 'str'>
- **Required**: Yes

### tokenType
- **Type**: <class 'str'>
- **Required**: Yes

### expiresIn
- **Type**: <class 'int'>
- **Required**: Yes

### refreshToken
- **Type**: <class 'str'>
- **Required**: Yes

### idToken
- **Type**: <class 'str'>
- **Required**: Yes

### issuedTokenType
- **Type**: <class 'str'>
- **Required**: Yes

### scope
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_oidc_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterClientRequestRequestTypeDef

### clientName
- **Type**: <class 'str'>
- **Required**: Yes

### clientType
- **Type**: <class 'str'>
- **Required**: Yes

### scopes
- **Type**: typing.Optional[typing.Sequence[str]]

### redirectUris
- **Type**: typing.Optional[typing.Sequence[str]]

### grantTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### issuerUrl
- **Type**: typing.Optional[str]

### entitledApplicationArn
- **Type**: typing.Optional[str]


# RegisterClientResponseTypeDef

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### clientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### clientIdIssuedAt
- **Type**: <class 'int'>
- **Required**: Yes

### clientSecretExpiresAt
- **Type**: <class 'int'>
- **Required**: Yes

### authorizationEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### tokenEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_oidc_classes.ResponseMetadataTypeDef'>
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


# StartDeviceAuthorizationRequestRequestTypeDef

### clientId
- **Type**: <class 'str'>
- **Required**: Yes

### clientSecret
- **Type**: <class 'str'>
- **Required**: Yes

### startUrl
- **Type**: <class 'str'>
- **Required**: Yes


# StartDeviceAuthorizationResponseTypeDef

### deviceCode
- **Type**: <class 'str'>
- **Required**: Yes

### userCode
- **Type**: <class 'str'>
- **Required**: Yes

### verificationUri
- **Type**: <class 'str'>
- **Required**: Yes

### verificationUriComplete
- **Type**: <class 'str'>
- **Required**: Yes

### expiresIn
- **Type**: <class 'int'>
- **Required**: Yes

### interval
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_oidc_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


