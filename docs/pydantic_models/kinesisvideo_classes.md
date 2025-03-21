# Kinesisvideo Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelInfoTypeDef

### ChannelName
- **Type**: typing.Optional[str]

### ChannelARN
- **Type**: typing.Optional[str]

### ChannelType
- **Type**: typing.Optional[typing.Literal['FULL_MESH', 'SINGLE_MASTER']]

### ChannelStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'UPDATING']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### SingleMasterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.SingleMasterConfigurationTypeDef]

### Version
- **Type**: typing.Optional[str]


# ChannelNameConditionTypeDef

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH']]

### ComparisonValue
- **Type**: typing.Optional[str]


# CreateSignalingChannelInputTypeDef

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelType
- **Type**: typing.Optional[typing.Literal['FULL_MESH', 'SINGLE_MASTER']]

### SingleMasterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.SingleMasterConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.kinesisvideo_classes.TagTypeDef]]


# CreateSignalingChannelOutputTypeDef

### ChannelARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStreamInputTypeDef

### StreamName
- **Type**: <class 'str'>
- **Required**: Yes

### DeviceName
- **Type**: typing.Optional[str]

### MediaType
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### DataRetentionInHours
- **Type**: typing.Optional[int]

### Tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateStreamOutputTypeDef

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEdgeConfigurationInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DeleteSignalingChannelInputTypeDef

### ChannelARN
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: typing.Optional[str]


# DeleteStreamInputTypeDef

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: typing.Optional[str]


# DeletionConfigTypeDef

### EdgeRetentionInHours
- **Type**: typing.Optional[int]

### LocalSizeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.LocalSizeConfigTypeDef]

### DeleteAfterUpload
- **Type**: typing.Optional[bool]


# DescribeEdgeConfigurationInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DescribeEdgeConfigurationOutputTypeDef

### StreamName
- **Type**: <class 'str'>
- **Required**: Yes

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SyncStatus
- **Type**: typing.Literal['ACKNOWLEDGED', 'DELETE_FAILED', 'DELETING', 'DELETING_ACKNOWLEDGED', 'IN_SYNC', 'SYNCING', 'SYNC_FAILED']
- **Required**: Yes

### FailedStatusDetails
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.EdgeConfigTypeDef'>
- **Required**: Yes

### EdgeAgentStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.EdgeAgentStatusTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeImageGenerationConfigurationInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DescribeImageGenerationConfigurationOutputTypeDef

### ImageGenerationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ImageGenerationConfigurationOutputTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeMappedResourceConfigurationInputPaginateTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.PaginatorConfigTypeDef]


# DescribeMappedResourceConfigurationInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMappedResourceConfigurationOutputTypeDef

### MappedResourceConfigurationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisvideo_classes.MappedResourceConfigurationListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMediaStorageConfigurationInputTypeDef

### ChannelName
- **Type**: typing.Optional[str]

### ChannelARN
- **Type**: typing.Optional[str]


# DescribeMediaStorageConfigurationOutputTypeDef

### MediaStorageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.MediaStorageConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeNotificationConfigurationInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DescribeNotificationConfigurationOutputTypeDef

### NotificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.NotificationConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeSignalingChannelInputTypeDef

### ChannelName
- **Type**: typing.Optional[str]

### ChannelARN
- **Type**: typing.Optional[str]


# DescribeSignalingChannelOutputTypeDef

### ChannelInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ChannelInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DescribeStreamInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DescribeStreamOutputTypeDef

### StreamInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.StreamInfoTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# EdgeAgentStatusTypeDef

### LastRecorderStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.LastRecorderStatusTypeDef]

### LastUploaderStatus
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.LastUploaderStatusTypeDef]


# EdgeConfigTypeDef

### HubDeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecorderConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.RecorderConfigTypeDef'>
- **Required**: Yes

### UploaderConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.UploaderConfigTypeDef]

### DeletionConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.DeletionConfigTypeDef]


# GetDataEndpointInputTypeDef

### APIName
- **Type**: typing.Literal['GET_CLIP', 'GET_DASH_STREAMING_SESSION_URL', 'GET_HLS_STREAMING_SESSION_URL', 'GET_IMAGES', 'GET_MEDIA', 'GET_MEDIA_FOR_FRAGMENT_LIST', 'LIST_FRAGMENTS', 'PUT_MEDIA']
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# GetDataEndpointOutputTypeDef

### DataEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSignalingChannelEndpointInputTypeDef

### ChannelARN
- **Type**: <class 'str'>
- **Required**: Yes

### SingleMasterChannelEndpointConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.SingleMasterChannelEndpointConfigurationTypeDef]


# GetSignalingChannelEndpointOutputTypeDef

### ResourceEndpointList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisvideo_classes.ResourceEndpointListItemTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImageGenerationConfigurationOutputTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ImageSelectorType
- **Type**: typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']
- **Required**: Yes

### DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ImageGenerationDestinationConfigTypeDef'>
- **Required**: Yes

### SamplingInterval
- **Type**: <class 'int'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['JPEG', 'PNG']
- **Required**: Yes

### FormatConfig
- **Type**: typing.Optional[typing.Dict[typing.Literal['JPEGQuality'], str]]

### WidthPixels
- **Type**: typing.Optional[int]

### HeightPixels
- **Type**: typing.Optional[int]


# ImageGenerationConfigurationTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ImageSelectorType
- **Type**: typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']
- **Required**: Yes

### DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ImageGenerationDestinationConfigTypeDef'>
- **Required**: Yes

### SamplingInterval
- **Type**: <class 'int'>
- **Required**: Yes

### Format
- **Type**: typing.Literal['JPEG', 'PNG']
- **Required**: Yes

### FormatConfig
- **Type**: typing.Optional[typing.Mapping[typing.Literal['JPEGQuality'], str]]

### WidthPixels
- **Type**: typing.Optional[int]

### HeightPixels
- **Type**: typing.Optional[int]


# ImageGenerationConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ImageGenerationDestinationConfigTypeDef

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationRegion
- **Type**: <class 'str'>
- **Required**: Yes


# LastRecorderStatusTypeDef

### JobStatusDetails
- **Type**: typing.Optional[str]

### LastCollectedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### RecorderStatus
- **Type**: typing.Optional[typing.Literal['SUCCESS', 'SYSTEM_ERROR', 'USER_ERROR']]


# LastUploaderStatusTypeDef

### JobStatusDetails
- **Type**: typing.Optional[str]

### LastCollectedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### UploaderStatus
- **Type**: typing.Optional[typing.Literal['SUCCESS', 'SYSTEM_ERROR', 'USER_ERROR']]


# ListEdgeAgentConfigurationsEdgeConfigTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### SyncStatus
- **Type**: typing.Optional[typing.Literal['ACKNOWLEDGED', 'DELETE_FAILED', 'DELETING', 'DELETING_ACKNOWLEDGED', 'IN_SYNC', 'SYNCING', 'SYNC_FAILED']]

### FailedStatusDetails
- **Type**: typing.Optional[str]

### EdgeConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.EdgeConfigTypeDef]


# ListEdgeAgentConfigurationsInputPaginateTypeDef

### HubDeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.PaginatorConfigTypeDef]


# ListEdgeAgentConfigurationsInputTypeDef

### HubDeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEdgeAgentConfigurationsOutputTypeDef

### EdgeConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisvideo_classes.ListEdgeAgentConfigurationsEdgeConfigTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSignalingChannelsInputPaginateTypeDef

### ChannelNameCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.ChannelNameConditionTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.PaginatorConfigTypeDef]


# ListSignalingChannelsInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ChannelNameCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.ChannelNameConditionTypeDef]


# ListSignalingChannelsOutputTypeDef

### ChannelInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisvideo_classes.ChannelInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStreamsInputPaginateTypeDef

### StreamNameCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.StreamNameConditionTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.PaginatorConfigTypeDef]


# ListStreamsInputTypeDef

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### StreamNameCondition
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.StreamNameConditionTypeDef]


# ListStreamsOutputTypeDef

### StreamInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisvideo_classes.StreamInfoTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceOutputTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForStreamInputTypeDef

### NextToken
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### StreamName
- **Type**: typing.Optional[str]


# ListTagsForStreamOutputTypeDef

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LocalSizeConfigTypeDef

### MaxLocalMediaSizeInMB
- **Type**: typing.Optional[int]

### StrategyOnFullSize
- **Type**: typing.Optional[typing.Literal['DELETE_OLDEST_MEDIA', 'DENY_NEW_MEDIA']]


# MappedResourceConfigurationListItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MediaSourceConfigTypeDef

### MediaUriSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaUriType
- **Type**: typing.Literal['FILE_URI', 'RTSP_URI']
- **Required**: Yes


# MediaStorageConfigurationTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### StreamARN
- **Type**: typing.Optional[str]


# NotificationConfigurationTypeDef

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.NotificationDestinationConfigTypeDef'>
- **Required**: Yes


# NotificationDestinationConfigTypeDef

### Uri
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RecorderConfigTypeDef

### MediaSourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.MediaSourceConfigTypeDef'>
- **Required**: Yes

### ScheduleConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.ScheduleConfigTypeDef]


# ResourceEndpointListItemTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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


# ScheduleConfigTypeDef

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### DurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes


# SingleMasterChannelEndpointConfigurationTypeDef

### Protocols
- **Type**: typing.Optional[typing.Sequence[typing.Literal['HTTPS', 'WEBRTC', 'WSS']]]

### Role
- **Type**: typing.Optional[typing.Literal['MASTER', 'VIEWER']]


# SingleMasterConfigurationTypeDef

### MessageTtlSeconds
- **Type**: typing.Optional[int]


# StartEdgeConfigurationUpdateInputTypeDef

### EdgeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.EdgeConfigTypeDef'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# StartEdgeConfigurationUpdateOutputTypeDef

### StreamName
- **Type**: <class 'str'>
- **Required**: Yes

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### CreationTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### LastUpdatedTime
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### SyncStatus
- **Type**: typing.Literal['ACKNOWLEDGED', 'DELETE_FAILED', 'DELETING', 'DELETING_ACKNOWLEDGED', 'IN_SYNC', 'SYNCING', 'SYNC_FAILED']
- **Required**: Yes

### FailedStatusDetails
- **Type**: <class 'str'>
- **Required**: Yes

### EdgeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.EdgeConfigTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StreamInfoTypeDef

### DeviceName
- **Type**: typing.Optional[str]

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### MediaType
- **Type**: typing.Optional[str]

### KmsKeyId
- **Type**: typing.Optional[str]

### Version
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'UPDATING']]

### CreationTime
- **Type**: typing.Optional[datetime.datetime]

### DataRetentionInHours
- **Type**: typing.Optional[int]


# StreamNameConditionTypeDef

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH']]

### ComparisonValue
- **Type**: typing.Optional[str]


# TagResourceInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.kinesisvideo_classes.TagTypeDef]
- **Required**: Yes


# TagStreamInputTypeDef

### Tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes

### StreamARN
- **Type**: typing.Optional[str]

### StreamName
- **Type**: typing.Optional[str]


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# UntagResourceInputTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeyList
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UntagStreamInputTypeDef

### TagKeyList
- **Type**: typing.Sequence[str]
- **Required**: Yes

### StreamARN
- **Type**: typing.Optional[str]

### StreamName
- **Type**: typing.Optional[str]


# UpdateDataRetentionInputTypeDef

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### Operation
- **Type**: typing.Literal['DECREASE_DATA_RETENTION', 'INCREASE_DATA_RETENTION']
- **Required**: Yes

### DataRetentionChangeInHours
- **Type**: <class 'int'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# UpdateImageGenerationConfigurationInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### ImageGenerationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.ImageGenerationConfigurationUnionTypeDef]


# UpdateMediaStorageConfigurationInputTypeDef

### ChannelARN
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStorageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.MediaStorageConfigurationTypeDef'>
- **Required**: Yes


# UpdateNotificationConfigurationInputTypeDef

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### NotificationConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.NotificationConfigurationTypeDef]


# UpdateSignalingChannelInputTypeDef

### ChannelARN
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SingleMasterConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo_classes.SingleMasterConfigurationTypeDef]


# UpdateStreamInputTypeDef

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### DeviceName
- **Type**: typing.Optional[str]

### MediaType
- **Type**: typing.Optional[str]


# UploaderConfigTypeDef

### ScheduleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo_classes.ScheduleConfigTypeDef'>
- **Required**: Yes


