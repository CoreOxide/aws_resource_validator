# Elastictranscoder Classes

# ArtworkTypeDef

### InputKey
- **Type**: typing.Optional[str]

### MaxWidth
- **Type**: typing.Optional[str]

### MaxHeight
- **Type**: typing.Optional[str]

### SizingPolicy
- **Type**: typing.Optional[str]

### PaddingPolicy
- **Type**: typing.Optional[str]

### AlbumArtFormat
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.EncryptionTypeDef]


# AudioCodecOptionsTypeDef

### Profile
- **Type**: typing.Optional[str]

### BitDepth
- **Type**: typing.Optional[str]

### BitOrder
- **Type**: typing.Optional[str]

### Signed
- **Type**: typing.Optional[str]


# AudioParametersTypeDef

### Codec
- **Type**: typing.Optional[str]

### SampleRate
- **Type**: typing.Optional[str]

### BitRate
- **Type**: typing.Optional[str]

### Channels
- **Type**: typing.Optional[str]

### AudioPackingMode
- **Type**: typing.Optional[str]

### CodecOptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.AudioCodecOptionsTypeDef]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJobRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# CaptionFormatTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CaptionSourceTypeDef

### Key
- **Type**: typing.Optional[str]

### Language
- **Type**: typing.Optional[str]

### TimeOffset
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.EncryptionTypeDef]


# CaptionsOutputTypeDef

### MergePolicy
- **Type**: typing.Optional[str]

### CaptionSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.CaptionSourceTypeDef]]

### CaptionFormats
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.CaptionFormatTypeDef]]


# CaptionsTypeDef

### MergePolicy
- **Type**: typing.Optional[str]

### CaptionSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elastictranscoder_classes.CaptionSourceTypeDef]]

### CaptionFormats
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elastictranscoder_classes.CaptionFormatTypeDef]]


# CaptionsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClipTypeDef

### TimeSpan
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.TimeSpanTypeDef]


# CreateJobOutputTypeDef

### Key
- **Type**: typing.Optional[str]

### ThumbnailPattern
- **Type**: typing.Optional[str]

### ThumbnailEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.EncryptionTypeDef]

### Rotate
- **Type**: typing.Optional[str]

### PresetId
- **Type**: typing.Optional[str]

### SegmentDuration
- **Type**: typing.Optional[str]

### Watermarks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elastictranscoder_classes.JobWatermarkTypeDef]]

### AlbumArt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.JobAlbumArtUnionTypeDef]

### Composition
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elastictranscoder_classes.ClipTypeDef]]

### Captions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.CaptionsUnionTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.EncryptionTypeDef]


# CreateJobPlaylistTypeDef

### Name
- **Type**: typing.Optional[str]

### Format
- **Type**: typing.Optional[str]

### OutputKeys
- **Type**: typing.Optional[typing.Sequence[str]]

### HlsContentProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.HlsContentProtectionTypeDef]

### PlayReadyDrm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.PlayReadyDrmTypeDef]


# CreateJobRequestTypeDef

### PipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.JobInputUnionTypeDef]

### Inputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elastictranscoder_classes.JobInputUnionTypeDef]]

### Output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.CreateJobOutputTypeDef]

### Outputs
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elastictranscoder_classes.CreateJobOutputTypeDef]]

### OutputKeyPrefix
- **Type**: typing.Optional[str]

### Playlists
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elastictranscoder_classes.CreateJobPlaylistTypeDef]]

### UserMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateJobResponseTypeDef

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePipelineRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### InputBucket
- **Type**: <class 'str'>
- **Required**: Yes

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### OutputBucket
- **Type**: typing.Optional[str]

### AwsKmsKeyArn
- **Type**: typing.Optional[str]

### Notifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.NotificationsTypeDef]

### ContentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.PipelineOutputConfigUnionTypeDef]

### ThumbnailConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.PipelineOutputConfigUnionTypeDef]


# CreatePipelineResponseTypeDef

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.PipelineTypeDef'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.WarningTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeletePipelineRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePresetRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DetectedPropertiesTypeDef

### Width
- **Type**: typing.Optional[int]

### Height
- **Type**: typing.Optional[int]

### FrameRate
- **Type**: typing.Optional[str]

### FileSize
- **Type**: typing.Optional[int]

### DurationMillis
- **Type**: typing.Optional[int]


# EncryptionTypeDef

### Mode
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### KeyMd5
- **Type**: typing.Optional[str]

### InitializationVector
- **Type**: typing.Optional[str]


# HlsContentProtectionTypeDef

### Method
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### KeyMd5
- **Type**: typing.Optional[str]

### InitializationVector
- **Type**: typing.Optional[str]

### LicenseAcquisitionUrl
- **Type**: typing.Optional[str]

### KeyStoragePolicy
- **Type**: typing.Optional[str]


# InputCaptionsOutputTypeDef

### MergePolicy
- **Type**: typing.Optional[str]

### CaptionSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.CaptionSourceTypeDef]]


# InputCaptionsTypeDef

### MergePolicy
- **Type**: typing.Optional[str]

### CaptionSources
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elastictranscoder_classes.CaptionSourceTypeDef]]


# JobAlbumArtOutputTypeDef

### MergePolicy
- **Type**: typing.Optional[str]

### Artwork
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.ArtworkTypeDef]]


# JobAlbumArtTypeDef

### MergePolicy
- **Type**: typing.Optional[str]

### Artwork
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elastictranscoder_classes.ArtworkTypeDef]]


# JobAlbumArtUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobInputOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobInputUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# JobOutputTypeDef

### Id
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### ThumbnailPattern
- **Type**: typing.Optional[str]

### ThumbnailEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.EncryptionTypeDef]

### Rotate
- **Type**: typing.Optional[str]

### PresetId
- **Type**: typing.Optional[str]

### SegmentDuration
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### StatusDetail
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[int]

### Width
- **Type**: typing.Optional[int]

### Height
- **Type**: typing.Optional[int]

### FrameRate
- **Type**: typing.Optional[str]

### FileSize
- **Type**: typing.Optional[int]

### DurationMillis
- **Type**: typing.Optional[int]

### Watermarks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.JobWatermarkTypeDef]]

### AlbumArt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.JobAlbumArtOutputTypeDef]

### Composition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.ClipTypeDef]]

### Captions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.CaptionsOutputTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.EncryptionTypeDef]

### AppliedColorSpaceConversion
- **Type**: typing.Optional[str]


# JobTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### PipelineId
- **Type**: typing.Optional[str]

### Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.JobInputOutputTypeDef]

### Inputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.JobInputOutputTypeDef]]

### Output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.JobOutputTypeDef]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.JobOutputTypeDef]]

### OutputKeyPrefix
- **Type**: typing.Optional[str]

### Playlists
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.PlaylistTypeDef]]

### Status
- **Type**: typing.Optional[str]

### UserMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### Timing
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.TimingTypeDef]


# JobWatermarkTypeDef

### PresetWatermarkId
- **Type**: typing.Optional[str]

### InputKey
- **Type**: typing.Optional[str]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.EncryptionTypeDef]


# ListJobsByPipelineRequestPaginateTypeDef

### PipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### Ascending
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.PaginatorConfigTypeDef]


# ListJobsByPipelineRequestTypeDef

### PipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### Ascending
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]


# ListJobsByPipelineResponseTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.JobTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListJobsByStatusRequestPaginateTypeDef

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Ascending
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.PaginatorConfigTypeDef]


# ListJobsByStatusRequestTypeDef

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Ascending
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]


# ListJobsByStatusResponseTypeDef

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.JobTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPipelinesRequestPaginateTypeDef

### Ascending
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.PaginatorConfigTypeDef]


# ListPipelinesRequestTypeDef

### Ascending
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]


# ListPipelinesResponseTypeDef

### Pipelines
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.PipelineTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPresetsRequestPaginateTypeDef

### Ascending
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.PaginatorConfigTypeDef]


# ListPresetsRequestTypeDef

### Ascending
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]


# ListPresetsResponseTypeDef

### Presets
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.PresetTypeDef]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# NotificationsTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PermissionOutputTypeDef

### GranteeType
- **Type**: typing.Optional[str]

### Grantee
- **Type**: typing.Optional[str]

### Access
- **Type**: typing.Optional[typing.List[str]]


# PermissionTypeDef

### GranteeType
- **Type**: typing.Optional[str]

### Grantee
- **Type**: typing.Optional[str]

### Access
- **Type**: typing.Optional[typing.Sequence[str]]


# PipelineOutputConfigOutputTypeDef

### Bucket
- **Type**: typing.Optional[str]

### StorageClass
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.PermissionOutputTypeDef]]


# PipelineOutputConfigTypeDef

### Bucket
- **Type**: typing.Optional[str]

### StorageClass
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elastictranscoder_classes.PermissionTypeDef]]


# PipelineOutputConfigUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PipelineTypeDef

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### InputBucket
- **Type**: typing.Optional[str]

### OutputBucket
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### AwsKmsKeyArn
- **Type**: typing.Optional[str]

### Notifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.NotificationsTypeDef]

### ContentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.PipelineOutputConfigOutputTypeDef]

### ThumbnailConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.PipelineOutputConfigOutputTypeDef]


# PlayReadyDrmTypeDef

### Format
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### KeyMd5
- **Type**: typing.Optional[str]

### KeyId
- **Type**: typing.Optional[str]

### InitializationVector
- **Type**: typing.Optional[str]

### LicenseAcquisitionUrl
- **Type**: typing.Optional[str]


# PlaylistTypeDef

### Name
- **Type**: typing.Optional[str]

### Format
- **Type**: typing.Optional[str]

### OutputKeys
- **Type**: typing.Optional[typing.List[str]]

### HlsContentProtection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.HlsContentProtectionTypeDef]

### PlayReadyDrm
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.PlayReadyDrmTypeDef]

### Status
- **Type**: typing.Optional[str]

### StatusDetail
- **Type**: typing.Optional[str]


# PresetTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PresetWatermarkTypeDef

### Id
- **Type**: typing.Optional[str]

### MaxWidth
- **Type**: typing.Optional[str]

### MaxHeight
- **Type**: typing.Optional[str]

### SizingPolicy
- **Type**: typing.Optional[str]

### HorizontalAlign
- **Type**: typing.Optional[str]

### HorizontalOffset
- **Type**: typing.Optional[str]

### VerticalAlign
- **Type**: typing.Optional[str]

### VerticalOffset
- **Type**: typing.Optional[str]

### Opacity
- **Type**: typing.Optional[str]

### Target
- **Type**: typing.Optional[str]


# ReadJobRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# ReadJobRequestWaitTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.WaiterConfigTypeDef]


# ReadJobResponseTypeDef

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.JobTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReadPipelineRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# ReadPipelineResponseTypeDef

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.PipelineTypeDef'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.WarningTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ReadPresetRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# ReadPresetResponseTypeDef

### Preset
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.PresetTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.ResponseMetadataTypeDef'>
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


# TestRoleRequestTypeDef

### Role
- **Type**: <class 'str'>
- **Required**: Yes

### InputBucket
- **Type**: <class 'str'>
- **Required**: Yes

### OutputBucket
- **Type**: <class 'str'>
- **Required**: Yes

### Topics
- **Type**: typing.Sequence[str]
- **Required**: Yes


# TestRoleResponseTypeDef

### Success
- **Type**: <class 'str'>
- **Required**: Yes

### Messages
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ThumbnailsTypeDef

### Format
- **Type**: typing.Optional[str]

### Interval
- **Type**: typing.Optional[str]

### Resolution
- **Type**: typing.Optional[str]

### AspectRatio
- **Type**: typing.Optional[str]

### MaxWidth
- **Type**: typing.Optional[str]

### MaxHeight
- **Type**: typing.Optional[str]

### SizingPolicy
- **Type**: typing.Optional[str]

### PaddingPolicy
- **Type**: typing.Optional[str]


# TimeSpanTypeDef

### StartTime
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]


# TimingTypeDef

### SubmitTimeMillis
- **Type**: typing.Optional[int]

### StartTimeMillis
- **Type**: typing.Optional[int]

### FinishTimeMillis
- **Type**: typing.Optional[int]


# UpdatePipelineNotificationsRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Notifications
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.NotificationsTypeDef'>
- **Required**: Yes


# UpdatePipelineNotificationsResponseTypeDef

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.PipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePipelineRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Name
- **Type**: typing.Optional[str]

### InputBucket
- **Type**: typing.Optional[str]

### Role
- **Type**: typing.Optional[str]

### AwsKmsKeyArn
- **Type**: typing.Optional[str]

### Notifications
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.NotificationsTypeDef]

### ContentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.PipelineOutputConfigUnionTypeDef]

### ThumbnailConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder_classes.PipelineOutputConfigUnionTypeDef]


# UpdatePipelineResponseTypeDef

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.PipelineTypeDef'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.WarningTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePipelineStatusRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePipelineStatusResponseTypeDef

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.PipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VideoParametersOutputTypeDef

### Codec
- **Type**: typing.Optional[str]

### CodecOptions
- **Type**: typing.Optional[typing.Dict[str, str]]

### KeyframesMaxDist
- **Type**: typing.Optional[str]

### FixedGOP
- **Type**: typing.Optional[str]

### BitRate
- **Type**: typing.Optional[str]

### FrameRate
- **Type**: typing.Optional[str]

### MaxFrameRate
- **Type**: typing.Optional[str]

### Resolution
- **Type**: typing.Optional[str]

### AspectRatio
- **Type**: typing.Optional[str]

### MaxWidth
- **Type**: typing.Optional[str]

### MaxHeight
- **Type**: typing.Optional[str]

### DisplayAspectRatio
- **Type**: typing.Optional[str]

### SizingPolicy
- **Type**: typing.Optional[str]

### PaddingPolicy
- **Type**: typing.Optional[str]

### Watermarks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder_classes.PresetWatermarkTypeDef]]


# VideoParametersTypeDef

### Codec
- **Type**: typing.Optional[str]

### CodecOptions
- **Type**: typing.Optional[typing.Mapping[str, str]]

### KeyframesMaxDist
- **Type**: typing.Optional[str]

### FixedGOP
- **Type**: typing.Optional[str]

### BitRate
- **Type**: typing.Optional[str]

### FrameRate
- **Type**: typing.Optional[str]

### MaxFrameRate
- **Type**: typing.Optional[str]

### Resolution
- **Type**: typing.Optional[str]

### AspectRatio
- **Type**: typing.Optional[str]

### MaxWidth
- **Type**: typing.Optional[str]

### MaxHeight
- **Type**: typing.Optional[str]

### DisplayAspectRatio
- **Type**: typing.Optional[str]

### SizingPolicy
- **Type**: typing.Optional[str]

### PaddingPolicy
- **Type**: typing.Optional[str]

### Watermarks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.elastictranscoder_classes.PresetWatermarkTypeDef]]


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# WarningTypeDef

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


