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
from aws_resource_validator.pydantic_models.ivs_constants import *

class AudioConfigurationTypeDef(BaseValidatorModel):
    channels: Optional[int] = None
    codec: Optional[str] = None
    sampleRate: Optional[int] = None
    targetBitrate: Optional[int] = None
    track: Optional[str] = None


class BatchErrorTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    code: Optional[str] = None
    message: Optional[str] = None


class BatchGetChannelRequestTypeDef(BaseValidatorModel):
    arns: Sequence[str]


class ResponseMetadataTypeDef(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class BatchGetStreamKeyRequestTypeDef(BaseValidatorModel):
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


class MultitrackInputConfigurationTypeDef(BaseValidatorModel):
    enabled: Optional[bool] = None
    maximumResolution: Optional[MultitrackMaximumResolutionType] = None
    policy: Optional[MultitrackPolicyType] = None


class SrtTypeDef(BaseValidatorModel):
    endpoint: Optional[str] = None
    passphrase: Optional[str] = None


class CreatePlaybackRestrictionPolicyRequestTypeDef(BaseValidatorModel):
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


class CreateStreamKeyRequestTypeDef(BaseValidatorModel):
    channelArn: str
    tags: Optional[Mapping[str, str]] = None


class DeleteChannelRequestTypeDef(BaseValidatorModel):
    arn: str


class DeletePlaybackKeyPairRequestTypeDef(BaseValidatorModel):
    arn: str


class DeletePlaybackRestrictionPolicyRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteRecordingConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str


class DeleteStreamKeyRequestTypeDef(BaseValidatorModel):
    arn: str


class S3DestinationConfigurationTypeDef(BaseValidatorModel):
    bucketName: str


class GetChannelRequestTypeDef(BaseValidatorModel):
    arn: str


class GetPlaybackKeyPairRequestTypeDef(BaseValidatorModel):
    arn: str


class PlaybackKeyPairTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    fingerprint: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class GetPlaybackRestrictionPolicyRequestTypeDef(BaseValidatorModel):
    arn: str


class GetRecordingConfigurationRequestTypeDef(BaseValidatorModel):
    arn: str


class GetStreamKeyRequestTypeDef(BaseValidatorModel):
    arn: str


class GetStreamRequestTypeDef(BaseValidatorModel):
    channelArn: str


class StreamTypeDef(BaseValidatorModel):
    channelArn: Optional[str] = None
    health: Optional[StreamHealthType] = None
    playbackUrl: Optional[str] = None
    startTime: Optional[datetime] = None
    state: Optional[StreamStateType] = None
    streamId: Optional[str] = None
    viewerCount: Optional[int] = None


class GetStreamSessionRequestTypeDef(BaseValidatorModel):
    channelArn: str
    streamId: Optional[str] = None


class ImportPlaybackKeyPairRequestTypeDef(BaseValidatorModel):
    publicKeyMaterial: str
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class VideoConfigurationTypeDef(BaseValidatorModel):
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


class PaginatorConfigTypeDef(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListChannelsRequestTypeDef(BaseValidatorModel):
    filterByName: Optional[str] = None
    filterByPlaybackRestrictionPolicyArn: Optional[str] = None
    filterByRecordingConfigurationArn: Optional[str] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListPlaybackKeyPairsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PlaybackKeyPairSummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListPlaybackRestrictionPoliciesRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class PlaybackRestrictionPolicySummaryTypeDef(BaseValidatorModel):
    allowedCountries: List[str]
    allowedOrigins: List[str]
    arn: str
    enableStrictOriginEnforcement: Optional[bool] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListRecordingConfigurationsRequestTypeDef(BaseValidatorModel):
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListStreamKeysRequestTypeDef(BaseValidatorModel):
    channelArn: str
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class StreamKeySummaryTypeDef(BaseValidatorModel):
    arn: Optional[str] = None
    channelArn: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListStreamSessionsRequestTypeDef(BaseValidatorModel):
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


class ListTagsForResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str


class PutMetadataRequestTypeDef(BaseValidatorModel):
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


class RenditionConfigurationTypeDef(BaseValidatorModel):
    renditionSelection: Optional[RenditionConfigurationRenditionSelectionType] = None
    renditions: Optional[Sequence[RenditionConfigurationRenditionType]] = None


class StartViewerSessionRevocationRequestTypeDef(BaseValidatorModel):
    channelArn: str
    viewerId: str
    viewerSessionVersionsLessThanOrEqualTo: Optional[int] = None


class StopStreamRequestTypeDef(BaseValidatorModel):
    channelArn: str


class TagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class ThumbnailConfigurationTypeDef(BaseValidatorModel):
    recordingMode: Optional[RecordingModeType] = None
    resolution: Optional[ThumbnailConfigurationResolutionType] = None
    storage: Optional[Sequence[ThumbnailConfigurationStorageType]] = None
    targetIntervalSeconds: Optional[int] = None


class UntagResourceRequestTypeDef(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdatePlaybackRestrictionPolicyRequestTypeDef(BaseValidatorModel):
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


class BatchStartViewerSessionRevocationRequestTypeDef(BaseValidatorModel):
    viewerSessions: Sequence[BatchStartViewerSessionRevocationViewerSessionTypeDef]


class ChannelSummaryTypeDef(BaseValidatorModel):
    pass


class ListChannelsResponseTypeDef(BaseValidatorModel):
    channels: List[ChannelSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


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


class IngestConfigurationsTypeDef(BaseValidatorModel):
    audioConfigurations: List[AudioConfigurationTypeDef]
    videoConfigurations: List[VideoConfigurationTypeDef]


class ListChannelsRequestPaginateTypeDef(BaseValidatorModel):
    filterByName: Optional[str] = None
    filterByPlaybackRestrictionPolicyArn: Optional[str] = None
    filterByRecordingConfigurationArn: Optional[str] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPlaybackKeyPairsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListRecordingConfigurationsRequestPaginateTypeDef(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStreamKeysRequestPaginateTypeDef(BaseValidatorModel):
    channelArn: str
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListPlaybackKeyPairsResponseTypeDef(BaseValidatorModel):
    keyPairs: List[PlaybackKeyPairSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListPlaybackRestrictionPoliciesResponseTypeDef(BaseValidatorModel):
    playbackRestrictionPolicies: List[PlaybackRestrictionPolicySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListStreamKeysResponseTypeDef(BaseValidatorModel):
    streamKeys: List[StreamKeySummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListStreamSessionsResponseTypeDef(BaseValidatorModel):
    streamSessions: List[StreamSessionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ListStreamsRequestPaginateTypeDef(BaseValidatorModel):
    filterBy: Optional[StreamFiltersTypeDef] = None
    PaginationConfig: Optional[PaginatorConfigTypeDef] = None


class ListStreamsRequestTypeDef(BaseValidatorModel):
    filterBy: Optional[StreamFiltersTypeDef] = None
    maxResults: Optional[int] = None
    nextToken: Optional[str] = None


class ListStreamsResponseTypeDef(BaseValidatorModel):
    streams: List[StreamSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class ChannelTypeDef(BaseValidatorModel):
    pass


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


class RenditionConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class ThumbnailConfigurationUnionTypeDef(BaseValidatorModel):
    pass


class CreateRecordingConfigurationRequestTypeDef(BaseValidatorModel):
    destinationConfiguration: DestinationConfigurationTypeDef
    name: Optional[str] = None
    recordingReconnectWindowSeconds: Optional[int] = None
    renditionConfiguration: Optional[RenditionConfigurationUnionTypeDef] = None
    tags: Optional[Mapping[str, str]] = None
    thumbnailConfiguration: Optional[ThumbnailConfigurationUnionTypeDef] = None


class ListRecordingConfigurationsResponseTypeDef(BaseValidatorModel):
    recordingConfigurations: List[RecordingConfigurationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: Optional[str] = None


class CreateRecordingConfigurationResponseTypeDef(BaseValidatorModel):
    recordingConfiguration: RecordingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class GetRecordingConfigurationResponseTypeDef(BaseValidatorModel):
    recordingConfiguration: RecordingConfigurationTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


class StreamEventTypeDef(BaseValidatorModel):
    pass


class StreamSessionTypeDef(BaseValidatorModel):
    channel: Optional[ChannelTypeDef] = None
    endTime: Optional[datetime] = None
    ingestConfiguration: Optional[IngestConfigurationTypeDef] = None
    ingestConfigurations: Optional[IngestConfigurationsTypeDef] = None
    recordingConfiguration: Optional[RecordingConfigurationTypeDef] = None
    startTime: Optional[datetime] = None
    streamId: Optional[str] = None
    truncatedEvents: Optional[List[StreamEventTypeDef]] = None


class GetStreamSessionResponseTypeDef(BaseValidatorModel):
    streamSession: StreamSessionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef


