# Iam Classes

# AccessDetailTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AccessKeyLastUsedTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# AddClientIDToOpenIDConnectProviderRequestTypeDef

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


# AddRoleToInstanceProfileRequestTypeDef

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


# AddUserToGroupRequestTypeDef

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


# AttachGroupPolicyRequestTypeDef

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


# AttachRolePolicyRequestRoleAttachPolicyTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachRolePolicyRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# AttachUserPolicyRequestPolicyAttachUserTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# AttachUserPolicyRequestTypeDef

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

# ChangePasswordRequestServiceResourceChangePasswordTypeDef

### OldPassword
- **Type**: <class 'str'>
- **Required**: Yes

### NewPassword
- **Type**: <class 'str'>
- **Required**: Yes


# ChangePasswordRequestTypeDef

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


# CreateAccessKeyRequestTypeDef

### UserName
- **Type**: typing.Optional[str]


# CreateAccessKeyResponseTypeDef

### AccessKey
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.AccessKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef

### AccountAlias
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAccountAliasRequestTypeDef

### AccountAlias
- **Type**: <class 'str'>
- **Required**: Yes


# CreateGroupRequestGroupCreateTypeDef

### Path
- **Type**: typing.Optional[str]


# CreateGroupRequestServiceResourceCreateGroupTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]


# CreateGroupRequestTypeDef

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


# CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateInstanceProfileRequestTypeDef

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
- **Type**: typing.Optional[str]

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# CreateLoginProfileRequestTypeDef

### UserName
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# CreateLoginProfileRequestUserCreateLoginProfileTypeDef

### Password
- **Type**: typing.Optional[str]

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# CreateLoginProfileResponseTypeDef

### LoginProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.LoginProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOpenIDConnectProviderRequestTypeDef

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


# CreatePolicyRequestTypeDef

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


# CreatePolicyVersionRequestTypeDef

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


# CreateRoleRequestTypeDef

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


# CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef

### SAMLMetadataDocument
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]

### AssertionEncryptionMode
- **Type**: typing.Optional[typing.Literal['Allowed', 'Required']]

### AddPrivateKey
- **Type**: typing.Optional[str]


# CreateSAMLProviderRequestTypeDef

### SAMLMetadataDocument
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]

### AssertionEncryptionMode
- **Type**: typing.Optional[typing.Literal['Allowed', 'Required']]

### AddPrivateKey
- **Type**: typing.Optional[str]


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


# CreateServiceLinkedRoleRequestTypeDef

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


# CreateServiceSpecificCredentialResponseTypeDef

### ServiceSpecificCredential
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ServiceSpecificCredentialTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# CreateUserRequestTypeDef

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


# CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef

### VirtualMFADeviceName
- **Type**: <class 'str'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]]


# CreateVirtualMFADeviceRequestTypeDef

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


# DeactivateMFADeviceRequestTypeDef

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# DeleteAccessKeyRequestTypeDef

### AccessKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# DeleteAccountAliasRequestTypeDef

### AccountAlias
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupPolicyRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteInstanceProfileRequestTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLoginProfileRequestTypeDef

### UserName
- **Type**: typing.Optional[str]


# DeleteOpenIDConnectProviderRequestTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePolicyVersionRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRolePermissionsBoundaryRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRolePolicyRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRoleRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSAMLProviderRequestTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSSHPublicKeyRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServerCertificateRequestTypeDef

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteServiceLinkedRoleRequestTypeDef

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


# DeleteServiceSpecificCredentialRequestTypeDef

### ServiceSpecificCredentialId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# DeleteSigningCertificateRequestTypeDef

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# DeleteUserPermissionsBoundaryRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserPolicyRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVirtualMFADeviceRequestTypeDef

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


# DetachGroupPolicyRequestTypeDef

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


# DetachRolePolicyRequestRoleDetachPolicyTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachRolePolicyRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# DetachUserPolicyRequestPolicyDetachUserTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes


# DetachUserPolicyRequestTypeDef

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


# DisableOrganizationsRootCredentialsManagementResponseTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledFeatures
- **Type**: typing.List[typing.Literal['RootCredentialsManagement', 'RootSessions']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisableOrganizationsRootSessionsResponseTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledFeatures
- **Type**: typing.List[typing.Literal['RootCredentialsManagement', 'RootSessions']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
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


# EnableMFADeviceRequestTypeDef

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


# EnableOrganizationsRootCredentialsManagementResponseTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledFeatures
- **Type**: typing.List[typing.Literal['RootCredentialsManagement', 'RootSessions']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EnableOrganizationsRootSessionsResponseTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledFeatures
- **Type**: typing.List[typing.Literal['RootCredentialsManagement', 'RootSessions']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EntityDetailsTypeDef

### EntityInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.EntityInfoTypeDef'>
- **Required**: Yes

### LastAuthenticated
- **Type**: typing.Optional[datetime.datetime]


# EntityInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# GenerateOrganizationsAccessReportRequestTypeDef

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


# GenerateServiceLastAccessedDetailsRequestTypeDef

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


# GetAccessKeyLastUsedRequestTypeDef

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


# GetAccountAuthorizationDetailsRequestPaginateTypeDef

### Filter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AWSManagedPolicy', 'Group', 'LocalManagedPolicy', 'Role', 'User']]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# GetAccountAuthorizationDetailsRequestTypeDef

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
- **Type**: typing.Dict[typing.Literal['AccessKeysPerUserQuota', 'AccountAccessKeysPresent', 'AccountMFAEnabled', 'AccountPasswordPresent', 'AccountSigningCertificatesPresent', 'AttachedPoliciesPerGroupQuota', 'AttachedPoliciesPerRoleQuota', 'AttachedPoliciesPerUserQuota', 'GlobalEndpointTokenVersion', 'GroupPolicySizeQuota', 'Groups', 'GroupsPerUserQuota', 'GroupsQuota', 'MFADevices', 'MFADevicesInUse', 'Policies', 'PoliciesQuota', 'PolicySizeQuota', 'PolicyVersionsInUse', 'PolicyVersionsInUseQuota', 'ServerCertificates', 'ServerCertificatesQuota', 'SigningCertificatesPerUserQuota', 'UserPolicySizeQuota', 'Users', 'UsersQuota', 'VersionsPerPolicyQuota'], int]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetContextKeysForCustomPolicyRequestTypeDef

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


# GetContextKeysForPrincipalPolicyRequestTypeDef

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


# GetGroupPolicyRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetGroupRequestPaginateTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# GetGroupRequestTypeDef

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


# GetInstanceProfileRequestTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes


# GetInstanceProfileRequestWaitTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.WaiterConfigTypeDef]


# GetInstanceProfileResponseTypeDef

### InstanceProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.InstanceProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetLoginProfileRequestTypeDef

### UserName
- **Type**: typing.Optional[str]


# GetLoginProfileResponseTypeDef

### LoginProfile
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.LoginProfileTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMFADeviceRequestTypeDef

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


# GetOpenIDConnectProviderRequestTypeDef

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


# GetOrganizationsAccessReportRequestTypeDef

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


# GetPolicyRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPolicyRequestWaitTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.WaiterConfigTypeDef]


# GetPolicyResponseTypeDef

### Policy
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.PolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPolicyVersionRequestTypeDef

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


# GetRolePolicyRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRoleRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes


# GetRoleRequestWaitTypeDef

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


# GetSAMLProviderRequestTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetSAMLProviderResponseTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes

### AssertionEncryptionMode
- **Type**: typing.Literal['Allowed', 'Required']
- **Required**: Yes

### PrivateKeyList
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.SAMLPrivateKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSSHPublicKeyRequestTypeDef

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


# GetServerCertificateRequestTypeDef

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


# GetServiceLastAccessedDetailsRequestTypeDef

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


# GetServiceLastAccessedDetailsWithEntitiesRequestTypeDef

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


# GetServiceLinkedRoleDeletionStatusRequestTypeDef

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


# GetUserPolicyRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetUserRequestTypeDef

### UserName
- **Type**: typing.Optional[str]


# GetUserRequestWaitTypeDef

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


# ListAccessKeysRequestPaginateTypeDef

### UserName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListAccessKeysRequestTypeDef

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


# ListAccountAliasesRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListAccountAliasesRequestTypeDef

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


# ListAttachedGroupPoliciesRequestPaginateTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListAttachedGroupPoliciesRequestTypeDef

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


# ListAttachedRolePoliciesRequestPaginateTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListAttachedRolePoliciesRequestTypeDef

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


# ListAttachedUserPoliciesRequestPaginateTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListAttachedUserPoliciesRequestTypeDef

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


# ListEntitiesForPolicyRequestPaginateTypeDef

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


# ListEntitiesForPolicyRequestTypeDef

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


# ListGroupPoliciesRequestPaginateTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListGroupPoliciesRequestTypeDef

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


# ListGroupsForUserRequestPaginateTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListGroupsForUserRequestTypeDef

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


# ListGroupsRequestPaginateTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListGroupsRequestTypeDef

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


# ListInstanceProfileTagsRequestPaginateTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListInstanceProfileTagsRequestTypeDef

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


# ListInstanceProfilesForRoleRequestPaginateTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListInstanceProfilesForRoleRequestTypeDef

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


# ListInstanceProfilesRequestPaginateTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListInstanceProfilesRequestTypeDef

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


# ListMFADeviceTagsRequestPaginateTypeDef

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListMFADeviceTagsRequestTypeDef

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


# ListMFADevicesRequestPaginateTypeDef

### UserName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListMFADevicesRequestTypeDef

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


# ListOpenIDConnectProviderTagsRequestPaginateTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListOpenIDConnectProviderTagsRequestTypeDef

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


# ListOrganizationsFeaturesResponseTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledFeatures
- **Type**: typing.List[typing.Literal['RootCredentialsManagement', 'RootSessions']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPoliciesGrantingServiceAccessEntryTypeDef

### ServiceNamespace
- **Type**: typing.Optional[str]

### Policies
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.iam_classes.PolicyGrantingServiceAccessTypeDef]]


# ListPoliciesGrantingServiceAccessRequestTypeDef

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


# ListPoliciesRequestPaginateTypeDef

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


# ListPoliciesRequestTypeDef

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


# ListPolicyTagsRequestPaginateTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListPolicyTagsRequestTypeDef

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


# ListPolicyVersionsRequestPaginateTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListPolicyVersionsRequestTypeDef

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


# ListRolePoliciesRequestPaginateTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListRolePoliciesRequestTypeDef

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


# ListRoleTagsRequestPaginateTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListRoleTagsRequestTypeDef

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


# ListRolesRequestPaginateTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListRolesRequestTypeDef

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


# ListSAMLProviderTagsRequestPaginateTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListSAMLProviderTagsRequestTypeDef

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


# ListSSHPublicKeysRequestPaginateTypeDef

### UserName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListSSHPublicKeysRequestTypeDef

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


# ListServerCertificateTagsRequestPaginateTypeDef

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListServerCertificateTagsRequestTypeDef

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


# ListServerCertificatesRequestPaginateTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListServerCertificatesRequestTypeDef

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


# ListServiceSpecificCredentialsResponseTypeDef

### ServiceSpecificCredentials
- **Type**: typing.List[aws_resource_validator.pydantic_models.iam_classes.ServiceSpecificCredentialMetadataTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSigningCertificatesRequestPaginateTypeDef

### UserName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListSigningCertificatesRequestTypeDef

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


# ListUserPoliciesRequestPaginateTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListUserPoliciesRequestTypeDef

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


# ListUserTagsRequestPaginateTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListUserTagsRequestTypeDef

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


# ListUsersRequestPaginateTypeDef

### PathPrefix
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListUsersRequestTypeDef

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


# ListVirtualMFADevicesRequestPaginateTypeDef

### AssignmentStatus
- **Type**: typing.Optional[typing.Literal['Any', 'Assigned', 'Unassigned']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PaginatorConfigTypeDef]


# ListVirtualMFADevicesRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentTypeDef]


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


# PolicyDocumentTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentTypeDef]

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


# PutGroupPolicyRequestTypeDef

### GroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutRolePermissionsBoundaryRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionsBoundary
- **Type**: <class 'str'>
- **Required**: Yes


# PutRolePolicyRequestRolePolicyPutTypeDef

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutRolePolicyRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyName
- **Type**: <class 'str'>
- **Required**: Yes

### PolicyDocument
- **Type**: <class 'str'>
- **Required**: Yes


# PutUserPermissionsBoundaryRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionsBoundary
- **Type**: <class 'str'>
- **Required**: Yes


# PutUserPolicyRequestTypeDef

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


# RemoveClientIDFromOpenIDConnectProviderRequestTypeDef

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


# RemoveRoleFromInstanceProfileRequestTypeDef

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


# RemoveUserFromGroupRequestTypeDef

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


# ResetServiceSpecificCredentialRequestTypeDef

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


# ResyncMFADeviceRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PolicyDocumentTypeDef]

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


# SAMLPrivateKeyTypeDef

### KeyId
- **Type**: typing.Optional[str]

### Timestamp
- **Type**: typing.Optional[datetime.datetime]


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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceSpecificCredentialMetadataTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ServiceSpecificCredentialTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SetDefaultPolicyVersionRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### VersionId
- **Type**: <class 'str'>
- **Required**: Yes


# SetSecurityTokenServicePreferencesRequestTypeDef

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


# SimulateCustomPolicyRequestPaginateTypeDef

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


# SimulateCustomPolicyRequestTypeDef

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


# SimulatePrincipalPolicyRequestPaginateTypeDef

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


# SimulatePrincipalPolicyRequestTypeDef

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


# StatementTypeDef

### SourcePolicyId
- **Type**: typing.Optional[str]

### SourcePolicyType
- **Type**: typing.Optional[typing.Literal['aws-managed', 'group', 'none', 'resource', 'role', 'user', 'user-managed']]

### StartPosition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PositionTypeDef]

### EndPosition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.iam_classes.PositionTypeDef]


# TagInstanceProfileRequestTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TagMFADeviceRequestTypeDef

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TagOpenIDConnectProviderRequestTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TagPolicyRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TagRoleRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TagSAMLProviderRequestTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.iam_classes.TagTypeDef]
- **Required**: Yes


# TagServerCertificateRequestTypeDef

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


# TagUserRequestTypeDef

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


# UntagInstanceProfileRequestTypeDef

### InstanceProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagMFADeviceRequestTypeDef

### SerialNumber
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagOpenIDConnectProviderRequestTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagPolicyRequestTypeDef

### PolicyArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagRoleRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagSAMLProviderRequestTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagServerCertificateRequestTypeDef

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagUserRequestTypeDef

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


# UpdateAccessKeyRequestTypeDef

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


# UpdateAccountPasswordPolicyRequestTypeDef

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


# UpdateAssumeRolePolicyRequestTypeDef

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


# UpdateGroupRequestTypeDef

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


# UpdateLoginProfileRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: typing.Optional[str]

### PasswordResetRequired
- **Type**: typing.Optional[bool]


# UpdateOpenIDConnectProviderThumbprintRequestTypeDef

### OpenIDConnectProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ThumbprintList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateRoleDescriptionRequestTypeDef

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


# UpdateRoleRequestTypeDef

### RoleName
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### MaxSessionDuration
- **Type**: typing.Optional[int]


# UpdateSAMLProviderRequestSamlProviderUpdateTypeDef

### SAMLMetadataDocument
- **Type**: typing.Optional[str]

### AssertionEncryptionMode
- **Type**: typing.Optional[typing.Literal['Allowed', 'Required']]

### AddPrivateKey
- **Type**: typing.Optional[str]

### RemovePrivateKey
- **Type**: typing.Optional[str]


# UpdateSAMLProviderRequestTypeDef

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


# UpdateSAMLProviderResponseTypeDef

### SAMLProviderArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.iam_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSSHPublicKeyRequestTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### SSHPublicKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes


# UpdateServerCertificateRequestServerCertificateUpdateTypeDef

### NewPath
- **Type**: typing.Optional[str]

### NewServerCertificateName
- **Type**: typing.Optional[str]


# UpdateServerCertificateRequestTypeDef

### ServerCertificateName
- **Type**: <class 'str'>
- **Required**: Yes

### NewPath
- **Type**: typing.Optional[str]

### NewServerCertificateName
- **Type**: typing.Optional[str]


# UpdateServiceSpecificCredentialRequestTypeDef

### ServiceSpecificCredentialId
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


# UpdateSigningCertificateRequestTypeDef

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['Active', 'Inactive']
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# UpdateUserRequestTypeDef

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


# UploadSSHPublicKeyRequestTypeDef

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


# UploadServerCertificateRequestTypeDef

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


# UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef

### CertificateBody
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]


# UploadSigningCertificateRequestTypeDef

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


