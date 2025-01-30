# mediapackage_classes

# AuthorizationTypeDef

### CdnIdentifierSecret
- **Type**: <class 'str'>
- **Required**: Yes

### SecretsRoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelTypeDef

### Arn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### Description
- **Type**: typing.Optional[str]

### EgressAccessLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.EgressAccessLogsTypeDef]

### HlsIngest
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.HlsIngestTypeDef]

### Id
- **Type**: typing.Optional[str]

### IngressAccessLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.IngressAccessLogsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CmafEncryptionPaginatorTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.SpekeKeyProviderPaginatorTypeDef'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_CTR', 'SAMPLE_AES']]

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]


# CmafEncryptionTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.SpekeKeyProviderTypeDef'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_CTR', 'SAMPLE_AES']]

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]


# CmafPackageCreateOrUpdateParametersTypeDef

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.CmafEncryptionTypeDef]

### HlsManifests
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.mediapackage_classes.HlsManifestCreateOrUpdateParametersTypeDef]]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### SegmentPrefix
- **Type**: typing.Optional[str]

### StreamSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.StreamSelectionTypeDef]


# CmafPackagePaginatorTypeDef

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.CmafEncryptionPaginatorTypeDef]

### HlsManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackage_classes.HlsManifestTypeDef]]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### SegmentPrefix
- **Type**: typing.Optional[str]

### StreamSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.StreamSelectionTypeDef]


# CmafPackageTypeDef

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.CmafEncryptionTypeDef]

### HlsManifests
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackage_classes.HlsManifestTypeDef]]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### SegmentPrefix
- **Type**: typing.Optional[str]

### StreamSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.StreamSelectionTypeDef]


# ConfigureLogsRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.EgressAccessLogsTypeDef]

### IngressAccessLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.IngressAccessLogsTypeDef]


# ConfigureLogsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.EgressAccessLogsTypeDef'>
- **Required**: Yes

### HlsIngest
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.HlsIngestTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.IngressAccessLogsTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateChannelRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateChannelResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.EgressAccessLogsTypeDef'>
- **Required**: Yes

### HlsIngest
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.HlsIngestTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.IngressAccessLogsTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateHarvestJobRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.S3DestinationTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: <class 'str'>
- **Required**: Yes


# CreateHarvestJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.S3DestinationTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateOriginEndpointRequestRequestTypeDef

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.AuthorizationTypeDef]

### CmafPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.CmafPackageCreateOrUpdateParametersTypeDef]

### DashPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.DashPackageTypeDef]

### Description
- **Type**: typing.Optional[str]

### HlsPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.HlsPackageTypeDef]

### ManifestName
- **Type**: typing.Optional[str]

### MssPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.MssPackageTypeDef]

### Origination
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### StartoverWindowSeconds
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### TimeDelaySeconds
- **Type**: typing.Optional[int]

### Whitelist
- **Type**: typing.Optional[typing.Sequence[str]]


# CreateOriginEndpointResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.AuthorizationTypeDef'>
- **Required**: Yes

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### CmafPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.CmafPackageTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DashPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.DashPackageTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### HlsPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.HlsPackageTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### MssPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.MssPackageTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DashEncryptionPaginatorTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.SpekeKeyProviderPaginatorTypeDef'>
- **Required**: Yes

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]


# DashEncryptionTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.SpekeKeyProviderTypeDef'>
- **Required**: Yes

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]


# DashPackagePaginatorTypeDef

### AdTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]

### AdsOnDeliveryRestrictions
- **Type**: typing.Optional[typing.Literal['BOTH', 'NONE', 'RESTRICTED', 'UNRESTRICTED']]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.DashEncryptionPaginatorTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.StreamSelectionTypeDef]

### SuggestedPresentationDelaySeconds
- **Type**: typing.Optional[int]

### UtcTiming
- **Type**: typing.Optional[typing.Literal['HTTP-HEAD', 'HTTP-ISO', 'HTTP-XSDATE', 'NONE']]

### UtcTimingUri
- **Type**: typing.Optional[str]


# DashPackageTypeDef

### AdTriggers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]

### AdsOnDeliveryRestrictions
- **Type**: typing.Optional[typing.Literal['BOTH', 'NONE', 'RESTRICTED', 'UNRESTRICTED']]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.DashEncryptionTypeDef]

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
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ADS']]]

### Profile
- **Type**: typing.Optional[typing.Literal['DVB_DASH_2014', 'HBBTV_1_5', 'HYBRIDCAST', 'NONE']]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### SegmentTemplateFormat
- **Type**: typing.Optional[typing.Literal['NUMBER_WITH_DURATION', 'NUMBER_WITH_TIMELINE', 'TIME_WITH_TIMELINE']]

### StreamSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.StreamSelectionTypeDef]

### SuggestedPresentationDelaySeconds
- **Type**: typing.Optional[int]

### UtcTiming
- **Type**: typing.Optional[typing.Literal['HTTP-HEAD', 'HTTP-ISO', 'HTTP-XSDATE', 'NONE']]

### UtcTimingUri
- **Type**: typing.Optional[str]


# DeleteChannelRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteOriginEndpointRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeChannelResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.EgressAccessLogsTypeDef'>
- **Required**: Yes

### HlsIngest
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.HlsIngestTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.IngressAccessLogsTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeHarvestJobRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeHarvestJobResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.S3DestinationTypeDef'>
- **Required**: Yes

### StartTime
- **Type**: <class 'str'>
- **Required**: Yes

### Status
- **Type**: typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeOriginEndpointRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeOriginEndpointResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.AuthorizationTypeDef'>
- **Required**: Yes

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### CmafPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.CmafPackageTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DashPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.DashPackageTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### HlsPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.HlsPackageTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### MssPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.MssPackageTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EgressAccessLogsTypeDef

### LogGroupName
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionContractConfigurationTypeDef

### PresetSpeke20Audio
- **Type**: typing.Literal['PRESET-AUDIO-1', 'PRESET-AUDIO-2', 'PRESET-AUDIO-3', 'SHARED', 'UNENCRYPTED']
- **Required**: Yes

### PresetSpeke20Video
- **Type**: typing.Literal['PRESET-VIDEO-1', 'PRESET-VIDEO-2', 'PRESET-VIDEO-3', 'PRESET-VIDEO-4', 'PRESET-VIDEO-5', 'PRESET-VIDEO-6', 'PRESET-VIDEO-7', 'PRESET-VIDEO-8', 'SHARED', 'UNENCRYPTED']
- **Required**: Yes


# HarvestJobTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.S3DestinationTypeDef]

### StartTime
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['FAILED', 'IN_PROGRESS', 'SUCCEEDED']]


# HlsEncryptionPaginatorTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.SpekeKeyProviderPaginatorTypeDef'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_128', 'SAMPLE_AES']]

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]

### RepeatExtXKey
- **Type**: typing.Optional[bool]


# HlsEncryptionTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.SpekeKeyProviderTypeDef'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_128', 'SAMPLE_AES']]

### KeyRotationIntervalSeconds
- **Type**: typing.Optional[int]

### RepeatExtXKey
- **Type**: typing.Optional[bool]


# HlsIngestTypeDef

### IngestEndpoints
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.mediapackage_classes.IngestEndpointTypeDef]]


# HlsManifestCreateOrUpdateParametersTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### AdMarkers
- **Type**: typing.Optional[typing.Literal['DATERANGE', 'NONE', 'PASSTHROUGH', 'SCTE35_ENHANCED']]

### AdTriggers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]

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


# HlsManifestTypeDef

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


# HlsPackagePaginatorTypeDef

### AdMarkers
- **Type**: typing.Optional[typing.Literal['DATERANGE', 'NONE', 'PASSTHROUGH', 'SCTE35_ENHANCED']]

### AdTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]

### AdsOnDeliveryRestrictions
- **Type**: typing.Optional[typing.Literal['BOTH', 'NONE', 'RESTRICTED', 'UNRESTRICTED']]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.HlsEncryptionPaginatorTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.StreamSelectionTypeDef]

### UseAudioRenditionGroup
- **Type**: typing.Optional[bool]


# HlsPackageTypeDef

### AdMarkers
- **Type**: typing.Optional[typing.Literal['DATERANGE', 'NONE', 'PASSTHROUGH', 'SCTE35_ENHANCED']]

### AdTriggers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['BREAK', 'DISTRIBUTOR_ADVERTISEMENT', 'DISTRIBUTOR_OVERLAY_PLACEMENT_OPPORTUNITY', 'DISTRIBUTOR_PLACEMENT_OPPORTUNITY', 'PROVIDER_ADVERTISEMENT', 'PROVIDER_OVERLAY_PLACEMENT_OPPORTUNITY', 'PROVIDER_PLACEMENT_OPPORTUNITY', 'SPLICE_INSERT']]]

### AdsOnDeliveryRestrictions
- **Type**: typing.Optional[typing.Literal['BOTH', 'NONE', 'RESTRICTED', 'UNRESTRICTED']]

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.HlsEncryptionTypeDef]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.StreamSelectionTypeDef]

### UseAudioRenditionGroup
- **Type**: typing.Optional[bool]


# IngestEndpointTypeDef

### Id
- **Type**: typing.Optional[str]

### Password
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]

### Username
- **Type**: typing.Optional[str]


# IngressAccessLogsTypeDef

### LogGroupName
- **Type**: typing.Optional[str]


# ListChannelsRequestListChannelsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.PaginatorConfigTypeDef]


# ListChannelsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListChannelsResponseTypeDef

### Channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_classes.ChannelTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListHarvestJobsRequestListHarvestJobsPaginateTypeDef

### IncludeChannelId
- **Type**: typing.Optional[str]

### IncludeStatus
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.PaginatorConfigTypeDef]


# ListHarvestJobsRequestRequestTypeDef

### IncludeChannelId
- **Type**: typing.Optional[str]

### IncludeStatus
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListHarvestJobsResponseTypeDef

### HarvestJobs
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_classes.HarvestJobTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOriginEndpointsRequestListOriginEndpointsPaginateTypeDef

### ChannelId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.PaginatorConfigTypeDef]


# ListOriginEndpointsRequestRequestTypeDef

### ChannelId
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListOriginEndpointsResponsePaginatorTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_classes.OriginEndpointPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListOriginEndpointsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### OriginEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_classes.OriginEndpointTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MssEncryptionPaginatorTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.SpekeKeyProviderPaginatorTypeDef'>
- **Required**: Yes


# MssEncryptionTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.SpekeKeyProviderTypeDef'>
- **Required**: Yes


# MssPackagePaginatorTypeDef

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.MssEncryptionPaginatorTypeDef]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### StreamSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.StreamSelectionTypeDef]


# MssPackageTypeDef

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.MssEncryptionTypeDef]

### ManifestWindowSeconds
- **Type**: typing.Optional[int]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### StreamSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.StreamSelectionTypeDef]


# OriginEndpointPaginatorTypeDef

### Arn
- **Type**: typing.Optional[str]

### Authorization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.AuthorizationTypeDef]

### ChannelId
- **Type**: typing.Optional[str]

### CmafPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.CmafPackagePaginatorTypeDef]

### CreatedAt
- **Type**: typing.Optional[str]

### DashPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.DashPackagePaginatorTypeDef]

### Description
- **Type**: typing.Optional[str]

### HlsPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.HlsPackagePaginatorTypeDef]

### Id
- **Type**: typing.Optional[str]

### ManifestName
- **Type**: typing.Optional[str]

### MssPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.MssPackagePaginatorTypeDef]

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


# OriginEndpointTypeDef

### Arn
- **Type**: typing.Optional[str]

### Authorization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.AuthorizationTypeDef]

### ChannelId
- **Type**: typing.Optional[str]

### CmafPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.CmafPackageTypeDef]

### CreatedAt
- **Type**: typing.Optional[str]

### DashPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.DashPackageTypeDef]

### Description
- **Type**: typing.Optional[str]

### HlsPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.HlsPackageTypeDef]

### Id
- **Type**: typing.Optional[str]

### ManifestName
- **Type**: typing.Optional[str]

### MssPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.MssPackageTypeDef]

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

### HostId
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


# RotateChannelCredentialsRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# RotateChannelCredentialsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.EgressAccessLogsTypeDef'>
- **Required**: Yes

### HlsIngest
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.HlsIngestTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.IngressAccessLogsTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# RotateIngestEndpointCredentialsRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngestEndpointId
- **Type**: <class 'str'>
- **Required**: Yes


# RotateIngestEndpointCredentialsResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.EgressAccessLogsTypeDef'>
- **Required**: Yes

### HlsIngest
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.HlsIngestTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.IngressAccessLogsTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# S3DestinationTypeDef

### BucketName
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestKey
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes


# SpekeKeyProviderPaginatorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.EncryptionContractConfigurationTypeDef]


# SpekeKeyProviderTypeDef

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SystemIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### CertificateArn
- **Type**: typing.Optional[str]

### EncryptionContractConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.EncryptionContractConfigurationTypeDef]


# StreamSelectionTypeDef

### MaxVideoBitsPerSecond
- **Type**: typing.Optional[int]

### MinVideoBitsPerSecond
- **Type**: typing.Optional[int]

### StreamOrder
- **Type**: typing.Optional[typing.Literal['ORIGINAL', 'VIDEO_BITRATE_ASCENDING', 'VIDEO_BITRATE_DESCENDING']]


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


# UpdateChannelRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Description
- **Type**: typing.Optional[str]


# UpdateChannelResponseTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.EgressAccessLogsTypeDef'>
- **Required**: Yes

### HlsIngest
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.HlsIngestTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### IngressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.IngressAccessLogsTypeDef'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateOriginEndpointRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.AuthorizationTypeDef]

### CmafPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.CmafPackageCreateOrUpdateParametersTypeDef]

### DashPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.DashPackageTypeDef]

### Description
- **Type**: typing.Optional[str]

### HlsPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.HlsPackageTypeDef]

### ManifestName
- **Type**: typing.Optional[str]

### MssPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_classes.MssPackageTypeDef]

### Origination
- **Type**: typing.Optional[typing.Literal['ALLOW', 'DENY']]

### StartoverWindowSeconds
- **Type**: typing.Optional[int]

### TimeDelaySeconds
- **Type**: typing.Optional[int]

### Whitelist
- **Type**: typing.Optional[typing.Sequence[str]]


# UpdateOriginEndpointResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.AuthorizationTypeDef'>
- **Required**: Yes

### ChannelId
- **Type**: <class 'str'>
- **Required**: Yes

### CmafPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.CmafPackageTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DashPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.DashPackageTypeDef'>
- **Required**: Yes

### Description
- **Type**: <class 'str'>
- **Required**: Yes

### HlsPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.HlsPackageTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### ManifestName
- **Type**: <class 'str'>
- **Required**: Yes

### MssPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.MssPackageTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


