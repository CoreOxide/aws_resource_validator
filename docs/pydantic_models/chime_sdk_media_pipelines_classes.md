# Chime Sdk Media Pipelines Classes

# ActiveSpeakerOnlyConfigurationTypeDef

### ActiveSpeakerPosition
- **Type**: typing.Optional[typing.Literal['BottomLeft', 'BottomRight', 'TopLeft', 'TopRight']]


# AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef

### LanguageCode
- **Type**: typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-US', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'pt-BR']
- **Required**: Yes

### VocabularyName
- **Type**: typing.Optional[str]

### VocabularyFilterName
- **Type**: typing.Optional[str]

### VocabularyFilterMethod
- **Type**: typing.Optional[typing.Literal['mask', 'remove', 'tag']]

### LanguageModelName
- **Type**: typing.Optional[str]

### EnablePartialResultsStabilization
- **Type**: typing.Optional[bool]

### PartialResultsStability
- **Type**: typing.Optional[typing.Literal['high', 'low', 'medium']]

### ContentIdentificationType
- **Type**: typing.Optional[typing.Literal['PII']]

### ContentRedactionType
- **Type**: typing.Optional[typing.Literal['PII']]

### PiiEntityTypes
- **Type**: typing.Optional[str]

### FilterPartialResults
- **Type**: typing.Optional[bool]

### PostCallAnalyticsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.PostCallAnalyticsSettingsTypeDef]

### CallAnalyticsStreamCategories
- **Type**: typing.Optional[typing.List[str]]


# AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef

### LanguageCode
- **Type**: typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-US', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'pt-BR']
- **Required**: Yes

### VocabularyName
- **Type**: typing.Optional[str]

### VocabularyFilterName
- **Type**: typing.Optional[str]

### VocabularyFilterMethod
- **Type**: typing.Optional[typing.Literal['mask', 'remove', 'tag']]

### LanguageModelName
- **Type**: typing.Optional[str]

### EnablePartialResultsStabilization
- **Type**: typing.Optional[bool]

### PartialResultsStability
- **Type**: typing.Optional[typing.Literal['high', 'low', 'medium']]

### ContentIdentificationType
- **Type**: typing.Optional[typing.Literal['PII']]

### ContentRedactionType
- **Type**: typing.Optional[typing.Literal['PII']]

### PiiEntityTypes
- **Type**: typing.Optional[str]

### FilterPartialResults
- **Type**: typing.Optional[bool]

### PostCallAnalyticsSettings
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.PostCallAnalyticsSettingsTypeDef]

### CallAnalyticsStreamCategories
- **Type**: typing.Optional[typing.Sequence[str]]


# AmazonTranscribeProcessorConfigurationTypeDef

### LanguageCode
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-US', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'pt-BR']]

### VocabularyName
- **Type**: typing.Optional[str]

### VocabularyFilterName
- **Type**: typing.Optional[str]

### VocabularyFilterMethod
- **Type**: typing.Optional[typing.Literal['mask', 'remove', 'tag']]

### ShowSpeakerLabel
- **Type**: typing.Optional[bool]

### EnablePartialResultsStabilization
- **Type**: typing.Optional[bool]

### PartialResultsStability
- **Type**: typing.Optional[typing.Literal['high', 'low', 'medium']]

### ContentIdentificationType
- **Type**: typing.Optional[typing.Literal['PII']]

### ContentRedactionType
- **Type**: typing.Optional[typing.Literal['PII']]

### PiiEntityTypes
- **Type**: typing.Optional[str]

### LanguageModelName
- **Type**: typing.Optional[str]

### FilterPartialResults
- **Type**: typing.Optional[bool]

### IdentifyLanguage
- **Type**: typing.Optional[bool]

### IdentifyMultipleLanguages
- **Type**: typing.Optional[bool]

### LanguageOptions
- **Type**: typing.Optional[str]

### PreferredLanguage
- **Type**: typing.Optional[typing.Literal['de-DE', 'en-AU', 'en-GB', 'en-US', 'es-US', 'fr-CA', 'fr-FR', 'it-IT', 'pt-BR']]

### VocabularyNames
- **Type**: typing.Optional[str]

### VocabularyFilterNames
- **Type**: typing.Optional[str]


# ArtifactsConcatenationConfigurationTypeDef

### Audio
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.AudioConcatenationConfigurationTypeDef'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VideoConcatenationConfigurationTypeDef'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ContentConcatenationConfigurationTypeDef'>
- **Required**: Yes

### DataChannel
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.DataChannelConcatenationConfigurationTypeDef'>
- **Required**: Yes

### TranscriptionMessages
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TranscriptionMessagesConcatenationConfigurationTypeDef'>
- **Required**: Yes

### MeetingEvents
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MeetingEventsConcatenationConfigurationTypeDef'>
- **Required**: Yes

### CompositedVideo
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.CompositedVideoConcatenationConfigurationTypeDef'>
- **Required**: Yes


# ArtifactsConfigurationTypeDef

### Audio
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.AudioArtifactsConfigurationTypeDef'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VideoArtifactsConfigurationTypeDef'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ContentArtifactsConfigurationTypeDef'>
- **Required**: Yes

### CompositedVideo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.CompositedVideoArtifactsConfigurationTypeDef]


# AudioArtifactsConfigurationTypeDef

### MuxType
- **Type**: typing.Literal['AudioOnly', 'AudioWithActiveSpeakerVideo', 'AudioWithCompositedVideo']
- **Required**: Yes


# AudioConcatenationConfigurationTypeDef

### State
- **Type**: typing.Literal['Enabled']
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelDefinitionTypeDef

### ChannelId
- **Type**: <class 'int'>
- **Required**: Yes

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]


# ChimeSdkMeetingConcatenationConfigurationTypeDef

### ArtifactsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ArtifactsConcatenationConfigurationTypeDef'>
- **Required**: Yes


# ChimeSdkMeetingConfigurationOutputTypeDef

### SourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SourceConfigurationOutputTypeDef]

### ArtifactsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ArtifactsConfigurationTypeDef]


# ChimeSdkMeetingConfigurationTypeDef

### SourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SourceConfigurationTypeDef]

### ArtifactsConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ArtifactsConfigurationTypeDef]


# ChimeSdkMeetingConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### MuxType
- **Type**: typing.Literal['AudioWithActiveSpeakerVideo', 'AudioWithCompositedVideo']
- **Required**: Yes

### CompositedVideo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.CompositedVideoArtifactsConfigurationTypeDef]

### SourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SourceConfigurationOutputTypeDef]


# ChimeSdkMeetingLiveConnectorConfigurationTypeDef

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### MuxType
- **Type**: typing.Literal['AudioWithActiveSpeakerVideo', 'AudioWithCompositedVideo']
- **Required**: Yes

### CompositedVideo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.CompositedVideoArtifactsConfigurationTypeDef]

### SourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SourceConfigurationUnionTypeDef]


# ChimeSdkMeetingLiveConnectorConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CompositedVideoArtifactsConfigurationTypeDef

### GridViewConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.GridViewConfigurationTypeDef'>
- **Required**: Yes

### Layout
- **Type**: typing.Optional[typing.Literal['GridView']]

### Resolution
- **Type**: typing.Optional[typing.Literal['FHD', 'HD']]


# CompositedVideoConcatenationConfigurationTypeDef

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# ConcatenationSinkTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConcatenationSourceTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContentArtifactsConfigurationTypeDef

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### MuxType
- **Type**: typing.Optional[typing.Literal['ContentOnly']]


# ContentConcatenationConfigurationTypeDef

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# CreateMediaCapturePipelineRequestTypeDef

### SourceType
- **Type**: typing.Literal['ChimeSdkMeeting']
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes

### SinkType
- **Type**: typing.Literal['S3Bucket']
- **Required**: Yes

### SinkArn
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### ChimeSdkMeetingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChimeSdkMeetingConfigurationUnionTypeDef]

### SseAwsKeyManagementParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SseAwsKeyManagementParamsTypeDef]

### SinkIamRoleArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TagTypeDef]]


# CreateMediaCapturePipelineResponseTypeDef

### MediaCapturePipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaCapturePipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMediaConcatenationPipelineRequestTypeDef

### Sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ConcatenationSourceTypeDef]
- **Required**: Yes

### Sinks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ConcatenationSinkTypeDef]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TagTypeDef]]


# CreateMediaConcatenationPipelineResponseTypeDef

### MediaConcatenationPipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaConcatenationPipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMediaInsightsPipelineConfigurationRequestTypeDef

### MediaInsightsPipelineConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Elements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationElementUnionTypeDef]
- **Required**: Yes

### RealTimeAlertConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RealTimeAlertConfigurationUnionTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TagTypeDef]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateMediaInsightsPipelineConfigurationResponseTypeDef

### MediaInsightsPipelineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMediaInsightsPipelineRequestTypeDef

### MediaInsightsPipelineConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### KinesisVideoStreamSourceRuntimeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamSourceRuntimeConfigurationUnionTypeDef]

### MediaInsightsRuntimeMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### KinesisVideoStreamRecordingSourceRuntimeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamRecordingSourceRuntimeConfigurationUnionTypeDef]

### S3RecordingSinkRuntimeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.S3RecordingSinkRuntimeConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TagTypeDef]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateMediaInsightsPipelineResponseTypeDef

### MediaInsightsPipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMediaLiveConnectorPipelineRequestTypeDef

### Sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LiveConnectorSourceConfigurationUnionTypeDef]
- **Required**: Yes

### Sinks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LiveConnectorSinkConfigurationTypeDef]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TagTypeDef]]


# CreateMediaLiveConnectorPipelineResponseTypeDef

### MediaLiveConnectorPipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaLiveConnectorPipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMediaPipelineKinesisVideoStreamPoolRequestTypeDef

### StreamConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamConfigurationTypeDef'>
- **Required**: Yes

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TagTypeDef]]


# CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef

### KinesisVideoStreamPoolConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamPoolConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMediaStreamPipelineRequestTypeDef

### Sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaStreamSourceTypeDef]
- **Required**: Yes

### Sinks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaStreamSinkTypeDef]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TagTypeDef]]


# CreateMediaStreamPipelineResponseTypeDef

### MediaStreamPipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaStreamPipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# DataChannelConcatenationConfigurationTypeDef

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# DeleteMediaCapturePipelineRequestTypeDef

### MediaPipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMediaInsightsPipelineConfigurationRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMediaPipelineKinesisVideoStreamPoolRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMediaPipelineRequestTypeDef

### MediaPipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadataTypeDef

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# FragmentSelectorOutputTypeDef

### FragmentSelectorType
- **Type**: typing.Literal['ProducerTimestamp', 'ServerTimestamp']
- **Required**: Yes

### TimestampRange
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TimestampRangeOutputTypeDef'>
- **Required**: Yes


# FragmentSelectorTypeDef

### FragmentSelectorType
- **Type**: typing.Literal['ProducerTimestamp', 'ServerTimestamp']
- **Required**: Yes

### TimestampRange
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TimestampRangeTypeDef'>
- **Required**: Yes


# GetMediaCapturePipelineRequestTypeDef

### MediaPipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaCapturePipelineResponseTypeDef

### MediaCapturePipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaCapturePipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMediaInsightsPipelineConfigurationRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaInsightsPipelineConfigurationResponseTypeDef

### MediaInsightsPipelineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMediaPipelineKinesisVideoStreamPoolRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef

### KinesisVideoStreamPoolConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamPoolConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetMediaPipelineRequestTypeDef

### MediaPipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaPipelineResponseTypeDef

### MediaPipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaPipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetSpeakerSearchTaskRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSpeakerSearchTaskResponseTypeDef

### SpeakerSearchTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SpeakerSearchTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GetVoiceToneAnalysisTaskRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceToneAnalysisTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceToneAnalysisTaskResponseTypeDef

### VoiceToneAnalysisTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VoiceToneAnalysisTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# GridViewConfigurationTypeDef

### ContentShareLayout
- **Type**: typing.Literal['ActiveSpeakerOnly', 'Horizontal', 'PresenterOnly', 'Vertical']
- **Required**: Yes

### PresenterOnlyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.PresenterOnlyConfigurationTypeDef]

### ActiveSpeakerOnlyConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ActiveSpeakerOnlyConfigurationTypeDef]

### HorizontalLayoutConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.HorizontalLayoutConfigurationTypeDef]

### VerticalLayoutConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VerticalLayoutConfigurationTypeDef]

### VideoAttribute
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VideoAttributeTypeDef]

### CanvasOrientation
- **Type**: typing.Optional[typing.Literal['Landscape', 'Portrait']]


# HorizontalLayoutConfigurationTypeDef

### TileOrder
- **Type**: typing.Optional[typing.Literal['JoinSequence', 'SpeakerSequence']]

### TilePosition
- **Type**: typing.Optional[typing.Literal['Bottom', 'Top']]

### TileCount
- **Type**: typing.Optional[int]

### TileAspectRatio
- **Type**: typing.Optional[str]


# IssueDetectionConfigurationTypeDef

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes


# KeywordMatchConfigurationOutputTypeDef

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### Keywords
- **Type**: typing.List[str]
- **Required**: Yes

### Negate
- **Type**: typing.Optional[bool]


# KeywordMatchConfigurationTypeDef

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### Keywords
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Negate
- **Type**: typing.Optional[bool]


# KinesisDataStreamSinkConfigurationTypeDef

### InsightsTarget
- **Type**: typing.Optional[str]


# KinesisVideoStreamConfigurationTypeDef

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### DataRetentionInHours
- **Type**: typing.Optional[int]


# KinesisVideoStreamConfigurationUpdateTypeDef

### DataRetentionInHours
- **Type**: typing.Optional[int]


# KinesisVideoStreamPoolConfigurationTypeDef

### PoolArn
- **Type**: typing.Optional[str]

### PoolName
- **Type**: typing.Optional[str]

### PoolId
- **Type**: typing.Optional[str]

### PoolStatus
- **Type**: typing.Optional[typing.Literal['ACTIVE', 'CREATING', 'DELETING', 'FAILED', 'UPDATING']]

### PoolSize
- **Type**: typing.Optional[int]

### StreamConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamConfigurationTypeDef]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# KinesisVideoStreamPoolSummaryTypeDef

### PoolName
- **Type**: typing.Optional[str]

### PoolId
- **Type**: typing.Optional[str]

### PoolArn
- **Type**: typing.Optional[str]


# KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef

### Streams
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RecordingStreamConfigurationTypeDef]
- **Required**: Yes

### FragmentSelector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.FragmentSelectorOutputTypeDef'>
- **Required**: Yes


# KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef

### Streams
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RecordingStreamConfigurationTypeDef]
- **Required**: Yes

### FragmentSelector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.FragmentSelectorTypeDef'>
- **Required**: Yes


# KinesisVideoStreamRecordingSourceRuntimeConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef

### Streams
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.StreamConfigurationOutputTypeDef]
- **Required**: Yes

### MediaEncoding
- **Type**: typing.Literal['pcm']
- **Required**: Yes

### MediaSampleRate
- **Type**: <class 'int'>
- **Required**: Yes


# KinesisVideoStreamSourceRuntimeConfigurationTypeDef

### Streams
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.StreamConfigurationTypeDef]
- **Required**: Yes

### MediaEncoding
- **Type**: typing.Literal['pcm']
- **Required**: Yes

### MediaSampleRate
- **Type**: <class 'int'>
- **Required**: Yes


# KinesisVideoStreamSourceRuntimeConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KinesisVideoStreamSourceTaskConfigurationTypeDef

### StreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelId
- **Type**: <class 'int'>
- **Required**: Yes

### FragmentNumber
- **Type**: typing.Optional[str]


# LambdaFunctionSinkConfigurationTypeDef

### InsightsTarget
- **Type**: typing.Optional[str]


# ListMediaCapturePipelinesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMediaCapturePipelinesResponseTypeDef

### MediaCapturePipelines
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaCapturePipelineSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMediaInsightsPipelineConfigurationsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMediaInsightsPipelineConfigurationsResponseTypeDef

### MediaInsightsPipelineConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMediaPipelineKinesisVideoStreamPoolsRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef

### KinesisVideoStreamPools
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamPoolSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMediaPipelinesRequestTypeDef

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMediaPipelinesResponseTypeDef

### MediaPipelines
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaPipelineSummaryTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponseTypeDef

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TagTypeDef]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# LiveConnectorRTMPConfigurationTypeDef

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### AudioChannels
- **Type**: typing.Optional[typing.Literal['Mono', 'Stereo']]

### AudioSampleRate
- **Type**: typing.Optional[str]


# LiveConnectorSinkConfigurationTypeDef

### SinkType
- **Type**: typing.Literal['RTMP']
- **Required**: Yes

### RTMPConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LiveConnectorRTMPConfigurationTypeDef'>
- **Required**: Yes


# LiveConnectorSourceConfigurationOutputTypeDef

### SourceType
- **Type**: typing.Literal['ChimeSdkMeeting']
- **Required**: Yes

### ChimeSdkMeetingLiveConnectorConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef'>
- **Required**: Yes


# LiveConnectorSourceConfigurationTypeDef

### SourceType
- **Type**: typing.Literal['ChimeSdkMeeting']
- **Required**: Yes

### ChimeSdkMeetingLiveConnectorConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChimeSdkMeetingLiveConnectorConfigurationUnionTypeDef'>
- **Required**: Yes


# LiveConnectorSourceConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MediaCapturePipelineSourceConfigurationTypeDef

### MediaPipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeSdkMeetingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChimeSdkMeetingConcatenationConfigurationTypeDef'>
- **Required**: Yes


# MediaCapturePipelineSummaryTypeDef

### MediaPipelineId
- **Type**: typing.Optional[str]

### MediaPipelineArn
- **Type**: typing.Optional[str]


# MediaCapturePipelineTypeDef

### MediaPipelineId
- **Type**: typing.Optional[str]

### MediaPipelineArn
- **Type**: typing.Optional[str]

### SourceType
- **Type**: typing.Optional[typing.Literal['ChimeSdkMeeting']]

### SourceArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Initializing', 'NotStarted', 'Paused', 'Stopped', 'Stopping']]

### SinkType
- **Type**: typing.Optional[typing.Literal['S3Bucket']]

### SinkArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ChimeSdkMeetingConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChimeSdkMeetingConfigurationOutputTypeDef]

### SseAwsKeyManagementParams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SseAwsKeyManagementParamsTypeDef]

### SinkIamRoleArn
- **Type**: typing.Optional[str]


# MediaConcatenationPipelineTypeDef

### MediaPipelineId
- **Type**: typing.Optional[str]

### MediaPipelineArn
- **Type**: typing.Optional[str]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ConcatenationSourceTypeDef]]

### Sinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ConcatenationSinkTypeDef]]

### Status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Initializing', 'NotStarted', 'Paused', 'Stopped', 'Stopping']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# MediaInsightsPipelineConfigurationElementOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MediaInsightsPipelineConfigurationElementUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MediaInsightsPipelineConfigurationSummaryTypeDef

### MediaInsightsPipelineConfigurationName
- **Type**: typing.Optional[str]

### MediaInsightsPipelineConfigurationId
- **Type**: typing.Optional[str]

### MediaInsightsPipelineConfigurationArn
- **Type**: typing.Optional[str]


# MediaInsightsPipelineConfigurationTypeDef

### MediaInsightsPipelineConfigurationName
- **Type**: typing.Optional[str]

### MediaInsightsPipelineConfigurationArn
- **Type**: typing.Optional[str]

### ResourceAccessRoleArn
- **Type**: typing.Optional[str]

### RealTimeAlertConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RealTimeAlertConfigurationOutputTypeDef]

### Elements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationElementOutputTypeDef]]

### MediaInsightsPipelineConfigurationId
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# MediaInsightsPipelineElementStatusTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MediaInsightsPipelineTypeDef

### MediaPipelineId
- **Type**: typing.Optional[str]

### MediaPipelineArn
- **Type**: typing.Optional[str]

### MediaInsightsPipelineConfigurationArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Initializing', 'NotStarted', 'Paused', 'Stopped', 'Stopping']]

### KinesisVideoStreamSourceRuntimeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef]

### MediaInsightsRuntimeMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### KinesisVideoStreamRecordingSourceRuntimeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef]

### S3RecordingSinkRuntimeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.S3RecordingSinkRuntimeConfigurationTypeDef]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ElementStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineElementStatusTypeDef]]


# MediaLiveConnectorPipelineTypeDef

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LiveConnectorSourceConfigurationOutputTypeDef]]

### Sinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LiveConnectorSinkConfigurationTypeDef]]

### MediaPipelineId
- **Type**: typing.Optional[str]

### MediaPipelineArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Initializing', 'NotStarted', 'Paused', 'Stopped', 'Stopping']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# MediaPipelineSummaryTypeDef

### MediaPipelineId
- **Type**: typing.Optional[str]

### MediaPipelineArn
- **Type**: typing.Optional[str]


# MediaPipelineTypeDef

### MediaCapturePipeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaCapturePipelineTypeDef]

### MediaLiveConnectorPipeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaLiveConnectorPipelineTypeDef]

### MediaConcatenationPipeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaConcatenationPipelineTypeDef]

### MediaInsightsPipeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineTypeDef]

### MediaStreamPipeline
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaStreamPipelineTypeDef]


# MediaStreamPipelineTypeDef

### MediaPipelineId
- **Type**: typing.Optional[str]

### MediaPipelineArn
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### Status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Initializing', 'NotStarted', 'Paused', 'Stopped', 'Stopping']]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaStreamSourceTypeDef]]

### Sinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaStreamSinkTypeDef]]


# MediaStreamSinkTypeDef

### SinkArn
- **Type**: <class 'str'>
- **Required**: Yes

### SinkType
- **Type**: typing.Literal['KinesisVideoStreamPool']
- **Required**: Yes

### ReservedStreamCapacity
- **Type**: <class 'int'>
- **Required**: Yes

### MediaStreamType
- **Type**: typing.Literal['IndividualAudio', 'MixedAudio']
- **Required**: Yes


# MediaStreamSourceTypeDef

### SourceType
- **Type**: typing.Literal['ChimeSdkMeeting']
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# MeetingEventsConcatenationConfigurationTypeDef

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# PostCallAnalyticsSettingsTypeDef

### OutputLocation
- **Type**: <class 'str'>
- **Required**: Yes

### DataAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### ContentRedactionOutput
- **Type**: typing.Optional[typing.Literal['redacted', 'redacted_and_unredacted']]

### OutputEncryptionKMSKeyId
- **Type**: typing.Optional[str]


# PresenterOnlyConfigurationTypeDef

### PresenterPosition
- **Type**: typing.Optional[typing.Literal['BottomLeft', 'BottomRight', 'TopLeft', 'TopRight']]


# RealTimeAlertConfigurationOutputTypeDef

### Disabled
- **Type**: typing.Optional[bool]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RealTimeAlertRuleOutputTypeDef]]


# RealTimeAlertConfigurationTypeDef

### Disabled
- **Type**: typing.Optional[bool]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RealTimeAlertRuleTypeDef]]


# RealTimeAlertConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RealTimeAlertRuleOutputTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RealTimeAlertRuleTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecordingStreamConfigurationTypeDef

### StreamArn
- **Type**: typing.Optional[str]


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


# S3BucketSinkConfigurationTypeDef

### Destination
- **Type**: <class 'str'>
- **Required**: Yes


# S3RecordingSinkConfigurationTypeDef

### Destination
- **Type**: typing.Optional[str]

### RecordingFileFormat
- **Type**: typing.Optional[typing.Literal['Opus', 'Wav']]


# S3RecordingSinkRuntimeConfigurationTypeDef

### Destination
- **Type**: <class 'str'>
- **Required**: Yes

### RecordingFileFormat
- **Type**: typing.Literal['Opus', 'Wav']
- **Required**: Yes


# SelectedVideoStreamsOutputTypeDef

### AttendeeIds
- **Type**: typing.Optional[typing.List[str]]

### ExternalUserIds
- **Type**: typing.Optional[typing.List[str]]


# SelectedVideoStreamsTypeDef

### AttendeeIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ExternalUserIds
- **Type**: typing.Optional[typing.Sequence[str]]


# SelectedVideoStreamsUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SentimentConfigurationTypeDef

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### SentimentType
- **Type**: typing.Literal['NEGATIVE']
- **Required**: Yes

### TimePeriod
- **Type**: <class 'int'>
- **Required**: Yes


# SnsTopicSinkConfigurationTypeDef

### InsightsTarget
- **Type**: typing.Optional[str]


# SourceConfigurationOutputTypeDef

### SelectedVideoStreams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SelectedVideoStreamsOutputTypeDef]


# SourceConfigurationTypeDef

### SelectedVideoStreams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SelectedVideoStreamsUnionTypeDef]


# SourceConfigurationUnionTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SpeakerSearchTaskTypeDef

### SpeakerSearchTaskId
- **Type**: typing.Optional[str]

### SpeakerSearchTaskStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Initializing', 'NotStarted', 'Stopped', 'Stopping']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# SqsQueueSinkConfigurationTypeDef

### InsightsTarget
- **Type**: typing.Optional[str]


# SseAwsKeyManagementParamsTypeDef

### AwsKmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsKmsEncryptionContext
- **Type**: typing.Optional[str]


# StartSpeakerSearchTaskRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceProfileDomainArn
- **Type**: <class 'str'>
- **Required**: Yes

### KinesisVideoStreamSourceTaskConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamSourceTaskConfigurationTypeDef]

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartSpeakerSearchTaskResponseTypeDef

### SpeakerSearchTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SpeakerSearchTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StartVoiceToneAnalysisTaskRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['en-US']
- **Required**: Yes

### KinesisVideoStreamSourceTaskConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamSourceTaskConfigurationTypeDef]

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartVoiceToneAnalysisTaskResponseTypeDef

### VoiceToneAnalysisTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VoiceToneAnalysisTaskTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# StopSpeakerSearchTaskRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# StopVoiceToneAnalysisTaskRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceToneAnalysisTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# StreamChannelDefinitionOutputTypeDef

### NumberOfChannels
- **Type**: <class 'int'>
- **Required**: Yes

### ChannelDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChannelDefinitionTypeDef]]


# StreamChannelDefinitionTypeDef

### NumberOfChannels
- **Type**: <class 'int'>
- **Required**: Yes

### ChannelDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChannelDefinitionTypeDef]]


# StreamConfigurationOutputTypeDef

### StreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### StreamChannelDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.StreamChannelDefinitionOutputTypeDef'>
- **Required**: Yes

### FragmentNumber
- **Type**: typing.Optional[str]


# StreamConfigurationTypeDef

### StreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### StreamChannelDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.StreamChannelDefinitionTypeDef'>
- **Required**: Yes

### FragmentNumber
- **Type**: typing.Optional[str]


# TagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TagTypeDef]
- **Required**: Yes


# TagTypeDef

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TimestampRangeOutputTypeDef

### StartTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# TimestampRangeTypeDef

### StartTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TimestampTypeDef'>
- **Required**: Yes

### EndTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TimestampTypeDef'>
- **Required**: Yes


# TimestampTypeDef

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TranscriptionMessagesConcatenationConfigurationTypeDef

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# UntagResourceRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateMediaInsightsPipelineConfigurationRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Elements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationElementUnionTypeDef]
- **Required**: Yes

### RealTimeAlertConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RealTimeAlertConfigurationUnionTypeDef]


# UpdateMediaInsightsPipelineConfigurationResponseTypeDef

### MediaInsightsPipelineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMediaInsightsPipelineStatusRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Literal['Pause', 'Resume']
- **Required**: Yes


# UpdateMediaPipelineKinesisVideoStreamPoolRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### StreamConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamConfigurationUpdateTypeDef]


# UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef

### KinesisVideoStreamPoolConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamPoolConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# VerticalLayoutConfigurationTypeDef

### TileOrder
- **Type**: typing.Optional[typing.Literal['JoinSequence', 'SpeakerSequence']]

### TilePosition
- **Type**: typing.Optional[typing.Literal['Left', 'Right']]

### TileCount
- **Type**: typing.Optional[int]

### TileAspectRatio
- **Type**: typing.Optional[str]


# VideoArtifactsConfigurationTypeDef

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### MuxType
- **Type**: typing.Optional[typing.Literal['VideoOnly']]


# VideoAttributeTypeDef

### CornerRadius
- **Type**: typing.Optional[int]

### BorderColor
- **Type**: typing.Optional[typing.Literal['Black', 'Blue', 'Green', 'Red', 'White', 'Yellow']]

### HighlightColor
- **Type**: typing.Optional[typing.Literal['Black', 'Blue', 'Green', 'Red', 'White', 'Yellow']]

### BorderThickness
- **Type**: typing.Optional[int]


# VideoConcatenationConfigurationTypeDef

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# VoiceAnalyticsProcessorConfigurationTypeDef

### SpeakerSearchStatus
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### VoiceToneAnalysisStatus
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# VoiceEnhancementSinkConfigurationTypeDef

### Disabled
- **Type**: typing.Optional[bool]


# VoiceToneAnalysisTaskTypeDef

### VoiceToneAnalysisTaskId
- **Type**: typing.Optional[str]

### VoiceToneAnalysisTaskStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Initializing', 'NotStarted', 'Stopped', 'Stopping']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


