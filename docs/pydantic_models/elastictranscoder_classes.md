# Elastictranscoder Classes

# Artwork

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
- **Type**: <class 'NoneType'>


# AudioCodecOptions

### Profile
- **Type**: typing.Optional[str]

### BitDepth
- **Type**: typing.Optional[str]

### BitOrder
- **Type**: typing.Optional[str]

### Signed
- **Type**: typing.Optional[str]


# AudioParameters

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.AudioCodecOptions]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelJobRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# CaptionFormat

### Format
- **Type**: typing.Optional[str]

### Pattern
- **Type**: typing.Optional[str]

### Encryption
- **Type**: <class 'NoneType'>


# CaptionSource

### Key
- **Type**: typing.Optional[str]

### Language
- **Type**: typing.Optional[str]

### TimeOffset
- **Type**: typing.Optional[str]

### Label
- **Type**: typing.Optional[str]

### Encryption
- **Type**: <class 'NoneType'>


# Captions

### MergePolicy
- **Type**: typing.Optional[str]

### CaptionSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.CaptionSource]]

### CaptionFormats
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.CaptionFormat]]


# CaptionsOutput

### MergePolicy
- **Type**: typing.Optional[str]

### CaptionSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.CaptionSource]]

### CaptionFormats
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.CaptionFormat]]


# Clip

### TimeSpan
- **Type**: <class 'NoneType'>


# CreateJobOutput

### Key
- **Type**: typing.Optional[str]

### ThumbnailPattern
- **Type**: typing.Optional[str]

### ThumbnailEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Encryption]

### Rotate
- **Type**: typing.Optional[str]

### PresetId
- **Type**: typing.Optional[str]

### SegmentDuration
- **Type**: typing.Optional[str]

### Watermarks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.JobWatermark]]

### AlbumArt
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.JobAlbumArt, aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.JobAlbumArtOutput, NoneType]

### Composition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Clip]]

### Captions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Captions, aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.CaptionsOutput, NoneType]

### Encryption
- **Type**: <class 'NoneType'>


# CreateJobPlaylist

### Name
- **Type**: typing.Optional[str]

### Format
- **Type**: typing.Optional[str]

### OutputKeys
- **Type**: typing.Optional[typing.List[str]]

### HlsContentProtection
- **Type**: <class 'NoneType'>

### PlayReadyDrm
- **Type**: <class 'NoneType'>


# CreateJobRequest

### PipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### Input
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.JobInput, aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.JobInputOutput, NoneType]

### Inputs
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.JobInput, aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.JobInputOutput]]]

### Output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.CreateJobOutput]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.CreateJobOutput]]

### OutputKeyPrefix
- **Type**: typing.Optional[str]

### Playlists
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.CreateJobPlaylist]]

### UserMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateJobResponse

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePipelineRequest

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
- **Type**: <class 'NoneType'>

### ContentConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PipelineOutputConfig, aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PipelineOutputConfigOutput, NoneType]

### ThumbnailConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PipelineOutputConfig, aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PipelineOutputConfigOutput, NoneType]


# CreatePipelineResponse

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Pipeline'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Warning]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePresetRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### Container
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Video
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.VideoParameters, aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.VideoParametersOutput, NoneType]

### Audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.AudioParameters]

### Thumbnails
- **Type**: <class 'NoneType'>


# CreatePresetResponse

### Preset
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Preset'>
- **Required**: Yes

### Warning
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
- **Required**: Yes


# DeletePipelineRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePresetRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DetectedProperties

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


# Encryption

### Mode
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### KeyMd5
- **Type**: typing.Optional[str]

### InitializationVector
- **Type**: typing.Optional[str]


# HlsContentProtection

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


# InputCaptions

### MergePolicy
- **Type**: typing.Optional[str]

### CaptionSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.CaptionSource]]


# InputCaptionsOutput

### MergePolicy
- **Type**: typing.Optional[str]

### CaptionSources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.CaptionSource]]


# Job

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### PipelineId
- **Type**: typing.Optional[str]

### Input
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.JobInputOutput]

### Inputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.JobInputOutput]]

### Output
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.JobOutput]

### Outputs
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.JobOutput]]

### OutputKeyPrefix
- **Type**: typing.Optional[str]

### Playlists
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Playlist]]

### Status
- **Type**: typing.Optional[str]

### UserMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### Timing
- **Type**: <class 'NoneType'>


# JobAlbumArt

### MergePolicy
- **Type**: typing.Optional[str]

### Artwork
- **Type**: typing.Optional[typing.List[NoneType]]


# JobAlbumArtOutput

### MergePolicy
- **Type**: typing.Optional[str]

### Artwork
- **Type**: typing.Optional[typing.List[NoneType]]


# JobInput

### Key
- **Type**: typing.Optional[str]

### FrameRate
- **Type**: typing.Optional[str]

### Resolution
- **Type**: typing.Optional[str]

### AspectRatio
- **Type**: typing.Optional[str]

### Interlaced
- **Type**: typing.Optional[str]

### Container
- **Type**: typing.Optional[str]

### Encryption
- **Type**: <class 'NoneType'>

### TimeSpan
- **Type**: <class 'NoneType'>

### InputCaptions
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.InputCaptions, aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.InputCaptionsOutput, NoneType]

### DetectedProperties
- **Type**: <class 'NoneType'>


# JobInputOutput

### Key
- **Type**: typing.Optional[str]

### FrameRate
- **Type**: typing.Optional[str]

### Resolution
- **Type**: typing.Optional[str]

### AspectRatio
- **Type**: typing.Optional[str]

### Interlaced
- **Type**: typing.Optional[str]

### Container
- **Type**: typing.Optional[str]

### Encryption
- **Type**: <class 'NoneType'>

### TimeSpan
- **Type**: <class 'NoneType'>

### InputCaptions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.InputCaptionsOutput]

### DetectedProperties
- **Type**: <class 'NoneType'>


# JobOutput

### Id
- **Type**: typing.Optional[str]

### Key
- **Type**: typing.Optional[str]

### ThumbnailPattern
- **Type**: typing.Optional[str]

### ThumbnailEncryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Encryption]

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.JobWatermark]]

### AlbumArt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.JobAlbumArtOutput]

### Composition
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Clip]]

### Captions
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.CaptionsOutput]

### Encryption
- **Type**: <class 'NoneType'>

### AppliedColorSpaceConversion
- **Type**: typing.Optional[str]


# JobWatermark

### PresetWatermarkId
- **Type**: typing.Optional[str]

### InputKey
- **Type**: typing.Optional[str]

### Encryption
- **Type**: <class 'NoneType'>


# ListJobsByPipelineRequest

### PipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### Ascending
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]


# ListJobsByPipelineRequestPaginate

### PipelineId
- **Type**: <class 'str'>
- **Required**: Yes

### Ascending
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PaginatorConfig]


# ListJobsByPipelineResponse

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Job]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
- **Required**: Yes


# ListJobsByStatusRequest

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Ascending
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]


# ListJobsByStatusRequestPaginate

### Status
- **Type**: <class 'str'>
- **Required**: Yes

### Ascending
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PaginatorConfig]


# ListJobsByStatusResponse

### Jobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Job]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
- **Required**: Yes


# ListPipelinesRequest

### Ascending
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]


# ListPipelinesRequestPaginate

### Ascending
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PaginatorConfig]


# ListPipelinesResponse

### Pipelines
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Pipeline]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
- **Required**: Yes


# ListPresetsRequest

### Ascending
- **Type**: typing.Optional[str]

### PageToken
- **Type**: typing.Optional[str]


# ListPresetsRequestPaginate

### Ascending
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PaginatorConfig]


# ListPresetsResponse

### Presets
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Preset]
- **Required**: Yes

### NextPageToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
- **Required**: Yes


# Notifications

### Progressing
- **Type**: typing.Optional[str]

### Completed
- **Type**: typing.Optional[str]

### Warning
- **Type**: typing.Optional[str]

### Error
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Permission

### GranteeType
- **Type**: typing.Optional[str]

### Grantee
- **Type**: typing.Optional[str]

### Access
- **Type**: typing.Optional[typing.List[str]]


# PermissionOutput

### GranteeType
- **Type**: typing.Optional[str]

### Grantee
- **Type**: typing.Optional[str]

### Access
- **Type**: typing.Optional[typing.List[str]]


# Pipeline

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
- **Type**: <class 'NoneType'>

### ContentConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PipelineOutputConfigOutput]

### ThumbnailConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PipelineOutputConfigOutput]


# PipelineOutputConfig

### Bucket
- **Type**: typing.Optional[str]

### StorageClass
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Permission]]


# PipelineOutputConfigOutput

### Bucket
- **Type**: typing.Optional[str]

### StorageClass
- **Type**: typing.Optional[str]

### Permissions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PermissionOutput]]


# PlayReadyDrm

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


# Playlist

### Name
- **Type**: typing.Optional[str]

### Format
- **Type**: typing.Optional[str]

### OutputKeys
- **Type**: typing.Optional[typing.List[str]]

### HlsContentProtection
- **Type**: <class 'NoneType'>

### PlayReadyDrm
- **Type**: <class 'NoneType'>

### Status
- **Type**: typing.Optional[str]

### StatusDetail
- **Type**: typing.Optional[str]


# Preset

### Id
- **Type**: typing.Optional[str]

### Arn
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Container
- **Type**: typing.Optional[str]

### Audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.AudioParameters]

### Video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.VideoParametersOutput]

### Thumbnails
- **Type**: <class 'NoneType'>

### Type
- **Type**: typing.Optional[str]


# PresetWatermark

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


# ReadJobRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# ReadJobRequestWait

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: <class 'NoneType'>


# ReadJobResponse

### Job
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Job'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
- **Required**: Yes


# ReadPipelineRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# ReadPipelineResponse

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Pipeline'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Warning]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
- **Required**: Yes


# ReadPresetRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# ReadPresetResponse

### Preset
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Preset'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
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


# TestRoleRequest

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
- **Type**: typing.List[str]
- **Required**: Yes


# TestRoleResponse

### Success
- **Type**: <class 'str'>
- **Required**: Yes

### Messages
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
- **Required**: Yes


# Thumbnails

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


# TimeSpan

### StartTime
- **Type**: typing.Optional[str]

### Duration
- **Type**: typing.Optional[str]


# Timing

### SubmitTimeMillis
- **Type**: typing.Optional[int]

### StartTimeMillis
- **Type**: typing.Optional[int]

### FinishTimeMillis
- **Type**: typing.Optional[int]


# UpdatePipelineNotificationsRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Notifications
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Notifications'>
- **Required**: Yes


# UpdatePipelineNotificationsResponse

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Pipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePipelineRequest

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
- **Type**: <class 'NoneType'>

### ContentConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PipelineOutputConfig, aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PipelineOutputConfigOutput, NoneType]

### ThumbnailConfig
- **Type**: typing.Union[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PipelineOutputConfig, aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PipelineOutputConfigOutput, NoneType]


# UpdatePipelineResponse

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Pipeline'>
- **Required**: Yes

### Warnings
- **Type**: typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Warning]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePipelineStatusRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: <class 'str'>
- **Required**: Yes


# UpdatePipelineStatusResponse

### Pipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.Pipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.ResponseMetadata'>
- **Required**: Yes


# VideoParameters

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PresetWatermark]]


# VideoParametersOutput

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.elastictranscoder.elastictranscoder_classes.PresetWatermark]]


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


# Warning

### Code
- **Type**: typing.Optional[str]

### Message
- **Type**: typing.Optional[str]


