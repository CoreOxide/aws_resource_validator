from typing import Any, Dict, IO, List, Literal, Mapping, Optional, Sequence, Union
from datetime import datetime
from pydantic import BaseModel, Field
from botocore.response import StreamingBody
from aws_resource_validator.pydantic_models.ivs_realtime.ivs_realtime_constants import *
from ..base_validator_model import BaseValidatorModel, EventStream




class ParticipantThumbnailConfigurationOutput(BaseValidatorModel):
    targetIntervalSeconds: Optional[int] = None
    storage: Optional[List[ThumbnailStorageTypeType]] = None
    recordingMode: Optional[ThumbnailRecordingModeType] = None


class ParticipantThumbnailConfiguration(BaseValidatorModel):
    targetIntervalSeconds: Optional[int] = None
    storage: Optional[List[ThumbnailStorageTypeType]] = None
    recordingMode: Optional[ThumbnailRecordingModeType] = None


class ChannelDestinationConfiguration(BaseValidatorModel):
    channelArn: str
    encoderConfigurationArn: Optional[str] = None


class DestinationSummary(BaseValidatorModel):
    id: str
    state: DestinationStateType
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


class CompositionThumbnailConfigurationOutput(BaseValidatorModel):
    targetIntervalSeconds: Optional[int] = None
    storage: Optional[List[ThumbnailStorageTypeType]] = None


class CompositionThumbnailConfiguration(BaseValidatorModel):
    targetIntervalSeconds: Optional[int] = None
    storage: Optional[List[ThumbnailStorageTypeType]] = None


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


# This class is the input for the 'create_ingest_configuration' function.
class CreateIngestConfigurationRequest(BaseValidatorModel):
    ingestProtocol: IngestProtocolType
    name: Optional[str] = None
    stageArn: Optional[str] = None
    userId: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    insecureIngest: Optional[bool] = None
    tags: Optional[Dict[str, str]] = None


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


# This class is the input for the 'create_participant_token' function.
class CreateParticipantTokenRequest(BaseValidatorModel):
    stageArn: str
    duration: Optional[int] = None
    userId: Optional[str] = None
    attributes: Optional[Dict[str, str]] = None
    capabilities: Optional[List[ParticipantTokenCapabilityType]] = None


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
    attributes: Optional[Dict[str, str]] = None
    capabilities: Optional[List[ParticipantTokenCapabilityType]] = None


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


# This class is the input for the 'get_composition' function.
class GetCompositionRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_encoder_configuration' function.
class GetEncoderConfigurationRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_ingest_configuration' function.
class GetIngestConfigurationRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_participant' function.
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


# This class is the input for the 'get_public_key' function.
class GetPublicKeyRequest(BaseValidatorModel):
    arn: str


class PublicKey(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    publicKeyMaterial: Optional[str] = None
    fingerprint: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'get_stage' function.
class GetStageRequest(BaseValidatorModel):
    arn: str


# This class is the input for the 'get_stage_session' function.
class GetStageSessionRequest(BaseValidatorModel):
    stageArn: str
    sessionId: str


class StageSession(BaseValidatorModel):
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


# This class is the input for the 'get_storage_configuration' function.
class GetStorageConfigurationRequest(BaseValidatorModel):
    arn: str


class GridConfiguration(BaseValidatorModel):
    featuredParticipantAttribute: Optional[str] = None
    omitStoppedVideo: Optional[bool] = None
    videoAspectRatio: Optional[VideoAspectRatioType] = None
    videoFillMode: Optional[VideoFillModeType] = None
    gridGap: Optional[int] = None


# This class is the input for the 'import_public_key' function.
class ImportPublicKeyRequest(BaseValidatorModel):
    publicKeyMaterial: str
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


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


# This class is the input for the 'list_compositions' function.
class ListCompositionsRequest(BaseValidatorModel):
    filterByStageArn: Optional[str] = None
    filterByEncoderConfigurationArn: Optional[str] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_encoder_configurations' function.
class ListEncoderConfigurationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PaginatorConfig(BaseValidatorModel):
    MaxItems: Optional[int] = None
    PageSize: Optional[int] = None
    StartingToken: Optional[str] = None


# This class is the input for the 'list_ingest_configurations' function.
class ListIngestConfigurationsRequest(BaseValidatorModel):
    filterByStageArn: Optional[str] = None
    filterByState: Optional[IngestConfigurationStateType] = None
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_participant_events' function.
class ListParticipantEventsRequest(BaseValidatorModel):
    stageArn: str
    sessionId: str
    participantId: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_participants' function.
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


# This class is the input for the 'list_public_keys' function.
class ListPublicKeysRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class PublicKeySummary(BaseValidatorModel):
    arn: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'list_stage_sessions' function.
class ListStageSessionsRequest(BaseValidatorModel):
    stageArn: str
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StageSessionSummary(BaseValidatorModel):
    sessionId: Optional[str] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None


# This class is the input for the 'list_stages' function.
class ListStagesRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


class StageSummary(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    activeSessionId: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


# This class is the input for the 'list_storage_configurations' function.
class ListStorageConfigurationsRequest(BaseValidatorModel):
    nextToken: Optional[str] = None
    maxResults: Optional[int] = None


# This class is the input for the 'list_tags_for_resource' function.
class ListTagsForResourceRequest(BaseValidatorModel):
    resourceArn: str


class RecordingConfiguration(BaseValidatorModel):
    format: Optional[Literal['HLS']] = None


class StageEndpoints(BaseValidatorModel):
    events: Optional[str] = None
    whip: Optional[str] = None
    rtmp: Optional[str] = None
    rtmps: Optional[str] = None


class StopCompositionRequest(BaseValidatorModel):
    arn: str


class TagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tags: Dict[str, str]


class UntagResourceRequest(BaseValidatorModel):
    resourceArn: str
    tagKeys: List[str]


# This class is the input for the 'update_ingest_configuration' function.
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
    mediaTypes: Optional[List[ParticipantRecordingMediaTypeType]] = None
    thumbnailConfiguration: Optional[ParticipantThumbnailConfiguration] = None
    recordingReconnectWindowSeconds: Optional[int] = None


class CompositionSummary(BaseValidatorModel):
    arn: str
    stageArn: str
    destinations: List[DestinationSummary]
    state: CompositionStateType
    tags: Optional[Dict[str, str]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

CompositionThumbnailConfigurationUnion = Union[CompositionThumbnailConfiguration, CompositionThumbnailConfigurationOutput]


# This class is the input for the 'create_encoder_configuration' function.
class CreateEncoderConfigurationRequest(BaseValidatorModel):
    name: Optional[str] = None
    video: Optional[Video] = None
    tags: Optional[Dict[str, str]] = None


class EncoderConfiguration(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    video: Optional[Video] = None
    tags: Optional[Dict[str, str]] = None


# This class is the output for the 'list_tags_for_resource' function.
class ListTagsForResourceResponse(BaseValidatorModel):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_ingest_configuration' function.
class CreateIngestConfigurationResponse(BaseValidatorModel):
    ingestConfiguration: IngestConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_ingest_configuration' function.
class GetIngestConfigurationResponse(BaseValidatorModel):
    ingestConfiguration: IngestConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_ingest_configuration' function.
class UpdateIngestConfigurationResponse(BaseValidatorModel):
    ingestConfiguration: IngestConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'create_participant_token' function.
class CreateParticipantTokenResponse(BaseValidatorModel):
    participantToken: ParticipantToken
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_storage_configuration' function.
class CreateStorageConfigurationRequest(BaseValidatorModel):
    s3: S3StorageConfiguration
    name: Optional[str] = None
    tags: Optional[Dict[str, str]] = None


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


# This class is the output for the 'list_encoder_configurations' function.
class ListEncoderConfigurationsResponse(BaseValidatorModel):
    encoderConfigurations: List[EncoderConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_participant_events' function.
class ListParticipantEventsResponse(BaseValidatorModel):
    events: List[Event]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'get_participant' function.
class GetParticipantResponse(BaseValidatorModel):
    participant: Participant
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_public_key' function.
class GetPublicKeyResponse(BaseValidatorModel):
    publicKey: PublicKey
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'import_public_key' function.
class ImportPublicKeyResponse(BaseValidatorModel):
    publicKey: PublicKey
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_stage_session' function.
class GetStageSessionResponse(BaseValidatorModel):
    stageSession: StageSession
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_ingest_configurations' function.
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


# This class is the output for the 'list_participants' function.
class ListParticipantsResponse(BaseValidatorModel):
    participants: List[ParticipantSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_public_keys' function.
class ListPublicKeysResponse(BaseValidatorModel):
    publicKeys: List[PublicKeySummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_stage_sessions' function.
class ListStageSessionsResponse(BaseValidatorModel):
    stageSessions: List[StageSessionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'list_stages' function.
class ListStagesResponse(BaseValidatorModel):
    stages: List[StageSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


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
    autoParticipantRecordingConfiguration: Optional[AutoParticipantRecordingConfigurationOutput] = None
    endpoints: Optional[StageEndpoints] = None

AutoParticipantRecordingConfigurationUnion = Union[AutoParticipantRecordingConfiguration, AutoParticipantRecordingConfigurationOutput]


# This class is the output for the 'list_compositions' function.
class ListCompositionsResponse(BaseValidatorModel):
    compositions: List[CompositionSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


class S3DestinationConfiguration(BaseValidatorModel):
    storageConfigurationArn: str
    encoderConfigurationArns: List[str]
    recordingConfiguration: Optional[RecordingConfiguration] = None
    thumbnailConfigurations: Optional[List[CompositionThumbnailConfigurationUnion]] = None


# This class is the output for the 'create_encoder_configuration' function.
class CreateEncoderConfigurationResponse(BaseValidatorModel):
    encoderConfiguration: EncoderConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_encoder_configuration' function.
class GetEncoderConfigurationResponse(BaseValidatorModel):
    encoderConfiguration: EncoderConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'list_storage_configurations' function.
class ListStorageConfigurationsResponse(BaseValidatorModel):
    storageConfigurations: List[StorageConfigurationSummary]
    ResponseMetadata: ResponseMetadata
    nextToken: Optional[str] = None


# This class is the output for the 'create_storage_configuration' function.
class CreateStorageConfigurationResponse(BaseValidatorModel):
    storageConfiguration: StorageConfiguration
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_storage_configuration' function.
class GetStorageConfigurationResponse(BaseValidatorModel):
    storageConfiguration: StorageConfiguration
    ResponseMetadata: ResponseMetadata


class DestinationConfigurationOutput(BaseValidatorModel):
    name: Optional[str] = None
    channel: Optional[ChannelDestinationConfiguration] = None
    s3: Optional[S3DestinationConfigurationOutput] = None


# This class is the output for the 'create_stage' function.
class CreateStageResponse(BaseValidatorModel):
    stage: Stage
    participantTokens: List[ParticipantToken]
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'get_stage' function.
class GetStageResponse(BaseValidatorModel):
    stage: Stage
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'update_stage' function.
class UpdateStageResponse(BaseValidatorModel):
    stage: Stage
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'create_stage' function.
class CreateStageRequest(BaseValidatorModel):
    name: Optional[str] = None
    participantTokenConfigurations: Optional[List[ParticipantTokenConfiguration]] = None
    tags: Optional[Dict[str, str]] = None
    autoParticipantRecordingConfiguration: Optional[AutoParticipantRecordingConfigurationUnion] = None


# This class is the input for the 'update_stage' function.
class UpdateStageRequest(BaseValidatorModel):
    arn: str
    name: Optional[str] = None
    autoParticipantRecordingConfiguration: Optional[AutoParticipantRecordingConfigurationUnion] = None

S3DestinationConfigurationUnion = Union[S3DestinationConfiguration, S3DestinationConfigurationOutput]


class Destination(BaseValidatorModel):
    id: str
    state: DestinationStateType
    configuration: DestinationConfigurationOutput
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None
    detail: Optional[DestinationDetail] = None


class DestinationConfiguration(BaseValidatorModel):
    name: Optional[str] = None
    channel: Optional[ChannelDestinationConfiguration] = None
    s3: Optional[S3DestinationConfigurationUnion] = None


class Composition(BaseValidatorModel):
    arn: str
    stageArn: str
    state: CompositionStateType
    layout: LayoutConfiguration
    destinations: List[Destination]
    tags: Optional[Dict[str, str]] = None
    startTime: Optional[datetime] = None
    endTime: Optional[datetime] = None

DestinationConfigurationUnion = Union[DestinationConfiguration, DestinationConfigurationOutput]


# This class is the output for the 'get_composition' function.
class GetCompositionResponse(BaseValidatorModel):
    composition: Composition
    ResponseMetadata: ResponseMetadata


# This class is the output for the 'start_composition' function.
class StartCompositionResponse(BaseValidatorModel):
    composition: Composition
    ResponseMetadata: ResponseMetadata


# This class is the input for the 'start_composition' function.
class StartCompositionRequest(BaseValidatorModel):
    stageArn: str
    destinations: List[DestinationConfigurationUnion]
    idempotencyToken: Optional[str] = None
    layout: Optional[LayoutConfiguration] = None
    tags: Optional[Dict[str, str]] = None