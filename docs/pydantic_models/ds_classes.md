# Ds Classes

# AcceptSharedDirectoryRequestTypeDef

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


# AddIpRoutesRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### IpRoutes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.IpRouteTypeDef]
- **Required**: Yes

### UpdateSecurityGroupForDirectoryControllers
- **Type**: typing.Optional[bool]


# AddTagsToResourceRequestTypeDef

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

# CancelSchemaExtensionRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaExtensionId
- **Type**: <class 'str'>
- **Required**: Yes


# CertificateInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClientAuthenticationSettingInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# ConnectDirectoryRequestTypeDef

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


# CreateAliasRequestTypeDef

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


# CreateComputerRequestTypeDef

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


# CreateConditionalForwarderRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DnsIpAddrs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CreateDirectoryRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.DirectoryVpcSettingsUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.TagTypeDef]]


# CreateDirectoryResultTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLogSubscriptionRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### LogGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateMicrosoftADRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### VpcSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.DirectoryVpcSettingsUnionTypeDef'>
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


# CreateSnapshotRequestTypeDef

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


# CreateTrustRequestTypeDef

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


# DeleteConditionalForwarderRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectoryRequestTypeDef

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


# DeleteLogSubscriptionRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotRequestTypeDef

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


# DeleteTrustRequestTypeDef

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


# DeregisterCertificateRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterEventTopicRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateRequestTypeDef

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


# DescribeClientAuthenticationSettingsResultTypeDef

### ClientAuthenticationSettingsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.ClientAuthenticationSettingInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConditionalForwardersRequestTypeDef

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


# DescribeDirectoriesRequestPaginateTypeDef

### DirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeDirectoriesRequestTypeDef

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


# DescribeDirectoryDataAccessRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDirectoryDataAccessResultTypeDef

### DataAccessStatus
- **Type**: typing.Literal['Disabled', 'Disabling', 'Enabled', 'Enabling', 'Failed']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDomainControllersRequestPaginateTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainControllerIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeDomainControllersRequestTypeDef

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


# DescribeEventTopicsRequestTypeDef

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


# DescribeLDAPSSettingsResultTypeDef

### LDAPSSettingsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.LDAPSSettingInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

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


# DescribeSettingsRequestTypeDef

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


# DescribeSharedDirectoriesRequestPaginateTypeDef

### OwnerDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SharedDirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeSharedDirectoriesRequestTypeDef

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


# DescribeSnapshotsRequestPaginateTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### SnapshotIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeSnapshotsRequestTypeDef

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


# DescribeTrustsRequestPaginateTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### TrustIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# DescribeTrustsRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# DirectoryVpcSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DisableDirectoryDataAccessRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableRadiusRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableSsoRequestTypeDef

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
- **Type**: typing.Optional[typing.Literal['Active', 'Creating', 'Deleted', 'Deleting', 'Failed', 'Impaired', 'Restoring', 'Updating']]

### StatusReason
- **Type**: typing.Optional[str]

### LaunchTime
- **Type**: typing.Optional[datetime.datetime]

### StatusLastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# EnableDirectoryDataAccessRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# EnableRadiusRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RadiusSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.RadiusSettingsUnionTypeDef'>
- **Required**: Yes


# EnableSsoRequestTypeDef

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


# GetSnapshotLimitsRequestTypeDef

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


# ListCertificatesRequestPaginateTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# ListCertificatesRequestTypeDef

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


# ListIpRoutesRequestPaginateTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# ListIpRoutesRequestTypeDef

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


# ListLogSubscriptionsRequestPaginateTypeDef

### DirectoryId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# ListLogSubscriptionsRequestTypeDef

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


# ListSchemaExtensionsRequestPaginateTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# ListSchemaExtensionsRequestTypeDef

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


# ListTagsForResourceRequestPaginateTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestTypeDef

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


# RadiusSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegionDescriptionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegionsInfoTypeDef

### PrimaryRegion
- **Type**: typing.Optional[str]

### AdditionalRegions
- **Type**: typing.Optional[typing.List[str]]


# RegisterCertificateResultTypeDef

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RegisterEventTopicRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes


# RejectSharedDirectoryRequestTypeDef

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


# RemoveIpRoutesRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### CidrIps
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RemoveRegionRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveTagsFromResourceRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResetUserPasswordRequestTypeDef

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


# RestoreFromSnapshotRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SettingTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ShareDirectoryRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# StartSchemaExtensionRequestTypeDef

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


# UnshareDirectoryRequestTypeDef

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

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateConditionalForwarderRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DnsIpAddrs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDirectorySetupRequestTypeDef

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


# UpdateNumberOfDomainControllersRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredNumber
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateRadiusRequestTypeDef

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RadiusSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.RadiusSettingsUnionTypeDef'>
- **Required**: Yes


# UpdateSettingsRequestTypeDef

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


# UpdateTrustRequestTypeDef

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


# VerifyTrustRequestTypeDef

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


