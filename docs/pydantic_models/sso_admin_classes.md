# Sso Admin Classes

# AccessControlAttributeOutputTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.AccessControlAttributeValueOutputTypeDef'>
- **Required**: Yes


# AccessControlAttributeTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.AccessControlAttributeValueTypeDef'>
- **Required**: Yes


# AccessControlAttributeValueOutputTypeDef

### Source
- **Type**: typing.List[str]
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


# AttachCustomerManagedPolicyReferenceToPermissionSetRequestTypeDef

### CustomerManagedPolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.CustomerManagedPolicyReferenceTypeDef'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachManagedPolicyToPermissionSetRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.AuthenticationMethodOutputTypeDef]

### AuthenticationMethodType
- **Type**: typing.Optional[typing.Literal['IAM']]


# AuthenticationMethodOutputTypeDef

### Iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.IamAuthenticationMethodOutputTypeDef]


# AuthenticationMethodTypeDef

### Iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.IamAuthenticationMethodTypeDef]


# AuthenticationMethodUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AuthorizationCodeGrantOutputTypeDef

### RedirectUris
- **Type**: typing.Optional[typing.List[str]]


# AuthorizationCodeGrantTypeDef

### RedirectUris
- **Type**: typing.Optional[typing.Sequence[str]]


# AuthorizedTokenIssuerOutputTypeDef

### AuthorizedAudiences
- **Type**: typing.Optional[typing.List[str]]

### TrustedTokenIssuerArn
- **Type**: typing.Optional[str]


# AuthorizedTokenIssuerTypeDef

### AuthorizedAudiences
- **Type**: typing.Optional[typing.Sequence[str]]

### TrustedTokenIssuerArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccountAssignmentRequestTypeDef

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


# CreateApplicationAssignmentRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# CreateApplicationRequestTypeDef

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


# CreateInstanceAccessControlAttributeConfigurationRequestTypeDef

### InstanceAccessControlAttributeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.InstanceAccessControlAttributeConfigurationUnionTypeDef'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateInstanceRequestTypeDef

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


# CreatePermissionSetRequestTypeDef

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


# CreateTrustedTokenIssuerRequestTypeDef

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


# DeleteAccountAssignmentRequestTypeDef

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


# DeleteApplicationAccessScopeRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationAssignmentRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# DeleteApplicationAuthenticationMethodRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMethodType
- **Type**: typing.Literal['IAM']
- **Required**: Yes


# DeleteApplicationGrantRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### GrantType
- **Type**: typing.Literal['authorization_code', 'refresh_token', 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'urn:ietf:params:oauth:grant-type:token-exchange']
- **Required**: Yes


# DeleteApplicationRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInlinePolicyFromPermissionSetRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceAccessControlAttributeConfigurationRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePermissionSetRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePermissionsBoundaryFromPermissionSetRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrustedTokenIssuerRequestTypeDef

### TrustedTokenIssuerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountAssignmentCreationStatusRequestTypeDef

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


# DescribeAccountAssignmentDeletionStatusRequestTypeDef

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


# DescribeApplicationAssignmentRequestTypeDef

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


# DescribeApplicationProviderRequestTypeDef

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


# DescribeApplicationRequestTypeDef

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


# DescribeInstanceAccessControlAttributeConfigurationRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInstanceAccessControlAttributeConfigurationResponseTypeDef

### InstanceAccessControlAttributeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.InstanceAccessControlAttributeConfigurationOutputTypeDef'>
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


# DescribeInstanceRequestTypeDef

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


# DescribePermissionSetProvisioningStatusRequestTypeDef

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


# DescribePermissionSetRequestTypeDef

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


# DescribeTrustedTokenIssuerRequestTypeDef

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


# DetachCustomerManagedPolicyReferenceFromPermissionSetRequestTypeDef

### CustomerManagedPolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.CustomerManagedPolicyReferenceTypeDef'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachManagedPolicyFromPermissionSetRequestTypeDef

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


# GetApplicationAccessScopeRequestTypeDef

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


# GetApplicationAssignmentConfigurationRequestTypeDef

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


# GetApplicationAuthenticationMethodRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMethodType
- **Type**: typing.Literal['IAM']
- **Required**: Yes


# GetApplicationAuthenticationMethodResponseTypeDef

### AuthenticationMethod
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.AuthenticationMethodOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetApplicationGrantRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### GrantType
- **Type**: typing.Literal['authorization_code', 'refresh_token', 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'urn:ietf:params:oauth:grant-type:token-exchange']
- **Required**: Yes


# GetApplicationGrantResponseTypeDef

### Grant
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.GrantOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInlinePolicyForPermissionSetRequestTypeDef

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


# GetPermissionsBoundaryForPermissionSetRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.GrantOutputTypeDef'>
- **Required**: Yes

### GrantType
- **Type**: typing.Literal['authorization_code', 'refresh_token', 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'urn:ietf:params:oauth:grant-type:token-exchange']
- **Required**: Yes


# GrantOutputTypeDef

### AuthorizationCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.AuthorizationCodeGrantOutputTypeDef]

### JwtBearer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.JwtBearerGrantOutputTypeDef]

### RefreshToken
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### TokenExchange
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# GrantTypeDef

### AuthorizationCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.AuthorizationCodeGrantTypeDef]

### JwtBearer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.JwtBearerGrantTypeDef]

### RefreshToken
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]

### TokenExchange
- **Type**: typing.Optional[typing.Mapping[str, typing.Any]]


# GrantUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IamAuthenticationMethodOutputTypeDef

### ActorPolicy
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# IamAuthenticationMethodTypeDef

### ActorPolicy
- **Type**: typing.Mapping[str, typing.Any]
- **Required**: Yes


# InstanceAccessControlAttributeConfigurationOutputTypeDef

### AccessControlAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.AccessControlAttributeOutputTypeDef]
- **Required**: Yes


# InstanceAccessControlAttributeConfigurationTypeDef

### AccessControlAttributes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.sso_admin_classes.AccessControlAttributeTypeDef]
- **Required**: Yes


# InstanceAccessControlAttributeConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# JwtBearerGrantOutputTypeDef

### AuthorizedTokenIssuers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.AuthorizedTokenIssuerOutputTypeDef]]


# JwtBearerGrantTypeDef

### AuthorizedTokenIssuers
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.sso_admin_classes.AuthorizedTokenIssuerTypeDef]]


# ListAccountAssignmentCreationStatusRequestPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.OperationStatusFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListAccountAssignmentCreationStatusRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssignmentDeletionStatusRequestPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.OperationStatusFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListAccountAssignmentDeletionStatusRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssignmentsFilterTypeDef

### AccountId
- **Type**: typing.Optional[str]


# ListAccountAssignmentsForPrincipalRequestPaginateTypeDef

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


# ListAccountAssignmentsForPrincipalRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssignmentsRequestPaginateTypeDef

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


# ListAccountAssignmentsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccountsForProvisionedPermissionSetRequestPaginateTypeDef

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


# ListAccountsForProvisionedPermissionSetRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAccessScopesRequestPaginateTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListApplicationAccessScopesRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAccessScopesResponseTypeDef

### Scopes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.ScopeDetailsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAssignmentsFilterTypeDef

### ApplicationArn
- **Type**: typing.Optional[str]


# ListApplicationAssignmentsForPrincipalRequestPaginateTypeDef

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


# ListApplicationAssignmentsForPrincipalRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAssignmentsRequestPaginateTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListApplicationAssignmentsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAuthenticationMethodsRequestPaginateTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListApplicationAuthenticationMethodsRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAuthenticationMethodsResponseTypeDef

### AuthenticationMethods
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.AuthenticationMethodItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationGrantsRequestPaginateTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListApplicationGrantsRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationGrantsResponseTypeDef

### Grants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.GrantItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationProvidersRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListApplicationProvidersRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationProvidersResponseTypeDef

### ApplicationProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.ApplicationProviderTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsFilterTypeDef

### ApplicationAccount
- **Type**: typing.Optional[str]

### ApplicationProvider
- **Type**: typing.Optional[str]


# ListApplicationsRequestPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.ListApplicationsFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListApplicationsRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomerManagedPolicyReferencesInPermissionSetRequestPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListCustomerManagedPolicyReferencesInPermissionSetRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInstancesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListInstancesRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInstancesResponseTypeDef

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.InstanceMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListManagedPoliciesInPermissionSetRequestPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListManagedPoliciesInPermissionSetRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionSetProvisioningStatusRequestPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.OperationStatusFilterTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListPermissionSetProvisioningStatusRequestTypeDef

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

### PermissionSetsProvisioningStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.PermissionSetProvisioningStatusMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionSetsProvisionedToAccountRequestPaginateTypeDef

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


# ListPermissionSetsProvisionedToAccountRequestTypeDef

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

### PermissionSets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionSetsRequestPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListPermissionSetsRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionSetsResponseTypeDef

### PermissionSets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrustedTokenIssuersRequestPaginateTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.PaginatorConfigTypeDef]


# ListTrustedTokenIssuersRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTrustedTokenIssuersResponseTypeDef

### TrustedTokenIssuers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin_classes.TrustedTokenIssuerMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


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


# ProvisionPermissionSetRequestTypeDef

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


# PutApplicationAccessScopeRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizedTargets
- **Type**: typing.Optional[typing.Sequence[str]]


# PutApplicationAssignmentConfigurationRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentRequired
- **Type**: <class 'bool'>
- **Required**: Yes


# PutApplicationAuthenticationMethodRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMethod
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.AuthenticationMethodUnionTypeDef'>
- **Required**: Yes

### AuthenticationMethodType
- **Type**: typing.Literal['IAM']
- **Required**: Yes


# PutApplicationGrantRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Grant
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.GrantUnionTypeDef'>
- **Required**: Yes

### GrantType
- **Type**: typing.Literal['authorization_code', 'refresh_token', 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'urn:ietf:params:oauth:grant-type:token-exchange']
- **Required**: Yes


# PutInlinePolicyToPermissionSetRequestTypeDef

### InlinePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutPermissionsBoundaryToPermissionSetRequestTypeDef

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


# TagResourceRequestTypeDef

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


# UntagResourceRequestTypeDef

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


# UpdateApplicationRequestTypeDef

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


# UpdateInstanceAccessControlAttributeConfigurationRequestTypeDef

### InstanceAccessControlAttributeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin_classes.InstanceAccessControlAttributeConfigurationUnionTypeDef'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateInstanceRequestTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePermissionSetRequestTypeDef

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


# UpdateTrustedTokenIssuerRequestTypeDef

### TrustedTokenIssuerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### TrustedTokenIssuerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin_classes.TrustedTokenIssuerUpdateConfigurationTypeDef]


