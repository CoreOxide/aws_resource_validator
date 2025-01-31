# Datasync Classes

# AddStorageSystemRequestRequestTypeDef

### ServerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.DiscoveryServerConfigurationTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.CredentialsTypeDef'>
- **Required**: Yes

### CloudWatchLogGroupArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]

### Name
- **Type**: typing.Optional[str]


# AddStorageSystemResponseTypeDef

### StorageSystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AgentListEntryTypeDef

### AgentArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['OFFLINE', 'ONLINE']]

### Platform
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PlatformTypeDef]


# AzureBlobSasConfigurationTypeDef

### Token
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelTaskExecutionRequestRequestTypeDef

### TaskExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes


# CapacityTypeDef

### Used
- **Type**: typing.Optional[int]

### Provisioned
- **Type**: typing.Optional[int]

### LogicalUsed
- **Type**: typing.Optional[int]

### ClusterCloudStorageUsed
- **Type**: typing.Optional[int]


# CreateAgentRequestRequestTypeDef

### ActivationKey
- **Type**: <class 'str'>
- **Required**: Yes

### AgentName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]

### VpcEndpointId
- **Type**: typing.Optional[str]

### SubnetArns
- **Type**: typing.Optional[typing.Sequence[str]]

### SecurityGroupArns
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateAgentResponseTypeDef

### AgentArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLocationAzureBlobRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.AzureBlobSasConfigurationTypeDef]

### BlobType
- **Type**: typing.Optional[typing.Literal['BLOCK']]

### AccessTier
- **Type**: typing.Optional[typing.Literal['ARCHIVE', 'COOL', 'HOT']]

### Subdirectory
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]


# CreateLocationAzureBlobResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLocationEfsRequestRequestTypeDef

### EfsFilesystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### Ec2Config
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.Ec2ConfigTypeDef'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]

### AccessPointArn
- **Type**: typing.Optional[str]

### FileSystemAccessRoleArn
- **Type**: typing.Optional[str]

### InTransitEncryption
- **Type**: typing.Optional[typing.Literal['NONE', 'TLS1_2']]


# CreateLocationEfsResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLocationFsxLustreRequestRequestTypeDef

### FsxFilesystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]


# CreateLocationFsxLustreResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLocationFsxOntapRequestRequestTypeDef

### Protocol
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.FsxProtocolTypeDef'>
- **Required**: Yes

### SecurityGroupArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StorageVirtualMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]


# CreateLocationFsxOntapResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLocationFsxOpenZfsRequestRequestTypeDef

### FsxFilesystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### Protocol
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.FsxProtocolTypeDef'>
- **Required**: Yes

### SecurityGroupArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]


# CreateLocationFsxOpenZfsResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLocationFsxWindowsRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]

### Domain
- **Type**: typing.Optional[str]


# CreateLocationFsxWindowsResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLocationHdfsRequestRequestTypeDef

### NameNodes
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.HdfsNameNodeTypeDef]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.QopConfigurationTypeDef]

### SimpleUser
- **Type**: typing.Optional[str]

### KerberosPrincipal
- **Type**: typing.Optional[str]

### KerberosKeytab
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### KerberosKrb5Conf
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]


# CreateLocationHdfsResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLocationNfsRequestRequestTypeDef

### Subdirectory
- **Type**: <class 'str'>
- **Required**: Yes

### ServerHostname
- **Type**: <class 'str'>
- **Required**: Yes

### OnPremConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.OnPremConfigTypeDef'>
- **Required**: Yes

### MountOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.NfsMountOptionsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]


# CreateLocationNfsResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLocationObjectStorageRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]

### ServerCertificate
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# CreateLocationObjectStorageResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLocationS3RequestRequestTypeDef

### S3BucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### S3Config
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.S3ConfigTypeDef'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### S3StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER', 'GLACIER_INSTANT_RETRIEVAL', 'INTELLIGENT_TIERING', 'ONEZONE_IA', 'OUTPOSTS', 'STANDARD', 'STANDARD_IA']]

### AgentArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]


# CreateLocationS3ResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLocationSmbRequestRequestTypeDef

### Subdirectory
- **Type**: <class 'str'>
- **Required**: Yes

### ServerHostname
- **Type**: <class 'str'>
- **Required**: Yes

### User
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### AgentArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]

### MountOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.SmbMountOptionsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]


# CreateLocationSmbResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTaskRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.OptionsTypeDef]

### Excludes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.FilterRuleTypeDef]]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.TaskScheduleTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]

### Includes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.FilterRuleTypeDef]]

### ManifestConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ManifestConfigTypeDef]

### TaskReportConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.TaskReportConfigTypeDef]


# CreateTaskResponseTypeDef

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CredentialsTypeDef

### Username
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAgentRequestRequestTypeDef

### AgentArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLocationRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTaskRequestRequestTypeDef

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAgentRequestRequestTypeDef

### AgentArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAgentResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.PrivateLinkConfigTypeDef'>
- **Required**: Yes

### Platform
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.PlatformTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeDiscoveryJobRequestRequestTypeDef

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeDiscoveryJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLocationAzureBlobRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationAzureBlobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLocationEfsRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationEfsResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### Ec2Config
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.Ec2ConfigOutputTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLocationFsxLustreRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationFsxLustreResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLocationFsxOntapRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationFsxOntapResponseTypeDef

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### Protocol
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.FsxProtocolTypeDef'>
- **Required**: Yes

### SecurityGroupArns
- **Type**: typing.List[str]
- **Required**: Yes

### StorageVirtualMachineArn
- **Type**: <class 'str'>
- **Required**: Yes

### FsxFilesystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLocationFsxOpenZfsRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationFsxOpenZfsResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupArns
- **Type**: typing.List[str]
- **Required**: Yes

### Protocol
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.FsxProtocolTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLocationFsxWindowsRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationFsxWindowsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLocationHdfsRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationHdfsResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### NameNodes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.HdfsNameNodeTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.QopConfigurationTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLocationNfsRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationNfsResponseTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### LocationUri
- **Type**: <class 'str'>
- **Required**: Yes

### OnPremConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.OnPremConfigOutputTypeDef'>
- **Required**: Yes

### MountOptions
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.NfsMountOptionsTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLocationObjectStorageRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationObjectStorageResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLocationS3RequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationS3ResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.S3ConfigTypeDef'>
- **Required**: Yes

### AgentArns
- **Type**: typing.List[str]
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLocationSmbRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLocationSmbResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.SmbMountOptionsTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStorageSystemRequestRequestTypeDef

### StorageSystemArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeStorageSystemResourceMetricsRequestDescribeStorageSystemResourceMetricsPaginateTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfigTypeDef]


# DescribeStorageSystemResourceMetricsRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeStorageSystemResourceMetricsResponseTypeDef

### Metrics
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.ResourceMetricsTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStorageSystemResourcesRequestRequestTypeDef

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


# DescribeStorageSystemResourcesResponseTypeDef

### ResourceDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResourceDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStorageSystemResponseTypeDef

### StorageSystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServerConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.DiscoveryServerConfigurationTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTaskExecutionRequestRequestTypeDef

### TaskExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTaskExecutionResponseTypeDef

### TaskExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELLING', 'ERROR', 'LAUNCHING', 'PREPARING', 'QUEUED', 'SUCCESS', 'TRANSFERRING', 'VERIFYING']
- **Required**: Yes

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.OptionsTypeDef'>
- **Required**: Yes

### Excludes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.FilterRuleTypeDef]
- **Required**: Yes

### Includes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.FilterRuleTypeDef]
- **Required**: Yes

### ManifestConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ManifestConfigTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.TaskExecutionResultDetailTypeDef'>
- **Required**: Yes

### TaskReportConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.TaskReportConfigTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ReportResultTypeDef'>
- **Required**: Yes

### EstimatedFilesToDelete
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTaskRequestRequestTypeDef

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeTaskResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.OptionsTypeDef'>
- **Required**: Yes

### Excludes
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.FilterRuleTypeDef]
- **Required**: Yes

### Schedule
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.TaskScheduleTypeDef'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.FilterRuleTypeDef]
- **Required**: Yes

### ManifestConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ManifestConfigTypeDef'>
- **Required**: Yes

### TaskReportConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.TaskReportConfigTypeDef'>
- **Required**: Yes

### ScheduleDetails
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.TaskScheduleDetailsTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DiscoveryJobListEntryTypeDef

### DiscoveryJobArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'COMPLETED_WITH_ISSUES', 'FAILED', 'RUNNING', 'STOPPED', 'TERMINATED', 'WARNING']]


# DiscoveryServerConfigurationTypeDef

### ServerHostname
- **Type**: <class 'str'>
- **Required**: Yes

### ServerPort
- **Type**: typing.Optional[int]


# Ec2ConfigOutputTypeDef

### SubnetArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupArns
- **Type**: typing.List[str]
- **Required**: Yes


# Ec2ConfigTypeDef

### SubnetArn
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroupArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# FilterRuleTypeDef

### FilterType
- **Type**: typing.Optional[typing.Literal['SIMPLE_PATTERN']]

### Value
- **Type**: typing.Optional[str]


# FsxProtocolNfsTypeDef

### MountOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.NfsMountOptionsTypeDef]


# FsxProtocolSmbTypeDef

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### User
- **Type**: <class 'str'>
- **Required**: Yes

### Domain
- **Type**: typing.Optional[str]

### MountOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.SmbMountOptionsTypeDef]


# FsxProtocolTypeDef

### NFS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.FsxProtocolNfsTypeDef]

### SMB
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.FsxProtocolSmbTypeDef]


# GenerateRecommendationsRequestRequestTypeDef

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ResourceType
- **Type**: typing.Literal['CLUSTER', 'SVM', 'VOLUME']
- **Required**: Yes


# HdfsNameNodeTypeDef

### Hostname
- **Type**: <class 'str'>
- **Required**: Yes

### Port
- **Type**: <class 'int'>
- **Required**: Yes


# IOPSTypeDef

### Read
- **Type**: typing.Optional[float]

### Write
- **Type**: typing.Optional[float]

### Other
- **Type**: typing.Optional[float]

### Total
- **Type**: typing.Optional[float]


# LatencyTypeDef

### Read
- **Type**: typing.Optional[float]

### Write
- **Type**: typing.Optional[float]

### Other
- **Type**: typing.Optional[float]


# ListAgentsRequestListAgentsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfigTypeDef]


# ListAgentsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAgentsResponseTypeDef

### Agents
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.AgentListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDiscoveryJobsRequestListDiscoveryJobsPaginateTypeDef

### StorageSystemArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfigTypeDef]


# ListDiscoveryJobsRequestRequestTypeDef

### StorageSystemArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListDiscoveryJobsResponseTypeDef

### DiscoveryJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.DiscoveryJobListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLocationsRequestListLocationsPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.LocationFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfigTypeDef]


# ListLocationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.LocationFilterTypeDef]]


# ListLocationsResponseTypeDef

### Locations
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.LocationListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStorageSystemsRequestListStorageSystemsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfigTypeDef]


# ListStorageSystemsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListStorageSystemsResponseTypeDef

### StorageSystems
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.StorageSystemListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestListTagsForResourcePaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTaskExecutionsRequestListTaskExecutionsPaginateTypeDef

### TaskArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfigTypeDef]


# ListTaskExecutionsRequestRequestTypeDef

### TaskArn
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTaskExecutionsResponseTypeDef

### TaskExecutions
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.TaskExecutionListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTasksRequestListTasksPaginateTypeDef

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TaskFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.PaginatorConfigTypeDef]


# ListTasksRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TaskFilterTypeDef]]


# ListTasksResponseTypeDef

### Tasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.datasync_classes.TaskListEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LocationFilterTypeDef

### Name
- **Type**: typing.Literal['CreationTime', 'LocationType', 'LocationUri']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['BeginsWith', 'Contains', 'Equals', 'GreaterThan', 'GreaterThanOrEqual', 'In', 'LessThan', 'LessThanOrEqual', 'NotContains', 'NotEquals']
- **Required**: Yes


# LocationListEntryTypeDef

### LocationArn
- **Type**: typing.Optional[str]

### LocationUri
- **Type**: typing.Optional[str]


# ManifestConfigTypeDef

### Action
- **Type**: typing.Optional[typing.Literal['TRANSFER']]

### Format
- **Type**: typing.Optional[typing.Literal['CSV']]

### Source
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.SourceManifestConfigTypeDef]


# MaxP95PerformanceTypeDef

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


# NetAppONTAPClusterTypeDef

### CifsShareCount
- **Type**: typing.Optional[int]

### NfsExportedVolumes
- **Type**: typing.Optional[int]

### ResourceId
- **Type**: typing.Optional[str]

### ClusterName
- **Type**: typing.Optional[str]

### MaxP95Performance
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.MaxP95PerformanceTypeDef]

### ClusterBlockStorageSize
- **Type**: typing.Optional[int]

### ClusterBlockStorageUsed
- **Type**: typing.Optional[int]

### ClusterBlockStorageLogicalUsed
- **Type**: typing.Optional[int]

### Recommendations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datasync_classes.RecommendationTypeDef]]

### RecommendationStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'NONE']]

### LunCount
- **Type**: typing.Optional[int]

### ClusterCloudStorageUsed
- **Type**: typing.Optional[int]


# NetAppONTAPSVMTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.MaxP95PerformanceTypeDef]

### Recommendations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datasync_classes.RecommendationTypeDef]]

### NfsExportedVolumes
- **Type**: typing.Optional[int]

### RecommendationStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'NONE']]

### TotalSnapshotCapacityUsed
- **Type**: typing.Optional[int]

### LunCount
- **Type**: typing.Optional[int]


# NetAppONTAPVolumeTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.MaxP95PerformanceTypeDef]

### Recommendations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datasync_classes.RecommendationTypeDef]]

### RecommendationStatus
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'NONE']]

### LunCount
- **Type**: typing.Optional[int]


# NfsMountOptionsTypeDef

### Version
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'NFS3', 'NFS4_0', 'NFS4_1']]


# OnPremConfigOutputTypeDef

### AgentArns
- **Type**: typing.List[str]
- **Required**: Yes


# OnPremConfigTypeDef

### AgentArns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# OptionsTypeDef

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


# P95MetricsTypeDef

### IOPS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.IOPSTypeDef]

### Throughput
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ThroughputTypeDef]

### Latency
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.LatencyTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlatformTypeDef

### Version
- **Type**: typing.Optional[str]


# PrivateLinkConfigTypeDef

### VpcEndpointId
- **Type**: typing.Optional[str]

### PrivateLinkEndpoint
- **Type**: typing.Optional[str]

### SubnetArns
- **Type**: typing.Optional[typing.List[str]]

### SecurityGroupArns
- **Type**: typing.Optional[typing.List[str]]


# QopConfigurationTypeDef

### RpcProtection
- **Type**: typing.Optional[typing.Literal['AUTHENTICATION', 'DISABLED', 'INTEGRITY', 'PRIVACY']]

### DataTransferProtection
- **Type**: typing.Optional[typing.Literal['AUTHENTICATION', 'DISABLED', 'INTEGRITY', 'PRIVACY']]


# RecommendationTypeDef

### StorageType
- **Type**: typing.Optional[str]

### StorageConfiguration
- **Type**: typing.Optional[typing.Dict[str, str]]

### EstimatedMonthlyStorageCost
- **Type**: typing.Optional[str]


# RemoveStorageSystemRequestRequestTypeDef

### StorageSystemArn
- **Type**: <class 'str'>
- **Required**: Yes


# ReportDestinationS3TypeDef

### S3BucketArn
- **Type**: <class 'str'>
- **Required**: Yes

### BucketAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]


# ReportDestinationTypeDef

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportDestinationS3TypeDef]


# ReportOverrideTypeDef

### ReportLevel
- **Type**: typing.Optional[typing.Literal['ERRORS_ONLY', 'SUCCESSES_AND_ERRORS']]


# ReportOverridesTypeDef

### Transferred
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportOverrideTypeDef]

### Verified
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportOverrideTypeDef]

### Deleted
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportOverrideTypeDef]

### Skipped
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportOverrideTypeDef]


# ReportResultTypeDef

### Status
- **Type**: typing.Optional[typing.Literal['ERROR', 'PENDING', 'SUCCESS']]

### ErrorCode
- **Type**: typing.Optional[str]

### ErrorDetail
- **Type**: typing.Optional[str]


# ResourceDetailsTypeDef

### NetAppONTAPSVMs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datasync_classes.NetAppONTAPSVMTypeDef]]

### NetAppONTAPVolumes
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datasync_classes.NetAppONTAPVolumeTypeDef]]

### NetAppONTAPClusters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.datasync_classes.NetAppONTAPClusterTypeDef]]


# ResourceMetricsTypeDef

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### P95Metrics
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.P95MetricsTypeDef]

### Capacity
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.CapacityTypeDef]

### ResourceId
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['CLUSTER', 'SVM', 'VOLUME']]


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


# S3ConfigTypeDef

### BucketAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# S3ManifestConfigTypeDef

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


# SmbMountOptionsTypeDef

### Version
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'SMB1', 'SMB2', 'SMB2_0', 'SMB3']]


# SourceManifestConfigTypeDef

### S3
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.S3ManifestConfigTypeDef'>
- **Required**: Yes


# StartDiscoveryJobRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]


# StartDiscoveryJobResponseTypeDef

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartTaskExecutionRequestRequestTypeDef

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### OverrideOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.OptionsTypeDef]

### Includes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.FilterRuleTypeDef]]

### Excludes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.FilterRuleTypeDef]]

### ManifestConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ManifestConfigTypeDef]

### TaskReportConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.TaskReportConfigTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]]


# StartTaskExecutionResponseTypeDef

### TaskExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopDiscoveryJobRequestRequestTypeDef

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes


# StorageSystemListEntryTypeDef

### StorageSystemArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# TagListEntryTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: typing.Optional[str]


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.TagListEntryTypeDef]
- **Required**: Yes


# TaskExecutionListEntryTypeDef

### TaskExecutionArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLING', 'ERROR', 'LAUNCHING', 'PREPARING', 'QUEUED', 'SUCCESS', 'TRANSFERRING', 'VERIFYING']]


# TaskExecutionResultDetailTypeDef

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


# TaskFilterTypeDef

### Name
- **Type**: typing.Literal['CreationTime', 'LocationId']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Operator
- **Type**: typing.Literal['BeginsWith', 'Contains', 'Equals', 'GreaterThan', 'GreaterThanOrEqual', 'In', 'LessThan', 'LessThanOrEqual', 'NotContains', 'NotEquals']
- **Required**: Yes


# TaskListEntryTypeDef

### TaskArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'QUEUED', 'RUNNING', 'UNAVAILABLE']]

### Name
- **Type**: typing.Optional[str]


# TaskReportConfigTypeDef

### Destination
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportDestinationTypeDef]

### OutputType
- **Type**: typing.Optional[typing.Literal['STANDARD', 'SUMMARY_ONLY']]

### ReportLevel
- **Type**: typing.Optional[typing.Literal['ERRORS_ONLY', 'SUCCESSES_AND_ERRORS']]

### ObjectVersionIds
- **Type**: typing.Optional[typing.Literal['INCLUDE', 'NONE']]

### Overrides
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ReportOverridesTypeDef]


# TaskScheduleDetailsTypeDef

### StatusUpdateTime
- **Type**: typing.Optional[datetime.datetime]

### DisabledReason
- **Type**: typing.Optional[str]

### DisabledBy
- **Type**: typing.Optional[typing.Literal['SERVICE', 'USER']]


# TaskScheduleTypeDef

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED']]


# ThroughputTypeDef

### Read
- **Type**: typing.Optional[float]

### Write
- **Type**: typing.Optional[float]

### Other
- **Type**: typing.Optional[float]

### Total
- **Type**: typing.Optional[float]


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Keys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateAgentRequestRequestTypeDef

### AgentArn
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]


# UpdateDiscoveryJobRequestRequestTypeDef

### DiscoveryJobArn
- **Type**: <class 'str'>
- **Required**: Yes

### CollectionDurationMinutes
- **Type**: <class 'int'>
- **Required**: Yes


# UpdateLocationAzureBlobRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['SAS']]

### SasConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.AzureBlobSasConfigurationTypeDef]

### BlobType
- **Type**: typing.Optional[typing.Literal['BLOCK']]

### AccessTier
- **Type**: typing.Optional[typing.Literal['ARCHIVE', 'COOL', 'HOT']]

### AgentArns
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateLocationHdfsRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### NameNodes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.HdfsNameNodeTypeDef]]

### BlockSize
- **Type**: typing.Optional[int]

### ReplicationFactor
- **Type**: typing.Optional[int]

### KmsKeyProviderUri
- **Type**: typing.Optional[str]

### QopConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.QopConfigurationTypeDef]

### AuthenticationType
- **Type**: typing.Optional[typing.Literal['KERBEROS', 'SIMPLE']]

### SimpleUser
- **Type**: typing.Optional[str]

### KerberosPrincipal
- **Type**: typing.Optional[str]

### KerberosKeytab
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### KerberosKrb5Conf
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]

### AgentArns
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateLocationNfsRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
- **Type**: typing.Optional[str]

### OnPremConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.OnPremConfigTypeDef]

### MountOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.NfsMountOptionsTypeDef]


# UpdateLocationObjectStorageRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
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

### AgentArns
- **Type**: typing.Optional[typing.Sequence[str]]

### ServerCertificate
- **Type**: typing.Union[str, bytes, typing.IO[typing.Any], NoneType]


# UpdateLocationSmbRequestRequestTypeDef

### LocationArn
- **Type**: <class 'str'>
- **Required**: Yes

### Subdirectory
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.SmbMountOptionsTypeDef]


# UpdateStorageSystemRequestRequestTypeDef

### StorageSystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### ServerConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.DiscoveryServerConfigurationTypeDef]

### AgentArns
- **Type**: typing.Optional[typing.Sequence[str]]

### Name
- **Type**: typing.Optional[str]

### CloudWatchLogGroupArn
- **Type**: typing.Optional[str]

### Credentials
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.CredentialsTypeDef]


# UpdateTaskExecutionRequestRequestTypeDef

### TaskExecutionArn
- **Type**: <class 'str'>
- **Required**: Yes

### Options
- **Type**: <class 'aws_resource_validator.pydantic_models.datasync_classes.OptionsTypeDef'>
- **Required**: Yes


# UpdateTaskRequestRequestTypeDef

### TaskArn
- **Type**: <class 'str'>
- **Required**: Yes

### Options
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.OptionsTypeDef]

### Excludes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.FilterRuleTypeDef]]

### Schedule
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.TaskScheduleTypeDef]

### Name
- **Type**: typing.Optional[str]

### CloudWatchLogGroupArn
- **Type**: typing.Optional[str]

### Includes
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.datasync_classes.FilterRuleTypeDef]]

### ManifestConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.ManifestConfigTypeDef]

### TaskReportConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.datasync_classes.TaskReportConfigTypeDef]


