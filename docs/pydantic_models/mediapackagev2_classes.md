# Mediapackagev2 Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CancelHarvestJobRequest

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


# ChannelGroupListConfiguration

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


# ChannelListConfiguration

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


# CreateChannelGroupRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateChannelGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateChannelRequest

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
- **Type**: <class 'NoneType'>

### OutputHeaderConfiguration
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateChannelResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.IngestEndpoint]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.InputSwitchConfiguration'>
- **Required**: Yes

### OutputHeaderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.OutputHeaderConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateDashManifestConfiguration

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationUnion]

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
- **Type**: <class 'NoneType'>

### DrmSignaling
- **Type**: typing.Optional[typing.Literal['INDIVIDUAL', 'REFERENCED']]

### UtcTiming
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.DashUtcTiming]


# CreateHarvestJobRequest

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedManifestsUnion'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvesterScheduleConfigurationUnion'>
- **Required**: Yes

### Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.Destination'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### ClientToken
- **Type**: typing.Optional[str]

### HarvestJobName
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateHarvestJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.Destination'>
- **Required**: Yes

### HarvestJobName
- **Type**: <class 'str'>
- **Required**: Yes

### HarvestedManifests
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedManifestsOutput'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvesterScheduleConfigurationOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHlsManifestConfiguration

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### ChildManifestName
- **Type**: typing.Optional[str]

### ScteHls
- **Type**: <class 'NoneType'>

### StartTag
- **Type**: <class 'NoneType'>

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### ProgramDateTimeIntervalSeconds
- **Type**: typing.Optional[int]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationUnion]


# CreateLowLatencyHlsManifestConfiguration

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### ChildManifestName
- **Type**: typing.Optional[str]

### ScteHls
- **Type**: <class 'NoneType'>

### StartTag
- **Type**: <class 'NoneType'>

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### ProgramDateTimeIntervalSeconds
- **Type**: typing.Optional[int]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationUnion]


# CreateOriginEndpointRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.SegmentUnion]

### ClientToken
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### StartoverWindowSeconds
- **Type**: typing.Optional[int]

### HlsManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.CreateHlsManifestConfiguration]]

### LowLatencyHlsManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.CreateLowLatencyHlsManifestConfiguration]]

### DashManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.CreateDashManifestConfiguration]]

### ForceEndpointErrorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationUnion]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateOriginEndpointResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.SegmentOutput'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetHlsManifestConfiguration]
- **Required**: Yes

### LowLatencyHlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetLowLatencyHlsManifestConfiguration]
- **Required**: Yes

### DashManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetDashManifestConfiguration]
- **Required**: Yes

### ForceEndpointErrorConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationOutput'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# DashUtcTiming

### TimingMode
- **Type**: typing.Optional[typing.Literal['HTTP_HEAD', 'HTTP_ISO', 'HTTP_XSDATE', 'UTC_DIRECT']]

### TimingSource
- **Type**: typing.Optional[str]


# DeleteChannelGroupRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelPolicyRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOriginEndpointPolicyRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOriginEndpointRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# Destination

### S3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.S3DestinationConfig'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# Encryption

### EncryptionMethod
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.EncryptionMethod'>
- **Required**: Yes

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.SpekeKeyProvider'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]


# EncryptionContractConfiguration

### PresetSpeke20Audio
- **Type**: typing.Literal['PRESET_AUDIO_1', 'PRESET_AUDIO_2', 'PRESET_AUDIO_3', 'SHARED', 'UNENCRYPTED']
- **Required**: Yes

### PresetSpeke20Video
- **Type**: typing.Literal['PRESET_VIDEO_1', 'PRESET_VIDEO_2', 'PRESET_VIDEO_3', 'PRESET_VIDEO_4', 'PRESET_VIDEO_5', 'PRESET_VIDEO_6', 'PRESET_VIDEO_7', 'PRESET_VIDEO_8', 'SHARED', 'UNENCRYPTED']
- **Required**: Yes


# EncryptionMethod

### TsEncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_128', 'SAMPLE_AES']]

### CmafEncryptionMethod
- **Type**: typing.Optional[typing.Literal['CBCS', 'CENC']]


# EncryptionOutput

### EncryptionMethod
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.EncryptionMethod'>
- **Required**: Yes

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.SpekeKeyProviderOutput'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]


# FilterConfiguration

### ManifestFilter
- **Type**: typing.Optional[str]

### Start
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.Timestamp]

### End
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.Timestamp]

### TimeDelaySeconds
- **Type**: typing.Optional[int]

### ClipStartTime
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.Timestamp]


# FilterConfigurationOutput

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


# FilterConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ForceEndpointErrorConfiguration

### EndpointErrorConditions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['INCOMPLETE_MANIFEST', 'MISSING_DRM_KEY', 'SLATE_INPUT', 'STALE_MANIFEST']]]


# ForceEndpointErrorConfigurationOutput

### EndpointErrorConditions
- **Type**: typing.Optional[typing.List[typing.Literal['INCOMPLETE_MANIFEST', 'MISSING_DRM_KEY', 'SLATE_INPUT', 'STALE_MANIFEST']]]


# ForceEndpointErrorConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# GetChannelGroupRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# GetChannelPolicyRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelPolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# GetChannelRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.IngestEndpoint]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.InputSwitchConfiguration'>
- **Required**: Yes

### OutputHeaderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.OutputHeaderConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# GetDashManifestConfiguration

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationOutput]

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
- **Type**: <class 'NoneType'>

### DrmSignaling
- **Type**: typing.Optional[typing.Literal['INDIVIDUAL', 'REFERENCED']]

### UtcTiming
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.DashUtcTiming]


# GetHarvestJobRequest

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


# GetHarvestJobRequestWait

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
- **Type**: <class 'NoneType'>


# GetHarvestJobResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.Destination'>
- **Required**: Yes

### HarvestJobName
- **Type**: <class 'str'>
- **Required**: Yes

### HarvestedManifests
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedManifestsOutput'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvesterScheduleConfigurationOutput'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# GetHlsManifestConfiguration

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
- **Type**: <class 'NoneType'>

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationOutput]

### StartTag
- **Type**: <class 'NoneType'>


# GetLowLatencyHlsManifestConfiguration

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
- **Type**: <class 'NoneType'>

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationOutput]

### StartTag
- **Type**: <class 'NoneType'>


# GetOriginEndpointPolicyRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# GetOriginEndpointPolicyResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# GetOriginEndpointRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# GetOriginEndpointResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.SegmentOutput'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetHlsManifestConfiguration]
- **Required**: Yes

### LowLatencyHlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetLowLatencyHlsManifestConfiguration]
- **Required**: Yes

### DashManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetDashManifestConfiguration]
- **Required**: Yes

### ForceEndpointErrorConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationOutput'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# HarvestJob

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.Destination'>
- **Required**: Yes

### HarvestJobName
- **Type**: <class 'str'>
- **Required**: Yes

### HarvestedManifests
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedManifestsOutput'>
- **Required**: Yes

### ScheduleConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvesterScheduleConfigurationOutput'>
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


# HarvestedDashManifest

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes


# HarvestedHlsManifest

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes


# HarvestedLowLatencyHlsManifest

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes


# HarvestedManifests

### HlsManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedHlsManifest]]

### DashManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedDashManifest]]

### LowLatencyHlsManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedLowLatencyHlsManifest]]


# HarvestedManifestsOutput

### HlsManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedHlsManifest]]

### DashManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedDashManifest]]

### LowLatencyHlsManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestedLowLatencyHlsManifest]]


# HarvestedManifestsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# HarvesterScheduleConfiguration

### StartTime
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.Timestamp'>
- **Required**: Yes

### EndTime
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.Timestamp'>
- **Required**: Yes


# HarvesterScheduleConfigurationOutput

### StartTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# HarvesterScheduleConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# IngestEndpoint

### Id
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# InputSwitchConfiguration

### MQCSInputSwitching
- **Type**: typing.Optional[bool]


# ListChannelGroupsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.PaginatorConfig]


# ListChannelGroupsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.ChannelGroupListConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsRequestPaginate

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.PaginatorConfig]


# ListChannelsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.ChannelListConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListDashManifestConfiguration

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: typing.Optional[str]


# ListHarvestJobsRequest

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


# ListHarvestJobsRequestPaginate

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.PaginatorConfig]


# ListHarvestJobsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.HarvestJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHlsManifestConfiguration

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### ChildManifestName
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# ListLowLatencyHlsManifestConfiguration

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### ChildManifestName
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# ListOriginEndpointsRequest

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


# ListOriginEndpointsRequestPaginate

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.PaginatorConfig]


# ListOriginEndpointsResponse

### Items
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.OriginEndpointListConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# OriginEndpointListConfiguration

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.ListHlsManifestConfiguration]]

### LowLatencyHlsManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.ListLowLatencyHlsManifestConfiguration]]

### DashManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.ListDashManifestConfiguration]]

### ForceEndpointErrorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationOutput]


# OutputHeaderConfiguration

### PublishMQCS
- **Type**: typing.Optional[bool]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutChannelPolicyRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutOriginEndpointPolicyRequest

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


# S3DestinationConfig

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationPath
- **Type**: <class 'str'>
- **Required**: Yes


# Scte

### ScteFilter
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROGRAM', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]


# ScteDash

### AdMarkerDash
- **Type**: typing.Optional[typing.Literal['BINARY', 'XML']]


# ScteHls

### AdMarkerHls
- **Type**: typing.Optional[typing.Literal['DATERANGE']]


# ScteOutput

### ScteFilter
- **Type**: typing.Optional[typing.List[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROGRAM', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]


# Segment

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
- **Type**: <class 'NoneType'>

### Encryption
- **Type**: <class 'NoneType'>


# SegmentOutput

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ScteOutput]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.EncryptionOutput]


# SegmentUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SpekeKeyProvider

### EncryptionContractConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.EncryptionContractConfiguration'>
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


# SpekeKeyProviderOutput

### EncryptionContractConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.EncryptionContractConfiguration'>
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


# StartTag

### TimeOffset
- **Type**: <class 'float'>
- **Required**: Yes

### Precise
- **Type**: typing.Optional[bool]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateChannelGroupRequest

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ETag
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]


# UpdateChannelGroupResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateChannelRequest

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
- **Type**: <class 'NoneType'>

### OutputHeaderConfiguration
- **Type**: <class 'NoneType'>


# UpdateChannelResponse

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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.IngestEndpoint]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.InputSwitchConfiguration'>
- **Required**: Yes

### OutputHeaderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.OutputHeaderConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateOriginEndpointRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.SegmentUnion]

### Description
- **Type**: typing.Optional[str]

### StartoverWindowSeconds
- **Type**: typing.Optional[int]

### HlsManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.CreateHlsManifestConfiguration]]

### LowLatencyHlsManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.CreateLowLatencyHlsManifestConfiguration]]

### DashManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackagev2_classes.CreateDashManifestConfiguration]]

### ForceEndpointErrorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationUnion]

### ETag
- **Type**: typing.Optional[str]


# UpdateOriginEndpointResponse

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.SegmentOutput'>
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
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetHlsManifestConfiguration]
- **Required**: Yes

### LowLatencyHlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetLowLatencyHlsManifestConfiguration]
- **Required**: Yes

### ForceEndpointErrorConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationOutput'>
- **Required**: Yes

### ETag
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### DashManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackagev2_classes.GetDashManifestConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadata'>
- **Required**: Yes


# WaiterConfig

### Delay
- **Type**: typing.Optional[int]

### MaxAttempts
- **Type**: typing.Optional[int]


