# Workmail Classes

# AccessControlRuleTypeDef

### Name
- **Type**: typing.Optional[str]

### Effect
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### Description
- **Type**: typing.Optional[str]

### IpRanges
- **Type**: typing.Optional[typing.List[str]]

### NotIpRanges
- **Type**: typing.Optional[typing.List[str]]

### Actions
- **Type**: typing.Optional[typing.List[str]]

### NotActions
- **Type**: typing.Optional[typing.List[str]]

### UserIds
- **Type**: typing.Optional[typing.List[str]]

### NotUserIds
- **Type**: typing.Optional[typing.List[str]]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateModified
- **Type**: typing.Optional[datetime.datetime]

### ImpersonationRoleIds
- **Type**: typing.Optional[typing.List[str]]

### NotImpersonationRoleIds
- **Type**: typing.Optional[typing.List[str]]


# AssociateDelegateToResourceRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateMemberToGroupRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeImpersonationRoleRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ImpersonationRoleId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeImpersonationRoleResponseTypeDef

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### ExpiresIn
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AvailabilityConfigurationTypeDef

### DomainName
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['EWS', 'LAMBDA']]

### EwsProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.RedactedEwsAvailabilityProviderTypeDef]

### LambdaProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.LambdaAvailabilityProviderTypeDef]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateModified
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BookingOptionsTypeDef

### AutoAcceptRequests
- **Type**: typing.Optional[bool]

### AutoDeclineRecurringRequests
- **Type**: typing.Optional[bool]

### AutoDeclineConflictingRequests
- **Type**: typing.Optional[bool]


# CancelMailboxExportJobRequestTypeDef

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAliasRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAvailabilityConfigurationRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### EwsProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.EwsAvailabilityProviderTypeDef]

### LambdaProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.LambdaAvailabilityProviderTypeDef]


# CreateGroupRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HiddenFromGlobalAddressList
- **Type**: typing.Optional[bool]


# CreateGroupResponseTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIdentityCenterApplicationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateIdentityCenterApplicationResponseTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateImpersonationRoleResponseTypeDef

### ImpersonationRoleId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMobileDeviceAccessRuleRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DeviceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### NotDeviceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### DeviceModels
- **Type**: typing.Optional[typing.Sequence[str]]

### NotDeviceModels
- **Type**: typing.Optional[typing.Sequence[str]]

### DeviceOperatingSystems
- **Type**: typing.Optional[typing.Sequence[str]]

### NotDeviceOperatingSystems
- **Type**: typing.Optional[typing.Sequence[str]]

### DeviceUserAgents
- **Type**: typing.Optional[typing.Sequence[str]]

### NotDeviceUserAgents
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateMobileDeviceAccessRuleResponseTypeDef

### MobileDeviceAccessRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOrganizationRequestTypeDef

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryId
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Domains
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.workmail_classes.DomainTypeDef]]

### KmsKeyArn
- **Type**: typing.Optional[str]

### EnableInteroperability
- **Type**: typing.Optional[bool]


# CreateOrganizationResponseTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateResourceResponseTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateUserRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[typing.Literal['REMOTE_USER', 'RESOURCE', 'SYSTEM_USER', 'USER']]

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]

### HiddenFromGlobalAddressList
- **Type**: typing.Optional[bool]

### IdentityProviderUserId
- **Type**: typing.Optional[str]


# CreateUserResponseTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DelegateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DeleteAccessControlRuleRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAliasRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAvailabilityConfigurationRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailMonitoringConfigurationRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityCenterApplicationRequestTypeDef

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityProviderConfigurationRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImpersonationRoleRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ImpersonationRoleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMailboxPermissionsRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### GranteeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMobileDeviceAccessOverrideRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMobileDeviceAccessRuleRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### MobileDeviceAccessRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOrganizationRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteDirectory
- **Type**: <class 'bool'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### ForceDelete
- **Type**: typing.Optional[bool]

### DeleteIdentityCenterApplication
- **Type**: typing.Optional[bool]


# DeleteOrganizationResponseTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePersonalAccessTokenRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### PersonalAccessTokenId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRetentionPolicyRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterFromWorkMailRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterMailDomainRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEmailMonitoringConfigurationRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEmailMonitoringConfigurationResponseTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeEntityRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGroupRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGroupResponseTypeDef

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DELETED', 'DISABLED', 'ENABLED']
- **Required**: Yes

### EnabledDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DisabledDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HiddenFromGlobalAddressList
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeIdentityProviderConfigurationRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityProviderConfigurationResponseTypeDef

### AuthenticationMode
- **Type**: typing.Literal['IDENTITY_PROVIDER_AND_DIRECTORY', 'IDENTITY_PROVIDER_ONLY']
- **Required**: Yes

### IdentityCenterConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.IdentityCenterConfigurationTypeDef'>
- **Required**: Yes

### PersonalAccessTokenConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.PersonalAccessTokenConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeInboundDmarcSettingsRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInboundDmarcSettingsResponseTypeDef

### Enforced
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMailboxExportJobRequestTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMailboxExportJobResponseTypeDef

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Prefix
- **Type**: <class 'str'>
- **Required**: Yes

### S3Path
- **Type**: <class 'str'>
- **Required**: Yes

### EstimatedProgress
- **Type**: <class 'int'>
- **Required**: Yes

### State
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'RUNNING']
- **Required**: Yes

### ErrorInfo
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOrganizationRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOrganizationResponseTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryType
- **Type**: <class 'str'>
- **Required**: Yes

### DefaultMailDomain
- **Type**: <class 'str'>
- **Required**: Yes

### CompletedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ARN
- **Type**: <class 'str'>
- **Required**: Yes

### MigrationAdmin
- **Type**: <class 'str'>
- **Required**: Yes

### InteroperabilityEnabled
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeResourceRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserResponseTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes

### DisplayName
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: typing.Literal['DELETED', 'DISABLED', 'ENABLED']
- **Required**: Yes

### UserRole
- **Type**: typing.Literal['REMOTE_USER', 'RESOURCE', 'SYSTEM_USER', 'USER']
- **Required**: Yes

### EnabledDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DisabledDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MailboxProvisionedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### MailboxDeprovisionedDate
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FirstName
- **Type**: <class 'str'>
- **Required**: Yes

### LastName
- **Type**: <class 'str'>
- **Required**: Yes

### HiddenFromGlobalAddressList
- **Type**: <class 'bool'>
- **Required**: Yes

### Initials
- **Type**: <class 'str'>
- **Required**: Yes

### Telephone
- **Type**: <class 'str'>
- **Required**: Yes

### Street
- **Type**: <class 'str'>
- **Required**: Yes

### JobTitle
- **Type**: <class 'str'>
- **Required**: Yes

### City
- **Type**: <class 'str'>
- **Required**: Yes

### Company
- **Type**: <class 'str'>
- **Required**: Yes

### ZipCode
- **Type**: <class 'str'>
- **Required**: Yes

### Department
- **Type**: <class 'str'>
- **Required**: Yes

### Country
- **Type**: <class 'str'>
- **Required**: Yes

### Office
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityProviderUserId
- **Type**: <class 'str'>
- **Required**: Yes

### IdentityProviderIdentityStoreId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateDelegateFromResourceRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberFromGroupRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes


# DnsRecordTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DomainTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### HostedZoneId
- **Type**: typing.Optional[str]


# EwsAvailabilityProviderTypeDef

### EwsEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### EwsUsername
- **Type**: <class 'str'>
- **Required**: Yes

### EwsPassword
- **Type**: <class 'str'>
- **Required**: Yes


# FolderConfigurationTypeDef

### Name
- **Type**: typing.Literal['DELETED_ITEMS', 'DRAFTS', 'INBOX', 'JUNK_EMAIL', 'SENT_ITEMS']
- **Required**: Yes

### Action
- **Type**: typing.Literal['DELETE', 'NONE', 'PERMANENTLY_DELETE']
- **Required**: Yes

### Period
- **Type**: typing.Optional[int]


# GetAccessControlEffectRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### IpAddress
- **Type**: <class 'str'>
- **Required**: Yes

### Action
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### ImpersonationRoleId
- **Type**: typing.Optional[str]


# GetAccessControlEffectResponseTypeDef

### Effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### MatchedRules
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDefaultRetentionPolicyRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDefaultRetentionPolicyResponseTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### FolderConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.FolderConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImpersonationRoleEffectRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ImpersonationRoleId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetUser
- **Type**: <class 'str'>
- **Required**: Yes


# GetImpersonationRoleRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ImpersonationRoleId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMailDomainRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMailDomainResponseTypeDef

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.DnsRecordTypeDef]
- **Required**: Yes

### IsTestDomain
- **Type**: <class 'bool'>
- **Required**: Yes

### IsDefault
- **Type**: <class 'bool'>
- **Required**: Yes

### OwnershipVerificationStatus
- **Type**: typing.Literal['FAILED', 'PENDING', 'VERIFIED']
- **Required**: Yes

### DkimVerificationStatus
- **Type**: typing.Literal['FAILED', 'PENDING', 'VERIFIED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMailboxDetailsRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMailboxDetailsResponseTypeDef

### MailboxQuota
- **Type**: <class 'int'>
- **Required**: Yes

### MailboxSize
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMobileDeviceAccessEffectRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceType
- **Type**: typing.Optional[str]

### DeviceModel
- **Type**: typing.Optional[str]

### DeviceOperatingSystem
- **Type**: typing.Optional[str]

### DeviceUserAgent
- **Type**: typing.Optional[str]


# GetMobileDeviceAccessEffectResponseTypeDef

### Effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### MatchedRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.MobileDeviceAccessMatchedRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMobileDeviceAccessOverrideRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMobileDeviceAccessOverrideResponseTypeDef

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### DateCreated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DateModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPersonalAccessTokenMetadataRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### PersonalAccessTokenId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPersonalAccessTokenMetadataResponseTypeDef

### PersonalAccessTokenId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### DateCreated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DateLastUsed
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ExpiresTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Scopes
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GroupIdentifierTypeDef

### GroupId
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]


# GroupTypeDef

### Id
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]

### EnabledDate
- **Type**: typing.Optional[datetime.datetime]

### DisabledDate
- **Type**: typing.Optional[datetime.datetime]


# IdentityCenterConfigurationTypeDef

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# ImpersonationMatchedRuleTypeDef

### ImpersonationRuleId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ImpersonationRoleTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImpersonationRuleOutputTypeDef

### ImpersonationRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### TargetUsers
- **Type**: typing.Optional[typing.List[str]]

### NotTargetUsers
- **Type**: typing.Optional[typing.List[str]]


# ImpersonationRuleTypeDef

### ImpersonationRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### TargetUsers
- **Type**: typing.Optional[typing.Sequence[str]]

### NotTargetUsers
- **Type**: typing.Optional[typing.Sequence[str]]


# LambdaAvailabilityProviderTypeDef

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListAccessControlRulesRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# ListAccessControlRulesResponseTypeDef

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.AccessControlRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAliasesRequestPaginateTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.PaginatorConfigTypeDef]


# ListAliasesRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListAliasesResponseTypeDef

### Aliases
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAvailabilityConfigurationsRequestPaginateTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.PaginatorConfigTypeDef]


# ListAvailabilityConfigurationsRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAvailabilityConfigurationsResponseTypeDef

### AvailabilityConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.AvailabilityConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupMembersRequestPaginateTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.PaginatorConfigTypeDef]


# ListGroupMembersRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGroupMembersResponseTypeDef

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.MemberTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsFiltersTypeDef

### NamePrefix
- **Type**: typing.Optional[str]

### PrimaryEmailPrefix
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]


# ListGroupsForEntityFiltersTypeDef

### GroupNamePrefix
- **Type**: typing.Optional[str]


# ListGroupsForEntityRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.ListGroupsForEntityFiltersTypeDef]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGroupsForEntityResponseTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.GroupIdentifierTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsRequestPaginateTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.ListGroupsFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.PaginatorConfigTypeDef]


# ListGroupsRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.ListGroupsFiltersTypeDef]


# ListGroupsResponseTypeDef

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.GroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImpersonationRolesRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListImpersonationRolesResponseTypeDef

### Roles
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.ImpersonationRoleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMailDomainsRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMailDomainsResponseTypeDef

### MailDomains
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.MailDomainSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMailboxExportJobsRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMailboxExportJobsResponseTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.MailboxExportJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMailboxPermissionsRequestPaginateTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.PaginatorConfigTypeDef]


# ListMailboxPermissionsRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMailboxPermissionsResponseTypeDef

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.PermissionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMobileDeviceAccessOverridesRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### DeviceId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMobileDeviceAccessOverridesResponseTypeDef

### Overrides
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.MobileDeviceAccessOverrideTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMobileDeviceAccessRulesRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# ListMobileDeviceAccessRulesResponseTypeDef

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.MobileDeviceAccessRuleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOrganizationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.PaginatorConfigTypeDef]


# ListOrganizationsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOrganizationsResponseTypeDef

### OrganizationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.OrganizationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPersonalAccessTokensRequestPaginateTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.PaginatorConfigTypeDef]


# ListPersonalAccessTokensRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPersonalAccessTokensResponseTypeDef

### PersonalAccessTokenSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.PersonalAccessTokenSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDelegatesRequestPaginateTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.PaginatorConfigTypeDef]


# ListResourceDelegatesRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListResourceDelegatesResponseTypeDef

### Delegates
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.DelegateTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesFiltersTypeDef

### NamePrefix
- **Type**: typing.Optional[str]

### PrimaryEmailPrefix
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]


# ListResourcesRequestPaginateTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.ListResourcesFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.PaginatorConfigTypeDef]


# ListResourcesRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.ListResourcesFiltersTypeDef]


# ListResourcesResponseTypeDef

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.ResourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListUsersFiltersTypeDef

### UsernamePrefix
- **Type**: typing.Optional[str]

### DisplayNamePrefix
- **Type**: typing.Optional[str]

### PrimaryEmailPrefix
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]

### IdentityProviderUserIdPrefix
- **Type**: typing.Optional[str]


# ListUsersRequestPaginateTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.ListUsersFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.PaginatorConfigTypeDef]


# ListUsersRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.ListUsersFiltersTypeDef]


# ListUsersResponseTypeDef

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail_classes.UserTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MailDomainSummaryTypeDef

### DomainName
- **Type**: typing.Optional[str]

### DefaultDomain
- **Type**: typing.Optional[bool]


# MailboxExportJobTypeDef

### JobId
- **Type**: typing.Optional[str]

### EntityId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### S3BucketName
- **Type**: typing.Optional[str]

### S3Path
- **Type**: typing.Optional[str]

### EstimatedProgress
- **Type**: typing.Optional[int]

### State
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'RUNNING']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]


# MemberTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MobileDeviceAccessMatchedRuleTypeDef

### MobileDeviceAccessRuleId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# MobileDeviceAccessOverrideTypeDef

### UserId
- **Type**: typing.Optional[str]

### DeviceId
- **Type**: typing.Optional[str]

### Effect
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### Description
- **Type**: typing.Optional[str]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateModified
- **Type**: typing.Optional[datetime.datetime]


# MobileDeviceAccessRuleTypeDef

### MobileDeviceAccessRuleId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Effect
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### DeviceTypes
- **Type**: typing.Optional[typing.List[str]]

### NotDeviceTypes
- **Type**: typing.Optional[typing.List[str]]

### DeviceModels
- **Type**: typing.Optional[typing.List[str]]

### NotDeviceModels
- **Type**: typing.Optional[typing.List[str]]

### DeviceOperatingSystems
- **Type**: typing.Optional[typing.List[str]]

### NotDeviceOperatingSystems
- **Type**: typing.Optional[typing.List[str]]

### DeviceUserAgents
- **Type**: typing.Optional[typing.List[str]]

### NotDeviceUserAgents
- **Type**: typing.Optional[typing.List[str]]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateModified
- **Type**: typing.Optional[datetime.datetime]


# OrganizationSummaryTypeDef

### OrganizationId
- **Type**: typing.Optional[str]

### Alias
- **Type**: typing.Optional[str]

### DefaultMailDomain
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionTypeDef

### GranteeId
- **Type**: <class 'str'>
- **Required**: Yes

### GranteeType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### PermissionValues
- **Type**: typing.List[typing.Literal['FULL_ACCESS', 'SEND_AS', 'SEND_ON_BEHALF']]
- **Required**: Yes


# PersonalAccessTokenConfigurationTypeDef

### Status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### LifetimeInDays
- **Type**: typing.Optional[int]


# PersonalAccessTokenSummaryTypeDef

### PersonalAccessTokenId
- **Type**: typing.Optional[str]

### UserId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateLastUsed
- **Type**: typing.Optional[datetime.datetime]

### ExpiresTime
- **Type**: typing.Optional[datetime.datetime]

### Scopes
- **Type**: typing.Optional[typing.List[str]]


# PutAccessControlRuleRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### IpRanges
- **Type**: typing.Optional[typing.Sequence[str]]

### NotIpRanges
- **Type**: typing.Optional[typing.Sequence[str]]

### Actions
- **Type**: typing.Optional[typing.Sequence[str]]

### NotActions
- **Type**: typing.Optional[typing.Sequence[str]]

### UserIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NotUserIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ImpersonationRoleIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NotImpersonationRoleIds
- **Type**: typing.Optional[typing.Sequence[str]]


# PutEmailMonitoringConfigurationRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutIdentityProviderConfigurationRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMode
- **Type**: typing.Literal['IDENTITY_PROVIDER_AND_DIRECTORY', 'IDENTITY_PROVIDER_ONLY']
- **Required**: Yes

### IdentityCenterConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.IdentityCenterConfigurationTypeDef'>
- **Required**: Yes

### PersonalAccessTokenConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.PersonalAccessTokenConfigurationTypeDef'>
- **Required**: Yes


# PutInboundDmarcSettingsRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Enforced
- **Type**: <class 'bool'>
- **Required**: Yes


# PutMailboxPermissionsRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### GranteeId
- **Type**: <class 'str'>
- **Required**: Yes

### PermissionValues
- **Type**: typing.Sequence[typing.Literal['FULL_ACCESS', 'SEND_AS', 'SEND_ON_BEHALF']]
- **Required**: Yes


# PutMobileDeviceAccessOverrideRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes

### Effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# PutRetentionPolicyRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FolderConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workmail_classes.FolderConfigurationTypeDef]
- **Required**: Yes

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# RedactedEwsAvailabilityProviderTypeDef

### EwsEndpoint
- **Type**: typing.Optional[str]

### EwsUsername
- **Type**: typing.Optional[str]


# RegisterMailDomainRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# RegisterToWorkMailRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes


# ResetPasswordRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# ResourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# StartMailboxExportJobRequestTypeDef

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### KmsKeyArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### S3Prefix
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# StartMailboxExportJobResponseTypeDef

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.workmail_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TestAvailabilityConfigurationRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: typing.Optional[str]

### EwsProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.EwsAvailabilityProviderTypeDef]

### LambdaProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.LambdaAvailabilityProviderTypeDef]


# TestAvailabilityConfigurationResponseTypeDef

### TestPassed
- **Type**: <class 'bool'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAvailabilityConfigurationRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EwsProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.EwsAvailabilityProviderTypeDef]

### LambdaProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail_classes.LambdaAvailabilityProviderTypeDef]


# UpdateDefaultMailDomainRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateGroupRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### HiddenFromGlobalAddressList
- **Type**: typing.Optional[bool]


# UpdateMailboxQuotaRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### MailboxQuota
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateMobileDeviceAccessRuleRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### MobileDeviceAccessRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### DeviceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### NotDeviceTypes
- **Type**: typing.Optional[typing.Sequence[str]]

### DeviceModels
- **Type**: typing.Optional[typing.Sequence[str]]

### NotDeviceModels
- **Type**: typing.Optional[typing.Sequence[str]]

### DeviceOperatingSystems
- **Type**: typing.Optional[typing.Sequence[str]]

### NotDeviceOperatingSystems
- **Type**: typing.Optional[typing.Sequence[str]]

### DeviceUserAgents
- **Type**: typing.Optional[typing.Sequence[str]]

### NotDeviceUserAgents
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdatePrimaryEmailAddressRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateUserRequestTypeDef

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: typing.Optional[typing.Literal['REMOTE_USER', 'RESOURCE', 'SYSTEM_USER', 'USER']]

### DisplayName
- **Type**: typing.Optional[str]

### FirstName
- **Type**: typing.Optional[str]

### LastName
- **Type**: typing.Optional[str]

### HiddenFromGlobalAddressList
- **Type**: typing.Optional[bool]

### Initials
- **Type**: typing.Optional[str]

### Telephone
- **Type**: typing.Optional[str]

### Street
- **Type**: typing.Optional[str]

### JobTitle
- **Type**: typing.Optional[str]

### City
- **Type**: typing.Optional[str]

### Company
- **Type**: typing.Optional[str]

### ZipCode
- **Type**: typing.Optional[str]

### Department
- **Type**: typing.Optional[str]

### Country
- **Type**: typing.Optional[str]

### Office
- **Type**: typing.Optional[str]

### IdentityProviderUserId
- **Type**: typing.Optional[str]


# UserTypeDef

### Id
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### DisplayName
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]

### UserRole
- **Type**: typing.Optional[typing.Literal['REMOTE_USER', 'RESOURCE', 'SYSTEM_USER', 'USER']]

### EnabledDate
- **Type**: typing.Optional[datetime.datetime]

### DisabledDate
- **Type**: typing.Optional[datetime.datetime]

### IdentityProviderUserId
- **Type**: typing.Optional[str]

### IdentityProviderIdentityStoreId
- **Type**: typing.Optional[str]


