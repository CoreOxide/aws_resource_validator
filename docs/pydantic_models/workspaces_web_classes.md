# Workspaces Web Classes

# AssociateBrowserSettingsRequest

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateBrowserSettingsResponse

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateDataProtectionSettingsRequest

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateDataProtectionSettingsResponse

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateIpAccessSettingsRequest

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateIpAccessSettingsResponse

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateNetworkSettingsRequest

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateNetworkSettingsResponse

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateTrustStoreRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateTrustStoreResponse

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateUserAccessLoggingSettingsRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateUserAccessLoggingSettingsResponse

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateUserSettingsRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateUserSettingsResponse

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BrowserSettings

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### associatedPortalArns
- **Type**: typing.Optional[typing.List[str]]

### browserPolicy
- **Type**: typing.Optional[str]

### customerManagedKey
- **Type**: typing.Optional[str]


# BrowserSettingsSummary

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# Certificate

### body
- **Type**: typing.Optional[bytes]

### issuer
- **Type**: typing.Optional[str]

### notValidAfter
- **Type**: typing.Optional[datetime.datetime]

### notValidBefore
- **Type**: typing.Optional[datetime.datetime]

### subject
- **Type**: typing.Optional[str]

### thumbprint
- **Type**: typing.Optional[str]


# CertificateSummary

### issuer
- **Type**: typing.Optional[str]

### notValidAfter
- **Type**: typing.Optional[datetime.datetime]

### notValidBefore
- **Type**: typing.Optional[datetime.datetime]

### subject
- **Type**: typing.Optional[str]

### thumbprint
- **Type**: typing.Optional[str]


# CookieSpecification

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]


# CookieSynchronizationConfiguration

### allowlist
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.CookieSpecification]
- **Required**: Yes

### blocklist
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.CookieSpecification]]


# CookieSynchronizationConfigurationOutput

### allowlist
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.CookieSpecification]
- **Required**: Yes

### blocklist
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.CookieSpecification]]


# CreateBrowserSettingsRequest

### browserPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### clientToken
- **Type**: typing.Optional[str]

### customerManagedKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Tag]]


# CreateBrowserSettingsResponse

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataProtectionSettingsRequest

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### clientToken
- **Type**: typing.Optional[str]

### customerManagedKey
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### inlineRedactionConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.InlineRedactionConfiguration, aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.InlineRedactionConfigurationOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Tag]]


# CreateDataProtectionSettingsResponse

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIdentityProviderRequest

### identityProviderDetails
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### identityProviderName
- **Type**: <class 'str'>
- **Required**: Yes

### identityProviderType
- **Type**: typing.Literal['Facebook', 'Google', 'LoginWithAmazon', 'OIDC', 'SAML', 'SignInWithApple']
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Tag]]


# CreateIdentityProviderResponse

### identityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIpAccessSettingsRequest

### ipRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.IpRule]
- **Required**: Yes

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### clientToken
- **Type**: typing.Optional[str]

### customerManagedKey
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Tag]]


# CreateIpAccessSettingsResponse

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNetworkSettingsRequest

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Tag]]


# CreateNetworkSettingsResponse

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePortalRequest

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### authenticationType
- **Type**: typing.Optional[typing.Literal['IAM_Identity_Center', 'Standard']]

### clientToken
- **Type**: typing.Optional[str]

### customerManagedKey
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[typing.Literal['standard.large', 'standard.regular', 'standard.xlarge']]

### maxConcurrentSessions
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Tag]]


# CreatePortalResponse

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrustStoreRequest

### certificateList
- **Type**: typing.List[typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Tag]]


# CreateTrustStoreResponse

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserAccessLoggingSettingsRequest

### kinesisStreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Tag]]


# CreateUserAccessLoggingSettingsResponse

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserSettingsRequest

### copyAllowed
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### downloadAllowed
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### pasteAllowed
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### printAllowed
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### uploadAllowed
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### clientToken
- **Type**: typing.Optional[str]

### cookieSynchronizationConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.CookieSynchronizationConfiguration, aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.CookieSynchronizationConfigurationOutput, NoneType]

### customerManagedKey
- **Type**: typing.Optional[str]

### deepLinkAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### disconnectTimeoutInMinutes
- **Type**: typing.Optional[int]

### idleDisconnectTimeoutInMinutes
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Tag]]

### toolbarConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ToolbarConfiguration, aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ToolbarConfigurationOutput, NoneType]


# CreateUserSettingsResponse

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# CustomPattern

### patternName
- **Type**: <class 'str'>
- **Required**: Yes

### patternRegex
- **Type**: <class 'str'>
- **Required**: Yes

### keywordRegex
- **Type**: typing.Optional[str]

### patternDescription
- **Type**: typing.Optional[str]


# DataProtectionSettings

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### associatedPortalArns
- **Type**: typing.Optional[typing.List[str]]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### customerManagedKey
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### inlineRedactionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.InlineRedactionConfigurationOutput]


# DataProtectionSettingsSummary

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]


# DeleteBrowserSettingsRequest

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataProtectionSettingsRequest

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityProviderRequest

### identityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIpAccessSettingsRequest

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNetworkSettingsRequest

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePortalRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrustStoreRequest

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserAccessLoggingSettingsRequest

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserSettingsRequest

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateBrowserSettingsRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateDataProtectionSettingsRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateIpAccessSettingsRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateNetworkSettingsRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateTrustStoreRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateUserAccessLoggingSettingsRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateUserSettingsRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# ExpireSessionRequest

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBrowserSettingsRequest

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetBrowserSettingsResponse

### browserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.BrowserSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# GetDataProtectionSettingsRequest

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataProtectionSettingsResponse

### dataProtectionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.DataProtectionSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# GetIdentityProviderRequest

### identityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentityProviderResponse

### identityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.IdentityProvider'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# GetIpAccessSettingsRequest

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetIpAccessSettingsResponse

### ipAccessSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.IpAccessSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# GetNetworkSettingsRequest

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkSettingsResponse

### networkSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.NetworkSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# GetPortalRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPortalResponse

### portal
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Portal'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# GetPortalServiceProviderMetadataRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPortalServiceProviderMetadataResponse

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### serviceProviderSamlMetadata
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# GetSessionRequest

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionResponse

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Session'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrustStoreCertificateRequest

### thumbprint
- **Type**: <class 'str'>
- **Required**: Yes

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrustStoreCertificateResponse

### certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Certificate'>
- **Required**: Yes

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# GetTrustStoreRequest

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrustStoreResponse

### trustStore
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.TrustStore'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserAccessLoggingSettingsRequest

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserAccessLoggingSettingsResponse

### userAccessLoggingSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.UserAccessLoggingSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserSettingsRequest

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserSettingsResponse

### userSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.UserSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# IdentityProvider

### identityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### identityProviderDetails
- **Type**: typing.Optional[typing.Dict[str, str]]

### identityProviderName
- **Type**: typing.Optional[str]

### identityProviderType
- **Type**: typing.Optional[typing.Literal['Facebook', 'Google', 'LoginWithAmazon', 'OIDC', 'SAML', 'SignInWithApple']]


# IdentityProviderSummary

### identityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### identityProviderName
- **Type**: typing.Optional[str]

### identityProviderType
- **Type**: typing.Optional[typing.Literal['Facebook', 'Google', 'LoginWithAmazon', 'OIDC', 'SAML', 'SignInWithApple']]


# InlineRedactionConfiguration

### inlineRedactionPatterns
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.InlineRedactionPattern]
- **Required**: Yes

### globalConfidenceLevel
- **Type**: typing.Optional[int]

### globalEnforcedUrls
- **Type**: typing.Optional[typing.List[str]]

### globalExemptUrls
- **Type**: typing.Optional[typing.List[str]]


# InlineRedactionConfigurationOutput

### inlineRedactionPatterns
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.InlineRedactionPatternOutput]
- **Required**: Yes

### globalConfidenceLevel
- **Type**: typing.Optional[int]

### globalEnforcedUrls
- **Type**: typing.Optional[typing.List[str]]

### globalExemptUrls
- **Type**: typing.Optional[typing.List[str]]


# InlineRedactionPattern

### redactionPlaceHolder
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.RedactionPlaceHolder'>
- **Required**: Yes

### builtInPatternId
- **Type**: typing.Optional[str]

### confidenceLevel
- **Type**: typing.Optional[int]

### customPattern
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.CustomPattern]

### enforcedUrls
- **Type**: typing.Optional[typing.List[str]]

### exemptUrls
- **Type**: typing.Optional[typing.List[str]]


# InlineRedactionPatternOutput

### redactionPlaceHolder
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.RedactionPlaceHolder'>
- **Required**: Yes

### builtInPatternId
- **Type**: typing.Optional[str]

### confidenceLevel
- **Type**: typing.Optional[int]

### customPattern
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.CustomPattern]

### enforcedUrls
- **Type**: typing.Optional[typing.List[str]]

### exemptUrls
- **Type**: typing.Optional[typing.List[str]]


# IpAccessSettings

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### associatedPortalArns
- **Type**: typing.Optional[typing.List[str]]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### customerManagedKey
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### ipRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.IpRule]]


# IpAccessSettingsSummary

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]


# IpRule

### ipRange
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ListBrowserSettingsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBrowserSettingsResponse

### browserSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.BrowserSettingsSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataProtectionSettingsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDataProtectionSettingsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.PaginatorConfig]


# ListDataProtectionSettingsResponse

### dataProtectionSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.DataProtectionSettingsSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIdentityProvidersRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIdentityProvidersResponse

### identityProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.IdentityProviderSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIpAccessSettingsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIpAccessSettingsResponse

### ipAccessSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.IpAccessSettingsSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkSettingsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkSettingsResponse

### networkSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.NetworkSettingsSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPortalsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPortalsResponse

### portals
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.PortalSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSessionsRequest

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['StartTimeAscending', 'StartTimeDescending']]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Terminated']]

### username
- **Type**: typing.Optional[str]


# ListSessionsRequestPaginate

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: typing.Optional[str]

### sortBy
- **Type**: typing.Optional[typing.Literal['StartTimeAscending', 'StartTimeDescending']]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Terminated']]

### username
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.PaginatorConfig]


# ListSessionsResponse

### sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.SessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# ListTrustStoreCertificatesRequest

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTrustStoreCertificatesResponse

### certificateList
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.CertificateSummary]
- **Required**: Yes

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTrustStoresRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTrustStoresResponse

### trustStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.TrustStoreSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUserAccessLoggingSettingsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListUserAccessLoggingSettingsResponse

### userAccessLoggingSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.UserAccessLoggingSettingsSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUserSettingsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListUserSettingsResponse

### userSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.UserSettingsSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# NetworkSettings

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### associatedPortalArns
- **Type**: typing.Optional[typing.List[str]]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### vpcId
- **Type**: typing.Optional[str]


# NetworkSettingsSummary

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Portal

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### authenticationType
- **Type**: typing.Optional[typing.Literal['IAM_Identity_Center', 'Standard']]

### browserSettingsArn
- **Type**: typing.Optional[str]

### browserType
- **Type**: typing.Optional[typing.Literal['Chrome']]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### customerManagedKey
- **Type**: typing.Optional[str]

### dataProtectionSettingsArn
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[typing.Literal['standard.large', 'standard.regular', 'standard.xlarge']]

### ipAccessSettingsArn
- **Type**: typing.Optional[str]

### maxConcurrentSessions
- **Type**: typing.Optional[int]

### networkSettingsArn
- **Type**: typing.Optional[str]

### portalEndpoint
- **Type**: typing.Optional[str]

### portalStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Incomplete', 'Pending']]

### rendererType
- **Type**: typing.Optional[typing.Literal['AppStream']]

### statusReason
- **Type**: typing.Optional[str]

### trustStoreArn
- **Type**: typing.Optional[str]

### userAccessLoggingSettingsArn
- **Type**: typing.Optional[str]

### userSettingsArn
- **Type**: typing.Optional[str]


# PortalSummary

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### authenticationType
- **Type**: typing.Optional[typing.Literal['IAM_Identity_Center', 'Standard']]

### browserSettingsArn
- **Type**: typing.Optional[str]

### browserType
- **Type**: typing.Optional[typing.Literal['Chrome']]

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### dataProtectionSettingsArn
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[typing.Literal['standard.large', 'standard.regular', 'standard.xlarge']]

### ipAccessSettingsArn
- **Type**: typing.Optional[str]

### maxConcurrentSessions
- **Type**: typing.Optional[int]

### networkSettingsArn
- **Type**: typing.Optional[str]

### portalEndpoint
- **Type**: typing.Optional[str]

### portalStatus
- **Type**: typing.Optional[typing.Literal['Active', 'Incomplete', 'Pending']]

### rendererType
- **Type**: typing.Optional[typing.Literal['AppStream']]

### trustStoreArn
- **Type**: typing.Optional[str]

### userAccessLoggingSettingsArn
- **Type**: typing.Optional[str]

### userSettingsArn
- **Type**: typing.Optional[str]


# RedactionPlaceHolder

### redactionPlaceHolderType
- **Type**: typing.Literal['CustomText']
- **Required**: Yes

### redactionPlaceHolderText
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


# Session

### clientIpAddresses
- **Type**: typing.Optional[typing.List[str]]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### portalArn
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Terminated']]

### username
- **Type**: typing.Optional[str]


# SessionSummary

### endTime
- **Type**: typing.Optional[datetime.datetime]

### portalArn
- **Type**: typing.Optional[str]

### sessionId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### status
- **Type**: typing.Optional[typing.Literal['Active', 'Terminated']]

### username
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Tag]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# ToolbarConfiguration

### hiddenToolbarItems
- **Type**: typing.Optional[typing.List[typing.Literal['DualMonitor', 'FullScreen', 'Microphone', 'Webcam', 'Windows']]]

### maxDisplayResolution
- **Type**: typing.Optional[typing.Literal['size1024X768', 'size1280X720', 'size1920X1080', 'size2560X1440', 'size3440X1440', 'size3840X2160', 'size4096X2160', 'size800X600']]

### toolbarType
- **Type**: typing.Optional[typing.Literal['Docked', 'Floating']]

### visualMode
- **Type**: typing.Optional[typing.Literal['Dark', 'Light']]


# ToolbarConfigurationOutput

### hiddenToolbarItems
- **Type**: typing.Optional[typing.List[typing.Literal['DualMonitor', 'FullScreen', 'Microphone', 'Webcam', 'Windows']]]

### maxDisplayResolution
- **Type**: typing.Optional[typing.Literal['size1024X768', 'size1280X720', 'size1920X1080', 'size2560X1440', 'size3440X1440', 'size3840X2160', 'size4096X2160', 'size800X600']]

### toolbarType
- **Type**: typing.Optional[typing.Literal['Docked', 'Floating']]

### visualMode
- **Type**: typing.Optional[typing.Literal['Dark', 'Light']]


# TrustStore

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### associatedPortalArns
- **Type**: typing.Optional[typing.List[str]]


# TrustStoreSummary

### trustStoreArn
- **Type**: typing.Optional[str]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateBrowserSettingsRequest

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### browserPolicy
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UpdateBrowserSettingsResponse

### browserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.BrowserSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateDataProtectionSettingsRequest

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### inlineRedactionConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.InlineRedactionConfiguration, aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.InlineRedactionConfigurationOutput, NoneType]


# UpdateDataProtectionSettingsResponse

### dataProtectionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.DataProtectionSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIdentityProviderRequest

### identityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### identityProviderDetails
- **Type**: typing.Optional[typing.Dict[str, str]]

### identityProviderName
- **Type**: typing.Optional[str]

### identityProviderType
- **Type**: typing.Optional[typing.Literal['Facebook', 'Google', 'LoginWithAmazon', 'OIDC', 'SAML', 'SignInWithApple']]


# UpdateIdentityProviderResponse

### identityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.IdentityProvider'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateIpAccessSettingsRequest

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### ipRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.IpRule]]


# UpdateIpAccessSettingsResponse

### ipAccessSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.IpAccessSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateNetworkSettingsRequest

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### subnetIds
- **Type**: typing.Optional[typing.List[str]]

### vpcId
- **Type**: typing.Optional[str]


# UpdateNetworkSettingsResponse

### networkSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.NetworkSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePortalRequest

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### authenticationType
- **Type**: typing.Optional[typing.Literal['IAM_Identity_Center', 'Standard']]

### displayName
- **Type**: typing.Optional[str]

### instanceType
- **Type**: typing.Optional[typing.Literal['standard.large', 'standard.regular', 'standard.xlarge']]

### maxConcurrentSessions
- **Type**: typing.Optional[int]


# UpdatePortalResponse

### portal
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.Portal'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTrustStoreRequest

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificatesToAdd
- **Type**: typing.Optional[typing.List[typing.Union[str, bytes, typing.IO[typing.Any], botocore.response.StreamingBody]]]

### certificatesToDelete
- **Type**: typing.Optional[typing.List[str]]

### clientToken
- **Type**: typing.Optional[str]


# UpdateTrustStoreResponse

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserAccessLoggingSettingsRequest

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### kinesisStreamArn
- **Type**: typing.Optional[str]


# UpdateUserAccessLoggingSettingsResponse

### userAccessLoggingSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.UserAccessLoggingSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateUserSettingsRequest

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### cookieSynchronizationConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.CookieSynchronizationConfiguration, aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.CookieSynchronizationConfigurationOutput, NoneType]

### copyAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### deepLinkAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### disconnectTimeoutInMinutes
- **Type**: typing.Optional[int]

### downloadAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### idleDisconnectTimeoutInMinutes
- **Type**: typing.Optional[int]

### pasteAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### printAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### toolbarConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ToolbarConfiguration, aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ToolbarConfigurationOutput, NoneType]

### uploadAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# UpdateUserSettingsResponse

### userSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.UserSettings'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ResponseMetadata'>
- **Required**: Yes


# UserAccessLoggingSettings

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### associatedPortalArns
- **Type**: typing.Optional[typing.List[str]]

### kinesisStreamArn
- **Type**: typing.Optional[str]


# UserAccessLoggingSettingsSummary

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### kinesisStreamArn
- **Type**: typing.Optional[str]


# UserSettings

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### associatedPortalArns
- **Type**: typing.Optional[typing.List[str]]

### cookieSynchronizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.CookieSynchronizationConfigurationOutput]

### copyAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### customerManagedKey
- **Type**: typing.Optional[str]

### deepLinkAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### disconnectTimeoutInMinutes
- **Type**: typing.Optional[int]

### downloadAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### idleDisconnectTimeoutInMinutes
- **Type**: typing.Optional[int]

### pasteAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### printAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### toolbarConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ToolbarConfigurationOutput]

### uploadAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# UserSettingsSummary

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### cookieSynchronizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.CookieSynchronizationConfigurationOutput]

### copyAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### deepLinkAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### disconnectTimeoutInMinutes
- **Type**: typing.Optional[int]

### downloadAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### idleDisconnectTimeoutInMinutes
- **Type**: typing.Optional[int]

### pasteAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### printAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### toolbarConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web.workspaces_web_classes.ToolbarConfigurationOutput]

### uploadAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


