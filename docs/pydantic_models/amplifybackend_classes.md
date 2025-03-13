# Amplifybackend Classes

# BackendAPIAppSyncAuthSettingsTypeDef

### CognitoUserPoolId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### ExpirationTime
- **Type**: typing.Optional[float]

### OpenIDAuthTTL
- **Type**: typing.Optional[str]

### OpenIDClientId
- **Type**: typing.Optional[str]

### OpenIDIatTTL
- **Type**: typing.Optional[str]

### OpenIDIssueURL
- **Type**: typing.Optional[str]

### OpenIDProviderName
- **Type**: typing.Optional[str]


# BackendAPIAuthTypeTypeDef

### Mode
- **Type**: typing.Optional[typing.Literal['AMAZON_COGNITO_USER_POOLS', 'API_KEY', 'AWS_IAM', 'OPENID_CONNECT']]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAPIAppSyncAuthSettingsTypeDef]


# BackendAPIConflictResolutionTypeDef

### ResolutionStrategy
- **Type**: typing.Optional[typing.Literal['AUTOMERGE', 'LAMBDA', 'NONE', 'OPTIMISTIC_CONCURRENCY']]


# BackendAPIResourceConfigOutputTypeDef

### AdditionalAuthTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAPIAuthTypeTypeDef]]

### ApiName
- **Type**: typing.Optional[str]

### ConflictResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAPIConflictResolutionTypeDef]

### DefaultAuthType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAPIAuthTypeTypeDef]

### Service
- **Type**: typing.Optional[str]

### TransformSchema
- **Type**: typing.Optional[str]


# BackendAPIResourceConfigTypeDef

### AdditionalAuthTypes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAPIAuthTypeTypeDef]]

### ApiName
- **Type**: typing.Optional[str]

### ConflictResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAPIConflictResolutionTypeDef]

### DefaultAuthType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAPIAuthTypeTypeDef]

### Service
- **Type**: typing.Optional[str]

### TransformSchema
- **Type**: typing.Optional[str]


# BackendAPIResourceConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BackendAuthAppleProviderConfigTypeDef

### ClientId
- **Type**: typing.Optional[str]

### KeyId
- **Type**: typing.Optional[str]

### PrivateKey
- **Type**: typing.Optional[str]

### TeamId
- **Type**: typing.Optional[str]


# BackendAuthSocialProviderConfigTypeDef

### ClientId
- **Type**: typing.Optional[str]

### ClientSecret
- **Type**: typing.Optional[str]


# BackendJobRespObjTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[str]

### JobId
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### UpdateTime
- **Type**: typing.Optional[str]


# BackendStoragePermissionsOutputTypeDef

### Authenticated
- **Type**: typing.List[typing.Literal['CREATE_AND_UPDATE', 'DELETE', 'READ']]
- **Required**: Yes

### UnAuthenticated
- **Type**: typing.Optional[typing.List[typing.Literal['CREATE_AND_UPDATE', 'DELETE', 'READ']]]


# BackendStoragePermissionsTypeDef

### Authenticated
- **Type**: typing.Sequence[typing.Literal['CREATE_AND_UPDATE', 'DELETE', 'READ']]
- **Required**: Yes

### UnAuthenticated
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CREATE_AND_UPDATE', 'DELETE', 'READ']]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloneBackendRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes


# CloneBackendResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBackendAPIRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAPIResourceConfigUnionTypeDef'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBackendAPIResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBackendAuthForgotPasswordConfigTypeDef

### DeliveryMethod
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### EmailSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.EmailSettingsTypeDef]

### SmsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.SmsSettingsTypeDef]


# CreateBackendAuthIdentityPoolConfigTypeDef

### IdentityPoolName
- **Type**: <class 'str'>
- **Required**: Yes

### UnauthenticatedLogin
- **Type**: <class 'bool'>
- **Required**: Yes


# CreateBackendAuthMFAConfigOutputTypeDef

### MFAMode
- **Type**: typing.Literal['OFF', 'ON', 'OPTIONAL']
- **Required**: Yes

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.SettingsOutputTypeDef]


# CreateBackendAuthMFAConfigTypeDef

### MFAMode
- **Type**: typing.Literal['OFF', 'ON', 'OPTIONAL']
- **Required**: Yes

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.SettingsTypeDef]


# CreateBackendAuthOAuthConfigOutputTypeDef

### OAuthGrantType
- **Type**: typing.Literal['CODE', 'IMPLICIT']
- **Required**: Yes

### OAuthScopes
- **Type**: typing.List[typing.Literal['AWS_COGNITO_SIGNIN_USER_ADMIN', 'EMAIL', 'OPENID', 'PHONE', 'PROFILE']]
- **Required**: Yes

### RedirectSignInURIs
- **Type**: typing.List[str]
- **Required**: Yes

### RedirectSignOutURIs
- **Type**: typing.List[str]
- **Required**: Yes

### DomainPrefix
- **Type**: typing.Optional[str]

### SocialProviderSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.SocialProviderSettingsTypeDef]


# CreateBackendAuthOAuthConfigTypeDef

### OAuthGrantType
- **Type**: typing.Literal['CODE', 'IMPLICIT']
- **Required**: Yes

### OAuthScopes
- **Type**: typing.Sequence[typing.Literal['AWS_COGNITO_SIGNIN_USER_ADMIN', 'EMAIL', 'OPENID', 'PHONE', 'PROFILE']]
- **Required**: Yes

### RedirectSignInURIs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### RedirectSignOutURIs
- **Type**: typing.Sequence[str]
- **Required**: Yes

### DomainPrefix
- **Type**: typing.Optional[str]

### SocialProviderSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.SocialProviderSettingsTypeDef]


# CreateBackendAuthPasswordPolicyConfigOutputTypeDef

### MinimumLength
- **Type**: <class 'float'>
- **Required**: Yes

### AdditionalConstraints
- **Type**: typing.Optional[typing.List[typing.Literal['REQUIRE_DIGIT', 'REQUIRE_LOWERCASE', 'REQUIRE_SYMBOL', 'REQUIRE_UPPERCASE']]]


# CreateBackendAuthPasswordPolicyConfigTypeDef

### MinimumLength
- **Type**: <class 'float'>
- **Required**: Yes

### AdditionalConstraints
- **Type**: typing.Optional[typing.Sequence[typing.Literal['REQUIRE_DIGIT', 'REQUIRE_LOWERCASE', 'REQUIRE_SYMBOL', 'REQUIRE_UPPERCASE']]]


# CreateBackendAuthRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthResourceConfigUnionTypeDef'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBackendAuthResourceConfigOutputTypeDef

### AuthResources
- **Type**: typing.Literal['IDENTITY_POOL_AND_USER_POOL', 'USER_POOL_ONLY']
- **Required**: Yes

### Service
- **Type**: typing.Literal['COGNITO']
- **Required**: Yes

### UserPoolConfigs
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthUserPoolConfigOutputTypeDef'>
- **Required**: Yes

### IdentityPoolConfigs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthIdentityPoolConfigTypeDef]


# CreateBackendAuthResourceConfigTypeDef

### AuthResources
- **Type**: typing.Literal['IDENTITY_POOL_AND_USER_POOL', 'USER_POOL_ONLY']
- **Required**: Yes

### Service
- **Type**: typing.Literal['COGNITO']
- **Required**: Yes

### UserPoolConfigs
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthUserPoolConfigTypeDef'>
- **Required**: Yes

### IdentityPoolConfigs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthIdentityPoolConfigTypeDef]


# CreateBackendAuthResourceConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateBackendAuthResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBackendAuthUserPoolConfigOutputTypeDef

### RequiredSignUpAttributes
- **Type**: typing.List[typing.Literal['ADDRESS', 'BIRTHDATE', 'EMAIL', 'FAMILY_NAME', 'GENDER', 'GIVEN_NAME', 'LOCALE', 'MIDDLE_NAME', 'NAME', 'NICKNAME', 'PHONE_NUMBER', 'PICTURE', 'PREFERRED_USERNAME', 'PROFILE', 'UPDATED_AT', 'WEBSITE', 'ZONE_INFO']]
- **Required**: Yes

### SignInMethod
- **Type**: typing.Literal['EMAIL', 'EMAIL_AND_PHONE_NUMBER', 'PHONE_NUMBER', 'USERNAME']
- **Required**: Yes

### UserPoolName
- **Type**: <class 'str'>
- **Required**: Yes

### ForgotPassword
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthForgotPasswordConfigTypeDef]

### Mfa
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthMFAConfigOutputTypeDef]

### OAuth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthOAuthConfigOutputTypeDef]

### PasswordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthPasswordPolicyConfigOutputTypeDef]

### VerificationMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthVerificationMessageConfigTypeDef]


# CreateBackendAuthUserPoolConfigTypeDef

### RequiredSignUpAttributes
- **Type**: typing.Sequence[typing.Literal['ADDRESS', 'BIRTHDATE', 'EMAIL', 'FAMILY_NAME', 'GENDER', 'GIVEN_NAME', 'LOCALE', 'MIDDLE_NAME', 'NAME', 'NICKNAME', 'PHONE_NUMBER', 'PICTURE', 'PREFERRED_USERNAME', 'PROFILE', 'UPDATED_AT', 'WEBSITE', 'ZONE_INFO']]
- **Required**: Yes

### SignInMethod
- **Type**: typing.Literal['EMAIL', 'EMAIL_AND_PHONE_NUMBER', 'PHONE_NUMBER', 'USERNAME']
- **Required**: Yes

### UserPoolName
- **Type**: <class 'str'>
- **Required**: Yes

### ForgotPassword
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthForgotPasswordConfigTypeDef]

### Mfa
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthMFAConfigTypeDef]

### OAuth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthOAuthConfigTypeDef]

### PasswordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthPasswordPolicyConfigTypeDef]

### VerificationMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthVerificationMessageConfigTypeDef]


# CreateBackendAuthVerificationMessageConfigTypeDef

### DeliveryMethod
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### EmailSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.EmailSettingsTypeDef]

### SmsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.SmsSettingsTypeDef]


# CreateBackendConfigRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendManagerAppId
- **Type**: typing.Optional[str]


# CreateBackendConfigResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBackendRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### AppName
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### ResourceName
- **Type**: typing.Optional[str]


# CreateBackendResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateBackendStorageRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendStorageResourceConfigTypeDef'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBackendStorageResourceConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateBackendStorageResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTokenRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateTokenResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### ChallengeCode
- **Type**: <class 'str'>
- **Required**: Yes

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Ttl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBackendAPIRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAPIResourceConfigUnionTypeDef]


# DeleteBackendAPIResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBackendAuthRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackendAuthResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBackendRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackendResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBackendStorageResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTokenRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTokenResponseTypeDef

### IsSuccess
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmailSettingsTypeDef

### EmailMessage
- **Type**: typing.Optional[str]

### EmailSubject
- **Type**: typing.Optional[str]


# GenerateBackendAPIModelsRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GenerateBackendAPIModelsResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBackendAPIModelsRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackendAPIModelsResponseTypeDef

### Models
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['LATEST', 'STALE']
- **Required**: Yes

### ModelIntrospectionSchema
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBackendAPIRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAPIResourceConfigUnionTypeDef]


# GetBackendAPIResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAPIResourceConfigOutputTypeDef'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBackendAuthRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackendAuthResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.CreateBackendAuthResourceConfigOutputTypeDef'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBackendJobRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackendJobResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBackendRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: typing.Optional[str]


# GetBackendResponseTypeDef

### AmplifyFeatureFlags
- **Type**: <class 'str'>
- **Required**: Yes

### AmplifyMetaConfig
- **Type**: <class 'str'>
- **Required**: Yes

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### AppName
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentList
- **Type**: typing.List[str]
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetBackendStorageRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackendStorageResourceConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetBackendStorageResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.GetBackendStorageResourceConfigTypeDef'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTokenRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTokenResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### ChallengeCode
- **Type**: <class 'str'>
- **Required**: Yes

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes

### Ttl
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportBackendAuthRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### NativeClientId
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### WebClientId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityPoolId
- **Type**: typing.Optional[str]


# ImportBackendAuthResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportBackendStorageResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListBackendJobsRequestPaginateTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.PaginatorConfigTypeDef]


# ListBackendJobsRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Operation
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# ListBackendJobsResponseTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendJobRespObjTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListS3BucketsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]


# ListS3BucketsResponseTypeDef

### Buckets
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifybackend_classes.S3BucketInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoginAuthConfigReqObjTypeDef

### AwsCognitoIdentityPoolId
- **Type**: typing.Optional[str]

### AwsCognitoRegion
- **Type**: typing.Optional[str]

### AwsUserPoolsId
- **Type**: typing.Optional[str]

### AwsUserPoolsWebClientId
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RemoveAllBackendsRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### CleanAmplifyApp
- **Type**: typing.Optional[bool]


# RemoveAllBackendsResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveBackendConfigRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveBackendConfigResponseTypeDef

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
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


# S3BucketInfoTypeDef

### CreationDate
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# SettingsOutputTypeDef

### MfaTypes
- **Type**: typing.Optional[typing.List[typing.Literal['SMS', 'TOTP']]]

### SmsMessage
- **Type**: typing.Optional[str]


# SettingsTypeDef

### MfaTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['SMS', 'TOTP']]]

### SmsMessage
- **Type**: typing.Optional[str]


# SettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SmsSettingsTypeDef

### SmsMessage
- **Type**: typing.Optional[str]


# SocialProviderSettingsTypeDef

### Facebook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAuthSocialProviderConfigTypeDef]

### Google
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAuthSocialProviderConfigTypeDef]

### LoginWithAmazon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAuthSocialProviderConfigTypeDef]

### SignInWithApple
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAuthAppleProviderConfigTypeDef]


# UpdateBackendAPIRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.BackendAPIResourceConfigUnionTypeDef]


# UpdateBackendAPIResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBackendAuthForgotPasswordConfigTypeDef

### DeliveryMethod
- **Type**: typing.Optional[typing.Literal['EMAIL', 'SMS']]

### EmailSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.EmailSettingsTypeDef]

### SmsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.SmsSettingsTypeDef]


# UpdateBackendAuthIdentityPoolConfigTypeDef

### UnauthenticatedLogin
- **Type**: typing.Optional[bool]


# UpdateBackendAuthMFAConfigTypeDef

### MFAMode
- **Type**: typing.Optional[typing.Literal['OFF', 'ON', 'OPTIONAL']]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.SettingsUnionTypeDef]


# UpdateBackendAuthOAuthConfigTypeDef

### DomainPrefix
- **Type**: typing.Optional[str]

### OAuthGrantType
- **Type**: typing.Optional[typing.Literal['CODE', 'IMPLICIT']]

### OAuthScopes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWS_COGNITO_SIGNIN_USER_ADMIN', 'EMAIL', 'OPENID', 'PHONE', 'PROFILE']]]

### RedirectSignInURIs
- **Type**: typing.Optional[typing.Sequence[str]]

### RedirectSignOutURIs
- **Type**: typing.Optional[typing.Sequence[str]]

### SocialProviderSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.SocialProviderSettingsTypeDef]


# UpdateBackendAuthPasswordPolicyConfigTypeDef

### AdditionalConstraints
- **Type**: typing.Optional[typing.Sequence[typing.Literal['REQUIRE_DIGIT', 'REQUIRE_LOWERCASE', 'REQUIRE_SYMBOL', 'REQUIRE_UPPERCASE']]]

### MinimumLength
- **Type**: typing.Optional[float]


# UpdateBackendAuthRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.UpdateBackendAuthResourceConfigTypeDef'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBackendAuthResourceConfigTypeDef

### AuthResources
- **Type**: typing.Literal['IDENTITY_POOL_AND_USER_POOL', 'USER_POOL_ONLY']
- **Required**: Yes

### Service
- **Type**: typing.Literal['COGNITO']
- **Required**: Yes

### UserPoolConfigs
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.UpdateBackendAuthUserPoolConfigTypeDef'>
- **Required**: Yes

### IdentityPoolConfigs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.UpdateBackendAuthIdentityPoolConfigTypeDef]


# UpdateBackendAuthResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBackendAuthUserPoolConfigTypeDef

### ForgotPassword
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.UpdateBackendAuthForgotPasswordConfigTypeDef]

### Mfa
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.UpdateBackendAuthMFAConfigTypeDef]

### OAuth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.UpdateBackendAuthOAuthConfigTypeDef]

### PasswordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.UpdateBackendAuthPasswordPolicyConfigTypeDef]

### VerificationMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.UpdateBackendAuthVerificationMessageConfigTypeDef]


# UpdateBackendAuthVerificationMessageConfigTypeDef

### DeliveryMethod
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### EmailSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.EmailSettingsTypeDef]

### SmsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.SmsSettingsTypeDef]


# UpdateBackendConfigRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### LoginAuthConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend_classes.LoginAuthConfigReqObjTypeDef]


# UpdateBackendConfigResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendManagerAppId
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### LoginAuthConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.LoginAuthConfigReqObjTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBackendJobRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]


# UpdateBackendJobResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateTime
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBackendStorageRequestTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.UpdateBackendStorageResourceConfigTypeDef'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBackendStorageResourceConfigTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateBackendStorageResponseTypeDef

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


