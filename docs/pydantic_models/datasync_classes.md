# Datasync Classes

# AddStorageSystemRequest

### ServerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.DiscoveryServerConfiguration'>
- **Required**: Yes

### SystemType
- **Type**: typing.Literal['NetAppONTAP']
- **Required**: Yes

### AgentArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Credentials
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.Credentials'>
- **Required**: Yes

### CloudWatchLogGroupArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]

### Name
- **Type**: typing.Optional[str]


# AddStorageSystemResponse

### StorageSystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# AgentListEntry

### AgentArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['OFFLINE', 'ONLINE']]

### Platform
- **Type**: <class 'NoneType'>


# AzureBlobSasConfiguration

### Token
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Blob

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelTaskExecutionRequest

### TaskExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes


# Capacity

### Used
- **Type**: typing.Optional[int]

### Provisioned
- **Type**: typing.Optional[int]

### LogicalUsed
- **Type**: typing.Optional[int]

### ClusterCloudStorageUsed
- **Type**: typing.Optional[int]


# CreateAgentRequest

### ActivationKey
- **Type**: <class 'str'>
- **Required**: Yes

### AgentName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]

### VpcEndpointId
- **Type**: typing.Optional[str]

### SubnetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupArns
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateAgentResponse

### AgentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLocationAzureBlobRequest

### ContainerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['SAS']
- **Required**: Yes

### AgentArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### SasConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.AzureBlobSasConfiguration]

### BlobType
- **Type**: typing.Optional[typing.Literal['BLOCK']]

### AccessTier
- **Type**: typing.Optional[typing.Literal['ARCHIVE', 'COOL', 'HOT']]

### Subdirectory
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]


# CreateLocationAzureBlobResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLocationEfsRequest

### EfsFilesystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### Ec2Config
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.Ec2ConfigUnion'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]

### AccessPointArn
- **Type**: typing.Optional[str]

### FileSystemAccessRoleArn
- **Type**: typing.Optional[str]

### InTransitEncryption
- **Type**: typing.Optional[typing.Literal['NONE', 'TLS1_2']]


# CreateLocationEfsResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLocationFsxLustreRequest

### FsxFilesystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]


# CreateLocationFsxLustreResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLocationFsxOntapResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLocationFsxOpenZfsResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLocationFsxWindowsRequest

### FsxFilesystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### User
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]

### Domain
- **Type**: typing.Optional[str]


# CreateLocationFsxWindowsResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLocationHdfsRequest

### NameNodes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.HdfsNameNode]
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['KERBEROS', 'SIMPLE']
- **Required**: Yes

### AgentArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### BlockSize
- **Type**: typing.Optional[int]

### ReplicationFactor
- **Type**: typing.Optional[int]

### KmsKeyProviderUri
- **Type**: typing.Optional[str]

### QopConfiguration
- **Type**: <class 'NoneType'>

### SimpleUser
- **Type**: typing.Optional[str]

### KerberosPrincipal
- **Type**: typing.Optional[str]

### KerberosKeytab
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Blob]

### KerberosKrb5Conf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Blob]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]


# CreateLocationHdfsResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLocationNfsRequest

### Subdirectory
- **Type**: <class 'str'>
- **Required**: Yes

### ServerHostname
- **Type**: <class 'str'>
- **Required**: Yes

### OnPremConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.OnPremConfigUnion'>
- **Required**: Yes

### MountOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.NfsMountOptions]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]


# CreateLocationNfsResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLocationObjectStorageRequest

### ServerHostname
- **Type**: <class 'str'>
- **Required**: Yes

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### AgentArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ServerPort
- **Type**: typing.Optional[int]

### ServerProtocol
- **Type**: typing.Optional[typing.Literal['HTTP', 'HTTPS']]

### Subdirectory
- **Type**: typing.Optional[str]

### AccessKey
- **Type**: typing.Optional[str]

### SecretKey
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]

### ServerCertificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Blob]


# CreateLocationObjectStorageResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLocationS3Request

### S3BucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3Config
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.S3Config'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### S3StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_INSTANT_RETRIEVAL', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'OUTPOSTS', 'STANDARD', 'STANDARD_IA']]

### AgentArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]


# CreateLocationS3Response

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLocationSmbRequest

### Subdirectory
- **Type**: <class 'str'>
- **Required**: Yes

### ServerHostname
- **Type**: <class 'str'>
- **Required**: Yes

### AgentArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### User
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### MountOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.SmbMountOptions]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['KERBEROS', 'NTLM']]

### DnsIpAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### KerberosPrincipal
- **Type**: typing.Optional[str]

### KerberosKeytab
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Blob]

### KerberosKrb5Conf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Blob]


# CreateLocationSmbResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTaskRequest

### SourceLocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationLocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLogGroupArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Options
- **Type**: <class 'NoneType'>

### Excludes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.FilterRule]]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.TaskSchedule]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]

### Includes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.FilterRule]]

### ManifestConfig
- **Type**: <class 'NoneType'>

### TaskReportConfig
- **Type**: <class 'NoneType'>

### TaskMode
- **Type**: typing.Optional[typing.Literal['BASIC', 'ENHANCED']]


# CreateTaskResponse

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# Credentials

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAgentRequest

### AgentArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLocationRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTaskRequest

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAgentRequest

### AgentArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAgentResponse

### AgentArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['OFFLINE', 'ONLINE']
- **Required**: Yes

### LastConnectionTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndpointType
- **Type**: typing.Literal['FIPS', 'PRIVATE_LINK', 'PUBLIC']
- **Required**: Yes

### PrivateLinkConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.PrivateLinkConfig'>
- **Required**: Yes

### Platform
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.Platform'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeDiscoveryJobRequest

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDiscoveryJobResponse

### StorageSystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CollectionDurationMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETED', 'COMPLETED_WITH_ISSUES', 'FAILED', 'RUNNING', 'STOPPED', 'TERMINATED', 'WARNING']
- **Required**: Yes

### JobStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### JobEndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLocationAzureBlobRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationAzureBlobResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['SAS']
- **Required**: Yes

### BlobType
- **Type**: typing.Literal['BLOCK']
- **Required**: Yes

### AccessTier
- **Type**: typing.Literal['ARCHIVE', 'COOL', 'HOT']
- **Required**: Yes

### AgentArns
- **Type**: typing.List[str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLocationEfsRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationEfsResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### Ec2Config
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.Ec2ConfigOutput'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### InTransitEncryption
- **Type**: typing.Literal['NONE', 'TLS1_2']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLocationFsxLustreRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationFsxLustreResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupArns
- **Type**: typing.List[str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLocationFsxOntapRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationFsxOpenZfsRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationFsxWindowsRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationFsxWindowsResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupArns
- **Type**: typing.List[str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### User
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLocationHdfsRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationHdfsResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### NameNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.HdfsNameNode]
- **Required**: Yes

### BlockSize
- **Type**: <class 'int'>
- **Required**: Yes

### ReplicationFactor
- **Type**: <class 'int'>
- **Required**: Yes

### KmsKeyProviderUri
- **Type**: <class 'str'>
- **Required**: Yes

### QopConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.QopConfiguration'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['KERBEROS', 'SIMPLE']
- **Required**: Yes

### SimpleUser
- **Type**: <class 'str'>
- **Required**: Yes

### KerberosPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### AgentArns
- **Type**: typing.List[str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLocationNfsRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationNfsResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### OnPremConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.OnPremConfigOutput'>
- **Required**: Yes

### MountOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.NfsMountOptions'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLocationObjectStorageRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationObjectStorageResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### AccessKey
- **Type**: <class 'str'>
- **Required**: Yes

### ServerPort
- **Type**: <class 'int'>
- **Required**: Yes

### ServerProtocol
- **Type**: typing.Literal['HTTP', 'HTTPS']
- **Required**: Yes

### AgentArns
- **Type**: typing.List[str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ServerCertificate
- **Type**: <class 'bytes'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLocationS3Request

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationS3Response

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### S3StorageClass
- **Type**: typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_INSTANT_RETRIEVAL', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'OUTPOSTS', 'STANDARD', 'STANDARD_IA']
- **Required**: Yes

### S3Config
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.S3Config'>
- **Required**: Yes

### AgentArns
- **Type**: typing.List[str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLocationSmbRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationSmbResponse

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### AgentArns
- **Type**: typing.List[str]
- **Required**: Yes

### User
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: <class 'str'>
- **Required**: Yes

### MountOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.SmbMountOptions'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DnsIpAddresses
- **Type**: typing.List[str]
- **Required**: Yes

### KerberosPrincipal
- **Type**: <class 'str'>
- **Required**: Yes

### AuthenticationType
- **Type**: typing.Literal['KERBEROS', 'NTLM']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStorageSystemRequest

### StorageSystemArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStorageSystemResourceMetricsRequest

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['CLUSTER', 'SVM', 'VOLUME']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Timestamp]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeStorageSystemResourceMetricsRequestPaginate

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['CLUSTER', 'SVM', 'VOLUME']
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Timestamp]

### EndTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Timestamp]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfig]


# DescribeStorageSystemResourceMetricsResponse

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.ResourceMetrics]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStorageSystemResourcesRequest

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['CLUSTER', 'SVM', 'VOLUME']
- **Required**: Yes

### ResourceIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filter
- **Type**: typing.Optional[typing.Mapping[typing.Literal['SVM'], typing.Sequence[str]]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeStorageSystemResourcesResponse

### ResourceDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResourceDetails'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStorageSystemResponse

### StorageSystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.DiscoveryServerConfiguration'>
- **Required**: Yes

### SystemType
- **Type**: typing.Literal['NetAppONTAP']
- **Required**: Yes

### AgentArns
- **Type**: typing.List[str]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ConnectivityStatus
- **Type**: typing.Literal['FAIL', 'PASS', 'UNKNOWN']
- **Required**: Yes

### CloudWatchLogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SecretsManagerArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTaskExecutionRequest

### TaskExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTaskExecutionResponse

### TaskExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELLING', 'ERROR', 'LAUNCHING', 'PREPARING', 'QUEUED', 'SUCCESS', 'TRANSFERRING', 'VERIFYING']
- **Required**: Yes

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.Options'>
- **Required**: Yes

### Excludes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.FilterRule]
- **Required**: Yes

### Includes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.FilterRule]
- **Required**: Yes

### ManifestConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ManifestConfig'>
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EstimatedFilesToTransfer
- **Type**: <class 'int'>
- **Required**: Yes

### EstimatedBytesToTransfer
- **Type**: <class 'int'>
- **Required**: Yes

### FilesTransferred
- **Type**: <class 'int'>
- **Required**: Yes

### BytesWritten
- **Type**: <class 'int'>
- **Required**: Yes

### BytesTransferred
- **Type**: <class 'int'>
- **Required**: Yes

### BytesCompressed
- **Type**: <class 'int'>
- **Required**: Yes

### Result
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.TaskExecutionResultDetail'>
- **Required**: Yes

### TaskReportConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.TaskReportConfig'>
- **Required**: Yes

### FilesDeleted
- **Type**: <class 'int'>
- **Required**: Yes

### FilesSkipped
- **Type**: <class 'int'>
- **Required**: Yes

### FilesVerified
- **Type**: <class 'int'>
- **Required**: Yes

### ReportResult
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ReportResult'>
- **Required**: Yes

### EstimatedFilesToDelete
- **Type**: <class 'int'>
- **Required**: Yes

### TaskMode
- **Type**: typing.Literal['BASIC', 'ENHANCED']
- **Required**: Yes

### FilesPrepared
- **Type**: <class 'int'>
- **Required**: Yes

### FilesListed
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.TaskExecutionFilesListedDetail'>
- **Required**: Yes

### FilesFailed
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.TaskExecutionFilesFailedDetail'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTaskRequest

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTaskResponse

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'QUEUED', 'RUNNING', 'UNAVAILABLE']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentTaskExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationLocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLogGroupArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceNetworkInterfaceArns
- **Type**: typing.List[str]
- **Required**: Yes

### DestinationNetworkInterfaceArns
- **Type**: typing.List[str]
- **Required**: Yes

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.Options'>
- **Required**: Yes

### Excludes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.FilterRule]
- **Required**: Yes

### Schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.TaskSchedule'>
- **Required**: Yes

### ErrorCode
- **Type**: <class 'str'>
- **Required**: Yes

### ErrorDetail
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Includes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.FilterRule]
- **Required**: Yes

### ManifestConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ManifestConfig'>
- **Required**: Yes

### TaskReportConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.TaskReportConfig'>
- **Required**: Yes

### ScheduleDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.TaskScheduleDetails'>
- **Required**: Yes

### TaskMode
- **Type**: typing.Literal['BASIC', 'ENHANCED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# DiscoveryJobListEntry

### DiscoveryJobArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ISSUES', 'FAILED', 'RUNNING', 'STOPPED', 'TERMINATED', 'WARNING']]


# DiscoveryServerConfiguration

### ServerHostname
- **Type**: <class 'str'>
- **Required**: Yes

### ServerPort
- **Type**: typing.Optional[int]


# Ec2Config

### SubnetArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# Ec2ConfigOutput

### SubnetArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupArns
- **Type**: typing.List[str]
- **Required**: Yes


# Ec2ConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# FilterRule

### FilterType
- **Type**: typing.Optional[typing.Literal['SIMPLE_PATTERN']]

### Value
- **Type**: typing.Optional[str]


# FsxProtocol

### NFS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.FsxProtocolNfs]

### SMB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.FsxProtocolSmb]


# FsxProtocolNfs

### MountOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.NfsMountOptions]


# FsxProtocolSmb

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### User
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]

### MountOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.SmbMountOptions]


# FsxUpdateProtocol

### NFS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.FsxProtocolNfs]

### SMB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.FsxUpdateProtocolSmb]


# FsxUpdateProtocolSmb

### Domain
- **Type**: typing.Optional[str]

### MountOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.SmbMountOptions]

### Password
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[str]


# GenerateRecommendationsRequest

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['CLUSTER', 'SVM', 'VOLUME']
- **Required**: Yes


# HdfsNameNode

### Hostname
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes


# IOPS

### Read
- **Type**: typing.Optional[float]

### Write
- **Type**: typing.Optional[float]

### Other
- **Type**: typing.Optional[float]

### Total
- **Type**: typing.Optional[float]


# Latency

### Read
- **Type**: typing.Optional[float]

### Write
- **Type**: typing.Optional[float]

### Other
- **Type**: typing.Optional[float]


# ListAgentsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAgentsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfig]


# ListAgentsResponse

### Agents
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.AgentListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDiscoveryJobsRequest

### StorageSystemArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDiscoveryJobsRequestPaginate

### StorageSystemArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfig]


# ListDiscoveryJobsResponse

### DiscoveryJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.DiscoveryJobListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLocationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.LocationFilter]]


# ListLocationsRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.LocationFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfig]


# ListLocationsResponse

### Locations
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.LocationListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStorageSystemsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListStorageSystemsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfig]


# ListStorageSystemsResponse

### StorageSystems
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.StorageSystemListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfig]


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTaskExecutionsRequest

### TaskArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTaskExecutionsRequestPaginate

### TaskArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfig]


# ListTaskExecutionsResponse

### TaskExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.TaskExecutionListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTasksRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TaskFilter]]


# ListTasksRequestPaginate

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TaskFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfig]


# ListTasksResponse

### Tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.TaskListEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LocationFilter

### Name
- **Type**: typing.Literal['CreationTime', 'LocationType', 'LocationUri']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['BeginsWith', 'Contains', 'Equals', 'GreaterThan', 'GreaterThanOrEqual', 'In', 'LessThan', 'LessThanOrEqual', 'NotContains', 'NotEquals']
- **Required**: Yes


# LocationListEntry

### LocationArn
- **Type**: typing.Optional[str]

### LocationUri
- **Type**: typing.Optional[str]


# ManifestConfig

### Action
- **Type**: typing.Optional[typing.Literal['TRANSFER']]

### Format
- **Type**: typing.Optional[typing.Literal['CSV']]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.SourceManifestConfig]


# MaxP95Performance

### IopsRead
- **Type**: typing.Optional[float]

### IopsWrite
- **Type**: typing.Optional[float]

### IopsOther
- **Type**: typing.Optional[float]

### IopsTotal
- **Type**: typing.Optional[float]

### ThroughputRead
- **Type**: typing.Optional[float]

### ThroughputWrite
- **Type**: typing.Optional[float]

### ThroughputOther
- **Type**: typing.Optional[float]

### ThroughputTotal
- **Type**: typing.Optional[float]

### LatencyRead
- **Type**: typing.Optional[float]

### LatencyWrite
- **Type**: typing.Optional[float]

### LatencyOther
- **Type**: typing.Optional[float]


# NetAppONTAPCluster

### CifsShareCount
- **Type**: typing.Optional[int]

### NfsExportedVolumes
- **Type**: typing.Optional[int]

### ResourceId
- **Type**: typing.Optional[str]

### ClusterName
- **Type**: typing.Optional[str]

### MaxP95Performance
- **Type**: <class 'NoneType'>

### ClusterBlockStorageSize
- **Type**: typing.Optional[int]

### ClusterBlockStorageUsed
- **Type**: typing.Optional[int]

### ClusterBlockStorageLogicalUsed
- **Type**: typing.Optional[int]

### Recommendations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datasync_classes.Recommendation]]

### RecommendationStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'NONE']]

### LunCount
- **Type**: typing.Optional[int]

### ClusterCloudStorageUsed
- **Type**: typing.Optional[int]


# NetAppONTAPSVM

### ClusterUuid
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### SvmName
- **Type**: typing.Optional[str]

### CifsShareCount
- **Type**: typing.Optional[int]

### EnabledProtocols
- **Type**: typing.Optional[typing.List[str]]

### TotalCapacityUsed
- **Type**: typing.Optional[int]

### TotalCapacityProvisioned
- **Type**: typing.Optional[int]

### TotalLogicalCapacityUsed
- **Type**: typing.Optional[int]

### MaxP95Performance
- **Type**: <class 'NoneType'>

### Recommendations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datasync_classes.Recommendation]]

### NfsExportedVolumes
- **Type**: typing.Optional[int]

### RecommendationStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'NONE']]

### TotalSnapshotCapacityUsed
- **Type**: typing.Optional[int]

### LunCount
- **Type**: typing.Optional[int]


# NetAppONTAPVolume

### VolumeName
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### CifsShareCount
- **Type**: typing.Optional[int]

### SecurityStyle
- **Type**: typing.Optional[str]

### SvmUuid
- **Type**: typing.Optional[str]

### SvmName
- **Type**: typing.Optional[str]

### CapacityUsed
- **Type**: typing.Optional[int]

### CapacityProvisioned
- **Type**: typing.Optional[int]

### LogicalCapacityUsed
- **Type**: typing.Optional[int]

### NfsExported
- **Type**: typing.Optional[bool]

### SnapshotCapacityUsed
- **Type**: typing.Optional[int]

### MaxP95Performance
- **Type**: <class 'NoneType'>

### Recommendations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datasync_classes.Recommendation]]

### RecommendationStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'NONE']]

### LunCount
- **Type**: typing.Optional[int]


# NfsMountOptions

### Version
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'NFS3', 'NFS4_0', 'NFS4_1']]


# OnPremConfig

### AgentArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# OnPremConfigOutput

### AgentArns
- **Type**: typing.List[str]
- **Required**: Yes


# OnPremConfigUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Options

### VerifyMode
- **Type**: typing.Optional[typing.Literal['NONE', 'ONLY_FILES_TRANSFERRED', 'POINT_IN_TIME_CONSISTENT']]

### OverwriteMode
- **Type**: typing.Optional[typing.Literal['ALWAYS', 'NEVER']]

### Atime
- **Type**: typing.Optional[typing.Literal['BEST_EFFORT', 'NONE']]

### Mtime
- **Type**: typing.Optional[typing.Literal['NONE', 'PRESERVE']]

### Uid
- **Type**: typing.Optional[typing.Literal['BOTH', 'INT_VALUE', 'NAME', 'NONE']]

### Gid
- **Type**: typing.Optional[typing.Literal['BOTH', 'INT_VALUE', 'NAME', 'NONE']]

### PreserveDeletedFiles
- **Type**: typing.Optional[typing.Literal['PRESERVE', 'REMOVE']]

### PreserveDevices
- **Type**: typing.Optional[typing.Literal['NONE', 'PRESERVE']]

### PosixPermissions
- **Type**: typing.Optional[typing.Literal['NONE', 'PRESERVE']]

### BytesPerSecond
- **Type**: typing.Optional[int]

### TaskQueueing
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]

### LogLevel
- **Type**: typing.Optional[typing.Literal['BASIC', 'OFF', 'TRANSFER']]

### TransferMode
- **Type**: typing.Optional[typing.Literal['ALL', 'CHANGED']]

### SecurityDescriptorCopyFlags
- **Type**: typing.Optional[typing.Literal['NONE', 'OWNER_DACL', 'OWNER_DACL_SACL']]

### ObjectTags
- **Type**: typing.Optional[typing.Literal['NONE', 'PRESERVE']]


# P95Metrics

### IOPS
- **Type**: <class 'NoneType'>

### Throughput
- **Type**: <class 'NoneType'>

### Latency
- **Type**: <class 'NoneType'>


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Platform

### Version
- **Type**: typing.Optional[str]


# PrivateLinkConfig

### VpcEndpointId
- **Type**: typing.Optional[str]

### PrivateLinkEndpoint
- **Type**: typing.Optional[str]

### SubnetArns
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupArns
- **Type**: typing.Optional[typing.List[str]]


# QopConfiguration

### RpcProtection
- **Type**: typing.Optional[typing.Literal['AUTHENTICATION', 'DISABLED', 'INTEGRITY', 'PRIVACY']]

### DataTransferProtection
- **Type**: typing.Optional[typing.Literal['AUTHENTICATION', 'DISABLED', 'INTEGRITY', 'PRIVACY']]


# Recommendation

### StorageType
- **Type**: typing.Optional[str]

### StorageConfiguration
- **Type**: typing.Optional[typing.Dict[str, str]]

### EstimatedMonthlyStorageCost
- **Type**: typing.Optional[str]


# RemoveStorageSystemRequest

### StorageSystemArn
- **Type**: <class 'str'>
- **Required**: Yes


# ReportDestination

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportDestinationS3]


# ReportDestinationS3

### S3BucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### BucketAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]


# ReportOverride

### ReportLevel
- **Type**: typing.Optional[typing.Literal['ERRORS_ONLY', 'SUCCESSES_AND_ERRORS']]


# ReportOverrides

### Transferred
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportOverride]

### Verified
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportOverride]

### Deleted
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportOverride]

### Skipped
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportOverride]


# ReportResult

### Status
- **Type**: typing.Optional[typing.Literal['ERROR', 'PENDING', 'SUCCESS']]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorDetail
- **Type**: typing.Optional[str]


# ResourceDetails

### NetAppONTAPSVMs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datasync_classes.NetAppONTAPSVM]]

### NetAppONTAPVolumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datasync_classes.NetAppONTAPVolume]]

### NetAppONTAPClusters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datasync_classes.NetAppONTAPCluster]]


# ResourceMetrics

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### P95Metrics
- **Type**: <class 'NoneType'>

### Capacity
- **Type**: <class 'NoneType'>

### ResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'SVM', 'VOLUME']]


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


# S3Config

### BucketAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# S3ManifestConfig

### ManifestObjectPath
- **Type**: <class 'str'>
- **Required**: Yes

### BucketAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3BucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestObjectVersionId
- **Type**: typing.Optional[str]


# SmbMountOptions

### Version
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'SMB1', 'SMB2', 'SMB2_0', 'SMB3']]


# SourceManifestConfig

### S3
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.S3ManifestConfig'>
- **Required**: Yes


# StartDiscoveryJobRequest

### StorageSystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### CollectionDurationMinutes
- **Type**: <class 'int'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]


# StartDiscoveryJobResponse

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# StartTaskExecutionRequest

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### OverrideOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Options]

### Includes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.FilterRule]]

### Excludes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.FilterRule]]

### ManifestConfig
- **Type**: <class 'NoneType'>

### TaskReportConfig
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]]


# StartTaskExecutionResponse

### TaskExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadata'>
- **Required**: Yes


# StopDiscoveryJobRequest

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# StorageSystemListEntry

### StorageSystemArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# TagListEntry

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntry]
- **Required**: Yes


# TaskExecutionFilesFailedDetail

### Prepare
- **Type**: typing.Optional[int]

### Transfer
- **Type**: typing.Optional[int]

### Verify
- **Type**: typing.Optional[int]

### Delete
- **Type**: typing.Optional[int]


# TaskExecutionFilesListedDetail

### AtSource
- **Type**: typing.Optional[int]

### AtDestinationForDelete
- **Type**: typing.Optional[int]


# TaskExecutionListEntry

### TaskExecutionArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLING', 'ERROR', 'LAUNCHING', 'PREPARING', 'QUEUED', 'SUCCESS', 'TRANSFERRING', 'VERIFYING']]

### TaskMode
- **Type**: typing.Optional[typing.Literal['BASIC', 'ENHANCED']]


# TaskExecutionResultDetail

### PrepareDuration
- **Type**: typing.Optional[int]

### PrepareStatus
- **Type**: typing.Optional[typing.Literal['ERROR', 'PENDING', 'SUCCESS']]

### TotalDuration
- **Type**: typing.Optional[int]

### TransferDuration
- **Type**: typing.Optional[int]

### TransferStatus
- **Type**: typing.Optional[typing.Literal['ERROR', 'PENDING', 'SUCCESS']]

### VerifyDuration
- **Type**: typing.Optional[int]

### VerifyStatus
- **Type**: typing.Optional[typing.Literal['ERROR', 'PENDING', 'SUCCESS']]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorDetail
- **Type**: typing.Optional[str]


# TaskFilter

### Name
- **Type**: typing.Literal['CreationTime', 'LocationId']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['BeginsWith', 'Contains', 'Equals', 'GreaterThan', 'GreaterThanOrEqual', 'In', 'LessThan', 'LessThanOrEqual', 'NotContains', 'NotEquals']
- **Required**: Yes


# TaskListEntry

### TaskArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'QUEUED', 'RUNNING', 'UNAVAILABLE']]

### Name
- **Type**: typing.Optional[str]

### TaskMode
- **Type**: typing.Optional[typing.Literal['BASIC', 'ENHANCED']]


# TaskReportConfig

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportDestination]

### OutputType
- **Type**: typing.Optional[typing.Literal['STANDARD', 'SUMMARY_ONLY']]

### ReportLevel
- **Type**: typing.Optional[typing.Literal['ERRORS_ONLY', 'SUCCESSES_AND_ERRORS']]

### ObjectVersionIds
- **Type**: typing.Optional[typing.Literal['INCLUDE', 'NONE']]

### Overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportOverrides]


# TaskSchedule

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# TaskScheduleDetails

### StatusUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### DisabledReason
- **Type**: typing.Optional[str]

### DisabledBy
- **Type**: typing.Optional[typing.Literal['SERVICE', 'USER']]


# Throughput

### Read
- **Type**: typing.Optional[float]

### Write
- **Type**: typing.Optional[float]

### Other
- **Type**: typing.Optional[float]

### Total
- **Type**: typing.Optional[float]


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Keys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAgentRequest

### AgentArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateDiscoveryJobRequest

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CollectionDurationMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateLocationAzureBlobRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['SAS']]

### SasConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.AzureBlobSasConfiguration]

### BlobType
- **Type**: typing.Optional[typing.Literal['BLOCK']]

### AccessTier
- **Type**: typing.Optional[typing.Literal['ARCHIVE', 'COOL', 'HOT']]

### AgentArns
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateLocationEfsRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### AccessPointArn
- **Type**: typing.Optional[str]

### FileSystemAccessRoleArn
- **Type**: typing.Optional[str]

### InTransitEncryption
- **Type**: typing.Optional[typing.Literal['NONE', 'TLS1_2']]


# UpdateLocationFsxLustreRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]


# UpdateLocationFsxWindowsRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]


# UpdateLocationHdfsRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### NameNodes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.HdfsNameNode]]

### BlockSize
- **Type**: typing.Optional[int]

### ReplicationFactor
- **Type**: typing.Optional[int]

### KmsKeyProviderUri
- **Type**: typing.Optional[str]

### QopConfiguration
- **Type**: <class 'NoneType'>

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['KERBEROS', 'SIMPLE']]

### SimpleUser
- **Type**: typing.Optional[str]

### KerberosPrincipal
- **Type**: typing.Optional[str]

### KerberosKeytab
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Blob]

### KerberosKrb5Conf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Blob]

### AgentArns
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateLocationNfsRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### ServerHostname
- **Type**: typing.Optional[str]

### OnPremConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.OnPremConfigUnion]

### MountOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.NfsMountOptions]


# UpdateLocationObjectStorageRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServerPort
- **Type**: typing.Optional[int]

### ServerProtocol
- **Type**: typing.Optional[typing.Literal['HTTP', 'HTTPS']]

### Subdirectory
- **Type**: typing.Optional[str]

### ServerHostname
- **Type**: typing.Optional[str]

### AccessKey
- **Type**: typing.Optional[str]

### SecretKey
- **Type**: typing.Optional[str]

### AgentArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ServerCertificate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Blob]


# UpdateLocationS3Request

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### S3StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_INSTANT_RETRIEVAL', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'OUTPOSTS', 'STANDARD', 'STANDARD_IA']]

### S3Config
- **Type**: <class 'NoneType'>


# UpdateLocationSmbRequest

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### ServerHostname
- **Type**: typing.Optional[str]

### User
- **Type**: typing.Optional[str]

### Domain
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### AgentArns
- **Type**: typing.Optional[typing.Sequence[str]]

### MountOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.SmbMountOptions]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['KERBEROS', 'NTLM']]

### DnsIpAddresses
- **Type**: typing.Optional[typing.Sequence[str]]

### KerberosPrincipal
- **Type**: typing.Optional[str]

### KerberosKeytab
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Blob]

### KerberosKrb5Conf
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.Blob]


# UpdateStorageSystemRequest

### StorageSystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.DiscoveryServerConfiguration]

### AgentArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Name
- **Type**: typing.Optional[str]

### CloudWatchLogGroupArn
- **Type**: typing.Optional[str]

### Credentials
- **Type**: <class 'NoneType'>


# UpdateTaskExecutionRequest

### TaskExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.Options'>
- **Required**: Yes


# UpdateTaskRequest

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### Options
- **Type**: <class 'NoneType'>

### Excludes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.FilterRule]]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.TaskSchedule]

### Name
- **Type**: typing.Optional[str]

### CloudWatchLogGroupArn
- **Type**: typing.Optional[str]

### Includes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.FilterRule]]

### ManifestConfig
- **Type**: <class 'NoneType'>

### TaskReportConfig
- **Type**: <class 'NoneType'>


