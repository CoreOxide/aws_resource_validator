# Efs Classes

# AccessPointDescriptionResponseTypeDef

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs_classes.TagTypeDef]
- **Required**: Yes

### AccessPointId
- **Type**: <class 'str'>
- **Required**: Yes

### AccessPointArn
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### PosixUser
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.PosixUserOutputTypeDef'>
- **Required**: Yes

### RootDirectory
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.RootDirectoryTypeDef'>
- **Required**: Yes

### OwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### LifeCycleState
- **Type**: typing.Literal['available', 'creating', 'deleted', 'deleting', 'error', 'updating']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AccessPointDescriptionTypeDef

### ClientToken
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.efs_classes.TagTypeDef]]

### AccessPointId
- **Type**: typing.Optional[str]

### AccessPointArn
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### PosixUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs_classes.PosixUserOutputTypeDef]

### RootDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs_classes.RootDirectoryTypeDef]

### OwnerId
- **Type**: typing.Optional[str]

### LifeCycleState
- **Type**: typing.Optional[typing.Literal['available', 'creating', 'deleted', 'deleting', 'error', 'updating']]


# BackupPolicyDescriptionTypeDef

### BackupPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.BackupPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BackupPolicyTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING']
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccessPointRequestTypeDef

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.efs_classes.TagTypeDef]]

### PosixUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs_classes.PosixUserUnionTypeDef]

### RootDirectory
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs_classes.RootDirectoryTypeDef]


# CreateFileSystemRequestTypeDef

### CreationToken
- **Type**: <class 'str'>
- **Required**: Yes

### PerformanceMode
- **Type**: typing.Optional[typing.Literal['generalPurpose', 'maxIO']]

### Encrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### ThroughputMode
- **Type**: typing.Optional[typing.Literal['bursting', 'elastic', 'provisioned']]

### ProvisionedThroughputInMibps
- **Type**: typing.Optional[float]

### AvailabilityZoneName
- **Type**: typing.Optional[str]

### Backup
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.efs_classes.TagTypeDef]]


# CreateMountTargetRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### IpAddress
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateReplicationConfigurationRequestTypeDef

### SourceFileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.efs_classes.DestinationToCreateTypeDef]
- **Required**: Yes


# CreateTagsRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.efs_classes.TagTypeDef]
- **Required**: Yes


# CreationInfoTypeDef

### OwnerUid
- **Type**: <class 'int'>
- **Required**: Yes

### OwnerGid
- **Type**: <class 'int'>
- **Required**: Yes

### Permissions
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessPointRequestTypeDef

### AccessPointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFileSystemPolicyRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFileSystemRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMountTargetRequestTypeDef

### MountTargetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationConfigurationRequestTypeDef

### SourceFileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionMode
- **Type**: typing.Optional[typing.Literal['ALL_CONFIGURATIONS', 'LOCAL_CONFIGURATION_ONLY']]


# DeleteTagsRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeAccessPointsRequestPaginateTypeDef

### AccessPointId
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs_classes.PaginatorConfigTypeDef]


# DescribeAccessPointsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccessPointId
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]


# DescribeAccessPointsResponseTypeDef

### AccessPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs_classes.AccessPointDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAccountPreferencesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeAccountPreferencesResponseTypeDef

### ResourceIdPreference
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResourceIdPreferenceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBackupPolicyRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFileSystemPolicyRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFileSystemsRequestPaginateTypeDef

### CreationToken
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs_classes.PaginatorConfigTypeDef]


# DescribeFileSystemsRequestTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### CreationToken
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]


# DescribeFileSystemsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystems
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs_classes.FileSystemDescriptionTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLifecycleConfigurationRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMountTargetSecurityGroupsRequestTypeDef

### MountTargetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMountTargetSecurityGroupsResponseTypeDef

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMountTargetsRequestPaginateTypeDef

### FileSystemId
- **Type**: typing.Optional[str]

### MountTargetId
- **Type**: typing.Optional[str]

### AccessPointId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs_classes.PaginatorConfigTypeDef]


# DescribeMountTargetsRequestTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### MountTargetId
- **Type**: typing.Optional[str]

### AccessPointId
- **Type**: typing.Optional[str]


# DescribeMountTargetsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### MountTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs_classes.MountTargetDescriptionTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeReplicationConfigurationsRequestPaginateTypeDef

### FileSystemId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs_classes.PaginatorConfigTypeDef]


# DescribeReplicationConfigurationsRequestTypeDef

### FileSystemId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeReplicationConfigurationsResponseTypeDef

### Replications
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs_classes.ReplicationConfigurationDescriptionTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeTagsRequestPaginateTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs_classes.PaginatorConfigTypeDef]


# DescribeTagsRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeTagsResponseTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs_classes.TagTypeDef]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DestinationToCreateTypeDef

### Region
- **Type**: typing.Optional[str]

### AvailabilityZoneName
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# DestinationTypeDef

### Status
- **Type**: typing.Literal['DELETING', 'ENABLED', 'ENABLING', 'ERROR', 'PAUSED', 'PAUSING']
- **Required**: Yes

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### LastReplicatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### OwnerId
- **Type**: typing.Optional[str]

### StatusMessage
- **Type**: typing.Optional[str]

### RoleArn
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FileSystemDescriptionResponseTypeDef

### OwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationToken
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LifeCycleState
- **Type**: typing.Literal['available', 'creating', 'deleted', 'deleting', 'error', 'updating']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### NumberOfMountTargets
- **Type**: <class 'int'>
- **Required**: Yes

### SizeInBytes
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.FileSystemSizeTypeDef'>
- **Required**: Yes

### PerformanceMode
- **Type**: typing.Literal['generalPurpose', 'maxIO']
- **Required**: Yes

### Encrypted
- **Type**: <class 'bool'>
- **Required**: Yes

### KmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### ThroughputMode
- **Type**: typing.Literal['bursting', 'elastic', 'provisioned']
- **Required**: Yes

### ProvisionedThroughputInMibps
- **Type**: <class 'float'>
- **Required**: Yes

### AvailabilityZoneName
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs_classes.TagTypeDef]
- **Required**: Yes

### FileSystemProtection
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.FileSystemProtectionDescriptionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FileSystemDescriptionTypeDef

### OwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationToken
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LifeCycleState
- **Type**: typing.Literal['available', 'creating', 'deleted', 'deleting', 'error', 'updating']
- **Required**: Yes

### NumberOfMountTargets
- **Type**: <class 'int'>
- **Required**: Yes

### SizeInBytes
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.FileSystemSizeTypeDef'>
- **Required**: Yes

### PerformanceMode
- **Type**: typing.Literal['generalPurpose', 'maxIO']
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs_classes.TagTypeDef]
- **Required**: Yes

### FileSystemArn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Encrypted
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### ThroughputMode
- **Type**: typing.Optional[typing.Literal['bursting', 'elastic', 'provisioned']]

### ProvisionedThroughputInMibps
- **Type**: typing.Optional[float]

### AvailabilityZoneName
- **Type**: typing.Optional[str]

### AvailabilityZoneId
- **Type**: typing.Optional[str]

### FileSystemProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs_classes.FileSystemProtectionDescriptionTypeDef]


# FileSystemPolicyDescriptionTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FileSystemProtectionDescriptionResponseTypeDef

### ReplicationOverwriteProtection
- **Type**: typing.Literal['DISABLED', 'ENABLED', 'REPLICATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FileSystemProtectionDescriptionTypeDef

### ReplicationOverwriteProtection
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'REPLICATING']]


# FileSystemSizeTypeDef

### Value
- **Type**: <class 'int'>
- **Required**: Yes

### Timestamp
- **Type**: typing.Optional[datetime.datetime]

### ValueInIA
- **Type**: typing.Optional[int]

### ValueInStandard
- **Type**: typing.Optional[int]

### ValueInArchive
- **Type**: typing.Optional[int]


# LifecycleConfigurationDescriptionTypeDef

### LifecyclePolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs_classes.LifecyclePolicyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LifecyclePolicyTypeDef

### TransitionToIA
- **Type**: typing.Optional[typing.Literal['AFTER_14_DAYS', 'AFTER_180_DAYS', 'AFTER_1_DAY', 'AFTER_270_DAYS', 'AFTER_30_DAYS', 'AFTER_365_DAYS', 'AFTER_60_DAYS', 'AFTER_7_DAYS', 'AFTER_90_DAYS']]

### TransitionToPrimaryStorageClass
- **Type**: typing.Optional[typing.Literal['AFTER_1_ACCESS']]

### TransitionToArchive
- **Type**: typing.Optional[typing.Literal['AFTER_14_DAYS', 'AFTER_180_DAYS', 'AFTER_1_DAY', 'AFTER_270_DAYS', 'AFTER_30_DAYS', 'AFTER_365_DAYS', 'AFTER_60_DAYS', 'AFTER_7_DAYS', 'AFTER_90_DAYS']]


# ListTagsForResourceRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ModifyMountTargetSecurityGroupsRequestTypeDef

### MountTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Optional[typing.Sequence[str]]


# MountTargetDescriptionResponseTypeDef

### OwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### MountTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### LifeCycleState
- **Type**: typing.Literal['available', 'creating', 'deleted', 'deleting', 'error', 'updating']
- **Required**: Yes

### IpAddress
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZoneId
- **Type**: <class 'str'>
- **Required**: Yes

### AvailabilityZoneName
- **Type**: <class 'str'>
- **Required**: Yes

### VpcId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MountTargetDescriptionTypeDef

### MountTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### LifeCycleState
- **Type**: typing.Literal['available', 'creating', 'deleted', 'deleting', 'error', 'updating']
- **Required**: Yes

### OwnerId
- **Type**: typing.Optional[str]

### IpAddress
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### AvailabilityZoneId
- **Type**: typing.Optional[str]

### AvailabilityZoneName
- **Type**: typing.Optional[str]

### VpcId
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PosixUserOutputTypeDef

### Uid
- **Type**: <class 'int'>
- **Required**: Yes

### Gid
- **Type**: <class 'int'>
- **Required**: Yes

### SecondaryGids
- **Type**: typing.Optional[typing.List[int]]


# PosixUserTypeDef

### Uid
- **Type**: <class 'int'>
- **Required**: Yes

### Gid
- **Type**: <class 'int'>
- **Required**: Yes

### SecondaryGids
- **Type**: typing.Optional[typing.Sequence[int]]


# PosixUserUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PutAccountPreferencesRequestTypeDef

### ResourceIdType
- **Type**: typing.Literal['LONG_ID', 'SHORT_ID']
- **Required**: Yes


# PutAccountPreferencesResponseTypeDef

### ResourceIdPreference
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResourceIdPreferenceTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PutBackupPolicyRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.BackupPolicyTypeDef'>
- **Required**: Yes


# PutFileSystemPolicyRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### BypassPolicyLockoutSafetyCheck
- **Type**: typing.Optional[bool]


# PutLifecycleConfigurationRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### LifecyclePolicies
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.efs_classes.LifecyclePolicyTypeDef]
- **Required**: Yes


# ReplicationConfigurationDescriptionResponseTypeDef

### SourceFileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFileSystemRegion
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFileSystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### OriginalSourceFileSystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs_classes.DestinationTypeDef]
- **Required**: Yes

### SourceFileSystemOwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReplicationConfigurationDescriptionTypeDef

### SourceFileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFileSystemRegion
- **Type**: <class 'str'>
- **Required**: Yes

### SourceFileSystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### OriginalSourceFileSystemArn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs_classes.DestinationTypeDef]
- **Required**: Yes

### SourceFileSystemOwnerId
- **Type**: typing.Optional[str]


# ResourceIdPreferenceTypeDef

### ResourceIdType
- **Type**: typing.Optional[typing.Literal['LONG_ID', 'SHORT_ID']]

### Resources
- **Type**: typing.Optional[typing.List[typing.Literal['FILE_SYSTEM', 'MOUNT_TARGET']]]


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


# RootDirectoryTypeDef

### Path
- **Type**: typing.Optional[str]

### CreationInfo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs_classes.CreationInfoTypeDef]


# TagResourceRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.efs_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateFileSystemProtectionRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationOverwriteProtection
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'REPLICATING']]


# UpdateFileSystemRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ThroughputMode
- **Type**: typing.Optional[typing.Literal['bursting', 'elastic', 'provisioned']]

### ProvisionedThroughputInMibps
- **Type**: typing.Optional[float]


