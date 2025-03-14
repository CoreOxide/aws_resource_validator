# Mediatailor Classes

# AccessConfigurationTypeDef

### AccessType
- **Type**: typing.Optional[typing.Literal['AUTODETECT_SIGV4', 'S3_SIGV4', 'SECRETS_MANAGER_ACCESS_TOKEN']]

### SecretsManagerAccessTokenConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SecretsManagerAccessTokenConfigurationTypeDef]


# AdBreakOpportunityTypeDef

### OffsetMillis
- **Type**: <class 'int'>
- **Required**: Yes


# AdBreakOutputTypeDef

### OffsetMillis
- **Type**: <class 'int'>
- **Required**: Yes

### MessageType
- **Type**: typing.Optional[typing.Literal['SPLICE_INSERT', 'TIME_SIGNAL']]

### Slate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SlateSourceTypeDef]

### SpliceInsertMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SpliceInsertMessageTypeDef]

### TimeSignalMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.TimeSignalMessageOutputTypeDef]

### AdBreakMetadata
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.KeyValuePairTypeDef]]


# AdBreakTypeDef

### OffsetMillis
- **Type**: <class 'int'>
- **Required**: Yes

### MessageType
- **Type**: typing.Optional[typing.Literal['SPLICE_INSERT', 'TIME_SIGNAL']]

### Slate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SlateSourceTypeDef]

### SpliceInsertMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SpliceInsertMessageTypeDef]

### TimeSignalMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.TimeSignalMessageUnionTypeDef]

### AdBreakMetadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.KeyValuePairTypeDef]]


# AdBreakUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AdConditioningConfigurationTypeDef

### StreamingMediaFileConditioning
- **Type**: typing.Literal['NONE', 'TRANSCODE']
- **Required**: Yes


# AdMarkerPassthroughTypeDef

### Enabled
- **Type**: typing.Optional[bool]


# AlertTypeDef

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


# AlternateMediaOutputTypeDef

### SourceLocationName
- **Type**: typing.Optional[str]

### LiveSourceName
- **Type**: typing.Optional[str]

### VodSourceName
- **Type**: typing.Optional[str]

### ClipRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.ClipRangeTypeDef]

### ScheduledStartTimeMillis
- **Type**: typing.Optional[int]

### AdBreaks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakOutputTypeDef]]

### DurationMillis
- **Type**: typing.Optional[int]


# AlternateMediaTypeDef

### SourceLocationName
- **Type**: typing.Optional[str]

### LiveSourceName
- **Type**: typing.Optional[str]

### VodSourceName
- **Type**: typing.Optional[str]

### ClipRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.ClipRangeTypeDef]

### ScheduledStartTimeMillis
- **Type**: typing.Optional[int]

### AdBreaks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakUnionTypeDef]]

### DurationMillis
- **Type**: typing.Optional[int]


# AlternateMediaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AudienceMediaOutputTypeDef

### Audience
- **Type**: typing.Optional[str]

### AlternateMedia
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AlternateMediaOutputTypeDef]]


# AudienceMediaTypeDef

### Audience
- **Type**: typing.Optional[str]

### AlternateMedia
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AlternateMediaUnionTypeDef]]


# AudienceMediaUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# AvailMatchingCriteriaTypeDef

### DynamicVariable
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes


# AvailSuppressionTypeDef

### Mode
- **Type**: typing.Optional[typing.Literal['AFTER_LIVE_EDGE', 'BEHIND_LIVE_EDGE', 'OFF']]

### Value
- **Type**: typing.Optional[str]

### FillPolicy
- **Type**: typing.Optional[typing.Literal['FULL_AVAIL_ONLY', 'PARTIAL_AVAIL']]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BumperTypeDef

### EndUrl
- **Type**: typing.Optional[str]

### StartUrl
- **Type**: typing.Optional[str]


# CdnConfigurationTypeDef

### AdSegmentUrlPrefix
- **Type**: typing.Optional[str]

### ContentSegmentUrlPrefix
- **Type**: typing.Optional[str]


# ChannelTypeDef

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.ResponseOutputItemTypeDef]
- **Required**: Yes

### PlaybackMode
- **Type**: <class 'str'>
- **Required**: Yes

### Tier
- **Type**: <class 'str'>
- **Required**: Yes

### LogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.LogConfigurationForChannelTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FillerSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SlateSourceTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### Audiences
- **Type**: typing.Optional[typing.List[str]]


# ClipRangeTypeDef

### EndOffsetMillis
- **Type**: typing.Optional[int]

### StartOffsetMillis
- **Type**: typing.Optional[int]


# ConfigureLogsForChannelRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### LogTypes
- **Type**: typing.Sequence[typing.Literal['AS_RUN']]
- **Required**: Yes


# ConfigureLogsForChannelResponseTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### LogTypes
- **Type**: typing.List[typing.Literal['AS_RUN']]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ConfigureLogsForPlaybackConfigurationRequestTypeDef

### PercentEnabled
- **Type**: <class 'int'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### EnabledLoggingStrategies
- **Type**: typing.Optional[typing.Sequence[typing.Literal['LEGACY_CLOUDWATCH', 'VENDED_LOGS']]]


# ConfigureLogsForPlaybackConfigurationResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateChannelRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.RequestOutputItemTypeDef]
- **Required**: Yes

### PlaybackMode
- **Type**: typing.Literal['LINEAR', 'LOOP']
- **Required**: Yes

### FillerSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SlateSourceTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Tier
- **Type**: typing.Optional[typing.Literal['BASIC', 'STANDARD']]

### TimeShiftConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.TimeShiftConfigurationTypeDef]

### Audiences
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateChannelResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.SlateSourceTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.ResponseOutputItemTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.TimeShiftConfigurationTypeDef'>
- **Required**: Yes

### Audiences
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLiveSourceRequestTypeDef

### HttpPackageConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.HttpPackageConfigurationTypeDef]
- **Required**: Yes

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateLiveSourceResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.HttpPackageConfigurationTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePrefetchScheduleRequestTypeDef

### Consumption
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchConsumptionUnionTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Retrieval
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchRetrievalUnionTypeDef'>
- **Required**: Yes

### StreamId
- **Type**: typing.Optional[str]


# CreatePrefetchScheduleResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Consumption
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchConsumptionOutputTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Retrieval
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchRetrievalOutputTypeDef'>
- **Required**: Yes

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProgramRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ScheduleConfigurationTypeDef'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### AdBreaks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakUnionTypeDef]]

### LiveSourceName
- **Type**: typing.Optional[str]

### VodSourceName
- **Type**: typing.Optional[str]

### AudienceMedia
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AudienceMediaUnionTypeDef]]


# CreateProgramResponseTypeDef

### AdBreaks
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakOutputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ClipRangeTypeDef'>
- **Required**: Yes

### DurationMillis
- **Type**: <class 'int'>
- **Required**: Yes

### AudienceMedia
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AudienceMediaOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSourceLocationRequestTypeDef

### HttpConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.HttpConfigurationTypeDef'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.AccessConfigurationTypeDef]

### DefaultSegmentDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.DefaultSegmentDeliveryConfigurationTypeDef]

### SegmentDeliveryConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.SegmentDeliveryConfigurationTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateSourceLocationResponseTypeDef

### AccessConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.AccessConfigurationTypeDef'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultSegmentDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.DefaultSegmentDeliveryConfigurationTypeDef'>
- **Required**: Yes

### HttpConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.HttpConfigurationTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SegmentDeliveryConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.SegmentDeliveryConfigurationTypeDef]
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateVodSourceRequestTypeDef

### HttpPackageConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.HttpPackageConfigurationTypeDef]
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateVodSourceResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.HttpPackageConfigurationTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DashConfigurationForPutTypeDef

### MpdLocation
- **Type**: typing.Optional[str]

### OriginManifestType
- **Type**: typing.Optional[typing.Literal['MULTI_PERIOD', 'SINGLE_PERIOD']]


# DashConfigurationTypeDef

### ManifestEndpointPrefix
- **Type**: typing.Optional[str]

### MpdLocation
- **Type**: typing.Optional[str]

### OriginManifestType
- **Type**: typing.Optional[typing.Literal['MULTI_PERIOD', 'SINGLE_PERIOD']]


# DashPlaylistSettingsTypeDef

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### MinBufferTimeSeconds
- **Type**: typing.Optional[int]

### MinUpdatePeriodSeconds
- **Type**: typing.Optional[int]

### SuggestedPresentationDelaySeconds
- **Type**: typing.Optional[int]


# DefaultSegmentDeliveryConfigurationTypeDef

### BaseUrl
- **Type**: typing.Optional[str]


# DeleteChannelPolicyRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLiveSourceRequestTypeDef

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePlaybackConfigurationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePrefetchScheduleRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProgramRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceLocationRequestTypeDef

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVodSourceRequestTypeDef

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.SlateSourceTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.ResponseOutputItemTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.LogConfigurationForChannelTypeDef'>
- **Required**: Yes

### TimeShiftConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.TimeShiftConfigurationTypeDef'>
- **Required**: Yes

### Audiences
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLiveSourceRequestTypeDef

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeLiveSourceResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.HttpPackageConfigurationTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeProgramRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProgramResponseTypeDef

### AdBreaks
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakOutputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ClipRangeTypeDef'>
- **Required**: Yes

### DurationMillis
- **Type**: <class 'int'>
- **Required**: Yes

### AudienceMedia
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AudienceMediaOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSourceLocationRequestTypeDef

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeSourceLocationResponseTypeDef

### AccessConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.AccessConfigurationTypeDef'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultSegmentDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.DefaultSegmentDeliveryConfigurationTypeDef'>
- **Required**: Yes

### HttpConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.HttpConfigurationTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SegmentDeliveryConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.SegmentDeliveryConfigurationTypeDef]
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeVodSourceRequestTypeDef

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeVodSourceResponseTypeDef

### AdBreakOpportunities
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakOpportunityTypeDef]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.HttpPackageConfigurationTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChannelPolicyRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelPolicyResponseTypeDef

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChannelScheduleRequestPaginateTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### DurationMinutes
- **Type**: typing.Optional[str]

### Audience
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# GetChannelScheduleRequestTypeDef

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


# GetChannelScheduleResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.ScheduleEntryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# GetPlaybackConfigurationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# GetPlaybackConfigurationResponseTypeDef

### AdDecisionServerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### AvailSuppression
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.AvailSuppressionTypeDef'>
- **Required**: Yes

### Bumper
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.BumperTypeDef'>
- **Required**: Yes

### CdnConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.CdnConfigurationTypeDef'>
- **Required**: Yes

### ConfigurationAliases
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### DashConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.DashConfigurationTypeDef'>
- **Required**: Yes

### HlsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.HlsConfigurationTypeDef'>
- **Required**: Yes

### InsertionMode
- **Type**: typing.Literal['PLAYER_SELECT', 'STITCHED_ONLY']
- **Required**: Yes

### LivePreRollConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.LivePreRollConfigurationTypeDef'>
- **Required**: Yes

### LogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.LogConfigurationTypeDef'>
- **Required**: Yes

### ManifestProcessingRules
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ManifestProcessingRulesTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.AdConditioningConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPrefetchScheduleRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# GetPrefetchScheduleResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Consumption
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchConsumptionOutputTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Retrieval
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchRetrievalOutputTypeDef'>
- **Required**: Yes

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HlsConfigurationTypeDef

### ManifestEndpointPrefix
- **Type**: typing.Optional[str]


# HlsPlaylistSettingsOutputTypeDef

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### AdMarkupType
- **Type**: typing.Optional[typing.List[typing.Literal['DATERANGE', 'SCTE35_ENHANCED']]]


# HlsPlaylistSettingsTypeDef

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### AdMarkupType
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DATERANGE', 'SCTE35_ENHANCED']]]


# HlsPlaylistSettingsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HttpConfigurationTypeDef

### BaseUrl
- **Type**: <class 'str'>
- **Required**: Yes


# HttpPackageConfigurationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KeyValuePairTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ListAlertsRequestPaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListAlertsRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListAlertsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AlertTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListChannelsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.ChannelTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListLiveSourcesRequestPaginateTypeDef

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListLiveSourcesRequestTypeDef

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListLiveSourcesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.LiveSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPlaybackConfigurationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListPlaybackConfigurationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPlaybackConfigurationsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.PlaybackConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPrefetchSchedulesRequestPaginateTypeDef

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### StreamId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListPrefetchSchedulesRequestTypeDef

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### StreamId
- **Type**: typing.Optional[str]


# ListPrefetchSchedulesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchScheduleTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSourceLocationsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListSourceLocationsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSourceLocationsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.SourceLocationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListVodSourcesRequestPaginateTypeDef

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListVodSourcesRequestTypeDef

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListVodSourcesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.VodSourceTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LivePreRollConfigurationTypeDef

### AdDecisionServerUrl
- **Type**: typing.Optional[str]

### MaxDurationSeconds
- **Type**: typing.Optional[int]


# LiveSourceTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.HttpPackageConfigurationTypeDef]
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


# LogConfigurationForChannelTypeDef

### LogTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AS_RUN']]]


# LogConfigurationTypeDef

### PercentEnabled
- **Type**: <class 'int'>
- **Required**: Yes

### EnabledLoggingStrategies
- **Type**: typing.Optional[typing.List[typing.Literal['LEGACY_CLOUDWATCH', 'VENDED_LOGS']]]


# ManifestProcessingRulesTypeDef

### AdMarkerPassthrough
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.AdMarkerPassthroughTypeDef]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlaybackConfigurationTypeDef

### AdDecisionServerUrl
- **Type**: typing.Optional[str]

### AvailSuppression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.AvailSuppressionTypeDef]

### Bumper
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.BumperTypeDef]

### CdnConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.CdnConfigurationTypeDef]

### ConfigurationAliases
- **Type**: typing.Optional[typing.Dict[str, typing.Dict[str, str]]]

### DashConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.DashConfigurationTypeDef]

### HlsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.HlsConfigurationTypeDef]

### InsertionMode
- **Type**: typing.Optional[typing.Literal['PLAYER_SELECT', 'STITCHED_ONLY']]

### LivePreRollConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.LivePreRollConfigurationTypeDef]

### LogConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.LogConfigurationTypeDef]

### ManifestProcessingRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.ManifestProcessingRulesTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.AdConditioningConfigurationTypeDef]


# PrefetchConsumptionOutputTypeDef

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AvailMatchingCriteria
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AvailMatchingCriteriaTypeDef]]

### StartTime
- **Type**: typing.Optional[datetime.datetime]


# PrefetchConsumptionTypeDef

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.TimestampTypeDef'>
- **Required**: Yes

### AvailMatchingCriteria
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AvailMatchingCriteriaTypeDef]]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.TimestampTypeDef]


# PrefetchConsumptionUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrefetchRetrievalOutputTypeDef

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DynamicVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### StartTime
- **Type**: typing.Optional[datetime.datetime]


# PrefetchRetrievalTypeDef

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.TimestampTypeDef'>
- **Required**: Yes

### DynamicVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### StartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.TimestampTypeDef]


# PrefetchRetrievalUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# PrefetchScheduleTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Consumption
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchConsumptionOutputTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Retrieval
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchRetrievalOutputTypeDef'>
- **Required**: Yes

### StreamId
- **Type**: typing.Optional[str]


# PutChannelPolicyRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutPlaybackConfigurationRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### AdDecisionServerUrl
- **Type**: typing.Optional[str]

### AvailSuppression
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.AvailSuppressionTypeDef]

### Bumper
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.BumperTypeDef]

### CdnConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.CdnConfigurationTypeDef]

### ConfigurationAliases
- **Type**: typing.Optional[typing.Mapping[str, typing.Mapping[str, str]]]

### DashConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.DashConfigurationForPutTypeDef]

### InsertionMode
- **Type**: typing.Optional[typing.Literal['PLAYER_SELECT', 'STITCHED_ONLY']]

### LivePreRollConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.LivePreRollConfigurationTypeDef]

### ManifestProcessingRules
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.ManifestProcessingRulesTypeDef]

### PersonalizationThresholdSeconds
- **Type**: typing.Optional[int]

### SlateAdUrl
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TranscodeProfileName
- **Type**: typing.Optional[str]

### VideoContentSourceUrl
- **Type**: typing.Optional[str]

### AdConditioningConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.AdConditioningConfigurationTypeDef]


# PutPlaybackConfigurationResponseTypeDef

### AdDecisionServerUrl
- **Type**: <class 'str'>
- **Required**: Yes

### AvailSuppression
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.AvailSuppressionTypeDef'>
- **Required**: Yes

### Bumper
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.BumperTypeDef'>
- **Required**: Yes

### CdnConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.CdnConfigurationTypeDef'>
- **Required**: Yes

### ConfigurationAliases
- **Type**: typing.Dict[str, typing.Dict[str, str]]
- **Required**: Yes

### DashConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.DashConfigurationTypeDef'>
- **Required**: Yes

### HlsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.HlsConfigurationTypeDef'>
- **Required**: Yes

### InsertionMode
- **Type**: typing.Literal['PLAYER_SELECT', 'STITCHED_ONLY']
- **Required**: Yes

### LivePreRollConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.LivePreRollConfigurationTypeDef'>
- **Required**: Yes

### LogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.LogConfigurationTypeDef'>
- **Required**: Yes

### ManifestProcessingRules
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ManifestProcessingRulesTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.AdConditioningConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RequestOutputItemTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceGroup
- **Type**: <class 'str'>
- **Required**: Yes

### DashPlaylistSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.DashPlaylistSettingsTypeDef]

### HlsPlaylistSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.HlsPlaylistSettingsUnionTypeDef]


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


# ResponseOutputItemTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.DashPlaylistSettingsTypeDef]

### HlsPlaylistSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.HlsPlaylistSettingsOutputTypeDef]


# ScheduleAdBreakTypeDef

### ApproximateDurationSeconds
- **Type**: typing.Optional[int]

### ApproximateStartTime
- **Type**: typing.Optional[datetime.datetime]

### SourceLocationName
- **Type**: typing.Optional[str]

### VodSourceName
- **Type**: typing.Optional[str]


# ScheduleConfigurationTypeDef

### Transition
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.TransitionTypeDef'>
- **Required**: Yes

### ClipRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.ClipRangeTypeDef]


# ScheduleEntryTypeDef

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.ScheduleAdBreakTypeDef]]

### ScheduleEntryType
- **Type**: typing.Optional[typing.Literal['ALTERNATE_MEDIA', 'FILLER_SLATE', 'PROGRAM']]

### VodSourceName
- **Type**: typing.Optional[str]

### Audiences
- **Type**: typing.Optional[typing.List[str]]


# SecretsManagerAccessTokenConfigurationTypeDef

### HeaderName
- **Type**: typing.Optional[str]

### SecretArn
- **Type**: typing.Optional[str]

### SecretStringKey
- **Type**: typing.Optional[str]


# SegmentDeliveryConfigurationTypeDef

### BaseUrl
- **Type**: typing.Optional[str]

### Name
- **Type**: typing.Optional[str]


# SegmentationDescriptorTypeDef

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


# SlateSourceTypeDef

### SourceLocationName
- **Type**: typing.Optional[str]

### VodSourceName
- **Type**: typing.Optional[str]


# SourceLocationTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HttpConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.HttpConfigurationTypeDef'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.AccessConfigurationTypeDef]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### DefaultSegmentDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.DefaultSegmentDeliveryConfigurationTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### SegmentDeliveryConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.SegmentDeliveryConfigurationTypeDef]]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# SpliceInsertMessageTypeDef

### AvailNum
- **Type**: typing.Optional[int]

### AvailsExpected
- **Type**: typing.Optional[int]

### SpliceEventId
- **Type**: typing.Optional[int]

### UniqueProgramId
- **Type**: typing.Optional[int]


# StartChannelRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# StopChannelRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimeShiftConfigurationTypeDef

### MaxTimeDelaySeconds
- **Type**: <class 'int'>
- **Required**: Yes


# TimeSignalMessageOutputTypeDef

### SegmentationDescriptors
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.SegmentationDescriptorTypeDef]]


# TimeSignalMessageTypeDef

### SegmentationDescriptors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.SegmentationDescriptorTypeDef]]


# TimeSignalMessageUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TransitionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateChannelRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.RequestOutputItemTypeDef]
- **Required**: Yes

### FillerSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SlateSourceTypeDef]

### TimeShiftConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.TimeShiftConfigurationTypeDef]

### Audiences
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateChannelResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.SlateSourceTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.ResponseOutputItemTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.TimeShiftConfigurationTypeDef'>
- **Required**: Yes

### Audiences
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateLiveSourceRequestTypeDef

### HttpPackageConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.HttpPackageConfigurationTypeDef]
- **Required**: Yes

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateLiveSourceResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.HttpPackageConfigurationTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProgramRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.UpdateProgramScheduleConfigurationTypeDef'>
- **Required**: Yes

### AdBreaks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakUnionTypeDef]]

### AudienceMedia
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AudienceMediaUnionTypeDef]]


# UpdateProgramResponseTypeDef

### AdBreaks
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakOutputTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ClipRangeTypeDef'>
- **Required**: Yes

### DurationMillis
- **Type**: <class 'int'>
- **Required**: Yes

### ScheduledStartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AudienceMedia
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AudienceMediaOutputTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProgramScheduleConfigurationTypeDef

### Transition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.UpdateProgramTransitionTypeDef]

### ClipRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.ClipRangeTypeDef]


# UpdateProgramTransitionTypeDef

### ScheduledStartTimeMillis
- **Type**: typing.Optional[int]

### DurationMillis
- **Type**: typing.Optional[int]


# UpdateSourceLocationRequestTypeDef

### HttpConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.HttpConfigurationTypeDef'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### AccessConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.AccessConfigurationTypeDef]

### DefaultSegmentDeliveryConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.DefaultSegmentDeliveryConfigurationTypeDef]

### SegmentDeliveryConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.SegmentDeliveryConfigurationTypeDef]]


# UpdateSourceLocationResponseTypeDef

### AccessConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.AccessConfigurationTypeDef'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DefaultSegmentDeliveryConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.DefaultSegmentDeliveryConfigurationTypeDef'>
- **Required**: Yes

### HttpConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.HttpConfigurationTypeDef'>
- **Required**: Yes

### LastModifiedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SegmentDeliveryConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.SegmentDeliveryConfigurationTypeDef]
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateVodSourceRequestTypeDef

### HttpPackageConfigurations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.HttpPackageConfigurationTypeDef]
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes


# UpdateVodSourceResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.HttpPackageConfigurationTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VodSourceTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### HttpPackageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.HttpPackageConfigurationTypeDef]
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


