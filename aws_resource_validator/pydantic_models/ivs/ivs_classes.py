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


# This class is the input for the 'batch_get_channel' function.
class BatchGetChannelRequest(BaseValidatorModel):
    arns: List[str]


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


# This class is the input for the 'batch_get_stream_key' function.
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


# This class is the input for the 'create_playback_restriction_policy' function.
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


# This class is the input for the 'create_stream_key' function.
class CreateStreamKeyRequest(BaseValidatorModel):
    channelArn: str
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'delete_channel' function.
class DeleteChannelRequest(BaseValidatorModel):
    arn: str


class DeletePlaybackKeyPairRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'delete_playback_restriction_policy' function.
class DeletePlaybackRestrictionPolicyRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'delete_recording_configuration' function.
class DeleteRecordingConfigurationRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'delete_stream_key' function.
class DeleteStreamKeyRequest(BaseValidatorModel):
    arn: str


class S3DestinationConfiguration(BaseValidatorModel):
    bucketName: str


# This class is the input for the 'get_channel' function.
class GetChannelRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_playback_key_pair' function.
class GetPlaybackKeyPairRequest(BaseValidatorModel):
    arn: str


class PlaybackKeyPair(BaseValidatorModel):
    arn: Optional[str] = None
    fingerprint: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'get_playback_restriction_policy' function.
class GetPlaybackRestrictionPolicyRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_recording_configuration' function.
class GetRecordingConfigurationRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_stream_key' function.
class GetStreamKeyRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_stream' function.
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


# This class is the input for the 'get_stream_session' function.
class GetStreamSessionRequest(BaseValidatorModel):
    channelArn: str
    streamId: Optional[str] = None


# This class is the input for the 'import_playback_key_pair' function.
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


# This class is the input for the 'list_channels' function.
class ListChannelsRequest(BaseValidatorModel):
    filterByName: Optional[str] = None
    filterByPlaybackRestrictionPolicyArn: Optional[str] = None
    filterByRecordingConfigurationArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_playback_key_pairs' function.
class ListPlaybackKeyPairsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PlaybackKeyPairSummary(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'list_playback_restriction_policies' function.
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


# This class is the input for the 'list_recording_configurations' function.
class ListRecordingConfigurationsRequest(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the input for the 'list_stream_keys' function.
class ListStreamKeysRequest(BaseValidatorModel):
    channelArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class StreamKeySummary(BaseValidatorModel):
    arn: Optional[str] = None
    channelArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'list_stream_sessions' function.
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


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


# This class is the input for the 'put_metadata' function.
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


# This class is the input for the 'update_playback_restriction_policy' function.
class UpdatePlaybackRestrictionPolicyRequest(BaseValidatorModel):
    arn: str
    allowedCountries: Optional[List[str]] = None
    allowedOrigins: Optional[List[str]] = None
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None


# This class is the output for the 'put_metadata' function.
class EmptyResponseMetadata(BaseValidatorModel):
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_get_stream_key' function.
class BatchGetStreamKeyResponse(BaseValidatorModel):
    errors: List[BatchError]
    streamKeys: List[StreamKey]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_stream_key' function.
class CreateStreamKeyResponse(BaseValidatorModel):
    streamKey: StreamKey
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_stream_key' function.
class GetStreamKeyResponse(BaseValidatorModel):
    streamKey: StreamKey
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'batch_start_viewer_session_revocation' function.
class BatchStartViewerSessionRevocationResponse(BaseValidatorModel):
    errors: List[BatchStartViewerSessionRevocationError]
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'batch_start_viewer_session_revocation' function.
class BatchStartViewerSessionRevocationRequest(BaseValidatorModel):
    viewerSessions: List[BatchStartViewerSessionRevocationViewerSession]


# This class is the output for the 'list_channels' function.
class ListChannelsResponse(BaseValidatorModel):
    channels: List[ChannelSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the input for the 'create_channel' function.
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


# This class is the input for the 'update_channel' function.
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


# This class is the output for the 'create_playback_restriction_policy' function.
class CreatePlaybackRestrictionPolicyResponse(BaseValidatorModel):
    playbackRestrictionPolicy: PlaybackRestrictionPolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_playback_restriction_policy' function.
class GetPlaybackRestrictionPolicyResponse(BaseValidatorModel):
    playbackRestrictionPolicy: PlaybackRestrictionPolicy
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_playback_restriction_policy' function.
class UpdatePlaybackRestrictionPolicyResponse(BaseValidatorModel):
    playbackRestrictionPolicy: PlaybackRestrictionPolicy
    ResponseMetadata: ResponseMetadata


class DestinationConfiguration(BaseValidatorModel):
    s3: Optional[S3DestinationConfiguration] = None


# This class is the output for the 'get_playback_key_pair' function.
class GetPlaybackKeyPairResponse(BaseValidatorModel):
    keyPair: PlaybackKeyPair
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_playback_key_pair' function.
class ImportPlaybackKeyPairResponse(BaseValidatorModel):
    keyPair: PlaybackKeyPair
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_stream' function.
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


# This class is the output for the 'list_playback_key_pairs' function.
class ListPlaybackKeyPairsResponse(BaseValidatorModel):
    keyPairs: List[PlaybackKeyPairSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_playback_restriction_policies' function.
class ListPlaybackRestrictionPoliciesResponse(BaseValidatorModel):
    playbackRestrictionPolicies: List[PlaybackRestrictionPolicySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_stream_keys' function.
class ListStreamKeysResponse(BaseValidatorModel):
    streamKeys: List[StreamKeySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_stream_sessions' function.
class ListStreamSessionsResponse(BaseValidatorModel):
    streamSessions: List[StreamSessionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListStreamsRequestPaginate(BaseValidatorModel):
    filterBy: Optional[StreamFilters] = None
    PaginationConfig: Optional[PaginatorConfig] = None


# This class is the input for the 'list_streams' function.
class ListStreamsRequest(BaseValidatorModel):
    filterBy: Optional[StreamFilters] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


# This class is the output for the 'list_streams' function.
class ListStreamsResponse(BaseValidatorModel):
    streams: List[StreamSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None

RenditionConfigurationUnion = Union[RenditionConfiguration, RenditionConfigurationOutput]

ThumbnailConfigurationUnion = Union[ThumbnailConfiguration, ThumbnailConfigurationOutput]


# This class is the output for the 'batch_get_channel' function.
class BatchGetChannelResponse(BaseValidatorModel):
    channels: List[Channel]
    errors: List[BatchError]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_channel' function.
class CreateChannelResponse(BaseValidatorModel):
    channel: Channel
    streamKey: StreamKey
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_channel' function.
class GetChannelResponse(BaseValidatorModel):
    channel: Channel
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_channel' function.
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


# This class is the input for the 'create_recording_configuration' function.
class CreateRecordingConfigurationRequest(BaseValidatorModel):
    destinationConfiguration: DestinationConfiguration
    name: Optional[str] = None
    recordingReconnectWindowSeconds: Optional[int] = None
    renditionConfiguration: Optional[RenditionConfigurationUnion] = None
    tags: Optional[Dict[str, str]] = None
    thumbnailConfiguration: Optional[ThumbnailConfigurationUnion] = None


# This class is the output for the 'list_recording_configurations' function.
class ListRecordingConfigurationsResponse(BaseValidatorModel):
    recordingConfigurations: List[RecordingConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_recording_configuration' function.
class CreateRecordingConfigurationResponse(BaseValidatorModel):
    recordingConfiguration: RecordingConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_recording_configuration' function.
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


# This class is the output for the 'get_stream_session' function.
class GetStreamSessionResponse(BaseValidatorModel):
    streamSession: StreamSession
    ResponseMetadata: ResponseMetadata