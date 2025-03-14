# Cognito Idp Classes

# AccountRecoverySettingTypeOutputTypeDef

### RecoveryMechanisms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.RecoveryOptionTypeTypeDef]]


# AccountRecoverySettingTypeTypeDef

### RecoveryMechanisms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.RecoveryOptionTypeTypeDef]]


# AccountRecoverySettingTypeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# AddCustomAttributesRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomAttributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.SchemaAttributeTypeTypeDef]
- **Required**: Yes


# AdminAddUserToGroupRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# AdminConfirmSignUpRequestTypeDef

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


# AdminCreateUserRequestTypeDef

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


# AdminDeleteUserAttributesRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserAttributeNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AdminDeleteUserRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdminDisableProviderForUserRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ProviderUserIdentifierTypeTypeDef'>
- **Required**: Yes


# AdminDisableUserRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdminEnableUserRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdminForgetDeviceRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes


# AdminGetDeviceRequestTypeDef

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


# AdminGetUserRequestTypeDef

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


# AdminInitiateAuthRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthFlow
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'ADMIN_USER_PASSWORD_AUTH', 'CUSTOM_AUTH', 'REFRESH_TOKEN', 'REFRESH_TOKEN_AUTH', 'USER_AUTH', 'USER_PASSWORD_AUTH', 'USER_SRP_AUTH']
- **Required**: Yes

### AuthParameters
- **Type**: typing.Optional[typing.Mapping[str, str]]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AnalyticsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataTypeTypeDef]

### ContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.ContextDataTypeTypeDef]

### Session
- **Type**: typing.Optional[str]


# AdminInitiateAuthResponseTypeDef

### ChallengeName
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'EMAIL_OTP', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD', 'PASSWORD_SRP', 'PASSWORD_VERIFIER', 'SELECT_CHALLENGE', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SMS_OTP', 'SOFTWARE_TOKEN_MFA', 'WEB_AUTHN']
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

### AvailableChallenges
- **Type**: typing.List[typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'EMAIL_OTP', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD', 'PASSWORD_SRP', 'PASSWORD_VERIFIER', 'SELECT_CHALLENGE', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SMS_OTP', 'SOFTWARE_TOKEN_MFA', 'WEB_AUTHN']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AdminLinkProviderForUserRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationUser
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ProviderUserIdentifierTypeTypeDef'>
- **Required**: Yes

### SourceUser
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ProviderUserIdentifierTypeTypeDef'>
- **Required**: Yes


# AdminListDevicesRequestTypeDef

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


# AdminListGroupsForUserRequestPaginateTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# AdminListGroupsForUserRequestTypeDef

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


# AdminListUserAuthEventsRequestPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# AdminListUserAuthEventsRequestTypeDef

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


# AdminRemoveUserFromGroupRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# AdminResetUserPasswordRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AdminRespondToAuthChallengeRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ChallengeName
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'EMAIL_OTP', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD', 'PASSWORD_SRP', 'PASSWORD_VERIFIER', 'SELECT_CHALLENGE', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SMS_OTP', 'SOFTWARE_TOKEN_MFA', 'WEB_AUTHN']
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
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'EMAIL_OTP', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD', 'PASSWORD_SRP', 'PASSWORD_VERIFIER', 'SELECT_CHALLENGE', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SMS_OTP', 'SOFTWARE_TOKEN_MFA', 'WEB_AUTHN']
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


# AdminSetUserMFAPreferenceRequestTypeDef

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

### EmailMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EmailMfaSettingsTypeTypeDef]


# AdminSetUserPasswordRequestTypeDef

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


# AdminSetUserSettingsRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### MFAOptions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.MFAOptionTypeTypeDef]
- **Required**: Yes


# AdminUpdateAuthEventFeedbackRequestTypeDef

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


# AdminUpdateDeviceStatusRequestTypeDef

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


# AdminUpdateUserAttributesRequestTypeDef

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


# AdminUserGlobalSignOutRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdvancedSecurityAdditionalFlowsTypeTypeDef

### CustomAuthMode
- **Type**: typing.Optional[typing.Literal['AUDIT', 'ENFORCED']]


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


# AssetTypeOutputTypeDef

### Category
- **Type**: typing.Literal['AUTH_APP_GRAPHIC', 'EMAIL_GRAPHIC', 'FAVICON_ICO', 'FAVICON_SVG', 'FORM_BACKGROUND', 'FORM_LOGO', 'IDP_BUTTON_ICON', 'PAGE_BACKGROUND', 'PAGE_FOOTER_BACKGROUND', 'PAGE_FOOTER_LOGO', 'PAGE_HEADER_BACKGROUND', 'PAGE_HEADER_LOGO', 'PASSKEY_GRAPHIC', 'PASSWORD_GRAPHIC', 'SMS_GRAPHIC']
- **Required**: Yes

### ColorMode
- **Type**: typing.Literal['DARK', 'DYNAMIC', 'LIGHT']
- **Required**: Yes

### Extension
- **Type**: typing.Literal['ICO', 'JPEG', 'PNG', 'SVG', 'WEBP']
- **Required**: Yes

### Bytes
- **Type**: typing.Optional[bytes]

### ResourceId
- **Type**: typing.Optional[str]


# AssetTypeTypeDef

### Category
- **Type**: typing.Literal['AUTH_APP_GRAPHIC', 'EMAIL_GRAPHIC', 'FAVICON_ICO', 'FAVICON_SVG', 'FORM_BACKGROUND', 'FORM_LOGO', 'IDP_BUTTON_ICON', 'PAGE_BACKGROUND', 'PAGE_FOOTER_BACKGROUND', 'PAGE_FOOTER_LOGO', 'PAGE_HEADER_BACKGROUND', 'PAGE_HEADER_LOGO', 'PASSKEY_GRAPHIC', 'PASSWORD_GRAPHIC', 'SMS_GRAPHIC']
- **Required**: Yes

### ColorMode
- **Type**: typing.Literal['DARK', 'DYNAMIC', 'LIGHT']
- **Required**: Yes

### Extension
- **Type**: typing.Literal['ICO', 'JPEG', 'PNG', 'SVG', 'WEBP']
- **Required**: Yes

### Bytes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.BlobTypeDef]

### ResourceId
- **Type**: typing.Optional[str]


# AssetTypeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateSoftwareTokenRequestTypeDef

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

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChallengeResponseTypeTypeDef

### ChallengeName
- **Type**: typing.Optional[typing.Literal['Mfa', 'Password']]

### ChallengeResponse
- **Type**: typing.Optional[typing.Literal['Failure', 'Success']]


# ChangePasswordRequestTypeDef

### ProposedPassword
- **Type**: <class 'str'>
- **Required**: Yes

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### PreviousPassword
- **Type**: typing.Optional[str]


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


# CompleteWebAuthnRegistrationRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### Credential
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


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


# CompromisedCredentialsRiskConfigurationTypeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfirmDeviceRequestTypeDef

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


# ConfirmForgotPasswordRequestTypeDef

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


# ConfirmSignUpRequestTypeDef

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

### Session
- **Type**: typing.Optional[str]


# ConfirmSignUpResponseTypeDef

### Session
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# CreateGroupRequestTypeDef

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


# CreateIdentityProviderRequestTypeDef

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


# CreateManagedLoginBrandingRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### UseCognitoProvidedValues
- **Type**: typing.Optional[bool]

### Settings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Assets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AssetTypeUnionTypeDef]]


# CreateManagedLoginBrandingResponseTypeDef

### ManagedLoginBranding
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ManagedLoginBrandingTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResourceServerRequestTypeDef

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


# CreateUserImportJobRequestTypeDef

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


# CreateUserPoolClientRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ADMIN_NO_SRP_AUTH', 'ALLOW_ADMIN_USER_PASSWORD_AUTH', 'ALLOW_CUSTOM_AUTH', 'ALLOW_REFRESH_TOKEN_AUTH', 'ALLOW_USER_AUTH', 'ALLOW_USER_PASSWORD_AUTH', 'ALLOW_USER_SRP_AUTH', 'CUSTOM_AUTH_FLOW_ONLY', 'USER_PASSWORD_AUTH']]]

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


# CreateUserPoolDomainRequestTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedLoginVersion
- **Type**: typing.Optional[int]

### CustomDomainConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CustomDomainConfigTypeTypeDef]


# CreateUserPoolDomainResponseTypeDef

### ManagedLoginVersion
- **Type**: <class 'int'>
- **Required**: Yes

### CloudFrontDomain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserPoolRequestTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolPolicyTypeUnionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserAttributeUpdateSettingsTypeUnionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountRecoverySettingTypeUnionTypeDef]

### UserPoolTier
- **Type**: typing.Optional[typing.Literal['ESSENTIALS', 'LITE', 'PLUS']]


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


# DeleteGroupRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityProviderRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteManagedLoginBrandingRequestTypeDef

### ManagedLoginBrandingId
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceServerRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserAttributesRequestTypeDef

### UserAttributeNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserPoolClientRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserPoolDomainRequestTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserPoolRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebAuthnCredentialRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### CredentialId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityProviderRequestTypeDef

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


# DescribeManagedLoginBrandingByClientRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ReturnMergedResources
- **Type**: typing.Optional[bool]


# DescribeManagedLoginBrandingByClientResponseTypeDef

### ManagedLoginBranding
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ManagedLoginBrandingTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeManagedLoginBrandingRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedLoginBrandingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReturnMergedResources
- **Type**: typing.Optional[bool]


# DescribeManagedLoginBrandingResponseTypeDef

### ManagedLoginBranding
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ManagedLoginBrandingTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourceServerRequestTypeDef

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


# DescribeRiskConfigurationRequestTypeDef

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


# DescribeUserImportJobRequestTypeDef

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


# DescribeUserPoolClientRequestTypeDef

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


# DescribeUserPoolDomainRequestTypeDef

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


# DescribeUserPoolRequestTypeDef

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

### ManagedLoginVersion
- **Type**: typing.Optional[int]


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


# EmailMfaConfigTypeTypeDef

### Message
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]


# EmailMfaSettingsTypeTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### PreferredMfa
- **Type**: typing.Optional[bool]


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


# FirehoseConfigurationTypeTypeDef

### StreamArn
- **Type**: typing.Optional[str]


# ForgetDeviceRequestTypeDef

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes

### AccessToken
- **Type**: typing.Optional[str]


# ForgotPasswordRequestTypeDef

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


# GetCSVHeaderRequestTypeDef

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


# GetDeviceRequestTypeDef

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


# GetGroupRequestTypeDef

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


# GetIdentityProviderByIdentifierRequestTypeDef

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


# GetLogDeliveryConfigurationRequestTypeDef

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


# GetSigningCertificateRequestTypeDef

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


# GetUICustomizationRequestTypeDef

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


# GetUserAttributeVerificationCodeRequestTypeDef

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


# GetUserAuthFactorsRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserAuthFactorsResponseTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### PreferredMfaSetting
- **Type**: <class 'str'>
- **Required**: Yes

### UserMFASettingList
- **Type**: typing.List[str]
- **Required**: Yes

### ConfiguredUserAuthFactors
- **Type**: typing.List[typing.Literal['EMAIL_OTP', 'PASSWORD', 'SMS_OTP', 'WEB_AUTHN']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserPoolMfaConfigRequestTypeDef

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

### EmailMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.EmailMfaConfigTypeTypeDef'>
- **Required**: Yes

### MfaConfiguration
- **Type**: typing.Literal['OFF', 'ON', 'OPTIONAL']
- **Required**: Yes

### WebAuthnConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.WebAuthnConfigurationTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserRequestTypeDef

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


# GlobalSignOutRequestTypeDef

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


# InitiateAuthRequestTypeDef

### AuthFlow
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'ADMIN_USER_PASSWORD_AUTH', 'CUSTOM_AUTH', 'REFRESH_TOKEN', 'REFRESH_TOKEN_AUTH', 'USER_AUTH', 'USER_PASSWORD_AUTH', 'USER_SRP_AUTH']
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

### Session
- **Type**: typing.Optional[str]


# InitiateAuthResponseTypeDef

### ChallengeName
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'EMAIL_OTP', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD', 'PASSWORD_SRP', 'PASSWORD_VERIFIER', 'SELECT_CHALLENGE', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SMS_OTP', 'SOFTWARE_TOKEN_MFA', 'WEB_AUTHN']
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

### AvailableChallenges
- **Type**: typing.List[typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'EMAIL_OTP', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD', 'PASSWORD_SRP', 'PASSWORD_VERIFIER', 'SELECT_CHALLENGE', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SMS_OTP', 'SOFTWARE_TOKEN_MFA', 'WEB_AUTHN']]
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


# ListDevicesRequestTypeDef

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


# ListGroupsRequestPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListGroupsRequestTypeDef

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


# ListIdentityProvidersRequestPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListIdentityProvidersRequestTypeDef

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


# ListResourceServersRequestPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListResourceServersRequestTypeDef

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


# ListTagsForResourceRequestTypeDef

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


# ListUserImportJobsRequestTypeDef

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


# ListUserPoolClientsRequestPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListUserPoolClientsRequestTypeDef

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


# ListUserPoolsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListUserPoolsRequestTypeDef

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


# ListUsersInGroupRequestPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListUsersInGroupRequestTypeDef

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


# ListUsersRequestPaginateTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### AttributesToGet
- **Type**: typing.Optional[typing.Sequence[str]]

### Filter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfigTypeDef]


# ListUsersRequestTypeDef

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


# ListWebAuthnCredentialsRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWebAuthnCredentialsResponseTypeDef

### Credentials
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.WebAuthnCredentialDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LogConfigurationTypeTypeDef

### LogLevel
- **Type**: typing.Literal['ERROR', 'INFO']
- **Required**: Yes

### EventSource
- **Type**: typing.Literal['userAuthEvents', 'userNotification']
- **Required**: Yes

### CloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CloudWatchLogsConfigurationTypeTypeDef]

### S3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.S3ConfigurationTypeTypeDef]

### FirehoseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.FirehoseConfigurationTypeTypeDef]


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


# ManagedLoginBrandingTypeTypeDef

### ManagedLoginBrandingId
- **Type**: typing.Optional[str]

### UserPoolId
- **Type**: typing.Optional[str]

### UseCognitoProvidedValues
- **Type**: typing.Optional[bool]

### Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Assets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.AssetTypeOutputTypeDef]]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


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

### PasswordHistorySize
- **Type**: typing.Optional[int]

### TemporaryPasswordValidityDays
- **Type**: typing.Optional[int]


# PreTokenGenerationVersionConfigTypeTypeDef

### LambdaVersion
- **Type**: typing.Literal['V1_0', 'V2_0', 'V3_0']
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


# ResendConfirmationCodeRequestTypeDef

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


# RespondToAuthChallengeRequestTypeDef

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ChallengeName
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'EMAIL_OTP', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD', 'PASSWORD_SRP', 'PASSWORD_VERIFIER', 'SELECT_CHALLENGE', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SMS_OTP', 'SOFTWARE_TOKEN_MFA', 'WEB_AUTHN']
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
- **Type**: typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'EMAIL_OTP', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD', 'PASSWORD_SRP', 'PASSWORD_VERIFIER', 'SELECT_CHALLENGE', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SMS_OTP', 'SOFTWARE_TOKEN_MFA', 'WEB_AUTHN']
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


# RevokeTokenRequestTypeDef

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


# RiskExceptionConfigurationTypeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3ConfigurationTypeTypeDef

### BucketArn
- **Type**: typing.Optional[str]


# SMSMfaSettingsTypeTypeDef

### Enabled
- **Type**: typing.Optional[bool]

### PreferredMfa
- **Type**: typing.Optional[bool]


# SchemaAttributeTypeTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SetLogDeliveryConfigurationRequestTypeDef

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


# SetRiskConfigurationRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: typing.Optional[str]

### CompromisedCredentialsRiskConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CompromisedCredentialsRiskConfigurationTypeUnionTypeDef]

### AccountTakeoverRiskConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountTakeoverRiskConfigurationTypeTypeDef]

### RiskExceptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.RiskExceptionConfigurationTypeUnionTypeDef]


# SetRiskConfigurationResponseTypeDef

### RiskConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.RiskConfigurationTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetUICustomizationRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: typing.Optional[str]

### CSS
- **Type**: typing.Optional[str]

### ImageFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.BlobTypeDef]


# SetUICustomizationResponseTypeDef

### UICustomization
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UICustomizationTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetUserMFAPreferenceRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### SMSMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SMSMfaSettingsTypeTypeDef]

### SoftwareTokenMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SoftwareTokenMfaSettingsTypeTypeDef]

### EmailMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EmailMfaSettingsTypeTypeDef]


# SetUserPoolMfaConfigRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### SmsMfaConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SmsMfaConfigTypeTypeDef]

### SoftwareTokenMfaConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SoftwareTokenMfaConfigTypeTypeDef]

### EmailMfaConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EmailMfaConfigTypeTypeDef]

### MfaConfiguration
- **Type**: typing.Optional[typing.Literal['OFF', 'ON', 'OPTIONAL']]

### WebAuthnConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.WebAuthnConfigurationTypeTypeDef]


# SetUserPoolMfaConfigResponseTypeDef

### SmsMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.SmsMfaConfigTypeTypeDef'>
- **Required**: Yes

### SoftwareTokenMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.SoftwareTokenMfaConfigTypeTypeDef'>
- **Required**: Yes

### EmailMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.EmailMfaConfigTypeTypeDef'>
- **Required**: Yes

### MfaConfiguration
- **Type**: typing.Literal['OFF', 'ON', 'OPTIONAL']
- **Required**: Yes

### WebAuthnConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.WebAuthnConfigurationTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetUserSettingsRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### MFAOptions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.MFAOptionTypeTypeDef]
- **Required**: Yes


# SignInPolicyTypeOutputTypeDef

### AllowedFirstAuthFactors
- **Type**: typing.Optional[typing.List[typing.Literal['EMAIL_OTP', 'PASSWORD', 'SMS_OTP', 'WEB_AUTHN']]]


# SignInPolicyTypeTypeDef

### AllowedFirstAuthFactors
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EMAIL_OTP', 'PASSWORD', 'SMS_OTP', 'WEB_AUTHN']]]


# SignUpRequestTypeDef

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### SecretHash
- **Type**: typing.Optional[str]

### Password
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

### Session
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


# StartUserImportJobRequestTypeDef

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


# StartWebAuthnRegistrationRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# StartWebAuthnRegistrationResponseTypeDef

### CredentialCreationOptions
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopUserImportJobRequestTypeDef

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


# TagResourceRequestTypeDef

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


# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAuthEventFeedbackRequestTypeDef

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


# UpdateDeviceStatusRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceRememberedStatus
- **Type**: typing.Optional[typing.Literal['not_remembered', 'remembered']]


# UpdateGroupRequestTypeDef

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


# UpdateIdentityProviderRequestTypeDef

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


# UpdateManagedLoginBrandingRequestTypeDef

### UserPoolId
- **Type**: typing.Optional[str]

### ManagedLoginBrandingId
- **Type**: typing.Optional[str]

### UseCognitoProvidedValues
- **Type**: typing.Optional[bool]

### Settings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Assets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AssetTypeUnionTypeDef]]


# UpdateManagedLoginBrandingResponseTypeDef

### ManagedLoginBranding
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ManagedLoginBrandingTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateResourceServerRequestTypeDef

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


# UpdateUserAttributesRequestTypeDef

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


# UpdateUserPoolClientRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ADMIN_NO_SRP_AUTH', 'ALLOW_ADMIN_USER_PASSWORD_AUTH', 'ALLOW_CUSTOM_AUTH', 'ALLOW_REFRESH_TOKEN_AUTH', 'ALLOW_USER_AUTH', 'ALLOW_USER_PASSWORD_AUTH', 'ALLOW_USER_SRP_AUTH', 'CUSTOM_AUTH_FLOW_ONLY', 'USER_PASSWORD_AUTH']]]

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


# UpdateUserPoolDomainRequestTypeDef

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedLoginVersion
- **Type**: typing.Optional[int]

### CustomDomainConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CustomDomainConfigTypeTypeDef]


# UpdateUserPoolDomainResponseTypeDef

### ManagedLoginVersion
- **Type**: <class 'int'>
- **Required**: Yes

### CloudFrontDomain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserPoolRequestTypeDef

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolPolicyTypeUnionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserAttributeUpdateSettingsTypeUnionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountRecoverySettingTypeUnionTypeDef]

### PoolName
- **Type**: typing.Optional[str]

### UserPoolTier
- **Type**: typing.Optional[typing.Literal['ESSENTIALS', 'LITE', 'PLUS']]


# UserAttributeUpdateSettingsTypeOutputTypeDef

### AttributesRequireVerificationBeforeUpdate
- **Type**: typing.Optional[typing.List[typing.Literal['email', 'phone_number']]]


# UserAttributeUpdateSettingsTypeTypeDef

### AttributesRequireVerificationBeforeUpdate
- **Type**: typing.Optional[typing.Sequence[typing.Literal['email', 'phone_number']]]


# UserAttributeUpdateSettingsTypeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### AdvancedSecurityAdditionalFlows
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AdvancedSecurityAdditionalFlowsTypeTypeDef]


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
- **Type**: typing.Optional[typing.List[typing.Literal['ADMIN_NO_SRP_AUTH', 'ALLOW_ADMIN_USER_PASSWORD_AUTH', 'ALLOW_CUSTOM_AUTH', 'ALLOW_REFRESH_TOKEN_AUTH', 'ALLOW_USER_AUTH', 'ALLOW_USER_PASSWORD_AUTH', 'ALLOW_USER_SRP_AUTH', 'CUSTOM_AUTH_FLOW_ONLY', 'USER_PASSWORD_AUTH']]]

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


# UserPoolPolicyTypeOutputTypeDef

### PasswordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PasswordPolicyTypeTypeDef]

### SignInPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SignInPolicyTypeOutputTypeDef]


# UserPoolPolicyTypeTypeDef

### PasswordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PasswordPolicyTypeTypeDef]

### SignInPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SignInPolicyTypeTypeDef]


# UserPoolPolicyTypeUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UserPoolTypeTypeDef

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolPolicyTypeOutputTypeDef]

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

### UserPoolTier
- **Type**: typing.Optional[typing.Literal['ESSENTIALS', 'LITE', 'PLUS']]


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


# VerifySoftwareTokenRequestTypeDef

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


# VerifyUserAttributeRequestTypeDef

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: <class 'str'>
- **Required**: Yes


# WebAuthnConfigurationTypeTypeDef

### RelyingPartyId
- **Type**: typing.Optional[str]

### UserVerification
- **Type**: typing.Optional[typing.Literal['preferred', 'required']]


# WebAuthnCredentialDescriptionTypeDef

### CredentialId
- **Type**: <class 'str'>
- **Required**: Yes

### FriendlyCredentialName
- **Type**: <class 'str'>
- **Required**: Yes

### RelyingPartyId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticatorTransports
- **Type**: typing.List[str]
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AuthenticatorAttachment
- **Type**: typing.Optional[str]


