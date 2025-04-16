# Ivs Realtime Classes

# AutoParticipantRecordingConfiguration

### storageConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### mediaTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AUDIO_ONLY', 'AUDIO_VIDEO', 'NONE']]]

### thumbnailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.ParticipantThumbnailConfiguration]

### recordingReconnectWindowSeconds
- **Type**: typing.Optional[int]


# AutoParticipantRecordingConfigurationOutput

### storageConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### mediaTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AUDIO_ONLY', 'AUDIO_VIDEO', 'NONE']]]

### thumbnailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.ParticipantThumbnailConfigurationOutput]

### recordingReconnectWindowSeconds
- **Type**: typing.Optional[int]


# AutoParticipantRecordingConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelDestinationConfiguration

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### encoderConfigurationArn
- **Type**: typing.Optional[str]


# Composition

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'FAILED', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### layout
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.LayoutConfiguration'>
- **Required**: Yes

### destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.Destination]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# CompositionSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.DestinationSummary]
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'FAILED', 'STARTING', 'STOPPED', 'STOPPING']
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# CompositionThumbnailConfiguration

### targetIntervalSeconds
- **Type**: typing.Optional[int]

### storage
- **Type**: typing.Optional[typing.Sequence[typing.Literal['LATEST', 'SEQUENTIAL']]]


# CompositionThumbnailConfigurationOutput

### targetIntervalSeconds
- **Type**: typing.Optional[int]

### storage
- **Type**: typing.Optional[typing.List[typing.Literal['LATEST', 'SEQUENTIAL']]]


# CompositionThumbnailConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CreateEncoderConfigurationRequest

### name
- **Type**: typing.Optional[str]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.Video]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEncoderConfigurationResponse

### encoderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.EncoderConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# CreateIngestConfigurationRequest

### ingestProtocol
- **Type**: typing.Literal['RTMP', 'RTMPS']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### stageArn
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### insecureIngest
- **Type**: typing.Optional[bool]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateIngestConfigurationResponse

### ingestConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.IngestConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# CreateParticipantTokenRequest

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### duration
- **Type**: typing.Optional[int]

### userId
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### capabilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PUBLISH', 'SUBSCRIBE']]]


# CreateParticipantTokenResponse

### participantToken
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ParticipantToken'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStageRequest

### name
- **Type**: typing.Optional[str]

### participantTokenConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ivs_realtime_classes.ParticipantTokenConfiguration]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### autoParticipantRecordingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.AutoParticipantRecordingConfigurationUnion]


# CreateStageResponse

### stage
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.Stage'>
- **Required**: Yes

### participantTokens
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.ParticipantToken]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# CreateStorageConfigurationRequest

### s3
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.S3StorageConfiguration'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateStorageConfigurationResponse

### storageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.StorageConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# DeleteEncoderConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIngestConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeletePublicKeyRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStageRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStorageConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# Destination

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DestinationConfiguration

### name
- **Type**: typing.Optional[str]

### channel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.ChannelDestinationConfiguration]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.S3DestinationConfigurationUnion]


# DestinationConfigurationOutput

### name
- **Type**: typing.Optional[str]

### channel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.ChannelDestinationConfiguration]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.S3DestinationConfigurationOutput]


# DestinationConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DestinationDetail

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.S3Detail]


# DestinationSummary

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DisconnectParticipantRequest

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### participantId
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]


# EncoderConfiguration

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.Video]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EncoderConfigurationSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# Event

### name
- **Type**: typing.Optional[typing.Literal['JOINED', 'JOIN_ERROR', 'LEFT', 'PUBLISH_ERROR', 'PUBLISH_STARTED', 'PUBLISH_STOPPED', 'SUBSCRIBE_ERROR', 'SUBSCRIBE_STARTED', 'SUBSCRIBE_STOPPED']]

### participantId
- **Type**: typing.Optional[str]

### eventTime
- **Type**: typing.Optional[datetime.datetime]

### remoteParticipantId
- **Type**: typing.Optional[str]

### errorCode
- **Type**: typing.Optional[typing.Literal['BITRATE_EXCEEDED', 'B_FRAME_PRESENT', 'INSUFFICIENT_CAPABILITIES', 'INTERNAL_SERVER_EXCEPTION', 'INVALID_AUDIO_CODEC', 'INVALID_INPUT', 'INVALID_PROTOCOL', 'INVALID_STREAM_KEY', 'INVALID_VIDEO_CODEC', 'PUBLISHER_NOT_FOUND', 'QUOTA_EXCEEDED', 'RESOLUTION_EXCEEDED', 'REUSE_OF_STREAM_KEY', 'STREAM_DURATION_EXCEEDED']]


# GetCompositionRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCompositionResponse

### composition
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.Composition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# GetEncoderConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetEncoderConfigurationResponse

### encoderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.EncoderConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# GetIngestConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetIngestConfigurationResponse

### ingestConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.IngestConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# GetParticipantRequest

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### participantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetParticipantResponse

### participant
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.Participant'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# GetPublicKeyRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPublicKeyResponse

### publicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.PublicKey'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# GetStageRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetStageResponse

### stage
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.Stage'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# GetStageSessionRequest

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStageSessionResponse

### stageSession
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.StageSession'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# GetStorageConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageConfigurationResponse

### storageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.StorageConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# GridConfiguration

### featuredParticipantAttribute
- **Type**: typing.Optional[str]

### omitStoppedVideo
- **Type**: typing.Optional[bool]

### videoAspectRatio
- **Type**: typing.Optional[typing.Literal['AUTO', 'PORTRAIT', 'SQUARE', 'VIDEO']]

### videoFillMode
- **Type**: typing.Optional[typing.Literal['CONTAIN', 'COVER', 'FILL']]

### gridGap
- **Type**: typing.Optional[int]


# ImportPublicKeyRequest

### publicKeyMaterial
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ImportPublicKeyResponse

### publicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.PublicKey'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# IngestConfiguration

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ingestProtocol
- **Type**: typing.Literal['RTMP', 'RTMPS']
- **Required**: Yes

### streamKey
- **Type**: <class 'str'>
- **Required**: Yes

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### participantId
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# IngestConfigurationSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### ingestProtocol
- **Type**: typing.Literal['RTMP', 'RTMPS']
- **Required**: Yes

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### participantId
- **Type**: <class 'str'>
- **Required**: Yes

### state
- **Type**: typing.Literal['ACTIVE', 'INACTIVE']
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]


# LayoutConfiguration

### grid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.GridConfiguration]

### pip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.PipConfiguration]


# ListCompositionsRequest

### filterByStageArn
- **Type**: typing.Optional[str]

### filterByEncoderConfigurationArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCompositionsResponse

### compositions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.CompositionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEncoderConfigurationsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEncoderConfigurationsResponse

### encoderConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.EncoderConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIngestConfigurationsRequest

### filterByStageArn
- **Type**: typing.Optional[str]

### filterByState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListIngestConfigurationsRequestPaginate

### filterByStageArn
- **Type**: typing.Optional[str]

### filterByState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.PaginatorConfig]


# ListIngestConfigurationsResponse

### ingestConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.IngestConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListParticipantEventsRequest

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### participantId
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListParticipantEventsResponse

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.Event]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListParticipantsRequest

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### filterByUserId
- **Type**: typing.Optional[str]

### filterByPublished
- **Type**: typing.Optional[bool]

### filterByState
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'DISCONNECTED']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]

### filterByRecordingState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'FAILED', 'STARTING', 'STOPPED', 'STOPPING']]


# ListParticipantsResponse

### participants
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.ParticipantSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPublicKeysRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPublicKeysRequestPaginate

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.PaginatorConfig]


# ListPublicKeysResponse

### publicKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.PublicKeySummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStageSessionsRequest

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStageSessionsResponse

### stageSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.StageSessionSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStagesRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStagesResponse

### stages
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.StageSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStorageConfigurationsRequest

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStorageConfigurationsResponse

### storageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.StorageConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
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
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# PaginatorConfig

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# Participant

### participantId
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'DISCONNECTED']]

### firstJoinTime
- **Type**: typing.Optional[datetime.datetime]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### published
- **Type**: typing.Optional[bool]

### ispName
- **Type**: typing.Optional[str]

### osName
- **Type**: typing.Optional[str]

### osVersion
- **Type**: typing.Optional[str]

### browserName
- **Type**: typing.Optional[str]

### browserVersion
- **Type**: typing.Optional[str]

### sdkVersion
- **Type**: typing.Optional[str]

### recordingS3BucketName
- **Type**: typing.Optional[str]

### recordingS3Prefix
- **Type**: typing.Optional[str]

### recordingState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DISABLED', 'FAILED', 'STARTING', 'STOPPED', 'STOPPING']]

### protocol
- **Type**: typing.Optional[typing.Literal['RTMP', 'RTMPS', 'UNKNOWN', 'WHIP']]


# ParticipantSummary

### participantId
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### state
- **Type**: typing.Optional[typing.Literal['CONNECTED', 'DISCONNECTED']]

### firstJoinTime
- **Type**: typing.Optional[datetime.datetime]

### published
- **Type**: typing.Optional[bool]

### recordingState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'DISABLED', 'FAILED', 'STARTING', 'STOPPED', 'STOPPING']]


# ParticipantThumbnailConfiguration

### targetIntervalSeconds
- **Type**: typing.Optional[int]

### storage
- **Type**: typing.Optional[typing.Sequence[typing.Literal['LATEST', 'SEQUENTIAL']]]

### recordingMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'INTERVAL']]


# ParticipantThumbnailConfigurationOutput

### targetIntervalSeconds
- **Type**: typing.Optional[int]

### storage
- **Type**: typing.Optional[typing.List[typing.Literal['LATEST', 'SEQUENTIAL']]]

### recordingMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'INTERVAL']]


# ParticipantToken

### participantId
- **Type**: typing.Optional[str]

### token
- **Type**: typing.Optional[str]

### userId
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Dict[str, str]]

### duration
- **Type**: typing.Optional[int]

### capabilities
- **Type**: typing.Optional[typing.List[typing.Literal['PUBLISH', 'SUBSCRIBE']]]

### expirationTime
- **Type**: typing.Optional[datetime.datetime]


# ParticipantTokenConfiguration

### duration
- **Type**: typing.Optional[int]

### userId
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### capabilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PUBLISH', 'SUBSCRIBE']]]


# PipConfiguration

### featuredParticipantAttribute
- **Type**: typing.Optional[str]

### omitStoppedVideo
- **Type**: typing.Optional[bool]

### videoFillMode
- **Type**: typing.Optional[typing.Literal['CONTAIN', 'COVER', 'FILL']]

### gridGap
- **Type**: typing.Optional[int]

### pipParticipantAttribute
- **Type**: typing.Optional[str]

### pipBehavior
- **Type**: typing.Optional[typing.Literal['DYNAMIC', 'STATIC']]

### pipOffset
- **Type**: typing.Optional[int]

### pipPosition
- **Type**: typing.Optional[typing.Literal['BOTTOM_LEFT', 'BOTTOM_RIGHT', 'TOP_LEFT', 'TOP_RIGHT']]

### pipWidth
- **Type**: typing.Optional[int]

### pipHeight
- **Type**: typing.Optional[int]


# PublicKey

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### publicKeyMaterial
- **Type**: typing.Optional[str]

### fingerprint
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PublicKeySummary

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# RecordingConfiguration

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

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

### storageConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### encoderConfigurationArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### recordingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.RecordingConfiguration]

### thumbnailConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ivs_realtime_classes.CompositionThumbnailConfigurationUnion]]


# S3DestinationConfigurationOutput

### storageConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### encoderConfigurationArns
- **Type**: typing.List[str]
- **Required**: Yes

### recordingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.RecordingConfiguration]

### thumbnailConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.CompositionThumbnailConfigurationOutput]]


# S3DestinationConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3Detail

### recordingPrefix
- **Type**: <class 'str'>
- **Required**: Yes


# S3StorageConfiguration

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# Stage

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### activeSessionId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### autoParticipantRecordingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.AutoParticipantRecordingConfigurationOutput]

### endpoints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.StageEndpoints]


# StageEndpoints

### events
- **Type**: typing.Optional[str]

### whip
- **Type**: typing.Optional[str]

### rtmp
- **Type**: typing.Optional[str]

### rtmps
- **Type**: typing.Optional[str]


# StageSession

### sessionId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# StageSessionSummary

### sessionId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# StageSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### activeSessionId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StartCompositionRequest

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### destinations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ivs_realtime_classes.DestinationConfigurationUnion]
- **Required**: Yes

### idempotencyToken
- **Type**: typing.Optional[str]

### layout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.LayoutConfiguration]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartCompositionResponse

### composition
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.Composition'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# StopCompositionRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# StorageConfiguration

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.S3StorageConfiguration]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StorageConfigurationSummary

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.S3StorageConfiguration]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# TagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequest

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateIngestConfigurationRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### stageArn
- **Type**: typing.Optional[str]


# UpdateIngestConfigurationResponse

### ingestConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.IngestConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateStageRequest

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### autoParticipantRecordingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.AutoParticipantRecordingConfigurationUnion]


# UpdateStageResponse

### stage
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.Stage'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadata'>
- **Required**: Yes


# Video

### width
- **Type**: typing.Optional[int]

### height
- **Type**: typing.Optional[int]

### framerate
- **Type**: typing.Optional[float]

### bitrate
- **Type**: typing.Optional[int]


