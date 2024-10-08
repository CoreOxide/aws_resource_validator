# Pydantic Models in grafana_classes

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


# AssociateLicenseRequestRequestTypeDef

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

# CreateWorkspaceApiKeyRequestRequestTypeDef

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


# CreateWorkspaceRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.NetworkAccessConfigurationTypeDef]

### organizationRoleName
- **Type**: typing.Optional[str]

### stackSetName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.VpcConfigurationTypeDef]

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


# CreateWorkspaceServiceAccountRequestRequestTypeDef

### grafanaRole
- **Type**: typing.Literal['ADMIN', 'EDITOR', 'VIEWER']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateWorkspaceServiceAccountResponseTypeDef

### grafanaRole
- **Type**: typing.Literal['ADMIN', 'EDITOR', 'VIEWER']
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateWorkspaceServiceAccountTokenRequestRequestTypeDef

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


# DeleteWorkspaceApiKeyRequestRequestTypeDef

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


# DeleteWorkspaceRequestRequestTypeDef

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


# DeleteWorkspaceServiceAccountRequestRequestTypeDef

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


# DeleteWorkspaceServiceAccountTokenRequestRequestTypeDef

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


# DescribeWorkspaceAuthenticationRequestRequestTypeDef

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


# DescribeWorkspaceConfigurationRequestRequestTypeDef

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


# DescribeWorkspaceRequestRequestTypeDef

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


# DisassociateLicenseRequestRequestTypeDef

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


# ListPermissionsRequestListPermissionsPaginateTypeDef

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


# ListPermissionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana_classes.PermissionEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListVersionsRequestListVersionsPaginateTypeDef

### workspaceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.PaginatorConfigTypeDef]


# ListVersionsRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkspaceServiceAccountTokensRequestRequestTypeDef

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

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

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


# ListWorkspaceServiceAccountsRequestListWorkspaceServiceAccountsPaginateTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.PaginatorConfigTypeDef]


# ListWorkspaceServiceAccountsRequestRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspaceServiceAccountsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### serviceAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana_classes.ServiceAccountSummaryTypeDef]
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListWorkspacesRequestListWorkspacesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.PaginatorConfigTypeDef]


# ListWorkspacesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspacesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### workspaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana_classes.WorkspaceSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# ServiceAccountSummaryTypeDef

### grafanaRole
- **Type**: typing.Literal['ADMIN', 'EDITOR', 'VIEWER']
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### isDisabled
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# ServiceAccountTokenSummaryTypeDef

### createdAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### expiresAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### lastUsedAt
- **Type**: typing.Optional[datetime.datetime]


# ServiceAccountTokenSummaryWithKeyTypeDef

### id
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

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


# UpdatePermissionsRequestRequestTypeDef

### updateInstructionBatch
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.grafana_classes.UpdateInstructionTypeDef, aws_resource_validator.pydantic_models.grafana_classes.UpdateInstructionOutputTypeDef]]
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


# UpdateWorkspaceAuthenticationRequestRequestTypeDef

### authenticationProviders
- **Type**: typing.Sequence[typing.Literal['AWS_SSO', 'SAML']]
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### samlConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.SamlConfigurationTypeDef]


# UpdateWorkspaceAuthenticationResponseTypeDef

### authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.AuthenticationDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateWorkspaceConfigurationRequestRequestTypeDef

### configuration
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### grafanaVersion
- **Type**: typing.Optional[str]


# UpdateWorkspaceRequestRequestTypeDef

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### accountAccessType
- **Type**: typing.Optional[typing.Literal['CURRENT_ACCOUNT', 'ORGANIZATION']]

### networkAccessControl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.NetworkAccessConfigurationTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.VpcConfigurationTypeDef]

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

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['SSO_GROUP', 'SSO_USER']
- **Required**: Yes


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


# WorkspaceDescriptionTypeDef

### authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.AuthenticationSummaryTypeDef'>
- **Required**: Yes

### created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### dataSources
- **Type**: typing.List[typing.Literal['AMAZON_OPENSEARCH_SERVICE', 'ATHENA', 'CLOUDWATCH', 'PROMETHEUS', 'REDSHIFT', 'SITEWISE', 'TIMESTREAM', 'TWINMAKER', 'XRAY']]
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### grafanaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### modified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATION_FAILED', 'DELETING', 'DELETION_FAILED', 'FAILED', 'LICENSE_REMOVAL_FAILED', 'UPDATE_FAILED', 'UPDATING', 'UPGRADE_FAILED', 'UPGRADING', 'VERSION_UPDATE_FAILED', 'VERSION_UPDATING']
- **Required**: Yes

### accountAccessType
- **Type**: typing.Optional[typing.Literal['CURRENT_ACCOUNT', 'ORGANIZATION']]

### description
- **Type**: typing.Optional[str]

### freeTrialConsumed
- **Type**: typing.Optional[bool]

### freeTrialExpiration
- **Type**: typing.Optional[datetime.datetime]

### grafanaToken
- **Type**: typing.Optional[str]

### licenseExpiration
- **Type**: typing.Optional[datetime.datetime]

### licenseType
- **Type**: typing.Optional[typing.Literal['ENTERPRISE', 'ENTERPRISE_FREE_TRIAL']]

### name
- **Type**: typing.Optional[str]

### networkAccessControl
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.NetworkAccessConfigurationOutputTypeDef]

### notificationDestinations
- **Type**: typing.Optional[typing.List[typing.Literal['SNS']]]

### organizationRoleName
- **Type**: typing.Optional[str]

### organizationalUnits
- **Type**: typing.Optional[typing.List[str]]

### permissionType
- **Type**: typing.Optional[typing.Literal['CUSTOMER_MANAGED', 'SERVICE_MANAGED']]

### stackSetName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### vpcConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana_classes.VpcConfigurationOutputTypeDef]

### workspaceRoleArn
- **Type**: typing.Optional[str]


# WorkspaceSummaryTypeDef

### authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana_classes.AuthenticationSummaryTypeDef'>
- **Required**: Yes

### created
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### endpoint
- **Type**: <class 'str'>
- **Required**: Yes

### grafanaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### id
- **Type**: <class 'str'>
- **Required**: Yes

### modified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### status
- **Type**: typing.Literal['ACTIVE', 'CREATING', 'CREATION_FAILED', 'DELETING', 'DELETION_FAILED', 'FAILED', 'LICENSE_REMOVAL_FAILED', 'UPDATE_FAILED', 'UPDATING', 'UPGRADE_FAILED', 'UPGRADING', 'VERSION_UPDATE_FAILED', 'VERSION_UPDATING']
- **Required**: Yes

### description
- **Type**: typing.Optional[str]

### grafanaToken
- **Type**: typing.Optional[str]

### licenseType
- **Type**: typing.Optional[typing.Literal['ENTERPRISE', 'ENTERPRISE_FREE_TRIAL']]

### name
- **Type**: typing.Optional[str]

### notificationDestinations
- **Type**: typing.Optional[typing.List[typing.Literal['SNS']]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


