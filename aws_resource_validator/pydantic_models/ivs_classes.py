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
from aws_resource_validator.pydantic_models.ivs_constants import *

class AudioConfigurationTypeDef(BaseValidatorModel):
    channels: Optional[int] = None
    codec: Optional[str] = None
    sampleRate: Optional[int] = None
    targetBitrate: Optional[int] = None

class BatchErrorTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None

class BatchGetChannelRequestRequestTypeDef(BaseValidatorModel):
    arns: Sequence[str]

class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None

class BatchGetStreamKeyRequestRequestTypeDef(BaseValidatorModel):
    arns: Sequence[str]

class StreamKeyTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    channelArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    value: Optional[str] = None

class BatchStartViewerSessionRevocationErrorTypeDef(BaseValidatorModel):
    channelArn: str
    viewerId: str
    code: Optional[str] = None
    message: Optional[str] = None

class BatchStartViewerSessionRevocationViewerSessionTypeDef(BaseValidatorModel):
    channelArn: str
    viewerId: str
    viewerSessionVersionsLessThanOrEqualTo: Optional[int] = None

class ChannelSummaryTypeDef(BaseValidatorModel):
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

class SrtTypeDef(BaseValidatorModel):
    endpoint: Optional[str] = None
    passphrase: Optional[str] = None

class CreateChannelRequestRequestTypeDef(BaseValidatorModel):
    authorized: Optional[bool] = None
    insecureIngest: Optional[bool] = None
    latencyMode: Optional[ChannelLatencyModeType] = None
    name: Optional[str] = None
    playbackRestrictionPolicyArn: Optional[str] = None
    preset: Optional[TranscodePresetType] = None
    recordingConfigurationArn: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None
    type: Optional[ChannelTypeType] = None

class CreatePlaybackRestrictionPolicyRequestRequestTypeDef(BaseValidatorModel):
    allowedCountries: Optional[Sequence[str]] = None
    allowedOrigins: Optional[Sequence[str]] = None
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class PlaybackRestrictionPolicyTypeDef(BaseValidatorModel):
    allowedCountries: List[str]
    allowedOrigins: List[str]
    arn: str
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class RenditionConfigurationTypeDef(BaseValidatorModel):
    renditionSelection: Optional[RenditionConfigurationRenditionSelectionType] = None
    renditions: Optional[Sequence[RenditionConfigurationRenditionType]] = None

class ThumbnailConfigurationTypeDef(BaseValidatorModel):
    recordingMode: Optional[RecordingModeType] = None
    resolution: Optional[ThumbnailConfigurationResolutionType] = None
    storage: Optional[Sequence[ThumbnailConfigurationStorageType]] = None
    targetIntervalSeconds: Optional[int] = None

class CreateStreamKeyRequestRequestTypeDef(BaseValidatorModel):
    channelArn: str
    tags: Optional[Mapping[str, str]] = None

class DeleteChannelRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeletePlaybackKeyPairRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeletePlaybackRestrictionPolicyRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteRecordingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class DeleteStreamKeyRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class S3DestinationConfigurationTypeDef(BaseValidatorModel):
    bucketName: str

class GetChannelRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetPlaybackKeyPairRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class PlaybackKeyPairTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    fingerprint: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class GetPlaybackRestrictionPolicyRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetRecordingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetStreamKeyRequestRequestTypeDef(BaseValidatorModel):
    arn: str

class GetStreamRequestRequestTypeDef(BaseValidatorModel):
    channelArn: str

class StreamTypeDef(BaseValidatorModel):
    channelArn: Optional[str] = None
    health: Optional[StreamHealthType] = None
    playbackUrl: Optional[str] = None
    startTime: Optional[datetime] = None
    state: Optional[StreamStateType] = None
    streamId: Optional[str] = None
    viewerCount: Optional[int] = None

class GetStreamSessionRequestRequestTypeDef(BaseValidatorModel):
    channelArn: str
    streamId: Optional[str] = None

class ImportPlaybackKeyPairRequestRequestTypeDef(BaseValidatorModel):
    publicKeyMaterial: str
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None

class VideoConfigurationTypeDef(BaseValidatorModel):
    avcLevel: Optional[str] = None
    avcProfile: Optional[str] = None
    codec: Optional[str] = None
    encoder: Optional[str] = None
    targetBitrate: Optional[int] = None
    targetFramerate: Optional[int] = None
    videoHeight: Optional[int] = None
    videoWidth: Optional[int] = None

class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None

class ListChannelsRequestRequestTypeDef(BaseValidatorModel):
    filterByName: Optional[str] = None
    filterByPlaybackRestrictionPolicyArn: Optional[str] = None
    filterByRecordingConfigurationArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListPlaybackKeyPairsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PlaybackKeyPairSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListPlaybackRestrictionPoliciesRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class PlaybackRestrictionPolicySummaryTypeDef(BaseValidatorModel):
    allowedCountries: List[str]
    allowedOrigins: List[str]
    arn: str
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListRecordingConfigurationsRequestRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListStreamKeysRequestRequestTypeDef(BaseValidatorModel):
    channelArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StreamKeySummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    channelArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class ListStreamSessionsRequestRequestTypeDef(BaseValidatorModel):
    channelArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class StreamSessionSummaryTypeDef(BaseValidatorModel):
    endTime: Optional[datetime] = None
    hasErrorEvent: Optional[bool] = None
    startTime: Optional[datetime] = None
    streamId: Optional[str] = None

class StreamFiltersTypeDef(BaseValidatorModel):
    health: Optional[StreamHealthType] = None

class StreamSummaryTypeDef(BaseValidatorModel):
    channelArn: Optional[str] = None
    health: Optional[StreamHealthType] = None
    startTime: Optional[datetime] = None
    state: Optional[StreamStateType] = None
    streamId: Optional[str] = None
    viewerCount: Optional[int] = None

class ListTagsForResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str

class PutMetadataRequestRequestTypeDef(BaseValidatorModel):
    channelArn: str
    metadata: str

class RenditionConfigurationOutputTypeDef(BaseValidatorModel):
    renditionSelection: Optional[RenditionConfigurationRenditionSelectionType] = None
    renditions: Optional[List[RenditionConfigurationRenditionType]] = None

class ThumbnailConfigurationOutputTypeDef(BaseValidatorModel):
    recordingMode: Optional[RecordingModeType] = None
    resolution: Optional[ThumbnailConfigurationResolutionType] = None
    storage: Optional[List[ThumbnailConfigurationStorageType]] = None
    targetIntervalSeconds: Optional[int] = None

class StartViewerSessionRevocationRequestRequestTypeDef(BaseValidatorModel):
    channelArn: str
    viewerId: str
    viewerSessionVersionsLessThanOrEqualTo: Optional[int] = None

class StopStreamRequestRequestTypeDef(BaseValidatorModel):
    channelArn: str

class StreamEventTypeDef(BaseValidatorModel):
    eventTime: Optional[datetime] = None
    name: Optional[str] = None
    type: Optional[str] = None

class TagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateChannelRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    authorized: Optional[bool] = None
    insecureIngest: Optional[bool] = None
    latencyMode: Optional[ChannelLatencyModeType] = None
    name: Optional[str] = None
    playbackRestrictionPolicyArn: Optional[str] = None
    preset: Optional[TranscodePresetType] = None
    recordingConfigurationArn: Optional[str] = None
    type: Optional[ChannelTypeType] = None

class UpdatePlaybackRestrictionPolicyRequestRequestTypeDef(BaseValidatorModel):
    arn: str
    allowedCountries: Optional[Sequence[str]] = None
    allowedOrigins: Optional[Sequence[str]] = None
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None

class EmptyResponseMetadataTypeDef(BaseValidatorModel):
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetStreamKeyResponseTypeDef(BaseValidatorModel):
    errors: List[BatchErrorTypeDef]
    streamKeys: List[StreamKeyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStreamKeyResponseTypeDef(BaseValidatorModel):
    streamKey: StreamKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamKeyResponseTypeDef(BaseValidatorModel):
    streamKey: StreamKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class BatchStartViewerSessionRevocationResponseTypeDef(BaseValidatorModel):
    errors: List[BatchStartViewerSessionRevocationErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchStartViewerSessionRevocationRequestRequestTypeDef(BaseValidatorModel):
    viewerSessions: Sequence[BatchStartViewerSessionRevocationViewerSessionTypeDef]

class ListChannelsResponseTypeDef(BaseValidatorModel):
    channels: List[ChannelSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ChannelTypeDef(BaseValidatorModel):
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

class CreatePlaybackRestrictionPolicyResponseTypeDef(BaseValidatorModel):
    playbackRestrictionPolicy: PlaybackRestrictionPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetPlaybackRestrictionPolicyResponseTypeDef(BaseValidatorModel):
    playbackRestrictionPolicy: PlaybackRestrictionPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdatePlaybackRestrictionPolicyResponseTypeDef(BaseValidatorModel):
    playbackRestrictionPolicy: PlaybackRestrictionPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DestinationConfigurationTypeDef(BaseValidatorModel):
    s3: Optional[S3DestinationConfigurationTypeDef] = None

class GetPlaybackKeyPairResponseTypeDef(BaseValidatorModel):
    keyPair: PlaybackKeyPairTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ImportPlaybackKeyPairResponseTypeDef(BaseValidatorModel):
    keyPair: PlaybackKeyPairTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetStreamResponseTypeDef(BaseValidatorModel):
    stream: StreamTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class IngestConfigurationTypeDef(BaseValidatorModel):
    audio: Optional[AudioConfigurationTypeDef] = None
    video: Optional[VideoConfigurationTypeDef] = None

class ListChannelsRequestListChannelsPaginateTypeDef(BaseValidatorModel):
    filterByName: Optional[str] = None
    filterByPlaybackRestrictionPolicyArn: Optional[str] = None
    filterByRecordingConfigurationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPlaybackKeyPairsRequestListPlaybackKeyPairsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListRecordingConfigurationsRequestListRecordingConfigurationsPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamKeysRequestListStreamKeysPaginateTypeDef(BaseValidatorModel):
    channelArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListPlaybackKeyPairsResponseTypeDef(BaseValidatorModel):
    keyPairs: List[PlaybackKeyPairSummaryTypeDef]
    nextToken: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListPlaybackRestrictionPoliciesResponseTypeDef(BaseValidatorModel):
    nextToken: str
    playbackRestrictionPolicies: List[PlaybackRestrictionPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamKeysResponseTypeDef(BaseValidatorModel):
    nextToken: str
    streamKeys: List[StreamKeySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamSessionsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    streamSessions: List[StreamSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListStreamsRequestListStreamsPaginateTypeDef(BaseValidatorModel):
    filterBy: Optional[StreamFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None

class ListStreamsRequestRequestTypeDef(BaseValidatorModel):
    filterBy: Optional[StreamFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None

class ListStreamsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    streams: List[StreamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class BatchGetChannelResponseTypeDef(BaseValidatorModel):
    channels: List[ChannelTypeDef]
    errors: List[BatchErrorTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateChannelResponseTypeDef(BaseValidatorModel):
    channel: ChannelTypeDef
    streamKey: StreamKeyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetChannelResponseTypeDef(BaseValidatorModel):
    channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChannelResponseTypeDef(BaseValidatorModel):
    channel: ChannelTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecordingConfigurationRequestRequestTypeDef(BaseValidatorModel):
    destinationConfiguration: DestinationConfigurationTypeDef
    name: Optional[str] = None
    recordingReconnectWindowSeconds: Optional[int] = None
    renditionConfiguration: Optional[RenditionConfigurationTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    thumbnailConfiguration: Optional[ThumbnailConfigurationTypeDef] = None

class RecordingConfigurationSummaryTypeDef(BaseValidatorModel):
    arn: str
    destinationConfiguration: DestinationConfigurationTypeDef
    state: RecordingConfigurationStateType
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None

class RecordingConfigurationTypeDef(BaseValidatorModel):
    arn: str
    destinationConfiguration: DestinationConfigurationTypeDef
    state: RecordingConfigurationStateType
    name: Optional[str] = None
    recordingReconnectWindowSeconds: Optional[int] = None
    renditionConfiguration: Optional[RenditionConfigurationOutputTypeDef] = None
    tags: Optional[Dict[str, str]] = None
    thumbnailConfiguration: Optional[ThumbnailConfigurationOutputTypeDef] = None

class ListRecordingConfigurationsResponseTypeDef(BaseValidatorModel):
    nextToken: str
    recordingConfigurations: List[RecordingConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class CreateRecordingConfigurationResponseTypeDef(BaseValidatorModel):
    recordingConfiguration: RecordingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetRecordingConfigurationResponseTypeDef(BaseValidatorModel):
    recordingConfiguration: RecordingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class StreamSessionTypeDef(BaseValidatorModel):
    channel: Optional[ChannelTypeDef] = None
    endTime: Optional[datetime] = None
    ingestConfiguration: Optional[IngestConfigurationTypeDef] = None
    recordingConfiguration: Optional[RecordingConfigurationTypeDef] = None
    startTime: Optional[datetime] = None
    streamId: Optional[str] = None
    truncatedEvents: Optional[List[StreamEventTypeDef]] = None

class GetStreamSessionResponseTypeDef(BaseValidatorModel):
    streamSession: StreamSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

