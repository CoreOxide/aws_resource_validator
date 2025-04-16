# Chime Sdk Media Pipelines Classes

# ActiveSpeakerOnlyConfiguration

### ActiveSpeakerPosition
- **Type**: typing.Optional[typing.Literal['BottomLeft', 'BottomRight', 'TopLeft', 'TopRight']]


# AmazonTranscribeCallAnalyticsProcessorConfiguration

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
- **Type**: <class 'NoneType'>

### CallAnalyticsStreamCategories
- **Type**: typing.Optional[typing.Sequence[str]]


# AmazonTranscribeCallAnalyticsProcessorConfigurationOutput

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
- **Type**: <class 'NoneType'>

### CallAnalyticsStreamCategories
- **Type**: typing.Optional[typing.List[str]]


# AmazonTranscribeProcessorConfiguration

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


# ArtifactsConcatenationConfiguration

### Audio
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.AudioConcatenationConfiguration'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VideoConcatenationConfiguration'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ContentConcatenationConfiguration'>
- **Required**: Yes

### DataChannel
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.DataChannelConcatenationConfiguration'>
- **Required**: Yes

### TranscriptionMessages
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TranscriptionMessagesConcatenationConfiguration'>
- **Required**: Yes

### MeetingEvents
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MeetingEventsConcatenationConfiguration'>
- **Required**: Yes

### CompositedVideo
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.CompositedVideoConcatenationConfiguration'>
- **Required**: Yes


# ArtifactsConfiguration

### Audio
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.AudioArtifactsConfiguration'>
- **Required**: Yes

### Video
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VideoArtifactsConfiguration'>
- **Required**: Yes

### Content
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ContentArtifactsConfiguration'>
- **Required**: Yes

### CompositedVideo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.CompositedVideoArtifactsConfiguration]


# AudioArtifactsConfiguration

### MuxType
- **Type**: typing.Literal['AudioOnly', 'AudioWithActiveSpeakerVideo', 'AudioWithCompositedVideo']
- **Required**: Yes


# AudioConcatenationConfiguration

### State
- **Type**: typing.Literal['Enabled']
- **Required**: Yes


# BaseValidatorModel

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChannelDefinition

### ChannelId
- **Type**: <class 'int'>
- **Required**: Yes

### ParticipantRole
- **Type**: typing.Optional[typing.Literal['AGENT', 'CUSTOMER']]


# ChimeSdkMeetingConcatenationConfiguration

### ArtifactsConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ArtifactsConcatenationConfiguration'>
- **Required**: Yes


# ChimeSdkMeetingConfiguration

### SourceConfiguration
- **Type**: <class 'NoneType'>

### ArtifactsConfiguration
- **Type**: <class 'NoneType'>


# ChimeSdkMeetingConfigurationOutput

### SourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SourceConfigurationOutput]

### ArtifactsConfiguration
- **Type**: <class 'NoneType'>


# ChimeSdkMeetingConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ChimeSdkMeetingLiveConnectorConfiguration

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### MuxType
- **Type**: typing.Literal['AudioWithActiveSpeakerVideo', 'AudioWithCompositedVideo']
- **Required**: Yes

### CompositedVideo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.CompositedVideoArtifactsConfiguration]

### SourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SourceConfigurationUnion]


# ChimeSdkMeetingLiveConnectorConfigurationOutput

### Arn
- **Type**: <class 'str'>
- **Required**: Yes

### MuxType
- **Type**: typing.Literal['AudioWithActiveSpeakerVideo', 'AudioWithCompositedVideo']
- **Required**: Yes

### CompositedVideo
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.CompositedVideoArtifactsConfiguration]

### SourceConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SourceConfigurationOutput]


# ChimeSdkMeetingLiveConnectorConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# CompositedVideoArtifactsConfiguration

### GridViewConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.GridViewConfiguration'>
- **Required**: Yes

### Layout
- **Type**: typing.Optional[typing.Literal['GridView']]

### Resolution
- **Type**: typing.Optional[typing.Literal['FHD', 'HD']]


# CompositedVideoConcatenationConfiguration

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# ConcatenationSink

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ConcatenationSource

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# ContentArtifactsConfiguration

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### MuxType
- **Type**: typing.Optional[typing.Literal['ContentOnly']]


# ContentConcatenationConfiguration

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# CreateMediaCapturePipelineRequest

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChimeSdkMeetingConfigurationUnion]

### SseAwsKeyManagementParams
- **Type**: <class 'NoneType'>

### SinkIamRoleArn
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.Tag]]


# CreateMediaCapturePipelineResponse

### MediaCapturePipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaCapturePipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMediaConcatenationPipelineRequest

### Sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ConcatenationSource]
- **Required**: Yes

### Sinks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ConcatenationSink]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.Tag]]


# CreateMediaConcatenationPipelineResponse

### MediaConcatenationPipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaConcatenationPipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMediaInsightsPipelineConfigurationRequest

### MediaInsightsPipelineConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Elements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationElementUnion]
- **Required**: Yes

### RealTimeAlertConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RealTimeAlertConfigurationUnion]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.Tag]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateMediaInsightsPipelineConfigurationResponse

### MediaInsightsPipelineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMediaInsightsPipelineRequest

### MediaInsightsPipelineConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### KinesisVideoStreamSourceRuntimeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamSourceRuntimeConfigurationUnion]

### MediaInsightsRuntimeMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### KinesisVideoStreamRecordingSourceRuntimeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamRecordingSourceRuntimeConfigurationUnion]

### S3RecordingSinkRuntimeConfiguration
- **Type**: <class 'NoneType'>

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.Tag]]

### ClientRequestToken
- **Type**: typing.Optional[str]


# CreateMediaInsightsPipelineResponse

### MediaInsightsPipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMediaLiveConnectorPipelineRequest

### Sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LiveConnectorSourceConfigurationUnion]
- **Required**: Yes

### Sinks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LiveConnectorSinkConfiguration]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.Tag]]


# CreateMediaLiveConnectorPipelineResponse

### MediaLiveConnectorPipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaLiveConnectorPipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMediaPipelineKinesisVideoStreamPoolRequest

### StreamConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamConfiguration'>
- **Required**: Yes

### PoolName
- **Type**: <class 'str'>
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.Tag]]


# CreateMediaPipelineKinesisVideoStreamPoolResponse

### KinesisVideoStreamPoolConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamPoolConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# CreateMediaStreamPipelineRequest

### Sources
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaStreamSource]
- **Required**: Yes

### Sinks
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaStreamSink]
- **Required**: Yes

### ClientRequestToken
- **Type**: typing.Optional[str]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.Tag]]


# CreateMediaStreamPipelineResponse

### MediaStreamPipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaStreamPipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# DataChannelConcatenationConfiguration

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# DeleteMediaCapturePipelineRequest

### MediaPipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMediaInsightsPipelineConfigurationRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMediaPipelineKinesisVideoStreamPoolRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMediaPipelineRequest

### MediaPipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# EmptyResponseMetadata

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# FragmentSelector

### FragmentSelectorType
- **Type**: typing.Literal['ProducerTimestamp', 'ServerTimestamp']
- **Required**: Yes

### TimestampRange
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TimestampRange'>
- **Required**: Yes


# FragmentSelectorOutput

### FragmentSelectorType
- **Type**: typing.Literal['ProducerTimestamp', 'ServerTimestamp']
- **Required**: Yes

### TimestampRange
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TimestampRangeOutput'>
- **Required**: Yes


# GetMediaCapturePipelineRequest

### MediaPipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaCapturePipelineResponse

### MediaCapturePipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaCapturePipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# GetMediaInsightsPipelineConfigurationRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaInsightsPipelineConfigurationResponse

### MediaInsightsPipelineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# GetMediaPipelineKinesisVideoStreamPoolRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaPipelineKinesisVideoStreamPoolResponse

### KinesisVideoStreamPoolConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamPoolConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# GetMediaPipelineRequest

### MediaPipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# GetMediaPipelineResponse

### MediaPipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaPipeline'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# GetSpeakerSearchTaskRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetSpeakerSearchTaskResponse

### SpeakerSearchTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SpeakerSearchTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# GetVoiceToneAnalysisTaskRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceToneAnalysisTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# GetVoiceToneAnalysisTaskResponse

### VoiceToneAnalysisTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VoiceToneAnalysisTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# GridViewConfiguration

### ContentShareLayout
- **Type**: typing.Literal['ActiveSpeakerOnly', 'Horizontal', 'PresenterOnly', 'Vertical']
- **Required**: Yes

### PresenterOnlyConfiguration
- **Type**: <class 'NoneType'>

### ActiveSpeakerOnlyConfiguration
- **Type**: <class 'NoneType'>

### HorizontalLayoutConfiguration
- **Type**: <class 'NoneType'>

### VerticalLayoutConfiguration
- **Type**: <class 'NoneType'>

### VideoAttribute
- **Type**: <class 'NoneType'>

### CanvasOrientation
- **Type**: typing.Optional[typing.Literal['Landscape', 'Portrait']]


# HorizontalLayoutConfiguration

### TileOrder
- **Type**: typing.Optional[typing.Literal['JoinSequence', 'SpeakerSequence']]

### TilePosition
- **Type**: typing.Optional[typing.Literal['Bottom', 'Top']]

### TileCount
- **Type**: typing.Optional[int]

### TileAspectRatio
- **Type**: typing.Optional[str]


# IssueDetectionConfiguration

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes


# KeywordMatchConfiguration

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### Keywords
- **Type**: typing.Sequence[str]
- **Required**: Yes

### Negate
- **Type**: typing.Optional[bool]


# KeywordMatchConfigurationOutput

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### Keywords
- **Type**: typing.List[str]
- **Required**: Yes

### Negate
- **Type**: typing.Optional[bool]


# KinesisDataStreamSinkConfiguration

### InsightsTarget
- **Type**: typing.Optional[str]


# KinesisVideoStreamConfiguration

### Region
- **Type**: <class 'str'>
- **Required**: Yes

### DataRetentionInHours
- **Type**: typing.Optional[int]


# KinesisVideoStreamConfigurationUpdate

### DataRetentionInHours
- **Type**: typing.Optional[int]


# KinesisVideoStreamPoolConfiguration

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamConfiguration]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# KinesisVideoStreamPoolSummary

### PoolName
- **Type**: typing.Optional[str]

### PoolId
- **Type**: typing.Optional[str]

### PoolArn
- **Type**: typing.Optional[str]


# KinesisVideoStreamRecordingSourceRuntimeConfiguration

### Streams
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RecordingStreamConfiguration]
- **Required**: Yes

### FragmentSelector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.FragmentSelector'>
- **Required**: Yes


# KinesisVideoStreamRecordingSourceRuntimeConfigurationOutput

### Streams
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RecordingStreamConfiguration]
- **Required**: Yes

### FragmentSelector
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.FragmentSelectorOutput'>
- **Required**: Yes


# KinesisVideoStreamRecordingSourceRuntimeConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KinesisVideoStreamSourceRuntimeConfiguration

### Streams
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.StreamConfiguration]
- **Required**: Yes

### MediaEncoding
- **Type**: typing.Literal['pcm']
- **Required**: Yes

### MediaSampleRate
- **Type**: <class 'int'>
- **Required**: Yes


# KinesisVideoStreamSourceRuntimeConfigurationOutput

### Streams
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.StreamConfigurationOutput]
- **Required**: Yes

### MediaEncoding
- **Type**: typing.Literal['pcm']
- **Required**: Yes

### MediaSampleRate
- **Type**: <class 'int'>
- **Required**: Yes


# KinesisVideoStreamSourceRuntimeConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# KinesisVideoStreamSourceTaskConfiguration

### StreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChannelId
- **Type**: <class 'int'>
- **Required**: Yes

### FragmentNumber
- **Type**: typing.Optional[str]


# LambdaFunctionSinkConfiguration

### InsightsTarget
- **Type**: typing.Optional[str]


# ListMediaCapturePipelinesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMediaCapturePipelinesResponse

### MediaCapturePipelines
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaCapturePipelineSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMediaInsightsPipelineConfigurationsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMediaInsightsPipelineConfigurationsResponse

### MediaInsightsPipelineConfigurations
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMediaPipelineKinesisVideoStreamPoolsRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMediaPipelineKinesisVideoStreamPoolsResponse

### KinesisVideoStreamPools
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamPoolSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListMediaPipelinesRequest

### NextToken
- **Type**: typing.Optional[str]

### MaxResults
- **Type**: typing.Optional[int]


# ListMediaPipelinesResponse

### MediaPipelines
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaPipelineSummary]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes

### NextToken
- **Type**: typing.Optional[str]


# ListTagsForResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes


# ListTagsForResourceResponse

### Tags
- **Type**: typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.Tag]
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# LiveConnectorRTMPConfiguration

### Url
- **Type**: <class 'str'>
- **Required**: Yes

### AudioChannels
- **Type**: typing.Optional[typing.Literal['Mono', 'Stereo']]

### AudioSampleRate
- **Type**: typing.Optional[str]


# LiveConnectorSinkConfiguration

### SinkType
- **Type**: typing.Literal['RTMP']
- **Required**: Yes

### RTMPConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LiveConnectorRTMPConfiguration'>
- **Required**: Yes


# LiveConnectorSourceConfiguration

### SourceType
- **Type**: typing.Literal['ChimeSdkMeeting']
- **Required**: Yes

### ChimeSdkMeetingLiveConnectorConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChimeSdkMeetingLiveConnectorConfigurationUnion'>
- **Required**: Yes


# LiveConnectorSourceConfigurationOutput

### SourceType
- **Type**: typing.Literal['ChimeSdkMeeting']
- **Required**: Yes

### ChimeSdkMeetingLiveConnectorConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChimeSdkMeetingLiveConnectorConfigurationOutput'>
- **Required**: Yes


# LiveConnectorSourceConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MediaCapturePipeline

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChimeSdkMeetingConfigurationOutput]

### SseAwsKeyManagementParams
- **Type**: <class 'NoneType'>

### SinkIamRoleArn
- **Type**: typing.Optional[str]


# MediaCapturePipelineSourceConfiguration

### MediaPipelineArn
- **Type**: <class 'str'>
- **Required**: Yes

### ChimeSdkMeetingConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChimeSdkMeetingConcatenationConfiguration'>
- **Required**: Yes


# MediaCapturePipelineSummary

### MediaPipelineId
- **Type**: typing.Optional[str]

### MediaPipelineArn
- **Type**: typing.Optional[str]


# MediaConcatenationPipeline

### MediaPipelineId
- **Type**: typing.Optional[str]

### MediaPipelineArn
- **Type**: typing.Optional[str]

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ConcatenationSource]]

### Sinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ConcatenationSink]]

### Status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Initializing', 'NotStarted', 'Paused', 'Stopped', 'Stopping']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# MediaInsightsPipeline

### MediaPipelineId
- **Type**: typing.Optional[str]

### MediaPipelineArn
- **Type**: typing.Optional[str]

### MediaInsightsPipelineConfigurationArn
- **Type**: typing.Optional[str]

### Status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Initializing', 'NotStarted', 'Paused', 'Stopped', 'Stopping']]

### KinesisVideoStreamSourceRuntimeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamSourceRuntimeConfigurationOutput]

### MediaInsightsRuntimeMetadata
- **Type**: typing.Optional[typing.Dict[str, str]]

### KinesisVideoStreamRecordingSourceRuntimeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamRecordingSourceRuntimeConfigurationOutput]

### S3RecordingSinkRuntimeConfiguration
- **Type**: <class 'NoneType'>

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### ElementStatuses
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineElementStatus]]


# MediaInsightsPipelineConfiguration

### MediaInsightsPipelineConfigurationName
- **Type**: typing.Optional[str]

### MediaInsightsPipelineConfigurationArn
- **Type**: typing.Optional[str]

### ResourceAccessRoleArn
- **Type**: typing.Optional[str]

### RealTimeAlertConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RealTimeAlertConfigurationOutput]

### Elements
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationElementOutput]]

### MediaInsightsPipelineConfigurationId
- **Type**: typing.Optional[str]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# MediaInsightsPipelineConfigurationElementOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MediaInsightsPipelineConfigurationElementUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MediaInsightsPipelineConfigurationSummary

### MediaInsightsPipelineConfigurationName
- **Type**: typing.Optional[str]

### MediaInsightsPipelineConfigurationId
- **Type**: typing.Optional[str]

### MediaInsightsPipelineConfigurationArn
- **Type**: typing.Optional[str]


# MediaInsightsPipelineElementStatus

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# MediaLiveConnectorPipeline

### Sources
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LiveConnectorSourceConfigurationOutput]]

### Sinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LiveConnectorSinkConfiguration]]

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


# MediaPipeline

### MediaCapturePipeline
- **Type**: <class 'NoneType'>

### MediaLiveConnectorPipeline
- **Type**: <class 'NoneType'>

### MediaConcatenationPipeline
- **Type**: <class 'NoneType'>

### MediaInsightsPipeline
- **Type**: <class 'NoneType'>

### MediaStreamPipeline
- **Type**: <class 'NoneType'>


# MediaPipelineSummary

### MediaPipelineId
- **Type**: typing.Optional[str]

### MediaPipelineArn
- **Type**: typing.Optional[str]


# MediaStreamPipeline

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
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaStreamSource]]

### Sinks
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaStreamSink]]


# MediaStreamSink

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


# MediaStreamSource

### SourceType
- **Type**: typing.Literal['ChimeSdkMeeting']
- **Required**: Yes

### SourceArn
- **Type**: <class 'str'>
- **Required**: Yes


# MeetingEventsConcatenationConfiguration

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# PostCallAnalyticsSettings

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


# PresenterOnlyConfiguration

### PresenterPosition
- **Type**: typing.Optional[typing.Literal['BottomLeft', 'BottomRight', 'TopLeft', 'TopRight']]


# RealTimeAlertConfiguration

### Disabled
- **Type**: typing.Optional[bool]

### Rules
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RealTimeAlertRule]]


# RealTimeAlertConfigurationOutput

### Disabled
- **Type**: typing.Optional[bool]

### Rules
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RealTimeAlertRuleOutput]]


# RealTimeAlertConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RealTimeAlertRule

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RealTimeAlertRuleOutput

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# RecordingStreamConfiguration

### StreamArn
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


# S3BucketSinkConfiguration

### Destination
- **Type**: <class 'str'>
- **Required**: Yes


# S3RecordingSinkConfiguration

### Destination
- **Type**: typing.Optional[str]

### RecordingFileFormat
- **Type**: typing.Optional[typing.Literal['Opus', 'Wav']]


# S3RecordingSinkRuntimeConfiguration

### Destination
- **Type**: <class 'str'>
- **Required**: Yes

### RecordingFileFormat
- **Type**: typing.Literal['Opus', 'Wav']
- **Required**: Yes


# SelectedVideoStreams

### AttendeeIds
- **Type**: typing.Optional[typing.Sequence[str]]

### ExternalUserIds
- **Type**: typing.Optional[typing.Sequence[str]]


# SelectedVideoStreamsOutput

### AttendeeIds
- **Type**: typing.Optional[typing.List[str]]

### ExternalUserIds
- **Type**: typing.Optional[typing.List[str]]


# SelectedVideoStreamsUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SentimentConfiguration

### RuleName
- **Type**: <class 'str'>
- **Required**: Yes

### SentimentType
- **Type**: typing.Literal['NEGATIVE']
- **Required**: Yes

### TimePeriod
- **Type**: <class 'int'>
- **Required**: Yes


# SnsTopicSinkConfiguration

### InsightsTarget
- **Type**: typing.Optional[str]


# SourceConfiguration

### SelectedVideoStreams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SelectedVideoStreamsUnion]


# SourceConfigurationOutput

### SelectedVideoStreams
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SelectedVideoStreamsOutput]


# SourceConfigurationUnion

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# SpeakerSearchTask

### SpeakerSearchTaskId
- **Type**: typing.Optional[str]

### SpeakerSearchTaskStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Initializing', 'NotStarted', 'Stopped', 'Stopping']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


# SqsQueueSinkConfiguration

### InsightsTarget
- **Type**: typing.Optional[str]


# SseAwsKeyManagementParams

### AwsKmsKeyId
- **Type**: <class 'str'>
- **Required**: Yes

### AwsKmsEncryptionContext
- **Type**: typing.Optional[str]


# StartSpeakerSearchTaskRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceProfileDomainArn
- **Type**: <class 'str'>
- **Required**: Yes

### KinesisVideoStreamSourceTaskConfiguration
- **Type**: <class 'NoneType'>

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartSpeakerSearchTaskResponse

### SpeakerSearchTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SpeakerSearchTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# StartVoiceToneAnalysisTaskRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### LanguageCode
- **Type**: typing.Literal['en-US']
- **Required**: Yes

### KinesisVideoStreamSourceTaskConfiguration
- **Type**: <class 'NoneType'>

### ClientRequestToken
- **Type**: typing.Optional[str]


# StartVoiceToneAnalysisTaskResponse

### VoiceToneAnalysisTask
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VoiceToneAnalysisTask'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# StopSpeakerSearchTaskRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# StopVoiceToneAnalysisTaskRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### VoiceToneAnalysisTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# StreamChannelDefinition

### NumberOfChannels
- **Type**: <class 'int'>
- **Required**: Yes

### ChannelDefinitions
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChannelDefinition]]


# StreamChannelDefinitionOutput

### NumberOfChannels
- **Type**: <class 'int'>
- **Required**: Yes

### ChannelDefinitions
- **Type**: typing.Optional[typing.List[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChannelDefinition]]


# StreamConfiguration

### StreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### StreamChannelDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.StreamChannelDefinition'>
- **Required**: Yes

### FragmentNumber
- **Type**: typing.Optional[str]


# StreamConfigurationOutput

### StreamArn
- **Type**: <class 'str'>
- **Required**: Yes

### StreamChannelDefinition
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.StreamChannelDefinitionOutput'>
- **Required**: Yes

### FragmentNumber
- **Type**: typing.Optional[str]


# Tag

### Key
- **Type**: <class 'str'>
- **Required**: Yes

### Value
- **Type**: <class 'str'>
- **Required**: Yes


# TagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### Tags
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.Tag]
- **Required**: Yes


# Timestamp

Oops! This Pydantic model is currently empty. Stay tuned!

<img src="/aws_resource_validator/images/oops_loki.png" width="500" height="400" title="Oops Loki">

# TimestampRange

### StartTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.Timestamp'>
- **Required**: Yes

### EndTimestamp
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.Timestamp'>
- **Required**: Yes


# TimestampRangeOutput

### StartTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes

### EndTimestamp
- **Type**: <class 'datetime.datetime'>
- **Required**: Yes


# TranscriptionMessagesConcatenationConfiguration

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# UntagResourceRequest

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateMediaInsightsPipelineConfigurationRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Elements
- **Type**: typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationElementUnion]
- **Required**: Yes

### RealTimeAlertConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RealTimeAlertConfigurationUnion]


# UpdateMediaInsightsPipelineConfigurationResponse

### MediaInsightsPipelineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# UpdateMediaInsightsPipelineStatusRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Literal['Pause', 'Resume']
- **Required**: Yes


# UpdateMediaPipelineKinesisVideoStreamPoolRequest

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### StreamConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamConfigurationUpdate]


# UpdateMediaPipelineKinesisVideoStreamPoolResponse

### KinesisVideoStreamPoolConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamPoolConfiguration'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadata'>
- **Required**: Yes


# VerticalLayoutConfiguration

### TileOrder
- **Type**: typing.Optional[typing.Literal['JoinSequence', 'SpeakerSequence']]

### TilePosition
- **Type**: typing.Optional[typing.Literal['Left', 'Right']]

### TileCount
- **Type**: typing.Optional[int]

### TileAspectRatio
- **Type**: typing.Optional[str]


# VideoArtifactsConfiguration

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes

### MuxType
- **Type**: typing.Optional[typing.Literal['VideoOnly']]


# VideoAttribute

### CornerRadius
- **Type**: typing.Optional[int]

### BorderColor
- **Type**: typing.Optional[typing.Literal['Black', 'Blue', 'Green', 'Red', 'White', 'Yellow']]

### HighlightColor
- **Type**: typing.Optional[typing.Literal['Black', 'Blue', 'Green', 'Red', 'White', 'Yellow']]

### BorderThickness
- **Type**: typing.Optional[int]


# VideoConcatenationConfiguration

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# VoiceAnalyticsProcessorConfiguration

### SpeakerSearchStatus
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]

### VoiceToneAnalysisStatus
- **Type**: typing.Optional[typing.Literal['Disabled', 'Enabled']]


# VoiceEnhancementSinkConfiguration

### Disabled
- **Type**: typing.Optional[bool]


# VoiceToneAnalysisTask

### VoiceToneAnalysisTaskId
- **Type**: typing.Optional[str]

### VoiceToneAnalysisTaskStatus
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Initializing', 'NotStarted', 'Stopped', 'Stopping']]

### CreatedTimestamp
- **Type**: typing.Optional[datetime.datetime]

### UpdatedTimestamp
- **Type**: typing.Optional[datetime.datetime]


