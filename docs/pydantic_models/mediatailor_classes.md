# Pydantic Models in mediatailor_classes

# AccessConfigurationTypeDef

### AccessType
- **Type**: typing.Optional[typing.Literal['AUTODETECT_SIGV4', 'S3_SIGV4', 'SECRETS_MANAGER_ACCESS_TOKEN']]

### SecretsManagerAccessTokenConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SecretsManagerAccessTokenConfigurationTypeDef]


# AdBreakOpportunityTypeDef

### OffsetMillis
- **Type**: <class 'int'>
- **Required**: Yes


# AdBreakTypeDef

### OffsetMillis
- **Type**: <class 'int'>
- **Required**: Yes

### AdBreakMetadata
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.KeyValuePairTypeDef]]

### MessageType
- **Type**: typing.Optional[typing.Literal['SPLICE_INSERT', 'TIME_SIGNAL']]

### Slate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SlateSourceTypeDef]

### SpliceInsertMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SpliceInsertMessageTypeDef]

### TimeSignalMessage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.TimeSignalMessageTypeDef]


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


# AlternateMediaTypeDef

### AdBreaks
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakTypeDef]]

### ClipRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.ClipRangeTypeDef]

### DurationMillis
- **Type**: typing.Optional[int]

### LiveSourceName
- **Type**: typing.Optional[str]

### ScheduledStartTimeMillis
- **Type**: typing.Optional[int]

### SourceLocationName
- **Type**: typing.Optional[str]

### VodSourceName
- **Type**: typing.Optional[str]


# AudienceMediaTypeDef

### AlternateMedia
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AlternateMediaTypeDef]]

### Audience
- **Type**: typing.Optional[str]


# AvailMatchingCriteriaTypeDef

### DynamicVariable
- **Type**: <class 'str'>
- **Required**: Yes

### Operator
- **Type**: typing.Literal['EQUALS']
- **Required**: Yes


# AvailSuppressionTypeDef

### FillPolicy
- **Type**: typing.Optional[typing.Literal['FULL_AVAIL_ONLY', 'PARTIAL_AVAIL']]

### Mode
- **Type**: typing.Optional[typing.Literal['AFTER_LIVE_EDGE', 'BEHIND_LIVE_EDGE', 'OFF']]

### Value
- **Type**: typing.Optional[str]


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


# ChannelPaginatorTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelState
- **Type**: <class 'str'>
- **Required**: Yes

### LogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.LogConfigurationForChannelTypeDef'>
- **Required**: Yes

### Outputs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.ResponseOutputItemPaginatorTypeDef]
- **Required**: Yes

### PlaybackMode
- **Type**: <class 'str'>
- **Required**: Yes

### Tier
- **Type**: <class 'str'>
- **Required**: Yes

### Audiences
- **Type**: typing.Optional[typing.List[str]]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FillerSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SlateSourceTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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

### LogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.LogConfigurationForChannelTypeDef'>
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

### Audiences
- **Type**: typing.Optional[typing.List[str]]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### FillerSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SlateSourceTypeDef]

### LastModifiedTime
- **Type**: typing.Optional[datetime.datetime]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ClipRangeTypeDef

### EndOffsetMillis
- **Type**: typing.Optional[int]

### StartOffsetMillis
- **Type**: typing.Optional[int]


# ConfigureLogsForChannelRequestRequestTypeDef

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


# ConfigureLogsForPlaybackConfigurationRequestRequestTypeDef

### PercentEnabled
- **Type**: <class 'int'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# ConfigureLogsForPlaybackConfigurationResponseTypeDef

### PercentEnabled
- **Type**: <class 'int'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateChannelRequestRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.RequestOutputItemTypeDef]
- **Required**: Yes

### PlaybackMode
- **Type**: typing.Literal['LINEAR', 'LOOP']
- **Required**: Yes

### Audiences
- **Type**: typing.Optional[typing.Sequence[str]]

### FillerSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SlateSourceTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### Tier
- **Type**: typing.Optional[typing.Literal['BASIC', 'STANDARD']]

### TimeShiftConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.TimeShiftConfigurationTypeDef]


# CreateChannelResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Audiences
- **Type**: typing.List[str]
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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateLiveSourceRequestRequestTypeDef

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


# CreatePrefetchScheduleRequestRequestTypeDef

### Consumption
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchConsumptionTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Retrieval
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchRetrievalTypeDef'>
- **Required**: Yes

### StreamId
- **Type**: typing.Optional[str]


# CreatePrefetchScheduleResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Consumption
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchConsumptionTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Retrieval
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchRetrievalTypeDef'>
- **Required**: Yes

### StreamId
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateProgramRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakTypeDef]]

### AudienceMedia
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AudienceMediaTypeDef]]

### LiveSourceName
- **Type**: typing.Optional[str]

### VodSourceName
- **Type**: typing.Optional[str]


# CreateProgramResponseTypeDef

### AdBreaks
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakTypeDef]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AudienceMedia
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AudienceMediaTypeDef]
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ClipRange
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ClipRangeTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DurationMillis
- **Type**: <class 'int'>
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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateSourceLocationRequestRequestTypeDef

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


# CreateVodSourceRequestRequestTypeDef

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


# DeleteChannelPolicyRequestRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelRequestRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteLiveSourceRequestRequestTypeDef

### LiveSourceName
- **Type**: <class 'str'>
- **Required**: Yes

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePlaybackConfigurationRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePrefetchScheduleRequestRequestTypeDef

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteProgramRequestRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteSourceLocationRequestRequestTypeDef

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteVodSourceRequestRequestTypeDef

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### VodSourceName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelRequestRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Audiences
- **Type**: typing.List[str]
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

### LogConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.LogConfigurationForChannelTypeDef'>
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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeLiveSourceRequestRequestTypeDef

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


# DescribeProgramRequestRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ProgramName
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeProgramResponseTypeDef

### AdBreaks
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakTypeDef]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AudienceMedia
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AudienceMediaTypeDef]
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ClipRange
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ClipRangeTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DurationMillis
- **Type**: <class 'int'>
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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSourceLocationRequestRequestTypeDef

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


# DescribeVodSourceRequestRequestTypeDef

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


# GetChannelPolicyRequestRequestTypeDef

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


# GetChannelScheduleRequestGetChannelSchedulePaginateTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Audience
- **Type**: typing.Optional[str]

### DurationMinutes
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# GetChannelScheduleRequestRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Audience
- **Type**: typing.Optional[str]

### DurationMinutes
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# GetChannelScheduleResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.ScheduleEntryTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPlaybackConfigurationRequestRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPrefetchScheduleRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchConsumptionTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Retrieval
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchRetrievalTypeDef'>
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


# HlsPlaylistSettingsPaginatorTypeDef

### AdMarkupType
- **Type**: typing.Optional[typing.List[typing.Literal['DATERANGE', 'SCTE35_ENHANCED']]]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]


# HlsPlaylistSettingsTypeDef

### AdMarkupType
- **Type**: typing.Optional[typing.Sequence[typing.Literal['DATERANGE', 'SCTE35_ENHANCED']]]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]


# HttpConfigurationTypeDef

### BaseUrl
- **Type**: <class 'str'>
- **Required**: Yes


# HttpPackageConfigurationTypeDef

### Path
- **Type**: <class 'str'>
- **Required**: Yes

### SourceGroup
- **Type**: <class 'str'>
- **Required**: Yes

### Type
- **Type**: typing.Literal['DASH', 'HLS']
- **Required**: Yes


# KeyValuePairTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# ListAlertsRequestListAlertsPaginateTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListAlertsRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelsRequestListChannelsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListChannelsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsResponsePaginatorTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.ChannelPaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListChannelsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.ChannelTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListLiveSourcesRequestListLiveSourcesPaginateTypeDef

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListLiveSourcesRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPlaybackConfigurationsRequestListPlaybackConfigurationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListPlaybackConfigurationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPlaybackConfigurationsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.PlaybackConfigurationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPrefetchSchedulesRequestListPrefetchSchedulesPaginateTypeDef

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### StreamId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListPrefetchSchedulesRequestRequestTypeDef

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### StreamId
- **Type**: typing.Optional[str]


# ListPrefetchSchedulesResponsePaginatorTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchSchedulePaginatorTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPrefetchSchedulesResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchScheduleTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListSourceLocationsRequestListSourceLocationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListSourceLocationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListSourceLocationsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.SourceLocationTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

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


# ListVodSourcesRequestListVodSourcesPaginateTypeDef

### SourceLocationName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.PaginatorConfigTypeDef]


# ListVodSourcesRequestRequestTypeDef

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

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


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


# PrefetchConsumptionPaginatorTypeDef

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### AvailMatchingCriteria
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AvailMatchingCriteriaTypeDef]]

### StartTime
- **Type**: typing.Optional[datetime.datetime]


# PrefetchConsumptionTypeDef

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### AvailMatchingCriteria
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AvailMatchingCriteriaTypeDef]]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# PrefetchRetrievalPaginatorTypeDef

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DynamicVariables
- **Type**: typing.Optional[typing.Dict[str, str]]

### StartTime
- **Type**: typing.Optional[datetime.datetime]


# PrefetchRetrievalTypeDef

### EndTime
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### DynamicVariables
- **Type**: typing.Optional[typing.Mapping[str, str]]

### StartTime
- **Type**: typing.Union[datetime.datetime, str, NoneType]


# PrefetchSchedulePaginatorTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Consumption
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchConsumptionPaginatorTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Retrieval
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchRetrievalPaginatorTypeDef'>
- **Required**: Yes

### StreamId
- **Type**: typing.Optional[str]


# PrefetchScheduleTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Consumption
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchConsumptionTypeDef'>
- **Required**: Yes

### Name
- **Type**: <class 'str'>
- **Required**: Yes

### PlaybackConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### Retrieval
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.PrefetchRetrievalTypeDef'>
- **Required**: Yes

### StreamId
- **Type**: typing.Optional[str]


# PutChannelPolicyRequestRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutPlaybackConfigurationRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.HlsPlaylistSettingsTypeDef]


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


# ResponseOutputItemPaginatorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.HlsPlaylistSettingsPaginatorTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.HlsPlaylistSettingsTypeDef]


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

### Audiences
- **Type**: typing.Optional[typing.List[str]]

### LiveSourceName
- **Type**: typing.Optional[str]

### ScheduleAdBreaks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.ScheduleAdBreakTypeDef]]

### ScheduleEntryType
- **Type**: typing.Optional[typing.Literal['ALTERNATE_MEDIA', 'FILLER_SLATE', 'PROGRAM']]

### VodSourceName
- **Type**: typing.Optional[str]


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

### SegmentNum
- **Type**: typing.Optional[int]

### SegmentationEventId
- **Type**: typing.Optional[int]

### SegmentationTypeId
- **Type**: typing.Optional[int]

### SegmentationUpid
- **Type**: typing.Optional[str]

### SegmentationUpidType
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


# StartChannelRequestRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# StopChannelRequestRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

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


# TimeSignalMessageTypeDef

### SegmentationDescriptors
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.SegmentationDescriptorTypeDef]]


# TransitionTypeDef

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


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateChannelRequestRequestTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Outputs
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.RequestOutputItemTypeDef]
- **Required**: Yes

### Audiences
- **Type**: typing.Optional[typing.Sequence[str]]

### FillerSlate
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.SlateSourceTypeDef]

### TimeShiftConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.TimeShiftConfigurationTypeDef]


# UpdateChannelResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Audiences
- **Type**: typing.List[str]
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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateLiveSourceRequestRequestTypeDef

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


# UpdateProgramRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakTypeDef]]

### AudienceMedia
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediatailor_classes.AudienceMediaTypeDef]]


# UpdateProgramResponseTypeDef

### AdBreaks
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AdBreakTypeDef]
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### AudienceMedia
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediatailor_classes.AudienceMediaTypeDef]
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ClipRange
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ClipRangeTypeDef'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### DurationMillis
- **Type**: <class 'int'>
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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediatailor_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateProgramScheduleConfigurationTypeDef

### ClipRange
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.ClipRangeTypeDef]

### Transition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediatailor_classes.UpdateProgramTransitionTypeDef]


# UpdateProgramTransitionTypeDef

### DurationMillis
- **Type**: typing.Optional[int]

### ScheduledStartTimeMillis
- **Type**: typing.Optional[int]


# UpdateSourceLocationRequestRequestTypeDef

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


# UpdateVodSourceRequestRequestTypeDef

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


