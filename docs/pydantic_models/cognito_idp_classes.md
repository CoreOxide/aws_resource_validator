# Cognito Idp Classes

# AccountRecoverySettingType

### RecoveryMechanisms
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.RecoveryOptionType]]


# AccountRecoverySettingTypeOutput

### RecoveryMechanisms
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.RecoveryOptionType]]


# AccountRecoverySettingTypeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccountTakeoverActionType

### Notify
- **Type**: <class 'bool'>
- **Required**: Yes

### EventAction
- **Type**: typing.Literal['BLOCK', 'MFA_IF_CONFIGURED', 'MFA_REQUIRED', 'NO_ACTION']
- **Required**: Yes


# AccountTakeoverActionsType

### LowAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountTakeoverActionType]

### MediumAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountTakeoverActionType]

### HighAction
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountTakeoverActionType]


# AccountTakeoverRiskConfigurationType

### Actions
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.AccountTakeoverActionsType'>
- **Required**: Yes

### NotifyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.NotifyConfigurationType]


# AddCustomAttributesRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### CustomAttributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.SchemaAttributeType]
- **Required**: Yes


# AdminAddUserToGroupRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# AdminConfirmSignUpRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AdminCreateUserConfigType

### AllowAdminCreateUserOnly
- **Type**: typing.Optional[bool]

### UnusedAccountValidityDays
- **Type**: typing.Optional[int]

### InviteMessageTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.MessageTemplateType]


# AdminCreateUserRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeType]]

### ValidationData
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeType]]

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


# AdminCreateUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# AdminDeleteUserAttributesRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserAttributeNames
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AdminDeleteUserRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdminDisableProviderForUserRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ProviderUserIdentifierType'>
- **Required**: Yes


# AdminDisableUserRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdminEnableUserRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdminForgetDeviceRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes


# AdminGetDeviceRequest

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdminGetDeviceResponse

### Device
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# AdminGetUserRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdminGetUserResponse

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeType]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.MFAOptionType]
- **Required**: Yes

### PreferredMfaSetting
- **Type**: <class 'str'>
- **Required**: Yes

### UserMFASettingList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# AdminInitiateAuthRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataType]

### ContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.ContextDataType]

### Session
- **Type**: typing.Optional[str]


# AdminInitiateAuthResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.AuthenticationResultType'>
- **Required**: Yes

### AvailableChallenges
- **Type**: typing.List[typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'EMAIL_OTP', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD', 'PASSWORD_SRP', 'PASSWORD_VERIFIER', 'SELECT_CHALLENGE', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SMS_OTP', 'SOFTWARE_TOKEN_MFA', 'WEB_AUTHN']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# AdminLinkProviderForUserRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationUser
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ProviderUserIdentifierType'>
- **Required**: Yes

### SourceUser
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ProviderUserIdentifierType'>
- **Required**: Yes


# AdminListDevicesRequest

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


# AdminListDevicesResponse

### Devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceType]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# AdminListGroupsForUserRequest

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


# AdminListGroupsForUserRequestPaginate

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfig]


# AdminListGroupsForUserResponse

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.GroupType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# AdminListUserAuthEventsRequest

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


# AdminListUserAuthEventsRequestPaginate

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfig]


# AdminListUserAuthEventsResponse

### AuthEvents
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.AuthEventType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# AdminRemoveUserFromGroupRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# AdminResetUserPasswordRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AdminRespondToAuthChallengeRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataType]

### ContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.ContextDataType]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AdminRespondToAuthChallengeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.AuthenticationResultType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# AdminSetUserMFAPreferenceRequest

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### SMSMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SMSMfaSettingsType]

### SoftwareTokenMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SoftwareTokenMfaSettingsType]

### EmailMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EmailMfaSettingsType]


# AdminSetUserPasswordRequest

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


# AdminSetUserSettingsRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### MFAOptions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.MFAOptionType]
- **Required**: Yes


# AdminUpdateAuthEventFeedbackRequest

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


# AdminUpdateDeviceStatusRequest

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


# AdminUpdateUserAttributesRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserAttributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeType]
- **Required**: Yes

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# AdminUserGlobalSignOutRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes


# AdvancedSecurityAdditionalFlowsType

### CustomAuthMode
- **Type**: typing.Optional[typing.Literal['AUDIT', 'ENFORCED']]


# AnalyticsConfigurationType

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


# AnalyticsMetadataType

### AnalyticsEndpointId
- **Type**: typing.Optional[str]


# AssetType

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.Blob]

### ResourceId
- **Type**: typing.Optional[str]


# AssetTypeOutput

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


# AssetTypeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AssociateSoftwareTokenRequest

### AccessToken
- **Type**: typing.Optional[str]

### Session
- **Type**: typing.Optional[str]


# AssociateSoftwareTokenResponse

### SecretCode
- **Type**: <class 'str'>
- **Required**: Yes

### Session
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# AttributeType

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# AuthEventType

### EventId
- **Type**: typing.Optional[str]

### EventType
- **Type**: typing.Optional[typing.Literal['ForgotPassword', 'PasswordChange', 'ResendCode', 'SignIn', 'SignUp']]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### EventResponse
- **Type**: typing.Optional[typing.Literal['Fail', 'InProgress', 'Pass']]

### EventRisk
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EventRiskType]

### ChallengeResponses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.ChallengeResponseType]]

### EventContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EventContextDataType]

### EventFeedback
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EventFeedbackType]


# AuthenticationResultType

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.NewDeviceMetadataType]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChallengeResponseType

### ChallengeName
- **Type**: typing.Optional[typing.Literal['Mfa', 'Password']]

### ChallengeResponse
- **Type**: typing.Optional[typing.Literal['Failure', 'Success']]


# ChangePasswordRequest

### ProposedPassword
- **Type**: <class 'str'>
- **Required**: Yes

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### PreviousPassword
- **Type**: typing.Optional[str]


# CloudWatchLogsConfigurationType

### LogGroupArn
- **Type**: typing.Optional[str]


# CodeDeliveryDetailsType

### Destination
- **Type**: typing.Optional[str]

### DeliveryMedium
- **Type**: typing.Optional[typing.Literal['EMAIL', 'SMS']]

### AttributeName
- **Type**: typing.Optional[str]


# CompleteWebAuthnRegistrationRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### Credential
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# CompromisedCredentialsActionsType

### EventAction
- **Type**: typing.Literal['BLOCK', 'NO_ACTION']
- **Required**: Yes


# CompromisedCredentialsRiskConfigurationType

### Actions
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.CompromisedCredentialsActionsType'>
- **Required**: Yes

### EventFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PASSWORD_CHANGE', 'SIGN_IN', 'SIGN_UP']]]


# CompromisedCredentialsRiskConfigurationTypeOutput

### Actions
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.CompromisedCredentialsActionsType'>
- **Required**: Yes

### EventFilter
- **Type**: typing.Optional[typing.List[typing.Literal['PASSWORD_CHANGE', 'SIGN_IN', 'SIGN_UP']]]


# CompromisedCredentialsRiskConfigurationTypeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConfirmDeviceRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceSecretVerifierConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceSecretVerifierConfigType]

### DeviceName
- **Type**: typing.Optional[str]


# ConfirmDeviceResponse

### UserConfirmationNecessary
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# ConfirmForgotPasswordRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataType]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataType]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ConfirmSignUpRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataType]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataType]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Session
- **Type**: typing.Optional[str]


# ConfirmSignUpResponse

### Session
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# ContextDataType

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
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.HttpHeader]
- **Required**: Yes

### EncodedData
- **Type**: typing.Optional[str]


# CreateGroupRequest

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


# CreateGroupResponse

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.GroupType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIdentityProviderRequest

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


# CreateIdentityProviderResponse

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.IdentityProviderType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# CreateManagedLoginBrandingRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AssetTypeUnion]]


# CreateManagedLoginBrandingResponse

### ManagedLoginBranding
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ManagedLoginBrandingType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourceServerRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerScopeType]]


# CreateResourceServerResponse

### ResourceServer
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserImportJobRequest

### JobName
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLogsRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateUserImportJobResponse

### UserImportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserImportJobType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserPoolClientRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.TokenValidityUnitsType]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsConfigurationType]

### PreventUserExistenceErrors
- **Type**: typing.Optional[typing.Literal['ENABLED', 'LEGACY']]

### EnableTokenRevocation
- **Type**: typing.Optional[bool]

### EnablePropagateAdditionalUserContextData
- **Type**: typing.Optional[bool]

### AuthSessionValidity
- **Type**: typing.Optional[int]


# CreateUserPoolClientResponse

### UserPoolClient
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolClientType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserPoolDomainRequest

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedLoginVersion
- **Type**: typing.Optional[int]

### CustomDomainConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CustomDomainConfigType]


# CreateUserPoolDomainResponse

### ManagedLoginVersion
- **Type**: <class 'int'>
- **Required**: Yes

### CloudFrontDomain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserPoolRequest

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolPolicyTypeUnion]

### DeletionProtection
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### LambdaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.LambdaConfigType]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.VerificationMessageTemplateType]

### SmsAuthenticationMessage
- **Type**: typing.Optional[str]

### MfaConfiguration
- **Type**: typing.Optional[typing.Literal['OFF', 'ON', 'OPTIONAL']]

### UserAttributeUpdateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserAttributeUpdateSettingsTypeUnion]

### DeviceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceConfigurationType]

### EmailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EmailConfigurationType]

### SmsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SmsConfigurationType]

### UserPoolTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AdminCreateUserConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AdminCreateUserConfigType]

### Schema
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.SchemaAttributeType]]

### UserPoolAddOns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolAddOnsType]

### UsernameConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UsernameConfigurationType]

### AccountRecoverySetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountRecoverySettingTypeUnion]

### UserPoolTier
- **Type**: typing.Optional[typing.Literal['ESSENTIALS', 'LITE', 'PLUS']]


# CreateUserPoolResponse

### UserPool
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# CustomDomainConfigType

### CertificateArn
- **Type**: <class 'str'>
- **Required**: Yes


# CustomEmailLambdaVersionConfigType

### LambdaVersion
- **Type**: typing.Literal['V1_0']
- **Required**: Yes

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# CustomSMSLambdaVersionConfigType

### LambdaVersion
- **Type**: typing.Literal['V1_0']
- **Required**: Yes

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityProviderRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteManagedLoginBrandingRequest

### ManagedLoginBrandingId
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceServerRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserAttributesRequest

### UserAttributeNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserPoolClientRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserPoolDomainRequest

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserPoolRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWebAuthnCredentialRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### CredentialId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityProviderRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ProviderName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityProviderResponse

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.IdentityProviderType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeManagedLoginBrandingByClientRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ReturnMergedResources
- **Type**: typing.Optional[bool]


# DescribeManagedLoginBrandingByClientResponse

### ManagedLoginBranding
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ManagedLoginBrandingType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeManagedLoginBrandingRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedLoginBrandingId
- **Type**: <class 'str'>
- **Required**: Yes

### ReturnMergedResources
- **Type**: typing.Optional[bool]


# DescribeManagedLoginBrandingResponse

### ManagedLoginBranding
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ManagedLoginBrandingType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeResourceServerRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourceServerResponse

### ResourceServer
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeRiskConfigurationRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: typing.Optional[str]


# DescribeRiskConfigurationResponse

### RiskConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.RiskConfigurationType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserImportJobRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserImportJobResponse

### UserImportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserImportJobType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserPoolClientRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserPoolClientResponse

### UserPoolClient
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolClientType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserPoolDomainRequest

### Domain
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserPoolDomainResponse

### DomainDescription
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.DomainDescriptionType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserPoolRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserPoolResponse

### UserPool
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# DeviceConfigurationType

### ChallengeRequiredOnNewDevice
- **Type**: typing.Optional[bool]

### DeviceOnlyRememberedOnUserPrompt
- **Type**: typing.Optional[bool]


# DeviceSecretVerifierConfigType

### PasswordVerifier
- **Type**: typing.Optional[str]

### Salt
- **Type**: typing.Optional[str]


# DeviceType

### DeviceKey
- **Type**: typing.Optional[str]

### DeviceAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeType]]

### DeviceCreateDate
- **Type**: typing.Optional[datetime.datetime]

### DeviceLastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### DeviceLastAuthenticatedDate
- **Type**: typing.Optional[datetime.datetime]


# DomainDescriptionType

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CustomDomainConfigType]

### ManagedLoginVersion
- **Type**: typing.Optional[int]


# EmailConfigurationType

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


# EmailMfaConfigType

### Message
- **Type**: typing.Optional[str]

### Subject
- **Type**: typing.Optional[str]


# EmailMfaSettingsType

### Enabled
- **Type**: typing.Optional[bool]

### PreferredMfa
- **Type**: typing.Optional[bool]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# EventContextDataType

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


# EventFeedbackType

### FeedbackValue
- **Type**: typing.Literal['Invalid', 'Valid']
- **Required**: Yes

### Provider
- **Type**: <class 'str'>
- **Required**: Yes

### FeedbackDate
- **Type**: typing.Optional[datetime.datetime]


# EventRiskType

### RiskDecision
- **Type**: typing.Optional[typing.Literal['AccountTakeover', 'Block', 'NoRisk']]

### RiskLevel
- **Type**: typing.Optional[typing.Literal['High', 'Low', 'Medium']]

### CompromisedCredentialsDetected
- **Type**: typing.Optional[bool]


# FirehoseConfigurationType

### StreamArn
- **Type**: typing.Optional[str]


# ForgetDeviceRequest

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes

### AccessToken
- **Type**: typing.Optional[str]


# ForgotPasswordRequest

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### SecretHash
- **Type**: typing.Optional[str]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataType]

### AnalyticsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataType]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ForgotPasswordResponse

### CodeDeliveryDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.CodeDeliveryDetailsType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# GetCSVHeaderRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetCSVHeaderResponse

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### CSVHeader
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# GetDeviceRequest

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes

### AccessToken
- **Type**: typing.Optional[str]


# GetDeviceResponse

### Device
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# GetGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupResponse

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.GroupType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdentityProviderByIdentifierRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### IdpIdentifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentityProviderByIdentifierResponse

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.IdentityProviderType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# GetLogDeliveryConfigurationRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetLogDeliveryConfigurationResponse

### LogDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.LogDeliveryConfigurationType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# GetSigningCertificateRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSigningCertificateResponse

### Certificate
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# GetUICustomizationRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: typing.Optional[str]


# GetUICustomizationResponse

### UICustomization
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UICustomizationType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserAttributeVerificationCodeRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# GetUserAttributeVerificationCodeResponse

### CodeDeliveryDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.CodeDeliveryDetailsType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserAuthFactorsRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserAuthFactorsResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserPoolMfaConfigRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserPoolMfaConfigResponse

### SmsMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.SmsMfaConfigType'>
- **Required**: Yes

### SoftwareTokenMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.SoftwareTokenMfaConfigType'>
- **Required**: Yes

### EmailMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.EmailMfaConfigType'>
- **Required**: Yes

### MfaConfiguration
- **Type**: typing.Literal['OFF', 'ON', 'OPTIONAL']
- **Required**: Yes

### WebAuthnConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.WebAuthnConfigurationType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserResponse

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### UserAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeType]
- **Required**: Yes

### MFAOptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.MFAOptionType]
- **Required**: Yes

### PreferredMfaSetting
- **Type**: <class 'str'>
- **Required**: Yes

### UserMFASettingList
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# GlobalSignOutRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# GroupType

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


# HttpHeader

### headerName
- **Type**: typing.Optional[str]

### headerValue
- **Type**: typing.Optional[str]


# IdentityProviderType

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


# InitiateAuthRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataType]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataType]

### Session
- **Type**: typing.Optional[str]


# InitiateAuthResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.AuthenticationResultType'>
- **Required**: Yes

### AvailableChallenges
- **Type**: typing.List[typing.Literal['ADMIN_NO_SRP_AUTH', 'CUSTOM_CHALLENGE', 'DEVICE_PASSWORD_VERIFIER', 'DEVICE_SRP_AUTH', 'EMAIL_OTP', 'MFA_SETUP', 'NEW_PASSWORD_REQUIRED', 'PASSWORD', 'PASSWORD_SRP', 'PASSWORD_VERIFIER', 'SELECT_CHALLENGE', 'SELECT_MFA_TYPE', 'SMS_MFA', 'SMS_OTP', 'SOFTWARE_TOKEN_MFA', 'WEB_AUTHN']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# LambdaConfigType

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PreTokenGenerationVersionConfigType]

### CustomSMSSender
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CustomSMSLambdaVersionConfigType]

### CustomEmailSender
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CustomEmailLambdaVersionConfigType]

### KMSKeyID
- **Type**: typing.Optional[str]


# ListDevicesRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### PaginationToken
- **Type**: typing.Optional[str]


# ListDevicesResponse

### Devices
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceType]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# ListGroupsRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Limit
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsRequestPaginate

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfig]


# ListGroupsResponse

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.GroupType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityProvidersRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListIdentityProvidersRequestPaginate

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfig]


# ListIdentityProvidersResponse

### Providers
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.ProviderDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceServersRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListResourceServersRequestPaginate

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfig]


# ListResourceServersResponse

### ResourceServers
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# ListUserImportJobsRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### PaginationToken
- **Type**: typing.Optional[str]


# ListUserImportJobsResponse

### UserImportJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.UserImportJobType]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# ListUserPoolClientsRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListUserPoolClientsRequestPaginate

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfig]


# ListUserPoolClientsResponse

### UserPoolClients
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolClientDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUserPoolsRequest

### MaxResults
- **Type**: <class 'int'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUserPoolsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfig]


# ListUserPoolsResponse

### UserPools
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolDescriptionType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsersInGroupRequest

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


# ListUsersInGroupRequestPaginate

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfig]


# ListUsersInGroupResponse

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.UserType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListUsersRequest

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


# ListUsersRequestPaginate

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### AttributesToGet
- **Type**: typing.Optional[typing.Sequence[str]]

### Filter
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PaginatorConfig]


# ListUsersResponse

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.UserType]
- **Required**: Yes

### PaginationToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# ListWebAuthnCredentialsRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListWebAuthnCredentialsResponse

### Credentials
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.WebAuthnCredentialDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LogConfigurationType

### LogLevel
- **Type**: typing.Literal['ERROR', 'INFO']
- **Required**: Yes

### EventSource
- **Type**: typing.Literal['userAuthEvents', 'userNotification']
- **Required**: Yes

### CloudWatchLogsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CloudWatchLogsConfigurationType]

### S3Configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.S3ConfigurationType]

### FirehoseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.FirehoseConfigurationType]


# LogDeliveryConfigurationType

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### LogConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.LogConfigurationType]
- **Required**: Yes


# MFAOptionType

### DeliveryMedium
- **Type**: typing.Optional[typing.Literal['EMAIL', 'SMS']]

### AttributeName
- **Type**: typing.Optional[str]


# ManagedLoginBrandingType

### ManagedLoginBrandingId
- **Type**: typing.Optional[str]

### UserPoolId
- **Type**: typing.Optional[str]

### UseCognitoProvidedValues
- **Type**: typing.Optional[bool]

### Settings
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### Assets
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.AssetTypeOutput]]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# MessageTemplateType

### SMSMessage
- **Type**: typing.Optional[str]

### EmailMessage
- **Type**: typing.Optional[str]

### EmailSubject
- **Type**: typing.Optional[str]


# NewDeviceMetadataType

### DeviceKey
- **Type**: typing.Optional[str]

### DeviceGroupKey
- **Type**: typing.Optional[str]


# NotifyConfigurationType

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### From
- **Type**: typing.Optional[str]

### ReplyTo
- **Type**: typing.Optional[str]

### BlockEmail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.NotifyEmailType]

### NoActionEmail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.NotifyEmailType]

### MfaEmail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.NotifyEmailType]


# NotifyEmailType

### Subject
- **Type**: <class 'str'>
- **Required**: Yes

### HtmlBody
- **Type**: typing.Optional[str]

### TextBody
- **Type**: typing.Optional[str]


# NumberAttributeConstraintsType

### MinValue
- **Type**: typing.Optional[str]

### MaxValue
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PasswordPolicyType

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


# PreTokenGenerationVersionConfigType

### LambdaVersion
- **Type**: typing.Literal['V1_0', 'V2_0', 'V3_0']
- **Required**: Yes

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# ProviderDescription

### ProviderName
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['Facebook', 'Google', 'LoginWithAmazon', 'OIDC', 'SAML', 'SignInWithApple']]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]


# ProviderUserIdentifierType

### ProviderName
- **Type**: typing.Optional[str]

### ProviderAttributeName
- **Type**: typing.Optional[str]

### ProviderAttributeValue
- **Type**: typing.Optional[str]


# RecoveryOptionType

### Priority
- **Type**: <class 'int'>
- **Required**: Yes

### Name
- **Type**: typing.Literal['admin_only', 'verified_email', 'verified_phone_number']
- **Required**: Yes


# ResendConfirmationCodeRequest

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### SecretHash
- **Type**: typing.Optional[str]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataType]

### AnalyticsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataType]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ResendConfirmationCodeResponse

### CodeDeliveryDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.CodeDeliveryDetailsType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# ResourceServerScopeType

### ScopeName
- **Type**: <class 'str'>
- **Required**: Yes

### ScopeDescription
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceServerType

### UserPoolId
- **Type**: typing.Optional[str]

### Identifier
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Scopes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerScopeType]]


# RespondToAuthChallengeRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataType]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataType]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# RespondToAuthChallengeResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.AuthenticationResultType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
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


# RevokeTokenRequest

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientSecret
- **Type**: typing.Optional[str]


# RiskConfigurationType

### UserPoolId
- **Type**: typing.Optional[str]

### ClientId
- **Type**: typing.Optional[str]

### CompromisedCredentialsRiskConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CompromisedCredentialsRiskConfigurationTypeOutput]

### AccountTakeoverRiskConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountTakeoverRiskConfigurationType]

### RiskExceptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.RiskExceptionConfigurationTypeOutput]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]


# RiskExceptionConfigurationType

### BlockedIPRangeList
- **Type**: typing.Optional[typing.Sequence[str]]

### SkippedIPRangeList
- **Type**: typing.Optional[typing.Sequence[str]]


# RiskExceptionConfigurationTypeOutput

### BlockedIPRangeList
- **Type**: typing.Optional[typing.List[str]]

### SkippedIPRangeList
- **Type**: typing.Optional[typing.List[str]]


# RiskExceptionConfigurationTypeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3ConfigurationType

### BucketArn
- **Type**: typing.Optional[str]


# SMSMfaSettingsType

### Enabled
- **Type**: typing.Optional[bool]

### PreferredMfa
- **Type**: typing.Optional[bool]


# SchemaAttributeType

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SetLogDeliveryConfigurationRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### LogConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.LogConfigurationType]
- **Required**: Yes


# SetLogDeliveryConfigurationResponse

### LogDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.LogDeliveryConfigurationType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# SetRiskConfigurationRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: typing.Optional[str]

### CompromisedCredentialsRiskConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CompromisedCredentialsRiskConfigurationTypeUnion]

### AccountTakeoverRiskConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountTakeoverRiskConfigurationType]

### RiskExceptionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.RiskExceptionConfigurationTypeUnion]


# SetRiskConfigurationResponse

### RiskConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.RiskConfigurationType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# SetUICustomizationRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientId
- **Type**: typing.Optional[str]

### CSS
- **Type**: typing.Optional[str]

### ImageFile
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.Blob]


# SetUICustomizationResponse

### UICustomization
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UICustomizationType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# SetUserMFAPreferenceRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### SMSMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SMSMfaSettingsType]

### SoftwareTokenMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SoftwareTokenMfaSettingsType]

### EmailMfaSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EmailMfaSettingsType]


# SetUserPoolMfaConfigRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### SmsMfaConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SmsMfaConfigType]

### SoftwareTokenMfaConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SoftwareTokenMfaConfigType]

### EmailMfaConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EmailMfaConfigType]

### MfaConfiguration
- **Type**: typing.Optional[typing.Literal['OFF', 'ON', 'OPTIONAL']]

### WebAuthnConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.WebAuthnConfigurationType]


# SetUserPoolMfaConfigResponse

### SmsMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.SmsMfaConfigType'>
- **Required**: Yes

### SoftwareTokenMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.SoftwareTokenMfaConfigType'>
- **Required**: Yes

### EmailMfaConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.EmailMfaConfigType'>
- **Required**: Yes

### MfaConfiguration
- **Type**: typing.Literal['OFF', 'ON', 'OPTIONAL']
- **Required**: Yes

### WebAuthnConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.WebAuthnConfigurationType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# SetUserSettingsRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### MFAOptions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.MFAOptionType]
- **Required**: Yes


# SignInPolicyType

### AllowedFirstAuthFactors
- **Type**: typing.Optional[typing.Sequence[typing.Literal['EMAIL_OTP', 'PASSWORD', 'SMS_OTP', 'WEB_AUTHN']]]


# SignInPolicyTypeOutput

### AllowedFirstAuthFactors
- **Type**: typing.Optional[typing.List[typing.Literal['EMAIL_OTP', 'PASSWORD', 'SMS_OTP', 'WEB_AUTHN']]]


# SignUpRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeType]]

### ValidationData
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeType]]

### AnalyticsMetadata
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsMetadataType]

### UserContextData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserContextDataType]

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# SignUpResponse

### UserConfirmed
- **Type**: <class 'bool'>
- **Required**: Yes

### CodeDeliveryDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.CodeDeliveryDetailsType'>
- **Required**: Yes

### UserSub
- **Type**: <class 'str'>
- **Required**: Yes

### Session
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# SmsConfigurationType

### SnsCallerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ExternalId
- **Type**: typing.Optional[str]

### SnsRegion
- **Type**: typing.Optional[str]


# SmsMfaConfigType

### SmsAuthenticationMessage
- **Type**: typing.Optional[str]

### SmsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SmsConfigurationType]


# SoftwareTokenMfaConfigType

### Enabled
- **Type**: typing.Optional[bool]


# SoftwareTokenMfaSettingsType

### Enabled
- **Type**: typing.Optional[bool]

### PreferredMfa
- **Type**: typing.Optional[bool]


# StartUserImportJobRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StartUserImportJobResponse

### UserImportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserImportJobType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# StartWebAuthnRegistrationRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes


# StartWebAuthnRegistrationResponse

### CredentialCreationOptions
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# StopUserImportJobRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes


# StopUserImportJobResponse

### UserImportJob
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserImportJobType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# StringAttributeConstraintsType

### MinLength
- **Type**: typing.Optional[str]

### MaxLength
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TokenValidityUnitsType

### AccessToken
- **Type**: typing.Optional[typing.Literal['days', 'hours', 'minutes', 'seconds']]

### IdToken
- **Type**: typing.Optional[typing.Literal['days', 'hours', 'minutes', 'seconds']]

### RefreshToken
- **Type**: typing.Optional[typing.Literal['days', 'hours', 'minutes', 'seconds']]


# UICustomizationType

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


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAuthEventFeedbackRequest

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


# UpdateDeviceStatusRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceKey
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceRememberedStatus
- **Type**: typing.Optional[typing.Literal['not_remembered', 'remembered']]


# UpdateGroupRequest

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


# UpdateGroupResponse

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.GroupType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIdentityProviderRequest

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


# UpdateIdentityProviderResponse

### IdentityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.IdentityProviderType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateManagedLoginBrandingRequest

### UserPoolId
- **Type**: typing.Optional[str]

### ManagedLoginBrandingId
- **Type**: typing.Optional[str]

### UseCognitoProvidedValues
- **Type**: typing.Optional[bool]

### Settings
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### Assets
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AssetTypeUnion]]


# UpdateManagedLoginBrandingResponse

### ManagedLoginBranding
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ManagedLoginBrandingType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateResourceServerRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerScopeType]]


# UpdateResourceServerResponse

### ResourceServer
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResourceServerType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserAttributesRequest

### UserAttributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeType]
- **Required**: Yes

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### ClientMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# UpdateUserAttributesResponse

### CodeDeliveryDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.CodeDeliveryDetailsType]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserPoolClientRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.TokenValidityUnitsType]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsConfigurationType]

### PreventUserExistenceErrors
- **Type**: typing.Optional[typing.Literal['ENABLED', 'LEGACY']]

### EnableTokenRevocation
- **Type**: typing.Optional[bool]

### EnablePropagateAdditionalUserContextData
- **Type**: typing.Optional[bool]

### AuthSessionValidity
- **Type**: typing.Optional[int]


# UpdateUserPoolClientResponse

### UserPoolClient
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolClientType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserPoolDomainRequest

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedLoginVersion
- **Type**: typing.Optional[int]

### CustomDomainConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.CustomDomainConfigType]


# UpdateUserPoolDomainResponse

### ManagedLoginVersion
- **Type**: <class 'int'>
- **Required**: Yes

### CloudFrontDomain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserPoolRequest

### UserPoolId
- **Type**: <class 'str'>
- **Required**: Yes

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolPolicyTypeUnion]

### DeletionProtection
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### LambdaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.LambdaConfigType]

### AutoVerifiedAttributes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['email', 'phone_number']]]

### SmsVerificationMessage
- **Type**: typing.Optional[str]

### EmailVerificationMessage
- **Type**: typing.Optional[str]

### EmailVerificationSubject
- **Type**: typing.Optional[str]

### VerificationMessageTemplate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.VerificationMessageTemplateType]

### SmsAuthenticationMessage
- **Type**: typing.Optional[str]

### UserAttributeUpdateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserAttributeUpdateSettingsTypeUnion]

### MfaConfiguration
- **Type**: typing.Optional[typing.Literal['OFF', 'ON', 'OPTIONAL']]

### DeviceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceConfigurationType]

### EmailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EmailConfigurationType]

### SmsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SmsConfigurationType]

### UserPoolTags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### AdminCreateUserConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AdminCreateUserConfigType]

### UserPoolAddOns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolAddOnsType]

### AccountRecoverySetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountRecoverySettingTypeUnion]

### PoolName
- **Type**: typing.Optional[str]

### UserPoolTier
- **Type**: typing.Optional[typing.Literal['ESSENTIALS', 'LITE', 'PLUS']]


# UserAttributeUpdateSettingsType

### AttributesRequireVerificationBeforeUpdate
- **Type**: typing.Optional[typing.Sequence[typing.Literal['email', 'phone_number']]]


# UserAttributeUpdateSettingsTypeOutput

### AttributesRequireVerificationBeforeUpdate
- **Type**: typing.Optional[typing.List[typing.Literal['email', 'phone_number']]]


# UserAttributeUpdateSettingsTypeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UserContextDataType

### IpAddress
- **Type**: typing.Optional[str]

### EncodedData
- **Type**: typing.Optional[str]


# UserImportJobType

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


# UserPoolAddOnsType

### AdvancedSecurityMode
- **Type**: typing.Literal['AUDIT', 'ENFORCED', 'OFF']
- **Required**: Yes

### AdvancedSecurityAdditionalFlows
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AdvancedSecurityAdditionalFlowsType]


# UserPoolClientDescription

### ClientId
- **Type**: typing.Optional[str]

### UserPoolId
- **Type**: typing.Optional[str]

### ClientName
- **Type**: typing.Optional[str]


# UserPoolClientType

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.TokenValidityUnitsType]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AnalyticsConfigurationType]

### PreventUserExistenceErrors
- **Type**: typing.Optional[typing.Literal['ENABLED', 'LEGACY']]

### EnableTokenRevocation
- **Type**: typing.Optional[bool]

### EnablePropagateAdditionalUserContextData
- **Type**: typing.Optional[bool]

### AuthSessionValidity
- **Type**: typing.Optional[int]


# UserPoolDescriptionType

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### LambdaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.LambdaConfigType]

### Status
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]


# UserPoolPolicyType

### PasswordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PasswordPolicyType]

### SignInPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SignInPolicyType]


# UserPoolPolicyTypeOutput

### PasswordPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.PasswordPolicyType]

### SignInPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SignInPolicyTypeOutput]


# UserPoolPolicyTypeUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UserPoolType

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Policies
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolPolicyTypeOutput]

### DeletionProtection
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### LambdaConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.LambdaConfigType]

### Status
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### LastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### CreationDate
- **Type**: typing.Optional[datetime.datetime]

### SchemaAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.SchemaAttributeType]]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.VerificationMessageTemplateType]

### SmsAuthenticationMessage
- **Type**: typing.Optional[str]

### UserAttributeUpdateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserAttributeUpdateSettingsTypeOutput]

### MfaConfiguration
- **Type**: typing.Optional[typing.Literal['OFF', 'ON', 'OPTIONAL']]

### DeviceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.DeviceConfigurationType]

### EstimatedNumberOfUsers
- **Type**: typing.Optional[int]

### EmailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.EmailConfigurationType]

### SmsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.SmsConfigurationType]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AdminCreateUserConfigType]

### UserPoolAddOns
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UserPoolAddOnsType]

### UsernameConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.UsernameConfigurationType]

### Arn
- **Type**: typing.Optional[str]

### AccountRecoverySetting
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.cognito_idp_classes.AccountRecoverySettingTypeOutput]

### UserPoolTier
- **Type**: typing.Optional[typing.Literal['ESSENTIALS', 'LITE', 'PLUS']]


# UserType

### Username
- **Type**: typing.Optional[str]

### Attributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.AttributeType]]

### UserCreateDate
- **Type**: typing.Optional[datetime.datetime]

### UserLastModifiedDate
- **Type**: typing.Optional[datetime.datetime]

### Enabled
- **Type**: typing.Optional[bool]

### UserStatus
- **Type**: typing.Optional[typing.Literal['ARCHIVED', 'COMPROMISED', 'CONFIRMED', 'EXTERNAL_PROVIDER', 'FORCE_CHANGE_PASSWORD', 'RESET_REQUIRED', 'UNCONFIRMED', 'UNKNOWN']]

### MFAOptions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.cognito_idp_classes.MFAOptionType]]


# UsernameConfigurationType

### CaseSensitive
- **Type**: <class 'bool'>
- **Required**: Yes


# VerificationMessageTemplateType

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


# VerifySoftwareTokenRequest

### UserCode
- **Type**: <class 'str'>
- **Required**: Yes

### AccessToken
- **Type**: typing.Optional[str]

### Session
- **Type**: typing.Optional[str]

### FriendlyDeviceName
- **Type**: typing.Optional[str]


# VerifySoftwareTokenResponse

### Status
- **Type**: typing.Literal['ERROR', 'SUCCESS']
- **Required**: Yes

### Session
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.cognito_idp_classes.ResponseMetadata'>
- **Required**: Yes


# VerifyUserAttributeRequest

### AccessToken
- **Type**: <class 'str'>
- **Required**: Yes

### AttributeName
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: <class 'str'>
- **Required**: Yes


# WebAuthnConfigurationType

### RelyingPartyId
- **Type**: typing.Optional[str]

### UserVerification
- **Type**: typing.Optional[typing.Literal['preferred', 'required']]


# WebAuthnCredentialDescription

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


