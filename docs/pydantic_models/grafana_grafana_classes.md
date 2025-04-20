# Grafana Grafana Classes

# AssertionAttributes

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


# AssociateLicenseRequest

### licenseType
- **Type**: typing.Literal['ENTERPRISE', 'ENTERPRISE_FREE_TRIAL']
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### grafanaToken
- **Type**: typing.Optional[str]


# AssociateLicenseResponse

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.WorkspaceDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# AuthenticationDescription

### providers
- **Type**: typing.List[typing.Literal['AWS_SSO', 'SAML']]
- **Required**: Yes

### awsSso
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.AwsSsoAuthentication]

### saml
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.SamlAuthentication]


# AuthenticationSummary

### providers
- **Type**: typing.List[typing.Literal['AWS_SSO', 'SAML']]
- **Required**: Yes

### samlConfigurationStatus
- **Type**: typing.Optional[typing.Literal['CONFIGURED', 'NOT_CONFIGURED']]


# AwsSsoAuthentication

### ssoClientId
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateWorkspaceApiKeyRequest

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


# CreateWorkspaceApiKeyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkspaceRequest

### accountAccessType
- **Type**: typing.Literal['CURRENT_ACCOUNT', 'ORGANIZATION']
- **Required**: Yes

### authenticationProviders
- **Type**: typing.List[typing.Literal['AWS_SSO', 'SAML']]
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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.grafana.grafana_classes.NetworkAccessConfiguration, aws_resource_validator.pydantic_models.grafana.grafana_classes.NetworkAccessConfigurationOutput, NoneType]

### organizationRoleName
- **Type**: typing.Optional[str]

### stackSetName
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### vpcConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.grafana.grafana_classes.VpcConfiguration, aws_resource_validator.pydantic_models.grafana.grafana_classes.VpcConfigurationOutput, NoneType]

### workspaceDataSources
- **Type**: typing.Optional[typing.List[typing.Literal['AMAZON_OPENSEARCH_SERVICE', 'ATHENA', 'CLOUDWATCH', 'PROMETHEUS', 'REDSHIFT', 'SITEWISE', 'TIMESTREAM', 'TWINMAKER', 'XRAY']]]

### workspaceDescription
- **Type**: typing.Optional[str]

### workspaceName
- **Type**: typing.Optional[str]

### workspaceNotificationDestinations
- **Type**: typing.Optional[typing.List[typing.Literal['SNS']]]

### workspaceOrganizationalUnits
- **Type**: typing.Optional[typing.List[str]]

### workspaceRoleArn
- **Type**: typing.Optional[str]


# CreateWorkspaceResponse

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.WorkspaceDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkspaceServiceAccountRequest

### grafanaRole
- **Type**: typing.Literal['ADMIN', 'EDITOR', 'VIEWER']
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateWorkspaceServiceAccountResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# CreateWorkspaceServiceAccountTokenRequest

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


# CreateWorkspaceServiceAccountTokenResponse

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceAccountToken
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ServiceAccountTokenSummaryWithKey'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWorkspaceApiKeyRequest

### keyName
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkspaceApiKeyResponse

### keyName
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWorkspaceRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkspaceResponse

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.WorkspaceDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWorkspaceServiceAccountRequest

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkspaceServiceAccountResponse

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteWorkspaceServiceAccountTokenRequest

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### tokenId
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteWorkspaceServiceAccountTokenResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorkspaceAuthenticationRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkspaceAuthenticationResponse

### authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.AuthenticationDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorkspaceConfigurationRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkspaceConfigurationResponse

### configuration
- **Type**: <class 'str'>
- **Required**: Yes

### grafanaVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorkspaceRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkspaceResponse

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.WorkspaceDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateLicenseRequest

### licenseType
- **Type**: typing.Literal['ENTERPRISE', 'ENTERPRISE_FREE_TRIAL']
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateLicenseResponse

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.WorkspaceDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# IdpMetadata

### url
- **Type**: typing.Optional[str]

### xml
- **Type**: typing.Optional[str]


# ListPermissionsRequest

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


# ListPermissionsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.PaginatorConfig]


# ListPermissionsResponse

### permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana.grafana_classes.PermissionEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# ListVersionsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]

### workspaceId
- **Type**: typing.Optional[str]


# ListVersionsRequestPaginate

### workspaceId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.PaginatorConfig]


# ListVersionsResponse

### grafanaVersions
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspaceServiceAccountTokensRequest

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


# ListWorkspaceServiceAccountTokensRequestPaginate

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.PaginatorConfig]


# ListWorkspaceServiceAccountTokensResponse

### serviceAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### serviceAccountTokens
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana.grafana_classes.ServiceAccountTokenSummary]
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspaceServiceAccountsRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspaceServiceAccountsRequestPaginate

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.PaginatorConfig]


# ListWorkspaceServiceAccountsResponse

### serviceAccounts
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana.grafana_classes.ServiceAccountSummary]
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspacesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListWorkspacesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.PaginatorConfig]


# ListWorkspacesResponse

### workspaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana.grafana_classes.WorkspaceSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# NetworkAccessConfiguration

### prefixListIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpceIds
- **Type**: typing.List[str]
- **Required**: Yes


# NetworkAccessConfigurationOutput

### prefixListIds
- **Type**: typing.List[str]
- **Required**: Yes

### vpceIds
- **Type**: typing.List[str]
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionEntry

### role
- **Type**: typing.Literal['ADMIN', 'EDITOR', 'VIEWER']
- **Required**: Yes

### user
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.User'>
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


# RoleValues

### admin
- **Type**: typing.Optional[typing.List[str]]

### editor
- **Type**: typing.Optional[typing.List[str]]


# RoleValuesOutput

### admin
- **Type**: typing.Optional[typing.List[str]]

### editor
- **Type**: typing.Optional[typing.List[str]]


# SamlAuthentication

### status
- **Type**: typing.Literal['CONFIGURED', 'NOT_CONFIGURED']
- **Required**: Yes

### configuration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.SamlConfigurationOutput]


# SamlConfiguration

### idpMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.IdpMetadata'>
- **Required**: Yes

### allowedOrganizations
- **Type**: typing.Optional[typing.List[str]]

### assertionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.AssertionAttributes]

### loginValidityDuration
- **Type**: typing.Optional[int]

### roleValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.RoleValues]


# SamlConfigurationOutput

### idpMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.IdpMetadata'>
- **Required**: Yes

### allowedOrganizations
- **Type**: typing.Optional[typing.List[str]]

### assertionAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.AssertionAttributes]

### loginValidityDuration
- **Type**: typing.Optional[int]

### roleValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.RoleValuesOutput]


# ServiceAccountSummary

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


# ServiceAccountTokenSummary

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


# ServiceAccountTokenSummaryWithKey

### id
- **Type**: <class 'str'>
- **Required**: Yes

### key
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateError

### causedBy
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.UpdateInstructionOutput'>
- **Required**: Yes

### code
- **Type**: <class 'int'>
- **Required**: Yes

### message
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateInstruction

### action
- **Type**: typing.Literal['ADD', 'REVOKE']
- **Required**: Yes

### role
- **Type**: typing.Literal['ADMIN', 'EDITOR', 'VIEWER']
- **Required**: Yes

### users
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana.grafana_classes.User]
- **Required**: Yes


# UpdateInstructionOutput

### action
- **Type**: typing.Literal['ADD', 'REVOKE']
- **Required**: Yes

### role
- **Type**: typing.Literal['ADMIN', 'EDITOR', 'VIEWER']
- **Required**: Yes

### users
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana.grafana_classes.User]
- **Required**: Yes


# UpdatePermissionsRequest

### updateInstructionBatch
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.grafana.grafana_classes.UpdateInstruction, aws_resource_validator.pydantic_models.grafana.grafana_classes.UpdateInstructionOutput]]
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePermissionsResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.grafana.grafana_classes.UpdateError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkspaceAuthenticationRequest

### authenticationProviders
- **Type**: typing.List[typing.Literal['AWS_SSO', 'SAML']]
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### samlConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.grafana.grafana_classes.SamlConfiguration, aws_resource_validator.pydantic_models.grafana.grafana_classes.SamlConfigurationOutput, NoneType]


# UpdateWorkspaceAuthenticationResponse

### authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.AuthenticationDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateWorkspaceConfigurationRequest

### configuration
- **Type**: <class 'str'>
- **Required**: Yes

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### grafanaVersion
- **Type**: typing.Optional[str]


# UpdateWorkspaceRequest

### workspaceId
- **Type**: <class 'str'>
- **Required**: Yes

### accountAccessType
- **Type**: typing.Optional[typing.Literal['CURRENT_ACCOUNT', 'ORGANIZATION']]

### networkAccessControl
- **Type**: typing.Union[aws_resource_validator.pydantic_models.grafana.grafana_classes.NetworkAccessConfiguration, aws_resource_validator.pydantic_models.grafana.grafana_classes.NetworkAccessConfigurationOutput, NoneType]

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.grafana.grafana_classes.VpcConfiguration, aws_resource_validator.pydantic_models.grafana.grafana_classes.VpcConfigurationOutput, NoneType]

### workspaceDataSources
- **Type**: typing.Optional[typing.List[typing.Literal['AMAZON_OPENSEARCH_SERVICE', 'ATHENA', 'CLOUDWATCH', 'PROMETHEUS', 'REDSHIFT', 'SITEWISE', 'TIMESTREAM', 'TWINMAKER', 'XRAY']]]

### workspaceDescription
- **Type**: typing.Optional[str]

### workspaceName
- **Type**: typing.Optional[str]

### workspaceNotificationDestinations
- **Type**: typing.Optional[typing.List[typing.Literal['SNS']]]

### workspaceOrganizationalUnits
- **Type**: typing.Optional[typing.List[str]]

### workspaceRoleArn
- **Type**: typing.Optional[str]


# UpdateWorkspaceResponse

### workspace
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.WorkspaceDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.ResponseMetadata'>
- **Required**: Yes


# User

### id
- **Type**: <class 'str'>
- **Required**: Yes

### type
- **Type**: typing.Literal['SSO_GROUP', 'SSO_USER']
- **Required**: Yes


# VpcConfiguration

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes


# VpcConfigurationOutput

### securityGroupIds
- **Type**: typing.List[str]
- **Required**: Yes

### subnetIds
- **Type**: typing.List[str]
- **Required**: Yes


# WorkspaceDescription

### authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.AuthenticationSummary'>
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.NetworkAccessConfigurationOutput]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.grafana.grafana_classes.VpcConfigurationOutput]

### workspaceRoleArn
- **Type**: typing.Optional[str]


# WorkspaceSummary

### authentication
- **Type**: <class 'aws_resource_validator.pydantic_models.grafana.grafana_classes.AuthenticationSummary'>
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


