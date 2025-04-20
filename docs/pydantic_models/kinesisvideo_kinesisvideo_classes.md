# Kinesisvideo Kinesisvideo Classes

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelInfo

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
- **Type**: <class 'NoneType'>

### Version
- **Type**: typing.Optional[str]


# ChannelNameCondition

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH']]

### ComparisonValue
- **Type**: typing.Optional[str]


# CreateSignalingChannelInput

### ChannelName
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelType
- **Type**: typing.Optional[typing.Literal['FULL_MESH', 'SINGLE_MASTER']]

### SingleMasterConfiguration
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.Tag]]


# CreateSignalingChannelOutput

### ChannelARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStreamInput

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
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateStreamOutput

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEdgeConfigurationInput

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DeleteSignalingChannelInput

### ChannelARN
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: typing.Optional[str]


# DeleteStreamInput

### StreamARN
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: typing.Optional[str]


# DeletionConfig

### EdgeRetentionInHours
- **Type**: typing.Optional[int]

### LocalSizeConfig
- **Type**: <class 'NoneType'>

### DeleteAfterUpload
- **Type**: typing.Optional[bool]


# DescribeEdgeConfigurationInput

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DescribeEdgeConfigurationOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.EdgeConfig'>
- **Required**: Yes

### EdgeAgentStatus
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.EdgeAgentStatus'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeImageGenerationConfigurationInput

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DescribeImageGenerationConfigurationOutput

### ImageGenerationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ImageGenerationConfigurationOutput'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeMappedResourceConfigurationInput

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# DescribeMappedResourceConfigurationInputPaginate

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.PaginatorConfig]


# DescribeMappedResourceConfigurationOutput

### MappedResourceConfigurationList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.MappedResourceConfigurationListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# DescribeMediaStorageConfigurationInput

### ChannelName
- **Type**: typing.Optional[str]

### ChannelARN
- **Type**: typing.Optional[str]


# DescribeMediaStorageConfigurationOutput

### MediaStorageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.MediaStorageConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeNotificationConfigurationInput

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DescribeNotificationConfigurationOutput

### NotificationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.NotificationConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeSignalingChannelInput

### ChannelName
- **Type**: typing.Optional[str]

### ChannelARN
- **Type**: typing.Optional[str]


# DescribeSignalingChannelOutput

### ChannelInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ChannelInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes


# DescribeStreamInput

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# DescribeStreamOutput

### StreamInfo
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.StreamInfo'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes


# EdgeAgentStatus

### LastRecorderStatus
- **Type**: <class 'NoneType'>

### LastUploaderStatus
- **Type**: <class 'NoneType'>


# EdgeConfig

### HubDeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### RecorderConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.RecorderConfig'>
- **Required**: Yes

### UploaderConfig
- **Type**: <class 'NoneType'>

### DeletionConfig
- **Type**: <class 'NoneType'>


# GetDataEndpointInput

### APIName
- **Type**: typing.Literal['GET_CLIP', 'GET_DASH_STREAMING_SESSION_URL', 'GET_HLS_STREAMING_SESSION_URL', 'GET_IMAGES', 'GET_MEDIA', 'GET_MEDIA_FOR_FRAGMENT_LIST', 'LIST_FRAGMENTS', 'PUT_MEDIA']
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# GetDataEndpointOutput

### DataEndpoint
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes


# GetSignalingChannelEndpointInput

### ChannelARN
- **Type**: <class 'str'>
- **Required**: Yes

### SingleMasterChannelEndpointConfiguration
- **Type**: <class 'NoneType'>


# GetSignalingChannelEndpointOutput

### ResourceEndpointList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResourceEndpointListItem]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes


# ImageGenerationConfiguration

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ImageSelectorType
- **Type**: typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']
- **Required**: Yes

### DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ImageGenerationDestinationConfig'>
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


# ImageGenerationConfigurationOutput

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### ImageSelectorType
- **Type**: typing.Literal['PRODUCER_TIMESTAMP', 'SERVER_TIMESTAMP']
- **Required**: Yes

### DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ImageGenerationDestinationConfig'>
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


# ImageGenerationDestinationConfig

### Uri
- **Type**: <class 'str'>
- **Required**: Yes

### DestinationRegion
- **Type**: <class 'str'>
- **Required**: Yes


# LastRecorderStatus

### JobStatusDetails
- **Type**: typing.Optional[str]

### LastCollectedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### RecorderStatus
- **Type**: typing.Optional[typing.Literal['SUCCESS', 'SYSTEM_ERROR', 'USER_ERROR']]


# LastUploaderStatus

### JobStatusDetails
- **Type**: typing.Optional[str]

### LastCollectedTime
- **Type**: typing.Optional[datetime.datetime]

### LastUpdatedTime
- **Type**: typing.Optional[datetime.datetime]

### UploaderStatus
- **Type**: typing.Optional[typing.Literal['SUCCESS', 'SYSTEM_ERROR', 'USER_ERROR']]


# ListEdgeAgentConfigurationsEdgeConfig

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
- **Type**: <class 'NoneType'>


# ListEdgeAgentConfigurationsInput

### HubDeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]


# ListEdgeAgentConfigurationsInputPaginate

### HubDeviceArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.PaginatorConfig]


# ListEdgeAgentConfigurationsOutput

### EdgeConfigs
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ListEdgeAgentConfigurationsEdgeConfig]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListSignalingChannelsInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### ChannelNameCondition
- **Type**: <class 'NoneType'>


# ListSignalingChannelsInputPaginate

### ChannelNameCondition
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.PaginatorConfig]


# ListSignalingChannelsOutput

### ChannelInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ChannelInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListStreamsInput

### MaxResults
- **Type**: typing.Optional[int]

### NextToken
- **Type**: typing.Optional[str]

### StreamNameCondition
- **Type**: <class 'NoneType'>


# ListStreamsInputPaginate

### StreamNameCondition
- **Type**: <class 'NoneType'>

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.PaginatorConfig]


# ListStreamsOutput

### StreamInfoList
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.StreamInfo]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceOutput

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForStreamInput

### NextToken
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### StreamName
- **Type**: typing.Optional[str]


# ListTagsForStreamOutput

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# LocalSizeConfig

### MaxLocalMediaSizeInMB
- **Type**: typing.Optional[int]

### StrategyOnFullSize
- **Type**: typing.Optional[typing.Literal['DELETE_OLDEST_MEDIA', 'DENY_NEW_MEDIA']]


# MappedResourceConfigurationListItem

### Type
- **Type**: typing.Optional[str]

### ARN
- **Type**: typing.Optional[str]


# MediaSourceConfig

### MediaUriSecretArn
- **Type**: <class 'str'>
- **Required**: Yes

### MediaUriType
- **Type**: typing.Literal['FILE_URI', 'RTSP_URI']
- **Required**: Yes


# MediaStorageConfiguration

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### StreamARN
- **Type**: typing.Optional[str]


# NotificationConfiguration

### Status
- **Type**: typing.Literal['DISABLED', 'ENABLED']
- **Required**: Yes

### DestinationConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.NotificationDestinationConfig'>
- **Required**: Yes


# NotificationDestinationConfig

### Uri
- **Type**: <class 'str'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# RecorderConfig

### MediaSourceConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.MediaSourceConfig'>
- **Required**: Yes

### ScheduleConfig
- **Type**: <class 'NoneType'>


# ResourceEndpointListItem

### Protocol
- **Type**: typing.Optional[typing.Literal['HTTPS', 'WEBRTC', 'WSS']]

### ResourceEndpoint
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


# ScheduleConfig

### ScheduleExpression
- **Type**: <class 'str'>
- **Required**: Yes

### DurationInSeconds
- **Type**: <class 'int'>
- **Required**: Yes


# SingleMasterChannelEndpointConfiguration

### Protocols
- **Type**: typing.Optional[typing.List[typing.Literal['HTTPS', 'WEBRTC', 'WSS']]]

### Role
- **Type**: typing.Optional[typing.Literal['MASTER', 'VIEWER']]


# SingleMasterConfiguration

### MessageTtlSeconds
- **Type**: typing.Optional[int]


# StartEdgeConfigurationUpdateInput

### EdgeConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.EdgeConfig'>
- **Required**: Yes

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]


# StartEdgeConfigurationUpdateOutput

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
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.EdgeConfig'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ResponseMetadata'>
- **Required**: Yes


# StreamInfo

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


# StreamNameCondition

### ComparisonOperator
- **Type**: typing.Optional[typing.Literal['BEGINS_WITH']]

### ComparisonValue
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.Tag]
- **Required**: Yes


# TagStreamInput

### Tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### StreamARN
- **Type**: typing.Optional[str]

### StreamName
- **Type**: typing.Optional[str]


# UntagResourceInput

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeyList
- **Type**: typing.List[str]
- **Required**: Yes


# UntagStreamInput

### TagKeyList
- **Type**: typing.List[str]
- **Required**: Yes

### StreamARN
- **Type**: typing.Optional[str]

### StreamName
- **Type**: typing.Optional[str]


# UpdateDataRetentionInput

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


# UpdateImageGenerationConfigurationInput

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### ImageGenerationConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ImageGenerationConfiguration, aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ImageGenerationConfigurationOutput, NoneType]


# UpdateMediaStorageConfigurationInput

### ChannelARN
- **Type**: <class 'str'>
- **Required**: Yes

### MediaStorageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.MediaStorageConfiguration'>
- **Required**: Yes


# UpdateNotificationConfigurationInput

### StreamName
- **Type**: typing.Optional[str]

### StreamARN
- **Type**: typing.Optional[str]

### NotificationConfiguration
- **Type**: <class 'NoneType'>


# UpdateSignalingChannelInput

### ChannelARN
- **Type**: <class 'str'>
- **Required**: Yes

### CurrentVersion
- **Type**: <class 'str'>
- **Required**: Yes

### SingleMasterConfiguration
- **Type**: <class 'NoneType'>


# UpdateStreamInput

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


# UploaderConfig

### ScheduleConfig
- **Type**: <class 'aws_resource_validator.pydantic_models.kinesisvideo.kinesisvideo_classes.ScheduleConfig'>
- **Required**: Yes


