# Pydantic Models in mediapackagev2_classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# CreateChannelGroupRequestRequestTypeDef

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


# CreateChannelRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationTypeDef]

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


# CreateHlsManifestConfigurationTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### ChildManifestName
- **Type**: typing.Optional[str]

### ScteHls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ScteHlsTypeDef]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### ProgramDateTimeIntervalSeconds
- **Type**: typing.Optional[int]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationTypeDef]


# CreateLowLatencyHlsManifestConfigurationTypeDef

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### ChildManifestName
- **Type**: typing.Optional[str]

### ScteHls
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ScteHlsTypeDef]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### ProgramDateTimeIntervalSeconds
- **Type**: typing.Optional[int]

### FilterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.FilterConfigurationTypeDef]


# CreateOriginEndpointRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.SegmentTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationTypeDef]

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


# DeleteChannelGroupRequestRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelPolicyRequestRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteChannelRequestRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOriginEndpointPolicyRequestRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOriginEndpointRequestRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointName
- **Type**: <class 'str'>
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


# FilterConfigurationTypeDef

### ManifestFilter
- **Type**: typing.Optional[str]

### Start
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### End
- **Type**: typing.Union[datetime.datetime, str, NoneType]

### TimeDelaySeconds
- **Type**: typing.Optional[int]


# ForceEndpointErrorConfigurationExtraOutputTypeDef

### EndpointErrorConditions
- **Type**: typing.Optional[typing.List[typing.Literal['INCOMPLETE_MANIFEST', 'MISSING_DRM_KEY', 'SLATE_INPUT', 'STALE_MANIFEST']]]


# ForceEndpointErrorConfigurationOutputTypeDef

### EndpointErrorConditions
- **Type**: typing.Optional[typing.List[typing.Literal['INCOMPLETE_MANIFEST', 'MISSING_DRM_KEY', 'SLATE_INPUT', 'STALE_MANIFEST']]]


# ForceEndpointErrorConfigurationTypeDef

### EndpointErrorConditions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['INCOMPLETE_MANIFEST', 'MISSING_DRM_KEY', 'SLATE_INPUT', 'STALE_MANIFEST']]]


# GetChannelGroupRequestRequestTypeDef

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


# GetChannelPolicyRequestRequestTypeDef

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


# GetChannelRequestRequestTypeDef

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


# GetOriginEndpointPolicyRequestRequestTypeDef

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


# GetOriginEndpointRequestRequestTypeDef

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


# IngestEndpointTypeDef

### Id
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# ListChannelGroupsRequestListChannelGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.PaginatorConfigTypeDef]


# ListChannelGroupsRequestRequestTypeDef

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


# ListChannelsRequestListChannelsPaginateTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.PaginatorConfigTypeDef]


# ListChannelsRequestRequestTypeDef

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


# ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.PaginatorConfigTypeDef]


# ListOriginEndpointsRequestRequestTypeDef

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


# ListTagsForResourceRequestRequestTypeDef

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


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PutChannelPolicyRequestRequestTypeDef

### ChannelGroupName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### Policy
- **Type**: <class 'str'>
- **Required**: Yes


# PutOriginEndpointPolicyRequestRequestTypeDef

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


# SpekeKeyProviderOutputTypeDef

### EncryptionContractConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.EncryptionContractConfigurationTypeDef'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### DrmSystems
- **Type**: typing.List[typing.Literal['CLEAR_KEY_AES_128', 'FAIRPLAY', 'PLAYREADY', 'WIDEVINE']]
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
- **Type**: typing.Sequence[typing.Literal['CLEAR_KEY_AES_128', 'FAIRPLAY', 'PLAYREADY', 'WIDEVINE']]
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateChannelGroupRequestRequestTypeDef

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


# UpdateChannelRequestRequestTypeDef

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

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackagev2_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateOriginEndpointRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.SegmentTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackagev2_classes.ForceEndpointErrorConfigurationTypeDef]

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


