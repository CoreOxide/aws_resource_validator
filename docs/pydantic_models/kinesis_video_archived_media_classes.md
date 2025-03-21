# Kinesis Video Archived Media Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClipFragmentSelectorTypeDef

### FragmentSelectorType
- **Type**: typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']
- **Required**: Yes

### TimestampRange
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.ClipTimestampRangeTypeDef'>
- **Required**: Yes


# ClipTimestampRangeTypeDef

### StartTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.TimestampTypeDef'>
- **Required**: Yes


# DASHFragmentSelectorTypeDef

### FragmentSelectorType
- **Type**: typing.Optional[typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']]

### TimestampRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.DASHTimestampRangeTypeDef]


# DASHTimestampRangeTypeDef

### StartTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.TimestampTypeDef]

### EndTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.TimestampTypeDef]


# FragmentSelectorTypeDef

### FragmentSelectorType
- **Type**: typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']
- **Required**: Yes

### TimestampRange
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.TimestampRangeTypeDef'>
- **Required**: Yes


# FragmentTypeDef

### FragmentNumber
- **Type**: typing.Optional[str]

### FragmentSizeInBytes
- **Type**: typing.Optional[int]

### ProducerTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ServerTimestamp
- **Type**: typing.Optional[datetime.datetime]

### FragmentLengthInMilliseconds
- **Type**: typing.Optional[int]


# GetClipInputTypeDef

### ClipFragmentSelector
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.ClipFragmentSelectorTypeDef'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# GetClipOutputTypeDef

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDASHStreamingSessionURLInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### PlaybackMode
- **Type**: typing.Optional[typing.Literal['LIVE', 'LIVE_REPLAY', 'ON_DEMAND']]

### DisplayFragmentTimestamp
- **Type**: typing.Optional[typing.Literal['ALWAYS', 'NEVER']]

### DisplayFragmentNumber
- **Type**: typing.Optional[typing.Literal['ALWAYS', 'NEVER']]

### DASHFragmentSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.DASHFragmentSelectorTypeDef]

### Expires
- **Type**: typing.Optional[int]

### MaxManifestFragmentResults
- **Type**: typing.Optional[int]


# GetDASHStreamingSessionURLOutputTypeDef

### DASHStreamingSessionURL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetHLSStreamingSessionURLInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### PlaybackMode
- **Type**: typing.Optional[typing.Literal['LIVE', 'LIVE_REPLAY', 'ON_DEMAND']]

### HLSFragmentSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.HLSFragmentSelectorTypeDef]

### ContainerFormat
- **Type**: typing.Optional[typing.Literal['FRAGMENTED_MP4', 'MPEG_TS']]

### DiscontinuityMode
- **Type**: typing.Optional[typing.Literal['ALWAYS', 'NEVER', 'ON_DISCONTINUITY']]

### DisplayFragmentTimestamp
- **Type**: typing.Optional[typing.Literal['ALWAYS', 'NEVER']]

### Expires
- **Type**: typing.Optional[int]

### MaxMediaPlaylistFragmentResults
- **Type**: typing.Optional[int]


# GetHLSStreamingSessionURLOutputTypeDef

### HLSStreamingSessionURL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetImagesInputPaginateTypeDef

### ImageSelectorType
- **Type**: typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']
- **Required**: Yes

### StartTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.TimestampTypeDef'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['JPEG', 'PNG']
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### SamplingInterval
- **Type**: typing.Optional[int]

### FormatConfig
- **Type**: typing.Optional[typing.Mapping[typing.Literal['JPEGQuality'], str]]

### WidthPixels
- **Type**: typing.Optional[int]

### HeightPixels
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.PaginatorConfigTypeDef]


# GetImagesInputTypeDef

### ImageSelectorType
- **Type**: typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']
- **Required**: Yes

### StartTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.TimestampTypeDef'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['JPEG', 'PNG']
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### SamplingInterval
- **Type**: typing.Optional[int]

### FormatConfig
- **Type**: typing.Optional[typing.Mapping[typing.Literal['JPEGQuality'], str]]

### WidthPixels
- **Type**: typing.Optional[int]

### HeightPixels
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetImagesOutputTypeDef

### Images
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.ImageTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMediaForFragmentListInputTypeDef

### Fragments
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# GetMediaForFragmentListOutputTypeDef

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HLSFragmentSelectorTypeDef

### FragmentSelectorType
- **Type**: typing.Optional[typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']]

### TimestampRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.HLSTimestampRangeTypeDef]


# HLSTimestampRangeTypeDef

### StartTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.TimestampTypeDef]

### EndTimestamp
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.TimestampTypeDef]


# ImageTypeDef

### TimeStamp
- **Type**: typing.Optional[datetime.datetime]

### Error
- **Type**: typing.Optional[typing.Literal['MEDIA_ERROR', 'NO_MEDIA']]

### ImageContent
- **Type**: typing.Optional[str]


# ListFragmentsInputPaginateTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### FragmentSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.FragmentSelectorTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.PaginatorConfigTypeDef]


# ListFragmentsInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### FragmentSelector
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.FragmentSelectorTypeDef]


# ListFragmentsOutputTypeDef

### Fragments
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.FragmentTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# TimestampRangeTypeDef

### StartTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media_classes.TimestampTypeDef'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

