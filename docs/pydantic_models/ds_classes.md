# Ds Classes

# AcceptSharedDirectoryRequest

### SharedDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# AcceptSharedDirectoryResult

### SharedDirectory
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.SharedDirectory'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# AddIpRoutesRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### IpRoutes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.IpRoute]
- **Required**: Yes

### UpdateSecurityGroupForDirectoryControllers
- **Type**: typing.Optional[bool]


# AddTagsToResourceRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.Tag]
- **Required**: Yes


# Attribute

### Name
- **Type**: typing.Optional[str]

### Value
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelSchemaExtensionRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SchemaExtensionId
- **Type**: <class 'str'>
- **Required**: Yes


# Certificate

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CertificateInfo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClientAuthenticationSettingInfo

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClientCertAuthSettings

### OCSPUrl
- **Type**: typing.Optional[str]


# Computer

### ComputerId
- **Type**: typing.Optional[str]

### ComputerName
- **Type**: typing.Optional[str]

### ComputerAttributes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ds_classes.Attribute]]


# ConditionalForwarder

### RemoteDomainName
- **Type**: typing.Optional[str]

### DnsIpAddrs
- **Type**: typing.Optional[typing.List[str]]

### ReplicationScope
- **Type**: typing.Optional[typing.Literal['Domain']]


# ConnectDirectoryRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.DirectoryConnectSettings'>
- **Required**: Yes

### ShortName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.Tag]]


# ConnectDirectoryResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAliasRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes


# CreateAliasResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Alias
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateComputerRequest

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.Attribute]]


# CreateComputerResult

### Computer
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.Computer'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateConditionalForwarderRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DnsIpAddrs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CreateDirectoryRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.DirectoryVpcSettingsUnion]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.Tag]]


# CreateDirectoryResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLogSubscriptionRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### LogGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# CreateMicrosoftADRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### VpcSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.DirectoryVpcSettingsUnion'>
- **Required**: Yes

### ShortName
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Edition
- **Type**: typing.Optional[typing.Literal['Enterprise', 'Standard']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.Tag]]


# CreateMicrosoftADResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSnapshotRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# CreateSnapshotResult

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTrustRequest

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


# CreateTrustResult

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteConditionalForwarderRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDomainName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectoryRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteDirectoryResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteLogSubscriptionRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotRequest

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotResult

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTrustRequest

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes

### DeleteAssociatedConditionalForwarder
- **Type**: typing.Optional[bool]


# DeleteTrustResult

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# DeregisterCertificateRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DeregisterEventTopicRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCertificateResult

### Certificate
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.Certificate'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeClientAuthenticationSettingsResult

### ClientAuthenticationSettingsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.ClientAuthenticationSettingInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeConditionalForwardersRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDomainNames
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeConditionalForwardersResult

### ConditionalForwarders
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.ConditionalForwarder]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDirectoriesRequest

### DirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeDirectoriesRequestPaginate

### DirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfig]


# DescribeDirectoriesResult

### DirectoryDescriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.DirectoryDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDirectoryDataAccessRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDirectoryDataAccessResult

### DataAccessStatus
- **Type**: typing.Literal['Disabled', 'Disabling', 'Enabled', 'Enabling', 'Failed']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDomainControllersRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainControllerIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeDomainControllersRequestPaginate

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### DomainControllerIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfig]


# DescribeDomainControllersResult

### DomainControllers
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.DomainController]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeEventTopicsRequest

### DirectoryId
- **Type**: typing.Optional[str]

### TopicNames
- **Type**: typing.Optional[typing.Sequence[str]]


# DescribeEventTopicsResult

### EventTopics
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.EventTopic]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLDAPSSettingsResult

### LDAPSSettingsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.LDAPSSettingInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeRegionsResult

### RegionsDescription
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.RegionDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSettingsRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['Default', 'Failed', 'Requested', 'Updated', 'Updating']]

### NextToken
- **Type**: typing.Optional[str]


# DescribeSettingsResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SettingEntries
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.SettingEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSharedDirectoriesRequest

### OwnerDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SharedDirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeSharedDirectoriesRequestPaginate

### OwnerDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### SharedDirectoryIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfig]


# DescribeSharedDirectoriesResult

### SharedDirectories
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.SharedDirectory]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSnapshotsRequest

### DirectoryId
- **Type**: typing.Optional[str]

### SnapshotIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeSnapshotsRequestPaginate

### DirectoryId
- **Type**: typing.Optional[str]

### SnapshotIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfig]


# DescribeSnapshotsResult

### Snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.Snapshot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeTrustsRequest

### DirectoryId
- **Type**: typing.Optional[str]

### TrustIds
- **Type**: typing.Optional[typing.Sequence[str]]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeTrustsRequestPaginate

### DirectoryId
- **Type**: typing.Optional[str]

### TrustIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfig]


# DescribeTrustsResult

### Trusts
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.Trust]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeUpdateDirectoryResult

### UpdateActivities
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.UpdateInfoEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DirectoryConnectSettings

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


# DirectoryConnectSettingsDescription

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


# DirectoryDescription

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DirectoryLimits

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


# DirectoryVpcSettings

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DirectoryVpcSettingsDescription

### VpcId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupId
- **Type**: typing.Optional[str]

### AvailabilityZones
- **Type**: typing.Optional[typing.List[str]]


# DirectoryVpcSettingsOutput

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes


# DirectoryVpcSettingsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DisableDirectoryDataAccessRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableRadiusRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# DisableSsoRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# DomainController

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


# EnableDirectoryDataAccessRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# EnableRadiusRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RadiusSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.RadiusSettingsUnion'>
- **Required**: Yes


# EnableSsoRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# EventTopic

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


# GetDirectoryLimitsResult

### DirectoryLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.DirectoryLimits'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# GetSnapshotLimitsRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSnapshotLimitsResult

### SnapshotLimits
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.SnapshotLimits'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# IpRoute

### CidrIp
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# IpRouteInfo

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


# LDAPSSettingInfo

### LDAPSStatus
- **Type**: typing.Optional[typing.Literal['Disabled', 'EnableFailed', 'Enabled', 'Enabling']]

### LDAPSStatusReason
- **Type**: typing.Optional[str]

### LastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# ListCertificatesRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListCertificatesRequestPaginate

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfig]


# ListCertificatesResult

### CertificatesInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.CertificateInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListIpRoutesRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListIpRoutesRequestPaginate

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfig]


# ListIpRoutesResult

### IpRoutesInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.IpRouteInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLogSubscriptionsRequest

### DirectoryId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListLogSubscriptionsRequestPaginate

### DirectoryId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfig]


# ListLogSubscriptionsResult

### LogSubscriptions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.LogSubscription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSchemaExtensionsRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListSchemaExtensionsRequestPaginate

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfig]


# ListSchemaExtensionsResult

### SchemaExtensionsInfo
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.SchemaExtensionInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTagsForResourceRequestPaginate

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.PaginatorConfig]


# ListTagsForResourceResult

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.ds_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LogSubscription

### DirectoryId
- **Type**: typing.Optional[str]

### LogGroupName
- **Type**: typing.Optional[str]

### SubscriptionCreatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# OSUpdateSettings

### OSVersion
- **Type**: typing.Optional[typing.Literal['SERVER_2012', 'SERVER_2019']]


# OwnerDirectoryDescription

### DirectoryId
- **Type**: typing.Optional[str]

### AccountId
- **Type**: typing.Optional[str]

### DnsIpAddrs
- **Type**: typing.Optional[typing.List[str]]

### VpcSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.DirectoryVpcSettingsDescription]

### RadiusSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.RadiusSettingsOutput]

### RadiusStatus
- **Type**: typing.Optional[typing.Literal['Completed', 'Creating', 'Failed']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RadiusSettings

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


# RadiusSettingsOutput

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


# RadiusSettingsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegionDescription

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RegionsInfo

### PrimaryRegion
- **Type**: typing.Optional[str]

### AdditionalRegions
- **Type**: typing.Optional[typing.List[str]]


# RegisterCertificateResult

### CertificateId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# RegisterEventTopicRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### TopicName
- **Type**: <class 'str'>
- **Required**: Yes


# RejectSharedDirectoryRequest

### SharedDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# RejectSharedDirectoryResult

### SharedDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveIpRoutesRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### CidrIps
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RemoveRegionRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes


# RemoveTagsFromResourceRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# ResetUserPasswordRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### NewPassword
- **Type**: <class 'str'>
- **Required**: Yes


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


# RestoreFromSnapshotRequest

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes


# SchemaExtensionInfo

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


# Setting

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# SettingEntry

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ShareDirectoryRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ShareTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ShareTarget'>
- **Required**: Yes

### ShareMethod
- **Type**: typing.Literal['HANDSHAKE', 'ORGANIZATIONS']
- **Required**: Yes

### ShareNotes
- **Type**: typing.Optional[str]


# ShareDirectoryResult

### SharedDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# ShareTarget

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SharedDirectory

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


# Snapshot

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SnapshotLimits

### ManualSnapshotsLimit
- **Type**: typing.Optional[int]

### ManualSnapshotsCurrentCount
- **Type**: typing.Optional[int]

### ManualSnapshotsLimitReached
- **Type**: typing.Optional[bool]


# StartSchemaExtensionRequest

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


# StartSchemaExtensionResult

### SchemaExtensionId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# Trust

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


# UnshareDirectoryRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UnshareTarget
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.UnshareTarget'>
- **Required**: Yes


# UnshareDirectoryResult

### SharedDirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# UnshareTarget

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UpdateConditionalForwarderRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RemoteDomainName
- **Type**: <class 'str'>
- **Required**: Yes

### DnsIpAddrs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDirectorySetupRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateType
- **Type**: typing.Literal['OS']
- **Required**: Yes

### OSUpdateSettings
- **Type**: <class 'NoneType'>

### CreateSnapshotBeforeUpdate
- **Type**: typing.Optional[bool]


# UpdateInfoEntry

### Region
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['UpdateFailed', 'Updated', 'Updating']]

### StatusReason
- **Type**: typing.Optional[str]

### InitiatedBy
- **Type**: typing.Optional[str]

### NewValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.UpdateValue]

### PreviousValue
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ds_classes.UpdateValue]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedDateTime
- **Type**: typing.Optional[datetime.datetime]


# UpdateNumberOfDomainControllersRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### DesiredNumber
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateRadiusRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### RadiusSettings
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.RadiusSettingsUnion'>
- **Required**: Yes


# UpdateSettingsRequest

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### Settings
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ds_classes.Setting]
- **Required**: Yes


# UpdateSettingsResult

### DirectoryId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateTrustRequest

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes

### SelectiveAuth
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# UpdateTrustResult

### RequestId
- **Type**: <class 'str'>
- **Required**: Yes

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateValue

### OSUpdateSettings
- **Type**: <class 'NoneType'>


# VerifyTrustRequest

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes


# VerifyTrustResult

### TrustId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ds_classes.ResponseMetadata'>
- **Required**: Yes


