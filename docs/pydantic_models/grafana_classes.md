# Grafana Classes

# AssertionAttributesTypeDef

### email
- **Type**: typing.Optional[str]

### groups
- **Type**: typing.Optional[str]

### login
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### org
- **Type**: typing.Optional[str]

### role
- **Type**: typing.Optional[str]


# AssociateLicenseRequestTypeDef

### licenseType
- **Type**: typing.Literal['ENTERPRISE', 'ENTERPRISE_FREE_TRIAL']
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### grafanaToken
- **Type**: typing.Optional[str]


# AssociateLicenseResponseTypeDef

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.WorkspaceDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AuthenticationDescriptionTypeDef

### providers
- **Type**: typing.List[typing.Literal['AWS_SSO', 'SAML']]
- **Required**: Yes

### awsSso
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.AwsSsoAuthenticationTypeDef]

### saml
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.SamlAuthenticationTypeDef]


# AuthenticationSummaryTypeDef

### providers
- **Type**: typing.List[typing.Literal['AWS_SSO', 'SAML']]
- **Required**: Yes

### samlConfigurationStatus
- **Type**: typing.Optional[typing.Literal['CONFIGURED', 'NOT_CONFIGURED']]


# AwsSsoAuthenticationTypeDef

### ssoClientId
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateWorkspaceApiKeyRequestTypeDef

### keyName
- **Type**: <class 'str'>
- **Required**: Yes

### keyRole
- **Type**: <class 'str'>
- **Required**: Yes

### secondsToLive
- **Type**: <class 'int'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateWorkspaceApiKeyResponseTypeDef

### key
- **Type**: <class 'str'>
- **Required**: Yes

### keyName
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkspaceRequestTypeDef

### accountAccessType
- **Type**: typing.Literal['CURRENT_ACCOUNT', 'ORGANIZATION']
- **Required**: Yes

### authenticationProviders
- **Type**: typing.Sequence[typing.Literal['AWS_SSO', 'SAML']]
- **Required**: Yes

### permissionType
- **Type**: typing.Literal['CUSTOMER_MANAGED', 'SERVICE_MANAGED']
- **Required**: Yes

### clientToken
- **Type**: typing.Optional[str]

### configuration
- **Type**: typing.Optional[str]

### grafanaVersion
- **Type**: typing.Optional[str]

### networkAccessControl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.NetworkAccessConfigurationUnionTypeDef]

### organizationRoleName
- **Type**: typing.Optional[str]

### stackSetName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.VpcConfigurationUnionTypeDef]

### workspaceDataSources
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AMAZON_OPENSEARCH_SERVICE', 'ATHENA', 'CLOUDWATCH', 'PROMETHEUS', 'REDSHIFT', 'SITEWISE', 'TIMESTREAM', 'TWINMAKER', 'XRAY']]]

### workspaceDescription
- **Type**: typing.Optional[str]

### workspaceName
- **Type**: typing.Optional[str]

### workspaceNotificationDestinations
- **Type**: typing.Optional[typing.Sequence[typing.Literal['SNS']]]

### workspaceOrganizationalUnits
- **Type**: typing.Optional[typing.Sequence[str]]

### workspaceRoleArn
- **Type**: typing.Optional[str]


# CreateWorkspaceResponseTypeDef

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.WorkspaceDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkspaceServiceAccountRequestTypeDef

### grafanaRole
- **Type**: typing.Literal['ADMIN', 'EDITOR', 'VIEWER']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateWorkspaceServiceAccountTokenRequestTypeDef

### name
- **Type**: <class 'str'>
- **Required**: Yes

### secondsToLive
- **Type**: <class 'int'>
- **Required**: Yes

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateWorkspaceServiceAccountTokenResponseTypeDef

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceAccountToken
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ServiceAccountTokenSummaryWithKeyTypeDef'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteWorkspaceApiKeyRequestTypeDef

### keyName
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkspaceApiKeyResponseTypeDef

### keyName
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteWorkspaceRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkspaceResponseTypeDef

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.WorkspaceDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteWorkspaceServiceAccountRequestTypeDef

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkspaceServiceAccountResponseTypeDef

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteWorkspaceServiceAccountTokenRequestTypeDef

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### tokenId
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkspaceServiceAccountTokenResponseTypeDef

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### tokenId
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorkspaceAuthenticationRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkspaceAuthenticationResponseTypeDef

### authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.AuthenticationDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorkspaceConfigurationRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkspaceConfigurationResponseTypeDef

### configuration
- **Type**: <class 'str'>
- **Required**: Yes

### grafanaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorkspaceRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkspaceResponseTypeDef

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.WorkspaceDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateLicenseRequestTypeDef

### licenseType
- **Type**: typing.Literal['ENTERPRISE', 'ENTERPRISE_FREE_TRIAL']
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateLicenseResponseTypeDef

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.WorkspaceDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IdpMetadataTypeDef

### url
- **Type**: typing.Optional[str]

### xml
- **Type**: typing.Optional[str]


# ListPermissionsRequestPaginateTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### groupId
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### userType
- **Type**: typing.Optional[typing.Literal['SSO_GROUP', 'SSO_USER']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.PaginatorConfigTypeDef]


# ListPermissionsRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### groupId
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### userType
- **Type**: typing.Optional[typing.Literal['SSO_GROUP', 'SSO_USER']]


# ListPermissionsResponseTypeDef

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana_classes.PermissionEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVersionsRequestPaginateTypeDef

### workspaceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.PaginatorConfigTypeDef]


# ListVersionsRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### workspaceId
- **Type**: typing.Optional[str]


# ListVersionsResponseTypeDef

### grafanaVersions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspaceServiceAccountTokensRequestPaginateTypeDef

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.PaginatorConfigTypeDef]


# ListWorkspaceServiceAccountTokensRequestTypeDef

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspaceServiceAccountTokensResponseTypeDef

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceAccountTokens
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana_classes.ServiceAccountTokenSummaryTypeDef]
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspaceServiceAccountsRequestPaginateTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.PaginatorConfigTypeDef]


# ListWorkspaceServiceAccountsRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspaceServiceAccountsResponseTypeDef

### serviceAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana_classes.ServiceAccountSummaryTypeDef]
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspacesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.PaginatorConfigTypeDef]


# ListWorkspacesRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspacesResponseTypeDef

### workspaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana_classes.WorkspaceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# NetworkAccessConfigurationOutputTypeDef

### prefixListIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpceIds
- **Type**: typing.List[str]
- **Required**: Yes


# NetworkAccessConfigurationTypeDef

### prefixListIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### vpceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# NetworkAccessConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionEntryTypeDef

### role
- **Type**: typing.Literal['ADMIN', 'EDITOR', 'VIEWER']
- **Required**: Yes

### user
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.UserTypeDef'>
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


# RoleValuesOutputTypeDef

### admin
- **Type**: typing.Optional[typing.List[str]]

### editor
- **Type**: typing.Optional[typing.List[str]]


# RoleValuesTypeDef

### admin
- **Type**: typing.Optional[typing.Sequence[str]]

### editor
- **Type**: typing.Optional[typing.Sequence[str]]


# SamlAuthenticationTypeDef

### status
- **Type**: typing.Literal['CONFIGURED', 'NOT_CONFIGURED']
- **Required**: Yes

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.SamlConfigurationOutputTypeDef]


# SamlConfigurationOutputTypeDef

### idpMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.IdpMetadataTypeDef'>
- **Required**: Yes

### allowedOrganizations
- **Type**: typing.Optional[typing.List[str]]

### assertionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.AssertionAttributesTypeDef]

### loginValidityDuration
- **Type**: typing.Optional[int]

### roleValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.RoleValuesOutputTypeDef]


# SamlConfigurationTypeDef

### idpMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.IdpMetadataTypeDef'>
- **Required**: Yes

### allowedOrganizations
- **Type**: typing.Optional[typing.Sequence[str]]

### assertionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.AssertionAttributesTypeDef]

### loginValidityDuration
- **Type**: typing.Optional[int]

### roleValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.RoleValuesTypeDef]


# SamlConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceAccountSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceAccountTokenSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceAccountTokenSummaryWithKeyTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateErrorTypeDef

### causedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.UpdateInstructionOutputTypeDef'>
- **Required**: Yes

### code
- **Type**: <class 'int'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateInstructionOutputTypeDef

### action
- **Type**: typing.Literal['ADD', 'REVOKE']
- **Required**: Yes

### role
- **Type**: typing.Literal['ADMIN', 'EDITOR', 'VIEWER']
- **Required**: Yes

### users
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana_classes.UserTypeDef]
- **Required**: Yes


# UpdateInstructionTypeDef

### action
- **Type**: typing.Literal['ADD', 'REVOKE']
- **Required**: Yes

### role
- **Type**: typing.Literal['ADMIN', 'EDITOR', 'VIEWER']
- **Required**: Yes

### users
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.grafana_classes.UserTypeDef]
- **Required**: Yes


# UpdateInstructionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdatePermissionsRequestTypeDef

### updateInstructionBatch
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.grafana_classes.UpdateInstructionUnionTypeDef]
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePermissionsResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana_classes.UpdateErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkspaceAuthenticationRequestTypeDef

### authenticationProviders
- **Type**: typing.Sequence[typing.Literal['AWS_SSO', 'SAML']]
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### samlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.SamlConfigurationUnionTypeDef]


# UpdateWorkspaceAuthenticationResponseTypeDef

### authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.AuthenticationDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkspaceConfigurationRequestTypeDef

### configuration
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### grafanaVersion
- **Type**: typing.Optional[str]


# UpdateWorkspaceRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### accountAccessType
- **Type**: typing.Optional[typing.Literal['CURRENT_ACCOUNT', 'ORGANIZATION']]

### networkAccessControl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.NetworkAccessConfigurationUnionTypeDef]

### organizationRoleName
- **Type**: typing.Optional[str]

### permissionType
- **Type**: typing.Optional[typing.Literal['CUSTOMER_MANAGED', 'SERVICE_MANAGED']]

### removeNetworkAccessConfiguration
- **Type**: typing.Optional[bool]

### removeVpcConfiguration
- **Type**: typing.Optional[bool]

### stackSetName
- **Type**: typing.Optional[str]

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.VpcConfigurationUnionTypeDef]

### workspaceDataSources
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AMAZON_OPENSEARCH_SERVICE', 'ATHENA', 'CLOUDWATCH', 'PROMETHEUS', 'REDSHIFT', 'SITEWISE', 'TIMESTREAM', 'TWINMAKER', 'XRAY']]]

### workspaceDescription
- **Type**: typing.Optional[str]

### workspaceName
- **Type**: typing.Optional[str]

### workspaceNotificationDestinations
- **Type**: typing.Optional[typing.Sequence[typing.Literal['SNS']]]

### workspaceOrganizationalUnits
- **Type**: typing.Optional[typing.Sequence[str]]

### workspaceRoleArn
- **Type**: typing.Optional[str]


# UpdateWorkspaceResponseTypeDef

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.WorkspaceDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# VpcConfigurationOutputTypeDef

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes


# VpcConfigurationTypeDef

### securityGroupIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# VpcConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkspaceDescriptionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# WorkspaceSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

