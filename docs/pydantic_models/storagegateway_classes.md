# Storagegateway Classes

# ActivateGatewayInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]


# ActivateGatewayOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# AddCacheInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### DiskIds
- **Type**: typing.List[str]
- **Required**: Yes


# AddCacheOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# AddTagsToResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]
- **Required**: Yes


# AddTagsToResourceOutput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# AddUploadBufferInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### DiskIds
- **Type**: typing.List[str]
- **Required**: Yes


# AddUploadBufferOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# AddWorkingStorageInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### DiskIds
- **Type**: typing.List[str]
- **Required**: Yes


# AddWorkingStorageOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# AssignTapePoolInput

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### PoolId
- **Type**: <class 'str'>
- **Required**: Yes

### BypassGovernanceRetention
- **Type**: typing.Optional[bool]


# AssignTapePoolOutput

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# AssociateFileSystemInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]

### AuditDestinationARN
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: <class 'NoneType'>

### EndpointNetworkConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.EndpointNetworkConfiguration, aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.EndpointNetworkConfigurationOutput, NoneType]


# AssociateFileSystemOutput

### FileSystemAssociationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# AttachVolumeInput

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


# AttachVolumeOutput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# AutomaticTapeCreationPolicyInfo

### AutomaticTapeCreationRules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.AutomaticTapeCreationRule]]

### GatewayARN
- **Type**: typing.Optional[str]


# AutomaticTapeCreationRule

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


# BandwidthRateLimitInterval

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


# BandwidthRateLimitIntervalOutput

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


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CacheAttributes

### CacheStaleTimeoutInSeconds
- **Type**: typing.Optional[int]


# CacheReportFilter

### Name
- **Type**: typing.Literal['UploadFailureReason', 'UploadState']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# CacheReportFilterOutput

### Name
- **Type**: typing.Literal['UploadFailureReason', 'UploadState']
- **Required**: Yes

### Values
- **Type**: typing.List[str]
- **Required**: Yes


# CacheReportInfo

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.CacheReportFilterOutput]]

### ExclusionFilters
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.CacheReportFilterOutput]]

### ReportName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]


# CachediSCSIVolume

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
- **Type**: <class 'NoneType'>

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### VolumeUsedInBytes
- **Type**: typing.Optional[int]

### KMSKey
- **Type**: typing.Optional[str]

### TargetName
- **Type**: typing.Optional[str]


# CancelArchivalInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes


# CancelArchivalOutput

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# CancelCacheReportInput

### CacheReportARN
- **Type**: <class 'str'>
- **Required**: Yes


# CancelCacheReportOutput

### CacheReportARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# CancelRetrievalInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes


# CancelRetrievalOutput

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ChapInfo

### TargetARN
- **Type**: typing.Optional[str]

### SecretToAuthenticateInitiator
- **Type**: typing.Optional[str]

### InitiatorName
- **Type**: typing.Optional[str]

### SecretToAuthenticateTarget
- **Type**: typing.Optional[str]


# CreateCachediSCSIVolumeInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]


# CreateCachediSCSIVolumeOutput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# CreateNFSFileShareInput

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
- **Type**: <class 'NoneType'>

### EncryptionType
- **Type**: typing.Optional[typing.Literal['DsseKms', 'SseKms', 'SseS3']]

### KMSEncrypted
- **Type**: typing.Optional[bool]

### KMSKey
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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]

### FileShareName
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: <class 'NoneType'>

### NotificationPolicy
- **Type**: typing.Optional[str]

### VPCEndpointDNSName
- **Type**: typing.Optional[str]

### BucketRegion
- **Type**: typing.Optional[str]

### AuditDestinationARN
- **Type**: typing.Optional[str]


# CreateNFSFileShareOutput

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSMBFileShareInput

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

### EncryptionType
- **Type**: typing.Optional[typing.Literal['DsseKms', 'SseKms', 'SseS3']]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]

### FileShareName
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: <class 'NoneType'>

### NotificationPolicy
- **Type**: typing.Optional[str]

### VPCEndpointDNSName
- **Type**: typing.Optional[str]

### BucketRegion
- **Type**: typing.Optional[str]

### OplocksEnabled
- **Type**: typing.Optional[bool]


# CreateSMBFileShareOutput

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSnapshotFromVolumeRecoveryPointInput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]


# CreateSnapshotFromVolumeRecoveryPointOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSnapshotInput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotDescription
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]


# CreateSnapshotOutput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### SnapshotId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStorediSCSIVolumeInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]


# CreateStorediSCSIVolumeOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTapePoolInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]


# CreateTapePoolOutput

### PoolARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTapeWithBarcodeInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]


# CreateTapeWithBarcodeOutput

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# CreateTapesInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]


# CreateTapesOutput

### TapeARNs
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteAutomaticTapeCreationPolicyInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteAutomaticTapeCreationPolicyOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteBandwidthRateLimitInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### BandwidthType
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteBandwidthRateLimitOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteCacheReportInput

### CacheReportARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteCacheReportOutput

### CacheReportARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteChapCredentialsInput

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### InitiatorName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChapCredentialsOutput

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### InitiatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteFileShareInput

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDelete
- **Type**: typing.Optional[bool]


# DeleteFileShareOutput

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteGatewayInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteGatewayOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteSnapshotScheduleInput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSnapshotScheduleOutput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTapeArchiveInput

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### BypassGovernanceRetention
- **Type**: typing.Optional[bool]


# DeleteTapeArchiveOutput

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTapeInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### BypassGovernanceRetention
- **Type**: typing.Optional[bool]


# DeleteTapeOutput

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteTapePoolInput

### PoolARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteTapePoolOutput

### PoolARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteVolumeInput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVolumeOutput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeAvailabilityMonitorTestInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAvailabilityMonitorTestOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBandwidthRateLimitInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBandwidthRateLimitOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeBandwidthRateLimitScheduleInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeBandwidthRateLimitScheduleOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### BandwidthRateLimitIntervals
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.BandwidthRateLimitIntervalOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCacheInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCacheOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCacheReportInput

### CacheReportARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeCacheReportOutput

### CacheReportInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.CacheReportInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeCachediSCSIVolumesInput

### VolumeARNs
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeCachediSCSIVolumesOutput

### CachediSCSIVolumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.CachediSCSIVolume]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeChapCredentialsInput

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChapCredentialsOutput

### ChapCredentials
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ChapInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeFileSystemAssociationsInput

### FileSystemAssociationARNList
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeFileSystemAssociationsOutput

### FileSystemAssociationInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.FileSystemAssociationInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeGatewayInformationInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeGatewayInformationOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.NetworkInterface]
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMaintenanceStartTimeInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeMaintenanceStartTimeOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.SoftwareUpdatePreferences'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeNFSFileSharesInput

### FileShareARNList
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeNFSFileSharesOutput

### NFSFileShareInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.NFSFileShareInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSMBFileSharesInput

### FileShareARNList
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeSMBFileSharesOutput

### SMBFileShareInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.SMBFileShareInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSMBSettingsInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSMBSettingsOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.SMBLocalGroupsOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSnapshotScheduleInput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSnapshotScheduleOutput

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStorediSCSIVolumesInput

### VolumeARNs
- **Type**: typing.List[str]
- **Required**: Yes


# DescribeStorediSCSIVolumesOutput

### StorediSCSIVolumes
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.StorediSCSIVolume]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTapeArchivesInput

### TapeARNs
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeTapeArchivesInputPaginate

### TapeARNs
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.PaginatorConfig]


# DescribeTapeArchivesOutput

### TapeArchives
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.TapeArchive]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTapeRecoveryPointsInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeTapeRecoveryPointsInputPaginate

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.PaginatorConfig]


# DescribeTapeRecoveryPointsOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeRecoveryPointInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.TapeRecoveryPointInfo]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeTapesInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeARNs
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeTapesInputPaginate

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### TapeARNs
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.PaginatorConfig]


# DescribeTapesOutput

### Tapes
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tape]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeUploadBufferInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeUploadBufferOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVTLDevicesInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### VTLDeviceARNs
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# DescribeVTLDevicesInputPaginate

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### VTLDeviceARNs
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.PaginatorConfig]


# DescribeVTLDevicesOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### VTLDevices
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.VTLDevice]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeWorkingStorageInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeWorkingStorageOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DetachVolumeInput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDetach
- **Type**: typing.Optional[bool]


# DetachVolumeOutput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DeviceiSCSIAttributes

### TargetARN
- **Type**: typing.Optional[str]

### NetworkInterfaceId
- **Type**: typing.Optional[str]

### NetworkInterfacePort
- **Type**: typing.Optional[int]

### ChapEnabled
- **Type**: typing.Optional[bool]


# DisableGatewayInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# DisableGatewayOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# DisassociateFileSystemInput

### FileSystemAssociationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ForceDelete
- **Type**: typing.Optional[bool]


# DisassociateFileSystemOutput

### FileSystemAssociationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# Disk

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


# EndpointNetworkConfiguration

### IpAddresses
- **Type**: typing.Optional[typing.List[str]]


# EndpointNetworkConfigurationOutput

### IpAddresses
- **Type**: typing.Optional[typing.List[str]]


# EvictFilesFailingUploadInput

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ForceRemove
- **Type**: typing.Optional[bool]


# EvictFilesFailingUploadOutput

### NotificationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# FileShareInfo

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


# FileSystemAssociationInfo

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]

### CacheAttributes
- **Type**: <class 'NoneType'>

### EndpointNetworkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.EndpointNetworkConfigurationOutput]

### FileSystemAssociationStatusDetails
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.FileSystemAssociationStatusDetail]]


# FileSystemAssociationStatusDetail

### ErrorCode
- **Type**: typing.Optional[str]


# FileSystemAssociationSummary

### FileSystemAssociationId
- **Type**: typing.Optional[str]

### FileSystemAssociationARN
- **Type**: typing.Optional[str]

### FileSystemAssociationStatus
- **Type**: typing.Optional[str]

### GatewayARN
- **Type**: typing.Optional[str]


# GatewayInfo

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


# JoinDomainInput

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
- **Type**: typing.Optional[typing.List[str]]

### TimeoutInSeconds
- **Type**: typing.Optional[int]


# JoinDomainOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ActiveDirectoryStatus
- **Type**: typing.Literal['ACCESS_DENIED', 'DETACHED', 'JOINED', 'JOINING', 'NETWORK_ERROR', 'TIMEOUT', 'UNKNOWN_ERROR']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListAutomaticTapeCreationPoliciesInput

### GatewayARN
- **Type**: typing.Optional[str]


# ListAutomaticTapeCreationPoliciesOutput

### AutomaticTapeCreationPolicyInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.AutomaticTapeCreationPolicyInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListCacheReportsInput

### Marker
- **Type**: typing.Optional[str]


# ListCacheReportsOutput

### CacheReportList
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.CacheReportInfo]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListFileSharesInput

### GatewayARN
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListFileSharesInputPaginate

### GatewayARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.PaginatorConfig]


# ListFileSharesOutput

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### FileShareInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.FileShareInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListFileSystemAssociationsInput

### GatewayARN
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]

### Marker
- **Type**: typing.Optional[str]


# ListFileSystemAssociationsInputPaginate

### GatewayARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.PaginatorConfig]


# ListFileSystemAssociationsOutput

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### NextMarker
- **Type**: <class 'str'>
- **Required**: Yes

### FileSystemAssociationSummaryList
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.FileSystemAssociationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListGatewaysInput

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListGatewaysInputPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.PaginatorConfig]


# ListGatewaysOutput

### Gateways
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.GatewayInfo]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListLocalDisksInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListLocalDisksOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### Disks
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Disk]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListTagsForResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTagsForResourceInputPaginate

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.PaginatorConfig]


# ListTagsForResourceOutput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListTapePoolsInput

### PoolARNs
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTapePoolsInputPaginate

### PoolARNs
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.PaginatorConfig]


# ListTapePoolsOutput

### PoolInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.PoolInfo]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListTapesInput

### TapeARNs
- **Type**: typing.Optional[typing.List[str]]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListTapesInputPaginate

### TapeARNs
- **Type**: typing.Optional[typing.List[str]]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.PaginatorConfig]


# ListTapesOutput

### TapeInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.TapeInfo]
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListVolumeInitiatorsInput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListVolumeInitiatorsOutput

### Initiators
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListVolumeRecoveryPointsInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListVolumeRecoveryPointsOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeRecoveryPointInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.VolumeRecoveryPointInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ListVolumesInput

### GatewayARN
- **Type**: typing.Optional[str]

### Marker
- **Type**: typing.Optional[str]

### Limit
- **Type**: typing.Optional[int]


# ListVolumesInputPaginate

### GatewayARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.PaginatorConfig]


# ListVolumesOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### Marker
- **Type**: <class 'str'>
- **Required**: Yes

### VolumeInfos
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.VolumeInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# NFSFileShareDefaults

### FileMode
- **Type**: typing.Optional[str]

### DirectoryMode
- **Type**: typing.Optional[str]

### GroupId
- **Type**: typing.Optional[int]

### OwnerId
- **Type**: typing.Optional[int]


# NFSFileShareInfo

### NFSFileShareDefaults
- **Type**: <class 'NoneType'>

### FileShareARN
- **Type**: typing.Optional[str]

### FileShareId
- **Type**: typing.Optional[str]

### FileShareStatus
- **Type**: typing.Optional[str]

### GatewayARN
- **Type**: typing.Optional[str]

### EncryptionType
- **Type**: typing.Optional[typing.Literal['DsseKms', 'SseKms', 'SseS3']]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]

### FileShareName
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: <class 'NoneType'>

### NotificationPolicy
- **Type**: typing.Optional[str]

### VPCEndpointDNSName
- **Type**: typing.Optional[str]

### BucketRegion
- **Type**: typing.Optional[str]

### AuditDestinationARN
- **Type**: typing.Optional[str]


# NetworkInterface

### Ipv4Address
- **Type**: typing.Optional[str]

### MacAddress
- **Type**: typing.Optional[str]

### Ipv6Address
- **Type**: typing.Optional[str]


# NotifyWhenUploadedInput

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes


# NotifyWhenUploadedOutput

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PoolInfo

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


# RefreshCacheInput

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### FolderList
- **Type**: typing.Optional[typing.List[str]]

### Recursive
- **Type**: typing.Optional[bool]


# RefreshCacheOutput

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### NotificationId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# RemoveTagsFromResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# RemoveTagsFromResourceOutput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ResetCacheInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# ResetCacheOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
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


# RetrieveTapeArchiveInput

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveTapeArchiveOutput

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# RetrieveTapeRecoveryPointInput

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# RetrieveTapeRecoveryPointOutput

### TapeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# SMBFileShareInfo

### FileShareARN
- **Type**: typing.Optional[str]

### FileShareId
- **Type**: typing.Optional[str]

### FileShareStatus
- **Type**: typing.Optional[str]

### GatewayARN
- **Type**: typing.Optional[str]

### EncryptionType
- **Type**: typing.Optional[typing.Literal['DsseKms', 'SseKms', 'SseS3']]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]

### FileShareName
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: <class 'NoneType'>

### NotificationPolicy
- **Type**: typing.Optional[str]

### VPCEndpointDNSName
- **Type**: typing.Optional[str]

### BucketRegion
- **Type**: typing.Optional[str]

### OplocksEnabled
- **Type**: typing.Optional[bool]


# SMBLocalGroups

### GatewayAdmins
- **Type**: typing.Optional[typing.List[str]]


# SMBLocalGroupsOutput

### GatewayAdmins
- **Type**: typing.Optional[typing.List[str]]


# SetLocalConsolePasswordInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### LocalConsolePassword
- **Type**: <class 'str'>
- **Required**: Yes


# SetLocalConsolePasswordOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# SetSMBGuestPasswordInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### Password
- **Type**: <class 'str'>
- **Required**: Yes


# SetSMBGuestPasswordOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# ShutdownGatewayInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# ShutdownGatewayOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# SoftwareUpdatePreferences

### AutomaticUpdatePolicy
- **Type**: typing.Optional[typing.Literal['ALL_VERSIONS', 'EMERGENCY_VERSIONS_ONLY']]


# StartAvailabilityMonitorTestInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# StartAvailabilityMonitorTestOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# StartCacheReportInput

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
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.CacheReportFilter, aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.CacheReportFilterOutput]]]

### ExclusionFilters
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.CacheReportFilter, aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.CacheReportFilterOutput]]]

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]


# StartCacheReportOutput

### CacheReportARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# StartGatewayInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# StartGatewayOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# StorediSCSIVolume

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
- **Type**: <class 'NoneType'>

### CreatedDate
- **Type**: typing.Optional[datetime.datetime]

### VolumeUsedInBytes
- **Type**: typing.Optional[int]

### KMSKey
- **Type**: typing.Optional[str]

### TargetName
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# Tape

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


# TapeArchive

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


# TapeInfo

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


# TapeRecoveryPointInfo

### TapeARN
- **Type**: typing.Optional[str]

### TapeRecoveryPointTime
- **Type**: typing.Optional[datetime.datetime]

### TapeSizeInBytes
- **Type**: typing.Optional[int]

### TapeStatus
- **Type**: typing.Optional[str]


# UpdateAutomaticTapeCreationPolicyInput

### AutomaticTapeCreationRules
- **Type**: typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.AutomaticTapeCreationRule]
- **Required**: Yes

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateAutomaticTapeCreationPolicyOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBandwidthRateLimitInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### AverageUploadRateLimitInBitsPerSec
- **Type**: typing.Optional[int]

### AverageDownloadRateLimitInBitsPerSec
- **Type**: typing.Optional[int]


# UpdateBandwidthRateLimitOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateBandwidthRateLimitScheduleInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### BandwidthRateLimitIntervals
- **Type**: typing.List[typing.Union[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.BandwidthRateLimitInterval, aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.BandwidthRateLimitIntervalOutput]]
- **Required**: Yes


# UpdateBandwidthRateLimitScheduleOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateChapCredentialsInput

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


# UpdateChapCredentialsOutput

### TargetARN
- **Type**: <class 'str'>
- **Required**: Yes

### InitiatorName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateFileSystemAssociationInput

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
- **Type**: <class 'NoneType'>


# UpdateFileSystemAssociationOutput

### FileSystemAssociationARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGatewayInformationInput

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


# UpdateGatewayInformationOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### GatewayName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateGatewaySoftwareNowInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateGatewaySoftwareNowOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMaintenanceStartTimeInput

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
- **Type**: <class 'NoneType'>


# UpdateMaintenanceStartTimeOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateNFSFileShareInput

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionType
- **Type**: typing.Optional[typing.Literal['DsseKms', 'SseKms', 'SseS3']]

### KMSEncrypted
- **Type**: typing.Optional[bool]

### KMSKey
- **Type**: typing.Optional[str]

### NFSFileShareDefaults
- **Type**: <class 'NoneType'>

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

### FileShareName
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: <class 'NoneType'>

### NotificationPolicy
- **Type**: typing.Optional[str]

### AuditDestinationARN
- **Type**: typing.Optional[str]


# UpdateNFSFileShareOutput

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSMBFileShareInput

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionType
- **Type**: typing.Optional[typing.Literal['DsseKms', 'SseKms', 'SseS3']]

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
- **Type**: typing.Optional[typing.List[str]]

### ValidUserList
- **Type**: typing.Optional[typing.List[str]]

### InvalidUserList
- **Type**: typing.Optional[typing.List[str]]

### AuditDestinationARN
- **Type**: typing.Optional[str]

### CaseSensitivity
- **Type**: typing.Optional[typing.Literal['CaseSensitive', 'ClientSpecified']]

### FileShareName
- **Type**: typing.Optional[str]

### CacheAttributes
- **Type**: <class 'NoneType'>

### NotificationPolicy
- **Type**: typing.Optional[str]

### OplocksEnabled
- **Type**: typing.Optional[bool]


# UpdateSMBFileShareOutput

### FileShareARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSMBFileShareVisibilityInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### FileSharesVisible
- **Type**: <class 'bool'>
- **Required**: Yes


# UpdateSMBFileShareVisibilityOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSMBLocalGroupsInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### SMBLocalGroups
- **Type**: typing.Union[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.SMBLocalGroups, aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.SMBLocalGroupsOutput]
- **Required**: Yes


# UpdateSMBLocalGroupsOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSMBSecurityStrategyInput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### SMBSecurityStrategy
- **Type**: typing.Literal['ClientSpecified', 'MandatoryEncryption', 'MandatoryEncryptionNoAes128', 'MandatorySigning']
- **Required**: Yes


# UpdateSMBSecurityStrategyOutput

### GatewayARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateSnapshotScheduleInput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.Tag]]


# UpdateSnapshotScheduleOutput

### VolumeARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVTLDeviceTypeInput

### VTLDeviceARN
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceType
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateVTLDeviceTypeOutput

### VTLDeviceARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.storagegateway.storagegateway_classes.ResponseMetadata'>
- **Required**: Yes


# VTLDevice

### VTLDeviceARN
- **Type**: typing.Optional[str]

### VTLDeviceType
- **Type**: typing.Optional[str]

### VTLDeviceVendor
- **Type**: typing.Optional[str]

### VTLDeviceProductIdentifier
- **Type**: typing.Optional[str]

### DeviceiSCSIAttributes
- **Type**: <class 'NoneType'>


# VolumeInfo

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


# VolumeRecoveryPointInfo

### VolumeARN
- **Type**: typing.Optional[str]

### VolumeSizeInBytes
- **Type**: typing.Optional[int]

### VolumeUsageInBytes
- **Type**: typing.Optional[int]

### VolumeRecoveryPointTime
- **Type**: typing.Optional[str]


# VolumeiSCSIAttributes

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


