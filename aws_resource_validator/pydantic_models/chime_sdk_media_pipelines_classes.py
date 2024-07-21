from datetime import datetime
from pydantic import BaseModel
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

class ActiveSpeakerOnlyConfigurationTypeDef(BaseModel):
    ActiveSpeakerPosition: Optional[ActiveSpeakerPositionType] = None

class PostCallAnalyticsSettingsTypeDef(BaseModel):
    OutputLocation: str
    DataAccessRoleArn: str
    ContentRedactionOutput: Optional[ContentRedactionOutputType] = None
    OutputEncryptionKMSKeyId: Optional[str] = None

class AmazonTranscribeProcessorConfigurationTypeDef(BaseModel):
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

class AudioConcatenationConfigurationTypeDef(BaseModel):
    State: Literal["Enabled"]

class CompositedVideoConcatenationConfigurationTypeDef(BaseModel):
    State: ArtifactsConcatenationStateType

class ContentConcatenationConfigurationTypeDef(BaseModel):
    State: ArtifactsConcatenationStateType

class DataChannelConcatenationConfigurationTypeDef(BaseModel):
    State: ArtifactsConcatenationStateType

class MeetingEventsConcatenationConfigurationTypeDef(BaseModel):
    State: ArtifactsConcatenationStateType

class TranscriptionMessagesConcatenationConfigurationTypeDef(BaseModel):
    State: ArtifactsConcatenationStateType

class VideoConcatenationConfigurationTypeDef(BaseModel):
    State: ArtifactsConcatenationStateType

class AudioArtifactsConfigurationTypeDef(BaseModel):
    MuxType: AudioMuxTypeType

class ContentArtifactsConfigurationTypeDef(BaseModel):
    State: ArtifactsStateType
    MuxType: Optional[Literal["ContentOnly"]] = None

class VideoArtifactsConfigurationTypeDef(BaseModel):
    State: ArtifactsStateType
    MuxType: Optional[Literal["VideoOnly"]] = None

class ChannelDefinitionTypeDef(BaseModel):
    ChannelId: int
    ParticipantRole: Optional[ParticipantRoleType] = None

class S3BucketSinkConfigurationTypeDef(BaseModel):
    Destination: str

class TagTypeDef(BaseModel):
    Key: str
    Value: str

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class S3RecordingSinkRuntimeConfigurationTypeDef(BaseModel):
    Destination: str
    RecordingFileFormat: RecordingFileFormatType

class KinesisVideoStreamConfigurationTypeDef(BaseModel):
    Region: str
    DataRetentionInHours: Optional[int] = None

class MediaStreamSinkTypeDef(BaseModel):
    SinkArn: str
    SinkType: Literal["KinesisVideoStreamPool"]
    ReservedStreamCapacity: int
    MediaStreamType: MediaStreamTypeType

class MediaStreamSourceTypeDef(BaseModel):
    SourceType: Literal["ChimeSdkMeeting"]
    SourceArn: str

class DeleteMediaCapturePipelineRequestRequestTypeDef(BaseModel):
    MediaPipelineId: str

class DeleteMediaInsightsPipelineConfigurationRequestRequestTypeDef(BaseModel):
    Identifier: str

class DeleteMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef(BaseModel):
    Identifier: str

class DeleteMediaPipelineRequestRequestTypeDef(BaseModel):
    MediaPipelineId: str

class TimestampRangeOutputTypeDef(BaseModel):
    StartTimestamp: datetime
    EndTimestamp: datetime

class GetMediaCapturePipelineRequestRequestTypeDef(BaseModel):
    MediaPipelineId: str

class GetMediaInsightsPipelineConfigurationRequestRequestTypeDef(BaseModel):
    Identifier: str

class GetMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef(BaseModel):
    Identifier: str

class GetMediaPipelineRequestRequestTypeDef(BaseModel):
    MediaPipelineId: str

class GetSpeakerSearchTaskRequestRequestTypeDef(BaseModel):
    Identifier: str
    SpeakerSearchTaskId: str

class SpeakerSearchTaskTypeDef(BaseModel):
    SpeakerSearchTaskId: Optional[str] = None
    SpeakerSearchTaskStatus: Optional[MediaPipelineTaskStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class GetVoiceToneAnalysisTaskRequestRequestTypeDef(BaseModel):
    Identifier: str
    VoiceToneAnalysisTaskId: str

class VoiceToneAnalysisTaskTypeDef(BaseModel):
    VoiceToneAnalysisTaskId: Optional[str] = None
    VoiceToneAnalysisTaskStatus: Optional[MediaPipelineTaskStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class HorizontalLayoutConfigurationTypeDef(BaseModel):
    TileOrder: Optional[TileOrderType] = None
    TilePosition: Optional[HorizontalTilePositionType] = None
    TileCount: Optional[int] = None
    TileAspectRatio: Optional[str] = None

class PresenterOnlyConfigurationTypeDef(BaseModel):
    PresenterPosition: Optional[PresenterPositionType] = None

class VerticalLayoutConfigurationTypeDef(BaseModel):
    TileOrder: Optional[TileOrderType] = None
    TilePosition: Optional[VerticalTilePositionType] = None
    TileCount: Optional[int] = None
    TileAspectRatio: Optional[str] = None

class VideoAttributeTypeDef(BaseModel):
    CornerRadius: Optional[int] = None
    BorderColor: Optional[BorderColorType] = None
    HighlightColor: Optional[HighlightColorType] = None
    BorderThickness: Optional[int] = None

class IssueDetectionConfigurationTypeDef(BaseModel):
    RuleName: str

class KeywordMatchConfigurationOutputTypeDef(BaseModel):
    RuleName: str
    Keywords: List[str]
    Negate: Optional[bool] = None

class KeywordMatchConfigurationTypeDef(BaseModel):
    RuleName: str
    Keywords: Sequence[str]
    Negate: Optional[bool] = None

class KinesisDataStreamSinkConfigurationTypeDef(BaseModel):
    InsightsTarget: Optional[str] = None

class KinesisVideoStreamConfigurationUpdateTypeDef(BaseModel):
    DataRetentionInHours: Optional[int] = None

class KinesisVideoStreamPoolSummaryTypeDef(BaseModel):
    PoolName: Optional[str] = None
    PoolId: Optional[str] = None
    PoolArn: Optional[str] = None

class RecordingStreamConfigurationTypeDef(BaseModel):
    StreamArn: Optional[str] = None

class KinesisVideoStreamSourceTaskConfigurationTypeDef(BaseModel):
    StreamArn: str
    ChannelId: int
    FragmentNumber: Optional[str] = None

class LambdaFunctionSinkConfigurationTypeDef(BaseModel):
    InsightsTarget: Optional[str] = None

class ListMediaCapturePipelinesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MediaCapturePipelineSummaryTypeDef(BaseModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None

class ListMediaInsightsPipelineConfigurationsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MediaInsightsPipelineConfigurationSummaryTypeDef(BaseModel):
    MediaInsightsPipelineConfigurationName: Optional[str] = None
    MediaInsightsPipelineConfigurationId: Optional[str] = None
    MediaInsightsPipelineConfigurationArn: Optional[str] = None

class ListMediaPipelineKinesisVideoStreamPoolsRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class ListMediaPipelinesRequestRequestTypeDef(BaseModel):
    NextToken: Optional[str] = None
    MaxResults: Optional[int] = None

class MediaPipelineSummaryTypeDef(BaseModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str

class LiveConnectorRTMPConfigurationTypeDef(BaseModel):
    Url: str
    AudioChannels: Optional[AudioChannelsOptionType] = None
    AudioSampleRate: Optional[str] = None

class S3RecordingSinkConfigurationTypeDef(BaseModel):
    Destination: Optional[str] = None
    RecordingFileFormat: Optional[RecordingFileFormatType] = None

class SnsTopicSinkConfigurationTypeDef(BaseModel):
    InsightsTarget: Optional[str] = None

class SqsQueueSinkConfigurationTypeDef(BaseModel):
    InsightsTarget: Optional[str] = None

class VoiceAnalyticsProcessorConfigurationTypeDef(BaseModel):
    SpeakerSearchStatus: Optional[VoiceAnalyticsConfigurationStatusType] = None
    VoiceToneAnalysisStatus: Optional[VoiceAnalyticsConfigurationStatusType] = None

class VoiceEnhancementSinkConfigurationTypeDef(BaseModel):
    Disabled: Optional[bool] = None

class MediaInsightsPipelineElementStatusTypeDef(BaseModel):
    Type: Optional[MediaInsightsPipelineConfigurationElementTypeType] = None
    Status: Optional[MediaPipelineElementStatusType] = None

class SentimentConfigurationTypeDef(BaseModel):
    RuleName: str
    SentimentType: Literal["NEGATIVE"]
    TimePeriod: int

class SelectedVideoStreamsOutputTypeDef(BaseModel):
    AttendeeIds: Optional[List[str]] = None
    ExternalUserIds: Optional[List[str]] = None

class SelectedVideoStreamsTypeDef(BaseModel):
    AttendeeIds: Optional[Sequence[str]] = None
    ExternalUserIds: Optional[Sequence[str]] = None

class StopSpeakerSearchTaskRequestRequestTypeDef(BaseModel):
    Identifier: str
    SpeakerSearchTaskId: str

class StopVoiceToneAnalysisTaskRequestRequestTypeDef(BaseModel):
    Identifier: str
    VoiceToneAnalysisTaskId: str

class UntagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    TagKeys: Sequence[str]

class UpdateMediaInsightsPipelineStatusRequestRequestTypeDef(BaseModel):
    Identifier: str
    UpdateStatus: MediaPipelineStatusUpdateType

class AmazonTranscribeCallAnalyticsProcessorConfigurationOutputTypeDef(BaseModel):
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

class AmazonTranscribeCallAnalyticsProcessorConfigurationTypeDef(BaseModel):
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

class ArtifactsConcatenationConfigurationTypeDef(BaseModel):
    Audio: AudioConcatenationConfigurationTypeDef
    Video: VideoConcatenationConfigurationTypeDef
    Content: ContentConcatenationConfigurationTypeDef
    DataChannel: DataChannelConcatenationConfigurationTypeDef
    TranscriptionMessages: TranscriptionMessagesConcatenationConfigurationTypeDef
    MeetingEvents: MeetingEventsConcatenationConfigurationTypeDef
    CompositedVideo: CompositedVideoConcatenationConfigurationTypeDef

class StreamChannelDefinitionOutputTypeDef(BaseModel):
    NumberOfChannels: int
    ChannelDefinitions: Optional[List[ChannelDefinitionTypeDef]] = None

class StreamChannelDefinitionTypeDef(BaseModel):
    NumberOfChannels: int
    ChannelDefinitions: Optional[Sequence[ChannelDefinitionTypeDef]] = None

class ConcatenationSinkTypeDef(BaseModel):
    Type: Literal["S3Bucket"]
    S3BucketSinkConfiguration: S3BucketSinkConfigurationTypeDef

class TagResourceRequestRequestTypeDef(BaseModel):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef(BaseModel):
    StreamConfiguration: KinesisVideoStreamConfigurationTypeDef
    PoolName: str
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class KinesisVideoStreamPoolConfigurationTypeDef(BaseModel):
    PoolArn: Optional[str] = None
    PoolName: Optional[str] = None
    PoolId: Optional[str] = None
    PoolStatus: Optional[KinesisVideoStreamPoolStatusType] = None
    PoolSize: Optional[int] = None
    StreamConfiguration: Optional[KinesisVideoStreamConfigurationTypeDef] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class CreateMediaStreamPipelineRequestRequestTypeDef(BaseModel):
    Sources: Sequence[MediaStreamSourceTypeDef]
    Sinks: Sequence[MediaStreamSinkTypeDef]
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class MediaStreamPipelineTypeDef(BaseModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None
    Status: Optional[MediaPipelineStatusType] = None
    Sources: Optional[List[MediaStreamSourceTypeDef]] = None
    Sinks: Optional[List[MediaStreamSinkTypeDef]] = None

class FragmentSelectorOutputTypeDef(BaseModel):
    FragmentSelectorType: FragmentSelectorTypeType
    TimestampRange: TimestampRangeOutputTypeDef

class GetSpeakerSearchTaskResponseTypeDef(BaseModel):
    SpeakerSearchTask: SpeakerSearchTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartSpeakerSearchTaskResponseTypeDef(BaseModel):
    SpeakerSearchTask: SpeakerSearchTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetVoiceToneAnalysisTaskResponseTypeDef(BaseModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StartVoiceToneAnalysisTaskResponseTypeDef(BaseModel):
    VoiceToneAnalysisTask: VoiceToneAnalysisTaskTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GridViewConfigurationTypeDef(BaseModel):
    ContentShareLayout: ContentShareLayoutOptionType
    PresenterOnlyConfiguration: Optional[PresenterOnlyConfigurationTypeDef] = None
    ActiveSpeakerOnlyConfiguration: Optional[ActiveSpeakerOnlyConfigurationTypeDef] = None
    HorizontalLayoutConfiguration: Optional[HorizontalLayoutConfigurationTypeDef] = None
    VerticalLayoutConfiguration: Optional[VerticalLayoutConfigurationTypeDef] = None
    VideoAttribute: Optional[VideoAttributeTypeDef] = None
    CanvasOrientation: Optional[CanvasOrientationType] = None

class UpdateMediaPipelineKinesisVideoStreamPoolRequestRequestTypeDef(BaseModel):
    Identifier: str
    StreamConfiguration: Optional[KinesisVideoStreamConfigurationUpdateTypeDef] = None

class ListMediaPipelineKinesisVideoStreamPoolsResponseTypeDef(BaseModel):
    KinesisVideoStreamPools: List[KinesisVideoStreamPoolSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class StartSpeakerSearchTaskRequestRequestTypeDef(BaseModel):
    Identifier: str
    VoiceProfileDomainArn: str
    KinesisVideoStreamSourceTaskConfiguration: Optional[       KinesisVideoStreamSourceTaskConfigurationTypeDef     ] = None
    ClientRequestToken: Optional[str] = None

class StartVoiceToneAnalysisTaskRequestRequestTypeDef(BaseModel):
    Identifier: str
    LanguageCode: Literal["en-US"]
    KinesisVideoStreamSourceTaskConfiguration: Optional[       KinesisVideoStreamSourceTaskConfigurationTypeDef     ] = None
    ClientRequestToken: Optional[str] = None

class ListMediaCapturePipelinesResponseTypeDef(BaseModel):
    MediaCapturePipelines: List[MediaCapturePipelineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMediaInsightsPipelineConfigurationsResponseTypeDef(BaseModel):
    MediaInsightsPipelineConfigurations: List[       MediaInsightsPipelineConfigurationSummaryTypeDef     ]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class ListMediaPipelinesResponseTypeDef(BaseModel):
    MediaPipelines: List[MediaPipelineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: Optional[str] = None

class LiveConnectorSinkConfigurationTypeDef(BaseModel):
    SinkType: Literal["RTMP"]
    RTMPConfiguration: LiveConnectorRTMPConfigurationTypeDef

class RealTimeAlertRuleOutputTypeDef(BaseModel):
    Type: RealTimeAlertRuleTypeType
    KeywordMatchConfiguration: Optional[KeywordMatchConfigurationOutputTypeDef] = None
    SentimentConfiguration: Optional[SentimentConfigurationTypeDef] = None
    IssueDetectionConfiguration: Optional[IssueDetectionConfigurationTypeDef] = None

class RealTimeAlertRuleTypeDef(BaseModel):
    Type: RealTimeAlertRuleTypeType
    KeywordMatchConfiguration: Optional[KeywordMatchConfigurationTypeDef] = None
    SentimentConfiguration: Optional[SentimentConfigurationTypeDef] = None
    IssueDetectionConfiguration: Optional[IssueDetectionConfigurationTypeDef] = None

class SourceConfigurationOutputTypeDef(BaseModel):
    SelectedVideoStreams: Optional[SelectedVideoStreamsOutputTypeDef] = None

class SourceConfigurationTypeDef(BaseModel):
    SelectedVideoStreams: Optional[SelectedVideoStreamsTypeDef] = None

class TimestampRangeTypeDef(BaseModel):
    StartTimestamp: TimestampTypeDef
    EndTimestamp: TimestampTypeDef

class MediaInsightsPipelineConfigurationElementOutputTypeDef(BaseModel):
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

class MediaInsightsPipelineConfigurationElementTypeDef(BaseModel):
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

class ChimeSdkMeetingConcatenationConfigurationTypeDef(BaseModel):
    ArtifactsConfiguration: ArtifactsConcatenationConfigurationTypeDef

class StreamConfigurationOutputTypeDef(BaseModel):
    StreamArn: str
    StreamChannelDefinition: StreamChannelDefinitionOutputTypeDef
    FragmentNumber: Optional[str] = None

class StreamConfigurationTypeDef(BaseModel):
    StreamArn: str
    StreamChannelDefinition: StreamChannelDefinitionTypeDef
    FragmentNumber: Optional[str] = None

class CreateMediaPipelineKinesisVideoStreamPoolResponseTypeDef(BaseModel):
    KinesisVideoStreamPoolConfiguration: KinesisVideoStreamPoolConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMediaPipelineKinesisVideoStreamPoolResponseTypeDef(BaseModel):
    KinesisVideoStreamPoolConfiguration: KinesisVideoStreamPoolConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMediaPipelineKinesisVideoStreamPoolResponseTypeDef(BaseModel):
    KinesisVideoStreamPoolConfiguration: KinesisVideoStreamPoolConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMediaStreamPipelineResponseTypeDef(BaseModel):
    MediaStreamPipeline: MediaStreamPipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class KinesisVideoStreamRecordingSourceRuntimeConfigurationOutputTypeDef(BaseModel):
    Streams: List[RecordingStreamConfigurationTypeDef]
    FragmentSelector: FragmentSelectorOutputTypeDef

class CompositedVideoArtifactsConfigurationTypeDef(BaseModel):
    GridViewConfiguration: GridViewConfigurationTypeDef
    Layout: Optional[Literal["GridView"]] = None
    Resolution: Optional[ResolutionOptionType] = None

class RealTimeAlertConfigurationOutputTypeDef(BaseModel):
    Disabled: Optional[bool] = None
    Rules: Optional[List[RealTimeAlertRuleOutputTypeDef]] = None

class RealTimeAlertConfigurationTypeDef(BaseModel):
    Disabled: Optional[bool] = None
    Rules: Optional[Sequence[RealTimeAlertRuleTypeDef]] = None

class FragmentSelectorTypeDef(BaseModel):
    FragmentSelectorType: FragmentSelectorTypeType
    TimestampRange: TimestampRangeTypeDef

class MediaCapturePipelineSourceConfigurationTypeDef(BaseModel):
    MediaPipelineArn: str
    ChimeSdkMeetingConfiguration: ChimeSdkMeetingConcatenationConfigurationTypeDef

class KinesisVideoStreamSourceRuntimeConfigurationOutputTypeDef(BaseModel):
    Streams: List[StreamConfigurationOutputTypeDef]
    MediaEncoding: Literal["pcm"]
    MediaSampleRate: int

class KinesisVideoStreamSourceRuntimeConfigurationTypeDef(BaseModel):
    Streams: Sequence[StreamConfigurationTypeDef]
    MediaEncoding: Literal["pcm"]
    MediaSampleRate: int

class ArtifactsConfigurationTypeDef(BaseModel):
    Audio: AudioArtifactsConfigurationTypeDef
    Video: VideoArtifactsConfigurationTypeDef
    Content: ContentArtifactsConfigurationTypeDef
    CompositedVideo: Optional[CompositedVideoArtifactsConfigurationTypeDef] = None

class ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef(BaseModel):
    Arn: str
    MuxType: LiveConnectorMuxTypeType
    CompositedVideo: Optional[CompositedVideoArtifactsConfigurationTypeDef] = None
    SourceConfiguration: Optional[SourceConfigurationOutputTypeDef] = None

class ChimeSdkMeetingLiveConnectorConfigurationTypeDef(BaseModel):
    Arn: str
    MuxType: LiveConnectorMuxTypeType
    CompositedVideo: Optional[CompositedVideoArtifactsConfigurationTypeDef] = None
    SourceConfiguration: Optional[SourceConfigurationTypeDef] = None

class MediaInsightsPipelineConfigurationTypeDef(BaseModel):
    MediaInsightsPipelineConfigurationName: Optional[str] = None
    MediaInsightsPipelineConfigurationArn: Optional[str] = None
    ResourceAccessRoleArn: Optional[str] = None
    RealTimeAlertConfiguration: Optional[RealTimeAlertConfigurationOutputTypeDef] = None
    Elements: Optional[List[MediaInsightsPipelineConfigurationElementOutputTypeDef]] = None
    MediaInsightsPipelineConfigurationId: Optional[str] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef(BaseModel):
    Streams: Sequence[RecordingStreamConfigurationTypeDef]
    FragmentSelector: FragmentSelectorTypeDef

class CreateMediaInsightsPipelineConfigurationRequestRequestTypeDef(BaseModel):
    MediaInsightsPipelineConfigurationName: str
    ResourceAccessRoleArn: str
    Elements: Sequence[MediaInsightsPipelineConfigurationElementUnionTypeDef]
    RealTimeAlertConfiguration: Optional[RealTimeAlertConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None

class UpdateMediaInsightsPipelineConfigurationRequestRequestTypeDef(BaseModel):
    Identifier: str
    ResourceAccessRoleArn: str
    Elements: Sequence[MediaInsightsPipelineConfigurationElementUnionTypeDef]
    RealTimeAlertConfiguration: Optional[RealTimeAlertConfigurationTypeDef] = None

class ConcatenationSourceTypeDef(BaseModel):
    Type: Literal["MediaCapturePipeline"]
    MediaCapturePipelineSourceConfiguration: MediaCapturePipelineSourceConfigurationTypeDef

class MediaInsightsPipelineTypeDef(BaseModel):
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

class ChimeSdkMeetingConfigurationOutputTypeDef(BaseModel):
    SourceConfiguration: Optional[SourceConfigurationOutputTypeDef] = None
    ArtifactsConfiguration: Optional[ArtifactsConfigurationTypeDef] = None

class ChimeSdkMeetingConfigurationTypeDef(BaseModel):
    SourceConfiguration: Optional[SourceConfigurationTypeDef] = None
    ArtifactsConfiguration: Optional[ArtifactsConfigurationTypeDef] = None

class LiveConnectorSourceConfigurationOutputTypeDef(BaseModel):
    SourceType: Literal["ChimeSdkMeeting"]
    ChimeSdkMeetingLiveConnectorConfiguration: ChimeSdkMeetingLiveConnectorConfigurationOutputTypeDef

class LiveConnectorSourceConfigurationTypeDef(BaseModel):
    SourceType: Literal["ChimeSdkMeeting"]
    ChimeSdkMeetingLiveConnectorConfiguration: ChimeSdkMeetingLiveConnectorConfigurationTypeDef

class CreateMediaInsightsPipelineConfigurationResponseTypeDef(BaseModel):
    MediaInsightsPipelineConfiguration: MediaInsightsPipelineConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMediaInsightsPipelineConfigurationResponseTypeDef(BaseModel):
    MediaInsightsPipelineConfiguration: MediaInsightsPipelineConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMediaInsightsPipelineConfigurationResponseTypeDef(BaseModel):
    MediaInsightsPipelineConfiguration: MediaInsightsPipelineConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMediaInsightsPipelineRequestRequestTypeDef(BaseModel):
    MediaInsightsPipelineConfigurationArn: str
    KinesisVideoStreamSourceRuntimeConfiguration: Optional[       KinesisVideoStreamSourceRuntimeConfigurationTypeDef     ] = None
    MediaInsightsRuntimeMetadata: Optional[Mapping[str, str]] = None
    KinesisVideoStreamRecordingSourceRuntimeConfiguration: Optional[       KinesisVideoStreamRecordingSourceRuntimeConfigurationTypeDef     ] = None
    S3RecordingSinkRuntimeConfiguration: Optional[       S3RecordingSinkRuntimeConfigurationTypeDef     ] = None
    Tags: Optional[Sequence[TagTypeDef]] = None
    ClientRequestToken: Optional[str] = None

class CreateMediaConcatenationPipelineRequestRequestTypeDef(BaseModel):
    Sources: Sequence[ConcatenationSourceTypeDef]
    Sinks: Sequence[ConcatenationSinkTypeDef]
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class MediaConcatenationPipelineTypeDef(BaseModel):
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None
    Sources: Optional[List[ConcatenationSourceTypeDef]] = None
    Sinks: Optional[List[ConcatenationSinkTypeDef]] = None
    Status: Optional[MediaPipelineStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class CreateMediaInsightsPipelineResponseTypeDef(BaseModel):
    MediaInsightsPipeline: MediaInsightsPipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MediaCapturePipelineTypeDef(BaseModel):
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

class CreateMediaCapturePipelineRequestRequestTypeDef(BaseModel):
    SourceType: Literal["ChimeSdkMeeting"]
    SourceArn: str
    SinkType: Literal["S3Bucket"]
    SinkArn: str
    ClientRequestToken: Optional[str] = None
    ChimeSdkMeetingConfiguration: Optional[ChimeSdkMeetingConfigurationTypeDef] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class MediaLiveConnectorPipelineTypeDef(BaseModel):
    Sources: Optional[List[LiveConnectorSourceConfigurationOutputTypeDef]] = None
    Sinks: Optional[List[LiveConnectorSinkConfigurationTypeDef]] = None
    MediaPipelineId: Optional[str] = None
    MediaPipelineArn: Optional[str] = None
    Status: Optional[MediaPipelineStatusType] = None
    CreatedTimestamp: Optional[datetime] = None
    UpdatedTimestamp: Optional[datetime] = None

class CreateMediaConcatenationPipelineResponseTypeDef(BaseModel):
    MediaConcatenationPipeline: MediaConcatenationPipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMediaCapturePipelineResponseTypeDef(BaseModel):
    MediaCapturePipeline: MediaCapturePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetMediaCapturePipelineResponseTypeDef(BaseModel):
    MediaCapturePipeline: MediaCapturePipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateMediaLiveConnectorPipelineResponseTypeDef(BaseModel):
    MediaLiveConnectorPipeline: MediaLiveConnectorPipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class MediaPipelineTypeDef(BaseModel):
    MediaCapturePipeline: Optional[MediaCapturePipelineTypeDef] = None
    MediaLiveConnectorPipeline: Optional[MediaLiveConnectorPipelineTypeDef] = None
    MediaConcatenationPipeline: Optional[MediaConcatenationPipelineTypeDef] = None
    MediaInsightsPipeline: Optional[MediaInsightsPipelineTypeDef] = None
    MediaStreamPipeline: Optional[MediaStreamPipelineTypeDef] = None

class CreateMediaLiveConnectorPipelineRequestRequestTypeDef(BaseModel):
    Sources: Sequence[LiveConnectorSourceConfigurationUnionTypeDef]
    Sinks: Sequence[LiveConnectorSinkConfigurationTypeDef]
    ClientRequestToken: Optional[str] = None
    Tags: Optional[Sequence[TagTypeDef]] = None

class GetMediaPipelineResponseTypeDef(BaseModel):
    MediaPipeline: MediaPipelineTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

