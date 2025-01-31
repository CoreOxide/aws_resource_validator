# Ivs Classes

# AudioConfigurationTypeDef

### channels
- **Type**: typing.Optional[int]

### codec
- **Type**: typing.Optional[str]

### sampleRate
- **Type**: typing.Optional[int]

### targetBitrate
- **Type**: typing.Optional[int]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchErrorTypeDef

### arn
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# BatchGetChannelRequestRequestTypeDef

### arns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetChannelResponseTypeDef

### channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_classes.ChannelTypeDef]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_classes.BatchErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchGetStreamKeyRequestRequestTypeDef

### arns
- **Type**: typing.Sequence[str]
- **Required**: Yes


# BatchGetStreamKeyResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_classes.BatchErrorTypeDef]
- **Required**: Yes

### streamKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_classes.StreamKeyTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchStartViewerSessionRevocationErrorTypeDef

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### viewerId
- **Type**: <class 'str'>
- **Required**: Yes

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# BatchStartViewerSessionRevocationRequestRequestTypeDef

### viewerSessions
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ivs_classes.BatchStartViewerSessionRevocationViewerSessionTypeDef]
- **Required**: Yes


# BatchStartViewerSessionRevocationResponseTypeDef

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_classes.BatchStartViewerSessionRevocationErrorTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# BatchStartViewerSessionRevocationViewerSessionTypeDef

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### viewerId
- **Type**: <class 'str'>
- **Required**: Yes

### viewerSessionVersionsLessThanOrEqualTo
- **Type**: typing.Optional[int]


# ChannelSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### authorized
- **Type**: typing.Optional[bool]

### insecureIngest
- **Type**: typing.Optional[bool]

### latencyMode
- **Type**: typing.Optional[typing.Literal['LOW', 'NORMAL']]

### name
- **Type**: typing.Optional[str]

### playbackRestrictionPolicyArn
- **Type**: typing.Optional[str]

### preset
- **Type**: typing.Optional[typing.Literal['CONSTRAINED_BANDWIDTH_DELIVERY', 'HIGHER_BANDWIDTH_DELIVERY']]

### recordingConfigurationArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### type
- **Type**: typing.Optional[typing.Literal['ADVANCED_HD', 'ADVANCED_SD', 'BASIC', 'STANDARD']]


# ChannelTypeDef

### arn
- **Type**: typing.Optional[str]

### authorized
- **Type**: typing.Optional[bool]

### ingestEndpoint
- **Type**: typing.Optional[str]

### insecureIngest
- **Type**: typing.Optional[bool]

### latencyMode
- **Type**: typing.Optional[typing.Literal['LOW', 'NORMAL']]

### name
- **Type**: typing.Optional[str]

### playbackRestrictionPolicyArn
- **Type**: typing.Optional[str]

### playbackUrl
- **Type**: typing.Optional[str]

### preset
- **Type**: typing.Optional[typing.Literal['CONSTRAINED_BANDWIDTH_DELIVERY', 'HIGHER_BANDWIDTH_DELIVERY']]

### recordingConfigurationArn
- **Type**: typing.Optional[str]

### srt
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.SrtTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### type
- **Type**: typing.Optional[typing.Literal['ADVANCED_HD', 'ADVANCED_SD', 'BASIC', 'STANDARD']]


# CreateChannelRequestRequestTypeDef

### authorized
- **Type**: typing.Optional[bool]

### insecureIngest
- **Type**: typing.Optional[bool]

### latencyMode
- **Type**: typing.Optional[typing.Literal['LOW', 'NORMAL']]

### name
- **Type**: typing.Optional[str]

### playbackRestrictionPolicyArn
- **Type**: typing.Optional[str]

### preset
- **Type**: typing.Optional[typing.Literal['CONSTRAINED_BANDWIDTH_DELIVERY', 'HIGHER_BANDWIDTH_DELIVERY']]

### recordingConfigurationArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### type
- **Type**: typing.Optional[typing.Literal['ADVANCED_HD', 'ADVANCED_SD', 'BASIC', 'STANDARD']]


# CreateChannelResponseTypeDef

### channel
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ChannelTypeDef'>
- **Required**: Yes

### streamKey
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.StreamKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreatePlaybackRestrictionPolicyRequestRequestTypeDef

### allowedCountries
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedOrigins
- **Type**: typing.Optional[typing.Sequence[str]]

### enableStrictOriginEnforcement
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreatePlaybackRestrictionPolicyResponseTypeDef

### playbackRestrictionPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.PlaybackRestrictionPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateRecordingConfigurationRequestRequestTypeDef

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.DestinationConfigurationTypeDef'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### recordingReconnectWindowSeconds
- **Type**: typing.Optional[int]

### renditionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.RenditionConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### thumbnailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.ThumbnailConfigurationTypeDef]


# CreateRecordingConfigurationResponseTypeDef

### recordingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.RecordingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStreamKeyRequestRequestTypeDef

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateStreamKeyResponseTypeDef

### streamKey
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.StreamKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteChannelRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePlaybackKeyPairRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePlaybackRestrictionPolicyRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecordingConfigurationRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStreamKeyRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationConfigurationTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.S3DestinationConfigurationTypeDef]


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetChannelRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelResponseTypeDef

### channel
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ChannelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPlaybackKeyPairRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPlaybackKeyPairResponseTypeDef

### keyPair
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.PlaybackKeyPairTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPlaybackRestrictionPolicyRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPlaybackRestrictionPolicyResponseTypeDef

### playbackRestrictionPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.PlaybackRestrictionPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetRecordingConfigurationRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecordingConfigurationResponseTypeDef

### recordingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.RecordingConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStreamKeyRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamKeyResponseTypeDef

### streamKey
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.StreamKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStreamRequestRequestTypeDef

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamResponseTypeDef

### stream
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.StreamTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStreamSessionRequestRequestTypeDef

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### streamId
- **Type**: typing.Optional[str]


# GetStreamSessionResponseTypeDef

### streamSession
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.StreamSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ImportPlaybackKeyPairRequestRequestTypeDef

### publicKeyMaterial
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ImportPlaybackKeyPairResponseTypeDef

### keyPair
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.PlaybackKeyPairTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IngestConfigurationTypeDef

### audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.AudioConfigurationTypeDef]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.VideoConfigurationTypeDef]


# ListChannelsRequestListChannelsPaginateTypeDef

### filterByName
- **Type**: typing.Optional[str]

### filterByPlaybackRestrictionPolicyArn
- **Type**: typing.Optional[str]

### filterByRecordingConfigurationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.PaginatorConfigTypeDef]


# ListChannelsRequestRequestTypeDef

### filterByName
- **Type**: typing.Optional[str]

### filterByPlaybackRestrictionPolicyArn
- **Type**: typing.Optional[str]

### filterByRecordingConfigurationArn
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListChannelsResponseTypeDef

### channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_classes.ChannelSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPlaybackKeyPairsRequestListPlaybackKeyPairsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.PaginatorConfigTypeDef]


# ListPlaybackKeyPairsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPlaybackKeyPairsResponseTypeDef

### keyPairs
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_classes.PlaybackKeyPairSummaryTypeDef]
- **Required**: Yes

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListPlaybackRestrictionPoliciesRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPlaybackRestrictionPoliciesResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### playbackRestrictionPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_classes.PlaybackRestrictionPolicySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListRecordingConfigurationsRequestListRecordingConfigurationsPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.PaginatorConfigTypeDef]


# ListRecordingConfigurationsRequestRequestTypeDef

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRecordingConfigurationsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### recordingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_classes.RecordingConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStreamKeysRequestListStreamKeysPaginateTypeDef

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.PaginatorConfigTypeDef]


# ListStreamKeysRequestRequestTypeDef

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStreamKeysResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### streamKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_classes.StreamKeySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStreamSessionsRequestRequestTypeDef

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStreamSessionsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### streamSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_classes.StreamSessionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListStreamsRequestListStreamsPaginateTypeDef

### filterBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.StreamFiltersTypeDef]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.PaginatorConfigTypeDef]


# ListStreamsRequestRequestTypeDef

### filterBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.StreamFiltersTypeDef]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStreamsResponseTypeDef

### nextToken
- **Type**: <class 'str'>
- **Required**: Yes

### streams
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_classes.StreamSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# ListTagsForResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlaybackKeyPairSummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PlaybackKeyPairTypeDef

### arn
- **Type**: typing.Optional[str]

### fingerprint
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PlaybackRestrictionPolicySummaryTypeDef

### allowedCountries
- **Type**: typing.List[str]
- **Required**: Yes

### allowedOrigins
- **Type**: typing.List[str]
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### enableStrictOriginEnforcement
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PlaybackRestrictionPolicyTypeDef

### allowedCountries
- **Type**: typing.List[str]
- **Required**: Yes

### allowedOrigins
- **Type**: typing.List[str]
- **Required**: Yes

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### enableStrictOriginEnforcement
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PutMetadataRequestRequestTypeDef

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'str'>
- **Required**: Yes


# RecordingConfigurationSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.DestinationConfigurationTypeDef'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# RecordingConfigurationTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.DestinationConfigurationTypeDef'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### recordingReconnectWindowSeconds
- **Type**: typing.Optional[int]

### renditionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.RenditionConfigurationOutputTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### thumbnailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.ThumbnailConfigurationOutputTypeDef]


# RenditionConfigurationOutputTypeDef

### renditionSelection
- **Type**: typing.Optional[typing.Literal['ALL', 'CUSTOM', 'NONE']]

### renditions
- **Type**: typing.Optional[typing.List[typing.Literal['FULL_HD', 'HD', 'LOWEST_RESOLUTION', 'SD']]]


# RenditionConfigurationTypeDef

### renditionSelection
- **Type**: typing.Optional[typing.Literal['ALL', 'CUSTOM', 'NONE']]

### renditions
- **Type**: typing.Optional[typing.Sequence[typing.Literal['FULL_HD', 'HD', 'LOWEST_RESOLUTION', 'SD']]]


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


# S3DestinationConfigurationTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# SrtTypeDef

### endpoint
- **Type**: typing.Optional[str]

### passphrase
- **Type**: typing.Optional[str]


# StartViewerSessionRevocationRequestRequestTypeDef

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### viewerId
- **Type**: <class 'str'>
- **Required**: Yes

### viewerSessionVersionsLessThanOrEqualTo
- **Type**: typing.Optional[int]


# StopStreamRequestRequestTypeDef

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes


# StreamEventTypeDef

### eventTime
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# StreamFiltersTypeDef

### health
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'STARVING', 'UNKNOWN']]


# StreamKeySummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### channelArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StreamKeyTypeDef

### arn
- **Type**: typing.Optional[str]

### channelArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### value
- **Type**: typing.Optional[str]


# StreamSessionSummaryTypeDef

### endTime
- **Type**: typing.Optional[datetime.datetime]

### hasErrorEvent
- **Type**: typing.Optional[bool]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### streamId
- **Type**: typing.Optional[str]


# StreamSessionTypeDef

### channel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.ChannelTypeDef]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### ingestConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.IngestConfigurationTypeDef]

### recordingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_classes.RecordingConfigurationTypeDef]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### streamId
- **Type**: typing.Optional[str]

### truncatedEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ivs_classes.StreamEventTypeDef]]


# StreamSummaryTypeDef

### channelArn
- **Type**: typing.Optional[str]

### health
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'STARVING', 'UNKNOWN']]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### state
- **Type**: typing.Optional[typing.Literal['LIVE', 'OFFLINE']]

### streamId
- **Type**: typing.Optional[str]

### viewerCount
- **Type**: typing.Optional[int]


# StreamTypeDef

### channelArn
- **Type**: typing.Optional[str]

### health
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'STARVING', 'UNKNOWN']]

### playbackUrl
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### state
- **Type**: typing.Optional[typing.Literal['LIVE', 'OFFLINE']]

### streamId
- **Type**: typing.Optional[str]

### viewerCount
- **Type**: typing.Optional[int]


# TagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# ThumbnailConfigurationOutputTypeDef

### recordingMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'INTERVAL']]

### resolution
- **Type**: typing.Optional[typing.Literal['FULL_HD', 'HD', 'LOWEST_RESOLUTION', 'SD']]

### storage
- **Type**: typing.Optional[typing.List[typing.Literal['LATEST', 'SEQUENTIAL']]]

### targetIntervalSeconds
- **Type**: typing.Optional[int]


# ThumbnailConfigurationTypeDef

### recordingMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'INTERVAL']]

### resolution
- **Type**: typing.Optional[typing.Literal['FULL_HD', 'HD', 'LOWEST_RESOLUTION', 'SD']]

### storage
- **Type**: typing.Optional[typing.Sequence[typing.Literal['LATEST', 'SEQUENTIAL']]]

### targetIntervalSeconds
- **Type**: typing.Optional[int]


# UntagResourceRequestRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateChannelRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### authorized
- **Type**: typing.Optional[bool]

### insecureIngest
- **Type**: typing.Optional[bool]

### latencyMode
- **Type**: typing.Optional[typing.Literal['LOW', 'NORMAL']]

### name
- **Type**: typing.Optional[str]

### playbackRestrictionPolicyArn
- **Type**: typing.Optional[str]

### preset
- **Type**: typing.Optional[typing.Literal['CONSTRAINED_BANDWIDTH_DELIVERY', 'HIGHER_BANDWIDTH_DELIVERY']]

### recordingConfigurationArn
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[typing.Literal['ADVANCED_HD', 'ADVANCED_SD', 'BASIC', 'STANDARD']]


# UpdateChannelResponseTypeDef

### channel
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ChannelTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdatePlaybackRestrictionPolicyRequestRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### allowedCountries
- **Type**: typing.Optional[typing.Sequence[str]]

### allowedOrigins
- **Type**: typing.Optional[typing.Sequence[str]]

### enableStrictOriginEnforcement
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]


# UpdatePlaybackRestrictionPolicyResponseTypeDef

### playbackRestrictionPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.PlaybackRestrictionPolicyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VideoConfigurationTypeDef

### avcLevel
- **Type**: typing.Optional[str]

### avcProfile
- **Type**: typing.Optional[str]

### codec
- **Type**: typing.Optional[str]

### encoder
- **Type**: typing.Optional[str]

### targetBitrate
- **Type**: typing.Optional[int]

### targetFramerate
- **Type**: typing.Optional[int]

### videoHeight
- **Type**: typing.Optional[int]

### videoWidth
- **Type**: typing.Optional[int]


