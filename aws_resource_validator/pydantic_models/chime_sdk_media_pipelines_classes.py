from aws_resource_validator.pydantic_models.base_validator_model import BaseValidatorModel
from botocore.response import StreamingBody
from datetime import datetime
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

class ActiveSpeakerOnlyConfiguration(BaseValidatorModel):
    ActiveSpeakerPosition: Optional[ActiveSpeakerPositionType] = None


class PostCallAnalyticsSettings(BaseValidatorModel):
    OutputLocation: str
    DataAccessRoleArn: str
    ContentRedactionOutput: Optional[ContentRedactionOutputType] = None
    OutputEncryptionKMSKeyId: Optional[str] = None


class AmazonTranscribeProcessorConfiguration(BaseValidatorModel):
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


class AudioConcatenationConfiguration(BaseValidatorModel):
    State: Literal["Enabled"]


class CompositedVideoConcatenationConfiguration(BaseValidatorModel):
    State: ArtifactsConcatenationStateType


class ContentConcatenationConfiguration(BaseValidatorModel):
    State: ArtifactsConcatenationStateType


class DataChannelConcatenationConfiguration(BaseValidatorModel):
    State: ArtifactsConcatenationStateType


class MeetingEventsConcatenationConfiguration(BaseValidatorModel):
    State: ArtifactsConcatenationStateType


class TranscriptionMessagesConcatenationConfiguration(BaseValidatorModel):
    State: ArtifactsConcatenationStateType


class VideoConcatenationConfiguration(BaseValidatorModel):
    State: ArtifactsConcatenationStateType


class AudioArtifactsConfiguration(BaseValidatorModel):
    MuxType: AudioMuxTypeType


class ContentArtifactsConfiguration(BaseValidatorModel):
    State: ArtifactsStateType
    MuxType: Optional[Literal["ContentOnly"]] = None


class VideoArtifactsConfiguration(BaseValidatorModel):
    State: ArtifactsStateType
    MuxType: Optional[Literal["VideoOnly"]] = None


class ChannelDefinition(BaseValidatorModel):
    ChannelId: int
    ParticipantRole: Optional[ParticipantRoleType] = None


class S3BucketSinkConfiguration(BaseValidatorModel):
    Destination: str


class SseAwsKeyManagementParams(BaseValidatorModel):
    AwsKmsKeyId: str
    AwsKmsEncryptionContext: Optional[str] = None


class Tag(BaseValidatorModel):
    Key: str
    Value: str


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class S3RecordingSinkRuntimeConfiguration(BaseValidatorModel):
    Destination: str
    RecordingFileFormat: RecordingFileFormatType


class KinesisVideoStreamConfiguration(BaseValidatorModel):
    Region: str
    DataRetentionInHours: Optional[int] = None


class MediaStreamSink(BaseValidatorModel):
    SinkArn: str
    SinkType: Literal["KinesisVideoStreamPool"]
    ReservedStreamCapacity: int
    MediaStreamType: MediaStreamTypeType


class MediaStreamSource(BaseValidatorModel):
    SourceType: Literal["ChimeSdkMeeting"]
    SourceArn: str


class DeleteMediaCapturePipelineRequest(BaseValidatorModel):
    MediaPipelineId: str


class DeleteMediaInsightsPipelineConfigurationRequest(BaseValidatorModel):
    Identifier: str


class DeleteMediaPipelineKinesisVideoStreamPoolRequest(BaseValidatorModel):
    Identifier: str


class DeleteMediaPipelineRequest(BaseValidatorModel):
    MediaPipelineId: str


class TimestampRangeOutput(BaseValidatorModel):
    StartTimestamp: datetime
    EndTimestamp: datetime


class GetMediaCapturePipelineRequest(BaseValidatorModel):
    MediaPipelineId: str


class GetMediaInsightsPipelineConfigurationRequest(BaseValidatorModel):
    Identifier: str


class GetMediaPipelineKinesisVideoStreamPoolRequest(BaseValidatorModel):
    Identifier: str


class GetMediaPipelineRequest(BaseValidatorModel):
    MediaPipelineId: str


class GetSpeakerSearchTaskRequest(BaseValidatorModel):
    Identifier: str
    SpeakerSearchTaskId: str


class SpeakerSearchTask(BaseValidatorModel):
    SpeakerSearchTaskId: Optional[str] = None
    SpeakerSearchTaskStatus: Optional[MediaPipelineTaskStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class GetVoiceToneAnalysisTaskRequest(BaseValidatorModel):
    Identifier: str
    VoiceToneAnalysisTaskId: str


class VoiceToneAnalysisTask(BaseValidatorModel):
    VoiceToneAnalysisTaskId: Optional[str] = None
    VoiceToneAnalysisTaskStatus: Optional[MediaPipelineTaskStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class HorizontalLayoutConfiguration(BaseValidatorModel):
    TileOrder: Optional[TileOrderType] = None
    TilePosition: Optional[HorizontalTilePositionType] = None
    TileCount: Optional[int] = None
    TileAspectRatio: Optional[str] = None


class PresenterOnlyConfiguration(BaseValidatorModel):
    PresenterPosition: Optional[PresenterPositionType] = None


class VerticalLayoutConfiguration(BaseValidatorModel):
    TileOrder: Optional[TileOrderType] = None
    TilePosition: Optional[VerticalTilePositionType] = None
    TileCount: Optional[int] = None
    TileAspectRatio: Optional[str] = None


class VideoAttribute(BaseValidatorModel):
    CornerRadius: Optional[int] = None
    BorderColor: Optional[BorderColorType] = None
    HighlightColor: Optional[HighlightColorType] = None
    BorderThickness: Optional[int] = None


class IssueDetectionConfiguration(BaseValidatorModel):
    RuleName: str


class KeywordMatchConfigurationOutput(BaseValidatorModel):
    RuleName: str
    Keywords: List[str]
    Negate: Optional[bool] = None


class KeywordMatchConfiguration(BaseValidatorModel):
    RuleName: str
    Keywords: Sequence[str]
    Negate: Optional[bool] = None


class KinesisDataStreamSinkConfiguration(BaseValidatorModel):
    InsightsTarget: Optional[str] = None


class KinesisVideoStreamConfigurationUpdate(BaseValidatorModel):
    DataRetentionInHours: Optional[int] = None


class KinesisVideoStreamPoolSummary(BaseValidatorModel):
    PoolName: Optional[str] = None
    PoolId: Optional[str] = None
    PoolArn: Optional[str] = None


class RecordingStreamConfiguration(BaseValidatorModel):
    StreamArn: Optional[str] = None


class KinesisVideoStreamSourceTaskConfiguration(BaseValidatorModel):
    StreamArn: str
    ChannelId: int
    FragmentNumber: Optional[str] = None


class LambdaFunctionSinkConfiguration(BaseValidatorModel):
    InsightsTarget: Optional[str] = None


class ListMediaCapturePipelinesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MediaCapturePipelineSummary(BaseValidatorModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None


class ListMediaInsightsPipelineConfigurationsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MediaInsightsPipelineConfigurationSummary(BaseValidatorModel):
    MediaInsightsPipelineConfigurationName: Optional[str] = None
    MediaInsightsPipelineConfigurationId: Optional[str] = None
    MediaInsightsPipelineConfigurationArn: Optional[str] = None


class ListMediaPipelineKinesisVideoStreamPoolsRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class ListMediaPipelinesRequest(BaseValidatorModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None


class MediaPipelineSummary(BaseValidatorModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    ResourceARN: str


class LiveConnectorRTMPConfiguration(BaseValidatorModel):
    Url: str
    AudioChannels: Optional[AudioChannelsOptionType] = None
    AudioSampleRate: Optional[str] = None


class S3RecordingSinkConfiguration(BaseValidatorModel):
    Destination: Optional[str] = None
    RecordingFileFormat: Optional[RecordingFileFormatType] = None


class SnsTopicSinkConfiguration(BaseValidatorModel):
    InsightsTarget: Optional[str] = None


class SqsQueueSinkConfiguration(BaseValidatorModel):
    InsightsTarget: Optional[str] = None


class VoiceAnalyticsProcessorConfiguration(BaseValidatorModel):
    SpeakerSearchStatus: Optional[VoiceAnalyticsConfigurationStatusType] = None
    VoiceToneAnalysisStatus: Optional[VoiceAnalyticsConfigurationStatusType] = None


class VoiceEnhancementSinkConfiguration(BaseValidatorModel):
    Disabled: Optional[bool] = None


class SentimentConfiguration(BaseValidatorModel):
    RuleName: str
    SentimentType: Literal["NEGATIVE"]
    TimePeriod: int


class SelectedVideoStreamsOutput(BaseValidatorModel):
    AttendeeIds: Optional[List[str]] = None
    ExternalUserIds: Optional[List[str]] = None


class SelectedVideoStreams(BaseValidatorModel):
    AttendeeIds: Optional[Sequence[str]] = None
    ExternalUserIds: Optional[Sequence[str]] = None


class StopSpeakerSearchTaskRequest(BaseValidatorModel):
    Identifier: str
    SpeakerSearchTaskId: str


class StopVoiceToneAnalysisTaskRequest(BaseValidatorModel):
    Identifier: str
    VoiceToneAnalysisTaskId: str


class UntagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    TagKeys: Sequence[str]


class UpdateMediaInsightsPipelineStatusRequest(BaseValidatorModel):
    Identifier: str
    UpdateStatus: MediaPipelineStatusUpdateType


class AmazonTranscribeCallAnalyticsProcessorConfigurationOutput(BaseValidatorModel):
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
    PostCallAnalyticsSettings: Optional[PostCallAnalyticsSettings] = None
    CallAnalyticsStreamCategories: Optional[List[str]] = None


class AmazonTranscribeCallAnalyticsProcessorConfiguration(BaseValidatorModel):
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
    PostCallAnalyticsSettings: Optional[PostCallAnalyticsSettings] = None
    CallAnalyticsStreamCategories: Optional[Sequence[str]] = None


class ArtifactsConcatenationConfiguration(BaseValidatorModel):
    Audio: AudioConcatenationConfiguration
    Video: VideoConcatenationConfiguration
    Content: ContentConcatenationConfiguration
    DataChannel: DataChannelConcatenationConfiguration
    TranscriptionMessages: TranscriptionMessagesConcatenationConfiguration
    MeetingEvents: MeetingEventsConcatenationConfiguration
    CompositedVideo: CompositedVideoConcatenationConfiguration


class StreamChannelDefinitionOutput(BaseValidatorModel):
    NumberOfChannels: int
    ChannelDefinitions: Optional[List[ChannelDefinition]] = None


class StreamChannelDefinition(BaseValidatorModel):
    NumberOfChannels: int
    ChannelDefinitions: Optional[Sequence[ChannelDefinition]] = None


class TagResourceRequest(BaseValidatorModel):
    ResourceARN: str
    Tags: Sequence[Tag]


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    Tags: List[Tag]
    ResponseMetadata: ResponseMetadata


class CreateMediaPipelineKinesisVideoStreamPoolRequest(BaseValidatorModel):
    StreamConfiguration: KinesisVideoStreamConfiguration
    PoolName: str
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class KinesisVideoStreamPoolConfiguration(BaseValidatorModel):
    PoolArn: Optional[str] = None
    PoolName: Optional[str] = None
    PoolId: Optional[str] = None
    PoolStatus: Optional[KinesisVideoStreamPoolStatusType] = None
    PoolSize: Optional[int] = None
    StreamConfiguration: Optional[KinesisVideoStreamConfiguration] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class CreateMediaStreamPipelineRequest(BaseValidatorModel):
    Sources: Sequence[MediaStreamSource]
    Sinks: Sequence[MediaStreamSink]
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class MediaStreamPipeline(BaseValidatorModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    Status: Optional[MediaPipelineStatusType] = None
    Sources: Optional[List[MediaStreamSource]] = None
    Sinks: Optional[List[MediaStreamSink]] = None


class FragmentSelectorOutput(BaseValidatorModel):
    FragmentSelectorType: FragmentSelectorTypeType
    TimestampRange: TimestampRangeOutput


class GetSpeakerSearchTaskResponse(BaseValidatorModel):
    SpeakerSearchTask: SpeakerSearchTask
    ResponseMetadata: ResponseMetadata


class StartSpeakerSearchTaskResponse(BaseValidatorModel):
    SpeakerSearchTask: SpeakerSearchTask
    ResponseMetadata: ResponseMetadata


class GetVoiceToneAnalysisTaskResponse(BaseValidatorModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTask
    ResponseMetadata: ResponseMetadata


class StartVoiceToneAnalysisTaskResponse(BaseValidatorModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTask
    ResponseMetadata: ResponseMetadata


class GridViewConfiguration(BaseValidatorModel):
    ContentShareLayout: ContentShareLayoutOptionType
    PresenterOnlyConfiguration: Optional[PresenterOnlyConfiguration] = None
    ActiveSpeakerOnlyConfiguration: Optional[ActiveSpeakerOnlyConfiguration] = None
    HorizontalLayoutConfiguration: Optional[HorizontalLayoutConfiguration] = None
    VerticalLayoutConfiguration: Optional[VerticalLayoutConfiguration] = None
    VideoAttribute: Optional[VideoAttribute] = None
    CanvasOrientation: Optional[CanvasOrientationType] = None


class UpdateMediaPipelineKinesisVideoStreamPoolRequest(BaseValidatorModel):
    Identifier: str
    StreamConfiguration: Optional[KinesisVideoStreamConfigurationUpdate] = None


class ListMediaPipelineKinesisVideoStreamPoolsResponse(BaseValidatorModel):
    KinesisVideoStreamPools: List[KinesisVideoStreamPoolSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class StartSpeakerSearchTaskRequest(BaseValidatorModel):
    Identifier: str
    VoiceProfileDomainArn: str
    KinesisVideoStreamSourceTaskConfiguration: Optional[ KinesisVideoStreamSourceTaskConfiguration ] = None
    ClientRequestToken: Optional[str] = None


class StartVoiceToneAnalysisTaskRequest(BaseValidatorModel):
    Identifier: str
    LanguageCode: Literal["en-US"]
    KinesisVideoStreamSourceTaskConfiguration: Optional[ KinesisVideoStreamSourceTaskConfiguration ] = None
    ClientRequestToken: Optional[str] = None


class ListMediaCapturePipelinesResponse(BaseValidatorModel):
    MediaCapturePipelines: List[MediaCapturePipelineSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMediaInsightsPipelineConfigurationsResponse(BaseValidatorModel):
    MediaInsightsPipelineConfigurations: List[MediaInsightsPipelineConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class ListMediaPipelinesResponse(BaseValidatorModel):
    MediaPipelines: List[MediaPipelineSummary]
    ResponseMetadata: ResponseMetadata
    NextToken: Optional[str] = None


class LiveConnectorSinkConfiguration(BaseValidatorModel):
    SinkType: Literal["RTMP"]
    RTMPConfiguration: LiveConnectorRTMPConfiguration


class SourceConfigurationOutput(BaseValidatorModel):
    SelectedVideoStreams: Optional[SelectedVideoStreamsOutput] = None


class Timestamp(BaseValidatorModel):
    pass


class TimestampRange(BaseValidatorModel):
    StartTimestamp: Timestamp
    EndTimestamp: Timestamp


class ChimeSdkMeetingConcatenationConfiguration(BaseValidatorModel):
    ArtifactsConfiguration: ArtifactsConcatenationConfiguration


class StreamConfigurationOutput(BaseValidatorModel):
    StreamArn: str
    StreamChannelDefinition: StreamChannelDefinitionOutput
    FragmentNumber: Optional[str] = None


class StreamConfiguration(BaseValidatorModel):
    StreamArn: str
    StreamChannelDefinition: StreamChannelDefinition
    FragmentNumber: Optional[str] = None


class CreateMediaPipelineKinesisVideoStreamPoolResponse(BaseValidatorModel):
    KinesisVideoStreamPoolConfiguration: KinesisVideoStreamPoolConfiguration
    ResponseMetadata: ResponseMetadata


class GetMediaPipelineKinesisVideoStreamPoolResponse(BaseValidatorModel):
    KinesisVideoStreamPoolConfiguration: KinesisVideoStreamPoolConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateMediaPipelineKinesisVideoStreamPoolResponse(BaseValidatorModel):
    KinesisVideoStreamPoolConfiguration: KinesisVideoStreamPoolConfiguration
    ResponseMetadata: ResponseMetadata


class CreateMediaStreamPipelineResponse(BaseValidatorModel):
    MediaStreamPipeline: MediaStreamPipeline
    ResponseMetadata: ResponseMetadata


class KinesisVideoStreamRecordingSourceRuntimeConfigurationOutput(BaseValidatorModel):
    Streams: List[RecordingStreamConfiguration]
    FragmentSelector: FragmentSelectorOutput


class CompositedVideoArtifactsConfiguration(BaseValidatorModel):
    GridViewConfiguration: GridViewConfiguration
    Layout: Optional[Literal["GridView"]] = None
    Resolution: Optional[ResolutionOptionType] = None


class RealTimeAlertRuleOutput(BaseValidatorModel):
    pass


class RealTimeAlertConfigurationOutput(BaseValidatorModel):
    Disabled: Optional[bool] = None
    Rules: Optional[List[RealTimeAlertRuleOutput]] = None


class RealTimeAlertRule(BaseValidatorModel):
    pass


class RealTimeAlertConfiguration(BaseValidatorModel):
    Disabled: Optional[bool] = None
    Rules: Optional[Sequence[RealTimeAlertRule]] = None


class SelectedVideoStreamsUnion(BaseValidatorModel):
    pass


class SourceConfiguration(BaseValidatorModel):
    SelectedVideoStreams: Optional[SelectedVideoStreamsUnion] = None


class FragmentSelector(BaseValidatorModel):
    FragmentSelectorType: FragmentSelectorTypeType
    TimestampRange: TimestampRange


class MediaCapturePipelineSourceConfiguration(BaseValidatorModel):
    MediaPipelineArn: str
    ChimeSdkMeetingConfiguration: ChimeSdkMeetingConcatenationConfiguration


class KinesisVideoStreamSourceRuntimeConfigurationOutput(BaseValidatorModel):
    Streams: List[StreamConfigurationOutput]
    MediaEncoding: Literal["pcm"]
    MediaSampleRate: int


class KinesisVideoStreamSourceRuntimeConfiguration(BaseValidatorModel):
    Streams: Sequence[StreamConfiguration]
    MediaEncoding: Literal["pcm"]
    MediaSampleRate: int


class ArtifactsConfiguration(BaseValidatorModel):
    Audio: AudioArtifactsConfiguration
    Video: VideoArtifactsConfiguration
    Content: ContentArtifactsConfiguration
    CompositedVideo: Optional[CompositedVideoArtifactsConfiguration] = None


class ChimeSdkMeetingLiveConnectorConfigurationOutput(BaseValidatorModel):
    Arn: str
    MuxType: LiveConnectorMuxTypeType
    CompositedVideo: Optional[CompositedVideoArtifactsConfiguration] = None
    SourceConfiguration: Optional[SourceConfigurationOutput] = None


class MediaInsightsPipelineConfigurationElementOutput(BaseValidatorModel):
    pass


class MediaInsightsPipelineConfiguration(BaseValidatorModel):
    MediaInsightsPipelineConfigurationName: Optional[str] = None
    MediaInsightsPipelineConfigurationArn: Optional[str] = None
    ResourceAccessRoleArn: Optional[str] = None
    RealTimeAlertConfiguration: Optional[RealTimeAlertConfigurationOutput] = None
    Elements: Optional[List[MediaInsightsPipelineConfigurationElementOutput]] = None
    MediaInsightsPipelineConfigurationId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class KinesisVideoStreamRecordingSourceRuntimeConfiguration(BaseValidatorModel):
    Streams: Sequence[RecordingStreamConfiguration]
    FragmentSelector: FragmentSelector


class MediaInsightsPipelineElementStatus(BaseValidatorModel):
    pass


class MediaInsightsPipeline(BaseValidatorModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None
    MediaInsightsPipelineConfigurationArn: Optional[str] = None
    Status: Optional[MediaPipelineStatusType] = None
    KinesisVideoStreamSourceRuntimeConfiguration: Optional[ KinesisVideoStreamSourceRuntimeConfigurationOutput ] = None
    MediaInsightsRuntimeMetadata: Optional[Dict[str, str]] = None
    KinesisVideoStreamRecordingSourceRuntimeConfiguration: Optional[ KinesisVideoStreamRecordingSourceRuntimeConfigurationOutput ] = None
    S3RecordingSinkRuntimeConfiguration: Optional[S3RecordingSinkRuntimeConfiguration] = None
    CreatedTimestamp: Optional[datetime] = None
    ElementStatuses: Optional[List[MediaInsightsPipelineElementStatus]] = None


class ChimeSdkMeetingConfigurationOutput(BaseValidatorModel):
    SourceConfiguration: Optional[SourceConfigurationOutput] = None
    ArtifactsConfiguration: Optional[ArtifactsConfiguration] = None


class ChimeSdkMeetingConfiguration(BaseValidatorModel):
    SourceConfiguration: Optional[SourceConfiguration] = None
    ArtifactsConfiguration: Optional[ArtifactsConfiguration] = None


class LiveConnectorSourceConfigurationOutput(BaseValidatorModel):
    SourceType: Literal["ChimeSdkMeeting"]
    ChimeSdkMeetingLiveConnectorConfiguration: ( ChimeSdkMeetingLiveConnectorConfigurationOutput )


class CreateMediaInsightsPipelineConfigurationResponse(BaseValidatorModel):
    MediaInsightsPipelineConfiguration: MediaInsightsPipelineConfiguration
    ResponseMetadata: ResponseMetadata


class GetMediaInsightsPipelineConfigurationResponse(BaseValidatorModel):
    MediaInsightsPipelineConfiguration: MediaInsightsPipelineConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateMediaInsightsPipelineConfigurationResponse(BaseValidatorModel):
    MediaInsightsPipelineConfiguration: MediaInsightsPipelineConfiguration
    ResponseMetadata: ResponseMetadata


class SourceConfigurationUnion(BaseValidatorModel):
    pass


class ChimeSdkMeetingLiveConnectorConfiguration(BaseValidatorModel):
    Arn: str
    MuxType: LiveConnectorMuxTypeType
    CompositedVideo: Optional[CompositedVideoArtifactsConfiguration] = None
    SourceConfiguration: Optional[SourceConfigurationUnion] = None


class RealTimeAlertConfigurationUnion(BaseValidatorModel):
    pass


class MediaInsightsPipelineConfigurationElementUnion(BaseValidatorModel):
    pass


class CreateMediaInsightsPipelineConfigurationRequest(BaseValidatorModel):
    MediaInsightsPipelineConfigurationName: str
    ResourceAccessRoleArn: str
    Elements: Sequence[MediaInsightsPipelineConfigurationElementUnion]
    RealTimeAlertConfiguration: Optional[RealTimeAlertConfigurationUnion] = None
    Tags: Optional[Sequence[Tag]] = None
    ClientRequestToken: Optional[str] = None


class UpdateMediaInsightsPipelineConfigurationRequest(BaseValidatorModel):
    Identifier: str
    ResourceAccessRoleArn: str
    Elements: Sequence[MediaInsightsPipelineConfigurationElementUnion]
    RealTimeAlertConfiguration: Optional[RealTimeAlertConfigurationUnion] = None


class ConcatenationSink(BaseValidatorModel):
    pass


class ConcatenationSource(BaseValidatorModel):
    pass


class CreateMediaConcatenationPipelineRequest(BaseValidatorModel):
    Sources: Sequence[ConcatenationSource]
    Sinks: Sequence[ConcatenationSink]
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class MediaConcatenationPipeline(BaseValidatorModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None
    Sources: Optional[List[ConcatenationSource]] = None
    Sinks: Optional[List[ConcatenationSink]] = None
    Status: Optional[MediaPipelineStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class CreateMediaInsightsPipelineResponse(BaseValidatorModel):
    MediaInsightsPipeline: MediaInsightsPipeline
    ResponseMetadata: ResponseMetadata


class MediaCapturePipeline(BaseValidatorModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None
    SourceType: Optional[Literal["ChimeSdkMeeting"]] = None
    SourceArn: Optional[str] = None
    Status: Optional[MediaPipelineStatusType] = None
    SinkType: Optional[Literal["S3Bucket"]] = None
    SinkArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    ChimeSdkMeetingConfiguration: Optional[ChimeSdkMeetingConfigurationOutput] = None
    SseAwsKeyManagementParams: Optional[SseAwsKeyManagementParams] = None
    SinkIamRoleArn: Optional[str] = None


class MediaLiveConnectorPipeline(BaseValidatorModel):
    Sources: Optional[List[LiveConnectorSourceConfigurationOutput]] = None
    Sinks: Optional[List[LiveConnectorSinkConfiguration]] = None
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None
    Status: Optional[MediaPipelineStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None


class KinesisVideoStreamSourceRuntimeConfigurationUnion(BaseValidatorModel):
    pass


class KinesisVideoStreamRecordingSourceRuntimeConfigurationUnion(BaseValidatorModel):
    pass


class CreateMediaInsightsPipelineRequest(BaseValidatorModel):
    MediaInsightsPipelineConfigurationArn: str
    KinesisVideoStreamSourceRuntimeConfiguration: Optional[ KinesisVideoStreamSourceRuntimeConfigurationUnion ] = None
    MediaInsightsRuntimeMetadata: Optional[Mapping[str, str]] = None
    KinesisVideoStreamRecordingSourceRuntimeConfiguration: Optional[ KinesisVideoStreamRecordingSourceRuntimeConfigurationUnion ] = None
    S3RecordingSinkRuntimeConfiguration: Optional[S3RecordingSinkRuntimeConfiguration] = None
    Tags: Optional[Sequence[Tag]] = None
    ClientRequestToken: Optional[str] = None


class CreateMediaConcatenationPipelineResponse(BaseValidatorModel):
    MediaConcatenationPipeline: MediaConcatenationPipeline
    ResponseMetadata: ResponseMetadata


class CreateMediaCapturePipelineResponse(BaseValidatorModel):
    MediaCapturePipeline: MediaCapturePipeline
    ResponseMetadata: ResponseMetadata


class GetMediaCapturePipelineResponse(BaseValidatorModel):
    MediaCapturePipeline: MediaCapturePipeline
    ResponseMetadata: ResponseMetadata


class ChimeSdkMeetingConfigurationUnion(BaseValidatorModel):
    pass


class CreateMediaCapturePipelineRequest(BaseValidatorModel):
    SourceType: Literal["ChimeSdkMeeting"]
    SourceArn: str
    SinkType: Literal["S3Bucket"]
    SinkArn: str
    ClientRequestToken: Optional[str] = None
    ChimeSdkMeetingConfiguration: Optional[ChimeSdkMeetingConfigurationUnion] = None
    SseAwsKeyManagementParams: Optional[SseAwsKeyManagementParams] = None
    SinkIamRoleArn: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


class CreateMediaLiveConnectorPipelineResponse(BaseValidatorModel):
    MediaLiveConnectorPipeline: MediaLiveConnectorPipeline
    ResponseMetadata: ResponseMetadata


class MediaPipeline(BaseValidatorModel):
    MediaCapturePipeline: Optional[MediaCapturePipeline] = None
    MediaLiveConnectorPipeline: Optional[MediaLiveConnectorPipeline] = None
    MediaConcatenationPipeline: Optional[MediaConcatenationPipeline] = None
    MediaInsightsPipeline: Optional[MediaInsightsPipeline] = None
    MediaStreamPipeline: Optional[MediaStreamPipeline] = None


class ChimeSdkMeetingLiveConnectorConfigurationUnion(BaseValidatorModel):
    pass


class LiveConnectorSourceConfiguration(BaseValidatorModel):
    SourceType: Literal["ChimeSdkMeeting"]
    ChimeSdkMeetingLiveConnectorConfiguration: ChimeSdkMeetingLiveConnectorConfigurationUnion


class GetMediaPipelineResponse(BaseValidatorModel):
    MediaPipeline: MediaPipeline
    ResponseMetadata: ResponseMetadata


class LiveConnectorSourceConfigurationUnion(BaseValidatorModel):
    pass


class CreateMediaLiveConnectorPipelineRequest(BaseValidatorModel):
    Sources: Sequence[LiveConnectorSourceConfigurationUnion]
    Sinks: Sequence[LiveConnectorSinkConfiguration]
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[Tag]] = None


