# Iam Iam Classes

# AccessDetail

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: typing.Optional[str]

### EntityPath
- **Type**: typing.Optional[str]

### LastAuthenticatedTime
- **Type**: typing.Optional[datetime.datetime]

### TotalAuthenticatedEntities
- **Type**: typing.Optional[int]


# AccessKey

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### SecretAccessKey
- **Type**: <class 'str'>
- **Required**: Yes

### CreateDate
- **Type**: typing.Optional[datetime.datetime]


# AccessKeyLastUsed

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### LastUsedDate
- **Type**: typing.Optional[datetime.datetime]


# AccessKeyMetadata

### UserName
- **Type**: typing.Optional[str]

### AccessKeyId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]


# AddClientIDToOpenIDConnectProviderRequest

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientID
- **Type**: <class 'str'>
- **Required**: Yes


# AddRoleToInstanceProfileRequest

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# AddRoleToInstanceProfileRequestInstanceProfileAddRole

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# AddUserToGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# AddUserToGroupRequestGroupAddUser

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# AddUserToGroupRequestUserAddGroup

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachGroupPolicyRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachGroupPolicyRequestGroupAttachPolicy

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachGroupPolicyRequestPolicyAttachGroup

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachRolePolicyRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachRolePolicyRequestPolicyAttachRole

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachRolePolicyRequestRoleAttachPolicy

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachUserPolicyRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachUserPolicyRequestPolicyAttachUser

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachUserPolicyRequestUserAttachPolicy

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachedPermissionsBoundary

### PermissionsBoundaryType
- **Type**: typing.Optional[typing.Literal['PermissionsBoundaryPolicy']]

### PermissionsBoundaryArn
- **Type**: typing.Optional[str]


# AttachedPolicy

### PolicyName
- **Type**: typing.Optional[str]

### PolicyArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChangePasswordRequest

### OldPassword
- **Type**: <class 'str'>
- **Required**: Yes

### NewPassword
- **Type**: <class 'str'>
- **Required**: Yes


# ChangePasswordRequestServiceResourceChangePassword

### OldPassword
- **Type**: <class 'str'>
- **Required**: Yes

### NewPassword
- **Type**: <class 'str'>
- **Required**: Yes


# ContextEntry

### ContextKeyName
- **Type**: typing.Optional[str]

### ContextKeyValues
- **Type**: typing.Optional[typing.List[str]]

### ContextKeyType
- **Type**: typing.Optional[typing.Literal['binary', 'binaryList', 'boolean', 'booleanList', 'date', 'dateList', 'ip', 'ipList', 'numeric', 'numericList', 'string', 'stringList']]


# CreateAccessKeyRequest

### UserName
- **Type**: typing.Optional[str]


# CreateAccessKeyResponse

### AccessKey
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.AccessKey'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAccountAliasRequest

### AccountAlias
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAccountAliasRequestServiceResourceCreateAccountAlias

### AccountAlias
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]


# CreateGroupRequestGroupCreate

### Path
- **Type**: typing.Optional[str]


# CreateGroupRequestServiceResourceCreateGroup

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]


# CreateGroupResponse

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.Group'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# CreateInstanceProfileRequest

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# CreateInstanceProfileRequestServiceResourceCreateInstanceProfile

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# CreateInstanceProfileResponse

### InstanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.InstanceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLoginProfileRequest

### UserName
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# CreateLoginProfileRequestLoginProfileCreate

### Password
- **Type**: typing.Optional[str]

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# CreateLoginProfileRequestUserCreateLoginProfile

### Password
- **Type**: typing.Optional[str]

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# CreateLoginProfileResponse

### LoginProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.LoginProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOpenIDConnectProviderRequest

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ClientIDList
- **Type**: typing.Optional[typing.List[str]]

### ThumbprintList
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# CreateOpenIDConnectProviderResponse

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePolicyRequest

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# CreatePolicyRequestServiceResourceCreatePolicy

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# CreatePolicyResponse

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.Policy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePolicyVersionRequest

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### SetAsDefault
- **Type**: typing.Optional[bool]


# CreatePolicyVersionRequestPolicyCreateVersion

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### SetAsDefault
- **Type**: typing.Optional[bool]


# CreatePolicyVersionResponse

### PolicyVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.PolicyVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRoleRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### AssumeRolePolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### MaxSessionDuration
- **Type**: typing.Optional[int]

### PermissionsBoundary
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# CreateRoleRequestServiceResourceCreateRole

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### AssumeRolePolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### MaxSessionDuration
- **Type**: typing.Optional[int]

### PermissionsBoundary
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# CreateRoleResponse

### Role
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.Role'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSAMLProviderRequest

### SAMLMetadataDocument
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]

### AssertionEncryptionMode
- **Type**: typing.Optional[typing.Literal['Allowed', 'Required']]

### AddPrivateKey
- **Type**: typing.Optional[str]


# CreateSAMLProviderRequestServiceResourceCreateSamlProvider

### SAMLMetadataDocument
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]

### AssertionEncryptionMode
- **Type**: typing.Optional[typing.Literal['Allowed', 'Required']]

### AddPrivateKey
- **Type**: typing.Optional[str]


# CreateSAMLProviderResponse

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceLinkedRoleRequest

### AWSServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CustomSuffix
- **Type**: typing.Optional[str]


# CreateServiceLinkedRoleResponse

### Role
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.Role'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# CreateServiceSpecificCredentialRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateServiceSpecificCredentialResponse

### ServiceSpecificCredential
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ServiceSpecificCredential'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundary
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# CreateUserRequestServiceResourceCreateUser

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundary
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# CreateUserRequestUserCreate

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundary
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# CreateUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVirtualMFADeviceRequest

### VirtualMFADeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDevice

### VirtualMFADeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# CreateVirtualMFADeviceResponse

### VirtualMFADevice
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.VirtualMFADevice'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# DeactivateMFADeviceRequest

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# DeleteAccessKeyRequest

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# DeleteAccountAliasRequest

### AccountAlias
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupPolicyRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceProfileRequest

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoginProfileRequest

### UserName
- **Type**: typing.Optional[str]


# DeleteOpenIDConnectProviderRequest

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyRequest

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyVersionRequest

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRolePermissionsBoundaryRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRolePolicyRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoleRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSAMLProviderRequest

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSSHPublicKeyRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServerCertificateRequest

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceLinkedRoleRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceLinkedRoleResponse

### DeletionTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteServiceSpecificCredentialRequest

### ServiceSpecificCredentialId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# DeleteSigningCertificateRequest

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# DeleteUserPermissionsBoundaryRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserPolicyRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVirtualMFADeviceRequest

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes


# DeletionTaskFailureReasonType

### Reason
- **Type**: typing.Optional[str]

### RoleUsageList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.RoleUsageType]]


# DetachGroupPolicyRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachGroupPolicyRequestGroupDetachPolicy

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachGroupPolicyRequestPolicyDetachGroup

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachRolePolicyRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachRolePolicyRequestPolicyDetachRole

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachRolePolicyRequestRoleDetachPolicy

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachUserPolicyRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachUserPolicyRequestPolicyDetachUser

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachUserPolicyRequestUserDetachPolicy

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DisableOrganizationsRootCredentialsManagementResponse

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledFeatures
- **Type**: typing.List[typing.Literal['RootCredentialsManagement', 'RootSessions']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# DisableOrganizationsRootSessionsResponse

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledFeatures
- **Type**: typing.List[typing.Literal['RootCredentialsManagement', 'RootSessions']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# EnableMFADeviceRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationCode1
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationCode2
- **Type**: <class 'str'>
- **Required**: Yes


# EnableMFADeviceRequestMfaDeviceAssociate

### AuthenticationCode1
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationCode2
- **Type**: <class 'str'>
- **Required**: Yes


# EnableMFADeviceRequestUserEnableMfa

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationCode1
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationCode2
- **Type**: <class 'str'>
- **Required**: Yes


# EnableOrganizationsRootCredentialsManagementResponse

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledFeatures
- **Type**: typing.List[typing.Literal['RootCredentialsManagement', 'RootSessions']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# EnableOrganizationsRootSessionsResponse

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledFeatures
- **Type**: typing.List[typing.Literal['RootCredentialsManagement', 'RootSessions']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# EntityDetails

### EntityInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.EntityInfo'>
- **Required**: Yes

### LastAuthenticated
- **Type**: typing.Optional[datetime.datetime]


# EntityInfo

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['GROUP', 'ROLE', 'USER']
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]


# ErrorDetails

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluationResult

### EvalActionName
- **Type**: <class 'str'>
- **Required**: Yes

### EvalDecision
- **Type**: typing.Literal['allowed', 'explicitDeny', 'implicitDeny']
- **Required**: Yes

### EvalResourceName
- **Type**: typing.Optional[str]

### MatchedStatements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Statement]]

### MissingContextValues
- **Type**: typing.Optional[typing.List[str]]

### OrganizationsDecisionDetail
- **Type**: <class 'NoneType'>

### PermissionsBoundaryDecisionDetail
- **Type**: <class 'NoneType'>

### EvalDecisionDetails
- **Type**: typing.Optional[typing.Dict[str, typing.Literal['allowed', 'explicitDeny', 'implicitDeny']]]

### ResourceSpecificResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.ResourceSpecificResult]]


# GenerateCredentialReportResponse

### State
- **Type**: typing.Literal['COMPLETE', 'INPROGRESS', 'STARTED']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateOrganizationsAccessReportRequest

### EntityPath
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationsPolicyId
- **Type**: typing.Optional[str]


# GenerateOrganizationsAccessReportResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GenerateServiceLastAccessedDetailsRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Granularity
- **Type**: typing.Optional[typing.Literal['ACTION_LEVEL', 'SERVICE_LEVEL']]


# GenerateServiceLastAccessedDetailsResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccessKeyLastUsedRequest

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessKeyLastUsedResponse

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessKeyLastUsed
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.AccessKeyLastUsed'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccountAuthorizationDetailsRequest

### Filter
- **Type**: typing.Optional[typing.List[typing.Literal['AWSManagedPolicy', 'Group', 'LocalManagedPolicy', 'Role', 'User']]]

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# GetAccountAuthorizationDetailsRequestPaginate

### Filter
- **Type**: typing.Optional[typing.List[typing.Literal['AWSManagedPolicy', 'Group', 'LocalManagedPolicy', 'Role', 'User']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# GetAccountAuthorizationDetailsResponse

### UserDetailList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.UserDetail]
- **Required**: Yes

### GroupDetailList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.GroupDetail]
- **Required**: Yes

### RoleDetailList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.RoleDetail]
- **Required**: Yes

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.ManagedPolicyDetail]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccountPasswordPolicyResponse

### PasswordPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.PasswordPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetAccountSummaryResponse

### SummaryMap
- **Type**: typing.Dict[typing.Literal['AccessKeysPerUserQuota', 'AccountAccessKeysPresent', 'AccountMFAEnabled', 'AccountPasswordPresent', 'AccountSigningCertificatesPresent', 'AttachedPoliciesPerGroupQuota', 'AttachedPoliciesPerRoleQuota', 'AttachedPoliciesPerUserQuota', 'GlobalEndpointTokenVersion', 'GroupPolicySizeQuota', 'Groups', 'GroupsPerUserQuota', 'GroupsQuota', 'MFADevices', 'MFADevicesInUse', 'Policies', 'PoliciesQuota', 'PolicySizeQuota', 'PolicyVersionsInUse', 'PolicyVersionsInUseQuota', 'ServerCertificates', 'ServerCertificatesQuota', 'SigningCertificatesPerUserQuota', 'UserPolicySizeQuota', 'Users', 'UsersQuota', 'VersionsPerPolicyQuota'], int]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetContextKeysForCustomPolicyRequest

### PolicyInputList
- **Type**: typing.List[str]
- **Required**: Yes


# GetContextKeysForPolicyResponse

### ContextKeyNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetContextKeysForPrincipalPolicyRequest

### PolicySourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyInputList
- **Type**: typing.Optional[typing.List[str]]


# GetCredentialReportResponse

### Content
- **Type**: <class 'bytes'>
- **Required**: Yes

### ReportFormat
- **Type**: typing.Literal['text/csv']
- **Required**: Yes

### GeneratedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetGroupPolicyRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupPolicyResponse

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: typing.Union[str, aws_resource_validator.pydantic_models.iam.iam_classes.PolicyDocumentDict]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# GetGroupRequestPaginate

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# GetGroupResponse

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.Group'>
- **Required**: Yes

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.User]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetInstanceProfileRequest

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceProfileRequestWait

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetInstanceProfileResponse

### InstanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.InstanceProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetLoginProfileRequest

### UserName
- **Type**: typing.Optional[str]


# GetLoginProfileResponse

### LoginProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.LoginProfile'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetMFADeviceRequest

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# GetMFADeviceResponse

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### EnableDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Certifications
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetOpenIDConnectProviderRequest

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetOpenIDConnectProviderResponse

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ClientIDList
- **Type**: typing.List[str]
- **Required**: Yes

### ThumbprintList
- **Type**: typing.List[str]
- **Required**: Yes

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetOrganizationsAccessReportRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### SortKey
- **Type**: typing.Optional[typing.Literal['LAST_AUTHENTICATED_TIME_ASCENDING', 'LAST_AUTHENTICATED_TIME_DESCENDING', 'SERVICE_NAMESPACE_ASCENDING', 'SERVICE_NAMESPACE_DESCENDING']]


# GetOrganizationsAccessReportResponse

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### JobCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JobCompletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### NumberOfServicesAccessible
- **Type**: <class 'int'>
- **Required**: Yes

### NumberOfServicesNotAccessed
- **Type**: <class 'int'>
- **Required**: Yes

### AccessDetails
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.AccessDetail]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ErrorDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetPolicyRequest

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyRequestWait

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetPolicyResponse

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.Policy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetPolicyVersionRequest

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyVersionResponse

### PolicyVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.PolicyVersion'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetRolePolicyRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRolePolicyResponse

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: typing.Union[str, aws_resource_validator.pydantic_models.iam.iam_classes.PolicyDocumentDict]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetRoleRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRoleRequestWait

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetRoleResponse

### Role
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.Role'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetSAMLProviderRequest

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetSAMLProviderResponse

### SAMLProviderUUID
- **Type**: <class 'str'>
- **Required**: Yes

### SAMLMetadataDocument
- **Type**: <class 'str'>
- **Required**: Yes

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ValidUntil
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes

### AssertionEncryptionMode
- **Type**: typing.Literal['Allowed', 'Required']
- **Required**: Yes

### PrivateKeyList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.SAMLPrivateKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetSSHPublicKeyRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Encoding
- **Type**: typing.Literal['PEM', 'SSH']
- **Required**: Yes


# GetSSHPublicKeyResponse

### SSHPublicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.SSHPublicKey'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetServerCertificateRequest

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetServerCertificateResponse

### ServerCertificate
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ServerCertificate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceLastAccessedDetailsRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# GetServiceLastAccessedDetailsResponse

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### JobType
- **Type**: typing.Literal['ACTION_LEVEL', 'SERVICE_LEVEL']
- **Required**: Yes

### JobCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServicesLastAccessed
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.ServiceLastAccessed]
- **Required**: Yes

### JobCompletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ErrorDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceLastAccessedDetailsWithEntitiesRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# GetServiceLastAccessedDetailsWithEntitiesResponse

### JobStatus
- **Type**: typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS']
- **Required**: Yes

### JobCreationDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JobCompletionDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EntityDetailsList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.EntityDetails]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ErrorDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetServiceLinkedRoleDeletionStatusRequest

### DeletionTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceLinkedRoleDeletionStatusResponse

### Status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'SUCCEEDED']
- **Required**: Yes

### Reason
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.DeletionTaskFailureReasonType'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserPolicyRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserPolicyResponse

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: typing.Union[str, aws_resource_validator.pydantic_models.iam.iam_classes.PolicyDocumentDict]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# GetUserRequest

### UserName
- **Type**: typing.Optional[str]


# GetUserRequestWait

### UserName
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: <class 'NoneType'>


# GetUserResponse

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.User'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# Group

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# GroupDetail

### Path
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### GroupPolicyList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.PolicyDetail]]

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.AttachedPolicy]]


# InstanceProfile

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceProfileId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Roles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Role]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# ListAccessKeysRequest

### UserName
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAccessKeysRequestPaginate

### UserName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListAccessKeysResponse

### AccessKeyMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.AccessKeyMetadata]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListAccountAliasesRequest

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAccountAliasesRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListAccountAliasesResponse

### AccountAliases
- **Type**: typing.List[str]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListAttachedGroupPoliciesRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAttachedGroupPoliciesRequestPaginate

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListAttachedGroupPoliciesResponse

### AttachedPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.AttachedPolicy]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListAttachedRolePoliciesRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAttachedRolePoliciesRequestPaginate

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListAttachedRolePoliciesResponse

### AttachedPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.AttachedPolicy]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListAttachedUserPoliciesRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAttachedUserPoliciesRequestPaginate

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListAttachedUserPoliciesResponse

### AttachedPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.AttachedPolicy]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListEntitiesForPolicyRequest

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### EntityFilter
- **Type**: typing.Optional[typing.Literal['AWSManagedPolicy', 'Group', 'LocalManagedPolicy', 'Role', 'User']]

### PathPrefix
- **Type**: typing.Optional[str]

### PolicyUsageFilter
- **Type**: typing.Optional[typing.Literal['PermissionsBoundary', 'PermissionsPolicy']]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListEntitiesForPolicyRequestPaginate

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### EntityFilter
- **Type**: typing.Optional[typing.Literal['AWSManagedPolicy', 'Group', 'LocalManagedPolicy', 'Role', 'User']]

### PathPrefix
- **Type**: typing.Optional[str]

### PolicyUsageFilter
- **Type**: typing.Optional[typing.Literal['PermissionsBoundary', 'PermissionsPolicy']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListEntitiesForPolicyResponse

### PolicyGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.PolicyGroup]
- **Required**: Yes

### PolicyUsers
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.PolicyUser]
- **Required**: Yes

### PolicyRoles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.PolicyRole]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListGroupPoliciesRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListGroupPoliciesRequestPaginate

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListGroupPoliciesResponse

### PolicyNames
- **Type**: typing.List[str]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListGroupsForUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListGroupsForUserRequestPaginate

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListGroupsForUserResponse

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Group]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListGroupsRequest

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListGroupsRequestPaginate

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListGroupsResponse

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Group]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListInstanceProfileTagsRequest

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListInstanceProfileTagsRequestPaginate

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListInstanceProfileTagsResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListInstanceProfilesForRoleRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListInstanceProfilesForRoleRequestPaginate

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListInstanceProfilesForRoleResponse

### InstanceProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.InstanceProfile]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListInstanceProfilesRequest

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListInstanceProfilesRequestPaginate

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListInstanceProfilesResponse

### InstanceProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.InstanceProfile]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListMFADeviceTagsRequest

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListMFADeviceTagsRequestPaginate

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListMFADeviceTagsResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListMFADevicesRequest

### UserName
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListMFADevicesRequestPaginate

### UserName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListMFADevicesResponse

### MFADevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.MFADevice]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListOpenIDConnectProviderTagsRequest

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListOpenIDConnectProviderTagsRequestPaginate

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListOpenIDConnectProviderTagsResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListOpenIDConnectProvidersResponse

### OpenIDConnectProviderList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.OpenIDConnectProviderListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListOrganizationsFeaturesResponse

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledFeatures
- **Type**: typing.List[typing.Literal['RootCredentialsManagement', 'RootSessions']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListPoliciesGrantingServiceAccessEntry

### ServiceNamespace
- **Type**: typing.Optional[str]

### Policies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.PolicyGrantingServiceAccess]]


# ListPoliciesGrantingServiceAccessRequest

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceNamespaces
- **Type**: typing.List[str]
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]


# ListPoliciesGrantingServiceAccessResponse

### PoliciesGrantingServiceAccess
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.ListPoliciesGrantingServiceAccessEntry]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListPoliciesRequest

### Scope
- **Type**: typing.Optional[typing.Literal['AWS', 'All', 'Local']]

### OnlyAttached
- **Type**: typing.Optional[bool]

### PathPrefix
- **Type**: typing.Optional[str]

### PolicyUsageFilter
- **Type**: typing.Optional[typing.Literal['PermissionsBoundary', 'PermissionsPolicy']]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListPoliciesRequestPaginate

### Scope
- **Type**: typing.Optional[typing.Literal['AWS', 'All', 'Local']]

### OnlyAttached
- **Type**: typing.Optional[bool]

### PathPrefix
- **Type**: typing.Optional[str]

### PolicyUsageFilter
- **Type**: typing.Optional[typing.Literal['PermissionsBoundary', 'PermissionsPolicy']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListPoliciesResponse

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Policy]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListPolicyTagsRequest

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListPolicyTagsRequestPaginate

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListPolicyTagsResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListPolicyVersionsRequest

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListPolicyVersionsRequestPaginate

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListPolicyVersionsResponse

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.PolicyVersion]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListRolePoliciesRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListRolePoliciesRequestPaginate

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListRolePoliciesResponse

### PolicyNames
- **Type**: typing.List[str]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListRoleTagsRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListRoleTagsRequestPaginate

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListRoleTagsResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListRolesRequest

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListRolesRequestPaginate

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListRolesResponse

### Roles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Role]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListSAMLProviderTagsRequest

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListSAMLProviderTagsRequestPaginate

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListSAMLProviderTagsResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListSAMLProvidersResponse

### SAMLProviderList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.SAMLProviderListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListSSHPublicKeysRequest

### UserName
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListSSHPublicKeysRequestPaginate

### UserName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListSSHPublicKeysResponse

### SSHPublicKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.SSHPublicKeyMetadata]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListServerCertificateTagsRequest

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListServerCertificateTagsRequestPaginate

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListServerCertificateTagsResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListServerCertificatesRequest

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListServerCertificatesRequestPaginate

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListServerCertificatesResponse

### ServerCertificateMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.ServerCertificateMetadata]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListServiceSpecificCredentialsRequest

### UserName
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]


# ListServiceSpecificCredentialsResponse

### ServiceSpecificCredentials
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.ServiceSpecificCredentialMetadata]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListSigningCertificatesRequest

### UserName
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListSigningCertificatesRequestPaginate

### UserName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListSigningCertificatesResponse

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.SigningCertificate]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListUserPoliciesRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListUserPoliciesRequestPaginate

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListUserPoliciesResponse

### PolicyNames
- **Type**: typing.List[str]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListUserTagsRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListUserTagsRequestPaginate

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListUserTagsResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListUsersRequest

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListUsersRequestPaginate

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListUsersResponse

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.User]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ListVirtualMFADevicesRequest

### AssignmentStatus
- **Type**: typing.Optional[typing.Literal['Any', 'Assigned', 'Unassigned']]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListVirtualMFADevicesRequestPaginate

### AssignmentStatus
- **Type**: typing.Optional[typing.Literal['Any', 'Assigned', 'Unassigned']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# ListVirtualMFADevicesResponse

### VirtualMFADevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.VirtualMFADevice]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# LoginProfile

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# MFADevice

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### EnableDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ManagedPolicyDetail

### PolicyName
- **Type**: typing.Optional[str]

### PolicyId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### DefaultVersionId
- **Type**: typing.Optional[str]

### AttachmentCount
- **Type**: typing.Optional[int]

### PermissionsBoundaryUsageCount
- **Type**: typing.Optional[int]

### IsAttachable
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### UpdateDate
- **Type**: typing.Optional[datetime.datetime]

### PolicyVersionList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.PolicyVersion]]


# OpenIDConnectProviderListEntry

### Arn
- **Type**: typing.Optional[str]


# OrganizationsDecisionDetail

### AllowedByOrganizations
- **Type**: typing.Optional[bool]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PasswordPolicy

### MinimumPasswordLength
- **Type**: typing.Optional[int]

### RequireSymbols
- **Type**: typing.Optional[bool]

### RequireNumbers
- **Type**: typing.Optional[bool]

### RequireUppercaseCharacters
- **Type**: typing.Optional[bool]

### RequireLowercaseCharacters
- **Type**: typing.Optional[bool]

### AllowUsersToChangePassword
- **Type**: typing.Optional[bool]

### ExpirePasswords
- **Type**: typing.Optional[bool]

### MaxPasswordAge
- **Type**: typing.Optional[int]

### PasswordReusePrevention
- **Type**: typing.Optional[int]

### HardExpiry
- **Type**: typing.Optional[bool]


# PermissionsBoundaryDecisionDetail

### AllowedByPermissionsBoundary
- **Type**: typing.Optional[bool]


# Policy

### PolicyName
- **Type**: typing.Optional[str]

### PolicyId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### DefaultVersionId
- **Type**: typing.Optional[str]

### AttachmentCount
- **Type**: typing.Optional[int]

### PermissionsBoundaryUsageCount
- **Type**: typing.Optional[int]

### IsAttachable
- **Type**: typing.Optional[bool]

### Description
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### UpdateDate
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# PolicyDetail

### PolicyName
- **Type**: typing.Optional[str]

### PolicyDocument
- **Type**: <class 'NoneType'>


# PolicyDocumentDict

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### Statement
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.PolicyDocumentStatement]
- **Required**: Yes


# PolicyDocumentStatement

### Effect
- **Type**: <class 'str'>
- **Required**: Yes

### Resource
- **Type**: typing.Union[typing.List[str], str]
- **Required**: Yes

### Sid
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Union[typing.List[str], str]
- **Required**: Yes


# PolicyGrantingServiceAccess

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyType
- **Type**: typing.Literal['INLINE', 'MANAGED']
- **Required**: Yes

### PolicyArn
- **Type**: typing.Optional[str]

### EntityType
- **Type**: typing.Optional[typing.Literal['GROUP', 'ROLE', 'USER']]

### EntityName
- **Type**: typing.Optional[str]


# PolicyGroup

### GroupName
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]


# PolicyRole

### RoleName
- **Type**: typing.Optional[str]

### RoleId
- **Type**: typing.Optional[str]


# PolicyUser

### UserName
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]


# PolicyVersion

### Document
- **Type**: typing.Union[str, aws_resource_validator.pydantic_models.iam.iam_classes.PolicyDocumentDict, NoneType]

### VersionId
- **Type**: typing.Optional[str]

### IsDefaultVersion
- **Type**: typing.Optional[bool]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]


# Position

### Line
- **Type**: typing.Optional[int]

### Column
- **Type**: typing.Optional[int]


# PutGroupPolicyRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutGroupPolicyRequestGroupCreatePolicy

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutGroupPolicyRequestGroupPolicyPut

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutRolePermissionsBoundaryRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionsBoundary
- **Type**: <class 'str'>
- **Required**: Yes


# PutRolePolicyRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutRolePolicyRequestRolePolicyPut

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutUserPermissionsBoundaryRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionsBoundary
- **Type**: <class 'str'>
- **Required**: Yes


# PutUserPolicyRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutUserPolicyRequestUserCreatePolicy

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutUserPolicyRequestUserPolicyPut

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveClientIDFromOpenIDConnectProviderRequest

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientID
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveRoleFromInstanceProfileRequest

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRole

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveUserFromGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveUserFromGroupRequestGroupRemoveUser

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveUserFromGroupRequestUserRemoveGroup

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# ResetServiceSpecificCredentialRequest

### ServiceSpecificCredentialId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# ResetServiceSpecificCredentialResponse

### ServiceSpecificCredential
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ServiceSpecificCredential'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# ResourceSpecificResult

### EvalResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### EvalResourceDecision
- **Type**: typing.Literal['allowed', 'explicitDeny', 'implicitDeny']
- **Required**: Yes

### MatchedStatements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Statement]]

### MissingContextValues
- **Type**: typing.Optional[typing.List[str]]

### EvalDecisionDetails
- **Type**: typing.Optional[typing.Dict[str, typing.Literal['allowed', 'explicitDeny', 'implicitDeny']]]

### PermissionsBoundaryDecisionDetail
- **Type**: <class 'NoneType'>


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


# ResyncMFADeviceRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationCode1
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationCode2
- **Type**: <class 'str'>
- **Required**: Yes


# ResyncMFADeviceRequestMfaDeviceResync

### AuthenticationCode1
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationCode2
- **Type**: <class 'str'>
- **Required**: Yes


# Role

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AssumeRolePolicyDocument
- **Type**: typing.Union[str, aws_resource_validator.pydantic_models.iam.iam_classes.PolicyDocumentDict, NoneType]

### Description
- **Type**: typing.Optional[str]

### MaxSessionDuration
- **Type**: typing.Optional[int]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.AttachedPermissionsBoundary]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]

### RoleLastUsed
- **Type**: <class 'NoneType'>


# RoleDetail

### Path
- **Type**: typing.Optional[str]

### RoleName
- **Type**: typing.Optional[str]

### RoleId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### AssumeRolePolicyDocument
- **Type**: typing.Union[str, aws_resource_validator.pydantic_models.iam.iam_classes.PolicyDocumentDict, NoneType]

### InstanceProfileList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.InstanceProfile]]

### RolePolicyList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.PolicyDetail]]

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.AttachedPolicy]]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.AttachedPermissionsBoundary]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]

### RoleLastUsed
- **Type**: <class 'NoneType'>


# RoleLastUsed

### LastUsedDate
- **Type**: typing.Optional[datetime.datetime]

### Region
- **Type**: typing.Optional[str]


# RoleUsageType

### Region
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Optional[typing.List[str]]


# SAMLPrivateKey

### KeyId
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


# SAMLProviderListEntry

### Arn
- **Type**: typing.Optional[str]

### ValidUntil
- **Type**: typing.Optional[datetime.datetime]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]


# SSHPublicKey

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Fingerprint
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKeyBody
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### UploadDate
- **Type**: typing.Optional[datetime.datetime]


# SSHPublicKeyMetadata

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### UploadDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ServerCertificate

### ServerCertificateMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ServerCertificateMetadata'>
- **Required**: Yes

### CertificateBody
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateChain
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# ServerCertificateMetadata

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### ServerCertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### UploadDate
- **Type**: typing.Optional[datetime.datetime]

### Expiration
- **Type**: typing.Optional[datetime.datetime]


# ServiceLastAccessed

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceNamespace
- **Type**: <class 'str'>
- **Required**: Yes

### LastAuthenticated
- **Type**: typing.Optional[datetime.datetime]

### LastAuthenticatedEntity
- **Type**: typing.Optional[str]

### LastAuthenticatedRegion
- **Type**: typing.Optional[str]

### TotalAuthenticatedEntities
- **Type**: typing.Optional[int]

### TrackedActionsLastAccessed
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.TrackedActionLastAccessed]]


# ServiceSpecificCredential

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceUserName
- **Type**: <class 'str'>
- **Required**: Yes

### ServicePassword
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceSpecificCredentialId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes


# ServiceSpecificCredentialMetadata

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### ServiceUserName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServiceSpecificCredentialId
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# SetDefaultPolicyVersionRequest

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes


# SetSecurityTokenServicePreferencesRequest

### GlobalEndpointTokenVersion
- **Type**: typing.Literal['v1Token', 'v2Token']
- **Required**: Yes


# SigningCertificate

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateBody
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### UploadDate
- **Type**: typing.Optional[datetime.datetime]


# SimulateCustomPolicyRequest

### PolicyInputList
- **Type**: typing.List[str]
- **Required**: Yes

### ActionNames
- **Type**: typing.List[str]
- **Required**: Yes

### PermissionsBoundaryPolicyInputList
- **Type**: typing.Optional[typing.List[str]]

### ResourceArns
- **Type**: typing.Optional[typing.List[str]]

### ResourcePolicy
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[str]

### CallerArn
- **Type**: typing.Optional[str]

### ContextEntries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.ContextEntry]]

### ResourceHandlingOption
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# SimulateCustomPolicyRequestPaginate

### PolicyInputList
- **Type**: typing.List[str]
- **Required**: Yes

### ActionNames
- **Type**: typing.List[str]
- **Required**: Yes

### PermissionsBoundaryPolicyInputList
- **Type**: typing.Optional[typing.List[str]]

### ResourceArns
- **Type**: typing.Optional[typing.List[str]]

### ResourcePolicy
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[str]

### CallerArn
- **Type**: typing.Optional[str]

### ContextEntries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.ContextEntry]]

### ResourceHandlingOption
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# SimulatePolicyResponse

### EvaluationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.EvaluationResult]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# SimulatePrincipalPolicyRequest

### PolicySourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActionNames
- **Type**: typing.List[str]
- **Required**: Yes

### PolicyInputList
- **Type**: typing.Optional[typing.List[str]]

### PermissionsBoundaryPolicyInputList
- **Type**: typing.Optional[typing.List[str]]

### ResourceArns
- **Type**: typing.Optional[typing.List[str]]

### ResourcePolicy
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[str]

### CallerArn
- **Type**: typing.Optional[str]

### ContextEntries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.ContextEntry]]

### ResourceHandlingOption
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# SimulatePrincipalPolicyRequestPaginate

### PolicySourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActionNames
- **Type**: typing.List[str]
- **Required**: Yes

### PolicyInputList
- **Type**: typing.Optional[typing.List[str]]

### PermissionsBoundaryPolicyInputList
- **Type**: typing.Optional[typing.List[str]]

### ResourceArns
- **Type**: typing.Optional[typing.List[str]]

### ResourcePolicy
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[str]

### CallerArn
- **Type**: typing.Optional[str]

### ContextEntries
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.ContextEntry]]

### ResourceHandlingOption
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.PaginatorConfig]


# Statement

### SourcePolicyId
- **Type**: typing.Optional[str]

### SourcePolicyType
- **Type**: typing.Optional[typing.Literal['aws-managed', 'group', 'none', 'resource', 'role', 'user', 'user-managed']]

### StartPosition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.Position]

### EndPosition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.Position]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagInstanceProfileRequest

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes


# TagMFADeviceRequest

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes


# TagOpenIDConnectProviderRequest

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes


# TagPolicyRequest

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes


# TagRoleRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes


# TagSAMLProviderRequest

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes


# TagServerCertificateRequest

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes


# TagUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes


# TrackedActionLastAccessed

### ActionName
- **Type**: typing.Optional[str]

### LastAccessedEntity
- **Type**: typing.Optional[str]

### LastAccessedTime
- **Type**: typing.Optional[datetime.datetime]

### LastAccessedRegion
- **Type**: typing.Optional[str]


# UntagInstanceProfileRequest

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UntagMFADeviceRequest

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UntagOpenIDConnectProviderRequest

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UntagPolicyRequest

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UntagRoleRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UntagSAMLProviderRequest

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UntagServerCertificateRequest

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UntagUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAccessKeyRequest

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# UpdateAccessKeyRequestAccessKeyActivate

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UpdateAccessKeyRequestAccessKeyDeactivate

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UpdateAccessKeyRequestAccessKeyPairActivate

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UpdateAccessKeyRequestAccessKeyPairDeactivate

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UpdateAccountPasswordPolicyRequest

### MinimumPasswordLength
- **Type**: typing.Optional[int]

### RequireSymbols
- **Type**: typing.Optional[bool]

### RequireNumbers
- **Type**: typing.Optional[bool]

### RequireUppercaseCharacters
- **Type**: typing.Optional[bool]

### RequireLowercaseCharacters
- **Type**: typing.Optional[bool]

### AllowUsersToChangePassword
- **Type**: typing.Optional[bool]

### MaxPasswordAge
- **Type**: typing.Optional[int]

### PasswordReusePrevention
- **Type**: typing.Optional[int]

### HardExpiry
- **Type**: typing.Optional[bool]


# UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdate

### MinimumPasswordLength
- **Type**: typing.Optional[int]

### RequireSymbols
- **Type**: typing.Optional[bool]

### RequireNumbers
- **Type**: typing.Optional[bool]

### RequireUppercaseCharacters
- **Type**: typing.Optional[bool]

### RequireLowercaseCharacters
- **Type**: typing.Optional[bool]

### AllowUsersToChangePassword
- **Type**: typing.Optional[bool]

### MaxPasswordAge
- **Type**: typing.Optional[int]

### PasswordReusePrevention
- **Type**: typing.Optional[int]

### HardExpiry
- **Type**: typing.Optional[bool]


# UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicy

### MinimumPasswordLength
- **Type**: typing.Optional[int]

### RequireSymbols
- **Type**: typing.Optional[bool]

### RequireNumbers
- **Type**: typing.Optional[bool]

### RequireUppercaseCharacters
- **Type**: typing.Optional[bool]

### RequireLowercaseCharacters
- **Type**: typing.Optional[bool]

### AllowUsersToChangePassword
- **Type**: typing.Optional[bool]

### MaxPasswordAge
- **Type**: typing.Optional[int]

### PasswordReusePrevention
- **Type**: typing.Optional[int]

### HardExpiry
- **Type**: typing.Optional[bool]


# UpdateAssumeRolePolicyRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdate

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateGroupRequest

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### NewPath
- **Type**: typing.Optional[str]

### NewGroupName
- **Type**: typing.Optional[str]


# UpdateGroupRequestGroupUpdate

### NewPath
- **Type**: typing.Optional[str]

### NewGroupName
- **Type**: typing.Optional[str]


# UpdateLoginProfileRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: typing.Optional[str]

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# UpdateLoginProfileRequestLoginProfileUpdate

### Password
- **Type**: typing.Optional[str]

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# UpdateOpenIDConnectProviderThumbprintRequest

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ThumbprintList
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateRoleDescriptionRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRoleDescriptionResponse

### Role
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.Role'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateRoleRequest

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### MaxSessionDuration
- **Type**: typing.Optional[int]


# UpdateSAMLProviderRequest

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### SAMLMetadataDocument
- **Type**: typing.Optional[str]

### AssertionEncryptionMode
- **Type**: typing.Optional[typing.Literal['Allowed', 'Required']]

### AddPrivateKey
- **Type**: typing.Optional[str]

### RemovePrivateKey
- **Type**: typing.Optional[str]


# UpdateSAMLProviderRequestSamlProviderUpdate

### SAMLMetadataDocument
- **Type**: typing.Optional[str]

### AssertionEncryptionMode
- **Type**: typing.Optional[typing.Literal['Allowed', 'Required']]

### AddPrivateKey
- **Type**: typing.Optional[str]

### RemovePrivateKey
- **Type**: typing.Optional[str]


# UpdateSAMLProviderResponse

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSSHPublicKeyRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes


# UpdateServerCertificateRequest

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### NewPath
- **Type**: typing.Optional[str]

### NewServerCertificateName
- **Type**: typing.Optional[str]


# UpdateServerCertificateRequestServerCertificateUpdate

### NewPath
- **Type**: typing.Optional[str]

### NewServerCertificateName
- **Type**: typing.Optional[str]


# UpdateServiceSpecificCredentialRequest

### ServiceSpecificCredentialId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# UpdateSigningCertificateRequest

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# UpdateSigningCertificateRequestSigningCertificateActivate

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UpdateSigningCertificateRequestSigningCertificateDeactivate

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UpdateUserRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### NewPath
- **Type**: typing.Optional[str]

### NewUserName
- **Type**: typing.Optional[str]


# UpdateUserRequestUserUpdate

### NewPath
- **Type**: typing.Optional[str]

### NewUserName
- **Type**: typing.Optional[str]


# UploadSSHPublicKeyRequest

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKeyBody
- **Type**: <class 'str'>
- **Required**: Yes


# UploadSSHPublicKeyResponse

### SSHPublicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.SSHPublicKey'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# UploadServerCertificateRequest

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateBody
- **Type**: <class 'str'>
- **Required**: Yes

### PrivateKey
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### CertificateChain
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# UploadServerCertificateRequestServiceResourceCreateServerCertificate

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateBody
- **Type**: <class 'str'>
- **Required**: Yes

### PrivateKey
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### CertificateChain
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# UploadServerCertificateResponse

### ServerCertificateMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ServerCertificateMetadata'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# UploadSigningCertificateRequest

### CertificateBody
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# UploadSigningCertificateRequestServiceResourceCreateSigningCertificate

### CertificateBody
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# UploadSigningCertificateResponse

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.SigningCertificate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam.iam_classes.ResponseMetadata'>
- **Required**: Yes


# User

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PasswordLastUsed
- **Type**: typing.Optional[datetime.datetime]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.AttachedPermissionsBoundary]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# UserDetail

### Path
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]

### UserPolicyList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.PolicyDetail]]

### GroupList
- **Type**: typing.Optional[typing.List[str]]

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.AttachedPolicy]]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam.iam_classes.AttachedPermissionsBoundary]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# VirtualMFADevice

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Base32StringSeed
- **Type**: typing.Optional[bytes]

### QRCodePNG
- **Type**: typing.Optional[bytes]

### User
- **Type**: <class 'NoneType'>

### EnableDate
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam.iam_classes.Tag]]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


