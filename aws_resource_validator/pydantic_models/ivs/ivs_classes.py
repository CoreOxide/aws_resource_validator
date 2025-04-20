from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ivs.ivs_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class AudioConfiguration(BaseValidatorModel):
    channels: Optional[int] = None
    codec: Optional[str] = None
    sampleRate: Optional[int] = None
    targetBitrate: Optional[int] = None
    track: Optional[str] = None


class BatchError(BaseValidatorModel):
    arn: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None


class BatchGetChannelRequest(BaseValidatorModel):
    arns: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetStreamKeyRequest(BaseValidatorModel):
    arns: List[str]


class StreamKey(BaseValidatorModel):
    arn: Optional[str] = None
    channelArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    value: Optional[str] = None


class BatchStartViewerSessionRevocationError(BaseValidatorModel):
    channelArn: str
    viewerId: str
    code: Optional[str] = None
    message: Optional[str] = None


class BatchStartViewerSessionRevocationViewerSession(BaseValidatorModel):
    channelArn: str
    viewerId: str
    viewerSessionVersionsLessThanOrEqualTo: Optional[int] = None


class ChannelSummary(BaseValidatorModel):
    arn: Optional[str] = None
    authorized: Optional[bool] = None
    insecureIngest: Optional[bool] = None
    latencyMode: Optional[ChannelLatencyModeType] = None
    name: Optional[str] = None
    playbackRestrictionPolicyArn: Optional[str] = None
    preset: Optional[TranscodePresetType] = None
    recordingConfigurationArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[ChannelTypeType] = None


class MultitrackInputConfiguration(BaseValidatorModel):
    enabled: Optional[bool] = None
    maximumResolution: Optional[MultitrackMaximumResolutionType] = None
    policy: Optional[MultitrackPolicyType] = None


class Srt(BaseValidatorModel):
    endpoint: Optional[str] = None
    passphrase: Optional[str] = None


class CreatePlaybackRestrictionPolicyRequest(BaseValidatorModel):
    allowedCountries: Optional[List[str]] = None
    allowedOrigins: Optional[List[str]] = None
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class PlaybackRestrictionPolicy(BaseValidatorModel):
    allowedCountries: List[str]
    allowedOrigins: List[str]
    arn: str
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class CreateStreamKeyRequest(BaseValidatorModel):
    channelArn: str
    tags: Optional[Dict[str, str]] = None


class DeleteChannelRequest(BaseValidatorModel):
    arn: str


class DeletePlaybackKeyPairRequest(BaseValidatorModel):
    arn: str


class DeletePlaybackRestrictionPolicyRequest(BaseValidatorModel):
    arn: str


class DeleteRecordingConfigurationRequest(BaseValidatorModel):
    arn: str


class DeleteStreamKeyRequest(BaseValidatorModel):
    arn: str


class S3DestinationConfiguration(BaseValidatorModel):
    bucketName: str


class GetChannelRequest(BaseValidatorModel):
    arn: str


class GetPlaybackKeyPairRequest(BaseValidatorModel):
    arn: str


class PlaybackKeyPair(BaseValidatorModel):
    arn: Optional[str] = None
    fingerprint: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class GetPlaybackRestrictionPolicyRequest(BaseValidatorModel):
    arn: str


class GetRecordingConfigurationRequest(BaseValidatorModel):
    arn: str


class GetStreamKeyRequest(BaseValidatorModel):
    arn: str


class GetStreamRequest(BaseValidatorModel):
    channelArn: str


class Stream(BaseValidatorModel):
    channelArn: Optional[str] = None
    health: Optional[StreamHealthType] = None
    playbackUrl: Optional[str] = None
    startTime: Optional[datetime] = None
    state: Optional[StreamStateType] = None
    streamId: Optional[str] = None
    viewerCount: Optional[int] = None


class GetStreamSessionRequest(BaseValidatorModel):
    channelArn: str
    streamId: Optional[str] = None


class ImportPlaybackKeyPairRequest(BaseValidatorModel):
    publicKeyMaterial: str
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class VideoConfiguration(BaseValidatorModel):
    avcLevel: Optional[str] = None
    avcProfile: Optional[str] = None
    codec: Optional[str] = None
    encoder: Optional[str] = None
    level: Optional[str] = None
    profile: Optional[str] = None
    targetBitrate: Optional[int] = None
    targetFramerate: Optional[int] = None
    track: Optional[str] = None
    videoHeight: Optional[int] = None
    videoWidth: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListChannelsRequest(BaseValidatorModel):
    filterByName: Optional[str] = None
    filterByPlaybackRestrictionPolicyArn: Optional[str] = None
    filterByRecordingConfigurationArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListPlaybackKeyPairsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PlaybackKeyPairSummary(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListPlaybackRestrictionPoliciesRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PlaybackRestrictionPolicySummary(BaseValidatorModel):
    allowedCountries: List[str]
    allowedOrigins: List[str]
    arn: str
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListRecordingConfigurationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListStreamKeysRequest(BaseValidatorModel):
    channelArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class StreamKeySummary(BaseValidatorModel):
    arn: Optional[str] = None
    channelArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListStreamSessionsRequest(BaseValidatorModel):
    channelArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class StreamSessionSummary(BaseValidatorModel):
    endTime: Optional[datetime] = None
    hasErrorEvent: Optional[bool] = None
    startTime: Optional[datetime] = None
    streamId: Optional[str] = None


class StreamFilters(BaseValidatorModel):
    health: Optional[StreamHealthType] = None


class StreamSummary(BaseValidatorModel):
    channelArn: Optional[str] = None
    health: Optional[StreamHealthType] = None
    startTime: Optional[datetime] = None
    state: Optional[StreamStateType] = None
    streamId: Optional[str] = None
    viewerCount: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class PutMetadataRequest(BaseValidatorModel):
    channelArn: str
    metadata: str


class RenditionConfigurationOutput(BaseValidatorModel):
    renditionSelection: Optional[RenditionConfigurationRenditionSelectionType] = None
    renditions: Optional[List[RenditionConfigurationRenditionType]] = None


class ThumbnailConfigurationOutput(BaseValidatorModel):
    recordingMode: Optional[RecordingModeType] = None
    resolution: Optional[ThumbnailConfigurationResolutionType] = None
    storage: Optional[List[ThumbnailConfigurationStorageType]] = None
    targetIntervalSeconds: Optional[int] = None


class RenditionConfiguration(BaseValidatorModel):
    renditionSelection: Optional[RenditionConfigurationRenditionSelectionType] = None
    renditions: Optional[List[RenditionConfigurationRenditionType]] = None


class StartViewerSessionRevocationRequest(BaseValidatorModel):
    channelArn: str
    viewerId: str
    viewerSessionVersionsLessThanOrEqualTo: Optional[int] = None


class StopStreamRequest(BaseValidatorModel):
    channelArn: str


class StreamEvent(BaseValidatorModel):
    code: Optional[str] = None
    eventTime: Optional[datetime] = None
    name: Optional[str] = None
    type: Optional[str] = None


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class ThumbnailConfiguration(BaseValidatorModel):
    recordingMode: Optional[RecordingModeType] = None
    resolution: Optional[ThumbnailConfigurationResolutionType] = None
    storage: Optional[List[ThumbnailConfigurationStorageType]] = None
    targetIntervalSeconds: Optional[int] = None


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


class UpdatePlaybackRestrictionPolicyRequest(BaseValidatorModel):
    arn: str
    allowedCountries: Optional[List[str]] = None
    allowedOrigins: Optional[List[str]] = None
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None


class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class BatchGetStreamKeyResponse(BaseValidatorModel):
    errors: List[BatchError]
    streamKeys: List[StreamKey]
    ResponseMetadata: ResponseMetadata


class CreateStreamKeyResponse(BaseValidatorModel):
    streamKey: StreamKey
    ResponseMetadata: ResponseMetadata


class GetStreamKeyResponse(BaseValidatorModel):
    streamKey: StreamKey
    ResponseMetadata: ResponseMetadata


class BatchStartViewerSessionRevocationResponse(BaseValidatorModel):
    errors: List[BatchStartViewerSessionRevocationError]
    ResponseMetadata: ResponseMetadata


class BatchStartViewerSessionRevocationRequest(BaseValidatorModel):
    viewerSessions: List[BatchStartViewerSessionRevocationViewerSession]


class ListChannelsResponse(BaseValidatorModel):
    channels: List[ChannelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateChannelRequest(BaseValidatorModel):
    authorized: Optional[bool] = None
    containerFormat: Optional[ContainerFormatType] = None
    insecureIngest: Optional[bool] = None
    latencyMode: Optional[ChannelLatencyModeType] = None
    multitrackInputConfiguration: Optional[MultitrackInputConfiguration] = None
    name: Optional[str] = None
    playbackRestrictionPolicyArn: Optional[str] = None
    preset: Optional[TranscodePresetType] = None
    recordingConfigurationArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[ChannelTypeType] = None


class UpdateChannelRequest(BaseValidatorModel):
    arn: str
    authorized: Optional[bool] = None
    containerFormat: Optional[ContainerFormatType] = None
    insecureIngest: Optional[bool] = None
    latencyMode: Optional[ChannelLatencyModeType] = None
    multitrackInputConfiguration: Optional[MultitrackInputConfiguration] = None
    name: Optional[str] = None
    playbackRestrictionPolicyArn: Optional[str] = None
    preset: Optional[TranscodePresetType] = None
    recordingConfigurationArn: Optional[str] = None
    type: Optional[ChannelTypeType] = None


class Channel(BaseValidatorModel):
    arn: Optional[str] = None
    authorized: Optional[bool] = None
    containerFormat: Optional[ContainerFormatType] = None
    ingestEndpoint: Optional[str] = None
    insecureIngest: Optional[bool] = None
    latencyMode: Optional[ChannelLatencyModeType] = None
    multitrackInputConfiguration: Optional[MultitrackInputConfiguration] = None
    name: Optional[str] = None
    playbackRestrictionPolicyArn: Optional[str] = None
    playbackUrl: Optional[str] = None
    preset: Optional[TranscodePresetType] = None
    recordingConfigurationArn: Optional[str] = None
    srt: Optional[Srt] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[ChannelTypeType] = None


class CreatePlaybackRestrictionPolicyResponse(BaseValidatorModel):
    playbackRestrictionPolicy: PlaybackRestrictionPolicy
    ResponseMetadata: ResponseMetadata


class GetPlaybackRestrictionPolicyResponse(BaseValidatorModel):
    playbackRestrictionPolicy: PlaybackRestrictionPolicy
    ResponseMetadata: ResponseMetadata


class UpdatePlaybackRestrictionPolicyResponse(BaseValidatorModel):
    playbackRestrictionPolicy: PlaybackRestrictionPolicy
    ResponseMetadata: ResponseMetadata


class DestinationConfiguration(BaseValidatorModel):
    s3: Optional[S3DestinationConfiguration] = None


class GetPlaybackKeyPairResponse(BaseValidatorModel):
    keyPair: PlaybackKeyPair
    ResponseMetadata: ResponseMetadata


class ImportPlaybackKeyPairResponse(BaseValidatorModel):
    keyPair: PlaybackKeyPair
    ResponseMetadata: ResponseMetadata


class GetStreamResponse(BaseValidatorModel):
    stream: Stream
    ResponseMetadata: ResponseMetadata


class IngestConfiguration(BaseValidatorModel):
    audio: Optional[AudioConfiguration] = None
    video: Optional[VideoConfiguration] = None


class IngestConfigurations(BaseValidatorModel):
    audioConfigurations: List[AudioConfiguration]
    videoConfigurations: List[VideoConfiguration]


class ListChannelsRequestPaginate(BaseValidatorModel):
    filterByName: Optional[str] = None
    filterByPlaybackRestrictionPolicyArn: Optional[str] = None
    filterByRecordingConfigurationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPlaybackKeyPairsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListRecordingConfigurationsRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStreamKeysRequestPaginate(BaseValidatorModel):
    channelArn: str
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPlaybackKeyPairsResponse(BaseValidatorModel):
    keyPairs: List[PlaybackKeyPairSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListPlaybackRestrictionPoliciesResponse(BaseValidatorModel):
    playbackRestrictionPolicies: List[PlaybackRestrictionPolicySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListStreamKeysResponse(BaseValidatorModel):
    streamKeys: List[StreamKeySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListStreamSessionsResponse(BaseValidatorModel):
    streamSessions: List[StreamSessionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListStreamsRequestPaginate(BaseValidatorModel):
    filterBy: Optional[StreamFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListStreamsRequest(BaseValidatorModel):
    filterBy: Optional[StreamFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListStreamsResponse(BaseValidatorModel):
    streams: List[StreamSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

RenditionConfigurationUnion = Union[RenditionConfiguration, RenditionConfigurationOutput]

ThumbnailConfigurationUnion = Union[ThumbnailConfiguration, ThumbnailConfigurationOutput]


class BatchGetChannelResponse(BaseValidatorModel):
    channels: List[Channel]
    errors: List[BatchError]
    ResponseMetadata: ResponseMetadata


class CreateChannelResponse(BaseValidatorModel):
    channel: Channel
    streamKey: StreamKey
    ResponseMetadata: ResponseMetadata


class GetChannelResponse(BaseValidatorModel):
    channel: Channel
    ResponseMetadata: ResponseMetadata


class UpdateChannelResponse(BaseValidatorModel):
    channel: Channel
    ResponseMetadata: ResponseMetadata


class RecordingConfigurationSummary(BaseValidatorModel):
    arn: str
    destinationConfiguration: DestinationConfiguration
    state: RecordingConfigurationStateType
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class RecordingConfiguration(BaseValidatorModel):
    arn: str
    destinationConfiguration: DestinationConfiguration
    state: RecordingConfigurationStateType
    name: Optional[str] = None
    recordingReconnectWindowSeconds: Optional[int] = None
    renditionConfiguration: Optional[RenditionConfigurationOutput] = None
    tags: Optional[Dict[str, str]] = None
    thumbnailConfiguration: Optional[ThumbnailConfigurationOutput] = None


class CreateRecordingConfigurationRequest(BaseValidatorModel):
    destinationConfiguration: DestinationConfiguration
    name: Optional[str] = None
    recordingReconnectWindowSeconds: Optional[int] = None
    renditionConfiguration: Optional[RenditionConfigurationUnion] = None
    tags: Optional[Dict[str, str]] = None
    thumbnailConfiguration: Optional[ThumbnailConfigurationUnion] = None


class ListRecordingConfigurationsResponse(BaseValidatorModel):
    recordingConfigurations: List[RecordingConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateRecordingConfigurationResponse(BaseValidatorModel):
    recordingConfiguration: RecordingConfiguration
    ResponseMetadata: ResponseMetadata


class GetRecordingConfigurationResponse(BaseValidatorModel):
    recordingConfiguration: RecordingConfiguration
    ResponseMetadata: ResponseMetadata


class StreamSession(BaseValidatorModel):
    channel: Optional[Channel] = None
    endTime: Optional[datetime] = None
    ingestConfiguration: Optional[IngestConfiguration] = None
    ingestConfigurations: Optional[IngestConfigurations] = None
    recordingConfiguration: Optional[RecordingConfiguration] = None
    startTime: Optional[datetime] = None
    streamId: Optional[str] = None
    truncatedEvents: Optional[List[StreamEvent]] = None


class GetStreamSessionResponse(BaseValidatorModel):
    streamSession: StreamSession
    ResponseMetadata: ResponseMetadata