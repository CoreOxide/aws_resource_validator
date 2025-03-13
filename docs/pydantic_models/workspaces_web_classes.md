# Workspaces Web Classes

# AssociateBrowserSettingsRequestTypeDef

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateBrowserSettingsResponseTypeDef

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateDataProtectionSettingsRequestTypeDef

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateDataProtectionSettingsResponseTypeDef

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateIpAccessSettingsRequestTypeDef

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateIpAccessSettingsResponseTypeDef

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateNetworkSettingsRequestTypeDef

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateNetworkSettingsResponseTypeDef

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateTrustStoreRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateTrustStoreResponseTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateUserAccessLoggingSettingsRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateUserAccessLoggingSettingsResponseTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateUserSettingsRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateUserSettingsResponseTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BlobTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BrowserSettingsSummaryTypeDef

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# BrowserSettingsTypeDef

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


# CertificateSummaryTypeDef

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


# CertificateTypeDef

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


# CookieSpecificationTypeDef

### domain
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### path
- **Type**: typing.Optional[str]


# CookieSynchronizationConfigurationOutputTypeDef

### allowlist
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.CookieSpecificationTypeDef]
- **Required**: Yes

### blocklist
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.CookieSpecificationTypeDef]]


# CookieSynchronizationConfigurationTypeDef

### allowlist
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.CookieSpecificationTypeDef]
- **Required**: Yes

### blocklist
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.CookieSpecificationTypeDef]]


# CookieSynchronizationConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateBrowserSettingsRequestTypeDef

### browserPolicy
- **Type**: <class 'str'>
- **Required**: Yes

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]

### customerManagedKey
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.TagTypeDef]]


# CreateBrowserSettingsResponseTypeDef

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataProtectionSettingsRequestTypeDef

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]

### customerManagedKey
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### inlineRedactionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.InlineRedactionConfigurationUnionTypeDef]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.TagTypeDef]]


# CreateDataProtectionSettingsResponseTypeDef

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIdentityProviderRequestTypeDef

### identityProviderDetails
- **Type**: typing.Mapping[str, str]
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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.TagTypeDef]]


# CreateIdentityProviderResponseTypeDef

### identityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIpAccessSettingsRequestTypeDef

### ipRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.IpRuleTypeDef]
- **Required**: Yes

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]

### customerManagedKey
- **Type**: typing.Optional[str]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.TagTypeDef]]


# CreateIpAccessSettingsResponseTypeDef

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNetworkSettingsRequestTypeDef

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### vpcId
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.TagTypeDef]]


# CreateNetworkSettingsResponseTypeDef

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePortalRequestTypeDef

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Mapping[str, str]]

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.TagTypeDef]]


# CreatePortalResponseTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### portalEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrustStoreRequestTypeDef

### certificateList
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.BlobTypeDef]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.TagTypeDef]]


# CreateTrustStoreResponseTypeDef

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserAccessLoggingSettingsRequestTypeDef

### kinesisStreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.TagTypeDef]]


# CreateUserAccessLoggingSettingsResponseTypeDef

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserSettingsRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]

### clientToken
- **Type**: typing.Optional[str]

### cookieSynchronizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.CookieSynchronizationConfigurationUnionTypeDef]

### customerManagedKey
- **Type**: typing.Optional[str]

### deepLinkAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### disconnectTimeoutInMinutes
- **Type**: typing.Optional[int]

### idleDisconnectTimeoutInMinutes
- **Type**: typing.Optional[int]

### tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.TagTypeDef]]

### toolbarConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.ToolbarConfigurationUnionTypeDef]


# CreateUserSettingsResponseTypeDef

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomPatternTypeDef

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


# DataProtectionSettingsSummaryTypeDef

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]


# DataProtectionSettingsTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.InlineRedactionConfigurationOutputTypeDef]


# DeleteBrowserSettingsRequestTypeDef

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDataProtectionSettingsRequestTypeDef

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityProviderRequestTypeDef

### identityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIpAccessSettingsRequestTypeDef

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNetworkSettingsRequestTypeDef

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePortalRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrustStoreRequestTypeDef

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserAccessLoggingSettingsRequestTypeDef

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserSettingsRequestTypeDef

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateBrowserSettingsRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateDataProtectionSettingsRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateIpAccessSettingsRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateNetworkSettingsRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateTrustStoreRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateUserAccessLoggingSettingsRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateUserSettingsRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# ExpireSessionRequestTypeDef

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetBrowserSettingsRequestTypeDef

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetBrowserSettingsResponseTypeDef

### browserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.BrowserSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDataProtectionSettingsRequestTypeDef

### dataProtectionSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetDataProtectionSettingsResponseTypeDef

### dataProtectionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.DataProtectionSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIdentityProviderRequestTypeDef

### identityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetIdentityProviderResponseTypeDef

### identityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.IdentityProviderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIpAccessSettingsRequestTypeDef

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetIpAccessSettingsResponseTypeDef

### ipAccessSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.IpAccessSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetNetworkSettingsRequestTypeDef

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetNetworkSettingsResponseTypeDef

### networkSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.NetworkSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPortalRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPortalResponseTypeDef

### portal
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.PortalTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPortalServiceProviderMetadataRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPortalServiceProviderMetadataResponseTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### serviceProviderSamlMetadata
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSessionRequestTypeDef

### portalId
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSessionResponseTypeDef

### session
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.SessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrustStoreCertificateRequestTypeDef

### thumbprint
- **Type**: <class 'str'>
- **Required**: Yes

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrustStoreCertificateResponseTypeDef

### certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.CertificateTypeDef'>
- **Required**: Yes

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetTrustStoreRequestTypeDef

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetTrustStoreResponseTypeDef

### trustStore
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.TrustStoreTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserAccessLoggingSettingsRequestTypeDef

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserAccessLoggingSettingsResponseTypeDef

### userAccessLoggingSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.UserAccessLoggingSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserSettingsRequestTypeDef

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserSettingsResponseTypeDef

### userSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.UserSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdentityProviderSummaryTypeDef

### identityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### identityProviderName
- **Type**: typing.Optional[str]

### identityProviderType
- **Type**: typing.Optional[typing.Literal['Facebook', 'Google', 'LoginWithAmazon', 'OIDC', 'SAML', 'SignInWithApple']]


# IdentityProviderTypeDef

### identityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### identityProviderDetails
- **Type**: typing.Optional[typing.Dict[str, str]]

### identityProviderName
- **Type**: typing.Optional[str]

### identityProviderType
- **Type**: typing.Optional[typing.Literal['Facebook', 'Google', 'LoginWithAmazon', 'OIDC', 'SAML', 'SignInWithApple']]


# InlineRedactionConfigurationOutputTypeDef

### inlineRedactionPatterns
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.InlineRedactionPatternOutputTypeDef]
- **Required**: Yes

### globalConfidenceLevel
- **Type**: typing.Optional[int]

### globalEnforcedUrls
- **Type**: typing.Optional[typing.List[str]]

### globalExemptUrls
- **Type**: typing.Optional[typing.List[str]]


# InlineRedactionConfigurationTypeDef

### inlineRedactionPatterns
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.InlineRedactionPatternTypeDef]
- **Required**: Yes

### globalConfidenceLevel
- **Type**: typing.Optional[int]

### globalEnforcedUrls
- **Type**: typing.Optional[typing.Sequence[str]]

### globalExemptUrls
- **Type**: typing.Optional[typing.Sequence[str]]


# InlineRedactionConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# InlineRedactionPatternOutputTypeDef

### redactionPlaceHolder
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.RedactionPlaceHolderTypeDef'>
- **Required**: Yes

### builtInPatternId
- **Type**: typing.Optional[str]

### confidenceLevel
- **Type**: typing.Optional[int]

### customPattern
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.CustomPatternTypeDef]

### enforcedUrls
- **Type**: typing.Optional[typing.List[str]]

### exemptUrls
- **Type**: typing.Optional[typing.List[str]]


# InlineRedactionPatternTypeDef

### redactionPlaceHolder
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.RedactionPlaceHolderTypeDef'>
- **Required**: Yes

### builtInPatternId
- **Type**: typing.Optional[str]

### confidenceLevel
- **Type**: typing.Optional[int]

### customPattern
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.CustomPatternTypeDef]

### enforcedUrls
- **Type**: typing.Optional[typing.Sequence[str]]

### exemptUrls
- **Type**: typing.Optional[typing.Sequence[str]]


# IpAccessSettingsSummaryTypeDef

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### creationDate
- **Type**: typing.Optional[datetime.datetime]

### description
- **Type**: typing.Optional[str]

### displayName
- **Type**: typing.Optional[str]


# IpAccessSettingsTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.IpRuleTypeDef]]


# IpRuleTypeDef

### ipRange
- **Type**: <class 'str'>
- **Required**: Yes

### description
- **Type**: typing.Optional[str]


# ListBrowserSettingsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBrowserSettingsResponseTypeDef

### browserSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.BrowserSettingsSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListDataProtectionSettingsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.PaginatorConfigTypeDef]


# ListDataProtectionSettingsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListDataProtectionSettingsResponseTypeDef

### dataProtectionSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.DataProtectionSettingsSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIdentityProvidersRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIdentityProvidersResponseTypeDef

### identityProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.IdentityProviderSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIpAccessSettingsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIpAccessSettingsResponseTypeDef

### ipAccessSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.IpAccessSettingsSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkSettingsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkSettingsResponseTypeDef

### networkSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.NetworkSettingsSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPortalsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPortalsResponseTypeDef

### portals
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.PortalSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListSessionsRequestPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.PaginatorConfigTypeDef]


# ListSessionsRequestTypeDef

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


# ListSessionsResponseTypeDef

### sessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.SessionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTrustStoreCertificatesRequestTypeDef

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTrustStoreCertificatesResponseTypeDef

### certificateList
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.CertificateSummaryTypeDef]
- **Required**: Yes

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTrustStoresRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTrustStoresResponseTypeDef

### trustStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.TrustStoreSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUserAccessLoggingSettingsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListUserAccessLoggingSettingsResponseTypeDef

### userAccessLoggingSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.UserAccessLoggingSettingsSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListUserSettingsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListUserSettingsResponseTypeDef

### userSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.UserSettingsSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# NetworkSettingsSummaryTypeDef

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### vpcId
- **Type**: typing.Optional[str]


# NetworkSettingsTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PortalSummaryTypeDef

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


# PortalTypeDef

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


# RedactionPlaceHolderTypeDef

### redactionPlaceHolderType
- **Type**: typing.Literal['CustomText']
- **Required**: Yes

### redactionPlaceHolderText
- **Type**: typing.Optional[str]


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


# SessionSummaryTypeDef

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


# SessionTypeDef

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


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.TagTypeDef]
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ToolbarConfigurationOutputTypeDef

### hiddenToolbarItems
- **Type**: typing.Optional[typing.List[typing.Literal['DualMonitor', 'FullScreen', 'Microphone', 'Webcam', 'Windows']]]

### maxDisplayResolution
- **Type**: typing.Optional[typing.Literal['size1024X768', 'size1280X720', 'size1920X1080', 'size2560X1440', 'size3440X1440', 'size3840X2160', 'size4096X2160', 'size800X600']]

### toolbarType
- **Type**: typing.Optional[typing.Literal['Docked', 'Floating']]

### visualMode
- **Type**: typing.Optional[typing.Literal['Dark', 'Light']]


# ToolbarConfigurationTypeDef

### hiddenToolbarItems
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DualMonitor', 'FullScreen', 'Microphone', 'Webcam', 'Windows']]]

### maxDisplayResolution
- **Type**: typing.Optional[typing.Literal['size1024X768', 'size1280X720', 'size1920X1080', 'size2560X1440', 'size3440X1440', 'size3840X2160', 'size4096X2160', 'size800X600']]

### toolbarType
- **Type**: typing.Optional[typing.Literal['Docked', 'Floating']]

### visualMode
- **Type**: typing.Optional[typing.Literal['Dark', 'Light']]


# ToolbarConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TrustStoreSummaryTypeDef

### trustStoreArn
- **Type**: typing.Optional[str]


# TrustStoreTypeDef

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### associatedPortalArns
- **Type**: typing.Optional[typing.List[str]]


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBrowserSettingsRequestTypeDef

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### browserPolicy
- **Type**: typing.Optional[str]

### clientToken
- **Type**: typing.Optional[str]


# UpdateBrowserSettingsResponseTypeDef

### browserSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.BrowserSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateDataProtectionSettingsRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.InlineRedactionConfigurationUnionTypeDef]


# UpdateDataProtectionSettingsResponseTypeDef

### dataProtectionSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.DataProtectionSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIdentityProviderRequestTypeDef

### identityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### identityProviderDetails
- **Type**: typing.Optional[typing.Mapping[str, str]]

### identityProviderName
- **Type**: typing.Optional[str]

### identityProviderType
- **Type**: typing.Optional[typing.Literal['Facebook', 'Google', 'LoginWithAmazon', 'OIDC', 'SAML', 'SignInWithApple']]


# UpdateIdentityProviderResponseTypeDef

### identityProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.IdentityProviderTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateIpAccessSettingsRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.IpRuleTypeDef]]


# UpdateIpAccessSettingsResponseTypeDef

### ipAccessSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.IpAccessSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateNetworkSettingsRequestTypeDef

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### securityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### subnetIds
- **Type**: typing.Optional[typing.Sequence[str]]

### vpcId
- **Type**: typing.Optional[str]


# UpdateNetworkSettingsResponseTypeDef

### networkSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.NetworkSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePortalRequestTypeDef

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


# UpdatePortalResponseTypeDef

### portal
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.PortalTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTrustStoreRequestTypeDef

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificatesToAdd
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workspaces_web_classes.BlobTypeDef]]

### certificatesToDelete
- **Type**: typing.Optional[typing.Sequence[str]]

### clientToken
- **Type**: typing.Optional[str]


# UpdateTrustStoreResponseTypeDef

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserAccessLoggingSettingsRequestTypeDef

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### kinesisStreamArn
- **Type**: typing.Optional[str]


# UpdateUserAccessLoggingSettingsResponseTypeDef

### userAccessLoggingSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.UserAccessLoggingSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateUserSettingsRequestTypeDef

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### cookieSynchronizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.CookieSynchronizationConfigurationUnionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.ToolbarConfigurationUnionTypeDef]

### uploadAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# UpdateUserSettingsResponseTypeDef

### userSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.UserSettingsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserAccessLoggingSettingsSummaryTypeDef

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### kinesisStreamArn
- **Type**: typing.Optional[str]


# UserAccessLoggingSettingsTypeDef

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### associatedPortalArns
- **Type**: typing.Optional[typing.List[str]]

### kinesisStreamArn
- **Type**: typing.Optional[str]


# UserSettingsSummaryTypeDef

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### cookieSynchronizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.CookieSynchronizationConfigurationOutputTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.ToolbarConfigurationOutputTypeDef]

### uploadAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# UserSettingsTypeDef

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### additionalEncryptionContext
- **Type**: typing.Optional[typing.Dict[str, str]]

### associatedPortalArns
- **Type**: typing.Optional[typing.List[str]]

### cookieSynchronizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.CookieSynchronizationConfigurationOutputTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.ToolbarConfigurationOutputTypeDef]

### uploadAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


