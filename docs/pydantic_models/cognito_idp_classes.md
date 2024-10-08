# Pydantic Models in cognito_idp_classes

# AccountRecoverySettingTypeOutputTypeDef

### RecoveryMechanisms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.RecoveryOptionTypeTypeDef]]


# AccountRecoverySettingTypeTypeDef

### RecoveryMechanisms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.RecoveryOptionTypeTypeDef]]


# AccountTakeoverActionTypeTypeDef

### Notify
- **Type**: <class 'bool'>
- **Required**: Yes

### EventAction
- **Type**: typing.Literal['BLOCK', 'MFA_IF_CONFIGURED', 'MFA_REQUIRED', 'NO_ACTION']
- **Required**: Yes


# AccountTakeoverActionsTypeTypeDef

### LowAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountTakeoverActionTypeTypeDef]

### MediumAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountTakeoverActionTypeTypeDef]

### HighAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountTakeoverActionTypeTypeDef]


# AccountTakeoverRiskConfigurationTypeTypeDef

### Actions
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.AccountTakeoverActionsTypeTypeDef'>
- **Required**: Yes

### NotifyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.NotifyConfigurationTypeTypeDef]


# AddCustomAttributesRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomAttributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.SchemaAttributeTypeTypeDef]
- **Required**: Yes


# AdminAddUserToGroupRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# AdminConfirmSignUpRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AdminCreateUserConfigTypeTypeDef

### AllowAdminCreateUserOnly
- **Type**: typing.Optional[bool]

### UnusedAccountValidityDays
- **Type**: typing.Optional[int]

### InviteMessageTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.MessageTemplateTypeTypeDef]


# AdminCreateUserRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeTypeTypeDef]]

### ValidationData
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeTypeTypeDef]]

### TemporaryPassword
- **Type**: typing.Optional[str]

### ForceAliasCreation
- **Type**: typing.Optional[bool]

### MessageAction
- **Type**: typing.Optional[typing.Literal['RESEND', 'SUPPRESS']]

### DesiredDeliveryMediums
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EMAIL', 'SMS']]]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AdminCreateUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AdminDeleteUserAttributesRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserAttributeNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AdminDeleteUserRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdminDisableProviderForUserRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ProviderUserIdentifierTypeTypeDef'>
- **Required**: Yes


# AdminDisableUserRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdminEnableUserRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdminForgetDeviceRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes


# AdminGetDeviceRequestRequestTypeDef

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdminGetDeviceResponseTypeDef

### Device
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AdminGetUserRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdminGetUserResponseTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeTypeTypeDef]
- **Required**: Yes

### UserCreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### UserLastModifiedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### UserStatus
- **Type**: typing.Literal['ARCHIVED', 'COMPROMISED', 'CONFIRMED', 'EXTERNAL_PROVIDER', 'FORCE_CHANGE_PASSWORD', 'RESET_REQUIRED', 'UNCONFIRMED', 'UNKNOWN']
- **Required**: Yes

### MFAOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.MFAOptionTypeTypeDef]
- **Required**: Yes

### PreferredMfaSetting
- **Type**: <class 'str'>
- **Required**: Yes

### UserMFASettingList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AdminInitiateAuthRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthFlow
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'ADMIN_USER_PASSWORD_AUTH', 'CUSTOM_AUTH', 'REFRESH_TOKEN', 'REFRESH_TOKEN_AUTH', 'USER_PASSWORD_AUTH', 'USER_SRP_AUTH']
- **Required**: Yes

### AuthParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AnalyticsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataTypeTypeDef]

### ContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.ContextDataTypeTypeDef]


# AdminInitiateAuthResponseTypeDef

### ChallengeName
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD_VERIFIER', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SOFTWARE_TOKEN_MFA']
- **Required**: Yes

### Session
- **Type**: <class 'str'>
- **Required**: Yes

### ChallengeParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### AuthenticationResult
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.AuthenticationResultTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AdminLinkProviderForUserRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationUser
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ProviderUserIdentifierTypeTypeDef'>
- **Required**: Yes

### SourceUser
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ProviderUserIdentifierTypeTypeDef'>
- **Required**: Yes


# AdminListDevicesRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### PaginationToken
- **Type**: typing.Optional[str]


# AdminListDevicesResponseTypeDef

### Devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceTypeTypeDef]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AdminListGroupsForUserRequestAdminListGroupsForUserPaginateTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# AdminListGroupsForUserRequestRequestTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# AdminListGroupsForUserResponseTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.GroupTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# AdminListUserAuthEventsRequestAdminListUserAuthEventsPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# AdminListUserAuthEventsRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# AdminListUserAuthEventsResponseTypeDef

### AuthEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.AuthEventTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# AdminRemoveUserFromGroupRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# AdminResetUserPasswordRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AdminRespondToAuthChallengeRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ChallengeName
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD_VERIFIER', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SOFTWARE_TOKEN_MFA']
- **Required**: Yes

### ChallengeResponses
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Session
- **Type**: typing.Optional[str]

### AnalyticsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataTypeTypeDef]

### ContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.ContextDataTypeTypeDef]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AdminRespondToAuthChallengeResponseTypeDef

### ChallengeName
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD_VERIFIER', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SOFTWARE_TOKEN_MFA']
- **Required**: Yes

### Session
- **Type**: <class 'str'>
- **Required**: Yes

### ChallengeParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### AuthenticationResult
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.AuthenticationResultTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AdminSetUserMFAPreferenceRequestRequestTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### SMSMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SMSMfaSettingsTypeTypeDef]

### SoftwareTokenMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SoftwareTokenMfaSettingsTypeTypeDef]


# AdminSetUserPasswordRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### Permanent
- **Type**: typing.Optional[bool]


# AdminSetUserSettingsRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### MFAOptions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.MFAOptionTypeTypeDef]
- **Required**: Yes


# AdminUpdateAuthEventFeedbackRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### EventId
- **Type**: <class 'str'>
- **Required**: Yes

### FeedbackValue
- **Type**: typing.Literal['Invalid', 'Valid']
- **Required**: Yes


# AdminUpdateDeviceStatusRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceRememberedStatus
- **Type**: typing.Optional[typing.Literal['not_remembered', 'remembered']]


# AdminUpdateUserAttributesRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserAttributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeTypeTypeDef]
- **Required**: Yes

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AdminUserGlobalSignOutRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AnalyticsConfigurationTypeTypeDef

### ApplicationId
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### ExternalId
- **Type**: typing.Optional[str]

### UserDataShared
- **Type**: typing.Optional[bool]


# AnalyticsMetadataTypeTypeDef

### AnalyticsEndpointId
- **Type**: typing.Optional[str]


# AssociateSoftwareTokenRequestRequestTypeDef

### AccessToken
- **Type**: typing.Optional[str]

### Session
- **Type**: typing.Optional[str]


# AssociateSoftwareTokenResponseTypeDef

### SecretCode
- **Type**: <class 'str'>
- **Required**: Yes

### Session
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttributeTypeTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# AuthEventTypeTypeDef

### EventId
- **Type**: typing.Optional[str]

### EventType
- **Type**: typing.Optional[typing.Literal['ForgotPassword', 'PasswordChange', 'ResendCode', 'SignIn', 'SignUp']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### EventResponse
- **Type**: typing.Optional[typing.Literal['Fail', 'InProgress', 'Pass']]

### EventRisk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EventRiskTypeTypeDef]

### ChallengeResponses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.ChallengeResponseTypeTypeDef]]

### EventContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EventContextDataTypeTypeDef]

### EventFeedback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EventFeedbackTypeTypeDef]


# AuthenticationResultTypeTypeDef

### AccessToken
- **Type**: typing.Optional[str]

### ExpiresIn
- **Type**: typing.Optional[int]

### TokenType
- **Type**: typing.Optional[str]

### RefreshToken
- **Type**: typing.Optional[str]

### IdToken
- **Type**: typing.Optional[str]

### NewDeviceMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.NewDeviceMetadataTypeTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChallengeResponseTypeTypeDef

### ChallengeName
- **Type**: typing.Optional[typing.Literal['Mfa', 'Password']]

### ChallengeResponse
- **Type**: typing.Optional[typing.Literal['Failure', 'Success']]


# ChangePasswordRequestRequestTypeDef

### PreviousPassword
- **Type**: <class 'str'>
- **Required**: Yes

### ProposedPassword
- **Type**: <class 'str'>
- **Required**: Yes

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# CloudWatchLogsConfigurationTypeTypeDef

### LogGroupArn
- **Type**: typing.Optional[str]


# CodeDeliveryDetailsTypeTypeDef

### Destination
- **Type**: typing.Optional[str]

### DeliveryMedium
- **Type**: typing.Optional[typing.Literal['EMAIL', 'SMS']]

### AttributeName
- **Type**: typing.Optional[str]


# CompromisedCredentialsActionsTypeTypeDef

### EventAction
- **Type**: typing.Literal['BLOCK', 'NO_ACTION']
- **Required**: Yes


# CompromisedCredentialsRiskConfigurationTypeOutputTypeDef

### Actions
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.CompromisedCredentialsActionsTypeTypeDef'>
- **Required**: Yes

### EventFilter
- **Type**: typing.Optional[typing.List[typing.Literal['PASSWORD_CHANGE', 'SIGN_IN', 'SIGN_UP']]]


# CompromisedCredentialsRiskConfigurationTypeTypeDef

### Actions
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.CompromisedCredentialsActionsTypeTypeDef'>
- **Required**: Yes

### EventFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PASSWORD_CHANGE', 'SIGN_IN', 'SIGN_UP']]]


# ConfirmDeviceRequestRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceSecretVerifierConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceSecretVerifierConfigTypeTypeDef]

### DeviceName
- **Type**: typing.Optional[str]


# ConfirmDeviceResponseTypeDef

### UserConfirmationNecessary
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfirmForgotPasswordRequestRequestTypeDef

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ConfirmationCode
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### SecretHash
- **Type**: typing.Optional[str]

### AnalyticsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataTypeTypeDef]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataTypeTypeDef]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ConfirmSignUpRequestRequestTypeDef

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ConfirmationCode
- **Type**: <class 'str'>
- **Required**: Yes

### SecretHash
- **Type**: typing.Optional[str]

### ForceAliasCreation
- **Type**: typing.Optional[bool]

### AnalyticsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataTypeTypeDef]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataTypeTypeDef]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ContextDataTypeTypeDef

### IpAddress
- **Type**: <class 'str'>
- **Required**: Yes

### ServerName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerPath
- **Type**: <class 'str'>
- **Required**: Yes

### HttpHeaders
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.HttpHeaderTypeDef]
- **Required**: Yes

### EncodedData
- **Type**: typing.Optional[str]


# CreateGroupRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Precedence
- **Type**: typing.Optional[int]


# CreateGroupResponseTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.GroupTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIdentityProviderRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderType
- **Type**: typing.Literal['Facebook', 'Google', 'LoginWithAmazon', 'OIDC', 'SAML', 'SignInWithApple']
- **Required**: Yes

### ProviderDetails
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### AttributeMapping
- **Type**: typing.Optional[typing.Mapping[str, str]]

### IdpIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateIdentityProviderResponseTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.IdentityProviderTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResourceServerRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scopes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerScopeTypeTypeDef]]


# CreateResourceServerResponseTypeDef

### ResourceServer
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserImportJobRequestRequestTypeDef

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLogsRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateUserImportJobResponseTypeDef

### UserImportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserImportJobTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserPoolClientRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientName
- **Type**: <class 'str'>
- **Required**: Yes

### GenerateSecret
- **Type**: typing.Optional[bool]

### RefreshTokenValidity
- **Type**: typing.Optional[int]

### AccessTokenValidity
- **Type**: typing.Optional[int]

### IdTokenValidity
- **Type**: typing.Optional[int]

### TokenValidityUnits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.TokenValidityUnitsTypeTypeDef]

### ReadAttributes
- **Type**: typing.Optional[typing.Sequence[str]]

### WriteAttributes
- **Type**: typing.Optional[typing.Sequence[str]]

### ExplicitAuthFlows
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ADMIN_NO_SRP_AUTH', 'ALLOW_ADMIN_USER_PASSWORD_AUTH', 'ALLOW_CUSTOM_AUTH', 'ALLOW_REFRESH_TOKEN_AUTH', 'ALLOW_USER_PASSWORD_AUTH', 'ALLOW_USER_SRP_AUTH', 'CUSTOM_AUTH_FLOW_ONLY', 'USER_PASSWORD_AUTH']]]

### SupportedIdentityProviders
- **Type**: typing.Optional[typing.Sequence[str]]

### CallbackURLs
- **Type**: typing.Optional[typing.Sequence[str]]

### LogoutURLs
- **Type**: typing.Optional[typing.Sequence[str]]

### DefaultRedirectURI
- **Type**: typing.Optional[str]

### AllowedOAuthFlows
- **Type**: typing.Optional[typing.Sequence[typing.Literal['client_credentials', 'code', 'implicit']]]

### AllowedOAuthScopes
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowedOAuthFlowsUserPoolClient
- **Type**: typing.Optional[bool]

### AnalyticsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsConfigurationTypeTypeDef]

### PreventUserExistenceErrors
- **Type**: typing.Optional[typing.Literal['ENABLED', 'LEGACY']]

### EnableTokenRevocation
- **Type**: typing.Optional[bool]

### EnablePropagateAdditionalUserContextData
- **Type**: typing.Optional[bool]

### AuthSessionValidity
- **Type**: typing.Optional[int]


# CreateUserPoolClientResponseTypeDef

### UserPoolClient
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolClientTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserPoolDomainRequestRequestTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomainConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CustomDomainConfigTypeTypeDef]


# CreateUserPoolDomainResponseTypeDef

### CloudFrontDomain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserPoolRequestRequestTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolPolicyTypeTypeDef]

### DeletionProtection
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### LambdaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.LambdaConfigTypeTypeDef]

### AutoVerifiedAttributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['email', 'phone_number']]]

### AliasAttributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['email', 'phone_number', 'preferred_username']]]

### UsernameAttributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['email', 'phone_number']]]

### SmsVerificationMessage
- **Type**: typing.Optional[str]

### EmailVerificationMessage
- **Type**: typing.Optional[str]

### EmailVerificationSubject
- **Type**: typing.Optional[str]

### VerificationMessageTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.VerificationMessageTemplateTypeTypeDef]

### SmsAuthenticationMessage
- **Type**: typing.Optional[str]

### MfaConfiguration
- **Type**: typing.Optional[typing.Literal['OFF', 'ON', 'OPTIONAL']]

### UserAttributeUpdateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserAttributeUpdateSettingsTypeTypeDef]

### DeviceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceConfigurationTypeTypeDef]

### EmailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EmailConfigurationTypeTypeDef]

### SmsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SmsConfigurationTypeTypeDef]

### UserPoolTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AdminCreateUserConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AdminCreateUserConfigTypeTypeDef]

### Schema
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.SchemaAttributeTypeTypeDef]]

### UserPoolAddOns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolAddOnsTypeTypeDef]

### UsernameConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UsernameConfigurationTypeTypeDef]

### AccountRecoverySetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountRecoverySettingTypeTypeDef]


# CreateUserPoolResponseTypeDef

### UserPool
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomDomainConfigTypeTypeDef

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# CustomEmailLambdaVersionConfigTypeTypeDef

### LambdaVersion
- **Type**: typing.Literal['V1_0']
- **Required**: Yes

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# CustomSMSLambdaVersionConfigTypeTypeDef

### LambdaVersion
- **Type**: typing.Literal['V1_0']
- **Required**: Yes

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityProviderRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceServerRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserAttributesRequestRequestTypeDef

### UserAttributeNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserPoolClientRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserPoolDomainRequestRequestTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserPoolRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityProviderRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityProviderResponseTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.IdentityProviderTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourceServerRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourceServerResponseTypeDef

### ResourceServer
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeRiskConfigurationRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: typing.Optional[str]


# DescribeRiskConfigurationResponseTypeDef

### RiskConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.RiskConfigurationTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserImportJobRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserImportJobResponseTypeDef

### UserImportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserImportJobTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserPoolClientRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserPoolClientResponseTypeDef

### UserPoolClient
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolClientTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserPoolDomainRequestRequestTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserPoolDomainResponseTypeDef

### DomainDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.DomainDescriptionTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUserPoolRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserPoolResponseTypeDef

### UserPool
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeviceConfigurationTypeTypeDef

### ChallengeRequiredOnNewDevice
- **Type**: typing.Optional[bool]

### DeviceOnlyRememberedOnUserPrompt
- **Type**: typing.Optional[bool]


# DeviceSecretVerifierConfigTypeTypeDef

### PasswordVerifier
- **Type**: typing.Optional[str]

### Salt
- **Type**: typing.Optional[str]


# DeviceTypeTypeDef

### DeviceKey
- **Type**: typing.Optional[str]

### DeviceAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeTypeTypeDef]]

### DeviceCreateDate
- **Type**: typing.Optional[datetime.datetime]

### DeviceLastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### DeviceLastAuthenticatedDate
- **Type**: typing.Optional[datetime.datetime]


# DomainDescriptionTypeTypeDef

### UserPoolId
- **Type**: typing.Optional[str]

### AWSAccountId
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### S3Bucket
- **Type**: typing.Optional[str]

### CloudFrontDistribution
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### CustomDomainConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CustomDomainConfigTypeTypeDef]


# EmailConfigurationTypeTypeDef

### SourceArn
- **Type**: typing.Optional[str]

### ReplyToEmailAddress
- **Type**: typing.Optional[str]

### EmailSendingAccount
- **Type**: typing.Optional[typing.Literal['COGNITO_DEFAULT', 'DEVELOPER']]

### From
- **Type**: typing.Optional[str]

### ConfigurationSet
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EventContextDataTypeTypeDef

### IpAddress
- **Type**: typing.Optional[str]

### DeviceName
- **Type**: typing.Optional[str]

### Timezone
- **Type**: typing.Optional[str]

### City
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]


# EventFeedbackTypeTypeDef

### FeedbackValue
- **Type**: typing.Literal['Invalid', 'Valid']
- **Required**: Yes

### Provider
- **Type**: <class 'str'>
- **Required**: Yes

### FeedbackDate
- **Type**: typing.Optional[datetime.datetime]


# EventRiskTypeTypeDef

### RiskDecision
- **Type**: typing.Optional[typing.Literal['AccountTakeover', 'Block', 'NoRisk']]

### RiskLevel
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium']]

### CompromisedCredentialsDetected
- **Type**: typing.Optional[bool]


# ForgetDeviceRequestRequestTypeDef

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes

### AccessToken
- **Type**: typing.Optional[str]


# ForgotPasswordRequestRequestTypeDef

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### SecretHash
- **Type**: typing.Optional[str]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataTypeTypeDef]

### AnalyticsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataTypeTypeDef]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ForgotPasswordResponseTypeDef

### CodeDeliveryDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.CodeDeliveryDetailsTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetCSVHeaderRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCSVHeaderResponseTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### CSVHeader
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDeviceRequestRequestTypeDef

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes

### AccessToken
- **Type**: typing.Optional[str]


# GetDeviceResponseTypeDef

### Device
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupResponseTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.GroupTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdentityProviderByIdentifierRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdpIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentityProviderByIdentifierResponseTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.IdentityProviderTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLogDeliveryConfigurationRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLogDeliveryConfigurationResponseTypeDef

### LogDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.LogDeliveryConfigurationTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSigningCertificateRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSigningCertificateResponseTypeDef

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUICustomizationRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: typing.Optional[str]


# GetUICustomizationResponseTypeDef

### UICustomization
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UICustomizationTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserAttributeVerificationCodeRequestRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetUserAttributeVerificationCodeResponseTypeDef

### CodeDeliveryDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.CodeDeliveryDetailsTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserPoolMfaConfigRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserPoolMfaConfigResponseTypeDef

### SmsMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.SmsMfaConfigTypeTypeDef'>
- **Required**: Yes

### SoftwareTokenMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.SoftwareTokenMfaConfigTypeTypeDef'>
- **Required**: Yes

### MfaConfiguration
- **Type**: typing.Literal['OFF', 'ON', 'OPTIONAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserRequestRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserResponseTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeTypeTypeDef]
- **Required**: Yes

### MFAOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.MFAOptionTypeTypeDef]
- **Required**: Yes

### PreferredMfaSetting
- **Type**: <class 'str'>
- **Required**: Yes

### UserMFASettingList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GlobalSignOutRequestRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# GroupTypeTypeDef

### GroupName
- **Type**: typing.Optional[str]

### UserPoolId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Precedence
- **Type**: typing.Optional[int]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]


# HttpHeaderTypeDef

### headerName
- **Type**: typing.Optional[str]

### headerValue
- **Type**: typing.Optional[str]


# IdentityProviderTypeTypeDef

### UserPoolId
- **Type**: typing.Optional[str]

### ProviderName
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['Facebook', 'Google', 'LoginWithAmazon', 'OIDC', 'SAML', 'SignInWithApple']]

### ProviderDetails
- **Type**: typing.Optional[typing.Dict[str, str]]

### AttributeMapping
- **Type**: typing.Optional[typing.Dict[str, str]]

### IdpIdentifiers
- **Type**: typing.Optional[typing.List[str]]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]


# InitiateAuthRequestRequestTypeDef

### AuthFlow
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'ADMIN_USER_PASSWORD_AUTH', 'CUSTOM_AUTH', 'REFRESH_TOKEN', 'REFRESH_TOKEN_AUTH', 'USER_PASSWORD_AUTH', 'USER_SRP_AUTH']
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AnalyticsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataTypeTypeDef]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataTypeTypeDef]


# InitiateAuthResponseTypeDef

### ChallengeName
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD_VERIFIER', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SOFTWARE_TOKEN_MFA']
- **Required**: Yes

### Session
- **Type**: <class 'str'>
- **Required**: Yes

### ChallengeParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### AuthenticationResult
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.AuthenticationResultTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LambdaConfigTypeTypeDef

### PreSignUp
- **Type**: typing.Optional[str]

### CustomMessage
- **Type**: typing.Optional[str]

### PostConfirmation
- **Type**: typing.Optional[str]

### PreAuthentication
- **Type**: typing.Optional[str]

### PostAuthentication
- **Type**: typing.Optional[str]

### DefineAuthChallenge
- **Type**: typing.Optional[str]

### CreateAuthChallenge
- **Type**: typing.Optional[str]

### VerifyAuthChallengeResponse
- **Type**: typing.Optional[str]

### PreTokenGeneration
- **Type**: typing.Optional[str]

### UserMigration
- **Type**: typing.Optional[str]

### PreTokenGenerationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PreTokenGenerationVersionConfigTypeTypeDef]

### CustomSMSSender
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CustomSMSLambdaVersionConfigTypeTypeDef]

### CustomEmailSender
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CustomEmailLambdaVersionConfigTypeTypeDef]

### KMSKeyID
- **Type**: typing.Optional[str]


# ListDevicesRequestRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### PaginationToken
- **Type**: typing.Optional[str]


# ListDevicesResponseTypeDef

### Devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceTypeTypeDef]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroupsRequestListGroupsPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListGroupsRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsResponseTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.GroupTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityProvidersRequestListIdentityProvidersPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListIdentityProvidersRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityProvidersResponseTypeDef

### Providers
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.ProviderDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceServersRequestListResourceServersPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListResourceServersRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceServersResponseTypeDef

### ResourceServers
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUserImportJobsRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### PaginationToken
- **Type**: typing.Optional[str]


# ListUserImportJobsResponseTypeDef

### UserImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.UserImportJobTypeTypeDef]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUserPoolClientsRequestListUserPoolClientsPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListUserPoolClientsRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListUserPoolClientsResponseTypeDef

### UserPoolClients
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolClientDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUserPoolsRequestListUserPoolsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListUserPoolsRequestRequestTypeDef

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUserPoolsResponseTypeDef

### UserPools
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolDescriptionTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsersInGroupRequestListUsersInGroupPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListUsersInGroupRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListUsersInGroupResponseTypeDef

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.UserTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequestListUsersPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### AttributesToGet
- **Type**: typing.Optional[typing.Sequence[str]]

### Filter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListUsersRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### AttributesToGet
- **Type**: typing.Optional[typing.Sequence[str]]

### Limit
- **Type**: typing.Optional[int]

### PaginationToken
- **Type**: typing.Optional[str]

### Filter
- **Type**: typing.Optional[str]


# ListUsersResponseTypeDef

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.UserTypeTypeDef]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LogConfigurationTypeTypeDef

### LogLevel
- **Type**: typing.Literal['ERROR']
- **Required**: Yes

### EventSource
- **Type**: typing.Literal['userNotification']
- **Required**: Yes

### CloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CloudWatchLogsConfigurationTypeTypeDef]


# LogDeliveryConfigurationTypeTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### LogConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.LogConfigurationTypeTypeDef]
- **Required**: Yes


# MFAOptionTypeTypeDef

### DeliveryMedium
- **Type**: typing.Optional[typing.Literal['EMAIL', 'SMS']]

### AttributeName
- **Type**: typing.Optional[str]


# MessageTemplateTypeTypeDef

### SMSMessage
- **Type**: typing.Optional[str]

### EmailMessage
- **Type**: typing.Optional[str]

### EmailSubject
- **Type**: typing.Optional[str]


# NewDeviceMetadataTypeTypeDef

### DeviceKey
- **Type**: typing.Optional[str]

### DeviceGroupKey
- **Type**: typing.Optional[str]


# NotifyConfigurationTypeTypeDef

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### From
- **Type**: typing.Optional[str]

### ReplyTo
- **Type**: typing.Optional[str]

### BlockEmail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.NotifyEmailTypeTypeDef]

### NoActionEmail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.NotifyEmailTypeTypeDef]

### MfaEmail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.NotifyEmailTypeTypeDef]


# NotifyEmailTypeTypeDef

### Subject
- **Type**: <class 'str'>
- **Required**: Yes

### HtmlBody
- **Type**: typing.Optional[str]

### TextBody
- **Type**: typing.Optional[str]


# NumberAttributeConstraintsTypeTypeDef

### MinValue
- **Type**: typing.Optional[str]

### MaxValue
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PasswordPolicyTypeTypeDef

### MinimumLength
- **Type**: typing.Optional[int]

### RequireUppercase
- **Type**: typing.Optional[bool]

### RequireLowercase
- **Type**: typing.Optional[bool]

### RequireNumbers
- **Type**: typing.Optional[bool]

### RequireSymbols
- **Type**: typing.Optional[bool]

### TemporaryPasswordValidityDays
- **Type**: typing.Optional[int]


# PreTokenGenerationVersionConfigTypeTypeDef

### LambdaVersion
- **Type**: typing.Literal['V1_0', 'V2_0']
- **Required**: Yes

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# ProviderDescriptionTypeDef

### ProviderName
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['Facebook', 'Google', 'LoginWithAmazon', 'OIDC', 'SAML', 'SignInWithApple']]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]


# ProviderUserIdentifierTypeTypeDef

### ProviderName
- **Type**: typing.Optional[str]

### ProviderAttributeName
- **Type**: typing.Optional[str]

### ProviderAttributeValue
- **Type**: typing.Optional[str]


# RecoveryOptionTypeTypeDef

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: typing.Literal['admin_only', 'verified_email', 'verified_phone_number']
- **Required**: Yes


# ResendConfirmationCodeRequestRequestTypeDef

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### SecretHash
- **Type**: typing.Optional[str]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataTypeTypeDef]

### AnalyticsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataTypeTypeDef]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ResendConfirmationCodeResponseTypeDef

### CodeDeliveryDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.CodeDeliveryDetailsTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceServerScopeTypeTypeDef

### ScopeName
- **Type**: <class 'str'>
- **Required**: Yes

### ScopeDescription
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceServerTypeTypeDef

### UserPoolId
- **Type**: typing.Optional[str]

### Identifier
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Scopes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerScopeTypeTypeDef]]


# RespondToAuthChallengeRequestRequestTypeDef

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ChallengeName
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD_VERIFIER', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SOFTWARE_TOKEN_MFA']
- **Required**: Yes

### Session
- **Type**: typing.Optional[str]

### ChallengeResponses
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AnalyticsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataTypeTypeDef]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataTypeTypeDef]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RespondToAuthChallengeResponseTypeDef

### ChallengeName
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD_VERIFIER', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SOFTWARE_TOKEN_MFA']
- **Required**: Yes

### Session
- **Type**: <class 'str'>
- **Required**: Yes

### ChallengeParameters
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### AuthenticationResult
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.AuthenticationResultTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
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


# RevokeTokenRequestRequestTypeDef

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSecret
- **Type**: typing.Optional[str]


# RiskConfigurationTypeTypeDef

### UserPoolId
- **Type**: typing.Optional[str]

### ClientId
- **Type**: typing.Optional[str]

### CompromisedCredentialsRiskConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CompromisedCredentialsRiskConfigurationTypeOutputTypeDef]

### AccountTakeoverRiskConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountTakeoverRiskConfigurationTypeTypeDef]

### RiskExceptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.RiskExceptionConfigurationTypeOutputTypeDef]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# RiskExceptionConfigurationTypeOutputTypeDef

### BlockedIPRangeList
- **Type**: typing.Optional[typing.List[str]]

### SkippedIPRangeList
- **Type**: typing.Optional[typing.List[str]]


# RiskExceptionConfigurationTypeTypeDef

### BlockedIPRangeList
- **Type**: typing.Optional[typing.Sequence[str]]

### SkippedIPRangeList
- **Type**: typing.Optional[typing.Sequence[str]]


# SMSMfaSettingsTypeTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### PreferredMfa
- **Type**: typing.Optional[bool]


# SchemaAttributeTypeTypeDef

### Name
- **Type**: typing.Optional[str]

### AttributeDataType
- **Type**: typing.Optional[typing.Literal['Boolean', 'DateTime', 'Number', 'String']]

### DeveloperOnlyAttribute
- **Type**: typing.Optional[bool]

### Mutable
- **Type**: typing.Optional[bool]

### Required
- **Type**: typing.Optional[bool]

### NumberAttributeConstraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.NumberAttributeConstraintsTypeTypeDef]

### StringAttributeConstraints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.StringAttributeConstraintsTypeTypeDef]


# SetLogDeliveryConfigurationRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### LogConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.LogConfigurationTypeTypeDef]
- **Required**: Yes


# SetLogDeliveryConfigurationResponseTypeDef

### LogDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.LogDeliveryConfigurationTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetRiskConfigurationRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: typing.Optional[str]

### CompromisedCredentialsRiskConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CompromisedCredentialsRiskConfigurationTypeTypeDef]

### AccountTakeoverRiskConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountTakeoverRiskConfigurationTypeTypeDef]

### RiskExceptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.RiskExceptionConfigurationTypeTypeDef]


# SetRiskConfigurationResponseTypeDef

### RiskConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.RiskConfigurationTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetUICustomizationRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: typing.Optional[str]

### CSS
- **Type**: typing.Optional[str]

### ImageFile
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# SetUICustomizationResponseTypeDef

### UICustomization
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UICustomizationTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetUserMFAPreferenceRequestRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### SMSMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SMSMfaSettingsTypeTypeDef]

### SoftwareTokenMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SoftwareTokenMfaSettingsTypeTypeDef]


# SetUserPoolMfaConfigRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### SmsMfaConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SmsMfaConfigTypeTypeDef]

### SoftwareTokenMfaConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SoftwareTokenMfaConfigTypeTypeDef]

### MfaConfiguration
- **Type**: typing.Optional[typing.Literal['OFF', 'ON', 'OPTIONAL']]


# SetUserPoolMfaConfigResponseTypeDef

### SmsMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.SmsMfaConfigTypeTypeDef'>
- **Required**: Yes

### SoftwareTokenMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.SoftwareTokenMfaConfigTypeTypeDef'>
- **Required**: Yes

### MfaConfiguration
- **Type**: typing.Literal['OFF', 'ON', 'OPTIONAL']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetUserSettingsRequestRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### MFAOptions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.MFAOptionTypeTypeDef]
- **Required**: Yes


# SignUpRequestRequestTypeDef

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### SecretHash
- **Type**: typing.Optional[str]

### UserAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeTypeTypeDef]]

### ValidationData
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeTypeTypeDef]]

### AnalyticsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataTypeTypeDef]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataTypeTypeDef]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# SignUpResponseTypeDef

### UserConfirmed
- **Type**: <class 'bool'>
- **Required**: Yes

### CodeDeliveryDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.CodeDeliveryDetailsTypeTypeDef'>
- **Required**: Yes

### UserSub
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SmsConfigurationTypeTypeDef

### SnsCallerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: typing.Optional[str]

### SnsRegion
- **Type**: typing.Optional[str]


# SmsMfaConfigTypeTypeDef

### SmsAuthenticationMessage
- **Type**: typing.Optional[str]

### SmsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SmsConfigurationTypeTypeDef]


# SoftwareTokenMfaConfigTypeTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# SoftwareTokenMfaSettingsTypeTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### PreferredMfa
- **Type**: typing.Optional[bool]


# StartUserImportJobRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StartUserImportJobResponseTypeDef

### UserImportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserImportJobTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopUserImportJobRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopUserImportJobResponseTypeDef

### UserImportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserImportJobTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StringAttributeConstraintsTypeTypeDef

### MinLength
- **Type**: typing.Optional[str]

### MaxLength
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TokenValidityUnitsTypeTypeDef

### AccessToken
- **Type**: typing.Optional[typing.Literal['days', 'hours', 'minutes', 'seconds']]

### IdToken
- **Type**: typing.Optional[typing.Literal['days', 'hours', 'minutes', 'seconds']]

### RefreshToken
- **Type**: typing.Optional[typing.Literal['days', 'hours', 'minutes', 'seconds']]


# UICustomizationTypeTypeDef

### UserPoolId
- **Type**: typing.Optional[str]

### ClientId
- **Type**: typing.Optional[str]

### ImageUrl
- **Type**: typing.Optional[str]

### CSS
- **Type**: typing.Optional[str]

### CSSVersion
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAuthEventFeedbackRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### EventId
- **Type**: <class 'str'>
- **Required**: Yes

### FeedbackToken
- **Type**: <class 'str'>
- **Required**: Yes

### FeedbackValue
- **Type**: typing.Literal['Invalid', 'Valid']
- **Required**: Yes


# UpdateDeviceStatusRequestRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceRememberedStatus
- **Type**: typing.Optional[typing.Literal['not_remembered', 'remembered']]


# UpdateGroupRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]

### Precedence
- **Type**: typing.Optional[int]


# UpdateGroupResponseTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.GroupTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIdentityProviderRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderDetails
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AttributeMapping
- **Type**: typing.Optional[typing.Mapping[str, str]]

### IdpIdentifiers
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateIdentityProviderResponseTypeDef

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.IdentityProviderTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateResourceServerRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Scopes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerScopeTypeTypeDef]]


# UpdateResourceServerResponseTypeDef

### ResourceServer
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserAttributesRequestRequestTypeDef

### UserAttributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeTypeTypeDef]
- **Required**: Yes

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateUserAttributesResponseTypeDef

### CodeDeliveryDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.CodeDeliveryDetailsTypeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserPoolClientRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientName
- **Type**: typing.Optional[str]

### RefreshTokenValidity
- **Type**: typing.Optional[int]

### AccessTokenValidity
- **Type**: typing.Optional[int]

### IdTokenValidity
- **Type**: typing.Optional[int]

### TokenValidityUnits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.TokenValidityUnitsTypeTypeDef]

### ReadAttributes
- **Type**: typing.Optional[typing.Sequence[str]]

### WriteAttributes
- **Type**: typing.Optional[typing.Sequence[str]]

### ExplicitAuthFlows
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ADMIN_NO_SRP_AUTH', 'ALLOW_ADMIN_USER_PASSWORD_AUTH', 'ALLOW_CUSTOM_AUTH', 'ALLOW_REFRESH_TOKEN_AUTH', 'ALLOW_USER_PASSWORD_AUTH', 'ALLOW_USER_SRP_AUTH', 'CUSTOM_AUTH_FLOW_ONLY', 'USER_PASSWORD_AUTH']]]

### SupportedIdentityProviders
- **Type**: typing.Optional[typing.Sequence[str]]

### CallbackURLs
- **Type**: typing.Optional[typing.Sequence[str]]

### LogoutURLs
- **Type**: typing.Optional[typing.Sequence[str]]

### DefaultRedirectURI
- **Type**: typing.Optional[str]

### AllowedOAuthFlows
- **Type**: typing.Optional[typing.Sequence[typing.Literal['client_credentials', 'code', 'implicit']]]

### AllowedOAuthScopes
- **Type**: typing.Optional[typing.Sequence[str]]

### AllowedOAuthFlowsUserPoolClient
- **Type**: typing.Optional[bool]

### AnalyticsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsConfigurationTypeTypeDef]

### PreventUserExistenceErrors
- **Type**: typing.Optional[typing.Literal['ENABLED', 'LEGACY']]

### EnableTokenRevocation
- **Type**: typing.Optional[bool]

### EnablePropagateAdditionalUserContextData
- **Type**: typing.Optional[bool]

### AuthSessionValidity
- **Type**: typing.Optional[int]


# UpdateUserPoolClientResponseTypeDef

### UserPoolClient
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolClientTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserPoolDomainRequestRequestTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomDomainConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.CustomDomainConfigTypeTypeDef'>
- **Required**: Yes


# UpdateUserPoolDomainResponseTypeDef

### CloudFrontDomain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserPoolRequestRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolPolicyTypeTypeDef]

### DeletionProtection
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### LambdaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.LambdaConfigTypeTypeDef]

### AutoVerifiedAttributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['email', 'phone_number']]]

### SmsVerificationMessage
- **Type**: typing.Optional[str]

### EmailVerificationMessage
- **Type**: typing.Optional[str]

### EmailVerificationSubject
- **Type**: typing.Optional[str]

### VerificationMessageTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.VerificationMessageTemplateTypeTypeDef]

### SmsAuthenticationMessage
- **Type**: typing.Optional[str]

### UserAttributeUpdateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserAttributeUpdateSettingsTypeTypeDef]

### MfaConfiguration
- **Type**: typing.Optional[typing.Literal['OFF', 'ON', 'OPTIONAL']]

### DeviceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceConfigurationTypeTypeDef]

### EmailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EmailConfigurationTypeTypeDef]

### SmsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SmsConfigurationTypeTypeDef]

### UserPoolTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AdminCreateUserConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AdminCreateUserConfigTypeTypeDef]

### UserPoolAddOns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolAddOnsTypeTypeDef]

### AccountRecoverySetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountRecoverySettingTypeTypeDef]


# UserAttributeUpdateSettingsTypeOutputTypeDef

### AttributesRequireVerificationBeforeUpdate
- **Type**: typing.Optional[typing.List[typing.Literal['email', 'phone_number']]]


# UserAttributeUpdateSettingsTypeTypeDef

### AttributesRequireVerificationBeforeUpdate
- **Type**: typing.Optional[typing.Sequence[typing.Literal['email', 'phone_number']]]


# UserContextDataTypeTypeDef

### IpAddress
- **Type**: typing.Optional[str]

### EncodedData
- **Type**: typing.Optional[str]


# UserImportJobTypeTypeDef

### JobName
- **Type**: typing.Optional[str]

### JobId
- **Type**: typing.Optional[str]

### UserPoolId
- **Type**: typing.Optional[str]

### PreSignedUrl
- **Type**: typing.Optional[str]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### StartDate
- **Type**: typing.Optional[datetime.datetime]

### CompletionDate
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['Created', 'Expired', 'Failed', 'InProgress', 'Pending', 'Stopped', 'Stopping', 'Succeeded']]

### CloudWatchLogsRoleArn
- **Type**: typing.Optional[str]

### ImportedUsers
- **Type**: typing.Optional[int]

### SkippedUsers
- **Type**: typing.Optional[int]

### FailedUsers
- **Type**: typing.Optional[int]

### CompletionMessage
- **Type**: typing.Optional[str]


# UserPoolAddOnsTypeTypeDef

### AdvancedSecurityMode
- **Type**: typing.Literal['AUDIT', 'ENFORCED', 'OFF']
- **Required**: Yes


# UserPoolClientDescriptionTypeDef

### ClientId
- **Type**: typing.Optional[str]

### UserPoolId
- **Type**: typing.Optional[str]

### ClientName
- **Type**: typing.Optional[str]


# UserPoolClientTypeTypeDef

### UserPoolId
- **Type**: typing.Optional[str]

### ClientName
- **Type**: typing.Optional[str]

### ClientId
- **Type**: typing.Optional[str]

### ClientSecret
- **Type**: typing.Optional[str]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### RefreshTokenValidity
- **Type**: typing.Optional[int]

### AccessTokenValidity
- **Type**: typing.Optional[int]

### IdTokenValidity
- **Type**: typing.Optional[int]

### TokenValidityUnits
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.TokenValidityUnitsTypeTypeDef]

### ReadAttributes
- **Type**: typing.Optional[typing.List[str]]

### WriteAttributes
- **Type**: typing.Optional[typing.List[str]]

### ExplicitAuthFlows
- **Type**: typing.Optional[typing.List[typing.Literal['ADMIN_NO_SRP_AUTH', 'ALLOW_ADMIN_USER_PASSWORD_AUTH', 'ALLOW_CUSTOM_AUTH', 'ALLOW_REFRESH_TOKEN_AUTH', 'ALLOW_USER_PASSWORD_AUTH', 'ALLOW_USER_SRP_AUTH', 'CUSTOM_AUTH_FLOW_ONLY', 'USER_PASSWORD_AUTH']]]

### SupportedIdentityProviders
- **Type**: typing.Optional[typing.List[str]]

### CallbackURLs
- **Type**: typing.Optional[typing.List[str]]

### LogoutURLs
- **Type**: typing.Optional[typing.List[str]]

### DefaultRedirectURI
- **Type**: typing.Optional[str]

### AllowedOAuthFlows
- **Type**: typing.Optional[typing.List[typing.Literal['client_credentials', 'code', 'implicit']]]

### AllowedOAuthScopes
- **Type**: typing.Optional[typing.List[str]]

### AllowedOAuthFlowsUserPoolClient
- **Type**: typing.Optional[bool]

### AnalyticsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsConfigurationTypeTypeDef]

### PreventUserExistenceErrors
- **Type**: typing.Optional[typing.Literal['ENABLED', 'LEGACY']]

### EnableTokenRevocation
- **Type**: typing.Optional[bool]

### EnablePropagateAdditionalUserContextData
- **Type**: typing.Optional[bool]

### AuthSessionValidity
- **Type**: typing.Optional[int]


# UserPoolDescriptionTypeTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### LambdaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.LambdaConfigTypeTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]


# UserPoolPolicyTypeTypeDef

### PasswordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PasswordPolicyTypeTypeDef]


# UserPoolTypeTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolPolicyTypeTypeDef]

### DeletionProtection
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### LambdaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.LambdaConfigTypeTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### SchemaAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.SchemaAttributeTypeTypeDef]]

### AutoVerifiedAttributes
- **Type**: typing.Optional[typing.List[typing.Literal['email', 'phone_number']]]

### AliasAttributes
- **Type**: typing.Optional[typing.List[typing.Literal['email', 'phone_number', 'preferred_username']]]

### UsernameAttributes
- **Type**: typing.Optional[typing.List[typing.Literal['email', 'phone_number']]]

### SmsVerificationMessage
- **Type**: typing.Optional[str]

### EmailVerificationMessage
- **Type**: typing.Optional[str]

### EmailVerificationSubject
- **Type**: typing.Optional[str]

### VerificationMessageTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.VerificationMessageTemplateTypeTypeDef]

### SmsAuthenticationMessage
- **Type**: typing.Optional[str]

### UserAttributeUpdateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserAttributeUpdateSettingsTypeOutputTypeDef]

### MfaConfiguration
- **Type**: typing.Optional[typing.Literal['OFF', 'ON', 'OPTIONAL']]

### DeviceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceConfigurationTypeTypeDef]

### EstimatedNumberOfUsers
- **Type**: typing.Optional[int]

### EmailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EmailConfigurationTypeTypeDef]

### SmsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SmsConfigurationTypeTypeDef]

### UserPoolTags
- **Type**: typing.Optional[typing.Dict[str, str]]

### SmsConfigurationFailure
- **Type**: typing.Optional[str]

### EmailConfigurationFailure
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### CustomDomain
- **Type**: typing.Optional[str]

### AdminCreateUserConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AdminCreateUserConfigTypeTypeDef]

### UserPoolAddOns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolAddOnsTypeTypeDef]

### UsernameConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UsernameConfigurationTypeTypeDef]

### Arn
- **Type**: typing.Optional[str]

### AccountRecoverySetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountRecoverySettingTypeOutputTypeDef]


# UserTypeTypeDef

### Username
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeTypeTypeDef]]

### UserCreateDate
- **Type**: typing.Optional[datetime.datetime]

### UserLastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### Enabled
- **Type**: typing.Optional[bool]

### UserStatus
- **Type**: typing.Optional[typing.Literal['ARCHIVED', 'COMPROMISED', 'CONFIRMED', 'EXTERNAL_PROVIDER', 'FORCE_CHANGE_PASSWORD', 'RESET_REQUIRED', 'UNCONFIRMED', 'UNKNOWN']]

### MFAOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.MFAOptionTypeTypeDef]]


# UsernameConfigurationTypeTypeDef

### CaseSensitive
- **Type**: <class 'bool'>
- **Required**: Yes


# VerificationMessageTemplateTypeTypeDef

### SmsMessage
- **Type**: typing.Optional[str]

### EmailMessage
- **Type**: typing.Optional[str]

### EmailSubject
- **Type**: typing.Optional[str]

### EmailMessageByLink
- **Type**: typing.Optional[str]

### EmailSubjectByLink
- **Type**: typing.Optional[str]

### DefaultEmailOption
- **Type**: typing.Optional[typing.Literal['CONFIRM_WITH_CODE', 'CONFIRM_WITH_LINK']]


# VerifySoftwareTokenRequestRequestTypeDef

### UserCode
- **Type**: <class 'str'>
- **Required**: Yes

### AccessToken
- **Type**: typing.Optional[str]

### Session
- **Type**: typing.Optional[str]

### FriendlyDeviceName
- **Type**: typing.Optional[str]


# VerifySoftwareTokenResponseTypeDef

### Status
- **Type**: typing.Literal['ERROR', 'SUCCESS']
- **Required**: Yes

### Session
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VerifyUserAttributeRequestRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: <class 'str'>
- **Required**: Yes


