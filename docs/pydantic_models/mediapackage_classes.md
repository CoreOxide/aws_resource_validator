# Mediapackage Classes

# Authorization

### CdnIdentifierSecret
- **Type**: <class 'str'>
- **Required**: Yes

### SecretsRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# Channel

### Arn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EgressAccessLogs
- **Type**: <class 'NoneType'>

### HlsIngest
- **Type**: <class 'NoneType'>

### Id
- **Type**: typing.Optional[str]

### IngressAccessLogs
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CmafEncryption

### SpekeKeyProvider
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.SpekeKeyProvider, aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.SpekeKeyProviderOutput]
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_CTR', 'SAMPLE_AES']]

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]


# CmafEncryptionOutput

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.SpekeKeyProviderOutput'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_CTR', 'SAMPLE_AES']]

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]


# CmafPackage

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.CmafEncryptionOutput]

### HlsManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsManifest]]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### SegmentPrefix
- **Type**: typing.Optional[str]

### StreamSelection
- **Type**: <class 'NoneType'>


# CmafPackageCreateOrUpdateParameters

### Encryption
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.CmafEncryption, aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.CmafEncryptionOutput, NoneType]

### HlsManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsManifestCreateOrUpdateParameters]]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### SegmentPrefix
- **Type**: typing.Optional[str]

### StreamSelection
- **Type**: <class 'NoneType'>


# ConfigureLogsRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'NoneType'>

### IngressAccessLogs
- **Type**: <class 'NoneType'>


# ConfigureLogsResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.EgressAccessLogs'>
- **Required**: Yes

### HlsIngest
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsIngest'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.IngressAccessLogs'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes


# CreateChannelRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateChannelResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.EgressAccessLogs'>
- **Required**: Yes

### HlsIngest
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsIngest'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.IngressAccessLogs'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes


# CreateHarvestJobRequest

### EndTime
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### S3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.S3Destination'>
- **Required**: Yes

### StartTime
- **Type**: <class 'str'>
- **Required**: Yes


# CreateHarvestJobResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### S3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.S3Destination'>
- **Required**: Yes

### StartTime
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes


# CreateOriginEndpointRequest

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'NoneType'>

### CmafPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.CmafPackageCreateOrUpdateParameters]

### DashPackage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.DashPackage, aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.DashPackageOutput, NoneType]

### Description
- **Type**: typing.Optional[str]

### HlsPackage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsPackage, aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsPackageOutput, NoneType]

### ManifestName
- **Type**: typing.Optional[str]

### MssPackage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.MssPackage, aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.MssPackageOutput, NoneType]

### Origination
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### StartoverWindowSeconds
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TimeDelaySeconds
- **Type**: typing.Optional[int]

### Whitelist
- **Type**: typing.Optional[typing.List[str]]


# CreateOriginEndpointResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.Authorization'>
- **Required**: Yes

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### CmafPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.CmafPackage'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DashPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.DashPackageOutput'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### HlsPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsPackageOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### MssPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.MssPackageOutput'>
- **Required**: Yes

### Origination
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### StartoverWindowSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TimeDelaySeconds
- **Type**: <class 'int'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### Whitelist
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes


# DashEncryption

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.SpekeKeyProvider'>
- **Required**: Yes

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]


# DashEncryptionOutput

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.SpekeKeyProviderOutput'>
- **Required**: Yes

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]


# DashPackage

### AdTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]

### AdsOnDeliveryRestrictions
- **Type**: typing.Optional[typing.Literal['BOTH', 'NONE', 'RESTRICTED', 'UNRESTRICTED']]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.DashEncryption]

### IncludeIframeOnlyStream
- **Type**: typing.Optional[bool]

### ManifestLayout
- **Type**: typing.Optional[typing.Literal['COMPACT', 'DRM_TOP_LEVEL_COMPACT', 'FULL']]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### MinBufferTimeSeconds
- **Type**: typing.Optional[int]

### MinUpdatePeriodSeconds
- **Type**: typing.Optional[int]

### PeriodTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['ADS']]]

### Profile
- **Type**: typing.Optional[typing.Literal['DVB_DASH_2014', 'HBBTV_1_5', 'HYBRIDCAST', 'NONE']]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### SegmentTemplateFormat
- **Type**: typing.Optional[typing.Literal['NUMBER_WITH_DURATION', 'NUMBER_WITH_TIMELINE', 'TIME_WITH_TIMELINE']]

### StreamSelection
- **Type**: <class 'NoneType'>

### SuggestedPresentationDelaySeconds
- **Type**: typing.Optional[int]

### UtcTiming
- **Type**: typing.Optional[typing.Literal['HTTP-HEAD', 'HTTP-ISO', 'HTTP-XSDATE', 'NONE']]

### UtcTimingUri
- **Type**: typing.Optional[str]


# DashPackageOutput

### AdTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]

### AdsOnDeliveryRestrictions
- **Type**: typing.Optional[typing.Literal['BOTH', 'NONE', 'RESTRICTED', 'UNRESTRICTED']]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.DashEncryptionOutput]

### IncludeIframeOnlyStream
- **Type**: typing.Optional[bool]

### ManifestLayout
- **Type**: typing.Optional[typing.Literal['COMPACT', 'DRM_TOP_LEVEL_COMPACT', 'FULL']]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### MinBufferTimeSeconds
- **Type**: typing.Optional[int]

### MinUpdatePeriodSeconds
- **Type**: typing.Optional[int]

### PeriodTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['ADS']]]

### Profile
- **Type**: typing.Optional[typing.Literal['DVB_DASH_2014', 'HBBTV_1_5', 'HYBRIDCAST', 'NONE']]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### SegmentTemplateFormat
- **Type**: typing.Optional[typing.Literal['NUMBER_WITH_DURATION', 'NUMBER_WITH_TIMELINE', 'TIME_WITH_TIMELINE']]

### StreamSelection
- **Type**: <class 'NoneType'>

### SuggestedPresentationDelaySeconds
- **Type**: typing.Optional[int]

### UtcTiming
- **Type**: typing.Optional[typing.Literal['HTTP-HEAD', 'HTTP-ISO', 'HTTP-XSDATE', 'NONE']]

### UtcTimingUri
- **Type**: typing.Optional[str]


# DeleteChannelRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOriginEndpointRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.EgressAccessLogs'>
- **Required**: Yes

### HlsIngest
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsIngest'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.IngressAccessLogs'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeHarvestJobRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHarvestJobResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### EndTime
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpointId
- **Type**: <class 'str'>
- **Required**: Yes

### S3Destination
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.S3Destination'>
- **Required**: Yes

### StartTime
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeOriginEndpointRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOriginEndpointResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.Authorization'>
- **Required**: Yes

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### CmafPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.CmafPackage'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DashPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.DashPackageOutput'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### HlsPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsPackageOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### MssPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.MssPackageOutput'>
- **Required**: Yes

### Origination
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### StartoverWindowSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TimeDelaySeconds
- **Type**: <class 'int'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### Whitelist
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes


# EgressAccessLogs

### LogGroupName
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionContractConfiguration

### PresetSpeke20Audio
- **Type**: typing.Literal['PRESET-AUDIO-1', 'PRESET-AUDIO-2', 'PRESET-AUDIO-3', 'SHARED', 'UNENCRYPTED']
- **Required**: Yes

### PresetSpeke20Video
- **Type**: typing.Literal['PRESET-VIDEO-1', 'PRESET-VIDEO-2', 'PRESET-VIDEO-3', 'PRESET-VIDEO-4', 'PRESET-VIDEO-5', 'PRESET-VIDEO-6', 'PRESET-VIDEO-7', 'PRESET-VIDEO-8', 'SHARED', 'UNENCRYPTED']
- **Required**: Yes


# HarvestJob

### Arn
- **Type**: typing.Optional[str]

### ChannelId
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### EndTime
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### OriginEndpointId
- **Type**: typing.Optional[str]

### S3Destination
- **Type**: <class 'NoneType'>

### StartTime
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]


# HlsEncryption

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.SpekeKeyProvider'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_128', 'SAMPLE_AES']]

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]

### RepeatExtXKey
- **Type**: typing.Optional[bool]


# HlsEncryptionOutput

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.SpekeKeyProviderOutput'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_128', 'SAMPLE_AES']]

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]

### RepeatExtXKey
- **Type**: typing.Optional[bool]


# HlsIngest

### IngestEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.IngestEndpoint]]


# HlsManifest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AdMarkers
- **Type**: typing.Optional[typing.Literal['DATERANGE', 'NONE', 'PASSTHROUGH', 'SCTE35_ENHANCED']]

### IncludeIframeOnlyStream
- **Type**: typing.Optional[bool]

### ManifestName
- **Type**: typing.Optional[str]

### PlaylistType
- **Type**: typing.Optional[typing.Literal['EVENT', 'NONE', 'VOD']]

### PlaylistWindowSeconds
- **Type**: typing.Optional[int]

### ProgramDateTimeIntervalSeconds
- **Type**: typing.Optional[int]

### Url
- **Type**: typing.Optional[str]

### AdTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]

### AdsOnDeliveryRestrictions
- **Type**: typing.Optional[typing.Literal['BOTH', 'NONE', 'RESTRICTED', 'UNRESTRICTED']]


# HlsManifestCreateOrUpdateParameters

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AdMarkers
- **Type**: typing.Optional[typing.Literal['DATERANGE', 'NONE', 'PASSTHROUGH', 'SCTE35_ENHANCED']]

### AdTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]

### AdsOnDeliveryRestrictions
- **Type**: typing.Optional[typing.Literal['BOTH', 'NONE', 'RESTRICTED', 'UNRESTRICTED']]

### IncludeIframeOnlyStream
- **Type**: typing.Optional[bool]

### ManifestName
- **Type**: typing.Optional[str]

### PlaylistType
- **Type**: typing.Optional[typing.Literal['EVENT', 'NONE', 'VOD']]

### PlaylistWindowSeconds
- **Type**: typing.Optional[int]

### ProgramDateTimeIntervalSeconds
- **Type**: typing.Optional[int]


# HlsPackage

### AdMarkers
- **Type**: typing.Optional[typing.Literal['DATERANGE', 'NONE', 'PASSTHROUGH', 'SCTE35_ENHANCED']]

### AdTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]

### AdsOnDeliveryRestrictions
- **Type**: typing.Optional[typing.Literal['BOTH', 'NONE', 'RESTRICTED', 'UNRESTRICTED']]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsEncryption]

### IncludeDvbSubtitles
- **Type**: typing.Optional[bool]

### IncludeIframeOnlyStream
- **Type**: typing.Optional[bool]

### PlaylistType
- **Type**: typing.Optional[typing.Literal['EVENT', 'NONE', 'VOD']]

### PlaylistWindowSeconds
- **Type**: typing.Optional[int]

### ProgramDateTimeIntervalSeconds
- **Type**: typing.Optional[int]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### StreamSelection
- **Type**: <class 'NoneType'>

### UseAudioRenditionGroup
- **Type**: typing.Optional[bool]


# HlsPackageOutput

### AdMarkers
- **Type**: typing.Optional[typing.Literal['DATERANGE', 'NONE', 'PASSTHROUGH', 'SCTE35_ENHANCED']]

### AdTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]

### AdsOnDeliveryRestrictions
- **Type**: typing.Optional[typing.Literal['BOTH', 'NONE', 'RESTRICTED', 'UNRESTRICTED']]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsEncryptionOutput]

### IncludeDvbSubtitles
- **Type**: typing.Optional[bool]

### IncludeIframeOnlyStream
- **Type**: typing.Optional[bool]

### PlaylistType
- **Type**: typing.Optional[typing.Literal['EVENT', 'NONE', 'VOD']]

### PlaylistWindowSeconds
- **Type**: typing.Optional[int]

### ProgramDateTimeIntervalSeconds
- **Type**: typing.Optional[int]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### StreamSelection
- **Type**: <class 'NoneType'>

### UseAudioRenditionGroup
- **Type**: typing.Optional[bool]


# IngestEndpoint

### Id
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# IngressAccessLogs

### LogGroupName
- **Type**: typing.Optional[str]


# ListChannelsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.PaginatorConfig]


# ListChannelsResponse

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.Channel]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListHarvestJobsRequest

### IncludeChannelId
- **Type**: typing.Optional[str]

### IncludeStatus
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHarvestJobsRequestPaginate

### IncludeChannelId
- **Type**: typing.Optional[str]

### IncludeStatus
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.PaginatorConfig]


# ListHarvestJobsResponse

### HarvestJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HarvestJob]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListOriginEndpointsRequest

### ChannelId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOriginEndpointsRequestPaginate

### ChannelId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.PaginatorConfig]


# ListOriginEndpointsResponse

### OriginEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.OriginEndpoint]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes


# MssEncryption

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.SpekeKeyProvider'>
- **Required**: Yes


# MssEncryptionOutput

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.SpekeKeyProviderOutput'>
- **Required**: Yes


# MssPackage

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.MssEncryption]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### StreamSelection
- **Type**: <class 'NoneType'>


# MssPackageOutput

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.MssEncryptionOutput]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### StreamSelection
- **Type**: <class 'NoneType'>


# OriginEndpoint

### Arn
- **Type**: typing.Optional[str]

### Authorization
- **Type**: <class 'NoneType'>

### ChannelId
- **Type**: typing.Optional[str]

### CmafPackage
- **Type**: <class 'NoneType'>

### CreatedAt
- **Type**: typing.Optional[str]

### DashPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.DashPackageOutput]

### Description
- **Type**: typing.Optional[str]

### HlsPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsPackageOutput]

### Id
- **Type**: typing.Optional[str]

### ManifestName
- **Type**: typing.Optional[str]

### MssPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.MssPackageOutput]

### Origination
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### StartoverWindowSeconds
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### TimeDelaySeconds
- **Type**: typing.Optional[int]

### Url
- **Type**: typing.Optional[str]

### Whitelist
- **Type**: typing.Optional[typing.List[str]]


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


# RotateChannelCredentialsRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# RotateChannelCredentialsResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.EgressAccessLogs'>
- **Required**: Yes

### HlsIngest
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsIngest'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.IngressAccessLogs'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes


# RotateIngestEndpointCredentialsRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngestEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# RotateIngestEndpointCredentialsResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.EgressAccessLogs'>
- **Required**: Yes

### HlsIngest
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsIngest'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.IngressAccessLogs'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes


# S3Destination

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestKey
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# SpekeKeyProvider

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SystemIds
- **Type**: typing.List[str]
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateArn
- **Type**: typing.Optional[str]

### EncryptionContractConfiguration
- **Type**: <class 'NoneType'>


# SpekeKeyProviderOutput

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SystemIds
- **Type**: typing.List[str]
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateArn
- **Type**: typing.Optional[str]

### EncryptionContractConfiguration
- **Type**: <class 'NoneType'>


# StreamSelection

### MaxVideoBitsPerSecond
- **Type**: typing.Optional[int]

### MinVideoBitsPerSecond
- **Type**: typing.Optional[int]

### StreamOrder
- **Type**: typing.Optional[typing.Literal['ORIGINAL', 'VIDEO_BITRATE_ASCENDING', 'VIDEO_BITRATE_DESCENDING']]


# TagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# UntagResourceRequest

### ResourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateChannelRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateChannelResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.EgressAccessLogs'>
- **Required**: Yes

### HlsIngest
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsIngest'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.IngressAccessLogs'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateOriginEndpointRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'NoneType'>

### CmafPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.CmafPackageCreateOrUpdateParameters]

### DashPackage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.DashPackage, aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.DashPackageOutput, NoneType]

### Description
- **Type**: typing.Optional[str]

### HlsPackage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsPackage, aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsPackageOutput, NoneType]

### ManifestName
- **Type**: typing.Optional[str]

### MssPackage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.MssPackage, aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.MssPackageOutput, NoneType]

### Origination
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### StartoverWindowSeconds
- **Type**: typing.Optional[int]

### TimeDelaySeconds
- **Type**: typing.Optional[int]

### Whitelist
- **Type**: typing.Optional[typing.List[str]]


# UpdateOriginEndpointResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.Authorization'>
- **Required**: Yes

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### CmafPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.CmafPackage'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DashPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.DashPackageOutput'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### HlsPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.HlsPackageOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### MssPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.MssPackageOutput'>
- **Required**: Yes

### Origination
- **Type**: typing.Literal['ALLOW', 'DENY']
- **Required**: Yes

### StartoverWindowSeconds
- **Type**: <class 'int'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### TimeDelaySeconds
- **Type**: <class 'int'>
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### Whitelist
- **Type**: typing.List[str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage.mediapackage_classes.ResponseMetadata'>
- **Required**: Yes


