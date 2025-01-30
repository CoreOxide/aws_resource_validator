# sso_admin_classes

# AccessControlAttributeTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.AccessControlAttributeValueTypeDef'>
- **Required**: Yes


# AccessControlAttributeValueTypeDef

### Source
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AccountAssignmentForPrincipalTypeDef

### AccountId
- **Type**: typing.Optional[str]

### PermissionSetArn
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### PrincipalType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]


# AccountAssignmentOperationStatusMetadataTypeDef

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### RequestId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]


# AccountAssignmentOperationStatusTypeDef

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### PermissionSetArn
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### PrincipalType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]

### RequestId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]

### TargetId
- **Type**: typing.Optional[str]

### TargetType
- **Type**: typing.Optional[typing.Literal['AWS_ACCOUNT']]


# AccountAssignmentTypeDef

### AccountId
- **Type**: typing.Optional[str]

### PermissionSetArn
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### PrincipalType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]


# ApplicationAssignmentForPrincipalTypeDef

### ApplicationArn
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### PrincipalType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]


# ApplicationAssignmentTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# ApplicationProviderTypeDef

### ApplicationProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayData
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.DisplayDataTypeDef]

### FederationProtocol
- **Type**: typing.Optional[typing.Literal['OAUTH', 'SAML']]

### ResourceServerConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.ResourceServerConfigTypeDef]


# ApplicationTypeDef

### ApplicationAccount
- **Type**: typing.Optional[str]

### ApplicationArn
- **Type**: typing.Optional[str]

### ApplicationProviderArn
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### InstanceArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PortalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PortalOptionsTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# AttachCustomerManagedPolicyReferenceToPermissionSetRequestRequestTypeDef

### CustomerManagedPolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.CustomerManagedPolicyReferenceTypeDef'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachManagedPolicyToPermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachedManagedPolicyTypeDef

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# AuthenticationMethodItemTypeDef

### AuthenticationMethod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.AuthenticationMethodTypeDef]

### AuthenticationMethodType
- **Type**: typing.Optional[typing.Literal['IAM']]


# AuthenticationMethodTypeDef

### Iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.IamAuthenticationMethodTypeDef]


# AuthorizationCodeGrantTypeDef

### RedirectUris
- **Type**: typing.Optional[typing.List[str]]


# AuthorizedTokenIssuerTypeDef

### AuthorizedAudiences
- **Type**: typing.Optional[typing.List[str]]

### TrustedTokenIssuerArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccountAssignmentRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetType
- **Type**: typing.Literal['AWS_ACCOUNT']
- **Required**: Yes


# CreateAccountAssignmentResponseTypeDef

### AccountAssignmentCreationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.AccountAssignmentOperationStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateApplicationAssignmentRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# CreateApplicationRequestRequestTypeDef

### ApplicationProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### PortalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PortalOptionsTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sso_admin_classes.TagTypeDef]]


# CreateApplicationResponseTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef

### InstanceAccessControlAttributeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.InstanceAccessControlAttributeConfigurationTypeDef'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateInstanceRequestRequestTypeDef

### ClientToken
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sso_admin_classes.TagTypeDef]]


# CreateInstanceResponseTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### RelayState
- **Type**: typing.Optional[str]

### SessionDuration
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sso_admin_classes.TagTypeDef]]


# CreatePermissionSetResponseTypeDef

### PermissionSet
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.PermissionSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrustedTokenIssuerRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TrustedTokenIssuerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.TrustedTokenIssuerConfigurationTypeDef'>
- **Required**: Yes

### TrustedTokenIssuerType
- **Type**: typing.Literal['OIDC_JWT']
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sso_admin_classes.TagTypeDef]]


# CreateTrustedTokenIssuerResponseTypeDef

### TrustedTokenIssuerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CustomerManagedPolicyReferenceTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]


# DeleteAccountAssignmentRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### TargetId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetType
- **Type**: typing.Literal['AWS_ACCOUNT']
- **Required**: Yes


# DeleteAccountAssignmentResponseTypeDef

### AccountAssignmentDeletionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.AccountAssignmentOperationStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteApplicationAccessScopeRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationAssignmentRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# DeleteApplicationAuthenticationMethodRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMethodType
- **Type**: typing.Literal['IAM']
- **Required**: Yes


# DeleteApplicationGrantRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### GrantType
- **Type**: typing.Literal['authorization_code', 'refresh_token', 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'urn:ietf:params:oauth:grant-type:token-exchange']
- **Required**: Yes


# DeleteApplicationRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInlinePolicyFromPermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceAccessControlAttributeConfigurationRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePermissionsBoundaryFromPermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrustedTokenIssuerRequestRequestTypeDef

### TrustedTokenIssuerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountAssignmentCreationStatusRequestRequestTypeDef

### AccountAssignmentCreationRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountAssignmentCreationStatusResponseTypeDef

### AccountAssignmentCreationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.AccountAssignmentOperationStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAccountAssignmentDeletionStatusRequestRequestTypeDef

### AccountAssignmentDeletionRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountAssignmentDeletionStatusResponseTypeDef

### AccountAssignmentDeletionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.AccountAssignmentOperationStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeApplicationAssignmentRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# DescribeApplicationAssignmentResponseTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeApplicationProviderRequestRequestTypeDef

### ApplicationProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationProviderResponseTypeDef

### ApplicationProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayData
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.DisplayDataTypeDef'>
- **Required**: Yes

### FederationProtocol
- **Type**: typing.Literal['OAUTH', 'SAML']
- **Required**: Yes

### ResourceServerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResourceServerConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeApplicationRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationResponseTypeDef

### ApplicationAccount
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PortalOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.PortalOptionsTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInstanceAccessControlAttributeConfigurationRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef

### InstanceAccessControlAttributeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.InstanceAccessControlAttributeConfigurationTypeDef'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'ENABLED']
- **Required**: Yes

### StatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInstanceRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInstanceResponseTypeDef

### CreatedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### IdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### OwnerAccountId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['ACTIVE', 'CREATE_IN_PROGRESS', 'DELETE_IN_PROGRESS']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePermissionSetProvisioningStatusRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionPermissionSetRequestId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePermissionSetProvisioningStatusResponseTypeDef

### PermissionSetProvisioningStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.PermissionSetProvisioningStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePermissionSetResponseTypeDef

### PermissionSet
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.PermissionSetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTrustedTokenIssuerRequestRequestTypeDef

### TrustedTokenIssuerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrustedTokenIssuerResponseTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TrustedTokenIssuerArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrustedTokenIssuerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.TrustedTokenIssuerConfigurationTypeDef'>
- **Required**: Yes

### TrustedTokenIssuerType
- **Type**: typing.Literal['OIDC_JWT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetachCustomerManagedPolicyReferenceFromPermissionSetRequestRequestTypeDef

### CustomerManagedPolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.CustomerManagedPolicyReferenceTypeDef'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachManagedPolicyFromPermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisplayDataTypeDef

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### IconUrl
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationAccessScopeRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationAccessScopeResponseTypeDef

### AuthorizedTargets
- **Type**: typing.List[str]
- **Required**: Yes

### Scope
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationAssignmentConfigurationRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationAssignmentConfigurationResponseTypeDef

### AssignmentRequired
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationAuthenticationMethodRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMethodType
- **Type**: typing.Literal['IAM']
- **Required**: Yes


# GetApplicationAuthenticationMethodResponseTypeDef

### AuthenticationMethod
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.AuthenticationMethodTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationGrantRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### GrantType
- **Type**: typing.Literal['authorization_code', 'refresh_token', 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'urn:ietf:params:oauth:grant-type:token-exchange']
- **Required**: Yes


# GetApplicationGrantResponseTypeDef

### Grant
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.GrantTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInlinePolicyForPermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetInlinePolicyForPermissionSetResponseTypeDef

### InlinePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPermissionsBoundaryForPermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPermissionsBoundaryForPermissionSetResponseTypeDef

### PermissionsBoundary
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.PermissionsBoundaryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GrantItemTypeDef

### Grant
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.GrantTypeDef'>
- **Required**: Yes

### GrantType
- **Type**: typing.Literal['authorization_code', 'refresh_token', 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'urn:ietf:params:oauth:grant-type:token-exchange']
- **Required**: Yes


# GrantTypeDef

### AuthorizationCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.AuthorizationCodeGrantTypeDef]

### JwtBearer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.JwtBearerGrantTypeDef]

### RefreshToken
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### TokenExchange
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# IamAuthenticationMethodTypeDef

### ActorPolicy
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# InstanceAccessControlAttributeConfigurationTypeDef

### AccessControlAttributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sso_admin_classes.AccessControlAttributeTypeDef]
- **Required**: Yes


# InstanceMetadataTypeDef

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### IdentityStoreId
- **Type**: typing.Optional[str]

### InstanceArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### OwnerAccountId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATE_IN_PROGRESS', 'DELETE_IN_PROGRESS']]


# JwtBearerGrantTypeDef

### AuthorizedTokenIssuers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.AuthorizedTokenIssuerTypeDef]]


# ListAccountAssignmentCreationStatusRequestListAccountAssignmentCreationStatusPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.OperationStatusFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListAccountAssignmentCreationStatusRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.OperationStatusFilterTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssignmentCreationStatusResponseTypeDef

### AccountAssignmentsCreationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.AccountAssignmentOperationStatusMetadataTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccountAssignmentDeletionStatusRequestListAccountAssignmentDeletionStatusPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.OperationStatusFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListAccountAssignmentDeletionStatusRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.OperationStatusFilterTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssignmentDeletionStatusResponseTypeDef

### AccountAssignmentsDeletionStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.AccountAssignmentOperationStatusMetadataTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccountAssignmentsFilterTypeDef

### AccountId
- **Type**: typing.Optional[str]


# ListAccountAssignmentsForPrincipalRequestListAccountAssignmentsForPrincipalPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.ListAccountAssignmentsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListAccountAssignmentsForPrincipalRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.ListAccountAssignmentsFilterTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssignmentsForPrincipalResponseTypeDef

### AccountAssignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.AccountAssignmentForPrincipalTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccountAssignmentsRequestListAccountAssignmentsPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListAccountAssignmentsRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssignmentsResponseTypeDef

### AccountAssignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.AccountAssignmentTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccountsForProvisionedPermissionSetRequestListAccountsForProvisionedPermissionSetPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningStatus
- **Type**: typing.Optional[typing.Literal['LATEST_PERMISSION_SET_NOT_PROVISIONED', 'LATEST_PERMISSION_SET_PROVISIONED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListAccountsForProvisionedPermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ProvisioningStatus
- **Type**: typing.Optional[typing.Literal['LATEST_PERMISSION_SET_NOT_PROVISIONED', 'LATEST_PERMISSION_SET_PROVISIONED']]


# ListAccountsForProvisionedPermissionSetResponseTypeDef

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationAccessScopesRequestListApplicationAccessScopesPaginateTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListApplicationAccessScopesRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAccessScopesResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Scopes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.ScopeDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationAssignmentsFilterTypeDef

### ApplicationArn
- **Type**: typing.Optional[str]


# ListApplicationAssignmentsForPrincipalRequestListApplicationAssignmentsForPrincipalPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.ListApplicationAssignmentsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListApplicationAssignmentsForPrincipalRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.ListApplicationAssignmentsFilterTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAssignmentsForPrincipalResponseTypeDef

### ApplicationAssignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.ApplicationAssignmentForPrincipalTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationAssignmentsRequestListApplicationAssignmentsPaginateTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListApplicationAssignmentsRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAssignmentsResponseTypeDef

### ApplicationAssignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.ApplicationAssignmentTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationAuthenticationMethodsRequestListApplicationAuthenticationMethodsPaginateTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListApplicationAuthenticationMethodsRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAuthenticationMethodsResponseTypeDef

### AuthenticationMethods
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.AuthenticationMethodItemTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationGrantsRequestListApplicationGrantsPaginateTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListApplicationGrantsRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationGrantsResponseTypeDef

### Grants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.GrantItemTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationProvidersRequestListApplicationProvidersPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListApplicationProvidersRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationProvidersResponseTypeDef

### ApplicationProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.ApplicationProviderTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListApplicationsFilterTypeDef

### ApplicationAccount
- **Type**: typing.Optional[str]

### ApplicationProvider
- **Type**: typing.Optional[str]


# ListApplicationsRequestListApplicationsPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.ListApplicationsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.ListApplicationsFilterTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsResponseTypeDef

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.ApplicationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCustomerManagedPolicyReferencesInPermissionSetRequestListCustomerManagedPolicyReferencesInPermissionSetPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListCustomerManagedPolicyReferencesInPermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListCustomerManagedPolicyReferencesInPermissionSetResponseTypeDef

### CustomerManagedPolicyReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.CustomerManagedPolicyReferenceTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInstancesRequestListInstancesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListInstancesRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInstancesResponseTypeDef

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.InstanceMetadataTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListManagedPoliciesInPermissionSetRequestListManagedPoliciesInPermissionSetPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListManagedPoliciesInPermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListManagedPoliciesInPermissionSetResponseTypeDef

### AttachedManagedPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.AttachedManagedPolicyTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPermissionSetProvisioningStatusRequestListPermissionSetProvisioningStatusPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.OperationStatusFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListPermissionSetProvisioningStatusRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.OperationStatusFilterTypeDef]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionSetProvisioningStatusResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetsProvisioningStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.PermissionSetProvisioningStatusMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPermissionSetsProvisionedToAccountRequestListPermissionSetsProvisionedToAccountPaginateTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningStatus
- **Type**: typing.Optional[typing.Literal['LATEST_PERMISSION_SET_NOT_PROVISIONED', 'LATEST_PERMISSION_SET_PROVISIONED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListPermissionSetsProvisionedToAccountRequestRequestTypeDef

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ProvisioningStatus
- **Type**: typing.Optional[typing.Literal['LATEST_PERMISSION_SET_NOT_PROVISIONED', 'LATEST_PERMISSION_SET_PROVISIONED']]


# ListPermissionSetsProvisionedToAccountResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPermissionSetsRequestListPermissionSetsPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListPermissionSetsRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionSetsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestListTagsForResourcePaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTrustedTokenIssuersRequestListTrustedTokenIssuersPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListTrustedTokenIssuersRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTrustedTokenIssuersResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### TrustedTokenIssuers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.TrustedTokenIssuerMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OidcJwtConfigurationTypeDef

### ClaimAttributePath
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityStoreAttributePath
- **Type**: <class 'str'>
- **Required**: Yes

### IssuerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### JwksRetrievalOption
- **Type**: typing.Literal['OPEN_ID_DISCOVERY']
- **Required**: Yes


# OidcJwtUpdateConfigurationTypeDef

### ClaimAttributePath
- **Type**: typing.Optional[str]

### IdentityStoreAttributePath
- **Type**: typing.Optional[str]

### JwksRetrievalOption
- **Type**: typing.Optional[typing.Literal['OPEN_ID_DISCOVERY']]


# OperationStatusFilterTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionSetProvisioningStatusMetadataTypeDef

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### RequestId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]


# PermissionSetProvisioningStatusTypeDef

### AccountId
- **Type**: typing.Optional[str]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### FailureReason
- **Type**: typing.Optional[str]

### PermissionSetArn
- **Type**: typing.Optional[str]

### RequestId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]


# PermissionSetTypeDef

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PermissionSetArn
- **Type**: typing.Optional[str]

### RelayState
- **Type**: typing.Optional[str]

### SessionDuration
- **Type**: typing.Optional[str]


# PermissionsBoundaryTypeDef

### CustomerManagedPolicyReference
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.CustomerManagedPolicyReferenceTypeDef]

### ManagedPolicyArn
- **Type**: typing.Optional[str]


# PortalOptionsTypeDef

### SignInOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.SignInOptionsTypeDef]

### Visibility
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ProvisionPermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### TargetType
- **Type**: typing.Literal['ALL_PROVISIONED_ACCOUNTS', 'AWS_ACCOUNT']
- **Required**: Yes

### TargetId
- **Type**: typing.Optional[str]


# ProvisionPermissionSetResponseTypeDef

### PermissionSetProvisioningStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.PermissionSetProvisioningStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutApplicationAccessScopeRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizedTargets
- **Type**: typing.Optional[typing.Sequence[str]]


# PutApplicationAssignmentConfigurationRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentRequired
- **Type**: <class 'bool'>
- **Required**: Yes


# PutApplicationAuthenticationMethodRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMethod
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.AuthenticationMethodTypeDef'>
- **Required**: Yes

### AuthenticationMethodType
- **Type**: typing.Literal['IAM']
- **Required**: Yes


# PutApplicationGrantRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Grant
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.GrantTypeDef'>
- **Required**: Yes

### GrantType
- **Type**: typing.Literal['authorization_code', 'refresh_token', 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'urn:ietf:params:oauth:grant-type:token-exchange']
- **Required**: Yes


# PutInlinePolicyToPermissionSetRequestRequestTypeDef

### InlinePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutPermissionsBoundaryToPermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionsBoundary
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.PermissionsBoundaryTypeDef'>
- **Required**: Yes


# ResourceServerConfigTypeDef

### Scopes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sso_admin_classes.ResourceServerScopeDetailsTypeDef]]


# ResourceServerScopeDetailsTypeDef

### DetailedTitle
- **Type**: typing.Optional[str]

### LongDescription
- **Type**: typing.Optional[str]


# ResponseMetadataTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### HostId
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


# ScopeDetailsTypeDef

### Scope
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizedTargets
- **Type**: typing.Optional[typing.List[str]]


# SignInOptionsTypeDef

### Origin
- **Type**: typing.Literal['APPLICATION', 'IDENTITY_CENTER']
- **Required**: Yes

### ApplicationUrl
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sso_admin_classes.TagTypeDef]
- **Required**: Yes

### InstanceArn
- **Type**: typing.Optional[str]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TrustedTokenIssuerConfigurationTypeDef

### OidcJwtConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.OidcJwtConfigurationTypeDef]


# TrustedTokenIssuerMetadataTypeDef

### Name
- **Type**: typing.Optional[str]

### TrustedTokenIssuerArn
- **Type**: typing.Optional[str]

### TrustedTokenIssuerType
- **Type**: typing.Optional[typing.Literal['OIDC_JWT']]


# TrustedTokenIssuerUpdateConfigurationTypeDef

### OidcJwtConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.OidcJwtUpdateConfigurationTypeDef]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes

### InstanceArn
- **Type**: typing.Optional[str]


# UpdateApplicationPortalOptionsTypeDef

### SignInOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.SignInOptionsTypeDef]


# UpdateApplicationRequestRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PortalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.UpdateApplicationPortalOptionsTypeDef]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateInstanceAccessControlAttributeConfigurationRequestRequestTypeDef

### InstanceAccessControlAttributeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.InstanceAccessControlAttributeConfigurationTypeDef'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateInstanceRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePermissionSetRequestRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### RelayState
- **Type**: typing.Optional[str]

### SessionDuration
- **Type**: typing.Optional[str]


# UpdateTrustedTokenIssuerRequestRequestTypeDef

### TrustedTokenIssuerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### TrustedTokenIssuerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.TrustedTokenIssuerUpdateConfigurationTypeDef]


