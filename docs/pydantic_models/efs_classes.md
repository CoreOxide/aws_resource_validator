# Efs Classes

# AccessPointDescription

### ClientToken
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.Tag]]

### AccessPointId
- **Type**: typing.Optional[str]

### AccessPointArn
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### PosixUser
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs.efs_classes.PosixUserOutput]

### RootDirectory
- **Type**: <class 'NoneType'>

### OwnerId
- **Type**: typing.Optional[str]

### LifeCycleState
- **Type**: typing.Optional[typing.Literal['available', 'creating', 'deleted', 'deleting', 'error', 'updating']]


# AccessPointDescriptionResponse

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.Tag]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.PosixUserOutput'>
- **Required**: Yes

### RootDirectory
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.RootDirectory'>
- **Required**: Yes

### OwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### LifeCycleState
- **Type**: typing.Literal['available', 'creating', 'deleted', 'deleting', 'error', 'updating']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# BackupPolicy

### Status
- **Type**: typing.Literal['DISABLED', 'DISABLING', 'ENABLED', 'ENABLING']
- **Required**: Yes


# BackupPolicyDescription

### BackupPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.BackupPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateAccessPointRequest

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.Tag]]

### PosixUser
- **Type**: typing.Union[aws_resource_validator.pydantic_models.efs.efs_classes.PosixUser, aws_resource_validator.pydantic_models.efs.efs_classes.PosixUserOutput, NoneType]

### RootDirectory
- **Type**: <class 'NoneType'>


# CreateFileSystemRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.Tag]]


# CreateMountTargetRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetId
- **Type**: <class 'str'>
- **Required**: Yes

### IpAddress
- **Type**: typing.Optional[str]

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]


# CreateReplicationConfigurationRequest

### SourceFileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.DestinationToCreate]
- **Required**: Yes


# CreateTagsRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.Tag]
- **Required**: Yes


# CreationInfo

### OwnerUid
- **Type**: <class 'int'>
- **Required**: Yes

### OwnerGid
- **Type**: <class 'int'>
- **Required**: Yes

### Permissions
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAccessPointRequest

### AccessPointId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFileSystemPolicyRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteFileSystemRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMountTargetRequest

### MountTargetId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteReplicationConfigurationRequest

### SourceFileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### DeletionMode
- **Type**: typing.Optional[typing.Literal['ALL_CONFIGURATIONS', 'LOCAL_CONFIGURATION_ONLY']]


# DeleteTagsRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeAccessPointsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### AccessPointId
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]


# DescribeAccessPointsRequestPaginate

### AccessPointId
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs.efs_classes.PaginatorConfig]


# DescribeAccessPointsResponse

### AccessPoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.AccessPointDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeAccountPreferencesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeAccountPreferencesResponse

### ResourceIdPreference
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResourceIdPreference'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBackupPolicyRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFileSystemPolicyRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeFileSystemsRequest

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]

### CreationToken
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]


# DescribeFileSystemsRequestPaginate

### CreationToken
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs.efs_classes.PaginatorConfig]


# DescribeFileSystemsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystems
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.FileSystemDescription]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLifecycleConfigurationRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMountTargetSecurityGroupsRequest

### MountTargetId
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMountTargetSecurityGroupsResponse

### SecurityGroups
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMountTargetsRequest

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


# DescribeMountTargetsRequestPaginate

### FileSystemId
- **Type**: typing.Optional[str]

### MountTargetId
- **Type**: typing.Optional[str]

### AccessPointId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs.efs_classes.PaginatorConfig]


# DescribeMountTargetsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### MountTargets
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.MountTargetDescription]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeReplicationConfigurationsRequest

### FileSystemId
- **Type**: typing.Optional[str]

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# DescribeReplicationConfigurationsRequestPaginate

### FileSystemId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs.efs_classes.PaginatorConfig]


# DescribeReplicationConfigurationsResponse

### Replications
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.ReplicationConfigurationDescription]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeTagsRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxItems
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# DescribeTagsRequestPaginate

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs.efs_classes.PaginatorConfig]


# DescribeTagsResponse

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.Tag]
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# Destination

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


# DestinationToCreate

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


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# FileSystemDescription

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
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.FileSystemSize'>
- **Required**: Yes

### PerformanceMode
- **Type**: typing.Literal['generalPurpose', 'maxIO']
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.Tag]
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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.efs.efs_classes.FileSystemProtectionDescription]


# FileSystemDescriptionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.FileSystemSize'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.Tag]
- **Required**: Yes

### FileSystemProtection
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.FileSystemProtectionDescription'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# FileSystemPolicyDescription

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# FileSystemProtectionDescription

### ReplicationOverwriteProtection
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'REPLICATING']]


# FileSystemProtectionDescriptionResponse

### ReplicationOverwriteProtection
- **Type**: typing.Literal['DISABLED', 'ENABLED', 'REPLICATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# FileSystemSize

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


# LifecycleConfigurationDescription

### LifecyclePolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.LifecyclePolicy]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# LifecyclePolicy

### TransitionToIA
- **Type**: typing.Optional[typing.Literal['AFTER_14_DAYS', 'AFTER_180_DAYS', 'AFTER_1_DAY', 'AFTER_270_DAYS', 'AFTER_30_DAYS', 'AFTER_365_DAYS', 'AFTER_60_DAYS', 'AFTER_7_DAYS', 'AFTER_90_DAYS']]

### TransitionToPrimaryStorageClass
- **Type**: typing.Optional[typing.Literal['AFTER_1_ACCESS']]

### TransitionToArchive
- **Type**: typing.Optional[typing.Literal['AFTER_14_DAYS', 'AFTER_180_DAYS', 'AFTER_1_DAY', 'AFTER_270_DAYS', 'AFTER_30_DAYS', 'AFTER_365_DAYS', 'AFTER_60_DAYS', 'AFTER_7_DAYS', 'AFTER_90_DAYS']]


# ListTagsForResourceRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ModifyMountTargetSecurityGroupsRequest

### MountTargetId
- **Type**: <class 'str'>
- **Required**: Yes

### SecurityGroups
- **Type**: typing.Optional[typing.List[str]]


# MountTargetDescription

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


# MountTargetDescriptionResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PosixUser

### Uid
- **Type**: <class 'int'>
- **Required**: Yes

### Gid
- **Type**: <class 'int'>
- **Required**: Yes

### SecondaryGids
- **Type**: typing.Optional[typing.List[int]]


# PosixUserOutput

### Uid
- **Type**: <class 'int'>
- **Required**: Yes

### Gid
- **Type**: <class 'int'>
- **Required**: Yes

### SecondaryGids
- **Type**: typing.Optional[typing.List[int]]


# PutAccountPreferencesRequest

### ResourceIdType
- **Type**: typing.Literal['LONG_ID', 'SHORT_ID']
- **Required**: Yes


# PutAccountPreferencesResponse

### ResourceIdPreference
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResourceIdPreference'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# PutBackupPolicyRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### BackupPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.BackupPolicy'>
- **Required**: Yes


# PutFileSystemPolicyRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### BypassPolicyLockoutSafetyCheck
- **Type**: typing.Optional[bool]


# PutLifecycleConfigurationRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### LifecyclePolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.LifecyclePolicy]
- **Required**: Yes


# ReplicationConfigurationDescription

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.Destination]
- **Required**: Yes

### SourceFileSystemOwnerId
- **Type**: typing.Optional[str]


# ReplicationConfigurationDescriptionResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.Destination]
- **Required**: Yes

### SourceFileSystemOwnerId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.efs.efs_classes.ResponseMetadata'>
- **Required**: Yes


# ResourceIdPreference

### ResourceIdType
- **Type**: typing.Optional[typing.Literal['LONG_ID', 'SHORT_ID']]

### Resources
- **Type**: typing.Optional[typing.List[typing.Literal['FILE_SYSTEM', 'MOUNT_TARGET']]]


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


# RootDirectory

### Path
- **Type**: typing.Optional[str]

### CreationInfo
- **Type**: <class 'NoneType'>


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.efs.efs_classes.Tag]
- **Required**: Yes


# UntagResourceRequest

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateFileSystemProtectionRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ReplicationOverwriteProtection
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'REPLICATING']]


# UpdateFileSystemRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ThroughputMode
- **Type**: typing.Optional[typing.Literal['bursting', 'elastic', 'provisioned']]

### ProvisionedThroughputInMibps
- **Type**: typing.Optional[float]


