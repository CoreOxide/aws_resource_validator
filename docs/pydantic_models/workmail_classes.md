# Workmail Classes

# AccessControlRule

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


# AssociateDelegateToResourceRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes


# AssociateMemberToGroupRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeImpersonationRoleRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ImpersonationRoleId
- **Type**: <class 'str'>
- **Required**: Yes


# AssumeImpersonationRoleResponse

### Token
- **Type**: <class 'str'>
- **Required**: Yes

### ExpiresIn
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# AvailabilityConfiguration

### DomainName
- **Type**: typing.Optional[str]

### ProviderType
- **Type**: typing.Optional[typing.Literal['EWS', 'LAMBDA']]

### EwsProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.RedactedEwsAvailabilityProvider]

### LambdaProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.LambdaAvailabilityProvider]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateModified
- **Type**: typing.Optional[datetime.datetime]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BookingOptions

### AutoAcceptRequests
- **Type**: typing.Optional[bool]

### AutoDeclineRecurringRequests
- **Type**: typing.Optional[bool]

### AutoDeclineConflictingRequests
- **Type**: typing.Optional[bool]


# CancelMailboxExportJobRequest

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAliasRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAvailabilityConfigurationRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### EwsProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.EwsAvailabilityProvider]

### LambdaProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.LambdaAvailabilityProvider]


# CreateGroupRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### HiddenFromGlobalAddressList
- **Type**: typing.Optional[bool]


# CreateGroupResponse

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIdentityCenterApplicationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# CreateIdentityCenterApplicationResponse

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateImpersonationRoleRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['FULL_ACCESS', 'READ_ONLY']
- **Required**: Yes

### Rules
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.workmail.workmail_classes.ImpersonationRule, aws_resource_validator.pydantic_models.workmail.workmail_classes.ImpersonationRuleOutput]]
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# CreateImpersonationRoleResponse

### ImpersonationRoleId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMobileDeviceAccessRuleRequest

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


# CreateMobileDeviceAccessRuleResponse

### MobileDeviceAccessRuleId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOrganizationRequest

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### DirectoryId
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### Domains
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.Domain]]

### KmsKeyArn
- **Type**: typing.Optional[str]

### EnableInteroperability
- **Type**: typing.Optional[bool]


# CreateOrganizationResponse

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateResourceRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['EQUIPMENT', 'ROOM']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### HiddenFromGlobalAddressList
- **Type**: typing.Optional[bool]


# CreateResourceResponse

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# CreateUserRequest

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


# CreateUserResponse

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# Delegate

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes


# DeleteAccessControlRuleRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAliasRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAvailabilityConfigurationRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteEmailMonitoringConfigurationRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGroupRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityCenterApplicationRequest

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIdentityProviderConfigurationRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteImpersonationRoleRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ImpersonationRoleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMailboxPermissionsRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### GranteeId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMobileDeviceAccessOverrideRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMobileDeviceAccessRuleRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### MobileDeviceAccessRuleId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOrganizationRequest

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


# DeleteOrganizationResponse

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### State
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePersonalAccessTokenRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### PersonalAccessTokenId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteResourceRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRetentionPolicyRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteUserRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterFromWorkMailRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterMailDomainRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEmailMonitoringConfigurationRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEmailMonitoringConfigurationResponse

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeEntityRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeEntityResponse

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['GROUP', 'RESOURCE', 'USER']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGroupRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeIdentityProviderConfigurationRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeIdentityProviderConfigurationResponse

### AuthenticationMode
- **Type**: typing.Literal['IDENTITY_PROVIDER_AND_DIRECTORY', 'IDENTITY_PROVIDER_ONLY']
- **Required**: Yes

### IdentityCenterConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.IdentityCenterConfiguration'>
- **Required**: Yes

### PersonalAccessTokenConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.PersonalAccessTokenConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeInboundDmarcSettingsRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeInboundDmarcSettingsResponse

### Enforced
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMailboxExportJobRequest

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMailboxExportJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOrganizationRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOrganizationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeResourceRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeResourceResponse

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['EQUIPMENT', 'ROOM']
- **Required**: Yes

### BookingOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.BookingOptions'>
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

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### HiddenFromGlobalAddressList
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUserRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUserResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateDelegateFromResourceRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes


# DisassociateMemberFromGroupRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### MemberId
- **Type**: <class 'str'>
- **Required**: Yes


# DnsRecord

### Type
- **Type**: typing.Optional[str]

### Hostname
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# Domain

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### HostedZoneId
- **Type**: typing.Optional[str]


# EwsAvailabilityProvider

### EwsEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### EwsUsername
- **Type**: <class 'str'>
- **Required**: Yes

### EwsPassword
- **Type**: <class 'str'>
- **Required**: Yes


# FolderConfiguration

### Name
- **Type**: typing.Literal['DELETED_ITEMS', 'DRAFTS', 'INBOX', 'JUNK_EMAIL', 'SENT_ITEMS']
- **Required**: Yes

### Action
- **Type**: typing.Literal['DELETE', 'NONE', 'PERMANENTLY_DELETE']
- **Required**: Yes

### Period
- **Type**: typing.Optional[int]


# GetAccessControlEffectRequest

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


# GetAccessControlEffectResponse

### Effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### MatchedRules
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# GetDefaultRetentionPolicyRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# GetDefaultRetentionPolicyResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.FolderConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# GetImpersonationRoleEffectRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ImpersonationRoleId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetUser
- **Type**: <class 'str'>
- **Required**: Yes


# GetImpersonationRoleEffectResponse

### Type
- **Type**: typing.Literal['FULL_ACCESS', 'READ_ONLY']
- **Required**: Yes

### Effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### MatchedRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.ImpersonationMatchedRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# GetImpersonationRoleRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ImpersonationRoleId
- **Type**: <class 'str'>
- **Required**: Yes


# GetImpersonationRoleResponse

### ImpersonationRoleId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['FULL_ACCESS', 'READ_ONLY']
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.ImpersonationRuleOutput]
- **Required**: Yes

### DateCreated
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DateModified
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# GetMailDomainRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# GetMailDomainResponse

### Records
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.DnsRecord]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# GetMailboxDetailsRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMailboxDetailsResponse

### MailboxQuota
- **Type**: <class 'int'>
- **Required**: Yes

### MailboxSize
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# GetMobileDeviceAccessEffectRequest

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


# GetMobileDeviceAccessEffectResponse

### Effect
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### MatchedRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.MobileDeviceAccessMatchedRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# GetMobileDeviceAccessOverrideRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMobileDeviceAccessOverrideResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# GetPersonalAccessTokenMetadataRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### PersonalAccessTokenId
- **Type**: <class 'str'>
- **Required**: Yes


# GetPersonalAccessTokenMetadataResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# Group

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


# GroupIdentifier

### GroupId
- **Type**: typing.Optional[str]

### GroupName
- **Type**: typing.Optional[str]


# IdentityCenterConfiguration

### InstanceArn
- **Type**: <class 'str'>
- **Required**: Yes

### ApplicationArn
- **Type**: <class 'str'>
- **Required**: Yes


# ImpersonationMatchedRule

### ImpersonationRuleId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# ImpersonationRole

### ImpersonationRoleId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['FULL_ACCESS', 'READ_ONLY']]

### DateCreated
- **Type**: typing.Optional[datetime.datetime]

### DateModified
- **Type**: typing.Optional[datetime.datetime]


# ImpersonationRule

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


# ImpersonationRuleOutput

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


# LambdaAvailabilityProvider

### LambdaArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListAccessControlRulesRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# ListAccessControlRulesResponse

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.AccessControlRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# ListAliasesRequest

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


# ListAliasesRequestPaginate

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.PaginatorConfig]


# ListAliasesResponse

### Aliases
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListAvailabilityConfigurationsRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAvailabilityConfigurationsRequestPaginate

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.PaginatorConfig]


# ListAvailabilityConfigurationsResponse

### AvailabilityConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.AvailabilityConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupMembersRequest

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


# ListGroupMembersRequestPaginate

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.PaginatorConfig]


# ListGroupMembersResponse

### Members
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.Member]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsFilters

### NamePrefix
- **Type**: typing.Optional[str]

### PrimaryEmailPrefix
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]


# ListGroupsForEntityFilters

### GroupNamePrefix
- **Type**: typing.Optional[str]


# ListGroupsForEntityRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.ListGroupsForEntityFilters]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListGroupsForEntityResponse

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.GroupIdentifier]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListGroupsRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.ListGroupsFilters]


# ListGroupsRequestPaginate

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.ListGroupsFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.PaginatorConfig]


# ListGroupsResponse

### Groups
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.Group]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListImpersonationRolesRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListImpersonationRolesResponse

### Roles
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.ImpersonationRole]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMailDomainsRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListMailDomainsResponse

### MailDomains
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.MailDomainSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMailboxExportJobsRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMailboxExportJobsResponse

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.MailboxExportJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMailboxPermissionsRequest

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


# ListMailboxPermissionsRequestPaginate

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.PaginatorConfig]


# ListMailboxPermissionsResponse

### Permissions
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.Permission]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMobileDeviceAccessOverridesRequest

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


# ListMobileDeviceAccessOverridesResponse

### Overrides
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.MobileDeviceAccessOverride]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMobileDeviceAccessRulesRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes


# ListMobileDeviceAccessRulesResponse

### Rules
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.MobileDeviceAccessRule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# ListOrganizationsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListOrganizationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.PaginatorConfig]


# ListOrganizationsResponse

### OrganizationSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.OrganizationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPersonalAccessTokensRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListPersonalAccessTokensRequestPaginate

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.PaginatorConfig]


# ListPersonalAccessTokensResponse

### PersonalAccessTokenSummaries
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.PersonalAccessTokenSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourceDelegatesRequest

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


# ListResourceDelegatesRequestPaginate

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.PaginatorConfig]


# ListResourceDelegatesResponse

### Delegates
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.Delegate]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListResourcesFilters

### NamePrefix
- **Type**: typing.Optional[str]

### PrimaryEmailPrefix
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]


# ListResourcesRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.ListResourcesFilters]


# ListResourcesRequestPaginate

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.ListResourcesFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.PaginatorConfig]


# ListResourcesResponse

### Resources
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.Resource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# ListUsersFilters

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


# ListUsersRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.ListUsersFilters]


# ListUsersRequestPaginate

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Filters
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.ListUsersFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.PaginatorConfig]


# ListUsersResponse

### Users
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.User]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# MailDomainSummary

### DomainName
- **Type**: typing.Optional[str]

### DefaultDomain
- **Type**: typing.Optional[bool]


# MailboxExportJob

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


# Member

### Id
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['GROUP', 'USER']]

### State
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]

### EnabledDate
- **Type**: typing.Optional[datetime.datetime]

### DisabledDate
- **Type**: typing.Optional[datetime.datetime]


# MobileDeviceAccessMatchedRule

### MobileDeviceAccessRuleId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# MobileDeviceAccessOverride

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


# MobileDeviceAccessRule

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


# OrganizationSummary

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


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Permission

### GranteeId
- **Type**: <class 'str'>
- **Required**: Yes

### GranteeType
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### PermissionValues
- **Type**: typing.List[typing.Literal['FULL_ACCESS', 'SEND_AS', 'SEND_ON_BEHALF']]
- **Required**: Yes


# PersonalAccessTokenConfiguration

### Status
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### LifetimeInDays
- **Type**: typing.Optional[int]


# PersonalAccessTokenSummary

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


# PutAccessControlRuleRequest

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

### ImpersonationRoleIds
- **Type**: typing.Optional[typing.List[str]]

### NotImpersonationRoleIds
- **Type**: typing.Optional[typing.List[str]]


# PutEmailMonitoringConfigurationRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### LogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes


# PutIdentityProviderConfigurationRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationMode
- **Type**: typing.Literal['IDENTITY_PROVIDER_AND_DIRECTORY', 'IDENTITY_PROVIDER_ONLY']
- **Required**: Yes

### IdentityCenterConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.IdentityCenterConfiguration'>
- **Required**: Yes

### PersonalAccessTokenConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.PersonalAccessTokenConfiguration'>
- **Required**: Yes


# PutInboundDmarcSettingsRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Enforced
- **Type**: <class 'bool'>
- **Required**: Yes


# PutMailboxPermissionsRequest

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
- **Type**: typing.List[typing.Literal['FULL_ACCESS', 'SEND_AS', 'SEND_ON_BEHALF']]
- **Required**: Yes


# PutMobileDeviceAccessOverrideRequest

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


# PutRetentionPolicyRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### FolderConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.FolderConfiguration]
- **Required**: Yes

### Id
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# RedactedEwsAvailabilityProvider

### EwsEndpoint
- **Type**: typing.Optional[str]

### EwsUsername
- **Type**: typing.Optional[str]


# RegisterMailDomainRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]


# RegisterToWorkMailRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes


# ResetPasswordRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# Resource

### Id
- **Type**: typing.Optional[str]

### Email
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['EQUIPMENT', 'ROOM']]

### State
- **Type**: typing.Optional[typing.Literal['DELETED', 'DISABLED', 'ENABLED']]

### EnabledDate
- **Type**: typing.Optional[datetime.datetime]

### DisabledDate
- **Type**: typing.Optional[datetime.datetime]

### Description
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


# StartMailboxExportJobRequest

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


# StartMailboxExportJobResponse

### JobId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.workmail.workmail_classes.Tag]
- **Required**: Yes


# TestAvailabilityConfigurationRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: typing.Optional[str]

### EwsProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.EwsAvailabilityProvider]

### LambdaProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.LambdaAvailabilityProvider]


# TestAvailabilityConfigurationResponse

### TestPassed
- **Type**: <class 'bool'>
- **Required**: Yes

### FailureReason
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.workmail.workmail_classes.ResponseMetadata'>
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateAvailabilityConfigurationRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EwsProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.EwsAvailabilityProvider]

### LambdaProvider
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.workmail.workmail_classes.LambdaAvailabilityProvider]


# UpdateDefaultMailDomainRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateGroupRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### GroupId
- **Type**: <class 'str'>
- **Required**: Yes

### HiddenFromGlobalAddressList
- **Type**: typing.Optional[bool]


# UpdateImpersonationRoleRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ImpersonationRoleId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['FULL_ACCESS', 'READ_ONLY']
- **Required**: Yes

### Rules
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.workmail.workmail_classes.ImpersonationRule, aws_resource_validator.pydantic_models.workmail.workmail_classes.ImpersonationRuleOutput]]
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateMailboxQuotaRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### UserId
- **Type**: <class 'str'>
- **Required**: Yes

### MailboxQuota
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateMobileDeviceAccessRuleRequest

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


# UpdatePrimaryEmailAddressRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### EntityId
- **Type**: <class 'str'>
- **Required**: Yes

### Email
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateResourceRequest

### OrganizationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### BookingOptions
- **Type**: <class 'NoneType'>

### Description
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['EQUIPMENT', 'ROOM']]

### HiddenFromGlobalAddressList
- **Type**: typing.Optional[bool]


# UpdateUserRequest

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


# User

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


