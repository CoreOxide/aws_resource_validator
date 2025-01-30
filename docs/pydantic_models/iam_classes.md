# iam_classes

# AccessDetailTypeDef

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


# AccessKeyLastUsedTypeDef

### LastUsedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes


# AccessKeyMetadataTypeDef

### UserName
- **Type**: typing.Optional[str]

### AccessKeyId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]


# AccessKeyTypeDef

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


# AddClientIDToOpenIDConnectProviderRequestRequestTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientID
- **Type**: <class 'str'>
- **Required**: Yes


# AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# AddRoleToInstanceProfileRequestRequestTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# AddUserToGroupRequestGroupAddUserTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# AddUserToGroupRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# AddUserToGroupRequestUserAddGroupTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachGroupPolicyRequestGroupAttachPolicyTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachGroupPolicyRequestPolicyAttachGroupTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachGroupPolicyRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachRolePolicyRequestPolicyAttachRoleTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachRolePolicyRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachRolePolicyRequestRoleAttachPolicyTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachUserPolicyRequestPolicyAttachUserTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachUserPolicyRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachUserPolicyRequestUserAttachPolicyTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachedPermissionsBoundaryResponseTypeDef

### PermissionsBoundaryType
- **Type**: typing.Literal['PermissionsBoundaryPolicy']
- **Required**: Yes

### PermissionsBoundaryArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachedPermissionsBoundaryTypeDef

### PermissionsBoundaryType
- **Type**: typing.Optional[typing.Literal['PermissionsBoundaryPolicy']]

### PermissionsBoundaryArn
- **Type**: typing.Optional[str]


# AttachedPolicyTypeDef

### PolicyName
- **Type**: typing.Optional[str]

### PolicyArn
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChangePasswordRequestRequestTypeDef

### OldPassword
- **Type**: <class 'str'>
- **Required**: Yes

### NewPassword
- **Type**: <class 'str'>
- **Required**: Yes


# ChangePasswordRequestServiceResourceChangePasswordTypeDef

### OldPassword
- **Type**: <class 'str'>
- **Required**: Yes

### NewPassword
- **Type**: <class 'str'>
- **Required**: Yes


# ContextEntryTypeDef

### ContextKeyName
- **Type**: typing.Optional[str]

### ContextKeyValues
- **Type**: typing.Optional[typing.Sequence[str]]

### ContextKeyType
- **Type**: typing.Optional[typing.Literal['binary', 'binaryList', 'boolean', 'booleanList', 'date', 'dateList', 'ip', 'ipList', 'numeric', 'numericList', 'string', 'stringList']]


# CreateAccessKeyRequestRequestTypeDef

### UserName
- **Type**: typing.Optional[str]


# CreateAccessKeyResponseTypeDef

### AccessKey
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.AccessKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAccountAliasRequestRequestTypeDef

### AccountAlias
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef

### AccountAlias
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGroupRequestGroupCreateTypeDef

### Path
- **Type**: typing.Optional[str]


# CreateGroupRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]


# CreateGroupRequestServiceResourceCreateGroupTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]


# CreateGroupResponseTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.GroupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateInstanceProfileRequestRequestTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateInstanceProfileResponseTypeDef

### InstanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.InstanceProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLoginProfileRequestLoginProfileCreateTypeDef

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# CreateLoginProfileRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# CreateLoginProfileRequestUserCreateLoginProfileTypeDef

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# CreateLoginProfileResponseTypeDef

### LoginProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.LoginProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOpenIDConnectProviderRequestRequestTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ClientIDList
- **Type**: typing.Optional[typing.Sequence[str]]

### ThumbprintList
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateOpenIDConnectProviderResponseTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePolicyRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreatePolicyRequestServiceResourceCreatePolicyTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreatePolicyResponseTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.PolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePolicyVersionRequestPolicyCreateVersionTypeDef

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### SetAsDefault
- **Type**: typing.Optional[bool]


# CreatePolicyVersionRequestRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes

### SetAsDefault
- **Type**: typing.Optional[bool]


# CreatePolicyVersionResponseTypeDef

### PolicyVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.PolicyVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRoleRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateRoleRequestServiceResourceCreateRoleTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateRoleResponseTypeDef

### Role
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.RoleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSAMLProviderRequestRequestTypeDef

### SAMLMetadataDocument
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef

### SAMLMetadataDocument
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateSAMLProviderResponseTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceLinkedRoleRequestRequestTypeDef

### AWSServiceName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CustomSuffix
- **Type**: typing.Optional[str]


# CreateServiceLinkedRoleResponseTypeDef

### Role
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.RoleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateServiceSpecificCredentialRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateServiceSpecificCredentialResponseTypeDef

### ServiceSpecificCredential
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ServiceSpecificCredentialTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundary
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateUserRequestServiceResourceCreateUserTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundary
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateUserRequestUserCreateTypeDef

### Path
- **Type**: typing.Optional[str]

### PermissionsBoundary
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVirtualMFADeviceRequestRequestTypeDef

### VirtualMFADeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef

### VirtualMFADeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateVirtualMFADeviceResponseTypeDef

### VirtualMFADevice
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.VirtualMFADeviceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeactivateMFADeviceRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessKeyRequestRequestTypeDef

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# DeleteAccountAliasRequestRequestTypeDef

### AccountAlias
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupPolicyRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceProfileRequestRequestTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoginProfileRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOpenIDConnectProviderRequestRequestTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyRequestRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyVersionRequestRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRolePermissionsBoundaryRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRolePolicyRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoleRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSAMLProviderRequestRequestTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSSHPublicKeyRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServerCertificateRequestRequestTypeDef

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceLinkedRoleRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceLinkedRoleResponseTypeDef

### DeletionTaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteServiceSpecificCredentialRequestRequestTypeDef

### ServiceSpecificCredentialId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# DeleteSigningCertificateRequestRequestTypeDef

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# DeleteUserPermissionsBoundaryRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserPolicyRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVirtualMFADeviceRequestRequestTypeDef

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes


# DeletionTaskFailureReasonTypeTypeDef

### Reason
- **Type**: typing.Optional[str]

### RoleUsageList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.RoleUsageTypeTypeDef]]


# DetachGroupPolicyRequestGroupDetachPolicyTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachGroupPolicyRequestPolicyDetachGroupTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachGroupPolicyRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachRolePolicyRequestPolicyDetachRoleTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachRolePolicyRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachRolePolicyRequestRoleDetachPolicyTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachUserPolicyRequestPolicyDetachUserTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachUserPolicyRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachUserPolicyRequestUserDetachPolicyTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableMFADeviceRequestMfaDeviceAssociateTypeDef

### AuthenticationCode1
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationCode2
- **Type**: <class 'str'>
- **Required**: Yes


# EnableMFADeviceRequestRequestTypeDef

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


# EnableMFADeviceRequestUserEnableMfaTypeDef

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationCode1
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationCode2
- **Type**: <class 'str'>
- **Required**: Yes


# EntityDetailsTypeDef

### EntityInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.EntityInfoTypeDef'>
- **Required**: Yes

### LastAuthenticated
- **Type**: typing.Optional[datetime.datetime]


# EntityInfoTypeDef

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


# ErrorDetailsTypeDef

### Message
- **Type**: <class 'str'>
- **Required**: Yes

### Code
- **Type**: <class 'str'>
- **Required**: Yes


# EvaluationResultTypeDef

### EvalActionName
- **Type**: <class 'str'>
- **Required**: Yes

### EvalDecision
- **Type**: typing.Literal['allowed', 'explicitDeny', 'implicitDeny']
- **Required**: Yes

### EvalResourceName
- **Type**: typing.Optional[str]

### MatchedStatements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.StatementTypeDef]]

### MissingContextValues
- **Type**: typing.Optional[typing.List[str]]

### OrganizationsDecisionDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.OrganizationsDecisionDetailTypeDef]

### PermissionsBoundaryDecisionDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PermissionsBoundaryDecisionDetailTypeDef]

### EvalDecisionDetails
- **Type**: typing.Optional[typing.Dict[str, typing.Literal['allowed', 'explicitDeny', 'implicitDeny']]]

### ResourceSpecificResults
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.ResourceSpecificResultTypeDef]]


# GenerateCredentialReportResponseTypeDef

### State
- **Type**: typing.Literal['COMPLETE', 'INPROGRESS', 'STARTED']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateOrganizationsAccessReportRequestRequestTypeDef

### EntityPath
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationsPolicyId
- **Type**: typing.Optional[str]


# GenerateOrganizationsAccessReportResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GenerateServiceLastAccessedDetailsRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Granularity
- **Type**: typing.Optional[typing.Literal['ACTION_LEVEL', 'SERVICE_LEVEL']]


# GenerateServiceLastAccessedDetailsResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccessKeyLastUsedRequestRequestTypeDef

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# GetAccessKeyLastUsedResponseTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessKeyLastUsed
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.AccessKeyLastUsedTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccountAuthorizationDetailsRequestGetAccountAuthorizationDetailsPaginateTypeDef

### Filter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWSManagedPolicy', 'Group', 'LocalManagedPolicy', 'Role', 'User']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# GetAccountAuthorizationDetailsRequestRequestTypeDef

### Filter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWSManagedPolicy', 'Group', 'LocalManagedPolicy', 'Role', 'User']]]

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# GetAccountAuthorizationDetailsResponseTypeDef

### UserDetailList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.UserDetailTypeDef]
- **Required**: Yes

### GroupDetailList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.GroupDetailTypeDef]
- **Required**: Yes

### RoleDetailList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.RoleDetailTypeDef]
- **Required**: Yes

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.ManagedPolicyDetailTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccountPasswordPolicyResponseTypeDef

### PasswordPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.PasswordPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetAccountSummaryResponseTypeDef

### SummaryMap
- **Type**: typing.Dict[typing.Literal['AccessKeysPerUserQuota', 'AccountAccessKeysPresent', 'AccountMFAEnabled', 'AccountSigningCertificatesPresent', 'AttachedPoliciesPerGroupQuota', 'AttachedPoliciesPerRoleQuota', 'AttachedPoliciesPerUserQuota', 'GlobalEndpointTokenVersion', 'GroupPolicySizeQuota', 'Groups', 'GroupsPerUserQuota', 'GroupsQuota', 'MFADevices', 'MFADevicesInUse', 'Policies', 'PoliciesQuota', 'PolicySizeQuota', 'PolicyVersionsInUse', 'PolicyVersionsInUseQuota', 'ServerCertificates', 'ServerCertificatesQuota', 'SigningCertificatesPerUserQuota', 'UserPolicySizeQuota', 'Users', 'UsersQuota', 'VersionsPerPolicyQuota'], int]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContextKeysForCustomPolicyRequestRequestTypeDef

### PolicyInputList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# GetContextKeysForPolicyResponseTypeDef

### ContextKeyNames
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContextKeysForPrincipalPolicyRequestRequestTypeDef

### PolicySourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyInputList
- **Type**: typing.Optional[typing.Sequence[str]]


# GetCredentialReportResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupPolicyRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# GetGroupPolicyResponseTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: typing.Union[str, aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentDictTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupRequestGetGroupPaginateTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# GetGroupRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# GetGroupResponseTypeDef

### Group
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.GroupTypeDef'>
- **Required**: Yes

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.UserTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetInstanceProfileRequestInstanceProfileExistsWaitTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.WaiterConfigTypeDef]


# GetInstanceProfileRequestRequestTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceProfileResponseTypeDef

### InstanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.InstanceProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLoginProfileRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# GetLoginProfileResponseTypeDef

### LoginProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.LoginProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMFADeviceRequestRequestTypeDef

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# GetMFADeviceResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOpenIDConnectProviderRequestRequestTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetOpenIDConnectProviderResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOrganizationsAccessReportRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### SortKey
- **Type**: typing.Optional[typing.Literal['LAST_AUTHENTICATED_TIME_ASCENDING', 'LAST_AUTHENTICATED_TIME_DESCENDING', 'SERVICE_NAMESPACE_ASCENDING', 'SERVICE_NAMESPACE_DESCENDING']]


# GetOrganizationsAccessReportResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.AccessDetailTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ErrorDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyRequestPolicyExistsWaitTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.WaiterConfigTypeDef]


# GetPolicyRequestRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyResponseTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.PolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyVersionRequestRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyVersionResponseTypeDef

### PolicyVersion
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.PolicyVersionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRolePolicyRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRolePolicyResponseTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: typing.Union[str, aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentDictTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRoleRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRoleRequestRoleExistsWaitTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.WaiterConfigTypeDef]


# GetRoleResponseTypeDef

### Role
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.RoleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSAMLProviderRequestRequestTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetSAMLProviderResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSSHPublicKeyRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Encoding
- **Type**: typing.Literal['PEM', 'SSH']
- **Required**: Yes


# GetSSHPublicKeyResponseTypeDef

### SSHPublicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.SSHPublicKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServerCertificateRequestRequestTypeDef

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes


# GetServerCertificateResponseTypeDef

### ServerCertificate
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ServerCertificateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceLastAccessedDetailsRequestRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# GetServiceLastAccessedDetailsResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.ServiceLastAccessedTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ErrorDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef

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


# GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.EntityDetailsTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Error
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ErrorDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetServiceLinkedRoleDeletionStatusRequestRequestTypeDef

### DeletionTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetServiceLinkedRoleDeletionStatusResponseTypeDef

### Status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'NOT_STARTED', 'SUCCEEDED']
- **Required**: Yes

### Reason
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.DeletionTaskFailureReasonTypeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserPolicyRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# GetUserPolicyResponseTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: typing.Union[str, aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentDictTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserRequestRequestTypeDef

### UserName
- **Type**: typing.Optional[str]


# GetUserRequestUserExistsWaitTypeDef

### UserName
- **Type**: typing.Optional[str]

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.WaiterConfigTypeDef]


# GetUserResponseTypeDef

### User
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.UserTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupDetailTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.PolicyDetailTypeDef]]

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.AttachedPolicyTypeDef]]


# GroupTypeDef

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


# InstanceProfileTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.RoleTypeDef]
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# ListAccessKeysRequestListAccessKeysPaginateTypeDef

### UserName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListAccessKeysRequestRequestTypeDef

### UserName
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAccessKeysResponseTypeDef

### AccessKeyMetadata
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.AccessKeyMetadataTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAccountAliasesRequestListAccountAliasesPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListAccountAliasesRequestRequestTypeDef

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAccountAliasesResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAttachedGroupPoliciesRequestListAttachedGroupPoliciesPaginateTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListAttachedGroupPoliciesRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAttachedGroupPoliciesResponseTypeDef

### AttachedPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.AttachedPolicyTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAttachedRolePoliciesRequestListAttachedRolePoliciesPaginateTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListAttachedRolePoliciesRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAttachedRolePoliciesResponseTypeDef

### AttachedPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.AttachedPolicyTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAttachedUserPoliciesRequestListAttachedUserPoliciesPaginateTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListAttachedUserPoliciesRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListAttachedUserPoliciesResponseTypeDef

### AttachedPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.AttachedPolicyTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListEntitiesForPolicyRequestListEntitiesForPolicyPaginateTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListEntitiesForPolicyRequestRequestTypeDef

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


# ListEntitiesForPolicyResponseTypeDef

### PolicyGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.PolicyGroupTypeDef]
- **Required**: Yes

### PolicyUsers
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.PolicyUserTypeDef]
- **Required**: Yes

### PolicyRoles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.PolicyRoleTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroupPoliciesRequestListGroupPoliciesPaginateTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListGroupPoliciesRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListGroupPoliciesResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroupsForUserRequestListGroupsForUserPaginateTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListGroupsForUserRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListGroupsForUserResponseTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.GroupTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGroupsRequestListGroupsPaginateTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListGroupsRequestRequestTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListGroupsResponseTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.GroupTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInstanceProfileTagsRequestListInstanceProfileTagsPaginateTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListInstanceProfileTagsRequestRequestTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListInstanceProfileTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInstanceProfilesForRoleRequestListInstanceProfilesForRolePaginateTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListInstanceProfilesForRoleRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListInstanceProfilesForRoleResponseTypeDef

### InstanceProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.InstanceProfileTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListInstanceProfilesRequestRequestTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListInstanceProfilesResponseTypeDef

### InstanceProfiles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.InstanceProfileTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMFADeviceTagsRequestListMFADeviceTagsPaginateTypeDef

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListMFADeviceTagsRequestRequestTypeDef

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListMFADeviceTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListMFADevicesRequestListMFADevicesPaginateTypeDef

### UserName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListMFADevicesRequestRequestTypeDef

### UserName
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListMFADevicesResponseTypeDef

### MFADevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.MFADeviceTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOpenIDConnectProviderTagsRequestListOpenIDConnectProviderTagsPaginateTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListOpenIDConnectProviderTagsRequestRequestTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListOpenIDConnectProviderTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOpenIDConnectProvidersResponseTypeDef

### OpenIDConnectProviderList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.OpenIDConnectProviderListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPoliciesGrantingServiceAccessEntryTypeDef

### ServiceNamespace
- **Type**: typing.Optional[str]

### Policies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.PolicyGrantingServiceAccessTypeDef]]


# ListPoliciesGrantingServiceAccessRequestRequestTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ServiceNamespaces
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]


# ListPoliciesGrantingServiceAccessResponseTypeDef

### PoliciesGrantingServiceAccess
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.ListPoliciesGrantingServiceAccessEntryTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPoliciesRequestListPoliciesPaginateTypeDef

### Scope
- **Type**: typing.Optional[typing.Literal['AWS', 'All', 'Local']]

### OnlyAttached
- **Type**: typing.Optional[bool]

### PathPrefix
- **Type**: typing.Optional[str]

### PolicyUsageFilter
- **Type**: typing.Optional[typing.Literal['PermissionsBoundary', 'PermissionsPolicy']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListPoliciesRequestRequestTypeDef

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


# ListPoliciesResponseTypeDef

### Policies
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.PolicyTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPolicyTagsRequestListPolicyTagsPaginateTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListPolicyTagsRequestRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListPolicyTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPolicyVersionsRequestListPolicyVersionsPaginateTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListPolicyVersionsRequestRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListPolicyVersionsResponseTypeDef

### Versions
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.PolicyVersionTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRolePoliciesRequestListRolePoliciesPaginateTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListRolePoliciesRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListRolePoliciesResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRoleTagsRequestListRoleTagsPaginateTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListRoleTagsRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListRoleTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRolesRequestListRolesPaginateTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListRolesRequestRequestTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListRolesResponseTypeDef

### Roles
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.RoleTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSAMLProviderTagsRequestListSAMLProviderTagsPaginateTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListSAMLProviderTagsRequestRequestTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListSAMLProviderTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSAMLProvidersResponseTypeDef

### SAMLProviderList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.SAMLProviderListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSSHPublicKeysRequestListSSHPublicKeysPaginateTypeDef

### UserName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListSSHPublicKeysRequestRequestTypeDef

### UserName
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListSSHPublicKeysResponseTypeDef

### SSHPublicKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.SSHPublicKeyMetadataTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServerCertificateTagsRequestListServerCertificateTagsPaginateTypeDef

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListServerCertificateTagsRequestRequestTypeDef

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListServerCertificateTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServerCertificatesRequestListServerCertificatesPaginateTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListServerCertificatesRequestRequestTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListServerCertificatesResponseTypeDef

### ServerCertificateMetadataList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.ServerCertificateMetadataTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListServiceSpecificCredentialsRequestRequestTypeDef

### UserName
- **Type**: typing.Optional[str]

### ServiceName
- **Type**: typing.Optional[str]


# ListServiceSpecificCredentialsResponseTypeDef

### ServiceSpecificCredentials
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.ServiceSpecificCredentialMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSigningCertificatesRequestListSigningCertificatesPaginateTypeDef

### UserName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListSigningCertificatesRequestRequestTypeDef

### UserName
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListSigningCertificatesResponseTypeDef

### Certificates
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.SigningCertificateTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUserPoliciesRequestListUserPoliciesPaginateTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListUserPoliciesRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListUserPoliciesResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUserTagsRequestListUserTagsPaginateTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListUserTagsRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListUserTagsResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUsersRequestListUsersPaginateTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListUsersRequestRequestTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListUsersResponseTypeDef

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.UserTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVirtualMFADevicesRequestListVirtualMFADevicesPaginateTypeDef

### AssignmentStatus
- **Type**: typing.Optional[typing.Literal['Any', 'Assigned', 'Unassigned']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListVirtualMFADevicesRequestRequestTypeDef

### AssignmentStatus
- **Type**: typing.Optional[typing.Literal['Any', 'Assigned', 'Unassigned']]

### Marker
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]


# ListVirtualMFADevicesResponseTypeDef

### VirtualMFADevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.VirtualMFADeviceTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LoginProfileTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### CreateDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# MFADeviceTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### EnableDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# ManagedPolicyDetailTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.PolicyVersionTypeDef]]


# OpenIDConnectProviderListEntryTypeDef

### Arn
- **Type**: typing.Optional[str]


# OrganizationsDecisionDetailTypeDef

### AllowedByOrganizations
- **Type**: typing.Optional[bool]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PasswordPolicyTypeDef

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


# PermissionsBoundaryDecisionDetailTypeDef

### AllowedByPermissionsBoundary
- **Type**: typing.Optional[bool]


# PolicyDetailTypeDef

### PolicyName
- **Type**: typing.Optional[str]

### PolicyDocument
- **Type**: typing.Union[str, aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentDictTypeDef, NoneType]


# PolicyDocumentDictTypeDef

### Version
- **Type**: <class 'str'>
- **Required**: Yes

### Statement
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentStatementTypeDef]
- **Required**: Yes


# PolicyDocumentStatementTypeDef

### Effect
- **Type**: <class 'str'>
- **Required**: Yes

### Resource
- **Type**: typing.Union[str, typing.List[str]]
- **Required**: Yes

### Sid
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: typing.Union[str, typing.List[str]]
- **Required**: Yes


# PolicyGrantingServiceAccessTypeDef

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


# PolicyGroupTypeDef

### GroupName
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[str]


# PolicyRoleTypeDef

### RoleName
- **Type**: typing.Optional[str]

### RoleId
- **Type**: typing.Optional[str]


# PolicyTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# PolicyUserTypeDef

### UserName
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]


# PolicyVersionTypeDef

### Document
- **Type**: typing.Union[str, aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentDictTypeDef, NoneType]

### VersionId
- **Type**: typing.Optional[str]

### IsDefaultVersion
- **Type**: typing.Optional[bool]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]


# PositionTypeDef

### Line
- **Type**: typing.Optional[int]

### Column
- **Type**: typing.Optional[int]


# PutGroupPolicyRequestGroupCreatePolicyTypeDef

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutGroupPolicyRequestGroupPolicyPutTypeDef

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutGroupPolicyRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutRolePermissionsBoundaryRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionsBoundary
- **Type**: <class 'str'>
- **Required**: Yes


# PutRolePolicyRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutRolePolicyRequestRolePolicyPutTypeDef

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutUserPermissionsBoundaryRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionsBoundary
- **Type**: <class 'str'>
- **Required**: Yes


# PutUserPolicyRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutUserPolicyRequestUserCreatePolicyTypeDef

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutUserPolicyRequestUserPolicyPutTypeDef

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveClientIDFromOpenIDConnectProviderRequestRequestTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientID
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveRoleFromInstanceProfileRequestRequestTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveUserFromGroupRequestGroupRemoveUserTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveUserFromGroupRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveUserFromGroupRequestUserRemoveGroupTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# ResetServiceSpecificCredentialRequestRequestTypeDef

### ServiceSpecificCredentialId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# ResetServiceSpecificCredentialResponseTypeDef

### ServiceSpecificCredential
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ServiceSpecificCredentialTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResourceSpecificResultTypeDef

### EvalResourceName
- **Type**: <class 'str'>
- **Required**: Yes

### EvalResourceDecision
- **Type**: typing.Literal['allowed', 'explicitDeny', 'implicitDeny']
- **Required**: Yes

### MatchedStatements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.StatementTypeDef]]

### MissingContextValues
- **Type**: typing.Optional[typing.List[str]]

### EvalDecisionDetails
- **Type**: typing.Optional[typing.Dict[str, typing.Literal['allowed', 'explicitDeny', 'implicitDeny']]]

### PermissionsBoundaryDecisionDetail
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PermissionsBoundaryDecisionDetailTypeDef]


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


# ResyncMFADeviceRequestMfaDeviceResyncTypeDef

### AuthenticationCode1
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationCode2
- **Type**: <class 'str'>
- **Required**: Yes


# ResyncMFADeviceRequestRequestTypeDef

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


# RoleDetailTypeDef

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
- **Type**: typing.Union[str, aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentDictTypeDef, NoneType]

### InstanceProfileList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.InstanceProfileTypeDef]]

### RolePolicyList
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.PolicyDetailTypeDef]]

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.AttachedPolicyTypeDef]]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.AttachedPermissionsBoundaryTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]

### RoleLastUsed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.RoleLastUsedTypeDef]


# RoleLastUsedResponseTypeDef

### LastUsedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RoleLastUsedTypeDef

### LastUsedDate
- **Type**: typing.Optional[datetime.datetime]

### Region
- **Type**: typing.Optional[str]


# RoleTypeDef

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
- **Type**: typing.Union[str, aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentDictTypeDef, NoneType]

### Description
- **Type**: typing.Optional[str]

### MaxSessionDuration
- **Type**: typing.Optional[int]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.AttachedPermissionsBoundaryTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]

### RoleLastUsed
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.RoleLastUsedTypeDef]


# RoleUsageTypeTypeDef

### Region
- **Type**: typing.Optional[str]

### Resources
- **Type**: typing.Optional[typing.List[str]]


# SAMLProviderListEntryTypeDef

### Arn
- **Type**: typing.Optional[str]

### ValidUntil
- **Type**: typing.Optional[datetime.datetime]

### CreateDate
- **Type**: typing.Optional[datetime.datetime]


# SSHPublicKeyMetadataTypeDef

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


# SSHPublicKeyTypeDef

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


# ServerCertificateMetadataResponseTypeDef

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
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Expiration
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ServerCertificateMetadataTypeDef

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


# ServerCertificateTypeDef

### ServerCertificateMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ServerCertificateMetadataTypeDef'>
- **Required**: Yes

### CertificateBody
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateChain
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# ServiceLastAccessedTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.TrackedActionLastAccessedTypeDef]]


# ServiceSpecificCredentialMetadataTypeDef

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


# ServiceSpecificCredentialTypeDef

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


# SetDefaultPolicyVersionRequestRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes


# SetSecurityTokenServicePreferencesRequestRequestTypeDef

### GlobalEndpointTokenVersion
- **Type**: typing.Literal['v1Token', 'v2Token']
- **Required**: Yes


# SigningCertificateTypeDef

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


# SimulateCustomPolicyRequestRequestTypeDef

### PolicyInputList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ActionNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PermissionsBoundaryPolicyInputList
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourcePolicy
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[str]

### CallerArn
- **Type**: typing.Optional[str]

### ContextEntries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.ContextEntryTypeDef]]

### ResourceHandlingOption
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# SimulateCustomPolicyRequestSimulateCustomPolicyPaginateTypeDef

### PolicyInputList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ActionNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PermissionsBoundaryPolicyInputList
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourcePolicy
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[str]

### CallerArn
- **Type**: typing.Optional[str]

### ContextEntries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.ContextEntryTypeDef]]

### ResourceHandlingOption
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# SimulatePolicyResponseTypeDef

### EvaluationResults
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.EvaluationResultTypeDef]
- **Required**: Yes

### IsTruncated
- **Type**: <class 'bool'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SimulatePrincipalPolicyRequestRequestTypeDef

### PolicySourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActionNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PolicyInputList
- **Type**: typing.Optional[typing.Sequence[str]]

### PermissionsBoundaryPolicyInputList
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourcePolicy
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[str]

### CallerArn
- **Type**: typing.Optional[str]

### ContextEntries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.ContextEntryTypeDef]]

### ResourceHandlingOption
- **Type**: typing.Optional[str]

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# SimulatePrincipalPolicyRequestSimulatePrincipalPolicyPaginateTypeDef

### PolicySourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ActionNames
- **Type**: typing.Sequence[str]
- **Required**: Yes

### PolicyInputList
- **Type**: typing.Optional[typing.Sequence[str]]

### PermissionsBoundaryPolicyInputList
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourceArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ResourcePolicy
- **Type**: typing.Optional[str]

### ResourceOwner
- **Type**: typing.Optional[str]

### CallerArn
- **Type**: typing.Optional[str]

### ContextEntries
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.ContextEntryTypeDef]]

### ResourceHandlingOption
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# StatementTypeDef

### SourcePolicyId
- **Type**: typing.Optional[str]

### SourcePolicyType
- **Type**: typing.Optional[typing.Literal['aws-managed', 'group', 'none', 'resource', 'role', 'user', 'user-managed']]

### StartPosition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PositionTypeDef]

### EndPosition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PositionTypeDef]


# TagInstanceProfileRequestRequestTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TagMFADeviceRequestRequestTypeDef

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TagOpenIDConnectProviderRequestRequestTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TagPolicyRequestRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TagRoleRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TagSAMLProviderRequestRequestTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TagServerCertificateRequestRequestTypeDef

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagUserRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TrackedActionLastAccessedTypeDef

### ActionName
- **Type**: typing.Optional[str]

### LastAccessedEntity
- **Type**: typing.Optional[str]

### LastAccessedTime
- **Type**: typing.Optional[datetime.datetime]

### LastAccessedRegion
- **Type**: typing.Optional[str]


# UntagInstanceProfileRequestRequestTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagMFADeviceRequestRequestTypeDef

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagOpenIDConnectProviderRequestRequestTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagPolicyRequestRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagRoleRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagSAMLProviderRequestRequestTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagServerCertificateRequestRequestTypeDef

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagUserRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAccessKeyRequestAccessKeyActivateTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UpdateAccessKeyRequestAccessKeyDeactivateTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UpdateAccessKeyRequestAccessKeyPairActivateTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UpdateAccessKeyRequestRequestTypeDef

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef

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


# UpdateAccountPasswordPolicyRequestRequestTypeDef

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


# UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef

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


# UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAssumeRolePolicyRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateGroupRequestGroupUpdateTypeDef

### NewPath
- **Type**: typing.Optional[str]

### NewGroupName
- **Type**: typing.Optional[str]


# UpdateGroupRequestRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### NewPath
- **Type**: typing.Optional[str]

### NewGroupName
- **Type**: typing.Optional[str]


# UpdateLoginProfileRequestLoginProfileUpdateTypeDef

### Password
- **Type**: typing.Optional[str]

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# UpdateLoginProfileRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: typing.Optional[str]

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# UpdateOpenIDConnectProviderThumbprintRequestRequestTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ThumbprintList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateRoleDescriptionRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateRoleDescriptionResponseTypeDef

### Role
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.RoleTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateRoleRequestRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### MaxSessionDuration
- **Type**: typing.Optional[int]


# UpdateSAMLProviderRequestRequestTypeDef

### SAMLMetadataDocument
- **Type**: <class 'str'>
- **Required**: Yes

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSAMLProviderRequestSamlProviderUpdateTypeDef

### SAMLMetadataDocument
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateSAMLProviderResponseTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSSHPublicKeyRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes


# UpdateServerCertificateRequestRequestTypeDef

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### NewPath
- **Type**: typing.Optional[str]

### NewServerCertificateName
- **Type**: typing.Optional[str]


# UpdateServerCertificateRequestServerCertificateUpdateTypeDef

### NewPath
- **Type**: typing.Optional[str]

### NewServerCertificateName
- **Type**: typing.Optional[str]


# UpdateServiceSpecificCredentialRequestRequestTypeDef

### ServiceSpecificCredentialId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# UpdateSigningCertificateRequestRequestTypeDef

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# UpdateSigningCertificateRequestSigningCertificateActivateTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Inactive']]


# UpdateUserRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### NewPath
- **Type**: typing.Optional[str]

### NewUserName
- **Type**: typing.Optional[str]


# UpdateUserRequestUserUpdateTypeDef

### NewPath
- **Type**: typing.Optional[str]

### NewUserName
- **Type**: typing.Optional[str]


# UploadSSHPublicKeyRequestRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKeyBody
- **Type**: <class 'str'>
- **Required**: Yes


# UploadSSHPublicKeyResponseTypeDef

### SSHPublicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.SSHPublicKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UploadServerCertificateRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# UploadServerCertificateResponseTypeDef

### ServerCertificateMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ServerCertificateMetadataTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UploadSigningCertificateRequestRequestTypeDef

### CertificateBody
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef

### CertificateBody
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# UploadSigningCertificateResponseTypeDef

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.SigningCertificateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserDetailTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.PolicyDetailTypeDef]]

### GroupList
- **Type**: typing.Optional[typing.List[str]]

### AttachedManagedPolicies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.AttachedPolicyTypeDef]]

### PermissionsBoundary
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.AttachedPermissionsBoundaryTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# UserResponseTypeDef

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
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### PermissionsBoundary
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.AttachedPermissionsBoundaryTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UserTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.AttachedPermissionsBoundaryTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# VirtualMFADeviceTypeDef

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Base32StringSeed
- **Type**: typing.Optional[bytes]

### QRCodePNG
- **Type**: typing.Optional[bytes]

### User
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.UserTypeDef]

### EnableDate
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


