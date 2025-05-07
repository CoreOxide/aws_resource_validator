# Ivs Classes

# AudioConfiguration

### channels
- **Type**: typing.Optional[int]

### codec
- **Type**: typing.Optional[str]

### sampleRate
- **Type**: typing.Optional[int]

### targetBitrate
- **Type**: typing.Optional[int]

### track
- **Type**: typing.Optional[str]


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BatchError

### arn
- **Type**: typing.Optional[str]

### code
- **Type**: typing.Optional[str]

### message
- **Type**: typing.Optional[str]


# BatchGetChannelRequest

### arns
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetChannelResponse

### channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.Channel]
- **Required**: Yes

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.BatchError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# BatchGetStreamKeyRequest

### arns
- **Type**: typing.List[str]
- **Required**: Yes


# BatchGetStreamKeyResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.BatchError]
- **Required**: Yes

### streamKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.StreamKey]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# BatchStartViewerSessionRevocationError

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


# BatchStartViewerSessionRevocationRequest

### viewerSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.BatchStartViewerSessionRevocationViewerSession]
- **Required**: Yes


# BatchStartViewerSessionRevocationResponse

### errors
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.BatchStartViewerSessionRevocationError]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# BatchStartViewerSessionRevocationViewerSession

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### viewerId
- **Type**: <class 'str'>
- **Required**: Yes

### viewerSessionVersionsLessThanOrEqualTo
- **Type**: typing.Optional[int]


# Channel

### arn
- **Type**: typing.Optional[str]

### authorized
- **Type**: typing.Optional[bool]

### containerFormat
- **Type**: typing.Optional[typing.Literal['FRAGMENTED_MP4', 'TS']]

### ingestEndpoint
- **Type**: typing.Optional[str]

### insecureIngest
- **Type**: typing.Optional[bool]

### latencyMode
- **Type**: typing.Optional[typing.Literal['LOW', 'NORMAL']]

### multitrackInputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.MultitrackInputConfiguration]

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.Srt]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### type
- **Type**: typing.Optional[typing.Literal['ADVANCED_HD', 'ADVANCED_SD', 'BASIC', 'STANDARD']]


# ChannelSummary

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


# CreateChannelRequest

### authorized
- **Type**: typing.Optional[bool]

### containerFormat
- **Type**: typing.Optional[typing.Literal['FRAGMENTED_MP4', 'TS']]

### insecureIngest
- **Type**: typing.Optional[bool]

### latencyMode
- **Type**: typing.Optional[typing.Literal['LOW', 'NORMAL']]

### multitrackInputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.MultitrackInputConfiguration]

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


# CreateChannelResponse

### channel
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.Channel'>
- **Required**: Yes

### streamKey
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.StreamKey'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# CreatePlaybackRestrictionPolicyRequest

### allowedCountries
- **Type**: typing.Optional[typing.List[str]]

### allowedOrigins
- **Type**: typing.Optional[typing.List[str]]

### enableStrictOriginEnforcement
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreatePlaybackRestrictionPolicyResponse

### playbackRestrictionPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.PlaybackRestrictionPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateRecordingConfigurationRequest

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.DestinationConfiguration'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### recordingReconnectWindowSeconds
- **Type**: typing.Optional[int]

### renditionConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ivs.ivs_classes.RenditionConfiguration, aws_resource_validator.pydantic_models.ivs.ivs_classes.RenditionConfigurationOutput, NoneType]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### thumbnailConfiguration
- **Type**: typing.Union[aws_resource_validator.pydantic_models.ivs.ivs_classes.ThumbnailConfiguration, aws_resource_validator.pydantic_models.ivs.ivs_classes.ThumbnailConfigurationOutput, NoneType]


# CreateRecordingConfigurationResponse

### recordingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.RecordingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStreamKeyRequest

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# CreateStreamKeyResponse

### streamKey
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.StreamKey'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteChannelRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePlaybackKeyPairRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeletePlaybackRestrictionPolicyRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteRecordingConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStreamKeyRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationConfiguration

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.S3DestinationConfiguration]


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# GetChannelRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetChannelResponse

### channel
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.Channel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# GetPlaybackKeyPairRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPlaybackKeyPairResponse

### keyPair
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.PlaybackKeyPair'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# GetPlaybackRestrictionPolicyRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPlaybackRestrictionPolicyResponse

### playbackRestrictionPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.PlaybackRestrictionPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# GetRecordingConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetRecordingConfigurationResponse

### recordingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.RecordingConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# GetStreamKeyRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamKeyResponse

### streamKey
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.StreamKey'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# GetStreamRequest

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes


# GetStreamResponse

### stream
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.Stream'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# GetStreamSessionRequest

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### streamId
- **Type**: typing.Optional[str]


# GetStreamSessionResponse

### streamSession
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.StreamSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# ImportPlaybackKeyPairRequest

### publicKeyMaterial
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# ImportPlaybackKeyPairResponse

### keyPair
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.PlaybackKeyPair'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# IngestConfiguration

### audio
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.AudioConfiguration]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.VideoConfiguration]


# IngestConfigurations

### audioConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.AudioConfiguration]
- **Required**: Yes

### videoConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.VideoConfiguration]
- **Required**: Yes


# ListChannelsRequest

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


# ListChannelsRequestPaginate

### filterByName
- **Type**: typing.Optional[str]

### filterByPlaybackRestrictionPolicyArn
- **Type**: typing.Optional[str]

### filterByRecordingConfigurationArn
- **Type**: typing.Optional[str]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.PaginatorConfig]


# ListChannelsResponse

### channels
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.ChannelSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPlaybackKeyPairsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPlaybackKeyPairsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.PaginatorConfig]


# ListPlaybackKeyPairsResponse

### keyPairs
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.PlaybackKeyPairSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPlaybackRestrictionPoliciesRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListPlaybackRestrictionPoliciesResponse

### playbackRestrictionPolicies
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.PlaybackRestrictionPolicySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListRecordingConfigurationsRequest

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListRecordingConfigurationsRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.PaginatorConfig]


# ListRecordingConfigurationsResponse

### recordingConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.RecordingConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStreamKeysRequest

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStreamKeysRequestPaginate

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.PaginatorConfig]


# ListStreamKeysResponse

### streamKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.StreamKeySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStreamSessionsRequest

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStreamSessionsResponse

### streamSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.StreamSessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStreamsRequest

### filterBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.StreamFilters]

### maxResults
- **Type**: typing.Optional[int]

### nextToken
- **Type**: typing.Optional[str]


# ListStreamsRequestPaginate

### filterBy
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.StreamFilters]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.PaginatorConfig]


# ListStreamsResponse

### streams
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.StreamSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# MultitrackInputConfiguration

### enabled
- **Type**: typing.Optional[bool]

### maximumResolution
- **Type**: typing.Optional[typing.Literal['FULL_HD', 'HD', 'SD']]

### policy
- **Type**: typing.Optional[typing.Literal['ALLOW', 'REQUIRE']]


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# PlaybackKeyPair

### arn
- **Type**: typing.Optional[str]

### fingerprint
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PlaybackKeyPairSummary

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PlaybackRestrictionPolicy

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


# PlaybackRestrictionPolicySummary

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


# PutMetadataRequest

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### metadata
- **Type**: <class 'str'>
- **Required**: Yes


# RecordingConfiguration

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.DestinationConfiguration'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### recordingReconnectWindowSeconds
- **Type**: typing.Optional[int]

### renditionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.RenditionConfigurationOutput]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### thumbnailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.ThumbnailConfigurationOutput]


# RecordingConfigurationSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### destinationConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.DestinationConfiguration'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'CREATE_FAILED', 'CREATING']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# RenditionConfiguration

### renditionSelection
- **Type**: typing.Optional[typing.Literal['ALL', 'CUSTOM', 'NONE']]

### renditions
- **Type**: typing.Optional[typing.List[typing.Literal['FULL_HD', 'HD', 'LOWEST_RESOLUTION', 'SD']]]


# RenditionConfigurationOutput

### renditionSelection
- **Type**: typing.Optional[typing.Literal['ALL', 'CUSTOM', 'NONE']]

### renditions
- **Type**: typing.Optional[typing.List[typing.Literal['FULL_HD', 'HD', 'LOWEST_RESOLUTION', 'SD']]]


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


# S3DestinationConfiguration

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# Srt

### endpoint
- **Type**: typing.Optional[str]

### passphrase
- **Type**: typing.Optional[str]


# StartViewerSessionRevocationRequest

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### viewerId
- **Type**: <class 'str'>
- **Required**: Yes

### viewerSessionVersionsLessThanOrEqualTo
- **Type**: typing.Optional[int]


# StopStreamRequest

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes


# Stream

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


# StreamEvent

### code
- **Type**: typing.Optional[str]

### eventTime
- **Type**: typing.Optional[datetime.datetime]

### name
- **Type**: typing.Optional[str]

### type
- **Type**: typing.Optional[str]


# StreamFilters

### health
- **Type**: typing.Optional[typing.Literal['HEALTHY', 'STARVING', 'UNKNOWN']]


# StreamKey

### arn
- **Type**: typing.Optional[str]

### channelArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### value
- **Type**: typing.Optional[str]


# StreamKeySummary

### arn
- **Type**: typing.Optional[str]

### channelArn
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StreamSession

### channel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.Channel]

### endTime
- **Type**: typing.Optional[datetime.datetime]

### ingestConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.IngestConfiguration]

### ingestConfigurations
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.IngestConfigurations]

### recordingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.RecordingConfiguration]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### streamId
- **Type**: typing.Optional[str]

### truncatedEvents
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ivs.ivs_classes.StreamEvent]]


# StreamSessionSummary

### endTime
- **Type**: typing.Optional[datetime.datetime]

### hasErrorEvent
- **Type**: typing.Optional[bool]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### streamId
- **Type**: typing.Optional[str]


# StreamSummary

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


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes


# ThumbnailConfiguration

### recordingMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'INTERVAL']]

### resolution
- **Type**: typing.Optional[typing.Literal['FULL_HD', 'HD', 'LOWEST_RESOLUTION', 'SD']]

### storage
- **Type**: typing.Optional[typing.List[typing.Literal['LATEST', 'SEQUENTIAL']]]

### targetIntervalSeconds
- **Type**: typing.Optional[int]


# ThumbnailConfigurationOutput

### recordingMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'INTERVAL']]

### resolution
- **Type**: typing.Optional[typing.Literal['FULL_HD', 'HD', 'LOWEST_RESOLUTION', 'SD']]

### storage
- **Type**: typing.Optional[typing.List[typing.Literal['LATEST', 'SEQUENTIAL']]]

### targetIntervalSeconds
- **Type**: typing.Optional[int]


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.List[str]
- **Required**: Yes


# UpdateChannelRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### authorized
- **Type**: typing.Optional[bool]

### containerFormat
- **Type**: typing.Optional[typing.Literal['FRAGMENTED_MP4', 'TS']]

### insecureIngest
- **Type**: typing.Optional[bool]

### latencyMode
- **Type**: typing.Optional[typing.Literal['LOW', 'NORMAL']]

### multitrackInputConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs.ivs_classes.MultitrackInputConfiguration]

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


# UpdateChannelResponse

### channel
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.Channel'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# UpdatePlaybackRestrictionPolicyRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### allowedCountries
- **Type**: typing.Optional[typing.List[str]]

### allowedOrigins
- **Type**: typing.Optional[typing.List[str]]

### enableStrictOriginEnforcement
- **Type**: typing.Optional[bool]

### name
- **Type**: typing.Optional[str]


# UpdatePlaybackRestrictionPolicyResponse

### playbackRestrictionPolicy
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.PlaybackRestrictionPolicy'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs.ivs_classes.ResponseMetadata'>
- **Required**: Yes


# VideoConfiguration

### avcLevel
- **Type**: typing.Optional[str]

### avcProfile
- **Type**: typing.Optional[str]

### codec
- **Type**: typing.Optional[str]

### encoder
- **Type**: typing.Optional[str]

### level
- **Type**: typing.Optional[str]

### profile
- **Type**: typing.Optional[str]

### targetBitrate
- **Type**: typing.Optional[int]

### targetFramerate
- **Type**: typing.Optional[int]

### track
- **Type**: typing.Optional[str]

### videoHeight
- **Type**: typing.Optional[int]

### videoWidth
- **Type**: typing.Optional[int]


