# Sso Admin Classes

# AccessControlAttribute

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AccessControlAttributeValue'>
- **Required**: Yes


# AccessControlAttributeOutput

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AccessControlAttributeValueOutput'>
- **Required**: Yes


# AccessControlAttributeValue

### Source
- **Type**: typing.List[str]
- **Required**: Yes


# AccessControlAttributeValueOutput

### Source
- **Type**: typing.List[str]
- **Required**: Yes


# AccountAssignment

### AccountId
- **Type**: typing.Optional[str]

### PermissionSetArn
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### PrincipalType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]


# AccountAssignmentForPrincipal

### AccountId
- **Type**: typing.Optional[str]

### PermissionSetArn
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### PrincipalType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]


# AccountAssignmentOperationStatus

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


# AccountAssignmentOperationStatusMetadata

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### RequestId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]


# Application

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
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ApplicationAssignment

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# ApplicationAssignmentForPrincipal

### ApplicationArn
- **Type**: typing.Optional[str]

### PrincipalId
- **Type**: typing.Optional[str]

### PrincipalType
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]


# ApplicationProvider

### ApplicationProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayData
- **Type**: <class 'NoneType'>

### FederationProtocol
- **Type**: typing.Optional[typing.Literal['OAUTH', 'SAML']]

### ResourceServerConfig
- **Type**: <class 'NoneType'>


# AttachCustomerManagedPolicyReferenceToPermissionSetRequest

### CustomerManagedPolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.CustomerManagedPolicyReference'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachManagedPolicyToPermissionSetRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachedManagedPolicy

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# AuthenticationMethod

### Iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.IamAuthenticationMethod]


# AuthenticationMethodItem

### AuthenticationMethod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AuthenticationMethodOutput]

### AuthenticationMethodType
- **Type**: typing.Optional[typing.Literal['IAM']]


# AuthenticationMethodOutput

### Iam
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.IamAuthenticationMethodOutput]


# AuthorizationCodeGrant

### RedirectUris
- **Type**: typing.Optional[typing.List[str]]


# AuthorizationCodeGrantOutput

### RedirectUris
- **Type**: typing.Optional[typing.List[str]]


# AuthorizedTokenIssuer

### AuthorizedAudiences
- **Type**: typing.Optional[typing.List[str]]

### TrustedTokenIssuerArn
- **Type**: typing.Optional[str]


# AuthorizedTokenIssuerOutput

### AuthorizedAudiences
- **Type**: typing.Optional[typing.List[str]]

### TrustedTokenIssuerArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccountAssignmentRequest

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


# CreateAccountAssignmentResponse

### AccountAssignmentCreationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AccountAssignmentOperationStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# CreateApplicationAssignmentRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# CreateApplicationRequest

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
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.Tag]]


# CreateApplicationResponse

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInstanceAccessControlAttributeConfigurationRequest

### InstanceAccessControlAttributeConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.InstanceAccessControlAttributeConfiguration, aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.InstanceAccessControlAttributeConfigurationOutput]
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# CreateInstanceRequest

### ClientToken
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.Tag]]


# CreateInstanceResponse

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePermissionSetRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.Tag]]


# CreatePermissionSetResponse

### PermissionSet
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PermissionSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrustedTokenIssuerRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TrustedTokenIssuerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.TrustedTokenIssuerConfiguration'>
- **Required**: Yes

### TrustedTokenIssuerType
- **Type**: typing.Literal['OIDC_JWT']
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.Tag]]


# CreateTrustedTokenIssuerResponse

### TrustedTokenIssuerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# CustomerManagedPolicyReference

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]


# DeleteAccountAssignmentRequest

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


# DeleteAccountAssignmentResponse

### AccountAssignmentDeletionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AccountAssignmentOperationStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteApplicationAccessScopeRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteApplicationAssignmentRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# DeleteApplicationAuthenticationMethodRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMethodType
- **Type**: typing.Literal['IAM']
- **Required**: Yes


# DeleteApplicationGrantRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### GrantType
- **Type**: typing.Literal['authorization_code', 'refresh_token', 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'urn:ietf:params:oauth:grant-type:token-exchange']
- **Required**: Yes


# DeleteApplicationRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInlinePolicyFromPermissionSetRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceAccessControlAttributeConfigurationRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePermissionSetRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePermissionsBoundaryFromPermissionSetRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTrustedTokenIssuerRequest

### TrustedTokenIssuerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountAssignmentCreationStatusRequest

### AccountAssignmentCreationRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountAssignmentCreationStatusResponse

### AccountAssignmentCreationStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AccountAssignmentOperationStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAccountAssignmentDeletionStatusRequest

### AccountAssignmentDeletionRequestId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAccountAssignmentDeletionStatusResponse

### AccountAssignmentDeletionStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AccountAssignmentOperationStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeApplicationAssignmentRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalId
- **Type**: <class 'str'>
- **Required**: Yes

### PrincipalType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# DescribeApplicationAssignmentResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeApplicationProviderRequest

### ApplicationProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationProviderResponse

### ApplicationProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayData
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.DisplayData'>
- **Required**: Yes

### FederationProtocol
- **Type**: typing.Literal['OAUTH', 'SAML']
- **Required**: Yes

### ResourceServerConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResourceServerConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeApplicationRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeApplicationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PortalOptions'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInstanceAccessControlAttributeConfigurationRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInstanceAccessControlAttributeConfigurationResponse

### InstanceAccessControlAttributeConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.InstanceAccessControlAttributeConfigurationOutput'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CREATION_FAILED', 'CREATION_IN_PROGRESS', 'ENABLED']
- **Required**: Yes

### StatusReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInstanceRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInstanceResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePermissionSetProvisioningStatusRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisionPermissionSetRequestId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePermissionSetProvisioningStatusResponse

### PermissionSetProvisioningStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PermissionSetProvisioningStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePermissionSetRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePermissionSetResponse

### PermissionSet
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PermissionSet'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTrustedTokenIssuerRequest

### TrustedTokenIssuerArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTrustedTokenIssuerResponse

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### TrustedTokenIssuerArn
- **Type**: <class 'str'>
- **Required**: Yes

### TrustedTokenIssuerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.TrustedTokenIssuerConfiguration'>
- **Required**: Yes

### TrustedTokenIssuerType
- **Type**: typing.Literal['OIDC_JWT']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# DetachCustomerManagedPolicyReferenceFromPermissionSetRequest

### CustomerManagedPolicyReference
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.CustomerManagedPolicyReference'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachManagedPolicyFromPermissionSetRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ManagedPolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisplayData

### Description
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### IconUrl
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# GetApplicationAccessScopeRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationAccessScopeResponse

### AuthorizedTargets
- **Type**: typing.List[str]
- **Required**: Yes

### Scope
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# GetApplicationAssignmentConfigurationRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetApplicationAssignmentConfigurationResponse

### AssignmentRequired
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# GetApplicationAuthenticationMethodRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMethodType
- **Type**: typing.Literal['IAM']
- **Required**: Yes


# GetApplicationAuthenticationMethodResponse

### AuthenticationMethod
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AuthenticationMethodOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# GetApplicationGrantRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### GrantType
- **Type**: typing.Literal['authorization_code', 'refresh_token', 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'urn:ietf:params:oauth:grant-type:token-exchange']
- **Required**: Yes


# GetApplicationGrantResponse

### Grant
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.GrantOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# GetInlinePolicyForPermissionSetRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetInlinePolicyForPermissionSetResponse

### InlinePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# GetPermissionsBoundaryForPermissionSetRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPermissionsBoundaryForPermissionSetResponse

### PermissionsBoundary
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PermissionsBoundary'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# Grant

### AuthorizationCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AuthorizationCodeGrant]

### JwtBearer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.JwtBearerGrant]

### RefreshToken
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### TokenExchange
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# GrantItem

### Grant
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.GrantOutput'>
- **Required**: Yes

### GrantType
- **Type**: typing.Literal['authorization_code', 'refresh_token', 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'urn:ietf:params:oauth:grant-type:token-exchange']
- **Required**: Yes


# GrantOutput

### AuthorizationCode
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AuthorizationCodeGrantOutput]

### JwtBearer
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.JwtBearerGrantOutput]

### RefreshToken
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### TokenExchange
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]


# IamAuthenticationMethod

### ActorPolicy
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# IamAuthenticationMethodOutput

### ActorPolicy
- **Type**: typing.Dict[str, typing.Any]
- **Required**: Yes


# InstanceAccessControlAttributeConfiguration

### AccessControlAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AccessControlAttribute]
- **Required**: Yes


# InstanceAccessControlAttributeConfigurationOutput

### AccessControlAttributes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AccessControlAttributeOutput]
- **Required**: Yes


# InstanceMetadata

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


# JwtBearerGrant

### AuthorizedTokenIssuers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AuthorizedTokenIssuer]]


# JwtBearerGrantOutput

### AuthorizedTokenIssuers
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AuthorizedTokenIssuerOutput]]


# ListAccountAssignmentCreationStatusRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.OperationStatusFilter]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssignmentCreationStatusRequestPaginate

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.OperationStatusFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListAccountAssignmentCreationStatusResponse

### AccountAssignmentsCreationStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AccountAssignmentOperationStatusMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssignmentDeletionStatusRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.OperationStatusFilter]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssignmentDeletionStatusRequestPaginate

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.OperationStatusFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListAccountAssignmentDeletionStatusResponse

### AccountAssignmentsDeletionStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AccountAssignmentOperationStatusMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssignmentsFilter

### AccountId
- **Type**: typing.Optional[str]


# ListAccountAssignmentsForPrincipalRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ListAccountAssignmentsFilter]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssignmentsForPrincipalRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ListAccountAssignmentsFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListAccountAssignmentsForPrincipalResponse

### AccountAssignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AccountAssignmentForPrincipal]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccountAssignmentsRequest

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


# ListAccountAssignmentsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListAccountAssignmentsResponse

### AccountAssignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AccountAssignment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAccountsForProvisionedPermissionSetRequest

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


# ListAccountsForProvisionedPermissionSetRequestPaginate

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningStatus
- **Type**: typing.Optional[typing.Literal['LATEST_PERMISSION_SET_NOT_PROVISIONED', 'LATEST_PERMISSION_SET_PROVISIONED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListAccountsForProvisionedPermissionSetResponse

### AccountIds
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAccessScopesRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAccessScopesRequestPaginate

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListApplicationAccessScopesResponse

### Scopes
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ScopeDetails]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAssignmentsFilter

### ApplicationArn
- **Type**: typing.Optional[str]


# ListApplicationAssignmentsForPrincipalRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ListApplicationAssignmentsFilter]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAssignmentsForPrincipalRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ListApplicationAssignmentsFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListApplicationAssignmentsForPrincipalResponse

### ApplicationAssignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ApplicationAssignmentForPrincipal]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAssignmentsRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAssignmentsRequestPaginate

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListApplicationAssignmentsResponse

### ApplicationAssignments
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ApplicationAssignment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAuthenticationMethodsRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationAuthenticationMethodsRequestPaginate

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListApplicationAuthenticationMethodsResponse

### AuthenticationMethods
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AuthenticationMethodItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationGrantsRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationGrantsRequestPaginate

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListApplicationGrantsResponse

### Grants
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.GrantItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationProvidersRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationProvidersRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListApplicationProvidersResponse

### ApplicationProviders
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ApplicationProvider]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsFilter

### ApplicationAccount
- **Type**: typing.Optional[str]

### ApplicationProvider
- **Type**: typing.Optional[str]


# ListApplicationsRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ListApplicationsFilter]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListApplicationsRequestPaginate

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ListApplicationsFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListApplicationsResponse

### Applications
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.Application]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListCustomerManagedPolicyReferencesInPermissionSetRequest

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


# ListCustomerManagedPolicyReferencesInPermissionSetRequestPaginate

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListCustomerManagedPolicyReferencesInPermissionSetResponse

### CustomerManagedPolicyReferences
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.CustomerManagedPolicyReference]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListInstancesRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListInstancesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListInstancesResponse

### Instances
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.InstanceMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListManagedPoliciesInPermissionSetRequest

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


# ListManagedPoliciesInPermissionSetRequestPaginate

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListManagedPoliciesInPermissionSetResponse

### AttachedManagedPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AttachedManagedPolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionSetProvisioningStatusRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.OperationStatusFilter]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionSetProvisioningStatusRequestPaginate

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Filter
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.OperationStatusFilter]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListPermissionSetProvisioningStatusResponse

### PermissionSetsProvisioningStatus
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PermissionSetProvisioningStatusMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionSetsProvisionedToAccountRequest

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


# ListPermissionSetsProvisionedToAccountRequestPaginate

### AccountId
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ProvisioningStatus
- **Type**: typing.Optional[typing.Literal['LATEST_PERMISSION_SET_NOT_PROVISIONED', 'LATEST_PERMISSION_SET_PROVISIONED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListPermissionSetsProvisionedToAccountResponse

### PermissionSets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionSetsRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPermissionSetsRequestPaginate

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListPermissionSetsResponse

### PermissionSets
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTrustedTokenIssuersRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTrustedTokenIssuersRequestPaginate

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PaginatorConfig]


# ListTrustedTokenIssuersResponse

### TrustedTokenIssuers
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.TrustedTokenIssuerMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# OidcJwtConfiguration

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


# OidcJwtUpdateConfiguration

### ClaimAttributePath
- **Type**: typing.Optional[str]

### IdentityStoreAttributePath
- **Type**: typing.Optional[str]

### JwksRetrievalOption
- **Type**: typing.Optional[typing.Literal['OPEN_ID_DISCOVERY']]


# OperationStatusFilter

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionSet

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


# PermissionSetProvisioningStatus

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


# PermissionSetProvisioningStatusMetadata

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### RequestId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]


# PermissionsBoundary

### CustomerManagedPolicyReference
- **Type**: <class 'NoneType'>

### ManagedPolicyArn
- **Type**: typing.Optional[str]


# PortalOptions

### SignInOptions
- **Type**: <class 'NoneType'>

### Visibility
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ProvisionPermissionSetRequest

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


# ProvisionPermissionSetResponse

### PermissionSetProvisioningStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PermissionSetProvisioningStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResponseMetadata'>
- **Required**: Yes


# PutApplicationAccessScopeRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Scope
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizedTargets
- **Type**: typing.Optional[typing.List[str]]


# PutApplicationAssignmentConfigurationRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AssignmentRequired
- **Type**: <class 'bool'>
- **Required**: Yes


# PutApplicationAuthenticationMethodRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMethod
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AuthenticationMethod, aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.AuthenticationMethodOutput]
- **Required**: Yes

### AuthenticationMethodType
- **Type**: typing.Literal['IAM']
- **Required**: Yes


# PutApplicationGrantRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Grant
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.Grant, aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.GrantOutput]
- **Required**: Yes

### GrantType
- **Type**: typing.Literal['authorization_code', 'refresh_token', 'urn:ietf:params:oauth:grant-type:jwt-bearer', 'urn:ietf:params:oauth:grant-type:token-exchange']
- **Required**: Yes


# PutInlinePolicyToPermissionSetRequest

### InlinePolicy
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutPermissionsBoundaryToPermissionSetRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionSetArn
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionsBoundary
- **Type**: <class 'aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.PermissionsBoundary'>
- **Required**: Yes


# ResourceServerConfig

### Scopes
- **Type**: typing.Optional[typing.Dict[str, aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.ResourceServerScopeDetails]]


# ResourceServerScopeDetails

### DetailedTitle
- **Type**: typing.Optional[str]

### LongDescription
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


# ScopeDetails

### Scope
- **Type**: <class 'str'>
- **Required**: Yes

### AuthorizedTargets
- **Type**: typing.Optional[typing.List[str]]


# SignInOptions

### Origin
- **Type**: typing.Literal['APPLICATION', 'IDENTITY_CENTER']
- **Required**: Yes

### ApplicationUrl
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.Tag]
- **Required**: Yes

### InstanceArn
- **Type**: typing.Optional[str]


# TrustedTokenIssuerConfiguration

### OidcJwtConfiguration
- **Type**: <class 'NoneType'>


# TrustedTokenIssuerMetadata

### Name
- **Type**: typing.Optional[str]

### TrustedTokenIssuerArn
- **Type**: typing.Optional[str]

### TrustedTokenIssuerType
- **Type**: typing.Optional[typing.Literal['OIDC_JWT']]


# TrustedTokenIssuerUpdateConfiguration

### OidcJwtConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.OidcJwtUpdateConfiguration]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes

### InstanceArn
- **Type**: typing.Optional[str]


# UpdateApplicationPortalOptions

### SignInOptions
- **Type**: <class 'NoneType'>


# UpdateApplicationRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### PortalOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.UpdateApplicationPortalOptions]

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# UpdateInstanceAccessControlAttributeConfigurationRequest

### InstanceAccessControlAttributeConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.InstanceAccessControlAttributeConfiguration, aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.InstanceAccessControlAttributeConfigurationOutput]
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateInstanceRequest

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePermissionSetRequest

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


# UpdateTrustedTokenIssuerRequest

### TrustedTokenIssuerArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### TrustedTokenIssuerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.sso_admin.sso_admin_classes.TrustedTokenIssuerUpdateConfiguration]


