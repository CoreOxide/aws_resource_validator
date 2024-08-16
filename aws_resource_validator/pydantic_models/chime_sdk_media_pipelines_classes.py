from datetime import datetime
from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from typing import Any
from typing import Dict
from typing import IO
from typing import List
from typing import Literal
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
from aws_resource_validator.pydantic_models.chime_sdk_media_pipelines_constants import *

class ActiveSpeakerOnlyConfigurationTypeDef(BaseValidatorModel):
    ActiveSpeakerPosition: Optional[ActiveSpeakerPositionType] = None

class PostCallAnalyticsSettingsTypeDef(BaseValidatorModel):
    OutputLocation: str
    DataAccessRoleArn: str
    ContentRedactionOutput: Optional[ContentRedactionOutputType] = None
    OutputEncryptionKMSKeyId: Optional[str] = None

class AmazonTranscribeProcessorConfigurationTypeDef(BaseValidatorModel):
    LanguageCode: Optional[CallAnalyticsLanguageCodeType] = None
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None
    ShowSpeakerLabel: Optional[bool] = None
    EnablePartialResultsStabilization: Optional[bool] = None
    PartialResultsStability: Optional[PartialResultsStabilityType] = None
    ContentIdentificationType: Optional[Literal["PII"]] = None
    ContentRedactionType: Optional[Literal["PII"]] = None
    PiiEntityTypes: Optional[str] = None
    LanguageModelName: Optional[str] = None
    FilterPartialResults: Optional[bool] = None
    IdentifyLanguage: Optional[bool] = None
    IdentifyMultipleLanguages: Optional[bool] = None
    LanguageOptions: Optional[str] = None
    PreferredLanguage: Optional[CallAnalyticsLanguageCodeType] = None
    VocabularyNames: Optional[str] = None
    VocabularyFilterNames: Optional[str] = None

class AudioConcatenationConfigurationTypeDef(BaseValidatorModel):
    State: Literal["Enabled"]

class CompositedVideoConcatenationConfigurationTypeDef(BaseValidatorModel):
    State: ArtifactsConcatenationStateType

class ContentConcatenationConfigurationTypeDef(BaseValidatorModel):
    State: ArtifactsConcatenationStateType

class DataChannelConcatenationConfigurationTypeDef(BaseValidatorModel):
    State: ArtifactsConcatenationStateType

class MeetingEventsConcatenationConfigurationTypeDef(BaseValidatorModel):
    State: ArtifactsConcatenationStateType

class TranscriptionMessagesConcatenationConfigurationTypeDef(BaseValidatorModel):
    State: ArtifactsConcatenationStateType

class VideoConcatenationConfigurationTypeDef(BaseValidatorModel):
    State: ArtifactsConcatenationStateType

class AudioArtifactsConfigurationTypeDef(BaseValidatorModel):
    MuxType: AudioMuxTypeType

class ContentArtifactsConfigurationTypeDef(BaseValidatorModel):
    State: ArtifactsStateType
    MuxType: Optional[Literal["ContentOnly"]] = None

class VideoArtifactsConfigurationTypeDef(BaseValidatorModel):
    State: ArtifactsStateType
    MuxType: Optional[Literal["VideoOnly"]] = None

class ChannelDefinitionTypeDef(BaseValidatorModel):
    ChannelId: int
    ParticipantRole: Optional[ParticipantRoleType] = None

class S3BucketSinkConfigurationTypeDef(BaseValidatorModel):
    Destination: str

class TagTypeDef(BaseValidatorModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class S3RecordingSinkRuntimeConfigurationTypeDef(BaseValidatorModel):
    Destination: str
    RecordingFileFormat: RecordingFileFormatType

class KinesisVideoStreamConfigurationTypeDef(BaseValidatorModel):
    Region: str
    DataRetentionInHours: Optional[int] = None

class MediaStreamSinkTypeDef(BaseValidatorModel):
    SinkArn: str
    SinkType: Literal["KinesisVideoStreamPool"]
    ReservedStreamCapacity: int
    MediaStreamType: MediaStreamTypeType

class MediaStreamSourceTypeDef(BaseValidatorModel):
    SourceType: Literal["ChimeSdkMeeting"]
    SourceArn: str

class DeleteMediaCapturePipelineRequestRequestTypeDef(BaseValidatorModel):
    MediaPipelineId: str

class DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class DeleteMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class DeleteMediaPipelineRequestRequestTypeDef(BaseValidatorModel):
    MediaPipelineId: str

class TimestampRangeOutputTypeDef(BaseValidatorModel):
    StartTimestamp: datetime
    EndTimestamp: datetime

class GetMediaCapturePipelineRequestRequestTypeDef(BaseValidatorModel):
    MediaPipelineId: str

class GetMediaInsightsPipelineConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class GetMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str

class GetMediaPipelineRequestRequestTypeDef(BaseValidatorModel):
    MediaPipelineId: str

class GetSpeakerSearchTaskRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    SpeakerSearchTaskId: str

class SpeakerSearchTaskTypeDef(BaseValidatorModel):
    SpeakerSearchTaskId: Optional[str] = None
    SpeakerSearchTaskStatus: Optional[MediaPipelineTaskStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class GetVoiceToneAnalysisTaskRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    VoiceToneAnalysisTaskId: str

class VoiceToneAnalysisTaskTypeDef(BaseValidatorModel):
    VoiceToneAnalysisTaskId: Optional[str] = None
    VoiceToneAnalysisTaskStatus: Optional[MediaPipelineTaskStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class HorizontalLayoutConfigurationTypeDef(BaseValidatorModel):
    TileOrder: Optional[TileOrderType] = None
    TilePosition: Optional[HorizontalTilePositionType] = None
    TileCount: Optional[int] = None
    TileAspectRatio: Optional[str] = None

class PresenterOnlyConfigurationTypeDef(BaseValidatorModel):
    PresenterPosition: Optional[PresenterPositionType] = None

class VerticalLayoutConfigurationTypeDef(BaseValidatorModel):
    TileOrder: Optional[TileOrderType] = None
    TilePosition: Optional[VerticalTilePositionType] = None
    TileCount: Optional[int] = None
    TileAspectRatio: Optional[str] = None

class VideoAttributeTypeDef(BaseValidatorModel):
    CornerRadius: Optional[int] = None
    BorderColor: Optional[BorderColorType] = None
    HighlightColor: Optional[HighlightColorType] = None
    BorderThickness: Optional[int] = None

class IssueDetectionConfigurationTypeDef(BaseValidatorModel):
    RuleName: str

class KeywordMatchConfigurationOutputTypeDef(BaseValidatorModel):
    RuleName: str
    Keywords: List[str]
    Negate: Optional[bool] = None

class KeywordMatchConfigurationTypeDef(BaseValidatorModel):
    RuleName: str
    Keywords: Sequence[str]
    Negate: Optional[bool] = None

class KinesisDataStreamSinkConfigurationTypeDef(BaseValidatorModel):
    InsightsTarget: Optional[str] = None

class KinesisVideoStreamConfigurationUpdateTypeDef(BaseValidatorModel):
    DataRetentionInHours: Optional[int] = None

class KinesisVideoStreamPoolSummaryTypeDef(BaseValidatorModel):
    PoolName: Optional[str] = None
    PoolId: Optional[str] = None
    PoolArn: Optional[str] = None

class RecordingStreamConfigurationTypeDef(BaseValidatorModel):
    StreamArn: Optional[str] = None

class KinesisVideoStreamSourceTaskConfigurationTypeDef(BaseValidatorModel):
    StreamArn: str
    ChannelId: int
    FragmentNumber: Optional[str] = None

class LambdaFunctionSinkConfigurationTypeDef(BaseValidatorModel):
    InsightsTarget: Optional[str] = None

class ListMediaCapturePipelinesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MediaCapturePipelineSummaryTypeDef(BaseValidatorModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None

class ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MediaInsightsPipelineConfigurationSummaryTypeDef(BaseValidatorModel):
    MediaInsightsPipelineConfigurationName: Optional[str] = None
    MediaInsightsPipelineConfigurationId: Optional[str] = None
    MediaInsightsPipelineConfigurationArn: Optional[str] = None

class ListMediaPipelineKinesisVideoStreamPoolsRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMediaPipelinesRequestRequestTypeDef(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MediaPipelineSummaryTypeDef(BaseValidatorModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str

class LiveConnectorRTMPConfigurationTypeDef(BaseValidatorModel):
    Url: str
    AudioChannels: Optional[AudioChannelsOptionType] = None
    AudioSampleRate: Optional[str] = None

class S3RecordingSinkConfigurationTypeDef(BaseValidatorModel):
    Destination: Optional[str] = None
    RecordingFileFormat: Optional[RecordingFileFormatType] = None

class SnsTopicSinkConfigurationTypeDef(BaseValidatorModel):
    InsightsTarget: Optional[str] = None

class SqsQueueSinkConfigurationTypeDef(BaseValidatorModel):
    InsightsTarget: Optional[str] = None

class VoiceAnalyticsProcessorConfigurationTypeDef(BaseValidatorModel):
    SpeakerSearchStatus: Optional[VoiceAnalyticsConfigurationStatusType] = None
    VoiceToneAnalysisStatus: Optional[VoiceAnalyticsConfigurationStatusType] = None

class VoiceEnhancementSinkConfigurationTypeDef(BaseValidatorModel):
    Disabled: Optional[bool] = None

class MediaInsightsPipelineElementStatusTypeDef(BaseValidatorModel):
    Type: Optional[MediaInsightsPipelineConfigurationElementTypeType] = None
    Status: Optional[MediaPipelineElementStatusType] = None

class SentimentConfigurationTypeDef(BaseValidatorModel):
    RuleName: str
    SentimentType: Literal["NEGATIVE"]
    TimePeriod: int

class SelectedVideoStreamsOutputTypeDef(BaseValidatorModel):
    AttendeeIds: Optional[List[str]] = None
    ExternalUserIds: Optional[List[str]] = None

class SelectedVideoStreamsTypeDef(BaseValidatorModel):
    AttendeeIds: Optional[Sequence[str]] = None
    ExternalUserIds: Optional[Sequence[str]] = None

class StopSpeakerSearchTaskRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    SpeakerSearchTaskId: str

class StopVoiceToneAnalysisTaskRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    VoiceToneAnalysisTaskId: str

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateMediaInsightsPipelineStatusRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    UpdateStatus: MediaPipelineStatusUpdateType

class AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef(BaseValidatorModel):
    LanguageCode: CallAnalyticsLanguageCodeType
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None
    LanguageModelName: Optional[str] = None
    EnablePartialResultsStabilization: Optional[bool] = None
    PartialResultsStability: Optional[PartialResultsStabilityType] = None
    ContentIdentificationType: Optional[Literal["PII"]] = None
    ContentRedactionType: Optional[Literal["PII"]] = None
    PiiEntityTypes: Optional[str] = None
    FilterPartialResults: Optional[bool] = None
    PostCallAnalyticsSettings: Optional[PostCallAnalyticsSettingsTypeDef] = None
    CallAnalyticsStreamCategories: Optional[List[str]] = None

class AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef(BaseValidatorModel):
    LanguageCode: CallAnalyticsLanguageCodeType
    VocabularyName: Optional[str] = None
    VocabularyFilterName: Optional[str] = None
    VocabularyFilterMethod: Optional[VocabularyFilterMethodType] = None
    LanguageModelName: Optional[str] = None
    EnablePartialResultsStabilization: Optional[bool] = None
    PartialResultsStability: Optional[PartialResultsStabilityType] = None
    ContentIdentificationType: Optional[Literal["PII"]] = None
    ContentRedactionType: Optional[Literal["PII"]] = None
    PiiEntityTypes: Optional[str] = None
    FilterPartialResults: Optional[bool] = None
    PostCallAnalyticsSettings: Optional[PostCallAnalyticsSettingsTypeDef] = None
    CallAnalyticsStreamCategories: Optional[Sequence[str]] = None

class ArtifactsConcatenationConfigurationTypeDef(BaseValidatorModel):
    Audio: AudioConcatenationConfigurationTypeDef
    Video: VideoConcatenationConfigurationTypeDef
    Content: ContentConcatenationConfigurationTypeDef
    DataChannel: DataChannelConcatenationConfigurationTypeDef
    TranscriptionMessages: TranscriptionMessagesConcatenationConfigurationTypeDef
    MeetingEvents: MeetingEventsConcatenationConfigurationTypeDef
    CompositedVideo: CompositedVideoConcatenationConfigurationTypeDef

class StreamChannelDefinitionOutputTypeDef(BaseValidatorModel):
    NumberOfChannels: int
    ChannelDefinitions: Optional[List[ChannelDefinitionTypeDef]] = None

class StreamChannelDefinitionTypeDef(BaseValidatorModel):
    NumberOfChannels: int
    ChannelDefinitions: Optional[Sequence[ChannelDefinitionTypeDef]] = None

class ConcatenationSinkTypeDef(BaseValidatorModel):
    Type: Literal["S3Bucket"]
    S3BucketSinkConfiguration: S3BucketSinkConfigurationTypeDef

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef(BaseValidatorModel):
    StreamConfiguration: KinesisVideoStreamConfigurationTypeDef
    PoolName: str
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class KinesisVideoStreamPoolConfigurationTypeDef(BaseValidatorModel):
    PoolArn: Optional[str] = None
    PoolName: Optional[str] = None
    PoolId: Optional[str] = None
    PoolStatus: Optional[KinesisVideoStreamPoolStatusType] = None
    PoolSize: Optional[int] = None
    StreamConfiguration: Optional[KinesisVideoStreamConfigurationTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class CreateMediaStreamPipelineRequestRequestTypeDef(BaseValidatorModel):
    Sources: Sequence[MediaStreamSourceTypeDef]
    Sinks: Sequence[MediaStreamSinkTypeDef]
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class MediaStreamPipelineTypeDef(BaseValidatorModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    Status: Optional[MediaPipelineStatusType] = None
    Sources: Optional[List[MediaStreamSourceTypeDef]] = None
    Sinks: Optional[List[MediaStreamSinkTypeDef]] = None

class FragmentSelectorOutputTypeDef(BaseValidatorModel):
    FragmentSelectorType: FragmentSelectorTypeType
    TimestampRange: TimestampRangeOutputTypeDef

class GetSpeakerSearchTaskResponseTypeDef(BaseValidatorModel):
    SpeakerSearchTask: SpeakerSearchTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSpeakerSearchTaskResponseTypeDef(BaseValidatorModel):
    SpeakerSearchTask: SpeakerSearchTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceToneAnalysisTaskResponseTypeDef(BaseValidatorModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartVoiceToneAnalysisTaskResponseTypeDef(BaseValidatorModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GridViewConfigurationTypeDef(BaseValidatorModel):
    ContentShareLayout: ContentShareLayoutOptionType
    PresenterOnlyConfiguration: Optional[PresenterOnlyConfigurationTypeDef] = None
    ActiveSpeakerOnlyConfiguration: Optional[ActiveSpeakerOnlyConfigurationTypeDef] = None
    HorizontalLayoutConfiguration: Optional[HorizontalLayoutConfigurationTypeDef] = None
    VerticalLayoutConfiguration: Optional[VerticalLayoutConfigurationTypeDef] = None
    VideoAttribute: Optional[VideoAttributeTypeDef] = None
    CanvasOrientation: Optional[CanvasOrientationType] = None

class UpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    StreamConfiguration: Optional[KinesisVideoStreamConfigurationUpdateTypeDef] = None

class ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef(BaseValidatorModel):
    KinesisVideoStreamPools: List[KinesisVideoStreamPoolSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartSpeakerSearchTaskRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    VoiceProfileDomainArn: str
    KinesisVideoStreamSourceTaskConfiguration: Optional[       KinesisVideoStreamSourceTaskConfigurationTypeDef     ] = None
    ClientRequestToken: Optional[str] = None

class StartVoiceToneAnalysisTaskRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    LanguageCode: Literal["en-US"]
    KinesisVideoStreamSourceTaskConfiguration: Optional[       KinesisVideoStreamSourceTaskConfigurationTypeDef     ] = None
    ClientRequestToken: Optional[str] = None

class ListMediaCapturePipelinesResponseTypeDef(BaseValidatorModel):
    MediaCapturePipelines: List[MediaCapturePipelineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMediaInsightsPipelineConfigurationsResponseTypeDef(BaseValidatorModel):
    MediaInsightsPipelineConfigurations: List[       MediaInsightsPipelineConfigurationSummaryTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMediaPipelinesResponseTypeDef(BaseValidatorModel):
    MediaPipelines: List[MediaPipelineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LiveConnectorSinkConfigurationTypeDef(BaseValidatorModel):
    SinkType: Literal["RTMP"]
    RTMPConfiguration: LiveConnectorRTMPConfigurationTypeDef

class RealTimeAlertRuleOutputTypeDef(BaseValidatorModel):
    Type: RealTimeAlertRuleTypeType
    KeywordMatchConfiguration: Optional[KeywordMatchConfigurationOutputTypeDef] = None
    SentimentConfiguration: Optional[SentimentConfigurationTypeDef] = None
    IssueDetectionConfiguration: Optional[IssueDetectionConfigurationTypeDef] = None

class RealTimeAlertRuleTypeDef(BaseValidatorModel):
    Type: RealTimeAlertRuleTypeType
    KeywordMatchConfiguration: Optional[KeywordMatchConfigurationTypeDef] = None
    SentimentConfiguration: Optional[SentimentConfigurationTypeDef] = None
    IssueDetectionConfiguration: Optional[IssueDetectionConfigurationTypeDef] = None

class SourceConfigurationOutputTypeDef(BaseValidatorModel):
    SelectedVideoStreams: Optional[SelectedVideoStreamsOutputTypeDef] = None

class SourceConfigurationTypeDef(BaseValidatorModel):
    SelectedVideoStreams: Optional[SelectedVideoStreamsTypeDef] = None

class TimestampRangeTypeDef(BaseValidatorModel):
    StartTimestamp: TimestampTypeDef
    EndTimestamp: TimestampTypeDef

class MediaInsightsPipelineConfigurationElementOutputTypeDef(BaseValidatorModel):
    Type: MediaInsightsPipelineConfigurationElementTypeType
    AmazonTranscribeCallAnalyticsProcessorConfiguration: Optional[       AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef     ] = None
    AmazonTranscribeProcessorConfiguration: Optional[       AmazonTranscribeProcessorConfigurationTypeDef     ] = None
    KinesisDataStreamSinkConfiguration: Optional[       KinesisDataStreamSinkConfigurationTypeDef     ] = None
    S3RecordingSinkConfiguration: Optional[S3RecordingSinkConfigurationTypeDef] = None
    VoiceAnalyticsProcessorConfiguration: Optional[       VoiceAnalyticsProcessorConfigurationTypeDef     ] = None
    LambdaFunctionSinkConfiguration: Optional[LambdaFunctionSinkConfigurationTypeDef] = None
    SqsQueueSinkConfiguration: Optional[SqsQueueSinkConfigurationTypeDef] = None
    SnsTopicSinkConfiguration: Optional[SnsTopicSinkConfigurationTypeDef] = None
    VoiceEnhancementSinkConfiguration: Optional[VoiceEnhancementSinkConfigurationTypeDef] = None

class MediaInsightsPipelineConfigurationElementTypeDef(BaseValidatorModel):
    Type: MediaInsightsPipelineConfigurationElementTypeType
    AmazonTranscribeCallAnalyticsProcessorConfiguration: Optional[       AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef     ] = None
    AmazonTranscribeProcessorConfiguration: Optional[       AmazonTranscribeProcessorConfigurationTypeDef     ] = None
    KinesisDataStreamSinkConfiguration: Optional[       KinesisDataStreamSinkConfigurationTypeDef     ] = None
    S3RecordingSinkConfiguration: Optional[S3RecordingSinkConfigurationTypeDef] = None
    VoiceAnalyticsProcessorConfiguration: Optional[       VoiceAnalyticsProcessorConfigurationTypeDef     ] = None
    LambdaFunctionSinkConfiguration: Optional[LambdaFunctionSinkConfigurationTypeDef] = None
    SqsQueueSinkConfiguration: Optional[SqsQueueSinkConfigurationTypeDef] = None
    SnsTopicSinkConfiguration: Optional[SnsTopicSinkConfigurationTypeDef] = None
    VoiceEnhancementSinkConfiguration: Optional[VoiceEnhancementSinkConfigurationTypeDef] = None

class ChimeSdkMeetingConcatenationConfigurationTypeDef(BaseValidatorModel):
    ArtifactsConfiguration: ArtifactsConcatenationConfigurationTypeDef

class StreamConfigurationOutputTypeDef(BaseValidatorModel):
    StreamArn: str
    StreamChannelDefinition: StreamChannelDefinitionOutputTypeDef
    FragmentNumber: Optional[str] = None

class StreamConfigurationTypeDef(BaseValidatorModel):
    StreamArn: str
    StreamChannelDefinition: StreamChannelDefinitionTypeDef
    FragmentNumber: Optional[str] = None

class CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef(BaseValidatorModel):
    KinesisVideoStreamPoolConfiguration: KinesisVideoStreamPoolConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef(BaseValidatorModel):
    KinesisVideoStreamPoolConfiguration: KinesisVideoStreamPoolConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef(BaseValidatorModel):
    KinesisVideoStreamPoolConfiguration: KinesisVideoStreamPoolConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMediaStreamPipelineResponseTypeDef(BaseValidatorModel):
    MediaStreamPipeline: MediaStreamPipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef(BaseValidatorModel):
    Streams: List[RecordingStreamConfigurationTypeDef]
    FragmentSelector: FragmentSelectorOutputTypeDef

class CompositedVideoArtifactsConfigurationTypeDef(BaseValidatorModel):
    GridViewConfiguration: GridViewConfigurationTypeDef
    Layout: Optional[Literal["GridView"]] = None
    Resolution: Optional[ResolutionOptionType] = None

class RealTimeAlertConfigurationOutputTypeDef(BaseValidatorModel):
    Disabled: Optional[bool] = None
    Rules: Optional[List[RealTimeAlertRuleOutputTypeDef]] = None

class RealTimeAlertConfigurationTypeDef(BaseValidatorModel):
    Disabled: Optional[bool] = None
    Rules: Optional[Sequence[RealTimeAlertRuleTypeDef]] = None

class FragmentSelectorTypeDef(BaseValidatorModel):
    FragmentSelectorType: FragmentSelectorTypeType
    TimestampRange: TimestampRangeTypeDef

class MediaCapturePipelineSourceConfigurationTypeDef(BaseValidatorModel):
    MediaPipelineArn: str
    ChimeSdkMeetingConfiguration: ChimeSdkMeetingConcatenationConfigurationTypeDef

class KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef(BaseValidatorModel):
    Streams: List[StreamConfigurationOutputTypeDef]
    MediaEncoding: Literal["pcm"]
    MediaSampleRate: int

class KinesisVideoStreamSourceRuntimeConfigurationTypeDef(BaseValidatorModel):
    Streams: Sequence[StreamConfigurationTypeDef]
    MediaEncoding: Literal["pcm"]
    MediaSampleRate: int

class ArtifactsConfigurationTypeDef(BaseValidatorModel):
    Audio: AudioArtifactsConfigurationTypeDef
    Video: VideoArtifactsConfigurationTypeDef
    Content: ContentArtifactsConfigurationTypeDef
    CompositedVideo: Optional[CompositedVideoArtifactsConfigurationTypeDef] = None

class ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef(BaseValidatorModel):
    Arn: str
    MuxType: LiveConnectorMuxTypeType
    CompositedVideo: Optional[CompositedVideoArtifactsConfigurationTypeDef] = None
    SourceConfiguration: Optional[SourceConfigurationOutputTypeDef] = None

class ChimeSdkMeetingLiveConnectorConfigurationTypeDef(BaseValidatorModel):
    Arn: str
    MuxType: LiveConnectorMuxTypeType
    CompositedVideo: Optional[CompositedVideoArtifactsConfigurationTypeDef] = None
    SourceConfiguration: Optional[SourceConfigurationTypeDef] = None

class MediaInsightsPipelineConfigurationTypeDef(BaseValidatorModel):
    MediaInsightsPipelineConfigurationName: Optional[str] = None
    MediaInsightsPipelineConfigurationArn: Optional[str] = None
    ResourceAccessRoleArn: Optional[str] = None
    RealTimeAlertConfiguration: Optional[RealTimeAlertConfigurationOutputTypeDef] = None
    Elements: Optional[List[MediaInsightsPipelineConfigurationElementOutputTypeDef]] = None
    MediaInsightsPipelineConfigurationId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef(BaseValidatorModel):
    Streams: Sequence[RecordingStreamConfigurationTypeDef]
    FragmentSelector: FragmentSelectorTypeDef

class CreateMediaInsightsPipelineConfigurationRequestRequestTypeDef(BaseValidatorModel):
    MediaInsightsPipelineConfigurationName: str
    ResourceAccessRoleArn: str
    Elements: Sequence[MediaInsightsPipelineConfigurationElementUnionTypeDef]
    RealTimeAlertConfiguration: Optional[RealTimeAlertConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None

class UpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef(BaseValidatorModel):
    Identifier: str
    ResourceAccessRoleArn: str
    Elements: Sequence[MediaInsightsPipelineConfigurationElementUnionTypeDef]
    RealTimeAlertConfiguration: Optional[RealTimeAlertConfigurationTypeDef] = None

class ConcatenationSourceTypeDef(BaseValidatorModel):
    Type: Literal["MediaCapturePipeline"]
    MediaCapturePipelineSourceConfiguration: MediaCapturePipelineSourceConfigurationTypeDef

class MediaInsightsPipelineTypeDef(BaseValidatorModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None
    MediaInsightsPipelineConfigurationArn: Optional[str] = None
    Status: Optional[MediaPipelineStatusType] = None
    KinesisVideoStreamSourceRuntimeConfiguration: Optional[       KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef     ] = None
    MediaInsightsRuntimeMetadata: Optional[Dict[str, str]] = None
    KinesisVideoStreamRecordingSourceRuntimeConfiguration: Optional[       KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef     ] = None
    S3RecordingSinkRuntimeConfiguration: Optional[       S3RecordingSinkRuntimeConfigurationTypeDef     ] = None
    CreatedTimestamp: Optional[datetime] = None
    ElementStatuses: Optional[List[MediaInsightsPipelineElementStatusTypeDef]] = None

class ChimeSdkMeetingConfigurationOutputTypeDef(BaseValidatorModel):
    SourceConfiguration: Optional[SourceConfigurationOutputTypeDef] = None
    ArtifactsConfiguration: Optional[ArtifactsConfigurationTypeDef] = None

class ChimeSdkMeetingConfigurationTypeDef(BaseValidatorModel):
    SourceConfiguration: Optional[SourceConfigurationTypeDef] = None
    ArtifactsConfiguration: Optional[ArtifactsConfigurationTypeDef] = None

class LiveConnectorSourceConfigurationOutputTypeDef(BaseValidatorModel):
    SourceType: Literal["ChimeSdkMeeting"]
    ChimeSdkMeetingLiveConnectorConfiguration: ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef

class LiveConnectorSourceConfigurationTypeDef(BaseValidatorModel):
    SourceType: Literal["ChimeSdkMeeting"]
    ChimeSdkMeetingLiveConnectorConfiguration: ChimeSdkMeetingLiveConnectorConfigurationTypeDef

class CreateMediaInsightsPipelineConfigurationResponseTypeDef(BaseValidatorModel):
    MediaInsightsPipelineConfiguration: MediaInsightsPipelineConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMediaInsightsPipelineConfigurationResponseTypeDef(BaseValidatorModel):
    MediaInsightsPipelineConfiguration: MediaInsightsPipelineConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMediaInsightsPipelineConfigurationResponseTypeDef(BaseValidatorModel):
    MediaInsightsPipelineConfiguration: MediaInsightsPipelineConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMediaInsightsPipelineRequestRequestTypeDef(BaseValidatorModel):
    MediaInsightsPipelineConfigurationArn: str
    KinesisVideoStreamSourceRuntimeConfiguration: Optional[       KinesisVideoStreamSourceRuntimeConfigurationTypeDef     ] = None
    MediaInsightsRuntimeMetadata: Optional[Mapping[str, str]] = None
    KinesisVideoStreamRecordingSourceRuntimeConfiguration: Optional[       KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef     ] = None
    S3RecordingSinkRuntimeConfiguration: Optional[       S3RecordingSinkRuntimeConfigurationTypeDef     ] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None

class CreateMediaConcatenationPipelineRequestRequestTypeDef(BaseValidatorModel):
    Sources: Sequence[ConcatenationSourceTypeDef]
    Sinks: Sequence[ConcatenationSinkTypeDef]
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class MediaConcatenationPipelineTypeDef(BaseValidatorModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None
    Sources: Optional[List[ConcatenationSourceTypeDef]] = None
    Sinks: Optional[List[ConcatenationSinkTypeDef]] = None
    Status: Optional[MediaPipelineStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class CreateMediaInsightsPipelineResponseTypeDef(BaseValidatorModel):
    MediaInsightsPipeline: MediaInsightsPipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MediaCapturePipelineTypeDef(BaseValidatorModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None
    SourceType: Optional[Literal["ChimeSdkMeeting"]] = None
    SourceArn: Optional[str] = None
    Status: Optional[MediaPipelineStatusType] = None
    SinkType: Optional[Literal["S3Bucket"]] = None
    SinkArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    ChimeSdkMeetingConfiguration: Optional[ChimeSdkMeetingConfigurationOutputTypeDef] = None

class CreateMediaCapturePipelineRequestRequestTypeDef(BaseValidatorModel):
    SourceType: Literal["ChimeSdkMeeting"]
    SourceArn: str
    SinkType: Literal["S3Bucket"]
    SinkArn: str
    ClientRequestToken: Optional[str] = None
    ChimeSdkMeetingConfiguration: Optional[ChimeSdkMeetingConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class MediaLiveConnectorPipelineTypeDef(BaseValidatorModel):
    Sources: Optional[List[LiveConnectorSourceConfigurationOutputTypeDef]] = None
    Sinks: Optional[List[LiveConnectorSinkConfigurationTypeDef]] = None
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None
    Status: Optional[MediaPipelineStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class CreateMediaConcatenationPipelineResponseTypeDef(BaseValidatorModel):
    MediaConcatenationPipeline: MediaConcatenationPipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMediaCapturePipelineResponseTypeDef(BaseValidatorModel):
    MediaCapturePipeline: MediaCapturePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMediaCapturePipelineResponseTypeDef(BaseValidatorModel):
    MediaCapturePipeline: MediaCapturePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMediaLiveConnectorPipelineResponseTypeDef(BaseValidatorModel):
    MediaLiveConnectorPipeline: MediaLiveConnectorPipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MediaPipelineTypeDef(BaseValidatorModel):
    MediaCapturePipeline: Optional[MediaCapturePipelineTypeDef] = None
    MediaLiveConnectorPipeline: Optional[MediaLiveConnectorPipelineTypeDef] = None
    MediaConcatenationPipeline: Optional[MediaConcatenationPipelineTypeDef] = None
    MediaInsightsPipeline: Optional[MediaInsightsPipelineTypeDef] = None
    MediaStreamPipeline: Optional[MediaStreamPipelineTypeDef] = None

class CreateMediaLiveConnectorPipelineRequestRequestTypeDef(BaseValidatorModel):
    Sources: Sequence[LiveConnectorSourceConfigurationUnionTypeDef]
    Sinks: Sequence[LiveConnectorSinkConfigurationTypeDef]
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class GetMediaPipelineResponseTypeDef(BaseValidatorModel):
    MediaPipeline: MediaPipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

