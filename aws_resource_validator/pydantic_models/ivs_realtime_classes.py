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
from aws_resource_validator.pydantic_models.ivs_realtime_constants import *

class ParticipantThumbnailConfigurationOutput(BaseValidatorModel):
    targetIntervalSeconds: Optional[int] = None
    storage: Optional[List[ThumbnailStorageTypeType]] = None
    recordingMode: Optional[ThumbnailRecordingModeType] = None


class ParticipantThumbnailConfiguration(BaseValidatorModel):
    targetIntervalSeconds: Optional[int] = None
    storage: Optional[Sequence[ThumbnailStorageTypeType]] = None
    recordingMode: Optional[ThumbnailRecordingModeType] = None


class ChannelDestinationConfiguration(BaseValidatorModel):
    channelArn: str
    encoderConfigurationArn: Optional[str] = None


class CompositionThumbnailConfigurationOutput(BaseValidatorModel):
    targetIntervalSeconds: Optional[int] = None
    storage: Optional[List[ThumbnailStorageTypeType]] = None


class CompositionThumbnailConfiguration(BaseValidatorModel):
    targetIntervalSeconds: Optional[int] = None
    storage: Optional[Sequence[ThumbnailStorageTypeType]] = None


class Video(BaseValidatorModel):
    width: Optional[int] = None
    height: Optional[int] = None
    framerate: Optional[float] = None
    bitrate: Optional[int] = None


class ResponseMetadata(BaseValidatorModel):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: Optional[str] = None


class CreateIngestConfigurationRequest(BaseValidatorModel):
    ingestProtocol: IngestProtocolType
    name: Optional[str] = None
    stageArn: Optional[str] = None
    userId: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    insecureIngest: Optional[bool] = None
    tags: Optional[Mapping[str, str]] = None


class IngestConfiguration(BaseValidatorModel):
    arn: str
    ingestProtocol: IngestProtocolType
    streamKey: str
    stageArn: str
    participantId: str
    state: IngestConfigurationStateType
    name: Optional[str] = None
    userId: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    tags: Optional[Dict[str, str]] = None


class CreateParticipantTokenRequest(BaseValidatorModel):
    stageArn: str
    duration: Optional[int] = None
    userId: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    capabilities: Optional[Sequence[ParticipantTokenCapabilityType]] = None


class ParticipantToken(BaseValidatorModel):
    participantId: Optional[str] = None
    token: Optional[str] = None
    userId: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    duration: Optional[int] = None
    capabilities: Optional[List[ParticipantTokenCapabilityType]] = None
    expirationTime: Optional[datetime] = None


class ParticipantTokenConfiguration(BaseValidatorModel):
    duration: Optional[int] = None
    userId: Optional[str] = None
    attributes: Optional[Mapping[str, str]] = None
    capabilities: Optional[Sequence[ParticipantTokenCapabilityType]] = None


class S3StorageConfiguration(BaseValidatorModel):
    bucketName: str


class DeleteEncoderConfigurationRequest(BaseValidatorModel):
    arn: str


class DeleteIngestConfigurationRequest(BaseValidatorModel):
    arn: str
    force: Optional[bool] = None


class DeletePublicKeyRequest(BaseValidatorModel):
    arn: str


class DeleteStageRequest(BaseValidatorModel):
    arn: str


class DeleteStorageConfigurationRequest(BaseValidatorModel):
    arn: str


class S3Detail(BaseValidatorModel):
    recordingPrefix: str


class DisconnectParticipantRequest(BaseValidatorModel):
    stageArn: str
    participantId: str
    reason: Optional[str] = None


class EncoderConfigurationSummary(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class Event(BaseValidatorModel):
    name: Optional[EventNameType] = None
    participantId: Optional[str] = None
    eventTime: Optional[datetime] = None
    remoteParticipantId: Optional[str] = None
    errorCode: Optional[EventErrorCodeType] = None


class GetCompositionRequest(BaseValidatorModel):
    arn: str


class GetEncoderConfigurationRequest(BaseValidatorModel):
    arn: str


class GetIngestConfigurationRequest(BaseValidatorModel):
    arn: str


class GetParticipantRequest(BaseValidatorModel):
    stageArn: str
    sessionId: str
    participantId: str


class Participant(BaseValidatorModel):
    participantId: Optional[str] = None
    userId: Optional[str] = None
    state: Optional[ParticipantStateType] = None
    firstJoinTime: Optional[datetime] = None
    attributes: Optional[Dict[str, str]] = None
    published: Optional[bool] = None
    ispName: Optional[str] = None
    osName: Optional[str] = None
    osVersion: Optional[str] = None
    browserName: Optional[str] = None
    browserVersion: Optional[str] = None
    sdkVersion: Optional[str] = None
    recordingS3BucketName: Optional[str] = None
    recordingS3Prefix: Optional[str] = None
    recordingState: Optional[ParticipantRecordingStateType] = None
    protocol: Optional[ParticipantProtocolType] = None


class GetPublicKeyRequest(BaseValidatorModel):
    arn: str


class PublicKey(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    publicKeyMaterial: Optional[str] = None
    fingerprint: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class GetStageRequest(BaseValidatorModel):
    arn: str


class GetStageSessionRequest(BaseValidatorModel):
    stageArn: str
    sessionId: str


class StageSession(BaseValidatorModel):
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class GetStorageConfigurationRequest(BaseValidatorModel):
    arn: str


class GridConfiguration(BaseValidatorModel):
    featuredParticipantAttribute: Optional[str] = None
    omitStoppedVideo: Optional[bool] = None
    videoAspectRatio: Optional[VideoAspectRatioType] = None
    videoFillMode: Optional[VideoFillModeType] = None
    gridGap: Optional[int] = None


class ImportPublicKeyRequest(BaseValidatorModel):
    publicKeyMaterial: str
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class IngestConfigurationSummary(BaseValidatorModel):
    arn: str
    ingestProtocol: IngestProtocolType
    stageArn: str
    participantId: str
    state: IngestConfigurationStateType
    name: Optional[str] = None
    userId: Optional[str] = None


class PipConfiguration(BaseValidatorModel):
    featuredParticipantAttribute: Optional[str] = None
    omitStoppedVideo: Optional[bool] = None
    videoFillMode: Optional[VideoFillModeType] = None
    gridGap: Optional[int] = None
    pipParticipantAttribute: Optional[str] = None
    pipBehavior: Optional[PipBehaviorType] = None
    pipOffset: Optional[int] = None
    pipPosition: Optional[PipPositionType] = None
    pipWidth: Optional[int] = None
    pipHeight: Optional[int] = None


class ListCompositionsRequest(BaseValidatorModel):
    filterByStageArn: Optional[str] = None
    filterByEncoderConfigurationArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListEncoderConfigurationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


class ListIngestConfigurationsRequest(BaseValidatorModel):
    filterByStageArn: Optional[str] = None
    filterByState: Optional[IngestConfigurationStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListParticipantEventsRequest(BaseValidatorModel):
    stageArn: str
    sessionId: str
    participantId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListParticipantsRequest(BaseValidatorModel):
    stageArn: str
    sessionId: str
    filterByUserId: Optional[str] = None
    filterByPublished: Optional[bool] = None
    filterByState: Optional[ParticipantStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None
    filterByRecordingState: Optional[ParticipantRecordingFilterByRecordingStateType] = None


class ParticipantSummary(BaseValidatorModel):
    participantId: Optional[str] = None
    userId: Optional[str] = None
    state: Optional[ParticipantStateType] = None
    firstJoinTime: Optional[datetime] = None
    published: Optional[bool] = None
    recordingState: Optional[ParticipantRecordingStateType] = None


class ListPublicKeysRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PublicKeySummary(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListStageSessionsRequest(BaseValidatorModel):
    stageArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StageSessionSummary(BaseValidatorModel):
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class ListStagesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StageSummary(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    activeSessionId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


class ListStorageConfigurationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class StageEndpoints(BaseValidatorModel):
    events: Optional[str] = None
    whip: Optional[str] = None
    rtmp: Optional[str] = None
    rtmps: Optional[str] = None


class StopCompositionRequest(BaseValidatorModel):
    arn: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Mapping[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: Sequence[str]


class UpdateIngestConfigurationRequest(BaseValidatorModel):
    arn: str
    stageArn: Optional[str] = None


class AutoParticipantRecordingConfigurationOutput(BaseValidatorModel):
    storageConfigurationArn: str
    mediaTypes: Optional[List[ParticipantRecordingMediaTypeType]] = None
    thumbnailConfiguration: Optional[ParticipantThumbnailConfigurationOutput] = None
    recordingReconnectWindowSeconds: Optional[int] = None


class AutoParticipantRecordingConfiguration(BaseValidatorModel):
    storageConfigurationArn: str
    mediaTypes: Optional[Sequence[ParticipantRecordingMediaTypeType]] = None
    thumbnailConfiguration: Optional[ParticipantThumbnailConfiguration] = None
    recordingReconnectWindowSeconds: Optional[int] = None


class DestinationSummary(BaseValidatorModel):
    pass


class CompositionSummary(BaseValidatorModel):
    arn: str
    stageArn: str
    destinations: List[DestinationSummary]
    state: CompositionStateType
    tags: Optional[Dict[str, str]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class CreateEncoderConfigurationRequest(BaseValidatorModel):
    name: Optional[str] = None
    video: Optional[Video] = None
    tags: Optional[Mapping[str, str]] = None


class EncoderConfiguration(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    video: Optional[Video] = None
    tags: Optional[Dict[str, str]] = None


class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


class CreateIngestConfigurationResponse(BaseValidatorModel):
    ingestConfiguration: IngestConfiguration
    ResponseMetadata: ResponseMetadata


class GetIngestConfigurationResponse(BaseValidatorModel):
    ingestConfiguration: IngestConfiguration
    ResponseMetadata: ResponseMetadata


class UpdateIngestConfigurationResponse(BaseValidatorModel):
    ingestConfiguration: IngestConfiguration
    ResponseMetadata: ResponseMetadata


class CreateParticipantTokenResponse(BaseValidatorModel):
    participantToken: ParticipantToken
    ResponseMetadata: ResponseMetadata


class CreateStorageConfigurationRequest(BaseValidatorModel):
    s3: S3StorageConfiguration
    name: Optional[str] = None
    tags: Optional[Mapping[str, str]] = None


class StorageConfigurationSummary(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    s3: Optional[S3StorageConfiguration] = None
    tags: Optional[Dict[str, str]] = None


class StorageConfiguration(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    s3: Optional[S3StorageConfiguration] = None
    tags: Optional[Dict[str, str]] = None


class DestinationDetail(BaseValidatorModel):
    s3: Optional[S3Detail] = None


class ListEncoderConfigurationsResponse(BaseValidatorModel):
    encoderConfigurations: List[EncoderConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListParticipantEventsResponse(BaseValidatorModel):
    events: List[Event]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class GetParticipantResponse(BaseValidatorModel):
    participant: Participant
    ResponseMetadata: ResponseMetadata


class GetPublicKeyResponse(BaseValidatorModel):
    publicKey: PublicKey
    ResponseMetadata: ResponseMetadata


class ImportPublicKeyResponse(BaseValidatorModel):
    publicKey: PublicKey
    ResponseMetadata: ResponseMetadata


class GetStageSessionResponse(BaseValidatorModel):
    stageSession: StageSession
    ResponseMetadata: ResponseMetadata


class ListIngestConfigurationsResponse(BaseValidatorModel):
    ingestConfigurations: List[IngestConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class LayoutConfiguration(BaseValidatorModel):
    grid: Optional[GridConfiguration] = None
    pip: Optional[PipConfiguration] = None


class ListIngestConfigurationsRequestPaginate(BaseValidatorModel):
    filterByStageArn: Optional[str] = None
    filterByState: Optional[IngestConfigurationStateType] = None
    PaginationConfig: Optional[PaginatorConfig] = None


class ListPublicKeysRequestPaginate(BaseValidatorModel):
    PaginationConfig: Optional[PaginatorConfig] = None


class ListParticipantsResponse(BaseValidatorModel):
    participants: List[ParticipantSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListPublicKeysResponse(BaseValidatorModel):
    publicKeys: List[PublicKeySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListStageSessionsResponse(BaseValidatorModel):
    stageSessions: List[StageSessionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class ListStagesResponse(BaseValidatorModel):
    stages: List[StageSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class RecordingConfiguration(BaseValidatorModel):
    pass


class S3DestinationConfigurationOutput(BaseValidatorModel):
    storageConfigurationArn: str
    encoderConfigurationArns: List[str]
    recordingConfiguration: Optional[RecordingConfiguration] = None
    thumbnailConfigurations: Optional[List[CompositionThumbnailConfigurationOutput]] = None


class Stage(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    activeSessionId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None
    autoParticipantRecordingConfiguration: Optional[ AutoParticipantRecordingConfigurationOutput ] = None
    endpoints: Optional[StageEndpoints] = None


class ListCompositionsResponse(BaseValidatorModel):
    compositions: List[CompositionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CompositionThumbnailConfigurationUnion(BaseValidatorModel):
    pass


class S3DestinationConfiguration(BaseValidatorModel):
    storageConfigurationArn: str
    encoderConfigurationArns: Sequence[str]
    recordingConfiguration: Optional[RecordingConfiguration] = None
    thumbnailConfigurations: Optional[Sequence[CompositionThumbnailConfigurationUnion]] = None


class CreateEncoderConfigurationResponse(BaseValidatorModel):
    encoderConfiguration: EncoderConfiguration
    ResponseMetadata: ResponseMetadata


class GetEncoderConfigurationResponse(BaseValidatorModel):
    encoderConfiguration: EncoderConfiguration
    ResponseMetadata: ResponseMetadata


class ListStorageConfigurationsResponse(BaseValidatorModel):
    storageConfigurations: List[StorageConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class CreateStorageConfigurationResponse(BaseValidatorModel):
    storageConfiguration: StorageConfiguration
    ResponseMetadata: ResponseMetadata


class GetStorageConfigurationResponse(BaseValidatorModel):
    storageConfiguration: StorageConfiguration
    ResponseMetadata: ResponseMetadata


class DestinationConfigurationOutput(BaseValidatorModel):
    name: Optional[str] = None
    channel: Optional[ChannelDestinationConfiguration] = None
    s3: Optional[S3DestinationConfigurationOutput] = None


class CreateStageResponse(BaseValidatorModel):
    stage: Stage
    participantTokens: List[ParticipantToken]
    ResponseMetadata: ResponseMetadata


class GetStageResponse(BaseValidatorModel):
    stage: Stage
    ResponseMetadata: ResponseMetadata


class UpdateStageResponse(BaseValidatorModel):
    stage: Stage
    ResponseMetadata: ResponseMetadata


class AutoParticipantRecordingConfigurationUnion(BaseValidatorModel):
    pass


class CreateStageRequest(BaseValidatorModel):
    name: Optional[str] = None
    participantTokenConfigurations: Optional[Sequence[ParticipantTokenConfiguration]] = None
    tags: Optional[Mapping[str, str]] = None
    autoParticipantRecordingConfiguration: Optional[ AutoParticipantRecordingConfigurationUnion ] = None


class UpdateStageRequest(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    autoParticipantRecordingConfiguration: Optional[ AutoParticipantRecordingConfigurationUnion ] = None


class S3DestinationConfigurationUnion(BaseValidatorModel):
    pass


class DestinationConfiguration(BaseValidatorModel):
    name: Optional[str] = None
    channel: Optional[ChannelDestinationConfiguration] = None
    s3: Optional[S3DestinationConfigurationUnion] = None


class Destination(BaseValidatorModel):
    pass


class Composition(BaseValidatorModel):
    arn: str
    stageArn: str
    state: CompositionStateType
    layout: LayoutConfiguration
    destinations: List[Destination]
    tags: Optional[Dict[str, str]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class GetCompositionResponse(BaseValidatorModel):
    composition: Composition
    ResponseMetadata: ResponseMetadata


class StartCompositionResponse(BaseValidatorModel):
    composition: Composition
    ResponseMetadata: ResponseMetadata


class DestinationConfigurationUnion(BaseValidatorModel):
    pass


class StartCompositionRequest(BaseValidatorModel):
    stageArn: str
    destinations: Sequence[DestinationConfigurationUnion]
    idempotencyToken: Optional[str] = None
    layout: Optional[LayoutConfiguration] = None
    tags: Optional[Mapping[str, str]] = None


