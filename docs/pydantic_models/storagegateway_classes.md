# Storagegateway Classes

# ActivateGatewayInputTypeDef

### ActivationKey
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayTimezone
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayRegion
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayType
- **Type**: typing.Optional[str]

### TapeDriveType
- **Type**: typing.Optional[str]

### MediumChangerType
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]


# ActivateGatewayOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddCacheInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### DiskIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AddCacheOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddTagsToResourceInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]
- **Required**: Yes


# AddTagsToResourceOutputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddUploadBufferInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### DiskIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AddUploadBufferOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AddWorkingStorageInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### DiskIds
- **Type**: typing.Sequence[str]
- **Required**: Yes


# AddWorkingStorageOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssignTapePoolInputTypeDef

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### BypassGovernanceRetention
- **Type**: typing.Optional[bool]


# AssignTapePoolOutputTypeDef

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AssociateFileSystemInputTypeDef

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### LocationARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]

### AuditDestinationARN
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.CacheAttributesTypeDef]

### EndpointNetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.EndpointNetworkConfigurationUnionTypeDef]


# AssociateFileSystemOutputTypeDef

### FileSystemAssociationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachVolumeInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### TargetName
- **Type**: typing.Optional[str]

### DiskId
- **Type**: typing.Optional[str]


# AttachVolumeOutputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AutomaticTapeCreationPolicyInfoTypeDef

### AutomaticTapeCreationRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.AutomaticTapeCreationRuleTypeDef]]

### GatewayARN
- **Type**: typing.Optional[str]


# AutomaticTapeCreationRuleTypeDef

### TapeBarcodePrefix
- **Type**: <class 'str'>
- **Required**: Yes

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### TapeSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### MinimumNumTapes
- **Type**: <class 'int'>
- **Required**: Yes

### Worm
- **Type**: typing.Optional[bool]


# BandwidthRateLimitIntervalOutputTypeDef

### StartHourOfDay
- **Type**: <class 'int'>
- **Required**: Yes

### StartMinuteOfHour
- **Type**: <class 'int'>
- **Required**: Yes

### EndHourOfDay
- **Type**: <class 'int'>
- **Required**: Yes

### EndMinuteOfHour
- **Type**: <class 'int'>
- **Required**: Yes

### DaysOfWeek
- **Type**: typing.List[int]
- **Required**: Yes

### AverageUploadRateLimitInBitsPerSec
- **Type**: typing.Optional[int]

### AverageDownloadRateLimitInBitsPerSec
- **Type**: typing.Optional[int]


# BandwidthRateLimitIntervalTypeDef

### StartHourOfDay
- **Type**: <class 'int'>
- **Required**: Yes

### StartMinuteOfHour
- **Type**: <class 'int'>
- **Required**: Yes

### EndHourOfDay
- **Type**: <class 'int'>
- **Required**: Yes

### EndMinuteOfHour
- **Type**: <class 'int'>
- **Required**: Yes

### DaysOfWeek
- **Type**: typing.Sequence[int]
- **Required**: Yes

### AverageUploadRateLimitInBitsPerSec
- **Type**: typing.Optional[int]

### AverageDownloadRateLimitInBitsPerSec
- **Type**: typing.Optional[int]


# BandwidthRateLimitIntervalUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CacheAttributesTypeDef

### CacheStaleTimeoutInSeconds
- **Type**: typing.Optional[int]


# CacheReportFilterOutputTypeDef

### Name
- **Type**: typing.Literal['UploadFailureReason', 'UploadState']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# CacheReportFilterTypeDef

### Name
- **Type**: typing.Literal['UploadFailureReason', 'UploadState']
- **Required**: Yes

### Values
- **Type**: typing.Sequence[str]
- **Required**: Yes


# CacheReportFilterUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CacheReportInfoTypeDef

### CacheReportARN
- **Type**: typing.Optional[str]

### CacheReportStatus
- **Type**: typing.Optional[typing.Literal['CANCELED', 'COMPLETED', 'ERROR', 'FAILED', 'IN_PROGRESS']]

### ReportCompletionPercent
- **Type**: typing.Optional[int]

### EndTime
- **Type**: typing.Optional[datetime.datetime]

### Role
- **Type**: typing.Optional[str]

### FileShareARN
- **Type**: typing.Optional[str]

### LocationARN
- **Type**: typing.Optional[str]

### StartTime
- **Type**: typing.Optional[datetime.datetime]

### InclusionFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.CacheReportFilterOutputTypeDef]]

### ExclusionFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.CacheReportFilterOutputTypeDef]]

### ReportName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]


# CachediSCSIVolumeTypeDef

### VolumeARN
- **Type**: typing.Optional[str]

### VolumeId
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[str]

### VolumeStatus
- **Type**: typing.Optional[str]

### VolumeAttachmentStatus
- **Type**: typing.Optional[str]

### VolumeSizeInBytes
- **Type**: typing.Optional[int]

### VolumeProgress
- **Type**: typing.Optional[float]

### SourceSnapshotId
- **Type**: typing.Optional[str]

### VolumeiSCSIAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.VolumeiSCSIAttributesTypeDef]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### VolumeUsedInBytes
- **Type**: typing.Optional[int]

### KMSKey
- **Type**: typing.Optional[str]

### TargetName
- **Type**: typing.Optional[str]


# CancelArchivalInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes


# CancelArchivalOutputTypeDef

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelCacheReportInputTypeDef

### CacheReportARN
- **Type**: <class 'str'>
- **Required**: Yes


# CancelCacheReportOutputTypeDef

### CacheReportARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CancelRetrievalInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes


# CancelRetrievalOutputTypeDef

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ChapInfoTypeDef

### TargetARN
- **Type**: typing.Optional[str]

### SecretToAuthenticateInitiator
- **Type**: typing.Optional[str]

### InitiatorName
- **Type**: typing.Optional[str]

### SecretToAuthenticateTarget
- **Type**: typing.Optional[str]


# CreateCachediSCSIVolumeInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### TargetName
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: typing.Optional[str]

### SourceVolumeARN
- **Type**: typing.Optional[str]

### KMSEncrypted
- **Type**: typing.Optional[bool]

### KMSKey
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]


# CreateCachediSCSIVolumeOutputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateNFSFileShareOutputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSMBFileShareOutputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSnapshotFromVolumeRecoveryPointInputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]


# CreateSnapshotFromVolumeRecoveryPointOutputTypeDef

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeRecoveryPointTime
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSnapshotInputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]


# CreateSnapshotOutputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStorediSCSIVolumeInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### DiskId
- **Type**: <class 'str'>
- **Required**: Yes

### PreserveExistingData
- **Type**: <class 'bool'>
- **Required**: Yes

### TargetName
- **Type**: <class 'str'>
- **Required**: Yes

### NetworkInterfaceId
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: typing.Optional[str]

### KMSEncrypted
- **Type**: typing.Optional[bool]

### KMSKey
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]


# CreateStorediSCSIVolumeOutputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTapePoolInputTypeDef

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### StorageClass
- **Type**: typing.Literal['DEEP_ARCHIVE', 'GLACIER']
- **Required**: Yes

### RetentionLockType
- **Type**: typing.Optional[typing.Literal['COMPLIANCE', 'GOVERNANCE', 'NONE']]

### RetentionLockTimeInDays
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]


# CreateTapePoolOutputTypeDef

### PoolARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTapeWithBarcodeInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### TapeBarcode
- **Type**: <class 'str'>
- **Required**: Yes

### KMSEncrypted
- **Type**: typing.Optional[bool]

### KMSKey
- **Type**: typing.Optional[str]

### PoolId
- **Type**: typing.Optional[str]

### Worm
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]


# CreateTapeWithBarcodeOutputTypeDef

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateTapesInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeSizeInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### NumTapesToCreate
- **Type**: <class 'int'>
- **Required**: Yes

### TapeBarcodePrefix
- **Type**: <class 'str'>
- **Required**: Yes

### KMSEncrypted
- **Type**: typing.Optional[bool]

### KMSKey
- **Type**: typing.Optional[str]

### PoolId
- **Type**: typing.Optional[str]

### Worm
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]


# CreateTapesOutputTypeDef

### TapeARNs
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteAutomaticTapeCreationPolicyInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAutomaticTapeCreationPolicyOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteBandwidthRateLimitInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### BandwidthType
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBandwidthRateLimitOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteCacheReportInputTypeDef

### CacheReportARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCacheReportOutputTypeDef

### CacheReportARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteChapCredentialsInputTypeDef

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### InitiatorName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChapCredentialsOutputTypeDef

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### InitiatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteFileShareInputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDelete
- **Type**: typing.Optional[bool]


# DeleteFileShareOutputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteGatewayInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGatewayOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteSnapshotScheduleInputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotScheduleOutputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTapeArchiveInputTypeDef

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### BypassGovernanceRetention
- **Type**: typing.Optional[bool]


# DeleteTapeArchiveOutputTypeDef

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTapeInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### BypassGovernanceRetention
- **Type**: typing.Optional[bool]


# DeleteTapeOutputTypeDef

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteTapePoolInputTypeDef

### PoolARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTapePoolOutputTypeDef

### PoolARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteVolumeInputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVolumeOutputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeAvailabilityMonitorTestInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAvailabilityMonitorTestOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['COMPLETE', 'FAILED', 'PENDING']
- **Required**: Yes

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBandwidthRateLimitInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBandwidthRateLimitOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### AverageUploadRateLimitInBitsPerSec
- **Type**: <class 'int'>
- **Required**: Yes

### AverageDownloadRateLimitInBitsPerSec
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeBandwidthRateLimitScheduleInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBandwidthRateLimitScheduleOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### BandwidthRateLimitIntervals
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.BandwidthRateLimitIntervalOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCacheInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCacheOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### DiskIds
- **Type**: typing.List[str]
- **Required**: Yes

### CacheAllocatedInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### CacheUsedPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### CacheDirtyPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### CacheHitPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### CacheMissPercentage
- **Type**: <class 'float'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCacheReportInputTypeDef

### CacheReportARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCacheReportOutputTypeDef

### CacheReportInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.CacheReportInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeCachediSCSIVolumesInputTypeDef

### VolumeARNs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeCachediSCSIVolumesOutputTypeDef

### CachediSCSIVolumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.CachediSCSIVolumeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeChapCredentialsInputTypeDef

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChapCredentialsOutputTypeDef

### ChapCredentials
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.ChapInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeFileSystemAssociationsInputTypeDef

### FileSystemAssociationARNList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeFileSystemAssociationsOutputTypeDef

### FileSystemAssociationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.FileSystemAssociationInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeGatewayInformationInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGatewayInformationOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayId
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayTimezone
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayState
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayNetworkInterfaces
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.NetworkInterfaceTypeDef]
- **Required**: Yes

### GatewayType
- **Type**: <class 'str'>
- **Required**: Yes

### NextUpdateAvailabilityDate
- **Type**: <class 'str'>
- **Required**: Yes

### LastSoftwareUpdate
- **Type**: <class 'str'>
- **Required**: Yes

### Ec2InstanceId
- **Type**: <class 'str'>
- **Required**: Yes

### Ec2InstanceRegion
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]
- **Required**: Yes

### VPCEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### CloudWatchLogGroupARN
- **Type**: <class 'str'>
- **Required**: Yes

### HostEnvironment
- **Type**: typing.Literal['EC2', 'HYPER-V', 'KVM', 'OTHER', 'SNOWBALL', 'VMWARE']
- **Required**: Yes

### EndpointType
- **Type**: <class 'str'>
- **Required**: Yes

### SoftwareUpdatesEndDate
- **Type**: <class 'str'>
- **Required**: Yes

### DeprecationDate
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayCapacity
- **Type**: typing.Literal['Large', 'Medium', 'Small']
- **Required**: Yes

### SupportedGatewayCapacities
- **Type**: typing.List[typing.Literal['Large', 'Medium', 'Small']]
- **Required**: Yes

### HostEnvironmentId
- **Type**: <class 'str'>
- **Required**: Yes

### SoftwareVersion
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMaintenanceStartTimeInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMaintenanceStartTimeOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### HourOfDay
- **Type**: <class 'int'>
- **Required**: Yes

### MinuteOfHour
- **Type**: <class 'int'>
- **Required**: Yes

### DayOfWeek
- **Type**: <class 'int'>
- **Required**: Yes

### DayOfMonth
- **Type**: <class 'int'>
- **Required**: Yes

### Timezone
- **Type**: <class 'str'>
- **Required**: Yes

### SoftwareUpdatePreferences
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.SoftwareUpdatePreferencesTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNFSFileSharesInputTypeDef

### FileShareARNList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeNFSFileSharesOutputTypeDef

### NFSFileShareInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.NFSFileShareInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSMBFileSharesInputTypeDef

### FileShareARNList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeSMBFileSharesOutputTypeDef

### SMBFileShareInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.SMBFileShareInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSMBSettingsInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSMBSettingsOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveDirectoryStatus
- **Type**: typing.Literal['ACCESS_DENIED', 'DETACHED', 'JOINED', 'JOINING', 'NETWORK_ERROR', 'TIMEOUT', 'UNKNOWN_ERROR']
- **Required**: Yes

### SMBGuestPasswordSet
- **Type**: <class 'bool'>
- **Required**: Yes

### SMBSecurityStrategy
- **Type**: typing.Literal['ClientSpecified', 'MandatoryEncryption', 'MandatoryEncryptionNoAes128', 'MandatorySigning']
- **Required**: Yes

### FileSharesVisible
- **Type**: <class 'bool'>
- **Required**: Yes

### SMBLocalGroups
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.SMBLocalGroupsOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSnapshotScheduleInputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSnapshotScheduleOutputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### StartAt
- **Type**: <class 'int'>
- **Required**: Yes

### RecurrenceInHours
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Timezone
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStorediSCSIVolumesInputTypeDef

### VolumeARNs
- **Type**: typing.Sequence[str]
- **Required**: Yes


# DescribeStorediSCSIVolumesOutputTypeDef

### StorediSCSIVolumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.StorediSCSIVolumeTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTapeArchivesInputPaginateTypeDef

### TapeARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# DescribeTapeArchivesInputTypeDef

### TapeARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeTapeArchivesOutputTypeDef

### TapeArchives
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.TapeArchiveTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTapeRecoveryPointsInputPaginateTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# DescribeTapeRecoveryPointsInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeTapeRecoveryPointsOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeRecoveryPointInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.TapeRecoveryPointInfoTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeTapesInputPaginateTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# DescribeTapesInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeTapesOutputTypeDef

### Tapes
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.TapeTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeUploadBufferInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUploadBufferOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### DiskIds
- **Type**: typing.List[str]
- **Required**: Yes

### UploadBufferUsedInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### UploadBufferAllocatedInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVTLDevicesInputPaginateTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### VTLDeviceARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# DescribeVTLDevicesInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### VTLDeviceARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeVTLDevicesOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### VTLDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.VTLDeviceTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeWorkingStorageInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkingStorageOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### DiskIds
- **Type**: typing.List[str]
- **Required**: Yes

### WorkingStorageUsedInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### WorkingStorageAllocatedInBytes
- **Type**: <class 'int'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DetachVolumeInputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDetach
- **Type**: typing.Optional[bool]


# DetachVolumeOutputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeviceiSCSIAttributesTypeDef

### TargetARN
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### NetworkInterfacePort
- **Type**: typing.Optional[int]

### ChapEnabled
- **Type**: typing.Optional[bool]


# DisableGatewayInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DisableGatewayOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DisassociateFileSystemInputTypeDef

### FileSystemAssociationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDelete
- **Type**: typing.Optional[bool]


# DisassociateFileSystemOutputTypeDef

### FileSystemAssociationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DiskTypeDef

### DiskId
- **Type**: typing.Optional[str]

### DiskPath
- **Type**: typing.Optional[str]

### DiskNode
- **Type**: typing.Optional[str]

### DiskStatus
- **Type**: typing.Optional[str]

### DiskSizeInBytes
- **Type**: typing.Optional[int]

### DiskAllocationType
- **Type**: typing.Optional[str]

### DiskAllocationResource
- **Type**: typing.Optional[str]

### DiskAttributeList
- **Type**: typing.Optional[typing.List[str]]


# EndpointNetworkConfigurationOutputTypeDef

### IpAddresses
- **Type**: typing.Optional[typing.List[str]]


# EndpointNetworkConfigurationTypeDef

### IpAddresses
- **Type**: typing.Optional[typing.Sequence[str]]


# EndpointNetworkConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# EvictFilesFailingUploadInputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ForceRemove
- **Type**: typing.Optional[bool]


# EvictFilesFailingUploadOutputTypeDef

### NotificationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FileShareInfoTypeDef

### FileShareType
- **Type**: typing.Optional[typing.Literal['NFS', 'SMB']]

### FileShareARN
- **Type**: typing.Optional[str]

### FileShareId
- **Type**: typing.Optional[str]

### FileShareStatus
- **Type**: typing.Optional[str]

### GatewayARN
- **Type**: typing.Optional[str]


# FileSystemAssociationInfoTypeDef

### FileSystemAssociationARN
- **Type**: typing.Optional[str]

### LocationARN
- **Type**: typing.Optional[str]

### FileSystemAssociationStatus
- **Type**: typing.Optional[str]

### AuditDestinationARN
- **Type**: typing.Optional[str]

### GatewayARN
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]

### CacheAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.CacheAttributesTypeDef]

### EndpointNetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.EndpointNetworkConfigurationOutputTypeDef]

### FileSystemAssociationStatusDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.FileSystemAssociationStatusDetailTypeDef]]


# FileSystemAssociationStatusDetailTypeDef

### ErrorCode
- **Type**: typing.Optional[str]


# FileSystemAssociationSummaryTypeDef

### FileSystemAssociationId
- **Type**: typing.Optional[str]

### FileSystemAssociationARN
- **Type**: typing.Optional[str]

### FileSystemAssociationStatus
- **Type**: typing.Optional[str]

### GatewayARN
- **Type**: typing.Optional[str]


# GatewayInfoTypeDef

### GatewayId
- **Type**: typing.Optional[str]

### GatewayARN
- **Type**: typing.Optional[str]

### GatewayType
- **Type**: typing.Optional[str]

### GatewayOperationalState
- **Type**: typing.Optional[str]

### GatewayName
- **Type**: typing.Optional[str]

### Ec2InstanceId
- **Type**: typing.Optional[str]

### Ec2InstanceRegion
- **Type**: typing.Optional[str]

### HostEnvironment
- **Type**: typing.Optional[typing.Literal['EC2', 'HYPER-V', 'KVM', 'OTHER', 'SNOWBALL', 'VMWARE']]

### HostEnvironmentId
- **Type**: typing.Optional[str]

### DeprecationDate
- **Type**: typing.Optional[str]

### SoftwareVersion
- **Type**: typing.Optional[str]


# JoinDomainInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes

### OrganizationalUnit
- **Type**: typing.Optional[str]

### DomainControllers
- **Type**: typing.Optional[typing.Sequence[str]]

### TimeoutInSeconds
- **Type**: typing.Optional[int]


# JoinDomainOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveDirectoryStatus
- **Type**: typing.Literal['ACCESS_DENIED', 'DETACHED', 'JOINED', 'JOINING', 'NETWORK_ERROR', 'TIMEOUT', 'UNKNOWN_ERROR']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListAutomaticTapeCreationPoliciesInputTypeDef

### GatewayARN
- **Type**: typing.Optional[str]


# ListAutomaticTapeCreationPoliciesOutputTypeDef

### AutomaticTapeCreationPolicyInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.AutomaticTapeCreationPolicyInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListCacheReportsInputTypeDef

### Marker
- **Type**: typing.Optional[str]


# ListCacheReportsOutputTypeDef

### CacheReportList
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.CacheReportInfoTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFileSharesInputPaginateTypeDef

### GatewayARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListFileSharesInputTypeDef

### GatewayARN
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListFileSharesOutputTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### FileShareInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.FileShareInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFileSystemAssociationsInputPaginateTypeDef

### GatewayARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListFileSystemAssociationsInputTypeDef

### GatewayARN
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListFileSystemAssociationsOutputTypeDef

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemAssociationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.FileSystemAssociationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListGatewaysInputPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListGatewaysInputTypeDef

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListGatewaysOutputTypeDef

### Gateways
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.GatewayInfoTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLocalDisksInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListLocalDisksOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### Disks
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.DiskTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceInputPaginateTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListTagsForResourceInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTagsForResourceOutputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTapePoolsInputPaginateTypeDef

### PoolARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListTapePoolsInputTypeDef

### PoolARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTapePoolsOutputTypeDef

### PoolInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.PoolInfoTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTapesInputPaginateTypeDef

### TapeARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListTapesInputTypeDef

### TapeARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTapesOutputTypeDef

### TapeInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.TapeInfoTypeDef]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVolumeInitiatorsInputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListVolumeInitiatorsOutputTypeDef

### Initiators
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVolumeRecoveryPointsInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListVolumeRecoveryPointsOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeRecoveryPointInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.VolumeRecoveryPointInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVolumesInputPaginateTypeDef

### GatewayARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListVolumesInputTypeDef

### GatewayARN
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListVolumesOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.VolumeInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NFSFileShareDefaultsTypeDef

### FileMode
- **Type**: typing.Optional[str]

### DirectoryMode
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[int]

### OwnerId
- **Type**: typing.Optional[int]


# NFSFileShareInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# NetworkInterfaceTypeDef

### Ipv4Address
- **Type**: typing.Optional[str]

### MacAddress
- **Type**: typing.Optional[str]

### Ipv6Address
- **Type**: typing.Optional[str]


# NotifyWhenUploadedInputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes


# NotifyWhenUploadedOutputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PoolInfoTypeDef

### PoolARN
- **Type**: typing.Optional[str]

### PoolName
- **Type**: typing.Optional[str]

### StorageClass
- **Type**: typing.Optional[typing.Literal['DEEP_ARCHIVE', 'GLACIER']]

### RetentionLockType
- **Type**: typing.Optional[typing.Literal['COMPLIANCE', 'GOVERNANCE', 'NONE']]

### RetentionLockTimeInDays
- **Type**: typing.Optional[int]

### PoolStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DELETED']]


# RefreshCacheInputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### FolderList
- **Type**: typing.Optional[typing.Sequence[str]]

### Recursive
- **Type**: typing.Optional[bool]


# RefreshCacheOutputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RemoveTagsFromResourceInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# RemoveTagsFromResourceOutputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ResetCacheInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# ResetCacheOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
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


# RetrieveTapeArchiveInputTypeDef

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveTapeArchiveOutputTypeDef

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RetrieveTapeRecoveryPointInputTypeDef

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveTapeRecoveryPointOutputTypeDef

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SMBFileShareInfoTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SMBLocalGroupsOutputTypeDef

### GatewayAdmins
- **Type**: typing.Optional[typing.List[str]]


# SMBLocalGroupsTypeDef

### GatewayAdmins
- **Type**: typing.Optional[typing.Sequence[str]]


# SMBLocalGroupsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SetLocalConsolePasswordInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### LocalConsolePassword
- **Type**: <class 'str'>
- **Required**: Yes


# SetLocalConsolePasswordOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SetSMBGuestPasswordInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# SetSMBGuestPasswordOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ShutdownGatewayInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# ShutdownGatewayOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# SoftwareUpdatePreferencesTypeDef

### AutomaticUpdatePolicy
- **Type**: typing.Optional[typing.Literal['ALL_VERSIONS', 'EMERGENCY_VERSIONS_ONLY']]


# StartAvailabilityMonitorTestInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# StartAvailabilityMonitorTestOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartCacheReportInputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### LocationARN
- **Type**: <class 'str'>
- **Required**: Yes

### BucketRegion
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### VPCEndpointDNSName
- **Type**: typing.Optional[str]

### InclusionFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.CacheReportFilterUnionTypeDef]]

### ExclusionFilters
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.CacheReportFilterUnionTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]


# StartCacheReportOutputTypeDef

### CacheReportARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartGatewayInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# StartGatewayOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StorediSCSIVolumeTypeDef

### VolumeARN
- **Type**: typing.Optional[str]

### VolumeId
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[str]

### VolumeStatus
- **Type**: typing.Optional[str]

### VolumeAttachmentStatus
- **Type**: typing.Optional[str]

### VolumeSizeInBytes
- **Type**: typing.Optional[int]

### VolumeProgress
- **Type**: typing.Optional[float]

### VolumeDiskId
- **Type**: typing.Optional[str]

### SourceSnapshotId
- **Type**: typing.Optional[str]

### PreservedExistingData
- **Type**: typing.Optional[bool]

### VolumeiSCSIAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.VolumeiSCSIAttributesTypeDef]

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### VolumeUsedInBytes
- **Type**: typing.Optional[int]

### KMSKey
- **Type**: typing.Optional[str]

### TargetName
- **Type**: typing.Optional[str]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TapeArchiveTypeDef

### TapeARN
- **Type**: typing.Optional[str]

### TapeBarcode
- **Type**: typing.Optional[str]

### TapeCreatedDate
- **Type**: typing.Optional[datetime.datetime]

### TapeSizeInBytes
- **Type**: typing.Optional[int]

### CompletionTime
- **Type**: typing.Optional[datetime.datetime]

### RetrievedTo
- **Type**: typing.Optional[str]

### TapeStatus
- **Type**: typing.Optional[str]

### TapeUsedInBytes
- **Type**: typing.Optional[int]

### KMSKey
- **Type**: typing.Optional[str]

### PoolId
- **Type**: typing.Optional[str]

### Worm
- **Type**: typing.Optional[bool]

### RetentionStartDate
- **Type**: typing.Optional[datetime.datetime]

### PoolEntryDate
- **Type**: typing.Optional[datetime.datetime]


# TapeInfoTypeDef

### TapeARN
- **Type**: typing.Optional[str]

### TapeBarcode
- **Type**: typing.Optional[str]

### TapeSizeInBytes
- **Type**: typing.Optional[int]

### TapeStatus
- **Type**: typing.Optional[str]

### GatewayARN
- **Type**: typing.Optional[str]

### PoolId
- **Type**: typing.Optional[str]

### RetentionStartDate
- **Type**: typing.Optional[datetime.datetime]

### PoolEntryDate
- **Type**: typing.Optional[datetime.datetime]


# TapeRecoveryPointInfoTypeDef

### TapeARN
- **Type**: typing.Optional[str]

### TapeRecoveryPointTime
- **Type**: typing.Optional[datetime.datetime]

### TapeSizeInBytes
- **Type**: typing.Optional[int]

### TapeStatus
- **Type**: typing.Optional[str]


# TapeTypeDef

### TapeARN
- **Type**: typing.Optional[str]

### TapeBarcode
- **Type**: typing.Optional[str]

### TapeCreatedDate
- **Type**: typing.Optional[datetime.datetime]

### TapeSizeInBytes
- **Type**: typing.Optional[int]

### TapeStatus
- **Type**: typing.Optional[str]

### VTLDevice
- **Type**: typing.Optional[str]

### Progress
- **Type**: typing.Optional[float]

### TapeUsedInBytes
- **Type**: typing.Optional[int]

### KMSKey
- **Type**: typing.Optional[str]

### PoolId
- **Type**: typing.Optional[str]

### Worm
- **Type**: typing.Optional[bool]

### RetentionStartDate
- **Type**: typing.Optional[datetime.datetime]

### PoolEntryDate
- **Type**: typing.Optional[datetime.datetime]


# UpdateAutomaticTapeCreationPolicyInputTypeDef

### AutomaticTapeCreationRules
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.AutomaticTapeCreationRuleTypeDef]
- **Required**: Yes

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAutomaticTapeCreationPolicyOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBandwidthRateLimitInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### AverageUploadRateLimitInBitsPerSec
- **Type**: typing.Optional[int]

### AverageDownloadRateLimitInBitsPerSec
- **Type**: typing.Optional[int]


# UpdateBandwidthRateLimitOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateBandwidthRateLimitScheduleInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### BandwidthRateLimitIntervals
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.BandwidthRateLimitIntervalUnionTypeDef]
- **Required**: Yes


# UpdateBandwidthRateLimitScheduleOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChapCredentialsInputTypeDef

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### SecretToAuthenticateInitiator
- **Type**: <class 'str'>
- **Required**: Yes

### InitiatorName
- **Type**: <class 'str'>
- **Required**: Yes

### SecretToAuthenticateTarget
- **Type**: typing.Optional[str]


# UpdateChapCredentialsOutputTypeDef

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### InitiatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateFileSystemAssociationInputTypeDef

### FileSystemAssociationARN
- **Type**: <class 'str'>
- **Required**: Yes

### UserName
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### AuditDestinationARN
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.CacheAttributesTypeDef]


# UpdateFileSystemAssociationOutputTypeDef

### FileSystemAssociationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGatewayInformationInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayName
- **Type**: typing.Optional[str]

### GatewayTimezone
- **Type**: typing.Optional[str]

### CloudWatchLogGroupARN
- **Type**: typing.Optional[str]

### GatewayCapacity
- **Type**: typing.Optional[typing.Literal['Large', 'Medium', 'Small']]


# UpdateGatewayInformationOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateGatewaySoftwareNowInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateGatewaySoftwareNowOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMaintenanceStartTimeInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### HourOfDay
- **Type**: typing.Optional[int]

### MinuteOfHour
- **Type**: typing.Optional[int]

### DayOfWeek
- **Type**: typing.Optional[int]

### DayOfMonth
- **Type**: typing.Optional[int]

### SoftwareUpdatePreferences
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.SoftwareUpdatePreferencesTypeDef]


# UpdateMaintenanceStartTimeOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateNFSFileShareOutputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSMBFileShareOutputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSMBFileShareVisibilityInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileSharesVisible
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateSMBFileShareVisibilityOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSMBLocalGroupsInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### SMBLocalGroups
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.SMBLocalGroupsUnionTypeDef'>
- **Required**: Yes


# UpdateSMBLocalGroupsOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSMBSecurityStrategyInputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### SMBSecurityStrategy
- **Type**: typing.Literal['ClientSpecified', 'MandatoryEncryption', 'MandatoryEncryptionNoAes128', 'MandatorySigning']
- **Required**: Yes


# UpdateSMBSecurityStrategyOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSnapshotScheduleInputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### StartAt
- **Type**: <class 'int'>
- **Required**: Yes

### RecurrenceInHours
- **Type**: <class 'int'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]


# UpdateSnapshotScheduleOutputTypeDef

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVTLDeviceTypeInputTypeDef

### VTLDeviceARN
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceType
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateVTLDeviceTypeOutputTypeDef

### VTLDeviceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VTLDeviceTypeDef

### VTLDeviceARN
- **Type**: typing.Optional[str]

### VTLDeviceType
- **Type**: typing.Optional[str]

### VTLDeviceVendor
- **Type**: typing.Optional[str]

### VTLDeviceProductIdentifier
- **Type**: typing.Optional[str]

### DeviceiSCSIAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.DeviceiSCSIAttributesTypeDef]


# VolumeInfoTypeDef

### VolumeARN
- **Type**: typing.Optional[str]

### VolumeId
- **Type**: typing.Optional[str]

### GatewayARN
- **Type**: typing.Optional[str]

### GatewayId
- **Type**: typing.Optional[str]

### VolumeType
- **Type**: typing.Optional[str]

### VolumeSizeInBytes
- **Type**: typing.Optional[int]

### VolumeAttachmentStatus
- **Type**: typing.Optional[str]


# VolumeRecoveryPointInfoTypeDef

### VolumeARN
- **Type**: typing.Optional[str]

### VolumeSizeInBytes
- **Type**: typing.Optional[int]

### VolumeUsageInBytes
- **Type**: typing.Optional[int]

### VolumeRecoveryPointTime
- **Type**: typing.Optional[str]


# VolumeiSCSIAttributesTypeDef

### TargetARN
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### NetworkInterfacePort
- **Type**: typing.Optional[int]

### LunNumber
- **Type**: typing.Optional[int]

### ChapEnabled
- **Type**: typing.Optional[bool]


