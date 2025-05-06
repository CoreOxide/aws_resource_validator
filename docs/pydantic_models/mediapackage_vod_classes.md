# Mediapackage Vod Classes

# AssetShallow

### Arn
- **Type**: typing.Optional[str]

### CreatedAt
- **Type**: typing.Optional[str]

### Id
- **Type**: typing.Optional[str]

### PackagingGroupId
- **Type**: typing.Optional[str]

### ResourceId
- **Type**: typing.Optional[str]

### SourceArn
- **Type**: typing.Optional[str]

### SourceRoleArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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

# CmafEncryption

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.SpekeKeyProvider'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]


# CmafEncryptionOutput

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.SpekeKeyProviderOutput'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]


# CmafPackage

### HlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.HlsManifest]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.CmafEncryption]

### IncludeEncoderConfigurationInSegments
- **Type**: typing.Optional[bool]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]


# CmafPackageOutput

### HlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.HlsManifest]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.CmafEncryptionOutput]

### IncludeEncoderConfigurationInSegments
- **Type**: typing.Optional[bool]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]


# ConfigureLogsRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'NoneType'>


# ConfigureLogsResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.Authorization'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.EgressAccessLogs'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.ResponseMetadata'>
- **Required**: Yes


# CreateAssetRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### PackagingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateAssetResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.EgressEndpoint]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### PackagingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePackagingConfigurationRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### PackagingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### CmafPackage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.CmafPackage, aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.CmafPackageOutput, NoneType]

### DashPackage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.DashPackage, aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.DashPackageOutput, NoneType]

### HlsPackage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.HlsPackage, aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.HlsPackageOutput, NoneType]

### MssPackage
- **Type**: typing.Union[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.MssPackage, aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.MssPackageOutput, NoneType]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreatePackagingConfigurationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CmafPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.CmafPackageOutput'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DashPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.DashPackageOutput'>
- **Required**: Yes

### HlsPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.HlsPackageOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MssPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.MssPackageOutput'>
- **Required**: Yes

### PackagingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePackagingGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'NoneType'>

### EgressAccessLogs
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreatePackagingGroupResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.Authorization'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.EgressAccessLogs'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.ResponseMetadata'>
- **Required**: Yes


# DashEncryption

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.SpekeKeyProvider'>
- **Required**: Yes


# DashEncryptionOutput

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.SpekeKeyProviderOutput'>
- **Required**: Yes


# DashManifest

### ManifestLayout
- **Type**: typing.Optional[typing.Literal['COMPACT', 'FULL']]

### ManifestName
- **Type**: typing.Optional[str]

### MinBufferTimeSeconds
- **Type**: typing.Optional[int]

### Profile
- **Type**: typing.Optional[typing.Literal['HBBTV_1_5', 'NONE']]

### ScteMarkersSource
- **Type**: typing.Optional[typing.Literal['MANIFEST', 'SEGMENTS']]

### StreamSelection
- **Type**: <class 'NoneType'>


# DashPackage

### DashManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.DashManifest]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.DashEncryption]

### IncludeEncoderConfigurationInSegments
- **Type**: typing.Optional[bool]

### IncludeIframeOnlyStream
- **Type**: typing.Optional[bool]

### PeriodTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['ADS']]]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### SegmentTemplateFormat
- **Type**: typing.Optional[typing.Literal['NUMBER_WITH_DURATION', 'NUMBER_WITH_TIMELINE', 'TIME_WITH_TIMELINE']]


# DashPackageOutput

### DashManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.DashManifest]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.DashEncryptionOutput]

### IncludeEncoderConfigurationInSegments
- **Type**: typing.Optional[bool]

### IncludeIframeOnlyStream
- **Type**: typing.Optional[bool]

### PeriodTriggers
- **Type**: typing.Optional[typing.List[typing.Literal['ADS']]]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### SegmentTemplateFormat
- **Type**: typing.Optional[typing.Literal['NUMBER_WITH_DURATION', 'NUMBER_WITH_TIMELINE', 'TIME_WITH_TIMELINE']]


# DeleteAssetRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePackagingConfigurationRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePackagingGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssetRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssetResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.EgressEndpoint]
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### PackagingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceId
- **Type**: <class 'str'>
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SourceRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePackagingConfigurationRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePackagingConfigurationResponse

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CmafPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.CmafPackageOutput'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DashPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.DashPackageOutput'>
- **Required**: Yes

### HlsPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.HlsPackageOutput'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MssPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.MssPackageOutput'>
- **Required**: Yes

### PackagingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.ResponseMetadata'>
- **Required**: Yes


# DescribePackagingGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePackagingGroupResponse

### ApproximateAssetCount
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.Authorization'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.EgressAccessLogs'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.ResponseMetadata'>
- **Required**: Yes


# EgressAccessLogs

### LogGroupName
- **Type**: typing.Optional[str]


# EgressEndpoint

### PackagingConfigurationId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.ResponseMetadata'>
- **Required**: Yes


# EncryptionContractConfiguration

### PresetSpeke20Audio
- **Type**: typing.Literal['PRESET-AUDIO-1', 'PRESET-AUDIO-2', 'PRESET-AUDIO-3', 'SHARED', 'UNENCRYPTED']
- **Required**: Yes

### PresetSpeke20Video
- **Type**: typing.Literal['PRESET-VIDEO-1', 'PRESET-VIDEO-2', 'PRESET-VIDEO-3', 'PRESET-VIDEO-4', 'PRESET-VIDEO-5', 'PRESET-VIDEO-6', 'PRESET-VIDEO-7', 'PRESET-VIDEO-8', 'SHARED', 'UNENCRYPTED']
- **Required**: Yes


# HlsEncryption

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.SpekeKeyProvider'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_128', 'SAMPLE_AES']]


# HlsEncryptionOutput

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.SpekeKeyProviderOutput'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_128', 'SAMPLE_AES']]


# HlsManifest

### AdMarkers
- **Type**: typing.Optional[typing.Literal['NONE', 'PASSTHROUGH', 'SCTE35_ENHANCED']]

### IncludeIframeOnlyStream
- **Type**: typing.Optional[bool]

### ManifestName
- **Type**: typing.Optional[str]

### ProgramDateTimeIntervalSeconds
- **Type**: typing.Optional[int]

### RepeatExtXKey
- **Type**: typing.Optional[bool]

### StreamSelection
- **Type**: <class 'NoneType'>


# HlsPackage

### HlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.HlsManifest]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.HlsEncryption]

### IncludeDvbSubtitles
- **Type**: typing.Optional[bool]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### UseAudioRenditionGroup
- **Type**: typing.Optional[bool]


# HlsPackageOutput

### HlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.HlsManifest]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.HlsEncryptionOutput]

### IncludeDvbSubtitles
- **Type**: typing.Optional[bool]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### UseAudioRenditionGroup
- **Type**: typing.Optional[bool]


# ListAssetsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### PackagingGroupId
- **Type**: typing.Optional[str]


# ListAssetsRequestPaginate

### PackagingGroupId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.PaginatorConfig]


# ListAssetsResponse

### Assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.AssetShallow]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPackagingConfigurationsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### PackagingGroupId
- **Type**: typing.Optional[str]


# ListPackagingConfigurationsRequestPaginate

### PackagingGroupId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.PaginatorConfig]


# ListPackagingConfigurationsResponse

### PackagingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.PackagingConfiguration]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListPackagingGroupsRequest

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPackagingGroupsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.PaginatorConfig]


# ListPackagingGroupsResponse

### PackagingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.PackagingGroup]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.ResponseMetadata'>
- **Required**: Yes


# MssEncryption

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.SpekeKeyProvider'>
- **Required**: Yes


# MssEncryptionOutput

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.SpekeKeyProviderOutput'>
- **Required**: Yes


# MssManifest

### ManifestName
- **Type**: typing.Optional[str]

### StreamSelection
- **Type**: <class 'NoneType'>


# MssPackage

### MssManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.MssManifest]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.MssEncryption]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]


# MssPackageOutput

### MssManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.MssManifest]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.MssEncryptionOutput]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]


# PackagingConfiguration

### Arn
- **Type**: typing.Optional[str]

### CmafPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.CmafPackageOutput]

### CreatedAt
- **Type**: typing.Optional[str]

### DashPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.DashPackageOutput]

### HlsPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.HlsPackageOutput]

### Id
- **Type**: typing.Optional[str]

### MssPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.MssPackageOutput]

### PackagingGroupId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PackagingGroup

### ApproximateAssetCount
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### Authorization
- **Type**: <class 'NoneType'>

### CreatedAt
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### EgressAccessLogs
- **Type**: <class 'NoneType'>

### Id
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# SpekeKeyProvider

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SystemIds
- **Type**: typing.List[str]
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionContractConfiguration
- **Type**: <class 'NoneType'>


# SpekeKeyProviderOutput

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SystemIds
- **Type**: typing.List[str]
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

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


# UpdatePackagingGroupRequest

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'NoneType'>


# UpdatePackagingGroupResponse

### ApproximateAssetCount
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.Authorization'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.EgressAccessLogs'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod.mediapackage_vod_classes.ResponseMetadata'>
- **Required**: Yes


