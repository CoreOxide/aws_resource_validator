# Fsx Classes

# ActiveDirectoryBackupAttributes

### DomainName
- **Type**: typing.Optional[str]

### ActiveDirectoryId
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]


# AdministrativeAction

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.AdministrativeActionFailureDetails]

### TargetVolumeValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.Volume]

### TargetSnapshotValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.Snapshot]

### TotalTransferBytes
- **Type**: typing.Optional[int]

### RemainingTransferBytes
- **Type**: typing.Optional[int]


# AdministrativeActionFailureDetails

### Message
- **Type**: typing.Optional[str]


# AdministrativeActionPaginator

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.AdministrativeActionFailureDetails]

### TargetVolumeValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.VolumePaginator]

### TargetSnapshotValues
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SnapshotPaginator]

### TotalTransferBytes
- **Type**: typing.Optional[int]

### RemainingTransferBytes
- **Type**: typing.Optional[int]


# AggregateConfiguration

### Aggregates
- **Type**: typing.Optional[typing.List[str]]

### TotalConstituents
- **Type**: typing.Optional[int]


# Alias

### Name
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATE_FAILED', 'CREATING', 'DELETE_FAILED', 'DELETING']]


# AssociateFileSystemAliasesRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Aliases
- **Type**: typing.List[str]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# AssociateFileSystemAliasesResponse

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Alias]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# AutoExportPolicy

### Events
- **Type**: typing.Optional[typing.List[typing.Literal['CHANGED', 'DELETED', 'NEW']]]


# AutoExportPolicyOutput

### Events
- **Type**: typing.Optional[typing.List[typing.Literal['CHANGED', 'DELETED', 'NEW']]]


# AutoImportPolicy

### Events
- **Type**: typing.Optional[typing.List[typing.Literal['CHANGED', 'DELETED', 'NEW']]]


# AutoImportPolicyOutput

### Events
- **Type**: typing.Optional[typing.List[typing.Literal['CHANGED', 'DELETED', 'NEW']]]


# AutocommitPeriod

### Type
- **Type**: typing.Literal['DAYS', 'HOURS', 'MINUTES', 'MONTHS', 'NONE', 'YEARS']
- **Required**: Yes

### Value
- **Type**: typing.Optional[int]


# Backup

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
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystem'>
- **Required**: Yes

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.BackupFailureDetails]

### ProgressPercent
- **Type**: typing.Optional[int]

### KmsKeyId
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### DirectoryInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.ActiveDirectoryBackupAttributes]

### OwnerId
- **Type**: typing.Optional[str]

### SourceBackupId
- **Type**: typing.Optional[str]

### SourceBackupRegion
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['FILE_SYSTEM', 'VOLUME']]

### Volume
- **Type**: <class 'NoneType'>

### SizeInBytes
- **Type**: typing.Optional[int]


# BackupFailureDetails

### Message
- **Type**: typing.Optional[str]


# BackupPaginator

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
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystemPaginator'>
- **Required**: Yes

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.BackupFailureDetails]

### ProgressPercent
- **Type**: typing.Optional[int]

### KmsKeyId
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### DirectoryInformation
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.ActiveDirectoryBackupAttributes]

### OwnerId
- **Type**: typing.Optional[str]

### SourceBackupId
- **Type**: typing.Optional[str]

### SourceBackupRegion
- **Type**: typing.Optional[str]

### ResourceType
- **Type**: typing.Optional[typing.Literal['FILE_SYSTEM', 'VOLUME']]

### Volume
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.VolumePaginator]

### SizeInBytes
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelDataRepositoryTaskRequest

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes


# CancelDataRepositoryTaskResponse

### Lifecycle
- **Type**: typing.Literal['CANCELED', 'CANCELING', 'EXECUTING', 'FAILED', 'PENDING', 'SUCCEEDED']
- **Required**: Yes

### TaskId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# CompletionReport

### Enabled
- **Type**: <class 'bool'>
- **Required**: Yes

### Path
- **Type**: typing.Optional[str]

### Format
- **Type**: typing.Optional[typing.Literal['REPORT_CSV_20191124']]

### Scope
- **Type**: typing.Optional[typing.Literal['FAILED_FILES_ONLY']]


# CopyBackupRequest

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]


# CopyBackupResponse

### Backup
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.Backup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# CopySnapshotAndUpdateVolumeRequest

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
- **Type**: typing.Optional[typing.List[typing.Literal['DELETE_CLONED_VOLUMES', 'DELETE_INTERMEDIATE_DATA', 'DELETE_INTERMEDIATE_SNAPSHOTS']]]


# CopySnapshotAndUpdateVolumeResponse

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'CREATED', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'PENDING']
- **Required**: Yes

### AdministrativeActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.AdministrativeAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAggregateConfiguration

### Aggregates
- **Type**: typing.Optional[typing.List[str]]

### ConstituentsPerAggregate
- **Type**: typing.Optional[int]


# CreateBackupRequest

### FileSystemId
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### VolumeId
- **Type**: typing.Optional[str]


# CreateBackupResponse

### Backup
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.Backup'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataRepositoryAssociationRequest

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
- **Type**: typing.Union[aws_resource_validator.pydantic_models.fsx.fsx_classes.S3DataRepositoryConfiguration, aws_resource_validator.pydantic_models.fsx.fsx_classes.S3DataRepositoryConfigurationOutput, NoneType]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]


# CreateDataRepositoryAssociationResponse

### Association
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.DataRepositoryAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDataRepositoryTaskRequest

### Type
- **Type**: typing.Literal['AUTO_RELEASE_DATA', 'EXPORT_TO_REPOSITORY', 'IMPORT_METADATA_FROM_REPOSITORY', 'RELEASE_DATA_FROM_FILESYSTEM']
- **Required**: Yes

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Report
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.CompletionReport'>
- **Required**: Yes

### Paths
- **Type**: typing.Optional[typing.List[str]]

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### CapacityToRelease
- **Type**: typing.Optional[int]

### ReleaseConfiguration
- **Type**: <class 'NoneType'>


# CreateDataRepositoryTaskResponse

### DataRepositoryTask
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.DataRepositoryTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFileCacheLustreConfiguration

### PerUnitStorageThroughput
- **Type**: <class 'int'>
- **Required**: Yes

### DeploymentType
- **Type**: typing.Literal['CACHE_1']
- **Required**: Yes

### MetadataConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.FileCacheLustreMetadataConfiguration'>
- **Required**: Yes

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]


# CreateFileCacheRequest

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
- **Type**: typing.List[str]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### CopyTagsToDataRepositoryAssociations
- **Type**: typing.Optional[bool]

### KmsKeyId
- **Type**: typing.Optional[str]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateFileCacheLustreConfiguration]

### DataRepositoryAssociations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileCacheDataRepositoryAssociation]]


# CreateFileCacheResponse

### FileCache
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.FileCacheCreating'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFileSystemFromBackupRequest

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### WindowsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateFileSystemWindowsConfiguration]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateFileSystemLustreConfiguration]

### StorageType
- **Type**: typing.Optional[typing.Literal['HDD', 'INTELLIGENT_TIERING', 'SSD']]

### KmsKeyId
- **Type**: typing.Optional[str]

### FileSystemTypeVersion
- **Type**: typing.Optional[str]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateFileSystemOpenZFSConfiguration]

### StorageCapacity
- **Type**: typing.Optional[int]


# CreateFileSystemFromBackupResponse

### FileSystem
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystem'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFileSystemLustreConfiguration

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

### EfaEnabled
- **Type**: typing.Optional[bool]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.LustreLogCreateConfiguration]

### RootSquashConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.fsx.fsx_classes.LustreRootSquashConfiguration, aws_resource_validator.pydantic_models.fsx.fsx_classes.LustreRootSquashConfigurationOutput, NoneType]

### MetadataConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateFileSystemLustreMetadataConfiguration]


# CreateFileSystemLustreMetadataConfiguration

### Mode
- **Type**: typing.Literal['AUTOMATIC', 'USER_PROVISIONED']
- **Required**: Yes

### Iops
- **Type**: typing.Optional[int]


# CreateFileSystemOntapConfiguration

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
- **Type**: <class 'NoneType'>

### PreferredSubnetId
- **Type**: typing.Optional[str]

### RouteTableIds
- **Type**: typing.Optional[typing.List[str]]

### ThroughputCapacity
- **Type**: typing.Optional[int]

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### HAPairs
- **Type**: typing.Optional[int]

### ThroughputCapacityPerHAPair
- **Type**: typing.Optional[int]


# CreateFileSystemOpenZFSConfiguration

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
- **Type**: <class 'NoneType'>

### RootVolumeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSCreateRootVolumeConfiguration]

### PreferredSubnetId
- **Type**: typing.Optional[str]

### EndpointIpAddressRange
- **Type**: typing.Optional[str]

### RouteTableIds
- **Type**: typing.Optional[typing.List[str]]

### ReadCacheConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSReadCacheConfiguration]


# CreateFileSystemRequest

### FileSystemType
- **Type**: typing.Literal['LUSTRE', 'ONTAP', 'OPENZFS', 'WINDOWS']
- **Required**: Yes

### SubnetIds
- **Type**: typing.List[str]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### StorageCapacity
- **Type**: typing.Optional[int]

### StorageType
- **Type**: typing.Optional[typing.Literal['HDD', 'INTELLIGENT_TIERING', 'SSD']]

### SecurityGroupIds
- **Type**: typing.Optional[typing.List[str]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### KmsKeyId
- **Type**: typing.Optional[str]

### WindowsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateFileSystemWindowsConfiguration]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateFileSystemLustreConfiguration]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateFileSystemOntapConfiguration]

### FileSystemTypeVersion
- **Type**: typing.Optional[str]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateFileSystemOpenZFSConfiguration]


# CreateFileSystemResponse

### FileSystem
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystem'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# CreateFileSystemWindowsConfiguration

### ThroughputCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### ActiveDirectoryId
- **Type**: typing.Optional[str]

### SelfManagedActiveDirectoryConfiguration
- **Type**: <class 'NoneType'>

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
- **Type**: typing.Optional[typing.List[str]]

### AuditLogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.WindowsAuditLogCreateConfiguration]

### DiskIopsConfiguration
- **Type**: <class 'NoneType'>


# CreateOntapVolumeConfiguration

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
- **Type**: <class 'NoneType'>

### OntapVolumeType
- **Type**: typing.Optional[typing.Literal['DP', 'RW']]

### SnapshotPolicy
- **Type**: typing.Optional[str]

### CopyTagsToBackups
- **Type**: typing.Optional[bool]

### SnaplockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateSnaplockConfiguration]

### VolumeStyle
- **Type**: typing.Optional[typing.Literal['FLEXGROUP', 'FLEXVOL']]

### AggregateConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateAggregateConfiguration]

### SizeInBytes
- **Type**: typing.Optional[int]


# CreateOpenZFSOriginSnapshotConfiguration

### SnapshotARN
- **Type**: <class 'str'>
- **Required**: Yes

### CopyStrategy
- **Type**: typing.Literal['CLONE', 'FULL_COPY', 'INCREMENTAL_COPY']
- **Required**: Yes


# CreateOpenZFSVolumeConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateOpenZFSOriginSnapshotConfiguration]

### ReadOnly
- **Type**: typing.Optional[bool]

### NfsExports
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSNfsExport, aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSNfsExportOutput]]]

### UserAndGroupQuotas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSUserOrGroupQuota]]


# CreateSnaplockConfiguration

### SnaplockType
- **Type**: typing.Literal['COMPLIANCE', 'ENTERPRISE']
- **Required**: Yes

### AuditLogVolume
- **Type**: typing.Optional[bool]

### AutocommitPeriod
- **Type**: <class 'NoneType'>

### PrivilegedDelete
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'PERMANENTLY_DISABLED']]

### RetentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SnaplockRetentionPeriod]

### VolumeAppendModeEnabled
- **Type**: typing.Optional[bool]


# CreateSnapshotRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]


# CreateSnapshotResponse

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStorageVirtualMachineRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateSvmActiveDirectoryConfiguration]

### ClientRequestToken
- **Type**: typing.Optional[str]

### SvmAdminPassword
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### RootVolumeSecurityStyle
- **Type**: typing.Optional[typing.Literal['MIXED', 'NTFS', 'UNIX']]


# CreateStorageVirtualMachineResponse

### StorageVirtualMachine
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.StorageVirtualMachine'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSvmActiveDirectoryConfiguration

### NetBiosName
- **Type**: <class 'str'>
- **Required**: Yes

### SelfManagedActiveDirectoryConfiguration
- **Type**: <class 'NoneType'>


# CreateVolumeFromBackupRequest

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateOntapVolumeConfiguration]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]


# CreateVolumeFromBackupResponse

### Volume
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.Volume'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVolumeRequest

### VolumeType
- **Type**: typing.Literal['ONTAP', 'OPENZFS']
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateOntapVolumeConfiguration]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CreateOpenZFSVolumeConfiguration]


# CreateVolumeResponse

### Volume
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.Volume'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# DataRepositoryAssociation

### AssociationId
- **Type**: typing.Optional[str]

### ResourceARN
- **Type**: typing.Optional[str]

### FileSystemId
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'UPDATING']]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.DataRepositoryFailureDetails]

### FileSystemPath
- **Type**: typing.Optional[str]

### DataRepositoryPath
- **Type**: typing.Optional[str]

### BatchImportMetaDataOnCreate
- **Type**: typing.Optional[bool]

### ImportedFileChunkSize
- **Type**: typing.Optional[int]

### S3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.S3DataRepositoryConfigurationOutput]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FileCacheId
- **Type**: typing.Optional[str]

### FileCachePath
- **Type**: typing.Optional[str]

### DataRepositorySubdirectories
- **Type**: typing.Optional[typing.List[str]]

### NFS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.NFSDataRepositoryConfiguration]


# DataRepositoryConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.DataRepositoryFailureDetails]


# DataRepositoryFailureDetails

### Message
- **Type**: typing.Optional[str]


# DataRepositoryTask

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### FileSystemId
- **Type**: typing.Optional[str]

### Paths
- **Type**: typing.Optional[typing.List[str]]

### FailureDetails
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.DataRepositoryTaskFailureDetails]

### Status
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.DataRepositoryTaskStatus]

### Report
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.CompletionReport]

### CapacityToRelease
- **Type**: typing.Optional[int]

### FileCacheId
- **Type**: typing.Optional[str]

### ReleaseConfiguration
- **Type**: <class 'NoneType'>


# DataRepositoryTaskFailureDetails

### Message
- **Type**: typing.Optional[str]


# DataRepositoryTaskFilter

### Name
- **Type**: typing.Optional[typing.Literal['data-repository-association-id', 'file-cache-id', 'file-system-id', 'task-lifecycle']]

### Values
- **Type**: typing.Optional[typing.List[str]]


# DataRepositoryTaskStatus

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


# DeleteBackupRequest

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# DeleteBackupResponse

### BackupId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'COPYING', 'CREATING', 'DELETED', 'FAILED', 'PENDING', 'TRANSFERRING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteDataRepositoryAssociationRequest

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### DeleteDataInFileSystem
- **Type**: typing.Optional[bool]


# DeleteDataRepositoryAssociationResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFileCacheRequest

### FileCacheId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# DeleteFileCacheResponse

### FileCacheId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFileSystemLustreConfiguration

### SkipFinalBackup
- **Type**: typing.Optional[bool]

### FinalBackupTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]


# DeleteFileSystemLustreResponse

### FinalBackupId
- **Type**: typing.Optional[str]

### FinalBackupTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]


# DeleteFileSystemOpenZFSConfiguration

### SkipFinalBackup
- **Type**: typing.Optional[bool]

### FinalBackupTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### Options
- **Type**: typing.Optional[typing.List[typing.Literal['DELETE_CHILD_VOLUMES_AND_SNAPSHOTS']]]


# DeleteFileSystemOpenZFSResponse

### FinalBackupId
- **Type**: typing.Optional[str]

### FinalBackupTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]


# DeleteFileSystemRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### WindowsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.DeleteFileSystemWindowsConfiguration]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.DeleteFileSystemLustreConfiguration]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.DeleteFileSystemOpenZFSConfiguration]


# DeleteFileSystemResponse

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'MISCONFIGURED_UNAVAILABLE', 'UPDATING']
- **Required**: Yes

### WindowsResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.DeleteFileSystemWindowsResponse'>
- **Required**: Yes

### LustreResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.DeleteFileSystemLustreResponse'>
- **Required**: Yes

### OpenZFSResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.DeleteFileSystemOpenZFSResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFileSystemWindowsConfiguration

### SkipFinalBackup
- **Type**: typing.Optional[bool]

### FinalBackupTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]


# DeleteFileSystemWindowsResponse

### FinalBackupId
- **Type**: typing.Optional[str]

### FinalBackupTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]


# DeleteSnapshotRequest

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# DeleteSnapshotResponse

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'CREATING', 'DELETING', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteStorageVirtualMachineRequest

### StorageVirtualMachineId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# DeleteStorageVirtualMachineResponse

### StorageVirtualMachineId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['CREATED', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'PENDING']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVolumeOntapConfiguration

### SkipFinalBackup
- **Type**: typing.Optional[bool]

### FinalBackupTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### BypassSnaplockEnterpriseRetention
- **Type**: typing.Optional[bool]


# DeleteVolumeOntapResponse

### FinalBackupId
- **Type**: typing.Optional[str]

### FinalBackupTags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]


# DeleteVolumeOpenZFSConfiguration

### Options
- **Type**: typing.Optional[typing.List[typing.Literal['DELETE_CHILD_VOLUMES_AND_SNAPSHOTS']]]


# DeleteVolumeRequest

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.DeleteVolumeOntapConfiguration]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.DeleteVolumeOpenZFSConfiguration]


# DeleteVolumeResponse

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'CREATED', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'PENDING']
- **Required**: Yes

### OntapResponse
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.DeleteVolumeOntapResponse'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBackupsRequest

### BackupIds
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeBackupsRequestPaginate

### BackupIds
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Filter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.PaginatorConfig]


# DescribeBackupsResponse

### Backups
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Backup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeBackupsResponsePaginator

### Backups
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.BackupPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDataRepositoryAssociationsRequest

### AssociationIds
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Filter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDataRepositoryAssociationsResponse

### Associations
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.DataRepositoryAssociation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeDataRepositoryTasksRequest

### TaskIds
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.DataRepositoryTaskFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeDataRepositoryTasksResponse

### DataRepositoryTasks
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.DataRepositoryTask]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFileCachesRequest

### FileCacheIds
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFileCachesResponse

### FileCaches
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileCache]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFileSystemAliasesRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFileSystemAliasesResponse

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Alias]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFileSystemsRequest

### FileSystemIds
- **Type**: typing.Optional[typing.List[str]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeFileSystemsRequestPaginate

### FileSystemIds
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.PaginatorConfig]


# DescribeFileSystemsResponse

### FileSystems
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeFileSystemsResponsePaginator

### FileSystems
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystemPaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeSharedVpcConfigurationResponse

### EnableFsxRouteTableUpdatesFromParticipantAccounts
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSnapshotsRequest

### SnapshotIds
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.SnapshotFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### IncludeShared
- **Type**: typing.Optional[bool]


# DescribeSnapshotsResponse

### Snapshots
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Snapshot]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeStorageVirtualMachinesRequest

### StorageVirtualMachineIds
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.StorageVirtualMachineFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeStorageVirtualMachinesRequestPaginate

### StorageVirtualMachineIds
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.StorageVirtualMachineFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.PaginatorConfig]


# DescribeStorageVirtualMachinesResponse

### StorageVirtualMachines
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.StorageVirtualMachine]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeVolumesRequest

### VolumeIds
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.VolumeFilter]]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeVolumesRequestPaginate

### VolumeIds
- **Type**: typing.Optional[typing.List[str]]

### Filters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.VolumeFilter]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.PaginatorConfig]


# DescribeVolumesResponse

### Volumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Volume]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeVolumesResponsePaginator

### Volumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.VolumePaginator]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DisassociateFileSystemAliasesRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### Aliases
- **Type**: typing.List[str]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# DisassociateFileSystemAliasesResponse

### Aliases
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Alias]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# DiskIopsConfiguration

### Mode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'USER_PROVISIONED']]

### Iops
- **Type**: typing.Optional[int]


# DurationSinceLastAccess

### Unit
- **Type**: typing.Optional[typing.Literal['DAYS']]

### Value
- **Type**: typing.Optional[int]


# FileCache

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileCacheFailureDetails]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileCacheLustreConfiguration]

### DataRepositoryAssociationIds
- **Type**: typing.Optional[typing.List[str]]


# FileCacheCreating

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileCacheFailureDetails]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### CopyTagsToDataRepositoryAssociations
- **Type**: typing.Optional[bool]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileCacheLustreConfiguration]

### DataRepositoryAssociationIds
- **Type**: typing.Optional[typing.List[str]]


# FileCacheDataRepositoryAssociation

### FileCachePath
- **Type**: <class 'str'>
- **Required**: Yes

### DataRepositoryPath
- **Type**: <class 'str'>
- **Required**: Yes

### DataRepositorySubdirectories
- **Type**: typing.Optional[typing.List[str]]

### NFS
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileCacheNFSConfiguration]


# FileCacheFailureDetails

### Message
- **Type**: typing.Optional[str]


# FileCacheLustreConfiguration

### PerUnitStorageThroughput
- **Type**: typing.Optional[int]

### DeploymentType
- **Type**: typing.Optional[typing.Literal['CACHE_1']]

### MountName
- **Type**: typing.Optional[str]

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### MetadataConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileCacheLustreMetadataConfiguration]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.LustreLogConfiguration]


# FileCacheLustreMetadataConfiguration

### StorageCapacity
- **Type**: <class 'int'>
- **Required**: Yes


# FileCacheNFSConfiguration

### Version
- **Type**: typing.Literal['NFS3']
- **Required**: Yes

### DnsIps
- **Type**: typing.Optional[typing.List[str]]


# FileSystem

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystemFailureDetails]

### StorageCapacity
- **Type**: typing.Optional[int]

### StorageType
- **Type**: typing.Optional[typing.Literal['HDD', 'INTELLIGENT_TIERING', 'SSD']]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### WindowsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.WindowsFileSystemConfiguration]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.LustreFileSystemConfiguration]

### AdministrativeActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.AdministrativeAction]]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.OntapFileSystemConfiguration]

### FileSystemTypeVersion
- **Type**: typing.Optional[str]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSFileSystemConfiguration]


# FileSystemEndpoint

### DNSName
- **Type**: typing.Optional[str]

### IpAddresses
- **Type**: typing.Optional[typing.List[str]]


# FileSystemEndpoints

### Intercluster
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystemEndpoint]

### Management
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystemEndpoint]


# FileSystemFailureDetails

### Message
- **Type**: typing.Optional[str]


# FileSystemLustreMetadataConfiguration

### Mode
- **Type**: typing.Literal['AUTOMATIC', 'USER_PROVISIONED']
- **Required**: Yes

### Iops
- **Type**: typing.Optional[int]


# FileSystemPaginator

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystemFailureDetails]

### StorageCapacity
- **Type**: typing.Optional[int]

### StorageType
- **Type**: typing.Optional[typing.Literal['HDD', 'INTELLIGENT_TIERING', 'SSD']]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### WindowsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.WindowsFileSystemConfiguration]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.LustreFileSystemConfiguration]

### AdministrativeActions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.AdministrativeActionPaginator]]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.OntapFileSystemConfiguration]

### FileSystemTypeVersion
- **Type**: typing.Optional[str]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSFileSystemConfiguration]


# Filter

### Name
- **Type**: typing.Optional[typing.Literal['backup-type', 'data-repository-type', 'file-cache-id', 'file-cache-type', 'file-system-id', 'file-system-type', 'volume-id']]

### Values
- **Type**: typing.Optional[typing.List[str]]


# LifecycleTransitionReason

### Message
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestPaginate

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.PaginatorConfig]


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LustreFileSystemConfiguration

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### DataRepositoryConfiguration
- **Type**: <class 'NoneType'>

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.LustreLogConfiguration]

### RootSquashConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.LustreRootSquashConfigurationOutput]

### MetadataConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystemLustreMetadataConfiguration]

### EfaEnabled
- **Type**: typing.Optional[bool]


# LustreLogConfiguration

### Level
- **Type**: typing.Literal['DISABLED', 'ERROR_ONLY', 'WARN_ERROR', 'WARN_ONLY']
- **Required**: Yes

### Destination
- **Type**: typing.Optional[str]


# LustreLogCreateConfiguration

### Level
- **Type**: typing.Literal['DISABLED', 'ERROR_ONLY', 'WARN_ERROR', 'WARN_ONLY']
- **Required**: Yes

### Destination
- **Type**: typing.Optional[str]


# LustreRootSquashConfiguration

### RootSquash
- **Type**: typing.Optional[str]

### NoSquashNids
- **Type**: typing.Optional[typing.List[str]]


# LustreRootSquashConfigurationOutput

### RootSquash
- **Type**: typing.Optional[str]

### NoSquashNids
- **Type**: typing.Optional[typing.List[str]]


# NFSDataRepositoryConfiguration

### Version
- **Type**: typing.Literal['NFS3']
- **Required**: Yes

### DnsIps
- **Type**: typing.Optional[typing.List[str]]

### AutoExportPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.AutoExportPolicyOutput]


# OntapFileSystemConfiguration

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### DeploymentType
- **Type**: typing.Optional[typing.Literal['MULTI_AZ_1', 'MULTI_AZ_2', 'SINGLE_AZ_1', 'SINGLE_AZ_2']]

### EndpointIpAddressRange
- **Type**: typing.Optional[str]

### Endpoints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystemEndpoints]

### DiskIopsConfiguration
- **Type**: <class 'NoneType'>

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


# OntapVolumeConfiguration

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
- **Type**: <class 'NoneType'>

### UUID
- **Type**: typing.Optional[str]

### OntapVolumeType
- **Type**: typing.Optional[typing.Literal['DP', 'LS', 'RW']]

### SnapshotPolicy
- **Type**: typing.Optional[str]

### CopyTagsToBackups
- **Type**: typing.Optional[bool]

### SnaplockConfiguration
- **Type**: <class 'NoneType'>

### VolumeStyle
- **Type**: typing.Optional[typing.Literal['FLEXGROUP', 'FLEXVOL']]

### AggregateConfiguration
- **Type**: <class 'NoneType'>

### SizeInBytes
- **Type**: typing.Optional[int]


# OpenZFSClientConfiguration

### Clients
- **Type**: <class 'str'>
- **Required**: Yes

### Options
- **Type**: typing.List[str]
- **Required**: Yes


# OpenZFSClientConfigurationOutput

### Clients
- **Type**: <class 'str'>
- **Required**: Yes

### Options
- **Type**: typing.List[str]
- **Required**: Yes


# OpenZFSCreateRootVolumeConfiguration

### RecordSizeKiB
- **Type**: typing.Optional[int]

### DataCompressionType
- **Type**: typing.Optional[typing.Literal['LZ4', 'NONE', 'ZSTD']]

### NfsExports
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSNfsExport, aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSNfsExportOutput]]]

### UserAndGroupQuotas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSUserOrGroupQuota]]

### CopyTagsToSnapshots
- **Type**: typing.Optional[bool]

### ReadOnly
- **Type**: typing.Optional[bool]


# OpenZFSFileSystemConfiguration

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
- **Type**: <class 'NoneType'>

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

### ReadCacheConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSReadCacheConfiguration]


# OpenZFSNfsExport

### ClientConfigurations
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSClientConfiguration, aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSClientConfigurationOutput]]
- **Required**: Yes


# OpenZFSNfsExportOutput

### ClientConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSClientConfigurationOutput]
- **Required**: Yes


# OpenZFSOriginSnapshotConfiguration

### SnapshotARN
- **Type**: typing.Optional[str]

### CopyStrategy
- **Type**: typing.Optional[typing.Literal['CLONE', 'FULL_COPY', 'INCREMENTAL_COPY']]


# OpenZFSReadCacheConfiguration

### SizingMode
- **Type**: typing.Optional[typing.Literal['NO_CACHE', 'PROPORTIONAL_TO_THROUGHPUT_CAPACITY', 'USER_PROVISIONED']]

### SizeGiB
- **Type**: typing.Optional[int]


# OpenZFSUserOrGroupQuota

### Type
- **Type**: typing.Literal['GROUP', 'USER']
- **Required**: Yes

### Id
- **Type**: <class 'int'>
- **Required**: Yes

### StorageCapacityQuotaGiB
- **Type**: <class 'int'>
- **Required**: Yes


# OpenZFSVolumeConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSOriginSnapshotConfiguration]

### ReadOnly
- **Type**: typing.Optional[bool]

### NfsExports
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSNfsExportOutput]]

### UserAndGroupQuotas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSUserOrGroupQuota]]

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


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ReleaseConfiguration

### DurationSinceLastAccess
- **Type**: <class 'NoneType'>


# ReleaseFileSystemNfsV3LocksRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# ReleaseFileSystemNfsV3LocksResponse

### FileSystem
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystem'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
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


# RestoreVolumeFromSnapshotRequest

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Options
- **Type**: typing.Optional[typing.List[typing.Literal['DELETE_CLONED_VOLUMES', 'DELETE_INTERMEDIATE_SNAPSHOTS']]]


# RestoreVolumeFromSnapshotResponse

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### Lifecycle
- **Type**: typing.Literal['AVAILABLE', 'CREATED', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'PENDING']
- **Required**: Yes

### AdministrativeActions
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.AdministrativeAction]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# RetentionPeriod

### Type
- **Type**: typing.Literal['DAYS', 'HOURS', 'INFINITE', 'MINUTES', 'MONTHS', 'SECONDS', 'UNSPECIFIED', 'YEARS']
- **Required**: Yes

### Value
- **Type**: typing.Optional[int]


# S3DataRepositoryConfiguration

### AutoImportPolicy
- **Type**: <class 'NoneType'>

### AutoExportPolicy
- **Type**: <class 'NoneType'>


# S3DataRepositoryConfigurationOutput

### AutoImportPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.AutoImportPolicyOutput]

### AutoExportPolicy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.AutoExportPolicyOutput]


# SelfManagedActiveDirectoryAttributes

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


# SelfManagedActiveDirectoryConfiguration

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
- **Type**: typing.List[str]
- **Required**: Yes

### OrganizationalUnitDistinguishedName
- **Type**: typing.Optional[str]

### FileSystemAdministratorsGroup
- **Type**: typing.Optional[str]


# SelfManagedActiveDirectoryConfigurationUpdates

### UserName
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### DnsIps
- **Type**: typing.Optional[typing.List[str]]

### DomainName
- **Type**: typing.Optional[str]

### OrganizationalUnitDistinguishedName
- **Type**: typing.Optional[str]

### FileSystemAdministratorsGroup
- **Type**: typing.Optional[str]


# SnaplockConfiguration

### AuditLogVolume
- **Type**: typing.Optional[bool]

### AutocommitPeriod
- **Type**: <class 'NoneType'>

### PrivilegedDelete
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'PERMANENTLY_DISABLED']]

### RetentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SnaplockRetentionPeriod]

### SnaplockType
- **Type**: typing.Optional[typing.Literal['COMPLIANCE', 'ENTERPRISE']]

### VolumeAppendModeEnabled
- **Type**: typing.Optional[bool]


# SnaplockRetentionPeriod

### DefaultRetention
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.RetentionPeriod'>
- **Required**: Yes

### MinimumRetention
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.RetentionPeriod'>
- **Required**: Yes

### MaximumRetention
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.RetentionPeriod'>
- **Required**: Yes


# Snapshot

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
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### AdministrativeActions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# SnapshotFilter

### Name
- **Type**: typing.Optional[typing.Literal['file-system-id', 'volume-id']]

### Values
- **Type**: typing.Optional[typing.List[str]]


# SnapshotPaginator

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
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### AdministrativeActions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]


# StartMisconfiguredStateRecoveryRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartMisconfiguredStateRecoveryResponse

### FileSystem
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystem'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# StorageVirtualMachine

### ActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SvmActiveDirectoryConfiguration]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### Endpoints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SvmEndpoints]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### LifecycleTransitionReason
- **Type**: <class 'NoneType'>

### RootVolumeSecurityStyle
- **Type**: typing.Optional[typing.Literal['MIXED', 'NTFS', 'UNIX']]


# StorageVirtualMachineFilter

### Name
- **Type**: typing.Optional[typing.Literal['file-system-id']]

### Values
- **Type**: typing.Optional[typing.List[str]]


# SvmActiveDirectoryConfiguration

### NetBiosName
- **Type**: typing.Optional[str]

### SelfManagedActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SelfManagedActiveDirectoryAttributes]


# SvmEndpoint

### DNSName
- **Type**: typing.Optional[str]

### IpAddresses
- **Type**: typing.Optional[typing.List[str]]


# SvmEndpoints

### Iscsi
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SvmEndpoint]

### Management
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SvmEndpoint]

### Nfs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SvmEndpoint]

### Smb
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SvmEndpoint]


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
- **Type**: typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]
- **Required**: Yes


# TieringPolicy

### CoolingPeriod
- **Type**: typing.Optional[int]

### Name
- **Type**: typing.Optional[typing.Literal['ALL', 'AUTO', 'NONE', 'SNAPSHOT_ONLY']]


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateDataRepositoryAssociationRequest

### AssociationId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### ImportedFileChunkSize
- **Type**: typing.Optional[int]

### S3
- **Type**: typing.Union[aws_resource_validator.pydantic_models.fsx.fsx_classes.S3DataRepositoryConfiguration, aws_resource_validator.pydantic_models.fsx.fsx_classes.S3DataRepositoryConfigurationOutput, NoneType]


# UpdateDataRepositoryAssociationResponse

### Association
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.DataRepositoryAssociation'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFileCacheLustreConfiguration

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]


# UpdateFileCacheRequest

### FileCacheId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.UpdateFileCacheLustreConfiguration]


# UpdateFileCacheResponse

### FileCache
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.FileCache'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFileSystemLustreConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.LustreLogCreateConfiguration]

### RootSquashConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.fsx.fsx_classes.LustreRootSquashConfiguration, aws_resource_validator.pydantic_models.fsx.fsx_classes.LustreRootSquashConfigurationOutput, NoneType]

### PerUnitStorageThroughput
- **Type**: typing.Optional[int]

### MetadataConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.UpdateFileSystemLustreMetadataConfiguration]


# UpdateFileSystemLustreMetadataConfiguration

### Iops
- **Type**: typing.Optional[int]

### Mode
- **Type**: typing.Optional[typing.Literal['AUTOMATIC', 'USER_PROVISIONED']]


# UpdateFileSystemOntapConfiguration

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### FsxAdminPassword
- **Type**: typing.Optional[str]

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### DiskIopsConfiguration
- **Type**: <class 'NoneType'>

### ThroughputCapacity
- **Type**: typing.Optional[int]

### AddRouteTableIds
- **Type**: typing.Optional[typing.List[str]]

### RemoveRouteTableIds
- **Type**: typing.Optional[typing.List[str]]

### ThroughputCapacityPerHAPair
- **Type**: typing.Optional[int]

### HAPairs
- **Type**: typing.Optional[int]


# UpdateFileSystemOpenZFSConfiguration

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
- **Type**: <class 'NoneType'>

### AddRouteTableIds
- **Type**: typing.Optional[typing.List[str]]

### RemoveRouteTableIds
- **Type**: typing.Optional[typing.List[str]]

### ReadCacheConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSReadCacheConfiguration]


# UpdateFileSystemRequest

### FileSystemId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### StorageCapacity
- **Type**: typing.Optional[int]

### WindowsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.UpdateFileSystemWindowsConfiguration]

### LustreConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.UpdateFileSystemLustreConfiguration]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.UpdateFileSystemOntapConfiguration]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.UpdateFileSystemOpenZFSConfiguration]

### StorageType
- **Type**: typing.Optional[typing.Literal['HDD', 'INTELLIGENT_TIERING', 'SSD']]

### FileSystemTypeVersion
- **Type**: typing.Optional[str]


# UpdateFileSystemResponse

### FileSystem
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.FileSystem'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFileSystemWindowsConfiguration

### WeeklyMaintenanceStartTime
- **Type**: typing.Optional[str]

### DailyAutomaticBackupStartTime
- **Type**: typing.Optional[str]

### AutomaticBackupRetentionDays
- **Type**: typing.Optional[int]

### ThroughputCapacity
- **Type**: typing.Optional[int]

### SelfManagedActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SelfManagedActiveDirectoryConfigurationUpdates]

### AuditLogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.WindowsAuditLogCreateConfiguration]

### DiskIopsConfiguration
- **Type**: <class 'NoneType'>


# UpdateOntapVolumeConfiguration

### JunctionPath
- **Type**: typing.Optional[str]

### SecurityStyle
- **Type**: typing.Optional[typing.Literal['MIXED', 'NTFS', 'UNIX']]

### SizeInMegabytes
- **Type**: typing.Optional[int]

### StorageEfficiencyEnabled
- **Type**: typing.Optional[bool]

### TieringPolicy
- **Type**: <class 'NoneType'>

### SnapshotPolicy
- **Type**: typing.Optional[str]

### CopyTagsToBackups
- **Type**: typing.Optional[bool]

### SnaplockConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.UpdateSnaplockConfiguration]

### SizeInBytes
- **Type**: typing.Optional[int]


# UpdateOpenZFSVolumeConfiguration

### StorageCapacityReservationGiB
- **Type**: typing.Optional[int]

### StorageCapacityQuotaGiB
- **Type**: typing.Optional[int]

### RecordSizeKiB
- **Type**: typing.Optional[int]

### DataCompressionType
- **Type**: typing.Optional[typing.Literal['LZ4', 'NONE', 'ZSTD']]

### NfsExports
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSNfsExport, aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSNfsExportOutput]]]

### UserAndGroupQuotas
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSUserOrGroupQuota]]

### ReadOnly
- **Type**: typing.Optional[bool]


# UpdateSharedVpcConfigurationRequest

### EnableFsxRouteTableUpdatesFromParticipantAccounts
- **Type**: typing.Optional[str]

### ClientRequestToken
- **Type**: typing.Optional[str]


# UpdateSharedVpcConfigurationResponse

### EnableFsxRouteTableUpdatesFromParticipantAccounts
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSnaplockConfiguration

### AuditLogVolume
- **Type**: typing.Optional[bool]

### AutocommitPeriod
- **Type**: <class 'NoneType'>

### PrivilegedDelete
- **Type**: typing.Optional[typing.Literal['DISABLED', 'ENABLED', 'PERMANENTLY_DISABLED']]

### RetentionPeriod
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SnaplockRetentionPeriod]

### VolumeAppendModeEnabled
- **Type**: typing.Optional[bool]


# UpdateSnapshotRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]


# UpdateSnapshotResponse

### Snapshot
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.Snapshot'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStorageVirtualMachineRequest

### StorageVirtualMachineId
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.UpdateSvmActiveDirectoryConfiguration]

### ClientRequestToken
- **Type**: typing.Optional[str]

### SvmAdminPassword
- **Type**: typing.Optional[str]


# UpdateStorageVirtualMachineResponse

### StorageVirtualMachine
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.StorageVirtualMachine'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSvmActiveDirectoryConfiguration

### SelfManagedActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SelfManagedActiveDirectoryConfigurationUpdates]

### NetBiosName
- **Type**: typing.Optional[str]


# UpdateVolumeRequest

### VolumeId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.UpdateOntapVolumeConfiguration]

### Name
- **Type**: typing.Optional[str]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.UpdateOpenZFSVolumeConfiguration]


# UpdateVolumeResponse

### Volume
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.Volume'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.fsx.fsx_classes.ResponseMetadata'>
- **Required**: Yes


# Volume

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FileSystemId
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATED', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'PENDING']]

### Name
- **Type**: typing.Optional[str]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.OntapVolumeConfiguration]

### ResourceARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### VolumeId
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[typing.Literal['ONTAP', 'OPENZFS']]

### LifecycleTransitionReason
- **Type**: <class 'NoneType'>

### AdministrativeActions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSVolumeConfiguration]


# VolumeFilter

### Name
- **Type**: typing.Optional[typing.Literal['file-system-id', 'storage-virtual-machine-id']]

### Values
- **Type**: typing.Optional[typing.List[str]]


# VolumePaginator

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FileSystemId
- **Type**: typing.Optional[str]

### Lifecycle
- **Type**: typing.Optional[typing.Literal['AVAILABLE', 'CREATED', 'CREATING', 'DELETING', 'FAILED', 'MISCONFIGURED', 'PENDING']]

### Name
- **Type**: typing.Optional[str]

### OntapConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.OntapVolumeConfiguration]

### ResourceARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Tag]]

### VolumeId
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[typing.Literal['ONTAP', 'OPENZFS']]

### LifecycleTransitionReason
- **Type**: <class 'NoneType'>

### AdministrativeActions
- **Type**: typing.Optional[typing.List[typing.Dict[str, typing.Any]]]

### OpenZFSConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.OpenZFSVolumeConfiguration]


# WindowsAuditLogConfiguration

### FileAccessAuditLogLevel
- **Type**: typing.Literal['DISABLED', 'FAILURE_ONLY', 'SUCCESS_AND_FAILURE', 'SUCCESS_ONLY']
- **Required**: Yes

### FileShareAccessAuditLogLevel
- **Type**: typing.Literal['DISABLED', 'FAILURE_ONLY', 'SUCCESS_AND_FAILURE', 'SUCCESS_ONLY']
- **Required**: Yes

### AuditLogDestination
- **Type**: typing.Optional[str]


# WindowsAuditLogCreateConfiguration

### FileAccessAuditLogLevel
- **Type**: typing.Literal['DISABLED', 'FAILURE_ONLY', 'SUCCESS_AND_FAILURE', 'SUCCESS_ONLY']
- **Required**: Yes

### FileShareAccessAuditLogLevel
- **Type**: typing.Literal['DISABLED', 'FAILURE_ONLY', 'SUCCESS_AND_FAILURE', 'SUCCESS_ONLY']
- **Required**: Yes

### AuditLogDestination
- **Type**: typing.Optional[str]


# WindowsFileSystemConfiguration

### ActiveDirectoryId
- **Type**: typing.Optional[str]

### SelfManagedActiveDirectoryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.SelfManagedActiveDirectoryAttributes]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.fsx.fsx_classes.Alias]]

### AuditLogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.fsx.fsx_classes.WindowsAuditLogConfiguration]

### DiskIopsConfiguration
- **Type**: <class 'NoneType'>


