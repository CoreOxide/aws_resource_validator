# Ds Classes

# AcceptSharedDirectoryRequestRequestTypeDef

### SharedDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptSharedDirectoryResultTypeDef

### SharedDirectory
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.SharedDirectoryTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddIpRoutesRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### IpRoutes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.IpRouteTypeDef]
- **Required**: Yes

### UpdateSecurityGroupForDirectoryControllers
- **Type**: typing.Optional[bool]


# AddRegionRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RegionName
- **Type**: <class 'str'>
- **Required**: Yes

### VPCSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.DirectoryVpcSettingsTypeDef'>
- **Required**: Yes


# AddTagsToResourceRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.TagTypeDef]
- **Required**: Yes


# AttributeTypeDef

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelSchemaExtensionRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaExtensionId
- **Type**: <class 'str'>
- **Required**: Yes


# CertificateInfoTypeDef

### CertificateId
- **Type**: typing.Optional[str]

### CommonName
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DeregisterFailed', 'Deregistered', 'Deregistering', 'RegisterFailed', 'Registered', 'Registering']]

### ExpiryDateTime
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['ClientCertAuth', 'ClientLDAPS']]


# CertificateTypeDef

### CertificateId
- **Type**: typing.Optional[str]

### State
- **Type**: typing.Optional[typing.Literal['DeregisterFailed', 'Deregistered', 'Deregistering', 'RegisterFailed', 'Registered', 'Registering']]

### StateReason
- **Type**: typing.Optional[str]

### CommonName
- **Type**: typing.Optional[str]

### RegisteredDateTime
- **Type**: typing.Optional[datetime.datetime]

### ExpiryDateTime
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['ClientCertAuth', 'ClientLDAPS']]

### ClientCertAuthSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.ClientCertAuthSettingsTypeDef]


# ClientAuthenticationSettingInfoTypeDef

### Type
- **Type**: typing.Optional[typing.Literal['SmartCard', 'SmartCardOrPassword']]

### Status
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### LastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# ClientCertAuthSettingsTypeDef

### OCSPUrl
- **Type**: typing.Optional[str]


# ComputerTypeDef

### ComputerId
- **Type**: typing.Optional[str]

### ComputerName
- **Type**: typing.Optional[str]

### ComputerAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ds_classes.AttributeTypeDef]]


# ConditionalForwarderTypeDef

### RemoteDomainName
- **Type**: typing.Optional[str]

### DnsIpAddrs
- **Type**: typing.Optional[typing.List[str]]

### ReplicationScope
- **Type**: typing.Optional[typing.Literal['Domain']]


# ConnectDirectoryRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### Size
- **Type**: typing.Literal['Large', 'Small']
- **Required**: Yes

### ConnectSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.DirectoryConnectSettingsTypeDef'>
- **Required**: Yes

### ShortName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.TagTypeDef]]


# ConnectDirectoryResultTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAliasRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAliasResultTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateComputerRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ComputerName
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationalUnitDistinguishedName
- **Type**: typing.Optional[str]

### ComputerAttributes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.AttributeTypeDef]]


# CreateComputerResultTypeDef

### Computer
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ComputerTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateConditionalForwarderRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DnsIpAddrs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CreateDirectoryRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### Size
- **Type**: typing.Literal['Large', 'Small']
- **Required**: Yes

### ShortName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### VpcSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.DirectoryVpcSettingsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.TagTypeDef]]


# CreateDirectoryResultTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLogSubscriptionRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### LogGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateMicrosoftADRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### VpcSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.DirectoryVpcSettingsTypeDef'>
- **Required**: Yes

### ShortName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Edition
- **Type**: typing.Optional[typing.Literal['Enterprise', 'Standard']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.TagTypeDef]]


# CreateMicrosoftADResultTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSnapshotRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# CreateSnapshotResultTypeDef

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTrustRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### TrustPassword
- **Type**: <class 'str'>
- **Required**: Yes

### TrustDirection
- **Type**: typing.Literal['One-Way: Incoming', 'One-Way: Outgoing', 'Two-Way']
- **Required**: Yes

### TrustType
- **Type**: typing.Optional[typing.Literal['External', 'Forest']]

### ConditionalForwarderIpAddrs
- **Type**: typing.Optional[typing.Sequence[str]]

### SelectiveAuth
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# CreateTrustResultTypeDef

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteConditionalForwarderRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectoryRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectoryResultTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteLogSubscriptionRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotRequestRequestTypeDef

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotResultTypeDef

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTrustRequestRequestTypeDef

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteAssociatedConditionalForwarder
- **Type**: typing.Optional[bool]


# DeleteTrustResultTypeDef

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeregisterCertificateRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterEventTopicRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateResultTypeDef

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.CertificateTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeClientAuthenticationSettingsRequestDescribeClientAuthenticationSettingsPaginateTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['SmartCard', 'SmartCardOrPassword']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeClientAuthenticationSettingsRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['SmartCard', 'SmartCardOrPassword']]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeClientAuthenticationSettingsResultTypeDef

### ClientAuthenticationSettingsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.ClientAuthenticationSettingInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConditionalForwardersRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDomainNames
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeConditionalForwardersResultTypeDef

### ConditionalForwarders
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.ConditionalForwarderTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDirectoriesRequestDescribeDirectoriesPaginateTypeDef

### DirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeDirectoriesRequestRequestTypeDef

### DirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeDirectoriesResultTypeDef

### DirectoryDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.DirectoryDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDomainControllersRequestDescribeDomainControllersPaginateTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainControllerIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeDomainControllersRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainControllerIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeDomainControllersResultTypeDef

### DomainControllers
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.DomainControllerTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEventTopicsRequestRequestTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### TopicNames
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeEventTopicsResultTypeDef

### EventTopics
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.EventTopicTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLDAPSSettingsRequestDescribeLDAPSSettingsPaginateTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['Client']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeLDAPSSettingsRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['Client']]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeLDAPSSettingsResultTypeDef

### LDAPSSettingsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.LDAPSSettingInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegionsRequestDescribeRegionsPaginateTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RegionName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeRegionsRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RegionName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegionsResultTypeDef

### RegionsDescription
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.RegionDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSettingsRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['Default', 'Failed', 'Requested', 'Updated', 'Updating']]

### NextToken
- **Type**: typing.Optional[str]


# DescribeSettingsResultTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SettingEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.SettingEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSharedDirectoriesRequestDescribeSharedDirectoriesPaginateTypeDef

### OwnerDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SharedDirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeSharedDirectoriesRequestRequestTypeDef

### OwnerDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SharedDirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeSharedDirectoriesResultTypeDef

### SharedDirectories
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.SharedDirectoryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSnapshotsRequestDescribeSnapshotsPaginateTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### SnapshotIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeSnapshotsRequestRequestTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### SnapshotIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeSnapshotsResultTypeDef

### Snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.SnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeTrustsRequestDescribeTrustsPaginateTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### TrustIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeTrustsRequestRequestTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### TrustIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeTrustsResultTypeDef

### Trusts
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.TrustTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeUpdateDirectoryRequestDescribeUpdateDirectoryPaginateTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateType
- **Type**: typing.Literal['OS']
- **Required**: Yes

### RegionName
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeUpdateDirectoryRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateType
- **Type**: typing.Literal['OS']
- **Required**: Yes

### RegionName
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]


# DescribeUpdateDirectoryResultTypeDef

### UpdateActivities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.UpdateInfoEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DirectoryConnectSettingsDescriptionTypeDef

### VpcId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### CustomerUserName
- **Type**: typing.Optional[str]

### SecurityGroupId
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]

### ConnectIps
- **Type**: typing.Optional[typing.List[str]]


# DirectoryConnectSettingsTypeDef

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CustomerDnsIps
- **Type**: typing.Sequence[str]
- **Required**: Yes

### CustomerUserName
- **Type**: <class 'str'>
- **Required**: Yes


# DirectoryDescriptionTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### ShortName
- **Type**: typing.Optional[str]

### Size
- **Type**: typing.Optional[typing.Literal['Large', 'Small']]

### Edition
- **Type**: typing.Optional[typing.Literal['Enterprise', 'Standard']]

### Alias
- **Type**: typing.Optional[str]

### AccessUrl
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### DnsIpAddrs
- **Type**: typing.Optional[typing.List[str]]

### Stage
- **Type**: typing.Optional[typing.Literal['Active', 'Created', 'Creating', 'Deleted', 'Deleting', 'Failed', 'Impaired', 'Inoperable', 'Requested', 'RestoreFailed', 'Restoring']]

### ShareStatus
- **Type**: typing.Optional[typing.Literal['Deleted', 'Deleting', 'PendingAcceptance', 'RejectFailed', 'Rejected', 'Rejecting', 'ShareFailed', 'Shared', 'Sharing']]

### ShareMethod
- **Type**: typing.Optional[typing.Literal['HANDSHAKE', 'ORGANIZATIONS']]

### ShareNotes
- **Type**: typing.Optional[str]

### LaunchTime
- **Type**: typing.Optional[datetime.datetime]

### StageLastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### Type
- **Type**: typing.Optional[typing.Literal['ADConnector', 'MicrosoftAD', 'SharedMicrosoftAD', 'SimpleAD']]

### VpcSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.DirectoryVpcSettingsDescriptionTypeDef]

### ConnectSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.DirectoryConnectSettingsDescriptionTypeDef]

### RadiusSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.RadiusSettingsOutputTypeDef]

### RadiusStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Creating', 'Failed']]

### StageReason
- **Type**: typing.Optional[str]

### SsoEnabled
- **Type**: typing.Optional[bool]

### DesiredNumberOfDomainControllers
- **Type**: typing.Optional[int]

### OwnerDirectoryDescription
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.OwnerDirectoryDescriptionTypeDef]

### RegionsInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.RegionsInfoTypeDef]

### OsVersion
- **Type**: typing.Optional[typing.Literal['SERVER_2012', 'SERVER_2019']]


# DirectoryLimitsTypeDef

### CloudOnlyDirectoriesLimit
- **Type**: typing.Optional[int]

### CloudOnlyDirectoriesCurrentCount
- **Type**: typing.Optional[int]

### CloudOnlyDirectoriesLimitReached
- **Type**: typing.Optional[bool]

### CloudOnlyMicrosoftADLimit
- **Type**: typing.Optional[int]

### CloudOnlyMicrosoftADCurrentCount
- **Type**: typing.Optional[int]

### CloudOnlyMicrosoftADLimitReached
- **Type**: typing.Optional[bool]

### ConnectedDirectoriesLimit
- **Type**: typing.Optional[int]

### ConnectedDirectoriesCurrentCount
- **Type**: typing.Optional[int]

### ConnectedDirectoriesLimitReached
- **Type**: typing.Optional[bool]


# DirectoryVpcSettingsDescriptionTypeDef

### VpcId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupId
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]


# DirectoryVpcSettingsExtraOutputTypeDef

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes


# DirectoryVpcSettingsOutputTypeDef

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes


# DirectoryVpcSettingsTypeDef

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DisableClientAuthenticationRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['SmartCard', 'SmartCardOrPassword']
- **Required**: Yes


# DisableLDAPSRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['Client']
- **Required**: Yes


# DisableRadiusRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableSsoRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# DomainControllerTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### DomainControllerId
- **Type**: typing.Optional[str]

### DnsIpAddr
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]

### SubnetId
- **Type**: typing.Optional[str]

### AvailabilityZone
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Creating', 'Deleted', 'Deleting', 'Failed', 'Impaired', 'Restoring']]

### StatusReason
- **Type**: typing.Optional[str]

### LaunchTime
- **Type**: typing.Optional[datetime.datetime]

### StatusLastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# EnableClientAuthenticationRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['SmartCard', 'SmartCardOrPassword']
- **Required**: Yes


# EnableLDAPSRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['Client']
- **Required**: Yes


# EnableRadiusRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RadiusSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.RadiusSettingsTypeDef'>
- **Required**: Yes


# EnableSsoRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# EventTopicTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### TopicName
- **Type**: typing.Optional[str]

### TopicArn
- **Type**: typing.Optional[str]

### CreatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['Deleted', 'Failed', 'Registered', 'Topic not found']]


# GetDirectoryLimitsResultTypeDef

### DirectoryLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.DirectoryLimitsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSnapshotLimitsRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSnapshotLimitsResultTypeDef

### SnapshotLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.SnapshotLimitsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IpRouteInfoTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### CidrIp
- **Type**: typing.Optional[str]

### IpRouteStatusMsg
- **Type**: typing.Optional[typing.Literal['AddFailed', 'Added', 'Adding', 'RemoveFailed', 'Removed', 'Removing']]

### AddedDateTime
- **Type**: typing.Optional[datetime.datetime]

### IpRouteStatusReason
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# IpRouteTypeDef

### CidrIp
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# LDAPSSettingInfoTypeDef

### LDAPSStatus
- **Type**: typing.Optional[typing.Literal['Disabled', 'EnableFailed', 'Enabled', 'Enabling']]

### LDAPSStatusReason
- **Type**: typing.Optional[str]

### LastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# ListCertificatesRequestListCertificatesPaginateTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# ListCertificatesRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListCertificatesResultTypeDef

### CertificatesInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.CertificateInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIpRoutesRequestListIpRoutesPaginateTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# ListIpRoutesRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListIpRoutesResultTypeDef

### IpRoutesInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.IpRouteInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLogSubscriptionsRequestListLogSubscriptionsPaginateTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# ListLogSubscriptionsRequestRequestTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListLogSubscriptionsResultTypeDef

### LogSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.LogSubscriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchemaExtensionsRequestListSchemaExtensionsPaginateTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# ListSchemaExtensionsRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListSchemaExtensionsResultTypeDef

### SchemaExtensionsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.SchemaExtensionInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestListTagsForResourcePaginateTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTagsForResourceResultTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LogSubscriptionTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### LogGroupName
- **Type**: typing.Optional[str]

### SubscriptionCreatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# OSUpdateSettingsTypeDef

### OSVersion
- **Type**: typing.Optional[typing.Literal['SERVER_2012', 'SERVER_2019']]


# OwnerDirectoryDescriptionTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### DnsIpAddrs
- **Type**: typing.Optional[typing.List[str]]

### VpcSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.DirectoryVpcSettingsDescriptionTypeDef]

### RadiusSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.RadiusSettingsOutputTypeDef]

### RadiusStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Creating', 'Failed']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RadiusSettingsExtraOutputTypeDef

### RadiusServers
- **Type**: typing.Optional[typing.List[str]]

### RadiusPort
- **Type**: typing.Optional[int]

### RadiusTimeout
- **Type**: typing.Optional[int]

### RadiusRetries
- **Type**: typing.Optional[int]

### SharedSecret
- **Type**: typing.Optional[str]

### AuthenticationProtocol
- **Type**: typing.Optional[typing.Literal['CHAP', 'MS-CHAPv1', 'MS-CHAPv2', 'PAP']]

### DisplayLabel
- **Type**: typing.Optional[str]

### UseSameUsername
- **Type**: typing.Optional[bool]


# RadiusSettingsOutputTypeDef

### RadiusServers
- **Type**: typing.Optional[typing.List[str]]

### RadiusPort
- **Type**: typing.Optional[int]

### RadiusTimeout
- **Type**: typing.Optional[int]

### RadiusRetries
- **Type**: typing.Optional[int]

### SharedSecret
- **Type**: typing.Optional[str]

### AuthenticationProtocol
- **Type**: typing.Optional[typing.Literal['CHAP', 'MS-CHAPv1', 'MS-CHAPv2', 'PAP']]

### DisplayLabel
- **Type**: typing.Optional[str]

### UseSameUsername
- **Type**: typing.Optional[bool]


# RadiusSettingsTypeDef

### RadiusServers
- **Type**: typing.Optional[typing.Sequence[str]]

### RadiusPort
- **Type**: typing.Optional[int]

### RadiusTimeout
- **Type**: typing.Optional[int]

### RadiusRetries
- **Type**: typing.Optional[int]

### SharedSecret
- **Type**: typing.Optional[str]

### AuthenticationProtocol
- **Type**: typing.Optional[typing.Literal['CHAP', 'MS-CHAPv1', 'MS-CHAPv2', 'PAP']]

### DisplayLabel
- **Type**: typing.Optional[str]

### UseSameUsername
- **Type**: typing.Optional[bool]


# RegionDescriptionTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### RegionName
- **Type**: typing.Optional[str]

### RegionType
- **Type**: typing.Optional[typing.Literal['Additional', 'Primary']]

### Status
- **Type**: typing.Optional[typing.Literal['Active', 'Created', 'Creating', 'Deleted', 'Deleting', 'Failed', 'Impaired', 'Inoperable', 'Requested', 'RestoreFailed', 'Restoring']]

### VpcSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.DirectoryVpcSettingsOutputTypeDef]

### DesiredNumberOfDomainControllers
- **Type**: typing.Optional[int]

### LaunchTime
- **Type**: typing.Optional[datetime.datetime]

### StatusLastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# RegionsInfoTypeDef

### PrimaryRegion
- **Type**: typing.Optional[str]

### AdditionalRegions
- **Type**: typing.Optional[typing.List[str]]


# RegisterCertificateRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateData
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Optional[typing.Literal['ClientCertAuth', 'ClientLDAPS']]

### ClientCertAuthSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.ClientCertAuthSettingsTypeDef]


# RegisterCertificateResultTypeDef

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterEventTopicRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes


# RejectSharedDirectoryRequestRequestTypeDef

### SharedDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# RejectSharedDirectoryResultTypeDef

### SharedDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveIpRoutesRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### CidrIps
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RemoveRegionRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveTagsFromResourceRequestRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResetUserPasswordRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### NewPassword
- **Type**: <class 'str'>
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


# RestoreFromSnapshotRequestRequestTypeDef

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes


# SchemaExtensionInfoTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### SchemaExtensionId
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### SchemaExtensionStatus
- **Type**: typing.Optional[typing.Literal['CancelInProgress', 'Cancelled', 'Completed', 'CreatingSnapshot', 'Failed', 'Initializing', 'Replicating', 'RollbackInProgress', 'UpdatingSchema']]

### SchemaExtensionStatusReason
- **Type**: typing.Optional[str]

### StartDateTime
- **Type**: typing.Optional[datetime.datetime]

### EndDateTime
- **Type**: typing.Optional[datetime.datetime]


# SettingEntryTypeDef

### Type
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### AllowedValues
- **Type**: typing.Optional[str]

### AppliedValue
- **Type**: typing.Optional[str]

### RequestedValue
- **Type**: typing.Optional[str]

### RequestStatus
- **Type**: typing.Optional[typing.Literal['Default', 'Failed', 'Requested', 'Updated', 'Updating']]

### RequestDetailedStatus
- **Type**: typing.Optional[typing.Dict[str, typing.Literal['Default', 'Failed', 'Requested', 'Updated', 'Updating']]]

### RequestStatusMessage
- **Type**: typing.Optional[str]

### LastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### LastRequestedDateTime
- **Type**: typing.Optional[datetime.datetime]

### DataType
- **Type**: typing.Optional[str]


# SettingTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ShareDirectoryRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ShareTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ShareTargetTypeDef'>
- **Required**: Yes

### ShareMethod
- **Type**: typing.Literal['HANDSHAKE', 'ORGANIZATIONS']
- **Required**: Yes

### ShareNotes
- **Type**: typing.Optional[str]


# ShareDirectoryResultTypeDef

### SharedDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ShareTargetTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ACCOUNT']
- **Required**: Yes


# SharedDirectoryTypeDef

### OwnerAccountId
- **Type**: typing.Optional[str]

### OwnerDirectoryId
- **Type**: typing.Optional[str]

### ShareMethod
- **Type**: typing.Optional[typing.Literal['HANDSHAKE', 'ORGANIZATIONS']]

### SharedAccountId
- **Type**: typing.Optional[str]

### SharedDirectoryId
- **Type**: typing.Optional[str]

### ShareStatus
- **Type**: typing.Optional[typing.Literal['Deleted', 'Deleting', 'PendingAcceptance', 'RejectFailed', 'Rejected', 'Rejecting', 'ShareFailed', 'Shared', 'Sharing']]

### ShareNotes
- **Type**: typing.Optional[str]

### CreatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# SnapshotLimitsTypeDef

### ManualSnapshotsLimit
- **Type**: typing.Optional[int]

### ManualSnapshotsCurrentCount
- **Type**: typing.Optional[int]

### ManualSnapshotsLimitReached
- **Type**: typing.Optional[bool]


# SnapshotTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### SnapshotId
- **Type**: typing.Optional[str]

### Type
- **Type**: typing.Optional[typing.Literal['Auto', 'Manual']]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Completed', 'Creating', 'Failed']]

### StartTime
- **Type**: typing.Optional[datetime.datetime]


# StartSchemaExtensionRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### CreateSnapshotBeforeSchemaExtension
- **Type**: <class 'bool'>
- **Required**: Yes

### LdifContent
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes


# StartSchemaExtensionResultTypeDef

### SchemaExtensionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TrustTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### TrustId
- **Type**: typing.Optional[str]

### RemoteDomainName
- **Type**: typing.Optional[str]

### TrustType
- **Type**: typing.Optional[typing.Literal['External', 'Forest']]

### TrustDirection
- **Type**: typing.Optional[typing.Literal['One-Way: Incoming', 'One-Way: Outgoing', 'Two-Way']]

### TrustState
- **Type**: typing.Optional[typing.Literal['Created', 'Creating', 'Deleted', 'Deleting', 'Failed', 'UpdateFailed', 'Updated', 'Updating', 'Verified', 'VerifyFailed', 'Verifying']]

### CreatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### StateLastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]

### TrustStateReason
- **Type**: typing.Optional[str]

### SelectiveAuth
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# UnshareDirectoryRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UnshareTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.UnshareTargetTypeDef'>
- **Required**: Yes


# UnshareDirectoryResultTypeDef

### SharedDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UnshareTargetTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['ACCOUNT']
- **Required**: Yes


# UpdateConditionalForwarderRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DnsIpAddrs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDirectorySetupRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateType
- **Type**: typing.Literal['OS']
- **Required**: Yes

### OSUpdateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.OSUpdateSettingsTypeDef]

### CreateSnapshotBeforeUpdate
- **Type**: typing.Optional[bool]


# UpdateInfoEntryTypeDef

### Region
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['UpdateFailed', 'Updated', 'Updating']]

### StatusReason
- **Type**: typing.Optional[str]

### InitiatedBy
- **Type**: typing.Optional[str]

### NewValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.UpdateValueTypeDef]

### PreviousValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.UpdateValueTypeDef]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# UpdateNumberOfDomainControllersRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredNumber
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateRadiusRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RadiusSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.RadiusSettingsTypeDef'>
- **Required**: Yes


# UpdateSettingsRequestRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.SettingTypeDef]
- **Required**: Yes


# UpdateSettingsResultTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateTrustRequestRequestTypeDef

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectiveAuth
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# UpdateTrustResultTypeDef

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateValueTypeDef

### OSUpdateSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.OSUpdateSettingsTypeDef]


# VerifyTrustRequestRequestTypeDef

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyTrustResultTypeDef

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


