# Ivs Realtime Classes

# AutoParticipantRecordingConfigurationOutputTypeDef

### storageConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### mediaTypes
- **Type**: typing.Optional[typing.List[typing.Literal['AUDIO_ONLY', 'AUDIO_VIDEO', 'NONE']]]

### thumbnailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.ParticipantThumbnailConfigurationOutputTypeDef]

### recordingReconnectWindowSeconds
- **Type**: typing.Optional[int]


# AutoParticipantRecordingConfigurationTypeDef

### storageConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### mediaTypes
- **Type**: typing.Optional[typing.Sequence[typing.Literal['AUDIO_ONLY', 'AUDIO_VIDEO', 'NONE']]]

### thumbnailConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.ParticipantThumbnailConfigurationTypeDef]

### recordingReconnectWindowSeconds
- **Type**: typing.Optional[int]


# AutoParticipantRecordingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelDestinationConfigurationTypeDef

### channelArn
- **Type**: <class 'str'>
- **Required**: Yes

### encoderConfigurationArn
- **Type**: typing.Optional[str]


# CompositionSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.DestinationSummaryTypeDef]
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


# CompositionThumbnailConfigurationOutputTypeDef

### targetIntervalSeconds
- **Type**: typing.Optional[int]

### storage
- **Type**: typing.Optional[typing.List[typing.Literal['LATEST', 'SEQUENTIAL']]]


# CompositionThumbnailConfigurationTypeDef

### targetIntervalSeconds
- **Type**: typing.Optional[int]

### storage
- **Type**: typing.Optional[typing.Sequence[typing.Literal['LATEST', 'SEQUENTIAL']]]


# CompositionThumbnailConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CompositionTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.LayoutConfigurationTypeDef'>
- **Required**: Yes

### destinations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.DestinationTypeDef]
- **Required**: Yes

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# CreateEncoderConfigurationRequestTypeDef

### name
- **Type**: typing.Optional[str]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.VideoTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateEncoderConfigurationResponseTypeDef

### encoderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.EncoderConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateIngestConfigurationRequestTypeDef

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


# CreateIngestConfigurationResponseTypeDef

### ingestConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.IngestConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateParticipantTokenRequestTypeDef

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


# CreateParticipantTokenResponseTypeDef

### participantToken
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ParticipantTokenTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStageRequestTypeDef

### name
- **Type**: typing.Optional[str]

### participantTokenConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ivs_realtime_classes.ParticipantTokenConfigurationTypeDef]]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]

### autoParticipantRecordingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.AutoParticipantRecordingConfigurationUnionTypeDef]


# CreateStageResponseTypeDef

### stage
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.StageTypeDef'>
- **Required**: Yes

### participantTokens
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.ParticipantTokenTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateStorageConfigurationRequestTypeDef

### s3
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.S3StorageConfigurationTypeDef'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# CreateStorageConfigurationResponseTypeDef

### storageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.StorageConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DeleteEncoderConfigurationRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteIngestConfigurationRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### force
- **Type**: typing.Optional[bool]


# DeletePublicKeyRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStageRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteStorageConfigurationRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# DestinationConfigurationOutputTypeDef

### name
- **Type**: typing.Optional[str]

### channel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.ChannelDestinationConfigurationTypeDef]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.S3DestinationConfigurationOutputTypeDef]


# DestinationConfigurationTypeDef

### name
- **Type**: typing.Optional[str]

### channel
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.ChannelDestinationConfigurationTypeDef]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.S3DestinationConfigurationUnionTypeDef]


# DestinationConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DestinationDetailTypeDef

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.S3DetailTypeDef]


# DestinationSummaryTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DestinationTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# DisconnectParticipantRequestTypeDef

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### participantId
- **Type**: <class 'str'>
- **Required**: Yes

### reason
- **Type**: typing.Optional[str]


# EncoderConfigurationSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EncoderConfigurationTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### video
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.VideoTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# EventTypeDef

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


# GetCompositionRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetCompositionResponseTypeDef

### composition
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.CompositionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetEncoderConfigurationRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetEncoderConfigurationResponseTypeDef

### encoderConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.EncoderConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetIngestConfigurationRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetIngestConfigurationResponseTypeDef

### ingestConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.IngestConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetParticipantRequestTypeDef

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes

### participantId
- **Type**: <class 'str'>
- **Required**: Yes


# GetParticipantResponseTypeDef

### participant
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ParticipantTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetPublicKeyRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetPublicKeyResponseTypeDef

### publicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.PublicKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStageRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetStageResponseTypeDef

### stage
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.StageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStageSessionRequestTypeDef

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### sessionId
- **Type**: <class 'str'>
- **Required**: Yes


# GetStageSessionResponseTypeDef

### stageSession
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.StageSessionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetStorageConfigurationRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# GetStorageConfigurationResponseTypeDef

### storageConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.StorageConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GridConfigurationTypeDef

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


# ImportPublicKeyRequestTypeDef

### publicKeyMaterial
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# ImportPublicKeyResponseTypeDef

### publicKey
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.PublicKeyTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# IngestConfigurationSummaryTypeDef

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


# IngestConfigurationTypeDef

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


# LayoutConfigurationTypeDef

### grid
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.GridConfigurationTypeDef]

### pip
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.PipConfigurationTypeDef]


# ListCompositionsRequestTypeDef

### filterByStageArn
- **Type**: typing.Optional[str]

### filterByEncoderConfigurationArn
- **Type**: typing.Optional[str]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListCompositionsResponseTypeDef

### compositions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.CompositionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListEncoderConfigurationsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListEncoderConfigurationsResponseTypeDef

### encoderConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.EncoderConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListIngestConfigurationsRequestPaginateTypeDef

### filterByStageArn
- **Type**: typing.Optional[str]

### filterByState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.PaginatorConfigTypeDef]


# ListIngestConfigurationsRequestTypeDef

### filterByStageArn
- **Type**: typing.Optional[str]

### filterByState
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'INACTIVE']]

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListIngestConfigurationsResponseTypeDef

### ingestConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.IngestConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListParticipantEventsRequestTypeDef

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


# ListParticipantEventsResponseTypeDef

### events
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.EventTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListParticipantsRequestTypeDef

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


# ListParticipantsResponseTypeDef

### participants
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.ParticipantSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListPublicKeysRequestPaginateTypeDef

### PaginationConfig
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.PaginatorConfigTypeDef]


# ListPublicKeysRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListPublicKeysResponseTypeDef

### publicKeys
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.PublicKeySummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStageSessionsRequestTypeDef

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStageSessionsResponseTypeDef

### stageSessions
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.StageSessionSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStagesRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStagesResponseTypeDef

### stages
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.StageSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListStorageConfigurationsRequestTypeDef

### nextToken
- **Type**: typing.Optional[str]

### maxResults
- **Type**: typing.Optional[int]


# ListStorageConfigurationsResponseTypeDef

### storageConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.StorageConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### nextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### tags
- **Type**: typing.Dict[str, str]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# PaginatorConfigTypeDef

### MaxItems
- **Type**: typing.Optional[int]

### PageSize
- **Type**: typing.Optional[int]

### StartingToken
- **Type**: typing.Optional[str]


# ParticipantSummaryTypeDef

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


# ParticipantThumbnailConfigurationOutputTypeDef

### targetIntervalSeconds
- **Type**: typing.Optional[int]

### storage
- **Type**: typing.Optional[typing.List[typing.Literal['LATEST', 'SEQUENTIAL']]]

### recordingMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'INTERVAL']]


# ParticipantThumbnailConfigurationTypeDef

### targetIntervalSeconds
- **Type**: typing.Optional[int]

### storage
- **Type**: typing.Optional[typing.Sequence[typing.Literal['LATEST', 'SEQUENTIAL']]]

### recordingMode
- **Type**: typing.Optional[typing.Literal['DISABLED', 'INTERVAL']]


# ParticipantTokenConfigurationTypeDef

### duration
- **Type**: typing.Optional[int]

### userId
- **Type**: typing.Optional[str]

### attributes
- **Type**: typing.Optional[typing.Mapping[str, str]]

### capabilities
- **Type**: typing.Optional[typing.Sequence[typing.Literal['PUBLISH', 'SUBSCRIBE']]]


# ParticipantTokenTypeDef

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


# ParticipantTypeDef

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


# PipConfigurationTypeDef

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


# PublicKeySummaryTypeDef

### arn
- **Type**: typing.Optional[str]

### name
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# PublicKeyTypeDef

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


# RecordingConfigurationTypeDef

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


# S3DestinationConfigurationOutputTypeDef

### storageConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### encoderConfigurationArns
- **Type**: typing.List[str]
- **Required**: Yes

### recordingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.RecordingConfigurationTypeDef]

### thumbnailConfigurations
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.ivs_realtime_classes.CompositionThumbnailConfigurationOutputTypeDef]]


# S3DestinationConfigurationTypeDef

### storageConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### encoderConfigurationArns
- **Type**: typing.Sequence[str]
- **Required**: Yes

### recordingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.RecordingConfigurationTypeDef]

### thumbnailConfigurations
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.ivs_realtime_classes.CompositionThumbnailConfigurationUnionTypeDef]]


# S3DestinationConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# S3DetailTypeDef

### recordingPrefix
- **Type**: <class 'str'>
- **Required**: Yes


# S3StorageConfigurationTypeDef

### bucketName
- **Type**: <class 'str'>
- **Required**: Yes


# StageEndpointsTypeDef

### events
- **Type**: typing.Optional[str]

### whip
- **Type**: typing.Optional[str]

### rtmp
- **Type**: typing.Optional[str]

### rtmps
- **Type**: typing.Optional[str]


# StageSessionSummaryTypeDef

### sessionId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# StageSessionTypeDef

### sessionId
- **Type**: typing.Optional[str]

### startTime
- **Type**: typing.Optional[datetime.datetime]

### endTime
- **Type**: typing.Optional[datetime.datetime]


# StageSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### activeSessionId
- **Type**: typing.Optional[str]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StageTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.AutoParticipantRecordingConfigurationOutputTypeDef]

### endpoints
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.StageEndpointsTypeDef]


# StartCompositionRequestTypeDef

### stageArn
- **Type**: <class 'str'>
- **Required**: Yes

### destinations
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.ivs_realtime_classes.DestinationConfigurationUnionTypeDef]
- **Required**: Yes

### idempotencyToken
- **Type**: typing.Optional[str]

### layout
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.LayoutConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Mapping[str, str]]


# StartCompositionResponseTypeDef

### composition
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.CompositionTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopCompositionRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes


# StorageConfigurationSummaryTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.S3StorageConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# StorageConfigurationTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### s3
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.S3StorageConfigurationTypeDef]

### tags
- **Type**: typing.Optional[typing.Dict[str, str]]


# TagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tags
- **Type**: typing.Mapping[str, str]
- **Required**: Yes


# UntagResourceRequestTypeDef

### resourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### tagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateIngestConfigurationRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### stageArn
- **Type**: typing.Optional[str]


# UpdateIngestConfigurationResponseTypeDef

### ingestConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.IngestConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateStageRequestTypeDef

### arn
- **Type**: <class 'str'>
- **Required**: Yes

### name
- **Type**: typing.Optional[str]

### autoParticipantRecordingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.ivs_realtime_classes.AutoParticipantRecordingConfigurationUnionTypeDef]


# UpdateStageResponseTypeDef

### stage
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.StageTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.ivs_realtime_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VideoTypeDef

### width
- **Type**: typing.Optional[int]

### height
- **Type**: typing.Optional[int]

### framerate
- **Type**: typing.Optional[float]

### bitrate
- **Type**: typing.Optional[int]


