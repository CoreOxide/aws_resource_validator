# Pydantic Models in workspaces_web_classes

# AssociateBrowserSettingsRequestRequestTypeDef

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


# AssociateIpAccessSettingsRequestRequestTypeDef

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


# AssociateNetworkSettingsRequestRequestTypeDef

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


# AssociateTrustStoreRequestRequestTypeDef

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


# AssociateUserAccessLoggingSettingsRequestRequestTypeDef

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


# AssociateUserSettingsRequestRequestTypeDef

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


# CreateBrowserSettingsRequestRequestTypeDef

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


# CreateIdentityProviderRequestRequestTypeDef

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


# CreateIpAccessSettingsRequestRequestTypeDef

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


# CreateNetworkSettingsRequestRequestTypeDef

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


# CreatePortalRequestRequestTypeDef

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


# CreateTrustStoreRequestRequestTypeDef

### certificateList
- **Type**: typing.Sequence[typing.Union[str, bytes, typing.IO[typing.Any]]]
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


# CreateUserAccessLoggingSettingsRequestRequestTypeDef

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


# CreateUserSettingsRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.CookieSynchronizationConfigurationTypeDef]

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


# CreateUserSettingsResponseTypeDef

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBrowserSettingsRequestRequestTypeDef

### browserSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityProviderRequestRequestTypeDef

### identityProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIpAccessSettingsRequestRequestTypeDef

### ipAccessSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteNetworkSettingsRequestRequestTypeDef

### networkSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePortalRequestRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrustStoreRequestRequestTypeDef

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserAccessLoggingSettingsRequestRequestTypeDef

### userAccessLoggingSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserSettingsRequestRequestTypeDef

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateBrowserSettingsRequestRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateIpAccessSettingsRequestRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateNetworkSettingsRequestRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateTrustStoreRequestRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateUserAccessLoggingSettingsRequestRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateUserSettingsRequestRequestTypeDef

### portalArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetBrowserSettingsRequestRequestTypeDef

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


# GetIdentityProviderRequestRequestTypeDef

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


# GetIpAccessSettingsRequestRequestTypeDef

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


# GetNetworkSettingsRequestRequestTypeDef

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


# GetPortalRequestRequestTypeDef

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


# GetPortalServiceProviderMetadataRequestRequestTypeDef

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


# GetTrustStoreCertificateRequestRequestTypeDef

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


# GetTrustStoreRequestRequestTypeDef

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


# GetUserAccessLoggingSettingsRequestRequestTypeDef

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


# GetUserSettingsRequestRequestTypeDef

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


# ListBrowserSettingsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListBrowserSettingsResponseTypeDef

### browserSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.BrowserSettingsSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIdentityProvidersRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListIpAccessSettingsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListIpAccessSettingsResponseTypeDef

### ipAccessSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.IpAccessSettingsSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListNetworkSettingsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListNetworkSettingsResponseTypeDef

### networkSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.NetworkSettingsSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPortalsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPortalsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### portals
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.PortalSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListTrustStoreCertificatesRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTrustStoresRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListTrustStoresResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### trustStores
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.TrustStoreSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUserAccessLoggingSettingsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListUserAccessLoggingSettingsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### userAccessLoggingSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.UserAccessLoggingSettingsSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUserSettingsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListUserSettingsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### userSettings
- **Type**: typing.List[aws_resource_validator.pydantic_models.workspaces_web_classes.UserSettingsSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workspaces_web_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# TagResourceRequestRequestTypeDef

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


# TrustStoreSummaryTypeDef

### trustStoreArn
- **Type**: typing.Optional[str]


# TrustStoreTypeDef

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### associatedPortalArns
- **Type**: typing.Optional[typing.List[str]]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateBrowserSettingsRequestRequestTypeDef

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


# UpdateIdentityProviderRequestRequestTypeDef

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


# UpdateIpAccessSettingsRequestRequestTypeDef

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


# UpdateNetworkSettingsRequestRequestTypeDef

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


# UpdatePortalRequestRequestTypeDef

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


# UpdateTrustStoreRequestRequestTypeDef

### trustStoreArn
- **Type**: <class 'str'>
- **Required**: Yes

### certificatesToAdd
- **Type**: typing.Optional[typing.Sequence[typing.Union[str, bytes, typing.IO[typing.Any]]]]

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


# UpdateUserAccessLoggingSettingsRequestRequestTypeDef

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


# UpdateUserSettingsRequestRequestTypeDef

### userSettingsArn
- **Type**: <class 'str'>
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### cookieSynchronizationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workspaces_web_classes.CookieSynchronizationConfigurationTypeDef]

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

### uploadAllowed
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


