# chime_sdk_media_pipelines_classes

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SourceConfigurationTypeDef]


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

### Type
- **Type**: typing.Literal['S3Bucket']
- **Required**: Yes

### S3BucketSinkConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.S3BucketSinkConfigurationTypeDef'>
- **Required**: Yes


# ConcatenationSourceTypeDef

### Type
- **Type**: typing.Literal['MediaCapturePipeline']
- **Required**: Yes

### MediaCapturePipelineSourceConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaCapturePipelineSourceConfigurationTypeDef'>
- **Required**: Yes


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


# CreateMediaCapturePipelineRequestRequestTypeDef

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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChimeSdkMeetingConfigurationTypeDef]

### Tags
- **Type**: typing.Optional[typing.Sequence[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.TagTypeDef]]


# CreateMediaCapturePipelineResponseTypeDef

### MediaCapturePipeline
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaCapturePipelineTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# CreateMediaConcatenationPipelineRequestRequestTypeDef

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


# CreateMediaInsightsPipelineConfigurationRequestRequestTypeDef

### MediaInsightsPipelineConfigurationName
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Elements
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationElementTypeDef, aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationElementOutputTypeDef]]
- **Required**: Yes

### RealTimeAlertConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RealTimeAlertConfigurationTypeDef]

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


# CreateMediaInsightsPipelineRequestRequestTypeDef

### MediaInsightsPipelineConfigurationArn
- **Type**: <class 'str'>
- **Required**: Yes

### KinesisVideoStreamSourceRuntimeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamSourceRuntimeConfigurationTypeDef]

### MediaInsightsRuntimeMetadata
- **Type**: typing.Optional[typing.Mapping[str, str]]

### KinesisVideoStreamRecordingSourceRuntimeConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef]

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


# CreateMediaLiveConnectorPipelineRequestRequestTypeDef

### Sources
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LiveConnectorSourceConfigurationTypeDef, aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LiveConnectorSourceConfigurationOutputTypeDef]]
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


# CreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef

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


# CreateMediaStreamPipelineRequestRequestTypeDef

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


# DeleteMediaCapturePipelineRequestRequestTypeDef

### MediaPipelineId
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes


# DeleteMediaPipelineRequestRequestTypeDef

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


# GetMediaCapturePipelineRequestRequestTypeDef

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


# GetMediaInsightsPipelineConfigurationRequestRequestTypeDef

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


# GetMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef

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


# GetMediaPipelineRequestRequestTypeDef

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


# GetSpeakerSearchTaskRequestRequestTypeDef

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


# GetVoiceToneAnalysisTaskRequestRequestTypeDef

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


# ListMediaCapturePipelinesRequestRequestTypeDef

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


# ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef

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


# ListMediaPipelineKinesisVideoStreamPoolsRequestRequestTypeDef

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


# ListMediaPipelinesRequestRequestTypeDef

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


# ListTagsForResourceRequestRequestTypeDef

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
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ChimeSdkMeetingLiveConnectorConfigurationTypeDef'>
- **Required**: Yes


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

### Type
- **Type**: typing.Literal['AmazonTranscribeCallAnalyticsProcessor', 'AmazonTranscribeProcessor', 'KinesisDataStreamSink', 'LambdaFunctionSink', 'S3RecordingSink', 'SnsTopicSink', 'SqsQueueSink', 'VoiceAnalyticsProcessor', 'VoiceEnhancementSink']
- **Required**: Yes

### AmazonTranscribeCallAnalyticsProcessorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef]

### AmazonTranscribeProcessorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.AmazonTranscribeProcessorConfigurationTypeDef]

### KinesisDataStreamSinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisDataStreamSinkConfigurationTypeDef]

### S3RecordingSinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.S3RecordingSinkConfigurationTypeDef]

### VoiceAnalyticsProcessorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VoiceAnalyticsProcessorConfigurationTypeDef]

### LambdaFunctionSinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LambdaFunctionSinkConfigurationTypeDef]

### SqsQueueSinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SqsQueueSinkConfigurationTypeDef]

### SnsTopicSinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SnsTopicSinkConfigurationTypeDef]

### VoiceEnhancementSinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VoiceEnhancementSinkConfigurationTypeDef]


# MediaInsightsPipelineConfigurationElementTypeDef

### Type
- **Type**: typing.Literal['AmazonTranscribeCallAnalyticsProcessor', 'AmazonTranscribeProcessor', 'KinesisDataStreamSink', 'LambdaFunctionSink', 'S3RecordingSink', 'SnsTopicSink', 'SqsQueueSink', 'VoiceAnalyticsProcessor', 'VoiceEnhancementSink']
- **Required**: Yes

### AmazonTranscribeCallAnalyticsProcessorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef]

### AmazonTranscribeProcessorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.AmazonTranscribeProcessorConfigurationTypeDef]

### KinesisDataStreamSinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KinesisDataStreamSinkConfigurationTypeDef]

### S3RecordingSinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.S3RecordingSinkConfigurationTypeDef]

### VoiceAnalyticsProcessorConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VoiceAnalyticsProcessorConfigurationTypeDef]

### LambdaFunctionSinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.LambdaFunctionSinkConfigurationTypeDef]

### SqsQueueSinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SqsQueueSinkConfigurationTypeDef]

### SnsTopicSinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SnsTopicSinkConfigurationTypeDef]

### VoiceEnhancementSinkConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.VoiceEnhancementSinkConfigurationTypeDef]


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

### Type
- **Type**: typing.Optional[typing.Literal['AmazonTranscribeCallAnalyticsProcessor', 'AmazonTranscribeProcessor', 'KinesisDataStreamSink', 'LambdaFunctionSink', 'S3RecordingSink', 'SnsTopicSink', 'SqsQueueSink', 'VoiceAnalyticsProcessor', 'VoiceEnhancementSink']]

### Status
- **Type**: typing.Optional[typing.Literal['Failed', 'InProgress', 'Initializing', 'NotStarted', 'NotSupported', 'Paused', 'Stopped', 'Stopping']]


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


# RealTimeAlertRuleOutputTypeDef

### Type
- **Type**: typing.Literal['IssueDetection', 'KeywordMatch', 'Sentiment']
- **Required**: Yes

### KeywordMatchConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KeywordMatchConfigurationOutputTypeDef]

### SentimentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SentimentConfigurationTypeDef]

### IssueDetectionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.IssueDetectionConfigurationTypeDef]


# RealTimeAlertRuleTypeDef

### Type
- **Type**: typing.Literal['IssueDetection', 'KeywordMatch', 'Sentiment']
- **Required**: Yes

### KeywordMatchConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.KeywordMatchConfigurationTypeDef]

### SentimentConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SentimentConfigurationTypeDef]

### IssueDetectionConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.IssueDetectionConfigurationTypeDef]


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
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.SelectedVideoStreamsTypeDef]


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


# StartSpeakerSearchTaskRequestRequestTypeDef

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


# StartVoiceToneAnalysisTaskRequestRequestTypeDef

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


# StopSpeakerSearchTaskRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### SpeakerSearchTaskId
- **Type**: <class 'str'>
- **Required**: Yes


# StopVoiceToneAnalysisTaskRequestRequestTypeDef

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


# TagResourceRequestRequestTypeDef

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
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes

### EndTimestamp
- **Type**: typing.Union[datetime.datetime, str]
- **Required**: Yes


# TranscriptionMessagesConcatenationConfigurationTypeDef

### State
- **Type**: typing.Literal['Disabled', 'Enabled']
- **Required**: Yes


# UntagResourceRequestRequestTypeDef

### ResourceARN
- **Type**: <class 'str'>
- **Required**: Yes

### TagKeys
- **Type**: typing.Sequence[str]
- **Required**: Yes


# UpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### ResourceAccessRoleArn
- **Type**: <class 'str'>
- **Required**: Yes

### Elements
- **Type**: typing.Sequence[typing.Union[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationElementTypeDef, aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationElementOutputTypeDef]]
- **Required**: Yes

### RealTimeAlertConfiguration
- **Type**: typing.Optional[aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.RealTimeAlertConfigurationTypeDef]


# UpdateMediaInsightsPipelineConfigurationResponseTypeDef

### MediaInsightsPipelineConfiguration
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.MediaInsightsPipelineConfigurationTypeDef'>
- **Required**: Yes

### ResponseMetadata
- **Type**: <class 'aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_classes.ResponseMetadataTypeDef'>
- **Required**: Yes


# UpdateMediaInsightsPipelineStatusRequestRequestTypeDef

### Identifier
- **Type**: <class 'str'>
- **Required**: Yes

### UpdateStatus
- **Type**: typing.Literal['Pause', 'Resume']
- **Required**: Yes


# UpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef

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


