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
from aws_resource_validator.pydantic_models.ivs_constants import *

class AudioConfigurationTypeDef(BaseModel):
    channels: Optional[int] = None
    codec: Optional[str] = None
    sampleRate: Optional[int] = None
    targetBitrate: Optional[int] = None

class BatchErrorTypeDef(BaseModel):
    arn: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None

class BatchGetChannelRequestRequestTypeDef(BaseModel):
    arns: Sequence[str]

class ResponseMetadataTypeDef(BaseModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchGetStreamKeyRequestRequestTypeDef(BaseModel):
    arns: Sequence[str]

class StreamKeyTypeDef(BaseModel):
    arn: Optional[str] = None
    channelArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    value: Optional[str] = None

class BatchStartViewerSessionRevocationErrorTypeDef(BaseModel):
    channelArn: str
    viewerId: str
    code: Optional[str] = None
    message: Optional[str] = None

class BatchStartViewerSessionRevocationViewerSessionTypeDef(BaseModel):
    channelArn: str
    viewerId: str
    viewerSessionVersionsLessThanOrEqualTo: Optional[int] = None

class ChannelSummaryTypeDef(BaseModel):
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

class SrtTypeDef(BaseModel):
    endpoint: Optional[str] = None
    passphrase: Optional[str] = None

class CreateChannelRequestRequestTypeDef(BaseModel):
    authorized: Optional[bool] = None
    insecureIngest: Optional[bool] = None
    latencyMode: Optional[ChannelLatencyModeType] = None
    name: Optional[str] = None
    playbackRestrictionPolicyArn: Optional[str] = None
    preset: Optional[TranscodePresetType] = None
    recordingConfigurationArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    type: Optional[ChannelTypeType] = None

class CreatePlaybackRestrictionPolicyRequestRequestTypeDef(BaseModel):
    allowedCountries: Optional[Sequence[str]] = None
    allowedOrigins: Optional[Sequence[str]] = None
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class PlaybackRestrictionPolicyTypeDef(BaseModel):
    allowedCountries: List[str]
    allowedOrigins: List[str]
    arn: str
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class RenditionConfigurationTypeDef(BaseModel):
    renditionSelection: Optional[RenditionConfigurationRenditionSelectionType] = None
    renditions: Optional[Sequence[RenditionConfigurationRenditionType]] = None

class ThumbnailConfigurationTypeDef(BaseModel):
    recordingMode: Optional[RecordingModeType] = None
    resolution: Optional[ThumbnailConfigurationResolutionType] = None
    storage: Optional[Sequence[ThumbnailConfigurationStorageType]] = None
    targetIntervalSeconds: Optional[int] = None

class CreateStreamKeyRequestRequestTypeDef(BaseModel):
    channelArn: str
    tags: Optional[Mapping[str, str]] = None

class DeleteChannelRequestRequestTypeDef(BaseModel):
    arn: str

class DeletePlaybackKeyPairRequestRequestTypeDef(BaseModel):
    arn: str

class DeletePlaybackRestrictionPolicyRequestRequestTypeDef(BaseModel):
    arn: str

class DeleteRecordingConfigurationRequestRequestTypeDef(BaseModel):
    arn: str

class DeleteStreamKeyRequestRequestTypeDef(BaseModel):
    arn: str

class S3DestinationConfigurationTypeDef(BaseModel):
    bucketName: str

class GetChannelRequestRequestTypeDef(BaseModel):
    arn: str

class GetPlaybackKeyPairRequestRequestTypeDef(BaseModel):
    arn: str

class PlaybackKeyPairTypeDef(BaseModel):
    arn: Optional[str] = None
    fingerprint: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class GetPlaybackRestrictionPolicyRequestRequestTypeDef(BaseModel):
    arn: str

class GetRecordingConfigurationRequestRequestTypeDef(BaseModel):
    arn: str

class GetStreamKeyRequestRequestTypeDef(BaseModel):
    arn: str

class GetStreamRequestRequestTypeDef(BaseModel):
    channelArn: str

class StreamTypeDef(BaseModel):
    channelArn: Optional[str] = None
    health: Optional[StreamHealthType] = None
    playbackUrl: Optional[str] = None
    startTime: Optional[datetime] = None
    state: Optional[StreamStateType] = None
    streamId: Optional[str] = None
    viewerCount: Optional[int] = None

class GetStreamSessionRequestRequestTypeDef(BaseModel):
    channelArn: str
    streamId: Optional[str] = None

class ImportPlaybackKeyPairRequestRequestTypeDef(BaseModel):
    publicKeyMaterial: str
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class VideoConfigurationTypeDef(BaseModel):
    avcLevel: Optional[str] = None
    avcProfile: Optional[str] = None
    codec: Optional[str] = None
    encoder: Optional[str] = None
    targetBitrate: Optional[int] = None
    targetFramerate: Optional[int] = None
    videoHeight: Optional[int] = None
    videoWidth: Optional[int] = None

class PaginatorConfigTypeDef(BaseModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseModel):
    filterByName: Optional[str] = None
    filterByPlaybackRestrictionPolicyArn: Optional[str] = None
    filterByRecordingConfigurationArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListPlaybackKeyPairsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PlaybackKeyPairSummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListPlaybackRestrictionPoliciesRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PlaybackRestrictionPolicySummaryTypeDef(BaseModel):
    allowedCountries: List[str]
    allowedOrigins: List[str]
    arn: str
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListRecordingConfigurationsRequestRequestTypeDef(BaseModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListStreamKeysRequestRequestTypeDef(BaseModel):
    channelArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StreamKeySummaryTypeDef(BaseModel):
    arn: Optional[str] = None
    channelArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListStreamSessionsRequestRequestTypeDef(BaseModel):
    channelArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StreamSessionSummaryTypeDef(BaseModel):
    endTime: Optional[datetime] = None
    hasErrorEvent: Optional[bool] = None
    startTime: Optional[datetime] = None
    streamId: Optional[str] = None

class StreamFiltersTypeDef(BaseModel):
    health: Optional[StreamHealthType] = None

class StreamSummaryTypeDef(BaseModel):
    channelArn: Optional[str] = None
    health: Optional[StreamHealthType] = None
    startTime: Optional[datetime] = None
    state: Optional[StreamStateType] = None
    streamId: Optional[str] = None
    viewerCount: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str

class PutMetadataRequestRequestTypeDef(BaseModel):
    channelArn: str
    metadata: str

class RenditionConfigurationOutputTypeDef(BaseModel):
    renditionSelection: Optional[RenditionConfigurationRenditionSelectionType] = None
    renditions: Optional[List[RenditionConfigurationRenditionType]] = None

class ThumbnailConfigurationOutputTypeDef(BaseModel):
    recordingMode: Optional[RecordingModeType] = None
    resolution: Optional[ThumbnailConfigurationResolutionType] = None
    storage: Optional[List[ThumbnailConfigurationStorageType]] = None
    targetIntervalSeconds: Optional[int] = None

class StartViewerSessionRevocationRequestRequestTypeDef(BaseModel):
    channelArn: str
    viewerId: str
    viewerSessionVersionsLessThanOrEqualTo: Optional[int] = None

class StopStreamRequestRequestTypeDef(BaseModel):
    channelArn: str

class StreamEventTypeDef(BaseModel):
    eventTime: Optional[datetime] = None
    name: Optional[str] = None
    type: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateChannelRequestRequestTypeDef(BaseModel):
    arn: str
    authorized: Optional[bool] = None
    insecureIngest: Optional[bool] = None
    latencyMode: Optional[ChannelLatencyModeType] = None
    name: Optional[str] = None
    playbackRestrictionPolicyArn: Optional[str] = None
    preset: Optional[TranscodePresetType] = None
    recordingConfigurationArn: Optional[str] = None
    type: Optional[ChannelTypeType] = None

class UpdatePlaybackRestrictionPolicyRequestRequestTypeDef(BaseModel):
    arn: str
    allowedCountries: Optional[Sequence[str]] = None
    allowedOrigins: Optional[Sequence[str]] = None
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None

class EmptyResponseMetadataTypeDef(BaseModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetStreamKeyResponseTypeDef(BaseModel):
    errors: List[BatchErrorTypeDef]
    streamKeys: List[StreamKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamKeyResponseTypeDef(BaseModel):
    streamKey: StreamKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamKeyResponseTypeDef(BaseModel):
    streamKey: StreamKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchStartViewerSessionRevocationResponseTypeDef(BaseModel):
    errors: List[BatchStartViewerSessionRevocationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchStartViewerSessionRevocationRequestRequestTypeDef(BaseModel):
    viewerSessions: Sequence[BatchStartViewerSessionRevocationViewerSessionTypeDef]

class ListChannelsResponseTypeDef(BaseModel):
    channels: List[ChannelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelTypeDef(BaseModel):
    arn: Optional[str] = None
    authorized: Optional[bool] = None
    ingestEndpoint: Optional[str] = None
    insecureIngest: Optional[bool] = None
    latencyMode: Optional[ChannelLatencyModeType] = None
    name: Optional[str] = None
    playbackRestrictionPolicyArn: Optional[str] = None
    playbackUrl: Optional[str] = None
    preset: Optional[TranscodePresetType] = None
    recordingConfigurationArn: Optional[str] = None
    srt: Optional[SrtTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    type: Optional[ChannelTypeType] = None

class CreatePlaybackRestrictionPolicyResponseTypeDef(BaseModel):
    playbackRestrictionPolicy: PlaybackRestrictionPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPlaybackRestrictionPolicyResponseTypeDef(BaseModel):
    playbackRestrictionPolicy: PlaybackRestrictionPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePlaybackRestrictionPolicyResponseTypeDef(BaseModel):
    playbackRestrictionPolicy: PlaybackRestrictionPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationConfigurationTypeDef(BaseModel):
    s3: Optional[S3DestinationConfigurationTypeDef] = None

class GetPlaybackKeyPairResponseTypeDef(BaseModel):
    keyPair: PlaybackKeyPairTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportPlaybackKeyPairResponseTypeDef(BaseModel):
    keyPair: PlaybackKeyPairTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamResponseTypeDef(BaseModel):
    stream: StreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IngestConfigurationTypeDef(BaseModel):
    audio: Optional[AudioConfigurationTypeDef] = None
    video: Optional[VideoConfigurationTypeDef] = None

class ListChannelsRequestListChannelsPaginateTypeDef(BaseModel):
    filterByName: Optional[str] = None
    filterByPlaybackRestrictionPolicyArn: Optional[str] = None
    filterByRecordingConfigurationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPlaybackKeyPairsRequestListPlaybackKeyPairsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecordingConfigurationsRequestListRecordingConfigurationsPaginateTypeDef(BaseModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamKeysRequestListStreamKeysPaginateTypeDef(BaseModel):
    channelArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPlaybackKeyPairsResponseTypeDef(BaseModel):
    keyPairs: List[PlaybackKeyPairSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPlaybackRestrictionPoliciesResponseTypeDef(BaseModel):
    nextToken: str
    playbackRestrictionPolicies: List[PlaybackRestrictionPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamKeysResponseTypeDef(BaseModel):
    nextToken: str
    streamKeys: List[StreamKeySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamSessionsResponseTypeDef(BaseModel):
    nextToken: str
    streamSessions: List[StreamSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamsRequestListStreamsPaginateTypeDef(BaseModel):
    filterBy: Optional[StreamFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamsRequestRequestTypeDef(BaseModel):
    filterBy: Optional[StreamFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListStreamsResponseTypeDef(BaseModel):
    nextToken: str
    streams: List[StreamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetChannelResponseTypeDef(BaseModel):
    channels: List[ChannelTypeDef]
    errors: List[BatchErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelResponseTypeDef(BaseModel):
    channel: ChannelTypeDef
    streamKey: StreamKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelResponseTypeDef(BaseModel):
    channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(BaseModel):
    channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecordingConfigurationRequestRequestTypeDef(BaseModel):
    destinationConfiguration: DestinationConfigurationTypeDef
    name: Optional[str] = None
    recordingReconnectWindowSeconds: Optional[int] = None
    renditionConfiguration: Optional[RenditionConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    thumbnailConfiguration: Optional[ThumbnailConfigurationTypeDef] = None

class RecordingConfigurationSummaryTypeDef(BaseModel):
    arn: str
    destinationConfiguration: DestinationConfigurationTypeDef
    state: RecordingConfigurationStateType
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class RecordingConfigurationTypeDef(BaseModel):
    arn: str
    destinationConfiguration: DestinationConfigurationTypeDef
    state: RecordingConfigurationStateType
    name: Optional[str] = None
    recordingReconnectWindowSeconds: Optional[int] = None
    renditionConfiguration: Optional[RenditionConfigurationOutputTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    thumbnailConfiguration: Optional[ThumbnailConfigurationOutputTypeDef] = None

class ListRecordingConfigurationsResponseTypeDef(BaseModel):
    nextToken: str
    recordingConfigurations: List[RecordingConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecordingConfigurationResponseTypeDef(BaseModel):
    recordingConfiguration: RecordingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecordingConfigurationResponseTypeDef(BaseModel):
    recordingConfiguration: RecordingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StreamSessionTypeDef(BaseModel):
    channel: Optional[ChannelTypeDef] = None
    endTime: Optional[datetime] = None
    ingestConfiguration: Optional[IngestConfigurationTypeDef] = None
    recordingConfiguration: Optional[RecordingConfigurationTypeDef] = None
    startTime: Optional[datetime] = None
    streamId: Optional[str] = None
    truncatedEvents: Optional[List[StreamEventTypeDef]] = None

class GetStreamSessionResponseTypeDef(BaseModel):
    streamSession: StreamSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

