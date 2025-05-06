# Kinesis Video Archived Media Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ClipFragmentSelector

### FragmentSelectorType
- **Type**: typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']
- **Required**: Yes

### TimestampRange
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.ClipTimestampRange'>
- **Required**: Yes


# ClipTimestampRange

### StartTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# DASHFragmentSelector

### FragmentSelectorType
- **Type**: typing.Optional[typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']]

### TimestampRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.DASHTimestampRange]


# DASHTimestampRange

### StartTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# Fragment

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


# FragmentSelector

### FragmentSelectorType
- **Type**: typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']
- **Required**: Yes

### TimestampRange
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.TimestampRange'>
- **Required**: Yes


# GetClipInput

### ClipFragmentSelector
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.ClipFragmentSelector'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# GetClipOutput

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.ResponseMetadata'>
- **Required**: Yes


# GetDASHStreamingSessionURLInput

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
- **Type**: <class 'NoneType'>

### Expires
- **Type**: typing.Optional[int]

### MaxManifestFragmentResults
- **Type**: typing.Optional[int]


# GetDASHStreamingSessionURLOutput

### DASHStreamingSessionURL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.ResponseMetadata'>
- **Required**: Yes


# GetHLSStreamingSessionURLInput

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### PlaybackMode
- **Type**: typing.Optional[typing.Literal['LIVE', 'LIVE_REPLAY', 'ON_DEMAND']]

### HLSFragmentSelector
- **Type**: <class 'NoneType'>

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


# GetHLSStreamingSessionURLOutput

### HLSStreamingSessionURL
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.ResponseMetadata'>
- **Required**: Yes


# GetImagesInput

### ImageSelectorType
- **Type**: typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']
- **Required**: Yes

### StartTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTimestamp
- **Type**: typing.Union[datetime.datetime, str]
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
- **Type**: typing.Optional[typing.Dict[typing.Literal['JPEGQuality'], str]]

### WidthPixels
- **Type**: typing.Optional[int]

### HeightPixels
- **Type**: typing.Optional[int]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetImagesInputPaginate

### ImageSelectorType
- **Type**: typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']
- **Required**: Yes

### StartTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTimestamp
- **Type**: typing.Union[datetime.datetime, str]
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
- **Type**: typing.Optional[typing.Dict[typing.Literal['JPEGQuality'], str]]

### WidthPixels
- **Type**: typing.Optional[int]

### HeightPixels
- **Type**: typing.Optional[int]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.PaginatorConfig]


# GetImagesOutput

### Images
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.Image]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetMediaForFragmentListInput

### Fragments
- **Type**: typing.List[str]
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# GetMediaForFragmentListOutput

### ContentType
- **Type**: <class 'str'>
- **Required**: Yes

### Payload
- **Type**: <class 'botocore.response.StreamingBody'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.ResponseMetadata'>
- **Required**: Yes


# HLSFragmentSelector

### FragmentSelectorType
- **Type**: typing.Optional[typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']]

### TimestampRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.HLSTimestampRange]


# HLSTimestampRange

### StartTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### EndTimestamp
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# Image

### TimeStamp
- **Type**: typing.Optional[datetime.datetime]

### Error
- **Type**: typing.Optional[typing.Literal['MEDIA_ERROR', 'NO_MEDIA']]

### ImageContent
- **Type**: typing.Optional[str]


# ListFragmentsInput

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### FragmentSelector
- **Type**: <class 'NoneType'>


# ListFragmentsInputPaginate

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### FragmentSelector
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.PaginatorConfig]


# ListFragmentsOutput

### Fragments
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.Fragment]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesis_video_archived_media.kinesis_video_archived_media_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


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


# TimestampRange

### StartTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


