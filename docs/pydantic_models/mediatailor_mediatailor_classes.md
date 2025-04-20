# Mediatailor Mediatailor Classes

# AccessConfiguration

### AccessType
- **Type**: typing.Optional[typing.Literal['AUTODETECT_SIGV4', 'S3_SIGV4', 'SECRETS_MANAGER_ACCESS_TOKEN']]

### SecretsManagerAccessTokenConfiguration
- **Type**: <class 'NoneType'>


# AdBreak

### OffsetMillis
- **Type**: <class 'int'>
- **Required**: Yes

### MessageType
- **Type**: typing.Optional[typing.Literal['SPLICE_INSERT', 'TIME_SIGNAL']]

### Slate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SlateSource]

### SpliceInsertMessage
- **Type**: <class 'NoneType'>

### TimeSignalMessage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.TimeSignalMessage, aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.TimeSignalMessageOutput, NoneType]

### AdBreakMetadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.KeyValuePair]]


# AdBreakOpportunity

### OffsetMillis
- **Type**: <class 'int'>
- **Required**: Yes


# AdBreakOutput

### OffsetMillis
- **Type**: <class 'int'>
- **Required**: Yes

### MessageType
- **Type**: typing.Optional[typing.Literal['SPLICE_INSERT', 'TIME_SIGNAL']]

### Slate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SlateSource]

### SpliceInsertMessage
- **Type**: <class 'NoneType'>

### TimeSignalMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.TimeSignalMessageOutput]

### AdBreakMetadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.KeyValuePair]]


# AdConditioningConfiguration

### StreamingMediaFileConditioning
- **Type**: typing.Literal['NONE', 'TRANSCODE']
- **Required**: Yes


# AdMarkerPassthrough

### Enabled
- **Type**: typing.Optional[bool]


# Alert

### AlertCode
- **Type**: <class 'str'>
- **Required**: Yes

### AlertMessage
- **Type**: <class 'str'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### RelatedResourceArns
- **Type**: typing.List[str]
- **Required**: Yes

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Category
- **Type**: typing.Optional[typing.Literal['INFO', 'PLAYBACK_WARNING', 'SCHEDULING_ERROR']]


# AlternateMedia

### SourceLocationName
- **Type**: typing.Optional[str]

### LiveSourceName
- **Type**: typing.Optional[str]

### VodSourceName
- **Type**: typing.Optional[str]

### ClipRange
- **Type**: <class 'NoneType'>

### ScheduledStartTimeMillis
- **Type**: typing.Optional[int]

### AdBreaks
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AdBreak, aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AdBreakOutput]]]

### DurationMillis
- **Type**: typing.Optional[int]


# AlternateMediaOutput

### SourceLocationName
- **Type**: typing.Optional[str]

### LiveSourceName
- **Type**: typing.Optional[str]

### VodSourceName
- **Type**: typing.Optional[str]

### ClipRange
- **Type**: <class 'NoneType'>

### ScheduledStartTimeMillis
- **Type**: typing.Optional[int]

### AdBreaks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AdBreakOutput]]

### DurationMillis
- **Type**: typing.Optional[int]


# AudienceMedia

### Audience
- **Type**: typing.Optional[str]

### AlternateMedia
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AlternateMedia, aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AlternateMediaOutput]]]


# AudienceMediaOutput

### Audience
- **Type**: typing.Optional[str]

### AlternateMedia
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AlternateMediaOutput]]


# AvailMatchingCriteria

### DynamicVariable
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes


# AvailSuppression

### Mode
- **Type**: typing.Optional[typing.Literal['AFTER_LIVE_EDGE', 'BEHIND_LIVE_EDGE', 'OFF']]

### Value
- **Type**: typing.Optional[str]

### FillPolicy
- **Type**: typing.Optional[typing.Literal['FULL_AVAIL_ONLY', 'PARTIAL_AVAIL']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Bumper

### EndUrl
- **Type**: typing.Optional[str]

### StartUrl
- **Type**: typing.Optional[str]


# CdnConfiguration

### AdSegmentUrlPrefix
- **Type**: typing.Optional[str]

### ContentSegmentUrlPrefix
- **Type**: typing.Optional[str]


# Channel

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelState
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseOutputItem]
- **Required**: Yes

### PlaybackMode
- **Type**: <class 'str'>
- **Required**: Yes

### Tier
- **Type**: <class 'str'>
- **Required**: Yes

### LogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.LogConfigurationForChannel'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FillerSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SlateSource]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Audiences
- **Type**: typing.Optional[typing.List[str]]


# ClipRange

### EndOffsetMillis
- **Type**: typing.Optional[int]

### StartOffsetMillis
- **Type**: typing.Optional[int]


# ConfigureLogsForChannelRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### LogTypes
- **Type**: typing.List[typing.Literal['AS_RUN']]
- **Required**: Yes


# ConfigureLogsForChannelResponse

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### LogTypes
- **Type**: typing.List[typing.Literal['AS_RUN']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# ConfigureLogsForPlaybackConfigurationRequest

### PercentEnabled
- **Type**: <class 'int'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledLoggingStrategies
- **Type**: typing.Optional[typing.List[typing.Literal['LEGACY_CLOUDWATCH', 'VENDED_LOGS']]]


# ConfigureLogsForPlaybackConfigurationResponse

### PercentEnabled
- **Type**: <class 'int'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledLoggingStrategies
- **Type**: typing.List[typing.Literal['LEGACY_CLOUDWATCH', 'VENDED_LOGS']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# CreateChannelRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.RequestOutputItem]
- **Required**: Yes

### PlaybackMode
- **Type**: typing.Literal['LINEAR', 'LOOP']
- **Required**: Yes

### FillerSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SlateSource]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Tier
- **Type**: typing.Optional[typing.Literal['BASIC', 'STANDARD']]

### TimeShiftConfiguration
- **Type**: <class 'NoneType'>

### Audiences
- **Type**: typing.Optional[typing.List[str]]


# CreateChannelResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelState
- **Type**: typing.Literal['RUNNING', 'STOPPED']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FillerSlate
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SlateSource'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseOutputItem]
- **Required**: Yes

### PlaybackMode
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tier
- **Type**: <class 'str'>
- **Required**: Yes

### TimeShiftConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.TimeShiftConfiguration'>
- **Required**: Yes

### Audiences
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# CreateLiveSourceRequest

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpPackageConfiguration]
- **Required**: Yes

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateLiveSourceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpPackageConfiguration]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePrefetchScheduleRequest

### Consumption
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PrefetchConsumption, aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PrefetchConsumptionOutput]
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Retrieval
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PrefetchRetrieval, aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PrefetchRetrievalOutput]
- **Required**: Yes

### StreamId
- **Type**: typing.Optional[str]


# CreatePrefetchScheduleResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Consumption
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PrefetchConsumptionOutput'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Retrieval
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PrefetchRetrievalOutput'>
- **Required**: Yes

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# CreateProgramRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ScheduleConfiguration'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### AdBreaks
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AdBreak, aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AdBreakOutput]]]

### LiveSourceName
- **Type**: typing.Optional[str]

### VodSourceName
- **Type**: typing.Optional[str]

### AudienceMedia
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AudienceMedia, aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AudienceMediaOutput]]]


# CreateProgramResponse

### AdBreaks
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AdBreakOutput]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ClipRange
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ClipRange'>
- **Required**: Yes

### DurationMillis
- **Type**: <class 'int'>
- **Required**: Yes

### AudienceMedia
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AudienceMediaOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# CreateSourceLocationRequest

### HttpConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpConfiguration'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessConfiguration
- **Type**: <class 'NoneType'>

### DefaultSegmentDeliveryConfiguration
- **Type**: <class 'NoneType'>

### SegmentDeliveryConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SegmentDeliveryConfiguration]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateSourceLocationResponse

### AccessConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AccessConfiguration'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultSegmentDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.DefaultSegmentDeliveryConfiguration'>
- **Required**: Yes

### HttpConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpConfiguration'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SegmentDeliveryConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SegmentDeliveryConfiguration]
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# CreateVodSourceRequest

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpPackageConfiguration]
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateVodSourceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpPackageConfiguration]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# DashConfiguration

### ManifestEndpointPrefix
- **Type**: typing.Optional[str]

### MpdLocation
- **Type**: typing.Optional[str]

### OriginManifestType
- **Type**: typing.Optional[typing.Literal['MULTI_PERIOD', 'SINGLE_PERIOD']]


# DashConfigurationForPut

### MpdLocation
- **Type**: typing.Optional[str]

### OriginManifestType
- **Type**: typing.Optional[typing.Literal['MULTI_PERIOD', 'SINGLE_PERIOD']]


# DashPlaylistSettings

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### MinBufferTimeSeconds
- **Type**: typing.Optional[int]

### MinUpdatePeriodSeconds
- **Type**: typing.Optional[int]

### SuggestedPresentationDelaySeconds
- **Type**: typing.Optional[int]


# DefaultSegmentDeliveryConfiguration

### BaseUrl
- **Type**: typing.Optional[str]


# DeleteChannelPolicyRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLiveSourceRequest

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePlaybackConfigurationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePrefetchScheduleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProgramRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceLocationRequest

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVodSourceRequest

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelState
- **Type**: typing.Literal['RUNNING', 'STOPPED']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FillerSlate
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SlateSource'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseOutputItem]
- **Required**: Yes

### PlaybackMode
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tier
- **Type**: <class 'str'>
- **Required**: Yes

### LogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.LogConfigurationForChannel'>
- **Required**: Yes

### TimeShiftConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.TimeShiftConfiguration'>
- **Required**: Yes

### Audiences
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeLiveSourceRequest

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLiveSourceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpPackageConfiguration]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeProgramRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProgramResponse

### AdBreaks
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AdBreakOutput]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduledStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ClipRange
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ClipRange'>
- **Required**: Yes

### DurationMillis
- **Type**: <class 'int'>
- **Required**: Yes

### AudienceMedia
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AudienceMediaOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSourceLocationRequest

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSourceLocationResponse

### AccessConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AccessConfiguration'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultSegmentDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.DefaultSegmentDeliveryConfiguration'>
- **Required**: Yes

### HttpConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpConfiguration'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SegmentDeliveryConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SegmentDeliveryConfiguration]
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeVodSourceRequest

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVodSourceResponse

### AdBreakOpportunities
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AdBreakOpportunity]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpPackageConfiguration]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# GetChannelPolicyRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelPolicyResponse

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# GetChannelScheduleRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### DurationMinutes
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### Audience
- **Type**: typing.Optional[str]


# GetChannelScheduleRequestPaginate

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### DurationMinutes
- **Type**: typing.Optional[str]

### Audience
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PaginatorConfig]


# GetChannelScheduleResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ScheduleEntry]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetPlaybackConfigurationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetPlaybackConfigurationResponse

### AdDecisionServerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### AvailSuppression
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AvailSuppression'>
- **Required**: Yes

### Bumper
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.Bumper'>
- **Required**: Yes

### CdnConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.CdnConfiguration'>
- **Required**: Yes

### ConfigurationAliases
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### DashConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.DashConfiguration'>
- **Required**: Yes

### HlsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HlsConfiguration'>
- **Required**: Yes

### InsertionMode
- **Type**: typing.Literal['PLAYER_SELECT', 'STITCHED_ONLY']
- **Required**: Yes

### LivePreRollConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.LivePreRollConfiguration'>
- **Required**: Yes

### LogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.LogConfiguration'>
- **Required**: Yes

### ManifestProcessingRules
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ManifestProcessingRules'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PersonalizationThresholdSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### PlaybackConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackEndpointPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### SessionInitializationEndpointPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### SlateAdUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TranscodeProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### VideoContentSourceUrl
- **Type**: <class 'str'>
- **Required**: Yes

### AdConditioningConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AdConditioningConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# GetPrefetchScheduleRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPrefetchScheduleResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Consumption
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PrefetchConsumptionOutput'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Retrieval
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PrefetchRetrievalOutput'>
- **Required**: Yes

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# HlsConfiguration

### ManifestEndpointPrefix
- **Type**: typing.Optional[str]


# HlsPlaylistSettings

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### AdMarkupType
- **Type**: typing.Optional[typing.List[typing.Literal['DATERANGE', 'SCTE35_ENHANCED']]]


# HlsPlaylistSettingsOutput

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### AdMarkupType
- **Type**: typing.Optional[typing.List[typing.Literal['DATERANGE', 'SCTE35_ENHANCED']]]


# HttpConfiguration

### BaseUrl
- **Type**: <class 'str'>
- **Required**: Yes


# HttpPackageConfiguration

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### SourceGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['DASH', 'HLS']
- **Required**: Yes


# KeyValuePair

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ListAlertsRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAlertsRequestPaginate

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PaginatorConfig]


# ListAlertsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.Alert]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PaginatorConfig]


# ListChannelsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.Channel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLiveSourcesRequest

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLiveSourcesRequestPaginate

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PaginatorConfig]


# ListLiveSourcesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.LiveSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPlaybackConfigurationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPlaybackConfigurationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PaginatorConfig]


# ListPlaybackConfigurationsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PlaybackConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPrefetchSchedulesRequest

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### StreamId
- **Type**: typing.Optional[str]


# ListPrefetchSchedulesRequestPaginate

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### StreamId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PaginatorConfig]


# ListPrefetchSchedulesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PrefetchSchedule]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSourceLocationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSourceLocationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PaginatorConfig]


# ListSourceLocationsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SourceLocation]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# ListVodSourcesRequest

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListVodSourcesRequestPaginate

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PaginatorConfig]


# ListVodSourcesResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.VodSource]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LivePreRollConfiguration

### AdDecisionServerUrl
- **Type**: typing.Optional[str]

### MaxDurationSeconds
- **Type**: typing.Optional[int]


# LiveSource

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpPackageConfiguration]
- **Required**: Yes

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# LogConfiguration

### PercentEnabled
- **Type**: <class 'int'>
- **Required**: Yes

### EnabledLoggingStrategies
- **Type**: typing.Optional[typing.List[typing.Literal['LEGACY_CLOUDWATCH', 'VENDED_LOGS']]]


# LogConfigurationForChannel

### LogTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AS_RUN']]]


# ManifestProcessingRules

### AdMarkerPassthrough
- **Type**: <class 'NoneType'>


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlaybackConfiguration

### AdDecisionServerUrl
- **Type**: typing.Optional[str]

### AvailSuppression
- **Type**: <class 'NoneType'>

### Bumper
- **Type**: <class 'NoneType'>

### CdnConfiguration
- **Type**: <class 'NoneType'>

### ConfigurationAliases
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]

### DashConfiguration
- **Type**: <class 'NoneType'>

### HlsConfiguration
- **Type**: <class 'NoneType'>

### InsertionMode
- **Type**: typing.Optional[typing.Literal['PLAYER_SELECT', 'STITCHED_ONLY']]

### LivePreRollConfiguration
- **Type**: <class 'NoneType'>

### LogConfiguration
- **Type**: <class 'NoneType'>

### ManifestProcessingRules
- **Type**: <class 'NoneType'>

### Name
- **Type**: typing.Optional[str]

### PersonalizationThresholdSeconds
- **Type**: typing.Optional[int]

### PlaybackConfigurationArn
- **Type**: typing.Optional[str]

### PlaybackEndpointPrefix
- **Type**: typing.Optional[str]

### SessionInitializationEndpointPrefix
- **Type**: typing.Optional[str]

### SlateAdUrl
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TranscodeProfileName
- **Type**: typing.Optional[str]

### VideoContentSourceUrl
- **Type**: typing.Optional[str]

### AdConditioningConfiguration
- **Type**: <class 'NoneType'>


# PrefetchConsumption

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### AvailMatchingCriteria
- **Type**: typing.Optional[typing.List[NoneType]]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# PrefetchConsumptionOutput

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AvailMatchingCriteria
- **Type**: typing.Optional[typing.List[NoneType]]

### StartTime
- **Type**: typing.Optional[datetime.datetime]


# PrefetchRetrieval

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### DynamicVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# PrefetchRetrievalOutput

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DynamicVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### StartTime
- **Type**: typing.Optional[datetime.datetime]


# PrefetchSchedule

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Consumption
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PrefetchConsumptionOutput'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Retrieval
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.PrefetchRetrievalOutput'>
- **Required**: Yes

### StreamId
- **Type**: typing.Optional[str]


# PutChannelPolicyRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutPlaybackConfigurationRequest

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AdDecisionServerUrl
- **Type**: typing.Optional[str]

### AvailSuppression
- **Type**: <class 'NoneType'>

### Bumper
- **Type**: <class 'NoneType'>

### CdnConfiguration
- **Type**: <class 'NoneType'>

### ConfigurationAliases
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]

### DashConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.DashConfigurationForPut]

### InsertionMode
- **Type**: typing.Optional[typing.Literal['PLAYER_SELECT', 'STITCHED_ONLY']]

### LivePreRollConfiguration
- **Type**: <class 'NoneType'>

### ManifestProcessingRules
- **Type**: <class 'NoneType'>

### PersonalizationThresholdSeconds
- **Type**: typing.Optional[int]

### SlateAdUrl
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TranscodeProfileName
- **Type**: typing.Optional[str]

### VideoContentSourceUrl
- **Type**: typing.Optional[str]

### AdConditioningConfiguration
- **Type**: <class 'NoneType'>


# PutPlaybackConfigurationResponse

### AdDecisionServerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### AvailSuppression
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AvailSuppression'>
- **Required**: Yes

### Bumper
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.Bumper'>
- **Required**: Yes

### CdnConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.CdnConfiguration'>
- **Required**: Yes

### ConfigurationAliases
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### DashConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.DashConfiguration'>
- **Required**: Yes

### HlsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HlsConfiguration'>
- **Required**: Yes

### InsertionMode
- **Type**: typing.Literal['PLAYER_SELECT', 'STITCHED_ONLY']
- **Required**: Yes

### LivePreRollConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.LivePreRollConfiguration'>
- **Required**: Yes

### LogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.LogConfiguration'>
- **Required**: Yes

### ManifestProcessingRules
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ManifestProcessingRules'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PersonalizationThresholdSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### PlaybackConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackEndpointPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### SessionInitializationEndpointPrefix
- **Type**: <class 'str'>
- **Required**: Yes

### SlateAdUrl
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TranscodeProfileName
- **Type**: <class 'str'>
- **Required**: Yes

### VideoContentSourceUrl
- **Type**: <class 'str'>
- **Required**: Yes

### AdConditioningConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AdConditioningConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# RequestOutputItem

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceGroup
- **Type**: <class 'str'>
- **Required**: Yes

### DashPlaylistSettings
- **Type**: <class 'NoneType'>

### HlsPlaylistSettings
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HlsPlaylistSettings, aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HlsPlaylistSettingsOutput, NoneType]


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


# ResponseOutputItem

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackUrl
- **Type**: <class 'str'>
- **Required**: Yes

### SourceGroup
- **Type**: <class 'str'>
- **Required**: Yes

### DashPlaylistSettings
- **Type**: <class 'NoneType'>

### HlsPlaylistSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HlsPlaylistSettingsOutput]


# ScheduleAdBreak

### ApproximateDurationSeconds
- **Type**: typing.Optional[int]

### ApproximateStartTime
- **Type**: typing.Optional[datetime.datetime]

### SourceLocationName
- **Type**: typing.Optional[str]

### VodSourceName
- **Type**: typing.Optional[str]


# ScheduleConfiguration

### Transition
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.Transition'>
- **Required**: Yes

### ClipRange
- **Type**: <class 'NoneType'>


# ScheduleEntry

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### ApproximateDurationSeconds
- **Type**: typing.Optional[int]

### ApproximateStartTime
- **Type**: typing.Optional[datetime.datetime]

### LiveSourceName
- **Type**: typing.Optional[str]

### ScheduleAdBreaks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ScheduleAdBreak]]

### ScheduleEntryType
- **Type**: typing.Optional[typing.Literal['ALTERNATE_MEDIA', 'FILLER_SLATE', 'PROGRAM']]

### VodSourceName
- **Type**: typing.Optional[str]

### Audiences
- **Type**: typing.Optional[typing.List[str]]


# SecretsManagerAccessTokenConfiguration

### HeaderName
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### SecretStringKey
- **Type**: typing.Optional[str]


# SegmentDeliveryConfiguration

### BaseUrl
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# SegmentationDescriptor

### SegmentationEventId
- **Type**: typing.Optional[int]

### SegmentationUpidType
- **Type**: typing.Optional[int]

### SegmentationUpid
- **Type**: typing.Optional[str]

### SegmentationTypeId
- **Type**: typing.Optional[int]

### SegmentNum
- **Type**: typing.Optional[int]

### SegmentsExpected
- **Type**: typing.Optional[int]

### SubSegmentNum
- **Type**: typing.Optional[int]

### SubSegmentsExpected
- **Type**: typing.Optional[int]


# SlateSource

### SourceLocationName
- **Type**: typing.Optional[str]

### VodSourceName
- **Type**: typing.Optional[str]


# SourceLocation

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HttpConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpConfiguration'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessConfiguration
- **Type**: <class 'NoneType'>

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### DefaultSegmentDeliveryConfiguration
- **Type**: <class 'NoneType'>

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### SegmentDeliveryConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SegmentDeliveryConfiguration]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SpliceInsertMessage

### AvailNum
- **Type**: typing.Optional[int]

### AvailsExpected
- **Type**: typing.Optional[int]

### SpliceEventId
- **Type**: typing.Optional[int]

### UniqueProgramId
- **Type**: typing.Optional[int]


# StartChannelRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# StopChannelRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# TimeShiftConfiguration

### MaxTimeDelaySeconds
- **Type**: <class 'int'>
- **Required**: Yes


# TimeSignalMessage

### SegmentationDescriptors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SegmentationDescriptor]]


# TimeSignalMessageOutput

### SegmentationDescriptors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SegmentationDescriptor]]


# Transition

### RelativePosition
- **Type**: typing.Literal['AFTER_PROGRAM', 'BEFORE_PROGRAM']
- **Required**: Yes

### Type
- **Type**: <class 'str'>
- **Required**: Yes

### DurationMillis
- **Type**: typing.Optional[int]

### RelativeProgram
- **Type**: typing.Optional[str]

### ScheduledStartTimeMillis
- **Type**: typing.Optional[int]


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateChannelRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.RequestOutputItem]
- **Required**: Yes

### FillerSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SlateSource]

### TimeShiftConfiguration
- **Type**: <class 'NoneType'>

### Audiences
- **Type**: typing.Optional[typing.List[str]]


# UpdateChannelResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelState
- **Type**: typing.Literal['RUNNING', 'STOPPED']
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### FillerSlate
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SlateSource'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseOutputItem]
- **Required**: Yes

### PlaybackMode
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### Tier
- **Type**: <class 'str'>
- **Required**: Yes

### TimeShiftConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.TimeShiftConfiguration'>
- **Required**: Yes

### Audiences
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateLiveSourceRequest

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpPackageConfiguration]
- **Required**: Yes

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateLiveSourceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpPackageConfiguration]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProgramRequest

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.UpdateProgramScheduleConfiguration'>
- **Required**: Yes

### AdBreaks
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AdBreak, aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AdBreakOutput]]]

### AudienceMedia
- **Type**: typing.Optional[typing.List[typing.Union[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AudienceMedia, aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AudienceMediaOutput]]]


# UpdateProgramResponse

### AdBreaks
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AdBreakOutput]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ClipRange
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ClipRange'>
- **Required**: Yes

### DurationMillis
- **Type**: <class 'int'>
- **Required**: Yes

### ScheduledStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AudienceMedia
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AudienceMediaOutput]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateProgramScheduleConfiguration

### Transition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.UpdateProgramTransition]

### ClipRange
- **Type**: <class 'NoneType'>


# UpdateProgramTransition

### ScheduledStartTimeMillis
- **Type**: typing.Optional[int]

### DurationMillis
- **Type**: typing.Optional[int]


# UpdateSourceLocationRequest

### HttpConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpConfiguration'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessConfiguration
- **Type**: <class 'NoneType'>

### DefaultSegmentDeliveryConfiguration
- **Type**: <class 'NoneType'>

### SegmentDeliveryConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SegmentDeliveryConfiguration]]


# UpdateSourceLocationResponse

### AccessConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.AccessConfiguration'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultSegmentDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.DefaultSegmentDeliveryConfiguration'>
- **Required**: Yes

### HttpConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpConfiguration'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SegmentDeliveryConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.SegmentDeliveryConfiguration]
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateVodSourceRequest

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpPackageConfiguration]
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateVodSourceResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpPackageConfiguration]
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.ResponseMetadata'>
- **Required**: Yes


# VodSource

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor.mediatailor_classes.HttpPackageConfiguration]
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


