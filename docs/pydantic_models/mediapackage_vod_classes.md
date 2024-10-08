# Pydantic Models in mediapackage_vod_classes

# AssetShallowTypeDef

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

# CmafEncryptionPaginatorTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.SpekeKeyProviderPaginatorTypeDef'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]


# CmafEncryptionTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.SpekeKeyProviderTypeDef'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]


# CmafPackagePaginatorTypeDef

### HlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod_classes.HlsManifestTypeDef]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.CmafEncryptionPaginatorTypeDef]

### IncludeEncoderConfigurationInSegments
- **Type**: typing.Optional[bool]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]


# CmafPackageTypeDef

### HlsManifests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediapackage_vod_classes.HlsManifestTypeDef]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.CmafEncryptionTypeDef]

### IncludeEncoderConfigurationInSegments
- **Type**: typing.Optional[bool]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]


# ConfigureLogsRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.EgressAccessLogsTypeDef]


# ConfigureLogsResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.AuthorizationTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.EgressAccessLogsTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateAssetRequestRequestTypeDef

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
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateAssetResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod_classes.EgressEndpointTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePackagingConfigurationRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### PackagingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### CmafPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.CmafPackageTypeDef]

### DashPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.DashPackageTypeDef]

### HlsPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.HlsPackageTypeDef]

### MssPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.MssPackageTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePackagingConfigurationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CmafPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.CmafPackageTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DashPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.DashPackageTypeDef'>
- **Required**: Yes

### HlsPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.HlsPackageTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MssPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.MssPackageTypeDef'>
- **Required**: Yes

### PackagingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePackagingGroupRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.AuthorizationTypeDef]

### EgressAccessLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.EgressAccessLogsTypeDef]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePackagingGroupResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.AuthorizationTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.EgressAccessLogsTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DashEncryptionPaginatorTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.SpekeKeyProviderPaginatorTypeDef'>
- **Required**: Yes


# DashEncryptionTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.SpekeKeyProviderTypeDef'>
- **Required**: Yes


# DashManifestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.StreamSelectionTypeDef]


# DashPackagePaginatorTypeDef

### DashManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod_classes.DashManifestTypeDef]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.DashEncryptionPaginatorTypeDef]

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


# DashPackageTypeDef

### DashManifests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediapackage_vod_classes.DashManifestTypeDef]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.DashEncryptionTypeDef]

### IncludeEncoderConfigurationInSegments
- **Type**: typing.Optional[bool]

### IncludeIframeOnlyStream
- **Type**: typing.Optional[bool]

### PeriodTriggers
- **Type**: typing.Optional[typing.Sequence[typing.Literal['ADS']]]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### SegmentTemplateFormat
- **Type**: typing.Optional[typing.Literal['NUMBER_WITH_DURATION', 'NUMBER_WITH_TIMELINE', 'TIME_WITH_TIMELINE']]


# DeleteAssetRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePackagingConfigurationRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePackagingGroupRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssetRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribeAssetResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### EgressEndpoints
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod_classes.EgressEndpointTypeDef]
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePackagingConfigurationRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePackagingConfigurationResponseTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### CmafPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.CmafPackageTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DashPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.DashPackageTypeDef'>
- **Required**: Yes

### HlsPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.HlsPackageTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### MssPackage
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.MssPackageTypeDef'>
- **Required**: Yes

### PackagingGroupId
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribePackagingGroupRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes


# DescribePackagingGroupResponseTypeDef

### ApproximateAssetCount
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.AuthorizationTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.EgressAccessLogsTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EgressAccessLogsTypeDef

### LogGroupName
- **Type**: typing.Optional[str]


# EgressEndpointTypeDef

### PackagingConfigurationId
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[str]

### Url
- **Type**: typing.Optional[str]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EncryptionContractConfigurationTypeDef

### PresetSpeke20Audio
- **Type**: typing.Literal['PRESET-AUDIO-1', 'PRESET-AUDIO-2', 'PRESET-AUDIO-3', 'SHARED', 'UNENCRYPTED']
- **Required**: Yes

### PresetSpeke20Video
- **Type**: typing.Literal['PRESET-VIDEO-1', 'PRESET-VIDEO-2', 'PRESET-VIDEO-3', 'PRESET-VIDEO-4', 'PRESET-VIDEO-5', 'PRESET-VIDEO-6', 'PRESET-VIDEO-7', 'PRESET-VIDEO-8', 'SHARED', 'UNENCRYPTED']
- **Required**: Yes


# HlsEncryptionPaginatorTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.SpekeKeyProviderPaginatorTypeDef'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_128', 'SAMPLE_AES']]


# HlsEncryptionTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.SpekeKeyProviderTypeDef'>
- **Required**: Yes

### ConstantInitializationVector
- **Type**: typing.Optional[str]

### EncryptionMethod
- **Type**: typing.Optional[typing.Literal['AES_128', 'SAMPLE_AES']]


# HlsManifestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.StreamSelectionTypeDef]


# HlsPackagePaginatorTypeDef

### HlsManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod_classes.HlsManifestTypeDef]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.HlsEncryptionPaginatorTypeDef]

### IncludeDvbSubtitles
- **Type**: typing.Optional[bool]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### UseAudioRenditionGroup
- **Type**: typing.Optional[bool]


# HlsPackageTypeDef

### HlsManifests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediapackage_vod_classes.HlsManifestTypeDef]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.HlsEncryptionTypeDef]

### IncludeDvbSubtitles
- **Type**: typing.Optional[bool]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]

### UseAudioRenditionGroup
- **Type**: typing.Optional[bool]


# ListAssetsRequestListAssetsPaginateTypeDef

### PackagingGroupId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.PaginatorConfigTypeDef]


# ListAssetsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### PackagingGroupId
- **Type**: typing.Optional[str]


# ListAssetsResponseTypeDef

### Assets
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod_classes.AssetShallowTypeDef]
- **Required**: Yes

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPackagingConfigurationsRequestListPackagingConfigurationsPaginateTypeDef

### PackagingGroupId
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.PaginatorConfigTypeDef]


# ListPackagingConfigurationsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### PackagingGroupId
- **Type**: typing.Optional[str]


# ListPackagingConfigurationsResponsePaginatorTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### PackagingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod_classes.PackagingConfigurationPaginatorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPackagingConfigurationsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### PackagingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod_classes.PackagingConfigurationTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPackagingGroupsRequestListPackagingGroupsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.PaginatorConfigTypeDef]


# ListPackagingGroupsRequestRequestTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListPackagingGroupsResponseTypeDef

### NextToken
- **Type**: <class 'str'>
- **Required**: Yes

### PackagingGroups
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod_classes.PackagingGroupTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# MssEncryptionPaginatorTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.SpekeKeyProviderPaginatorTypeDef'>
- **Required**: Yes


# MssEncryptionTypeDef

### SpekeKeyProvider
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.SpekeKeyProviderTypeDef'>
- **Required**: Yes


# MssManifestTypeDef

### ManifestName
- **Type**: typing.Optional[str]

### StreamSelection
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.StreamSelectionTypeDef]


# MssPackagePaginatorTypeDef

### MssManifests
- **Type**: typing.List[aws_resource_validator.pydantic_models.mediapackage_vod_classes.MssManifestTypeDef]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.MssEncryptionPaginatorTypeDef]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]


# MssPackageTypeDef

### MssManifests
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.mediapackage_vod_classes.MssManifestTypeDef]
- **Required**: Yes

### Encryption
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.MssEncryptionTypeDef]

### SegmentDurationSeconds
- **Type**: typing.Optional[int]


# PackagingConfigurationPaginatorTypeDef

### Arn
- **Type**: typing.Optional[str]

### CmafPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.CmafPackagePaginatorTypeDef]

### CreatedAt
- **Type**: typing.Optional[str]

### DashPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.DashPackagePaginatorTypeDef]

### HlsPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.HlsPackagePaginatorTypeDef]

### Id
- **Type**: typing.Optional[str]

### MssPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.MssPackagePaginatorTypeDef]

### PackagingGroupId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PackagingConfigurationTypeDef

### Arn
- **Type**: typing.Optional[str]

### CmafPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.CmafPackageTypeDef]

### CreatedAt
- **Type**: typing.Optional[str]

### DashPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.DashPackageTypeDef]

### HlsPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.HlsPackageTypeDef]

### Id
- **Type**: typing.Optional[str]

### MssPackage
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.MssPackageTypeDef]

### PackagingGroupId
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PackagingGroupTypeDef

### ApproximateAssetCount
- **Type**: typing.Optional[int]

### Arn
- **Type**: typing.Optional[str]

### Authorization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.AuthorizationTypeDef]

### CreatedAt
- **Type**: typing.Optional[str]

### DomainName
- **Type**: typing.Optional[str]

### EgressAccessLogs
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.EgressAccessLogsTypeDef]

### Id
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Dict[str, str]]


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


# SpekeKeyProviderPaginatorTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.EncryptionContractConfigurationTypeDef]


# SpekeKeyProviderTypeDef

### RoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### SystemIds
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### EncryptionContractConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.EncryptionContractConfigurationTypeDef]


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


# UpdatePackagingGroupRequestRequestTypeDef

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.mediapackage_vod_classes.AuthorizationTypeDef]


# UpdatePackagingGroupResponseTypeDef

### ApproximateAssetCount
- **Type**: <class 'int'>
- **Required**: Yes

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### Authorization
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.AuthorizationTypeDef'>
- **Required**: Yes

### CreatedAt
- **Type**: <class 'str'>
- **Required**: Yes

### DomainName
- **Type**: <class 'str'>
- **Required**: Yes

### EgressAccessLogs
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.EgressAccessLogsTypeDef'>
- **Required**: Yes

### Id
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.mediapackage_vod_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


