# Amplifybackend Amplifybackend Classes

# BackendAPIAppSyncAuthSettings

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


# BackendAPIAuthType

### Mode
- **Type**: typing.Optional[typing.Literal['AMAZON_COGNITO_USER_POOLS', 'API_KEY', 'AWS_IAM', 'OPENID_CONNECT']]

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIAppSyncAuthSettings]


# BackendAPIConflictResolution

### ResolutionStrategy
- **Type**: typing.Optional[typing.Literal['AUTOMERGE', 'LAMBDA', 'NONE', 'OPTIMISTIC_CONCURRENCY']]


# BackendAPIResourceConfig

### AdditionalAuthTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIAuthType]]

### ApiName
- **Type**: typing.Optional[str]

### ConflictResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIConflictResolution]

### DefaultAuthType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIAuthType]

### Service
- **Type**: typing.Optional[str]

### TransformSchema
- **Type**: typing.Optional[str]


# BackendAPIResourceConfigOutput

### AdditionalAuthTypes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIAuthType]]

### ApiName
- **Type**: typing.Optional[str]

### ConflictResolution
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIConflictResolution]

### DefaultAuthType
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIAuthType]

### Service
- **Type**: typing.Optional[str]

### TransformSchema
- **Type**: typing.Optional[str]


# BackendAuthAppleProviderConfig

### ClientId
- **Type**: typing.Optional[str]

### KeyId
- **Type**: typing.Optional[str]

### PrivateKey
- **Type**: typing.Optional[str]

### TeamId
- **Type**: typing.Optional[str]


# BackendAuthSocialProviderConfig

### ClientId
- **Type**: typing.Optional[str]

### ClientSecret
- **Type**: typing.Optional[str]


# BackendJobRespObj

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


# BackendStoragePermissions

### Authenticated
- **Type**: typing.List[typing.Literal['CREATE_AND_UPDATE', 'DELETE', 'READ']]
- **Required**: Yes

### UnAuthenticated
- **Type**: typing.Optional[typing.List[typing.Literal['CREATE_AND_UPDATE', 'DELETE', 'READ']]]


# BackendStoragePermissionsOutput

### Authenticated
- **Type**: typing.List[typing.Literal['CREATE_AND_UPDATE', 'DELETE', 'READ']]
- **Required**: Yes

### UnAuthenticated
- **Type**: typing.Optional[typing.List[typing.Literal['CREATE_AND_UPDATE', 'DELETE', 'READ']]]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CloneBackendRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### TargetEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes


# CloneBackendResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBackendAPIRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIResourceConfig, aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIResourceConfigOutput]
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBackendAPIResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBackendAuthForgotPasswordConfig

### DeliveryMethod
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### EmailSettings
- **Type**: <class 'NoneType'>

### SmsSettings
- **Type**: <class 'NoneType'>


# CreateBackendAuthIdentityPoolConfig

### IdentityPoolName
- **Type**: <class 'str'>
- **Required**: Yes

### UnauthenticatedLogin
- **Type**: <class 'bool'>
- **Required**: Yes


# CreateBackendAuthMFAConfig

### MFAMode
- **Type**: typing.Literal['OFF', 'ON', 'OPTIONAL']
- **Required**: Yes

### Settings
- **Type**: <class 'NoneType'>


# CreateBackendAuthMFAConfigOutput

### MFAMode
- **Type**: typing.Literal['OFF', 'ON', 'OPTIONAL']
- **Required**: Yes

### Settings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.SettingsOutput]


# CreateBackendAuthOAuthConfig

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
- **Type**: <class 'NoneType'>


# CreateBackendAuthOAuthConfigOutput

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
- **Type**: <class 'NoneType'>


# CreateBackendAuthPasswordPolicyConfig

### MinimumLength
- **Type**: <class 'float'>
- **Required**: Yes

### AdditionalConstraints
- **Type**: typing.Optional[typing.List[typing.Literal['REQUIRE_DIGIT', 'REQUIRE_LOWERCASE', 'REQUIRE_SYMBOL', 'REQUIRE_UPPERCASE']]]


# CreateBackendAuthPasswordPolicyConfigOutput

### MinimumLength
- **Type**: <class 'float'>
- **Required**: Yes

### AdditionalConstraints
- **Type**: typing.Optional[typing.List[typing.Literal['REQUIRE_DIGIT', 'REQUIRE_LOWERCASE', 'REQUIRE_SYMBOL', 'REQUIRE_UPPERCASE']]]


# CreateBackendAuthRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthResourceConfig, aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthResourceConfigOutput]
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBackendAuthResourceConfig

### AuthResources
- **Type**: typing.Literal['IDENTITY_POOL_AND_USER_POOL', 'USER_POOL_ONLY']
- **Required**: Yes

### Service
- **Type**: typing.Literal['COGNITO']
- **Required**: Yes

### UserPoolConfigs
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthUserPoolConfig'>
- **Required**: Yes

### IdentityPoolConfigs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthIdentityPoolConfig]


# CreateBackendAuthResourceConfigOutput

### AuthResources
- **Type**: typing.Literal['IDENTITY_POOL_AND_USER_POOL', 'USER_POOL_ONLY']
- **Required**: Yes

### Service
- **Type**: typing.Literal['COGNITO']
- **Required**: Yes

### UserPoolConfigs
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthUserPoolConfigOutput'>
- **Required**: Yes

### IdentityPoolConfigs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthIdentityPoolConfig]


# CreateBackendAuthResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBackendAuthUserPoolConfig

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthForgotPasswordConfig]

### Mfa
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthMFAConfig]

### OAuth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthOAuthConfig]

### PasswordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthPasswordPolicyConfig]

### VerificationMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthVerificationMessageConfig]


# CreateBackendAuthUserPoolConfigOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthForgotPasswordConfig]

### Mfa
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthMFAConfigOutput]

### OAuth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthOAuthConfigOutput]

### PasswordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthPasswordPolicyConfigOutput]

### VerificationMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthVerificationMessageConfig]


# CreateBackendAuthVerificationMessageConfig

### DeliveryMethod
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### EmailSettings
- **Type**: <class 'NoneType'>

### SmsSettings
- **Type**: <class 'NoneType'>


# CreateBackendConfigRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendManagerAppId
- **Type**: typing.Optional[str]


# CreateBackendConfigResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBackendRequest

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
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### ResourceName
- **Type**: typing.Optional[str]


# CreateBackendResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# CreateBackendStorageRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendStorageResourceConfig'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateBackendStorageResourceConfig

### Permissions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendStoragePermissions, aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendStoragePermissionsOutput]
- **Required**: Yes

### ServiceName
- **Type**: typing.Literal['S3']
- **Required**: Yes

### BucketName
- **Type**: typing.Optional[str]


# CreateBackendStorageResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTokenRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateTokenResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBackendAPIRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIResourceConfig, aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIResourceConfigOutput, NoneType]


# DeleteBackendAPIResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBackendAuthRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackendAuthResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBackendRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBackendResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBackendStorageRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceName
- **Type**: typing.Literal['S3']
- **Required**: Yes


# DeleteBackendStorageResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTokenRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTokenResponse

### IsSuccess
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# EmailSettings

### EmailMessage
- **Type**: typing.Optional[str]

### EmailSubject
- **Type**: typing.Optional[str]


# GenerateBackendAPIModelsRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GenerateBackendAPIModelsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# GetBackendAPIModelsRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackendAPIModelsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# GetBackendAPIRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIResourceConfig, aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIResourceConfigOutput, NoneType]


# GetBackendAPIResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIResourceConfigOutput'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# GetBackendAuthRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackendAuthResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.CreateBackendAuthResourceConfigOutput'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# GetBackendJobRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackendJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# GetBackendRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: typing.Optional[str]


# GetBackendResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# GetBackendStorageRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# GetBackendStorageResourceConfig

### Imported
- **Type**: <class 'bool'>
- **Required**: Yes

### ServiceName
- **Type**: typing.Literal['S3']
- **Required**: Yes

### BucketName
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendStoragePermissionsOutput]


# GetBackendStorageResponse

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.GetBackendStorageResourceConfig'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# GetTokenRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### SessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetTokenResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# ImportBackendAuthRequest

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


# ImportBackendAuthResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# ImportBackendStorageRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceName
- **Type**: typing.Literal['S3']
- **Required**: Yes

### BucketName
- **Type**: typing.Optional[str]


# ImportBackendStorageResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# ListBackendJobsRequest

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


# ListBackendJobsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.PaginatorConfig]


# ListBackendJobsResponse

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendJobRespObj]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListS3BucketsRequest

### NextToken
- **Type**: typing.Optional[str]


# ListS3BucketsResponse

### Buckets
- **Type**: typing.List[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.S3BucketInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LoginAuthConfigReqObj

### AwsCognitoIdentityPoolId
- **Type**: typing.Optional[str]

### AwsCognitoRegion
- **Type**: typing.Optional[str]

### AwsUserPoolsId
- **Type**: typing.Optional[str]

### AwsUserPoolsWebClientId
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RemoveAllBackendsRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### CleanAmplifyApp
- **Type**: typing.Optional[bool]


# RemoveAllBackendsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveBackendConfigRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveBackendConfigResponse

### Error
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
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


# S3BucketInfo

### CreationDate
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# Settings

### MfaTypes
- **Type**: typing.Optional[typing.List[typing.Literal['SMS', 'TOTP']]]

### SmsMessage
- **Type**: typing.Optional[str]


# SettingsOutput

### MfaTypes
- **Type**: typing.Optional[typing.List[typing.Literal['SMS', 'TOTP']]]

### SmsMessage
- **Type**: typing.Optional[str]


# SmsSettings

### SmsMessage
- **Type**: typing.Optional[str]


# SocialProviderSettings

### Facebook
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAuthSocialProviderConfig]

### Google
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAuthSocialProviderConfig]

### LoginWithAmazon
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAuthSocialProviderConfig]

### SignInWithApple
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAuthAppleProviderConfig]


# UpdateBackendAPIRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIResourceConfig, aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendAPIResourceConfigOutput, NoneType]


# UpdateBackendAPIResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBackendAuthForgotPasswordConfig

### DeliveryMethod
- **Type**: typing.Optional[typing.Literal['EMAIL', 'SMS']]

### EmailSettings
- **Type**: <class 'NoneType'>

### SmsSettings
- **Type**: <class 'NoneType'>


# UpdateBackendAuthIdentityPoolConfig

### UnauthenticatedLogin
- **Type**: typing.Optional[bool]


# UpdateBackendAuthMFAConfig

### MFAMode
- **Type**: typing.Optional[typing.Literal['OFF', 'ON', 'OPTIONAL']]

### Settings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.Settings, aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.SettingsOutput, NoneType]


# UpdateBackendAuthOAuthConfig

### DomainPrefix
- **Type**: typing.Optional[str]

### OAuthGrantType
- **Type**: typing.Optional[typing.Literal['CODE', 'IMPLICIT']]

### OAuthScopes
- **Type**: typing.Optional[typing.List[typing.Literal['AWS_COGNITO_SIGNIN_USER_ADMIN', 'EMAIL', 'OPENID', 'PHONE', 'PROFILE']]]

### RedirectSignInURIs
- **Type**: typing.Optional[typing.List[str]]

### RedirectSignOutURIs
- **Type**: typing.Optional[typing.List[str]]

### SocialProviderSettings
- **Type**: <class 'NoneType'>


# UpdateBackendAuthPasswordPolicyConfig

### AdditionalConstraints
- **Type**: typing.Optional[typing.List[typing.Literal['REQUIRE_DIGIT', 'REQUIRE_LOWERCASE', 'REQUIRE_SYMBOL', 'REQUIRE_UPPERCASE']]]

### MinimumLength
- **Type**: typing.Optional[float]


# UpdateBackendAuthRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.UpdateBackendAuthResourceConfig'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBackendAuthResourceConfig

### AuthResources
- **Type**: typing.Literal['IDENTITY_POOL_AND_USER_POOL', 'USER_POOL_ONLY']
- **Required**: Yes

### Service
- **Type**: typing.Literal['COGNITO']
- **Required**: Yes

### UserPoolConfigs
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.UpdateBackendAuthUserPoolConfig'>
- **Required**: Yes

### IdentityPoolConfigs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.UpdateBackendAuthIdentityPoolConfig]


# UpdateBackendAuthResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBackendAuthUserPoolConfig

### ForgotPassword
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.UpdateBackendAuthForgotPasswordConfig]

### Mfa
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.UpdateBackendAuthMFAConfig]

### OAuth
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.UpdateBackendAuthOAuthConfig]

### PasswordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.UpdateBackendAuthPasswordPolicyConfig]

### VerificationMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.UpdateBackendAuthVerificationMessageConfig]


# UpdateBackendAuthVerificationMessageConfig

### DeliveryMethod
- **Type**: typing.Literal['EMAIL', 'SMS']
- **Required**: Yes

### EmailSettings
- **Type**: <class 'NoneType'>

### SmsSettings
- **Type**: <class 'NoneType'>


# UpdateBackendConfigRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### LoginAuthConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.LoginAuthConfigReqObj]


# UpdateBackendConfigResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.LoginAuthConfigReqObj'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBackendJobRequest

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


# UpdateBackendJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBackendStorageRequest

### AppId
- **Type**: <class 'str'>
- **Required**: Yes

### BackendEnvironmentName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.UpdateBackendStorageResourceConfig'>
- **Required**: Yes

### ResourceName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateBackendStorageResourceConfig

### Permissions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendStoragePermissions, aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.BackendStoragePermissionsOutput]
- **Required**: Yes

### ServiceName
- **Type**: typing.Literal['S3']
- **Required**: Yes


# UpdateBackendStorageResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.amplifybackend.amplifybackend_classes.ResponseMetadata'>
- **Required**: Yes


