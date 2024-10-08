# Pydantic Models in storagegateway_classes

# ActivateGatewayInputRequestTypeDef

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


# AddCacheInputRequestTypeDef

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


# AddTagsToResourceInputRequestTypeDef

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


# AddUploadBufferInputRequestTypeDef

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


# AddWorkingStorageInputRequestTypeDef

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


# AssignTapePoolInputRequestTypeDef

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


# AssociateFileSystemInputRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.EndpointNetworkConfigurationTypeDef]


# AssociateFileSystemOutputTypeDef

### FileSystemAssociationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# AttachVolumeInputRequestTypeDef

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


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CacheAttributesTypeDef

### CacheStaleTimeoutInSeconds
- **Type**: typing.Optional[int]


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


# CancelArchivalInputRequestTypeDef

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


# CancelRetrievalInputRequestTypeDef

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


# CreateCachediSCSIVolumeInputRequestTypeDef

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


# CreateNFSFileShareInputRequestTypeDef

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### LocationARN
- **Type**: <class 'str'>
- **Required**: Yes

### NFSFileShareDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.NFSFileShareDefaultsTypeDef]

### KMSEncrypted
- **Type**: typing.Optional[bool]

### KMSKey
- **Type**: typing.Optional[str]

### DefaultStorageClass
- **Type**: typing.Optional[str]

### ObjectACL
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]

### ClientList
- **Type**: typing.Optional[typing.Sequence[str]]

### Squash
- **Type**: typing.Optional[str]

### ReadOnly
- **Type**: typing.Optional[bool]

### GuessMIMETypeEnabled
- **Type**: typing.Optional[bool]

### RequesterPays
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]

### FileShareName
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.CacheAttributesTypeDef]

### NotificationPolicy
- **Type**: typing.Optional[str]

### VPCEndpointDNSName
- **Type**: typing.Optional[str]

### BucketRegion
- **Type**: typing.Optional[str]

### AuditDestinationARN
- **Type**: typing.Optional[str]


# CreateNFSFileShareOutputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSMBFileShareInputRequestTypeDef

### ClientToken
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### LocationARN
- **Type**: <class 'str'>
- **Required**: Yes

### KMSEncrypted
- **Type**: typing.Optional[bool]

### KMSKey
- **Type**: typing.Optional[str]

### DefaultStorageClass
- **Type**: typing.Optional[str]

### ObjectACL
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]

### ReadOnly
- **Type**: typing.Optional[bool]

### GuessMIMETypeEnabled
- **Type**: typing.Optional[bool]

### RequesterPays
- **Type**: typing.Optional[bool]

### SMBACLEnabled
- **Type**: typing.Optional[bool]

### AccessBasedEnumeration
- **Type**: typing.Optional[bool]

### AdminUserList
- **Type**: typing.Optional[typing.Sequence[str]]

### ValidUserList
- **Type**: typing.Optional[typing.Sequence[str]]

### InvalidUserList
- **Type**: typing.Optional[typing.Sequence[str]]

### AuditDestinationARN
- **Type**: typing.Optional[str]

### Authentication
- **Type**: typing.Optional[str]

### CaseSensitivity
- **Type**: typing.Optional[typing.Literal['CaseSensitive', 'ClientSpecified']]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]

### FileShareName
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.CacheAttributesTypeDef]

### NotificationPolicy
- **Type**: typing.Optional[str]

### VPCEndpointDNSName
- **Type**: typing.Optional[str]

### BucketRegion
- **Type**: typing.Optional[str]

### OplocksEnabled
- **Type**: typing.Optional[bool]


# CreateSMBFileShareOutputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef

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


# CreateSnapshotInputRequestTypeDef

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


# CreateStorediSCSIVolumeInputRequestTypeDef

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


# CreateTapePoolInputRequestTypeDef

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


# CreateTapeWithBarcodeInputRequestTypeDef

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


# CreateTapesInputRequestTypeDef

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


# DeleteAutomaticTapeCreationPolicyInputRequestTypeDef

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


# DeleteBandwidthRateLimitInputRequestTypeDef

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


# DeleteChapCredentialsInputRequestTypeDef

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


# DeleteFileShareInputRequestTypeDef

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


# DeleteGatewayInputRequestTypeDef

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


# DeleteSnapshotScheduleInputRequestTypeDef

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


# DeleteTapeArchiveInputRequestTypeDef

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


# DeleteTapeInputRequestTypeDef

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


# DeleteTapePoolInputRequestTypeDef

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


# DeleteVolumeInputRequestTypeDef

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


# DescribeAvailabilityMonitorTestInputRequestTypeDef

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


# DescribeBandwidthRateLimitInputRequestTypeDef

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


# DescribeBandwidthRateLimitScheduleInputRequestTypeDef

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


# DescribeCacheInputRequestTypeDef

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


# DescribeCachediSCSIVolumesInputRequestTypeDef

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


# DescribeChapCredentialsInputRequestTypeDef

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


# DescribeFileSystemAssociationsInputRequestTypeDef

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


# DescribeGatewayInformationInputRequestTypeDef

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


# DescribeMaintenanceStartTimeInputRequestTypeDef

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


# DescribeNFSFileSharesInputRequestTypeDef

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


# DescribeSMBFileSharesInputRequestTypeDef

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


# DescribeSMBSettingsInputRequestTypeDef

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


# DescribeSnapshotScheduleInputRequestTypeDef

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


# DescribeStorediSCSIVolumesInputRequestTypeDef

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


# DescribeTapeArchivesInputDescribeTapeArchivesPaginateTypeDef

### TapeARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# DescribeTapeArchivesInputRequestTypeDef

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


# DescribeTapeRecoveryPointsInputDescribeTapeRecoveryPointsPaginateTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# DescribeTapeRecoveryPointsInputRequestTypeDef

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


# DescribeTapesInputDescribeTapesPaginateTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# DescribeTapesInputRequestTypeDef

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


# DescribeUploadBufferInputRequestTypeDef

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


# DescribeVTLDevicesInputDescribeVTLDevicesPaginateTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### VTLDeviceARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# DescribeVTLDevicesInputRequestTypeDef

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


# DescribeWorkingStorageInputRequestTypeDef

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


# DetachVolumeInputRequestTypeDef

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


# DisableGatewayInputRequestTypeDef

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


# DisassociateFileSystemInputRequestTypeDef

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


# JoinDomainInputRequestTypeDef

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


# ListAutomaticTapeCreationPoliciesInputRequestTypeDef

### GatewayARN
- **Type**: typing.Optional[str]


# ListAutomaticTapeCreationPoliciesOutputTypeDef

### AutomaticTapeCreationPolicyInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.AutomaticTapeCreationPolicyInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListFileSharesInputListFileSharesPaginateTypeDef

### GatewayARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListFileSharesInputRequestTypeDef

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


# ListFileSystemAssociationsInputListFileSystemAssociationsPaginateTypeDef

### GatewayARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListFileSystemAssociationsInputRequestTypeDef

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


# ListGatewaysInputListGatewaysPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListGatewaysInputRequestTypeDef

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


# ListLocalDisksInputRequestTypeDef

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


# ListTagsForResourceInputListTagsForResourcePaginateTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListTagsForResourceInputRequestTypeDef

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


# ListTapePoolsInputListTapePoolsPaginateTypeDef

### PoolARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListTapePoolsInputRequestTypeDef

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


# ListTapesInputListTapesPaginateTypeDef

### TapeARNs
- **Type**: typing.Optional[typing.Sequence[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListTapesInputRequestTypeDef

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


# ListVolumeInitiatorsInputRequestTypeDef

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


# ListVolumeRecoveryPointsInputRequestTypeDef

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


# ListVolumesInputListVolumesPaginateTypeDef

### GatewayARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.PaginatorConfigTypeDef]


# ListVolumesInputRequestTypeDef

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

### NFSFileShareDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.NFSFileShareDefaultsTypeDef]

### FileShareARN
- **Type**: typing.Optional[str]

### FileShareId
- **Type**: typing.Optional[str]

### FileShareStatus
- **Type**: typing.Optional[str]

### GatewayARN
- **Type**: typing.Optional[str]

### KMSEncrypted
- **Type**: typing.Optional[bool]

### KMSKey
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### LocationARN
- **Type**: typing.Optional[str]

### DefaultStorageClass
- **Type**: typing.Optional[str]

### ObjectACL
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]

### ClientList
- **Type**: typing.Optional[typing.List[str]]

### Squash
- **Type**: typing.Optional[str]

### ReadOnly
- **Type**: typing.Optional[bool]

### GuessMIMETypeEnabled
- **Type**: typing.Optional[bool]

### RequesterPays
- **Type**: typing.Optional[bool]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]

### FileShareName
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.CacheAttributesTypeDef]

### NotificationPolicy
- **Type**: typing.Optional[str]

### VPCEndpointDNSName
- **Type**: typing.Optional[str]

### BucketRegion
- **Type**: typing.Optional[str]

### AuditDestinationARN
- **Type**: typing.Optional[str]


# NetworkInterfaceTypeDef

### Ipv4Address
- **Type**: typing.Optional[str]

### MacAddress
- **Type**: typing.Optional[str]

### Ipv6Address
- **Type**: typing.Optional[str]


# NotifyWhenUploadedInputRequestTypeDef

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


# RefreshCacheInputRequestTypeDef

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


# RemoveTagsFromResourceInputRequestTypeDef

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


# ResetCacheInputRequestTypeDef

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


# RetrieveTapeArchiveInputRequestTypeDef

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


# RetrieveTapeRecoveryPointInputRequestTypeDef

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

### FileShareARN
- **Type**: typing.Optional[str]

### FileShareId
- **Type**: typing.Optional[str]

### FileShareStatus
- **Type**: typing.Optional[str]

### GatewayARN
- **Type**: typing.Optional[str]

### KMSEncrypted
- **Type**: typing.Optional[bool]

### KMSKey
- **Type**: typing.Optional[str]

### Path
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### LocationARN
- **Type**: typing.Optional[str]

### DefaultStorageClass
- **Type**: typing.Optional[str]

### ObjectACL
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]

### ReadOnly
- **Type**: typing.Optional[bool]

### GuessMIMETypeEnabled
- **Type**: typing.Optional[bool]

### RequesterPays
- **Type**: typing.Optional[bool]

### SMBACLEnabled
- **Type**: typing.Optional[bool]

### AccessBasedEnumeration
- **Type**: typing.Optional[bool]

### AdminUserList
- **Type**: typing.Optional[typing.List[str]]

### ValidUserList
- **Type**: typing.Optional[typing.List[str]]

### InvalidUserList
- **Type**: typing.Optional[typing.List[str]]

### AuditDestinationARN
- **Type**: typing.Optional[str]

### Authentication
- **Type**: typing.Optional[str]

### CaseSensitivity
- **Type**: typing.Optional[typing.Literal['CaseSensitive', 'ClientSpecified']]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway_classes.TagTypeDef]]

### FileShareName
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.CacheAttributesTypeDef]

### NotificationPolicy
- **Type**: typing.Optional[str]

### VPCEndpointDNSName
- **Type**: typing.Optional[str]

### BucketRegion
- **Type**: typing.Optional[str]

### OplocksEnabled
- **Type**: typing.Optional[bool]


# SMBLocalGroupsOutputTypeDef

### GatewayAdmins
- **Type**: typing.Optional[typing.List[str]]


# SMBLocalGroupsTypeDef

### GatewayAdmins
- **Type**: typing.Optional[typing.Sequence[str]]


# SetLocalConsolePasswordInputRequestTypeDef

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


# SetSMBGuestPasswordInputRequestTypeDef

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


# ShutdownGatewayInputRequestTypeDef

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


# StartAvailabilityMonitorTestInputRequestTypeDef

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


# StartGatewayInputRequestTypeDef

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


# UpdateAutomaticTapeCreationPolicyInputRequestTypeDef

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


# UpdateBandwidthRateLimitInputRequestTypeDef

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


# UpdateBandwidthRateLimitScheduleInputRequestTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### BandwidthRateLimitIntervals
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.storagegateway_classes.BandwidthRateLimitIntervalTypeDef, aws_resource_validator.pydantic_models.storagegateway_classes.BandwidthRateLimitIntervalOutputTypeDef]]
- **Required**: Yes


# UpdateBandwidthRateLimitScheduleOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChapCredentialsInputRequestTypeDef

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


# UpdateFileSystemAssociationInputRequestTypeDef

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


# UpdateGatewayInformationInputRequestTypeDef

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


# UpdateGatewaySoftwareNowInputRequestTypeDef

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


# UpdateMaintenanceStartTimeInputRequestTypeDef

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


# UpdateNFSFileShareInputRequestTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### KMSEncrypted
- **Type**: typing.Optional[bool]

### KMSKey
- **Type**: typing.Optional[str]

### NFSFileShareDefaults
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.NFSFileShareDefaultsTypeDef]

### DefaultStorageClass
- **Type**: typing.Optional[str]

### ObjectACL
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]

### ClientList
- **Type**: typing.Optional[typing.Sequence[str]]

### Squash
- **Type**: typing.Optional[str]

### ReadOnly
- **Type**: typing.Optional[bool]

### GuessMIMETypeEnabled
- **Type**: typing.Optional[bool]

### RequesterPays
- **Type**: typing.Optional[bool]

### FileShareName
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.CacheAttributesTypeDef]

### NotificationPolicy
- **Type**: typing.Optional[str]

### AuditDestinationARN
- **Type**: typing.Optional[str]


# UpdateNFSFileShareOutputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSMBFileShareInputRequestTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### KMSEncrypted
- **Type**: typing.Optional[bool]

### KMSKey
- **Type**: typing.Optional[str]

### DefaultStorageClass
- **Type**: typing.Optional[str]

### ObjectACL
- **Type**: typing.Optional[typing.Literal['authenticated-read', 'aws-exec-read', 'bucket-owner-full-control', 'bucket-owner-read', 'private', 'public-read', 'public-read-write']]

### ReadOnly
- **Type**: typing.Optional[bool]

### GuessMIMETypeEnabled
- **Type**: typing.Optional[bool]

### RequesterPays
- **Type**: typing.Optional[bool]

### SMBACLEnabled
- **Type**: typing.Optional[bool]

### AccessBasedEnumeration
- **Type**: typing.Optional[bool]

### AdminUserList
- **Type**: typing.Optional[typing.Sequence[str]]

### ValidUserList
- **Type**: typing.Optional[typing.Sequence[str]]

### InvalidUserList
- **Type**: typing.Optional[typing.Sequence[str]]

### AuditDestinationARN
- **Type**: typing.Optional[str]

### CaseSensitivity
- **Type**: typing.Optional[typing.Literal['CaseSensitive', 'ClientSpecified']]

### FileShareName
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway_classes.CacheAttributesTypeDef]

### NotificationPolicy
- **Type**: typing.Optional[str]

### OplocksEnabled
- **Type**: typing.Optional[bool]


# UpdateSMBFileShareOutputTypeDef

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSMBFileShareVisibilityInputRequestTypeDef

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


# UpdateSMBLocalGroupsInputRequestTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### SMBLocalGroups
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.SMBLocalGroupsTypeDef'>
- **Required**: Yes


# UpdateSMBLocalGroupsOutputTypeDef

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateSMBSecurityStrategyInputRequestTypeDef

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


# UpdateSnapshotScheduleInputRequestTypeDef

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


# UpdateVTLDeviceTypeInputRequestTypeDef

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


