# Mediapackagev2 Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelHarvestJobRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### HarvestJobName
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: typing.Optional[str]


# ChannelGroupListConfigurationTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# ChannelListConfigurationTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### InputType
- **Type**: typing.Optional[typing.Literal['CMAF', 'HLS']]


# CreateChannelGroupRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateChannelGroupResponseTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### EgressDomain
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateChannelRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### InputType
- **Type**: typing.Optional[typing.Literal['CMAF', 'HLS']]

### Description
- **Type**: typing.Optional[str]

### InputSwitchConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.InputSwitchConfigurationTypeDef]

### OutputHeaderConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.OutputHeaderConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateChannelResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IngestEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.IngestEndpointTypeDef]
- **Required**: Yes

### InputType
- **Type**: typing.Literal['CMAF', 'HLS']
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### InputSwitchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.InputSwitchConfigurationTypeDef'>
- **Required**: Yes

### OutputHeaderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.OutputHeaderConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateDashManifestConfigurationTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationUnionTypeDef]

### MinUpdatePeriodSeconds
- **Type**: typing.Optional[int]

### MinBufferTimeSeconds
- **Type**: typing.Optional[int]

### SuggestedPresentationDelaySeconds
- **Type**: typing.Optional[int]

### SegmentTemplateFormat
- **Type**: typing.Optional[typing.Literal['NUMBER_WITH_TIMELINE']]

### PeriodTriggers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AVAILS', 'DRM_KEY_ROTATION', 'NONE', 'SOURCE_CHANGES', 'SOURCE_DISRUPTIONS']]]

### ScteDash
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ScteDashTypeDef]

### DrmSignaling
- **Type**: typing.Optional[typing.Literal['INDIVIDUAL', 'REFERENCED']]

### UtcTiming
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.DashUtcTimingTypeDef]


# CreateHarvestJobRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### HarvestedManifests
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedManifestsUnionTypeDef'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvesterScheduleConfigurationUnionTypeDef'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.DestinationTypeDef'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### HarvestJobName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateHarvestJobResponseTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.DestinationTypeDef'>
- **Required**: Yes

### HarvestJobName
- **Type**: <class 'str'>
- **Required**: Yes

### HarvestedManifests
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedManifestsOutputTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvesterScheduleConfigurationOutputTypeDef'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHlsManifestConfigurationTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### ChildManifestName
- **Type**: typing.Optional[str]

### ScteHls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ScteHlsTypeDef]

### StartTag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.StartTagTypeDef]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### ProgramDateTimeIntervalSeconds
- **Type**: typing.Optional[int]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationUnionTypeDef]


# CreateLowLatencyHlsManifestConfigurationTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### ChildManifestName
- **Type**: typing.Optional[str]

### ScteHls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ScteHlsTypeDef]

### StartTag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.StartTagTypeDef]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### ProgramDateTimeIntervalSeconds
- **Type**: typing.Optional[int]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationUnionTypeDef]


# CreateOriginEndpointRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerType
- **Type**: typing.Literal['CMAF', 'TS']
- **Required**: Yes

### Segment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.SegmentUnionTypeDef]

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### StartoverWindowSeconds
- **Type**: typing.Optional[int]

### HlsManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.CreateHlsManifestConfigurationTypeDef]]

### LowLatencyHlsManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.CreateLowLatencyHlsManifestConfigurationTypeDef]]

### DashManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.CreateDashManifestConfigurationTypeDef]]

### ForceEndpointErrorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateOriginEndpointResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerType
- **Type**: typing.Literal['CMAF', 'TS']
- **Required**: Yes

### Segment
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.SegmentOutputTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### StartoverWindowSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### HlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetHlsManifestConfigurationTypeDef]
- **Required**: Yes

### LowLatencyHlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetLowLatencyHlsManifestConfigurationTypeDef]
- **Required**: Yes

### DashManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetDashManifestConfigurationTypeDef]
- **Required**: Yes

### ForceEndpointErrorConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationOutputTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DashUtcTimingTypeDef

### TimingMode
- **Type**: typing.Optional[typing.Literal['HTTP_HEAD', 'HTTP_ISO', 'HTTP_XSDATE', 'UTC_DIRECT']]

### TimingSource
- **Type**: typing.Optional[str]


# DeleteChannelGroupRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelPolicyRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOriginEndpointPolicyRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOriginEndpointRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationTypeDef

### S3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.S3DestinationConfigTypeDef'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionContractConfigurationTypeDef

### PresetSpeke20Audio
- **Type**: typing.Literal['PRESET_AUDIO_1', 'PRESET_AUDIO_2', 'PRESET_AUDIO_3', 'SHARED', 'UNENCRYPTED']
- **Required**: Yes

### PresetSpeke20Video
- **Type**: typing.Literal['PRESET_VIDEO_1', 'PRESET_VIDEO_2', 'PRESET_VIDEO_3', 'PRESET_VIDEO_4', 'PRESET_VIDEO_5', 'PRESET_VIDEO_6', 'PRESET_VIDEO_7', 'PRESET_VIDEO_8', 'SHARED', 'UNENCRYPTED']
- **Required**: Yes


# EncryptionMethodTypeDef

### TsEncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_128', 'SAMPLE_AES']]

### CmafEncryptionMethod
- **Type**: typing.Optional[typing.Literal['CBCS', 'CENC']]


# EncryptionOutputTypeDef

### EncryptionMethod
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.EncryptionMethodTypeDef'>
- **Required**: Yes

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.SpekeKeyProviderOutputTypeDef'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]


# EncryptionTypeDef

### EncryptionMethod
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.EncryptionMethodTypeDef'>
- **Required**: Yes

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.SpekeKeyProviderTypeDef'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]


# FilterConfigurationOutputTypeDef

### ManifestFilter
- **Type**: typing.Optional[str]

### Start
- **Type**: typing.Optional[datetime.datetime]

### End
- **Type**: typing.Optional[datetime.datetime]

### TimeDelaySeconds
- **Type**: typing.Optional[int]

### ClipStartTime
- **Type**: typing.Optional[datetime.datetime]


# FilterConfigurationTypeDef

### ManifestFilter
- **Type**: typing.Optional[str]

### Start
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.TimestampTypeDef]

### End
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.TimestampTypeDef]

### TimeDelaySeconds
- **Type**: typing.Optional[int]

### ClipStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.TimestampTypeDef]


# FilterConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ForceEndpointErrorConfigurationOutputTypeDef

### EndpointErrorConditions
- **Type**: typing.Optional[typing.List[typing.Literal['INCOMPLETE_MANIFEST', 'MISSING_DRM_KEY', 'SLATE_INPUT', 'STALE_MANIFEST']]]


# ForceEndpointErrorConfigurationTypeDef

### EndpointErrorConditions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['INCOMPLETE_MANIFEST', 'MISSING_DRM_KEY', 'SLATE_INPUT', 'STALE_MANIFEST']]]


# ForceEndpointErrorConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetChannelGroupRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelGroupResponseTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### EgressDomain
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChannelPolicyRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelPolicyResponseTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChannelRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IngestEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.IngestEndpointTypeDef]
- **Required**: Yes

### InputType
- **Type**: typing.Literal['CMAF', 'HLS']
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### InputSwitchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.InputSwitchConfigurationTypeDef'>
- **Required**: Yes

### OutputHeaderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.OutputHeaderConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetDashManifestConfigurationTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationOutputTypeDef]

### MinUpdatePeriodSeconds
- **Type**: typing.Optional[int]

### MinBufferTimeSeconds
- **Type**: typing.Optional[int]

### SuggestedPresentationDelaySeconds
- **Type**: typing.Optional[int]

### SegmentTemplateFormat
- **Type**: typing.Optional[typing.Literal['NUMBER_WITH_TIMELINE']]

### PeriodTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['AVAILS', 'DRM_KEY_ROTATION', 'NONE', 'SOURCE_CHANGES', 'SOURCE_DISRUPTIONS']]]

### ScteDash
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ScteDashTypeDef]

### DrmSignaling
- **Type**: typing.Optional[typing.Literal['INDIVIDUAL', 'REFERENCED']]

### UtcTiming
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.DashUtcTimingTypeDef]


# GetHarvestJobRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### HarvestJobName
- **Type**: <class 'str'>
- **Required**: Yes


# GetHarvestJobRequestWaitTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### HarvestJobName
- **Type**: <class 'str'>
- **Required**: Yes

### WaiterConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.WaiterConfigTypeDef]


# GetHarvestJobResponseTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.DestinationTypeDef'>
- **Required**: Yes

### HarvestJobName
- **Type**: <class 'str'>
- **Required**: Yes

### HarvestedManifests
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedManifestsOutputTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvesterScheduleConfigurationOutputTypeDef'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']
- **Required**: Yes

### ErrorMessage
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetHlsManifestConfigurationTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ChildManifestName
- **Type**: typing.Optional[str]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### ProgramDateTimeIntervalSeconds
- **Type**: typing.Optional[int]

### ScteHls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ScteHlsTypeDef]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationOutputTypeDef]

### StartTag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.StartTagTypeDef]


# GetLowLatencyHlsManifestConfigurationTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ChildManifestName
- **Type**: typing.Optional[str]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### ProgramDateTimeIntervalSeconds
- **Type**: typing.Optional[int]

### ScteHls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ScteHlsTypeDef]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationOutputTypeDef]

### StartTag
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.StartTagTypeDef]


# GetOriginEndpointPolicyRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# GetOriginEndpointPolicyResponseTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetOriginEndpointRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# GetOriginEndpointResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerType
- **Type**: typing.Literal['CMAF', 'TS']
- **Required**: Yes

### Segment
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.SegmentOutputTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### StartoverWindowSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### HlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetHlsManifestConfigurationTypeDef]
- **Required**: Yes

### LowLatencyHlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetLowLatencyHlsManifestConfigurationTypeDef]
- **Required**: Yes

### DashManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetDashManifestConfigurationTypeDef]
- **Required**: Yes

### ForceEndpointErrorConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationOutputTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# HarvestJobTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.DestinationTypeDef'>
- **Required**: Yes

### HarvestJobName
- **Type**: <class 'str'>
- **Required**: Yes

### HarvestedManifests
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedManifestsOutputTypeDef'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvesterScheduleConfigurationOutputTypeDef'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ErrorMessage
- **Type**: typing.Optional[str]

### ETag
- **Type**: typing.Optional[str]


# HarvestedDashManifestTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes


# HarvestedHlsManifestTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes


# HarvestedLowLatencyHlsManifestTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes


# HarvestedManifestsOutputTypeDef

### HlsManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedHlsManifestTypeDef]]

### DashManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedDashManifestTypeDef]]

### LowLatencyHlsManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedLowLatencyHlsManifestTypeDef]]


# HarvestedManifestsTypeDef

### HlsManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedHlsManifestTypeDef]]

### DashManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedDashManifestTypeDef]]

### LowLatencyHlsManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedLowLatencyHlsManifestTypeDef]]


# HarvestedManifestsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HarvesterScheduleConfigurationOutputTypeDef

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# HarvesterScheduleConfigurationTypeDef

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.TimestampTypeDef'>
- **Required**: Yes


# HarvesterScheduleConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IngestEndpointTypeDef

### Id
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# InputSwitchConfigurationTypeDef

### MQCSInputSwitching
- **Type**: typing.Optional[bool]


# ListChannelGroupsRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.PaginatorConfigTypeDef]


# ListChannelGroupsRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelGroupsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.ChannelGroupListConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsRequestPaginateTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.PaginatorConfigTypeDef]


# ListChannelsRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.ChannelListConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDashManifestConfigurationTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: typing.Optional[str]


# ListHarvestJobsRequestPaginateTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: typing.Optional[str]

### OriginEndpointName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.PaginatorConfigTypeDef]


# ListHarvestJobsRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: typing.Optional[str]

### OriginEndpointName
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['CANCELLED', 'COMPLETED', 'FAILED', 'IN_PROGRESS', 'QUEUED']]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHarvestJobsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestJobTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHlsManifestConfigurationTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### ChildManifestName
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# ListLowLatencyHlsManifestConfigurationTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### ChildManifestName
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# ListOriginEndpointsRequestPaginateTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.PaginatorConfigTypeDef]


# ListOriginEndpointsRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOriginEndpointsResponseTypeDef

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.OriginEndpointListConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# OriginEndpointListConfigurationTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerType
- **Type**: typing.Literal['CMAF', 'TS']
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[datetime.datetime]

### ModifiedAt
- **Type**: typing.Optional[datetime.datetime]

### HlsManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.ListHlsManifestConfigurationTypeDef]]

### LowLatencyHlsManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.ListLowLatencyHlsManifestConfigurationTypeDef]]

### DashManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.ListDashManifestConfigurationTypeDef]]

### ForceEndpointErrorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationOutputTypeDef]


# OutputHeaderConfigurationTypeDef

### PublishMQCS
- **Type**: typing.Optional[bool]


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutChannelPolicyRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutOriginEndpointPolicyRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
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


# S3DestinationConfigTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPath
- **Type**: <class 'str'>
- **Required**: Yes


# ScteDashTypeDef

### AdMarkerDash
- **Type**: typing.Optional[typing.Literal['BINARY', 'XML']]


# ScteHlsTypeDef

### AdMarkerHls
- **Type**: typing.Optional[typing.Literal['DATERANGE']]


# ScteOutputTypeDef

### ScteFilter
- **Type**: typing.Optional[typing.List[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROGRAM', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]


# ScteTypeDef

### ScteFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROGRAM', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]


# SegmentOutputTypeDef

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### SegmentName
- **Type**: typing.Optional[str]

### TsUseAudioRenditionGroup
- **Type**: typing.Optional[bool]

### IncludeIframeOnlyStreams
- **Type**: typing.Optional[bool]

### TsIncludeDvbSubtitles
- **Type**: typing.Optional[bool]

### Scte
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ScteOutputTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.EncryptionOutputTypeDef]


# SegmentTypeDef

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### SegmentName
- **Type**: typing.Optional[str]

### TsUseAudioRenditionGroup
- **Type**: typing.Optional[bool]

### IncludeIframeOnlyStreams
- **Type**: typing.Optional[bool]

### TsIncludeDvbSubtitles
- **Type**: typing.Optional[bool]

### Scte
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ScteTypeDef]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.EncryptionTypeDef]


# SegmentUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SpekeKeyProviderOutputTypeDef

### EncryptionContractConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.EncryptionContractConfigurationTypeDef'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DrmSystems
- **Type**: typing.List[typing.Literal['CLEAR_KEY_AES_128', 'FAIRPLAY', 'IRDETO', 'PLAYREADY', 'WIDEVINE']]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes


# SpekeKeyProviderTypeDef

### EncryptionContractConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.EncryptionContractConfigurationTypeDef'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DrmSystems
- **Type**: typing.Sequence[typing.Literal['CLEAR_KEY_AES_128', 'FAIRPLAY', 'IRDETO', 'PLAYREADY', 'WIDEVINE']]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes


# StartTagTypeDef

### TimeOffset
- **Type**: <class 'float'>
- **Required**: Yes

### Precise
- **Type**: typing.Optional[bool]


# TagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateChannelGroupRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateChannelGroupResponseTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### EgressDomain
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateChannelRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### InputSwitchConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.InputSwitchConfigurationTypeDef]

### OutputHeaderConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.OutputHeaderConfigurationTypeDef]


# UpdateChannelResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### IngestEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.IngestEndpointTypeDef]
- **Required**: Yes

### InputType
- **Type**: typing.Literal['CMAF', 'HLS']
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### InputSwitchConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.InputSwitchConfigurationTypeDef'>
- **Required**: Yes

### OutputHeaderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.OutputHeaderConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateOriginEndpointRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerType
- **Type**: typing.Literal['CMAF', 'TS']
- **Required**: Yes

### Segment
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.SegmentUnionTypeDef]

### Description
- **Type**: typing.Optional[str]

### StartoverWindowSeconds
- **Type**: typing.Optional[int]

### HlsManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.CreateHlsManifestConfigurationTypeDef]]

### LowLatencyHlsManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.CreateLowLatencyHlsManifestConfigurationTypeDef]]

### DashManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.CreateDashManifestConfigurationTypeDef]]

### ForceEndpointErrorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationUnionTypeDef]

### ETag
- **Type**: typing.Optional[str]


# UpdateOriginEndpointResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes

### ContainerType
- **Type**: typing.Literal['CMAF', 'TS']
- **Required**: Yes

### Segment
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.SegmentOutputTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### ModifiedAt
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### StartoverWindowSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### HlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetHlsManifestConfigurationTypeDef]
- **Required**: Yes

### LowLatencyHlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetLowLatencyHlsManifestConfigurationTypeDef]
- **Required**: Yes

### ForceEndpointErrorConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationOutputTypeDef'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### DashManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetDashManifestConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# WaiterConfigTypeDef

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


