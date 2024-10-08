# Pydantic Models in fsx_classes

# ActiveDirectoryBackupAttributesTypeDef

### DomainName
- **Type**: typing.Optional[str]

### ActiveDirectoryId
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]


# AdministrativeActionFailureDetailsTypeDef

### Message
- **Type**: typing.Optional[str]


# AdministrativeActionTypeDef

### AdministrativeActionType
- **Type**: typing.Optional[typing.Literal['DOWNLOAD_DATA_FROM_BACKUP', 'FILE_SYSTEM_ALIAS_ASSOCIATION', 'FILE_SYSTEM_ALIAS_DISASSOCIATION', 'FILE_SYSTEM_UPDATE', 'IOPS_OPTIMIZATION', 'MISCONFIGURED_STATE_RECOVERY', 'RELEASE_NFS_V3_LOCKS', 'SNAPSHOT_UPDATE', 'STORAGE_OPTIMIZATION', 'STORAGE_TYPE_OPTIMIZATION', 'THROUGHPUT_OPTIMIZATION', 'VOLUME_INITIALIZE_WITH_SNAPSHOT', 'VOLUME_RESTORE', 'VOLUME_UPDATE', 'VOLUME_UPDATE_WITH_SNAPSHOT']]

### ProgressPercent
- **Type**: typing.Optional[int]

### RequestTime
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['COMPLETED', 'FAILED', 'IN_PROGRESS', 'OPTIMIZING', 'PENDING', 'UPDATED_OPTIMIZING']]

### TargetFileSystemValues
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.AdministrativeActionFailureDetailsTypeDef]

### TargetVolumeValues
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### TargetSnapshotValues
- **Type**: typing.Optional[typing.Dict[str, typing.Any]]

### TotalTransferBytes
- **Type**: typing.Optional[int]

### RemainingTransferBytes
- **Type**: typing.Optional[int]


# AggregateConfigurationTypeDef

### Aggregates
- **Type**: typing.Optional[typing.List[str]]

### TotalConstituents
- **Type**: typing.Optional[int]


# AliasTypeDef

### Name
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING']]


# AssociateFileSystemAliasesRequestRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Aliases
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# AssociateFileSystemAliasesResponseTypeDef

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx_classes.AliasTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AutoExportPolicyOutputTypeDef

### Events
- **Type**: typing.Optional[typing.List[typing.Literal['CHANGED', 'DELETED', 'NEW']]]


# AutoExportPolicyTypeDef

### Events
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CHANGED', 'DELETED', 'NEW']]]


# AutoImportPolicyOutputTypeDef

### Events
- **Type**: typing.Optional[typing.List[typing.Literal['CHANGED', 'DELETED', 'NEW']]]


# AutoImportPolicyTypeDef

### Events
- **Type**: typing.Optional[typing.Sequence[typing.Literal['CHANGED', 'DELETED', 'NEW']]]


# AutocommitPeriodTypeDef

### Type
- **Type**: typing.Literal['DAYS', 'HOURS', 'MINUTES', 'MONTHS', 'NONE', 'YEARS']
- **Required**: Yes

### Value
- **Type**: typing.Optional[int]


# BackupFailureDetailsTypeDef

### Message
- **Type**: typing.Optional[str]


# BackupTypeDef

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'COPYING', 'CREATING', 'DELETED', 'FAILED', 'PENDING', 'TRANSFERRING']
- **Required**: Yes

### Type
- **Type**: typing.Literal['AUTOMATIC', 'AWS_BACKUP', 'USER_INITIATED']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FileSystem
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.FileSystemTypeDef'>
- **Required**: Yes

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.BackupFailureDetailsTypeDef]

### ProgressPercent
- **Type**: typing.Optional[int]

### KmsKeyId
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### DirectoryInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.ActiveDirectoryBackupAttributesTypeDef]

### OwnerId
- **Type**: typing.Optional[str]

### SourceBackupId
- **Type**: typing.Optional[str]

### SourceBackupRegion
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['FILE_SYSTEM', 'VOLUME']]

### Volume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.VolumeTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelDataRepositoryTaskRequestRequestTypeDef

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelDataRepositoryTaskResponseTypeDef

### Lifecycle
- **Type**: typing.Literal['CANCELED', 'CANCELING', 'EXECUTING', 'FAILED', 'PENDING', 'SUCCEEDED']
- **Required**: Yes

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CompletionReportTypeDef

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Format
- **Type**: typing.Optional[typing.Literal['REPORT_CSV_20191124']]

### Scope
- **Type**: typing.Optional[typing.Literal['FAILED_FILES_ONLY']]


# CopyBackupRequestRequestTypeDef

### SourceBackupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### SourceRegion
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### CopyTags
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]


# CopyBackupResponseTypeDef

### Backup
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.BackupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CopySnapshotAndUpdateVolumeRequestRequestTypeDef

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceSnapshotARN
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### CopyStrategy
- **Type**: typing.Optional[typing.Literal['CLONE', 'FULL_COPY', 'INCREMENTAL_COPY']]

### Options
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DELETE_CLONED_VOLUMES', 'DELETE_INTERMEDIATE_DATA', 'DELETE_INTERMEDIATE_SNAPSHOTS']]]


# CopySnapshotAndUpdateVolumeResponseTypeDef

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'CREATED', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'PENDING']
- **Required**: Yes

### AdministrativeActions
- **Type**: typing.List[ForwardRef('AdministrativeActionTypeDef')]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAggregateConfigurationTypeDef

### Aggregates
- **Type**: typing.Optional[typing.Sequence[str]]

### ConstituentsPerAggregate
- **Type**: typing.Optional[int]


# CreateBackupRequestRequestTypeDef

### FileSystemId
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### VolumeId
- **Type**: typing.Optional[str]


# CreateBackupResponseTypeDef

### Backup
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.BackupTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataRepositoryAssociationRequestRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### DataRepositoryPath
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemPath
- **Type**: typing.Optional[str]

### BatchImportMetaDataOnCreate
- **Type**: typing.Optional[bool]

### ImportedFileChunkSize
- **Type**: typing.Optional[int]

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.S3DataRepositoryConfigurationTypeDef]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]


# CreateDataRepositoryAssociationResponseTypeDef

### Association
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.DataRepositoryAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDataRepositoryTaskRequestRequestTypeDef

### Type
- **Type**: typing.Literal['AUTO_RELEASE_DATA', 'EXPORT_TO_REPOSITORY', 'IMPORT_METADATA_FROM_REPOSITORY', 'RELEASE_DATA_FROM_FILESYSTEM']
- **Required**: Yes

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Report
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.CompletionReportTypeDef'>
- **Required**: Yes

### Paths
- **Type**: typing.Optional[typing.Sequence[str]]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### CapacityToRelease
- **Type**: typing.Optional[int]

### ReleaseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.ReleaseConfigurationTypeDef]


# CreateDataRepositoryTaskResponseTypeDef

### DataRepositoryTask
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.DataRepositoryTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFileCacheLustreConfigurationTypeDef

### PerUnitStorageThroughput
- **Type**: <class 'int'>
- **Required**: Yes

### DeploymentType
- **Type**: typing.Literal['CACHE_1']
- **Required**: Yes

### MetadataConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.FileCacheLustreMetadataConfigurationTypeDef'>
- **Required**: Yes

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]


# CreateFileCacheRequestRequestTypeDef

### FileCacheType
- **Type**: typing.Literal['LUSTRE']
- **Required**: Yes

### FileCacheTypeVersion
- **Type**: <class 'str'>
- **Required**: Yes

### StorageCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### CopyTagsToDataRepositoryAssociations
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateFileCacheLustreConfigurationTypeDef]

### DataRepositoryAssociations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.FileCacheDataRepositoryAssociationTypeDef]]


# CreateFileCacheResponseTypeDef

### FileCache
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.FileCacheCreatingTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFileSystemFromBackupRequestRequestTypeDef

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### WindowsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateFileSystemWindowsConfigurationTypeDef]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateFileSystemLustreConfigurationTypeDef]

### StorageType
- **Type**: typing.Optional[typing.Literal['HDD', 'SSD']]

### KmsKeyId
- **Type**: typing.Optional[str]

### FileSystemTypeVersion
- **Type**: typing.Optional[str]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateFileSystemOpenZFSConfigurationTypeDef]

### StorageCapacity
- **Type**: typing.Optional[int]


# CreateFileSystemFromBackupResponseTypeDef

### FileSystem
- **Type**: ForwardRef('FileSystemTypeDef')
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFileSystemLustreConfigurationTypeDef

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### ImportPath
- **Type**: typing.Optional[str]

### ExportPath
- **Type**: typing.Optional[str]

### ImportedFileChunkSize
- **Type**: typing.Optional[int]

### DeploymentType
- **Type**: typing.Optional[typing.Literal['PERSISTENT_1', 'PERSISTENT_2', 'SCRATCH_1', 'SCRATCH_2']]

### AutoImportPolicy
- **Type**: typing.Optional[typing.Literal['NEW', 'NEW_CHANGED', 'NEW_CHANGED_DELETED', 'NONE']]

### PerUnitStorageThroughput
- **Type**: typing.Optional[int]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### CopyTagsToBackups
- **Type**: typing.Optional[bool]

### DriveCacheType
- **Type**: typing.Optional[typing.Literal['NONE', 'READ']]

### DataCompressionType
- **Type**: typing.Optional[typing.Literal['LZ4', 'NONE']]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.LustreLogCreateConfigurationTypeDef]

### RootSquashConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.LustreRootSquashConfigurationTypeDef]

### MetadataConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateFileSystemLustreMetadataConfigurationTypeDef]


# CreateFileSystemLustreMetadataConfigurationTypeDef

### Mode
- **Type**: typing.Literal['AUTOMATIC', 'USER_PROVISIONED']
- **Required**: Yes

### Iops
- **Type**: typing.Optional[int]


# CreateFileSystemOntapConfigurationTypeDef

### DeploymentType
- **Type**: typing.Literal['MULTI_AZ_1', 'MULTI_AZ_2', 'SINGLE_AZ_1', 'SINGLE_AZ_2']
- **Required**: Yes

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### EndpointIpAddressRange
- **Type**: typing.Optional[str]

### FsxAdminPassword
- **Type**: typing.Optional[str]

### DiskIopsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DiskIopsConfigurationTypeDef]

### PreferredSubnetId
- **Type**: typing.Optional[str]

### RouteTableIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ThroughputCapacity
- **Type**: typing.Optional[int]

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### HAPairs
- **Type**: typing.Optional[int]

### ThroughputCapacityPerHAPair
- **Type**: typing.Optional[int]


# CreateFileSystemOpenZFSConfigurationTypeDef

### DeploymentType
- **Type**: typing.Literal['MULTI_AZ_1', 'SINGLE_AZ_1', 'SINGLE_AZ_2', 'SINGLE_AZ_HA_1', 'SINGLE_AZ_HA_2']
- **Required**: Yes

### ThroughputCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### CopyTagsToBackups
- **Type**: typing.Optional[bool]

### CopyTagsToVolumes
- **Type**: typing.Optional[bool]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### DiskIopsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DiskIopsConfigurationTypeDef]

### RootVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSCreateRootVolumeConfigurationTypeDef]

### PreferredSubnetId
- **Type**: typing.Optional[str]

### EndpointIpAddressRange
- **Type**: typing.Optional[str]

### RouteTableIds
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateFileSystemRequestRequestTypeDef

### FileSystemType
- **Type**: typing.Literal['LUSTRE', 'ONTAP', 'OPENZFS', 'WINDOWS']
- **Required**: Yes

### StorageCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### StorageType
- **Type**: typing.Optional[typing.Literal['HDD', 'SSD']]

### SecurityGroupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### KmsKeyId
- **Type**: typing.Optional[str]

### WindowsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateFileSystemWindowsConfigurationTypeDef]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateFileSystemLustreConfigurationTypeDef]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateFileSystemOntapConfigurationTypeDef]

### FileSystemTypeVersion
- **Type**: typing.Optional[str]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateFileSystemOpenZFSConfigurationTypeDef]


# CreateFileSystemResponseTypeDef

### FileSystem
- **Type**: ForwardRef('FileSystemTypeDef')
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateFileSystemWindowsConfigurationTypeDef

### ThroughputCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### ActiveDirectoryId
- **Type**: typing.Optional[str]

### SelfManagedActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SelfManagedActiveDirectoryConfigurationTypeDef]

### DeploymentType
- **Type**: typing.Optional[typing.Literal['MULTI_AZ_1', 'SINGLE_AZ_1', 'SINGLE_AZ_2']]

### PreferredSubnetId
- **Type**: typing.Optional[str]

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### CopyTagsToBackups
- **Type**: typing.Optional[bool]

### Aliases
- **Type**: typing.Optional[typing.Sequence[str]]

### AuditLogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.WindowsAuditLogCreateConfigurationTypeDef]

### DiskIopsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DiskIopsConfigurationTypeDef]


# CreateOntapVolumeConfigurationTypeDef

### StorageVirtualMachineId
- **Type**: <class 'str'>
- **Required**: Yes

### JunctionPath
- **Type**: typing.Optional[str]

### SecurityStyle
- **Type**: typing.Optional[typing.Literal['MIXED', 'NTFS', 'UNIX']]

### SizeInMegabytes
- **Type**: typing.Optional[int]

### StorageEfficiencyEnabled
- **Type**: typing.Optional[bool]

### TieringPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.TieringPolicyTypeDef]

### OntapVolumeType
- **Type**: typing.Optional[typing.Literal['DP', 'RW']]

### SnapshotPolicy
- **Type**: typing.Optional[str]

### CopyTagsToBackups
- **Type**: typing.Optional[bool]

### SnaplockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateSnaplockConfigurationTypeDef]

### VolumeStyle
- **Type**: typing.Optional[typing.Literal['FLEXGROUP', 'FLEXVOL']]

### AggregateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateAggregateConfigurationTypeDef]

### SizeInBytes
- **Type**: typing.Optional[int]


# CreateOpenZFSOriginSnapshotConfigurationTypeDef

### SnapshotARN
- **Type**: <class 'str'>
- **Required**: Yes

### CopyStrategy
- **Type**: typing.Literal['CLONE', 'FULL_COPY', 'INCREMENTAL_COPY']
- **Required**: Yes


# CreateOpenZFSVolumeConfigurationTypeDef

### ParentVolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### StorageCapacityReservationGiB
- **Type**: typing.Optional[int]

### StorageCapacityQuotaGiB
- **Type**: typing.Optional[int]

### RecordSizeKiB
- **Type**: typing.Optional[int]

### DataCompressionType
- **Type**: typing.Optional[typing.Literal['LZ4', 'NONE', 'ZSTD']]

### CopyTagsToSnapshots
- **Type**: typing.Optional[bool]

### OriginSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateOpenZFSOriginSnapshotConfigurationTypeDef]

### ReadOnly
- **Type**: typing.Optional[bool]

### NfsExports
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSNfsExportTypeDef]]

### UserAndGroupQuotas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSUserOrGroupQuotaTypeDef]]


# CreateSnaplockConfigurationTypeDef

### SnaplockType
- **Type**: typing.Literal['COMPLIANCE', 'ENTERPRISE']
- **Required**: Yes

### AuditLogVolume
- **Type**: typing.Optional[bool]

### AutocommitPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.AutocommitPeriodTypeDef]

### PrivilegedDelete
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'PERMANENTLY_DISABLED']]

### RetentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SnaplockRetentionPeriodTypeDef]

### VolumeAppendModeEnabled
- **Type**: typing.Optional[bool]


# CreateSnapshotRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]


# CreateSnapshotResponseTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStorageVirtualMachineRequestRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateSvmActiveDirectoryConfigurationTypeDef]

### ClientRequestToken
- **Type**: typing.Optional[str]

### SvmAdminPassword
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### RootVolumeSecurityStyle
- **Type**: typing.Optional[typing.Literal['MIXED', 'NTFS', 'UNIX']]


# CreateStorageVirtualMachineResponseTypeDef

### StorageVirtualMachine
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.StorageVirtualMachineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSvmActiveDirectoryConfigurationTypeDef

### NetBiosName
- **Type**: <class 'str'>
- **Required**: Yes

### SelfManagedActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SelfManagedActiveDirectoryConfigurationTypeDef]


# CreateVolumeFromBackupRequestRequestTypeDef

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateOntapVolumeConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]


# CreateVolumeFromBackupResponseTypeDef

### Volume
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.VolumeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVolumeRequestRequestTypeDef

### VolumeType
- **Type**: typing.Literal['ONTAP', 'OPENZFS']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateOntapVolumeConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CreateOpenZFSVolumeConfigurationTypeDef]


# CreateVolumeResponseTypeDef

### Volume
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.VolumeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataRepositoryAssociationTypeDef

### AssociationId
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'UPDATING']]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DataRepositoryFailureDetailsTypeDef]

### FileSystemPath
- **Type**: typing.Optional[str]

### DataRepositoryPath
- **Type**: typing.Optional[str]

### BatchImportMetaDataOnCreate
- **Type**: typing.Optional[bool]

### ImportedFileChunkSize
- **Type**: typing.Optional[int]

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.S3DataRepositoryConfigurationOutputTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FileCacheId
- **Type**: typing.Optional[str]

### FileCachePath
- **Type**: typing.Optional[str]

### DataRepositorySubdirectories
- **Type**: typing.Optional[typing.List[str]]

### NFS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.NFSDataRepositoryConfigurationTypeDef]


# DataRepositoryConfigurationTypeDef

### Lifecycle
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'UPDATING']]

### ImportPath
- **Type**: typing.Optional[str]

### ExportPath
- **Type**: typing.Optional[str]

### ImportedFileChunkSize
- **Type**: typing.Optional[int]

### AutoImportPolicy
- **Type**: typing.Optional[typing.Literal['NEW', 'NEW_CHANGED', 'NEW_CHANGED_DELETED', 'NONE']]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DataRepositoryFailureDetailsTypeDef]


# DataRepositoryFailureDetailsTypeDef

### Message
- **Type**: typing.Optional[str]


# DataRepositoryTaskFailureDetailsTypeDef

### Message
- **Type**: typing.Optional[str]


# DataRepositoryTaskFilterTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['data-repository-association-id', 'file-cache-id', 'file-system-id', 'task-lifecycle']]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# DataRepositoryTaskStatusTypeDef

### TotalCount
- **Type**: typing.Optional[int]

### SucceededCount
- **Type**: typing.Optional[int]

### FailedCount
- **Type**: typing.Optional[int]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### ReleasedCapacity
- **Type**: typing.Optional[int]


# DataRepositoryTaskTypeDef

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['CANCELED', 'CANCELING', 'EXECUTING', 'FAILED', 'PENDING', 'SUCCEEDED']
- **Required**: Yes

### Type
- **Type**: typing.Literal['AUTO_RELEASE_DATA', 'EXPORT_TO_REPOSITORY', 'IMPORT_METADATA_FROM_REPOSITORY', 'RELEASE_DATA_FROM_FILESYSTEM']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### ResourceARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### FileSystemId
- **Type**: typing.Optional[str]

### Paths
- **Type**: typing.Optional[typing.List[str]]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DataRepositoryTaskFailureDetailsTypeDef]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DataRepositoryTaskStatusTypeDef]

### Report
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.CompletionReportTypeDef]

### CapacityToRelease
- **Type**: typing.Optional[int]

### FileCacheId
- **Type**: typing.Optional[str]

### ReleaseConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.ReleaseConfigurationTypeDef]


# DeleteBackupRequestRequestTypeDef

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# DeleteBackupResponseTypeDef

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'COPYING', 'CREATING', 'DELETED', 'FAILED', 'PENDING', 'TRANSFERRING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteDataRepositoryAssociationRequestRequestTypeDef

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### DeleteDataInFileSystem
- **Type**: typing.Optional[bool]


# DeleteDataRepositoryAssociationResponseTypeDef

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'UPDATING']
- **Required**: Yes

### DeleteDataInFileSystem
- **Type**: <class 'bool'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFileCacheRequestRequestTypeDef

### FileCacheId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# DeleteFileCacheResponseTypeDef

### FileCacheId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFileSystemLustreConfigurationTypeDef

### SkipFinalBackup
- **Type**: typing.Optional[bool]

### FinalBackupTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]


# DeleteFileSystemLustreResponseTypeDef

### FinalBackupId
- **Type**: typing.Optional[str]

### FinalBackupTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]


# DeleteFileSystemOpenZFSConfigurationTypeDef

### SkipFinalBackup
- **Type**: typing.Optional[bool]

### FinalBackupTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### Options
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DELETE_CHILD_VOLUMES_AND_SNAPSHOTS']]]


# DeleteFileSystemOpenZFSResponseTypeDef

### FinalBackupId
- **Type**: typing.Optional[str]

### FinalBackupTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]


# DeleteFileSystemRequestRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### WindowsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DeleteFileSystemWindowsConfigurationTypeDef]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DeleteFileSystemLustreConfigurationTypeDef]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DeleteFileSystemOpenZFSConfigurationTypeDef]


# DeleteFileSystemResponseTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'MISCONFIGURED_UNAVAILABLE', 'UPDATING']
- **Required**: Yes

### WindowsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.DeleteFileSystemWindowsResponseTypeDef'>
- **Required**: Yes

### LustreResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.DeleteFileSystemLustreResponseTypeDef'>
- **Required**: Yes

### OpenZFSResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.DeleteFileSystemOpenZFSResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFileSystemWindowsConfigurationTypeDef

### SkipFinalBackup
- **Type**: typing.Optional[bool]

### FinalBackupTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]


# DeleteFileSystemWindowsResponseTypeDef

### FinalBackupId
- **Type**: typing.Optional[str]

### FinalBackupTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]


# DeleteSnapshotRequestRequestTypeDef

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# DeleteSnapshotResponseTypeDef

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteStorageVirtualMachineRequestRequestTypeDef

### StorageVirtualMachineId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# DeleteStorageVirtualMachineResponseTypeDef

### StorageVirtualMachineId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['CREATED', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVolumeOntapConfigurationTypeDef

### SkipFinalBackup
- **Type**: typing.Optional[bool]

### FinalBackupTags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### BypassSnaplockEnterpriseRetention
- **Type**: typing.Optional[bool]


# DeleteVolumeOntapResponseTypeDef

### FinalBackupId
- **Type**: typing.Optional[str]

### FinalBackupTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]


# DeleteVolumeOpenZFSConfigurationTypeDef

### Options
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DELETE_CHILD_VOLUMES_AND_SNAPSHOTS']]]


# DeleteVolumeRequestRequestTypeDef

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DeleteVolumeOntapConfigurationTypeDef]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DeleteVolumeOpenZFSConfigurationTypeDef]


# DeleteVolumeResponseTypeDef

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'CREATED', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'PENDING']
- **Required**: Yes

### OntapResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.DeleteVolumeOntapResponseTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBackupsRequestDescribeBackupsPaginateTypeDef

### BackupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.FilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.PaginatorConfigTypeDef]


# DescribeBackupsRequestRequestTypeDef

### BackupIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBackupsResponseTypeDef

### Backups
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx_classes.BackupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDataRepositoryAssociationsRequestRequestTypeDef

### AssociationIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.FilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDataRepositoryAssociationsResponseTypeDef

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx_classes.DataRepositoryAssociationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDataRepositoryTasksRequestRequestTypeDef

### TaskIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.DataRepositoryTaskFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDataRepositoryTasksResponseTypeDef

### DataRepositoryTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx_classes.DataRepositoryTaskTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFileCachesRequestRequestTypeDef

### FileCacheIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFileCachesResponseTypeDef

### FileCaches
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx_classes.FileCacheTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFileSystemAliasesRequestRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFileSystemAliasesResponseTypeDef

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx_classes.AliasTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFileSystemsRequestDescribeFileSystemsPaginateTypeDef

### FileSystemIds
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.PaginatorConfigTypeDef]


# DescribeFileSystemsRequestRequestTypeDef

### FileSystemIds
- **Type**: typing.Optional[typing.Sequence[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFileSystemsResponseTypeDef

### FileSystems
- **Type**: typing.List[ForwardRef('FileSystemTypeDef')]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSharedVpcConfigurationResponseTypeDef

### EnableFsxRouteTableUpdatesFromParticipantAccounts
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSnapshotsRequestRequestTypeDef

### SnapshotIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.SnapshotFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]


# DescribeSnapshotsResponseTypeDef

### Snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx_classes.SnapshotTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStorageVirtualMachinesRequestDescribeStorageVirtualMachinesPaginateTypeDef

### StorageVirtualMachineIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.StorageVirtualMachineFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.PaginatorConfigTypeDef]


# DescribeStorageVirtualMachinesRequestRequestTypeDef

### StorageVirtualMachineIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.StorageVirtualMachineFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeStorageVirtualMachinesResponseTypeDef

### StorageVirtualMachines
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx_classes.StorageVirtualMachineTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeVolumesRequestDescribeVolumesPaginateTypeDef

### VolumeIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.VolumeFilterTypeDef]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.PaginatorConfigTypeDef]


# DescribeVolumesRequestRequestTypeDef

### VolumeIds
- **Type**: typing.Optional[typing.Sequence[str]]

### Filters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.VolumeFilterTypeDef]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeVolumesResponseTypeDef

### Volumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx_classes.VolumeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateFileSystemAliasesRequestRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Aliases
- **Type**: typing.Sequence[str]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# DisassociateFileSystemAliasesResponseTypeDef

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx_classes.AliasTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DiskIopsConfigurationTypeDef

### Mode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'USER_PROVISIONED']]

### Iops
- **Type**: typing.Optional[int]


# DurationSinceLastAccessTypeDef

### Unit
- **Type**: typing.Optional[typing.Literal['DAYS']]

### Value
- **Type**: typing.Optional[int]


# FileCacheCreatingTypeDef

### OwnerId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FileCacheId
- **Type**: typing.Optional[str]

### FileCacheType
- **Type**: typing.Optional[typing.Literal['LUSTRE']]

### FileCacheTypeVersion
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.FileCacheFailureDetailsTypeDef]

### StorageCapacity
- **Type**: typing.Optional[int]

### VpcId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### NetworkInterfaceIds
- **Type**: typing.Optional[typing.List[str]]

### DNSName
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### CopyTagsToDataRepositoryAssociations
- **Type**: typing.Optional[bool]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.FileCacheLustreConfigurationTypeDef]

### DataRepositoryAssociationIds
- **Type**: typing.Optional[typing.List[str]]


# FileCacheDataRepositoryAssociationTypeDef

### FileCachePath
- **Type**: <class 'str'>
- **Required**: Yes

### DataRepositoryPath
- **Type**: <class 'str'>
- **Required**: Yes

### DataRepositorySubdirectories
- **Type**: typing.Optional[typing.Sequence[str]]

### NFS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.FileCacheNFSConfigurationTypeDef]


# FileCacheFailureDetailsTypeDef

### Message
- **Type**: typing.Optional[str]


# FileCacheLustreConfigurationTypeDef

### PerUnitStorageThroughput
- **Type**: typing.Optional[int]

### DeploymentType
- **Type**: typing.Optional[typing.Literal['CACHE_1']]

### MountName
- **Type**: typing.Optional[str]

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### MetadataConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.FileCacheLustreMetadataConfigurationTypeDef]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.LustreLogConfigurationTypeDef]


# FileCacheLustreMetadataConfigurationTypeDef

### StorageCapacity
- **Type**: <class 'int'>
- **Required**: Yes


# FileCacheNFSConfigurationTypeDef

### Version
- **Type**: typing.Literal['NFS3']
- **Required**: Yes

### DnsIps
- **Type**: typing.Optional[typing.Sequence[str]]


# FileCacheTypeDef

### OwnerId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FileCacheId
- **Type**: typing.Optional[str]

### FileCacheType
- **Type**: typing.Optional[typing.Literal['LUSTRE']]

### FileCacheTypeVersion
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.FileCacheFailureDetailsTypeDef]

### StorageCapacity
- **Type**: typing.Optional[int]

### VpcId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### NetworkInterfaceIds
- **Type**: typing.Optional[typing.List[str]]

### DNSName
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.FileCacheLustreConfigurationTypeDef]

### DataRepositoryAssociationIds
- **Type**: typing.Optional[typing.List[str]]


# FileSystemEndpointTypeDef

### DNSName
- **Type**: typing.Optional[str]

### IpAddresses
- **Type**: typing.Optional[typing.List[str]]


# FileSystemEndpointsTypeDef

### Intercluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.FileSystemEndpointTypeDef]

### Management
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.FileSystemEndpointTypeDef]


# FileSystemFailureDetailsTypeDef

### Message
- **Type**: typing.Optional[str]


# FileSystemLustreMetadataConfigurationTypeDef

### Mode
- **Type**: typing.Literal['AUTOMATIC', 'USER_PROVISIONED']
- **Required**: Yes

### Iops
- **Type**: typing.Optional[int]


# FileSystemTypeDef

### OwnerId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FileSystemId
- **Type**: typing.Optional[str]

### FileSystemType
- **Type**: typing.Optional[typing.Literal['LUSTRE', 'ONTAP', 'OPENZFS', 'WINDOWS']]

### Lifecycle
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'MISCONFIGURED_UNAVAILABLE', 'UPDATING']]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.FileSystemFailureDetailsTypeDef]

### StorageCapacity
- **Type**: typing.Optional[int]

### StorageType
- **Type**: typing.Optional[typing.Literal['HDD', 'SSD']]

### VpcId
- **Type**: typing.Optional[str]

### SubnetIds
- **Type**: typing.Optional[typing.List[str]]

### NetworkInterfaceIds
- **Type**: typing.Optional[typing.List[str]]

### DNSName
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### WindowsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.WindowsFileSystemConfigurationTypeDef]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.LustreFileSystemConfigurationTypeDef]

### AdministrativeActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.AdministrativeActionTypeDef]]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.OntapFileSystemConfigurationTypeDef]

### FileSystemTypeVersion
- **Type**: typing.Optional[str]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSFileSystemConfigurationTypeDef]


# FilterTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['backup-type', 'data-repository-type', 'file-cache-id', 'file-cache-type', 'file-system-id', 'file-system-type', 'volume-id']]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# LifecycleTransitionReasonTypeDef

### Message
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestListTagsForResourcePaginateTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.PaginatorConfigTypeDef]


# ListTagsForResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LustreFileSystemConfigurationTypeDef

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### DataRepositoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DataRepositoryConfigurationTypeDef]

### DeploymentType
- **Type**: typing.Optional[typing.Literal['PERSISTENT_1', 'PERSISTENT_2', 'SCRATCH_1', 'SCRATCH_2']]

### PerUnitStorageThroughput
- **Type**: typing.Optional[int]

### MountName
- **Type**: typing.Optional[str]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### CopyTagsToBackups
- **Type**: typing.Optional[bool]

### DriveCacheType
- **Type**: typing.Optional[typing.Literal['NONE', 'READ']]

### DataCompressionType
- **Type**: typing.Optional[typing.Literal['LZ4', 'NONE']]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.LustreLogConfigurationTypeDef]

### RootSquashConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.LustreRootSquashConfigurationOutputTypeDef]

### MetadataConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.FileSystemLustreMetadataConfigurationTypeDef]


# LustreLogConfigurationTypeDef

### Level
- **Type**: typing.Literal['DISABLED', 'ERROR_ONLY', 'WARN_ERROR', 'WARN_ONLY']
- **Required**: Yes

### Destination
- **Type**: typing.Optional[str]


# LustreLogCreateConfigurationTypeDef

### Level
- **Type**: typing.Literal['DISABLED', 'ERROR_ONLY', 'WARN_ERROR', 'WARN_ONLY']
- **Required**: Yes

### Destination
- **Type**: typing.Optional[str]


# LustreRootSquashConfigurationOutputTypeDef

### RootSquash
- **Type**: typing.Optional[str]

### NoSquashNids
- **Type**: typing.Optional[typing.List[str]]


# LustreRootSquashConfigurationTypeDef

### RootSquash
- **Type**: typing.Optional[str]

### NoSquashNids
- **Type**: typing.Optional[typing.Sequence[str]]


# NFSDataRepositoryConfigurationTypeDef

### Version
- **Type**: typing.Literal['NFS3']
- **Required**: Yes

### DnsIps
- **Type**: typing.Optional[typing.List[str]]

### AutoExportPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.AutoExportPolicyOutputTypeDef]


# OntapFileSystemConfigurationTypeDef

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### DeploymentType
- **Type**: typing.Optional[typing.Literal['MULTI_AZ_1', 'MULTI_AZ_2', 'SINGLE_AZ_1', 'SINGLE_AZ_2']]

### EndpointIpAddressRange
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.FileSystemEndpointsTypeDef]

### DiskIopsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DiskIopsConfigurationTypeDef]

### PreferredSubnetId
- **Type**: typing.Optional[str]

### RouteTableIds
- **Type**: typing.Optional[typing.List[str]]

### ThroughputCapacity
- **Type**: typing.Optional[int]

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### FsxAdminPassword
- **Type**: typing.Optional[str]

### HAPairs
- **Type**: typing.Optional[int]

### ThroughputCapacityPerHAPair
- **Type**: typing.Optional[int]


# OntapVolumeConfigurationTypeDef

### FlexCacheEndpointType
- **Type**: typing.Optional[typing.Literal['CACHE', 'NONE', 'ORIGIN']]

### JunctionPath
- **Type**: typing.Optional[str]

### SecurityStyle
- **Type**: typing.Optional[typing.Literal['MIXED', 'NTFS', 'UNIX']]

### SizeInMegabytes
- **Type**: typing.Optional[int]

### StorageEfficiencyEnabled
- **Type**: typing.Optional[bool]

### StorageVirtualMachineId
- **Type**: typing.Optional[str]

### StorageVirtualMachineRoot
- **Type**: typing.Optional[bool]

### TieringPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.TieringPolicyTypeDef]

### UUID
- **Type**: typing.Optional[str]

### OntapVolumeType
- **Type**: typing.Optional[typing.Literal['DP', 'LS', 'RW']]

### SnapshotPolicy
- **Type**: typing.Optional[str]

### CopyTagsToBackups
- **Type**: typing.Optional[bool]

### SnaplockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SnaplockConfigurationTypeDef]

### VolumeStyle
- **Type**: typing.Optional[typing.Literal['FLEXGROUP', 'FLEXVOL']]

### AggregateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.AggregateConfigurationTypeDef]

### SizeInBytes
- **Type**: typing.Optional[int]


# OpenZFSClientConfigurationOutputTypeDef

### Clients
- **Type**: <class 'str'>
- **Required**: Yes

### Options
- **Type**: typing.List[str]
- **Required**: Yes


# OpenZFSClientConfigurationTypeDef

### Clients
- **Type**: <class 'str'>
- **Required**: Yes

### Options
- **Type**: typing.Sequence[str]
- **Required**: Yes


# OpenZFSCreateRootVolumeConfigurationTypeDef

### RecordSizeKiB
- **Type**: typing.Optional[int]

### DataCompressionType
- **Type**: typing.Optional[typing.Literal['LZ4', 'NONE', 'ZSTD']]

### NfsExports
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSNfsExportTypeDef]]

### UserAndGroupQuotas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSUserOrGroupQuotaTypeDef]]

### CopyTagsToSnapshots
- **Type**: typing.Optional[bool]

### ReadOnly
- **Type**: typing.Optional[bool]


# OpenZFSFileSystemConfigurationTypeDef

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### CopyTagsToBackups
- **Type**: typing.Optional[bool]

### CopyTagsToVolumes
- **Type**: typing.Optional[bool]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### DeploymentType
- **Type**: typing.Optional[typing.Literal['MULTI_AZ_1', 'SINGLE_AZ_1', 'SINGLE_AZ_2', 'SINGLE_AZ_HA_1', 'SINGLE_AZ_HA_2']]

### ThroughputCapacity
- **Type**: typing.Optional[int]

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### DiskIopsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DiskIopsConfigurationTypeDef]

### RootVolumeId
- **Type**: typing.Optional[str]

### PreferredSubnetId
- **Type**: typing.Optional[str]

### EndpointIpAddressRange
- **Type**: typing.Optional[str]

### RouteTableIds
- **Type**: typing.Optional[typing.List[str]]

### EndpointIpAddress
- **Type**: typing.Optional[str]


# OpenZFSNfsExportOutputTypeDef

### ClientConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSClientConfigurationOutputTypeDef]
- **Required**: Yes


# OpenZFSNfsExportTypeDef

### ClientConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSClientConfigurationTypeDef]
- **Required**: Yes


# OpenZFSOriginSnapshotConfigurationTypeDef

### SnapshotARN
- **Type**: typing.Optional[str]

### CopyStrategy
- **Type**: typing.Optional[typing.Literal['CLONE', 'FULL_COPY', 'INCREMENTAL_COPY']]


# OpenZFSUserOrGroupQuotaTypeDef

### Type
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### Id
- **Type**: <class 'int'>
- **Required**: Yes

### StorageCapacityQuotaGiB
- **Type**: <class 'int'>
- **Required**: Yes


# OpenZFSVolumeConfigurationTypeDef

### ParentVolumeId
- **Type**: typing.Optional[str]

### VolumePath
- **Type**: typing.Optional[str]

### StorageCapacityReservationGiB
- **Type**: typing.Optional[int]

### StorageCapacityQuotaGiB
- **Type**: typing.Optional[int]

### RecordSizeKiB
- **Type**: typing.Optional[int]

### DataCompressionType
- **Type**: typing.Optional[typing.Literal['LZ4', 'NONE', 'ZSTD']]

### CopyTagsToSnapshots
- **Type**: typing.Optional[bool]

### OriginSnapshot
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSOriginSnapshotConfigurationTypeDef]

### ReadOnly
- **Type**: typing.Optional[bool]

### NfsExports
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSNfsExportOutputTypeDef]]

### UserAndGroupQuotas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSUserOrGroupQuotaTypeDef]]

### RestoreToSnapshot
- **Type**: typing.Optional[str]

### DeleteIntermediateSnaphots
- **Type**: typing.Optional[bool]

### DeleteClonedVolumes
- **Type**: typing.Optional[bool]

### DeleteIntermediateData
- **Type**: typing.Optional[bool]

### SourceSnapshotARN
- **Type**: typing.Optional[str]

### DestinationSnapshot
- **Type**: typing.Optional[str]

### CopyStrategy
- **Type**: typing.Optional[typing.Literal['CLONE', 'FULL_COPY', 'INCREMENTAL_COPY']]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ReleaseConfigurationTypeDef

### DurationSinceLastAccess
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DurationSinceLastAccessTypeDef]


# ReleaseFileSystemNfsV3LocksRequestRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# ReleaseFileSystemNfsV3LocksResponseTypeDef

### FileSystem
- **Type**: ForwardRef('FileSystemTypeDef')
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
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


# RestoreVolumeFromSnapshotRequestRequestTypeDef

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DELETE_CLONED_VOLUMES', 'DELETE_INTERMEDIATE_SNAPSHOTS']]]


# RestoreVolumeFromSnapshotResponseTypeDef

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'CREATED', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'PENDING']
- **Required**: Yes

### AdministrativeActions
- **Type**: typing.List[ForwardRef('AdministrativeActionTypeDef')]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RetentionPeriodTypeDef

### Type
- **Type**: typing.Literal['DAYS', 'HOURS', 'INFINITE', 'MINUTES', 'MONTHS', 'SECONDS', 'UNSPECIFIED', 'YEARS']
- **Required**: Yes

### Value
- **Type**: typing.Optional[int]


# S3DataRepositoryConfigurationOutputTypeDef

### AutoImportPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.AutoImportPolicyOutputTypeDef]

### AutoExportPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.AutoExportPolicyOutputTypeDef]


# S3DataRepositoryConfigurationTypeDef

### AutoImportPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.AutoImportPolicyTypeDef]

### AutoExportPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.AutoExportPolicyTypeDef]


# SelfManagedActiveDirectoryAttributesTypeDef

### DomainName
- **Type**: typing.Optional[str]

### OrganizationalUnitDistinguishedName
- **Type**: typing.Optional[str]

### FileSystemAdministratorsGroup
- **Type**: typing.Optional[str]

### UserName
- **Type**: typing.Optional[str]

### DnsIps
- **Type**: typing.Optional[typing.List[str]]


# SelfManagedActiveDirectoryConfigurationTypeDef

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### DnsIps
- **Type**: typing.Sequence[str]
- **Required**: Yes

### OrganizationalUnitDistinguishedName
- **Type**: typing.Optional[str]

### FileSystemAdministratorsGroup
- **Type**: typing.Optional[str]


# SelfManagedActiveDirectoryConfigurationUpdatesTypeDef

### UserName
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### DnsIps
- **Type**: typing.Optional[typing.Sequence[str]]

### DomainName
- **Type**: typing.Optional[str]

### OrganizationalUnitDistinguishedName
- **Type**: typing.Optional[str]

### FileSystemAdministratorsGroup
- **Type**: typing.Optional[str]


# SnaplockConfigurationTypeDef

### AuditLogVolume
- **Type**: typing.Optional[bool]

### AutocommitPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.AutocommitPeriodTypeDef]

### PrivilegedDelete
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'PERMANENTLY_DISABLED']]

### RetentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SnaplockRetentionPeriodTypeDef]

### SnaplockType
- **Type**: typing.Optional[typing.Literal['COMPLIANCE', 'ENTERPRISE']]

### VolumeAppendModeEnabled
- **Type**: typing.Optional[bool]


# SnaplockRetentionPeriodTypeDef

### DefaultRetention
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.RetentionPeriodTypeDef'>
- **Required**: Yes

### MinimumRetention
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.RetentionPeriodTypeDef'>
- **Required**: Yes

### MaximumRetention
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.RetentionPeriodTypeDef'>
- **Required**: Yes


# SnapshotFilterTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['file-system-id', 'volume-id']]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# SnapshotTypeDef

### ResourceARN
- **Type**: typing.Optional[str]

### SnapshotId
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### VolumeId
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Lifecycle
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'PENDING']]

### LifecycleTransitionReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.LifecycleTransitionReasonTypeDef]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### AdministrativeActions
- **Type**: typing.Optional[typing.List[ForwardRef('AdministrativeActionTypeDef')]]


# StartMisconfiguredStateRecoveryRequestRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartMisconfiguredStateRecoveryResponseTypeDef

### FileSystem
- **Type**: ForwardRef('FileSystemTypeDef')
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StorageVirtualMachineFilterTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['file-system-id']]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# StorageVirtualMachineTypeDef

### ActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SvmActiveDirectoryConfigurationTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Endpoints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SvmEndpointsTypeDef]

### FileSystemId
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[typing.Literal['CREATED', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'PENDING']]

### Name
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]

### StorageVirtualMachineId
- **Type**: typing.Optional[str]

### Subtype
- **Type**: typing.Optional[typing.Literal['DEFAULT', 'DP_DESTINATION', 'SYNC_DESTINATION', 'SYNC_SOURCE']]

### UUID
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### LifecycleTransitionReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.LifecycleTransitionReasonTypeDef]

### RootVolumeSecurityStyle
- **Type**: typing.Optional[typing.Literal['MIXED', 'NTFS', 'UNIX']]


# SvmActiveDirectoryConfigurationTypeDef

### NetBiosName
- **Type**: typing.Optional[str]

### SelfManagedActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SelfManagedActiveDirectoryAttributesTypeDef]


# SvmEndpointTypeDef

### DNSName
- **Type**: typing.Optional[str]

### IpAddresses
- **Type**: typing.Optional[typing.List[str]]


# SvmEndpointsTypeDef

### Iscsi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SvmEndpointTypeDef]

### Management
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SvmEndpointTypeDef]

### Nfs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SvmEndpointTypeDef]

### Smb
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SvmEndpointTypeDef]


# TagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TieringPolicyTypeDef

### CoolingPeriod
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[typing.Literal['ALL', 'AUTO', 'NONE', 'SNAPSHOT_ONLY']]


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateDataRepositoryAssociationRequestRequestTypeDef

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### ImportedFileChunkSize
- **Type**: typing.Optional[int]

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.S3DataRepositoryConfigurationTypeDef]


# UpdateDataRepositoryAssociationResponseTypeDef

### Association
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.DataRepositoryAssociationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFileCacheLustreConfigurationTypeDef

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]


# UpdateFileCacheRequestRequestTypeDef

### FileCacheId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.UpdateFileCacheLustreConfigurationTypeDef]


# UpdateFileCacheResponseTypeDef

### FileCache
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.FileCacheTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFileSystemLustreConfigurationTypeDef

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### AutoImportPolicy
- **Type**: typing.Optional[typing.Literal['NEW', 'NEW_CHANGED', 'NEW_CHANGED_DELETED', 'NONE']]

### DataCompressionType
- **Type**: typing.Optional[typing.Literal['LZ4', 'NONE']]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.LustreLogCreateConfigurationTypeDef]

### RootSquashConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.LustreRootSquashConfigurationTypeDef]

### PerUnitStorageThroughput
- **Type**: typing.Optional[int]

### MetadataConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.UpdateFileSystemLustreMetadataConfigurationTypeDef]


# UpdateFileSystemLustreMetadataConfigurationTypeDef

### Iops
- **Type**: typing.Optional[int]

### Mode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'USER_PROVISIONED']]


# UpdateFileSystemOntapConfigurationTypeDef

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### FsxAdminPassword
- **Type**: typing.Optional[str]

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### DiskIopsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DiskIopsConfigurationTypeDef]

### ThroughputCapacity
- **Type**: typing.Optional[int]

### AddRouteTableIds
- **Type**: typing.Optional[typing.Sequence[str]]

### RemoveRouteTableIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ThroughputCapacityPerHAPair
- **Type**: typing.Optional[int]

### HAPairs
- **Type**: typing.Optional[int]


# UpdateFileSystemOpenZFSConfigurationTypeDef

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### CopyTagsToBackups
- **Type**: typing.Optional[bool]

### CopyTagsToVolumes
- **Type**: typing.Optional[bool]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### ThroughputCapacity
- **Type**: typing.Optional[int]

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### DiskIopsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DiskIopsConfigurationTypeDef]

### AddRouteTableIds
- **Type**: typing.Optional[typing.Sequence[str]]

### RemoveRouteTableIds
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateFileSystemRequestRequestTypeDef

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### StorageCapacity
- **Type**: typing.Optional[int]

### WindowsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.UpdateFileSystemWindowsConfigurationTypeDef]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.UpdateFileSystemLustreConfigurationTypeDef]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.UpdateFileSystemOntapConfigurationTypeDef]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.UpdateFileSystemOpenZFSConfigurationTypeDef]

### StorageType
- **Type**: typing.Optional[typing.Literal['HDD', 'SSD']]


# UpdateFileSystemResponseTypeDef

### FileSystem
- **Type**: ForwardRef('FileSystemTypeDef')
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFileSystemWindowsConfigurationTypeDef

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### ThroughputCapacity
- **Type**: typing.Optional[int]

### SelfManagedActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SelfManagedActiveDirectoryConfigurationUpdatesTypeDef]

### AuditLogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.WindowsAuditLogCreateConfigurationTypeDef]

### DiskIopsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DiskIopsConfigurationTypeDef]


# UpdateOntapVolumeConfigurationTypeDef

### JunctionPath
- **Type**: typing.Optional[str]

### SecurityStyle
- **Type**: typing.Optional[typing.Literal['MIXED', 'NTFS', 'UNIX']]

### SizeInMegabytes
- **Type**: typing.Optional[int]

### StorageEfficiencyEnabled
- **Type**: typing.Optional[bool]

### TieringPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.TieringPolicyTypeDef]

### SnapshotPolicy
- **Type**: typing.Optional[str]

### CopyTagsToBackups
- **Type**: typing.Optional[bool]

### SnaplockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.UpdateSnaplockConfigurationTypeDef]

### SizeInBytes
- **Type**: typing.Optional[int]


# UpdateOpenZFSVolumeConfigurationTypeDef

### StorageCapacityReservationGiB
- **Type**: typing.Optional[int]

### StorageCapacityQuotaGiB
- **Type**: typing.Optional[int]

### RecordSizeKiB
- **Type**: typing.Optional[int]

### DataCompressionType
- **Type**: typing.Optional[typing.Literal['LZ4', 'NONE', 'ZSTD']]

### NfsExports
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSNfsExportTypeDef]]

### UserAndGroupQuotas
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSUserOrGroupQuotaTypeDef]]

### ReadOnly
- **Type**: typing.Optional[bool]


# UpdateSharedVpcConfigurationRequestRequestTypeDef

### EnableFsxRouteTableUpdatesFromParticipantAccounts
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]


# UpdateSharedVpcConfigurationResponseTypeDef

### EnableFsxRouteTableUpdatesFromParticipantAccounts
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSnaplockConfigurationTypeDef

### AuditLogVolume
- **Type**: typing.Optional[bool]

### AutocommitPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.AutocommitPeriodTypeDef]

### PrivilegedDelete
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'PERMANENTLY_DISABLED']]

### RetentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SnaplockRetentionPeriodTypeDef]

### VolumeAppendModeEnabled
- **Type**: typing.Optional[bool]


# UpdateSnapshotRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# UpdateSnapshotResponseTypeDef

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.SnapshotTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStorageVirtualMachineRequestRequestTypeDef

### StorageVirtualMachineId
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.UpdateSvmActiveDirectoryConfigurationTypeDef]

### ClientRequestToken
- **Type**: typing.Optional[str]

### SvmAdminPassword
- **Type**: typing.Optional[str]


# UpdateStorageVirtualMachineResponseTypeDef

### StorageVirtualMachine
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.StorageVirtualMachineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSvmActiveDirectoryConfigurationTypeDef

### SelfManagedActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SelfManagedActiveDirectoryConfigurationUpdatesTypeDef]

### NetBiosName
- **Type**: typing.Optional[str]


# UpdateVolumeRequestRequestTypeDef

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.UpdateOntapVolumeConfigurationTypeDef]

### Name
- **Type**: typing.Optional[str]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.UpdateOpenZFSVolumeConfigurationTypeDef]


# UpdateVolumeResponseTypeDef

### Volume
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.VolumeTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VolumeFilterTypeDef

### Name
- **Type**: typing.Optional[typing.Literal['file-system-id', 'storage-virtual-machine-id']]

### Values
- **Type**: typing.Optional[typing.Sequence[str]]


# VolumeTypeDef

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FileSystemId
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATED', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'PENDING']]

### Name
- **Type**: typing.Optional[str]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.OntapVolumeConfigurationTypeDef]

### ResourceARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.TagTypeDef]]

### VolumeId
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[typing.Literal['ONTAP', 'OPENZFS']]

### LifecycleTransitionReason
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.LifecycleTransitionReasonTypeDef]

### AdministrativeActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.AdministrativeActionTypeDef]]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.OpenZFSVolumeConfigurationTypeDef]


# WindowsAuditLogConfigurationTypeDef

### FileAccessAuditLogLevel
- **Type**: typing.Literal['DISABLED', 'FAILURE_ONLY', 'SUCCESS_AND_FAILURE', 'SUCCESS_ONLY']
- **Required**: Yes

### FileShareAccessAuditLogLevel
- **Type**: typing.Literal['DISABLED', 'FAILURE_ONLY', 'SUCCESS_AND_FAILURE', 'SUCCESS_ONLY']
- **Required**: Yes

### AuditLogDestination
- **Type**: typing.Optional[str]


# WindowsAuditLogCreateConfigurationTypeDef

### FileAccessAuditLogLevel
- **Type**: typing.Literal['DISABLED', 'FAILURE_ONLY', 'SUCCESS_AND_FAILURE', 'SUCCESS_ONLY']
- **Required**: Yes

### FileShareAccessAuditLogLevel
- **Type**: typing.Literal['DISABLED', 'FAILURE_ONLY', 'SUCCESS_AND_FAILURE', 'SUCCESS_ONLY']
- **Required**: Yes

### AuditLogDestination
- **Type**: typing.Optional[str]


# WindowsFileSystemConfigurationTypeDef

### ActiveDirectoryId
- **Type**: typing.Optional[str]

### SelfManagedActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.SelfManagedActiveDirectoryAttributesTypeDef]

### DeploymentType
- **Type**: typing.Optional[typing.Literal['MULTI_AZ_1', 'SINGLE_AZ_1', 'SINGLE_AZ_2']]

### RemoteAdministrationEndpoint
- **Type**: typing.Optional[str]

### PreferredSubnetId
- **Type**: typing.Optional[str]

### PreferredFileServerIp
- **Type**: typing.Optional[str]

### ThroughputCapacity
- **Type**: typing.Optional[int]

### MaintenanceOperationsInProgress
- **Type**: typing.Optional[typing.List[typing.Literal['BACKING_UP', 'PATCHING']]]

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### CopyTagsToBackups
- **Type**: typing.Optional[bool]

### Aliases
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx_classes.AliasTypeDef]]

### AuditLogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.WindowsAuditLogConfigurationTypeDef]

### DiskIopsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx_classes.DiskIopsConfigurationTypeDef]

